## GenerativeExperiencesRuntime

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/GenerativeExperiencesRuntime`

```diff

-291.1.0.5.0
-  __TEXT.__text: 0xeab80
-  __TEXT.__objc_methlist: 0x94c
-  __TEXT.__const: 0x5b4c
-  __TEXT.__cstring: 0x1ed5
-  __TEXT.__constg_swiftt: 0x1f14
-  __TEXT.__swift5_typeref: 0x2898
+291.6.0.5.101
+  __TEXT.__text: 0xef500
+  __TEXT.__objc_methlist: 0x96c
+  __TEXT.__const: 0x5ba8
+  __TEXT.__cstring: 0x1f75
+  __TEXT.__constg_swiftt: 0x1f10
+  __TEXT.__swift5_typeref: 0x2854
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_reflstr: 0x104d
-  __TEXT.__swift5_fieldmd: 0x145c
+  __TEXT.__swift5_reflstr: 0x108d
+  __TEXT.__swift5_fieldmd: 0x1484
   __TEXT.__swift5_assocty: 0x400
-  __TEXT.__oslogstring: 0x89a0
-  __TEXT.__swift5_proto: 0x304
-  __TEXT.__swift5_types: 0x220
-  __TEXT.__swift_as_entry: 0x350
-  __TEXT.__swift_as_ret: 0x368
-  __TEXT.__swift_as_cont: 0x73c
-  __TEXT.__swift5_capture: 0x2794
+  __TEXT.__oslogstring: 0x8e40
+  __TEXT.__swift5_proto: 0x308
+  __TEXT.__swift5_types: 0x224
+  __TEXT.__swift_as_entry: 0x36c
+  __TEXT.__swift_as_ret: 0x384
+  __TEXT.__swift_as_cont: 0x76c
+  __TEXT.__swift5_capture: 0x28d4
   __TEXT.__swift5_protos: 0x54
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3468
-  __TEXT.__eh_frame: 0x941c
+  __TEXT.__unwind_info: 0x3600
+  __TEXT.__eh_frame: 0x9714
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x128
-  __DATA_CONST.__objc_classlist: 0x1d8
+  __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e0
+  __DATA_CONST.__objc_selrefs: 0x700
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x8488
-  __AUTH_CONST.__objc_const: 0x3248
+  __AUTH_CONST.__const: 0x8800
+  __AUTH_CONST.__objc_const: 0x3300
   __AUTH_CONST.__auth_got: 0x27b0
   __AUTH.__objc_data: 0x3b8
-  __AUTH.__data: 0x508
-  __DATA.__data: 0xb08
-  __DATA.__bss: 0x27f0
-  __DATA.__common: 0xa0
+  __AUTH.__data: 0x5a0
+  __DATA.__data: 0xb90
+  __DATA.__bss: 0x27e0
+  __DATA.__common: 0xb0
   __DATA_DIRTY.__objc_data: 0x6c8
-  __DATA_DIRTY.__data: 0x3298
+  __DATA_DIRTY.__data: 0x3248
   __DATA_DIRTY.__bss: 0x2900
   __DATA_DIRTY.__common: 0x2b0
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AppleIntelligenceReporting.framework/AppleIntelligenceReporting
   - /System/Library/PrivateFrameworks/AppleIntelligenceReportingProcessing.framework/AppleIntelligenceReportingProcessing
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/AtomicsInternal.framework/AtomicsInternal
   - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5187
-  Symbols:   283
-  CStrings:  656
+  Functions: 5262
+  Symbols:   286
+  CStrings:  673
 
Symbols:
+ _MobileGestalt_get_isVirtualDevice
+ _OBJC_CLASS_$_AMSEphemeralDefaults
+ _OBJC_CLASS_$_NSURLCache
CStrings:
+ "AvailabilityReporter skipped redundant write, but would have logged event: %{public}s"
+ "LanguagePreferences initialized with: %s"
+ "LanguagePreferences language change detected: %s"
+ "LanguagePreferences received %s, fetched: %s"
+ "WaitlistEnrollmentBackfill: %{public}s; enrolling + applying bypass"
+ "WaitlistEnrollmentBackfill: applied gmEligibilityBypass; now %{bool,public}d"
+ "WaitlistEnrollmentBackfill: gmEligibilityBypass already set; left as-is"
+ "WaitlistEnrollmentBackfill: signed up for waitlist featureID=%{public}s; status=%{public}s"
+ "WaitlistEnrollmentBackfill: skipping waitlist signup — virtual device"
+ "WaitlistEnrollmentBackfill: skipping — device not exempt and no accepted waitlist override (isExemptDevice=%{bool,public}d, forcedWaitlistStatus=%{public}s)"
+ "WaitlistEnrollmentBackfill: skipping — not an internal build"
+ "WaitlistEnrollmentBackfill: waitlist signup failed for featureID=%{public}s: %{public}s"
+ "accepted waitlist override present"
+ "com.apple.GenerativeFunctions.PeriodicTasks.WaitlistEnrollmentBackfill.Boot"
+ "device is exempt from waitlist"
+ "forceWaitlistStatus: set GM eligibility bypass to %{bool,public}d; gmEligibilityBypass() now %{bool,public}d"
+ "runWaitlistEnrollmentBackfill: missingEntitlementForAdditionalCapability"
```
