## com.apple.iokit.IO80211Family

> `com.apple.iokit.IO80211Family`

```diff

-1585.79.0.0.0
+1587.5.0.0.0
   __TEXT.__os_log: 0x9e58
   __TEXT.__const: 0x2bec0
-  __TEXT.__cstring: 0x98b09
-  __TEXT_EXEC.__text: 0x2769f4
+  __TEXT.__cstring: 0x99674
+  __TEXT_EXEC.__text: 0x270d3c
   __TEXT_EXEC.__auth_stubs: 0x1420
   __DATA.__data: 0x5ec8
   __DATA.__common: 0x3160
   __DATA_CONST.__mod_init_func: 0x558
   __DATA_CONST.__mod_term_func: 0x558
-  __DATA_CONST.__const: 0x3a378
+  __DATA_CONST.__const: 0x3a448
   __DATA_CONST.__kalloc_type: 0x9ec0
   __DATA_CONST.__kalloc_var: 0xa00
   __DATA_CONST.__auth_got: 0xa10
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x20
-  Functions: 13130
-  Symbols:   17152
-  CStrings:  14885
+  Functions: 13141
+  Symbols:   17165
+  CStrings:  14931
 
Symbols:
+ __FUNCTION__._ZN18IO80211PeerManager16getStringForRoleEj
+ __FUNCTION__._ZN25IO80211P2PDataPathManager24clearRoleCachedPeerCountEv
+ __FUNCTION__._ZN25IO80211P2PDataPathManager27setCurrentPeerCacheSizeOnlyEj
+ __ZN16IO80211BSSBeacon17isHave6gOpElementEv
+ __ZN17IO80211BssManager33runActionOnMatchingCachedNetworksEU13block_pointerFbP8OSObjectE
+ __ZN18IO80211RoamProfile23disableBlockedBandBoostEP22ExtendedRoamParameters5Bands
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
+ __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1309
+ __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1352
+ __ZZN16IO80211BSSBeacon4freeEvE21kalloc_type_view_1368
+ __ZZN21IO80211NANAttributeTx15initWithManagerEP21IO80211NANPeerManagerE21kalloc_type_view_1372
+ __ZZN21IO80211NANAttributeTx4freeEvE21kalloc_type_view_1386
+ __ZZN21IO80211ScanCacheStore25initIO80211ScanCacheStoreER27IO80211ScanCacheStoreParamsE20kalloc_type_view_581
+ __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_40736
+ __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_40720
+ __ZZN24WCLJoinCandidateSelector28initWCLJoinCandidateSelectorER30WCLJoinCandidateSelectorParamsE20kalloc_type_view_175
+ __ZZN25IO80211NANDataPathManager17deleteNanInfoListEPP13ndp_info_nodeE21kalloc_type_view_5115
+ __ZZN25IO80211NANDataPathManager19addEntryNanInfoListEPP13ndp_info_nodePhtjjE21kalloc_type_view_5064
+ __ZZN27IO80211NANDataPathInitiator4freeEvE19kalloc_type_view_94
+ __ZZN27IO80211NANDataPathResponder4freeEvE19kalloc_type_view_97
+ ____ZN13WCLNetManager15connectCompleteEPv_block_invoke
+ ____ZN24WCLJoinCandidateSelector14removeBad6gApsEP14WCLJoinRequest_block_invoke
- __FUNCTION__._ZN25IO80211P2PDataPathManager23setCurrentPeerCacheSizeEj
- __ZN25IO80211P2PDataPathManager20getMyCachedPeerCountEv
- __ZZN11IO80211Peer20freeTxLatencyStorageEvE21kalloc_type_view_2679
- __ZZN11IO80211Peer21allocTxLatencyStorageEvE21kalloc_type_view_2667
- __ZZN13WCLNetManager15initWithOptionsEP13WCLControllerP16WCLBulletinBoardE20kalloc_type_view_279
- __ZZN13WCLNetManager4freeEvE20kalloc_type_view_224
- __ZZN14IO80211NANPeer13freeResourcesEvE20kalloc_type_view_192
- __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1853
- __ZZN14IO80211NANPeer23lowlatencyGetStatisticsEP11IO80211PeerE21kalloc_type_view_1871
- __ZZN14IO80211NANPeer25initWithAddressAndManagerEPKhP18IO80211PeerManagerE20kalloc_type_view_163
- __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1307
- __ZZN16IO80211BSSBeacon16initWithChanSpecEP11CCLogStreamP19CommonFaultReporterE21kalloc_type_view_1350
- __ZZN16IO80211BSSBeacon4freeEvE21kalloc_type_view_1366
- __ZZN21IO80211NANAttributeTx15initWithManagerEP21IO80211NANPeerManagerE21kalloc_type_view_1362
- __ZZN21IO80211NANAttributeTx4freeEvE21kalloc_type_view_1376
- __ZZN21IO80211ScanCacheStore25initIO80211ScanCacheStoreER27IO80211ScanCacheStoreParamsE20kalloc_type_view_579
- __ZZN22IO80211AWDLPeerManager28freeAwdlPacketDescriptorPoolEvE22kalloc_type_view_40696
- __ZZN22IO80211AWDLPeerManager28initAwdlPacketDescriptorPoolEjE22kalloc_type_view_40680
- __ZZN24WCLJoinCandidateSelector28initWCLJoinCandidateSelectorER30WCLJoinCandidateSelectorParamsE20kalloc_type_view_170
- __ZZN25IO80211NANDataPathManager17deleteNanInfoListEPP13ndp_info_nodeE21kalloc_type_view_5113
- __ZZN25IO80211NANDataPathManager19addEntryNanInfoListEPP13ndp_info_nodePhtjjE21kalloc_type_view_5062
- __ZZN27IO80211NANDataPathInitiator4freeEvE19kalloc_type_view_90
- __ZZN27IO80211NANDataPathResponder4freeEvE19kalloc_type_view_87
CStrings:
+ "\"IO80211_kexts-1587.5\""
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
+ "IO80211_kexts-1587.5"
+ "WARNING: Service ID list attribute length %d holds more than %d service IDs, list will be truncated\n"
+ "[ik] %s@%d:Other band roaming blocked for band %d, boost disabled\n"
+ "[wcl] %s@%d:WCLJoinCandidateSelector bad 6G AP\n"
+ "clearRoleCachedPeerCount"
+ "disableBlockedBandBoost"
+ "setCurrentPeerCacheSizeOnly"
- "\"IO80211_kexts-1585.79\""
- "%s: ERROR: P2P peer count mismatch in FW cache; current total peer cache count in FW %u, P2P peer cache count %u\n"
- "%s: ERROR: trackedWakePeers is NULL!\n"
- "IO80211_kexts-1585.79"
```
