## TextInputCore

> `/System/Library/PrivateFrameworks/TextInputCore.framework/Versions/A/TextInputCore`

```diff

-3567.400.0.0.0
-  __TEXT.__text: 0x1f88dc
+3568.1.4.0.0
+  __TEXT.__text: 0x1f3e10
   __TEXT.__init_offsets: 0xc0
-  __TEXT.__objc_methlist: 0x10068
-  __TEXT.__const: 0x2e10
-  __TEXT.__cstring: 0x12c69
+  __TEXT.__objc_methlist: 0xfb90
+  __TEXT.__const: 0x2e00
+  __TEXT.__cstring: 0x1296d
   __TEXT.__dlopen_cstrs: 0x9d
-  __TEXT.__oslogstring: 0x3b40
-  __TEXT.__ustring: 0x7bc
-  __TEXT.__unwind_info: 0x77b0
+  __TEXT.__oslogstring: 0x39a2
+  __TEXT.__ustring: 0x7c4
+  __TEXT.__unwind_info: 0x7648
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19f8
-  __DATA_CONST.__objc_classlist: 0x818
+  __DATA_CONST.__const: 0x19c0
+  __DATA_CONST.__objc_classlist: 0x7c8
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9520
-  __DATA_CONST.__objc_superrefs: 0x6d8
+  __DATA_CONST.__objc_selrefs: 0x9340
+  __DATA_CONST.__objc_superrefs: 0x688
   __DATA_CONST.__objc_arraydata: 0xf30
-  __DATA_CONST.__got: 0x14c8
-  __AUTH_CONST.__const: 0xbcd0
-  __AUTH_CONST.__cfstring: 0xff80
-  __AUTH_CONST.__objc_const: 0x19590
+  __DATA_CONST.__got: 0x14a0
+  __AUTH_CONST.__const: 0xbbe0
+  __AUTH_CONST.__cfstring: 0xfd60
+  __AUTH_CONST.__objc_const: 0x18b98
   __AUTH_CONST.__weak_auth_got: 0x30
-  __AUTH_CONST.__objc_intobj: 0x5e8
+  __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1880
+  __AUTH_CONST.__auth_got: 0x1830
   __AUTH.__objc_data: 0x1fe0
   __AUTH.__data: 0x18
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x20
-  __DATA.__objc_ivar: 0x11d0
+  __DATA.__objc_ivar: 0x1190
   __DATA.__data: 0x21c0
   __DATA.__common: 0x408
-  __DATA_DIRTY.__objc_data: 0x3110
+  __DATA_DIRTY.__objc_data: 0x2df0
   __DATA_DIRTY.__data: 0xb0
-  __DATA_DIRTY.__bss: 0xaa8
+  __DATA_DIRTY.__bss: 0xa90
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libmecabra.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 10173
-  Symbols:   20476
-  CStrings:  3197
+  Functions: 10068
+  Symbols:   20210
+  CStrings:  3158
 
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
+ OBJC_IVAR_$_TIMecabraEnvironmentContextWrapper._stringContext
+ OBJC_IVAR_$_TITextCheckerExemptionsImpl._contactDeltaObserver
+ TIInputManagerServerOSLogFacility.logFacility
+ TIInputManagerServerOSLogFacility.onceToken
+ _MecabraContextSetStringContext
+ _OBJC_CLASS_$_NSCountedSet
+ _TIInputManagerServerOSLogFacility
+ __OBJC_$_CLASS_METHODS_TITextCheckerExemptions(TestingSupport)
+ __ZL20nameTokensForContactP10_ICContact
+ ___52+[TIChineseExtras stringContainsOffensiveCharacter:]_block_invoke
+ ___TIInputManagerServerOSLogFacility_block_invoke
+ ____ZN17AppTrieLoaderImpl20perform_initial_loadEv_block_invoke
+ ____ZZN17AppTrieLoaderImpl20perform_initial_loadEvENK3$_0clEv_block_invoke
+ ___block_descriptor_40_a8_32s_e34_v24?0"NSArray"8"NSDictionary"16l
+ ___block_descriptor_56_a8_32c55_ZTSKZN17AppTrieLoaderImpl20perform_initial_loadEvE3$_0_e5_v8?0l
+ ___block_descriptor_56_a8_32c68_ZTSKZZN17AppTrieLoaderImpl20perform_initial_loadEvENK3$_0clEvEUlvE__e5_v8?0l
+ ___copy_helper_block_a8_32c55_ZTSKZN17AppTrieLoaderImpl20perform_initial_loadEvE3$_0
+ ___copy_helper_block_a8_32c68_ZTSKZZN17AppTrieLoaderImpl20perform_initial_loadEvENK3$_0clEvEUlvE_
+ ___destroy_helper_block_a8_32c55_ZTSKZN17AppTrieLoaderImpl20perform_initial_loadEvE3$_0
+ ___destroy_helper_block_a8_32c68_ZTSKZZN17AppTrieLoaderImpl20perform_initial_loadEvENK3$_0clEvEUlvE_
+ _malloc_zone_pressure_relief
+ _objc_msgSend$_resetForTesting
+ _objc_msgSend$applyContactDeltaChanges:
+ _objc_msgSend$currentLoadedInputModes
+ _objc_msgSend$dropResourcesExcludingInputModes:
+ _objc_msgSend$leftDocumentContextForCandidates
+ _objc_msgSend$rebuildAddressBookTokensFromSnapshot:
+ _objc_msgSend$releaseAllInputManagersAndLanguageModelResources
+ _objc_msgSend$setStringContext:
+ _objc_msgSend$stringContext
+ _objc_msgSend$stringContextIsEmpty
+ stringContainsOffensiveCharacter:.offensiveCharacterSet
+ stringContainsOffensiveCharacter:.onceToken
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
- OBJC_IVAR_$_HCBurstTrie._burstTrie
- OBJC_IVAR_$_HCBurstTrie._keysAdded
- OBJC_IVAR_$_HCHuffmanCoder._burstTrie
- OBJC_IVAR_$_HCHuffmanCoder._indexTable
- OBJC_IVAR_$_HCIndexTable._fileHeader
- OBJC_IVAR_$_HCIndexTable._huffmanCodesMemoryMappedData
- OBJC_IVAR_$_HCIndexTable._mutableHuffmanCodes
- OBJC_IVAR_$_HCIndexTable._versionUUID
- OBJC_IVAR_$_TIDPNgramRecorder._shouldDonateNgramSampleRandomly
- OBJC_IVAR_$_TIDPNgramRecorderCascading._n
- OBJC_IVAR_$_TIDPNgramWordEntryPair._wordEntryAligned
- OBJC_IVAR_$_TIDPNgramWordEntryPair._wordString
- OBJC_IVAR_$_TIDPRecorder._characterCoder
- OBJC_IVAR_$_TIDPRecorder._wordCoder
- OBJC_IVAR_$_TIDPWordRecord._coder
- OBJC_IVAR_$_TILaunchServicesLookup._cache
- OBJC_IVAR_$_TILaunchServicesLookup._lastCacheUpdate
- OBJC_IVAR_$_TITextCheckerExemptionsImpl._contactObserver
- _CFBurstTrieContains
- _CFBurstTrieCreate
- _CFBurstTrieCreateFromMapBytes
- _CFBurstTrieGetCount
- _CFBurstTrieRelease
- _CFBurstTrieSerializeWithFileDescriptor
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
- _ZZ23-[HCIndexTable isValid]E12staticHeader
- _ZZL21libmecabraLibraryCorePPcE16frameworkLibrary
- _ZZL42getMecabraContextSetStringContextSymbolLocvE3ptr
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
- ___28-[TIDPNgramRecorder records]_block_invoke
- ___40+[TILaunchServicesLookup sharedInstance]_block_invoke
- ___40-[TIDPRecorder characterExplodedRecords]_block_invoke
- ___43+[HCHuffmanCoder coderMatchingName:locale:]_block_invoke
- ___46-[TIDPUnknownTokenWithContextRecorder records]_block_invoke
- ___46-[TIDPUnknownTokenWithContextRecorder records]_block_invoke_2
- ___ZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1__block_invoke
- ____ZL21libmecabraLibraryCorePPc_block_invoke
- ____ZL27background_append_app_namesN2KB10retain_ptrIP10_LXLexiconEERKNS_16StaticDictionaryE_block_invoke
- ____ZL42getMecabraContextSetStringContextSymbolLocv_block_invoke
- ____ZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1__block_invoke
- ____ZZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_ENK3$_0clEv_block_invoke
- ___block_descriptor_144_a8_32c42_ZTSNSt3__18weak_ptrI17AppTrieLoaderImplEE48c17_ZTSKN2KB6StringE80c17_ZTSKN2KB6StringE112c17_ZTSKN2KB6StringE_e22_v16?0"NSDictionary"8l
- ___block_descriptor_152_a8_32c85_ZTSKZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_E3$_0_e5_v8?0l
- ___block_descriptor_152_a8_32c98_ZTSKZZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_ENK3$_0clEvEUlvE__e5_v8?0l
- ___block_descriptor_32_e35_B32?0"TIWordEntryAligned"8Q16^B24l
- ___block_descriptor_40_8_32r_e57_v44?0^{__CFURL=}8i16^{__CFLocale=}20^{__CFString=}28^B36l
- ___block_descriptor_48_8_32s40s_e21_v24?0"NSArray"8^B16l
- ___block_descriptor_48_a8_32c36_ZTSN2KB10retain_ptrIP10_LXLexiconEE_e22_v24?0"NSString"8^B16l
- ___block_descriptor_48_a8_32r_e5_v8?0l
- ___block_descriptor_56_8_32s40s48r_e52_v56?0"NSString"8{_NSRange=QQ}16{_NSRange=QQ}32^B48l
- ___copy_helper_block_a8_32c36_ZTSN2KB10retain_ptrIP10_LXLexiconEE
- ___copy_helper_block_a8_32c42_ZTSNSt3__18weak_ptrI17AppTrieLoaderImplEE48c17_ZTSKN2KB6StringE80c17_ZTSKN2KB6StringE112c17_ZTSKN2KB6StringE
- ___copy_helper_block_a8_32c85_ZTSKZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_E3$_0
- ___copy_helper_block_a8_32c98_ZTSKZZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_ENK3$_0clEvEUlvE_
- ___destroy_helper_block_a8_32c36_ZTSN2KB10retain_ptrIP10_LXLexiconEE
- ___destroy_helper_block_a8_32c42_ZTSNSt3__18weak_ptrI17AppTrieLoaderImplEE48c17_ZTSKN2KB6StringE80c17_ZTSKN2KB6StringE112c17_ZTSKN2KB6StringE
- ___destroy_helper_block_a8_32c85_ZTSKZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_E3$_0
- ___destroy_helper_block_a8_32c98_ZTSKZZZN17AppTrieLoaderImpl28register_as_contact_observerEN2KB6StringES1_S1_EUb_ENK3$_0clEvEUlvE_
- _dlerror
- _dlsym
- _fileno
- _log2
- _objc_msgSend$_createUnderlyingBurstTrie
- _objc_msgSend$_normalizedWordEntryStringForWordEntry:
- _objc_msgSend$_prepareCharacterCoderMatchingSession
- _objc_msgSend$_prepareWordCoderMatchingSession
- _objc_msgSend$appNames
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
- _objc_msgSend$isFromStaticLexicon
- _objc_msgSend$isStandaloneString
- _objc_msgSend$lastCacheUpdate
- _objc_msgSend$lookupAppNames
- _objc_msgSend$n
- _objc_msgSend$numberWithLongLong:
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
- sharedInstance.instance
CStrings:
+ "%s  kbd is %zu bytes over the inactive limit, hard-resetting all language models (including advanced ones)"
+ "%s  kbd is still %zu bytes over the inactive limit, releasing all cached input managers and language model resources"
+ "%s TITextCheckerExemptions:applyContactDeltaChanges - applying %lu delta records"
+ "%s TITextCheckerExemptions:rebuildAddressBookTokensFromSnapshot - rebuilding from snapshot of %lu contacts"
+ "%s perform_initial_load perf: %.3f ms"
+ "-[TITextCheckerExemptionsImpl applyContactDeltaChanges:]"
+ "-[TITextCheckerExemptionsImpl rebuildAddressBookTokensFromSnapshot:]"
+ "KBDInputManagerServer"
+ "perform_initial_load"
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
- "%s AppName=%@"
- "%s Failed to open app filtering dictionary at %s"
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
- "/usr/lib/libmecabra.dylib"
- "/usr/local/lib/libmecabra.dylib"
- "2"
- "B32@?0@\"TIWordEntryAligned\"8Q16^B24"
- "DifferentialPrivacyHuffmanCoder"
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
- "v24@?0@\"NSArray\"8^B16"
- "wb+"
- "words"
- "~AppTrieLoaderImpl"
```
