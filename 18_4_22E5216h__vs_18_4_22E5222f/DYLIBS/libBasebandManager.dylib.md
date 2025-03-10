## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1248.0.0.0.0
-  __TEXT.__text: 0x200d18
-  __TEXT.__auth_stubs: 0x3300
-  __TEXT.__init_offsets: 0x144
+1249.1.0.0.0
+  __TEXT.__text: 0x1fc204
+  __TEXT.__auth_stubs: 0x3240
+  __TEXT.__init_offsets: 0x134
   __TEXT.__objc_methlist: 0x46c
-  __TEXT.__const: 0xcdeb
-  __TEXT.__gcc_except_tab: 0x32cb8
-  __TEXT.__cstring: 0x7139
-  __TEXT.__oslogstring: 0xb4ae
-  __TEXT.__unwind_info: 0x9b20
+  __TEXT.__const: 0xcd1b
+  __TEXT.__gcc_except_tab: 0x321e4
+  __TEXT.__cstring: 0x6ef7
+  __TEXT.__oslogstring: 0xb303
+  __TEXT.__unwind_info: 0x99f0
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
   __TEXT.__objc_methtype: 0x1753
   __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0x2140
-  __DATA_CONST.__const: 0x1f10
+  __DATA_CONST.__got: 0x20e8
+  __DATA_CONST.__const: 0x1e90
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x568
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1990
-  __AUTH_CONST.__const: 0x10128
-  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__auth_got: 0x1930
+  __AUTH_CONST.__const: 0x10058
+  __AUTH_CONST.__cfstring: 0x6c0
   __AUTH_CONST.__objc_const: 0x918
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x5e8
+  __DATA.__data: 0x5a0
   __DATA.__bss: 0x4c8
   __DATA.__common: 0x21
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x550
-  __DATA_DIRTY.__common: 0xc8
-  __DATA_DIRTY.__bss: 0x23a
+  __DATA_DIRTY.__data: 0x4f8
+  __DATA_DIRTY.__common: 0xc0
+  __DATA_DIRTY.__bss: 0x20a
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5957
-  Symbols:   8741
-  CStrings:  2523
+  Functions: 5936
+  Symbols:   8694
+  CStrings:  2496
 
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
+ "AppleBasebandManager-AppleBasebandServices_Manager-1249.1"
+ "AppleBasebandServices_Manager-1249.1"
+ "Default pattern masks will be used"
- "#D     %s"
- "#D Enumerating HealthEvents to be written to disk:"
- "#D HealthEvents dictionary representation to be written to disk: %@"
- "#I Simulated notification: %s"
- "#I Triggering stackshot"
- "#I Triggering stackshot  -- done"
- "#I blocking reset until user signals"
- ", reason "
- "-l 0xffffffff -v 99 -N"
- "AppleBasebandManager-AppleBasebandServices_Manager-1248"
- "AppleBasebandServices_Manager-1248"
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
