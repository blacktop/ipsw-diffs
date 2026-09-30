## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

```diff

-684.0.14.0.0
-  __TEXT.__text: 0x63624
-  __TEXT.__auth_stubs: 0x11b0
-  __TEXT.__objc_methlist: 0x59bc
-  __TEXT.__const: 0xae0
-  __TEXT.__cstring: 0x48cd
-  __TEXT.__oslogstring: 0x43c1
+684.0.20.0.2
+  __TEXT.__text: 0x5de74
+  __TEXT.__auth_stubs: 0x11a0
+  __TEXT.__objc_methlist: 0x582c
+  __TEXT.__const: 0x940
+  __TEXT.__cstring: 0x484d
+  __TEXT.__oslogstring: 0x42eb
   __TEXT.__gcc_except_tab: 0xd80
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x74

   __TEXT.__constg_swiftt: 0x300
   __TEXT.__swift5_reflstr: 0x2ed
   __TEXT.__swift5_fieldmd: 0x2fc
-  __TEXT.__swift5_capture: 0x40
+  __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x40
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x1920
+  __TEXT.__unwind_info: 0x1878
   __TEXT.__eh_frame: 0x770
-  __TEXT.__objc_classname: 0xd95
-  __TEXT.__objc_methname: 0x9e05
-  __TEXT.__objc_methtype: 0x12fc
-  __TEXT.__objc_stubs: 0x7f80
-  __DATA_CONST.__got: 0x818
-  __DATA_CONST.__const: 0x1198
-  __DATA_CONST.__objc_classlist: 0x4a8
+  __TEXT.__objc_classname: 0xd7f
+  __TEXT.__objc_methname: 0x9c0d
+  __TEXT.__objc_methtype: 0x129c
+  __TEXT.__objc_stubs: 0x7e00
+  __DATA_CONST.__got: 0x810
+  __DATA_CONST.__const: 0x1190
+  __DATA_CONST.__objc_classlist: 0x4a0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2550
+  __DATA_CONST.__objc_selrefs: 0x24d0
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x2f0
-  __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x8f0
-  __AUTH_CONST.__const: 0x7f0
-  __AUTH_CONST.__cfstring: 0x4080
-  __AUTH_CONST.__objc_const: 0xb020
-  __AUTH_CONST.__objc_intobj: 0x3c0
+  __DATA_CONST.__objc_superrefs: 0x2e8
+  __DATA_CONST.__objc_arraydata: 0xe8
+  __AUTH_CONST.__auth_got: 0x8e8
+  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__cfstring: 0x3fe0
+  __AUTH_CONST.__objc_const: 0xad68
+  __AUTH_CONST.__objc_intobj: 0x3a8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xe58
   __AUTH.__data: 0x168
-  __DATA.__objc_ivar: 0x554
+  __DATA.__objc_ivar: 0x530
   __DATA.__data: 0x998
   __DATA.__bss: 0x950
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x2538
+  __DATA_DIRTY.__objc_data: 0x24e8
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x188
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 02DF2984-9AB8-34E1-B594-D9548F47696B
-  Functions: 2511
-  Symbols:   7858
-  CStrings:  3569
+  UUID: A3CEB7C3-163A-3C4A-AB11-6D24F24A14E0
+  Functions: 2420
+  Symbols:   7692
+  CStrings:  3522
 
Symbols:
+ +[_DPKeyProperties parametersForAlgorithm:properties:epsilon:]
+ -[_DPServer donateEventToCoreAnalytics:succeeded:count:]
+ -[_DPServer recordWords:forKey:withReply:].cold.1
+ ___61-[_DPPreambleRandomizer randomizeBitVectors:metadata:forKey:]_block_invoke.cold.3
+ ___block_literal_global.193
+ _objc_msgSend$donateEventToCoreAnalytics:succeeded:count:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$parametersForAlgorithm:properties:epsilon:
+ _objc_msgSend$shard:metaData:dimension:error:
- +[_DPKeyProperties parametersForAlgorithm:properties:epsilon:fragmentWidth:]
- +[_DPPTValueRandomizer randomizerWithEpsilon:numberOfGroups:]
- -[_DPBitValueRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPDataRecorder bitStringAlgorithm]
- -[_DPDataRecorder fragmentWidth]
- -[_DPDatabaseRecorder recordWords:].cold.2
- -[_DPDatabaseRecorder recordWords:].cold.3
- -[_DPDatabaseRecorder recordWords:].cold.4
- -[_DPDatabaseRecorder recordWords:].cold.5
- -[_DPDatabaseRecorder recordWords:].cold.6
- -[_DPKeyProperties bitStringAlgorithm]
- -[_DPKeyProperties fragmentWidth]
- -[_DPNumberRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPOBHRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPOHEBitValueRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPPTValueRandomizer bucketCount]
- -[_DPPTValueRandomizer chancePMinusQ]
- -[_DPPTValueRandomizer epsilon]
- -[_DPPTValueRandomizer initWithEpsilon:numberOfGroups:]
- -[_DPPTValueRandomizer init]
- -[_DPPTValueRandomizer mask]
- -[_DPPTValueRandomizer numGroups]
- -[_DPPTValueRandomizer randomize:]
- -[_DPPTValueRandomizer randomizeBitValues:forKey:]
- -[_DPPTValueRandomizer randomizeStrings:forKey:]
- -[_DPPTValueRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPPTValueRandomizer setBucketCount:]
- -[_DPPTValueRandomizer setChancePMinusQ:]
- -[_DPPTValueRandomizer setEpsilon:]
- -[_DPPTValueRandomizer setMask:]
- -[_DPPTValueRandomizer setNumGroups:]
- -[_DPPrioPiRapporValueRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPPrioPlusPlusMetadataValueRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPPrioPlusPlusMetricsValueRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPPrioPlusPlusValueRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPPrioValueRandomizer randomizeWords:fragmentWidth:forKey:]
- _OBJC_CLASS_$__DPPTValueRandomizer
- _OBJC_IVAR_$__DPDataRecorder._bitStringAlgorithm
- _OBJC_IVAR_$__DPDataRecorder._fragmentWidth
- _OBJC_IVAR_$__DPKeyProperties._bitStringAlgorithm
- _OBJC_IVAR_$__DPKeyProperties._fragmentWidth
- _OBJC_IVAR_$__DPPTValueRandomizer._bucketCount
- _OBJC_IVAR_$__DPPTValueRandomizer._chancePMinusQ
- _OBJC_IVAR_$__DPPTValueRandomizer._epsilon
- _OBJC_IVAR_$__DPPTValueRandomizer._mask
- _OBJC_IVAR_$__DPPTValueRandomizer._numGroups
- _OBJC_METACLASS_$__DPPTValueRandomizer
- _XXH128
- _XXH128_canonicalFromHash
- _XXH128_cmp
- _XXH128_hashFromCanonical
- _XXH128_isEqual
- _XXH32
- _XXH32_canonicalFromHash
- _XXH32_copyState
- _XXH32_createState
- _XXH32_digest
- _XXH32_finalize
- _XXH32_freeState
- _XXH32_hashFromCanonical
- _XXH32_reset
- _XXH32_update
- _XXH3_128bits
- _XXH3_128bits_digest
- _XXH3_128bits_reset
- _XXH3_128bits_reset_withSecret
- _XXH3_128bits_reset_withSeed
- _XXH3_128bits_update
- _XXH3_128bits_withSecret
- _XXH3_128bits_withSeed
- _XXH3_64bits
- _XXH3_64bits_digest
- _XXH3_64bits_reset
- _XXH3_64bits_reset_withSecret
- _XXH3_64bits_reset_withSeed
- _XXH3_64bits_update
- _XXH3_64bits_withSecret
- _XXH3_64bits_withSeed
- _XXH3_copyState
- _XXH3_createState
- _XXH3_freeState
- _XXH3_hashLong_128b_defaultSecret
- _XXH3_hashLong_128b_withSecret
- _XXH3_hashLong_128b_withSeed
- _XXH3_hashLong_64b_defaultSecret
- _XXH3_hashLong_64b_withSecret
- _XXH3_hashLong_64b_withSeed
- _XXH3_len_129to240_128b
- _XXH3_len_129to240_64b
- _XXH3_mergeAccs
- _XXH64
- _XXH64_canonicalFromHash
- _XXH64_copyState
- _XXH64_createState
- _XXH64_digest
- _XXH64_finalize
- _XXH64_freeState
- _XXH64_hashFromCanonical
- _XXH64_reset
- _XXH64_update
- _XXH_versionNumber
- __OBJC_$_CLASS_METHODS__DPPTValueRandomizer
- __OBJC_$_INSTANCE_METHODS__DPPTValueRandomizer
- __OBJC_$_INSTANCE_VARIABLES__DPPTValueRandomizer
- __OBJC_$_PROP_LIST__DPPTValueRandomizer
- __OBJC_CLASS_PROTOCOLS_$__DPPTValueRandomizer
- __OBJC_CLASS_RO_$__DPPTValueRandomizer
- __OBJC_METACLASS_RO_$__DPPTValueRandomizer
- ___35-[_DPDatabaseRecorder recordWords:]_block_invoke
- ___35-[_DPDatabaseRecorder recordWords:]_block_invoke.cold.1
- ___block_literal_global.201
- ___memcpy_chk
- _kDPAPptNumGroups
- _kSecret
- _objc_msgSend$arrayByAddingObject:
- _objc_msgSend$bitStringAlgorithm
- _objc_msgSend$bucketCount
- _objc_msgSend$chancePMinusQ
- _objc_msgSend$fragmentWidth
- _objc_msgSend$getCharacters:range:
- _objc_msgSend$initWithEpsilon:numberOfGroups:
- _objc_msgSend$initWithKey:ascending:
- _objc_msgSend$mask
- _objc_msgSend$numGroups
- _objc_msgSend$parametersForAlgorithm:properties:epsilon:fragmentWidth:
- _objc_msgSend$randomizeWords:fragmentWidth:forKey:
- _objc_msgSend$randomizerWithEpsilon:numberOfGroups:
- _objc_msgSend$sequenceWithoutPadding
- _objc_msgSend$shard:metaData:error:
- _objc_msgSend$sortedArrayUsingDescriptors:
CStrings:
+ "@48@0:8@16@24q32^@40"
+ "Fail to privatize one-hot with Preamble for %@ error=%@"
+ "Privatizing with Preamble for vector %lu for %@"
+ "Successfully privatized with Preamble for %@"
+ "XPCConnectionRejectedWithoutEntitlement"
+ "donateEventToCoreAnalytics:succeeded:count:"
+ "fedstats:com.apple.insights.internal-collection.analysisB"
+ "numberWithInt:"
+ "parametersForAlgorithm:properties:epsilon:"
+ "recordWords API is no longer supported."
+ "shard:metaData:dimension:error:"
- "%lu,%lu,%llu"
- "@\"NSArray\"40@0:8@\"NSArray\"16Q24@\"NSString\"32"
- "@28@0:8d16I24"
- "@48@0:8@16@24@32Q40"
- "@unionOfObjects.word"
- "Fail to privatize one-hot with Preamble: one-hot index=%@ error=%@"
- "Missing sequence in %@ - not recording in DB"
- "Missing sequenceWithoutPadding in %@ - not recording in DB"
- "PrefixTrie"
- "Privatizing with Preamble for vector %lu with value one at index %lu"
- "Sharding with Preamble: one-hot index=%@"
- "Successfully privatized with Preamble: one hot index=%@"
- "TB,R,N,V_bitStringAlgorithm"
- "TI,N,V_bucketCount"
- "TI,N,V_numGroups"
- "TQ,N,V_mask"
- "TQ,R,N,V_fragmentWidth"
- "Td,N,V_chancePMinusQ"
- "Td,N,V_epsilon"
- "_DPPTValueRandomizer"
- "_bitStringAlgorithm"
- "_bucketCount"
- "_chancePMinusQ"
- "_fragmentWidth"
- "_mask"
- "_numGroups"
- "arrayByAddingObject:"
- "bitStringAlgorithm"
- "bucketCount"
- "chancePMinusQ"
- "com.apple.differentialprivacy.recordWords"
- "fragmentWidth"
- "getCharacters:range:"
- "initWithEpsilon:numberOfGroups:"
- "initWithKey:ascending:"
- "mask"
- "numGroups"
- "parametersForAlgorithm:properties:epsilon:fragmentWidth:"
- "randomizeWords:fragmentWidth:forKey:"
- "randomizerWithEpsilon:numberOfGroups:"
- "recordWords with fragment width and count is no longer supported."
- "recordWords, missing sequence"
- "recordWords, missing sequence without padding"
- "recordWords, missing sequence without padding blacklisted"
- "setBucketCount:"
- "setChancePMinusQ:"
- "setEpsilon:"
- "setMask:"
- "setNumGroups:"
- "shard:metaData:error:"
- "sortedArrayUsingDescriptors:"

```
