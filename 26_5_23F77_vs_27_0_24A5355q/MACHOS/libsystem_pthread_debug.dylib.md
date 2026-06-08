## libsystem_pthread_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_pthread_debug.dylib`

```diff

-539.100.4.0.0
-  __TEXT.__text: 0x1c024
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__const: 0xd4
+553.0.0.0.0
+  __TEXT.__text: 0x1c200
+  __TEXT.__const: 0xcc
   __TEXT.__cstring: 0xc10
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__unwind_info: 0x298
+  __TEXT.__auth_stubs: 0x430
   __DATA_CONST.__got: 0x30
   __AUTH_CONST.__auth_got: 0x218
   __DATA.__data: 0x1c

   - /System/DriverKit/usr/lib/system/libdyld.dylib
   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
-  UUID: 8D19A9B0-C16B-3668-8D77-CED3AF67BF9E
+  UUID: B5CF159B-ED36-3238-997A-92AD7AE0F6DD
   Functions: 306
-  Symbols:   426
+  Symbols:   427
   CStrings:  58
 
Symbols:
+ __dyld_thread_local_free
Functions:
~ __pthread_globals_init : 132 -> 144
~ ___pthread_init : 1732 -> 1740
~ __pthread_wqthread_setup : 1328 -> 1348
~ __pthread_allocate : 1676 -> 1684
~ __pthread_terminate : 936 -> 948
~ __pthread_introspection_hook_callout_thread_terminate : 224 -> 232
~ __pthread_introspection_hook_callout_thread_start : 224 -> 232
~ __pthread_ulock_cond_cleanup : 116 -> 124
~ _pthread_mutex_init : 1268 -> 1276
~ __pthread_mutex_fairshare_lock_slow : 1108 -> 1116
~ __pthread_mutex_fairshare_lock_wait : 744 -> 756
~ __pthread_mutex_fairshare_unlock_slow : 1404 -> 1416
~ __pthread_mutex_firstfit_unlock_slow : 1232 -> 1240
~ __pthread_mutex_firstfit_lock_slow : 1136 -> 1144
~ __pthread_mutex_firstfit_lock_wait : 728 -> 740
~ __pthread_mutex_droplock : 2440 -> 2456
~ _pthread_mutex_unlock : 648 -> 656
~ __pthread_mutex_fairshare_unlock : 532 -> 540
~ _pthread_mutex_lock : 868 -> 876
~ _pthread_mutex_trylock : 872 -> 880
~ _pthread_mutex_destroy : 832 -> 840
~ __pthread_mutex_check_init_slow : 1960 -> 1968
~ __pthread_mutex_fairshare_lock : 648 -> 656
~ _pthread_qos_max_parallelism : 772 -> 796
~ _pthread_time_constraint_max_parallelism : 472 -> 480
~ _pthread_rwlock_destroy : 1148 -> 1152
~ _pthread_rwlock_init : 1336 -> 1348
~ __pthread_rwlock_lock_slow : 2568 -> 2576
~ _pthread_rwlock_rdlock : 1600 -> 1608
~ _pthread_rwlock_tryrdlock : 1600 -> 1608
~ _pthread_rwlock_wrlock : 1596 -> 1604
~ _pthread_rwlock_trywrlock : 1600 -> 1608
~ __pthread_rwlock_unlock_slow : 1628 -> 1636
~ _pthread_rwlock_unlock : 1444 -> 1452
~ __pthread_rwlock_check_init_slow : 1244 -> 1252
~ __pthread_key_global_init : 16 -> 120
~ _pthread_key_create -> __pthread_key_set_destructor : 184 -> 200
~ __pthread_key_set_destructor -> _pthread_key_create : 196 -> 184
~ __pthread_key_unset_destructor : 108 -> 112
~ __pthread_tsd_cleanup_key : 152 -> 156
~ _pthread_atfork : 720 -> 716
~ __pthread_atfork_prepare_handlers : 308 -> 312
~ __pthread_atfork_prepare : 252 -> 256
~ __pthread_atfork_parent : 204 -> 208
~ __pthread_atfork_parent_handlers : 300 -> 304
~ __pthread_atfork_child : 248 -> 252
~ __pthread_atfork_child_handlers : 308 -> 312
~ __pthread_dependency_fulfill_slow : 308 -> 312

```
