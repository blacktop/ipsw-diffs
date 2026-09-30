## UserNotifications

> `/System/Library/Frameworks/UserNotifications.framework/Versions/A/UserNotifications`

```diff

-717.0.0.0.0
-  __TEXT.__text: 0x32e1c
-  __TEXT.__objc_methlist: 0x3858
+720.0.1.0.0
+  __TEXT.__text: 0x336dc
+  __TEXT.__objc_methlist: 0x38e8
   __TEXT.__cstring: 0x368c
-  __TEXT.__const: 0xd8
+  __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0x224
   __TEXT.__oslogstring: 0x207a
   __TEXT.__dlopen_cstrs: 0x8a
-  __TEXT.__unwind_info: 0xd20
+  __TEXT.__unwind_info: 0xd30
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cb8
+  __DATA_CONST.__objc_selrefs: 0x1d00
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__got: 0x3b8
   __AUTH_CONST.__const: 0xbd0
   __AUTH_CONST.__cfstring: 0x35a0
-  __AUTH_CONST.__objc_const: 0xa808
+  __AUTH_CONST.__objc_const: 0xa870
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x354
+  __DATA.__objc_ivar: 0x358
   __DATA.__data: 0x848
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0xa00

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1391
-  Symbols:   3043
+  Functions: 1403
+  Symbols:   3067
   CStrings:  644
 
Symbols:
+ -[UNUserNotificationCenter handlesNotificationResponses]
+ -[UNUserNotificationCenter hasNotificationDelegate]
+ -[UNUserNotificationServiceConnection _queue_handlesNotificationResponsesForBundleIdentifier:]
+ -[UNUserNotificationServiceConnection _queue_reestablishResponseObserversIfNeeded]
+ -[UNUserNotificationServiceConnection _queue_updateHandlesNotificationResponsesForBundleIdentifier:]
+ -[UNUserNotificationServiceConnection serverReconnectAttempts]
+ -[UNUserNotificationServiceConnection setHandlesNotificationResponses:forBundleIdentifier:]
+ -[UNUserNotificationServiceConnection setServerReconnectAttempts:]
+ -[UNUserNotificationServiceConnection updateHandlesNotificationResponsesForBundleIdentifier:]
+ GCC_except_table203
+ OBJC_IVAR_$_UNUserNotificationServiceConnection._serverReconnectAttempts
+ ___67-[UNUserNotificationServiceConnection _queue_interruptedConnection]_block_invoke
+ ___91-[UNUserNotificationServiceConnection setHandlesNotificationResponses:forBundleIdentifier:]_block_invoke
+ ___93-[UNUserNotificationServiceConnection updateHandlesNotificationResponsesForBundleIdentifier:]_block_invoke
+ _dispatch_after
+ _objc_msgSend$_queue_handlesNotificationResponsesForBundleIdentifier:
+ _objc_msgSend$_queue_reestablishResponseObserversIfNeeded
+ _objc_msgSend$_queue_updateHandlesNotificationResponsesForBundleIdentifier:
+ _objc_msgSend$delegate
+ _objc_msgSend$handlesNotificationResponses
+ _objc_msgSend$hasNotificationDelegate
+ _objc_msgSend$setHandlesNotificationResponses:forBundleIdentifier:
+ _objc_msgSend$updateHandlesNotificationResponsesForBundleIdentifier:
+ _objc_sync_enter
+ _objc_sync_exit
- GCC_except_table199
```
