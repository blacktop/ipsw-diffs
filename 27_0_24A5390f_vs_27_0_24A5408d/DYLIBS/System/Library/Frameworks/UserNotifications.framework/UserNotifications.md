## UserNotifications

> `/System/Library/Frameworks/UserNotifications.framework/UserNotifications`

```diff

-717.0.0.0.0
-  __TEXT.__text: 0x2f710
-  __TEXT.__objc_methlist: 0x37d8
+720.0.0.0.0
+  __TEXT.__text: 0x2f830
+  __TEXT.__objc_methlist: 0x37f8
   __TEXT.__cstring: 0x3661
   __TEXT.__const: 0xd0
   __TEXT.__gcc_except_tab: 0x224
   __TEXT.__oslogstring: 0x2118
   __TEXT.__dlopen_cstrs: 0x8a
-  __TEXT.__unwind_info: 0xd78
+  __TEXT.__unwind_info: 0xd80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c90
+  __DATA_CONST.__objc_selrefs: 0x1ca8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__got: 0x3b8
   __AUTH_CONST.__const: 0x3a0
   __AUTH_CONST.__cfstring: 0x35a0
-  __AUTH_CONST.__objc_const: 0xa7a8
+  __AUTH_CONST.__objc_const: 0xa7d8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x354
+  __DATA.__objc_ivar: 0x358
   __DATA.__data: 0x848
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0xa00

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1365
-  Symbols:   2975
+  Functions: 1369
+  Symbols:   2981
   CStrings:  646
 
Symbols:
+ -[UNUserNotificationServiceConnection serverReconnectAttempts]
+ -[UNUserNotificationServiceConnection setHandlesNotificationResponses:forBundleIdentifier:]
+ -[UNUserNotificationServiceConnection setServerReconnectAttempts:]
+ GCC_except_table180
+ _OBJC_IVAR_$_UNUserNotificationServiceConnection._serverReconnectAttempts
+ ___91-[UNUserNotificationServiceConnection setHandlesNotificationResponses:forBundleIdentifier:]_block_invoke
+ _objc_msgSend$setHandlesNotificationResponses:forBundleIdentifier:
- GCC_except_table178
```
