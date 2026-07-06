## NotesSupport

> `/System/Library/PrivateFrameworks/NotesSupport.framework/Versions/A/NotesSupport`

```diff

-  __TEXT.__text: 0x57e94
+  __TEXT.__text: 0x5904c
   __TEXT.__delay_helper: 0x2cc
-  __TEXT.__objc_methlist: 0x4208
+  __TEXT.__objc_methlist: 0x42f8
   __TEXT.__const: 0x9ac
-  __TEXT.__cstring: 0x42ea
-  __TEXT.__gcc_except_tab: 0xe9c
-  __TEXT.__oslogstring: 0x3ae6
+  __TEXT.__cstring: 0x433a
+  __TEXT.__gcc_except_tab: 0xed0
+  __TEXT.__oslogstring: 0x3d46
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x2bb
   __TEXT.__swift5_capture: 0x210

   __TEXT.__swift_as_entry: 0x30
   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x2c
-  __TEXT.__unwind_info: 0x1c98
+  __TEXT.__unwind_info: 0x1cf8
   __TEXT.__eh_frame: 0x7a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8c8
+  __DATA_CONST.__const: 0x8d0
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3098
+  __DATA_CONST.__objc_selrefs: 0x3100
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x178
-  __DATA_CONST.__got: 0x880
-  __AUTH_CONST.__const: 0x2210
-  __AUTH_CONST.__cfstring: 0x4180
-  __AUTH_CONST.__objc_const: 0x5de8
+  __DATA_CONST.__got: 0x888
+  __AUTH_CONST.__const: 0x22b0
+  __AUTH_CONST.__cfstring: 0x41c0
+  __AUTH_CONST.__objc_const: 0x5e80
   __AUTH_CONST.__objc_intobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0xea0
-  __AUTH.__objc_data: 0x170
-  __AUTH.__data: 0x1f0
-  __DATA.__objc_ivar: 0x218
-  __DATA.__data: 0x678
-  __DATA.__bss: 0x510
-  __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1220
-  __DATA_DIRTY.__data: 0x330
-  __DATA_DIRTY.__bss: 0x790
+  __AUTH.__objc_data: 0x120
+  __AUTH.__data: 0xa0
+  __DATA.__objc_ivar: 0x220
+  __DATA.__data: 0x628
+  __DATA.__bss: 0x480
+  __DATA_DIRTY.__objc_data: 0x1270
+  __DATA_DIRTY.__data: 0x4d0
+  __DATA_DIRTY.__bss: 0x820
+  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2556
-  Symbols:   5389
-  CStrings:  1508
+  Functions: 2583
+  Symbols:   5433
+  CStrings:  1523
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ -[ICBaseSearchIndexerDataSource indexingScope]
+ -[ICBaseSearchIndexerDataSource setIndexingScope:]
+ -[ICBaseSearchIndexerDataSource waitForPendingChangeProcessing]
+ -[ICCDCSIReindexer reindexAllSearchableItemsWithScope:completionHandler:]
+ -[ICIndexItemsOperation _indexBatchItemCount]
+ -[ICIndexItemsOperation _indexBatchMaxTotalSize]
+ -[ICIndexItemsOperation _resetContextForDataSourceIfNeededInExtension:]
+ -[ICReindexAllItemsOperation indexingScope]
+ -[ICReindexAllItemsOperation setIndexingScope:]
+ -[ICSearchIndexer _startObservingChangesOnIndexingQueue]
+ -[ICSearchIndexer determineIfReindexIsNeededFromClientStateWithCompletionHandler:]
+ -[ICSearchIndexer finishObservedChangesAndRemainingOperationsWithCompletionHandler:]
+ -[ICSearchIndexer indexPendingItemsWithCompletionHandler:]
+ -[ICSearchIndexer reindexAllSearchableItemsInIndex:scope:completionHandler:]
+ -[ICSearchIndexer reindexAllSearchableItemsWithScope:completionHandler:]
+ -[ICSearchIndexer startObservingChangesAndWait]
+ GCC_except_table13
+ GCC_except_table25
+ GCC_except_table33
+ GCC_except_table49
+ GCC_except_table54
+ GCC_except_table55
+ GCC_except_table63
+ GCC_except_table79
+ GCC_except_table84
+ GCC_except_table88
+ GCC_except_table89
+ OBJC_IVAR_$_ICBaseSearchIndexerDataSource._indexingScope
+ OBJC_IVAR_$_ICReindexAllItemsOperation._indexingScope
+ __58-[ICSearchIndexer indexPendingItemsWithCompletionHandler:]_block_invoke
+ __76-[ICSearchIndexer reindexAllSearchableItemsInIndex:scope:completionHandler:]_block_invoke
+ __82-[ICSearchIndexer determineIfReindexIsNeededFromClientStateWithCompletionHandler:]_block_invoke
+ __84-[ICSearchIndexer finishObservedChangesAndRemainingOperationsWithCompletionHandler:]_block_invoke
+ ___47-[ICSearchIndexer startObservingChangesAndWait]_block_invoke
+ ___58-[ICSearchIndexer indexPendingItemsWithCompletionHandler:]_block_invoke
+ ___63-[ICBaseSearchIndexerDataSource waitForPendingChangeProcessing]_block_invoke
+ ___71-[ICIndexItemsOperation _resetContextForDataSourceIfNeededInExtension:]_block_invoke
+ ___76-[ICSearchIndexer reindexAllSearchableItemsInIndex:scope:completionHandler:]_block_invoke
+ ___82-[ICSearchIndexer determineIfReindexIsNeededFromClientStateWithCompletionHandler:]_block_invoke
+ ___84-[ICSearchIndexer finishObservedChangesAndRemainingOperationsWithCompletionHandler:]_block_invoke
+ ___84-[ICSearchIndexer finishObservedChangesAndRemainingOperationsWithCompletionHandler:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSData"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0l
+ _kICReindexAttachmentsOnLaunchKey
+ _objc_msgSend$_indexBatchItemCount
+ _objc_msgSend$_indexBatchMaxTotalSize
+ _objc_msgSend$_resetContextForDataSourceIfNeededInExtension:
+ _objc_msgSend$_startObservingChangesOnIndexingQueue
+ _objc_msgSend$indexingScope
+ _objc_msgSend$processChanges
+ _objc_msgSend$reindexAllSearchableItemsInIndex:scope:completionHandler:
+ _objc_msgSend$setIndexingScope:
+ _objc_msgSend$shouldDeferIndexingInMemoryConstrainedExtension
+ _objc_msgSend$waitForPendingChangeProcessing
- -[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]
- GCC_except_table38
- GCC_except_table42
- GCC_except_table47
- GCC_except_table56
- GCC_except_table65
- GCC_except_table76
- GCC_except_table77
- GCC_except_table82
- __40-[ICSearchIndexer startObservingChanges]_block_invoke
- __70-[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]_block_invoke
- ___70-[ICSearchIndexer reindexAllSearchableItemsInIndex:completionHandler:]_block_invoke
- _objc_msgSend$reindexAllSearchableItemsInIndex:completionHandler:
CStrings:
+ "Client state from CoreSpotlight does not match defaults; reindex needed"
+ "Deferring large object %@ from in-extension indexing to avoid jetsam; the app will index it on next launch."
+ "Error fetching client state from CoreSpotlight: %@; assuming reindex needed"
+ "Finished indexing pending items, error: %@"
+ "Finished observed changes and remaining indexing operations"
+ "ICAttachment"
+ "Indexing %lu pending item(s) with a regular indexing operation"
+ "No client state in CoreSpotlight; reindex needed"
+ "No client state in defaults; reindex needed"
+ "No pending items to index"
+ "ReindexAttachmentsOnLaunch"
+ "Search indexing disabled. Not indexing pending items."
+ "Staging data source %@ for reindexing in operation %@ (scope %lu)"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
- "Staging data source %@ for reindexing in operation %@"

```
