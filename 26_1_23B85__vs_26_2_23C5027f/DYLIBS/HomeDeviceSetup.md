## HomeDeviceSetup

> `/System/Library/PrivateFrameworks/HomeDeviceSetup.framework/HomeDeviceSetup`

```diff

-345.10.23.0.0
-  __TEXT.__text: 0x6fcac
-  __TEXT.__auth_stubs: 0xff0
+345.20.5.0.0
+  __TEXT.__text: 0x6fac0
+  __TEXT.__auth_stubs: 0xfe0
   __TEXT.__objc_methlist: 0x30fc
   __TEXT.__const: 0x468
-  __TEXT.__cstring: 0x1a534
+  __TEXT.__cstring: 0x1a524
   __TEXT.__oslogstring: 0x5bd
   __TEXT.__gcc_except_tab: 0x1a8
   __TEXT.__constg_swiftt: 0xe0

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x230
-  __AUTH_CONST.__auth_got: 0x808
+  __AUTH_CONST.__auth_got: 0x800
   __AUTH_CONST.__const: 0xb18
   __AUTH_CONST.__cfstring: 0x5360
   __AUTH_CONST.__objc_const: 0x7250

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 13628D3A-BF20-38C5-A025-614149D2FCB2
+  UUID: 2549A835-A63F-326E-98CC-E015C8327F0E
   Functions: 2849
-  Symbols:   8358
-  CStrings:  6091
+  Symbols:   8357
+  CStrings:  6090
 
Symbols:
+ ___block_literal_global.3632
+ ___block_literal_global.3635
+ ___block_literal_global.3638
+ ___block_literal_global.3642
+ ___block_literal_global.3646
+ ___block_literal_global.3664
+ ___block_literal_global.3676
+ ___block_literal_global.3680
+ ___block_literal_global.3683
+ ___block_literal_global.3686
+ ___block_literal_global.3690
+ ___block_literal_global.3695
+ ___block_literal_global.3699
+ ___block_literal_global.3704
+ ___block_literal_global.3708
+ ___block_literal_global.3711
+ ___block_literal_global.3714
+ ___block_literal_global.3718
+ ___block_literal_global.3721
+ ___block_literal_global.3725
+ ___block_literal_global.3728
+ ___block_literal_global.3731
+ ___block_literal_global.3735
+ ___block_literal_global.3739
+ ___block_literal_global.3840
- ___block_literal_global.3633
- ___block_literal_global.3636
- ___block_literal_global.3639
- ___block_literal_global.3643
- ___block_literal_global.3647
- ___block_literal_global.3665
- ___block_literal_global.3677
- ___block_literal_global.3681
- ___block_literal_global.3684
- ___block_literal_global.3687
- ___block_literal_global.3691
- ___block_literal_global.3696
- ___block_literal_global.3700
- ___block_literal_global.3705
- ___block_literal_global.3709
- ___block_literal_global.3712
- ___block_literal_global.3715
- ___block_literal_global.3719
- ___block_literal_global.3722
- ___block_literal_global.3726
- ___block_literal_global.3729
- ___block_literal_global.3732
- ___block_literal_global.3736
- ___block_literal_global.3740
- ___block_literal_global.3841
- _os_eligibility_get_domain_answer
Functions:
~ +[HDSDefaults sysDropBuildMode] : 152 -> 96
~ -[HDSSetupSession _runHomeKitPrimarySSIDFetch] : 2680 -> 2616
~ -[HDSSetupSession _runPreAuthRequest] : 1364 -> 1272
~ -[HDSSetupSession _logUsageMetrics:] : 1976 -> 1900
~ -[HDSSetupSession createWiFiConfigurationForSetup:password:] : 860 -> 720
~ -[HDSSetupSession _run] : 3728 -> 3664
CStrings:
+ "sysdrop_carry"
- "oseligibility_eu"
- "sysdrop_external"

```
