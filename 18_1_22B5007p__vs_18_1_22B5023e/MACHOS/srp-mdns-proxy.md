## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2559.0.31.0.0
-  __TEXT.__text: 0x70190
-  __TEXT.__auth_stubs: 0x1210
-  __TEXT.__cstring: 0x66e5
+2559.40.2.0.0
+  __TEXT.__text: 0x71810
+  __TEXT.__auth_stubs: 0x1220
+  __TEXT.__cstring: 0x67c6
   __TEXT.__const: 0x1fb
-  __TEXT.__oslogstring: 0xeb0f
+  __TEXT.__oslogstring: 0xf0b8
   __TEXT.__objc_classname: 0x1
   __TEXT.__info_plist: 0x241
-  __TEXT.__unwind_info: 0x510
+  __TEXT.__unwind_info: 0x518
   __TEXT.__eh_frame: 0x74
-  __DATA_CONST.__auth_got: 0x908
+  __DATA_CONST.__auth_got: 0x910
   __DATA_CONST.__got: 0x208
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x7d0
+  __DATA_CONST.__const: 0x7e0
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x1c8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
-  Functions: 402
-  Symbols:   972
-  CStrings:  2035
+  Functions: 407
+  Symbols:   977
+  CStrings:  2055
 
Symbols:
+ _DNSServiceRegisterRecordWithAttribute
+ _DNSServiceRegisterWithAttribute
+ __block_descriptor_tmp.1089
+ __block_descriptor_tmp.113.232
+ __block_descriptor_tmp.17.1193
+ __block_descriptor_tmp.189
+ __block_descriptor_tmp.36.1320
+ __block_descriptor_tmp.501
+ __block_descriptor_tmp.8.1134
+ __block_literal_global.499
+ _mrc_dns_service_registration_set_reports_connection_errors
+ _service_publisher_start_wait
+ _service_tracker_cancel_probes
+ _srp_message_tsr_attribute_generate
+ _state_machine_cancel
- _DNSServiceRegisterInternal
- _DNSServiceRegisterRecordInternal
- __block_descriptor_tmp.107.228
- __block_descriptor_tmp.1080
- __block_descriptor_tmp.17.1184
- __block_descriptor_tmp.185
- __block_descriptor_tmp.36.1311
- __block_descriptor_tmp.492
- __block_descriptor_tmp.8.1125
- __block_literal_global.490
CStrings:
+ "%!{(MISSING)public}s: DNSServiceRegister failed: %!d(MISSING) (instance %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegister failed: %!{(MISSING)public}s (instance %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegister failed: %!{(MISSING)public}s.%!{(MISSING)public}s host %!{(MISSING)private, mask.hash}s: %!d(MISSING) (instance %!p(MISSING) sdref %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegister failed: %!{(MISSING)public}s.%!{(MISSING)public}s host %!{(MISSING)private, mask.hash}s: %!d(MISSING) (instance %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegister succeeded: %!{(MISSING)public}s.%!{(MISSING)public}s host %!{(MISSING)private, mask.hash}s (instance %!p(MISSING) sdref %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegister succeeded: %!{(MISSING)public}s.%!{(MISSING)public}s host %!{(MISSING)private, mask.hash}s at %!{(MISSING)public}s (instance %!p(MISSING) sdref %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegister, TSR for instance %!{(MISSING)private, mask.hash}s host %!{(MISSING)private, mask.hash}s set to %!{(MISSING)public}s(instance %!p(MISSING) sdref %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegisterRecord failed on host %!{(MISSING)public}s: %!d(MISSING) (record %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegisterRecord failed on host %!{(MISSING)public}s: %!{(MISSING)public}s (record %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegisterRecord failed: %!d(MISSING) (record %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegisterRecord for %!{(MISSING)private, mask.hash}s, TSR set to %!{(MISSING)public}s (record %!p(MISSING) rref %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceRegisterRecord succeeded on host %!{(MISSING)public}s at %!{(MISSING)public}s (record %!p(MISSING) rref %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceUpdateRecord TSR for %!{(MISSING)private, mask.hash}s set to %!{(MISSING)public}s (record %!p(MISSING) rref %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceUpdateRecord for %!{(MISSING)private, mask.hash}s, TSR set to %!{(MISSING)public}s (instance %!p(MISSING) sdref %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceUpdateRecord for instance %!{(MISSING)private, mask.hash}s TXT record failed: %!d(MISSING) (instance %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceUpdateRecord for instance %!{(MISSING)private, mask.hash}s, TSR failed: %!d(MISSING) (instance %!p(MISSING) sdref %!p(MISSING))"
+ "%!{(MISSING)public}s: DNSServiceUpdateRecordWithAttribute for host tsr failed: %!d(MISSING) (record %!p(MISSING) rref %!p(MISSING))"
+ "%!{(MISSING)public}s: Registered DNS Push connection failed on server with error: %!d(MISSING)"
+ "%!{(MISSING)public}s: bad service event received with no published service."
+ "%!{(MISSING)public}s: canceling %!{(MISSING)public}s"
+ "%!{(MISSING)public}s: didn't remove stale rref %!p(MISSING) because %!l(MISSING)x != %!p(MISSING)"
+ "%!{(MISSING)public}s: host is already registered: %!{(MISSING)public}s (record %!p(MISSING) rref %!p(MISSING))"
+ "%!{(MISSING)public}s: host registration is stale: %!{(MISSING)public}s (record %!p(MISSING) rref %!p(MISSING))"
+ "%!{(MISSING)public}s: publisher is in an invalid state, so we shouldn't re-advertise anything."
+ "%!{(MISSING)public}s: re-registration for %!{(MISSING)private, mask.hash}s (record %!p(MISSING) rref %!p(MISSING)) failed with code %!d(MISSING)"
+ "%!{(MISSING)public}s: re-registration for %!{(MISSING)private, mask.hash}s (record %!p(MISSING) rref %!p(MISSING)) succeeded."
+ "%!{(MISSING)public}s: removing rref %!p(MISSING)"
+ "%!{(MISSING)public}s: service %!{(MISSING)private, mask.hash}s.%!{(MISSING)private, mask.hash}s host not present -> true"
+ "%!{(MISSING)public}s: service %!{(MISSING)private, mask.hash}s.%!{(MISSING)private, mask.hash}s is present"
+ "%!{(MISSING)public}s: skipping DNSServiceUpdateRecord for instance %!{(MISSING)private, mask.hash}s TSR (instance %!p(MISSING))"
+ "%!{(MISSING)public}s: srp service %!{(MISSING)private, mask.hash}s.%!{(MISSING)private, mask.hash}s present but no addresses -> true"
+ "%!{(MISSING)public}s: starting wakeup timer to publish cached services after stale service timeout."
+ "%!{(MISSING)public}s: unadvertising %!{(MISSING)private, mask.hash}s IN AAAA {%!{(MISSING)public}s%!{(MISSING)private, mask.hash, srp:in6_addr_segment}.6P:%!{(MISSING)public, mask.hash, srp:in6_addr_segment}.2P:%!{(MISSING)private, mask.hash, srp:in6_addr_segment}.8P} rec %!p(MISSING) rref %!p(MISSING)"
+ "%!{(MISSING)public}s: unadvertising %!{(MISSING)private, mask.hash}s.%!{(MISSING)private, mask.hash}s instance %!p(MISSING) sdref %!p(MISSING)"
+ "%!{(MISSING)public}s: updated TXT record for %!{(MISSING)private, mask.hash}s . %!{(MISSING)private, mask.hash}s (instance %!p(MISSING) sdref %!p(MISSING))."
+ "16:05:59"
+ "Aug  2 2024"
+ "dns_registration_bad_service"
+ "dnssd_clientstub DNSServiceRemoveRecord called with NULL DNSRecordRef"
+ "probe_srp_service_probe_cancel"
+ "service_publisher_cancel"
+ "service_publisher_have_competing_unicast_service"
+ "state_machine_cancel"
- "%!{(MISSING)public}s: DNSServiceRegister failed: %!d(MISSING)"
- "%!{(MISSING)public}s: DNSServiceRegister failed: %!{(MISSING)public}s"
- "%!{(MISSING)public}s: DNSServiceRegister failed: %!{(MISSING)public}s.%!{(MISSING)public}s host %!{(MISSING)private, mask.hash}s: %!d(MISSING)"
- "%!{(MISSING)public}s: DNSServiceRegister service_ref %!p(MISSING), TSR for instance %!{(MISSING)private, mask.hash}s host %!{(MISSING)private, mask.hash}s set to %!{(MISSING)public}s"
- "%!{(MISSING)public}s: DNSServiceRegister succeeded: %!{(MISSING)public}s.%!{(MISSING)public}s host %!{(MISSING)private, mask.hash}s"
- "%!{(MISSING)public}s: DNSServiceRegisterRecord failed on host %!{(MISSING)public}s: %!d(MISSING)"
- "%!{(MISSING)public}s: DNSServiceRegisterRecord failed on host %!{(MISSING)public}s: %!{(MISSING)public}s"
- "%!{(MISSING)public}s: DNSServiceRegisterRecord failed: %!d(MISSING)"
- "%!{(MISSING)public}s: DNSServiceRegisterRecord rref = %!p(MISSING), TSR for %!{(MISSING)private, mask.hash}s set to %!{(MISSING)public}s"
- "%!{(MISSING)public}s: DNSServiceRegisterRecord succeeded on host %!{(MISSING)public}s"
- "%!{(MISSING)public}s: DNSServiceUpdateRecord TSR for %!{(MISSING)private, mask.hash}s set to %!{(MISSING)public}s"
- "%!{(MISSING)public}s: DNSServiceUpdateRecord for instance %!{(MISSING)private, mask.hash}s TSR failed: %!d(MISSING)"
- "%!{(MISSING)public}s: DNSServiceUpdateRecord for instance %!{(MISSING)private, mask.hash}s TXT record failed: %!d(MISSING)"
- "%!{(MISSING)public}s: DNSServiceUpdateRecordWithAttribute for host tsr failed: %!d(MISSING)"
- "%!{(MISSING)public}s: re-registration for %!{(MISSING)private, mask.hash}s %!p(MISSING) %!p(MISSING) failed with code %!d(MISSING)"
- "%!{(MISSING)public}s: re-registration for %!{(MISSING)private, mask.hash}s succeeded."
- "%!{(MISSING)public}s: skipping DNSServiceUpdateRecord for instance %!{(MISSING)private, mask.hash}s TSR"
- "%!{(MISSING)public}s: srp service %!{(MISSING)private, mask.hash}s.%!{(MISSING)private, mask.hash}s not present -> true"
- "%!{(MISSING)public}s: unadvertising %!{(MISSING)private, mask.hash}s IN AAAA {%!{(MISSING)public}s%!{(MISSING)private, mask.hash, srp:in6_addr_segment}.6P:%!{(MISSING)public, mask.hash, srp:in6_addr_segment}.2P:%!{(MISSING)private, mask.hash, srp:in6_addr_segment}.8P}"
- "%!{(MISSING)public}s: unadvertising %!{(MISSING)private, mask.hash}s.%!{(MISSING)private, mask.hash}s"
- "%!{(MISSING)public}s: updated TXT record for %!{(MISSING)private, mask.hash}s . %!{(MISSING)private, mask.hash}s."
- "11:23:30"
- "Jul 12 2024"

```
