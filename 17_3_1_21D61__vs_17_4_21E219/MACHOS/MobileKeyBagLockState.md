## MobileKeyBagLockState

> `/System/Library/UserEventPlugins/MobileKeyBagLockState.plugin/MobileKeyBagLockState`

```diff

-621.40.2.0.0
-  __TEXT.__text: 0x470
-  __TEXT.__auth_stubs: 0x100
-  __TEXT.__cstring: 0xc1
+625.100.7.0.0
+  __TEXT.__text: 0x4b0
+  __TEXT.__auth_stubs: 0x130
+  __TEXT.__cstring: 0xdb
   __TEXT.__oslogstring: 0x15e
-  __TEXT.__unwind_info: 0x58
-  __DATA.__auth_got: 0x80
+  __TEXT.__unwind_info: 0x50
+  __DATA.__auth_got: 0x98
   __DATA.__got: 0x28
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
-  UUID: 36CE8EC0-4E47-36D3-B7F4-3AB31CA06F03
+  UUID: B22C742B-6F03-387E-8791-E242AA3C75EE
   Functions: 3
-  Symbols:   24
-  CStrings:  13
+  Symbols:   27
+  CStrings:  14
 
Symbols:
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create_with_target$V2
CStrings:
+ "KeyBagLockState 2nd queue"

```
