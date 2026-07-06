## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-  __TEXT.__text: 0x1099d4
+  __TEXT.__text: 0x10a26c
   __TEXT.__auth_stubs: 0x2fb0
   __TEXT.__objc_stubs: 0x20c0
   __TEXT.__objc_methlist: 0x694
-  __TEXT.__cstring: 0x179a2
+  __TEXT.__cstring: 0x17aea
   __TEXT.__const: 0x14bc
   __TEXT.__gcc_except_tab: 0x37c
-  __TEXT.__oslogstring: 0x20d1e
+  __TEXT.__oslogstring: 0x20ef8
   __TEXT.__objc_classname: 0x646
   __TEXT.__objc_methname: 0x1e32
   __TEXT.__objc_methtype: 0x64d

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__auth_got: 0x17e8
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__got: 0x400
   __DATA_CONST.__auth_ptr: 0x78
   __DATA.__objc_const: 0x4188
   __DATA.__objc_selrefs: 0x9e8
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x1270
   __DATA.__data: 0x4330
-  __DATA.__bss: 0x16e40
+  __DATA.__bss: 0x16e38
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  Functions: 1868
-  Symbols:   4635
-  CStrings:  4905
+  Functions: 1869
+  Symbols:   4636
+  CStrings:  4926
 
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
+ GCC_except_table1832
+ ____post_natt_analytics_block_invoke
+ _dnssd_analytics_record_natt_outcome
+ s_natt_state
- GCC_except_table1831
- InterfaceIndexToInterfaceID.getLoopbackIndexOnce
- InterfaceIndexToInterfaceID.loopbackIndex
- ___InterfaceIndexToInterfaceID_block_invoke
Functions:
~ _main : 5080 -> 5072
~ _mDNS_vsnprintf : 3620 -> 3492
~ _UpdateInterfaceList : 6376 -> 6372
~ _NetWakeInterface : 1584 -> 1588
~ _AppendDomainLabel : 172 -> 160
~ _ConstructServiceName : 2716 -> 2720
~ _AppendDomainName : 184 -> 176
~ _mDNSMacOSXNetworkChanged : 2068 -> 2076
~ _request_callback : 44052 -> 44040
~ _mDNS_StartNATOperation_internal : 484 -> 504
~ _mDNSCoreReceive : 4180 -> 4192
~ _mDNSCoreReceiveQuery : 10868 -> 10872
~ _getDomainName : 236 -> 232
~ _DeconstructServiceName : 328 -> 324
~ _AdvertiseHostname : 736 -> 740
~ _MD5_Update : 3344 -> 3272
~ _mDNSCoreReceiveResponse : 26276 -> 28056
~ _mDNSCoreReceiveUpdate : 3192 -> 3188
~ _SendNDP : 736 -> 740
~ _dns_obj_domain_name_create_with_cstring : 448 -> 452
~ _natTraversalHandlePortMapReplyWithAddress : 620 -> 672
~ _StartRecordNatMap : 348 -> 356
~ _GetRRDisplayString_rdb : 2872 -> 2864
~ _DumpMDNSPacket : 14668 -> 14728
~ _GetReverseIPv6Addr : 264 -> 256
~ ___mDNSMacOSXNetworkChanged_block_invoke_2 : 1476 -> 1480
~ _getExtendedFlags : 344 -> 348
~ _handleLNTDeviceDescriptionResponse : 1160 -> 1116
~ _handleLNTGetExternalAddressResponse : 488 -> 524
~ _handleLNTPortMappingResponse : 896 -> 904
~ _DomainNameFromString : 296 -> 300
~ __DNSRecordDataToStringEx2 : 5324 -> 5216
~ _GetAddrInfoClientRequestStart : 1020 -> 1012
~ _InterfaceIndexToInterfaceID : 248 -> 192
~ _QueryRecordClientRequestStart : 908 -> 900
- ___InterfaceIndexToInterfaceID_block_invoke
~ ___dnssd_analytics_init_block_invoke_3 : 1172 -> 1336
+ _dnssd_analytics_record_natt_outcome
+ ____post_natt_analytics_block_invoke
~ _mdns_trust_checks_check : 3904 -> 3896
~ __mdns_siphash_with_key_ex : 980 -> 972
CStrings:
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
- "mDNSResponder-3085.0.0.0.1"

```
