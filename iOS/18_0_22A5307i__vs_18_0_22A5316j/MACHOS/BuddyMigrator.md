## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-5333.0.0.0.0
-  __TEXT.__text: 0xb9c8
-  __TEXT.__auth_stubs: 0x7a0
+5336.0.0.0.0
+  __TEXT.__text: 0xee00
+  __TEXT.__auth_stubs: 0x950
   __TEXT.__objc_stubs: 0x19e0
-  __TEXT.__objc_methlist: 0x7cc
-  __TEXT.__const: 0x310
+  __TEXT.__objc_methlist: 0x81c
+  __TEXT.__const: 0x16c
   __TEXT.__gcc_except_tab: 0x218
-  __TEXT.__objc_methname: 0x1ed6
-  __TEXT.__cstring: 0xb12
-  __TEXT.__oslogstring: 0x13a7
+  __TEXT.__objc_methname: 0x1f8c
+  __TEXT.__cstring: 0xec1
+  __TEXT.__oslogstring: 0x15a8
   __TEXT.__objc_classname: 0xf2
   __TEXT.__objc_methtype: 0x275
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__constg_swiftt: 0x128
-  __TEXT.__swift5_typeref: 0x225
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0xb5
-  __TEXT.__swift5_fieldmd: 0xb8
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__swift5_proto: 0x14
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__swift5_capture: 0x9c
-  __TEXT.__unwind_info: 0x3f8
-  __TEXT.__eh_frame: 0x470
-  __DATA_CONST.__auth_got: 0x3e0
-  __DATA_CONST.__got: 0x2a0
-  __DATA_CONST.__auth_ptr: 0x128
-  __DATA_CONST.__const: 0x608
+  __TEXT.__swift5_typeref: 0x2f1
+  __TEXT.__swift5_fieldmd: 0xf4
+  __TEXT.__constg_swiftt: 0x188
+  __TEXT.__swift5_capture: 0xc8
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__swift5_reflstr: 0xa1
+  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__eh_frame: 0x768
+  __DATA_CONST.__auth_got: 0x4b8
+  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__auth_ptr: 0x28
+  __DATA_CONST.__const: 0x660
   __DATA_CONST.__cfstring: 0xa40
-  __DATA_CONST.__objc_classlist: 0x50
-  __DATA_CONST.__objc_protolist: 0x48
+  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x14d0
-  __DATA.__objc_selrefs: 0x800
+  __DATA.__objc_const: 0x16b8
+  __DATA.__objc_selrefs: 0x818
   __DATA.__objc_ivar: 0xa8
-  __DATA.__objc_data: 0x540
-  __DATA.__data: 0x318
-  __DATA.__bss: 0x2e0
+  __DATA.__objc_data: 0x738
+  __DATA.__data: 0x3b0
+  __DATA.__bss: 0x60
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
-  - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
   - /System/Library/PrivateFrameworks/CloudServices.framework/CloudServices
   - /System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures

   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/DEPClientLibrary.framework/DEPClientLibrary
   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 319
-  Symbols:   283
-  CStrings:  634
+  Functions: 353
+  Symbols:   300
+  CStrings:  672
 
Symbols:
+ _AKAppleIDAuthenticationErrorDomain
+ _OBJC_CLASS_$_AKURLBag
+ _OBJC_CLASS_$_CSFFeatureManager
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$__TtC13BuddyMigrator25IntelligenceStateProvider
+ _OBJC_CLASS_$__TtC13BuddyMigrator27BuddyGMAvailabilityProvider
+ _OBJC_CLASS_$__TtC13BuddyMigrator33IntelligenceServerControlProvider
+ _OBJC_METACLASS_$__TtC13BuddyMigrator25IntelligenceStateProvider
+ _OBJC_METACLASS_$__TtC13BuddyMigrator27BuddyGMAvailabilityProvider
+ _OBJC_METACLASS_$__TtC13BuddyMigrator33IntelligenceServerControlProvider
+ __swiftEmptyArrayStorage
+ __swift_stdlib_bridgeErrorToNSError
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x3
+ _swift_allocError
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_continuation_throwingResume
+ _swift_continuation_throwingResumeWithError
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_willThrow
- _AFDeviceSupportsSystemAssistantExperience
- _OBJC_CLASS_$_CSFAvailability
- _OBJC_CLASS_$__TtC13BuddyMigrator31IntelligenceEligibilityProvider
- _OBJC_METACLASS_$__TtC13BuddyMigrator31IntelligenceEligibilityProvider
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreLocation
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
- _objc_release_x11
- _swift_deletedAsyncMethodErrorTu
- _swift_getForeignTypeMetadata
- _swift_getWitnessTable
CStrings:
+ "Checking if intelligence is available: %!{(MISSING)bool}d"
+ "Checking intelligence bag"
+ "Checking override flag"
+ "Failed to determine intelligence status. Abort!"
+ "Failed to fetch latest availability status with error: %!@(MISSING)"
+ "Fetching latest Intelligence availability status"
+ "Found intelligence override flag: %!{(MISSING)bool}d"
+ "GM on device status: shouldShow: %!{(MISSING)bool}d, with availability state: %!l(MISSING)d"
+ "Insufficient space allocated to copy string contents"
+ "Intelligence is already enabled."
+ "Intelligence state: %!s(MISSING)"
+ "IntelligenceServerFlagOverride"
+ "Should show intelligence: %!{(MISSING)bool}d"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "Updating intelligence availability"
+ "_TtC13BuddyMigrator25IntelligenceStateProvider"
+ "_TtC13BuddyMigrator27BuddyGMAvailabilityProvider"
+ "_TtC13BuddyMigrator33IntelligenceServerControlProvider"
+ "_TtP13BuddyMigrator25ProvidesIntelligenceState_"
+ "_TtP13BuddyMigrator33ProvidesIntelligenceServerControl_"
+ "_TtP13BuddyMigrator36ProvidesGenerativeModelsAvailability_"
+ "configurationValueForKey:fromCache:completion:"
+ "fetchLatestAvailabilityStatusWithCompletionHandler:"
+ "fetchLatestAvailabilityWithCompletionHandler:"
+ "generativeModelsAvailabilityProvider"
+ "getGMOptInToggleWithCompletion:"
+ "includeAppleIntelligenceForSetupAssistant"
+ "initWithFeatureFlags:availabilityProvider:stateProvider:"
+ "intelligence bag check failed with error: %!@(MISSING)"
+ "intelligence bag key not found"
+ "intelligence value in bag: %!{(MISSING)bool}d"
+ "invalid Collection: less than 'count' elements in collection"
+ "isAvailable"
+ "isDeviceEligibleForIntelligenceWithCompletionHandler:"
+ "isEnabledWithCompletionHandler:"
+ "isFeatureEnabledWithCompletionHandler:"
+ "isIntelligenceEnabledWithCompletionHandler:"
+ "serverControlProvider"
+ "serverFlag"
+ "shouldShowIntelligenceWithServerCheck:completionHandler:"
+ "stateProvider"
+ "v16@?0@\"NSError\"8"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@?0@8@\"NSError\"16"
+ "v28@0:8B16@?20"
+ "v28@0:8B16@?<v@?B>20"
- "BuddyMigrator/IntelligenceAvailabilityProvider.swift"
- "CSF is unavailable"
- "Intelligence availability status is %!l(MISSING)d with unavailability reason %!l(MISSING)d"
- "System is eligible for Intelligence upsell."
- "System is not eligible for Intelligence upsell."
- "Unknown availability status: "
- "_TtC13BuddyMigrator31IntelligenceEligibilityProvider"
- "_TtP13BuddyMigrator31ProvidesIntelligenceEligibility_"
- "availability"
- "currentAvailabilityWithCompletionHandler:"
- "eligibilityProvider"
- "getCurrentAvailabilityWithCompletionHandler:"
- "initWithFeatureFlags:availabilityProvider:eligibilityProvider:"
- "isAvailableWithCompletionHandler:"
- "isEligibleWithCompletionHandler:"
- "shouldNotShowReasons"
- "shouldShowIntelligenceWithCompletionHandler:"
- "status"
- "unavailabiltyReasons"
- "v16@?0@\"CSFAvailability\"8"
- "v24@0:8@?<v@?@\"CSFAvailability\">16"

```
