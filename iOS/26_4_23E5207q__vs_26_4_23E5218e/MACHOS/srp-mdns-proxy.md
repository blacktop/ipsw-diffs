## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2881.100.53.0.0
-  __TEXT.__text: 0x83468
+2881.100.56.0.0
+  __TEXT.__text: 0x837d8
   __TEXT.__auth_stubs: 0x1350
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x22c
   __TEXT.__const: 0x27a
-  __TEXT.__cstring: 0x7c62
-  __TEXT.__oslogstring: 0x11f61
+  __TEXT.__cstring: 0x7c80
+  __TEXT.__oslogstring: 0x11ef9
   __TEXT.__objc_classname: 0x38
   __TEXT.__objc_methname: 0x506
   __TEXT.__objc_methtype: 0x237
-  __TEXT.__unwind_info: 0x588
+  __TEXT.__unwind_info: 0x580
   __DATA_CONST.__auth_got: 0x9b0
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x10

   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C73E15F7-2CE3-337F-BED2-6F1AB106B889
+  UUID: E748BC75-DF50-3541-A24A-0A57DA29C4D8
   Functions: 454
   Symbols:   1135
-  CStrings:  2470
+  CStrings:  2472
 
Symbols:
+ __block_descriptor_tmp.1417
+ __block_descriptor_tmp.17.1503
+ __block_descriptor_tmp.18.1598
+ __block_descriptor_tmp.2620
+ __block_descriptor_tmp.8.1461
+ __block_literal_global.1504
- __block_descriptor_tmp.1410
- __block_descriptor_tmp.17.1496
- __block_descriptor_tmp.18.1591
- __block_descriptor_tmp.2613
- __block_descriptor_tmp.8.1454
- __block_literal_global.1497
Functions:
~ _adv_xpc_message : 9776 -> 9784
~ _adv_xpc_connection_delete : 1044 -> 1624
~ _adv_ctl_need_service_instance : 824 -> 1124
~ _dns_rdata_parse_data_ : 2036 -> 2028
CStrings:
+ "%{public}s: Unable to create service array"
+ "%{public}s: connection %p"
+ "%{public}s: connection %p for wanted service %{public}s.%{public}s freed."
+ "%{public}s: connection %p for wanted service %{public}s.%{public}s has dropped."
+ "%{public}s: found service = %p"
+ "%{public}s: out"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/adv-ctl-server.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/cti-services.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-client.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-proxy.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/ioloop.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/macos-ioloop.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/node-type-tracker.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/omr-watcher.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/probe-srp.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/service-publisher.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/service-tracker.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/srp-decompress.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/srp-mdns-proxy.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/srp-parse.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/state-machine.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/thread-device.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/thread-service.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/thread-tracker.c"
+ "/Library/Caches/com.apple.xbs/CB7FA062-4D93-4AAD-867B-D6A406B48A4D/TemporaryDirectory.Ie6kM6/Sources/mDNSResponderExtras/ServiceRegistration/tls-macos.c"
+ "01:37:42"
+ "Feb 16 2026"
+ "adv_ctl_need_service_instance"
- "%{public}s: adv_xpc_get_host_service: Unable to create reply dictionary."
- "%{public}s: adv_xpc_list_services: Unable to create reply dictionary."
- "%{public}s: adv_xpc_list_services: Unable to create service array"
- "%{public}s: adv_xpc_list_services: failed to allocate instance dictionary for %{private, mask.hash}s"
- "%{public}s: adv_xpc_message: Unable to create reply dictionary."
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/adv-ctl-server.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/cti-services.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-client.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-proxy.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/ioloop.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/macos-ioloop.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/node-type-tracker.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/omr-watcher.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/probe-srp.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/service-publisher.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/service-tracker.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/srp-decompress.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/srp-mdns-proxy.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/srp-parse.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/state-machine.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/thread-device.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/thread-service.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/thread-tracker.c"
- "/Library/Caches/com.apple.xbs/24B30AE4-77B3-46C3-8FAD-489D89885622/TemporaryDirectory.VkidpV/Sources/mDNSResponderExtras/ServiceRegistration/tls-macos.c"
- "21:52:41"
- "Jan 29 2026"

```
