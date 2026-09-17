## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3111.0.5.0.1
-  __TEXT.__text: 0x8e320
+3111.40.40.0.0
+  __TEXT.__text: 0x8e37c
   __TEXT.__auth_stubs: 0x14f0
   __TEXT.__const: 0x2f5
-  __TEXT.__cstring: 0x9120
-  __TEXT.__oslogstring: 0x14128
+  __TEXT.__cstring: 0x91d2
+  __TEXT.__oslogstring: 0x14112
   __TEXT.__unwind_info: 0x848
   __TEXT.__eh_frame: 0x7c
   __DATA_CONST.__const: 0x920

   - /usr/lib/libsqlite3.dylib
   Functions: 481
   Symbols:   1120
-  CStrings:  2603
+  CStrings:  2607
 
Symbols:
+ _thread_service_note_function
- _thread_service_note
Functions:
~ _dnssd_client_action_probing : 3080 -> 3096
~ _dnssd_client_service_unpublish : 68 -> 76
~ _thread_service_note -> _thread_service_note_function : 1168 -> 1132
~ _adv_ctl_start_thread_shutdown : 592 -> 608
~ _service_tracker_callback : 3020 -> 3048
~ _service_tracker_services_are_awaiting_removal : 256 -> 264
~ _service_publisher_have_competing_unicast_service : 484 -> 512
~ _service_publisher_anycast_service_present : 132 -> 144
~ _service_publisher_stale_service_present : 256 -> 272
~ _service_publisher_queue_run : 1488 -> 1496
~ _service_publisher_update_callback : 1756 -> 1744
CStrings:
+ "%{public}s: could not parse u32 (%u bytes were available)"
+ "dnssd_client_service_unpublish"
+ "service_publisher_anycast_service_present"
+ "service_publisher_have_competing_unicast_service"
+ "service_publisher_stale_service_present"
+ "service_tracker_thread_service_note"
- "%{public}s: service TLV value must be at least 6 bytes long (was %u bytes long)"
- "thread_service_note"
```
