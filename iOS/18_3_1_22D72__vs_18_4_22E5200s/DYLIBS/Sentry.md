## Sentry

> `/System/Library/PrivateFrameworks/Sentry.framework/Sentry`

```diff

-1.20.38.0.0
-  __TEXT.__text: 0xf7dc
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_methlist: 0xd00
+1.20.42.0.0
+  __TEXT.__text: 0x106cc
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_methlist: 0xd60
   __TEXT.__const: 0xe4
-  __TEXT.__cstring: 0x12dd
-  __TEXT.__oslogstring: 0x1b7a
-  __TEXT.__gcc_except_tab: 0x438
-  __TEXT.__unwind_info: 0x440
-  __TEXT.__objc_classname: 0x192
-  __TEXT.__objc_methname: 0x2d44
-  __TEXT.__objc_methtype: 0x3bb
-  __TEXT.__objc_stubs: 0x1e40
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0x450
-  __DATA_CONST.__objc_classlist: 0x80
+  __TEXT.__cstring: 0x1426
+  __TEXT.__oslogstring: 0x1c31
+  __TEXT.__gcc_except_tab: 0x474
+  __TEXT.__unwind_info: 0x490
+  __TEXT.__objc_classname: 0x1b1
+  __TEXT.__objc_methname: 0x2e56
+  __TEXT.__objc_methtype: 0x3dd
+  __TEXT.__objc_stubs: 0x1f00
+  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__const: 0x4a0
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9f8
-  __DATA_CONST.__objc_superrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x340
-  __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x1020
-  __AUTH_CONST.__objc_const: 0x1828
+  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_superrefs: 0x50
+  __AUTH_CONST.__auth_got: 0x370
+  __AUTH_CONST.__const: 0x340
+  __AUTH_CONST.__cfstring: 0x11c0
+  __AUTH_CONST.__objc_const: 0x19b0
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x12c
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x148
   __DATA.__data: 0xe8
-  __DATA.__bss: 0x80
-  __DATA.__common: 0x18
+  __DATA.__bss: 0x90
+  __DATA.__common: 0x11
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__bss: 0x90
-  __DATA_DIRTY.__common: 0x50
+  __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DiagnosticRequest.framework/DiagnosticRequest
   - /System/Library/PrivateFrameworks/MetricKitSource.framework/MetricKitSource
   - /System/Library/PrivateFrameworks/SignpostCollection.framework/SignpostCollection

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 418
-  Symbols:   676
-  CStrings:  822
+  Functions: 442
+  Symbols:   708
+  CStrings:  855
 
Symbols:
+ _AnalyticsSendEvent
+ _OBJC_CLASS_$_STYSignpostStreamingStatistics
+ _OBJC_METACLASS_$_STYSignpostStreamingStatistics
+ _TSPDumpOptions_EndTimestamp
+ ___udivti3
+ __dispatch_source_type_signal
+ _dispatch_block_create_with_qos_class
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_source_cancel
+ _objc_retain_x27
- _TSPDumpOptions_MaxTimestamp
CStrings:
+ "\x17"
+ "%@:%@"
+ "@\"STYSignpostStreamingStatistics\""
+ "Emitting com.apple.Sentry.SignpostStreaming telemetry %@"
+ "Emitting com.apple.Sentry.SignpostStreaming.SubsystemCategory telemetry %@"
+ "No signposts, and only monitoring for less than a minute, not emitting telemetry"
+ "STYSignpostStreamingStatistics"
+ "T@\"STYSignpostStreamingStatistics\",&,V_streamingStatistics"
+ "_machAbsTimeStart"
+ "_periodicTimer"
+ "_queue"
+ "_sigtermSource"
+ "_streamingStatistics"
+ "_subsystemDict"
+ "_totalCount"
+ "addSignpost:"
+ "com.apple.Sentry.SignpostStreaming"
+ "com.apple.Sentry.SignpostStreaming.PendingTelemetry"
+ "com.apple.Sentry.SignpostStreaming.SubsystemCategory"
+ "com.apple.sentry.signpostsMonitor.SignpostStreamingStatistics"
+ "emitTelemetry"
+ "initWithFormat:"
+ "isSyntheticIntervalEvent"
+ "largest_sc"
+ "largest_sc_count"
+ "largest_sc_rate"
+ "largest_signpost"
+ "largest_signpost_count"
+ "largest_signpost_rate"
+ "sc"
+ "sc_count"
+ "sc_rate"
+ "setStreamingStatistics:"
+ "signpost_count"
+ "signpost_rate"
+ "streamingStatistics"
- "\x16"
- "App launch threshold enforced"
- "ApplicationFirstFramePresentation"

```
