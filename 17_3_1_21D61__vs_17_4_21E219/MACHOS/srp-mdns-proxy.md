## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2200.80.16.0.0
-  __TEXT.__text: 0x60afc
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_stubs: 0x100
-  __TEXT.__const: 0xb4
-  __TEXT.__cstring: 0x5bae
-  __TEXT.__oslogstring: 0xc013
-  __TEXT.__objc_methname: 0x7d
-  __TEXT.__unwind_info: 0x494
-  __DATA_CONST.__auth_got: 0x7a8
-  __DATA_CONST.__got: 0x1d8
+2200.100.94.0.2
+  __TEXT.__text: 0x63360
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__const: 0xc4
+  __TEXT.__cstring: 0x5dd9
+  __TEXT.__oslogstring: 0xc9fc
+  __TEXT.__objc_classname: 0x1
+  __TEXT.__unwind_info: 0x498
+  __DATA_CONST.__auth_got: 0x810
+  __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x750
+  __DATA_CONST.__const: 0x780
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x40
-  __DATA.__objc_classrefs: 0x30
-  __DATA.__data: 0x1a0
-  __DATA.__bss: 0x460
+  __DATA.__data: 0x1a8
+  __DATA.__bss: 0x768
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libipconfig.dylib
   - /usr/lib/libmdns.dylib
-  - /usr/lib/libobjc.A.dylib
-  Functions: 350
-  Symbols:   863
-  CStrings:  1760
+  - /usr/lib/libmrc.dylib
+  Functions: 359
+  Symbols:   878
+  CStrings:  1822
 
Symbols:
+ _CFArrayContainsValue
+ _CFArrayCreate
+ _CFDateFormatterCreate
+ _CFDateFormatterCreateStringWithDate
+ _CFStringGetCStringPtr
+ _DNSServiceUpdateRecord
+ _SCDynamicStoreCopyLocalHostName
+ _SCDynamicStoreCreate
+ _SCDynamicStoreKeyCreateHostNames
+ _SCDynamicStoreSetDispatchQueue
+ _SCDynamicStoreSetNotificationKeys
+ ___block_descriptor_40_e11_v16?0i8i12l
+ ___dnssd_client_service_publish_block_invoke
+ ___maskrune
+ ___stderrp
+ __block_descriptor_tmp.104
+ __block_descriptor_tmp.107
+ __block_descriptor_tmp.111
+ __block_descriptor_tmp.114
+ __block_descriptor_tmp.17.1096
+ __block_descriptor_tmp.185
+ __block_descriptor_tmp.466
+ __block_descriptor_tmp.74
+ __block_descriptor_tmp.78
+ __block_descriptor_tmp.8.1043
+ __block_descriptor_tmp.80
+ __block_descriptor_tmp.83
+ __block_descriptor_tmp.85
+ __block_descriptor_tmp.87
+ __block_descriptor_tmp.95
+ __block_descriptor_tmp.998
+ __block_literal_global.464
+ __cti_event_handler_block_invoke.113
+ __cti_log_object_block_invoke.84
+ __cti_log_object_block_invoke.93
+ __cti_log_object_block_invoke_2.86
+ __cti_log_object_block_invoke_2.96
+ __init_connection_block_invoke.73
+ _dns_proxy_input_for_server
+ _dns_rdata_dump_to_buf
+ _dns_txt_data_print
+ _fprintf
+ _ioloop_normalize_address
+ _ioloop_read_source_cancel_callback
+ _local_host_name
+ _local_host_name_dot_local
+ _mdns_address_create_ipv6
+ _mdns_dns_service_definition_add_domain
+ _mdns_dns_service_definition_append_server_address
+ _mdns_dns_service_definition_create
+ _mdns_domain_name_create
+ _mdns_release
+ _monitor_name_changes_callback
+ _mrc_dns_service_registration_activate
+ _mrc_dns_service_registration_create
+ _mrc_dns_service_registration_invalidate
+ _mrc_dns_service_registration_set_event_handler
+ _mrc_dns_service_registration_set_queue
+ _mrc_release
+ _my_name
+ _my_name_buf
+ _probe_srp_probe_state_context_release
+ _sc_dynamic_store_key_host_name
+ _served_domain_process_name_change
+ _srp_dump_server_stats
+ _srp_parse_client_updates_free_
+ _strncmp
+ _update_my_name
- _OBJC_CLASS_$_NEPolicy
- _OBJC_CLASS_$_NEPolicyCondition
- _OBJC_CLASS_$_NEPolicyResult
- _OBJC_CLASS_$_NEPolicySession
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSUUID
- ___cti_event_handler_block_invoke_2
- ___init_connection_block_invoke_2
- __block_descriptor_tmp.103
- __block_descriptor_tmp.110
- __block_descriptor_tmp.112
- __block_descriptor_tmp.17.1072
- __block_descriptor_tmp.174
- __block_descriptor_tmp.444
- __block_descriptor_tmp.73
- __block_descriptor_tmp.77
- __block_descriptor_tmp.79
- __block_descriptor_tmp.8.1019
- __block_descriptor_tmp.82
- __block_descriptor_tmp.84
- __block_descriptor_tmp.86
- __block_descriptor_tmp.94
- __block_descriptor_tmp.97
- __block_descriptor_tmp.974
- __block_literal_global.442
- __cti_log_object_block_invoke.83
- __cti_log_object_block_invoke.92
- __cti_log_object_block_invoke_2.85
- __cti_log_object_block_invoke_2.95
- _dso_send_formerr
- _ioloop_read_cancel
- _nw_resolver_config_add_name_server
- _nw_resolver_config_create
- _nw_resolver_config_publish
- _nw_resolver_config_set_class
- _nw_resolver_config_set_identifier
- _nw_resolver_config_set_protocol
- _objc_alloc
- _objc_alloc_init
- _objc_msgSend
- _objc_msgSend$addPolicy:
- _objc_msgSend$apply
- _objc_msgSend$arrayWithObjects:count:
- _objc_msgSend$domain:
- _objc_msgSend$getUUIDBytes:
- _objc_msgSend$initWithOrder:result:conditions:
- _objc_msgSend$netAgentUUID:
- _objc_msgSend$setPriority:
- _objc_release_x20
- _objc_release_x21
- _objc_release_x8
- _probe_srp_connection_finalize
- _srp_parse_client_updates_free
CStrings:
+ " %04x"
+ " live"
+ " update-pending"
+ "%s\n"
+ "%s.local."
+ "%{public}s:   %{public}s instance %{private, mask.hash}s %{private, mask.hash}s %d (%{private, mask.hash}s)"
+ "%{public}s:   IN    A %{private, mask.hash, network:in_addr}.4P%{private, mask.hash}s"
+ "%{public}s:   IN AAAA %{public}s%{private, mask.hash, network:in6_addr}.16P%{private, mask.hash}s"
+ "%{public}s: %p at %{public}s:%d"
+ "%{public}s: %{public}s my_name: %{private, mask.hash}s, local host name: %{private, mask.hash}s"
+ "%{public}s: %{public}s%d hosts (%d matter, %d hap), %d instances, %d a records, %d aaaa records at %.6lf"
+ "%{public}s: CFStringGetCString failed - local host name: %{private, mask.hash}s"
+ "%{public}s: DNS service registration gracefully invalidated"
+ "%{public}s: DNS service registration interrupted"
+ "%{public}s: DNS service registration invalidated with error: %d"
+ "%{public}s: DNS service registration started"
+ "%{public}s: DNSServiceUpdateRecord failed to update NS record to new name - name: %{private, mask.hash}s"
+ "%{public}s: Rotating the expired TLS certificate - creation date: %s, now: %s, elapsed: %lf."
+ "%{public}s: SCDynamicStoreSetDispatchQueue failed"
+ "%{public}s: SCDynamicStoreSetNotificationKeys failed"
+ "%{public}s: SecKeyCreateRandomKey failed to create private key - error description: %s."
+ "%{public}s: SecKeyVerifySignature failed to validate - Error Description: %s"
+ "%{public}s: Start to monitor local host name changes"
+ "%{public}s: Updating record - new NS record rdata: %{private, mask.hash}s"
+ "%{public}s: [CX%d] %{public}s"
+ "%{public}s: [CX%d] %{public}s(%{public}s): %{public}s%{public}s%{public}s %{public}s"
+ "%{public}s: [CX%d] %{public}s(%{public}s): %{public}s%{public}s%{public}s %{public}s%{public}s%{public}s"
+ "%{public}s: [CX%d] %{public}s(%{public}s): %{public}s%{public}s%{public}s %{public}s%{public}s: %{public}s%{public}s"
+ "%{public}s: [CX%d] %{public}s(%{public}s): %{public}s%{public}s%{public}s + %{public}s%{public}s"
+ "%{public}s: [CX%d] %{public}s(%{public}s): %{public}s%{public}s%{public}s +%{public}s%{public}s"
+ "%{public}s: [CX%d] %{public}s(%{public}s): %{public}s%{public}s%{public}s +%{public}s: %{public}s%{public}s"
+ "%{public}s: [CX%d] (%{public}s): cleanup"
+ "%{public}s: [CX%d] No callback"
+ "%{public}s: [CX%d] No node type returned."
+ "%{public}s: [CX%d] calling callback for %p"
+ "%{public}s: [CX%d] canceling connection %p"
+ "%{public}s: [CX%d] canceling xpc connection %p"
+ "%{public}s: [CX%d] conn_ref = %p"
+ "%{public}s: [CX%d] cti_event_handler(%{public}s): no memory, canceling %p."
+ "%{public}s: [CX%d] cti_event_handler: Unexpected Connection Error [%{public}s]"
+ "%{public}s: [CX%d] cti_internal_tunnel_reply_callback: nonzero result %llu"
+ "%{public}s: [CX%d] no memory"
+ "%{public}s: [CX%d] node type type is %{public}s instead of string."
+ "%{public}s: [CX%d] not calling callback for %p"
+ "%{public}s: [CX%d] releasing connection %p"
+ "%{public}s: [CX%d] sending message on connection %p"
+ "%{public}s: [CX%d] services array not present in Thread:Services event."
+ "%{public}s: [CX%d] xpc connection: %p"
+ "%{public}s: couldn't append server address to service definition"
+ "%{public}s: datagram from %{private, mask.hash}s on port %d xid %x (question xid %x) rcode %d"
+ "%{public}s: datagram from {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P} on port %d xid %x (question xid %x) rcode %d"
+ "%{public}s: failed to create CFArrayRef for monitored keys"
+ "%{public}s: failed to create SCDynamicStoreKey for host name"
+ "%{public}s: failed to create SCDynamicStoreRef"
+ "%{public}s: failed to create address object"
+ "%{public}s: failed to create domain name for default.service.arpa.: %d\n"
+ "%{public}s: failed to get updated local host name"
+ "%{public}s: failed to monitor name changes"
+ "%{public}s: failed to update my name"
+ "%{public}s: failed to update myname"
+ "%{public}s: generated name too long: %{public}s.home.arpa."
+ "%{public}s: have_srp_listener is true but there's no listener!"
+ "%{public}s: host %{private, mask.hash}s key_id %xu stable %llx lease %d key_lease %d expiry %d%{public}s%{public}s"
+ "%{public}s: host update for %{private, mask.hash}s, key id %x %{public}s (skipped xid%{public}s%{public}s)"
+ "%{public}s: initialize_my_name_and_monitoring failed"
+ "%{public}s: invalid DNS name - name: %{public}s"
+ "%{public}s: io %p fd %d, read source %p, write_source %p"
+ "%{public}s: io->fd has been set to -1 too early"
+ "%{public}s: my_name is not set"
+ "%{public}s: not sending response."
+ "%{public}s: sending %zd byte UDP response from %{private, mask.hash, network:in_addr}.4P port %d index %d to %{private, mask.hash, network:in_addr}.4P#%d"
+ "%{public}s: sending %zd byte UDP response from {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P} port %d index %d to {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}#%d"
+ "%{public}s: snprintf failed - name length: %lu, max: %lu"
+ "%{public}s: something else"
+ "%{public}s: unable to allocate mdns_dns_service_definition object"
+ "%{public}s: unable to create client DNS service registration"
+ "%{public}s: update contains multiple key ids %x and %x"
+ "%{public}s: update for %{private, mask.hash}s #%d, xid %x validates, lease time %d, receive_time %{public}s, remote %{private, mask.hash}s -> %p."
+ ".home.arpa."
+ "/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-client.c"
+ "22:55:54"
+ "Feb 16 2024"
+ "_hap._udp"
+ "_matter"
+ "after update, "
+ "cti_events_discontinue"
+ "cti_internal_reply_callback"
+ "cti_internal_state_reply_callback"
+ "dns_proxy_input_for_server"
+ "dns_registration_invalidated"
+ "dnssd-proxy:watch for name change events"
+ "dnssd_client_dns_service_event_handler"
+ "initialize_my_name_and_monitoring"
+ "ioloop_close"
+ "ioloop_read_source_cancel_callback"
+ "live"
+ "lo0"
+ "localhost."
+ "monitor_name_changes"
+ "monitor_name_changes_callback"
+ "probe_srp_probe_state_context_release"
+ "rrtype: %u  qclass: %u  name: %s %s\n"
+ "s"
+ "srp_dump_server_stats"
+ "srp_parse_client_updates_free_"
+ "stale"
+ "unregistered"
+ "update_my_name"
+ "updated"
+ "v16@?0i8i12"
- "%{public}s: %{private, mask.hash}s is not in default.service.arpa, or no replacement zone (%p)"
- "%{public}s: %{public}s(%{public}s): %{public}s%{public}s%{public}s %{public}s"
- "%{public}s: %{public}s(%{public}s): %{public}s%{public}s%{public}s %{public}s%{public}s%{public}s"
- "%{public}s: %{public}s(%{public}s): %{public}s%{public}s%{public}s %{public}s%{public}s: %{public}s%{public}s"
- "%{public}s: %{public}s(%{public}s): %{public}s%{public}s%{public}s + %{public}s%{public}s"
- "%{public}s: %{public}s(%{public}s): %{public}s%{public}s%{public}s +%{public}s%{public}s"
- "%{public}s: %{public}s(%{public}s): %{public}s%{public}s%{public}s +%{public}s: %{public}s%{public}s"
- "%{public}s: (%{public}s): cleanup"
- "%{public}s: Failed to register resolver"
- "%{public}s: No callback"
- "%{public}s: Not calling callback."
- "%{public}s: Registered resolver at %{private, mask.hash}s uuid %{uuid_t}.16P"
- "%{public}s: Rotating the expired TLS certificate - creation date: %@, now: %@, elapsed: %lf."
- "%{public}s: SecKeyCreateRandomKey failed to create private key - error description: %@."
- "%{public}s: SecKeyVerifySignature failed to validate - Error Description: %@"
- "%{public}s: after update, %d hosts, %d instances, %d a records, %d aaaa records"
- "%{public}s: conn_ref = %p"
- "%{public}s: cti_event_handler(%{public}s): no memory."
- "%{public}s: cti_event_handler: Unexpected Connection Error [%{public}s]"
- "%{public}s: cti_internal_network_node_type_callback: No node type returned."
- "%{public}s: cti_internal_network_node_type_callback: node type type is %{public}s instead of string."
- "%{public}s: cti_internal_tunnel_reply_callback: nonzero result %llu"
- "%{public}s: datagram from {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P} on port %d xid %x (question xid %x)"
- "%{public}s: failed to start TCP listener - listener index: %d"
- "%{public}s: failed to start UDP listener - listener index: %d"
- "%{public}s: sending %zd byte UDP response to %{private, mask.hash, network:in_addr}.4P#%d"
- "%{public}s: sending %zd byte UDP response to {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}#%d"
- "%{public}s: sending UDP response from %{private, mask.hash, network:in_addr}.4P#%d"
- "%{public}s: sending UDP response from {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}#%d"
- "%{public}s: services array not present in Thread:Services event."
- "%{public}s: start_dnssd_proxy_listener failed"
- "%{public}s: update for %{private, mask.hash}s #%d, xid %x validates, lease time %d, receive_time %{public}s, remote %{private, mask.hash}s."
- "/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-client.m"
- "20:02:37"
- "DNS UDP Listener"
- "Dec 20 2023"
- "TCP DNS Listener"
- "addPolicy:"
- "apply"
- "arrayWithObjects:count:"
- "dns_proxy_input"
- "domain:"
- "getUUIDBytes:"
- "initWithOrder:result:conditions:"
- "localhost"
- "netAgentUUID:"
- "probe_srp_connection_finalize"
- "setPriority:"

```
