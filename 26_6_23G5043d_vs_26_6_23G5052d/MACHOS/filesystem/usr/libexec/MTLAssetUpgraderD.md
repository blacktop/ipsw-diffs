## MTLAssetUpgraderD

> `/usr/libexec/MTLAssetUpgraderD`

```diff

-  __TEXT.__text: 0x15a1c
+  __TEXT.__text: 0x15aec
   __TEXT.__auth_stubs: 0x870
   __TEXT.__objc_stubs: 0x740
   __TEXT.__gcc_except_tab: 0xf54
   __TEXT.__const: 0xe0
-  __TEXT.__oslogstring: 0xa51
-  __TEXT.__cstring: 0x8be
+  __TEXT.__oslogstring: 0xa96
+  __TEXT.__cstring: 0x8c6
   __TEXT.text_env: 0x257c
   __TEXT.__objc_methname: 0x4e0
   __TEXT.__unwind_info: 0x578
   __DATA_CONST.__auth_got: 0x448
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__const: 0x228
-  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x1d0
   __DATA.__data: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 288
-  Symbols:   1863
-  CStrings:  205
+  Functions: 286
+  Symbols:   1852
+  CStrings:  208
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.text_env : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ _objc_retain_x27
- _OUTLINED_FUNCTION_12
- _objc_retain_x26
CStrings:
+ "<no error>"
+ "addRecompilationWork: failed to get dynamic library type of '%s'"
+ "recompilation: serialization of dynamic library %@ failed: %@"
- "recompilation: serialization of dynamic library %@ failed"

```
