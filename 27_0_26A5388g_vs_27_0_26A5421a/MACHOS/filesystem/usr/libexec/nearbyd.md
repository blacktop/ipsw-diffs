## nearbyd

> `/usr/libexec/nearbyd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-564.0.0.0.0
-  __TEXT.__text: 0x4d5a20
+568.0.0.0.0
+  __TEXT.__text: 0x4d9acc
   __TEXT.__auth_stubs: 0x27d0
-  __TEXT.__objc_stubs: 0x132a0
+  __TEXT.__objc_stubs: 0x13500
   __TEXT.__init_offsets: 0x2d4
-  __TEXT.__objc_methlist: 0xdc04
-  __TEXT.__gcc_except_tab: 0x4acc0
-  __TEXT.__const: 0x3ee0f8
-  __TEXT.__cstring: 0x34a53
-  __TEXT.__objc_methname: 0x1ec63
-  __TEXT.__oslogstring: 0x54e22
-  __TEXT.__objc_classname: 0x1ade
-  __TEXT.__objc_methtype: 0x1fd8a
+  __TEXT.__objc_methlist: 0xdd24
+  __TEXT.__gcc_except_tab: 0x4b2d0
+  __TEXT.__const: 0x3ee118
+  __TEXT.__cstring: 0x34bc3
+  __TEXT.__objc_methname: 0x1f033
+  __TEXT.__oslogstring: 0x55122
+  __TEXT.__objc_classname: 0x1aee
+  __TEXT.__objc_methtype: 0x206da
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x1e8
   __TEXT.__swift5_capture: 0x114

   __TEXT.__swift5_reflstr: 0x2b5
   __TEXT.__swift5_fieldmd: 0x22c
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x19dc8
+  __TEXT.__unwind_info: 0x19ec8
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__const: 0x1d620
-  __DATA_CONST.__cfstring: 0x14f80
-  __DATA_CONST.__objc_classlist: 0x558
+  __DATA_CONST.__cfstring: 0x15120
+  __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x4e0
+  __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x438
   __DATA_CONST.__objc_arrayobj: 0x1f8
-  __DATA_CONST.__objc_intobj: 0x6f0
+  __DATA_CONST.__objc_intobj: 0x708
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__auth_got: 0x1400
   __DATA_CONST.__got: 0x930
   __DATA_CONST.__auth_ptr: 0xe0
-  __DATA.__objc_const: 0x17bd8
-  __DATA.__objc_selrefs: 0x5f20
-  __DATA.__objc_ivar: 0x1720
-  __DATA.__objc_data: 0x39f8
+  __DATA.__objc_const: 0x17ee8
+  __DATA.__objc_selrefs: 0x5fd0
+  __DATA.__objc_ivar: 0x1764
+  __DATA.__objc_data: 0x3a48
   __DATA.__data: 0x34a4
   __DATA.__bss: 0xcd38
   __DATA.__common: 0xdf8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21200
+  Functions: 21247
   Symbols:   947
-  CStrings:  17276
+  CStrings:  17342
 
CStrings:
+ " - Client Name: [%s], initiator_addr: [%u], start_TS: [%@], end_TS: [%@], total_duration: [%.4f s], initiator_mac_addr: [0x%02x]\n                Session Updates:  raw_measurement: [%u], vio_input_count: [%u], pdr_input_count: [%u], latest_uwb_rssi: [%ld dBm], initial_oob_rssi: [%ld dBm]"
+ "#!"
+ "#dltdoa-ble-oob,Discovered DL-TDOA anchor via BLE: MAC=0x%04hx, RSSI: %ld, oobPayload=%s"
+ "#dltdoa-cluster-select,Found cluster 0x%02hx: using  %s current RSSI=%ld dBm (smoothed=%ld dBm)"
+ "#dltdoa-cluster-select,Pending cluster 0x%02hx (OOB RSSI=%ld) qualifies to replace active cluster 0x%02hx (UWB RSSI=%ld, discovery OOB RSSI=%ld, measurements=%u)"
+ "#dltdoa-cluster-select,Scanned OOB result: %s. NO UWB network Id found in OOB"
+ "#dltdoa-cluster-select,Scanned OOB result: %s. uwb session id: [0x%02x], not match client's network identifier: [0x%02x]"
+ "#dltdoa-cluster-select,recordAnchorMeasurementsForCluster: 0x%02hx, latest_uwb_rssi: %ld, anchors.size(): %zu"
+ "#ni-ca,BTCS common summary submission"
+ "#ni-ca,BTCS finder event submission"
+ "#ni-ca,[%@] send analytics event %@ (BTCS):\n%@\n"
+ "#ses-ecosystem,updateMotionState got new motionState: %ld"
+ "#ses-loc,attempted to start tracking stronger pending cluster [0x%02hx] in the freed slot, result: %s"
+ "#ses-loc,cluster [0x%02hx] evicted in favor of stronger pending cluster [0x%02hx], invalidate succeed? :%d"
+ "@\"<NIDLTDOAClusterSelectorDelegate>\""
+ "@\"NIDLTDOAClusterSelector\""
+ "@40@0:8@16@24I32B36"
+ "AppleUnknown"
+ "BTCSAccessory"
+ "BTCSAccessory1"
+ "BTCSAccessory2"
+ "ChannelSoundingParticleFilterUncertaintyHysteresis"
+ "ChannelSoundingParticleFilterUncertaintyThresh"
+ "ItemBTChannelSounding"
+ "NIDLTDOAClusterSelector"
+ "NIDLTDOAClusterSelectorDelegate"
+ "Others"
+ "ReplacedByStrongerPendingCluster"
+ "_armFlushSelectionTimerIfNeeded"
+ "_btcsDisconnectionCount"
+ "_btcsLaunchedFromNI"
+ "_bypassNetworkIdentifierCheck"
+ "_cachedDeviceState"
+ "_clusterSelector"
+ "_flushSelectionTimer"
+ "_lastKnownRSSI"
+ "_lastSessionStartTimestamp"
+ "_parseBeaconData"
+ "_payloadMatchesNetworkIdentifier:"
+ "_pendingClusterRSSI"
+ "_pruneClustersNotSeenWithinSmoothingWindow"
+ "_recentRSSISamples"
+ "_seekForReplacementIfAny"
+ "_selectRSSIForCluster:"
+ "_sessionHasNoUniqueAnchors:"
+ "_stopFlushSelectionTimer"
+ "_submitBTChannelSoundingSummaryWithDuration:"
+ "_timeAtFirstRawBTCSRange"
+ "_updateSmoothedRSSIForCluster:sample:"
+ "avgRangingRate"
+ "com.apple.nearbyinteraction.btchannelsounding"
+ "disconnectionEvent"
+ "endAllTrackingSessions"
+ "endTrackingSessionForCluster:"
+ "fallback band"
+ "flushSelection"
+ "incrementBTCSDisconnectionCount"
+ "initWithQueue:clusterSelector:"
+ "initWithQueue:delegate:networkIdentifier:bypassNetworkIdentifierCheck:"
+ "launchedFromNI"
+ "longValue"
+ "notifyWifiScanUpdate"
+ "preferred band"
+ "printableActiveSessionsState"
+ "q28@0:8S16q20"
+ "recordAnchorMeasurementsForCluster:anchors:"
+ "recordDiscoveredPayload:rssi:preferredBand:"
+ "recordPDRInputForAllActiveSessions"
+ "recordVIOInputForAllActiveSessions"
+ "regulatory,settings,setInRestrictedRegion,ignoreUpdates,isUWBChannelSettingChanged,%d,isUWBPowerTableChanged,%d,isNBChannelSettingChanged,%d,isNBPowerTableChanged,%d"
+ "selectSessionToReplaceWithStrongestPendingCluster"
+ "startTrackingSessionForCluster:clientIdentifier:"
+ "updateDiscoveryMethod:"
+ "updateWithBTCSPeerVendorID:productID:"
+ "v128@0:8{SessionRecord=IIdIIIqq{set<unsigned short, std::less<unsigned short>, std::allocator<unsigned short>>={__tree<unsigned short, std::less<unsigned short>, std::allocator<unsigned short>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}{optional<double>=(?=cd)B}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}16"
+ "v24@0:8S16S20"
+ "v28@0:8S16r^v20"
+ "v36@0:8r^v16q24B32"
+ "{BTCSItemFinderAlgorithmConfig=BBB{ParticleFilterConfig=BBqBBBdddddddddddddBBddddddBdddddddddddddddddddddddddddddddBBBBBdiddddiB{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}}{SyntheticApertureConfig=BBBBBdd}B}16@0:8"
+ "{PeopleFinderAlgorithmConfig=BBBBBBBdddddddd{ParticleFilterConfig=BBqBBBdddddddddddddBBddddddBdddddddddddddddddddddddddddddddBBBBBdiddddiB{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}}B{GnssReliabilityIndicatorConfig=dd}BdBBB}16@0:8"
+ "{map<unsigned short, (anonymous namespace)::ClusterRSSIInfo, std::less<unsigned short>, std::allocator<std::pair<const unsigned short, (anonymous namespace)::ClusterRSSIInfo>>>=\"__tree_\"{__tree<std::__value_type<unsigned short, (anonymous namespace)::ClusterRSSIInfo>, std::__map_value_compare<unsigned short, std::pair<const unsigned short, (anonymous namespace)::ClusterRSSIInfo>, std::less<unsigned short>>, std::allocator<std::pair<const unsigned short, (anonymous namespace)::ClusterRSSIInfo>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<unsigned short, long, std::less<unsigned short>, std::allocator<std::pair<const unsigned short, long>>>=\"__tree_\"{__tree<std::__value_type<unsigned short, long>, std::__map_value_compare<unsigned short, std::pair<const unsigned short, long>, std::less<unsigned short>>, std::allocator<std::pair<const unsigned short, long>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{map<unsigned short, std::deque<std::pair<double, long>>, std::less<unsigned short>, std::allocator<std::pair<const unsigned short, std::deque<std::pair<double, long>>>>>=\"__tree_\"{__tree<std::__value_type<unsigned short, std::deque<std::pair<double, long>>>, std::__map_value_compare<unsigned short, std::pair<const unsigned short, std::deque<std::pair<double, long>>>, std::less<unsigned short>>, std::allocator<std::pair<const unsigned short, std::deque<std::pair<double, long>>>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}"
+ "{optional<ClusterReplacementDecision>=(?=c{ClusterReplacementDecision=SS})B}16@0:8"
+ "{optional<SessionRecord>=(?=c{SessionRecord=IIdIIIqq{set<unsigned short, std::less<unsigned short>, std::allocator<unsigned short>>={__tree<unsigned short, std::less<unsigned short>, std::allocator<unsigned short>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}{optional<double>=(?=cd)B}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}})B}20@0:8S16"
+ "{optional<nearby::algorithms::device_presence::DeviceState>=\"\"(?=\"__null_state_\"c\"__val_\"i)\"__engaged_\"B}"
+ "{vector<(anonymous namespace)::PendingWifiDiscovery, std::allocator<(anonymous namespace)::PendingWifiDiscovery>>=^{PendingWifiDiscovery}^{PendingWifiDiscovery}{?=^{PendingWifiDiscovery}}}16@0:8"
+ "{vector<SessionRecord, std::allocator<SessionRecord>>=^{SessionRecord}^{SessionRecord}{?=^{SessionRecord}}}16@0:8"
+ "\xf0\xf0r"
- " (both bands available)"
- " - Client Name: [%s], initiator_addr: [%u], start_TS: [%@], end_TS: [%@], total_duration: [%.4f s], initiator_mac_addr: [0x%02x]\n                Session Updates:  raw_measurement: [%u], vio_input_count: [%u], pdr_input_count: [%u]"
- "#dltdoa-ble-oob,Discovered DL-TDOA anchor via BLE: MAC=0x%04hx, oobPayload=%s"
- "#dltdoa-wifi-oob,Found anchor 0x%02hx: using %s RSSI=%ld dBm%s"
- "#ses-loc,Scanned OOB result: %s. Mac addr: [0x%02hx], uwb session id: [0x%02x], not match client's network identifier: [0x%02lx]"
- "#ses-loc,Scanned OOB result: %s. NO UWB network Id found in OOB"
- "2.4GHz"
- "@\"<NIDLTDOAOOBScannerDelegate>\""
- "NIDLTDOAOOBScannerDelegate"
- "Other bands"
- "_notifyDelegateWithPayloads:anchorBandRSSI:cacheCount:"
- "_processBeaconData"
- "_selectPreferredRSSI:"
- "_sortAnchorsByRSSI:"
- "initWithQueue:delegate:"
- "regulatory,settings,setInRestrictedRegion,ignoreUpdates,isChannelSettingChanged,%d,isPowerTableChanged,%d"
- "v40@0:8r^v16r^v24Q32"
- "v88@0:8{SessionRecord=IIdIII{optional<double>=(?=cd)B}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}16"
- "{BTCSItemFinderAlgorithmConfig=BBB{ParticleFilterConfig=BBqBBBdddddddddddddBBddddddBdddddddddddddddddddddddddddddddBBBBdiddddiB{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}}{SyntheticApertureConfig=BBBBBdd}B}16@0:8"
- "{PeopleFinderAlgorithmConfig=BBBBBBBdddddddd{ParticleFilterConfig=BBqBBBdddddddddddddBBddddddBdddddddddddddddddddddddddddddddBBBBdiddddiB{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}{vector<nearby::algorithms::common::TLocationScaleParamsWithRange, std::allocator<nearby::algorithms::common::TLocationScaleParamsWithRange>>=^{TLocationScaleParamsWithRange}^{TLocationScaleParamsWithRange}{?=^{TLocationScaleParamsWithRange}}}}B{GnssReliabilityIndicatorConfig=dd}BdBBB}16@0:8"
- "{map<unsigned short, BandRSSIInfo, std::less<unsigned short>, std::allocator<std::pair<const unsigned short, BandRSSIInfo>>>={__tree<std::__value_type<unsigned short, BandRSSIInfo>, std::__map_value_compare<unsigned short, std::pair<const unsigned short, BandRSSIInfo>, std::less<unsigned short>>, std::allocator<std::pair<const unsigned short, BandRSSIInfo>>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}16@0:8"
- "{vector<std::pair<unsigned short, long>, std::allocator<std::pair<unsigned short, long>>>=^v^v{?=^v}}24@0:8r^v16"
- "\xf0\xf0b"
```
