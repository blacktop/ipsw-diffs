## com.apple.iokit.IO80211Family

> `com.apple.iokit.IO80211Family`

```diff

-1585.80.0.0.0
+1587.10.0.0.0
   __TEXT.__os_log: 0x9e58
   __TEXT.__const: 0x2bec0
-  __TEXT.__cstring: 0x98b09
-  __TEXT_EXEC.__text: 0x281278
+  __TEXT.__cstring: 0x999ac
+  __TEXT_EXEC.__text: 0x27c304
   __TEXT_EXEC.__auth_stubs: 0x1420
   __DATA.__data: 0x5ec8
-  __DATA.__common: 0x3160
-  __DATA.__bss: 0x3448
+  __DATA.__common: 0x50c8
+  __DATA.__bss: 0x14d8
   __DATA_CONST.__mod_init_func: 0x558
   __DATA_CONST.__mod_term_func: 0x558
-  __DATA_CONST.__const: 0x3a378
+  __DATA_CONST.__const: 0x3a488
   __DATA_CONST.__kalloc_type: 0x9ec0
   __DATA_CONST.__kalloc_var: 0xa00
   __DATA_CONST.__auth_got: 0xa10
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x20
-  Functions: 13130
-  Symbols:   17152
-  CStrings:  14885
+  Functions: 13152
+  Symbols:   17176
+  CStrings:  14943
 
Symbols:
+ __FUNCTION__._ZN18IO80211PeerManager16getStringForRoleEj
+ __FUNCTION__._ZN22IO80211AWDLPeerManager15setAirDropStateEb
+ __FUNCTION__._ZN25IO80211P2PDataPathManager24clearRoleCachedPeerCountEv
+ __FUNCTION__._ZN25IO80211P2PDataPathManager27setCurrentPeerCacheSizeOnlyEj
+ __Z25getChanSwitchFromRawStatsP31apple80211_channel_switch_statsP30apple80211_channel_switch_data
+ __Z28apple80211getAGGRESSIVE_EDCAP23IO80211SkywalkInterfaceP26apple80211_aggressive_edca
+ __Z28apple80211setAGGRESSIVE_EDCAP23IO80211SkywalkInterfaceP26apple80211_aggressive_edca
+ __Z34getNanChanBoundaryStatFromRawStatsP31apple80211_channel_switch_statsP42apple80211_nan_channel_boundary_event_data
+ __ZN16IO80211BSSBeacon17isHave6gOpElementEv
+ __ZN17IO80211BssManager33runActionOnMatchingCachedNetworksEU13block_pointerFbP8OSObjectE
+ __ZN18IO80211RoamProfile23disableBlockedBandBoostEP22ExtendedRoamParameters5Bands
+ __ZN21IO80211NANPeerManager28clearNonSdbOn5GhzOnlyPendingE34apple80211_nonsdb_5ghz_only_client
+ __ZN21IO80211NANPeerManager30monitorNonSdbOn5GhzOnlyPendingEv
+ __ZN21IO80211NANPeerManager31clearAllNonSdbOn5GhzOnlyPendingEv
+ __ZN21IO80211NANPeerManager34enableNonSdbOn5GhzAvailabilityOnlyE34apple80211_nonsdb_5ghz_only_clientbb
+ __ZN21IO80211ScanCacheStore14setAuthContextER18IO80211AuthContext
+ __ZN22IO80211AWDLPeerManager15setAirDropStateEb
+ __ZN22IO80211AWDLPeerManager17sendAggresiveEdcaEb
+ __ZN22IO80211AWDLPeerManager19aggressiveEdcaTimerEP18IO80211TimerSource
+ __ZN22WCLDeviceConfiguration17isPruneBad6GBssidEv
+ __ZN23IO80211SkywalkInterface20postPeerPresenceDoneEP10ether_addrb
+ __ZN24WCLJoinCandidateSelector14removeBad6gApsEP14WCLJoinRequest
+ __ZN25IO80211P2PDataPathManager22getRoleCachedPeerCountEv
+ __ZN25IO80211P2PDataPathManager24clearRoleCachedPeerCountEv
+ __ZN25IO80211P2PDataPathManager27setCurrentPeerCacheSizeOnlyEj
+ __ZN30IO80211NANRadioResourceManager36shouldForceChannelAvailabilityUpdateE43apple80211_nan_radio_resource_change_reason
+ __ZZN11IO80211Peer20freeTxLatencyStorageEvE21kalloc_type_view_2682
+ __ZZN11IO80211Peer21allocTxLatencyStorageEvE21kalloc_type_view_2670
+ __ZZN13WCLNetManager15initWithOptionsEP13WCLControllerP16WCLBulletinBoardE20kalloc_type_view_280
+ __ZZN13WCLNetManager4freeEvE20kalloc_type_view_225
+ __ZZN14IO80211NANPeer13freeResourcesEvE20kalloc_type_view_193
+ __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1854
+ __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1872
+ __ZZN14IO80211NANPeer25initWithAddressAndManagerEPKhP18IO80211PeerManagerE20kalloc_type_view_164
+ __ZZN14WCL11axManager15freeActionFrameEPvE20kalloc_type_view_866
+ __ZZN14WCL11axManager22send11axAsrActionFrameEhhPhjE21kalloc_type_view_1166
+ __ZZN14WCL11axManager24sendHsLpEmlsrActionFrameEbbjE21kalloc_type_view_1216
+ __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1309
+ __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1352
+ __ZZN16IO80211BSSBeacon4freeEvE21kalloc_type_view_1368
+ __ZZN21IO80211NANAttributeTx15initWithManagerEP21IO80211NANPeerManagerE21kalloc_type_view_1174
+ __ZZN21IO80211NANAttributeTx4freeEvE21kalloc_type_view_1188
+ __ZZN21IO80211NANPeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP10ether_addrE20kalloc_type_view_212
+ __ZZN21IO80211NANPeerManager4freeEvE20kalloc_type_view_357
+ __ZZN21IO80211ScanCacheStore25initIO80211ScanCacheStoreER27IO80211ScanCacheStoreParamsE20kalloc_type_view_590
+ __ZZN21IO80211ScanCacheStore4freeEvE20kalloc_type_view_127
+ __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19449
+ __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19461
+ __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19485
+ __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19497
+ __ZZN22IO80211AWDLPeerManager13freeResourcesEvE21kalloc_type_view_2665
+ __ZZN22IO80211AWDLPeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP10ether_addrE21kalloc_type_view_2132
+ __ZZN22IO80211AWDLPeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP10ether_addrE21kalloc_type_view_2619
+ __ZZN22IO80211AWDLPeerManager22initAWDLStateTrackInfoEvE22kalloc_type_view_24999
+ __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_40752
+ __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_40736
+ __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30630
+ __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30660
+ __ZZN22IO80211AWDLPeerManager4freeEvE21kalloc_type_view_2712
+ __ZZN22IO80211AWDLPeerManager4freeEvE21kalloc_type_view_2723
+ __ZZN24WCLJoinCandidateSelector28initWCLJoinCandidateSelectorER30WCLJoinCandidateSelectorParamsE20kalloc_type_view_175
+ __ZZN25IO80211NANDataPathManager17deleteNanInfoListEPP13ndp_info_nodeE21kalloc_type_view_5122
+ __ZZN25IO80211NANDataPathManager19addEntryNanInfoListEPP13ndp_info_nodePhtjjE21kalloc_type_view_5071
+ __ZZN27IO80211NANDataPathInitiator4freeEvE19kalloc_type_view_96
+ __ZZN27IO80211NANDataPathResponder4freeEvE20kalloc_type_view_103
+ ____ZN13WCLNetManager15connectCompleteEPv_block_invoke
+ ____ZN24WCLJoinCandidateSelector14removeBad6gApsEP14WCLJoinRequest_block_invoke
+ _availAttributes
+ _validateNANAvailabilityAttribute
- __FUNCTION__._ZN25IO80211P2PDFSProxyManager28checkForDFSPrimeAvailabilityEP18apple80211_channelPh28apple80211_dfs_proxy_clients
- __FUNCTION__._ZN25IO80211P2PDataPathManager23setCurrentPeerCacheSizeEj
- __ZL15availAttributes
- __ZL32validateNANAvailabilityAttributeP24apple80211_nan_attribute
- __ZN21IO80211NANPeerManager34enableNonSdbOn5GhzAvailabilityOnlyE34apple80211_nonsdb_5ghz_only_clientb
- __ZN25IO80211P2PDataPathManager20getMyCachedPeerCountEv
- __ZZN11IO80211Peer20freeTxLatencyStorageEvE21kalloc_type_view_2679
- __ZZN11IO80211Peer21allocTxLatencyStorageEvE21kalloc_type_view_2667
- __ZZN13WCLNetManager15initWithOptionsEP13WCLControllerP16WCLBulletinBoardE20kalloc_type_view_279
- __ZZN13WCLNetManager4freeEvE20kalloc_type_view_224
- __ZZN14IO80211NANPeer13freeResourcesEvE20kalloc_type_view_192
- __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1853
- __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1871
- __ZZN14IO80211NANPeer25initWithAddressAndManagerEPKhP18IO80211PeerManagerE20kalloc_type_view_163
- __ZZN14WCL11axManager15freeActionFrameEPvE20kalloc_type_view_858
- __ZZN14WCL11axManager22send11axAsrActionFrameEhhPhjE21kalloc_type_view_1158
- __ZZN14WCL11axManager24sendHsLpEmlsrActionFrameEbbjE21kalloc_type_view_1208
- __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1307
- __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1350
- __ZZN16IO80211BSSBeacon4freeEvE21kalloc_type_view_1366
- __ZZN21IO80211NANAttributeTx15initWithManagerEP21IO80211NANPeerManagerE21kalloc_type_view_1362
- __ZZN21IO80211NANAttributeTx4freeEvE21kalloc_type_view_1376
- __ZZN21IO80211NANPeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP10ether_addrE20kalloc_type_view_176
- __ZZN21IO80211NANPeerManager4freeEvE20kalloc_type_view_321
- __ZZN21IO80211ScanCacheStore25initIO80211ScanCacheStoreER27IO80211ScanCacheStoreParamsE20kalloc_type_view_579
- __ZZN21IO80211ScanCacheStore4freeEvE20kalloc_type_view_126
- __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19428
- __ZZN22IO80211AWDLPeerManager10growAFRingEvE22kalloc_type_view_19440
- __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19464
- __ZZN22IO80211AWDLPeerManager12shrinkAFRingEvE22kalloc_type_view_19476
- __ZZN22IO80211AWDLPeerManager13freeResourcesEvE21kalloc_type_view_2653
- __ZZN22IO80211AWDLPeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP10ether_addrE21kalloc_type_view_2129
- __ZZN22IO80211AWDLPeerManager17initWithInterfaceEP23IO80211VirtualInterfaceP10ether_addrE21kalloc_type_view_2607
- __ZZN22IO80211AWDLPeerManager22initAWDLStateTrackInfoEvE22kalloc_type_view_24978
- __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_40696
- __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_40680
- __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30609
- __ZZN22IO80211AWDLPeerManager33realTimeStatsGetSkywalkStatisticsEvE22kalloc_type_view_30639
- __ZZN22IO80211AWDLPeerManager4freeEvE21kalloc_type_view_2699
- __ZZN22IO80211AWDLPeerManager4freeEvE21kalloc_type_view_2710
- __ZZN24WCLJoinCandidateSelector28initWCLJoinCandidateSelectorER30WCLJoinCandidateSelectorParamsE20kalloc_type_view_170
- __ZZN25IO80211NANDataPathManager17deleteNanInfoListEPP13ndp_info_nodeE21kalloc_type_view_5113
- __ZZN25IO80211NANDataPathManager19addEntryNanInfoListEPP13ndp_info_nodePhtjjE21kalloc_type_view_5062
- __ZZN27IO80211NANDataPathInitiator4freeEvE19kalloc_type_view_90
- __ZZN27IO80211NANDataPathResponder4freeEvE19kalloc_type_view_87
CStrings:
+ "\"IO80211_kexts-1587.10\""
+ "%s: ERROR: DP attribute length %u too short for publish id\n"
+ "%s: ERROR: DP attribute length %u too short for responder NDI\n"
+ "%s: ERROR: DP attribute length %u too short, minimum %u\n"
+ "%s: ERROR: P2P peer count mismatch in FW cache for role %s (%s); global total=%u < this-role count=%u (role myCount=%u). Logging only, no corrective action taken.\n"
+ "%s: Error: trying to get NAN DW awake period when NAN not configured\n"
+ "%s: Error: trying to get NAN Master Preference when NAN not configured\n"
+ "%s: Error: trying to get NAN Random Factor when NAN not configured\n"
+ "%s: Error: trying to get NAN cluster ID when NAN not configured\n"
+ "%s: Error: trying to get NAN master channel when NAN not configured\n"
+ "%s: Error: trying to get NAN random factor rotation when NAN not configured\n"
+ "%s: Error: trying to get NAN secondary master channel when NAN not configured\n"
+ "%s: Error: trying to set NAN DW awake period when NAN not configured\n"
+ "%s: Error: trying to set NAN Master Preference when NAN not configured\n"
+ "%s: Error: trying to set NAN Random Factor when NAN not configured\n"
+ "%s: Error: trying to set NAN cluster ID when NAN not configured\n"
+ "%s: Error: trying to set NAN master channel when NAN not configured\n"
+ "%s: Error: trying to set NAN random factor rotation when NAN not configured\n"
+ "%s: Error: trying to set NAN secondary master channel when NAN not configured\n"
+ "%s: global=%u->%u myCount=%u (unchanged)\n"
+ "%s: myCount=%u->0 global=%u (unchanged)\n"
+ "%s:%d DFSP AWDL peer manager not available, not starting DFS monitoring for %s\n"
+ "%s:%d ERROR: DFSP AWDL peer manager not available, cannot configure DFS Proxy\n"
+ "%s::%s  Unable to instantiate _awdlAggressiveEdcaTimer \n"
+ "121122222222222"
+ "122222222222222222222222222222222222222222222222222222222222222222222211111111112222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221212"
+ "1222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111112"
+ "APPLE80211_IOC_AGGRESSIVE_EDCA"
+ "AirDrop aggressiveEdcaTimer timeout \n"
+ "Bad 6G AP"
+ "CPCDBG[dec] role=%u this=%p g=%u->%u my=%u->%u\n"
+ "CPCDBG[inFW++] inFW=%u->%u myCount=%u\n"
+ "CPCDBG[inFW--] inFW=%u->%u myCount=%u\n"
+ "CPCDBG[inFW=] inFW=%u->%u myCount=%u\n"
+ "CPCDBG[inc] role=%u this=%p g=%u->%u my=%u->%u\n"
+ "CPCDBG[removeAllPeers-enter] global=%u myCount=%u inFW=%u\n"
+ "CPCDBG[removeCachedPeers-enter] requested=%u global=%u myCount=%u\n"
+ "CPCDBG[removeCachedPeers-ok] subtracted=%u global=%u->%u myCount=%u->%u\n"
+ "CPCDBG[removeCachedPeers] dpMgr=NULL requested=%u (zeroing caller's count)\n"
+ "CPCDBG[reset-enter] global=%u myCount=%u inFW=%u\n"
+ "CPCDBG[reset-exit] global=%u myCount=%u inFW=%u\n"
+ "CPCDBG[set] role=%u this=%p c=%u g=%u->%u my=%u->%u\n"
+ "ERROR: %s::%s NAN attribute ID %d at offset %u with length %u exceeds dataLen %u\n"
+ "ERROR: %s::%s Parsing SD attribute, SRF length %u exceeds remaining %u\n"
+ "ERROR: %s::%s Parsing SD attribute, length %u too short for SRF header\n"
+ "ERROR: %s::%s Parsing SD attribute, length %u too short for match filter length\n"
+ "ERROR: %s::%s Parsing SD attribute, length %u too short for service info length\n"
+ "ERROR: %s::%s Parsing SD attribute, length %u too short, minimum %u\n"
+ "ERROR: %s::%s Parsing SD attribute, match filter length %u exceeds remaining %u\n"
+ "ERROR: %s::%s Parsing SD attribute, service info length %u exceeds remaining %u\n"
+ "ERROR: %s::%s Truncated NAN attribute header at offset %u, dataLen %u\n"
+ "IO80211_kexts-1587.10"
+ "NAN-5GOnly: ALERT: DP setup still in progress after %s, client %s(%d), EstDPs %d, %u msecs since progress, %u msecs deferred - enabling 5GHzOnly anyway\n"
+ "NAN-5GOnly: Clearing deferred 5GHzOnly enable, client %s(%d), was deferred %u msecs\n"
+ "NAN-5GOnly: DP progress, client %s(%d), EstDPs %d -> %d, refreshing no-progress budget after %u msecs (%u msecs deferred so far)\n"
+ "NAN-5GOnly: DP setup in progress - deferring enable, client %s(%d), waitForIr %d, EstDPs %d, %u msecs since progress, %u msecs deferred\n"
+ "NAN-5GOnly: armed deferred 5GHzOnly enable, client %s(%d), waitForIr %d, EstDPs %d, budgets %u/%u msecs\n"
+ "NAN-5GOnly: deferral on DP setup %s\n"
+ "NAN-5GOnly: monitor APPLIED deferred 5GHzOnly enable, client %s(%d), deferred %u msecs, bmap 0x%x\n"
+ "NAN-Avail: ALERT: 5GHzOnly enable with invalid client %d\n"
+ "NAN-Avail: enable request, client %s(%d), waitForIr %d, waitForDpSetup %d, bmap 0x%x, pending %d, forceBootArg %d\n"
+ "NAN-Avail: waiting for IR to kick in before moving to 5GHz only channel sequence\n"
+ "Oct 14 2026 23:07:05"
+ "WARNING: Service ID list attribute length %d holds more than %d service IDs, list will be truncated\n"
+ "[ik] %s@%d:AirDrop state changed to <%d> <%llu>\n"
+ "[ik] %s@%d:Other band roaming blocked for band %d, boost disabled\n"
+ "[wcl] %s@%d:WCLJoinCandidateSelector bad 6G AP\n"
+ "clearRoleCachedPeerCount"
+ "disableBlockedBandBoost"
+ "max defer ceiling"
+ "no-progress budget"
+ "nonSdb5GOnlyDefer"
+ "setAirDropState"
+ "setCurrentPeerCacheSizeOnly"
- "\"IO80211_kexts-1585.80\""
- "%s: ERROR: P2P peer count mismatch in FW cache; current total peer cache count in FW %u, P2P peer cache count %u\n"
- "%s: ERROR: trackedWakePeers is NULL!\n"
- "1211222222222"
- "12222222222222222222222222222222222222222222222222222222222222222222221111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221212"
- "122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221111111111111111111111111111111111112"
- "ERROR: Invalid Availability Type to %x\n"
- "ERROR: Parsing availability attribute with incorrect chanList length in availEntry, %d, %d\n"
- "ERROR: Parsing availability attribute with incorrect length %d, %d, %d\n"
- "ERROR: Parsing availability attribute with incorrect length in availEntry %d\n"
- "ERROR: Parsing availability attribute with incorrect timeBmap length in availEntry %d, %d, %d\n"
- "ERROR: Parsing availability attribute with number of band ids %d >= %d\n"
- "ERROR: Parsing availability attribute with timeBmap length %d greater %d\n"
- "IO80211_kexts-1585.80"
- "Sep 18 2026 21:52:45"
- "waiting for IR to kick in before moving to 5GHz only channel sequence\n"
```
