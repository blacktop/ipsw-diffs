## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-355.2.12.101.0
-  __TEXT.__text: 0x7b75c
-  __TEXT.__objc_methlist: 0x5348
+355.3.7.0.0
+  __TEXT.__text: 0x7c1f0
+  __TEXT.__objc_methlist: 0x53b8
   __TEXT.__const: 0xb28
-  __TEXT.__cstring: 0x6d1b
-  __TEXT.__gcc_except_tab: 0xfbc
-  __TEXT.__oslogstring: 0x37de
+  __TEXT.__cstring: 0x6d8b
+  __TEXT.__gcc_except_tab: 0x101c
+  __TEXT.__oslogstring: 0x388e
   __TEXT.__dlopen_cstrs: 0x2f6
   __TEXT.__swift5_typeref: 0x466
   __TEXT.__constg_swiftt: 0x1b0

   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x30
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x25c8
+  __TEXT.__unwind_info: 0x25e8
   __TEXT.__eh_frame: 0x590
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1bd0
+  __DATA_CONST.__const: 0x1c00
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c30
+  __DATA_CONST.__objc_selrefs: 0x2c70
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__got: 0x728
   __AUTH_CONST.__const: 0x8c8
-  __AUTH_CONST.__cfstring: 0x4d80
-  __AUTH_CONST.__objc_const: 0x10a18
+  __AUTH_CONST.__cfstring: 0x4e20
+  __AUTH_CONST.__objc_const: 0x10a88
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xc20
+  __AUTH_CONST.__auth_got: 0xc28
   __AUTH.__objc_data: 0x1250
   __AUTH.__data: 0x120
-  __DATA.__objc_ivar: 0x5d0
+  __DATA.__objc_ivar: 0x5d8
   __DATA.__data: 0xc80
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0xaf0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2697
-  Symbols:   3884
-  CStrings:  1103
+  Functions: 2711
+  Symbols:   3898
+  CStrings:  1110
 
Symbols:
+ +[PRSHostConfigurationEntry entryWithExtensionID:descriptorID:posterUUID:userInfo:migratedConfigurationMatchingMask:]
+ +[PRSHostConfigurationEntry entryWithExtensionID:descriptorID:userInfo:]
+ +[PRSHostConfigurationEntry supportedUserInfoValueClasses]
+ +[PRSPosterUpdate posterUpdateColumnComplications:]
+ -[PRSHostConfigurationEntry initWithExtensionID:descriptorID:posterUUID:userInfo:migratedConfigurationMatchingMask:]
+ -[PRSHostConfigurationEntry initWithExtensionID:descriptorID:userInfo:]
+ -[PRSHostConfigurationEntry setUserInfo:]
+ -[PRSHostConfigurationEntry userInfo]
+ -[PRSMigrationDescriptor setSimulatesCrossDeviceRestore:]
+ -[PRSMigrationDescriptor simulatesCrossDeviceRestore]
+ -[PRSService _deleteDataStoreTerminating:completion:]
+ _OBJC_IVAR_$_PRSHostConfigurationEntry._userInfo
+ _OBJC_IVAR_$_PRSMigrationDescriptor._simulatesCrossDeviceRestore
+ _PF_IS_V68_DEVICE
+ ___53-[PRSService _deleteDataStoreTerminating:completion:]_block_invoke
+ ___73-[PRSServer fetchAssociatedHomeScreenPosterConfigurationUUID:completion:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48bs_e40_v24?0"PFServerPosterPath"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_65_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- +[PRSHostConfigurationEntry entryWithExtensionID:descriptorID:posterUUID:migratedConfigurationMatchingMask:]
- -[PRSHostConfigurationEntry initWithExtensionID:descriptorID:posterUUID:migratedConfigurationMatchingMask:]
- ___44-[PRSService deleteDataStoreWithCompletion:]_block_invoke
- ___block_descriptor_64_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
CStrings:
+ "Data store is being deleted by process %@ (terminate: %{BOOL}u)"
+ "PRSHostContext init: skipping screen %lu (main=%{BOOL}d) — no valid orientation"
+ "PRSHostContext init: use active display (%{public}@) instead of main display (%{public}@)"
+ "PRSPosterUpdateTypeComplicationColumn"
+ "_simulatesCrossDeviceRestore"
+ "activationState"
+ "fetching poster did error in %@ : error=%@ posterUUID=%@"
+ "simulatesCrossDeviceRestore"
+ "userInfo"
- "Data store is being deleted by process %@"
- "PRSHostContext init: skipping screen %lu — no valid orientation"
```
