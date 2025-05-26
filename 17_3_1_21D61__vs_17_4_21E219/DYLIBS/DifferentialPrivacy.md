## DifferentialPrivacy

> `/System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy`

```diff

-485.80.4.0.0
-  __TEXT.__text: 0x55618
-  __TEXT.__auth_stubs: 0xcd0
-  __TEXT.__objc_methlist: 0x4e88
-  __TEXT.__const: 0x572
-  __TEXT.__cstring: 0x2c6a4
-  __TEXT.__oslogstring: 0x39cc
-  __TEXT.__gcc_except_tab: 0xb90
+558.0.0.0.0
+  __TEXT.__text: 0x5a2e8
+  __TEXT.__auth_stubs: 0xe40
+  __TEXT.__objc_methlist: 0x5120
+  __TEXT.__const: 0x6c2
+  __TEXT.__cstring: 0x2ce57
+  __TEXT.__oslogstring: 0x3e36
+  __TEXT.__gcc_except_tab: 0xb0c
   __TEXT.__dlopen_cstrs: 0x170
   __TEXT.__ustring: 0x578
-  __TEXT.__constg_swiftt: 0x98
-  __TEXT.__swift5_typeref: 0x68
-  __TEXT.__swift5_reflstr: 0x9f
-  __TEXT.__swift5_fieldmd: 0x74
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__swift5_proto: 0x18
-  __TEXT.__unwind_info: 0x1810
-  __TEXT.__eh_frame: 0x1c8
-  __TEXT.__objc_classname: 0xbef
-  __TEXT.__objc_methname: 0x939f
-  __TEXT.__objc_methtype: 0x1294
-  __TEXT.__objc_stubs: 0x7840
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0xfc0
-  __DATA_CONST.__objc_classlist: 0x418
+  __TEXT.__constg_swiftt: 0x158
+  __TEXT.__swift5_typeref: 0xcd
+  __TEXT.__swift5_reflstr: 0x11d
+  __TEXT.__swift5_fieldmd: 0x110
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_proto: 0x24
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__unwind_info: 0x1a4c
+  __TEXT.__eh_frame: 0x2f8
+  __TEXT.__objc_classname: 0xc50
+  __TEXT.__objc_methname: 0x9559
+  __TEXT.__objc_methtype: 0x131d
+  __TEXT.__objc_stubs: 0x7b80
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__const: 0xff0
+  __DATA_CONST.__objc_classlist: 0x448
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x88
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6fa0
-  __DATA_CONST.__objc_selrefs: 0x2230
-  __DATA_CONST.__objc_arraydata: 0x4d9a0
-  __AUTH_CONST.__cfstring: 0x9dfa0
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__objc_intobj: 0x748c8
+  __DATA_CONST.__objc_const: 0x7350
+  __DATA_CONST.__objc_selrefs: 0x2360
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x590
+  __DATA_CONST.__objc_superrefs: 0x2b8
+  __DATA_CONST.__objc_arraydata: 0x4d990
+  __AUTH_CONST.__cfstring: 0x9e260
+  __AUTH_CONST.__objc_const: 0x438
+  __AUTH_CONST.__objc_intobj: 0x748b0
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__const: 0x308
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__auth_got: 0x680
-  __AUTH.__objc_data: 0x0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x560
-  __DATA.__objc_superrefs: 0x2a0
-  __DATA.__objc_ivar: 0x508
-  __DATA.__data: 0x850
-  __DATA.__bss: 0x3c0
+  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__auth_got: 0x738
+  __AUTH.__objc_data: 0x4e8
+  __AUTH.__data: 0x78
+  __DATA.__objc_ivar: 0x50c
+  __DATA.__data: 0x918
+  __DATA.__bss: 0x540
   __DATA.__common: 0x28
-  __DATA_DIRTY.__const: 0x4e0
-  __DATA_DIRTY.__objc_const: 0x37a0
-  __DATA_DIRTY.__objc_data: 0x2998
+  __DATA_DIRTY.__const: 0x3a0
+  __DATA_DIRTY.__objc_const: 0x35a8
+  __DATA_DIRTY.__objc_data: 0x2808
   __DATA_DIRTY.__data: 0xd8
   __DATA_DIRTY.__bss: 0x170
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
+  - /System/Library/PrivateFrameworks/VDAF.framework/VDAF
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
-  Functions: 2188
-  Symbols:   7183
-  CStrings:  22395
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 2352
+  Symbols:   7485
+  CStrings:  22532
 
Symbols:
+ +[_DPApproximateDP isValidDelta:error:]
+ +[_DPApproximateDP isValidDelta:error:].cold.1
+ +[_DPApproximateDP isValidEpsilon:error:]
+ +[_DPApproximateDP isValidEpsilon:error:].cold.1
+ +[_DPBudgetAuditor isDediscoV1:]
+ +[_DPBudgetAuditor isMetadataValid:plistParameters:error:]
+ +[_DPBudgetAuditor isMetadataValid:plistParameters:error:].cold.1
+ +[_DPBudgetAuditor isMetadataValid:plistParameters:error:].cold.2
+ +[_DPBudgetAuditor isMetadataValid:plistParameters:error:].cold.3
+ +[_DPBudgetAuditor isMetadataValid:plistParameters:error:].cold.4
+ +[_DPBudgetAuditor isMetadataValid:plistParameters:error:].cold.5
+ +[_DPBudgetAuditor isMetadataValid:plistParameters:error:].cold.6
+ +[_DPBudgetAuditor isMetadataValid:plistParameters:error:].cold.7
+ +[_DPBudgetAuditor isMetadataValid:plistParameters:error:].cold.8
+ +[_DPDediscoDonation insertIfPossibleObj:intoJSONDictionary:withKey:]
+ +[_DPDediscoDonation insertIfPossibleObj:intoJSONDictionary:withKey:].cold.1
+ +[_DPPrio3SumVectorRandomizer new]
+ +[_DPPrio3SumVectorRandomizer randomizerWithEpsilon:parameters:]
+ +[_DPPrioValueRandomizer randomizerWithEpsilon:parameters:]
+ +[_DPRenyiDP defaultAlphas]
+ +[_DPRenyiDP isValidAlpha:error:]
+ +[_DPRenyiDP isValidAlpha:error:].cold.1
+ +[_DPStrings DediscoTokensDirectoryPath]
+ +[_DPSymmetricRAPPORWithOHE binomialPMFForN:p:x:logBinomCoef:]
+ +[_DPSymmetricRAPPORWithOHE logBinomialCoefForN:x:prevLogBinomCoef:]
+ +[_DPTransparencyLogMaintainer checkAndRemoveFile:]
+ +[_DPTransparencyLogMaintainer checkAndRemoveFile:].cold.1
+ +[_DPTransparencyLogMaintainer lifetimeOfFile:]
+ +[_DPTransparencyLogMaintainer lifetimeOfFile:].cold.1
+ +[_DPTransparencyLogMaintainer lifetimeOfFile:].cold.2
+ +[_DPTransparencyLogMaintainer lifetimeOfFile:].cold.3
+ -[NSString(_DPTArguments) dp_dictionaryFromJsonString].cold.1
+ -[_DPApproximateDP delta]
+ -[_DPApproximateDP description]
+ -[_DPApproximateDP epsilon]
+ -[_DPApproximateDP exceed:]
+ -[_DPApproximateDP initWithEpsilon:delta:error:]
+ -[_DPBudgetAuditor .cxx_destruct]
+ -[_DPBudgetAuditor auditedMetadataForSymmetricRAPPOR:error:]
+ -[_DPBudgetAuditor auditedMetadataForSymmetricRAPPOR:error:].cold.1
+ -[_DPBudgetAuditor auditedMetadataForSymmetricRAPPOR:error:].cold.2
+ -[_DPBudgetAuditor auditedMetadataForSymmetricRAPPOR:error:].cold.3
+ -[_DPBudgetAuditor auditedMetadataForSymmetricRAPPOR:error:].cold.4
+ -[_DPBudgetAuditor auditedMetadataForSymmetricRAPPOR:error:].cold.5
+ -[_DPBudgetAuditor createSymmetricRAPPORWithError:]
+ -[_DPBudgetAuditor createSymmetricRAPPORWithError:].cold.1
+ -[_DPBudgetAuditor defaultLocalEpsilon]
+ -[_DPBudgetAuditor initWithDefaultLocalEpsilon:metadata:plistParameters:error:]
+ -[_DPBudgetAuditor initWithDefaultLocalEpsilon:metadata:plistParameters:isInternalBuild:error:]
+ -[_DPBudgetAuditor isInternalBuild]
+ -[_DPBudgetAuditor metadata]
+ -[_DPBudgetAuditor plistParameters]
+ -[_DPDataRecorder initWithKey:].cold.1
+ -[_DPDataRecorder initWithKey:].cold.2
+ -[_DPDataRecorder initWithKey:].cold.3
+ -[_DPDatabaseRecorder recordBitValues:metadata:].cold.4
+ -[_DPDediscoDonation jsonRepresentationForMetadata]
+ -[_DPDediscoDonation jsonRepresentationFromParameters:]
+ -[_DPDediscoError logAndStoreInError:]
+ -[_DPDediscoError logAndStoreInError:].cold.1
+ -[_DPKeyProperties initWithPropertyName:dictionary:].cold.1
+ -[_DPKeyProperties initWithPropertyName:dictionary:].cold.2
+ -[_DPKeyProperties initWithPropertyName:dictionary:].cold.3
+ -[_DPKeyProperties initWithPropertyName:dictionary:].cold.4
+ -[_DPKeyProperties initWithPropertyName:dictionary:].cold.5
+ -[_DPKeyProperties initWithPropertyName:dictionary:].cold.6
+ -[_DPKeyProperties initWithPropertyName:dictionary:].cold.7
+ -[_DPKeyProperties initWithPropertyName:dictionary:].cold.8
+ -[_DPKeyProperties initWithPropertyName:dictionary:].cold.9
+ -[_DPKeyProperties transparencyLogLifetime]
+ -[_DPPrio3SumVectorRandomizer .cxx_destruct]
+ -[_DPPrio3SumVectorRandomizer addNoiseToData:withLocalEpsilon:withError:]
+ -[_DPPrio3SumVectorRandomizer defaultLocalEpsilon]
+ -[_DPPrio3SumVectorRandomizer dimensionFromMetadata:]
+ -[_DPPrio3SumVectorRandomizer dimensionFromMetadata:].cold.1
+ -[_DPPrio3SumVectorRandomizer initWithEpsilon:parameters:]
+ -[_DPPrio3SumVectorRandomizer initWithEpsilon:parameters:].cold.1
+ -[_DPPrio3SumVectorRandomizer initWithEpsilon:parameters:].cold.2
+ -[_DPPrio3SumVectorRandomizer initWithEpsilon:parameters:].cold.3
+ -[_DPPrio3SumVectorRandomizer initWithEpsilon:parameters:].cold.4
+ -[_DPPrio3SumVectorRandomizer init]
+ -[_DPPrio3SumVectorRandomizer parameters]
+ -[_DPPrio3SumVectorRandomizer plistParameters]
+ -[_DPPrio3SumVectorRandomizer randomizeBitValue:withLocalEpsilon:metadata:error:]
+ -[_DPPrio3SumVectorRandomizer randomizeBitValues:forKey:]
+ -[_DPPrio3SumVectorRandomizer randomizeBitValues:metadata:forKey:]
+ -[_DPPrio3SumVectorRandomizer randomizeBitValues:metadata:forKey:].cold.1
+ -[_DPPrio3SumVectorRandomizer randomizeBitValues:metadata:forKey:].cold.2
+ -[_DPPrio3SumVectorRandomizer randomizeBitValues:metadata:forKey:].cold.3
+ -[_DPPrio3SumVectorRandomizer randomizeBitVectors:metadata:forKey:]
+ -[_DPPrio3SumVectorRandomizer randomizeBitVectors:metadata:forKey:].cold.1
+ -[_DPPrio3SumVectorRandomizer randomizeBitVectors:metadata:forKey:].cold.2
+ -[_DPPrio3SumVectorRandomizer randomizeBitVectors:metadata:forKey:].cold.3
+ -[_DPPrio3SumVectorRandomizer randomizeStrings:forKey:]
+ -[_DPPrio3SumVectorRandomizer randomizeVector:withLocalEpsilon:metadata:error:]
+ -[_DPPrio3SumVectorRandomizer randomizeWords:fragmentWidth:forKey:]
+ -[_DPPrio3SumVectorRandomizer recordWithShardResult:metadata:key:]
+ -[_DPPrioValueRandomizer .cxx_destruct]
+ -[_DPPrioValueRandomizer defaultLocalEpsilon]
+ -[_DPPrioValueRandomizer initWithEpsilon:parameters:]
+ -[_DPPrioValueRandomizer initWithEpsilon:parameters:].cold.1
+ -[_DPPrioValueRandomizer initWithEpsilon:parameters:].cold.2
+ -[_DPPrioValueRandomizer plistParameters]
+ -[_DPPrioValueRandomizer randomize:withLocalEpsilon:metadata:]
+ -[_DPPrioValueRandomizer randomize:withLocalEpsilon:metadata:].cold.1
+ -[_DPPrioValueRandomizer randomize:withLocalEpsilon:metadata:].cold.2
+ -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:].cold.1
+ -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:].cold.2
+ -[_DPPrioValueRandomizer randomizeBitValues:metadata:forKey:].cold.3
+ -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:].cold.1
+ -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:].cold.2
+ -[_DPPrioValueRandomizer randomizeBitVectors:metadata:forKey:].cold.3
+ -[_DPPrioValueRandomizer randomizeVector:withLocalEpsilon:metadata:]
+ -[_DPPrioValueRandomizer randomizeVector:withLocalEpsilon:metadata:].cold.1
+ -[_DPRenyiDP alpha]
+ -[_DPRenyiDP approximateDPForDelta:error:]
+ -[_DPRenyiDP approximateDPForDelta:error:].cold.1
+ -[_DPRenyiDP approximateDPForDelta:error:].cold.2
+ -[_DPRenyiDP initWithAlpha:tau:error:]
+ -[_DPRenyiDP initWithAlpha:tau:error:].cold.1
+ -[_DPRenyiDP tau]
+ -[_DPSemanticVersion initWithMajorVersion:minorVersion:patchVersion:]
+ -[_DPSemanticVersion initWithString:error:]
+ -[_DPSemanticVersion initWithString:error:].cold.1
+ -[_DPSemanticVersion initWithString:error:].cold.2
+ -[_DPSemanticVersion isBackwardCompatibleWithVersion:]
+ -[_DPSemanticVersion isEqual:]
+ -[_DPSemanticVersion majorVersion]
+ -[_DPSemanticVersion minorVersion]
+ -[_DPSemanticVersion patchVersion]
+ -[_DPServer recordBitValues:metadata:forKey:withReply:].cold.1
+ -[_DPSymmetricRAPPORWithOHE approximateDPBudgetForDelta:error:]
+ -[_DPSymmetricRAPPORWithOHE batchSize]
+ -[_DPSymmetricRAPPORWithOHE initWithBatchSize:localEpsilon:error:]
+ -[_DPSymmetricRAPPORWithOHE initWithBatchSize:localEpsilon:error:].cold.1
+ -[_DPSymmetricRAPPORWithOHE initWithBatchSize:localEpsilon:error:].cold.2
+ -[_DPSymmetricRAPPORWithOHE localEpsilon]
+ -[_DPSymmetricRAPPORWithOHE renyiDPBudgetsForAlphas:error:]
+ -[_DPSymmetricRAPPORWithOHE renyiDPBudgetsForAlphas:error:].cold.1
+ -[_DPSymmetricRAPPORWithOHE renyiDPBudgetsForAlphas:error:].cold.2
+ -[_DPTokenFetcher cleanupStaleTokensInPath:]
+ -[_DPTokenFetcher doMaintenance]
+ -[_DPTokenFetcher doMaintenance].cold.1
+ -[_DPTokenFetcher scheduleMaintenanceWithName:database:]
+ -[_DPToolCommand executeCommand].cold.1
+ -[_DPToolCommand queryForKey:].cold.1
+ -[_DPToolCommand recordBitVectors:metadata:forKey:].cold.1
+ -[_DPTransparencyLogMaintainer .cxx_destruct]
+ -[_DPTransparencyLogMaintainer doMaintenance]
+ -[_DPTransparencyLogMaintainer initWithDirectoryPath:]
+ -[_DPTransparencyLogMaintainer init]
+ -[_DPTransparencyLogMaintainer reportsDirectoryPath]
+ -[_DPTransparencyLogMaintainer scheduleMaintenanceWithName:database:]
+ -[_DPTransparencyLogMaintainer setReportsDirectoryPath:]
+ _OBJC_CLASS_$__DPApproximateDP
+ _OBJC_CLASS_$__DPBudgetAuditor
+ _OBJC_CLASS_$__DPPrio3SumVectorParameter
+ _OBJC_CLASS_$__DPPrio3SumVectorRandomizer
+ _OBJC_CLASS_$__DPPrio3SumVectorShim
+ _OBJC_CLASS_$__DPRenyiDP
+ _OBJC_CLASS_$__DPSemanticVersion
+ _OBJC_CLASS_$__DPSymmetricRAPPORWithOHE
+ _OBJC_CLASS_$__DPTokenFetcher
+ _OBJC_CLASS_$__DPTransparencyLogMaintainer
+ _OBJC_CLASS_$__DPVDAFShardResult
+ _OBJC_IVAR_$__DPApproximateDP._delta
+ _OBJC_IVAR_$__DPApproximateDP._epsilon
+ _OBJC_IVAR_$__DPBudgetAuditor._defaultLocalEpsilon
+ _OBJC_IVAR_$__DPBudgetAuditor._isInternalBuild
+ _OBJC_IVAR_$__DPBudgetAuditor._metadata
+ _OBJC_IVAR_$__DPBudgetAuditor._plistParameters
+ _OBJC_IVAR_$__DPKeyProperties._transparencyLogLifetime
+ _OBJC_IVAR_$__DPPrio3SumVectorRandomizer._defaultLocalEpsilon
+ _OBJC_IVAR_$__DPPrio3SumVectorRandomizer._parameters
+ _OBJC_IVAR_$__DPPrio3SumVectorRandomizer._plistParameters
+ _OBJC_IVAR_$__DPPrioValueRandomizer._defaultLocalEpsilon
+ _OBJC_IVAR_$__DPPrioValueRandomizer._plistParameters
+ _OBJC_IVAR_$__DPRenyiDP._alpha
+ _OBJC_IVAR_$__DPRenyiDP._tau
+ _OBJC_IVAR_$__DPSemanticVersion._majorVersion
+ _OBJC_IVAR_$__DPSemanticVersion._minorVersion
+ _OBJC_IVAR_$__DPSemanticVersion._patchVersion
+ _OBJC_IVAR_$__DPSymmetricRAPPORWithOHE._batchSize
+ _OBJC_IVAR_$__DPSymmetricRAPPORWithOHE._localEpsilon
+ _OBJC_IVAR_$__DPTransparencyLogMaintainer._reportsDirectoryPath
+ _OBJC_METACLASS_$__DPApproximateDP
+ _OBJC_METACLASS_$__DPBudgetAuditor
+ _OBJC_METACLASS_$__DPPrio3SumVectorParameter
+ _OBJC_METACLASS_$__DPPrio3SumVectorRandomizer
+ _OBJC_METACLASS_$__DPPrio3SumVectorShim
+ _OBJC_METACLASS_$__DPRenyiDP
+ _OBJC_METACLASS_$__DPSemanticVersion
+ _OBJC_METACLASS_$__DPSymmetricRAPPORWithOHE
+ _OBJC_METACLASS_$__DPTokenFetcher
+ _OBJC_METACLASS_$__DPTransparencyLogMaintainer
+ _OBJC_METACLASS_$__DPVDAFShardResult
+ __DATA__DPPrio3SumVectorParameter
+ __DATA__DPPrio3SumVectorShim
+ __DATA__DPVDAFShardResult
+ __DPPrivacyBudgetError
+ __DPPrivacyBudgetErrorDomain
+ __DPSemanticVersionError
+ __DPSemanticVersionErrorDomain
+ __DPVDAFError
+ __DPVDAFErrorDomain
+ __IVARS__DPPrio3SumVectorParameter
+ __IVARS__DPVDAFShardResult
+ __METACLASS_DATA__DPPrio3SumVectorParameter
+ __METACLASS_DATA__DPPrio3SumVectorShim
+ __METACLASS_DATA__DPVDAFShardResult
+ __OBJC_$_CLASS_METHODS__DPApproximateDP
+ __OBJC_$_CLASS_METHODS__DPBudgetAuditor
+ __OBJC_$_CLASS_METHODS__DPPrio3SumVectorRandomizer
+ __OBJC_$_CLASS_METHODS__DPPrio3SumVectorShim
+ __OBJC_$_CLASS_METHODS__DPRenyiDP
+ __OBJC_$_CLASS_METHODS__DPSymmetricRAPPORWithOHE
+ __OBJC_$_CLASS_METHODS__DPTransparencyLogMaintainer
+ __OBJC_$_INSTANCE_METHODS__DPApproximateDP
+ __OBJC_$_INSTANCE_METHODS__DPBudgetAuditor
+ __OBJC_$_INSTANCE_METHODS__DPPrio3SumVectorParameter
+ __OBJC_$_INSTANCE_METHODS__DPPrio3SumVectorRandomizer
+ __OBJC_$_INSTANCE_METHODS__DPPrio3SumVectorShim
+ __OBJC_$_INSTANCE_METHODS__DPRenyiDP
+ __OBJC_$_INSTANCE_METHODS__DPSemanticVersion
+ __OBJC_$_INSTANCE_METHODS__DPSymmetricRAPPORWithOHE
+ __OBJC_$_INSTANCE_METHODS__DPTokenFetcher
+ __OBJC_$_INSTANCE_METHODS__DPTransparencyLogMaintainer
+ __OBJC_$_INSTANCE_METHODS__DPVDAFShardResult
+ __OBJC_$_INSTANCE_VARIABLES__DPApproximateDP
+ __OBJC_$_INSTANCE_VARIABLES__DPBudgetAuditor
+ __OBJC_$_INSTANCE_VARIABLES__DPPrio3SumVectorRandomizer
+ __OBJC_$_INSTANCE_VARIABLES__DPRenyiDP
+ __OBJC_$_INSTANCE_VARIABLES__DPSemanticVersion
+ __OBJC_$_INSTANCE_VARIABLES__DPSymmetricRAPPORWithOHE
+ __OBJC_$_INSTANCE_VARIABLES__DPTransparencyLogMaintainer
+ __OBJC_$_PROP_LIST__DPApproximateDP
+ __OBJC_$_PROP_LIST__DPBudgetAuditor
+ __OBJC_$_PROP_LIST__DPPrio3SumVectorRandomizer
+ __OBJC_$_PROP_LIST__DPRenyiDP
+ __OBJC_$_PROP_LIST__DPSemanticVersion
+ __OBJC_$_PROP_LIST__DPSymmetricRAPPORWithOHE
+ __OBJC_$_PROP_LIST__DPTransparencyLogMaintainer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__DPPrivacyBudgetAnalysis
+ __OBJC_$_PROTOCOL_METHOD_TYPES__DPPrivacyBudgetAnalysis
+ __OBJC_CLASS_PROTOCOLS_$__DPPrio3SumVectorRandomizer
+ __OBJC_CLASS_PROTOCOLS_$__DPSymmetricRAPPORWithOHE
+ __OBJC_CLASS_PROTOCOLS_$__DPTokenFetcher
+ __OBJC_CLASS_PROTOCOLS_$__DPTransparencyLogMaintainer
+ __OBJC_CLASS_RO_$__DPApproximateDP
+ __OBJC_CLASS_RO_$__DPBudgetAuditor
+ __OBJC_CLASS_RO_$__DPPrio3SumVectorRandomizer
+ __OBJC_CLASS_RO_$__DPRenyiDP
+ __OBJC_CLASS_RO_$__DPSemanticVersion
+ __OBJC_CLASS_RO_$__DPSymmetricRAPPORWithOHE
+ __OBJC_CLASS_RO_$__DPTokenFetcher
+ __OBJC_CLASS_RO_$__DPTransparencyLogMaintainer
+ __OBJC_LABEL_PROTOCOL_$__DPPrivacyBudgetAnalysis
+ __OBJC_METACLASS_RO_$__DPApproximateDP
+ __OBJC_METACLASS_RO_$__DPBudgetAuditor
+ __OBJC_METACLASS_RO_$__DPPrio3SumVectorRandomizer
+ __OBJC_METACLASS_RO_$__DPRenyiDP
+ __OBJC_METACLASS_RO_$__DPSemanticVersion
+ __OBJC_METACLASS_RO_$__DPSymmetricRAPPORWithOHE
+ __OBJC_METACLASS_RO_$__DPTokenFetcher
+ __OBJC_METACLASS_RO_$__DPTransparencyLogMaintainer
+ __OBJC_PROTOCOL_$__DPPrivacyBudgetAnalysis
+ __PROPERTIES__DPPrio3SumVectorParameter
+ __PROPERTIES__DPVDAFShardResult
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___27+[_DPRenyiDP defaultAlphas]_block_invoke
+ ___32-[_DPTokenFetcher doMaintenance]_block_invoke
+ ___32-[_DPTokenFetcher doMaintenance]_block_invoke.cold.1
+ ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.31
+ ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.31.cold.1
+ ___56-[_DPTokenFetcher scheduleMaintenanceWithName:database:]_block_invoke
+ ___62-[_DPPrioValueRandomizer randomize:withLocalEpsilon:metadata:]_block_invoke
+ ___68-[_DPPrioValueRandomizer randomizeVector:withLocalEpsilon:metadata:]_block_invoke
+ ___69-[_DPTransparencyLogMaintainer scheduleMaintenanceWithName:database:]_block_invoke
+ ___block_descriptor_32_e20_v20?0B8"NSError"12l
+ ___block_literal_global.135
+ ___block_literal_global.137
+ ___block_literal_global.205
+ ___block_literal_global.69
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_DifferentialPrivacy
+ _associated conformance 19DifferentialPrivacy18Prio3SumVectorShimC8VDAFTypeOSHAASQ
+ _defaultAlphas.onceToken
+ _kDPKPTransparencyLogLifetime
+ _kDPMaxCentralDelta
+ _kDPMaxCentralEpsilon
+ _kDPMetadataDediscoTaskConfigDPConfig
+ _kDPMetadataDediscoTaskConfigDPConfigLocalEpsilon
+ _kDPMetadataDediscoTaskConfigDPConfigRenyiAlpha
+ _kDPMetadataDediscoTaskConfigDPConfigTargetCentralDelta
+ _kDPMetadataDediscoTaskConfigDPConfigTargetCentralEpsilon
+ _kDPMetadataDediscoTaskConfigFeatures
+ _kDPMetadataDediscoTaskConfigFeaturesOHTTP
+ _kDPMetadataDediscoTaskConfigFeaturesPAT
+ _kDPMetadataVDAF
+ _kDPMetadataVDAFNonce
+ _kDPMetadataVDAFPrio3SumVectorChunkLength
+ _kDPMetadataVDAFPrio3SumVectorDimension
+ _kDPMetadataVDAFPublicShare
+ _kDPPrioDefaultMinBatchSize
+ _kDPVDAFPrio3NumOfProofs
+ _kDPVDAFPrio3SumVectorBitWidth
+ _kDPVDAFType
+ _kDefaultAlphas
+ _kSecondsIn4Hours
+ _log1p
+ _logaddexp
+ _memset
+ _objc_msgSend$DediscoTokensDirectoryPath
+ _objc_msgSend$addNoiseToData:withLocalEpsilon:withError:
+ _objc_msgSend$addTimeInterval:
+ _objc_msgSend$alpha
+ _objc_msgSend$approximateDPBudgetForDelta:error:
+ _objc_msgSend$approximateDPForDelta:error:
+ _objc_msgSend$auditedMetadataForSymmetricRAPPOR:error:
+ _objc_msgSend$batchSize
+ _objc_msgSend$binomialPMFForN:p:x:logBinomCoef:
+ _objc_msgSend$checkAndRemoveFile:
+ _objc_msgSend$chunkLength
+ _objc_msgSend$cleanupStaleTokensInPath:
+ _objc_msgSend$createSymmetricRAPPORWithError:
+ _objc_msgSend$dataWithContentsOfFile:
+ _objc_msgSend$decodeObjectOfClasses:forKey:
+ _objc_msgSend$defaultAlphas
+ _objc_msgSend$defaultLocalEpsilon
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dimensionFromMetadata:
+ _objc_msgSend$exceed:
+ _objc_msgSend$fetchTokenWithReply:
+ _objc_msgSend$initWithAlpha:tau:error:
+ _objc_msgSend$initWithBatchSize:localEpsilon:error:
+ _objc_msgSend$initWithBitWidth:numOfAggregators:numOfProofs:vdafType:
+ _objc_msgSend$initWithDefaultLocalEpsilon:metadata:plistParameters:error:
+ _objc_msgSend$initWithDefaultLocalEpsilon:metadata:plistParameters:isInternalBuild:error:
+ _objc_msgSend$initWithEpsilon:delta:error:
+ _objc_msgSend$initWithEpsilon:parameters:
+ _objc_msgSend$initWithMajorVersion:minorVersion:patchVersion:
+ _objc_msgSend$inputShares
+ _objc_msgSend$insertIfPossibleObj:intoJSONDictionary:withKey:
+ _objc_msgSend$isDediscoV1:
+ _objc_msgSend$isMetadataValid:plistParameters:error:
+ _objc_msgSend$isValidAlpha:error:
+ _objc_msgSend$isValidDelta:error:
+ _objc_msgSend$isValidEpsilon:error:
+ _objc_msgSend$isValidJSONObject:
+ _objc_msgSend$isValidNumOfProofs:
+ _objc_msgSend$isValidVDAFType:
+ _objc_msgSend$jsonRepresentationForMetadata
+ _objc_msgSend$jsonRepresentationFromParameters:
+ _objc_msgSend$lifetimeOfFile:
+ _objc_msgSend$localEpsilon
+ _objc_msgSend$logBinomialCoefForN:x:prevLogBinomCoef:
+ _objc_msgSend$matchesInString:options:range:
+ _objc_msgSend$nonce
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$parameters
+ _objc_msgSend$patchVersion
+ _objc_msgSend$plistParameters
+ _objc_msgSend$publicShare
+ _objc_msgSend$randomize:withLocalEpsilon:metadata:
+ _objc_msgSend$randomizeBitValue:withLocalEpsilon:metadata:error:
+ _objc_msgSend$randomizeVector:withLocalEpsilon:metadata:
+ _objc_msgSend$randomizeVector:withLocalEpsilon:metadata:error:
+ _objc_msgSend$randomizerWithEpsilon:parameters:
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$recordWithShardResult:metadata:key:
+ _objc_msgSend$renyiDPBudgetsForAlphas:error:
+ _objc_msgSend$service
+ _objc_msgSend$shard:parameter:error:
+ _objc_msgSend$tau
+ _objc_msgSend$transparencyLogLifetime
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _symbolic $sSY
+ _symbolic Say_____G 10Foundation4DataV
+ _symbolic Si
+ _symbolic _____ 19DifferentialPrivacy18Prio3SumVectorShimC
+ _symbolic _____ 19DifferentialPrivacy18Prio3SumVectorShimC11ShardResultC
+ _symbolic _____ 19DifferentialPrivacy18Prio3SumVectorShimC8VDAFTypeO
+ _symbolic _____ 19DifferentialPrivacy18Prio3SumVectorShimC9ParameterC
+ _symbolic _____ s6UInt32V
+ _symbolic _____y_____SWG 4VDAF13SumVectorTypeV AA7Field64V
+ _symbolic _____y_____y_____SWG_____G 4VDAF5Prio3V AA13SumVectorTypeV AA7Field64V AA19XofHmacSha256Aes128C
- +[_DPBSSFPWithOHERandomizer extractLocaleFromKey:]
- +[_DPBSSFPWithOHERandomizer extractSortedTokensFromWordsArray:]
- +[_DPBSSFPWithOHERandomizer randomizerWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:huffmanTableClassName:]
- +[_DPDeviceInfo isDisabledByTaskingForPrio]
- +[_DPPrioError errorWithCode:description:]
- +[_DPPrioError errorWithCode:underlyingError:description:]
- +[_DPPrioValueRandomizer randomizerWithEpsilon:dimensionality:dynamicVectorSize:]
- +[_DPStrings ENReportsDirectoryPath]
- +[_DPStrings unitTestInputDirectoryPath]
- +[_DPUploadHelper writeFileForEN:]
- -[_DPBSFPWithOHE encode:isVerificationMode:segmentIndex:]
- -[_DPBSFPWithOHE encode:isVerificationMode:segmentIndex:].cold.1
- -[_DPBSFPWithOHE encode:isVerificationMode:segmentIndex:].cold.2
- -[_DPBSFPWithOHE encode:isVerificationMode:segmentIndex:].cold.3
- -[_DPBSFPWithOHE initWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:]
- -[_DPBSFPWithOHE initWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:].cold.1
- -[_DPBSFPWithOHE initWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:].cold.2
- -[_DPBSFPWithOHE initWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:].cold.3
- -[_DPBSFPWithOHE init]
- -[_DPBSFPWithOHE privatize:]
- -[_DPBSFPWithOHE privatize:].cold.1
- -[_DPBSFPWithOHE privatize:].cold.2
- -[_DPBSFPWithOHE privatizeWithOHE:isVerificationMode:]
- -[_DPBSFPWithOHEResult .cxx_destruct]
- -[_DPBSFPWithOHEResult initWithBitString:segmentIndex:verificationMode:]
- -[_DPBSFPWithOHEResult init]
- -[_DPBSFPWithOHEResult privatizedString]
- -[_DPBSFPWithOHEResult segmentIndex]
- -[_DPBSFPWithOHEResult verificationMode]
- -[_DPBSSFPWithOHERandomizer .cxx_destruct]
- -[_DPBSSFPWithOHERandomizer bitStringFromEncodedTokens:]
- -[_DPBSSFPWithOHERandomizer bssfpWOHE]
- -[_DPBSSFPWithOHERandomizer hasHuffmanTable]
- -[_DPBSSFPWithOHERandomizer huffmanEncoder]
- -[_DPBSSFPWithOHERandomizer huffmanTableClassNamePattern]
- -[_DPBSSFPWithOHERandomizer initWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:huffmanTableClassName:]
- -[_DPBSSFPWithOHERandomizer init]
- -[_DPBSSFPWithOHERandomizer instantiateLocalizedHuffmanTable:]
- -[_DPBSSFPWithOHERandomizer isLocalizable]
- -[_DPBSSFPWithOHERandomizer maxRecordBitLength]
- -[_DPBSSFPWithOHERandomizer randomize:forKey:]
- -[_DPBSSFPWithOHERandomizer randomizeBitString:huffmanVersion:forKey:]
- -[_DPBSSFPWithOHERandomizer randomizeBitValues:forKey:]
- -[_DPBSSFPWithOHERandomizer randomizeEncodedTokens:huffmanVersion:forKey:]
- -[_DPBSSFPWithOHERandomizer randomizeNumbers:metadata:forKey:]
- -[_DPBSSFPWithOHERandomizer randomizeNumbersVectors:metadata:forKey:]
- -[_DPBSSFPWithOHERandomizer randomizeStrings:forKey:]
- -[_DPBSSFPWithOHERandomizer randomizeWords:fragmentWidth:forKey:]
- -[_DPPrioError initWithCode:description:]
- -[_DPPrioError initWithCode:underlyingError:description:]
- -[_DPPrioReporter defaultRecordsWithValues:key:properties:]
- -[_DPPrioReporter deleteRecordsForKey:storage:]
- -[_DPPrioReporter jsonReportFromObject:]
- -[_DPPrioReporter jsonReportFromObject:].cold.1
- -[_DPPrioReporter jsonReportFromObject:].cold.2
- -[_DPPrioReporter keysWithDefaultValues]
- -[_DPPrioReporter reportPrioKeys:storage:]
- -[_DPPrioReporter reportPrioRecords:]
- -[_DPPrioReporter reportPrioRecords:].cold.1
- -[_DPPrioReporter reportPrioRecords:].cold.2
- -[_DPPrioReporter reportToPrioRecords:forKey:parameters:storage:]
- -[_DPPrioReporter reportToPrioRecords:forKey:parameters:storage:].cold.1
- -[_DPPrioReporter scheduleMaintenanceWithName:database:]
- -[_DPPrioValueRandomizer epsilon]
- -[_DPPrioValueRandomizer initWithEpsilon:dimensionality:dynamicVectorSize:]
- -[_DPPrioValueRandomizer randomize:metadata:]
- -[_DPPrioValueRandomizer randomize:metadata:].cold.1
- -[_DPPrioValueRandomizer randomize:metadata:].cold.2
- -[_DPPrioValueRandomizer randomizeVector:metadata:]
- -[_DPPrioValueRandomizer randomizeVector:metadata:].cold.1
- _OBJC_CLASS_$__DPBSFPWithOHE
- _OBJC_CLASS_$__DPBSFPWithOHEResult
- _OBJC_CLASS_$__DPBSSFPWithOHERandomizer
- _OBJC_CLASS_$__DPPrioError
- _OBJC_CLASS_$__DPPrioReporter
- _OBJC_IVAR_$__DPBSFPWithOHE._epsilon
- _OBJC_IVAR_$__DPBSFPWithOHE._hashSeed
- _OBJC_IVAR_$__DPBSFPWithOHE._hashSeedInVerification
- _OBJC_IVAR_$__DPBSFPWithOHE._maxRecordBitLength
- _OBJC_IVAR_$__DPBSFPWithOHE._numOfSegments
- _OBJC_IVAR_$__DPBSFPWithOHE._probabilityOfVerification
- _OBJC_IVAR_$__DPBSFPWithOHE._segmentBitLength
- _OBJC_IVAR_$__DPBSFPWithOHE._signatureBitLength
- _OBJC_IVAR_$__DPBSFPWithOHE._signatureBitLengthInVerification
- _OBJC_IVAR_$__DPBSFPWithOHEResult._privatizedString
- _OBJC_IVAR_$__DPBSFPWithOHEResult._segmentIndex
- _OBJC_IVAR_$__DPBSFPWithOHEResult._verificationMode
- _OBJC_IVAR_$__DPBSSFPWithOHERandomizer._bssfpWOHE
- _OBJC_IVAR_$__DPBSSFPWithOHERandomizer._hasHuffmanTable
- _OBJC_IVAR_$__DPBSSFPWithOHERandomizer._huffmanEncoder
- _OBJC_IVAR_$__DPBSSFPWithOHERandomizer._huffmanTableClassNamePattern
- _OBJC_IVAR_$__DPBSSFPWithOHERandomizer._isLocalizable
- _OBJC_IVAR_$__DPBSSFPWithOHERandomizer._maxRecordBitLength
- _OBJC_IVAR_$__DPPrioValueRandomizer._epsilon
- _OBJC_METACLASS_$__DPBSFPWithOHE
- _OBJC_METACLASS_$__DPBSFPWithOHEResult
- _OBJC_METACLASS_$__DPBSSFPWithOHERandomizer
- _OBJC_METACLASS_$__DPPrioError
- _OBJC_METACLASS_$__DPPrioReporter
- __DPHuffmanLocalePatternString
- __DPPrioErrorDomain
- __OBJC_$_CLASS_METHODS__DPBSSFPWithOHERandomizer
- __OBJC_$_CLASS_METHODS__DPPrioError
- __OBJC_$_INSTANCE_METHODS__DPBSFPWithOHE
- __OBJC_$_INSTANCE_METHODS__DPBSFPWithOHEResult
- __OBJC_$_INSTANCE_METHODS__DPBSSFPWithOHERandomizer
- __OBJC_$_INSTANCE_METHODS__DPPrioError
- __OBJC_$_INSTANCE_METHODS__DPPrioReporter
- __OBJC_$_INSTANCE_VARIABLES__DPBSFPWithOHE
- __OBJC_$_INSTANCE_VARIABLES__DPBSFPWithOHEResult
- __OBJC_$_INSTANCE_VARIABLES__DPBSSFPWithOHERandomizer
- __OBJC_$_PROP_LIST__DPBSFPWithOHEResult
- __OBJC_$_PROP_LIST__DPBSSFPWithOHERandomizer
- __OBJC_CLASS_PROTOCOLS_$__DPBSSFPWithOHERandomizer
- __OBJC_CLASS_RO_$__DPBSFPWithOHE
- __OBJC_CLASS_RO_$__DPBSFPWithOHEResult
- __OBJC_CLASS_RO_$__DPBSSFPWithOHERandomizer
- __OBJC_CLASS_RO_$__DPPrioError
- __OBJC_CLASS_RO_$__DPPrioReporter
- __OBJC_METACLASS_RO_$__DPBSFPWithOHE
- __OBJC_METACLASS_RO_$__DPBSFPWithOHEResult
- __OBJC_METACLASS_RO_$__DPBSSFPWithOHERandomizer
- __OBJC_METACLASS_RO_$__DPPrioError
- __OBJC_METACLASS_RO_$__DPPrioReporter
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___40-[_DPPrioReporter keysWithDefaultValues]_block_invoke
- ___42-[_DPPrioReporter reportPrioKeys:storage:]_block_invoke
- ___45-[_DPPrioValueRandomizer randomize:metadata:]_block_invoke
- ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.33
- ___46-[_DPDatabaseRecorder recordStrings:metadata:]_block_invoke.33.cold.1
- ___47-[_DPPrioReporter deleteRecordsForKey:storage:]_block_invoke
- ___47-[_DPPrioReporter deleteRecordsForKey:storage:]_block_invoke.cold.1
- ___51-[_DPPrioValueRandomizer randomizeVector:metadata:]_block_invoke
- ___56-[_DPPrioReporter scheduleMaintenanceWithName:database:]_block_invoke
- ___65-[_DPPrioReporter reportToPrioRecords:forKey:parameters:storage:]_block_invoke
- ___65-[_DPPrioReporter reportToPrioRecords:forKey:parameters:storage:]_block_invoke.71
- ___65-[_DPPrioReporter reportToPrioRecords:forKey:parameters:storage:]_block_invoke.71.cold.1
- ___65-[_DPPrioReporter reportToPrioRecords:forKey:parameters:storage:]_block_invoke.71.cold.2
- ___65-[_DPPrioReporter reportToPrioRecords:forKey:parameters:storage:]_block_invoke.cold.1
- ___block_descriptor_40_e20_v20?0B8"NSError"12l
- ___block_descriptor_48_e8_32r_e37_v28?0B8"NSError"12"NSDictionary"20lr32l8
- ___block_descriptor_48_e8_32s40s_e56_v32?0"<_DPStorageMOConversion><_DPJSONString>"8Q16^B24ls32l8s40l8
- ___block_literal_global.198
- ___block_literal_global.29
- ___block_literal_global.71
- ___block_literal_global.96
- ___block_literal_global.98
- ___one_time_setup_block_invoke.cold.7
- __unnamed_array_storage.14
- _kDPAPBitStringSFPwOHEHashSeed
- _kDPAPBitStringSFPwOHEHashSeedInVerification
- _kDPAPBitStringSFPwOHEMaxRecordBitLength
- _kDPAPBitStringSFPwOHEProbabilityOfVerification
- _kDPAPBitStringSFPwOHESegmentBitLength
- _kDPAPBitStringSFPwOHESignatureBitLength
- _kDPAPBitStringSFPwOHESignatureBitLengthInVerification
- _objc_msgSend$ENReportsDirectoryPath
- _objc_msgSend$bitStringFromEncodedTokens:
- _objc_msgSend$bssfpWOHE
- _objc_msgSend$containsString:
- _objc_msgSend$deleteAllRecordsByKey:withCompletion:
- _objc_msgSend$deleteRecordsForKey:storage:
- _objc_msgSend$encode:isVerificationMode:segmentIndex:
- _objc_msgSend$encodeTokens:
- _objc_msgSend$extractLocaleFromKey:
- _objc_msgSend$extractSortedTokensFromWordsArray:
- _objc_msgSend$filteredArrayUsingPredicate:
- _objc_msgSend$hasHuffmanTable
- _objc_msgSend$huffmanEncoder
- _objc_msgSend$huffmanTableClassNamePattern
- _objc_msgSend$initWithBitString:segmentIndex:verificationMode:
- _objc_msgSend$initWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:
- _objc_msgSend$initWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:huffmanTableClassName:
- _objc_msgSend$initWithTableClassName:maxOutputBitLength:
- _objc_msgSend$instantiateLocalizedHuffmanTable:
- _objc_msgSend$isDisabledByTaskingForPrio
- _objc_msgSend$isLocalizable
- _objc_msgSend$isMultiDayIntervalBudgetWithName:
- _objc_msgSend$jsonReportFromObject:
- _objc_msgSend$maxRecordBitLength
- _objc_msgSend$privatize:
- _objc_msgSend$privatizeWithOHE:isVerificationMode:
- _objc_msgSend$privatizedString
- _objc_msgSend$randomize:forKey:
- _objc_msgSend$randomizeBitString:huffmanVersion:forKey:
- _objc_msgSend$randomizeEncodedTokens:huffmanVersion:forKey:
- _objc_msgSend$randomizerWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:huffmanTableClassName:
- _objc_msgSend$reportPrioKeys:storage:
- _objc_msgSend$reportPrioRecords:
- _objc_msgSend$reportToPrioRecords:forKey:parameters:storage:
- _objc_msgSend$submitToPrioShare1:share2:key:parameters:metadata:withReply:
- _objc_msgSend$tableUUID
- _objc_msgSend$writeFileForEN:
CStrings:
+ "\x17\"\x11A"
+ "(%f, %f)-ADP"
+ "/var/mobile/Library/PPM/PAT/"
+ "@\"NSArray\"32@0:8@\"NSArray\"16^@24"
+ "@\"_DPApproximateDP\"32@0:8d16^@24"
+ "@\"_DPPrio3SumVectorParameter\""
+ "@32@0:8d16@24"
+ "@32@0:8d16^@24"
+ "@36@0:8I16d20^@28"
+ "@40@0:8@16@24^@32"
+ "@40@0:8@16d24@32"
+ "@40@0:8Q16Q24Q32"
+ "@40@0:8d16d24^@32"
+ "@44@0:8q16q24q32I40"
+ "@48@0:8@16d24@32^@40"
+ "@48@0:8d16@24@32^@40"
+ "@52@0:8d16@24@32B40^@44"
+ "@56@0:8@16@24@32q40q48"
+ "Approximate-DP delta cannot be 0 when converting Renyi-DP to approximate-DP."
+ "Approximate-DP delta must be not NAN, at least 0.0, and less than 1.0."
+ "Approximate-DP epsilon must be finite, not NAN, and at least 0.0."
+ "B24@0:8q16"
+ "B32@0:8d16^@24"
+ "B40@0:8@16@24^@32"
+ "B40@0:8@16d24^@32"
+ "Batch size = %d, local epsilon = %f will use %@ budget that exceeds the target %@ budget."
+ "Batch size must be greater than 0."
+ "Cannot create _randomizer for _keyProperties = %@"
+ "Cannot load key property for key = %@"
+ "Command (%@) not found"
+ "DP budget auditor using symmetric RAPPOR with min batch size = %d, local epsilon = %f"
+ "DPConfig"
+ "DediscoTokensDirectoryPath"
+ "DefaultMinBatchSize"
+ "DifferentialPrivacy.Parameter"
+ "DifferentialPrivacy.ShardResult"
+ "DifferentialPrivacy/Prio3SumVectorShim.swift"
+ "Donation failed DP auditing check, error=%@"
+ "Donation metadata cannot be nil."
+ "Done to privatize bitValue=%@"
+ "Fail to allocate nonce"
+ "Fail to allocate seed bytes"
+ "Fail to create randomizer"
+ "Fail to fetch dimension"
+ "Fail to find budget for %@"
+ "Fail to find entityName for key=(%@)"
+ "Fail to parse metadata = (%@)"
+ "Fail to privatize bitValue=%@ with error=%@"
+ "Fail to privatize vector=%@ with error=%@"
+ "Failed to analyze Renyi-DP tau. The computed tau is not a finite value."
+ "Failed to convert Renyi-DP to approximate-DP. The converted epsilon is not a valid value."
+ "Failed to create DP budget auditor, error=%@"
+ "Failed to create symmetric RAPPOR in DP budget auditor, error=%@"
+ "Failed to fetch tokens with error: %@"
+ "Failed to parse semantic version from '%@'."
+ "Failed to read the JSON transparency log for file %@ with error %@."
+ "Failed to remove token bucket file %@ with error %@."
+ "Failed to remove transparency log %@ with error %@."
+ "Fatal error"
+ "Features"
+ "Found the key %@ in transparency log %@"
+ "Invalid bitWidth = %@: must be one"
+ "Invalid epsilon = %f"
+ "Invalid epsilon = %f."
+ "Invalid numOfProofs = %@"
+ "Invalid value (%d) at position %zu"
+ "Launching service to fetch tokens"
+ "Local epsilon %f exceeds the maximum allowed local epsilon %f."
+ "LocalEpsilon"
+ "Malformed %@, expected a dictionary."
+ "Malformed parameter (%@) in plist, expected numbers."
+ "Malformed parameter (%@.%@) in metadata, expected a dictionary."
+ "Malformed parameter (%@.%@) in metadata, expected numbers."
+ "Malformed parameter (%@.%@.%@) in metadata, expected numbers."
+ "Malformed plist parameters, expect non-nil parameters."
+ "MaxCentralDelta"
+ "MaxCentralEpsilon"
+ "No key found in the transparency log %@"
+ "No key properties was found for key %@ in file %@"
+ "Nonce"
+ "Not setting target central DP budget in donation metadata."
+ "OHTTP"
+ "Plist parameters cannot be nil."
+ "Prio default dimension p must be provided, and cannot be 0."
+ "Prio3NumberOfProofs"
+ "Prio3SumVectorBitWidth"
+ "Prio3SumVectorChunkLength"
+ "Prio3SumVectorDimension"
+ "Prio3SumVectorField64MultiproofHmacSha256Aes128"
+ "PrivateAccessToken"
+ "PublicShare"
+ "Renyi-DP alpha list cannot be empty"
+ "Renyi-DP alpha must be finite, not NAN, and greater than 1.0."
+ "Renyi-DP tau must be finite, and not NAN."
+ "RenyiAlpha"
+ "Setting target central DP budget in donation metadata to be %@"
+ "Skipping field (%@) expected NSDictionary value, got %@."
+ "Skipping field =(%@) as it cannot be serialized into JSON, type=%@."
+ "Skipping recording for key=%@"
+ "Start to privatize bitValue=%@"
+ "Successfully removed token bucket file %@."
+ "Successfully removed transparency log %@."
+ "T@\"NSArray\",N,R"
+ "T@\"NSData\",N,R"
+ "T@\"NSDictionary\",R,N,V_metadata"
+ "T@\"NSDictionary\",R,N,V_plistParameters"
+ "T@\"NSString\",?,R,C"
+ "T@\"_DPPrio3SumVectorParameter\",R,N,V_parameters"
+ "TB,R,N,V_isInternalBuild"
+ "TI,N,R,VvdafType"
+ "TI,R,N,V_batchSize"
+ "TQ,R,N,V_majorVersion"
+ "TQ,R,N,V_minorVersion"
+ "TQ,R,N,V_patchVersion"
+ "TQ,R,N,V_transparencyLogLifetime"
+ "Target %@ budget exceeds the maximum allowed %@ budget."
+ "Target central DP budget specified by donation metadata: %@"
+ "TargetCentralDelta"
+ "TargetCentralEpsilon"
+ "Td,R,N,V_alpha"
+ "Td,R,N,V_defaultLocalEpsilon"
+ "Td,R,N,V_localEpsilon"
+ "Td,R,N,V_tau"
+ "Tq,N,R,VbitWidth"
+ "Tq,N,R,VchunkLength"
+ "Tq,N,R,Vdimension"
+ "Tq,N,R,VnumOfAggregators"
+ "Tq,N,R,VnumberOfProofs"
+ "TransparencyLogLifetime"
+ "Unknown VDAFType = %@"
+ "Unknown noise distribution = %@."
+ "Unknown privatization algorithm string = %@."
+ "VDAF"
+ "VDAFType"
+ "Version string is not a valid semantic version string. It should specify at least \"<major>.<minor>.<patch>\"."
+ "^(0|[1-9]\\d*)\\.(0|[1-9]\\d*)\\.(0|[1-9]\\d*)(?:-((?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\\.(?:0|[1-9]\\d*|\\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\\+([0-9a-zA-Z-]+(?:\\.[0-9a-zA-Z-]+)*))?$"
+ "_DPApproximateDP"
+ "_DPBudgetAuditor"
+ "_DPPrio3SumVectorParameter"
+ "_DPPrio3SumVectorRandomizer"
+ "_DPPrio3SumVectorShim"
+ "_DPPrivacyBudgetAnalysis"
+ "_DPRenyiDP"
+ "_DPSemanticVersion"
+ "_DPSymmetricRAPPORWithOHE"
+ "_DPTokenFetcher"
+ "_DPTransparencyLogMaintainer"
+ "_DPVDAFShardResult"
+ "_alpha"
+ "_batchSize"
+ "_defaultLocalEpsilon"
+ "_isInternalBuild"
+ "_localEpsilon"
+ "_parameters"
+ "_patchVersion"
+ "_plistParameters"
+ "_tau"
+ "_transparencyLogLifetime"
+ "addNoiseToData:withLocalEpsilon:withError:"
+ "addTimeInterval:"
+ "alpha"
+ "approximateDPBudgetForDelta:error:"
+ "approximateDPForDelta:error:"
+ "auditedMetadataForSymmetricRAPPOR:error:"
+ "batchSize"
+ "binomialPMFForN:p:x:logBinomCoef:"
+ "bitValue=(%@) >= dimension=(%@)"
+ "bitWidth"
+ "checkAndRemoveFile:"
+ "chunkLength"
+ "cleanupStaleTokensInPath:"
+ "com.apple.DifferentialPrivacy.DPPrivacyBudgetError"
+ "com.apple.DifferentialPrivacy.DPVDAFError"
+ "com.apple.DifferentialPrivacy.SemanticVersionError"
+ "com.apple.DifferentialPrivacy.TokenFetcher"
+ "com.apple.DifferentialPrivacy.TransparencyLogMaintenance"
+ "com.apple.differentialprivacy.TokenFetcherHandler"
+ "com.apple.differentialprivacy.TransparencyLogMaintenanceHandler"
+ "createSymmetricRAPPORWithError:"
+ "d32@0:8I16I20d24"
+ "d40@0:8I16d20I28d32"
+ "dataWithContentsOfFile:"
+ "decodeObjectOfClasses:forKey:"
+ "defaultAlphas"
+ "defaultLocalEpsilon"
+ "dictionaryWithDictionary:"
+ "dimension=(%lu) should be less than or equal to %zu"
+ "dimensionFromMetadata:"
+ "exceed:"
+ "fetchTokenWithReply:"
+ "initWithAlpha:tau:error:"
+ "initWithBatchSize:localEpsilon:error:"
+ "initWithBitWidth:numOfAggregators:numOfProofs:vdafType:"
+ "initWithDefaultLocalEpsilon:metadata:plistParameters:error:"
+ "initWithDefaultLocalEpsilon:metadata:plistParameters:isInternalBuild:error:"
+ "initWithEpsilon:delta:error:"
+ "initWithEpsilon:parameters:"
+ "initWithMajorVersion:minorVersion:patchVersion:"
+ "initWithPublicShare:inputShares:nonce:dimension:chunkLength:"
+ "initWithString:error:"
+ "inputShares"
+ "insertIfPossibleObj:intoJSONDictionary:withKey:"
+ "invalid epsilon = %@"
+ "isBackwardCompatibleWithVersion:"
+ "isDediscoV1:"
+ "isMetadataValid:plistParameters:error:"
+ "isValidAlpha:error:"
+ "isValidDelta:error:"
+ "isValidEpsilon:error:"
+ "isValidJSONObject:"
+ "isValidNumOfProofs:"
+ "isValidVDAFType:"
+ "jsonRepresentationForMetadata"
+ "jsonRepresentationFromParameters:"
+ "key(%@) is required in metadata."
+ "lifetimeOfFile:"
+ "localEpsilon"
+ "logAndStoreInError:"
+ "logBinomialCoefForN:x:prevLogBinomCoef:"
+ "matchesInString:options:range:"
+ "nil dataAlgorithmString"
+ "nil privacyParameter"
+ "nil propertiesName"
+ "nil serverAlgorithmString"
+ "nonce"
+ "numOfAggregators"
+ "numberOfProofs"
+ "numberOfRanges"
+ "parameters"
+ "patchVersion"
+ "plistParameters"
+ "publicShare"
+ "randomize:withLocalEpsilon:metadata:"
+ "randomizeBitValue:withLocalEpsilon:metadata:error:"
+ "randomizeVector:withLocalEpsilon:metadata:"
+ "randomizeVector:withLocalEpsilon:metadata:error:"
+ "randomizerWithEpsilon:parameters:"
+ "rangeAtIndex:"
+ "recordWithShardResult:metadata:key:"
+ "renyiDPBudgetsForAlphas:error:"
+ "shard:parameter:error:"
+ "tau"
+ "transparencyLogLifetime"
+ "unknown dataAlgorithmString = %lu"
+ "v24@0:8@?<v@?B@\"NSError\">16"
+ "v24@0:8^@16"
+ "vdafType"
+ "vector must not be nil"
- "\x17\"\x111"
- "%@: Disabled by Tasking - skipping prio reporter"
- "%@: Failed to submit shares to Prio, error: %@"
- "%@: Shares were submitted but submission details are missing!"
- "%@: Shares were submitted to Prio"
- "%@: Treating incoming numbers array as vector %@"
- "%@: failed to delete records for key excluding records %@"
- "%@: failed to extract json from object, exception: %@"
- "*"
- "/AppleInternal/Tests/DifferentialPrivacy/DifferentialPrivacy_tests.xctest/"
- "/var/mobile/Library/Logs/ExposureNotification"
- "@\"_DPBSFPWithOHE\""
- "@\"_DPHuffmanEncoder\""
- "@36@0:8@16B24Q28"
- "@36@0:8@16Q24B32"
- "@80@0:8d16Q24Q32d40Q48Q56Q64Q72"
- "@88@0:8d16Q24Q32d40Q48Q56Q64Q72@80"
- "BitStringSequenceFragmentPuzzleWithOneHotEncoding"
- "DifferentialPrivacyDisablePrio"
- "EN reports directory creation failed with %@"
- "ENReportsDirectoryPath"
- "Fail OHE %@"
- "Fail to encode %@"
- "Invalid epsilon=%f"
- "Invalid maxRecordBitLength=%lu, segmentBitLength=%lu"
- "Invalid probabilityOfVerification=%f"
- "No successful submissions, nothing to write to output report"
- "Report was written to %@"
- "T@\"NSString\",R,C,N,V_privatizedString"
- "T@\"NSString\",R,N,V_huffmanTableClassNamePattern"
- "T@\"_DPBSFPWithOHE\",R,N,V_bssfpWOHE"
- "T@\"_DPHuffmanEncoder\",R,N,V_huffmanEncoder"
- "TB,R,N,V_hasHuffmanTable"
- "TB,R,N,V_isLocalizable"
- "TB,R,N,V_verificationMode"
- "TQ,R,N,V_maxRecordBitLength"
- "TQ,R,N,V_segmentIndex"
- "Telemetry"
- "Updating multi-day queries: %@"
- "_"
- "_DPBSFPWithOHE"
- "_DPBSFPWithOHEResult"
- "_DPBSSFPWithOHERandomizer"
- "_DPPrioError"
- "_DPPrioReporter"
- "_bssfpWOHE"
- "_hasHuffmanTable"
- "_hashSeed"
- "_hashSeedInVerification"
- "_huffmanEncoder"
- "_huffmanTableClassNamePattern"
- "_isLocalizable"
- "_maxRecordBitLength"
- "_numOfSegments"
- "_privatizedString"
- "_probabilityOfVerification"
- "_segmentBitLength"
- "_signatureBitLength"
- "_signatureBitLengthInVerification"
- "bitString is Nil"
- "bitStringFromEncodedTokens:"
- "bssfpWOHE"
- "com.apple.DPPrio"
- "com.apple.DifferentialPrivacy.PrioReporter"
- "com.apple.EN.BeaconCount"
- "com.apple.EN.CodeVerified"
- "com.apple.EN.CodeVerifiedWithReportTypeV2D14"
- "com.apple.EN.DateExposure"
- "com.apple.EN.DateExposureV2D14"
- "com.apple.EN.DiagnosedVaccineStatus"
- "com.apple.EN.KeysUploaded"
- "com.apple.EN.KeysUploadedVaccineStatusV2D14"
- "com.apple.EN.KeysUploadedWithReportTypeV2D14"
- "com.apple.EN.PeriodicExposureNotificationV2D14"
- "com.apple.EN.SecondaryAttackV2D14"
- "com.apple.EN.UserNotification"
- "com.apple.EN.UserNotificationInteraction"
- "com.apple.EN.UserRisk"
- "com.apple.EN.UserRiskParameters"
- "com.apple.differentialprivacy.prioReporterHandler"
- "containsString:"
- "could not create connection to %@"
- "deleteRecordsForKey:storage:"
- "encode:isVerificationMode:segmentIndex:"
- "extractLocaleFromKey:"
- "extractSortedTokensFromWordsArray:"
- "filteredArrayUsingPredicate:"
- "hasHuffmanTable"
- "hashSeed"
- "hashSeedInVerification"
- "huffmanEncoder"
- "huffmanTableClassNamePattern"
- "initWithBitString:segmentIndex:verificationMode:"
- "initWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:"
- "initWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:huffmanTableClassName:"
- "instantiateLocalizedHuffmanTable:"
- "invalid input string: non bit character at %c"
- "invalid input string: size=%lu"
- "isDisabledByTaskingForPrio"
- "isLocalizable"
- "jsonReportFromObject:"
- "maxRecordBitLength"
- "privatize:"
- "privatizeWithOHE:isVerificationMode:"
- "privatizedString"
- "probabilityOfVerification"
- "randomize:forKey:"
- "randomizeBitString:huffmanVersion:forKey:"
- "randomizeEncodedTokens:huffmanVersion:forKey:"
- "randomizerWithEpsilon:maxRecordBitLength:segmentBitLength:probabilityOfVerification:hashSeed:hashSeedInVerification:signatureBitLength:signatureBitLengthInVerification:huffmanTableClassName:"
- "reportPrioKeys:storage:"
- "reportPrioRecords:"
- "reportToPrioRecords:forKey:parameters:storage:"
- "segmentBitLength"
- "signatureBitLength"
- "signatureBitLengthInVerification"
- "submitToPrioShare1:share2:key:parameters:metadata:withReply:"
- "submitting to Prio (records:%lu) key %@"
- "unitTestInputDirectoryPath"
- "v28@?0B8@\"NSError\"12@\"NSDictionary\"20"
- "v32@?0@\"<_DPStorageMOConversion><_DPJSONString>\"8Q16^B24"
- "v64@0:8@\"NSData\"16@\"NSData\"24@\"NSString\"32@\"NSDictionary\"40@\"NSDictionary\"48@?<v@?B@\"NSError\"@\"NSDictionary\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "wordPosition != 0"
- "writeFileForEN:"

```
