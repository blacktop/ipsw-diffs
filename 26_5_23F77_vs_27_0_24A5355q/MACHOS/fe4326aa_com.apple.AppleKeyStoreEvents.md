## com.apple.AppleKeyStoreEvents

> `/System/Library/UserEventPlugins/com.apple.AppleKeyStoreEvents.plugin/com.apple.AppleKeyStoreEvents`

```diff

-2155.122.1.0.0
-  __TEXT.__text: 0x320 sha256:02796fc8bba792c161a12576716fb0f2faf19a18af28f2d2aeab95cae0f54fbe
-  __TEXT.__auth_stubs: 0xc0 sha256:d46961262b49bb42218c034f932aeadac2944b31d3370b7ab48e454c51976078
-  __TEXT.__cstring: 0x135 sha256:d63025aeb0ca70d348c8ea9f5b5396b80a1f79eb28516e36876ec17a7f1d0660
-  __TEXT.__oslogstring: 0xa8 sha256:4e3808c571c582795711dcb0a0b5134fe72e6733125dc62931d10c072d314854
-  __TEXT.__unwind_info: 0x68 sha256:a0399c8466825249a00a69d22502717a2672e436b451af81c94d1fcea00d7c0e
-  __DATA.__auth_got: 0x60 sha256:75443b2d7eb304af704e135ce779b1582e40b4e112f49dba1aedc8490c781a2a
-  __DATA.__got: 0x10 sha256:40cb96e58e665ad64a2cf8f5ec089104d0e2d98f344bfd9e55d74bd7c0b96392
+2369.0.0.0.7
+  __TEXT.__text: 0x1684 sha256:1f34b2115954ff8ac24df73b1bbf2a9a8ef6a816c246fa8f919e06ab5097fdc2
+  __TEXT.__auth_stubs: 0x250 sha256:e2a0737aa6b78281f5e39538457147b6623a590de5bbdccaa79fce403c26fbb6
+  __TEXT.__const: 0xd8 sha256:90bc5ac964755c2815ff10cbcbf61653cf68264208c955e4ad551f86478880f0
+  __TEXT.__cstring: 0x3a4 sha256:61ee01baa40e97cb2ff0b55ab67132985db982f90442153179c012619eed4d55
+  __TEXT.__oslogstring: 0x17c sha256:0c144cb52db40f56548d5ace454a01d10f476b7faa8a25386553f9c35da4265b
+  __TEXT.__unwind_info: 0xe0 sha256:fcda00669ad74bf427f8262151e6a07469a61435f0db680894b5047d29641647
+  __DATA.__const: 0xa8 sha256:88023623fb18c71140bc916139e5ea04829956b2ed21156cbe735c6e5060268d
+  __DATA.__data: 0x4 sha256:ad95131bc0b799c0b1af477fb14fcf26a6a9f76079e48bf090acb7e8367bfd0e
+  __DATA.__auth_got: 0x128 sha256:92b159f863c99d81135dedd2f73bbcc47ce3b354b3c12bf745f21160f657d794
+  __DATA.__got: 0x28 sha256:d4e59ab65e31e49ede043585045ba9e443a29dfaf2bc6e5470adeb552a3ae2b8
+  __DATA.__auth_ptr: 0x8 sha256:3c434e043460eb153fb9d083737226365344d20461c45db225446b0e64e9ca79
+  __DATA.__common: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
+  __DATA.__bss: 0x50 sha256:5b6fb58e61fa475939767d68a446f97f1bff02c0e5935a3ea8bb51e6515783d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
-  UUID: A09F4EE1-BF75-3DB6-AF55-3F6CAF0C0FEC
-  Functions: 5
-  Symbols:   16
-  CStrings:  13
+  UUID: 3AAE2E1D-1AAF-3635-8DD2-E664A6F1DB7C
+  Functions: 55
+  Symbols:   92
+  CStrings:  46
 
Symbols:
+ _AKS_FV_MDM_RECOVERY_KEY_UUID
+ _REQUIRE_func
+ __NSConcreteStackBlock
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___stdoutp
+ __akslog_filter
+ __os_log_debug_impl
+ _abort
+ _analytics_send_event_lazy
+ _analytics_send_perf_data
+ _ascii_hex_to_bytes
+ _byte_swap_val
+ _bytes_to_str_hint
+ _cc_cmp_safe
+ _ccdigest
+ _cchmac
+ _ccsha256_di
+ _circular_queue_clear
+ _circular_queue_dequeue
+ _circular_queue_dequeue_all
+ _circular_queue_enqueue
+ _circular_queue_free
+ _circular_queue_init
+ _circular_queue_peek
+ _circular_queue_size
+ _class_gen_get
+ _class_gen_set
+ _class_id_get
+ _class_persona_get
+ _class_persona_set
+ _class_persona_unset
+ _compress_uuid
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create_with_target$V2
+ _dump_bytes_internal
+ _dump_deltas
+ _err_sks_to_aks
+ _fprintf
+ _free
+ _fs_class_key
+ _get_akslog_context
+ _get_akslog_pid
+ _get_clock_time
+ _get_kcv
+ _get_usec_time
+ _gettimeofday
+ _ipc_microseconds_to_seconds
+ _ipc_seconds_to_microsecond_interval
+ _is_non_zero
+ _keychain_key
+ _keystore_type
+ _lock_state_change_delta_id_to_string
+ _mach_continuous_time
+ _mach_timebase_info
+ _malloc_type_calloc
+ _memcmp_c
+ _memcpy
+ _memset_s
+ _persona_uuid_is_valid
+ _pfk_params_is_valid
+ _print_kcv
+ _set_akslog_context
+ _set_akslog_pid
+ _snprintf
+ _store_type_equal
+ _ticket_update
+ _time_absolute_to_nanoseconds
+ _time_seconds_to_abs_interval
+ _uuid_to_string
+ _uuid_unparse
+ _vsnprintf
+ _xpc_dictionary_create
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_uint64
CStrings:
+ "%02x"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s %sdump %s (len = %zd)%s%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s overflow%s\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleKeyStore/timestamp_ticket.c"
+ ":"
+ "AKSKeyBagLockState 2nd queue"
+ "CA event submitted"
+ "CA fwk missing, not sending event"
+ "KeyStoreNotifier %s: duration = %0.3lf %s"
+ "REQUIRE_func"
+ "^v8@?0"
+ "aks"
+ "apfs_to_uea"
+ "circular_queue_init"
+ "com.apple.applekeystore.notification.lock_state"
+ "delta: %s = %x0x"
+ "dump_bytes_internal"
+ "kAppleKeyStoreLockStateChangeMessageWithPayload (%d)"
+ "kext_to_apfs"
+ "last"
+ "ms"
+ "notification_id"
+ "ns"
+ "pico quick!"
+ "processing(delta_id:%d): last_timestamp=0x%llx"
+ "s"
+ "sks_to_kext"
+ "uea_to_app"
+ "unknown"
+ "version"
+ "μs"

```
