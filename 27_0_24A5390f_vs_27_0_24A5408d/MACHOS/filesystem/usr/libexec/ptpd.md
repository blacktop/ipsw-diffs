## ptpd

> `/usr/libexec/ptpd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2116.0.0.0.0
-  __TEXT.__text: 0x22818
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_stubs: 0x41a0
+2118.0.0.0.0
+  __TEXT.__text: 0x22918
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_stubs: 0x41c0
   __TEXT.__objc_methlist: 0x1a80
   __TEXT.__const: 0x4c
   __TEXT.__gcc_except_tab: 0x45c
   __TEXT.__cstring: 0x259a
-  __TEXT.__objc_methname: 0x4f63
+  __TEXT.__objc_methname: 0x4f70
   __TEXT.__oslogstring: 0x3f
   __TEXT.__ustring: 0xc32
   __TEXT.__objc_classname: 0xef

   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA_CONST.__auth_got: 0x510
-  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__auth_got: 0x518
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x26c8
-  __DATA.__objc_selrefs: 0x1628
+  __DATA.__objc_selrefs: 0x1630
   __DATA.__objc_ivar: 0x284
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x1b0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 615
-  Symbols:   238
-  CStrings:  1588
+  Functions: 616
+  Symbols:   240
+  CStrings:  1589
 
Symbols:
+ _OBJC_CLASS_$_NSThread
+ _objc_retainBlock
CStrings:
+ "isMainThread"
```
