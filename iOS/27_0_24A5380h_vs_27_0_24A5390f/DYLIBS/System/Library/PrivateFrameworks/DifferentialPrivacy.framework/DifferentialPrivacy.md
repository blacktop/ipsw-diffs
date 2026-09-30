## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-791.0.0.0.1
-  __TEXT.__text: 0x4763c
-  __TEXT.__objc_methlist: 0x399c
-  __TEXT.__const: 0x7e8
-  __TEXT.__cstring: 0x402c
-  __TEXT.__oslogstring: 0x2ed9
+793.0.0.0.3
+  __TEXT.__text: 0x499c0
+  __TEXT.__objc_methlist: 0x39d4
+  __TEXT.__const: 0x898
+  __TEXT.__cstring: 0x430c
+  __TEXT.__oslogstring: 0x2faa
   __TEXT.__gcc_except_tab: 0xaac
   __TEXT.__ustring: 0x96
-  __TEXT.__constg_swiftt: 0x318
-  __TEXT.__swift5_typeref: 0x2ac
-  __TEXT.__swift5_fieldmd: 0x390
-  __TEXT.__swift5_reflstr: 0x347
-  __TEXT.__swift5_types: 0x44
+  __TEXT.__constg_swiftt: 0x334
+  __TEXT.__swift5_typeref: 0x2b5
+  __TEXT.__swift5_fieldmd: 0x400
+  __TEXT.__swift5_reflstr: 0x3b7
+  __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_capture: 0x28
-  __TEXT.__unwind_info: 0x10e8
-  __TEXT.__eh_frame: 0x410
+  __TEXT.__unwind_info: 0x1130
+  __TEXT.__eh_frame: 0x508
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1078
+  __DATA_CONST.__const: 0x1098
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d38
+  __DATA_CONST.__objc_selrefs: 0x1d50
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x620
-  __AUTH_CONST.__const: 0x740
-  __AUTH_CONST.__cfstring: 0x3960
-  __AUTH_CONST.__objc_const: 0x73d0
+  __AUTH_CONST.__const: 0x7d0
+  __AUTH_CONST.__cfstring: 0x3ac0
+  __AUTH_CONST.__objc_const: 0x7490
   __AUTH_CONST.__objc_doubleobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x8c0
+  __AUTH_CONST.__auth_got: 0x8c8
   __AUTH.__objc_data: 0x360
-  __DATA.__objc_ivar: 0x330
-  __DATA.__data: 0x9e0
+  __DATA.__objc_ivar: 0x338
+  __DATA.__data: 0x9f8
   __DATA.__bss: 0x670
-  __DATA_DIRTY.__objc_data: 0x22d8
+  __DATA_DIRTY.__objc_data: 0x22e8
   __DATA_DIRTY.__data: 0x1f0
   __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1720
-  Symbols:   3660
-  CStrings:  776
+  Functions: 1743
+  Symbols:   3674
+  CStrings:  788
 
Symbols:
+ -[_DPHistogramWithAggregatorDiscreteGaussian initWithSigma:squaredL2Sensitivity:rappor:error:]
+ -[_DPPreambleBudgetAnalysis initWithBlockSize:numSuperBlocks:dimension:paddedDimension:cohortSigma:sigmaLocal:minBatchSize:error:]
+ -[_DPPreambleBudgetAnalysis minBatchSize]
+ -[_DPPreambleBudgetAnalysis sigmaLocal]
+ _OBJC_IVAR_$__DPPreambleBudgetAnalysis._minBatchSize
+ _OBJC_IVAR_$__DPPreambleBudgetAnalysis._sigmaLocal
+ ___130-[_DPPreambleBudgetAnalysis initWithBlockSize:numSuperBlocks:dimension:paddedDimension:cohortSigma:sigmaLocal:minBatchSize:error:]_block_invoke
+ _initWithBlockSize:numSuperBlocks:dimension:paddedDimension:cohortSigma:sigmaLocal:minBatchSize:error:.onceToken
+ _kDPMetadataDediscoTaskConfigDPConfigMechanismDiscreteGaussianWithZeroConcentratedDpAccountant
+ _kTokenFieldNotBefore
+ _lgamma
+ _objc_msgSend$initWithBlockSize:numSuperBlocks:dimension:paddedDimension:cohortSigma:sigmaLocal:minBatchSize:error:
+ _objc_msgSend$initWithSigma:squaredL2Sensitivity:rappor:error:
+ _objc_msgSend$integerScalingFactor
+ _objc_msgSend$numVectors
+ _symbolic SSm
+ _symbolic _____ 19DifferentialPrivacy43PreambleProofWithOneHotBlockEngineParameterV
+ _type_layout_string 19DifferentialPrivacy43PreambleProofWithOneHotBlockEngineParameterV
- -[_DPPreambleBudgetAnalysis initWithBlockSize:numSuperBlocks:dimension:paddedDimension:cohortSigma:error:]
- ___106-[_DPPreambleBudgetAnalysis initWithBlockSize:numSuperBlocks:dimension:paddedDimension:cohortSigma:error:]_block_invoke
- _initWithBlockSize:numSuperBlocks:dimension:paddedDimension:cohortSigma:error:.onceToken
- _objc_msgSend$initWithBlockSize:numSuperBlocks:dimension:paddedDimension:cohortSigma:error:
CStrings:
+ "DistributedDiscreteGaussianWithZeroConcentratedDpAccountantForPreambleProof"
+ "Malformed parameter (%@) in metadata DPConfig expected a number."
+ "Malformed parameter (%@) in metadata PreambleParameters, expected a number."
+ "Malformed parameter (%@) in metadata taskConfig, expected a number."
+ "Precomputed minSigma bound %.17g exceeds cohortSigma %.17g"
+ "Unsupported DP mechanism (%@) in metadata DPConfig."
+ "delta %.17g exceeds target %.17g for Gaussian noise when numBlocks %u == numSuperBlocks %u"
+ "failureProb >= %.17g which exceeds maxFailureProb %.17g"
+ "minBatchSize must be positive."
+ "minSamplesNeeded %f > expectedNumSamples %f, i.e., Pr[Bin(minBatchSize, gamma) < minSamplesNeeded] exceeds 0.5"
+ "notBefore"
+ "sigmaLocal %.17g >= cohortSigma %.17g. In this case, for the preamble algorithm with random allocation accountant, every client will add enough noise to guarantee central DP for the coordinates it donates to."
+ "sigmaLocal = %.17g and minBatchSize = %u achieve actualCohortSigma = %.17g which is lower than the target cohortSigma = %.17g when sampling rate is 100%%"
+ "sigmaLocal must be finite, non NaN, and positive."
+ "squaredL2Sensitivity must be finite, not NAN, and greater than 0.0."
- "Malformed parameter (%@) in metadata PreambleParameters expected a number."
- "Precomputed minSigma bound %f exceeds cohortSigma %f"
- "delta %f exceeds minDelta bound %f for Gaussian noise when numBlocks %u == numSuperBlocks %u"
```
