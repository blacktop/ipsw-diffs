## DocumentUnderstanding

> `/System/Library/PrivateFrameworks/DocumentUnderstanding.framework/DocumentUnderstanding`

```diff

-116.7.6.0.0
-  __TEXT.__text: 0x1e3c94
-  __TEXT.__auth_stubs: 0x3390
+116.7.7.0.0
+  __TEXT.__text: 0x1dc194
+  __TEXT.__auth_stubs: 0x3320
   __TEXT.__objc_methlist: 0x8f7c
-  __TEXT.__const: 0xc7c8
+  __TEXT.__const: 0xc738
   __TEXT.__dlopen_cstrs: 0xed
-  __TEXT.__cstring: 0xea65
-  __TEXT.__constg_swiftt: 0x5f10
-  __TEXT.__swift5_typeref: 0x2cb8
+  __TEXT.__cstring: 0xe315
+  __TEXT.__constg_swiftt: 0x5ec4
+  __TEXT.__swift5_typeref: 0x2c02
   __TEXT.__swift5_reflstr: 0x4559
-  __TEXT.__swift5_fieldmd: 0x41d0
-  __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_assocty: 0xa68
-  __TEXT.__swift5_proto: 0x7e0
-  __TEXT.__swift5_types: 0x3b8
-  __TEXT.__oslogstring: 0x6293
-  __TEXT.__swift5_capture: 0x7b0
-  __TEXT.__swift_as_entry: 0x274
-  __TEXT.__swift_as_ret: 0x2b8
+  __TEXT.__swift5_fieldmd: 0x41dc
+  __TEXT.__swift5_builtin: 0x17c
+  __TEXT.__swift5_assocty: 0xa50
+  __TEXT.__swift5_proto: 0x7dc
+  __TEXT.__swift5_types: 0x3bc
+  __TEXT.__oslogstring: 0x5d83
+  __TEXT.__swift5_capture: 0x724
+  __TEXT.__swift_as_entry: 0x260
+  __TEXT.__swift_as_ret: 0x29c
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0x4238
-  __TEXT.__unwind_info: 0x7bd8
-  __TEXT.__eh_frame: 0xac9c
+  __TEXT.__unwind_info: 0x7a08
+  __TEXT.__eh_frame: 0xa63c
   __TEXT.__objc_classname: 0x3b3
-  __TEXT.__objc_methname: 0x8087
+  __TEXT.__objc_methname: 0x7fe4
   __TEXT.__objc_methtype: 0xd87
   __TEXT.__objc_stubs: 0x2d20
-  __DATA_CONST.__got: 0xed0
+  __DATA_CONST.__got: 0xe28
   __DATA_CONST.__const: 0x10b0
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x56c8
+  __DATA_CONST.__objc_selrefs: 0x56a8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xd8
-  __AUTH_CONST.__auth_got: 0x19e0
-  __AUTH_CONST.__const: 0x91d8
+  __AUTH_CONST.__auth_got: 0x19a8
+  __AUTH_CONST.__const: 0x9038
   __AUTH_CONST.__cfstring: 0x2c0
-  __AUTH_CONST.__objc_const: 0x9f68
+  __AUTH_CONST.__objc_const: 0x9f40
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x3958
-  __AUTH.__data: 0x3a28
+  __AUTH.__objc_data: 0x39a8
+  __AUTH.__data: 0x3988
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x9d0
   __DATA.__objc_ivar: 0x9c
-  __DATA.__data: 0x2768
+  __DATA.__data: 0x2730
   __DATA.__bss: 0xc3f8
-  __DATA.__common: 0x831
+  __DATA.__common: 0x841
   __DATA_DIRTY.__objc_data: 0x1a38
   __DATA_DIRTY.__data: 0x30d0
   __DATA_DIRTY.__bss: 0x17a8

   - /System/Library/PrivateFrameworks/PromptKit.framework/PromptKit
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TextGeneration.framework/TextGeneration
+  - /System/Library/PrivateFrameworks/TextInput.framework/TextInput
   - /System/Library/PrivateFrameworks/TextUnderstandingShared.framework/TextUnderstandingShared
   - /System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration
   - /System/Library/PrivateFrameworks/Trial.framework/Trial

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 40072E44-DE17-37EB-8F24-358EA012EB50
-  Functions: 13234
-  Symbols:   883
-  CStrings:  4904
+  UUID: DA21324F-7F0E-3A72-AA2C-3127CA92A5FD
+  Functions: 13103
+  Symbols:   884
+  CStrings:  4864
 
Symbols:
+ _OBJC_CLASS_$_TILinguisticAssetDownloadClient
+ _objc_release_x12
- _NLTagSchemeTokenType
CStrings:
+ "Download for asset locale %s has already been requested"
+ "Failed to request download for %s with error: %@"
+ "NLEmbedding is not supported for %s."
+ "Requesting download for asset locale %s, embedding language %s"
+ "Skipping download for language %s as TILinguisticAssetDownloadClient is unavailable on the device."
+ "Successfully requested download for asset locale %s"
+ "_TtC21DocumentUnderstanding32ClassifierModelDownloadInitiator"
+ "classifierModelDownloadInitiator"
+ "logger"
+ "previousDownloadRequestLocales"
+ "requestLinguisticAssetsForLanguage:completion:"
- "C6178FFA-4CF2-46D8-94DC-3255D3B32A02"
- "DUFoundInEventClassificationImplementation: LinguisticData bundle not found, requesting download of NLAsset"
- "DUFoundInEventMultilingualBERTImplementation: Error loading FoundInEvent model head"
- "DUFoundInEventMultilingualBERTImplementation: Error loading bundle for FoundInEvent model head"
- "DUFoundInEventMultilingualBERTImplementation: Error while making FoundInEventMultilingualBERToClassificationModel token prediction"
- "DUFoundInEventMultilingualBERTImplementation: Fail to obtain NLContextualEmbeddingResult with error: %@"
- "DUFoundInEventMultilingualBERTImplementation: Fail to run lstmPredictions with modelHeadWrapper"
- "DUFoundInEventMultilingualBERTImplementation: Failed to chunk text"
- "DUFoundInEventMultilingualBERTImplementation: FoundInEvent no input text"
- "DUFoundInEventMultilingualBERTImplementation: FoundInModels are disabled"
- "DUFoundInEventMultilingualBERTImplementation: NLContextualEmbedding not available"
- "DUFoundInEventMultilingualBERTImplementation: Unable parse CSS inputMapping"
- "DUFoundInEventMultilingualBERTImplementation: Unable parse DD inputMapping"
- "DUFoundInEventMultilingualBERTImplementation: Unable to load FoundInEvent model head"
- "DUFoundInEventMultilingualBERTImplementation: Unable to load engineConfiguration"
- "DUFoundInEventMultilingualBERTImplementation: Unable to load flattenedOutputMapping"
- "DUFoundInEventMultilingualBERTImplementation: Unable to load inputMapping"
- "DUFoundInEventMultilingualBERTImplementation: Unable to load outputMapping"
- "DUFoundInEventMultilingualBERTImplementation: Unable to obtain ContextualEmbedding"
- "DUFoundInEventMultilingualBERTImplementation: Unable to obtain token output mapping from FoundInEventPreprocessingPostprocessingAssets"
- "DUFoundInEventMultilingualBERTImplementation: Unable to return DD Results"
- "DUFoundInEventMultilingualBERTImplementation: Undable to run inference on FoundInEvent model head"
- "DUFoundInEventMultilingualBERTImplementation: cannot find matched max value element for token prediction"
- "DUFoundInEventMultilingualBERTImplementation: cannot find max value element for token %ld"
- "DUFoundInEventMultilingualBERTImplementation: embedding assets not available"
- "DUFoundInEventMultilingualBERTImplementation: error enumerateTokens in NLContextualEmbedding %@"
- "DUFoundInEventMultilingualBERTImplementation: error parsing tokenOutputMapping"
- "DUFoundInEventMultilingualBERTImplementation: fail to requestResult from NLContextualEmbedding"
- "DUFoundInEventMultilingualBERTImplementation: inputArray wrong dimension %ld"
- "DUFoundInEventMultilingualBERTImplementation: nil document received"
- "DUFoundInEventMultilingualBERTImplementation: number of embeddingResults %ld is not consistent with number of shiftedStartLocations %s"
- "DUFoundInEventMultilingualBERTImplementation: unexpected multihot feature %s"
- "DUIDClassificationImplementation: LinguisticData bundle not found, requesting download of NLAsset"
- "DULDAssetUtils: Error when requesting assets %@"
- "DULDAssetUtils: Requesting assets"
- "DULDAssetUtils: did not find embedding for language %s, skipping asset request"
- "DULDAssetUtils: request assets complete, return code %ld"
- "FoundInEventFlattenedOutputMapping"
- "FoundInEventInputMapping"
- "FoundInEventmBERTHead"
- "SGDDMatchDelivery"
- "SGDDMatchEmailAddress"
- "SGDDMatchPostalAddress"
- "_TtC21DocumentUnderstanding44DUFoundInEventMultilingualBERTImplementation"
- "contextualEmbeddingWithIdentifier:"
- "embedding"
- "enumerateTokensForString:language:inRange:error:usingBlock:"
- "hasAvailableAssets"
- "requestAssetsWithCompletionHandler:"
- "requestEmbeddingResultForString:language:completionHandler:"
- "v24@?0@\"NLContextualEmbeddingResult\"8@\"NSError\"16"

```
