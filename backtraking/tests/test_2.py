#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""test foreground and background colors"""

import time
from colored import fg, bg, attr


def main():

    colors = (

        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "light_gray",
        "dark_gray",
        "light_red",
        "light_green",
        "light_yellow",
        "light_blue",
        "light_magenta",
        "light_cyan",
        "white",
        "grey_0",
        "navy_blue",
        "dark_blue",
        "blue_3a",
        "blue_3b",
        "blue_1",
        "dark_green",
        "deep_sky_blue_4a",
        "deep_sky_blue_4b",
        "deep_sky_blue_4c",
        "dodger_blue_3",
        "dodger_blue_2",
        "green_4",
        "spring_green_4",
        "turquoise_4",
        "deep_sky_blue_3a",
        "deep_sky_blue_3b",
        "dodger_blue_1",
        "green_3a",
        "spring_green_3a",
        "dark_cyan",
        "light_sea_green",
        "deep_sky_blue_2",
        "deep_sky_blue_1",
        "green_3b",
        "spring_green_3b",
        "spring_green_2a",
        "cyan_3",
        "dark_turquoise",
        "turquoise_2",
        "green_1",
        "spring_green_2b",
        "spring_green_1",
        "medium_spring_green",
        "cyan_2",
        "cyan_1",
        "dark_red_1",
        "deep_pink_4a",
        "purple_4a",
        "purple_4b",
        "purple_3",
        "blue_violet",
        "orange_4a",
        "grey_37",
        "medium_purple_4",
        "slate_blue_3a",
        "slate_blue_3b",
        "royal_blue_1",
        "chartreuse_4",
        "dark_sea_green_4a",
        "pale_turquoise_4",
        "steel_blue",
        "steel_blue_3",
        "cornflower_blue",
        "chartreuse_3a",
        "dark_sea_green_4b",
        "cadet_blue_2",
        "cadet_blue_1",
        "sky_blue_3",
        "steel_blue_1a",
        "chartreuse_3b",
        "pale_green_3a",
        "sea_green_3",
        "aquamarine_3",
        "medium_turquoise",
        "steel_blue_1b",
        "chartreuse_2a",
        "sea_green_2",
        "sea_green_1a",
        "sea_green_1b",
        "aquamarine_1a",
        "dark_slate_gray_2",
        "dark_red_2",
        "deep_pink_4b",
        "dark_magenta_1",
        "dark_magenta_2",
        "dark_violet_1a",
        "purple_1a",
        "orange_4b",
        "light_pink_4",
        "plum_4",
        "medium_purple_3a",
        "medium_purple_3b",
        "slate_blue_1",
        "yellow_4a",
        "wheat_4",
        "grey_53",
        "light_slate_grey",
        "medium_purple",
        "light_slate_blue",
        "yellow_4b",
        "dark_olive_green_3a",
        "dark_green_sea",
        "light_sky_blue_3a",
        "light_sky_blue_3b",
        "sky_blue_2",
        "chartreuse_2b",
        "dark_olive_green_3b",
        "pale_green_3b",
        "dark_sea_green_3a",
        "dark_slate_gray_3",
        "sky_blue_1",
        "chartreuse_1",
        "light_green_2",
        "light_green_3",
        "pale_green_1a",
        "aquamarine_1b",
        "dark_slate_gray_1",
        "red_3a",
        "deep_pink_4c",
        "medium_violet_red",
        "magenta_3a",
        "dark_violet_1b",
        "purple_1b",
        "dark_orange_3a",
        "indian_red_1a",
        "hot_pink_3a",
        "medium_orchid_3",
        "medium_orchid",
        "medium_purple_2a",
        "dark_goldenrod",
        "light_salmon_3a",
        "rosy_brown",
        "grey_63",
        "medium_purple_2b",
        "medium_purple_1",
        "gold_3a",
        "dark_khaki",
        "navajo_white_3",
        "grey_69",
        "light_steel_blue_3",
        "light_steel_blue",
        "yellow_3a",
        "dark_olive_green_3",
        "dark_sea_green_3b",
        "dark_sea_green_2",
        "light_cyan_3",
        "light_sky_blue_1",
        "green_yellow",
        "dark_olive_green_2",
        "pale_green_1b",
        "dark_sea_green_5b",
        "dark_sea_green_5a",
        "pale_turquoise_1",
        "red_3b",
        "deep_pink_3a",
        "deep_pink_3b",
        "magenta_3b",
        "magenta_3c",
        "magenta_2a",
        "dark_orange_3b",
        "indian_red_1b",
        "hot_pink_3b",
        "hot_pink_2",
        "orchid",
        "medium_orchid_1a",
        "orange_3",
        "light_salmon_3b",
        "light_pink_3",
        "pink_3",
        "plum_3",
        "violet",
        "gold_3b",
        "light_goldenrod_3",
        "tan",
        "misty_rose_3",
        "thistle_3",
        "plum_2",
        "yellow_3b",
        "khaki_3",
        "light_goldenrod_2a",
        "light_yellow_3",
        "grey_84",
        "light_steel_blue_1",
        "yellow_2",
        "dark_olive_green_1a",
        "dark_olive_green_1b",
        "dark_sea_green_1",
        "honeydew_2",
        "light_cyan_1",
        "red_1",
        "deep_pink_2",
        "deep_pink_1a",
        "deep_pink_1b",
        "magenta_2b",
        "magenta_1",
        "orange_red_1",
        "indian_red_1c",
        "indian_red_1d",
        "hot_pink_1a",
        "hot_pink_1b",
        "medium_orchid_1b",
        "dark_orange",
        "salmon_1",
        "light_coral",
        "pale_violet_red_1",
        "orchid_2",
        "orchid_1",
        "orange_1",
        "sandy_brown",
        "light_salmon_1",
        "light_pink_1",
        "pink_1",
        "plum_1",
        "gold_1",
        "light_goldenrod_2b",
        "light_goldenrod_2c",
        "navajo_white_1",
        "misty_rose1",
        "thistle_1",
        "yellow_1",
        "light_goldenrod_1",
        "khaki_1",
        "wheat_1",
        "cornsilk_1",
        "grey_100",
        "grey_3",
        "grey_7",
        "grey_11",
        "grey_15",
        "grey_19",
        "grey_23",
        "grey_27",
        "grey_30",
        "grey_35",
        "grey_39",
        "grey_42",
        "grey_46",
        "grey_50",
        "grey_54",
        "grey_58",
        "grey_62",
        "grey_66",
        "grey_70",
        "grey_74",
        "grey_78",
        "grey_82",
        "grey_85",
        "grey_89",
        "grey_93"
    )

    for color in colors:
        print(
            "{}This text is colored: {}{}".format(
                fg(color),
                color,
                attr("reset")))
        print(
            "{}This text is colored: {}{}".format(
                bg(color),
                color,
                attr("reset")))
        time.sleep(0.1)


if __name__ == "__main__":
    main()