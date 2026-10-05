## HealthPlatformFoundation

> `/System/Library/PrivateFrameworks/HealthPlatformFoundation.framework/HealthPlatformFoundation`

```diff

-7027.1.45.2.4
-  __TEXT.__text: 0x57d98
+7027.1.54.2.3
+  __TEXT.__text: 0x5ef74
   __TEXT.__objc_methlist: 0x240
-  __TEXT.__const: 0x35ac
-  __TEXT.__swift5_typeref: 0xe31
-  __TEXT.__swift5_capture: 0x134
-  __TEXT.__oslogstring: 0xcf8
-  __TEXT.__constg_swiftt: 0x1120
-  __TEXT.__swift5_reflstr: 0xdbf
-  __TEXT.__swift5_fieldmd: 0x1120
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__cstring: 0x82f
-  __TEXT.__swift5_proto: 0x294
-  __TEXT.__swift5_types: 0x138
-  __TEXT.__swift_as_entry: 0xc8
+  __TEXT.__const: 0x36dc
+  __TEXT.__swift5_typeref: 0xe4b
+  __TEXT.__swift5_capture: 0x144
+  __TEXT.__oslogstring: 0xf48
+  __TEXT.__constg_swiftt: 0x113c
+  __TEXT.__swift5_reflstr: 0xdff
+  __TEXT.__swift5_fieldmd: 0x116c
+  __TEXT.__swift5_builtin: 0x3c
+  __TEXT.__cstring: 0xcaf
+  __TEXT.__swift5_proto: 0x29c
+  __TEXT.__swift5_types: 0x13c
+  __TEXT.__swift_as_entry: 0xcc
   __TEXT.__swift_as_ret: 0xbc
-  __TEXT.__swift_as_cont: 0x148
+  __TEXT.__swift_as_cont: 0x14c
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_protos: 0x58
-  __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1d70
-  __TEXT.__eh_frame: 0x2328
+  __TEXT.__swift5_mpenum: 0x10
+  __TEXT.__unwind_info: 0x1e58
+  __TEXT.__eh_frame: 0x23e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x180
+  __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__got: 0x510
-  __AUTH_CONST.__const: 0x20f8
-  __AUTH_CONST.__objc_const: 0xce8
-  __AUTH_CONST.__auth_got: 0xcc8
+  __DATA_CONST.__got: 0x6c0
+  __AUTH_CONST.__const: 0x21b8
+  __AUTH_CONST.__objc_const: 0xd08
+  __AUTH_CONST.__auth_got: 0xd30
   __AUTH.__objc_data: 0x240
   __AUTH.__data: 0x6c0
-  __DATA.__data: 0x8f0
+  __DATA.__data: 0x9c0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x1600

   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/HealthOrchestration.framework/HealthOrchestration
+  - /System/Library/PrivateFrameworks/HealthUtilities.framework/HealthUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2012
-  Symbols:   633
-  CStrings:  122
+  Functions: 2076
+  Symbols:   642
+  CStrings:  163
 
Symbols:
+ _get_enum_tag_for_layout_string 24HealthPlatformFoundation0A37AppIntelligenceAvailabilitySimulationV4ModeO
+ _kHKAppleIntelligenceAvailabilitySimulation
+ _kHKAppleIntelligenceConfigurationHeldEnabledState
+ _swift_retain_x8
+ _symbolic Say_____G 16FoundationModels19SystemLanguageModelC20InternalAvailabilityO14RestrictedInfoV0H6ReasonO
+ _symbolic Shy_____G 16FoundationModels19SystemLanguageModelC20InternalAvailabilityO15UnavailableInfoV0H6ReasonO
+ _symbolic _____ 24HealthPlatformFoundation0A37AppIntelligenceAvailabilitySimulationV
+ _symbolic _____ 24HealthPlatformFoundation0A37AppIntelligenceAvailabilitySimulationV4ModeO
+ _symbolic _____Sg 15HealthUtilities20SendableUserDefaultsC
+ _symbolic _____ySbSgGSg 15HealthUtilities21ObservableUserDefaultC
+ _type_layout_string 24HealthPlatformFoundation0A37AppIntelligenceAvailabilitySimulationV
+ _type_layout_string 24HealthPlatformFoundation0A37AppIntelligenceAvailabilitySimulationV4ModeO
- _swift_retain_x24
- _symbolic So14NSUserDefaultsCSg
- _symbolic _____ 24HealthPlatformFoundation0A24AppIntelligenceUtilitiesV
CStrings:
+ "Health App Intelligent Configuration availability simulated: %{public}s"
+ "Health App Intelligent Configuration is disabled for language identifier: %{public}s"
+ "Ignoring unparseable Health App Intelligent Configuration availability simulation: %{public}s"
+ "Model eligibility undetermined for language identifier: %{public}s; holding %{bool,public}d"
+ "No availability reported"
+ "Received undetermined restricted reasons: %s"
+ "Received undetermined unavailable reasons: %s"
+ "Recorded Health App Intelligent Configuration state: %{bool,public}d"
+ "Restricted with no reason given"
+ "Unavailable with no reason given"
+ "accessNotGranted"
+ "countryBillingIneligible"
+ "countryLocationIneligible"
+ "deviceClassIneligible"
+ "deviceIsInsecure"
+ "deviceNotCapable"
+ "externalBootDrive"
+ "externalIntelligenceNotAllowed"
+ "key value "
+ "localeIneligible"
+ "mdmAndParentalControl"
+ "noCacheForBaseUnavailableReasons"
+ "parentalRestriction"
+ "partnerNotSelected"
+ "pendingEnrollment"
+ "profileMisconfigured"
+ "regionIneligible"
+ "regionalSafetyAssetPendingUpdate"
+ "selectedLanguageDoesNotMatchSelectedSiriLanguage"
+ "selectedLanguageIneligible"
+ "selectedSiriLanguageIneligible"
+ "signInNotAllowed"
+ "siriAssetIsNotReady"
+ "siriAssetStatusUnknown"
+ "startupInProgress"
+ "unableToFetchAvailability"
+ "useCaseDoesNotAllowCurrentIPCountryCode"
+ "useCaseDoesNotAllowUserLocaleRegion"
+ "useCaseDoesNotSupportCurrentRegion"
+ "useCaseDoesNotSupportRequestedLanguage"
+ "useCaseDoesNotSupportSystemLanguage"
+ "workspaceNotAllowed"
- "No availability reported; treating as unavailable"
```
