## libsandbox.1.dylib

> `/usr/lib/libsandbox.1.dylib`

```diff

-3033.0.0.0.1
-  __TEXT.__text: 0x182c sha256:bb11c3d9704d3d2bee5ab494ca4016c59438c85b8b4ca1c77b66e9aadfddadc2
+3051.0.18.0.3
+  __TEXT.__text: 0x18ac sha256:060fc74418b091ac948758e3b8d3e469fc267ebc05706840723f8a2d71d4d48e
   __TEXT.__const: 0x20 sha256:3e21dcb09e321ccd49e0ea4ed992dd68b37ff6f70c4b53e43e56f5d7e75a5caa
+  __TEXT.__cstring: 0x1d5 sha256:d0322bdf5e68daf799ab59390406b4218775bdcbc28941bfee1fe56be044bf19
   __TEXT.__oslogstring: 0x1f sha256:bee8caa2787a92021d2e8b286c20b817da4399f6596c43fa5fed2d2288c95541
-  __TEXT.__cstring: 0x1c2 sha256:ca3cf1d9d2d1eeabc0d0514df5e3f3a3ac1361b84f153601e00eb8267c2cb9cd
-  __TEXT.__unwind_info: 0xe8 sha256:d747230291a825947adab36ea40fdf09fa598d2055542bb30e4c41028418b2f0
+  __TEXT.__unwind_info: 0xe8 sha256:60e9231a68e14cc154ff821f291adc67ef30196beb8073544d16aa80028f6ab8
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x20 sha256:b85468ce5a4ac61fd3d1a808fe4323c116af19d4b2059b66415fb2381e22094d
+  __DATA_CONST.__const: 0x20 sha256:06ffbd6eeeaecb947927e4971130fc1a1072b722c2b17a04893b09e7594ffe5d
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/libMatch.1.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: D878385A-8953-37C6-97DC-D07A190B6201
+  UUID: 7AAB5B65-091F-3C32-99CC-35F27A203916
   Functions: 50
-  Symbols:   97
-  CStrings:  22
+  Symbols:   96
+  CStrings:  23
 
Symbols:
+ _sb_packbuff_init_with_buffer.cold.1
- _reallocf
- _sb_packbuff_pack_item.cold.3
CStrings:
+ "(bytes_to_advance % ITEM_ALIGNMENT) == 0"
+ "FC875440-875A-419D-94A1-5367A943F40B"
+ "buffer != NULL"
+ "sb_packbuff_init_with_buffer"
- "(bytes_to_advance % BYTE_ALIGNMENT) == 0"
- "C7CDAAD8-33DB-4677-8224-7E1A0221C01C"
- "additional_bytes != NULL"

```
