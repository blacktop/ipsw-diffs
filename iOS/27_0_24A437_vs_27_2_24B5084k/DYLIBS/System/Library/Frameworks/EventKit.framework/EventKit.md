## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1976.0.100.0.0
-  __TEXT.__text: 0x1989dc
-  __TEXT.__objc_methlist: 0x15ac4
-  __TEXT.__cstring: 0xbe6f
-  __TEXT.__const: 0x4820
-  __TEXT.__oslogstring: 0xefd8
-  __TEXT.__gcc_except_tab: 0x3978
+1976.1.3.0.0
+  __TEXT.__text: 0x1997a8
+  __TEXT.__objc_methlist: 0x15b9c
+  __TEXT.__cstring: 0xbdbf
+  __TEXT.__const: 0x4870
+  __TEXT.__oslogstring: 0xf1b4
+  __TEXT.__gcc_except_tab: 0x3950
   __TEXT.__dlopen_cstrs: 0x400
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
-  __TEXT.__unwind_info: 0x8388
-  __TEXT.__eh_frame: 0x2620
+  __TEXT.__unwind_info: 0x83a8
+  __TEXT.__eh_frame: 0x261c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x48e0
-  __DATA_CONST.__objc_classlist: 0x7b0
+  __DATA_CONST.__const: 0x4908
+  __DATA_CONST.__objc_classlist: 0x7b8
   __DATA_CONST.__objc_catlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x250
+  __DATA_CONST.__objc_protolist: 0x258
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xae98
+  __DATA_CONST.__objc_selrefs: 0xaee8
   __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x530
+  __DATA_CONST.__objc_superrefs: 0x538
   __DATA_CONST.__objc_arraydata: 0x5d8
   __DATA_CONST.__got: 0x1a50
   __AUTH_CONST.__const: 0x4500
   __AUTH_CONST.__cfstring: 0x9ec0
-  __AUTH_CONST.__objc_const: 0x18628
+  __AUTH_CONST.__objc_const: 0x187c8
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH_CONST.__auth_got: 0x1428
-  __AUTH.__objc_data: 0x34d0
+  __AUTH.__objc_data: 0x3520
   __AUTH.__data: 0xf08
-  __DATA.__objc_ivar: 0xd7c
-  __DATA.__data: 0x2890
+  __DATA.__objc_ivar: 0xd88
+  __DATA.__data: 0x28e0
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1bd0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10688
-  Symbols:   17573
-  CStrings:  2669
+  Functions: 10703
+  Symbols:   17610
+  CStrings:  2672
 
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
+ GCC_except_table438
+ GCC_except_table447
+ GCC_except_table449
+ GCC_except_table459
+ GCC_except_table463
+ GCC_except_table466
+ GCC_except_table469
+ GCC_except_table473
+ GCC_except_table476
+ GCC_except_table502
+ GCC_except_table504
+ GCC_except_table536
+ GCC_except_table550
+ GCC_except_table573
+ GCC_except_table587
+ GCC_except_table590
+ GCC_except_table594
+ GCC_except_table609
+ GCC_except_table645
+ GCC_except_table687
+ GCC_except_table693
+ GCC_except_table711
+ GCC_except_table716
+ GCC_except_table719
+ GCC_except_table726
+ GCC_except_table733
+ GCC_except_table741
+ GCC_except_table749
+ GCC_except_table759
+ GCC_except_table768
+ GCC_except_table772
+ _OBJC_CLASS_$_EKWeakLinkedSuggestionsService
+ _OBJC_IVAR_$_EKEventStore._lastDatabaseCommitTimestamp
+ _OBJC_IVAR_$_EKEventStore._suggestionsServiceOverride
+ _OBJC_IVAR_$_EKWeakLinkedSuggestionsService._service
+ _OBJC_METACLASS_$_EKWeakLinkedSuggestionsService
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
+ ___block_descriptor_120_e8_32s40s48s56r64r72r80r88r96r104r112r_e124_v56?0i8"NSDictionary"12"NSDictionary"20"NSDictionary"28"CADInMemoryChangeTimestamp"36"CADInMemoryChangeTimestamp"44B52lr56l8r64l8s32l8s40l8r72l8r80l8r88l8r96l8r104l8r112l8s48l8
+ ___block_descriptor_40_e8_32s_e61_q24?0"CalSpotlightQueryResult"8"CalSpotlightQueryResult"16ls32l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e23_v32?0"NSDate"8Q16^B24ls32l8r48l8r56l8s40l8r64l8
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
- GCC_except_table448
- GCC_except_table452
- GCC_except_table454
- GCC_except_table464
- GCC_except_table468
- GCC_except_table474
- GCC_except_table478
- GCC_except_table481
- GCC_except_table507
- GCC_except_table509
- GCC_except_table541
- GCC_except_table562
- GCC_except_table571
- GCC_except_table585
- GCC_except_table588
- GCC_except_table592
- GCC_except_table607
- GCC_except_table639
- GCC_except_table685
- GCC_except_table689
- GCC_except_table707
- GCC_except_table714
- GCC_except_table717
- GCC_except_table724
- GCC_except_table731
- GCC_except_table739
- GCC_except_table743
- GCC_except_table753
- GCC_except_table766
- GCC_except_table770
- ___37-[EKEventStore deleteSuggestedEvent:]_block_invoke
- ___37-[EKEventStore deleteSuggestedEvent:]_block_invoke_2
- ___37-[EKEventStore lastDatabaseTimestamp]_block_invoke
- ___38-[EKEventStore confirmSuggestedEvent:]_block_invoke
- ___38-[EKEventStore confirmSuggestedEvent:]_block_invoke_2
- ___block_descriptor_112_e8_32s40s48r56r64r72r80r88r96r104r_e93_v48?0i8"NSDictionary"12"NSDictionary"20"NSDictionary"28"CADInMemoryChangeTimestamp"36B44lr48l8r56l8s32l8s40l8r64l8r72l8r80l8r88l8r96l8r104l8
- ___block_descriptor_80_e8_32s40s48s56r64r72r_e23_v32?0"NSDate"8Q16^B24ls32l8s40l8r56l8r64l8s48l8r72l8
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
