## MetadataUtilities

> `/System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities`

```diff

-  __TEXT.__text: 0x5c34c
+  __TEXT.__text: 0x5d7b4
   __TEXT.__objc_methlist: 0x494
-  __TEXT.__const: 0x3d56
-  __TEXT.__cstring: 0x71df
-  __TEXT.__oslogstring: 0x1a18
+  __TEXT.__const: 0x3d72
+  __TEXT.__cstring: 0x722b
+  __TEXT.__oslogstring: 0x1a3a
   __TEXT.__ustring: 0x9a
   __TEXT.__gcc_except_tab: 0x18
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0xc78
+  __TEXT.__unwind_info: 0xcb0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x400
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x370
-  __DATA_CONST.__got: 0x158
+  __DATA_CONST.__got: 0x160
   __AUTH_CONST.__const: 0x8f8
   __AUTH_CONST.__cfstring: 0x4c80
   __AUTH_CONST.__objc_const: 0x1178
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0xd60
-  __AUTH.__objc_data: 0x190
+  __AUTH_CONST.__auth_got: 0xd88
+  __AUTH.__objc_data: 0x2d0
   __AUTH.__data: 0x30
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x28
   __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x2157c
-  __DATA.__bss: 0x2d8
-  __DATA.__common: 0x850
-  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA.__bss: 0x2e8
+  __DATA.__common: 0x860
+  __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x1b8
-  __DATA_DIRTY.__common: 0xf0
-  __DATA_DIRTY.__bss: 0x348
+  __DATA_DIRTY.__common: 0xe0
+  __DATA_DIRTY.__bss: 0x338
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreNLP.framework/CoreNLP

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1417
-  Symbols:   3706
-  CStrings:  1878
+  Functions: 1446
+  Symbols:   3740
+  CStrings:  1883
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__data : content changed
~ __AUTH.__thread_vars : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ __db_rwlock_init
+ __db_write_lock
+ __db_write_lock_downgraded
+ _db_convert_to_reader
+ _db_downgrade_lock
+ _db_dryrun_lock
+ _db_longread_lock
+ _db_longread_unlock
+ _db_read_lock
+ _db_read_unlock
+ _db_rwlock_alloc_waiter
+ _db_rwlock_destroy
+ _db_rwlock_is_locked
+ _db_rwlock_reader_excluded
+ _db_rwlock_unlock_unknown
+ _db_rwlock_wait
+ _db_rwlock_waiter_list_dequeue_from_list_inner
+ _db_rwlock_waiter_list_enqueue_inner
+ _db_rwlock_waiter_list_prepend
+ _db_rwlock_wakeup
+ _db_upgrade_lock
+ _db_write_unlock
+ _db_writelock_assertlock
+ _db_writer_yield_lock
+ _exc_pthread_key
+ _pthread_cond_signal
+ _pthread_mutex_trylock
+ _pthread_override_qos_class_end_np
+ _pthread_override_qos_class_start_np
+ _pthread_self
+ _qos_level
CStrings:
+ "*warn* fd[%d] - len:%d %{public}s"
+ "list->head==0"
+ "lock->writer != pthread_self()"
+ "sdb2_rwlock.c"
+ "waiter->threadid"

```
