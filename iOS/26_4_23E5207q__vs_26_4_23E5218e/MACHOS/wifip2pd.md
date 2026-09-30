## wifip2pd

> `/usr/libexec/wifip2pd`

```diff

-855.25.0.0.0
-  __TEXT.__text: 0x4ca604
-  __TEXT.__auth_stubs: 0x48f0
-  __TEXT.__objc_stubs: 0x37e0
-  __TEXT.__objc_methlist: 0x16ec
-  __TEXT.__const: 0x38c60
-  __TEXT.__swift5_typeref: 0xb270
+855.30.4.1.0
+  __TEXT.__text: 0x4de3fc
+  __TEXT.__auth_stubs: 0x4950
+  __TEXT.__objc_stubs: 0x3b20
+  __TEXT.__objc_methlist: 0x177c
+  __TEXT.__const: 0x390f8
+  __TEXT.__swift5_typeref: 0xb43e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0xa56a
-  __TEXT.__oslogstring: 0x1766c
-  __TEXT.__constg_swiftt: 0xdea0
-  __TEXT.__swift5_fieldmd: 0x14444
-  __TEXT.__swift5_types: 0x1088
-  __TEXT.__swift5_reflstr: 0x12466
-  __TEXT.__swift5_builtin: 0x152c
+  __TEXT.__cstring: 0xa77e
+  __TEXT.__oslogstring: 0x16adc
+  __TEXT.__constg_swiftt: 0xe07c
+  __TEXT.__swift5_fieldmd: 0x1464c
+  __TEXT.__swift5_types: 0x10b0
+  __TEXT.__swift5_reflstr: 0x126d6
+  __TEXT.__swift5_builtin: 0x157c
   __TEXT.__swift5_assocty: 0x2958
-  __TEXT.__swift5_protos: 0xe4
-  __TEXT.__swift5_proto: 0x2b3c
+  __TEXT.__swift5_protos: 0xe8
+  __TEXT.__swift5_proto: 0x2b44
   __TEXT.__objc_classname: 0xd39
-  __TEXT.__objc_methtype: 0x1a17
-  __TEXT.__objc_methname: 0x8135
-  __TEXT.__swift5_capture: 0x4b2c
+  __TEXT.__objc_methtype: 0x1bc7
+  __TEXT.__objc_methname: 0x8775
+  __TEXT.__swift5_capture: 0x4c14
   __TEXT.__swift5_mpenum: 0x16c
   __TEXT.__swift_as_entry: 0x110
   __TEXT.__swift_as_ret: 0xb0
-  __TEXT.__unwind_info: 0xdb08
-  __TEXT.__eh_frame: 0x17b84
-  __DATA_CONST.__auth_got: 0x2480
-  __DATA_CONST.__got: 0xea8
-  __DATA_CONST.__auth_ptr: 0x1e20
-  __DATA_CONST.__const: 0x2e9e0
+  __TEXT.__unwind_info: 0xdc90
+  __TEXT.__eh_frame: 0x18130
+  __DATA_CONST.__auth_got: 0x24b0
+  __DATA_CONST.__got: 0xed8
+  __DATA_CONST.__auth_ptr: 0x1e30
+  __DATA_CONST.__const: 0x2ef30
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x138
-  __DATA.__objc_const: 0x89d8
-  __DATA.__objc_selrefs: 0x11e0
-  __DATA.__objc_data: 0x1370
-  __DATA.__data: 0x11178
+  __DATA.__objc_const: 0x8b48
+  __DATA.__objc_selrefs: 0x12f0
+  __DATA.__objc_data: 0x1390
+  __DATA.__data: 0x11370
   __DATA.__common: 0x8e8
-  __DATA.__bss: 0x54340
+  __DATA.__bss: 0x543c0
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CB0EF4FA-2F74-3C34-965F-D518B2A3B66F
-  Functions: 21010
-  Symbols:   2117
-  CStrings:  4205
+  UUID: 356DCCA6-C483-39A8-966F-AF5367F7FE24
+  Functions: 21152
+  Symbols:   2129
+  CStrings:  4247
 
Symbols:
+ _$sSo8NSObjectCSQ10ObjectiveCMc
+ _$ss12_ArrayBufferV18_typeCheckSlowPathyySiF
+ _$ss15_AnySequenceBoxC13_makeIterators0aE0VyxGyFTj
+ _$ss18_CocoaArrayWrapperVys12_SliceBufferVyyXlGSnySiGcig
+ _$ss19_AnyIteratorBoxBaseC4nextxSgyFTj
+ _$ss28__ContiguousArrayStorageBaseCMa
+ _$ss6MirrorV8childrens13AnyCollectionVySSSg5label_yp5valuetGvg
+ _OBJC_CLASS_$_WiFiAwareBandSchedule
+ _OBJC_CLASS_$_WiFiAwareChannelSchedule
+ _OBJC_CLASS_$_WiFiAwareNDIInfo
+ _OBJC_CLASS_$_WiFiAwareRadioSchedule
+ _OBJC_CLASS_$_WiFiAwareSrvInfo
+ _OBJC_CLASS_$_WiFiAwareSrvSessionInfo
- _OBJC_CLASS_$_WiFiAwareDataPathInfoPerDataAddress
CStrings:
+ "    Channel %u opClass=%hhu committedAvailability=%{bool}d"
+ "    Reserved slot opClass=%hhu committedAvailability=%{bool}d"
+ "  Map[%ld] mapID=%s entries=%ld"
+ "#### Data Confirmed With Peer: %@[deviceID %llu] ipv6:%s port: %hu, serviceSpecificInfo: %s, agent UUID: %s)"
+ "%@ pairing timeout: %ld seconds"
+ "%s: Authentication request transmission failed. Aborting"
+ "%s: Authentication request transmission succeeded"
+ "Attempting to send unicast schedule update to initiator %s for responder datapath %hhu"
+ "Attempting to send unicast schedule update to responder %s for initiator datapath %hhu"
+ "Attempting to transmit OOB AF [mapId=%s] to peer: %s (5G=%{bool}d, 2G=%{bool}d), supportsSimultaneousDualBand=%{bool}d dynamicSDB=%{bool}don clusterID: %s"
+ "Current NANDatapathState: %s totalSessions=%u, established=%u, ndiCount=%ld %s"
+ "Current NANRadioSchedule: %s DB=%{bool}d, SDB=%{bool}d, PrefChCount=%u"
+ "Dynamic SDB Supported"
+ "Failed to send unicast schedule update to initiator %s: %@"
+ "Failed to send unicast schedule update to responder %s: %@"
+ "Failed to update HE capabilities: %@"
+ "Failed to update HT capabilities: %@"
+ "Failed to update VHT capabilities: %@"
+ "Initiator datapath %s has no responderDataAddress"
+ "NAN enabled with initial committedAvailability: %ld map entries"
+ "NANSrv Current NANSrvInfo: %s pub=%u, sub=%u"
+ "NANSrv Previous NANSrvInfo: %s pub=%u, sub=%u"
+ "NANSrv Previous NANSrvInfo: nil (first time)"
+ "No pairing session to remove"
+ "P2P Controller.queryNANAvail for XPC Session: %@"
+ "P2P Controller.queryNANSrv for XPC Session: %@"
+ "PCL Peer %s potential channels: %s, usagePreference: %s, requiresExtraBW: %{bool}d"
+ "Peer %s supportsDynamicSDB: %{bool}d"
+ "Peer not discovered yet for %s, queueing resolve request"
+ "Previous NANDatapathState: %s totalSessions=%u, established=%u, ndiCount=%ld %s"
+ "Previous NANDatapathState: nil (first time)"
+ "Previous NANRadioSchedule: %s DB=%{bool}d, SDB=%{bool}d, PrefChCount=%u"
+ "Previous NANRadioSchedule: nil (first time)"
+ "RadioScheduleChanged"
+ "Removing pairing session to: %s"
+ "Removing pairing sessions"
+ "Retrying pending resolve for %s"
+ "SDB mode changed to %{bool}d, sending unicast schedule updates to all low latency datapaths"
+ "Supported channels: %s"
+ "Trying to remove pairing sessions"
+ "Unknown datapath instance type, returning default zeroed NdInfo"
+ "Unknown datapathState instance type"
+ "WiFiAwareStateHandler handling MAC address change to %s for interface %s"
+ "WiFiAwareStateHandler link state change to %s for interface %s with MAC %s"
+ "WiFiP2P-855.30.4.1 Feb 17 2026 21:02:39"
+ "_currentSchedule"
+ "band24GHz"
+ "band5GHz"
+ "channel"
+ "channels"
+ "convertToWiFiAwareRadioSchedule: Added 2.4GHz channel %u (opClass=%hhu, bw=%hhu, period=%hhu) from map %s"
+ "convertToWiFiAwareRadioSchedule: Added 5GHz channel %u (opClass=%hhu, bw=%hhu, period=%hhu) from map %s"
+ "convertToWiFiAwareRadioSchedule: Created band24GHz with %ld channels, band5GHz with %ld channels"
+ "convertToWiFiAwareRadioSchedule: Final values - primaryChannel=%@, secondaryChannel=%s, infraChannel=%s, preferredChannelsCount=%u, preferredChannels=%s"
+ "convertToWiFiAwareRadioSchedule: Processing map %s with %ld entries"
+ "convertToWiFiAwareRadioSchedule: Using NANInterface preferredChannels: %s"
+ "convertToWiFiAwareRadioSchedule: Using channelResolver preferredChannels: %s"
+ "convertToWiFiAwareRadioSchedule: Using first 5GHz channel %u as secondaryChannel"
+ "convertToWiFiAwareRadioSchedule: availability has %ld map entries"
+ "driverRadioSchedule"
+ "infraChannel"
+ "initWithChannel:bandwidth:band:period:timeBitmap:"
+ "initWithChannels:"
+ "initWithDpId:dpRole:serviceId:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:sessionState:"
+ "initWithInterfaceName:interfaceAddr:isEnabled:band24GHz:band5GHz:supportsDualBand:supportsSimultaneousDualBand:primaryChannel:secondaryChannel:infraChannel:preferredChannelsCount:preferredChannelNumbers:"
+ "initWithInterfaceName:interfaceAddr:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:"
+ "initWithInterfaceName:interfaceAddr:isEnabled:publishServiceCount:subscribeServiceCount:srvSessionCount:srvSessionInfos:"
+ "initWithInterfaceName:interfaceAddr:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiInfos:preferredChannelNumbers:preferredChannelClasses:ndiSessionInfos:"
+ "initWithNdiName:ndiAddr:sessionCount:security:qosType:"
+ "initWithSrvId:srvType:srvName:srvHash:ndiInfos:numofPeers:"
+ "interfaceAddr"
+ "lastNotifiedRadioSchedule"
+ "lastNotifiedSrvInfo"
+ "lastRadioScheduleChangedOptions"
+ "lastSrvInfoChangedOptions"
+ "nan_event: %s APPLE80211_M_NAN_MASTER_CHANGED immediateMaster=%@ rank=%hhu:%hhu anchorMaster=%@ rank=%hhu:%hhu flags=%u"
+ "nan_event: %s APPLE80211_M_NAN_PREFERRED_CHANNELS_CHANGED count=%ld channels=%s"
+ "nan_event: %s APPLE80211_M_NAN_RADIO_SCHED_CHANGED band24G=%s band5G=%s"
+ "nan_send: %s __LINE__ APPLE80211_IOC_NAN_SCHEDULE_UPDATE"
+ "ndiAddr"
+ "ndiInfos"
+ "ndiName"
+ "ndiSessionInfos"
+ "ndiSessionInfos["
+ "numofPeers"
+ "preferredChannelClasses"
+ "preferredChannelNumbers"
+ "preferredChannelsCount"
+ "preferredChannelsMonitoringToken"
+ "primaryChannel"
+ "publishServiceCount"
+ "queryNANAvailWithCompletionHandler:"
+ "queryNANSrvWithCompletionHandler:"
+ "retryHandler"
+ "sdbModeMonitoringToken"
+ "secondaryChannel"
+ "sendUnicastScheduleUpdate(targetPeerAddress:)"
+ "srvHash"
+ "srvId"
+ "srvName"
+ "srvSessionCount"
+ "srvSessionInfos"
+ "srvSessionInfos.ndiInfos"
+ "srvSessionInfos.numofPeers"
+ "srvSessionInfos.srvHash"
+ "srvSessionInfos.srvId"
+ "srvSessionInfos.srvName"
+ "srvSessionInfos.srvType"
+ "srvType"
+ "subscribeServiceCount"
+ "timeBitmap"
+ "updatedNANAvailability:"
+ "updatedNANAvailabilityWithChangedOptions:changedOptions:"
+ "updatedNANAvailabilityWithChangedOptions:changedOptions:forceAllChangedOptions:"
+ "updatedNANDpStateWithChangedOptions:changedOptions:forceAllChangedOptions:"
+ "updatedNANSrvInfo:"
+ "updatedNANSrvInfoWithChangedOptions:changedOptions:"
+ "updatedNANSrvInfoWithChangedOptions:changedOptions:forceAllChangedOptions:"
+ "updatedNANStateWithChangedOptions:changedOptions:forceAllChangedOptions:"
+ "v24@0:8@\"WiFiAwareRadioSchedule\"16"
+ "v24@0:8@\"WiFiAwareSrvInfo\"16"
+ "v24@0:8@?<v@?@\"WiFiAwareRadioSchedule\">16"
+ "v24@0:8@?<v@?@\"WiFiAwareSrvInfo\">16"
+ "v32@0:8@\"WiFiAwareRadioSchedule\"16@\"NSArray\"24"
+ "v32@0:8@\"WiFiAwareSrvInfo\"16@\"NSArray\"24"
+ "v36@0:8@\"WiFiAwareDataPathState\"16@\"NSArray\"24B32"
+ "v36@0:8@\"WiFiAwareRadioSchedule\"16@\"NSArray\"24B32"
+ "v36@0:8@\"WiFiAwareSrvInfo\"16@\"NSArray\"24B32"
+ "v36@0:8@\"WiFiAwareState\"16@\"NSArray\"24B32"
+ "v36@0:8@16@24B32"
- "#### Data Confirmed With Peer: %@[deviceID %llu] ipv6:%s port: %hu, serviceSpecificInfo: %s"
- "%@ is monitoringNAN state information with options: %lu"
- "%@ was invalidated for NAN stateMonitoring"
- "Attempting to transmit OOB AF [mapId=%s] to peer: %s (5G=%{bool}d, 2G=%{bool}d) on clusterID: %s"
- "Checking changedOptions comparing nil datapath states: state1=%s, state2=%s, result=%{bool}d"
- "Checking changedOptions comparing nil states: state1=%s, state2=%s, result=%{bool}d"
- "Checking changedOptions comparison result: %{bool}d"
- "Checking changedOptions overall datapath comparison result: %{bool}d"
- "Current datapathState: totalSessions=%u, established=%u, ndiCount=%u"
- "DEBUG: Creating session info for initiator dpId=%hhu, security=%hhu, cipherSuite=%s"
- "DEBUG: Creating session info for responder dpId=%hhu, security=%hhu, cipherSuite=%s"
- "Master changed event indicates enabled state should be %{bool}d"
- "Master changed event indicates fw_election should be %{bool}d"
- "Master changed event updating anchor master: addr=%s, metric=masterPref:%hhu randomFactor:%hhu"
- "Master changed event updating cluster ID from %s to %s"
- "Master changed event updating election metric from masterPref:%hhu randomFactor:%hhu to masterPref:%hhu randomFactor:%hhu"
- "Master changed event updating hop count from %ld to %ld"
- "Master changed event updating immediate master: addr=%s, metric=masterPref:%hhu randomFactor:%hhu"
- "NAN datapathState changed, notifying monitoring sessions"
- "NAN datapathState unchanged, skipping notification"
- "NANInterface::startMonitoringNANState() for XPC Session: %@ with configuration: %@"
- "NANState changed, notifying monitoringNAN sessions"
- "NANState unchanged (excluding timestamps), skipping notification"
- "NDI address %s for interface %s already exists in tracking ndiSessions, interfaceNames: [%s] calling handleNANDataPathStateChange"
- "No active monitoringNAN sessions for datapath state updates, skipping"
- "No active monitoringNAN sessions for state updates, skipping"
- "Not found NDI address %s for interface %s in tracking ndiSessions, still calling handleNANDataPathStateChange"
- "Previous datapathState: nil (first time)"
- "Previous datapathState: totalSessions=%u, established=%u, ndiCount=%u"
- "Received preferred channels: %s"
- "Sending datapath state update with %ld changedOptions: %s"
- "Sending state update with %ld changedOptions: %s"
- "Skipping analytics collection for .released subReason"
- "State comparison result: hasChanged=%{bool}d"
- "Supported channels information: %s"
- "Unknown datapath instance type"
- "WARNING: Calling empty updateSocialChannels()"
- "WiFiAwareSateHandler handling MAC address change to %s for interface %s"
- "WiFiAwareSateHandler interface %s link down, but keeping NDI address since interface still exists"
- "WiFiAwareSateHandler link state change to %s for interface %s with MAC %s"
- "WiFiP2P-855.25 Feb 09 2026 22:02:32"
- "added NDI session for address %s in ndiSessions interfaceName %s with 0 sessions with isEnabled=%{bool}d"
- "added initiator session info for peer %s, establishedDataInitiator: %{bool}d"
- "added initiator session info, establishedDataInitiator: %{bool}d"
- "added interface %s to existing NDI address %s in ndiSessions, interfaceNames: [%s], total unique NDI addresses: %ld calling handleNANDataPathStateChange"
- "added interface %s to existing ndiSessions address %s, interfaceNames: [%s], total unique NDI addresses: %ld calling handleNANDataPathStateChange"
- "added new NDI address %s in ndiSessions for interface %s, interfaceNames: [%s], total unique NDI addresses: %ld calling handleNANDataPathStateChange"
- "added new NDI address %s to ndiSessions for interface %s, interfaceNames: [%s], total unique NDI addresses: %ld calling handleNANDataPathStateChange"
- "added responder session info for peer %s, establishedDataResponder: %{bool}d"
- "added responder session info, establishedDataResponder: %{bool}d"
- "changedOptions: %s: %s -> %s"
- "converting %ld deviceLinks (including transitional states) to WiFiAwareDataPathState"
- "converting to DatapathState directly from establishedData discovery engine"
- "created empty datapathState with %ld NDI addresses with isEnabled=%{bool}d"
- "customPreferredChannelClass"
- "customPreferredChannelNumber"
- "dataAddress"
- "datapathState comparison result: hasChanged=%{bool}d"
- "discoveryEngine has %ld total deviceLinks and %ld peers with establishedDatapath"
- "discoveryEngine.ndiSessions.count = %ld"
- "establishedDatapath discoveryEngine.datapathInitiators.count = %ld discoveryEngine.datapathResponders.count = %ld"
- "found establishedDatapath sessions without deviceLinks, creating state from initiators/responders"
- "found initiator in deviceLinks for peer %s, state: %s"
- "found responder in establshedDataResponders for peer %s, state: %s"
- "generated dpState, Sending initial dpState to new monitoringNANDp session: %s"
- "handling NAN datapathState change"
- "initWithDpId:dpRole:serviceId:security:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:qosType:sessionState:"
- "initWithInterfaceName:dataAddress:sessionCount:"
- "initWithInterfaceName:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfAddress:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:"
- "initWithInterfaceName:macAddress:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiDataAddressCount:ndiSessions:customPreferredChannelNumber:customPreferredChannelClass:sessionInfos:"
- "mark all fiedls in changedOptions for first-time call"
- "matched dpId %hhu in tracking ndiSessions with address %@, new count: %u"
- "matched session %hhu to tracked ndiSessions %@, new count: %u"
- "nan_event: %s APPLE80211_M_NAN_MASTER_CHANGED"
- "nan_event: %s APPLE80211_M_NAN_PREFERRED_CHANNELS_CHANGED"
- "ndiDataAddressCount"
- "no establishedDatapath connections found, returning empty datapath state with isEnabled = %{bool}d"
- "peer %s has %ld channels, all 2.4GHz: %{bool}d"
- "pre-populated NDI session for tracking ndiSessions address %s"
- "pre-populated NDI session in tracking ndiSessions for address %s"
- "processing datapathState initiator %hhu, state: %s"
- "processing datapathState responder %hhu, state: %s"
- "processing deviceLinks for peer %s"
- "removed NDI address %s from ndiSessions for interface %s, no more interfaces using this address, interfaceNames: [], total unique NDI addresses: %ld calling handleNANDataPathStateChange"
- "removed interface %s from ndiSessions address %s, interfaceNames: [%s], total unique NDI addresses: %ld calling handleNANDataPathStateChange"
- "removed old NDI address %s from ndiSessions as no interfaces use it anymore, interfaceNames: []"
- "replaced old NDI address %s with existing NDI address %s in ndiSessions for interface %s, interfaceNames: [%s], total unique NDI addresses: %ld"
- "replaced old NDI address %s with new NDI address %sin ndiSessions for interface %s, interfaceNames: [%s], total unique NDI addresses: %ld"
- "selfAddress"
- "sessionInfos"
- "spatialStreaming uses Sidecar: %{bool}d"
- "supportedChannelsInformation"
- "using discoveryEngine all deviceLinks including transitional states"
- "using preferred channel %u class %hhu"

```
