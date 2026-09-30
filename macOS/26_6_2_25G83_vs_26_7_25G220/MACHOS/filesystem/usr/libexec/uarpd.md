## uarpd

> `usr/libexec/uarpd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1345.160.8.0.1
-  __TEXT.__text: 0xa1f44
+1345.160.9.700.1
+  __TEXT.__text: 0xa2198
   __TEXT.__auth_stubs: 0x8f0
   __TEXT.__objc_stubs: 0x8c40
   __TEXT.__objc_methlist: 0x76c8

   __TEXT.__objc_classname: 0x18e8
   __TEXT.__objc_methtype: 0x28c3
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x968c
-  __TEXT.__oslogstring: 0x77f6
+  __TEXT.__cstring: 0x96da
+  __TEXT.__oslogstring: 0x7839
   __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__unwind_info: 0x1e10
+  __TEXT.__unwind_info: 0x1e20
   __DATA_CONST.__auth_got: 0x488
   __DATA_CONST.__got: 0x4f8
   __DATA_CONST.__const: 0x10a8
-  __DATA_CONST.__cfstring: 0x4c00
+  __DATA_CONST.__cfstring: 0x4da0
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 3509
+  Functions: 3512
   Symbols:   208
-  CStrings:  4341
+  CStrings:  4355
 
CStrings:
+ "%s: uncompressedLength (%u) exceeds decompressionBuffer size (%lu)"
+ "A3060"
+ "A3061"
+ "A3345"
+ "A3436"
+ "A3437"
+ "A3438"
+ "A3439"
+ "A3440"
+ "A3441"
+ "A3531"
+ "A3532"
+ "A3533"
+ "A3577"
```
