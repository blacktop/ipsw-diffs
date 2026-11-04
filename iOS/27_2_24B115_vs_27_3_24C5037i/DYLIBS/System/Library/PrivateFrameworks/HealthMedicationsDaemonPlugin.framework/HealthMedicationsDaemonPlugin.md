## HealthMedicationsDaemonPlugin

> `/System/Library/PrivateFrameworks/HealthMedicationsDaemonPlugin.framework/HealthMedicationsDaemonPlugin`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0x5b17c
-  __TEXT.__objc_methlist: 0x4604
-  __TEXT.__const: 0x5ac
-  __TEXT.__cstring: 0x6610
+7027.2.13.0.0
+  __TEXT.__text: 0x690b0
+  __TEXT.__delay_stubs: 0x40
+  __TEXT.__delay_helper: 0xa4
+  __TEXT.__objc_methlist: 0x470c
+  __TEXT.__const: 0x5d0
+  __TEXT.__cstring: 0x6750
   __TEXT.__gcc_except_tab: 0xa10
-  __TEXT.__oslogstring: 0x66c0
+  __TEXT.__oslogstring: 0x679c
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0xb4
-  __TEXT.__swift5_typeref: 0x104
+  __TEXT.__swift5_typeref: 0x10a
   __TEXT.__swift5_reflstr: 0x59
   __TEXT.__swift5_fieldmd: 0xa8
   __TEXT.__swift5_proto: 0x24

   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x14
-  __TEXT.__unwind_info: 0x1b88
-  __TEXT.__eh_frame: 0x4d8
+  __TEXT.__unwind_info: 0x1e60
+  __TEXT.__eh_frame: 0xbd0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d50
-  __DATA_CONST.__objc_classlist: 0x2b8
+  __DATA_CONST.__const: 0x1da0
+  __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3020
+  __DATA_CONST.__objc_selrefs: 0x3120
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0x2d8
-  __DATA_CONST.__got: 0x8c8
+  __DATA_CONST.__got: 0x978
   __AUTH_CONST.__const: 0x808
-  __AUTH_CONST.__cfstring: 0x34c0
-  __AUTH_CONST.__objc_const: 0x7968
+  __AUTH_CONST.__cfstring: 0x3520
+  __AUTH_CONST.__objc_const: 0x7a80
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x8d0
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x39c
-  __DATA.__data: 0x11d0
+  __AUTH_CONST.__auth_got: 0xaf0
+  __AUTH.__objc_data: 0x3e0
+  __AUTH.__data: 0x28
+  __DATA.__objc_ivar: 0x3a0
+  __DATA.__data: 0x12f4
   __DATA_DIRTY.__objc_data: 0x17c0
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x310

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2050
-  Symbols:   3618
-  CStrings:  856
+  Functions: 2204
+  Symbols:   3665
+  CStrings:  866
 
Symbols:
+ +[HDKeyValueDomain(Medications) hdmd_siriDonationDomainWithProfile:]
+ -[HDMedicationDataDonator _donateWithReason:onlyIfChanged:]
+ -[HDMedicationDataDonator _donationDigestForActiveMedications:profile:]
+ -[HDMedicationDataDonator _itemIdentifierForConcept:]
+ -[HDMedicationDataDonator _lastDonationRecordForProfile:]
+ -[HDMedicationDataDonator _nameForConcept:]
+ -[HDMedicationDataDonator _performDataDonationForProfile:onlyIfChanged:completion:]
+ -[HDMedicationDataDonator _requireUnconditionalDonationOnNextUnlock]
+ -[HDMedicationDataDonator _saveLastDonationWithDigest:osBuild:profile:]
+ -[HDMedicationDataDonator _takeUnconditionalDonationRequiredOnNextUnlock]
+ -[HDMedicationDataDonator unitTesting_performDataDonationIfNeededForProfile:completion:]
+ _AFDeviceSupportsSiriUOD$delayInitStub
+ _OBJC_CLASS_$_HDMedicationDonationRecord
+ _OBJC_CLASS_$_NSNull
+ _OBJC_IVAR_$_HDMedicationDataDonator._unconditionalDonationRequiredOnNextUnlock
+ _OBJC_METACLASS_$_HDMedicationDonationRecord
+ __CLASS_METHODS_HDMedicationDonationRecord
+ __DATA_HDMedicationDonationRecord
+ __INSTANCE_METHODS_HDMedicationDonationRecord
+ __IVARS_HDMedicationDonationRecord
+ __METACLASS_DATA_HDMedicationDonationRecord
+ __PROPERTIES_HDMedicationDonationRecord
+ ___59-[HDMedicationDataDonator _donateWithReason:onlyIfChanged:]_block_invoke
+ ___83-[HDMedicationDataDonator _performDataDonationForProfile:onlyIfChanged:completion:]_block_invoke
+ ___block_descriptor_41_e8_32s_e20_v20?0B8"NSError"12ls32l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e47_v24?0"<HDMedicationsDataStream>"8"NSError"16ls32l8s72l8s40l8s48l8s56l8s64l8
+ ___swift_allocate_boxed_opaque_existential_0
+ __swiftEmptyDictionarySingleton
+ __swift_stdlib_reportUnimplementedInitializer
+ _dlopen
+ _dlopenHelper$AssistantServices
+ _dlopenHelperFlag$AssistantServices
+ _memcmp
+ _objc_allocWithZone
+ _swift_arrayDestroy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_getObjCClassFromMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_getTupleTypeMetadata3
+ _swift_initStackObject
+ _swift_release_x12
+ _swift_release_x20
+ _swift_release_x23
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain
+ _swift_retain_x19
+ _swift_setDeallocating
+ _symbolic _____ 13HealthDomains31MedicationsEscalationEvaluationV
+ _symbolic _____ 13HealthDomains42MedicationInteractionsEscalationEvaluationV
- -[HDMedicationDataDonator _donateWithReason:]
- -[HDMedicationDataDonator _performDataDonationForProfile:completion:]
- ___45-[HDMedicationDataDonator _donateWithReason:]_block_invoke
- ___69-[HDMedicationDataDonator _performDataDonationForProfile:completion:]_block_invoke
- ___block_descriptor_56_e8_32s40s48bs_e47_v24?0"<HDMedicationsDataStream>"8"NSError"16ls32l8s48l8s40l8
- _symbolic _____ 13HealthDomains35MedicationNamesEscalationEvaluationV
CStrings:
+ "/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices"
+ "HDMedicationDataDonatorDonationRequestToken"
+ "HealthMedicationsDaemonPlugin.HDMedicationDonationRecord"
+ "MedicationsLastSiriDonation"
+ "[%{public}@] Medications are unchanged since the last donation. Skipping data donation."
+ "[%{public}@] [Error] Failed to read the last donation: %{public}@"
+ "[%{public}@] [Error] Failed to save the last donation: %{public}@"
+ "com.apple.health.medications.siri-donation"
+ "init()"
+ "pair title details "
```
