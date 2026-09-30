## fseventsd

> `/usr/libexec/fseventsd`

```diff

-1406.0.0.0.0
-  __TEXT.__text: 0x18240
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__cstring: 0xde4
+1407.0.0.0.0
+  __TEXT.__text: 0x17680
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__cstring: 0xd9a
   __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0x3124
-  __TEXT.__unwind_info: 0x370
-  __DATA_CONST.__auth_got: 0x6b8
-  __DATA_CONST.__got: 0xb0
+  __TEXT.__oslogstring: 0x2f2f
+  __TEXT.__unwind_info: 0x360
+  __DATA_CONST.__auth_got: 0x688
+  __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x318
+  __DATA_CONST.__const: 0x2d8
   __DATA_CONST.__cfstring: 0x4e0
   __DATA.__data: 0x232
   __DATA.__bss: 0x468

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: D7EEC28B-1A79-3A35-AD82-4B3E14AC7C98
-  Functions: 379
-  Symbols:   241
-  CStrings:  494
+  UUID: 1D490BF0-1AB7-3395-A16A-8E783FE38C79
+  Functions: 371
+  Symbols:   229
+  CStrings:  482
 
Symbols:
- _XPC_ACTIVITY_GRACE_PERIOD
- _XPC_ACTIVITY_INTERVAL
- _XPC_ACTIVITY_INTERVAL_1_DAY
- _XPC_ACTIVITY_PRIORITY
- _XPC_ACTIVITY_PRIORITY_MAINTENANCE
- _XPC_ACTIVITY_REPEATING
- _stat
- _xpc_activity_get_state
- _xpc_activity_register
- _xpc_activity_set_criteria
- _xpc_dictionary_set_bool
- _xpc_dictionary_set_uint64
CStrings:
- "%s: (%s) dev(%d) Check purge threshold - delta(%ld) last_id(%llu)"
- "%s: (%s) dev(%d) Cooldown period for purge threshold - delta(%ld) last_id(%llu)"
- "%s: (%s) dev(%d) stat failed <%d>:<%s> "
- "%s: PURGE num_logs(%d)"
- "%s: di %p (%s) dev(%d)"
- "%s: di %p (%s) dev(%d) - HFSIOC_GET_VERY_LOW_DISK blocks(%u) "
- "%s: di %p (%s) dev(%d) - HFSIOC_GET_VERY_LOW_DISK failed <%d>:<%s> "
- "%s: di %p (%s) dev(%d) - statfs  block_size<%u> free_blocks<%lld> allocated_blocks<%lld>"
- "%s: di %p (%s) dev(%d) - statfs failed <%d>:<%s> "
- "com.apple.fseventsd.daily"
- "purge_history_policy"
- "v16@?0^{_xpc_activity_s=}8"

```
