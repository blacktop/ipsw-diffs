## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-345.50.7.0.0
-  __TEXT.__text: 0x7150c
+345.50.9.0.0
+  __TEXT.__text: 0x715d0
   __TEXT.__auth_stubs: 0xfb0
-  __TEXT.__objc_methlist: 0x30fc
+  __TEXT.__objc_methlist: 0x310c
   __TEXT.__const: 0x468
-  __TEXT.__cstring: 0x1a344
+  __TEXT.__cstring: 0x1a354
   __TEXT.__oslogstring: 0x5bd
   __TEXT.__gcc_except_tab: 0x1a4
   __TEXT.__constg_swiftt: 0xe0

   __TEXT.__unwind_info: 0x1800
   __TEXT.__eh_frame: 0x480
   __TEXT.__objc_classname: 0x31b
-  __TEXT.__objc_methname: 0xcbc2
+  __TEXT.__objc_methname: 0xcbcf
   __TEXT.__objc_methtype: 0x11ab
-  __TEXT.__objc_stubs: 0x7c80
+  __TEXT.__objc_stubs: 0x7ca0
   __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x1780
+  __DATA_CONST.__const: 0x1788
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b18
+  __DATA_CONST.__objc_selrefs: 0x2b20
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x230
   __AUTH_CONST.__auth_got: 0x7e8
   __AUTH_CONST.__const: 0xb18
-  __AUTH_CONST.__cfstring: 0x5360
+  __AUTH_CONST.__cfstring: 0x53a0
   __AUTH_CONST.__objc_const: 0x7250
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x3c0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 27307795-9B2B-3295-96D9-89DB74893702
-  Functions: 2973
-  Symbols:   8603
-  CStrings:  6080
+  UUID: DB768872-6C38-3AAD-B7EB-ABD8FBEEBE6C
+  Functions: 2974
+  Symbols:   8607
+  CStrings:  6085
 
Symbols:
+ +[HDSDefaults usesEthernet]
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1714
+ ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1714.cold.1
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1861
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1862
+ ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1862.cold.1
+ ___block_literal_global.1716
+ ___block_literal_global.3623
+ ___block_literal_global.3627
+ ___block_literal_global.3637
+ ___block_literal_global.3645
+ ___block_literal_global.3649
+ ___block_literal_global.3663
+ ___block_literal_global.3667
+ ___block_literal_global.3686
+ ___block_literal_global.3690
+ ___block_literal_global.3694
+ ___block_literal_global.3712
+ ___block_literal_global.3724
+ ___block_literal_global.3734
+ ___block_literal_global.3738
+ ___block_literal_global.3743
+ ___block_literal_global.3747
+ ___block_literal_global.3752
+ ___block_literal_global.3762
+ ___block_literal_global.3769
+ ___block_literal_global.3779
+ ___block_literal_global.3783
+ ___block_literal_global.3787
+ ___block_literal_global.3888
+ _kDefaultsKey_UsesEthernet
+ _objc_msgSend$usesEthernet
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1711
- ___32-[HDSSetupSession _runWiFiSetup]_block_invoke_2.1711.cold.1
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke.1858
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1859
- ___73-[HDSSetupSession _runMultiUserEnableEnableSettingStart:privateSettings:]_block_invoke_2.1859.cold.1
- ___block_literal_global.1713
- ___block_literal_global.3620
- ___block_literal_global.3624
- ___block_literal_global.3628
- ___block_literal_global.3642
- ___block_literal_global.3646
- ___block_literal_global.3660
- ___block_literal_global.3664
- ___block_literal_global.3677
- ___block_literal_global.3687
- ___block_literal_global.3691
- ___block_literal_global.3709
- ___block_literal_global.3721
- ___block_literal_global.3725
- ___block_literal_global.3735
- ___block_literal_global.3740
- ___block_literal_global.3744
- ___block_literal_global.3749
- ___block_literal_global.3753
- ___block_literal_global.3763
- ___block_literal_global.3770
- ___block_literal_global.3780
- ___block_literal_global.3784
- ___block_literal_global.3885
Functions:
+ +[HDSDefaults numberOfWiFiRetries]
~ -[HDSSetupSession _runPreflightWiFi] : 3948 -> 3976
~ -[HDSSetupSession preflightCheckPhonesNetwork] : 3476 -> 3504
~ -[HDSSetupSession _run] : 3480 -> 3576
CStrings:
+ "owe"
+ "usesEthernet"

```
