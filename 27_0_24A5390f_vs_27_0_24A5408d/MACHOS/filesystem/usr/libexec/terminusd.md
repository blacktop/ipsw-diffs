## terminusd

> `/usr/libexec/terminusd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-914.0.22.0.1
-  __TEXT.__text: 0x1fcc44
+914.0.34.0.4
+  __TEXT.__text: 0x200eb8
   __TEXT.__auth_stubs: 0x3ed0
-  __TEXT.__objc_stubs: 0x9400
-  __TEXT.__objc_methlist: 0x5be4
-  __TEXT.__const: 0x72c
+  __TEXT.__objc_stubs: 0x9020
+  __TEXT.__objc_methlist: 0x58c4
+  __TEXT.__const: 0x73c
   __TEXT.__swift5_typeref: 0x4ce
-  __TEXT.__cstring: 0x5185b
+  __TEXT.__cstring: 0x525cf
   __TEXT.__swift5_capture: 0x4a4
-  __TEXT.__objc_methtype: 0x4467
+  __TEXT.__objc_methtype: 0x4346
   __TEXT.__oslogstring: 0x2dee
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_reflstr: 0x8b
   __TEXT.__swift5_fieldmd: 0xf0
-  __TEXT.__objc_classname: 0x148e
-  __TEXT.__objc_methname: 0x138a5
+  __TEXT.__objc_classname: 0x14dc
+  __TEXT.__objc_methname: 0x13205
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x18

   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift_as_cont: 0xdc
-  __TEXT.__gcc_except_tab: 0x61f4
-  __TEXT.__unwind_info: 0x3170
+  __TEXT.__gcc_except_tab: 0x628c
+  __TEXT.__unwind_info: 0x3188
   __TEXT.__eh_frame: 0xe90
-  __DATA_CONST.__const: 0x4e20
-  __DATA_CONST.__cfstring: 0xdba0
-  __DATA_CONST.__objc_classlist: 0x5a0
+  __DATA_CONST.__const: 0x4eb0
+  __DATA_CONST.__cfstring: 0xdf80
+  __DATA_CONST.__objc_classlist: 0x5b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1a0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0x1f78
   __DATA_CONST.__got: 0xec0
   __DATA_CONST.__auth_ptr: 0x1d8
-  __DATA.__objc_const: 0x19c38
-  __DATA.__objc_selrefs: 0x2ee0
-  __DATA.__objc_ivar: 0x1fdc
-  __DATA.__objc_data: 0x3800
+  __DATA.__objc_const: 0x1a0e8
+  __DATA.__objc_selrefs: 0x2d00
+  __DATA.__objc_ivar: 0x2074
+  __DATA.__objc_data: 0x38f0
   __DATA.__data: 0x1938
-  __DATA.__bss: 0xcb8
+  __DATA.__bss: 0xcc8
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4016
+  Functions: 3973
   Symbols:   1536
-  CStrings:  11649
+  CStrings:  11674
 
Symbols:
+ _nrXPCKeyAllDevices
- _nrXPCKeyPersistentMesh
CStrings:
+ "%s%.30s:%-4d %@ Wi-Fi Aware reached %d consecutive failures; triggering ABC"
+ "%s%.30s:%-4d %@ requested distribution start, but the room distributor is unused"
+ "%s%.30s:%-4d %@: rejecting Wi-Fi Aware activate request since we are on %@ infrastructure Wi-Fi; distribution will flow over Wi-Fi"
+ "%s%.30s:%-4d %@: rejecting Wi-Fi Aware probe request, we are on %@ infrastructure Wi-Fi"
+ "%s%.30s:%-4d Begin elevated inbound traffic level"
+ "%s%.30s:%-4d Client %@ attempted to register mesh without identifier"
+ "%s%.30s:%-4d Client %@ attempted to unregister mesh without identifier"
+ "%s%.30s:%-4d Client %@ copying all devices"
+ "%s%.30s:%-4d Client %@ failed to register mesh '%@': %@"
+ "%s%.30s:%-4d Client %@ failed to unregister mesh '%@': %@"
+ "%s%.30s:%-4d Client %@ registering mesh with identifier '%@'"
+ "%s%.30s:%-4d Client %@ unregistering mesh with identifier '%@'"
+ "%s%.30s:%-4d End elevated inbound traffic level"
+ "%s%.30s:%-4d HomeKit data changed. Update distribution group."
+ "%s%.30s:%-4d Listen request %@ for asName %@ not allowed: missing entitlement"
+ "%s%.30s:%-4d Mesh '%@' is not registered; nothing to unregister"
+ "%s%.30s:%-4d No mesh convergence analytics available"
+ "%s%.30s:%-4d Not accepting Wi-Fi Aware connection to %@: device is on %@ infrastructure Wi-Fi"
+ "%s%.30s:%-4d Not accepting Wi-Fi Aware connection to %@: neighbour is on %@ infrastructure Wi-Fi"
+ "%s%.30s:%-4d Not marking %@ as my distributee: we are locally on %@ infrastructure Wi-Fi"
+ "%s%.30s:%-4d Not starting NAN: room distributor is unused (wired link or 2.4GHz/6GHz infrastructure Wi-Fi)"
+ "%s%.30s:%-4d Rx throughput for %@: %lf kbps"
+ "%s%.30s:%-4d Tearing down Wi-Fi Aware link with %@: device is on %@ infrastructure Wi-Fi"
+ "%s%.30s:%-4d detected mismatch in connect peripheral states for %@"
+ "%s%.30s:%-4d failed to create extended metadata for %@ (%lu bytes)"
+ "%s%.30s:%-4d ignoring start resolve request for %@ from unentitled client %@"
+ "%s%.30s:%-4d pid %d has entitlement, via agent check"
+ "%s%.30s:%-4d room distributor unused (wired link or 2.4GHz/6GHz infrastructure Wi-Fi), not establishing a distribution relationship towards the room distributor"
+ "%s%.30s:%-4d started connectPeripheral watchdog"
+ "%s%.30s:%-4d stopped connectPeripheral watchdog"
+ "-[NRBabelManager establishDistributionGroupWithChangeReason:]"
+ "-[NRBabelManager establishDistributionGroupWithChangeReason:]_block_invoke"
+ "-[NRBabelManager handleHighTrafficLevelBegin]"
+ "-[NRBabelManager handleHighTrafficLevelEnd:]"
+ "-[NRBabelManager homeKitManagerDidUpdateData:]_block_invoke"
+ "-[NRBabelManager recomputeCostsAndRoutesForNeighbour:changeReason:]"
+ "-[NRBabelManager runRouteSelectionWithChangeReason:]"
+ "-[NRBabelManager updateConvergenceTrackingWithDate:changeReason:]"
+ "-[NRBabelManager updateDistributees:withChangeReason:]"
+ "-[NRLinkDirector registerMeshWithIdentifier:operationalProperties:errorDescription:currentMeshIdentifier:]"
+ "-[NRLinkDirector unregisterMeshWithIdentifier:errorDescription:currentMeshIdentifier:]"
+ "-[NRLinkManagerBluetooth checkConnectingPeripheralsMismatch]_block_invoke_2"
+ "-[NRLinkManagerBluetooth startConnectPeripheralWatchdogIfNeeded]"
+ "-[NRLinkManagerBluetooth stopConnectPeripheralWatchdog]"
+ "-[NRVirtualMulticastManager registerPeerWithAddress:interfaceName:name:routeBitmap:linkType:completion:]_block_invoke"
+ "914.0.34.0.4"
+ "@\"NRAnalyticsMeshConvergence\""
+ "@\"NRAnalyticsMeshDataSession\""
+ "Failed to serialize all devices"
+ "Mesh already registered with a different identifier"
+ "Mesh registered with a different identifier"
+ "Missing mesh identifier"
+ "NRASMRequestIsAuthorizedForASName_block_invoke"
+ "NRAnalyticsMeshConvergence"
+ "NRAnalyticsMeshDataSession"
+ "NRBabelThroughputReport"
+ "NetworkRelay service connector entitled agent"
+ "SCEntitled"
+ "Wi-Fi Aware Suppressed"
+ "_averageKBitsPerSecond"
+ "_collectRxTputSamples"
+ "_connectPeripheralMismatchDetectedOnce"
+ "_connectPeripheralWatchdogTimer"
+ "_convergenceEventCount"
+ "_currentConvergenceAnalytics"
+ "_currentDataSessionAnalytics"
+ "_currentSampleStartDate"
+ "_didDQDueToChannelMismatch"
+ "_didDQDueToInsufficientNAN"
+ "_didDQDueToNANRSSI"
+ "_didDQDueToWired"
+ "_duration"
+ "_hasActiveTrafficAdvisory"
+ "_hasDistributees"
+ "_hasPrimaryAssist"
+ "_hasRoomDistributor"
+ "_helloReceived"
+ "_homeChanged"
+ "_isSender"
+ "_meshSize"
+ "_neighbourCapabilitiesChanged"
+ "_neighbourCostChanged"
+ "_neighbourRemoved"
+ "_primaryAssistIsRoomDistributor"
+ "_receivedRouteUpdate"
+ "_routeExpired"
+ "_rxPacketsThisInterval"
+ "_rxTputAverage"
+ "_rxTputEstimator"
+ "_rxTputStddev"
+ "_serviceConnectorEntitledAgent"
+ "_serviceConnectorEntitledAgentUUID"
+ "_standardDeviationKBitsPerSecond"
+ "_usedNAN"
+ "com.apple.networkrelay.analytics.meshConvergence"
+ "com.apple.networkrelay.analytics.meshDataSession"
+ "com.apple.private.network.restricted.port.ids_cloud_service_connector"
+ "consecutive failures reached threshold"
+ "convergenceEventCount"
+ "detected mismatch in connect peripheral states"
+ "didDQDueToChannelMismatch"
+ "didDQDueToInsufficientNAN"
+ "didDQDueToNANRSSI"
+ "didDQDueToWired"
+ "disableWiFiAwareOn2GHz"
+ "disableWiFiAwareOn6GHz"
+ "duration"
+ "extendedMetadata:"
+ "failed to create extended metadata for %@ (%lu bytes)"
+ "handleCopyAllDevices"
+ "handleRegisterMesh"
+ "handleUnregisterMesh"
+ "hasDistributees"
+ "hasPrimaryAssist"
+ "hasRoomDistributor"
+ "helloReceived"
+ "homeChanged"
+ "initWithDouble:"
+ "isSender"
+ "meshSize"
+ "neighbourCapabilitiesChanged"
+ "neighbourCostChanged"
+ "neighbourRemoved"
+ "primaryAssistIsRoomDistributor"
+ "receivedRouteUpdate"
+ "retrieveConnectingPeripherals"
+ "routeExpired"
+ "rxTputAvg"
+ "rxTputStdDev"
+ "service-connector.identityservicesd"
+ "setIsEnabled:"
+ "usedNAN"
+ "\xd1"
- "%s%.30s:%-4d Client %@ %sabling persistent mesh mode"
- "%s%.30s:%-4d Client %@ %sabling persistent mesh mode with identifier '%@'"
- "%s%.30s:%-4d Client %@ attempted to %sable persistent mesh mode without identifier"
- "%s%.30s:%-4d HomeKit configuration has changed. Update distribution group."
- "%s%.30s:%-4d local link type is wired, not establishing a distribution relationship towards the room distributor"
- "-[NRBabelManager establishDistributionGroup]"
- "-[NRBabelManager establishDistributionGroup]_block_invoke"
- "-[NRBabelManager homeKitManager:didUpdateMediaGroupPairings:]_block_invoke"
- "-[NRBabelManager recomputeCostsAndRoutesForNeighbour:]"
- "-[NRBabelManager runRouteSelection]"
- "-[NRBabelManager updateDistributees:]"
- "-[NRLinkDirector setPersistentMesh:meshIdentifier:operationalProperties:]"
- "-[NRVirtualMulticastManager registerPeerWithAddress:interfaceName:name:routeBitmap:completion:]_block_invoke"
- "914.0.22.0.1"
- "B24@0:8@?16"
- "B40@0:8r*16Q24^(sockaddr_in_4_6={sockaddr=CC[14c]}{__sockaddr_header=CC}{sockaddr_in=CCS{in_addr=I}[8c]}{sockaddr_in6=CCSI{in6_addr=(?=[16C][8S][4I])}I})32"
- "T@\"NSArray\",&,N,V_routeEntriesSnapshot"
- "T@\"NSMutableArray\",&,N,V_peers"
- "T@\"NSMutableArray\",&,N,V_receivedDatagrams"
- "T@\"NSMutableArray\",&,N,V_routeBitmapCache"
- "T@\"NSMutableDictionary\",&,N,V_peerConnectionDictionary"
- "T@\"NSNumber\",&,N,V_localBIERID"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_nexusGroup"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_createConnectionsTimer"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_dNexusReadSource"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_dNexusWriteSource"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_metricsTimer"
- "T@\"NSObject<OS_nw_agent>\",&,N,V_virtualMulticastAgent"
- "T@\"NSString\",&,N,V_interfaceName"
- "T@\"NSString\",&,N,V_name"
- "T@\"NWAddressEndpoint\",&,N,V_endpoint"
- "T@\"NWAddressEndpoint\",&,N,V_localIPv4Endpoint"
- "T@\"NWAddressEndpoint\",&,N,V_localIPv6Endpoint"
- "TB,N,V_dNexusReadSourceSuspended"
- "TB,N,V_dNexusWriteSourceSuspended"
- "TB,N,V_hasActiveMulticastSubscriptions"
- "TB,N,V_packetsWrittenSinceLastFlush"
- "TQ,N,V_routeBitmap"
- "TS,N,V_ipHeaderOffset"
- "T^{NEVirtualInterface_s=},N,V_virtualInterface"
- "T^{channel=},N,V_nexusChannel"
- "T^{channel_ring_desc=},N,V_nexusInputRing"
- "T^{channel_ring_desc=},N,V_nexusOutputRing"
- "^{channel=}16@0:8"
- "^{channel_ring_desc=}16@0:8"
- "armCreateConnectionsTimer"
- "createConnectionsTimer"
- "createPeerConnectionsIfNeeded"
- "handleSetPersistentMesh"
- "hasActiveMulticastSubscriptions"
- "homeKitManager:didUpdateMediaGroupPairings:"
- "ipHeaderOffset"
- "localBIERID"
- "localIPv4Endpoint"
- "localIPv6Endpoint"
- "logMetrics"
- "metricsTimer"
- "nexusGroup"
- "nexusOutputRing"
- "packetsWrittenSinceLastFlush"
- "parseIPAddressFromPacket:length:addressBuffer:"
- "peerConnectionDictionary"
- "performBlockSyncWithTimeout:"
- "readFromConnection:peer:"
- "receivedDatagrams"
- "recordForwardedMetricsForPacketOfSize:"
- "recordInjectedMetricsForPacketOfSize:"
- "recordMetrics:forPacketOfSize:"
- "recordReceivedMetricsForPacketOfSize:"
- "recordSentMetricsForPacketOfSize:"
- "routeBitmap"
- "routeBitmapCache"
- "routeEntriesSnapshot"
- "sendPacket:fromPeer:toPeersInBitmap:sendGroup:metricType:"
- "setCreateConnectionsTimer:"
- "setDNexusReadSource:"
- "setDNexusReadSourceSuspended:"
- "setDNexusWriteSource:"
- "setDNexusWriteSourceSuspended:"
- "setEndpoint:"
- "setHasActiveMulticastSubscriptions:"
- "setIpHeaderOffset:"
- "setLocalBIERID:"
- "setLocalIPv4Endpoint:"
- "setLocalIPv6Endpoint:"
- "setMetricsTimer:"
- "setName:"
- "setNexusChannel:"
- "setNexusGroup:"
- "setNexusInputRing:"
- "setNexusOutputRing:"
- "setPacketsWrittenSinceLastFlush:"
- "setPeerConnectionDictionary:"
- "setPeers:"
- "setReceivedDatagrams:"
- "setRouteBitmap:"
- "setRouteBitmapCache:"
- "setRouteEntriesSnapshot:"
- "setVirtualMulticastAgent:"
- "setupNexus"
- "setupVirtualInterfaceIfNeeded"
- "v24@0:8^{channel=}16"
- "v24@0:8^{channel_ring_desc=}16"
- "v32@0:8@\"NRHomeKitManager\"16@\"NSDictionary\"24"
- "v32@0:8Q16Q24"
- "v56@0:8@16@24Q32@40Q48"
- "virtualMulticastAgent"
- "\xb1"
```
