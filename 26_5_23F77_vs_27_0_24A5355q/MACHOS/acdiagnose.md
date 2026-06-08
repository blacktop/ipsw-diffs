## acdiagnose

> `/System/Library/Frameworks/Accounts.framework/Support/acdiagnose`

```diff

-1036.0.0.0.0
-  __TEXT.__text: 0xbf4
-  __TEXT.__auth_stubs: 0x200
+1116.0.0.0.0
+  __TEXT.__text: 0xbc4
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__objc_stubs: 0x3a0
   __TEXT.__const: 0x8
-  __TEXT.__gcc_except_tab: 0x128
-  __TEXT.__cstring: 0x260
-  __TEXT.__objc_classname: 0x1
+  __TEXT.__gcc_except_tab: 0x134
+  __TEXT.__cstring: 0x26f
   __TEXT.__objc_methname: 0x1c9
   __TEXT.__unwind_info: 0x70
-  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__const: 0x20
+  __DATA_CONST.__cfstring: 0x2c0
+  __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x20
-  __DATA_CONST.__cfstring: 0x2a0
-  __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0xe8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AccountsDaemon.framework/AccountsDaemon
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3E3A2DE9-0330-3956-B581-1E9B86947E0E
+  UUID: E1D9C1BF-3D7B-340A-A6F9-0042D81B1D4C
   Functions: 3
-  Symbols:   46
-  CStrings:  72
+  Symbols:   50
+  CStrings:  74
 
Symbols:
+ _ACIsInternal
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x22
+ _objc_retain_x8
- _objc_retain_x19
- _objc_retain_x24
Functions:
~ sub_1000009b8 -> sub_100000968 : 2264 -> 2168
~ sub_100001318 -> sub_100001268 : 660 -> 708
CStrings:
+ "%s%@(%@) %@ %@"

```
