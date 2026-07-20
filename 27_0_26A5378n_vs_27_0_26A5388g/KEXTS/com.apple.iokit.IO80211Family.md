## com.apple.iokit.IO80211Family

> `com.apple.iokit.IO80211Family`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-1585.62.0.0.0
+1585.70.0.0.0
   __TEXT.__os_log: 0x9e36
   __TEXT.__const: 0x2bec0
-  __TEXT.__cstring: 0x98784
-  __TEXT_EXEC.__text: 0x2786cc
+  __TEXT.__cstring: 0x98988
+  __TEXT_EXEC.__text: 0x278cd0
   __TEXT_EXEC.__auth_stubs: 0x1420
   __DATA.__data: 0x5ec8
   __DATA.__common: 0x2c70

   __DATA_CONST.__auth_got: 0xa10
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x20
-  Functions: 13080
-  Symbols:   17099
-  CStrings:  14868
+  Functions: 13085
+  Symbols:   17107
+  CStrings:  14876
 
Symbols:
+ __FUNCTION__._ZN15IO80211AWDLPeer16recordParseErrorEj
+ __FUNCTION__._ZN15IO80211AWDLPeer18recordParseSuccessEv
+ __FUNCTION__._ZN17IO80211BssManager22getCurrentBeaconPeriodEPj
+ __ZN14IO80211NANPeer17clearInfraChannelEv
+ __ZN15IO80211AWDLPeer16recordParseErrorEj
+ __ZN15IO80211AWDLPeer18recordParseSuccessEv
+ __ZN15IO80211AWDLPeer18recordPostAFToP2pdEv
+ __ZN22IO80211AWDLPeerManager11exitProModeE17proModeExitReasonP15IO80211AWDLPeerb
+ __ZN22WCLTrafficPatternAgent30updateSignalStrengthHysteresisEi
+ __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1827
+ __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1845
+ __ZZN15IO80211AWDLPeer13freeResourcesEvE20kalloc_type_view_462
+ __ZZN15IO80211AWDLPeer13freeResourcesEvE20kalloc_type_view_467
+ __ZZN15IO80211AWDLPeer13freeResourcesEvE20kalloc_type_view_472
+ __ZZN15IO80211AWDLPeer15clearCacheStateEvE20kalloc_type_view_497
+ __ZZN15IO80211AWDLPeer15clearCacheStateEvE20kalloc_type_view_502
+ __ZZN15IO80211AWDLPeer21setStateForCachedPeerEvE20kalloc_type_view_515
+ __ZZN15IO80211AWDLPeer21setStateForCachedPeerEvE20kalloc_type_view_522
+ __ZZN15IO80211AWDLPeer25initWithAddressAndManagerEPKhP22IO80211AWDLPeerManagerE20kalloc_type_view_372
+ __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1307
+ __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1350
+ __ZZN16IO80211BSSBeacon4freeEvE21kalloc_type_view_1366
+ __ZZN17IO80211BssManager15initwithOptionsEP11CCLogStreamP21IO80211ScanCacheStoreE20kalloc_type_view_144
+ __ZZN17IO80211BssManager4freeEvE20kalloc_type_view_167
+ __ZZN21IO80211NANAttributeTx15initWithManagerEP21IO80211NANPeerManagerE21kalloc_type_view_1396
+ __ZZN21IO80211NANAttributeTx4freeEvE21kalloc_type_view_1410
+ __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19420
+ __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19432
+ __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19456
+ __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19468
+ __ZZN22IO80211AWDLPeerManager22initAWDLStateTrackInfoEvE22kalloc_type_view_24970
+ __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_40689
+ __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_40673
+ __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30601
+ __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30631
+ __ZZN27IO80211NANDataPathInitiator4initEP21IO80211NANPeerManagerP18IO80211PeerManager22apple80211_nan_dp_rolePvE19kalloc_type_view_46
- __ZN22IO80211AWDLPeerManager11exitProModeE17proModeExitReasonP15IO80211AWDLPeer
- __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1814
- __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1832
- __ZZN15IO80211AWDLPeer13freeResourcesEvE20kalloc_type_view_456
- __ZZN15IO80211AWDLPeer13freeResourcesEvE20kalloc_type_view_461
- __ZZN15IO80211AWDLPeer13freeResourcesEvE20kalloc_type_view_466
- __ZZN15IO80211AWDLPeer15clearCacheStateEvE20kalloc_type_view_491
- __ZZN15IO80211AWDLPeer15clearCacheStateEvE20kalloc_type_view_496
- __ZZN15IO80211AWDLPeer21setStateForCachedPeerEvE20kalloc_type_view_509
- __ZZN15IO80211AWDLPeer21setStateForCachedPeerEvE20kalloc_type_view_516
- __ZZN15IO80211AWDLPeer25initWithAddressAndManagerEPKhP22IO80211AWDLPeerManagerE20kalloc_type_view_369
- __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1302
- __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1345
- __ZZN16IO80211BSSBeacon4freeEvE21kalloc_type_view_1361
- __ZZN17IO80211BssManager15initwithOptionsEP11CCLogStreamP21IO80211ScanCacheStoreE20kalloc_type_view_142
- __ZZN17IO80211BssManager4freeEvE20kalloc_type_view_165
- __ZZN21IO80211NANAttributeTx15initWithManagerEP21IO80211NANPeerManagerE21kalloc_type_view_1390
- __ZZN21IO80211NANAttributeTx4freeEvE21kalloc_type_view_1404
- __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19415
- __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19427
- __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19451
- __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19463
- __ZZN22IO80211AWDLPeerManager22initAWDLStateTrackInfoEvE22kalloc_type_view_24953
- __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_40670
- __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_40654
- __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30584
- __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30614
- __ZZN27IO80211NANDataPathInitiator4initEP21IO80211NANPeerManagerP18IO80211PeerManager22apple80211_nan_dp_rolePvE19kalloc_type_view_47
CStrings:
+ "\"IO80211_kexts-1585.70\""
+ "%s: ERROR: band %d num_channels %u exceeds max %u\n"
+ "%s: ERROR: source num_channels %u exceeds max %u\n"
+ "%s[%d] AF parse RECOVERED for peer %02X:%02X:%02X:%02X:%02X:%02X after %u consecutive errors\n"
+ "%s[%d] AWDL AF parse error for peer %02X:%02X:%02X:%02X:%02X:%02X reason=%u\n"
+ "%s[%d] AWDL peer %02X:%02X:%02X:%02X:%02X:%02X AFs:%u but no postAFToP2pd ever (reachability=%u, peerPresencePosted=%s)\n"
+ "%s[%d]: P2P-Concur: Alert: AirDrop while AWDL is adopting NAN Chs (%d, %d), overriding..\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Connectivity/IO80211BSSBeacon.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Connectivity/IO80211Gas/IO80211GASDefragFsm.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Connectivity/IO80211Scan/IO80211ScanCacheStore.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Connectivity/IO80211ScanManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LQMData.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211WCL/WCLJoin/WCLJoinManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jtmrIv/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
+ "222211222222222222122222222222222222221222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222211222222222222211222"
+ "Caught invalid WPS IE"
+ "ERROR: %s: REJECTED non-spec WLAN Infra attribute: channel=%u op_class=%u bandwidth=%u — clearing peer infra state\n"
+ "ERROR: %s: peer is null or not IO80211NANPeer — skipping attribute\n"
+ "IO80211_kexts-1585.70"
+ "Jul 14 2026 21:23:19"
+ "Mode"
+ "[ik] %s@%d:Caught invalid WPS IE"
+ "[ik] %s@%d:Force beacon period to %u"
+ "[ik] %s@%d:Invalid WPS IE length %d, offset %d, totalLen %d\n"
+ "allocateChannelSlots"
+ "getCurrentBeaconPeriod"
+ "parseWpsIE"
+ "peerInfraBW"
+ "peerInfraBand"
+ "peerInfraChannel"
+ "recordParseError"
+ "recordParseSuccess"
+ "saveNANExtInfraAttribute"
+ "selfInfraBW"
+ "selfInfraBand"
+ "selfInfraChannel"
- "\"IO80211_kexts-1585.62\""
- "%s: dpId %d skipping LLW setup, NDP terminating (state=%d)\n"
- "%s::%s: AirDrop service %s, overrideNAN %d\n"
- "%s[%d]: P2P-Concur: Alert: AirDrop while AWDL is adopting NAN Chs, overriding..\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Connectivity/IO80211Gas/IO80211GASDefragFsm.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Connectivity/IO80211Scan/IO80211ScanCacheStore.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Connectivity/IO80211ScanManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LQMData.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211WCL/WCLJoin/WCLJoinManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
- "2222112222222222221222222222222222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222112222222222222112"
- "ADDED"
- "DELETED"
- "ERROR: NDC attribute length %u < minimum fixed header size %u\n"
- "ERROR: NDC map_id %u exceeds maximum %u\n"
- "ERROR: NDC remaining length %u < minimum schedule entry size %u\n"
- "ERROR: NDC schedule entry size %u (header %u + bitmap %u) exceeds remaining %u\n"
- "ERROR: NDC time_bitmap_len %u exceeds destination buffer size %zu\n"
- "ERROR: Too many unique map_ids in NDC attribute\n"
- "IO80211_kexts-1585.62"
- "Jun 29 2026 21:06:44"
- "kProModeMode"
- "kProModePeerInfraBW"
- "kProModePeerInfraBand"
- "kProModePeerInfraChannel"
- "kProModeSelfInfraBW"
- "kProModeSelfInfraBand"
- "kProModeSelfInfraChannel"
```
