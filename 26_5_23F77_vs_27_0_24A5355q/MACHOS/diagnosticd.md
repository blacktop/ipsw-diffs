## diagnosticd

> `/usr/libexec/diagnosticd`

```diff

-1861.120.4.0.0
-  __TEXT.__text: 0x8000
-  __TEXT.__auth_stubs: 0xf40
+1952.0.0.0.0
+  __TEXT.__text: 0x9dbc
+  __TEXT.__auth_stubs: 0x1080
   __TEXT.__objc_stubs: 0x460
   __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x470
-  __TEXT.__cstring: 0x1ad5
+  __TEXT.__const: 0x468
+  __TEXT.__cstring: 0x1d32
   __TEXT.__objc_methname: 0x33c
-  __TEXT.__objc_classname: 0x11
+  __TEXT.__objc_classname: 0xe
   __TEXT.__objc_methtype: 0x50
-  __TEXT.__unwind_info: 0x1a8
-  __DATA_CONST.__auth_got: 0x7a8
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x7b0
+  __TEXT.__unwind_info: 0x1f0
+  __DATA_CONST.__const: 0x8f0
   __DATA_CONST.__cfstring: 0x940
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x848
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0x100
   __DATA.__objc_selrefs: 0x138
   __DATA.__objc_ivar: 0x8

   __DATA.__os_assumes_log: 0x8
   __DATA.__data: 0x1a4
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1d0
+  __DATA.__bss: 0x1e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 7ACE841E-8019-3596-831C-8F7B5BA92175
-  Functions: 90
-  Symbols:   292
-  CStrings:  338
+  UUID: C46E4B3B-C2CB-33F2-816C-A219597D0CB1
+  Functions: 119
+  Symbols:   313
+  CStrings:  361
 
Symbols:
+ __os_trace_personas_in_oslog_enabled
+ __xpc_type_array
+ _dispatch_get_global_queue
+ _kpersona_info
+ _notify_register_dispatch
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x1
+ _os_map_128_clear
+ _os_map_128_count
+ _os_map_128_destroy
+ _os_map_128_find
+ _os_map_128_init
+ _os_map_128_insert
+ _os_map_32_clear
+ _os_map_32_destroy
+ _os_map_32_find
+ _os_map_32_init
+ _os_map_32_insert
+ _os_map_str_clear
+ _os_map_str_destroy
+ _os_map_str_entry
+ _os_map_str_find
+ _os_map_str_init
+ _os_map_str_insert
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _uuid_is_null
+ _xpc_array_apply
+ _xpc_dictionary_get_uuid
- __catalog_create
- __catalog_destroy
- __catalog_procinfo_create
- __catalog_procinfo_uuidinfo_add
- __catalog_procinfo_uuidinfo_remove
- __catalog_subchunk_procinfo_add
- __catalog_update_earliest_fhbuf_ts
- _objc_release
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "B20@?0I8^v12"
+ "B24@?0Q8^v16"
+ "B32@?0{os_map_128_key_s=[2Q]}8^v24"
+ "Cleared persona map due to persona generation change"
+ "Failed to register for persona generation notification: %u"
+ "Received persona generation change notification"
+ "Registered for persona generation change notifications"
+ "admin request %llu failed: %s"
+ "admin request %llu returned error: %s (%d)"
+ "com.apple.mobile.usermanagerd.personageneration_changed"
+ "error harvesting kernel uuid text: failed to send request"
+ "identifier"
+ "kernel_kext_uuids"
+ "kernel_shared_cache_uuid"
+ "kernel_subsystems"
+ "kext_load_addr"
+ "kext_load_size"
+ "kext_uuid"
+ "launch_persona_id"
+ "launch_persona_name"
+ "launch_persona_type"
+ "persona_id"
+ "persona_name"
+ "persona_type"
+ "v12@?0i8"
- "BUG IN LIBTRACE: Unexpected xpc object"
- "error harvesting kernel uuid text: %s"

```
