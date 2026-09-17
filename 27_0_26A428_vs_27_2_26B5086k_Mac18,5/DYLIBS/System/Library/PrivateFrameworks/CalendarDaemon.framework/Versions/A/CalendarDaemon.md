## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/Versions/A/CalendarDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1246.0.0.0.0
-  __TEXT.__text: 0x78e98
-  __TEXT.__objc_methlist: 0x679c
+1246.1.4.0.0
+  __TEXT.__text: 0x79a4c
+  __TEXT.__objc_methlist: 0x67c4
   __TEXT.__cstring: 0x7447
   __TEXT.__const: 0x190
   __TEXT.__oslogstring: 0x8bab
-  __TEXT.__gcc_except_tab: 0x1b64
+  __TEXT.__gcc_except_tab: 0x1c0c
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x22d8
+  __TEXT.__unwind_info: 0x22f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0x350
-  __DATA_CONST.__got: 0x9e0
-  __AUTH_CONST.__const: 0x2790
+  __DATA_CONST.__got: 0xa08
+  __AUTH_CONST.__const: 0x27c0
   __AUTH_CONST.__cfstring: 0x7ce0
-  __AUTH_CONST.__objc_const: 0xcb18
+  __AUTH_CONST.__objc_const: 0xcb58
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1af8
+  __AUTH_CONST.__auth_got: 0x1b00
   __AUTH.__objc_data: 0x1a90
   __AUTH.__data: 0xa50
-  __DATA.__objc_ivar: 0x830
+  __DATA.__objc_ivar: 0x838
   __DATA.__data: 0x16c8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xe10

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2371
-  Symbols:   6863
+  Functions: 2378
+  Symbols:   6880
   CStrings:  1796
 
Symbols:
+ -[CADInMemoryChangeTimestamp hash]
+ -[CADInMemoryChangeTimestamp isEqual:]
+ -[CADStatsCalendars accountTypeForStore:]
+ -[CADStatsReminders eventDictionaries]
+ -[CADXPCImplementation(CADDatabaseOperationGroup) insert:deletes:updates:insertedObjectIDMap:inDatabase:selfTimestamp:]
+ GCC_except_table106
+ GCC_except_table118
+ GCC_except_table121
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table91
+ OBJC_IVAR_$_CADStatsCalendarInfo._accountType
+ OBJC_IVAR_$_CADStatsCalendarInfo._storeType
+ _ACAccountTypeIdentifierAppleAccount
+ _ACAccountTypeIdentifierExchange
+ _ACAccountTypeIdentifierGmail
+ _ACAccountTypeIdentifierYahoo
+ _CalDatabaseSaveWithOptionsAndOutSelfTimestamp
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12l
+ ___block_descriptor_64_e8_32s40s48r56r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20l
+ ___block_descriptor_80_e8_32s40r48r56r64r72r_e76_v40?0i8"NSDictionary"12"NSDictionary"20"CADInMemoryChangeTimestamp"28B36l
+ ___block_descriptor_92_e8_32s40s48s56s64s72s80r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12l
+ ___copy_helper_block_e8_32s40r48r56r64r72r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104r
+ ___destroy_helper_block_e8_32s40r48r56r64r72r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104r
+ _kCalDatabaseSaveOptionsDefaultOptions
+ _objc_msgSend$accountTypeForStore:
+ _objc_msgSend$insert:deletes:updates:insertedObjectIDMap:inDatabase:selfTimestamp:
- -[CADStatsReminders reminderDictionaries]
- -[CADXPCImplementation(CADDatabaseOperationGroup) insert:deletes:updates:insertedObjectIDMap:inDatabase:]
- GCC_except_table104
- GCC_except_table114
- GCC_except_table117
- GCC_except_table120
- GCC_except_table122
- GCC_except_table89
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12l
- ___block_descriptor_64_e8_32r40r48r56r_e76_v40?0i8"NSDictionary"12"NSDictionary"20"CADInMemoryChangeTimestamp"28B36l
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96r
- _objc_msgSend$insert:deletes:updates:insertedObjectIDMap:inDatabase:
CStrings:
+ "integration:reminders"
- "integration.reminders"
```
