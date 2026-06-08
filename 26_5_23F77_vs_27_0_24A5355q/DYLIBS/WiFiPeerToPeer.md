## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-860.7.0.0.0
-  __TEXT.__text: 0x2ef08
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x4164
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x6b34
-  __TEXT.__gcc_except_tab: 0x380
-  __TEXT.__oslogstring: 0xb97
-  __TEXT.__unwind_info: 0xbc8
-  __TEXT.__objc_classname: 0x8fa
-  __TEXT.__objc_methname: 0xa2c3
-  __TEXT.__objc_methtype: 0x20bc
-  __TEXT.__objc_stubs: 0x50a0
-  __DATA_CONST.__got: 0x238
-  __DATA_CONST.__const: 0x1080
-  __DATA_CONST.__objc_classlist: 0x1a0
-  __DATA_CONST.__objc_protolist: 0xd0
+885.62.0.0.0
+  __TEXT.__text: 0x3d458
+  __TEXT.__objc_methlist: 0x5494
+  __TEXT.__const: 0x250
+  __TEXT.__oslogstring: 0x1332
+  __TEXT.__swift5_typeref: 0x8c
+  __TEXT.__cstring: 0x8661
+  __TEXT.__constg_swiftt: 0x70
+  __TEXT.__swift5_reflstr: 0x7
+  __TEXT.__swift5_fieldmd: 0x2c
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__gcc_except_tab: 0x2f0
+  __TEXT.__unwind_info: 0xf38
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x13e8
+  __DATA_CONST.__objc_classlist: 0x260
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c80
-  __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x190
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x5540
-  __AUTH_CONST.__objc_const: 0x76c8
+  __DATA_CONST.__objc_selrefs: 0x2228
+  __DATA_CONST.__objc_protorefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0x240
+  __DATA_CONST.__got: 0x320
+  __AUTH_CONST.__const: 0x4a8
+  __AUTH_CONST.__cfstring: 0x6a60
+  __AUTH_CONST.__objc_const: 0x9b20
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x5bc
-  __DATA.__data: 0x9c0
-  __DATA_DIRTY.__objc_data: 0xcd0
+  __AUTH_CONST.__auth_got: 0x560
+  __AUTH.__objc_data: 0x98
+  __DATA.__objc_ivar: 0x718
+  __DATA.__data: 0xc80
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x17f8
+  __DATA_DIRTY.__data: 0x60
+  __DATA_DIRTY.__common: 0x8
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ABD1158E-2FAC-3085-B6BE-05A2CE05BAF7
-  Functions: 1311
-  Symbols:   4618
-  CStrings:  3345
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: A566D5C1-5657-3DDA-BF67-4327BFEBC937
+  Functions: 1722
+  Symbols:   5902
+  CStrings:  1920
 
Symbols:
+ +[WiFiAwareDataSessionConfig supportsSecureCoding]
+ +[WiFiAwareInterfaceInfo supportsSecureCoding]
+ +[WiFiAwarePKBootstrappingRecordIngestionResult stringForRejectionReason:]
+ +[WiFiAwarePKBootstrappingRecordIngestionResult supportsSecureCoding]
+ +[WiFiAwarePKBootstrappingRecords supportsSecureCoding]
+ +[WiFiAwarePKBootstrappingRecordsIngestionReport supportsSecureCoding]
+ +[WiFiAwarePairingConfig stringForPairSetupMode:]
+ +[WiFiAwarePairingConfig stringForPairingMode:]
+ +[WiFiAwarePairingConfig supportsSecureCoding]
+ +[WiFiAwarePairingSession WiFiAwarePairingRoleToString:]
+ +[WiFiAwarePeerAvailBandEntry supportsSecureCoding]
+ +[WiFiAwarePeerAvailChannelEntry supportsSecureCoding]
+ +[WiFiAwarePeerAvailInfo supportsSecureCoding]
+ +[WiFiAwarePeerDevice supportsSecureCoding]
+ +[WiFiAwarePeerInfo supportsSecureCoding]
+ +[WiFiAwarePerformanceForecast supportsSecureCoding]
+ +[WiFiAwareTDSConfig stringForDeviceFilter:]
+ +[WiFiAwareTDSConfig stringForOperation:]
+ +[WiFiAwareTDSConfig supportsSecureCoding]
+ +[WiFiAwareTDSDevice supportsSecureCoding]
+ +[WiFiP2PNANStateMonitorConfiguration supportsSecureCoding]
+ -[AWDLServiceDiscoveryManager addAWDLDiscoveryClient:forService:error:]
+ -[AWDLServiceDiscoveryManager refreshAWDLDiscoveryActivityForService:error:]
+ -[AWDLServiceDiscoveryManager removeAWDLDiscoveryClient:forService:error:]
+ -[WiFiAwareChannelConfiguration .cxx_destruct]
+ -[WiFiAwareChannelConfiguration description]
+ -[WiFiAwareChannelConfiguration initWithPreferredChannelNumbers:preferredChannelClasses:]
+ -[WiFiAwareChannelConfiguration preferredChannelClasses]
+ -[WiFiAwareChannelConfiguration preferredChannelNumbers]
+ -[WiFiAwareDataPathState initWithInterfaceInfo:sessionCounters:channelConfig:ndiInfos:ndiSessionInfos:]
+ -[WiFiAwareDataPathState interfaceInfo]
+ -[WiFiAwareDataSession initSecureConnectionWithPairedDevice:configuration:]
+ -[WiFiAwareDataSession setSkipInfrastructureRelayCheck:]
+ -[WiFiAwareDataSession skipInfrastructureRelayCheck]
+ -[WiFiAwareDataSessionConfig .cxx_destruct]
+ -[WiFiAwareDataSessionConfig copyWithZone:]
+ -[WiFiAwareDataSessionConfig description]
+ -[WiFiAwareDataSessionConfig encodeWithCoder:]
+ -[WiFiAwareDataSessionConfig hash]
+ -[WiFiAwareDataSessionConfig initWithCoder:]
+ -[WiFiAwareDataSessionConfig initWithServiceType:]
+ -[WiFiAwareDataSessionConfig initWithServiceType:internetSharingConfiguration:]
+ -[WiFiAwareDataSessionConfig internetSharingConfiguration]
+ -[WiFiAwareDataSessionConfig isEqual:]
+ -[WiFiAwareDataSessionConfig serviceType]
+ -[WiFiAwareDataSessionConfig setInternetSharingConfiguration:]
+ -[WiFiAwareDataSessionConfig setServiceType:]
+ -[WiFiAwareDataSessionConfig setUserID:]
+ -[WiFiAwareDataSessionConfig userID]
+ -[WiFiAwareDatapathConfiguration setSkipInfrastructureRelayCheck:]
+ -[WiFiAwareDatapathConfiguration setUserID:]
+ -[WiFiAwareDatapathConfiguration skipInfrastructureRelayCheck]
+ -[WiFiAwareDatapathConfiguration userID]
+ -[WiFiAwareDiscoveryResult autoPairable]
+ -[WiFiAwareDiscoveryResult initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:pairedUUID:pairedDeviceName:signature:autoPairable:performanceForecast:]
+ -[WiFiAwareDiscoveryResult performanceForecast]
+ -[WiFiAwareInterfaceInfo .cxx_destruct]
+ -[WiFiAwareInterfaceInfo copyWithZone:]
+ -[WiFiAwareInterfaceInfo description]
+ -[WiFiAwareInterfaceInfo encodeWithCoder:]
+ -[WiFiAwareInterfaceInfo hash]
+ -[WiFiAwareInterfaceInfo initWithCoder:]
+ -[WiFiAwareInterfaceInfo initWithInterfaceName:interfaceAddr:isEnabled:]
+ -[WiFiAwareInterfaceInfo interfaceAddr]
+ -[WiFiAwareInterfaceInfo interfaceName]
+ -[WiFiAwareInterfaceInfo isEnabled]
+ -[WiFiAwareInterfaceInfo isEqual:]
+ -[WiFiAwareNDIInfo initWithNdiName:ndiAddr:sessionCount:qosType:security:]
+ -[WiFiAwareNDISessionCounters description]
+ -[WiFiAwareNDISessionCounters established]
+ -[WiFiAwareNDISessionCounters initWithTotal:established:with24GOnlyPeer:rtm:rtmWith24GOnly:rtmLowLatency:]
+ -[WiFiAwareNDISessionCounters rtmLowLatency]
+ -[WiFiAwareNDISessionCounters rtmWith24GOnly]
+ -[WiFiAwareNDISessionCounters rtm]
+ -[WiFiAwareNDISessionCounters total]
+ -[WiFiAwareNDISessionCounters with24GOnlyPeer]
+ -[WiFiAwarePKBootstrappingRecordIngestionResult description]
+ -[WiFiAwarePKBootstrappingRecordIngestionResult encodeWithCoder:]
+ -[WiFiAwarePKBootstrappingRecordIngestionResult ingested]
+ -[WiFiAwarePKBootstrappingRecordIngestionResult initWithCoder:]
+ -[WiFiAwarePKBootstrappingRecordIngestionResult initWithIngested:rejectionReason:]
+ -[WiFiAwarePKBootstrappingRecordIngestionResult rejectionReason]
+ -[WiFiAwarePKBootstrappingRecordIngestionResult setIngested:]
+ -[WiFiAwarePKBootstrappingRecordIngestionResult setRejectionReason:]
+ -[WiFiAwarePKBootstrappingRecords .cxx_destruct]
+ -[WiFiAwarePKBootstrappingRecords bootstrappingRecords]
+ -[WiFiAwarePKBootstrappingRecords description]
+ -[WiFiAwarePKBootstrappingRecords encodeWithCoder:]
+ -[WiFiAwarePKBootstrappingRecords expiration]
+ -[WiFiAwarePKBootstrappingRecords initWithCoder:]
+ -[WiFiAwarePKBootstrappingRecords initWithexpiration:bootstrappingRecords:]
+ -[WiFiAwarePKBootstrappingRecordsIngestionReport .cxx_destruct]
+ -[WiFiAwarePKBootstrappingRecordsIngestionReport description]
+ -[WiFiAwarePKBootstrappingRecordsIngestionReport encodeWithCoder:]
+ -[WiFiAwarePKBootstrappingRecordsIngestionReport initWithCoder:]
+ -[WiFiAwarePKBootstrappingRecordsIngestionReport initWithRecordsProcessed:ingestionResults:]
+ -[WiFiAwarePKBootstrappingRecordsIngestionReport recordsProcessed]
+ -[WiFiAwarePKBootstrappingRecordsIngestionReport results]
+ -[WiFiAwarePKBootstrappingRecordsIngestionReport setRecordsProcessed:]
+ -[WiFiAwarePKBootstrappingRecordsStore .cxx_destruct]
+ -[WiFiAwarePKBootstrappingRecordsStore activate]
+ -[WiFiAwarePKBootstrappingRecordsStore addRemotePKBootstrappingRecords:completion:]
+ -[WiFiAwarePKBootstrappingRecordsStore deactivate]
+ -[WiFiAwarePKBootstrappingRecordsStore init]
+ -[WiFiAwarePKBootstrappingRecordsStore queryEphemeralLocalPKBootstrappingRecords:]
+ -[WiFiAwarePKBootstrappingRecordsStore queryLocalPKBootstrappingRecords:]
+ -[WiFiAwarePKBootstrappingRecordsStore remoteObjectInterface]
+ -[WiFiAwarePKBootstrappingRecordsStore startConnectionUsingProxy:completionHandler:]
+ -[WiFiAwarePairingConfig .cxx_destruct]
+ -[WiFiAwarePairingConfig copyWithZone:]
+ -[WiFiAwarePairingConfig description]
+ -[WiFiAwarePairingConfig encodeWithCoder:]
+ -[WiFiAwarePairingConfig initWithCoder:]
+ -[WiFiAwarePairingConfig initWithPairingMode:pairingMetadata:]
+ -[WiFiAwarePairingConfig pairingMetadata]
+ -[WiFiAwarePairingConfig pairingMode]
+ -[WiFiAwarePairingConfig pairingSetupMode]
+ -[WiFiAwarePairingConfig setPairingMetadata:]
+ -[WiFiAwarePairingConfig setPairingMode:]
+ -[WiFiAwarePairingConfig setPairingSetupMode:]
+ -[WiFiAwarePairingConfig setUserID:]
+ -[WiFiAwarePairingConfig userID]
+ -[WiFiAwarePairingSession .cxx_destruct]
+ -[WiFiAwarePairingSession activateForPublishID:initiatorAddress:]
+ -[WiFiAwarePairingSession deactivate]
+ -[WiFiAwarePairingSession delegate]
+ -[WiFiAwarePairingSession description]
+ -[WiFiAwarePairingSession discoveryResult]
+ -[WiFiAwarePairingSession exportedInterface]
+ -[WiFiAwarePairingSession exportedObject]
+ -[WiFiAwarePairingSession handleError:]
+ -[WiFiAwarePairingSession initWithPairingConfig:delegate:]
+ -[WiFiAwarePairingSession initiatorAddress]
+ -[WiFiAwarePairingSession pairWithDiscoveryResult:]
+ -[WiFiAwarePairingSession pairingConfig]
+ -[WiFiAwarePairingSession pairingDidFailTo:error:]
+ -[WiFiAwarePairingSession pairingDidSucceedWithDeviceInfo:pairingStoreID:]
+ -[WiFiAwarePairingSession publishID]
+ -[WiFiAwarePairingSession remoteObjectInterface]
+ -[WiFiAwarePairingSession requiresPINDisplay:]
+ -[WiFiAwarePairingSession requiresPINInputWithCompletionHandler:]
+ -[WiFiAwarePairingSession requiresPassphraseDisplay:]
+ -[WiFiAwarePairingSession requiresPassphraseInputWithCompletionHandler:]
+ -[WiFiAwarePairingSession role]
+ -[WiFiAwarePairingSession setDelegate:]
+ -[WiFiAwarePairingSession setDiscoveryResult:]
+ -[WiFiAwarePairingSession setInitiatorAddress:]
+ -[WiFiAwarePairingSession setPublishID:]
+ -[WiFiAwarePairingSession setRole:]
+ -[WiFiAwarePairingSession startConnectionUsingProxy:completionHandler:]
+ -[WiFiAwarePeerAvailBandEntry .cxx_destruct]
+ -[WiFiAwarePeerAvailBandEntry bands]
+ -[WiFiAwarePeerAvailBandEntry copyWithZone:]
+ -[WiFiAwarePeerAvailBandEntry description]
+ -[WiFiAwarePeerAvailBandEntry encodeWithCoder:]
+ -[WiFiAwarePeerAvailBandEntry initWithCoder:]
+ -[WiFiAwarePeerAvailBandEntry initWithMapId:bands:usagePreference:rxNSS:utilization:]
+ -[WiFiAwarePeerAvailBandEntry mapId]
+ -[WiFiAwarePeerAvailBandEntry rxNSS]
+ -[WiFiAwarePeerAvailBandEntry usagePreference]
+ -[WiFiAwarePeerAvailBandEntry utilization]
+ -[WiFiAwarePeerAvailChannelEntry .cxx_destruct]
+ -[WiFiAwarePeerAvailChannelEntry band]
+ -[WiFiAwarePeerAvailChannelEntry bandwidth]
+ -[WiFiAwarePeerAvailChannelEntry channel]
+ -[WiFiAwarePeerAvailChannelEntry copyWithZone:]
+ -[WiFiAwarePeerAvailChannelEntry description]
+ -[WiFiAwarePeerAvailChannelEntry encodeWithCoder:]
+ -[WiFiAwarePeerAvailChannelEntry initWithCoder:]
+ -[WiFiAwarePeerAvailChannelEntry initWithMapId:channel:bandwidth:band:period:offset:timeBitmap:usagePreference:rxNSS:utilization:]
+ -[WiFiAwarePeerAvailChannelEntry mapId]
+ -[WiFiAwarePeerAvailChannelEntry offset]
+ -[WiFiAwarePeerAvailChannelEntry period]
+ -[WiFiAwarePeerAvailChannelEntry rxNSS]
+ -[WiFiAwarePeerAvailChannelEntry timeBitmap]
+ -[WiFiAwarePeerAvailChannelEntry usagePreference]
+ -[WiFiAwarePeerAvailChannelEntry utilization]
+ -[WiFiAwarePeerAvailInfo .cxx_destruct]
+ -[WiFiAwarePeerAvailInfo copyWithZone:]
+ -[WiFiAwarePeerAvailInfo description]
+ -[WiFiAwarePeerAvailInfo encodeWithCoder:]
+ -[WiFiAwarePeerAvailInfo initWithCoder:]
+ -[WiFiAwarePeerAvailInfo initWithInterfaceInfo:peerInfos:]
+ -[WiFiAwarePeerAvailInfo init]
+ -[WiFiAwarePeerAvailInfo interfaceInfo]
+ -[WiFiAwarePeerAvailInfo peerInfos]
+ -[WiFiAwarePeerAvailInfo(DetailedDescription) detailedDescriptionWithChangedOptions:previousPeerAvailInfo:forceAllChangedOptions:]
+ -[WiFiAwarePeerAvailInfo(DetailedDescription) detailedDescription]
+ -[WiFiAwarePeerDevice .cxx_destruct]
+ -[WiFiAwarePeerDevice description]
+ -[WiFiAwarePeerDevice encodeWithCoder:]
+ -[WiFiAwarePeerDevice initWithCoder:]
+ -[WiFiAwarePeerDevice initWithInstanceID:macAddress:]
+ -[WiFiAwarePeerDevice instanceID]
+ -[WiFiAwarePeerDevice macAddress]
+ -[WiFiAwarePeerDevice setInstanceID:]
+ -[WiFiAwarePeerDevice setMacAddress:]
+ -[WiFiAwarePeerInfo .cxx_destruct]
+ -[WiFiAwarePeerInfo committedEntries]
+ -[WiFiAwarePeerInfo conditionalEntries]
+ -[WiFiAwarePeerInfo copyWithZone:]
+ -[WiFiAwarePeerInfo description]
+ -[WiFiAwarePeerInfo encodeWithCoder:]
+ -[WiFiAwarePeerInfo initWithCoder:]
+ -[WiFiAwarePeerInfo initWithPeerAddress:committedEntries:potentialChannelEntries:potentialBandEntries:conditionalEntries:]
+ -[WiFiAwarePeerInfo peerAddress]
+ -[WiFiAwarePeerInfo potentialBandEntries]
+ -[WiFiAwarePeerInfo potentialChannelEntries]
+ -[WiFiAwarePerformanceForecast .cxx_destruct]
+ -[WiFiAwarePerformanceForecast copyWithZone:]
+ -[WiFiAwarePerformanceForecast description]
+ -[WiFiAwarePerformanceForecast encodeWithCoder:]
+ -[WiFiAwarePerformanceForecast hash]
+ -[WiFiAwarePerformanceForecast initWithCoder:]
+ -[WiFiAwarePerformanceForecast initWithTimestamp:localTimestamp:signalStrength:localThroughputCeilingMbps:localThroughputCapacityMbps:localThroughputCapacityRatio:localInfrastructureThroughputCapacityRatio:unavailabilityLatencyCeilingMs:]
+ -[WiFiAwarePerformanceForecast isEqual:]
+ -[WiFiAwarePerformanceForecast localInfrastructureThroughputCapacityRatio]
+ -[WiFiAwarePerformanceForecast localThroughputCapacityMbps]
+ -[WiFiAwarePerformanceForecast localThroughputCapacityRatio]
+ -[WiFiAwarePerformanceForecast localThroughputCeilingMbps]
+ -[WiFiAwarePerformanceForecast localTimestamp]
+ -[WiFiAwarePerformanceForecast signalStrength]
+ -[WiFiAwarePerformanceForecast timestamp]
+ -[WiFiAwarePerformanceForecast unavailabilityLatencyCeilingMs]
+ -[WiFiAwarePublishConfiguration setUserID:]
+ -[WiFiAwarePublishConfiguration userID]
+ -[WiFiAwarePublisher activatePairingModeWithConfig:delegate:completionHandler:]
+ -[WiFiAwarePublisher deactivatePairingMode]
+ -[WiFiAwarePublisher newPairingSessionFromInitiatorAddress:]
+ -[WiFiAwarePublisher pairingSession]
+ -[WiFiAwarePublisher publishReceivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:]
+ -[WiFiAwarePublisher receivedNewPairingSessionFromInitiatorAddress:withSubscriberInfo:]
+ -[WiFiAwarePublisher receivedNewPairingSessionFromInitiatorAddress:withSubscriberInfo:userApprovalHandler:]
+ -[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:]
+ -[WiFiAwarePublisher setPairingSession:]
+ -[WiFiAwareRadioSchedule initWithInterfaceInfo:band24GHz:band5GHz:supportsDualBand:supportsSimultaneousDualBand:primaryChannel:secondaryChannel:infraChannel:preferredChannels:]
+ -[WiFiAwareRadioSchedule interfaceInfo]
+ -[WiFiAwareRadioSchedule preferredChannels]
+ -[WiFiAwareState initWithInterfaceInfo:isFWElection:nanRole:hopCount:clusterId:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:]
+ -[WiFiAwareState interfaceInfo]
+ -[WiFiAwareStateMonitor beginPeerAvailMonitoring]
+ -[WiFiAwareStateMonitor channelSequenceChangedEvent:map1Channels:]
+ -[WiFiAwareStateMonitor endPeerAvailMonitoring]
+ -[WiFiAwareStateMonitor getFormattedPeerAvailInfoDescription:]
+ -[WiFiAwareStateMonitor lastPeerAvailChangedOptions]
+ -[WiFiAwareStateMonitor lastPeerAvailInfo]
+ -[WiFiAwareStateMonitor peerAvailInfoUpdatedHandler]
+ -[WiFiAwareStateMonitor queryNANPeerAvail]
+ -[WiFiAwareStateMonitor setLastPeerAvailChangedOptions:]
+ -[WiFiAwareStateMonitor setLastPeerAvailInfo:]
+ -[WiFiAwareStateMonitor setPeerAvailInfoUpdatedHandler:]
+ -[WiFiAwareStateMonitor updatedNANPeerAvail:]
+ -[WiFiAwareStateMonitor updatedNANPeerAvailWithChangedOptions:changedOptions:]
+ -[WiFiAwareStateMonitor updatedNANPeerAvailWithChangedOptions:changedOptions:forceAllChangedOptions:]
+ -[WiFiAwareSubscribeConfiguration setUserID:]
+ -[WiFiAwareSubscribeConfiguration userID]
+ -[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:]
+ -[WiFiAwareTDSConfig .cxx_destruct]
+ -[WiFiAwareTDSConfig copyWithZone:]
+ -[WiFiAwareTDSConfig description]
+ -[WiFiAwareTDSConfig deviceFilter]
+ -[WiFiAwareTDSConfig encodeWithCoder:]
+ -[WiFiAwareTDSConfig initWithCoder:]
+ -[WiFiAwareTDSConfig initWithOperation:serviceName:deviceFilter:]
+ -[WiFiAwareTDSConfig operation]
+ -[WiFiAwareTDSConfig serviceName]
+ -[WiFiAwareTDSDevice .cxx_destruct]
+ -[WiFiAwareTDSDevice bluetoothAddress]
+ -[WiFiAwareTDSDevice copyWithZone:]
+ -[WiFiAwareTDSDevice description]
+ -[WiFiAwareTDSDevice encodeWithCoder:]
+ -[WiFiAwareTDSDevice identifier]
+ -[WiFiAwareTDSDevice initWithCoder:]
+ -[WiFiAwareTDSDevice initWithName:identifier:bluetoothAddress:]
+ -[WiFiAwareTDSDevice name]
+ -[WiFiAwareTDSSession .cxx_destruct]
+ -[WiFiAwareTDSSession activate]
+ -[WiFiAwareTDSSession deactivate]
+ -[WiFiAwareTDSSession delegate]
+ -[WiFiAwareTDSSession exportedInterface]
+ -[WiFiAwareTDSSession exportedObject]
+ -[WiFiAwareTDSSession handleError:]
+ -[WiFiAwareTDSSession initWithTDSConfig:delegate:]
+ -[WiFiAwareTDSSession matchFound:transportState:]
+ -[WiFiAwareTDSSession pairedMatchFound:transportState:]
+ -[WiFiAwareTDSSession remoteObjectInterface]
+ -[WiFiAwareTDSSession setDelegate:]
+ -[WiFiAwareTDSSession setTdsConfig:]
+ -[WiFiAwareTDSSession startConnectionUsingProxy:completionHandler:]
+ -[WiFiAwareTDSSession tdsConfig]
+ -[WiFiAwareTDSSession timedOut]
+ -[WiFiP2PKeychainAgent .cxx_destruct]
+ -[WiFiP2PKeychainAgent activate]
+ -[WiFiP2PKeychainAgent addUsing:completionHandler:]
+ -[WiFiP2PKeychainAgent deleteUsing:completionHandler:]
+ -[WiFiP2PKeychainAgent exportedInterface]
+ -[WiFiP2PKeychainAgent exportedObject]
+ -[WiFiP2PKeychainAgent getUsing:completionHandler:]
+ -[WiFiP2PKeychainAgent init]
+ -[WiFiP2PKeychainAgent invalidate]
+ -[WiFiP2PKeychainAgent startConnectionUsingProxy:completionHandler:]
+ -[WiFiP2PKeychainAgent updateUsing:to:completionHandler:]
+ -[WiFiP2PNANStateMonitor .cxx_destruct]
+ -[WiFiP2PNANStateMonitor beginMonitoring]
+ -[WiFiP2PNANStateMonitor channelSequenceChangedEvent:map1Channels:]
+ -[WiFiP2PNANStateMonitor channelSequenceUpdatedEventHandler]
+ -[WiFiP2PNANStateMonitor endMonitoring]
+ -[WiFiP2PNANStateMonitor exportedInterface]
+ -[WiFiP2PNANStateMonitor exportedObject]
+ -[WiFiP2PNANStateMonitor init]
+ -[WiFiP2PNANStateMonitor setChannelSequenceUpdatedEventHandler:]
+ -[WiFiP2PNANStateMonitor startConnectionUsingProxy:completionHandler:]
+ -[WiFiP2PNANStateMonitor updatedNANAvailability:]
+ -[WiFiP2PNANStateMonitor updatedNANAvailabilityWithChangedOptions:changedOptions:]
+ -[WiFiP2PNANStateMonitor updatedNANAvailabilityWithChangedOptions:changedOptions:forceAllChangedOptions:]
+ -[WiFiP2PNANStateMonitor updatedNANDpState:]
+ -[WiFiP2PNANStateMonitor updatedNANDpStateWithChangedOptions:changedOptions:]
+ -[WiFiP2PNANStateMonitor updatedNANDpStateWithChangedOptions:changedOptions:forceAllChangedOptions:]
+ -[WiFiP2PNANStateMonitor updatedNANPeerAvail:]
+ -[WiFiP2PNANStateMonitor updatedNANPeerAvailWithChangedOptions:changedOptions:]
+ -[WiFiP2PNANStateMonitor updatedNANPeerAvailWithChangedOptions:changedOptions:forceAllChangedOptions:]
+ -[WiFiP2PNANStateMonitor updatedNANSrvInfo:]
+ -[WiFiP2PNANStateMonitor updatedNANSrvInfoWithChangedOptions:changedOptions:]
+ -[WiFiP2PNANStateMonitor updatedNANSrvInfoWithChangedOptions:changedOptions:forceAllChangedOptions:]
+ -[WiFiP2PNANStateMonitor updatedNANState:]
+ -[WiFiP2PNANStateMonitor updatedNANStateWithChangedOptions:changedOptions:]
+ -[WiFiP2PNANStateMonitor updatedNANStateWithChangedOptions:changedOptions:forceAllChangedOptions:]
+ -[WiFiP2PNANStateMonitorConfiguration copyWithZone:]
+ -[WiFiP2PNANStateMonitorConfiguration encodeWithCoder:]
+ -[WiFiP2PNANStateMonitorConfiguration initWithCoder:]
+ -[WiFiP2PNANStateMonitorConfiguration init]
+ -[WiFiP2PNANStateMonitorConfiguration options]
+ -[WiFiP2PNANStateMonitorConfiguration setOptions:]
+ -[WiFiP2PUIAgent showAccessoryNotificationWithUUID:deviceName:localization:completionHandler:]
+ -[WiFiP2PUIAgent userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:]
+ GCC_except_table133
+ GCC_except_table44
+ _.str.32
+ _AWDLTrafficRegistrationServiceTimeSyncCalibration
+ _CFCopyTypeIDDescription
+ _CreateNSErrorFrom
+ _NSClassFromString
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ _OBJC_CLASS_$_NSMeasurement
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSUnitDuration
+ _OBJC_CLASS_$_WiFiAwareChannelConfiguration
+ _OBJC_CLASS_$_WiFiAwareDataSessionConfig
+ _OBJC_CLASS_$_WiFiAwareInterfaceInfo
+ _OBJC_CLASS_$_WiFiAwareNDISessionCounters
+ _OBJC_CLASS_$_WiFiAwarePKBootstrappingRecordIngestionResult
+ _OBJC_CLASS_$_WiFiAwarePKBootstrappingRecords
+ _OBJC_CLASS_$_WiFiAwarePKBootstrappingRecordsIngestionReport
+ _OBJC_CLASS_$_WiFiAwarePKBootstrappingRecordsStore
+ _OBJC_CLASS_$_WiFiAwarePairingConfig
+ _OBJC_CLASS_$_WiFiAwarePairingSession
+ _OBJC_CLASS_$_WiFiAwarePeerAvailBandEntry
+ _OBJC_CLASS_$_WiFiAwarePeerAvailChannelEntry
+ _OBJC_CLASS_$_WiFiAwarePeerAvailInfo
+ _OBJC_CLASS_$_WiFiAwarePeerDevice
+ _OBJC_CLASS_$_WiFiAwarePeerInfo
+ _OBJC_CLASS_$_WiFiAwarePerformanceForecast
+ _OBJC_CLASS_$_WiFiAwareTDSConfig
+ _OBJC_CLASS_$_WiFiAwareTDSDevice
+ _OBJC_CLASS_$_WiFiAwareTDSSession
+ _OBJC_CLASS_$_WiFiP2PKeychainAgent
+ _OBJC_CLASS_$_WiFiP2PNANStateMonitor
+ _OBJC_CLASS_$_WiFiP2PNANStateMonitorConfiguration
+ _OBJC_CLASS_$__TtC14WiFiPeerToPeer15WiFiP2PKeychain
+ _OBJC_CLASS_$__TtC14WiFiPeerToPeer20WiFiP2PKeychainUtils
+ _OBJC_IVAR_$_WiFiAwareChannelConfiguration._preferredChannelClasses
+ _OBJC_IVAR_$_WiFiAwareChannelConfiguration._preferredChannelNumbers
+ _OBJC_IVAR_$_WiFiAwareDataPathState._interfaceInfo
+ _OBJC_IVAR_$_WiFiAwareDataSession._skipInfrastructureRelayCheck
+ _OBJC_IVAR_$_WiFiAwareDataSession._userID
+ _OBJC_IVAR_$_WiFiAwareDataSessionConfig._internetSharingConfiguration
+ _OBJC_IVAR_$_WiFiAwareDataSessionConfig._serviceType
+ _OBJC_IVAR_$_WiFiAwareDataSessionConfig._userID
+ _OBJC_IVAR_$_WiFiAwareDatapathConfiguration._skipInfrastructureRelayCheck
+ _OBJC_IVAR_$_WiFiAwareDatapathConfiguration._userID
+ _OBJC_IVAR_$_WiFiAwareDiscoveryResult._autoPairable
+ _OBJC_IVAR_$_WiFiAwareDiscoveryResult._performanceForecast
+ _OBJC_IVAR_$_WiFiAwareInterfaceInfo._interfaceAddr
+ _OBJC_IVAR_$_WiFiAwareInterfaceInfo._interfaceName
+ _OBJC_IVAR_$_WiFiAwareInterfaceInfo._isEnabled
+ _OBJC_IVAR_$_WiFiAwareNDISessionCounters._established
+ _OBJC_IVAR_$_WiFiAwareNDISessionCounters._rtm
+ _OBJC_IVAR_$_WiFiAwareNDISessionCounters._rtmLowLatency
+ _OBJC_IVAR_$_WiFiAwareNDISessionCounters._rtmWith24GOnly
+ _OBJC_IVAR_$_WiFiAwareNDISessionCounters._total
+ _OBJC_IVAR_$_WiFiAwareNDISessionCounters._with24GOnlyPeer
+ _OBJC_IVAR_$_WiFiAwarePKBootstrappingRecordIngestionResult._ingested
+ _OBJC_IVAR_$_WiFiAwarePKBootstrappingRecordIngestionResult._rejectionReason
+ _OBJC_IVAR_$_WiFiAwarePKBootstrappingRecords._bootstrappingRecords
+ _OBJC_IVAR_$_WiFiAwarePKBootstrappingRecords._expiration
+ _OBJC_IVAR_$_WiFiAwarePKBootstrappingRecordsIngestionReport._recordsProcessed
+ _OBJC_IVAR_$_WiFiAwarePKBootstrappingRecordsIngestionReport._results
+ _OBJC_IVAR_$_WiFiAwarePKBootstrappingRecordsStore._xpcConnection
+ _OBJC_IVAR_$_WiFiAwarePairingConfig._pairingMetadata
+ _OBJC_IVAR_$_WiFiAwarePairingConfig._pairingMode
+ _OBJC_IVAR_$_WiFiAwarePairingConfig._pairingSetupMode
+ _OBJC_IVAR_$_WiFiAwarePairingConfig._userID
+ _OBJC_IVAR_$_WiFiAwarePairingSession._delegate
+ _OBJC_IVAR_$_WiFiAwarePairingSession._discoveryResult
+ _OBJC_IVAR_$_WiFiAwarePairingSession._initiatorAddress
+ _OBJC_IVAR_$_WiFiAwarePairingSession._logger
+ _OBJC_IVAR_$_WiFiAwarePairingSession._pairingConfig
+ _OBJC_IVAR_$_WiFiAwarePairingSession._publishID
+ _OBJC_IVAR_$_WiFiAwarePairingSession._role
+ _OBJC_IVAR_$_WiFiAwarePairingSession._xpcConnection
+ _OBJC_IVAR_$_WiFiAwarePeerAvailBandEntry._bands
+ _OBJC_IVAR_$_WiFiAwarePeerAvailBandEntry._mapId
+ _OBJC_IVAR_$_WiFiAwarePeerAvailBandEntry._rxNSS
+ _OBJC_IVAR_$_WiFiAwarePeerAvailBandEntry._usagePreference
+ _OBJC_IVAR_$_WiFiAwarePeerAvailBandEntry._utilization
+ _OBJC_IVAR_$_WiFiAwarePeerAvailChannelEntry._band
+ _OBJC_IVAR_$_WiFiAwarePeerAvailChannelEntry._bandwidth
+ _OBJC_IVAR_$_WiFiAwarePeerAvailChannelEntry._channel
+ _OBJC_IVAR_$_WiFiAwarePeerAvailChannelEntry._mapId
+ _OBJC_IVAR_$_WiFiAwarePeerAvailChannelEntry._offset
+ _OBJC_IVAR_$_WiFiAwarePeerAvailChannelEntry._period
+ _OBJC_IVAR_$_WiFiAwarePeerAvailChannelEntry._rxNSS
+ _OBJC_IVAR_$_WiFiAwarePeerAvailChannelEntry._timeBitmap
+ _OBJC_IVAR_$_WiFiAwarePeerAvailChannelEntry._usagePreference
+ _OBJC_IVAR_$_WiFiAwarePeerAvailChannelEntry._utilization
+ _OBJC_IVAR_$_WiFiAwarePeerAvailInfo._interfaceInfo
+ _OBJC_IVAR_$_WiFiAwarePeerAvailInfo._peerInfos
+ _OBJC_IVAR_$_WiFiAwarePeerDevice._instanceID
+ _OBJC_IVAR_$_WiFiAwarePeerDevice._macAddress
+ _OBJC_IVAR_$_WiFiAwarePeerInfo._committedEntries
+ _OBJC_IVAR_$_WiFiAwarePeerInfo._conditionalEntries
+ _OBJC_IVAR_$_WiFiAwarePeerInfo._peerAddress
+ _OBJC_IVAR_$_WiFiAwarePeerInfo._potentialBandEntries
+ _OBJC_IVAR_$_WiFiAwarePeerInfo._potentialChannelEntries
+ _OBJC_IVAR_$_WiFiAwarePerformanceForecast._localInfrastructureThroughputCapacityRatio
+ _OBJC_IVAR_$_WiFiAwarePerformanceForecast._localThroughputCapacityMbps
+ _OBJC_IVAR_$_WiFiAwarePerformanceForecast._localThroughputCapacityRatio
+ _OBJC_IVAR_$_WiFiAwarePerformanceForecast._localThroughputCeilingMbps
+ _OBJC_IVAR_$_WiFiAwarePerformanceForecast._localTimestamp
+ _OBJC_IVAR_$_WiFiAwarePerformanceForecast._signalStrength
+ _OBJC_IVAR_$_WiFiAwarePerformanceForecast._timestamp
+ _OBJC_IVAR_$_WiFiAwarePerformanceForecast._unavailabilityLatencyCeilingMs
+ _OBJC_IVAR_$_WiFiAwarePublishConfiguration._userID
+ _OBJC_IVAR_$_WiFiAwarePublisher._activePairingSessions
+ _OBJC_IVAR_$_WiFiAwarePublisher._pairingConfig
+ _OBJC_IVAR_$_WiFiAwarePublisher._pairingDelegate
+ _OBJC_IVAR_$_WiFiAwarePublisher._pairingSession
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._interfaceInfo
+ _OBJC_IVAR_$_WiFiAwareRadioSchedule._preferredChannels
+ _OBJC_IVAR_$_WiFiAwareState._interfaceInfo
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._lastConfiguration
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._lastPeerAvailChangedOptions
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._lastPeerAvailInfo
+ _OBJC_IVAR_$_WiFiAwareStateMonitor._peerAvailInfoUpdatedHandler
+ _OBJC_IVAR_$_WiFiAwareSubscribeConfiguration._userID
+ _OBJC_IVAR_$_WiFiAwareTDSConfig._deviceFilter
+ _OBJC_IVAR_$_WiFiAwareTDSConfig._operation
+ _OBJC_IVAR_$_WiFiAwareTDSConfig._serviceName
+ _OBJC_IVAR_$_WiFiAwareTDSDevice._bluetoothAddress
+ _OBJC_IVAR_$_WiFiAwareTDSDevice._identifier
+ _OBJC_IVAR_$_WiFiAwareTDSDevice._name
+ _OBJC_IVAR_$_WiFiAwareTDSSession._delegate
+ _OBJC_IVAR_$_WiFiAwareTDSSession._logger
+ _OBJC_IVAR_$_WiFiAwareTDSSession._tdsConfig
+ _OBJC_IVAR_$_WiFiAwareTDSSession._xpcConnection
+ _OBJC_IVAR_$_WiFiP2PKeychainAgent._keychain
+ _OBJC_IVAR_$_WiFiP2PKeychainAgent._logger
+ _OBJC_IVAR_$_WiFiP2PKeychainAgent._xpcConnection
+ _OBJC_IVAR_$_WiFiP2PNANStateMonitor._channelSequenceUpdatedEventHandler
+ _OBJC_IVAR_$_WiFiP2PNANStateMonitor._xpcConnection
+ _OBJC_IVAR_$_WiFiP2PNANStateMonitorConfiguration._options
+ _OBJC_IVAR_$_WiFiP2PUIAgent._logger
+ _OBJC_METACLASS_$_WiFiAwareChannelConfiguration
+ _OBJC_METACLASS_$_WiFiAwareDataSessionConfig
+ _OBJC_METACLASS_$_WiFiAwareInterfaceInfo
+ _OBJC_METACLASS_$_WiFiAwareNDISessionCounters
+ _OBJC_METACLASS_$_WiFiAwarePKBootstrappingRecordIngestionResult
+ _OBJC_METACLASS_$_WiFiAwarePKBootstrappingRecords
+ _OBJC_METACLASS_$_WiFiAwarePKBootstrappingRecordsIngestionReport
+ _OBJC_METACLASS_$_WiFiAwarePKBootstrappingRecordsStore
+ _OBJC_METACLASS_$_WiFiAwarePairingConfig
+ _OBJC_METACLASS_$_WiFiAwarePairingSession
+ _OBJC_METACLASS_$_WiFiAwarePeerAvailBandEntry
+ _OBJC_METACLASS_$_WiFiAwarePeerAvailChannelEntry
+ _OBJC_METACLASS_$_WiFiAwarePeerAvailInfo
+ _OBJC_METACLASS_$_WiFiAwarePeerDevice
+ _OBJC_METACLASS_$_WiFiAwarePeerInfo
+ _OBJC_METACLASS_$_WiFiAwarePerformanceForecast
+ _OBJC_METACLASS_$_WiFiAwareTDSConfig
+ _OBJC_METACLASS_$_WiFiAwareTDSDevice
+ _OBJC_METACLASS_$_WiFiAwareTDSSession
+ _OBJC_METACLASS_$_WiFiP2PKeychainAgent
+ _OBJC_METACLASS_$_WiFiP2PNANStateMonitor
+ _OBJC_METACLASS_$_WiFiP2PNANStateMonitorConfiguration
+ _OBJC_METACLASS_$__TtC14WiFiPeerToPeer15WiFiP2PKeychain
+ _OBJC_METACLASS_$__TtC14WiFiPeerToPeer20WiFiP2PKeychainUtils
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
+ _SecItemUpdate
+ _UNNotificationDismissActionIdentifier
+ _WiFiAwareFormatChannelWithBandwidth
+ _WiFiAwareFormatTimeBitmap
+ _WiFiAwareFormatTimeBitmapForPeriod
+ _WiFiAwareFormatTimeBitmapWithChanges
+ _WiFiAwareFormatTimeBitmapWithChangesForPeriod
+ _WiFiAwarePairingClientToString
+ _WiFiAwarePairingStorageClassToString
+ __CLASS_METHODS__TtC14WiFiPeerToPeer20WiFiP2PKeychainUtils
+ __DATA__TtC14WiFiPeerToPeer15WiFiP2PKeychain
+ __DATA__TtC14WiFiPeerToPeer20WiFiP2PKeychainUtils
+ __INSTANCE_METHODS__TtC14WiFiPeerToPeer15WiFiP2PKeychain
+ __INSTANCE_METHODS__TtC14WiFiPeerToPeer20WiFiP2PKeychainUtils
+ __IVARS__TtC14WiFiPeerToPeer15WiFiP2PKeychain
+ __METACLASS_DATA__TtC14WiFiPeerToPeer15WiFiP2PKeychain
+ __METACLASS_DATA__TtC14WiFiPeerToPeer20WiFiP2PKeychainUtils
+ __OBJC_$_CLASS_METHODS_WiFiAwareDataSessionConfig
+ __OBJC_$_CLASS_METHODS_WiFiAwareInterfaceInfo
+ __OBJC_$_CLASS_METHODS_WiFiAwarePKBootstrappingRecordIngestionResult
+ __OBJC_$_CLASS_METHODS_WiFiAwarePKBootstrappingRecords
+ __OBJC_$_CLASS_METHODS_WiFiAwarePKBootstrappingRecordsIngestionReport
+ __OBJC_$_CLASS_METHODS_WiFiAwarePairingConfig
+ __OBJC_$_CLASS_METHODS_WiFiAwarePairingSession
+ __OBJC_$_CLASS_METHODS_WiFiAwarePeerAvailBandEntry
+ __OBJC_$_CLASS_METHODS_WiFiAwarePeerAvailChannelEntry
+ __OBJC_$_CLASS_METHODS_WiFiAwarePeerAvailInfo
+ __OBJC_$_CLASS_METHODS_WiFiAwarePeerDevice
+ __OBJC_$_CLASS_METHODS_WiFiAwarePeerInfo
+ __OBJC_$_CLASS_METHODS_WiFiAwarePerformanceForecast
+ __OBJC_$_CLASS_METHODS_WiFiAwareTDSConfig
+ __OBJC_$_CLASS_METHODS_WiFiAwareTDSDevice
+ __OBJC_$_CLASS_METHODS_WiFiP2PNANStateMonitorConfiguration
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareDataSessionConfig
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareInterfaceInfo
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePKBootstrappingRecordIngestionResult
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePKBootstrappingRecords
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePKBootstrappingRecordsIngestionReport
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePairingConfig
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePeerAvailBandEntry
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePeerAvailChannelEntry
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePeerAvailInfo
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePeerDevice
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePeerInfo
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwarePerformanceForecast
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareTDSConfig
+ __OBJC_$_CLASS_PROP_LIST_WiFiAwareTDSDevice
+ __OBJC_$_CLASS_PROP_LIST_WiFiP2PNANStateMonitorConfiguration
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareChannelConfiguration
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareDataSessionConfig
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareInterfaceInfo
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareNDISessionCounters
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePKBootstrappingRecordIngestionResult
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePKBootstrappingRecords
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePKBootstrappingRecordsIngestionReport
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePKBootstrappingRecordsStore
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePairingConfig
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePairingSession
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePeerAvailBandEntry
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePeerAvailChannelEntry
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePeerAvailInfo(DetailedDescription)
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePeerDevice
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePeerInfo
+ __OBJC_$_INSTANCE_METHODS_WiFiAwarePerformanceForecast
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareTDSConfig
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareTDSDevice
+ __OBJC_$_INSTANCE_METHODS_WiFiAwareTDSSession
+ __OBJC_$_INSTANCE_METHODS_WiFiP2PKeychainAgent
+ __OBJC_$_INSTANCE_METHODS_WiFiP2PNANStateMonitor
+ __OBJC_$_INSTANCE_METHODS_WiFiP2PNANStateMonitorConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareChannelConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareDataSessionConfig
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareInterfaceInfo
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareNDISessionCounters
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePKBootstrappingRecordIngestionResult
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePKBootstrappingRecords
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePKBootstrappingRecordsIngestionReport
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePKBootstrappingRecordsStore
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePairingConfig
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePairingSession
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePeerAvailBandEntry
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePeerAvailChannelEntry
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePeerAvailInfo
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePeerDevice
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePeerInfo
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwarePerformanceForecast
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareTDSConfig
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareTDSDevice
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAwareTDSSession
+ __OBJC_$_INSTANCE_VARIABLES_WiFiP2PKeychainAgent
+ __OBJC_$_INSTANCE_VARIABLES_WiFiP2PNANStateMonitor
+ __OBJC_$_INSTANCE_VARIABLES_WiFiP2PNANStateMonitorConfiguration
+ __OBJC_$_PROP_LIST_WiFiAwareChannelConfiguration
+ __OBJC_$_PROP_LIST_WiFiAwareDataSessionConfig
+ __OBJC_$_PROP_LIST_WiFiAwareInterfaceInfo
+ __OBJC_$_PROP_LIST_WiFiAwareNDISessionCounters
+ __OBJC_$_PROP_LIST_WiFiAwarePKBootstrappingRecordIngestionResult
+ __OBJC_$_PROP_LIST_WiFiAwarePKBootstrappingRecords
+ __OBJC_$_PROP_LIST_WiFiAwarePKBootstrappingRecordsIngestionReport
+ __OBJC_$_PROP_LIST_WiFiAwarePKBootstrappingRecordsStore
+ __OBJC_$_PROP_LIST_WiFiAwarePairingConfig
+ __OBJC_$_PROP_LIST_WiFiAwarePairingSession
+ __OBJC_$_PROP_LIST_WiFiAwarePeerAvailBandEntry
+ __OBJC_$_PROP_LIST_WiFiAwarePeerAvailChannelEntry
+ __OBJC_$_PROP_LIST_WiFiAwarePeerAvailInfo
+ __OBJC_$_PROP_LIST_WiFiAwarePeerDevice
+ __OBJC_$_PROP_LIST_WiFiAwarePeerInfo
+ __OBJC_$_PROP_LIST_WiFiAwarePerformanceForecast
+ __OBJC_$_PROP_LIST_WiFiAwareTDSConfig
+ __OBJC_$_PROP_LIST_WiFiAwareTDSDevice
+ __OBJC_$_PROP_LIST_WiFiAwareTDSSession
+ __OBJC_$_PROP_LIST_WiFiP2PNANStateMonitor
+ __OBJC_$_PROP_LIST_WiFiP2PNANStateMonitorConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_WiFiAwarePairingXPCDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiAwarePKRecordsXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiAwarePairingXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiAwarePairingXPCDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiAwareTDSXPCDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiP2PKeychainAgentXPCDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiP2PNANStateMonitorXPCDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwarePKRecordsXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwarePairingXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwarePairingXPCDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwareTDSXPCDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiP2PKeychainAgentXPCDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiP2PNANStateMonitorXPCDelegate
+ __OBJC_$_PROTOCOL_REFS_WiFiAwarePKRecordsXPC
+ __OBJC_$_PROTOCOL_REFS_WiFiAwarePairingXPC
+ __OBJC_$_PROTOCOL_REFS_WiFiAwarePairingXPCDelegate
+ __OBJC_$_PROTOCOL_REFS_WiFiAwareTDSXPC
+ __OBJC_$_PROTOCOL_REFS_WiFiAwareTDSXPCDelegate
+ __OBJC_$_PROTOCOL_REFS_WiFiP2PKeychainAgentXPCDelegate
+ __OBJC_$_PROTOCOL_REFS_WiFiP2PNANStateMonitorXPCDelegate
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareDataSessionConfig
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareInterfaceInfo
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePKBootstrappingRecordIngestionResult
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePKBootstrappingRecords
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePKBootstrappingRecordsIngestionReport
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePKBootstrappingRecordsStore
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePairingConfig
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePairingSession
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePeerAvailBandEntry
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePeerAvailChannelEntry
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePeerAvailInfo
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePeerDevice
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePeerInfo
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwarePerformanceForecast
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareTDSConfig
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareTDSDevice
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAwareTDSSession
+ __OBJC_CLASS_PROTOCOLS_$_WiFiP2PNANStateMonitor
+ __OBJC_CLASS_PROTOCOLS_$_WiFiP2PNANStateMonitorConfiguration
+ __OBJC_CLASS_RO_$_WiFiAwareChannelConfiguration
+ __OBJC_CLASS_RO_$_WiFiAwareDataSessionConfig
+ __OBJC_CLASS_RO_$_WiFiAwareInterfaceInfo
+ __OBJC_CLASS_RO_$_WiFiAwareNDISessionCounters
+ __OBJC_CLASS_RO_$_WiFiAwarePKBootstrappingRecordIngestionResult
+ __OBJC_CLASS_RO_$_WiFiAwarePKBootstrappingRecords
+ __OBJC_CLASS_RO_$_WiFiAwarePKBootstrappingRecordsIngestionReport
+ __OBJC_CLASS_RO_$_WiFiAwarePKBootstrappingRecordsStore
+ __OBJC_CLASS_RO_$_WiFiAwarePairingConfig
+ __OBJC_CLASS_RO_$_WiFiAwarePairingSession
+ __OBJC_CLASS_RO_$_WiFiAwarePeerAvailBandEntry
+ __OBJC_CLASS_RO_$_WiFiAwarePeerAvailChannelEntry
+ __OBJC_CLASS_RO_$_WiFiAwarePeerAvailInfo
+ __OBJC_CLASS_RO_$_WiFiAwarePeerDevice
+ __OBJC_CLASS_RO_$_WiFiAwarePeerInfo
+ __OBJC_CLASS_RO_$_WiFiAwarePerformanceForecast
+ __OBJC_CLASS_RO_$_WiFiAwareTDSConfig
+ __OBJC_CLASS_RO_$_WiFiAwareTDSDevice
+ __OBJC_CLASS_RO_$_WiFiAwareTDSSession
+ __OBJC_CLASS_RO_$_WiFiP2PKeychainAgent
+ __OBJC_CLASS_RO_$_WiFiP2PNANStateMonitor
+ __OBJC_CLASS_RO_$_WiFiP2PNANStateMonitorConfiguration
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwarePKRecordsXPC
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwarePairingXPC
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwarePairingXPCDelegate
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwareTDSXPC
+ __OBJC_LABEL_PROTOCOL_$_WiFiAwareTDSXPCDelegate
+ __OBJC_LABEL_PROTOCOL_$_WiFiP2PKeychainAgentXPCDelegate
+ __OBJC_LABEL_PROTOCOL_$_WiFiP2PNANStateMonitorXPCDelegate
+ __OBJC_METACLASS_RO_$_WiFiAwareChannelConfiguration
+ __OBJC_METACLASS_RO_$_WiFiAwareDataSessionConfig
+ __OBJC_METACLASS_RO_$_WiFiAwareInterfaceInfo
+ __OBJC_METACLASS_RO_$_WiFiAwareNDISessionCounters
+ __OBJC_METACLASS_RO_$_WiFiAwarePKBootstrappingRecordIngestionResult
+ __OBJC_METACLASS_RO_$_WiFiAwarePKBootstrappingRecords
+ __OBJC_METACLASS_RO_$_WiFiAwarePKBootstrappingRecordsIngestionReport
+ __OBJC_METACLASS_RO_$_WiFiAwarePKBootstrappingRecordsStore
+ __OBJC_METACLASS_RO_$_WiFiAwarePairingConfig
+ __OBJC_METACLASS_RO_$_WiFiAwarePairingSession
+ __OBJC_METACLASS_RO_$_WiFiAwarePeerAvailBandEntry
+ __OBJC_METACLASS_RO_$_WiFiAwarePeerAvailChannelEntry
+ __OBJC_METACLASS_RO_$_WiFiAwarePeerAvailInfo
+ __OBJC_METACLASS_RO_$_WiFiAwarePeerDevice
+ __OBJC_METACLASS_RO_$_WiFiAwarePeerInfo
+ __OBJC_METACLASS_RO_$_WiFiAwarePerformanceForecast
+ __OBJC_METACLASS_RO_$_WiFiAwareTDSConfig
+ __OBJC_METACLASS_RO_$_WiFiAwareTDSDevice
+ __OBJC_METACLASS_RO_$_WiFiAwareTDSSession
+ __OBJC_METACLASS_RO_$_WiFiP2PKeychainAgent
+ __OBJC_METACLASS_RO_$_WiFiP2PNANStateMonitor
+ __OBJC_METACLASS_RO_$_WiFiP2PNANStateMonitorConfiguration
+ __OBJC_PROTOCOL_$_WiFiAwarePKRecordsXPC
+ __OBJC_PROTOCOL_$_WiFiAwarePairingXPC
+ __OBJC_PROTOCOL_$_WiFiAwarePairingXPCDelegate
+ __OBJC_PROTOCOL_$_WiFiAwareTDSXPC
+ __OBJC_PROTOCOL_$_WiFiAwareTDSXPCDelegate
+ __OBJC_PROTOCOL_$_WiFiP2PKeychainAgentXPCDelegate
+ __OBJC_PROTOCOL_$_WiFiP2PNANStateMonitorXPCDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiAwarePKRecordsXPC
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiAwarePairingXPC
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiAwarePairingXPCDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiAwareTDSXPC
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiAwareTDSXPCDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiP2PKeychainAgentXPCDelegate
+ __OBJC_PROTOCOL_REFERENCE_$_WiFiP2PNANStateMonitorXPCDelegate
+ ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.117
+ ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.120
+ ___118-[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:]_block_invoke
+ ___119-[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:]_block_invoke
+ ___130-[WiFiAwarePeerAvailInfo(DetailedDescription) detailedDescriptionWithChangedOptions:previousPeerAvailInfo:forceAllChangedOptions:]_block_invoke
+ ___130-[WiFiAwarePeerAvailInfo(DetailedDescription) detailedDescriptionWithChangedOptions:previousPeerAvailInfo:forceAllChangedOptions:]_block_invoke_2
+ ___130-[WiFiAwarePeerAvailInfo(DetailedDescription) detailedDescriptionWithChangedOptions:previousPeerAvailInfo:forceAllChangedOptions:]_block_invoke_3
+ ___130-[WiFiAwarePeerAvailInfo(DetailedDescription) detailedDescriptionWithChangedOptions:previousPeerAvailInfo:forceAllChangedOptions:]_block_invoke_4
+ ___33-[WiFiAwareTDSSession deactivate]_block_invoke
+ ___37-[WiFiAwarePairingSession deactivate]_block_invoke
+ ___39-[WiFiAwareDiscoveryResult description]_block_invoke
+ ___42-[WiFiAwareStateMonitor queryNANPeerAvail]_block_invoke
+ ___42-[WiFiAwareStateMonitor queryNANPeerAvail]_block_invoke_2
+ ___43-[WiFiAwarePublisher deactivatePairingMode]_block_invoke
+ ___43-[WiFiAwarePublisher deactivatePairingMode]_block_invoke_2
+ ___61-[WiFiP2PUIAgent configureNotificationsWithBundleIdentifier:]_block_invoke
+ ___65-[WiFiAwarePairingSession requiresPINInputWithCompletionHandler:]_block_invoke
+ ___71-[AWDLServiceDiscoveryManager addAWDLDiscoveryClient:forService:error:]_block_invoke
+ ___72-[WiFiAwarePairingSession requiresPassphraseInputWithCompletionHandler:]_block_invoke
+ ___73-[WiFiAwarePKBootstrappingRecordsStore queryLocalPKBootstrappingRecords:]_block_invoke
+ ___74-[AWDLServiceDiscoveryManager removeAWDLDiscoveryClient:forService:error:]_block_invoke
+ ___76-[AWDLServiceDiscoveryManager refreshAWDLDiscoveryActivityForService:error:]_block_invoke
+ ___79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.165
+ ___79-[WiFiAwarePublisher activatePairingModeWithConfig:delegate:completionHandler:]_block_invoke
+ ___79-[WiFiAwarePublisher activatePairingModeWithConfig:delegate:completionHandler:]_block_invoke_2
+ ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke.179
+ ___82-[WiFiAwarePKBootstrappingRecordsStore queryEphemeralLocalPKBootstrappingRecords:]_block_invoke
+ ___83-[WiFiAwarePKBootstrappingRecordsStore addRemotePKBootstrappingRecords:completion:]_block_invoke
+ ___block_descriptor_32_e75_q24?0"WiFiAwarePeerAvailChannelEntry"8"WiFiAwarePeerAvailChannelEntry"16l
+ ___block_descriptor_40_e8_32bs_e18_v16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32bs_e32_v16?0"WiFiAwarePeerAvailInfo"8ls32l8
+ ___block_descriptor_40_e8_32bs_e33_v16?0"<WiFiAwarePKRecordsXPC>"8ls32l8
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_40_e8_32s_e33_v16?0"<WiFiAwarePublisherXPC>"8ls32l8
+ ___block_descriptor_40_e8_32s_e55_v32?0"NSNumber"8"WiFiAwarePerformanceForecast"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e8_v16?0q8ls32l8
+ ___block_descriptor_40_e8_32w_e31_v16?0"<WiFiAwarePairingXPC>"8lw32l8
+ ___block_descriptor_40_e8_32w_e8_v16?08lw32l8
+ ___block_descriptor_48_e8_32s40bs_e33_v16?0"<WiFiAwarePKRecordsXPC>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e40_v24?0"<WiFiP2PXPCProtocol>"8?<v?q>16ls32l8s40l8
+ ___block_descriptor_50_e8_32s40s_e44_v24?0"<WiFiAwareSubscriberXPC>"8?<v?q>16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e21_v24?0q8"NSString"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e33_v16?0"<WiFiAwarePublisherXPC>"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.104
+ ___block_literal_global.107
+ ___block_literal_global.116
+ ___block_literal_global.194
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.202
+ ___block_literal_global.245
+ ___block_literal_global.282
+ ___block_literal_global.289
+ ___block_literal_global.292
+ ___block_literal_global.295
+ ___block_literal_global.301
+ ___block_literal_global.320
+ ___block_literal_global.325
+ ___block_literal_global.397
+ ___block_literal_global.52
+ ___block_literal_global.577
+ ___block_literal_global.638
+ ___block_literal_global.640
+ ___block_literal_global.642
+ ___block_literal_global.87
+ ___block_literal_global.89
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_WiFiPeerToPeer
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_WiFiPeerToPeer
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_WiFiPeerToPeer
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_WiFiPeerToPeer
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_WiFiPeerToPeer
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_WiFiPeerToPeer
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_WiFiPeerToPeer
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_WiFiPeerToPeer
+ __swift_stdlib_malloc_size
+ _bytesToShowForPeriod
+ _bzero
+ _getuid
+ _kSecAttrAccount
+ _kSecValueData
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$WiFiAwarePairingRoleToString:
+ _objc_msgSend$actionIdentifier
+ _objc_msgSend$activateForPublishID:initiatorAddress:
+ _objc_msgSend$activatePairingModeWithConfig:completionHandler:
+ _objc_msgSend$addAWDLDiscoveryClient:forService:completionHandler:
+ _objc_msgSend$addRemotePKRecords:completion:
+ _objc_msgSend$addWithQuery:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$attachToPairingResponderForPublishID:initiatorAddress:completionHandler:
+ _objc_msgSend$autoPairable
+ _objc_msgSend$bands
+ _objc_msgSend$bluetoothAddress
+ _objc_msgSend$bundleIdentifier
+ _objc_msgSend$categoryIdentifier
+ _objc_msgSend$committedEntries
+ _objc_msgSend$conditionalEntries
+ _objc_msgSend$content
+ _objc_msgSend$createPKRecordsStore:
+ _objc_msgSend$createPairingInitiatorForDiscoveryResult:pairingConfig:completionHandler:
+ _objc_msgSend$createTDSSessionWithConfiguration:completionHandler:
+ _objc_msgSend$deactivatePairingMode:
+ _objc_msgSend$defaultCenter
+ _objc_msgSend$deleteWithQuery:
+ _objc_msgSend$detailedDescriptionWithChangedOptions:previousPeerAvailInfo:forceAllChangedOptions:
+ _objc_msgSend$deviceFilter
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$established
+ _objc_msgSend$getWithQuery:results:
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithDiscoveryResult:serviceType:serviceSpecificInfo:
+ _objc_msgSend$initWithIngested:rejectionReason:
+ _objc_msgSend$initWithInterfaceInfo:band24GHz:band5GHz:supportsDualBand:supportsSimultaneousDualBand:primaryChannel:secondaryChannel:infraChannel:preferredChannels:
+ _objc_msgSend$initWithInterfaceInfo:isFWElection:nanRole:hopCount:clusterId:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:
+ _objc_msgSend$initWithInterfaceInfo:peerInfos:
+ _objc_msgSend$initWithInterfaceInfo:sessionCounters:channelConfig:ndiInfos:ndiSessionInfos:
+ _objc_msgSend$initWithInterfaceName:interfaceAddr:isEnabled:
+ _objc_msgSend$initWithMapId:bands:usagePreference:rxNSS:utilization:
+ _objc_msgSend$initWithMapId:channel:bandwidth:band:period:offset:timeBitmap:usagePreference:rxNSS:utilization:
+ _objc_msgSend$initWithName:identifier:bluetoothAddress:
+ _objc_msgSend$initWithNdiName:ndiAddr:sessionCount:qosType:security:
+ _objc_msgSend$initWithOperation:serviceName:deviceFilter:
+ _objc_msgSend$initWithPairingConfig:delegate:
+ _objc_msgSend$initWithPairingMode:pairingMetadata:
+ _objc_msgSend$initWithPeerAddress:committedEntries:potentialChannelEntries:potentialBandEntries:conditionalEntries:
+ _objc_msgSend$initWithPreferredChannelNumbers:preferredChannelClasses:
+ _objc_msgSend$initWithRecordsProcessed:ingestionResults:
+ _objc_msgSend$initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:pairedUUID:pairedDeviceName:signature:autoPairable:performanceForecast:
+ _objc_msgSend$initWithServiceType:internetSharingConfiguration:
+ _objc_msgSend$initWithTimestamp:localTimestamp:signalStrength:localThroughputCeilingMbps:localThroughputCapacityMbps:localThroughputCapacityRatio:localInfrastructureThroughputCapacityRatio:unavailabilityLatencyCeilingMs:
+ _objc_msgSend$initWithTotal:established:with24GOnlyPeer:rtm:rtmWith24GOnly:rtmLowLatency:
+ _objc_msgSend$initWithexpiration:bootstrappingRecords:
+ _objc_msgSend$instanceID
+ _objc_msgSend$interfaceInfo
+ _objc_msgSend$lastPeerAvailChangedOptions
+ _objc_msgSend$lastPeerAvailInfo
+ _objc_msgSend$localInfrastructureThroughputCapacityRatio
+ _objc_msgSend$localThroughputCapacityMbps
+ _objc_msgSend$localThroughputCapacityRatio
+ _objc_msgSend$localThroughputCeilingMbps
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$mainBundle
+ _objc_msgSend$mapId
+ _objc_msgSend$name
+ _objc_msgSend$notification
+ _objc_msgSend$offset
+ _objc_msgSend$operation
+ _objc_msgSend$pairingMode
+ _objc_msgSend$pairingSession:didFailTo:error:
+ _objc_msgSend$pairingSession:didSucceedWithDeviceInfo:pairingStoreID:
+ _objc_msgSend$pairingSession:requiresPINDisplay:
+ _objc_msgSend$pairingSession:requiresPINInputWithCompletionHandler:
+ _objc_msgSend$pairingSession:requiresPassphraseDisplay:
+ _objc_msgSend$pairingSession:requiresPassphraseInputWithCompletionHandler:
+ _objc_msgSend$pairingSessionFailedToStart:
+ _objc_msgSend$peerAvailInfoUpdatedHandler
+ _objc_msgSend$peerInfos
+ _objc_msgSend$performanceForecast
+ _objc_msgSend$postNotificationName:object:userInfo:
+ _objc_msgSend$potentialBandEntries
+ _objc_msgSend$potentialChannelEntries
+ _objc_msgSend$preferredChannels
+ _objc_msgSend$publisher:newPairingSession:
+ _objc_msgSend$publisher:receivedCCADataForMulticastSession:ccaOBSS:ccaNonWiFi:
+ _objc_msgSend$publisher:receivedNewPairingSession:withInfo:
+ _objc_msgSend$publisher:receivedNewPairingSession:withInfo:userApprovalHandler:
+ _objc_msgSend$queryEphemeralLocalPKRecords:
+ _objc_msgSend$queryLocalPKRecords:
+ _objc_msgSend$queryNANPeerAvailWithCompletionHandler:
+ _objc_msgSend$refreshAWDLDiscoveryActivityForService:completionHandler:
+ _objc_msgSend$removeAWDLDiscoveryClient:forService:completionHandler:
+ _objc_msgSend$request
+ _objc_msgSend$requestAuthorizationWithOptions:completionHandler:
+ _objc_msgSend$rtm
+ _objc_msgSend$rtmLowLatency
+ _objc_msgSend$rtmWith24GOnly
+ _objc_msgSend$rxNSS
+ _objc_msgSend$sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:
+ _objc_msgSend$serializeKeychainResults:resultType:
+ _objc_msgSend$set
+ _objc_msgSend$setCategoryIdentifier:
+ _objc_msgSend$setLastPeerAvailChangedOptions:
+ _objc_msgSend$setLastPeerAvailInfo:
+ _objc_msgSend$setPairingMode:
+ _objc_msgSend$setServiceType:
+ _objc_msgSend$setShouldAuthenticateDefaultAction:
+ _objc_msgSend$setShouldBackgroundDefaultAction:
+ _objc_msgSend$setSkipInfrastructureRelayCheck:
+ _objc_msgSend$setUserID:
+ _objc_msgSend$setUserInfo:
+ _objc_msgSend$setWantsNotificationResponsesDelivered
+ _objc_msgSend$skipInfrastructureRelayCheck
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$stringForDeviceFilter:
+ _objc_msgSend$stringForOperation:
+ _objc_msgSend$stringForPairSetupMode:
+ _objc_msgSend$stringForPairingMode:
+ _objc_msgSend$stringForRejectionReason:
+ _objc_msgSend$tdsSession:failedToActivate:
+ _objc_msgSend$tdsSession:foundMatch:transportState:
+ _objc_msgSend$tdsSession:foundPairedMatch:transportState:
+ _objc_msgSend$tdsSessionTimedOut:
+ _objc_msgSend$term
+ _objc_msgSend$total
+ _objc_msgSend$unavailabilityLatencyCeilingMs
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updateWithQuery:updates:
+ _objc_msgSend$updatedNANPeerAvailWithChangedOptions:changedOptions:
+ _objc_msgSend$usagePreference
+ _objc_msgSend$userID
+ _objc_msgSend$userInfo
+ _objc_msgSend$utilization
+ _objc_msgSend$with24GOnlyPeer
+ _objc_opt_self
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _os_log_create
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_retain_x20
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic SDySSypG
+ _symbolic SaySDySSypGG
+ _symbolic So8NSObjectC
+ _symbolic So8NSObjectCSg
+ _symbolic _____ 010WiFiPeerToC00aB11P2PKeychainC
+ _symbolic _____ 010WiFiPeerToC00aB16P2PKeychainUtilsC
+ _symbolic _____ 2os6LoggerV
+ _symbolic _____ySDySSypGG s23_ContiguousArrayStorageC
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____yyXlXpG s23_ContiguousArrayStorageC
+ _symbolic yXlSg
+ _symbolic ypSg
- -[WiFiAwareDataPathState initWithInterfaceName:interfaceAddr:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiInfos:preferredChannelNumbers:preferredChannelClasses:ndiSessionInfos:]
- -[WiFiAwareDiscoveryResult initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:pairedUUID:pairedDeviceName:signature:]
- -[WiFiAwareNDIInfo initWithNdiName:ndiAddr:sessionCount:security:qosType:]
- -[WiFiAwareRadioSchedule infraChannelClass]
- -[WiFiAwareRadioSchedule initWithInterfaceName:interfaceAddr:isEnabled:band24GHz:band5GHz:supportsDualBand:supportsSimultaneousDualBand:primaryChannel:secondaryChannel:infraChannel:preferredChannelsCount:preferredChannelNumbers:]
- -[WiFiAwareRadioSchedule init]
- -[WiFiAwareRadioSchedule preferredChannelClasses]
- -[WiFiAwareRadioSchedule preferredChannelNumbers]
- -[WiFiAwareRadioSchedule preferredChannelsCount]
- -[WiFiAwareRadioSchedule primaryChannelClass]
- -[WiFiAwareRadioSchedule secondaryChannelClass]
- -[WiFiAwareRadioSchedule setInterfaceAddr:]
- -[WiFiAwareRadioSchedule setInterfaceName:]
- -[WiFiAwareRadioSchedule setIsEnabled:]
- -[WiFiAwareState initWithInterfaceName:interfaceAddr:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:]
- -[WiFiAwareState init]
- GCC_except_table127
- GCC_except_table43
- _OBJC_IVAR_$_WiFiAwareDataPathState._interfaceAddr
- _OBJC_IVAR_$_WiFiAwareDataPathState._interfaceName
- _OBJC_IVAR_$_WiFiAwareDataPathState._isEnabled
- _OBJC_IVAR_$_WiFiAwareRadioSchedule._infraChannelClass
- _OBJC_IVAR_$_WiFiAwareRadioSchedule._interfaceAddr
- _OBJC_IVAR_$_WiFiAwareRadioSchedule._interfaceName
- _OBJC_IVAR_$_WiFiAwareRadioSchedule._isEnabled
- _OBJC_IVAR_$_WiFiAwareRadioSchedule._preferredChannelClasses
- _OBJC_IVAR_$_WiFiAwareRadioSchedule._preferredChannelNumbers
- _OBJC_IVAR_$_WiFiAwareRadioSchedule._preferredChannelsCount
- _OBJC_IVAR_$_WiFiAwareRadioSchedule._primaryChannelClass
- _OBJC_IVAR_$_WiFiAwareRadioSchedule._secondaryChannelClass
- _OBJC_IVAR_$_WiFiAwareState._interfaceAddr
- _OBJC_IVAR_$_WiFiAwareState._interfaceName
- _OBJC_IVAR_$_WiFiAwareState._isEnabled
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_WiFiAwareStateMonitorXPCDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiAwareStateMonitorXPCDelegate
- __OBJC_$_PROTOCOL_REFS_WiFiAwareStateMonitorXPCDelegate
- __OBJC_LABEL_PROTOCOL_$_WiFiAwareStateMonitorXPCDelegate
- __OBJC_PROTOCOL_$_WiFiAwareStateMonitorXPCDelegate
- __OBJC_PROTOCOL_REFERENCE_$_WiFiAwareStateMonitorXPCDelegate
- ___108-[WiFiAwarePublisher sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:]_block_invoke
- ___109-[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:]_block_invoke
- ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.118
- ___115-[WiFiAwareDataSession datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:]_block_invoke.121
- ___79-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:]_block_invoke.149
- ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke.163
- ___block_literal_global.105
- ___block_literal_global.108
- ___block_literal_global.117
- ___block_literal_global.178
- ___block_literal_global.180
- ___block_literal_global.182
- ___block_literal_global.184
- ___block_literal_global.186
- ___block_literal_global.224
- ___block_literal_global.276
- ___block_literal_global.280
- ___block_literal_global.283
- ___block_literal_global.376
- ___block_literal_global.529
- ___block_literal_global.53
- ___block_literal_global.618
- ___block_literal_global.620
- ___block_literal_global.622
- ___block_literal_global.88
- ___block_literal_global.90
- _objc_msgSend$decodeObjectForKey:
- _objc_msgSend$hasSuffix:
- _objc_msgSend$initWithInterfaceName:interfaceAddr:isEnabled:band24GHz:band5GHz:supportsDualBand:supportsSimultaneousDualBand:primaryChannel:secondaryChannel:infraChannel:preferredChannelsCount:preferredChannelNumbers:
- _objc_msgSend$initWithInterfaceName:interfaceAddr:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:
- _objc_msgSend$initWithInterfaceName:interfaceAddr:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiInfos:preferredChannelNumbers:preferredChannelClasses:ndiSessionInfos:
- _objc_msgSend$initWithNdiName:ndiAddr:sessionCount:security:qosType:
- _objc_msgSend$initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:pairedUUID:pairedDeviceName:signature:
- _objc_msgSend$preferredChannelsCount
CStrings:
+ "\n\t\t[%@] %@"
+ "\n\x1b[1mBand.Map%u UsgPref=%u RxNss=%u Util=%u, %@\x1b[0m"
+ "\n<peer %lu: %@%@"
+ "\n<peer %lu: %@, Cmt/Pot/Cnd/Bands=%lu/%lu/%lu/%lu"
+ "\nBand.Map%u UsgPref=%u RxNss=%u Util=%u, "
+ "\nBand.Map%u UsgPref=%u RxNss=%u Util=%u, %@"
+ "\nCmt.Map%u %@/%@ %@"
+ "\nCmt.Map%u %@/%u %@"
+ "\nCnd.Map%u %@/%@ %@"
+ "\nCnd.Map%u %@/%u %@"
+ "\nPot.Map%u %@/%@ %@"
+ "\nPot.Map%u %@/%u %@"
+ "\x1b[1m%lu\x1b[0m"
+ "\x1b[1m<no peer avail info>\x1b[0m"
+ "%@\n"
+ "%@ Requesting Connection"
+ "%@%@"
+ "%@: Activated pairing mode. Cross Transport Discovery ID: %@"
+ "%@: Activating pairing mode, Config: %@, delegate: %@"
+ "%@: Deactivated pairing mode"
+ "%@: Deactivating pairing mode"
+ "%@: Failed to activate pairing mode. Error: %ld"
+ "%@: Failed to deactivate pairing mode. Error: %ld"
+ "%@: New Pairing session from: %@"
+ "%@: New Pairing session from: %@, Subscriber Info: %@"
+ "%lu"
+ "%s: %@"
+ "%s: %@ Device Found"
+ "%s: %@ Paired Device Found"
+ "%s: %@ Timed out"
+ "%s: Starting TDS session with config: %@"
+ "%s: Starting connection with pairing role: %@, %@"
+ "%s: delegate=%@, error=%ld, %@"
+ "%s: discoveryResult=%@, %@"
+ "%s: error=%ld, %@"
+ "%s: publishID=%d, initiatorAddress=%@, %@"
+ "(null)"
+ ", Cmt/Pot/Cnd/Bands=%@/%@/%@/%@"
+ ", publishID=%d"
+ ", rejectionReason=%@"
+ "-[WiFiAwarePairingSession activateForPublishID:initiatorAddress:]"
+ "-[WiFiAwarePairingSession deactivate]"
+ "-[WiFiAwarePairingSession handleError:]"
+ "-[WiFiAwarePairingSession initWithPairingConfig:delegate:]"
+ "-[WiFiAwarePairingSession pairWithDiscoveryResult:]"
+ "-[WiFiAwarePairingSession pairingDidFailTo:error:]"
+ "-[WiFiAwarePairingSession pairingDidSucceedWithDeviceInfo:pairingStoreID:]"
+ "-[WiFiAwarePairingSession requiresPINDisplay:]"
+ "-[WiFiAwarePairingSession requiresPINInputWithCompletionHandler:]"
+ "-[WiFiAwarePairingSession requiresPassphraseDisplay:]"
+ "-[WiFiAwarePairingSession requiresPassphraseInputWithCompletionHandler:]"
+ "-[WiFiAwarePairingSession startConnectionUsingProxy:completionHandler:]"
+ "-[WiFiAwareTDSSession activate]"
+ "-[WiFiAwareTDSSession deactivate]"
+ "-[WiFiAwareTDSSession handleError:]"
+ "-[WiFiAwareTDSSession initWithTDSConfig:delegate:]"
+ "-[WiFiAwareTDSSession matchFound:transportState:]"
+ "-[WiFiAwareTDSSession pairedMatchFound:transportState:]"
+ "-[WiFiAwareTDSSession startConnectionUsingProxy:completionHandler:]"
+ "-[WiFiAwareTDSSession timedOut]"
+ "1"
+ "2.4Ghz"
+ "5Ghz"
+ "6GHz"
+ "6Ghz"
+ "<%@: %@"
+ "<%@: %@, Peers=%lu"
+ "<%@: %p> expiration=%@, bootstrappingRecordsCount=<%lu>"
+ "<%@: %p> ingested=%@%@"
+ "<%@: %p> name=%@, identifier=%@, bluetoothAddress=%@"
+ "<%@: %p> operation=%@, serviceName=%@, deviceFilter=%@"
+ "<%@: %p> pairingMode=%@, pairingMetadata=%@, pairSetupMode=%@, userID=%u"
+ "<%@: %p> recordsProcessed=%u, results=%@"
+ "<%@: %p> role=%@%@, pairingConfiguration=%@"
+ "<%@: %p> serviceType=%ld, internetSharingConfiguration=%@, userID=%u"
+ "<WiFiAwareChannelConfiguration: numbers=[%@], classes=[%@]>"
+ "<WiFiAwareDatapathConfiguration: discoveryResult=%@, serviceType=%s, passphrase=%@, pmk=%@, pmkID=%@, serviceSpecificInfo=%@, internetSharing=%@, pairingMethod=%s, pairingCaching=%s, pairSetupServiceSpecificInfo=%@>, connectionMode=%ld, pairingMetadata=%@, multicastConfiguration=%@, userID=%u"
+ "<WiFiAwareDiscoveryResult:\n\tname=%@\n\tserviceSpecificInfo=%@\n\tpublishID=%u\n\tpublisherAddress=%@\n\tdatapath=%s\n\tsecurity=%s\n\tcipherSuite=%s\n\tFSD=%s\n\trssi=%ld\n\tpairSetup=%s\n\tpairing=%@\n\tUUID=%@\n\tpairedDeviceName=%@\n\tSignature=0x%02lx [%ld]\n\tautoPairable=%s\n\tperformanceForecast=%@>"
+ "<WiFiAwareInterfaceInfo: %@, %@, %@>"
+ "<WiFiAwareNDISessionCounters: total=%u, established=%u, with24GOnly=%u, rtm=%u, rtmWith24GOnly=%u, rtmLowLatency=%u>"
+ "<WiFiAwarePeerDevice: instanceID=%u, macAddress=%@>"
+ "<WiFiAwarePublishConfiguration: serviceName=%@, serviceSpecificInfo=%@, furtherServiceDiscoveryRequired=%s, jumboMessages=%s, dataConfig=%@, fastDiscovery=%@, internetSharing=%@>, allowedDeviceIDs=%@, timeoutAfter=%ld, channelInfo=%@, cc=%@, multicastConfiguration=%@, pairingMetadata=%@, userID=%u>"
+ "<WiFiAwareSubscribeConfiguration: name=%@, serviceSpecificInfo=%@, fastDiscoveryConfiguration=%@, multicastAddress=%@, timeoutAfter=%ld>, allowedDeviceIDs=%@, channelInfo=%@, cc=%@, multicastConfiguration=%@>, discoveryMode=%ld, userID=%u"
+ "<no peer avail info>"
+ "A reference to something invalid was passed"
+ "ASK"
+ "Accessory Requesting Connection"
+ "AccessoryDisplayName"
+ "AccessoryWiFiPairedUUID"
+ "Airplay"
+ "AllPairedDevices"
+ "Already paired to peer"
+ "An accessory is requesting to connect to your Personal WLAN Hotspot. UUID: %@"
+ "An accessory is requesting to connect to your Personal Wi-Fi Hotspot. UUID: %@"
+ "AnyDevice"
+ "AskForConsent"
+ "AutoPair"
+ "AutoReply"
+ "Band.Map%u UsgPref=%u RxNss=%u Util=%u, "
+ "CLI"
+ "Cmt.Map%u %@/%u %@\n"
+ "Cnd.Map%u %@/%u %@\n"
+ "DDUI"
+ "Delegate does not implement pairingSession:requiresPINDisplay:"
+ "Delegate does not implement pairingSession:requiresPINInputWithCompletionHandler:"
+ "Delegate does not implement pairingSession:requiresPassphraseDisplay:"
+ "Delegate does not implement pairingSession:requiresPassphraseInputWithCompletionHandler:"
+ "Discovery result does not contain pairing SSI"
+ "Duplicate"
+ "Expired"
+ "Failed to deserialize keychain data: %s"
+ "Failed to request notification authorization: %{public}@"
+ "Failed to serialize object"
+ "Initiator"
+ "Internet sharing failure (deprecated)"
+ "Invalid Format"
+ "Invalid Signature"
+ "Invalid Timestamps"
+ "KeychainAgent"
+ "Map%u Bands=%@ UsagePref=%u RxNSS=%u Util=%u"
+ "Map%u Ch=%u %uMHz %@ Period=%uTU Off=%u Slots=%@ UsagePref=%u RxNSS=%u Util=%u"
+ "No more instance IDs were available to provide for this service"
+ "No paired devices found"
+ "Not Set"
+ "Notification authorization granted"
+ "Notification authorization not granted"
+ "Notification center not available"
+ "Notification center not configured, cannot add notification request"
+ "Notification center not configured, cannot remove notifications"
+ "Object to serialize is nil"
+ "PK Bootstrapping records are in an invalid format"
+ "PK Bootstrapping records have expired"
+ "Paired device store is unavailable"
+ "Pairing authentication failed"
+ "Pairing no pairing meta data was set"
+ "Pairing request rejected"
+ "Peer: %@\n"
+ "Permanent"
+ "Pin Code"
+ "Pot.Map%u %@/%u %@\n"
+ "Provide"
+ "Public Key Bootstrapping (Mutual)"
+ "Public Key Bootstrapping (OneWay)"
+ "Publisher does not contain pairing related attributes"
+ "Responder"
+ "Serialization failed: %s"
+ "Temporary"
+ "The XPC connection with the daemon was invalidated"
+ "The arguments passed to the daemon in the request were invalid"
+ "The daemon is unavailable on this system"
+ "The security parameters passed were invalid"
+ "The system did not have sufficient resources required to fulfill this request"
+ "UIAgent"
+ "UNMutableNotificationContent"
+ "UNNotificationIcon"
+ "UNNotificationRequest"
+ "UNNotificationSound"
+ "UNUserNotificationCenter"
+ "Unknown (%ld)"
+ "Unknown WiFi P2P error"
+ "Unknown or unsupported result type: %lu"
+ "Unknown(%ld)"
+ "Unsupported result type: %lu"
+ "User %@ notification for %@ with identifier %@"
+ "UserNotifications framework not available, skipping infrastructure disconnect notification for %{public}@"
+ "UserNotifications framework not available, skipping notification center configuration"
+ "UserNotifications not available"
+ "WiFiAwareDataRequest.skipInfrastructureRelayCheck"
+ "WiFiAwareDataRequest.userID"
+ "WiFiAwareDataSessionConfig.internetSharingConfiguration"
+ "WiFiAwareDataSessionConfig.serviceType"
+ "WiFiAwareDataSessionConfig.userID"
+ "WiFiAwareDiscoveryResult.autoPairable"
+ "WiFiAwareDiscoveryResult.performanceForecast"
+ "WiFiAwarePKBootstrappingRecordIngestionResult.ingested"
+ "WiFiAwarePKBootstrappingRecordIngestionResult.rejectionReason"
+ "WiFiAwarePKBootstrappingRecords.bootstrappingRecords"
+ "WiFiAwarePKBootstrappingRecords.expiration"
+ "WiFiAwarePKBootstrappingRecordsIngestionReport.ingestionResults"
+ "WiFiAwarePKBootstrappingRecordsIngestionReport.recordsProcessed"
+ "WiFiAwarePairingConfig.pairingMetadata"
+ "WiFiAwarePairingConfig.pairingMode"
+ "WiFiAwarePairingConfig.pairingSetupMode"
+ "WiFiAwarePairingConfig.userID"
+ "WiFiAwarePairingMetadata(bundleID: %@, selfPairingName: %@, peerDeviceName: %@, storageClass: %@, lifetime: %.2f, pairingClient: %@)"
+ "WiFiAwarePairingMetadata.bundleID"
+ "WiFiAwarePairingSession"
+ "WiFiAwarePerformanceForecast.localInfrastructureThroughputCapacityRatio"
+ "WiFiAwarePerformanceForecast.localThroughputCapacity"
+ "WiFiAwarePerformanceForecast.localThroughputCapacityRatio"
+ "WiFiAwarePerformanceForecast.localThroughputCeiling"
+ "WiFiAwarePerformanceForecast.localTimestamp"
+ "WiFiAwarePerformanceForecast.signalStrength"
+ "WiFiAwarePerformanceForecast.timestamp"
+ "WiFiAwarePerformanceForecast.unavailabilityLatencyCeiling"
+ "WiFiAwarePerformanceForecast:\n \tTimestamp: %@\n \tLocalTimestamp: %@\n \tSignal Strength: %@\n \tLocal Throughput Ceiling: %@ Mbps\n \tLocal Throughput Capacity: %@ Mbps\n \tLocal Throughput Capacity Ratio: %@\n \tLocal Infra Throughput Capacity Ratio: %@\n \tUnavailability Latency Ceiling: %@"
+ "WiFiAwarePublishConfiguration.userID"
+ "WiFiAwareSubscribeConfiguration.multicastConfiguration"
+ "WiFiAwareSubscribeConfiguration.userID"
+ "WiFiAwareTDSConfig.deviceFilter"
+ "WiFiAwareTDSConfig.operation"
+ "WiFiAwareTDSConfig.serviceName"
+ "WiFiAwareTDSDevice.bluetoothAddress"
+ "WiFiAwareTDSDevice.identifier"
+ "WiFiAwareTDSDevice.name"
+ "WiFiAwareTDSSession"
+ "[ADD] %@"
+ "[ADD] Query: %@, Status: %d"
+ "[DELETE] %@"
+ "[DELETE] Query: %@, Status: %d"
+ "[GET] %@"
+ "[GET] Failed to serialize keychain results"
+ "[GET] Query: %@, Status: %d, Result: %s"
+ "[GET] Results: %@, Type: %ld (%@)"
+ "[UPDATE] %@ -> %@"
+ "[UPDATE] Query: %@, Status: %d, Updates: %@"
+ "action"
+ "bands"
+ "com.apple.wifip2p"
+ "com.apple.wifip2p.WiFiAwarePKRecordsStore"
+ "com.apple.wifip2p.WiFiAwarePairing"
+ "com.apple.wifip2p.WiFiAwareTDS"
+ "com.apple.wifip2p.WiFiP2PKeychainAgent"
+ "com.apple.wifip2p.WiFiP2PNANStateMonitor"
+ "committedEntries"
+ "conditionalEntries"
+ "dismissed"
+ "instanceID"
+ "interfaceInfo"
+ "mapId"
+ "offset"
+ "peer.%@.band.map%u"
+ "peerInfos"
+ "peers"
+ "potentialBandEntries"
+ "potentialChannelEntries"
+ "preferredChannels"
+ "q24@?0@\"WiFiAwarePeerAvailChannelEntry\"8@\"WiFiAwarePeerAvailChannelEntry\"16"
+ "rxNSS"
+ "tapped"
+ "timeSyncCalibration"
+ "usagePreference"
+ "utilization"
+ "uuid"
+ "v16@?0@\"<WiFiAwarePKRecordsXPC>\"8"
+ "v16@?0@\"<WiFiAwarePairingXPC>\"8"
+ "v16@?0@\"WiFiAwarePeerAvailInfo\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v32@?0@\"NSNumber\"8@\"WiFiAwarePerformanceForecast\"16^B24"
+ "wifip2p.nanphproxcard"
+ "wifip2p.notificationResponse"
+ "\xe1Q"
- "\f"
- "#16@0:8"
- ".cxx_destruct"
- "<WiFiAwareDatapathConfiguration: discoveryResult=%@, serviceType=%s, passphrase=%@, pmk=%@, pmkID=%@, serviceSpecificInfo=%@, internetSharing=%@, pairingMethod=%s, pairingCaching=%s, pairSetupServiceSpecificInfo=%@>, connectionMode=%ld, pairingMetadata=%@, multicastConfiguration=%@"
- "<WiFiAwareDiscoveryResult: name=%@, serviceSpecificInfo=%@, publishID=%u, publisherAddress=%@, datapath=%s, security=%s, cipherSuite=%s, FSD=%s, rssi=%ld, pairSetup=%s, pairing=%@, UUID=%@>, pairedDeviceName=%@ Signature=0x%02lx [%ld]"
- "<WiFiAwarePublishConfiguration: serviceName=%@, serviceSpecificInfo=%@, furtherServiceDiscoveryRequired=%s, jumboMessages=%s, dataConfig=%@, fastDiscovery=%@, internetSharing=%@>, allowedDeviceIDs=%@, timeoutAfter=%ld, channelInfo=%@, cc=%@, multicastConfiguration=%@, pairingMetadata=%@>"
- "<WiFiAwareSubscribeConfiguration: name=%@, serviceSpecificInfo=%@, fastDiscoveryConfiguration=%@, multicastAddress=%@, timeoutAfter=%ld>, allowedDeviceIDs=%@, channelInfo=%@, cc=%@, multicastConfiguration=%@>, discoveryMode=%ld"
- "@"
- "@\"<WiFiAwareDataSessionDelegate>\""
- "@\"<WiFiAwareDataSessionPairingDelegate>\""
- "@\"<WiFiAwareDevicesStoreDelegate>\""
- "@\"<WiFiAwarePublisherDelegate>\""
- "@\"<WiFiAwarePublisherPairingDelegate>\""
- "@\"<WiFiAwareStateMonitorXPCDelegate>\""
- "@\"<WiFiAwareSubscriberDelegate>\""
- "@\"<WiFiP2PXPCConnectionDelegate>\""
- "@\"NSArray\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSLock\""
- "@\"NSMutableArray\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_source>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\""
- "@\"NSXPCConnection\""
- "@\"NSXPCInterface\"16@0:8"
- "@\"UNUserNotificationCenter\""
- "@\"WiFiAwareBandSchedule\""
- "@\"WiFiAwareDiscoveryResult\""
- "@\"WiFiAwareFastDiscoveryConfiguration\""
- "@\"WiFiAwareInternetSharingConfiguration\""
- "@\"WiFiAwareMulticastConfiguration\""
- "@\"WiFiAwarePairingConfiguration\""
- "@\"WiFiAwarePairingMetadata\""
- "@\"WiFiAwarePublishConfiguration\""
- "@\"WiFiAwarePublishDatapathConfiguration\""
- "@\"WiFiAwarePublishDatapathSecurityConfiguration\""
- "@\"WiFiAwarePublishDatapathServiceSpecificInfo\""
- "@\"WiFiAwarePublishServiceSpecificInfo\""
- "@\"WiFiAwareRadioSchedule\""
- "@\"WiFiAwareSrvInfo\""
- "@\"WiFiAwareSubscribeConfiguration\""
- "@\"WiFiChannel\""
- "@\"WiFiMACAddress\""
- "@\"WiFiP2PXPCConnection\""
- "@112@0:8@16@24C32C36@40B48q52q60q68B76@80@88@96q104"
- "@116@0:8@16q24@32@40@48@56@64q72B80@84q92@100@108"
- "@144@0:8@16@24B32B36Q40q48@56q64q72@80q88q96@104q112q120q128Q136"
- "@16@0:8"
- "@20@0:8C16"
- "@20@0:8I16"
- "@22@0:8{ether_addr=[6C]}16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8@16B24"
- "@28@0:8B16@?20"
- "@28@0:8C16@20"
- "@28@0:8q16S24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16B24B28"
- "@32@0:8@16Q24"
- "@32@0:8@16q24"
- "@32@0:8^{__CFDictionary=}16^B24"
- "@32@0:8q16@24"
- "@32@0:8{in6_addr=(?=[16C][8S][4I])}16"
- "@332@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128B136@140@148@156@164@172@180@188@196@204@212@220@228@236@244@252@260@268@276@284@292@300@308@316@324"
- "@36@0:8@16@24B32"
- "@36@0:8@16B24q28"
- "@36@0:8@16Q24B32"
- "@36@0:8C16q20@28"
- "@38@0:8{ether_addr=[6C]}16{in6_addr=(?=[16C][8S][4I])}22"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16Q24@32"
- "@40@0:8@16q24@32"
- "@40@0:8@16{in6_addr=(?=[16C][8S][4I])}24"
- "@40@0:8I16I20I24I28@32"
- "@40@0:8Q16@24q32"
- "@40@0:8Q16^@24@?32"
- "@40@0:8d16d24d32"
- "@40@0:8q16@24q32"
- "@44@0:8@16@24I32C36I40"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16q24@32@40"
- "@48@0:8I16q20B28B32B36B40B44"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16@24B32I36I40I44@48"
- "@56@0:8@16q24@32@40@48"
- "@56@0:8C16Q20@28@36@44I52"
- "@56@0:8Q16@24@32^@40@?48"
- "@64@0:8@16@24@32q40d48q56"
- "@64@0:8@16q24@32@40@48@56"
- "@64@0:8C16Q20C28@32@40@48Q56"
- "@72@0:8@16@24@32@40@48@56d64"
- "@80@0:8@16B24B28@32B40I44@48@56@64@72"
- "@92@0:8@16@24B32I36I40I44I48I52I56@60@68@76@84"
- "@96@0:8@16@24@32@40B48C52@56q64q72q80q88"
- "@96@0:8@16@24B32@36@44B52B56@60@68@76I84@88"
- "@?"
- "@?16@0:8"
- "AWDLServiceDiscoveryConfiguration"
- "AWDLServiceDiscoveryManager"
- "AWDLServiceDiscoveryManagerXPC"
- "AWDLServiceDiscoveryManagerXPCDelegate"
- "AWDLTrafficRegistrationConfiguration"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8@?16"
- "B24@0:8^@16"
- "B32@0:8@16^@24"
- "B32@0:8^@16^@24"
- "B40@0:8@16@?24^@32"
- "B40@0:8@?16@?24^@32"
- "B40@0:8Q16^@24@?32"
- "B40@0:8^@16^@24^@32"
- "BoldFormatting"
- "C"
- "C16@0:8"
- "DetailedDescription"
- "F"
- "I"
- "I16@0:8"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "Q64@0:8@16@24q32d40q48^@56"
- "S"
- "S16@0:8"
- "T#,R"
- "T@\"<WiFiAwareDataSessionDelegate>\",W,N,V_delegate"
- "T@\"<WiFiAwareDataSessionPairingDelegate>\",W,N,V_pairingDelegate"
- "T@\"<WiFiAwareDevicesStoreDelegate>\",W,N,V_delegate"
- "T@\"<WiFiAwarePublisherDelegate>\",W,N,V_delegate"
- "T@\"<WiFiAwarePublisherPairingDelegate>\",W,N,V_pairingDelegate"
- "T@\"<WiFiAwareSubscriberDelegate>\",W,N,V_delegate"
- "T@\"<WiFiP2PXPCConnectionDelegate>\",W,V_delegate"
- "T@\"NSArray\",&,N,V_lastDataPathStateChangedOptions"
- "T@\"NSArray\",&,N,V_lastRadioScheduleChangedOptions"
- "T@\"NSArray\",&,N,V_lastSrvInfoChangedOptions"
- "T@\"NSArray\",&,N,V_lastStateChangedOptions"
- "T@\"NSArray\",C,N,V_rxFWDelayHistogram"
- "T@\"NSArray\",C,N,V_rxIPCDelayHistogram"
- "T@\"NSArray\",C,N,V_rxRSSIHistogram"
- "T@\"NSArray\",C,N,V_servicesRequiringAvailabilityNotification"
- "T@\"NSArray\",C,N,V_supportedPairSetupMethods"
- "T@\"NSArray\",C,N,V_txCCAHistogram"
- "T@\"NSArray\",C,N,V_txConsecutiveErrorsHistogram"
- "T@\"NSArray\",C,N,V_txPacketExpiryHistogram"
- "T@\"NSArray\",R,N,V_channelSequence"
- "T@\"NSArray\",R,N,V_channels"
- "T@\"NSArray\",R,N,V_ndiInfos"
- "T@\"NSArray\",R,N,V_ndiSessionInfos"
- "T@\"NSArray\",R,N,V_passphraseList"
- "T@\"NSArray\",R,N,V_pmkList"
- "T@\"NSArray\",R,N,V_preferredChannelClasses"
- "T@\"NSArray\",R,N,V_preferredChannelNumbers"
- "T@\"NSArray\",R,N,V_srvSessionInfos"
- "T@\"NSArray\",R,N,V_supportedCipherSuites"
- "T@\"NSData\",C,N,V_blob"
- "T@\"NSData\",C,N,V_gtkKey"
- "T@\"NSData\",C,N,V_igtkKey"
- "T@\"NSData\",C,N,V_keyBlob"
- "T@\"NSData\",C,N,V_serviceSpecificInfo"
- "T@\"NSData\",C,N,V_txtRecordData"
- "T@\"NSData\",R,N,V_localTimestamp"
- "T@\"NSData\",R,N,V_pairingNFCTag"
- "T@\"NSData\",R,N,V_pairingQRCodeInformation"
- "T@\"NSData\",R,N,V_pmk"
- "T@\"NSData\",R,N,V_pmkID"
- "T@\"NSData\",R,N,V_serviceKey"
- "T@\"NSData\",R,N,V_serviceValue"
- "T@\"NSData\",R,N,V_srvHash"
- "T@\"NSData\",R,N,V_timeBitmap"
- "T@\"NSData\",R,V_data"
- "T@\"NSData\",R,V_ipv6LinkLocalAddress"
- "T@\"NSDate\",R,N,V_timestamp"
- "T@\"NSDictionary\",R,C,N,V_attributes"
- "T@\"NSDictionary\",R,N,V_txLatency"
- "T@\"NSNumber\",C,N,V_channelSequenceMismatchOn2GCount"
- "T@\"NSNumber\",C,N,V_channelSequenceMismatchOn5GCount"
- "T@\"NSNumber\",C,N,V_csaCount"
- "T@\"NSNumber\",C,N,V_dfsChannelsCount"
- "T@\"NSNumber\",C,N,V_infraAssocCount"
- "T@\"NSNumber\",C,N,V_infraDisassocCount"
- "T@\"NSNumber\",C,N,V_infraRelayRequestersCount"
- "T@\"NSNumber\",C,N,V_infraScanCount"
- "T@\"NSNumber\",C,N,V_instantCommunicationChannel"
- "T@\"NSNumber\",C,N,V_packetsHOFOn2GCount"
- "T@\"NSNumber\",C,N,V_packetsNAVOn2GCount"
- "T@\"NSNumber\",C,N,V_packetsOn2GCount"
- "T@\"NSNumber\",C,N,V_packetsOn5GCount"
- "T@\"NSNumber\",C,N,V_packetsOverridenOn5GCount"
- "T@\"NSNumber\",C,N,V_preferred2GChannelsCount"
- "T@\"NSNumber\",C,N,V_preferred5GChannelsCount"
- "T@\"NSNumber\",C,N,V_quietIECount"
- "T@\"NSNumber\",C,N,V_rtpSequenceNumber"
- "T@\"NSNumber\",C,N,V_rtpStartTime"
- "T@\"NSNumber\",C,N,V_txChipModeErrorCount"
- "T@\"NSNumber\",C,N,V_txDroppedCount"
- "T@\"NSNumber\",C,N,V_txErrorCount"
- "T@\"NSNumber\",C,N,V_txExpiredCount"
- "T@\"NSNumber\",C,N,V_txFailedCount"
- "T@\"NSNumber\",C,N,V_txFirmwareFreePacketCount"
- "T@\"NSNumber\",C,N,V_txForceLifetimeExpiredCount"
- "T@\"NSNumber\",C,N,V_txIOErrorCount"
- "T@\"NSNumber\",C,N,V_txInternalErrorCount"
- "T@\"NSNumber\",C,N,V_txMaxRetriesCount"
- "T@\"NSNumber\",C,N,V_txMemoryErrorCount"
- "T@\"NSNumber\",C,N,V_txNoACKCount"
- "T@\"NSNumber\",C,N,V_txNoRemotePeerCount"
- "T@\"NSNumber\",C,N,V_txNoResourcesCount"
- "T@\"NSNumber\",R,N,V_infraChannel"
- "T@\"NSNumber\",R,N,V_infraChannelClass"
- "T@\"NSNumber\",R,N,V_infrastructureChannel"
- "T@\"NSNumber\",R,N,V_operatingChannel"
- "T@\"NSNumber\",R,N,V_operatingClass"
- "T@\"NSNumber\",R,N,V_primaryChannel"
- "T@\"NSNumber\",R,N,V_primaryChannelClass"
- "T@\"NSNumber\",R,N,V_secondaryChannel"
- "T@\"NSNumber\",R,N,V_secondaryChannelClass"
- "T@\"NSNumber\",R,N,V_signalStrength"
- "T@\"NSNumber\",R,N,V_throughputCapacityMbps"
- "T@\"NSNumber\",R,N,V_throughputCeilingMbps"
- "T@\"NSSet\",C,N,V_allowedDeviceIDs"
- "T@\"NSSet\",R,N,V_supportedFeatures"
- "T@\"NSString\",&,N,V_interfaceName"
- "T@\"NSString\",&,N,V_pinCode"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_bundleID"
- "T@\"NSString\",C,N,V_countryCode"
- "T@\"NSString\",C,N,V_hostname"
- "T@\"NSString\",C,N,V_instanceName"
- "T@\"NSString\",C,N,V_interfaceName"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_peerDeviceName"
- "T@\"NSString\",C,N,V_pinCode"
- "T@\"NSString\",C,N,V_selfPairingName"
- "T@\"NSString\",C,N,V_uniqueIdentifier"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N,V_modelName"
- "T@\"NSString\",R,C,N,V_pairingName"
- "T@\"NSString\",R,C,N,V_vendorName"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_countryCode"
- "T@\"NSString\",R,N,V_discoveryInterfaceName"
- "T@\"NSString\",R,N,V_interfaceName"
- "T@\"NSString\",R,N,V_ndiName"
- "T@\"NSString\",R,N,V_pairedDeviceName"
- "T@\"NSString\",R,N,V_pairingPINCode"
- "T@\"NSString\",R,N,V_pairingPassphrase"
- "T@\"NSString\",R,N,V_passphrase"
- "T@\"NSString\",R,N,V_service"
- "T@\"NSString\",R,N,V_serviceName"
- "T@\"NSString\",R,N,V_srvName"
- "T@\"NSUUID\",R,N,V_pairedUUID"
- "T@\"WiFiAwareBandSchedule\",R,N,V_band24GHz"
- "T@\"WiFiAwareBandSchedule\",R,N,V_band5GHz"
- "T@\"WiFiAwareDiscoveryResult\",R,N,V_discoveryResult"
- "T@\"WiFiAwareFastDiscoveryConfiguration\",C,N,V_fastDiscoveryConfiguration"
- "T@\"WiFiAwareInternetSharingConfiguration\",C,N,V_internetSharingConfiguration"
- "T@\"WiFiAwareMulticastConfiguration\",C,N,V_multicastConfiguration"
- "T@\"WiFiAwarePairingConfiguration\",C,N,V_pairingConfiguration"
- "T@\"WiFiAwarePairingConfiguration\",R,N,V_pairingConfiguration"
- "T@\"WiFiAwarePairingMetadata\",C,N,V_pairingMetadata"
- "T@\"WiFiAwarePublishConfiguration\",R,N,V_configuration"
- "T@\"WiFiAwarePublishDatapathConfiguration\",C,N,V_datapathConfiguration"
- "T@\"WiFiAwarePublishDatapathSecurityConfiguration\",&,N,V_securityConfiguration"
- "T@\"WiFiAwarePublishDatapathServiceSpecificInfo\",C,N,V_serviceSpecificInfo"
- "T@\"WiFiAwarePublishDatapathServiceSpecificInfo\",R,N,V_serviceSpecificInfo"
- "T@\"WiFiAwarePublishServiceSpecificInfo\",C,N,V_pairSetupServiceSpecificInfo"
- "T@\"WiFiAwarePublishServiceSpecificInfo\",C,N,V_serviceSpecificInfo"
- "T@\"WiFiAwarePublishServiceSpecificInfo\",R,N,V_serviceSpecificInfo"
- "T@\"WiFiAwarePublishServiceSpecificInfo\",R,V_pairSetupServiceSpecificInfo"
- "T@\"WiFiAwareRadioSchedule\",&,N,V_lastRadioSchedule"
- "T@\"WiFiAwareSrvInfo\",&,N,V_lastSrvInfo"
- "T@\"WiFiAwareSubscribeConfiguration\",R,N,V_configuration"
- "T@\"WiFiChannel\",C,N,V_channelInfo"
- "T@\"WiFiChannel\",R,N,V_peerMasterChannel"
- "T@\"WiFiChannel\",R,N,V_peerPrimaryPreferredChannel"
- "T@\"WiFiChannel\",R,N,V_peerSecondaryPreferredChannel"
- "T@\"WiFiMACAddress\",C,N,V_interfaceAddr"
- "T@\"WiFiMACAddress\",C,N,V_multicastAddress"
- "T@\"WiFiMACAddress\",C,N,V_peerAddress"
- "T@\"WiFiMACAddress\",R,N"
- "T@\"WiFiMACAddress\",R,N,V_anchorMaster"
- "T@\"WiFiMACAddress\",R,N,V_clusterId"
- "T@\"WiFiMACAddress\",R,N,V_immediateMaster"
- "T@\"WiFiMACAddress\",R,N,V_initiatorDataAddress"
- "T@\"WiFiMACAddress\",R,N,V_interfaceAddr"
- "T@\"WiFiMACAddress\",R,N,V_macAddress"
- "T@\"WiFiMACAddress\",R,N,V_ndiAddr"
- "T@\"WiFiMACAddress\",R,N,V_peerAddress"
- "T@\"WiFiMACAddress\",R,N,V_peerDataAddress"
- "T@\"WiFiMACAddress\",R,N,V_peerNmiMacAddress"
- "T@\"WiFiMACAddress\",R,N,V_publisherAddress"
- "T@,W,N,V_exportedObject"
- "T@?,C,N,V_availUpdatedHandler"
- "T@?,C,N,V_channelSequenceUpdatedEventHandler"
- "T@?,C,N,V_dpStateUpdatedHandler"
- "T@?,C,N,V_invalidationHandler"
- "T@?,C,N,V_lowLatencyStatisticsUpdatedHandler"
- "T@?,C,N,V_realtimeModeUpdatedHandler"
- "T@?,C,N,V_serviceAvailabilityUpdatedHandler"
- "T@?,C,N,V_setCountryCodeHandler"
- "T@?,C,N,V_softAPChannelChangedEventHandler"
- "T@?,C,N,V_srvInfoUpdatedHandler"
- "T@?,C,N,V_stateUpdatedHandler"
- "T@?,C,N,V_statisticsUpdatedHandler"
- "T@?,C,N,V_threadCoexistenceEventHandler"
- "TB,N,V_activeFlagOverride"
- "TB,N,V_automatic"
- "TB,N,V_dynamicLinkRate"
- "TB,N,V_furtherServiceDiscoveryRequired"
- "TB,N,V_infraRelayOperationStatus"
- "TB,N,V_isEnabled"
- "TB,N,V_jumboServiceDiscoveryMessages"
- "TB,N,V_legacyUpgradeRequired"
- "TB,N,V_pairingCachingEnabled"
- "TB,N,V_provider"
- "TB,N,V_showsUIAlertOnError"
- "TB,N,V_useBridging"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_datapathSupported"
- "TB,R,N,V_extensionChannelAbove"
- "TB,R,N,V_is2_4GHz"
- "TB,R,N,V_is5GHz"
- "TB,R,N,V_is6GHz"
- "TB,R,N,V_isDFS"
- "TB,R,N,V_isEnabled"
- "TB,R,N,V_isFWElection"
- "TB,R,N,V_isResolve"
- "TB,R,N,V_pairSetupRequired"
- "TB,R,N,V_supportsDataTransfer"
- "TB,R,N,V_supportsDualBand"
- "TB,R,N,V_supportsSimultaneousDualBand"
- "TB,R,N,V_supportsSoloMode"
- "TB,V_pairingCachingEnabled"
- "TC,N,V_peerBandInformation"
- "TC,R,N,V_datapathID"
- "TC,R,N,V_dpId"
- "TC,R,N,V_publishID"
- "TC,R,N,V_security"
- "TC,R,N,V_serviceId"
- "TC,R,N,V_srvId"
- "TC,R,N,V_supportedBands"
- "TI,R,N,V_band"
- "TI,R,N,V_bandwidth"
- "TI,R,N,V_channel"
- "TI,R,N,V_channelNumber"
- "TI,R,N,V_establishedSessionCounter"
- "TI,R,N,V_localInterfaceIndex"
- "TI,R,N,V_numofPeers"
- "TI,R,N,V_period"
- "TI,R,N,V_preferredChannelsCount"
- "TI,R,N,V_publishServiceCount"
- "TI,R,N,V_qosType"
- "TI,R,N,V_rtmLowLatencySessionRefCount"
- "TI,R,N,V_rtmSessionRefCount"
- "TI,R,N,V_rtmSessionWith24GOnlyCount"
- "TI,R,N,V_sessionCount"
- "TI,R,N,V_sessionWith24GOnlyPeerCount"
- "TI,R,N,V_srvSessionCount"
- "TI,R,N,V_subscribeServiceCount"
- "TI,R,N,V_substate"
- "TI,R,N,V_totalSessionCounter"
- "TQ,N,V_deviceID"
- "TQ,N,V_options"
- "TQ,N,V_timeoutAfterSeconds"
- "TQ,R"
- "TQ,R,N,V_dpRole"
- "TQ,R,N,V_nanRole"
- "TQ,R,N,V_sessionState"
- "TQ,R,N,V_srvType"
- "TQ,R,N,V_tsf"
- "TS,N,V_preferredChannel"
- "TS,N,V_secondaryPreferredChannel"
- "TS,R,N,V_servicePort"
- "Td,N,V_lifetime"
- "Td,N,V_value"
- "Td,R,N,V_binEnd"
- "Td,R,N,V_binStart"
- "Td,R,N,V_durationActive"
- "Tq,N,V_authenticationType"
- "Tq,N,V_connectionMode"
- "Tq,N,V_discoveryMode"
- "Tq,N,V_keyExchangeOverMedium"
- "Tq,N,V_options"
- "Tq,N,V_pairingClient"
- "Tq,N,V_pairingMethod"
- "Tq,N,V_pairingSetupMode"
- "Tq,N,V_storageClass"
- "Tq,R,N"
- "Tq,R,N,V_ambtt"
- "Tq,R,N,V_anchorMasterRankM"
- "Tq,R,N,V_anchorMasterRankR"
- "Tq,R,N,V_bandwidth"
- "Tq,R,N,V_hopCount"
- "Tq,R,N,V_immediateMasterRankM"
- "Tq,R,N,V_immediateMasterRankR"
- "Tq,R,N,V_maxDatapaths"
- "Tq,R,N,V_maxPeers"
- "Tq,R,N,V_maxPublishers"
- "Tq,R,N,V_maxSubscribers"
- "Tq,R,N,V_protocolType"
- "Tq,R,N,V_rssi"
- "Tq,R,N,V_selfRankM"
- "Tq,R,N,V_selfRankR"
- "Tq,R,N,V_serviceType"
- "Tq,R,N,V_signature"
- "Tq,V_pairingMethod"
- "UNUserNotificationCenterDelegate"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "WiFiAwareBandSchedule"
- "WiFiAwareChannelSchedule"
- "WiFiAwareDataPathSessionInfo"
- "WiFiAwareDataPathState"
- "WiFiAwareDataSession"
- "WiFiAwareDataSessionIssueReport"
- "WiFiAwareDataSessionStatisticsHistogramBin"
- "WiFiAwareDataSessionStatisticsReport"
- "WiFiAwareDatapathConfiguration"
- "WiFiAwareDatapathInfo"
- "WiFiAwareDatapathInfoXPC"
- "WiFiAwareDatapathPerformanceReport"
- "WiFiAwareDatapathXPC"
- "WiFiAwareDatapathXPCDelegate"
- "WiFiAwareDeviceCapabilities"
- "WiFiAwareDevicesStore"
- "WiFiAwareDiscoveryResult"
- "WiFiAwareFastDiscoveryConfiguration"
- "WiFiAwareInternetSharingConfiguration"
- "WiFiAwareMulticastConfiguration"
- "WiFiAwareNDIInfo"
- "WiFiAwarePairedDeviceInfo"
- "WiFiAwarePairedDevicesXPC"
- "WiFiAwarePairedDevicesXPCDelegate"
- "WiFiAwarePairingConfiguration"
- "WiFiAwarePairingInfo"
- "WiFiAwarePairingMetadata"
- "WiFiAwarePairingMetadata(bundleID: %@, selfPairingName: %@, peerDeviceName: %@)"
- "WiFiAwarePairingMetadata.bundldeID"
- "WiFiAwarePublishConfiguration"
- "WiFiAwarePublishDatapathConfiguration"
- "WiFiAwarePublishDatapathSecurityConfiguration"
- "WiFiAwarePublishDatapathServiceSpecificInfo"
- "WiFiAwarePublishServiceSpecificInfo"
- "WiFiAwarePublisher"
- "WiFiAwarePublisherDataSessionHandle"
- "WiFiAwarePublisherXPC"
- "WiFiAwarePublisherXPCDelegate"
- "WiFiAwareRadioSchedule"
- "WiFiAwareSrvInfo"
- "WiFiAwareSrvSessionInfo"
- "WiFiAwareState"
- "WiFiAwareStateMonitor"
- "WiFiAwareStateMonitorConfiguration"
- "WiFiAwareStateMonitorXPCDelegate"
- "WiFiAwareSubscribeConfiguration"
- "WiFiAwareSubscriber"
- "WiFiAwareSubscriberXPC"
- "WiFiAwareSubscriberXPCDelegate"
- "WiFiChannel"
- "WiFiMACAddress"
- "WiFiP2PAWDLState"
- "WiFiP2PAWDLStateMonitor"
- "WiFiP2PAWDLStateMonitorConfiguration"
- "WiFiP2PAWDLStateMonitorXPCDelegate"
- "WiFiP2PDNSServiceDiscoveryManager"
- "WiFiP2PDNSServiceDiscoveryXPC"
- "WiFiP2PDNSServiceDiscoveryXPCDelegate"
- "WiFiP2PSPITransactionRequestor"
- "WiFiP2PSPITransactionResponderXPC"
- "WiFiP2PTrafficRegistrationReservation"
- "WiFiP2PUIAgent"
- "WiFiP2PUIAgentXPCDelegate"
- "WiFiP2PXPCConnection"
- "WiFiP2PXPCConnectionDelegate"
- "WiFiP2PXPCExportedObjectProxy"
- "WiFiP2PXPCListenerProtocol"
- "WiFiP2PXPCProtocol"
- "WiFiRemoteClientCountryCodeMonitor"
- "WiFiRemoteClientCountryCodeMonitorXPCDelegate"
- "^{_NSZone=}16@0:8"
- "_activeFlagOverride"
- "_activeTrafficRegistrations"
- "_allowedDeviceIDs"
- "_ambtt"
- "_anchorMaster"
- "_anchorMasterRankM"
- "_anchorMasterRankR"
- "_attemptedReconnect"
- "_attributes"
- "_authenticationType"
- "_automatic"
- "_availUpdatedHandler"
- "_band"
- "_band24GHz"
- "_band5GHz"
- "_bandwidth"
- "_binEnd"
- "_binStart"
- "_blob"
- "_bundleID"
- "_channel"
- "_channelInfo"
- "_channelNumber"
- "_channelSequence"
- "_channelSequenceMismatchOn2GCount"
- "_channelSequenceMismatchOn5GCount"
- "_channelSequenceUpdatedEventHandler"
- "_channels"
- "_clusterId"
- "_configuration"
- "_connection"
- "_connectionMode"
- "_countryCode"
- "_csaCount"
- "_data"
- "_dataSessionHandles"
- "_datapathCipherSuite"
- "_datapathConfiguration"
- "_datapathID"
- "_datapathSupported"
- "_delegate"
- "_derivedLocalization"
- "_destroyConnection"
- "_deviceID"
- "_dfsChannelsCount"
- "_discoveryInterfaceName"
- "_discoveryMode"
- "_discoveryResult"
- "_dpId"
- "_dpRole"
- "_dpStateUpdatedHandler"
- "_durationActive"
- "_dynamicLinkRate"
- "_enabledCount"
- "_endpointType"
- "_establishedSessionCounter"
- "_exportedObject"
- "_exportedObjectClass"
- "_extensionChannelAbove"
- "_fastDiscoveryConfiguration"
- "_fsdFunction"
- "_furtherServiceDiscoveryRequired"
- "_gtkKey"
- "_hopCount"
- "_hostname"
- "_igtkKey"
- "_immediateMaster"
- "_immediateMasterRankM"
- "_immediateMasterRankR"
- "_infraAssocCount"
- "_infraChannel"
- "_infraChannelClass"
- "_infraDisassocCount"
- "_infraRelayOperationStatus"
- "_infraRelayRequestersCount"
- "_infraScanCount"
- "_infrastructureChannel"
- "_initiatorDataAddress"
- "_instanceName"
- "_instantCommunicationChannel"
- "_interestedUniqueIdentifiers"
- "_interfaceAddr"
- "_interfaceName"
- "_internetSharingConfiguration"
- "_internetSharingPolicy"
- "_invalidationHandler"
- "_ipv6LinkLocalAddress"
- "_is2_4GHz"
- "_is5GHz"
- "_is6GHz"
- "_isDFS"
- "_isEnabled"
- "_isFWElection"
- "_isResolve"
- "_jumboServiceDiscoveryMessages"
- "_keyBlob"
- "_keyExchangeOverMedium"
- "_lastDataPathStateChangedOptions"
- "_lastRadioSchedule"
- "_lastRadioScheduleChangedOptions"
- "_lastSrvInfo"
- "_lastSrvInfoChangedOptions"
- "_lastStateChangedOptions"
- "_legacyUpgradeRequired"
- "_lifetime"
- "_localInterfaceIndex"
- "_localTimestamp"
- "_lock"
- "_lowLatencyStatisticsUpdatedHandler"
- "_macAddress"
- "_maxDatapaths"
- "_maxPeers"
- "_maxPublishers"
- "_maxSubscribers"
- "_maximumNANDataPath"
- "_modelName"
- "_multicastAddress"
- "_multicastConfiguration"
- "_name"
- "_nanRole"
- "_ndiAddr"
- "_ndiInfos"
- "_ndiName"
- "_ndiSessionInfos"
- "_notificationCenter"
- "_notifyToken"
- "_numofPeers"
- "_openTransactions"
- "_operatingChannel"
- "_operatingClass"
- "_options"
- "_packetsHOFOn2GCount"
- "_packetsNAVOn2GCount"
- "_packetsOn2GCount"
- "_packetsOn5GCount"
- "_packetsOverridenOn5GCount"
- "_pairSetupRequired"
- "_pairSetupServiceSpecificInfo"
- "_pairedDeviceName"
- "_pairedUUID"
- "_pairingCachingEnabled"
- "_pairingClient"
- "_pairingConfiguration"
- "_pairingDelegate"
- "_pairingMetadata"
- "_pairingMethod"
- "_pairingNFCTag"
- "_pairingName"
- "_pairingPINCode"
- "_pairingPassphrase"
- "_pairingQRCodeInformation"
- "_pairingSetupMode"
- "_passphrase"
- "_passphraseList"
- "_peerAddress"
- "_peerBandInformation"
- "_peerDataAddress"
- "_peerDeviceName"
- "_peerMacAddress"
- "_peerMasterChannel"
- "_peerNmiMacAddress"
- "_peerPrimaryPreferredChannel"
- "_peerSecondaryPreferredChannel"
- "_period"
- "_pinCode"
- "_pmk"
- "_pmkID"
- "_pmkList"
- "_preferred2GChannelsCount"
- "_preferred5GChannelsCount"
- "_preferredChannel"
- "_preferredChannelClasses"
- "_preferredChannelNumbers"
- "_preferredChannelsCount"
- "_primaryChannel"
- "_primaryChannelClass"
- "_protocolType"
- "_provider"
- "_publishID"
- "_publishServiceCount"
- "_publisherAddress"
- "_qosType"
- "_queue"
- "_queuedRequests"
- "_quietIECount"
- "_realtimeModeUpdatedHandler"
- "_registeredServices"
- "_remoteObject"
- "_remoteProxy"
- "_removeFirstTrafficRegistrationMatching:"
- "_removeOpenTransaction:"
- "_requiresConnection"
- "_retryConnection"
- "_retryTimeout"
- "_retryTimer"
- "_role"
- "_rssi"
- "_rtmLowLatencySessionRefCount"
- "_rtmSessionRefCount"
- "_rtmSessionWith24GOnlyCount"
- "_rtpSequenceNumber"
- "_rtpStartTime"
- "_rxFWDelayHistogram"
- "_rxIPCDelayHistogram"
- "_rxRSSIHistogram"
- "_secondaryChannel"
- "_secondaryChannelClass"
- "_secondaryPreferredChannel"
- "_security"
- "_securityConfiguration"
- "_selfPairingName"
- "_selfRankM"
- "_selfRankR"
- "_service"
- "_serviceAvailabilityUpdatedHandler"
- "_serviceCallback"
- "_serviceId"
- "_serviceKey"
- "_serviceName"
- "_servicePort"
- "_serviceSpecificInfo"
- "_serviceType"
- "_serviceValue"
- "_servicesRequiringAvailabilityNotification"
- "_sessionCount"
- "_sessionState"
- "_sessionWith24GOnlyPeerCount"
- "_setCountryCodeHandler"
- "_setQueue:"
- "_showsUIAlertOnError"
- "_signalStrength"
- "_signature"
- "_softAPChannelChangedEventHandler"
- "_srvHash"
- "_srvId"
- "_srvInfoUpdatedHandler"
- "_srvName"
- "_srvSessionCount"
- "_srvSessionInfos"
- "_srvType"
- "_stateUpdatedHandler"
- "_statisticsUpdatedHandler"
- "_storageClass"
- "_subscribeID"
- "_subscribeServiceCount"
- "_substate"
- "_supportedBands"
- "_supportedCipherSuites"
- "_supportedFeatures"
- "_supportedPairSetupMethods"
- "_supportsDataTransfer"
- "_supportsDualBand"
- "_supportsSimultaneousDualBand"
- "_supportsSoloMode"
- "_suspendCount"
- "_threadCoexistenceEventHandler"
- "_throughputCapacityMbps"
- "_throughputCeilingMbps"
- "_timeBitmap"
- "_timeoutAfterSeconds"
- "_timestamp"
- "_totalSessionCounter"
- "_tsf"
- "_txCCAHistogram"
- "_txChipModeErrorCount"
- "_txConsecutiveErrorsHistogram"
- "_txDroppedCount"
- "_txErrorCount"
- "_txExpiredCount"
- "_txFailedCount"
- "_txFirmwareFreePacketCount"
- "_txForceLifetimeExpiredCount"
- "_txIOErrorCount"
- "_txInternalErrorCount"
- "_txLatency"
- "_txMaxRetriesCount"
- "_txMemoryErrorCount"
- "_txNoACKCount"
- "_txNoRemotePeerCount"
- "_txNoResourcesCount"
- "_txPacketExpiryHistogram"
- "_txtRecordData"
- "_uniqueIdentifier"
- "_useBridging"
- "_useWiFiAware"
- "_usingAWDLDiscoveryManagerProxy:onSuccess:error:"
- "_value"
- "_vendorName"
- "_xpcConnection"
- "activate"
- "activateWithCompletion:"
- "activeFlagOverride"
- "addNotificationRequest:completionHandler:"
- "addNotificationRequest:withCompletionHandler:"
- "addObject:"
- "addorUpdateAutoPairingBootstrapBlob:"
- "addorUpdateAutoPairingBootstrapBlob:uuid:"
- "addorUpdateAutoPairingBootstrapBlobForPeer:"
- "allKeys"
- "allowedDeviceIDs"
- "appendFormat:"
- "appendString:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:"
- "arrayWithObjects:count:"
- "attemptConnection"
- "attributes"
- "authenticationType"
- "authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:completionHandler:"
- "authorizeNewPairedDeviceFor:pairingKeyStoreID:storageClass:lifetime:client:error:"
- "automatic"
- "automaticallyProvideInternetToResponders"
- "automaticallyRequestInternetFromInitiators"
- "autorelease"
- "availUpdatedHandler"
- "availabilityUpdatedForService:error:"
- "beginAvailabilityMonitoring"
- "beginDataPathMonitoring"
- "beginMonitoring"
- "beginSrvInfoMonitoring"
- "beginTransaction:completionHandler:"
- "binEnd"
- "binStart"
- "blob"
- "blobEquals:"
- "body"
- "boolValue"
- "bundleForClass:"
- "bundleID"
- "bundleWithPath:"
- "bytes"
- "cancel"
- "channelConfigurationEqual:"
- "channelInfo"
- "channelNumber"
- "channelSequence"
- "channelSequenceChangedEvent:"
- "channelSequenceMismatchOn2GCount"
- "channelSequenceMismatchOn5GCount"
- "channelSequenceUpdatedEventHandler"
- "characterAtIndex:"
- "class"
- "cleanUpRemovingNotifyToken:"
- "clearTrafficRegistration:error:"
- "compare:"
- "componentsJoinedByString:"
- "configuration"
- "configureNotificationsWithBundleIdentifier:"
- "conformsToProtocol:"
- "connectionInvalidated"
- "connectionMode"
- "containsObject:"
- "containsString:"
- "convertError:"
- "copy"
- "copyActiveServiceUniqueIdentifiers"
- "copyLowLatencyStatistics"
- "copySidecarStatistics"
- "copyStatistics"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countryCode"
- "countryCodeEqual:"
- "createDatapathInfoWithDatapathID:role:peerMacAddress:completion:"
- "createDatapathWithConfiguration:completionHandler:"
- "createPairingStore:"
- "createPublishWithConfiguration:completionHandler:"
- "createSubscribeWithConfiguration:completionHandler:"
- "createXPCResponderWithType:completionHandler:"
- "csaCount"
- "currentDeviceCapabilities"
- "currentLocale"
- "currentState"
- "d"
- "d16@0:8"
- "data"
- "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:"
- "dataSession:confirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
- "dataSession:failedToStartWithError:"
- "dataSession:receivedControlDataAddress:serviceSpecificInfo:onInterfaceIndex:"
- "dataSession:terminatedWithReason:"
- "dataSession:updatedPeerRSSI:"
- "dataSessionRequestStarted:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "datapathCipherSuite"
- "datapathConfiguration"
- "datapathConfigurationEqual:"
- "datapathConfirmedForPeerDataAddress:serviceSpecificInfo:"
- "datapathConfirmedForPeerDataAddress:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
- "datapathFailedToStartWithError:"
- "datapathID"
- "datapathPairingDidSucceedWithPairingKeyStoreID:deviceID:"
- "datapathPairingRequestStartedWithPairingMethod:pairingAuthenticationInputCompletionHandler:"
- "datapathReceivedControlDataAddress:serviceSpecificInfo:onInterfaceIndex:"
- "datapathSecurityRequired"
- "datapathStartedWithInstanceID:initiatorDataAddress:localInterfaceIndex:"
- "datapathSupported"
- "datapathTerminatedWithReason:"
- "datapathUpdatedInternetSharingPolicy:"
- "datapathUpdatedPeerRSSI:"
- "datapathUpdatedServiceSpecificInfo:"
- "deactivate"
- "dealloc"
- "deauthorizePairedDeviceFor:withDeviceID:remove:"
- "deauthorizePairedDeviceFor:withDeviceID:remove:completionHandler:"
- "debugDescription"
- "decodeArrayOfObjectsOfClass:forKey:"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeInt32ForKey:"
- "decodeInt64ForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultRetryTimeout"
- "defaultSound"
- "delegate"
- "deleteAutoPairingBootstrapBlobForClientUUID:"
- "deleteCharactersInRange:"
- "deriveSharedSecretForProtocolName:context:derivationMethod:completion:"
- "description"
- "descriptionWithChangedOptions:"
- "descriptionWithChangedOptions:forceAllChangedOptions:"
- "detailedDescriptionWithChangedOptions:previousSchedule:"
- "detailedDescriptionWithChangedOptions:previousSchedule:forceAllChangedOptions:"
- "detailedDescriptionWithChangedOptions:previousSrvInfo:"
- "deviceAdded:"
- "deviceChanged:"
- "deviceID"
- "deviceRemoved:"
- "dfsChannelsCount"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "directQueryOnEndpointType:error:querying:"
- "directQueryOnEndpointType:exportedObject:withExportedInterface:error:querying:"
- "directRequestOnEndpointType:error:requesting:"
- "discoveryInterfaceName"
- "discoveryMode"
- "discoveryResult"
- "doubleValue"
- "dpStateUpdatedHandler"
- "dump:to:maximumDepth:completionHandler:"
- "durationActive"
- "dynamicLinkRate"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInt32:forKey:"
- "encodeInt64:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "endAvailabilityMonitoring"
- "endDataPathMonitoring"
- "endMonitoring"
- "endSrvInfoMonitoring"
- "endTransaction:"
- "endTransaction:completionHandler:"
- "endpointForEndpointType:"
- "endpointForType:processName:completionHandler:"
- "errorWithDomain:code:userInfo:"
- "exportedInterface"
- "exportedObject"
- "extensionChannelAbove"
- "fastDiscoveryConfigEqual:"
- "fastDiscoveryConfiguration"
- "fastDiscoveryConfigurationEqual:"
- "fetchAWDLActiveServices:withActivePorts:error:"
- "fetchAutoPairingBootstrapBlob:error:"
- "firstObject"
- "forwardInvocation:"
- "frameworkBundle"
- "fsdFunction"
- "fsdFunctionString"
- "furtherServiceDiscoveryRequired"
- "generateCurrentNetworkRecordForInternetSharingSession:"
- "generateDiversifiedPINForDataSession:completionHandler:"
- "generateDiversifiedPINWithCompletionHandler:"
- "generateStatisticsReportForDataSession:completionHandler:"
- "generateStatisticsReportWithCompletionHandler:"
- "getActiveTrafficRegistrationWithCompletionHandler:"
- "getDiversifiedPinCodeForDataSession:completionHandler:"
- "getFormattedDataPathStateDescription"
- "getFormattedDataPathStateDescription:"
- "getFormattedRadioScheduleDescription:"
- "getFormattedSrvInfoDescription:"
- "getFormattedStateDescription:"
- "gtkKey"
- "handleConnectionEstablishedWithProxy:"
- "handleConnectionInvalidated"
- "handleError:"
- "handleEventType:keyData:valueData:"
- "hasPrefix:"
- "hasSimilarOptionsTo:"
- "hasSuffix:"
- "hash"
- "hostname"
- "hostnameEquals:"
- "i24@0:8@16"
- "i24@0:8Q16"
- "iconNamed:"
- "igtkKey"
- "indexOfObject:"
- "infraAssocCount"
- "infraChannelClass"
- "infraDisassocCount"
- "infraRelayOperationStatus"
- "infraRelayRequestersCount"
- "infraScanCount"
- "infrastructureChannel"
- "init"
- "initForService:"
- "initInternal"
- "initUsingWiFiAware:serviceCallback:"
- "initWithAddress:"
- "initWithAddress:ipv6Address:"
- "initWithBinStart:binEnd:value:"
- "initWithBundleID:selfPairingName:peerDeviceName:storageClass:lifetime:pairingClient:"
- "initWithBundleIdentifier:"
- "initWithChannel:bandwidth:band:period:timeBitmap:"
- "initWithChannelNumber:bandwidth:is2_4GHz:is5GHz:is6GHz:isDFS:extensionChannelAbove:"
- "initWithChannels:"
- "initWithCoder:"
- "initWithConfiguration:"
- "initWithDatapathID:initiatorDataAddress:"
- "initWithDatapathID:role:peerMacAddress:"
- "initWithDictionary:isActive:"
- "initWithDiscoveryResult:serviceType:passphrase:pmk:pmkID:serviceSpecificInfo:internetSharingConfiguration:pairingMethod:pairingCachingEnabled:pairSetupServiceSpecificInfo:connectionMode:pairingMetadata:multicastConfiguration:"
- "initWithDiscoveryResult:serviceType:serviceSpecificInfo:"
- "initWithDiscoveryResult:serviceType:serviceSpecificInfo:passphrase:"
- "initWithDiscoveryResult:serviceType:serviceSpecificInfo:passphrase:pmk:pmkID:"
- "initWithDiscoveryResult:serviceType:serviceSpecificInfo:pmk:"
- "initWithDiscoveryResult:serviceType:serviceSpecificInfo:pmk:pmkID:"
- "initWithDpId:dpRole:serviceId:initiatorDataAddress:peerNmiMacAddress:peerDataAddress:sessionState:"
- "initWithEndpointType:queue:retryTimeout:"
- "initWithFormat:locale:"
- "initWithInterfaceName:interfaceAddr:isEnabled:band24GHz:band5GHz:supportsDualBand:supportsSimultaneousDualBand:primaryChannel:secondaryChannel:infraChannel:preferredChannelsCount:preferredChannelNumbers:"
- "initWithInterfaceName:interfaceAddr:isEnabled:isFWElection:nanRole:hopCount:clusterId:selfRankM:selfRankR:immediateMaster:immediateMasterRankM:immediateMasterRankR:anchorMaster:anchorMasterRankM:anchorMasterRankR:ambtt:tsf:"
- "initWithInterfaceName:interfaceAddr:isEnabled:publishServiceCount:subscribeServiceCount:srvSessionCount:srvSessionInfos:"
- "initWithInterfaceName:interfaceAddr:isEnabled:totalSessionCounter:establishedSessionCounter:sessionWith24GOnlyPeerCount:rtmSessionRefCount:rtmSessionWith24GOnlyCount:rtmLowLatencySessionRefCount:ndiInfos:preferredChannelNumbers:preferredChannelClasses:ndiSessionInfos:"
- "initWithInterfaceName:isProvider:isAutomatic:"
- "initWithInterfaceName:supportsSoloMode:supportsDataTransfer:channelSequence:isEnabled:substate:macAddress:peerMasterChannel:peerPrimaryPreferredChannel:peerSecondaryPreferredChannel:"
- "initWithKey:"
- "initWithKey:value:resolve:"
- "initWithLinkLocalIPv6Address:"
- "initWithListenerEndpoint:"
- "initWithLocaleIdentifier:"
- "initWithMachServiceName:options:"
- "initWithMulticastIPv6Address:"
- "initWithName:pairingName:vendorName:modelName:attributes:"
- "initWithName:vendorID:modelName:attributes:"
- "initWithNdiName:ndiAddr:sessionCount:security:qosType:"
- "initWithPMK:andPMKID:"
- "initWithPMKList:passphraseList:"
- "initWithPairingConfiguration:usingPairingDelegate:"
- "initWithPairingConfiguration:usingPairingDelegate:usingPairingNFCTag:"
- "initWithPairingConfiguration:usingPairingDelegate:usingPairingPINCode:"
- "initWithPairingConfiguration:usingPairingDelegate:usingPairingPassphrase:"
- "initWithPairingConfiguration:usingPairingDelegate:usingPairingQRCodeInformation:"
- "initWithPeerAddress:infrastructureChannel:txCCAHistogram:rxRSSIHistogram:preferred2GChannelsCount:preferred5GChannelsCount:dfsChannelsCount:csaCount:quietIECount:txErrorCount:packetsOn2GCount:packetsNAVOn2GCount:packetsHOFOn2GCount:packetsOn5GCount:packetsOverridenOn5GCount:infraRelayOperationStatus:infraRelayRequestersCount:txExpiredCount:txNoACKCount:txFailedCount:txNoResourcesCount:txIOErrorCount:txMemoryErrorCount:txChipModeErrorCount:txNoRemotePeerCount:txInternalErrorCount:txDroppedCount:txFirmwareFreePacketCount:txMaxRetriesCount:txForceLifetimeExpiredCount:channelSequenceMismatchOn5GCount:channelSequenceMismatchOn2GCount:infraScanCount:infraAssocCount:infraDisassocCount:countryCode:txConsecutiveErrorsHistogram:rxFWDelayHistogram:rxIPCDelayHistogram:txPacketExpiryHistogram:"
- "initWithPeerDeviceName:"
- "initWithProtocolType:servicePort:"
- "initWithServiceName:"
- "initWithServiceName:discoveryMode:"
- "initWithServiceName:serviceSpecificInfo:"
- "initWithServiceName:serviceSpecificInfo:publishID:subscribeID:publisherAddressKey:datapathSupported:datapathCipherSuite:fsdFunction:rssi:pairSetupRequired:pairingConfiguration:pairedUUID:pairedDeviceName:signature:"
- "initWithServiceType:securityConfiguration:"
- "initWithServiceType:securityConfiguration:connectionMode:"
- "initWithSrvId:srvType:srvName:srvHash:ndiInfos:numofPeers:"
- "initWithSupportedFeatures:operatingChannel:operatingClass:supportedCipherSuites:supportsDataTransfer:supportedBands:discoveryInterfaceName:maxPeers:maxPublishers:maxSubscribers:maxDatapaths:"
- "initWithSupportedPairSetupMethods:pairingCachingEnabled:"
- "initWithSupportedPairSetupMethods:pairingCachingEnabled:pairingSetupMode:"
- "initWithTimestamp:localTimestamp:throughputCeilingMbps:throughputCapacityMbps:txLatency:signalStrength:durationActive:"
- "initWithUniqueIdentifier:peerAddress:"
- "initWithUniqueIdentifier:peerIPv6Address:"
- "initWithUnsignedLong:"
- "instanceMethodSignatureForSelector:"
- "instanceName"
- "instanceNameEquals:"
- "instantCommunicationChannel"
- "intValue"
- "integerValue"
- "interfaceNameEqual:"
- "interfaceWithProtocol:"
- "internetSharingConfiguration"
- "internetSharingConfigurationEqual:"
- "internetSharingEqual:"
- "internetSharingPolicy"
- "invalidate"
- "invalidatedActiveTrafficRegistration:"
- "invalidationHandler"
- "invokeWithTarget:"
- "ipv6LinkLocalAddress"
- "is2_4GHz"
- "is5GHz"
- "is6GHz"
- "isDFS"
- "isEqual:"
- "isEqualToArray:"
- "isEqualToData:"
- "isEqualToString:"
- "isKindOfClass:"
- "isKnownService"
- "isMemberOfClass:"
- "isProxy"
- "isResolve"
- "jumboServiceDiscoveryMessages"
- "keyBlob"
- "keyExchangeOverMedium"
- "lastDataPathStateChangedOptions"
- "lastRadioSchedule"
- "lastRadioScheduleChangedOptions"
- "lastSrvInfo"
- "lastSrvInfoChangedOptions"
- "lastStateChangedOptions"
- "legacyUpgradeRequired"
- "length"
- "lifetime"
- "localDataAddress"
- "localInterfaceIndex"
- "localTimestamp"
- "localeIdentifier"
- "localization"
- "localizations"
- "localizedErrorForConflictBetweenExistingService:withNewService:localDeviceName:localization:"
- "localizedStringForKey:value:table:localization:"
- "lock"
- "lowLatencyStatisticsDifferenceBetweenPrevious:current:"
- "lowLatencyStatisticsUpdatedHandler"
- "mapSessionStateToNumber:"
- "maxDatapaths"
- "maxPeers"
- "maxPublishers"
- "maxSubscribers"
- "methodSignatureForSelector:"
- "modelName"
- "multicastAddress"
- "multicastAddressConfigurationEqual:"
- "multicastConfiguration"
- "multicastConfigurationEqual:"
- "mutableCopy"
- "name"
- "null"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedShort:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "operatingChannel"
- "operatingClass"
- "packetsHOFOn2GCount"
- "packetsNAVOn2GCount"
- "packetsOn2GCount"
- "packetsOn5GCount"
- "packetsOverridenOn5GCount"
- "pairSetupRequired"
- "pairSetupServiceSpecificInfo"
- "pairSetupServiceSpecificInfoEqual:"
- "pairedDeviceAdded:"
- "pairedDeviceChanged:"
- "pairedDeviceName"
- "pairedDeviceRemoved:"
- "pairedUUID"
- "pairingCachingEnabled"
- "pairingClient"
- "pairingConfiguration"
- "pairingDelegate"
- "pairingMetadata"
- "pairingMethod"
- "pairingNFCTag"
- "pairingName"
- "pairingPINCode"
- "pairingPassphrase"
- "pairingQRCodeInformation"
- "pairingRequestApprovalRequiredByPublisher:forSubscriber:withPairingMethod:pairingSetupApprovalCompletion:"
- "pairingRequestApprovalRequiredByPublisher:forSubscriber:withPairingMethod:pairingSetupApprovalHandler:"
- "pairingRequestCompletedForDataSession:pairingKeyStoreID:deviceID:"
- "pairingRequestCompletedForPublisher:pairingKeyStoreID:deviceID:"
- "pairingRequestEndedForPublisher:bySubscriber:reason:"
- "pairingRequestIndicatedForPublisher:bySubscriber:usingNFCTag:"
- "pairingRequestIndicatedForPublisher:bySubscriber:usingPINCode:"
- "pairingRequestIndicatedForPublisher:bySubscriber:usingPassphrase:"
- "pairingRequestIndicatedForPublisher:bySubscriber:usingQRCodeInformation:"
- "pairingRequestStartedForDataSession:nfcTagScannedCompletionHandler:"
- "pairingRequestStartedForDataSession:passphraseInputCompletionHandler:"
- "pairingRequestStartedForDataSession:pinCodeInputCompletionHandler:"
- "pairingRequestStartedForDataSession:qrCodeScannedCompletionHandler:"
- "pairingSetupMode"
- "passphrase"
- "passphraseEqual:"
- "passphraseList"
- "peerBandInformation"
- "peerDeviceName"
- "peerMasterChannel"
- "peerPrimaryPreferredChannel"
- "peerSecondaryPreferredChannel"
- "performRealtimeConnectivityCheckWithConfiguration:completionHandler:"
- "performRealtimeConnectivityCheckWithConfiguration:error:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performance:"
- "pinCode"
- "pmk"
- "pmkEqual:"
- "pmkID"
- "pmkIDEqual:"
- "pmkList"
- "preferred2GChannelsCount"
- "preferred5GChannelsCount"
- "preferredChannel"
- "preferredLanguages"
- "preferredLocalizationsFromArray:forPreferences:"
- "primaryChannelClass"
- "protocolType"
- "provideInternetToInitiatorsFromInterface:"
- "publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:"
- "publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:"
- "publishDataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
- "publishDataTerminatedForHandle:reason:"
- "publishDetectedMulticastError:fromMulticastReceiver:"
- "publishFailedToStartWithError:"
- "publishID"
- "publishKeysBlobForMulticastSession:"
- "publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalCompletion:"
- "publishPairingApprovalForSubscriber:withPairingMethod:pairingSetupApprovalHandler:"
- "publishPairingDidSucceedWithPairingKeyStoreID:deviceID:"
- "publishPairingRequestEndedWithSubscriber:reason:"
- "publishPairingRequestIndicatedBySubscriber:withPairingMethod:pairingAuthenticationGeneratedCompletionHandler:"
- "publishReceivedDataBlobForMulticastSession:fromPeer:"
- "publishReceivedMessage:fromSubscriberID:subscriberAddress:"
- "publishStartedWithInstanceID:maximumNANDataPath:"
- "publishTerminatedWithReason:"
- "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:"
- "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:"
- "publisher:dataConfirmedForHandle:localInterfaceIndex:serviceSpecificInfo:pairingKeyStoreID:deviceID:"
- "publisher:dataTerminatedForHandle:reason:"
- "publisher:detectedMulticastError:fromMulticastReceiver:"
- "publisher:failedToStartWithError:"
- "publisher:getKeysBlobForMulticastSession:"
- "publisher:receivedDataBlobForMulticastSession:fromPeer:"
- "publisher:receivedMessage:fromSubscriberID:subscriberAddress:"
- "publisher:terminatedWithReason:"
- "publisherAddress"
- "publisherStarted:"
- "q16@0:8"
- "queryAWDLLowLatencyStatisticsWithCompletionHandler:"
- "queryAWDLState:"
- "queryAWDLStatisticsWithCompletionHandler:"
- "queryActiveServiceUniqueIdentifiersWithCompletionHandler:"
- "queryActiveServicesAndActivePortsWithCompletionHandler:"
- "queryAirPlayConnectivityWithConfiguration:error:"
- "queryAverageRSSIForAWDLPeer:completionHandler:"
- "queryAverageRSSIForPeer:"
- "queryCurrentDeviceCapabilities:"
- "queryNANAvail"
- "queryNANAvailWithCompletionHandler:"
- "queryNANDataPathState"
- "queryNANDataPathStateWithCompletionHandler:"
- "queryNANEnabled"
- "queryNANEnabledWithCompletionHandler:"
- "queryNANSrv"
- "queryNANSrvWithCompletionHandler:"
- "queryNANState"
- "queryNANStateWithCompletionHandler:"
- "queryPairedDevicesInfo:"
- "queryPeerDatabase"
- "queryPeersWithCompletionHandler:"
- "quietIECount"
- "r*16@0:8"
- "rangeOfString:"
- "rangeOfString:options:"
- "realtimeModeUpdatedHandler"
- "reauthorizePairedDeviceFor:withDeviceID:"
- "reauthorizePairedDeviceFor:withDeviceID:completionHandler:"
- "reconnectOnAvailableNotification"
- "registerAvailabilityUpdatesForService:"
- "release"
- "remoteObjectInterface"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllDeliveredNotifications"
- "removeAllObjects"
- "removeAllPairedDevices"
- "removeAllPairedDevices:"
- "removeAllPairedDevicesFor:"
- "removeAllPairedDevicesFor:completionHandler:"
- "removeAllPendingNotificationRequests"
- "removeDeliveredNotificationsWithIdentifiers:"
- "removeNotificationsWithIdentifiers:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removePairedDeviceFor:withDeviceID:"
- "removePairedDeviceFor:withDeviceID:completionHandler:"
- "replaceObjectAtIndex:withObject:"
- "reportIssue:"
- "reportIssue:forDataSession:"
- "requestInterentFromResponder"
- "requestWithIdentifier:content:trigger:"
- "reserveTrafficRegistrationsForConfiguration:enabled:completionHandler:"
- "resetState"
- "respondsToSelector:"
- "resumeAWDLWithError:"
- "retain"
- "retainCount"
- "rotateAutoPairingBootstrapBlobs"
- "rssi"
- "rtpSequenceNumber"
- "rtpSequenceNumberEquals:"
- "rtpStartTime"
- "rtpStartTimeEquals:"
- "rxFWDelayHistogram"
- "rxIPCDelayHistogram"
- "rxRSSIHistogram"
- "secondaryChannelClass"
- "secondaryPreferredChannel"
- "securityConfiguration"
- "securityConfigurationEqual:"
- "self"
- "selfPairingName"
- "sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:"
- "sendMessage:toPeerAddress:withInstanceID:completionHandler:"
- "service"
- "serviceAvailabilityUpdatedHandler"
- "serviceKey"
- "serviceName"
- "servicePort"
- "serviceSpecificInfo"
- "serviceSpecificInfoEqual:"
- "serviceType"
- "serviceValue"
- "servicesRequiringAvailabilityNotification"
- "setAWDLSuspendedState:completionHandler:"
- "setActiveFlagOverride:"
- "setAllowedDeviceIDs:"
- "setAuthenticationType:"
- "setAutomatic:"
- "setAvailUpdatedHandler:"
- "setBlob:"
- "setBody:"
- "setBundleID:"
- "setChannelInfo:"
- "setChannelSequenceMismatchOn2GCount:"
- "setChannelSequenceMismatchOn5GCount:"
- "setChannelSequenceUpdatedEventHandler:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConnectionMode:"
- "setCountryCode:"
- "setCountryCodeHandler"
- "setCsaCount:"
- "setDatapathConfiguration:"
- "setDelegate:"
- "setDeviceID:"
- "setDfsChannelsCount:"
- "setDiscoveryMode:"
- "setDpStateUpdatedHandler:"
- "setDynamicLinkRate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFastDiscoveryConfiguration:"
- "setFurtherServiceDiscoveryRequired:"
- "setGtkKey:"
- "setHostname:"
- "setIcon:"
- "setIgtkKey:"
- "setInfraAssocCount:"
- "setInfraDisassocCount:"
- "setInfraRelayOperationStatus:"
- "setInfraRelayRequestersCount:"
- "setInfraScanCount:"
- "setInstanceName:"
- "setInstantCommunicationChannel:"
- "setInterfaceAddr:"
- "setInterfaceName:"
- "setInternetSharingConfiguration:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsEnabled:"
- "setJumboServiceDiscoveryMessages:"
- "setKeyBlob:"
- "setKeyExchangeOverMedium:"
- "setLastDataPathStateChangedOptions:"
- "setLastRadioSchedule:"
- "setLastRadioScheduleChangedOptions:"
- "setLastSrvInfo:"
- "setLastSrvInfoChangedOptions:"
- "setLastStateChangedOptions:"
- "setLegacyUpgradeRequired:"
- "setLifetime:"
- "setLowLatencyStatisticsUpdatedHandler:"
- "setMulticastAddress:"
- "setMulticastConfiguration:"
- "setName:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptions:"
- "setPacketsHOFOn2GCount:"
- "setPacketsNAVOn2GCount:"
- "setPacketsOn2GCount:"
- "setPacketsOn5GCount:"
- "setPacketsOverridenOn5GCount:"
- "setPairSetupServiceSpecificInfo:"
- "setPairingCachingEnabled:"
- "setPairingClient:"
- "setPairingConfiguration:"
- "setPairingDelegate:"
- "setPairingMetadata:"
- "setPairingMethod:"
- "setPairingSetupMode:"
- "setPeerAddress:"
- "setPeerBandInformation:"
- "setPeerDeviceName:"
- "setPinCode:"
- "setPreferred2GChannelsCount:"
- "setPreferred5GChannelsCount:"
- "setPreferredChannel:"
- "setProvider:"
- "setQuietIECount:"
- "setRealtimeModeUpdatedHandler:"
- "setRemoteObjectInterface:"
- "setRtpSequenceNumber:"
- "setRtpStartTime:"
- "setRxFWDelayHistogram:"
- "setRxIPCDelayHistogram:"
- "setRxRSSIHistogram:"
- "setSecondaryPreferredChannel:"
- "setSecurityConfiguration:"
- "setSelfPairingName:"
- "setServiceAvailabilityUpdatedHandler:"
- "setServiceSpecificInfo:"
- "setServicesRequiringAvailabilityNotification:"
- "setSetCountryCodeHandler:"
- "setShouldHideDate:"
- "setShouldHideTime:"
- "setShouldIgnoreDoNotDisturb:"
- "setShouldIgnoreDowntime:"
- "setShowsUIAlertOnError:"
- "setSoftAPChannelChangedEventHandler:"
- "setSound:"
- "setSrvInfoUpdatedHandler:"
- "setStateUpdatedHandler:"
- "setStatisticsUpdatedHandler:"
- "setStorageClass:"
- "setSupportedPairSetupMethods:"
- "setThreadCoexistenceEventHandler:"
- "setTimeoutAfterSeconds:"
- "setTitle:"
- "setTrafficRegistration:error:"
- "setTrafficRegistration:onInvalidationHandler:error:"
- "setTxCCAHistogram:"
- "setTxChipModeErrorCount:"
- "setTxConsecutiveErrorsHistogram:"
- "setTxDroppedCount:"
- "setTxErrorCount:"
- "setTxExpiredCount:"
- "setTxFailedCount:"
- "setTxFirmwareFreePacketCount:"
- "setTxForceLifetimeExpiredCount:"
- "setTxIOErrorCount:"
- "setTxInternalErrorCount:"
- "setTxMaxRetriesCount:"
- "setTxMemoryErrorCount:"
- "setTxNoACKCount:"
- "setTxNoRemotePeerCount:"
- "setTxNoResourcesCount:"
- "setTxPacketExpiryHistogram:"
- "setTxtRecordData:"
- "setUniqueIdentifier:"
- "setUseBridging:"
- "setValue:"
- "setWantsPeerRSSIUpdates:withCompletionHandler:"
- "setWithArray:"
- "setWithObjects:"
- "shared"
- "showInfrastructureDisconnectOnRetroModeNotificationForService:localization:phoneDisconnected:uuid:completionHandler:"
- "showsUIAlertOnError"
- "signalStrength"
- "signature"
- "softAPChannelChangedEvent:channelNumber:"
- "softAPChannelChangedEventHandler"
- "sortedArrayUsingSelector:"
- "srvInfoUpdatedHandler"
- "start"
- "startConnectionUsingProxy:completionHandler:"
- "startCountryCodeMonitoringWithCompletionHandler:"
- "startMonitoringAWDLStateWithConfiguration:completionHandler:"
- "startMonitoringNANStateWithConfiguration:completionHandler:"
- "startServiceDiscoveryWithConfiguration:"
- "startServiceDiscoveryWithConfiguration:completionHandler:"
- "stateUpdatedHandler"
- "statisticsUpdatedHandler"
- "stop"
- "stopServiceDiscoveryWithConfiguration:"
- "stopServiceDiscoveryWithConfiguration:completionHandler:"
- "storageClass"
- "string"
- "stringForQosType:"
- "stringForSecurity:"
- "stringForSessionState:"
- "stringValue"
- "stringWithCString:encoding:"
- "stringWithCapacity:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subscribeDetectedMulticastError:fromMulticastSender:"
- "subscribeFailedToStartWithError:"
- "subscribeID"
- "subscribeLostDiscoveryResultForPublishID:address:"
- "subscribeReceivedDataBlobForMulticastSession:fromPeer:"
- "subscribeReceivedDiscoveryResult:"
- "subscribeReceivedMessage:fromPublishID:address:"
- "subscribeStartedWithInstanceID:"
- "subscribeTerminatedWithReason:"
- "subscriber:detectedMulticastError:fromMulticastSender:"
- "subscriber:failedToStartWithError:"
- "subscriber:lostDiscoveryResultForPublishID:address:"
- "subscriber:receivedDataBlobForMulticastSession:fromPeer:"
- "subscriber:receivedDiscoveryResult:"
- "subscriber:receivedDiscoveyResult:"
- "subscriber:receivedMessage:fromPublishID:address:"
- "subscriber:terminatedWithReason:"
- "subscriberStarted:"
- "substate"
- "substringToIndex:"
- "superclass"
- "supportedCipherSuites"
- "supportedFeatures"
- "supportedPairSetupMethods"
- "supportsDataTransfer"
- "supportsSecureCoding"
- "supportsSoloMode"
- "supportsWiFiP2P"
- "suspendAWDLWithError:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "terminateDataSession:completionHandler:"
- "terminateMulticastSession:completionHandler:"
- "threadCoexistenceEvent:"
- "threadCoexistenceEventHandler"
- "throughputCapacityMbps"
- "throughputCeilingMbps"
- "timeoutAfterSeconds"
- "timestamp"
- "title"
- "trafficRegistration:enabled:completionHandler:"
- "trafficRegistrationConfiguration"
- "txCCAHistogram"
- "txChipModeErrorCount"
- "txConsecutiveErrorsHistogram"
- "txDroppedCount"
- "txErrorCount"
- "txExpiredCount"
- "txFailedCount"
- "txFirmwareFreePacketCount"
- "txForceLifetimeExpiredCount"
- "txIOErrorCount"
- "txInternalErrorCount"
- "txLatency"
- "txMaxRetriesCount"
- "txMemoryErrorCount"
- "txNoACKCount"
- "txNoRemotePeerCount"
- "txNoResourcesCount"
- "txPacketExpiryHistogram"
- "txtRecordData"
- "txtRecordEquals:"
- "uninstallPairedDeviceFor:withDeviceID:"
- "uninstallPairedDeviceFor:withDeviceID:completionHandler:"
- "uniqueIdentifier"
- "unlock"
- "unsignedCharValue"
- "unsignedIntegerValue"
- "unsignedLongValue"
- "unsignedShortValue"
- "updateAWDLLTERestrictedChannels:completionHandler:"
- "updateDatapathServiceSpecificInfo:completionHandler:"
- "updateLTERestrictedChannels:error:"
- "updateLinkStatus:"
- "updateLinkStatus:forDataSession:"
- "updatePairedDeviceNameFor:withDeviceID:toNewName:"
- "updatePairedDeviceNameFor:withDeviceID:toNewName:completionHandler:"
- "updateServiceSpecificInfo:completionHandler:"
- "updateTimeout:completionHandler:"
- "updatedAWDLState:"
- "updatedLowLatencyStatistics"
- "updatedNANAvailability:"
- "updatedNANAvailabilityWithChangedOptions:changedOptions:"
- "updatedNANAvailabilityWithChangedOptions:changedOptions:forceAllChangedOptions:"
- "updatedNANDpState:"
- "updatedNANDpStateWithChangedOptions:changedOptions:"
- "updatedNANDpStateWithChangedOptions:changedOptions:forceAllChangedOptions:"
- "updatedNANSrvInfo:"
- "updatedNANSrvInfoWithChangedOptions:changedOptions:"
- "updatedNANSrvInfoWithChangedOptions:changedOptions:forceAllChangedOptions:"
- "updatedNANState:"
- "updatedNANStateWithChangedOptions:changedOptions:"
- "updatedNANStateWithChangedOptions:changedOptions:forceAllChangedOptions:"
- "updatedRealtimeMode:"
- "updatedStatistics"
- "useBridging"
- "userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:"
- "userNotificationCenter:openSettingsForNotification:"
- "userNotificationCenter:willPresentNotification:withCompletionHandler:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8S16"
- "v20@0:8i16"
- "v24@0:8@\"AWDLTrafficRegistrationConfiguration\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@\"WiFiAwareDataPathState\"16"
- "v24@0:8@\"WiFiAwareDataSessionIssueReport\"16"
- "v24@0:8@\"WiFiAwareDiscoveryResult\"16"
- "v24@0:8@\"WiFiAwarePairedDeviceInfo\"16"
- "v24@0:8@\"WiFiAwarePublishDatapathServiceSpecificInfo\"16"
- "v24@0:8@\"WiFiAwareRadioSchedule\"16"
- "v24@0:8@\"WiFiAwareSrvInfo\"16"
- "v24@0:8@\"WiFiAwareState\"16"
- "v24@0:8@\"WiFiP2PAWDLState\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSArray\">16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSDictionary\">16"
- "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"WiFiAwareDataPathState\">16"
- "v24@0:8@?<v@?@\"WiFiAwareDatapathPerformanceReport\">16"
- "v24@0:8@?<v@?@\"WiFiAwareDeviceCapabilities\">16"
- "v24@0:8@?<v@?@\"WiFiAwareRadioSchedule\">16"
- "v24@0:8@?<v@?@\"WiFiAwareSrvInfo\">16"
- "v24@0:8@?<v@?@\"WiFiAwareState\">16"
- "v24@0:8@?<v@?@\"WiFiP2PAWDLState\">16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8@?<v@?q>16"
- "v24@0:8@?<v@?q@\"NSDictionary\">16"
- "v24@0:8@?<v@?q@\"NSString\">16"
- "v24@0:8@?<v@?q@\"WiFiAwareDataSessionStatisticsReport\">16"
- "v24@0:8B16S20"
- "v24@0:8C16I20"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"
- "v28@0:8B16@?<v@?q>20"
- "v28@0:8C16@\"WiFiMACAddress\"20"
- "v28@0:8C16@20"
- "v32@0:8@\"<WiFiP2PXPCProtocol>\"16@?<v@?q>24"
- "v32@0:8@\"AWDLServiceDiscoveryConfiguration\"16@?<v@?q>24"
- "v32@0:8@\"AWDLTrafficRegistrationConfiguration\"16@?<v@?@\"NSNumber\">24"
- "v32@0:8@\"NSArray\"16@?<v@?q>24"
- "v32@0:8@\"NSData\"16@\"WiFiMACAddress\"24"
- "v32@0:8@\"NSString\"16@\"NSError\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16Q24"
- "v32@0:8@\"UNNotificationRequest\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24"
- "v32@0:8@\"WiFiAwareDataPathState\"16@\"NSArray\"24"
- "v32@0:8@\"WiFiAwareDataSessionIssueReport\"16@\"WiFiAwarePublisherDataSessionHandle\"24"
- "v32@0:8@\"WiFiAwareDatapathConfiguration\"16@?<v@?q>24"
- "v32@0:8@\"WiFiAwarePublishConfiguration\"16@?<v@?q>24"
- "v32@0:8@\"WiFiAwarePublishDatapathServiceSpecificInfo\"16@?<v@?q>24"
- "v32@0:8@\"WiFiAwarePublishServiceSpecificInfo\"16@?<v@?q>24"
- "v32@0:8@\"WiFiAwarePublishServiceSpecificInfo\"16q24"
- "v32@0:8@\"WiFiAwarePublisherDataSessionHandle\"16@?<v@?q>24"
- "v32@0:8@\"WiFiAwarePublisherDataSessionHandle\"16@?<v@?q@\"NSString\">24"
- "v32@0:8@\"WiFiAwarePublisherDataSessionHandle\"16@?<v@?q@\"WiFiAwareDataSessionStatisticsReport\">24"
- "v32@0:8@\"WiFiAwarePublisherDataSessionHandle\"16q24"
- "v32@0:8@\"WiFiAwareRadioSchedule\"16@\"NSArray\"24"
- "v32@0:8@\"WiFiAwareSrvInfo\"16@\"NSArray\"24"
- "v32@0:8@\"WiFiAwareState\"16@\"NSArray\"24"
- "v32@0:8@\"WiFiAwareStateMonitorConfiguration\"16@?<v@?q>24"
- "v32@0:8@\"WiFiAwareSubscribeConfiguration\"16@?<v@?q>24"
- "v32@0:8@\"WiFiMACAddress\"16@\"WiFiAwarePublishDatapathServiceSpecificInfo\"24"
- "v32@0:8@\"WiFiMACAddress\"16@?<v@?i>24"
- "v32@0:8@\"WiFiMACAddress\"16@?<v@?q>24"
- "v32@0:8@\"WiFiP2PAWDLStateMonitorConfiguration\"16@?<v@?q>24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v32@0:8@?16@?24"
- "v32@0:8C16@\"WiFiMACAddress\"20I28"
- "v32@0:8C16@20I28"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?q>24"
- "v32@0:8q16@\"WiFiAwarePublisherDataSessionHandle\"24"
- "v32@0:8q16@\"WiFiMACAddress\"24"
- "v32@0:8q16@24"
- "v32@0:8q16@?24"
- "v32@0:8q16@?<v@?@\"NSData\">24"
- "v32@0:8q16@?<v@?q>24"
- "v36@0:8@\"AWDLTrafficRegistrationConfiguration\"16B24@?<v@?@\"NSError\">28"
- "v36@0:8@\"NSData\"16C24@\"WiFiMACAddress\"28"
- "v36@0:8@\"WiFiAwareDataPathState\"16@\"NSArray\"24B32"
- "v36@0:8@\"WiFiAwarePublisherDataSessionHandle\"16I24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"28"
- "v36@0:8@\"WiFiAwareRadioSchedule\"16@\"NSArray\"24B32"
- "v36@0:8@\"WiFiAwareSrvInfo\"16@\"NSArray\"24B32"
- "v36@0:8@\"WiFiAwareState\"16@\"NSArray\"24B32"
- "v36@0:8@\"WiFiMACAddress\"16@\"WiFiAwarePublishDatapathServiceSpecificInfo\"24I32"
- "v36@0:8@16@24B32"
- "v36@0:8@16@24I32"
- "v36@0:8@16B24@?28"
- "v36@0:8@16C24@28"
- "v36@0:8@16I24@28"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\">32"
- "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotification\"24@?<v@?Q>32"
- "v40@0:8@\"UNUserNotificationCenter\"16@\"UNNotificationResponse\"24@?<v@?>32"
- "v40@0:8@\"WiFiAwarePublishServiceSpecificInfo\"16q24@?<v@?@\"NSData\">32"
- "v40@0:8@\"WiFiAwarePublishServiceSpecificInfo\"16q24@?<v@?q@\"NSData\">32"
- "v40@0:8@\"WiFiAwarePublishServiceSpecificInfo\"16q24@?<v@?q@\"WiFiAwarePairingInfo\">32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16q24@?32"
- "v40@0:8Q16@\"NSData\"24@\"NSData\"32"
- "v40@0:8Q16@\"NSString\"24@?<v@?@\"NSXPCListenerEndpoint\">32"
- "v40@0:8Q16@24@32"
- "v40@0:8Q16@24@?32"
- "v44@0:8@\"NSData\"16@\"WiFiMACAddress\"24C32@?<v@?q>36"
- "v44@0:8@\"NSString\"16Q24B32@?<v@?@\"NSError\">36"
- "v44@0:8@\"WiFiAwarePublisherDataSessionHandle\"16I24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"28@\"NSUUID\"36"
- "v44@0:8@16@24C32@?36"
- "v44@0:8@16I24@28@36"
- "v44@0:8@16Q24B32@?36"
- "v44@0:8C16q20@\"WiFiMACAddress\"28@?<v@?q>36"
- "v44@0:8C16q20@28@?36"
- "v48@0:8@\"NSArray\"16@\"NSFileHandle\"24q32@?<v@?q>40"
- "v48@0:8@\"NSString\"16@\"NSString\"24q32@?<v@?@\"NSData\">40"
- "v48@0:8@\"NSString\"16Q24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@\"WiFiMACAddress\"16@\"WiFiAwarePublishDatapathServiceSpecificInfo\"24@\"NSUUID\"32Q40"
- "v48@0:8@16@24@32Q40"
- "v48@0:8@16@24q32@?40"
- "v48@0:8@16Q24@32@?40"
- "v52@0:8@\"NSString\"16@\"NSString\"24B32@\"NSUUID\"36@?<v@?@\"NSError\">44"
- "v52@0:8@\"WiFiAwarePublisherDataSessionHandle\"16I24@\"WiFiAwarePublishDatapathServiceSpecificInfo\"28@\"NSUUID\"36Q44"
- "v52@0:8@16@24B32@36@?44"
- "v52@0:8@16I24@28@36Q44"
- "v64@0:8@\"NSString\"16@\"NSUUID\"24q32d40q48@?<v@?Q@\"NSError\">56"
- "v64@0:8@16@24q32d40q48@?56"
- "value"
- "valueForKey:"
- "vendorName"
- "weakExportedObjectProxy:"
- "wifiPeerToPeerAvailableNotification"
- "wifiPeerToPeerWorkloop"
- "wifip2pExportedXPCInterfaceFor:"
- "wifip2pRemoteXPCInterface"
- "withRemoteObjectProxy:"
- "withRemoteObjectProxy:clientCompletionHandler:"
- "withRemoteObjectProxy:clientErrorHandler:"
- "zeroAddress"
- "zone"
- "\xd1Q"

```
