## acdiagnose

> `/System/Library/Frameworks/Accounts.framework/Support/acdiagnose`

```diff

-1025.0.0.0.0
-  __TEXT.__text: 0xb64
-  __TEXT.__auth_stubs: 0x230
+1034.0.0.0.0
+  __TEXT.__text: 0xbf4
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x3a0
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0x134
+  __TEXT.__gcc_except_tab: 0x128
   __TEXT.__cstring: 0x260
   __TEXT.__objc_classname: 0x1
   __TEXT.__objc_methname: 0x1c9
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x128
+  __DATA_CONST.__auth_got: 0x110
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x20

   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6E815CDA-9B33-305C-9743-ED8A3F81BA7F
+  UUID: D145E04B-AE1B-3175-AEE5-FF67F4DA6244
   Functions: 3
-  Symbols:   49
+  Symbols:   46
   CStrings:  72
 
Symbols:
+ _objc_retain_x19
+ _objc_retain_x24
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x22
- _objc_retain_x8
Functions:
~ sub_1000009b8 : 2156 -> 2264
~ sub_1000012ac -> sub_100001318 : 624 -> 660

```
