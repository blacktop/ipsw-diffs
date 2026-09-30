## TextInputCore

> `/System/Library/PrivateFrameworks/TextInputCore.framework/TextInputCore`

```diff

-3567.0.0.0.0
-  __TEXT.__text: 0x21a12c
+3568.1.4.0.0
+  __TEXT.__text: 0x216bb8
   __TEXT.__init_offsets: 0xc0
-  __TEXT.__objc_methlist: 0x10af0
+  __TEXT.__objc_methlist: 0x10618
   __TEXT.__dlopen_cstrs: 0x781
   __TEXT.__const: 0x2e40
-  __TEXT.__cstring: 0x1ca14
-  __TEXT.__oslogstring: 0x4479
-  __TEXT.__ustring: 0x7d8
-  __TEXT.__unwind_info: 0x7e08
+  __TEXT.__cstring: 0x1c8d8
+  __TEXT.__oslogstring: 0x42db
+  __TEXT.__ustring: 0x7e0
+  __TEXT.__unwind_info: 0x7cc8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4f30
-  __DATA_CONST.__objc_classlist: 0x858
+  __DATA_CONST.__const: 0x4ea8
+  __DATA_CONST.__objc_classlist: 0x808
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa088
-  __DATA_CONST.__objc_superrefs: 0x728
+  __DATA_CONST.__objc_selrefs: 0x9eb0
+  __DATA_CONST.__objc_superrefs: 0x6d8
   __DATA_CONST.__objc_arraydata: 0x10a8
-  __DATA_CONST.__got: 0x18b8
-  __AUTH_CONST.__const: 0x8870
-  __AUTH_CONST.__cfstring: 0x13e80
-  __AUTH_CONST.__objc_const: 0x1a680
+  __DATA_CONST.__got: 0x1890
+  __AUTH_CONST.__const: 0x8878
+  __AUTH_CONST.__cfstring: 0x13dc0
+  __AUTH_CONST.__objc_const: 0x19c88
   __AUTH_CONST.__weak_auth_got: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x3c0
-  __AUTH_CONST.__objc_intobj: 0x6c0
+  __AUTH_CONST.__objc_intobj: 0x690
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1af0
+  __AUTH_CONST.__auth_got: 0x1ac8
   __AUTH.__objc_data: 0x2080
   __AUTH.__data: 0x18
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0x12c8
+  __DATA.__objc_ivar: 0x1288
   __DATA.__data: 0x22a8
   __DATA.__common: 0x408
-  __DATA_DIRTY.__objc_data: 0x32f0
+  __DATA_DIRTY.__objc_data: 0x2fd0
   __DATA_DIRTY.__data: 0xb0
-  __DATA_DIRTY.__bss: 0xc50
+  __DATA_DIRTY.__bss: 0xc28
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10539
-  Symbols:   21821
-  CStrings:  4086
+  Functions: 10446
+  Symbols:   21580
+  CStrings:  4061
 
Symbols:
+ +[TIChineseExtras stringContainsOffensiveCharacter:]
+ +[TILaunchServicesLookup enumerateInstalledApplicationsWithPreferredLocalizations:block:]
+ +[TILaunchServicesLookup localizedNameForBundleIdentifier:preferredLocalizations:]
+ +[TITextCheckerExemptions(TestingSupport) _resetForTesting]
+ -[TIKeyboardInputManagerLoader releaseAllInputManagersAndLanguageModelResources]
+ -[TIMecabraEnvironment leftDocumentContextForCandidates]
+ -[TIMecabraEnvironmentContextWrapper setStringContext:]
+ -[TIMecabraEnvironmentContextWrapper stringContextIsEmpty]
+ -[TIMecabraEnvironmentContextWrapper stringContext]
+ -[TITextCheckerExemptionsImpl _resetForTesting]
+ -[TITextCheckerExemptionsImpl applyContactDeltaChanges:]
+ -[TITextCheckerExemptionsImpl rebuildAddressBookTokensFromSnapshot:]
+ _CFEqual
+ _CFNotificationCenterGetDistributedCenter
+ _CFNotificationCenterRemoveEveryObserver
+ _MecabraContextSetStringContext
+ _OBJC_IVAR_$_TIMecabraEnvironmentContextWrapper._stringContext
+ _OBJC_IVAR_$_TITextCheckerExemptionsImpl._contactDeltaObserver
+ _TIInputManagerServerOSLogFacility
+ _TIInputManagerServerOSLogFacility.logFacility
+ _TIInputManagerServerOSLogFacility.onceToken
+ __OBJC_$_CLASS_METHODS_TITextCheckerExemptions(TestingSupport)
+ __ZL17apply_token_deltaP10_LXLexiconRKNSt3__16vectorIN2KB6StringENS1_9allocatorIS4_EEEEi
+ __ZL20nameTokensForContactP10_ICContact
+ __ZL28filtered_tokens_for_app_nameP8NSStringRKN2KB16StaticDictionaryE
+ __ZL34preferred_localizations_for_localeRKN2KB6StringE
+ __ZN17AppTrieLoaderImpl22app_name_loading_queueEv
+ __ZN17AppTrieLoaderImpl33distributed_notification_callbackEP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2KB6StringENS_6vectorIS3_NS_9allocatorIS3_EEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS5_ISC_EEE17__deallocate_nodeB9fon220106EPNS_11__hash_nodeIS8_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2KB6StringENS_6vectorIS3_NS_9allocatorIS3_EEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS5_ISC_EEE4findIS3_EENS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2KB6StringENS_6vectorIS3_NS_9allocatorIS3_EEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS5_ISC_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2KB6StringENS_6vectorIS3_NS_9allocatorIS3_EEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS5_ISC_EEED2Ev
+ __ZZNSt3__112__hash_tableINS_17__hash_value_typeIN2KB6StringENS_6vectorIS3_NS_9allocatorIS3_EEEEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S7_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SC_SG_SE_EENS5_ISC_EEE16__emplace_uniqueB9fon220106IJRKNS_21piecewise_construct_tENS_5tupleIJOS3_EEENSQ_IJEEEEEENSA_INS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEEDpOT_ENKUlRSB_SP_OSS_OST_E_clES14_SP_S15_S16_
+ ___51-[TITextCheckerExemptionsImpl addObserverAssertion]_block_invoke_2
+ ___52+[TIChineseExtras stringContainsOffensiveCharacter:]_block_invoke
+ ___TIInputManagerServerOSLogFacility_block_invoke
+ ____ZN17AppTrieLoaderImpl20perform_initial_loadEv_block_invoke
+ ____ZN17AppTrieLoaderImpl33distributed_notification_callbackEP22__CFNotificationCenterPvPK10__CFStringPKvPK14__CFDictionary_block_invoke
+ ____ZZN17AppTrieLoaderImpl20perform_initial_loadEvENK3$_0clEv_block_invoke
+ ____ZZZN17AppTrieLoaderImpl20perform_initial_loadEvENK3$_0clEvENKUlvE_clEv_block_invoke
+ ___block_descriptor_40_a8_32s_e34_v24?0"NSArray"8"NSDictionary"16ls32l8
+ ___block_descriptor_48_8_32r_e5_v8?0lr32l8
+ ___block_descriptor_56_a8_32c45_ZTSNSt3__110shared_ptrI17AppTrieLoaderImplEE48c36_ZTSN2KB10retain_ptrIP10_LXLexiconEE_e35_v32?0"NSString"8"NSString"16^B24l
+ ___block_descriptor_56_a8_32c55_ZTSKZN17AppTrieLoaderImpl20perform_initial_loadEvE3$_0_e5_v8?0l
+ ___block_descriptor_56_a8_32c68_ZTSKZZN17AppTrieLoaderImpl20perform_initial_loadEvENK3$_0clEvEUlvE__e5_v8?0l
+ ___block_descriptor_57_a8_32s40c42_ZTSNSt3__18weak_ptrI17AppTrieLoaderImplEE_e5_v8?0l
+ ___copy_helper_block_a8_32c45_ZTSNSt3__110shared_ptrI17AppTrieLoaderImplEE48c36_ZTSN2KB10retain_ptrIP10_LXLexiconEE
+ ___copy_helper_block_a8_32c55_ZTSKZN17AppTrieLoaderImpl20perform_initial_loadEvE3$_0
+ ___copy_helper_block_a8_32c68_ZTSKZZN17AppTrieLoaderImpl20perform_initial_loadEvENK3$_0clEvEUlvE_
+ ___copy_helper_block_a8_40c42_ZTSNSt3__18weak_ptrI17AppTrieLoaderImplEE
+ ___destroy_helper_block_a8_32c45_ZTSNSt3__110shared_ptrI17AppTrieLoaderImplEE48c36_ZTSN2KB10retain_ptrIP10_LXLexiconEE
+ ___destroy_helper_block_a8_32c55_ZTSKZN17AppTrieLoaderImpl20perform_initial_loadEvE3$_0
+ ___destroy_helper_block_a8_32c68_ZTSKZZN17AppTrieLoaderImpl20perform_initial_loadEvENK3$_0clEvEUlvE_
+ ___destroy_helper_block_a8_40c42_ZTSNSt3__18weak_ptrI17AppTrieLoaderImplEE
+ ___getLSApplicationRecordClass_block_invoke
+ _getLSApplicationRecordClass
+ _getLSApplicationRecordClass.softClass
+ _malloc_zone_pressure_relief
+ _objc_msgSend$_resetForTesting
+ _objc_msgSend$applyContactDeltaChanges:
+ _objc_msgSend$currentLoadedInputModes
+ _objc_msgSend$enumerateInstalledApplicationsWithPreferredLocalizations:block:
+ _objc_msgSend$enumeratorWithOptions:
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$leftDocumentContextForCandidates
+ _objc_msgSend$localizedNameForBundleIdentifier:preferredLocalizations:
+ _objc_msgSend$localizedNameWithPreferredLocalizations:
+ _objc_msgSend$nextObject
+ _objc_msgSend$objectForKey:ofClass:
+ _objc_msgSend$rebuildAddressBookTokensFromSnapshot:
+ _objc_msgSend$releaseAllInputManagersAndLanguageModelResources
+ _objc_msgSend$setStringContext:
+ _objc_msgSend$stringContext
+ _objc_msgSend$stringContextIsEmpty
+ _stringContainsOffensiveCharacter:.offensiveCharacterSet
+ _stringContainsOffensiveCharacter:.onceToken
- +[HCBurstTrie burstTrieFromFile:]
- +[HCHuffmanCoder characterCoderForLocale:]
- +[HCHuffmanCoder coderFromBurstTrieFile:indexTableFile:]
- +[HCHuffmanCoder coderMatchingName:locale:]
- +[HCHuffmanCoder wordCoderForLocale:]
- +[HCIndexTable indexTableFromFile:]
- +[TIDPNgramRecorder enumerateNgramsFromSession:n:usingBlock:]
- +[TIDPWordRecord word:atPosition:coder:]
- +[TILaunchServicesLookup enumerateInstalledApplicationNames:]
- +[TILaunchServicesLookup lookupAppNames]
- +[TILaunchServicesLookup sharedInstance]
- -[HCBurstTrie _createUnderlyingBurstTrie]
- -[HCBurstTrie burstTrie]
- -[HCBurstTrie count]
- -[HCBurstTrie dealloc]
- -[HCBurstTrie init]
- -[HCBurstTrie keysAdded]
- -[HCBurstTrie payloadForKey:]
- -[HCBurstTrie setBurstTrie:]
- -[HCBurstTrie writeToFile:]
- -[HCHuffmanCoder .cxx_destruct]
- -[HCHuffmanCoder burstTrie]
- -[HCHuffmanCoder codeForKey:]
- -[HCHuffmanCoder count]
- -[HCHuffmanCoder indexTable]
- -[HCHuffmanCoder initWithBurstTrie:indexTable:]
- -[HCHuffmanCoder init]
- -[HCHuffmanCoder setBurstTrie:]
- -[HCHuffmanCoder setIndexTable:]
- -[HCHuffmanCoder stringCodeForKey:]
- -[HCHuffmanCoder versionUUID]
- -[HCIndexTable .cxx_construct]
- -[HCIndexTable .cxx_destruct]
- -[HCIndexTable codeAtIndex:]
- -[HCIndexTable count]
- -[HCIndexTable fileHeader]
- -[HCIndexTable huffmanCodesMemoryMappedData]
- -[HCIndexTable huffmanCodes]
- -[HCIndexTable initWithHuffmanCodesMemoryMappedData:]
- -[HCIndexTable init]
- -[HCIndexTable isValid]
- -[HCIndexTable versionUUID]
- -[HCIndexTable writeToFile:]
- -[TIDPNamedEntityTokenRecorder delegate]
- -[TIDPNamedEntityTokenRecorder recordingKey]
- -[TIDPNamedEntityTokenRecorder records]
- -[TIDPNamedEntityTokenRecorder report]
- -[TIDPNgramRecorder _normalizedWordEntryStringForWordEntry:]
- -[TIDPNgramRecorder delegate]
- -[TIDPNgramRecorder initWithTypingSession:aligned:n:shouldDonateNgramSampleRandomly:]
- -[TIDPNgramRecorder randomRecordsLimitedByCount:]
- -[TIDPNgramRecorder randomRecords]
- -[TIDPNgramRecorder recordingKey]
- -[TIDPNgramRecorder records]
- -[TIDPNgramRecorder report]
- -[TIDPNgramRecorder setShouldDonateNgramSampleRandomly:]
- -[TIDPNgramRecorder shouldDonateNgramSampleRandomly]
- -[TIDPNgramRecorderCascading initWithTypingSession:aligned:n:]
- -[TIDPNgramRecorderCascading n]
- -[TIDPNgramRecorderCascading report]
- -[TIDPNgramRecorderCascading setN:]
- -[TIDPNgramRecorderRandom initWithTypingSession:aligned:n:]
- -[TIDPNgramRecorderRandom report]
- -[TIDPNgramWordEntryPair .cxx_destruct]
- -[TIDPNgramWordEntryPair initWithWordString:]
- -[TIDPNgramWordEntryPair initWithWordString:wordEntryAligned:]
- -[TIDPNgramWordEntryPair isStandaloneString]
- -[TIDPNgramWordEntryPair setWordEntryAligned:]
- -[TIDPNgramWordEntryPair setWordString:]
- -[TIDPNgramWordEntryPair wordEntryAligned]
- -[TIDPNgramWordEntryPair wordString]
- -[TIDPRecorder _prepareCharacterCoderMatchingSession]
- -[TIDPRecorder _prepareWordCoderMatchingSession]
- -[TIDPRecorder characterCoder]
- -[TIDPRecorder characterExplodedRecords]
- -[TIDPRecorder wordCoder]
- -[TIDPUnknownTokenRecorder delegate]
- -[TIDPUnknownTokenRecorder recordingKey]
- -[TIDPUnknownTokenRecorder records]
- -[TIDPUnknownTokenRecorder report]
- -[TIDPUnknownTokenWithContextRecorder recordingKey]
- -[TIDPUnknownTokenWithContextRecorder records]
- -[TIDPWordRecord codedWordAsString]
- -[TIDPWordRecord codedWord]
- -[TIDPWordRecord coderVersion]
- -[TIDPWordRecord coder]
- -[TIDPWordRecord setCoder:]
- -[TIDPWordRecord toDPWordRecord]
- -[TILaunchServicesLookup .cxx_destruct]
- -[TILaunchServicesLookup appNames]
- -[TILaunchServicesLookup cacheNames:]
- -[TILaunchServicesLookup cache]
- -[TILaunchServicesLookup dealloc]
- -[TILaunchServicesLookup enumerateAppNames:]
- -[TILaunchServicesLookup handleMemoryPressureLevel:excessMemoryInBytes:]
- -[TILaunchServicesLookup init]
- -[TILaunchServicesLookup keyboardActivityDidTransition:]
- -[TILaunchServicesLookup lastCacheUpdate]
- -[TILaunchServicesLookup resetCache]
- -[TILaunchServicesLookup setCache:]
- -[TILaunchServicesLookup setLastCacheUpdate:]
- -[TILaunchServicesLookup tryCache]
- -[TIMecabraEnvironmentContextWrapper contextString:forRightContext:]
- _CFBurstTrieContains
- _CFBurstTrieCreate
- _CFBurstTrieCreateFromMapBytes
- _CFBurstTrieGetCount
- _CFBurstTrieRelease
- _CFBurstTrieSerializeWithFileDescriptor
- _CoreServicesLibrary
- _MecabraGetLengthForContextString
- _OBJC_CLASS_$_HCBurstTrie
- _OBJC_CLASS_$_HCHuffmanCoder
- _OBJC_CLASS_$_HCIndexTable
- _OBJC_CLASS_$_TIDPNamedEntityTokenRecorder
- _OBJC_CLASS_$_TIDPNgramRecorder
- _OBJC_CLASS_$_TIDPNgramRecorderCascading
- _OBJC_CLASS_$_TIDPNgramRecorderRandom
- _OBJC_CLASS_$_TIDPNgramWordEntryPair
- _OBJC_CLASS_$_TIDPUnknownTokenRecorder
- _OBJC_CLASS_$_TIDPUnknownTokenWithContextRecorder
- _OBJC_CLASS_$__DPNumericDataRecorder
- _OBJC_CLASS_$__DPWordRecord
- _OBJC_CLASS_$__DPWordRecorder
- _OBJC_IVAR_$_HCBurstTrie._burstTrie
- _OBJC_IVAR_$_HCBurstTrie._keysAdded
- _OBJC_IVAR_$_HCHuffmanCoder._burstTrie
- _OBJC_IVAR_$_HCHuffmanCoder._indexTable
- _OBJC_IVAR_$_HCIndexTable._fileHeader
- _OBJC_IVAR_$_HCIndexTable._huffmanCodesMemoryMappedData
- _OBJC_IVAR_$_HCIndexTable._mutableHuffmanCodes
- _OBJC_IVAR_$_HCIndexTable._versionUUID
- _OBJC_IVAR_$_TIDPNgramRecorder._shouldDonateNgramSampleRandomly
- _OBJC_IVAR_$_TIDPNgramRecorderCascading._n
- _OBJC_IVAR_$_TIDPNgramWordEntryPair._wordEntryAligned
- _OBJC_IVAR_$_TIDPNgramWordEntryPair._wordString
- _OBJC_IVAR_$_TIDPRecorder._characterCoder
- _OBJC_IVAR_$_TIDPRecorder._wordCoder
- _OBJC_IVAR_$_TIDPWordRecord._coder
- _OBJC_IVAR_$_TILaunchServicesLookup._cache
- _OBJC_IVAR_$_TILaunchServicesLookup._lastCacheUpdate
- _OBJC_IVAR_$_TITextCheckerExemptionsImpl._contactObserver
- _OBJC_METACLASS_$_HCBurstTrie
- _OBJC_METACLASS_$_HCHuffmanCoder
- _OBJC_METACLASS_$_HCIndexTable
- _OBJC_METACLASS_$_TIDPNamedEntityTokenRecorder
- _OBJC_METACLASS_$_TIDPNgramRecorder
- _OBJC_METACLASS_$_TIDPNgramRecorderCascading
- _OBJC_METACLASS_$_TIDPNgramRecorderRandom
- _OBJC_METACLASS_$_TIDPNgramWordEntryPair
- _OBJC_METACLASS_$_TIDPUnknownTokenRecorder
- _OBJC_METACLASS_$_TIDPUnknownTokenWithContextRecorder
- __OBJC_$_CLASS_METHODS_HCBurstTrie
- __OBJC_$_CLASS_METHODS_HCHuffmanCoder
- __OBJC_$_CLASS_METHODS_HCIndexTable
- __OBJC_$_CLASS_METHODS_TIDPNgramRecorder
- __OBJC_$_INSTANCE_METHODS_HCBurstTrie
- __OBJC_$_INSTANCE_METHODS_HCHuffmanCoder
- __OBJC_$_INSTANCE_METHODS_HCIndexTable
- __OBJC_$_INSTANCE_METHODS_TIDPNamedEntityTokenRecorder
- __OBJC_$_INSTANCE_METHODS_TIDPNgramRecorder
- __OBJC_$_INSTANCE_METHODS_TIDPNgramRecorderCascading
- __OBJC_$_INSTANCE_METHODS_TIDPNgramRecorderRandom
- __OBJC_$_INSTANCE_METHODS_TIDPNgramWordEntryPair
- __OBJC_$_INSTANCE_METHODS_TIDPUnknownTokenRecorder
- __OBJC_$_INSTANCE_METHODS_TIDPUnknownTokenWithContextRecorder
- __OBJC_$_INSTANCE_METHODS_TILaunchServicesLookup
- __OBJC_$_INSTANCE_VARIABLES_HCBurstTrie
- __OBJC_$_INSTANCE_VARIABLES_HCHuffmanCoder
- __OBJC_$_INSTANCE_VARIABLES_HCIndexTable
- __OBJC_$_INSTANCE_VARIABLES_TIDPNgramRecorder
- __OBJC_$_INSTANCE_VARIABLES_TIDPNgramRecorderCascading
- __OBJC_$_INSTANCE_VARIABLES_TIDPNgramWordEntryPair
- __OBJC_$_INSTANCE_VARIABLES_TILaunchServicesLookup
- __OBJC_$_PROP_LIST_HCBurstTrie
- __OBJC_$_PROP_LIST_HCHuffmanCoder
- __OBJC_$_PROP_LIST_HCIndexTable
- __OBJC_$_PROP_LIST_TIDPNgramRecorder
- __OBJC_$_PROP_LIST_TIDPNgramRecorderCascading
- __OBJC_$_PROP_LIST_TIDPNgramWordEntryPair
- __OBJC_$_PROP_LIST_TILaunchServicesLookup
- __OBJC_CLASS_PROTOCOLS_$_TILaunchServicesLookup
- __OBJC_CLASS_RO_$_HCBurstTrie
- __OBJC_CLASS_RO_$_HCHuffmanCoder
- __OBJC_CLASS_RO_$_HCIndexTable
- __OBJC_CLASS_RO_$_TIDPNamedEntityTokenRecorder
- __OBJC_CLASS_RO_$_TIDPNgramRecorder
- __OBJC_CLASS_RO_$_TIDPNgramRecorderCascading
- __OBJC_CLASS_RO_$_TIDPNgramRecorderRandom
- __OBJC_CLASS_RO_$_TIDPNgramWordEntryPair
- __OBJC_CLASS_RO_$_TIDPUnknownTokenRecorder
- __OBJC_CLASS_RO_$_TIDPUnknownTokenWithContextRecorder
- __OBJC_METACLASS_RO_$_HCBurstTrie
- __OBJC_METACLASS_RO_$_HCHuffmanCoder
- __OBJC_METACLASS_RO_$_HCIndexTable
- __OBJC_METACLASS_RO_$_TIDPNamedEntityTokenRecorder
- __OBJC_METACLASS_RO_$_TIDPNgramRecorder
- __OBJC_METACLASS_RO_$_TIDPNgramRecorderCascading
- __OBJC_METACLASS_RO_$_TIDPNgramRecorderRandom
- __OBJC_METACLASS_RO_$_TIDPNgramWordEntryPair
- __OBJC_METACLASS_RO_$_TIDPUnknownTokenRecorder
- __OBJC_METACLASS_RO_$_TIDPUnknownTokenWithContextRecorder
- __ZGVZ23-[HCIndexTable isValid]E12staticHeader
- __ZL21libmecabraLibraryCorePPc
- __ZL42getMecabraContextSetStringContextSymbolLocv
- __ZZ23-[HCIndexTable isValid]E12staticHeader
- __ZZL21libmecabraLibraryCorePPcE16frameworkLibrary
- __ZZL42getMecabraContextSetStringContextSymbolLocvE3ptr
- ___28-[TIDPNgramRecorder records]_block_invoke
- ___40+[TILaunchServicesLookup lookupAppNames]_block_invoke
- ___40+[TILaunchServicesLookup sharedInstance]_block_invoke
- ___40-[TIDPRecorder characterExplodedRecords]_block_invoke
- ___43+[HCHuffmanCoder coderMatchingName:locale:]_block_invoke
- ___46-[TIDPUnknownTokenWithContextRecorder records]_block_invoke
- ___46-[TIDPUnknownTokenWithContextRecorder records]_block_invoke_2
- ____ZL21libmecabraLibraryCorePPc_block_invoke
- ____ZL27background_append_app_namesN2KB10retain_ptrIP10_LXLexiconEERKNS_16StaticDictionaryE_block_invoke
- ____ZL42getMecabraContextSetStringContextSymbolLocv_block_invoke
- ____ZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1__block_invoke
- ____ZZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_ENK3$_0clEv_block_invoke
- ___block_descriptor_144_a8_32c42_ZTSNSt3__18weak_ptrI17AppTrieLoaderImplEE48c17_ZTSKN2KB6StringE80c17_ZTSKN2KB6StringE112c17_ZTSKN2KB6StringE_e22_v16?0"NSDictionary"8l
- ___block_descriptor_152_a8_32c85_ZTSKZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_E3$_0_e5_v8?0l
- ___block_descriptor_152_a8_32c98_ZTSKZZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_ENK3$_0clEvEUlvE__e5_v8?0l
- ___block_descriptor_32_e35_B32?0"TIWordEntryAligned"8Q16^B24l
- ___block_descriptor_40_8_32r_e57_v44?0^{__CFURL=}8i16^{__CFLocale=}20^{__CFString=}28^B36lr32l8
- ___block_descriptor_40_8_32s_e27_v24?0"LSBundleProxy"8^B16ls32l8
- ___block_descriptor_48_8_32s40s_e21_v24?0"NSArray"8^B16ls32l8s40l8
- ___block_descriptor_48_a8_32c36_ZTSN2KB10retain_ptrIP10_LXLexiconEE_e22_v24?0"NSString"8^B16l
- ___block_descriptor_48_a8_32r_e5_v8?0lr32l8
- ___copy_helper_block_a8_32c36_ZTSN2KB10retain_ptrIP10_LXLexiconEE
- ___copy_helper_block_a8_32c42_ZTSNSt3__18weak_ptrI17AppTrieLoaderImplEE48c17_ZTSKN2KB6StringE80c17_ZTSKN2KB6StringE112c17_ZTSKN2KB6StringE
- ___copy_helper_block_a8_32c85_ZTSKZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_E3$_0
- ___copy_helper_block_a8_32c98_ZTSKZZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_ENK3$_0clEvEUlvE_
- ___destroy_helper_block_a8_32c36_ZTSN2KB10retain_ptrIP10_LXLexiconEE
- ___destroy_helper_block_a8_32c42_ZTSNSt3__18weak_ptrI17AppTrieLoaderImplEE48c17_ZTSKN2KB6StringE80c17_ZTSKN2KB6StringE112c17_ZTSKN2KB6StringE
- ___destroy_helper_block_a8_32c85_ZTSKZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_E3$_0
- ___destroy_helper_block_a8_32c98_ZTSKZZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_ENK3$_0clEvEUlvE_
- ___getLSApplicationProxyClass_block_invoke
- ___getLSApplicationWorkspaceClass_block_invoke
- _fileno
- _getLSApplicationProxyClass.softClass
- _getLSApplicationWorkspaceClass.softClass
- _log2
- _objc_msgSend$_createUnderlyingBurstTrie
- _objc_msgSend$_normalizedWordEntryStringForWordEntry:
- _objc_msgSend$_prepareCharacterCoderMatchingSession
- _objc_msgSend$_prepareWordCoderMatchingSession
- _objc_msgSend$appNames
- _objc_msgSend$applicationProxyForIdentifier:
- _objc_msgSend$applicationType
- _objc_msgSend$burstTrieFromFile:
- _objc_msgSend$bytes
- _objc_msgSend$cache
- _objc_msgSend$cacheNames:
- _objc_msgSend$characterCoder
- _objc_msgSend$characterCoderForLocale:
- _objc_msgSend$characterExplodedRecords
- _objc_msgSend$cleanedWord
- _objc_msgSend$codeAtIndex:
- _objc_msgSend$codeForKey:
- _objc_msgSend$codedWord
- _objc_msgSend$codedWordAsString
- _objc_msgSend$coder
- _objc_msgSend$coderFromBurstTrieFile:indexTableFile:
- _objc_msgSend$coderMatchingName:locale:
- _objc_msgSend$coderVersion
- _objc_msgSend$contextString:forRightContext:
- _objc_msgSend$dataWithBytesNoCopy:length:freeWhenDone:
- _objc_msgSend$dataWithContentsOfFile:options:error:
- _objc_msgSend$deletionRangesWithElementsToKeep:
- _objc_msgSend$enumerateAppNames:
- _objc_msgSend$enumerateBundlesOfType:block:
- _objc_msgSend$enumerateInstalledApplicationNames:
- _objc_msgSend$enumerateNgramsFromSession:n:usingBlock:
- _objc_msgSend$fileHandleForWritingAtPath:
- _objc_msgSend$fileHeader
- _objc_msgSend$huffmanCodes
- _objc_msgSend$huffmanCodesMemoryMappedData
- _objc_msgSend$indexTable
- _objc_msgSend$indexTableFromFile:
- _objc_msgSend$initWithBurstTrie:indexTable:
- _objc_msgSend$initWithHuffmanCodesMemoryMappedData:
- _objc_msgSend$initWithKey:
- _objc_msgSend$initWithTypingSession:aligned:n:
- _objc_msgSend$initWithTypingSession:aligned:n:shouldDonateNgramSampleRandomly:
- _objc_msgSend$initWithWordString:
- _objc_msgSend$initWithWordString:wordEntryAligned:
- _objc_msgSend$isFeatureEnabledForInternalBuilds
- _objc_msgSend$isFromStaticLexicon
- _objc_msgSend$isStandaloneString
- _objc_msgSend$lastCacheUpdate
- _objc_msgSend$lookupAppNames
- _objc_msgSend$n
- _objc_msgSend$objectForInfoDictionaryKey:ofClass:
- _objc_msgSend$payloadForKey:
- _objc_msgSend$randomRecords
- _objc_msgSend$randomRecordsLimitedByCount:
- _objc_msgSend$record:metadata:
- _objc_msgSend$setCache:
- _objc_msgSend$setCoder:
- _objc_msgSend$setLastCacheUpdate:
- _objc_msgSend$setN:
- _objc_msgSend$setShouldDonateNgramSampleRandomly:
- _objc_msgSend$setWordEntryAligned:
- _objc_msgSend$setWordString:
- _objc_msgSend$shouldDonateNgramSampleRandomly
- _objc_msgSend$stringCodeForKey:
- _objc_msgSend$toDPWordRecord
- _objc_msgSend$tryCache
- _objc_msgSend$unsignedLongLongValue
- _objc_msgSend$versionUUID
- _objc_msgSend$word:atPosition:coder:
- _objc_msgSend$wordCoder
- _objc_msgSend$wordCoderForLocale:
- _objc_msgSend$wordEntryAligned
- _objc_msgSend$wordString
- _objc_msgSend$writeData:error:
CStrings:
+ "%s  kbd is %zu bytes over the inactive limit, hard-resetting all language models (including advanced ones)"
+ "%s  kbd is still %zu bytes over the inactive limit, releasing all cached input managers and language model resources"
+ "%s Adding app to lexicon: %@ (%@)"
+ "%s Registering for LaunchServices app install/uninstall notifications"
+ "%s Removing LaunchServices app install/uninstall observer"
+ "%s Removing app from lexicon: %@"
+ "%s TITextCheckerExemptions:applyContactDeltaChanges - applying %lu delta records"
+ "%s TITextCheckerExemptions:rebuildAddressBookTokensFromSnapshot - rebuilding from snapshot of %lu contacts"
+ "%s perform_initial_load perf: %.3f ms"
+ "-[TITextCheckerExemptionsImpl applyContactDeltaChanges:]"
+ "-[TITextCheckerExemptionsImpl rebuildAddressBookTokensFromSnapshot:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__bit_reference:113: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1171: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:419: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:434: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:438: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:442: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:446: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:509: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:297: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/optional:1112: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/optional:1121: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/optional:1130: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/span:508: libc++ Hardening assertion __count <= size() failed: span<T>::last(count): count out of range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/span:537: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/string_view:343: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
+ "KBDInputManagerServer"
+ "LSApplicationRecord"
+ "SBInternalAppTag"
+ "bundleIDs"
+ "com.apple.LaunchServices.applicationRegistered"
+ "com.apple.LaunchServices.applicationUnregistered"
+ "install_app"
+ "isPlaceholder"
+ "operator()_block_invoke"
+ "perform_initial_load"
+ "register_for_app_changes"
+ "uninstall_app"
+ "屄屌肏"
- "%@.htbl"
- "%@.triemap"
- "%s  %@"
- "%s  Could not load the huffman coder from the supplied file paths."
- "%s  Couldn't find a Huffman coder for locale: '%@'"
- "%s  Couldn't open file '%@' for writing."
- "%s  Error while loading index map from file: '%@'"
- "%s  Got installed app names (count = %lu)."
- "%s  Not recording n-grams for locale '%@' because a valid word coder could not be loaded."
- "%s  Not recording unknown tokens for locale '%@' because a valid character coder could not be loaded."
- "%s  Requesting installed app names from LaunchServices."
- "%s  Using random n value: %lu"
- "%s  kbd is already over inactive limit, hard-resetting all language models (including advanced ones)"
- "%s Adding app names entries to dynamic trie and vocabulary"
- "%s Adding contact observer for app names"
- "%s Removing contact observer for app names"
- "%s TITextCheckerExemptions:addObserverAssertion - processing %ld contacts"
- "+[HCHuffmanCoder coderFromBurstTrieFile:indexTableFile:]"
- "+[HCHuffmanCoder coderMatchingName:locale:]"
- "+[HCIndexTable indexTableFromFile:]"
- "-[HCIndexTable writeToFile:]"
- "-[TIDPNgramRecorder records]"
- "-[TIDPNgramRecorderRandom report]"
- "-[TIDPUnknownTokenRecorder records]"
- "-[TILaunchServicesLookup appNames]"
- "-[TITextCheckerExemptionsImpl addObserverAssertion]_block_invoke"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__bit_reference:113: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__utility/is_pointer_in_range.h:38: libc++ Hardening assertion std::__is_valid_range(__begin, __end) failed: [__begin, __end) is not a valid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1171: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:419: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:434: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:438: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:442: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:446: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:509: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector_bool.h:297: libc++ Hardening assertion __n < size() failed: vector<bool>::operator[] index out of bounds\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1112: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1121: libc++ Hardening assertion this->has_value() failed: optional operator-> called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/optional:1130: libc++ Hardening assertion this->has_value() failed: optional operator* called on a disengaged value\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:508: libc++ Hardening assertion __count <= size() failed: span<T>::last(count): count out of range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/span:537: libc++ Hardening assertion __idx < size() failed: span<T>::operator[](index): index out of range\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/string_view:343: libc++ Hardening assertion (__end - __begin) >= 0 failed: std::string_view::string_view(iterator, sentinel) received invalid range\n"
- "/usr/lib/libmecabra.dylib"
- "/usr/local/lib/libmecabra.dylib"
- "B32@?0@\"TIWordEntryAligned\"8Q16^B24"
- "DifferentialPrivacyHuffmanCoder"
- "Hidden"
- "Internal"
- "LSApplicationProxy"
- "MecabraContextSetStringContext"
- "TIDPReporterMock"
- "UNKNOWN_VERSION"
- "VersionHash"
- "background_append_app_names"
- "background_append_app_names_block_invoke"
- "chars"
- "com.apple.TextInput.AddressBookNameMatch."
- "com.apple.TextInput.UnknownToken."
- "com.apple.TextInput.UnknownTokenWithContext."
- "com.apple.TextInput.WordNgrams.%lu."
- "u_token"
- "v24@?0@\"LSBundleProxy\"8^B16"
- "v24@?0@\"NSArray\"8^B16"
- "wb+"
- "words"
```
