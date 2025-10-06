## LiveFS

> `/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS`

```diff

-208.42.1.0.0
-  __TEXT.__text: 0x1cd08
+208.60.13.0.2
+  __TEXT.__text: 0x1ce40
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_methlist: 0x16a0
+  __TEXT.__objc_methlist: 0x16a8
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0xfc7
+  __TEXT.__cstring: 0x1033
   __TEXT.__oslogstring: 0x1425
   __TEXT.__gcc_except_tab: 0xb74
-  __TEXT.__unwind_info: 0x9c8
+  __TEXT.__unwind_info: 0x9cc
   __TEXT.__objc_classname: 0x324
   __TEXT.__objc_methname: 0x409a
-  __TEXT.__objc_methtype: 0x26a6
+  __TEXT.__objc_methtype: 0x283c
   __TEXT.__objc_stubs: 0x2860
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__const: 0xdf8

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9859A17B-340A-3E4F-B378-B83B85ECCA5E
-  Functions: 779
-  Symbols:   2645
-  CStrings:  1333
+  UUID: 44849E52-18C5-34E1-A355-EF4C96135D80
+  Functions: 780
+  Symbols:   2647
+  CStrings:  1337
 
Symbols:
+ -[LiveFSMountClient dealloc]
+ GCC_except_table22
+ GCC_except_table31
+ GCC_except_table34
+ ___31-[LiveFSAppleDouble createFile]_block_invoke.74
+ ___31-[LiveFSAppleDouble createFile]_block_invoke_2.76
+ ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.72
+ ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.72.cold.1
+ ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.74
+ ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.74.cold.1
+ ___75-[LiveFSMountClient unmountVolumeNamed:providerName:domainError:how:reply:]_block_invoke.75
+ ___block_descriptor_32_e19_v20?0i8"NSData"12l
+ ___block_descriptor_40_e8_32r_e22_v28?0i8Q12"NSData"20lr32l8
+ ___block_descriptor_48_e8_32bs40r_e22_v28?0i8Q12"NSData"20lr40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e19_v20?0i8"NSData"12ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e19_v20?0i8"NSData"12ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e22_v28?0i8Q12"NSData"20lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e47_v52?0i8"NSData"12Q20"NSData"28Q36"NSData"44lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e57_v52?0i8"NSData"12Q20"NSString"28"NSData"36"NSData"44lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e65_v64?0i8"NSData"12"NSString"20Q28"NSString"36Q44i52"NSData"56lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e85_v92?0i8"NSData"12Q20"NSData"28Q36Q44"NSString"52B60Q64"NSString"72B80"NSData"84lr40l8s32l8
+ ___block_descriptor_52_e8_32s40r_e22_v28?0i8Q12"NSData"20lr40l8s32l8
+ ___block_descriptor_56_e8_32s40r48r_e22_v28?0i8Q12"NSData"20lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40r48w_e65_v64?0i8"NSData"12"NSString"20Q28"NSString"36Q44i52"NSData"56lw48l8r40l8s32l8
+ ___block_descriptor_56_e8_32s40r_e22_v28?0i8Q12"NSData"20lr40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e65_v64?0i8"NSData"12"NSString"20Q28"NSString"36Q44i52"NSData"56ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e52_v56?0i8"NSData"12Q20Q28"NSString"36B44"NSData"48ls56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e57_v52?0i8"NSData"12Q20"NSString"28"NSData"36"NSData"44ls56l8s32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e47_v52?0i8"NSData"12Q20"NSData"28Q36"NSData"44ls64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs_e85_v92?0i8"NSData"12Q20"NSData"28Q36Q44"NSString"52B60Q64"NSString"72B80"NSData"84ls72l8s32l8s40l8s48l8s56l8s64l8
- GCC_except_table21
- GCC_except_table27
- GCC_except_table30
- ___31-[LiveFSAppleDouble createFile]_block_invoke.75
- ___31-[LiveFSAppleDouble createFile]_block_invoke_2.77
- ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.70
- ___39-[LiveFSMountClient unmountVolume:how:]_block_invoke.70.cold.1
- ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.72
- ___43-[LiveFSMountClient unmountVolumeByID:how:]_block_invoke.72.cold.1
- ___75-[LiveFSMountClient unmountVolumeNamed:providerName:domainError:how:reply:]_block_invoke.73
- ___block_descriptor_32_e8_v12?0i8l
- ___block_descriptor_40_e8_32r_e11_v20?0i8Q12lr32l8
- ___block_descriptor_40_e8_32s_e8_v12?0i8ls32l8
- ___block_descriptor_48_e8_32bs40r_e11_v20?0i8Q12lr40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e8_v12?0i8ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e11_v20?0i8Q12lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e36_v44?0i8"NSData"12Q20"NSData"28Q36lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e46_v44?0i8"NSData"12Q20"NSString"28"NSData"36lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e54_v56?0i8"NSData"12"NSString"20Q28"NSString"36Q44i52lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e74_v84?0i8"NSData"12Q20"NSData"28Q36Q44"NSString"52B60Q64"NSString"72B80lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e8_v12?0i8ls32l8r40l8
- ___block_descriptor_52_e8_32s40r_e11_v20?0i8Q12lr40l8s32l8
- ___block_descriptor_56_e8_32s40r48r_e11_v20?0i8Q12lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40r48w_e54_v56?0i8"NSData"12"NSString"20Q28"NSString"36Q44i52lw48l8r40l8s32l8
- ___block_descriptor_56_e8_32s40r_e11_v20?0i8Q12lr40l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e54_v56?0i8"NSData"12"NSString"20Q28"NSString"36Q44i52ls48l8s32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e46_v44?0i8"NSData"12Q20"NSString"28"NSData"36ls56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e36_v44?0i8"NSData"12Q20"NSData"28Q36ls64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs_e74_v84?0i8"NSData"12Q20"NSData"28Q36Q44"NSString"52B60Q64"NSString"72B80ls72l8s32l8s40l8s48l8s56l8s64l8
CStrings:
+ "v28@?0i8Q12@\"NSData\"20"
+ "v48@0:8@\"NSString\"16@\"NSData\"24Q32@?<v@?i@\"NSData\"@\"NSData\">40"
+ "v48@0:8@\"NSString\"16@\"NSData\"24Q32@?<v@?i@\"NSData\"@\"NSString\"Q@\"NSString\"Qi@\"NSData\">40"
+ "v48@0:8@\"NSString\"16Q24Q32@?<v@?i@\"NSData\">40"
+ "v52@?0i8@\"NSData\"12Q20@\"NSData\"28Q36@\"NSData\"44"
+ "v52@?0i8@\"NSData\"12Q20@\"NSString\"28@\"NSData\"36@\"NSData\"44"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSString\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32Q40@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">48"
+ "v56@0:8@\"NSString\"16Q24@\"LiveFSSharedMutableBuffer\"32Q40@?<v@?iQ@\"NSData\">48"
+ "v56@0:8@\"NSString\"16Q24@\"NSData\"32Q40@?<v@?iQ@\"NSData\">48"
+ "v56@?0i8@\"NSData\"12Q20Q28@\"NSString\"36B44@\"NSData\"48"
+ "v60@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32i40Q44@?<v@?i@\"NSData\"@\"NSData\">52"
+ "v60@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32i40Q44@?<v@?i@\"NSData\"QQ@\"NSString\"B@\"NSData\">52"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40Q48@?<v@?i@\"NSData\"Q@\"NSString\"@\"NSData\"@\"NSData\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40Q48@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">56"
+ "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32Q40Q48@?<v@?i@\"NSData\"Q@\"NSData\"Q@\"NSData\">56"
+ "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\"I@\"NSData\">56"
+ "v64@?0i8@\"NSData\"12@\"NSString\"20Q28@\"NSString\"36Q44i52@\"NSData\"56"
+ "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40I48Q52@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSData\">60"
+ "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40I48Q52@?<v@?i@\"NSData\"@\"NSData\"@\"NSData\">60"
+ "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40I48Q52@?<v@?i@\"NSData\"Q@\"NSData\"QQ@\"NSString\"BQ@\"NSString\"B@\"NSData\">60"
+ "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40Q48Q56@?<v@?i@\"NSData\"Q@\"NSString\"@\"NSData\"@\"NSData\">64"
+ "v76@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40I48Q52Q60@?<v@?i@\"NSData\"Q@\"NSString\"@\"NSData\"@\"NSData\">68"
+ "v92@?0i8@\"NSData\"12Q20@\"NSData\"28Q36Q44@\"NSString\"52B60Q64@\"NSString\"72B80@\"NSData\"84"
- "v20@?0i8Q12"
- "v44@?0i8@\"NSData\"12Q20@\"NSData\"28Q36"
- "v44@?0i8@\"NSData\"12Q20@\"NSString\"28@\"NSData\"36"
- "v48@0:8@\"NSString\"16@\"NSData\"24Q32@?<v@?i@\"NSData\">40"
- "v48@0:8@\"NSString\"16@\"NSData\"24Q32@?<v@?i@\"NSData\"@\"NSString\"Q@\"NSString\"Qi>40"
- "v48@0:8@\"NSString\"16Q24Q32@?<v@?i>40"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40@?<v@?i@\"NSData\">48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\">48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\"@\"NSString\">48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32Q40@?<v@?i@\"NSData\"@\"NSData\">48"
- "v56@0:8@\"NSString\"16Q24@\"NSData\"32Q40@?<v@?iQ>48"
- "v56@?0i8@\"NSData\"12@\"NSString\"20Q28@\"NSString\"36Q44i52"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32Q40Q48@?<v@?i@\"NSData\"Q@\"NSString\"@\"NSData\">56"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40Q48@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\">56"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32Q40Q48@?<v@?i@\"NSData\"Q@\"NSData\"Q>56"
- "v64@0:8@\"NSString\"16{_NSRange=QQ}24i40I44Q48@?<v@?i@\"NSData\"I>56"
- "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40I48Q52@?<v@?i@\"NSData\"@\"NSString\"@\"NSData\">60"
- "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40I48Q52@?<v@?i@\"NSData\"@\"NSData\">60"
- "v68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40I48Q52@?<v@?i@\"NSData\"Q@\"NSData\"QQ@\"NSString\"BQ@\"NSString\"B>60"
- "v72@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40Q48Q56@?<v@?i@\"NSData\"Q@\"NSString\"@\"NSData\">64"
- "v76@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40I48Q52Q60@?<v@?i@\"NSData\"Q@\"NSString\"@\"NSData\">68"
- "v84@?0i8@\"NSData\"12Q20@\"NSData\"28Q36Q44@\"NSString\"52B60Q64@\"NSString\"72B80"

```
