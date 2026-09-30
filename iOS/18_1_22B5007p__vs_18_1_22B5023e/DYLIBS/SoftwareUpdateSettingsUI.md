## SoftwareUpdateSettingsUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI`

```diff

-362.0.0.0.0
-  __TEXT.__text: 0xeb3a8
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x4030
-  __TEXT.__cstring: 0x944e
-  __TEXT.__oslogstring: 0x14cb4
-  __TEXT.__gcc_except_tab: 0x3280
+384.0.0.0.0
+  __TEXT.__text: 0xee00c
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_methlist: 0x4068
+  __TEXT.__cstring: 0x96de
+  __TEXT.__oslogstring: 0x15264
+  __TEXT.__gcc_except_tab: 0x34c0
   __TEXT.__dlopen_cstrs: 0x658
-  __TEXT.__const: 0x6a
+  __TEXT.__const: 0x6e
   __TEXT.__swift5_typeref: 0xc3
   __TEXT.__swift5_capture: 0xbc
   __TEXT.__unwind_info: 0x1668
   __TEXT.__eh_frame: 0xf0
-  __TEXT.__objc_classname: 0x6f2
-  __TEXT.__objc_methname: 0xe1b5
+  __TEXT.__objc_classname: 0x6f3
+  __TEXT.__objc_methname: 0xe29e
   __TEXT.__objc_methtype: 0x2424
-  __TEXT.__objc_stubs: 0x9520
-  __DATA_CONST.__got: 0x6b8
-  __DATA_CONST.__const: 0x88a0
+  __TEXT.__objc_stubs: 0x95e0
+  __DATA_CONST.__got: 0x6c0
+  __DATA_CONST.__const: 0x90b8
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ce8
+  __DATA_CONST.__objc_selrefs: 0x2d28
   __DATA_CONST.__objc_superrefs: 0x100
-  __AUTH_CONST.__auth_got: 0x4a0
+  __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0x358
-  __AUTH_CONST.__cfstring: 0x42a0
-  __AUTH_CONST.__objc_const: 0x9d88
+  __AUTH_CONST.__cfstring: 0x4360
+  __AUTH_CONST.__objc_const: 0x9dc8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x444
+  __DATA.__objc_ivar: 0x44c
   __DATA.__data: 0x990
   __DATA.__bss: 0x241
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftWebKit.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2080
-  Symbols:   2465
-  CStrings:  3622
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2084
+  Symbols:   2483
+  CStrings:  3653
 
Symbols:
+ _OBJC_EHTYPE_$_NSException
+ __swift_FORCE_LOAD_$_swiftWebKit
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _objc_begin_catch
+ _objc_end_catch
CStrings:
+ "\x04\x1b"
+ "%!s(MISSING) [%!{(MISSING)public}@]: The seeding beta manager was not configured for this scan operation. Skipping."
+ "%!s(MISSING): Error (code: %!l(MISSING)d) while performing scan for requested URL: %!{(MISSING)public}@"
+ "%!s(MISSING): Found a UTs session stored in NSUserDefaults. However, the process '%!d(MISSING)' isn't running anymore. As SUSkipMockingKitPIDValidation is on - we will continue to use the test plan with this, incorrect, PID."
+ "%!s(MISSING): Found a UTs session stored in NSUserDefaults. However, the process '%!d(MISSING)' isn't running anymore. Killing the session."
+ "%!s(MISSING): Found a UTs session stored in NSUserDefaults. However, the session stored process start time for pid %!l(MISSING)d, %!l(MISSING)d, different than the start time of the current process with this pid, %!l(MISSING)d. As SUSkipMockingKitPIDValidation is on - we will continue to use the test plan with this, corrupted, PID."
+ "%!s(MISSING): Found a UTs session stored in NSUserDefaults. However, the session stored process start time for pid %!l(MISSING)d, %!l(MISSING)d, different than the start time of the current process with this pid, %!l(MISSING)d. Killing the session."
+ "%!s(MISSING): Start to observe for Unit Testing requests.\nNSUserDefaults Automation enabled? %!@(MISSING)"
+ "%!s(MISSING): Stateful UI Manager Checkpoint\n\tcurrentState: %!{(MISSING)public}@ (%!l(MISSING)d)\n\tdelegate: %!{(MISSING)public}@ (%!p(MISSING))\n\tscanError: %!{(MISSING)public}@\n\tpreferredDescriptor: %!{(MISSING)public}@\n\talternateDescriptor: %!{(MISSING)public}@\n\tdownload: %!{(MISSING)public}@ (%!p(MISSING))\n\tthirdPartyScan: %!{(MISSING)public}s\n\tscheduledForAutoInstall: %!{(MISSING)public}s\n\thiddenUpdatesPostSelection: preferred[%!{(MISSING)public}s, %!{(MISSING)public}@]; alternate[%!{(MISSING)public}s, %!{(MISSING)public}@];\n\tselectedBetaProgram: %!l(MISSING)u (count: %!l(MISSING)d)\n\tOpFSMs: scan[%!p(MISSING)]; refresh[%!p(MISSING)]; update[%!p(MISSING)]; auxiliaryOperationsCount[%!l(MISSING)u]\n\nScan has finished, but we've been given a nil options. Skipping."
+ "%!s(MISSING): Stops observing for Unit Testing requests."
+ "%!s(MISSING): Timeout while performing scan for requested URL: %!{(MISSING)public}@"
+ "-[SUSUISoftwareUpdateController(SoftwareUpdate) beginInstallOperation]_block_invoke"
+ "-[SUSUISoftwareUpdateController(SoftwareUpdate) beginInstallTonightOperation]_block_invoke"
+ "-[SUSUISoftwareUpdateController(SoftwareUpdate) beginUpdateDownloadOnlyOperation]_block_invoke"
+ "-[SUSUISoftwareUpdateController(SoftwareUpdate) beginUpdateNowOperation]_block_invoke"
+ "-[SUSUISoftwareUpdateController(SoftwareUpdate) beginUpdateTonightOperation]_block_invoke"
+ "-[SUSUITestAutomationManager resolveStoredXCUISession:]"
+ "-[SUSUITestAutomationManager startObserving]"
+ "-[SUSUITestAutomationManager stopObserving]"
+ "SupportedDeviceNames"
+ "SupportedDevices"
+ "UnsupportedDevices"
+ "[XCUI correlationId: %!@(MISSING)] Sending the didEnd event to service type: %!@(MISSING)"
+ "_MeasurementAlgorithm"
+ "_OSVersionCompatibilities"
+ "_currentActivityStyle"
+ "_observing"
+ "isPerformingFullScan"
+ "isPerformingRefresh"
+ "isPerformingUpdate"
+ "shouldDisableAutoDownloadIOSUpdatesToggle"
+ "shouldSkipMockingKitPIDValidation"
+ "shouldSkipMockingKitPIDValidation:"
+ "startObserving"
+ "stopObserving"
+ "version"
- "\x0f"
- "%!s(MISSING): NSUserDefaults Automation enabled? %!@(MISSING)"
- "-[SUSUITestAutomationManager init]"
- "Found a UTs session stored in NSUserDefaults. However, the process '%!d(MISSING)' isn't running anymore. Killing the session."
- "Found a UTs session stored in NSUserDefaults. However, the session stored process start time for pid %!l(MISSING)d, %!l(MISSING)d, different than the start time of the current process with this pid, %!l(MISSING)d. Killing the session."

```
