## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-640.5.31.0.0
-  __TEXT.__text: 0x3afd4
+640.5.32.103.0
+  __TEXT.__text: 0x3b100
   __TEXT.__auth_stubs: 0x10d0
-  __TEXT.__objc_methlist: 0x231c
+  __TEXT.__objc_methlist: 0x232c
   __TEXT.__const: 0x394
-  __TEXT.__oslogstring: 0x646a
-  __TEXT.__cstring: 0x1322
+  __TEXT.__oslogstring: 0x64ba
+  __TEXT.__cstring: 0x1342
   __TEXT.__gcc_except_tab: 0x844
   __TEXT.__swift5_typeref: 0x38e
   __TEXT.__swift5_fieldmd: 0x9c

   __TEXT.__unwind_info: 0xd98
   __TEXT.__eh_frame: 0x250
   __TEXT.__objc_classname: 0x947
-  __TEXT.__objc_methname: 0xb6b9
+  __TEXT.__objc_methname: 0xb6e9
   __TEXT.__objc_methtype: 0x1b54
-  __TEXT.__objc_stubs: 0x9680
-  __DATA_CONST.__got: 0x8d8
+  __TEXT.__objc_stubs: 0x96a0
+  __DATA_CONST.__got: 0x8e0
   __DATA_CONST.__const: 0x1188
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a60
+  __DATA_CONST.__objc_selrefs: 0x2a68
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x878
   __AUTH_CONST.__const: 0x5d8
-  __AUTH_CONST.__cfstring: 0xdc0
+  __AUTH_CONST.__cfstring: 0xde0
   __AUTH_CONST.__objc_const: 0x59e0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 775F1A35-2234-343F-B454-C6A01B215DF9
-  Functions: 1068
-  Symbols:   4307
-  CStrings:  2342
+  UUID: 474B5079-0F44-3BCE-8311-DC739CEB74E3
+  Functions: 1070
+  Symbols:   4317
+  CStrings:  2346
 
Symbols:
+ -[UNSNotificationSettingsService _shouldIncludeSectionInfo:forFilter:]
+ -[UNSNotificationSettingsService _shouldIncludeSectionInfo:forFilter:].cold.1
+ -[UNSNotificationSettingsService _shouldIncludeSectionInfo:forFilter:].cold.2
+ GCC_except_table28
+ _OBJC_CLASS_$_UNCSpotlightUninstallHelper
+ ___63-[UNSDefaultDataProvider _queue_modifyBulletinForNotification:]_block_invoke.91
+ ___73-[UNSDefaultDataProvider _queue_addBulletinForNotification:shouldRepost:]_block_invoke.93
+ ___76-[UNSDefaultDataProvider _queue_withdrawBulletinForNotification:shouldSync:]_block_invoke.94
+ ___block_literal_global.16
+ ___block_literal_global.97
+ _objc_msgSend$_shouldIncludeSectionInfo:forFilter:
+ _objc_msgSend$removeAllForBundleIdentifier:
- -[UNSNotificationSettingsService notificationSourcesWithFilter:].cold.1
- ___63-[UNSDefaultDataProvider _queue_modifyBulletinForNotification:]_block_invoke.90
- ___73-[UNSDefaultDataProvider _queue_addBulletinForNotification:shouldRepost:]_block_invoke.92
- ___76-[UNSDefaultDataProvider _queue_withdrawBulletinForNotification:shouldSync:]_block_invoke.93
- ___block_literal_global.15
- ___block_literal_global.96
- _objc_msgSend$initWithArray:
Functions:
~ _OUTLINED_FUNCTION_3 : 28 -> 20
+ _OUTLINED_FUNCTION_4
~ -[UNSNotificationSettingsService notificationSourcesWithFilter:] : 1380 -> 724
+ -[UNSNotificationSettingsService _shouldIncludeSectionInfo:forFilter:]
~ -[UNSDefaultDataProvider uninstall] : 100 -> 152
~ __IsTelephonyDevice.cold.1 : 20 -> 4
- -[UNSNotificationSettingsService notificationSourcesWithFilter:].cold.1
+ -[UNSNotificationSettingsService _shouldIncludeSectionInfo:forFilter:].cold.2
CStrings:
+ "UNSNotificationSettingsService [%{public}@] Unknown filter type: '%{public}@'"
+ "_shouldIncludeSectionInfo:forFilter:"
+ "com.apple.mobiletimer"
+ "removeAllForBundleIdentifier:"
- "initWithArray:"

```
