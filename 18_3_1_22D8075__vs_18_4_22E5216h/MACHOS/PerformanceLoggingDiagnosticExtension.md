## PerformanceLoggingDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/PerformanceLoggingDiagnosticExtension.appex/PerformanceLoggingDiagnosticExtension`

```diff

-331.3.0.0.0
-  __TEXT.__text: 0x7b78
-  __TEXT.__auth_stubs: 0x500
+354.2.0.0.0
+  __TEXT.__text: 0x8108
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x83c
+  __TEXT.__objc_methlist: 0x85c
   __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x110b
+  __TEXT.__cstring: 0x1176
   __TEXT.__oslogstring: 0xba0
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__objc_methname: 0x2fff
+  __TEXT.__objc_methname: 0x3146
   __TEXT.__objc_classname: 0x6e
   __TEXT.__objc_methtype: 0x64c
-  __TEXT.__unwind_info: 0x150
-  __DATA_CONST.__auth_got: 0x290
+  __TEXT.__unwind_info: 0x1a0
+  __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x508
-  __DATA_CONST.__cfstring: 0x12c0
+  __DATA_CONST.__const: 0x520
+  __DATA_CONST.__cfstring: 0x1320
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x15d0
-  __DATA.__objc_selrefs: 0x708
-  __DATA.__objc_ivar: 0x19c
+  __DATA.__objc_const: 0x1660
+  __DATA.__objc_selrefs: 0x720
+  __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x28
   __DATA.__bss: 0x80

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 202
-  Symbols:   257
-  CStrings:  710
+  Functions: 238
+  Symbols:   262
+  CStrings:  722
 
Symbols:
+ __os_log_error_impl
+ _kHTPrefsAugmentSentryTailspinWithSignposts
+ _kHTPrefsConsecutiveHangWaitTimeoutDurationMSec
+ _kPDSEWBClientHangKillSwitch
+ _kPDSEWBClientHangPeriodDays
+ _objc_release_x28
- _kHTPrefsCollectOSSignpostsDeferred
CStrings:
+ "HangTracerConsecutiveHangWaitTimeoutDuration"
+ "PDSEPrefWBClientHangKillSwitch"
+ "PDSEPrefWBClientHangPeriodDays"
+ "TB,R,V_pdseWBClientHangKillSwitch"
+ "TB,R,V_shouldAugmentSentryTailspinWithSignposts"
+ "TQ,R,V_consecutiveHangWaitTimeoutDurationMSec"
+ "Ti,R,V_pdseWBClientHangPeriodDays"
+ "_consecutiveHangWaitTimeoutDurationMSec"
+ "_pdseWBClientHangKillSwitch"
+ "_pdseWBClientHangPeriodDays"
+ "_shouldAugmentSentryTailspinWithSignposts"
+ "consecutiveHangWaitTimeoutDurationMSec"
+ "pdseWBClientHangKillSwitch"
+ "pdseWBClientHangPeriodDays"
+ "shouldAugmentSentryTailspinWithSignposts"
+ "\xf0\xf0A!&!"
- "TB,R,V_shouldCollectOSSignpostsDeferred"
- "_shouldCollectOSSignpostsDeferred"
- "shouldCollectOSSignpostsDeferred"
- "\xf0\xf0A\x11&!"

```
