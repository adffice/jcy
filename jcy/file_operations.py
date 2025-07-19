import csv
import json
import json5
import os
import shutil
import re
from jcy_model import FeatureConfig

class FileOperations:

    UE01A = ""

    """
    负责处理所有文件相关的操作，如复制和删除。
    """
    def __init__(self, config: FeatureConfig):
        self.config = config
        self.dir_mod = config.dir_mod

    def common_encode_private_use_chars(self, text):
        r"""
        替换所有私用区字符为 \uXXXX 形式
        """
        def repl(m):
            return '\\u%04X' % ord(m.group(0))
        return re.sub(r'[\uE000-\uF8FF]', repl, text)

    def common_empty_file(self, files: list, isEnabled: bool):
        """
        公共方法 遍历处理files列表
        True: 创建 文件名 空文件
        False: 删除 文件名文件
        """
        count = 0

        for file in files:
            target_file = os.path.join(self.dir_mod, file)
            try:
                if isEnabled:
                    with open(target_file, 'w') as f:
                        pass
                else:
                    os.remove(target_file)
                count += 1
            except Exception as e:
                print(e);

        return (count, len(files))
    
    def common_rename(self, files: list, isEnabled: bool):
        """
        公共方法 遍历处理files列表
        True: 文件名.tmp -> 文件名
        False: 文件名 -> 文件名.tmp
        """
        count = 0
        for file in files:
            try:
                target_file = os.path.join(self.dir_mod, file)
                temp_file = target_file + ".tmp"
                os.replace(temp_file, target_file) if isEnabled else os.replace(target_file, temp_file)
                count += 1
            except Exception as e:
                print(e)

        return (count, len(files))
    
    def common_swap(self, files: list, isEnabled: bool):
        """
        公共方法 遍历处理files列表
        True files[0] -> files[2]
        False files[1] -> files[2]
        """
        count = 0
        total = len(files)

        for file in files:
            try:
                true_file = os.path.join(self.dir_mod, file[0]) 
                false_file = os.path.join(self.dir_mod, file[1]) 
                target_file = os.path.join(self.dir_mod, file[2])
                shutil.copy2(true_file if isEnabled else false_file, target_file)
                count += 1
            except Exception as e:
                print(e)
        return (count, total)

    def toggle_mini_cube(self, isEnabled: bool):
        """
        INI方块
        """
        files_mini_cube = (
            r"data/global/ui/layouts/minihoradriccubelayouthd.json",
            r"data/global/ui/layouts/minihoradriccubelayout.json",
        )

        return self.common_rename(files_mini_cube, isEnabled)

    def toggle_droped_highlight(self, isEnabled: bool):
        """
        开关 掉落光柱
        """
        files_droped_highlight = (
            r"data/hd/items/misc/charm/charm_large.json",
            r"data/hd/items/misc/charm/charm_small.json",
            r"data/hd/items/misc/gem/perfect_diamond.json",
            r"data/hd/items/misc/rune/ber_rune.json",
            r"data/hd/items/misc/rune/cham_rune.json",
            r"data/hd/items/misc/rune/gul_rune.json",
            r"data/hd/items/misc/rune/ist_rune.json",
            r"data/hd/items/misc/rune/jah_rune.json",
            r"data/hd/items/misc/rune/lem_rune.json",
            r"data/hd/items/misc/rune/lo_rune.json",
            r"data/hd/items/misc/rune/mal_rune.json",
            r"data/hd/items/misc/rune/ohm_rune.json",
            r"data/hd/items/misc/rune/pul_rune.json",
            r"data/hd/items/misc/rune/sur_rune.json",
            r"data/hd/items/misc/rune/um_rune.json",
            r"data/hd/items/misc/rune/vex_rune.json",
            r"data/hd/items/misc/rune/zod_rune.json",
            r"data/hd/items/misc/key/mephisto_key.json",
        )

        return self.common_rename(files_droped_highlight, isEnabled)

    def toggle_chest_highlight(self, isEnabled: bool):
        """
        开关 箱子高亮
        """
        files_chest_highlight = (
            r"data/hd/objects/armor_weapons/armor_stand_1.json",
            r"data/hd/objects/armor_weapons/armor_stand_2.json",
            r"data/hd/objects/armor_weapons/armor_stand_left.json",
            r"data/hd/objects/armor_weapons/armor_stand_right.json",
            r"data/hd/objects/armor_weapons/weapon_rack_1.json",
            r"data/hd/objects/armor_weapons/weapon_rack_2.json",
            r"data/hd/objects/armor_weapons/weapon_rack_left.json",
            r"data/hd/objects/armor_weapons/weapon_rack_right.json",
            r"data/hd/objects/caskets/act_3_dungeon_casket.json",
            r"data/hd/objects/caskets/arcane_casket_1.json",
            r"data/hd/objects/caskets/baal_tomb_1.json",
            r"data/hd/objects/caskets/baal_tomb_2.json",
            r"data/hd/objects/caskets/baal_tomb_3.json",
            r"data/hd/objects/caskets/casket_1.json",
            r"data/hd/objects/caskets/casket_2.json",
            r"data/hd/objects/caskets/casket_3.json",
            r"data/hd/objects/caskets/casket_4.json",
            r"data/hd/objects/caskets/casket_5.json",
            r"data/hd/objects/caskets/casket_6.json",
            r"data/hd/objects/caskets/desert_coffin.json",
            r"data/hd/objects/caskets/ground_tomb.json",
            r"data/hd/objects/caskets/mummy_casket.json",
            r"data/hd/objects/caskets/tomb_act_2.json",
            r"data/hd/objects/caskets/tomb_baal_1.json",
            r"data/hd/objects/caskets/tomb_baal_2.json",
            r"data/hd/objects/caskets/tomb_baal_3.json",
            r"data/hd/objects/caskets/tomb_baal_4.json",
            r"data/hd/objects/caskets/tomb_baal_5.json",
            r"data/hd/objects/caskets/tomb_baal_6.json",
            r"data/hd/objects/caskets/tomb_baal_7.json",
            r"data/hd/objects/caskets/tomb_baal_8.json",
            r"data/hd/objects/caskets/tomb_baal_9.json",
            r"data/hd/objects/caskets/yet_another_tomb.json",
            r"data/hd/objects/characters/burned_body_1_act_1.json",
            r"data/hd/objects/characters/corpse_1_act_3.json",
            r"data/hd/objects/characters/corpse_2_act_3.json",
            r"data/hd/objects/characters/corpse_3.json",
            r"data/hd/objects/characters/corpse_skeleton.json",
            r"data/hd/objects/characters/damned_v_1.json",
            r"data/hd/objects/characters/damned_v_2.json",
            r"data/hd/objects/characters/dead_barbarian.json",
            r"data/hd/objects/characters/dead_palace_guard.json",
            r"data/hd/objects/characters/dead_person.json",
            r"data/hd/objects/characters/dead_person_again.json",
            r"data/hd/objects/characters/dungeon_guy.json",
            r"data/hd/objects/characters/guard_corpse_2_act_2.json",
            r"data/hd/objects/characters/guard_on_a_stick.json",
            r"data/hd/objects/characters/harem_guard_1.json",
            r"data/hd/objects/characters/harem_guard_2.json",
            r"data/hd/objects/characters/harem_guard_3.json",
            r"data/hd/objects/characters/harem_guard_4.json",
            r"data/hd/objects/characters/jack_in_the_box_1.json",
            r"data/hd/objects/characters/jack_in_the_box_2.json",
            r"data/hd/objects/characters/rogue_corpse_1.json",
            r"data/hd/objects/characters/rogue_corpse_2.json",
            r"data/hd/objects/characters/rogue_rolling_corpse_1.json",
            r"data/hd/objects/characters/rogue_staked_corpse_1.json",
            r"data/hd/objects/characters/rogue_staked_corpse_2.json",
            r"data/hd/objects/characters/sewer_dungeon_body.json",
            r"data/hd/objects/characters/wirt.json",
            r"data/hd/objects/characters/yet_another_dead_body.json",
            r"data/hd/objects/chests/arcane_chest_1.json",
            r"data/hd/objects/chests/arcane_chest_2.json",
            r"data/hd/objects/chests/arcane_chest_3.json",
            r"data/hd/objects/chests/arcane_chest_4.json",
            r"data/hd/objects/chests/chest_1_b.json",
            r"data/hd/objects/chests/chest_2.json",
            r"data/hd/objects/chests/chest_2_b.json",
            r"data/hd/objects/chests/chest_3.json",
            r"data/hd/objects/chests/chest_3_b.json",
            r"data/hd/objects/chests/chest_4.json",
            r"data/hd/objects/chests/chest_5.json",
            r"data/hd/objects/chests/chest_6.json",
            r"data/hd/objects/chests/chest_7.json",
            r"data/hd/objects/chests/chest_8.json",
            r"data/hd/objects/chests/chest_burial_r.json",
            r"data/hd/objects/chests/chest_bur_i_all.json",
            r"data/hd/objects/chests/chest_outdoor_1.json",
            r"data/hd/objects/chests/chest_outdoor_2.json",
            r"data/hd/objects/chests/chest_outdoor_3.json",
            r"data/hd/objects/chests/chest_outdoor_4.json",
            r"data/hd/objects/chests/cloth_chest_l.json",
            r"data/hd/objects/chests/cloth_chest_r.json",
            r"data/hd/objects/chests/consolation_chest.json",
            r"data/hd/objects/chests/forgotten_tower_chest.json",
            r"data/hd/objects/chests/jungle_chest.json",
            r"data/hd/objects/chests/jungle_chest_2.json",
            r"data/hd/objects/chests/large_chest_l.json",
            r"data/hd/objects/chests/large_chest_r.json",
            r"data/hd/objects/chests/sewer_chest.json",
            r"data/hd/objects/chests/sewer_chest_large_left.json",
            r"data/hd/objects/chests/sewer_chest_med_right.json",
            r"data/hd/objects/chests/sewer_chest_tall_left.json",
            r"data/hd/objects/chests/sewer_chest_tall_right.json",
            r"data/hd/objects/chests/snow_chest_l.json",
            r"data/hd/objects/chests/snow_chest_r.json",
            r"data/hd/objects/chests/snow_cloth_chest_l.json",
            r"data/hd/objects/chests/snow_cloth_chest_r.json",
            r"data/hd/objects/chests/snow_wood_chest_l.json",
            r"data/hd/objects/chests/snow_wood_chest_r.json",
            r"data/hd/objects/chests/special_chest_100.json",
            r"data/hd/objects/chests/tomb_chest_1.json",
            r"data/hd/objects/chests/tomb_chest_2.json",
            r"data/hd/objects/chests/travincal_chest_large_left.json",
            r"data/hd/objects/chests/travincal_chest_large_right.json",
            r"data/hd/objects/chests/travincal_chest_med_left.json",
            r"data/hd/objects/chests/travincal_chest_med_right.json",
            r"data/hd/objects/chests/wood_chest_l.json",
            r"data/hd/objects/chests/wood_chest_r.json",
            r"data/hd/objects/destructibles/barrel.json",
            r"data/hd/objects/destructibles/barrel_3.json",
            r"data/hd/objects/destructibles/barrel_exploding.json",
            r"data/hd/objects/destructibles/basket_1.json",
            r"data/hd/objects/destructibles/basket_2.json",
            r"data/hd/objects/destructibles/box_1.json",
            r"data/hd/objects/destructibles/box_2.json",
            r"data/hd/objects/destructibles/crate.json",
            r"data/hd/objects/destructibles/dungeon_basket.json",
            r"data/hd/objects/destructibles/dungeon_rock_pile.json",
            r"data/hd/objects/destructibles/exploding_chest_100.json",
            r"data/hd/objects/destructibles/e_jar_1.json",
            r"data/hd/objects/destructibles/e_jar_2.json",
            r"data/hd/objects/destructibles/e_jar_3.json",
            r"data/hd/objects/destructibles/ice_cave_evil_urn.json",
            r"data/hd/objects/destructibles/ice_cave_jar_1.json",
            r"data/hd/objects/destructibles/ice_cave_jar_2.json",
            r"data/hd/objects/destructibles/ice_cave_jar_3.json",
            r"data/hd/objects/destructibles/ice_cave_jar_4.json",
            r"data/hd/objects/destructibles/ice_cave_jar_5.json",
            r"data/hd/objects/destructibles/jug_outdoor_1.json",
            r"data/hd/objects/destructibles/jug_outdoor_2.json",
            r"data/hd/objects/destructibles/pillar_2.json",
            r"data/hd/objects/destructibles/urn_1.json",
            r"data/hd/objects/destructibles/urn_2.json",
            r"data/hd/objects/destructibles/urn_3.json",
            r"data/hd/objects/destructibles/urn_4.json",
            r"data/hd/objects/destructibles/urn_5.json",
            r"data/hd/objects/env_manmade/barrel_2.json",
            r"data/hd/objects/env_manmade/bookshelf_1.json",
            r"data/hd/objects/env_manmade/bookshelf_2.json",
            r"data/hd/objects/env_manmade/compelling_orb.json",
            r"data/hd/objects/env_manmade/hole_in_ground.json",
            r"data/hd/objects/env_organic/cocoon_1.json",
            r"data/hd/objects/env_organic/cocoon_2.json",
            r"data/hd/objects/env_organic/goo_pile.json",
            r"data/hd/objects/env_organic/sewer_rat_nest.json",
            r"data/hd/objects/env_pillars/ancients_altar.json",
            r"data/hd/objects/env_pillars/ice_cave_object_1.json",
            r"data/hd/objects/env_pillars/inside_altar.json",
            r"data/hd/objects/env_pillars/jungle_pillar_0.json",
            r"data/hd/objects/env_pillars/jungle_pillar_1.json",
            r"data/hd/objects/env_pillars/jungle_pillar_2.json",
            r"data/hd/objects/env_pillars/jungle_pillar_3.json",
            r"data/hd/objects/env_pillars/mephisto_pillar_1.json",
            r"data/hd/objects/env_pillars/mephisto_pillar_2.json",
            r"data/hd/objects/env_pillars/mephisto_pillar_3.json",
            r"data/hd/objects/env_pillars/obelisk_1.json",
            r"data/hd/objects/env_pillars/obelisk_2.json",
            r"data/hd/objects/env_pillars/object_1_temple.json",
            r"data/hd/objects/env_pillars/object_2_temple.json",
            r"data/hd/objects/env_pillars/snowy_generic_name.json",
            r"data/hd/objects/env_pillars/steeg_stone.json",
            r"data/hd/objects/env_pillars/stone_stash.json",
            r"data/hd/objects/env_pillars/tower_tome.json",
            r"data/hd/objects/env_skeletons/e_shit.json",
            r"data/hd/objects/env_skeletons/hell_bone_pile.json",
            r"data/hd/objects/env_skeletons/inner_hell_object_1.json",
            r"data/hd/objects/env_skeletons/inner_hell_object_2.json",
            r"data/hd/objects/env_skeletons/inner_hell_object_3.json",
            r"data/hd/objects/env_skeletons/outer_hell_object_1.json",
            r"data/hd/objects/env_skeletons/outer_hell_skeleton.json",
            r"data/hd/objects/env_skeletons/skull_pile.json",
            r"data/hd/objects/env_stone/hidden_stash.json",
            r"data/hd/objects/env_stone/rock.json",
            r"data/hd/objects/env_stone/rock_c.json",
            r"data/hd/objects/env_stone/rock_d.json",
            r"data/hd/objects/env_wood/log.json",
        )

        return self.common_rename(files_chest_highlight, isEnabled)

    def toggle_roomtiles_arrow(self, isEnabled: bool):
        """
        开关 入口八方箭头
        """
        files_entrance_arrow = (
            r"data/hd/objects/env_pillars/Arcane_tome.json",
            r"data/hd/objects/env_pillars/Seven_tombs_receptacle.json",
            r"data/hd/objects/env_stone/Stone_alpha.json",
            r"data/hd/objects/env_wood/inifuss_tree.json",
            r"data/hd/roomtiles/act_1_catacombs_down.json",
            r"data/hd/roomtiles/act_1_crypt_down.json",
            r"data/hd/roomtiles/act_1_jail_down.json",
            r"data/hd/roomtiles/act_1_jail_up.json",
            r"data/hd/roomtiles/act_1_wilderness_to_cave_cliff_l.json",
            r"data/hd/roomtiles/act_1_wilderness_to_cave_cliff_r.json",
            r"data/hd/roomtiles/act_1_wilderness_to_cave_floor_l.json",
            r"data/hd/roomtiles/act_1_wilderness_to_cave_floor_r.json",
            r"data/hd/roomtiles/act_1_wilderness_to_tower.json",
            r"data/hd/roomtiles/act_2_desert_to_lair.json",
            r"data/hd/roomtiles/act_2_desert_to_sewer_trap.json",
            r"data/hd/roomtiles/act_2_desert_to_tomb_l_1.json",
            r"data/hd/roomtiles/act_2_desert_to_tomb_l_2.json",
            r"data/hd/roomtiles/act_2_desert_to_tomb_r_1.json",
            r"data/hd/roomtiles/act_2_desert_to_tomb_r_2.json",
            r"data/hd/roomtiles/act_2_desert_to_tomb_viper.json",
            r"data/hd/roomtiles/act_2_lair_down.json",
            r"data/hd/roomtiles/act_2_sewer_down.json",
            r"data/hd/roomtiles/act_2_tomb_down.json",
            r"data/hd/roomtiles/act_3_dungeon_down.json",
            r"data/hd/roomtiles/act_3_jungle_to_dungeon_fort.json",
            r"data/hd/roomtiles/act_3_jungle_to_dungeon_hole.json",
            r"data/hd/roomtiles/act_3_jungle_to_spider.json",
            r"data/hd/roomtiles/act_3_kurast_to_temple.json",
            r"data/hd/roomtiles/act_3_mephisto_down_l.json",
            r"data/hd/roomtiles/act_3_mephisto_down_r.json",
            r"data/hd/roomtiles/act_3_sewer_down.json",
            r"data/hd/roomtiles/act_4_mesa_to_lava.json",
            r"data/hd/roomtiles/act_5_baal_temple_down_l.json",
            r"data/hd/roomtiles/act_5_baal_temple_down_r.json",
            r"data/hd/roomtiles/act_5_barricade_down_wall_l.json",
            r"data/hd/roomtiles/act_5_barricade_down_wall_r.json",
            r"data/hd/roomtiles/act_5_ice_caves_down_floor.json",
            r"data/hd/roomtiles/act_5_ice_caves_down_l.json",
            r"data/hd/roomtiles/act_5_ice_caves_down_r.json",
            r"data/hd/roomtiles/act_5_temple_down.json",
        )

        return self.common_rename(files_entrance_arrow, isEnabled)

    def toggle_waypoint_arrow(self, isEnabled: bool):
        """
        开关 小站八方箭头
        """
        files_entrance_arrow = (
            r"data/hd/objects/waypoint_portals/sewer_waypoint.json",
            r"data/hd/objects/waypoint_portals/temple_waypoint.json",
            r"data/hd/objects/waypoint_portals/travincal_waypoint.json",
            r"data/hd/objects/waypoint_portals/waypoint_act_2.json",
            r"data/hd/objects/waypoint_portals/waypoint_act_3.json",
            r"data/hd/objects/waypoint_portals/waypoint_baal.json",
            r"data/hd/objects/waypoint_portals/waypoint_cellar.json",
            r"data/hd/objects/waypoint_portals/waypoint_exp.json",
            r"data/hd/objects/waypoint_portals/waypoint_ice_cave.json",
            r"data/hd/objects/waypoint_portals/waypoint_inside_act_1.json",
            r"data/hd/objects/waypoint_portals/waypoint_outside_act_1.json",
            r"data/hd/objects/waypoint_portals/waypoint_outside_act_4.json",
            r"data/hd/objects/waypoint_portals/waypoint_wilderness.json",
        )

        return self.common_rename(files_entrance_arrow, isEnabled)

    def toggle_low_quality(self, isEnabled: bool):
        """
        屏蔽 劣等的/損壞的/破舊的 武器装备
        """
        paths = [
            r"data/local/lng/strings/ui.json",
        ]

        count = 0
        total = len(paths)
        for path in paths:
            target_path = os.path.join(self.dir_mod, path)
            temp_path = target_path + ".tmp"
            try:
                # 1.load
                json_data = None
                with open(target_path, 'r', encoding='utf-8-sig') as f:
                    json_data = json.load(f)

                # 2.modify
                for i, item in enumerate(json_data):
                    if item["id"] == 1712:
                        item["enUS"] = "" if isEnabled else "%0%1"
                        item["zhTW"] = "" if isEnabled else "%0%1"
                        item["zhCN"] = "" if isEnabled else "%0%1"
                
                # 3. dump & encode
                json_string = json.dumps(json_data, ensure_ascii=False, indent=2)
                json_string = self.common_encode_private_use_chars(json_string)

                # 4.write
                with open(temp_path, 'w', encoding="utf-8-sig") as f:
                    f.write(json_string)

                # 5.replace
                os.replace(temp_path, target_path)
                count += 1
            except Exception as e:
                print(e)
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        return (count, total)

    def toggle_no_mosaic_sin(self, isEnabled: bool):
        """
        开关 马赛克护眼
        """
        files_no_mosaic_sin = (
            r"data/hd/missiles/ground_fire_medium.json",
            r"data/hd/missiles/ground_fire_small.json",
            r"data/hd/missiles/missiles.json",
        )

        return self.common_rename(files_no_mosaic_sin, isEnabled)

    def toggle_escape(self, isEnabled: bool):
        """
        开关 Esc退出
        """
        files_escape = (
            r"data/global/ui/layouts/hudpanelhd.json",
            r"data/global/ui/layouts/pauselayout.json", 
            r"data/global/ui/layouts/pauselayouthd.json",
        )

        return self.common_rename(files_escape, isEnabled) 

    def toggle_missiles_javelin(self, isEnabled: bool):
        """
        投掷标枪->闪电枪特效
        """
        files_missiles_javelin = (
            r"data/hd/missiles/glaive.json",
            r"data/hd/missiles/javelin.json",
            r"data/hd/missiles/maiden_javelin_missile.json",
            r"data/hd/missiles/short_spear_missile.json",
            r"data/hd/missiles/throwing_spear_missile.json",
        )

        return self.common_rename(files_missiles_javelin, isEnabled)
    
    def toggle_missiles_throw(self, isEnabled: bool):
        """
        投掷飞刀->闪电尾特效
        """
        files_missiles_throw = (
            r"data/hd/missiles/balanced_axe_missile.json",
            r"data/hd/missiles/balanced_knife_missile.json",
            r"data/hd/missiles/missile_dagger.json",
            r"data/hd/missiles/missile_hand_axe.json",
        )

        return self.common_rename(files_missiles_throw, isEnabled)

    def toggle_hd_env_presets(self, isEnabled: bool):
        """
        开关 地形变化 (A2贤者之谷小站, A3崔凡克, A4混沌庇护所, A5毁灭王座)
        """
        files_hd_env_presets = (
            r"data/hd/env/preset/act2/outdoors/kingwarp.json",
            r"data/hd/env/preset/act3/travincal/travn.json",
            r"data/hd/env/preset/act4/diab/entry1.json",
            r"data/hd/env/preset/expansion/baallair/wthrone.json",
        )
        
        return self.common_rename(files_hd_env_presets, isEnabled)

    def toggle_lava_river_flow(self, isEnabled: bool):
        """
        开关 屏蔽火焰之河岩浆特效
        """
        files_lava_effect = (
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge1_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge1_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge1_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge1_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge1_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge3_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge3_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge3_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge3_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge3_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge4_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge4_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge4_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge4_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridge4_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridgelava_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridgelava_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridgelava_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridgelava_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_bridgelava_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_entry1_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_entry1_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_entry1_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_entry1_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_entry1_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_heart_center_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_heart_center_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_heart_center_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_heart_center_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_heart_center_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_heart_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_heart_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_heart_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_heart_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_heart_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_winge1_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_winge1_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_winge1_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_winge1_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_winge1_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_winge2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_winge2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_winge2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_winge2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_winge2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingn1_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingn1_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingn1_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingn1_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingn1_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingn2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingn2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingn2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingn2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingn2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wings1_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wings1_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wings1_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wings1_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wings1_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wings2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wings2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wings2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wings2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wings2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingw1_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingw1_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingw1_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingw1_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingw1_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingw2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingw2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingw2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingw2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/diab_wingw2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavae2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavae2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavae2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavae2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavae2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaew2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaew2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaew2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaew2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaew2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaew_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaew_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaew_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaew_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaew_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavae_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavae_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavae_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavae_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavae_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavan2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavan2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavan2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavan2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavan2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavans2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavans2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavans2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavans2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavans2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavans_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavans_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavans_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavans_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavans_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavan_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavan_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavan_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavan_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavan_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavas2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavas2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavas2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavas2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavas2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavas_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavas_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavas_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavas_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavas_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaw2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaw2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaw2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaw2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaw2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaw_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaw_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaw_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaw_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/expansion_lavaw_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_forgee_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_forgee_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_forgee_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_forgee_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_forgee_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_forgew_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_forgew_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_forgew_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_forgew_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_forgew_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_heart_center_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_heart_center_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_heart_center_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_heart_center_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_heart_center_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavae2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavae2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavae2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavae2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavae2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaew2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaew2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaew2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaew2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaew2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaew_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaew_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaew_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaew_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaew_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavae_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavae_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavae_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavae_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavae_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavan2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavan2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavan2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavan2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavan2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavane2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavane2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavane2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavane2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavane2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanew2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanew2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanew2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanew2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanew2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanew_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanew_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanew_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanew_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanew_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavane_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavane_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavane_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavane_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavane_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavans2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavans2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavans2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavans2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavans2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanse2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanse2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanse2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanse2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanse2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansew2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansew2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansew2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansew2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansew2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansew_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansew_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansew_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansew_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansew_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanse_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanse_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanse_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanse_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanse_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansw2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansw2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansw2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansw2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansw2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansw_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansw_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansw_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansw_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavansw_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavans_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavans_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavans_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavans_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavans_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanw2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanw2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanw2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanw2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanw2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanw_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanw_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanw_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanw_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavanw_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavan_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavan_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavan_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavan_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavan_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavas2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavas2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavas2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavas2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavas2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavase2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavase2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavase2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavase2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavase2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasew2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasew2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasew2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasew2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasew2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasew_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasew_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasew_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasew_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasew_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavase_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavase_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavase_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavase_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavase_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasw2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasw2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasw2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasw2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasw2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasw_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasw_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasw_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasw_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavasw_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavas_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavas_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavas_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavas_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavas_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaw2_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaw2_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaw2_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaw2_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaw2_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaw_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaw_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaw_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaw_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavaw_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavax_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavax_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavax_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavax_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_lavax_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_warpmesa1_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_warpmesa1_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_warpmesa1_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_warpmesa1_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_warpmesa1_lod4.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_warpmesa_lod0.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_warpmesa_lod1.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_warpmesa_lod2.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_warpmesa_lod3.model",
            r"data/hd/env/model/act4/lava/act4_lava_river_flow/lava_warpmesa_lod4.model",
        )

        return self.common_empty_file(files_lava_effect, isEnabled)

    def toggle_load_screen_panel(self, isEnabled: bool):
        """
        开关 删除进门动画
        """
        files_load_screen_panel = [
            r"data/global/ui/layouts/loadscreenpanel.json",
            r"data/global/ui/layouts/loadscreenpanelhd.json",
        ]

        return self.common_rename(files_load_screen_panel, isEnabled)

    def toggle_experience_bar(self, isEnabled: bool):
        """
        开关 经验条变色
        """
        files_experience_bar = (
            r"data/hd/global/ui/panel/hud_02/experience_bar.lowend.sprite",
            r"data/hd/global/ui/panel/hud_02/experience_bar.sprite",
        )

        return self.common_rename(files_experience_bar, isEnabled)
    
    def toggle_sound(self, isEnabled: bool):
        """
        开关 咒符/符文/技能结束提示音
        """
        files_sound = (
            r"data/global/excel/misc.txt",
            r"data/global/excel/states.txt",
        )

        return self.common_rename(files_sound, isEnabled)
    
    def toggle_hd_global_palette_randtransforms_json(self, isEnabled: bool):
        """
        开关 变色精英怪
        """
        files_random_elite = (
            r"data/hd/global/palette/randtransforms.json",
        )

        return self.common_rename(files_random_elite, isEnabled)

    def toggle_global_excel_affixes(self, isEnabled: bool):
        """
        开关 特殊词缀装备变色
        """
        files_global_excel_affixes = (
            r"data/global/excel/magicprefix.txt",
            r"data/global/excel/magicsuffix.txt",
            r"data/global/ui/layouts/globaldatahd.json"
        )

        return self.common_rename(files_global_excel_affixes, isEnabled)

    def toggle_mephisto_key(self, isEnabled: bool):
        """
        开关 6BOSS钥匙皮肤
        """
        files_key = (
            r"data/hd/items/items.json",
        )
        return self.common_rename(files_key, isEnabled)

    def toggle_hellfire_torch(self, isEnabled: bool):
        """
        "126": "屏蔽 地狱火炬火焰风暴特效",
        """
        paths = [
            r"data/global/excel/skills.txt",
        ]

        params = {
            "DiabWall" : {"col": "ItemCltEffect", True: "200", False: ""},
        }

        count = 0
        total = len(paths)

        for path in paths:
            file_path = os.path.join(self.dir_mod, path)
            temp_path = file_path + ".tmp"

            try:
                original_formatted_rows = [] # 源数据列表(保持样式)
                working_unquoted_rows = [] # 干净数据列表(操作用)
                # 1.读取数据
                with open(file_path, 'r', newline='', encoding='utf-8') as f:
                    for line_num, line in enumerate(f):
                        line = line.rstrip('\r\n') # 移除行末的换行符，避免写入时多余空行
                        current_original_fields = line.split('\t') 
                        original_formatted_rows.append(current_original_fields)
                        # 为工作台创建一份“去引号”的副本。这使得后续的查找和修改更简单。
                        current_unquoted_fields = [
                            field.strip('"') if field.startswith('"') and field.endswith('"') else field 
                            for field in current_original_fields
                        ]
                        working_unquoted_rows.append(current_unquoted_fields)
                
                # 2.修改数据
                for i, working_unquoted_row in enumerate(working_unquoted_rows):
                    skill = working_unquoted_row[0]
                    if(skill in params):
                        param = params[skill]
                        x = i
                        y = working_unquoted_rows[0].index(param["col"])
                        original_value = original_formatted_rows[x][y]
                        new_value = param[isEnabled]
                        if original_value.startswith('"') and original_value.endswith('"'):
                            original_formatted_rows[x][y] = f"\"{new_value}\""
                        else:
                            original_formatted_rows[x][y] = new_value

                # 3.将修改后的数据写回新文件
                with open(temp_path, 'w', newline='', encoding='utf-8') as f:
                    for row_fields in original_formatted_rows:
                        line = '\t'.join(row_fields) + '\n'
                        # 手动将字段用制表符拼接，然后写入文件，保留原始格式
                        f.write(line) # <-- 修正点！直接字符串拼接写入
                
                # 4.将临时文件重命名为原文件，覆盖原文件
                os.replace(temp_path, file_path)
                count += 1
            except Exception as e:
                print(e)
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        return (count, total)
    
    def toggle_pointer(self, isEnabled: bool):
        """
        "A1兵营/A4火焰之河/A5尼拉塞克/BOSS 指引"
        """
        paths = [
            #
            r"data/hd/env/preset/act1/court/courte.json",
            r"data/hd/env/preset/act1/court/courtn.json",
            r"data/hd/env/preset/act1/court/courtw.json",
            #
            r"data/hd/env/preset/act4/diab/bridge1.json",
            r"data/hd/env/preset/act4/diab/bridge2.json",
            r"data/hd/env/preset/act4/diab/bridge3.json",
            r"data/hd/env/preset/act4/diab/bridge4.json",
            #
            r"data/hd/env/preset/expansion/wildtemple/nihle.json",
            r"data/hd/env/preset/expansion/wildtemple/nihln.json",
            r"data/hd/env/preset/expansion/wildtemple/nihls.json",
            r"data/hd/env/preset/expansion/wildtemple/nihlw.json",
            #
            r"data/hd/character/enemy/hephasto.json",
            r"data/hd/character/enemy/izual.json",
            r"data/hd/character/enemy/maggotqueen1.json",
            r"data/hd/character/enemy/radament.json",
            r"data/hd/character/enemy/smith.json",
            r"data/hd/character/enemy/summoner.json",
            r"data/hd/character/enemy/Uberandariel.json",
            r"data/hd/character/enemy/Uberduriel.json",
            r"data/hd/character/monsters.json",
        ]

        return self.common_rename(paths, isEnabled)

    def toggle_hd_local_video(self, isEnabled: bool):
        """
        开/关 屏蔽动画
        """
        files_hd_local_video = [
            #
            r"data/global/video/act2/act02start.webm",
            r"data/global/video/act3/act03start.webm",
            r"data/global/video/act4/act04end.webm",
            r"data/global/video/act4/act04start.webm",
            r"data/global/video/act5/d2x_out.webm",
            r"data/global/video/bliznorth.webm",
            r"data/global/video/d2intro.webm",
            r"data/global/video/d2x_intro.webm",
            r"data/global/video/new_bliz.webm",
            #
            r"data/hd/global/video/act2/act02start.webm",
            r"data/hd/global/video/act3/act03start.webm",
            r"data/hd/global/video/act4/act04end.webm",
            r"data/hd/global/video/act4/act04start.webm",
            r"data/hd/global/video/act5/d2x_out.webm",
            r"data/hd/global/video/blizzardlogos.webm",
            r"data/hd/global/video/creditsloop.webm",
            r"data/hd/global/video/d2intro.webm",
            r"data/hd/global/video/d2x_intro.webm",
            r"data/hd/global/video/logoanim.webm",
            r"data/hd/global/video/logoloop.webm",
            #
            r"data/hd/local/video/act2/act02start.flac",
            r"data/hd/local/video/act3/act03start.flac",
            r"data/hd/local/video/act4/act04end.flac",
            r"data/hd/local/video/act4/act04start.flac",
            r"data/hd/local/video/act5/d2x_out.flac",
            r"data/hd/local/video/blizzardlogos.flac",
            r"data/hd/local/video/d2intro.flac",
            r"data/hd/local/video/d2x_intro.flac",
            r"data/hd/local/video/logoanim.flac",
            #
            r"data/local/video/act2/act02start.flac",
            r"data/local/video/act3/act03start.flac",
            r"data/local/video/act4/act04end.flac",
            r"data/local/video/act4/act04start.flac",
            r"data/local/video/act5/d2x_out.flac",
            r"data/local/video/d2intro.flac",
            r"data/local/video/d2x_intro.flac",
        ]

        return self.common_empty_file(files_hd_local_video, isEnabled)

    def toggle_quick_game(self, isEnabled: bool):
        """
        点击角色快速建立最高难度游戏
        """
        files_quick_game = [
            r"data/global/ui/layouts/mainmenupanelhd.json",
        ]

        return self.common_rename(files_quick_game, isEnabled)
    
    def toggle_context_menu(self, isEnabled: bool):
        """
        更大的好友菜单
        """
        files_context_menu = [
            r"data/global/ui/layouts/contextmenuhd.json",
        ]

        return self.common_rename(files_context_menu, isEnabled);

    def toggle_character_enemy(self, isEnabled: bool):
        """
        怪物光源+危险标识
        """
        files_danger_enemy = [
            r"data/hd/character/enemy/andariel.json",
            r"data/hd/character/enemy/arach1.json",
            r"data/hd/character/enemy/baalclone.json",
            r"data/hd/character/enemy/baalcrab.json",
            r"data/hd/character/enemy/baalminion1.json",
            r"data/hd/character/enemy/baboon1.json",
            r"data/hd/character/enemy/baboon6.json",
            r"data/hd/character/enemy/barricadedoor1.json",
            r"data/hd/character/enemy/barricadedoor2.json",
            r"data/hd/character/enemy/barricadetower.json",
            r"data/hd/character/enemy/barricadewall1.json",
            r"data/hd/character/enemy/barricadewall2.json",
            r"data/hd/character/enemy/batdemon1.json",
            r"data/hd/character/enemy/bighead1.json",
            r"data/hd/character/enemy/bladecreeper.json",
            r"data/hd/character/enemy/bloodgolem.json",
            r"data/hd/character/enemy/bloodlord1.json",
            r"data/hd/character/enemy/bloodraven.json",
            r"data/hd/character/enemy/blunderbore1.json",
            r"data/hd/character/enemy/bonefetish1.json",
            r"data/hd/character/enemy/boneprison1.json",
            r"data/hd/character/enemy/boneprison2.json",
            r"data/hd/character/enemy/boneprison3.json",
            r"data/hd/character/enemy/boneprison4.json",
            r"data/hd/character/enemy/brute2.json",
            r"data/hd/character/enemy/cantor1.json",
            r"data/hd/character/enemy/catapult1.json",
            r"data/hd/character/enemy/catapultspotter1.json",
            r"data/hd/character/enemy/chargeboltsentry.json",
            r"data/hd/character/enemy/claygolem.json",
            r"data/hd/character/enemy/compellingorb.json",
            r"data/hd/character/enemy/corpsefire.json",
            r"data/hd/character/enemy/corruptrogue1.json",
            r"data/hd/character/enemy/councilmember1.json",
            r"data/hd/character/enemy/cowking.json",
            r"data/hd/character/enemy/cr_archer1.json",
            r"data/hd/character/enemy/cr_lancer1.json",
            r"data/hd/character/enemy/crownest1.json",
            r"data/hd/character/enemy/darkelder.json",
            r"data/hd/character/enemy/darkwanderer.json",
            r"data/hd/character/enemy/deathmauler1.json",
            r"data/hd/character/enemy/deathsentry.json",
            r"data/hd/character/enemy/diablo.json",
            r"data/hd/character/enemy/doomknight1.json",
            r"data/hd/character/enemy/doomknight2.json",
            r"data/hd/character/enemy/doomknight3.json",
            r"data/hd/character/enemy/dopplezon.json",
            r"data/hd/character/enemy/duriel.json",
            r"data/hd/character/enemy/evilhole1.json",
            r"data/hd/character/enemy/evilhut.json",
            r"data/hd/character/enemy/fallen1.json",
            r"data/hd/character/enemy/fallenshaman1.json",
            r"data/hd/character/enemy/fetish1.json",
            r"data/hd/character/enemy/fetish11.json",
            r"data/hd/character/enemy/fetishblow1.json",
            r"data/hd/character/enemy/fetishshaman1.json",
            r"data/hd/character/enemy/fingermage1.json",
            r"data/hd/character/enemy/firetower.json",
            r"data/hd/character/enemy/flyingscimitar.json",
            r"data/hd/character/enemy/foulcrow1.json",
            r"data/hd/character/enemy/frogdemon1.json",
            r"data/hd/character/enemy/frozenhorror1.json",
            r"data/hd/character/enemy/gargoyletrap.json",
            r"data/hd/character/enemy/goatman1.json",
            r"data/hd/character/enemy/gorgon1.json",
            r"data/hd/character/enemy/griswold.json",
            r"data/hd/character/enemy/hellbovine.json",
            r"data/hd/character/enemy/imp1.json",
            r"data/hd/character/enemy/invisopet.json",
            r"data/hd/character/enemy/invisospawner.json",
            r"data/hd/character/enemy/lightningsentry.json",
            r"data/hd/character/enemy/lightningspire.json",
            r"data/hd/character/enemy/maggotbaby1.json",
            r"data/hd/character/enemy/maggotegg1.json",
            r"data/hd/character/enemy/megademon1.json",
            r"data/hd/character/enemy/mephisto.json",
            r"data/hd/character/enemy/mephistospirit.json",
            r"data/hd/character/enemy/minion1.json",
            r"data/hd/character/enemy/minionspawner1.json",
            r"data/hd/character/enemy/mosquito1.json",
            r"data/hd/character/enemy/mummy1.json",
            r"data/hd/character/enemy/nihlathakboss.json",
            r"data/hd/character/enemy/overseer1.json",
            r"data/hd/character/enemy/painworm1.json",
            r"data/hd/character/enemy/pantherwoman1.json",
            r"data/hd/character/enemy/prisondoor.json",
            r"data/hd/character/enemy/putriddefiler1.json",
            r"data/hd/character/enemy/quillbear1.json",
            r"data/hd/character/enemy/quillrat1.json",
            r"data/hd/character/enemy/reanimatedhorde1.json",
            r"data/hd/character/enemy/regurgitator1.json",
            r"data/hd/character/enemy/sandleaper1.json",
            r"data/hd/character/enemy/sandmaggot1.json",
            r"data/hd/character/enemy/sandraider1.json",
            r"data/hd/character/enemy/sarcophagus.json",
            r"data/hd/character/enemy/scarab1.json",
            r"data/hd/character/enemy/seventombs.json",
            r"data/hd/character/enemy/shadowwarrior.json",
            r"data/hd/character/enemy/siegebeast1.json",
            r"data/hd/character/enemy/sk_archer1.json",
            r"data/hd/character/enemy/skeleton1.json",
            r"data/hd/character/enemy/skmage_cold1.json",
            r"data/hd/character/enemy/skmage_fire1.json",
            r"data/hd/character/enemy/skmage_ltng1.json",
            r"data/hd/character/enemy/skmage_pois1.json",
            r"data/hd/character/enemy/slinger1.json",
            r"data/hd/character/enemy/slinger5.json",
            r"data/hd/character/enemy/snowyeti1.json",
            r"data/hd/character/enemy/succubus1.json",
            r"data/hd/character/enemy/succubuswitch1.json",
            r"data/hd/character/enemy/suicideminion1.json",
            r"data/hd/character/enemy/swarm1.json",
            r"data/hd/character/enemy/tentacle1.json",
            r"data/hd/character/enemy/tentaclehead1.json",
            r"data/hd/character/enemy/thornhulk1.json",
            r"data/hd/character/enemy/trappedsoul1.json",
            r"data/hd/character/enemy/trappedsoul2.json",
            r"data/hd/character/enemy/turret1.json",
            r"data/hd/character/enemy/unraveler1.json",
            r"data/hd/character/enemy/vampire1.json",
            r"data/hd/character/enemy/venomlord.json",
            r"data/hd/character/enemy/vilechild1.json",
            r"data/hd/character/enemy/vilemother1.json",
            r"data/hd/character/enemy/vulture1.json",
            r"data/hd/character/enemy/willowisp1.json",
            r"data/hd/character/enemy/window1.json",
            r"data/hd/character/enemy/window2.json",
            r"data/hd/character/enemy/wraith1.json",
            r"data/hd/character/enemy/zealot1.json",
            r"data/hd/character/enemy/zombie1.json",
        ]

        return self.common_rename(files_danger_enemy, isEnabled)

    def toggle_skill_logo(self, isEnabled: bool):
        """
        技能图标
        """
        files_skill_logo = [
            r"data/global/excel/overlay.txt",
            r"data/hd/overlays/assassin/fade.json",
            r"data/hd/overlays/assassin/quickness.json",
            r"data/hd/overlays/common/battlecommand.json",
            r"data/hd/overlays/common/battleorders.json",
            r"data/hd/overlays/common/progressive_cold_1.json",
            r"data/hd/overlays/common/progressive_cold_2.json",
            r"data/hd/overlays/common/progressive_cold_3.json",
            r"data/hd/overlays/common/progressive_damage_1.json",
            r"data/hd/overlays/common/progressive_damage_2.json",
            r"data/hd/overlays/common/progressive_damage_3.json",
            r"data/hd/overlays/common/progressive_fire_1.json",
            r"data/hd/overlays/common/progressive_fire_2.json",
            r"data/hd/overlays/common/progressive_fire_3.json",
            r"data/hd/overlays/common/progressive_lightning_1.json",
            r"data/hd/overlays/common/progressive_lightning_2.json",
            r"data/hd/overlays/common/progressive_lightning_3.json",
            r"data/hd/overlays/common/progressive_other_1.json",
            r"data/hd/overlays/common/progressive_other_2.json",
            r"data/hd/overlays/common/progressive_other_3.json",
            r"data/hd/overlays/common/progressive_steal_1.json",
            r"data/hd/overlays/common/progressive_steal_2.json",
            r"data/hd/overlays/common/progressive_steal_3.json",
            r"data/hd/overlays/common/shout.json",
            r"data/hd/overlays/sorceress/enchant.json",
        ]

        return self.common_rename(files_skill_logo, isEnabled)

    def select_town_portal(self, radio: str):
        """
        传送门皮肤
        """
        params = {
            "default" :"data/hd/vfx/particles/objects/vfx_only/town_portal/vfx_town_portal_newstuff.particles",
            "1": "data/hd/vfx/particles/objects/vfx_only/town_portal/vfx_town_portal_newstuff_newred.particles",
            "2": "data/hd/vfx/particles/objects/vfx_only/town_portal/vfx_town_portal.particles",
            "3": "data/hd/vfx/particles/objects/vfx_only/town_portal/vfx_town_portal_newstuff_redversion.particles"
        }

        paths = [
            r"data/hd/objects/vfx_only/town_portal.json"
        ]
        count = 0
        total = len(paths)
        for path in paths:
            target_path = os.path.join(self.dir_mod, path)
            temp_path = target_path + ".tmp"
            try:
                # 1.load
                json_data = None
                with open(target_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                # 2.modify
                json_data["entities"][0]["components"][2]["filename"] = params[radio]
                
                # 3.dump temp
                with open(temp_path, 'w', encoding="utf-8") as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)

                # 4.replace
                os.replace(temp_path, target_path)
                count += 1
            except Exception as e:
                print(e)
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        return (count, total)

    def select_teleport_skin(self, radio: str):
        """
        传送术皮肤
        """
        params = {
            "default": "data/hd/overlays/sorceress/teleport.json",
            "1": "data/hd/overlays/sorceress/teleport.json.1",
            "2": "data/hd/overlays/sorceress/teleport.json.2",
        }

        paths = [
            r"data/hd/objects/vfx_only/town_portal.json"
        ]
        count = 0
        total = len(paths)
        for path in paths:
            target_path = os.path.join(self.dir_mod, path)
            temp_path = target_path + ".tmp"
            try:
                src_path = os.path.join(self.dir_mod, params[radio])
                dst_path = os.path.join(self.dir_mod, params["default"])
                if "default" == radio:
                    os.remove(dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
                count += 1
            except Exception as e:
                print(e)
        return (count, total)

    def select_arrow_skin(self, radio: str):
        """
        箭皮肤
        """
        params = {
            "default": r"data/hd/vfx/particles/missiles/arrow/vfx_arrow.particles",
            "1": r"data/hd/vfx/particles/missiles/safe_arrow/safe_arrow.particles",
            "2": r"data/hd/vfx/particles/missiles/ice_arrow/fx_ice_projectile_arrow.particles",
            "3": r"data/hd/vfx/particles/missiles/fire_arrow/fx_fire_projectile_arrow.particles",
        }

        paths = [
            r"data/hd/missiles/arrow.json",
            r"data/hd/missiles/x_bow_bolt.json",
        ]

        count = 0
        total = len(paths)
        for path in paths:
            target_path = os.path.join(self.dir_mod, path)
            temp_path = target_path + ".tmp"
            try:
                # 1.load
                json_data = None
                with open(target_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                # 2.modify
                json_data["entities"][-1]["components"][0]["filename"] = params[radio]
                
                # 3.dump temp
                with open(temp_path, 'w', encoding="utf-8") as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)

                # 4.replace
                os.replace(temp_path, target_path)
                count += 1
            except Exception as e:
                print(e)
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        return (count, total)
    
    def select_enemy_arrow_skin(self, radio: str):
        """
        老鼠刺针/剥皮吹箭样式
        """
        params = {
            "default": [r"data/hd/vfx/particles/missiles/spike_fiend_missle/vfx_spikefiend_missile.particles", r"data/hd/vfx/particles/missiles/blowdart/vfx_blowdart.particles"],
            "1": r"data/hd/vfx/particles/missiles/safe_arrow/safe_arrow.particles",
            "2": r"data/hd/vfx/particles/missiles/ice_arrow/fx_ice_projectile_arrow.particles",
            "3": r"data/hd/vfx/particles/missiles/fire_arrow/fx_fire_projectile_arrow.particles",
        }
        
        paths = [
            r"data/hd/missiles/spike_fiend_missle.json",
            r"data/hd/missiles/blowdart.json",
        ]

        count = 0
        total = len(paths)
        for i, path in enumerate(paths):
            target_path = os.path.join(self.dir_mod, path)
            temp_path = target_path + ".tmp"
            try:
                # 1.load
                json_data = None
                with open(target_path, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                # 2.modify
                json_data["entities"][1]["components"][-1]["filename"] = params[radio][i] if "default" == radio else params[radio]
                
                # 3.dump temp
                with open(temp_path, 'w', encoding="utf-8") as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)

                # 4.replace
                os.replace(temp_path, target_path)
                count += 1
            except Exception as e:
                print(e)
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
        return (count, total)

    def modify_character_player(self, val: int):
        """
        角色光源
        """
        params = [
            r"data/hd/character/player/amazon.json",
            r"data/hd/character/player/assassin.json",
            r"data/hd/character/player/barbarian.json",
            r"data/hd/character/player/druid.json",
            r"data/hd/character/player/necromancer.json",
            r"data/hd/character/player/paladin.json",
            r"data/hd/character/player/sorceress.json",
        ]

        count = 0
        total = len(params)

        for param in params:
            try:
                # 0.var
                target_file = os.path.join(self.dir_mod, param)
                temp_file = target_file + ".tmp"
                # 1.load
                json_data = None
                with open(target_file, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                # 2.modify
                json_data["entities"][-1]["components"][-1]["power"] = val * 3000
                
                # 3.dump temp
                with open(temp_file, 'w', encoding="utf-8") as f:
                    json.dump(json_data, f, ensure_ascii=False, indent=4)

                # 4.replace
                os.replace(temp_file, target_file)
                count += 1
            except Exception as e:
                print(e)
        return (count, total)
    
    def modify_rune_rectangle(self, val: int):
        """
        符文名称大小
        """
        params = [
            r"data/local/lng/strings/item-runes.json",
        ]

        count = 0
        total = len(params)

        try:
            # 0.var
            target_file = os.path.join(self.dir_mod, params[0])
            temp_file = target_file + ".tmp"
            # 1.load
            json_data = None
            with open(target_file, 'r', encoding='utf-8-sig') as f:
                json_data = json.load(f)
            
            # 2.modify
            pattern = re.compile(r"^r(2[2-9]|3[0-3])$")
            for object in json_data:
                if pattern.match(object["Key"]):
                    object["enUS"] = ("\n"*val) + object["enUS"].replace("\n", "").replace("=","").replace("ÿc8","\nÿc8") + ("\n"*val)
                    object["zhCN"] = ("\n"*val) + object["zhCN"].replace("\n", "").replace("=","").replace("ÿc8","\nÿc8") + ("\n"*val)
                    object["zhTW"] = ("\n"*val) + object["zhTW"].replace("\n", "").replace("=","").replace("ÿc8","\nÿc8") + ("\n"*val)
                    if(val > 0) :
                        object["enUS"] = object["enUS"] + ("="*(2*val+10))
                        object["zhCN"] = object["zhCN"] + ("="*(2*val+10))
                        object["zhTW"] = object["zhTW"] + ("="*(2*val+10))
            
            # 3.dump temp
            with open(temp_file, 'w', encoding="utf-8-sig") as f:
                json.dump(json_data, f, ensure_ascii=False, indent=2)

            # 4.replace
            os.replace(temp_file, target_file)
            count += 1
        except Exception as e:
            print(e)
        return (count, total)
    
    def toggle_fade_dummy(self, isEnabled: bool):
        """
        屏蔽影散隐身效果
        """
        files_diab_bridge = [
            r"data/global/excel/itemstatcost.txt",
        ]

        return self.common_rename(files_diab_bridge, isEnabled);

    def toggle_necroskeleton(self, isEnabled: bool):
        """
        骷髅火焰刀+圣盾特效
        """
        files_necroskeleton = [
            r"data/hd/character/enemy/necroskeleton.json"
        ]

        return self.common_rename(files_necroskeleton, isEnabled)
    
    def toggle_circlet(self, isEnabled: bool):
        """
        隐藏头盔类装备外观
        """
        files__circlet = [
            r"data/hd/items/armor/circlet/circlet.json",
            r"data/hd/items/armor/circlet/coronet.json",
            r"data/hd/items/armor/circlet/diadem.json",
            r"data/hd/items/armor/circlet/tiara.json",
        ]

        return self.common_rename(files__circlet, isEnabled)

    def toggle_env_vis(self, isEnabled: bool):
        """
        画面变亮
        """
        files_env_vis = [
            r"data/hd/env/vis/1_default_day.json",
            r"data/hd/env/vis/act1_barracks_dawn1.json",
            r"data/hd/env/vis/act1_barracks_dawn2.json",
            r"data/hd/env/vis/act1_barracks_day.json",
            r"data/hd/env/vis/act1_barracks_desecrated.json",
            r"data/hd/env/vis/act1_barracks_dusk1.json",
            r"data/hd/env/vis/act1_barracks_dusk2.json",
            r"data/hd/env/vis/act1_barracks_night.json",
            r"data/hd/env/vis/act1_campfire_dawn1.json",
            r"data/hd/env/vis/act1_campfire_dawn2.json",
            r"data/hd/env/vis/act1_campfire_day.json",
            r"data/hd/env/vis/act1_campfire_dusk1.json",
            r"data/hd/env/vis/act1_campfire_dusk2.json",
            r"data/hd/env/vis/act1_campfire_night.json",
            r"data/hd/env/vis/act1_catacombs_dawn1.json",
            r"data/hd/env/vis/act1_catacombs_dawn2.json",
            r"data/hd/env/vis/act1_catacombs_day.json",
            r"data/hd/env/vis/act1_catacombs_desecrated.json",
            r"data/hd/env/vis/act1_catacombs_dusk1.json",
            r"data/hd/env/vis/act1_catacombs_dusk2.json",
            r"data/hd/env/vis/act1_catacombs_night.json",
            r"data/hd/env/vis/act1_cathedral_dawn1.json",
            r"data/hd/env/vis/act1_cathedral_dawn2.json",
            r"data/hd/env/vis/act1_cathedral_day.json",
            r"data/hd/env/vis/act1_cathedral_dusk1.json",
            r"data/hd/env/vis/act1_cathedral_dusk2.json",
            r"data/hd/env/vis/act1_cathedral_night.json",
            r"data/hd/env/vis/act1_caves_dawn1.json",
            r"data/hd/env/vis/act1_caves_dawn2.json",
            r"data/hd/env/vis/act1_caves_day.json",
            r"data/hd/env/vis/act1_caves_desecrated.json",
            r"data/hd/env/vis/act1_caves_dusk1.json",
            r"data/hd/env/vis/act1_caves_dusk2.json",
            r"data/hd/env/vis/act1_caves_night.json",
            r"data/hd/env/vis/act1_court_dawn1.json",
            r"data/hd/env/vis/act1_court_dawn2.json",
            r"data/hd/env/vis/act1_court_day.json",
            r"data/hd/env/vis/act1_court_desecrated.json",
            r"data/hd/env/vis/act1_court_dusk1.json",
            r"data/hd/env/vis/act1_court_dusk2.json",
            r"data/hd/env/vis/act1_court_night.json",
            r"data/hd/env/vis/act1_crypt_dawn1.json",
            r"data/hd/env/vis/act1_crypt_dawn2.json",
            r"data/hd/env/vis/act1_crypt_day.json",
            r"data/hd/env/vis/act1_crypt_desecrated.json",
            r"data/hd/env/vis/act1_crypt_dusk1.json",
            r"data/hd/env/vis/act1_crypt_dusk2.json",
            r"data/hd/env/vis/act1_crypt_night.json",
            r"data/hd/env/vis/act1_outdoors_dawn1.json",
            r"data/hd/env/vis/act1_outdoors_dawn2.json",
            r"data/hd/env/vis/act1_outdoors_day.json",
            r"data/hd/env/vis/act1_outdoors_desecrated.json",
            r"data/hd/env/vis/act1_outdoors_dusk1.json",
            r"data/hd/env/vis/act1_outdoors_dusk2.json",
            r"data/hd/env/vis/act1_outdoors_interior01_vis.json",
            r"data/hd/env/vis/act1_outdoors_night.json",
            r"data/hd/env/vis/act1_tristram_dawn1.json",
            r"data/hd/env/vis/act1_tristram_dawn2.json",
            r"data/hd/env/vis/act1_tristram_day.json",
            r"data/hd/env/vis/act1_tristram_dusk1.json",
            r"data/hd/env/vis/act1_tristram_dusk2.json",
            r"data/hd/env/vis/act1_tristram_night.json",
            r"data/hd/env/vis/act2_arcane_dawn1.json",
            r"data/hd/env/vis/act2_arcane_dawn2.json",
            r"data/hd/env/vis/act2_arcane_day.json",
            r"data/hd/env/vis/act2_arcane_desecrated.json",
            r"data/hd/env/vis/act2_arcane_dusk1.json",
            r"data/hd/env/vis/act2_arcane_dusk2.json",
            r"data/hd/env/vis/act2_arcane_night.json",
            r"data/hd/env/vis/act2_bigcliff_dawn1.json",
            r"data/hd/env/vis/act2_bigcliff_dawn2.json",
            r"data/hd/env/vis/act2_bigcliff_day.json",
            r"data/hd/env/vis/act2_bigcliff_dusk1.json",
            r"data/hd/env/vis/act2_bigcliff_dusk2.json",
            r"data/hd/env/vis/act2_bigcliff_night.json",
            r"data/hd/env/vis/act2_frontend_dawn1.json",
            r"data/hd/env/vis/act2_frontend_dawn2.json",
            r"data/hd/env/vis/act2_frontend_day.json",
            r"data/hd/env/vis/act2_frontend_dusk1.json",
            r"data/hd/env/vis/act2_frontend_dusk2.json",
            r"data/hd/env/vis/act2_frontend_night.json",
            r"data/hd/env/vis/act2_maggot_dawn1.json",
            r"data/hd/env/vis/act2_maggot_dawn2.json",
            r"data/hd/env/vis/act2_maggot_day.json",
            r"data/hd/env/vis/act2_maggot_desecrated.json",
            r"data/hd/env/vis/act2_maggot_dusk1.json",
            r"data/hd/env/vis/act2_maggot_dusk2.json",
            r"data/hd/env/vis/act2_maggot_night.json",
            r"data/hd/env/vis/act2_outdoors_dawn1.json",
            r"data/hd/env/vis/act2_outdoors_dawn2.json",
            r"data/hd/env/vis/act2_outdoors_day.json",
            r"data/hd/env/vis/act2_outdoors_dusk1.json",
            r"data/hd/env/vis/act2_outdoors_dusk2.json",
            r"data/hd/env/vis/act2_outdoors_night.json",
            r"data/hd/env/vis/act2_palace_cells_dawn1.json",
            r"data/hd/env/vis/act2_palace_cells_dawn2.json",
            r"data/hd/env/vis/act2_palace_cells_day.json",
            r"data/hd/env/vis/act2_palace_cells_desecrated.json",
            r"data/hd/env/vis/act2_palace_cells_dusk1.json",
            r"data/hd/env/vis/act2_palace_cells_dusk2.json",
            r"data/hd/env/vis/act2_palace_cells_night.json",
            r"data/hd/env/vis/act2_palace_clean_dawn1.json",
            r"data/hd/env/vis/act2_palace_clean_dawn2.json",
            r"data/hd/env/vis/act2_palace_clean_day.json",
            r"data/hd/env/vis/act2_palace_clean_dusk1.json",
            r"data/hd/env/vis/act2_palace_clean_dusk2.json",
            r"data/hd/env/vis/act2_palace_clean_night.json",
            r"data/hd/env/vis/act2_palace_dawn1.json",
            r"data/hd/env/vis/act2_palace_dawn2.json",
            r"data/hd/env/vis/act2_palace_day.json",
            r"data/hd/env/vis/act2_palace_desecrated.json",
            r"data/hd/env/vis/act2_palace_dusk1.json",
            r"data/hd/env/vis/act2_palace_dusk2.json",
            r"data/hd/env/vis/act2_palace_night.json",
            r"data/hd/env/vis/act2_ruin_dawn1.json",
            r"data/hd/env/vis/act2_ruin_dawn2.json",
            r"data/hd/env/vis/act2_ruin_day.json",
            r"data/hd/env/vis/act2_ruin_dusk1.json",
            r"data/hd/env/vis/act2_ruin_dusk2.json",
            r"data/hd/env/vis/act2_ruin_night.json",
            r"data/hd/env/vis/act2_sewer_dawn1.json",
            r"data/hd/env/vis/act2_sewer_dawn2.json",
            r"data/hd/env/vis/act2_sewer_day.json",
            r"data/hd/env/vis/act2_sewer_desecrated.json",
            r"data/hd/env/vis/act2_sewer_dusk1.json",
            r"data/hd/env/vis/act2_sewer_dusk2.json",
            r"data/hd/env/vis/act2_sewer_night.json",
            r"data/hd/env/vis/act2_tainted_sun.json",
            r"data/hd/env/vis/act2_tomb_dawn1.json",
            r"data/hd/env/vis/act2_tomb_dawn2.json",
            r"data/hd/env/vis/act2_tomb_day.json",
            r"data/hd/env/vis/act2_tomb_desecrated.json",
            r"data/hd/env/vis/act2_tomb_dusk1.json",
            r"data/hd/env/vis/act2_tomb_dusk2.json",
            r"data/hd/env/vis/act2_tomb_night.json",
            r"data/hd/env/vis/act2_town_dawn1.json",
            r"data/hd/env/vis/act2_town_dawn2.json",
            r"data/hd/env/vis/act2_town_day.json",
            r"data/hd/env/vis/act2_town_desecrated.json",
            r"data/hd/env/vis/act2_town_dusk1.json",
            r"data/hd/env/vis/act2_town_dusk2.json",
            r"data/hd/env/vis/act2_town_interior_vis.json",
            r"data/hd/env/vis/act2_town_night.json",
            r"data/hd/env/vis/act3_docktown_dawn1.json",
            r"data/hd/env/vis/act3_docktown_dawn2.json",
            r"data/hd/env/vis/act3_docktown_day.json",
            r"data/hd/env/vis/act3_docktown_desecrated.json",
            r"data/hd/env/vis/act3_docktown_dusk1.json",
            r"data/hd/env/vis/act3_docktown_dusk2.json",
            r"data/hd/env/vis/act3_docktown_night.json",
            r"data/hd/env/vis/act3_jungle_dawn1.json",
            r"data/hd/env/vis/act3_jungle_dawn2.json",
            r"data/hd/env/vis/act3_jungle_day.json",
            r"data/hd/env/vis/act3_jungle_dungeon_dawn1.json",
            r"data/hd/env/vis/act3_jungle_dungeon_dawn2.json",
            r"data/hd/env/vis/act3_jungle_dungeon_day.json",
            r"data/hd/env/vis/act3_jungle_dungeon_desecrated.json",
            r"data/hd/env/vis/act3_jungle_dungeon_dusk1.json",
            r"data/hd/env/vis/act3_jungle_dungeon_dusk2.json",
            r"data/hd/env/vis/act3_jungle_dungeon_night.json",
            r"data/hd/env/vis/act3_jungle_dusk1.json",
            r"data/hd/env/vis/act3_jungle_dusk2.json",
            r"data/hd/env/vis/act3_jungle_night.json",
            r"data/hd/env/vis/act3_kurast_dawn1.json",
            r"data/hd/env/vis/act3_kurast_dawn2.json",
            r"data/hd/env/vis/act3_kurast_day.json",
            r"data/hd/env/vis/act3_kurast_dusk1.json",
            r"data/hd/env/vis/act3_kurast_dusk2.json",
            r"data/hd/env/vis/act3_kurast_night.json",
            r"data/hd/env/vis/act3_kurast_stone_tile_dawn1.json",
            r"data/hd/env/vis/act3_kurast_stone_tile_dawn2.json",
            r"data/hd/env/vis/act3_kurast_stone_tile_day.json",
            r"data/hd/env/vis/act3_kurast_stone_tile_dusk1.json",
            r"data/hd/env/vis/act3_kurast_stone_tile_dusk2.json",
            r"data/hd/env/vis/act3_kurast_stone_tile_night.json",
            r"data/hd/env/vis/act3_sewer_dawn1.json",
            r"data/hd/env/vis/act3_sewer_dawn2.json",
            r"data/hd/env/vis/act3_sewer_day.json",
            r"data/hd/env/vis/act3_sewer_desecrated.json",
            r"data/hd/env/vis/act3_sewer_dusk1.json",
            r"data/hd/env/vis/act3_sewer_dusk2.json",
            r"data/hd/env/vis/act3_sewer_night.json",
            r"data/hd/env/vis/act3_spider_dawn1.json",
            r"data/hd/env/vis/act3_spider_dawn2.json",
            r"data/hd/env/vis/act3_spider_day.json",
            r"data/hd/env/vis/act3_spider_desecrated.json",
            r"data/hd/env/vis/act3_spider_dusk1.json",
            r"data/hd/env/vis/act3_spider_dusk2.json",
            r"data/hd/env/vis/act3_spider_night.json",
            r"data/hd/env/vis/act3_temple_dawn1.json",
            r"data/hd/env/vis/act3_temple_dawn2.json",
            r"data/hd/env/vis/act3_temple_day.json",
            r"data/hd/env/vis/act3_temple_desecrated.json",
            r"data/hd/env/vis/act3_temple_dusk1.json",
            r"data/hd/env/vis/act3_temple_dusk2.json",
            r"data/hd/env/vis/act3_temple_night.json",
            r"data/hd/env/vis/act3_travincal_dawn1.json",
            r"data/hd/env/vis/act3_travincal_dawn2.json",
            r"data/hd/env/vis/act3_travincal_day.json",
            r"data/hd/env/vis/act3_travincal_desecrated.json",
            r"data/hd/env/vis/act3_travincal_dusk1.json",
            r"data/hd/env/vis/act3_travincal_dusk2.json",
            r"data/hd/env/vis/act3_travincal_night.json",
            r"data/hd/env/vis/act4_diab_dawn1.json",
            r"data/hd/env/vis/act4_diab_dawn2.json",
            r"data/hd/env/vis/act4_diab_day.json",
            r"data/hd/env/vis/act4_diab_dusk1.json",
            r"data/hd/env/vis/act4_diab_dusk2.json",
            r"data/hd/env/vis/act4_diab_night.json",
            r"data/hd/env/vis/act4_fort_dawn1.json",
            r"data/hd/env/vis/act4_fort_dawn2.json",
            r"data/hd/env/vis/act4_fort_day.json",
            r"data/hd/env/vis/act4_fort_dusk1.json",
            r"data/hd/env/vis/act4_fort_dusk2.json",
            r"data/hd/env/vis/act4_fort_interior_vis.json",
            r"data/hd/env/vis/act4_fort_night.json",
            r"data/hd/env/vis/act4_lava_dawn1.json",
            r"data/hd/env/vis/act4_lava_dawn2.json",
            r"data/hd/env/vis/act4_lava_day.json",
            r"data/hd/env/vis/act4_lava_desecrated.json",
            r"data/hd/env/vis/act4_lava_dusk1.json",
            r"data/hd/env/vis/act4_lava_dusk2.json",
            r"data/hd/env/vis/act4_lava_night.json",
            r"data/hd/env/vis/act4_mesa_dawn1.json",
            r"data/hd/env/vis/act4_mesa_dawn2.json",
            r"data/hd/env/vis/act4_mesa_day.json",
            r"data/hd/env/vis/act4_mesa_desecrated.json",
            r"data/hd/env/vis/act4_mesa_dusk1.json",
            r"data/hd/env/vis/act4_mesa_dusk2.json",
            r"data/hd/env/vis/act4_mesa_night.json",
            r"data/hd/env/vis/expansion_baallair_dawn1.json",
            r"data/hd/env/vis/expansion_baallair_dawn2.json",
            r"data/hd/env/vis/expansion_baallair_day.json",
            r"data/hd/env/vis/expansion_baallair_dusk1.json",
            r"data/hd/env/vis/expansion_baallair_dusk2.json",
            r"data/hd/env/vis/expansion_baallair_night.json",
            r"data/hd/env/vis/expansion_baallair_throneroom_dawn1.json",
            r"data/hd/env/vis/expansion_baallair_throneroom_dawn2.json",
            r"data/hd/env/vis/expansion_baallair_throneroom_day.json",
            r"data/hd/env/vis/expansion_baallair_throneroom_desecrated.json",
            r"data/hd/env/vis/expansion_baallair_throneroom_dusk1.json",
            r"data/hd/env/vis/expansion_baallair_throneroom_dusk2.json",
            r"data/hd/env/vis/expansion_baallair_throneroom_night.json",
            r"data/hd/env/vis/expansion_icecave_dawn1.json",
            r"data/hd/env/vis/expansion_icecave_dawn2.json",
            r"data/hd/env/vis/expansion_icecave_day.json",
            r"data/hd/env/vis/expansion_icecave_desecrated.json",
            r"data/hd/env/vis/expansion_icecave_dusk1.json",
            r"data/hd/env/vis/expansion_icecave_dusk2.json",
            r"data/hd/env/vis/expansion_icecave_night.json",
            r"data/hd/env/vis/expansion_mountaintop_dawn1.json",
            r"data/hd/env/vis/expansion_mountaintop_dawn2.json",
            r"data/hd/env/vis/expansion_mountaintop_day.json",
            r"data/hd/env/vis/expansion_mountaintop_desecrated.json",
            r"data/hd/env/vis/expansion_mountaintop_dusk1.json",
            r"data/hd/env/vis/expansion_mountaintop_dusk2.json",
            r"data/hd/env/vis/expansion_mountaintop_night.json",
            r"data/hd/env/vis/expansion_ruins_dawn1.json",
            r"data/hd/env/vis/expansion_ruins_dawn2.json",
            r"data/hd/env/vis/expansion_ruins_day.json",
            r"data/hd/env/vis/expansion_ruins_dusk1.json",
            r"data/hd/env/vis/expansion_ruins_dusk2.json",
            r"data/hd/env/vis/expansion_ruins_night.json",
            r"data/hd/env/vis/expansion_ruins_snow_dawn1.json",
            r"data/hd/env/vis/expansion_ruins_snow_dawn2.json",
            r"data/hd/env/vis/expansion_ruins_snow_day.json",
            r"data/hd/env/vis/expansion_ruins_snow_dusk1.json",
            r"data/hd/env/vis/expansion_ruins_snow_dusk2.json",
            r"data/hd/env/vis/expansion_ruins_snow_night.json",
            r"data/hd/env/vis/expansion_siege_dawn1.json",
            r"data/hd/env/vis/expansion_siege_dawn2.json",
            r"data/hd/env/vis/expansion_siege_day.json",
            r"data/hd/env/vis/expansion_siege_desecrated.json",
            r"data/hd/env/vis/expansion_siege_dusk1.json",
            r"data/hd/env/vis/expansion_siege_dusk2.json",
            r"data/hd/env/vis/expansion_siege_night.json",
            r"data/hd/env/vis/expansion_siege_town_dawn1.json",
            r"data/hd/env/vis/expansion_siege_town_dawn2.json",
            r"data/hd/env/vis/expansion_siege_town_day.json",
            r"data/hd/env/vis/expansion_siege_town_dusk1.json",
            r"data/hd/env/vis/expansion_siege_town_dusk2.json",
            r"data/hd/env/vis/expansion_siege_town_night.json",
            r"data/hd/env/vis/expansion_town_dawn1.json",
            r"data/hd/env/vis/expansion_town_dawn2.json",
            r"data/hd/env/vis/expansion_town_day.json",
            r"data/hd/env/vis/expansion_town_dusk1.json",
            r"data/hd/env/vis/expansion_town_dusk2.json",
            r"data/hd/env/vis/expansion_town_night.json",
            r"data/hd/env/vis/expansion_wildtemple_dawn1.json",
            r"data/hd/env/vis/expansion_wildtemple_dawn2.json",
            r"data/hd/env/vis/expansion_wildtemple_day.json",
            r"data/hd/env/vis/expansion_wildtemple_desecrated.json",
            r"data/hd/env/vis/expansion_wildtemple_dusk1.json",
            r"data/hd/env/vis/expansion_wildtemple_dusk2.json",
            r"data/hd/env/vis/expansion_wildtemple_night.json",
            r"data/hd/env/vis/expansion_wildtemple_tempenter_dawn1.json",
            r"data/hd/env/vis/expansion_wildtemple_tempenter_dawn2.json",
            r"data/hd/env/vis/expansion_wildtemple_tempenter_day.json",
            r"data/hd/env/vis/expansion_wildtemple_tempenter_desecrated.json",
            r"data/hd/env/vis/expansion_wildtemple_tempenter_dusk1.json",
            r"data/hd/env/vis/expansion_wildtemple_tempenter_dusk2.json",
            r"data/hd/env/vis/expansion_wildtemple_tempenter_night.json",
            r"data/hd/env/vis/graphics_dawn1.json",
            r"data/hd/env/vis/graphics_dawn2.json",
            r"data/hd/env/vis/graphics_day.json",
            r"data/hd/env/vis/graphics_dusk1.json",
            r"data/hd/env/vis/graphics_dusk2.json",
            r"data/hd/env/vis/graphics_night.json",
            r"data/hd/env/vis/lightroom_dawn1.json",
            r"data/hd/env/vis/lightroom_dawn2.json",
            r"data/hd/env/vis/lightroom_day.json",
            r"data/hd/env/vis/lightroom_dusk1.json",
            r"data/hd/env/vis/lightroom_dusk2.json",
            r"data/hd/env/vis/lightroom_night.json",
            r"data/hd/env/vis/viewer_units.json",
            r"data/hd/env/vis/visbox_act1_cathedral_vis.json",
            r"data/hd/env/vis/visbox_docktown_interior01_vis.json",
            r"data/hd/env/vis/visbox_harrograth_vis.json",
            r"data/hd/env/vis/visbox_kurast_hut_ambient_vis.json",
            r"data/hd/env/vis/visbox_kurast_temple_ambient_vis.json",
            r"data/hd/env/vis/visbox_monastry_vis.json",
            r"data/hd/env/vis/visbox_tempenter_darkness_vis.json",
            r"data/hd/env/vis/visbox_tempenter_roof_vis.json",
            r"data/hd/env/vis/visbox_tower_vis.json",
        ]
        
        return self.common_rename(files_env_vis, isEnabled)
    
    def toggle_monster_health(self, isEnabled: bool):
        """
        怪物血条加宽加高
        """
        files_monster_health = [
            r"data/global/ui/layouts/hudmonsterhealthhd.json",
        ]

        return self.common_rename(files_monster_health, isEnabled)
    
    def toggle_hurricane(self, isEnabled: bool):
        """
        德鲁伊飓风术特效
        """
        files_hurricane = [
            r"data/hd/missiles/expansion_hurricane_rocks.json",
            r"data/hd/missiles/expansion_hurricane_tree.json",
            r"data/hd/missiles/expansion_hurricane_swoosh.json",
        ]

        return self.common_rename(files_hurricane, isEnabled)
    
    def toggle_shrine(self, isEnabled: bool):
        """
        经验/宝石祭坛特效
        """
        files_common_shrine = [
            r"data/hd/overlays/common/shrine_experience.json",
            r"data/hd/overlays/common/shrine_stamina.json",
        ]

        return self.common_rename(files_common_shrine, isEnabled)

    def toggle_lightningbolt_big(self, isEnabled: bool):
        """
        屏蔽雷云风暴吓人特效
        """
        files_lightningbolt_big = [
            r"data/hd/missiles/lightningbolt_big.json",
        ]

        return self.common_rename(files_lightningbolt_big, isEnabled)
    
    def toggle_electric_nova(self, isEnabled: bool):
        """
        降低闪电新星亮度
        """
        files_electric_nova = [
            r"data/hd/missiles/electric_nova.json",
        ]

        return self.common_rename(files_electric_nova, isEnabled)

    def toogle_d2r_wiki(self, isEnabled: bool):
        """
        暗黑2百科
        """
        _files = [
            r"data/global/ui/layouts/hudpanel_realhd.json",
            r"data/global/ui/layouts/hudpanel_real.json",
        ]

        return self.common_rename(_files, isEnabled)
    
    def toggle_inventory_expansion(self, isEnabled: bool):
        """
        物品栏+精品词缀
        """
        _files = [
            r"data/global/ui/layouts/playerinventoryexpansionlayouthd.json",
        ]

        return self.common_rename(_files, isEnabled)
    
    def toggle_bank_expansion(self, isEnabled: bool):
        """
        储物箱+精品词缀
        """
        _files = [
            r"data/global/ui/layouts/bankexpansionlayouthd.json",
        ]

        return self.common_rename(_files, isEnabled)
    
    def toogle_cube_formula(self, isEnabled: bool):
        """
        方块+符文升级公式
        """
        _files = [
            r"data/global/ui/layouts/horadriccubelayouthd.json",
        ]

        return self.common_rename(_files, isEnabled)

    def toggle_shenk(self, isEnabled: bool):
        """
        # "屏蔽 A5督军山克死亡特效",
        """
        _files = [
            r"data/global/excel/missiles.txt",
        ]

        return self.common_rename(_files, isEnabled)
    
    def select_hireables_panel(self, radio: str):
        """
        佣兵图标位置
        """
        params = {
            "default": r"data/global/ui/layouts/hireablespanelhd.json",
            "1": r"data/global/ui/layouts/hireablespanelhd.json.1",
            "2": r"data/global/ui/layouts/hireablespanelhd.json.2",
            "3": r"data/global/ui/layouts/hireablespanelhd.json.3",
        }

        paths = [
            r"data/global/ui/layouts/hireablespanelhd.json"
        ]
        count = 0
        total = len(paths)
        for path in paths:
            src_path = os.path.join(self.dir_mod, params[radio])
            dst_path = os.path.join(self.dir_mod, path)
            if "default" == radio:
                os.remove(dst_path)
            else:
                shutil.copy2(src_path, dst_path)
            count += 1
        return (count, total)
    
    def select_character_effects(self, keys: list):
        """
        角色特效
        """

        params = {
            "1": {
                "type": "Entity",
                "name": "entity_root",
                "id": 1079187010,
                "components": [
                    {
                        "type": "VfxDefinitionComponent",
                        "name": "entity_root_VfxDefinition",
                        "filename": "data/hd/vfx/particles/overlays/paladin/aura_fanatic/aura_fanatic.particles",
                        "hardKillOnDestroy": False
                    }
                ]
            },
            "2": {
                "type": "Entity",
                "name": "entity_root",
                "id": 1079187010,
                "components": [
                    {
                        "type": "VfxDefinitionComponent",
                        "name": "entity_root_VfxDefinition",
                        "filename": "data/hd/vfx/particles/overlays/sorceress/thunderstormcast/ThunderCastOverlayOper.particles",
                        "hardKillOnDestroy": False
                    }
                ]
            },
            "3": {
                "type": "Entity",
                "name": "entity_root",
                "id": 1079187010,
                "components": [
                    {
                        "type": "VfxDefinitionComponent",
                        "name": "entity_root_VfxDefinition",
                        "filename": "data/hd/vfx/particles/missiles/high_priest_lightning/highpriestlightning_fx.particles",
                        "hardKillOnDestroy": False
                    },
                    {
                        "type": "TransformDefinitionComponent",
                        "name": "TransformDefinitionComponent002",
                        "position": {
                            "x": 0,
                            "y": 4,
                            "z": 0
                        },
                        "orientation": {
                            "x": 0,
                            "y": 0,
                            "z": 0,
                            "w": 1
                        },
                        "scale": {
                            "x": 1.8,
                            "y": 1.8,
                            "z": 1.8
                        },
                        "inheritOnlyPosition": False
                    }
                ]
            },
            "4": {
                "type": "Entity",
                "name": "entity_VFX",
                "id": 3636956308,
                "components": [
                    {
                        "type": "VfxDefinitionComponent",
                        "name": "entity_VFX_VfxDefinition",
                        "filename": "data/hd/vfx/particles/overlays/monster/fingermagecurse/fingerMage_curse.particles",
                        "hardKillOnDestroy": False
                    }
                ]
            },
            "5": [
                {
                    "type": "Entity",
                    "name": "entity_wings_shell",
                    "id": 2343070520,
                    "components": [
                        {
                            "type": "EntityAttachmentDefinitionComponent",
                            "name": "entity_spectralflames_EntityAttachmentDefinition",
                            "targetbone": "helmet"
                        },
                        {
                            "type": "ModelDefinitionComponent",
                            "name": "entity_wings_shell_ModelDefinition001",
                            "filename": "data/hd/character/npc/izualghost/bottomwings_lod0.model",
                            "visibleLayers": 1073741824,
                            "lightMask": 19,
                            "shadowMask": 3,
                            "ghostShadows": False,
                            "floorModel": False,
                            "terrainBlendEnableYUpBlend": False,
                            "terrainBlendMode": 1
                        },
                        {
                            "type": "TransformDefinitionComponent",
                            "name": "entity_wings_shell_TransformDefinition001",
                            "position": {
                                "x": 1,
                                "y": -1.6,
                                "z": -2
                            },
                            "orientation": {
                                "x": 0.15,
                                "y": 0,
                                "z": -0.6,
                                "w": 1
                            },
                            "scale": {
                                "x": 0.25,
                                "y": 0.35,
                                "z": 0.25
                            },
                            "inheritOnlyPosition": False
                        },
                        {
                            "type": "ObjectEffectDefinitionComponent",
                            "name": "entity_wings_shell_ObjectEffectDefinition001",
                            "filename": "data/hd/vfx/particles/character/enemy/willowisp1/vfx_willowisp1_neutral.particles"
                        }
                    ]
                },
                {
                    "type": "Entity",
                    "name": "entity_wings_shell",
                    "id": 2343070520,
                    "components": [
                        {
                            "type": "EntityAttachmentDefinitionComponent",
                            "name": "entity_spectralflames_EntityAttachmentDefinition",
                            "targetbone": "helmet"
                        },
                        {
                            "type": "ModelDefinitionComponent",
                            "name": "entity_wings_shell_ModelDefinition001",
                            "filename": "data/hd/character/npc/izualghost/bottomwings_vfx_lod0.model",
                            "visibleLayers": 1073741824,
                            "lightMask": 19,
                            "shadowMask": 3,
                            "ghostShadows": False,
                            "floorModel": False,
                            "terrainBlendEnableYUpBlend": False,
                            "terrainBlendMode": 1
                        },
                        {
                            "type": "TransformDefinitionComponent",
                            "name": "entity_wings_shell_TransformDefinition001",
                            "position": {
                                "x": -1,
                                "y": -1.6,
                                "z": -2
                            },
                            "orientation": {
                                "x": 0.15,
                                "y": 0,
                                "z": 0.6,
                                "w": 1
                            },
                            "scale": {
                                "x": 0.25,
                                "y": 0.35,
                                "z": 0.25
                            },
                            "inheritOnlyPosition": False
                        },
                        {
                            "type": "ObjectEffectDefinitionComponent",
                            "name": "entity_wings_shell_ObjectEffectDefinition001",
                            "filename": "data/hd/vfx/particles/character/enemy/willowisp1/vfx_willowisp1_neutral.particles"
                        }
                    ]
                }
            ]
        }

        _backup_path = r"data/hd/character/player/bak"
        _target_path = r"data/hd/character/player"


        paths = [
            r"amazon.json",
            r"assassin.json",
            r"barbarian.json",
            r"druid.json",
            r"necromancer.json",
            r"paladin.json",
            r"sorceress.json",
        ]

        count = 0
        total = len(paths)

        for path in paths:
            backup_path = os.path.join(self.dir_mod, _backup_path, path)
            target_path = os.path.join(self.dir_mod, _target_path, path)
            temp_path = target_path + ".tmp"
            try:
                # 1.load
                backup_data = None
                with open(backup_path, 'r', encoding='utf-8') as f:
                    backup_data = json.load(f)
                target_data = None
                with open(target_path, 'r', encoding='utf-8') as f:
                    target_data = json.load(f)

                # 2.modify
                for key in keys:
                    value = params.get(key)
                    if isinstance(value, list):
                        backup_data["entities"].extend(value)
                    else:
                        backup_data["entities"].append(value)


                backup_data["entities"].append(target_data["entities"][-1])

                # 3.write
                with open(temp_path, 'w', encoding="utf-8") as f:
                    json.dump(backup_data, f, ensure_ascii=False, indent=4)
                    
                # 5.replace
                os.replace(temp_path, target_path)
                count += 1
            except Exception as e:
                print(e)
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)

        return (count, total)

    def toggle_quick_buy(self, isEnabled:bool):
        """
        左键快速购买
        """
        _files = [
            r"data/global/ui/layouts/vendorpanellayouthd.json",
        ]

        return self.common_rename(_files, isEnabled)
    
    def load_filter_config(self):
        """
        读取道具过滤配置&相应item-names数据
        """
        # 0.data
        data = []

        # 1.load settings.json
        settings_path = os.path.join(self.dir_mod, "settings.json")
        settings_dict = None
        with open(settings_path, 'r', encoding="utf-8") as f:
            settings_dict = json.load(f)
        item_filter_states = settings_dict.get("501", {})
        
        # 2.load item-names.json 
        item_name_dict = {}
        item_names_path = os.path.join(self.dir_mod, r"data/local/lng/strings/item-names.original.json")
        item_names_data = None
        with open(item_names_path, 'r', encoding='utf-8-sig') as f:
            item_names_data = json.load(f)
        for i, item in enumerate(item_names_data):
            item_name_dict[str(item["id"])] = item

        # mix
        for id in item_filter_states:
            item_name = item_name_dict[id]
            data.append([
                id,
                id,
                item_name["enUS"],
                item_name["zhCN"],
                item_name["zhTW"],
            ])
        
        return data
    
    def modify_item_names(self, data):
        """
        修改 道具屏蔽
        """
        # 1.load item-names.json 
        item_name_dict = {}
        item_names_path = os.path.join(self.dir_mod, r"data/local/lng/strings/item-names.json")
        item_names_data = None
        with open(item_names_path, 'r', encoding='utf-8-sig') as f:
            item_names_data = json.load(f)
        for i, item in enumerate(item_names_data):
            item_name_dict[str(item["id"])] = item

        # 2.modify
        for id, filter in data.items():
            item_name = item_name_dict[id]
            item_name["enUS"] = self.UE01A + item_name["enUS"].removeprefix(self.UE01A) if filter else item_name["enUS"].removeprefix(self.UE01A)
            item_name["zhCN"] = self.UE01A + item_name["zhCN"].removeprefix(self.UE01A) if filter else item_name["zhCN"].removeprefix(self.UE01A)
            item_name["zhTW"] = self.UE01A + item_name["zhTW"].removeprefix(self.UE01A) if filter else item_name["zhTW"].removeprefix(self.UE01A)
            
        # 3.write
        with open(item_names_path, 'w', encoding='utf-8-sig') as f:
            json.dump(item_names_data, f, ensure_ascii=False, indent=2)

        return (1, 1)
    
    def select_rune_skin(self, radio: str):
        """
        符文皮肤
        """
        path = r"data/hd/global/ui/items/misc/rune"
        files = (
            r"amn_rune.lowend.sprite",
            r"amn_rune.sprite",
            r"ber_rune.lowend.sprite",
            r"ber_rune.sprite",
            r"cham_rune.lowend.sprite",
            r"cham_rune.sprite",
            r"dol_rune.lowend.sprite",
            r"dol_rune.sprite",
            r"eld_rune.lowend.sprite",
            r"eld_rune.sprite",
            r"el_rune.lowend.sprite",
            r"el_rune.sprite",
            r"eth_rune.lowend.sprite",
            r"eth_rune.sprite",
            r"fal_rune.lowend.sprite",
            r"fal_rune.sprite",
            r"gul_rune.lowend.sprite",
            r"gul_rune.sprite",
            r"hel_rune.lowend.sprite",
            r"hel_rune.sprite",
            r"io_rune.lowend.sprite",
            r"io_rune.sprite",
            r"ist_rune.lowend.sprite",
            r"ist_rune.sprite",
            r"ith_rune.lowend.sprite",
            r"ith_rune.sprite",
            r"jah_rune.lowend.sprite",
            r"jah_rune.sprite",
            r"ko_rune.lowend.sprite",
            r"ko_rune.sprite",
            r"lem_rune.lowend.sprite",
            r"lem_rune.sprite",
            r"lo_rune.lowend.sprite",
            r"lo_rune.sprite",
            r"lum_rune.lowend.sprite",
            r"lum_rune.sprite",
            r"mal_rune.lowend.sprite",
            r"mal_rune.sprite",
            r"nef_rune.lowend.sprite",
            r"nef_rune.sprite",
            r"ohm_rune.lowend.sprite",
            r"ohm_rune.sprite",
            r"ort_rune.lowend.sprite",
            r"ort_rune.sprite",
            r"pul_rune.lowend.sprite",
            r"pul_rune.sprite",
            r"ral_rune.lowend.sprite",
            r"ral_rune.sprite",
            r"shael_rune.lowend.sprite",
            r"shael_rune.sprite",
            r"sol_rune.lowend.sprite",
            r"sol_rune.sprite",
            r"sur_rune.lowend.sprite",
            r"sur_rune.sprite",
            r"tal_rune.lowend.sprite",
            r"tal_rune.sprite",
            r"thul_rune.lowend.sprite",
            r"thul_rune.sprite",
            r"tir_rune.lowend.sprite",
            r"tir_rune.sprite",
            r"um_rune.lowend.sprite",
            r"um_rune.sprite",
            r"vex_rune.lowend.sprite",
            r"vex_rune.sprite",
            r"zod_rune.lowend.sprite",
            r"zod_rune.sprite",
        )

        count = 0
        total = len(files)

        if(radio == "default"):
            for file in files:
                try:
                    dst = os.path.join(self.dir_mod, path, file)
                    os.remove(dst)
                    count += 1
                except Exception as e:
                    print(e)
        else:
            for file in files:
                try:
                    src = os.path.join(self.dir_mod, path, radio, file)
                    dst = os.path.join(self.dir_mod, path, file)
                    shutil.copy2(src, dst)
                    count += 1
                except Exception as e:
                    print(e)
        return (count, total)