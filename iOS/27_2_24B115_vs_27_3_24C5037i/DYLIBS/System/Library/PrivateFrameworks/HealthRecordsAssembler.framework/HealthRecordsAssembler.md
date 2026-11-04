## HealthRecordsAssembler

> `/System/Library/PrivateFrameworks/HealthRecordsAssembler.framework/HealthRecordsAssembler`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0x2644
-  __TEXT.__const: 0x2f2
+7027.2.13.0.0
+  __TEXT.__text: 0xbfd8
+  __TEXT.__objc_methlist: 0x2c
+  __TEXT.__const: 0x452
+  __TEXT.__cstring: 0x14b
+  __TEXT.__constg_swiftt: 0xac
+  __TEXT.__swift5_typeref: 0xdb
+  __TEXT.__swift5_fieldmd: 0x78
+  __TEXT.__swift5_reflstr: 0x95
+  __TEXT.__swift5_proto: 0x28
+  __TEXT.__swift5_types: 0xc
   __TEXT.__oslogstring: 0x6
-  __TEXT.__swift5_typeref: 0xb5
-  __TEXT.__swift5_reflstr: 0x55
   __TEXT.__swift5_assocty: 0x38
-  __TEXT.__constg_swiftt: 0x64
-  __TEXT.__swift5_fieldmd: 0x40
-  __TEXT.__swift5_proto: 0x1c
-  __TEXT.__swift5_types: 0x4
   __TEXT.__swift5_acfuncs: 0x14
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x10
-  __TEXT.__unwind_info: 0x188
-  __TEXT.__eh_frame: 0x280
+  __TEXT.__unwind_info: 0x320
+  __TEXT.__eh_frame: 0x470
+  __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_selrefs: 0x178
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x28
-  __AUTH_CONST.__objc_const: 0xd0
-  __AUTH_CONST.__auth_got: 0x250
-  __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0xc8
-  __DATA.__data: 0x98
+  __AUTH_CONST.__const: 0x118
+  __AUTH_CONST.__objc_const: 0x118
+  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH.__objc_data: 0x100
+  __AUTH.__data: 0xf0
+  __DATA.__data: 0x258
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 58
-  Symbols:   115
-  CStrings:  1
+  Functions: 160
+  Symbols:   183
+  CStrings:  6
 
Symbols:
+ _HKFHIRResourceTypeCondition
+ _HKFHIRResourceTypeObservation
+ _OBJC_CLASS_$_HDMedicalHistoryFHIRSynthesizer
+ _OBJC_CLASS_$_HKConcept
+ _OBJC_CLASS_$_HKFHIRResource
+ _OBJC_CLASS_$_HKFHIRVersion
+ _OBJC_CLASS_$_HKMedicalCodingSystem
+ _OBJC_CLASS_$_HKMedicalDate
+ _OBJC_CLASS_$_HKMedicalHistoryFHIRSynthesisResult
+ _OBJC_CLASS_$_HKMedicalHistoryHealthConcernRecord
+ _OBJC_CLASS_$_HKMedicalHistoryQuantitativeLabResultRecord
+ _OBJC_CLASS_$_HKMedicalHistoryRecord
+ _OBJC_CLASS_$_HKReferenceRange
+ _OBJC_CLASS_$_NSObject
+ _OBJC_METACLASS_$_HDMedicalHistoryFHIRSynthesizer
+ _OBJC_METACLASS_$_NSObject
+ __CLASS_METHODS_HDMedicalHistoryFHIRSynthesizer
+ __DATA_HDMedicalHistoryFHIRSynthesizer
+ __INSTANCE_METHODS_HDMedicalHistoryFHIRSynthesizer
+ __METACLASS_DATA_HDMedicalHistoryFHIRSynthesizer
+ ___swift_allocate_value_buffer
+ ___swift_memcpy16_8
+ ___swift_project_value_buffer
+ __swiftEmptySetSingleton
+ _associated conformance 22HealthRecordsAssembler17MHRSynthesisErrorO10Foundation09LocalizedE0AAs0E0
+ _objc_allocWithZone
+ _objc_autorelease
+ _objc_autoreleaseReturnValue
+ _objc_msgSend
+ _objc_msgSendSuper2
+ _objc_opt_self
+ _objc_release_x19
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x24
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x2
+ _objc_retain_x8
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_bridgeObjectRelease_n
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocClassInstance
+ _swift_dynamicCastObjCClass
+ _swift_errorRelease
+ _swift_getErrorValue
+ _swift_getMetatypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_once
+ _swift_release_x19
+ _swift_release_x28
+ _swift_setDeallocating
+ _swift_willThrow
+ _symbolic SS
+ _symbolic So8NSObjectC
+ _symbolic _____ 22HealthRecordsAssembler17MHRSynthesisErrorO
+ _symbolic _____ 22HealthRecordsAssembler29MedicalHistoryFHIRSynthesizerC
+ _type_layout_string 22HealthRecordsAssembler17MHRSynthesisErrorO
CStrings:
+ "No FHIR synthesis is implemented for medical history records of type "
+ "The record's primary concept has no coding or display name"
+ "http://terminology.hl7.org/CodeSystem/condition-clinical"
+ "http://terminology.hl7.org/CodeSystem/condition-ver-status"
+ "http://terminology.hl7.org/CodeSystem/observation-category"
```
