## ptpcamerad

> `/usr/libexec/ptpcamerad`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2116.0.0.0.0
-  __TEXT.__text: 0x1b76c
+2118.0.0.0.0
+  __TEXT.__text: 0x1b780
   __TEXT.__auth_stubs: 0xa60
   __TEXT.__objc_stubs: 0x3a40
-  __TEXT.__objc_methlist: 0x1734
+  __TEXT.__objc_methlist: 0x174c
   __TEXT.__const: 0x60
-  __TEXT.__objc_methname: 0x460e
+  __TEXT.__objc_methname: 0x4666
   __TEXT.__cstring: 0x1a8b
   __TEXT.__oslogstring: 0x3f
   __TEXT.__objc_classname: 0x113

   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__auth_got: 0x540
   __DATA_CONST.__got: 0x2b0
-  __DATA.__objc_const: 0x1ed0
-  __DATA.__objc_selrefs: 0x13b8
-  __DATA.__objc_ivar: 0x1cc
+  __DATA.__objc_const: 0x1f00
+  __DATA.__objc_selrefs: 0x13c8
+  __DATA.__objc_ivar: 0x1d0
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x48

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 512
+  Functions: 514
   Symbols:   267
-  CStrings:  1333
+  CStrings:  1337
 
CStrings:
+ "TB,N,V_sessionCloseCalled"
+ "_sessionCloseCalled"
+ "sessionCloseCalled"
+ "setSessionCloseCalled:"
```
