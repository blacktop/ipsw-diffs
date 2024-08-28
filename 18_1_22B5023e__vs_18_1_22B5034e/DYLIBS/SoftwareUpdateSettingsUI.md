## SoftwareUpdateSettingsUI

> `/System/Library/PrivateFrameworks/SoftwareUpdateSettingsUI.framework/SoftwareUpdateSettingsUI`

```diff

-384.0.0.0.0
-  __TEXT.__text: 0xee00c
+388.0.0.0.0
+  __TEXT.__text: 0xf2da0
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x4068
-  __TEXT.__cstring: 0x96de
-  __TEXT.__oslogstring: 0x15264
-  __TEXT.__gcc_except_tab: 0x34c0
+  __TEXT.__objc_methlist: 0x40d8
+  __TEXT.__cstring: 0x996e
+  __TEXT.__oslogstring: 0x15b54
+  __TEXT.__gcc_except_tab: 0x3b4c
   __TEXT.__dlopen_cstrs: 0x658
   __TEXT.__const: 0x6e
   __TEXT.__swift5_typeref: 0xc3
   __TEXT.__swift5_capture: 0xbc
-  __TEXT.__unwind_info: 0x1668
+  __TEXT.__unwind_info: 0x16c0
   __TEXT.__eh_frame: 0xf0
-  __TEXT.__objc_classname: 0x6f3
-  __TEXT.__objc_methname: 0xe29e
-  __TEXT.__objc_methtype: 0x2424
-  __TEXT.__objc_stubs: 0x95e0
-  __DATA_CONST.__got: 0x6c0
-  __DATA_CONST.__const: 0x90b8
+  __TEXT.__objc_classname: 0x6f5
+  __TEXT.__objc_methname: 0xe422
+  __TEXT.__objc_methtype: 0x2437
+  __TEXT.__objc_stubs: 0x96e0
+  __DATA_CONST.__got: 0x6f0
+  __DATA_CONST.__const: 0x9158
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d28
+  __DATA_CONST.__objc_selrefs: 0x2d70
   __DATA_CONST.__objc_superrefs: 0x100
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__auth_ptr: 0x28
   __AUTH_CONST.__const: 0x358
-  __AUTH_CONST.__cfstring: 0x4360
-  __AUTH_CONST.__objc_const: 0x9dc8
+  __AUTH_CONST.__cfstring: 0x4380
+  __AUTH_CONST.__objc_const: 0x9df8
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xaf0
-  __DATA.__objc_ivar: 0x44c
+  __DATA.__objc_ivar: 0x450
   __DATA.__data: 0x990
   __DATA.__bss: 0x241
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2084
-  Symbols:   2483
-  CStrings:  3653
+  Functions: 2109
+  Symbols:   2514
+  CStrings:  3681
 
Symbols:
+ _kSUOpenAlternateUpdateTapped
+ _kSUOpenNonPromotedUpdateTapped
+ _kSUOpenBetaUpdatesTapped
+ _kSUEnrollToBetaUpdatesTapped
+ _kSUOpenAutomaticUpdatesTapped
+ _kSUUnenrollToBetaUpdatesTapped
CStrings:
+ "%!s(MISSING): Hiding Apple ID row - device has installation restriction (%!l(MISSING)d)."
+ "%!s(MISSING): Stateful UI Manager Checkpoint\n\tcurrentState: %!{(MISSING)public}@ (%!l(MISSING)d)\n\tdelegate: %!{(MISSING)public}@ (%!p(MISSING))\n\tscanError: %!{(MISSING)public}@\n\tpreferredDescriptor: %!{(MISSING)public}@\n\talternateDescriptor: %!{(MISSING)public}@\n\tdownload: %!{(MISSING)public}@ (%!p(MISSING))\n\tthirdPartyScan: %!{(MISSING)public}s\n\tscheduledForAutoInstall: %!{(MISSING)public}s\n\thiddenUpdatesPostSelection: preferred[%!{(MISSING)public}s, %!{(MISSING)public}@]; alternate[%!{(MISSING)public}s, %!{(MISSING)public}@];\n\tselectedBetaProgram: %!l(MISSING)u (count: %!l(MISSING)d)\n\tOpFSMs: scan[%!p(MISSING)]; refresh[%!p(MISSING)]; update[%!p(MISSING)]; auxiliaryOperationsCount[%!l(MISSING)u]\n\nPurge result: %!d(MISSING); error: %!{(MISSING)public}@"
+ "v40@?0@\"SUSettingsStatefulUIManager\"8@\"SUDownload\"16@\"SDBetaProgram\"24@?<v@?Q>32"
+ "analyticsNonPromotedUpdateCellTappedString"
+ "setBetaProgramFromUI:forViewController:withCompletion:"
+ "analyticsBetaUpdatesCellTappedString"
+ "-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]"
+ "%!s(MISSING): %!s(MISSING) in program %!l(MISSING)d"
+ "-[SUSettingsStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]_block_invoke"
+ "_isBusy"
+ "\x16"
+ "enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:"
+ "v24@?0@\"SDBetaProgram\"8@\"NSError\"16"
+ "analyticsEnrolledToBetaUpdatesString"
+ "Failed to enroll"
+ "TB,N,V_isBusy"
+ "-[SUSUISoftwareUpdateBetaUpdatesController tableView:didSelectRowAtIndexPath:]_block_invoke"
+ "doEnrollInBetaUpdatesProgram:completionHandler:"
+ "objectAtIndexedSubscript:"
+ "%!s(MISSING): Enrolling in program %!l(MISSING)d"
+ "%!s(MISSING): Skipping adding %!{(MISSING)public}@ to program list"
+ "%!s(MISSING): Unenrolling from beta updates"
+ "analyticsAlternateUpdateCellTappedString"
+ "analyticsUnenrolledToBetaUpdatesString"
+ "-[SUSUISoftwareUpdateBetaUpdatesController tableView:didSelectRowAtIndexPath:]"
+ "-[SUSUISoftwareUpdateBetaUpdatesController appleIDSpecifier]"
+ "%!s(MISSING): Switch Beta Apple ID button tapped."
+ "-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:withPurgeConfirmation:completionHandler:]_block_invoke_2"
+ "Sucessfully enroll"
+ "v40@0:8@16@?24@?32"
+ "analyticsAutomaticUpdatesCellTappedString"
+ "%!s(MISSING): Stateful UI Manager Checkpoint\n\tcurrentState: %!{(MISSING)public}@ (%!l(MISSING)d)\n\tdelegate: %!{(MISSING)public}@ (%!p(MISSING))\n\tscanError: %!{(MISSING)public}@\n\tpreferredDescriptor: %!{(MISSING)public}@\n\talternateDescriptor: %!{(MISSING)public}@\n\tdownload: %!{(MISSING)public}@ (%!p(MISSING))\n\tthirdPartyScan: %!{(MISSING)public}s\n\tscheduledForAutoInstall: %!{(MISSING)public}s\n\thiddenUpdatesPostSelection: preferred[%!{(MISSING)public}s, %!{(MISSING)public}@]; alternate[%!{(MISSING)public}s, %!{(MISSING)public}@];\n\tselectedBetaProgram: %!l(MISSING)u (count: %!l(MISSING)d)\n\tOpFSMs: scan[%!p(MISSING)]; refresh[%!p(MISSING)]; update[%!p(MISSING)]; auxiliaryOperationsCount[%!l(MISSING)u]\n\nAttempts to enroll in beta program: %!l(MISSING)d (%!p(MISSING))"
+ "setIsBusy:"
+ "-[SUSettingsStatefulUIManager doEnrollInBetaUpdatesProgram:completionHandler:]"
+ "%!s(MISSING): Stateful UI Manager Checkpoint\n\tcurrentState: %!{(MISSING)public}@ (%!l(MISSING)d)\n\tdelegate: %!{(MISSING)public}@ (%!p(MISSING))\n\tscanError: %!{(MISSING)public}@\n\tpreferredDescriptor: %!{(MISSING)public}@\n\talternateDescriptor: %!{(MISSING)public}@\n\tdownload: %!{(MISSING)public}@ (%!p(MISSING))\n\tthirdPartyScan: %!{(MISSING)public}s\n\tscheduledForAutoInstall: %!{(MISSING)public}s\n\thiddenUpdatesPostSelection: preferred[%!{(MISSING)public}s, %!{(MISSING)public}@]; alternate[%!{(MISSING)public}s, %!{(MISSING)public}@];\n\tselectedBetaProgram: %!l(MISSING)u (count: %!l(MISSING)d)\n\tOpFSMs: scan[%!p(MISSING)]; refresh[%!p(MISSING)]; update[%!p(MISSING)]; auxiliaryOperationsCount[%!l(MISSING)u]\n\nUser responded to the targeted update purge request of %!{(MISSING)public}@, for beta program %!l(MISSING)d (%!p(MISSING)): %!{(MISSING)public}@"
+ "DELETE_CONFIRMATION_BODY_BETA_UPDATE_ENROLLMENT"
+ "%!s(MISSING): Stateful UI Manager Checkpoint\n\tcurrentState: %!{(MISSING)public}@ (%!l(MISSING)d)\n\tdelegate: %!{(MISSING)public}@ (%!p(MISSING))\n\tscanError: %!{(MISSING)public}@\n\tpreferredDescriptor: %!{(MISSING)public}@\n\talternateDescriptor: %!{(MISSING)public}@\n\tdownload: %!{(MISSING)public}@ (%!p(MISSING))\n\tthirdPartyScan: %!{(MISSING)public}s\n\tscheduledForAutoInstall: %!{(MISSING)public}s\n\thiddenUpdatesPostSelection: preferred[%!{(MISSING)public}s, %!{(MISSING)public}@]; alternate[%!{(MISSING)public}s, %!{(MISSING)public}@];\n\tselectedBetaProgram: %!l(MISSING)u (count: %!l(MISSING)d)\n\tOpFSMs: scan[%!p(MISSING)]; refresh[%!p(MISSING)]; update[%!p(MISSING)]; auxiliaryOperationsCount[%!l(MISSING)u]\n\nA targeted update exists when attempting to enroll in beta program: %!l(MISSING)d (%!p(MISSING)). Asking to purge the targeted update."
- "setBetaProgramFromUI:forSpecifier:"
- "\x06"
- "-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]"
- "Skipping adding %!{(MISSING)public}@ to program list"
- "-[SUSettingsStatefulUIManager enrollInBetaUpdatesProgram:completionHandler:]_block_invoke"
- "Enrolling in program %!l(MISSING)d"
- "Hiding Apple ID row - device has installation restriction (%!l(MISSING)d)."
- "enrollInBetaUpdatesProgram:completionHandler:"
- "Switch Beta Apple ID button tapped."
- "Unenrolling from beta updates"

```
