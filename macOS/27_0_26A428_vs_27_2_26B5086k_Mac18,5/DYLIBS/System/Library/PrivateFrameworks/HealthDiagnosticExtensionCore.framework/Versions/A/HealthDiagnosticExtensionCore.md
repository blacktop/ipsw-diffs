## HealthDiagnosticExtensionCore

> `/System/Library/PrivateFrameworks/HealthDiagnosticExtensionCore.framework/Versions/A/HealthDiagnosticExtensionCore`

```diff

-7027.0.72.1.1
-  __TEXT.__text: 0xadc4
-  __TEXT.__objc_methlist: 0x664
+7027.1.36.1.2
+  __TEXT.__text: 0xa098
+  __TEXT.__objc_methlist: 0x5ec
   __TEXT.__const: 0x92
   __TEXT.__gcc_except_tab: 0x2bc
-  __TEXT.__cstring: 0x21b6
+  __TEXT.__cstring: 0x204b
   __TEXT.__oslogstring: 0x34
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_typeref: 0x22
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x378
+  __TEXT.__unwind_info: 0x350
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__objc_classlist: 0x60
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x810
+  __DATA_CONST.__objc_selrefs: 0x740
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0xa8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x20e0
-  __AUTH_CONST.__objc_const: 0x918
+  __AUTH_CONST.__const: 0x4f0
+  __AUTH_CONST.__cfstring: 0x1ee0
+  __AUTH_CONST.__objc_const: 0x888
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x300
-  __AUTH.__objc_data: 0x420
+  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH.__objc_data: 0x3d0
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/HealthDaemon.framework/Versions/A/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/Versions/A/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
-  - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/Versions/A/RegulatoryDomain
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 188
-  Symbols:   784
-  CStrings:  296
+  Functions: 178
+  Symbols:   732
+  CStrings:  279
 
Symbols:
- -[HDFeatureStatusDiagnosticOperation _reportCountryCodeOverride]
- -[HDFeatureStatusDiagnosticOperation _reportCountryCodeSource]
- -[HDFeatureStatusDiagnosticOperation _reportFeatureStatusByFeature]
- -[HDFeatureStatusDiagnosticOperation _reportFeatureStatusForFeature:healthStore:]
- -[HDFeatureStatusDiagnosticOperation _reportRegionAvailabilityByFeature]
- -[HDFeatureStatusDiagnosticOperation _reportRegionAvailabilityForFeature:healthStore:]
- -[HDFeatureStatusDiagnosticOperation _reportRequirementSatisfactionOverridesByFeature]
- -[HDFeatureStatusDiagnosticOperation reportFilename]
- -[HDFeatureStatusDiagnosticOperation run]
- _HKAllFeatureIdentifiers
- _HKFeatureIdentifierAFibBurden
- _HKPreferredRegulatoryDomainProvider
- _HKPrettyPrintedFeatureStatus
- _HKRegulatoryDomainEstimateOverrideISOCode
- _NSStringFromHKOnboardingCompletionCountryCodeProvenance
- _OBJC_CLASS_$_HDFeatureStatusDiagnosticOperation
- _OBJC_CLASS_$_HKFeatureAvailabilityRequirementSatisfactionOverrides
- _OBJC_CLASS_$_HKFeatureStatusManager
- _OBJC_CLASS_$_RDEstimate
- _OBJC_METACLASS_$_HDFeatureStatusDiagnosticOperation
- __OBJC_$_INSTANCE_METHODS_HDFeatureStatusDiagnosticOperation
- __OBJC_CLASS_RO_$_HDFeatureStatusDiagnosticOperation
- __OBJC_METACLASS_RO_$_HDFeatureStatusDiagnosticOperation
- ___86-[HDFeatureStatusDiagnosticOperation _reportRequirementSatisfactionOverridesByFeature]_block_invoke
- ___block_descriptor_40_e8_32s_e31_v24?0"NSString"8"NSString"16l
- _objc_msgSend$ISOCode
- _objc_msgSend$_reportCountryCodeOverride
- _objc_msgSend$_reportCountryCodeSource
- _objc_msgSend$_reportFeatureStatusByFeature
- _objc_msgSend$_reportFeatureStatusForFeature:healthStore:
- _objc_msgSend$_reportRegionAvailabilityByFeature
- _objc_msgSend$_reportRegionAvailabilityForFeature:healthStore:
- _objc_msgSend$_reportRequirementSatisfactionOverridesByFeature
- _objc_msgSend$allObjects
- _objc_msgSend$allowExperimentalHealthTypesUsage
- _objc_msgSend$boolValue
- _objc_msgSend$currentEstimate
- _objc_msgSend$currentEstimates
- _objc_msgSend$featureAvailabilityProvidingForFeatureIdentifier:
- _objc_msgSend$featureStatusWithError:
- _objc_msgSend$features
- _objc_msgSend$initWithFeatureIdentifier:
- _objc_msgSend$initWithFeatureIdentifier:healthStore:countryCodeSource:
- _objc_msgSend$overriddenRequirementIdentifiers
- _objc_msgSend$overriddenSatisfactionOfRequirementWithIdentifier:
- _objc_msgSend$prettyPrintedDescription
- _objc_msgSend$provenance
- _objc_msgSend$regionAvailabilityWithError:
- _objc_msgSend$sortedArrayUsingSelector:
- _objc_msgSend$timestamp
- _objc_retainAutoreleasedReturnValue
- _swift_bridgeObjectRelease
CStrings:
+ "HealthTypes Enabled: true\n"
- "%@ (%@)"
- "%@:"
- "<none>"
- "<redacted>"
- "Country Code Information"
- "Country Code Override"
- "Error evaluating feature status for %@: %@"
- "Error evaluating region availability for %@: %@"
- "Feature Status"
- "HKRegulatoryDomainEstimate"
- "HealthFeatureStatus.txt"
- "HealthTypes Enabled: "
- "RDEstimate.currentEstimates"
- "Region Availability"
- "Requirement Satisfaction Overrides"
- "Retrieved: %@"
- "nil"
- "v24@?0@\"NSString\"8@\"NSString\"16"
```
