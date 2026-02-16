## libdns_services.dylib

> `/usr/lib/libdns_services.dylib`

```diff

-2881.80.4.0.1
-  __TEXT.__text: 0xd4d4
+2881.100.53.0.0
+  __TEXT.__text: 0xdc80
   __TEXT.__auth_stubs: 0x5f0
   __TEXT.__objc_methlist: 0x13c
-  __TEXT.__const: 0x68
-  __TEXT.__oslogstring: 0xe44
-  __TEXT.__cstring: 0x1172
-  __TEXT.__unwind_info: 0x218
+  __TEXT.__const: 0x70
+  __TEXT.__oslogstring: 0xea0
+  __TEXT.__cstring: 0x11d8
+  __TEXT.__unwind_info: 0x208
   __TEXT.__objc_classname: 0x6c
   __TEXT.__objc_methname: 0x15b
   __TEXT.__objc_methtype: 0xb5

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4014F1C2-7453-36F3-8C5F-2FAF19972E35
+  UUID: 9C234106-BD08-381E-85A4-00B278F4D7AB
   Functions: 186
   Symbols:   498
   CStrings:  327
Symbols:
+ _adv_connection_call_callback
- _dnssd_svcb_service_name_is_empty
CStrings:
+ "/Library/Caches/com.apple.xbs/949508ED-541C-406C-A343-7E79C6C9DE59/TemporaryDirectory.8reSri/Sources/mDNSResponderServices/ServiceRegistration/adv-resolve.c"
+ "/Library/Caches/com.apple.xbs/949508ED-541C-406C-A343-7E79C6C9DE59/TemporaryDirectory.8reSri/Sources/mDNSResponderServices/ServiceRegistration/advertising_proxy_services.c"
+ "adv_event_handler (%s): (expected) reply callback after connection invalidated %p %p"
+ "adv_host_get_services_callback: number of instances doesn't match num_instances: %zu %zu"
+ "adv_ula_callback: error response code %d"
+ "advertising_proxy_start_dropping_push_connections"
+ "advertising_proxy_unblock_anycast_service"
+ "advertising_proxy_undrop_srpl_advertisement"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponderServices/ServiceRegistration/adv-resolve.c"
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponderServices/ServiceRegistration/advertising_proxy_services.c"
- "adv_event_handler (%s): no callback"
- "adv_event_handler (%s): spurious invalid callback %p %p"
- "adv_event_handler: no callback"
- "advertising_proxy_disable_start_dropping_push_connections"
- "advertising_proxy_disable_unblock_anycast_service"
- "advertising_proxy_disable_undrop_srpl_advertisement"

```
