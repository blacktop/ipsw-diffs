## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-345.0.7.0.0
-  __TEXT.__text: 0x6ed64
+345.0.9.0.0
+  __TEXT.__text: 0x6f1ec
   __TEXT.__auth_stubs: 0xfe0
-  __TEXT.__objc_methlist: 0x30cc
+  __TEXT.__objc_methlist: 0x30e4
   __TEXT.__const: 0x438
-  __TEXT.__cstring: 0x1a1e4
+  __TEXT.__cstring: 0x1a334
   __TEXT.__oslogstring: 0x5ad
   __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x16d8
+  __TEXT.__unwind_info: 0x1700
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0x2bc
-  __TEXT.__objc_methname: 0xca14
+  __TEXT.__objc_methname: 0xcaa0
   __TEXT.__objc_methtype: 0x113e
-  __TEXT.__objc_stubs: 0x7b80
+  __TEXT.__objc_stubs: 0x7bc0
   __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x1754
+  __DATA_CONST.__const: 0x172c
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ad8
+  __DATA_CONST.__objc_selrefs: 0x2af0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x240
   __AUTH_CONST.__auth_got: 0x800
-  __AUTH_CONST.__const: 0xaf8
-  __AUTH_CONST.__cfstring: 0x52a0
-  __AUTH_CONST.__objc_const: 0x71d0
+  __AUTH_CONST.__const: 0xb18
+  __AUTH_CONST.__cfstring: 0x52e0
+  __AUTH_CONST.__objc_const: 0x7210
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH.__objc_data: 0x688
   __AUTH.__data: 0x2f8
-  __DATA.__objc_ivar: 0xa24
+  __DATA.__objc_ivar: 0xa2c
   __DATA.__data: 0xa40
   __DATA.__common: 0x40
   __DATA.__bss: 0x740

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 80D9DC1C-A4F8-3A14-BACB-69912E5983B4
-  Functions: 2833
-  Symbols:   8311
-  CStrings:  6044
+  UUID: C5DE96CC-EA7F-3990-998A-11699DC5001B
+  Functions: 2842
+  Symbols:   8333
+  CStrings:  6059
 
Symbols:
+ -[HDSDeviceOperationHomeKitSetup startHomeNameCreation:hasMultipleHomes:]
+ -[HDSSetupService activateWithCompletion:]
+ -[HDSSetupSession _runPreflightMisc].cold.12
+ -[HDSSetupSession homeKitStartHomeNameCreation:hasMultipleHomes:]
+ -[HDSSetupSession reportMetricsOnWiFiDismissal]
+ -[HDSSetupSession reportMetricsOnWiFiDismissal].cold.1
+ -[HDSSetupSession reportMetricsOnWiFiDismissal].cold.2
+ GCC_except_table12
+ GCC_except_table309
+ GCC_except_table368
+ GCC_except_table419
+ _OBJC_IVAR_$_HDSSetupSession._lastWiFiError
+ _OBJC_IVAR_$_HDSSetupSession._wifiJoinAttemptCompleted
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1661
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1661.cold.1
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.340
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.342
+ ___34-[HDSSetupService _sfServiceStart]_block_invoke.342.cold.1
+ ___34-[HDSSetupSession locationEnable:]_block_invoke_2
+ ___34-[HDSSetupSession locationEnable:]_block_invoke_2.cold.1
+ ___34-[HDSSetupSession locationEnable:]_block_invoke_2.cold.2
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.658
+ ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.658.cold.1
+ ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.680
+ ___42-[HDSSetupService activateWithCompletion:]_block_invoke
+ ___42-[HDSSetupService activateWithCompletion:]_block_invoke.cold.1
+ ___42-[HDSSetupService activateWithCompletion:]_block_invoke_2
+ ___42-[HDSSetupService activateWithCompletion:]_block_invoke_3
+ ___65-[HDSSetupSession homeKitStartHomeNameCreation:hasMultipleHomes:]_block_invoke
+ ___65-[HDSSetupSession homeKitStartHomeNameCreation:hasMultipleHomes:]_block_invoke.cold.1
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.505
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.505.cold.1
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.505.cold.2
+ ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.505.cold.3
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1808
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1809
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1809.cold.1
+ ___block_descriptor_56_e8_32s40bs48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e33_v28?0B8"NSString"12"NSError"20ls32l8r48l8s40l8
+ ___block_literal_global.1009
+ ___block_literal_global.1338
+ ___block_literal_global.1342
+ ___block_literal_global.1354
+ ___block_literal_global.1358
+ ___block_literal_global.1363
+ ___block_literal_global.1367
+ ___block_literal_global.1379
+ ___block_literal_global.1385
+ ___block_literal_global.1392
+ ___block_literal_global.1396
+ ___block_literal_global.1400
+ ___block_literal_global.1410
+ ___block_literal_global.1414
+ ___block_literal_global.1663
+ ___block_literal_global.3562
+ ___block_literal_global.3566
+ ___block_literal_global.3570
+ ___block_literal_global.3573
+ ___block_literal_global.3584
+ ___block_literal_global.3588
+ ___block_literal_global.3602
+ ___block_literal_global.3606
+ ___block_literal_global.3619
+ ___block_literal_global.3622
+ ___block_literal_global.3625
+ ___block_literal_global.3629
+ ___block_literal_global.3633
+ ___block_literal_global.3663
+ ___block_literal_global.3667
+ ___block_literal_global.3673
+ ___block_literal_global.3677
+ ___block_literal_global.3682
+ ___block_literal_global.3691
+ ___block_literal_global.3695
+ ___block_literal_global.3698
+ ___block_literal_global.3701
+ ___block_literal_global.3705
+ ___block_literal_global.3708
+ ___block_literal_global.3712
+ ___block_literal_global.3715
+ ___block_literal_global.3718
+ ___block_literal_global.3722
+ ___block_literal_global.3726
+ ___block_literal_global.3827
+ ___block_literal_global.598
+ ___block_literal_global.663
+ ___block_literal_global.700
+ ___block_literal_global.772
+ ___block_literal_global.972
+ _objc_msgSend$isLocationServicesEnabled
+ _objc_msgSend$startHomeNameCreation:hasMultipleHomes:
+ _objc_msgSend$updateLocationServicesEnabled:completion:
- -[HDSDeviceOperationHomeKitSetup startHomeNameCreation:hasNameConflict:]
- -[HDSSetupSession homeKitStartHomeNameCreation:hasNameConflict:]
- GCC_except_table10
- GCC_except_table308
- GCC_except_table366
- GCC_except_table417
- ___27-[HDSSetupService activate]_block_invoke.cold.1
- ___27-[HDSSetupService activate]_block_invoke_2
- ___27-[HDSSetupService activate]_block_invoke_3
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1660
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1660.cold.1
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.343
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.345
- ___34-[HDSSetupService _sfServiceStart]_block_invoke.345.cold.1
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.657
- ___37-[HDSSetupSession _runSFSessionStart]_block_invoke.657.cold.1
- ___39-[HDSSetupSession _runHomeKitSetupMode]_block_invoke_2.679
- ___64-[HDSSetupSession homeKitStartHomeNameCreation:hasNameConflict:]_block_invoke
- ___64-[HDSSetupSession homeKitStartHomeNameCreation:hasNameConflict:]_block_invoke.cold.1
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.506
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.506.cold.1
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.506.cold.2
- ___69-[HDSSetupSession exportAMSTokenAndAccountSetup:ifMissing:ifInvalid:]_block_invoke_2.506.cold.3
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1807
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1808
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1808.cold.1
- ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
- ___block_descriptor_64_e8_32s40s48r56r_e33_v28?0B8"NSString"12"NSError"20ls32l8r48l8r56l8s40l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8r56l8r64l8s48l8
- ___block_literal_global.1012
- ___block_literal_global.1340
- ___block_literal_global.1344
- ___block_literal_global.1356
- ___block_literal_global.1360
- ___block_literal_global.1365
- ___block_literal_global.1369
- ___block_literal_global.1381
- ___block_literal_global.1387
- ___block_literal_global.1394
- ___block_literal_global.1398
- ___block_literal_global.1402
- ___block_literal_global.1412
- ___block_literal_global.1416
- ___block_literal_global.1662
- ___block_literal_global.3550
- ___block_literal_global.3554
- ___block_literal_global.3558
- ___block_literal_global.3561
- ___block_literal_global.3564
- ___block_literal_global.3572
- ___block_literal_global.3590
- ___block_literal_global.3594
- ___block_literal_global.3607
- ___block_literal_global.3610
- ___block_literal_global.3613
- ___block_literal_global.3617
- ___block_literal_global.3621
- ___block_literal_global.3639
- ___block_literal_global.3655
- ___block_literal_global.3658
- ___block_literal_global.3661
- ___block_literal_global.3665
- ___block_literal_global.3674
- ___block_literal_global.3679
- ___block_literal_global.3683
- ___block_literal_global.3689
- ___block_literal_global.3693
- ___block_literal_global.3696
- ___block_literal_global.3700
- ___block_literal_global.3703
- ___block_literal_global.3706
- ___block_literal_global.3710
- ___block_literal_global.3714
- ___block_literal_global.3815
- ___block_literal_global.662
- ___block_literal_global.703
- ___block_literal_global.775
- ___block_literal_global.975
- _objc_msgSend$startHomeNameCreation:hasNameConflict:
CStrings:
+ "-[HDSSetupService activateWithCompletion:]_block_invoke"
+ "-[HDSSetupSession homeKitStartHomeNameCreation:hasMultipleHomes:]_block_invoke"
+ "-[HDSSetupSession locationEnable:]_block_invoke_2"
+ "-[HDSSetupSession reportMetricsOnWiFiDismissal]"
+ "Failed to Update Location, error %@\n"
+ "Location enabled %s\n"
+ "Reporting metrics on WiFi Dismissal \n"
+ "Successfully updated Location"
+ "WiFi has not started, skipping WiFi dismissal metric reporting\n"
+ "WiFiSetup-Dismiss"
+ "WiFiSetupMaxRetries"
+ "WiFiSetupMaxRetries-TimeOut"
+ "_lastWiFiError"
+ "_wifiJoinAttemptCompleted"
+ "homeKitStartHomeNameCreation:hasMultipleHomes:"
+ "isLocationServicesEnabled"
+ "reportMetricsOnWiFiDismissal"
+ "startHomeNameCreation:hasMultipleHomes:"
+ "updateLocationServicesEnabled:completion:"
+ "userWiFiRetryCount"
+ "validateHomename success %s, hasMultipleHomes %s\n"
- "-[HDSSetupService activate]_block_invoke"
- "-[HDSSetupSession homeKitStartHomeNameCreation:hasNameConflict:]_block_invoke"
- "Location enabled\n"
- "WiFiSetup2"
- "WiFiSetupTimeOut"
- "homeKitStartHomeNameCreation:hasNameConflict:"
- "startHomeNameCreation:hasNameConflict:"
- "validateHomename success %s, hasNameConflict %s\n"

```
