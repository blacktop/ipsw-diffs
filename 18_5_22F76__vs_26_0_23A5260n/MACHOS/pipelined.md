## pipelined

> `/usr/libexec/pipelined`

```diff

-794.0.1.0.0
-  __TEXT.__text: 0x3842c4
-  __TEXT.__auth_stubs: 0x2920
-  __TEXT.__objc_stubs: 0x7440
-  __TEXT.__init_offsets: 0x8d4
-  __TEXT.__objc_methlist: 0x41d4
-  __TEXT.__gcc_except_tab: 0x2fbc0
-  __TEXT.__const: 0x18c72
-  __TEXT.__cstring: 0x1b5af
-  __TEXT.__oslogstring: 0x10280
+798.0.0.0.0
+  __TEXT.__text: 0x387344
+  __TEXT.__auth_stubs: 0x2910
+  __TEXT.__objc_stubs: 0x7480
+  __TEXT.__init_offsets: 0x8d8
+  __TEXT.__objc_methlist: 0x41e4
+  __TEXT.__gcc_except_tab: 0x2f590
+  __TEXT.__const: 0x18e62
+  __TEXT.__cstring: 0x1b601
+  __TEXT.__oslogstring: 0x1049d
   __TEXT.__objc_classname: 0x81a
-  __TEXT.__objc_methname: 0xaf64
-  __TEXT.__objc_methtype: 0x6d8a
-  __TEXT.__unwind_info: 0x12a30
-  __DATA_CONST.__auth_got: 0x14a8
-  __DATA_CONST.__got: 0x780
+  __TEXT.__objc_methname: 0xae30
+  __TEXT.__objc_methtype: 0x614b
+  __TEXT.__unwind_info: 0x12730
+  __DATA_CONST.__auth_got: 0x14a0
+  __DATA_CONST.__got: 0x7b0
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1a2c8
-  __DATA_CONST.__cfstring: 0x2aa0
+  __DATA_CONST.__const: 0x1a460
+  __DATA_CONST.__cfstring: 0x2b20
   __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xe0

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x6fa8
-  __DATA.__objc_selrefs: 0x2718
+  __DATA.__objc_const: 0x6fb0
+  __DATA.__objc_selrefs: 0x2730
   __DATA.__objc_ivar: 0x51c
   __DATA.__objc_data: 0x1450
   __DATA.__data: 0x1558
-  __DATA.__bss: 0x14a8
+  __DATA.__bss: 0x1570
   __DATA.__common: 0x14210
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib

   - /usr/lib/libprotobuf.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: BAA659CF-5D73-35ED-ABC8-1C9FAFE8F90A
-  Functions: 12619
-  Symbols:   952
-  CStrings:  6070
+  UUID: 3C76EFE3-EBE1-34C3-9103-9FFE33FB59F7
+  Functions: 12594
+  Symbols:   957
+  CStrings:  6089
 
Symbols:
+ _OBJC_CLASS_$_SDRDiagnosticReporter
+ __ZNSt3__118condition_variable10notify_oneEv
+ __ZNSt3__118condition_variable15__do_timed_waitERNS_11unique_lockINS_5mutexEEENS_6chrono10time_pointINS5_12system_clockENS5_8durationIxNS_5ratioILl1ELl1000000000EEEEEEE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ _kSymptomDiagnosticActionDiagnosticExtensions
+ _kSymptomDiagnosticReplyReasonString
+ _kSymptomDiagnosticReplySessionID
+ _kSymptomDiagnosticReplySuccess
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- _wmemchr
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B1cfugBJb6xfih1Jw40olWMOkRjClxV9wnkLQLg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/exception/detail/exception_ptr.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B1cfugBJb6xfih1Jw40olWMOkRjClxV9wnkLQLg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B1cfugBJb6xfih1Jw40olWMOkRjClxV9wnkLQLg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/add_rings.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B1cfugBJb6xfih1Jw40olWMOkRjClxV9wnkLQLg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B1cfugBJb6xfih1Jw40olWMOkRjClxV9wnkLQLg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/rational.hpp"
+ "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16"
+ "@AutoBugCapture, done triggering diagnostic report"
+ "@AutoBugCapture, error, the parameters passed in are invalid!"
+ "@AutoBugCapture, notified in %{public}lld ms"
+ "@AutoBugCapture, triggering diagnostic report..."
+ "@AutoBugCapture, wait timeout"
+ "@AutoBugCapture: notifying waiting thread via condition variable"
+ "Location"
+ "T{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})},R,N,V_serializedOutdoorEstimatorLogEntry"
+ "T{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})},R,N,V_serializedVIOEstimation"
+ "T{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})},R,N,V_serializedVLLocalizationResult"
+ "T{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}},V_wifiOnlyDownloadLocIdxs"
+ "T{vector<std::string, std::allocator<std::string>>=^v^v^v},R,V_locationIds"
+ "database crash"
+ "pipelined"
+ "session:didUpdateDLTDOAMeasurements:"
+ "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
+ "snapshotWithSignature:delay:events:payload:actions:reply:"
+ "v16@?0@\"NSDictionary\"8"
+ "v40@0:8{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16"
+ "v48@0:8@16{vector<std::shared_ptr<ITileDb>, std::allocator<std::shared_ptr<ITileDb>>>=^v^v^v}24"
+ "{\"msg%{public}.0s\":\"@AutoBugCapture, success, diagnostic report accepted\", \"sessionID\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"@AutoBugCapture, warning, diagnostic report rejected\", \"reason\":%{public, location:escape_only}@}"
+ "{?=\"odometer\"d\"deltaDistance\"d\"deltaDistanceAccuracy\"d\"timestampGps\"d\"machtime\"d\"horzUncSemiMaj\"f\"horzUncSemiMin\"f\"horzUncSemiMajAz\"f\"isFitnessMatch\"B\"matchQuality\"i\"matchCoordinate\"{?=\"latitude\"d\"longitude\"d}\"matchCourse\"d\"matchFormOfWay\"i\"matchRoadClass\"i\"matchShifted\"B\"mapMatcherData\"{?=\"rawUnmodifiedCourse\"d\"rawUnmodifiedCourseUnc\"d\"isStatic\"B\"isMounted\"B\"estimatedLane\"i\"estimatedLaneProbability\"d\"estimatedLaneFeatureID\"q\"flowlineSnapLat\"d\"flowlineSnapLon\"d\"flowlineSnapCourse\"d}\"trackRunData\"{?=\"lapInformation\"{?=\"lapCount\"i\"currentLapStartTime\"d\"currentLapDurationInSeconds\"d\"currentLapDistanceInMeters\"d\"previousLapDurationInSeconds\"d\"previousLapDistanceInMeters\"d\"previousLapPositionAtCompletionInDegrees\"{?=\"latitude\"d\"longitude\"d}\"currentTrackRunSessionDurationInSeconds\"d\"currentTrackRunSessionDistanceInMeters\"d}\"laneNumber\"i\"trackId\"Q\"estimatedLaneNumber\"i\"laneCount\"i\"estimatedLaneConfidence\"i\"trackProximity\"i\"distanceToTrackMeters\"d\"odometerHasBeenCorrected\"B}\"pressure\"{?=\"value\"d\"std\"d}\"undulationModel\"i\"undulation\"f\"specialCoordinate\"{?=\"latitude\"d\"longitude\"d}\"specialHorizontalAccuracy\"d\"machContinuousTime\"d\"originDevice\"i\"isMatcherPropagatedCoordinates\"B\"slope\"d\"maxAbsSlope\"d\"groundAltitude\"d\"groundAltitudeUncertainty\"d\"rawHorizontalAccuracy\"d\"rawAltitude\"d\"rawVerticalAccuracy\"d\"rawCourseAccuracy\"d\"isCoordinateFused\"B\"isCoordinateFusedWithVL\"B\"fusedCoordinate\"{?=\"latitude\"d\"longitude\"d}\"fusedHorizontalAccuracy\"d\"fusedReferenceFrame\"i\"fusedAltitude\"d\"fusedVerticalAccuracy\"d\"fusedCourse\"d\"fusedCourseAccuracy\"d\"smoothedGPSAltitude\"d\"smoothedGPSAltitudeUncertainty\"d\"positionContextState\"i\"probabilityPositionContextStateIndoor\"d\"probabilityPositionContextStateOutdoor\"d\"batchedLocationFixType\"i\"wifiZaxisData\"{?=\"numberOfZaxisSlamApsUsed\"I}\"demFlatnessMetricData\"{?=\"demNumContiguousFlatPoints\"i\"confidence\"f}\"isTrustedForTimeZone\"B}"
+ "{CoastedGravityEstimator=\"fImpl\"{unique_ptr<CoastedGravityEstimatorImpl, std::default_delete<CoastedGravityEstimatorImpl>>=\"__ptr_\"^{CoastedGravityEstimatorImpl}}}"
+ "{Info={basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}16@0:8"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16@0:8"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}24@0:8@16"
+ "{list<std::unique_ptr<ScanInformation>, std::allocator<std::unique_ptr<ScanInformation>>>=\"__end_\"{__list_node_base<std::unique_ptr<ScanInformation>, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_\"Q}"
+ "{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=\"__tree_\"{__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16@0:8"
+ "{unique_ptr<BeaconSensor, std::default_delete<BeaconSensor>>=\"__ptr_\"^{BeaconSensor}}"
+ "{unique_ptr<FloorEnvironmentLoader, std::default_delete<FloorEnvironmentLoader>>=\"__ptr_\"^{FloorEnvironmentLoader}}"
+ "{unique_ptr<GPSSensor, std::default_delete<GPSSensor>>=\"__ptr_\"^{GPSSensor}}"
+ "{unique_ptr<GenericWifiSensor, std::default_delete<GenericWifiSensor>>=\"__ptr_\"^{GenericWifiSensor}}"
+ "{unique_ptr<IOSActivityStateSensorBridge, std::default_delete<IOSActivityStateSensorBridge>>=\"__ptr_\"^{IOSActivityStateSensorBridge}}"
+ "{unique_ptr<IOSInertialSensorBridge, std::default_delete<IOSInertialSensorBridge>>=\"__ptr_\"^{IOSInertialSensorBridge}}"
+ "{unique_ptr<IOSNearbyObjectSensor, std::default_delete<IOSNearbyObjectSensor>>=\"__ptr_\"^{IOSNearbyObjectSensor}}"
+ "{unique_ptr<LocalizerApi, std::default_delete<LocalizerApi>>=\"__ptr_\"^{LocalizerApi}}"
+ "{unique_ptr<PedometrySensor, std::default_delete<PedometrySensor>>=\"__ptr_\"^{PedometrySensor}}"
+ "{unique_ptr<ScanInformation, std::default_delete<ScanInformation>>=^{ScanInformation}}40@0:8^{__WiFiDeviceClient=}16@24Q32"
+ "{unique_ptr<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>>, std::default_delete<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>>>>=\"__ptr_\"^v}"
+ "{vector<NSArray *, std::allocator<NSArray *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
+ "{vector<NSInputStream *, std::allocator<NSInputStream *>>=\"__begin_\"^@\"__end_\"^@\"__cap_\"^@}"
+ "{vector<int, std::allocator<int>>=^i^i^i}16@0:8"
+ "{vector<std::shared_ptr<ITileDb>, std::allocator<std::shared_ptr<ITileDb>>>=^v^v^v}16@0:8"
+ "{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
+ "{vector<std::string, std::allocator<std::string>>=^v^v^v}16@0:8"
+ "{vector<std::string, std::allocator<std::string>>=^v^v^v}24@0:8@16"
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/exception/detail/exception_ptr.hpp"
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/has_self_intersections.hpp"
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/overlay/add_rings.hpp"
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/rational.hpp"
- "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16"
- "T{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}},R,N,V_serializedOutdoorEstimatorLogEntry"
- "T{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}},R,N,V_serializedVIOEstimation"
- "T{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}},R,N,V_serializedVLLocalizationResult"
- "T{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<unsigned long, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<unsigned long>>=Q}}},V_wifiOnlyDownloadLocIdxs"
- "T{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}},R,V_locationIds"
- "v40@0:8{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<unsigned long, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<unsigned long>>=Q}}}16"
- "v48@0:8@16{vector<std::shared_ptr<ITileDb>, std::allocator<std::shared_ptr<ITileDb>>>=^v^v{__compressed_pair<std::shared_ptr<ITileDb> *, std::allocator<std::shared_ptr<ITileDb>>>=^v}}24"
- "{?=\"odometer\"d\"deltaDistance\"d\"deltaDistanceAccuracy\"d\"timestampGps\"d\"machtime\"d\"horzUncSemiMaj\"f\"horzUncSemiMin\"f\"horzUncSemiMajAz\"f\"isFitnessMatch\"B\"matchQuality\"i\"matchCoordinate\"{?=\"latitude\"d\"longitude\"d}\"matchCourse\"d\"matchFormOfWay\"i\"matchRoadClass\"i\"matchShifted\"B\"mapMatcherData\"{?=\"rawUnmodifiedCourse\"d\"rawUnmodifiedCourseUnc\"d\"isStatic\"B\"isMounted\"B\"estimatedLane\"i\"estimatedLaneProbability\"d\"estimatedLaneFeatureID\"q\"flowlineSnapLat\"d\"flowlineSnapLon\"d\"flowlineSnapCourse\"d}\"trackRunData\"{?=\"lapInformation\"{?=\"lapCount\"i\"currentLapStartTime\"d\"currentLapDurationInSeconds\"d\"currentLapDistanceInMeters\"d\"previousLapDurationInSeconds\"d\"previousLapDistanceInMeters\"d\"previousLapPositionAtCompletionInDegrees\"{?=\"latitude\"d\"longitude\"d}\"currentTrackRunSessionDurationInSeconds\"d\"currentTrackRunSessionDistanceInMeters\"d}\"laneNumber\"i\"trackId\"Q\"estimatedLaneNumber\"i\"laneCount\"i\"estimatedLaneConfidence\"i\"trackProximity\"i\"distanceToTrackMeters\"d\"odometerHasBeenCorrected\"B}\"pressure\"{?=\"value\"d\"std\"d}\"undulationModel\"i\"undulation\"f\"specialCoordinate\"{?=\"latitude\"d\"longitude\"d}\"specialHorizontalAccuracy\"d\"machContinuousTime\"d\"originDevice\"i\"isMatcherPropagatedCoordinates\"B\"slope\"d\"maxAbsSlope\"d\"groundAltitude\"d\"groundAltitudeUncertainty\"d\"rawHorizontalAccuracy\"d\"rawAltitude\"d\"rawVerticalAccuracy\"d\"rawCourseAccuracy\"d\"isCoordinateFused\"B\"isCoordinateFusedWithVL\"B\"fusedCoordinate\"{?=\"latitude\"d\"longitude\"d}\"fusedHorizontalAccuracy\"d\"fusedReferenceFrame\"i\"fusedAltitude\"d\"fusedVerticalAccuracy\"d\"fusedCourse\"d\"fusedCourseAccuracy\"d\"smoothedGPSAltitude\"d\"smoothedGPSAltitudeUncertainty\"d\"positionContextState\"i\"probabilityPositionContextStateIndoor\"d\"probabilityPositionContextStateOutdoor\"d\"batchedLocationFixType\"i\"wifiZaxisData\"{?=\"numberOfZaxisSlamApsUsed\"I}\"demFlatnessMetricData\"{?=\"demNumContiguousFlatPoints\"i\"confidence\"f}\"isGnssFromRavenEstimators\"B}"
- "{CoastedGravityEstimator=\"fImpl\"{unique_ptr<CoastedGravityEstimatorImpl, std::default_delete<CoastedGravityEstimatorImpl>>=\"__ptr_\"{__compressed_pair<CoastedGravityEstimatorImpl *, std::default_delete<CoastedGravityEstimatorImpl>>=\"__value_\"^{CoastedGravityEstimatorImpl}}}}"
- "{Info={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}16@0:8"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16@0:8"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}24@0:8@16"
- "{list<std::unique_ptr<ScanInformation>, std::allocator<std::unique_ptr<ScanInformation>>>=\"__end_\"{__list_node_base<std::unique_ptr<ScanInformation>, void *>=\"__prev_\"^v\"__next_\"^v}\"__size_alloc_\"{__compressed_pair<unsigned long, std::allocator<std::__list_node<std::unique_ptr<ScanInformation>, void *>>>=\"__value_\"Q}}"
- "{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=\"__tree_\"{__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<unsigned long, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::less<unsigned long>>=\"__value_\"Q}}}"
- "{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<unsigned long, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<unsigned long>>=Q}}}16@0:8"
- "{unique_ptr<BeaconSensor, std::default_delete<BeaconSensor>>=\"__ptr_\"{__compressed_pair<BeaconSensor *, std::default_delete<BeaconSensor>>=\"__value_\"^{BeaconSensor}}}"
- "{unique_ptr<FloorEnvironmentLoader, std::default_delete<FloorEnvironmentLoader>>=\"__ptr_\"{__compressed_pair<FloorEnvironmentLoader *, std::default_delete<FloorEnvironmentLoader>>=\"__value_\"^{FloorEnvironmentLoader}}}"
- "{unique_ptr<GPSSensor, std::default_delete<GPSSensor>>=\"__ptr_\"{__compressed_pair<GPSSensor *, std::default_delete<GPSSensor>>=\"__value_\"^{GPSSensor}}}"
- "{unique_ptr<GenericWifiSensor, std::default_delete<GenericWifiSensor>>=\"__ptr_\"{__compressed_pair<GenericWifiSensor *, std::default_delete<GenericWifiSensor>>=\"__value_\"^{GenericWifiSensor}}}"
- "{unique_ptr<IOSActivityStateSensorBridge, std::default_delete<IOSActivityStateSensorBridge>>=\"__ptr_\"{__compressed_pair<IOSActivityStateSensorBridge *, std::default_delete<IOSActivityStateSensorBridge>>=\"__value_\"^{IOSActivityStateSensorBridge}}}"
- "{unique_ptr<IOSInertialSensorBridge, std::default_delete<IOSInertialSensorBridge>>=\"__ptr_\"{__compressed_pair<IOSInertialSensorBridge *, std::default_delete<IOSInertialSensorBridge>>=\"__value_\"^{IOSInertialSensorBridge}}}"
- "{unique_ptr<IOSNearbyObjectSensor, std::default_delete<IOSNearbyObjectSensor>>=\"__ptr_\"{__compressed_pair<IOSNearbyObjectSensor *, std::default_delete<IOSNearbyObjectSensor>>=\"__value_\"^{IOSNearbyObjectSensor}}}"
- "{unique_ptr<LocalizerApi, std::default_delete<LocalizerApi>>=\"__ptr_\"{__compressed_pair<LocalizerApi *, std::default_delete<LocalizerApi>>=\"__value_\"^{LocalizerApi}}}"
- "{unique_ptr<PedometrySensor, std::default_delete<PedometrySensor>>=\"__ptr_\"{__compressed_pair<PedometrySensor *, std::default_delete<PedometrySensor>>=\"__value_\"^{PedometrySensor}}}"
- "{unique_ptr<ScanInformation, std::default_delete<ScanInformation>>={__compressed_pair<ScanInformation *, std::default_delete<ScanInformation>>=^{ScanInformation}}}40@0:8^{__WiFiDeviceClient=}16@24Q32"
- "{unique_ptr<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>>, std::default_delete<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>>>>=\"__ptr_\"{__compressed_pair<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>> *, std::default_delete<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>>>>=\"__value_\"^v}}"
- "{vector<NSArray *, std::allocator<NSArray *>>=\"__begin_\"^@\"__end_\"^@\"__end_cap_\"{__compressed_pair<NSArray *__strong *, std::allocator<NSArray *>>=\"__value_\"^@}}"
- "{vector<NSInputStream *, std::allocator<NSInputStream *>>=\"__begin_\"^@\"__end_\"^@\"__end_cap_\"{__compressed_pair<NSInputStream *__strong *, std::allocator<NSInputStream *>>=\"__value_\"^@}}"
- "{vector<int, std::allocator<int>>=^i^i{__compressed_pair<int *, std::allocator<int>>=^i}}16@0:8"
- "{vector<std::shared_ptr<ITileDb>, std::allocator<std::shared_ptr<ITileDb>>>=^v^v{__compressed_pair<std::shared_ptr<ITileDb> *, std::allocator<std::shared_ptr<ITileDb>>>=^v}}16@0:8"
- "{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::string *, std::allocator<std::string>>=\"__value_\"^v}}"
- "{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}16@0:8"
- "{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}24@0:8@16"

```
