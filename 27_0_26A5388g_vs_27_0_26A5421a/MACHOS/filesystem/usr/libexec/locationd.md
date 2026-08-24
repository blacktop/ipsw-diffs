## locationd

> `/usr/libexec/locationd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_classname`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3183.0.0.0.0
-  __TEXT.__text: 0x67e2e0
+3185.0.6.0.0
+  __TEXT.__text: 0x68800c
   __TEXT.__auth_stubs: 0x38f0
-  __TEXT.__objc_stubs: 0x10dc0
+  __TEXT.__objc_stubs: 0x10e00
   __TEXT.__init_offsets: 0x184
-  __TEXT.__objc_methlist: 0x12a38
-  __TEXT.__const: 0x17908
-  __TEXT.__gcc_except_tab: 0x2a918
-  __TEXT.__cstring: 0x7ac36
-  __TEXT.__oslogstring: 0x97c66
-  __TEXT.__objc_methname: 0x1fcce
+  __TEXT.__objc_methlist: 0x12a70
+  __TEXT.__const: 0x17f98
+  __TEXT.__gcc_except_tab: 0x2a958
+  __TEXT.__cstring: 0x7ae16
+  __TEXT.__oslogstring: 0x988d6
+  __TEXT.__objc_methname: 0x1fd8e
   __TEXT.__objc_classname: 0x33f4
-  __TEXT.__objc_methtype: 0xf15c
+  __TEXT.__objc_methtype: 0xf14c
   __TEXT.__ustring: 0x346
   __TEXT.__constg_swiftt: 0x424
   __TEXT.__swift5_typeref: 0x241

   __TEXT.__swift_as_cont: 0x10
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x1abb8
+  __TEXT.__unwind_info: 0x1aba8
   __TEXT.__eh_frame: 0x620
-  __DATA_CONST.__const: 0x2c058
-  __DATA_CONST.__cfstring: 0x15d40
+  __DATA_CONST.__const: 0x2bfb8
+  __DATA_CONST.__cfstring: 0x15d00
   __DATA_CONST.__objc_classlist: 0x8d0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x5b0

   __DATA_CONST.__auth_got: 0x1c98
   __DATA_CONST.__got: 0xc00
   __DATA_CONST.__auth_ptr: 0x2d0
-  __DATA.__objc_const: 0x1eb00
-  __DATA.__objc_selrefs: 0x7808
-  __DATA.__objc_ivar: 0x1290
+  __DATA.__objc_const: 0x1eb70
+  __DATA.__objc_selrefs: 0x7838
+  __DATA.__objc_ivar: 0x1298
   __DATA.__objc_data: 0x5b98
   __DATA.__data: 0x56e8
-  __DATA.__common: 0x7e8
-  __DATA.__bss: 0x2c50
+  __DATA.__common: 0x7d8
+  __DATA.__bss: 0x2c40
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 27069
+  Functions: 27076
   Symbols:   1391
-  CStrings:  24848
+  CStrings:  24919
 
CStrings:
+ "#gfm, checkForGpsFailure, GPS failure detected"
+ "#gfm, checkForGpsFailure, high map match confidence, smoothed, %{public}.3f, isSnapUsable, %{public}d"
+ "#gfm, checkForGpsFailure, in/near tunnel/bridge, current, %{public}d, recent, %{public}d, inTunnel, %{public}d, nearTunnel, %{public}d, nearBridge, %{public}d"
+ "#gfm, checkForGpsFailure, insufficient accurate GPS, count, %{public}d, threshold, %{public}d"
+ "#gfm, checkForGpsFailure, insufficient duration"
+ "#gfm, checkForGpsFailure, insufficient movement"
+ "#gfm, checkForGpsFailure, recent accessory location, age, %{public}.1f"
+ "#gfm, checkForGpsFailure, sufficient accurate GPS, count, %{public}d, threshold, %{public}d"
+ "#gfm, countAccurateGpsInWindow, window, %{public}.1f, count, %{public}d, bufferSize, %{public}zu"
+ "#gfm, getDisplacement, found motion, displacement, %{public}.1f, rmsHAcc, %{public}.1f, effective, %{public}.1f, threshold, %{public}.1f, timeSpan, %{public}.1f"
+ "#gfm, getDisplacement, no candidate met dynamic threshold"
+ "#gfm, getDisplacement, no locations"
+ "#gfm, getDisplacement, stale, age, %{public}.1f"
+ "#gfm, hasHealthySatelliteReception, medianSV, %{public}d, medianFrac, %{public}.2f, samples, %{public}zu, result, %{public}d"
+ "#gfm, onFitnessActivityUpdate, active, %{public}d, wasActive, %{public}d"
+ "#gfm, onFitnessActivityUpdate, ended, duration, %{public}.1f"
+ "#gfm, onFitnessActivityUpdate, started"
+ "#gfm, onFocusedNavigationUpdate, active, %{public}d, wasActive, %{public}d, override, %{public}d"
+ "#gfm, onFocusedNavigationUpdate, ended, duration, %{public}.1f"
+ "#gfm, onFocusedNavigationUpdate, forcing active due to defaults override"
+ "#gfm, onFocusedNavigationUpdate, ignoring inactive state due to defaults override"
+ "#gfm, onFocusedNavigationUpdate, started"
+ "#gfm, onHeartbeat"
+ "#gfm, onHeartbeat, GPS failure condition began"
+ "#gfm, onHeartbeat, GPS failure confirmed (sustained %{public}.1fs)"
+ "#gfm, onHeartbeat, GPS failure end detected, currentTime, %{public}.3f, onsetTime, %{public}.3f, sustainedDuration, %{public}.1f"
+ "#gfm, onHeartbeat, GPS failure pending confirmation, sustained, %{public}.1f, required, %{public}.1f, driftType, %{public}d, distFromRoad, %{public}.1f, driftFailures, %{public}d, driftConf, %{public}.2f"
+ "#gfm, onHeartbeat, failure context, dominantOrientation, %{public}d"
+ "#gfm, onHeartbeat, transient GPS gap rejected, sustained, %{public}.1f, required, %{public}.1f"
+ "#gfm, updateAccurateGpsTimestamp, updated, timestamp, %{public}.3f, hAcc, %{public}.1f, type, %{public}d"
+ "#luLive unrecognized liveUpdateConfiguration, falling back to Default"
+ "#wci,ggselector,GpsSimulatorTestMode,1,ignoring domain updates"
+ "#wci,ggselector,WCIOverrideRegion,%{public}d,overriding domain and box updates"
+ "#wci,ggselector,boxResult,isUS,%{private}d,rd,%{private}d,isAtLeast5kmInsideUS,%{private}d"
+ "#wci,ggselector,disabling restricted mode,reason,%{public}s,wifiAvailability,%{public}s,observedWifiIntervalSec,%{public}.1f,adaptiveThresholdSec,%{public}.1f,currentGapSec,%{public}.1f,isDriving,%{public}d,isDenseUrban,%{public}d,urban,%{public}d,graceActive,%{public}d,sessionAgeSec,%{public}.1f,gnssActive,%{public}d"
+ "#wci,ggselector,persisting gnss restricted mode (resist mode engaged),observedWifiIntervalSec,%{public}.1f,releaseThresholdSec,%{public}.1f,currentGapSec,%{public}.1f,isDriving,%{public}d,wifiAvailability,%{public}s"
+ "#wci,ggselector,resist mode reset,observedWifiIntervalSec,%{public}.1f,thresholdSec,%{public}.1f"
+ "#wci,ggselector,resist mode started,observedWifiIntervalSec,%{public}.1f,releaseThresholdSec,%{public}.1f,requiredSec,%{public}.1f"
+ "#wci,ggselector,resist mode,sustainedSec,%{public}.1f,requiredSec,%{public}.1f,ready,%{public}d"
+ "#wci,ggselector,session resist upgrade cleared,reason,gnss session ended"
+ "#wci,ggselector,watch,session end,lastSessionHadWifi,%{public}d"
+ "#wci,ggselector,watch,session start,no session grace period,isUrban,%{public}d,lastSessionHadWifi,%{public}d"
+ "#wci,ggselector,watch,session start,session grace period extended,graceEndMctSec,%{public}.3f,graceSec,%{public}.1f,isUrban,%{public}d,lastSessionHadWifi,%{public}d"
+ "#wci,ggselector,workout override,currentRestrictedMode,%{public}d"
+ "#wci,usmon,evaluated,nowMctSec,%{public}.3f,sinceLastEvalSec,%{public}.1f,latDeg,%{sensitive}.7f,lonDeg,%{sensitive}.7f,hAccM,%{public}.1f,rawRegion,%{public}d,region,%{public}d,isUS,%{private}d,sigmaMult,%{public}.2f,maxAccM,%{public}.1f,borderDistM,%{private}.1f,fenceM,%{private}.1f,changed,%{public}d,isAtLeast5kmInsideUS,%{private}d"
+ "#wci,usmon,init,sigmaMult,%{public}.2f,maxAccM,%{public}.1f"
+ "04:49:39"
+ "@76@0:8d16d24@32@40@48B56Q60B68B72"
+ "@ClxWciClient, Fix, 1, ll, %{sensitive}.7f, %{sensitive}.7f, acc, %{public}.2f, speed, %{private}.1f, course, %{private}.1f, type, %{public}d, alt, %{private}.1f, altunc, %{public}.1f, ellipsoidalAlt, %{private}.1f, speedUnc, %{public}.1f, courseUnc, %{public}.1f, signalEnv, %{private}d, timestamp, %{public}.3f, mct, %{public}.3f, fromEst, %{public}d"
+ "@SqliteDB, PRAGMA table_info aborted with non-terminal result; preserving existing table"
+ "@SqliteDB, schema mismatch on populated table — refusing to drop, preserving data (rdar://179790049)"
+ "Assertion failed: !empty(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 147,back() on empty buffer."
+ "Assertion failed: !empty(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 225,variance() on empty buffer."
+ "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 255,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 71,invalid col %zu > %zu."
+ "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 78,invalid col %zu > %zu."
+ "Assertion failed: col > row, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 256,invalid element %zu <= %zu."
+ "Assertion failed: lambda2 != 0, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMOQuaternion.cpp, line 152,invalid weights."
+ "Assertion failed: ldx < M*N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 84,invalid element %zu >= %zu."
+ "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 70,invalid row %zu > %zu."
+ "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 77,invalid row %zu > %zu."
+ "Assertion failed: row < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 209,invalid row %zu > %zu."
+ "Assertion failed: start <= end && end <= fCapacity, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/CMQueue.h, line 267,start=%zu end=%zu fCapacity=%u."
+ "Assertion failed: static_cast<uint32_t>(Cap) == fCapacity, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/CMQueue.h, line 252,fastIndex Cap=%zu mismatches fCapacity=%u."
+ "Aug 10 2026"
+ "Aug 10 2026 04:51:20"
+ "CLUSRegionMonitor::CLUSRegionMonitor(CLUSRegionMonitor::RegionChangedCallback)"
+ "CMVector<T, 3> CMFactoredMatrix<float, 3>::biermanObservationalUpdateSkew3(T, T, T, T, T, T, T) [T = float, N = 3, Dummy = void]"
+ "GnssFailureStatus"
+ "NonlinearBiasFit,imuIndex,%{public}u,%{public}s"
+ "TB,R,N,V_isContinuationOfPriorBatch"
+ "Ti,N,V_testType"
+ "_isContinuationOfPriorBatch"
+ "_testType"
+ "adhrHeartRate"
+ "adhrHeartRateConfidence"
+ "alpha <= 0, matrix !positive definite"
+ "bool CLGnssFailureMonitor::checkForGpsFailure() const"
+ "bool CLGnssFailureMonitor::hasHealthySatelliteReception() const"
+ "const T &CMQueue<CMVector<float, 3>>::fastIndex(const size_t) const [T = CMVector<float, 3>, Cap = 16UL]"
+ "containsValueForKey:"
+ "density"
+ "epochsWithInsufficientHGForStiction"
+ "epochsWithStiction"
+ "epochsWithoutStiction"
+ "groupADeltaVThreshold1"
+ "groupADeltaVThreshold2"
+ "groupAMaxAccelNormThreshold"
+ "groupAPeakPressure"
+ "groupAShortAudioNumThreshold"
+ "groupAZgTimeThreshold"
+ "groupApplied"
+ "groupBDeltaVThreshold1"
+ "groupBDeltaVThreshold2"
+ "groupBMaxAccelNormThreshold"
+ "groupBPeakPressure"
+ "groupBShortAudioNumThreshold"
+ "groupBZgTimeThreshold"
+ "groupIsA"
+ "hasTestType"
+ "initWithStartTime:endTime:locationSamples:odometrySamples:altitudeSamples:is1HzData:workoutActivityType:startsNewSegment:isContinuationOfPriorBatch:"
+ "int CLGnssFailureMonitor::countAccurateGpsInWindow(double) const"
+ "isContinuationOfPriorBatch"
+ "scaledADHRMets"
+ "setHasTestType:"
+ "setTestType:"
+ "sigenv transition"
+ "stictionDuration"
+ "stictionStatus"
+ "stictionThreshold"
+ "testType"
+ "v1732@0:8i16{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}CC}20"
+ "void CLGnssFailureMonitor::getDisplacement(const double, double &, double &) const"
+ "void CLGnssFailureMonitor::onFitnessActivityUpdate(bool)"
+ "void CLGnssFailureMonitor::onFocusedNavigationUpdate(bool)"
+ "void CLGnssFailureMonitor::onHeartbeat()"
+ "void CLGnssFailureMonitor::updateAccurateGpsTimestamp(const Location &)"
+ "void CLGpsGalSelector::onGnssSessionActiveChanged(bool)"
+ "void CLGpsGalSelector::onUSRegionMonitorChanged(bool, bool)"
+ "void CLUSRegionMonitor::evaluateAt(double, double, double)"
+ "void CMQueue<CMVector<float, 3>>::linearRanges(size_t, size_t, const T **, size_t *, const T **, size_t *) const [T = CMVector<float, 3>]"
+ "workout dist"
+ "workout env"
+ "workout mode"
+ "workout type"
+ "zgIsAHStateStable"
+ "zgIsFreefallA"
+ "zgIsFreefallB"
+ "zgMetaTotalZgTimeA"
+ "zgMetaTotalZgTimeB"
+ "zgSelectedVariant"
+ "zgSettledAHState"
+ "zgUsedSettledState"
+ "{\"msg%{public}.0s\":\"#luLive unrecognized liveUpdateConfiguration, falling back to Default\", \"value\":%{public, location:escape_only}@, \"configuration\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"@SqliteDB, PRAGMA table_info aborted with non-terminal result; preserving existing table\", \"table\":%{private, location:escape_only}s, \"sqlite_rc\":%{public}d, \"columns_read\":%{public}d}"
+ "{\"msg%{public}.0s\":\"@SqliteDB, schema mismatch on populated table — refusing to drop, preserving data (rdar://179790049)\", \"table\":%{private, location:escape_only}s, \"rows\":%{public}lld}"
+ "{\"msg%{public}.0s\":\"Harvester registering for wifi notifications\"}"
+ "{\"msg%{public}.0s\":\"Harvester unregistering for wifi notifications\"}"
+ "{\"msg%{public}.0s\":\"skip #rehydration quarantined client\", \"Client\":%{public, location:escape_only}@}"
+ "{?=\"durationInSeconds\"b1\"estimatedHRRecoveryParam\"b1\"estimatedHRResponseParam\"b1\"estimatedVo2Max\"b1\"filteredVo2Max\"b1\"hrMax\"b1\"hrMin\"b1\"sessionVo2Max\"b1\"startTime\"b1\"variance\"b1\"numWorkoutsContrToEstimate\"b1\"platformSource\"b1\"sessionType\"b1\"testType\"b1\"workoutType\"b1\"eligibleForCalorimetry\"b1\"eligibleForHealthKit\"b1}"
+ "{AudioAccessorySample={?={CMOQuaternion=}{CMVector<float, 3UL>=}{CMVector<float, 3UL>=}{CMVector<float, 3UL>=}{Status=S}}Qdd{CMVector<float, 3UL>=}fiIiiQd[3f]BCBBddBBI}24@0:8@16"
+ "{Config=i[64c][32c]iBII[32c][32c][32c]{CMOQuaternion=}B{CMOQuaternion=}}24@0:8@16"
- "#wci,WCIOverrideRegion set"
- "#wci,ggselector,boxResult,isUS,%{private}d,rd,%{public}d"
- "#wci,ggselector,disabling restricted mode,reason,%{public}s,wifiAvailability,%{public}s,observedWifiIntervalSec,%{public}.1f,adaptiveThresholdSec,%{public}.1f,currentGapSec,%{public}.1f,isDriving,%{public}d,isDenseUrban,%{public}d,urban,%{public}d,graceActive,%{public}d,activeDurationSec,%{public}.1f,gnssActive,%{public}d"
- "#wci,ggselector,persisting GPS+GAL,observedWifiIntervalSec,%{public}.1f,releaseThresholdSec,%{public}.1f,currentGapSec,%{public}.1f,isDriving,%{public}d,wifiAvailability,%{public}s"
- "#wci,ggselector,workout sustained mode reset,observedWifiIntervalSec,%{public}.1f,thresholdSec,%{public}.1f"
- "#wci,ggselector,workout sustained mode started,observedWifiIntervalSec,%{public}.1f,releaseThresholdSec,%{public}.1f,requiredSec,%{public}.1f"
- "#wci,ggselector,workout sustained mode,sustainedSec,%{public}.1f,requiredSec,%{public}.1f,ready,%{public}d"
- "#wci,usmon,evaluated,nowMctSec,%{public}.3f,sinceLastEvalSec,%{public}.1f,latDeg,%{sensitive}.7f,lonDeg,%{sensitive}.7f,region,%{public}d,isUS,%{private}d,borderDistM,%{private}.1f,fenceM,%{public}.1f,changed,%{public}d"
- "%zu: alpha <= 0, matrix ! positive definite"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Shared/Motion/Eclipse/CLSPUEclipseInterface.mm"
- "03:13:35"
- "@72@0:8d16d24@32@40@48B56Q60B68"
- "@ClxWciClient, Fix, 1, ll, %{sensitive}.7f, %{sensitive}.7f, acc, %{public}.2f, speed, %{private}.1f, course, %{private}.1f, type, %{public}d, alt, %{private}.1f, altunc, %{public}.1f, ellipsoidalAlt, %{private}.1f, speedUnc, %{public}.1f, courseUnc, %{public}.1f, signalEnv, %{private}d, timestamp, %{public}.3f, mct, %{public}.3f"
- "Assertion failed: !empty(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 145,back() on empty buffer."
- "Assertion failed: !empty(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 210,variance() on empty buffer."
- "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 242,invalid col %zu > %zu."
- "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 73,invalid col %zu > %zu."
- "Assertion failed: col < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 80,invalid col %zu > %zu."
- "Assertion failed: col > row, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 243,invalid element %zu <= %zu."
- "Assertion failed: i < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMVector.h, line 299,invalid index %zu >= %zu."
- "Assertion failed: i < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMVector.h, line 305,invalid index %zu >= %zu."
- "Assertion failed: i < size(), file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/CMVectorBuffer.h, line 45,out of buffer range %zu."
- "Assertion failed: lambda2 != 0, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMOQuaternion.cpp, line 208,invalid weights."
- "Assertion failed: ldx < M*N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 86,invalid element %zu >= %zu."
- "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 72,invalid row %zu > %zu."
- "Assertion failed: row < M, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMMatrix.h, line 79,invalid row %zu > %zu."
- "Assertion failed: row < N, file /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/CoreLocation/Oscar/Math/CMFactoredMatrix.h, line 196,invalid row %zu > %zu."
- "CMVector<T, N> CMFactoredMatrix<float, 3>::biermanObservationalUpdate(const CMMatrix<T, P, N> &, const CMVector<T, P> &, const CMVector<T, P> &) [T = float, N = 3, P = 3UL]"
- "DisableViewObstructedSuppression"
- "EnableProxBaselineEstimation"
- "EnableViewObstructedMLSuppression"
- "ForceAlwaysOnViewObstructed"
- "ForceSuppressionEnabled"
- "Jul 11 2026"
- "Jul 11 2026 03:15:03"
- "KeepViewObstructedRunningDelaySecs"
- "LCPM,stopping gps and clearing throttle state"
- "MockA2DPActivity"
- "NonlinearBiasFit,%{public}s,imuIndex,%{public}u"
- "T &CMVector<float, 3>::operator[](const size_t) [T = float, N = 3]"
- "T CMVector<float, 3>::operator[](const size_t) const [T = float, N = 3]"
- "VOEvent"
- "ViewObstructedStateChange"
- "ViewObstructedSuppressionDelaySecs"
- "[CLSPUEclipseControl] Configure failed"
- "[CLSPUEclipseControl] Configuring,enableSuppression,%{public}d,enableAlwaysOnViewObstructed,%{public}d,mlEnabled,%{public}d,viewObstructedStateDebugEnabled,%{public}d,suppressionDelayUs,%{public}llu,disableViewObstructedSuppression,%{public}d,keepViewObstructedRunningDelaySecs,%{public}llu,enableProxBaselineEstimation,%{public}d"
- "[CLSPUEclipseControl] Suppression Report received shouldSuppress,%{public}d,APAwake,%{public}d,currentState,%{public}hhu,orientation,%{public}hhu,motionType,%{public}hhu,lux,%{public}f,pocketProbability,%{public}f,facedownStatic,%{public}hhu"
- "[CLSPUEclipseInterface] Service required"
- "bool CLGpsGalSelector::mustPopulateDedicatedEstimateIntoWirelessClientInfo() const_block_invoke"
- "const Element &CMVectorBufferBase<float, 3>::operator[](const size_t) const [T = float, N = 3]"
- "entered dense urban — full GNSS mode"
- "eventTimeNS"
- "initWithStartTime:endTime:locationSamples:odometrySamples:altitudeSamples:is1HzData:workoutActivityType:startsNewSegment:"
- "isAvailable()"
- "not plausibly US (box or rd)"
- "sendCommand"
- "static void CLSPUEclipseControl::eclipseControlCallback(void *, void *, void *, IOHIDEventRef)"
- "suppress"
- "unsuppress"
- "v1732@0:8i16{NotificationData={CLDaemonLocation=i{?=dd}ddddddddidi{?=dd}diIiiidB}{CLDaemonLocationPrivate=dddddfffBi{?=dd}diiB{?=ddBBidqddd}{?={?=iddddd{?=dd}dd}iQiiiidB}{?=dd}if{?=dd}ddiBddddddddBB{?=dd}diddddddB{shared_ptr<const CLDaemonLocationPrivate::AboveHorizonSatelliteVisibilityReport>=^{AboveHorizonSatelliteVisibilityReport}^{__shared_weak_count}}i{AltitudeInfo=dddi}CdddCCBii{?=I}{?=if}iiiBffffd{?=dddffffff}}{shared_ptr<CLBatchedLocations>=^{CLBatchedLocations}^{__shared_weak_count}}{TechnologyStatus=iB}Bd{?=dddd}{?=dd}{XtraFileAvailable=d{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}}i{LocationDerivedSpeed=ddd}{?=dddi}{?=ddddddB[3[3d]]dddQi}i{?=idddddd[5d]ddddii}{CLStrongPtr<NSData *>=@}{PredictedGnssAvailability=iidd}{CLRhythmicGnssStatusUpdate=iBi{bitset<2UL>=Q}BI}{CLRhythmicStreamingControl=B}{CLGNSSStateQueryAssertionReportData=ddd}{ProactiveLocationSessionStats=id}B{RecentLocationsRevised=ddd}{MapMatchingDriftSignal=iidddddid}{CLPIOSample=dddfffffffffffffffffffffCCCCCCS}{AnomalousGnssDetectionInfo=BBB}}20"
- "virtual bool CLSPUEclipseControl::configure()"
- "void CLGpsGalSelector::onUSRegionMonitorChanged(bool)"
- "void CLUSRegionMonitor::evaluateAt(double, double)"
- "wifi dense enough to release"
- "wifi interval below threshold"
- "{\"msg%{public}.0s\":\"Harvester registering for wifi notificatons\"}"
- "{\"msg%{public}.0s\":\"Harvester unregistering for wifi notificatons\"}"
- "{\"msg%{public}.0s\":\"[CLSPUEclipseInterface] Service required\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{?=\"durationInSeconds\"b1\"estimatedHRRecoveryParam\"b1\"estimatedHRResponseParam\"b1\"estimatedVo2Max\"b1\"filteredVo2Max\"b1\"hrMax\"b1\"hrMin\"b1\"sessionVo2Max\"b1\"startTime\"b1\"variance\"b1\"numWorkoutsContrToEstimate\"b1\"platformSource\"b1\"sessionType\"b1\"workoutType\"b1\"eligibleForCalorimetry\"b1\"eligibleForHealthKit\"b1}"
- "{AudioAccessorySample={?={CMOQuaternion=[4f]}{CMVector<float, 3UL>=[3f]}{CMVector<float, 3UL>=[3f]}{CMVector<float, 3UL>=[3f]}{Status=S}}Qdd{CMVector<float, 3UL>=[3f]}fiIiiQd[3f]BCBBddBBI}24@0:8@16"
- "{Config=i[64c][32c]iBII[32c][32c][32c]{CMOQuaternion=[4f]}B{CMOQuaternion=[4f]}}24@0:8@16"
```
