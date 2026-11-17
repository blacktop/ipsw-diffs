## sysdiagnosed

> `/usr/libexec/sysdiagnosed`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1598.60.5.0.0
-  __TEXT.__text: 0x602f4
+1598.60.7.0.0
+  __TEXT.__text: 0x603ec
   __TEXT.__auth_stubs: 0x1700
-  __TEXT.__objc_stubs: 0x9420
+  __TEXT.__objc_stubs: 0x9440
   __TEXT.__objc_methlist: 0x3f74
   __TEXT.__const: 0x1d4
-  __TEXT.__cstring: 0x10dcd
+  __TEXT.__cstring: 0x10dcc
   __TEXT.__objc_classname: 0x38b
   __TEXT.__objc_methtype: 0x183c
   __TEXT.__gcc_except_tab: 0xda8
-  __TEXT.__objc_methname: 0xa7b4
+  __TEXT.__objc_methname: 0xa7d1
   __TEXT.__oslogstring: 0x8177
   __TEXT.__ustring: 0x4e8
   __TEXT.__unwind_info: 0x1638
   __DATA_CONST.__const: 0x13e0
-  __DATA_CONST.__cfstring: 0x11880
+  __DATA_CONST.__cfstring: 0x118e0
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x90
-  __DATA_CONST.__objc_arraydata: 0xec0
+  __DATA_CONST.__objc_arraydata: 0xed0
   __DATA_CONST.__objc_arrayobj: 0x1428
   __DATA_CONST.__objc_intobj: 0x300
   __DATA_CONST.__objc_floatobj: 0x10

   __DATA_CONST.__got: 0x468
   __DATA_CONST.__auth_ptr: 0x60
   __DATA.__objc_const: 0x53b8
-  __DATA.__objc_selrefs: 0x2a08
+  __DATA.__objc_selrefs: 0x2a10
   __DATA.__objc_ivar: 0x478
   __DATA.__objc_data: 0xbe0
   __DATA.__data: 0x3a0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 1779
+  Functions: 1780
   Symbols:   505
-  CStrings:  4880
+  CStrings:  4884
 
CStrings:
+ "--output"
+ "/.nofollow"
+ "/.nofollow/"
+ "/.resolve/"
+ "rangeOfString:options:range:"
- "/private/var/mobile/tmp/com.apple.audiomxd/"
```
