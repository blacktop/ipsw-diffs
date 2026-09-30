## threadradiod

> `/System/Library/PrivateFrameworks/CoreThreadRadio.framework/threadradiod`

```diff

-275.0.101.1.0
-  __TEXT.__text: 0x3cb66c
-  __TEXT.__auth_stubs: 0x11450
-  __TEXT.__objc_stubs: 0x9640
+275.0.103.0.0
+  __TEXT.__text: 0x3cb464
+  __TEXT.__auth_stubs: 0x11470
+  __TEXT.__objc_stubs: 0x9680
   __TEXT.__init_offsets: 0xa4
-  __TEXT.__objc_methlist: 0x64d8
+  __TEXT.__objc_methlist: 0x64f0
   __TEXT.__objc_classname: 0x5f4
   __TEXT.__const: 0x8180
-  __TEXT.__gcc_except_tab: 0x2a750
-  __TEXT.__objc_methname: 0xe910
-  __TEXT.__cstring: 0x2f10c
-  __TEXT.__oslogstring: 0x228d9
+  __TEXT.__gcc_except_tab: 0x2a734
+  __TEXT.__objc_methname: 0xe952
+  __TEXT.__cstring: 0x2f317
+  __TEXT.__oslogstring: 0x228cc
   __TEXT.__objc_methtype: 0x4450
-  __TEXT.__unwind_info: 0x7290
+  __TEXT.__unwind_info: 0x7288
   __TEXT.__eh_frame: 0x60
-  __DATA_CONST.__auth_got: 0x8a40
+  __DATA_CONST.__auth_got: 0x8a50
   __DATA_CONST.__got: 0x918
   __DATA_CONST.__auth_ptr: 0x60
   __DATA_CONST.__const: 0xada8

   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x140
-  __DATA.__objc_const: 0x84b8
-  __DATA.__objc_selrefs: 0x35a0
-  __DATA.__objc_ivar: 0x530
+  __DATA.__objc_const: 0x84e8
+  __DATA.__objc_selrefs: 0x35b0
+  __DATA.__objc_ivar: 0x534
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0x5b8
   __DATA.__common: 0x3fdc4

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15778
-  Symbols:   82225
-  CStrings:  12094
+  Functions: 15783
+  Symbols:   82241
+  CStrings:  12109
 
Symbols:
+ -[ThreadNetworkManagerInstance mIsTestClient]
+ -[ThreadNetworkManagerInstance setMIsTestClient:]
+ GCC_except_table181
+ GCC_except_table213
+ GCC_except_table226
+ GCC_except_table340
+ GCC_except_table363
+ GCC_except_table377
+ OBJC_IVAR_$_ThreadNetworkManagerInstance._mIsTestClient
+ _ZN14RcpHostContext22isThreadSessionEnabledEv.cold.1
+ __48-[ThreadNetworkManagerInstance getAllMacMetrics]_block_invoke.216
+ __52-[ThreadNetworkManagerInstance getEngagementMetrics]_block_invoke.258
+ __54-[ThreadNetworkManagerInstance getNetworkRadioMetrics]_block_invoke.198
+ __72-[ThreadNetworkManagerInstance saveThreadConfiguration:passPhrase:uuid:]_block_invoke.359
+ __72-[ThreadNetworkManagerInstance saveThreadConfiguration:passPhrase:uuid:]_block_invoke.359.cold.1
+ __85-[ThreadNetworkManagerInstance fillupThreadCredentialsToSelfHealThreadNetwork:store:]_block_invoke.311
+ __85-[ThreadNetworkManagerInstance fillupThreadCredentialsToSelfHealThreadNetwork:store:]_block_invoke.311.cold.1
+ __Block_byref_object_copy_.309
+ __Block_byref_object_dispose_.310
+ __ZN14RcpHostContext22isThreadSessionEnabledEv
+ __ZN2ot17AppMetricsManager10HasAppPortERNS_3Ip63Udp6HeaderE
+ __ZN2ot3Mle3Mle22isThreadSessionEnabledEv
+ __ZNK2ot3Ip63Hap6Header16GetHasParseErrorEv
+ __ZNK2ot3Ip66Matter6Header16GetHasParseErrorEv
+ __block_literal_global.273
+ _objc_msgSend$mIsTestClient
+ _objc_msgSend$setMIsTestClient:
- GCC_except_table294
- GCC_except_table305
- GCC_except_table332
- _ZN11PcapManager19push_packet_to_fileERK10PcapPacket.cold.1
- _ZN11PcapManager19push_packet_to_fileERK10PcapPacket.cold.2
- _ZN11PcapManager19push_packet_to_fileERK10PcapPacket.cold.3
- _ZN11PcapManager19push_packet_to_fileERK10PcapPacket.cold.4
- _ZN11PcapManager19push_packet_to_fileERK10PcapPacket.cold.5
- _ZN15HostInterpreter22isThreadSessionEnabledEv.cold.1
- __48-[ThreadNetworkManagerInstance getAllMacMetrics]_block_invoke.215
- __52-[ThreadNetworkManagerInstance getEngagementMetrics]_block_invoke.257
- __54-[ThreadNetworkManagerInstance getNetworkRadioMetrics]_block_invoke.197
- __72-[ThreadNetworkManagerInstance saveThreadConfiguration:passPhrase:uuid:]_block_invoke.358
- __72-[ThreadNetworkManagerInstance saveThreadConfiguration:passPhrase:uuid:]_block_invoke.358.cold.1
- __85-[ThreadNetworkManagerInstance fillupThreadCredentialsToSelfHealThreadNetwork:store:]_block_invoke.310
- __85-[ThreadNetworkManagerInstance fillupThreadCredentialsToSelfHealThreadNetwork:store:]_block_invoke.310.cold.1
- __Block_byref_object_copy_.308
- __Block_byref_object_dispose_.309
- __block_literal_global.272
CStrings:
+ " %s:threadStartTime : %lld, triggered ABC_THREAD_SESSION_DURATION_EXCEEDED : threadStopTime : %lld, Session duration in sec : %lld"
+ " Morty_Version: V0.275.0.103"
+ "BT Load: %s There is BT audio task: %s or HID is connected: %d, config the x/y setting as %d/%d for SR discovery scan."
+ "BT Load: %s There is no BT activity, config the x/y setting as %d/%d for SR discovery scan."
+ "BT Load: %s Thread is On, change Coex Config based on new coex radioload"
+ "Error In Status = %d, Error = %d"
+ "Failed to parse Ip6::Headers, error = %s"
+ "OT instance is already invalidated, Daemon exiting"
+ "OT_ERROR_PARSE <<exit>>"
+ "OT_ERROR_PARSE <<framePending>>"
+ "OT_ERROR_PARSE <<headerUpdated>>"
+ "OT_ERROR_PARSE <<keyId>> <<frameCounter>>"
+ "OT_ERROR_PARSE <<status value from RCP>>"
+ "OT_ERROR_PARSE <<status>>"
+ "TB,V_mIsTestClient"
+ "Thread session duration"
+ "Thread session duration exceeded"
+ "[netif] *****RX ICMP error packet dump******"
+ "[netif] *****TX ICMP error packet dump******"
+ "_mIsTestClient"
+ "mIsTestClient"
+ "setMIsTestClient:"
+ "wpanctl"
- " Morty_Version: V0.275.0.101"
- "BT Load: %s There is BT audio task %s, config the x/y setting as %d/%d for SR discovery scan."
- "BT Load: %s There is no BT audio task, config the x/y setting as %d/%d for SR discovery scan."
- "SNIFFER_TLF:: Could not get file size :%s for sniffer file."
- "SNIFFER_TLF:: Failed to open sniffer file : %s for writing after backup sniff file."
- "[netif] *****ICMP packet dump******"
- "ccSt()t(LL)"
- "dD"

```
