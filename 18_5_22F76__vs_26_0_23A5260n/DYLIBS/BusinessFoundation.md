## BusinessFoundation

> `/System/Library/PrivateFrameworks/BusinessFoundation.framework/BusinessFoundation`

```diff

-30095.35.3.18.4
-  __TEXT.__text: 0x6fc0
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__const: 0x3f2
+30109.30.5.20.1
+  __TEXT.__text: 0x16e58
+  __TEXT.__auth_stubs: 0xb70
+  __TEXT.__objc_methlist: 0x1194
+  __TEXT.__const: 0x468
   __TEXT.__swift5_typeref: 0x1ea
-  __TEXT.__cstring: 0x22a
+  __TEXT.__cstring: 0x9fc
   __TEXT.__swift5_capture: 0xd4
   __TEXT.__constg_swiftt: 0x2b4
   __TEXT.__swift5_reflstr: 0x11f

   __TEXT.__swift5_types: 0x18
   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__unwind_info: 0x3a8
-  __TEXT.__eh_frame: 0x970
-  __TEXT.__objc_methname: 0x98
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__objc_classlist: 0x18
+  __TEXT.__ustring: 0x5b0
+  __TEXT.__gcc_except_tab: 0x37c
+  __TEXT.__unwind_info: 0x700
+  __TEXT.__eh_frame: 0x978
+  __TEXT.__objc_classname: 0xf1
+  __TEXT.__objc_methname: 0x3f63
+  __TEXT.__objc_methtype: 0x441
+  __TEXT.__objc_stubs: 0x2ac0
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__const: 0x130
+  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x488
-  __AUTH_CONST.__const: 0x328
-  __AUTH_CONST.__objc_const: 0x308
-  __AUTH.__objc_data: 0x50
+  __DATA_CONST.__objc_selrefs: 0xde8
+  __DATA_CONST.__objc_superrefs: 0x48
+  __DATA_CONST.__objc_arraydata: 0x18
+  __AUTH_CONST.__auth_got: 0x5c8
+  __AUTH_CONST.__const: 0x428
+  __AUTH_CONST.__cfstring: 0x1ca0
+  __AUTH_CONST.__objc_const: 0x19b0
+  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x2b0
-  __DATA.__data: 0x258
+  __DATA.__objc_ivar: 0x154
+  __DATA.__data: 0xbaa8
   __DATA.__bss: 0x280
+  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__bss: 0xf0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
+  - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: ACB31810-4CFD-3CA0-A261-DB4A0CDFE3D6
-  Functions: 218
-  Symbols:   221
-  CStrings:  26
+  UUID: 4047C05C-185B-3568-A389-B3FC7D6E0474
+  Functions: 589
+  Symbols:   1572
+  CStrings:  1106
 
Symbols:
+ +[BFPhoneNumberNormalizer countryCode]
+ +[BFPhoneNumberNormalizer normalizedPhoneNumberForPhoneNumber:]
+ +[_NBMetadataHelper CCode2CNMap]
+ +[_NBMetadataHelper CN2CCodeMap]
+ +[_NBMetadataHelper countryCodeFromRegionCode:]
+ +[_NBMetadataHelper hasValue:]
+ +[_NBMetadataHelper jsonObjectFromZippedDataWithBytes:compressedLength:expandedLength:]
+ +[_NBMetadataHelper phoneNumberDataMap]
+ +[_NBMetadataHelper regionCodeFromCountryCode:]
+ +[_NBPhoneNumberUtil initialize]
+ +[_NBPhoneNumberUtil sharedInstance]
+ +[_NBRegularExpressionCache sharedInstance]
+ -[NSArray(_NBAdditions) nb_safeArrayAtIndex:]
+ -[NSArray(_NBAdditions) nb_safeDataAtIndex:]
+ -[NSArray(_NBAdditions) nb_safeNumberAtIndex:]
+ -[NSArray(_NBAdditions) nb_safeObjectAtIndex:class:]
+ -[NSArray(_NBAdditions) nb_safeStringAtIndex:]
+ -[_NBAsYouTypeFormatter .cxx_destruct]
+ -[_NBAsYouTypeFormatter CHARACTER_CLASS_PATTERN_]
+ -[_NBAsYouTypeFormatter DIGIT_PATTERN_]
+ -[_NBAsYouTypeFormatter ELIGIBLE_FORMAT_PATTERN_]
+ -[_NBAsYouTypeFormatter NATIONAL_PREFIX_SEPARATORS_PATTERN_]
+ -[_NBAsYouTypeFormatter STANDALONE_DIGIT_PATTERN_]
+ -[_NBAsYouTypeFormatter ableToExtractLongerNdd_]
+ -[_NBAsYouTypeFormatter ableToFormat_]
+ -[_NBAsYouTypeFormatter accruedInputWithoutFormatting_]
+ -[_NBAsYouTypeFormatter accruedInput_]
+ -[_NBAsYouTypeFormatter appendNationalNumber_:]
+ -[_NBAsYouTypeFormatter attemptToChooseFormattingPattern_]
+ -[_NBAsYouTypeFormatter attemptToChoosePatternWithPrefixExtracted_]
+ -[_NBAsYouTypeFormatter attemptToExtractCountryCallingCode_]
+ -[_NBAsYouTypeFormatter attemptToExtractIdd_]
+ -[_NBAsYouTypeFormatter attemptToFormatAccruedDigits_]
+ -[_NBAsYouTypeFormatter clear]
+ -[_NBAsYouTypeFormatter createFormattingTemplate_:]
+ -[_NBAsYouTypeFormatter currentFormattingPattern_]
+ -[_NBAsYouTypeFormatter currentMetaData_]
+ -[_NBAsYouTypeFormatter currentOutput_]
+ -[_NBAsYouTypeFormatter defaultCountry_]
+ -[_NBAsYouTypeFormatter defaultMetaData_]
+ -[_NBAsYouTypeFormatter description]
+ -[_NBAsYouTypeFormatter formattingTemplate_]
+ -[_NBAsYouTypeFormatter getAvailableFormats_:]
+ -[_NBAsYouTypeFormatter getFormattingTemplate_:numberFormat:]
+ -[_NBAsYouTypeFormatter getMetadataForRegion_:]
+ -[_NBAsYouTypeFormatter getRememberedPosition]
+ -[_NBAsYouTypeFormatter initWithRegionCode:]
+ -[_NBAsYouTypeFormatter initWithRegionCode:bundle:]
+ -[_NBAsYouTypeFormatter init]
+ -[_NBAsYouTypeFormatter inputAccruedNationalNumber_]
+ -[_NBAsYouTypeFormatter inputDigit:]
+ -[_NBAsYouTypeFormatter inputDigitAndRememberPosition:]
+ -[_NBAsYouTypeFormatter inputDigitHelper_:]
+ -[_NBAsYouTypeFormatter inputDigitWithOptionToRememberPosition_:rememberPosition:]
+ -[_NBAsYouTypeFormatter inputHasFormatting_]
+ -[_NBAsYouTypeFormatter inputString:]
+ -[_NBAsYouTypeFormatter inputStringAndRememberPosition:]
+ -[_NBAsYouTypeFormatter isCompleteNumber_]
+ -[_NBAsYouTypeFormatter isDigitOrLeadingPlusSign_:]
+ -[_NBAsYouTypeFormatter isExpectingCountryCallingCode_]
+ -[_NBAsYouTypeFormatter isFormatEligible_:]
+ -[_NBAsYouTypeFormatter isNanpaNumberWithNationalPrefix_]
+ -[_NBAsYouTypeFormatter isSuccessfulFormatting]
+ -[_NBAsYouTypeFormatter lastMatchPosition_]
+ -[_NBAsYouTypeFormatter maybeCreateNewTemplate_]
+ -[_NBAsYouTypeFormatter narrowDownPossibleFormats_:]
+ -[_NBAsYouTypeFormatter nationalNumber_]
+ -[_NBAsYouTypeFormatter nationalPrefixExtracted_]
+ -[_NBAsYouTypeFormatter normalizeAndAccrueDigitsAndPlusSign_:rememberPosition:]
+ -[_NBAsYouTypeFormatter originalPosition_]
+ -[_NBAsYouTypeFormatter phoneUtil_]
+ -[_NBAsYouTypeFormatter positionToRemember_]
+ -[_NBAsYouTypeFormatter possibleFormats_]
+ -[_NBAsYouTypeFormatter prefixBeforeNationalNumber_]
+ -[_NBAsYouTypeFormatter removeLastDigitAndRememberPosition]
+ -[_NBAsYouTypeFormatter removeLastDigit]
+ -[_NBAsYouTypeFormatter removeNationalPrefixFromNationalNumber_]
+ -[_NBAsYouTypeFormatter setAbleToFormat_:]
+ -[_NBAsYouTypeFormatter setAccruedInputWithoutFormatting_:]
+ -[_NBAsYouTypeFormatter setAccruedInput_:]
+ -[_NBAsYouTypeFormatter setCHARACTER_CLASS_PATTERN_:]
+ -[_NBAsYouTypeFormatter setCurrentFormattingPattern_:]
+ -[_NBAsYouTypeFormatter setCurrentMetaData_:]
+ -[_NBAsYouTypeFormatter setCurrentOutput_:]
+ -[_NBAsYouTypeFormatter setDIGIT_PATTERN_:]
+ -[_NBAsYouTypeFormatter setDefaultCountry_:]
+ -[_NBAsYouTypeFormatter setDefaultMetaData_:]
+ -[_NBAsYouTypeFormatter setELIGIBLE_FORMAT_PATTERN_:]
+ -[_NBAsYouTypeFormatter setFormattingTemplate_:]
+ -[_NBAsYouTypeFormatter setInputHasFormatting_:]
+ -[_NBAsYouTypeFormatter setIsCompleteNumber_:]
+ -[_NBAsYouTypeFormatter setIsExpectingCountryCallingCode_:]
+ -[_NBAsYouTypeFormatter setLastMatchPosition_:]
+ -[_NBAsYouTypeFormatter setNATIONAL_PREFIX_SEPARATORS_PATTERN_:]
+ -[_NBAsYouTypeFormatter setNationalNumber_:]
+ -[_NBAsYouTypeFormatter setNationalPrefixExtracted_:]
+ -[_NBAsYouTypeFormatter setOriginalPosition_:]
+ -[_NBAsYouTypeFormatter setPhoneUtil_:]
+ -[_NBAsYouTypeFormatter setPositionToRemember_:]
+ -[_NBAsYouTypeFormatter setPossibleFormats_:]
+ -[_NBAsYouTypeFormatter setPrefixBeforeNationalNumber_:]
+ -[_NBAsYouTypeFormatter setSTANDALONE_DIGIT_PATTERN_:]
+ -[_NBAsYouTypeFormatter setShouldAddSpaceAfterNationalPrefix_:]
+ -[_NBAsYouTypeFormatter shouldAddSpaceAfterNationalPrefix_]
+ -[_NBMetadataHelper .cxx_destruct]
+ -[_NBMetadataHelper getAllMetadata]
+ -[_NBMetadataHelper getMetadataForNonGeographicalRegion:]
+ -[_NBMetadataHelper getMetadataForRegion:]
+ -[_NBMetadataHelper init]
+ -[_NBMetadataHelper metadataCache]
+ -[_NBMetadataHelper setMetadataCache:]
+ -[_NBNumberFormat .cxx_destruct]
+ -[_NBNumberFormat copyWithZone:]
+ -[_NBNumberFormat description]
+ -[_NBNumberFormat domesticCarrierCodeFormattingRule]
+ -[_NBNumberFormat format]
+ -[_NBNumberFormat initWithEntry:]
+ -[_NBNumberFormat initWithPattern:withFormat:withLeadingDigitsPatterns:withNationalPrefixFormattingRule:whenFormatting:withDomesticCarrierCodeFormattingRule:]
+ -[_NBNumberFormat leadingDigitsPatterns]
+ -[_NBNumberFormat nationalPrefixFormattingRule]
+ -[_NBNumberFormat nationalPrefixOptionalWhenFormatting]
+ -[_NBNumberFormat pattern]
+ -[_NBNumberFormat setDomesticCarrierCodeFormattingRule:]
+ -[_NBNumberFormat setFormat:]
+ -[_NBNumberFormat setLeadingDigitsPatterns:]
+ -[_NBNumberFormat setNationalPrefixFormattingRule:]
+ -[_NBNumberFormat setNationalPrefixOptionalWhenFormatting:]
+ -[_NBNumberFormat setPattern:]
+ -[_NBPhoneMetaData .cxx_destruct]
+ -[_NBPhoneMetaData codeID]
+ -[_NBPhoneMetaData countryCode]
+ -[_NBPhoneMetaData description]
+ -[_NBPhoneMetaData emergency]
+ -[_NBPhoneMetaData fixedLine]
+ -[_NBPhoneMetaData generalDesc]
+ -[_NBPhoneMetaData initWithEntry:]
+ -[_NBPhoneMetaData init]
+ -[_NBPhoneMetaData internationalPrefix]
+ -[_NBPhoneMetaData intlNumberFormats]
+ -[_NBPhoneMetaData leadingDigits]
+ -[_NBPhoneMetaData leadingZeroPossible]
+ -[_NBPhoneMetaData mainCountryForCode]
+ -[_NBPhoneMetaData mobile]
+ -[_NBPhoneMetaData nationalPrefixForParsing]
+ -[_NBPhoneMetaData nationalPrefixTransformRule]
+ -[_NBPhoneMetaData nationalPrefix]
+ -[_NBPhoneMetaData noInternationalDialling]
+ -[_NBPhoneMetaData numberFormatsFromEntry:]
+ -[_NBPhoneMetaData numberFormats]
+ -[_NBPhoneMetaData pager]
+ -[_NBPhoneMetaData personalNumber]
+ -[_NBPhoneMetaData preferredExtnPrefix]
+ -[_NBPhoneMetaData preferredInternationalPrefix]
+ -[_NBPhoneMetaData premiumRate]
+ -[_NBPhoneMetaData sameMobileAndFixedLinePattern]
+ -[_NBPhoneMetaData setCodeID:]
+ -[_NBPhoneMetaData setCountryCode:]
+ -[_NBPhoneMetaData setEmergency:]
+ -[_NBPhoneMetaData setFixedLine:]
+ -[_NBPhoneMetaData setGeneralDesc:]
+ -[_NBPhoneMetaData setInternationalPrefix:]
+ -[_NBPhoneMetaData setIntlNumberFormats:]
+ -[_NBPhoneMetaData setLeadingDigits:]
+ -[_NBPhoneMetaData setLeadingZeroPossible:]
+ -[_NBPhoneMetaData setMainCountryForCode:]
+ -[_NBPhoneMetaData setMobile:]
+ -[_NBPhoneMetaData setNationalPrefix:]
+ -[_NBPhoneMetaData setNationalPrefixForParsing:]
+ -[_NBPhoneMetaData setNationalPrefixTransformRule:]
+ -[_NBPhoneMetaData setNoInternationalDialling:]
+ -[_NBPhoneMetaData setNumberFormats:]
+ -[_NBPhoneMetaData setPager:]
+ -[_NBPhoneMetaData setPersonalNumber:]
+ -[_NBPhoneMetaData setPreferredExtnPrefix:]
+ -[_NBPhoneMetaData setPreferredInternationalPrefix:]
+ -[_NBPhoneMetaData setPremiumRate:]
+ -[_NBPhoneMetaData setSameMobileAndFixedLinePattern:]
+ -[_NBPhoneMetaData setSharedCost:]
+ -[_NBPhoneMetaData setTollFree:]
+ -[_NBPhoneMetaData setUan:]
+ -[_NBPhoneMetaData setVoicemail:]
+ -[_NBPhoneMetaData setVoip:]
+ -[_NBPhoneMetaData sharedCost]
+ -[_NBPhoneMetaData tollFree]
+ -[_NBPhoneMetaData uan]
+ -[_NBPhoneMetaData voicemail]
+ -[_NBPhoneMetaData voip]
+ -[_NBPhoneNumber .cxx_destruct]
+ -[_NBPhoneNumber clearCountryCodeSource]
+ -[_NBPhoneNumber copyWithZone:]
+ -[_NBPhoneNumber countryCodeSource]
+ -[_NBPhoneNumber countryCode]
+ -[_NBPhoneNumber description]
+ -[_NBPhoneNumber encodeWithCoder:]
+ -[_NBPhoneNumber extension]
+ -[_NBPhoneNumber getCountryCodeSourceOrDefault]
+ -[_NBPhoneNumber hash]
+ -[_NBPhoneNumber initWithCoder:]
+ -[_NBPhoneNumber init]
+ -[_NBPhoneNumber isEqual:]
+ -[_NBPhoneNumber italianLeadingZero]
+ -[_NBPhoneNumber nationalNumber]
+ -[_NBPhoneNumber numberOfLeadingZeros]
+ -[_NBPhoneNumber preferredDomesticCarrierCode]
+ -[_NBPhoneNumber rawInput]
+ -[_NBPhoneNumber setCountryCode:]
+ -[_NBPhoneNumber setCountryCodeSource:]
+ -[_NBPhoneNumber setExtension:]
+ -[_NBPhoneNumber setItalianLeadingZero:]
+ -[_NBPhoneNumber setNationalNumber:]
+ -[_NBPhoneNumber setNumberOfLeadingZeros:]
+ -[_NBPhoneNumber setPreferredDomesticCarrierCode:]
+ -[_NBPhoneNumber setRawInput:]
+ -[_NBPhoneNumberDesc .cxx_destruct]
+ -[_NBPhoneNumberDesc description]
+ -[_NBPhoneNumberDesc exampleNumber]
+ -[_NBPhoneNumberDesc initWithEntry:]
+ -[_NBPhoneNumberDesc nationalNumberMatcherData]
+ -[_NBPhoneNumberDesc nationalNumberPattern]
+ -[_NBPhoneNumberDesc possibleLengthLocalOnly]
+ -[_NBPhoneNumberDesc possibleLength]
+ -[_NBPhoneNumberDesc possibleNumberMatcherData]
+ -[_NBPhoneNumberDesc possibleNumberPattern]
+ -[_NBPhoneNumberUtil .cxx_destruct]
+ -[_NBPhoneNumberUtil CAPTURING_DIGIT_PATTERN]
+ -[_NBPhoneNumberUtil DIGIT_MAPPINGS]
+ -[_NBPhoneNumberUtil VALID_ALPHA_PHONE_PATTERN]
+ -[_NBPhoneNumberUtil buildNationalNumberForParsing:nationalNumber:]
+ -[_NBPhoneNumberUtil canBeInternationallyDialled:]
+ -[_NBPhoneNumberUtil canBeInternationallyDialled:error:]
+ -[_NBPhoneNumberUtil checkRegionForParsing:defaultRegion:]
+ -[_NBPhoneNumberUtil chooseFormattingPatternForNumber:nationalNumber:]
+ -[_NBPhoneNumberUtil componentsSeparatedByRegex:regex:]
+ -[_NBPhoneNumberUtil convertAlphaCharactersInNumber:]
+ -[_NBPhoneNumberUtil countryCodeByCarrier]
+ -[_NBPhoneNumberUtil descHasPossibleNumberData:]
+ -[_NBPhoneNumberUtil entireRegularExpressionWithPattern:options:error:]
+ -[_NBPhoneNumberUtil entireStringCacheLock]
+ -[_NBPhoneNumberUtil entireStringRegexCache]
+ -[_NBPhoneNumberUtil errorWithObject:withDomain:]
+ -[_NBPhoneNumberUtil extractCountryCode:nationalNumber:]
+ -[_NBPhoneNumberUtil extractPossibleNumber:]
+ -[_NBPhoneNumberUtil format:numberFormat:]
+ -[_NBPhoneNumberUtil format:numberFormat:error:]
+ -[_NBPhoneNumberUtil formatByPattern:numberFormat:userDefinedFormats:]
+ -[_NBPhoneNumberUtil formatByPattern:numberFormat:userDefinedFormats:error:]
+ -[_NBPhoneNumberUtil formatInOriginalFormat:regionCallingFrom:]
+ -[_NBPhoneNumberUtil formatInOriginalFormat:regionCallingFrom:error:]
+ -[_NBPhoneNumberUtil formatNationalNumberWithCarrierCode:carrierCode:]
+ -[_NBPhoneNumberUtil formatNationalNumberWithCarrierCode:carrierCode:error:]
+ -[_NBPhoneNumberUtil formatNationalNumberWithPreferredCarrierCode:fallbackCarrierCode:]
+ -[_NBPhoneNumberUtil formatNationalNumberWithPreferredCarrierCode:fallbackCarrierCode:error:]
+ -[_NBPhoneNumberUtil formatNsn:metadata:phoneNumberFormat:carrierCode:]
+ -[_NBPhoneNumberUtil formatNsnUsingPattern:formattingPattern:numberFormat:carrierCode:]
+ -[_NBPhoneNumberUtil formatNumberForMobileDialing:regionCallingFrom:withFormatting:]
+ -[_NBPhoneNumberUtil formatNumberForMobileDialing:regionCallingFrom:withFormatting:error:]
+ -[_NBPhoneNumberUtil formatOutOfCountryCallingNumber:regionCallingFrom:]
+ -[_NBPhoneNumberUtil formatOutOfCountryCallingNumber:regionCallingFrom:error:]
+ -[_NBPhoneNumberUtil formatOutOfCountryKeepingAlphaChars:regionCallingFrom:]
+ -[_NBPhoneNumberUtil formatOutOfCountryKeepingAlphaChars:regionCallingFrom:error:]
+ -[_NBPhoneNumberUtil formattingRuleHasFirstGroupOnly:]
+ -[_NBPhoneNumberUtil getCountryCodeForRegion:]
+ -[_NBPhoneNumberUtil getCountryCodeForValidRegion:error:]
+ -[_NBPhoneNumberUtil getCountryMobileTokenFromCountryCode:]
+ -[_NBPhoneNumberUtil getExampleNumber:error:]
+ -[_NBPhoneNumberUtil getExampleNumberForNonGeoEntity:error:]
+ -[_NBPhoneNumberUtil getExampleNumberForType:type:error:]
+ -[_NBPhoneNumberUtil getLengthOfGeographicalAreaCode:]
+ -[_NBPhoneNumberUtil getLengthOfGeographicalAreaCode:error:]
+ -[_NBPhoneNumberUtil getLengthOfNationalDestinationCode:]
+ -[_NBPhoneNumberUtil getLengthOfNationalDestinationCode:error:]
+ -[_NBPhoneNumberUtil getMetadataForRegionOrCallingCode:regionCode:]
+ -[_NBPhoneNumberUtil getNationalSignificantNumber:]
+ -[_NBPhoneNumberUtil getNddPrefixForRegion:stripNonDigits:]
+ -[_NBPhoneNumberUtil getNumberDescByType:type:]
+ -[_NBPhoneNumberUtil getNumberType:]
+ -[_NBPhoneNumberUtil getNumberTypeHelper:metadata:]
+ -[_NBPhoneNumberUtil getRegionCodeForCountryCode:]
+ -[_NBPhoneNumberUtil getRegionCodeForNumber:]
+ -[_NBPhoneNumberUtil getRegionCodeForNumberFromRegionList:regionCodes:]
+ -[_NBPhoneNumberUtil getRegionCodesForCountryCode:]
+ -[_NBPhoneNumberUtil getSupportedRegions]
+ -[_NBPhoneNumberUtil hasFormattingPatternForNumber:]
+ -[_NBPhoneNumberUtil hasUnexpectedItalianLeadingZero:]
+ -[_NBPhoneNumberUtil hasValidCountryCallingCode:]
+ -[_NBPhoneNumberUtil helper]
+ -[_NBPhoneNumberUtil indexOfStringByString:target:]
+ -[_NBPhoneNumberUtil initNormalizationMappings]
+ -[_NBPhoneNumberUtil initRegularExpressionSet]
+ -[_NBPhoneNumberUtil init]
+ -[_NBPhoneNumberUtil isAllDigits:]
+ -[_NBPhoneNumberUtil isAlphaNumber:]
+ -[_NBPhoneNumberUtil isLeadingZeroPossible:]
+ -[_NBPhoneNumberUtil isNANPACountry:]
+ -[_NBPhoneNumberUtil isNationalNumberSuffixOfTheOther:second:]
+ -[_NBPhoneNumberUtil isNumberGeographical:]
+ -[_NBPhoneNumberUtil isNumberMatch:second:]
+ -[_NBPhoneNumberUtil isNumberMatch:second:error:]
+ -[_NBPhoneNumberUtil isNumberMatchingDesc:numberDesc:]
+ -[_NBPhoneNumberUtil isPossibleNumber:]
+ -[_NBPhoneNumberUtil isPossibleNumber:error:]
+ -[_NBPhoneNumberUtil isPossibleNumberString:regionDialingFrom:error:]
+ -[_NBPhoneNumberUtil isPossibleNumberWithReason:]
+ -[_NBPhoneNumberUtil isPossibleNumberWithReason:error:]
+ -[_NBPhoneNumberUtil isStartingStringByRegex:regex:]
+ -[_NBPhoneNumberUtil isValidNumber:]
+ -[_NBPhoneNumberUtil isValidNumberForRegion:regionCode:]
+ -[_NBPhoneNumberUtil isValidRegionCode:]
+ -[_NBPhoneNumberUtil isViablePhoneNumber:]
+ -[_NBPhoneNumberUtil lockPatternCache]
+ -[_NBPhoneNumberUtil matchFirstByRegex:regex:]
+ -[_NBPhoneNumberUtil matchedStringByRegex:regex:]
+ -[_NBPhoneNumberUtil matcher]
+ -[_NBPhoneNumberUtil matchesByRegex:regex:]
+ -[_NBPhoneNumberUtil matchesEntirely:string:]
+ -[_NBPhoneNumberUtil maybeExtractCountryCode:metadata:nationalNumber:keepRawInput:phoneNumber:error:]
+ -[_NBPhoneNumberUtil maybeGetFormattedExtension:metadata:numberFormat:]
+ -[_NBPhoneNumberUtil maybeStripExtension:]
+ -[_NBPhoneNumberUtil maybeStripInternationalPrefixAndNormalize:possibleIddPrefix:]
+ -[_NBPhoneNumberUtil maybeStripNationalPrefixAndCarrierCode:metadata:carrierCode:]
+ -[_NBPhoneNumberUtil normalize:]
+ -[_NBPhoneNumberUtil normalizeDiallableCharsOnly:]
+ -[_NBPhoneNumberUtil normalizeDigitsOnly:]
+ -[_NBPhoneNumberUtil normalizeHelper:normalizationReplacements:removeNonMatches:]
+ -[_NBPhoneNumberUtil normalizeSB:]
+ -[_NBPhoneNumberUtil parse:defaultRegion:error:]
+ -[_NBPhoneNumberUtil parseAndKeepRawInput:defaultRegion:error:]
+ -[_NBPhoneNumberUtil parseHelper:defaultRegion:keepRawInput:checkRegion:error:]
+ -[_NBPhoneNumberUtil parsePrefixAsIdd:sourceString:]
+ -[_NBPhoneNumberUtil parseWithPhoneCarrierRegion:error:]
+ -[_NBPhoneNumberUtil prefixNumberWithCountryCallingCode:phoneNumberFormat:formattedNationalNumber:formattedExtension:]
+ -[_NBPhoneNumberUtil rawInputContainsNationalPrefix:nationalPrefix:regionCode:]
+ -[_NBPhoneNumberUtil regexPatternCache]
+ -[_NBPhoneNumberUtil regularExpressionWithPattern:options:error:]
+ -[_NBPhoneNumberUtil replaceFirstStringByRegex:regex:withTemplate:]
+ -[_NBPhoneNumberUtil replaceStringByRegex:regex:withTemplate:]
+ -[_NBPhoneNumberUtil setCAPTURING_DIGIT_PATTERN:]
+ -[_NBPhoneNumberUtil setEntireStringCacheLock:]
+ -[_NBPhoneNumberUtil setEntireStringRegexCache:]
+ -[_NBPhoneNumberUtil setHelper:]
+ -[_NBPhoneNumberUtil setItalianLeadingZerosForPhoneNumber:phoneNumber:]
+ -[_NBPhoneNumberUtil setLockPatternCache:]
+ -[_NBPhoneNumberUtil setMatcher:]
+ -[_NBPhoneNumberUtil setRegexPatternCache:]
+ -[_NBPhoneNumberUtil setVALID_ALPHA_PHONE_PATTERN:]
+ -[_NBPhoneNumberUtil stringByReplacingOccurrencesString:withMap:removeNonMatches:]
+ -[_NBPhoneNumberUtil stringPositionByRegex:regex:]
+ -[_NBPhoneNumberUtil telephonyNetworkInfo]
+ -[_NBPhoneNumberUtil testNumberLength:desc:]
+ -[_NBPhoneNumberUtil truncateTooLongNumber:]
+ -[_NBPhoneNumberUtil validateNumberLength:metadata:]
+ -[_NBPhoneNumberUtil validateNumberLength:metadata:type:]
+ -[_NBRegExMatcher matchNationalNumber:phoneNumberDesc:allowsPrefixMatch:]
+ -[_NBRegularExpressionCache .cxx_destruct]
+ -[_NBRegularExpressionCache cache]
+ -[_NBRegularExpressionCache init]
+ -[_NBRegularExpressionCache regularExpressionForPattern:error:]
+ -[_NBRegularExpressionCache setCache:]
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table3
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table4
+ GCC_except_table43
+ GCC_except_table45
+ GCC_except_table47
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table62
+ GCC_except_table87
+ GCC_except_table92
+ _GEO_MOBILE_COUNTRIES
+ _NB_NON_BREAKING_SPACE
+ _NB_PLUS_CHARS
+ _NB_REGION_CODE_FOR_NON_GEO_ENTITY
+ _NB_UNKNOWN_REGION
+ _NB_VALID_DIGITS_STRING
+ _NSLocaleCountryCode
+ _NSLocaleIdentifier
+ _NSLocalizedDescriptionKey
+ _OBJC_CLASS_$_BFPhoneNumberNormalizer
+ _OBJC_CLASS_$_CTTelephonyNetworkInfo
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSBundle
+ _OBJC_CLASS_$_NSCache
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$__NBAsYouTypeFormatter
+ _OBJC_CLASS_$__NBMetadataHelper
+ _OBJC_CLASS_$__NBNumberFormat
+ _OBJC_CLASS_$__NBPhoneMetaData
+ _OBJC_CLASS_$__NBPhoneNumber
+ _OBJC_CLASS_$__NBPhoneNumberDesc
+ _OBJC_CLASS_$__NBPhoneNumberUtil
+ _OBJC_CLASS_$__NBRegExMatcher
+ _OBJC_CLASS_$__NBRegularExpressionCache
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._CHARACTER_CLASS_PATTERN_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._DIGIT_PATTERN_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._ELIGIBLE_FORMAT_PATTERN_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._NATIONAL_PREFIX_SEPARATORS_PATTERN_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._STANDALONE_DIGIT_PATTERN_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._ableToFormat_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._accruedInputWithoutFormatting_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._accruedInput_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._currentFormattingPattern_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._currentMetaData_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._currentOutput_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._defaultCountry_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._defaultMetaData_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._formattingTemplate_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._inputHasFormatting_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._isCompleteNumber_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._isExpectingCountryCallingCode_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._isSuccessfulFormatting
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._lastMatchPosition_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._nationalNumber_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._nationalPrefixExtracted_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._originalPosition_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._phoneUtil_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._positionToRemember_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._possibleFormats_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._prefixBeforeNationalNumber_
+ _OBJC_IVAR_$__NBAsYouTypeFormatter._shouldAddSpaceAfterNationalPrefix_
+ _OBJC_IVAR_$__NBMetadataHelper._metadataCache
+ _OBJC_IVAR_$__NBNumberFormat._domesticCarrierCodeFormattingRule
+ _OBJC_IVAR_$__NBNumberFormat._format
+ _OBJC_IVAR_$__NBNumberFormat._leadingDigitsPatterns
+ _OBJC_IVAR_$__NBNumberFormat._nationalPrefixFormattingRule
+ _OBJC_IVAR_$__NBNumberFormat._nationalPrefixOptionalWhenFormatting
+ _OBJC_IVAR_$__NBNumberFormat._pattern
+ _OBJC_IVAR_$__NBPhoneMetaData._codeID
+ _OBJC_IVAR_$__NBPhoneMetaData._countryCode
+ _OBJC_IVAR_$__NBPhoneMetaData._emergency
+ _OBJC_IVAR_$__NBPhoneMetaData._fixedLine
+ _OBJC_IVAR_$__NBPhoneMetaData._generalDesc
+ _OBJC_IVAR_$__NBPhoneMetaData._internationalPrefix
+ _OBJC_IVAR_$__NBPhoneMetaData._intlNumberFormats
+ _OBJC_IVAR_$__NBPhoneMetaData._leadingDigits
+ _OBJC_IVAR_$__NBPhoneMetaData._leadingZeroPossible
+ _OBJC_IVAR_$__NBPhoneMetaData._mainCountryForCode
+ _OBJC_IVAR_$__NBPhoneMetaData._mobile
+ _OBJC_IVAR_$__NBPhoneMetaData._nationalPrefix
+ _OBJC_IVAR_$__NBPhoneMetaData._nationalPrefixForParsing
+ _OBJC_IVAR_$__NBPhoneMetaData._nationalPrefixTransformRule
+ _OBJC_IVAR_$__NBPhoneMetaData._noInternationalDialling
+ _OBJC_IVAR_$__NBPhoneMetaData._numberFormats
+ _OBJC_IVAR_$__NBPhoneMetaData._pager
+ _OBJC_IVAR_$__NBPhoneMetaData._personalNumber
+ _OBJC_IVAR_$__NBPhoneMetaData._preferredExtnPrefix
+ _OBJC_IVAR_$__NBPhoneMetaData._preferredInternationalPrefix
+ _OBJC_IVAR_$__NBPhoneMetaData._premiumRate
+ _OBJC_IVAR_$__NBPhoneMetaData._sameMobileAndFixedLinePattern
+ _OBJC_IVAR_$__NBPhoneMetaData._sharedCost
+ _OBJC_IVAR_$__NBPhoneMetaData._tollFree
+ _OBJC_IVAR_$__NBPhoneMetaData._uan
+ _OBJC_IVAR_$__NBPhoneMetaData._voicemail
+ _OBJC_IVAR_$__NBPhoneMetaData._voip
+ _OBJC_IVAR_$__NBPhoneNumber._countryCode
+ _OBJC_IVAR_$__NBPhoneNumber._countryCodeSource
+ _OBJC_IVAR_$__NBPhoneNumber._extension
+ _OBJC_IVAR_$__NBPhoneNumber._italianLeadingZero
+ _OBJC_IVAR_$__NBPhoneNumber._nationalNumber
+ _OBJC_IVAR_$__NBPhoneNumber._numberOfLeadingZeros
+ _OBJC_IVAR_$__NBPhoneNumber._preferredDomesticCarrierCode
+ _OBJC_IVAR_$__NBPhoneNumber._rawInput
+ _OBJC_IVAR_$__NBPhoneNumberDesc._exampleNumber
+ _OBJC_IVAR_$__NBPhoneNumberDesc._nationalNumberMatcherData
+ _OBJC_IVAR_$__NBPhoneNumberDesc._nationalNumberPattern
+ _OBJC_IVAR_$__NBPhoneNumberDesc._possibleLength
+ _OBJC_IVAR_$__NBPhoneNumberDesc._possibleLengthLocalOnly
+ _OBJC_IVAR_$__NBPhoneNumberDesc._possibleNumberMatcherData
+ _OBJC_IVAR_$__NBPhoneNumberDesc._possibleNumberPattern
+ _OBJC_IVAR_$__NBPhoneNumberUtil._CAPTURING_DIGIT_PATTERN
+ _OBJC_IVAR_$__NBPhoneNumberUtil._VALID_ALPHA_PHONE_PATTERN
+ _OBJC_IVAR_$__NBPhoneNumberUtil._entireStringCacheLock
+ _OBJC_IVAR_$__NBPhoneNumberUtil._entireStringRegexCache
+ _OBJC_IVAR_$__NBPhoneNumberUtil._helper
+ _OBJC_IVAR_$__NBPhoneNumberUtil._lockPatternCache
+ _OBJC_IVAR_$__NBPhoneNumberUtil._matcher
+ _OBJC_IVAR_$__NBPhoneNumberUtil._regexPatternCache
+ _OBJC_IVAR_$__NBRegularExpressionCache._cache
+ _OBJC_METACLASS_$_BFPhoneNumberNormalizer
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$__NBAsYouTypeFormatter
+ _OBJC_METACLASS_$__NBMetadataHelper
+ _OBJC_METACLASS_$__NBNumberFormat
+ _OBJC_METACLASS_$__NBPhoneMetaData
+ _OBJC_METACLASS_$__NBPhoneNumber
+ _OBJC_METACLASS_$__NBPhoneNumberDesc
+ _OBJC_METACLASS_$__NBPhoneNumberUtil
+ _OBJC_METACLASS_$__NBRegExMatcher
+ _OBJC_METACLASS_$__NBRegularExpressionCache
+ _StringByTrimming
+ __MergedGlobals
+ __NSConcreteGlobalBlock
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$__NBAdditions
+ __OBJC_$_CATEGORY_NSArray_$__NBAdditions
+ __OBJC_$_CLASS_METHODS_BFPhoneNumberNormalizer
+ __OBJC_$_CLASS_METHODS__NBMetadataHelper
+ __OBJC_$_CLASS_METHODS__NBPhoneNumberUtil
+ __OBJC_$_CLASS_METHODS__NBRegularExpressionCache
+ __OBJC_$_INSTANCE_METHODS__NBAsYouTypeFormatter
+ __OBJC_$_INSTANCE_METHODS__NBMetadataHelper
+ __OBJC_$_INSTANCE_METHODS__NBNumberFormat
+ __OBJC_$_INSTANCE_METHODS__NBPhoneMetaData
+ __OBJC_$_INSTANCE_METHODS__NBPhoneNumber
+ __OBJC_$_INSTANCE_METHODS__NBPhoneNumberDesc
+ __OBJC_$_INSTANCE_METHODS__NBPhoneNumberUtil
+ __OBJC_$_INSTANCE_METHODS__NBRegExMatcher
+ __OBJC_$_INSTANCE_METHODS__NBRegularExpressionCache
+ __OBJC_$_INSTANCE_VARIABLES__NBAsYouTypeFormatter
+ __OBJC_$_INSTANCE_VARIABLES__NBMetadataHelper
+ __OBJC_$_INSTANCE_VARIABLES__NBNumberFormat
+ __OBJC_$_INSTANCE_VARIABLES__NBPhoneMetaData
+ __OBJC_$_INSTANCE_VARIABLES__NBPhoneNumber
+ __OBJC_$_INSTANCE_VARIABLES__NBPhoneNumberDesc
+ __OBJC_$_INSTANCE_VARIABLES__NBPhoneNumberUtil
+ __OBJC_$_INSTANCE_VARIABLES__NBRegularExpressionCache
+ __OBJC_$_PROP_LIST__NBAsYouTypeFormatter
+ __OBJC_$_PROP_LIST__NBMetadataHelper
+ __OBJC_$_PROP_LIST__NBNumberFormat
+ __OBJC_$_PROP_LIST__NBPhoneMetaData
+ __OBJC_$_PROP_LIST__NBPhoneNumber
+ __OBJC_$_PROP_LIST__NBPhoneNumberDesc
+ __OBJC_$_PROP_LIST__NBPhoneNumberUtil
+ __OBJC_$_PROP_LIST__NBRegularExpressionCache
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$__NBPhoneNumber
+ __OBJC_CLASS_RO_$_BFPhoneNumberNormalizer
+ __OBJC_CLASS_RO_$__NBAsYouTypeFormatter
+ __OBJC_CLASS_RO_$__NBMetadataHelper
+ __OBJC_CLASS_RO_$__NBNumberFormat
+ __OBJC_CLASS_RO_$__NBPhoneMetaData
+ __OBJC_CLASS_RO_$__NBPhoneNumber
+ __OBJC_CLASS_RO_$__NBPhoneNumberDesc
+ __OBJC_CLASS_RO_$__NBPhoneNumberUtil
+ __OBJC_CLASS_RO_$__NBRegExMatcher
+ __OBJC_CLASS_RO_$__NBRegularExpressionCache
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_BFPhoneNumberNormalizer
+ __OBJC_METACLASS_RO_$__NBAsYouTypeFormatter
+ __OBJC_METACLASS_RO_$__NBMetadataHelper
+ __OBJC_METACLASS_RO_$__NBNumberFormat
+ __OBJC_METACLASS_RO_$__NBPhoneMetaData
+ __OBJC_METACLASS_RO_$__NBPhoneNumber
+ __OBJC_METACLASS_RO_$__NBPhoneNumberDesc
+ __OBJC_METACLASS_RO_$__NBPhoneNumberUtil
+ __OBJC_METACLASS_RO_$__NBRegExMatcher
+ __OBJC_METACLASS_RO_$__NBRegularExpressionCache
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __Unwind_Resume
+ ___32+[_NBMetadataHelper CCode2CNMap]_block_invoke
+ ___36+[_NBPhoneNumberUtil sharedInstance]_block_invoke
+ ___36-[_NBPhoneNumberUtil DIGIT_MAPPINGS]_block_invoke
+ ___39+[_NBMetadataHelper phoneNumberDataMap]_block_invoke
+ ___41-[_NBPhoneNumberUtil getSupportedRegions]_block_invoke
+ ___42-[_NBPhoneNumberUtil telephonyNetworkInfo]_block_invoke
+ ___43+[_NBRegularExpressionCache sharedInstance]_block_invoke
+ ___46-[_NBPhoneNumberUtil initRegularExpressionSet]_block_invoke
+ ___47-[_NBPhoneNumberUtil initNormalizationMappings]_block_invoke
+ ___CFConstantStringClassReference
+ ___StringByTrimming_block_invoke
+ ___block_descriptor_32_e25_B24?08"NSDictionary"16l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e5_v8?0l
+ ___block_literal_global
+ ___block_literal_global.117
+ ___block_literal_global.293
+ ___block_literal_global.569
+ ___block_literal_global.590
+ ___block_literal_global.825
+ ___isNan_block_invoke
+ ___objc_personality_v0
+ ___unnamed_16
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_BusinessFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_BusinessFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_BusinessFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_BusinessFoundation
+ _dispatch_once
+ _inflate
+ _inflateEnd
+ _inflateInit2_
+ _initNormalizationMappings.onceToken
+ _initRegularExpressionSet.onceToken
+ _isNan
+ _kPhoneNumberMetaData
+ _objc_alloc
+ _objc_alloc_init
+ _objc_autorelease
+ _objc_autoreleaseReturnValue
+ _objc_begin_catch
+ _objc_claimAutoreleasedReturnValue
+ _objc_end_catch
+ _objc_enumerationMutation
+ _objc_exception_rethrow
+ _objc_msgSend$CCode2CNMap
+ _objc_msgSend$CHARACTER_CLASS_PATTERN_
+ _objc_msgSend$CN2CCodeMap
+ _objc_msgSend$DIGIT_MAPPINGS
+ _objc_msgSend$ELIGIBLE_FORMAT_PATTERN_
+ _objc_msgSend$ISOCountryCodes
+ _objc_msgSend$JSONObjectWithData:options:error:
+ _objc_msgSend$NATIONAL_PREFIX_SEPARATORS_PATTERN_
+ _objc_msgSend$STANDALONE_DIGIT_PATTERN_
+ _objc_msgSend$ableToExtractLongerNdd_
+ _objc_msgSend$ableToFormat_
+ _objc_msgSend$accruedInputWithoutFormatting_
+ _objc_msgSend$accruedInput_
+ _objc_msgSend$addObject:
+ _objc_msgSend$allKeys
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendNationalNumber_:
+ _objc_msgSend$appendString:
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$attemptToChooseFormattingPattern_
+ _objc_msgSend$attemptToChoosePatternWithPrefixExtracted_
+ _objc_msgSend$attemptToExtractCountryCallingCode_
+ _objc_msgSend$attemptToExtractIdd_
+ _objc_msgSend$attemptToFormatAccruedDigits_
+ _objc_msgSend$boolValue
+ _objc_msgSend$buildNationalNumberForParsing:nationalNumber:
+ _objc_msgSend$bytes
+ _objc_msgSend$cache
+ _objc_msgSend$canBeInternationallyDialled:
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$checkRegionForParsing:defaultRegion:
+ _objc_msgSend$chooseFormattingPatternForNumber:nationalNumber:
+ _objc_msgSend$clear
+ _objc_msgSend$clearCountryCodeSource
+ _objc_msgSend$compare:
+ _objc_msgSend$componentsSeparatedByRegex:regex:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copy
+ _objc_msgSend$count
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$countryCode
+ _objc_msgSend$countryCodeByCarrier
+ _objc_msgSend$countryCodeSource
+ _objc_msgSend$createFormattingTemplate_:
+ _objc_msgSend$currentFormattingPattern_
+ _objc_msgSend$currentLocale
+ _objc_msgSend$currentMetaData_
+ _objc_msgSend$currentOutput_
+ _objc_msgSend$dataWithLength:
+ _objc_msgSend$decimalDigitCharacterSet
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$defaultCountry_
+ _objc_msgSend$defaultMetaData_
+ _objc_msgSend$descHasPossibleNumberData:
+ _objc_msgSend$description
+ _objc_msgSend$dictionaryWithObject:forKey:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$dictionaryWithObjectsAndKeys:
+ _objc_msgSend$displayNameForKey:value:
+ _objc_msgSend$domain
+ _objc_msgSend$domesticCarrierCodeFormattingRule
+ _objc_msgSend$encodeObject:forKey:
+ _objc_msgSend$entireRegularExpressionWithPattern:options:error:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$errorWithObject:withDomain:
+ _objc_msgSend$exampleNumber
+ _objc_msgSend$extension
+ _objc_msgSend$extractCountryCode:nationalNumber:
+ _objc_msgSend$extractPossibleNumber:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$firstObject
+ _objc_msgSend$fixedLine
+ _objc_msgSend$formUnionWithCharacterSet:
+ _objc_msgSend$format
+ _objc_msgSend$format:numberFormat:
+ _objc_msgSend$format:numberFormat:error:
+ _objc_msgSend$formatByPattern:numberFormat:userDefinedFormats:
+ _objc_msgSend$formatInOriginalFormat:regionCallingFrom:
+ _objc_msgSend$formatNationalNumberWithCarrierCode:carrierCode:
+ _objc_msgSend$formatNationalNumberWithPreferredCarrierCode:fallbackCarrierCode:
+ _objc_msgSend$formatNsn:metadata:phoneNumberFormat:carrierCode:
+ _objc_msgSend$formatNsnUsingPattern:formattingPattern:numberFormat:carrierCode:
+ _objc_msgSend$formatNumberForMobileDialing:regionCallingFrom:withFormatting:
+ _objc_msgSend$formatOutOfCountryCallingNumber:regionCallingFrom:
+ _objc_msgSend$formatOutOfCountryKeepingAlphaChars:regionCallingFrom:
+ _objc_msgSend$formattingRuleHasFirstGroupOnly:
+ _objc_msgSend$formattingTemplate_
+ _objc_msgSend$generalDesc
+ _objc_msgSend$getAvailableFormats_:
+ _objc_msgSend$getCountryCodeForRegion:
+ _objc_msgSend$getCountryCodeForValidRegion:error:
+ _objc_msgSend$getExampleNumberForType:type:error:
+ _objc_msgSend$getFormattingTemplate_:numberFormat:
+ _objc_msgSend$getLengthOfGeographicalAreaCode:
+ _objc_msgSend$getLengthOfNationalDestinationCode:
+ _objc_msgSend$getMetadataForNonGeographicalRegion:
+ _objc_msgSend$getMetadataForRegion:
+ _objc_msgSend$getMetadataForRegionOrCallingCode:regionCode:
+ _objc_msgSend$getMetadataForRegion_:
+ _objc_msgSend$getNationalSignificantNumber:
+ _objc_msgSend$getNddPrefixForRegion:stripNonDigits:
+ _objc_msgSend$getNumberDescByType:type:
+ _objc_msgSend$getNumberType:
+ _objc_msgSend$getNumberTypeHelper:metadata:
+ _objc_msgSend$getRegionCodeForCountryCode:
+ _objc_msgSend$getRegionCodeForNumber:
+ _objc_msgSend$getRegionCodeForNumberFromRegionList:regionCodes:
+ _objc_msgSend$hasFormattingPatternForNumber:
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$hasValidCountryCallingCode:
+ _objc_msgSend$hasValue:
+ _objc_msgSend$hash
+ _objc_msgSend$helper
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$indexOfStringByString:target:
+ _objc_msgSend$init
+ _objc_msgSend$initNormalizationMappings
+ _objc_msgSend$initRegularExpressionSet
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithEntry:
+ _objc_msgSend$initWithPattern:options:error:
+ _objc_msgSend$initWithPattern:withFormat:withLeadingDigitsPatterns:withNationalPrefixFormattingRule:whenFormatting:withDomesticCarrierCodeFormattingRule:
+ _objc_msgSend$initWithRegionCode:bundle:
+ _objc_msgSend$initWithString:
+ _objc_msgSend$inputAccruedNationalNumber_
+ _objc_msgSend$inputDigit:
+ _objc_msgSend$inputDigitAndRememberPosition:
+ _objc_msgSend$inputDigitHelper_:
+ _objc_msgSend$inputDigitWithOptionToRememberPosition_:rememberPosition:
+ _objc_msgSend$inputHasFormatting_
+ _objc_msgSend$integerValue
+ _objc_msgSend$internationalPrefix
+ _objc_msgSend$intlNumberFormats
+ _objc_msgSend$invertedSet
+ _objc_msgSend$isCompleteNumber_
+ _objc_msgSend$isDigitOrLeadingPlusSign_:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isExpectingCountryCallingCode_
+ _objc_msgSend$isFormatEligible_:
+ _objc_msgSend$isLeadingZeroPossible:
+ _objc_msgSend$isNANPACountry:
+ _objc_msgSend$isNanpaNumberWithNationalPrefix_
+ _objc_msgSend$isNationalNumberSuffixOfTheOther:second:
+ _objc_msgSend$isNumberGeographical:
+ _objc_msgSend$isNumberMatch:second:
+ _objc_msgSend$isNumberMatchingDesc:numberDesc:
+ _objc_msgSend$isPossibleNumber:
+ _objc_msgSend$isPossibleNumberWithReason:
+ _objc_msgSend$isStartingStringByRegex:regex:
+ _objc_msgSend$isValidNumber:
+ _objc_msgSend$isValidNumberForRegion:regionCode:
+ _objc_msgSend$isValidRegionCode:
+ _objc_msgSend$isViablePhoneNumber:
+ _objc_msgSend$isoCountryCode
+ _objc_msgSend$italianLeadingZero
+ _objc_msgSend$jsonObjectFromZippedDataWithBytes:compressedLength:expandedLength:
+ _objc_msgSend$lastMatchPosition_
+ _objc_msgSend$lastObject
+ _objc_msgSend$leadingDigits
+ _objc_msgSend$leadingDigitsPatterns
+ _objc_msgSend$leadingZeroPossible
+ _objc_msgSend$length
+ _objc_msgSend$localeIdentifierFromComponents:
+ _objc_msgSend$lock
+ _objc_msgSend$longLongValue
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$mainBundle
+ _objc_msgSend$matchFirstByRegex:regex:
+ _objc_msgSend$matchedStringByRegex:regex:
+ _objc_msgSend$matchesByRegex:regex:
+ _objc_msgSend$matchesEntirely:string:
+ _objc_msgSend$matchesInString:options:range:
+ _objc_msgSend$maybeCreateNewTemplate_
+ _objc_msgSend$maybeExtractCountryCode:metadata:nationalNumber:keepRawInput:phoneNumber:error:
+ _objc_msgSend$maybeGetFormattedExtension:metadata:numberFormat:
+ _objc_msgSend$maybeStripExtension:
+ _objc_msgSend$maybeStripInternationalPrefixAndNormalize:possibleIddPrefix:
+ _objc_msgSend$maybeStripNationalPrefixAndCarrierCode:metadata:carrierCode:
+ _objc_msgSend$mobile
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$name
+ _objc_msgSend$narrowDownPossibleFormats_:
+ _objc_msgSend$nationalNumber
+ _objc_msgSend$nationalNumberPattern
+ _objc_msgSend$nationalNumber_
+ _objc_msgSend$nationalPrefix
+ _objc_msgSend$nationalPrefixExtracted_
+ _objc_msgSend$nationalPrefixForParsing
+ _objc_msgSend$nationalPrefixFormattingRule
+ _objc_msgSend$nationalPrefixOptionalWhenFormatting
+ _objc_msgSend$nationalPrefixTransformRule
+ _objc_msgSend$nb_safeArrayAtIndex:
+ _objc_msgSend$nb_safeDataAtIndex:
+ _objc_msgSend$nb_safeNumberAtIndex:
+ _objc_msgSend$nb_safeObjectAtIndex:class:
+ _objc_msgSend$nb_safeStringAtIndex:
+ _objc_msgSend$noInternationalDialling
+ _objc_msgSend$normalize:
+ _objc_msgSend$normalizeAndAccrueDigitsAndPlusSign_:rememberPosition:
+ _objc_msgSend$normalizeDigitsOnly:
+ _objc_msgSend$normalizeHelper:normalizationReplacements:removeNonMatches:
+ _objc_msgSend$normalizeSB:
+ _objc_msgSend$numberFormats
+ _objc_msgSend$numberFormatsFromEntry:
+ _objc_msgSend$numberOfLeadingZeros
+ _objc_msgSend$numberOfRanges
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$originalPosition_
+ _objc_msgSend$pager
+ _objc_msgSend$parse:defaultRegion:error:
+ _objc_msgSend$parseHelper:defaultRegion:keepRawInput:checkRegion:error:
+ _objc_msgSend$parsePrefixAsIdd:sourceString:
+ _objc_msgSend$pattern
+ _objc_msgSend$personalNumber
+ _objc_msgSend$phoneNumberDataMap
+ _objc_msgSend$phoneUtil_
+ _objc_msgSend$positionToRemember_
+ _objc_msgSend$possibleFormats_
+ _objc_msgSend$possibleLength
+ _objc_msgSend$possibleLengthLocalOnly
+ _objc_msgSend$possibleNumberPattern
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$preferredDomesticCarrierCode
+ _objc_msgSend$preferredExtnPrefix
+ _objc_msgSend$preferredInternationalPrefix
+ _objc_msgSend$prefixBeforeNationalNumber_
+ _objc_msgSend$prefixNumberWithCountryCallingCode:phoneNumberFormat:formattedNationalNumber:formattedExtension:
+ _objc_msgSend$premiumRate
+ _objc_msgSend$range
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$rangeOfCharacterFromSet:
+ _objc_msgSend$rangeOfFirstMatchInString:options:range:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$rangeOfString:options:range:
+ _objc_msgSend$rawInput
+ _objc_msgSend$rawInputContainsNationalPrefix:nationalPrefix:regionCode:
+ _objc_msgSend$reason
+ _objc_msgSend$regionCodeFromCountryCode:
+ _objc_msgSend$regularExpressionForPattern:error:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeNationalPrefixFromNationalNumber_
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$replaceFirstStringByRegex:regex:withTemplate:
+ _objc_msgSend$replaceStringByRegex:regex:withTemplate:
+ _objc_msgSend$sameMobileAndFixedLinePattern
+ _objc_msgSend$setAbleToFormat_:
+ _objc_msgSend$setAccruedInputWithoutFormatting_:
+ _objc_msgSend$setAccruedInput_:
+ _objc_msgSend$setCHARACTER_CLASS_PATTERN_:
+ _objc_msgSend$setCountryCode:
+ _objc_msgSend$setCountryCodeSource:
+ _objc_msgSend$setCurrentFormattingPattern_:
+ _objc_msgSend$setCurrentMetaData_:
+ _objc_msgSend$setCurrentOutput_:
+ _objc_msgSend$setDIGIT_PATTERN_:
+ _objc_msgSend$setDefaultCountry_:
+ _objc_msgSend$setDefaultMetaData_:
+ _objc_msgSend$setELIGIBLE_FORMAT_PATTERN_:
+ _objc_msgSend$setExtension:
+ _objc_msgSend$setFormat:
+ _objc_msgSend$setFormattingTemplate_:
+ _objc_msgSend$setInputHasFormatting_:
+ _objc_msgSend$setIsCompleteNumber_:
+ _objc_msgSend$setIsExpectingCountryCallingCode_:
+ _objc_msgSend$setItalianLeadingZero:
+ _objc_msgSend$setItalianLeadingZerosForPhoneNumber:phoneNumber:
+ _objc_msgSend$setLastMatchPosition_:
+ _objc_msgSend$setNATIONAL_PREFIX_SEPARATORS_PATTERN_:
+ _objc_msgSend$setNationalNumber:
+ _objc_msgSend$setNationalNumber_:
+ _objc_msgSend$setNationalPrefixExtracted_:
+ _objc_msgSend$setNationalPrefixFormattingRule:
+ _objc_msgSend$setNumberOfLeadingZeros:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setOriginalPosition_:
+ _objc_msgSend$setPattern:
+ _objc_msgSend$setPhoneUtil_:
+ _objc_msgSend$setPositionToRemember_:
+ _objc_msgSend$setPossibleFormats_:
+ _objc_msgSend$setPreferredDomesticCarrierCode:
+ _objc_msgSend$setPrefixBeforeNationalNumber_:
+ _objc_msgSend$setRawInput:
+ _objc_msgSend$setSTANDALONE_DIGIT_PATTERN_:
+ _objc_msgSend$setShouldAddSpaceAfterNationalPrefix_:
+ _objc_msgSend$setString:
+ _objc_msgSend$sharedCost
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$shouldAddSpaceAfterNationalPrefix_
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$stringByAppendingString:
+ _objc_msgSend$stringByPaddingToLength:withString:startingAtIndex:
+ _objc_msgSend$stringByReplacingMatchesInString:options:range:withTemplate:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:options:range:
+ _objc_msgSend$stringByReplacingOccurrencesString:withMap:removeNonMatches:
+ _objc_msgSend$stringByTrimmingCharactersInSet:
+ _objc_msgSend$stringPositionByRegex:regex:
+ _objc_msgSend$stringValue
+ _objc_msgSend$stringWithCharacters:length:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithString:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$subscriberCellularProvider
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$substringToIndex:
+ _objc_msgSend$substringWithRange:
+ _objc_msgSend$systemLocale
+ _objc_msgSend$telephonyNetworkInfo
+ _objc_msgSend$testNumberLength:desc:
+ _objc_msgSend$tollFree
+ _objc_msgSend$truncateTooLongNumber:
+ _objc_msgSend$uan
+ _objc_msgSend$unlock
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$unsignedLongLongValue
+ _objc_msgSend$uppercaseString
+ _objc_msgSend$validateNumberLength:metadata:
+ _objc_msgSend$validateNumberLength:metadata:type:
+ _objc_msgSend$voicemail
+ _objc_msgSend$voip
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _objc_msgSendSuper2
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release
+ _objc_release_x1
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x19
+ _objc_retain_x2
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x26
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_storeStrong
+ _objc_sync_enter
+ _objc_sync_exit
+ _objc_terminate
+ _objc_unsafeClaimAutoreleasedReturnValue
- ___unnamed_15
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_BusinessFoundation
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_BusinessFoundation
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_BusinessFoundation
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_BusinessFoundation
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_BusinessFoundation
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_BusinessFoundation
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_BusinessFoundation
- _swift_release_n
- _swift_retain_n
CStrings:
+ ""
+ "\b "
+ "\r\xff"
+ "\x0e\xff"
+ "\x0f\xff"
+ "\x10 "
+ "\x10\xff"
+ "\x11 "
+ "\x11\xff"
+ "\x12 "
+ "\x12\""
+ "\x12\xff"
+ "\x13 "
+ "\x13\xff"
+ "\x14 "
+ "\x14\xff"
+ "\x15 "
+ "\x15\xff"
+ "\x16\xff"
+ "\x17\xff"
+ "\x18\xff"
+ "\x19\xff"
+ " "
+ " - countryCode[%@], nationalNumber[%@], extension[%@], italianLeadingZero[%@], numberOfLeadingZeros[%@], rawInput[%@] countryCodeSource[%@] preferredDomesticCarrierCode[%@]"
+ " ext. "
+ "#"
+ "$1"
+ "$1$2"
+ "%@"
+ "%@ %@"
+ "%@ %@ %@%@"
+ "%@%@"
+ "%@%@%@"
+ "%@+%@-%@%@"
+ "%C"
+ "("
+ "(?:%@)$"
+ "(?:.*?[A-Za-z]){3}.*"
+ "([%@])"
+ "(\\$\\d)"
+ "(\\d+)(.*)"
+ "*"
+ "* codeID[%@] countryCode[%@] generalDesc[%@] fixedLine[%@] mobile[%@] tollFree[%@] premiumRate[%@] sharedCost[%@] personalNumber[%@] voip[%@] pager[%@] uan[%@] emergency[%@] voicemail[%@] noInternationalDialling[%@] internationalPrefix[%@] preferredInternationalPrefix[%@] nationalPrefix[%@] preferredExtnPrefix[%@] nationalPrefixForParsing[%@] nationalPrefixTransformRule[%@] sameMobileAndFixedLinePattern[%@] numberFormats[%@] intlNumberFormats[%@] mainCountryForCode[%@] leadingDigits[%@] leadingZeroPossible[%@]"
+ "+"
+ "+%@ %@%@"
+ "+%@%@"
+ "+%@%@%@"
+ "-"
+ "."
+ ".cxx_destruct"
+ "/"
+ "0"
+ "001"
+ "1"
+ "1%@"
+ "1.2.12"
+ "2"
+ "3"
+ "4"
+ "5"
+ "6"
+ "7"
+ "8"
+ "9"
+ "999999999999999"
+ ";"
+ ";ext="
+ ";isub="
+ ";phone-context="
+ "<SEP>"
+ "@\"NSArray\""
+ "@\"NSCache\""
+ "@\"NSData\""
+ "@\"NSLock\""
+ "@\"NSMutableArray\""
+ "@\"NSMutableDictionary\""
+ "@\"NSMutableString\""
+ "@\"NSNumber\""
+ "@\"NSRegularExpression\""
+ "@\"NSString\""
+ "@\"_NBMetadataHelper\""
+ "@\"_NBPhoneMetaData\""
+ "@\"_NBPhoneNumberDesc\""
+ "@\"_NBPhoneNumberUtil\""
+ "@\"_NBRegExMatcher\""
+ "@16@0:8"
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@16"
+ "@24@0:8Q16"
+ "@24@0:8^@16"
+ "@24@0:8^{_NSZone=}16"
+ "@24@0:8q16"
+ "@28@0:8@16B24"
+ "@32@0:8@16@24"
+ "@32@0:8@16^@24"
+ "@32@0:8@16q24"
+ "@32@0:8Q16#24"
+ "@36@0:8@16@24B32"
+ "@40@0:8*16Q24Q32"
+ "@40@0:8@16@24@32"
+ "@40@0:8@16@24^@32"
+ "@40@0:8@16@24q32"
+ "@40@0:8@16Q24^@32"
+ "@40@0:8@16q24@32"
+ "@40@0:8@16q24^@32"
+ "@44@0:8@16@24B32^@36"
+ "@48@0:8@16@24B32B36^@40"
+ "@48@0:8@16@24q32@40"
+ "@48@0:8@16q24@32@40"
+ "@48@0:8@16q24@32^@40"
+ "@60@0:8@16@24@32@40B48@52"
+ "@60@0:8@16@24^@32B40^@44^@52"
+ "A"
+ "A-Za-z"
+ "AR"
+ "B"
+ "B16@0:8"
+ "B24@0:8@16"
+ "B24@?0@8@\"NSDictionary\"16"
+ "B32@0:8@16@24"
+ "B32@0:8@16^@24"
+ "B36@0:8@16@24B32"
+ "B40@0:8@16@24@32"
+ "B40@0:8@16@24^@32"
+ "B40@0:8^@16@24^@32"
+ "BFPhoneNumberNormalizer"
+ "BR"
+ "C"
+ "CAPTURING_DIGIT_PATTERN"
+ "CCode2CNMap"
+ "CHARACTER_CLASS_PATTERN_"
+ "CN2CCodeMap"
+ "CO"
+ "D"
+ "DIGIT_MAPPINGS"
+ "DIGIT_PATTERN_"
+ "E"
+ "ELIGIBLE_FORMAT_PATTERN_"
+ "F"
+ "G"
+ "H"
+ "I"
+ "INVALID_COUNTRY_CODE"
+ "INVALID_COUNTRY_CODE:%@"
+ "INVALID_REGION_CODE"
+ "ISOCountryCodes"
+ "Invalid country code:%@"
+ "Invalid region code:%@"
+ "J"
+ "K"
+ "L"
+ "M"
+ "MX"
+ "N"
+ "NA"
+ "NATIONAL_PREFIX_SEPARATORS_PATTERN_"
+ "NOT_A_NUMBER"
+ "NOT_A_NUMBER:%@"
+ "NSCoding"
+ "NSCopying"
+ "NonMatch"
+ "O"
+ "P"
+ "Q"
+ "Q16@0:8"
+ "R"
+ "S"
+ "STANDALONE_DIGIT_PATTERN_"
+ "T"
+ "T@\"CTTelephonyNetworkInfo\",R,N"
+ "T@\"NSArray\",&,N,V_intlNumberFormats"
+ "T@\"NSArray\",&,N,V_leadingDigitsPatterns"
+ "T@\"NSArray\",&,N,V_numberFormats"
+ "T@\"NSArray\",R,N,V_possibleLength"
+ "T@\"NSArray\",R,N,V_possibleLengthLocalOnly"
+ "T@\"NSCache\",&,N,V_cache"
+ "T@\"NSCache\",&,N,V_metadataCache"
+ "T@\"NSData\",R,N,V_nationalNumberMatcherData"
+ "T@\"NSData\",R,N,V_possibleNumberMatcherData"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSLock\",&,N,V_entireStringCacheLock"
+ "T@\"NSLock\",&,N,V_lockPatternCache"
+ "T@\"NSMutableArray\",&,N,V_possibleFormats_"
+ "T@\"NSMutableDictionary\",&,N,V_entireStringRegexCache"
+ "T@\"NSMutableDictionary\",&,N,V_regexPatternCache"
+ "T@\"NSMutableString\",&,N,V_accruedInputWithoutFormatting_"
+ "T@\"NSMutableString\",&,N,V_accruedInput_"
+ "T@\"NSMutableString\",&,N,V_formattingTemplate_"
+ "T@\"NSMutableString\",&,N,V_nationalNumber_"
+ "T@\"NSMutableString\",&,N,V_prefixBeforeNationalNumber_"
+ "T@\"NSNumber\",&,N,V_countryCode"
+ "T@\"NSNumber\",&,N,V_countryCodeSource"
+ "T@\"NSNumber\",&,N,V_nationalNumber"
+ "T@\"NSNumber\",&,N,V_numberOfLeadingZeros"
+ "T@\"NSRegularExpression\",&,N,V_CAPTURING_DIGIT_PATTERN"
+ "T@\"NSRegularExpression\",&,N,V_CHARACTER_CLASS_PATTERN_"
+ "T@\"NSRegularExpression\",&,N,V_DIGIT_PATTERN_"
+ "T@\"NSRegularExpression\",&,N,V_ELIGIBLE_FORMAT_PATTERN_"
+ "T@\"NSRegularExpression\",&,N,V_NATIONAL_PREFIX_SEPARATORS_PATTERN_"
+ "T@\"NSRegularExpression\",&,N,V_STANDALONE_DIGIT_PATTERN_"
+ "T@\"NSRegularExpression\",&,N,V_VALID_ALPHA_PHONE_PATTERN"
+ "T@\"NSString\",&,N,V_codeID"
+ "T@\"NSString\",&,N,V_currentFormattingPattern_"
+ "T@\"NSString\",&,N,V_currentOutput_"
+ "T@\"NSString\",&,N,V_defaultCountry_"
+ "T@\"NSString\",&,N,V_domesticCarrierCodeFormattingRule"
+ "T@\"NSString\",&,N,V_extension"
+ "T@\"NSString\",&,N,V_format"
+ "T@\"NSString\",&,N,V_internationalPrefix"
+ "T@\"NSString\",&,N,V_leadingDigits"
+ "T@\"NSString\",&,N,V_nationalPrefix"
+ "T@\"NSString\",&,N,V_nationalPrefixExtracted_"
+ "T@\"NSString\",&,N,V_nationalPrefixForParsing"
+ "T@\"NSString\",&,N,V_nationalPrefixFormattingRule"
+ "T@\"NSString\",&,N,V_nationalPrefixTransformRule"
+ "T@\"NSString\",&,N,V_pattern"
+ "T@\"NSString\",&,N,V_preferredDomesticCarrierCode"
+ "T@\"NSString\",&,N,V_preferredExtnPrefix"
+ "T@\"NSString\",&,N,V_preferredInternationalPrefix"
+ "T@\"NSString\",&,N,V_rawInput"
+ "T@\"NSString\",R,N,V_exampleNumber"
+ "T@\"NSString\",R,N,V_nationalNumberPattern"
+ "T@\"NSString\",R,N,V_possibleNumberPattern"
+ "T@\"_NBMetadataHelper\",&,N,V_helper"
+ "T@\"_NBPhoneMetaData\",&,N,V_currentMetaData_"
+ "T@\"_NBPhoneMetaData\",&,N,V_defaultMetaData_"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_emergency"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_fixedLine"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_generalDesc"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_mobile"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_noInternationalDialling"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_pager"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_personalNumber"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_premiumRate"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_sharedCost"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_tollFree"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_uan"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_voicemail"
+ "T@\"_NBPhoneNumberDesc\",&,N,V_voip"
+ "T@\"_NBPhoneNumberUtil\",&,N,V_phoneUtil_"
+ "T@\"_NBRegExMatcher\",&,N,V_matcher"
+ "TB,N,V_ableToFormat_"
+ "TB,N,V_inputHasFormatting_"
+ "TB,N,V_isCompleteNumber_"
+ "TB,N,V_isExpectingCountryCallingCode_"
+ "TB,N,V_italianLeadingZero"
+ "TB,N,V_leadingZeroPossible"
+ "TB,N,V_mainCountryForCode"
+ "TB,N,V_nationalPrefixOptionalWhenFormatting"
+ "TB,N,V_sameMobileAndFixedLinePattern"
+ "TB,N,V_shouldAddSpaceAfterNationalPrefix_"
+ "TB,R,N,V_isSuccessfulFormatting"
+ "TOO_LONG"
+ "TOO_LONG:%@"
+ "TOO_SHORT_AFTER_IDD"
+ "TOO_SHORT_AFTER_IDD:%@"
+ "TOO_SHORT_NSN"
+ "TOO_SHORT_NSN:%@"
+ "TQ,N,V_lastMatchPosition_"
+ "TQ,N,V_originalPosition_"
+ "TQ,N,V_positionToRemember_"
+ "U"
+ "V"
+ "VALID_ALPHA_PHONE_PATTERN"
+ "W"
+ "X"
+ "Y"
+ "Z"
+ "ZZ"
+ "[%@%@]"
+ "[%@]+"
+ "[- ]"
+ "[\\\\\\/] *x"
+ "[\\d]+(?:[~\\u2053\\u223C\\uFF5E][\\d]+)?"
+ "[^%@%@#]+$"
+ "[pattern:%@, format:%@, leadingDigitsPattern:%@, nationalPrefixFormattingRule:%@, nationalPrefixOptionalWhenFormatting:%@, domesticCarrierCodeFormattingRule:%@]"
+ "\\$1"
+ "\\$CC"
+ "\\$FG"
+ "\\$NP"
+ "\\D+"
+ "\\[([^\\[\\]])*\\]"
+ "\\\\d"
+ "\\d(?=[^,}][^,}])"
+ "^"
+ "^%@"
+ "^(?:%@)"
+ "^(?:%@)$"
+ "^(?:\\+|%@)"
+ "^[%@]+"
+ "^\\(?\\$1\\)?"
+ "_CAPTURING_DIGIT_PATTERN"
+ "_CHARACTER_CLASS_PATTERN_"
+ "_DIGIT_PATTERN_"
+ "_ELIGIBLE_FORMAT_PATTERN_"
+ "_NATIONAL_PREFIX_SEPARATORS_PATTERN_"
+ "_NBAdditions"
+ "_NBAsYouTypeFormatter"
+ "_NBMetadataHelper"
+ "_NBNumberFormat"
+ "_NBPhoneMetaData"
+ "_NBPhoneNumber"
+ "_NBPhoneNumberDesc"
+ "_NBPhoneNumberUtil"
+ "_NBRegExMatcher"
+ "_NBRegularExpressionCache"
+ "_STANDALONE_DIGIT_PATTERN_"
+ "_VALID_ALPHA_PHONE_PATTERN"
+ "_ableToFormat_"
+ "_accruedInputWithoutFormatting_"
+ "_accruedInput_"
+ "_cache"
+ "_codeID"
+ "_countryCode"
+ "_countryCodeSource"
+ "_currentFormattingPattern_"
+ "_currentMetaData_"
+ "_currentOutput_"
+ "_defaultCountry_"
+ "_defaultMetaData_"
+ "_domesticCarrierCodeFormattingRule"
+ "_emergency"
+ "_entireStringCacheLock"
+ "_entireStringRegexCache"
+ "_exampleNumber"
+ "_extension"
+ "_fixedLine"
+ "_format"
+ "_formattingTemplate_"
+ "_generalDesc"
+ "_helper"
+ "_inputHasFormatting_"
+ "_internationalPrefix"
+ "_intlNumberFormats"
+ "_isCompleteNumber_"
+ "_isExpectingCountryCallingCode_"
+ "_isSuccessfulFormatting"
+ "_italianLeadingZero"
+ "_lastMatchPosition_"
+ "_leadingDigits"
+ "_leadingDigitsPatterns"
+ "_leadingZeroPossible"
+ "_lockPatternCache"
+ "_mainCountryForCode"
+ "_matcher"
+ "_metadataCache"
+ "_mobile"
+ "_nationalNumber"
+ "_nationalNumberMatcherData"
+ "_nationalNumberPattern"
+ "_nationalNumber_"
+ "_nationalPrefix"
+ "_nationalPrefixExtracted_"
+ "_nationalPrefixForParsing"
+ "_nationalPrefixFormattingRule"
+ "_nationalPrefixOptionalWhenFormatting"
+ "_nationalPrefixTransformRule"
+ "_noInternationalDialling"
+ "_numberFormats"
+ "_numberOfLeadingZeros"
+ "_originalPosition_"
+ "_pager"
+ "_pattern"
+ "_personalNumber"
+ "_phoneUtil_"
+ "_positionToRemember_"
+ "_possibleFormats_"
+ "_possibleLength"
+ "_possibleLengthLocalOnly"
+ "_possibleNumberMatcherData"
+ "_possibleNumberPattern"
+ "_preferredDomesticCarrierCode"
+ "_preferredExtnPrefix"
+ "_preferredInternationalPrefix"
+ "_prefixBeforeNationalNumber_"
+ "_premiumRate"
+ "_rawInput"
+ "_regexPatternCache"
+ "_sameMobileAndFixedLinePattern"
+ "_sharedCost"
+ "_shouldAddSpaceAfterNationalPrefix_"
+ "_tollFree"
+ "_uan"
+ "_voicemail"
+ "_voip"
+ "`\x06"
+ "` "
+ "a"
+ "a\x06"
+ "ableToExtractLongerNdd_"
+ "ableToFormat_"
+ "accruedInputWithoutFormatting_"
+ "accruedInput_"
+ "addObject:"
+ "allKeys"
+ "allocWithZone:"
+ "appendFormat:"
+ "appendNationalNumber_:"
+ "appendString:"
+ "arrayByAddingObjectsFromArray:"
+ "arrayWithCapacity:"
+ "arrayWithObjects:count:"
+ "attemptToChooseFormattingPattern_"
+ "attemptToChoosePatternWithPrefixExtracted_"
+ "attemptToExtractCountryCallingCode_"
+ "attemptToExtractIdd_"
+ "attemptToFormatAccruedDigits_"
+ "b"
+ "b\x06"
+ "boolValue"
+ "buildNationalNumberForParsing:nationalNumber:"
+ "bytes"
+ "c"
+ "c\x06"
+ "cache"
+ "canBeInternationallyDialled:"
+ "canBeInternationallyDialled:error:"
+ "caseInsensitiveCompare:"
+ "characterAtIndex:"
+ "characterSetWithCharactersInString:"
+ "checkRegionForParsing:defaultRegion:"
+ "chooseFormattingPatternForNumber:nationalNumber:"
+ "clear"
+ "clearCountryCodeSource"
+ "code"
+ "codeID"
+ "compare:"
+ "componentsSeparatedByRegex:regex:"
+ "componentsSeparatedByString:"
+ "containsObject:"
+ "convertAlphaCharactersInNumber:"
+ "copy"
+ "copyWithZone:"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "countryCode"
+ "countryCodeByCarrier"
+ "countryCodeFromRegionCode:"
+ "countryCodeSource"
+ "countryCodeToRegionCodeMap"
+ "countryToMetadata"
+ "createFormattingTemplate_:"
+ "currentFormattingPattern_"
+ "currentLocale"
+ "currentMetaData_"
+ "currentOutput_"
+ "d"
+ "d\x06"
+ "dataWithLength:"
+ "decimalDigitCharacterSet"
+ "decodeObjectForKey:"
+ "defaultCountry_"
+ "defaultMetaData_"
+ "descHasPossibleNumberData:"
+ "description"
+ "dictionaryWithObject:forKey:"
+ "dictionaryWithObjects:forKeys:count:"
+ "dictionaryWithObjectsAndKeys:"
+ "displayNameForKey:value:"
+ "domain"
+ "domesticCarrierCodeFormattingRule"
+ "e"
+ "e\x06"
+ "emergency"
+ "encodeObject:forKey:"
+ "encodeWithCoder:"
+ "entireRegularExpressionWithPattern:options:error:"
+ "entireStringCacheLock"
+ "entireStringRegexCache"
+ "errorWithDomain:code:userInfo:"
+ "errorWithObject:withDomain:"
+ "exampleNumber"
+ "extension"
+ "extractCountryCode:nationalNumber:"
+ "extractPossibleNumber:"
+ "f"
+ "f\x06"
+ "f\t"
+ "filteredArrayUsingPredicate:"
+ "firstMatchInString:options:range:"
+ "firstObject"
+ "fixedLine"
+ "formUnionWithCharacterSet:"
+ "format"
+ "format:numberFormat:"
+ "format:numberFormat:error:"
+ "formatByPattern:numberFormat:userDefinedFormats:"
+ "formatByPattern:numberFormat:userDefinedFormats:error:"
+ "formatInOriginalFormat:regionCallingFrom:"
+ "formatInOriginalFormat:regionCallingFrom:error:"
+ "formatNationalNumberWithCarrierCode:carrierCode:"
+ "formatNationalNumberWithCarrierCode:carrierCode:error:"
+ "formatNationalNumberWithPreferredCarrierCode:fallbackCarrierCode:"
+ "formatNationalNumberWithPreferredCarrierCode:fallbackCarrierCode:error:"
+ "formatNsn:metadata:phoneNumberFormat:carrierCode:"
+ "formatNsnUsingPattern:formattingPattern:numberFormat:carrierCode:"
+ "formatNumberForMobileDialing:regionCallingFrom:withFormatting:"
+ "formatNumberForMobileDialing:regionCallingFrom:withFormatting:error:"
+ "formatOutOfCountryCallingNumber:regionCallingFrom:"
+ "formatOutOfCountryCallingNumber:regionCallingFrom:error:"
+ "formatOutOfCountryKeepingAlphaChars:regionCallingFrom:"
+ "formatOutOfCountryKeepingAlphaChars:regionCallingFrom:error:"
+ "formattingRuleHasFirstGroupOnly:"
+ "formattingTemplate_"
+ "g"
+ "g\x06"
+ "g\t"
+ "generalDesc"
+ "getAllMetadata"
+ "getAvailableFormats_:"
+ "getCountryCodeForRegion:"
+ "getCountryCodeForValidRegion:error:"
+ "getCountryCodeSourceOrDefault"
+ "getCountryMobileTokenFromCountryCode:"
+ "getExampleNumber:error:"
+ "getExampleNumberForNonGeoEntity:error:"
+ "getExampleNumberForType:type:error:"
+ "getFormattingTemplate_:numberFormat:"
+ "getLengthOfGeographicalAreaCode:"
+ "getLengthOfGeographicalAreaCode:error:"
+ "getLengthOfNationalDestinationCode:"
+ "getLengthOfNationalDestinationCode:error:"
+ "getMetadataForNonGeographicalRegion:"
+ "getMetadataForRegion:"
+ "getMetadataForRegionOrCallingCode:regionCode:"
+ "getMetadataForRegion_:"
+ "getNationalSignificantNumber:"
+ "getNddPrefixForRegion:stripNonDigits:"
+ "getNumberDescByType:type:"
+ "getNumberType:"
+ "getNumberTypeHelper:metadata:"
+ "getRegionCodeForCountryCode:"
+ "getRegionCodeForNumber:"
+ "getRegionCodeForNumberFromRegionList:regionCodes:"
+ "getRegionCodesForCountryCode:"
+ "getRememberedPosition"
+ "getSupportedRegions"
+ "h"
+ "h\x06"
+ "h\t"
+ "hasFormattingPatternForNumber:"
+ "hasPrefix:"
+ "hasSuffix:"
+ "hasUnexpectedItalianLeadingZero:"
+ "hasValidCountryCallingCode:"
+ "hasValue:"
+ "hash"
+ "helper"
+ "i"
+ "i\x06"
+ "i\t"
+ "i24@0:8@16"
+ "i32@0:8@16@24"
+ "i32@0:8@16^@24"
+ "indexOfObject:"
+ "indexOfStringByString:target:"
+ "init"
+ "initNormalizationMappings"
+ "initRegularExpressionSet"
+ "initWithCapacity:"
+ "initWithCoder:"
+ "initWithEntry:"
+ "initWithPattern:options:error:"
+ "initWithPattern:withFormat:withLeadingDigitsPatterns:withNationalPrefixFormattingRule:whenFormatting:withDomesticCarrierCodeFormattingRule:"
+ "initWithRegionCode:"
+ "initWithRegionCode:bundle:"
+ "initWithString:"
+ "initialize"
+ "inputAccruedNationalNumber_"
+ "inputDigit:"
+ "inputDigitAndRememberPosition:"
+ "inputDigitHelper_:"
+ "inputDigitWithOptionToRememberPosition_:rememberPosition:"
+ "inputHasFormatting_"
+ "inputString:"
+ "inputStringAndRememberPosition:"
+ "integerValue"
+ "internationalPrefix"
+ "intlNumberFormats"
+ "invertedSet"
+ "isAllDigits:"
+ "isAlphaNumber:"
+ "isCompleteNumber_"
+ "isDigitOrLeadingPlusSign_:"
+ "isEqual:"
+ "isEqualToNumber:"
+ "isEqualToString:"
+ "isExpectingCountryCallingCode_"
+ "isFormatEligible_:"
+ "isLeadingZeroPossible:"
+ "isNANPACountry:"
+ "isNanpaNumberWithNationalPrefix_"
+ "isNationalNumberSuffixOfTheOther:second:"
+ "isNumberGeographical:"
+ "isNumberMatch:second:"
+ "isNumberMatch:second:error:"
+ "isNumberMatchingDesc:numberDesc:"
+ "isPossibleNumber:"
+ "isPossibleNumber:error:"
+ "isPossibleNumberString:regionDialingFrom:error:"
+ "isPossibleNumberWithReason:"
+ "isPossibleNumberWithReason:error:"
+ "isStartingStringByRegex:regex:"
+ "isSuccessfulFormatting"
+ "isValidNumber:"
+ "isValidNumberForRegion:regionCode:"
+ "isValidRegionCode:"
+ "isViablePhoneNumber:"
+ "isoCountryCode"
+ "italianLeadingZero"
+ "j"
+ "j\t"
+ "jsonObjectFromZippedDataWithBytes:compressedLength:expandedLength:"
+ "k"
+ "k\t"
+ "l"
+ "l\t"
+ "lastMatchPosition_"
+ "lastObject"
+ "leadingDigits"
+ "leadingDigitsPatterns"
+ "leadingZeroPossible"
+ "length"
+ "localeIdentifierFromComponents:"
+ "lock"
+ "lockPatternCache"
+ "longLongValue"
+ "lowercaseString"
+ "m"
+ "m\t"
+ "mainBundle"
+ "mainCountryForCode"
+ "matchFirstByRegex:regex:"
+ "matchNationalNumber:phoneNumberDesc:allowsPrefixMatch:"
+ "matchedStringByRegex:regex:"
+ "matcher"
+ "matchesByRegex:regex:"
+ "matchesEntirely:string:"
+ "matchesInString:options:range:"
+ "maybeCreateNewTemplate_"
+ "maybeExtractCountryCode:metadata:nationalNumber:keepRawInput:phoneNumber:error:"
+ "maybeGetFormattedExtension:metadata:numberFormat:"
+ "maybeStripExtension:"
+ "maybeStripInternationalPrefixAndNormalize:possibleIddPrefix:"
+ "maybeStripNationalPrefixAndCarrierCode:metadata:carrierCode:"
+ "metadata"
+ "metadataCache"
+ "mobile"
+ "mutableCopy"
+ "n"
+ "n\t"
+ "name"
+ "narrowDownPossibleFormats_:"
+ "nationalNumber"
+ "nationalNumberMatcherData"
+ "nationalNumberPattern"
+ "nationalNumberPattern[%@] possibleNumberPattern[%@] possibleLength[%@] possibleLengthLocalOnly[%@] exampleNumber[%@]"
+ "nationalNumber_"
+ "nationalPrefix"
+ "nationalPrefixExtracted_"
+ "nationalPrefixForParsing"
+ "nationalPrefixFormattingRule"
+ "nationalPrefixOptionalWhenFormatting"
+ "nationalPrefixTransformRule"
+ "nb_safeArrayAtIndex:"
+ "nb_safeDataAtIndex:"
+ "nb_safeNumberAtIndex:"
+ "nb_safeObjectAtIndex:class:"
+ "nb_safeStringAtIndex:"
+ "noInternationalDialling"
+ "normalize:"
+ "normalizeAndAccrueDigitsAndPlusSign_:rememberPosition:"
+ "normalizeDiallableCharsOnly:"
+ "normalizeDigitsOnly:"
+ "normalizeHelper:normalizationReplacements:removeNonMatches:"
+ "normalizeSB:"
+ "normalizedPhoneNumberForPhoneNumber:"
+ "numberFormats"
+ "numberFormatsFromEntry:"
+ "numberOfLeadingZeros"
+ "numberOfRanges"
+ "numberWithBool:"
+ "numberWithInteger:"
+ "numberWithLongLong:"
+ "numberWithUnsignedInteger:"
+ "o"
+ "o\t"
+ "objectAtIndex:"
+ "objectAtIndexedSubscript:"
+ "objectForKey:"
+ "objectForKeyedSubscript:"
+ "originalPosition_"
+ "p"
+ "pager"
+ "parse:defaultRegion:error:"
+ "parseAndKeepRawInput:defaultRegion:error:"
+ "parseHelper:defaultRegion:keepRawInput:checkRegion:error:"
+ "parsePrefixAsIdd:sourceString:"
+ "parseWithPhoneCarrierRegion:error:"
+ "pattern"
+ "personalNumber"
+ "phoneNumberDataMap"
+ "phoneUtil_"
+ "positionToRemember_"
+ "possibleFormats_"
+ "possibleLength"
+ "possibleLengthLocalOnly"
+ "possibleNumberMatcherData"
+ "possibleNumberPattern"
+ "predicateWithBlock:"
+ "preferredDomesticCarrierCode"
+ "preferredExtnPrefix"
+ "preferredInternationalPrefix"
+ "prefixBeforeNationalNumber_"
+ "prefixNumberWithCountryCallingCode:phoneNumberFormat:formattedNationalNumber:formattedExtension:"
+ "premiumRate"
+ "q"
+ "q16@0:8"
+ "q24@0:8@16"
+ "q32@0:8@16@24"
+ "q32@0:8@16^@24"
+ "q32@0:8^@16@24"
+ "q40@0:8@16@24^@32"
+ "q40@0:8@16@24q32"
+ "r"
+ "range"
+ "rangeAtIndex:"
+ "rangeOfCharacterFromSet:"
+ "rangeOfFirstMatchInString:options:range:"
+ "rangeOfString:"
+ "rangeOfString:options:"
+ "rangeOfString:options:range:"
+ "rawInput"
+ "rawInputContainsNationalPrefix:nationalPrefix:regionCode:"
+ "reason"
+ "regexPatternCache"
+ "regionCodeFromCountryCode:"
+ "regularExpressionForPattern:error:"
+ "regularExpressionWithPattern:options:error:"
+ "removeAllObjects"
+ "removeLastDigit"
+ "removeLastDigitAndRememberPosition"
+ "removeNationalPrefixFromNationalNumber_"
+ "removeObject:"
+ "removeObjectAtIndex:"
+ "replaceFirstStringByRegex:regex:withTemplate:"
+ "replaceStringByRegex:regex:withTemplate:"
+ "s"
+ "sameMobileAndFixedLinePattern"
+ "setAbleToFormat_:"
+ "setAccruedInputWithoutFormatting_:"
+ "setAccruedInput_:"
+ "setCAPTURING_DIGIT_PATTERN:"
+ "setCHARACTER_CLASS_PATTERN_:"
+ "setCache:"
+ "setCodeID:"
+ "setCountryCode:"
+ "setCountryCodeSource:"
+ "setCurrentFormattingPattern_:"
+ "setCurrentMetaData_:"
+ "setCurrentOutput_:"
+ "setDIGIT_PATTERN_:"
+ "setDefaultCountry_:"
+ "setDefaultMetaData_:"
+ "setDomesticCarrierCodeFormattingRule:"
+ "setELIGIBLE_FORMAT_PATTERN_:"
+ "setEmergency:"
+ "setEntireStringCacheLock:"
+ "setEntireStringRegexCache:"
+ "setExtension:"
+ "setFixedLine:"
+ "setFormat:"
+ "setFormattingTemplate_:"
+ "setGeneralDesc:"
+ "setHelper:"
+ "setInputHasFormatting_:"
+ "setInternationalPrefix:"
+ "setIntlNumberFormats:"
+ "setIsCompleteNumber_:"
+ "setIsExpectingCountryCallingCode_:"
+ "setItalianLeadingZero:"
+ "setItalianLeadingZerosForPhoneNumber:phoneNumber:"
+ "setLastMatchPosition_:"
+ "setLeadingDigits:"
+ "setLeadingDigitsPatterns:"
+ "setLeadingZeroPossible:"
+ "setLockPatternCache:"
+ "setMainCountryForCode:"
+ "setMatcher:"
+ "setMetadataCache:"
+ "setMobile:"
+ "setNATIONAL_PREFIX_SEPARATORS_PATTERN_:"
+ "setNationalNumber:"
+ "setNationalNumber_:"
+ "setNationalPrefix:"
+ "setNationalPrefixExtracted_:"
+ "setNationalPrefixForParsing:"
+ "setNationalPrefixFormattingRule:"
+ "setNationalPrefixOptionalWhenFormatting:"
+ "setNationalPrefixTransformRule:"
+ "setNoInternationalDialling:"
+ "setNumberFormats:"
+ "setNumberOfLeadingZeros:"
+ "setObject:forKey:"
+ "setObject:forKeyedSubscript:"
+ "setOriginalPosition_:"
+ "setPager:"
+ "setPattern:"
+ "setPersonalNumber:"
+ "setPhoneUtil_:"
+ "setPositionToRemember_:"
+ "setPossibleFormats_:"
+ "setPreferredDomesticCarrierCode:"
+ "setPreferredExtnPrefix:"
+ "setPreferredInternationalPrefix:"
+ "setPrefixBeforeNationalNumber_:"
+ "setPremiumRate:"
+ "setRawInput:"
+ "setRegexPatternCache:"
+ "setSTANDALONE_DIGIT_PATTERN_:"
+ "setSameMobileAndFixedLinePattern:"
+ "setSharedCost:"
+ "setShouldAddSpaceAfterNationalPrefix_:"
+ "setString:"
+ "setTollFree:"
+ "setUan:"
+ "setVALID_ALPHA_PHONE_PATTERN:"
+ "setVoicemail:"
+ "setVoip:"
+ "sharedCost"
+ "sharedInstance"
+ "shouldAddSpaceAfterNationalPrefix_"
+ "sortedArrayUsingSelector:"
+ "stringByAppendingString:"
+ "stringByPaddingToLength:withString:startingAtIndex:"
+ "stringByReplacingMatchesInString:options:range:withTemplate:"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "stringByReplacingOccurrencesOfString:withString:options:range:"
+ "stringByReplacingOccurrencesString:withMap:removeNonMatches:"
+ "stringByTrimmingCharactersInSet:"
+ "stringPositionByRegex:regex:"
+ "stringValue"
+ "stringWithCharacters:length:"
+ "stringWithFormat:"
+ "stringWithString:"
+ "subarrayWithRange:"
+ "subscriberCellularProvider"
+ "substringFromIndex:"
+ "substringToIndex:"
+ "substringWithRange:"
+ "systemLocale"
+ "t"
+ "tel:"
+ "telephonyNetworkInfo"
+ "testNumberLength:desc:"
+ "tollFree"
+ "truncateTooLongNumber:"
+ "u"
+ "uan"
+ "unlock"
+ "unsignedIntegerValue"
+ "unsignedLongLongValue"
+ "uppercaseString"
+ "us"
+ "v"
+ "v16@0:8"
+ "v20@0:8B16"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@16"
+ "v24@0:8Q16"
+ "v24@0:8^@16"
+ "v32@0:8@16@24"
+ "v32@0:8@16^@24"
+ "validateNumberLength:metadata:"
+ "validateNumberLength:metadata:type:"
+ "voicemail"
+ "voip"
+ "w"
+ "whitespaceAndNewlineCharacterSet"
+ "x"
+ "y"
+ "z"
+ "|"
+ "~"
+ "\xa0"
+ "\xe6\t"
+ "\xe7\t"
+ "\xe8\t"
+ "\xe9\t"
+ "\xea\t"
+ "\xeb\t"
+ "\xec\t"
+ "\xed\t"
+ "\xee\t"
+ "\xef\t"
+ "\xf0\x06"
+ "\xf1\x06"
+ "\xf2\x06"
+ "\xf3\x06"
+ "\xf4\x06"
+ "\xf5\x06"
+ "\xf6\x06"
+ "\xf7\x06"
+ "\xf8\x06"
+ "\xf9\x06"

```
