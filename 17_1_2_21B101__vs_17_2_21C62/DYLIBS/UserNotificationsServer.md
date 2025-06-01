## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-491.2.1.0.0
-  __TEXT.__text: 0x56fbc
+491.8.0.0.0
+  __TEXT.__text: 0x57330
   __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x45fc
-  __TEXT.__cstring: 0x4726
-  __TEXT.__oslogstring: 0x6fad
+  __TEXT.__objc_methlist: 0x462c
+  __TEXT.__cstring: 0x4735
+  __TEXT.__oslogstring: 0x6fde
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x488
-  __TEXT.__unwind_info: 0x128c
+  __TEXT.__unwind_info: 0x1294
   __TEXT.__objc_classname: 0xae6
-  __TEXT.__objc_methname: 0x12f6e
-  __TEXT.__objc_methtype: 0x1f30
-  __TEXT.__objc_stubs: 0xd6e0
+  __TEXT.__objc_methname: 0x1305e
+  __TEXT.__objc_methtype: 0x1f33
+  __TEXT.__objc_stubs: 0xd840
   __DATA_CONST.__got: 0x340
   __DATA_CONST.__const: 0x1828
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xb470
-  __DATA_CONST.__objc_selrefs: 0x38f0
-  __AUTH_CONST.__cfstring: 0x4620
+  __DATA_CONST.__objc_const: 0xb4a0
+  __DATA_CONST.__objc_selrefs: 0x3948
+  __AUTH_CONST.__cfstring: 0x4640
   __AUTH_CONST.__objc_const: 0x13e8
   __AUTH_CONST.__const: 0x760
   __AUTH_CONST.__objc_intobj: 0x60

   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x568
   __DATA.__objc_superrefs: 0x168
-  __DATA.__objc_ivar: 0x760
+  __DATA.__objc_ivar: 0x764
   __DATA.__data: 0xc98
   __DATA.__bss: 0x1
   __DATA_DIRTY.__objc_data: 0x1090

   - /System/Library/PrivateFrameworks/UserNotificationsSettings.framework/UserNotificationsSettings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8A70AACB-4C65-3A5A-9520-599DA10BAA54
-  Functions: 1990
-  Symbols:   7490
-  CStrings:  4522
+  UUID: 9DA994DE-0F78-3400-8871-3FDB2418954C
+  Functions: 1994
+  Symbols:   7510
+  CStrings:  4537
 
Symbols:
+ +[UNNotificationAttachment(Staging) stagingActionForFileHandle:fromLocalClientConnection:orFromServiceExtensionOfBundleProxy:servicingBundleIdentifier:error:]
+ +[UNNotificationAttachment(Staging) stagingActionForFileHandle:fromLocalClientConnection:orFromServiceExtensionOfBundleProxy:servicingBundleIdentifier:error:].cold.1
+ -[BBSectionInfo(UserNotificationsServer) uns_bundlePath]
+ -[BBSectionInfo(UserNotificationsServer) uns_settingsIcon]
+ -[UNSNotificationRecord setSpeechLanguage:]
+ -[UNSNotificationRecord speechLanguage]
+ _OBJC_IVAR_$_UNSNotificationRecord._speechLanguage
+ ___block_literal_global.1135
+ ___block_literal_global.1138
+ ___block_literal_global.1180
+ _objc_msgSend$_bestVariantForFormat:
+ _objc_msgSend$iconAtPath:
+ _objc_msgSend$iconData
+ _objc_msgSend$iconNamed:
+ _objc_msgSend$iconWithData:
+ _objc_msgSend$imageData
+ _objc_msgSend$imagePath
+ _objc_msgSend$initWithIdentifier:isHidden:displayName:icon:settings:bundlePath:
+ _objc_msgSend$setSpeechLanguage:
+ _objc_msgSend$speechLanguage
+ _objc_msgSend$stagingActionForFileHandle:fromLocalClientConnection:orFromServiceExtensionOfBundleProxy:servicingBundleIdentifier:error:
+ _objc_msgSend$uns_bundlePath
+ _objc_msgSend$uns_settingsIcon
- +[UNNotificationAttachment(Staging) stagingActionForFileHandle:fromLocalClientConnection:orFromServiceExtensionOfBundleProxy:error:]
- +[UNNotificationAttachment(Staging) stagingActionForFileHandle:fromLocalClientConnection:orFromServiceExtensionOfBundleProxy:error:].cold.1
- ___block_literal_global.1127
- ___block_literal_global.1130
- ___block_literal_global.1172
- _objc_msgSend$initWithIdentifier:isHidden:displayName:icon:settings:
- _objc_msgSend$stagingActionForFileHandle:fromLocalClientConnection:orFromServiceExtensionOfBundleProxy:error:
CStrings:
+ "Q56@0:8@16@24@32@40^@48"
+ "SpeechLanguage"
+ "T@\"NSString\",C,N,V_speechLanguage"
+ "Y,\x1f\x03\x12\x16\x11\x12\x13\x14\x11\x15\x12"
+ "[Notification Service Extension] Copying not moving attachment to prevent system process from effectively deleting this file it doesn't have access to. Push notification service connection '%{public}@'. Notification service extension for bundle: '%{public}@', Attachment: '%{public}@', Effective Notifications Bundle ID: '%{public}@'"
+ "_bestVariantForFormat:"
+ "_speechLanguage"
+ "iconAtPath:"
+ "iconData"
+ "iconNamed:"
+ "iconWithData:"
+ "imageData"
+ "imagePath"
+ "initWithIdentifier:isHidden:displayName:icon:settings:bundlePath:"
+ "setSpeechLanguage:"
+ "speechLanguage"
+ "stagingActionForFileHandle:fromLocalClientConnection:orFromServiceExtensionOfBundleProxy:servicingBundleIdentifier:error:"
+ "uns_bundlePath"
+ "uns_settingsIcon"
- "Q48@0:8@16@24@32^@40"
- "Y,\x1f\x03\x12\x16\x11\x12\x13\x14\x11\x15\x11"
- "[Notification Service Extension] Copying not moving attachment to prevent system process from effectively deleting this file it doesn't have access to. Push notification service connection '%{public}@'. Notification service extension for bundle: '%{public}@', Attachment: '%{public}@'"
- "initWithIdentifier:isHidden:displayName:icon:settings:"
- "stagingActionForFileHandle:fromLocalClientConnection:orFromServiceExtensionOfBundleProxy:error:"

```
