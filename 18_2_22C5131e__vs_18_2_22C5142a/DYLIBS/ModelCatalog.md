## ModelCatalog

> `/System/Library/PrivateFrameworks/ModelCatalog.framework/ModelCatalog`

```diff

-158.622.1.0.0
-  __TEXT.__text: 0xff540
-  __TEXT.__auth_stubs: 0x1710
+158.631.0.0.0
+  __TEXT.__text: 0x106bbc
+  __TEXT.__auth_stubs: 0x17b0
   __TEXT.__objc_methlist: 0x25c
-  __TEXT.__cstring: 0x114f0
-  __TEXT.__swift5_typeref: 0x4c58
-  __TEXT.__const: 0x227c8
-  __TEXT.__constg_swiftt: 0x554c
+  __TEXT.__cstring: 0x11770
+  __TEXT.__swift5_typeref: 0x4d9e
+  __TEXT.__const: 0x22af8
+  __TEXT.__constg_swiftt: 0x56d4
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x1a7a
-  __TEXT.__swift5_fieldmd: 0xcff0
-  __TEXT.__swift5_types: 0x8c4
-  __TEXT.__oslogstring: 0xf0d
-  __TEXT.__swift5_capture: 0x3f8c
-  __TEXT.__swift5_assocty: 0x2c68
-  __TEXT.__swift5_protos: 0xf8
-  __TEXT.__swift5_proto: 0x29e4
+  __TEXT.__swift5_reflstr: 0x1bba
+  __TEXT.__swift5_fieldmd: 0xd158
+  __TEXT.__swift5_types: 0x8d8
+  __TEXT.__oslogstring: 0x15cd
+  __TEXT.__swift5_capture: 0x402c
+  __TEXT.__swift5_assocty: 0x2c80
+  __TEXT.__swift5_protos: 0xfc
+  __TEXT.__swift5_proto: 0x2a10
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x6780
-  __TEXT.__eh_frame: 0x5090
+  __TEXT.__unwind_info: 0x6940
+  __TEXT.__eh_frame: 0x5418
   __TEXT.__objc_classname: 0x2f
-  __TEXT.__objc_methname: 0xab9
+  __TEXT.__objc_methname: 0xb4e
   __TEXT.__objc_methtype: 0xeb
-  __DATA_CONST.__got: 0x300
-  __DATA_CONST.__const: 0x1a8
-  __DATA_CONST.__objc_classlist: 0x58
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f0
+  __DATA_CONST.__objc_selrefs: 0x310
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0xb88
-  __AUTH_CONST.__auth_ptr: 0x750
-  __AUTH_CONST.__const: 0x3b6a0
-  __AUTH_CONST.__objc_const: 0xf08
+  __AUTH_CONST.__auth_got: 0xbd8
+  __AUTH_CONST.__auth_ptr: 0x7a8
+  __AUTH_CONST.__const: 0x3b998
+  __AUTH_CONST.__objc_const: 0x1000
   __AUTH.__objc_data: 0x260
-  __AUTH.__data: 0x398
-  __DATA.__data: 0x42a8
-  __DATA.__bss: 0x44e00
+  __AUTH.__data: 0x4c0
+  __DATA.__data: 0x43a0
+  __DATA.__bss: 0x45300
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x4c8
-  __DATA_DIRTY.__data: 0x3658
+  __DATA_DIRTY.__data: 0x3770
   __DATA_DIRTY.__bss: 0xd880
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 16321
-  Symbols:   216
-  CStrings:  1403
+  Functions: 16491
+  Symbols:   221
+  CStrings:  1439
 
Symbols:
+ _OBJC_CLASS_$_UAFAssetSetSubscription
+ _objc_retain_x1
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
- _UAFSubscriptionDownloadStatusDescription
CStrings:
+ "Can't construct Array with count < 0"
+ "Cancelled download request updates for settings"
+ "Failed to create UAFAssetSetSubscription for subscription: "
+ "Failed to subscribe for subscription: "
+ "Failed to unsubscribe for subscription: "
+ "Finish request download for settings"
+ "Negative value is not representable"
+ "SubscriptionManagerProvider: Could not retrieve the disk space needed for subscriber: %!s(MISSING), subscription name: %!s(MISSING). Error: %!@(MISSING)"
+ "SubscriptionManagerProvider: Disk space needed for subscriber: %!s(MISSING), subscription name: %!s(MISSING), bytes: %!l(MISSING)ld"
+ "SubscriptionManagerProvider: Download status for subscriber: %!s(MISSING), subscription name: %!s(MISSING), returned download status: %!s(MISSING)"
+ "SubscriptionManagerProvider: Download status type of: %!l(MISSING)u has not been accounted for"
+ "SubscriptionManagerProvider: Failed to create UAFAssetSetSubscription for subscription: %!s(MISSING)"
+ "SubscriptionManagerProvider: Finished request to update assets for subscriber: %!s(MISSING), subscription name: %!s(MISSING)"
+ "SubscriptionManagerProvider: Progress received for subscriber: %!s(MISSING), subscription name: %!s(MISSING) - %!f(MISSING)"
+ "SubscriptionManagerProvider: Request ID %!s(MISSING). Failed to subscribe."
+ "SubscriptionManagerProvider: Request ID %!s(MISSING). Failed to unsubscribe."
+ "SubscriptionManagerProvider: Request ID: %!s(MISSING), requesting unsubscribe for: %!s(MISSING), subscription name: %!s(MISSING)"
+ "SubscriptionManagerProvider: Request ID: %!s(MISSING), subscription request for: %!s(MISSING), UAF subscription: %!@(MISSING)"
+ "SubscriptionManagerProvider: Request ID: %!s(MISSING), successfully subscribed to subscription %!s(MISSING)"
+ "SubscriptionManagerProvider: Starting request to retrieve disk space needed for subscriber: %!s(MISSING), subscription name: %!s(MISSING)"
+ "SubscriptionManagerProvider: Starting request to retrieve download status for subscriber: %!s(MISSING), subscription name: %!s(MISSING)"
+ "SubscriptionManagerProvider: Starting request to update assets for subscriber: %!s(MISSING), subscription name: %!s(MISSING)"
+ "Swift/Array.swift"
+ "Swift/Integers.swift"
+ "Unable to unsubscribe using request resources key: "
+ "Unexpected termination while requesting download for settings"
+ "_TtC12ModelCatalog27SubscriptionManagerProvider"
+ "catalogIndex"
+ "com.apple.modelcatalog.request-download-for-settings"
+ "com.apple.siri.intelligenceengine"
+ "initWithName:assetSets:usageAliases:expires:"
+ "longLongValue"
+ "manager"
+ "resourceBundleOverrides"
+ "resourceOverrides"
+ "subscribe:subscriptions:queue:completion:"
+ "subscriptionManager"
+ "unableToUnsubscribe"
+ "unsubscribe:subscriptionNames:queue:completion:"
- "Unknown download status: %!s(MISSING)"
- "staticResourceBundles"
- "staticResources"

```
