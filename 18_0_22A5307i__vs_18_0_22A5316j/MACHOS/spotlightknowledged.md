## spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

-2310.1.0.4.0
-  __TEXT.__text: 0x7a824
-  __TEXT.__auth_stubs: 0x1980
-  __TEXT.__objc_stubs: 0x8200
-  __TEXT.__objc_methlist: 0x446c
-  __TEXT.__const: 0x638
-  __TEXT.__cstring: 0x4680
-  __TEXT.__oslogstring: 0x2638
-  __TEXT.__gcc_except_tab: 0x3d48
-  __TEXT.__objc_classname: 0x726
-  __TEXT.__objc_methname: 0x9437
-  __TEXT.__objc_methtype: 0xd28
+2312.1.0.2.0
+  __TEXT.__text: 0x7b75c
+  __TEXT.__auth_stubs: 0x1a70
+  __TEXT.__objc_stubs: 0x82c0
+  __TEXT.__objc_methlist: 0x4350
+  __TEXT.__const: 0x640
+  __TEXT.__cstring: 0x47fe
+  __TEXT.__oslogstring: 0x27c3
+  __TEXT.__gcc_except_tab: 0x3ca8
+  __TEXT.__objc_classname: 0x708
+  __TEXT.__objc_methname: 0x972c
+  __TEXT.__objc_methtype: 0xe61
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x2068
-  __DATA_CONST.__auth_got: 0xcd8
-  __DATA_CONST.__got: 0x5b8
-  __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x3308
-  __DATA_CONST.__cfstring: 0x6aa0
-  __DATA_CONST.__objc_classlist: 0x348
+  __TEXT.__unwind_info: 0x20b0
+  __DATA_CONST.__auth_got: 0xd50
+  __DATA_CONST.__got: 0x5d0
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x3310
+  __DATA_CONST.__cfstring: 0x69a0
+  __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x5c0
+  __DATA_CONST.__objc_superrefs: 0x1f8
+  __DATA_CONST.__objc_arraydata: 0x580
   __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA_CONST.__objc_dictobj: 0xf0
+  __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__objc_intobj: 0x2b8
-  __DATA.__objc_const: 0x80f0
-  __DATA.__objc_selrefs: 0x2668
-  __DATA.__objc_ivar: 0x4b4
-  __DATA.__objc_data: 0x20d0
+  __DATA_CONST.__objc_intobj: 0x2e8
+  __DATA.__objc_const: 0x7be0
+  __DATA.__objc_selrefs: 0x26f0
+  __DATA.__objc_ivar: 0x4cc
+  __DATA.__objc_data: 0x2030
   __DATA.__data: 0x520
-  __DATA.__bss: 0xaa8
+  __DATA.__bss: 0xab8
   __DATA.__common: 0x30008
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2421
-  Symbols:   590
-  CStrings:  3235
+  Functions: 2408
+  Symbols:   608
+  CStrings:  3287
 
Symbols:
+ _CFCalendarCreateWithIdentifier
+ _CFCalendarDecomposeAbsoluteTime
+ _CFCalendarSetTimeZone
+ _CFDictionaryGetValue
+ _CFLocaleGetIdentifier
+ _CFLocaleGetSystem
+ _CFStringGetCString
+ _CFTimeZoneCopySystem
+ __CFCopySystemVersionDictionary
+ __CFPrefsSetDirectModeEnabled
+ __CFPrefsSetReadOnly
+ ___strlcpy_chk
+ __kCFSystemVersionBuildVersionKey
+ _db_delete_datastore
+ _fd_lseek
+ _fd_release
+ _fd_write
+ _fd_zero_truncate
+ _fprintf
+ _kCFAllocatorSystemDefault
+ _kCFGregorianCalendar
+ _objc_setProperty_atomic
+ _sandbox_free_error
+ _sandbox_init
- _CFStringCreateWithCharacters
- _CFStringGetCStringPtr
- _CFStringGetCharacters
- _CFStringGetCharactersPtr
- _CFStringGetRangeOfComposedCharactersAtIndex
- _objc_retain_x7
CStrings:
+ "\x05A\x11"
+ "### completing background task early %!@(MISSING)"
+ "### file open failed"
+ "### mmap failed"
+ "### unknown type %!d(MISSING) at offset %!l(MISSING)d\n"
+ "%!d(MISSING)-%!d(MISSING)-%!d(MISSING) %!d(MISSING):%!d(MISSING):%!d(MISSING)"
+ "%!s(MISSING) pid: %!d(MISSING) time: %!s(MISSING)sbuild: %!s(MISSING)\n"
+ "%!s(MISSING):%!s(MISSING)"
+ "(_kMDItemUpdaterVersion!=* || _kMDItemUpdaterVersion!=%!l(MISSING)d)"
+ "/usr/share/sandbox/com.apple.spotlightknowledged.importer.sb"
+ "3\x13\x14"
+ "@\"NSString\"8@?0"
+ "@32@0:8^{fd_obj=}16q24"
+ "@48@0:8r*16r*24r*32Q40"
+ "B44@0:8i16r*20Q28@36"
+ "B56@0:8@16@24@?32@?40@?48"
+ "B56@0:8r*16r*24r*32Q40r*48"
+ "B96@0:8@16@24@32@40Q48^q56@?64@?72@?80@?88"
+ "Defaults"
+ "Embedding"
+ "EnableSemanticSearch"
+ "Init"
+ "Journal was reset at time %!s(MISSING), size before reset: %!l(MISSING)lu, size after reset: %!l(MISSING)lu\n"
+ "Language"
+ "Received item - bundle: %!s(MISSING) identifier: %!s(MISSING)\n"
+ "SKGActivityJournal"
+ "SKGActivityJournalPlayback:block:"
+ "SKGUpdaterStore#readLanguageFromBundleID illegal language to bundleID: %!s(MISSING), identifier: %!s(MISSING)"
+ "SKGUpdaterStore#writeLanguageForBundleID failed to add field %!@(MISSING) with rc: %!d(MISSING)"
+ "SKGUpdaterStore#writeLanguageForBundleID failed to store object err: %!d(MISSING)"
+ "SKGUpdaterStore#writeLanguageForBundleID language %!s(MISSING) is too long"
+ "SKGUpdaterStore[%!@(MISSING)]#purgeAllWithUUID deleted %!l(MISSING)ld dbos"
+ "SKGUpdaterStore[%!@(MISSING)]#purgeAllWithUUID failed to delete dbo with rc: %!d(MISSING)"
+ "SKGUpdaterStore[%!@(MISSING)]#purgeAllWithUUID failed to get dbo with rc: %!d(MISSING)"
+ "Sandbox initialization failed, error:%!s(MISSING)\n"
+ "SupportedLanguages"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_clientCheckInQueue"
+ "T@\"SKGSystemListener\",R,N"
+ "TB,N,V_force"
+ "TB,N,V_started"
+ "T^{fd_obj=},N,V_fd"
+ "Test %!s(MISSING)\n"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "^{fd_obj=}"
+ "^{fd_obj=}16@0:8"
+ "_SKGActivityDump:dst:"
+ "_clientCheckInQueue"
+ "_fd"
+ "_force"
+ "_initWithName:protectionClass:bundleIdentifier:options:"
+ "_kMDItemPrioritySN"
+ "_locked_doNotUpdateList"
+ "_locked_hasDiskCapacity"
+ "_locked_lastDiskFlushDate"
+ "_locked_semanticSearchEnabled"
+ "_locked_supportedSemanticLanguages"
+ "addReceiveEvent:identifier:"
+ "addTestEvent:"
+ "canProcessEvent:"
+ "canProcessRecord:"
+ "clientCheckInQueue"
+ "closeAndDeleteStore"
+ "com.apple.private.corespotlight.sender.importer"
+ "com.apple.spotlightknowledged.client-check-in"
+ "defaults.plist"
+ "en-US"
+ "enumerateItems:"
+ "enumerateProcessedItemsFromRecord:referenceIdentifier:bundleIdentifier:protectionClass:processorFlags:workCost:fetchCachedLanguageBlock:cacheLanguageBlock:processedItemBlock:cancelBlock:"
+ "fd"
+ "force"
+ "generateKeyphrasesForRecord:processedItem:fetchCachedLanguageBlock:cacheLanguageBlock:cancelBlock:"
+ "hasDiskCapacity"
+ "initWithArray:"
+ "initWithFd:limit:"
+ "initWithLocaleIdentifier:"
+ "kSKGActivityJournalReset: Journal size %!l(MISSING)ld is > %!l(MISSING)ld\n"
+ "main"
+ "processLanguageOfTextContentFromRecord:processedItem:fetchCachedLanguageBlock:cacheLanguageBlock:cancelBlock:"
+ "readLanguageFromBundleID:identifier:UUID:serialNumber:"
+ "root"
+ "rootLocale"
+ "runWithJobContext:queue:group:delegate:deferBlock:completeBlock:cancelBlock:"
+ "semanticSearchEnabled"
+ "setClientCheckInQueue:"
+ "setFd:"
+ "setForce:"
+ "setLock:"
+ "setStarted:"
+ "spotlightknowledged.m"
+ "supportedSemanticLanguages"
+ "updateDefaultWithKey:value:"
+ "updateLocaleWithLocale:preferredLanguages:force:"
+ "updateResources"
+ "v16@?0@\"NSString\"8"
+ "v16@?0r^{skg_playback_info=I(?={?=Id*}{?=dqq}{?=*}{?=**})}8"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v24@0:8^{fd_obj=}16"
+ "v32@0:8I16^v20I28"
+ "v32@0:8r*16@?24"
+ "v32@0:8r*16^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24"
+ "writeEvent:data:dataSize:"
+ "writeInit"
+ "writeLanguageForBundleID:identifier:UUID:serialNumber:language:"
+ "writeUpdaterProgressToStoreWithIndexType:UUID:serialNumber:error:"
+ "yMdHms"
+ "{os_unfair_lock_s=I}16@0:8"
- "\x06AQ"
- "\x13\x15"
- "%!@(MISSING)-%!@(MISSING)_%!@(MISSING)"
- "%!l(MISSING)u:=:%!@(MISSING)"
- "((_kMDItemUpdaterVersion!=* || _kMDItemUpdaterVersion!=%!l(MISSING)d) && %!@(MISSING) && %!@(MISSING))"
- "(true)"
- "001"
- ":=:"
- "B48@0:8@16r*24Q32@40"
- "B80@0:8@16@24@32@40Q48^q56@?64@?72"
- "CSSnippetUpdater"
- "CSSummariesUpdater"
- "CSTestUpdater"
- "Hans"
- "SKG: available capacity: %!@(MISSING)"
- "SKG: checking disk capacity"
- "SKGUpdaterStore#purgeAllWithUUID deleted %!l(MISSING)ld dbos"
- "SKGUpdaterStore#purgeAllWithUUID failed to delete dbo with rc: %!d(MISSING)"
- "SKGUpdaterStore#purgeAllWithUUID failed to get dbo with rc: %!d(MISSING)"
- "SnippetUpdate"
- "SpotlightEmbedding"
- "SummariesUpdate"
- "TestUpdate"
- "Tq,N,V_minDiskCapacity"
- "_kMDItemSnippetUpdate"
- "_kMDItemSummariesSN"
- "_kMDItemTestSN"
- "_minDiskCapacity"
- "_semanticSearchLanguages"
- "autoupdatingCurrentLocale"
- "canProcess"
- "com.apple.spotlight.SpotlightKnowledge.Processor"
- "enumerateProcessedItemsFromRecord:referenceIdentifier:bundleIdentifier:protectionClass:processorFlags:workCost:processedItemBlock:cancelBlock:"
- "generateKeyphrasesForRecord:processedItem:cancelBlock:"
- "knowledgeCompletedWithFeedback:"
- "languageCode"
- "languageIdentifier"
- "loadAllParametersForClient:"
- "loadLocale:preferredLanguages:"
- "minDiskCapacity"
- "not enough capacity"
- "preferredLanguages"
- "processLanguageOfTextContentFromRecord:processedItem:cancelBlock:"
- "processorQueue"
- "resourcesForClient:options:"
- "runWithJobContext:group:delegate:deferBlock:completeBlock:cancelBlock:"
- "scriptCode"
- "semanticSearchLanguages"
- "semanticSearchSupportedLanguages"
- "setMinDiskCapacity:"
- "setPreferredLanguages:currentLocale:"
- "snippets"
- "summaries"
- "updateLocaleWithLocale:preferredLanguages:"
- "v64@0:8@16@24@32@?40@?48@?56"
- "writeUpdaterProgressToStore:UUID:serialNumber:error:"

```
