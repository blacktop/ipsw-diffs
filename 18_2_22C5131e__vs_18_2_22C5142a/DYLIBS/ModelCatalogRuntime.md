## ModelCatalogRuntime

> `/System/Library/PrivateFrameworks/ModelCatalogRuntime.framework/ModelCatalogRuntime`

```diff

-158.622.1.0.0
-  __TEXT.__text: 0x2a2c8
-  __TEXT.__auth_stubs: 0x14a0
+158.631.0.0.0
+  __TEXT.__text: 0x25f1c
+  __TEXT.__auth_stubs: 0x1440
   __TEXT.__objc_methlist: 0x144
-  __TEXT.__const: 0x470
-  __TEXT.__swift5_typeref: 0x786
-  __TEXT.__swift5_fieldmd: 0x19c
-  __TEXT.__constg_swiftt: 0x3e4
-  __TEXT.__cstring: 0xd3e
-  __TEXT.__oslogstring: 0x10c6
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x16d
+  __TEXT.__const: 0x3f8
+  __TEXT.__swift5_typeref: 0x694
+  __TEXT.__swift5_fieldmd: 0x154
+  __TEXT.__constg_swiftt: 0x380
+  __TEXT.__cstring: 0xd6e
+  __TEXT.__oslogstring: 0x10a8
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift5_capture: 0x3d0
+  __TEXT.__swift5_types: 0x20
+  __TEXT.__swift5_capture: 0x2a8
   __TEXT.__swift5_proto: 0x1c
+  __TEXT.__swift5_reflstr: 0x144
   __TEXT.__swift5_assocty: 0x38
   __TEXT.__unwind_info: 0x7b0
-  __TEXT.__eh_frame: 0xdd8
+  __TEXT.__eh_frame: 0x1090
   __TEXT.__objc_classname: 0x2d
-  __TEXT.__objc_methname: 0x715
+  __TEXT.__objc_methname: 0x5f6
   __TEXT.__objc_methtype: 0xe9
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0xd8
+  __DATA_CONST.__got: 0x210
+  __DATA_CONST.__const: 0x90
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1a8
+  __DATA_CONST.__objc_selrefs: 0x160
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0xa50
-  __AUTH_CONST.__auth_ptr: 0x348
-  __AUTH_CONST.__const: 0xca0
-  __AUTH_CONST.__objc_const: 0x678
+  __AUTH_CONST.__auth_got: 0xa20
+  __AUTH_CONST.__auth_ptr: 0x338
+  __AUTH_CONST.__const: 0x958
+  __AUTH_CONST.__objc_const: 0x698
   __AUTH.__objc_data: 0x1d0
   __AUTH.__data: 0x98
-  __DATA.__data: 0x380
+  __DATA.__data: 0x3c8
   __DATA.__bss: 0x200
-  __DATA_DIRTY.__objc_data: 0xe0
-  __DATA_DIRTY.__data: 0x438
-  __DATA_DIRTY.__common: 0x78
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0xe8
+  __DATA_DIRTY.__data: 0x3e0
+  __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks

   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog
   - /System/Library/PrivateFrameworks/TokenGenerationInference.framework/TokenGenerationInference
-  - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 749
-  Symbols:   166
-  CStrings:  251
+  Functions: 785
+  Symbols:   155
+  CStrings:  241
 
Symbols:
+ _swift_setDeallocating
- _OBJC_CLASS_$_UAFAssetSetManager
- _OBJC_CLASS_$_UAFAssetSetSubscription
- _objc_retain_x1
- _objc_retain_x25
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _swift_continuation_await
- _swift_continuation_init
- _swift_continuation_throwingResume
- _swift_continuation_throwingResumeWithError
- _swift_getForeignTypeMetadata
- _swift_retain_n
CStrings:
+ ". One request resource key maps to a single subscription."
+ "Attempting explicit release for resource id: %!s(MISSING)"
+ "Attempting explicit request found resource: %!s(MISSING)"
+ "CatalogServiceServer: Failed to release resource for identifier: %!s(MISSING). Error: %!@(MISSING)"
+ "CatalogServiceServer: Failed to release resources for key: %!s(MISSING). Error: %!@(MISSING)"
+ "CatalogServiceServer: Failed to request resource for identifier: %!s(MISSING). Error: %!@(MISSING)"
+ "CatalogServiceServer: Failed to request resources for key: %!s(MISSING). Error: %!@(MISSING)"
+ "Must unsubscribe under one subscription name: "
+ "com.apple.modelcatalog.migration.18.2"
+ "explicit-request-resource-"
+ "request-resources-key-"
+ "siriResourceAvailability: Enough storage on disk."
+ "siriResourceAvailability: Out of space, disk space required: %!l(MISSING)ld"
+ "siriResourceAvailability: Unable to fetch asset size for siri assets with error: %!@(MISSING)"
+ "subscriptionManager"
- "Attempting explicit replease for resource id: %!s(MISSING)"
- "Attempting explicit request  found resource: %!s(MISSING)"
- "Explicit request for resource: %!s(MISSING): %!@(MISSING)"
- "Failed to initialize UAFAssetSetSubscription for subscription name "
- "Failed to subscribe to subscription name %!s(MISSING), asset sets: %!s(MISSING)"
- "Failed to unsubscribe %!s(MISSING)"
- "Failed to unsubscribe %!s(MISSING): %!@(MISSING)"
- "ModelCatalogRuntime/AssetManager.swift"
- "No existing subscriptions to expire with requestResourcesKey %!s(MISSING)"
- "Subscribing to UAF with subscriberID: %!s(MISSING), subscriptions: %!@(MISSING)"
- "Unable to fetch asset size for siri assets with error: %!@(MISSING)"
- "com.apple.siri.intelligenceengine"
- "diskSpaceNeededForSubscriber:subscriptionName:error:"
- "downloadStatusForSubscriber:subscriptionName:"
- "init:assetSets:usageAliases:expires:"
- "longLongValue"
- "name"
- "sharedManager"
- "siriResourceAvailability result: %!@(MISSING)"
- "subscribe:subscriptions:queue:completion:"
- "subscriptionsForSubscriber:"
- "unsubcribing from expiring lock as we have permanent lock acquired %!s(MISSING)"
- "unsubcribing from permanent lock as we are trying to remove assets %!s(MISSING)"
- "unsubscribe:subscriptionNames:queue:completion:"
- "v16@?0@\"NSError\"8"

```
