## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2559.80.8.0.0
-  __TEXT.__text: 0x74d80
-  __TEXT.__auth_stubs: 0x11f0
-  __TEXT.__cstring: 0x6cf2
+2600.100.147.0.0
+  __TEXT.__text: 0x756b8
+  __TEXT.__auth_stubs: 0x1220
   __TEXT.__const: 0x20b
-  __TEXT.__oslogstring: 0xef12
+  __TEXT.__cstring: 0x6e73
+  __TEXT.__oslogstring: 0xf71a
   __TEXT.__objc_classname: 0x1
-  __TEXT.__unwind_info: 0x520
-  __TEXT.__eh_frame: 0x74
-  __DATA_CONST.__auth_got: 0x8f8
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__auth_ptr: 0x10
+  __TEXT.__unwind_info: 0x500
+  __TEXT.__eh_frame: 0xb4
+  __DATA_CONST.__auth_got: 0x910
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0x820
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x1c8
-  __DATA.__bss: 0x7d0
+  __DATA.__bss: 0x7e0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Network.framework/Versions/A/Network

   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6D3B52A8-B616-300F-88C9-7238939F7893
-  Functions: 409
-  Symbols:   977
-  CStrings:  2070
+  UUID: EEF5BE4F-D936-38F3-AF95-36AA62D710FF
+  Functions: 395
+  Symbols:   984
+  CStrings:  2101
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __block_descriptor_tmp.1114
+ __block_descriptor_tmp.21
+ __block_descriptor_tmp.24
+ __block_descriptor_tmp.502
+ __block_descriptor_tmp.8.1159
+ __block_literal_global.1218
+ __block_literal_global.500
+ __isPlatformVersionAtLeast.cold.1
+ __isPlatformVersionAtLeast.cold.2
+ _adv_ctl_update_primary_resident
+ _dnssd_proxy_ifaddr_callback
+ _freeifaddrs
+ _getifaddrs
+ _interface_addresses
+ _ioctl
+ _ioloop_dnssd_txn_retain_
+ _srp_mdns_cancel_previous_instance
+ _srp_mdns_cancel_previous_record
- _DNSServiceUpdateRecordInternal
- __block_descriptor_tmp.1090
- __block_descriptor_tmp.21.1206
- __block_descriptor_tmp.24.1207
- __block_descriptor_tmp.501
- __block_descriptor_tmp.8.1135
- __block_literal_global.1194
- __block_literal_global.499
- _service_publisher_start_wait
- _srp_host_record_retry_callback
- _srp_instance_retry_callback
- _thread_device_startup
- _update_instance_tsr
CStrings:
+ "\n%p %s ("
+ "    new"
+ "   kept"
+ "%02x:%02x:%02x:%02x:%02x:%02x"
+ "%{public}s: %{public}s IN A %{private, mask.hash, network:in_addr}.4P %{public}s"
+ "%{public}s: %{public}s address from the served domain - domain: %{private, mask.hash}s"
+ "%{public}s: %{public}s cancelling previous registration for service %{private, mask.hash}s.%{private, mask.hash}s.%{private, mask.hash}s -> %{private, mask.hash}s"
+ "%{public}s: %{public}s previous registration for service %{private, mask.hash}s.%{private, mask.hash}s.%{private, mask.hash}s -> %{private, mask.hash}s got code %d"
+ "%{public}s: %{public}s: previous registration for host %{private, mask.hash}s address %{private, mask.hash, network:in_addr}.4P%{public}s%{public}s."
+ "%{public}s: %{public}s: previous registration for host %{private, mask.hash}s address {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}%{public}s%{public}s."
+ "%{public}s: %{public}s: previous registration for host %{private, mask.hash}s key %{public}s%{public}s."
+ "%{public}s: %{public}s: registration for host %{private, mask.hash}s unknown record type %d%{public}s%{public}s."
+ "%{public}s: %{public}s:%{public}s"
+ "%{public}s: A address and mask are not in the same sa_family - address family: %d, mask family: %d"
+ "%{public}s: B address and mask are no in the same sa_family - address family: %d, mask family: %d"
+ "%{public}s: Client uid %d pid %d sent a kDNSSDAdvertisingProxyUpdatePrimaryResident request."
+ "%{public}s: DNS push %{public}s parse from %{private, mask.hash}s failed: length mismatch (%d != %d)"
+ "%{public}s: Fatal: sizeof (*dso)[%zu], outsize[%zu], namespace[%zu]"
+ "%{public}s: Interface %{public}s address %{private, mask.hash, network:in_addr}.4P mask %{private, mask.hash, network:in_addr}.4P index %d %{public}s"
+ "%{public}s: Interface %{public}s address %{public}s%{private, mask.hash, network:in6_addr}.16P mask %{public}s%{private, mask.hash, network:in6_addr}.16P index %d %{public}s"
+ "%{public}s: Interface %{public}s address type %d index %d %{public}s"
+ "%{public}s: New served domain created and hardwired response created - domain: %{private, mask.hash}s"
+ "%{public}s: Removing served domain with 0 address - domain: %{private, mask.hash}s, interface name: %{public}s"
+ "%{public}s: [DSO%d] DSO Message (Primary TLV=%d) (xid=%x) received from %{private, mask.hash}s"
+ "%{public}s: [DSO%d][TRK%d] RR parse for %{private, mask.hash}s from %{public}s failed"
+ "%{public}s: [DSO%d][TRK%d] push subscribe with zero xid received from %{private, mask.hash}s(opcode %{public}s)"
+ "%{public}s: [QU%d] DNSServiceQueryRecord failed for '%{private, mask.hash}s': %d"
+ "%{public}s: [QU%d] question name %{private, mask.hash}s is too long for %{private, mask.hash}s."
+ "%{public}s: [QU%d] question name %{private, mask.hash}s is too long for .local."
+ "%{public}s: address added/removed successfully - event: %{public}s"
+ "%{public}s: address not found in the interface address list - interface name: %{public}s"
+ "%{public}s: adv_proxy_enable: unable to allocate srp_wanted structure."
+ "%{public}s: calloc failed - allocated size: %lu"
+ "%{public}s: calloc failed - allocated size: %zu"
+ "%{public}s: failed to %{public}s new interface address"
+ "%{public}s: failed to add new served domain - interface name: %{public}s"
+ "%{public}s: failed to setup hardwired response for newly created served domain - domain: %{private, mask.hash}s"
+ "%{public}s: forgotten rref"
+ "%{public}s: getifaddrs failed: %{public}s"
+ "%{public}s: ignoring non IP address"
+ "%{public}s: ioctl(SIOCGIFAFLAG_IN6): %{public}s"
+ "%{public}s: local address %{private, mask.hash, network:in_addr}.4P is not seen as present on any known interface."
+ "%{public}s: local address {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P} is not seen as present on any known interface."
+ "%{public}s: matched %{public}s"
+ "%{public}s: new IPv4 interface address added - ifname: %{public}s, addr: %{private, mask.hash, network:in_addr}.4P"
+ "%{public}s: new IPv6 interface address added - ifname: %{public}s, addr: {%{public}s%{private, mask.hash, srp:in6_addr_segment}.6P:%{public, mask.hash, srp:in6_addr_segment}.2P:%{private, mask.hash, srp:in6_addr_segment}.8P}"
+ "%{public}s: new link-layer address not dropped because %{private, mask.hash}s - ifname: %{public}s, addr: %{private, mask.hash, srp:mac_addr}.6P"
+ "%{public}s: new link-layer interface address dropped - ifname: %{public}s, addr: %{private, mask.hash, srp:mac_addr}.6P"
+ "%{public}s: null record"
+ "%{public}s: registration for service %{private, mask.hash}s.%{private, mask.hash}s.%{private, mask.hash}s -> %{private, mask.hash}s has completed under %{private, mask.hash}s.%{private, mask.hash}s%{private, mask.hash}s"
+ "%{public}s: removing %{public}s %p %p"
+ "%{public}s: shutdown request unexpectedly NULL here."
+ "%{public}s: socket(AF_INET6, SOCK_DGRAM): %{public}s"
+ "%{public}s: unexpected post-update success for instance %{private, mask.hash}s (%{private, mask.hash}s %{private, mask.hash}s %{private, mask.hash}s)"
+ "%{public}s: update primary resident to %{public}s"
+ ", result code = %d"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/adv-ctl-server.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/cti-services.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-client.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-proxy.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/ioloop.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/macos-ioloop.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/node-type-tracker.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/probe-srp.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/service-publisher.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/service-tracker.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/srp-mdns-proxy.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/srp-parse.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/state-machine.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/thread-device.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/thread-service.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/thread-tracker.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/tls-macos.c"
+ "07:19:53"
+ "Adding"
+ "Mar  8 2025"
+ "Removing"
+ "added"
+ "adv_ctl_update_primary_resident"
+ "adv_instance_state %d %d %d %d|"
+ "adv_proxy_wanted"
+ "adv_service_state %d %d %d %d|"
+ "advertising_proxy_subscription %d %d %d %d|"
+ "cache"
+ "current rref"
+ "deleted"
+ "dnssd_clientstub CallbackWithError called with bad op %u"
+ "dnssd_clientstub DNSServiceProcessResult daemon version %u does not match client version %d"
+ "dnssd_clientstub DNSServiceRegisterRecord called with non-DNSServiceCreateConnection DNSServiceRef %p %u"
+ "dnssd_clientstub kDNSServiceFlagsShareConnection used with invalid DNSServiceRef %p %08X %08X op %u"
+ "dnssd_proxy_find_usable_interface_address"
+ "dnssd_proxy_ifaddr_callback"
+ "ended"
+ "interface_add_new_address"
+ "interface_addr_t_equal"
+ "interface_process_addr_change"
+ "interface_remove_old_address"
+ "ioloop_dnssd_txn_retain_"
+ "ioloop_map_interface_addresses_here_"
+ "local host IPv4 address matching interface"
+ "local host IPv6 address matching interface"
+ "no memory for stale service to unpublish"
+ "previous rref"
+ "primary"
+ "register"
+ "srp_mdns_cancel_previous_instance"
+ "srp_mdns_cancel_previous_record"
+ "threadsim_network_state %d %d %d %d|"
+ "threadsim_node_state %d %d %d %d|"
+ "update primary resident"
- " completed with conflict."
- " with a conflict"
- "${DaemonNameOrIdentifierHere}"
- "%{public}s: %{private, mask.hash}s (%p): failed to update TSR, re-registering"
- "%{public}s: DNS push %{public}s parse from %s failed: length mismatch (%d != %d)"
- "%{public}s: DNSServiceUpdateRecord TSR for %{private, mask.hash}s set to %{public}s (record %p rref %p)"
- "%{public}s: DNSServiceUpdateRecord for %{private, mask.hash}s, TSR set to %{public}s (instance %p sdref %p)"
- "%{public}s: DNSServiceUpdateRecord for instance %{private, mask.hash}s TXT record failed: %d (instance %p)"
- "%{public}s: DNSServiceUpdateRecord for instance %{private, mask.hash}s, TSR failed: %d (instance %p sdref %p)"
- "%{public}s: DNSServiceUpdateRecordWithAttribute for host tsr failed: %d (record %p rref %p)"
- "%{public}s: Fatal: sizeof (*dso)[%zd], outsize[%zd], namespace[%zd]"
- "%{public}s: [DSO%d] DSO Message (Primary TLV=%d) received from %{private, mask.hash}s"
- "%{public}s: [DSO%d][TRK%d] RR parse for %s from %s failed"
- "%{public}s: [QU%d] DNSServiceQueryRecord failed for '%s': %d"
- "%{public}s: [QU%d] question name %s is too long for %s."
- "%{public}s: [QU%d] question name %s is too long for .local."
- "%{public}s: already scheduled attempt to reregister record %p"
- "%{public}s: instance %{private, mask.hash}s (%p) shared connection (%lx) is stale, re-registering"
- "%{public}s: instance %{private, mask.hash}s (%p) tsr update failed, re-registering"
- "%{public}s: no longer updating host %p because host is no longer valid."
- "%{public}s: no longer updating instance %p because host is no longer valid."
- "%{public}s: null rref"
- "%{public}s: re-registering host record %p."
- "%{public}s: re-registering updating instance %p."
- "%{public}s: re-update succeeded for instance %{private, mask.hash}s (%{private, mask.hash}s %{private, mask.hash}s %{private, mask.hash}s)"
- "%{public}s: record->host[%p], record->rref[%p] when we update host TSR."
- "%{public}s: registration for service %{private, mask.hash}s.%{private, mask.hash}s.%{private, mask.hash}s -> %{private, mask.hash}s has completed%{public}s."
- "%{public}s: registration is under %{private, mask.hash}s.%{private, mask.hash}s%{private, mask.hash}s"
- "%{public}s: removing rref %p"
- "%{public}s: sdref is NULL when updating instance TSR."
- "%{public}s: shared_txn is NULL when we update host TSR."
- "%{public}s: shared_txn->sdref is NULL when we update host TSR."
- "%{public}s: skipping DNSServiceUpdateRecord for instance %{private, mask.hash}s TSR (instance %p)"
- "%{public}s: starting wakeup timer to publish cached services after stale service timeout."
- "%{public}s: txn is NULL updating instance TSR."
- "%{public}s: unable to allocate srp_wanted structure."
- "%{public}s: unable to make wakeup &host->re_register_wakeup"
- "%{public}s: unable to make wakeup &instance->retry_wakeup"
- "%{public}s: updated TXT record for %{private, mask.hash}s . %{private, mask.hash}s (instance %p sdref %p)."
- "%{public}s: we got a bad reference error: why?"
- "%{public}s: will attempt to reregister instance %p in %.3lf seconds"
- "%{public}s: will attempt to reregister record %p in %.3lf seconds"
- "%{public}s: will not attempt to reregister record %p"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/adv-ctl-server.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/cti-services.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-client.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/dnssd-proxy.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/ioloop.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/macos-ioloop.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/node-type-tracker.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/probe-srp.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/service-publisher.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/service-tracker.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/srp-mdns-proxy.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/srp-parse.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/state-machine.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/thread-device.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/thread-service.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/thread-tracker.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/mDNSResponderExtras/ServiceRegistration/tls-macos.c"
- "00:26:28"
- ":"
- "Dec 14 2024"
- "dnssd_clientstub CallbackWithError called with bad op %d"
- "dnssd_clientstub DNSServiceProcessResult daemon version %d does not match client version %d"
- "dnssd_clientstub DNSServiceRegisterRecord called with non-DNSServiceCreateConnection DNSServiceRef %p %d"
- "dnssd_clientstub DNSServiceRemoveRecord called with NULL DNSRecordRef"
- "dnssd_clientstub kDNSServiceFlagsShareConnection used with invalid DNSServiceRef %p %08X %08X op %d"
- "no memory for service to delete"
- "service_publisher_have_competing_unicast_service"
- "service_publisher_unpublish_stale_service"
- "srp_device_mode"
- "srp_host_record_retry_callback"
- "srp_instance_retry_callback"
- "srp_schedule_host_record_retry"
- "srp_schedule_instance_retry"
- "thread device ML-EID"
- "update_host_tsr"
- "update_instance_tsr"

```
