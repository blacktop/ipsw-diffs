## EventKit

> `/System/Library/Frameworks/EventKit.framework/Versions/A/EventKit`

```diff

-1976.0.0.0.0
-  __TEXT.__text: 0x1b8644
-  __TEXT.__objc_methlist: 0x15ac4
-  __TEXT.__cstring: 0xc2bf
-  __TEXT.__const: 0x47c0
-  __TEXT.__oslogstring: 0xee08
-  __TEXT.__gcc_except_tab: 0x3a54
+1976.2.2.0.0
+  __TEXT.__text: 0x1b9aac
+  __TEXT.__objc_methlist: 0x15c04
+  __TEXT.__cstring: 0xc20f
+  __TEXT.__const: 0x4810
+  __TEXT.__oslogstring: 0xf0c4
+  __TEXT.__gcc_except_tab: 0x3a58
   __TEXT.__dlopen_cstrs: 0x4e4
   __TEXT.__ustring: 0x1a0
   __TEXT.__swift5_typeref: 0x1988
-  __TEXT.__swift5_reflstr: 0x1261
+  __TEXT.__swift5_reflstr: 0x1271
   __TEXT.__swift5_assocty: 0x210
   __TEXT.__constg_swiftt: 0x1300
   __TEXT.__swift5_fieldmd: 0x11c8

   __TEXT.__swift_as_ret: 0xec
   __TEXT.__swift_as_cont: 0x1a8
   __TEXT.__swift5_mpenum: 0x60
-  __TEXT.__unwind_info: 0x6958
-  __TEXT.__eh_frame: 0x25e8
+  __TEXT.__unwind_info: 0x69b8
+  __TEXT.__eh_frame: 0x25e4
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x12d8
-  __DATA_CONST.__objc_classlist: 0x7b8
+  __DATA_CONST.__objc_classlist: 0x7c0
   __DATA_CONST.__objc_catlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x258
+  __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaef8
+  __DATA_CONST.__objc_selrefs: 0xaf88
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x518
+  __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_arraydata: 0x5d8
-  __DATA_CONST.__got: 0x1a20
-  __AUTH_CONST.__const: 0x82c0
+  __DATA_CONST.__got: 0x1a28
+  __AUTH_CONST.__const: 0x8310
   __AUTH_CONST.__cfstring: 0x9f40
-  __AUTH_CONST.__objc_const: 0x18730
+  __AUTH_CONST.__objc_const: 0x188e0
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_doubleobj: 0x100
-  __AUTH_CONST.__auth_got: 0x1238
-  __AUTH_CONST.__auth_ptr: 0x598
-  __AUTH.__objc_data: 0x3430
-  __AUTH.__data: 0xf08
-  __DATA.__objc_ivar: 0xd74
-  __DATA.__data: 0x2870
+  __AUTH_CONST.__auth_got: 0x1248
+  __AUTH_CONST.__auth_ptr: 0x5a8
+  __AUTH.__objc_data: 0x1db8
+  __AUTH.__data: 0x610
+  __DATA.__objc_ivar: 0xd80
+  __DATA.__data: 0x28e0
   __DATA.__bss: 0x45b0
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x1cc0
-  __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x788
+  __DATA_DIRTY.__objc_data: 0x3388
+  __DATA_DIRTY.__data: 0x928
+  __DATA_DIRTY.__bss: 0x7a0
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10817
-  Symbols:   17861
-  CStrings:  2698
+  Functions: 10846
+  Symbols:   17921
+  CStrings:  2704
 
Symbols:
+ +[EKAttachment _expandedArchiveTemporaryDirectoryRootForURL:]
+ +[EKAttachment _volumeIdentifierForURL:]
+ +[EKAutocompletePendingSearch _shouldReturnResultForEvent:considerReadonlyEvents:enforceRecencyCutoff:ignoreScheduledEvents:initialEvent:]
+ +[EKAutocompleteSearch pasteboardResultsFromProvider:ignoreScheduledEvents:]
+ +[EKEventStore _isSuggestedEvent:confirmed:uniqueKey:]
+ +[EKEventSuggestionGenerator eventSuggestionsFromPasteboardItemProvider:referenceDate:]
+ -[EKAttachment _mirroredTemporaryURLForExpandedArchiveContentsOfArchiveAtURL:]
+ -[EKAttachment localURLExpandingArchiveIfNeeded]
+ -[EKEventStore _suggestionsService]
+ -[EKEventStore gatherConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:fromInsertedObjects:deletedObjects:]
+ -[EKEventStore lastDatabaseCommitTimestamp]
+ -[EKEventStore notifySuggestionsOfConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:]
+ -[EKEventStore realAuthorizationStatusForEntityType:]
+ -[EKEventStore setSuggestionsServiceOverride:]
+ -[EKEventStore shouldNotifySuggestionsOfChangesToSuggestedEvents]
+ -[EKEventStore suggestionsServiceOverride]
+ -[EKFrozenReminderObject shouldCheckExistenceBeforeRefresh]
+ -[EKPersistentObject _shouldAllowUnloadingProperties]
+ -[EKPersistentObject shouldCheckExistenceBeforeRefresh]
+ -[EKWeakLinkedSuggestionsService .cxx_destruct]
+ -[EKWeakLinkedSuggestionsService confirmEventByRecordId:withCompletion:]
+ -[EKWeakLinkedSuggestionsService deleteEventByRecordId:withCompletion:]
+ -[EKWeakLinkedSuggestionsService eventFromUniqueId:withCompletion:]
+ -[EKWeakLinkedSuggestionsService init]
+ -[EKWeakLinkedSuggestionsService rejectEventByRecordId:withCompletion:]
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table113
+ GCC_except_table118
+ GCC_except_table122
+ GCC_except_table126
+ GCC_except_table130
+ GCC_except_table136
+ GCC_except_table140
+ GCC_except_table142
+ GCC_except_table145
+ GCC_except_table153
+ GCC_except_table157
+ GCC_except_table161
+ GCC_except_table163
+ GCC_except_table166
+ GCC_except_table191
+ GCC_except_table200
+ GCC_except_table202
+ GCC_except_table216
+ GCC_except_table219
+ GCC_except_table222
+ GCC_except_table257
+ GCC_except_table261
+ GCC_except_table263
+ GCC_except_table266
+ GCC_except_table269
+ GCC_except_table272
+ GCC_except_table274
+ GCC_except_table276
+ GCC_except_table280
+ GCC_except_table284
+ GCC_except_table293
+ GCC_except_table295
+ GCC_except_table297
+ GCC_except_table305
+ GCC_except_table308
+ GCC_except_table314
+ GCC_except_table352
+ GCC_except_table354
+ GCC_except_table357
+ GCC_except_table385
+ GCC_except_table389
+ GCC_except_table391
+ GCC_except_table393
+ GCC_except_table395
+ GCC_except_table397
+ GCC_except_table410
+ GCC_except_table414
+ GCC_except_table416
+ GCC_except_table423
+ GCC_except_table426
+ GCC_except_table429
+ GCC_except_table434
+ GCC_except_table446
+ GCC_except_table450
+ GCC_except_table455
+ GCC_except_table471
+ GCC_except_table476
+ GCC_except_table482
+ GCC_except_table492
+ GCC_except_table499
+ GCC_except_table502
+ GCC_except_table509
+ GCC_except_table535
+ GCC_except_table537
+ GCC_except_table569
+ GCC_except_table583
+ GCC_except_table590
+ GCC_except_table612
+ GCC_except_table629
+ GCC_except_table633
+ GCC_except_table652
+ GCC_except_table686
+ GCC_except_table688
+ GCC_except_table69
+ GCC_except_table690
+ GCC_except_table732
+ GCC_except_table736
+ GCC_except_table738
+ GCC_except_table74
+ GCC_except_table756
+ GCC_except_table758
+ GCC_except_table766
+ GCC_except_table773
+ GCC_except_table780
+ GCC_except_table788
+ GCC_except_table792
+ GCC_except_table794
+ GCC_except_table796
+ GCC_except_table802
+ GCC_except_table804
+ GCC_except_table806
+ GCC_except_table81
+ GCC_except_table822
+ GCC_except_table826
+ GCC_except_table86
+ OBJC_IVAR_$_EKEventStore._lastDatabaseCommitTimestamp
+ OBJC_IVAR_$_EKEventStore._suggestionsServiceOverride
+ OBJC_IVAR_$_EKWeakLinkedSuggestionsService._service
+ _NSURLVolumeIdentifierKey
+ _OBJC_CLASS_$_EKWeakLinkedSuggestionsService
+ _OBJC_METACLASS_$_EKWeakLinkedSuggestionsService
+ _OUTLINED_FUNCTION_34
+ _UnzipArchive
+ __95-[EKEventStore notifySuggestionsOfConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:]_block_invoke
+ __95-[EKEventStore notifySuggestionsOfConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:]_block_invoke_2
+ __OBJC_$_INSTANCE_METHODS_EKWeakLinkedSuggestionsService
+ __OBJC_$_INSTANCE_VARIABLES_EKWeakLinkedSuggestionsService
+ __OBJC_$_PROP_LIST_EKWeakLinkedSuggestionsService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EKSuggestionsServiceEventsProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EKSuggestionsServiceEventsProtocol
+ __OBJC_$_PROTOCOL_REFS_EKSuggestionsServiceEventsProtocol
+ __OBJC_CLASS_PROTOCOLS_$_EKWeakLinkedSuggestionsService
+ __OBJC_CLASS_RO_$_EKWeakLinkedSuggestionsService
+ __OBJC_LABEL_PROTOCOL_$_EKSuggestionsServiceEventsProtocol
+ __OBJC_METACLASS_RO_$_EKWeakLinkedSuggestionsService
+ __OBJC_PROTOCOL_$_EKSuggestionsServiceEventsProtocol
+ ___43-[EKEventStore lastDatabaseCommitTimestamp]_block_invoke
+ ___61+[EKAttachment _expandedArchiveTemporaryDirectoryRootForURL:]_block_invoke
+ ___95-[EKEventStore notifySuggestionsOfConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:]_block_invoke
+ ___95-[EKEventStore notifySuggestionsOfConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:]_block_invoke_2
+ ___block_descriptor_120_e8_32s40s48s56r64r72r80r88r96r104r112r_e124_v56?0i8"NSDictionary"12"NSDictionary"20"NSDictionary"28"CADInMemoryChangeTimestamp"36"CADInMemoryChangeTimestamp"44B52l
+ ___block_descriptor_40_e8_32s_e61_q24?0"CalSpotlightQueryResult"8"CalSpotlightQueryResult"16l
+ ___block_descriptor_72_e8_32s40s48r56r64r_e23_v32?0"NSDate"8Q16^B24l
+ ___copy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r
+ ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r
+ _expandedArchiveTemporaryDirectoryRootForURL:.cachedRootsByVolume
+ _expandedArchiveTemporaryDirectoryRootForURL:.onceToken
+ _objc_msgSend$CalTemporaryDirectoryAppropriateForURL:
+ _objc_msgSend$_expandedArchiveTemporaryDirectoryRootForURL:
+ _objc_msgSend$_isSuggestedEvent:confirmed:uniqueKey:
+ _objc_msgSend$_mirroredTemporaryURLForExpandedArchiveContentsOfArchiveAtURL:
+ _objc_msgSend$_shouldAllowUnloadingProperties
+ _objc_msgSend$_shouldReturnResultForEvent:considerReadonlyEvents:enforceRecencyCutoff:ignoreScheduledEvents:initialEvent:
+ _objc_msgSend$_suggestionsService
+ _objc_msgSend$_volumeIdentifierForURL:
+ _objc_msgSend$autoArchived
+ _objc_msgSend$currentProcessIsIntentsExtension
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$gatherConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:fromInsertedObjects:deletedObjects:
+ _objc_msgSend$localURLForArchivedData
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$notifySuggestionsOfConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:
+ _objc_msgSend$pasteboardResultsFromProvider:ignoreScheduledEvents:
+ _objc_msgSend$shouldCheckExistenceBeforeRefresh
+ _objc_msgSend$shouldNotifySuggestionsOfChangesToSuggestedEvents
+ _objc_msgSend$suggestionsServiceOverride
- +[EKEventStore _isConfirmedSuggestedEvent:uniqueKey:]
- -[EKEventStore _SGSuggestionsServiceClass]
- -[EKEventStore confirmSuggestedEvent:]
- -[EKEventStore lastDatabaseTimestamp]
- GCC_except_table102
- GCC_except_table107
- GCC_except_table111
- GCC_except_table116
- GCC_except_table121
- GCC_except_table128
- GCC_except_table134
- GCC_except_table138
- GCC_except_table144
- GCC_except_table149
- GCC_except_table151
- GCC_except_table160
- GCC_except_table162
- GCC_except_table165
- GCC_except_table186
- GCC_except_table190
- GCC_except_table199
- GCC_except_table208
- GCC_except_table215
- GCC_except_table218
- GCC_except_table256
- GCC_except_table260
- GCC_except_table262
- GCC_except_table265
- GCC_except_table268
- GCC_except_table271
- GCC_except_table273
- GCC_except_table275
- GCC_except_table279
- GCC_except_table283
- GCC_except_table292
- GCC_except_table294
- GCC_except_table296
- GCC_except_table304
- GCC_except_table307
- GCC_except_table313
- GCC_except_table316
- GCC_except_table351
- GCC_except_table353
- GCC_except_table356
- GCC_except_table384
- GCC_except_table388
- GCC_except_table390
- GCC_except_table392
- GCC_except_table394
- GCC_except_table396
- GCC_except_table401
- GCC_except_table409
- GCC_except_table413
- GCC_except_table415
- GCC_except_table422
- GCC_except_table425
- GCC_except_table428
- GCC_except_table433
- GCC_except_table445
- GCC_except_table453
- GCC_except_table475
- GCC_except_table486
- GCC_except_table500
- GCC_except_table503
- GCC_except_table510
- GCC_except_table513
- GCC_except_table539
- GCC_except_table541
- GCC_except_table573
- GCC_except_table587
- GCC_except_table596
- GCC_except_table609
- GCC_except_table623
- GCC_except_table630
- GCC_except_table649
- GCC_except_table68
- GCC_except_table683
- GCC_except_table685
- GCC_except_table687
- GCC_except_table729
- GCC_except_table73
- GCC_except_table733
- GCC_except_table735
- GCC_except_table753
- GCC_except_table755
- GCC_except_table76
- GCC_except_table760
- GCC_except_table770
- GCC_except_table777
- GCC_except_table785
- GCC_except_table789
- GCC_except_table791
- GCC_except_table793
- GCC_except_table799
- GCC_except_table80
- GCC_except_table801
- GCC_except_table803
- GCC_except_table819
- GCC_except_table823
- GCC_except_table99
- __37-[EKEventStore deleteSuggestedEvent:]_block_invoke_2
- __38-[EKEventStore confirmSuggestedEvent:]_block_invoke_2
- ___37-[EKEventStore deleteSuggestedEvent:]_block_invoke
- ___37-[EKEventStore deleteSuggestedEvent:]_block_invoke_2
- ___37-[EKEventStore lastDatabaseTimestamp]_block_invoke
- ___38-[EKEventStore confirmSuggestedEvent:]_block_invoke
- ___38-[EKEventStore confirmSuggestedEvent:]_block_invoke_2
- ___block_descriptor_112_e8_32s40s48r56r64r72r80r88r96r104r_e93_v48?0i8"NSDictionary"12"NSDictionary"20"NSDictionary"28"CADInMemoryChangeTimestamp"36B44l
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e23_v32?0"NSDate"8Q16^B24l
- ___copy_helper_block_e8_32s40s48r56r64r72r80r88r96r104r
- ___destroy_helper_block_e8_32s40s48r56r64r72r80r88r96r104r
- _objc_msgSend$_isConfirmedSuggestedEvent:uniqueKey:
- _objc_msgSend$confirmSuggestedEvent:
CStrings:
+ "%s: Not serializing %{public}@ to a draft because it has a never-committed co-commit sibling event that would be lost on restore"
+ "Found a deleted suggested event - notifying suggestions."
+ "Found a newly-confirmed suggested event - notifying suggestions."
+ "Found a rejected suggested event - notifying suggestions."
+ "Ignoring added suggested event that does not have a unique key"
+ "Ignoring removed suggested event that did not have a unique key"
+ "Invalidating new conference because event was deleted"
+ "Invalidating new conference because event was rolled back"
+ "Invalidating old conference because it is being replaced and was never committed"
+ "Not checking whether URL %@ needs invalidating because eventStore is nil"
+ "Not notifying suggestions about a confirmed event that moved from one account to another"
+ "Unable to determine volume identifier for %@: %@"
+ "Unable to expand attachment archive %@"
+ "confirmEventByRecordId failed with error %@"
+ "deleteEventByRecordId failed with error %@"
+ "q24@?0@\"CalSpotlightQueryResult\"8@\"CalSpotlightQueryResult\"16"
+ "rejectEventByRecordId failed with error %@"
+ "v56@?0i8@\"NSDictionary\"12@\"NSDictionary\"20@\"NSDictionary\"28@\"CADInMemoryChangeTimestamp\"36@\"CADInMemoryChangeTimestamp\"44B52"
- "%s - Notifying suggestions we have deleted previously confirmed event %@"
- "%s - Notifying suggestions we have ignored event %@"
- "%s - confirmEventByRecordId failed with error %@"
- "%s - deleteEventByRecordId failed with error %@"
- "%s - event has no suggestions key"
- "%s - rejectEventByRecordId failed with error %@"
- "-[EKEventStore _commitObjectsWithIdentifiers:error:]"
- "-[EKEventStore _commitObjectsWithIdentifiers:error:]_block_invoke_2"
- "-[EKEventStore confirmSuggestedEvent:]"
- "-[EKEventStore confirmSuggestedEvent:]_block_invoke_2"
- "-[EKEventStore deleteSuggestedEvent:]_block_invoke_2"
- "v48@?0i8@\"NSDictionary\"12@\"NSDictionary\"20@\"NSDictionary\"28@\"CADInMemoryChangeTimestamp\"36B44"
```
