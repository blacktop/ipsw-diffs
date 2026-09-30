## MobileKeyBagLockState

> `/System/Library/UserEventPlugins/MobileKeyBagLockState.plugin/MobileKeyBagLockState`

```diff

-640.120.2.0.0
-  __TEXT.__text: 0x4b4
-  __TEXT.__auth_stubs: 0x130
+674.0.0.0.0
+  __TEXT.__text: 0x444
+  __TEXT.__auth_stubs: 0x120
   __TEXT.__const: 0x10
   __TEXT.__cstring: 0xdb
-  __TEXT.__oslogstring: 0x15e
+  __TEXT.__oslogstring: 0x12e
   __TEXT.__unwind_info: 0x60
-  __DATA.__auth_got: 0x98
+  __DATA.__auth_got: 0x90
   __DATA.__got: 0x28
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
-  UUID: C278ECF6-A8C9-35A4-AFAA-BBF983FA04D4
+  UUID: 1F065101-4E36-3A92-BEFD-22B079C253D2
   Functions: 3
-  Symbols:   27
+  Symbols:   26
   CStrings:  14
 
Symbols:
- _aks_get_extended_device_state
Functions:
~ sub_698 : 600 -> 488
CStrings:
+ " LockStateNotifier %s posted notification: %s (handle: %d)\n"
+ " LockStateNotifier %s posting notification: %s (handle: %d)\n"
+ "MKBPLUGINSTART: LockStateNotifier %s posting notification: %s (handle: %d)\n"
- " LockStateNotifier %s posted notification: %s (handle: %d, lock state: %d)\n"
- " LockStateNotifier %s posting notification: %s (handle: %d, lock state: %d)\n"
- "MKBPLUGINSTART: LockStateNotifier %s posting notification: %s (handle: %d, lock state: %d)\n"

```
