## fseventsd

> `/usr/libexec/fseventsd`

```diff

-1407.0.0.0.0
-  __TEXT.__text: 0x17680
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__cstring: 0xd9a
+1407.40.3.0.0
+  __TEXT.__text: 0x18a64
+  __TEXT.__auth_stubs: 0xdd0
+  __TEXT.__cstring: 0xe9c
   __TEXT.__const: 0x148
-  __TEXT.__oslogstring: 0x2f2f
-  __TEXT.__unwind_info: 0x360
-  __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x80
+  __TEXT.__oslogstring: 0x3156
+  __TEXT.__unwind_info: 0x380
+  __DATA_CONST.__auth_got: 0x6e8
+  __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x2d8
-  __DATA_CONST.__cfstring: 0x4e0
+  __DATA_CONST.__const: 0x318
+  __DATA_CONST.__cfstring: 0x4a0
   __DATA.__data: 0x232
   __DATA.__bss: 0x468
   __DATA.__common: 0x2248

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B28D3A82-B53E-3ABD-80D5-FFFEBCD92851
-  Functions: 371
-  Symbols:   229
-  CStrings:  482
+  UUID: 32EA1F72-3465-3CD2-99C8-96A6DA48309A
+  Functions: 393
+  Symbols:   247
+  CStrings:  502
 
Symbols:
+ _XPC_ACTIVITY_GRACE_PERIOD
+ _XPC_ACTIVITY_INTERVAL
+ _XPC_ACTIVITY_INTERVAL_1_DAY
+ _XPC_ACTIVITY_PRIORITY
+ _XPC_ACTIVITY_PRIORITY_MAINTENANCE
+ _XPC_ACTIVITY_REPEATING
+ __os_feature_enabled_impl
+ _acl_add_perm
+ _acl_clear_flags_np
+ _acl_clear_perms
+ _acl_create_entry_np
+ _acl_free
+ _acl_get_flagset_np
+ _acl_get_permset
+ _acl_init
+ _acl_set_file
+ _acl_set_flagset_np
+ _acl_set_qualifier
+ _acl_set_tag_type
+ _getxattr
+ _removexattr
+ _setxattr
+ _stat
+ _xpc_activity_get_state
+ _xpc_activity_register
+ _xpc_activity_set_criteria
+ _xpc_dictionary_set_bool
+ _xpc_dictionary_set_uint64
- _CFErrorGetCode
- _CFPropertyListCreateWithStream
- _CFPropertyListWrite
- _CFReadStreamClose
- _CFReadStreamCreateWithFile
- _CFReadStreamOpen
- _CFShow
- _CFWriteStreamClose
- _CFWriteStreamCreateWithFile
- _CFWriteStreamOpen
CStrings:
+ "%s: (%s) dev(%d) Check purge threshold - delta(%ld) last_id(%llu)"
+ "%s: (%s) dev(%d) Cooldown period for purge threshold - delta(%ld) last_id(%llu)"
+ "%s: (%s) dev(%d) stat failed <%d>:<%s> "
+ "%s: PURGE num_logs(%d)"
+ "%s: di %p (%s) dev(%d)"
+ "%s: di %p (%s) dev(%d) - HFSIOC_GET_VERY_LOW_DISK blocks(%u) "
+ "%s: di %p (%s) dev(%d) - HFSIOC_GET_VERY_LOW_DISK failed <%d>:<%s> "
+ "%s: di %p (%s) dev(%d) - statfs  block_size<%u> free_blocks<%lld> allocated_blocks<%lld>"
+ "%s: di %p (%s) dev(%d) - statfs failed <%d>:<%s> "
+ "%s:%d acl_add_perm err (%s)"
+ "%s:%d acl_clear_flags_np err (%s)"
+ "%s:%d acl_clear_perms err (%s)"
+ "%s:%d acl_create_entry_np err (%s)"
+ "%s:%d acl_get_flagset_np err (%s)"
+ "%s:%d acl_get_permset err (%s)"
+ "%s:%d acl_init err (%s)"
+ "%s:%d acl_set_file err (%s)"
+ "%s:%d acl_set_flagset_np err (%s)"
+ "%s:%d acl_set_tag_type err (%s)"
+ "%s:%d getxattr err (%s)"
+ "%s:%d removexattr err (%s)"
+ "%s:%d setxattr err (%s)"
+ "%s:%d uuid_parse err (%s)"
+ "ABCDEFAB-CDEF-ABCD-EFAB-CDEF0000000C"
+ "DI_IGNORE_ME (di->dev  %d) (dev %d) (flags 0x%x) (num_devices %d)"
+ "NO-UUID-UNKNOWN-DEVICE (di->dev  %d) (dev %d) (flags 0x%x) (num_devices %d)"
+ "com.apple.fsevents.last_pruned_event_id"
+ "com.apple.fsevents.previous_uuid"
+ "com.apple.fseventsd.daily"
+ "fsevents"
+ "fsevents.last_pruned_event_id"
+ "fsevents.previous_uuid"
+ "handle_device_config_xattr"
+ "historyPruning"
+ "no di found for dev %d (num_devices %d)"
+ "purge_history_policy"
+ "remove_uuid"
+ "set_xattr_acl"
+ "v16@?0^{_xpc_activity_s=}8"
- "%s: ([SET] previous_uuid) CFStringGetCString ERROR"
- "%s: CFPropertyListCreateWithStream done"
- "%s: CFPropertyListCreateWithStream err(%ld)"
- "%s: CFPropertyListWrite done"
- "%s: CFPropertyListWrite err(%ld)"
- "%s: CFReadStreamCreateWithFile error"
- "%s: CFWriteStreamCreateWithFile error"
- "%s: [GET] (last_pruned_event_id) CFStringGetCString ERROR"
- "%s: [GET] (previous_uuid) CFStringGetCString ERROR"
- "%s: [SET] (last_pruned_event_id) CFStringGetCString ERROR"
- "%s: load previous uuid"
- "%s: open_dprotected_np err(%s)"
- "%s: prev_uuid_cfstr == NULL"
- "%s: save previous uuid"
- "handle_device_config"
- "last_pruned_event_id"
- "previous_uuid"

```
