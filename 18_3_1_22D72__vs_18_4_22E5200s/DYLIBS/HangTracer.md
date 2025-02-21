## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

```diff

-331.3.0.0.0
-  __TEXT.__text: 0xee1c
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x7e4
+352.0.0.0.0
+  __TEXT.__text: 0xfde0
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x808
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x3722
-  __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__oslogstring: 0x1e4e
-  __TEXT.__unwind_info: 0x330
+  __TEXT.__cstring: 0x3866
+  __TEXT.__gcc_except_tab: 0x1a8
+  __TEXT.__oslogstring: 0x2011
+  __TEXT.__unwind_info: 0x418
   __TEXT.__objc_classname: 0x37
-  __TEXT.__objc_methname: 0x316d
+  __TEXT.__objc_methname: 0x32b4
   __TEXT.__objc_methtype: 0x67d
   __TEXT.__objc_stubs: 0xd60
   __DATA_CONST.__got: 0x130
-  __DATA_CONST.__const: 0x1460
+  __DATA_CONST.__const: 0x13b8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x760
+  __DATA_CONST.__objc_selrefs: 0x778
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_got: 0x470
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x49a0
-  __AUTH_CONST.__objc_const: 0x15f8
+  __AUTH_CONST.__cfstring: 0x4b00
+  __AUTH_CONST.__objc_const: 0x1688
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0x1ac
+  __DATA.__objc_ivar: 0x1b8
   __DATA.__data: 0x1a8
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0x78
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0xf0
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 375
-  Symbols:   834
-  CStrings:  1274
+  Functions: 435
+  Symbols:   913
+  CStrings:  1301
 
Symbols:
+ _HT_MOBILE_CRASH_REPORTER_RETIRED_DIRECTORY
+ __HTBeginNonResponsiveAssertion
+ __os_log_error_impl
+ _kHTPrefsAugmentSentryTailspinWithSignposts
+ _kHTPrefsConsecutiveHangWaitTimeoutDurationMSec
+ _kHTPrefsPrefixWBClientHangEnablement
+ _kPDSEWBClientHangKillSwitch
+ _kPDSEWBClientHangPeriodDays
+ _kPDSEWBClientHangTimeoutTimestampSec
+ _kWBClientHangEnabled
- _kHTPrefsCollectOSSignpostsDeferred
CStrings:
+ "%s: event->startTime is greater than endTime, shared memory is most likely corrupted."
+ "%s: nil event passed"
+ "/var/mobile/Library/Logs/CrashReporter/Retired/"
+ "CPU Limit"
+ "HTInitializeHangTracerMonitor: XPC_TYPE_ERR for appConnection: %s"
+ "HangTracerConsecutiveHangWaitTimeoutDuration"
+ "PDSEPrefWBClientHangKillSwitch"
+ "PDSEPrefWBClientHangPeriodDays"
+ "PDSEWBClientHang"
+ "PDSEWBClientHangTimeoutTimestampSec"
+ "Self Restrict"
+ "TB,R,V_pdseWBClientHangKillSwitch"
+ "TB,R,V_shouldAugmentSentryTailspinWithSignposts"
+ "TQ,R,V_consecutiveHangWaitTimeoutDurationMSec"
+ "Ti,R,V_pdseWBClientHangPeriodDays"
+ "WBClientHangEnable"
+ "_consecutiveHangWaitTimeoutDurationMSec"
+ "_pdseWBClientHangKillSwitch"
+ "_pdseWBClientHangPeriodDays"
+ "_shouldAugmentSentryTailspinWithSignposts"
+ "checkForHangWithUserMovedAwayAndRecentAssertions"
+ "consecutiveHangWaitTimeoutDurationMSec"
+ "cpu limit"
+ "event->bundleID has been corrupted, final char in array is not \\0. bundleID: %s"
+ "event->serviceName has been corrupted, final char in array is not \\0. serviceName: %s"
+ "hangEvent->bundleID has been corrupted, final char in array is not \\0. bundleID: %s"
+ "hangEvent->serviceName has been corrupted, final char in array is not \\0. serviceName: %s"
+ "pdseWBClientHangKillSwitch"
+ "pdseWBClientHangPeriodDays"
+ "self restrict"
+ "shouldAugmentSentryTailspinWithSignposts"
+ "\xf0\xf0A!&!"
- "HTInitializeHangTracerMonitor: XPC_TYPE_ERR for appConnection"
- "TB,R,V_shouldCollectOSSignpostsDeferred"
- "_shouldCollectOSSignpostsDeferred"
- "shouldCollectOSSignpostsDeferred"
- "\xf0\xf0A\x11&!"

```
