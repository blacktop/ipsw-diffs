## libsystem_pthread.dylib

> `/usr/lib/system/libsystem_pthread.dylib`

```diff

-  __TEXT.__text: 0xa6e8
+  __TEXT.__text: 0xa6f0
   __TEXT.__const: 0x150
   __TEXT.__cstring: 0xdbd
   __TEXT.__unwind_info: 0x338

   __DATA.__common: 0x2
   __DATA_DIRTY.__data: 0x40
   __DATA_DIRTY.__common: 0x38
-  __DATA_DIRTY.__bss: 0xc030
+  __DATA_DIRTY.__bss: 0x8030
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libmacho.dylib
   - /usr/lib/system/libsystem_kernel.dylib
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ _pthread_key_create : 276 -> 284

```
