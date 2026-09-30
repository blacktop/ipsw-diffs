## locationd

> `/usr/libexec/locationd`

```diff

-  __TEXT.__text: 0x1ad5990
-  __TEXT.__auth_stubs: 0x6470
-  __TEXT.__objc_stubs: 0x3d360
+  __TEXT.__text: 0x1ab9b38
+  __TEXT.__auth_stubs: 0x6460
+  __TEXT.__objc_stubs: 0x3d4e0
   __TEXT.__init_offsets: 0xbe0
-  __TEXT.__objc_methlist: 0x2dc88
-  __TEXT.__const: 0x168370
-  __TEXT.__gcc_except_tab: 0xd724c
-  __TEXT.__oslogstring: 0x283b60
-  __TEXT.__cstring: 0x20a616
-  __TEXT.__objc_methname: 0x5b13f
+  __TEXT.__objc_methlist: 0x2dd40
+  __TEXT.__const: 0x168490
+  __TEXT.__gcc_except_tab: 0xd7818
+  __TEXT.__oslogstring: 0x2853c0
+  __TEXT.__cstring: 0x205e79
+  __TEXT.__objc_methname: 0x5b56f
   __TEXT.__objc_classname: 0x7ff7
-  __TEXT.__objc_methtype: 0x389b8
+  __TEXT.__objc_methtype: 0x38a78
   __TEXT.__dlopen_cstrs: 0x4a
   __TEXT.__ustring: 0xa5e
   __TEXT.__constg_swiftt: 0x5e4

   __TEXT.__swift_as_cont: 0x18
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x75f50
+  __TEXT.__unwind_info: 0x75d08
   __TEXT.__eh_frame: 0xec8
-  __DATA_CONST.__const: 0xbf3c0
-  __DATA_CONST.__cfstring: 0x41f20
+  __DATA_CONST.__const: 0xbf620
+  __DATA_CONST.__cfstring: 0x41fe0
   __DATA_CONST.__objc_classlist: 0x1488
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xe48

   __DATA_CONST.__objc_arrayobj: 0x978
   __DATA_CONST.__objc_floatobj: 0x80
   __DATA_CONST.__linkguard: 0x15
-  __DATA_CONST.__auth_got: 0x3258
-  __DATA_CONST.__got: 0x2368
+  __DATA_CONST.__auth_got: 0x3250
+  __DATA_CONST.__got: 0x2580
   __DATA_CONST.__auth_ptr: 0x698
-  __DATA.__objc_const: 0x4e520
-  __DATA.__objc_selrefs: 0x13638
-  __DATA.__objc_ivar: 0x3ac4
+  __DATA.__objc_const: 0x4e638
+  __DATA.__objc_selrefs: 0x136b8
+  __DATA.__objc_ivar: 0x3adc
   __DATA.__objc_data: 0xd2f0
-  __DATA.__data: 0x62e98
-  __DATA.__common: 0x21ff0
-  __DATA.__bss: 0x12778
+  __DATA.__data: 0x62ea8
+  __DATA.__common: 0x22028
+  __DATA.__bss: 0x127a8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ActivityKit.framework/ActivityKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 112326
-  Symbols:   2893
-  CStrings:  92857
+  Functions: 112346
+  Symbols:   2892
+  CStrings:  92926
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__objc_classname : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ _IOHIDEventGetEventWithOptions
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE2atEm
- __ZNSt3__132__internal_log_hardening_failureEPKc
CStrings:
+ "#GnssSignalQuality,mct,%{public}.3f,trackingRateL1,%{public}.3f,trackingRateL5,%{public}.3f,keystoneL1_CN0,%{public}.1f,keystoneL5_CN0,%{public}.1f,ravenAcceptedCount,%{public}d"
+ "#WirelessClientInfo: applied regulatory coords overlay. coords=%{sensitive}.7f,%{sensitive}.7f, hAcc=%{public}.1f, vAcc=%{public}.1f, alt=%{private}.1f"
+ "#WirelessClientInfo: incoming fix has no valid regulatory coords; preserving previously stored fLastWirelessClientInfo for timer-driven re-evaluations. fence=%{private}s"
+ "#WirelessClientInfo: regulatory coords diverge from original fix (originalType=%{public}d, hAcc=%{public}.1f); substituting %{public}s"
+ "#WirelessClientInfo: skipping evaluation — regulatory coords invalid. fence=%{private}s"
+ "#WirelessClientInfoUnsupportedCombination: Client %{public}@ registered fence %{private}s with both WirelessClientInfo and SignificantRegion flags; combination is not supported, rejecting registration"
+ "#WirelessClientInfoUnsupportedCombination: refusing to evaluate fence with WirelessClientInfo flag via significant-region path; regulatory-coordinate selection is not supported here. fence=%{private}s, reason=%{public}s"
+ "#altimeter,compute visit elevation,now,%.3f,startTime,%.3f,endTime,%.3f"
+ "#altimeter,error adding elevations to routine,error,%@"
+ "#fusion,WCI-fusion,getWCIFusedLocation failed,WCI fusion is disabled."
+ "#fusion,WCI-fusion,getWCIFusedLocation failed,WCI hypothesized location is invalid"
+ "#pcm, anomalous negative reconnection gap (%{public}.3f s); dispatching kConnection"
+ "#pcm, declareParkedCarEvent suppressed by monotonic gate; skipping retry-arm to avoid leaking the rejected parkingTime into the retry path"
+ "#pcm, deferred disconnection location, hAcc %{public}.3f m exceeds threshold %{public}.3f m"
+ "#pcm, deferred heading-timestamp location at headingCfat=%{public}.3f, hAcc %{public}.3f m exceeds threshold %{public}.3f m"
+ "#pcm, failed to fetch disconnection location"
+ "#pcm, invalidated in-memory fLastParkedCarEvent cache"
+ "#pcm, invalidated persisted parked car location/heading on disk (timestamp + vehicle identity retained)"
+ "#pcm, rapid reconnection during exit-pending (%{public}.1f s since disconnect), dispatching kRapidReconnection"
+ "#pcm, setLastParkedCarEvent rejected: new parkingTime %{public}.3f vs existing %{public}.3f (delta %{public}.3f s) not > %{public}.3f s newer, keeping current"
+ "#vhe, getParkedVehicleHeadingPriorToCFAbsoluteTime, search-back found no better σ within window"
+ "#vhe, getParkedVehicleHeadingPriorToCFAbsoluteTime, search-back halted at moving sample (Δt=%{public}.3f s, speed=%{public}.3f m/s)"
+ "#vhe, getParkedVehicleHeadingPriorToCFAbsoluteTime, search-back improved σ from %{public}.3f° to %{public}.3f° (Δt=%{public}.3f s, headingDeltaFromAnchor=%{public}.3f°)"
+ "#vhe, tryUpdateHeadingFilterWithHeartbeat, clearing in-vehicle session, mct, %{public}.3f, last-mounted-mct, %{public}.3f, gap_s, %{public}.1f"
+ "#wci setting (%{sensitive}.3f,%{sensitive}.3f)"
+ "#wci,GnssRestrictedMode,cancelTransition,intent,%{public}d"
+ "#wci,GnssRestrictedMode,downgrade,stopCompleted"
+ "#wci,GnssRestrictedMode,downgrade,stopCompleted,canceledBeforeRestart"
+ "#wci,GnssRestrictedMode,drive,transitioning,intent,%{public}d"
+ "#wci,GnssRestrictedMode,upgrade,configApplied,canceledBeforeCompletion"
+ "#wci,refLoc,floor cachedGps hunc,was,%{public}.1f"
+ "-[CLSmootherMonitor submitCoreRoutineFetchReplyAnalyticsEventForType:intervalIndex:callId:result:fetchTimeMsec:returnedSampleCount:fetchIntervalDurationSeconds:samplesPerSecond:error:]_block_invoke"
+ "21:47:18"
+ "21:57:17"
+ "@72@0:8d16d24@32@40@48B56Q60B68"
+ "@LocalCellTagging, #Warning Location Services disabled, not storing location entry"
+ "@LocalCellTagging, cell %{private}s is local <%{sensitive}+.8f,%{sensitive}+.8f> remote <%{sensitive}+.8f,%{sensitive}+.8f> only %.2fm apart - not storing locally"
+ "@LocalCellTagging, cell %{private}s is local at <%{sensitive}+.8f,%{sensitive}+.8f>"
+ "@LocalCellTagging, distance, %{public}.1lf, not storing locally, %{private}s, location, %{sensitive}s"
+ "@LocalCellTagging, distance, %{public}.1lf, override local location, %{private}s, location, %{sensitive}s"
+ "@LocalCellTagging, isEnabled, %{public}d. CDMA local harvesting not done"
+ "@LocalCellTagging, isEnabled, %{public}d. GSM local harvesting not done"
+ "@LocalCellTagging, isEnabled, %{public}d. LTE local harvesting not done"
+ "@LocalCellTagging, isEnabled, %{public}d. Legacy CDMA local harvesting not done"
+ "@LocalCellTagging, isEnabled, %{public}d. Legacy GSM local harvesting not done"
+ "@LocalCellTagging, isEnabled, %{public}d. Legacy LTE local harvesting not done"
+ "@LocalCellTagging, isEnabled, %{public}d. Legacy NR local harvesting not done"
+ "@LocalCellTagging, isEnabled, %{public}d. Legacy SCDMA local harvesting not done"
+ "@LocalCellTagging, isEnabled, %{public}d. NR local harvesting not done"
+ "@LocalCellTagging, isEnabled, %{public}d. SCDMA local harvesting not done"
+ "@LocalCellTagging, local cell tagging enabled via defaults write isLocalCellTaggingEnabled"
+ "@LocalCellTagging, scdma cell %{private}s is local <%{sensitive}+.8f,%{sensitive}+.8f> remote <%{sensitive}+.8f,%{sensitive}+.8f> only %.2fm apart - not storing locally"
+ "@LocalCellTagging, scdma cell %{private}s is local at <%{sensitive}+.8f,%{sensitive}+.8f>"
+ "@TileOptimization: defaults write TileOptimizationEnabled to %{public}s"
+ "AmbiguousCountryRetryTimeout"
+ "AngleServiceReport"
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 236,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 242,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 237,invalid element %zu <= %zu."
+ "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 243,invalid element %zu <= %zu."
+ "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 307,indices exceed factored matrix size."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 191,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 196,invalid row %zu > %zu."
+ "B1632@0:8{NotificationData={Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}id{FenceMonitorAnalytics=i{CLFenceAnalyticsGeofenceEventTimes=Bdddddddddddddd}d{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}iiiddddddd{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}B}}16"
+ "B1840@0:8{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}{shared_ptr<const gnss::MeasurementData>=^{MeasurementData}^{__shared_weak_count}}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLBasebandTimeFreqTransfer=d{CLBasebandSystemClock=Qffdfd}Qf{LeapSecondInfo=sC{LeapSecondChange=Qs}}}{CLGnssBasebandCausesL1InterferenceGnssBandChangeData=ii}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}}16"
+ "B32@0:8^{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}16r^v24"
+ "BOOL CLSmootherMonitorUtils::shouldFetchIOForInterval(NSArray<CLLocation *> *, CLMotionActivity::Type, const IOFetchHysteresis<kIOFetchHysteresisWindowSize> &)"
+ "CLGnssSignalQualityResult CLGnssSignalQualityMetric::update(const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport &, int, CFTimeInterval)"
+ "CLP.LogEntry.PrivateData.LocationControllerInternalState.GnssSignalQualityMetric"
+ "CLP.LogEntry.Raven.RavenReset"
+ "CLRS,1Hz TSP path,isIOSupportedWorkoutType,%d,ratioOfLocationsThatAreDenseUrban,%{public}.1lf,routeLinearity,%{public}.3lf,denseUrbanRatioQualifiesForIOFusion,%{public}d,is1HzDataRequiringIOFusion,%{public}d"
+ "CLRS,1Hz TSP,enableIOFusion,%{public}d,denseUrbanRatioQualifiesForIOFusion,%{public}d,routeLinearity,%{public}.3f"
+ "CLRS,crossBatchSeam,bridge,precedingSeamStartTime set on first 1Hz interval,%{public}.2f"
+ "CLRS,crossBatchSeam,bridgeable,seam,%{public}.1lf,threshold,%{public}.1lf"
+ "CLRS,crossBatchSeam,overlapsRecordedPause,seam,%{public}.1lf,threshold,%{public}.1lf"
+ "CLRS,crossBatchSeam,seam,%{public}.1lf,threshold,%{public}.1lf"
+ "CLRS,crossBatchSeam,startsNewSegment set on first 1Hz interval"
+ "CLRS,denseUrbanRatioQualifiesForIOFusion,ratioCurrent,%{public}.3f,ratioCombined,%{public}.3f,contextCount,%{public}lu,contextDU,%{public}lu,newCount,%{public}lu,newDU,%{public}lu,denseUrbanRatioQualifiesForIOFusion,%{public}d"
+ "CLRS,elevation fetch complete,intervalIndex,%{public}u,totalCount,%{public}lu,accumulatedYield,%{public}.2lf"
+ "CLRS,empty interval with context to flush,count,%{public}zu,contextLoc,%{public}lu,final,%{public}d"
+ "CLRS,fetch locations completion block,hadLocationFetchError,%{public}d,jj,%{public}u"
+ "CLRS,fetchBackgroundInertialOdometrySamplesWithStartTime,startTime,%{public}.1lf,endTime,%{public}.1lf,buffer,%{public}.1lf,intervalIndex,%{public}u,seamWidened,%{public}d"
+ "CLRS,gap found,time,%{public}.1lf,gap duration,%{public}.1lf,forced,%{public}d"
+ "CLRS,gapDetection,batchSPI,%{public}d,activity,%{public}d,isWatch,%{public}d,isNIO,%{public}d,gap,%{public}.1lf,maxBridgeableGap_s,%{public}.1lf"
+ "CLRS,intraBatchGap,startsNewSegment set at,%{public}.2f"
+ "CLRS,routined appears unreachable,batch completed with no fetch replies,fetchesDispatched,%{public}zu,fetchReplies,%{public}zu,fetchTimeouts,%{public}zu,intervals,%{public}zu"
+ "CLRS,shouldFetchIOSamplesForInterval,workoutActivity,%{public}d,totalLocations,%{public}lu,hasSufficientDenseUrbanLocations,%{public}d,historicalFetch,%{public}d,shouldFetch,%{public}d"
+ "CLRS,startsNewSegment,Passthrough clearing context and reseeding seam at,%{public}.2f"
+ "CLRS,startsNewSegment,TSP clearing context and reseeding seam at,%{public}.2f"
+ "CLRS,startsNewSegment,forcing segment break at,%{public}.2f"
+ "CLRS,suppressing late CoreRoutineFetchResults after timeout,fetchType,%{public}@,intervalIndex,%{public}u"
+ "CLRS,synthesizedFlushInterval,batchType,%{public}s"
+ "CLStepCountHealthKitWriter: backfill streamed %{public}lu datums for %@"
+ "CLStepCountHealthKitWriter: query [%{public}f,%{public}f] -> %{public}lu rows (rc=%d)"
+ "CLStepCountHealthKitWriter::writeDatumsFromBackfilledRecords id=%@ [%{public}f, %{public}f]"
+ "CLStepCountHealthKitWriter::writeDatumsFromBackfilledRecords: fDb is null, cannot backfill"
+ "CLWifiAccessPoint CLWifiPositionCalculatorWithAssociatedAp::calculateAssociatedApCentroidFromHarvestDatabase(std::shared_ptr<CLWifiAssociatedApHarvestDatabase>, AssociatedApCentroidFetchOutcome, const CFTimeInterval &)"
+ "CMSidebandSensorFusionImuIndex"
+ "CellQuery, ignore, matched, %{private}s"
+ "CountryTrackerRetryIfAmbiguous"
+ "FindNearbyLocalFindableAccessoryExtendedRange"
+ "HK collector %s, last persisted=%{public}f, backfill window=[%{public}f,%{public}f]"
+ "HKQuantityDatum * _Nullable (anonymous namespace)::makeBackfillDelta(HKQuantityTypeIdentifier _Nonnull, const CLStepCountEntry &, const CLStepCountEntry &)"
+ "Jun 30 2026"
+ "Jun 30 2026 21:52:36"
+ "MotionLoggerLogButtonAccidentalsSignals"
+ "MotionLoggerLogButtonPresses"
+ "NonFinalSeam"
+ "PednetRunSubset set to %{public}d"
+ "SigFence"
+ "T@\"NSArray\",&,N,V_lastAmbiguousCountryCodes"
+ "TB,N,V_hasUsedAmbiguousRetry"
+ "TB,N,V_lastAmbiguousDisputedState"
+ "TB,R,N,V_startsNewSegment"
+ "Td,N,V_ambiguousCountryRetryTimeout"
+ "TileOptimizationEnabled"
+ "WifiCalc, skip updating computed location using associated AP %{private}s as the %{public}s centroid fails to pass cross-check with GPS/Cell!"
+ "WifiCalc, skip updating computed location using associated AP %{private}s as the %{public}s centroid is KnownAC"
+ "WifiCalc, skip updating computed location using associated AP %{private}s as the %{public}s centroid is invalid!"
+ "WifiCalc, skip updating computed location using associated AP %{private}s as the %{public}s centroid uncertainty %{public}.1f is greater than %{public}.1f"
+ "WifiCalc, skip updating computed location using associated AP %{private}s as the %{public}s centroid's LOI type %{private}s is not enabled"
+ "WifiCalc, skip updating computed location using associated AP %{private}s as we cannot determine the LOI type for the %{public}s centroid"
+ "WifiCalc, skip updating computed location using associated AP %{private}s with %{public}s centroid as distance %.1f is greater than threshold %.0f"
+ "WifiCalc, skip updating computed location using associated AP %{private}s with %{public}s centroid as server-side centroid from tile/als is invalid"
+ "WifiCalc, skip updating computed location using associated AP %{private}s with %{public}s centroid as server-side centroid from tile/als is unavailable"
+ "WifiCalc, updating wirelessClientInfo using associated AP %{private}s wifi-harvest centroid, latlon, %{sensitive}.7f, %{sensitive}.7f, acc, %{public}.1f"
+ "WifiCalc, using %{public}zu %{public}s samples for associated AP %{private}s from harvest database, computed centroid %{sensitive}s"
+ "WifiCalc, will update computed location using associated AP %{private}s with %{public}s centroid as distance %.1f is no more than threshold %.0f"
+ "WifiCalc, will update computed location using associated AP %{private}s with %{public}s centroid as stationary time %.1f is no less than threshold %.1f"
+ "WifiCalc, will update computed location using associated AP %{private}s with %{public}s centroid on residential devices"
+ "[ADHRCalorimetry][ADHRMets] cadence lock rejected, hr, %.0f, cadence, %.3f, agreement, %.4f, confidence, %.2f"
+ "[ADHRCalorimetry][ADHRMets] computeScaledHRMets, hr, %.0f, effectiveHRMin, %.0f, sedentaryHRMin, %.0f, demographicHRMin, %.0f, hrmax, %.0f, age, %.0f, vo2max, %.2f"
+ "[CLSPU][%hhu] Send command failed %s"
+ "[CLSPU][%hhu] Sending CameraDebug command %hhu"
+ "[SidebandSensorFusion] configuring,imuIndex,%{public}d,enableCount,%{public}d,latencyCount,%{public}d,snoopCount,%{public}d"
+ "[SidebandSensorFusion] imuIndex %{public}d out of range, device has %{public}d IMUs; ignoring"
+ "[SidebandSensorFusion] setGyroLowNoiseMode: CLGyro1 not available, ignoring imuIndex,1"
+ "_ambiguousCountryRetryTimeout"
+ "_hasUsedAmbiguousRetry"
+ "_lastAmbiguousCountryCodes"
+ "_lastAmbiguousDisputedState"
+ "_lastInputLocationTimeOfPriorBatch"
+ "_startsNewSegment"
+ "accelBias0"
+ "accelBias1"
+ "ambiguousCountryRetryTimeout"
+ "auto CLGnssController::driveDeviceGpsGalState()::(anonymous class)::operator()() const"
+ "batchIndex"
+ "bool CLMotionCoprocessor::setGyroLowNoiseMode(bool, uint8_t)"
+ "bool CLParkedCarMonitor::setLastParkedCarEvent(const CLParkedCarEvent &, bool)"
+ "bool CLWifiPositionCalculatorWithAssociatedAp::shouldUsePersonalizedCentroid(const CLWifiAccessPoint &, AssociatedApCentroidFetchOutcome, double)"
+ "bool computeDenseUrbanRatioQualifiesForIOFusionWithContext(NSArray<CLTripSegmentLocation *> *, double, size_t, size_t, bool, bool, double)"
+ "buttonPress"
+ "cancelAmbiguousCountryRetry"
+ "com.apple.routesmoother.CoreRoutineFetchResults"
+ "deltaPositionAltimeterZ"
+ "down"
+ "errorDomain"
+ "fAmbiguousCountryRetryTimer"
+ "fetchType"
+ "gps-harvest"
+ "handleRecentHighConfidenceHeartRates:"
+ "hasUsedAmbiguousRetry"
+ "initWithStartTime:endTime:locationSamples:odometrySamples:altitudeSamples:is1HzData:workoutActivityType:startsNewSegment:"
+ "io"
+ "isDenseUrbanSignalEnvironment"
+ "isLocalCellTaggingEnabled"
+ "kCLLocationType_Cell"
+ "kCLLocationType_WiFi"
+ "kRapidReconnection"
+ "lastAmbiguousCountryCodes"
+ "lastAmbiguousDisputedState"
+ "local-store"
+ "makeBackfillDelta: unknown HKQuantityType identifier:%@"
+ "maxBridgeableGapSecondsFromStartTime:toEndTime:"
+ "postAmbiguousCountryResult"
+ "returnedSampleCount"
+ "routined_slow_to_respond_elevation"
+ "routined_slow_to_respond_io"
+ "routined_slow_to_respond_location"
+ "routined_unreachable"
+ "samplesPerSecond"
+ "setAmbiguousCountryRetryTimeout:"
+ "setHasUsedAmbiguousRetry:"
+ "setLastAmbiguousCountryCodes:"
+ "setLastAmbiguousDisputedState:"
+ "setNPDREnable error - service not available"
+ "shouldRetryIfAmbiguousResult"
+ "startsNewSegment"
+ "static bool CLADHRMetsModel::isHRElevated(float, float, float)"
+ "static bool CLCellLocalTaggingSettings::isEnabled()_block_invoke"
+ "static bool CLFenceMonitorLogic::applyWirelessClientInfoCoordinatesForGeofence(CLDaemonLocation &, CLDaemonLocationPrivate &, const CLFenceManager_Type::Fence &)"
+ "static bool CLTileOptimizationManager::isEnabled()_block_invoke"
+ "static void CLVehicleHeadingEstimator::ageOutStaleHeartbeatState(HeadingEstimationFilterParameters &, const CFTimeInterval)"
+ "stopLessDesirableProviders,got better location provider,%{public}d,NOT stopping worse location provider,%{public}d,keepWifiUpWhileGpsOrAccessoryEngaged,1"
+ "submitCoreRoutineFetchReplyAnalyticsEventForType:intervalIndex:callId:result:fetchTimeMsec:returnedSampleCount:fetchIntervalDurationSeconds:samplesPerSecond:error:"
+ "submitCoreRoutineFetchResultAnalyticsEventForType:intervalIndex:result:fetchTimeMsec:returnedSampleCount:fetchIntervalDurationSeconds:samplesPerSecond:error:"
+ "syncgetCellServerLocation:forCell:"
+ "usage"
+ "usagePage"
+ "v1632@0:8{NotificationData={Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}id{FenceMonitorAnalytics=i{CLFenceAnalyticsGeofenceEventTimes=Bdddddddddddddd}d{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}iiiddddddd{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}B}}16"
+ "v1636@0:8i16{NotificationData={Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}id{FenceMonitorAnalytics=i{CLFenceAnalyticsGeofenceEventTimes=Bdddddddddddddd}d{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}iiiddddddd{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}B}}20"
+ "v1640@0:8{NotificationData={Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}id{FenceMonitorAnalytics=i{CLFenceAnalyticsGeofenceEventTimes=Bdddddddddddddd}d{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}iiiddddddd{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}B}}16@?1632"
+ "v1644@0:8{NotificationData={Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}id{FenceMonitorAnalytics=i{CLFenceAnalyticsGeofenceEventTimes=Bdddddddddddddd}d{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}iiiddddddd{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}B}}16B1632@?1636"
+ "v1840@0:8{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}{shared_ptr<const gnss::MeasurementData>=^{MeasurementData}^{__shared_weak_count}}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLBasebandTimeFreqTransfer=d{CLBasebandSystemClock=Qffdfd}Qf{LeapSecondInfo=sC{LeapSecondChange=Qs}}}{CLGnssBasebandCausesL1InterferenceGnssBandChangeData=ii}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}}16"
+ "v1844@0:8i16{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}{shared_ptr<const gnss::MeasurementData>=^{MeasurementData}^{__shared_weak_count}}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLBasebandTimeFreqTransfer=d{CLBasebandSystemClock=Qffdfd}Qf{LeapSecondInfo=sC{LeapSecondChange=Qs}}}{CLGnssBasebandCausesL1InterferenceGnssBandChangeData=ii}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}}20"
+ "v1856@0:8{shared_ptr<CLBarometerCalibration_Types::CLBarometerCalibrationLocationData>=^{CLBarometerCalibrationLocationData}^{__shared_weak_count}}16{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}{shared_ptr<const gnss::MeasurementData>=^{MeasurementData}^{__shared_weak_count}}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLBasebandTimeFreqTransfer=d{CLBasebandSystemClock=Qffdfd}Qf{LeapSecondInfo=sC{LeapSecondChange=Qs}}}{CLGnssBasebandCausesL1InterferenceGnssBandChangeData=ii}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}}32"
+ "v32@?0B8@?<{DaemonLocation={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}}@?>12i20d24"
+ "v36@0:8@?<{DaemonLocation={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}}@?>16B24@?<v@?B@?<{DaemonLocation={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}}@?>id>28"
+ "v52@?0I8^@12{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}20d44"
+ "v72@0:8Q16I24Q28i36Q40d48d56@64"
+ "v80@0:8Q16I24Q28Q36i44Q48d56d64@72"
+ "virtual bool CLSPU::configureDevMotion3(uint8_t, bool, uint8_t)"
+ "virtual void CLStepCountHealthKitWriter::writeDatumsFromBackfilledRecords(HKQuantityTypeIdentifier _Nonnull, CFAbsoluteTime, CFAbsoluteTime)"
+ "void CLAOP2Motion::setNPDREnable(bool)"
+ "void CLGnssController::cancelDeviceGpsGalTransition()"
+ "void CLGnssController::driveDeviceGpsGalState()"
+ "void CLMotionCoprocessor::updateSidebandSensorFusion(uint8_t)_block_invoke"
+ "void CLParkedCarMonitor::copyPersistentStoreToRoutineApp()"
+ "void CLParkedCarMonitor::invalidateLastParkedCarEventInMemory()"
+ "void CLParkedCarMonitor::invalidatePersistedParkedCarLocationAndHeading()"
+ "void CLWifiPositionCalculatorWithAssociatedAp::updateWirelessClientInfoUsingWifiHarvestCentroid(CL::Wifi1::Types::ComputedLocation &)"
+ "wifi-harvest"
+ "yOffset"
+ "{\"msg%{public}.0s\":\"#Warning got invalid location for WCI client, not sending\", \"client\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"ambiguous country retry timer fired, posting cached ambiguous result\"}"
+ "{\"msg%{public}.0s\":\"device with multiple territory results, retry already in progress\"}"
+ "{\"msg%{public}.0s\":\"got non-ambiguous country result, cancelling retry timer\"}"
+ "{\"msg%{public}.0s\":\"multiple territory results, requesting best accuracy and starting retry timer\", \"timeout\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"posting cached ambiguous country result as fallback\"}"
+ "{\"msg%{public}.0s\":\"settings initialized\", \"AllowSimulatedLocations\":%{public}hhd, \"CountryLocationMinimumConfidence\":%{public}d, \"MaximumCountryLocationChangeSpeed\":\"%{public}f\", \"MaximumCountryLocationChangeAccuracy\":\"%{public}f\", \"MinimumMoveDistance\":\"%{public}f\", \"CountryLocationDebounceTime\":\"%{public}f\", \"CountryLocationStalenessTime\":\"%{public}f\", \"TimeToCountryUnknown\":\"%{public}f\", \"MinimumTimeBetweenExpensiveQueries\":\"%{public}f\", \"AmbiguousCountryRetryTimeout\":\"%{public}f\", \"TimeToCountryCheapLocation\":\"%{public}f\"}"
+ "{\"msg%{public}.0s\":\"settings updated\", \"AllowSimulatedLocations\":%{public}hhd, \"CountryLocationMinimumConfidence\":%{public}d, \"MaximumCountryLocationChangeSpeed\":\"%{public}f\", \"MaximumCountryLocationChangeAccuracy\":\"%{public}f\", \"MinimumMoveDistance\":\"%{public}f\", \"CountryLocationDebounceTime\":\"%{public}f\", \"CountryLocationStalenessTime\":\"%{public}f\", \"TimeToCountryUnknown\":\"%{public}f\", \"TimeToCountryCheapLocation\":\"%{public}f\", \"TimeToRequestCheapActiveLocation\":\"%{public}f\", \"MinimumTimeBetweenExpensiveQueries\":\"%{public}f\", \"AmbiguousCountryRetryTimeout\":\"%{public}f\", \"CountryDebounceInterval\":%{public}d}"
+ "{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}16@0:8"
+ "{CLTrackingAvoidanceMetrics=\"state\"{CLTaMetricState=\"uniqueIds\"{set<std::string, std::less<std::string>, std::allocator<std::string>>=\"__tree_\"{__tree<std::string, std::less<std::string>, std::allocator<std::string>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"detectedIds\"{map<std::string, int, std::less<std::string>, std::allocator<std::pair<const std::string, int>>>=\"__tree_\"{__tree<std::__value_type<std::string, int>, std::__map_value_compare<std::string, std::pair<const std::string, int>, std::less<std::string>>, std::allocator<std::pair<const std::string, int>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"suspiciousVisits\"i\"suspiciousGeneral\"i\"suspiciousOther\"i\"timeNextSent\"d\"sendHour\"i\"unitTest\"B\"nextWeeklySubmissionTime\"d\"weeklyCountOfSuspiciousDevices\"I\"nextMonthlySubmissionTime\"d\"monthlyCountOfSuspiciousDevices\"I}\"signalEnvironment\"i\"lastLocation\"{CLDaemonLocation=\"suitability\"i\"coordinate\"{?=\"latitude\"d\"longitude\"d}\"horizontalAccuracy\"d\"altitude\"d\"verticalAccuracy\"d\"speed\"d\"speedAccuracy\"d\"course\"d\"courseAccuracy\"d\"timestamp\"d\"confidence\"i\"lifespan\"d\"type\"i\"rawCoordinate\"{?=\"latitude\"d\"longitude\"d}\"rawCourse\"d\"floor\"i\"integrity\"I\"referenceFrame\"i\"rawReferenceFrame\"i\"signalEnvironmentType\"i\"ellipsoidalAltitude\"d\"fromSimulationController\"B}\"lastLocationPrivate\"{CLDaemonLocationPrivate=\"odometer\"d\"deltaDistance\"d\"deltaDistanceAccuracy\"d\"timestampGps\"d\"machtime\"d\"horzUncSemiMaj\"f\"horzUncSemiMin\"f\"horzUncSemiMajAz\"f\"isFitnessMatch\"B\"matchQuality\"i\"matchCoordinate\"{?=\"latitude\"d\"longitude\"d}\"matchCourse\"d\"matchFormOfWay\"i\"matchRoadClass\"i\"matchShifted\"B\"mapMatcherData\"{?=\"rawUnmodifiedCourse\"d\"rawUnmodifiedCourseUnc\"d\"isStatic\"B\"isMounted\"B\"estimatedLane\"i\"estimatedLaneProbability\"d\"estimatedLaneFeatureID\"q\"flowlineSnapLat\"d\"flowlineSnapLon\"d\"flowlineSnapCourse\"d}\"trackRunData\"{?=\"lapInformation\"{?=\"lapCount\"i\"currentLapStartTime\"d\"currentLapDurationInSeconds\"d\"currentLapDistanceInMeters\"d\"previousLapDurationInSeconds\"d\"previousLapDistanceInMeters\"d\"previousLapPositionAtCompletionInDegrees\"{?=\"latitude\"d\"longitude\"d}\"currentTrackRunSessionDurationInSeconds\"d\"currentTrackRunSessionDistanceInMeters\"d}\"laneNumber\"i\"trackId\"Q\"estimatedLaneNumber\"i\"laneCount\"i\"estimatedLaneConfidence\"i\"trackProximity\"i\"distanceToTrackMeters\"d\"odometerHasBeenCorrected\"B}\"pressure\"{?=\"value\"d\"std\"d}\"undulationModel\"i\"undulation\"f\"specialCoordinate\"{?=\"latitude\"d\"longitude\"d}\"specialHorizontalAccuracy\"d\"machContinuousTime\"d\"originDevice\"i\"isMatcherPropagatedCoordinates\"B\"slope\"d\"maxAbsSlope\"d\"groundAltitude\"d\"groundAltitudeUncertainty\"d\"rawHorizontalAccuracy\"d\"preFusingAltitude\"d\"preFusingVerticalAccuracy\"d\"rawCourseAccuracy\"d\"isCoordinateFused\"B\"isCoordinateFusedWithVL\"B\"fusedCoordinate\"{?=\"latitude\"d\"longitude\"d}\"fusedHorizontalAccuracy\"d\"fusedReferenceFrame\"i\"fusedAltitude\"d\"fusedVerticalAccuracy\"d\"fusedCourse\"d\"fusedCourseAccuracy\"d\"smoothedGPSAltitude\"d\"smoothedGPSAltitudeUncertainty\"d\"isSimulatedOrSpoofed\"B\"satelliteVisibilityReport\"{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=\"__ptr_\"^{AboveHorizonSatelliteVisibilityReport}\"__cntrl_\"^{__shared_weak_count}}\"gnssContent\"i\"rawAltitude\"{AltitudeInfo=\"altitude\"d\"verticalAccuracy\"d\"undulation\"d\"undulationModel\"i}\"estimatedPositionContextState\"C\"estimatedPositionContextStateProbabilityIndoor\"d\"estimatedPositionContextStateProbabilityOutdoor\"d\"estimatedWorstCaseError\"d\"wifiFixType\"C\"mapMatcherType\"C\"isRouteHintsTriggeredMapMatching\"B\"loiLocationSourceAccuracy\"i\"batchedLocationFixType\"i\"wifiZaxisData\"{?=\"numberOfZaxisSlamApsUsed\"I}\"demFlatnessMetricData\"{?=\"demNumContiguousFlatPoints\"i\"confidence\"f}\"accessoryLocationType\"i\"gnssEstimatorSource\"i\"numRavenAcceptedGnssRangeMeasurements\"i\"isTrustedForTimeZone\"B\"attitude_ECEF2Device_Q1\"f\"attitude_ECEF2Device_Q2\"f\"attitude_ECEF2Device_Q3\"f\"attitude_ECEF2Device_Q4\"f\"deviceAttitudeApplicabilityTimeMctSec\"d\"wirelessClientInfo\"{?=\"latitudeDegrees\"d\"longitudeDegrees\"d\"mslAltitudeMeters\"d\"horizontalAccuracyMeters\"f\"verticalAccuracyMeters\"f\"speedMetersPerSecond\"f\"speedAccuracyMetersPerSecond\"f\"courseDegrees\"f\"courseAccuracyDegrees\"f}}}"
+ "{DaemonLocation={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}}8@?0"
- "#Error,WCI-fusion,getWCIFusedLocation failed,WCI fusion is disabled."
- "#pcm, failed to fetch disconnection location, will attempt again upon exit detection"
- "#pcm, failed to update disconnection location"
- "#wci,GnssRestrictedMode,downgrade,stopCompleted,startingDevice"
- "#wci,GnssRestrictedMode,receivedRequestWhileRestartInFlight,requestedEnable,%{public}d,ignored,keptCurrent,%{public}d"
- "#wci,ggselector,enableRecordInternalState"
- "#wci,stopLessDesirableProviders,got better location provider,%{public}d,NOT stopping worse location provider,%{public}d,keepWifiUpWhileGpsOrAccessoryEngaged,1"
- "%s NIO on AOP2"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:122: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:127: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:158: libc++ Hardening assertion __i != __last failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/nth_element.h:164: libc++ Hardening assertion __j != __first failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:512: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:525: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__bit_reference:113: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__memory/unique_ptr.h:583: libc++ Hardening assertion __checker_.__in_bounds<deleter_type>(std::__to_address(__ptr_), __i) failed: unique_ptr<T[]>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1171: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:419: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:434: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:438: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:442: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:446: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:509: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:297: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:302: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:317: libc++ Hardening assertion !empty() failed: vector<bool>::back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/array:279: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/array:284: libc++ Hardening assertion __n < _Size failed: out-of-bounds access in std::array<T, N>\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1534: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1542: libc++ Hardening assertion __i < size() failed: deque::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1565: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1571: libc++ Hardening assertion !empty() failed: deque::front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1577: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:1584: libc++ Hardening assertion !empty() failed: deque::back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2199: libc++ Hardening assertion !empty() failed: deque::pop_front called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2213: libc++ Hardening assertion !empty() failed: deque::pop_back called on an empty deque\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2341: libc++ Hardening assertion __f != end() failed: deque::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/deque:2367: libc++ Hardening assertion __f <= __l failed: deque::erase(first, last) called with an invalid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:1394: libc++ Hardening assertion !empty() failed: list::pop_front() called with empty list\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:1403: libc++ Hardening assertion !empty() failed: list::pop_back() called on an empty list\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:1412: libc++ Hardening assertion __p != end() failed: list::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:1500: libc++ Hardening assertion this != std::addressof(__c) failed: list::splice(iterator, list) called with this == &list\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:830: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:834: libc++ Hardening assertion !empty() failed: list::front called on empty list\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:838: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/list:842: libc++ Hardening assertion !empty() failed: list::back called on empty list\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1112: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1121: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1130: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1139: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/streambuf:301: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gnext) failed: [gbeg, gnext) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/streambuf:302: libc++ Hardening assertion std::__is_valid_range(__gbeg, __gend) failed: [gbeg, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/streambuf:303: libc++ Hardening assertion std::__is_valid_range(__gnext, __gend) failed: [gnext, gend) must be a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1362: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:1371: libc++ Hardening assertion __pos <= size() failed: string index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:3374: libc++ Hardening assertion __pos != end() failed: string::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string:3393: libc++ Hardening assertion !empty() failed: string::pop_back(): string is already empty\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:343: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "20:15:35"
- "20:26:30"
- "@68@0:8d16d24@32@40@48B56Q60"
- "AngleCalibrationEstimate"
- "AnglePowerLog"
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 234,invalid col %zu > %zu."
- "Assertion failed: col < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 240,invalid col %zu > %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 235,invalid element %zu <= %zu."
- "Assertion failed: col > row, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 241,invalid element %zu <= %zu."
- "Assertion failed: i0 < N-Ni+1 && j0 < N-Nj+1, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 305,indices exceed factored matrix size."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 189,invalid row %zu > %zu."
- "Assertion failed: row < N, file /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 194,invalid row %zu > %zu."
- "B1624@0:8{NotificationData={Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}id{FenceMonitorAnalytics=i{CLFenceAnalyticsGeofenceEventTimes=Bdddddddddddddd}d{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}iiiddddddd{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}}}16"
- "B1840@0:8{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}{shared_ptr<const gnss::MeasurementData>=^{MeasurementData}^{__shared_weak_count}}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLBasebandTimeFreqTransfer=d{CLBasebandSystemClock=Qffdfd}Qf{LeapSecondInfo=sC{LeapSecondChange=Qs}}}{CLGnssBasebandCausesL1InterferenceGnssBandChangeData=ii}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}}16"
- "CDMA local harvesting not done"
- "CELL_LOC: cell (%s) is local <%{sensitive}+.8f,%{sensitive}+.8f> remote <%{sensitive}+.8f,%{sensitive}+.8f> only %.2fm apart - not storing locally"
- "CELL_LOC: cell (%s) is local at <%{sensitive}+.8f,%{sensitive}+.8f>"
- "CELL_LOC: distance, %.1lf, not storing locally, %s, location, %{sensitive}s"
- "CELL_LOC: distance, %.1lf, override local location, %s, location, %{sensitive}s"
- "CLRS,1Hz TSP path,isIOSupportedWorkoutType,%d,ratioOfLocationsThatAreDenseUrban,%{public}.1lf,routeLinearity,%{public}.3lf,isMajorityDUArea,%{public}d,is1HzDataRequiringIOFusion,%{public}d"
- "CLRS,1Hz TSP,enableIOFusion,%{public}d,isDUArea,%{public}d,routeLinearity,%{public}.3f"
- "CLRS,fetch locations completion block,hadLocationFetchError,%{public}d,jj,%{public}u,is1HzData,%{public}d"
- "CLRS,fetchBackgroundInertialOdometrySamplesWithStartTime,startTime,%{public}.1lf,endTime,%{public}.1lf,buffer,%{public}.1lf,intervalIndex,%{public}u"
- "CLRS,final batch with <2 samples but has context to flush,count,%{public}zu,contextLoc,%{public}lu"
- "CLRS,gap found,time,%{public}.1lf,gap duration,%{public}.1lf"
- "CLRS,gapDetection,batchSPI,%{public}d,activity,%{public}d,ioCanBridgeGap,%{public}d,gap,%{public}.1lf,kMaxGapWithinInterval_s,%{public}.1lf"
- "CLRS,shouldFetchIOSamplesForInterval,workoutActivity,%{public}d,totalLocations,%{public}lu,denseUrbanCount,%{public}lu,denseUrbanPercentage,%{public}.2f,ioSupportedWorkoutType,%{public}d,hasSufficientDenseUrbanLocations,%{public}d"
- "CLRS,synthesizedFlushInterval,batchType,Final"
- "CLStepCountHealthKitWriter::getDatumsFromBackfilledRecords()"
- "CLWifiAccessPoint CLWifiPositionCalculatorWithAssociatedAp::calculateAssociatedApCentroidFromHarvestDatabase(std::shared_ptr<CLWifiAssociatedApHarvestDatabase>, const std::string &, const CFTimeInterval &)"
- "CellQuery, ignore, matched, %{public}d, %{private}s"
- "EnablePedNetInference set to %{public}d, PednetRunSubset set to %{public}d"
- "Failed to %s NIO on AOP2, err %d"
- "Foreground NIO: %{public}d"
- "GSM local harvesting not done"
- "HK collector %s, last persisted with time %{public}f"
- "Jun 18 2026"
- "Jun 18 2026 20:21:08"
- "LTE local harvesting not done"
- "Legacy CDMA local harvesting not done"
- "Legacy GSM local harvesting not done"
- "Legacy LTE local harvesting not done"
- "Legacy NR local harvesting not done"
- "Legacy SCDMA local harvesting not done"
- "NR local harvesting not done"
- "PedNet inference disabled via EnablePedNetInference defaults write"
- "SCDMA local harvesting not done"
- "WifiCalc, skip updating computed location using associated AP %{private}s as distance %.1f is greater than threshold %.0f"
- "WifiCalc, skip updating computed location using associated AP %{private}s as it does not have a valid centroid!"
- "WifiCalc, skip updating computed location using associated AP %{private}s as it fails to pass cross-check with GPS/Cell!"
- "WifiCalc, skip updating computed location using associated AP %{private}s as it is KnownAC"
- "WifiCalc, skip updating computed location using associated AP %{private}s as its LOI type %{private}s is not enabled"
- "WifiCalc, skip updating computed location using associated AP %{private}s as its uncertainty %{public}.1f is greater than %{public}.1f"
- "WifiCalc, skip updating computed location using associated AP %{private}s as server-side centroid from tile/als is invalid"
- "WifiCalc, skip updating computed location using associated AP %{private}s as server-side centroid from tile/als is unavailable"
- "WifiCalc, skip updating computed location using associated AP %{private}s as we cannot determine its LOI type"
- "WifiCalc, using %{public}zu %{public}s harvest samples for associated AP %{private}s from harvest database, computed centroid %{sensitive}s"
- "WifiCalc, will update computed location using associated AP %{private}s as distance %.1f is no more than threshold %.0f"
- "WifiCalc, will update computed location using associated AP %{private}s as stationary time %.1f is no less than threshold %.1f"
- "WifiCalc, will update computed location using associated AP %{private}s on residential devices"
- "[ADHRCalorimetry][ADHRMets] computeScaledHRMets, hr, %.0f, hrmin, %.0f, hrmax, %.0f, age, %.0f, vo2max, %.2f"
- "[CLSPU] Send command failed %s"
- "[CLSPU] Sending CameraDebug command %hhu"
- "[SidebandSensorFusion] configuring,enableCount,%{public}d,latencyCount,%{public}d,snoopCount,%{public}d"
- "_foregroundNIOClientCount"
- "auto CLGnssController::setGnssRestrictedMode(bool)::(anonymous class)::operator()() const"
- "bool CLWifiPositionCalculatorWithAssociatedAp::shouldUpdateComputedLocation()"
- "cell %03d %03d 0x%x 0x%x is local <%{sensitive}+.8f,%{sensitive}+.8f> remote <%{sensitive}+.8f,%{sensitive}+.8f> only %.2fm apart - not storing locally"
- "cell %03d %03d 0x%x 0x%x is local at <%{sensitive}+.8f,%{sensitive}+.8f>"
- "com.apple.routesmoother.BackgroundIOFetchResults"
- "com.apple.routesmoother.LocationFetchResults"
- "didHaveError"
- "error adding elevations to routine: %@"
- "errorMessage"
- "initWithStartTime:endTime:locationSamples:odometrySamples:altitudeSamples:is1HzData:workoutActivityType:"
- "isActivityIOSupportedFromStartTime:toEndTime:"
- "scdma cell %03d %03d 0x%x 0x%x is local <%{sensitive}+.8f,%{sensitive}+.8f> remote <%{sensitive}+.8f,%{sensitive}+.8f> only %.2fm apart - not storing locally"
- "scdma cell %03d %03d 0x%x 0x%x is local at <%{sensitive}+.8f,%{sensitive}+.8f>"
- "setForegroundNIOActive:"
- "setInertialOdometryEnable error - service not available"
- "setNIOEnable error - service not available"
- "static bool CLADHRMetsModel::isHRElevated(float, const CLBodyMetrics &)"
- "v1624@0:8{NotificationData={Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}id{FenceMonitorAnalytics=i{CLFenceAnalyticsGeofenceEventTimes=Bdddddddddddddd}d{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}iiiddddddd{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}}}16"
- "v1628@0:8i16{NotificationData={Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}id{FenceMonitorAnalytics=i{CLFenceAnalyticsGeofenceEventTimes=Bdddddddddddddd}d{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}iiiddddddd{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}}}20"
- "v1632@0:8{NotificationData={Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}id{FenceMonitorAnalytics=i{CLFenceAnalyticsGeofenceEventTimes=Bdddddddddddddd}d{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}iiiddddddd{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}}}16@?1624"
- "v1636@0:8{NotificationData={Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{Fence={basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}ddddddddiiidQiiBiiB{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}{CLStrongPtr<NSUUID *>=@}{vector<CLClientLocationCoordinate, std::allocator<CLClientLocationCoordinate>>=^{?}^{?}{?=^{?}}}}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}id{FenceMonitorAnalytics=i{CLFenceAnalyticsGeofenceEventTimes=Bdddddddddddddd}d{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}iiiddddddd{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}{CLMotionActivity=iiiiiidBfdBidi{FsmTransitionData=CCCS} dii{?=b1b1b1b1b1}iidQi}}}16B1624@?1628"
- "v1840@0:8{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}{shared_ptr<const gnss::MeasurementData>=^{MeasurementData}^{__shared_weak_count}}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLBasebandTimeFreqTransfer=d{CLBasebandSystemClock=Qffdfd}Qf{LeapSecondInfo=sC{LeapSecondChange=Qs}}}{CLGnssBasebandCausesL1InterferenceGnssBandChangeData=ii}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}}16"
- "v1844@0:8i16{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}{shared_ptr<const gnss::MeasurementData>=^{MeasurementData}^{__shared_weak_count}}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLBasebandTimeFreqTransfer=d{CLBasebandSystemClock=Qffdfd}Qf{LeapSecondInfo=sC{LeapSecondChange=Qs}}}{CLGnssBasebandCausesL1InterferenceGnssBandChangeData=ii}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}}20"
- "v1856@0:8{shared_ptr<CLBarometerCalibration_Types::CLBarometerCalibrationLocationData>=^{CLBarometerCalibrationLocationData}^{__shared_weak_count}}16{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}{shared_ptr<const gnss::MeasurementData>=^{MeasurementData}^{__shared_weak_count}}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLBasebandTimeFreqTransfer=d{CLBasebandSystemClock=Qffdfd}Qf{LeapSecondInfo=sC{LeapSecondChange=Qs}}}{CLGnssBasebandCausesL1InterferenceGnssBandChangeData=ii}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}}32"
- "v32@?0B8@?<{DaemonLocation={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiBffffd{?=dddffffff}}}@?>12i20d24"
- "v36@0:8@?<{DaemonLocation={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiBffffd{?=dddffffff}}}@?>16B24@?<v@?B@?<{DaemonLocation={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiBffffd{?=dddffffff}}}@?>id>28"
- "virtual NSMutableArray<HKQuantityDatum *> * _Nullable CLStepCountHealthKitWriter::getDatumsFromBackfilledRecords(CFAbsoluteTime, CFAbsoluteTime)"
- "virtual bool CLSPU::configureDevMotion3()"
- "void CLAOP2Motion::setInertialOdometryEnable(bool)"
- "void CLAOP2Motion::setNIOEnable(bool)"
- "void CLMotionCoprocessor::updateSidebandSensorFusion()_block_invoke"
- "yield"
- "{\"msg%{public}.0s\":\"settings initialized\", \"AllowSimulatedLocations\":%{public}hhd, \"CountryLocationMinimumConfidence\":%{public}d, \"MaximumCountryLocationChangeSpeed\":\"%{public}f\", \"MaximumCountryLocationChangeAccuracy\":\"%{public}f\", \"MinimumMoveDistance\":\"%{public}f\", \"CountryLocationDebounceTime\":\"%{public}f\", \"CountryLocationStalenessTime\":\"%{public}f\", \"TimeToCountryUnknown\":\"%{public}f\", \"MinimumTimeBetweenExpensiveQueries\":\"%{public}f\", \"TimeToCountryCheapLocation\":\"%{public}f\"}"
- "{\"msg%{public}.0s\":\"settings updated\", \"AllowSimulatedLocations\":%{public}hhd, \"CountryLocationMinimumConfidence\":%{public}d, \"MaximumCountryLocationChangeSpeed\":\"%{public}f\", \"MaximumCountryLocationChangeAccuracy\":\"%{public}f\", \"MinimumMoveDistance\":\"%{public}f\", \"CountryLocationDebounceTime\":\"%{public}f\", \"CountryLocationStalenessTime\":\"%{public}f\", \"TimeToCountryUnknown\":\"%{public}f\", \"TimeToCountryCheapLocation\":\"%{public}f\", \"TimeToRequestCheapActiveLocation\":\"%{public}f\", \"MinimumTimeBetweenExpensiveQueries\":\"%{public}f\", \"CountryDebounceInterval\":%{public}d}"
- "{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiBffffd{?=dddffffff}}16@0:8"
- "{CLTrackingAvoidanceMetrics=\"state\"{CLTaMetricState=\"uniqueIds\"{set<std::string, std::less<std::string>, std::allocator<std::string>>=\"__tree_\"{__tree<std::string, std::less<std::string>, std::allocator<std::string>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"detectedIds\"{map<std::string, int, std::less<std::string>, std::allocator<std::pair<const std::string, int>>>=\"__tree_\"{__tree<std::__value_type<std::string, int>, std::__map_value_compare<std::string, std::pair<const std::string, int>, std::less<std::string>>, std::allocator<std::pair<const std::string, int>>>=\"__begin_node_\"^v\"\"{?=\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"\"{?=\"__size_\"Q}}}\"suspiciousVisits\"i\"suspiciousGeneral\"i\"suspiciousOther\"i\"timeNextSent\"d\"sendHour\"i\"unitTest\"B\"nextWeeklySubmissionTime\"d\"weeklyCountOfSuspiciousDevices\"I\"nextMonthlySubmissionTime\"d\"monthlyCountOfSuspiciousDevices\"I}\"signalEnvironment\"i\"lastLocation\"{CLDaemonLocation=\"suitability\"i\"coordinate\"{?=\"latitude\"d\"longitude\"d}\"horizontalAccuracy\"d\"altitude\"d\"verticalAccuracy\"d\"speed\"d\"speedAccuracy\"d\"course\"d\"courseAccuracy\"d\"timestamp\"d\"confidence\"i\"lifespan\"d\"type\"i\"rawCoordinate\"{?=\"latitude\"d\"longitude\"d}\"rawCourse\"d\"floor\"i\"integrity\"I\"referenceFrame\"i\"rawReferenceFrame\"i\"signalEnvironmentType\"i\"ellipsoidalAltitude\"d\"fromSimulationController\"B}\"lastLocationPrivate\"{CLDaemonLocationPrivate=\"odometer\"d\"deltaDistance\"d\"deltaDistanceAccuracy\"d\"timestampGps\"d\"machtime\"d\"horzUncSemiMaj\"f\"horzUncSemiMin\"f\"horzUncSemiMajAz\"f\"isFitnessMatch\"B\"matchQuality\"i\"matchCoordinate\"{?=\"latitude\"d\"longitude\"d}\"matchCourse\"d\"matchFormOfWay\"i\"matchRoadClass\"i\"matchShifted\"B\"mapMatcherData\"{?=\"rawUnmodifiedCourse\"d\"rawUnmodifiedCourseUnc\"d\"isStatic\"B\"isMounted\"B\"estimatedLane\"i\"estimatedLaneProbability\"d\"estimatedLaneFeatureID\"q\"flowlineSnapLat\"d\"flowlineSnapLon\"d\"flowlineSnapCourse\"d}\"trackRunData\"{?=\"lapInformation\"{?=\"lapCount\"i\"currentLapStartTime\"d\"currentLapDurationInSeconds\"d\"currentLapDistanceInMeters\"d\"previousLapDurationInSeconds\"d\"previousLapDistanceInMeters\"d\"previousLapPositionAtCompletionInDegrees\"{?=\"latitude\"d\"longitude\"d}\"currentTrackRunSessionDurationInSeconds\"d\"currentTrackRunSessionDistanceInMeters\"d}\"laneNumber\"i\"trackId\"Q\"estimatedLaneNumber\"i\"laneCount\"i\"estimatedLaneConfidence\"i\"trackProximity\"i\"distanceToTrackMeters\"d\"odometerHasBeenCorrected\"B}\"pressure\"{?=\"value\"d\"std\"d}\"undulationModel\"i\"undulation\"f\"specialCoordinate\"{?=\"latitude\"d\"longitude\"d}\"specialHorizontalAccuracy\"d\"machContinuousTime\"d\"originDevice\"i\"isMatcherPropagatedCoordinates\"B\"slope\"d\"maxAbsSlope\"d\"groundAltitude\"d\"groundAltitudeUncertainty\"d\"rawHorizontalAccuracy\"d\"preFusingAltitude\"d\"preFusingVerticalAccuracy\"d\"rawCourseAccuracy\"d\"isCoordinateFused\"B\"isCoordinateFusedWithVL\"B\"fusedCoordinate\"{?=\"latitude\"d\"longitude\"d}\"fusedHorizontalAccuracy\"d\"fusedReferenceFrame\"i\"fusedAltitude\"d\"fusedVerticalAccuracy\"d\"fusedCourse\"d\"fusedCourseAccuracy\"d\"smoothedGPSAltitude\"d\"smoothedGPSAltitudeUncertainty\"d\"isSimulatedOrSpoofed\"B\"satelliteVisibilityReport\"{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=\"__ptr_\"^{AboveHorizonSatelliteVisibilityReport}\"__cntrl_\"^{__shared_weak_count}}\"gnssContent\"i\"rawAltitude\"{AltitudeInfo=\"altitude\"d\"verticalAccuracy\"d\"undulation\"d\"undulationModel\"i}\"estimatedPositionContextState\"C\"estimatedPositionContextStateProbabilityIndoor\"d\"estimatedPositionContextStateProbabilityOutdoor\"d\"estimatedWorstCaseError\"d\"wifiFixType\"C\"mapMatcherType\"C\"isRouteHintsTriggeredMapMatching\"B\"loiLocationSourceAccuracy\"i\"batchedLocationFixType\"i\"wifiZaxisData\"{?=\"numberOfZaxisSlamApsUsed\"I}\"demFlatnessMetricData\"{?=\"demNumContiguousFlatPoints\"i\"confidence\"f}\"accessoryLocationType\"i\"gnssEstimatorSource\"i\"isTrustedForTimeZone\"B\"attitude_ECEF2Device_Q1\"f\"attitude_ECEF2Device_Q2\"f\"attitude_ECEF2Device_Q3\"f\"attitude_ECEF2Device_Q4\"f\"deviceAttitudeApplicabilityTimeMctSec\"d\"wirelessClientInfo\"{?=\"latitudeDegrees\"d\"longitudeDegrees\"d\"mslAltitudeMeters\"d\"horizontalAccuracyMeters\"f\"verticalAccuracyMeters\"f\"speedMetersPerSecond\"f\"speedAccuracyMetersPerSecond\"f\"courseDegrees\"f\"courseAccuracyDegrees\"f}}}"
- "{DaemonLocation={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiBffffd{?=dddffffff}}}8@?0"

```
