## libsystem_malloc_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib`

```diff

-657.60.19.0.0
-  __TEXT.__text: 0x961f8
+657.60.20.0.0
+  __TEXT.__text: 0x97204
   __TEXT.__auth_stubs: 0x6b0
   __TEXT.__const: 0x614
   __TEXT.__cstring: 0x14a9e

   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  Functions: 1033
-  Symbols:   1297
+  Functions: 1038
+  Symbols:   1302
   CStrings:  1006
 
Symbols:
+ _pgm_malloc_type_calloc
+ _pgm_malloc_type_malloc
+ _pgm_malloc_type_malloc_with_options
+ _pgm_malloc_type_memalign
+ _pgm_malloc_type_realloc

```
