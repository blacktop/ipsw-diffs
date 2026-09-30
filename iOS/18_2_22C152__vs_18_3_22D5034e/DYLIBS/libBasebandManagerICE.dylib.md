## libBasebandManagerICE.dylib

> `/usr/lib/libBasebandManagerICE.dylib`

```diff

-1211.0.0.0.0
-  __TEXT.__text: 0x1f7158
-  __TEXT.__auth_stubs: 0x3180
-  __TEXT.__init_offsets: 0x12c
+1218.0.0.0.0
+  __TEXT.__text: 0x1fbfb8
+  __TEXT.__auth_stubs: 0x32a0
+  __TEXT.__init_offsets: 0x138
   __TEXT.__objc_methlist: 0x270
-  __TEXT.__const: 0xcae7
-  __TEXT.__gcc_except_tab: 0x309b0
-  __TEXT.__oslogstring: 0xaade
-  __TEXT.__cstring: 0x6b1a
-  __TEXT.__unwind_info: 0x9320
+  __TEXT.__const: 0xcbf7
+  __TEXT.__gcc_except_tab: 0x31408
+  __TEXT.__oslogstring: 0xad1b
+  __TEXT.__cstring: 0x6d4c
+  __TEXT.__unwind_info: 0x9458
   __TEXT.__objc_classname: 0x109
   __TEXT.__objc_methname: 0x1187
   __TEXT.__objc_methtype: 0x1853
   __TEXT.__objc_stubs: 0xfa0
-  __DATA_CONST.__got: 0x2068
-  __DATA_CONST.__const: 0x1ab0
+  __DATA_CONST.__got: 0x20b0
+  __DATA_CONST.__const: 0x1ac8
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x470
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x18d0
-  __AUTH_CONST.__const: 0xff70
-  __AUTH_CONST.__cfstring: 0x760
+  __AUTH_CONST.__auth_got: 0x1960
+  __AUTH_CONST.__const: 0x10010
+  __AUTH_CONST.__cfstring: 0x7a0
   __AUTH_CONST.__objc_const: 0xcc0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x5b8
+  __DATA.__data: 0x600
   __DATA.__common: 0x29
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__data: 0x4a8
-  __DATA_DIRTY.__common: 0xb0
-  __DATA_DIRTY.__bss: 0x1fa
+  __DATA_DIRTY.__data: 0x500
+  __DATA_DIRTY.__common: 0xb8
+  __DATA_DIRTY.__bss: 0x22a
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 5728
-  Symbols:   8186
-  CStrings:  2381
+  Functions: 5748
+  Symbols:   8235
+  CStrings:  2413
 
Symbols:
+ _CFUserNotificationCreate
+ _CFUserNotificationDisplayNotice
+ _CFUserNotificationReceiveResponse
+ _TelephonyBasebandWatchdogStartWithStackshot
+ _TelephonyUtilTriggerNMI
+ _TelephonyUtilWriteStackshot
+ __ZGVN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN12capabilities3abs17shouldBlockResetsEv
+ __ZN12capabilities3abs26shouldPanicOnBasebandResetEv
+ __ZN12capabilities3abs27kKeySupportsCMHandDetectionE
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
+ "No Action for dumping log"
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "OK"
+ "PANIC: %s"
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
