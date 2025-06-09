## thermalmonitord

> `/usr/libexec/thermalmonitord`

```diff

-2007.120.5.0.0
-  __TEXT.__text: 0x58ba8
-  __TEXT.__auth_stubs: 0x1420
-  __TEXT.__objc_stubs: 0x5360
-  __TEXT.__objc_methlist: 0x419c
+2040.0.0.0.0
+  __TEXT.__text: 0x5a0b8
+  __TEXT.__auth_stubs: 0x13b0
+  __TEXT.__objc_stubs: 0x4f40
+  __TEXT.__objc_methlist: 0x40ec
   __TEXT.__const: 0x1cc0
-  __TEXT.__objc_classname: 0x111d
-  __TEXT.__objc_methtype: 0x19e9
-  __TEXT.__objc_methname: 0x88a5
-  __TEXT.__cstring: 0x4c23
-  __TEXT.__gcc_except_tab: 0x410
-  __TEXT.__oslogstring: 0x916e
-  __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x11e8
-  __DATA_CONST.__auth_got: 0xa28
-  __DATA_CONST.__got: 0x588
+  __TEXT.__objc_classname: 0x12be
+  __TEXT.__objc_methtype: 0x1ab8
+  __TEXT.__objc_methname: 0x82f4
+  __TEXT.__cstring: 0x4a8c
+  __TEXT.__gcc_except_tab: 0x3bc
+  __TEXT.__oslogstring: 0x991b
+  __TEXT.__unwind_info: 0x11a8
+  __DATA_CONST.__auth_got: 0x9f0
+  __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1460
-  __DATA_CONST.__cfstring: 0x61c0
-  __DATA_CONST.__objc_classlist: 0x4b0
+  __DATA_CONST.__const: 0x13b0
+  __DATA_CONST.__cfstring: 0x61e0
+  __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x300
+  __DATA_CONST.__objc_superrefs: 0x308
   __DATA_CONST.__objc_intobj: 0x768
   __DATA_CONST.__objc_arraydata: 0x260
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x1c8
-  __DATA.__objc_const: 0xcac8
-  __DATA.__objc_selrefs: 0x1ae0
-  __DATA.__objc_ivar: 0xab8
-  __DATA.__objc_data: 0x2ee0
-  __DATA.__data: 0x3c8
-  __DATA.__bss: 0x80f4
-  __DATA.__common: 0x9f0
+  __DATA.__objc_const: 0xc9b8
+  __DATA.__objc_selrefs: 0x1970
+  __DATA.__objc_ivar: 0xa64
+  __DATA.__objc_data: 0x32a0
+  __DATA.__data: 0x370
+  __DATA.__bss: 0x8e5c
+  __DATA.__common: 0x9e8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 48A530B4-42F5-39AF-A629-4F40B1A3C43F
-  Functions: 2036
-  Symbols:   417
-  CStrings:  4511
+  UUID: E0262E4E-81AD-3BEF-BF4F-D21AE578E1EA
+  Functions: 2014
+  Symbols:   407
+  CStrings:  4484
 
Symbols:
+ _NSStringFromSelector
+ __ZnwmSt19__type_descriptor_t
- _CFMakeCollectable
- _OBJC_CLASS_$__CDContextualChangeRegistration
- _OBJC_CLASS_$__CDContextualKeyPath
- _OBJC_CLASS_$__CDContextualPredicate
- __CTServerConnectionSetMaxTemperature
- __Znwm
- __os_feature_enabled_impl
- __sl_dlopen
- _abort_report_np
- _dispatch_assert_queue$V2
- _objc_getClass
- _objc_opt_new
CStrings:
+ "<Error> %@ Failed to create Cores per IP key for die %u loop %u\n"
+ "<Error> %@ must be overridden in a subclass"
+ "<Error> %@: Failed to create Cores per IP key for die %u loop %u\n"
+ "<Error> ERROR getNVRAMValueWithType: Unknown NVRAMValueType %d"
+ "<Error> ERROR: getNVRAMValue requested on non-NVRAM supported device"
+ "<Error> ERROR: readNVRAM Could not create LTS State TDDB IS copy"
+ "<Error> ERROR: readNVRAMData requested but path to NVRAM does not exist!"
+ "<Error> ERROR: readNVRAMData requested on non-NVRAM supported device!"
+ "<Error> Error: readNVRAMData Failed to read LTS State from NVRam"
+ "<Error> Failed to allocate memory for TDDB Integrator State\n"
+ "<Error> Failed to allocate memory for ltsStateACSKV4 struct\n"
+ "<Error> Failed to allocate memory for perIPCoreCountPtr struct\n"
+ "<Error> Failed to create TDDB IS key for die %u loop %u\n"
+ "<Error> Failed to create TDDB key for die %u loop %u core %u\n"
+ "<Error> Failed to create cluster core num key for die %u loop %u\n"
+ "<Error> Failed to create key for die %u loop %u core %u\n"
+ "<Error> Failed to create revision key for die %u loop %u core %u\n"
+ "<Error> Failed to read tddb cluster mask from persistant LTS Stats"
+ "<Error> Failed to save Cores per IP for lts-ctrl-%u-%u-cores\n"
+ "<Error> Failed to save IS revision for lts-ctrl-%u-%u-%u-is-rev\n"
+ "<Error> Failed to save cluster mask\n"
+ "<Error> Failed to send TDDB data to PMP: die %u loop %u core %u"
+ "<Error> Failed to send data to PMP: die %u loop %u core %u"
+ "<Error> Failed to update LTS TDDB Integrator State!\n"
+ "<Error> Failed to update! Cleaning up ltsStateData - loops: %u"
+ "<Error> Illegal ACSK Persistence version %d! Sending nothing to PMP!"
+ "<Error> Illegal Persistence version %d! Sending nothing to PMP!"
+ "<Error> LifetimeServoStatePersistenceACSK init failed\n"
+ "<Error> LifetimeServoStatePersistenceBase init failed\n"
+ "<Error> NVRAM Length %ld less than required %ld, cannot acquire IS data"
+ "<Error> notify_post(com.apple.system.earlythermalnotification) failed"
+ "<Error> notify_register_check(com.apple.system.earlythermalnotification) failed"
+ "<Error> notify_set_state(com.apple.system.earlythermalnotification) failed"
+ "<Notice> %@: Saving TDDB Cluster Mask 0x%x to NAND"
+ "<Notice> %@: lts-ctrl-%u-%u-cores=%u"
+ "<Notice> %@: lts-ctrl-tddb-cluster-mask=0x%x, tddb_cores: %u"
+ "<Notice> %@: total_cores: %u"
+ "<Notice> Copied TDDB LTS IS data from PMP"
+ "<Notice> Early notification = %d"
+ "<Notice> Failed to read Cores per IP for key %@"
+ "<Notice> Failed to read TDDB integrator state for key %@"
+ "<Notice> LTS getNANDVer: NAND counter does not exist"
+ "<Notice> NAND version %d too high - IS will be discarded and updated to version %d"
+ "<Notice> NVRAM version %d too high - IS will be discarded and updated to version %d"
+ "<Notice> Persistence filepath:%s"
+ "<Notice> Sending data to PMP: die %u loop %u core %u TDDB is: %@"
+ "<Notice> Sending data to PMP: die %u loop %u core %u is: %@"
+ "<Notice> getNVRAMValueWithType: %s = %d"
+ "<Notice> getNVRAMValueWithType: NVRAM ltsStateCommon pointer was not provided"
+ "<Notice> readNVRAM could not allocate memory for number of cores per IP"
+ "<Notice> sendLTSStateToPMP: dieCount:%u loopCount:%u tddbMask: 0x%x"
+ "<Notice> update power save active: %{BOOL}u"
+ "@\"LifetimeServoStatePersistenceBase\""
+ "B24@0:8^Q16"
+ "B24@0:8^v16"
+ "B28@0:8^{ltsStateACSKV4=^{ltsStateCommon}I^I^Q^Q^I}16I24"
+ "B32@0:8^v16^{__CFString=}24"
+ "B32@0:8^{ltsStateACSKV4=^{ltsStateCommon}I^I^Q^Q^I}16I24I28"
+ "Counter"
+ "I24@0:8^{ltsStateACSKV4=^{ltsStateCommon}I^I^Q^Q^I}16"
+ "I28@0:8i16^{ltsStateCommon=IIII}20"
+ "LTSUsesACSK"
+ "LifetimeServoStatePersistenceACSK"
+ "LifetimeServoStatePersistenceBase"
+ "None"
+ "TB,N,V_lowerPowerModeActive"
+ "TVRM"
+ "Version"
+ "^v16@0:8"
+ "^{__CFData=}16@0:8"
+ "_currNvramLTSStateACSK"
+ "_lowerPowerModeActive"
+ "com.apple.system.earlythermalnotification"
+ "die %u loop %u core %u TDDB is: %{public}@"
+ "die %u loop %u core %u is: %{public}@"
+ "earlyThermalNotificationToken"
+ "emitEarlyThermalNotification"
+ "forceSensorExchangeDataToSMC"
+ "getNVRAMValueWithType:commonState:"
+ "getNumTotalEntries:"
+ "getNumTotalTDDBEntries:"
+ "initClassVariables"
+ "isNandDataValidForKey:"
+ "isNvramDataValid:"
+ "lowerPowerModeActive"
+ "lts-ctrl-%u-%u-%u-is"
+ "lts-ctrl-%u-%u-%u-is-inuse"
+ "lts-ctrl-%u-%u-%u-is-rev"
+ "lts-ctrl-%u-%u-%u-is-tddb"
+ "lts-ctrl-%u-%u-%u-is-tddb-inuse"
+ "lts-ctrl-%u-%u-0-is-tddb-inuse"
+ "lts-ctrl-%u-%u-cores"
+ "lts-ctrl-0-0-0-is"
+ "lts-ctrl-tddb-cluster-mask"
+ "readNVRAMData"
+ "resolvePersistentLTSState:integratorStatePtr:nandDataValidityKey:minValidVer:"
+ "safeFreeLTSStatePtrs:"
+ "setLowerPowerModeActive:"
+ "tm109a1ab9d733f0974b9ea596d532ae40"
+ "tm13f8efd00743a586cd57f9fb88db752c"
+ "tm27675a4b01be1906dceb13c7b1048f3b"
+ "tm419884bb6ddcc8e81d56fee1c3529b9c"
+ "tm758adc76eb525f577accde7a9b98d157"
+ "tm7ed2703e2d4ee90243ee3fa14fdae9b9"
+ "tm8cbd64acbc3aafc953e23bd26f93df00"
+ "tma64f6721a707318428f8bb83c5fbc836"
+ "tmab617fa4739fe73705ca67f8e17c0eb2"
+ "tmb938222af14e487f9b18428a60284ec9"
+ "tmc8825e0d7de2c0d9d778618564948ffd"
+ "updateEarlyThermalNotification:"
+ "updateLTSStateISFromPMP:total_cores:"
+ "updateLTSStateISRev:total_cores:"
+ "updateLTSStateTDDBISFromPMP:tddb_cluster_mask:tddb_cores:"
+ "updatePowerSaveActive"
+ "v24@0:8^v16"
+ "v36@?0B8{vector<abm::BasebandThermalID, std::allocator<abm::BasebandThermalID>>=^C^C^C}12"
+ "v36@?0B8{vector<abm::ThermalSensorData, std::allocator<abm::ThermalSensorData>>=^{ThermalSensorData}^{ThermalSensorData}^{ThermalSensorData}}12"
+ "v44@0:8^{ltsStateCommon=IIII}16^Q24^{__CFString=}32I40"
+ "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}8^v40"
+ "writePersistedStateNvram:path:"
+ "{DetailedThermalBudgets=\"budgets\"[33{DetailedThermalBudget=\"clientID\"C\"powerValue\"I\"details\"Q}]\"count\"i}"
+ "{ltsStateACSKV4=\"ltsStateCommonPtr\"^{ltsStateCommon}\"tddbClusterMask\"I\"perIPCoreCountPtr\"^I\"integratorStatePtr\"^Q\"TDDBintegratorStatePtr\"^Q\"integratorStateRevPtr\"^I}"
- "-[ContextInPocket initWithParams:]"
- "/charging/topOffCheckpoint"
- "<Error> CT bad drop limit"
- "<Error> Could not create pocket context"
- "<Error> ERROR: getNVRAMCounter requested on non-NVRAM supported device"
- "<Error> ERROR: getNVRAMVer requested on non-NVRAM supported device"
- "<Error> ERROR: readNVRAM requested but path to NVRAM does not exist!"
- "<Error> ERROR: readNVRAM requested on non-NVRAM supported device!"
- "<Notice> Backlight Status changed %d -> %d"
- "<Notice> Disengaging HiP - backlightIsOn %d, connectedExternally %d, toppingOff %d, audioIsOn %d, carSessionActive %d, wakeInProgress %d, fieldDetectInProgress %d, powerIsOn %d"
- "<Notice> Engaging HiP - backlightIsOn %d, connectedExternally %d, toppingOff %d, audioIsOn %d, carSessionActive %d, wakeInProgress %d, fieldDetectInProgress %d, powerIsOn %d"
- "<Notice> HIP: Reacquiring Backlight Assertion"
- "<Notice> In-pocket context disabled due to restricted perf mode"
- "<Notice> LTS getNANDCounter: NAND counter does not exist"
- "<Notice> LTS getNVRAMCounter: NVRAM counter %d"
- "<Notice> LTS getNVRAMCounter: NVRAM counter does not exist"
- "<Notice> LTS getNVRAMVer: NVRAM version %d"
- "<Notice> LTS getNVRAMVer: NVRAM version does not exist"
- "<Notice> Persitence filepath:%s"
- "<Notice> UpdateSystemPower: Updare Power State to %d"
- "<Notice> UpdateSystemPower: WakeInProgress Reset"
- "@\"<BrightnessSystemMonitorable>\""
- "@\"<TMInvalidatable>\""
- "@\"CARSessionStatus\""
- "@\"LifetimeServoStatePersistence\""
- "B32@0:8^{ltsStateV3=^{ltsStateCommon}^Q^I}16^{__CFString=}24"
- "CARSessionObserving"
- "CARSessionStatus"
- "ContextInPocket"
- "ContextInPocket state"
- "HotInPocket Backlight Signal"
- "IOServiceFirstPublish"
- "RestrictedPerfMode"
- "T@\"<BrightnessSystemMonitorable>\",&,N,V_brightnessSystemMonitor"
- "T@\"NSObject<OS_dispatch_queue>\",N,V_inPocketQueue"
- "TB,N"
- "TB,N,VaudioIsOn"
- "TB,N,VconnectedExternally"
- "TB,N,VcontextIsActive"
- "TB,N,VpowerIsOn"
- "TB,N,VusesPackagePowerControl"
- "TC,N,V_minCPU"
- "TC,N,V_minGPU"
- "TI,N,VpmuPowerService"
- "TQ,N,VstockholmFieldDetectInProgressUntilTime"
- "TQ,N,VwakeInProgressUntilTime"
- "Ti,N,V_audioRunningToken"
- "Ti,N,V_minPackagePower"
- "Ti,N,V_stockholmToken"
- "Ti,N,V_uncapRequestClientID"
- "Ti,N,VmitigationControllerListID"
- "Unable to find class %s"
- "^{ltsStateV3=^{ltsStateCommon}^Q^I}16@0:8"
- "_acquireBacklightAssertion"
- "_atomic_isBacklightOn"
- "_audioRunningToken"
- "_backlightAssertion"
- "_brightnessSystemMonitor"
- "_carSessionActive"
- "_carSessionStatus"
- "_inPocketQueue"
- "_minCPU"
- "_minGPU"
- "_minPackagePower"
- "_stockholmToken"
- "_uncapRequestClientID"
- "addSessionObserver:"
- "audioIsOn"
- "audioRunningToken"
- "backlightIsOn"
- "brightnessSystemMonitor"
- "cancelledConnectionAttemptOnTransport:"
- "com.apple.ThermalMonitor.context.pocket"
- "com.apple.cltm.context"
- "com.apple.cltm.obcstatus"
- "com.apple.coreaudio.IORunning"
- "com.apple.request.hipuncap"
- "connectedExternally"
- "contextIsActive"
- "createNewInPocketContext:"
- "currentSession"
- "getNANDCounter"
- "getNANDVer"
- "getNVRAMCounter"
- "getNVRAMVer"
- "handleCurrentTopOffStatusWithContext:"
- "inPocketContextParams"
- "inPocketQueue"
- "initAudioHandling"
- "initPowerHandling"
- "initStockholmHandling"
- "isNandDataValid"
- "isNvramDataValid"
- "keyPathWithKey:"
- "localWakingRegistrationWithIdentifier:contextualPredicate:clientIdentifier:callback:"
- "logHiPSignalsToPowerLog::::"
- "minCPU"
- "minGPU"
- "minPackagePower"
- "mitigationControllerListID"
- "powerIsOn"
- "powerexperienced"
- "predicateForChangeAtKeyPath:"
- "registerCallback:"
- "registerForTopOffStatusChanges"
- "removeSessionObserver:"
- "resolvePersistentLTSState"
- "session:didUpdateConfiguration:"
- "sessionDidConnect:"
- "sessionDidDisconnect:"
- "setAudioIsOn:"
- "setAudioRunningToken:"
- "setBacklightIsOn:"
- "setBrightnessSystemMonitor:"
- "setConnectedExternally:"
- "setContextIsActive:"
- "setInPocketQueue:"
- "setMinCPU:"
- "setMinGPU:"
- "setMinPackagePower:"
- "setMitigationControllerListID:"
- "setPmuPowerService:"
- "setPowerIsOn:"
- "setStockholmFieldDetectInProgressUntilTime:"
- "setStockholmToken:"
- "setUncapRequestClientID:"
- "setUsesPackagePowerControl:"
- "setWakeInProgressUntilTime:"
- "softlink:r:path:/System/Library/PrivateFrameworks/CarKit.framework/CarKit"
- "startedConnectionAttemptOnTransport:"
- "stockholmFieldDetectInProgressUntilTime"
- "stockholmToken"
- "uncapRequestClientID"
- "updateContextActiveState"
- "usesInPocketContext"
- "usesPackagePowerControl"
- "v24@0:8@\"CARSession\"16"
- "v24@0:8^{ltsStateV3=^{ltsStateCommon}^Q^I}16"
- "v24@?0@\"NSString\"8@\"NSDictionary\"16"
- "v32@0:8@\"CARSession\"16@\"CARSessionConfiguration\"24"
- "v32@0:8c16B20B24B28"
- "v36@?0B8{vector<abm::BasebandThermalID, std::allocator<abm::BasebandThermalID>>=^C^C{__compressed_pair<abm::BasebandThermalID *, std::allocator<abm::BasebandThermalID>>=^C}}12"
- "v36@?0B8{vector<abm::ThermalSensorData, std::allocator<abm::ThermalSensorData>>=^{ThermalSensorData}^{ThermalSensorData}{__compressed_pair<abm::ThermalSensorData *, std::allocator<abm::ThermalSensorData>>=^{ThermalSensorData}}}12"
- "v48@?0{Result=i{basic_string<char, std::char_traits<char>, std::allocator<char>>={__compressed_pair<std::basic_string<char>::__rep, std::allocator<char>>=(__rep={__short=[23c][0C]b7b1}{__long=*Qb63b1})}}}8^v40"
- "wakeInProgressUntilTime"
- "writeV3PersistedStateNvram:path:"
- "{DetailedThermalBudgets=\"budgets\"[30{DetailedThermalBudget=\"clientID\"C\"powerValue\"I\"details\"Q}]\"count\"i}"

```
