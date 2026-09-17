## FMIPCore

> `/System/Library/PrivateFrameworks/FMIPCore.framework/Versions/A/FMIPCore`

```diff

-470.20.6.14.30
-  __TEXT.__text: 0x1b9f5c
+470.21.6.16.27
+  __TEXT.__text: 0x1bb17c
   __TEXT.__objc_methlist: 0x1310
-  __TEXT.__const: 0x13c8c
-  __TEXT.__swift5_typeref: 0x423b
-  __TEXT.__swift5_fieldmd: 0x6090
-  __TEXT.__constg_swiftt: 0x68cc
-  __TEXT.__swift5_reflstr: 0x5501
+  __TEXT.__const: 0x132cc
+  __TEXT.__swift5_typeref: 0x4149
+  __TEXT.__swift5_fieldmd: 0x5dac
+  __TEXT.__constg_swiftt: 0x6798
+  __TEXT.__swift5_reflstr: 0x5411
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__swift5_assocty: 0xd50
-  __TEXT.__cstring: 0x53cc
-  __TEXT.__swift5_capture: 0x2694
-  __TEXT.__oslogstring: 0xa540
+  __TEXT.__swift5_assocty: 0xd38
+  __TEXT.__cstring: 0x532c
+  __TEXT.__swift5_capture: 0x2684
+  __TEXT.__oslogstring: 0xa5c0
   __TEXT.__swift5_protos: 0x6c
-  __TEXT.__swift5_proto: 0xeac
-  __TEXT.__swift5_types: 0x5f8
+  __TEXT.__swift5_proto: 0xe18
+  __TEXT.__swift5_types: 0x5cc
   __TEXT.__swift_as_entry: 0x78
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x114
-  __TEXT.__unwind_info: 0x63f0
-  __TEXT.__eh_frame: 0x43f0
+  __TEXT.__unwind_info: 0x6238
+  __TEXT.__eh_frame: 0x40c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x448
+  __DATA_CONST.__const: 0x450
   __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90

   __DATA_CONST.__objc_selrefs: 0x1580
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x12a01
-  __AUTH_CONST.__objc_const: 0xefb8
-  __AUTH_CONST.__auth_got: 0x13c0
-  __AUTH.__objc_data: 0x11b8
-  __AUTH.__data: 0x4f20
-  __DATA.__data: 0x1a88
-  __DATA.__common: 0x380
+  __AUTH_CONST.__const: 0x12319
+  __AUTH_CONST.__objc_const: 0xef50
+  __AUTH_CONST.__auth_got: 0x1520
+  __AUTH.__objc_data: 0x1208
+  __AUTH.__data: 0x52a8
+  __DATA.__data: 0x1930
+  __DATA.__common: 0x388
   __DATA_DIRTY.__objc_data: 0x8a8
-  __DATA_DIRTY.__data: 0x5808
+  __DATA_DIRTY.__data: 0x5818
   __DATA_DIRTY.__bss: 0x9200
   __DATA_DIRTY.__common: 0x328
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /System/Library/PrivateFrameworks/FMNetworking.framework/Versions/A/FMNetworking
   - /System/Library/PrivateFrameworks/FeatureFlags.framework/Versions/A/FeatureFlags
   - /System/Library/PrivateFrameworks/FindMyBase.framework/Versions/A/FindMyBase
+  - /System/Library/PrivateFrameworks/FindMyCore.framework/Versions/A/FindMyCore
   - /System/Library/PrivateFrameworks/FindMyCrypto.framework/Versions/A/FindMyCrypto
   - /System/Library/PrivateFrameworks/FindMyDevice.framework/Versions/A/FindMyDevice
   - /System/Library/PrivateFrameworks/FindMyDeviceAccessories.framework/Versions/A/FindMyDeviceAccessories

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
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
-  Functions: 8764
-  Symbols:   408
-  CStrings:  1399
+  Functions: 8643
+  Symbols:   409
+  CStrings:  1391
 
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
