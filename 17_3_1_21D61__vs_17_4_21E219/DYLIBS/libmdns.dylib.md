## libmdns.dylib

> `/usr/lib/libmdns.dylib`

```diff

-2200.80.16.0.0
-  __TEXT.__text: 0x30d38
-  __TEXT.__auth_stubs: 0x1c90
+2200.100.94.0.2
+  __TEXT.__text: 0x30f44
+  __TEXT.__auth_stubs: 0x1c70
   __TEXT.__objc_methlist: 0x10c
-  __TEXT.__cstring: 0x1fab
+  __TEXT.__cstring: 0x1f91
   __TEXT.__const: 0xa6
   __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__oslogstring: 0x364f
-  __TEXT.__unwind_info: 0x924
+  __TEXT.__oslogstring: 0x36a7
+  __TEXT.__unwind_info: 0x92c
   __TEXT.__eh_frame: 0x7c
   __TEXT.__objc_classname: 0x523
-  __TEXT.__objc_methname: 0xca9
-  __TEXT.__objc_methtype: 0x5ec
-  __TEXT.__objc_stubs: 0xc20
-  __DATA_CONST.__got: 0x208
+  __TEXT.__objc_methname: 0xd73
+  __TEXT.__objc_methtype: 0x52d
+  __TEXT.__objc_stubs: 0xd00
+  __DATA_CONST.__got: 0x200
   __DATA_CONST.__const: 0x2888
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x34b8
-  __DATA_CONST.__objc_selrefs: 0x348
-  __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x560
+  __DATA_CONST.__objc_selrefs: 0x380
+  __AUTH_CONST.__const: 0x3c0
+  __AUTH_CONST.__cfstring: 0x520
+  __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0xe58
+  __AUTH_CONST.__auth_got: 0xe48
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0xe0
+  __DATA.__objc_classrefs: 0xe8
   __DATA.__objc_superrefs: 0x8
   __DATA.__data: 0x1394
-  __DATA.__bss: 0x378
-  __DATA_DIRTY.__const: 0x1198
+  __DATA.__bss: 0x370
+  __DATA_DIRTY.__const: 0x1078
   __DATA_DIRTY.__objc_const: 0x120
   __DATA_DIRTY.__objc_data: 0xeb0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess
-  - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PacketFilter.framework/PacketFilter
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 519BAFC6-DEA6-39E2-B999-F5C95624401F
-  Functions: 792
-  Symbols:   2903
-  CStrings:  1157
+  UUID: 76B256F2-10B1-3D29-88C2-5EA1D138EAC3
+  Functions: 793
+  Symbols:   2909
+  CStrings:  1161
 
Symbols:
+ +[DNSHeuristics clearNetworkAsFiltered:]
+ +[DNSHeuristics setNetworkAsFiltered:]
+ +[DNSHeuristics setNetworkAsFiltered:filtered:]
+ +[DNSHeuristics setNetworkSettings:value:]
+ _OBJC_CLASS_$_CWFInterface
+ ___Block_byref_object_copy_.629
+ ___Block_byref_object_dispose_.630
+ ____mdns_create_dns_over_bytestream_framer_block_invoke.1173
+ ___block_descriptor_tmp.1.1520
+ ___block_descriptor_tmp.1.437
+ ___block_descriptor_tmp.10.1168
+ ___block_descriptor_tmp.10.904
+ ___block_descriptor_tmp.1022
+ ___block_descriptor_tmp.1044
+ ___block_descriptor_tmp.1226
+ ___block_descriptor_tmp.14.1177
+ ___block_descriptor_tmp.1422
+ ___block_descriptor_tmp.1462
+ ___block_descriptor_tmp.1478
+ ___block_descriptor_tmp.15.902
+ ___block_descriptor_tmp.1507
+ ___block_descriptor_tmp.1517
+ ___block_descriptor_tmp.16.205
+ ___block_descriptor_tmp.18.1181
+ ___block_descriptor_tmp.19.208
+ ___block_descriptor_tmp.2.722
+ ___block_descriptor_tmp.2.906
+ ___block_descriptor_tmp.209.398
+ ___block_descriptor_tmp.213.418
+ ___block_descriptor_tmp.22.1175
+ ___block_descriptor_tmp.22.689
+ ___block_descriptor_tmp.228.400
+ ___block_descriptor_tmp.23.696
+ ___block_descriptor_tmp.24.697
+ ___block_descriptor_tmp.26.698
+ ___block_descriptor_tmp.27.1171
+ ___block_descriptor_tmp.27.699
+ ___block_descriptor_tmp.29.701
+ ___block_descriptor_tmp.3.1029
+ ___block_descriptor_tmp.3.684
+ ___block_descriptor_tmp.31.702
+ ___block_descriptor_tmp.33.705
+ ___block_descriptor_tmp.34.714
+ ___block_descriptor_tmp.37.1186
+ ___block_descriptor_tmp.37.711
+ ___block_descriptor_tmp.39.1183
+ ___block_descriptor_tmp.4.1355
+ ___block_descriptor_tmp.4.442
+ ___block_descriptor_tmp.40.707
+ ___block_descriptor_tmp.41.1165
+ ___block_descriptor_tmp.41.709
+ ___block_descriptor_tmp.420
+ ___block_descriptor_tmp.433
+ ___block_descriptor_tmp.44.1155
+ ___block_descriptor_tmp.46.1151
+ ___block_descriptor_tmp.476
+ ___block_descriptor_tmp.49.1356
+ ___block_descriptor_tmp.5.1361
+ ___block_descriptor_tmp.50.1246
+ ___block_descriptor_tmp.596
+ ___block_descriptor_tmp.6.446
+ ___block_descriptor_tmp.6.718
+ ___block_descriptor_tmp.6.910
+ ___block_descriptor_tmp.67.1229
+ ___block_descriptor_tmp.680
+ ___block_descriptor_tmp.69.1230
+ ___block_descriptor_tmp.7.1371
+ ___block_descriptor_tmp.7.449
+ ___block_descriptor_tmp.70.1253
+ ___block_descriptor_tmp.71.1252
+ ___block_descriptor_tmp.72.1250
+ ___block_descriptor_tmp.752
+ ___block_descriptor_tmp.899
+ ___block_descriptor_tmp.92.1305
+ ___block_descriptor_tmp.97.1282
+ ___block_literal_global.1009
+ ___block_literal_global.1041
+ ___block_literal_global.12.1166
+ ___block_literal_global.1359
+ ___block_literal_global.1418
+ ___block_literal_global.146.632
+ ___block_literal_global.1460
+ ___block_literal_global.1476
+ ___block_literal_global.1504
+ ___block_literal_global.1515
+ ___block_literal_global.16.1174
+ ___block_literal_global.20.1179
+ ___block_literal_global.259
+ ___block_literal_global.342
+ ___block_literal_global.43.703
+ ___block_literal_global.47
+ ___block_literal_global.474
+ ___block_literal_global.5.1026
+ ___block_literal_global.593
+ ___block_literal_global.658
+ ___block_literal_global.675
+ ___block_literal_global.746
+ ___block_literal_global.8.873
+ ___block_literal_global.8.908
+ ___block_literal_global.879
+ ___block_literal_global.897
+ ___getHeuristicsQueue_block_invoke
+ __mdns_querier_clear_delegation
+ _audit_token_to_pid
+ _getHeuristicsQueue
+ _getHeuristicsQueue.onceToken
+ _getHeuristicsQueue.queue
+ _nw_parameters_set_prefer_no_proxy
+ _nw_parameters_set_source_application
+ _objc_msgSend$DNSHeuristicsFailureStateInfo
+ _objc_msgSend$activate
+ _objc_msgSend$clearNetworkAsFiltered:
+ _objc_msgSend$currentKnownNetworkProfile
+ _objc_msgSend$invalidate
+ _objc_msgSend$isDNSHeuristicsFilteredNetwork
+ _objc_msgSend$setDNSHeuristicsFailureStateInfo:
+ _objc_msgSend$setDNSHeuristicsFilteredNetwork:
+ _objc_msgSend$setNetworkAsFiltered:
+ _objc_msgSend$setNetworkAsFiltered:filtered:
+ _objc_msgSend$setNetworkSettings:value:
+ _objc_msgSend$updateKnownNetworkProfile:properties:error:
+ _objc_opt_new
+ _uuid_clear
- +[DNSHeuristics clearNetworkAsFiltered:network:]
- +[DNSHeuristics setNetworkAsFiltered:network:]
- +[DNSHeuristics setNetworkAsFiltered:network:filtered:]
- +[DNSHeuristics setNetworkSettings:network:value:]
- _WiFiDeviceClientCopyCurrentNetwork
- _WiFiDeviceClientGetInterfaceRoleIndex
- _WiFiManagerClientCopyCurrentSessionBasedNetwork
- _WiFiManagerClientCopyInterfaces
- _WiFiManagerClientCreate
- _WiFiManagerClientSetNetworkProperty
- _WiFiNetworkGetProperty
- ___Block_byref_object_copy_.623
- ___Block_byref_object_dispose_.624
- ____mdns_create_dns_over_bytestream_framer_block_invoke.1136
- ___block_descriptor_tmp.1.1483
- ___block_descriptor_tmp.1.429
- ___block_descriptor_tmp.10.1131
- ___block_descriptor_tmp.10.893
- ___block_descriptor_tmp.1015
- ___block_descriptor_tmp.1037
- ___block_descriptor_tmp.1189
- ___block_descriptor_tmp.13.210
- ___block_descriptor_tmp.1385
- ___block_descriptor_tmp.14.1140
- ___block_descriptor_tmp.1425
- ___block_descriptor_tmp.1441
- ___block_descriptor_tmp.1470
- ___block_descriptor_tmp.1480
- ___block_descriptor_tmp.15.891
- ___block_descriptor_tmp.18.1144
- ___block_descriptor_tmp.2.713
- ___block_descriptor_tmp.2.895
- ___block_descriptor_tmp.207
- ___block_descriptor_tmp.209.391
- ___block_descriptor_tmp.213.410
- ___block_descriptor_tmp.22.1138
- ___block_descriptor_tmp.22.682
- ___block_descriptor_tmp.228.393
- ___block_descriptor_tmp.23.689
- ___block_descriptor_tmp.24.690
- ___block_descriptor_tmp.26.691
- ___block_descriptor_tmp.27.1134
- ___block_descriptor_tmp.27.692
- ___block_descriptor_tmp.29.694
- ___block_descriptor_tmp.3.1022
- ___block_descriptor_tmp.3.677
- ___block_descriptor_tmp.31.695
- ___block_descriptor_tmp.33.697
- ___block_descriptor_tmp.34.705
- ___block_descriptor_tmp.37.1149
- ___block_descriptor_tmp.37.702
- ___block_descriptor_tmp.39.1146
- ___block_descriptor_tmp.4.1318
- ___block_descriptor_tmp.4.434
- ___block_descriptor_tmp.40.699
- ___block_descriptor_tmp.41.1128
- ___block_descriptor_tmp.41.700
- ___block_descriptor_tmp.412
- ___block_descriptor_tmp.425
- ___block_descriptor_tmp.44.1118
- ___block_descriptor_tmp.46.1114
- ___block_descriptor_tmp.468
- ___block_descriptor_tmp.49.1319
- ___block_descriptor_tmp.5.1324
- ___block_descriptor_tmp.50.1209
- ___block_descriptor_tmp.590
- ___block_descriptor_tmp.6.438
- ___block_descriptor_tmp.6.709
- ___block_descriptor_tmp.6.899
- ___block_descriptor_tmp.67.1192
- ___block_descriptor_tmp.673
- ___block_descriptor_tmp.69.1193
- ___block_descriptor_tmp.7.1334
- ___block_descriptor_tmp.7.441
- ___block_descriptor_tmp.70.1216
- ___block_descriptor_tmp.71.1215
- ___block_descriptor_tmp.72.1213
- ___block_descriptor_tmp.743
- ___block_descriptor_tmp.888
- ___block_descriptor_tmp.92.1269
- ___block_descriptor_tmp.97.1245
- ___block_literal_global.1002
- ___block_literal_global.1034
- ___block_literal_global.12.1129
- ___block_literal_global.1322
- ___block_literal_global.1381
- ___block_literal_global.1423
- ___block_literal_global.1439
- ___block_literal_global.145
- ___block_literal_global.1467
- ___block_literal_global.1478
- ___block_literal_global.16.1137
- ___block_literal_global.20.1142
- ___block_literal_global.256
- ___block_literal_global.335
- ___block_literal_global.40
- ___block_literal_global.44
- ___block_literal_global.466
- ___block_literal_global.5.1019
- ___block_literal_global.587
- ___block_literal_global.651
- ___block_literal_global.668
- ___block_literal_global.737
- ___block_literal_global.8.864
- ___block_literal_global.8.897
- ___block_literal_global.870
- ___block_literal_global.886
- ___copyHeuristicsQueue_block_invoke
- _copyHeuristicsQueue
- _copyHeuristicsQueue.onceToken
- _copyHeuristicsQueue.queue
- _getNetworkManager.manager
- _kCFBooleanFalse
- _objc_msgSend$clearNetworkAsFiltered:network:
- _objc_msgSend$copy
- _objc_msgSend$setNetworkAsFiltered:network:
- _objc_msgSend$setNetworkAsFiltered:network:filtered:
- _objc_msgSend$setNetworkSettings:network:value:
CStrings:
+ "@24@0:8@16"
+ "B32@0:8@16@24"
+ "DNSHeuristicsFailureStateInfo"
+ "T@\"NSString\",?,R,C"
+ "activate"
+ "clearNetworkAsFiltered:"
+ "currentKnownNetworkProfile"
+ "dns_heuristics_report_resolution_failure %@ %d"
+ "dns_heuristics_report_resolution_success"
+ "invalidate"
+ "isDNSHeuristicsFilteredNetwork"
+ "q"
+ "setDNSHeuristicsFailureStateInfo:"
+ "setDNSHeuristicsFilteredNetwork:"
+ "setNetworkAsFiltered:"
+ "setNetworkAsFiltered:filtered:"
+ "setNetworkSettings:value:"
+ "updateKnownNetworkProfile:properties:error:"
- "@24@0:8^{__WiFiNetwork=}16"
- "B24@0:8^{__WiFiNetwork=}16"
- "B32@0:8^{__WiFiManagerClient=}16^{__WiFiNetwork=}24"
- "B36@0:8^{__WiFiManagerClient=}16^{__WiFiNetwork=}24B32"
- "B40@0:8^{__WiFiManagerClient=}16^{__WiFiNetwork=}24@32"
- "DNSFailures"
- "FilteredNetwork"
- "clearNetworkAsFiltered:network:"
- "copy"
- "setNetworkAsFiltered:network:"
- "setNetworkAsFiltered:network:filtered:"
- "setNetworkSettings:network:value:"

```
