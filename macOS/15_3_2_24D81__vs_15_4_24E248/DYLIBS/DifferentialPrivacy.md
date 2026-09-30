## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/Versions/A/DifferentialPrivacy`

```diff

-643.80.4.0.0
-  __TEXT.__text: 0x66b8c
-  __TEXT.__auth_stubs: 0xdb0
-  __TEXT.__objc_methlist: 0x54e4
-  __TEXT.__const: 0x850
-  __TEXT.__cstring: 0x489d
-  __TEXT.__oslogstring: 0x3f48
-  __TEXT.__gcc_except_tab: 0xb84
+659.100.11.0.0
+  __TEXT.__text: 0x66174
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x5700
+  __TEXT.__const: 0x810
+  __TEXT.__cstring: 0x473d
+  __TEXT.__oslogstring: 0x4112
+  __TEXT.__gcc_except_tab: 0xbc4
   __TEXT.__ustring: 0x4
   __TEXT.__dlopen_cstrs: 0x74
   __TEXT.__constg_swiftt: 0x218

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__unwind_info: 0x18e8
-  __TEXT.__eh_frame: 0x460
-  __TEXT.__objc_classname: 0xd8f
-  __TEXT.__objc_methname: 0x9e18
-  __TEXT.__objc_methtype: 0x1393
-  __TEXT.__objc_stubs: 0x7f60
-  __DATA_CONST.__got: 0x7b8
-  __DATA_CONST.__const: 0x870
-  __DATA_CONST.__objc_classlist: 0x4a8
+  __TEXT.__unwind_info: 0x1888
+  __TEXT.__eh_frame: 0x548
+  __TEXT.__objc_classname: 0xd30
+  __TEXT.__objc_methname: 0x99e7
+  __TEXT.__objc_methtype: 0x12fe
+  __TEXT.__objc_stubs: 0x7c60
+  __DATA_CONST.__got: 0x7a8
+  __DATA_CONST.__const: 0x7d8
+  __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24a8
+  __DATA_CONST.__objc_selrefs: 0x2480
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x308
-  __DATA_CONST.__objc_arraydata: 0x748
-  __AUTH_CONST.__auth_got: 0x6f0
-  __AUTH_CONST.__const: 0xfc0
-  __AUTH_CONST.__cfstring: 0x4cc0
-  __AUTH_CONST.__objc_const: 0xbc28
-  __AUTH_CONST.__objc_intobj: 0xd08
+  __DATA_CONST.__objc_superrefs: 0x2e0
+  __DATA_CONST.__objc_arraydata: 0x728
+  __AUTH_CONST.__auth_got: 0x6d8
+  __AUTH_CONST.__const: 0xf90
+  __AUTH_CONST.__cfstring: 0x4b00
+  __AUTH_CONST.__objc_const: 0xaad0
+  __AUTH_CONST.__objc_intobj: 0xd38
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x1498
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0x57c
+  __DATA.__objc_ivar: 0x530
   __DATA.__data: 0x908
   __DATA.__bss: 0x8b0
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1db0
+  __DATA_DIRTY.__objc_data: 0x1c20
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 5B91E897-71FC-3749-A646-C0CC8EF1C8E0
-  Functions: 2425
-  Symbols:   5648
-  CStrings:  3745
+  UUID: 3EF6D8B0-8988-33C5-8562-C1C7FF0398C5
+  Functions: 2395
+  Symbols:   5521
+  CStrings:  3679
 
Symbols:
+ +[_DPBitValueMap initialize].cold.1
+ +[_DPBlacklist initialize].cold.1
+ +[_DPCoreAnalyticsCollector sharedInstance].cold.1
+ +[_DPDeviceInfo isDataCollectionEnabled].cold.1
+ +[_DPDeviceInfo isInternalBuild].cold.1
+ +[_DPDeviceInfo isRunningAsLaunchDaemon].cold.1
+ +[_DPDeviceInfo isRunningUnitTests].cold.1
+ +[_DPKeyProperties initialize].cold.1
+ +[_DPKeyProperties privatizationAlgorithmStringFor:]
+ +[_DPLog daemon].cold.1
+ +[_DPLog framework].cold.1
+ +[_DPLog service].cold.1
+ +[_DPLog tool].cold.1
+ +[_DPPrioPiRapporValueRandomizer shouldForwardToV2DelegateWithMetadata:]
+ +[_DPPrioPiRapporValueRandomizer shouldForwardToV2DelegateWithMetadata:].cold.1
+ +[_DPPrioValueRandomizer shouldForwardToDelegateWithMetadata:]
+ +[_DPPrioValueRandomizer shouldForwardToDelegateWithMetadata:].cold.1
+ +[_DPPrivacyBudget initialize].cold.1
+ +[_DPRenyiDP defaultAlphas].cold.1
+ +[_DPStorage errorStringFor:].cold.1
+ +[_DPStrings algorithmParametersPath].cold.1
+ +[_DPStrings budgetPropertiesPath].cold.1
+ +[_DPStrings dataTypeParametersPath].cold.1
+ +[_DPStrings databaseDirectoryPath].cold.1
+ +[_DPStrings keyNamesPath].cold.1
+ +[_DPStrings keyPropertiesPath].cold.1
+ +[_DPStrings namespaceParametersPath].cold.1
+ +[_DPStrings tokensDirectoryPath].cold.1
+ +[_DPStrings transparencyLogDirectoryPath].cold.1
+ +[_DPToolCommand supportedCommands].cold.1
+ +[_DPToolCommand supportedMetadataKeys].cold.1
+ +[_DPTransparencyLogCreator formatSerializedData:]
+ +[_DPTransparencyLogCreator inPlaceReplaceOccurrencesOf:with:inBytes:bytesLength:caseSensitiveSearch:repeat:]
+ -[_DPKeyProperties dataSource]
+ -[_DPPINERandomizer randomizeFloatVectors:metadata:forKey:].cold.1
+ -[_DPPINERandomizer randomizeFloatVectors:metadata:forKey:].cold.2
+ -[_DPPINERandomizer recordWithShardResult:noisedVector:metadata:key:]
+ -[_DPPrioPiRapporValueRandomizer minBatchSize]
+ -[_DPPrioPiRapporValueRandomizer minBatchSize].cold.1
+ -[_DPPrioPiRapporValueRandomizer v2MetadataFromMetadata:]
+ -[_DPPrioPiRapporValueRandomizer v2MetadataFromMetadata:].cold.1
+ -[_DPPrioPiRapporValueRandomizer v2Randomizer]
+ -[_DPPrioValueRandomizer delegateMetadataFromMetadata:]
+ -[_DPPrioValueRandomizer delegateMetadataFromMetadata:].cold.1
+ -[_DPPrioValueRandomizer delegateRandomizer]
+ -[_DPPrioValueRandomizer delegateRandomizer].cold.1
+ -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:].cold.3
+ -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:].cold.3
+ -[_DPTransparencyLogCreator contentsForDonations:withReportName:]
+ -[_DPTransparencyLogCreator dataSource]
+ -[_DPTransparencyLogCreator filterMetadataFieldsInPrivateEvolutionLog:]
+ -[_DPTransparencyLogCreator initWithDonations:error:].cold.2
+ -[_DPTransparencyLogCreator numDonations]
+ -[_DPTransparencyLogCreator rawSerializedData]
+ -[_DPTransparencyLogCreator serializedData]
+ OBJC_IVAR_$__DPKeyProperties._dataSource
+ OBJC_IVAR_$__DPTransparencyLogCreator._dataSource
+ OBJC_IVAR_$__DPTransparencyLogCreator._numDonations
+ OBJC_IVAR_$__DPTransparencyLogCreator._rawSerializedData
+ OBJC_IVAR_$__DPTransparencyLogCreator._serializedData
+ _DPDediscoVersionWithMetadata.cold.1
+ _DPDediscoVersionWithMetadata.cold.2
+ _DPDediscoVersionWithMetadata.cold.3
+ _DPDediscoVersionWithMetadata.cold.4
+ _DPMetadataExpectedClasses.cold.1
+ _DPMetadataOptionalKeys.cold.1
+ _DPMetadataRequiredKeys.cold.1
+ _DPMetadataV2OptionalKeys.cold.1
+ _DPMetadataV2RequiredKeys.cold.1
+ _NSInternalInconsistencyException
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$_NSNull
+ __46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.33
+ __46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.33.cold.1
+ __DPDediscoVersionWithMetadata
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ __block_literal_global.177
+ __block_literal_global.179
+ __block_literal_global.181
+ __block_literal_global.183
+ __block_literal_global.193
+ _kDPKPDataSource
+ _kDPMetadataNoisedData
+ _kDPMetadataPrivatizationAlgorithmCache
+ _kDPMetadataPrivatizationAlgorithmParametersCache
+ _objc_msgSend$contentsForDonations:withReportName:
+ _objc_msgSend$dataSource
+ _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
+ _objc_msgSend$defaultLocalEpsilon
+ _objc_msgSend$delegateMetadataFromMetadata:
+ _objc_msgSend$delegateRandomizer
+ _objc_msgSend$filterMetadataFieldsInPrivateEvolutionLog:
+ _objc_msgSend$formatSerializedData:
+ _objc_msgSend$inPlaceReplaceOccurrencesOf:with:inBytes:bytesLength:caseSensitiveSearch:repeat:
+ _objc_msgSend$initWithString:error:
+ _objc_msgSend$isBackwardCompatibleWithVersion:
+ _objc_msgSend$minBatchSize
+ _objc_msgSend$numDonations
+ _objc_msgSend$privatizationAlgorithmStringFor:
+ _objc_msgSend$raise:format:
+ _objc_msgSend$recordWithShardResult:noisedVector:metadata:key:
+ _objc_msgSend$serializedData
+ _objc_msgSend$shouldForwardToDelegateWithMetadata:
+ _objc_msgSend$shouldForwardToV2DelegateWithMetadata:
+ _objc_msgSend$uppercaseString
+ _objc_msgSend$v2MetadataFromMetadata:
+ _objc_msgSend$v2Randomizer
+ _objc_msgSend$writeToFile:atomically:
+ minBatchSize.minBatchSizes
- +[_DPCMSRandomizer randomizerWithEpsilon:bitCount:hashFunctionCount:]
- +[_DPCMSRandomizer randomizerWithEpsilon:bitCount:hashFunctionCount:fragmentEpsilon:fragmentBitCount:fragmentHashFunctionCount:]
- +[_DPCMSSample cmsSampleWith:privacyParameter:hashFunctionCount:bitCount:]
- +[_DPCMSSample convertToHexString:]
- +[_DPCMSSample dataFor:hashAtIndex:privacyParameter:bitCount:]
- +[_DPCMSSample jsonStringFrom:hashIndex:]
- +[_DPCMSSample jsonStringFromSequence:sequenceHashIndex:fragment:fragmentHashIndex:fragmentPosition:]
- +[_DPHCMSRandomizer randomizerWithEpsilon:bitCount:hashFunctionCount:]
- +[_DPHCMSRandomizer randomizerWithEpsilon:bitCount:hashFunctionCount:fragmentEpsilon:fragmentBitCount:fragmentHashFunctionCount:]
- +[_DPHCMSSample convertDataToString:]
- +[_DPHCMSSample dataFor:hashAtIndex:epsilon:bitCount:bitIndex:]
- +[_DPHCMSSample hcmsSampleWith:privacyParameter:hashFunctionCount:bitCount:]
- +[_DPHCMSSample jsonStringFrom:hashIndex:bitIndex:]
- +[_DPHCMSSample jsonStringFromSequence:sequenceHashIndex:sequencebitIndex:fragment:fragmentHashIndex:fragmentbitIndex:fragmentPosition:]
- +[_DPPrioCountMinSketchValueRandomizer randomizerWithEpsilon:bitCount:hashFunctionCount:]
- +[_DPPrioPlusPlusValueRandomizer reconstructedDataFromShare1:share2:]
- +[_DPPrioPlusPlusValueRandomizer reconstructedDataFromShare1:share2:].cold.1
- -[_DPCMSRandomizer cmsSampleForFragment:]
- -[_DPCMSRandomizer cmsSampleForString:]
- -[_DPCMSRandomizer description]
- -[_DPCMSRandomizer epsilon]
- -[_DPCMSRandomizer fragmentEpsilon]
- -[_DPCMSRandomizer fragmentK]
- -[_DPCMSRandomizer fragmentM]
- -[_DPCMSRandomizer initWithEpsilon:bitCount:hashFunctionCount:]
- -[_DPCMSRandomizer initWithEpsilon:bitCount:hashFunctionCount:fragmentEpsilon:fragmentBitCount:fragmentHashFunctionCount:]
- -[_DPCMSRandomizer init]
- -[_DPCMSRandomizer k]
- -[_DPCMSRandomizer m]
- -[_DPCMSRandomizer randomizeBitValues:forKey:]
- -[_DPCMSRandomizer randomizeStrings:forKey:]
- -[_DPCMSRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPCMSSample .cxx_destruct]
- -[_DPCMSSample bitString]
- -[_DPCMSSample hashFunctionIndex]
- -[_DPCMSSample initWith:privacyParameter:hashFunctionCount:bitCount:]
- -[_DPCMSSample init]
- -[_DPCMSSequenceRecord jsonString]
- -[_DPCMSWordRecord jsonString]
- -[_DPDatabaseRecorder puzzlePieceCount]
- -[_DPHCMSRandomizer description]
- -[_DPHCMSRandomizer epsilon]
- -[_DPHCMSRandomizer fragmentEpsilon]
- -[_DPHCMSRandomizer fragmentK]
- -[_DPHCMSRandomizer fragmentM]
- -[_DPHCMSRandomizer hcmsSampleForFragment:]
- -[_DPHCMSRandomizer hcmsSampleForString:]
- -[_DPHCMSRandomizer initWithEpsilon:bitCount:hashFunctionCount:]
- -[_DPHCMSRandomizer initWithEpsilon:bitCount:hashFunctionCount:fragmentEpsilon:fragmentBitCount:fragmentHashFunctionCount:]
- -[_DPHCMSRandomizer init]
- -[_DPHCMSRandomizer k]
- -[_DPHCMSRandomizer m]
- -[_DPHCMSRandomizer randomizeBitValues:forKey:]
- -[_DPHCMSRandomizer randomizeStrings:forKey:]
- -[_DPHCMSRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPHCMSSample .cxx_destruct]
- -[_DPHCMSSample bitIndex]
- -[_DPHCMSSample bitString]
- -[_DPHCMSSample hashFunctionIndex]
- -[_DPHCMSSample initWith:privacyParameter:hashFunctionCount:bitCount:]
- -[_DPHCMSSample init]
- -[_DPHCMSSequenceRecord jsonString]
- -[_DPHCMSWordRecord jsonString]
- -[_DPKeyProperties keyPatternsAllowed]
- -[_DPPINERandomizer randomizeFloatVector:metadata:].cold.4
- -[_DPPINERandomizer recordWithShardResult:metadata:key:]
- -[_DPPrioCountMinSketchValueRandomizer epsilon]
- -[_DPPrioCountMinSketchValueRandomizer initWithEpsilon:bitCount:hashFunctionCount:]
- -[_DPPrioCountMinSketchValueRandomizer init]
- -[_DPPrioCountMinSketchValueRandomizer k]
- -[_DPPrioCountMinSketchValueRandomizer m]
- -[_DPPrioCountMinSketchValueRandomizer randomize:metadata:]
- -[_DPPrioCountMinSketchValueRandomizer randomize:metadata:].cold.1
- -[_DPPrioCountMinSketchValueRandomizer randomizeBitValues:forKey:]
- -[_DPPrioCountMinSketchValueRandomizer randomizeStrings:forKey:]
- -[_DPPrioCountMinSketchValueRandomizer randomizeStrings:metadata:forKey:]
- -[_DPPrioCountMinSketchValueRandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPTransparencyLogCreator contentsForDonations:withReportName:error:]
- -[_DPTransparencyLogCreator contentsForDonations:withReportName:error:].cold.1
- -[_DPTransparencyLogCreator contentsForDonations:withReportName:error:].cold.2
- -[_DPTransparencyLogCreator contents]
- -[_DPTransparencyLogCreator filterFieldsForPrivateEvolutionLogInMetadata:]
- -[_DPTransparencyLogCreator reportNameAcronym]
- -[_DPTransparencyLogCreator serializedContentsWithError:]
- -[_DPTransparencyLogCreator serializedContentsWithError:].cold.1
- OBJC_IVAR_$__DPCMSRandomizer._epsilon
- OBJC_IVAR_$__DPCMSRandomizer._fragmentEpsilon
- OBJC_IVAR_$__DPCMSRandomizer._fragmentK
- OBJC_IVAR_$__DPCMSRandomizer._fragmentM
- OBJC_IVAR_$__DPCMSRandomizer._k
- OBJC_IVAR_$__DPCMSRandomizer._m
- OBJC_IVAR_$__DPCMSSample._bitString
- OBJC_IVAR_$__DPCMSSample._hashFunctionIndex
- OBJC_IVAR_$__DPDatabaseRecorder._puzzlePieceCount
- OBJC_IVAR_$__DPHCMSRandomizer._epsilon
- OBJC_IVAR_$__DPHCMSRandomizer._fragmentEpsilon
- OBJC_IVAR_$__DPHCMSRandomizer._fragmentK
- OBJC_IVAR_$__DPHCMSRandomizer._fragmentM
- OBJC_IVAR_$__DPHCMSRandomizer._k
- OBJC_IVAR_$__DPHCMSRandomizer._m
- OBJC_IVAR_$__DPHCMSSample._bitIndex
- OBJC_IVAR_$__DPHCMSSample._bitString
- OBJC_IVAR_$__DPHCMSSample._hashFunctionIndex
- OBJC_IVAR_$__DPKeyProperties._keyPatternsAllowed
- OBJC_IVAR_$__DPPrioCountMinSketchValueRandomizer._epsilon
- OBJC_IVAR_$__DPPrioCountMinSketchValueRandomizer._k
- OBJC_IVAR_$__DPPrioCountMinSketchValueRandomizer._m
- OBJC_IVAR_$__DPTransparencyLogCreator._contents
- OBJC_IVAR_$__DPTransparencyLogCreator._reportNameAcronym
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
- __46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.34
- __46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.34.cold.1
- __OBJC_$_CLASS_METHODS__DPCMSRandomizer
- __OBJC_$_CLASS_METHODS__DPCMSSample
- __OBJC_$_CLASS_METHODS__DPHCMSRandomizer
- __OBJC_$_CLASS_METHODS__DPHCMSSample
- __OBJC_$_CLASS_METHODS__DPPrioCountMinSketchValueRandomizer
- __OBJC_$_INSTANCE_METHODS__DPCMSRandomizer
- __OBJC_$_INSTANCE_METHODS__DPCMSSample
- __OBJC_$_INSTANCE_METHODS__DPHCMSRandomizer
- __OBJC_$_INSTANCE_METHODS__DPHCMSSample
- __OBJC_$_INSTANCE_METHODS__DPPrioCountMinSketchValueRandomizer
- __OBJC_$_INSTANCE_VARIABLES__DPCMSRandomizer
- __OBJC_$_INSTANCE_VARIABLES__DPCMSSample
- __OBJC_$_INSTANCE_VARIABLES__DPHCMSRandomizer
- __OBJC_$_INSTANCE_VARIABLES__DPHCMSSample
- __OBJC_$_INSTANCE_VARIABLES__DPPrioCountMinSketchValueRandomizer
- __OBJC_$_PROP_LIST__DPCMSRandomizer
- __OBJC_$_PROP_LIST__DPCMSSample
- __OBJC_$_PROP_LIST__DPHCMSRandomizer
- __OBJC_$_PROP_LIST__DPHCMSSample
- __OBJC_$_PROP_LIST__DPPrioCountMinSketchValueRandomizer
- __OBJC_CLASS_PROTOCOLS_$__DPCMSRandomizer
- __OBJC_CLASS_PROTOCOLS_$__DPHCMSRandomizer
- __OBJC_CLASS_PROTOCOLS_$__DPPrioCountMinSketchValueRandomizer
- __OBJC_CLASS_RO_$__DPCMSRandomizer
- __OBJC_CLASS_RO_$__DPCMSSample
- __OBJC_CLASS_RO_$__DPHCMSRandomizer
- __OBJC_CLASS_RO_$__DPHCMSSample
- __OBJC_CLASS_RO_$__DPPrioCountMinSketchValueRandomizer
- __OBJC_METACLASS_RO_$__DPCMSRandomizer
- __OBJC_METACLASS_RO_$__DPCMSSample
- __OBJC_METACLASS_RO_$__DPHCMSRandomizer
- __OBJC_METACLASS_RO_$__DPHCMSSample
- __OBJC_METACLASS_RO_$__DPPrioCountMinSketchValueRandomizer
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___59-[_DPPrioCountMinSketchValueRandomizer randomize:metadata:]_block_invoke
- ___block_descriptor_52_e8_32s_e12_B24?0^I8Q16l
- __block_literal_global.168
- __block_literal_global.170
- __block_literal_global.172
- __block_literal_global.174
- __block_literal_global.213
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
- _kDediscoReportNameAcronym
- _kPrivateEvolutionReportNameAcronym
- _objc_msgSend$bitIndex
- _objc_msgSend$bitString
- _objc_msgSend$cmsSampleForFragment:
- _objc_msgSend$cmsSampleForString:
- _objc_msgSend$cmsSampleWith:privacyParameter:hashFunctionCount:bitCount:
- _objc_msgSend$containsString:
- _objc_msgSend$contents
- _objc_msgSend$contentsForDonations:withReportName:error:
- _objc_msgSend$convertDataToString:
- _objc_msgSend$dataFor:hashAtIndex:epsilon:bitCount:bitIndex:
- _objc_msgSend$dataFor:hashAtIndex:privacyParameter:bitCount:
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$dataWithBytesNoCopy:length:
- _objc_msgSend$dataWithCapacity:
- _objc_msgSend$decodeObjectForKey:
- _objc_msgSend$filterFieldsForPrivateEvolutionLogInMetadata:
- _objc_msgSend$fragmentEpsilon
- _objc_msgSend$fragmentK
- _objc_msgSend$fragmentM
- _objc_msgSend$hashFunctionIndex
- _objc_msgSend$hcmsSampleForFragment:
- _objc_msgSend$hcmsSampleForString:
- _objc_msgSend$hcmsSampleWith:privacyParameter:hashFunctionCount:bitCount:
- _objc_msgSend$initWith:privacyParameter:hashFunctionCount:bitCount:
- _objc_msgSend$initWithEpsilon:bitCount:hashFunctionCount:
- _objc_msgSend$initWithEpsilon:bitCount:hashFunctionCount:fragmentEpsilon:fragmentBitCount:fragmentHashFunctionCount:
- _objc_msgSend$initWithKey:plainSequence:sequence:sequenceHashIndex:creationDate:submitted:objectId:
- _objc_msgSend$initWithKey:plainSequence:sequence:sequenceHashIndex:plainFragment:fragment:fragmentHashIndex:fragmentPosition:creationDate:submitted:objectId:
- _objc_msgSend$initWithKey:plainSequence:sequence:sequenceHashIndex:sequenceBitIndex:creationDate:submitted:objectId:
- _objc_msgSend$initWithKey:plainSequence:sequence:sequenceHashIndex:sequenceBitIndex:plainFragment:fragment:fragmentHashIndex:fragmentBitIndex:fragmentPosition:creationDate:submitted:objectId:
- _objc_msgSend$jsonStringFrom:hashIndex:
- _objc_msgSend$jsonStringFrom:hashIndex:bitIndex:
- _objc_msgSend$jsonStringFromSequence:sequenceHashIndex:fragment:fragmentHashIndex:fragmentPosition:
- _objc_msgSend$jsonStringFromSequence:sequenceHashIndex:sequencebitIndex:fragment:fragmentHashIndex:fragmentbitIndex:fragmentPosition:
- _objc_msgSend$k
- _objc_msgSend$keyPatternsAllowed
- _objc_msgSend$m
- _objc_msgSend$numberWithFloat:
- _objc_msgSend$predicateForRecordsNotSubmittedForKey:
- _objc_msgSend$randomizerWithEpsilon:bitCount:hashFunctionCount:
- _objc_msgSend$randomizerWithEpsilon:bitCount:hashFunctionCount:fragmentEpsilon:fragmentBitCount:fragmentHashFunctionCount:
- _objc_msgSend$reconstructedDataFromShare1:share2:
- _objc_msgSend$replaceOccurrencesOfString:withString:options:range:
- _objc_msgSend$reportNameAcronym
- _objc_msgSend$serializedContentsWithError:
- _objc_msgSend$unsignedShortValue
- _objc_msgSend$writeDediscoSubmission:withReportName:inDirectory:
- _set_bit
- _uint32_from_string
CStrings:
+ "\"["
+ "%.4f,"
+ "%.4f]"
+ "%@: failed to serialize transparency log content to json"
+ "%@: { propertiesName=%@ ; possibleRange=%@ ; acceptableError=%@ ; trimmedScale=%@ ; noiseDistribution=%@ ; budget=%@ ; privacyParameter=%@ ; transport=%ld ; privatizationAlgorithm=%@ ; submissionPriority=%lu ; parameterDictionary=%@ ;  }"
+ "DEDISCO"
+ "DataSource"
+ "Expecting v2 metadata but got nil"
+ "Fail to add noise to vector with key=%@, continuing..."
+ "Fail to compute minimum batch size for local epsilon=%f"
+ "Fail to infer version from metadata=%@"
+ "Fail to privatize vector with key=%@, continuing..."
+ "Forwarding to delegate randomizer"
+ "Malformed PPM version in donation metadata, error: %@"
+ "Malformed parameter (%@.%@) in metadata, expected numbers, got=%@"
+ "Missing %@ in metadata"
+ "NoisedData"
+ "PPM version is not specified in donation metadata. Using default PPM version %@ to upload the donation."
+ "PrivatizationAlgorithmCache"
+ "PrivatizationAlgorithmParametersCache"
+ "Q56@0:8@16@24*32Q40B48B52"
+ "T@\"NSData\",R,N,V_rawSerializedData"
+ "T@\"NSData\",R,N,V_serializedData"
+ "T@\"NSString\",R,N,V_dataSource"
+ "TQ,R,N,V_numDonations"
+ "Unable to find a matching PPM version from donation metadata's version string: '%@'"
+ "Using PPM compatible version %@ to upload the donation."
+ "Using default dimensionality %lu while forwarding to v2 route"
+ "["
+ "]"
+ "]\""
+ "_dataSource"
+ "_numDonations"
+ "_rawSerializedData"
+ "_serializedData"
+ "contentsForDonations:withReportName:"
+ "dataWithBytesNoCopy:length:freeWhenDone:"
+ "delegateMetadataFromMetadata:"
+ "delegateRandomizer"
+ "filterMetadataFieldsInPrivateEvolutionLog:"
+ "formatSerializedData:"
+ "inPlaceReplaceOccurrencesOf:with:inBytes:bytesLength:caseSensitiveSearch:repeat:"
+ "minBatchSize"
+ "numDonations"
+ "privatizationAlgorithmStringFor:"
+ "raise:format:"
+ "rawSerializedData"
+ "recordWithShardResult:noisedVector:metadata:key:"
+ "serializedData"
+ "shouldForwardToDelegateWithMetadata:"
+ "shouldForwardToV2DelegateWithMetadata:"
+ "uppercaseString"
+ "v2MetadataFromMetadata:"
+ "v2Randomizer"
+ "writeToFile:atomically:"
- "\"%hu,"
- "%@: failed to serialize transparency log content to json, error: %@"
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
- "Donation algorithm is expected to be PrioPlusPlus, instead got %@."
- "Fail to private vector with key=%@, continuing..."
- "Failed to expand share2 from PrioPlusPlus."
- "HadamardCountMedianSketch"
- "Malformed data in donation."
- "Malformed parameter (%@.%@) in metadata, expected numbers."
- "PPM"
- "PrioCountMinSketch"
- "PrivateEvolutionPlugin:results"
- "SequenceDiscoveryWithPuzzlePiece"
- "SequenceFragmentPuzzle+CountMedianSketch"
- "SequenceFragmentPuzzle+HadamardCountMedianSketch"
- "T@\"NSArray\",R,N,V_contents"
- "T@\"NSData\",R,N,V_bitString"
- "T@\"NSString\",R,N,V_reportNameAcronym"
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
- "_contents"
- "_fragmentEpsilon"
- "_fragmentK"
- "_fragmentM"
- "_hashFunctionIndex"
- "_k"
- "_keyPatternsAllowed"
- "_puzzlePieceCount"
- "_reportNameAcronym"
- "bitIndex"
- "bitString"
- "cmsSampleForFragment:"
- "cmsSampleForString:"
- "cmsSampleWith:privacyParameter:hashFunctionCount:bitCount:"
- "containsString:"
- "contents"
- "contentsForDonations:withReportName:error:"
- "convertDataToString:"
- "dataFor:hashAtIndex:epsilon:bitCount:bitIndex:"
- "dataFor:hashAtIndex:privacyParameter:bitCount:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:"
- "dataWithCapacity:"
- "decodeObjectForKey:"
- "email"
- "filterFieldsForPrivateEvolutionLogInMetadata:"
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
- "k"
- "keyPatternsAllowed"
- "numberWithFloat:"
- "puzzleCount"
- "puzzlePieceCount"
- "randomizerWithEpsilon:bitCount:hashFunctionCount:"
- "randomizerWithEpsilon:bitCount:hashFunctionCount:fragmentEpsilon:fragmentBitCount:fragmentHashFunctionCount:"
- "reconstructedDataFromShare1:share2:"
- "replaceOccurrencesOfString:withString:options:range:"
- "reportNameAcronym"
- "sequenceFragmentBias"
- "sequenceK"
- "sequenceM"
- "serializedContentsWithError:"
- "unsignedShortValue"

```
