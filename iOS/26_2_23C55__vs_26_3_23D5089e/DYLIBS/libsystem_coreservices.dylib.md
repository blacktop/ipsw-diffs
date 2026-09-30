## libsystem_coreservices.dylib

> `/usr/lib/system/libsystem_coreservices.dylib`

```diff

-191.2.4.0.0
-  __TEXT.__text: 0x193c
-  __TEXT.__auth_stubs: 0x2a0
+191.3.2.0.0
+  __TEXT.__text: 0x1990
+  __TEXT.__auth_stubs: 0x2e0
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x31b
-  __TEXT.__oslogstring: 0x1ff
+  __TEXT.__cstring: 0x376
+  __TEXT.__oslogstring: 0x1c2
   __TEXT.__unwind_info: 0xd8
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x928
-  __AUTH_CONST.__auth_got: 0x150
+  __AUTH_CONST.__auth_got: 0x170
   __AUTH_CONST.__const: 0x80
   __DATA.__bss: 0x820
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 1F15AF51-8E5D-3907-8114-36997941C191
-  Functions: 42
+  UUID: 3C0A8240-C4A1-37C2-8898-64FD3D947389
+  Functions: 41
   Symbols:   184
-  CStrings:  59
+  CStrings:  62
 
Symbols:
+ __dyld_get_image_uuid
+ __dyld_get_shared_cache_range
+ __dyld_get_shared_cache_uuid
+ __os_log_simple
- __set_user_dir_suffix.cold.2
- __set_user_dir_suffix.cold.3
Functions:
~ __set_user_dir_suffix : 412 -> 348
~ _validate_user_dir_suffix : 192 -> 408
- _makeDirectory.cold.2
- __set_user_dir_suffix.cold.3
CStrings:
+ "%s: '..' not allowed, suffix=%s"
+ "%s: slash not allowed, suffix=%s"
+ "../"
+ "/"
+ "validate_user_dir_suffix"
- "/../"
- "illegal path traversal (..) pattern found in user_dir_suffix"

```
