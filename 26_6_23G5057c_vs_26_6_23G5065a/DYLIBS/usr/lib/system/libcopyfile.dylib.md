## libcopyfile.dylib

> `/usr/lib/system/libcopyfile.dylib`

```diff

-  __TEXT.__text: 0x7940
-  __TEXT.__auth_stubs: 0x630
+  __TEXT.__text: 0x796c
+  __TEXT.__auth_stubs: 0x620
   __TEXT.__const: 0x1c8
   __TEXT.__cstring: 0x1b8e
   __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x3b0
-  __AUTH_CONST.__auth_got: 0x318
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__const: 0xe0
   __DATA_DIRTY.__bss: 0x10
   - /usr/lib/system/libcompiler_rt.dylib
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
Functions:
~ _copyfile : 3976 -> 3996
~ _copyfile_set_dst_permissions : 476 -> 500

```
