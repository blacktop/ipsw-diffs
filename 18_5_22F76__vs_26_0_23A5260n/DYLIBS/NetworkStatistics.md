## NetworkStatistics

> `/System/Library/PrivateFrameworks/NetworkStatistics.framework/NetworkStatistics`

```diff

-249.120.2.0.0
-  __TEXT.__text: 0x2cd0c
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0x4248
-  __TEXT.__cstring: 0x50fe
-  __TEXT.__oslogstring: 0x2013
-  __TEXT.__const: 0x1dc
+260.0.0.0.0
+  __TEXT.__text: 0x2dcb4
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_methlist: 0x45a0
+  __TEXT.__cstring: 0x716e
+  __TEXT.__oslogstring: 0x2378
+  __TEXT.__const: 0x1e0
   __TEXT.__gcc_except_tab: 0x404
-  __TEXT.__unwind_info: 0xa18
-  __TEXT.__objc_classname: 0x4f2
-  __TEXT.__objc_methname: 0x78ce
-  __TEXT.__objc_methtype: 0x7d63
-  __TEXT.__objc_stubs: 0x4b60
+  __TEXT.__unwind_info: 0xa08
+  __TEXT.__objc_classname: 0x501
+  __TEXT.__objc_methname: 0x83a3
+  __TEXT.__objc_methtype: 0x9345
+  __TEXT.__objc_stubs: 0x4d20
   __DATA_CONST.__got: 0x190
-  __DATA_CONST.__const: 0x868
+  __DATA_CONST.__const: 0x900
   __DATA_CONST.__objc_classlist: 0x188
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19b0
+  __DATA_CONST.__objc_selrefs: 0x1bd8
   __DATA_CONST.__objc_superrefs: 0x120
   __DATA_CONST.__objc_arraydata: 0x8a8
-  __AUTH_CONST.__auth_got: 0x558
+  __AUTH_CONST.__auth_got: 0x568
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x5660
-  __AUTH_CONST.__objc_const: 0x7b30
+  __AUTH_CONST.__cfstring: 0x65c0
+  __AUTH_CONST.__objc_const: 0x8060
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_ivar: 0x748
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x760
   __DATA.__data: 0x508
   __DATA.__common: 0x18
   __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0xf50
+  __DATA_DIRTY.__objc_data: 0xe10
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x80
   __DATA_DIRTY.__common: 0x4

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B3EC7B5B-DCBE-39A8-8FE2-9055C7646ABD
-  Functions: 1521
-  Symbols:   4902
-  CStrings:  3351
+  UUID: 1AFEFC2D-CF8A-3180-AF52-C9B6E022AAD4
+  Functions: 1599
+  Symbols:   5100
+  CStrings:  3798
 
Symbols:
+ +[NWStatsManager dumpKernelMetrics:]
+ +[NWStatsManager getKernelMetrics:]
+ -[NWStatsConnSnapshot initWithConnDetails:startTime:flowFlags:]
+ -[NWStatsConnSource initWithDetails:length:monitor:]
+ -[NWStatsConnSource processExtendedDetails:length:]
+ -[NWStatsConnSource processExtendedDetails:length:].cold.1
+ -[NWStatsConnSource processExtendedDetails:length:].cold.2
+ -[NWStatsConnSource updateWithDetails:length:monitor:]
+ -[NWStatsManager _sendDetailsRequestMessage:]
+ -[NWStatsProtocolSnapshot _adjustedByteCount:packets:]
+ -[NWStatsProtocolSnapshot _deltaForCurrentBytes:packets:prevBytes:prevPackets:]
+ -[NWStatsProtocolSnapshot _details_adjustment_bytes]
+ -[NWStatsProtocolSnapshot _details_delta_ptr]
+ -[NWStatsProtocolSnapshot _details_ptr]
+ -[NWStatsProtocolSnapshot alternateBytesRepresentUnclassified]
+ -[NWStatsProtocolSnapshot deltaAccountingRxAlternateBytes]
+ -[NWStatsProtocolSnapshot deltaAccountingRxWiFiInfraBytes]
+ -[NWStatsProtocolSnapshot deltaAccountingRxWiFiNonInfraBytes]
+ -[NWStatsProtocolSnapshot deltaAccountingTxAlternateBytes]
+ -[NWStatsProtocolSnapshot deltaAccountingTxWiFiInfraBytes]
+ -[NWStatsProtocolSnapshot deltaAccountingTxWiFiNonInfraBytes]
+ -[NWStatsProtocolSnapshot deltaRxAlternateBytes]
+ -[NWStatsProtocolSnapshot deltaRxWiFiInfraBytes]
+ -[NWStatsProtocolSnapshot deltaRxWiFiNonInfraBytes]
+ -[NWStatsProtocolSnapshot deltaTxAlternateBytes]
+ -[NWStatsProtocolSnapshot deltaTxWiFiInfraBytes]
+ -[NWStatsProtocolSnapshot deltaTxWiFiNonInfraBytes]
+ -[NWStatsProtocolSnapshot hasAlternateTrafficDelta]
+ -[NWStatsProtocolSnapshot hasAlternateTraffic]
+ -[NWStatsProtocolSnapshot hasCompanionLinkBluetoothTrafficDelta]
+ -[NWStatsProtocolSnapshot hasCompanionLinkBluetoothTraffic]
+ -[NWStatsProtocolSnapshot hasValidPerInterfaceTypeActivityMaps]
+ -[NWStatsProtocolSnapshot hasWiFiInfraTrafficDelta]
+ -[NWStatsProtocolSnapshot hasWiFiInfraTraffic]
+ -[NWStatsProtocolSnapshot hasWiFiNonInfraTrafficDelta]
+ -[NWStatsProtocolSnapshot hasWiFiNonInfraTraffic]
+ -[NWStatsProtocolSnapshot initWithDetails:startTime:flowFlags:previously:peerEgressCellularCounts:]
+ -[NWStatsProtocolSnapshot interfaceUltraConstrained]
+ -[NWStatsProtocolSnapshot interfaceWiFiNonInfra]
+ -[NWStatsProtocolSnapshot networkActivityMapAlternatePart1]
+ -[NWStatsProtocolSnapshot networkActivityMapAlternatePart2]
+ -[NWStatsProtocolSnapshot networkActivityMapAlternateStartTime]
+ -[NWStatsProtocolSnapshot networkActivityMapAlternate]
+ -[NWStatsProtocolSnapshot networkActivityMapBTPart1]
+ -[NWStatsProtocolSnapshot networkActivityMapBTPart2]
+ -[NWStatsProtocolSnapshot networkActivityMapBTStartTime]
+ -[NWStatsProtocolSnapshot networkActivityMapBT]
+ -[NWStatsProtocolSnapshot networkActivityMapCellPart1]
+ -[NWStatsProtocolSnapshot networkActivityMapCellPart2]
+ -[NWStatsProtocolSnapshot networkActivityMapCellStartTime]
+ -[NWStatsProtocolSnapshot networkActivityMapCell]
+ -[NWStatsProtocolSnapshot networkActivityMapTotalPart1]
+ -[NWStatsProtocolSnapshot networkActivityMapTotalPart2]
+ -[NWStatsProtocolSnapshot networkActivityMapTotalStartTime]
+ -[NWStatsProtocolSnapshot networkActivityMapTotal]
+ -[NWStatsProtocolSnapshot networkActivityMapWiFiInfraPart1]
+ -[NWStatsProtocolSnapshot networkActivityMapWiFiInfraPart2]
+ -[NWStatsProtocolSnapshot networkActivityMapWiFiInfraStartTime]
+ -[NWStatsProtocolSnapshot networkActivityMapWiFiInfra]
+ -[NWStatsProtocolSnapshot networkActivityMapWiFiNonInfraPart1]
+ -[NWStatsProtocolSnapshot networkActivityMapWiFiNonInfraPart2]
+ -[NWStatsProtocolSnapshot networkActivityMapWiFiNonInfraStartTime]
+ -[NWStatsProtocolSnapshot networkActivityMapWiFiNonInfra]
+ -[NWStatsProtocolSnapshot networkActivityMapWiredPart1]
+ -[NWStatsProtocolSnapshot networkActivityMapWiredPart2]
+ -[NWStatsProtocolSnapshot networkActivityMapWiredStartTime]
+ -[NWStatsProtocolSnapshot networkActivityMapWired]
+ -[NWStatsProtocolSnapshot numSpecificBitmaps]
+ -[NWStatsProtocolSnapshot rawDeltaRxAlternateBytes]
+ -[NWStatsProtocolSnapshot rawDeltaRxWiFiInfraBytes]
+ -[NWStatsProtocolSnapshot rawDeltaRxWiFiNonInfraBytes]
+ -[NWStatsProtocolSnapshot rawDeltaTxAlternateBytes]
+ -[NWStatsProtocolSnapshot rawDeltaTxWiFiInfraBytes]
+ -[NWStatsProtocolSnapshot rawDeltaTxWiFiNonInfraBytes]
+ -[NWStatsProtocolSnapshot rawRxAlternateBytes]
+ -[NWStatsProtocolSnapshot rawRxWiFiInfraBytes]
+ -[NWStatsProtocolSnapshot rawRxWiFiNonInfraBytes]
+ -[NWStatsProtocolSnapshot rawTxAlternateBytes]
+ -[NWStatsProtocolSnapshot rawTxWiFiInfraBytes]
+ -[NWStatsProtocolSnapshot rawTxWiFiNonInfraBytes]
+ -[NWStatsProtocolSnapshot rxAlternateBytes]
+ -[NWStatsProtocolSnapshot rxWiFiInfraBytes]
+ -[NWStatsProtocolSnapshot rxWiFiNonInfraBytes]
+ -[NWStatsProtocolSnapshot txAlternateBytes]
+ -[NWStatsProtocolSnapshot txWiFiInfraBytes]
+ -[NWStatsProtocolSnapshot txWiFiNonInfraBytes]
+ -[NWStatsQUICSnapshot initWithDetails:startTime:flowFlags:previously:peerEgressCellularCounts:]
+ -[NWStatsQUICSnapshot interfaceUltraConstrained]
+ -[NWStatsQUICSource initWithDetails:length:monitor:]
+ -[NWStatsQUICSource updateWithDetails:length:monitor:]
+ -[NWStatsSource handleDomainInfo:]
+ -[NWStatsSource handleDomainInfo:].cold.1
+ -[NWStatsSource initWithDetails:length:monitor:]
+ -[NWStatsSource processExtendedDetails:length:]
+ -[NWStatsSource processExtendedDetails:length:].cold.1
+ -[NWStatsSource processExtendedDetails:length:].cold.2
+ -[NWStatsSource updateWithDetails:length:monitor:]
+ -[NWStatsTCPSnapshot initWithDetails:startTime:flowFlags:previously:peerEgressCellularCounts:]
+ -[NWStatsTCPSnapshot interfaceUltraConstrained]
+ -[NWStatsTCPSource initWithDetails:length:monitor:]
+ -[NWStatsTCPSource updateWithDetails:length:monitor:]
+ -[NWStatsUDPSnapshot initWithDetails:startTime:flowFlags:previously:peerEgressCellularCounts:]
+ -[NWStatsUDPSnapshot interfaceUltraConstrained]
+ -[NWStatsUDPSource initWithDetails:length:monitor:]
+ -[NWStatsUDPSource updateWithDetails:length:monitor:]
+ _OBJC_IVAR_$_NWStatsConnSnapshot._nstat_details
+ _OBJC_IVAR_$_NWStatsConnSource._nstatConnDetails
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._alternateBytesRepresentUnclassified
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._deltaRxAlternateBytes
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._deltaTxAlternateBytes
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._hasAlternateTraffic
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._hasAlternateTrafficDelta
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._hasValidPerInterfaceTypeActivityMaps
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._interfaceUltraConstrained
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._interfaceWiFiNonInfra
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._nstat_details
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._txWiFiInfraBytes
+ _OBJC_IVAR_$_NWStatsProtocolSnapshot._txWiFiNonInfraBytes
+ _OBJC_IVAR_$_NWStatsQUICSource._nstatQUICDetails
+ _OBJC_IVAR_$_NWStatsTCPSource._nstatTCPDetails
+ _OBJC_IVAR_$_NWStatsUDPSource._nstatUDPDetails
+ __OBJC_$_CLASS_METHODS_NWStatsManager
+ _bzero
+ _fillClientMetrics
+ _getCurrentMetrics
+ _getGlobalMetrics
+ _getGrandTotalMetrics
+ _getPidMetrics
+ _getPreviousMetrics
+ _getProcessMetrics
+ _handleField
+ _kNWStatsThresholdPDPInterfaces
+ _kNtstatMetricClientAdded
+ _kNtstatMetricClientName
+ _kNtstatMetricClientPid
+ _kNtstatMetricClientWatching
+ _kNtstatMetricId
+ _kNtstatMetricIdPretty
+ _kNtstatMetricItemName
+ _kNtstatMetricItemPretty
+ _kNtstatMetricItemValue
+ _kNtstatMetricItems
+ _kNtstatMetricsCurrent
+ _kNtstatMetricsGlobal
+ _kNtstatMetricsGrandTotal
+ _kNtstatMetricsPid
+ _kNtstatMetricsPrevious
+ _kNtstatMetricsProcessName
+ _kNtstatMetricsReportZeroCounts
+ _kNtstatMetricsSelf
+ _objc_msgSend$_adjustedByteCount:packets:
+ _objc_msgSend$_deltaForCurrentBytes:packets:prevBytes:prevPackets:
+ _objc_msgSend$_details_adjustment_bytes
+ _objc_msgSend$_details_delta_ptr
+ _objc_msgSend$_details_ptr
+ _objc_msgSend$_sendDetailsRequestMessage:
+ _objc_msgSend$deltaAccountingRxAlternateBytes
+ _objc_msgSend$deltaAccountingRxWiFiInfraBytes
+ _objc_msgSend$deltaAccountingRxWiFiNonInfraBytes
+ _objc_msgSend$deltaAccountingTxAlternateBytes
+ _objc_msgSend$deltaAccountingTxWiFiInfraBytes
+ _objc_msgSend$deltaAccountingTxWiFiNonInfraBytes
+ _objc_msgSend$deltaRxAlternateBytes
+ _objc_msgSend$deltaRxWiFiInfraBytes
+ _objc_msgSend$deltaRxWiFiNonInfraBytes
+ _objc_msgSend$deltaTxAlternateBytes
+ _objc_msgSend$deltaTxWiFiInfraBytes
+ _objc_msgSend$deltaTxWiFiNonInfraBytes
+ _objc_msgSend$getKernelMetrics:
+ _objc_msgSend$handleDomainInfo:
+ _objc_msgSend$hasCompanionLinkBluetoothTrafficDelta
+ _objc_msgSend$initWithConnDetails:startTime:flowFlags:
+ _objc_msgSend$initWithDetails:length:monitor:
+ _objc_msgSend$initWithDetails:startTime:flowFlags:previously:peerEgressCellularCounts:
+ _objc_msgSend$processExtendedDetails:length:
+ _objc_msgSend$rawDeltaRxCompanionLinkBluetoothBytes
+ _objc_msgSend$rawDeltaRxWiFiInfraBytes
+ _objc_msgSend$rawDeltaRxWiFiNonInfraBytes
+ _objc_msgSend$rawDeltaTxCompanionLinkBluetoothBytes
+ _objc_msgSend$rawDeltaTxWiFiInfraBytes
+ _objc_msgSend$rawDeltaTxWiFiNonInfraBytes
+ _objc_msgSend$stringByPaddingToLength:withString:startingAtIndex:
+ _objc_msgSend$updateWithDetails:length:monitor:
+ _scanClientMetrics
+ _specificClientMetrics
+ _sysctlbyname
- -[NWStatsConnSnapshot initWithConnUpdate:startTime:flowFlags:]
- -[NWStatsConnSource initWithUpdate:length:monitor:]
- -[NWStatsConnSource processExtendedUpdate:length:]
- -[NWStatsConnSource processExtendedUpdate:length:].cold.1
- -[NWStatsConnSource processExtendedUpdate:length:].cold.2
- -[NWStatsConnSource updateWithUpdate:length:monitor:]
- -[NWStatsProtocolSnapshot _adjustedByteCount:otherBytes:packets:]
- -[NWStatsProtocolSnapshot _deltaForCurrentBytes:otherBytes:packets:prevBytes:prevOtherBytes:prevPackets:]
- -[NWStatsProtocolSnapshot _nstatCountsDictionaryForm:]
- -[NWStatsProtocolSnapshot _quicDescriptorDictionaryForm:]
- -[NWStatsProtocolSnapshot _tcpDescriptorDictionaryForm:]
- -[NWStatsProtocolSnapshot _udpDescriptorDictionaryForm:]
- -[NWStatsProtocolSnapshot _update_adjustment_bytes]
- -[NWStatsProtocolSnapshot _update_delta_ptr]
- -[NWStatsProtocolSnapshot _update_ptr]
- -[NWStatsProtocolSnapshot dictionaryForm]
- -[NWStatsProtocolSnapshot initWithUpdate:startTime:flowFlags:previously:bluetoothCounts:peerEgressCellularCounts:]
- -[NWStatsQUICSnapshot initWithUpdate:startTime:flowFlags:previously:bluetoothCounts:peerEgressCellularCounts:]
- -[NWStatsQUICSource initWithUpdate:length:monitor:]
- -[NWStatsQUICSource updateWithUpdate:length:monitor:]
- -[NWStatsSource handleDomainUpdate:]
- -[NWStatsSource handleDomainUpdate:].cold.1
- -[NWStatsSource initWithUpdate:length:monitor:]
- -[NWStatsSource processExtendedUpdate:length:bluetoothCounts:]
- -[NWStatsSource processExtendedUpdate:length:bluetoothCounts:].cold.1
- -[NWStatsSource processExtendedUpdate:length:bluetoothCounts:].cold.2
- -[NWStatsSource processExtendedUpdate:length:bluetoothCounts:].cold.3
- -[NWStatsSource processExtendedUpdate:length:bluetoothCounts:].cold.4
- -[NWStatsSource saveOldBTCounts:]
- -[NWStatsSource saveOldBTCounts:].cold.1
- -[NWStatsSource updateWithUpdate:length:monitor:]
- -[NWStatsTCPSnapshot initWithUpdate:startTime:flowFlags:previously:bluetoothCounts:peerEgressCellularCounts:]
- -[NWStatsTCPSource initWithUpdate:length:monitor:]
- -[NWStatsTCPSource updateWithUpdate:length:monitor:]
- -[NWStatsUDPSnapshot initWithUpdate:startTime:flowFlags:previously:bluetoothCounts:peerEgressCellularCounts:]
- -[NWStatsUDPSource initWithUpdate:length:monitor:]
- -[NWStatsUDPSource updateWithUpdate:length:monitor:]
- _OBJC_IVAR_$_NWStatsConnSnapshot._nstat_update
- _OBJC_IVAR_$_NWStatsConnSource._nstatConnUpdate
- _OBJC_IVAR_$_NWStatsProtocolSnapshot._bluetooth_counts
- _OBJC_IVAR_$_NWStatsProtocolSnapshot._nstat_update
- _OBJC_IVAR_$_NWStatsQUICSource._nstatBluetoothCounts
- _OBJC_IVAR_$_NWStatsQUICSource._nstatQUICUpdate
- _OBJC_IVAR_$_NWStatsTCPSource._nstatBluetoothCounts
- _OBJC_IVAR_$_NWStatsTCPSource._nstatTCPUpdate
- _OBJC_IVAR_$_NWStatsUDPSource._nstatBluetoothCounts
- _OBJC_IVAR_$_NWStatsUDPSource._nstatUDPUpdate
- _objc_msgSend$_adjustedByteCount:otherBytes:packets:
- _objc_msgSend$_deltaForCurrentBytes:otherBytes:packets:prevBytes:prevOtherBytes:prevPackets:
- _objc_msgSend$_nstatCountsDictionaryForm:
- _objc_msgSend$_quicDescriptorDictionaryForm:
- _objc_msgSend$_tcpDescriptorDictionaryForm:
- _objc_msgSend$_udpDescriptorDictionaryForm:
- _objc_msgSend$_update_adjustment_bytes
- _objc_msgSend$_update_delta_ptr
- _objc_msgSend$_update_ptr
- _objc_msgSend$handleDomainUpdate:
- _objc_msgSend$initWithConnUpdate:startTime:flowFlags:
- _objc_msgSend$initWithUpdate:length:monitor:
- _objc_msgSend$initWithUpdate:startTime:flowFlags:previously:bluetoothCounts:peerEgressCellularCounts:
- _objc_msgSend$noBluetoothUseExpected:
- _objc_msgSend$processExtendedUpdate:length:
- _objc_msgSend$processExtendedUpdate:length:bluetoothCounts:
- _objc_msgSend$saveOldBTCounts:
- _objc_msgSend$uiBackgroundAudioCapable
- _objc_msgSend$updateWithUpdate:length:monitor:
CStrings:
+ " "
+ " added provider bitmap 0x%x"
+ " watched provider bitmap 0x%x"
+ "%@ %12lld  %@"
+ "-[NWStatsConnSource processExtendedDetails:length:]"
+ "-[NWStatsSource handleDomainInfo:]"
+ "-[NWStatsSource processExtendedDetails:length:]"
+ "@36@0:8r^{nstat_msg_src_details_conn={nstat_msg_hdr=QISS}QQ{nstat_detailed_counts={media_stats={traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}}QQQIIII[16C]}I[4C]{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]}}16d24I32"
+ "@40@0:8^{nstat_msg_src_details_convenient={nstat_msg_src_details_hdr={nstat_msg_hdr=QISS}QQ{nstat_detailed_counts={media_stats={traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}}QQQIIII[16C]}I[4C]}(?={nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}{nstat_route_descriptor=QQQ(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})II[4C]}{nstat_ifnet_descriptor=QI{nstat_ifnet_desc_link_status=I(?={nstat_ifnet_desc_cellular_status=IIIIIIIIIIIIIIIIS[2C]}{nstat_ifnet_desc_wifi_status=IIIIIIIIIIIIIIIIIIII})}I[128c][17c][3C]}{nstat_sysinfo_descriptor=I}{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]})}16q24@32"
+ "@52@0:8r^{nstat_msg_src_details_convenient={nstat_msg_src_details_hdr={nstat_msg_hdr=QISS}QQ{nstat_detailed_counts={media_stats={traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}}QQQIIII[16C]}I[4C]}(?={nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}{nstat_route_descriptor=QQQ(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})II[4C]}{nstat_ifnet_descriptor=QI{nstat_ifnet_desc_link_status=I(?={nstat_ifnet_desc_cellular_status=IIIIIIIIIIIIIIIIS[2C]}{nstat_ifnet_desc_wifi_status=IIIIIIIIIIIIIIIIIIII})}I[128c][17c][3C]}{nstat_sysinfo_descriptor=I}{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]})}16d24I32^{details_subset_for_deltas=QQQQQQQQQQQQQQQQQQQQQQQQQQQQIII}36r^{nstat_interface_counts=QQQQ}44"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaRxAlternateBytes = %llu, adjustmentRxAlternateBytes = %llu\n%@"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaRxCellularBytes = %llu, adjustmentRxCellularBytes = %llu\n%@"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaRxWiFiInfraBytes = %llu, adjustmentRxWiFiInfraBytes = %llu\n%@"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaRxWiFiNonInfraBytes = %llu, adjustmentRxWiFiNonInfraBytes = %llu\n%@"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaRxWiredBytes = %llu, adjustmentRxWiredBytes = %llu\n%@"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaTxAlternateBytes = %llu, adjustmentTxAlternateBytes = %llu\n%@"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaTxCellularBytes = %llu, adjustmentTxCellularBytes = %llu\n%@"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaTxCompanionLinkBluetoothBytes = %llu, adjustmentTxCompanionLinkBluetoothBytes = %llu\n%@"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaTxWiFiInfraBytes = %llu, adjustmentTxWiFiInfraBytes = %llu\n%@"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaTxWiFiNonInfraBytes = %llu, adjustmentTxWiFiNonInfraBytes = %llu\n%@"
+ "Accounting adjustment counts > actual deltas in the snapshot. deltaTxWiredBytes = %llu, adjustmentTxWiredBytes = %llu\n%@"
+ "B40@0:8^{nstat_msg_src_details_convenient={nstat_msg_src_details_hdr={nstat_msg_hdr=QISS}QQ{nstat_detailed_counts={media_stats={traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}}QQQIIII[16C]}I[4C]}(?={nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}{nstat_route_descriptor=QQQ(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})II[4C]}{nstat_ifnet_descriptor=QI{nstat_ifnet_desc_link_status=I(?={nstat_ifnet_desc_cellular_status=IIIIIIIIIIIIIIIIS[2C]}{nstat_ifnet_desc_wifi_status=IIIIIIIIIIIIIIIIIIII})}I[128c][17c][3C]}{nstat_sysinfo_descriptor=I}{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]})}16q24@32"
+ "Can't send a descriptor for \"gone\" source"
+ "Client request for counts on a single source"
+ "Client request to remove a source which is no longer there"
+ "Client request to remove a source which is still in existence"
+ "Client requests for all counts"
+ "Client requests for all counts hit limit on number returned per batch"
+ "Client requests for all descriptors"
+ "Client requests for all descriptors hit limit on number returned per batch"
+ "Client requests for all details hit limit on number returned per batch"
+ "Client requests for all updates"
+ "Client requests for all updates hit limit on number returned per batch"
+ "Client requests for descriptor on a single source"
+ "Client requests for details on a single source"
+ "Client requests for details on all sources"
+ "Client requests for update on a single source"
+ "Client yields lock due to possibly higher priority processing"
+ "Contended acquisitions of exlusive lock"
+ "Contended acquisitions of shared lock"
+ "Expected path, locus on pcb_detach"
+ "Expected path, locus on pcb_detach, an associated source being detached"
+ "Expected to be redundant/removed when socket handling code is refined"
+ "Failed goodbyes, further qualified by.."
+ "Failed to send a counts message"
+ "Failed to send a description message"
+ "Failed to send a details message"
+ "Failed to send a removed message"
+ "Failed to send an update message"
+ "Inverted numbers in delta calculations for flow %lld, current bytes %lld pkts %lld when previous bytes %lld pkts %lld"
+ "Metric:  %{public}@"
+ "Metric: %{public}@"
+ "NWStatsManager %p: %@ src-add %lld details open %lld poll %lld event %lld close %lld"
+ "No buffers for counts message send"
+ "No buffers for details message send"
+ "No buffers for message send"
+ "No buffers for update message send"
+ "Q32@0:8Q16Q24"
+ "Q48@0:8Q16Q24Q32Q40"
+ "QUIC details message with size %ld below minimum %ld\n"
+ "Sent a concluding counts message"
+ "Sent a concluding description message"
+ "Sent a concluding details message"
+ "Sent a concluding removed message"
+ "Sent a concluding update message"
+ "Skip a dead PCB when adding all TCP"
+ "Skip a dead PCB when adding all UDP"
+ "Skipped on sending a removed message"
+ "Skipped trying to send a details message"
+ "Skipped trying to send an update message"
+ "Skipped trying to send both counts and descriptor messages"
+ "Socket has WNT_STOPUSING when creating the initial locus"
+ "Successful goodbyes (include cases messages filtered out)"
+ "Successful lock upgrade to handle \"gone\" source"
+ "TB,R,N,V_alternateBytesRepresentUnclassified"
+ "TB,R,N,V_hasAlternateTraffic"
+ "TB,R,N,V_hasAlternateTrafficDelta"
+ "TB,R,N,V_hasValidPerInterfaceTypeActivityMaps"
+ "TB,R,N,V_interfaceUltraConstrained"
+ "TB,R,N,V_interfaceWiFiNonInfra"
+ "TCP Socket ownership discovered to have changed"
+ "TCP Socket ownership discovered to have changed, fail to get new name"
+ "TCP details message with size %ld below minimum %ld\n"
+ "TQ,R,N,V_deltaRxAlternateBytes"
+ "TQ,R,N,V_deltaTxAlternateBytes"
+ "TQ,R,N,V_txWiFiInfraBytes"
+ "TQ,R,N,V_txWiFiNonInfraBytes"
+ "T^{accumulator_bytes=QQQQQQQQQQQQ},R,N"
+ "T^{details_subset_for_deltas=QQQQQQQQQQQQQQQQQQQQQQQQQQQQIII},R,N"
+ "T^{xnu_activity_bitmap=Q[2Q]},R,N"
+ "Ti,R,N"
+ "Tr^{details_subset_for_deltas=QQQQQQQQQQQQQQQQQQQQQQQQQQQQIII},R,N"
+ "Tr^{nstat_msg_src_details_convenient={nstat_msg_src_details_hdr={nstat_msg_hdr=QISS}QQ{nstat_detailed_counts={media_stats={traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}}QQQIIII[16C]}I[4C]}(?={nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}{nstat_route_descriptor=QQQ(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})II[4C]}{nstat_ifnet_descriptor=QI{nstat_ifnet_desc_link_status=I(?={nstat_ifnet_desc_cellular_status=IIIIIIIIIIIIIIIIS[2C]}{nstat_ifnet_desc_wifi_status=IIIIIIIIIIIIIIIIIIII})}I[128c][17c][3C]}{nstat_sysinfo_descriptor=I}{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]})},R,N"
+ "UDP Socket ownership discovered to have changed"
+ "UDP Socket ownership discovered to have changed, fail to get new name"
+ "UDP details message with size %ld below minimum %ld\n"
+ "Uncontended acquisitions of exlusive lock"
+ "Uncontended acquisitions of shared lock"
+ "Unexpected path, no locus on pcb_detach"
+ "Unknown"
+ "Unknown metric: %{public}@"
+ "Unsuccessful lock upgrade to handle \"gone\" source"
+ "Userland connection details message with size %ld below minimum %ld\n"
+ "[11{provider_counts=\"numSrcsAdded\"Q\"numDetailsOnOpen\"Q\"numDetailsOnPoll\"Q\"numDetailsOnEvent\"Q\"numDetailsOnClose\"Q}]"
+ "^{accumulator_bytes=QQQQQQQQQQQQ}16@0:8"
+ "^{details_subset_for_deltas=QQQQQQQQQQQQQQQQQQQQQQQQQQQQIII}16@0:8"
+ "^{xnu_activity_bitmap=Q[2Q]}16@0:8"
+ "_adjustedByteCount:packets:"
+ "_alternateBytesRepresentUnclassified"
+ "_deltaForCurrentBytes:packets:prevBytes:prevPackets:"
+ "_deltaRxAlternateBytes"
+ "_deltaTxAlternateBytes"
+ "_details_adjustment_bytes"
+ "_details_delta_ptr"
+ "_details_ptr"
+ "_hasAlternateTraffic"
+ "_hasAlternateTrafficDelta"
+ "_hasValidPerInterfaceTypeActivityMaps"
+ "_interfaceUltraConstrained"
+ "_interfaceWiFiNonInfra"
+ "_nstatConnDetails"
+ "_nstatQUICDetails"
+ "_nstatTCPDetails"
+ "_nstatUDPDetails"
+ "_nstat_details"
+ "_sendDetailsRequestMessage:"
+ "_txWiFiInfraBytes"
+ "_txWiFiNonInfraBytes"
+ "accumulator rx/tx cell %lld %lld wifi-infra %lld %lld non-infra %lld %lld wired %lld %lld bt %lld %lld"
+ "adjustment counts > actual deltas in the snapshot. deltaRxCompanionLinkBluetoothBytes = %llu, adjustmentRxCompanionLinkBluetoothBytes = %llu\n%@"
+ "alternateBytesRepresentUnclassified"
+ "can't set name on sock locus create"
+ "count rx/tx pkts %lld %lld bytes %lld %lld cell %lld %lld wifi-infra %lld %lld non-infra %lld %lld wired %lld %lld bt %lld %lld alternate %lld %lld dup %lld ooo %lld retx %lld"
+ "current number of clients overall"
+ "current number of generic shadow objects overall"
+ "current number of nstat_tu_shadow objects overall"
+ "current number of procdetails objects overall"
+ "current number of srcs for client"
+ "current number of srcs overall"
+ "current number of tcp nstat_sock_locus overall"
+ "current number of udp nstat_extended_sock_locus overall"
+ "deltaAccountingRxAlternateBytes"
+ "deltaAccountingRxWiFiInfraBytes"
+ "deltaAccountingRxWiFiNonInfraBytes"
+ "deltaAccountingTxAlternateBytes"
+ "deltaAccountingTxWiFiInfraBytes"
+ "deltaAccountingTxWiFiNonInfraBytes"
+ "deltaRxAlternateBytes"
+ "deltaRxWiFiInfraBytes"
+ "deltaRxWiFiNonInfraBytes"
+ "deltaTxAlternateBytes"
+ "deltaTxWiFiInfraBytes"
+ "deltaTxWiFiNonInfraBytes"
+ "details"
+ "details message for unknown provider %d\n"
+ "dumpKernelMetrics:"
+ "fail to add because client is in clean up state"
+ "fail to get buffer for initial src-added"
+ "fail to get memory for nstat_src structure"
+ "fail to send initial src-added"
+ "getKernelMetrics:"
+ "handleDomainInfo:"
+ "hasAlternateTraffic"
+ "hasAlternateTrafficDelta"
+ "hasCompanionLinkBluetoothTraffic"
+ "hasCompanionLinkBluetoothTrafficDelta"
+ "hasValidPerInterfaceTypeActivityMaps"
+ "hasWiFiInfraTraffic"
+ "hasWiFiInfraTrafficDelta"
+ "hasWiFiNonInfraTraffic"
+ "hasWiFiNonInfraTrafficDelta"
+ "idle check removes a TCP locus"
+ "idle check removes a UDP locus"
+ "initWithConnDetails:startTime:flowFlags:"
+ "initWithDetails:length:monitor:"
+ "initWithDetails:startTime:flowFlags:previously:peerEgressCellularCounts:"
+ "interfaceUltraConstrained"
+ "interfaceWiFiNonInfra"
+ "kNWStatsThresholdPDPInterfaces"
+ "kNtstatMetricClientAdded"
+ "kNtstatMetricClientName"
+ "kNtstatMetricClientPid"
+ "kNtstatMetricClientWatching"
+ "kNtstatMetricId"
+ "kNtstatMetricIdPretty"
+ "kNtstatMetricItemName"
+ "kNtstatMetricItemPretty"
+ "kNtstatMetricItemValue"
+ "kNtstatMetricItems"
+ "kNtstatMetricsCurrent"
+ "kNtstatMetricsGlobal"
+ "kNtstatMetricsGrandTotal"
+ "kNtstatMetricsPid"
+ "kNtstatMetricsPrevious"
+ "kNtstatMetricsProcessName"
+ "kNtstatMetricsReportZeroCounts"
+ "kNtstatMetricsSelf"
+ "max number of clients overall"
+ "max number of procdetails overall"
+ "max number of srcs for client"
+ "max number of srcs overall"
+ "max number of tcp nstat_sock_locus overall"
+ "max number of tu_shadows overall"
+ "max number of udp nstat_extended_sock_locus overall"
+ "net.stats.global_counts"
+ "net.stats.metrics"
+ "networkActivityMapAlternate"
+ "networkActivityMapAlternatePart1"
+ "networkActivityMapAlternatePart2"
+ "networkActivityMapAlternateStartTime"
+ "networkActivityMapBT"
+ "networkActivityMapBTPart1"
+ "networkActivityMapBTPart2"
+ "networkActivityMapBTStartTime"
+ "networkActivityMapCell"
+ "networkActivityMapCellPart1"
+ "networkActivityMapCellPart2"
+ "networkActivityMapCellStartTime"
+ "networkActivityMapTotal"
+ "networkActivityMapTotalPart1"
+ "networkActivityMapTotalPart2"
+ "networkActivityMapTotalStartTime"
+ "networkActivityMapWiFiInfra"
+ "networkActivityMapWiFiInfraPart1"
+ "networkActivityMapWiFiInfraPart2"
+ "networkActivityMapWiFiInfraStartTime"
+ "networkActivityMapWiFiNonInfra"
+ "networkActivityMapWiFiNonInfraPart1"
+ "networkActivityMapWiFiNonInfraPart2"
+ "networkActivityMapWiFiNonInfraStartTime"
+ "networkActivityMapWired"
+ "networkActivityMapWiredPart1"
+ "networkActivityMapWiredPart2"
+ "networkActivityMapWiredStartTime"
+ "nstat_add_all_tcp_skip_dead"
+ "nstat_add_all_udp_skip_dead"
+ "nstat_global_client_alloc_fails"
+ "nstat_global_client_allocs"
+ "nstat_global_client_current"
+ "nstat_global_client_max"
+ "nstat_global_counts  Metrics that are \"global\", i.e. not per client"
+ "nstat_global_exclusive_lock_contended"
+ "nstat_global_exclusive_lock_uncontended"
+ "nstat_global_gshad_allocs"
+ "nstat_global_gshad_current"
+ "nstat_global_gshad_max"
+ "nstat_global_idlecheck_route_src_gone"
+ "nstat_global_idlecheck_tcp_gone"
+ "nstat_global_idlecheck_udp_gone"
+ "nstat_global_pcb_detach_tcp"
+ "nstat_global_pcb_detach_udp"
+ "nstat_global_pcb_detach_with_locus"
+ "nstat_global_pcb_detach_with_src"
+ "nstat_global_pcb_detach_without_locus"
+ "nstat_global_procdetails_allocs"
+ "nstat_global_procdetails_current"
+ "nstat_global_procdetails_max"
+ "nstat_global_sck_fail_first_owner"
+ "nstat_global_sck_fail_last_owner"
+ "nstat_global_sck_update_last_owner"
+ "nstat_global_shared_lock_contended"
+ "nstat_global_shared_lock_uncontended"
+ "nstat_global_src_alloc_fails"
+ "nstat_global_src_allocs"
+ "nstat_global_src_current"
+ "nstat_global_src_max"
+ "nstat_global_tcp_desc_fail_name"
+ "nstat_global_tcp_desc_new_name"
+ "nstat_global_tcp_sck_locus_alloc_fails"
+ "nstat_global_tcp_sck_locus_allocs"
+ "nstat_global_tcp_sck_locus_current"
+ "nstat_global_tcp_sck_locus_max"
+ "nstat_global_tcp_sck_locus_stop_using"
+ "nstat_global_tu_shad_allocs"
+ "nstat_global_tu_shad_current"
+ "nstat_global_tu_shad_max"
+ "nstat_global_udp_desc_fail_name"
+ "nstat_global_udp_desc_new_name"
+ "nstat_global_udp_sck_locus_alloc_fails"
+ "nstat_global_udp_sck_locus_allocs"
+ "nstat_global_udp_sck_locus_current"
+ "nstat_global_udp_sck_locus_max"
+ "nstat_global_udp_sck_locus_stop_using"
+ "nstat_metrics   Accumulated from all previous NetworkStatistics clients as they closed down"
+ "nstat_metrics   For client id: %d  process name %@ pid %d"
+ "nstat_metrics   Grand total accumulated from all current and previous NetworkStatistics clients"
+ "nstat_pcb_event"
+ "nstat_pcb_update_last_owner() was called"
+ "nstat_pcb_update_last_owner() was called, no name available"
+ "nstat_query_description_all"
+ "nstat_query_description_limit"
+ "nstat_query_description_nobuf"
+ "nstat_query_description_one"
+ "nstat_query_description_yield"
+ "nstat_query_details_all"
+ "nstat_query_details_limit"
+ "nstat_query_details_nobuf"
+ "nstat_query_details_noupgrade"
+ "nstat_query_details_one"
+ "nstat_query_details_upgrade"
+ "nstat_query_details_yield"
+ "nstat_query_request_all"
+ "nstat_query_request_limit"
+ "nstat_query_request_nobuf"
+ "nstat_query_request_nodesc"
+ "nstat_query_request_noupgrade"
+ "nstat_query_request_one"
+ "nstat_query_request_upgrade"
+ "nstat_query_request_yield"
+ "nstat_query_update_all"
+ "nstat_query_update_limit"
+ "nstat_query_update_nobuf"
+ "nstat_query_update_nodesc"
+ "nstat_query_update_noupgrade"
+ "nstat_query_update_one"
+ "nstat_query_update_upgrade"
+ "nstat_query_update_yield"
+ "nstat_remove_src_found"
+ "nstat_remove_src_missed"
+ "nstat_route_src_gone_idlecheck"
+ "nstat_send_event"
+ "nstat_send_event_fail"
+ "nstat_send_event_notsup"
+ "nstat_src_add_no_buf"
+ "nstat_src_add_no_src_mem"
+ "nstat_src_add_send_err"
+ "nstat_src_add_success"
+ "nstat_src_add_while_cleanup"
+ "nstat_src_current"
+ "nstat_src_gone_idlecheck"
+ "nstat_src_goodbye_failed_counts"
+ "nstat_src_goodbye_failed_description"
+ "nstat_src_goodbye_failed_details"
+ "nstat_src_goodbye_failed_removed"
+ "nstat_src_goodbye_failed_update"
+ "nstat_src_goodbye_failures"
+ "nstat_src_goodbye_filtered_counts"
+ "nstat_src_goodbye_filtered_details"
+ "nstat_src_goodbye_filtered_removed"
+ "nstat_src_goodbye_filtered_update"
+ "nstat_src_goodbye_sent_counts"
+ "nstat_src_goodbye_sent_description"
+ "nstat_src_goodbye_sent_details"
+ "nstat_src_goodbye_sent_removed"
+ "nstat_src_goodbye_sent_update"
+ "nstat_src_goodbye_successes"
+ "nstat_src_max"
+ "nstat_src_removed_linkage"
+ "nstat_wifi_infra_rxbytes"
+ "nstat_wifi_infra_txbytes"
+ "nstat_wifi_non_infra_rxbytes"
+ "nstat_wifi_non_infra_txbytes"
+ "numSpecificBitmaps"
+ "pcb detach removes a TCP locus"
+ "pcb detach removes a UDP locus"
+ "processExtendedDetails:length:"
+ "r^{details_subset_for_deltas=QQQQQQQQQQQQQQQQQQQQQQQQQQQQIII}16@0:8"
+ "r^{nstat_msg_src_details_convenient={nstat_msg_src_details_hdr={nstat_msg_hdr=QISS}QQ{nstat_detailed_counts={media_stats={traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}}QQQIIII[16C]}I[4C]}(?={nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}{nstat_route_descriptor=QQQ(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})II[4C]}{nstat_ifnet_descriptor=QI{nstat_ifnet_desc_link_status=I(?={nstat_ifnet_desc_cellular_status=IIIIIIIIIIIIIIIIS[2C]}{nstat_ifnet_desc_wifi_status=IIIIIIIIIIIIIIIIIIII})}I[128c][17c][3C]}{nstat_sysinfo_descriptor=I}{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]})}16@0:8"
+ "rawDeltaRxAlternateBytes"
+ "rawDeltaRxWiFiInfraBytes"
+ "rawDeltaRxWiFiNonInfraBytes"
+ "rawDeltaTxAlternateBytes"
+ "rawDeltaTxWiFiInfraBytes"
+ "rawDeltaTxWiFiNonInfraBytes"
+ "rawRxAlternateBytes"
+ "rawRxWiFiInfraBytes"
+ "rawRxWiFiNonInfraBytes"
+ "rawTxAlternateBytes"
+ "rawTxWiFiInfraBytes"
+ "rawTxWiFiNonInfraBytes"
+ "removed src linkages on the way to deletion"
+ "route src gone noted during periodic idle check"
+ "rxAlternateBytes"
+ "rxWiFiInfraBytes"
+ "rxWiFiNonInfraBytes"
+ "saved rx/tx pkts %lld %lld bytes %lld %lld cell %lld %lld wifi-infra %lld %lld non-infra %lld %lld wired %lld %lld bt %lld %lld alternate %lld %lld dup %d ooo %d retx %d"
+ "savedRxWiFiInfraBytes"
+ "savedRxWiFiNonInfraBytes"
+ "savedTxWiFiInfraBytes"
+ "savedTxWiFiNonInfraBytes"
+ "send event fail, likely lack of buffers"
+ "send event not supported, old style client"
+ "send event successful"
+ "send pcb event code called, one precursor to the send_event metrics"
+ "stringByPaddingToLength:withString:startingAtIndex:"
+ "successful src_add"
+ "systcl %s EINVAL global counts version %d != expected %d\n"
+ "systcl %s fail %{darwin.errno}d "
+ "systcl %s fail requesting version %d, specific id %d err %{darwin.errno}d "
+ "systcl %s fail scanning requesting version %d,  requested id %d err %{darwin.errno}d"
+ "total number of clients allocated"
+ "total number of failures to allocate a client"
+ "total number of failures to allocate a source"
+ "total number of failures to allocate a tcp nstat_sock_locus"
+ "total number of failures to allocate a udp nstat_extended_sock_locus"
+ "total number of procdetails allocated"
+ "total number of route sources discovered \"gone\" in idle check"
+ "total number of sources allocated"
+ "total number of tcp nstat_sock_locus allocated"
+ "total number of tu_shadows allocated"
+ "total number of udp nstat_extended_sock_locus allocated"
+ "txAlternateBytes"
+ "txWiFiInfraBytes"
+ "txWiFiNonInfraBytes"
+ "updateWithDetails:length:monitor:"
+ "v24@0:8^{nstat_detailed_counts={media_stats={traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}{traffic_stats=QQQQ{activity_bitmap=Q[2Q]}}}QQQIIII[16C]}16"
+ "{accumulator_bytes=\"rxCellularBytes\"Q\"rxWiFiInfraBytes\"Q\"rxWiFiNonInfraBytes\"Q\"rxWiredBytes\"Q\"rxCompanionLinkBluetoothBytes\"Q\"rxAlternateBytes\"Q\"txCellularBytes\"Q\"txWiFiInfraBytes\"Q\"txWiFiNonInfraBytes\"Q\"txWiredBytes\"Q\"txCompanionLinkBluetoothBytes\"Q\"txAlternateBytes\"Q}"
+ "{details_subset_for_deltas=\"savedRxPackets\"Q\"savedRxBytes\"Q\"savedTxPackets\"Q\"savedTxBytes\"Q\"savedRxCellularBytes\"Q\"savedTxCellularBytes\"Q\"savedRxCellularPackets\"Q\"savedTxCellularPackets\"Q\"savedRxWiFiInfraBytes\"Q\"savedTxWiFiInfraBytes\"Q\"savedRxWiFiInfraPackets\"Q\"savedTxWiFiInfraPackets\"Q\"savedRxWiFiNonInfraBytes\"Q\"savedTxWiFiNonInfraBytes\"Q\"savedRxWiFiNonInfraPackets\"Q\"savedTxWiFiNonInfraPackets\"Q\"savedRxWiredBytes\"Q\"savedTxWiredBytes\"Q\"savedRxWiredPackets\"Q\"savedTxWiredPackets\"Q\"savedRxCompanionLinkBluetoothBytes\"Q\"savedTxCompanionLinkBluetoothBytes\"Q\"savedRxCompanionLinkBluetoothPackets\"Q\"savedTxCompanionLinkBluetoothPackets\"Q\"savedRxAlternateBytes\"Q\"savedTxAlternateBytes\"Q\"savedRxAlternatePackets\"Q\"savedTxAlternatePackets\"Q\"savedRxDuplicateBytes\"I\"savedRxOutOfOrderBytes\"I\"savedTxRetransmittedBytes\"I}"
+ "{nstat_msg_src_details_conn=\"hdr\"{nstat_msg_hdr=\"context\"Q\"type\"I\"length\"S\"flags\"S}\"srcref\"Q\"event_flags\"Q\"detailed_counts\"{nstat_detailed_counts=\"nstat_media_stats\"{media_stats=\"ms_total\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_cellular\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wifi_infra\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wifi_non_infra\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wired\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_bluetooth\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_alternate\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}}\"nstat_rxduplicatebytes\"Q\"nstat_rxoutoforderbytes\"Q\"nstat_txretransmit\"Q\"nstat_min_rtt\"I\"nstat_avg_rtt\"I\"nstat_var_rtt\"I\"nstat_xtra_flags\"I\"nstat_xtra_uuid\"[16C]}\"provider\"I\"reserved\"[4C]\"conn_desc\"{nstat_connection_descriptor=\"start_timestamp\"Q\"timestamp\"Q\"upid\"Q\"eupid\"Q\"pid\"I\"epid\"I\"ifnet_properties\"I\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"cuuid\"[16C]\"puuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"reserved\"[4C]}}"
+ "{nstat_msg_src_details_convenient=\"hdr\"{nstat_msg_src_details_hdr=\"hdr\"{nstat_msg_hdr=\"context\"Q\"type\"I\"length\"S\"flags\"S}\"srcref\"Q\"event_flags\"Q\"detailed_counts\"{nstat_detailed_counts=\"nstat_media_stats\"{media_stats=\"ms_total\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_cellular\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wifi_infra\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wifi_non_infra\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wired\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_bluetooth\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_alternate\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}}\"nstat_rxduplicatebytes\"Q\"nstat_rxoutoforderbytes\"Q\"nstat_txretransmit\"Q\"nstat_min_rtt\"I\"nstat_avg_rtt\"I\"nstat_var_rtt\"I\"nstat_xtra_flags\"I\"nstat_xtra_uuid\"[16C]}\"provider\"I\"reserved\"[4C]}\"\"(?=\"tcp\"{nstat_tcp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"rx_transfer_size\"Q\"tx_transfer_size\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"ifindex\"I\"state\"I\"sndbufsize\"I\"sndbufused\"I\"rcvbufsize\"I\"rcvbufused\"I\"txunacked\"I\"txwindow\"I\"txcwindow\"I\"traffic_class\"I\"traffic_mgt_flags\"I\"pid\"I\"epid\"I\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"cc_algo\"[16c]\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"\"(?=\"connstatus\"{tcp_conn_status=\"\"(?=\"\"{?=\"probe_activated\"b1\"write_probe_failed\"b1\"read_probe_failed\"b1\"conn_probe_failed\"b1}\"pad_field\"I)}\"__pad_connstatus\"[4C])\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}\"udp\"{nstat_udp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"ifindex\"I\"rcvbufsize\"I\"rcvbufused\"I\"traffic_class\"I\"pid\"I\"pname\"[64c]\"epid\"I\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}\"route\"{nstat_route_descriptor=\"id\"Q\"parent_id\"Q\"gateway_id\"Q\"dst\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I}\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]})\"mask\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I}\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]})\"gateway\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I}\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]})\"ifindex\"I\"flags\"I\"reserved\"[4C]}\"ifnet\"{nstat_ifnet_descriptor=\"threshold\"Q\"ifindex\"I\"link_status\"{nstat_ifnet_desc_link_status=\"link_status_type\"I\"u\"(?=\"cellular\"{nstat_ifnet_desc_cellular_status=\"valid_bitmask\"I\"link_quality_metric\"I\"ul_effective_bandwidth\"I\"ul_max_bandwidth\"I\"ul_min_latency\"I\"ul_effective_latency\"I\"ul_max_latency\"I\"ul_retxt_level\"I\"ul_bytes_lost\"I\"ul_min_queue_size\"I\"ul_avg_queue_size\"I\"ul_max_queue_size\"I\"dl_effective_bandwidth\"I\"dl_max_bandwidth\"I\"config_inactivity_time\"I\"config_backoff_time\"I\"mss_recommended\"S\"reserved\"[2C]}\"wifi\"{nstat_ifnet_desc_wifi_status=\"valid_bitmask\"I\"link_quality_metric\"I\"ul_effective_bandwidth\"I\"ul_max_bandwidth\"I\"ul_min_latency\"I\"ul_effective_latency\"I\"ul_max_latency\"I\"ul_retxt_level\"I\"ul_bytes_lost\"I\"ul_error_rate\"I\"dl_effective_bandwidth\"I\"dl_max_bandwidth\"I\"dl_min_latency\"I\"dl_effective_latency\"I\"dl_max_latency\"I\"dl_error_rate\"I\"config_frequency\"I\"config_multicast_rate\"I\"scan_count\"I\"scan_duration\"I})}\"type\"I\"description\"[128c]\"name\"[17c]\"reserved\"[3C]}\"sysinfo\"{nstat_sysinfo_descriptor=\"flags\"I}\"quic\"{nstat_tcp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"rx_transfer_size\"Q\"tx_transfer_size\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"ifindex\"I\"state\"I\"sndbufsize\"I\"sndbufused\"I\"rcvbufsize\"I\"rcvbufused\"I\"txunacked\"I\"txwindow\"I\"txcwindow\"I\"traffic_class\"I\"traffic_mgt_flags\"I\"pid\"I\"epid\"I\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"cc_algo\"[16c]\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"\"(?=\"connstatus\"{tcp_conn_status=\"\"(?=\"\"{?=\"probe_activated\"b1\"write_probe_failed\"b1\"read_probe_failed\"b1\"conn_probe_failed\"b1}\"pad_field\"I)}\"__pad_connstatus\"[4C])\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}\"conn\"{nstat_connection_descriptor=\"start_timestamp\"Q\"timestamp\"Q\"upid\"Q\"eupid\"Q\"pid\"I\"epid\"I\"ifnet_properties\"I\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"cuuid\"[16C]\"puuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"reserved\"[4C]})}"
+ "{nstat_msg_src_details_quic=\"hdr\"{nstat_msg_hdr=\"context\"Q\"type\"I\"length\"S\"flags\"S}\"srcref\"Q\"event_flags\"Q\"detailed_counts\"{nstat_detailed_counts=\"nstat_media_stats\"{media_stats=\"ms_total\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_cellular\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wifi_infra\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wifi_non_infra\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wired\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_bluetooth\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_alternate\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}}\"nstat_rxduplicatebytes\"Q\"nstat_rxoutoforderbytes\"Q\"nstat_txretransmit\"Q\"nstat_min_rtt\"I\"nstat_avg_rtt\"I\"nstat_var_rtt\"I\"nstat_xtra_flags\"I\"nstat_xtra_uuid\"[16C]}\"provider\"I\"reserved\"[4C]\"quic_desc\"{nstat_tcp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"rx_transfer_size\"Q\"tx_transfer_size\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"ifindex\"I\"state\"I\"sndbufsize\"I\"sndbufused\"I\"rcvbufsize\"I\"rcvbufused\"I\"txunacked\"I\"txwindow\"I\"txcwindow\"I\"traffic_class\"I\"traffic_mgt_flags\"I\"pid\"I\"epid\"I\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"cc_algo\"[16c]\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"\"(?=\"connstatus\"{tcp_conn_status=\"\"(?=\"\"{?=\"probe_activated\"b1\"write_probe_failed\"b1\"read_probe_failed\"b1\"conn_probe_failed\"b1}\"pad_field\"I)}\"__pad_connstatus\"[4C])\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}}"
+ "{nstat_msg_src_details_tcp=\"hdr\"{nstat_msg_hdr=\"context\"Q\"type\"I\"length\"S\"flags\"S}\"srcref\"Q\"event_flags\"Q\"detailed_counts\"{nstat_detailed_counts=\"nstat_media_stats\"{media_stats=\"ms_total\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_cellular\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wifi_infra\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wifi_non_infra\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wired\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_bluetooth\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_alternate\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}}\"nstat_rxduplicatebytes\"Q\"nstat_rxoutoforderbytes\"Q\"nstat_txretransmit\"Q\"nstat_min_rtt\"I\"nstat_avg_rtt\"I\"nstat_var_rtt\"I\"nstat_xtra_flags\"I\"nstat_xtra_uuid\"[16C]}\"provider\"I\"reserved\"[4C]\"tcp_desc\"{nstat_tcp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"rx_transfer_size\"Q\"tx_transfer_size\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"ifindex\"I\"state\"I\"sndbufsize\"I\"sndbufused\"I\"rcvbufsize\"I\"rcvbufused\"I\"txunacked\"I\"txwindow\"I\"txcwindow\"I\"traffic_class\"I\"traffic_mgt_flags\"I\"pid\"I\"epid\"I\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"cc_algo\"[16c]\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"\"(?=\"connstatus\"{tcp_conn_status=\"\"(?=\"\"{?=\"probe_activated\"b1\"write_probe_failed\"b1\"read_probe_failed\"b1\"conn_probe_failed\"b1}\"pad_field\"I)}\"__pad_connstatus\"[4C])\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}}"
+ "{nstat_msg_src_details_udp=\"hdr\"{nstat_msg_hdr=\"context\"Q\"type\"I\"length\"S\"flags\"S}\"srcref\"Q\"event_flags\"Q\"detailed_counts\"{nstat_detailed_counts=\"nstat_media_stats\"{media_stats=\"ms_total\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_cellular\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wifi_infra\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wifi_non_infra\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_wired\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_bluetooth\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}\"ms_alternate\"{traffic_stats=\"ts_rxpackets\"Q\"ts_rxbytes\"Q\"ts_txpackets\"Q\"ts_txbytes\"Q\"ts_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}}}\"nstat_rxduplicatebytes\"Q\"nstat_rxoutoforderbytes\"Q\"nstat_txretransmit\"Q\"nstat_min_rtt\"I\"nstat_avg_rtt\"I\"nstat_var_rtt\"I\"nstat_xtra_flags\"I\"nstat_xtra_uuid\"[16C]}\"provider\"I\"reserved\"[4C]\"udp_desc\"{nstat_udp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"ifindex\"I\"rcvbufsize\"I\"rcvbufused\"I\"traffic_class\"I\"pid\"I\"pname\"[64c]\"epid\"I\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}}"
+ "\xf0\xf0X"
+ "\xf0\xf0\xf0\xf0\xf0\xf0a"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xe1"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0R\x96"
- "-[NWStatsConnSource processExtendedUpdate:length:]"
- "-[NWStatsSource handleDomainUpdate:]"
- "-[NWStatsSource processExtendedUpdate:length:bluetoothCounts:]"
- "-[NWStatsSource saveOldBTCounts:]"
- "@24@0:8^{nstat_counts=QQQQQQQQQQIIIIIIII}16"
- "@24@0:8^{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}16"
- "@24@0:8^{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}16"
- "@36@0:8r^{nstat_msg_src_update_conn={nstat_msg_hdr=QISS}QQ{nstat_counts=QQQQQQQQQQIIIIIIII}I[4C]{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]}}16d24I32"
- "@40@0:8^{nstat_msg_src_update_convenient={nstat_msg_src_update_hdr={nstat_msg_hdr=QISS}QQ{nstat_counts=QQQQQQQQQQIIIIIIII}I[4C]}(?={nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}{nstat_route_descriptor=QQQ(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})II[4C]}{nstat_ifnet_descriptor=QI{nstat_ifnet_desc_link_status=I(?={nstat_ifnet_desc_cellular_status=IIIIIIIIIIIIIIIIS[2C]}{nstat_ifnet_desc_wifi_status=IIIIIIIIIIIIIIIIIIII})}I[128c][17c][3C]}{nstat_sysinfo_descriptor=I}{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]})}16q24@32"
- "@60@0:8r^{nstat_msg_src_update_convenient={nstat_msg_src_update_hdr={nstat_msg_hdr=QISS}QQ{nstat_counts=QQQQQQQQQQIIIIIIII}I[4C]}(?={nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}{nstat_route_descriptor=QQQ(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})II[4C]}{nstat_ifnet_descriptor=QI{nstat_ifnet_desc_link_status=I(?={nstat_ifnet_desc_cellular_status=IIIIIIIIIIIIIIIIS[2C]}{nstat_ifnet_desc_wifi_status=IIIIIIIIIIIIIIIIIIII})}I[128c][17c][3C]}{nstat_sysinfo_descriptor=I}{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]})}16d24I32^{update_subset_for_deltas=QQQQQQQQQQQQIII}36r^{nstat_interface_counts=QQQQ}44r^{nstat_interface_counts=QQQQ}52"
- "B24@0:8^{nstat_interface_counts=QQQQ}16"
- "B40@0:8^{nstat_msg_src_extended_item_hdr=II}16q24^{nstat_interface_counts=QQQQ}32"
- "B40@0:8^{nstat_msg_src_update_convenient={nstat_msg_src_update_hdr={nstat_msg_hdr=QISS}QQ{nstat_counts=QQQQQQQQQQIIIIIIII}I[4C]}(?={nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}{nstat_route_descriptor=QQQ(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})II[4C]}{nstat_ifnet_descriptor=QI{nstat_ifnet_desc_link_status=I(?={nstat_ifnet_desc_cellular_status=IIIIIIIIIIIIIIIIS[2C]}{nstat_ifnet_desc_wifi_status=IIIIIIIIIIIIIIIIIIII})}I[128c][17c][3C]}{nstat_sysinfo_descriptor=I}{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]})}16q24@32"
- "Inverted numbers in delta calculations for flow %lld, current bytes %lld other bytes %lld pkts %lld when previous bytes %lld other %lld pkts %lld"
- "NWStatsManager %p: %@ src-add %lld updates open %lld poll %lld event %lld close %lld"
- "Noted multiple interface usage for TCP/QUIC flow"
- "Q40@0:8Q16Q24Q32"
- "Q64@0:8Q16Q24Q32Q40Q48Q56"
- "QUIC update message with size %ld below minimum %ld\n"
- "TCP update message with size %ld below minimum %ld\n"
- "T^{accumulator_bytes=QQQQQQQQ},R,N"
- "T^{update_subset_for_deltas=QQQQQQQQQQQQIII},R,N"
- "Tr^{nstat_msg_src_update_convenient={nstat_msg_src_update_hdr={nstat_msg_hdr=QISS}QQ{nstat_counts=QQQQQQQQQQIIIIIIII}I[4C]}(?={nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}{nstat_route_descriptor=QQQ(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})II[4C]}{nstat_ifnet_descriptor=QI{nstat_ifnet_desc_link_status=I(?={nstat_ifnet_desc_cellular_status=IIIIIIIIIIIIIIIIS[2C]}{nstat_ifnet_desc_wifi_status=IIIIIIIIIIIIIIIIIIII})}I[128c][17c][3C]}{nstat_sysinfo_descriptor=I}{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]})},R,N"
- "Tr^{update_subset_for_deltas=QQQQQQQQQQQQIII},R,N"
- "UDP update message with size %ld below minimum %ld\n"
- "Unexpected provider %d when converting to dictionary form"
- "Userland connection update message with size %ld below minimum %ld\n"
- "VPN adjustment bytecounts > actual deltas in the snapshot. deltaRxCellularBytes = %llu, adjustmentRxCellularBytes = %llu"
- "VPN adjustment bytecounts > actual deltas in the snapshot. deltaRxWiFiBytes = %llu, adjustmentRxWiFiBytes = %llu"
- "VPN adjustment bytecounts > actual deltas in the snapshot. deltaRxWiredBytes = %llu, adjustmentRxWiredBytes = %llu"
- "VPN adjustment bytecounts > actual deltas in the snapshot. deltaTxCellularBytes = %llu, adjustmentTxCellularBytes = %llu"
- "VPN adjustment bytecounts > actual deltas in the snapshot. deltaTxWiFiBytes = %llu, adjustmentTxWiFiBytes = %llu"
- "VPN adjustment bytecounts > actual deltas in the snapshot. deltaTxWiredBytes = %llu, adjustmentTxWiredBytes = %llu"
- "[11{provider_counts=\"numSrcsAdded\"Q\"numUpdatesOnOpen\"Q\"numUpdatesOnPoll\"Q\"numUpdatesOnEvent\"Q\"numUpdatesOnClose\"Q}]"
- "^{accumulator_bytes=QQQQQQQQ}16@0:8"
- "^{update_subset_for_deltas=QQQQQQQQQQQQIII}16@0:8"
- "_adjustedByteCount:otherBytes:packets:"
- "_bluetooth_counts"
- "_deltaForCurrentBytes:otherBytes:packets:prevBytes:prevOtherBytes:prevPackets:"
- "_nstatBluetoothCounts"
- "_nstatConnUpdate"
- "_nstatCountsDictionaryForm:"
- "_nstatQUICUpdate"
- "_nstatTCPUpdate"
- "_nstatUDPUpdate"
- "_nstat_update"
- "_quicDescriptorDictionaryForm:"
- "_tcpDescriptorDictionaryForm:"
- "_udpDescriptorDictionaryForm:"
- "_update_adjustment_bytes"
- "_update_delta_ptr"
- "_update_ptr"
- "adjustment bytecounts > actual deltas in the snapshot. deltaRxCompanionLinkBluetoothBytes = %llu, adjustmentRxCompanionLinkBluetoothBytes = %llu"
- "adjustment bytecounts > actual deltas in the snapshot. deltaTxCompanionLinkBluetoothBytes = %llu, adjustmentTxCompanionLinkBluetoothBytes = %llu"
- "count rx/tx pkts %lld %lld bytes %lld %lld cell %lld %lld wifi %lld %lld wired %lld %lld dup %d ooo %d retx %d"
- "counts != NULL"
- "handleDomainUpdate:"
- "initWithConnUpdate:startTime:flowFlags:"
- "initWithUpdate:length:monitor:"
- "initWithUpdate:startTime:flowFlags:previously:bluetoothCounts:peerEgressCellularCounts:"
- "itemLength >= sizeof(nstat_interface_counts)"
- "length >= sizeof(nstat_interface_counts)"
- "local"
- "nstat_connectattempts"
- "nstat_connectsuccesses"
- "nstat_wifi_rxbytes"
- "nstat_wifi_txbytes"
- "processExtendedUpdate:length:"
- "processExtendedUpdate:length:bluetoothCounts:"
- "r^{nstat_msg_src_update_convenient={nstat_msg_src_update_hdr={nstat_msg_hdr=QISS}QQ{nstat_counts=QQQQQQQQQQIIIIIIII}I[4C]}(?={nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_udp_descriptor=QQQQ{activity_bitmap=Q[2Q]}(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})IIIII[64c]I[16C][16C][16C][16C]IIIC[3C]}{nstat_route_descriptor=QQQ(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I}{sockaddr=CC[14c]})II[4C]}{nstat_ifnet_descriptor=QI{nstat_ifnet_desc_link_status=I(?={nstat_ifnet_desc_cellular_status=IIIIIIIIIIIIIIIIS[2C]}{nstat_ifnet_desc_wifi_status=IIIIIIIIIIIIIIIIIIII})}I[128c][17c][3C]}{nstat_sysinfo_descriptor=I}{nstat_tcp_descriptor=QQQQQQ{activity_bitmap=Q[2Q]}IIIIIIIIIIIII(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})(?={sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})[16c][64c][16C][16C][16C][16C]II(?={tcp_conn_status=(?={?=b1b1b1b1}I)}[4C])IC[3C]}{nstat_connection_descriptor=QQQQIII[64c][16C][16C][16C][16C][16C]II[4C]})}16@0:8"
- "r^{update_subset_for_deltas=QQQQQQQQQQQQIII}16@0:8"
- "remote"
- "saveOldBTCounts:"
- "saved rx/tx cell %lld %lld wifi %lld %lld wired %lld %lld bt %lld %lld"
- "saved rx/tx pkts %lld %lld bytes %lld %lld cell %lld %lld wifi %lld %lld wired %lld %lld dup %d ooo %d retx %d"
- "savedRxWiFiBytes"
- "savedTxWiFiBytes"
- "tbd"
- "update"
- "updateWithUpdate:length:monitor:"
- "v24@0:8^{nstat_counts=QQQQQQQQQQIIIIIIII}16"
- "{accumulator_bytes=\"rxCellularBytes\"Q\"rxWiFiBytes\"Q\"rxWiredBytes\"Q\"rxCompanionLinkBluetoothBytes\"Q\"txCellularBytes\"Q\"txWiFiBytes\"Q\"txWiredBytes\"Q\"txCompanionLinkBluetoothBytes\"Q}"
- "{nstat_interface_counts=\"nstat_rxpackets\"Q\"nstat_rxbytes\"Q\"nstat_txpackets\"Q\"nstat_txbytes\"Q}"
- "{nstat_msg_src_update_conn=\"hdr\"{nstat_msg_hdr=\"context\"Q\"type\"I\"length\"S\"flags\"S}\"srcref\"Q\"event_flags\"Q\"counts\"{nstat_counts=\"nstat_rxpackets\"Q\"nstat_rxbytes\"Q\"nstat_txpackets\"Q\"nstat_txbytes\"Q\"nstat_cell_rxbytes\"Q\"nstat_cell_txbytes\"Q\"nstat_wifi_rxbytes\"Q\"nstat_wifi_txbytes\"Q\"nstat_wired_rxbytes\"Q\"nstat_wired_txbytes\"Q\"nstat_rxduplicatebytes\"I\"nstat_rxoutoforderbytes\"I\"nstat_txretransmit\"I\"nstat_connectattempts\"I\"nstat_connectsuccesses\"I\"nstat_min_rtt\"I\"nstat_avg_rtt\"I\"nstat_var_rtt\"I}\"provider\"I\"reserved\"[4C]\"conn_desc\"{nstat_connection_descriptor=\"start_timestamp\"Q\"timestamp\"Q\"upid\"Q\"eupid\"Q\"pid\"I\"epid\"I\"ifnet_properties\"I\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"cuuid\"[16C]\"puuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"reserved\"[4C]}}"
- "{nstat_msg_src_update_convenient=\"hdr\"{nstat_msg_src_update_hdr=\"hdr\"{nstat_msg_hdr=\"context\"Q\"type\"I\"length\"S\"flags\"S}\"srcref\"Q\"event_flags\"Q\"counts\"{nstat_counts=\"nstat_rxpackets\"Q\"nstat_rxbytes\"Q\"nstat_txpackets\"Q\"nstat_txbytes\"Q\"nstat_cell_rxbytes\"Q\"nstat_cell_txbytes\"Q\"nstat_wifi_rxbytes\"Q\"nstat_wifi_txbytes\"Q\"nstat_wired_rxbytes\"Q\"nstat_wired_txbytes\"Q\"nstat_rxduplicatebytes\"I\"nstat_rxoutoforderbytes\"I\"nstat_txretransmit\"I\"nstat_connectattempts\"I\"nstat_connectsuccesses\"I\"nstat_min_rtt\"I\"nstat_avg_rtt\"I\"nstat_var_rtt\"I}\"provider\"I\"reserved\"[4C]}\"\"(?=\"tcp\"{nstat_tcp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"rx_transfer_size\"Q\"tx_transfer_size\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"ifindex\"I\"state\"I\"sndbufsize\"I\"sndbufused\"I\"rcvbufsize\"I\"rcvbufused\"I\"txunacked\"I\"txwindow\"I\"txcwindow\"I\"traffic_class\"I\"traffic_mgt_flags\"I\"pid\"I\"epid\"I\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"cc_algo\"[16c]\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"\"(?=\"connstatus\"{tcp_conn_status=\"\"(?=\"\"{?=\"probe_activated\"b1\"write_probe_failed\"b1\"read_probe_failed\"b1\"conn_probe_failed\"b1}\"pad_field\"I)}\"__pad_connstatus\"[4C])\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}\"udp\"{nstat_udp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"ifindex\"I\"rcvbufsize\"I\"rcvbufused\"I\"traffic_class\"I\"pid\"I\"pname\"[64c]\"epid\"I\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}\"route\"{nstat_route_descriptor=\"id\"Q\"parent_id\"Q\"gateway_id\"Q\"dst\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I}\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]})\"mask\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I}\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]})\"gateway\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I}\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]})\"ifindex\"I\"flags\"I\"reserved\"[4C]}\"ifnet\"{nstat_ifnet_descriptor=\"threshold\"Q\"ifindex\"I\"link_status\"{nstat_ifnet_desc_link_status=\"link_status_type\"I\"u\"(?=\"cellular\"{nstat_ifnet_desc_cellular_status=\"valid_bitmask\"I\"link_quality_metric\"I\"ul_effective_bandwidth\"I\"ul_max_bandwidth\"I\"ul_min_latency\"I\"ul_effective_latency\"I\"ul_max_latency\"I\"ul_retxt_level\"I\"ul_bytes_lost\"I\"ul_min_queue_size\"I\"ul_avg_queue_size\"I\"ul_max_queue_size\"I\"dl_effective_bandwidth\"I\"dl_max_bandwidth\"I\"config_inactivity_time\"I\"config_backoff_time\"I\"mss_recommended\"S\"reserved\"[2C]}\"wifi\"{nstat_ifnet_desc_wifi_status=\"valid_bitmask\"I\"link_quality_metric\"I\"ul_effective_bandwidth\"I\"ul_max_bandwidth\"I\"ul_min_latency\"I\"ul_effective_latency\"I\"ul_max_latency\"I\"ul_retxt_level\"I\"ul_bytes_lost\"I\"ul_error_rate\"I\"dl_effective_bandwidth\"I\"dl_max_bandwidth\"I\"dl_min_latency\"I\"dl_effective_latency\"I\"dl_max_latency\"I\"dl_error_rate\"I\"config_frequency\"I\"config_multicast_rate\"I\"scan_count\"I\"scan_duration\"I})}\"type\"I\"description\"[128c]\"name\"[17c]\"reserved\"[3C]}\"sysinfo\"{nstat_sysinfo_descriptor=\"flags\"I}\"quic\"{nstat_tcp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"rx_transfer_size\"Q\"tx_transfer_size\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"ifindex\"I\"state\"I\"sndbufsize\"I\"sndbufused\"I\"rcvbufsize\"I\"rcvbufused\"I\"txunacked\"I\"txwindow\"I\"txcwindow\"I\"traffic_class\"I\"traffic_mgt_flags\"I\"pid\"I\"epid\"I\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"cc_algo\"[16c]\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"\"(?=\"connstatus\"{tcp_conn_status=\"\"(?=\"\"{?=\"probe_activated\"b1\"write_probe_failed\"b1\"read_probe_failed\"b1\"conn_probe_failed\"b1}\"pad_field\"I)}\"__pad_connstatus\"[4C])\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}\"conn\"{nstat_connection_descriptor=\"start_timestamp\"Q\"timestamp\"Q\"upid\"Q\"eupid\"Q\"pid\"I\"epid\"I\"ifnet_properties\"I\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"cuuid\"[16C]\"puuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"reserved\"[4C]})}"
- "{nstat_msg_src_update_quic=\"hdr\"{nstat_msg_hdr=\"context\"Q\"type\"I\"length\"S\"flags\"S}\"srcref\"Q\"event_flags\"Q\"counts\"{nstat_counts=\"nstat_rxpackets\"Q\"nstat_rxbytes\"Q\"nstat_txpackets\"Q\"nstat_txbytes\"Q\"nstat_cell_rxbytes\"Q\"nstat_cell_txbytes\"Q\"nstat_wifi_rxbytes\"Q\"nstat_wifi_txbytes\"Q\"nstat_wired_rxbytes\"Q\"nstat_wired_txbytes\"Q\"nstat_rxduplicatebytes\"I\"nstat_rxoutoforderbytes\"I\"nstat_txretransmit\"I\"nstat_connectattempts\"I\"nstat_connectsuccesses\"I\"nstat_min_rtt\"I\"nstat_avg_rtt\"I\"nstat_var_rtt\"I}\"provider\"I\"reserved\"[4C]\"quic_desc\"{nstat_tcp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"rx_transfer_size\"Q\"tx_transfer_size\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"ifindex\"I\"state\"I\"sndbufsize\"I\"sndbufused\"I\"rcvbufsize\"I\"rcvbufused\"I\"txunacked\"I\"txwindow\"I\"txcwindow\"I\"traffic_class\"I\"traffic_mgt_flags\"I\"pid\"I\"epid\"I\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"cc_algo\"[16c]\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"\"(?=\"connstatus\"{tcp_conn_status=\"\"(?=\"\"{?=\"probe_activated\"b1\"write_probe_failed\"b1\"read_probe_failed\"b1\"conn_probe_failed\"b1}\"pad_field\"I)}\"__pad_connstatus\"[4C])\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}}"
- "{nstat_msg_src_update_tcp=\"hdr\"{nstat_msg_hdr=\"context\"Q\"type\"I\"length\"S\"flags\"S}\"srcref\"Q\"event_flags\"Q\"counts\"{nstat_counts=\"nstat_rxpackets\"Q\"nstat_rxbytes\"Q\"nstat_txpackets\"Q\"nstat_txbytes\"Q\"nstat_cell_rxbytes\"Q\"nstat_cell_txbytes\"Q\"nstat_wifi_rxbytes\"Q\"nstat_wifi_txbytes\"Q\"nstat_wired_rxbytes\"Q\"nstat_wired_txbytes\"Q\"nstat_rxduplicatebytes\"I\"nstat_rxoutoforderbytes\"I\"nstat_txretransmit\"I\"nstat_connectattempts\"I\"nstat_connectsuccesses\"I\"nstat_min_rtt\"I\"nstat_avg_rtt\"I\"nstat_var_rtt\"I}\"provider\"I\"reserved\"[4C]\"tcp_desc\"{nstat_tcp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"rx_transfer_size\"Q\"tx_transfer_size\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"ifindex\"I\"state\"I\"sndbufsize\"I\"sndbufused\"I\"rcvbufsize\"I\"rcvbufused\"I\"txunacked\"I\"txwindow\"I\"txcwindow\"I\"traffic_class\"I\"traffic_mgt_flags\"I\"pid\"I\"epid\"I\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"cc_algo\"[16c]\"pname\"[64c]\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"\"(?=\"connstatus\"{tcp_conn_status=\"\"(?=\"\"{?=\"probe_activated\"b1\"write_probe_failed\"b1\"read_probe_failed\"b1\"conn_probe_failed\"b1}\"pad_field\"I)}\"__pad_connstatus\"[4C])\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}}"
- "{nstat_msg_src_update_udp=\"hdr\"{nstat_msg_hdr=\"context\"Q\"type\"I\"length\"S\"flags\"S}\"srcref\"Q\"event_flags\"Q\"counts\"{nstat_counts=\"nstat_rxpackets\"Q\"nstat_rxbytes\"Q\"nstat_txpackets\"Q\"nstat_txbytes\"Q\"nstat_cell_rxbytes\"Q\"nstat_cell_txbytes\"Q\"nstat_wifi_rxbytes\"Q\"nstat_wifi_txbytes\"Q\"nstat_wired_rxbytes\"Q\"nstat_wired_txbytes\"Q\"nstat_rxduplicatebytes\"I\"nstat_rxoutoforderbytes\"I\"nstat_txretransmit\"I\"nstat_connectattempts\"I\"nstat_connectsuccesses\"I\"nstat_min_rtt\"I\"nstat_avg_rtt\"I\"nstat_var_rtt\"I}\"provider\"I\"reserved\"[4C]\"udp_desc\"{nstat_udp_descriptor=\"upid\"Q\"eupid\"Q\"start_timestamp\"Q\"timestamp\"Q\"activity_bitmap\"{activity_bitmap=\"start\"Q\"bitmap\"[2Q]}\"local\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"remote\"(?=\"v4\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"v6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"sin6_port\"S\"sin6_flowinfo\"I\"sin6_addr\"{in6_addr=\"__u6_addr\"(?=\"__u6_addr8\"[16C]\"__u6_addr16\"[8S]\"__u6_addr32\"[4I])}\"sin6_scope_id\"I})\"ifindex\"I\"rcvbufsize\"I\"rcvbufused\"I\"traffic_class\"I\"pid\"I\"pname\"[64c]\"epid\"I\"uuid\"[16C]\"euuid\"[16C]\"vuuid\"[16C]\"fuuid\"[16C]\"persona_id\"I\"uid\"I\"ifnet_properties\"I\"fallback_mode\"C\"reserved\"[3C]}}"
- "{update_subset_for_deltas=\"savedRxPackets\"Q\"savedRxBytes\"Q\"savedTxPackets\"Q\"savedTxBytes\"Q\"savedRxCellularBytes\"Q\"savedRxWiFiBytes\"Q\"savedRxWiredBytes\"Q\"savedRxCompanionLinkBluetoothBytes\"Q\"savedTxCellularBytes\"Q\"savedTxWiFiBytes\"Q\"savedTxWiredBytes\"Q\"savedTxCompanionLinkBluetoothBytes\"Q\"savedRxDuplicateBytes\"I\"savedRxOutOfOrderBytes\"I\"savedTxRetransmittedBytes\"I}"
- "\xf0H"
- "\xf0\xf0\xf0\xd1"
- "\xf0\xf0\xf0\xf0a"
- "\xf0\xf0\xf0\xf0\xf0\xf0rV"

```
