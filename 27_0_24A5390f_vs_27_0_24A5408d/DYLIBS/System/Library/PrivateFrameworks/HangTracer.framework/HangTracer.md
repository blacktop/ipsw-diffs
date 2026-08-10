## HangTracer

> `/System/Library/PrivateFrameworks/HangTracer.framework/HangTracer`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA_DIRTY.__objc_data`

```diff

-424.0.0.0.0
-  __TEXT.__text: 0x17524
-  __TEXT.__objc_methlist: 0x9fc
-  __TEXT.__const: 0x268
+426.0.0.0.0
+  __TEXT.__text: 0x1837c
+  __TEXT.__lazy_helpers: 0x54
+  __TEXT.__objc_methlist: 0xb6c
+  __TEXT.__const: 0x258
   __TEXT.__gcc_except_tab: 0x214
-  __TEXT.__cstring: 0x45aa
-  __TEXT.__oslogstring: 0x2bf4
+  __TEXT.__cstring: 0x469d
+  __TEXT.__oslogstring: 0x2d1c
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__unwind_info: 0x618
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x17f8
-  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__const: 0x1890
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa58
+  __DATA_CONST.__objc_selrefs: 0xb48
   __DATA_CONST.__objc_superrefs: 0x20
-  __DATA_CONST.__got: 0x1f0
-  __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x5c60
-  __AUTH_CONST.__objc_const: 0x1a98
+  __DATA_CONST.__got: 0x1f8
+  __AUTH_CONST.__const: 0x5c0
+  __AUTH_CONST.__cfstring: 0x5d20
+  __AUTH_CONST.__objc_const: 0x1cb8
+  __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x5f0
-  __AUTH.__objc_data: 0x140
+  __AUTH_CONST.__auth_got: 0x610
+  __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x1f4
-  __DATA.__data: 0x220
+  __DATA.__data: 0x30c
   __DATA.__common: 0x18
-  __DATA.__bss: 0xe0
+  __DATA.__bss: 0x138
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 589
-  Symbols:   1510
-  CStrings:  1001
+  Functions: 606
+  Symbols:   1569
+  CStrings:  1012
 
Symbols:
+ -[HTBacklightHostObserver backlight:didCompleteUpdateToState:forEvent:]
+ GCC_except_table47
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table54
+ GCC_except_table75
+ GCC_except_table85
+ _HTHangEventCreateWithBundleID.__htBacklight
+ _HTHangEventCreateWithBundleID.__htBacklightHostObserver
+ _HTHangEventCreateWithBundleID.sbBacklightHostObserverOnce
+ _HTHangEventCreateWithBundleID.sbLegacyDisplayComparisonOnce
+ _HTScreenOffAssertionQueue._htScreenOffAssertionQueue
+ _HTScreenOffAssertionQueue.onceToken
+ _HTTrackDisplayStateForMonitorComparison
+ _HTTrackDisplayStateForMonitorComparison.populateSystemDisplayStatusArrayToken
+ _HTTrackDisplayStateForMonitorComparison.prevDisplayState
+ _HTTrackDisplayStateForMonitorComparison.prevTransitionTime
+ _MCTU_TO_MS
+ _OBJC_CLASS_$_BLSBacklight
+ _OBJC_CLASS_$_BLSBacklight$lazyGOT
+ _OBJC_CLASS_$_BLSBacklight$lazyGOT$loadHelper_x8
+ _OBJC_CLASS_$_HTBacklightHostObserver
+ _OBJC_METACLASS_$_HTBacklightHostObserver
+ __OBJC_$_INSTANCE_METHODS_HTBacklightHostObserver
+ __OBJC_$_PROP_LIST_HTBacklightHostObserver
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BLSBacklightStateObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BLSBacklightStateObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_BLSBacklightStateObserving
+ __OBJC_CLASS_PROTOCOLS_$_HTBacklightHostObserver
+ __OBJC_CLASS_RO_$_HTBacklightHostObserver
+ __OBJC_LABEL_PROTOCOL_$_BLSBacklightStateObserving
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_HTBacklightHostObserver
+ __OBJC_PROTOCOL_$_BLSBacklightStateObserving
+ __OBJC_PROTOCOL_$_NSObject
+ ___71-[HTBacklightHostObserver backlight:didCompleteUpdateToState:forEvent:]_block_invoke
+ ___HTScreenOffAssertionQueue_block_invoke
+ ___HTTrackDisplayStateForMonitorComparison_block_invoke
+ ___HTTrackDisplayStateForMonitorComparison_block_invoke_2
+ ___HTTrackDisplayStateForMonitorComparison_block_invoke_3
+ ___block_descriptor_121_e8_32s40s_e8_v16?0q8ls32l8s40l8
+ ___block_descriptor_44_e19_"NSDictionary"8?0l
+ ___block_descriptor_44_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_52_e19_"NSDictionary"8?0l
+ ___block_descriptor_64_e8_32bs_e5_v8?0ls32l8
+ __dyld_lazy_load
+ _dispatch_after
+ _dispatch_time
+ _gHTDisplayMonitorComparisonLock
+ _gHTScreenOffAssertion
+ _hasOpenScreenOffAssertionOverlappingHang
+ _kHTCAEventDisplayMonitorMissedState
+ _kHTCAEventDisplayMonitorNotifyLatency
+ _kHTCoreAnalyticsDisplayMonitorSource
+ _kHTCoreAnalyticsDisplayState
+ _kHTCoreAnalyticsNotifyLatencyMs
+ _kHTCoreAnalyticsTimeSinceDisplayChangeMs
+ _lazyLoadFlag$BacklightServices
+ _memcpy
+ _objc_msgSend$addObserver:
+ _objc_msgSend$backlightState
+ _objc_msgSend$changeRequest
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$sharedBacklight
+ _objc_msgSend$timestamp
- GCC_except_table41
- GCC_except_table43
- GCC_except_table45
- GCC_except_table48
- GCC_except_table53
- GCC_except_table64
- _HTIsDeviceRestricted
- ___block_descriptor_56_e19_"NSDictionary"8?0l
- _kHTAppActivationFailureReasonWatchdog_block_invoke.htAssertion
- _kHTAppActivationFailureReasonWatchdog_block_invoke.prevDisplayState
CStrings:
+ "BLS timestamp underflow detected (finalContinuousTime=%llu < timeDelta=%llu), using mach_absolute_time()"
+ "Hang detected: %.2fs (overlaps an open screen-off assertion; deferring classification %.0fms to recheck)"
+ "Hang detected: %.2fs (under capture threshold, emitting telemetry)"
+ "HangTracer SB: BLSBacklight host observer subscribed (sharedBacklight=%p initialState=%ld)"
+ "HangTracer SB: failed to subscribe legacy display comparison signal (notify status %u)"
+ "com.apple.hangtracer.display.comparison.notification"
+ "com.apple.hangtracer.display_monitor_missed_state"
+ "com.apple.hangtracer.display_monitor_notify_latency"
+ "com.apple.hangtracer.screenoffassertionqueue"
+ "display_state"
+ "monitor_source"
+ "notify_latency_ms"
+ "time_since_display_change_ms"
+ "v16@?0q8"
- "Display state changed %i -> %i"
- "HangTracer SB Screen State: Detected Screen ON -> OFF but an old HT Assertion still exists when we're about to create a new one"
- "com.apple.hangtracer.display.notification"
```
