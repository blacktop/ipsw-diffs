## libsandbox.1.dylib

> `/usr/lib/libsandbox.1.dylib`

```diff

-2680.120.12.0.0
-  __TEXT.__text: 0x1734 sha256:02e994f179a9ba2e70339989eb7a657dfddc7b8d23e1ac735fd5ed4675b8d6f6
-  __TEXT.__auth_stubs: 0x160 sha256:2f1f10d2a378a9f2b620b6f1bf3bfa35cc2b41e20821944a0d1841f5078bb1f4
+3033.0.0.0.1
+  __TEXT.__text: 0x182c sha256:bb11c3d9704d3d2bee5ab494ca4016c59438c85b8b4ca1c77b66e9aadfddadc2
   __TEXT.__const: 0x20 sha256:3e21dcb09e321ccd49e0ea4ed992dd68b37ff6f70c4b53e43e56f5d7e75a5caa
   __TEXT.__oslogstring: 0x1f sha256:bee8caa2787a92021d2e8b286c20b817da4399f6596c43fa5fed2d2288c95541
-  __TEXT.__cstring: 0x16e sha256:d14656bdb6444c2bc832f5db77a437e992b984429b12a22d99760e65b7df6d4f
-  __TEXT.__unwind_info: 0xe0 sha256:b80f82e48f2aedeab3ac887836f27c480c81629c2ac1a960b5138429f36ed154
-  __DATA_CONST.__got: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
-  __DATA_CONST.__const: 0x20 sha256:1fcf447743bc1b4b330e4b70faa152dbcfca7823f23383dfe475914662fd8366
-  __AUTH_CONST.__auth_got: 0xb0 sha256:86d2cf5b090f43ee54d8f7c1dcf746a853951191457ff6dac96269a9d24860b9
+  __TEXT.__cstring: 0x1c2 sha256:ca3cf1d9d2d1eeabc0d0514df5e3f3a3ac1361b84f153601e00eb8267c2cb9cd
+  __TEXT.__unwind_info: 0xe8 sha256:d747230291a825947adab36ea40fdf09fa598d2055542bb30e4c41028418b2f0
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x20 sha256:b85468ce5a4ac61fd3d1a808fe4323c116af19d4b2059b66415fb2381e22094d
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/libMatch.1.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: D37545FB-664F-338E-B7AA-F63E7CFE2ADF
-  Functions: 48
-  Symbols:   95
-  CStrings:  19
+  UUID: D878385A-8953-37C6-97DC-D07A190B6201
+  Functions: 50
+  Symbols:   97
+  CStrings:  22
 
Symbols:
+ _sb_packbuff_extend
+ _sb_packbuff_pack_item.cold.3
+ _sb_packbuff_pack_string.cold.1
- ___stack_chk_fail
- ___stack_chk_guard
- _sb_packbuff_realloc
CStrings:
+ "C7CDAAD8-33DB-4677-8224-7E1A0221C01C"
+ "item_type != SB_PACKBUFF_ITEM_TYPE_STRING"
+ "sb_packbuff_pack_string"
+ "str_value != NULL"
- "21F2AA5D-510A-4585-978E-A4E40C7DF520"

```
