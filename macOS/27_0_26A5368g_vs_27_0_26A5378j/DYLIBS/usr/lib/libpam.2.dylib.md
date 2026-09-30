## libpam.2.dylib

> `/usr/lib/libpam.2.dylib`

```diff

-  __TEXT.__text: 0x34ec
+  __TEXT.__text: 0x34bc
   __TEXT.__cstring: 0x1ef5
   __TEXT.__const: 0x5d
   __TEXT.__unwind_info: 0x140
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _openpam_read_apple_chain : 224 -> 232
~ _openpam_read_chain_from_filehandle : 1276 -> 1240
~ _match_word : 148 -> 140
~ _openpam_free_envlist : 104 -> 88
~ _openpam_readline : 568 -> 592
~ _openpam_set_option : 480 -> 484
~ _pam_getenv : 140 -> 116

```
