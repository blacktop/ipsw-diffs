## RunningBoard

> `/System/Library/PrivateFrameworks/RunningBoard.framework/RunningBoard`

```diff

-945.40.4.0.0
-  __TEXT.__text: 0x7a988
-  __TEXT.__auth_stubs: 0x1420
-  __TEXT.__objc_methlist: 0x4f00
+945.60.5.502.1
+  __TEXT.__text: 0x7b2e8
+  __TEXT.__auth_stubs: 0x1410
+  __TEXT.__objc_methlist: 0x4f30
   __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0x6ae4
-  __TEXT.__oslogstring: 0xb003
-  __TEXT.__gcc_except_tab: 0xc4c
-  __TEXT.__unwind_info: 0x1aa8
+  __TEXT.__cstring: 0x6b91
+  __TEXT.__oslogstring: 0xb1e7
+  __TEXT.__gcc_except_tab: 0xcb0
+  __TEXT.__unwind_info: 0x1ac8
   __TEXT.__objc_classname: 0xf1d
-  __TEXT.__objc_methname: 0xcbbe
-  __TEXT.__objc_methtype: 0x2b68
-  __TEXT.__objc_stubs: 0x9a60
-  __DATA_CONST.__got: 0x778
-  __DATA_CONST.__const: 0x1620
+  __TEXT.__objc_methname: 0xcce1
+  __TEXT.__objc_methtype: 0x2b92
+  __TEXT.__objc_stubs: 0x9b80
+  __DATA_CONST.__got: 0x788
+  __DATA_CONST.__const: 0x1648
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x168
-  __DATA_CONST.__objc_protolist: 0x190
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ad0
+  __DATA_CONST.__objc_selrefs: 0x2b18
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x6b8
-  __AUTH_CONST.__auth_got: 0xa20
+  __AUTH_CONST.__auth_got: 0xa18
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x5820
-  __AUTH_CONST.__objc_const: 0xea38
+  __AUTH_CONST.__cfstring: 0x5860
+  __AUTH_CONST.__objc_const: 0xeb38
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x9c8
-  __DATA.__data: 0x12c0
+  __DATA.__objc_ivar: 0x9d8
+  __DATA.__data: 0x1320
   __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0x1fe0
   __DATA_DIRTY.__data: 0x10

   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/IOGPU.framework/IOGPU
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
+  - /System/Library/PrivateFrameworks/OSEligibility.framework/OSEligibility
   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 2530
-  Symbols:   3294
-  CStrings:  4338
+  Functions: 2539
+  Symbols:   3307
+  CStrings:  4368
 
Symbols:
+ _OBJC_CLASS_$_OSEligibilityQuery
+ _OBJC_CLASS_$_TRIClient
- _os_eligibility_get_domain_answer
CStrings:
+ "\x05\x17"
+ "@\"<RBXNUWrapper>\""
+ "@\"TRIClient\""
+ "BallastOffset"
+ "Bundle ID on LSApplication record is nil, defaulting to eligible"
+ "COREOS_GMPOWER_VM_TUNING_PAGE_SHORTAGE_THRESHOLDS"
+ "Error setting ballast drained for %!@(MISSING): %!{(MISSING)public}s"
+ "Error setting ballast drained to YES for %!@(MISSING)"
+ "Error setting ballast offset"
+ "Foreground app is %!@(MISSING), setting ballast drained to NO"
+ "Making eligibility query with domain: %!l(MISSING)lu, bundle ID: %!@(MISSING), persona: %!@(MISSING)"
+ "Setting ballast offset to %!l(MISSING)ld"
+ "The last foreground app removed was app is %!@(MISSING), setting ballast drained to YES"
+ "Trial Update Received: Setting ballast offset to %!l(MISSING)ld"
+ "_ballastOffsetMB"
+ "_deviceIsEligibleForDomain:bundleID:"
+ "_runningVisibleApps"
+ "_setBallastOffset:"
+ "_trialClient"
+ "_xnuWrapper"
+ "addUpdateHandlerForNamespaceName:usingBlock:"
+ "answer"
+ "ballastOffsetMB"
+ "clientWithIdentifier:"
+ "failure getting eligibility info for domain %!q(MISSING)u with error: %!@(MISSING)"
+ "initWithDomain:bundleID:persona:error:"
+ "initWithStateCaptureManager:historialStatistics:xnuWrapper:"
+ "kern.memorystatus.ballast_drained"
+ "kern.memorystatus.ballast_offset_mb"
+ "levelForFactor:withNamespaceName:"
+ "q20@0:8B16"
+ "refresh"
+ "setBallastDrained:"
+ "v16@?0@\"<TRINamespaceUpdateProtocol>\"8"
- "\x05\x15"
- "_deviceIsEligibleForDomain:"
- "failure getting eligibility info for domain %!q(MISSING)u: %!s(MISSING)"
- "initWithStateCaptureManager:historialStatistics:"

```
