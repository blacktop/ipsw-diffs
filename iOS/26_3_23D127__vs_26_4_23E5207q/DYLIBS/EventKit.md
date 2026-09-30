## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1934.3.1.0.0
-  __TEXT.__text: 0x14cb54
-  __TEXT.__auth_stubs: 0x1a40
-  __TEXT.__objc_methlist: 0x15604
-  __TEXT.__const: 0xe68
-  __TEXT.__cstring: 0xb99e
-  __TEXT.__oslogstring: 0xe33e
-  __TEXT.__gcc_except_tab: 0x3a2c
+1934.4.7.0.0
+  __TEXT.__text: 0x1587a4
+  __TEXT.__auth_stubs: 0x19e0
+  __TEXT.__objc_methlist: 0x15644
+  __TEXT.__const: 0xe58
+  __TEXT.__cstring: 0xb49f
+  __TEXT.__oslogstring: 0xe36e
+  __TEXT.__gcc_except_tab: 0x3954
   __TEXT.__dlopen_cstrs: 0x398
   __TEXT.__ustring: 0x1a0
   __TEXT.__swift5_typeref: 0x590

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x5450
-  __TEXT.__eh_frame: 0x3a0
-  __TEXT.__objc_classname: 0x1b0b
-  __TEXT.__objc_methname: 0x2eb92
-  __TEXT.__objc_methtype: 0x4972
-  __TEXT.__objc_stubs: 0x210c0
-  __DATA_CONST.__got: 0x1778
+  __TEXT.__unwind_info: 0x5b78
+  __TEXT.__eh_frame: 0x348
+  __TEXT.__objc_classname: 0x1ca9
+  __TEXT.__objc_methname: 0x2ef14
+  __TEXT.__objc_methtype: 0x49d6
+  __TEXT.__objc_stubs: 0x21420
+  __DATA_CONST.__got: 0x1788
   __DATA_CONST.__const: 0x47b0
   __DATA_CONST.__objc_classlist: 0x760
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xabe8
+  __DATA_CONST.__objc_selrefs: 0xac10
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x5d8
-  __AUTH_CONST.__auth_got: 0xd30
+  __AUTH_CONST.__auth_got: 0xd00
   __AUTH_CONST.__const: 0x22a8
   __AUTH_CONST.__cfstring: 0x9d40
-  __AUTH_CONST.__objc_const: 0x175f0
+  __AUTH_CONST.__objc_const: 0x17600
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x1b8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 61596F65-06F3-313C-ADF4-5142143B7022
-  Functions: 9005
-  Symbols:   27126
-  CStrings:  11579
+  UUID: F770F909-79A3-31AC-99F4-AA023C68114E
+  Functions: 9053
+  Symbols:   27437
+  CStrings:  11566
 
Symbols:
+ +[EKSpotlightSearch reindexingInProgress]
+ -[EKBirthdayListener incrementalUpdateWithContext:].cold.3
+ -[EKEvent passthroughSpotlightAttributes]
+ -[EKEvent setPassthroughSpotlightAttributes:]
+ -[EKEventStore _trimCaches]
+ -[EKEventStore partialReset]
+ GCC_except_table398
+ GCC_except_table433
+ GCC_except_table438
+ GCC_except_table469
+ GCC_except_table535
+ GCC_except_table540
+ GCC_except_table549
+ GCC_except_table556
+ GCC_except_table565
+ GCC_except_table579
+ GCC_except_table585
+ GCC_except_table600
+ GCC_except_table632
+ GCC_except_table634
+ GCC_except_table680
+ GCC_except_table682
+ GCC_except_table696
+ GCC_except_table698
+ GCC_except_table703
+ GCC_except_table706
+ GCC_except_table713
+ GCC_except_table720
+ GCC_except_table732
+ GCC_except_table734
+ GCC_except_table742
+ GCC_except_table744
+ GCC_except_table756
+ GCC_except_table818
+ GCC_except_table847
+ _OBJC_CLASS_$_CADSpotlightDefaults
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ ___27-[EKEventStore _trimCaches]_block_invoke
+ ___27-[EKEventStore _trimCaches]_block_invoke_2
+ ___99-[EKSpotlightSearch initWithSearchWithCSQuery:inStore:inCalendars:resultHandler:completionHandler:]_block_invoke.15
+ ___block_descriptor_56_e8_32s40s48r_e21_v24?0"NSArray"8^B16ls32l8s40l8r48l8
+ _kCalEventPassthroughSpotlightAttributes
+ _objc_msgSend$_trimCaches
+ _objc_msgSend$batchedEventsMatchingPredicate:batchSize:error:handler:
+ _objc_msgSend$beginSearchForTerm:
+ _objc_msgSend$cachedMeltedObjects
+ _objc_msgSend$conferenceRoomForSource:
+ _objc_msgSend$conferenceRoomSearchResults
+ _objc_msgSend$contactsSearchResults
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$eventsSearchResults
+ _objc_msgSend$initWithBool:
+ _objc_msgSend$initWithUnsignedInteger:
+ _objc_msgSend$insertedPersistentObjectWithEntityName:
+ _objc_msgSend$isPendingInsert
+ _objc_msgSend$mapCompletionSearchResults
+ _objc_msgSend$partialReset
+ _objc_msgSend$persistentObjectWithEntityName:
+ _objc_msgSend$recentsSearchResults
+ _objc_msgSend$reindexingInProgress
+ _objc_msgSend$resultsPending
+ _objc_msgSend$searchFor:onSource:withContext:
+ _objc_msgSend$setCachedMeltedObjects:
+ _objc_msgSend$setFindPeople:
+ _objc_msgSend$setFindRecents:
+ _objc_msgSend$setLocalCustomObject:forKey:
+ _objc_msgSend$setSupportedSearchTypes:
+ _objc_msgSend$setUseDirectorySearch:
+ _objc_msgSend$textualSearchResults
+ _objc_msgSend$updatedPropertiesWithOnlyPersistentObjects
+ _objc_msgSend$virtualObjectIDWithEntityType:
+ _swift_bridgeObjectRelease_n
- GCC_except_table393
- GCC_except_table396
- GCC_except_table431
- GCC_except_table436
- GCC_except_table467
- GCC_except_table531
- GCC_except_table538
- GCC_except_table545
- GCC_except_table552
- GCC_except_table561
- GCC_except_table575
- GCC_except_table577
- GCC_except_table596
- GCC_except_table626
- GCC_except_table628
- GCC_except_table672
- GCC_except_table678
- GCC_except_table692
- GCC_except_table694
- GCC_except_table699
- GCC_except_table702
- GCC_except_table709
- GCC_except_table716
- GCC_except_table724
- GCC_except_table726
- GCC_except_table736
- GCC_except_table738
- GCC_except_table748
- GCC_except_table814
- GCC_except_table843
- ___51-[EKBirthdayListener incrementalUpdateWithContext:]_block_invoke.cold.4
- ___51-[EKBirthdayListener incrementalUpdateWithContext:]_block_invoke.cold.5
- ___99-[EKSpotlightSearch initWithSearchWithCSQuery:inStore:inCalendars:resultHandler:completionHandler:]_block_invoke.14
- ___block_descriptor_48_e8_32s40s_e21_v24?0"EKEvent"8^B16ls32l8s40l8
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$enumerateEventsMatchingPredicate:usingBlock:
- _objc_msgSend$isObjectInserted:
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _swift_bridgeObjectRetain_n
CStrings:
+ "@36@0:8Q16@24B32"
+ "Error finding existing birthday events: %@"
+ "_trimCaches"
+ "partialReset"
+ "passthroughSpotlightAttributes"
+ "reindexingInProgress"
+ "setPassthroughSpotlightAttributes:"
+ "v24@?0@\"NSArray\"8^B16"
- "@32@0:8i16@20B28"
- "@44@0:8i16@20@28B36B40"
- "v24@?0@\"EKEvent\"8^B16"

```
