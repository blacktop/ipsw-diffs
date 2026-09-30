## CoreIndoor

> `/System/Library/PrivateFrameworks/CoreIndoor.framework/CoreIndoor`

```diff

-794.0.1.0.0
-  __TEXT.__text: 0x5fa78
+798.0.0.0.0
+  __TEXT.__text: 0x600dc
   __TEXT.__auth_stubs: 0xd70
   __TEXT.__init_offsets: 0x44
   __TEXT.__objc_methlist: 0x14cc
-  __TEXT.__gcc_except_tab: 0x476c
-  __TEXT.__cstring: 0x2fa4
+  __TEXT.__gcc_except_tab: 0x4790
+  __TEXT.__cstring: 0x2fae
   __TEXT.__const: 0x46aa
   __TEXT.__oslogstring: 0x2dda
-  __TEXT.__unwind_info: 0x2300
+  __TEXT.__unwind_info: 0x2320
   __TEXT.__objc_classname: 0x2ab
-  __TEXT.__objc_methname: 0x3ce9
-  __TEXT.__objc_methtype: 0x28a9
+  __TEXT.__objc_methname: 0x3afe
+  __TEXT.__objc_methtype: 0x23b0
   __TEXT.__objc_stubs: 0x1a80
-  __DATA_CONST.__got: 0x168
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0xd0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x48

   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x6c8
-  __AUTH_CONST.__const: 0x3978
+  __AUTH_CONST.__const: 0x3998
   __AUTH_CONST.__cfstring: 0x12e0
   __AUTH_CONST.__objc_const: 0x2548
   __AUTH_CONST.__objc_dictobj: 0x28

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 121FB7DE-15E9-36E7-95E4-5251D244F0DE
-  Functions: 1665
-  Symbols:   347
+  UUID: 61C7F7E0-577C-3A03-B4DC-D11131D737FD
+  Functions: 1668
+  Symbols:   350
   CStrings:  1286
 
Symbols:
+ __ZNSt12out_of_rangeD1Ev
+ __ZTISt12out_of_range
+ __ZTVSt12out_of_range
+ _objc_retain_x25
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE5eraseEmm
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~B1cfugBJb6xfih1Jw40olWMOkRjClxV9wnkLQLg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/exception/detail/exception_ptr.hpp"
+ "/AppleInternal/Library/BuildRoots/4~B1cfugBJb6xfih1Jw40olWMOkRjClxV9wnkLQLg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.0.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
+ "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16"
+ "T{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})},R,N,V_serializedOutdoorEstimatorLogEntry"
+ "T{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})},R,N,V_serializedVIOEstimation"
+ "T{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})},R,N,V_serializedVLLocalizationResult"
+ "T{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}},V_wifiOnlyDownloadLocIdxs"
+ "T{vector<std::string, std::allocator<std::string>>=^v^v^v},R,V_locationIds"
+ "v40@0:8{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16"
+ "{?=\"odometer\"d\"deltaDistance\"d\"deltaDistanceAccuracy\"d\"timestampGps\"d\"machtime\"d\"horzUncSemiMaj\"f\"horzUncSemiMin\"f\"horzUncSemiMajAz\"f\"isFitnessMatch\"B\"matchQuality\"i\"matchCoordinate\"{?=\"latitude\"d\"longitude\"d}\"matchCourse\"d\"matchFormOfWay\"i\"matchRoadClass\"i\"matchShifted\"B\"mapMatcherData\"{?=\"rawUnmodifiedCourse\"d\"rawUnmodifiedCourseUnc\"d\"isStatic\"B\"isMounted\"B\"estimatedLane\"i\"estimatedLaneProbability\"d\"estimatedLaneFeatureID\"q\"flowlineSnapLat\"d\"flowlineSnapLon\"d\"flowlineSnapCourse\"d}\"trackRunData\"{?=\"lapInformation\"{?=\"lapCount\"i\"currentLapStartTime\"d\"currentLapDurationInSeconds\"d\"currentLapDistanceInMeters\"d\"previousLapDurationInSeconds\"d\"previousLapDistanceInMeters\"d\"previousLapPositionAtCompletionInDegrees\"{?=\"latitude\"d\"longitude\"d}\"currentTrackRunSessionDurationInSeconds\"d\"currentTrackRunSessionDistanceInMeters\"d}\"laneNumber\"i\"trackId\"Q\"estimatedLaneNumber\"i\"laneCount\"i\"estimatedLaneConfidence\"i\"trackProximity\"i\"distanceToTrackMeters\"d\"odometerHasBeenCorrected\"B}\"pressure\"{?=\"value\"d\"std\"d}\"undulationModel\"i\"undulation\"f\"specialCoordinate\"{?=\"latitude\"d\"longitude\"d}\"specialHorizontalAccuracy\"d\"machContinuousTime\"d\"originDevice\"i\"isMatcherPropagatedCoordinates\"B\"slope\"d\"maxAbsSlope\"d\"groundAltitude\"d\"groundAltitudeUncertainty\"d\"rawHorizontalAccuracy\"d\"rawAltitude\"d\"rawVerticalAccuracy\"d\"rawCourseAccuracy\"d\"isCoordinateFused\"B\"isCoordinateFusedWithVL\"B\"fusedCoordinate\"{?=\"latitude\"d\"longitude\"d}\"fusedHorizontalAccuracy\"d\"fusedReferenceFrame\"i\"fusedAltitude\"d\"fusedVerticalAccuracy\"d\"fusedCourse\"d\"fusedCourseAccuracy\"d\"smoothedGPSAltitude\"d\"smoothedGPSAltitudeUncertainty\"d\"positionContextState\"i\"probabilityPositionContextStateIndoor\"d\"probabilityPositionContextStateOutdoor\"d\"batchedLocationFixType\"i\"wifiZaxisData\"{?=\"numberOfZaxisSlamApsUsed\"I}\"demFlatnessMetricData\"{?=\"demNumContiguousFlatPoints\"i\"confidence\"f}\"isTrustedForTimeZone\"B}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}16@0:8"
+ "{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=\"__tree_\"{__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=\"__begin_node_\"^v\"__end_node_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}\"__size_\"Q}}"
+ "{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}16@0:8"
+ "{unique_ptr<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>>, std::default_delete<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>>>>=\"__ptr_\"^v}"
+ "{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__cap_\"^v}"
+ "{vector<std::string, std::allocator<std::string>>=^v^v^v}16@0:8"
+ "{vector<std::string, std::allocator<std::string>>=^v^v^v}24@0:8@16"
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/exception/detail/exception_ptr.hpp"
- "/AppleInternal/Library/BuildRoots/24f0c819-1ca3-11f0-bc1f-ae4c1e672297/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.5.Internal.sdk/usr/local/include/boost/geometry/algorithms/detail/throw_on_empty_input.hpp"
- "@40@0:8{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16"
- "T{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}},R,N,V_serializedOutdoorEstimatorLogEntry"
- "T{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}},R,N,V_serializedVIOEstimation"
- "T{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}},R,N,V_serializedVLLocalizationResult"
- "T{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<unsigned long, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<unsigned long>>=Q}}},V_wifiOnlyDownloadLocIdxs"
- "T{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}},R,V_locationIds"
- "v40@0:8{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<unsigned long, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<unsigned long>>=Q}}}16"
- "{?=\"odometer\"d\"deltaDistance\"d\"deltaDistanceAccuracy\"d\"timestampGps\"d\"machtime\"d\"horzUncSemiMaj\"f\"horzUncSemiMin\"f\"horzUncSemiMajAz\"f\"isFitnessMatch\"B\"matchQuality\"i\"matchCoordinate\"{?=\"latitude\"d\"longitude\"d}\"matchCourse\"d\"matchFormOfWay\"i\"matchRoadClass\"i\"matchShifted\"B\"mapMatcherData\"{?=\"rawUnmodifiedCourse\"d\"rawUnmodifiedCourseUnc\"d\"isStatic\"B\"isMounted\"B\"estimatedLane\"i\"estimatedLaneProbability\"d\"estimatedLaneFeatureID\"q\"flowlineSnapLat\"d\"flowlineSnapLon\"d\"flowlineSnapCourse\"d}\"trackRunData\"{?=\"lapInformation\"{?=\"lapCount\"i\"currentLapStartTime\"d\"currentLapDurationInSeconds\"d\"currentLapDistanceInMeters\"d\"previousLapDurationInSeconds\"d\"previousLapDistanceInMeters\"d\"previousLapPositionAtCompletionInDegrees\"{?=\"latitude\"d\"longitude\"d}\"currentTrackRunSessionDurationInSeconds\"d\"currentTrackRunSessionDistanceInMeters\"d}\"laneNumber\"i\"trackId\"Q\"estimatedLaneNumber\"i\"laneCount\"i\"estimatedLaneConfidence\"i\"trackProximity\"i\"distanceToTrackMeters\"d\"odometerHasBeenCorrected\"B}\"pressure\"{?=\"value\"d\"std\"d}\"undulationModel\"i\"undulation\"f\"specialCoordinate\"{?=\"latitude\"d\"longitude\"d}\"specialHorizontalAccuracy\"d\"machContinuousTime\"d\"originDevice\"i\"isMatcherPropagatedCoordinates\"B\"slope\"d\"maxAbsSlope\"d\"groundAltitude\"d\"groundAltitudeUncertainty\"d\"rawHorizontalAccuracy\"d\"rawAltitude\"d\"rawVerticalAccuracy\"d\"rawCourseAccuracy\"d\"isCoordinateFused\"B\"isCoordinateFusedWithVL\"B\"fusedCoordinate\"{?=\"latitude\"d\"longitude\"d}\"fusedHorizontalAccuracy\"d\"fusedReferenceFrame\"i\"fusedAltitude\"d\"fusedVerticalAccuracy\"d\"fusedCourse\"d\"fusedCourseAccuracy\"d\"smoothedGPSAltitude\"d\"smoothedGPSAltitudeUncertainty\"d\"positionContextState\"i\"probabilityPositionContextStateIndoor\"d\"probabilityPositionContextStateOutdoor\"d\"batchedLocationFixType\"i\"wifiZaxisData\"{?=\"numberOfZaxisSlamApsUsed\"I}\"demFlatnessMetricData\"{?=\"demNumContiguousFlatPoints\"i\"confidence\"f}\"isGnssFromRavenEstimators\"B}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"__r_\"{__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=\"__value_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__padding_\"[0C]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
- "{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}16@0:8"
- "{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=\"__tree_\"{__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=\"__begin_node_\"^v\"__pair1_\"{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<unsigned long, void *>>>=\"__value_\"{__tree_end_node<std::__tree_node_base<void *> *>=\"__left_\"^v}}\"__pair3_\"{__compressed_pair<unsigned long, std::less<unsigned long>>=\"__value_\"Q}}}"
- "{set<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>={__tree<unsigned long, std::less<unsigned long>, std::allocator<unsigned long>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<unsigned long, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<unsigned long>>=Q}}}16@0:8"
- "{unique_ptr<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>>, std::default_delete<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>>>>=\"__ptr_\"{__compressed_pair<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>> *, std::default_delete<boost::geometry::model::polygon<boost::geometry::model::d2::point_xy<double>>>>=\"__value_\"^v}}"
- "{vector<std::string, std::allocator<std::string>>=\"__begin_\"^v\"__end_\"^v\"__end_cap_\"{__compressed_pair<std::string *, std::allocator<std::string>>=\"__value_\"^v}}"
- "{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}16@0:8"
- "{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}24@0:8@16"

```
