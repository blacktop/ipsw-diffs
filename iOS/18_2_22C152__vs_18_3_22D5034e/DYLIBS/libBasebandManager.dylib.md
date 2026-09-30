## libBasebandManager.dylib

> `/usr/lib/libBasebandManager.dylib`

```diff

-1211.0.0.0.0
-  __TEXT.__text: 0x1fd18c
-  __TEXT.__auth_stubs: 0x3170
-  __TEXT.__init_offsets: 0x124
+1218.0.0.0.0
+  __TEXT.__text: 0x203f78
+  __TEXT.__auth_stubs: 0x3290
+  __TEXT.__init_offsets: 0x134
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__gcc_except_tab: 0x30bd8
-  __TEXT.__const: 0xcb7b
-  __TEXT.__cstring: 0x6d20
-  __TEXT.__oslogstring: 0xac5b
-  __TEXT.__unwind_info: 0x93b8
+  __TEXT.__gcc_except_tab: 0x31a9c
+  __TEXT.__const: 0xcc9b
+  __TEXT.__cstring: 0x6fbd
+  __TEXT.__oslogstring: 0xaeae
+  __TEXT.__unwind_info: 0x9528
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
   __TEXT.__objc_methtype: 0x1853
   __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0x2020
-  __DATA_CONST.__const: 0x1d98
+  __DATA_CONST.__got: 0x2090
+  __DATA_CONST.__const: 0x1e10
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x18c8
-  __AUTH_CONST.__const: 0xfe08
-  __AUTH_CONST.__cfstring: 0x6c0
+  __AUTH_CONST.__auth_got: 0x1958
+  __AUTH_CONST.__const: 0xff08
+  __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0xcc0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x5a0
+  __DATA.__data: 0x5e8
   __DATA.__bss: 0x4c8
   __DATA.__common: 0x21
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x4f8
-  __DATA_DIRTY.__bss: 0x1ea
-  __DATA_DIRTY.__common: 0xc0
+  __DATA_DIRTY.__data: 0x550
+  __DATA_DIRTY.__bss: 0x21a
+  __DATA_DIRTY.__common: 0xc8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5775
-  Symbols:   8239
-  CStrings:  2434
+  Functions: 5805
+  Symbols:   8302
+  CStrings:  2469
 
Symbols:
+ _CFUserNotificationCreate
+ _CFUserNotificationDisplayNotice
+ _CFUserNotificationReceiveResponse
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyUtilTriggerNMI
+ _TelephonyUtilWriteStackshot
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN10DataModule20setDataProperty_syncEN3xpc4dictEN8dispatch5blockIU13block_pointerFviS1_EEE
+ __ZN12capabilities3abs17shouldBlockResetsEv
+ __ZN12capabilities3abs24kKeyDataPowerSaveEnabledE
+ __ZN12capabilities3abs26kKeyDataFlowControlEnabledE
+ __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
+ __ZN12capabilities3abs27kKeyDataAggregationProtocolE
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
+ __ZN12capabilities3abs31kKeyDataAggregationMaxSizeBytesE
+ __ZN12capabilities3abs35kKeyDataAggregationDatagramMaxCountE
+ __ZN12capabilities3abs39shouldTriggerStackshotOnShutdownTimeoutEv
+ __ZN12capabilities5trace42supportsCoredumpCrashReasonOnCustomerBuildEv
+ __ZN3abm22kCommandQueryLogDumpDBE
+ __ZN3ctu4llvm9StringRef4nposE
+ __ZN3ctu5power7manager20simulateNotificationEjb
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN3ctu9split_anyENS_4llvm9StringRefES1_
+ __ZN3sar8toStringENS_16HSARSubErrorCodeE
+ __ZN3sar8toStringENS_19AppleSARMessageTypeE
+ __ZN8defaults7bbtrace14bandwidth_mbpsEv
+ __ZN9LogDumpDB14queryLogDumpDBERN3xpc4dictE
+ __ZN9LogDumpDB9writeToDBERK9ResetInfo
+ __ZN9LogDumpDB9writeToDBERK9ResetInfoNSt3__16chrono8durationIxNS3_5ratioILl1ELl1EEEEE
+ __ZN9SARModule7dumpLogENSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEENS_16SARErrorBehaviorE
+ __ZN9SARModule8asStringENS_16SARErrorBehaviorE
+ __ZNK3ctu4llvm9StringRef4findES1_m
+ __ZNSt3__14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationDefaultButtonTitleKey
- __ZN9LogDumpDB12isDuplicatedERK9ResetInfoNSt3__16chrono8durationIxNS3_5ratioILl1ELl1EEEEE
CStrings:
+ " \t\n"
+ "#D     %s"
+ "#D Enumerating HealthEvents to be written to disk:"
+ "#D HealthEvents dictionary representation to be written to disk: %@"
+ "#I Behavior: %s"
+ "#I Detected HSAR error: %s"
+ "#I Found %s = 0x%x"
+ "#I Simulated notification: %s"
+ "#I Triggering stackshot"
+ "#I Triggering stackshot  -- done"
+ "#I We don't trigger the log dump request from the kernel driver if it is not Carrier/Internal build"
+ "#I We don't trigger the log dump request from the kernel driver in Restore Mode"
+ "#I blocking reset until user signals"
+ "#I boot failure count: %ld, baseband crash count: %ld, ping failure count: %ld"
+ ", reason "
+ "-l 0xffffffff -v 99 -N"
+ "="
+ "AppleBasebandManager-AppleBasebandServices_Manager-1218"
+ "AppleBasebandServices_Manager-1218"
+ "Baseband Firmware Not Found"
+ "Baseband Hard-Reset: "
+ "Capability %s returning overridden value"
+ "Did you forget to check update baseband or set permissions if you used a custom build?"
+ "Dump coredump along with telephony logs"
+ "Dump only telephony logs"
+ "Failed to create xpc array for querying logdump DB"
+ "Failed to create xpc dictionary for querying logdump DB"
+ "Incompatible Baseband firmware."
+ "Invalid property type"
+ "No Action for dumping log"
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "OK"
+ "PANIC: %s"
+ "QMI low power, please file radar in Purple Telephony - 1.0"
+ "ResetInfoReasonRegexPattern"
+ "ResetInfoReasonRegexPatternMask"
+ "ResetInfoRegexPatterns"
+ "ServiceManager sleep timeout"
+ "ServiceManager wake timeout"
+ "Triggering stackshot, goes with "
+ "Undefined Behavior"
+ "Unexpected behavior may occur. Please upgrade to a newer firmware."
+ "Unsupported ABM profile, check your plist!"
+ "com.apple.telephony.capabilities"
+ "hsar-error-behavior"
- "#D Not found duplicated log"
- "#I We don't trigger the coredump request from the kernel driver if it is not Carrier/Internal build"
- "#I We don't trigger the coredump request from the kernel driver in Restore Mode"
- "#I boot failure count: %ld, ping failure count: %ld"
- "-l 0xffffffdf -v 0 -N"
- "AppleBasebandManager-AppleBasebandServices_Manager-1211"
- "AppleBasebandServices_Manager-1211"
- "Default pattern masks will be used"
- "Log Dump History"
- "OCP packet error"
- "SPMI Bus error"

```
