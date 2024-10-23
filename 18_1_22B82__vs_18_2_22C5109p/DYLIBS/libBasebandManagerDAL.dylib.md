## libBasebandManagerDAL.dylib

> `/usr/lib/libBasebandManagerDAL.dylib`

```diff

-1183.0.0.0.0
-  __TEXT.__text: 0x1078e4
-  __TEXT.__auth_stubs: 0x21d0
-  __TEXT.__init_offsets: 0x84
+1209.0.0.0.0
+  __TEXT.__text: 0x118fb4
+  __TEXT.__auth_stubs: 0x2340
+  __TEXT.__init_offsets: 0xb4
   __TEXT.__objc_methlist: 0x140
-  __TEXT.__const: 0x5ce7
-  __TEXT.__gcc_except_tab: 0x18564
-  __TEXT.__oslogstring: 0x4cfc
-  __TEXT.__cstring: 0x2bed
-  __TEXT.__unwind_info: 0x4c78
+  __TEXT.__const: 0x64d7
+  __TEXT.__gcc_except_tab: 0x1a2b4
+  __TEXT.__oslogstring: 0x5200
+  __TEXT.__cstring: 0x2f56
+  __TEXT.__unwind_info: 0x5208
   __TEXT.__objc_classname: 0x68
   __TEXT.__objc_methname: 0x626
   __TEXT.__objc_methtype: 0x1389
   __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x10a0
-  __DATA_CONST.__const: 0xe78
+  __DATA_CONST.__got: 0x1148
+  __DATA_CONST.__const: 0xf10
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x10f8
-  __AUTH_CONST.__const: 0x8130
-  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__auth_got: 0x11b0
+  __AUTH_CONST.__const: 0x8a38
+  __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x658
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x670
-  __DATA.__common: 0x38
-  __DATA.__bss: 0x1a8
+  __DATA.__data: 0x7c0
+  __DATA.__common: 0x40
+  __DATA.__bss: 0x1d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2873
-  Symbols:   4179
-  CStrings:  1100
+  Functions: 3061
+  Symbols:   4448
+  CStrings:  1164
 
Symbols:
+ _CFUserNotificationCreate
+ _CFUserNotificationDisplayNotice
+ _CFUserNotificationReceiveResponse
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyUtilTriggerNMI
+ _TelephonyUtilWriteStackshot
+ __ZGVN3ctu9SingletonI13HealthEventDBS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZGVN3ctu9SingletonI15DeviceHistoryDBS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN10BootModule30reportStatisticsSoftReset_syncEv
+ __ZN12HealthModule10initializeEN8dispatch13group_sessionE
+ __ZN12HealthModule19hasBarrierEventTypeERK11HealthEvent
+ __ZN12HealthModule25getBasebandFWVersion_syncEN8dispatch5blockIU13block_pointerFvNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEE
+ __ZN12HealthModule4wakeEN8dispatch13group_sessionE
+ __ZN12HealthModule5sleepEN8dispatch13group_sessionE
+ __ZN12HealthModule5startEN8dispatch13group_sessionE
+ __ZN12HealthModule6createENSt3__18weak_ptrI14ServiceManagerEE
+ __ZN12HealthModule8shutdownE13ShutdownStageN8dispatch13group_sessionE
+ __ZN12HealthModuleC1ENSt3__18weak_ptrI14ServiceManagerEEN8dispatch8workloopE
+ __ZN12HealthModuleC2ENSt3__18weak_ptrI14ServiceManagerEEN8dispatch8workloopE
+ __ZN12HealthModuleD0Ev
+ __ZN12HealthModuleD1Ev
+ __ZN12HealthModuleD2Ev
+ __ZN12capabilities3abs17shouldBlockResetsEv
+ __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
+ __ZN12capabilities3abs26supportsEFSEraseOnBootLoopEv
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
+ __ZN13BasebandStats11updateStatsEN3xpc4dictE
+ __ZN13BasebandStats12initFromDiskEv
+ __ZN13BasebandStats23getCurrentBasebandStatsEv
+ __ZN13BasebandStats8getStatsEv
+ __ZN13HealthEventDB12commitToDiskEv
+ __ZN13HealthEventDB12initFromDiskEv
+ __ZN13HealthEventDB13getHealthInfoEv
+ __ZN13HealthEventDB14addHealthEventEN11HealthEvent4TypeE
+ __ZN13HealthEventDB14addHealthEventERK11HealthEvent
+ __ZN13HealthEventDB15updateBootStatsEN3xpc4dictE
+ __ZN13HealthEventDB7clearDBEv
+ __ZN13HealthEventDB7getNameEv
+ __ZN13HealthEventDBC1Ev
+ __ZN13HealthEventDBC2Ev
+ __ZN15CommCenterStats11updateStatsEN3xpc4dictE
+ __ZN15CommCenterStats12initFromDiskEv
+ __ZN15CommCenterStats8getStatsEv
+ __ZN15DeviceHistoryDB12commitToDiskEv
+ __ZN15DeviceHistoryDB12initFromDiskEv
+ __ZN15DeviceHistoryDB16addDeviceHistoryE18_DeviceHistoryItem
+ __ZN15DeviceHistoryDB7getNameEv
+ __ZN15DeviceHistoryDBC1Ev
+ __ZN15DeviceHistoryDBC2Ev
+ __ZN20AppleBasebandManager7performENSt3__110shared_ptrIN3abm6client7CommandEEE
+ __ZN3abm17kKeyBasebandStatsE
+ __ZN3abm18kHealthEventDBNameE
+ __ZN3abm18kKeyBasebandUpTimeE
+ __ZN3abm18kLogVersionHistoryE
+ __ZN3abm19kKeyCommCenterStatsE
+ __ZN3abm20kBasebandNVDataEraseE
+ __ZN3abm20kKeyHealthEventTimesE
+ __ZN3abm20kKeyHealthEventTypesE
+ __ZN3abm22kCommandBasebandNVDataE
+ __ZN3abm22kCommandGetHealthStatsE
+ __ZN3abm23KEventDeviceInfoChangedE
+ __ZN3abm23kEventSystemInfoChangedE
+ __ZN3abm24kKeyBasebandNVDataActionE
+ __ZN3abm25kCommandUpdateBBBootStatsE
+ __ZN3abm25kKeyCommCenterStatsUpTimeE
+ __ZN3abm26kKeyTraceResetModeOnAPBootE
+ __ZN3abm27kKeyStatsBootHardResetCountE
+ __ZN3abm27kKeyStatsBootSoftResetCountE
+ __ZN3abm29kKeyCommCenterStatsLastUpTimeE
+ __ZN3abm30kKeyCommCenterStatsLaunchCountE
+ __ZN3abm32kEventSystemInfoOSVersionChangedE
+ __ZN3abm34kEventSystemInfoFirmwareSideLoadedE
+ __ZN3abm36kEventSystemInfoHardwareModelChangedE
+ __ZN3abm6client7Command6createERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEN3xpc4dictEN8dispatch8callbackIU13block_pointerFviN3ctu2cf11CFSharedRefIK14__CFDictionaryEEEEE
+ __ZN3ctu20DispatchTimerService6createENSt3__110shared_ptrINS_9LogServerEEE
+ __ZN3ctu2cf6assignERaPK10__CFNumber
+ __ZN3ctu2cf6assignERxPK10__CFNumber
+ __ZN3ctu5power7manager20simulateNotificationEjb
+ __ZN3ctu9SingletonI13HealthEventDBS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN3ctu9SingletonI15DeviceHistoryDBS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN3sys18isFWVersionChangedERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN3sys18isOSVersionChangedEv
+ __ZN3sys22isHardwareModelChangedEv
+ __ZN3sys25getCurrentBootSessionUUIDEv
+ __ZN3xpc19dyn_cast_or_defaultERKNS_6objectEl
+ __ZN8defaults7bbtrace17resetModeOnAPBootEv
+ __ZN9LogDumpDB7clearDBEv
+ __ZNK12HealthModule17getShutdownStagesEv
+ __ZNK12HealthModule35getFailureCountInHealthEventDB_syncEv
+ __ZNK12HealthModule37findMostRecentBarrierHealthEvent_syncEv
+ __ZNK12HealthModule42sendUserNotificationForCellularDiagnosticsEv
+ __ZNK12HealthModule56checkFailuresAgainstThresholdAndEraseEFSAccordingly_syncEv
+ __ZNK12HealthModule7getNameEv
+ __ZNK13HealthEventDB15getHealthEventsEv
+ __ZNK3ctu2cf11map_adapter19copyCFDictionaryRefEPK10__CFString
+ __ZNSt11logic_errorC2ERKS_
+ __ZNSt12length_errorD2Ev
+ __ZTI12HealthModule
+ __ZTI13BasebandStats
+ __ZTI13HealthEventDB
+ __ZTI15CommCenterStats
+ __ZTI15DeviceHistoryDB
+ __ZTS12HealthModule
+ __ZTS13BasebandStats
+ __ZTS13HealthEventDB
+ __ZTS15CommCenterStats
+ __ZTS15DeviceHistoryDB
+ __ZTV12HealthModule
+ __ZTV13BasebandStats
+ __ZTV13HealthEventDB
+ __ZTV15CommCenterStats
+ __ZTV15DeviceHistoryDB
+ __ZThn48_N12HealthModuleD0Ev
+ __ZThn48_N12HealthModuleD1Ev
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationDefaultButtonTitleKey
- __ZN3abm9kKeyStatsE
CStrings:
+ "#D     %!s(MISSING)"
+ "#D Adding health event: %!s(MISSING)"
+ "#D Enumerating HealthEvents to be written to disk:"
+ "#D HealthEvents dictionary representation to be written to disk: %!@(MISSING)"
+ "#I %!s(MISSING) detected"
+ "#I Baseband ping timer already running"
+ "#I Broadcasting %!s(MISSING)"
+ "#I Canceling baseband ping timer"
+ "#I Cleaning up health event db due to change in hardware model"
+ "#I Cleaning up log dump db due to change in hardware model"
+ "#I Empty info passed"
+ "#I Found preliminary barrier event: %!s(MISSING)"
+ "#I Health DB is cleared"
+ "#I Log Dump DB is cleared"
+ "#I Pinging baseband to verify it is healthy"
+ "#I Simulated notification: %!s(MISSING)"
+ "#I Starting %!u(MISSING) sec timer before pinging baseband"
+ "#I Submitting Stats of soft reset time"
+ "#I Successfully received ping response from baseband (firmware version is %!s(MISSING))"
+ "#I Total health failure count reached EFS erase threshold (%!d(MISSING))%!s(MISSING)"
+ "#I Triggering stackshot"
+ "#I Triggering stackshot  -- done"
+ "#I blocking reset until user signals"
+ "#I boot failure count: %!l(MISSING)d, ping failure count: %!l(MISSING)d"
+ ", but EFS erase is not supported"
+ ", reason "
+ "/private/var/wireless/Library/Preferences/com.apple.AppleBasebandManager.Statistics.plist"
+ "; requesting EFS erase"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1209"
+ "AppleBasebandServices_Manager-1209"
+ "BB stats is empty"
+ "Baseband Hard-Reset: "
+ "Baseband HealthModule Ping Timer"
+ "Capability %!s(MISSING) returning overridden value"
+ "CellularIssue"
+ "CommandGetHealthStats"
+ "CommandUpdateBBBootStats"
+ "DeviceHistroyDB"
+ "Failed to create AppleBasebandManager instance"
+ "Failed to create dictionary to collect health info"
+ "Failed to get boot session uuid, error: %!s(MISSING)"
+ "HealthEventDB"
+ "HealthEventTimes"
+ "HealthEventTypes"
+ "Incompatible Baseband firmware."
+ "KeyBasebandStats"
+ "KeyBasebandUpTime"
+ "KeyCommCenterStats"
+ "KeyCommCenterStatsLastUpTime"
+ "KeyCommCenterStatsLaunchCount"
+ "KeyCommCenterStatsUpTime"
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "OK"
+ "PANIC: %!s(MISSING)"
+ "ResetInfoReasonRegexPattern"
+ "ResetInfoReasonRegexPatternMask"
+ "ResetInfoRegexPatterns"
+ "ServiceManager sleep timeout"
+ "ServiceManager wake timeout"
+ "Triggering stackshot, goes with "
+ "Unexpected behavior may occur. Please upgrade to a newer firmware."
+ "Unsupported ABM profile, check your plist!"
+ "circular_buffer"
+ "com.apple.telephony.capabilities"
+ "failed to init %!s(MISSING) from disk"
+ "health.mod"
+ "kern.bootsessionuuid"
- "AppleBasebandManager-AppleBasebandServices_Manager-1183"
- "AppleBasebandServices_Manager-1183"
- "Default pattern masks will be used"

```
