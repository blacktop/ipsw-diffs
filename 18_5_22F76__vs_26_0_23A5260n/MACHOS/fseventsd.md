## fseventsd

> `/usr/libexec/fseventsd`

```diff

-1400.100.1.0.0
-  __TEXT.__text: 0x1632c
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__cstring: 0xbd5
+1404.0.0.0.0
+  __TEXT.__text: 0x17e3c
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__cstring: 0xd74
   __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0x2b59
-  __TEXT.__unwind_info: 0x338
-  __DATA_CONST.__auth_got: 0x638
-  __DATA_CONST.__got: 0x80
+  __TEXT.__oslogstring: 0x307e
+  __TEXT.__unwind_info: 0x358
+  __DATA_CONST.__auth_got: 0x6b0
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2b8
-  __DATA_CONST.__cfstring: 0x4a0
+  __DATA_CONST.__const: 0x2d8
+  __DATA_CONST.__cfstring: 0x4e0
   __DATA.__data: 0x232
   __DATA.__bss: 0x468
   __DATA.__common: 0x2248

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 142BA4DA-E012-3D8C-BB5D-6F64DD55D2C4
-  Functions: 354
-  Symbols:   219
-  CStrings:  441
+  UUID: 0BCCE789-2200-3696-9833-9B750EEF398C
+  Functions: 377
+  Symbols:   240
+  CStrings:  487
 
Symbols:
+ _CFErrorGetCode
+ _CFPropertyListCreateWithStream
+ _CFPropertyListWrite
+ _CFReadStreamClose
+ _CFReadStreamCreateWithFile
+ _CFReadStreamOpen
+ _CFShow
+ _CFWriteStreamClose
+ _CFWriteStreamCreateWithFile
+ _CFWriteStreamOpen
+ _XPC_ACTIVITY_GRACE_PERIOD
+ _XPC_ACTIVITY_INTERVAL
+ _XPC_ACTIVITY_INTERVAL_1_DAY
+ _XPC_ACTIVITY_PRIORITY
+ _XPC_ACTIVITY_PRIORITY_MAINTENANCE
+ _XPC_ACTIVITY_REPEATING
+ _xpc_activity_get_state
+ _xpc_activity_register
+ _xpc_activity_set_criteria
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_uint64
CStrings:
+ "\t%s pid %d, flags 0x%llx, #paths %d, sinceWhen: 0x%llx [delta: %llu]\n"
+ "\t%s pid %d, flags 0x%llx, #paths %d, sinceWhen: Now\n"
+ "%s/fseventsd-config"
+ "%s:    purge_events: deleting: %s"
+ "%s: ([SET] previous_uuid) CFStringGetCString ERROR"
+ "%s: <%s> no di found for dev %d (num_devices %d)"
+ "%s: CFPropertyListCreateWithStream done"
+ "%s: CFPropertyListCreateWithStream err(%ld)"
+ "%s: CFPropertyListWrite done"
+ "%s: CFPropertyListWrite err(%ld)"
+ "%s: CFReadStreamCreateWithFile error"
+ "%s: CFWriteStreamCreateWithFile error"
+ "%s: LOW DISK SPACE - logging disabled"
+ "%s: PURGE num_logs(%d)"
+ "%s: [GET] (last_pruned_event_id) CFStringGetCString ERROR"
+ "%s: [GET] (previous_uuid) CFStringGetCString ERROR"
+ "%s: [GET] last_pruned_event_id<%s> "
+ "%s: [GET] prev_uuid_str<%s> "
+ "%s: [SET] (last_pruned_event_id) CFStringGetCString ERROR"
+ "%s: [SET] last_pruned_event_id<%s> "
+ "%s: [SET] prev_uuid_str<%s> "
+ "%s: client (%p) SENT device state event to pid %d\n"
+ "%s: client (%p) failed sending device state event (0x%x) to pid %d\n"
+ "%s: client: %p : %s : DEVICE STATE EVENT"
+ "%s: di %p (%s) dev(%d)"
+ "%s: di %p (%s) dev(%d) - HFSIOC_GET_DESIRED_DISK blocks(%u) "
+ "%s: di %p (%s) dev(%d) - HFSIOC_GET_DESIRED_DISK failed <%d>:<%s> "
+ "%s: di %p (%s) dev(%d) - statfs  block_size<%u> free_blocks<%lld> allocated_blocks<%lld>"
+ "%s: di %p (%s) dev(%d) - statfs failed <%d>:<%s> "
+ "%s: load previous uuid"
+ "%s: open_dprotected_np err(%s)"
+ "%s: prev_uuid_cfstr == NULL"
+ "%s: save previous uuid"
+ "%s: state_event_path(%s) %d (num_devices %d)"
+ "/.fseventsd-config/current_uuid/%s/previous_uuid/%s/last_pruned_event_id/%s"
+ "/.fseventsd-config/current_uuid/%s/previous_uuid/NO-UUID/last_pruned_event_id/0"
+ "/.fseventsd-config/current_uuid/NO-UUID-NO-DEV-INFO"
+ "check_low_disk_space"
+ "client_loop"
+ "com.apple.fseventsd.daily"
+ "handle_device_config"
+ "last_pruned_event_id"
+ "previous_uuid"
+ "purge_history_policy"
+ "send_device_state_event"
+ "v16@?0^{_xpc_activity_s=}8"
- "\t%s pid %d, flags 0x%x, #paths %d, sinceWhen: 0x%llx [delta: %llu]\n"
- "\t%s pid %d, flags 0x%x, #paths %d, sinceWhen: Now\n"

```
