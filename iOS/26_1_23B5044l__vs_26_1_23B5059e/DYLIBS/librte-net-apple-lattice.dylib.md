## librte-net-apple-lattice.dylib

> `/usr/lib/dpdk/pmds/librte-net-apple-lattice.dylib`

```diff

-146.0.0.0.0
-  __TEXT.__text: 0xc990
-  __TEXT.__auth_stubs: 0x730
+151.0.0.0.0
+  __TEXT.__text: 0xecdc
+  __TEXT.__auth_stubs: 0x770
   __TEXT.__init_offsets: 0xc
-  __TEXT.__gcc_except_tab: 0x560
-  __TEXT.__const: 0x5e4
-  __TEXT.__cstring: 0x1cfc
-  __TEXT.__oslogstring: 0x341
-  __TEXT.__unwind_info: 0x5c8
+  __TEXT.__gcc_except_tab: 0x4f8
+  __TEXT.__const: 0x554
+  __TEXT.__cstring: 0x275a
+  __TEXT.__oslogstring: 0x531
+  __TEXT.__unwind_info: 0x5d8
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__const: 0x58
-  __AUTH_CONST.__auth_got: 0x3a0
-  __AUTH_CONST.__const: 0x578
+  __AUTH_CONST.__auth_got: 0x3c0
+  __AUTH_CONST.__const: 0x568
   __AUTH.__data: 0x58
-  __DATA.__data: 0x270
-  __DATA.__common: 0xec0
-  __DATA.__bss: 0x4e0
+  __DATA.__data: 0x2b8
+  __DATA.__common: 0x1028
+  __DATA.__bss: 0x870
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdpdk.dylib
-  UUID: FEFEE28C-9994-33CF-8FE9-738F9154651E
-  Functions: 320
-  Symbols:   812
-  CStrings:  292
+  UUID: FD21EAED-F168-382F-BFE8-EC7EC0A619C0
+  Functions: 407
+  Symbols:   917
+  CStrings:  378
 
Symbols:
+ GCC_except_table108
+ GCC_except_table109
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table16
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table28
+ GCC_except_table49
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table57
+ GCC_except_table70
+ GCC_except_table78
+ GCC_except_table79
+ GCC_except_table8
+ GCC_except_table84
+ GCC_except_table86
+ GCC_except_table91
+ GCC_except_table99
+ _OUTLINED_FUNCTION_2
+ __ZN10RingDriver14onNotificationEhj
+ __ZN13MetricsLogger11appendBodyfEPKcz
+ __ZN13MetricsLogger11logCountersEy
+ __ZN13MetricsLogger13appendFooterfEPKcz
+ __ZN13MetricsLogger13appendHeaderfEPKcz
+ __ZN13MetricsLogger4initEPFvPKcS1_S1_E
+ __ZN13MetricsLogger5startEv
+ __ZN13MetricsLogger6BufferILm256EE5resetEv
+ __ZN13MetricsLogger6BufferILm256EE8vappendfEPKcPc
+ __ZN13MetricsLogger6BufferILm256EEC1Ev
+ __ZN13MetricsLogger6BufferILm256EEC2Ev
+ __ZN13MetricsLogger6BufferILm64EE5resetEv
+ __ZN13MetricsLogger6BufferILm64EE8vappendfEPKcPc
+ __ZN13MetricsLogger6BufferILm64EEC1Ev
+ __ZN13MetricsLogger6BufferILm64EEC2Ev
+ __ZN13MetricsLogger6BufferILm704EE5resetEv
+ __ZN13MetricsLogger6BufferILm704EE8vappendfEPKcPc
+ __ZN13MetricsLogger6BufferILm704EEC1Ev
+ __ZN13MetricsLogger6BufferILm704EEC2Ev
+ __ZN13MetricsLogger6finishEv
+ __ZN13MetricsLoggerC1Ev
+ __ZN13MetricsLoggerC2Ev
+ __ZN5AU4RN17RingServiceClient11unmapMemoryINS_18NHIDescriptorRingsEEEvRPT_j
+ __ZN5AU4RN17RingServiceClient11unmapMemoryIvEEvRPT_j
+ __ZN5AU4RN17RingServiceClient16shutdownNHILinksEv
+ __ZN5AU4RN17RingServiceClient17mapMemoryAnywhereINS_18NHIDescriptorRingsEEEPT_jjPy
+ __ZN5AU4RN17RingServiceClient17mapMemoryAnywhereIvEEPT_jjPy
+ __ZN5AU4RN17RingServiceClient17nhiRegistersTypesE
+ __ZN5AU4RN17RingServiceClient18initializeNHILinksEv
+ __ZN5AU4RN17RingServiceClient18linkChangeCompleteENS_9LinkIndexENS_9LinkStateE
+ __ZN5AU4RN17RingServiceClient20getCIOMemoryMappingsENS_9LinkIndexE
+ __ZN5AU4RN17RingServiceClient22removeLatticeInterfaceEN7Lattice19ExternalInterfaceIdE
+ __ZN5AU4RN17RingServiceClient23nhiDescriptorRingsTypesE
+ __ZN5AU4RN6VectorINS_15LinkStateChangeEE11setCapacityEm
+ __ZN5AU4RN6VectorINS_15LinkStateChangeEE4pushERKS1_
+ __ZN5AU4RN7NHILink4pathENS_9PathIndexE
+ __ZN5AU4RN7NHILink5startENS_9LinkIndexEPVjPNS_18NHIDescriptorRingsE
+ __ZN5AU4RN7NHILink6linkUpERKNS_13CIOMemoryInfoE
+ __ZN5AU4RN7NHILink8linkDownEv
+ __ZN5AU4RN7NHILink8shutdownEv
+ __ZN5AU4RN7NHILinkC1Ev
+ __ZN5AU4RN7NHILinkC2Ev
+ __ZN5AU4RN7NHIPath5startENS_9LinkIndexENS_9PathIndexEPVjPNS_18NHIDescriptorRingsE
+ __ZN5AU4RN7NHIPath6linkUpERKNS_13CIOMemoryInfoE
+ __ZN5AU4RN7NHIPath8linkDownEv
+ __ZN5AU4RN7NHIPath8shutdownEv
+ __ZN5AU4RN7NHIPathC1Ev
+ __ZN5AU4RN7NHIPathC2Ev
+ __ZN5AU4RN7NHIRing12readRegisterEj
+ __ZN5AU4RN7NHIRing12readRegisterEj.cold.1
+ __ZN5AU4RN7NHIRing13writeRegisterEjj
+ __ZN5AU4RN7NHIRing13writeRegisterEjj.cold.1
+ __ZN5AU4RN7NHIRing25translateToCIODPDKAddressEjj
+ __ZN5AU4RN7NHIRing25translateToCIODPDKAddressEjj.cold.1
+ __ZN5AU4RN7NHIRing25translateToCIODPDKAddressEjj.cold.2
+ __ZN5AU4RN7NHIRing27translateFromCIODPDKAddressEyj
+ __ZN5AU4RN7NHIRing27translateFromCIODPDKAddressEyj.cold.1
+ __ZN5AU4RN7NHIRing27translateFromCIODPDKAddressEyj.cold.2
+ __ZN5AU4RN7NHIRing27translateFromCIODPDKAddressEyj.cold.3
+ __ZN5AU4RN9NHIRxRing12completePushEv
+ __ZN5AU4RN9NHIRxRing3popERjRtRNS_9SlitIndexE
+ __ZN5AU4RN9NHIRxRing4pushEjt
+ __ZN5AU4RN9NHIRxRing5startENS_9LinkIndexENS_9PathIndexEPVjPNS_18NHIDescriptorRingsE
+ __ZN5AU4RN9NHIRxRing5startENS_9LinkIndexENS_9PathIndexEPVjPNS_18NHIDescriptorRingsE.cold.1
+ __ZN5AU4RN9NHIRxRing5startENS_9LinkIndexENS_9PathIndexEPVjPNS_18NHIDescriptorRingsE.cold.2
+ __ZN5AU4RN9NHIRxRing6linkUpERKNS_13CIOMemoryInfoE
+ __ZN5AU4RN9NHIRxRing7popDownERjRtRNS_9SlitIndexE
+ __ZN5AU4RN9NHIRxRing8linkDownEv
+ __ZN5AU4RN9NHITxRing12completePushEv
+ __ZN5AU4RN9NHITxRing3popERjRtRNS_9SlitIndexERNS_11TxPoolIndexE
+ __ZN5AU4RN9NHITxRing4pushEjtNS_9SlitIndexENS_11TxPoolIndexE
+ __ZN5AU4RN9NHITxRing5startENS_9LinkIndexENS_9PathIndexEPVjPNS_18NHIDescriptorRingsE
+ __ZN5AU4RN9NHITxRing5startENS_9LinkIndexENS_9PathIndexEPVjPNS_18NHIDescriptorRingsE.cold.1
+ __ZN5AU4RN9NHITxRing5startENS_9LinkIndexENS_9PathIndexEPVjPNS_18NHIDescriptorRingsE.cold.2
+ __ZN5AU4RN9NHITxRing6linkUpERKNS_13CIOMemoryInfoE
+ __ZN5AU4RN9NHITxRing6linkUpERKNS_13CIOMemoryInfoE.cold.1
+ __ZN5AU4RN9NHITxRing6linkUpERKNS_13CIOMemoryInfoE.cold.2
+ __ZN5AU4RN9NHITxRing6linkUpERKNS_13CIOMemoryInfoE.cold.3
+ __ZN5AU4RN9NHITxRing7popDownERjRtRNS_9SlitIndexERNS_11TxPoolIndexE
+ __ZN5AU4RN9NHITxRing8linkDownEv
+ __ZN7Lattice10DPDKSystem12prepareNHIRxEP11rte_mempoolN5AU4RN9LinkIndexE
+ __ZN7Lattice10DPDKSystem13sendLockedNHIERNS_8DPDKMBufENS_11EgressRouteEN5AU4RN11TxPoolIndexE
+ __ZN7Lattice10DPDKSystem19sendLockedHostRingsERNS_8DPDKMBufENS_11EgressRouteEN5AU4RN11TxPoolIndexE
+ __ZN7Lattice10DPDKSystem21handleLinkStateChangeEN5AU4RN9LinkIndexENS1_9LinkStateE
+ __ZN7Lattice10DPDKSystem29processNHITxCompletionsLockedEv
+ __ZN7Lattice10DPDKSystem5rxNHIEP11rte_mempoolPP8rte_mbuftN5AU4RN9LinkIndexE
+ __ZN7Lattice10DPDKSystem5txNHIEPP8rte_mbuft
+ __ZN7Lattice13LatticeRouter17routeEgressPacketINS_8DPDKMBufEEENS_19EgressRouteDecisionERT_NS_19InternalInterfaceIdENS_18LatticeHeaderFlagsE
+ __ZN7Lattice13LatticeRouter18routeIngressPacketINS_10DPDKSystemEEENS_20IngressRouteDecisionERT_RNS4_4MBufEN5AU4RN9LinkIndexENS8_9SlitIndexE
+ __ZN7Lattice13LatticeRouter27routeEgressPacketBridgeModeINS_8DPDKMBufEEENS_19EgressRouteDecisionERT_NS_19InternalInterfaceIdENS_18LatticeHeaderFlagsE
+ __ZN7Lattice13LatticeRouter28routeEgressPacketComputeModeINS_8DPDKMBufEEENS_19EgressRouteDecisionERT_NS_19InternalInterfaceIdENS_18LatticeHeaderFlagsE
+ __ZN7Lattice13LatticeRouter4initEN5AU4RN9SlotIndexENS1_17LatticeRouterModeEyyy.cold.1
+ __ZN7Lattice13LatticeRouter4initEN5AU4RN9SlotIndexENS1_17LatticeRouterModeEyyy.cold.2
+ __ZN7Lattice14InterfaceTable12addInterfaceERKNS_14LocalInterfaceE
+ __ZN7Lattice14InterfaceTable15removeInterfaceEPNS_14LocalInterfaceE
+ __ZN7Lattice14InterfaceTable20ensurePortIdAssignedEPNS_14LocalInterfaceE
+ __ZN7Lattice14InterfaceTable20ensurePortIdAssignedEPNS_14LocalInterfaceE.cold.1
+ __ZN7Lattice14InterfaceTable28addOrUpdateInterfaceOnBridgeERKNS_14LocalInterfaceE
+ __ZN7Lattice14InterfaceTable28addOrUpdateInterfaceOnBridgeERKNS_14LocalInterfaceE.cold.1
+ __ZN7Lattice14InterfaceTable33addOrUpdateInterfaceOnComputeNodeERKNS_14LocalInterfaceE
+ __ZN7Lattice14InterfaceTable33addOrUpdateInterfaceOnComputeNodeERKNS_14LocalInterfaceE.cold.1
+ __ZN7Lattice14InterfaceTable37removeInterfaceOnComputeNodeFromTableERKNS_19ExternalInterfaceIdE
+ __ZN7Lattice14InterfaceTable38addOrGetInterfaceOnComputeNodeFromUserERNS_14LocalInterfaceE
+ __ZN7Lattice14InterfaceTable38addOrGetInterfaceOnComputeNodeFromUserERNS_14LocalInterfaceE.cold.1
+ __ZN7Lattice15LinkStatusTable23computeLinkStateChangesERN5AU4RN6VectorINS1_15LinkStateChangeEEEy
+ __ZN7Lattice8DPDKMBuf10makeDirectEv
+ __ZN7LatticeL13osLogFunctionEPKcS1_S1_
+ __ZN7LatticeL40rte_pmd_lattice_set_rx_tx_checksum_flagsEP8rte_mbuf
+ __ZNK13MetricsLogger6BufferILm256EE5c_strEv
+ __ZNK13MetricsLogger6BufferILm256EE6lengthEv
+ __ZNK13MetricsLogger6BufferILm256EE7isEmptyEv
+ __ZNK13MetricsLogger6BufferILm256EE9remainingEv
+ __ZNK13MetricsLogger6BufferILm64EE5c_strEv
+ __ZNK13MetricsLogger6BufferILm64EE6lengthEv
+ __ZNK13MetricsLogger6BufferILm64EE7isEmptyEv
+ __ZNK13MetricsLogger6BufferILm64EE9remainingEv
+ __ZNK13MetricsLogger6BufferILm704EE5c_strEv
+ __ZNK13MetricsLogger6BufferILm704EE6lengthEv
+ __ZNK13MetricsLogger6BufferILm704EE7isEmptyEv
+ __ZNK13MetricsLogger6BufferILm704EE9remainingEv
+ __ZNKSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEE11target_typeEv
+ __ZNKSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEE6targetERKSt9type_info
+ __ZNKSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEE7__cloneEPNS0_6__baseIS7_EE
+ __ZNKSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEE7__cloneEv
+ __ZNSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEE7destroyEv
+ __ZNSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEED0Ev
+ __ZNSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEED1Ev
+ __ZNSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEEclEv
+ __ZTINSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEEE
+ __ZTIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1
+ __ZTSNSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEEE
+ __ZTSZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1
+ __ZTVNSt3__110__function6__funcIZN7Lattice10DPDKSystem22startBackgroundThreadsEvE3$_1NS_9allocatorIS4_EEFvvEEE
+ _dpdk_descriptor_offset_to_mbuf_with_length
+ _dpdk_descriptor_offset_to_mbuf_with_length.cold.1
+ _dpdk_descriptor_offset_to_mbuf_with_length.cold.2
+ _dpdk_descriptor_offset_to_mbuf_with_length.cold.3
+ _dpdk_descriptor_offset_to_mbuf_with_length.cold.4
+ _dpdk_descriptor_offset_to_mbuf_with_length.cold.5
+ _eth_applesio_lattice_nhi_rx
+ _eth_applesio_lattice_nhi_tx
+ _increment_tx_copy_counter
+ _ring_driver_add_interface.cold.3
+ _ring_driver_get_lattice_mode
+ _ring_driver_lattice_nhi_prepare
+ _ring_driver_lattice_nhi_rx
+ _ring_driver_lattice_nhi_tx
+ _ring_driver_list_interfaces.cold.1
+ _ring_driver_print_counters
+ _ring_driver_process_tx_completions_locked
+ _ring_driver_process_tx_completions_locked.cold.1
+ _ring_driver_process_tx_completions_locked.cold.2
+ _ring_driver_process_tx_completions_locked.cold.3
+ _ring_driver_process_tx_completions_locked.cold.4
+ _ring_driver_remove_interface.cold.1
+ _ring_driver_start_publishing.cold.1
+ _rte_net_get_ptype
+ _rte_pktmbuf_copy
+ _rte_pmd_print_counters
+ _vsnprintf
- GCC_except_table100
- GCC_except_table101
- GCC_except_table102
- GCC_except_table105
- GCC_except_table118
- GCC_except_table123
- GCC_except_table126
- GCC_except_table22
- GCC_except_table25
- GCC_except_table27
- GCC_except_table29
- GCC_except_table3
- GCC_except_table33
- GCC_except_table38
- GCC_except_table4
- GCC_except_table45
- GCC_except_table46
- GCC_except_table5
- GCC_except_table58
- GCC_except_table60
- GCC_except_table61
- GCC_except_table62
- GCC_except_table63
- GCC_except_table66
- GCC_except_table72
- GCC_except_table73
- GCC_except_table74
- GCC_except_table77
- GCC_except_table81
- GCC_except_table92
- GCC_except_table93
- __ZN10RingDriver14onNotificationEht
- __ZN10RingDriver14updateLimitersEv
- __ZN10RingDriver16updateRouteTableEv
- __ZN10RingDriver21reportEgressBytesUsedEy
- __ZN10RingDriver22reportIngressBytesUsedEy
- __ZN18BandwidthCollector4stopEv
- __ZN18BandwidthCollector5startENSt3__18functionIFvRKNS_16IncrementalUsageEEEENS0_6chrono8durationIxNS0_5ratioILl1ELl1000EEEEE
- __ZN18BandwidthCollectorD2Ev
- __ZN5AU4RN12PacketRouter5routeEPh
- __ZN5AU4RN17RingServiceClient11reportUsageERKN18BandwidthCollector16IncrementalUsageE
- __ZN5AU4RN17RingServiceClient14getLimiterDataEv
- __ZN5AU4RN17RingServiceClient17getRouteTableDataEv
- __ZN5AU4RN17RingServiceClient22removeLatticeInterfaceEN7Lattice19InternalInterfaceIdE
- __ZN5AU4RN17RingServiceClientC2ERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj.cold.1
- __ZN5AU4RN4Lock4withIZNS_12PacketRouter19onRouteTableChangedERKN35AppleLatticeDPDKUserClientInterface14RouteTableDataEEUlvE_EEvOT_
- __ZN5AU4RN6VectorIN7Lattice15LinkStatusTable15LinkStateChangeEE11setCapacityEm
- __ZN5AU4RN6VectorIN7Lattice15LinkStatusTable15LinkStateChangeEE4pushERKS3_
- __ZN5AU4RN7Limiter11drainBucketEy
- __ZN5AU4RN7Limiter14shouldThrottleEyy
- __ZN7Lattice13LatticeRouter17routeEgressPacketINS_8DPDKMBufEEENS_19EgressRouteDecisionERT_NS_19InternalInterfaceIdE
- __ZN7Lattice13LatticeRouter18routeIngressPacketINS_10DPDKSystemEEENS_20IngressRouteDecisionERT_RNS4_4MBufEN5AU4RN9LinkIndexE
- __ZN7Lattice13LatticeRouter27routeEgressPacketBridgeModeINS_8DPDKMBufEEENS_19EgressRouteDecisionERT_NS_19InternalInterfaceIdE
- __ZN7Lattice13LatticeRouter28routeEgressPacketComputeModeINS_8DPDKMBufEEENS_19EgressRouteDecisionERT_NS_19InternalInterfaceIdE
- __ZN7Lattice14InterfaceTable12addInterfaceERNS_14LocalInterfaceE
- __ZN7Lattice14InterfaceTable15removeInterfaceERKNS_19ExternalInterfaceIdE
- __ZN7Lattice14InterfaceTable20addOrUpdateInterfaceERNS_14LocalInterfaceE
- __ZN7Lattice14InterfaceTable20addOrUpdateInterfaceERNS_14LocalInterfaceE.cold.1
- __ZN7Lattice14InterfaceTable20addOrUpdateInterfaceERNS_14LocalInterfaceE.cold.2
- __ZN7Lattice15LinkStatusTable23computeLinkStateChangesERN5AU4RN6VectorINS0_15LinkStateChangeEEEy
- __ZN7Lattice8DPDKMBufC2EP11rte_mempool
- __ZN7Lattice8DPDKMBufC2EP11rte_mempool.cold.1
- __ZN7Lattice8DPDKMBufC2EP11rte_mempool.cold.2
- __ZNK35AppleLatticeDPDKUserClientInterface19GetRingModeResponse19getLatticeRouteModeEv
- __ZNKSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EE11target_typeEv
- __ZNKSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EE6targetERKSt9type_info
- __ZNKSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EE7__cloneEPNS0_6__baseISE_EE
- __ZNKSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EE7__cloneEv
- __ZNSt3__110__function12__value_funcIFvRKN18BandwidthCollector16IncrementalUsageEEE4swapB8ne200100ERS7_
- __ZNSt3__110__function12__value_funcIFvRKN18BandwidthCollector16IncrementalUsageEEEC2B8ne200100ERKS7_
- __ZNSt3__110__function12__value_funcIFvRKN18BandwidthCollector16IncrementalUsageEEED2B8ne200100Ev
- __ZNSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EE18destroy_deallocateEv
- __ZNSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EE7destroyEv
- __ZNSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EED0Ev
- __ZNSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EED1Ev
- __ZNSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EEclESD_
- __ZNSt3__110unique_ptrIN5AU4RN12PacketRouterENS_14default_deleteIS2_EEE5resetB8ne200100EPS2_
- __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEZN18BandwidthCollector5startENS_8functionIFvRKNS6_16IncrementalUsageEEEENS_6chrono8durationIxNS_5ratioILl1ELl1000EEEEEEUlvE_EEENS3_ISJ_EEED1B8ne200100Ev
- __ZNSt3__111unique_lockINS_5mutexEE4lockB8ne200100Ev
- __ZNSt3__114__thread_proxyB8ne200100INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEZN18BandwidthCollector5startENS_8functionIFvRKNS7_16IncrementalUsageEEEENS_6chrono8durationIxNS_5ratioILl1ELl1000EEEEEEUlvE_EEEEEPvSL_
- __ZNSt3__16threadC2IZN18BandwidthCollector5startENS_8functionIFvRKNS2_16IncrementalUsageEEEENS_6chrono8durationIxNS_5ratioILl1ELl1000EEEEEEUlvE_JELi0EEEOT_DpOT0_
- __ZNSt3__18functionIFvRKN18BandwidthCollector16IncrementalUsageEEEaSERKS6_
- __ZTINSt3__110__function6__baseIFvRKN18BandwidthCollector16IncrementalUsageEEEE
- __ZTINSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EEE
- __ZTIZN5AU4RN17RingServiceClient7connectERKNS0_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_
- __ZTSNSt3__110__function6__baseIFvRKN18BandwidthCollector16IncrementalUsageEEEE
- __ZTSNSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EEE
- __ZTSZN5AU4RN17RingServiceClient7connectERKNS0_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_
- __ZTVNSt3__110__function6__funcIZN5AU4RN17RingServiceClient7connectERKNS3_13ConnectConfigEEUlN18BandwidthCollector16IncrementalUsageEE_NS_9allocatorIS9_EEFvRKS8_EEE
- __ZZN18BandwidthCollector5startENSt3__18functionIFvRKNS_16IncrementalUsageEEEENS0_6chrono8durationIxNS0_5ratioILl1ELl1000EEEEEENKUlvE_clEv
- __ZZN5AU4RN12PacketRouter19onRouteTableChangedERKN35AppleLatticeDPDKUserClientInterface14RouteTableDataEENKUlvE_clEv
- _abort
- _eth_applesio_ring_rx
- _eth_applesio_ring_tx
- _mach_absolute_time
- _ring_driver_get_mode
- _ring_driver_prepare
- _ring_driver_process_tx_completions
- _ring_driver_ring_rx
- _ring_driver_ring_tx
CStrings:
+ "\nCounters (Non-Zero Only)\n"
+ "%s:%d Only single RX queue (queue 0) is supported, attempted queue %d\n"
+ "%s:%d Only single TX queue (queue 0) is supported, attempted queue %d\n"
+ "%{public}s%{public}s%{public}s"
+ "(%s:%d)Driver not initialized\n"
+ "(%s:%d)Failed to decode link state change from seqNum: %u\n"
+ "(%s:%d)Failed to notify kernel of link change completion for link %d\n"
+ "(%s:%d)In LatticeRouterMode::COMPUTE_NODE but localSlot is equal to 0, which is reserved for the packet bridge\n\n"
+ "(%s:%d)In LatticeRouterMode::PACKET_BRIDGE but localSlot is NOT equal to 0\n\n"
+ "(%s:%d)InternalId for interface chaging from 0x%x to 0x%x on compute node\n"
+ "(%s:%d)Received link state change notification: Link %d -> %s\n"
+ "(%s:%d)Stopped timer\n"
+ "(%s:%d)Stopping timer\n"
+ "(%s:%d)linkChangeComplete: link=%d state=%s\n"
+ "((_regsOffset + offset) & 0x3) == 0"
+ "(offset & 0x3) == 0"
+ ", \"%s\": %lld"
+ "------------------------\n"
+ "Bridge mode detected - initializing NHI links\n"
+ "Bridge mode detected - mapping NHI resources"
+ "Bring up NHI Links for link %d\n"
+ "Cached lattice mode: BRIDGE\n"
+ "Cached lattice mode: COMPUTE\n"
+ "Cannot close ioservice connection %d\n"
+ "Cannot get ringMode\n"
+ "Closed ioservice connection\n"
+ "Closing ioservice connection\n"
+ "Completed NHI link shutdown\n"
+ "Completed NHI path shutdown\n"
+ "Completed shutdown of NHI link %d\n"
+ "Completed shutdown of all NHI links\n"
+ "Compute mode detected - skipping NHI link initialization"
+ "Compute mode detected - skipping NHI resource mapping"
+ "Driver not initialized\n"
+ "Failed to decode link state change from seqNum: %u\n"
+ "Failed to get CIO memory mapping for link %d\n"
+ "Failed to get ring driver lattice mode%.0s"
+ "Failed to get ring mode during initialization\n"
+ "Failed to notify kernel of link change completion for link %d\n"
+ "Failed to prepare driver\n"
+ "Failed to start NHI link %d\n"
+ "Finished initializing NHI Links\n"
+ "IOService connection closed successfully\n"
+ "In LatticeRouterMode::COMPUTE_NODE but localSlot is equal to 0, which is reserved for the packet bridge\n\n"
+ "In LatticeRouterMode::PACKET_BRIDGE but localSlot is NOT equal to 0\n\n"
+ "InternalId for interface chaging from 0x%x to 0x%x on compute node\n"
+ "Link.cpp"
+ "Memory regions unmapped\n"
+ "NHI link initialization failed\n"
+ "NHI rings shutdown completed\n"
+ "Received link state change notification: Link %d -> %s\n"
+ "Ring driver stopped\n"
+ "RingClient.h"
+ "Shutting down NHI link %d\n"
+ "Shutting down NHI rings before ioservice release\n"
+ "Skipping shutdown of NHI link %d (Compute mode)\n"
+ "Starting NHI link shutdown\n"
+ "Starting NHI path shutdown\n"
+ "Starting shutdown of NHI links before ioservice release\n"
+ "Stopped timer\n"
+ "Stopping ring driver\n"
+ "Stopping timer\n"
+ "Unable to call LinkChangeComplete for link %d ret=%d\n"
+ "Unable to get CIO memory mappings for link %d ret=%d\n"
+ "Unable to get NHI descriptor rings memory for link %d"
+ "Unable to get NHI registers memory for link %d"
+ "Unable to get ring mode"
+ "Unknown lattice mode detected\n"
+ "Unknown ring driver lattice mode %d%.0s"
+ "Unmapping memory regions\n"
+ "Unregistering notifications\n"
+ "Using latticeRouterMode=%d"
+ "Using localSlot=%d"
+ "_memoryInfo.dpdkMemoryRegionCIOAddress != 0"
+ "bufs[bufIndex]"
+ "cioAddress + length < _memoryInfo.dpdkMemoryRegionCIOAddress + _memoryInfo.dpdkMemoryRegionLength"
+ "cioAddress >= _memoryInfo.dpdkMemoryRegionCIOAddress"
+ "dpdk_descriptor_offset_to_mbuf_with_length"
+ "ingress data packet csums maybe invalid"
+ "ingress data packet csums valid"
+ "ingress route cannot set flags"
+ "ingress route drop slit mismatch"
+ "length <= mbuf->buf_len - mbuf->data_off"
+ "linkChangeComplete: link=%d state=%s\n"
+ "linkUp"
+ "memoryInfo.dpdkMemoryRegionCIOAddress"
+ "memoryInfo.dpdkMemoryRegionLength"
+ "memoryInfo.dpdkMemoryRegionUserspaceAddress"
+ "nhiDescriptorRings[%d]=%p\n"
+ "nhiRegisters"
+ "nhiRegisters[%d]=%p\n"
+ "number of packets sent to local interface (potentially invalid checksum)"
+ "number of packets sent to local interface (valid checksum)"
+ "offset + length < _memoryInfo.dpdkMemoryRegionLength"
+ "offsetPtr > 2"
+ "offsetPtr >= mbuf_offset"
+ "os_metrics: {\"timestamp\": %llu, \"group\": \"lattice\""
+ "os_metrics: {\"timestamp\": %llu, \"group\": \"lattice\", \"link\": %d"
+ "readRegister"
+ "rings"
+ "rte_pktmbuf_mtod(mbuf, uintptr_t) == offsetPtr"
+ "rx iface table packet"
+ "rx returned %d\n"
+ "start"
+ "translateFromCIODPDKAddress"
+ "translateToCIODPDKAddress"
+ "tx copy to direct"
+ "tx csum maybe invalid"
+ "tx csum valid"
+ "tx make direct failed"
+ "tx returned %d\n"
+ "writeRegister"
+ "}"
- "%s:%d Updated limiters in userspace egress=%llu ingress=%llu\n"
- "%s:%d Updated route table in userspace\n"
- "%s:%d rx limiter bytes per second=%llu\n"
- "%s:%d rx limiter disabled\n"
- "%s:%d tx bytes per second=%llu\n"
- "%s:%d tx limiter disabled\n"
- "(%s:%d)Error attempt to add an externaId that already exists\n"
- "(%s:%d)Invalid offset. offset=%lx mbuf_offset=%x\n\n"
- "/Library/Caches/com.apple.xbs/Sources/AppleLatticeNetwork/DPDKRing/ring_driver.cpp"
- "Cannot close connection %d\n"
- "Cannot get ringMode"
- "Cannot push mbuf"
- "Error attempt to add an externaId that already exists\n"
- "Failed to prepare driver"
- "Info configuring limiters: counter=%llu freq=%llu\n"
- "Invalid offset. offset=%lx mbuf_offset=%x\n\n"
- "Releasing connection\n"
- "Stopping bandwidth collector\n"
- "Unable to get limiter data ret=%d\n"
- "Unable to report usage conn=%x method=%d requestSize=%lu responseSize=%zu ret=%d\n"
- "Unknown ring driver mode %d%.0s"
- "Unknown ring node %d%.0s"
- "ingress data packet"
- "number of packets sent to local interface"
- "unique_lock::lock: already locked"
- "unique_lock::lock: references null mutex"
- "unique_lock::unlock: not locked"

```
