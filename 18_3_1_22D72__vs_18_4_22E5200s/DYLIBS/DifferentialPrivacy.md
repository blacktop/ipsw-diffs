## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

```diff

-643.80.4.0.0
-  __TEXT.__text: 0x5f1a8
-  __TEXT.__auth_stubs: 0xf10
-  __TEXT.__objc_methlist: 0x554c
-  __TEXT.__const: 0x850
-  __TEXT.__cstring: 0x2cfdd
-  __TEXT.__oslogstring: 0x408d
-  __TEXT.__gcc_except_tab: 0xd44
+659.100.5.0.0
+  __TEXT.__text: 0x5e000
+  __TEXT.__auth_stubs: 0xee0
+  __TEXT.__objc_methlist: 0x5738
+  __TEXT.__const: 0x7f2
+  __TEXT.__cstring: 0x2ce8d
+  __TEXT.__oslogstring: 0x428d
+  __TEXT.__gcc_except_tab: 0xd80
   __TEXT.__ustring: 0x578
   __TEXT.__dlopen_cstrs: 0x74
   __TEXT.__constg_swiftt: 0x218

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__unwind_info: 0x1840
-  __TEXT.__eh_frame: 0x460
-  __TEXT.__objc_classname: 0xd8f
-  __TEXT.__objc_methname: 0x9edc
-  __TEXT.__objc_methtype: 0x1393
-  __TEXT.__objc_stubs: 0x8100
-  __DATA_CONST.__got: 0x798
-  __DATA_CONST.__const: 0x11f0
-  __DATA_CONST.__objc_classlist: 0x4a8
+  __TEXT.__unwind_info: 0x17d8
+  __TEXT.__eh_frame: 0x548
+  __TEXT.__objc_classname: 0xd2c
+  __TEXT.__objc_methname: 0x99ed
+  __TEXT.__objc_methtype: 0x12e4
+  __TEXT.__objc_stubs: 0x7de0
+  __DATA_CONST.__got: 0x788
+  __DATA_CONST.__const: 0x1130
+  __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24e8
+  __DATA_CONST.__objc_selrefs: 0x24a8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x308
-  __DATA_CONST.__objc_arraydata: 0x4da28
-  __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH_CONST.__auth_ptr: 0x188
+  __DATA_CONST.__objc_superrefs: 0x2e0
+  __DATA_CONST.__objc_arraydata: 0x4da08
+  __AUTH_CONST.__auth_got: 0x788
+  __AUTH_CONST.__auth_ptr: 0x180
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x9e4c0
-  __AUTH_CONST.__objc_const: 0xbc28
-  __AUTH_CONST.__objc_intobj: 0x74958
+  __AUTH_CONST.__cfstring: 0x9e2a0
+  __AUTH_CONST.__objc_const: 0xaa40
+  __AUTH_CONST.__objc_intobj: 0x74988
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xa40
   __AUTH.__data: 0xf0
-  __DATA.__objc_ivar: 0x57c
+  __DATA.__objc_ivar: 0x524
   __DATA.__data: 0x8f8
   __DATA.__bss: 0x740
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x2808
+  __DATA_DIRTY.__objc_data: 0x2678
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x188
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2404
-  Symbols:   3096
-  CStrings:  22714
+  Functions: 2365
+  Symbols:   3051
+  CStrings:  22652
 
Symbols:
+ _NSInternalInconsistencyException
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSNull
+ __DPDediscoVersionWithMetadata
+ _kDPMetadataPrivatizationAlgorithmCache
+ _kDPMetadataPrivatizationAlgorithmParametersCache
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initStructMetadataWithLayoutString
- _CC_SHA256_Final
- _CC_SHA256_Init
- _CC_SHA256_Update
- _OBJC_CLASS_$__DPCMSRandomizer
- _OBJC_CLASS_$__DPCMSSample
- _OBJC_CLASS_$__DPHCMSRandomizer
- _OBJC_CLASS_$__DPHCMSSample
- _OBJC_CLASS_$__DPPrioCountMinSketchValueRandomizer
- _OBJC_METACLASS_$__DPCMSRandomizer
- _OBJC_METACLASS_$__DPCMSSample
- _OBJC_METACLASS_$__DPHCMSRandomizer
- _OBJC_METACLASS_$__DPHCMSSample
- _OBJC_METACLASS_$__DPPrioCountMinSketchValueRandomizer
- _kDPAPPuzzleCount
- _kDPAPcmsFragmentK
- _kDPAPcmsFragmentM
- _kDPAPcmsK
- _kDPAPcmsM
- _kDPAPcmsSequenceFragmentBias
- _kDPAPcmsSequenceK
- _kDPAPcmsSequenceM
- _kDPAPhmbhG
- _kDPPrioCountMinSketchK
- _kDPPrioCountMinSketchM
- _set_bit
- _swift_initStructMetadata
- _uint32_from_string
CStrings:
+ "%@: { propertiesName=%@ ; possibleRange=%@ ; acceptableError=%@ ; trimmedScale=%@ ; noiseDistribution=%@ ; budget=%@ ; privacyParameter=%@ ; transport=%ld ; privatizationAlgorithm=%@ ; submissionPriority=%lu ; parameterDictionary=%@ ;  }"
+ "Expecting v2 metadata but got nil"
+ "Fail to compute minimum batch size for local epsilon=%f"
+ "Fail to infer version from metadata=%@"
+ "Forwarding to delegate randomizer"
+ "Malformed PPM version in donation metadata, error: %@"
+ "Malformed parameter (%@.%@) in metadata, expected numbers, got=%@"
+ "Missing %@ in metadata"
+ "PPM version is not specified in donation metadata. Using default PPM version %@ to upload the donation."
+ "PrivatizationAlgorithmCache"
+ "PrivatizationAlgorithmParametersCache"
+ "Unable to find a matching PPM version from donation metadata's version string: '%@'"
+ "Using PPM compatible version %@ to upload the donation."
+ "Using default dimensionality %lu while forwarding to v2 route"
+ "delegateMetadataFromMetadata:"
+ "delegateRandomizer"
+ "minBatchSize"
+ "privatizationAlgorithmStringFor:"
+ "raise:format:"
+ "shouldForwardToDelegateWithMetadata:"
+ "shouldForwardToV2DelegateWithMetadata:"
+ "v2MetadataFromMetadata:"
+ "v2Randomizer"
- "\"%hu,"
- "%@: { epsilon=%.16g ; m=%ld ; k=%ld ; fragmentEpsilon=%.16g ; fragmentM=%ld ; fragmentK=%ld }"
- "%@: { propertiesName=%@ ; possibleRange=%@ ; acceptableError=%@ ; trimmedScale=%@ ; noiseDistribution=%@ ; budget=%@ ; privacyParameter=%@ ; transport=%ld ; privatizationAlgorithm=%@ ; keyPatternsAllowed=%d ; submissionPriority=%lu ; parameterDictionary=%@ ;  }"
- "%ld,"
- ",%ld,%hu,"
- ",%ld,%hu,%ld,"
- "@40@0:8@16Q24Q32"
- "@40@0:8d16Q24Q32"
- "@44@0:8@16S24@28S36S40"
- "@48@0:8@16Q24d32Q40"
- "@48@0:8@16d24Q32Q40"
- "@56@0:8@16Q24d32Q40Q48"
- "@60@0:8@16S24Q28@36S44Q48S56"
- "@64@0:8d16Q24Q32d40Q48Q56"
- "CountMedianSketch"
- "HadamardCountMedianSketch"
- "Malformed parameter (%@.%@) in metadata, expected numbers."
- "PrioCountMinSketch"
- "SequenceDiscoveryWithPuzzlePiece"
- "SequenceFragmentPuzzle+CountMedianSketch"
- "SequenceFragmentPuzzle+HadamardCountMedianSketch"
- "T@\"NSData\",R,N,V_bitString"
- "TB,R,N,V_keyPatternsAllowed"
- "TQ,R,N,V_bitIndex"
- "TQ,R,N,V_fragmentK"
- "TQ,R,N,V_fragmentM"
- "TQ,R,N,V_hashFunctionIndex"
- "TQ,R,N,V_k"
- "TQ,R,N,V_puzzlePieceCount"
- "Td,R,N,V_fragmentEpsilon"
- "_DPCMSRandomizer"
- "_DPCMSSample"
- "_DPHCMSRandomizer"
- "_DPHCMSSample"
- "_DPPrioCountMinSketchValueRandomizer"
- "_bitIndex"
- "_bitString"
- "_fragmentEpsilon"
- "_fragmentK"
- "_fragmentM"
- "_hashFunctionIndex"
- "_k"
- "_keyPatternsAllowed"
- "_puzzlePieceCount"
- "bitIndex"
- "bitString"
- "cmsSampleForFragment:"
- "cmsSampleForString:"
- "cmsSampleWith:privacyParameter:hashFunctionCount:bitCount:"
- "convertDataToString:"
- "dataFor:hashAtIndex:epsilon:bitCount:bitIndex:"
- "dataFor:hashAtIndex:privacyParameter:bitCount:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:"
- "dataWithCapacity:"
- "decodeObjectForKey:"
- "fragmentEpsilon"
- "fragmentK"
- "fragmentM"
- "g"
- "hashFunctionIndex"
- "hcmsSampleForFragment:"
- "hcmsSampleForString:"
- "hcmsSampleWith:privacyParameter:hashFunctionCount:bitCount:"
- "initWith:privacyParameter:hashFunctionCount:bitCount:"
- "initWithEpsilon:bitCount:hashFunctionCount:"
- "initWithEpsilon:bitCount:hashFunctionCount:fragmentEpsilon:fragmentBitCount:fragmentHashFunctionCount:"
- "jsonStringFrom:hashIndex:"
- "jsonStringFrom:hashIndex:bitIndex:"
- "jsonStringFromSequence:sequenceHashIndex:fragment:fragmentHashIndex:fragmentPosition:"
- "jsonStringFromSequence:sequenceHashIndex:sequencebitIndex:fragment:fragmentHashIndex:fragmentbitIndex:fragmentPosition:"
- "keyPatternsAllowed"
- "puzzleCount"
- "puzzlePieceCount"
- "randomizerWithEpsilon:bitCount:hashFunctionCount:"
- "randomizerWithEpsilon:bitCount:hashFunctionCount:fragmentEpsilon:fragmentBitCount:fragmentHashFunctionCount:"
- "sequenceFragmentBias"
- "sequenceK"
- "sequenceM"
- "unsignedShortValue"

```
