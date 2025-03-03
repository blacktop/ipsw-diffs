## sysdiagnose

> `/usr/bin/sysdiagnose`

```diff

-1438.80.3.0.0
-  __TEXT.__text: 0x43e8
+1438.100.39.0.0
+  __TEXT.__text: 0x4424
   __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_stubs: 0x820
   __TEXT.__objc_methlist: 0xac
-  __TEXT.__const: 0x80
+  __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x78
   __TEXT.__cstring: 0x234c
   __TEXT.__oslogstring: 0x6c6
   __TEXT.__objc_methname: 0x5d9
   __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x5b
-  __TEXT.__unwind_info: 0x158
+  __TEXT.__unwind_info: 0x168
   __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0x140
   __DATA_CONST.__auth_ptr: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 73
+  Functions: 81
   Symbols:   151
   CStrings:  236
 
CStrings:
+ "assertion failure: \"name\" -> %llu"
- "assertion failure: \"name\" -> %lld"

```
