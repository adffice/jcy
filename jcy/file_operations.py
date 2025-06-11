import csv
import json
import json5
import os
import shutil
from jcy_model import FeatureConfig

class FileOperations:
    """
    负责处理所有文件相关的操作，如复制和删除。
    """
    def __init__(self, config: FeatureConfig):
        self.config = config
        self.dir_mod = config.dir_mod

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
        开/关 MINI盒子
        """
        files_mini_cube = (
            r"data\global\ui\layouts\playerinventoryexpansionlayouthd.json",
        )

        return self.common_rename(files_mini_cube, isEnabled)

    def toggle_droped_highlight(self, isEnabled: bool):
        """
        开关 掉落光柱
        """
        files_droped_highlight = (
            r"data\hd\items\misc\charm\charm_large.json",
            r"data\hd\items\misc\charm\charm_small.json",
            r"data\hd\items\misc\gem\perfect_diamond.json",
            r"data\hd\items\misc\rune\ber_rune.json",
            r"data\hd\items\misc\rune\cham_rune.json",
            r"data\hd\items\misc\rune\gul_rune.json",
            r"data\hd\items\misc\rune\ist_rune.json",
            r"data\hd\items\misc\rune\jah_rune.json",
            r"data\hd\items\misc\rune\lem_rune.json",
            r"data\hd\items\misc\rune\lo_rune.json",
            r"data\hd\items\misc\rune\mal_rune.json",
            r"data\hd\items\misc\rune\ohm_rune.json",
            r"data\hd\items\misc\rune\pul_rune.json",
            r"data\hd\items\misc\rune\sur_rune.json",
            r"data\hd\items\misc\rune\um_rune.json",
            r"data\hd\items\misc\rune\vex_rune.json",
            r"data\hd\items\misc\rune\zod_rune.json",
            r"data\hd\items\misc\key\mephisto_key.json",
        )

        return self.common_rename(files_droped_highlight, isEnabled)

    def toggle_rune_sprite(self, isEnabled: bool):
        """
        开关 符文贴图
        """
        files_rune_sprite = (
            r"data\hd\global\ui\items\misc\rune\amn_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\amn_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\ber_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\ber_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\cham_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\cham_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\dol_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\dol_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\eld_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\eld_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\el_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\el_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\eth_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\eth_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\fal_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\fal_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\gul_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\gul_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\hel_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\hel_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\io_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\io_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\ist_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\ist_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\ith_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\ith_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\jah_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\jah_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\ko_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\ko_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\lem_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\lem_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\lo_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\lo_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\lum_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\lum_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\mal_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\mal_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\nef_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\nef_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\ohm_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\ohm_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\ort_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\ort_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\pul_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\pul_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\ral_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\ral_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\shael_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\shael_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\sol_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\sol_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\sur_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\sur_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\tal_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\tal_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\thul_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\thul_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\tir_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\tir_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\um_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\um_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\vex_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\vex_rune.sprite",
            r"data\hd\global\ui\items\misc\rune\zod_rune.lowend.sprite",
            r"data\hd\global\ui\items\misc\rune\zod_rune.sprite",
        )

        return self.common_rename(files_rune_sprite, isEnabled)

    def toggle_chest_highlight(self, isEnabled: bool):
        """
        开关 箱子高亮
        """
        files_chest_highlight = (
            r"data\hd\objects\armor_weapons\armor_stand_1.json",
            r"data\hd\objects\armor_weapons\armor_stand_2.json",
            r"data\hd\objects\armor_weapons\armor_stand_left.json",
            r"data\hd\objects\armor_weapons\armor_stand_right.json",
            r"data\hd\objects\armor_weapons\weapon_rack_1.json",
            r"data\hd\objects\armor_weapons\weapon_rack_2.json",
            r"data\hd\objects\armor_weapons\weapon_rack_left.json",
            r"data\hd\objects\armor_weapons\weapon_rack_right.json",
            r"data\hd\objects\caskets\act_3_dungeon_casket.json",
            r"data\hd\objects\caskets\arcane_casket_1.json",
            r"data\hd\objects\caskets\baal_tomb_1.json",
            r"data\hd\objects\caskets\baal_tomb_2.json",
            r"data\hd\objects\caskets\baal_tomb_3.json",
            r"data\hd\objects\caskets\casket_1.json",
            r"data\hd\objects\caskets\casket_2.json",
            r"data\hd\objects\caskets\casket_3.json",
            r"data\hd\objects\caskets\casket_4.json",
            r"data\hd\objects\caskets\casket_5.json",
            r"data\hd\objects\caskets\casket_6.json",
            r"data\hd\objects\caskets\desert_coffin.json",
            r"data\hd\objects\caskets\ground_tomb.json",
            r"data\hd\objects\caskets\mummy_casket.json",
            r"data\hd\objects\caskets\tomb_act_2.json",
            r"data\hd\objects\caskets\tomb_baal_1.json",
            r"data\hd\objects\caskets\tomb_baal_2.json",
            r"data\hd\objects\caskets\tomb_baal_3.json",
            r"data\hd\objects\caskets\tomb_baal_4.json",
            r"data\hd\objects\caskets\tomb_baal_5.json",
            r"data\hd\objects\caskets\tomb_baal_6.json",
            r"data\hd\objects\caskets\tomb_baal_7.json",
            r"data\hd\objects\caskets\tomb_baal_8.json",
            r"data\hd\objects\caskets\tomb_baal_9.json",
            r"data\hd\objects\caskets\yet_another_tomb.json",
            r"data\hd\objects\characters\burned_body_1_act_1.json",
            r"data\hd\objects\characters\corpse_1_act_3.json",
            r"data\hd\objects\characters\corpse_2_act_3.json",
            r"data\hd\objects\characters\corpse_3.json",
            r"data\hd\objects\characters\corpse_skeleton.json",
            r"data\hd\objects\characters\damned_v_1.json",
            r"data\hd\objects\characters\damned_v_2.json",
            r"data\hd\objects\characters\dead_barbarian.json",
            r"data\hd\objects\characters\dead_palace_guard.json",
            r"data\hd\objects\characters\dead_person.json",
            r"data\hd\objects\characters\dead_person_again.json",
            r"data\hd\objects\characters\dungeon_guy.json",
            r"data\hd\objects\characters\guard_corpse_2_act_2.json",
            r"data\hd\objects\characters\guard_on_a_stick.json",
            r"data\hd\objects\characters\harem_guard_1.json",
            r"data\hd\objects\characters\harem_guard_2.json",
            r"data\hd\objects\characters\harem_guard_3.json",
            r"data\hd\objects\characters\harem_guard_4.json",
            r"data\hd\objects\characters\jack_in_the_box_1.json",
            r"data\hd\objects\characters\jack_in_the_box_2.json",
            r"data\hd\objects\characters\rogue_corpse_1.json",
            r"data\hd\objects\characters\rogue_corpse_2.json",
            r"data\hd\objects\characters\rogue_rolling_corpse_1.json",
            r"data\hd\objects\characters\rogue_staked_corpse_1.json",
            r"data\hd\objects\characters\rogue_staked_corpse_2.json",
            r"data\hd\objects\characters\sewer_dungeon_body.json",
            r"data\hd\objects\characters\wirt.json",
            r"data\hd\objects\characters\yet_another_dead_body.json",
            r"data\hd\objects\chests\arcane_chest_1.json",
            r"data\hd\objects\chests\arcane_chest_2.json",
            r"data\hd\objects\chests\arcane_chest_3.json",
            r"data\hd\objects\chests\arcane_chest_4.json",
            r"data\hd\objects\chests\chest_1_b.json",
            r"data\hd\objects\chests\chest_2.json",
            r"data\hd\objects\chests\chest_2_b.json",
            r"data\hd\objects\chests\chest_3.json",
            r"data\hd\objects\chests\chest_3_b.json",
            r"data\hd\objects\chests\chest_4.json",
            r"data\hd\objects\chests\chest_5.json",
            r"data\hd\objects\chests\chest_6.json",
            r"data\hd\objects\chests\chest_7.json",
            r"data\hd\objects\chests\chest_8.json",
            r"data\hd\objects\chests\chest_burial_r.json",
            r"data\hd\objects\chests\chest_bur_i_all.json",
            r"data\hd\objects\chests\chest_outdoor_1.json",
            r"data\hd\objects\chests\chest_outdoor_2.json",
            r"data\hd\objects\chests\chest_outdoor_3.json",
            r"data\hd\objects\chests\chest_outdoor_4.json",
            r"data\hd\objects\chests\cloth_chest_l.json",
            r"data\hd\objects\chests\cloth_chest_r.json",
            r"data\hd\objects\chests\consolation_chest.json",
            r"data\hd\objects\chests\forgotten_tower_chest.json",
            r"data\hd\objects\chests\jungle_chest.json",
            r"data\hd\objects\chests\jungle_chest_2.json",
            r"data\hd\objects\chests\large_chest_l.json",
            r"data\hd\objects\chests\large_chest_r.json",
            r"data\hd\objects\chests\sewer_chest.json",
            r"data\hd\objects\chests\sewer_chest_large_left.json",
            r"data\hd\objects\chests\sewer_chest_med_right.json",
            r"data\hd\objects\chests\sewer_chest_tall_left.json",
            r"data\hd\objects\chests\sewer_chest_tall_right.json",
            r"data\hd\objects\chests\snow_chest_l.json",
            r"data\hd\objects\chests\snow_chest_r.json",
            r"data\hd\objects\chests\snow_cloth_chest_l.json",
            r"data\hd\objects\chests\snow_cloth_chest_r.json",
            r"data\hd\objects\chests\snow_wood_chest_l.json",
            r"data\hd\objects\chests\snow_wood_chest_r.json",
            r"data\hd\objects\chests\special_chest_100.json",
            r"data\hd\objects\chests\tomb_chest_1.json",
            r"data\hd\objects\chests\tomb_chest_2.json",
            r"data\hd\objects\chests\travincal_chest_large_left.json",
            r"data\hd\objects\chests\travincal_chest_large_right.json",
            r"data\hd\objects\chests\travincal_chest_med_left.json",
            r"data\hd\objects\chests\travincal_chest_med_right.json",
            r"data\hd\objects\chests\wood_chest_l.json",
            r"data\hd\objects\chests\wood_chest_r.json",
            r"data\hd\objects\destructibles\barrel.json",
            r"data\hd\objects\destructibles\barrel_3.json",
            r"data\hd\objects\destructibles\barrel_exploding.json",
            r"data\hd\objects\destructibles\basket_1.json",
            r"data\hd\objects\destructibles\basket_2.json",
            r"data\hd\objects\destructibles\box_1.json",
            r"data\hd\objects\destructibles\box_2.json",
            r"data\hd\objects\destructibles\crate.json",
            r"data\hd\objects\destructibles\dungeon_basket.json",
            r"data\hd\objects\destructibles\dungeon_rock_pile.json",
            r"data\hd\objects\destructibles\exploding_chest_100.json",
            r"data\hd\objects\destructibles\e_jar_1.json",
            r"data\hd\objects\destructibles\e_jar_2.json",
            r"data\hd\objects\destructibles\e_jar_3.json",
            r"data\hd\objects\destructibles\ice_cave_evil_urn.json",
            r"data\hd\objects\destructibles\ice_cave_jar_1.json",
            r"data\hd\objects\destructibles\ice_cave_jar_2.json",
            r"data\hd\objects\destructibles\ice_cave_jar_3.json",
            r"data\hd\objects\destructibles\ice_cave_jar_4.json",
            r"data\hd\objects\destructibles\ice_cave_jar_5.json",
            r"data\hd\objects\destructibles\jug_outdoor_1.json",
            r"data\hd\objects\destructibles\jug_outdoor_2.json",
            r"data\hd\objects\destructibles\pillar_2.json",
            r"data\hd\objects\destructibles\urn_1.json",
            r"data\hd\objects\destructibles\urn_2.json",
            r"data\hd\objects\destructibles\urn_3.json",
            r"data\hd\objects\destructibles\urn_4.json",
            r"data\hd\objects\destructibles\urn_5.json",
            r"data\hd\objects\env_manmade\barrel_2.json",
            r"data\hd\objects\env_manmade\bookshelf_1.json",
            r"data\hd\objects\env_manmade\bookshelf_2.json",
            r"data\hd\objects\env_manmade\compelling_orb.json",
            r"data\hd\objects\env_manmade\hole_in_ground.json",
            r"data\hd\objects\env_organic\cocoon_1.json",
            r"data\hd\objects\env_organic\cocoon_2.json",
            r"data\hd\objects\env_organic\goo_pile.json",
            r"data\hd\objects\env_organic\sewer_rat_nest.json",
            r"data\hd\objects\env_pillars\ancients_altar.json",
            r"data\hd\objects\env_pillars\ice_cave_object_1.json",
            r"data\hd\objects\env_pillars\inside_altar.json",
            r"data\hd\objects\env_pillars\jungle_pillar_0.json",
            r"data\hd\objects\env_pillars\jungle_pillar_1.json",
            r"data\hd\objects\env_pillars\jungle_pillar_2.json",
            r"data\hd\objects\env_pillars\jungle_pillar_3.json",
            r"data\hd\objects\env_pillars\mephisto_pillar_1.json",
            r"data\hd\objects\env_pillars\mephisto_pillar_2.json",
            r"data\hd\objects\env_pillars\mephisto_pillar_3.json",
            r"data\hd\objects\env_pillars\obelisk_1.json",
            r"data\hd\objects\env_pillars\obelisk_2.json",
            r"data\hd\objects\env_pillars\object_1_temple.json",
            r"data\hd\objects\env_pillars\object_2_temple.json",
            r"data\hd\objects\env_pillars\snowy_generic_name.json",
            r"data\hd\objects\env_pillars\steeg_stone.json",
            r"data\hd\objects\env_pillars\stone_stash.json",
            r"data\hd\objects\env_pillars\tower_tome.json",
            r"data\hd\objects\env_skeletons\e_shit.json",
            r"data\hd\objects\env_skeletons\hell_bone_pile.json",
            r"data\hd\objects\env_skeletons\inner_hell_object_1.json",
            r"data\hd\objects\env_skeletons\inner_hell_object_2.json",
            r"data\hd\objects\env_skeletons\inner_hell_object_3.json",
            r"data\hd\objects\env_skeletons\outer_hell_object_1.json",
            r"data\hd\objects\env_skeletons\outer_hell_skeleton.json",
            r"data\hd\objects\env_skeletons\skull_pile.json",
            r"data\hd\objects\env_stone\hidden_stash.json",
            r"data\hd\objects\env_stone\rock.json",
            r"data\hd\objects\env_stone\rock_c.json",
            r"data\hd\objects\env_stone\rock_d.json",
            r"data\hd\objects\env_wood\log.json",
        )

        return self.common_rename(files_chest_highlight, isEnabled)

    def toggle_entrance_arrow(self, isEnabled: bool):
        """
        开关 入口/小站八方箭头
        """
        files_entrance_arrow = (
            r"data\hd\objects\env_pillars\Arcane_tome.json",
            r"data\hd\objects\env_pillars\Seven_tombs_receptacle.json",
            r"data\hd\objects\env_stone\Stone_alpha.json",
            r"data\hd\objects\waypoint_portals\sewer_waypoint.json",
            r"data\hd\objects\waypoint_portals\temple_waypoint.json",
            r"data\hd\objects\waypoint_portals\travincal_waypoint.json",
            r"data\hd\objects\waypoint_portals\waypoint_act_2.json",
            r"data\hd\objects\waypoint_portals\waypoint_act_3.json",
            r"data\hd\objects\waypoint_portals\waypoint_baal.json",
            r"data\hd\objects\waypoint_portals\waypoint_cellar.json",
            r"data\hd\objects\waypoint_portals\waypoint_exp.json",
            r"data\hd\objects\waypoint_portals\waypoint_ice_cave.json",
            r"data\hd\objects\waypoint_portals\waypoint_inside_act_1.json",
            r"data\hd\objects\waypoint_portals\waypoint_outside_act_1.json",
            r"data\hd\objects\waypoint_portals\waypoint_outside_act_4.json",
            r"data\hd\objects\waypoint_portals\waypoint_wilderness.json",
            r"data\hd\roomtiles\act_5_temple_down.json",
            r"data\hd\roomtiles\act_1_catacombs_down.json",
            r"data\hd\roomtiles\act_1_crypt_down.json",
            r"data\hd\roomtiles\act_1_jail_down.json",
            r"data\hd\roomtiles\act_1_jail_up.json",
            r"data\hd\roomtiles\act_1_tower_to_crypt.json",
            r"data\hd\roomtiles\act_1_wilderness_to_cave_cliff_l.json",
            r"data\hd\roomtiles\act_1_wilderness_to_cave_cliff_r.json",
            r"data\hd\roomtiles\act_1_wilderness_to_cave_floor_l.json",
            r"data\hd\roomtiles\act_1_wilderness_to_cave_floor_r.json",
            r"data\hd\roomtiles\act_1_wilderness_to_tower.json",
            r"data\hd\roomtiles\act_2_desert_to_lair.json",
            r"data\hd\roomtiles\act_2_desert_to_sewer_trap.json",
            r"data\hd\roomtiles\act_2_desert_to_tomb_l_1.json",
            r"data\hd\roomtiles\act_2_desert_to_tomb_l_2.json",
            r"data\hd\roomtiles\act_2_desert_to_tomb_r_1.json",
            r"data\hd\roomtiles\act_2_desert_to_tomb_r_2.json",
            r"data\hd\roomtiles\act_2_desert_to_tomb_viper.json",
            r"data\hd\roomtiles\act_2_lair_down.json",
            r"data\hd\roomtiles\act_2_sewer_down.json",
            r"data\hd\roomtiles\act_2_tomb_down.json",
            r"data\hd\roomtiles\act_3_dungeon_down.json",
            r"data\hd\roomtiles\act_3_jungle_to_dungeon_fort.json",
            r"data\hd\roomtiles\act_3_jungle_to_dungeon_hole.json",
            r"data\hd\roomtiles\act_3_jungle_to_spider.json",
            r"data\hd\roomtiles\act_3_kurast_to_temple.json",
            r"data\hd\roomtiles\act_3_mephisto_down_l.json",
            r"data\hd\roomtiles\act_3_mephisto_down_r.json",
            r"data\hd\roomtiles\act_3_sewer_down.json",
            r"data\hd\roomtiles\act_4_mesa_to_lava.json",
            r"data\hd\roomtiles\act_5_baal_temple_down_l.json",
            r"data\hd\roomtiles\act_5_baal_temple_down_r.json",
            r"data\hd\roomtiles\act_5_barricade_down_wall_l.json",
            r"data\hd\roomtiles\act_5_barricade_down_wall_r.json",
            r"data\hd\roomtiles\act_5_ice_caves_down_floor.json",
            r"data\hd\roomtiles\act_5_ice_caves_down_l.json",
            r"data\hd\roomtiles\act_5_ice_caves_down_r.json",
        )

        return self.common_rename(files_entrance_arrow, isEnabled)

    def toggle_low_quality(self, isEnabled: bool):
        """
        开关 屏蔽垃圾道具
        """
        files_ui = (
            (
                r"data\local\lng\strings\ui.filter.json",
                r"data\local\lng\strings\ui.fully.json", 
                r"data\local\lng\strings\ui.json",
            ),
        )

        return self.common_swap(files_ui, isEnabled)

    def toggle_other_misc(self, isEnabled: bool):
        """
        开关 屏蔽垃圾道具
        """
        files_misc = (
            (
                r"data\local\lng\strings\item-names.filter.json",
                r"data\local\lng\strings\item-names.fully.json", 
                r"data\local\lng\strings\item-names.json",
            ),
        )

        return self.common_swap(files_misc, isEnabled)

    def toggle_player_light(self, isEnabled: bool):
        """
        开/关 角色灯光
        """
        files_character_lighting = (
            r"data\hd\character\player\amazon.json",
            r"data\hd\character\player\assassin.json",
            r"data\hd\character\player\barbarian.json",
            r"data\hd\character\player\druid.json",
            r"data\hd\character\player\necromancer.json",
            r"data\hd\character\player\paladin.json",
            r"data\hd\character\player\sorceress.json",
        )

        return self.common_rename(files_character_lighting, isEnabled)

    def toggle_no_mosaic_sin(self, isEnabled: bool):
        """
        开关 马赛克护眼
        """
        files_no_mosaic_sin = (
            r"data\hd\missiles\ground_fire_medium.json",
            r"data\hd\missiles\ground_fire_small.json",
            r"data\hd\missiles\missiles.json",
        )

        return self.common_rename(files_no_mosaic_sin, isEnabled)

    def toggle_escape(self, isEnabled: bool):
        """
        开关 Esc退出
        """
        files_escape = (
            r"data\global\ui\layouts\hudpanelhd.json",
            r"data\global\ui\layouts\pauselayout.json", 
            r"data\global\ui\layouts\pauselayouthd.json",
        )

        return self.common_rename(files_escape, isEnabled) 

    def toggle_magic_arrow(self, isEnabled: bool):
        """
        开关 魔法箭特效
        """
        files_hd_missiles_arrows = (
            r"data\hd\missiles\arrow.json",
            r"data\hd\missiles\x_bow_bolt.json",
        )

        return self.common_rename(files_hd_missiles_arrows, isEnabled)

    def toggle_hd_env_presets(self, isEnabled: bool):
        """
        开关 地形变化 (A2贤者之谷小站, A3崔凡克, A4混沌庇护所, A5毁灭王座)
        """
        files_hd_env_presets = (
            r"data\hd\env\preset\act2\outdoors\kingwarp.json",
            r"data\hd\env\preset\act3\travincal\travn.json",
            r"data\hd\env\preset\act4\diab\entry1.json",
            r"data\hd\env\preset\expansion\baallair\wthrone.json",
        )
        
        return self.common_rename(files_hd_env_presets, isEnabled)

    def toggle_lava_river_flow(self, isEnabled: bool):
        """
        开关 屏蔽火焰之河岩浆特效
        """
        files_lava_effect = (
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge1_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge1_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge1_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge1_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge1_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge3_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge3_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge3_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge3_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge3_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge4_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge4_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge4_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge4_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridge4_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridgelava_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridgelava_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridgelava_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridgelava_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_bridgelava_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_entry1_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_entry1_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_entry1_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_entry1_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_entry1_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_heart_center_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_heart_center_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_heart_center_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_heart_center_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_heart_center_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_heart_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_heart_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_heart_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_heart_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_heart_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_winge1_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_winge1_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_winge1_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_winge1_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_winge1_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_winge2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_winge2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_winge2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_winge2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_winge2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingn1_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingn1_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingn1_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingn1_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingn1_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingn2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingn2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingn2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingn2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingn2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wings1_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wings1_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wings1_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wings1_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wings1_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wings2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wings2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wings2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wings2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wings2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingw1_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingw1_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingw1_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingw1_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingw1_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingw2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingw2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingw2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingw2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\diab_wingw2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavae2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavae2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavae2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavae2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavae2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaew2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaew2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaew2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaew2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaew2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaew_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaew_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaew_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaew_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaew_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavae_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavae_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavae_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavae_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavae_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavan2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavan2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavan2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavan2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavan2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavans2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavans2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavans2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavans2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavans2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavans_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavans_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavans_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavans_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavans_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavan_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavan_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavan_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavan_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavan_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavas2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavas2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavas2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavas2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavas2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavas_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavas_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavas_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavas_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavas_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaw2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaw2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaw2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaw2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaw2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaw_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaw_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaw_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaw_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\expansion_lavaw_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_forgee_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_forgee_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_forgee_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_forgee_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_forgee_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_forgew_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_forgew_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_forgew_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_forgew_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_forgew_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_heart_center_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_heart_center_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_heart_center_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_heart_center_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_heart_center_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavae2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavae2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavae2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavae2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavae2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaew2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaew2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaew2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaew2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaew2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaew_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaew_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaew_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaew_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaew_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavae_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavae_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavae_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavae_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavae_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavan2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavan2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavan2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavan2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavan2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavane2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavane2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavane2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavane2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavane2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanew2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanew2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanew2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanew2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanew2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanew_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanew_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanew_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanew_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanew_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavane_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavane_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavane_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavane_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavane_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavans2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavans2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavans2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavans2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavans2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanse2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanse2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanse2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanse2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanse2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansew2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansew2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansew2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansew2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansew2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansew_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansew_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansew_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansew_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansew_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanse_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanse_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanse_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanse_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanse_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansw2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansw2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansw2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansw2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansw2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansw_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansw_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansw_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansw_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavansw_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavans_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavans_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavans_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavans_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavans_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanw2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanw2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanw2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanw2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanw2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanw_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanw_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanw_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanw_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavanw_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavan_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavan_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavan_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavan_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavan_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavas2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavas2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavas2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavas2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavas2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavase2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavase2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavase2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavase2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavase2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasew2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasew2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasew2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasew2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasew2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasew_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasew_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasew_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasew_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasew_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavase_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavase_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavase_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavase_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavase_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasw2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasw2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasw2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasw2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasw2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasw_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasw_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasw_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasw_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavasw_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavas_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavas_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavas_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavas_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavas_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaw2_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaw2_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaw2_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaw2_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaw2_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaw_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaw_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaw_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaw_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavaw_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavax_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavax_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavax_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavax_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_lavax_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_warpmesa1_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_warpmesa1_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_warpmesa1_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_warpmesa1_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_warpmesa1_lod4.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_warpmesa_lod0.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_warpmesa_lod1.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_warpmesa_lod2.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_warpmesa_lod3.model",
            r"data\hd\env\model\act4\lava\act4_lava_river_flow\lava_warpmesa_lod4.model",
        )

        return self.common_empty_file(files_lava_effect, isEnabled)

    def toggle_experience_bar(self, isEnabled: bool):
        """
        开关 经验条变色
        """
        files_experience_bar = (
            r"data\hd\global\ui\panel\hud_02\experience_bar.lowend.sprite",
            r"data\hd\global\ui\panel\hud_02\experience_bar.sprite",
        )

        return self.common_rename(files_experience_bar, isEnabled)
    
    def toggle_sound(self, isEnabled: bool):
        """
        开关 咒符/符文/技能结束提示音
        """
        files_sound = (
            r"data\global\excel\misc.txt",
            r"data\global\excel\states.txt",
        )

        return self.common_rename(files_sound, isEnabled)
    
    def toggle_hd_global_palette_randtransforms_json(self, isEnabled: bool):
        """
        开关 变色精英怪
        """
        files_random_elite = (
            r"data\hd\global\palette\randtransforms.json",
        )

        return self.common_rename(files_random_elite, isEnabled)

    def toggle_global_excel_affixes(self, isEnabled: bool):
        """
        开关 特殊词缀装备变色
        """
        files_global_excel_affixes = (
            r"data\global\excel\magicprefix.txt",
            r"data\global\excel\magicsuffix.txt",
            r"data\global\ui\layouts\globaldatahd.json"
        )

        return self.common_rename(files_global_excel_affixes, isEnabled)

    def toggle_mephisto_key(self, isEnabled: bool):
        """
        开关 6BOSS钥匙皮肤
        """
        files_key = (
            r"data\hd\items\items.json",
        )
        return self.common_rename(files_key, isEnabled)

    def toggle_hellfire_torch(self, isEnabled: bool):
        """
        开关 屏蔽地狱火炬火焰风暴特效
        开: 修改skill.txt文件 
        关: 修改skill.txt文件 
        """
        global_excel_skills_txt = {
            "file": r"data\global\excel\skills.txt",
            "diabwall": [
                {"col": "ItemCltEffect", "row": "DiabWall", True: "200", False: ""}
            ]
        }

        file_path = os.path.join(self.dir_mod, global_excel_skills_txt["file"])
        temp_path = file_path + ".tmp"
        file_data = global_excel_skills_txt["diabwall"]

        try:
            original_formatted_rows = [] # 源数据列表(保持样式)
            working_unquoted_rows = [] # 干净数据列表(操作用)
            skills = [] # 首列=技能名称
            # 1.读取数据
            with open(file_path, 'r', newline='', encoding='utf-8') as f:
                for line_num, line in enumerate(f):
                    line = line.rstrip('\r\n') # 移除行末的换行符，避免写入时多余空行
                    
                    # 使用 split('\t') 分割原始行。此时，如果原始文件有引号，字段会保留引号。
                    current_original_fields = line.split('\t') 
                    original_formatted_rows.append(current_original_fields)
                    
                    # 为工作台创建一份“去引号”的副本。这使得后续的查找和修改更简单。
                    current_unquoted_fields = [
                        field.strip('"') if field.startswith('"') and field.endswith('"') else field 
                        for field in current_original_fields
                    ]
                    working_unquoted_rows.append(current_unquoted_fields)
                    skills.append(current_unquoted_fields[0])
            # 2.修改数据
            for data in file_data:
                x = skills.index(data["row"])
                y = working_unquoted_rows[0].index(data["col"])

                original_value = original_formatted_rows[x][y]
                new_value = data[isEnabled]

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
        except Exception as e:
            print(e)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
        return (1, 1)