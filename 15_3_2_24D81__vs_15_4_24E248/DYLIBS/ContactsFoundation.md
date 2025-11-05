## ContactsFoundation

> `/System/Library/PrivateFrameworks/ContactsFoundation.framework/Versions/A/ContactsFoundation`

```diff

-1368.400.1.0.0
-  __TEXT.__text: 0x8d258
-  __TEXT.__auth_stubs: 0x17d0
-  __TEXT.__objc_methlist: 0x96ec
-  __TEXT.__cstring: 0x6c08
+1368.500.71.0.0
+  __TEXT.__text: 0x8ccd0
+  __TEXT.__auth_stubs: 0x17b0
+  __TEXT.__objc_methlist: 0xa4fc
+  __TEXT.__cstring: 0x6988
   __TEXT.__const: 0x508
   __TEXT.__oslogstring: 0x1f6b
   __TEXT.__gcc_except_tab: 0x1264

   __TEXT.__swift5_fieldmd: 0x18c
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x24
-  __TEXT.__unwind_info: 0x3288
+  __TEXT.__unwind_info: 0x3338
   __TEXT.__eh_frame: 0x158
   __TEXT.__objc_classname: 0x2533
-  __TEXT.__objc_methname: 0x12017
+  __TEXT.__objc_methname: 0x12068
   __TEXT.__objc_methtype: 0x2ec1
-  __TEXT.__objc_stubs: 0xce00
-  __DATA_CONST.__got: 0xd90
-  __DATA_CONST.__const: 0x1010
+  __TEXT.__objc_stubs: 0xce60
+  __DATA_CONST.__got: 0xda0
+  __DATA_CONST.__const: 0x1030
   __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4800
+  __DATA_CONST.__objc_selrefs: 0x4910
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x9c88
-  __AUTH_CONST.__auth_got: 0xbf8
-  __AUTH_CONST.__const: 0x4b58
+  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH_CONST.__const: 0x4b78
   __AUTH_CONST.__cfstring: 0xa640
-  __AUTH_CONST.__objc_const: 0x17008
+  __AUTH_CONST.__objc_const: 0x157b8
   __AUTH_CONST.__objc_dictobj: 0x2580
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x1de0
+  __AUTH.__objc_data: 0x1d90
   __AUTH.__data: 0x238
   __DATA.__objc_ivar: 0x7ac
-  __DATA.__data: 0x18c8
+  __DATA.__data: 0x18a8
   __DATA.__bss: 0x800
-  __DATA.__common: 0x38
+  __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x4ce0
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x270

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 977E4DB4-997B-37EE-B749-F746E1707EF3
-  Functions: 4443
-  Symbols:   10604
-  CStrings:  7053
+  UUID: E6EC0824-F187-32B4-9664-2BEEE80D512B
+  Functions: 4522
+  Symbols:   10726
+  CStrings:  7040
 
Symbols:
+ +[CNArchiver os_log].cold.1
+ +[CNAuditTokenUtilities os_log].cold.1
+ +[CNAuthorizationContext os_log].cold.1
+ +[CNAuthorizationContext sharedInstance].cold.1
+ +[CNBlockCountingSchedulerDecorator os_log].cold.1
+ +[CNCallStackRecordingSchedulerDecorator os_log].cold.1
+ +[CNChildDelegateAccountsStore os_log].cold.1
+ +[CNCoalescingTimer os_log].cold.1
+ +[CNDate gmtBuddhistCalendar].cold.1
+ +[CNDate gmtChineseCalendar].cold.1
+ +[CNDate gmtGregorianCalendar].cold.1
+ +[CNDate gmtIslamicCalendar].cold.1
+ +[CNDate gmtJapaneseCalendar].cold.1
+ +[CNDateComponentsFormatter os_log].cold.1
+ +[CNDateHelper gregorianCalendarInGMT].cold.1
+ +[CNDateHelper gregorianCalendar].cold.1
+ +[CNEither eitherWithLeft:].cold.2
+ +[CNEither eitherWithRight:].cold.2
+ +[CNEither firstLeftInLazyChain:].cold.2
+ +[CNEncryptionHelper os_log].cold.1
+ +[CNEnvironment os_log].cold.1
+ +[CNEnvironmentBase defaultStack].cold.1
+ +[CNFamilyCircleConfigurationUpdateTask os_log].cold.1
+ +[CNFeatureFlags currentFlags].cold.1
+ +[CNFileServices sharedInstance].cold.1
+ +[CNFileServices tmpDirLog].cold.1
+ +[CNFileUtilities fileLock].cold.1
+ +[CNFileUtilities os_log].cold.1
+ +[CNFileUtilities sharedInstance].cold.1
+ +[CNFoundationUserDefaults sharedDefaults].cold.1
+ +[CNLogging apiUsageLog].cold.1
+ +[CNLogging notificationOSLog].cold.1
+ +[CNLogging sdkBreakageLog].cold.1
+ +[CNManagedConfiguration os_log].cold.1
+ +[CNMultiDictionary multiDictionary].cold.1
+ +[CNObservable emptyObservable].cold.1
+ +[CNObservable neverObservable].cold.1
+ +[CNObservable os_log].cold.1
+ +[CNObservable os_log_protocol].cold.1
+ +[CNObservableContractEnforcement os_log].cold.1
+ +[CNObservableEvent completionEvent].cold.1
+ +[CNProcessSharedLock os_log].cold.1
+ +[CNRegulatoryLogger sharedInstanceForAddressBook].cold.1
+ +[CNScheduler globalAsyncScheduler].cold.1
+ +[CNScheduler immediateScheduler].cold.1
+ +[CNScheduler inlineScheduler].cold.1
+ +[CNScheduler mainThreadScheduler].cold.1
+ +[CNScheduler offMainThreadScheduler].cold.1
+ +[CNSimulatedCrashReporter os_log].cold.1
+ +[CNSimulatedCrashReporter simulateCrashWithCode:description:].cold.3
+ +[CNSocialProfileURLParser servicesDictionary].cold.1
+ +[CNStringTokenizer isCharacterNonBreaking:].cold.1
+ +[CNTCCVersion2 os_log].cold.1
+ +[CNTimeIntervalFormatter sharedFormatter].cold.1
+ +[CNTimeProfilingSchedulerDecorator os_log].cold.1
+ +[CNURLSessionFactory defaultFactory].cold.1
+ +[NSString(ContactsFoundationPhoneNumbers) _cn_LTRControlCharacters].cold.1
+ +[NSString(ContactsFoundationPhoneNumbers) _cn_whitespaceExceptAscii32CharacterSet].cold.1
+ +[NSTermOfAddress(ContactsFoundation) os_log].cold.1
+ +[_CNBlockFutureImpl log].cold.1
+ +[_CNOffMainThreadScheduler os_log].cold.1
+ +[_CNRunningBoardInhibitor os_log].cold.1
+ +[_CNRunningBoardInhibitor runningBoardTarget].cold.1
+ -[CNCancelationToken addCancelable:].cold.2
+ -[CNEntitlementVerifier highPriorityBundleIdentifiers].cold.1
+ -[CNHandleStringClassifier initWithClassificationStrategy:].cold.2
+ -[CNNameComponentsStringTokenizer initWithString:].cold.2
+ -[CNPair initWithFirst:second:].cold.1
+ -[CNPair initWithFirst:second:].cold.2
+ -[CNTCCVersion1 checkAuthorizationStatusOfCurrentProcess].cold.1
+ -[CNTask initWithName:].cold.2
+ -[CNVirtualFileManager asyncDataWithContentsOfURL:].cold.2
+ -[CNVirtualFileManager asyncWriteData:toURL:options:].cold.2
+ -[CNVirtualFileManager dataWithContentsOfURL:].cold.2
+ -[CNVirtualFileManager fileExistsAtURL:].cold.2
+ -[CNVirtualFileManager fileExistsAtURL:isDirectory:].cold.2
+ -[CNVirtualFileManager observableWithContentsOfURL:].cold.2
+ -[CNVirtualFileManager writeData:toURL:options:].cold.2
+ -[NSString(ContactsFoundation) _cn_containsOnlyDigits]
+ -[_CNBlockTask initWithName:block:].cold.2
+ -[_CNOffMainThreadScheduler initWithBackgroundScheduler:].cold.2
+ -[_CNRunningBoardInhibitor start].cold.2
+ -[_CNTimeProfilingTask initWithTask:timeProvider:logger:].cold.4
+ -[_CNTimeProfilingTask initWithTask:timeProvider:logger:].cold.5
+ -[_CNTimeProfilingTask initWithTask:timeProvider:logger:].cold.6
+ -[_GreenTeaPostalAddressLocalizer localizedStringForPostalAddressString:returningNilIfNotFound:].cold.1
+ -[_GreenTeaPostalAddressLocalizer localizedStringForPostalAddressString:returningNilIfNotFound:].cold.2
+ -[_StandardPostalAddressLocalizer localizedStringForPostalAddressString:returningNilIfNotFound:].cold.1
+ CNContactsFoundationBundle.cold.1
+ CNGetICUCollatorVersions.cold.1
+ CNIsArabicString.cold.1
+ CNIsChineseJapaneseKoreanString.cold.1
+ CNIsChineseString.cold.1
+ CNNameDelimiterForString.cold.1
+ CNSocialProfileStandardServices.cold.1
+ CNStringContainsChineseJapaneseKoreanCharacters.cold.1
+ CNStringContainsEmojiCharacters.cold.1
+ CNStringContainsKoreanCharacters.cold.1
+ CNStringContainsNonLatinCharacters.cold.1
+ DarwinObservers.cold.1
+ _ACAccountDataclassContacts
+ _ACAccountDataclassContactsSearch
+ __CNEmojiCharacterSet_block_invoke.cold.1
+ ___49-[_CNACAccountStoreBasedProvider allAccountTypes]_block_invoke
+ ___block_descriptor_32_e23_B16?0"ACAccountType"8l
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ __block_literal_global.124
+ __block_literal_global.126
+ __block_literal_global.129
+ __block_literal_global.131
+ __block_literal_global.133
+ __block_literal_global.136
+ __block_literal_global.138
+ __block_literal_global.29
+ __softLinkSimulateCrashAvailable_block_invoke.cold.1
+ _objc_msgSend$decimalDigitCharacterSet
+ _objc_msgSend$invertedSet
+ _objc_msgSend$supportedDataclasses
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain_n
+ initACAccountStore.cold.1
+ initCEMEnumerateEmojiTokensInStringWithBlock.cold.1
+ initCTFontCopyCharacterSet.cold.1
+ initCTFontCreateWithName.cold.1
+ initDiagnosticLogSubmissionEnabled.cold.1
+ initFAFetchFamilyCircleRequest.cold.1
+ initIntlUtility.cold.1
+ initNSPersonNameComponentsFormatterPreferences.cold.1
+ initSimulateCrash.cold.1
- ___swift_destroy_boxed_opaque_existential_1
- __block_literal_global.123
- __block_literal_global.125
- __block_literal_global.128
- __block_literal_global.130
- __block_literal_global.132
- __block_literal_global.135
- __block_literal_global.137
- __block_literal_global.70
CStrings:
+ "_cn_containsOnlyDigits"
+ "decimalDigitCharacterSet"
+ "invertedSet"
+ "supportedDataclasses"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
