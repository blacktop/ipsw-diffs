## Accounts

> `/System/Library/Frameworks/Accounts.framework/Accounts`

```diff

-1014.0.0.0.0
-  __TEXT.__text: 0x5c7d4
+1016.0.0.0.0
+  __TEXT.__text: 0x5c968
   __TEXT.__auth_stubs: 0xc90
-  __TEXT.__objc_methlist: 0x42e4
+  __TEXT.__objc_methlist: 0x42ec
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x3ecc
-  __TEXT.__cstring: 0x3c7b
+  __TEXT.__gcc_except_tab: 0x3ee8
+  __TEXT.__cstring: 0x3ca9
   __TEXT.__oslogstring: 0x5245
-  __TEXT.__unwind_info: 0x1a78
+  __TEXT.__unwind_info: 0x1a80
   __TEXT.__objc_classname: 0x599
-  __TEXT.__objc_methname: 0x89ab
-  __TEXT.__objc_methtype: 0x150f
-  __TEXT.__objc_stubs: 0x6520
-  __DATA_CONST.__got: 0x338
+  __TEXT.__objc_methname: 0x8996
+  __TEXT.__objc_methtype: 0x1523
+  __TEXT.__objc_stubs: 0x6560
+  __DATA_CONST.__got: 0x340
   __DATA_CONST.__const: 0x2518
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x30

   __DATA_CONST.__objc_arraydata: 0x38
   __AUTH_CONST.__auth_got: 0x658
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x4860
-  __AUTH_CONST.__objc_const: 0x5e18
+  __AUTH_CONST.__cfstring: 0x4880
+  __AUTH_CONST.__objc_const: 0x5e60
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0x3dc
+  __DATA.__objc_ivar: 0x3e4
   __DATA.__data: 0x4d0
   __DATA.__bss: 0x109
   __DATA_DIRTY.__objc_data: 0x730

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 17372AD6-E5EF-33E7-AFBE-B852F8C4B8FC
-  Functions: 1958
-  Symbols:   6750
-  CStrings:  3426
+  UUID: B59E5F9C-3C35-39C3-9676-05E5C77A84E4
+  Functions: 1960
+  Symbols:   6761
+  CStrings:  3430
 
Symbols:
+ -[ACNotificationRebroadcaster .cxx_destruct]
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_IVAR_$_ACNotificationRebroadcaster._daemonAccountStoreDidChangeObserver
+ _OBJC_IVAR_$_ACNotificationRebroadcaster._queue
+ __OBJC_$_INSTANCE_VARIABLES_ACNotificationRebroadcaster
+ ___80-[ACNotificationRebroadcaster _beginObservingAccountStoreDidChangeNotifications]_block_invoke
+ _objc_msgSend$_accountStoreDidChange:
+ _objc_msgSend$setMaxConcurrentOperationCount:
+ _objc_msgSend$setName:
+ _objc_msgSend$setQualityOfService:
- _objc_msgSend$addObserver:selector:name:object:suspensionBehavior:
- _objc_msgSend$removeObserver:name:object:
Functions:
~ -[ACNotificationRebroadcaster init] : 84 -> 148
~ -[ACNotificationRebroadcaster _beginObservingAccountStoreDidChangeNotifications] : 128 -> 296
+ ___80-[ACNotificationRebroadcaster _beginObservingAccountStoreDidChangeNotifications]_block_invoke
~ -[ACNotificationRebroadcaster _endObservingAccountStoreDidChangeNotifications] : 116 -> 120
+ -[ACNotificationRebroadcaster .cxx_destruct]
CStrings:
+ "@\"NSOperationQueue\""
+ "_queue"
+ "com.apple.accounts.notification.rebroadcaster"
+ "setMaxConcurrentOperationCount:"
+ "setQualityOfService:"
- "addObserver:selector:name:object:suspensionBehavior:"
- "removeObserver:name:object:"

```
