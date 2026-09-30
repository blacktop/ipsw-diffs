## libCoreFSCache.dylib

> `/System/Library/Frameworks/OpenGLES.framework/libCoreFSCache.dylib`

```diff

-  __TEXT.__text: 0x5a90
+  __TEXT.__text: 0x5a78
   __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x29a
   __TEXT.__oslogstring: 0xb9a
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__unwind_info: 0x140
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x58
   __DATA_CONST.__got: 0x0
Sections:
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
Functions:
~ _fscache_open -> _close_data_file : 88 -> 308
~ _close_data_file -> _fscache_open : 308 -> 88
~ _fscache_close_worker : 1144 -> 1120

```
