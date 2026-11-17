## HealthRecordsPlugin

> `/System/Library/PrivateFrameworks/HealthRecordsPlugin.framework/HealthRecordsPlugin`

```diff

-7027.2.13.0.0
-  __TEXT.__text: 0xcc820
-  __TEXT.__objc_methlist: 0x7a44
+7027.2.519.2.2
+  __TEXT.__text: 0xce480
+  __TEXT.__objc_methlist: 0x7a9c
   __TEXT.__const: 0xfc0
-  __TEXT.__cstring: 0x9c7f
-  __TEXT.__oslogstring: 0x10b07
+  __TEXT.__cstring: 0x9cdf
+  __TEXT.__oslogstring: 0x10ae7
   __TEXT.__gcc_except_tab: 0x1978
   __TEXT.__ustring: 0x7e
-  __TEXT.__swift5_typeref: 0x781
-  __TEXT.__swift5_capture: 0x574
+  __TEXT.__swift5_typeref: 0x7b9
+  __TEXT.__swift5_capture: 0x5b8
   __TEXT.__constg_swiftt: 0x4d4
   __TEXT.__swift5_reflstr: 0x2b3
   __TEXT.__swift5_fieldmd: 0x36c

   __TEXT.__swift_as_ret: 0x60
   __TEXT.__swift_as_cont: 0xc4
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__unwind_info: 0x39a8
-  __TEXT.__eh_frame: 0x1428
+  __TEXT.__unwind_info: 0x3a00
+  __TEXT.__eh_frame: 0x1458
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x2fa0
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x120
-  __DATA_CONST.__objc_protolist: 0x130
+  __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5440
-  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x5470
+  __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x2d8
   __DATA_CONST.__objc_arraydata: 0x150
-  __DATA_CONST.__got: 0x1428
-  __AUTH_CONST.__const: 0x1a58
-  __AUTH_CONST.__cfstring: 0x6960
-  __AUTH_CONST.__objc_const: 0xbad0
+  __DATA_CONST.__got: 0x1468
+  __AUTH_CONST.__const: 0x1b68
+  __AUTH_CONST.__cfstring: 0x6940
+  __AUTH_CONST.__objc_const: 0xbb28
   __AUTH_CONST.__objc_intobj: 0x4f8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__auth_got: 0xf90
+  __AUTH_CONST.__auth_got: 0xfc8
   __AUTH.__objc_data: 0x18f0
   __AUTH.__data: 0x278
   __DATA.__objc_ivar: 0x5e4
-  __DATA.__data: 0x1008
+  __DATA.__data: 0x1080
   __DATA_DIRTY.__objc_data: 0x1420
   __DATA_DIRTY.__data: 0x578
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3909
-  Symbols:   5667
-  CStrings:  1844
+  Functions: 3938
+  Symbols:   5672
+  CStrings:  1847
 
Symbols:
+ -[HDHealthRecordsProfileExtension requestMedicalHistoryClinicalRecordDerivation]
+ GCC_except_table117
+ GCC_except_table191
+ _HDClinicalRecordEntityPropertyOriginalMHRecordROWID
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_IVAR_$_HDHealthRecordsProfileExtension._medicalHistoryDerivationManager
+ __OBJC_$_INSTANCE_METHODS_HDMedicalHistoryDerivationManager(HealthRecordsPlugin)
+ __OBJC_CLASS_PROTOCOLS_$_HDMedicalHistoryDerivationManager(HealthRecordsPlugin)
+ ___128-[HDClinicalAccountEntity(HealthRecordsPlugin) deleteCredentialWithProfile:transaction:deleteTokens:credentialIdentifier:error:]_block_invoke
+ _swift_retain_x8
+ _symbolic Ieg_
+ _symbolic IeyB_
+ _symbolic So33HDMedicalHistoryDerivationManagerCSgXw
- -[HDHealthRecordsProfileExtension _enqueueMedicalHistoryClinicalRecordDerivationWithManager:]
- GCC_except_table116
- GCC_except_table190
- _OBJC_IVAR_$_HDHealthRecordsProfileExtension._medicalHistoryDerivationScheduled
- __INSTANCE_METHODS_HDMedicalHistoryDerivationManager
- ___106-[HDHealthRecordsProfileExtension scheduleMedicalHistoryClinicalRecordDerivationAfterCommitOfTransaction:]_block_invoke
- ___93-[HDHealthRecordsProfileExtension _enqueueMedicalHistoryClinicalRecordDerivationWithManager:]_block_invoke
- ___93-[HDHealthRecordsProfileExtension _enqueueMedicalHistoryClinicalRecordDerivationWithManager:]_block_invoke_2
CStrings:
+ "%@ completed derivation of clinical records"
+ "%@ derivation already pending, not queuing another"
+ "%@ failed to derive clinical records: %s"
+ "%@ found no medical history records without a derived clinical record"
+ "%@ has no maintenance work coordinator, cannot derive clinical records"
+ "%@ has no profile, cannot derive clinical records"
+ "%@ scheduling derivation of clinical records"
+ "%@ skipping %s, it already has a derived clinical record"
+ "HDMedicalHistoryDerivationManager.observer"
+ "NOT EXISTS (SELECT 1 FROM "
- "$."
- "%@ found no self-entered lab results to derive from"
- "%{public}@: Completed derivation of clinical records for medical history records"
- "%{public}@: Failed to derive clinical records for medical history records: %{private}@"
- "%{public}@: No maintenance work coordinator, cannot derive clinical records for medical history records"
- "%{public}@: No medical history derivation manager, not deriving clinical records for medical history records"
- "%{public}@: Scheduling derivation of clinical records for medical history records"
```
