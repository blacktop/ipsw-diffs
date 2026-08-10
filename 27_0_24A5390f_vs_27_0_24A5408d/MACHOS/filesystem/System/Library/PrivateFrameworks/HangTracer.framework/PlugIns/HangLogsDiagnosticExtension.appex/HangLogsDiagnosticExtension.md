## HangLogsDiagnosticExtension

> `/System/Library/PrivateFrameworks/HangTracer.framework/PlugIns/HangLogsDiagnosticExtension.appex/HangLogsDiagnosticExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`

```diff

-424.0.0.0.0
-  __TEXT.__text: 0x133b0
-  __TEXT.__auth_stubs: 0xa30
+426.0.0.0.0
+  __TEXT.__text: 0x14a70
+  __TEXT.__auth_stubs: 0xab0
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_stubs: 0x1cc0
-  __TEXT.__objc_methlist: 0xbbc
-  __TEXT.__const: 0x260
-  __TEXT.__cstring: 0x26e5
-  __TEXT.__oslogstring: 0x1cb8
+  __TEXT.__objc_stubs: 0x1d20
+  __TEXT.__objc_methlist: 0xd2c
+  __TEXT.__const: 0x280
+  __TEXT.__cstring: 0x281c
+  __TEXT.__oslogstring: 0x2145
   __TEXT.__gcc_except_tab: 0x1cc
-  __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methname: 0x447c
-  __TEXT.__objc_methtype: 0x852
+  __TEXT.__objc_classname: 0xde
+  __TEXT.__objc_methname: 0x46b9
+  __TEXT.__objc_methtype: 0xa29
   __TEXT.__ustring: 0xe0
-  __TEXT.__unwind_info: 0x400
-  __DATA_CONST.__const: 0xd58
-  __DATA_CONST.__cfstring: 0x2680
-  __DATA_CONST.__objc_classlist: 0x48
+  __TEXT.__unwind_info: 0x448
+  __DATA_CONST.__const: 0xe48
+  __DATA_CONST.__cfstring: 0x2760
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x528
+  __DATA_CONST.__auth_got: 0x568
   __DATA_CONST.__got: 0x1d0
-  __DATA.__objc_const: 0x1fa8
-  __DATA.__objc_selrefs: 0xbe8
+  __DATA.__objc_const: 0x21c8
+  __DATA.__objc_selrefs: 0xcc0
   __DATA.__objc_ivar: 0x22c
-  __DATA.__objc_data: 0x2d0
-  __DATA.__data: 0x10c
-  __DATA.__bss: 0xf0
+  __DATA.__objc_data: 0x320
+  __DATA.__data: 0x204
+  __DATA.__bss: 0x150
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libapp_launch_measurement.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 456
-  Symbols:   478
-  CStrings:  1206
+  Functions: 484
+  Symbols:   503
+  CStrings:  1284
 
Symbols:
+ _HTEndNonResponsiveTaskAtTime
+ _MCTU_TO_MS
+ _OBJC_CLASS_$_HTBacklightHostObserver
+ _OBJC_METACLASS_$_HTBacklightHostObserver
+ __dyld_lazy_load
+ _assertionSignpost
+ _dispatch_after
+ _dispatch_time
+ _getEventFromPid
+ _getTimeBetweenAbsoluteAndContinuousTime
+ _getpid
+ _hasOpenScreenOffAssertionOverlappingHang
+ _kHTCAEventDisplayMonitorMissedState
+ _kHTCAEventDisplayMonitorNotifyLatency
+ _kHTCoreAnalyticsDisplayMonitorSource
+ _kHTCoreAnalyticsDisplayState
+ _kHTCoreAnalyticsNotifyLatencyMs
+ _kHTCoreAnalyticsTimeSinceDisplayChangeMs
+ _kHTScreenOffAssertionName
+ _legacySignpost
+ _mach_continuous_time
+ _memcpy
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _strncpy
CStrings:
+ "#16@0:8"
+ "%{public, signpost.description:end_time}llu missedTimeout=%{public, signpost.telemetry:number2}i"
+ "@\"NSString\"16@0:8"
+ "@24@0:8:16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "BLS timestamp underflow detected (finalContinuousTime=%llu < timeDelta=%llu), using mach_absolute_time()"
+ "BLSBacklightStateObserving"
+ "HTAssertion: HTBeginAssertion: track assertionId=%llu assertionname=(%s) starttime=%llu expirationTime=%llu"
+ "HTAssertion: desired timeout (%f) is greater than max allowed timeout (%f), using max allowed timeout"
+ "HTAssertions: HTEndAssertion: assertionId not found in recent array"
+ "HTAssertions: HTEndAssertion: assertionId=%llu assertionname=(%s) missed timeout (endTime was %fms after timeout)!"
+ "HTAssertions: HTEndAssertion: update assertionId=%llu assertionname=(%s) endTime is now=%llu"
+ "HTAssertions: HTEndAssertion:assertionCounter is 0"
+ "HTBacklightHostObserver"
+ "HTNonResponsiveTaskAssertion"
+ "Hang detected: %.2fs (overlaps an open screen-off assertion; deferring classification %.0fms to recheck)"
+ "Hang detected: %.2fs (under capture threshold, emitting telemetry)"
+ "NSObject"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TQ,R"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "autorelease"
+ "backlight:activatingWithEvent:"
+ "backlight:deactivatingWithEvent:"
+ "backlight:didChangeAlwaysOnEnabled:"
+ "backlight:didCompleteUpdateToState:forEvent:"
+ "backlight:didCompleteUpdateToState:forEvents:abortedEvents:"
+ "backlight:performingEvent:"
+ "changeRequest"
+ "class"
+ "com.apple.hangtracer.display_monitor_missed_state"
+ "com.apple.hangtracer.display_monitor_notify_latency"
+ "com.apple.hangtracer.screenoffassertionqueue"
+ "com.apple.springboard"
+ "conformsToProtocol:"
+ "debugDescription"
+ "display_state"
+ "hash"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "missedTimeout=%{public, signpost.telemetry:number2}i"
+ "monitor_source"
+ "name=%s timeout=%f screenOffAssertion=%{BOOL}i noTimeout=%{BOOL}i"
+ "name=%{public, signpost.description:attribute}s appliedTimeoutSecs=%{public, signpost.telemetry:number1}f"
+ "non_responsive_assertion"
+ "notify_latency_ms"
+ "numberWithInteger:"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "signpost_hang"
+ "superclass"
+ "system_screen_off"
+ "time_since_display_change_ms"
+ "v16@?0q8"
+ "v28@0:8@\"<BLSBacklightStateObservable>\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@\"<BLSBacklightStateObservable>\"16@\"BLSBacklightChangeEvent\"24"
+ "v32@0:8@16@24"
+ "v40@0:8@\"<BLSBacklightStateObservable>\"16q24@\"BLSBacklightChangeEvent\"32"
+ "v40@0:8@16q24@32"
+ "v48@0:8@\"<BLSBacklightStateObservable>\"16q24@\"NSArray\"32@\"NSArray\"40"
+ "v48@0:8@16q24@32@40"
+ "zone"
```
