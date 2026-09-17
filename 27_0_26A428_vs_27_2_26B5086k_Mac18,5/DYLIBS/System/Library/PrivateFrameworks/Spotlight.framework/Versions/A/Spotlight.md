## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Versions/A/Spotlight`

```diff

-2459.405.0.0.0
-  __TEXT.__text: 0xd6600
-  __TEXT.__objc_methlist: 0x53e4
-  __TEXT.__const: 0x25b0
-  __TEXT.__gcc_except_tab: 0x4154
-  __TEXT.__cstring: 0x6cab
-  __TEXT.__oslogstring: 0x584f
+2465.1.2.0.0
+  __TEXT.__text: 0xe26a8
+  __TEXT.__objc_methlist: 0x5444
+  __TEXT.__const: 0x2620
+  __TEXT.__gcc_except_tab: 0x4160
+  __TEXT.__cstring: 0x6dd1
+  __TEXT.__oslogstring: 0x5bbf
   __TEXT.__ustring: 0x32
-  __TEXT.__constg_swiftt: 0xaac
-  __TEXT.__swift5_typeref: 0xd79
-  __TEXT.__swift5_reflstr: 0x757
-  __TEXT.__swift5_fieldmd: 0x7f8
-  __TEXT.__swift5_types: 0xa0
+  __TEXT.__swift5_typeref: 0xe5f
+  __TEXT.__swift5_fieldmd: 0x834
+  __TEXT.__constg_swiftt: 0xa2c
+  __TEXT.__swift5_reflstr: 0x7d7
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_proto: 0x14c
-  __TEXT.__swift_as_entry: 0xd0
+  __TEXT.__swift5_types: 0x9c
+  __TEXT.__swift_as_entry: 0xd4
   __TEXT.__swift_as_ret: 0xc0
-  __TEXT.__swift_as_cont: 0x174
-  __TEXT.__swift5_capture: 0x4f0
+  __TEXT.__swift_as_cont: 0x168
+  __TEXT.__swift5_capture: 0x680
   __TEXT.__swift5_assocty: 0x168
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__unwind_info: 0x2f18
-  __TEXT.__eh_frame: 0x1a98
+  __TEXT.__unwind_info: 0x3028
+  __TEXT.__eh_frame: 0x1ce8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4590
+  __DATA_CONST.__objc_selrefs: 0x4630
   __DATA_CONST.__objc_superrefs: 0x190
-  __DATA_CONST.__objc_arraydata: 0xa38
-  __DATA_CONST.__got: 0x1548
-  __AUTH_CONST.__const: 0x4368
-  __AUTH_CONST.__cfstring: 0x6ec0
-  __AUTH_CONST.__objc_const: 0x7c68
+  __DATA_CONST.__objc_arraydata: 0xa18
+  __DATA_CONST.__got: 0x15b0
+  __AUTH_CONST.__const: 0x4828
+  __AUTH_CONST.__cfstring: 0x6f40
+  __AUTH_CONST.__objc_const: 0x7d58
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x8b8
-  __AUTH_CONST.__objc_arrayobj: 0x2d0
+  __AUTH_CONST.__objc_intobj: 0x8d0
+  __AUTH_CONST.__objc_arrayobj: 0x2a0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1758
+  __AUTH_CONST.__auth_got: 0x1870
   __AUTH.__objc_data: 0x580
   __AUTH.__data: 0x60
-  __DATA.__objc_ivar: 0x588
-  __DATA.__data: 0xc40
+  __DATA.__objc_ivar: 0x58c
+  __DATA.__data: 0xcd0
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1a60
-  __DATA_DIRTY.__data: 0x8e0
-  __DATA_DIRTY.__bss: 0xc20
+  __DATA_DIRTY.__objc_data: 0x1a48
+  __DATA_DIRTY.__data: 0x8e8
+  __DATA_DIRTY.__bss: 0xc10
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/SpotlightResources.framework/Versions/A/SpotlightResources
   - /System/Library/PrivateFrameworks/SpotlightServices.framework/Versions/A/SpotlightServices
   - /System/Library/PrivateFrameworks/SpotlightUIServices.framework/Versions/A/SpotlightUIServices
+  - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /System/Library/PrivateFrameworks/ToolKit.framework/Versions/A/ToolKit
   - /usr/lib/libDiagnosticMessagesClient.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3308
-  Symbols:   6700
-  CStrings:  1498
+  Functions: 3410
+  Symbols:   6755
+  CStrings:  1520
 
Symbols:
+ +[SPApplicationQuery _test_attemptCount]
+ +[SPApplicationQuery _test_bumpAttemptCount]
+ +[SPApplicationQuery _test_resetAttemptCount]
+ +[SPApplicationQuery _test_setAppBundleIDs:]
+ -[SPCoreSpotlightResult isSyntheticBookmark]
+ -[SPCoreSpotlightResult setIsSyntheticBookmark:]
+ -[SPQueryTask(MixedRanking) applyRootOverSubDomainPolicyToSections:]
+ -[SPQueryTask(MixedRanking) resultIsBookmarkLike:]
+ GCC_except_table118
+ GCC_except_table126
+ GCC_except_table156
+ GCC_except_table88
+ OBJC_IVAR_$_SPCoreSpotlightResult._isSyntheticBookmark
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _SSAppExclusionsEnabled
+ _SSCopyTCCDisabledBundlesForSiriAccess
+ _SSSubscribeTCCEventsForSiriAccess
+ _SSUnsubscribeTCCEventsForSiriAccess
+ __49+[SPApplicationQuery getOrUpdateAppBundleIDList:]_block_invoke
+ __OBJC_$_CLASS_METHODS_SPGenerativeSearchClient(Spotlight|Spotlight)
+ __OBJC_$_INSTANCE_METHODS_SPGenerativeSearchClient(Spotlight|Spotlight)
+ ___swift_closure_destructorTm
+ ___swift_project_boxed_opaque_existential_1
+ __swift_closure_destructor.157Tm
+ __swift_closure_destructor.224Tm
+ __swift_closure_destructor.264Tm
+ __swift_closure_destructor.55Tm
+ __swift_closure_destructor.69Tm
+ _objc_msgSend$applyRootOverSubDomainPolicyToSections:
+ _objc_msgSend$combineScores:config:
+ _objc_msgSend$contactEntity
+ _objc_msgSend$emailAddresses
+ _objc_msgSend$executeMailQueryWithContactEmails:contactNames:limit:completionHandler:
+ _objc_msgSend$hasCorrespondingBookmark
+ _objc_msgSend$isSyntheticBookmark
+ _objc_msgSend$isZKWAutoShortcutBundle:
+ _objc_msgSend$name
+ _objc_msgSend$pinOverrideMrScoreThreshold
+ _objc_msgSend$resultIsBookmarkLike:
+ _objc_msgSend$scoreResultType
+ _objc_msgSend$setHasCorrespondingBookmark:
+ _objc_msgSend$setIsSyntheticBookmark:
+ _objc_msgSend$setPolicyApplied:
+ _objc_msgSend$setPrePolicyScore:
+ _objc_msgSend$setScoreResultType:
+ _swift_isEscapingClosureAtFileLocation
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic Ig_
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic Say_____G 9Spotlight16SPPreferenceRuleV
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic So13CSSearchQueryC
+ _symbolic So17OS_dispatch_queueC
+ _symbolic _____SgXw 9Spotlight19SPPreferenceManagerC
+ _symbolic _____SgXwz_Xx 9Spotlight19SPPreferenceManagerC
+ _symbolic _____ySbG 2os21OSAllocatedUnfairLockV
+ _symbolic _____ySb_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____yShySSGG 2os21OSAllocatedUnfairLockV
+ _symbolic _____yShySSG_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
+ _symbolic _____yShy_____GG 2os21OSAllocatedUnfairLockV 9Spotlight16SPPreferenceRuleV
+ _symbolic _____yShy_____G_____G s13ManagedBufferCsRi__rlE 9Spotlight16SPPreferenceRuleV So16os_unfair_lock_sV
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 9Spotlight19SPPreferenceManagerC16FastAccessFilterV
+ _symbolic _____y_____GSg 12HybridSearch15ComposableQueryV AA11MailContentV
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 9Spotlight19SPPreferenceManagerC16FastAccessFilterV So16os_unfair_lock_sV
+ _symbolic _____y_____y_____GG s23_ContiguousArrayStorageC 12HybridSearch15ComposableQueryV AC11MailContentV
+ _symbolic _____yytG 8Dispatch0A11SpecificKeyC
+ getOrUpdateAppBundleIDList:.gClientBundleID
+ getOrUpdateAppBundleIDList:.gClientBundleIDOnceToken
- GCC_except_table113
- GCC_except_table121
- GCC_except_table151
- _CFNumberGetTypeID
- __INSTANCE_METHODS_SPGenerativeSearchClient
- __OBJC_$_CLASS_METHODS_SPGenerativeSearchClient(Spotlight)
- __ZNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEE5clearB9nqn220106Ev
- __swift_closure_destructor.183Tm
- __swift_closure_destructor.186Tm
- __swift_closure_destructor.205Tm
- _swift_dynamicCastUnknownClassUnconditional
- _symbolic ScCyyt_____GSg s5NeverO
- _symbolic ShySSGz_Xx
- _symbolic _____ 12HybridSearch15RetrievalResultV
- _symbolic _____yyt_____G s13ManagedBufferCsRi__rlE So16os_unfair_lock_sV
CStrings:
+ " || _kMDItemDomainIdentifier!="
+ " || kMDItemRelatedAppBundleIdentifier!="
+ "App Shortcuts"
+ "Contact participant mail query [%s] cancelled during error handling"
+ "Contact participant mail query [%s] cancelled with CancellationError"
+ "Contact participant mail query [%s] could not attach participant filter, returning no results: %s"
+ "Contact participant mail query [%s] failed: %s"
+ "Contact participant mail query [%s] returned %ld results, tophitCount=%ld"
+ "Contact participant mail query [%s]: %ld/%ld results dropped — unsupported entity types filtered by wrapMailSearchResults"
+ "Contact participant mail query [%s]: no usable contact handles, returning no results"
+ "DisabledBundlesFromSiriTCC"
+ "Executing contact participant mail query [%s]: emails=%ld names=%ld limit: %ld"
+ "Root-over-sub"
+ "SPGenerativeSearchClient"
+ "SPZKWQueryTask addApplicationResultsFromPredictionResponse"
+ "SSSubscribeTCCEventsForSiriAccess failed — TCC events will not be delivered this session"
+ "TU extraction query [%s]: hsClient is nil — cannot resolve source documents for %ld TU results"
+ "[%@] Root-over-sub: demoted %.4f -> %.4f below anchor %.4f"
+ "[%@] Root-over-sub: demoted shortcut %.4f -> %.4f below bookmark anchor %.4f"
+ "[qid=%llu][\"%@\"][%@] Pin '%@' (mrScore=%.4f) yielded to superior '%@' (mrScore=%.4f, delta=%.4f > threshold=%.4f)"
+ "[qid=%lu][SPKGenerativeSearchMailQuery] Contact-entity query: emails=%lu names=%lu"
+ "[qid=%lu][SPKGenerativeSearchSiriTranscriptQuery] Disabled: contact-entity search excludes transcripts"
+ "com.apple.CloudDocs.MobileDocumentsFileProvider"
+ "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
+ "com.apple.DocumentsApp"
+ "com.apple.FileProvider.LocalStorage"
+ "com.apple.Spotlight.prefs-mutations"
+ "com.apple.Spotlight.prefs-notify"
+ "com.apple.campo"
+ "com.apple.proactive.suggestedActions"
+ "com.apple.spotlight.tcc"
+ "contactParticipant emails=%ld names=%ld limit=%ld"
+ "lastUsedDate"
+ "mailClientAdapter is nil - cannot execute contact participant mail query"
+ "status=filterRejected"
+ "zkw has %lu apps"
- "Mail identifier retrieval (hardFilter) [%s] cancelled"
- "Mail identifier retrieval (hardFilter) [%s] cancelled during error handling"
- "Mail identifier retrieval (hardFilter) [%s] failed: %s"
- "Mail identifier retrieval (hardFilter) [%s] returned %ld results"
- "MailSearchClient.retrieveIdentifiers"
- "Retrieving mail identifiers (hardFilter) [%s]: '%{private}s' llmParses=%ld"
- "SPZKWQueryTask addApplicationResultsFromPredictionResponse with apps: %lu"
- "TU extraction query [%s]: gsClient is nil — cannot resolve source documents for %ld TU results"
- "[qid=%lu][%{public}@] Empty query string. Returning early."
- "_kMDItemBundleID!=com.apple.duetexpertd || _kMDItemDomainIdentifier!=com.apple.proactive.suggestedActions || kMDItemRelatedAppBundleIdentifier!="
- "_kMDItemBundleID!=com.apple.shortcuts || kMDItemRelatedAppBundleIdentifier!="
- "mailClientAdapter is nil - cannot retrieve mail identifiers"
- "userQueryString=%{private}s llmParses=%ld"
- "zkw has apps"
```
