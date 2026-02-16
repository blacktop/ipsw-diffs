## DACalDAV

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACalDAV.framework/DACalDAV`

```diff

-2691.2.2.0.0
-  __TEXT.__text: 0x378b8
-  __TEXT.__auth_stubs: 0x1e90
-  __TEXT.__objc_methlist: 0x4604
+2691.4.5.0.0
+  __TEXT.__text: 0x3bbb8
+  __TEXT.__auth_stubs: 0x1e50
+  __TEXT.__objc_methlist: 0x462c
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x1641
+  __TEXT.__cstring: 0x16d2
   __TEXT.__oslogstring: 0x506c
-  __TEXT.__gcc_except_tab: 0x5e4
+  __TEXT.__gcc_except_tab: 0x52c
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0xa40
+  __TEXT.__unwind_info: 0xc40
   __TEXT.__objc_classname: 0x505
-  __TEXT.__objc_methname: 0x9e2c
-  __TEXT.__objc_methtype: 0x1f9f
-  __TEXT.__objc_stubs: 0x7f80
-  __DATA_CONST.__got: 0x7e0
-  __DATA_CONST.__const: 0x9f8
+  __TEXT.__objc_methname: 0x9e90
+  __TEXT.__objc_methtype: 0x1fea
+  __TEXT.__objc_stubs: 0x7fa0
+  __DATA_CONST.__got: 0x7e8
+  __DATA_CONST.__const: 0xa20
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2810
+  __DATA_CONST.__objc_selrefs: 0x2820
   __DATA_CONST.__objc_superrefs: 0x90
-  __AUTH_CONST.__auth_got: 0xf58
+  __AUTH_CONST.__auth_got: 0xf38
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x23a0
-  __AUTH_CONST.__objc_const: 0x8a80
+  __AUTH_CONST.__cfstring: 0x24e0
+  __AUTH_CONST.__objc_const: 0x8d98
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0x340

   - /System/Library/PrivateFrameworks/CalDAV.framework/CalDAV
   - /System/Library/PrivateFrameworks/CalendarDatabase.framework/CalendarDatabase
   - /System/Library/PrivateFrameworks/CalendarFoundation.framework/CalendarFoundation
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreDAV.framework/CoreDAV
   - /System/Library/PrivateFrameworks/DataAccess.framework/DataAccess
   - /System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DACoreDAVGlue.framework/DACoreDAVGlue

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: B3440BF8-BE6D-352C-9957-7B2E05B1E29A
-  Functions: 1090
-  Symbols:   4743
-  CStrings:  2906
+  UUID: 3B0CB820-2D07-3948-9417-EAE0DE56049F
+  Functions: 1100
+  Symbols:   4760
+  CStrings:  2933
 
Symbols:
+ -[MobileCalDAVAccount pushRefreshInterval]
+ -[MobileCalDAVPrincipal completeWithError:httpMethod:latency:task:responseStatusCode:]
+ -[MobileCalDAVPrincipal pushRefreshInterval]
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table119
+ GCC_except_table121
+ GCC_except_table84
+ GCC_except_table98
+ _AnalyticsSendEventLazy
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ ___86-[MobileCalDAVPrincipal completeWithError:httpMethod:latency:task:responseStatusCode:]_block_invoke
+ ___block_descriptor_80_e8_32s40s48s56s_e19_"NSDictionary"8?0ls32l8s40l8s48l8s56l8
+ _cdXMLCalendarServerRefreshInterval
+ _objc_msgSend$pushRefreshInterval
- GCC_except_table101
- GCC_except_table104
- GCC_except_table118
- GCC_except_table120
- GCC_except_table83
- GCC_except_table97
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "@\"NSDictionary\"8@?0"
+ "@32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
+ "B36@0:8i16@20^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}28"
+ "B40@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32"
+ "DELETE"
+ "POST"
+ "PUT"
+ "T@\"NSString\",?,R,C,N"
+ "Td,R,N"
+ "Tq,R,N"
+ "^v32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16^v24"
+ "^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}"
+ "com.apple.dataaccess.caldav.CoreDAVTaskComplete"
+ "completeWithError:httpMethod:latency:task:responseStatusCode:"
+ "errorCode"
+ "errorDomain"
+ "latency"
+ "method"
+ "pushRefreshInterval"
+ "responseCode"
+ "serverType"
+ "v24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
+ "v32@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}Q^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"
+ "v56@0:8@\"NSError\"16@\"NSString\"24d32@\"NSString\"40q48"
+ "v56@0:8@16@24d32@40q48"
- "@32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16@24"
- "B36@0:8i16@20^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}28"
- "B40@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24@32"
- "T@\"NSData\",R,C,N"
- "^v32@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16^v24"
- "^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}"
- "v24@0:8^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}16"
- "v32@0:8@16^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}24"

```
