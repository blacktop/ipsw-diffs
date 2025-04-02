## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness`

```diff

-1902.100.119.0.0
-  __TEXT.__text: 0xd2270
+1902.120.16.0.0
+  __TEXT.__text: 0xd1ee8
   __TEXT.__auth_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x6a5c
-  __TEXT.__const: 0x8f40
+  __TEXT.__objc_methlist: 0x6a3c
+  __TEXT.__const: 0x8f30
   __TEXT.__gcc_except_tab: 0x18e0
-  __TEXT.__cstring: 0x855e
-  __TEXT.__oslogstring: 0x10bb7
+  __TEXT.__cstring: 0x8693
+  __TEXT.__oslogstring: 0x10959
   __TEXT.__dlopen_cstrs: 0xca
   __TEXT.__unwind_info: 0x2bd8
-  __TEXT.__objc_classname: 0x8b0
-  __TEXT.__objc_methname: 0xd3a2
-  __TEXT.__objc_methtype: 0x3331
-  __TEXT.__objc_stubs: 0xac80
+  __TEXT.__objc_classname: 0x8c9
+  __TEXT.__objc_methname: 0xd5f8
+  __TEXT.__objc_methtype: 0x3479
+  __TEXT.__objc_stubs: 0xad40
   __DATA_CONST.__got: 0x388
   __DATA_CONST.__const: 0xc70
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33c0
+  __DATA_CONST.__objc_selrefs: 0x3400
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x310
-  __DATA_CONST.__objc_arraydata: 0x618
+  __DATA_CONST.__objc_arraydata: 0x608
   __AUTH_CONST.__auth_got: 0xb88
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x1de8
-  __AUTH_CONST.__cfstring: 0x9ae0
-  __AUTH_CONST.__objc_const: 0x14200
+  __AUTH_CONST.__cfstring: 0x9c40
+  __AUTH_CONST.__objc_const: 0x14940
   __AUTH_CONST.__objc_intobj: 0x6c0
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x320
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH.__objc_data: 0xd20
-  __DATA.__objc_ivar: 0xe78
-  __DATA.__data: 0x58515
+  __DATA.__objc_ivar: 0xe6c
+  __DATA.__data: 0x58575
   __DATA.__bss: 0x1c0
   __DATA_DIRTY.__objc_data: 0x1220
   __DATA_DIRTY.__data: 0x30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4195
-  Symbols:   9075
-  CStrings:  6269
+  Functions: 4183
+  Symbols:   9085
+  CStrings:  6309
 
Symbols:
+ -[CBPILParams cilCurveLux]
+ -[CBPILParams cilCurveNits]
+ -[CBPILParams cilKnownDutyCycle]
+ -[CBPILParams cilKnownNits]
+ -[CBPILParams initWithLuxArray:nitsArray:lutSize:]
+ -[CBPILParams maxHWDutyCycle]
+ -[CBPILParams milCurveLux]
+ -[CBPILParams milCurveNits]
+ -[CBPILParams milKnownDutyCycle]
+ -[CBPILParams milKnownNits]
+ -[CBPILParams minHWDutyCycle]
+ -[PILABCurve initWithParams:andPilControlType:]
+ -[PILABCurve initWithParams:andPilControlType:].cold.1
+ -[PILABCurve initialiseCurveFrom:andPilControlType:]
+ -[PILAutoBrightnessModule handleEnablementStateChange:]
+ -[PILAutoBrightnessModule initWithQueue:PILParams:calibration:andALSServiceClient:andPILControlType:]
+ -[PILAutoBrightnessModule updatePILRangeIfNeeded]
+ -[PILContainer handleEnablementStateChangeForKeyPath:andState:]
+ -[PILController calibrationScalar]
+ -[PILController dealloc]
+ -[PILController dutyCycleRangeFetched]
+ -[PILController fetchDutyCycleRangeIfNeeded]
+ -[PILController fetchDutyCycleRangeIfNeeded].cold.1
+ -[PILController handleIndicatorStateChange:]
+ -[PILController initWithCalibration:andControlType:andTransport:andDefaults:]
+ -[PILController isIndicatorEnabled]
+ -[PILController maximumAchievableBrightness]
+ -[PILController minimumAchievableBrightness]
+ -[PILController setBrightness:]
+ -[PILController setBrightness:].cold.1
+ -[PILController setCalibrationScalar:]
+ -[PILController setSystemDesiredScalar:]
+ -[PILController start]
+ -[PILController start].cold.1
+ -[PILController stop]
+ -[PILController stop].cold.1
+ -[PILController systemDesiredScalar]
+ -[PILStateMonitor handlePILIOServiceEvent:]
+ -[PILStateMonitor handlePILSystemStatusEvent:]
+ -[PILStateMonitor initWithQueue:andSource:]
+ -[PILStateMonitor registerForAllSystemStatusNotifications]
+ -[PILStateMonitor unregisterForAllSystemStatusNotifications]
+ -[PILStateMonitor updatePILStateForControl:fromSource:newState:]
+ -[PILTransportAPDS dealloc]
+ -[PILTransportAPDS dealloc].cold.1
+ -[PILTransportAPDS getDutyCycleMin:andMax:]
+ -[PILTransportAPDS getDutyCycleMin:andMax:].cold.1
+ -[PILTransportAPDS initWithQueue:]
+ -[PILTransportAPDS initWithQueue:].cold.1
+ -[PILTransportAPDS setDutyCycle:]
+ -[PILTransportAPDS setDutyCycle:].cold.1
+ -[PILTransportAPDS start]
+ -[PILTransportAPDS stop]
+ -[PILTransportHID dealloc]
+ -[PILTransportHID getDutyCycleMin:andMax:]
+ -[PILTransportHID getDutyCycleThreshold:]
+ -[PILTransportHID getDutyCycleThreshold:].cold.1
+ -[PILTransportHID hidServiceArrived:]
+ -[PILTransportHID initWithQueue:]
+ -[PILTransportHID lookupMILServiceTrusted]
+ -[PILTransportHID lookupMILServiceUntrusted]
+ -[PILTransportHID readData:withSize:fromRegister:]
+ -[PILTransportHID registerForAllMILNotifications]
+ -[PILTransportHID registerForAllMILNotifications].cold.1
+ -[PILTransportHID setDutyCycle:]
+ -[PILTransportHID setDutyCycleInternal:]
+ -[PILTransportHID setDutyCycleInternal:].cold.1
+ -[PILTransportHID start]
+ -[PILTransportHID stop]
+ -[PILTransportHID unregisterForAllMILNotifications]
+ -[PILTransportHID writeDataTrusted:]
+ -[PILTransportHID writeDataUntrusted:withSize:toRegister:withAddressSize:]
+ OBJC_IVAR_$_CBPILParams._cilCurveLux
+ OBJC_IVAR_$_CBPILParams._cilCurveNits
+ OBJC_IVAR_$_CBPILParams._cilKnownDutyCycle
+ OBJC_IVAR_$_CBPILParams._cilKnownNits
+ OBJC_IVAR_$_CBPILParams._maxHWDutyCycle
+ OBJC_IVAR_$_CBPILParams._milCurveLux
+ OBJC_IVAR_$_CBPILParams._milCurveNits
+ OBJC_IVAR_$_CBPILParams._milKnownDutyCycle
+ OBJC_IVAR_$_CBPILParams._milKnownNits
+ OBJC_IVAR_$_CBPILParams._minHWDutyCycle
+ OBJC_IVAR_$_PILABCurve._params
+ OBJC_IVAR_$_PILAutoBrightnessModule._pilBrightnessRangeSet
+ OBJC_IVAR_$_PILAutoBrightnessModule._pilController
+ OBJC_IVAR_$_PILAutoBrightnessModule._rampString
+ OBJC_IVAR_$_PILContainer._cilBrightnessModule
+ OBJC_IVAR_$_PILContainer._milBrightnessModule
+ OBJC_IVAR_$_PILController._calibrationScalar
+ OBJC_IVAR_$_PILController._defaults
+ OBJC_IVAR_$_PILController._dutyCycleRangeFetched
+ OBJC_IVAR_$_PILController._isIndicatorEnabled
+ OBJC_IVAR_$_PILController._knownDutyCycle
+ OBJC_IVAR_$_PILController._knownNits
+ OBJC_IVAR_$_PILController._logHandle
+ OBJC_IVAR_$_PILController._maximumDutyCycle
+ OBJC_IVAR_$_PILController._minimumDutyCycle
+ OBJC_IVAR_$_PILController._running
+ OBJC_IVAR_$_PILController._systemDesiredScalar
+ OBJC_IVAR_$_PILController._transport
+ OBJC_IVAR_$_PILStateMonitor._source
+ OBJC_IVAR_$_PILTransportAPDS._apdsConnection
+ OBJC_IVAR_$_PILTransportAPDS._running
+ OBJC_IVAR_$_PILTransportHID._connect
+ OBJC_IVAR_$_PILTransportHID._ioNotificationObject
+ OBJC_IVAR_$_PILTransportHID._ioNotificationPort
+ OBJC_IVAR_$_PILTransportHID._ioServiceArrivalIterator
+ OBJC_IVAR_$_PILTransportHID._logHandle
+ OBJC_IVAR_$_PILTransportHID._milHIDSystemClient
+ OBJC_IVAR_$_PILTransportHID._milPlugin
+ OBJC_IVAR_$_PILTransportHID._queue
+ OBJC_IVAR_$_PILTransportHID._running
+ _OBJC_CLASS_$_PILController
+ _OBJC_CLASS_$_PILTransportAPDS
+ _OBJC_CLASS_$_PILTransportHID
+ _OBJC_METACLASS_$_PILController
+ _OBJC_METACLASS_$_PILTransportAPDS
+ _OBJC_METACLASS_$_PILTransportHID
+ __28-[PILContainer setupModules]_block_invoke.12
+ __28-[PILContainer setupModules]_block_invoke.12.cold.1
+ __42-[PILTransportHID lookupMILServiceTrusted]_block_invoke.12
+ __OBJC_$_INSTANCE_METHODS_PILController
+ __OBJC_$_INSTANCE_METHODS_PILTransportAPDS
+ __OBJC_$_INSTANCE_METHODS_PILTransportHID
+ __OBJC_$_INSTANCE_VARIABLES_PILController
+ __OBJC_$_INSTANCE_VARIABLES_PILTransportAPDS
+ __OBJC_$_INSTANCE_VARIABLES_PILTransportHID
+ __OBJC_$_PROP_LIST_PILController
+ __OBJC_$_PROP_LIST_PILTransportAPDS
+ __OBJC_$_PROP_LIST_PILTransportHID
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PILTransportProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PILTransportProtocol
+ __OBJC_$_PROTOCOL_REFS_PILTransportProtocol
+ __OBJC_CLASS_PROTOCOLS_$_PILTransportAPDS
+ __OBJC_CLASS_PROTOCOLS_$_PILTransportHID
+ __OBJC_CLASS_RO_$_PILController
+ __OBJC_CLASS_RO_$_PILTransportAPDS
+ __OBJC_CLASS_RO_$_PILTransportHID
+ __OBJC_LABEL_PROTOCOL_$_PILTransportProtocol
+ __OBJC_METACLASS_RO_$_PILController
+ __OBJC_METACLASS_RO_$_PILTransportAPDS
+ __OBJC_METACLASS_RO_$_PILTransportHID
+ __OBJC_PROTOCOL_$_PILTransportProtocol
+ ___29-[PILContainer newStatusInfo]_block_invoke
+ ___42-[PILTransportHID lookupMILServiceTrusted]_block_invoke
+ ___58-[PILStateMonitor registerForAllSystemStatusNotifications]_block_invoke
+ ___58-[PILStateMonitor registerForAllSystemStatusNotifications]_block_invoke_2
+ _objc_msgSend$cameraAttributions
+ _objc_msgSend$cilCurveLux
+ _objc_msgSend$cilCurveNits
+ _objc_msgSend$cilKnownDutyCycle
+ _objc_msgSend$cilKnownNits
+ _objc_msgSend$getDutyCycleMin:andMax:
+ _objc_msgSend$handleEnablementStateChange:
+ _objc_msgSend$handleEnablementStateChangeForKeyPath:andState:
+ _objc_msgSend$handlePILIOServiceEvent:
+ _objc_msgSend$handlePILSystemStatusEvent:
+ _objc_msgSend$initWithCalibration:andControlType:andTransport:andDefaults:
+ _objc_msgSend$initWithParams:andPilControlType:
+ _objc_msgSend$initWithQueue:PILParams:calibration:andALSServiceClient:andPILControlType:
+ _objc_msgSend$initWithQueue:andSource:
+ _objc_msgSend$initialiseCurveFrom:andPilControlType:
+ _objc_msgSend$maxHWDutyCycle
+ _objc_msgSend$maximumAchievableBrightness
+ _objc_msgSend$milCurveLux
+ _objc_msgSend$milCurveNits
+ _objc_msgSend$milKnownDutyCycle
+ _objc_msgSend$milKnownNits
+ _objc_msgSend$minHWDutyCycle
+ _objc_msgSend$minimumAchievableBrightness
+ _objc_msgSend$registerForAllSystemStatusNotifications
+ _objc_msgSend$setDutyCycleInternal:
+ _objc_msgSend$unregisterForAllSystemStatusNotifications
+ _objc_msgSend$updatePILRangeIfNeeded
+ _objc_msgSend$updatePILStateForControl:fromSource:newState:
- -[CBMILInterface dealloc]
- -[CBMILInterface getDutyCycleThreshold:]
- -[CBMILInterface getDutyCycleThreshold:].cold.1
- -[CBMILInterface hidServiceArrived:]
- -[CBMILInterface initWithQueue:]
- -[CBMILInterface lookupMILServiceTrusted]
- -[CBMILInterface lookupMILServiceUntrusted]
- -[CBMILInterface readData:withSize:fromRegister:]
- -[CBMILInterface registerForAllMILNotifications]
- -[CBMILInterface registerForAllMILNotifications].cold.1
- -[CBMILInterface setDutyCycle:]
- -[CBMILInterface setDutyCycle:].cold.1
- -[CBMILInterface start]
- -[CBMILInterface stop]
- -[CBMILInterface unregisterForAllMILNotifications]
- -[CBMILInterface writeDataTrusted:]
- -[CBMILInterface writeDataUntrusted:withSize:toRegister:withAddressSize:]
- -[CBPILParams blackBezel]
- -[CBPILParams initWithLuxArray:nitsArray:lutSize:andBlackBezel:]
- -[CBPILParams pilCurveLux]
- -[CBPILParams pilCurveNits]
- -[CILController calibrationScalar]
- -[CILController dealloc]
- -[CILController dealloc].cold.1
- -[CILController dutyCycleRangeFetched]
- -[CILController fetchDutyCycleRangeIfNeeded]
- -[CILController fetchDutyCycleRangeIfNeeded].cold.1
- -[CILController fetchDutyCycleRangeIfNeeded].cold.2
- -[CILController getBrightness]
- -[CILController getMaximumAchievableBrightness]
- -[CILController getMinimumAchievableBrightness]
- -[CILController handleIndicatorStateChange:]
- -[CILController initWithCurveVersion:]
- -[CILController initWithCurveVersion:].cold.1
- -[CILController initWithCurveVersion:].cold.2
- -[CILController initWithCurveVersion:].cold.3
- -[CILController isIndicatorEnabled]
- -[CILController setBrightness:]
- -[CILController setBrightness:].cold.1
- -[CILController setBrightness:].cold.2
- -[CILController setCalibrationSacalar:]
- -[CILController setCalibrationScalar:]
- -[CILController setSystemDesiredScalar:]
- -[CILController start]
- -[CILController start].cold.1
- -[CILController stop]
- -[CILController stop].cold.1
- -[CILController systemDesiredScalar]
- -[MILController calibrationScalar]
- -[MILController dealloc]
- -[MILController dutyCycleRangeFetched]
- -[MILController fetchDutyCycleThresholdIfNeeded]
- -[MILController fetchDutyCycleThresholdIfNeeded].cold.1
- -[MILController getBrightness]
- -[MILController getMaximumAchievableBrightness]
- -[MILController getMinimumAchievableBrightness]
- -[MILController handleIndicatorStateChange:]
- -[MILController initWithQueue:andCurveVersion:]
- -[MILController initWithQueue:andCurveVersion:].cold.1
- -[MILController isIndicatorEnabled]
- -[MILController setBrightness:]
- -[MILController setCalibrationSacalar:]
- -[MILController setCalibrationScalar:]
- -[MILController setSystemDesiredScalar:]
- -[MILController start]
- -[MILController start].cold.1
- -[MILController stop]
- -[MILController stop].cold.1
- -[MILController systemDesiredScalar]
- -[PILABCurve description]
- -[PILABCurve initWithParams:]
- -[PILABCurve initWithParams:].cold.1
- -[PILABCurve initialiseCurveFrom:]
- -[PILABCurve version]
- -[PILAutoBrightnessModule handlePILCameraStateChange:]
- -[PILAutoBrightnessModule handlePILMicStateChange:]
- -[PILAutoBrightnessModule initWithQueue:PILParams:calibration:andALSServiceClient:]
- -[PILAutoBrightnessModule initialiseControllersWithCalibration:]
- -[PILAutoBrightnessModule updateBrightness:].cold.2
- -[PILAutoBrightnessModule updateCILRangeIfNeeded]
- -[PILAutoBrightnessModule updateMILRangeIfNeeded]
- -[PILStateMonitor cameraStateChanged:]
- -[PILStateMonitor initWithQueue:]
- -[PILStateMonitor registerForAllMicNotifications]
- -[PILStateMonitor unregisterForAllMicNotifications]
- -[PILStateMonitor updateMicStateWithMediaData:]
- OBJC_IVAR_$_CBMILInterface._connect
- OBJC_IVAR_$_CBMILInterface._ioNotificationObject
- OBJC_IVAR_$_CBMILInterface._ioNotificationPort
- OBJC_IVAR_$_CBMILInterface._ioServiceArrivalIterator
- OBJC_IVAR_$_CBMILInterface._logHandle
- OBJC_IVAR_$_CBMILInterface._milHIDSystemClient
- OBJC_IVAR_$_CBMILInterface._milPlugin
- OBJC_IVAR_$_CBMILInterface._queue
- OBJC_IVAR_$_CBMILInterface._running
- OBJC_IVAR_$_CBPILParams._blackBezel
- OBJC_IVAR_$_CBPILParams._pilCurveLux
- OBJC_IVAR_$_CBPILParams._pilCurveNits
- OBJC_IVAR_$_CILController._apdsConnection
- OBJC_IVAR_$_CILController._calibrationScalar
- OBJC_IVAR_$_CILController._curveVersion
- OBJC_IVAR_$_CILController._dutyCycleRangeFetched
- OBJC_IVAR_$_CILController._isIndicatorEnabled
- OBJC_IVAR_$_CILController._knownDutyCycle
- OBJC_IVAR_$_CILController._knownNits
- OBJC_IVAR_$_CILController._logHandle
- OBJC_IVAR_$_CILController._mappedBrightness
- OBJC_IVAR_$_CILController._maximumDutyCycle
- OBJC_IVAR_$_CILController._minimumDutyCycle
- OBJC_IVAR_$_CILController._running
- OBJC_IVAR_$_CILController._systemDesiredScalar
- OBJC_IVAR_$_MILController._calibrationScalar
- OBJC_IVAR_$_MILController._dutyCycleRangeFetched
- OBJC_IVAR_$_MILController._isIndicatorEnabled
- OBJC_IVAR_$_MILController._knownDutyCycle
- OBJC_IVAR_$_MILController._knownNits
- OBJC_IVAR_$_MILController._logHandle
- OBJC_IVAR_$_MILController._mappedBrightness
- OBJC_IVAR_$_MILController._maximumDutyCycle
- OBJC_IVAR_$_MILController._milInterface
- OBJC_IVAR_$_MILController._minimumDutyCycle
- OBJC_IVAR_$_MILController._queue
- OBJC_IVAR_$_MILController._running
- OBJC_IVAR_$_MILController._systemDesiredScalar
- OBJC_IVAR_$_PILABCurve._version
- OBJC_IVAR_$_PILAutoBrightnessModule._cilBrightnessRangeSet
- OBJC_IVAR_$_PILAutoBrightnessModule._cilController
- OBJC_IVAR_$_PILAutoBrightnessModule._milBrightnessRangeSet
- OBJC_IVAR_$_PILAutoBrightnessModule._milController
- _OBJC_CLASS_$_CBMILInterface
- _OBJC_CLASS_$_CILController
- _OBJC_CLASS_$_MILController
- _OBJC_METACLASS_$_CBMILInterface
- _OBJC_METACLASS_$_CILController
- _OBJC_METACLASS_$_MILController
- __41-[CBMILInterface lookupMILServiceTrusted]_block_invoke.12
- __OBJC_$_INSTANCE_METHODS_CBMILInterface
- __OBJC_$_INSTANCE_METHODS_CILController
- __OBJC_$_INSTANCE_METHODS_MILController
- __OBJC_$_INSTANCE_VARIABLES_CBMILInterface
- __OBJC_$_INSTANCE_VARIABLES_CILController
- __OBJC_$_INSTANCE_VARIABLES_MILController
- __OBJC_$_PROP_LIST_CILController
- __OBJC_$_PROP_LIST_MILController
- __OBJC_$_PROP_LIST_PILABCurve
- __OBJC_CLASS_RO_$_CBMILInterface
- __OBJC_CLASS_RO_$_CILController
- __OBJC_CLASS_RO_$_MILController
- __OBJC_METACLASS_RO_$_CBMILInterface
- __OBJC_METACLASS_RO_$_CILController
- __OBJC_METACLASS_RO_$_MILController
- ___41-[CBMILInterface lookupMILServiceTrusted]_block_invoke
- ___49-[PILStateMonitor registerForAllMicNotifications]_block_invoke
- ___49-[PILStateMonitor registerForAllMicNotifications]_block_invoke_2
- _objc_msgSend$blackBezel
- _objc_msgSend$calibrationScalar
- _objc_msgSend$cameraStateChanged:
- _objc_msgSend$fetchDutyCycleThresholdIfNeeded
- _objc_msgSend$handlePILCameraStateChange:
- _objc_msgSend$handlePILMicStateChange:
- _objc_msgSend$initWithCurveVersion:
- _objc_msgSend$initWithParams:
- _objc_msgSend$initWithQueue:PILParams:calibration:andALSServiceClient:
- _objc_msgSend$initWithQueue:andCurveVersion:
- _objc_msgSend$initialiseControllersWithCalibration:
- _objc_msgSend$initialiseCurveFrom:
- _objc_msgSend$isPILBrightnessRamping
- _objc_msgSend$pilCurveLux
- _objc_msgSend$pilCurveNits
- _objc_msgSend$registerForAllMicNotifications
- _objc_msgSend$setCalibrationScalar:
- _objc_msgSend$unregisterForAllMicNotifications
- _objc_msgSend$updateCILRangeIfNeeded
- _objc_msgSend$updateMILRangeIfNeeded
- _objc_msgSend$updateMicStateWithMediaData:
- _objc_msgSend$version
CStrings:
+ "%s calibration updated to: %f"
+ "-[PILTransportHID hidServiceArrived:]"
+ "@\"<PILTransportProtocol>\""
+ "@\"PILAutoBrightnessModule\""
+ "@\"PILController\""
+ "@24@0:8@\"NSObject<OS_dispatch_queue>\"16"
+ "@40@0:8@16{PILStateSource=QQ}24"
+ "@40@0:8^f16^f24Q32"
+ "@52@0:8S16Q20@28{PILDefaults=IIIf}36"
+ "@56@0:8@16@24@32@40Q48"
+ "Auto-brightness Module initialised for %s Control"
+ "B32@0:8@16Q24"
+ "B32@0:8^I16^I24"
+ "CIL"
+ "CILAutoBrightnessEnabled"
+ "CILBrightness"
+ "CILBrightnessModule"
+ "CIL_BRIGHTNESS_RAMP"
+ "ControllerEnabled"
+ "Could not fetch duty cycle range for PIL Controller"
+ "Curve is initialised to default"
+ "Enablement status changed to %d"
+ "MIL"
+ "MILAutoBrightnessEnabled"
+ "MILBrightness"
+ "MILBrightnessModule"
+ "MIL_BRIGHTNESS_RAMP"
+ "Minimum achieavable brightness: %f ; Maximum achieavable brightness: %f"
+ "PIL Controller Started"
+ "PIL Controller Stopped"
+ "PIL Controller updated with min duty cycle: %i and max duty cycle: %i"
+ "PILController"
+ "PILTransportAPDS"
+ "PILTransportHID"
+ "PILTransportProtocol"
+ "Set duty cycle for PIL: %d for Nits: %f"
+ "T@\"CBFloatArray\",R,V_cilCurveLux"
+ "T@\"CBFloatArray\",R,V_cilCurveNits"
+ "T@\"CBFloatArray\",R,V_milCurveLux"
+ "T@\"CBFloatArray\",R,V_milCurveNits"
+ "TI,R,V_cilKnownNits"
+ "TI,R,V_maxHWDutyCycle"
+ "TI,R,V_milKnownNits"
+ "TI,R,V_minHWDutyCycle"
+ "Tf,R,V_cilKnownDutyCycle"
+ "Tf,R,V_milKnownDutyCycle"
+ "[New HID Event] eventTimestamp=%llu PILData.(pilEnablementStatus=%i) \n"
+ "_cilBrightnessModule"
+ "_cilCurveLux"
+ "_cilCurveNits"
+ "_cilKnownDutyCycle"
+ "_cilKnownNits"
+ "_defaults"
+ "_maxHWDutyCycle"
+ "_milBrightnessModule"
+ "_milCurveLux"
+ "_milCurveNits"
+ "_milKnownDutyCycle"
+ "_milKnownNits"
+ "_minHWDutyCycle"
+ "_pilBrightnessRangeSet"
+ "_pilController"
+ "_rampString"
+ "_source"
+ "_transport"
+ "cameraAttributions"
+ "cil-aab-curve-lux"
+ "cil-aab-curve-nits"
+ "cil-known-dutycycle"
+ "cil-known-nits"
+ "cilCurveLux"
+ "cilCurveNits"
+ "cilKnownDutyCycle"
+ "cilKnownNits"
+ "com.apple.CoreBrightness.CILABCurve"
+ "com.apple.CoreBrightness.CILAutoBrightnessModule"
+ "com.apple.CoreBrightness.MILABCurve"
+ "com.apple.CoreBrightness.MILAutoBrightnessModule"
+ "failed to commit brightness update"
+ "getDutyCycleMin:andMax:"
+ "handleEnablementStateChange:"
+ "handleEnablementStateChangeForKeyPath:andState:"
+ "handlePILIOServiceEvent:"
+ "handlePILSystemStatusEvent:"
+ "initWithCalibration:andControlType:andTransport:andDefaults:"
+ "initWithLuxArray:nitsArray:lutSize:"
+ "initWithParams:andPilControlType:"
+ "initWithQueue:PILParams:calibration:andALSServiceClient:andPILControlType:"
+ "initWithQueue:andSource:"
+ "initialiseCurveFrom:andPilControlType:"
+ "max-hw-dutycycle"
+ "maxHWDutyCycle"
+ "maximumAchievableBrightness"
+ "mil-aab-curve-lux"
+ "mil-aab-curve-nits"
+ "mil-known-dutycycle"
+ "mil-known-nits"
+ "milCurveLux"
+ "milCurveNits"
+ "milKnownDutyCycle"
+ "milKnownNits"
+ "min-hw-dutycycle"
+ "minHWDutyCycle"
+ "minimumAchievableBrightness"
+ "registerForAllSystemStatusNotifications"
+ "setDutyCycleInternal:"
+ "unregisterForAllSystemStatusNotifications"
+ "updatePILRangeIfNeeded"
+ "updatePILStateForControl:fromSource:newState:"
+ "v28@0:8@16B24"
+ "v36@0:8Q16Q24B32"
+ "{PILDefaults=\"minHWDutyCycle\"I\"maxHWDutyCycle\"I\"knownNits\"I\"knownDutyCycle\"f}"
+ "{PILStateSource=\"milSource\"Q\"cilSource\"Q}"
- "-[CBMILInterface hidServiceArrived:]"
- "@\"CBMILInterface\""
- "@\"CILController\""
- "@\"MILController\""
- "@44@0:8^f16^f24Q32B40"
- "Auto-brightness Module initialised for PIL Control"
- "CBMILInterface"
- "CIL Controller Started"
- "CIL Controller Started with min duty cycle: %i and max duty cycle: %i"
- "CIL Controller Stopped"
- "CIL Controller updated with min duty cycle: %i and max duty cycle: %i"
- "CIL calibration updated to: %f"
- "CIL minimum achieavable brightness: %f ; CIL maximum achieavable brightness: %f"
- "CIL status changed to %d"
- "CILController"
- "CILEnabled"
- "Could not fetch duty cycle range for CIL Controller"
- "Could not fetch duty cycle range for MIL Controller"
- "MIL Controller Started"
- "MIL Controller Stopped"
- "MIL Controller updated with min duty cycle: %i and max duty cycle: %i"
- "MIL calibration updated to: %f"
- "MIL minimum achieavable brightness: %f ; MIL maximum achieavable brightness: %f"
- "MIL status changed to %d"
- "MILController"
- "MILEnabled"
- "PIL AAB Curve is initialised to default"
- "PILBrightnessModule"
- "PILCurve Curve version: %lu"
- "PIL_BRIGHTNESS_RAMP"
- "Ramp update denied (currentRampTarget: %f -> targetNits: %f) - target change too small (%f); ramp ongoing: %s"
- "Set duty cycle for CIL: %d for Nits: %f"
- "T@\"CBFloatArray\",R,V_pilCurveLux"
- "T@\"CBFloatArray\",R,V_pilCurveNits"
- "TB,R,V_blackBezel"
- "[New MIL Event] eventTimestamp=%llu PILData.(pilEnablementStatus=%i) \n"
- "_blackBezel"
- "_cilBrightnessRangeSet"
- "_cilController"
- "_mappedBrightness"
- "_milBrightnessRangeSet"
- "_milController"
- "_milInterface"
- "black-bezel"
- "blackBezel"
- "cameraStateChanged:"
- "com.apple.CoreBrightness.PILABCurve"
- "com.apple.CoreBrightness.PILAutoBrightnessModule"
- "error creating the CIL Controller"
- "error creating the MIL Controller"
- "failed to commit CIL brightness update"
- "failed to commit MIL brightness update"
- "fetchDutyCycleThresholdIfNeeded"
- "getBrightness"
- "handlePILCameraStateChange:"
- "handlePILMicStateChange:"
- "initWithCurveVersion:"
- "initWithLuxArray:nitsArray:lutSize:andBlackBezel:"
- "initWithParams:"
- "initWithQueue:PILParams:calibration:andALSServiceClient:"
- "initWithQueue:andCurveVersion:"
- "initialiseControllersWithCalibration:"
- "initialiseCurveFrom:"
- "pil-aab-curve-lux"
- "pil-aab-curve-nits"
- "pilCurveLux"
- "pilCurveNits"
- "registerForAllMicNotifications"
- "setCalibrationSacalar:"
- "unregisterForAllMicNotifications"
- "updateCILRangeIfNeeded"
- "updateMILRangeIfNeeded"
- "updateMicStateWithMediaData:"

```
