## nearbyd

> `/usr/libexec/nearbyd`

```diff

-  __TEXT.__text: 0x565168
+  __TEXT.__text: 0x54dce4
   __TEXT.__auth_stubs: 0x30d0
-  __TEXT.__objc_stubs: 0x168c0
-  __TEXT.__init_offsets: 0x7dc
-  __TEXT.__objc_methlist: 0xf29c
-  __TEXT.__gcc_except_tab: 0x54e28
-  __TEXT.__const: 0x3dbf48
-  __TEXT.__cstring: 0x38a5d
-  __TEXT.__objc_methname: 0x227f5
-  __TEXT.__oslogstring: 0x61bee
-  __TEXT.__objc_classname: 0x203e
-  __TEXT.__objc_methtype: 0x2209d
+  __TEXT.__objc_stubs: 0x16b80
+  __TEXT.__init_offsets: 0x6fc
+  __TEXT.__objc_methlist: 0xf404
+  __TEXT.__gcc_except_tab: 0x54538
+  __TEXT.__const: 0x3e6260
+  __TEXT.__cstring: 0x38cec
+  __TEXT.__objc_methname: 0x22e85
+  __TEXT.__oslogstring: 0x62465
+  __TEXT.__objc_classname: 0x204e
+  __TEXT.__objc_methtype: 0x221fd
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x7ec
   __TEXT.__swift5_capture: 0x574

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x80
-  __TEXT.__unwind_info: 0x1ce78
+  __TEXT.__unwind_info: 0x1cbf8
   __TEXT.__eh_frame: 0x5a0
-  __DATA_CONST.__const: 0x1f080
-  __DATA_CONST.__cfstring: 0x16de0
-  __DATA_CONST.__objc_classlist: 0x628
+  __DATA_CONST.__const: 0x1f160
+  __DATA_CONST.__cfstring: 0x171c0
+  __DATA_CONST.__objc_classlist: 0x630
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x318
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x528
+  __DATA_CONST.__objc_superrefs: 0x530
   __DATA_CONST.__objc_arraydata: 0x470
   __DATA_CONST.__objc_arrayobj: 0x210
   __DATA_CONST.__objc_intobj: 0x978
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__auth_got: 0x1880
-  __DATA_CONST.__got: 0xcd8
+  __DATA_CONST.__got: 0xe50
   __DATA_CONST.__auth_ptr: 0x300
-  __DATA.__objc_const: 0x1acc8
-  __DATA.__objc_selrefs: 0x6e50
-  __DATA.__objc_ivar: 0x191c
-  __DATA.__objc_data: 0x4928
-  __DATA.__data: 0x3f5c
-  __DATA.__bss: 0x21430
+  __DATA.__objc_const: 0x1b148
+  __DATA.__objc_selrefs: 0x6f28
+  __DATA.__objc_ivar: 0x1994
+  __DATA.__objc_data: 0x4978
+  __DATA.__data: 0x41ac
+  __DATA.__bss: 0xe720
   __DATA.__common: 0xe60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 23376
-  Symbols:   1284
-  CStrings:  22852
+  Functions: 23361
+  Symbols:   1307
+  CStrings:  22998
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__common : content changed
Symbols:
+ _MKPointOfInterestCategoryAirport
+ _MKPointOfInterestCategoryAquarium
+ _MKPointOfInterestCategoryBakery
+ _MKPointOfInterestCategoryCafe
+ _MKPointOfInterestCategoryConventionCenter
+ _MKPointOfInterestCategoryFoodMarket
+ _MKPointOfInterestCategoryHotel
+ _MKPointOfInterestCategoryLibrary
+ _MKPointOfInterestCategoryMovieTheater
+ _MKPointOfInterestCategoryMuseum
+ _MKPointOfInterestCategoryParking
+ _MKPointOfInterestCategoryPharmacy
+ _MKPointOfInterestCategoryPublicTransport
+ _MKPointOfInterestCategoryRestaurant
+ _MKPointOfInterestCategorySchool
+ _MKPointOfInterestCategoryStadium
+ _MKPointOfInterestCategoryStore
+ _MKPointOfInterestCategoryTheater
+ _MKPointOfInterestCategoryUniversity
+ _MKPointOfInterestCategoryZoo
+ _OBJC_CLASS_$_MKLocalPointsOfInterestRequest
+ _OBJC_CLASS_$_MKLocalSearch
+ _OBJC_CLASS_$_MKPointOfInterestFilter
CStrings:
+ "#accessory-service,Generate UWB session ID - process %@ will use new UWB session ID %u from accessory blob (v2.2)"
+ "#accessory-service,Prep session objects: Phone is responder, using staticStsIV from accessory blob (v2.2)"
+ "#configurator,setSMBClkCfg: failed"
+ "#configurator,setSMBClkCfg: setting value %u"
+ "#configurator,setSMBClkCfg: succeeded"
+ "#ni-ca,send dl tdoa analytics event:\n%@\n"
+ "#roseprovider,\t\t\t\tresp %d: [rx_status: 0x%0x, address: 0x%04x, dtm_block_idx: %d, soi_rssi: %.1f, local_ts_sec: %.10f, dtm_ts_sec: %.10f, local_ts_raw: %llu, dtm_ts_raw: %llu, res_cfo_ppm: %.10f]"
+ "#roseprovider, GOT DTM from [0x%04x]: block start_time: %llu: { [status: 0x%0hx, block_idx: %u, round_idx: %u, nRes: %hu, nS: %hu, nF: %hu]. POLL: [rx_status: 0x%0x, addr: 0x%04x, rssi: %.4f, local_ts: %.10f, dtm_ts: %.10f, local_ts_raw: %llu, dtm_ts_raw: %llu, cfo_ppt: %d]. FINAL: [rx_status: 0x%0x, rssi_dbm: %.1f, local_ts: %.10f, dtm_ts: %.10f, local_ts_raw: %llu, dtm_ts_raw: %llu, cfo_ppt: %d]. }"
+ "#ses-container,[Auth] ASK [%@]: DeviceAccess.framework not available at runtime"
+ "#ses-container,[Auth] ASK revoked mid-session for peer %@; invalidating container"
+ "#ses-container,[Auth] ASK: DeviceAccess.framework not available at runtime; ASK gating disabled"
+ "#ses-container,[Auth] ASK: armed mid-session revocation observer for peer %@"
+ "#ses-container,[Auth] ASK: authorizationUpdated received; peer %@ still authorized"
+ "#ses-container,[Auth] ASK: failed to register for authorizationUpdated (status=%u)"
+ "#ses-loc,No POIs found near location or error: %{public}@"
+ "#ses-loc,No location available for POI category lookup"
+ "#ses-loc,No specific POI match, using fallback: %{private}@, AnchorDeploymentCategory: %d"
+ "#ses-loc,POI MKMapItem: %zu"
+ "#ses-loc,POI location manager failed: %{private}@"
+ "#ses-loc,Relevant POI: %{private}@, mapped to AnchorDeploymentCategory: %d"
+ "#threshold-detector, threshsize:%zu [in-%d] rssi: %f, rssiBorder: %f, rssiDelta: %f, mindecayfactor: %f, decayed_in_threshold: %f, samples: %d/%d, time: %f/%f"
+ "#threshold-detector, threshsize:%zu [no-change] rssi: %f, rssiBorder: %f, rssiDelta: %f, mindecayfactor: %f, decayed_in_threshold:%f, decayed_out_threshold:%f, samples: %d/%d, time: %f/%f"
+ "#threshold-detector, threshsize:%zu [out-%d] rssi: %f, rssiBorder: %f, rssiDelta: %f, mindecayfactor: %f, decayed_out_threshold:%f, samples: %d/%d, time: %f/%f"
+ "#threshold-detector, threshsize:%zu rssi: %f, thresholds: [%s], prev_state:%d possible_state:%d"
+ "-[NINearbyUpdatesEngine acceptDTTagMeasurements:analyticsManager:]"
+ "@\"DLTDoAAnalytics\""
+ "@144@0:8Q16Q24q32q40d48Q56d64Q72d80d88@96104@136"
+ "@36@0:8r^v16S24@28"
+ "AnchorCoordinateType"
+ "AnchorPOICategory"
+ "AnchorVisibilityRate"
+ "AopSFUseRecentRSSIForShrink"
+ "DLTDoA"
+ "DLTDoAAnalytics"
+ "DeviceEnclosureMaterial"
+ "DiscoveryLatency"
+ "Failed to apply SMBClkCfg defaults override (%u); continuing boot"
+ "FirstMeasurementLatency"
+ "FirstSolutionLatency"
+ "ILSSolutionYieldRate"
+ "KFSolutionYieldRate"
+ "OOBDiscoveryMethod"
+ "PAU"
+ "RangingYieldRate"
+ "Raw Receive Time: [%llu], "
+ "Raw Transmit Time: [%llu], "
+ "RawReceiveTime"
+ "RawTransmitTime"
+ "SMBClkCfg"
+ "SMBClkCfg defaults value %ld out of range [0, 255]; skipping"
+ "SMBClockConfig"
+ "SensorFusionFlag"
+ "SessionEndReason"
+ "SystemEventDictKey_SMBClkCfgValue"
+ "TQ,R,N,V_rawReceiveTime"
+ "TQ,R,N,V_rawTransmitTime"
+ "TotalAnchorsObserved"
+ "TotalClustersDiscovered"
+ "TotalILSSolutionYield"
+ "TotalKFSolutionYield"
+ "TotalRangingBlocksExpected"
+ "TotalRangingBlocksRecieved"
+ "UsageType"
+ "[15B]"
+ "_allAnchors"
+ "_allClusters"
+ "_anchorCategoryFromPOICategory:"
+ "_anchorCoordinatesType"
+ "_anchorDeployPOICategory"
+ "_armASKRevocationObserverForPeer:"
+ "_askGatedPeerIdentifier"
+ "_convertPEAnchorMessages:analyticsManager:"
+ "_convertPEResponderAnchorMessage:initiatorAddress:analyticsManager:"
+ "_daAuthNotifyToken"
+ "_deviceAccessAvailable"
+ "_firstAnchorBeingDiscovery"
+ "_firstMeasurementBeingReceived"
+ "_firstSolutionBeingReceived"
+ "_handleASKAuthorizationUpdate"
+ "_invalidateSessionWithError:reason:"
+ "_poiLocationManager"
+ "_previousBlockIndex"
+ "_rangingIntervalMs"
+ "_rawReceiveTime"
+ "_rawTransmitTime"
+ "_schedulingFirstSession"
+ "_sensorFusionFlag"
+ "_sessionEndedReason"
+ "_setSMBClkCfg:"
+ "_startPOILocationManager"
+ "_timeAtFirstAnchorDiscovery"
+ "_timeAtFirstRawMeasurement"
+ "_timeAtFirstSolution"
+ "_timeWaitingForReceivingFirstDTTagEvent"
+ "_totalExpectedRangingRound"
+ "_totalILSSolution"
+ "_totalKFSolution"
+ "_totalReceivedRangingBlocks"
+ "_totalSeeingAnchors"
+ "acceptDTTagMeasurements:analyticsManager:"
+ "com.apple.DeviceAccess.authorizationUpdated"
+ "com.apple.nearbyd.UWBUsageAggregation.v2"
+ "com.apple.nearbyinteraction.dl-tdoa"
+ "configAnchorDeployPOICategory:"
+ "configCoordinatesType:"
+ "configRangingInterval:"
+ "configSessionSensorFusionFlag:"
+ "didGenerateSolutionFromILS:"
+ "didReceiveRawMeasurementFromAnchor:fromInitator:"
+ "didScheduleRangingSession"
+ "discoverCluster:fromMethod:"
+ "initIncludingCategories:"
+ "initWithAnchorAddress:clusterInitiatorAddress:measurementType:coordinatesType:transmitTime:rawTransmitTime:receiveTime:rawReceiveTime:signalStrength:carrierFrequencyOffset:responderClockFrequencyOffset:coordinates:floorElevation:"
+ "initWithCenterCoordinate:radius:"
+ "initWithPointsOfInterestRequest:"
+ "mapItems"
+ "pointOfInterestCategory"
+ "rawReceiveTime"
+ "rawTransmitTime"
+ "regulatory,comp,getDeviceEnclosureMaterial,%s"
+ "regulatory,comp,getDeviceEnclosureMaterial,ignoring default override on unsupported device"
+ "regulatory,comp,getDeviceEnclosureMaterial,set by default,%s"
+ "regulatory,comp,getDeviceEnclosureMaterial,unrecognized raw value %d — material will be UNKNOWN and nearbyd will crash unless a valid override is set via defaults write"
+ "sessionInvalidateWithReason:"
+ "setPointOfInterestFilter:"
+ "setRawReceiveTime:"
+ "setRawTransmitTime:"
+ "setRoseSMBClkCfg. Success: %d. Value: %u"
+ "setSMBClkCfg:"
+ "startWithCompletionHandler:"
+ "v24@0:8S16B20"
+ "v24@0:8S16C20"
+ "v24@?0@\"MKLocalSearchResponse\"8@\"NSError\"16"
+ "v28@0:8q16C24"
+ "{optional<AnchorDeploymentCategory>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}"
+ "{optional<DLTDoAAnchorCoordinatesType>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}"
+ "{optional<rose::fira::AccessoryConfigurationData>=\"\"(?=\"__null_state_\"c\"__val_\"{AccessoryConfigurationData=\"accessoryProtocolVersion\"{Version=\"major\"S\"minor\"S}\"v10\"{V10_Fields=\"preferredUpdateRate\"C}\"rfu\"[10C]\"uwbConfigDataLength\"C\"uwbConfigData\"{UWBConfigData=\"uwbInteropVersion\"{Version=\"major\"S\"minor\"S}\"v10\"{V10_Fields=\"manufacturerId\"I\"uwbChipsetModelId\"I\"uwbMiddlewareVersion\"I\"rangingRole\"C\"sourceAddress\"S}\"v11\"{V11_Fields=\"maxUwbClockDriftPpm\"S}\"v20\"{V20_Fields=\"rfu\"[4C]\"hoppingMode\"C\"numSlotsPerRound\"S\"slotDurationRSTU\"S\"rangingIntervalMs\"S}\"v21\"{V21_Fields=\"requestedMultiNodeMode\"C\"requestedRangingRoundUsage\"C}\"v22\"{V22_Fields=\"uwbSessionId\"I\"staticStsInitializationVector\"[6C]}}})\"__engaged_\"B}"
+ "\xa2"
+ "\xf0\xf0\x94"
- "#roseprovider,\t\t\t\tresp %d: [rx_status: 0x%0x, address: 0x%04x, dtm_block_idx: %d, soi_rssi: %.1f, local_ts_sec: %.10f, dtm_ts_sec: %.10f, res_cfo_ppm: %.10f]"
- "#roseprovider, GOT DTM from [0x%04x]: block start_time: %llu: { [status: 0x%0hx, block_idx: %u, round_idx: %u, nRes: %hu, nS: %hu, nF: %hu]. POLL: [rx_status: 0x%0x, addr: 0x%04x, rssi: %.4f, local_ts: %.10f, dtm_ts: %.10f, cfo_ppt: %d]. FINAL: [rx_status: 0x%0x, rssi_dbm: %.1f, local_ts: %.10f, dtm_ts: %.10f, cfo_ppt: %d]. }"
- "#threshold-detector, threshsize:%zu [in] rssi: %f, rssiBorder: %f, rssiDelta: %f, mindecayfactor: %f, samples: %d/%d, time: %f/%f"
- "#threshold-detector, threshsize:%zu [out] rssi: %f, rssiBorder: %f, rssiDelta: %f, mindecayfactor: %f, samples: %d/%d, time: %f/%f"
- "-[NINearbyUpdatesEngine acceptDTTagMeasurements:]"
- "@28@0:8r^v16S24"
- "Command %s not allowed in deep sleep"
- "Failed to get deep sleep state"
- "MAX_FILTER"
- "MAX_OF_MEAN_CHAN_FILTER"
- "MEAN_FIILTER"
- "MEDIAN_FILTER"
- "MEDIAN_OF_MEAN_CHAN_FILTER"
- "OLYMPIC_FILTER"
- "RAYLEIGH_FILTER"
- "[13B]"
- "_convertPEAnchorMessages:"
- "_convertPEResponderAnchorMessage:initiatorAddress:"
- "_invalidateSessionWithError:"
- "acceptDTTagMeasurements:"
- "r"
- "{optional<rose::fira::AccessoryConfigurationData>=\"\"(?=\"__null_state_\"c\"__val_\"{AccessoryConfigurationData=\"accessoryProtocolVersion\"{Version=\"major\"S\"minor\"S}\"v10\"{V10_Fields=\"preferredUpdateRate\"C}\"rfu\"[10C]\"uwbConfigDataLength\"C\"uwbConfigData\"{UWBConfigData=\"uwbInteropVersion\"{Version=\"major\"S\"minor\"S}\"v10\"{V10_Fields=\"manufacturerId\"I\"uwbChipsetModelId\"I\"uwbMiddlewareVersion\"I\"rangingRole\"C\"sourceAddress\"S}\"v11\"{V11_Fields=\"maxUwbClockDriftPpm\"S}\"v20\"{V20_Fields=\"rfu\"[4C]\"hoppingMode\"C\"numSlotsPerRound\"S\"slotDurationRSTU\"S\"rangingIntervalMs\"S}\"v21\"{V21_Fields=\"requestedMultiNodeMode\"C\"requestedRangingRoundUsage\"C}}})\"__engaged_\"B}"
- "\x82"
- "\xf0\xf0t"

```
