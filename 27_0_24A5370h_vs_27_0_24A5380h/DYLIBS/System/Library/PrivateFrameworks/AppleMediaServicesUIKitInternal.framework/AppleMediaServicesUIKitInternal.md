## AppleMediaServicesUIKitInternal

> `/System/Library/PrivateFrameworks/AppleMediaServicesUIKitInternal.framework/AppleMediaServicesUIKitInternal`

```diff

-  __TEXT.__text: 0xb5b50
+  __TEXT.__text: 0xd9564
   __TEXT.__objc_methlist: 0x2d0
-  __TEXT.__const: 0x79a4
-  __TEXT.__constg_swiftt: 0x2c7c
-  __TEXT.__swift5_typeref: 0xbc3e
-  __TEXT.__swift5_reflstr: 0x165b
-  __TEXT.__swift5_fieldmd: 0x1a68
+  __TEXT.__const: 0x85f4
+  __TEXT.__constg_swiftt: 0x3000
+  __TEXT.__swift5_typeref: 0xc85e
+  __TEXT.__swift5_reflstr: 0x19ab
+  __TEXT.__swift5_fieldmd: 0x1de0
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__swift5_assocty: 0x938
-  __TEXT.__oslogstring: 0x13e4
-  __TEXT.__swift5_proto: 0x1e0
-  __TEXT.__swift5_types: 0x1d0
-  __TEXT.__swift_as_entry: 0xbc
-  __TEXT.__swift_as_ret: 0x12c
-  __TEXT.__swift_as_cont: 0x2a0
-  __TEXT.__swift5_capture: 0xbe4
-  __TEXT.__cstring: 0x19c2
+  __TEXT.__swift5_assocty: 0x9b0
+  __TEXT.__oslogstring: 0x2134
+  __TEXT.__swift5_proto: 0x210
+  __TEXT.__swift5_types: 0x1f4
+  __TEXT.__swift_as_entry: 0x100
+  __TEXT.__swift_as_ret: 0x17c
+  __TEXT.__swift_as_cont: 0x350
+  __TEXT.__swift5_capture: 0xe3c
+  __TEXT.__cstring: 0x1c22
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x2080
-  __TEXT.__eh_frame: 0x32cc
+  __TEXT.__unwind_info: 0x2758
+  __TEXT.__eh_frame: 0x4554
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x500
+  __DATA_CONST.__objc_selrefs: 0x568
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__got: 0xbb8
-  __AUTH_CONST.__const: 0x3848
-  __AUTH_CONST.__objc_const: 0x1100
-  __AUTH_CONST.__auth_got: 0x1ab0
-  __AUTH.__objc_data: 0x118
-  __AUTH.__data: 0xce8
-  __DATA.__data: 0x18a8
-  __DATA.__bss: 0x26b0
-  __DATA.__common: 0x160
-  __DATA_DIRTY.__objc_data: 0x2f8
-  __DATA_DIRTY.__data: 0x2880
+  __DATA_CONST.__got: 0xc80
+  __AUTH_CONST.__const: 0x4058
+  __AUTH_CONST.__objc_const: 0x12b0
+  __AUTH_CONST.__auth_got: 0x1c40
+  __AUTH.__objc_data: 0x168
+  __AUTH.__data: 0xfd8
+  __DATA.__data: 0x1cd8
+  __DATA.__bss: 0x2d70
+  __DATA.__common: 0x1a0
+  __DATA_DIRTY.__objc_data: 0x2f0
+  __DATA_DIRTY.__data: 0x2800
   __DATA_DIRTY.__bss: 0x1bb0
   __DATA_DIRTY.__common: 0x130
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2968
-  Symbols:   251
-  CStrings:  232
+  Functions: 3467
+  Symbols:   260
+  CStrings:  290
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
+ _NSUbiquitousKeyValueStoreDidChangeExternallyNotification
+ _OBJC_CLASS_$_AKAccountManager
+ _OBJC_CLASS_$_AKAppleIDAuthenticationController
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSNotificationCenter
+ _objc_retain_x27
+ _swift_bridgeObjectRetain_n
+ _swift_coroFrameAlloc
+ _swift_isEscapingClosureAtFileLocation
+ _swift_release_x3
+ _swift_task_getMainExecutor
- _swift_getObjCClassFromMetadata
- _swift_willThrowTypedImpl
CStrings:
+ "AMSUIKit.SignificantChange."
+ "AgeProvider.age: computed age = %ld"
+ "AgeProvider.age: failed to compute year-delta from birthday"
+ "AgeProvider.age: fetched birthday = %{private}s"
+ "AgeProvider.age: starting AuthKit birthday fetch"
+ "AgeProvider.ageOfMajority: jurisdictional majority = %ld"
+ "AgeProvider.ageOfMajority: no primary Apple account, defaulting to %ld"
+ "AgeProvider: AKAppleIDAuthenticationController() returned nil"
+ "AgeProvider: calling AKAppleIDAuthenticationController.fetchBirthday"
+ "AgeProvider: fetchBirthday callback error: %s"
+ "AgeProvider: fetchBirthday callback parsed date OK"
+ "AgeProvider: fetchBirthday callback returned no error but parts could not be assembled (birthday=%{private}s, birthmonth=%{private}s)"
+ "AgeProvider: fetching birthday from AuthKit"
+ "AgeProvider: no birth year for account"
+ "AgeProvider: no primary AuthKit account"
+ "AgeProvider: no primary altDSID"
+ "AgeProvider: resolved altDSID"
+ "AgeProvider: resolved birthYear = %{private}@"
+ "AgeProvider: resolved primary AuthKit account"
+ "AppBlockingModifier: .adultRequiresAck → showSignificantUpdateAcknowledgment"
+ "AppBlockingModifier: .minorRequiresConsent → cover will show via shouldBlock"
+ "AppBlockingModifier: .notApplicable → markAsHandled"
+ "AppBlockingModifier: adult ack succeeded → markAsHandled"
+ "AppBlockingModifier: every declared change already handled; skipping resolver"
+ "AppBlockingModifier: resolving decision for %ld/%ld still-pending change(s)"
+ "AppleMediaServicesUIKitInternal/SignificantChangeBlocking.swift"
+ "AppleMediaServicesUIKitInternal/SignificantChangeStore.swift"
+ "Approval Unavailable"
+ "CFBundleShortVersionString"
+ "ComplianceResolver: AuthKit branch — fetching age + ageOfMajority"
+ "ComplianceResolver: AuthKit isMinor=%{bool}d (age=%ld threshold=%ld)"
+ "ComplianceResolver: age check failed: %s"
+ "ComplianceResolver: failing closed to %s"
+ "ComplianceResolver: features parental=%{bool}d adult=%{bool}d"
+ "ComplianceResolver: fetching requiredRegulatoryFeatures"
+ "ComplianceResolver: final decision → %s"
+ "ComplianceResolver: no relevant feature → .notApplicable"
+ "ComplianceResolver: requiredRegulatoryFeatures failed: %s — failing closed to .minorRequiresConsent"
+ "ComplianceResolver: using test seam override → %s"
+ "Could not request approval at this time. Please try again later."
+ "DeclaredAgeRangeAction"
+ "Duplicate values for key: '"
+ "Failed to load jetpack: "
+ "Fatal error"
+ "FeatureBlockingModifier(%{public}s): .adultRequiresAck → showSignificantUpdateAcknowledgment"
+ "FeatureBlockingModifier(%{public}s): .minorRequiresConsent → presenting cover sheet"
+ "FeatureBlockingModifier(%{public}s): .notApplicable → markAsHandled, dismissing"
+ "FeatureBlockingModifier(%{public}s): adult ack already in flight — skipping re-dispatch"
+ "FeatureBlockingModifier(%{public}s): adult ack succeeded → markAsHandled"
+ "FeatureBlockingModifier(%{public}s): decision = %s"
+ "FeatureBlockingModifier(%{public}s): resolving decision"
+ "Incorrect actor executor assumption; Expected same executor as "
+ "Optional<SignificantChangeStore>"
+ "OriginalAppVersion"
+ "PendingApprovals"
+ "SignificantChangeBlockingHostView ask failed: %s"
+ "SignificantUpdateAction"
+ "Swift/NativeDictionary.swift"
+ "View.task @ AppleMediaServicesUIKitInternal/AMSUIKitStoreAccountProfileButton.swift:"
+ "View.task @ AppleMediaServicesUIKitInternal/SignificantChangeBlocking.swift:"
+ "significantChangeAppBlocking adult-acknowledgment failed: %s. Leaving changes unhandled; will retry next launch."
+ "significantChangeAppBlocking applied without a SignificantChangeStore in the environment. Apply .significantChangeStore(_:) above this view. Blocking is disabled."
+ "significantChangeFeatureBlocking adult-acknowledgment failed: %s. Leaving change unhandled; will retry next presentation."
+ "significantChangeFeatureBlocking applied without a SignificantChangeStore in the environment. Apply .significantChangeStore(_:) above this view. Blocking is disabled."
+ "waitUntilReady()"
- "Failed to create bundle from "
- "Failed to load Jetpack: "
- "Failed to load jetpack resource bundle."
- "Failed to load jetpack with error: "
- "Jetpack missing from app bundle at: "
- "Using amsuikit-account-hub.jetpack loaded from bundle: "
- "amsuikit-account-hub"

```
