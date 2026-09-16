## libdispatch_debug.dylib

> `/System/DriverKit/usr/lib/system/libdispatch_debug.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__dof_dispatch`
- `__TEXT.__dof_voucher`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__data`

```diff

-1605.0.2.0.0
-  __TEXT.__text: 0xb87a8
+1605.40.4.0.0
+  __TEXT.__text: 0xb88c8
   __TEXT.__const: 0x54b
   __TEXT.__cstring: 0x8a15
   __TEXT.__dof_dispatch: 0x288c

   - /System/DriverKit/usr/lib/system/libsystem_malloc.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  Functions: 1170
-  Symbols:   1589
+  Functions: 1171
+  Symbols:   1590
   CStrings:  793
 
Symbols:
+ _firehose_mach_port_allocate_connection_port
Functions:
~ _firehose_client_reconnect : 3004 -> 3048
+ _firehose_mach_port_allocate_connection_port
```
