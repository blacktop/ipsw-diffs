## mDNSResponder

> `/usr/sbin/mDNSResponder`

```diff

-2874.0.0.0.1
-  __TEXT.__text: 0x105790
-  __TEXT.__auth_stubs: 0x2ed0
+2881.0.7.0.0
+  __TEXT.__text: 0x105ab0
+  __TEXT.__auth_stubs: 0x2ef0
   __TEXT.__objc_stubs: 0x1b60
   __TEXT.__objc_methlist: 0x63c
   __TEXT.__const: 0x1168
-  __TEXT.__cstring: 0x17532
+  __TEXT.__cstring: 0x17566
   __TEXT.__gcc_except_tab: 0x32c
   __TEXT.__oslogstring: 0x1ec77
   __TEXT.__objc_classname: 0x649
-  __TEXT.__objc_methname: 0x19f2
+  __TEXT.__objc_methname: 0x19fe
   __TEXT.__objc_methtype: 0x62a
   __TEXT.__unwind_info: 0x1648
   __TEXT.__eh_frame: 0x74
-  __DATA_CONST.__auth_got: 0x1778
-  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__auth_got: 0x1788
+  __DATA_CONST.__got: 0x3f0
   __DATA_CONST.__auth_ptr: 0x78
   __DATA_CONST.__const: 0x6478
   __DATA_CONST.__cfstring: 0x1160

   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 27DB679F-D0B5-34E1-B0EC-D7898989B0A6
+  UUID: 6455637E-3884-3553-86F7-48B45FB3026D
   Functions: 1833
-  Symbols:   4555
-  CStrings:  4830
+  Symbols:   4556
+  CStrings:  4831
 
Symbols:
+ __Block_byref_object_copy_.913
+ __Block_byref_object_dispose_.914
+ __block_descriptor_tmp.11.852
+ __block_descriptor_tmp.12.853
+ __block_descriptor_tmp.14.1054
+ __block_descriptor_tmp.14.865
+ __block_descriptor_tmp.145.937
+ __block_descriptor_tmp.17.1055
+ __block_descriptor_tmp.17.893
+ __block_descriptor_tmp.18.895
+ __block_descriptor_tmp.19.896
+ __block_descriptor_tmp.20.897
+ __block_descriptor_tmp.20.985
+ __block_descriptor_tmp.25.1052
+ __block_descriptor_tmp.27.952
+ __block_descriptor_tmp.3.991
+ __block_descriptor_tmp.38.1033
+ __block_descriptor_tmp.39.1042
+ __block_descriptor_tmp.41.1037
+ __block_descriptor_tmp.51.1041
+ __block_descriptor_tmp.536
+ __block_descriptor_tmp.55.1039
+ __block_descriptor_tmp.58.1035
+ __block_descriptor_tmp.6.988
+ __block_descriptor_tmp.60.1029
+ __block_descriptor_tmp.63.999
+ __block_descriptor_tmp.69.1004
+ __block_descriptor_tmp.7.839
+ __block_descriptor_tmp.8.847
+ __block_descriptor_tmp.833
+ __block_descriptor_tmp.981
+ __block_literal_global.831
+ __block_literal_global.979
+ _nw_proxy_config_get_agent_domain
+ _nw_proxy_config_get_system_privacy_proxy_agent_type
+ _objc_msgSend$removeNetworkAgentDomain:agentType:
- __Block_byref_object_copy_.912
- __Block_byref_object_dispose_.913
- __block_descriptor_tmp.11.851
- __block_descriptor_tmp.12.852
- __block_descriptor_tmp.14.1053
- __block_descriptor_tmp.14.864
- __block_descriptor_tmp.145.936
- __block_descriptor_tmp.17.1054
- __block_descriptor_tmp.17.892
- __block_descriptor_tmp.18.894
- __block_descriptor_tmp.19.895
- __block_descriptor_tmp.20.896
- __block_descriptor_tmp.20.984
- __block_descriptor_tmp.25.1051
- __block_descriptor_tmp.27.951
- __block_descriptor_tmp.3.990
- __block_descriptor_tmp.38.1032
- __block_descriptor_tmp.39.1041
- __block_descriptor_tmp.41.1036
- __block_descriptor_tmp.51.1040
- __block_descriptor_tmp.537
- __block_descriptor_tmp.55.1038
- __block_descriptor_tmp.58.1034
- __block_descriptor_tmp.6.987
- __block_descriptor_tmp.60.1028
- __block_descriptor_tmp.63.998
- __block_descriptor_tmp.69.1003
- __block_descriptor_tmp.7.838
- __block_descriptor_tmp.8.846
- __block_descriptor_tmp.832
- __block_descriptor_tmp.980
- __block_literal_global.830
- __block_literal_global.978
- _ne_privacy_proxy_netagent_id
- _objc_msgSend$removeNetworkAgentUUID:
Functions:
~ _mDNS_StartQuery_internal : 9128 -> 9260
~ _mDNS_Execute : 24196 -> 24236
~ _CheckForSoonToExpireRecordsEx : 268 -> 308
~ _mDNSCoreReceiveResponse : 42424 -> 42844
~ ___mdns_dns_service_manager_apply_pending_updates_block_invoke : 1316 -> 1380
~ _EtcHostsAddNewEntries : 684 -> 720
~ _EtcHostsDeleteOldEntries : 756 -> 824
CStrings:
+ "EtcHostsAddNewEntries: Skipping, locahost sub-domain %s"
+ "mDNSResponder-2881.0.7"
+ "removeNetworkAgentDomain:agentType:"
- "mDNSResponder-2874.0.0.0.1"
- "removeNetworkAgentUUID:"

```
