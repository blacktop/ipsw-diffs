## appledepthd

> `/usr/libexec/appledepthd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-177.0.0.0.0
-  __TEXT.__text: 0x2950
-  __TEXT.__auth_stubs: 0x370
+179.0.0.0.0
+  __TEXT.__text: 0x28d4
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_stubs: 0x860
   __TEXT.__objc_methlist: 0x40c
-  __TEXT.__const: 0x88
+  __TEXT.__const: 0x90
   __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__cstring: 0x198
-  __TEXT.__oslogstring: 0x586
+  __TEXT.__cstring: 0x18e
+  __TEXT.__oslogstring: 0x576
   __TEXT.__objc_classname: 0xf6
   __TEXT.__objc_methname: 0xa2d
   __TEXT.__objc_methtype: 0x323

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__auth_got: 0x1d0
+  __DATA_CONST.__auth_got: 0x1c8
   __DATA_CONST.__got: 0x88
   __DATA.__objc_const: 0x828
   __DATA.__objc_selrefs: 0x318

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 55
-  Symbols:   81
-  CStrings:  219
+  Symbols:   80
+  CStrings:  218
 
Symbols:
- _proc_name
Functions:
~ sub_100001440 -> sub_100001490 : 2288 -> 2292
~ sub_10000323c -> sub_100003290 : 828 -> 700
CStrings:
+ "appledepthd accepted new XPC connection from pid=%d"
- "(unknown)"
- "appledepthd accepted new XPC connection from pid=%d name=%{public}s"
```
