## nearbyd

> `/usr/libexec/nearbyd`

```diff

-458.0.11.0.0
-  __TEXT.__text: 0x431a5c
+460.0.13.0.1
+  __TEXT.__text: 0x435b64
   __TEXT.__auth_stubs: 0x2910
-  __TEXT.__objc_stubs: 0x11000
+  __TEXT.__objc_stubs: 0x11140
   __TEXT.__init_offsets: 0x5e8
-  __TEXT.__objc_methlist: 0x9a54
-  __TEXT.__gcc_except_tab: 0x47300
-  __TEXT.__const: 0x2d54b0
-  __TEXT.__cstring: 0x30b1c
-  __TEXT.__objc_methname: 0x19fc6
-  __TEXT.__oslogstring: 0x4c5d4
-  __TEXT.__objc_classname: 0x185b
-  __TEXT.__objc_methtype: 0x1c188
+  __TEXT.__objc_methlist: 0x9b84
+  __TEXT.__gcc_except_tab: 0x4771c
+  __TEXT.__const: 0x2d5680
+  __TEXT.__cstring: 0x30e52
+  __TEXT.__objc_methname: 0x1a47d
+  __TEXT.__oslogstring: 0x4cb17
+  __TEXT.__objc_classname: 0x185c
+  __TEXT.__objc_methtype: 0x1d030
   __TEXT.__swift5_typeref: 0x7d
   __TEXT.__swift5_capture: 0x20
   __TEXT.__constg_swiftt: 0x88
   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x17578
+  __TEXT.__unwind_info: 0x17700
   __TEXT.__eh_frame: 0x38
   __DATA_CONST.__auth_got: 0x14a0
   __DATA_CONST.__got: 0x980
   __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x1f888
-  __DATA_CONST.__cfstring: 0x11880
+  __DATA_CONST.__const: 0x1fa20
+  __DATA_CONST.__cfstring: 0x119c0
   __DATA_CONST.__objc_classlist: 0x4a8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x258

   __DATA_CONST.__objc_arrayobj: 0x198
   __DATA_CONST.__objc_intobj: 0x510
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x17360
-  __DATA.__objc_selrefs: 0x4e68
-  __DATA.__objc_ivar: 0x12d8
+  __DATA.__objc_const: 0x17558
+  __DATA.__objc_selrefs: 0x4f38
+  __DATA.__objc_ivar: 0x1300
   __DATA.__objc_data: 0x2f48
-  __DATA.__data: 0x302c
-  __DATA.__bss: 0xc228
+  __DATA.__data: 0x30a4
+  __DATA.__bss: 0xc5a0
   __DATA.__common: 0xcb0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 18813
+  Functions: 18919
   Symbols:   1001
-  CStrings:  16540
+  CStrings:  16606
 
CStrings:
+ "\x01aQr\x92!"
+ "\n\x18CLPRoseMotionEvent.proto\x12\x11CLP.LogEntry.Rose\"\x9e\b\n\x0eRoseMotionData\x12I\n\rdevice_motion\x18\x01 \x01(\v22.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData\x1a<\n\x0eUnitQuaternion\x12\t\n\x01w\x18\x01 \x01(\x01\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\t\n\x01z\x18\x04 \x01(\x01\x1a\x82\a\n\x10DeviceMotionData\x12\x1e\n\x16mach_continuous_time_s\x18\x01 \x01(\x01\x12M\n\battitude\x18\x02 \x01(\v2;.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData.Attitude\x12V\n\rrotation_rate\x18\x03 \x01(\v2?.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData.RotationRate\x12^\n\x11user_acceleration\x18\x04 \x01(\v2C.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData.UserAcceleration\x12\x1c\n\x14mach_absolute_time_s\x18\x05 \x01(\x01\x12M\n\tgravity_g\x18\x06 \x01(\v2:.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData.Gravity\x12X\n\x0emagnetic_field\x18\a \x01(\v2@.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData.MagenticField\x1a\x8b\x01\n\bAttitude\x12I\n\x0funit_quaternion\x18\x01 \x01(\v20.CLP.LogEntry.Rose.RoseMotionData.UnitQuaternion\x12\x0f\n\ayaw_rad\x18\x02 \x01(\x01\x12\x11\n\tpitch_rad\x18\x03 \x01(\x01\x12\x10\n\broll_rad\x18\x04 \x01(\x01\x1aA\n\fRotationRate\x12\x0f\n\ax_rad_s\x18\x01 \x01(\x01\x12\x0f\n\ay_rad_s\x18\x02 \x01(\x01\x12\x0f\n\az_rad_s\x18\x03 \x01(\x01\x1aB\n\x10UserAcceleration\x12\x0e\n\x06x_m_s2\x18\x01 \x01(\x01\x12\x0e\n\x06y_m_s2\x18\x02 \x01(\x01\x12\x0e\n\x06z_m_s2\x18\x03 \x01(\x01\x1a0\n\aGravity\x12\v\n\x03x_g\x18\x01 \x01(\x01\x12\v\n\x03y_g\x18\x02 \x01(\x01\x12\v\n\x03z_g\x18\x03 \x01(\x01\x1a9\n\rMagenticField\x12\f\n\x04x_uT\x18\x01 \x01(\x01\x12\f\n\x04y_uT\x18\x02 \x01(\x01\x12\f\n\x04z_uT\x18\x03 \x01(\x01"
+ "!\x12\xf0!a\xa2\xf0\xf0\xa2"
+ "\"\x13"
+ "#GestureFileUtils Resource bundle does not exist in system volume for Primary and Secondary predictor."
+ "#GestureFileUtils Secondary Resource bundle '%!s(MISSING)' does not exist in system volume."
+ "#ble,Overriding advertising T19 payload to burst adv rate: [%!@(MISSING)]"
+ "#nimd,cannot start activity updates because fMotionActivityMgr is nil"
+ "#nimd,cannot start device motion updates because fMotionManager is nil"
+ "#nimd,continued monitoring motion updates, detector type is %!s(MISSING)"
+ "#nimd,delivered motion state %!s(MISSING) with motion event id %!u(MISSING)"
+ "#nimd,generated new motion state %!s(MISSING) with event id %!u(MISSING), detector type is %!s(MISSING)"
+ "#nimd,motion state is forced to be Moving"
+ "#nimd,paused monitoring motion updates, detector type is %!s(MISSING)"
+ "#nimd,stale measurement timer fires"
+ "#nimd,started monitoring motion updates, detector type is %!s(MISSING)"
+ "#nimd,stopped monitoring motion updates"
+ "#nimd,switched motion detector type to DeviceMotionGravity"
+ "#nimd,switched motion detector type to MotionActivity"
+ "#nimd,switching to motion activity detector timer fires"
+ "#nimd,trying to switch to motion detector type DeviceMotionGravity which is current motion detector type"
+ "#nimd,trying to switch to motion detector type MotionActivity which is current motion detector type"
+ "#regionmon #spatialGesturesPredictor creating deviceMonitor with intent predictor MotionBasedSpatialGestures for dev %!l(MISSING)lx"
+ "#regionmon #spatialGesturesPredictor for intent predictor MotionBasedSpatialGestures, gestureClassifiers should have value"
+ "#regionmon #spatialGesturesPredictor for intent predictor MotionBasedSpatialGestures, motionTriggeredHandoffCallback must be defined"
+ "#regionmon %!s(MISSING):%!d(MISSING): assertion failure in %!s(MISSING)"
+ "#regionmon ERROR: Ideally should NOT enter this switch case since initStateForDevice is handled separately in a different function for non-BT samples. Returning false."
+ "#regionmon Initializing BT device monitoring without spatial gesture detection, allowCoarseEstimation: %!d(MISSING)."
+ "#regionmon Motion based spatial gestures predictor not defined"
+ "#regionmon Setting typePredictor as None since WifiToF/ObjectTracking based ranging does not use user intent score."
+ "#ses-container,Creating a new session: %!d(MISSING), Signing identity: %!@(MISSING), pid: %!d(MISSING)."
+ "#ses-home,#regions, updatesEngine didUpdateRegion: %!@(MISSING), previousRegion: %!@(MISSING), suppressed: %!d(MISSING)"
+ "#ses-home,#supportsDevicePresence homeDeviceSessionBTLeechingEnabled: %!d(MISSING)"
+ "#ses-home,Device rediscovered decision: Not restarting UWB session since addressChange?: %!d(MISSING), role == responder?: %!d(MISSING) and active UWB session?:%!d(MISSING)"
+ "#ses-home,Device rediscovered decision: not restarting Wifi session since address is the same and role != responder and wifi ranging bit is unchanged and wifi ranging not enabled."
+ "#ses-home,Device rediscovered decision: restarting UWB session since address is change, role == responder and there's active UWB session."
+ "#ses-home,Restart Wifi Session due to address roll or updated device's wifi ranging capable bit. advAddressChanged: %!d(MISSING), current device's wifiRanging: %!d(MISSING)"
+ "#ses-home,Stop Wifi Session due to updated device's wifi ranging capable bit off. advAddressChanged: %!d(MISSING), current device's wifiRanging: %!d(MISSING)"
+ "#spatialGesturesPredictor Gesture classifier was not configured"
+ "#spatialGesturesPredictor Initializing models for UWB based spatial gestures"
+ "#spatialGesturesPredictor Initializing models for motion based spatial gestures"
+ "#spatialGesturesPredictor Not enough samples to run motion based spatial gestures."
+ "#spatialGesturesPredictor Should never get here"
+ "#spatialGesturesPredictor Should not get here"
+ "#threshold-detector, resetRssiOffset originalOffset: %!f(MISSING), originalRssiThresh: %!f(MISSING), newRssiThresh: %!f(MISSING)"
+ "#threshold-detector, threshsize:%!z(MISSING)u [in early] rssi: %!f(MISSING), rssiBorder: %!f(MISSING), rssiEarlyOffset: %!f(MISSING)"
+ "#type19,Commit change (empty uwb payload). But no actual change."
+ "#type19,Commit change (empty uwb payload). Notify payload change"
+ "#type19,Commit change (non-empty uwb payload). But no actual change"
+ "#type19,Commit change (non-empty uwb payload). Notify payload change with Aggregated uwb data: %!@(MISSING). Flag FE: %!d(MISSING). FS: %!d(MISSING). FC: %!d(MISSING)"
+ "#type19,Parsed. Flag FE: %!d(MISSING). FS: %!d(MISSING). FC: %!d(MISSING). FC2: %!d(MISSING)."
+ "#type19,UWB Data to parse: %!@(MISSING), Presence Data to parse: %!@(MISSING) "
+ "%!@(MISSING): %!f(MISSING)m %!s(MISSING) C:%!d(MISSING),I:%!d(MISSING),P:%!d(MISSING) CE: %!d(MISSING)"
+ "-[NINearbyUpdatesEngine _configureForRegionMonitoring:]"
+ "/AppleInternal/Library/BuildRoots/e20a253b-8c72-11ef-890e-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
+ "/AppleInternal/Library/BuildRoots/e20a253b-8c72-11ef-890e-725d7f06bcf4/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.2.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
+ "/Library/Caches/com.apple.xbs/Sources/Proximity/Libraries/NearbyAlgorithms/RegionMonitoring/NRBYDeviceMonitor.cpp"
+ "@60@0:8@16q24f32q36B44B48q52"
+ "@76@0:8d16@24@32i40d44@52@60@68"
+ "DeviceDiscoveryBurstAdvertiseRate"
+ "GesturePredictorWrapper"
+ "MotionBasedSpatialGesturesResources.bundle"
+ "NRBYRegionMonitor.mm"
+ "NRBYSpatialGesturePredictor.mm"
+ "PredictorSecondary_GestureClassifier"
+ "T@\"NSData\",C,N,V_presenceConfigData"
+ "TB,N,V_presenceConfigEnabled"
+ "TB,R,N,V_presenceConfigEnabled"
+ "TB,V_coarseEstimation"
+ "TC,R,N,V_handOrFaceDetection"
+ "TC,R,N,V_regionPresenceDetection"
+ "_aggregatedPresenceData"
+ "_aggregatedUWBData"
+ "_coarseEstimation"
+ "_fillNearbyObject:fromRegionSizeCategory:"
+ "_getRegionSizeCategoriesFromRegions:"
+ "_handOrFaceDetection"
+ "_handleDeviceConnectionWithDevice:isEligibleMotionState:isEligibleRegionState:selfAssociationState:"
+ "_handleDeviceRequestGravityMotionDetector:requestGravityMotionDetector:"
+ "_initWithUWBConfigData:presenceConfigData:"
+ "_isExecuteRegion:"
+ "_parseUWBData:presenceData:"
+ "_pathToModelWeights[kIdxMotionBasedSpatialGesturePredictor].has_value()"
+ "_pathToModelWeights[kIdxUwbSpatialGesturePredictor].has_value()"
+ "_presenceConfigData"
+ "_presenceConfigEnabled"
+ "_regionCategoryFromBluetoothDevice:"
+ "_regionMonitorMap"
+ "_regionPresenceDetection"
+ "acceptBluetoothSample:coarseEstimation:regionCategory:"
+ "aggregatedPresenceData"
+ "aggregatedUWBData"
+ "cachedDevices"
+ "coarseEstimation"
+ "gestureClassifiers[kIdxMotionBasedSpatialGesturePredictor] != NULL"
+ "gestureClassifiers[kIdxUwbSpatialGesturePredictor] != NULL"
+ "handOrFaceDetection"
+ "initStateForBluetoothDevice"
+ "initWithName:regionSizeCategory:radius:preferredUpdateRate:requiresUserIntent:coarseEstimation:devicePresencePreset:"
+ "initWithPresenceConfigData:"
+ "initWithRSSI:identifier:model:channel:machContinuousTimeSeconds:partIdentifier:name:presenceConfigData:"
+ "initWithUWBConfigData:"
+ "inputObject.deviceMotionBufferAfterProcessingPrimary.has_value() and inputObject.deltaUwbBufferAfterProcessingPrimary.has_value()"
+ "inputObject.deviceMotionBufferSecondary.has_value()"
+ "name: %!@(MISSING), cat: %!@(MISSING), radius: %!f(MISSING) m, rate: %!s(MISSING), intent: %!d(MISSING),  coarse: %!d(MISSING), presencePreset: %!s(MISSING)"
+ "pitch"
+ "presenceConfigData"
+ "presenceConfigEnabled"
+ "prewarmStateRegionThreshold"
+ "regionPresenceDetection"
+ "roll"
+ "setCoarseEstimation:"
+ "setHandOrFaceDetection:"
+ "setPresenceConfigData:"
+ "setPresenceConfigEnabled:"
+ "setRegionPresenceDetection:"
+ "v28@0:8Q16B24"
+ "v340@?0d8Q16{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}fiiiBB})B}24{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}fiiiBB})B}80{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}})B}136{optional<float>=(?=cf)B}328B336"
+ "v348@0:8Q16{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}fiiiBB})B}24{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}fiiiBB})B}80d136{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}})B}144{optional<float>=(?=cf)B}336B344"
+ "v36@0:8r^v16B24q28"
+ "v44@0:8{optional<unsigned long long>=(?=cQ)B}16B32B36B40"
+ "yaw"
+ "{set<NIRegionSizeCategory, std::less<NIRegionSizeCategory>, std::allocator<NIRegionSizeCategory>>={__tree<NIRegionSizeCategory, std::less<NIRegionSizeCategory>, std::allocator<NIRegionSizeCategory>>=^v{__compressed_pair<std::__tree_end_node<std::__tree_node_base<void *> *>, std::allocator<std::__tree_node<NIRegionSizeCategory, void *>>>={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{__compressed_pair<unsigned long, std::less<NIRegionSizeCategory>>=Q}}}24@0:8@16"
+ "{unordered_map<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>, std::hash<NIRegionSizeCategory>, std::equal_to<NIRegionSizeCategory>, std::allocator<std::pair<const NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>>>=\"__table_\"{__hash_table<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, std::__unordered_map_hasher<NIRegionSizeCategory, std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, std::hash<NIRegionSizeCategory>, std::equal_to<NIRegionSizeCategory>>, std::__unordered_map_equal<NIRegionSizeCategory, std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, std::equal_to<NIRegionSizeCategory>, std::hash<NIRegionSizeCategory>>, std::allocator<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<NIRegionSizeCategory, std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, std::hash<NIRegionSizeCategory>, std::equal_to<NIRegionSizeCategory>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<NIRegionSizeCategory, std::__hash_value_type<NIRegionSizeCategory, std::unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor>>, std::equal_to<NIRegionSizeCategory>, std::hash<NIRegionSizeCategory>>>=\"__value_\"f}}}"
+ "\xf0\xf0B"
- "\x01!Qr\x92!"
- "\n\x18CLPRoseMotionEvent.proto\x12\x11CLP.LogEntry.Rose\"\xe7\a\n\x0eRoseMotionData\x12I\n\rdevice_motion\x18\x01 \x01(\v22.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData\x1a<\n\x0eUnitQuaternion\x12\t\n\x01w\x18\x01 \x01(\x01\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\t\n\x01z\x18\x04 \x01(\x01\x1a\xcb\x06\n\x10DeviceMotionData\x12\x1e\n\x16mach_continuous_time_s\x18\x01 \x01(\x01\x12M\n\battitude\x18\x02 \x01(\v2;.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData.Attitude\x12V\n\rrotation_rate\x18\x03 \x01(\v2?.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData.RotationRate\x12^\n\x11user_acceleration\x18\x04 \x01(\v2C.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData.UserAcceleration\x12\x1c\n\x14mach_absolute_time_s\x18\x05 \x01(\x01\x12M\n\tgravity_g\x18\x06 \x01(\v2:.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData.Gravity\x12X\n\x0emagnetic_field\x18\a \x01(\v2@.CLP.LogEntry.Rose.RoseMotionData.DeviceMotionData.MagenticField\x1aU\n\bAttitude\x12I\n\x0funit_quaternion\x18\x01 \x01(\v20.CLP.LogEntry.Rose.RoseMotionData.UnitQuaternion\x1aA\n\fRotationRate\x12\x0f\n\ax_rad_s\x18\x01 \x01(\x01\x12\x0f\n\ay_rad_s\x18\x02 \x01(\x01\x12\x0f\n\az_rad_s\x18\x03 \x01(\x01\x1aB\n\x10UserAcceleration\x12\x0e\n\x06x_m_s2\x18\x01 \x01(\x01\x12\x0e\n\x06y_m_s2\x18\x02 \x01(\x01\x12\x0e\n\x06z_m_s2\x18\x03 \x01(\x01\x1a0\n\aGravity\x12\v\n\x03x_g\x18\x01 \x01(\x01\x12\v\n\x03y_g\x18\x02 \x01(\x01\x12\v\n\x03z_g\x18\x03 \x01(\x01\x1a9\n\rMagenticField\x12\f\n\x04x_uT\x18\x01 \x01(\x01\x12\f\n\x04y_uT\x18\x02 \x01(\x01\x12\f\n\x04z_uT\x18\x03 \x01(\x01"
- "!\x12\xf0!a\xa2\xf0\xf0B"
- "\"\x12"
- "#GestureFileUtils Model weights file '%!s(MISSING)' does not exist."
- "#ble,Overriding advertising burst rate with %!f(MISSING) ms"
- "#nimd,Cannot start activity updates because fMotionActivityMgr is nil"
- "#nimd,Cannot start device motion updates because fMotionManager is nil"
- "#nimd,Continued monitoring motion updates, detector type is %!s(MISSING)"
- "#nimd,Delivered motion state %!s(MISSING) with motion event id %!u(MISSING)"
- "#nimd,Generated new motion state %!s(MISSING) with event id %!u(MISSING), detector type is %!s(MISSING)"
- "#nimd,Minimum range measurement is %!f(MISSING), to switch motion detector type to DeviceMotionGravity"
- "#nimd,Minimum range measurement is %!f(MISSING), to switch motion detector type to MotionActivity"
- "#nimd,Motion state is forced to be Moving"
- "#nimd,No range measurements for too long time, switch to detector type of MotionActivity"
- "#nimd,Paused monitoring motion updates, detector type is %!s(MISSING)"
- "#nimd,Started device motion updates"
- "#nimd,Started monitoring motion updates, detector type is %!s(MISSING)"
- "#nimd,Started motion activity updates"
- "#nimd,Stopped device motion updates"
- "#nimd,Stopped monitoring motion updates"
- "#nimd,Stopped motion activity updates"
- "#nimd,Switched to motion detector type DeviceMotionGravity"
- "#nimd,Switched to motion detector type MotionActivity"
- "#nimd,Trying to switch to motion detector type DeviceMotionGravity which is current motion detector type"
- "#nimd,Trying to switch to motion detector type MotionActivity which is current motion detector type"
- "#nrby-eng,#spatialGesturesPredictor unexpected gesture type provided. defaulting to no predictor"
- "#regionmon Setting typePredictor as None since WifiToF based ranging does not use user intent score."
- "#ses-container,Creating a new session."
- "#ses-home,Can't update configuration, parameters are too different\nOld: %!@(MISSING)\nNew: %!@(MISSING)"
- "#ses-home,Device rediscovered decision: not restarting session since address is the same and role != responder and wifi ranging bit is unchanged and wifi ranging not enabled."
- "#ses-home,Dropping BT RSSI sample for device with idsDeviceID is nil"
- "#ses-home,Dropping BT RSSI sample for device: %!@(MISSING) which does not have model info"
- "#ses-home,Dropping BT RSSI sample for device: %!@(MISSING) which is of model: %!@(MISSING) because reported RSSI is UNKNOWN"
- "#ses-home,Empty string is generating a non zero hash, this will break device part logic -- INVESTIGATE"
- "#ses-home,adjusting ranging parameters command due to peer address roll or wifi ranging capable bit update. advAddressChanged: %!d(MISSING), wifiRangingChanged: %!d(MISSING)"
- "#type19,Commit change (empty payload). But no actual change."
- "#type19,Commit change (empty payload). Using dummy data."
- "#type19,Commit change (non-empty payload), but no actual change"
- "#type19,Commit change (non-empty payload). Aggregated data: %!@(MISSING). Flag FE: %!d(MISSING). FS: %!d(MISSING). FC: %!d(MISSING)"
- "#type19,Data to parse: %!@(MISSING)"
- "#type19,Parsed. Flag FE: %!d(MISSING). FS: %!d(MISSING). FC: %!d(MISSING). FC2: %!d(MISSING)"
- "%!@(MISSING): %!f(MISSING)m %!s(MISSING) C:%!d(MISSING),I:%!d(MISSING),P:%!d(MISSING)"
- "/AppleInternal/Library/BuildRoots/955b7ce0-87db-11ef-857c-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/google/protobuf/repeated_field.h"
- "/AppleInternal/Library/BuildRoots/955b7ce0-87db-11ef-857c-86b8363ea862/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS18.1.Internal.sdk/usr/local/include/google/protobuf/wire_format_lite_inl.h"
- "@68@0:8d16@24@32i40d44@52@60"
- "DeviceDiscoveryBurstAdvertiseRateMs"
- "NRBYRegionMonitor.cpp"
- "NRBYSpatialGesturePredictor.cpp"
- "_aggregatedData"
- "_parseData:"
- "_pathToModelWeights.has_value()"
- "_regionMonitor"
- "acceptBluetoothSample:"
- "aggregatedData"
- "initWithRSSI:identifier:model:channel:machContinuousTimeSeconds:partIdentifier:name:"
- "name: %!@(MISSING), cat: %!@(MISSING), radius: %!f(MISSING) m, rate: %!s(MISSING), intent: %!d(MISSING), presencePreset: %!s(MISSING)"
- "v340@?0d8Q16{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}fiiiB})B}24{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}fiiiB})B}80{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}})B}136{optional<float>=(?=cf)B}328B336"
- "v348@0:8Q16{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}fiiiB})B}24{optional<nearby::algorithms::region_monitoring::Region>=(?=c{Region={basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>={__rep=(?={__short=[23c][0C]b7b1}{__long=*Qb63b1}{__raw=[3Q]})}}}fiiiB})B}80d136{optional<nearby::algorithms::common::RangeResult>=(?=c{RangeResult=Qdfi{optional<nearby::algorithms::common::AngleMeasurement>=(?=c{AngleMeasurement=ffi})B}d{optional<int>=(?=ci)B}{optional<int>=(?=ci)B}{optional<double>=(?=cd)B}{optional<unsigned char>=(?=cC)B}{optional<double>=(?=cd)B}{optional<double>=(?=cd)B}ii{optional<nearby::algorithms::common::MagneticFieldStrengthCheckParameter>=(?=c{MagneticFieldStrengthCheckParameter=idd})B}{optional<double>=(?=cd)B}{optional<unsigned short>=(?=cS)B}{optional<unsigned char>=(?=cC)B}{optional<unsigned char>=(?=cC)B}})B}144{optional<float>=(?=cf)B}336B344"
- "{unique_ptr<nearby::algorithms::region_monitoring::RegionMonitor, std::default_delete<nearby::algorithms::region_monitoring::RegionMonitor>>=\"__ptr_\"{__compressed_pair<nearby::algorithms::region_monitoring::RegionMonitor *, std::default_delete<nearby::algorithms::region_monitoring::RegionMonitor>>=\"__value_\"^{RegionMonitor}}}"
- "\xf0\xf2"

```
