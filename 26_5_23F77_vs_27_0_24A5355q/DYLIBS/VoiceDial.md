## VoiceDial

> `/System/Library/VoiceServices/PlugIns/VoiceDial.vsplugin/VoiceDial`

```diff

-3027.600.41.2.1
-  __TEXT.__text: 0xad60
-  __TEXT.__auth_stubs: 0x7a0
+3060.100.14.2.1
+  __TEXT.__text: 0xa738
   __TEXT.__objc_methlist: 0x92c
   __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x6b4
   __TEXT.__oslogstring: 0x15b
-  __TEXT.__cstring: 0x6a4
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__unwind_info: 0x250
-  __TEXT.__objc_classname: 0x222
-  __TEXT.__objc_methname: 0x1aac
-  __TEXT.__objc_methtype: 0x51b
-  __TEXT.__objc_stubs: 0x1860
-  __DATA_CONST.__got: 0x210
+  __TEXT.__unwind_info: 0x228
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x740
   __DATA_CONST.__objc_superrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x3e0
+  __DATA_CONST.__got: 0x210
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xa40
   __AUTH_CONST.__objc_const: 0x1560
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x460
   __DATA.__objc_ivar: 0xe8
   __DATA.__data: 0x1d0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D6806A71-E7C2-3A65-BFCB-F5478FF93A0A
+  UUID: 5916DC63-E53A-3009-96D8-81A33EBD0FF9
   Functions: 195
   Symbols:   980
-  CStrings:  580
+  CStrings:  178
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
- _objc_release_x3
- _objc_retainAutoreleasedReturnValue
Functions:
~ -[VoiceDialResultHandler _nameSource] : 124 -> 108
~ -[VoiceDialResultHandler _addressBook] : 132 -> 128
~ -[VoiceDialResultHandler _phoneticNames:fromDictionary:] : 408 -> 412
~ -[VoiceDialResultHandler actionForRecognitionResults:] : 7484 -> 7256
~ __ResultHandlerAddressBookCallback : 3672 -> 3576
~ __CommaSeparatedStringFromArray : 356 -> 324
~ _PHDefaultLog : 84 -> 68
~ _PHOversizedLog : 84 -> 68
~ _PHOversizedLogQueue : 84 -> 68
~ ___PHOversizedLogQueue_block_invoke : 108 -> 104
~ -[VoiceDialRecognitionAction initWithPhoneNumber:uid:] : 136 -> 140
~ -[VoiceDialRecognitionAction perform] : 696 -> 628
~ -[DigitDialResultValidator deviceCountryCode] : 92 -> 80
~ -[DigitDialResultValidator networkCountryCode] : 92 -> 80
~ -[DigitDialResultValidator _copyExceptionsForCountryCode:] : 220 -> 208
~ -[DigitDialResultValidator _isValidExceptionForDevice:] : 128 -> 124
~ -[DigitDialResultValidator _isValidExceptionForNetwork:] : 128 -> 124
~ -[DigitDialResultValidator indexOfValidPhoneNumber:] : 404 -> 388
~ -[DigitDialResultValidator validRecognitionResultFromRecognitionResult:] : 140 -> 128
~ -[DigitDialResultValidator setDeviceCountryCode:] : 64 -> 12
~ -[DigitDialResultValidator setNetworkCountryCode:] : 64 -> 12
~ -[DigitDialResultHandler actionForRecognitionResult:] : 908 -> 828
~ -[DigitDialResultHandler contactsDataProvider] : 136 -> 128
~ -[DigitDialResultHandler setContactsDataProvider:] : 64 -> 12
~ _DigitDialPhoneNumberFromResult : 1932 -> 1856
~ __SpokenValueFromElementValue : 100 -> 96
~ __AppendValueToPhoneNumbersInRange : 432 -> 428
~ +[VoiceDialNameDataSource _nameDataSourceByLanguageMap] : 88 -> 72
~ __CreateNameDataSourceMap : 180 -> 168
~ +[VoiceDialNameDataSource nameDataSourceForLanguageIdentifier:] : 244 -> 232
~ -[VoiceDialNameDataSource matchingNameType:fromTypes:forPerson:] : 444 -> 448
~ _VoiceDialMaidenNameDataSourceCreateMaidenNameFromLastName : 1252 -> 1216
~ __IsNamePrefixString : 332 -> 288
~ -[VoiceDialVoicemailRecognitionAction init] : 328 -> 308
~ _VoiceDialCopyNameLabelAndTypeFromRecognitionResult : 532 -> 556
~ _VoiceDialCopyNamesLabelAndTypeFromRecognitionResults : 472 -> 484
~ _VoiceDialSendNameAndExtendedLabelMatches : 976 -> 984
~ _VoiceDialCopyMostLikelyNumberWithPersonAndLabel : 596 -> 572
~ _stringValueForContactProperty : 164 -> 152
~ _VoiceDialGetMostLikelyFacetimeContactWithPersonAndLabel : 992 -> 940
~ _VoiceDialCopyErrorActionForResult : 384 -> 372
~ _VoiceDialSpokenLocalizedString : 148 -> 132
~ _VoiceDialBundle : 120 -> 108
~ _VoiceDialSpokenLocalizedStringIfAvailable : 368 -> 356
~ _VoiceDialConfigureSpokenLocalizedLabel : 336 -> 324
~ _VoiceDialTelephonyUtilitiesFrameworkHandle : 96 -> 92
~ -[NSDictionary(VoiceDialResultHandlerMerge) mergeSetValuesIntoArray] : 356 -> 352
~ -[VDDisambiguationAddressBookContext setPreviousName:] : 64 -> 12
~ -[VDDisambiguationAddressBookContext setMatchedName:] : 64 -> 12
~ -[VDDisambiguationAddressBookContext setResult:] : 64 -> 12
~ -[VoiceDialDataProvider init] : 264 -> 252
~ -[VoiceDialDataProvider dealloc] : 192 -> 188
~ -[VoiceDialDataProvider _addressBook] : 132 -> 128
~ -[VoiceDialDataProvider _namesSource] : 156 -> 140
~ -[VoiceDialDataProvider getLabels:andWeightedLabels:ForABProperty:] : 1768 -> 1740
~ ___67-[VoiceDialDataProvider getLabels:andWeightedLabels:ForABProperty:]_block_invoke : 264 -> 244
~ -[VoiceDialDataProvider _phoneLabels] : 160 -> 168
~ -[VoiceDialDataProvider _facetimeLabels] : 348 -> 344
~ -[VoiceDialDataProvider _totalPeople] : 180 -> 176
~ -[VoiceDialDataProvider _voiceDialRecordAtIndex:] : 516 -> 508
~ -[VoiceDialDataProvider valueCountForClassWithIdentifier:inModelWithIdentifier:] : 168 -> 156
~ -[VoiceDialDataProvider getValue:weight:atIndex:forClassWithIdentifier:inModelWithIdentifier:] : 432 -> 428
~ ___48-[VoiceDialDataProvider cacheValidityIdentifier]_block_invoke : 336 -> 332
~ -[VoiceDialDataProvider isCacheValidityIdentifierValid:] : 592 -> 588
~ ___56-[VoiceDialDataProvider isCacheValidityIdentifierValid:]_block_invoke : 424 -> 412
~ -[VoiceDialDataProvider beginReportingChanges] : 160 -> 156
~ -[VoiceDialDataProvider stopReportingChanges] : 176 -> 172
~ -[VoiceDialDataProvider _handleAddressBookChanged] : 160 -> 156
~ -[VoiceDialFacetimeRecognitionAction initWithContactInfo:uid:] : 140 -> 144
~ -[VoiceDialFacetimeRecognitionAction perform] : 688 -> 620
~ -[VoiceDialResultValidator _addressBook] : 132 -> 128
~ -[VoiceDialResultValidator _nameSource] : 124 -> 108
~ -[VoiceDialResultValidator validRecognitionResultFromRecognitionResult:] : 468 -> 464
~ -[VoiceDialResultValidator validRecognitionResultFromRecognitionResult:knownDisambiguationValues:] : 1068 -> 1056
~ __ResultDisambiguationAddressBookCallback : 580 -> 584
~ -[VoiceDialResultValidator _addressBook].cold.1 : 124 -> 80
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSSet\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"40@0:8q16@\"NSString\"24@\"NSString\"32"
- "@\"TUContactsDataProvider\""
- "@\"VSRecognitionAction\"24@0:8@\"NSArray\"16"
- "@\"VSRecognitionAction\"24@0:8@\"VSRecognitionResult\"16"
- "@\"VSRecognitionResult\""
- "@\"VSRecognitionResult\"24@0:8@\"VSRecognitionResult\"16"
- "@\"VSRecognitionResult\"32@0:8@\"VSRecognitionResult\"16@\"NSDictionary\"24"
- "@\"VoiceDialNameDataSource\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16i24"
- "@28@0:8^v16i24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8q16@24@32"
- "B"
- "B16@0:8"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSDictionary\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B48@0:8^@16^@24Q32^v40"
- "B56@0:8^@16^q24q32@\"NSString\"40@\"NSString\"48"
- "B56@0:8^@16^q24q32@40@48"
- "B60@0:8Q16^@24^@32i40^Q44^v52"
- "DigitDialResultHandler"
- "DigitDialResultValidator"
- "NSObject"
- "Q"
- "Q16@0:8"
- "Q20@0:8i16"
- "Q24@0:8@16"
- "T#,R"
- "T@\"NSMutableDictionary\",&,V_firstNamesByLastNames"
- "T@\"NSMutableDictionary\",&,V_lastNamesByFirstNames"
- "T@\"NSMutableDictionary\",&,V_phoneticNamesByName"
- "T@\"NSMutableSet\",&,V_compositeNames"
- "T@\"NSMutableSet\",&,V_localizedEmailLabels"
- "T@\"NSMutableSet\",&,V_localizedPhoneLabels"
- "T@\"NSMutableSet\",&,V_spokenCompositeNames"
- "T@\"NSMutableSet\",&,V_topLevelNonNickNames"
- "T@\"NSMutableSet\",&,V_unlocalizedEmailLabels"
- "T@\"NSMutableSet\",&,V_unlocalizedPhoneLabels"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_serialQueue"
- "T@\"NSString\",&,N,V_deviceCountryCode"
- "T@\"NSString\",&,N,V_matchedName"
- "T@\"NSString\",&,N,V_networkCountryCode"
- "T@\"NSString\",&,N,V_previousName"
- "T@\"NSString\",&,V_matchedName"
- "T@\"NSString\",&,V_nameToMatch"
- "T@\"NSString\",&,V_previousName"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"TUContactsDataProvider\",&,N,V_contactsDataProvider"
- "T@\"VSRecognitionResult\",&,N,V_result"
- "TB,V_allNamesMatchedType"
- "TB,V_allowFirstFT"
- "TB,V_resultFound"
- "TQ,R"
- "T^@,V_result"
- "T^v,V_resultPerson"
- "T^{__CFString=},V_contactInfo"
- "Ti,V_lastNameMatchType"
- "Ti,V_matchedLabelType"
- "Ti,V_previousNameProperty"
- "Ti,V_requiredNameMatchType"
- "Ti,V_resultStatus"
- "Tq,V_nicknameMatchCount"
- "URL"
- "VDDisambiguationAddressBookContext"
- "VSRecognitionModelDataProvider"
- "VSRecognitionResultHandler"
- "VSRecognitionResultValidator"
- "VoiceDialDataProvider"
- "VoiceDialDisambiguationAddressBookContext"
- "VoiceDialFacetimeRecognitionAction"
- "VoiceDialLastNameDataSource"
- "VoiceDialMaidenNameDataSource"
- "VoiceDialNameDataSource"
- "VoiceDialRecognitionAction"
- "VoiceDialResultHandler"
- "VoiceDialResultHandlerContext"
- "VoiceDialResultHandlerMerge"
- "VoiceDialResultValidator"
- "VoiceDialVoicemailRecognitionAction"
- "Vv16@0:8"
- "^@"
- "^@16@0:8"
- "^v"
- "^v16@0:8"
- "^v24@0:8q16"
- "^{_NSZone=}16@0:8"
- "^{__CFArray=}"
- "^{__CFString=}"
- "^{__CFString=}16@0:8"
- "_abID"
- "_addressBook"
- "_allNamesMatchedType"
- "_allowFirstFT"
- "_compositeNames"
- "_compositeNamesOnly"
- "_contactInfo"
- "_contactsDataProvider"
- "_copyExceptionsForCountryCode:"
- "_deviceCountryCode"
- "_deviceExceptions"
- "_facetimeLabels"
- "_firstNamesByLastNames"
- "_handleAddressBookChanged"
- "_hasMinimumNumberOfDigits:countryCode:"
- "_isValidExceptionForDevice:"
- "_isValidExceptionForNetwork:"
- "_lastDatabaseUUID"
- "_lastNameMatchType"
- "_lastNamesByFirstNames"
- "_lastSequenceNumber"
- "_localizedEmailLabels"
- "_localizedPhoneLabels"
- "_matchedLabelType"
- "_matchedName"
- "_nameDataSourceByLanguageMap"
- "_nameSource"
- "_nameToMatch"
- "_nameTypeMask"
- "_namesSource"
- "_networkCountryCode"
- "_networkExceptions"
- "_nicknameMatchCount"
- "_people"
- "_peopleRange"
- "_phoneLabels"
- "_phoneNumber"
- "_phoneticNames:fromDictionary:"
- "_phoneticNamesByName"
- "_previousName"
- "_previousNameProperty"
- "_requiredNameMatchType"
- "_result"
- "_resultFound"
- "_resultPerson"
- "_resultStatus"
- "_sequenceNumberIsValid:"
- "_serialQueue"
- "_shouldUseCompositeNamesOnly"
- "_spokenCompositeNames"
- "_topLevelNonNickNames"
- "_totalPeople"
- "_uid"
- "_unlocalizedEmailLabels"
- "_unlocalizedPhoneLabels"
- "_voiceDialProviderFlags"
- "_voiceDialRecordAtIndex:"
- "_weightedFacetimeLabels"
- "_weightedPhoneLabels"
- "actionForRecognitionResult:"
- "actionForRecognitionResults:"
- "actionType"
- "addIndex:"
- "addListenerID:forService:"
- "addObject:"
- "addObjectsFromArray:"
- "airplaneMode"
- "allKeys"
- "allNamesMatchedType"
- "allObjects"
- "allowFirstFT"
- "anyObject"
- "appendString:"
- "arrayWithArray:"
- "autorelease"
- "beginReportingChanges"
- "boolValue"
- "bundleForClass:"
- "bundleIdentifier"
- "cacheValidityIdentifier"
- "capitalizedString"
- "caseInsensitiveCompare:"
- "class"
- "compositeNames"
- "conformsToProtocol:"
- "contactFromPerson:keysToFetch:"
- "contactFromPersonID:keysToFetch:"
- "contactInfo"
- "contactLabel"
- "contactProperty"
- "contactsDataProvider"
- "containsObject:"
- "copyPronunciationPropertyForPerson:withNameType:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countOfNamesOfType:"
- "dealloc"
- "debugDescription"
- "description"
- "deviceCountryCode"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjectsAndKeys:"
- "elementCount"
- "entriesForContact:"
- "executeFetchRequest:"
- "faceTimeProvider"
- "facetimeService"
- "fileSystemRepresentation"
- "firstIndex"
- "firstNamesByLastNames"
- "getElementClassIdentifier:value:atIndex:"
- "getLabels:andWeightedLabels:ForABProperty:"
- "getName:phoneticName:atIndex:forPerson:"
- "getNth:name:phoneticName:ofType:nameIndex:forPerson:"
- "getValue:weight:atIndex:forClassWithIdentifier:inModelWithIdentifier:"
- "handleWithDestinationID:"
- "hash"
- "i"
- "i16@0:8"
- "i24@0:8Q16"
- "i40@0:8@16Q24^v32"
- "identifier"
- "indexGreaterThanIndex:"
- "indexGreaterThanOrEqualToIndex:"
- "indexLessThanIndex:"
- "indexOfMainNameOfType:"
- "indexOfValidPhoneNumber:"
- "init"
- "initWithArray:"
- "initWithBool:"
- "initWithCapacity:"
- "initWithContactInfo:uid:"
- "initWithContactsDataSource:"
- "initWithContentsOfFile:"
- "initWithContentsOfURL:"
- "initWithFormat:"
- "initWithHandle:"
- "initWithInt:"
- "initWithModelIdentifier:"
- "initWithPhoneNumber:uid:"
- "initWithProvider:"
- "initWithSet:"
- "initWithSpokenFeedbackString:willTerminate:"
- "initWithString:"
- "initWithType:value:"
- "initWithUnsignedInt:"
- "intValue"
- "intersectSet:"
- "isCacheValidityIdentifierValid:"
- "isEqual:"
- "isEqualToString:"
- "isFaceTimeVideoAvailable"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "knownValueForClassIdentifier:"
- "knownValuesForClassIdentifier:"
- "lastNameMatchType"
- "lastNamesByFirstNames"
- "lastObject"
- "length"
- "localizedEmailLabels"
- "localizedName"
- "localizedPhoneLabels"
- "localizedStringForKey:value:table:"
- "matchedLabelType"
- "matchedName"
- "matchingNameType:fromTypes:forPerson:"
- "mergeSetValuesIntoArray"
- "minusSet:"
- "mutableCopy"
- "nameDataSourceForLanguageIdentifier:"
- "nameToMatch"
- "nameTypes"
- "networkCountryCode"
- "nicknameMatchCount"
- "objectAtIndex:"
- "objectForKey:"
- "pathForResource:ofType:"
- "pathForResource:ofType:inDirectory:"
- "perform"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "personNameCount"
- "phoneticNamesByName"
- "phoneticValueAtIndex:forClassWithIdentifier:inModelWithIdentifier:"
- "previousName"
- "previousNameProperty"
- "q"
- "q16@0:8"
- "q32@0:8@\"NSString\"16@\"NSString\"24"
- "q32@0:8@16@24"
- "rangeOfString:"
- "recognitionAction"
- "recognitionResultByReplacingValueForClassIdentifier:withValue:"
- "release"
- "removeListenerID:forService:"
- "removeObject:"
- "requiredNameMatchType"
- "respondsToSelector:"
- "result"
- "resultFound"
- "resultPerson"
- "resultStatus"
- "retain"
- "retainCount"
- "self"
- "sensitiveActionsEnabled"
- "serialQueue"
- "set"
- "setAllNamesMatchedType:"
- "setAllowFirstFT:"
- "setAmbiguousValues:phoneticValues:forClassIdentifier:"
- "setCompositeNames:"
- "setContactIdentifier:"
- "setContactInfo:"
- "setContactsDataProvider:"
- "setDeviceCountryCode:"
- "setFirstNamesByLastNames:"
- "setHandle:"
- "setKeywords:"
- "setKnownValue:phoneticValue:forClassIdentifier:"
- "setKnownValues:phoneticValues:forClassIdentifier:"
- "setLastNameMatchType:"
- "setLastNamesByFirstNames:"
- "setLocalizedEmailLabels:"
- "setLocalizedPhoneLabels:"
- "setMatchedLabelType:"
- "setMatchedName:"
- "setNameToMatch:"
- "setNetworkCountryCode:"
- "setNicknameMatchCount:"
- "setObject:forKey:"
- "setOriginatingUIType:"
- "setPhoneticNamesByName:"
- "setPreviousName:"
- "setPreviousNameProperty:"
- "setRepeatedSpokenFeedbackString:"
- "setRequiredNameMatchType:"
- "setResult:"
- "setResultDisplayString:"
- "setResultFound:"
- "setResultPerson:"
- "setResultStatus:"
- "setSequenceTag:"
- "setSpokenCompositeNames:"
- "setSpokenFeedbackString:"
- "setStatusDisplayString:"
- "setTopLevelNonNickNames:"
- "setURL:"
- "setUnlocalizedEmailLabels:"
- "setUnlocalizedPhoneLabels:"
- "setUseCompositeNamesOnly:"
- "sharedInstance"
- "sortUsingSelector:"
- "spokenCompositeNames"
- "statusForID:onService:"
- "stopReportingChanges"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringValue"
- "stringWithFormat:"
- "substringToIndex:"
- "superclass"
- "telephonyProvider"
- "topLevelNonNickNames"
- "typeOfNameAtIndex:"
- "unionSet:"
- "unlocalizedEmailLabels"
- "unlocalizedPhoneLabels"
- "unsignedIntValue"
- "useCompositeNamesOnly"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8^@16"
- "v24@0:8^v16"
- "v24@0:8^{__CFString=}16"
- "v24@0:8q16"
- "v36@0:8^@16^@24i32"
- "validRecognitionResultFromRecognitionResult:"
- "validRecognitionResultFromRecognitionResult:knownDisambiguationValues:"
- "value"
- "valueAtIndex:forClassWithIdentifier:inModelWithIdentifier:"
- "valueCountForClassWithIdentifier:inModelWithIdentifier:"
- "valueOfFirstElementWithClassIdentifier:"
- "zone"
- "{?=\"hasDeterminedCompositePref\"b1\"compositeNamesOnly\"b1\"canVideoCall\"b1}"
- "{?=\"location\"q\"length\"q}"

```
