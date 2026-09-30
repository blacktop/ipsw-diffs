## com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

-3401.25.3.11.1
-  __TEXT.__text: 0x31970
-  __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_stubs: 0x7cc0
-  __TEXT.__objc_methlist: 0x189c
+3402.62.3.1.3
+  __TEXT.__text: 0x2c1f4
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_stubs: 0x7180
+  __TEXT.__objc_methlist: 0x151c
   __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x1b08
-  __TEXT.__cstring: 0x4062
-  __TEXT.__objc_methname: 0x9b2c
-  __TEXT.__oslogstring: 0x42ba
-  __TEXT.__objc_classname: 0x257
-  __TEXT.__objc_methtype: 0x1911
-  __TEXT.__unwind_info: 0x7e0
-  __DATA_CONST.__auth_got: 0x4c0
-  __DATA_CONST.__got: 0x6d8
+  __TEXT.__gcc_except_tab: 0x1a44
+  __TEXT.__cstring: 0x3d40
+  __TEXT.__objc_methname: 0x8da3
+  __TEXT.__oslogstring: 0x3e7f
+  __TEXT.__objc_classname: 0x212
+  __TEXT.__objc_methtype: 0x1845
+  __TEXT.__unwind_info: 0x6b0
+  __DATA_CONST.__auth_got: 0x488
+  __DATA_CONST.__got: 0x650
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xc60
-  __DATA_CONST.__cfstring: 0x2ac0
-  __DATA_CONST.__objc_classlist: 0xa0
-  __DATA_CONST.__objc_catlist: 0x20
+  __DATA_CONST.__const: 0xb20
+  __DATA_CONST.__cfstring: 0x2900
+  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_intobj: 0xa8
+  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x31b0
-  __DATA.__objc_selrefs: 0x2310
-  __DATA.__objc_ivar: 0x254
-  __DATA.__objc_data: 0x640
+  __DATA.__objc_const: 0x2fb0
+  __DATA.__objc_selrefs: 0x1f78
+  __DATA.__objc_ivar: 0x24c
+  __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x268
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x140
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 627
-  Symbols:   383
-  CStrings:  2410
+  Functions: 540
+  Symbols:   359
+  CStrings:  2233
 
Symbols:
+ _CESRPowerLogEventString
+ _OBJC_CLASS_$_CESRUtilities
+ _earPackageResultCandidateId
+ _setEARPackageResultCandidateId
- _AFBuildVersion
- _AFDeviceSupportsSiriMUX
- _AFIsCustomerInstall
- _AFShouldRunAsrOnServerForUOD
- _NSFileModificationDate
- _NSLocaleCountryCode
- _NSLocaleLanguageCode
- _OBJC_CLASS_$_AFInstanceContext
- _OBJC_CLASS_$_AFSettingsConnection
- _OBJC_CLASS_$_AFSpeechAcousticFeature
- _OBJC_CLASS_$_AFSpeechAudioAnalytics
- _OBJC_CLASS_$_AFSpeechInfoPackage
- _OBJC_CLASS_$_AFSpeechLatticeMitigatorResult
- _OBJC_CLASS_$_AFVoiceCommandGrammarParamMatch
- _OBJC_CLASS_$_AFVoiceCommandGrammarParseCandidate
- _OBJC_CLASS_$_AFVoiceCommandGrammarParsePackage
- _OBJC_CLASS_$_AFVoiceCommandGrammarParseResult
- _OBJC_CLASS_$_CCTypeIdentifierRegistry
- _OBJC_CLASS_$_NSCalendar
- _OBJC_CLASS_$_NSDateFormatter
- _OBJC_CLASS_$_NSTimeZone
- _OBJC_CLASS_$__EARSpeechRecognitionToken
- _OBJC_CLASS_$__EARUserProfileContainer
- _PLLogRegisteredEvent
- _SFMappedLocaleForSpeechProfile
- _SFSpeechProfileSiteDirectories
- _mach_get_times
- _mach_timebase_info
CStrings:
- "%!@(MISSING)-%!@(MISSING)"
- "%!l(MISSING)u"
- "%!s(MISSING) AFSpeechLatticeMitigatorResult Score = %!f(MISSING), Threshold = %!f(MISSING), CalibrationScale = %!f(MISSING), CalibrationOffset = %!f(MISSING)"
- "%!s(MISSING) AFSpeechUtterance at index %!l(MISSING)d will have a nil AFSpeechInterpretation (used for lossless n-best) since the lossless n-best does not have an entry at this index."
- "%!s(MISSING) Categories (%!@(MISSING)) matched no item types"
- "%!s(MISSING) Count of command interpretation sets does not match count of speech recognition results"
- "%!s(MISSING) Failed to resolve item type for field type, error: %!@(MISSING)"
- "%!s(MISSING) Loaded new type of speech profile: path=%!{(MISSING)private}@ profile=%!d(MISSING)"
- "%!s(MISSING) Mapped language=nil"
- "%!s(MISSING) Reused new type of speech profile: path=%!{(MISSING)private}@"
- "%!s(MISSING) Root directories for new type of speech profile: %!{(MISSING)private}@"
- "%!s(MISSING) Size of lossless n-best (%!l(MISSING)d) exceeds size of sausage-based n-best (%!l(MISSING)d); this leads to information loss in the lossless n-best."
- "%!s(MISSING) Size of lossless n-best (%!l(MISSING)d) is less than size of sausage-based n-best (%!l(MISSING)d); this is unexpected."
- "%!s(MISSING) Unable to trigger ABC due to error %!@(MISSING)."
- "%!s(MISSING) loadSpeechProfiles was incorrectly called with profiles=nil"
- "%!s(MISSING) speechProfilePathsWithLanguage was incorrectly called with language=nil"
- "+[CESRSpeechProfileCategoryGroup _buildCachesFromBaseMap:]"
- "+[CESRSpeechProfileCategoryGroup groupForSpeechCategories:]"
- "+[CESRUtilities AFSpeechInfoPackageForEARSpeechRecognitionResultPackage:]_block_invoke"
- "+[CESRUtilities generateABCSnapshotForType:subType:context:]_block_invoke"
- "+[CESRUtilities loadSpeechProfiles:language:]"
- "+[CESRUtilities speechProfilePathsWithLanguage:]"
- "+[CESRUtilities speechProfileRootDirectories]"
- ", "
- "-[CESRSpeechProfileCategoryGroup initWithItemTypes:speechCategories:]"
- "@24@0:8Q16"
- "@28@0:8@16B24"
- "@32@0:8@16Q24"
- "@32@0:8@16d24"
- "@48@0:8@16Q24@32Q40"
- "@48@0:8@16d24B32@36B44"
- "AFPhrasesAndUtterancesForEARSausage"
- "AFSpeechLatticeMitigatorResultForEar"
- "ASR Event"
- "B24@0:8^@16"
- "B24@0:8^{__CFString=}16"
- "CESRSpeechProfileCategoryGroup"
- "CESRUtilities"
- "CESRUtilitiesAdditions"
- "EARUserProfileContainerLoadDate"
- "Param"
- "Q20@0:8f16"
- "Q24@0:8Q16"
- "Q32@0:8d16Q24"
- "ResultCandidateId"
- "SpeechProfile"
- "T@\"NSDate\",C,N"
- "T@\"NSSet\",R,N,V_itemTypes"
- "T@\"NSSet\",R,N,V_speechCategories"
- "UTC"
- "[%!@(MISSING)]"
- "_addAssociatedSpeechCategories:"
- "_alignTokenToFirstSeenPartialResult:tokenIndex:firstSeenPartialResultTokens:firstSeenPartialResultIndex:"
- "_all"
- "_buildCaches"
- "_buildCachesFromBaseMap:"
- "_firstSeenPartialResultIndicesForTokens:firstSeenPartialResultTokens:"
- "_itemTypes"
- "_speechCategories"
- "aFEnableFeatureAndCheckPreferenceValueWithKey:"
- "acousticCost"
- "acousticFeatureValuePerFrame"
- "acousticFeatures"
- "acousticModelVersion"
- "afVoiceCommandGrammarParseResultForEARTokenString:withEARVoiceCommandInterpretations:"
- "all"
- "arguments"
- "attributesOfItemAtPath:error:"
- "audioAnalytics"
- "avoid"
- "bestSupportedLanguageCodeForLanguageCode:"
- "buildVersion"
- "calculateDiffInDaysFromTimestamp:"
- "calibrationOffset"
- "calibrationScale"
- "categoryToFieldTypeMap"
- "commandIdentifier"
- "components:fromDate:toDate:options:"
- "confidenceScore"
- "currentCalendar"
- "currentDictationLanguageCodes"
- "currentSiriLanguageCode"
- "d32@0:8@16Q24"
- "dateWithTimeIntervalSince1970:"
- "day"
- "defaultContext"
- "descriptionForTypeIdentifier:"
- "earTokensForAFTokens:appendedAutoPunctuation:"
- "endOfSentenceLikelihood"
- "endTime"
- "enumerateRangesUsingBlock:"
- "enumeratorAtPath:"
- "f24@0:8Q16"
- "frameDuration"
- "getHostClockFrequency"
- "graphCost"
- "groupForSets:"
- "groupForSpeechCategories:"
- "hasSpaceBefore"
- "indexes"
- "initWithAcousticFeatureValue:frameDuration:"
- "initWithCommandGrammarParsePackage:"
- "initWithCommandId:isComplete:paramMatches:"
- "initWithInstanceContext:"
- "initWithInterpretationIndices:confidenceScore:interpretation:"
- "initWithItemTypes:speechCategories:"
- "initWithNBestParses:preITNNBestParses:"
- "initWithPath:error:"
- "initWithRecognition:rawRecognition:audioAnalytics:isFinal:utteranceStart:"
- "initWithRecognition:unfilteredRecognition:rawRecognition:audioAnalytics:isFinal:utteranceStart:latticeMitigatorResult:recognitionPaused:speechProfileUsed:resultCandidateId:endOfSentenceLikelihood:modelVersion:acousticModelVersion:potentialCommandPrecedingUtterance:potentialCommandUtterance:numOneBestTokensExcludingTriggerPhrase:"
- "initWithResults:score:threshold:calibrationScale:calibrationOffset:"
- "initWithSpeechRecognitionFeatures:acousticFeatures:snr:"
- "initWithText:"
- "initWithTokenName:start:end:silenceStart:confidence:hasSpaceAfter:hasSpaceBefore:phoneSequence:ipaPhoneSequence:appendedAutoPunctuation:"
- "initWithUtterance:parseCandidates:"
- "isASRSupported"
- "isAssistantEnabled"
- "isCustomerInstall"
- "isDictationEnabled"
- "isEqualToSpeechCategoryGroup:"
- "isOfflineDictationSupported"
- "isSamplingSupportedForTask:"
- "isSiriMuxSupported"
- "isSiriUODSupported"
- "isSiriUODwithASROnServerSupported"
- "itemTypeForFieldType:error:"
- "itemTypes"
- "languageCode"
- "languageCodeForLocale:"
- "languageStringForLocaleString:"
- "latticeMitigatorResult"
- "loadDate"
- "localeStringForLanguageString:"
- "mapContextOptionToString:"
- "mergeGroups:"
- "nBestVoiceCommandInterpretations"
- "numTokensExcludingTriggerPhrase"
- "numberWithUnsignedShort:"
- "potentialCommandRecognition"
- "potentialPrecedingRecognition"
- "preITNNBestVoiceCommandInterpretations"
- "preITNVoiceCommandInterpretations"
- "presence"
- "q24@0:8@16"
- "reduced"
- "removeSpaceAfter"
- "removeSpaceBefore"
- "setAcousticCost:"
- "setConfidenceScore:"
- "setGraphCost:"
- "setIsLowConfidence:"
- "setLoadDate:"
- "setTimeZone:"
- "setWithSet:"
- "silenceStartTime"
- "snr"
- "speechCategories"
- "speechCategoriesDescription"
- "speechProfileRootDirectories"
- "speechRecognitionFeatures"
- "startTime"
- "stringByAppendingFormat:"
- "subdataWithRange:"
- "threshold"
- "timeIntervalSinceReferenceDate"
- "timeZoneWithAbbreviation:"
- "triggerABCForType:subType:context:completionHandler:"
- "unconstrained"
- "unionSet:"
- "unsignedShortValue"
- "utterances"
- "v32@?0@\"EARVoiceCommandArgument\"8Q16^B24"
- "v32@?0{_NSRange=QQ}8^B24"
- "voiceCommandInterpretations"
- "voiceCommandsParamKeyBuilder:"
- "{itemTypes: [%!@(MISSING)], speechCategories: [%!@(MISSING)]}"

```
