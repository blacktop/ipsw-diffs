## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-5726.2.0.0.0
-  __TEXT.__text: 0x3df538
-  __TEXT.__auth_stubs: 0x3ad0
-  __TEXT.__objc_methlist: 0x33d58
-  __TEXT.__const: 0xad58
+5728.0.0.0.0
+  __TEXT.__text: 0x3e0644
+  __TEXT.__auth_stubs: 0x3ae0
+  __TEXT.__objc_methlist: 0x33dbc
+  __TEXT.__const: 0xad98
   __TEXT.__swift5_typeref: 0x38b6
   __TEXT.__constg_swiftt: 0x2bb8
   __TEXT.__swift5_reflstr: 0x1e06
   __TEXT.__swift5_fieldmd: 0x263c
-  __TEXT.__swift5_proto: 0x7c8
+  __TEXT.__swift5_proto: 0x7cc
   __TEXT.__swift5_types: 0x360
   __TEXT.__swift5_capture: 0xd24
   __TEXT.__swift_as_entry: 0x290
   __TEXT.__swift_as_ret: 0x300
-  __TEXT.__cstring: 0x508a7
+  __TEXT.__cstring: 0x508c6
   __TEXT.__swift5_builtin: 0x140
   __TEXT.__swift5_protos: 0x64
-  __TEXT.__oslogstring: 0x1712a
+  __TEXT.__oslogstring: 0x172d8
   __TEXT.__swift5_assocty: 0x3a8
   __TEXT.__swift5_mpenum: 0x4c
-  __TEXT.__gcc_except_tab: 0x5568
+  __TEXT.__gcc_except_tab: 0x556c
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x27a
-  __TEXT.__unwind_info: 0xe4d0
-  __TEXT.__eh_frame: 0x90d8
+  __TEXT.__unwind_info: 0xe500
+  __TEXT.__eh_frame: 0x9110
   __TEXT.__objc_classname: 0x7642
-  __TEXT.__objc_methname: 0x850c2
+  __TEXT.__objc_methname: 0x85135
   __TEXT.__objc_methtype: 0xc56c
-  __TEXT.__objc_stubs: 0x350c0
+  __TEXT.__objc_stubs: 0x35140
   __DATA_CONST.__got: 0x2ba8
-  __DATA_CONST.__const: 0x118b0
+  __DATA_CONST.__const: 0x11898
   __DATA_CONST.__objc_classlist: 0x1c80
   __DATA_CONST.__objc_catlist: 0x2b0
   __DATA_CONST.__objc_protolist: 0x8c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14508
+  __DATA_CONST.__objc_selrefs: 0x14528
   __DATA_CONST.__objc_protorefs: 0x208
   __DATA_CONST.__objc_superrefs: 0x15a0
   __DATA_CONST.__objc_arraydata: 0x1d48
-  __AUTH_CONST.__auth_got: 0x1d80
-  __AUTH_CONST.__const: 0xaf48
-  __AUTH_CONST.__cfstring: 0x30a20
-  __AUTH_CONST.__objc_const: 0x76b18
+  __AUTH_CONST.__auth_got: 0x1d88
+  __AUTH_CONST.__const: 0xaf68
+  __AUTH_CONST.__cfstring: 0x30a40
+  __AUTH_CONST.__objc_const: 0x76bb0
   __AUTH_CONST.__objc_arrayobj: 0x540
   __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0xbe0

   __AUTH.__data: 0x770
   __DATA.__objc_ivar: 0x4444
   __DATA.__data: 0x6650
-  __DATA.__bss: 0xb558
+  __DATA.__bss: 0xb5d8
   __DATA.__common: 0xf8
   __DATA_DIRTY.__objc_ivar: 0xf04
   __DATA_DIRTY.__objc_data: 0xd9e8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8502DA5A-57DF-381B-B60A-5AEE34B0F211
-  Functions: 23765
-  Symbols:   65145
-  CStrings:  37177
+  UUID: 3ADD8E34-4FE3-368C-B01A-E7DC468CD2BA
+  Functions: 23779
+  Symbols:   65160
+  CStrings:  37189
 
Symbols:
+ +[FCAudioPlaylist requiresBatchedFirstSync]
+ +[FCIssueReadingHistory requiresBatchedFirstSync]
+ +[FCPersonalizationData requiresBatchedFirstSync]
+ +[FCPrivateChannelMembershipController requiresBatchedFirstSync]
+ +[FCPrivateDataController requiresBatchedFirstSync]
+ +[FCPuzzleHistory requiresBatchedFirstSync]
+ +[FCReadingHistory requiresBatchedFirstSync]
+ +[FCReadingList requiresBatchedFirstSync]
+ +[FCShortcutCategoryList requiresBatchedFirstSync]
+ +[FCShortcutList requiresBatchedFirstSync]
+ +[FCSubscriptionList requiresBatchedFirstSync]
+ +[FCUserEventHistory requiresBatchedFirstSync]
+ +[FCUserInfo requiresBatchedFirstSync]
+ -[FCModifyRecordsCommand createdOrModifiedRecordIDs]
+ -[FCModifyRecordsCommand deletedRecordIDs]
+ -[FCPrivateDataController recordNamesPendingSaveToCloud]
+ -[FCPrivateZoneSyncManager initWithRecordZoneID:desiredKeys:requiresBatchedFirstSync:currentState:]
+ -[FCReadingHistory willAccessArticleIDs:]
+ -[FCRemoveRecordsCommand createdOrModifiedRecordIDs]
+ -[FCRemoveRecordsCommand deletedRecordIDs]
+ _.str.26
+ _FCOperationPurposePDFReplica
+ _FCPuzzleThumbnailVersion
+ _OBJC_IVAR_$_FCPrivateZoneSyncManager._requiresBatchedFirstSync
+ __OBJC_$_PROP_LIST_FCRecordTransformingCommand
+ __OBJC_$_PROP_LIST_FCRemoveRecordsCommand
+ __PROTOCOLS__TtC8NewsCore20ItemExposureRegistry.18
+ ___107-[FCModifyRecordsCommand handleBatchOfLocalRecords:internalPrivateDataContext:qualityOfService:completion:]_block_invoke.40
+ ___107-[FCModifyRecordsCommand handleBatchOfLocalRecords:internalPrivateDataContext:qualityOfService:completion:]_block_invoke.42
+ ___52-[FCModifyRecordsCommand createdOrModifiedRecordIDs]_block_invoke
+ ___58-[FCPrivateDataController _serialSyncUpToDate:completion:]_block_invoke.77
+ ___58-[FCPrivateDataController _serialSyncUpToDate:completion:]_block_invoke.85
+ ___58-[FCPrivateDataController _serialSyncUpToDate:completion:]_block_invoke_2.88
+ ___67-[FCPuzzleThumbnailURLProtocol _fetchResourceMapWithID:completion:]_block_invoke.69
+ ___67-[FCPuzzleThumbnailURLProtocol _fetchResourceMapWithID:completion:]_block_invoke_2.71
+ ___67-[FCReadingHistory _preprocessSyncedDeletions:didUserClearHistory:]_block_invoke.135
+ ___block_literal_global.138
+ ___block_literal_global.2272
+ ___block_literal_global.2301
+ ___block_literal_global.2693
+ ___block_literal_global.2781
+ ___block_literal_global.2871
+ ___block_literal_global.2873
+ ___block_literal_global.2875
+ ___block_literal_global.2880
+ ___block_literal_global.2891
+ ___block_literal_global.2896
+ ___block_literal_global.2901
+ ___block_literal_global.2906
+ ___block_literal_global.291
+ ___block_literal_global.296
+ ___block_literal_global.356
+ _objc_msgSend$createdOrModifiedRecordIDs
+ _objc_msgSend$eraseAll
+ _objc_msgSend$fc_dateWithTimeIntervalBeforeNow:
+ _objc_msgSend$recordNamesPendingSaveToCloud
+ _objc_msgSend$requiresBatchedFirstSync
+ _objc_msgSend$stringByAppendingFormat:
+ _objc_msgSend$subsetOfItemIDs:accessedSinceDate:
- +[FCAudioPlaylist requiresBatchedSync]
- +[FCIssueReadingHistory requiresBatchedSync]
- +[FCPersonalizationData requiresBatchedSync]
- +[FCPrivateChannelMembershipController requiresBatchedSync]
- +[FCPrivateDataController requiresBatchedSync]
- +[FCPuzzleHistory requiresBatchedSync]
- +[FCReadingHistory requiresBatchedSync]
- +[FCReadingList requiresBatchedSync]
- +[FCShortcutCategoryList requiresBatchedSync]
- +[FCShortcutList requiresBatchedSync]
- +[FCSubscriptionList requiresBatchedSync]
- +[FCUserEventHistory requiresBatchedSync]
- +[FCUserInfo requiresBatchedSync]
- -[FCPrivateZoneSyncManager initWithRecordZoneID:desiredKeys:requiresBatchedSync:currentState:]
- -[FCReadingHistory willAcccessArticleIDs:]
- _.str.39
- _OBJC_IVAR_$_FCPrivateZoneSyncManager._requiresBatchedSync
- __PROTOCOLS__TtC8NewsCore20ItemExposureRegistry.17
- ___107-[FCModifyRecordsCommand handleBatchOfLocalRecords:internalPrivateDataContext:qualityOfService:completion:]_block_invoke.37
- ___107-[FCModifyRecordsCommand handleBatchOfLocalRecords:internalPrivateDataContext:qualityOfService:completion:]_block_invoke.39
- ___58-[FCPrivateDataController _serialSyncUpToDate:completion:]_block_invoke.68
- ___58-[FCPrivateDataController _serialSyncUpToDate:completion:]_block_invoke.79
- ___58-[FCPrivateDataController _serialSyncUpToDate:completion:]_block_invoke_2.82
- ___67-[FCPuzzleThumbnailURLProtocol _fetchResourceMapWithID:completion:]_block_invoke.63
- ___67-[FCPuzzleThumbnailURLProtocol _fetchResourceMapWithID:completion:]_block_invoke_2.65
- ___block_literal_global.134
- ___block_literal_global.2278
- ___block_literal_global.2307
- ___block_literal_global.2699
- ___block_literal_global.2787
- ___block_literal_global.280
- ___block_literal_global.283
- ___block_literal_global.2877
- ___block_literal_global.2879
- ___block_literal_global.2881
- ___block_literal_global.2886
- ___block_literal_global.2897
- ___block_literal_global.2902
- ___block_literal_global.2907
- ___block_literal_global.2912
- ___block_literal_global.352
- ___block_literal_global.81
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_NewsCore
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_NewsCore
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMIDI_$_NewsCore
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_NewsCore
- _objc_msgSend$allExposedItemIDs
- _objc_msgSend$firstExposureDateForItemID:
- _objc_msgSend$requiresBatchedSync
CStrings:
+ "%{public}@ detected a likely remote pruning of seen items"
+ "%{public}@ did fetch promoted headlines, tagFetchedAt=%{public}@, tagModifiedAt=%{public}@, tagPromotedArticleIDs=%{public}@, fetchedArticleIDs=%{public}@"
+ "%{public}@ did will finish early because promoted articles are expired"
+ "%{public}@ for zone %{public}@ will fetch changes, all=%{public}@, token=%{public}@"
+ "%{public}@ will resurrect %lu history items after server-side pruning"
+ "+[FCPrivateDataController requiresBatchedFirstSync]"
+ "-[FCPrivateZoneSyncManager initWithRecordZoneID:desiredKeys:requiresBatchedFirstSync:currentState:]"
+ "@\"NSArray\"32@0:8@\"NSArray\"16@\"NSDate\"24"
+ "Failed to lookup exposures by access date, error=%{public}@"
+ "_%lu"
+ "_requiresBatchedFirstSync"
+ "createdOrModifiedRecordIDs"
+ "deletedRecordIDs"
+ "pdfReplica"
+ "recordNamesPendingSaveToCloud"
+ "requiresBatchedFirstSync"
+ "stringByAppendingFormat:"
+ "subsetOfItemIDs:accessedSinceDate:"
+ "v%lu"
+ "willAccessArticleIDs:"
- "%{public}@ for zone %{public}@ will fetch changes with token %{public}@"
- "+[FCPrivateDataController requiresBatchedSync]"
- "-[FCPrivateZoneSyncManager initWithRecordZoneID:desiredKeys:requiresBatchedSync:currentState:]"
- "T0o72iqJnQRyx0E9YzkoKFA"
- "TFZX59DDWR22CqH8gMQt4Lw"
- "_requiresBatchedSync"
- "firstExposureDateForItemID:"
- "requiresBatchedSync"
- "willAcccessArticleIDs:"

```
