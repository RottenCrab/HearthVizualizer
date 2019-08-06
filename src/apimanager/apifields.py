class APICollectibleFields:
    ARMOR = 'armor'
    ARTIST = 'artist'
    ATTACK = 'attack'
    CARD_CLASS = 'cardClass'
    CLASSES = 'classes'
    COLLECTIBLE = 'collectible'
    COLLECTION_TEXT = 'collectionText'
    COST = 'cost'
    DBFID = 'dbfId'
    DURABILITY = 'durability'
    ELITE = 'elite'
    ENTOURAGE = 'entourage'
    FACTION = 'faction'
    FLAVOR = 'flavor'
    HEALTH = 'health'
    HIDE_STATS = 'hideStats'
    HOW_T0_EARN = 'howToEarn'
    HOW_TO_EARN_GOLDEN = 'howToEarnGolden'
    ID = 'id'
    MECHANICS = 'mechanics'
    MULTI_CLASS_GROUP = 'multiClassGroup'
    NAME = 'name'
    OVERLOAD = 'overload'
    PLAY_REQUIREMENTS = 'playRequirements'
    QUEST_REWARD = 'questReward'
    RACE = 'race'
    RARITY = 'rarity'
    REFERENCED_TAGS = 'referencedTags'
    SET = 'set'
    SPELL_DAMAGE = 'spellDamage'
    TARGETING_ARROW_TEXT = 'targetingArrowText'
    TEXT = 'text'
    TYPE = 'type'

    CARD_TYPES = {
        'MINION': 'MINION',
        'SPELL': 'SPELL',
        'WEAPON': 'WEAPON',
        'HERO': 'HERO'
    }

    COUNTABLE_FIELDS = [
        COST,
        FACTION,
        RACE,
        RARITY,
        TYPE,
        CARD_CLASS,
        SET
    ]

    def __init__(self):
        pass

    @property
    def all_mechanics(self):
        all_mechanics = ['SECRET',
                         'HEROPOWER_DAMAGE',
                         'RECEIVES_DOUBLE_SPELLDAMAGE_BONUS',
                         'INSPIRE',
                         'BATTLECRY',
                         'DEATHRATTLE',
                         'TRIGGER_VISUAL',
                         'InvisibleDeathrattle',
                         'COMBO',
                         'CHOOSE_ONE',
                         'AURA',
                         'OVERLOAD',
                         'CHARGE',
                         'DIVINE_SHIELD',
                         'FORGETFUL',
                         'SPELLPOWER',
                         'STEALTH',
                         'TAUNT',
                         'CANT_ATTACK',
                         'TOPDECK',
                         'MODULAR',
                         'RUSH',
                         'AFFECTED_BY_SPELL_POWER',
                         'POISONOUS',
                         'LIFESTEAL',
                         'CANT_BE_TARGETED_BY_SPELLS',
                         'CANT_BE_TARGETED_BY_HERO_POWERS',
                         'DISCOVER',
                         'FINISH_ATTACK_SPELL_ON_DAMAGE',
                         'ECHO',
                         'GRIMY_GOONS',
                         'KABAL',
                         'WINDFURY',
                         'JADE_GOLEM',
                         'JADE_LOTUS',
                         'FREEZE',
                         'ENRAGED',
                         'TWINSPELL',
                         'MULTIPLY_BUFF_VALUE',
                         'ADJACENT_BUFF',
                         'SILENCE',
                         'ImmuneToSpellpower',
                         'COLLECTIONMANAGER_FILTER_MANA_EVEN',
                         'START_OF_GAME',
                         'COLLECTIONMANAGER_FILTER_MANA_ODD',
                         'DEATH_KNIGHT',
                         'RITUAL',
                         'OVERKILL',
                         'QUEST']
        return all_mechanics

    @property
    def useful_mechanics(self):
        useful_mechanics = ['TAUNT',
                            'RUSH',
                            'CHARGE']
        return useful_mechanics

    @property
    def common_mechanics(self):
        common_mechanics = ['TAUNT',
                            'RUSH',
                            'BATTLECRY',
                            'DEATHRATTLE',
                            'LIFESTEAL',
                            'MODULAR',
                            'INSPIRE',
                            'DISCOVER',
                            'CHARGE',
                            'WINDFURY',
                            'POISONOUS',
                            'TWINSPELL',
                            'SILENCE',
                            'CANT_ATTACK',
                            'OVERKILL',
                            'DIVINE_SHIELD',
                            'OVERLOAD',
                            'CHOOSE_ONE',
                            'FREEZE',
                            'ECHO',
                            'COMBO',
                            'STEALTH',
                            'SECRET']
        return common_mechanics


class APIAllCardFields:
    """
    This class is here only to demonstrate that in the future I may decide to analyze and plot data from both
    collectible and non collectible cards. But in this time of writing I do not care about non collectible cards
    """
    pass
