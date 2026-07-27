## com.apple.iokit.IO80211Family

> `com.apple.iokit.IO80211Family`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-1561.3.0.0.0
+1566.5.0.0.0
   __TEXT.__os_log: 0x9947
   __TEXT.__const: 0x12fd8
-  __TEXT.__cstring: 0x9309b
-  __TEXT_EXEC.__text: 0x261d28
+  __TEXT.__cstring: 0x933bd
+  __TEXT_EXEC.__text: 0x2622a8
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x5a60
   __DATA.__common: 0x2038

   __DATA_CONST.__kalloc_var: 0xa00
   Functions: 12726
   Symbols:   16641
-  CStrings:  14415
+  CStrings:  14422
 
Symbols:
+ __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1868
+ __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1916
+ __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1089
+ __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1137
+ __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1527
+ __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1553
+ __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1497
+ __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1516
+ __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1796
+ __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1814
+ __ZZN21IO80211NANAttributeTx15initWithManagerEP21IO80211NANPeerManagerE21kalloc_type_view_1359
+ __ZZN21IO80211NANAttributeTx4freeEvE21kalloc_type_view_1373
+ __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19169
+ __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19181
+ __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19205
+ __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19217
+ __ZZN22IO80211AWDLPeerManager22initAWDLStateTrackInfoEvE22kalloc_type_view_24656
+ __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_40050
+ __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_40034
+ __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30238
+ __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30268
- __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1867
- __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1915
- __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1088
- __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1136
- __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1526
- __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1552
- __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1496
- __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1515
- __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1783
- __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1801
- __ZZN21IO80211NANAttributeTx15initWithManagerEP21IO80211NANPeerManagerE21kalloc_type_view_1313
- __ZZN21IO80211NANAttributeTx4freeEvE21kalloc_type_view_1327
- __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19165
- __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19177
- __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19201
- __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19213
- __ZZN22IO80211AWDLPeerManager22initAWDLStateTrackInfoEvE22kalloc_type_view_24652
- __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_40046
- __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_40030
- __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30234
- __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30264
Functions:
~ __Z27IO80211_io80211isDebuggablev : 224 -> 232
~ __ZN15IO80211AWDLPeer17updateAwdlChanSeqEN7libkern11bounded_ptrI19awdl_chan_seq_info2N9os_detail21panic_trapping_policyEEE : 1552 -> 1564
~ __ZN15IO80211AWDLPeer5printEP12userPrintCtx : 3796 -> 3968
~ __ZN15IO80211AWDLPeer17actionFrameReportEP24actionFrameReportContext : 11272 -> 11436
~ __ZN15IO80211AWDLPeer15parseNanSyncTlvERK19IO80211BufferCursor : 296 -> 748
~ __ZN22IO80211AWDLPeerManager20reportDataPathEventsEjPvm : 13220 -> 13244
~ __ZL13setCIPHER_KEYP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211req : 448 -> 472
~ __ZN17IO80211Controller19io80211isDebuggableEPb : 236 -> 248
~ __ZN21IO80211NANPeerManager35setNANUserConfiguredChannelSequenceEP45apple80211_nan_user_configured_radio_schedule : 176 -> 260
~ __ZN14IO80211NANPeer14handleBeaconRxEP38apple80211_nan_beacon_recvd_event_data : 1648 -> 1712
~ __Z16_getNANAttributehPht : 60 -> 92
~ __ZL32validateNANAvailabilityAttributeP24apple80211_nan_attribute : 1024 -> 1080
~ __ZL36validateNANElementContainerAttributeP24apple80211_nan_attribute : 120 -> 160
~ __ZN30IO80211NANRadioResourceManager22initializeCCALogBufferEv : 312 -> 308
~ __ZN30IO80211NANRadioResourceManager25createPrioritizedScheduleEv : 224 -> 232
~ __ZN30IO80211NANRadioResourceManager20allocateChannelSlotsEP32apple80211_channel_schedule_listS1_Ph : 268 -> 372
~ __ZN30IO80211NANRadioResourceManager22prepareSDBAvailabilityEv : 904 -> 912
~ __ZN30IO80211NANRadioResourceManager25prepareNonSDBAvailabilityEv : 1968 -> 1980
~ __ZN30IO80211NANRadioResourceManager32saveCurrentCommitedRawTimebitmapEP37apple80211_nan_committed_availabilityP38apple80211_nan_committed_base_schedule : 872 -> 888
~ __ZN27IO80211NANDataPathInitiator27handleDataPathResponseRecvdEP39apple80211_nan_dp_resp_recvd_event_data : 1972 -> 2032
~ __ZN27IO80211NANDataPathResponder26handleDataPathRequestRecvdEP42apple80211_nan_dp_request_recvd_event_data : 2100 -> 2160
CStrings:
+ "\"IO80211_kexts-1566.5\""
+ "%s %02X:%02X:%02X:%02X:%02X:%02X | %3s | %02X:%02X:%02X:%02X:%02X:%02X %5u | %2u | %5u | %5u | %02X:%02X:%02X:%02X:%02X:%02X | %5u | %5u | %5u | %5u | %3d | %3d |%s%8s%s|%7u| %3s | %2X | "
+ "%s: ACCEPTED NTLV from peer %02X:%02X:%02X:%02X:%02X:%02X peerHC=%u ntlvHC=%u amMet=%u origMet=%u src=%02X:%02X:%02X:%02X:%02X:%02X AM=%02X:%02X:%02X:%02X:%02X:%02X AMBTT=0x%x TSF=0x%x_%x\n"
+ "%s: ERROR: band %d num_channels %u exceeds max %u\n"
+ "%s: ERROR: source num_channels %u exceeds max %u\n"
+ "%s: REJECTING NTLV from peer %02X:%02X:%02X:%02X:%02X:%02X peerHC=%u ntlvHC=%u amMet=%u origMet=%u src=%02X:%02X:%02X:%02X:%02X:%02X AM=%02X:%02X:%02X:%02X:%02X:%02X AMBTT=0x%x TSF=0x%x_%x != root=%02X:%02X:%02X:%02X:%02X:%02X\n"
+ "%s: clearing stale NTLV buffer for peer %02X:%02X (bcast AF without NTLV)\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Connectivity/IO80211Gas/IO80211GASDefragFsm.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Connectivity/IO80211Scan/IO80211ScanCacheStore.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Connectivity/IO80211ScanManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211WCL/WCLJoin/WCLJoinManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DA3Fx3/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
+ "IO80211_kexts-1566.5"
+ "Jul 13 2026 19:58:50"
+ "allocateChannelSlots"
- "\"IO80211_kexts-1561.3\""
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Connectivity/IO80211Gas/IO80211GASDefragFsm.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Connectivity/IO80211Scan/IO80211ScanCacheStore.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Connectivity/IO80211ScanManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211WCL/WCLJoin/WCLJoinManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.vI3Of6/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
- "IO80211_kexts-1561.3"
- "Jun 21 2026 19:07:02"
```
