## liblog_location.dylib

> `/usr/lib/log/liblog_location.dylib`

```diff

-3075.0.8.0.0
-  __TEXT.__text: 0x6a58
-  __TEXT.__auth_stubs: 0x290
+3164.0.0.0.0
+  __TEXT.__text: 0x6938
   __TEXT.__objc_methlist: 0x350
-  __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x44
-  __TEXT.__cstring: 0x47d4
-  __TEXT.__unwind_info: 0x158
-  __TEXT.__objc_classname: 0xf
-  __TEXT.__objc_methname: 0x10bb
-  __TEXT.__objc_methtype: 0xb4
-  __TEXT.__objc_stubs: 0x6e0
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0xae0
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0x34
+  __TEXT.__cstring: 0x483c
+  __TEXT.__unwind_info: 0x140
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xad8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x390
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x5480
+  __AUTH_CONST.__cfstring: 0x54c0
   __AUTH_CONST.__objc_const: 0xf8
+  __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__objc_dictobj: 0x168
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x8c0
-  __DATA.__bss: 0x10
+  __DATA.__data: 0x900
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 15C89DBA-60C5-3A38-A21A-341F4E2FB195
-  Functions: 90
-  Symbols:   601
-  CStrings:  1487
+  UUID: C14F81E5-7910-3966-919E-3AD9CA743DFA
+  Functions: 86
+  Symbols:   591
+  CStrings:  1363
 
Symbols:
+ _logObject_CLPerceptionHelper_Default
+ _logObject_Flip_Default
+ _logObject_Geotagging_Default
+ _logObject_HeadToHeadset_Default
+ _onceToken_CLPerceptionHelper_Default
+ _onceToken_Flip_Default
+ _onceToken_Geotagging_Default
+ _onceToken_HeadToHeadset_Default
- GCC_except_table74
- __ZNSt11logic_errorC2EPKc
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt12length_errorD1Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZTISt12length_error
- __ZTVSt12length_error
- __ZnwmSt19__type_descriptor_t
- ___cxa_allocate_exception
- ___cxa_free_exception
- ___cxa_throw
- _memmove
CStrings:
+ "CLLocationProvider_Type::kNotificationBufferedGnssLocation"
+ "CLLocationProvider_Type::kNotificationProactiveInertialOdometry"
- ":24@0:8@16"
- "@\"NSMethodSignature\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@16@0:8"
- "@32@0:8@16^{os_log_type_info_s=IB}24"
- "@40@0:8r*16@24^{os_log_type_info_s=IB}32"
- "Gyro"
- "JSONObjectWithType:value:info:"
- "JSONObjectWith_CLAppMonitor_Type__Notification:info:"
- "JSONObjectWith_CLBTLEFenceManager_Type__Notification:info:"
- "JSONObjectWith_CLBarometerCalibration_Types__Context:info:"
- "JSONObjectWith_CLBatteryChargerType:info:"
- "JSONObjectWith_CLClientAuthorizationStatus:info:"
- "JSONObjectWith_CLClientCorrectiveCompensation:info:"
- "JSONObjectWith_CLClientInUseLevel:info:"
- "JSONObjectWith_CLClientIncidentalUseMode:info:"
- "JSONObjectWith_CLClientLocation:info:"
- "JSONObjectWith_CLClientLocationReferenceFrame:info:"
- "JSONObjectWith_CLClientLocationSuitability:info:"
- "JSONObjectWith_CLClientManager_Type__AuthorizationRequestType:info:"
- "JSONObjectWith_CLClientRegistrationResult:info:"
- "JSONObjectWith_CLClientServiceType:info:"
- "JSONObjectWith_CLClientServiceTypeMask:info:"
- "JSONObjectWith_CLDaemonLocation:info:"
- "JSONObjectWith_CLDaemonLocationPrivate__OriginDevice:info:"
- "JSONObjectWith_CLDaemonStatus_Type__Battery:info:"
- "JSONObjectWith_CLDaemonStatus_Type__Reachability:info:"
- "JSONObjectWith_CLFenceManager_Type__Notification:info:"
- "JSONObjectWith_CLLocationDictionaryUtilitiesArrowState:info:"
- "JSONObjectWith_CLLocationDictionaryUtilitiesAuthorizationMask:info:"
- "JSONObjectWith_CLLocationDictionaryUtilitiesEntityClass:info:"
- "JSONObjectWith_CLLocationProvider_Type__MotionDetected:info:"
- "JSONObjectWith_CLLocationProvider_Type__Notification:info:"
- "JSONObjectWith_CLLocationStreamingGranularity:info:"
- "JSONObjectWith_CLLocationType:info:"
- "JSONObjectWith_CLMonitoringState:info:"
- "JSONObjectWith_CLMotionActivity:info:"
- "JSONObjectWith_CLMotionActivity__Confidence:info:"
- "JSONObjectWith_CLMotionActivity__Type:info:"
- "JSONObjectWith_CLRegionState:info:"
- "JSONObjectWith_CLSensorRecorder_Types__DataType:info:"
- "JSONObjectWith_CLSimulationLocationDeliveryBehavior:info:"
- "JSONObjectWith_CLSimulationLocationRepeatBehavior:info:"
- "JSONObjectWith_CLStreamingAwareLocationProviderLocalGPSStateMachine__LocationSourceState:info:"
- "JSONObjectWith_CLStreamingAwareLocationProviderLocalGPSStateMachine__WorkoutState:info:"
- "JSONObjectWith_CLStreamingAwareLocationProviderNoLocalGPSStateMachine__LocationSourceState:info:"
- "JSONObjectWith_CLStreamingAwareLocationProviderStateMachine__LocationSource:info:"
- "JSONObjectWith_CLSubHarvesterIdentifier:info:"
- "JSONObjectWith_CLTelephonyService_Type__Cell:info:"
- "JSONObjectWith_CLWifiService_Type__ScanType:info:"
- "JSONObjectWith_CMMotionCoprocessorReply_Log:info:"
- "JSONObjectWith_CMWakeGestureCrownOrientation:info:"
- "JSONObjectWith_CMWakeGestureState:info:"
- "JSONObjectWith_CMWakeGestureWristOrientation:info:"
- "JSONObjectWith_Encrypted_CLClientLocation:info:"
- "JSONObjectWith_Encrypted_CLLocationCoordinate2D:info:"
- "JSONObjectWith_Encrypted_latitude:info:"
- "JSONObjectWith_Encrypted_longitude:info:"
- "JSONObjectWith_Generic:info:"
- "JSONObjectWith_IOMessage:info:"
- "JSONObjectWith_NEVPNConnectivityState:info:"
- "JSONObjectWith_PSYSyncRestriction:info:"
- "JSONObjectWith_PSYSyncSessionType:info:"
- "JSONObjectWith_RBSTaskState:info:"
- "JSONObjectWith_RTLGestureType:info:"
- "JSONObjectWith_RTLState:info:"
- "JSONObjectWith_RTLocationOfInterestType:info:"
- "JSONObjectWith_RTRoutineMode:info:"
- "JSONObjectWith_SYSessionState:info:"
- "JSONObjectWith_SqliteResult:info:"
- "JSONObjectWith__CLClientManagerStateTrackerState:info:"
- "JSONObjectWith__CLDaemonStatusStateTrackerState:info:"
- "JSONObjectWith__CLLocationManagerStateTrackerState:info:"
- "JSONObjectWith_escape_only:info:"
- "UTF8String"
- "_formatterSignature"
- "_q"
- "_selectorForType"
- "addObject:"
- "array"
- "basic_string"
- "bytes"
- "count"
- "currentDirectoryPath"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithContentsOfFile:options:error:"
- "dataWithJSONObject:options:error:"
- "dealloc"
- "defaultManager"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "fileExistsAtPath:"
- "getReturnValue:"
- "init"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithClientLocation:"
- "initWithData:encoding:"
- "initWithString:"
- "instanceMethodSignatureForSelector:"
- "intValue"
- "integerValue"
- "invocationWithMethodSignature:"
- "invoke"
- "length"
- "longLongValue"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "objectForKeyedSubscript:"
- "pointerValue"
- "selectorForType:"
- "setArgument:atIndex:"
- "setObject:forKeyedSubscript:"
- "setSelector:"
- "setTarget:"
- "stringByAppendingFormat:"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "unsignedLongValue"
- "v16@0:8"
- "valueWithPointer:"

```
