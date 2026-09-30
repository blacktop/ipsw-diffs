## STF

> `/System/Library/VideoProcessors/STF.bundle/STF`

```diff

-  __TEXT.__text: 0xfcd20
+  __TEXT.__text: 0xf9128
   __TEXT.__objc_methlist: 0x171c
   __TEXT.__const: 0x580
   __TEXT.__oslogstring: 0x1c4b
   __TEXT.__cstring: 0x84c5
   __TEXT.__gcc_except_tab: 0x24c
-  __TEXT.__unwind_info: 0xea8
-  __TEXT.__eh_frame: 0x5c0
+  __TEXT.__unwind_info: 0xeb0
+  __TEXT.__eh_frame: 0x608
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0xcf0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__got: 0x0
+  __DATA_CONST.__got: 0x190
   __AUTH_CONST.__const: 0x388
   __AUTH_CONST.__cfstring: 0xfa0
   __AUTH_CONST.__objc_const: 0x3dd0
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__oslogstring : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ _cblas_isamax$NEWLAPACK : 596 -> 588
~ -[STFLtmFrameProcessorV1 computeBinned8BitsMonochromeThumbnail:width:height:binnedThumbnail:] : 836 -> 828
~ __ZN11accelerate210production23trsm_left_upper_fms_1x4IfLb1ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1408 -> 1276
~ __ZN11accelerate210production23trsm_left_upper_fms_1x4IfLb1ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1260 -> 1120
~ __ZN11accelerate210production23trsm_left_upper_fms_1x2IfLb1ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 984 -> 824
~ __ZN11accelerate210production23trsm_left_upper_fms_1x2IfLb1ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 812 -> 644
~ __ZN11accelerate210production23trsm_left_upper_fms_1x4IfLb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1436 -> 1300
~ __ZN11accelerate210production23trsm_left_upper_fms_1x4IfLb1ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1284 -> 1144
~ __ZN11accelerate210production23trsm_left_upper_fms_1x2IfLb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1040 -> 876
~ __ZN11accelerate210production23trsm_left_upper_fms_1x2IfLb1ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 836 -> 672
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb1ELb1ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1340 -> 1240
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb1ELb1ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1172 -> 1076
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb1ELb1ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 980 -> 884
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb1ELb1ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 832 -> 740
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1320 -> 1220
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1152 -> 1060
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 932 -> 836
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 816 -> 724
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb1ELb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1540 -> 1440
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb1ELb1ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1392 -> 1272
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb1ELb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1188 -> 1080
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb1ELb1ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1008 -> 928
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1512 -> 1420
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1352 -> 1260
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1120 -> 1028
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 996 -> 908
~ __ZN11accelerate210production23trsm_left_upper_fms_1x4IfLb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1164 -> 1032
~ __ZN11accelerate210production23trsm_left_upper_fms_1x4IfLb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1052 -> 872
~ __ZN11accelerate210production23trsm_left_upper_fms_1x2IfLb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 884 -> 688
~ __ZN11accelerate210production23trsm_left_upper_fms_1x2IfLb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 704 -> 552
~ __ZN11accelerate210production23trsm_left_upper_fms_1x4IfLb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1200 -> 1056
~ __ZN11accelerate210production23trsm_left_upper_fms_1x4IfLb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1088 -> 896
~ __ZN11accelerate210production23trsm_left_upper_fms_1x2IfLb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 916 -> 740
~ __ZN11accelerate210production23trsm_left_upper_fms_1x2IfLb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 756 -> 572
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb0ELb1ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1100 -> 996
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb0ELb1ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 972 -> 872
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb0ELb1ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 820 -> 708
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb0ELb1ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 692 -> 612
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1080 -> 980
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 956 -> 856
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 768 -> 668
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 684 -> 596
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb0ELb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1312 -> 1204
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb0ELb1ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1180 -> 1080
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb0ELb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1000 -> 900
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb0ELb1ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 888 -> 792
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1292 -> 1196
~ __ZN11accelerate210production23trsm_left_lower_fms_1x4IfLb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1160 -> 1064
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 952 -> 852
~ __ZN11accelerate210production23trsm_left_lower_fms_1x2IfLb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 872 -> 776
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb1ELb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1060 -> 988
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb1ELb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 976 -> 892
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb1ELb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 872 -> 788
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb1ELb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 816 -> 732
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb0ELb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1024 -> 952
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb0ELb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 924 -> 856
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb0ELb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 804 -> 728
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb0ELb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 752 -> 696
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_l : 1116 -> 1016
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_l : 1008 -> 900
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_l : 852 -> 748
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_l : 728 -> 612
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb1ELb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_l : 1156 -> 1048
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb1ELb1ELb1ELb0EEEvllPKT_S4_lS4_lPS2_l : 1044 -> 928
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb1ELb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_l : 912 -> 804
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb1ELb1ELb1ELb0EEEvllPKT_S4_lS4_lPS2_l : 768 -> 648
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb1ELb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1264 -> 1164
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb1ELb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1136 -> 1064
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb1ELb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1016 -> 972
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb1ELb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 900 -> 856
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb0ELb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1220 -> 1124
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb0ELb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1084 -> 1028
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb0ELb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 940 -> 908
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb0ELb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 860 -> 820
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb1ELb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1080 -> 1016
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb1ELb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 996 -> 908
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb1ELb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 896 -> 808
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb1ELb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 816 -> 732
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb0ELb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 1040 -> 988
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb0ELb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 944 -> 872
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb0ELb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 820 -> 748
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb0ELb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 752 -> 696
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_l : 1152 -> 1048
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_l : 1028 -> 924
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_l : 880 -> 772
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_l : 728 -> 612
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb1ELb1ELb0ELb1EEEvllPKT_S4_lS4_lPS2_l : 1192 -> 1072
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb1ELb1ELb0ELb0EEEvllPKT_S4_lS4_lPS2_l : 1068 -> 956
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb1ELb1ELb0ELb1EEEvllPKT_S4_lS4_lPS2_l : 952 -> 828
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb1ELb1ELb0ELb0EEEvllPKT_S4_lS4_lPS2_l : 768 -> 648
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb1ELb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1304 -> 1200
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb1ELb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1164 -> 1084
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb1ELb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1036 -> 992
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb1ELb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 900 -> 856
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb0ELb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1248 -> 1156
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb1ELb0ELb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1112 -> 1044
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb0ELb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 960 -> 928
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb1ELb0ELb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 860 -> 820
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb1ELb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 852 -> 792
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb1ELb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 780 -> 708
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb1ELb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 704 -> 636
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb1ELb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 676 -> 604
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb0ELb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 824 -> 740
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb0ELb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 748 -> 664
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb0ELb1ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 632 -> 576
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb0ELb1ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 632 -> 560
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_l : 928 -> 804
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_l : 848 -> 724
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_l : 736 -> 604
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_l : 632 -> 504
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb0ELb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_l : 976 -> 840
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb0ELb1ELb1ELb0EEEvllPKT_S4_lS4_lPS2_l : 892 -> 756
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb0ELb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_l : 816 -> 664
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb0ELb1ELb1ELb0EEEvllPKT_S4_lS4_lPS2_l : 664 -> 544
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb1ELb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1060 -> 960
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb1ELb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 956 -> 880
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb1ELb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 852 -> 800
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb1ELb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 772 -> 720
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb0ELb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1012 -> 916
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb0ELb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 904 -> 844
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb0ELb1ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 772 -> 740
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb0ELb1ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 716 -> 684
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb1ELb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 884 -> 808
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb1ELb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 796 -> 728
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb1ELb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 740 -> 648
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb1ELb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 676 -> 604
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb0ELb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 852 -> 780
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb0ELb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 768 -> 684
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb0ELb0ELb0ELb1ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 656 -> 592
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb0ELb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_lS5_l : 632 -> 560
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_l : 988 -> 836
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_l : 864 -> 736
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_l : 752 -> 636
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb0ELb0ELb0ELb0EEEvllPKT_S4_lS4_lPS2_l : 632 -> 504
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb0ELb1ELb0ELb1EEEvllPKT_S4_lS4_lPS2_l : 1012 -> 864
~ __ZN11accelerate210production24trsm_right_upper_fms_4x1IfLb0ELb1ELb0ELb0EEEvllPKT_S4_lS4_lPS2_l : 896 -> 772
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb0ELb1ELb0ELb1EEEvllPKT_S4_lS4_lPS2_l : 844 -> 692
~ __ZN11accelerate210production24trsm_right_upper_fms_2x1IfLb0ELb1ELb0ELb0EEEvllPKT_S4_lS4_lPS2_l : 664 -> 544
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb1ELb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1100 -> 996
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb1ELb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 968 -> 900
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb1ELb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 872 -> 824
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb1ELb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 772 -> 720
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb0ELb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1052 -> 952
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb0ELb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 932 -> 860
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb0ELb0ELb0ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 804 -> 764
~ __ZN11accelerate210production24trsm_right_lower_fms_2x1IfLb0ELb0ELb0ELb0ELb0ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 716 -> 684
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb0ELb1ELb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1260 -> 1160
~ __ZN11accelerate210production24trsm_right_lower_fms_4x1IfLb0ELb0ELb0ELb1ELb1ELb1EEEvllPKT_S4_lS4_lPS2_lS5_l : 1304 -> 1188
~ __ZN10accelerate10production29accelerate_right_trsm_generalIfEEvbbbllPKT_lPS2_l : 3368 -> 3400
~ __ZN6lapack9reference6ieeeckERKiRKfS4_ : 196 -> 200
~ _sgebpScale_1M1N : 188 -> 184
~ _sgebp_1M1N : 176 -> 172
~ __ZN10accelerate10production26accelerate_lu_trsm_generalIfEEvbbllPKT_lPS2_lS5_l : 1568 -> 1576
~ _sgetrf_default_internal : 1364 -> 1320
~ __ZN11accelerate210production13syrk_internalIfLb0EEEvbllT_PKS2_lS2_PS2_l : 672 -> 644
~ __ZN11accelerate210production17syrk_upper_fma_b0IfLb1ELb1EEEvllPKT_lPS2_l : 252 -> 256
~ __ZN11accelerate210production17syrk_upper_fma_b0IfLb1ELb0EEEvllPKT_lPS2_l : 84 -> 88
~ __ZN11accelerate210production17syrk_lower_fma_b0IfLb1ELb1EEEvllPKT_lPS2_l : 244 -> 248
~ __Z28accelerate_transpose_alignedmmPKfmPfm : 420 -> 428
~ _accelerate_transpose_aligned_2xN : 532 -> 504
~ _strsm_noPack_RUNU : 1216 -> 1220
~ _strsm_noPack_RUNN : 1388 -> 1392
~ _accelerate_sgemm_worker : 4068 -> 4024
~ _accelerate_sgemm_worker_2x2 : 1876 -> 1860
~ _accelerate_sgemm_worker_2x1 : 540 -> 512
~ _accelerate_sgemm_worker_1x2 : 572 -> 544
~ _accelerate_sgemm_worker_1x1 : 304 -> 284
~ _accelerate_ssyrk_worker : 2084 -> 2044
~ _strsm_noPack_LUNU : 1284 -> 1244
~ _strsm_noPack_LUNN : 1444 -> 1404
~ _sgePack_A_NoTran_Unaligned : 280 -> 232
~ _strsm_noPack_LLTU : 1496 -> 1460
~ _strsm_noPack_LLTN : 1668 -> 1624
~ __ZN11accelerate210production11gemm_fma_b1IfLb1ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 220 -> 228
~ __ZN11accelerate210production11gemm_fma_b1IfLb1ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 192 -> 196
~ __ZN11accelerate210production11gemm_fma_b1IfLb1ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 196 -> 200
~ __ZN11accelerate210production11gemm_fma_b1IfLb1ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 288 -> 292
~ __ZN11accelerate210production11gemm_fma_b1IfLb1ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 200 -> 204
~ __ZN11accelerate210production11gemm_fma_b1IfLb1ELb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 272 -> 260
~ __ZN11accelerate210production11gemm_fma_b1IfLb1ELb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 164 -> 152
~ __ZN11accelerate210production11gemm_fma_b1IfLb0ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 300 -> 292
~ __ZN11accelerate210production11gemm_fma_b1IfLb0ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 268 -> 256
~ __ZN11accelerate210production11gemm_fma_b1IfLb0ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 216 -> 208
~ __ZN11accelerate210production11gemm_fma_b1IfLb0ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 356 -> 344
~ __ZN11accelerate210production15gemm_fma_1xN_b1IfLb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 756 -> 764
~ __ZN11accelerate210production15gemm_fma_1xN_b1IfLb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 672 -> 680
~ __ZN11accelerate210production15gemm_fma_1xN_b1IfLb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 836 -> 840
~ __ZN11accelerate210production15gemm_fma_1xN_b1IfLb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 732 -> 736
~ __ZN11accelerate210production15gemm_fma_1xN_b1IfLb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 820 -> 812
~ __ZN11accelerate210production15gemm_fma_1xN_b1IfLb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 732 -> 724
~ __ZN11accelerate210production15gemm_fma_1xN_b1IfLb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 888 -> 876
~ __ZN11accelerate210production15gemm_fma_1xN_b1IfLb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 804 -> 792
~ __ZN11accelerate210production15gemm_fma_Mx1_b1IfLb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 224 -> 232
~ __ZN11accelerate210production15gemm_fma_Mx1_b1IfLb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 200 -> 208
~ __ZN11accelerate210production15gemm_fma_Mx1_b1IfLb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 276 -> 280
~ __ZN11accelerate210production15gemm_fma_Mx1_b1IfLb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 248 -> 252
~ __ZN11accelerate210production15gemm_fma_Mx1_b1IfLb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 316 -> 308
~ __ZN11accelerate210production15gemm_fma_Mx1_b1IfLb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 272 -> 264
~ __ZN11accelerate210production15gemm_fma_Mx1_b1IfLb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 356 -> 344
~ __ZN11accelerate210production15gemm_fma_Mx1_b1IfLb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 312 -> 300
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb1ELb1ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 196 -> 192
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb1ELb1ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 276 -> 272
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb1ELb1ELb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 236 -> 228
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb0ELb1ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 380 -> 376
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb0ELb1ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 212 -> 208
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb0ELb1ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 408 -> 388
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb0ELb1ELb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 264 -> 244
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb1ELb1ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 392 -> 376
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb1ELb1ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 328 -> 308
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb1ELb1ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 304 -> 288
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb0ELb1ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 496 -> 476
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb1ELb0ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 268 -> 264
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb0ELb0ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 420 -> 416
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb0ELb0ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 284 -> 280
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb1ELb0ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 432 -> 416
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb1ELb0ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 400 -> 380
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb0ELb0ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 536 -> 516
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb1ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 1004 -> 1000
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb1ELb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 868 -> 864
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb0ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 952 -> 936
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb0ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 848 -> 832
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb0ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 1088 -> 1068
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb0ELb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 972 -> 952
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb1ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 396 -> 392
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb1ELb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 356 -> 352
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb0ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 472 -> 456
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb0ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 400 -> 384
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb0ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 544 -> 524
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb0ELb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 472 -> 452
~ __ZN11accelerate210production11gemm_fms_b1IfLb1ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 220 -> 228
~ __ZN11accelerate210production11gemm_fms_b1IfLb1ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 192 -> 196
~ __ZN11accelerate210production11gemm_fms_b1IfLb1ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 196 -> 200
~ __ZN11accelerate210production11gemm_fms_b1IfLb1ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 288 -> 292
~ __ZN11accelerate210production11gemm_fms_b1IfLb1ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 200 -> 204
~ __ZN11accelerate210production11gemm_fms_b1IfLb1ELb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 272 -> 260
~ __ZN11accelerate210production11gemm_fms_b1IfLb1ELb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 164 -> 152
~ __ZN11accelerate210production11gemm_fms_b1IfLb0ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 300 -> 292
~ __ZN11accelerate210production11gemm_fms_b1IfLb0ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 268 -> 256
~ __ZN11accelerate210production11gemm_fms_b1IfLb0ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 216 -> 208
~ __ZN11accelerate210production11gemm_fms_b1IfLb0ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 356 -> 344
~ __ZN11accelerate210production15gemm_fms_1xN_b1IfLb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 756 -> 764
~ __ZN11accelerate210production15gemm_fms_1xN_b1IfLb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 672 -> 680
~ __ZN11accelerate210production15gemm_fms_1xN_b1IfLb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 836 -> 840
~ __ZN11accelerate210production15gemm_fms_1xN_b1IfLb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 732 -> 736
~ __ZN11accelerate210production15gemm_fms_1xN_b1IfLb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 820 -> 812
~ __ZN11accelerate210production15gemm_fms_1xN_b1IfLb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 732 -> 724
~ __ZN11accelerate210production15gemm_fms_1xN_b1IfLb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 888 -> 876
~ __ZN11accelerate210production15gemm_fms_1xN_b1IfLb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 804 -> 792
~ __ZN11accelerate210production15gemm_fms_Mx1_b1IfLb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 224 -> 232
~ __ZN11accelerate210production15gemm_fms_Mx1_b1IfLb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 200 -> 208
~ __ZN11accelerate210production15gemm_fms_Mx1_b1IfLb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 276 -> 280
~ __ZN11accelerate210production15gemm_fms_Mx1_b1IfLb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 248 -> 252
~ __ZN11accelerate210production15gemm_fms_Mx1_b1IfLb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 316 -> 308
~ __ZN11accelerate210production15gemm_fms_Mx1_b1IfLb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 272 -> 264
~ __ZN11accelerate210production15gemm_fms_Mx1_b1IfLb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 356 -> 344
~ __ZN11accelerate210production15gemm_fms_Mx1_b1IfLb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 312 -> 300
~ __ZN11accelerate210production11gemm_fms_b0IfLb1ELb1ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 196 -> 192
~ __ZN11accelerate210production11gemm_fms_b0IfLb1ELb1ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 276 -> 272
~ __ZN11accelerate210production11gemm_fms_b0IfLb1ELb1ELb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 236 -> 228
~ __ZN11accelerate210production11gemm_fms_b0IfLb1ELb0ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 380 -> 376
~ __ZN11accelerate210production11gemm_fms_b0IfLb1ELb0ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 212 -> 208
~ __ZN11accelerate210production11gemm_fms_b0IfLb1ELb0ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 408 -> 388
~ __ZN11accelerate210production11gemm_fms_b0IfLb1ELb0ELb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 264 -> 244
~ __ZN11accelerate210production11gemm_fms_b0IfLb0ELb1ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 392 -> 376
~ __ZN11accelerate210production11gemm_fms_b0IfLb0ELb1ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 328 -> 308
~ __ZN11accelerate210production11gemm_fms_b0IfLb0ELb1ELb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 304 -> 288
~ __ZN11accelerate210production11gemm_fms_b0IfLb0ELb0ELb1ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 496 -> 476
~ __ZN11accelerate210production11gemm_fms_b0IfLb1ELb1ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 268 -> 264
~ __ZN11accelerate210production11gemm_fms_b0IfLb1ELb0ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 420 -> 416
~ __ZN11accelerate210production11gemm_fms_b0IfLb1ELb0ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 284 -> 280
~ __ZN11accelerate210production11gemm_fms_b0IfLb0ELb1ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 432 -> 416
~ __ZN11accelerate210production11gemm_fms_b0IfLb0ELb1ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 400 -> 380
~ __ZN11accelerate210production11gemm_fms_b0IfLb0ELb0ELb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 536 -> 516
~ __ZN11accelerate210production15gemm_fms_1xN_b0IfLb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 1004 -> 1000
~ __ZN11accelerate210production15gemm_fms_1xN_b0IfLb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 868 -> 864
~ __ZN11accelerate210production15gemm_fms_1xN_b0IfLb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 952 -> 936
~ __ZN11accelerate210production15gemm_fms_1xN_b0IfLb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 848 -> 832
~ __ZN11accelerate210production15gemm_fms_1xN_b0IfLb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 1088 -> 1068
~ __ZN11accelerate210production15gemm_fms_1xN_b0IfLb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 972 -> 952
~ __ZN11accelerate210production15gemm_fms_Mx1_b0IfLb1ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 396 -> 392
~ __ZN11accelerate210production15gemm_fms_Mx1_b0IfLb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 356 -> 352
~ __ZN11accelerate210production15gemm_fms_Mx1_b0IfLb0ELb1ELb1EEEvlllPKT_lS4_lPS2_l : 472 -> 456
~ __ZN11accelerate210production15gemm_fms_Mx1_b0IfLb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 400 -> 384
~ __ZN11accelerate210production15gemm_fms_Mx1_b0IfLb0ELb0ELb1EEEvlllPKT_lS4_lPS2_l : 544 -> 524
~ __ZN11accelerate210production15gemm_fms_Mx1_b0IfLb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 472 -> 452
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb1ELb1ELb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 180 -> 176
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb1ELb1ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 188 -> 184
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb1ELb1ELb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 220 -> 212
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb0ELb1ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 292 -> 288
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb0ELb1ELb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 196 -> 192
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb0ELb1ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 320 -> 300
~ __ZN11accelerate210production11gemm_fma_b0IfLb1ELb0ELb1ELb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 248 -> 228
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb1ELb1ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 304 -> 288
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb1ELb1ELb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 312 -> 292
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb1ELb1ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 216 -> 200
~ __ZN11accelerate210production11gemm_fma_b0IfLb0ELb0ELb1ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 408 -> 388
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb1ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 364 -> 360
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb1ELb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 300 -> 296
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb0ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 312 -> 296
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb0ELb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 280 -> 264
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb0ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 448 -> 436
~ __ZN11accelerate210production15gemm_fma_1xN_b0IfLb0ELb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 384 -> 364
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb1ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 276 -> 272
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb1ELb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 252 -> 248
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb0ELb1ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 352 -> 336
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb0ELb1ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 296 -> 280
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb0ELb0ELb1ELb0EEEvlllPKT_lS4_lPS2_l : 424 -> 404
~ __ZN11accelerate210production15gemm_fma_Mx1_b0IfLb0ELb0ELb0ELb0EEEvlllPKT_lS4_lPS2_l : 368 -> 348
~ _sgemvT_packed_base : 7016 -> 7268
~ __ZN11accelerate210production24repack_unaligned_alignedIfLb0EEEvllPKT_lPS2_l : 604 -> 644
~ __ZN11accelerate210production25accelerate2_no_trans_packIfEEvllPKT_lPS2_l : 316 -> 296
~ __ZN11accelerate210production22repack_aligned_alignedIfLb1EEEvllPKT_lPS2_l : 396 -> 440
~ __ZN11accelerate210production22repack_aligned_alignedIfLb0EEEvllPKT_lPS2_l : 272 -> 328
~ __ZN11accelerate210production24repack_unaligned_alignedIfLb1EEEvllPKT_lPS2_l : 744 -> 756

```
