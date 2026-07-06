## SpotlightLinguistics

> `/System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics`

```diff

-  __TEXT.__text: 0x482b8
-  __TEXT.__const: 0x5520
+  __TEXT.__text: 0x472ec
+  __TEXT.__const: 0x5510
+  __TEXT.__cstring: 0x2c54
   __TEXT.__oslogstring: 0xe28
-  __TEXT.__cstring: 0x2ca0
   __TEXT.__gcc_except_tab: 0x1134
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1030
+  __TEXT.__unwind_info: 0x1008
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x14d8
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__const: 0xf48
   __AUTH_CONST.__cfstring: 0x2f20
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__auth_got: 0xc28
+  __AUTH_CONST.__auth_got: 0xc00
   __DATA.__data: 0x1098
   __DATA.__bss: 0x368
-  __DATA.__common: 0xcc
-  __DATA_DIRTY.__common: 0xb0
+  __DATA.__common: 0xc4
   __DATA_DIRTY.__bss: 0x15c8
+  __DATA_DIRTY.__common: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1315
-  Symbols:   3739
-  CStrings:  1395
+  Functions: 1288
+  Symbols:   3675
+  CStrings:  1391
 
Sections:
~ __TEXT.__oslogstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __DATA.__data : content changed
Symbols:
- __db_write_lock_downgraded
- _db_convert_to_reader
- _db_downgrade_lock
- _db_dryrun_lock
- _db_longread_lock
- _db_longread_unlock
- _db_read_unlock
- _db_rwlock_alloc_waiter
- _db_rwlock_reader_excluded
- _db_rwlock_wait
- _db_rwlock_waiter_list_enqueue_inner
- _db_rwlock_wakeup
- _db_upgrade_lock
- _db_write_unlock
- _db_writelock_assertlock
- _db_writer_yield_lock
- _exc_pthread_key
- _pthread_cond_destroy
- _pthread_cond_init
- _pthread_cond_signal
- _pthread_cond_wait
- _pthread_mutex_destroy
- _pthread_mutex_init
- _pthread_mutex_trylock
- _pthread_override_qos_class_end_np
- _pthread_override_qos_class_start_np
- _pthread_self
- _qos_class_self
- _qos_level
CStrings:
- "list->head==0"
- "lock->writer != pthread_self()"
- "sdb2_rwlock.c"
- "waiter->threadid"

```
