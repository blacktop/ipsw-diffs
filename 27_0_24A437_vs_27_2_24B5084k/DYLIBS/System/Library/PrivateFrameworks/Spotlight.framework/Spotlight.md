## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`

```diff

-2459.105.0.0.0
-  __TEXT.__text: 0x98e84
+2465.1.2.0.0
+  __TEXT.__text: 0x9c800
   __TEXT.__objc_methlist: 0x2ad4
-  __TEXT.__const: 0xe24
-  __TEXT.__oslogstring: 0x5608
-  __TEXT.__cstring: 0x35cc
-  __TEXT.__gcc_except_tab: 0x5564
+  __TEXT.__const: 0xe74
+  __TEXT.__oslogstring: 0x5822
+  __TEXT.__cstring: 0x355c
+  __TEXT.__gcc_except_tab: 0x5598
   __TEXT.__ustring: 0x6
-  __TEXT.__swift5_typeref: 0x7bc
-  __TEXT.__swift5_fieldmd: 0x298
-  __TEXT.__constg_swiftt: 0x414
-  __TEXT.__swift5_reflstr: 0x334
+  __TEXT.__swift5_typeref: 0x7da
+  __TEXT.__swift5_fieldmd: 0x28c
+  __TEXT.__constg_swiftt: 0x3fc
+  __TEXT.__swift5_reflstr: 0x324
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_types: 0x38
-  __TEXT.__swift_as_entry: 0x98
+  __TEXT.__swift_as_entry: 0x9c
   __TEXT.__swift_as_ret: 0x78
-  __TEXT.__swift_as_cont: 0x118
-  __TEXT.__swift5_capture: 0x3c8
+  __TEXT.__swift_as_cont: 0x114
+  __TEXT.__swift5_capture: 0x3f4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__unwind_info: 0x1aa8
-  __TEXT.__eh_frame: 0x1130
+  __TEXT.__unwind_info: 0x1af8
+  __TEXT.__eh_frame: 0x1200
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e40
+  __DATA_CONST.__objc_selrefs: 0x2e50
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_arraydata: 0x3e8
-  __DATA_CONST.__got: 0x18f0
-  __AUTH_CONST.__const: 0x1400
-  __AUTH_CONST.__cfstring: 0x3000
-  __AUTH_CONST.__objc_const: 0x4710
+  __DATA_CONST.__got: 0x1918
+  __AUTH_CONST.__const: 0x1488
+  __AUTH_CONST.__cfstring: 0x2fe0
+  __AUTH_CONST.__objc_const: 0x4700
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x258
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x12f0
+  __AUTH_CONST.__auth_got: 0x1368
   __AUTH.__objc_data: 0xe8
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x3c4
-  __DATA.__data: 0x750
-  __DATA_DIRTY.__objc_data: 0xe60
-  __DATA_DIRTY.__data: 0x2f0
+  __DATA.__data: 0x768
+  __DATA_DIRTY.__objc_data: 0xe50
+  __DATA_DIRTY.__data: 0x2f8
   __DATA_DIRTY.__bss: 0x6b0
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1714
-  Symbols:   4466
-  CStrings:  933
+  Functions: 1735
+  Symbols:   4487
+  CStrings:  937
 
Symbols:
+ -[SPClientSession dealloc]
+ _CFNotificationCenterRemoveObserver
+ _CFPreferencesSynchronize
+ _SSAppExclusionsEnabled
+ _SSGetDisabledAppSet
+ _SSGetDisabledBundleSet
+ _SSInvalidateAppExclusionsDisabledIDsCache
+ __OBJC_$_CLASS_METHODS_SPGenerativeSearchClient(Spotlight|Spotlight)
+ __OBJC_$_INSTANCE_METHODS_SPGenerativeSearchClient(Spotlight|Spotlight)
+ __SPTCCSiriAccessChangedCallback
+ ___27-[SPClientSession activate]_block_invoke_2
+ ____SPTCCSiriAccessChangedCallback_block_invoke
+ ___swift_closure_destructor.157Tm
+ ___swift_closure_destructorTm
+ ___swift_project_boxed_opaque_existential_1
+ _activate.sTCCObserverOnce
+ _kCFPreferencesAnyHost
+ _kCFPreferencesCurrentUser
+ _notify_cancel
+ _objc_msgSend$contactEntity
+ _objc_msgSend$executeMailQueryWithContactEmails:contactNames:limit:completionHandler:
+ _objc_msgSend$isZKWAutoShortcutBundle:
+ _objc_msgSend$name
+ _objc_msgSend$wantsSearchDomain:
+ _swift_beginAccess
+ _swift_endAccess
+ _swift_retain_x27
+ _symbolic _____y_____GSg 12HybridSearch15ComposableQueryV AA11MailContentV
+ _symbolic _____y_____y_____GG s23_ContiguousArrayStorageC 12HybridSearch15ComposableQueryV AC11MailContentV
- -[SPClientSession disabledBundleIds]
- _SPGetDisabledAppSet
- _SPGetDisabledBundleSet
- __INSTANCE_METHODS_SPGenerativeSearchClient
- __OBJC_$_CLASS_METHODS_SPGenerativeSearchClient(Spotlight)
- ___swift_closure_destructor.186Tm
- _objc_msgSend$setWithSet:
- _symbolic _____ 12HybridSearch15RetrievalResultV
CStrings:
+ "App Shortcuts"
+ "Contact participant mail query [%s] cancelled during error handling"
+ "Contact participant mail query [%s] cancelled with CancellationError"
+ "Contact participant mail query [%s] could not attach participant filter, returning no results: %s"
+ "Contact participant mail query [%s] failed: %s"
+ "Contact participant mail query [%s] returned %ld results, tophitCount=%ld"
+ "Contact participant mail query [%s]: %ld/%ld results dropped — unsupported entity types filtered by wrapMailSearchResults"
+ "Contact participant mail query [%s]: no usable contact handles, returning no results"
+ "Executing contact participant mail query [%s]: emails=%ld names=%ld limit: %ld"
+ "SPGenerativeSearchClient"
+ "SPZKWQueryTask addApplicationResultsFromPredictionResponse"
+ "TU extraction query [%s]: hsClient is nil — cannot resolve source documents for %ld TU results"
+ "[qid=%lu][SPKGenerativeSearchMailQuery] Contact-entity query: emails=%lu names=%lu"
+ "[qid=%lu][SPKGenerativeSearchSiriTranscriptQuery] Disabled: contact-entity search excludes transcripts"
+ "_kMDItemThumbnailData"
+ "com.apple.spotlight.tcc.siriAccessChanged"
+ "contactParticipant emails=%ld names=%ld limit=%ld"
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
- "com.apple.CloudDocs.MobileDocumentsFileProvider"
- "com.apple.CloudDocs.iCloudDriveFileProvider"
- "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
- "com.apple.FileProvider.LocalStorage"
- "mailClientAdapter is nil - cannot retrieve mail identifiers"
- "userQueryString=%{private}s llmParses=%ld"
- "zkw has apps"
```
