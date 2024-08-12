## SpotlightKnowledge

> `/System/Library/PrivateFrameworks/SpotlightKnowledge.framework/SpotlightKnowledge`

```diff

-2312.1.0.4.0
-  __TEXT.__text: 0x7394
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x664
-  __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x1244
-  __TEXT.__oslogstring: 0x15
+2314.2.0.0.0
+  __TEXT.__text: 0x95a8
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_methlist: 0x794
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x1610
+  __TEXT.__oslogstring: 0xd8
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__objc_classname: 0xae
-  __TEXT.__objc_methname: 0x14fa
-  __TEXT.__objc_methtype: 0x1de
-  __TEXT.__objc_stubs: 0x1240
-  __DATA_CONST.__got: 0x150
-  __DATA_CONST.__const: 0x978
-  __DATA_CONST.__objc_classlist: 0x30
+  __TEXT.__unwind_info: 0x2a0
+  __TEXT.__objc_classname: 0xc4
+  __TEXT.__objc_methname: 0x18d3
+  __TEXT.__objc_methtype: 0x330
+  __TEXT.__objc_stubs: 0x1440
+  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__const: 0xa28
+  __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x648
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x728
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x3c0
-  __AUTH_CONST.__auth_got: 0x300
-  __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x3360
-  __AUTH_CONST.__objc_const: 0x870
+  __AUTH_CONST.__auth_got: 0x3f0
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x3400
+  __AUTH_CONST.__objc_const: 0xa00
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x68
-  __DATA.__bss: 0xd0
-  __DATA_DIRTY.__objc_data: 0x50
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x7c
+  __DATA.__bss: 0x118
+  __DATA_DIRTY.__objc_data: 0x140
+  __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
+  - /System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex
   - /System/Library/PrivateFrameworks/SpotlightEmbedding.framework/SpotlightEmbedding
   - /System/Library/PrivateFrameworks/SpotlightLinguistics.framework/SpotlightLinguistics
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 188
-  Symbols:   347
-  CStrings:  723
+  Functions: 243
+  Symbols:   438
+  CStrings:  817
 
Symbols:
+ _CFCalendarCreateWithIdentifier
+ _CFCalendarDecomposeAbsoluteTime
+ _CFCalendarSetTimeZone
+ _CFDictionaryGetValue
+ _CFStringGetCString
+ _CFTimeZoneCopySystem
+ _OBJC_CLASS_$_SKGActivityJournal
+ _OBJC_METACLASS_$_SKGActivityJournal
+ _SKGLogAgentInit
+ _SKGLogCategoryDefault
+ _SKGLogEmbedInit
+ _SKGLogEventInit
+ _SKGLogGraphInit
+ _SKGLogInit
+ _SKGLogJournalInit
+ _SKGLogKeyphraseInit
+ _SKGLogUpdaterInit
+ __CFCopySystemVersionDictionary
+ __MDPlistContainerCopyObject
+ ___error
+ ___stderrp
+ __kCFSystemVersionBuildVersionKey
+ __os_log_error_impl
+ _close
+ _fd_create_protected
+ _fd_lseek
+ _fd_release
+ _fd_write
+ _fd_zero_truncate
+ _fprintf
+ _fwrite
+ _getpid
+ _isAppleInternalInstall
+ _kCFAllocatorSystemDefault
+ _kCFGregorianCalendar
+ _lseek
+ _mmap
+ _munmap
+ _objc_autorelease
+ _open
+ _os_log_create
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _si_compute_oid_for_identifier_bundle_id
+ _snprintf
+ _strlen
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "\x11"
+ "### SKGActivityJournal#initWithParentPath Error %!@(MISSING) creating %!@(MISSING)"
+ "### SKGActivityJournal#initWithParentPath error opening errno %!d(MISSING) creating %!@(MISSING)"
+ "### file open failed"
+ "### mmap failed"
+ "### unknown type %!d(MISSING) at offset %!l(MISSING)d\n"
+ "%!d(MISSING)-%!d(MISSING)-%!d(MISSING) %!d(MISSING):%!d(MISSING):%!d(MISSING)"
+ "%!s(MISSING) for item - bundle: %!s(MISSING) identifier: %!s(MISSING) oid: 0x%!l(MISSING)lx\n"
+ "%!s(MISSING) pid: %!d(MISSING) time: %!s(MISSING)sbuild: %!s(MISSING)\n"
+ "/%!@(MISSING)"
+ "/%!s(MISSING)/%!s(MISSING)"
+ "@40@0:8@16@24q32"
+ "@48@0:8{?=*Q{?=IC}}16@40"
+ "B48@0:8@16@24^@32^Q40"
+ "IndexCompleteFromEmbeddingUpdater"
+ "IndexFromEmbeddingUpdater"
+ "Init"
+ "ItemLanguageNotSupportedForEmbedding"
+ "Journal was reset at time %!s(MISSING), size before reset: %!l(MISSING)lu, size after reset: %!l(MISSING)lu\n"
+ "Library/Spotlight/CoreSpotlight"
+ "PrimaryEmbeddingComplete"
+ "PrimaryEmbeddingEmpty"
+ "PrimaryEmbeddingNoTextInput"
+ "Process"
+ "Receive"
+ "Reset"
+ "SKGActivityJournal"
+ "SKGActivityJournal.log"
+ "SKGActivityJournalPlayback:block:"
+ "SecondaryEmbeddingComplete"
+ "SecondaryEmbeddingNoTextInput"
+ "SpotlightKnowledgeAgent"
+ "SpotlightKnowledgeEmbedding"
+ "SpotlightKnowledgeEvent"
+ "SpotlightKnowledgeEvents/index.V2"
+ "SpotlightKnowledgeGraph"
+ "SpotlightKnowledgeJournals"
+ "SpotlightKnowledgeKeyphrases"
+ "SpotlightKnowledgeUpdater"
+ "T@\"NSString\",&,N,V_path"
+ "TB,N,V_isInternalInstall"
+ "TB,N,V_started"
+ "T^{fd_obj=},N,V_fd"
+ "Test"
+ "Test %!s(MISSING)\n"
+ "T{os_unfair_lock_s=I},N,V_lock"
+ "Unknown"
+ "^{fd_obj=}"
+ "^{fd_obj=}16@0:8"
+ "_SKGActivityDump:dst:"
+ "_fd"
+ "_isInternalInstall"
+ "_kMDItemTextContentEmbedCheckLen"
+ "_lock"
+ "_path"
+ "_started"
+ "activity_journal"
+ "addEventForCSSearchableItems:items:"
+ "addEventForItem:bundleID:identifier:"
+ "addUpdaterAttributesForMDPlistRecord:bundleID:"
+ "bundleID"
+ "com.apple.spotlightknowledge"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "extractContentFromRecord:bundleID:content:maxChunkCountPtr:"
+ "extractContentFromRecordForCalendar:bundleID:content:maxChunkCountPtr:"
+ "extractContentFromRecordForMail:bundleID:content:maxChunkCountPtr:"
+ "extractContentFromRecordForMessages:bundleID:content:maxChunkCountPtr:"
+ "extractContentFromRecordForSafari:bundleID:content:maxChunkCountPtr:"
+ "fd"
+ "fileSystemRepresentation"
+ "initWithParentPath:fileName:limit:"
+ "isInternalInstall"
+ "kSKGActivityJournalReset: Journal size %!l(MISSING)ld is > %!l(MISSING)ld\n"
+ "lock"
+ "needsPriorityForRecord:bundleID:"
+ "processorAttributesForRecord:bundleID:"
+ "setFd:"
+ "setIsInternalInstall:"
+ "setLock:"
+ "setPath:"
+ "setStarted:"
+ "sharedJournal"
+ "shouldGenerateEmbeddingsForPastRecord:bundleID:"
+ "shouldGenerateEmbeddingsForRecord:bundleID:"
+ "shouldGenerateKeyphrasesForRecord:bundleID:"
+ "started"
+ "stringByAppendingFormat:"
+ "stringByAppendingString:"
+ "uniqueIdentifier"
+ "unsignedIntegerValue"
+ "v16@?0r^{skg_playback_info=I(?={?=Id*}{?=dqq}{?=*}{?=**q})}8"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "v24@0:8^{fd_obj=}16"
+ "v28@0:8i16@20"
+ "v32@0:8@16^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24"
+ "v32@0:8I16^v20I28"
+ "v32@0:8r*16@?24"
+ "v36@0:8i16@20@28"
+ "writeEvent:data:dataSize:"
+ "writeInit"
+ "yMdHms"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "@44@0:8@16B24^Q28^Q36"
- "Q32@0:8@16Q24"
- "extractContentFromRecord:returnContent:contentLenPtr:maxChunkCountPtr:"
- "needsPriorityForRecord:"
- "processorAttributesForRecord:"
- "shouldGenerateEmbeddingsForPastRecord:"
- "shouldGenerateEmbeddingsForRecord:"
- "shouldGenerateKeyphrasesForRecord:"
- "stringComposedLength:maxLen:"

```
