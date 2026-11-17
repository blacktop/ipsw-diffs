## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

```diff

-1246.2.1.0.0
-  __TEXT.__text: 0x75a48
-  __TEXT.__objc_methlist: 0x697c
+1246.3.4.0.0
+  __TEXT.__text: 0x75b88
+  __TEXT.__objc_methlist: 0x69a4
   __TEXT.__cstring: 0x7520
-  __TEXT.__const: 0x190
+  __TEXT.__const: 0x1a0
   __TEXT.__oslogstring: 0x8ddb
   __TEXT.__gcc_except_tab: 0x1bcc
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x22b8
+  __TEXT.__unwind_info: 0x22c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3538
+  __DATA_CONST.__objc_selrefs: 0x3558
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x350

   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1c80
+  __AUTH_CONST.__auth_got: 0x1c98
   __AUTH.__objc_data: 0x8c0
   __AUTH.__data: 0xa50
   __DATA.__objc_ivar: 0x868

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2350
-  Symbols:   5614
+  Functions: 2354
+  Symbols:   5622
   CStrings:  1819
 
Symbols:
+ +[CADSpotlightIndexer _mainOccurrenceExistsForEvent:isRecurring:]
+ -[CADSpotlightIndexer _performContinueReindexWithState:]
+ -[CADSpotlightIndexer _performIncrementalUpdate]
+ -[CADSpotlightIndexer _reindexEventsWithUUIDs:calendarsWithUUIDs:requestedItemCount:]
+ GCC_except_table106
+ GCC_except_table35
+ GCC_except_table47
+ GCC_except_table92
+ _CalCalendarItemCopyExceptionDatesForRecurrences
+ _CalDatabaseCopyAttendeeWithUID
+ _CalEventCopySelfAttendee
+ ___48-[CADSpotlightIndexer _performIncrementalUpdate]_block_invoke
+ ___56-[CADSpotlightIndexer _performContinueReindexWithState:]_block_invoke
+ ___85-[CADSpotlightIndexer _reindexEventsWithUUIDs:calendarsWithUUIDs:requestedItemCount:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s_e8_B12?0B8ls32l8s40l8s48l8s56l8
+ _kCADSpotlightIndexerMediumReindexRetryInterval
- GCC_except_table102
- GCC_except_table30
- GCC_except_table45
- GCC_except_table88
- ___41-[CADSpotlightIndexer _incrementalUpdate]_block_invoke
- ___49-[CADSpotlightIndexer _continueReindexWithState:]_block_invoke
- ___99-[CADSpotlightIndexer reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:]_block_invoke_2
- ___block_descriptor_64_e8_32s40s48s56s_e344_v28?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12^B20ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s_e8_B12?0B8ls32l8s40l8s48l8s56l8s64l8
```
