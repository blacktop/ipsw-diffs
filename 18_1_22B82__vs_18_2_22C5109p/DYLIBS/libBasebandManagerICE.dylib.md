## libBasebandManagerICE.dylib

> `/usr/lib/libBasebandManagerICE.dylib`

```diff

-1183.0.0.0.0
-  __TEXT.__text: 0x1eb84c
-  __TEXT.__auth_stubs: 0x3160
-  __TEXT.__init_offsets: 0x114
-  __TEXT.__objc_methlist: 0x238
-  __TEXT.__const: 0xc5c7
-  __TEXT.__gcc_except_tab: 0x2f6d0
-  __TEXT.__oslogstring: 0xa532
-  __TEXT.__cstring: 0x69c3
-  __TEXT.__unwind_info: 0x8fd0
-  __TEXT.__objc_classname: 0xdb
-  __TEXT.__objc_methname: 0x10e9
-  __TEXT.__objc_methtype: 0x170a
-  __TEXT.__objc_stubs: 0xf00
-  __DATA_CONST.__got: 0x1ff8
-  __DATA_CONST.__const: 0x1a30
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x20
+1209.0.0.0.0
+  __TEXT.__text: 0x1f9280
+  __TEXT.__auth_stubs: 0x3240
+  __TEXT.__init_offsets: 0x138
+  __TEXT.__objc_methlist: 0x270
+  __TEXT.__const: 0xcbd7
+  __TEXT.__gcc_except_tab: 0x30e14
+  __TEXT.__oslogstring: 0xab79
+  __TEXT.__cstring: 0x6ccf
+  __TEXT.__unwind_info: 0x93d8
+  __TEXT.__objc_classname: 0x109
+  __TEXT.__objc_methname: 0x1187
+  __TEXT.__objc_methtype: 0x1853
+  __TEXT.__objc_stubs: 0xfa0
+  __DATA_CONST.__got: 0x2098
+  __DATA_CONST.__const: 0x1aa8
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x440
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x18c0
-  __AUTH_CONST.__const: 0xf9d8
-  __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0xb08
+  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_superrefs: 0x20
+  __AUTH_CONST.__auth_got: 0x1930
+  __AUTH_CONST.__const: 0xffe0
+  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__objc_const: 0xcc0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0x558
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x40
+  __DATA.__data: 0x658
   __DATA.__common: 0x29
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x450
-  __DATA_DIRTY.__common: 0xb0
-  __DATA_DIRTY.__bss: 0x200
+  __DATA_DIRTY.__data: 0x4a8
+  __DATA_DIRTY.__common: 0xb8
+  __DATA_DIRTY.__bss: 0x230
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
+  - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5610
-  Symbols:   8025
-  CStrings:  2319
+  Functions: 5735
+  Symbols:   8212
+  CStrings:  2399
 
Symbols:
+ _CFUserNotificationCreate
+ _CFUserNotificationDisplayNotice
+ _CFUserNotificationReceiveResponse
+ _OBJC_CLASS_$_CXCallObserver
+ _OBJC_CLASS_$_VoIPCallObserverImpl
+ _OBJC_METACLASS_$_VoIPCallObserverImpl
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyUtilTriggerNMI
+ _TelephonyUtilWriteStackshot
+ __ZGVN3ctu9SingletonI15DeviceHistoryDBS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN10BootModule30reportStatisticsSoftReset_syncEv
+ __ZN10OBDManager16registerCallbackEN8dispatch8callbackIU13block_pointerFvN3sar8OBDStateENS2_10TunerStateEEEE
+ __ZN12capabilities3abs17shouldBlockResetsEv
+ __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
+ __ZN13BasebandStats11updateStatsEN3xpc4dictE
+ __ZN13BasebandStats12initFromDiskEv
+ __ZN13BasebandStats23getCurrentBasebandStatsEv
+ __ZN13BasebandStats8getStatsEv
+ __ZN13HealthEventDB13getHealthInfoEv
+ __ZN13HealthEventDB15updateBootStatsEN3xpc4dictE
+ __ZN13HealthEventDB7clearDBEv
+ __ZN15CommCenterStats11updateStatsEN3xpc4dictE
+ __ZN15CommCenterStats12initFromDiskEv
+ __ZN15CommCenterStats8getStatsEv
+ __ZN15DeviceHistoryDB12commitToDiskEv
+ __ZN15DeviceHistoryDB12initFromDiskEv
+ __ZN15DeviceHistoryDB16addDeviceHistoryE18_DeviceHistoryItem
+ __ZN15DeviceHistoryDB7getNameEv
+ __ZN15DeviceHistoryDBC1Ev
+ __ZN15DeviceHistoryDBC2Ev
+ __ZN16VoIPCallDelegate6createEN8dispatch5queueENSt3__18functionIFvbbPKcEEE
+ __ZN16VoIPCallDelegateC1EN8dispatch5queueENSt3__18functionIFvbbPKcEEE
+ __ZN16VoIPCallDelegateC2EN8dispatch5queueENSt3__18functionIFvbbPKcEEE
+ __ZN3abm17kKeyBasebandStatsE
+ __ZN3abm18kHealthEventDBNameE
+ __ZN3abm18kKeyBasebandUpTimeE
+ __ZN3abm18kLogVersionHistoryE
+ __ZN3abm19kKeyCommCenterStatsE
+ __ZN3abm20kKeyHealthEventTimesE
+ __ZN3abm20kKeyHealthEventTypesE
+ __ZN3abm22kCommandGetHealthStatsE
+ __ZN3abm23KEventDeviceInfoChangedE
+ __ZN3abm23kEventSystemInfoChangedE
+ __ZN3abm25kCommandUpdateBBBootStatsE
+ __ZN3abm25kKeyCommCenterStatsUpTimeE
+ __ZN3abm26kKeyTraceResetModeOnAPBootE
+ __ZN3abm27kCommandBasebandAllowFSSyncE
+ __ZN3abm27kKeyStatsBootHardResetCountE
+ __ZN3abm27kKeyStatsBootSoftResetCountE
+ __ZN3abm29kCommandBasebandPreventFSSyncE
+ __ZN3abm29kKeyCommCenterStatsLastUpTimeE
+ __ZN3abm30kKeyCommCenterStatsLaunchCountE
+ __ZN3abm32kEventSystemInfoOSVersionChangedE
+ __ZN3abm34kEventSystemInfoFirmwareSideLoadedE
+ __ZN3abm36kEventSystemInfoHardwareModelChangedE
+ __ZN3ctu5power7manager20simulateNotificationEjb
+ __ZN3ctu9SingletonI15DeviceHistoryDBS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN3sar8toStringENS_10TunerStateE
+ __ZN3sar8toStringENS_8OBDStateE
+ __ZN3sys18isFWVersionChangedERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
+ __ZN3sys18isOSVersionChangedEv
+ __ZN3sys22isHardwareModelChangedEv
+ __ZN3sys25getCurrentBootSessionUUIDEv
+ __ZN8defaults7bbtrace17resetModeOnAPBootEv
+ __ZN9LogDumpDB7clearDBEv
+ __ZN9SARModule17processCallStatusEb
+ __ZN9SARModule32initializeVoIPCallDetection_syncEv
+ __ZTI13BasebandStats
+ __ZTI15CommCenterStats
+ __ZTI15DeviceHistoryDB
+ __ZTS13BasebandStats
+ __ZTS15CommCenterStats
+ __ZTS15DeviceHistoryDB
+ __ZTV13BasebandStats
+ __ZTV15CommCenterStats
+ __ZTV15DeviceHistoryDB
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationDefaultButtonTitleKey
- __ZN10OBDManager16registerCallbackEN8dispatch8callbackIU13block_pointerFvNS_8OBDStateENS_10TunerStateEEEE
- __ZN10OBDManager8toStringENS_10TunerStateE
- __ZN10OBDManager8toStringENS_8OBDStateE
- __ZN3abm16kCommandGetStatsE
CStrings:
+ "#D     %!s(MISSING)"
+ "#D Enumerating HealthEvents to be written to disk:"
+ "#D HealthEvents dictionary representation to be written to disk: %!@(MISSING)"
+ "#D No matching condition to check FT Call status"
+ "#I %!s(MISSING) detected"
+ "#I %!s(MISSING): callStarting: %!s(MISSING), callActive: %!s(MISSING)"
+ "#I Broadcasting %!s(MISSING)"
+ "#I Call state is same as before. No update the HSAR Voice Call: %!s(MISSING)"
+ "#I Cleaning up health event db due to change in hardware model"
+ "#I Cleaning up log dump db due to change in hardware model"
+ "#I Empty info passed"
+ "#I Get property for \"%!s(MISSING)\" command is not supported"
+ "#I Getting call state"
+ "#I Health DB is cleared"
+ "#I Initializing FT Call Detection"
+ "#I Log Dump DB is cleared"
+ "#I RFS status during request: Remote=%!s(MISSING) Ready=%!s(MISSING) Prevent=%!s(MISSING)"
+ "#I RFS sync is not allowed"
+ "#I Request to allow rfs sync"
+ "#I Request to prevent rfs sync"
+ "#I Setting HSAR Voice Call: %!s(MISSING)"
+ "#I Simulated notification: %!s(MISSING)"
+ "#I Submitting Stats of soft reset time"
+ "#I Succeeded getting call state: %!s(MISSING)"
+ "#I Triggering stackshot"
+ "#I Triggering stackshot  -- done"
+ "#I blocking reset until user signals"
+ "#I cellular transmit state: %!s(MISSING)"
+ "(1) call connected: %!{(MISSING)BOOL}d, call ended: %!{(MISSING)BOOL}d, fVoIPCallStarting: %!{(MISSING)BOOL}d, fVoIPCallActive: %!{(MISSING)BOOL}d"
+ "(2) call connected: %!{(MISSING)BOOL}d, call ended: %!{(MISSING)BOOL}d, fVoIPCallStarting: %!{(MISSING)BOOL}d, fVoIPCallActive: %!{(MISSING)BOOL}d"
+ ", reason "
+ "-l 0xffffffff -v 99 -N"
+ "/private/var/wireless/Library/Preferences/com.apple.AppleBasebandManager.Statistics.plist"
+ "@\"CXCallObserver\""
+ "@56@0:8{function<void (bool, bool, const char *)>={__value_func<void (bool, bool, const char *)>={type=[24C]}^v}}16^{dispatch_queue_s=}48"
+ "A"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1209"
+ "AppleBasebandServices_Manager-1209"
+ "B"
+ "BB stats is empty"
+ "Baseband Firmware Not Found"
+ "Baseband Hard-Reset: "
+ "CXCallObserverDelegate"
+ "Call observer created"
+ "Capability %!s(MISSING) returning overridden value"
+ "CommandGetHealthStats"
+ "CommandUpdateBBBootStats"
+ "DeviceHistroyDB"
+ "Did you forget to check update baseband or set permissions if you used a custom build?"
+ "Failed to create AppleBasebandManager instance"
+ "Failed to create Call observer from CallKit"
+ "Failed to create dictionary to collect health info"
+ "Failed to get boot session uuid, error: %!s(MISSING)"
+ "Failed to get call state!"
+ "Failed to set call state!"
+ "Incompatible Baseband firmware."
+ "KeyBasebandStats"
+ "KeyBasebandUpTime"
+ "KeyCommCenterStats"
+ "KeyCommCenterStatsLastUpTime"
+ "KeyCommCenterStatsLaunchCount"
+ "KeyCommCenterStatsUpTime"
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "No provider ID. Reject this call"
+ "OK"
+ "PANIC: %!s(MISSING)"
+ "Provider ID: %!@(MISSING)"
+ "ResetInfoReasonRegexPattern"
+ "ResetInfoReasonRegexPatternMask"
+ "ResetInfoRegexPatterns"
+ "ServiceManager sleep timeout"
+ "ServiceManager wake timeout"
+ "Triggering stackshot, goes with "
+ "Unexpected behavior may occur. Please upgrade to a newer firmware."
+ "Unsupported ABM profile, check your plist!"
+ "VoIPCallObserverImpl"
+ "callObserver:callChanged:"
+ "com.apple.telephony.capabilities"
+ "fCallObserver"
+ "fVoIPCallActive"
+ "fVoIPCallStarting"
+ "failed to init %!s(MISSING) from disk"
+ "hasConnected"
+ "hasEnded"
+ "initWithCallback:queue:"
+ "kern.bootsessionuuid"
+ "providerIdentifier"
+ "setDelegate:queue:"
+ "v24@?0B8B12r*16"
+ "v32@0:8@\"CXCallObserver\"16@\"CXCall\"24"
+ "{function<void (bool, bool, const char *)>=\"__f_\"{__value_func<void (bool, bool, const char *)>=\"__buf_\"{type=\"__lx\"[24C]}\"__f_\"^v}}"
- "#I RFS status during request: Remote=%!s(MISSING) Ready=%!s(MISSING)"
- "-l 0xffffffdf -v 0 -N"
- "AppleBasebandManager-AppleBasebandServices_Manager-1183"
- "AppleBasebandServices_Manager-1183"
- "BODY"
- "Default pattern masks will be used"
- "FREE"
- "Failed to get data."
- "Failed: Stats get command works only abm stats. %!s(MISSING) is not recognized."
- "HEAD"
- "NONFREE"

```
