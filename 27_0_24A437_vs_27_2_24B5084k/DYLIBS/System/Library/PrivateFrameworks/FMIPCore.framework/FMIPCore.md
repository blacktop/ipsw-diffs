## FMIPCore

> `/System/Library/PrivateFrameworks/FMIPCore.framework/FMIPCore`

```diff

-470.30.6.14.34
-  __TEXT.__text: 0x1c3288
+470.31.6.16.26
+  __TEXT.__text: 0x1c4658
   __TEXT.__objc_methlist: 0x1340
-  __TEXT.__const: 0x13ebc
-  __TEXT.__swift5_typeref: 0x43c9
-  __TEXT.__swift5_fieldmd: 0x6100
-  __TEXT.__constg_swiftt: 0x69e8
-  __TEXT.__swift5_reflstr: 0x5571
+  __TEXT.__const: 0x1352c
+  __TEXT.__swift5_typeref: 0x42df
+  __TEXT.__swift5_fieldmd: 0x5e1c
+  __TEXT.__constg_swiftt: 0x68b4
+  __TEXT.__swift5_reflstr: 0x5481
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__swift5_assocty: 0xd50
-  __TEXT.__cstring: 0x555c
+  __TEXT.__swift5_assocty: 0xd38
+  __TEXT.__cstring: 0x54bc
   __TEXT.__swift5_capture: 0x286c
-  __TEXT.__oslogstring: 0xaa50
+  __TEXT.__oslogstring: 0xaad0
   __TEXT.__swift5_protos: 0x74
-  __TEXT.__swift5_proto: 0xeb8
-  __TEXT.__swift5_types: 0x600
+  __TEXT.__swift5_proto: 0xe24
+  __TEXT.__swift5_types: 0x5d4
   __TEXT.__swift_as_entry: 0xa4
   __TEXT.__swift_as_ret: 0x68
   __TEXT.__swift_as_cont: 0x184
-  __TEXT.__unwind_info: 0x66f0
-  __TEXT.__eh_frame: 0x49f0
+  __TEXT.__unwind_info: 0x6510
+  __TEXT.__eh_frame: 0x46c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__const: 0x450
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90

   __DATA_CONST.__objc_selrefs: 0x15f8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x12f59
-  __AUTH_CONST.__objc_const: 0xf250
-  __AUTH_CONST.__auth_got: 0x14a8
-  __AUTH.__objc_data: 0x11b8
-  __AUTH.__data: 0x4fb8
-  __DATA.__data: 0x1af0
-  __DATA.__common: 0x380
+  __AUTH_CONST.__const: 0x128c1
+  __AUTH_CONST.__objc_const: 0xf1e8
+  __AUTH_CONST.__auth_got: 0x1610
+  __AUTH.__objc_data: 0x1208
+  __AUTH.__data: 0x5340
+  __DATA.__data: 0x19a8
+  __DATA.__common: 0x388
   __DATA_DIRTY.__objc_data: 0x8a8
   __DATA_DIRTY.__data: 0x59c8
   __DATA_DIRTY.__bss: 0x9200

   - /System/Library/PrivateFrameworks/FMNetworking.framework/FMNetworking
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/FindMyBase.framework/FindMyBase
+  - /System/Library/PrivateFrameworks/FindMyCore.framework/FindMyCore
   - /System/Library/PrivateFrameworks/FindMyCrypto.framework/FindMyCrypto
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice
   - /System/Library/PrivateFrameworks/FindMyDeviceAccessories.framework/FindMyDeviceAccessories

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8929
-  Symbols:   423
-  CStrings:  1422
+  Functions: 8812
+  Symbols:   424
+  CStrings:  1414
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftIntents
CStrings:
+ "FMIPDevice:\n    -- id: %s,\n    -- name: %s,\n    -- baId: %s\n    -- isAccessory: %{bool}d\n    -- onlineLocation: %s\n    -- offlineLocation: %s\n    -- bestLocation: %s\n    -- itemGroup: %s\n    -- itemGroupItemsId: %s\n    -- deviceConnectedType: %s\n    -- deviceAssociatedWithBeacon: %s\n    -- productCapabilities: %ld"
+ "FMIPManager: Failed to instantiate demo beacon refreshing controller due to error: %s"
+ "companionDeviceIdentifier"
- "FMIPDevice:\n    -- id: %s,\n    -- name: %s,\n    -- baId: %s\n    -- isAccessory: %{bool}d\n    -- onlineLocation: %s\n    -- offlineLocation: %s\n    -- bestLocation: %s\n    -- itemGroup: %s\n    -- itemGroupItemsId: %s\n    -- deviceConnectedType: %s\n    -- deviceAssociatedWithBeacon: %s"
- "MacBookPro16_1-spacegray"
- "airpods"
- "categoryTemplate"
- "iMacPro"
- "iMacPro1_1-silver"
- "iPad"
- "iPhone"
- "iphone11ProMax-1-2-0"
- "macbookPro"
- "watch"
```
