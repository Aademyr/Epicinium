'''
File containing pregenerated text parts to use when composing procedural
objects and entities.
'''

'''
These words are categorized so they can be used intelligently when
needed rather than only randomly. They also include as the second element
of their tuple a weight which signifies how likely they are to be used.
'''

NOUNS {
'weapons' : {
    'edged' :   {
        'sword':
            (
            ('sword', 1.5),
            ('blade', 1.5),
            ('saber', 1.0),
            ('backsword', 0.5),
            ('brand', 1.0),
            ('broadsword', 1.0),
            ('claymore', 1.0),
            ('cutlass', 1.0),
            ('epee', 1.0),
            ('falchion', 1.0),
            ('foil', 0.5),
            ('hanger', 0.2),
            ('rapier', 1.0),
            ('sabre', 1.0),
            ('scimitar', 1.0),
            ('toledo', 0.2),
            ('bilbo', 0.2),
            ('curtana', 1.0),
            ('damascus blade', 0.2),
            ('estoc', 1.0),
            ('glaive', 1.0),
            ('scimiter', 1.0),
            ('smallsword', 1.0),
            ('spadroon', 1.0),
            ),
        'axe':
            (
            ('axe', 1.0),
            ('adz', 1.0),
            ('chopper', 0.5),
            ('hatchet', 1.0),
            ('tomahawk', 1.0),
            ),
    },
    'blunt' :   {
        'hammer':
            (
            ('mallet', 1.0),
            ('staff', 1.0),
            ('baton', 1.0),
            ('billy', 1.0),
            ('blackjack', 1.0),
            ('cosh', 1.0),
            ('cudgel', 1.0),
            ('hammer', 2.0),
            ('hickory', 1.0),
            ('mace', 1.0),
            ('nightstick', 1.0),
            ('maul', 2.0),
            ('persuader', 0.5),
            ('sap', 1.0),
            ('shillelagh', 1.0),
            ('truncheon', 1.0),
            ('convincer', 0.2),
            ),
        'staff':
            (
            ('quarterstaff', 1.0),
            ('staff', 1.0),
            ('stick', 1.0),
            ('cane', 1.0),
            ('club', 1.0),
            ('pikestaff', 1.0),
            ('pole', 1.0),
            ('rod', 1.0),
            ('stave', 1.0),
            ('wand', 1.0),
            ('walking stick', 1.0),
            ),
            },
    'whip':   {
            (
            ('whip', 1.0),
            ('cane', 1.0),
            ('belt', 1.0),
            ('birch', 1.0),
            ('cat-o\'-nine-tails', 1.0),
            ('crop', 1.0),
            ('goad', 1.0),
            ('horsewhip', 1.0),
            ('knout', 1.0),
            ('lash', 1.0),
            ('prod', 1.0),
            ('rawhide', 1.0),
            ('scourge', 1.0),
            ('strap', 1.0),
            ('switch', 1.0),
            ('thong', 1.0),
            ('bullwhip', 1.0),
            ),
    },
    'spear' :   {
            (
            ('spear', 1.0),
            ('lance', 1.0),
            ('bayonet', 1.0),
            ('bill', 1.0),
            ('gar', 1.0),
            ('halberd', 1.0),
            ('javelin', 1.0),
            ('lancet', 1.0),
            ('partisan', 1.0),
            ('partizan', 1.0),
            ('pike', 1.0),
            ('bayonet', 1.0),
            ('harpoon', 1.0),
            ('skewer', 1.0),
            ('bolt', 1.0),
            ('bore', 1.0),
            ('javelin', 1.0),
            ('lance', 1.0),
            ('spike', 1.0),
            ('spire', 1.0),
            ('trident', 1.0),
            ),
    },
    'dagger' :   {
        'dagger':
            (
            ('dagger', 1.0),
            ('creese', 1.0),
            ('dirk', 1.0),
            ('kris', 1.0),
            ('knife', 1.0),
            ('bodkin', 1.0),
            ('poniard', 1.0),
            ('stiletto', 1.0),
            ('stylet', 1.0),
            ('switchblade', 1.0),
            ('anlace', 1.0),
            ('skean', 1.0),
            ),
    },
},
'armor': {
    'head':
        (
        ('helmet', 1.0),
        ('helm', 1.0),
        ('headdress', 1.0),
        ('hat', 1.0),
        ('tiara', 1.0),
        ('turban', 1.0),
        ('biretta', 1.0),
        ('bonnet', 1.0),
        ('busby', 1.0),
        ('cap', 1.0),
        ('coiffure', 1.0),
        ('coronet', 1.0),
        ('crown', 1.0),
        ('hood', 1.0),
        ('miter', 1.0),
        ('toque', 1.0),
        ('bandore', 1.0),
        ('headband', 1.0),
        ('chaplet', 1.0),
        ('circlet', 1.0),
        ('coronal', 1.0),
        ('coronet', 1.0),
        ('diadem', 1.0),
        ('garland', 1.0),
        ('wreath', 1.0),
        ('royal crown', 1.0),
        ),
    'body':
        (
        ('breastplate', 1.0),
        ('mail', 1.0),
        ('chainmail', 1.0),
        ('chain armor', 1.0),
        ('coat of mail', 1.0),
        ('mail', 1.0),
        ('ring armor', 1.0),
        ('ring mail', 1.0),
        ('hauberk', 1.0),
        ('chain mail', 1.0),
        ('ring armor', 1.0),
        ('ring mail', 1.0),
        ('suit of armor', 1.0),
        ('chest plate', 1.0),
        ),
    'feet':
        (
        ('tall boots', 2.0),
        ('highboots', 2.0),
        ('galoshes', 1.0),
        ('waders', 1.0),
        ('snow shoes', 0.2),
        ('boots', 2.0),
        ('cleats', 1.0),
        ('loafers', 1.0),
        ('slippers', 1.0),
        ('moccasins', 1.0),
        ('sandals', 1.0),
        ('stiletto heels', 0.3),
        ),
    'offhand':
        'other':
            (
            ('globe', 1.0),
            ('sphere', 1.0),
            ('map', 1.0),
            ('planet', 1.0),
            ('apple', 1.0),
            ('ball', 1.0),
            ('balloon', 1.0),
            ('orb', 1.0),
            ('diamond', 1.0),
            ('gemstone', 1.0),
            ('gem', 1.0),
            ('jewel', 1.0),
            ('rhinestone', 1.0),
            ('rock', 1.0),
            ('zircon', 1.0),
            ('treasure', 1.0),
            ('jewel', 1.0),
            ('jewelry', 1.0),
            ('masterpiece', 1.0),
            ('ornament', 1.0),
            ('stone', 1.0),
            ('bauble', 1.0),
            ('pearl', 1.0),
            ('pick', 1.0),
            ('sparkler', 1.0),
            ('lantern', 1.0),
            ('lamp', 1.0),
            ('beacon', 1.0),
            ('torch', 1.0),
            ('whirlwind', 1.0),
            ('lightning', 1.0),
            ('tornado', 1.0),
            ('soul', 1.0),
            ('spirit', 1.0),
            ('essence', 1.0),
            ('force', 1.0),
            ('shadow', 1.0),
            ('shard', 1.0),
            ('fragment', 1.0),
            ('remnants', 1.0),
            ('scrap', 1.0),
            ('harp', 1.0),
            ('apparatus', 1.0),
            ('device', 1.0),
            ('gadget', 1.0),
            ('gizmo', 1.0),
            ('contraption', 1.0),
            ),
        'shield':
            (
            ('shield', 2.0),
            ('absorber', 1.0),
            ('aegis', 1.0),
            ('buckler', 2.0),
            ('escutcheon', 1.0),
            ('ward', 1.0),
            ('tower shield', 1.0),
            ('kite shield', 1.0),
            ),
        },
}

FIRST_ADJECTIVE {
    ('glowing', 1.0),
    ('brightly burning', 1.0),
    ('flaming', 1.0),
    ('gleaming', 1.0),
    ('luminous', 1.0),
    ('vibrant', 1.0),
    ('red', 1.0),
    ('sanguine', 1.0),
    ('lustrous', 1.0),
    ('phosphorescent', 1.0),
    ('shining', 1.0),
    ('glistening', 1.0),
    ('radiant', 1.0),
    ('shimmering', 1.0),
    ('dark', 1.0),
    ('black', 1.0),
    ('cloudy', 1.0),
    ('dull', 1.0),
    ('misty', 1.0),
    ('shadowy', 1.0),
    ('clouded', 1.0),
    ('grimy', 1.0),
    ('nebulous', 1.0),
    ('pitch-black', 1.0),
    ('sooty', 1.0),
    ('stygian', 1.0),
    ('dark', 1.0),
    ('ghostly', 1.0),
    ('eerie', 1.0),
    ('ghastly', 1.0),
    ('shadowy', 1.0),
    ('spectral', 1.0),
    ('divine', 1.0),
    ('haunted', 1.0),
    ('holy', 1.0),
    ('phantasmal', 1.0),
    ('unearthly', 1.0),
    ('vampiric', 1.0),
    ('spectral', 1.0),
    ('magical', 1.0),
    ('bewitching', 1.0),
    ('enchanted', 1.0),
    ('enchanting', 1.0),
    ('extraordinary', 1.0),
    ('fascinating', 1.0),
    ('magic', 1.0),
    ('marvelous', 1.0),
    ('mysterious', 1.0),
    ('mythical', 1.0),
    ('otherworldly', 1.0),
    ('spellbinding', 1.0),
    ('bewitched', 1.0),
    ('demonic', 1.0),
    ('diabolical', 1.0),
    ('ensorcelled', 1.0),
    ('entrancing', 1.0),
    ('fiendish', 1.0),
    ('necromantic', 1.0),
    ('runic', 1.0),
    ('spellbound', 1.0),
    ('thaumaturgic', 1.0),
    ('charmed', 1.0),
    ('magical', 1.0),
    ('amazing', 1.0),
    ('astonishing', 1.0),
    ('bizarre', 1.0),
    ('curious', 1.0),
    ('exceptional', 1.0),
    ('extraordinary', 1.0),
    ('incredible', 1.0),
    ('phenomenal', 1.0),
    ('remarkable', 1.0),
    ('singular', 1.0),
    ('special', 1.0),
    ('strange', 1.0),
    ('outstanding', 1.0),
    ('unparalleled', 1.0),
    ('fiendish', 1.0),
    ('brutish', 1.0),
    ('nefarious', 1.0),
    ('atrocious', 1.0),
    ('beastly', 1.0),
    ('cruel', 1.0),
    ('demonical', 1.0),
    ('devilish', 1.0),
    ('diabolic', 1.0),
    ('savage', 1.0),
    ('vicious', 1.0),
    ('wicked', 1.0),
    ('shrouded', 1.0),
    ('veiled', 1.0),
    ('enshrouded', 1.0),
    ('inconspicuous', 1.0),
    ('envenomed', 1.0),
}

SPECIAL_DESCRIPTION_ENDINGS {
(
    ('of the Crazed Cleric', 1.0),
    ('of the Crazed Conjurer', 1.0),
    ('of Dwarven craftsmanship', 1.0),
    ('of the Barbaric Wyrm', 1.0),
    ('of the King Breaker', 1.0),
    ('of the Titans', 1.0),
    ('of the Good Queen', 1.0),
    ('of deflection', 1.0),
    ('of the Beast', 1.0),
    ('of Insanity', 1.0),
    ('Fortuitous Soldier\'s Pyramid of Stranglers', 1.0),
    ('Generous Monk\'s Cube of the Hearers\' Charm of Lava', 1.0),
    ('Hellish Yellow Orb of Bronze Hail', 1.0),
    ('Holy Sphere', 1.0),
    ('Jagged Cube of Silver Touches', 1.0),
    ('Keen Cone', 1.0),
    ('Orb of Fine Sea Serpents', 1.0),
    ('Red Sphere of Doomed Infamy', 1.0),
    ('Sylvan Speaker\'s Cone', 1.0),
    ('Unjust Divinity\'s Cube of Crystal Ring', 1.0),
    ('Unjust Monk\'s Orb', 1.0),
    ('Wonderful Animate Cube', 1.0),
    ('Black Gauntlet of the Defender', 1.0),
    ('Chain Mail of Imperial Lineage', 1.0),
    ('Dire Fiery Hauberk of Platinum Blasts', 1.0),
    ('Ethereal Envenomed Quilted Armor', 1.0),
    ('Evil Joiners\' Tower Shield of Dexterity', 1.0),
    ('Green Shield of Distant Cleverness', 1.0),
    ('Haunted Spectres\' Buckler', 1.0),
    ('Intelligent Traveller\'s Shield', 1.0),
    ('Lady\'s Buckler of the Charismatic Beater', 1.0),
    ('Leather Armor of Platinum Cloud', 1.0),
    ('Lost Banded Mail of Influence Conjuration', 1.0),
    ('Mystic Tower Shield', 1.0),
    ('Prismatic Banded Mail', 1.0),
    ('Ring Mail of Bone Barriers', 1.0),
    ('Serene Annihilator\'s Hauberk', 1.0),
    ('Shield of Intoxication', 1.0),
    ('Shooting Breast Plate of Mana Clouds', 1.0),
    ('Studious Traitor\'s Shield', 1.0),
    ('Sylvan Jagged Quilted Armor of Perfect Slime', 1.0),
    ('Tower Shield of Copper and Assailing', 1.0),
    ('Abyssimal Gauntlet of Diamond Lance', 1.0),
    ('Ancient Knights\' Tower Shield of Kill Fish', 1.0),
    ('Armguard of Diamond Lances', 1.0),
    ('Banded Mail of the Elemental Messiah', 1.0),
    ('Blessed Immovable Gauntlet of the Humanoid', 1.0),
    ('Buckler of Diamond Zones', 1.0),
    ('Buckler of Ice Spans', 1.0),
    ('Corrupt Vipers\' Tower Shield', 1.0),
    ('Demonic Snakes\' Tower Shield of the Unspeakable Evocation of Blending', 1.0),
    ('Gauntlet of the Clever King', 1.0),
    ('God\'s Hauberk', 1.0),
    ('Illuminated Ring Mail of Villainous Lightning', 1.0),
    ('Mystical Gauntlet of Intoxication', 1.0),
    ('Mystical Gods\' Quilted Armor', 1.0),
    ('Perfected Serpents\' Buckler', 1.0),
    ('Perfected Shooting Ring Mail', 1.0),
    ('Plate Mail of the Speaker', 1.0),
    ('Tower Shield of the Unknowable Illusion of Invisibility', 1.0),
    ('Unknowable Adamantine Armguard', 1.0),
    ('Unspeakable Yellow Banded Mail', 1.0),
    ('Armguard of Compassion', 1.0),
    ('Blue Greaves of Transform Nondetection', 1.0),
    ('Bracer of Conjure Sneaking', 1.0),
    ('Breast Plate of Greater Mana Shield', 1.0),
    ('Breast Plate of the Lawful Witchery of the Hateful Caretakers', 1.0),
    ('Chain Mail of Dwarven Flesh Barriers', 1.0),
    ('Chain Mail of Mystical Bone Chains', 1.0),
    ('Deadly Spined Breast Plate of Lust Circle', 1.0),
    ('Glorious Undead\'s Tower Shield', 1.0),
    ('Gods\' Armguard', 1.0),
    ('Hauberk of the Ancestral Ritual of Kill Consumer', 1.0),
    ('Hauberk of the Hex of Carnage', 1.0),
    ('Hellish Undead\'s Buckler of the Glamour of Earth', 1.0),
    ('Insane Saint\'s Banded Mail', 1.0),
    ('Leather Armor of Spirit Clouds', 1.0),
    ('Meteoric Shield of Ghost Slaying', 1.0),
    ('Otherworldly Envenomed Chain Mail', 1.0),
    ('Perfected Amazon\'s Armguard of Monsters', 1.0),
    ('Tower Shield of the Screaming Archmagi', 1.0),
    ('Worldly Icy Shield of Acid Beams', 1.0),
}
