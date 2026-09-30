## DataAccess

> `/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess`

```diff

-2691.0.0.0.0
-  __TEXT.__text: 0x3cea4
+2691.0.2.0.0
+  __TEXT.__text: 0x3cf3c
   __TEXT.__auth_stubs: 0x1090
   __TEXT.__objc_methlist: 0x482c
   __TEXT.__const: 0x180

   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__unwind_info: 0xf48
   __TEXT.__objc_classname: 0x7a0
-  __TEXT.__objc_methname: 0xb9d6
-  __TEXT.__objc_methtype: 0x1ba6
+  __TEXT.__objc_methname: 0xb9ef
+  __TEXT.__objc_methtype: 0x1bad
   __TEXT.__objc_stubs: 0x7700
   __DATA_CONST.__got: 0x750
   __DATA_CONST.__const: 0xb50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 00F7B80E-F0D0-3836-8754-9B9FBA4E6ADB
+  UUID: D575A6E9-08D1-3D77-80FB-F04BB16B1A09
   Functions: 1597
   Symbols:   5678
   CStrings:  3357
Symbols:
+ -[DACalDBHelper _openDatabaseForAccountID:auxDatabaseRef:path:clientID:createdDatabaseToConsume:]
+ -[DACalDBHelper _openDatabaseForAccountID:auxDatabaseRef:path:clientID:createdDatabaseToConsume:].cold.1
+ _objc_msgSend$_openDatabaseForAccountID:auxDatabaseRef:path:clientID:createdDatabaseToConsume:
- -[DACalDBHelper _openDatabaseForPath:clientID:createdDatabaseToConsume:]
- -[DACalDBHelper _openDatabaseForPath:clientID:createdDatabaseToConsume:].cold.1
- _objc_msgSend$_openDatabaseForPath:clientID:createdDatabaseToConsume:
Functions:
~ ___51-[DACalDBHelper openDatabaseForAccountID:clientID:]_block_invoke : 108 -> 116
~ ___56-[DACalDBHelper openDatabaseForAuxDatabaseRef:clientID:]_block_invoke : 408 -> 416
~ -[DACalDBHelper _openDatabaseForPath:clientID:createdDatabaseToConsume:] -> -[DACalDBHelper _openDatabaseForAccountID:auxDatabaseRef:path:clientID:createdDatabaseToConsume:] : 992 -> 1128
CStrings:
+ "_openDatabaseForAccountID:auxDatabaseRef:path:clientID:createdDatabaseToConsume:"
+ "v56@0:8@16^v24@32@40^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}48"
- "_openDatabaseForPath:clientID:createdDatabaseToConsume:"
- "v40@0:8@16@24^{CalDatabase={__CFRuntimeBase=QAQ}i^{CPRecordStore}^{CalEventOccurrenceCache}^{CalScheduledTaskCache}^v^v^{__CFDictionary}^{__CFDictionary}{os_unfair_lock_s=I}II^{__CFArray}^{__CFString}^{__CFArray}ii^{__CFString}^{__CFURL}^{__CFString}^{__CFString}Qiii@?{_opaque_pthread_mutex_t=q[56c]}B^{__CFArray}B^{__CFSet}@@@@@*IIiQBBBBBBB}32"

```
