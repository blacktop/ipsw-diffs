## spotlightknowledged

> `/System/Library/Frameworks/CoreSpotlight.framework/spotlightknowledged`

```diff

-2312.1.0.4.0
-  __TEXT.__text: 0x7b75c
-  __TEXT.__auth_stubs: 0x1a70
-  __TEXT.__objc_stubs: 0x82c0
-  __TEXT.__objc_methlist: 0x4350
-  __TEXT.__const: 0x640
-  __TEXT.__cstring: 0x47fe
-  __TEXT.__oslogstring: 0x27c3
-  __TEXT.__gcc_except_tab: 0x3ca8
-  __TEXT.__objc_classname: 0x708
-  __TEXT.__objc_methname: 0x972c
-  __TEXT.__objc_methtype: 0xe61
+2314.2.0.0.0
+  __TEXT.__text: 0x7fad8
+  __TEXT.__auth_stubs: 0x1be0
+  __TEXT.__objc_stubs: 0x84c0
+  __TEXT.__objc_methlist: 0x4400
+  __TEXT.__const: 0x660
+  __TEXT.__cstring: 0x4d22
+  __TEXT.__oslogstring: 0x2ae3
+  __TEXT.__gcc_except_tab: 0x3cbc
+  __TEXT.__objc_classname: 0x710
+  __TEXT.__objc_methname: 0x99e5
+  __TEXT.__objc_methtype: 0xec9
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x20b0
-  __DATA_CONST.__auth_got: 0xd50
+  __TEXT.__unwind_info: 0x2160
+  __DATA_CONST.__auth_got: 0xe08
   __DATA_CONST.__got: 0x5d0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x3310
-  __DATA_CONST.__cfstring: 0x69a0
+  __DATA_CONST.__const: 0x3500
+  __DATA_CONST.__cfstring: 0x6be0
   __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1f8
-  __DATA_CONST.__objc_arraydata: 0x580
-  __DATA_CONST.__objc_arrayobj: 0x360
-  __DATA_CONST.__objc_dictobj: 0xa0
+  __DATA_CONST.__objc_arraydata: 0x5c8
+  __DATA_CONST.__objc_arrayobj: 0x390
+  __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__objc_intobj: 0x2e8
-  __DATA.__objc_const: 0x7be0
-  __DATA.__objc_selrefs: 0x26f0
-  __DATA.__objc_ivar: 0x4cc
+  __DATA_CONST.__objc_intobj: 0x318
+  __DATA.__objc_const: 0x7c80
+  __DATA.__objc_selrefs: 0x2750
+  __DATA.__objc_ivar: 0x4d4
   __DATA.__objc_data: 0x2030
-  __DATA.__data: 0x520
-  __DATA.__bss: 0xab8
-  __DATA.__common: 0x30008
+  __DATA.__data: 0x560
+  __DATA.__bss: 0xae8
+  __DATA.__common: 0x30010
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2408
-  Symbols:   608
-  CStrings:  3287
+  Functions: 2479
+  Symbols:   631
+  CStrings:  3364
 
Symbols:
+ _CFRunLoopGetMain
+ __MDPlistContainerValidateRootObjectFromBytes
+ _chmod
+ _chown
+ _faccessat
+ _fchownat
+ _fd_create_protected
+ _fsgetpath
+ _fstatat
+ _ftruncate
+ _getattrlist
+ _getattrlistat
+ _getattrlistbulk
+ _geteuid
+ _linkat
+ _mkdir
+ _mkdirat
+ _pthread_fchdir_np
+ _pthread_getugid_np
+ _pthread_setugid_np
+ _renameatx_np
+ _renamex_np
+ _sprintf
+ _statfs
+ _strchr
+ _strlcat
+ _strlcpy
- _OSAtomicAdd64
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
CStrings:
+ "### SKGActivityJournal#initWithParentPath Error %!@(MISSING) creating %!@(MISSING)"
+ "### SKGActivityJournal#initWithParentPath error opening errno %!d(MISSING) creating %!@(MISSING)"
+ "### Unable to warmup %!@(MISSING) - %!s(MISSING), will retry later"
+ "### ignored journal - already active - %!@(MISSING)"
+ "### ignored journal - failed retainTocFd - %!@(MISSING)"
+ "### timeout %!@(MISSING) for %!@(MISSING), continuing to wait"
+ "### timeout openning journal file (%!@(MISSING)) from searchd, continuing to wait"
+ "%!@(MISSING) || _kMDItemNeedsEmbeddings=1 || (%!@(MISSING)=*&&%!@(MISSING)=%!l(MISSING)d) || (kMDItemEmbeddingVersion=*&&kMDItemEmbeddingVersion=%!l(MISSING)d)"
+ "%!s(MISSING) for item - bundle: %!s(MISSING) identifier: %!s(MISSING) oid: 0x%!l(MISSING)lx\n"
+ "(_kMDItemIsZombie!=* || _kMDItemIsZombie!=1)"
+ "(_kMDItemKnowledgeIndexVersion!=* || (_kMDItemKnowledgeIndexVersion=*&&_kMDItemKnowledgeIndexVersion!=%!l(MISSING)d))"
+ "(_kMDItemKnowledgeUpdaterVersion=*&&_kMDItemKnowledgeUpdaterVersion!=%!l(MISSING)d)"
+ "(_kMDItemMediaEmbeddingVersion=*&&_kMDItemMediaEmbeddingVersion!=%!l(MISSING)d)"
+ "(_kMDItemNeedsEmbeddings!=* && ((kMDItemEmbeddingVersion=*&&kMDItemEmbeddingVersion!=%!l(MISSING)d) || (_kMDItemMediaEmbeddingVersion=*&&_kMDItemMediaEmbeddingVersion!=%!l(MISSING)d)))"
+ "(_kMDItemNeedsKeyphrases!=* && (kMDItemKeyphraseVersion!=* || (kMDItemKeyphraseVersion=*&&kMDItemKeyphraseVersion!=%!l(MISSING)d)) && %!@(MISSING))"
+ "(_kMDItemUpdaterVersion!=*&&(%!@(MISSING)))"
+ "(_kMDItemUpdaterVersion=*&&_kMDItemUpdaterVersion!=%!l(MISSING)d)"
+ "(kMDItemEmbeddingVersion=*&&kMDItemEmbeddingVersion!=%!l(MISSING)d)"
+ "(kMDItemKeyphraseVersion=*&&kMDItemKeyphraseVersion!=%!l(MISSING)d)"
+ "(kMDItemTextContentLanguage!=* || (kMDItemTextContentLanguage=*&&FieldMatch(kMDItemTextContentLanguage,%!@(MISSING))))"
+ "(true)"
+ ","
+ ".."
+ "/.vol/%!l(MISSING)lu/%!l(MISSING)lu"
+ "/System/Volumes/Data"
+ "/System/Volumes/Data/.Spotlight-V100/"
+ "/System/Volumes/Data/private/var/db/Spotlight-V100/"
+ "/System/Volumes/Data/private/var/db/Spotlight/"
+ "/private/var/db/Spotlight-V100/"
+ "/private/var/db/Spotlight/"
+ "@\"NSDictionary\"8@?0"
+ "@172@0:8*16{?=*Q{?=IC}}24{?=*Q{?=IC}}48{?=*Q{?=IC}}72{?=*Q{?=IC}}96{?=*Q{?=IC}}120{?=*Q{?=IC}}144I168"
+ "B124@?0q8r*16{?=*Q{?=IC}}24{?=*Q{?=IC}}48{?=*Q{?=IC}}72{?=*Q{?=IC}}96B120"
+ "B48@0:8@16@24^@32^Q40"
+ "B52@?0q8i16r*20{?=*Q{?=IC}}28"
+ "B60@0:8@16@24I32@?36@?44@?52"
+ "B72@?0q8r*16{?=*Q{?=IC}}24{?=*Q{?=IC}}48"
+ "B76@0:8@16@24I32@?36@?44@?52@?60@?68"
+ "Bad journal plist, magic:0x%!l(MISSING)x, size:%!l(MISSING)d, pos:%!l(MISSING)d, end:%!l(MISSING)d"
+ "CSEmbeddingsUpdaterTimeout"
+ "FieldMatch(kMDItemContentType,%!@(MISSING))"
+ "IndexCompleteFromEmbeddingUpdater"
+ "IndexFromEmbeddingUpdater"
+ "ItemLanguageNotSupportedForEmbedding"
+ "MDFileUtil.c"
+ "PrimaryEmbeddingComplete"
+ "PrimaryEmbeddingEmpty"
+ "PrimaryEmbeddingNoTextInput"
+ "Process"
+ "Receive"
+ "Reset"
+ "SKGActivityJournal.log"
+ "SKGJob+Text:counterItems:"
+ "SKGUpdaterStore#setProtectionClassForFolder Cannot get dir for parentFd:%!d(MISSING) pathBuffer:%!s(MISSING)"
+ "SKGUpdaterStore#setProtectionClassForFolder Cannot get realpath for parentFd:%!d(MISSING) errno:%!d(MISSING)"
+ "SKGUpdaterStore#setProtectionClassForFolder File with name %!s(MISSING) has pc %!d(MISSING). Setting pc to %!d(MISSING)"
+ "SKGUpdaterStore#setProtectionClassForFolder Parent directory at path %!s(MISSING) has pc %!d(MISSING). Setting pc to %!d(MISSING)"
+ "SecondaryEmbeddingComplete"
+ "SecondaryEmbeddingNoTextInput"
+ "T@\"NSString\",&,N,V_path"
+ "TB,N,V_isInternalInstall"
+ "Test"
+ "Timeout"
+ "[Document Embedding Generation][SPEmbeddingModel] preheat timeout"
+ "_isInternalInstall"
+ "_kMDItemIsEvictedFile!=1"
+ "_kMDItemKnowledgeUpdaterVersion!=*"
+ "_kMDItemOwnerUserID==%!d(MISSING)"
+ "_kMDItemTextContentEmbedCheckLen"
+ "_path"
+ "_runCSCounterForQueryString:queryContext:counterItemBlock:counterAttrBlock:cancelBlock:"
+ "_runCSExtractForQueryString:queryContext:flags:processedItemBlock:batchArchivedBlock:batchUpdatedBlock:cancelBlock:errorBlock:"
+ "_runCSReindexForQueryString:queryContext:flags:batchProcessedBlock:batchUpdatedBlock:cancelBlock:"
+ "accurate_realpath"
+ "activity_journal"
+ "addEventForCSSearchableItems:items:"
+ "addEventForItem:bundleID:identifier:"
+ "com.adobe.pdf"
+ "com.apple.private.corespotlight.skgupdater"
+ "encodeProgressReport:"
+ "end counting"
+ "extractContentFromRecord:bundleID:content:maxChunkCountPtr:"
+ "extractContentFromRecordForCalendar:bundleID:content:maxChunkCountPtr:"
+ "extractContentFromRecordForMail:bundleID:content:maxChunkCountPtr:"
+ "extractContentFromRecordForMessages:bundleID:content:maxChunkCountPtr:"
+ "extractContentFromRecordForSafari:bundleID:content:maxChunkCountPtr:"
+ "generateCSReportWithCancelBlock:"
+ "generateEmbeddingForTextInputs:extendedContextLength:queryID:timeout:workCost:error:"
+ "indexSearchableItems:timeout:timeoutError:completion:"
+ "initWithParentPath:fileName:limit:"
+ "isInternalInstall"
+ "itemCount"
+ "itemsNeedEmbeddings"
+ "itemsNeedProcessing"
+ "itemsNeedProcessingDict"
+ "loadGraphWithJobContext:group:cancelBlock:"
+ "needsPriorityForRecord:bundleID:"
+ "processJournals %!@(MISSING)"
+ "processReportWithJobContext:group:cancelBlock:"
+ "public.plain-text"
+ "public.presentation"
+ "public.rtf"
+ "public.spreadsheet"
+ "rc == 0"
+ "requestCSProgressReport:cancelBlock:"
+ "setDisableBundles:"
+ "setIsInternalInstall:"
+ "setPath:"
+ "setProtectionClassForFolder:protectionClass:"
+ "sharedJournal"
+ "shouldGenerateEmbeddingsForPastRecord:bundleID:"
+ "shouldGenerateEmbeddingsForRecord:bundleID:"
+ "shouldGenerateKeyphrasesForRecord:bundleID:"
+ "starting counting"
+ "stringByAppendingString:"
+ "unloadGraphWithJobContext:group:cancelBlock:"
+ "v116@?0r*8{?=*Q{?=IC}}16{?=*Q{?=IC}}40{?=*Q{?=IC}}64{?=*Q{?=IC}}88B112"
+ "v16@?0@\"NSDictionary\"8"
+ "v16@?0r^{skg_playback_info=I(?={?=Id*}{?=dqq}{?=*}{?=**q})}8"
+ "v24@0:8i16i20"
+ "v28@0:8i16@20"
+ "v32@0:8@16^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24"
+ "v32@?0@\"NSString\"8@\"NSString\"16@\"NSNumber\"24"
+ "v32@?0{?=*Q{?=IC}}8"
+ "v36@0:8i16@20@28"
+ "v40@0:8@16@24@?32"
+ "v48@0:8@16d24@32@?40"
+ "v48@?0r*8Q16{?=*Q{?=IC}}24"
+ "v72@?0q8r*16{?=*Q{?=IC}}24{?=*Q{?=IC}}48"
+ "{?=\"containerBytes\"*\"containerLength\"Q\"reference\"{?=\"embeddedReference\"I\"type\"C}}"
- "((kMDItemEmbeddingVersion!=%!l(MISSING)d || _kMDItemMediaEmbeddingVersion!=%!l(MISSING)d) || (kMDItemEmbeddingVersion!=*))"
- "(_kMDItemKnowledgeIndexVersion!=* || _kMDItemKnowledgeIndexVersion!=%!l(MISSING)d)"
- "(_kMDItemKnowledgeUpdaterVersion!=* || _kMDItemKnowledgeUpdaterVersion!=%!l(MISSING)d)"
- "(_kMDItemUpdaterVersion!=* || _kMDItemUpdaterVersion!=%!l(MISSING)d)"
- "(kMDItemEmbeddingVersion==* || _kMDItemMediaEmbeddingVersion==*)"
- "(kMDItemKeyphraseVersion!=%!l(MISSING)d || (kMDItemKeyphraseVersion!=* && (%!@(MISSING))))"
- "@124@0:8*16{?=*{?=IC}}24{?=*{?=IC}}40{?=*{?=IC}}56{?=*{?=IC}}72{?=*{?=IC}}88{?=*{?=IC}}104I120"
- "@32@0:8^{fd_obj=}16q24"
- "@32@0:8q16@?24"
- "@44@0:8@16B24^Q28^Q36"
- "B44@?0q8i16r*20{?=*{?=IC}}28"
- "B56@?0q8r*16{?=*{?=IC}}24{?=*{?=IC}}40"
- "B64@0:8@16@24B32B36@?40@?48@?56"
- "B92@?0q8r*16{?=*{?=IC}}24{?=*{?=IC}}40{?=*{?=IC}}56{?=*{?=IC}}72B88"
- "Error running query to get eligible items for embedding generation: %!@(MISSING)"
- "Error running query to get items with embeddings: %!@(MISSING)"
- "Received item - bundle: %!s(MISSING) identifier: %!s(MISSING)\n"
- "SKGUpdaterStore#initWithParentFd created DB for indexType: %!d(MISSING) parentFd: %!d(MISSING) name: %!s(MISSING)"
- "Timeout running query to find eligible items"
- "_kMDItemIsZombie!=1"
- "_kMDItemNeedsEmbeddings!=*"
- "_kMDItemNeedsKeyphrases!=*"
- "_runCSExtractForQueryString:queryContext:shouldArchive:processedItemBlock:batchArchivedBlock:batchUpdatedBlock:cancelBlock:errorBlock:"
- "_runCSReindexForQueryString:queryContext:includeKeyphrases:includeEmbeddings:batchProcessedBlock:batchUpdatedBlock:cancelBlock:"
- "addReceiveEvent:identifier:"
- "addTestEvent:"
- "com.apple.private.corespotlight.sender"
- "csevent"
- "extractContentFromRecord:returnContent:contentLenPtr:maxChunkCountPtr:"
- "generateEmbeddingForTextInputs:queryID:timeout:workCost:error:"
- "graph exceeds capacity"
- "initWithFd:limit:"
- "itemsNeedEmbedding"
- "kMDItemTextContentLanguage!=* || (%!@(MISSING))"
- "kMDItemTextContentLanguage=\"%!@(MISSING)\""
- "loadGraphWithJobContext:cancelBlock:"
- "needsPriorityForRecord:"
- "queryEmbeddingGenProgressWithTimeout:cancelBlock:"
- "reportEmbeddingProgress"
- "reportProgress:group:cancelBlock:"
- "reportProgressWithCancelBlock:"
- "shouldGenerateEmbeddingsForPastRecord:"
- "shouldGenerateEmbeddingsForRecord:"
- "shouldGenerateKeyphrasesForRecord:"
- "stringComposedLength:maxLen:"
- "unloadGraphWithCancelBlock:"
- "v16@?0r^{skg_playback_info=I(?={?=Id*}{?=dqq}{?=*}{?=**})}8"
- "v24@?0{?=*{?=IC}}8"
- "v32@0:8r*16^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24"
- "v40@?0r*8Q16{?=*{?=IC}}24"
- "v56@?0q8r*16{?=*{?=IC}}24{?=*{?=IC}}40"
- "v84@?0r*8{?=*{?=IC}}16{?=*{?=IC}}32{?=*{?=IC}}48{?=*{?=IC}}64B80"
- "{?=\"containerBytes\"*\"reference\"{?=\"embeddedReference\"I\"type\"C}}"

```
