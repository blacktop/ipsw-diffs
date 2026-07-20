## libsystem_malloc.dylib

> `/usr/lib/system/libsystem_malloc.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__dof_magmalloc`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__data`
- `__AUTH.__v_zone`
- `__DATA.__data`

```diff

-886.0.4.0.0
-  __TEXT.__text: 0x4329c
+886.0.8.0.0
+  __TEXT.__text: 0x43304
   __TEXT.__const: 0x614
   __TEXT.__cstring: 0xb5c5
   __TEXT.__dof_magmalloc: 0x912

   __AUTH.__v_zone: 0x4000
   __DATA.__data: 0xb8
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x210c
+  __DATA.__bss: 0x2114
   __DATA.__common: 0x78
   __DATA_DIRTY.__data: 0x30
   __DATA_DIRTY.__bss: 0xc0

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
-  Functions: 1102
+  Functions: 1101
   Symbols:   1156
   CStrings:  965
 
Symbols:
+ __msl_lock
+ _msl_registered
- __register_msl_dylib_pred
- _register_msl_dylib
Functions:
~ __malloc_fork_prepare : 240 -> 284
~ __malloc_fork_parent : 216 -> 256
~ __malloc_register_stack_logger : 236 -> 644
- _register_msl_dylib
~ __malloc_fork_child : 228 -> 236
```
