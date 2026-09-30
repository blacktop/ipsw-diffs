## VoiceDial

> `/System/Library/VoiceServices/PlugIns/VoiceDial.vsplugin/VoiceDial`

```diff

-3027.400.41.2.2
-  __TEXT.__text: 0xa7e0
+3027.500.161.0.0
+  __TEXT.__text: 0xad60
   __TEXT.__auth_stubs: 0x7a0
   __TEXT.__objc_methlist: 0x92c
-  __TEXT.__const: 0x78
+  __TEXT.__const: 0x88
   __TEXT.__oslogstring: 0x15b
   __TEXT.__cstring: 0x6a4
   __TEXT.__gcc_except_tab: 0x120
-  __TEXT.__unwind_info: 0x228
+  __TEXT.__unwind_info: 0x250
   __TEXT.__objc_classname: 0x222
   __TEXT.__objc_methname: 0x1aac
   __TEXT.__objc_methtype: 0x51b

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12A7B7B9-5C16-301E-8F81-EB7C9EDFC474
+  UUID: D7347F99-8C6D-3B09-B0F8-B251BD9B2B3F
   Functions: 195
   Symbols:   980
   CStrings:  580
Symbols:
+ _objc_release_x3
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
Functions:
~ -[VoiceDialResultHandlerContext init] : 88 -> 80
~ -[VoiceDialResultHandler _nameSource] : 108 -> 124
~ -[VoiceDialResultHandler _addressBook] : 128 -> 132
~ -[VoiceDialResultHandler actionForRecognitionResults:] : 7244 -> 7484
~ __ResultHandlerAddressBookCallback : 3576 -> 3672
~ __CommaSeparatedStringFromArray : 324 -> 356
~ _PHDefaultLog : 68 -> 84
~ _PHOversizedLog : 68 -> 84
~ _PHOversizedLogQueue : 68 -> 84
~ ___PHOversizedLogQueue_block_invoke : 104 -> 108
~ -[VoiceDialRecognitionAction perform] : 660 -> 696
~ -[DigitDialResultValidator deviceCountryCode] : 80 -> 92
~ -[DigitDialResultValidator networkCountryCode] : 80 -> 92
~ -[DigitDialResultValidator _copyExceptionsForCountryCode:] : 208 -> 220
~ -[DigitDialResultValidator _isValidExceptionForDevice:] : 124 -> 128
~ -[DigitDialResultValidator _isValidExceptionForNetwork:] : 124 -> 128
~ -[DigitDialResultValidator indexOfValidPhoneNumber:] : 416 -> 404
~ -[DigitDialResultValidator validRecognitionResultFromRecognitionResult:] : 128 -> 140
~ -[DigitDialResultValidator setDeviceCountryCode:] : 12 -> 64
~ -[DigitDialResultValidator setNetworkCountryCode:] : 12 -> 64
~ -[DigitDialResultHandler actionForRecognitionResult:] : 828 -> 908
~ -[DigitDialResultHandler contactsDataProvider] : 128 -> 136
~ -[DigitDialResultHandler setContactsDataProvider:] : 12 -> 64
~ _DigitDialPhoneNumberFromResult : 1832 -> 1932
~ __SpokenValueFromElementValue : 96 -> 100
~ __AppendValueToPhoneNumbersInRange : 428 -> 432
~ +[VoiceDialNameDataSource _nameDataSourceByLanguageMap] : 72 -> 88
~ __CreateNameDataSourceMap : 168 -> 180
~ +[VoiceDialNameDataSource nameDataSourceForLanguageIdentifier:] : 232 -> 244
~ -[VoiceDialNameDataSource matchingNameType:fromTypes:forPerson:] : 452 -> 444
~ _VoiceDialMaidenNameDataSourceCreateMaidenNameFromLastName : 1244 -> 1252
~ -[VoiceDialVoicemailRecognitionAction init] : 308 -> 328
~ _VoiceDialCopyNameLabelAndTypeFromRecognitionResult : 556 -> 532
~ _VoiceDialCopyNamesLabelAndTypeFromRecognitionResults : 480 -> 472
~ _VoiceDialSendNameAndExtendedLabelMatches : 984 -> 976
~ _VoiceDialCopyMostLikelyNumberWithPersonAndLabel : 568 -> 596
~ _stringValueForContactProperty : 152 -> 164
~ _VoiceDialGetMostLikelyFacetimeContactWithPersonAndLabel : 964 -> 992
~ _VoiceDialCopyErrorActionForResult : 372 -> 384
~ _VoiceDialSpokenLocalizedString : 132 -> 148
~ _VoiceDialBundle : 108 -> 120
~ _VoiceDialSpokenLocalizedStringIfAvailable : 356 -> 368
~ _VoiceDialConfigureSpokenLocalizedLabel : 324 -> 336
~ _VoiceDialNumberToDialForNumber : 156 -> 160
~ _VoiceDialTelephonyUtilitiesFrameworkHandle : 92 -> 96
~ -[NSDictionary(VoiceDialResultHandlerMerge) mergeSetValuesIntoArray] : 348 -> 356
~ -[VDDisambiguationAddressBookContext setPreviousName:] : 12 -> 64
~ -[VDDisambiguationAddressBookContext setMatchedName:] : 12 -> 64
~ -[VDDisambiguationAddressBookContext setResult:] : 12 -> 64
~ -[VoiceDialDataProvider init] : 252 -> 264
~ -[VoiceDialDataProvider dealloc] : 188 -> 192
~ -[VoiceDialDataProvider _addressBook] : 128 -> 132
~ -[VoiceDialDataProvider _namesSource] : 140 -> 156
~ -[VoiceDialDataProvider getLabels:andWeightedLabels:ForABProperty:] : 1732 -> 1768
~ ___67-[VoiceDialDataProvider getLabels:andWeightedLabels:ForABProperty:]_block_invoke : 244 -> 264
~ -[VoiceDialDataProvider _phoneLabels] : 168 -> 160
~ -[VoiceDialDataProvider _facetimeLabels] : 344 -> 348
~ -[VoiceDialDataProvider _totalPeople] : 176 -> 180
~ -[VoiceDialDataProvider _voiceDialRecordAtIndex:] : 508 -> 516
~ -[VoiceDialDataProvider valueCountForClassWithIdentifier:inModelWithIdentifier:] : 156 -> 168
~ -[VoiceDialDataProvider getValue:weight:atIndex:forClassWithIdentifier:inModelWithIdentifier:] : 424 -> 432
~ ___48-[VoiceDialDataProvider cacheValidityIdentifier]_block_invoke : 332 -> 336
~ -[VoiceDialDataProvider isCacheValidityIdentifierValid:] : 588 -> 592
~ ___56-[VoiceDialDataProvider isCacheValidityIdentifierValid:]_block_invoke : 412 -> 424
~ -[VoiceDialDataProvider beginReportingChanges] : 156 -> 160
~ -[VoiceDialDataProvider stopReportingChanges] : 172 -> 176
~ -[VoiceDialDataProvider _handleAddressBookChanged] : 156 -> 160
~ -[VoiceDialFacetimeRecognitionAction perform] : 648 -> 688
~ -[VoiceDialResultValidator _addressBook] : 128 -> 132
~ -[VoiceDialResultValidator _nameSource] : 108 -> 124
~ -[VoiceDialResultValidator validRecognitionResultFromRecognitionResult:] : 464 -> 468
~ -[VoiceDialResultValidator validRecognitionResultFromRecognitionResult:knownDisambiguationValues:] : 1060 -> 1068
~ __ResultDisambiguationAddressBookCallback : 584 -> 580

```
