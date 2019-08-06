from src.cardpool import counter, visualizer
from src.apimanager import apicalls
from src.reporting import substitutions, reporting_tool
from src.settings import (STANDARD_PLOTS_PATH, WILD_PLOTS_PATH, WILD_EXCLUSIVE_PLOTS_PATH, ARENA_PLOTS_PATH,
                          STANDARD_REPORT_PATH, WILD_REPORT_PATH, WILD_EXCLUSIVE_REPORT_PATH, ARENA_REPORT_PATH,
                          TEMPLATE_PATH, PROJECT_ROOT)


def generate_plots(save=True):
    standard_plots = visualizer.CardPoolVisualizer(apicalls.standard_cards(), STANDARD_PLOTS_PATH, save)
    wild_plots = visualizer.CardPoolVisualizer(apicalls.wild_cards(), WILD_PLOTS_PATH, save)
    wild_exclusive_plots = visualizer.CardPoolVisualizer(apicalls.wild_exclusive_cards(), WILD_EXCLUSIVE_PLOTS_PATH,
                                                         save)
    arena_plots = visualizer.CardPoolVisualizer(apicalls.arena_cards(), ARENA_PLOTS_PATH, save)

    # Generate Standard Plots
    standard_plots.cost_distribution(complete=True, minions=True, spells=True)
    standard_plots.cost_distribution(complete=True, minions=True, spells=True, kde=True)
    standard_plots.generate_countplots()
    standard_plots.generate_avg_stats_plot()
    standard_plots.stats_per_race()
    standard_plots.probability_plots()

    # Generate Wild Plots
    wild_plots.cost_distribution(complete=True, minions=True, spells=True)
    wild_plots.cost_distribution(complete=True, minions=True, spells=True, kde=True)
    wild_plots.generate_countplots()
    wild_plots.generate_avg_stats_plot()
    wild_plots.stats_per_race()
    wild_plots.probability_plots()

    # Generate Wild Exclusive Plots
    wild_exclusive_plots.cost_distribution(complete=True, minions=True, spells=True)
    wild_exclusive_plots.cost_distribution(complete=True, minions=True, spells=True, kde=True)
    wild_exclusive_plots.generate_countplots()
    wild_exclusive_plots.generate_avg_stats_plot()
    wild_exclusive_plots.stats_per_race()
    wild_exclusive_plots.probability_plots()

    # Generate Arena Plots
    arena_plots.cost_distribution(complete=True, minions=True, spells=True)
    arena_plots.cost_distribution(complete=True, minions=True, spells=True, kde=True)
    arena_plots.generate_countplots()
    arena_plots.generate_avg_stats_plot()
    arena_plots.stats_per_race()
    arena_plots.probability_plots()


def generate_reports():
    standard_counter = counter.CardPoolCounter(apicalls.standard_cards())
    standard_regular_cost, standard_golden_cost = standard_counter.crafting_cost()
    wild_counter = counter.CardPoolCounter(apicalls.wild_cards())
    wild_regular_cost, wild_golden_cost = wild_counter.crafting_cost()
    wild_exclusive_counter = counter.CardPoolCounter(apicalls.wild_exclusive_cards())
    wild_exclusive_regular_cost, wild_exclusive_golden_cost = wild_exclusive_counter.crafting_cost()
    arena_counter = counter.CardPoolCounter(apicalls.arena_cards())
    arena_regular_cost, arena_golden_cost = arena_counter.crafting_cost()

    standard_substitutions = substitutions.Substitutions(hearthstone_format='Standard',
                                                         total_cards=standard_counter.total_cards,
                                                         total_spells=standard_counter.total_spells,
                                                         total_minions=standard_counter.total_minions,
                                                         total_weapons=standard_counter.total_weapons,
                                                         crafting_cost_regular=standard_regular_cost,
                                                         crafting_cost_golden=standard_golden_cost,
                                                         cards_per_mechanic=standard_counter.cards_per_mechanic())

    wild_substitutions = substitutions.Substitutions(hearthstone_format='Wild',
                                                     total_cards=wild_counter.total_cards,
                                                     total_spells=wild_counter.total_spells,
                                                     total_minions=wild_counter.total_minions,
                                                     total_weapons=wild_counter.total_weapons,
                                                     crafting_cost_regular=wild_regular_cost,
                                                     crafting_cost_golden=wild_golden_cost,
                                                     cards_per_mechanic=wild_counter.cards_per_mechanic())

    wild_ex_substitutions = substitutions.Substitutions(hearthstone_format='Wild Exclusive',
                                                        total_cards=wild_exclusive_counter.total_cards,
                                                        total_spells=wild_exclusive_counter.total_spells,
                                                        total_minions=wild_exclusive_counter.total_minions,
                                                        total_weapons=wild_exclusive_counter.total_weapons,
                                                        crafting_cost_regular=wild_exclusive_regular_cost,
                                                        crafting_cost_golden=wild_exclusive_golden_cost,
                                                        cards_per_mechanic=wild_exclusive_counter.cards_per_mechanic())

    arena_substitutions = substitutions.Substitutions(hearthstone_format='Arena',
                                                      total_cards=arena_counter.total_cards,
                                                      total_spells=arena_counter.total_spells,
                                                      total_minions=arena_counter.total_minions,
                                                      total_weapons=arena_counter.total_weapons,
                                                      crafting_cost_regular=arena_regular_cost,
                                                      crafting_cost_golden=arena_golden_cost,
                                                      cards_per_mechanic=arena_counter.cards_per_mechanic())

    standard_sub_dict = standard_substitutions.generate_substitutions()
    wild_sub_dict = wild_substitutions.generate_substitutions()
    wild_ex_sub_dict = wild_ex_substitutions.generate_substitutions()
    arena_sub_dict = arena_substitutions.generate_substitutions()
    
    reporting_tool.reporting_tool(standard_sub_dict, PROJECT_ROOT, TEMPLATE_PATH, STANDARD_REPORT_PATH)
    reporting_tool.reporting_tool(wild_sub_dict, PROJECT_ROOT, TEMPLATE_PATH, WILD_REPORT_PATH)
    reporting_tool.reporting_tool(wild_ex_sub_dict, PROJECT_ROOT, TEMPLATE_PATH, WILD_EXCLUSIVE_REPORT_PATH)
    reporting_tool.reporting_tool(arena_sub_dict, PROJECT_ROOT, TEMPLATE_PATH, ARENA_REPORT_PATH)


if __name__ == '__main__':
    generate_plots()
    generate_reports()
