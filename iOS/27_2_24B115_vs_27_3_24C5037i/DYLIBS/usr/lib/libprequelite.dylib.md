## libprequelite.dylib

> `/usr/lib/libprequelite.dylib`

```diff

-162.0.0.0.0
-  __TEXT.__text: 0xce48
-  __TEXT.__objc_methlist: 0x1028
+164.0.0.0.0
+  __TEXT.__text: 0xce94
+  __TEXT.__objc_methlist: 0x1030
   __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0xf47
+  __TEXT.__cstring: 0xf73
   __TEXT.__oslogstring: 0x696
   __TEXT.__gcc_except_tab: 0xa8
-  __TEXT.__unwind_info: 0x568
+  __TEXT.__unwind_info: 0x570
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_selrefs: 0xa30
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__got: 0x138
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0xc80
+  __AUTH_CONST.__cfstring: 0xca0
   __AUTH_CONST.__objc_const: 0x2740
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 351
-  Symbols:   809
-  CStrings:  204
+  Functions: 352
+  Symbols:   810
+  CStrings:  205
 
Symbols:
+ -[PQLConnection registerFunction:nArgs:flags:handler:]
Functions:
~ -[PQLConnection registerFunction:nArgs:handler:] : 436 -> 12
+ -[PQLConnection registerFunction:nArgs:flags:handler:]
CStrings:
+ "flags 0x%x must not contain a text encoding"
```
