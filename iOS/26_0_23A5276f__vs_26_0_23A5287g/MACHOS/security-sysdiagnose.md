## security-sysdiagnose

> `/usr/libexec/security-sysdiagnose`

```diff

-61901.0.33.0.2
-  __TEXT.__text: 0x381c
-  __TEXT.__auth_stubs: 0x7e0
+61901.0.46.502.1
+  __TEXT.__text: 0x37d8
+  __TEXT.__auth_stubs: 0x7d0
   __TEXT.__objc_stubs: 0x500
   __TEXT.__objc_methlist: 0xd0
   __TEXT.__const: 0x70

   __TEXT.__objc_classname: 0x3d
   __TEXT.__objc_methname: 0x3f8
   __TEXT.__objc_methtype: 0x17e
-  __TEXT.__cstring: 0xd90
+  __TEXT.__cstring: 0xd62
   __TEXT.__oslogstring: 0xa8
   __TEXT.__unwind_info: 0xf0
-  __DATA_CONST.__auth_got: 0x400
+  __DATA_CONST.__auth_got: 0x3f8
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x310
-  __DATA_CONST.__cfstring: 0xa80
+  __DATA_CONST.__cfstring: 0xa60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A6D9B88D-134F-36D2-AC3C-988655AB263A
+  UUID: 08A2448A-10F6-3FE7-889C-C90A15A58E60
   Functions: 32
-  Symbols:   173
-  CStrings:  276
+  Symbols:   172
+  CStrings:  274
 
Symbols:
- _NSLog
Functions:
~ sub_100000d98 : 748 -> 724
~ sub_10000135c -> sub_100001344 : 5828 -> 5784
CStrings:
- "Failed to fetch DB path with status error: %@"

```
