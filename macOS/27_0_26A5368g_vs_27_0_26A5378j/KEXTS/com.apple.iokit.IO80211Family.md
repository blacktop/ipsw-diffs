## com.apple.iokit.IO80211Family

> `com.apple.iokit.IO80211Family`

```diff

   __TEXT.__os_log: 0x9e36
   __TEXT.__const: 0x2bec0
-  __TEXT.__cstring: 0x97c76
-  __TEXT_EXEC.__text: 0x277348
+  __TEXT.__cstring: 0x98784
+  __TEXT_EXEC.__text: 0x2786cc
   __TEXT_EXEC.__auth_stubs: 0x1420
   __DATA.__data: 0x5ec8
   __DATA.__common: 0x2c70
   __DATA.__bss: 0x3448
   __DATA_CONST.__mod_init_func: 0x550
   __DATA_CONST.__mod_term_func: 0x550
-  __DATA_CONST.__const: 0x3a0c8
+  __DATA_CONST.__const: 0x3a0d8
   __DATA_CONST.__kalloc_type: 0x9e00
   __DATA_CONST.__kalloc_var: 0xa00
   __DATA_CONST.__auth_got: 0xa10
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x20
-  Functions: 13073
-  Symbols:   20496
-  CStrings:  15048
+  Functions: 13080
+  Symbols:   20516
+  CStrings:  15095
 
Sections:
~ __TEXT.__const : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ __FUNCTION__._ZN11IO80211Glue15routeEventToWclEjPvm
+ __FUNCTION__._ZN20IO80211P2PSupervisor16enterSteadyStateEv
+ __FUNCTION__._ZN20IO80211P2PSupervisor16getNANDeviceInfoEP26apple80211_nan_device_info
+ __FUNCTION__._ZN21IO80211NANPeerManager21setNANMulticastPeerOpEP32apple80211_nan_multicast_peer_op
+ __FUNCTION__._ZN25IO80211P2PSteeringManager24notifyInfra6GSteerStatusEi
+ __Z34apple80211getNAN_MULTICAST_PEER_OPP23IO80211SkywalkInterfaceP32apple80211_nan_multicast_peer_op
+ __Z34apple80211setNAN_MULTICAST_PEER_OPP23IO80211SkywalkInterfaceP32apple80211_nan_multicast_peer_op
+ __ZL24setNAN_MULTICAST_PEER_OPP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211req
+ __ZN11IO80211Glue22drainPendingEventQueueEv
+ __ZN13WCLBssManager13getCurrentNetEP22apple80211_scan_result
+ __ZN13WCLNetManager16handleAssocFrameER20bulletinBoardMessage
+ __ZN14WCLRoamManager23configureRoamingProfileEPKc
+ __ZN18IO80211RoamProfile13addRoamOffsetEjb
+ __ZN18IO80211RoamProfile16removeRoamOffsetEjb
+ __ZN21IO80211NANPeerManager21setNANMulticastPeerOpEP32apple80211_nan_multicast_peer_op
+ __ZN21IO80211RangingManager29dispatchRestartPendingRequestEv
+ __ZN22IO80211AWDLPeerManager11isInProModeEv
+ __ZN22IO80211AWDLPeerManager13has6GDataPeerEP15IO80211AWDLPeer
+ __ZN22IO80211AWDLPeerManager16has6GAirDropPeerERbP15IO80211AWDLPeer
+ __ZN22IO80211AWDLPeerManager20getNumOfAirDropPeersERtS0_S0_S0_P15IO80211AWDLPeer
+ __ZN22IO80211AWDLPeerManager21isForcedMasterEnabledEv
+ __ZN22IO80211AWDLPeerManager34updateP2PRealTimeStateAndNotifyWCLEv
+ __ZN25IO80211P2PSteeringManager24notifyInfra6GSteerStatusEi
+ __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1868
+ __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1916
+ __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1095
+ __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1143
+ __ZZL14_allocPeerNodeP25apple80211_ranging_peer_tjbE20kalloc_type_view_120
+ __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1527
+ __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1553
+ __ZZL17_allocRequestNodeP34apple80211_ranging_start_request_tE19kalloc_type_view_84
+ __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1497
+ __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1516
+ __ZZN11IO80211Glue13freeResourcesEvE20kalloc_type_view_183
+ __ZZN11IO80211Glue15initWithOptionsEP23IO80211SkywalkInterfaceE20kalloc_type_view_231
+ __ZZN13WCLNetManager15initWithOptionsEP13WCLControllerP16WCLBulletinBoardE20kalloc_type_view_279
+ __ZZN13WCLNetManager4freeEvE20kalloc_type_view_224
+ __ZZN14WCLRoamManager15initWithOptionsEP13WCLControllerP16WCLBulletinBoardE20kalloc_type_view_201
+ __ZZN14WCLRoamManager4freeEvE20kalloc_type_view_153
+ __ZZN20IO80211P2PSupervisor17initWithInterfaceEP23IO80211VirtualInterfaceE20kalloc_type_view_116
+ __ZZN20IO80211P2PSupervisor17initWithInterfaceEP23IO80211VirtualInterfaceE20kalloc_type_view_171
+ __ZZN20IO80211P2PSupervisor4freeEvE20kalloc_type_view_201
+ __ZZN20IO80211P2PSupervisor4freeEvE20kalloc_type_view_207
+ __ZZN21IO80211NANAttributeTx15initWithManagerEP21IO80211NANPeerManagerE21kalloc_type_view_1390
+ __ZZN21IO80211NANAttributeTx4freeEvE21kalloc_type_view_1404
+ __ZZN21IO80211RangingManager10_freePeersEbE20kalloc_type_view_270
+ __ZZN21IO80211RangingManager10_freePeersEbE20kalloc_type_view_279
+ __ZZN21IO80211RangingManager13_freeRequestsEbE20kalloc_type_view_253
+ __ZZN21IO80211RangingManager13_freeRequestsEbE20kalloc_type_view_255
+ __ZZN21IO80211RangingManager13rangingResultEP25apple80211_ranging_peer_tE21kalloc_type_view_1611
+ __ZZN21IO80211RangingManager18initWithControllerEP17IO80211ControllerE20kalloc_type_view_165
+ __ZZN21IO80211RangingManager19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_1394
+ __ZZN21IO80211RangingManager19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_1401
+ __ZZN21IO80211RangingManager19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_1404
+ __ZZN21IO80211RangingManager4freeEvE20kalloc_type_view_311
+ __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19415
+ __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19427
+ __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19451
+ __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19463
+ __ZZN22IO80211AWDLPeerManager13freeResourcesEvE21kalloc_type_view_2653
+ __ZZN22IO80211AWDLPeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP10ether_addrE21kalloc_type_view_2129
+ __ZZN22IO80211AWDLPeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP10ether_addrE21kalloc_type_view_2607
+ __ZZN22IO80211AWDLPeerManager22initAWDLStateTrackInfoEvE22kalloc_type_view_24953
+ __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_40670
+ __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_40654
+ __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30584
+ __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30614
+ __ZZN22IO80211AWDLPeerManager4freeEvE21kalloc_type_view_2699
+ __ZZN22IO80211AWDLPeerManager4freeEvE21kalloc_type_view_2710
+ __ZZN24IO80211RangingManagerExt13rangingResultEP25apple80211_ranging_peer_tE21kalloc_type_view_2516
+ __ZZN24IO80211RangingManagerExt13rangingResultEP25apple80211_ranging_peer_tE21kalloc_type_view_2522
+ __ZZN24IO80211RangingManagerExt16getRangingResultEP35apple80211_ranging_peer_list_data_tbE21kalloc_type_view_2330
+ __ZZN24IO80211RangingManagerExt16getRangingResultEP35apple80211_ranging_peer_list_data_tbE21kalloc_type_view_2332
+ __ZZN24IO80211RangingManagerExt17_rangingCompletedEP10ether_addrP35io80211_ranging_manager_result_nodeE21kalloc_type_view_2436
+ __ZZN24IO80211RangingManagerExt17_rangingCompletedEP10ether_addrP35io80211_ranging_manager_result_nodeE21kalloc_type_view_2438
+ __ZZN24IO80211RangingManagerExt19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_2051
+ __ZZN24IO80211RangingManagerExt19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_2063
+ __ZZN24IO80211RangingManagerExt19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_2068
+ __ZZN25IO80211NANDataPathManager17deleteNanInfoListEPP13ndp_info_nodeE21kalloc_type_view_5100
+ __ZZN25IO80211NANDataPathManager19addEntryNanInfoListEPP13ndp_info_nodePhtjjE21kalloc_type_view_5049
+ __ZZN25IO80211P2PSteeringManager17initWithInterfaceEP20IO80211P2PSupervisorE20kalloc_type_view_148
+ __ZZN25IO80211P2PSteeringManager4freeEvE20kalloc_type_view_186
+ __ZZN27IO80211NANDataPathResponder4freeEvE19kalloc_type_view_87
- __FUNCTION__._ZN21IO80211NANPeerManager25setNANRemoveMulticastPeerEP36apple80211_nan_remove_multicast_peer
- __FUNCTION__._ZN22IO80211AWDLPeerManager28enableForceMasterRTGElectionEP15IO80211AWDLPeer
- __FUNCTION__._ZN25IO80211NANDataPathManager25configureLowLatencyParamsEP10ether_addrbh
- __Z38apple80211getNAN_REMOVE_MULTICAST_PEERP23IO80211SkywalkInterfaceP36apple80211_nan_remove_multicast_peer
- __Z38apple80211setNAN_REMOVE_MULTICAST_PEERP23IO80211SkywalkInterfaceP36apple80211_nan_remove_multicast_peer
- __ZL28setNAN_REMOVE_MULTICAST_PEERP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211req
- __ZN14WCLRoamManager13setRoamOffsetER20bulletinBoardMessage
- __ZN14WCLRoamManager23configureRoamingProfileEv
- __ZN18IO80211RoamProfile13addRoamOffsetEj
- __ZN18IO80211RoamProfile16removeRoamOffsetEj
- __ZN21IO80211NANPeerManager25setNANRemoveMulticastPeerEP36apple80211_nan_remove_multicast_peer
- __ZN22IO80211AWDLPeerManager13has6GDataPeerEv
- __ZN22IO80211AWDLPeerManager16has6GAirDropPeerERb
- __ZN22IO80211AWDLPeerManager20getNumOfAirDropPeersERtS0_S0_S0_
- __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1861
- __ZZL10setNAN_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1909
- __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1088
- __ZZL11setAWDL_CTLP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1136
- __ZZL14_allocPeerNodeP25apple80211_ranging_peer_tjbE20kalloc_type_view_113
- __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1520
- __ZZL16setRANGING_STARTP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1546
- __ZZL17_allocRequestNodeP34apple80211_ranging_start_request_tE19kalloc_type_view_77
- __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1490
- __ZZL17setRANGING_ENABLEP17IO80211ControllerP23IO80211SkywalkInterfaceP20IO80211APIUserClientP13apple80211reqE21kalloc_type_view_1509
- __ZZN11IO80211Glue13freeResourcesEvE20kalloc_type_view_171
- __ZZN11IO80211Glue15initWithOptionsEP23IO80211SkywalkInterfaceE20kalloc_type_view_211
- __ZZN13WCLNetManager15initWithOptionsEP13WCLControllerP16WCLBulletinBoardE20kalloc_type_view_274
- __ZZN13WCLNetManager4freeEvE20kalloc_type_view_219
- __ZZN14WCLRoamManager15initWithOptionsEP13WCLControllerP16WCLBulletinBoardE20kalloc_type_view_202
- __ZZN14WCLRoamManager4freeEvE20kalloc_type_view_154
- __ZZN20IO80211P2PSupervisor17initWithInterfaceEP23IO80211VirtualInterfaceE20kalloc_type_view_108
- __ZZN20IO80211P2PSupervisor17initWithInterfaceEP23IO80211VirtualInterfaceE20kalloc_type_view_163
- __ZZN20IO80211P2PSupervisor4freeEvE20kalloc_type_view_193
- __ZZN20IO80211P2PSupervisor4freeEvE20kalloc_type_view_199
- __ZZN21IO80211NANAttributeTx15initWithManagerEP21IO80211NANPeerManagerE21kalloc_type_view_1327
- __ZZN21IO80211NANAttributeTx4freeEvE21kalloc_type_view_1341
- __ZZN21IO80211RangingManager10_freePeersEbE20kalloc_type_view_251
- __ZZN21IO80211RangingManager10_freePeersEbE20kalloc_type_view_260
- __ZZN21IO80211RangingManager13_freeRequestsEbE20kalloc_type_view_234
- __ZZN21IO80211RangingManager13_freeRequestsEbE20kalloc_type_view_236
- __ZZN21IO80211RangingManager13rangingResultEP25apple80211_ranging_peer_tE21kalloc_type_view_1589
- __ZZN21IO80211RangingManager18initWithControllerEP17IO80211ControllerE20kalloc_type_view_158
- __ZZN21IO80211RangingManager19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_1372
- __ZZN21IO80211RangingManager19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_1379
- __ZZN21IO80211RangingManager19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_1382
- __ZZN21IO80211RangingManager4freeEvE20kalloc_type_view_289
- __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19363
- __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19375
- __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19399
- __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19411
- __ZZN22IO80211AWDLPeerManager13freeResourcesEvE21kalloc_type_view_2650
- __ZZN22IO80211AWDLPeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP10ether_addrE21kalloc_type_view_2126
- __ZZN22IO80211AWDLPeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP10ether_addrE21kalloc_type_view_2604
- __ZZN22IO80211AWDLPeerManager22initAWDLStateTrackInfoEvE22kalloc_type_view_24901
- __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_40504
- __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_40488
- __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30532
- __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30562
- __ZZN22IO80211AWDLPeerManager4freeEvE21kalloc_type_view_2696
- __ZZN22IO80211AWDLPeerManager4freeEvE21kalloc_type_view_2707
- __ZZN24IO80211RangingManagerExt13rangingResultEP25apple80211_ranging_peer_tE21kalloc_type_view_2509
- __ZZN24IO80211RangingManagerExt13rangingResultEP25apple80211_ranging_peer_tE21kalloc_type_view_2515
- __ZZN24IO80211RangingManagerExt16getRangingResultEP35apple80211_ranging_peer_list_data_tbE21kalloc_type_view_2323
- __ZZN24IO80211RangingManagerExt16getRangingResultEP35apple80211_ranging_peer_list_data_tbE21kalloc_type_view_2325
- __ZZN24IO80211RangingManagerExt17_rangingCompletedEP10ether_addrP35io80211_ranging_manager_result_nodeE21kalloc_type_view_2429
- __ZZN24IO80211RangingManagerExt17_rangingCompletedEP10ether_addrP35io80211_ranging_manager_result_nodeE21kalloc_type_view_2431
- __ZZN24IO80211RangingManagerExt19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_2044
- __ZZN24IO80211RangingManagerExt19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_2054
- __ZZN24IO80211RangingManagerExt19freePeerNodeTimeoutEP8OSObjectP18IO80211TimerSourceE21kalloc_type_view_2056
- __ZZN25IO80211NANDataPathManager17deleteNanInfoListEPP13ndp_info_nodeE21kalloc_type_view_5085
- __ZZN25IO80211NANDataPathManager19addEntryNanInfoListEPP13ndp_info_nodePhtjjE21kalloc_type_view_5034
- __ZZN25IO80211P2PSteeringManager17initWithInterfaceEP20IO80211P2PSupervisorE20kalloc_type_view_146
- __ZZN25IO80211P2PSteeringManager4freeEvE20kalloc_type_view_184
- __ZZN27IO80211NANDataPathResponder4freeEvE19kalloc_type_view_85
CStrings:
+ "\"IO80211_kexts-1585.62\""
+ "%s [RTG-SYNC] AssistedDiscovery active, deferring RTG forced master %02X:%02X:%02X:%02X:%02X:%02X until AD exits\n"
+ "%s [RTG-SYNC] awdlElectionOnHostEnabled is disabled, skipping RTG forced master %02X:%02X:%02X:%02X:%02X:%02X\n"
+ "%s: AD exited, deferred RTG forced master %02X:%02X:%02X:%02X:%02X:%02X no longer in peer list, dropping\n"
+ "%s: AD exited, replaying deferred RTG forced master %02X:%02X:%02X:%02X:%02X:%02X\n"
+ "%s: AssistedDiscovery overriding active RTG forced master %02X:%02X:%02X:%02X:%02X:%02X, will replay on AD exit\n"
+ "%s: ERROR: invalid operation %u\n"
+ "%s: ERROR: invalid peer count %u\n"
+ "%s: ERROR: null data\n"
+ "%s: ERROR: setIOCTL failed ret=%d\n"
+ "%s: P2P-Concurrency: AWDL has been enabled for %u ms, re-entering warmup for forced master\n"
+ "%s: P2P-Concurrency: forced-master warmup hold timed out after %u ms (cap=%u), forcing AD exit + steady state\n"
+ "%s: P2P-Concurrency: warmup timeout elapsed but AssistedDiscovery forced master active, holding warmup (%u/%u ms)\n"
+ "%s: Skipping NAN AM sync — AssistedDiscovery forced master active\n"
+ "%s: enterWarmupState failed (rv=0x%x), aborting forced master setup (RTG untouched)\n"
+ "%s: forced master active, re-entering warmup to suppress NAN FW election\n"
+ "%s: forced master cleared, concurrency already in steady state\n"
+ "%s: forced master cleared, concurrency is OFF (torn down during AD), no recovery\n"
+ "%s: forced master cleared, resuming concurrency steady state\n"
+ "%s: forced master cleared, unexpected concurrency state=%d, forcing steady state\n"
+ "%s: operation=%u count=%u mcast=%02x:%02x:%02x:%02x:%02x:%02x\n"
+ "%s: startRanging alloc req fail \n\n"
+ "%s:%u ERROR: _ensemblePeerListOSArray is nil, not adding peer to RTG\n"
+ "%s:%u: sending UMI#%u to Peer %02X:%02X:%02X:%02X:%02X:%02X at (AW: %u Slot: %u UnicastOptions 0x%x options2 0x%x) \n"
+ "%s::%s(%d) destroying reporters, manager RC=%u %s\n"
+ "%s::%s(%d) reporters destroyed, deferring addPeerOp (RC=%u deferred=%u) %s\n"
+ "%s::%s(%d) reporters destroyed, deferring removePeerOp (RC=%u deferred=%u) %s\n"
+ "%s:[%d]:  peer %02X:%02X:%02X:%02X:%02X:%02X. being deleted\n"
+ "%s[%d] : Roam Completed, Status %d wasNan6GSteer=%d\n"
+ "%s[%d] EARLY RETURN nanPM=%p virtIf=%p — event NOT posted\n"
+ "%s[%d] Peer %02X:%02X:%02X:%02X:%02X:%02X already exited ProMode\n"
+ "%s[%d] Posting NAN_INFRA_6G_STEER_STATUS result=%d reason=%d roamStatus=%d\n"
+ "%s[%d] Roam Complete (SteerInProgress: %d), roamStatus:%d was6GSteer=%d\n"
+ "%s[%d] exit ProMode for %02X:%02X:%02X:%02X:%02X:%02X\n"
+ "%s[%d] inProMode %d peer %p\n"
+ "%s[%d] postMessage returned 0x%x (%s)\n"
+ "%s[%u] ERROR: Peer %02X:%02X:%02X:%02X:%02X:%02X deleted after sleep/wake during traffic registration (mgr RC=%u)\n"
+ "%s[%u] ERROR: Peer %02X:%02X:%02X:%02X:%02X:%02X was deleted (mgr RC=%u)\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Connectivity/IO80211Gas/IO80211GASDefragFsm.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Connectivity/IO80211Scan/IO80211ScanCacheStore.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Connectivity/IO80211ScanManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LQMData.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211WCL/WCLJoin/WCLJoinManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wQyAyG/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
+ "111111111111111222222211222222222222222222222222222222222222222221222"
+ "1111222211121112"
+ "122222222211122222222222222222222222222222222222222222222222222222222222222222222121112212"
+ "APPLE80211_IOC_NAN_MULTICAST_PEER_OP"
+ "APPLE80211_M_NAN_INFRA_6G_STEER_STATUS"
+ "ERROR: NDC attribute length %u < minimum fixed header size %u\n"
+ "ERROR: NDC map_id %u exceeds maximum %u\n"
+ "ERROR: NDC remaining length %u < minimum schedule entry size %u\n"
+ "ERROR: NDC schedule entry size %u (header %u + bitmap %u) exceeds remaining %u\n"
+ "ERROR: NDC time_bitmap_len %u exceeds destination buffer size %zu\n"
+ "ERROR: Too many unique map_ids in NDC attribute\n"
+ "IO80211_kexts-1585.62"
+ "Jun 29 2026 21:06:44"
+ "[wcl] %s@%d:Assoc frame received while connected, possible FW debounce\n"
+ "[wcl] %s@%d:glue is not active\n"
+ "[wcl] %s@%d:routeEventToWcl: glue is not active, dropping msg<%u>\n"
+ "assocTimerBeat"
+ "countryCodeChanged"
+ "notifyInfra6GSteerStatus"
+ "notifyPeerRemovedFromCache"
+ "other mgr req"
+ "processPendingEventQueue"
+ "routeEventToWcl"
+ "setNANMulticastPeerOp"
- "\"IO80211_kexts-1585.56\""
- "%s [RTG-SYNC] awdlElectionOnHostEnabled is disabled\n"
- "%s:%u: sending UMI#%u to Peer %02X:%02X:%02X:%02X:%02X:%02X at (AW: %u Slot: %u UnicastOptions 0x%x) \n"
- "%s:[%d]:  peer %02X:%02X:%02X:%02X:%02X:%02X. being deleted, not sending UMI\n"
- "%s[%d] Roam Complete (SteerInProgress: %d), roamStatus:%d\n"
- "%s[%u] ERROR: Peer %02X:%02X:%02X:%02X:%02X:%02X deleted after sleep/wake during traffic registration\n"
- "%s[%u] ERROR: Peer %02X:%02X:%02X:%02X:%02X:%02X was deleted\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Connectivity/IO80211Gas/IO80211GASDefragFsm.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Connectivity/IO80211Scan/IO80211ScanCacheStore.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Connectivity/IO80211ScanManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLMulticastPeer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211AWDLPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSteeringManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211P2PSupervisor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/AWDL/IO80211ServiceRequestDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211DynamicBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/Buffers/IO80211StaticBufferPool.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/IO80211Controller.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/IO80211ControllerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/IO80211InfraInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/IO80211InterfaceMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/IO80211PacketDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/IO80211Peer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/IO80211PeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/IO80211PeerMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/IO80211SkywalkInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/IO80211VirtualInterface.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LQMData.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/Infra/IO80211LinkRecovery.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathInitiator.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/NAN/DataPathManager/IO80211NANDataPathManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/NAN/DiscoveryEngine/IO80211NANDiscoveryEngine.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/NAN/Miscellaneous/IO80211NANUtils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANDataInterfacePeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeer.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/NAN/PeerManager/IO80211NANPeerManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceDescriptor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/NAN/ServiceManager/IO80211NANServiceManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/NAN/SynchronizationEngine/IO80211NANSyncEngine.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/UserClients/IO80211AsyncUserClientParameters.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/Utils/IO80211CommandQueue.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/Utils/IO80211FlowQueueDatabase.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/Utils/IO80211Util.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_get_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlers.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211Family/ioctls/apple80211_ioctl_set_handlersLegacy.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211WCL/WCLDeauthDisassoc.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211WCL/WCLJoin/WCLJoinManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211WCL/WCLNearbyDeviceDiscoveryManager.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.128WJU/Sources/IO80211_kexts/IO80211WCL/WCLNetManager.cpp"
- "11111111111111122222221122222222222222222222222222222222222222221222"
- "111122221112111"
- "12222222221112222222222222222222222222222222222222222222222222222222222222222222121112212"
- "APPLE80211_IOC_NAN_REMOVE_MULTICAST_PEER"
- "IO80211_kexts-1585.56"
- "Jun 15 2026 22:38:51"
- "[wcl] %s@%d:Roam profile is supported. Re-enable roam engine...\n"
- "setNANRemoveMulticastPeer"

```
