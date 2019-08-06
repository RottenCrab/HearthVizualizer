import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from src.cardpool import builder
from src.apimanager.apifields import APICollectibleFields


# TODO refactor duplicate code (mostly matplotlib stuff)


class CardPoolVisualizer(builder.CardPoolBuilder):
    def __init__(self, card_pool, path_to_plots, save=True):
        super().__init__(card_pool)
        self.path_to_plots = path_to_plots
        self.save = save

    def _distplot(self, data, xlabel, ylabel, plot_title, kde=False, save_fig=True, save_title=None):
        sns.set()
        plt.figure()
        sns.distplot(data[APICollectibleFields.COST], kde=kde,
                     bins=max(data[APICollectibleFields.COST].unique().tolist()),
                     color='Red')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(plot_title)
        if save_fig:
            self.save_plot(save_title)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def annotation():
        pass

    @staticmethod
    def plt_customization():
        pass

    def save_plot(self,
                  plot_title,
                  extension='.png'):
        plt.savefig('{path}{title}{ext}'.format(path=self.path_to_plots,
                                                title=plot_title,
                                                ext=extension), bbox_inches='tight')

    def cost_distribution(self, complete=True, minions=False, spells=False, kde=False):
        if complete:
            self._distplot(self.card_pool,
                           'Mana Cost',
                           'Total Cards',
                           'Cost Distribution: All cards',
                           kde=kde,
                           save_title='cost_distribution_kde_{}'.format(kde))
        if minions:
            self._distplot(self.minions,
                           'Mana Cost',
                           'Total Minions',
                           'Cost Distribution: Minions',
                           kde=kde,
                           save_title='minion_distribution_kde_{}'.format(kde))
        if spells:
            self._distplot(self.spells,
                           'Mana Cost',
                           'Total Spells',
                           'Cost Distribution: Spells',
                           kde=kde,
                           save_title='spell_distribution_kde_{}'.format(kde))

    def generate_countplots(self, adventure=False):
        sns.set(palette='bright')
        xpos = 'center'
        xpos = xpos.lower()
        ha = {'center': 'center',
              'right': 'left',
              'left': 'right'}
        offset = {'center': 0.5,
                  'right': 0.60,  # 0.57
                  'left': 0.45}  # 0.43
        countable_fields = APICollectibleFields.COUNTABLE_FIELDS
        if adventure:
            countable_fields.remove(APICollectibleFields.FACTION)
        for countable in countable_fields:
            plt.figure()
            ax = sns.countplot(x=countable, data=self.card_pool)
            if not np.issubdtype(self.card_pool[countable], np.integer):
                ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
            # Annotate the top of the bars with their corresponding values
            for rect in ax.patches:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.002 * height,
                        '{}'.format(height), ha=ha[xpos], va='bottom', rotation=90, fontsize=11)
            plt.ylim(0, max(self.card_pool[countable].value_counts()) * 1.20)
            plt.xlabel(countable.upper())
            plt.ylabel('counts'.upper())
            plt.title('{} counts'.format(countable).upper())
            if self.save:
                self.save_plot('{}_counts'.format(countable))
        plt.tight_layout()
        plt.show()

    def generate_avg_stats_plot(self):
        ax = sns.barplot(x='MANA_COST', y='STATS', data=self.avg_stats(), hue='TYPE_OF_STATS', palette='seismic')
        xpos = 'center'
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center',
              'right': 'left',
              'left': 'right'}
        offset = {'center': 0.5,
                  'right': 0.60,
                  'left': 0.45}
        # Annotate the top of the bars with their corresponding values
        for rect in ax.patches:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.008 * height,
                    '{}'.format(height), ha=ha[xpos], va='bottom', rotation=90, fontsize=11)
            # Customize plot's Legend
        leg = ax.legend(loc=2)
        leg.set_title('Type of Stats')
        for t, l in zip(leg.texts, ['Average Attack', 'Average Health']):
            t.set_text(l)
        plt.ylim(0, 12)
        plt.xlabel('Mana Cost')
        plt.ylabel('Average Stats')
        plt.title('Average Stats Per Mana Cost')
        sns.despine()
        if self.save:
            self.save_plot('average_stats')
        plt.show()

    def stats_per_race(self):
        sns.set()
        avg_stats = self.avg_stats_by_race()
        races = avg_stats['RACE'].unique().tolist()
        xpos = 'center'
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center',
              'right': 'left',
              'left': 'right'}
        offset = {'center': 0.5,
                  'right': 0.60,
                  'left': 0.45}
        for race in races:
            plt.figure()
            ax = sns.barplot(x='COST', y='STATS', data=avg_stats[avg_stats['RACE'] == race],
                             hue='STATS TYPE', palette='seismic')
            # Annotate the top of the bars with their corresponding values
            for rect in ax.patches:
                height = rect.get_height()
                if height == 0:
                    continue
                ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.008 * height,
                        '{}'.format(height), ha=ha[xpos], va='bottom', rotation=90, fontsize=11)

            leg = ax.legend(loc=2)
            leg.set_title('Type of Stats')
            for t, l in zip(leg.texts, ['Average Attack', 'Average Health']):
                t.set_text(l)
            plt.ylim(0, avg_stats[avg_stats['RACE'] == race]['STATS'].max() + 2)
            plt.xlabel('Mana Cost')
            plt.ylabel('Average Stats')
            plt.title('Average Stats Per Mana Cost: ' + race)
            sns.despine()
            if self.save:
                self.save_plot('avg_stats_{}'.format(race.lower()))
            plt.show()

    def probability_plots(self):
        sns.set(palette='muted')
        ax = sns.barplot(x='cost', y='probability', data=self.probabilities(), hue='mechanics', palette='Set1')
        xpos = 'center'
        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center',
              'right': 'left',
              'left': 'right'}
        offset = {'center': 0.5,
                  'right': 0.60,
                  'left': 0.45}
        # Annotate the top of the bars with their corresponding values
        for rect in ax.patches:
            height = rect.get_height()
            if height == 0:
                continue
            ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.008 * height,
                    '{}%'.format(int(height)), ha=ha[xpos], va='bottom', rotation=90, fontsize=7)
            # Customize plot's Legend
        leg = ax.legend(loc=0)
        leg.set_title('Type of Mechanic')
        plt.ylim(0, self.probabilities()['probability'].max() + 5)
        plt.xlabel('Mana Cost')
        plt.ylabel('Probability')
        plt.title('Taunt, Rush, Charge Probabilities per Cost')
        sns.despine()
        if self.save:
            self.save_plot('probabilities')
        plt.show()
