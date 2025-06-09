## DataAccess

> `/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess`

```diff

-2673.6.1.0.0
-  __TEXT.__text: 0x3cf74
-  __TEXT.__auth_stubs: 0x10a0
-  __TEXT.__objc_methlist: 0x4854
+2690.0.0.0.0
+  __TEXT.__text: 0x3cea4
+  __TEXT.__auth_stubs: 0x1090
+  __TEXT.__objc_methlist: 0x482c
   __TEXT.__const: 0x180
   __TEXT.__gcc_except_tab: 0x18cc
-  __TEXT.__cstring: 0x32af
-  __TEXT.__oslogstring: 0x5370
+  __TEXT.__cstring: 0x32ab
+  __TEXT.__oslogstring: 0x531e
   __TEXT.__dlopen_cstrs: 0x102
-  __TEXT.__unwind_info: 0xf50
+  __TEXT.__unwind_info: 0xf48
   __TEXT.__objc_classname: 0x7a0
-  __TEXT.__objc_methname: 0xb97a
-  __TEXT.__objc_methtype: 0x1b90
+  __TEXT.__objc_methname: 0xb9d6
+  __TEXT.__objc_methtype: 0x1ba6
   __TEXT.__objc_stubs: 0x7700
   __DATA_CONST.__got: 0x750
   __DATA_CONST.__const: 0xb50

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2da8
+  __DATA_CONST.__objc_selrefs: 0x2d98
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x860
+  __AUTH_CONST.__auth_got: 0x858
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x31a0
-  __AUTH_CONST.__objc_const: 0x71b8
+  __AUTH_CONST.__objc_const: 0x7220
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_ivar: 0x350
+  __DATA.__objc_ivar: 0x358
   __DATA.__data: 0x420
-  __DATA.__bss: 0x180
+  __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__bss: 0x114
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12CE81BC-F9F3-3762-9782-57CF41A9BA26
-  Functions: 1600
-  Symbols:   5686
-  CStrings:  3356
+  UUID: 3E6C5BA2-1B8E-3A16-8529-26204DEA4736
+  Functions: 1597
+  Symbols:   5678
+  CStrings:  3357
 
Symbols:
+ -[DAAccount _webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]
+ -[DAAccount webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]
+ -[DACalDBHelper _effectiveAndCanonicalMainDatabasePath]
+ -[DACalDBHelper initWithDatabaseInitOptions:mainDatabasePath:containerProvider:]
+ -[DALocalDBHelper initWithCalendarMainDatabasePath:containerProvider:]
+ _OBJC_IVAR_$_DACalDBHelper._containerProviderOverride
+ _OBJC_IVAR_$_DACalDBHelper._mainDatabasePathOverride
+ __OBJC_$_CLASS_PROP_LIST_DABabysitter
+ ___73-[DAAccount webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]_block_invoke
+ ___74-[DAAccount _webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]_block_invoke
+ ___74-[DAAccount _webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e669_v24?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}16ls32l8
+ ___block_descriptor_48_e8_32s40s_e669_v24?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}*IIiQBBBBBBB}16ls32l8s40l8
+ ___block_literal_global.531
+ _objc_msgSend$_effectiveAndCanonicalMainDatabasePath
+ _objc_msgSend$initWithCalendarMainDatabasePath:containerProvider:
+ _objc_msgSend$initWithDatabaseInitOptions:mainDatabasePath:containerProvider:
+ _objc_msgSend$mobileCalDAVAccount
- +[DACalDBHelper containerProvider]
- +[DACalDBHelper mainDatabasePath]
- +[DACalDBHelper setMainDatabasePath:containerProvider:]
- +[DALocalDBHelper calContainerProvider]
- +[DALocalDBHelper calMainDatabasePath]
- +[DALocalDBHelper calSetMainDatabasePath:containerProvider:]
- -[DAAccount(AuthenticationExtensions) _webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]
- -[DAAccount(AuthenticationExtensions) webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]
- ___100-[DAAccount(AuthenticationExtensions) _webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]_block_invoke
- ___100-[DAAccount(AuthenticationExtensions) _webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]_block_invoke_2
- ___99-[DAAccount(AuthenticationExtensions) webLoginRequestedAtURL:reasonString:inQueue:completionBlock:]_block_invoke
- ___block_descriptor_40_e8_32s_e673_v24?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}16ls32l8
- ___block_descriptor_48_e8_32s40s_e673_v24?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}i*IIiQBBBBBBB}16ls32l8s40l8
- ___block_literal_global.527
- __containerProvider
- __mainDatabasePathOverride
- _objc_msgSend$containerProvider
- _objc_msgSend$mainDatabasePath
- _objc_msgSend$noteCalDBDirChanged
- _objc_msgSend$setMainDatabasePath:containerProvider:
- _objc_release_x10
CStrings:
+ "@\"<CalCalendarDataContainerProvider>\""
+ "B36@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24B32"
+ "T@\"DABabysitter\",R,N"
+ "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@0:8@16"
+ "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@0:8^v16"
+ "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32@0:8@16^@24"
+ "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32@0:8^v16^@24"
+ "_containerProviderOverride"
+ "_effectiveAndCanonicalMainDatabasePath"
+ "_mainDatabasePathOverride"
+ "initWithCalendarMainDatabasePath:containerProvider:"
+ "initWithDatabaseInitOptions:mainDatabasePath:containerProvider:"
+ "mobileCalDAVAccount"
+ "v24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "v24@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "v32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
+ "v40@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"
- "B36@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16@24B32"
- "Setting unit test Calendar Main Database directory to: %@, Container Provider: %@"
- "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24@0:8@16"
- "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}24@0:8^v16"
- "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32@0:8@16^@24"
- "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32@0:8^v16^@24"
- "calContainerProvider"
- "calMainDatabasePath"
- "calSetMainDatabasePath:containerProvider:"
- "containerProvider"
- "mainDatabasePath"
- "setMainDatabasePath:containerProvider:"
- "v24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16"
- "v24@?0^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16"
- "v32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}16@24"
- "v40@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@i@@@*IIiQBBBBBBB}32"

```
