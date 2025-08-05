## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-345.0.9.0.0
-  __TEXT.__text: 0x6f1ec
-  __TEXT.__auth_stubs: 0xfe0
+345.0.15.0.0
+  __TEXT.__text: 0x6f75c
+  __TEXT.__auth_stubs: 0xff0
   __TEXT.__objc_methlist: 0x30e4
   __TEXT.__const: 0x438
-  __TEXT.__cstring: 0x1a334
+  __TEXT.__cstring: 0x1a3f4
   __TEXT.__oslogstring: 0x5ad
   __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x1700
+  __TEXT.__unwind_info: 0x16f8
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0x2bc
-  __TEXT.__objc_methname: 0xcaa0
-  __TEXT.__objc_methtype: 0x113e
-  __TEXT.__objc_stubs: 0x7bc0
+  __TEXT.__objc_methname: 0xcaaf
+  __TEXT.__objc_methtype: 0x114c
+  __TEXT.__objc_stubs: 0x7be0
   __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x172c
+  __DATA_CONST.__const: 0x177c
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2af0
+  __DATA_CONST.__objc_selrefs: 0x2af8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x240
-  __AUTH_CONST.__auth_got: 0x800
+  __AUTH_CONST.__auth_got: 0x808
   __AUTH_CONST.__const: 0xb18
-  __AUTH_CONST.__cfstring: 0x52e0
+  __AUTH_CONST.__cfstring: 0x5320
   __AUTH_CONST.__objc_const: 0x7210
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C5DE96CC-EA7F-3990-998A-11699DC5001B
-  Functions: 2842
-  Symbols:   8333
-  CStrings:  6059
+  UUID: 5D674B91-8107-338F-A84A-98FAD6B32BE2
+  Functions: 2845
+  Symbols:   8342
+  CStrings:  6073
 
Symbols:
+ -[HDSDeviceOperationHomeKitSetup startHomeNameCreation:namingIssue:]
+ -[HDSSetupService _handlePreAuthRequest:responseHandler:].cold.13
+ -[HDSSetupSession homeKitStartHomeNameCreation:namingIssue:]
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1667
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1667.cold.1
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.343
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.345
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.345.cold.1
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.661
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.661.cold.1
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.683
+ ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_13
+ ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_13.cold.1
+ ___60-[HDSSetupSession homeKitStartHomeNameCreation:namingIssue:]_block_invoke
+ ___60-[HDSSetupSession homeKitStartHomeNameCreation:namingIssue:]_block_invoke.cold.1
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.508
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.508.cold.1
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.508.cold.2
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.508.cold.3
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1814
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1815
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1815.cold.1
+ ___block_descriptor_45_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e33_v28?0B8"NSString"12"NSError"20ls32l8r48l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0ls32l8r48l8r56l8s40l8
+ ___block_literal_global.1016
+ ___block_literal_global.1345
+ ___block_literal_global.1349
+ ___block_literal_global.1361
+ ___block_literal_global.1365
+ ___block_literal_global.1370
+ ___block_literal_global.1374
+ ___block_literal_global.1386
+ ___block_literal_global.1399
+ ___block_literal_global.1403
+ ___block_literal_global.1407
+ ___block_literal_global.1417
+ ___block_literal_global.1421
+ ___block_literal_global.1669
+ ___block_literal_global.3572
+ ___block_literal_global.3580
+ ___block_literal_global.3583
+ ___block_literal_global.3586
+ ___block_literal_global.3594
+ ___block_literal_global.3598
+ ___block_literal_global.3612
+ ___block_literal_global.3616
+ ___block_literal_global.3630
+ ___block_literal_global.3636
+ ___block_literal_global.3640
+ ___block_literal_global.3644
+ ___block_literal_global.3662
+ ___block_literal_global.3674
+ ___block_literal_global.3678
+ ___block_literal_global.3681
+ ___block_literal_global.3684
+ ___block_literal_global.3688
+ ___block_literal_global.3693
+ ___block_literal_global.3697
+ ___block_literal_global.3702
+ ___block_literal_global.3706
+ ___block_literal_global.3709
+ ___block_literal_global.3716
+ ___block_literal_global.3719
+ ___block_literal_global.3723
+ ___block_literal_global.3729
+ ___block_literal_global.3733
+ ___block_literal_global.3737
+ ___block_literal_global.3838
+ ___block_literal_global.601
+ ___block_literal_global.666
+ ___block_literal_global.703
+ ___block_literal_global.775
+ ___block_literal_global.979
+ _objc_msgSend$homePodHasCaptiveNetwork
+ _objc_msgSend$startHomeNameCreation:namingIssue:
+ _os_eligibility_get_domain_answer
- -[HDSDeviceOperationHomeKitSetup startHomeNameCreation:hasMultipleHomes:]
- -[HDSSetupSession homeKitStartHomeNameCreation:hasMultipleHomes:]
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1661
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1661.cold.1
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.340
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.342
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.342.cold.1
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.658
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.658.cold.1
- ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.680
- ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_10.cold.1
- ___65-[HDSSetupSession homeKitStartHomeNameCreation:hasMultipleHomes:]_block_invoke
- ___65-[HDSSetupSession homeKitStartHomeNameCreation:hasMultipleHomes:]_block_invoke.cold.1
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.505
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.505.cold.1
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.505.cold.2
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.505.cold.3
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1808
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1809
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1809.cold.1
- ___block_descriptor_42_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e33_v28?0B8"NSString"12"NSError"20ls32l8r48l8s40l8
- ___block_literal_global.1009
- ___block_literal_global.1338
- ___block_literal_global.1342
- ___block_literal_global.1354
- ___block_literal_global.1358
- ___block_literal_global.1363
- ___block_literal_global.1367
- ___block_literal_global.1379
- ___block_literal_global.1385
- ___block_literal_global.1396
- ___block_literal_global.1400
- ___block_literal_global.1410
- ___block_literal_global.1414
- ___block_literal_global.1663
- ___block_literal_global.3562
- ___block_literal_global.3566
- ___block_literal_global.3570
- ___block_literal_global.3573
- ___block_literal_global.3584
- ___block_literal_global.3588
- ___block_literal_global.3602
- ___block_literal_global.3606
- ___block_literal_global.3619
- ___block_literal_global.3622
- ___block_literal_global.3625
- ___block_literal_global.3629
- ___block_literal_global.3651
- ___block_literal_global.3663
- ___block_literal_global.3667
- ___block_literal_global.3670
- ___block_literal_global.3673
- ___block_literal_global.3677
- ___block_literal_global.3682
- ___block_literal_global.3686
- ___block_literal_global.3691
- ___block_literal_global.3695
- ___block_literal_global.3698
- ___block_literal_global.3701
- ___block_literal_global.3705
- ___block_literal_global.3708
- ___block_literal_global.3715
- ___block_literal_global.3718
- ___block_literal_global.3722
- ___block_literal_global.3827
- ___block_literal_global.598
- ___block_literal_global.663
- ___block_literal_global.700
- ___block_literal_global.772
- ___block_literal_global.972
- _objc_msgSend$startHomeNameCreation:hasMultipleHomes:
Functions:
~ ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_4 : 8 -> 224
~ ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_5 : 8 -> 16
~ ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_10 : 176 -> 8
+ ___41-[HDSSetupService _handleSessionStarted:]_block_invoke_13
~ -[HDSSetupService _handlePreAuthRequest:responseHandler:] : 3388 -> 3508
~ _OUTLINED_FUNCTION_4 : 12 -> 16
~ _OUTLINED_FUNCTION_5 : 16 -> 12
~ _OUTLINED_FUNCTION_6 : 8 -> 16
+ _OUTLINED_FUNCTION_7
~ -[HDSSetupSession _runHomeKitPrimarySSIDFetch] : 2644 -> 2708
~ -[HDSSetupSession _runPreAuthRequest] : 1248 -> 1364
~ ___34-[HDSSetupSession _runCaptiveJoin]_block_invoke_2 : 1204 -> 1224
~ -[HDSSetupSession _logUsageMetrics:] : 1876 -> 1976
~ -[HDSSetupSession createWiFiConfigurationForSetup:password:] : 240 -> 860
~ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke : 836 -> 888
~ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke_2 : 232 -> 208
~ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke_3 : 232 -> 264
~ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke_4 : 204 -> 136
~ -[HDSSetupService _handleBasicConfigRequest:].cold.5 : 88 -> 84
~ -[HDSSetupService _handleBasicConfigRequest:].cold.6 : 88 -> 84
~ -[HDSSetupService _handlePreAuthRequest:responseHandler:].cold.11 : 52 -> 84
+ -[HDSSetupService _handlePreAuthRequest:responseHandler:].cold.13
~ -[HDSSetupSession _run] : 3652 -> 3708
~ -[HDSSetupSession createWiFiConfigurationForSetup:password:].cold.1 : 28 -> 52
~ ___47-[HDSSetupSession validateHomeName:completion:]_block_invoke_4.cold.1 : 184 -> 140
CStrings:
+ "%@ is Open Network: %s\n"
+ "-[HDSSetupService _handleSessionStarted:]_block_invoke_13"
+ "-[HDSSetupSession homeKitStartHomeNameCreation:namingIssue:]_block_invoke"
+ "Ends with invalid character"
+ "Has prohibited characters"
+ "Name Conflict"
+ "Starts with invalid character"
+ "default"
+ "hds_i_l_e"
+ "homeKitStartHomeNameCreation:namingIssue:"
+ "homePodHasCaptiveNetwork"
+ "isLocaleEligible: %s \n"
+ "isNetworkSelectionEligibleInLocale"
+ "oseligability_eu"
+ "startHomeNameCreation:namingIssue:"
+ "v24@0:8B16i20"
+ "validateHomename success %s, homeCreationIssue %s\n"
- "-[HDSSetupService _handleSessionStarted:]_block_invoke_10"
- "-[HDSSetupSession homeKitStartHomeNameCreation:hasMultipleHomes:]_block_invoke"
- "homeKitStartHomeNameCreation:hasMultipleHomes:"
- "startHomeNameCreation:hasMultipleHomes:"
- "validateHomeName error %@ | conflict name %@\n"
- "validateHomename success %s, hasMultipleHomes %s\n"

```
