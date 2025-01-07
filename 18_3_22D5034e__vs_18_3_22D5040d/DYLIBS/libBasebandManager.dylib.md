## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1218.0.0.0.0
-  __TEXT.__text: 0x203f78
-  __TEXT.__auth_stubs: 0x3290
-  __TEXT.__init_offsets: 0x134
+1219.0.0.0.0
+  __TEXT.__text: 0x1ffe0c
+  __TEXT.__auth_stubs: 0x31e0
+  __TEXT.__init_offsets: 0x124
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x31a9c
-  __TEXT.__const: 0xcc9b
-  __TEXT.__cstring: 0x6fbd
-  __TEXT.__oslogstring: 0xaeae
-  __TEXT.__unwind_info: 0x9528
+  __TEXT.__gcc_except_tab: 0x3106c
+  __TEXT.__const: 0xcbab
+  __TEXT.__cstring: 0x6d83
+  __TEXT.__oslogstring: 0xae93
+  __TEXT.__unwind_info: 0x9408
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
   __TEXT.__objc_methtype: 0x1853
   __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0x2090
-  __DATA_CONST.__const: 0x1e10
+  __DATA_CONST.__got: 0x2038
+  __DATA_CONST.__const: 0x1d90
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1958
-  __AUTH_CONST.__const: 0xff08
-  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__auth_got: 0x1900
+  __AUTH_CONST.__const: 0xfe98
+  __AUTH_CONST.__cfstring: 0x6c0
   __AUTH_CONST.__objc_const: 0xcc0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x5e8
+  __DATA.__data: 0x5a0
   __DATA.__bss: 0x4c8
   __DATA.__common: 0x21
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x550
-  __DATA_DIRTY.__bss: 0x21a
-  __DATA_DIRTY.__common: 0xc8
+  __DATA_DIRTY.__data: 0x4f8
+  __DATA_DIRTY.__bss: 0x1ea
+  __DATA_DIRTY.__common: 0xc0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5805
-  Symbols:   8302
-  CStrings:  2469
+  Functions: 5787
+  Symbols:   8261
+  CStrings:  2452
 
Symbols:
+ __ZN11WiFiManager18stopWiFiQueryTimerEv
+ __ZN11WiFiManager19startWiFiQueryTimerEv
+ __ZN7antenna13CommandDriver8toStringENS_7NVItemsE
- _CFUserNotificationCreate
- _CFUserNotificationDisplayNotice
- _CFUserNotificationReceiveResponse
- _TelephonyBasebandWatchdogStartWithStackshot
- _TelephonyUtilTriggerNMI
- _TelephonyUtilWriteStackshot
- __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
- __ZN10DataModule20setDataProperty_syncEN3xpc4dictEN8dispatch5blockIU13block_pointerFviS1_EEE
- __ZN12capabilities3abs17shouldBlockResetsEv
- __ZN12capabilities3abs24kKeyDataPowerSaveEnabledE
- __ZN12capabilities3abs26kKeyDataFlowControlEnabledE
- __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
- __ZN12capabilities3abs27kKeyDataAggregationProtocolE
- __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
- __ZN12capabilities3abs31kKeyDataAggregationMaxSizeBytesE
- __ZN12capabilities3abs35kKeyDataAggregationDatagramMaxCountE
- __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
- __ZN3ctu5power7manager20simulateNotificationEjb
- __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _kCFUserNotificationAlertHeaderKey
- _kCFUserNotificationAlertMessageKey
- _kCFUserNotificationDefaultButtonTitleKey
CStrings:
+ "#D WiFiManager: Interface Added Event"
+ "#D WiFiManager: Power Change Event"
+ "#I %s nv item is detected"
+ "#I Assuming the first attempt to query WiFi state is incorrect from WiFi Framework. So, we skip the first event."
+ "#I Getting HSAR Config from kernel"
+ "#I Performing Wifi timer-based status query"
+ "#I Succeeded getting HSAR Configuration: HSAR is %s"
+ "-l 0xffffffdf -v 0 -N"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1219"
+ "AppleBasebandServices_Manager-1219"
+ "Default pattern masks will be used"
+ "Failed to get HSAR configuration!"
+ "Failed to get NV item!"
+ "Failed to set HSAR configuration!"
+ "v16@?0B8i12"
- "#D     %s"
- "#D Enumerating HealthEvents to be written to disk:"
- "#D HealthEvents dictionary representation to be written to disk: %@"
- "#D WiFiManager Power Change Event"
- "#I Simulated notification: %s"
- "#I Triggering stackshot"
- "#I Triggering stackshot  -- done"
- "#I blocking reset until user signals"
- ", reason "
- "-l 0xffffffff -v 99 -N"
- "AppleBasebandManager-AppleBasebandServices_Manager-1218"
- "AppleBasebandServices_Manager-1218"
- "Baseband Firmware Not Found"
- "Baseband Hard-Reset: "
- "Capability %s returning overridden value"
- "Did you forget to check update baseband or set permissions if you used a custom build?"
- "Incompatible Baseband firmware."
- "Invalid property type"
- "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
- "OK"
- "PANIC: %s"
- "QMI low power, please file radar in Purple Telephony - 1.0"
- "ResetInfoReasonRegexPattern"
- "ResetInfoReasonRegexPatternMask"
- "ResetInfoRegexPatterns"
- "ServiceManager sleep timeout"
- "ServiceManager wake timeout"
- "Triggering stackshot, goes with "
- "Unexpected behavior may occur. Please upgrade to a newer firmware."
- "Unsupported ABM profile, check your plist!"
- "com.apple.telephony.capabilities"

```
