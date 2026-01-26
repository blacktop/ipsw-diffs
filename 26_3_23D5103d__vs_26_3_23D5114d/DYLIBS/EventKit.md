## EventKit

> `/System/Library/Frameworks/EventKit.framework/EventKit`

```diff

-1934.2.3.0.0
-  __TEXT.__text: 0x14cae8
+1934.3.1.0.0
+  __TEXT.__text: 0x14cb54
   __TEXT.__auth_stubs: 0x1a40
-  __TEXT.__objc_methlist: 0x155ec
+  __TEXT.__objc_methlist: 0x15604
   __TEXT.__const: 0xe68
-  __TEXT.__cstring: 0xb98e
-  __TEXT.__oslogstring: 0xe2fe
+  __TEXT.__cstring: 0xb99e
+  __TEXT.__oslogstring: 0xe33e
   __TEXT.__gcc_except_tab: 0x3a2c
   __TEXT.__dlopen_cstrs: 0x398
   __TEXT.__ustring: 0x1a0

   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x5458
+  __TEXT.__unwind_info: 0x5450
   __TEXT.__eh_frame: 0x3a0
-  __TEXT.__objc_classname: 0x1b07
-  __TEXT.__objc_methname: 0x2eb5d
-  __TEXT.__objc_methtype: 0x4921
-  __TEXT.__objc_stubs: 0x210a0
+  __TEXT.__objc_classname: 0x1b0b
+  __TEXT.__objc_methname: 0x2eb92
+  __TEXT.__objc_methtype: 0x4972
+  __TEXT.__objc_stubs: 0x210c0
   __DATA_CONST.__got: 0x1778
-  __DATA_CONST.__const: 0x4788
+  __DATA_CONST.__const: 0x47b0
   __DATA_CONST.__objc_classlist: 0x760
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xabe0
+  __DATA_CONST.__objc_selrefs: 0xabe8
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x5d8
   __AUTH_CONST.__auth_got: 0xd30
   __AUTH_CONST.__const: 0x22a8
   __AUTH_CONST.__cfstring: 0x9d40
-  __AUTH_CONST.__objc_const: 0x17548
+  __AUTH_CONST.__objc_const: 0x175f0
   __AUTH_CONST.__objc_intobj: 0x6d8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0x1b8
   __AUTH_CONST.__objc_doubleobj: 0x100
   __AUTH.__objc_data: 0x2c30
   __AUTH.__data: 0x1e0
-  __DATA.__objc_ivar: 0xd10
+  __DATA.__objc_ivar: 0xd24
   __DATA.__data: 0x1ad0
   __DATA.__bss: 0x8a0
   __DATA.__common: 0x58

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: DD2D6088-E8A3-3367-BEB4-0907AE1FB581
-  Functions: 9002
-  Symbols:   27113
-  CStrings:  11568
+  UUID: 6F9A35B6-94B7-3C27-AF66-0634B0C7852B
+  Functions: 9005
+  Symbols:   27126
+  CStrings:  11579
 
Symbols:
+ -[EKEventStore batchedEventsMatchingPredicate:batchSize:error:handler:]
+ -[EKEventStore batchedEventsMatchingPredicate:batchSize:error:handler:].cold.1
+ -[EKPredicateSearch stepWithBatchSize:completed:error:]
+ GCC_except_table29
+ GCC_except_table626
+ GCC_except_table628
+ GCC_except_table630
+ _OBJC_IVAR_$_EKPredicateSearch._batchError
+ _OBJC_IVAR_$_EKPredicateSearch._batchSize
+ _OBJC_IVAR_$_EKPredicateSearch._batchingEnabled
+ _OBJC_IVAR_$_EKPredicateSearch._returnedFirstBatch
+ _OBJC_IVAR_$_EKPredicateSearch._returnedLastBatch
+ __OBJC_$_PROP_LIST_EKPredicateMonitor.133
+ ___80-[EKPredicateSearch _startProcessingWithCompletion:synchronous:processor:queue:]_block_invoke_2
+ ___block_descriptor_56_e8_32s40bs48bs_e23_v24?0i8"NSArray"12B20ls32l8s40l8s48l8
+ ___block_literal_global.74
+ ___block_literal_global.77
+ _objc_msgSend$CADDatabaseFetchEventsWithPredicate:fetchIdentifier:batchSize:reply:
+ _objc_msgSend$stepWithBatchSize:completed:error:
- -[EKEventStore predicateForRandomMasterEventsWithStartDate:endDate:needToHaveAttendee:needToHaveLocation:allDay:filteredOutTitles:limit:calendars:]
- GCC_except_table625
- GCC_except_table627
- GCC_except_table629
- __OBJC_$_PROP_LIST_EKPredicateMonitor.132
- ___block_literal_global.72
- ___block_literal_global.75
- _objc_msgSend$initWithEntityType:filters:calendars:limit:randomize:
CStrings:
+ "@36@0:8i16^B20^@28"
+ "B44@0:8@16i24^@28@?36"
+ "Batch returned no results but claimed to not be completed."
+ "CADDatabaseFetchEventsWithPredicate:fetchIdentifier:batchSize:reply:"
+ "_batchError"
+ "_batchSize"
+ "_batchingEnabled"
+ "_returnedFirstBatch"
+ "_returnedLastBatch"
+ "batchedEventsMatchingPredicate:batchSize:error:handler:"
+ "stepWithBatchSize:completed:error:"
+ "v24@?0i8@\"NSArray\"12B20"
+ "v40@0:8@\"NSPredicate\"16I24i28@?<v@?i@\"NSArray\"B>32"
+ "v40@0:8@16I24i28@?32"
+ "v52@0:8@\"NSPredicate\"16Q24Q32I40@?<v@?i>44"
+ "v52@0:8@16Q24Q32I40@?44"
- "@68@0:8@16@24B32B36B40@44q52@60"
- "initWithEntityType:filters:calendars:limit:randomize:"
- "predicateForRandomMasterEventsWithStartDate:endDate:needToHaveAttendee:needToHaveLocation:allDay:filteredOutTitles:limit:calendars:"
- "v52@0:8@\"NSPredicate\"16Q24Q32i40@?<v@?i>44"
- "v52@0:8@16Q24Q32i40@?44"

```
