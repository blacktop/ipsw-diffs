## com.apple.AppleKeyStoreEvents

> `/System/Library/UserEventPlugins/com.apple.AppleKeyStoreEvents.plugin/com.apple.AppleKeyStoreEvents`

```diff

-2155.122.1.0.0
-  __TEXT.__text: 0x320
-  __TEXT.__auth_stubs: 0xc0
-  __TEXT.__cstring: 0x135
-  __TEXT.__oslogstring: 0xa8
-  __TEXT.__unwind_info: 0x68
-  __DATA.__auth_got: 0x60
-  __DATA.__got: 0x10
+2369.0.0.0.7
+  __TEXT.__text: 0x1684
+  __TEXT.__auth_stubs: 0x250
+  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0x3a4
+  __TEXT.__oslogstring: 0x17c
+  __TEXT.__unwind_info: 0xe0
+  __DATA.__const: 0xa8
+  __DATA.__data: 0x4
+  __DATA.__auth_got: 0x128
+  __DATA.__got: 0x28
+  __DATA.__auth_ptr: 0x8
+  __DATA.__common: 0x8
+  __DATA.__bss: 0x50
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
