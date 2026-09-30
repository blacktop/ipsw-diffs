## AppleMediaServicesUIKitInternal

> `/System/Library/PrivateFrameworks/AppleMediaServicesUIKitInternal.framework/AppleMediaServicesUIKitInternal`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`

```diff

-2.0.23.0.0
-  __TEXT.__text: 0xd9564
+2.0.26.0.0
+  __TEXT.__text: 0xe4b68
   __TEXT.__objc_methlist: 0x2d0
-  __TEXT.__const: 0x85f4
-  __TEXT.__constg_swiftt: 0x3000
-  __TEXT.__swift5_typeref: 0xc85e
-  __TEXT.__swift5_reflstr: 0x19ab
-  __TEXT.__swift5_fieldmd: 0x1de0
-  __TEXT.__swift5_builtin: 0xb4
+  __TEXT.__const: 0x9374
+  __TEXT.__constg_swiftt: 0x325c
+  __TEXT.__swift5_typeref: 0xd35e
+  __TEXT.__swift5_reflstr: 0x1abb
+  __TEXT.__swift5_fieldmd: 0x1fe0
+  __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__swift5_assocty: 0x9b0
-  __TEXT.__oslogstring: 0x2134
-  __TEXT.__swift5_proto: 0x210
-  __TEXT.__swift5_types: 0x1f4
-  __TEXT.__swift_as_entry: 0x100
+  __TEXT.__swift5_assocty: 0xa10
+  __TEXT.__oslogstring: 0x1e24
+  __TEXT.__swift5_proto: 0x2c0
+  __TEXT.__swift5_types: 0x224
+  __TEXT.__swift_as_entry: 0x108
   __TEXT.__swift_as_ret: 0x17c
-  __TEXT.__swift_as_cont: 0x350
-  __TEXT.__swift5_capture: 0xe3c
-  __TEXT.__cstring: 0x1c22
+  __TEXT.__swift_as_cont: 0x348
+  __TEXT.__swift5_capture: 0xefc
+  __TEXT.__cstring: 0x1d12
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x2758
-  __TEXT.__eh_frame: 0x4554
+  __TEXT.__unwind_info: 0x2968
+  __TEXT.__eh_frame: 0x4564
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x568
+  __DATA_CONST.__objc_selrefs: 0x528
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__got: 0xc80
-  __AUTH_CONST.__const: 0x4058
-  __AUTH_CONST.__objc_const: 0x12b0
-  __AUTH_CONST.__auth_got: 0x1c40
+  __DATA_CONST.__got: 0xd18
+  __AUTH_CONST.__const: 0x44e8
+  __AUTH_CONST.__objc_const: 0x12d0
+  __AUTH_CONST.__auth_got: 0x1d58
   __AUTH.__objc_data: 0x168
-  __AUTH.__data: 0xfd8
-  __DATA.__data: 0x1cd8
-  __DATA.__bss: 0x2d70
-  __DATA.__common: 0x1a0
+  __AUTH.__data: 0xf68
+  __DATA.__data: 0x1ef8
+  __DATA.__bss: 0x40b0
+  __DATA.__common: 0x198
   __DATA_DIRTY.__objc_data: 0x2f0
-  __DATA_DIRTY.__data: 0x2800
-  __DATA_DIRTY.__bss: 0x1bb0
-  __DATA_DIRTY.__common: 0x130
+  __DATA_DIRTY.__data: 0x2a60
+  __DATA_DIRTY.__bss: 0x1eb0
+  __DATA_DIRTY.__common: 0x138
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3467
-  Symbols:   260
-  CStrings:  290
+  Functions: 3706
+  Symbols:   265
+  CStrings:  281
 
Symbols:
+ _AMSErrorDomain
+ _OBJC_CLASS_$_AMSAuthenticateTask
+ _OBJC_CLASS_$_AMSProcessInfo
+ _objc_retain_x1
+ _swift_cvw_initEnumMetadataSinglePayloadWithLayoutString
+ _swift_cvw_singlePayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_singlePayloadEnumGeneric_getEnumTag
+ _swift_retain_x9
+ _swift_unknownObjectRetain_n
- _OBJC_CLASS_$_AKAccountManager
- _OBJC_CLASS_$_AKAppleIDAuthenticationController
- _OBJC_CLASS_$_NSDateFormatter
- _objc_retain_x27
CStrings:
+ "AMS.UIKit.AccountHub.AccountButton.SignIn"
+ "AMS.UIKit.AccountHub.SignIn.Disabled"
+ "ComplianceResolver: userAge SPI isMinor=%{bool}d (age=%ld approvalAge=%ld)"
+ "ComplianceResolver: userAge unavailable — falling back to \\.requestAgeRange"
+ "FeatureBlockingModifier(%{public}s): .minorRequiresConsent → presenting cover"
+ "Invalid number of keys found, expected one."
+ "Running silent AMSAuthenticateTask inline"
+ "Something went wrong"
+ "We couldn't show the update notification. Please try again."
+ "handleAuthenticateRequest: %@"
+ "handleDialogRequest: %@"
+ "listenForAskResponses: received approval — questionID: %s"
+ "listenForAskResponses: received non-approval (declined) — questionID: %s; clearing pending entry"
+ "persistPendingApprovals: failed to encode pending-approval state; leaving stored value unchanged"
+ "restorePendingApprovals: stored value is not decodable; removing stale entry (pending approvals expire in 24h)"
+ "significantChangeAppBlocking adult-acknowledgment failed: %s. Surfacing retry alert."
+ "significantChangeFeatureBlocking adult-acknowledgment failed: %s. Surfacing retry alert."
- "AMSUIKitAccountHubWebViewModel creating webModel"
- "AgeProvider.age: computed age = %ld"
- "AgeProvider.age: failed to compute year-delta from birthday"
- "AgeProvider.age: fetched birthday = %{private}s"
- "AgeProvider.age: starting AuthKit birthday fetch"
- "AgeProvider.ageOfMajority: jurisdictional majority = %ld"
- "AgeProvider.ageOfMajority: no primary Apple account, defaulting to %ld"
- "AgeProvider: AKAppleIDAuthenticationController() returned nil"
- "AgeProvider: calling AKAppleIDAuthenticationController.fetchBirthday"
- "AgeProvider: fetchBirthday callback error: %s"
- "AgeProvider: fetchBirthday callback parsed date OK"
- "AgeProvider: fetchBirthday callback returned no error but parts could not be assembled (birthday=%{private}s, birthmonth=%{private}s)"
- "AgeProvider: fetching birthday from AuthKit"
- "AgeProvider: no birth year for account"
- "AgeProvider: no primary AuthKit account"
- "AgeProvider: no primary altDSID"
- "AgeProvider: resolved altDSID"
- "AgeProvider: resolved birthYear = %{private}@"
- "AgeProvider: resolved primary AuthKit account"
- "ComplianceResolver: AuthKit branch — fetching age + ageOfMajority"
- "ComplianceResolver: AuthKit isMinor=%{bool}d (age=%ld threshold=%ld)"
- "FeatureBlockingModifier(%{public}s): .minorRequiresConsent → presenting cover sheet"
- "handleAuthenticateRequest called"
- "handleDialogRequest called"
- "significantChangeAppBlocking adult-acknowledgment failed: %s. Leaving changes unhandled; will retry next launch."
- "significantChangeFeatureBlocking adult-acknowledgment failed: %s. Leaving change unhandled; will retry next presentation."
```
