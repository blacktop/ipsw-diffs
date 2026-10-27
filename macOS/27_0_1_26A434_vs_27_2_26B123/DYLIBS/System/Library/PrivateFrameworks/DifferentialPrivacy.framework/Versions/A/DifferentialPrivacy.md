## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/Versions/A/DifferentialPrivacy`

```diff

-796.0.0.0.0
-  __TEXT.__text: 0x4d9a0
-  __TEXT.__objc_methlist: 0x3984
+800.0.0.0.0
+  __TEXT.__text: 0x4ed38
+  __TEXT.__objc_methlist: 0x3a4c
   __TEXT.__const: 0x8b8
-  __TEXT.__cstring: 0x433c
+  __TEXT.__cstring: 0x45cc
   __TEXT.__oslogstring: 0x309e
   __TEXT.__gcc_except_tab: 0xa40
   __TEXT.__ustring: 0x96
   __TEXT.__constg_swiftt: 0x334
-  __TEXT.__swift5_typeref: 0x2b5
-  __TEXT.__swift5_fieldmd: 0x400
-  __TEXT.__swift5_reflstr: 0x3b7
+  __TEXT.__swift5_typeref: 0x315
+  __TEXT.__swift5_fieldmd: 0x430
+  __TEXT.__swift5_reflstr: 0x427
   __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__unwind_info: 0x11c8
-  __TEXT.__eh_frame: 0x508
+  __TEXT.__unwind_info: 0x11e8
+  __TEXT.__eh_frame: 0x548
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x7e0
-  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d18
+  __DATA_CONST.__objc_selrefs: 0x1d40
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x78
-  __DATA_CONST.__got: 0x608
+  __DATA_CONST.__got: 0x628
   __AUTH_CONST.__const: 0x1120
-  __AUTH_CONST.__cfstring: 0x3a80
-  __AUTH_CONST.__objc_const: 0x7490
+  __AUTH_CONST.__cfstring: 0x3b60
+  __AUTH_CONST.__objc_const: 0x77f8
   __AUTH_CONST.__objc_doubleobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x7b8
+  __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x360
-  __DATA.__objc_ivar: 0x338
-  __DATA.__data: 0x9f0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x360
+  __DATA.__data: 0x2e8
   __DATA.__bss: 0x640
-  __DATA_DIRTY.__objc_data: 0x22e8
-  __DATA_DIRTY.__data: 0x1f8
+  __DATA_DIRTY.__objc_data: 0x2648
+  __DATA_DIRTY.__data: 0x900
   __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1770
-  Symbols:   3693
-  CStrings:  795
+  Functions: 1785
+  Symbols:   3738
+  CStrings:  807
 
Symbols:
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis .cxx_destruct]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis blockSize]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis cohortAnalysis]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis cohortSigma]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis dimension]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis exceedApproximateDPBudget:error:]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis initWithCohortSigma:sigmaLocal:squaredL2Sensitivity:blockSize:dimension:minBatchSize:error:]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis initWithCohortSigma:sigmaLocal:squaredL2Sensitivity:blockSize:numKeptBlocks:dimension:minBatchSize:error:]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis minBatchSize]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis numKeptBlocks]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis numLeafNodes]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis paddedDimension]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis sigmaLocal]
+ -[_DPPreambleProofOneHotBlockBudgetAnalysis squaredL2Sensitivity]
+ -[_DPPreambleProofOneHotBlockBudgetAuditor initWithMetadata:plistParameters:error:]
+ OBJC_IVAR_$__DPPreambleProofOneHotBlockBudgetAnalysis._blockSize
+ OBJC_IVAR_$__DPPreambleProofOneHotBlockBudgetAnalysis._cohortAnalysis
+ OBJC_IVAR_$__DPPreambleProofOneHotBlockBudgetAnalysis._cohortSigma
+ OBJC_IVAR_$__DPPreambleProofOneHotBlockBudgetAnalysis._dimension
+ OBJC_IVAR_$__DPPreambleProofOneHotBlockBudgetAnalysis._minBatchSize
+ OBJC_IVAR_$__DPPreambleProofOneHotBlockBudgetAnalysis._numKeptBlocks
+ OBJC_IVAR_$__DPPreambleProofOneHotBlockBudgetAnalysis._numLeafNodes
+ OBJC_IVAR_$__DPPreambleProofOneHotBlockBudgetAnalysis._paddedDimension
+ OBJC_IVAR_$__DPPreambleProofOneHotBlockBudgetAnalysis._sigmaLocal
+ OBJC_IVAR_$__DPPreambleProofOneHotBlockBudgetAnalysis._squaredL2Sensitivity
+ _OBJC_CLASS_$__DPPreambleProofOneHotBlockBudgetAnalysis
+ _OBJC_CLASS_$__DPPreambleProofOneHotBlockBudgetAuditor
+ _OBJC_METACLASS_$__DPPreambleProofOneHotBlockBudgetAnalysis
+ _OBJC_METACLASS_$__DPPreambleProofOneHotBlockBudgetAuditor
+ __OBJC_$_INSTANCE_METHODS__DPPreambleProofOneHotBlockBudgetAnalysis
+ __OBJC_$_INSTANCE_METHODS__DPPreambleProofOneHotBlockBudgetAuditor
+ __OBJC_$_INSTANCE_VARIABLES__DPPreambleProofOneHotBlockBudgetAnalysis
+ __OBJC_$_PROP_LIST__DPPreambleProofOneHotBlockBudgetAnalysis
+ __OBJC_CLASS_PROTOCOLS_$__DPPreambleProofOneHotBlockBudgetAnalysis
+ __OBJC_CLASS_RO_$__DPPreambleProofOneHotBlockBudgetAnalysis
+ __OBJC_CLASS_RO_$__DPPreambleProofOneHotBlockBudgetAuditor
+ __OBJC_METACLASS_RO_$__DPPreambleProofOneHotBlockBudgetAnalysis
+ __OBJC_METACLASS_RO_$__DPPreambleProofOneHotBlockBudgetAuditor
+ _objc_msgSend$cohortAnalysis
+ _objc_msgSend$initWithCohortSigma:sigmaLocal:squaredL2Sensitivity:blockSize:numKeptBlocks:dimension:minBatchSize:error:
+ _objc_msgSend$numLeafNodes
+ _symbolic Sd10noiseSigma_Sd5limitt
+ _symbolic Sd5value_Sd5limitt
+ _symbolic Si11measurement_t
+ _symbolic _____13scalingFactor_AA5limitt s6UInt64V
CStrings:
+ " exceeds integer range limit "
+ " exceeds maximum allowed integer limit "
+ " exceeds safe headroom limit "
+ " is negative, index must be >= 0."
+ "Failed to initialize one-hot-block budget analysis from metadata parameters:"
+ "Noise standard deviation "
+ "blockSize must not be zero."
+ "cohortSigma must be finite, not NAN, and greater than 0.0."
+ "numKeptBlocks must not be zero."
+ "samplesNeeded < 1: fewer than one client would add noise per block."
+ "sigmaLocal = %.17g and minBatchSize = %u achieve actualCohortSigma = %.17g which is lower than the target cohortSigma = %.17g when sampling rate is 100%%."
+ "sigmaLocal must be finite, not NAN, and greater than 0.0."
```
