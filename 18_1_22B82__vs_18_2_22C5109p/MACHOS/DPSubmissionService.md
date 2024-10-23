## DPSubmissionService

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/XPCServices/DPSubmissionService.xpc/DPSubmissionService`

```diff

-618.40.2.0.0
-  __TEXT.__text: 0x51458
-  __TEXT.__auth_stubs: 0x1050
-  __TEXT.__objc_stubs: 0x2f20
-  __TEXT.__objc_methlist: 0x10b0
-  __TEXT.__const: 0x27a8
-  __TEXT.__cstring: 0x2950
-  __TEXT.__objc_methname: 0x391b
+640.0.0.0.1
+  __TEXT.__text: 0x547ac
+  __TEXT.__auth_stubs: 0x1060
+  __TEXT.__objc_stubs: 0x3040
+  __TEXT.__objc_methlist: 0x10f0
+  __TEXT.__const: 0x2838
+  __TEXT.__cstring: 0x2a60
+  __TEXT.__objc_methname: 0x3b62
   __TEXT.__objc_classname: 0x331
   __TEXT.__objc_methtype: 0xa41
-  __TEXT.__oslogstring: 0x1336
+  __TEXT.__oslogstring: 0x1333
   __TEXT.__gcc_except_tab: 0x268
-  __TEXT.__swift5_typeref: 0x890
-  __TEXT.__swift5_fieldmd: 0x133c
-  __TEXT.__constg_swiftt: 0xd6c
-  __TEXT.__swift5_reflstr: 0x14a3
+  __TEXT.__swift5_typeref: 0x89e
+  __TEXT.__swift5_fieldmd: 0x1460
+  __TEXT.__constg_swiftt: 0xd88
+  __TEXT.__swift5_reflstr: 0x1753
   __TEXT.__swift5_capture: 0x24
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__swift5_proto: 0x2f8
-  __TEXT.__swift5_types: 0x16c
-  __TEXT.__swift5_assocty: 0x5a0
+  __TEXT.__swift5_proto: 0x300
+  __TEXT.__swift5_types: 0x170
+  __TEXT.__swift5_assocty: 0x5b8
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x1e68
-  __TEXT.__eh_frame: 0x4158
-  __DATA_CONST.__auth_got: 0x838
-  __DATA_CONST.__got: 0x4b0
-  __DATA_CONST.__auth_ptr: 0x310
-  __DATA_CONST.__const: 0x2cd8
-  __DATA_CONST.__cfstring: 0x1700
+  __TEXT.__unwind_info: 0x1ee8
+  __TEXT.__eh_frame: 0x4300
+  __DATA_CONST.__auth_got: 0x840
+  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__auth_ptr: 0x318
+  __DATA_CONST.__const: 0x2df0
+  __DATA_CONST.__cfstring: 0x1720
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa8
-  __DATA_CONST.__objc_intobj: 0xa8
-  __DATA_CONST.__objc_arraydata: 0x48
+  __DATA_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__objc_arraydata: 0x68
+  __DATA_CONST.__objc_arrayobj: 0x60
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x2a18
-  __DATA.__objc_selrefs: 0xd10
+  __DATA.__objc_selrefs: 0xd58
   __DATA.__objc_ivar: 0x100
   __DATA.__objc_data: 0xe78
-  __DATA.__data: 0x23f0
-  __DATA.__bss: 0x58b0
+  __DATA.__data: 0x2458
+  __DATA.__bss: 0x59d0
   __DATA.__common: 0x140
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2431
-  Symbols:   341
-  CStrings:  1145
+  Functions: 2481
+  Symbols:   359
+  CStrings:  1158
 
Symbols:
+ _OBJC_CLASS_$__DPCoreAnalyticsCollector
+ __DPCoreAnalyticsEvent_PhaseCount
+ __DPCoreAnalyticsField_Counts
+ __DPCoreAnalyticsField_Phase
+ __DPCoreAnalyticsField_Status
+ __DPCoreAnalyticsField_TaskName
+ __DPMetadataIsV2
+ ___kCFBooleanTrue
+ _kDPMetadataDPConfigCohortSigma
+ _kDPMetadataDPConfigMaxCohortSize
+ _kDPMetadataDPConfigNumIterations
+ _kDPMetadataDPConfigPopulationSize
+ _kDPMetadataDPConfigRenyiOrder
+ _kDPMetadataDPConfigSigmaAfterNormalizing
+ _kDPMetadataDPConfigSquaredL2Sensitivity
+ _kDPMetadataDediscoTaskConfigDPConfigMechanismGaussianWithSubsampledMomentsAccountant
+ _kDPMetadataDediscoTaskConfigDPConfigMechanismNone
+ _kDPMetadataPINEChunkLengthNormEquality
+ _kDPMetadataPINEFractionalBitCount
+ _kDPMetadataPINEL2NormBoundInt
+ _kDPPINEWraparoundCheckCount
- _kDPMetadataDediscoTaskConfigDPConfigSquaredL2Sensitivity
- _kDPMetadataPINEL2NormBound
- _kDPPINEFractionalBitCount
CStrings:
+ "@64@0:8Q16I24I28I32I36C40S44@48^@56"
+ "@80@0:8Q16I24Q28I36d40d48d56d64^@72"
+ "Bypassing SGX for collectionID %!@(MISSING) - Sending DAP report only"
+ "Incorrect data type for %!@(MISSING).%!@(MISSING) - expect dictionary"
+ "Property for case `distributed_gaussian_with_subsampled_moments_accountant` is nil."
+ "Property for case `pine_field32_hmac_sha256_aes128` is nil."
+ "Unknown VDAFType = %!@(MISSING)."
+ "containsObject:"
+ "defaultValueForKey:"
+ "donateEventToBitacoraForKey:eventPhase:uuid:succeeded:errorCode:errorMessage:aggregateFunction:count:telemetryAllowed:"
+ "encodedGaussianWithSubsampledMomentsAccountantConfigWithMaxCohortSize:numIterations:populationSize:renyiOrder:sigma:sigmaAfterNormalization:targetCentralEpsilon:targetCentralDelta:error:"
+ "encodedNoneDPConfigAndReturnError:"
+ "encodedPINE32VDAFConfigWithL2NormBound:numFractionalBits:length:chunkLength:chunkLengthNormEquality:numProofs:wraparoundCheckCount:encodedDPConfig:error:"
+ "encodedPINE64VDAFConfigWithL2NormBound:numFractionalBits:length:chunkLength:chunkLengthNormEquality:numProofs:wraparoundCheckCount:encodedDPConfig:error:"
+ "fedstats:com.apple.Bitacora.TokenFetcher:000:000:iOS"
+ "reportMetricsForEvent:withMetrics:"
+ "setWithArray:"
+ "unsignedLongValue"
+ "validatePINEParametersWithError:"
- "@52@0:8f16I20I24I28C32@36^@44"
- "Bypassing SGX for V2 collectionID %!@(MISSING) - Sending DAP report only"
- "Unknown VDAFType = %!l(MISSING)u."
- "donateEventToBitacoraForKey:eventPhase:uuid:succeeded:errorCode:errorMessage:telemetryAllowed:"
- "encodedPINEVDAFConfigWithL2NormBound:numFractionalBits:length:chunkLength:numProofs:encodedDPConfig:error:"
- "fedstats:com.apple.Bitacora.TokenFetcher:000:000:000"

```
