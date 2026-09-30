## libsystem_coreservices.dylib

> `/usr/lib/system/libsystem_coreservices.dylib`

```diff

-190.0.0.0.0
-  __TEXT.__text: 0x1ba0
-  __TEXT.__auth_stubs: 0x2f0
-  __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x3cd
-  __TEXT.__oslogstring: 0x1ae
-  __TEXT.__unwind_info: 0xe0
+191.1.2.0.0
+  __TEXT.__text: 0x1c54
+  __TEXT.__auth_stubs: 0x2b0
+  __TEXT.__const: 0x68
+  __TEXT.__cstring: 0x329
+  __TEXT.__oslogstring: 0x23d
+  __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x928
-  __AUTH_CONST.__auth_got: 0x178
-  __AUTH_CONST.__const: 0x80
+  __DATA_CONST.__const: 0x948
+  __AUTH_CONST.__auth_got: 0x158
+  __AUTH_CONST.__const: 0xa0
   __DATA.__bss: 0x820
-  __DATA_DIRTY.__bss: 0x20
+  __DATA_DIRTY.__bss: 0x30
   __DATA_DIRTY.__common: 0x88
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib

   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: AF147A9B-F6EC-3543-8BAF-FA344478BBA1
-  Functions: 43
-  Symbols:   187
-  CStrings:  64
+  UUID: E3E6E328-B4BE-396A-A064-FD4AAEA7C7A3
+  Functions: 47
+  Symbols:   201
+  CStrings:  63
 
Symbols:
+ _lchmod
+ _makeDirectoryWithUIDAndGID.cold.1
+ _makeDirectoryWithUIDAndGID.cold.2
+ _makeDirectoryWithUIDAndGID.cold.3
+ _makeDirectoryWithUIDAndGID.cold.4
+ _makeDirectoryWithUIDAndGID.cold.5
+ _makeDirectoryWithUIDAndGID.cold.6
- __dyld_get_image_uuid
- __dyld_get_shared_cache_range
- __dyld_get_shared_cache_uuid
- __os_log_simple
- _chmod
CStrings:
+ "makeDirectory"
- "default"
- "makeDirectoryWithUIDAndGID"

```
