## libsystem_platform.dylib

> `/usr/lib/system/libsystem_platform.dylib`

```diff

-  __TEXT.__text: 0x7e5c
+  __TEXT.__text: 0x7e08
   __TEXT.__resolver_help: 0x288
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x8a1
Sections:
~ __TEXT.__unwind_info : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA_DIRTY.__la_resolver : content changed
Functions:
~ __platform_strlcpy : 1308 -> 1276
~ __platform_strstr : 140 -> 136
~ __platform_strncpy : 1080 -> 1044
~ __simple_asl_msg_set : 332 -> 312
~ __simple_getenv : 164 -> 176
~ __platform_memmove : 720 -> 736
~ ___sme_memcpy : 248 -> 256
~ __platform_memccpy : 1080 -> 1052

```
