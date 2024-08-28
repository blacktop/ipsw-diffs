## BTLEServer

> `/usr/sbin/BTLEServer`

```diff

-340.48.0.0.0
-  __TEXT.__text: 0x7346c
-  __TEXT.__auth_stubs: 0x1060
-  __TEXT.__objc_stubs: 0xbf80
-  __TEXT.__objc_methlist: 0x6428
+341.1.0.0.0
+  __TEXT.__text: 0x7320c
+  __TEXT.__auth_stubs: 0x1080
+  __TEXT.__objc_stubs: 0xbf60
+  __TEXT.__objc_methlist: 0x6420
   __TEXT.__const: 0x508
   __TEXT.__cstring: 0x313e
-  __TEXT.__objc_methname: 0x10feb
-  __TEXT.__oslogstring: 0xb41c
+  __TEXT.__objc_methname: 0x10fd3
+  __TEXT.__oslogstring: 0xb449
   __TEXT.__objc_classname: 0x7f0
   __TEXT.__objc_methtype: 0x2d86
-  __TEXT.__gcc_except_tab: 0x10e0
+  __TEXT.__gcc_except_tab: 0xe00
   __TEXT.__dlopen_cstrs: 0x13e
   __TEXT.__ustring: 0xc6
-  __TEXT.__unwind_info: 0x1798
-  __DATA_CONST.__auth_got: 0x840
+  __TEXT.__unwind_info: 0x1760
+  __DATA_CONST.__auth_got: 0x850
   __DATA_CONST.__got: 0x8a8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x15a0

   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xee80
-  __DATA.__objc_selrefs: 0x3948
+  __DATA.__objc_selrefs: 0x3940
   __DATA.__objc_ivar: 0x758
   __DATA.__objc_data: 0x1860
   __DATA.__data: 0x848
-  __DATA.__bss: 0x1a0
+  __DATA.__bss: 0x1a8
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2731
-  Symbols:   542
+  Symbols:   544
   CStrings:  4735
 
Symbols:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "No XPC Connection to send Check-In reply msg"
- "sendMsg:args:forClient:"

```
