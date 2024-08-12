## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1179.0.0.0.0
-  __TEXT.__text: 0x1f674c
-  __TEXT.__auth_stubs: 0x3210
-  __TEXT.__init_offsets: 0x11c
+1180.0.0.0.0
+  __TEXT.__text: 0x1f1a4c
+  __TEXT.__auth_stubs: 0x3150
+  __TEXT.__init_offsets: 0x10c
   __TEXT.__objc_methlist: 0x238
-  __TEXT.__gcc_except_tab: 0x303e8
-  __TEXT.__const: 0xc78b
-  __TEXT.__cstring: 0x6e0f
-  __TEXT.__oslogstring: 0xa83d
-  __TEXT.__unwind_info: 0x9198
+  __TEXT.__gcc_except_tab: 0x2f930
+  __TEXT.__const: 0xc68b
+  __TEXT.__cstring: 0x6bc9
+  __TEXT.__oslogstring: 0xa692
+  __TEXT.__unwind_info: 0x9068
   __TEXT.__objc_classname: 0xdb
   __TEXT.__objc_methname: 0x10e9
   __TEXT.__objc_methtype: 0x170a
   __TEXT.__objc_stubs: 0xf00
-  __DATA_CONST.__got: 0x2008
-  __DATA_CONST.__const: 0x1d98
+  __DATA_CONST.__got: 0x1fb0
+  __DATA_CONST.__const: 0x1d18
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x440
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x1918
-  __AUTH_CONST.__const: 0xf970
-  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__auth_got: 0x18b8
+  __AUTH_CONST.__const: 0xf8a0
+  __AUTH_CONST.__cfstring: 0x6c0
   __AUTH_CONST.__objc_const: 0xb08
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x30
-  __DATA.__data: 0x538
+  __DATA.__data: 0x4f0
   __DATA.__bss: 0x4c8
   __DATA.__common: 0x21
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x548
-  __DATA_DIRTY.__bss: 0x21a
-  __DATA_DIRTY.__common: 0xc8
+  __DATA_DIRTY.__data: 0x4f0
+  __DATA_DIRTY.__bss: 0x1ea
+  __DATA_DIRTY.__common: 0xc0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5679
-  Symbols:   8124
-  CStrings:  2399
+  Functions: 5657
+  Symbols:   8078
+  CStrings:  2372
 
Symbols:
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
+ "-l 0xffffffdf -v 0 -N"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1180"
+ "AppleBasebandServices_Manager-1180"
+ "Default pattern masks will be used"
- "#D     %!s(MISSING)"
- "#D Enumerating HealthEvents to be written to disk:"
- "#D HealthEvents dictionary representation to be written to disk: %!@(MISSING)"
- "#I Simulated notification: %!s(MISSING)"
- "#I Triggering stackshot"
- "#I Triggering stackshot  -- done"
- "#I blocking reset until user signals"
- ", reason "
- "-l 0xffffffff -v 99 -N"
- "AppleBasebandManager-AppleBasebandServices_Manager-1179"
- "AppleBasebandServices_Manager-1179"
- "Baseband Firmware Not Found"
- "Baseband Hard-Reset: "
- "Capability %!s(MISSING) returning overridden value"
- "Did you forget to check update baseband or set permissions if you used a custom build?"
- "Incompatible Baseband firmware."
- "Invalid property type"
- "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
- "OK"
- "PANIC: %!s(MISSING)"
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
