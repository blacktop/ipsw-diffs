## CalendarDaemon

> `/System/Library/PrivateFrameworks/CalendarDaemon.framework/CalendarDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-1246.0.0.0.0
-  __TEXT.__text: 0x74f84
-  __TEXT.__objc_methlist: 0x6954
+1246.1.4.0.0
+  __TEXT.__text: 0x75964
+  __TEXT.__objc_methlist: 0x697c
   __TEXT.__cstring: 0x7520
   __TEXT.__const: 0x190
   __TEXT.__oslogstring: 0x8da3
-  __TEXT.__gcc_except_tab: 0x1b20
+  __TEXT.__gcc_except_tab: 0x1bcc
   __TEXT.__dlopen_cstrs: 0xc0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x22a8
+  __TEXT.__unwind_info: 0x22b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2200
+  __DATA_CONST.__const: 0x2250
   __DATA_CONST.__objc_classlist: 0x420
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x1c8

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2d0
   __DATA_CONST.__objc_arraydata: 0x350
-  __DATA_CONST.__got: 0xa70
+  __DATA_CONST.__got: 0xa98
   __AUTH_CONST.__const: 0x8c0
   __AUTH_CONST.__cfstring: 0x7e60
-  __AUTH_CONST.__objc_const: 0xce80
+  __AUTH_CONST.__objc_const: 0xcec0
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1c68
+  __AUTH_CONST.__auth_got: 0x1c70
   __AUTH.__objc_data: 0x1b80
   __AUTH.__data: 0xa50
-  __DATA.__objc_ivar: 0x860
+  __DATA.__objc_ivar: 0x868
   __DATA.__data: 0x1728
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xdc0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2347
-  Symbols:   6956
+  Functions: 2350
+  Symbols:   6970
   CStrings:  1818
 
Symbols:
+ -[CADInMemoryChangeTimestamp hash]
+ -[CADInMemoryChangeTimestamp isEqual:]
+ -[CADStatsCalendars accountTypeForStore:]
+ -[CADStatsReminders eventDictionaries]
+ -[CADXPCImplementation(CADDatabaseOperationGroup) insert:deletes:updates:insertedObjectIDMap:inDatabase:selfTimestamp:]
+ _ACAccountTypeIdentifierAppleAccount
+ _ACAccountTypeIdentifierExchange
+ _ACAccountTypeIdentifierGmail
+ _ACAccountTypeIdentifierYahoo
+ _CalDatabaseSaveWithOptionsAndOutSelfTimestamp
+ _OBJC_IVAR_$_CADStatsCalendarInfo._accountType
+ _OBJC_IVAR_$_CADStatsCalendarInfo._storeType
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr104l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96s104r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r104l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_64_e8_32s40s48r56r_e352_v28?0i8"NSArray"12^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}20ls32l8s40l8r48l8r56l8
+ ___block_descriptor_72_e8_32s40s48s56s64r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40r48r56r64r72r_e76_v40?0i8"NSDictionary"12"NSDictionary"20"CADInMemoryChangeTimestamp"28B36lr40l8r48l8r56l8r64l8s32l8r72l8
+ ___block_descriptor_92_e8_32s40s48s56s64s72s80r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ _kCalDatabaseSaveOptionsDefaultOptions
+ _objc_msgSend$accountTypeForStore:
+ _objc_msgSend$insert:deletes:updates:insertedObjectIDMap:inDatabase:selfTimestamp:
- -[CADStatsReminders reminderDictionaries]
- -[CADXPCImplementation(CADDatabaseOperationGroup) insert:deletes:updates:insertedObjectIDMap:inDatabase:]
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88s96r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12ls32l8s40l8s48l8s56l8r96l8s64l8s72l8s80l8s88l8
- ___block_descriptor_64_e8_32r40r48r56r_e76_v40?0i8"NSDictionary"12"NSDictionary"20"CADInMemoryChangeTimestamp"28B36lr32l8r40l8r48l8r56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72r_e340_v20?0i8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}12lr72l8s32l8s40l8s48l8s56l8s64l8
- _objc_msgSend$insert:deletes:updates:insertedObjectIDMap:inDatabase:
CStrings:
+ "integration:reminders"
- "integration.reminders"
```
