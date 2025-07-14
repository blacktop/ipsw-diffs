## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2200.100.94.0.2
-  __TEXT.__text: 0x63360
-  __TEXT.__auth_stubs: 0x1020
+2200.120.24.0.0
+  __TEXT.__text: 0x64a38
+  __TEXT.__auth_stubs: 0x1010
   __TEXT.__const: 0xc4
-  __TEXT.__cstring: 0x5dd9
-  __TEXT.__oslogstring: 0xc9fc
+  __TEXT.__oslogstring: 0xcb0e
+  __TEXT.__cstring: 0x5e34
   __TEXT.__objc_classname: 0x1
   __TEXT.__unwind_info: 0x498
-  __DATA_CONST.__auth_got: 0x810
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_got: 0x808
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x780
   __DATA_CONST.__cfstring: 0x140

   - /usr/lib/libipconfig.dylib
   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
-  UUID: 4189B94C-47AE-3E4A-879B-C567E42D58AF
+  UUID: 7D1346ED-EAE8-3064-AEBD-256B9C243B9A
   Functions: 359
-  Symbols:   878
-  CStrings:  1832
+  Symbols:   876
+  CStrings:  1839
 
Symbols:
+ ___ioloop_listener_create_block_invoke_2
+ ___probe_srp_create_block_invoke
+ __block_descriptor_tmp.17.1097
+ __block_descriptor_tmp.22
+ __block_descriptor_tmp.27
+ __block_descriptor_tmp.36.1216
+ __block_descriptor_tmp.39
+ __block_descriptor_tmp.45
+ __block_descriptor_tmp.48
+ __block_descriptor_tmp.50
+ __block_descriptor_tmp.57
+ __block_descriptor_tmp.59
+ __block_descriptor_tmp.62
+ __block_descriptor_tmp.8.1044
+ __block_descriptor_tmp.999
+ __ioloop_connection_create_block_invoke.26
+ _dnssd_client_release_
+ _dp_query_context_release
+ _probe_srp_create
+ _served_domain_free
+ _service_publisher_release_
+ _srp_adv_host_context_release
+ _thread_service_release_
+ _thread_service_retain_
- ___probe_state_create_block_invoke
- ___stderrp
- __block_descriptor_tmp.17.1096
- __block_descriptor_tmp.23
- __block_descriptor_tmp.28
- __block_descriptor_tmp.37
- __block_descriptor_tmp.40
- __block_descriptor_tmp.46
- __block_descriptor_tmp.49
- __block_descriptor_tmp.51
- __block_descriptor_tmp.58
- __block_descriptor_tmp.60
- __block_descriptor_tmp.65
- __block_descriptor_tmp.8.1043
- __block_descriptor_tmp.998
- __ioloop_connection_create_block_invoke.27
- __ioloop_listener_create_block_invoke.21
- _cti_internal_string_event_reply
- _delete_served_domain
- _dns_rdata_dump_to_buf
- _dnssd_client_release
- _fprintf
- _probe_state_create
- _service_publisher_release
- _thread_service_release
- _thread_service_retain
CStrings:
+ " is still being probed"
+ "%{public}s: %s for %s when no subscription exists."
+ "%{public}s: %s for %s when subscription already exists."
+ "%{public}s: %{public}s for %{public}s."
+ "%{public}s: [DSO%d] not replying from cache for %{private, mask.hash}s %d %d"
+ "%{public}s: [DSO%d] replying from cache for %{private, mask.hash}s %d %d"
+ "%{public}s: data region %zd:%zd is out of range for message length %d"
+ "%{public}s: invalid service type %d on service %p"
+ "%{public}s: oversized datagram length %zd"
+ "%{public}s: unable to allocate message."
+ "%{public}s: update for host %{private, mask.hash}s which has been deleted."
+ "22:56:37"
+ "Apr 16 2024"
+ "dnssd_client_release_"
+ "dp_query_context_release"
+ "node_type_tracker_release_"
+ "probe_srp_create"
+ "served_domain_free"
+ "service_publisher_release_"
+ "service_tracker_release_"
+ "service_tracker_unverified_service_get returning %p"
+ "srp_adv_host_context_release"
+ "thread_service_release_"
+ "thread_service_retain_"
+ "thread_tracker_release_"
- "%s\n"
- "%{public}s: datagram_read: %{public}s"
- "%{public}s: datagram_read: data region %zd:%zd is out of range for message length %d"
- "%{public}s: datagram_read: oversized datagram length %zd"
- "%{public}s: datagram_read: unable to allocate message."
- "%{public}s: dso_message: %s for %s when no subscription exists."
- "00:49:04"
- "Mar  9 2024"
- "delete_served_domain"
- "dnssd_client_release"
- "node_type_tracker_release"
- "probe_state_create"
- "rrtype: %u  qclass: %u  name: %s %s\n"
- "service_publisher_release"
- "service_tracker_release"
- "thread_service_release"
- "thread_service_retain"
- "thread_tracker_release"

```
