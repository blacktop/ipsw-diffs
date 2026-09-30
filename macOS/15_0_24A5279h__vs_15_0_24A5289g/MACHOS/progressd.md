## progressd

> `/System/Library/Frameworks/ClassKit.framework/Versions/A/progressd`

```diff

-150.0.52.0.0
-  __TEXT.__text: 0x18a320
-  __TEXT.__auth_stubs: 0x1510
-  __TEXT.__objc_stubs: 0x14bc0
-  __TEXT.__objc_methlist: 0x1358c
+150.0.55.0.0
+  __TEXT.__text: 0x188cb8
+  __TEXT.__auth_stubs: 0x1520
+  __TEXT.__objc_stubs: 0x14ae0
+  __TEXT.__objc_methlist: 0x1351c
   __TEXT.__const: 0x10c8
   __TEXT.__swift5_typeref: 0x39e
   __TEXT.__swift5_reflstr: 0x288
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__constg_swiftt: 0x5c0
   __TEXT.__swift5_fieldmd: 0x354
-  __TEXT.__objc_methname: 0x1b8f6
-  __TEXT.__cstring: 0x1be6d
+  __TEXT.__objc_methname: 0x1b7b0
+  __TEXT.__cstring: 0x1bd01
   __TEXT.__swift5_proto: 0xb8
   __TEXT.__swift5_types: 0x50
   __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift5_protos: 0x4
   __TEXT.__objc_classname: 0x1892
-  __TEXT.__objc_methtype: 0x3d61
+  __TEXT.__objc_methtype: 0x3cfd
   __TEXT.__gcc_except_tab: 0x396c
-  __TEXT.__oslogstring: 0xdd38
+  __TEXT.__oslogstring: 0xd921
   __TEXT.__ustring: 0x58
   __TEXT.__info_plist: 0x6bf
-  __TEXT.__unwind_info: 0x4e18
+  __TEXT.__unwind_info: 0x4e00
   __TEXT.__eh_frame: 0x318
-  __DATA_CONST.__auth_got: 0xaa0
-  __DATA_CONST.__got: 0xa58
+  __DATA_CONST.__auth_got: 0xaa8
+  __DATA_CONST.__got: 0xa40
   __DATA_CONST.__auth_ptr: 0x1e0
   __DATA_CONST.__const: 0x5248
-  __DATA_CONST.__cfstring: 0x135c0
+  __DATA_CONST.__cfstring: 0x13400
   __DATA_CONST.__objc_classlist: 0x798
   __DATA_CONST.__objc_catlist: 0x200
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x968
-  __DATA_CONST.__objc_intobj: 0x3f0
+  __DATA_CONST.__objc_intobj: 0x330
   __DATA_CONST.__objc_arraydata: 0x130
   __DATA_CONST.__objc_arrayobj: 0x168
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x22668
-  __DATA.__objc_selrefs: 0x70c8
-  __DATA.__objc_ivar: 0x1300
+  __DATA.__objc_const: 0x225f8
+  __DATA.__objc_selrefs: 0x7088
+  __DATA.__objc_ivar: 0x12fc
   __DATA.__objc_data: 0x4ef8
   __DATA.__data: 0x14d8
   __DATA.__objc_stublist: 0x28

   - /System/Library/PrivateFrameworks/ApplePushService.framework/Versions/A/ApplePushService
   - /System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/Versions/A/BackgroundSystemTasks
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomePubSub.framework/Versions/A/BiomePubSub
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/CloudDocs.framework/Versions/A/CloudDocs

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8128
-  Symbols:   751
-  CStrings:  2734
+  Functions: 8119
+  Symbols:   749
+  CStrings:  2720
 
Symbols:
+ _BiomeLibrary
- _CLSUserSettingDateKey
- _CLSUserSettingEnabledKey
- _OBJC_CLASS_$_BMStreams
CStrings:
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/ClassKitSwift/progressd/UserNotifications/PDHandoutCompletedNotificationTrigger.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/ClassKitSwift/progressd/UserNotifications/PDRevisedSubmissionNotificationTrigger.m"
+ "/AppleInternal/Library/BuildRoots/0d0cb32e-3694-11ef-ba2c-e2437461156c/Library/Caches/com.apple.xbs/Sources/ClassKitSwift/progressd/UserNotifications/PDRevisionRequestedNotificationTrigger.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/ClassKitSwift/progressd/UserNotifications/PDHandoutCompletedNotificationTrigger.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/ClassKitSwift/progressd/UserNotifications/PDRevisedSubmissionNotificationTrigger.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/ClassKitSwift/progressd/UserNotifications/PDRevisionRequestedNotificationTrigger.m"
- "Fetch settings failed. Invalid notification type."
- "Fetch settings not allowed. Require dashboard entitlement."
- "Set settings failed. Invalid notification type."
- "Set settings not allowed. Require dashboard entitlement."
- "StuAttcUpdated"
- "StuHODueSoon"
- "StuHOPastDue"
- "StuHORevNeeded"
- "StuHandoutCompleted"
- "StuNewHO"
- "TeaHORevReviewDue"
- "TeaHOReviewDue"
- "UNSettingDate"
- "UNSettingDisabled"

```
