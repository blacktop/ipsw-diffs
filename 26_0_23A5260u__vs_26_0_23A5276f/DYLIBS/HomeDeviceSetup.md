## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-345.0.1.0.0
-  __TEXT.__text: 0x6eb88
+345.0.6.0.0
+  __TEXT.__text: 0x6ebc4
   __TEXT.__auth_stubs: 0xfd0
-  __TEXT.__objc_methlist: 0x30c4
+  __TEXT.__objc_methlist: 0x30cc
   __TEXT.__const: 0x432
-  __TEXT.__cstring: 0x1a264
+  __TEXT.__cstring: 0x1a1e4
   __TEXT.__oslogstring: 0x5ad
   __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x16e8
+  __TEXT.__unwind_info: 0x16d8
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0x2bc
-  __TEXT.__objc_methname: 0xc9d3
+  __TEXT.__objc_methname: 0xca14
   __TEXT.__objc_methtype: 0x113e
-  __TEXT.__objc_stubs: 0x7b60
+  __TEXT.__objc_stubs: 0x7b80
   __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x179c
+  __DATA_CONST.__const: 0x1754
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ad0
+  __DATA_CONST.__objc_selrefs: 0x2ad8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x240
   __AUTH_CONST.__auth_got: 0x7f8
   __AUTH_CONST.__const: 0xad0
   __AUTH_CONST.__cfstring: 0x52a0
-  __AUTH_CONST.__objc_const: 0x7170
+  __AUTH_CONST.__objc_const: 0x71d0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH.__objc_data: 0x688
   __AUTH.__data: 0x2f8
-  __DATA.__objc_ivar: 0xa18
+  __DATA.__objc_ivar: 0xa24
   __DATA.__data: 0xa40
   __DATA.__common: 0x40
   __DATA.__bss: 0x740

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CC148A0D-F37D-31C9-8ABF-1ECE2EF93029
+  UUID: 26A12360-9DD3-35F8-A9A8-1C8B76908AED
   Functions: 2831
-  Symbols:   8316
-  CStrings:  6042
+  Symbols:   8311
+  CStrings:  6044
 
Symbols:
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.10
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.11
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.12
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.13
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.14
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.15
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.16
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.4
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.5
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.6
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.7
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.8
+ -[HDSSetupSession _runHomeKitPrimarySSIDFetch].cold.9
+ -[HDSSetupSession showWiFiPicker]
+ GCC_except_table308
+ GCC_except_table366
+ GCC_except_table417
+ _OBJC_IVAR_$_HDSSetupSession._hasAlreadySkipped
+ _OBJC_IVAR_$_HDSSetupSession._homePodScanContainsPrimary
+ _OBJC_IVAR_$_HDSSetupSession._phoneMatchesPrimary
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1660
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1660.cold.1
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.343
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.345
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.345.cold.1
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.657
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.657.cold.1
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.679
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_3.cold.1
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_3.cold.2
+ ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_3.cold.3
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.506
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.506.cold.1
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.506.cold.2
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.506.cold.3
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1807
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1808
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1808.cold.1
+ ___block_literal_global.1012
+ ___block_literal_global.1340
+ ___block_literal_global.1344
+ ___block_literal_global.1356
+ ___block_literal_global.1360
+ ___block_literal_global.1365
+ ___block_literal_global.1369
+ ___block_literal_global.1381
+ ___block_literal_global.1387
+ ___block_literal_global.1394
+ ___block_literal_global.1398
+ ___block_literal_global.1402
+ ___block_literal_global.1412
+ ___block_literal_global.1416
+ ___block_literal_global.1662
+ ___block_literal_global.3550
+ ___block_literal_global.3558
+ ___block_literal_global.3561
+ ___block_literal_global.3564
+ ___block_literal_global.3572
+ ___block_literal_global.3576
+ ___block_literal_global.3590
+ ___block_literal_global.3594
+ ___block_literal_global.3607
+ ___block_literal_global.3613
+ ___block_literal_global.3617
+ ___block_literal_global.3621
+ ___block_literal_global.3639
+ ___block_literal_global.3655
+ ___block_literal_global.3661
+ ___block_literal_global.3665
+ ___block_literal_global.3670
+ ___block_literal_global.3674
+ ___block_literal_global.3683
+ ___block_literal_global.3700
+ ___block_literal_global.3706
+ ___block_literal_global.3710
+ ___block_literal_global.3714
+ ___block_literal_global.3815
+ ___block_literal_global.662
+ ___block_literal_global.703
+ ___block_literal_global.775
+ ___block_literal_global.975
+ _objc_msgSend$primaryResidentNetworkInfo
+ _objc_msgSend$showWiFiPicker
- GCC_except_table310
- GCC_except_table368
- GCC_except_table419
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1657
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1657.cold.1
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.340
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.342
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.342.cold.1
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.654
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.654.cold.1
- ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.676
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.10
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.11
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.12
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.2
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.3
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.4
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.5
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.6
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.7
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.8
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_2.cold.9
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_4
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_4.cold.1
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_5
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_5.cold.1
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_5.cold.2
- ___46-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_5.cold.3
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.503
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.503.cold.1
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.503.cold.2
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.503.cold.3
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1804
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1805
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1805.cold.1
- ___block_descriptor_40_e8_32s_e39_v24?0"HMHomeNetworkInfo"8"NSError"16ls32l8
- ___block_literal_global.1009
- ___block_literal_global.1337
- ___block_literal_global.1341
- ___block_literal_global.1353
- ___block_literal_global.1357
- ___block_literal_global.1362
- ___block_literal_global.1366
- ___block_literal_global.1378
- ___block_literal_global.1384
- ___block_literal_global.1391
- ___block_literal_global.1395
- ___block_literal_global.1399
- ___block_literal_global.1409
- ___block_literal_global.1413
- ___block_literal_global.1659
- ___block_literal_global.3543
- ___block_literal_global.3547
- ___block_literal_global.3551
- ___block_literal_global.3557
- ___block_literal_global.3565
- ___block_literal_global.3569
- ___block_literal_global.3583
- ___block_literal_global.3587
- ___block_literal_global.3600
- ___block_literal_global.3603
- ___block_literal_global.3606
- ___block_literal_global.3614
- ___block_literal_global.3632
- ___block_literal_global.3644
- ___block_literal_global.3648
- ___block_literal_global.3654
- ___block_literal_global.3663
- ___block_literal_global.3667
- ___block_literal_global.3672
- ___block_literal_global.3676
- ___block_literal_global.3682
- ___block_literal_global.3699
- ___block_literal_global.3707
- ___block_literal_global.3808
- ___block_literal_global.659
- ___block_literal_global.700
- ___block_literal_global.772
- ___block_literal_global.972
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_HomeDeviceSetup
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HomeDeviceSetup
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HomeDeviceSetup
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HomeDeviceSetup
- _objc_msgSend$getPrimaryResidentNetworkInfoWithCompletion:
CStrings:
+ "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_3"
+ "HomePod scan contains Primary Resident network\n"
+ "Primary Network returned nil\n"
+ "_hasAlreadySkipped"
+ "_homePodScanContainsPrimary"
+ "_phoneMatchesPrimary"
+ "primaryResidentNetworkInfo"
+ "showWiFiPicker"
- "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_4"
- "-[HDSSetupSession _runHomeKitPrimarySSIDFetch]_block_invoke_5"
- "HomeKitPrimarySSIDFetchV2 Cached skipping since network is null\n"
- "Primary Network Cached fetch failed %@\n"
- "getPrimaryResidentNetworkInfoWithCompletion:"
- "v24@?0@\"HMHomeNetworkInfo\"8@\"NSError\"16"

```
