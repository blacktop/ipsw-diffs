## mDNSResponder

> `/usr/sbin/mDNSResponder`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-3089.0.0.0.1
-  __TEXT.__text: 0x106a04
-  __TEXT.__auth_stubs: 0x2ff0
+3109.0.0.0.0
+  __TEXT.__text: 0x107284
+  __TEXT.__auth_stubs: 0x3000
   __TEXT.__objc_stubs: 0xf00
   __TEXT.__objc_methlist: 0x2a4
-  __TEXT.__const: 0x15e4
-  __TEXT.__cstring: 0x18abf
+  __TEXT.__const: 0x15dc
+  __TEXT.__cstring: 0x18a7f
   __TEXT.__gcc_except_tab: 0x3d0
-  __TEXT.__oslogstring: 0x1fd1a
+  __TEXT.__oslogstring: 0x1fef8
   __TEXT.__objc_classname: 0x5fe
   __TEXT.__objc_methname: 0xe47
   __TEXT.__objc_methtype: 0x4ea

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x1808
+  __DATA_CONST.__auth_got: 0x1810
   __DATA_CONST.__got: 0x370
   __DATA_CONST.__auth_ptr: 0xa0
   __DATA.__objc_const: 0x3b20

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1799
-  Symbols:   3847
-  CStrings:  4565
+  Functions: 1800
+  Symbols:   3849
+  CStrings:  4568
 
Symbols:
+ GCC_except_table1229
+ GCC_except_table1238
+ GCC_except_table1366
+ GCC_except_table1761
+ _FormatKeepaliveRData
+ __exit
+ _mdns_powerlog_service_register_start
- GCC_except_table1228
- GCC_except_table1237
- GCC_except_table1365
- GCC_except_table1760
- _UpdateKeepaliveRData
CStrings:
+ " ["
+ " key%u"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dns_push/dns_push_discovery.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssd_server.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_crypto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_mdns_core.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_denial_of_existence.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_domain_name.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_resource_record_member.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_dnskey.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_nsec3.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rrset.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_validation_manager.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/domain_name_labels.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uAhOzp/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/rdata_parser.c"
+ "FormatKeepaliveRData: InterfaceID mismatch mti.IntfId = %p InterfaceID = %p"
+ "FormatKeepaliveRData: mDNSPlatformRetrieveTCPInfo failed %d"
+ "FormatKeepaliveRData: not a valid record %s for keepalive %#a:%d %#a:%d"
+ "SetRData: rdata length %u for type %u exceeds storage %u"
+ "UpdateKeepaliveRDataWithMAC: Freed allocated memory for keep alive packet: %s "
+ "UpdateKeepaliveRDataWithMAC: successfully updated the record %s"
+ "mDNSResponder-3109"
+ "register_service_instance: TSR registration rejected, different host key for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "register_service_instance: TSR registration rejected, existing non-TSR record for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
+ "register_service_instance: non-TSR registration rejected, existing TSR record for %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u"
- " %s%s"
- " key%u=\""
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dns_push/dns_push_discovery.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssd_server.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_crypto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_mdns_core.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_denial_of_existence.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_domain_name.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_resource_record_member.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_dnskey.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_nsec3.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rrset.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_validation_manager.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/domain_name_labels.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/rdata_parser.c"
- "UpdateKeepaliveRData: Freed allocated memory for keep alive packet: %s "
- "UpdateKeepaliveRData: could not allocate memory %s"
- "UpdateKeepaliveRData: not a valid record %s for keepalive %#a:%d %#a:%d"
- "UpdateKeepaliveRData: successfully updated the record %s"
- "mDNSPlatformRetrieveTCPInfo: InterfaceID mismatch mti.IntfId = %p InterfaceID = %p"
- "mDNSPlatformRetrieveTCPInfo: mDNSPlatformRetrieveTCPInfo failed %d"
- "mDNSResponder-3089.0.0.0.1"
```
