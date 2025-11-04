## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

```diff

-684.40.8.0.0
-  __TEXT.__text: 0x5fa24
-  __TEXT.__auth_stubs: 0x1170
-  __TEXT.__objc_methlist: 0x585c
+684.60.1.0.5
+  __TEXT.__text: 0x5fc30
+  __TEXT.__auth_stubs: 0x1180
+  __TEXT.__objc_methlist: 0x588c
   __TEXT.__const: 0x9e8
-  __TEXT.__cstring: 0x493c
+  __TEXT.__cstring: 0x4a0c
   __TEXT.__oslogstring: 0x431f
-  __TEXT.__gcc_except_tab: 0xd80
+  __TEXT.__gcc_except_tab: 0xd14
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x74
   __TEXT.__constg_swiftt: 0x300

   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__unwind_info: 0x18a0
+  __TEXT.__unwind_info: 0x18c0
   __TEXT.__eh_frame: 0x858
   __TEXT.__objc_classname: 0xd7f
-  __TEXT.__objc_methname: 0x9c77
-  __TEXT.__objc_methtype: 0x129c
-  __TEXT.__objc_stubs: 0x7e40
+  __TEXT.__objc_methname: 0x9d45
+  __TEXT.__objc_methtype: 0x12be
+  __TEXT.__objc_stubs: 0x7ee0
   __DATA_CONST.__got: 0x810
-  __DATA_CONST.__const: 0x11a8
+  __DATA_CONST.__const: 0x1210
   __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24e8
+  __DATA_CONST.__objc_selrefs: 0x2510
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x2e8
-  __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x8d0
+  __DATA_CONST.__objc_arraydata: 0x108
+  __AUTH_CONST.__auth_got: 0x8d8
   __AUTH_CONST.__const: 0x7a0
-  __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0xadf8
+  __AUTH_CONST.__cfstring: 0x40c0
+  __AUTH_CONST.__objc_const: 0xae28
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xe70
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0x530
+  __DATA.__objc_ivar: 0x534
   __DATA.__data: 0x9d0
   __DATA.__bss: 0x950
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E2BAA5CE-0127-37AD-A0D3-005508469BE4
-  Functions: 2436
-  Symbols:   7702
-  CStrings:  3540
+  UUID: 60CB0D08-5717-3A23-A951-CF31D9C248B5
+  Functions: 2441
+  Symbols:   7731
+  CStrings:  3564
 
Symbols:
+ +[_DPPrivacyBudget creditUnsafe:budgetWithName:]
+ +[_DPPrivacyBudget debitUnsafe:budgetWithName:]
+ +[_DPPrivacyBudget enforceSimpleBudgetForRecords:withKey:inDatabase:].cold.2
+ +[_DPPrivacyBudget updateBudgetForRecords:withKey:refundAmount:inDatabase:]
+ +[_DPPrivacyBudget updateEnhancedBudgetForRecords:withKey:refundAmount:inDatabase:]
+ +[_DPPrivacyBudget updateSimpleBudgetForRecords:withKey:refundAmount:inDatabase:]
+ -[_DPDiagnosticsAndUsageTransparencyLog shouldHideMPCParameters]
+ -[_DPPrivacyBudget initializeBudgetRecordUnsafeFrom:]
+ -[_DPPrivacyBudget maxBalance]
+ GCC_except_table21
+ GCC_except_table28
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table37
+ _OBJC_IVAR_$__DPDiagnosticsAndUsageTransparencyLog._shouldHideMPCParameters
+ ___assert_rtn
+ ___block_literal_global.204
+ ___block_literal_global.206
+ ___block_literal_global.208
+ ___block_literal_global.210
+ _kCollectionExcludingPrefixes
+ _kDPMetadataPINEWraparoundCheckCount
+ _kDPMetadataVDAFNumOfProofs
+ _kDPMetadataVDAFPrio3SumVectorBitWidth
+ _kDiagnosticsAndUsageTransparencyLogCollection
+ _kDiagnosticsAndUsageTransparencyLogDataSource
+ _kDiagnosticsAndUsageTransparencyLogDimension
+ _kDiagnosticsAndUsageTransparencyLogMetadata
+ _kDiagnosticsAndUsageTransparencyLogNoisedData
+ _kDiagnosticsAndUsageTransparencyLogSecretShare1
+ _kDiagnosticsAndUsageTransparencyLogSecretShare2
+ _kDiagnosticsAndUsageTransparencyLogServerAlgorithm
+ _kPrivateEvolutionReportName
+ _objc_msgSend$creditUnsafe:budgetWithName:
+ _objc_msgSend$debitUnsafe:budgetWithName:
+ _objc_msgSend$initializeBudgetRecordUnsafeFrom:
+ _objc_msgSend$maxBalance
+ _objc_msgSend$shouldHideMPCParameters
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$updateBudgetForRecords:withKey:refundAmount:inDatabase:
+ _objc_msgSend$updateEnhancedBudgetForRecords:withKey:refundAmount:inDatabase:
+ _objc_msgSend$updateSimpleBudgetForRecords:withKey:refundAmount:inDatabase:
- +[_DPPrivacyBudget updateBudgetForRecords:withKey:inDatabase:]
- +[_DPPrivacyBudget updateEnhancedBudgetForRecords:withKey:inDatabase:]
- +[_DPPrivacyBudget updateSimpleBudgetForRecords:withKey:inDatabase:]
- -[_DPDiagnosticsAndUsageTransparencyLog filterMetadataFieldsInSimplifiedLog:]
- GCC_except_table15
- ___block_literal_global.195
- ___block_literal_global.197
- ___block_literal_global.199
- ___block_literal_global.201
- _objc_msgSend$filterMetadataFieldsInSimplifiedLog:
- _objc_msgSend$updateBudgetForRecords:withKey:inDatabase:
- _objc_msgSend$updateEnhancedBudgetForRecords:withKey:inDatabase:
- _objc_msgSend$updateSimpleBudgetForRecords:withKey:inDatabase:
CStrings:
+ "+[_DPPrivacyBudget enforceSimpleBudgetForRecords:withKey:inDatabase:]"
+ "PrivateEvolution"
+ "TB,R,N,V_shouldHideMPCParameters"
+ "_DPPrivacyBudget.m"
+ "_shouldHideMPCParameters"
+ "allowedCount == (int64_t)recordsToSubmit.count"
+ "collection"
+ "creditUnsafe:budgetWithName:"
+ "debitUnsafe:budgetWithName:"
+ "fedstats:"
+ "initializeBudgetRecordUnsafeFrom:"
+ "maxBalance"
+ "pfl:"
+ "secretShare1"
+ "secretShare2"
+ "shouldHideMPCParameters"
+ "substringFromIndex:"
+ "updateBudgetForRecords:withKey:refundAmount:inDatabase:"
+ "updateEnhancedBudgetForRecords:withKey:refundAmount:inDatabase:"
+ "updateSimpleBudgetForRecords:withKey:refundAmount:inDatabase:"
+ "v32@0:8Q16@24"
+ "v48@0:8@16@24Q32@40"
- "filterMetadataFieldsInSimplifiedLog:"
- "updateBudgetForRecords:withKey:inDatabase:"
- "updateEnhancedBudgetForRecords:withKey:inDatabase:"
- "updateSimpleBudgetForRecords:withKey:inDatabase:"

```
