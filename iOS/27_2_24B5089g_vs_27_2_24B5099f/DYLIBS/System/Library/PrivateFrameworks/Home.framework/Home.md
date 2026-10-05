## Home

> `/System/Library/PrivateFrameworks/Home.framework/Home`

```diff

-1265.0.0.1.1
-  __TEXT.__text: 0x3aa118
-  __TEXT.__objc_methlist: 0x2cb7c
-  __TEXT.__const: 0x5970
+1269.2.3.0.1
+  __TEXT.__text: 0x3aa8f0
+  __TEXT.__objc_methlist: 0x2cbe4
+  __TEXT.__const: 0x5978
   __TEXT.__dlopen_cstrs: 0x4b
   __TEXT.__swift5_typeref: 0x2cd4
-  __TEXT.__oslogstring: 0x1da48
+  __TEXT.__oslogstring: 0x1db38
   __TEXT.__swift5_reflstr: 0xee3
   __TEXT.__swift5_assocty: 0x320
   __TEXT.__swift5_fieldmd: 0x1238
   __TEXT.__constg_swiftt: 0x2274
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__cstring: 0x34f66
+  __TEXT.__cstring: 0x35011
   __TEXT.__swift5_protos: 0x44
   __TEXT.__swift5_proto: 0x260
   __TEXT.__swift5_types: 0x19c

   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0x4d2c
   __TEXT.__ustring: 0x72
-  __TEXT.__unwind_info: 0x12130
-  __TEXT.__eh_frame: 0x7460
+  __TEXT.__unwind_info: 0x12150
+  __TEXT.__eh_frame: 0x7498
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x112b0
+  __DATA_CONST.__const: 0x112c0
   __DATA_CONST.__objc_classlist: 0x1888
   __DATA_CONST.__objc_catlist: 0x418
   __DATA_CONST.__objc_protolist: 0x948
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13130
+  __DATA_CONST.__objc_selrefs: 0x13170
   __DATA_CONST.__objc_protorefs: 0x420
   __DATA_CONST.__objc_superrefs: 0x1320
   __DATA_CONST.__objc_arraydata: 0x3d8
   __DATA_CONST.__got: 0x32b0
   __AUTH_CONST.__const: 0xf470
-  __AUTH_CONST.__cfstring: 0x275a0
-  __AUTH_CONST.__objc_const: 0x4c650
+  __AUTH_CONST.__cfstring: 0x27620
+  __AUTH_CONST.__objc_const: 0x4c660
   __AUTH_CONST.__objc_intobj: 0x2358
   __AUTH_CONST.__objc_doubleobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x270

   __AUTH.__objc_data: 0xa458
   __AUTH.__data: 0x1550
   __DATA.__objc_ivar: 0x1614
-  __DATA.__data: 0x7970
+  __DATA.__data: 0x7980
   __DATA.__objc_stublist: 0x10
   __DATA.__common: 0x148
   __DATA_DIRTY.__objc_ivar: 0xcb8
   __DATA_DIRTY.__objc_data: 0x6750
-  __DATA_DIRTY.__data: 0xf20
-  __DATA_DIRTY.__bss: 0x1e40
+  __DATA_DIRTY.__data: 0xf30
+  __DATA_DIRTY.__bss: 0x1e38
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21297
-  Symbols:   30349
-  CStrings:  8570
+  Functions: 21306
+  Symbols:   30361
+  CStrings:  8577
 
Symbols:
+ +[HFHomeKitDispatcher isProxPairingLaunch]
+ +[HFHomeKitDispatcher setIsProxPairingLaunch:]
+ +[HFSetupPairingControllerUtilities factoryResetRequiredDescriptionForCategory:]
+ +[HFSetupPairingControllerUtilities factoryResetRequiredTitleForCategory:]
+ -[HFHomeKitDispatcher _allowsLocationSensing]
+ -[HFSetupAccessoryResult _allZerosSetupCodeError]
+ -[HFSoftwareUpdateManager isSoftwareUpdateOnAssetServer:]
+ -[HMAccessory(HFSoftwareUpdateAdditions) hf_isSoftwareUpdateOnAssetServer]
+ GCC_except_table171
+ GCC_except_table201
+ GCC_except_table202
+ GCC_except_table205
+ GCC_except_table39
+ GCC_except_table45
+ GCC_except_table59
+ GCC_except_table77
+ GCC_except_table79
+ _HFPreferencesCameraClipsDebugMenuKey
+ ___isProxPairingLaunch
- GCC_except_table168
- GCC_except_table199
- GCC_except_table200
- GCC_except_table203
- GCC_except_table57
- GCC_except_table70
- GCC_except_table78
CStrings:
+ "HFSetupPairingControllerStatusDescriptionFailureFactoryResetRequired"
+ "HFSetupPairingControllerStatusTitleFailureFactoryResetRequired"
+ "No software update to check: %@"
+ "OnAssetServer"
+ "Update State: %@; On Asset Server: %{BOOL}d; %@"
+ "_allowsLocationSensing -> %{bool}d (hostProcess: %ld, isAllowedProcess: %{bool}d, isProxPairingLaunchInHomeUIService: %{bool}d, isRunningOnAccessory: %{bool}d)"
+ "cameraClipsShowDebugMenu"
```
