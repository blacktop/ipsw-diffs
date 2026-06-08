## SpeechRecognitionCore

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore`

```diff

-6.9.0.0.0
-  __TEXT.__text: 0x122a8
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x7ec
-  __TEXT.__cstring: 0x1395
-  __TEXT.__gcc_except_tab: 0x1058
-  __TEXT.__const: 0xea
-  __TEXT.__oslogstring: 0x470
-  __TEXT.__ustring: 0xc
+34.0.0.0.0
+  __TEXT.__text: 0x1ae9c
+  __TEXT.__objc_methlist: 0xdec
+  __TEXT.__cstring: 0x199d
+  __TEXT.__gcc_except_tab: 0xf90
+  __TEXT.__const: 0x132
+  __TEXT.__ustring: 0x41a
+  __TEXT.__oslogstring: 0x1054
   __TEXT.__swift5_typeref: 0x28
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__unwind_info: 0xa08
-  __TEXT.__objc_classname: 0x12c
-  __TEXT.__objc_methname: 0x1390
-  __TEXT.__objc_methtype: 0x5a8
-  __TEXT.__objc_stubs: 0x9e0
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x460
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__unwind_info: 0xb08
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x4a0
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f8
+  __DATA_CONST.__weak_got: 0x10
+  __DATA_CONST.__objc_selrefs: 0xa28
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x7b0
-  __AUTH_CONST.__const: 0x4f0
-  __AUTH_CONST.__cfstring: 0xcc0
-  __AUTH_CONST.__objc_const: 0xf40
-  __AUTH.__objc_data: 0x230
+  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_arraydata: 0xf40
+  __DATA_CONST.__got: 0x218
+  __AUTH_CONST.__const: 0x5d0
+  __AUTH_CONST.__cfstring: 0x37a0
+  __AUTH_CONST.__objc_const: 0x1ed8
+  __AUTH_CONST.__weak_auth_got: 0x28
+  __AUTH_CONST.__objc_arrayobj: 0x150
+  __AUTH_CONST.__objc_dictobj: 0x1e0
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x7f0
+  __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0xa4
-  __DATA.__data: 0x498
-  __DATA.__bss: 0xe8
-  __DATA.__common: 0x28
+  __DATA.__objc_ivar: 0x17c
+  __DATA.__data: 0x4a8
+  __DATA.__bss: 0x160
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 583A580D-8881-369F-8B71-2041627DC750
-  Functions: 483
-  Symbols:   1542
-  CStrings:  673
+  UUID: C2ACD848-8C73-34E1-B349-AF252A7D47BE
+  Functions: 635
+  Symbols:   2195
+  CStrings:  975
 
Symbols:
+ +[SRDBuiltInLMMatchingCache setCurrentLocale:]
+ +[SRDBuiltInLMMatchingCache sharedCache]
+ +[SRDBuiltInLMMatchingCache sharedCache].cold.1
+ +[SRDCommandMatcher dictationOnlyScore]
+ +[SRDCommandSegment literalSegmentWithText:]
+ +[SRDCommandSegment placeholderSegmentWithIdentifier:isDictation:]
+ +[SRDLinguisticPrefixChecker englishLinguisticPrefixes]
+ +[SRDLinguisticPrefixChecker englishLinguisticPrefixes].cold.1
+ +[SRDLinguisticPrefixChecker isPrefix:linguisticPrefixOf:locale:]
+ +[SRDLinguisticPrefixChecker linguisticPrefixesForLocale:]
+ +[SRDMatchResult noMatchResult]
+ +[SRDParsedCommandTemplate parseSegmentsFromString:identifierLookup:adlibSet:]
+ +[SRDParsedCommandTemplate templateFromString:cacheIdentifiers:adlibIdentifiers:multiMatchIdentifiers:locale:]
+ +[SRDSegmentMatchResult completeWithMatchedObjects:displayString:]
+ +[SRDSegmentMatchResult noMatch]
+ +[SRDSegmentMatchResult prefixWithMatchedObjects:]
+ +[SRDTextNormalizer _localeStripsApostrophes:]
+ +[SRDTextNormalizer lowercaseString:withLocale:]
+ +[SRDTextNormalizer normalizeString:withLocale:]
+ +[SRDTextNormalizer stripApostrophesFromString:locale:]
+ +[SRDTextNormalizer stripApostrophesFromString:locale:].cold.1
+ +[SRDTextNormalizer stripBidiMarks:]
+ +[SRDTextNormalizer stripBidiMarks:].cold.1
+ -[RXXPCCSpeechRecognitionClientService recognizedTranscription:]
+ -[SRDBuiltInLMMatchingCache .cxx_destruct]
+ -[SRDBuiltInLMMatchingCache _currentLocale]
+ -[SRDBuiltInLMMatchingCache addItem:withString:forIdentifier:]
+ -[SRDBuiltInLMMatchingCache beginDeferredUpdatesForIdentifier:]
+ -[SRDBuiltInLMMatchingCache cacheForIdentifier:]
+ -[SRDBuiltInLMMatchingCache clearAllCaches]
+ -[SRDBuiltInLMMatchingCache finalizeDeferredUpdatesForIdentifier:]
+ -[SRDBuiltInLMMatchingCache hasAmbiguousPrefixForItem:forIdentifier:]
+ -[SRDBuiltInLMMatchingCache hasItemWithPrefix:forIdentifier:]
+ -[SRDBuiltInLMMatchingCache init]
+ -[SRDBuiltInLMMatchingCache removeAllItemsForIdentifier:]
+ -[SRDCommandMatcher .cxx_destruct]
+ -[SRDCommandMatcher _appendText:toAttributedString:withQuotes:needsSpacing:]
+ -[SRDCommandMatcher _buildDisplayStringFromMatch:stringIndex:recognizedText:normalization:matchedObjects:variantOverrides:]
+ -[SRDCommandMatcher _buildPrefixCache]
+ -[SRDCommandMatcher _collapseSpellingTokens:]
+ -[SRDCommandMatcher _collapseSpellingTokens:limit:consumedLength:]
+ -[SRDCommandMatcher _collapseSpellingTokens:limit:consumedLength:].cold.1
+ -[SRDCommandMatcher _compileMatchingStrategiesForStrings]
+ -[SRDCommandMatcher _compileMatchingStrategiesForStrings].cold.1
+ -[SRDCommandMatcher _compileMatchingStrategiesForStrings].cold.2
+ -[SRDCommandMatcher _displayTextForCacheKey:items:]
+ -[SRDCommandMatcher _initializeNormalizationMapIfNeeded]
+ -[SRDCommandMatcher _isSpellingQualifiedToken:]
+ -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:]
+ -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.1
+ -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.2
+ -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.3
+ -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.4
+ -[SRDCommandMatcher _matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:]
+ -[SRDCommandMatcher _matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.1
+ -[SRDCommandMatcher _matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.2
+ -[SRDCommandMatcher _matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.3
+ -[SRDCommandMatcher _matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:]
+ -[SRDCommandMatcher _matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.1
+ -[SRDCommandMatcher _matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.2
+ -[SRDCommandMatcher _matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.3
+ -[SRDCommandMatcher _matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:]
+ -[SRDCommandMatcher _matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.1
+ -[SRDCommandMatcher _matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.2
+ -[SRDCommandMatcher _matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:].cold.3
+ -[SRDCommandMatcher _matchingCache]
+ -[SRDCommandMatcher _metadataForStringIndex:]
+ -[SRDCommandMatcher _normalizeRecognizedText:]
+ -[SRDCommandMatcher _normalizeRecognizedTextWithMapping:]
+ -[SRDCommandMatcher _parseTemplatesForStrings]
+ -[SRDCommandMatcher _regexForStringIndex:]
+ -[SRDCommandMatcher _segmentMatchForTranscription:withTemplate:isSpellingMode:]
+ -[SRDCommandMatcher _segmentTemplateForStringIndex:]
+ -[SRDCommandMatcher _strategyForStringIndex:]
+ -[SRDCommandMatcher _wordLevensteinDistance:target:]
+ -[SRDCommandMatcher closeMatchWithTranscriptionResult:]
+ -[SRDCommandMatcher closeMatchWithTranscriptionResult:].cold.1
+ -[SRDCommandMatcher closeMatchWithTranscriptionResult:].cold.2
+ -[SRDCommandMatcher closeMatchWithTranscriptionResult:].cold.3
+ -[SRDCommandMatcher fixedPrefixes]
+ -[SRDCommandMatcher hasNoFixedPrefixString]
+ -[SRDCommandMatcher initWithCommand:locale:builtInLMMatchingCache:localeNeedsInterwordSpaces:adlibIdentifiers:exactMatchLMIdentifiers:multiMatchLMIdentifiers:commandIdentifier:commandStrings:]
+ -[SRDCommandMatcher matchWithTranscriptionResult:]
+ -[SRDCommandMatcher matchWithTranscriptionResult:].cold.1
+ -[SRDCommandMatcher matchWithTranscriptionResult:].cold.2
+ -[SRDCommandMatcher prefixMatchStatusForTranscription:isSpellingMode:]
+ -[SRDCommandSegment .cxx_destruct]
+ -[SRDCommandSegment description]
+ -[SRDCommandSegment identifier]
+ -[SRDCommandSegment text]
+ -[SRDCommandSegment type]
+ -[SRDMatchResult .cxx_destruct]
+ -[SRDMatchResult asrRank]
+ -[SRDMatchResult closeMatchType]
+ -[SRDMatchResult command]
+ -[SRDMatchResult description]
+ -[SRDMatchResult displayString]
+ -[SRDMatchResult initWithCommand:transcriptionResult:matched:score:asrRank:parameters:matchedObjects:displayString:closeMatchType:]
+ -[SRDMatchResult matchedObjects]
+ -[SRDMatchResult matchedTranscriptionString]
+ -[SRDMatchResult matched]
+ -[SRDMatchResult parameters]
+ -[SRDMatchResult score]
+ -[SRDMatchResult transcriptionResult]
+ -[SRDMatchedObject .cxx_destruct]
+ -[SRDMatchedObject captureGroupIndex]
+ -[SRDMatchedObject description]
+ -[SRDMatchedObject initWithObjects:text:captureGroupIndex:]
+ -[SRDMatchedObject items]
+ -[SRDMatchedObject text]
+ -[SRDNormalizedText .cxx_destruct]
+ -[SRDNormalizedText initWithNormalizedString:originalString:normalizedRanges:originalRanges:]
+ -[SRDNormalizedText normalizedRanges]
+ -[SRDNormalizedText normalizedString]
+ -[SRDNormalizedText originalRanges]
+ -[SRDNormalizedText originalString]
+ -[SRDNormalizedText originalTextForNormalizedRange:]
+ -[SRDParsedCommandTemplate .cxx_destruct]
+ -[SRDParsedCommandTemplate description]
+ -[SRDParsedCommandTemplate literalPrefix]
+ -[SRDParsedCommandTemplate originalTemplate]
+ -[SRDParsedCommandTemplate segments]
+ -[SRDPrefixMatchResult initWithStatus:score:]
+ -[SRDPrefixMatchResult score]
+ -[SRDPrefixMatchResult status]
+ -[SRDSegmentMatchResult .cxx_destruct]
+ -[SRDSegmentMatchResult displayString]
+ -[SRDSegmentMatchResult initWithMatchedObjects:prefixMatchStatus:displayString:]
+ -[SRDSegmentMatchResult matchedObjects]
+ -[SRDSegmentMatchResult prefixMatchStatus]
+ -[SRDTranscriptionResult description]
+ -[SRDTranscriptionResult isSpellingMode]
+ -[SRDTranscriptionResult nBestResultStrings]
+ -[SRDTranscriptionResult preITN_nBestResultStrings]
+ -[SRDTranscriptionResult setIsSpellingMode:]
+ -[SRDTranscriptionResult setNBestResultStrings:]
+ -[SRDTranscriptionResult setPreITN_nBestResultStrings:]
+ GCC_except_table18
+ GCC_except_table43
+ GCC_except_table50
+ GCC_except_table6
+ GCC_except_table68
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table95
+ _CACGrammarMatchingShouldLogCommandID
+ _CACGrammarMatchingShouldLogCommandID.cold.1
+ _CACGrammarMatchingShouldLogCommandID.onceToken
+ _CACGrammarMatchingShouldLogCommandID.sFilterEnabled
+ _CACGrammarMatchingShouldLogCommandID.sFilteredCommandIDs
+ _CFCharacterSetCreateInvertedSet
+ _CFPreferencesCopyValue
+ _CFStringGetRangeOfComposedCharactersAtIndex
+ _NSLocaleLanguageCode
+ _NSStringFromClass
+ _OBJC_CLASS_$_NSAssertionHandler
+ _OBJC_CLASS_$_NSAttributedString
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_SRDBuiltInLMMatchingCache
+ _OBJC_CLASS_$_SRDCommandMatcher
+ _OBJC_CLASS_$_SRDCommandSegment
+ _OBJC_CLASS_$_SRDLinguisticPrefixChecker
+ _OBJC_CLASS_$_SRDMatchResult
+ _OBJC_CLASS_$_SRDMatchedObject
+ _OBJC_CLASS_$_SRDNormalizedText
+ _OBJC_CLASS_$_SRDParsedCommandTemplate
+ _OBJC_CLASS_$_SRDPrefixMatchResult
+ _OBJC_CLASS_$_SRDSegmentMatchResult
+ _OBJC_CLASS_$_SRDTextNormalizer
+ _OBJC_IVAR_$_SRDBuiltInLMMatchingCache._cache
+ _OBJC_IVAR_$_SRDBuiltInLMMatchingCache._deferredCache
+ _OBJC_IVAR_$_SRDBuiltInLMMatchingCache._deferredIdentifiers
+ _OBJC_IVAR_$_SRDBuiltInLMMatchingCache._sortedKeys
+ _OBJC_IVAR_$_SRDCommandMatcher._adlibIdentifiers
+ _OBJC_IVAR_$_SRDCommandMatcher._builtInLMMatchingCache
+ _OBJC_IVAR_$_SRDCommandMatcher._command
+ _OBJC_IVAR_$_SRDCommandMatcher._compiled
+ _OBJC_IVAR_$_SRDCommandMatcher._compiledRegexes
+ _OBJC_IVAR_$_SRDCommandMatcher._exactMatchLMIdentifiers
+ _OBJC_IVAR_$_SRDCommandMatcher._fixedPrefixes
+ _OBJC_IVAR_$_SRDCommandMatcher._hasNoFixedPrefixString
+ _OBJC_IVAR_$_SRDCommandMatcher._identifier
+ _OBJC_IVAR_$_SRDCommandMatcher._locale
+ _OBJC_IVAR_$_SRDCommandMatcher._localeNeedsInterwordSpaces
+ _OBJC_IVAR_$_SRDCommandMatcher._localizedSpacebar
+ _OBJC_IVAR_$_SRDCommandMatcher._matchingStrategies
+ _OBJC_IVAR_$_SRDCommandMatcher._multiMatchLMIdentifiers
+ _OBJC_IVAR_$_SRDCommandMatcher._normalizationLanguageCode
+ _OBJC_IVAR_$_SRDCommandMatcher._normalizationMap
+ _OBJC_IVAR_$_SRDCommandMatcher._parsedTemplates
+ _OBJC_IVAR_$_SRDCommandMatcher._prefixesCacheBuilt
+ _OBJC_IVAR_$_SRDCommandMatcher._regexMetadata
+ _OBJC_IVAR_$_SRDCommandMatcher._segmentTemplates
+ _OBJC_IVAR_$_SRDCommandMatcher._strings
+ _OBJC_IVAR_$_SRDCommandSegment._identifier
+ _OBJC_IVAR_$_SRDCommandSegment._text
+ _OBJC_IVAR_$_SRDCommandSegment._type
+ _OBJC_IVAR_$_SRDMatchResult._asrRank
+ _OBJC_IVAR_$_SRDMatchResult._closeMatchType
+ _OBJC_IVAR_$_SRDMatchResult._command
+ _OBJC_IVAR_$_SRDMatchResult._displayString
+ _OBJC_IVAR_$_SRDMatchResult._matched
+ _OBJC_IVAR_$_SRDMatchResult._matchedObjects
+ _OBJC_IVAR_$_SRDMatchResult._parameters
+ _OBJC_IVAR_$_SRDMatchResult._score
+ _OBJC_IVAR_$_SRDMatchResult._transcriptionResult
+ _OBJC_IVAR_$_SRDMatchedObject._captureGroupIndex
+ _OBJC_IVAR_$_SRDMatchedObject._items
+ _OBJC_IVAR_$_SRDMatchedObject._text
+ _OBJC_IVAR_$_SRDNormalizedText._normalizedRanges
+ _OBJC_IVAR_$_SRDNormalizedText._normalizedString
+ _OBJC_IVAR_$_SRDNormalizedText._originalRanges
+ _OBJC_IVAR_$_SRDNormalizedText._originalString
+ _OBJC_IVAR_$_SRDParsedCommandTemplate._originalTemplate
+ _OBJC_IVAR_$_SRDParsedCommandTemplate._segments
+ _OBJC_IVAR_$_SRDPrefixMatchResult._score
+ _OBJC_IVAR_$_SRDPrefixMatchResult._status
+ _OBJC_IVAR_$_SRDSegmentMatchResult._displayString
+ _OBJC_IVAR_$_SRDSegmentMatchResult._matchedObjects
+ _OBJC_IVAR_$_SRDSegmentMatchResult._prefixMatchStatus
+ _OBJC_IVAR_$_SRDTranscriptionResult._isSpellingMode
+ _OBJC_IVAR_$_SRDTranscriptionResult._nBestResultStrings
+ _OBJC_IVAR_$_SRDTranscriptionResult._preITN_nBestResultStrings
+ _OBJC_METACLASS_$_SRDBuiltInLMMatchingCache
+ _OBJC_METACLASS_$_SRDCommandMatcher
+ _OBJC_METACLASS_$_SRDCommandSegment
+ _OBJC_METACLASS_$_SRDLinguisticPrefixChecker
+ _OBJC_METACLASS_$_SRDMatchResult
+ _OBJC_METACLASS_$_SRDMatchedObject
+ _OBJC_METACLASS_$_SRDNormalizedText
+ _OBJC_METACLASS_$_SRDParsedCommandTemplate
+ _OBJC_METACLASS_$_SRDPrefixMatchResult
+ _OBJC_METACLASS_$_SRDSegmentMatchResult
+ _OBJC_METACLASS_$_SRDTextNormalizer
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _SRDLogGrammarMatching
+ _SRDLogGrammarMatching.cold.1
+ _SRDLogGrammarMatching.onceToken
+ _SRDLogGrammarMatching.sLogGrammarMatching
+ __OBJC_$_CLASS_METHODS_SRDBuiltInLMMatchingCache
+ __OBJC_$_CLASS_METHODS_SRDCommandMatcher
+ __OBJC_$_CLASS_METHODS_SRDCommandSegment
+ __OBJC_$_CLASS_METHODS_SRDLinguisticPrefixChecker
+ __OBJC_$_CLASS_METHODS_SRDMatchResult
+ __OBJC_$_CLASS_METHODS_SRDParsedCommandTemplate
+ __OBJC_$_CLASS_METHODS_SRDSegmentMatchResult
+ __OBJC_$_CLASS_METHODS_SRDTextNormalizer
+ __OBJC_$_CLASS_PROP_LIST_SRDCommandMatcher
+ __OBJC_$_INSTANCE_METHODS_SRDBuiltInLMMatchingCache
+ __OBJC_$_INSTANCE_METHODS_SRDCommandMatcher
+ __OBJC_$_INSTANCE_METHODS_SRDCommandSegment
+ __OBJC_$_INSTANCE_METHODS_SRDMatchResult
+ __OBJC_$_INSTANCE_METHODS_SRDMatchedObject
+ __OBJC_$_INSTANCE_METHODS_SRDNormalizedText
+ __OBJC_$_INSTANCE_METHODS_SRDParsedCommandTemplate
+ __OBJC_$_INSTANCE_METHODS_SRDPrefixMatchResult
+ __OBJC_$_INSTANCE_METHODS_SRDSegmentMatchResult
+ __OBJC_$_INSTANCE_VARIABLES_SRDBuiltInLMMatchingCache
+ __OBJC_$_INSTANCE_VARIABLES_SRDCommandMatcher
+ __OBJC_$_INSTANCE_VARIABLES_SRDCommandSegment
+ __OBJC_$_INSTANCE_VARIABLES_SRDMatchResult
+ __OBJC_$_INSTANCE_VARIABLES_SRDMatchedObject
+ __OBJC_$_INSTANCE_VARIABLES_SRDNormalizedText
+ __OBJC_$_INSTANCE_VARIABLES_SRDParsedCommandTemplate
+ __OBJC_$_INSTANCE_VARIABLES_SRDPrefixMatchResult
+ __OBJC_$_INSTANCE_VARIABLES_SRDSegmentMatchResult
+ __OBJC_$_PROP_LIST_SRDCommandMatcher
+ __OBJC_$_PROP_LIST_SRDCommandSegment
+ __OBJC_$_PROP_LIST_SRDMatchResult
+ __OBJC_$_PROP_LIST_SRDMatchedObject
+ __OBJC_$_PROP_LIST_SRDNormalizedText
+ __OBJC_$_PROP_LIST_SRDParsedCommandTemplate
+ __OBJC_$_PROP_LIST_SRDPrefixMatchResult
+ __OBJC_$_PROP_LIST_SRDSegmentMatchResult
+ __OBJC_CLASS_RO_$_SRDBuiltInLMMatchingCache
+ __OBJC_CLASS_RO_$_SRDCommandMatcher
+ __OBJC_CLASS_RO_$_SRDCommandSegment
+ __OBJC_CLASS_RO_$_SRDLinguisticPrefixChecker
+ __OBJC_CLASS_RO_$_SRDMatchResult
+ __OBJC_CLASS_RO_$_SRDMatchedObject
+ __OBJC_CLASS_RO_$_SRDNormalizedText
+ __OBJC_CLASS_RO_$_SRDParsedCommandTemplate
+ __OBJC_CLASS_RO_$_SRDPrefixMatchResult
+ __OBJC_CLASS_RO_$_SRDSegmentMatchResult
+ __OBJC_CLASS_RO_$_SRDTextNormalizer
+ __OBJC_METACLASS_RO_$_SRDBuiltInLMMatchingCache
+ __OBJC_METACLASS_RO_$_SRDCommandMatcher
+ __OBJC_METACLASS_RO_$_SRDCommandSegment
+ __OBJC_METACLASS_RO_$_SRDLinguisticPrefixChecker
+ __OBJC_METACLASS_RO_$_SRDMatchResult
+ __OBJC_METACLASS_RO_$_SRDMatchedObject
+ __OBJC_METACLASS_RO_$_SRDNormalizedText
+ __OBJC_METACLASS_RO_$_SRDParsedCommandTemplate
+ __OBJC_METACLASS_RO_$_SRDPrefixMatchResult
+ __OBJC_METACLASS_RO_$_SRDSegmentMatchResult
+ __OBJC_METACLASS_RO_$_SRDTextNormalizer
+ __ZNKSt3__111__copy_implclB9fqe220100INS_21__tree_const_iteratorIP8RXObjectPNS_11__tree_nodeIS4_PvEElEES9_NS_20back_insert_iteratorINS_6vectorIS4_NS_9allocatorIS4_EEEEEELi0EEENS_4pairIT_T1_EESH_T0_SI_
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE13find_first_ofB9fqe220100EPKcm
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findB9fqe220100ERKS5_m
+ __ZNSt12length_errorC1B9fqe220100EPKc
+ __ZNSt12out_of_rangeC1B9fqe220100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB9fqe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9fqe220100Em
+ __ZNSt3__116__set_differenceB9fqe220100INS_6__lessIvvEERNS_21__tree_const_iteratorIP8RXObjectPNS_11__tree_nodeIS5_PvEElEESB_SB_SB_RNS_20back_insert_iteratorINS_6vectorIS5_NS_9allocatorIS5_EEEEEEEENS_4pairIu14__remove_cvrefIT0_Eu14__remove_cvrefIT4_EEEOSK_OT1_OT2_OT3_OSM_OT_
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIP16RXLanguageObjectEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIP19RXRecognitionSystemEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIP8RXObjectEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIPKvEENS_16allocator_traitsIS4_EEEENS_19__allocation_resultINT0_7pointerENS8_9size_typeEEERT_m
+ __ZNSt3__119__allocate_at_leastB9fqe220100INS_9allocatorIyEENS_16allocator_traitsIS2_EEEENS_19__allocation_resultINT0_7pointerENS6_9size_typeEEERT_m
+ __ZNSt3__120__throw_length_errorB9fqe220100EPKc
+ __ZNSt3__120__throw_out_of_rangeB9fqe220100EPKc
+ __ZNSt3__127__tree_balance_after_insertB9fqe220100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__13setIP8RXObjectNS_4lessIS2_EENS_9allocatorIS2_EEE6insertB9fqe220100ERKS2_
+ __ZNSt3__16__treeIP8RXObjectNS_4lessIS2_EENS_9allocatorIS2_EEE14__tree_deleterclB9fqe220100EPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16vectorIP16RXLanguageObjectNS_9allocatorIS2_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIP16RXLanguageObjectNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP16RXLanguageObjectNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP19RXRecognitionSystemNS_9allocatorIS2_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIP19RXRecognitionSystemNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIP8RXObjectNS_9allocatorIS2_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIP8RXObjectNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJRKS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB9fqe220100Ev
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE24__emplace_back_slow_pathIJyEEEPyDpOT_
+ __ZNSt3__1plB9fqe220100IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_PKS6_
+ __ZNSt3__1plB9fqe220100IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_SB_
+ __ZSt28__throw_bad_array_new_lengthB9fqe220100v
+ __ZZL27RXGetIllegitimateCharactersvE13sIllegitChars
+ __ZZL27RXGetIllegitimateCharactersvE19sInitIllegitCharSet
+ ___36+[SRDTextNormalizer stripBidiMarks:]_block_invoke
+ ___40+[SRDBuiltInLMMatchingCache sharedCache]_block_invoke
+ ___55+[SRDLinguisticPrefixChecker englishLinguisticPrefixes]_block_invoke
+ ___55+[SRDTextNormalizer stripApostrophesFromString:locale:]_block_invoke
+ ___55-[SRDCommandMatcher closeMatchWithTranscriptionResult:]_block_invoke
+ ___55-[SRDCommandMatcher closeMatchWithTranscriptionResult:]_block_invoke.840
+ ___CACGrammarMatchingShouldLogCommandID_block_invoke
+ ___NSDictionary0__struct
+ ___SRDLogGrammarMatching_block_invoke
+ ____ZL27RXGetIllegitimateCharactersv_block_invoke
+ ____ZL27RXGetIllegitimateCharactersv_block_invoke.cold.1
+ ____ZN5RXXPC11ClientEventEPU24objcproto13OS_xpc_object8NSObject_block_invoke.132
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke.129
+ ____ZN5RXXPC19EstablishConnectionEv_block_invoke.130
+ ___block_descriptor_40_e8_32s_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48ls32l8
+ ___block_literal_global.105
+ ___block_literal_global.12
+ ___block_literal_global.135
+ ___block_literal_global.59
+ ___block_literal_global.68
+ ___block_literal_global.72
+ ___block_literal_global.75
+ ___block_literal_global.81
+ ___block_literal_global.970
+ ___block_literal_global.98
+ ___sCurrentLocale
+ __os_log_debug_impl
+ _englishLinguisticPrefixes.onceToken
+ _englishLinguisticPrefixes.prefixes
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _kRDKeyPlaybackAudio
+ _kRDKeySupportsMultiplePartialInvocations
+ _malloc_type_calloc
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_appendText:toAttributedString:withQuotes:needsSpacing:
+ _objc_msgSend$_buildDisplayStringFromMatch:stringIndex:recognizedText:normalization:matchedObjects:variantOverrides:
+ _objc_msgSend$_buildPrefixCache
+ _objc_msgSend$_collapseSpellingTokens:
+ _objc_msgSend$_collapseSpellingTokens:limit:consumedLength:
+ _objc_msgSend$_compileMatchingStrategiesForStrings
+ _objc_msgSend$_currentLocale
+ _objc_msgSend$_displayTextForCacheKey:items:
+ _objc_msgSend$_initializeNormalizationMapIfNeeded
+ _objc_msgSend$_isSpellingQualifiedToken:
+ _objc_msgSend$_localeStripsApostrophes:
+ _objc_msgSend$_matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:
+ _objc_msgSend$_matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:
+ _objc_msgSend$_matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:
+ _objc_msgSend$_matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:
+ _objc_msgSend$_matchingCache
+ _objc_msgSend$_metadataForStringIndex:
+ _objc_msgSend$_normalizeRecognizedText:
+ _objc_msgSend$_normalizeRecognizedTextWithMapping:
+ _objc_msgSend$_parseTemplatesForStrings
+ _objc_msgSend$_regexForStringIndex:
+ _objc_msgSend$_segmentMatchForTranscription:withTemplate:isSpellingMode:
+ _objc_msgSend$_segmentTemplateForStringIndex:
+ _objc_msgSend$_strategyForStringIndex:
+ _objc_msgSend$_wordLevensteinDistance:target:
+ _objc_msgSend$addObject:
+ _objc_msgSend$allKeys
+ _objc_msgSend$appendAttributedString:
+ _objc_msgSend$array
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$asrRank
+ _objc_msgSend$cacheForIdentifier:
+ _objc_msgSend$capitalizedString
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$characterIsMember:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$closeMatchType
+ _objc_msgSend$command
+ _objc_msgSend$compare:
+ _objc_msgSend$completeWithMatchedObjects:displayString:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$componentsSeparatedByCharactersInSet:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$currentHandler
+ _objc_msgSend$decimalDigitCharacterSet
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$displayString
+ _objc_msgSend$englishLinguisticPrefixes
+ _objc_msgSend$enumerateSubstringsInRange:options:usingBlock:
+ _objc_msgSend$escapedPatternForString:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$firstBestResult
+ _objc_msgSend$firstObject
+ _objc_msgSend$formUnionWithCharacterSet:
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$hasAmbiguousPrefixForItem:forIdentifier:
+ _objc_msgSend$hasItemWithPrefix:forIdentifier:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$identifier
+ _objc_msgSend$initWithCommand:transcriptionResult:matched:score:asrRank:parameters:matchedObjects:displayString:closeMatchType:
+ _objc_msgSend$initWithMatchedObjects:prefixMatchStatus:displayString:
+ _objc_msgSend$initWithNormalizedString:originalString:normalizedRanges:originalRanges:
+ _objc_msgSend$initWithObjects:text:captureGroupIndex:
+ _objc_msgSend$initWithStatus:score:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$initWithString:attributes:
+ _objc_msgSend$invertedSet
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isPrefix:linguisticPrefixOf:locale:
+ _objc_msgSend$isSpellingMode
+ _objc_msgSend$items
+ _objc_msgSend$label
+ _objc_msgSend$languageCode
+ _objc_msgSend$linguisticPrefixesForLocale:
+ _objc_msgSend$literalSegmentWithText:
+ _objc_msgSend$localeIdentifier
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$lowercaseLetterCharacterSet
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$lowercaseString:withLocale:
+ _objc_msgSend$lowercaseStringWithLocale:
+ _objc_msgSend$matched
+ _objc_msgSend$matchedObjects
+ _objc_msgSend$matchesInString:options:range:
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$nBestResultStrings
+ _objc_msgSend$noMatch
+ _objc_msgSend$noMatchResult
+ _objc_msgSend$normalizeString:withLocale:
+ _objc_msgSend$normalizedString
+ _objc_msgSend$null
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$originalTextForNormalizedRange:
+ _objc_msgSend$parseSegmentsFromString:identifierLookup:adlibSet:
+ _objc_msgSend$pattern
+ _objc_msgSend$placeholderSegmentWithIdentifier:isDictation:
+ _objc_msgSend$predicateWithFormat:
+ _objc_msgSend$prefixMatchStatus
+ _objc_msgSend$prefixWithMatchedObjects:
+ _objc_msgSend$punctuationCharacterSet
+ _objc_msgSend$range
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$rangeOfString:options:range:
+ _objc_msgSend$rangeValue
+ _objc_msgSend$recognizedTranscription:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$score
+ _objc_msgSend$segments
+ _objc_msgSend$set
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$sharedCache
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$string
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$stripApostrophesFromString:locale:
+ _objc_msgSend$stripBidiMarks:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$symbolCharacterSet
+ _objc_msgSend$templateFromString:cacheIdentifiers:adlibIdentifiers:multiMatchIdentifiers:locale:
+ _objc_msgSend$text
+ _objc_msgSend$transcriptionResult
+ _objc_msgSend$type
+ _objc_msgSend$uppercaseLetterCharacterSet
+ _objc_msgSend$uppercaseString
+ _objc_msgSend$valueWithRange:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_opt_isKindOfClass
+ _objc_opt_new
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x8
+ _sharedCache.onceToken
+ _sharedCache.sharedInstance
+ _stripApostrophesFromString:locale:.apostrophes
+ _stripApostrophesFromString:locale:.onceToken
+ _stripBidiMarks:.bidiMarks
+ _stripBidiMarks:.onceToken
- GCC_except_table40
- GCC_except_table73
- GCC_except_table92
- _RXIsAudioDonationSupported
- _RXIsKeywordSpotterEnabled
- _RXIsLocaleSupportingKeywordSpotter
- _RXIsLocaleSupportingOndeviceSpeechDetection
- _RXIsSpeechDetectorEnabled
- _RXIsVoiceActionsVisionKWSEnabled
- __ZNKSt3__111__copy_implclB9nqe210106INS_21__tree_const_iteratorIP8RXObjectPNS_11__tree_nodeIS4_PvEElEES9_NS_20back_insert_iteratorINS_6vectorIS4_NS_9allocatorIS4_EEEEEEEENS_4pairIT_T1_EESH_T0_SI_
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE13find_first_ofB9nqe210106EPKcm
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE4findB9nqe210106ERKS5_m
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt12out_of_rangeC1B9nqe210106EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_out_of_rangeB9nqe210106Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9nqe210106ILi0EEEPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9nqe210106ENS_24__uninitialized_size_tagEmRKS4_
- __ZNSt3__116__set_differenceB9nqe210106INS_6__lessIvvEERNS_21__tree_const_iteratorIP8RXObjectPNS_11__tree_nodeIS5_PvEElEESB_SB_SB_RNS_20back_insert_iteratorINS_6vectorIS5_NS_9allocatorIS5_EEEEEEEENS_4pairIu14__remove_cvrefIT0_Eu14__remove_cvrefIT4_EEEOSK_OT1_OT2_OT3_OSM_OT_
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIP16RXLanguageObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIP19RXRecognitionSystemEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIP8RXObjectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- __ZNSt3__120__throw_out_of_rangeB9nqe210106EPKc
- __ZNSt3__120back_insert_iteratorINS_6vectorIP8RXObjectNS_9allocatorIS3_EEEEEaSB9nqe210106ERKS3_
- __ZNSt3__121__concatenate_stringsB9nqe210106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS8_NS_15__type_identityINS_17basic_string_viewIS6_S7_EEE4typeESG_
- __ZNSt3__127__tree_balance_after_insertB9nqe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__16__treeIP8RXObjectNS_4lessIS2_EENS_9allocatorIS2_EEE25__emplace_unique_key_argsIS2_JRKS2_EEENS_4pairINS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEbEERKT_DpOT0_
- __ZNSt3__16vectorIP16RXLanguageObjectNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIP8RXObjectNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE9push_backB9nqe210106EOS2_
- __ZNSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__16vectorIyNS_9allocatorIyEEE9push_backB9nqe210106EOy
- __ZNSt3__1plB9nqe210106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_PKS6_
- __ZNSt3__1plB9nqe210106IcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_SB_
- __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- ____ZN5RXXPC11ClientEventEPU24objcproto13OS_xpc_object8NSObject_block_invoke.130
- ____ZN5RXXPC19EstablishConnectionEv_block_invoke.125
- ____ZN5RXXPC19EstablishConnectionEv_block_invoke.126
- ___block_literal_global.101
- ___block_literal_global.133
- ___block_literal_global.58
- ___block_literal_global.66
- ___block_literal_global.70
- ___block_literal_global.73
- ___block_literal_global.79
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "\n\n"
+ "  [%lu] Compiled exact match regex: '%{public}@' -> '%{public}@'"
+ "  [%lu] Compiled placeholder regex: '%{public}@' -> '%{public}@', metadata: %{public}@"
+ "  [%lu] Failed to compile placeholder regex for '%{public}@': %{public}@"
+ "  [%lu] Failed to compile regex for '%{public}@': %{public}@"
+ "  [%lu] Skipping invalid command string: '%{public}@'"
+ "  [%lu] Using segment matching for '%{public}@' (%lu cache placeholders), regex fallback: '%{public}@'"
+ "%@, %@"
+ "'%@'"
+ "'’ʼ"
+ "(.+?)"
+ "0"
+ "1"
+ "10"
+ "11"
+ "12"
+ "14"
+ "15"
+ "16"
+ "17"
+ "18"
+ "19"
+ "2"
+ "20"
+ "21"
+ "22"
+ "23"
+ "24"
+ "25"
+ "26"
+ "27"
+ "28"
+ "29"
+ "3"
+ "30"
+ "31"
+ "32"
+ "33"
+ "34"
+ "35"
+ "36"
+ "37"
+ "38"
+ "39"
+ "4"
+ "40"
+ "41"
+ "42"
+ "43"
+ "44"
+ "45"
+ "46"
+ "47"
+ "48"
+ "49"
+ "5"
+ "50"
+ "51"
+ "52"
+ "53"
+ "54"
+ "55"
+ "56"
+ "57"
+ "58"
+ "59"
+ "6"
+ "60"
+ "61"
+ "62"
+ "63"
+ "64"
+ "65"
+ "66"
+ "67"
+ "68"
+ "69"
+ "7"
+ "70"
+ "71"
+ "72"
+ "73"
+ "74"
+ "75"
+ "76"
+ "77"
+ "78"
+ "79"
+ "8"
+ "80"
+ "81"
+ "82"
+ "83"
+ "84"
+ "85"
+ "86"
+ "87"
+ "88"
+ "89"
+ "9"
+ "90"
+ "91"
+ "92"
+ "93"
+ "94"
+ "95"
+ "96"
+ "97"
+ "98"
+ "99"
+ "<%@: %p matched=%@ score=%.3f asrRank=%lu closeMatchType=%lu \ncommand=%@ \ntranscription=%@ \nmatchedObjects=%@>"
+ "<%@: captureGroupIndex=%lu, text=%@, items=[%@]>"
+ "<%@: utteranceID=%lu, isPartialResult=%d, nBestResultStrings=%@>"
+ "<Dictation: %@>"
+ "<Literal: \"%@\">"
+ "<Placeholder: %@>"
+ "<SRDParsedCommandTemplate: %@ segments=%@>"
+ "CACGrammarMatchingDebugCommandIDs"
+ "Compiling regexes for command '%{public}@' with %lu strings"
+ "Dictation.Streaming"
+ "Finished compiling %lu strings for command '%{public}@'"
+ "GrammarMatching"
+ "IVXLCDM"
+ "SRDCommandMatcher.m"
+ "Spelling mode not supported for non-space delimited languages"
+ "[%{public}@] All %lu placeholders validated for n-best[%lu]"
+ "[%{public}@] Cache hit for '%{public}@'='%{public}@': %lu items"
+ "[%{public}@] Cache miss for '%{public}@'='%{public}@' (key not found)"
+ "[%{public}@] Capture group %lu for '%{public}@': '%{public}@'"
+ "[%{public}@] Close match check: '%{public}@' (normalized)"
+ "[%{public}@] Close match found for '%{public}@' (word distance=1)"
+ "[%{public}@] Dictation placeholder '%{public}@' captured: '%{public}@'"
+ "[%{public}@] Exact match (no placeholders) at n-best[%lu]"
+ "[%{public}@] New best match: score=%.2f, asrRank=%lu"
+ "[%{public}@] No cache available for identifier '%{public}@'"
+ "[%{public}@] No close match found"
+ "[%{public}@] No match found after trying all n-best transcriptions"
+ "[%{public}@] No match: empty transcription"
+ "[%{public}@] Placeholder validation failed: matched %lu of %lu"
+ "[%{public}@] Regex for string %lu matched! numberOfRanges=%lu"
+ "[%{public}@] Returning best match: score=%.2f, asrRank=%lu"
+ "[%{public}@] Segment match: new best match score=%.2f, asrRank=%lu"
+ "[%{public}@] Segment: ambiguous cache match '%{public}@' for '%{public}@'"
+ "[%{public}@] Segment: dictation found literal '%{public}@' at position %lu"
+ "[%{public}@] Segment: dictation placeholder returning prefix (foundPrefixPath=%d)"
+ "[%{public}@] Segment: dictation with no following literal (prefix)"
+ "[%{public}@] Segment: extra text after all segments: '%{public}@'"
+ "[%{public}@] Segment: full match with %lu matched objects"
+ "[%{public}@] Segment: literal '%{public}@' matched"
+ "[%{public}@] Segment: literal '%{public}@' mismatch"
+ "[%{public}@] Segment: multi-match branch for '%{public}@'='%{public}@' result=%lu"
+ "[%{public}@] Segment: no cache for '%{public}@'"
+ "[%{public}@] Segment: no cache key matched for '%{public}@'"
+ "[%{public}@] Segment: prefix path found for '%{public}@'"
+ "[%{public}@] Segment: returning best complete match for '%{public}@' with %lu items"
+ "[%{public}@] Segment: skipping consumed cache key '%{public}@' for '%{public}@'"
+ "[%{public}@] Segment: trailing dictation placeholder (prefix)"
+ "[%{public}@] Segment: transcription exhausted with %lu segments remaining (prefix)"
+ "[%{public}@] Segment: transcription is prefix of cache item for '%{public}@'"
+ "[%{public}@] Segment: transcription is prefix of literal '%{public}@'"
+ "[%{public}@] Segment: trying '%{public}@'='%{public}@'"
+ "[%{public}@] Segment: trying multi-match branch for '%{public}@'='%{public}@'"
+ "[%{public}@] Trying regex for string %lu: '%{public}@'"
+ "[%{public}@] Trying segment matching for string %lu"
+ "\\A"
+ "\\A%@\\z"
+ "\\z"
+ "\\{([^}]+)\\}"
+ "acht"
+ "altı"
+ "and"
+ "az"
+ "beş"
+ "bir"
+ "cero"
+ "cinco"
+ "cinq"
+ "cinque"
+ "com.apple.speech.SpeechRecognitionCommandAndControl"
+ "cuatro"
+ "de"
+ "deux"
+ "dokuz"
+ "dos"
+ "drei"
+ "dua"
+ "due"
+ "dört"
+ "eight"
+ "ein"
+ "eine"
+ "einem"
+ "einen"
+ "einer"
+ "eines"
+ "eins"
+ "elf"
+ "empat"
+ "en"
+ "en-US"
+ "enam"
+ "es"
+ "five"
+ "for"
+ "four"
+ "fr"
+ "fünf"
+ "huit"
+ "iki"
+ "isSpellingMode"
+ "it"
+ "ja"
+ "kRXRecognitionSystemProperty_PlaybackAudio"
+ "ko"
+ "kosong"
+ "lapan"
+ "length > 0"
+ "lima"
+ "matchedUtteranceSilenceStart"
+ "ms"
+ "nBestResultStrings"
+ "neuf"
+ "neun"
+ "nine"
+ "nove"
+ "nueve"
+ "null"
+ "ocho"
+ "one"
+ "otto"
+ "playbackAudio"
+ "preITN_nBestResultStrings"
+ "quatre"
+ "quattro"
+ "ru"
+ "satu"
+ "sechs"
+ "sei"
+ "seis"
+ "sekiz"
+ "sembilan"
+ "sept"
+ "sette"
+ "seven"
+ "sieben"
+ "siete"
+ "sifar"
+ "six"
+ "supportsMultiplePartialInvocations"
+ "sıfır"
+ "th"
+ "th_TH"
+ "three"
+ "tiga"
+ "to"
+ "tr"
+ "tre"
+ "tres"
+ "trois"
+ "tujuh"
+ "two"
+ "un"
+ "una"
+ "une"
+ "uno"
+ "v56@?0@\"NSString\"8{_NSRange=QQ}16{_NSRange=QQ}32^B48"
+ "vier"
+ "yedi"
+ "zehn"
+ "zero"
+ "zh"
+ "zwei"
+ "zwo"
+ "zwölf"
+ "zéro"
+ "{"
+ "üç"
+ "восемь"
+ "два"
+ "две"
+ "девять"
+ "ноль"
+ "нуль"
+ "один"
+ "одна"
+ "одни"
+ "одно"
+ "пять"
+ "семь"
+ "три"
+ "четыре"
+ "шесть"
+ "أربع"
+ "أربعة"
+ "اثنان"
+ "اثنتان"
+ "اثنتين"
+ "اثنين"
+ "تسع"
+ "تسعة"
+ "ثمان"
+ "ثماني"
+ "ثمانية"
+ "ثﻼث"
+ "ثﻼثة"
+ "خمس"
+ "خمسة"
+ "سبع"
+ "سبعة"
+ "ست"
+ "ستة"
+ "صفر"
+ "وأربع"
+ "وأربعة"
+ "واثنان"
+ "واثنتان"
+ "واثنتين"
+ "واثنين"
+ "واحد"
+ "واحدة"
+ "وتسع"
+ "وتسعة"
+ "وثمان"
+ "وثماني"
+ "وثمانية"
+ "وثﻼث"
+ "وثﻼثة"
+ "وخمس"
+ "وخمسة"
+ "وسبع"
+ "وسبعة"
+ "وست"
+ "وستة"
+ "وواحد"
+ "وواحدة"
+ "ศูนย์"
+ "สอง"
+ "สาม"
+ "สี่"
+ "หก"
+ "หนึ่ง"
+ "ห้า"
+ "เก้า"
+ "เจ็ด"
+ "แปด"
+ "๐"
+ "๑"
+ "๒"
+ "๓"
+ "๔"
+ "๕"
+ "๖"
+ "๗"
+ "๘"
+ "๙"
+ "\u200e\u200f"
+ "〇"
+ "一"
+ "七"
+ "三"
+ "两"
+ "九"
+ "二"
+ "五"
+ "兩"
+ "八"
+ "六"
+ "四"
+ "壱"
+ "零"
+ "공"
+ "구"
+ "넉"
+ "네"
+ "넷"
+ "다섯"
+ "두"
+ "둘"
+ "사"
+ "삼"
+ "석"
+ "세"
+ "셋"
+ "아홉"
+ "여덟"
+ "여섯"
+ "영"
+ "오"
+ "육"
+ "이"
+ "일"
+ "일곱"
+ "칠"
+ "팔"
+ "하나"
+ "한"
+ "\xf01"
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SRDClientProtocol>\""
- "@\"<SRDRecognizerDelegate>\""
- "@\"NSArray\""
- "@\"NSLocale\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"SRDMachTime\""
- "@\"SRDTranscriptionResult\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8^{RXXPC=BBBQ^{__CFString}^{__CFString}@@@Q^{__CFArray}Q{_opaque_pthread_mutex_t=q[56c]}}16@24"
- "@32@0:8^{__RXLanguageObject=}16@24"
- "@40@0:8:16@24@32"
- "@40@0:8^{__CFLocale=}16Q24@32"
- "@40@0:8^{__RXRecognitionSystem=}16@24Q32"
- "@80@0:8@16@24@32@40d48B56B60@64@72"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "Q16@0:8"
- "RXXPCCSpeechRecognitionClientService"
- "SRDBrokerProtocol"
- "SRDClientProtocol"
- "SRDConnection"
- "SRDInternalClientProtocol"
- "SRDLanguageObject"
- "SRDMachTime"
- "SRDRecognizer"
- "SRDRecognizer:didRecognize:"
- "SRDTranscriptionResult"
- "SRDTranscriptionToken"
- "T#,R"
- "T@\"NSArray\",&,N,V_nBestResults"
- "T@\"NSArray\",&,N,V_preITN_nBestResults"
- "T@\"NSArray\",&,N,V_preITN_tokenSausage"
- "T@\"NSArray\",&,N,V_tokenSausage"
- "T@\"NSLocale\",&,N,V_locale"
- "T@\"NSString\",&,N,V_firstBestResult"
- "T@\"NSString\",&,N,V_ipaPhoneSequence"
- "T@\"NSString\",&,N,V_phoneSequence"
- "T@\"NSString\",&,N,V_preITN_firstBestResult"
- "T@\"NSString\",&,N,V_tokenName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"SRDMachTime\",&,N,V_end"
- "T@\"SRDMachTime\",&,N,V_silenceStart"
- "T@\"SRDMachTime\",&,N,V_start"
- "T@\"SRDMachTime\",&,N,V_timeAsrResultReceived"
- "T@\"SRDMachTime\",&,N,V_timeCommandExecutionEnded"
- "T@\"SRDMachTime\",&,N,V_timeCommandExecutionStarted"
- "T@\"SRDMachTime\",&,N,V_timeMatchedUtteranceSilenceStart"
- "T@\"SRDMachTime\",&,N,V_timeSRDResponseSent"
- "T@\"SRDMachTime\",&,N,V_timeUtteranceEnd"
- "T@\"SRDMachTime\",&,N,V_timeUtteranceStart"
- "T@\"SRDTranscriptionResult\",&,V_transcriptionResult"
- "TB,N,V_appendedAutoPunctuation"
- "TB,N,V_hasSpaceAfter"
- "TB,N,V_hasSpaceBefore"
- "TB,N,V_isModifiedByAutoPunctuation"
- "TB,N,V_isPartialResult"
- "TB,N,V_prependedAutoPunctuation"
- "TB,R"
- "TQ,N,V_mach_time"
- "TQ,N,V_utteranceID"
- "TQ,R"
- "T^{__RXLanguageObject=},V_languageObject"
- "Td,N,V_confidence"
- "VoiceControl"
- "Vv16@0:8"
- "^{RXXPC=BBBQ^{__CFString}^{__CFString}@@@Q^{__CFArray}Q{_opaque_pthread_mutex_t=q[56c]}}"
- "^{_NSZone=}16@0:8"
- "^{__CFLocale=}"
- "^{__RXLanguageObject=}"
- "^{__RXLanguageObject=}16@0:8"
- "^{__RXRecognitionSystem=}"
- "^{__RXRecognitionSystem=}16@0:8"
- "^{__RXRecognizer=}"
- "^{__RXRecognizer=}16@0:8"
- "_TtP21SpeechRecognitionCore11SRDProtocol_"
- "_appendedAutoPunctuation"
- "_confidence"
- "_delegate"
- "_end"
- "_externalServiceClient"
- "_firstBestResult"
- "_flags"
- "_hasSpaceAfter"
- "_hasSpaceBefore"
- "_ipaPhoneSequence"
- "_isModifiedByAutoPunctuation"
- "_isPartialResult"
- "_languageObject"
- "_locale"
- "_mach_time"
- "_nBestResults"
- "_phoneSequence"
- "_preITN_firstBestResult"
- "_preITN_nBestResults"
- "_preITN_tokenSausage"
- "_prependedAutoPunctuation"
- "_recognitionSystem"
- "_recognizer"
- "_setEndpoint:"
- "_silenceStart"
- "_start"
- "_timeAsrResultReceived"
- "_timeCommandExecutionEnded"
- "_timeCommandExecutionStarted"
- "_timeMatchedUtteranceSilenceStart"
- "_timeSRDResponseSent"
- "_timeUtteranceEnd"
- "_timeUtteranceStart"
- "_tokenName"
- "_tokenSausage"
- "_transcriptionResult"
- "_utteranceID"
- "_xpc"
- "addLeadingContext:"
- "addOtherContext:"
- "appendString:"
- "appendedAutoPunctuation"
- "arrayWithObjects:count:"
- "autorelease"
- "brokerIntro:reply:"
- "caseInsensitiveCompare:"
- "class"
- "clientUpdateWithMessage:"
- "combineTokens:isLocaleWithNoSpaceSeparator:"
- "conformsToProtocol:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "crashServer"
- "d"
- "d16@0:8"
- "dealloc"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeInt64ForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "description"
- "en_CA"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInt64:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "exportedInterface"
- "forwardInvocation:"
- "hash"
- "helloWithObjectID:liveAudio:deviceUID:locale:flags:reply:"
- "init"
- "initWithCoder:"
- "initWithLanguageObject:transcriptionResult:"
- "initWithListenerEndpoint:"
- "initWithLocale:flags:delegate:"
- "initWithMachTime:"
- "initWithRXXPC:externalServiceClient:"
- "initWithRecognitionSystem:delegate:flags:"
- "initWithTokenName:start:end:silenceStart:confidence:hasSpaceAfter:hasSpaceBefore:phoneSequence:ipaPhoneSequence:"
- "interfaceWithProtocol:"
- "invalidate"
- "invokeWithTarget:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isModifiedByAutoPunctuation"
- "isPartialResult"
- "isProxy"
- "languageObject"
- "lastObject"
- "legacyClientEventWithMessage:"
- "legacySendMessage:reply:"
- "length"
- "logUpdates"
- "mach_time"
- "numberWithUnsignedInteger:"
- "objectAtIndexedSubscript:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "phoneticNeighborsWithText:reply:"
- "pingWithObjectID:"
- "pong:"
- "prependedAutoPunctuation"
- "recognitionSystem"
- "recognizedEventWithLegacyMessage:result:"
- "recognizer"
- "release"
- "releaseResult:"
- "remoteObjectProxy"
- "resetRecognition"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "saveUserProfileToFile:"
- "selector"
- "self"
- "sendVitamins"
- "setAppendedAutoPunctuation:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setConfidence:"
- "setEnd:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFirstBestResult:"
- "setHasSpaceAfter:"
- "setHasSpaceBefore:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIpaPhoneSequence:"
- "setIsModifiedByAutoPunctuation:"
- "setIsPartialResult:"
- "setLanguageObject:"
- "setLocale:"
- "setMach_time:"
- "setNBestResults:"
- "setPhoneSequence:"
- "setPreITN_firstBestResult:"
- "setPreITN_nBestResults:"
- "setPreITN_tokenSausage:"
- "setPrependedAutoPunctuation:"
- "setRemoteObjectInterface:"
- "setResetRecognitionMode:"
- "setSecureFieldFocused:"
- "setSilenceStart:"
- "setStart:"
- "setTimeAsrResultReceived:"
- "setTimeCommandExecutionEnded:"
- "setTimeCommandExecutionStarted:"
- "setTimeMatchedUtteranceSilenceStart:"
- "setTimeSRDResponseSent:"
- "setTimeUtteranceEnd:"
- "setTimeUtteranceStart:"
- "setTokenName:"
- "setTokenSausage:"
- "setTranscriptionResult:"
- "setUtteranceID:"
- "setWithArray:"
- "setWithObjects:"
- "stringWithFormat:"
- "substringWithRange:"
- "superclass"
- "supportsSecureCoding"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeAsrResultReceived"
- "timeCommandExecutionEnded"
- "timeCommandExecutionStarted"
- "timeMatchedUtteranceSilenceStart"
- "timeSRDResponseSent"
- "timeUtteranceEnd"
- "timeUtteranceStart"
- "transcriptionResult"
- "unsignedIntegerValue"
- "updateMatchedUtteranceSilenceStart:isLocaleWithNoSpaceSeparator:"
- "use_speech_detector"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8^{__RXLanguageObject=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@16B24"
- "v32@0:8@\"NSDictionary\"16@\"SRDTranscriptionResult\"24"
- "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSXPCListenerEndpoint\">24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v60@0:8q16B24@\"NSString\"28@\"NSString\"36Q44@?<v@?@\"NSString\">52"
- "v60@0:8q16B24@28@36Q44@?52"
- "zone"

```
