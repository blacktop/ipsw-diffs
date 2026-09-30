## logd_reporter

> `/usr/libexec/logd_reporter`

```diff

-1643.120.5.0.0
-  __TEXT.__text: 0x359c
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x100
-  __TEXT.__const: 0xa0
-  __TEXT.__objc_methname: 0x96c
-  __TEXT.__oslogstring: 0x578
-  __TEXT.__cstring: 0x47d
+1815.0.0.0.0
+  __TEXT.__text: 0x3d84
+  __TEXT.__auth_stubs: 0x500
+  __TEXT.__objc_stubs: 0xc00
+  __TEXT.__objc_methlist: 0x118
+  __TEXT.__const: 0xa8
+  __TEXT.__objc_methname: 0xa82
+  __TEXT.__oslogstring: 0x5ff
+  __TEXT.__cstring: 0x509
   __TEXT.__objc_classname: 0x21
-  __TEXT.__objc_methtype: 0xc2
-  __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0x98
+  __TEXT.__objc_methtype: 0xd5
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x288
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x160
-  __DATA_CONST.__cfstring: 0x620
+  __DATA_CONST.__const: 0x1e8
+  __DATA_CONST.__cfstring: 0x700
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x3a8
-  __DATA.__objc_selrefs: 0x2f8
-  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_const: 0x3f8
+  __DATA.__objc_selrefs: 0x330
+  __DATA.__objc_ivar: 0x48
   __DATA.__objc_data: 0xa0
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 699F0C42-D823-330A-A2E0-36842D9CF79B
-  Functions: 41
-  Symbols:   99
-  CStrings:  284
+  UUID: 643A58F8-5CE2-3853-9ECB-6E0C9419CE7A
+  Functions: 47
+  Symbols:   111
+  CStrings:  312
 
Symbols:
+ __NSConcreteStackBlock
+ __dispatch_source_type_timer
+ _dispatch_queue_create
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x27
- __os_feature_enabled_impl
- _objc_retain_x24
- _objc_retain_x28
CStrings:
+ "5"
+ "@36@0:8q16q24I32"
+ "Asked to defer readback. Launch conditions no longer met."
+ "B16@?0@\"OSLogEventProxy\"8"
+ "I"
+ "Interrupted early! Returning early."
+ "T@\"NSMutableArray\",R,N,V_simulatedQuarantines"
+ "Trying to stop in-flight reporting work."
+ "_min_quarantine_time_covered_sec"
+ "_simulatedQuarantines"
+ "addObject:"
+ "bookId"
+ "boolValue"
+ "com.apple.logd.statistics.quarantines.simulated"
+ "com.apple.logd_reporter.defer_polling_queue"
+ "initWithUnixTimeBoundAndMinQuarantineTime:to:min_quarantine_time_covered_sec:"
+ "numberWithBool:"
+ "numberWithUnsignedChar:"
+ "overallTotalPayloadBytes"
+ "processName"
+ "processTotalPayloadBytes"
+ "setEventHandler:"
+ "simulated"
+ "simulatedQuarantines"
+ "superQuarantine"
- "$"
- "Libtrace"
- "logd_reporter_quarantine_reports"
- "logd_reporter_sampling_reports"

```
