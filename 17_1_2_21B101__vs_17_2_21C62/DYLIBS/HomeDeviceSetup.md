## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-217.11.1.0.0
-  __TEXT.__text: 0x4bb88
+217.20.8.0.0
+  __TEXT.__text: 0x4c34c
   __TEXT.__auth_stubs: 0xaa0
   __TEXT.__objc_methlist: 0x1c70
   __TEXT.__const: 0x258
-  __TEXT.__cstring: 0x1418b
+  __TEXT.__cstring: 0x143a5
   __TEXT.__gcc_except_tab: 0xf8
   __TEXT.__oslogstring: 0x3bc
   __TEXT.__unwind_info: 0xb50
   __TEXT.__objc_classname: 0x21e
-  __TEXT.__objc_methname: 0x9826
+  __TEXT.__objc_methname: 0x9876
   __TEXT.__objc_methtype: 0xe52
-  __TEXT.__objc_stubs: 0x6320
+  __TEXT.__objc_stubs: 0x6380
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x11b8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5888
-  __DATA_CONST.__objc_selrefs: 0x1ea8
+  __DATA_CONST.__objc_const: 0x58a8
+  __DATA_CONST.__objc_selrefs: 0x1ec0
   __DATA_CONST.__objc_arraydata: 0x1c8
-  __AUTH_CONST.__cfstring: 0x3900
+  __AUTH_CONST.__cfstring: 0x3980
   __AUTH_CONST.__objc_const: 0x540
   __AUTH_CONST.__const: 0x620
   __AUTH_CONST.__objc_arrayobj: 0x18

   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x220
   __DATA.__objc_superrefs: 0x48
-  __DATA.__objc_ivar: 0x788
+  __DATA.__objc_ivar: 0x78c
   __DATA.__data: 0x820
   __DATA.__common: 0x10
   __DATA.__bss: 0x4d8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   Functions: 1116
-  Symbols:   4291
-  CStrings:  4161
+  Symbols:   4295
+  CStrings:  4183
 
Symbols:
+ _OBJC_IVAR_$_HDSSetupSession._homePod6GCapable
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke.1336
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.537
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1463
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1464
+ ___block_literal_global.1338
+ ___block_literal_global.2754
+ ___block_literal_global.2758
+ ___block_literal_global.2762
+ ___block_literal_global.2766
+ ___block_literal_global.2770
+ ___block_literal_global.2774
+ ___block_literal_global.2790
+ ___block_literal_global.2803
+ ___block_literal_global.2807
+ ___block_literal_global.2811
+ ___block_literal_global.2816
+ ___block_literal_global.2845
+ ___block_literal_global.2849
+ ___block_literal_global.2855
+ ___block_literal_global.2860
+ ___block_literal_global.2864
+ ___block_literal_global.2869
+ ___block_literal_global.2882
+ ___block_literal_global.2886
+ ___block_literal_global.2976
+ ___block_literal_global.542
+ __unnamed_array_storage.1080
+ __unnamed_array_storage.1081
+ __unnamed_array_storage.1103
+ __unnamed_array_storage.1104
+ __unnamed_array_storage.1114
+ __unnamed_array_storage.1115
+ __unnamed_array_storage.1168
+ __unnamed_array_storage.1169
+ __unnamed_array_storage.1838
+ __unnamed_array_storage.1839
+ __unnamed_array_storage.557
+ __unnamed_array_storage.791
+ __unnamed_array_storage.792
+ __unnamed_array_storage.813
+ __unnamed_array_storage.814
+ __unnamed_array_storage.953
+ __unnamed_array_storage.954
+ _objc_msgSend$reachabilityError
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$setShouldSetupHomePod:
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke.1317
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.536
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1438
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1439
- ___block_literal_global.1319
- ___block_literal_global.2729
- ___block_literal_global.2733
- ___block_literal_global.2737
- ___block_literal_global.2741
- ___block_literal_global.2745
- ___block_literal_global.2749
- ___block_literal_global.2765
- ___block_literal_global.2778
- ___block_literal_global.2782
- ___block_literal_global.2786
- ___block_literal_global.2791
- ___block_literal_global.2795
- ___block_literal_global.2824
- ___block_literal_global.2830
- ___block_literal_global.2835
- ___block_literal_global.2839
- ___block_literal_global.2844
- ___block_literal_global.2857
- ___block_literal_global.2861
- ___block_literal_global.2951
- ___block_literal_global.541
- __unnamed_array_storage.1061
- __unnamed_array_storage.1062
- __unnamed_array_storage.1084
- __unnamed_array_storage.1085
- __unnamed_array_storage.1095
- __unnamed_array_storage.1096
- __unnamed_array_storage.1149
- __unnamed_array_storage.1150
- __unnamed_array_storage.1814
- __unnamed_array_storage.1815
- __unnamed_array_storage.555
- __unnamed_array_storage.776
- __unnamed_array_storage.777
- __unnamed_array_storage.798
- __unnamed_array_storage.799
- __unnamed_array_storage.934
- __unnamed_array_storage.935
CStrings:
+ "### Current Wifi info failed to fetch\n"
+ "### StandAlone not in WIfi Info %#m\n"
+ "Background activation hasn't succeeded yet (%d)\n"
+ "CaptiveNetwork"
+ "CaptiveNetwork failed"
+ "CaptiveNetwork failed, root cause error: %@"
+ "Device current wifi info: %@\n"
+ "HomePod 6g capable: %s | %#m\n"
+ "HomePod Not 6G Capable"
+ "HomePod can be added to Phone's network\n"
+ "Is HomePod 6G capable: %s\n"
+ "Phone on 6G network: %s\n"
+ "Preflight WiFi Info %@\n"
+ "SFSession UUID: %@\n"
+ "Setup Ending due to error, Session identifier %@\n"
+ "Setup Finished, Session identifier %@\n"
+ "_homePod6GCapable"
+ "hp_wifi6_capable"
+ "password"
+ "reachabilityError"
+ "removeObjectForKey:"
+ "setShouldSetupHomePod:"
+ "standalone6G"
- "psgHelper done\n"

```
