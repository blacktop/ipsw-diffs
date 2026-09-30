## locationd

> `/usr/libexec/locationd`

```diff

-3056.0.25.0.8
-  __TEXT.__text: 0x1bdaaf8
+3060.0.8.0.2
+  __TEXT.__text: 0x1bda5d4
   __TEXT.__auth_stubs: 0x6930
-  __TEXT.__objc_stubs: 0x47360
+  __TEXT.__objc_stubs: 0x47440
   __TEXT.__init_offsets: 0xa68
-  __TEXT.__objc_methlist: 0x333c8
-  __TEXT.__const: 0x160eb1
-  __TEXT.__cstring: 0x1f3fe4
-  __TEXT.__gcc_except_tab: 0xdac74
-  __TEXT.__objc_methname: 0x682c2
-  __TEXT.__oslogstring: 0x28ac5a
-  __TEXT.__objc_classname: 0x837b
-  __TEXT.__objc_methtype: 0x3769c
+  __TEXT.__objc_methlist: 0x33468
+  __TEXT.__const: 0x160fc1
+  __TEXT.__cstring: 0x1f4294
+  __TEXT.__gcc_except_tab: 0xda2c0
+  __TEXT.__objc_methname: 0x684fd
+  __TEXT.__oslogstring: 0x28bab6
+  __TEXT.__objc_classname: 0x839c
+  __TEXT.__objc_methtype: 0x37667
   __TEXT.__constg_swiftt: 0x624
   __TEXT.__swift5_typeref: 0x522
   __TEXT.__swift5_fieldmd: 0x2d4

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x71f50
+  __TEXT.__unwind_info: 0x72038
   __TEXT.__eh_frame: 0xcb8
   __DATA_CONST.__auth_got: 0x34b8
-  __DATA_CONST.__got: 0x2f68
+  __DATA_CONST.__got: 0x2f80
   __DATA_CONST.__auth_ptr: 0x5a0
-  __DATA_CONST.__const: 0xbee30
+  __DATA_CONST.__const: 0xbee78
   __DATA_CONST.__cfstring: 0x450c0
   __DATA_CONST.__objc_classlist: 0x15d8
   __DATA_CONST.__objc_catlist: 0xd8
-  __DATA_CONST.__objc_protolist: 0xe68
+  __DATA_CONST.__objc_protolist: 0xe70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xaa8
   __DATA_CONST.__objc_classrefs: 0x8

   __DATA_CONST.__objc_arrayobj: 0x960
   __DATA_CONST.__objc_floatobj: 0x80
   __DATA_CONST.__linkguard: 0x15
-  __DATA.__objc_const: 0x53b18
-  __DATA.__objc_selrefs: 0x162e0
-  __DATA.__objc_ivar: 0x3e3c
+  __DATA.__objc_const: 0x53c48
+  __DATA.__objc_selrefs: 0x16348
+  __DATA.__objc_ivar: 0x3e54
   __DATA.__objc_data: 0xe1c8
-  __DATA.__data: 0x61d70
+  __DATA.__data: 0x61dd0
   __DATA.__common: 0x1fe90
   __DATA.__bss: 0x118a8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices
   - /System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction
   - /System/Library/Frameworks/Network.framework/Network
+  - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 73DF64F6-B34A-3D0B-99EB-0963EAAED28A
-  Functions: 106371
-  Symbols:   3348
-  CStrings:  95251
+  UUID: 7C7375A3-2801-3D25-86DB-75844A6B712C
+  Functions: 106410
+  Symbols:   3350
+  CStrings:  95320
 
Symbols:
+ _EAAccessoryNMEASentenceFromAccessoryKey
+ _NSURLErrorDomain
+ _OBJC_CLASS_$_NEVPNConnectivityManager
- __swift_FORCE_LOAD_$_swiftCoreImage
CStrings:
+ "#GPSPowerSavings,reporting state to powerlog,fThrottlingGps,%{public}d"
+ "#GnssConstControl,setGnssConstellationSettingsFromMobileAssets,maBlocked,0x%{public}x,defaultForceEnable,0x%{public}x,result,0x%{public}x"
+ "#SystemServiceSwitch ignoring setting sync state on the watch"
+ "#fusion,Feed InertialOdometry,IO sample(s) is ignored,detected likely in-flight Airplane Mode."
+ "#fusion,indoorOutdoor state update is ignored,detected likely in-flight Airplane Mode."
+ "#fusion,invalidate selected/yielding hypothesis,hID,%{public}d,following an airplane mode toggle to disabled"
+ "#fusion,mct,%{public}.3f,Airplane Mode enabled status,elapsed time since enabled_s,%{public}.1f,elapsed time since last location update_s,%{public}.1f,accumulated_ap_sleep_time_since_s,%{public}.1f, %{public}.1f  buffering [%{public}d]"
+ "#fusion,mct,%{public}.3f,Airplane Mode toggled to disable,elapsed time since enabled_s,%{public}.3f"
+ "#fusion,mct,%{public}.3f,detected likely in-flight Airplane Mode,setting high dynamics mode,%{public}d,elapsed time since Airplane Mode enabled_s,%{public}.1f,elapsed time since last location update_s,%{public}.1f,AP-Up durations [s] since last location update (excluding AP sleeps),%{public}.1f"
+ "#fusion,mct,%{public}.3f,received Airplane Mode Status,Airplane Mode enabled,%{public}d"
+ "#fusion,motion state update is ignored,detected likely in-flight Airplane Mode."
+ "#fusion,now_mct,%{public}.3f,AP sleep wakeup called while fused state is not in sleep mode,accumulated_sleep_time_s,%{public}.2f,late arrival wakeup notification"
+ "#fusion,purging skipped,to avoid losing the selected/yielding hypothesis,hID,%{public}d,elapsed time since last location update_s,%{public}.1f,LatestMotionActivity,%{public}s"
+ "#fusion,slept_mct,%{public}.3f,now_mct,%{public}.3f,AP sleep wakeup after,%{public}.2f,[s],accumulated_sleep_time_s,%{public}.2f"
+ "#pbio Routine, userCfAbsoluteTimestamp_s, %{public}.3f, machContinuousTimestamp_s, %{public}.3f, sampleInterval_s, %{public}.3f, dPosX_m, %{private}+.3f, dPosY_m, %{private}+.3f, dPosZ_m, %{private}+.3f, dVelX_mps, %{private}+.3f, dVelY_mps, %{private}+.3f, dVelZ_mps, %{private}+.3f, qX, %{private}+.3f, qY, %{private}+.3f, qZ, %{private}+.3f, qW, %{private}+.3f, rotationToTrueNorthFromMagnetometer_rad, %{private}+.3f, referenceFrameContinuity, %{public}d, referenceFrame, %{public}d, staticFlag, %{public}d, isDeltaPositionValid, %{private}d, isRotationToTrueNorthFromMagnetometerValid, %{private}d, isDeltaVelocityValid, %d, isAttitudeValid, %{private}d, zuptIndicator, %{private}d, dotChangeIndicator, %{private}d, mountState, %{private}d,now, %{public}.3f, diffNowMinusSample, %{public}.3f"
+ "#pbio enabling forward of samples to routined, isWatch, %{public}d, fIntervalWithNoDeltaPositionToDeclareStaticPeriod_s, %{public}.3f, fDeltaPositionThresholdToDeclareStaticPeriod_m, %{public}.3f."
+ "#pbio, ending forced static period, input static flag, %{public}d, time since last non-negligible delta position, %{public}.3f, threshold, %{public}.3f"
+ "#pbio, starting forced static period, input static flag, %{public}d, time since last non-negligible delta position, %{public}.3f, threshold, %{public}.3f"
+ "#selection,Rejecting hypotheses in favor of gps based hypothesis,hID,%{public}d,lastYieldProminentProviderType,%{public}d,goodGNSSQuality,%{public}d,gpsHunc,%{public}.1f,gpsSpeed_mps,%{public}.2f,isStationary,%{public}d,MotionActivity,%{public}s"
+ "/AppleInternal/Library/BuildRoots/4~B9_5ugBW5sCotXfS0Ih7sotVFbeZw5F0ADjfNaI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B9_5ugBW5sCotXfS0Ih7sotVFbeZw5F0ADjfNaI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
+ "/AppleInternal/Library/BuildRoots/4~B9_5ugBW5sCotXfS0Ih7sotVFbeZw5F0ADjfNaI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B9_5ugBW5sCotXfS0Ih7sotVFbeZw5F0ADjfNaI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/4~B9_5ugBW5sCotXfS0Ih7sotVFbeZw5F0ADjfNaI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.1.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "00:23:54"
+ "00:30:50"
+ "@\"NEVPNConnectivityManager\""
+ "AONSenseKappaConfigService is nil, cannot request config"
+ "CL: -[CLInternalService reportLocationUtilityEvent:atDate:withReplyBlock:]"
+ "CL: _CLDaemonConfigure"
+ "CL: _CLDaemonCopyLastLog"
+ "CL: _CLDaemonCopyNearbyAssetSettings"
+ "CL: _CLDaemonCopyNearbyAssetSettingsOfAccessoryFileWithReply"
+ "CL: _CLDaemonCopyRoutineAssetSettings"
+ "CL: _CLDaemonDeleteCurrentEmergencyLocationAsset"
+ "CL: _CLDaemonDisplayStatistics"
+ "CL: _CLDaemonDumpLogs"
+ "CL: _CLDaemonGetActiveClientsUsingLocation"
+ "CL: _CLDaemonGetActivities"
+ "CL: _CLDaemonGetAppsUsingLocation"
+ "CL: _CLDaemonGetAuthorizationPromptMapDisplayEnabled"
+ "CL: _CLDaemonGetAuthorizationStatus"
+ "CL: _CLDaemonGetAuthorizationStatusForAppWithAuditToken"
+ "CL: _CLDaemonGetClientManagerInternalState"
+ "CL: _CLDaemonGetControlPlaneStatusReport"
+ "CL: _CLDaemonGetEEDCloakingKeyWithReply"
+ "CL: _CLDaemonGetEEDEmergencyContactNamesWithReply"
+ "CL: _CLDaemonGetEmergencyLocationSettingsVersion"
+ "CL: _CLDaemonGetGestureServiceEnabled"
+ "CL: _CLDaemonGetGnssBandsInUse"
+ "CL: _CLDaemonGetGroundAltitude"
+ "CL: _CLDaemonGetLocation"
+ "CL: _CLDaemonGetLocationDefault"
+ "CL: _CLDaemonGetLocationServicesEnabled"
+ "CL: _CLDaemonGetMonitoredRegions"
+ "CL: _CLDaemonGetPrecisionPermission"
+ "CL: _CLDaemonGetPrivateMode"
+ "CL: _CLDaemonGetStatusBarIconEnabledForEntityClass"
+ "CL: _CLDaemonGetStatusBarIconState"
+ "CL: _CLDaemonGetTechnologiesInUse"
+ "CL: _CLDaemonGetZaxisStats"
+ "CL: _CLDaemonGyroCalibrationDatabaseGetBiasFitAtTemperature"
+ "CL: _CLDaemonGyroCalibrationDatabaseGetNumTemperatures"
+ "CL: _CLDaemonGyroCalibrationDatabaseInsertBiasEstimateIfValid"
+ "CL: _CLDaemonGyroCalibrationDatabaseSupportsMiniCalibration"
+ "CL: _CLDaemonGyroCalibrationDatabaseWipe"
+ "CL: _CLDaemonOscarTimeSync"
+ "CL: _CLDaemonPerformMigration"
+ "CL: _CLDaemonPingDaemon"
+ "CL: _CLDaemonResetAllClients"
+ "CL: _CLDaemonResetClient"
+ "CL: _CLDaemonSetAuthorizationPromptMapDisplayEnabled"
+ "CL: _CLDaemonSetAuthorizationStatus"
+ "CL: _CLDaemonSetAuthorizationStatusByType"
+ "CL: _CLDaemonSetBackgroundIndicatorEnabled"
+ "CL: _CLDaemonSetGestureServiceEnabled"
+ "CL: _CLDaemonSetLocationDefault"
+ "CL: _CLDaemonSetLocationServicesEnabled"
+ "CL: _CLDaemonSetMapMatchingRouteHint"
+ "CL: _CLDaemonSetPrivateMode"
+ "CL: _CLDaemonSetStatusBarIconEnabledForEntityClass"
+ "CL: _CLDaemonSetTemporaryPreciseAuthorization"
+ "CL: _CLDaemonSetTrackRunHint"
+ "CL: _CLDaemonShouldDisplayEEDUI"
+ "CL: _CLDaemonShutdownDaemon"
+ "CL: _CLDaemonStartStopAdvertisingBeacon"
+ "CL: _CLDaemonTearDownLocationAuthPrompt"
+ "CL: _CLDaemonTimeZoneAtLocation"
+ "CL: _CLDaemongetAccessoryMotionSensorLogs"
+ "CL: _CLDaemongetMotionSensorLogs"
+ "CL: _CLDaemongetPipelinedCache"
+ "CL: _CLGetClientTransientAuthorizationInfo"
+ "CL: _CLInternalChangeClientAuthorizationTime"
+ "CL: _CLInternalTriggerExpiredAuthorizationPurge"
+ "CL: _CLPassKitNotifyPayment"
+ "CL: _CLSetClientTransientAuthorizationInfo"
+ "CL: deleteInterestZoneWithId:"
+ "CL: getAccessoryPASCDTransmissionStateWithReplyBlock"
+ "CL: getAccessoryTypeBitSetWithReplyBlock"
+ "CL: getIncidentalUseModeForBundleID:forBundleID:orBundlePath:replyBlock:"
+ "CL: getLearnedRoutesAccessForBundleID:forBundleID:orBundlePath:replyBlock:"
+ "CL: getOdometryBatchedLocationsWithReplyBlock"
+ "CL: getPinnedLocationAuthorization:replyBlock:"
+ "CL: getVisitHistoryAccessAllowedTimeForBundleID:forBundleID:orBundlePath:replyBlock:"
+ "CL: getVisitHistoryAccessForBundleID:forBundleID:orBundlePath:replyBlock:"
+ "CL: locctl_tool,fetchRecentLocationsWithOptions:withReply"
+ "CL: locctl_tool,getRecentLocationsBufferStatusWithReplyBlock"
+ "CL: locctl_tool,requestRouteReconstructionForPedestrian"
+ "CL: locctl_tool,triggerRecentLocationsRevisedFromMachContinuousTime:toMachContinuousTime"
+ "CL: registerCircularInterestZoneWithId:"
+ "CL: registerPhenolicInterestZoneWithId:"
+ "CL: setIncidentalUseMode:forBundleID:orBundlePath:replyBlock:"
+ "CL: setLearnedRoutesAccess:forBundleID:orBundlePath:replyBlock:"
+ "CL: setLocationButtonUseMode:forBundleID:orBundlePath:replyBlock:"
+ "CL: setPinnedLocationAuthorization:"
+ "CL: setRelevance:forInterestZoneWithName:"
+ "CL: setVisitHistoryAccess:forBundleID:orBundlePath:replyBlock:"
+ "CL: updateCorrectiveCompensationChoiceForOutstandingPrompt:replyBlock:"
+ "CL: updatePillButtonChoiceForOutstandingPrompt:replyBlock:"
+ "CL: updatePromptedLatitude:longitude:replyBlock:"
+ "CLAONSenseKappaConfigService *SafetyUtils::initAONSenseKappaConfigService(dispatch_queue_t  _Nonnull const &)_block_invoke"
+ "CLDeltaPositionThresholdToDeclareStaticPeriodMeters"
+ "CLIntervalWithNoDeltaPositionToDeclareStaticPeriodSec"
+ "CLJR,PedestrianDetector,first update,motion_cfat,%{public}.3f,type,%{public}d,mct,%{public}.3f"
+ "CLJR,PedestrianDetector,reset,prev_sum,%{public}d,mct,%{public}.3f"
+ "CLMM,CLTSP,CLAStarRouteConstructor,constructPedestrian,invalid processingTimeTracker"
+ "CLTSP,CLMM,input retrun road array is nil"
+ "Error reading and combining configs"
+ "GeoIPCountryCoalescingPeriod"
+ "GeoIPCountryRetryAttempts"
+ "GeoIPCountryRetryPeriod"
+ "LCPM,bestAccuracyDoesNotRequireGps,false,on heartbeat,fThrottlingGps,%{public}d"
+ "LCPM,bestAccuracyDoesNotRequireGps,true,on heartbeat"
+ "LCPM,bestAccuracyDoesNotRequireGps,true,on provider start"
+ "LCPM,update required location granularity to Best,notification,%{public}d,unregisterForNotificationInternal"
+ "LCPM,update required location granularity to Best,on heartbeat"
+ "LCPM,update required location granularity to Best,on provider start,haveBestAccuracyClients,%{public}d,requiredGranularity,%{public}d"
+ "LCPM,update required location granularity to Fine,notification,%{public}d,unregisterForNotificationInternal"
+ "LCPM,update required location granularity to Fine,on heartbeat"
+ "LCPM,update required location granularity to Fine,on provider start"
+ "LocationController,gnssPredictedAvailability,%{public}d,probability,%{public}.3f,timestamp,%{public}.3f,lastPredictionTimestamp,%{public}.3f,propagation_us,%{public}.3f,clients,%{public}d"
+ "NEVPNConnectivityManagerDelegate"
+ "NMEA Received from different accessory"
+ "NSMutableDictionary<NSString *,id> * _Nullable SafetyUtils::readAndCombineConfigs(NSURL * _Nonnull, NSURL * _Nullable, NSDictionary * _Nonnull)"
+ "NSMutableDictionary<NSString *,id> * _Nullable SafetyUtils::readConfigFile(NSURL *)"
+ "NSURL * _Nullable SafetyUtils::extractFileUrl(UAFAssetSet *, NSString *)"
+ "No Accessory information in NMEA message"
+ "No userInfo in NMEA message"
+ "Sep 17 2025"
+ "Sep 17 2025 00:27:40"
+ "T@\"NEVPNConnectivityManager\",&,N,V_vpnConnectivityMgr"
+ "TB,R,N,GgetHasAtLeastOneValidLocation"
+ "TQ,N,V_prevVPNConnectivityState"
+ "Td,N,V_coalescingPeriod"
+ "Td,N,V_retryPeriod"
+ "Ti,N,V_retryAttempts"
+ "_advTimeFormat"
+ "_coalescingPeriod"
+ "_prevVPNConnectivityState"
+ "_retryAttempts"
+ "_retryPeriod"
+ "_vpnConnectivityMgr"
+ "bool CLAStarRouteConstructor::constructPedestrian(CLDistanceCalc &, const CFAbsoluteTime, std::shared_ptr<CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker>, const CLMapRoadPtr &, const CLMapRoadPtr &, std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, const GEOLocationCoordinate2D &, const double, double, const std::optional<double>)"
+ "bool cllcf::CLLCFusion::isLikelyInFlightAirplaneMode()"
+ "coalesceGeoIPRequest"
+ "coalescingPeriod"
+ "connectivityManagerDidChange:"
+ "connectivityState"
+ "fGeoIPCoalescingTimer"
+ "fGeoIPRetryTimer"
+ "getAndPostCountryCodeWithRetriesRemaining:"
+ "getHasAtLeastOneValidLocation"
+ "hasAtLeastOneValidLocation"
+ "nil baseUrl"
+ "prevVPNConnectivityState"
+ "retryAttempts"
+ "retryPeriod"
+ "setCoalescingPeriod:"
+ "setPrevVPNConnectivityState:"
+ "setRetryAttempts:"
+ "setRetryPeriod:"
+ "setVpnConnectivityMgr:"
+ "shouldDeescalateBecauseOfCrashClassifierCondition"
+ "v24@0:8@\"NEVPNConnectivityManager\"16"
+ "virtual void CLKappaNotifier::Armed::entry(uint64_t, const void *)"
+ "void CLLocationController::trySetCachedLocationFromAdl(const CLLocationBufferBase::LCBufferLocation &)"
+ "void CLLocationControllerPedestrianDetector::reset()"
+ "void CLProactiveInertialOdometryManager::exportBackgroundInertialOdometrySamplesToRoutine(const std::vector<CLPIOSample> &)"
+ "void cllcf::CLLCFusion::airplaneModeStatusUpdate(const CFTimeInterval &, bool)"
+ "vpnConnectivityMgr"
+ "{\"msg%{public}.0s\":\"#SystemServiceSwitch ignoring setting sync state on the watch\"}"
+ "{\"msg%{public}.0s\":\"#monitor #Warning unable to exclude path from backup\", \"path\":%{public, location:escape_only}@, \"error\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"@ClxProvider,starting all location providers up to threshold\", \"threshold\":%{public}d, \"desiredAccuracy\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"Geo IP: VPN connectivity state changed\", \"previous\":%{public, location:NEVPNConnectivityState}lld, \"current\":%{public, location:NEVPNConnectivityState}lld}"
+ "{\"msg%{public}.0s\":\"Geo IP: VPN state transitioned between being off and on, so querying GeoIP after coalescing\", \"coalesce\":\"%{public}.1f\"}"
+ "{\"msg%{public}.0s\":\"Geo IP: connection error, will retry after delay\", \"retries_remaining\":%{public}d, \"attempts_made\":%{public}d, \"retry_delay\":%{public}d}"
+ "{\"msg%{public}.0s\":\"Geo IP: connection or throttling error, no more retries remaining\"}"
+ "{\"msg%{public}.0s\":\"Geo IP: got response from GeoServices about IP-based country\", \"cc\":%{private, location:escape_only}@, \"error\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"checking if remind timed of source\", \"source\":%{public, location:escape_only}@, \"elapsed\":\"%{public}0.2f\", \"cooldown\":\"%{public}0.2f\", \"timezone\":%{public, location:escape_only}s}"
- "#GPSPowerSavings,reporting state to powerlog,%{public}d"
- "#GnssConstControl,setGnssConstellationSettingsFromMobileAssets,0x%{public}x"
- "#fusion,now_mct,%{public}.3f,mct_slept,%{public}.3f,AP sleep wakeup called while fused state is not in sleep mode, waking up after,%{public}.3f,[s]"
- "#fusion,purging skipped,to avoid losing the selected/yielding hypothesis,hID,%{public}d,LatestMotionActivity,%{public}s"
- "#fusion,slept_mct,%{public}.3f,now_mct,%{public}.3f,AP sleep wakeup after,%{public}.2f,[s]"
- "#pbio enabling forward of samples to routined."
- "/AppleInternal/Library/BuildRoots/4~B8cxugCHzX7zVJwujddmLJ4Myy8Vrp5iVUoivNA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "/AppleInternal/Library/BuildRoots/4~B8cxugCHzX7zVJwujddmLJ4Myy8Vrp5iVUoivNA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/uuid/detail/random_provider_posix.ipp"
- "/AppleInternal/Library/BuildRoots/4~B8cxugCHzX7zVJwujddmLJ4Myy8Vrp5iVUoivNA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/uuid/string_generator.hpp"
- "/AppleInternal/Library/BuildRoots/4~B8cxugCHzX7zVJwujddmLJ4Myy8Vrp5iVUoivNA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/4~B8cxugCHzX7zVJwujddmLJ4Myy8Vrp5iVUoivNA/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "20:55:23"
- "21:03:51"
- "Aug 26 2025"
- "Aug 26 2025 20:59:26"
- "CL: -[CLInternalService reportLocationUtilityEvent:atDate:withReplyBlock:] (Fallback)"
- "CL: _CLDaemonConfigure (Fallback)"
- "CL: _CLDaemonCopyLastLog (Fallback)"
- "CL: _CLDaemonCopyNearbyAssetSettings (Fallback)"
- "CL: _CLDaemonCopyNearbyAssetSettingsOfAccessoryFileWithReply (Fallback)"
- "CL: _CLDaemonCopyRoutineAssetSettings (Fallback)"
- "CL: _CLDaemonDeleteCurrentEmergencyLocationAsset (Fallback)"
- "CL: _CLDaemonDisplayStatistics (Fallback)"
- "CL: _CLDaemonDumpLogs (Fallback)"
- "CL: _CLDaemonGetActiveClientsUsingLocation (Fallback)"
- "CL: _CLDaemonGetActivities (Fallback)"
- "CL: _CLDaemonGetAppsUsingLocation (Fallback)"
- "CL: _CLDaemonGetAuthorizationPromptMapDisplayEnabled (Fallback)"
- "CL: _CLDaemonGetAuthorizationStatus (Fallback)"
- "CL: _CLDaemonGetAuthorizationStatusForAppWithAuditToken (Fallback)"
- "CL: _CLDaemonGetClientManagerInternalState (Fallback)"
- "CL: _CLDaemonGetControlPlaneStatusReport (Fallback)"
- "CL: _CLDaemonGetEEDCloakingKeyWithReply (Fallback)"
- "CL: _CLDaemonGetEEDEmergencyContactNamesWithReply (Fallback)"
- "CL: _CLDaemonGetEmergencyLocationSettingsVersion (Fallback)"
- "CL: _CLDaemonGetGestureServiceEnabled (Fallback)"
- "CL: _CLDaemonGetGnssBandsInUse (Fallback)"
- "CL: _CLDaemonGetGroundAltitude (Fallback)"
- "CL: _CLDaemonGetLocation (Fallback)"
- "CL: _CLDaemonGetLocationDefault (Fallback)"
- "CL: _CLDaemonGetLocationServicesEnabled (Fallback)"
- "CL: _CLDaemonGetMonitoredRegions (Fallback)"
- "CL: _CLDaemonGetPrecisionPermission (Fallback)"
- "CL: _CLDaemonGetPrivateMode (Fallback)"
- "CL: _CLDaemonGetStatusBarIconEnabledForEntityClass (Fallback)"
- "CL: _CLDaemonGetStatusBarIconState (Fallback)"
- "CL: _CLDaemonGetTechnologiesInUse (Fallback)"
- "CL: _CLDaemonGetZaxisStats (Fallback)"
- "CL: _CLDaemonGyroCalibrationDatabaseGetBiasFitAtTemperature (Fallback)"
- "CL: _CLDaemonGyroCalibrationDatabaseGetNumTemperatures (Fallback)"
- "CL: _CLDaemonGyroCalibrationDatabaseInsertBiasEstimateIfValid (Fallback)"
- "CL: _CLDaemonGyroCalibrationDatabaseSupportsMiniCalibration (Fallback)"
- "CL: _CLDaemonGyroCalibrationDatabaseWipe (Fallback)"
- "CL: _CLDaemonOscarTimeSync (Fallback)"
- "CL: _CLDaemonPerformMigration (Fallback)"
- "CL: _CLDaemonPingDaemon (Fallback)"
- "CL: _CLDaemonResetAllClients (Fallback)"
- "CL: _CLDaemonResetClient (Fallback)"
- "CL: _CLDaemonSetAuthorizationPromptMapDisplayEnabled (Fallback)"
- "CL: _CLDaemonSetAuthorizationStatus (Fallback)"
- "CL: _CLDaemonSetAuthorizationStatusByType (Fallback)"
- "CL: _CLDaemonSetBackgroundIndicatorEnabled (Fallback)"
- "CL: _CLDaemonSetGestureServiceEnabled (Fallback)"
- "CL: _CLDaemonSetLocationDefault (Fallback)"
- "CL: _CLDaemonSetLocationServicesEnabled (Fallback)"
- "CL: _CLDaemonSetMapMatchingRouteHint (Fallback)"
- "CL: _CLDaemonSetPrivateMode (Fallback)"
- "CL: _CLDaemonSetStatusBarIconEnabledForEntityClass (Fallback)"
- "CL: _CLDaemonSetTemporaryPreciseAuthorization (Fallback)"
- "CL: _CLDaemonSetTrackRunHint (Fallback)"
- "CL: _CLDaemonShouldDisplayEEDUI (Fallback)"
- "CL: _CLDaemonShutdownDaemon (Fallback)"
- "CL: _CLDaemonStartStopAdvertisingBeacon (Fallback)"
- "CL: _CLDaemonTearDownLocationAuthPrompt (Fallback)"
- "CL: _CLDaemonTimeZoneAtLocation (Fallback)"
- "CL: _CLDaemongetAccessoryMotionSensorLogs (Fallback)"
- "CL: _CLDaemongetMotionSensorLogs (Fallback)"
- "CL: _CLDaemongetPipelinedCache (Fallback)"
- "CL: _CLGetClientTransientAuthorizationInfo (Fallback)"
- "CL: _CLInternalChangeClientAuthorizationTime (Fallback)"
- "CL: _CLInternalTriggerExpiredAuthorizationPurge (Fallback)"
- "CL: _CLPassKitNotifyPayment (Fallback)"
- "CL: _CLSetClientTransientAuthorizationInfo (Fallback)"
- "CL: deleteInterestZoneWithId: (Fallback)"
- "CL: getAccessoryPASCDTransmissionStateWithReplyBlock (Fallback)"
- "CL: getAccessoryTypeBitSetWithReplyBlock (Fallback)"
- "CL: getIncidentalUseModeForBundleID:forBundleID:orBundlePath:replyBlock: (Fallback)"
- "CL: getLearnedRoutesAccessForBundleID:forBundleID:orBundlePath:replyBlock: (Fallback)"
- "CL: getOdometryBatchedLocationsWithReplyBlock (Fallback)"
- "CL: getPinnedLocationAuthorization:replyBlock: (Fallback)"
- "CL: getVisitHistoryAccessAllowedTimeForBundleID:forBundleID:orBundlePath:replyBlock: (Fallback)"
- "CL: getVisitHistoryAccessForBundleID:forBundleID:orBundlePath:replyBlock: (Fallback)"
- "CL: locctl_tool,fetchRecentLocationsWithOptions:withReply (Fallback)"
- "CL: locctl_tool,getRecentLocationsBufferStatusWithReplyBlock (Fallback)"
- "CL: locctl_tool,requestRouteReconstructionForPedestrian (Fallback)"
- "CL: locctl_tool,triggerRecentLocationsRevisedFromMachContinuousTime:toMachContinuousTime (Fallback)"
- "CL: notifyClientsWithData (Fallback)"
- "CL: registerCircularInterestZoneWithId: (Fallback)"
- "CL: registerPhenolicInterestZoneWithId: (Fallback)"
- "CL: setIncidentalUseMode:forBundleID:orBundlePath:replyBlock: (Fallback)"
- "CL: setLearnedRoutesAccess:forBundleID:orBundlePath:replyBlock: (Fallback)"
- "CL: setLocationButtonUseMode:forBundleID:orBundlePath:replyBlock: (Fallback)"
- "CL: setPinnedLocationAuthorization: (Fallback)"
- "CL: setRelevance:forInterestZoneWithName: (Fallback)"
- "CL: setVisitHistoryAccess:forBundleID:orBundlePath:replyBlock: (Fallback)"
- "CL: updateCorrectiveCompensationChoiceForOutstandingPrompt:replyBlock: (Fallback)"
- "CL: updatePillButtonChoiceForOutstandingPrompt:replyBlock: (Fallback)"
- "CL: updatePromptedLatitude:longitude:replyBlock: (Fallback)"
- "CLAONSenseKappaConfigService *SafetyUtils::initAONSenseKappaConfigService(const dispatch_queue_t &)_block_invoke"
- "LCPM,bestAccuracyDoesNotRequireGps,false"
- "LCPM,bestAccuracyDoesNotRequireGps,true"
- "LocationController,gnssPredictedAvailability,%{public}d,probability,%{public}.3f,timestamp,%{public}.3f,lastPredictionTimestamp,%{public}.3f,propagation_us,%{public}.3f"
- "NSMutableDictionary<NSString *,id> * _Nullable SafetyUtils::readConfigFile(UAFAssetSet *, NSString *)"
- "bool CLAStarRouteConstructor::constructPedestrian(CLDistanceCalc &, const CFAbsoluteTime, CLGeoMapFeatureAccessGeometryCommon::ProcessingTimeTracker &, const CLMapRoadPtr &, const CLMapRoadPtr &, std::shared_ptr<CLGeoMapFeatureRoadGeometryBuffer>, const GEOLocationCoordinate2D &, const double, double, const std::optional<double>)"
- "fAtLeastOneValidLocation"
- "fGnssAvailabilityPredictorClient"
- "getAndPostCountryCode"
- "kill"
- "onGnssAvailabilityPredictorNotification:data:"
- "roadDisableNetwork"
- "roadHorizontalAccuracy"
- "roadSearchRadius"
- "shouldArmMarty"
- "void CLLocationController::outputBufferCallback(const CLLocationBufferBase::LCBufferLocation &)"
- "void CLSourceBuffer<CLOutdoorGnssAvailabilityPredictor>::add(const T &) [T = CLOutdoorGnssAvailabilityPredictor]"
- "{\"msg%{public}.0s\":\"#monitor #Warning unable to exclude path from backup\", \"path\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"Starting all location providers up to threshold\", \"threshold\":%{public}d, \"desiredAccuracy\":\"%{public}f\"}"
- "{\"msg%{public}.0s\":\"got response from GeoServices about IP-based country\", \"cc\":%{private, location:escape_only}@, \"error\":%{public, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"notifyClientsWithData\", \"event\":%{public, location:escape_only}s, \"name\":%{public, location:escape_only}s, \"notification\":%{public}lld}"
- "{unique_ptr<CLLocationProvider_Type::Client, std::default_delete<CLLocationProvider_Type::Client>>=\"__ptr_\"^{Client}}"

```
