## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

 1211.0.0.0.0
-  __TEXT.__text: 0x201eac
-  __TEXT.__auth_stubs: 0x3230
-  __TEXT.__init_offsets: 0x134
+  __TEXT.__text: 0x1fd18c
+  __TEXT.__auth_stubs: 0x3170
+  __TEXT.__init_offsets: 0x124
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x316a4
-  __TEXT.__const: 0xcc6b
-  __TEXT.__cstring: 0x6f66
-  __TEXT.__oslogstring: 0xae06
-  __TEXT.__unwind_info: 0x94f0
+  __TEXT.__gcc_except_tab: 0x30bd8
+  __TEXT.__const: 0xcb7b
+  __TEXT.__cstring: 0x6d20
+  __TEXT.__oslogstring: 0xac5b
+  __TEXT.__unwind_info: 0x93b8
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
   __TEXT.__objc_methtype: 0x1853
   __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0x2078
-  __DATA_CONST.__const: 0x1e18
+  __DATA_CONST.__got: 0x2020
+  __DATA_CONST.__const: 0x1d98
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x1928
-  __AUTH_CONST.__const: 0xfed8
-  __AUTH_CONST.__cfstring: 0x700
+  __AUTH_CONST.__auth_got: 0x18c8
+  __AUTH_CONST.__const: 0xfe08
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
-  Functions: 5797
-  Symbols:   8285
-  CStrings:  2461
+  Functions: 5775
+  Symbols:   8239
+  CStrings:  2434
 
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
