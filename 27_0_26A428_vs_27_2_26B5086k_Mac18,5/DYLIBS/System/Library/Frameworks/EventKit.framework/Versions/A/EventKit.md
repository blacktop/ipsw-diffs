## EventKit

> `/System/Library/Frameworks/EventKit.framework/Versions/A/EventKit`

```diff

-1976.0.0.0.0
-  __TEXT.__text: 0x1ada6c
-  __TEXT.__objc_methlist: 0x15ac4
-  __TEXT.__cstring: 0xc2bf
-  __TEXT.__const: 0x47c0
-  __TEXT.__oslogstring: 0xee08
-  __TEXT.__gcc_except_tab: 0x3a54
+1976.1.3.0.0
+  __TEXT.__text: 0x1aea54
+  __TEXT.__objc_methlist: 0x15b9c
+  __TEXT.__cstring: 0xc20f
+  __TEXT.__const: 0x4810
+  __TEXT.__oslogstring: 0xefe4
+  __TEXT.__gcc_except_tab: 0x3a2c
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
-  __TEXT.__unwind_info: 0x85f0
-  __TEXT.__eh_frame: 0x25f0
+  __TEXT.__unwind_info: 0x8628
+  __TEXT.__eh_frame: 0x2664
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
+  __DATA_CONST.__objc_selrefs: 0xaf48
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x518
+  __DATA_CONST.__objc_superrefs: 0x520
   __DATA_CONST.__objc_arraydata: 0x5d8
   __DATA_CONST.__got: 0x1a20
-  __AUTH_CONST.__const: 0x82c0
+  __AUTH_CONST.__const: 0x82f0
   __AUTH_CONST.__cfstring: 0x9f40
-  __AUTH_CONST.__objc_const: 0x18730
+  __AUTH_CONST.__objc_const: 0x188d0
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH_CONST.__auth_got: 0x1238
-  __AUTH.__objc_data: 0x3430
+  __AUTH.__objc_data: 0x3480
   __AUTH.__data: 0xf08
-  __DATA.__objc_ivar: 0xd74
-  __DATA.__data: 0x2870
+  __DATA.__objc_ivar: 0xd80
+  __DATA.__data: 0x28e0
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1cc0
   __DATA_DIRTY.__data: 0x20

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10817
-  Symbols:   17861
-  CStrings:  2698
+  Functions: 10835
+  Symbols:   17898
+  CStrings:  2701
 
Symbols:
+ +[EKAutocompletePendingSearch _shouldReturnResultForEvent:considerReadonlyEvents:enforceRecencyCutoff:ignoreScheduledEvents:initialEvent:]
+ +[EKAutocompleteSearch pasteboardResultsFromProvider:ignoreScheduledEvents:]
+ +[EKEventStore _isSuggestedEvent:confirmed:uniqueKey:]
+ +[EKEventSuggestionGenerator eventSuggestionsFromPasteboardItemProvider:referenceDate:]
+ -[EKEventStore _suggestionsService]
+ -[EKEventStore gatherConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:fromInsertedObjects:deletedObjects:]
+ -[EKEventStore lastDatabaseCommitTimestamp]
+ -[EKEventStore notifySuggestionsOfConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:]
+ -[EKEventStore setSuggestionsServiceOverride:]
+ -[EKEventStore shouldNotifySuggestionsOfChangesToSuggestedEvents]
+ -[EKEventStore suggestionsServiceOverride]
+ -[EKWeakLinkedSuggestionsService .cxx_destruct]
+ -[EKWeakLinkedSuggestionsService confirmEventByRecordId:withCompletion:]
+ -[EKWeakLinkedSuggestionsService deleteEventByRecordId:withCompletion:]
+ -[EKWeakLinkedSuggestionsService eventFromUniqueId:withCompletion:]
+ -[EKWeakLinkedSuggestionsService init]
+ -[EKWeakLinkedSuggestionsService rejectEventByRecordId:withCompletion:]
+ GCC_except_table470
+ GCC_except_table479
+ GCC_except_table481
+ GCC_except_table491
+ GCC_except_table495
+ GCC_except_table498
+ GCC_except_table501
+ GCC_except_table505
+ GCC_except_table508
+ GCC_except_table534
+ GCC_except_table536
+ GCC_except_table568
+ GCC_except_table582
+ GCC_except_table589
+ GCC_except_table611
+ GCC_except_table625
+ GCC_except_table628
+ GCC_except_table632
+ GCC_except_table651
+ GCC_except_table689
+ GCC_except_table731
+ GCC_except_table737
+ GCC_except_table757
+ GCC_except_table762
+ GCC_except_table765
+ GCC_except_table772
+ GCC_except_table779
+ GCC_except_table787
+ GCC_except_table795
+ GCC_except_table805
+ GCC_except_table821
+ GCC_except_table825
+ OBJC_IVAR_$_EKEventStore._lastDatabaseCommitTimestamp
+ OBJC_IVAR_$_EKEventStore._suggestionsServiceOverride
+ OBJC_IVAR_$_EKWeakLinkedSuggestionsService._service
+ _OBJC_CLASS_$_EKWeakLinkedSuggestionsService
+ _OBJC_METACLASS_$_EKWeakLinkedSuggestionsService
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
+ ___95-[EKEventStore notifySuggestionsOfConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:]_block_invoke
+ ___95-[EKEventStore notifySuggestionsOfConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:]_block_invoke_2
+ ___block_descriptor_120_e8_32s40s48s56r64r72r80r88r96r104r112r_e124_v56?0i8"NSDictionary"12"NSDictionary"20"NSDictionary"28"CADInMemoryChangeTimestamp"36"CADInMemoryChangeTimestamp"44B52l
+ ___block_descriptor_40_e8_32s_e61_q24?0"CalSpotlightQueryResult"8"CalSpotlightQueryResult"16l
+ ___block_descriptor_72_e8_32s40s48r56r64r_e23_v32?0"NSDate"8Q16^B24l
+ ___copy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r
+ ___destroy_helper_block_e8_32s40s48s56r64r72r80r88r96r104r112r
+ _objc_msgSend$_isSuggestedEvent:confirmed:uniqueKey:
+ _objc_msgSend$_shouldReturnResultForEvent:considerReadonlyEvents:enforceRecencyCutoff:ignoreScheduledEvents:initialEvent:
+ _objc_msgSend$_suggestionsService
+ _objc_msgSend$currentProcessIsIntentsExtension
+ _objc_msgSend$gatherConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:fromInsertedObjects:deletedObjects:
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$notifySuggestionsOfConfirmedSuggestions:rejectedSuggestions:deletedSuggestions:
+ _objc_msgSend$pasteboardResultsFromProvider:ignoreScheduledEvents:
+ _objc_msgSend$shouldNotifySuggestionsOfChangesToSuggestedEvents
+ _objc_msgSend$suggestionsServiceOverride
- +[EKEventStore _isConfirmedSuggestedEvent:uniqueKey:]
- -[EKEventStore _SGSuggestionsServiceClass]
- -[EKEventStore confirmSuggestedEvent:]
- -[EKEventStore lastDatabaseTimestamp]
- GCC_except_table480
- GCC_except_table486
- GCC_except_table496
- GCC_except_table500
- GCC_except_table503
- GCC_except_table506
- GCC_except_table510
- GCC_except_table513
- GCC_except_table539
- GCC_except_table541
- GCC_except_table573
- GCC_except_table587
- GCC_except_table596
- GCC_except_table609
- GCC_except_table623
- GCC_except_table626
- GCC_except_table630
- GCC_except_table649
- GCC_except_table683
- GCC_except_table729
- GCC_except_table733
- GCC_except_table753
- GCC_except_table760
- GCC_except_table763
- GCC_except_table770
- GCC_except_table777
- GCC_except_table785
- GCC_except_table789
- GCC_except_table799
- GCC_except_table819
- GCC_except_table823
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
