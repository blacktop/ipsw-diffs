## libgmalloc.dylib

> `/usr/lib/libgmalloc.dylib`

```diff

-  __TEXT.__text: 0x27b8
+  __TEXT.__text: 0x27b4
   __TEXT.__auth_stubs: 0x360
   __TEXT.__const: 0x48
   __TEXT.__cstring: 0x1308
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __AUTH_CONST.__interpose : content changed
~ __DATA.__data : content changed
Functions:
~ _GMmprotect : 220 -> 232
~ _GuardMalloc_batch_malloc : 164 -> 148
CStrings:
+ "version 064578.53.2\n"
- "version 064578.53.1\n"

```
