## libsystem_pthread_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_pthread_debug.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_DIRTY.__data`

```diff

-553.0.0.0.0
-  __TEXT.__text: 0x1c1c8
+553.0.1.0.0
+  __TEXT.__text: 0x1c1d0
   __TEXT.__const: 0xcc
   __TEXT.__cstring: 0xc10
   __TEXT.__unwind_info: 0x298
Functions:
~ ___pthread_init : 1740 -> 1736
~ __pthread_bsdthread_init : 652 -> 664
```
