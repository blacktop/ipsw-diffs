## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-345.10.20.0.0
-  __TEXT.__text: 0x6faa0
+345.10.22.0.0
+  __TEXT.__text: 0x6fc00
   __TEXT.__auth_stubs: 0xff0
   __TEXT.__objc_methlist: 0x30fc
   __TEXT.__const: 0x438
-  __TEXT.__cstring: 0x1a524
+  __TEXT.__cstring: 0x1a534
   __TEXT.__oslogstring: 0x5bd
   __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x24
-  __TEXT.__unwind_info: 0x16f8
+  __TEXT.__unwind_info: 0x1708
   __TEXT.__eh_frame: 0x460
   __TEXT.__objc_classname: 0x2bc
   __TEXT.__objc_methname: 0xcb4d

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 710B0D51-5F8D-3D7A-B752-41CAAB4A69F2
-  Functions: 2848
-  Symbols:   8356
-  CStrings:  6090
+  UUID: 9681937A-44C4-3DD9-B8E6-86464C853DB7
+  Functions: 2849
+  Symbols:   8358
+  CStrings:  6091
 
Symbols:
+ -[HDSSetupSession _runDataAndPrivacy].cold.5
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1666
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1666.cold.1
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1813
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1814
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1814.cold.1
+ ___block_literal_global.1668
+ ___block_literal_global.3575
+ ___block_literal_global.3579
+ ___block_literal_global.3583
+ ___block_literal_global.3586
+ ___block_literal_global.3589
+ ___block_literal_global.3597
+ ___block_literal_global.3601
+ ___block_literal_global.3615
+ ___block_literal_global.3619
+ ___block_literal_global.3633
+ ___block_literal_global.3636
+ ___block_literal_global.3639
+ ___block_literal_global.3643
+ ___block_literal_global.3647
+ ___block_literal_global.3665
+ ___block_literal_global.3677
+ ___block_literal_global.3681
+ ___block_literal_global.3684
+ ___block_literal_global.3687
+ ___block_literal_global.3691
+ ___block_literal_global.3696
+ ___block_literal_global.3700
+ ___block_literal_global.3705
+ ___block_literal_global.3709
+ ___block_literal_global.3712
+ ___block_literal_global.3715
+ ___block_literal_global.3719
+ ___block_literal_global.3722
+ ___block_literal_global.3726
+ ___block_literal_global.3729
+ ___block_literal_global.3732
+ ___block_literal_global.3736
+ ___block_literal_global.3740
+ ___block_literal_global.3841
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1665
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1665.cold.1
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1812
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1813
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1813.cold.1
- ___block_literal_global.1667
- ___block_literal_global.3574
- ___block_literal_global.3578
- ___block_literal_global.3582
- ___block_literal_global.3585
- ___block_literal_global.3588
- ___block_literal_global.3596
- ___block_literal_global.3600
- ___block_literal_global.3614
- ___block_literal_global.3618
- ___block_literal_global.3632
- ___block_literal_global.3635
- ___block_literal_global.3638
- ___block_literal_global.3642
- ___block_literal_global.3646
- ___block_literal_global.3664
- ___block_literal_global.3676
- ___block_literal_global.3680
- ___block_literal_global.3683
- ___block_literal_global.3686
- ___block_literal_global.3690
- ___block_literal_global.3695
- ___block_literal_global.3699
- ___block_literal_global.3704
- ___block_literal_global.3708
- ___block_literal_global.3711
- ___block_literal_global.3714
- ___block_literal_global.3718
- ___block_literal_global.3721
- ___block_literal_global.3725
- ___block_literal_global.3728
- ___block_literal_global.3731
- ___block_literal_global.3735
- ___block_literal_global.3739
- ___block_literal_global.3840
Functions:
~ -[HDSSetupSession _runDataAndPrivacy] : 976 -> 1276
~ -[HDSSetupSession _runDataAndPrivacy].cold.4 : 28 -> 52
+ -[HDSSetupSession _runAuthKitTrustStartIfNeeded].cold.1
CStrings:
+ "DataAndPrivacy Skipping\n"

```
