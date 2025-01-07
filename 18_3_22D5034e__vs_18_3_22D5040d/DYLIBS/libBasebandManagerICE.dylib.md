## libBasebandManagerICE.dylib

> `/usr/lib/libBasebandManagerICE.dylib`

```diff

-1218.0.0.0.0
-  __TEXT.__text: 0x1fbfb8
-  __TEXT.__auth_stubs: 0x32a0
-  __TEXT.__init_offsets: 0x138
+1219.0.0.0.0
+  __TEXT.__text: 0x1f9dd8
+  __TEXT.__auth_stubs: 0x31f0
+  __TEXT.__init_offsets: 0x12c
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__const: 0xcbf7
-  __TEXT.__gcc_except_tab: 0x31408
-  __TEXT.__oslogstring: 0xad1b
-  __TEXT.__cstring: 0x6d4c
-  __TEXT.__unwind_info: 0x9458
+  __TEXT.__const: 0xcb07
+  __TEXT.__gcc_except_tab: 0x30e44
+  __TEXT.__oslogstring: 0xad16
+  __TEXT.__cstring: 0x6b7d
+  __TEXT.__unwind_info: 0x9378
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
   __TEXT.__objc_methtype: 0x1853
   __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0x20b0
-  __DATA_CONST.__const: 0x1ac8
+  __DATA_CONST.__got: 0x2080
+  __DATA_CONST.__const: 0x1aa8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1960
-  __AUTH_CONST.__const: 0x10010
-  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__auth_got: 0x1908
+  __AUTH_CONST.__const: 0x10000
+  __AUTH_CONST.__cfstring: 0x760
   __AUTH_CONST.__objc_const: 0xcc0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x600
+  __DATA.__data: 0x5b8
   __DATA.__common: 0x29
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x500
-  __DATA_DIRTY.__common: 0xb8
-  __DATA_DIRTY.__bss: 0x22a
+  __DATA_DIRTY.__data: 0x4a8
+  __DATA_DIRTY.__common: 0xb0
+  __DATA_DIRTY.__bss: 0x1fa
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5748
-  Symbols:   8235
-  CStrings:  2413
+  Functions: 5740
+  Symbols:   8208
+  CStrings:  2399
 
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
- __ZN12capabilities3abs17shouldBlockResetsEv
- __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
- __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
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
- "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
- "OK"
- "PANIC: %s"
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
