## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-634.0.0.0.0
-  __TEXT.__text: 0x38b18
+640.0.0.0.0
+  __TEXT.__text: 0x38d50
   __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x2294
+  __TEXT.__objc_methlist: 0x22ac
   __TEXT.__const: 0x2c4
   __TEXT.__oslogstring: 0x625a
-  __TEXT.__cstring: 0x1587
+  __TEXT.__cstring: 0x15a7
   __TEXT.__gcc_except_tab: 0x868
   __TEXT.__swift5_typeref: 0x38e
   __TEXT.__swift5_fieldmd: 0x9c

   __TEXT.__unwind_info: 0xd60
   __TEXT.__eh_frame: 0x248
   __TEXT.__objc_classname: 0x700
-  __TEXT.__objc_methname: 0xb1ff
+  __TEXT.__objc_methname: 0xb284
   __TEXT.__objc_methtype: 0x1a09
-  __TEXT.__objc_stubs: 0x92c0
-  __DATA_CONST.__got: 0x898
+  __TEXT.__objc_stubs: 0x9340
+  __DATA_CONST.__got: 0x8a8
   __DATA_CONST.__const: 0x10f8
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29d0
+  __DATA_CONST.__objc_selrefs: 0x29f0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /System/Library/PrivateFrameworks/UserNotificationsCore.framework/UserNotificationsCore
+  - /System/Library/PrivateFrameworks/UserNotificationsKit.framework/UserNotificationsKit
   - /System/Library/PrivateFrameworks/UserNotificationsServices.framework/UserNotificationsServices
   - /System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings
   - /System/Library/PrivateFrameworks/UserNotificationsTranslation.framework/UserNotificationsTranslation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EF9997B6-2E13-30F5-AC77-4DB7EE40729F
-  Functions: 1041
-  Symbols:   4171
-  CStrings:  2284
+  UUID: 64F86388-8C5E-3B83-8B9C-B98E212F5BA1
+  Functions: 1043
+  Symbols:   4181
+  CStrings:  2290
 
Symbols:
+ -[UNSDefaultDataProvider _sectionIconVariantForApplicationIdentifier:format:]
+ -[UNSDefaultDataProvider _sectionIconVariantForUTI:format:]
+ GCC_except_table111
+ GCC_except_table112
+ _OBJC_CLASS_$_UNNotificationOnboardingDefaults
+ _UNNotificationSourceFilterEnabled
+ ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke.78
+ ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke.80
+ ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke_2.82
+ ___78-[UNSUserNotificationServer performAction:forNotification:inApp:withUserText:]_block_invoke.85.cold.1
+ ___78-[UNSUserNotificationServer performAction:forNotification:inApp:withUserText:]_block_invoke.86
+ ___block_literal_global.108
+ ___block_literal_global.340
+ ___block_literal_global.69
+ ___block_literal_global.73
+ ___block_literal_global.75
+ _objc_msgSend$_sectionIconVariantForApplicationIdentifier:format:
+ _objc_msgSend$_sectionIconVariantForUTI:format:
+ _objc_msgSend$allowsNotifications
+ _objc_msgSend$applyToSettingsIfNecessary
- GCC_except_table109
- GCC_except_table110
- ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke.77
- ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke.79
- ___76-[UNSUserNotificationServer _buildForegroundAction:queue:completionHandler:]_block_invoke_2.81
- ___78-[UNSUserNotificationServer performAction:forNotification:inApp:withUserText:]_block_invoke.84
- ___78-[UNSUserNotificationServer performAction:forNotification:inApp:withUserText:]_block_invoke.84.cold.1
- ___block_literal_global.107
- ___block_literal_global.339
- ___block_literal_global.68
- ___block_literal_global.72
- ___block_literal_global.74
CStrings:
+ "?"
+ "@\"OS_dispatch_queue\""
+ "_sectionIconVariantForApplicationIdentifier:format:"
+ "_sectionIconVariantForUTI:format:"
+ "allowsNotifications"
+ "applyToSettingsIfNecessary"

```
