## acdiagnose

> `/System/Library/Frameworks/Accounts.framework/Support/acdiagnose`

```diff

-999.4.0.0.0
-  __TEXT.__text: 0xb38
-  __TEXT.__auth_stubs: 0x220
+1014.0.0.0.0
+  __TEXT.__text: 0xb64
+  __TEXT.__auth_stubs: 0x230
   __TEXT.__objc_stubs: 0x3a0
   __TEXT.__const: 0x8
   __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__cstring: 0x25b
+  __TEXT.__cstring: 0x260
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x1c9
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x120
+  __DATA_CONST.__auth_got: 0x128
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x20

   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA74F6E4-3AF0-3F4C-B89F-4E16326F821E
+  UUID: 724304C3-C2D4-3296-B14D-FBB73DD0580A
   Functions: 3
-  Symbols:   48
+  Symbols:   49
   CStrings:  72
 
Symbols:
+ _ACHashedString
+ _objc_retain_x22
- _objc_retain_x24
Functions:
~ sub_1000012ac : 580 -> 624
CStrings:
+ "%s%@(%@) %@ (%@) %@"
- "%s%@(%@) %@ %@"

```
