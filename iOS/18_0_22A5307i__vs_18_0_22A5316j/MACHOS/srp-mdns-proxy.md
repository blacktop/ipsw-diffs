## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2559.0.10.0.1
-  __TEXT.__text: 0x6dd5c
-  __TEXT.__auth_stubs: 0x1160
+2559.0.31.0.0
+  __TEXT.__text: 0x70190
+  __TEXT.__auth_stubs: 0x1210
+  __TEXT.__cstring: 0x66e5
   __TEXT.__const: 0x1fb
-  __TEXT.__oslogstring: 0xe56e
-  __TEXT.__cstring: 0x648a
+  __TEXT.__oslogstring: 0xeb0f
   __TEXT.__objc_classname: 0x1
-  __TEXT.__info_plist: 0x23c
-  __TEXT.__unwind_info: 0x4e8
-  __DATA_CONST.__auth_got: 0x8b0
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x7c0
+  __TEXT.__info_plist: 0x241
+  __TEXT.__unwind_info: 0x510
+  __TEXT.__eh_frame: 0x74
+  __DATA_CONST.__auth_got: 0x908
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__const: 0x7d0
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x1c8
-  __DATA.__bss: 0x798
+  __DATA.__bss: 0x7d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
-  Functions: 390
-  Symbols:   944
-  CStrings:  1989
+  Functions: 402
+  Symbols:   972
+  CStrings:  2035
 
Symbols:
+ _DNSServiceAttributeDeallocate
+ _DNSServiceRegisterInternal
+ _DNSServiceRegisterRecordInternal
+ _DNSServiceUpdateRecordInternal
+ __MergedGlobals
+ ___isPlatformVersionAtLeast
+ __availability_version_check
+ __block_descriptor_tmp.1080
+ __block_descriptor_tmp.17.1184
+ __block_descriptor_tmp.36.1311
+ __block_descriptor_tmp.492
+ __block_descriptor_tmp.8.1125
+ __block_literal_global.490
+ __initializeAvailabilityCheck
+ _adv_ctl_need_service_instance
+ _adv_ctl_wanted_service_free
+ _compatibilityInitializeAvailabilityCheck
+ _dispatch_once_f
+ _dlsym
+ _fclose
+ _fopen
+ _fread
+ _fseek
+ _ftell
+ _initializeAvailabilityCheck
+ _malloc
+ _old_saref_created
+ _old_saref_finalized
+ _put_attribute_tlvs
+ _put_tlv_uint32
+ _rewind
+ _saref_created
+ _saref_finalized
+ _service_publisher_sed_timeout_expired
+ _service_publisher_wanted_service_added
+ _srp_format_time_offset
+ _sscanf
- _DNSServiceRegister
- _DNSServiceRegisterRecord
- _DNSServiceUpdateRecord
- __block_descriptor_tmp.1067
- __block_descriptor_tmp.17.1171
- __block_descriptor_tmp.36.1298
- __block_descriptor_tmp.491
- __block_descriptor_tmp.8.1112
- __block_literal_global.489
CStrings:
+ " canceled"
+ "%!d(MISSING).%!d(MISSING).%!d(MISSING)"
+ "%!{(MISSING)public}s: %!{(MISSING)private, mask.hash}s%!{(MISSING)public}s: %!p(MISSING)"
+ "%!{(MISSING)public}s: Client uid %!d(MISSING) pid %!d(MISSING) sent a kDNSSDAdvertisingProxyNeedServiceInstance request."
+ "%!{(MISSING)public}s: DNSServiceRegister service_ref %!p(MISSING), TSR for instance %!{(MISSING)private, mask.hash}s host %!{(MISSING)private, mask.hash}s set to %!{(MISSING)public}s"
+ "%!{(MISSING)public}s: DNSServiceRegisterRecord rref = %!p(MISSING), TSR for %!{(MISSING)private, mask.hash}s set to %!{(MISSING)public}s"
+ "%!{(MISSING)public}s: DNSServiceUpdateRecord TSR for %!{(MISSING)private, mask.hash}s set to %!{(MISSING)public}s"
+ "%!{(MISSING)public}s: DNSServiceUpdateRecord for instance %!{(MISSING)private, mask.hash}s TSR failed: %!d(MISSING)"
+ "%!{(MISSING)public}s: DNSServiceUpdateRecordWithAttribute for host tsr failed: %!d(MISSING)"
+ "%!{(MISSING)public}s: [DSO%!d(MISSING)][Q%!d(MISSING)] hardwired response for %!{(MISSING)private, mask.hash}s %!d(MISSING) %!d(MISSING)"
+ "%!{(MISSING)public}s: [Q%!d(MISSING)][QU%!d(MISSING)] %!{(MISSING)private, mask.hash}s%!{(MISSING)public}s%!{(MISSING)public}s"
+ "%!{(MISSING)public}s: all needed services present -> false"
+ "%!{(MISSING)public}s: instance %!{(MISSING)private, mask.hash}s (%!p(MISSING)) tsr update failed, re-registering"
+ "%!{(MISSING)public}s: no memory for base_type, comparison can't be done."
+ "%!{(MISSING)public}s: record->host[%!p(MISSING)], record->rref[%!p(MISSING)] when we update host TSR."
+ "%!{(MISSING)public}s: shared_txn is NULL when we update host TSR."
+ "%!{(MISSING)public}s: shared_txn->sdref is NULL when we update host TSR."
+ "%!{(MISSING)public}s: skipping DNSServiceUpdateRecord for instance %!{(MISSING)private, mask.hash}s TSR"
+ "%!{(MISSING)public}s: srp on demand is %!{(MISSING)public}s"
+ "%!{(MISSING)public}s: srp service %!{(MISSING)private, mask.hash}s.%!{(MISSING)private, mask.hash}s not present -> true"
+ "%!{(MISSING)public}s: srp service %!{(MISSING)private, mask.hash}s.%!{(MISSING)private, mask.hash}s present as %!{(MISSING)private, mask.hash}s but has no address on local mesh -> true"
+ "%!{(MISSING)public}s: srp_service_needed == true -> true"
+ "%!{(MISSING)public}s: update for %!{(MISSING)private, mask.hash}s #%!d(MISSING), xid %!x(MISSING) validates, key lease %!d(MISSING), host lease %!d(MISSING), message lease %!d(MISSING), receive_time %!{(MISSING)public}s, remote %!{(MISSING)private, mask.hash}s -> %!p(MISSING)."
+ "/System/Library/CoreServices/SystemVersion.plist"
+ "11:14:05"
+ "CFDataCreateWithBytesNoCopy"
+ "CFDictionaryGetValue"
+ "CFGetTypeID"
+ "CFPropertyListCreateFromXMLData"
+ "CFPropertyListCreateWithData"
+ "CFRelease"
+ "CFStringCreateWithCStringNoCopy"
+ "CFStringGetCString"
+ "CFStringGetTypeID"
+ "Jul 12 2024"
+ "ProductVersion"
+ "[DC%!l(MISSING)ld]"
+ "adv_ctl_service_types_compare"
+ "adv_ctl_wanted_service_allocate"
+ "adv_ctl_wanted_service_free"
+ "kCFAllocatorNull"
+ "need service instance"
+ "needed"
+ "r"
+ "service-type"
+ "service_publisher_sed_timeout_expired"
+ "service_publisher_wanted_service_added"
+ "service_publisher_wanted_service_missing"
+ "srp_needed"
+ "srp_on_demand"
+ "update_host_tsr"
- "%!{(MISSING)public}s: [DSO%!d(MISSING)][Q%!d(MISSING)] not replying from cache for %!{(MISSING)private, mask.hash}s %!d(MISSING) %!d(MISSING)"
- "%!{(MISSING)public}s: [Q%!d(MISSING)][QU%!d(MISSING)] %!{(MISSING)private, mask.hash}s%!{(MISSING)public}s"
- "%!{(MISSING)public}s: update for %!{(MISSING)private, mask.hash}s #%!d(MISSING), xid %!x(MISSING) validates, lease time %!d(MISSING), receive_time %!{(MISSING)public}s, remote %!{(MISSING)private, mask.hash}s -> %!p(MISSING)."
- "00:10:57"
- "Jun 29 2024"

```
