## libsystem_malloc_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_malloc_debug.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__dof_magmalloc`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__AUTH.__v_zone`
- `__DATA.__data`

```diff

-886.0.4.0.0
-  __TEXT.__text: 0xf0860
+886.0.8.0.0
+  __TEXT.__text: 0xf0b64
   __TEXT.__const: 0x69f
   __TEXT.__cstring: 0x30b45
   __TEXT.__dof_magmalloc: 0x8c7

   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
   Functions: 1215
-  Symbols:   1471
+  Symbols:   1472
   CStrings:  1629
 
Symbols:
+ __msl_lock
+ _msl_registered
- __register_msl_dylib_pred
Functions:
~ __malloc_lock_all : 480 -> 700
~ __malloc_unlock_all : 440 -> 620
~ __malloc_reinit_lock_all : 412 -> 440
~ __malloc_register_stack_logger : 260 -> 604
```
