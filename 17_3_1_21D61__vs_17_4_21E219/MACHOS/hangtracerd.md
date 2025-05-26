## hangtracerd

> `/usr/libexec/hangtracerd`

```diff

-281.2.0.0.0
-  __TEXT.__text: 0x24294
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x3c00
-  __TEXT.__objc_methlist: 0x1250
+288.0.0.0.0
+  __TEXT.__text: 0x25be8
+  __TEXT.__auth_stubs: 0xe30
+  __TEXT.__objc_stubs: 0x4140
+  __TEXT.__objc_methlist: 0x1488
   __TEXT.__const: 0x1d8
-  __TEXT.__gcc_except_tab: 0x320
-  __TEXT.__cstring: 0x339c
-  __TEXT.__objc_classname: 0x16a
-  __TEXT.__objc_methname: 0x6291
-  __TEXT.__objc_methtype: 0xc75
-  __TEXT.__oslogstring: 0x4709
-  __TEXT.__unwind_info: 0x55c
-  __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x1c8
+  __TEXT.__gcc_except_tab: 0x338
+  __TEXT.__cstring: 0x3448
+  __TEXT.__objc_classname: 0x19b
+  __TEXT.__objc_methname: 0x6850
+  __TEXT.__objc_methtype: 0xd30
+  __TEXT.__oslogstring: 0x48e4
+  __TEXT.__unwind_info: 0x5e8
+  __DATA_CONST.__auth_got: 0x728
+  __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1310
+  __DATA_CONST.__const: 0x14a8
   __DATA_CONST.__cfstring: 0x3e60
-  __DATA_CONST.__objc_classlist: 0x78
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x228
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x98
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x3048
-  __DATA.__objc_selrefs: 0x12e0
-  __DATA.__objc_classrefs: 0x1f8
-  __DATA.__objc_superrefs: 0x40
-  __DATA.__objc_ivar: 0x2e0
-  __DATA.__objc_data: 0x4b0
+  __DATA.__objc_const: 0x35d8
+  __DATA.__objc_selrefs: 0x1458
+  __DATA.__objc_ivar: 0x330
+  __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x290
-  __DATA.__bss: 0xb00
+  __DATA.__bss: 0xb10
   __DATA.__common: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 618
-  Symbols:   342
-  CStrings:  2033
+  Functions: 681
+  Symbols:   350
+  CStrings:  2133
 
Symbols:
+ _CACurrentMediaTime
+ _CAFrameRateRangeMake
+ _NSDefaultRunLoopMode
+ _OBJC_CLASS_$_CADisplayLink
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_NSThread
+ _OBJC_METACLASS_$_CATextLayer
+ _kCAContextDisplayId
+ _objc_opt_isKindOfClass
- _kCAContextDisplayName
CStrings:
+ "\x01!"
+ "\x03\x11"
+ "\x064"
+ "\x121"
+ "%{public}@ added to tailspin capture"
+ "%{public}@ hit its Generated Log limit of %u for this reporting period. Not saving a report!"
+ "%{public}@: Could not create file - won't take a tailspin: %{public}@ %s"
+ "%{public}@: Hang detected %.2fs (%{public}@, %{public}@) duration < capture threshold %.2fs after accounting for assertion overlaps, not capturing tailspin for it"
+ "%{public}@: Hang detected %.2fs (%{public}@, %{public}@) duration > capture threshold %.2fs after accounting for assertion overlaps"
+ "%{public}@: HangTracer tailspin support is disabled, not saving a report!"
+ "%{public}@: Moving tailspin to spool: %{public}@\n"
+ "%{public}@: Tailspin Request Denied because tailspin-buffer has been dumped since this hang ended -> it won't have any trace data for this hang\n"
+ "%{public}@: Tailspin filepaths will be scrubbed: %{BOOL}d (Customer build: %{BOOL}d, DiagnosticPipeline upload enabled: %{BOOL}d)"
+ "%{public}@: Tried to save tailspin, but shouldSaveHangLogs said NO"
+ "%{public}@: Tried to save tailspin, but tailspin support is not present on this device!"
+ "%{public}@: Unable to create UTF8 string from JSON: %{public}@\n"
+ "%{public}@: Unable to move tailspin to final path: %{public}@"
+ "%{public}@: Unable to save tailspin data to file, reason: %ld\n"
+ "%{public}@: Unable to serialize Info Dict into JSON: %{public}@ - %{public}@\n"
+ "@\"<NSObject><NSCopying>\""
+ "@\"CADisplayLink\""
+ "@\"HUDDurationLayer\""
+ "@\"HUDTheme\""
+ "@\"NSMutableArray\""
+ "@56@0:8d16d24d32@?40@?48"
+ "@?"
+ "@?16@0:8"
+ "B32@?0@\"HUDAnimation\"8Q16^B24"
+ "Fence-hang: Hang detected %.2fs (%{public}@) > capture threshold"
+ "Fence-hang: Hang detected %.2fs (%{public}@), duration < capture threshold after accounting for assertion overlaps, not capturing tailspin for it"
+ "HUDAnimation"
+ "HUDAnimator"
+ "HUDDurationLayer"
+ "Hang %{public}@ detected for bundleid %{public}@ for already reported user switched away hang, startTime %llu"
+ "Hang %{public}@ detected, %{public}@ hang is over timeout threshold of %llu exceeded => capturing hang log"
+ "Hang %{public}@ detected: %.2fs (debugger attached, not reporting)"
+ "Hang %{public}@ detected: xctest with debugger attached will still be tracked as non-debugger hang"
+ "Hang on App Exit detected, %{public}@ hang is over %@ log threshold of %llu exceeded => capturing hang log"
+ "Initialization complete now watching hangs for %{public}@ | %{public}s"
+ "New proc: %{public}@(%u)"
+ "Successfully created directory at path %@"
+ "T@\"<NSObject><NSCopying>\",&,N,V_identifier"
+ "T@\"HUDDurationLayer\",R,N,V_durationLayer"
+ "T@\"HUDTheme\",&,N,V_currentTheme"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
+ "T@\"NSString\",?,R,C"
+ "T@\"UISCurrentUserInterfaceStyleValue\",&,N,V_userInterfaceStyleObserver"
+ "T@?,C,N,V_completionBlock"
+ "T@?,C,N,V_updateBlock"
+ "TB,N,V_canceled"
+ "TB,N,V_retargeted"
+ "Tailspin Request Denied: tailspin-buffer will not contain relevant trace data for the time-range of this request due to recent tailspin-capture\n               Filename: %{public}@, Process: %{public}@, Time Between Recent Tailspin Capture and Hang EndTime: %f secs, Hang EndTime: %f secs ago, Recent Tailspin Capture: %f secs ago\n"
+ "Td,N,V_endTime"
+ "Td,N,V_fromValue"
+ "Td,N,V_hangDuration"
+ "Td,N,V_startTime"
+ "Td,N,V_toValue"
+ "Td,N,V_updateInterval"
+ "There was an error querying the LS database for bundle id %{public}@: %@"
+ "Unable to create an LS application record from bundle id %{public}@: %@"
+ "WARNING: %{public}@ was already being watched."
+ "_animationQueue"
+ "_animations"
+ "_canceled"
+ "_completionBlock"
+ "_currentAnimation"
+ "_currentTheme"
+ "_displayLink"
+ "_displayLinkAccessQueue"
+ "_displayLinkInvalidated"
+ "_fromValue"
+ "_hangDuration"
+ "_identifier"
+ "_retargeted"
+ "_toValue"
+ "_updateBlock"
+ "_updateInterval"
+ "_userInterfaceStyleObserver"
+ "addToRunLoop:forMode:"
+ "beginAnimationFromValue:toValue:duration:updateBlock:completionBlock:"
+ "canceled"
+ "client %{public}@ [%d] does not bear entitlement \"%s\"; refusing HANGTRACER_XPC_CMD_COLLECT_LOGS command"
+ "client %{public}@ [%d] does not bear entitlement \"%s\"; refusing HANGTRACER_XPC_CMD_HANG_LOGS_PROCESSED command"
+ "client %{public}@ [%d] is not expected to issue this command; refusing HANGTRACER_XPC_CMD_HANG_LOGS_PROCESSED command"
+ "com.apple.hangtracerd.HUDAnimationDisplayLinkQueue"
+ "com.apple.hangtracerd.HUDAnimationQueue"
+ "com.apple.hangtracerd.HUDAnimator"
+ "completionBlock"
+ "currentRunLoop"
+ "currentTheme"
+ "d24@0:8d16"
+ "displayId"
+ "displayLinkFired:"
+ "displayLinkWithTarget:selector:"
+ "endAnimation:"
+ "fromValue"
+ "hang endTime  %llu for hangsubType %{public}@"
+ "hangDuration"
+ "hangtracerd: Received XPC Event via notifyd: notification name = %{public}@"
+ "indexOfObjectPassingTest:"
+ "indexesOfObjectsPassingTest:"
+ "initWithBlock:"
+ "initWithLayer:"
+ "objectsAtIndexes:"
+ "queue"
+ "removeObjectsAtIndexes:"
+ "replaceObjectAtIndex:withObject:"
+ "retargeted"
+ "run"
+ "setCanceled:"
+ "setCurrentTheme:"
+ "setEndTime:"
+ "setFromValue:"
+ "setHangDuration:"
+ "setHangDuration:animated:"
+ "setIdentifier:"
+ "setPreferredFrameRateRange:"
+ "setProcessName:duration:textColor:animated:"
+ "setQualityOfService:"
+ "setQueue:"
+ "setRetargeted:"
+ "setStartTime:"
+ "setUpdateBlock:"
+ "setUpdateInterval:"
+ "setUserInterfaceStyleObserver:"
+ "sharedAnimator"
+ "start"
+ "toValue"
+ "updateAnimation:toValue:duration:"
+ "updateBlock"
+ "updateCurrentTheme"
+ "updateDisplayLink"
+ "updateInterval"
+ "userInterfaceStyleObserver"
+ "v16@?0B8B12"
+ "v16@?0d8"
+ "v40@0:8@16d24d32"
+ "v44@0:8@16d24^{CGColor=}32B40"
+ "valueAtTime:"
- "\x054"
- "\x12"
- "%@ added to tailspin capture"
- "%@ hit its Generated Log limit of %u for this reporting period. Not saving a report!"
- "%@: Could not create file - won't take a tailspin: %@ %s"
- "%@: Hang detected %.2fs (%@, %@) duration < capture threshold %.2fs after accounting for assertion overlaps, not capturing tailspin for it"
- "%@: Hang detected %.2fs (%@, %@) duration > capture threshold %.2fs after accounting for assertion overlaps"
- "%@: HangTracer tailspin support is disabled, not saving a report!"
- "%@: Tailspin Request Denied because tailspin-buffer has been dumped since this hang ended -> it won't have any trace data for this hang\n"
- "%@: Tailspin filepaths will be scrubbed: %{BOOL}d (Customer build: %{BOOL}d, DiagnosticPipeline upload enabled: %{BOOL}d)"
- "%@: Tried to save tailspin, but shouldSaveHangLogs said NO"
- "%@: Tried to save tailspin, but tailspin support is not present on this device!"
- "%@: Unable to create UTF8 string from JSON: %@\n"
- "%@: Unable to move tailspin to final path: %@"
- "%@: Unable to save tailspin data to file, reason: %ld\n"
- "%@: Unable to serialize Info Dict into JSON: %@ - %@\n"
- "Fence-hang: Hang detected %.2fs (%@) > capture threshold"
- "Fence-hang: Hang detected %.2fs (%@), duration < capture threshold after accounting for assertion overlaps, not capturing tailspin for it"
- "Hang %@ detected for bundleid %@ for already reported user switched away hang, startTime %llu"
- "Hang %@ detected, %@ hang is over timeout threshold of %llu exceeded => capturing hang log"
- "Hang %@ detected: %.2fs (debugger attached, not reporting)"
- "Hang %@ detected: xctest with debugger attached will still be tracked as non-debugger hang"
- "Hang on App Exit detected, %@ hang is over %@ log threshold of %llu exceeded => capturing hang log"
- "Initialization complete now watching hangs for %@ | %s"
- "LCD"
- "New proc: %@(%u)"
- "Sucessfully created directory at path %@"
- "T@\"CATextLayer\",R,N,V_durationLayer"
- "T@\"UISCurrentUserInterfaceStyleValue\",&,N,V_userInterfaceStyle"
- "Tailspin Request Denied: tailspin-buffer will not contain relevant trace data for the time-range of this request due to recent tailspin-capture\n               Filename: %@, Process: %@, Time Between Recent Tailspin Capture and Hang EndTime: %f secs, Hang EndTime: %f secs ago, Recent Tailspin Capture: %f secs ago\n"
- "There was an error querying the LS database for bundle id %@: %@"
- "WARNING: %@ was already being watched."
- "_userInterfaceStyle"
- "client %@ [%d] does not bear entitlement \"%s\"; refusing HANGTRACER_XPC_CMD_COLLECT_LOGS command"
- "client %@ [%d] does not bear entitlement \"%s\"; refusing HANGTRACER_XPC_CMD_HANG_LOGS_PROCESSED command"
- "client %@ [%d] is not expected to issue this command; refusing HANGTRACER_XPC_CMD_HANG_LOGS_PROCESSED command"
- "hang endTime  %llu for hangsubType %@"
- "hangtracerd: Received XPC Event via notifyd: notification name = %@"
- "setUserInterfaceStyle:"

```
