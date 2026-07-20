## ptpcamerad

> `/usr/libexec/ptpcamerad`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2114.0.0.0.0
+2116.0.0.0.0
   __TEXT.__text: 0x1b76c
   __TEXT.__auth_stubs: 0xa60
   __TEXT.__objc_stubs: 0x3a40
-  __TEXT.__objc_methlist: 0x171c
+  __TEXT.__objc_methlist: 0x1734
   __TEXT.__const: 0x60
-  __TEXT.__objc_methname: 0x45e5
+  __TEXT.__objc_methname: 0x460e
   __TEXT.__cstring: 0x1a8b
   __TEXT.__oslogstring: 0x3f
   __TEXT.__objc_classname: 0x113

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__auth_got: 0x540
   __DATA_CONST.__got: 0x2b0
-  __DATA.__objc_const: 0x1e50
-  __DATA.__objc_selrefs: 0x13b0
+  __DATA.__objc_const: 0x1ed0
+  __DATA.__objc_selrefs: 0x13b8
   __DATA.__objc_ivar: 0x1cc
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x1e0

   - /usr/lib/libobjc.A.dylib
   Functions: 512
   Symbols:   267
-  CStrings:  1331
+  CStrings:  1333
 
CStrings:
+ "T@\"NSString\",?,R,C,N"
+ "mediaItemIdentifier"
```
