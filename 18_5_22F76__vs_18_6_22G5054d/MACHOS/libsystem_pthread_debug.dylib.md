## libsystem_pthread_debug.dylib

> `/System/DriverKit/usr/lib/system/libsystem_pthread_debug.dylib`

```diff

 536.0.0.0.0
-  __TEXT.__text: 0x1c14c
+  __TEXT.__text: 0x1c030
   __TEXT.__auth_stubs: 0x430
   __TEXT.__const: 0xcc
   __TEXT.__cstring: 0xbcd

   - /System/DriverKit/usr/lib/system/libdyld.dylib
   - /System/DriverKit/usr/lib/system/libsystem_kernel.dylib
   - /System/DriverKit/usr/lib/system/libsystem_platform.dylib
-  UUID: DC38ACDC-698A-3258-8E4B-4E71FF484514
+  UUID: 7782CEE4-D26E-3C25-AEB5-DACFDDC98D40
   Functions: 306
   Symbols:   427
   CStrings:  56
Functions:
~ __pthread_deallocate : 192 -> 188
~ __pthread_start : 732 -> 708
~ __pthread_create : 1172 -> 1168
~ _pthread_install_workgroup_functions_np : 100 -> 96
~ _pthread_create_with_workgroup_np : 140 -> 136
~ __pthread_joiner_wake : 188 -> 184
~ _pthread_exit : 236 -> 232
~ __pthread_set_self : 144 -> 140
~ ___pthread_init : 1696 -> 1684
~ __pthread_bsdthread_init : 656 -> 652
~ __pthread_main_thread_postfork_init : 144 -> 140
~ __pthread_wqthread : 1360 -> 1352
~ __pthread_wqthread_setup : 1348 -> 1336
~ __pthread_wqthread_legacy_worker_wrap : 708 -> 704
~ __pthread_workqueue_supported : 64 -> 60
~ __pthread_allocate : 1684 -> 1676
~ __pthread_join : 2080 -> 2076
~ __pthread_joiner_wait : 1128 -> 1120
~ __pthread_joiner_abort_wait : 628 -> 624
~ __pthread_cond_wait : 1320 -> 1316
~ _pthread_cond_broadcast : 2988 -> 2968
~ _pthread_cond_signal_thread_np : 3136 -> 3116
~ _pthread_cond_signal : 2984 -> 2964
~ __pthread_ulock_cond_wait : 1084 -> 1076
~ __pthread_cond_check_init_slow : 1380 -> 1376
~ __pthread_mutex_fairshare_unlock_drop : 356 -> 352
~ __pthread_mutex_ulock_lock_slow : 828 -> 824
~ __pthread_mutex_ulock_unlock_slow : 412 -> 404
~ __pthread_mutex_firstfit_wake : 264 -> 260
~ __pthread_qos_class_encode_workqueue : 340 -> 336
~ __pthread_workqueue_parallelism_for_priority : 344 -> 340
~ __pthread_rwlock_lock_wait : 1512 -> 1508
~ __pthread_rwlock_unlock_drop : 264 -> 260
~ _pthread_introspection_setspecific_np : 120 -> 116
~ _pthread_introspection_getspecific_np : 116 -> 112
~ __pthread_dependency_fulfill_slow : 328 -> 312
~ _pthread_dependency_wait_np : 584 -> 560

```
