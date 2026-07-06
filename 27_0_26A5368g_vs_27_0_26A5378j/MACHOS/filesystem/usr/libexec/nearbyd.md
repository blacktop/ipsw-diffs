## nearbyd

> `/usr/libexec/nearbyd`

```diff

-  __TEXT.__text: 0x4ec34c
+  __TEXT.__text: 0x4d4f54
   __TEXT.__auth_stubs: 0x27d0
-  __TEXT.__objc_stubs: 0x13140
-  __TEXT.__init_offsets: 0x3b0
-  __TEXT.__objc_methlist: 0xda84
-  __TEXT.__gcc_except_tab: 0x4b694
-  __TEXT.__const: 0x3cf460
-  __TEXT.__cstring: 0x34824
-  __TEXT.__objc_methname: 0x1e743
-  __TEXT.__oslogstring: 0x548fb
-  __TEXT.__objc_classname: 0x1ade
-  __TEXT.__objc_methtype: 0x1fc2a
+  __TEXT.__objc_stubs: 0x132e0
+  __TEXT.__init_offsets: 0x2d8
+  __TEXT.__objc_methlist: 0xdbcc
+  __TEXT.__gcc_except_tab: 0x4ac74
+  __TEXT.__const: 0x3d9da8
+  __TEXT.__cstring: 0x34a13
+  __TEXT.__objc_methname: 0x1ecb3
+  __TEXT.__oslogstring: 0x54e82
+  __TEXT.__objc_classname: 0x1aee
+  __TEXT.__objc_methtype: 0x1fd8a
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x1e8
   __TEXT.__swift5_capture: 0x114

   __TEXT.__swift5_reflstr: 0x2b5
   __TEXT.__swift5_fieldmd: 0x22c
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1a038
+  __TEXT.__unwind_info: 0x19d88
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__const: 0x1d4d8
-  __DATA_CONST.__cfstring: 0x14c20
-  __DATA_CONST.__objc_classlist: 0x558
+  __DATA_CONST.__const: 0x1d558
+  __DATA_CONST.__cfstring: 0x14f80
+  __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x4e0
+  __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x428
   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_intobj: 0x6f0
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__auth_got: 0x1400
-  __DATA_CONST.__got: 0x888
+  __DATA_CONST.__got: 0x930
   __DATA_CONST.__auth_ptr: 0xe0
-  __DATA.__objc_const: 0x178e0
-  __DATA.__objc_selrefs: 0x5e90
-  __DATA.__objc_ivar: 0x16c4
-  __DATA.__objc_data: 0x39f8
-  __DATA.__data: 0x3254
-  __DATA.__bss: 0x1ee88
+  __DATA.__objc_const: 0x17d00
+  __DATA.__objc_selrefs: 0x5f28
+  __DATA.__objc_ivar: 0x1730
+  __DATA.__objc_data: 0x3a48
+  __DATA.__data: 0x34a4
+  __DATA.__bss: 0xcd38
   __DATA.__common: 0xde8
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 21207
+  Functions: 21184
   Symbols:   947
-  CStrings:  20173
+  CStrings:  20288
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA.__common : content changed
CStrings:
+ "#accessory-service,Generate UWB session ID - process %@ will use new UWB session ID %u from accessory blob (v2.2)"
+ "#accessory-service,Prep session objects: Phone is responder, using staticStsIV from accessory blob (v2.2)"
+ "#configurator,setSMBClkCfg: failed"
+ "#configurator,setSMBClkCfg: setting value %u"
+ "#configurator,setSMBClkCfg: succeeded"
+ "#ni-ca,send dl tdoa analytics event:\n%@\n"
+ "#roseprovider,\t\t\t\tresp %d: [rx_status: 0x%0x, address: 0x%04x, dtm_block_idx: %d, soi_rssi: %.1f, local_ts_sec: %.10f, dtm_ts_sec: %.10f, local_ts_raw: %llu, dtm_ts_raw: %llu, res_cfo_ppm: %.10f]"
+ "#roseprovider, GOT DTM from [0x%04x]: block start_time: %llu: { [status: 0x%0hx, block_idx: %u, round_idx: %u, nRes: %hu, nS: %hu, nF: %hu]. POLL: [rx_status: 0x%0x, addr: 0x%04x, rssi: %.4f, local_ts: %.10f, dtm_ts: %.10f, local_ts_raw: %llu, dtm_ts_raw: %llu, cfo_ppt: %d]. FINAL: [rx_status: 0x%0x, rssi_dbm: %.1f, local_ts: %.10f, dtm_ts: %.10f, local_ts_raw: %llu, dtm_ts_raw: %llu, cfo_ppt: %d]. }"
+ "#ses-loc,No location available for POI category lookup"
+ "#ses-loc,POI location manager failed: %{private}@"
+ "#threshold-detector, threshsize:%zu [in-%d] rssi: %f, rssiBorder: %f, rssiDelta: %f, mindecayfactor: %f, decayed_in_threshold: %f, samples: %d/%d, time: %f/%f"
+ "#threshold-detector, threshsize:%zu [no-change] rssi: %f, rssiBorder: %f, rssiDelta: %f, mindecayfactor: %f, decayed_in_threshold:%f, decayed_out_threshold:%f, samples: %d/%d, time: %f/%f"
+ "#threshold-detector, threshsize:%zu [out-%d] rssi: %f, rssiBorder: %f, rssiDelta: %f, mindecayfactor: %f, decayed_out_threshold:%f, samples: %d/%d, time: %f/%f"
+ "#threshold-detector, threshsize:%zu rssi: %f, thresholds: [%s], prev_state:%d possible_state:%d"
+ "-[NINearbyUpdatesEngine acceptDTTagMeasurements:analyticsManager:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/AppState/PRAppStateMonitor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/DevicePresence/NIServerBluetoothSampleDistributor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/RangingLimitManager/NIServerRangingLimitManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerAcwgSession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerBaseSession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerCarKeySession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerHomeDeviceSession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerNearbyAccessoryRangingService.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerNearbyPeerGrSession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerNearbyPeerSession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerSessionContainer.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/UWB/NIServerRoseSession.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/UpdatesEngine/NIServerNearbyUpdatesEngine.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/Services/NearbyInteraction/VIO/NIServerVisionDataDistributor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Daemon/nearbyd.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/AlishaSupport/AlishaParameterNegotiation.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/AlishaSupport/AlishaStateMachine.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/DaemonCore/PRConfigurationManager.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/DaemonCore/Ranging/Monitors/PRLocationMonitor.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/DaemonCore/Ranging/Providers/Rose/IO/PRRose.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/DaemonCore/Ranging/Providers/Rose/PRRoseProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/DaemonCore/Ranging/Providers/Rose/PRRoseSupervisorPacketBuilder.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/NearbyAlgorithms/AutoUnlock/NRBYPeerRangingDecisionProcessor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/NearbyAlgorithms/Finding/ParticleFilter.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/NearbyAlgorithms/RangeBiasEstimation/NRBYRangeBiasEstimator.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/NearbyAlgorithms/RegionMonitoring/NRBYDeviceMonitor.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/RangingServiceLib/ServiceProvider/RoseCycleIntervalPicker.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/RangingServiceLib/ServiceProvider/RoseRequestsFactory.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/Libraries/RangingServiceLib/SolutionProvider/RoseSolutionProvider.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPBTProxEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPBTProxEstimatorEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPChannelSoundingLogEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPLogEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPMoCapSystemLogEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPNearbyd.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPOptiTrackLogEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPOptiTrackStreamedLogEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPPrivateDataCapture.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPRangeAndAoaSolution.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPRoseCommunicationEvent.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPRoseLogEntry.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPRoseMotionEvent.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/CLPVisionEvent.pb.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Nzegrt/Sources/Proximity/protobuf/NearbyInteractionTypes.pb.cc"
+ "@\"DLTDoAAnalytics\""
+ "@144@0:8Q16Q24q32q40d48Q56d64Q72d80d88@96104@136"
+ "@36@0:8r^v16S24@28"
+ "AnchorCoordinateType"
+ "AnchorPOICategory"
+ "AnchorVisibilityRate"
+ "AopSFUseRecentRSSIForShrink"
+ "DLTDoAAnalytics"
+ "DeviceEnclosureMaterial"
+ "DiscoveryLatency"
+ "Failed to apply SMBClkCfg defaults override (%u); continuing boot"
+ "FirstMeasurementLatency"
+ "FirstSolutionLatency"
+ "ILSSolutionYieldRate"
+ "KFSolutionYieldRate"
+ "OOBDiscoveryMethod"
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
+ "_allAnchors"
+ "_allClusters"
+ "_anchorCoordinatesType"
+ "_anchorDeployPOICategory"
+ "_armASKRevocationObserverForPeer:"
+ "_convertPEAnchorMessages:analyticsManager:"
+ "_convertPEResponderAnchorMessage:initiatorAddress:analyticsManager:"
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
+ "com.apple.nearbyinteraction.dl-tdoa"
+ "configAnchorDeployPOICategory:"
+ "configCoordinatesType:"
+ "configRangingInterval:"
+ "configSessionSensorFusionFlag:"
+ "didGenerateSolutionFromILS:"
+ "didReceiveRawMeasurementFromAnchor:fromInitator:"
+ "didScheduleRangingSession"
+ "discoverCluster:fromMethod:"
+ "initWithAnchorAddress:clusterInitiatorAddress:measurementType:coordinatesType:transmitTime:rawTransmitTime:receiveTime:rawReceiveTime:signalStrength:carrierFrequencyOffset:responderClockFrequencyOffset:coordinates:floorElevation:"
+ "rawReceiveTime"
+ "rawTransmitTime"
+ "regulatory,comp,getDeviceEnclosureMaterial,%s"
+ "regulatory,comp,getDeviceEnclosureMaterial,ignoring default override on unsupported device"
+ "regulatory,comp,getDeviceEnclosureMaterial,set by default,%s"
+ "regulatory,comp,getDeviceEnclosureMaterial,unrecognized raw value %d — material will be UNKNOWN and nearbyd will crash unless a valid override is set via defaults write"
+ "sessionInvalidateWithReason:"
+ "setRawReceiveTime:"
+ "setRawTransmitTime:"
+ "setRoseSMBClkCfg. Success: %d. Value: %u"
+ "setSMBClkCfg:"
+ "v24@0:8S16B20"
+ "v24@0:8S16C20"
+ "v28@0:8q16C24"
+ "{optional<AnchorDeploymentCategory>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}"
+ "{optional<DLTDoAAnchorCoordinatesType>=\"\"(?=\"__null_state_\"c\"__val_\"C)\"__engaged_\"B}"
+ "{optional<rose::fira::AccessoryConfigurationData>=\"\"(?=\"__null_state_\"c\"__val_\"{AccessoryConfigurationData=\"accessoryProtocolVersion\"{Version=\"major\"S\"minor\"S}\"v10\"{V10_Fields=\"preferredUpdateRate\"C}\"rfu\"[10C]\"uwbConfigDataLength\"C\"uwbConfigData\"{UWBConfigData=\"uwbInteropVersion\"{Version=\"major\"S\"minor\"S}\"v10\"{V10_Fields=\"manufacturerId\"I\"uwbChipsetModelId\"I\"uwbMiddlewareVersion\"I\"rangingRole\"C\"sourceAddress\"S}\"v11\"{V11_Fields=\"maxUwbClockDriftPpm\"S}\"v20\"{V20_Fields=\"rfu\"[4C]\"hoppingMode\"C\"numSlotsPerRound\"S\"slotDurationRSTU\"S\"rangingIntervalMs\"S}\"v21\"{V21_Fields=\"requestedMultiNodeMode\"C\"requestedRangingRoundUsage\"C}\"v22\"{V22_Fields=\"uwbSessionId\"I\"staticStsInitializationVector\"[6C]}}})\"__engaged_\"B}"
+ "\xa2"
- "#roseprovider,\t\t\t\tresp %d: [rx_status: 0x%0x, address: 0x%04x, dtm_block_idx: %d, soi_rssi: %.1f, local_ts_sec: %.10f, dtm_ts_sec: %.10f, res_cfo_ppm: %.10f]"
- "#roseprovider, GOT DTM from [0x%04x]: block start_time: %llu: { [status: 0x%0hx, block_idx: %u, round_idx: %u, nRes: %hu, nS: %hu, nF: %hu]. POLL: [rx_status: 0x%0x, addr: 0x%04x, rssi: %.4f, local_ts: %.10f, dtm_ts: %.10f, cfo_ppt: %d]. FINAL: [rx_status: 0x%0x, rssi_dbm: %.1f, local_ts: %.10f, dtm_ts: %.10f, cfo_ppt: %d]. }"
- "#threshold-detector, threshsize:%zu [in] rssi: %f, rssiBorder: %f, rssiDelta: %f, mindecayfactor: %f, samples: %d/%d, time: %f/%f"
- "#threshold-detector, threshsize:%zu [out] rssi: %f, rssiBorder: %f, rssiDelta: %f, mindecayfactor: %f, samples: %d/%d, time: %f/%f"
- "-[NINearbyUpdatesEngine acceptDTTagMeasurements:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/AppState/PRAppStateMonitor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/DevicePresence/NIServerBluetoothSampleDistributor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/RangingLimitManager/NIServerRangingLimitManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerAcwgSession.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerBaseSession.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerCarKeySession.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerHomeDeviceSession.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerNearbyAccessoryRangingService.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerNearbyPeerGrSession.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerNearbyPeerSession.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/Session/NIServerSessionContainer.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/UWB/NIServerRoseSession.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/UpdatesEngine/NIServerNearbyUpdatesEngine.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/Services/NearbyInteraction/VIO/NIServerVisionDataDistributor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Daemon/nearbyd.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/AlishaSupport/AlishaParameterNegotiation.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/AlishaSupport/AlishaStateMachine.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/DaemonCore/PRConfigurationManager.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/DaemonCore/Ranging/Monitors/PRLocationMonitor.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/DaemonCore/Ranging/Providers/Rose/IO/PRRose.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/DaemonCore/Ranging/Providers/Rose/PRRoseProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/DaemonCore/Ranging/Providers/Rose/PRRoseSupervisorPacketBuilder.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/NearbyAlgorithms/AutoUnlock/NRBYPeerRangingDecisionProcessor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/NearbyAlgorithms/Finding/ParticleFilter.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/NearbyAlgorithms/RangeBiasEstimation/NRBYRangeBiasEstimator.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/NearbyAlgorithms/RegionMonitoring/NRBYDeviceMonitor.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/RangingServiceLib/ServiceProvider/RoseCycleIntervalPicker.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/RangingServiceLib/ServiceProvider/RoseRequestsFactory.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/Libraries/RangingServiceLib/SolutionProvider/RoseSolutionProvider.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPBTProxEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPBTProxEstimatorEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPChannelSoundingLogEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPLogEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPMoCapSystemLogEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPNearbyd.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPOptiTrackLogEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPOptiTrackStreamedLogEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPPrivateDataCapture.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPRangeAndAoaSolution.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPRoseCommunicationEvent.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPRoseLogEntry.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPRoseMotionEvent.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/CLPVisionEvent.pb.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.M2IbXn/Sources/Proximity/protobuf/NearbyInteractionTypes.pb.cc"
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
- "_convertPEAnchorMessages:"
- "_convertPEResponderAnchorMessage:initiatorAddress:"
- "_invalidateSessionWithError:"
- "acceptDTTagMeasurements:"
- "r"
- "{optional<rose::fira::AccessoryConfigurationData>=\"\"(?=\"__null_state_\"c\"__val_\"{AccessoryConfigurationData=\"accessoryProtocolVersion\"{Version=\"major\"S\"minor\"S}\"v10\"{V10_Fields=\"preferredUpdateRate\"C}\"rfu\"[10C]\"uwbConfigDataLength\"C\"uwbConfigData\"{UWBConfigData=\"uwbInteropVersion\"{Version=\"major\"S\"minor\"S}\"v10\"{V10_Fields=\"manufacturerId\"I\"uwbChipsetModelId\"I\"uwbMiddlewareVersion\"I\"rangingRole\"C\"sourceAddress\"S}\"v11\"{V11_Fields=\"maxUwbClockDriftPpm\"S}\"v20\"{V20_Fields=\"rfu\"[4C]\"hoppingMode\"C\"numSlotsPerRound\"S\"slotDurationRSTU\"S\"rangingIntervalMs\"S}\"v21\"{V21_Fields=\"requestedMultiNodeMode\"C\"requestedRangingRoundUsage\"C}}})\"__engaged_\"B}"
- "\x82"

```
