## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-  __TEXT.__text: 0x1060c8
+  __TEXT.__text: 0x106a04
   __TEXT.__auth_stubs: 0x2ff0
   __TEXT.__objc_stubs: 0xf00
   __TEXT.__objc_methlist: 0x2a4
   __TEXT.__const: 0x15e4
-  __TEXT.__cstring: 0x18977
+  __TEXT.__cstring: 0x18abf
   __TEXT.__gcc_except_tab: 0x3d0
-  __TEXT.__oslogstring: 0x1fb40
+  __TEXT.__oslogstring: 0x1fd1a
   __TEXT.__objc_classname: 0x5fe
   __TEXT.__objc_methname: 0xe47
   __TEXT.__objc_methtype: 0x4ea

   __DATA.__objc_selrefs: 0x4f0
   __DATA.__objc_data: 0x1180
   __DATA.__data: 0x42c8
-  __DATA.__bss: 0x16dd8
+  __DATA.__bss: 0x16dd0
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1798
-  Symbols:   4327
-  CStrings:  4694
+  Functions: 1799
+  Symbols:   4328
+  CStrings:  4715
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table1760
+ ____post_natt_analytics_block_invoke
+ _dnssd_analytics_record_natt_outcome
+ s_natt_state
- GCC_except_table1759
- InterfaceIndexToInterfaceID.getLoopbackIndexOnce
- InterfaceIndexToInterfaceID.loopbackIndex
- ___InterfaceIndexToInterfaceID_block_invoke
Functions:
~ _main : 10632 -> 10624
~ _mDNS_vsnprintf : 3620 -> 3492
~ _UpdateInterfaceList : 5812 -> 5704
~ _NetWakeInterface : 1584 -> 1588
~ _AppendDomainLabel : 172 -> 160
~ _ConstructServiceName : 2716 -> 2720
~ _AppendDomainName : 184 -> 176
~ _mDNS_SetSecretForDomain : 4136 -> 4120
~ _request_callback : 43580 -> 43856
~ _mDNS_StartNATOperation_internal : 484 -> 504
~ _mDNSCoreReceive : 4168 -> 4192
~ _mDNSCoreReceiveQuery : 10840 -> 10844
~ _getDomainName : 236 -> 232
~ _DeconstructServiceName : 336 -> 332
~ _AdvertiseHostname : 736 -> 740
~ _MD5_Update : 3344 -> 3272
~ _mDNSCoreReceiveResponse : 26272 -> 28052
~ _mDNSCoreReceiveUpdate : 3192 -> 3188
~ ___SendQueries_block_invoke : 1596 -> 1592
~ _SendNDP : 736 -> 740
~ _dns_obj_domain_name_create_with_cstring : 448 -> 452
~ _natTraversalHandlePortMapReplyWithAddress : 620 -> 672
~ _StartRecordNatMap : 348 -> 356
~ _GetRRDisplayString_rdb : 2872 -> 2864
~ _DumpMDNSPacket : 14656 -> 14716
~ _GetReverseIPv6Addr : 264 -> 256
~ ___mDNSMacOSXNetworkChanged_block_invoke_2 : 1476 -> 1480
~ _getExtendedFlags : 344 -> 348
~ _handleLNTDeviceDescriptionResponse : 1160 -> 1116
~ _handleLNTGetExternalAddressResponse : 488 -> 524
~ _handleLNTPortMappingResponse : 896 -> 904
~ _DomainNameFromString : 296 -> 300
~ __DNSRecordDataToStringEx2 : 5324 -> 5212
~ _GetAddrInfoClientRequestStart : 1020 -> 1012
~ _InterfaceIndexToInterfaceID : 248 -> 192
~ _QueryRecordClientRequestStart : 908 -> 900
- ___InterfaceIndexToInterfaceID_block_invoke
~ ___dnssd_analytics_init_block_invoke_3 : 1172 -> 1336
+ _dnssd_analytics_record_natt_outcome
+ ____post_natt_analytics_block_invoke
~ _mdns_trust_checks_check : 5188 -> 5180
~ __mdns_siphash_with_key_ex : 980 -> 972
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dns_push/dns_push_discovery.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssd_server.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_crypto.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_mdns_core.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_denial_of_existence.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_domain_name.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_resource_record_member.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_dnskey.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_nsec3.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rrset.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_validation_manager.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/domain_name_labels.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.GpJza2/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/rdata_parser.c"
+ "Unicast assist ReconfirmNeeded cleared by record refresh - %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{mdns:rrtype}d"
+ "Unicast assist ReconfirmNeeded preserved across non-refresh response - %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{mdns:rrtype}d UnansweredQueries %u"
+ "Unicast assist cleared by response - %{sensitive, mdnsresponder:domain_name}.*P %{mdns:dn_hash}u %{mdns:rrtype}d"
+ "com.apple.mDNSResponder.natTraversal"
+ "com.apple.mDNSResponder.natTraversal: Analytic not posted"
+ "dnsservice_port_mapping"
+ "igd_map_failed"
+ "igd_map_succeeded"
+ "igd_query_failed"
+ "igd_query_succeeded"
+ "llq"
+ "mDNSResponder-3089.0.0.0.1"
+ "pcp_map_failed"
+ "pcp_map_succeeded"
+ "pcp_query_failed"
+ "pcp_query_succeeded"
+ "pmp_map_failed"
+ "pmp_map_succeeded"
+ "pmp_query_failed"
+ "pmp_query_succeeded"
+ "udns_hostname_advertisement"
+ "udns_record_registration"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dns_push/dns_push_discovery.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssd_server.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_crypto.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_mdns_core.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_denial_of_existence.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_domain_name.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_resource_record_member.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_dnskey.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rr_nsec3.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_rrset.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSMacOSX/dnssec_v2/dnssec_objs/dnssec_obj_validation_manager.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/domain_name_labels.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yVum9h/Sources/mDNSResponder/mDNSShared/dns_objects/utilities/rdata_parser.c"
- "mDNSResponder-3083.0.0.0.1"

```
