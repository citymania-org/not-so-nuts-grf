import pathlib

from datetime import date

import grf

NUTS_DIR = pathlib.Path('/home/dp/Builds/NUTS')
NUTS_GFX_DIR = NUTS_DIR / 'gfx'
g = grf.NewGRF(
    grfid=b'CMNN',
    name='CityMania Not So NUTS 1.4',
    description='Simplified subset of NUTS train newgrf. Only MEOW engines and no universal wagons. For use with CityMania special event newgrf.',
    version=5,
    min_compatible_version=5,
)
g.strings.import_lang_dir('lang', 'english.txt')
g.set_railtype_table(['RAIL', 'UNI2', 'UNI3', 'UNI4', 'UNI5'])
g.set_cargo_table([
    #  0      1       2       3        4
    'BATT', 'BUBL', 'COLA', 'CTCD', 'FZDR',
    'PLST', 'SWET', 'SUGR', 'TOFF', 'TOYS',  # +5
    'PASS', 'MAIL',                          # +10
])
Train, Define, Switch, VehicleSpriteTable, GenericSpriteLayout = map(g.bind, [grf.Train, grf.Define, grf.Switch, grf.VehicleSpriteTable, grf.GenericSpriteLayout])

g.add(grf.DisableDefault(grf.RV, range(204 - 116)))
DEFAULT_RVS = [
    (122, 'PASS'),
    (131, 'MAIL'),
    (176, 'SUGR'),
    (179, 'COLA'),
    (182, 'CTCD'),
    (185, 'TOFF'),
    (188, 'TOYS'),
    (191, 'SWET'),
    (194, 'BATT'),
    (197, 'FZDR'),
    (200, 'PLST'),
    (203, 'BUBL'),
]
for rvid, cargo in DEFAULT_RVS:
    g.add(grf.Define(
        feature=grf.RV,
        id=rvid - 116,
        props={
            'climates_available': grf.ALL_CLIMATES,
            'default_cargo_type': g.get_cargo_id(cargo),
            'introduction_date': date(1950, 1, 1),
        }
    ))


def tmpl_railflatbed1(is_full, y, func):
    return [
        func(0 + 164 * is_full, 21 * y, 10, 20, xofs=-4, yofs=-14),
        func(11 + 164 * is_full, 21 * y, 20, 16, xofs=-11, yofs=-9),
        func(32 + 164 * is_full, 21 * y, 23, 12, xofs=-6, yofs=-7),
        func(61 + 164 * is_full, 21 * y, 20, 16, xofs=4, yofs=-4),
        func(82 + 164 * is_full, 21 * y, 10, 20, xofs=-4, yofs=-6),
        func(93 + 164 * is_full, 21 * y, 20, 16, xofs=-19, yofs=-5),
        func(114 + 164 * is_full, 21 * y, 23, 12, xofs=-22, yofs=-7),
        func(143 + 164 * is_full, 21 * y, 20, 16, xofs=-4, yofs=-8),
    ]


def tmpl_engine32wtf(x, y, func):
    return [
        func(0 + x, 29 * y, 12, 28, xofs=-5, yofs=-15),
        func(13 + x, 29 * y, 22, 21, xofs=-13, yofs=-13),
        func(36 + x, 29 * y, 32, 16, xofs=-16, yofs=-11),
        func(69 + x, 29 * y, 22, 21, xofs=-5, yofs=-12),
        func(92 + x, 29 * y, 12, 28, xofs=-5, yofs=-15),
        func(105 + x, 29 * y, 22, 21, xofs=-13, yofs=-13),
        func(128 + x, 29 * y, 32, 16, xofs=-16, yofs=-11),
        func(161 + x, 29 * y, 22, 21, xofs=-5, yofs=-12),
    ]


def tmpl_meow_rail_engine(x, y, func):
    return [
        func(0 + 350 * x, y * 90, 12, 44, xofs=-5, yofs=-16),

        func(4 + 9 + 350 * x, y * 90, 42, 31, xofs=-27, yofs=-14),
        func(8 + 48 + 350 * x, y * 90, 68, 16, xofs=-50, yofs=-9),
        func(12 + 113 + 350 * x, y * 90, 42, 31, xofs=-22, yofs=-20),
        func(16 + 152 + 350 * x, y * 90, 12, 44, xofs=-5, yofs=-25),
        func(20 + 161 + 350 * x, y * 90, 42, 31, xofs=-16, yofs=-21),
        func(24 + 200 + 350 * x, y * 90, 68, 16, xofs=-18, yofs=-9),
        func(28 + 265 + 350 * x, y * 90, 42, 31, xofs=-11, yofs=-13),
    ]


def tmpl_meow_rail_tender(x, y, func):
    return [
        func(0 + 350 * x, 90 * y + 45, 12, 28, xofs=-5, yofs=-13),
        func(4 + 9 + 350 * x, 90 * y + 45, 26, 21, xofs=-13, yofs=-11),
        func(8 + 48 + 350 * x, 90 * y + 45, 36, 16, xofs=-18, yofs=-9),
        func(12 + 113 + 350 * x, 90 * y + 45, 26, 21, xofs=-5, yofs=-10),
        func(16 + 152 + 350 * x, 90 * y + 45, 12, 28, xofs=-5, yofs=-12),
        func(20 + 161 + 350 * x, 90 * y + 45, 26, 21, xofs=-16, yofs=-12),
        func(24 + 200 + 350 * x, 90 * y + 45, 36, 16, xofs=-18, yofs=-9),
        func(28 + 265 + 350 * x, 90 * y + 45, 26, 21, xofs=-8, yofs=-10),
    ]


def tmpl_purchase_menu(x, y, func):
    return func(95 * x, 15 * y, 94, 14, xofs=-31, yofs=-8)


def tmpl_express_wagons(x, y, func):
    return [
        func(0 + 184 * x, 29 * y, 12, 28, xofs=-5, yofs=-15),
        func(13 + 184 * x, 29 * y, 22, 21, xofs=-13, yofs=-13),
        func(36 + 184 * x, 29 * y, 32, 16, xofs=-16, yofs=-11),
        func(69 + 184 * x, 29 * y, 22, 21, xofs=-5, yofs=-12),
        func(92 + 184 * x, 29 * y, 12, 28, xofs=-5, yofs=-15),
        func(105 + 184 * x, 29 * y, 22, 21, xofs=-13, yofs=-13),
        func(128 + 184 * x, 29 * y, 32, 16, xofs=-16, yofs=-11),
        func(161 + 184 * x, 29 * y, 22, 21, xofs=-5, yofs=-12),
    ]

# Define(
#     feature=grf.GLOBAL_VAR,
#     id=0,
#     props={'grfid_overrides': (g.grfid, b'HA\x01\x01')}
# )

NUTS_ENGINE_PROPS = {
    'climates_available': grf.ALL_CLIMATES,
    # 'introduction_date': 0,
    'model_life': 255,
    'vehicle_life': 255,
    'reliability_decay': 5,
    'refittable_cargo_classes': 1,
    'refittable_cargo_types': 0,
    'non_refittable_cargo_classes': 0,
    'loading_speed': 5,
    # 'cost_factor': 10,
    'running_cost_factor': 100,
    'sprite_id': 253,
    'max_speed': 358,
    'misc_flags': 10,
    'refit_cost': 0,
    'track_type': g.get_railtype_id('UNI2'),
    'curve_speed_mod': 0,
    'ai_special_flag': 0,
    'power': 10000,
    'running_cost_base': 19504,
    'is_dual_headed': 0,
    'cargo_capacity': 0,
    'weight': 80,
    'extra_weight_per_wagon_high': 0,
    'ai_engine_rank': 0,
    'engine_class': 0,
    'extra_power_per_wagon': 0,
    'tractive_effort_coefficient': 128,
    'air_drag_coefficient': 1,
    'shorten_by': 0,
    'visual_effect_and_powered': 138,
    'extra_weight_per_wagon_low': 0,
    'bitmask_vehicle_info': 0
}

NUTS_TENDER_PROPS = {
    'climates_available': 0,
    'introduction_date': 0,
    'model_life': 255,
    'vehicle_life': 255,
    'reliability_decay': 5,
    'refittable_cargo_classes': 1,
    'refittable_cargo_types': 0,
    'non_refittable_cargo_classes': 0,
    'default_cargo_type': 57,
    'loading_speed': 5,
    'cost_factor': 10,
    'running_cost_factor': 100,
    'sprite_id': 253,
    'max_speed': 995,
    'misc_flags': 14,
    'refit_cost': 0,
    'track_type': g.get_railtype_id('UNI2'),
    'curve_speed_mod': 0,
    'ai_special_flag': 0,
    'power': 1,
    'running_cost_base': 19504,
    'is_dual_headed': 0,
    'cargo_capacity': 0,
    'weight': 80,
    'extra_weight_per_wagon_high': 0,
    'ai_engine_rank': 0,
    'engine_class': 0,
    'extra_power_per_wagon': 0,
    'tractive_effort_coefficient': 255,
    'air_drag_coefficient': 1,
    'shorten_by': 0,
    'visual_effect_and_powered': 202,
    'extra_weight_per_wagon_low': 0,
    'bitmask_vehicle_info': 0
}

ENGINES = [
    {
        'intro_date': date(1950, 1, 1),
        'cost_factor': 20,
        'te': 117,
        'speed': 90,
        'power': 900,
    },
    {
        'intro_date': date(1990, 1, 1),
        'weight': 80,
        'cost_factor': 30,
        'te': 122,
        'speed': 95,
        'power': 1200,
    },
    {
        'intro_date': date(2007, 1, 1),
        'cost_factor': 40,
        'te': 126,
        'speed': 102,
        'power': 1700,
    },
    {
        'intro_date': date(2009, 1, 1),
        'cost_factor': 55,
        'te': 131,
        'speed': 109,
        'power': 2700,
    },
    {
        'intro_date': date(2011, 1, 1),
        'cost_factor': 70,
        'te': 135,
        'speed': 117,
        'power': 3500,
    },
    {
        'intro_date': date(2013, 1, 1),
        'cost_factor': 85,
        'te': 140,
        'speed': 127,
        'power': 4400,
    },
    {
        'intro_date': date(2015, 1, 1),
        'cost_factor': 100,
        'te': 144,
        'speed': 139,
        'power': 5200,
    },
    {
        'intro_date': date(2017, 1, 1),
        'cost_factor': 120,
        'te': 149,
        'speed': 151,
        'power': 6100,
    },
    {
        'intro_date': date(2020, 1, 1),
        'cost_factor': 140,
        'te': 153,
        'speed': 168,
        'power': 7000,
    },
]

meow_rail_png = grf.ImageFile(NUTS_GFX_DIR / 'MEOW_RAIL.png')
meow_purchase_png = grf.ImageFile(NUTS_GFX_DIR / 'PurchaseMenu.png')
for generation, data in enumerate(ENGINES):
    sprite_table = VehicleSpriteTable(grf.TRAIN)
    engine_layouts, tender_layouts = [], []
    for i in range(5):
        row_id = sprite_table.add_row(tmpl_meow_rail_engine(generation, i, lambda *args, **kw: grf.FileSprite(meow_rail_png, *args, **kw, bpp=8)))
        engine_layouts.append(sprite_table.get_layout(row_id))
        row_id = sprite_table.add_row(tmpl_meow_rail_tender(generation, i, lambda *args, **kw: grf.FileSprite(meow_rail_png, *args, **kw, bpp=8)))
        tender_layouts.append(sprite_table.get_layout(row_id))
    row_id = sprite_table.add_purchase_graphics(tmpl_purchase_menu(6, generation, lambda *args, **kw: grf.FileSprite(meow_purchase_png, *args, **kw, bpp=8)))
    purchase_layout = sprite_table.get_layout(row_id)

    engine_graphics_switch = Switch(
        related_scope=False,
        ranges={
            g.get_railtype_id(rt): sprite
            for sprite, rt in zip(engine_layouts, ('RAIL', 'UNI2', 'UNI3', 'UNI4', 'UNI5'))
        },
        default=engine_layouts[0],
        code='current_railtype',
    )

    tender_graphics_switch = Switch(
        related_scope=False,
        ranges={
            g.get_railtype_id(rt): sprite
            for sprite, rt in zip(tender_layouts, ('RAIL', 'UNI2', 'UNI3', 'UNI4', 'UNI5'))
        },
        default=tender_layouts[0],
        code='current_railtype',
    )

    base_te = data['te']
    base_power = data['power']
    base_speed = data['speed']
    # ranges={9: Ref(195), b: Ref(185), d: CB(100), 16: CB(80), 1f: Ref(38)},
    properties_switch = grf.Switch(
        related_scope=False,
        ranges={
            0x1f: Switch(
                related_scope=False,
                ranges={
                    g.get_railtype_id('RAIL'): base_te,
                    g.get_railtype_id('UNI2'): base_te * 13 // 10,
                    g.get_railtype_id('UNI5'): base_te * 11 // 10,
                },
                default=base_te,
                code='current_railtype',
            ),
            0x09: Switch(
                related_scope=False,
                ranges={
                    g.get_railtype_id('RAIL'): base_speed,
                    g.get_railtype_id('UNI3'): base_speed * 13 // 10,
                    g.get_railtype_id('UNI5'): base_speed * 11 // 10,
                },
                default=base_speed,
                code='current_railtype',
            ),
            0x0b: Switch(
                related_scope=False,
                ranges={
                    g.get_railtype_id('RAIL'): base_power,
                    g.get_railtype_id('UNI4'): base_power * 13 // 10,
                    g.get_railtype_id('UNI5'): base_power * 11 // 10,
                },
                default=base_power,
                code='current_railtype',
            )
        },
        default=engine_layouts[0],
        code='extra_callback_info1_byte',
    )

    t = Train(
        id=801 + generation,
        name=g.strings[f'STR_NAME_MEOW_rail_0{generation + 1}'],
        callbacks={
            'graphics': grf.GraphicsCallback(engine_graphics_switch, purchase_layout),
            'change_properties': properties_switch,
        },
        **NUTS_ENGINE_PROPS,
        introduction_date=data['intro_date'],
        cost_factor=data['cost_factor'],
        additional_text=g.strings['STR_MEOW_PURCHASE_TEXT'],
    ).add_articulated_part(
        id=781 + generation,
        callbacks={
            'graphics': tender_graphics_switch,
        },
        skip_props_check=True,
        **NUTS_TENDER_PROPS,
    )


WAGONS = [
    {
        'name': 'Passenger Carriage',
        'graphics': ('default3', 8),
        'cargo': 'PASS',
        'cost': 247,
        'weight': 25,
        'capacity': 40,
    }, {
        'name': 'Mail Van',
        'graphics': ('default3', 9),
        'cargo': 'MAIL',
        'cost': 228,
        'weight': 21,
        'capacity': 30,
    }, {
        'name': 'Sugar Hopper',
        'graphics': ('hopper3', 14),
        'cargo': 'SUGR',
        'cost': 176,
        'weight': 19,
        'capacity': 30,
    }, {
        'name': 'Candyfloss Hopper',
        'graphics': ('hopper3', 1),
        'cargo': 'CTCD',
        'cost': 178,
        'weight': 20,
        'capacity': 30,
    }, {
        'name': 'Toffee Hopper',
        'graphics': ('hopper3', 15),
        'cargo': 'TOFF',
        'cost': 192,
        'weight': 20,
        'capacity': 30,
    }, {
        'name': 'Bubble Truck',
        'cargo': 'BUBL',
        'graphics': ('flatbed3', 2),
        'cost': 190,
        'weight': 21,
        'capacity': 30,
    }, {
        'name': 'Cola Tanker',
        'cargo': 'COLA',
        'graphics': ('tanker3', 0),
        'cost': 182,
        'weight': 24,
        'capacity': 25,
    }, {
        'name': 'Sweet Truck',
        'cargo': 'SWET',
        'graphics': ('flatbed3', 14),
        'cost': 181,
        'weight': 21,
        'capacity': 25,
    }, {
        'name': 'Toy Truck',
        'cargo': 'TOYS',
        'graphics': ('flatbed3', 15),
        'cost': 183,
        'weight': 21,
        'capacity': 20,
    }, {
        'name': 'Battery Truck',
        'cargo': 'BATT',
        'graphics': ('flatbed3', 1),
        'cost': 196,
        'weight': 18,
        'capacity': 22,
    }, {
        'name': 'Fizzy Drink Truck',
        'cargo': 'FZDR',
        'graphics': ('flatbed3', 3),
        'cost': 193,
        'weight': 18,
        'capacity': 25,
    }, {
        'name': 'Plastic Tanker',
        'cargo': 'PLST',
        'graphics': ('tanker3', 7),
        'cost': 191,
        'weight': 18,
        'capacity': 30,
    },
]

flatbed1_png = grf.ImageFile(NUTS_GFX_DIR / 'RailWagons_1st_Flatbed.png')
flatbed2_png = grf.ImageFile(NUTS_GFX_DIR / 'RailWagons_2nd_Flatbed.png')
flatbed3_png = grf.ImageFile(NUTS_GFX_DIR / 'RailWagons_3rd_Flatbed.png')
hopper2_png = grf.ImageFile(NUTS_GFX_DIR / 'RailWagons_2nd_Hopper.png')
hopper3_png = grf.ImageFile(NUTS_GFX_DIR / 'RailWagons_3rd_Hopper.png')
tanker2_png = grf.ImageFile(NUTS_GFX_DIR / 'RailWagons_2nd_Tanker.png')
tanker3_png = grf.ImageFile(NUTS_GFX_DIR / 'RailWagons_3rd_Tanker.png')
express_png = grf.ImageFile(NUTS_GFX_DIR / 'EXPRESS_wagons.png')


def get_flatbed1_sprites():
    return tmpl_railflatbed1(0, 26, lambda *args, **kw: grf.FileSprite(flatbed1_png, *args, **kw, bpp=8))


def get_flatbed2_sprites():
    return tmpl_engine32wtf(0, 0, lambda *args, **kw: grf.FileSprite(flatbed2_png, *args, **kw, bpp=8))


def get_wtf32_sprites(png, cargo, stage):
    assert 0 <= stage < 4, stage
    x, y = 0, cargo * 2
    if 0 < stage < 3:
        y += 1
    if stage > 2:
        x += 184
    return tmpl_engine32wtf(x, y, lambda *args, **kw: grf.FileSprite(png, *args, **kw, bpp=8))


def get_default1_sprites(cargo):
    return tmpl_express_wagons(cargo, 0, lambda *args, **kw: grf.FileSprite(express_png, *args, **kw, bpp=8))


def get_default2_sprites(cargo):
    return tmpl_express_wagons(cargo, 2, lambda *args, **kw: grf.FileSprite(express_png, *args, **kw, bpp=8))


def get_default3_sprites(cargo):
    return tmpl_express_wagons(cargo, 4, lambda *args, **kw: grf.FileSprite(express_png, *args, **kw, bpp=8))


for i, data in enumerate(WAGONS):
    grtype, grcargo = data['graphics']

    if grtype.startswith('default'):
        if grtype == 'default1':
            sprite_getter = get_default1_sprites
        elif grtype == 'default2':
            sprite_getter = get_default2_sprites
        elif grtype == 'default3':
            sprite_getter = get_default3_sprites
        sprite_table = VehicleSpriteTable(grf.TRAIN)
        layout = sprite_table.get_layout(sprite_table.add_row(sprite_getter(grcargo)))
        purchase_layout = layout
    else:
        if grtype == 'flatbed3':
            def sprite_getter(stage):
                return get_wtf32_sprites(flatbed3_png, grcargo, stage)
        elif grtype == 'hopper2':
            def sprite_getter(stage):
                return get_wtf32_sprites(hopper2_png, grcargo, stage)
        elif grtype == 'hopper3':
            def sprite_getter(stage):
                return get_wtf32_sprites(hopper3_png, grcargo, stage)
        elif grtype == 'tanker2':
            def sprite_getter(stage):
                return get_wtf32_sprites(tanker2_png, grcargo, stage)
        elif grtype == 'tanker3':
            def sprite_getter(stage):
                return get_wtf32_sprites(tanker3_png, grcargo, stage)
        else:
            raise ValueError(grtype)

        rows = [sprite_table.add_row(sprite_getter(i)) for i in range(4)]
        layout = grf.GenericSpriteLayout(
            feature=grf.TRAIN,
            ent1=rows,
            ent2=rows,
        )
        purchase_layout = sprite_table.get_layout(sprite_table.add_row(sprite_getter(3)))

    cargo_id = g.get_cargo_id(data['cargo'])
    Train(
        id=4000 + i,
        name=data['name'],
        engine_class=Train.EngineClass.STEAM,
        max_speed=0,
        power=0,
        # introduction_date=date(1900, 1, 1),
        introduction_date=0,
        loading_speed=5,
        weight=data['weight'],
        tractive_effort_coefficient=0,
        vehicle_life=255,
        model_life=255,
        climates_available=grf.ALL_CLIMATES,
        running_cost_factor=0,
        cargo_capacity=data['capacity'],
        default_cargo_type=cargo_id,
        cost_factor=data['cost'],
        refittable_cargo_types=0,
        visual_effect_and_powered=202,
        track_type=g.get_railtype_id('UNI2'),
        callbacks={
            'graphics': grf.GraphicsCallback(layout, purchase_layout),
        }
    )

g.write('notsonuts.grf')
