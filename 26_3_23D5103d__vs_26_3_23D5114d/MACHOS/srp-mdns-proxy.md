## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2881.80.3.0.0
-  __TEXT.__text: 0x836bc
+2881.80.4.0.1
+  __TEXT.__text: 0x83898
   __TEXT.__auth_stubs: 0x1340
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x27a
-  __TEXT.__cstring: 0x77ab
-  __TEXT.__oslogstring: 0x11fd8
+  __TEXT.__cstring: 0x7801
+  __TEXT.__oslogstring: 0x12009
   __TEXT.__objc_classname: 0x38
   __TEXT.__objc_methname: 0x4e6
   __TEXT.__objc_methtype: 0x237

   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C4EDB0A-919C-3388-9A00-479E053E5352
-  Functions: 453
-  Symbols:   1135
-  CStrings:  2470
+  UUID: 3FFFB1B6-ECEA-35E3-A12A-117337F7886E
+  Functions: 454
+  Symbols:   1136
+  CStrings:  2474
 
Symbols:
+ __block_descriptor_tmp.2611
+ _service_tracker_services_are_awaiting_removal
- __block_descriptor_tmp.2608
Functions:
~ _adv_ctl_thread_shutdown_status_check : 52 -> 92
~ _adv_ctl_start_thread_shutdown : 416 -> 604
~ _service_tracker_callback : 2816 -> 2808
+ _service_tracker_services_are_awaiting_removal
CStrings:
+ "%{public}s: no remaining services await removal."
+ "02:19:48"
+ "Jan 21 2026"
+ "awaiting removal"
+ "service_tracker_services_are_awaiting_removal"
+ "still awaiting removal"
- "21:51:05"
- "Dec 20 2025"

```
