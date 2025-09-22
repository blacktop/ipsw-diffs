## UserNotificationsServer

> `/System/Library/PrivateFrameworks/UserNotificationsServer.framework/UserNotificationsServer`

```diff

-640.0.0.0.0
-  __TEXT.__text: 0x38d6c
+640.1.9.100.0
+  __TEXT.__text: 0x39050
   __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_methlist: 0x22ac
+  __TEXT.__objc_methlist: 0x22c4
   __TEXT.__const: 0x2c4
-  __TEXT.__oslogstring: 0x625a
+  __TEXT.__oslogstring: 0x629a
   __TEXT.__cstring: 0x15a7
   __TEXT.__gcc_except_tab: 0x868
   __TEXT.__swift5_typeref: 0x38e

   __TEXT.__unwind_info: 0xd60
   __TEXT.__eh_frame: 0x248
   __TEXT.__objc_classname: 0x700
-  __TEXT.__objc_methname: 0xb284
+  __TEXT.__objc_methname: 0xb2ce
   __TEXT.__objc_methtype: 0x1a09
-  __TEXT.__objc_stubs: 0x9340
+  __TEXT.__objc_stubs: 0x9360
   __DATA_CONST.__got: 0x8a8
   __DATA_CONST.__const: 0x10f8
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29f0
+  __DATA_CONST.__objc_selrefs: 0x29f8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
   __AUTH_CONST.__auth_got: 0x890
   __AUTH_CONST.__const: 0x5d8
   __AUTH_CONST.__cfstring: 0xbc0
-  __AUTH_CONST.__objc_const: 0x5998
+  __AUTH_CONST.__objc_const: 0x59a0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0xd8
   __AUTH.__data: 0x98

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A19C3692-3611-3507-8FCA-70429350DFFF
-  Functions: 1043
-  Symbols:   4181
-  CStrings:  2290
+  UUID: 69732308-4006-33D8-BBC8-BF5209A4A111
+  Functions: 1045
+  Symbols:   4192
+  CStrings:  2292
 
Symbols:
+ -[UNSNotificationSettingsService revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]
+ -[UNSNotificationSettingsService revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:].cold.1
+ -[UNSNotificationSettingsService revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:].cold.2
+ -[UNSUserNotificationServerSettingsConnectionListener revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:]
+ GCC_except_table22
+ _objc_msgSend$revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:
CStrings:
+ "UNSNotificationSettingsService [%{public}@] Revoking Authorization"
+ "revokeAuthorizationForNotificationSourceIdentifier:withCompletionHandler:"

```
