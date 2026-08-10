## ClipServices

> `/System/Library/PrivateFrameworks/ClipServices.framework/ClipServices`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1038.8.1.0.0
-  __TEXT.__text: 0x3839c
-  __TEXT.__objc_methlist: 0x322c
+1038.10.0.0.0
+  __TEXT.__text: 0x384b0
+  __TEXT.__objc_methlist: 0x323c
   __TEXT.__gcc_except_tab: 0xa6c
   __TEXT.__cstring: 0x3f4a
   __TEXT.__const: 0x110
   __TEXT.__oslogstring: 0x480d
   __TEXT.__dlopen_cstrs: 0x2e4
-  __TEXT.__unwind_info: 0x10d0
+  __TEXT.__unwind_info: 0x10d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2500
+  __DATA_CONST.__objc_selrefs: 0x2508
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x4d0
   __AUTH_CONST.__const: 0x620
   __AUTH_CONST.__cfstring: 0x34a0
-  __AUTH_CONST.__objc_const: 0x5128
+  __AUTH_CONST.__objc_const: 0x5138
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1487
-  Symbols:   3402
+  Functions: 1489
+  Symbols:   3405
   CStrings:  832
 
Symbols:
+ -[CPSSession metadataSnapshot]
+ GCC_except_table79
+ ___30-[CPSSession metadataSnapshot]_block_invoke
+ _objc_msgSend$metadataSnapshot
- GCC_except_table77
```
