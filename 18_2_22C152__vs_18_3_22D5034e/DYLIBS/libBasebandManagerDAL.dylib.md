## libBasebandManagerDAL.dylib

> `/usr/lib/libBasebandManagerDAL.dylib`

```diff

-1211.0.0.0.0
-  __TEXT.__text: 0x1170cc
-  __TEXT.__auth_stubs: 0x2280
-  __TEXT.__init_offsets: 0xa8
+1218.0.0.0.0
+  __TEXT.__text: 0x11ad0c
+  __TEXT.__auth_stubs: 0x2350
+  __TEXT.__init_offsets: 0xb4
   __TEXT.__objc_methlist: 0x140
-  __TEXT.__const: 0x63ff
-  __TEXT.__gcc_except_tab: 0x19e98
-  __TEXT.__oslogstring: 0x5165
-  __TEXT.__cstring: 0x2e15
-  __TEXT.__unwind_info: 0x5178
+  __TEXT.__const: 0x64e7
+  __TEXT.__gcc_except_tab: 0x1a748
+  __TEXT.__oslogstring: 0x5364
+  __TEXT.__cstring: 0x2f6b
+  __TEXT.__unwind_info: 0x5280
   __TEXT.__objc_classname: 0x68
   __TEXT.__objc_methname: 0x626
   __TEXT.__objc_methtype: 0x1389
   __TEXT.__objc_stubs: 0x500
-  __DATA_CONST.__got: 0x1120
-  __DATA_CONST.__const: 0xf18
+  __DATA_CONST.__got: 0x1160
+  __DATA_CONST.__const: 0xf30
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1150
-  __AUTH_CONST.__const: 0x89c8
-  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__auth_got: 0x11b8
+  __AUTH_CONST.__const: 0x8a68
+  __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0x658
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x1c
-  __DATA.__data: 0x6a8
-  __DATA.__common: 0x20
-  __DATA.__bss: 0x1a8
-  __DATA_DIRTY.__data: 0x78
+  __DATA.__data: 0x740
+  __DATA.__common: 0x28
+  __DATA.__bss: 0x1d8
+  __DATA_DIRTY.__data: 0x80
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3055
-  Symbols:   4424
-  CStrings:  1148
+  Functions: 3073
+  Symbols:   4464
+  CStrings:  1170
 
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
+ __ZN3ctu5power7manager20simulateNotificationEjb
+ __ZN3ctu9SingletonI21CapabilitiesOverridesS1_NS_23PthreadMutexGuardPolicyIS1_EEE9sInstanceE
+ __ZN8defaults7bbtrace14bandwidth_mbpsEv
+ __ZN9LogDumpDB14queryLogDumpDBERN3xpc4dictE
+ __ZN9LogDumpDB9writeToDBERK9ResetInfo
+ __ZN9LogDumpDB9writeToDBERK9ResetInfoNSt3__16chrono8durationIxNS3_5ratioILl1ELl1EEEEE
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _kCFUserNotificationAlertHeaderKey
+ _kCFUserNotificationAlertMessageKey
+ _kCFUserNotificationDefaultButtonTitleKey
- __ZN9LogDumpDB12isDuplicatedERK9ResetInfoNSt3__16chrono8durationIxNS3_5ratioILl1ELl1EEEEE
CStrings:
+ "#D     %s"
+ "#D Enumerating HealthEvents to be written to disk:"
+ "#D HealthEvents dictionary representation to be written to disk: %@"
+ "#I Simulated notification: %s"
+ "#I Triggering stackshot"
+ "#I Triggering stackshot  -- done"
+ "#I blocking reset until user signals"
+ "#I boot failure count: %ld, baseband crash count: %ld, ping failure count: %ld"
+ ", reason "
+ "AppleBasebandManager-AppleBasebandServices_Manager-1218"
+ "AppleBasebandServices_Manager-1218"
+ "Baseband Hard-Reset: "
+ "Capability %s returning overridden value"
+ "Failed to create xpc array for querying logdump DB"
+ "Failed to create xpc dictionary for querying logdump DB"
+ "Incompatible Baseband firmware."
+ "No ResetInfoRegexPatterns entry found in ABMProperties, so the default patterns will be used"
+ "OK"
+ "PANIC: %s"
+ "ResetInfoReasonRegexPattern"
+ "ResetInfoReasonRegexPatternMask"
+ "ResetInfoRegexPatterns"
+ "ServiceManager sleep timeout"
+ "ServiceManager wake timeout"
+ "Triggering stackshot, goes with "
+ "Unexpected behavior may occur. Please upgrade to a newer firmware."
+ "Unsupported ABM profile, check your plist!"
+ "com.apple.telephony.capabilities"
- "#D Not found duplicated log"
- "#I boot failure count: %ld, ping failure count: %ld"
- "AppleBasebandManager-AppleBasebandServices_Manager-1211"
- "AppleBasebandServices_Manager-1211"
- "Default pattern masks will be used"
- "Log Dump History"

```
