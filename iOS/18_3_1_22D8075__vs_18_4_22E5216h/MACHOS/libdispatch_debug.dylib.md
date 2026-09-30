## libdispatch_debug.dylib

> `/System/DriverKit/usr/lib/system/libdispatch_debug.dylib`

```diff

-1504.60.7.0.0
-  __TEXT.__text: 0xc8e1c
+1521.100.8.0.0
+  __TEXT.__text: 0xb7b40
   __TEXT.__auth_stubs: 0xb70
-  __TEXT.__const: 0x558
-  __TEXT.__cstring: 0x87b0
+  __TEXT.__const: 0x553
+  __TEXT.__cstring: 0x87e4
   __TEXT.__dof_dispatch: 0x288c
   __TEXT.__dof_voucher: 0x9b5
-  __TEXT.__unwind_info: 0x948
+  __TEXT.__unwind_info: 0x888
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__const: 0x6a0
   __AUTH_CONST.__auth_got: 0x5b8

   - /System/DriverKit/usr/lib/system/libsystem_malloc.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
   - /System/DriverKit/usr/lib/system/libsystem_pthread.dylib
-  Functions: 1198
+  Functions: 1152
   Symbols:   1734
-  CStrings:  777
+  CStrings:  778
 
Symbols:
+ __dispatch_calloc_typed
+ _dispatch_bug.db_last_seen
+ _dispatch_bug_deprecated.dbd_last_seen
+ _dispatch_bug_kevent_client.dbkc_last_seen_1
+ _dispatch_bug_kevent_client.dbkc_last_seen_2
+ _dispatch_bug_kevent_client.dbkc_last_seen_3
+ _dispatch_bug_kevent_vanished.dbkv_last_seen
+ _dispatch_bug_mach_client.dbmc_last_seen
- __dispatch_calloc
- _dispatch_bug.last_seen
- _dispatch_bug_deprecated.last_seen
- _dispatch_bug_kevent_client.last_seen
- _dispatch_bug_kevent_client.last_seen.4172
- _dispatch_bug_kevent_client.last_seen.4174
- _dispatch_bug_kevent_vanished.last_seen
- _dispatch_bug_mach_client.last_seen
CStrings:
+ "BUG IN LIBDISPATCH: Unexpected error from mach recv"

```
