## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2862.0.0.0.1
-  __TEXT.__text: 0x824a0
+2874.0.0.0.1
+  __TEXT.__text: 0x81eb4
   __TEXT.__auth_stubs: 0x1350
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x282
-  __TEXT.__cstring: 0x75ea
-  __TEXT.__oslogstring: 0x11be9
+  __TEXT.__cstring: 0x75e0
+  __TEXT.__oslogstring: 0x11d26
   __TEXT.__objc_classname: 0x38
   __TEXT.__objc_methname: 0x4e6
   __TEXT.__objc_methtype: 0x237

   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 94207CAA-A855-37C7-8C9B-43787362EFE6
+  UUID: 6425E48B-EA2F-3FA8-B431-434506C079AA
   Functions: 450
   Symbols:   1124
-  CStrings:  2439
+  CStrings:  2444
 
Symbols:
+ __block_descriptor_tmp.1333
+ __block_descriptor_tmp.17.1423
+ __block_descriptor_tmp.18.1517
+ __block_descriptor_tmp.2523
+ __block_descriptor_tmp.8.1380
+ __block_literal_global.1424
- __block_descriptor_tmp.1334
- __block_descriptor_tmp.17.1424
- __block_descriptor_tmp.18.1518
- __block_descriptor_tmp.2514
- __block_descriptor_tmp.8.1381
- __block_literal_global.1425
Functions:
~ _thread_device_rloc16_callback : 9512 -> 9524
~ _thread_device_stop : 9020 -> 5512
~ _dns_wire_parse_ : 2624 -> 2548
~ _omr_watcher_finalize : 836 -> 1140
~ _omr_watcher_netdata_mode_callback : 840 -> 2304
~ _service_publisher_re_advertise_matching : 1904 -> 2040
~ _service_publisher_can_publish : 1816 -> 1924
~ _service_publisher_service_unpublish : 328 -> 332
~ _service_publisher_action_publishing : 2920 -> 2960
CStrings:
+ "%{public}s: %{public}s %x%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s"
+ "%{public}s: callback %p context %p context_release %p %scanceled"
+ "%{public}s: host %{private, mask.hash}s has no address on current mesh-local prefix"
+ "%{public}s: new api"
+ "%{public}s: no anycast sequence number!"
+ "%{public}s: not all callbacks were canceled prior to releasing omr_watcher."
+ "%{public}s: old api"
+ "%{public}s: server_state->rloc16 updated to %x"
+ "01:39:10"
+ ": can publish"
+ ": can't publish"
+ "Jun 14 2025"
+ "service_publisher_publish"
- "%{public}s: %{public}s %{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s%{public}s"
- "%{public}s: server_state->rloc16 updated to %d"
- "00:42:26"
- "May 25 2025"
- "can publish"
- "can't publish"
- "omr_watcher_cancel"
- "omr_watcher_release_"

```
