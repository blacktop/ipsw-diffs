## spctl

> `/usr/sbin/spctl`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_security_`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_dupclass`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-823.1.1.0.0
-  __TEXT.__text: 0xc350
+823.40.10.0.0
+  __TEXT.__text: 0xc470
   __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_stubs: 0x10a0
+  __TEXT.__objc_stubs: 0x10e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x8e8
-  __TEXT.__const: 0x518
+  __TEXT.__const: 0x520
   __TEXT.__cstring: 0x1ac6
   __TEXT.__oslogstring: 0x8f3
   __TEXT.__objc_classname: 0x107
-  __TEXT.__objc_methname: 0x1a5d
+  __TEXT.__objc_methname: 0x1a92
   __TEXT.__objc_methtype: 0x8f5
   __TEXT.__gcc_except_tab: 0x5fc
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__dof_security_: 0x28e
-  __TEXT.__unwind_info: 0x678
+  __TEXT.__unwind_info: 0x680
   __DATA_CONST.__const: 0xc88
   __DATA_CONST.__cfstring: 0xda0
   __DATA_CONST.__objc_classlist: 0x68

   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0xf28
-  __DATA.__objc_selrefs: 0x680
+  __DATA.__objc_selrefs: 0x690
   __DATA.__objc_ivar: 0x74
   __DATA.__objc_data: 0x410
   __DATA.__data: 0x188

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 363
+  Functions: 364
   Symbols:   262
-  CStrings:  695
+  CStrings:  697
 
CStrings:
+ "URLByStandardizingPath"
+ "objectAtIndexedSubscript:"
+ "pathComponents"
- "hasPrefix:"
```
