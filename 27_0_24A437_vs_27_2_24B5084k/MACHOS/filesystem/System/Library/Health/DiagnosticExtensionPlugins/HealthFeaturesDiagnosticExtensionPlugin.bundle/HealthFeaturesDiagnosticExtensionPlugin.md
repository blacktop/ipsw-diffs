## HealthFeaturesDiagnosticExtensionPlugin

> `/System/Library/Health/DiagnosticExtensionPlugins/HealthFeaturesDiagnosticExtensionPlugin.bundle/HealthFeaturesDiagnosticExtensionPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_capture`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x161c
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_stubs: 0x260
-  __TEXT.__objc_methlist: 0x64
-  __TEXT.__const: 0x10a
-  __TEXT.__objc_classname: 0x76
-  __TEXT.__objc_methname: 0x1da
+7027.1.36.2.7
+  __TEXT.__text: 0x4368
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_stubs: 0x480
+  __TEXT.__objc_methlist: 0x94
+  __TEXT.__const: 0x448
+  __TEXT.__objc_classname: 0xc6
+  __TEXT.__objc_methname: 0x374
   __TEXT.__objc_methtype: 0x59
-  __TEXT.__constg_swiftt: 0x64
-  __TEXT.__swift5_typeref: 0x52
-  __TEXT.__swift5_fieldmd: 0x20
+  __TEXT.__constg_swiftt: 0xdc
+  __TEXT.__swift5_typeref: 0xc8
+  __TEXT.__swift5_fieldmd: 0x68
   __TEXT.__swift5_capture: 0x14
-  __TEXT.__cstring: 0x7d
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__objc_classlist: 0x10
+  __TEXT.__cstring: 0x1c8
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0x23
+  __TEXT.__swift5_assocty: 0x60
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__eh_frame: 0x150
+  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__auth_got: 0x260
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0xd0
-  __DATA.__objc_selrefs: 0xb8
-  __DATA.__objc_data: 0x160
-  __DATA.__data: 0xf0
+  __DATA_CONST.__auth_got: 0x360
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__auth_ptr: 0xc8
+  __DATA.__objc_const: 0x130
+  __DATA.__objc_selrefs: 0x140
+  __DATA.__objc_data: 0x210
+  __DATA.__data: 0x1a8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/PrivateFrameworks/HealthDiagnosticExtensionCore.framework/HealthDiagnosticExtensionCore
   - /System/Library/PrivateFrameworks/HealthFeatures.framework/HealthFeatures
+  - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 22
-  Symbols:   67
-  CStrings:  36
+  Functions: 91
+  Symbols:   94
+  CStrings:  63
 
Symbols:
+ _HKAllFeatureIdentifiers
+ _HKFeatureIdentifierAFibBurden
+ _HKPreferredRegulatoryDomainProvider
+ _HKPrettyPrintedFeatureStatus
+ _NSStringFromHKOnboardingCompletionCountryCodeProvenance
+ _OBJC_CLASS_$_HKFeatureAvailabilityRequirementSatisfactionOverrides
+ _OBJC_CLASS_$_HKFeatureStatusManager
+ _OBJC_CLASS_$_HKRegulatoryDomainManager
+ _OBJC_CLASS_$_RDEstimate
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftOSLog
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_release_x26
+ _objc_retain_x21
+ _objc_retain_x23
+ _swift_arrayInitWithCopy
+ _swift_bridgeObjectRetain
+ _swift_getErrorValue
+ _swift_getForeignTypeMetadata
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_x19
+ _swift_release_x22
+ _swift_release_x8
CStrings:
+ "Country Code Information"
+ "Country Code Override"
+ "Error evaluating feature status for "
+ "Error evaluating region availability for "
+ "HKRegulatoryDomainEstimate"
+ "HealthFeatureStatus.txt"
+ "ISOCode"
+ "RDEstimate.currentEstimates"
+ "Region Availability"
+ "Requirement Satisfaction Overrides"
+ "_TtC39HealthFeaturesDiagnosticExtensionPlugin32FeatureStatusDiagnosticOperation"
+ "appendNewline"
+ "appendRow:"
+ "boolValue"
+ "currentEstimate"
+ "currentEstimates"
+ "featureAvailabilityProvidingForFeatureIdentifier:"
+ "featureStatusWithError:"
+ "initWithFeatureIdentifier:"
+ "initWithFeatureIdentifier:healthStore:"
+ "overriddenRequirementIdentifiers"
+ "overriddenSatisfactionOfRequirementWithIdentifier:"
+ "overrideISOCountryCode"
+ "prettyPrintedDescription"
+ "provenance"
+ "regionAvailabilityWithError:"
+ "timestamp"
```
