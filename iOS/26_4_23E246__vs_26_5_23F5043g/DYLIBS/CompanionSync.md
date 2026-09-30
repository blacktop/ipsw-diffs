## CompanionSync

> `/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync`

```diff

-275.0.0.0.0
-  __TEXT.__text: 0xa034c
-  __TEXT.__auth_stubs: 0x10d0
+275.1.0.0.0
+  __TEXT.__text: 0xa012c
+  __TEXT.__auth_stubs: 0x10e0
   __TEXT.__objc_methlist: 0x8db0
   __TEXT.__cstring: 0x7746
   __TEXT.__const: 0x1c0
   __TEXT.__oslogstring: 0x9512
   __TEXT.__gcc_except_tab: 0x35e0
-  __TEXT.__unwind_info: 0x2e28
+  __TEXT.__unwind_info: 0x2df0
   __TEXT.__objc_classname: 0xd61
-  __TEXT.__objc_methname: 0xd3ab
+  __TEXT.__objc_methname: 0xd39b
   __TEXT.__objc_methtype: 0x2a52
   __TEXT.__objc_stubs: 0xa700
   __DATA_CONST.__got: 0x5f8

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x878
+  __AUTH_CONST.__auth_got: 0x880
   __AUTH_CONST.__const: 0x4c0
   __AUTH_CONST.__cfstring: 0x3920
   __AUTH_CONST.__objc_const: 0x14890

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6B85D35D-BC02-3222-B791-9D302C4F0B04
+  UUID: E14E78EA-A594-3ADF-81AD-9BCF95AF4B69
   Functions: 3786
-  Symbols:   14132
+  Symbols:   14133
   CStrings:  5097
 
Symbols:
+ _objc_setProperty_atomic
Functions:
~ -[SYLogEngineState setQueueSuspendedDate:] : 80 -> 12
~ -[SYLogEngineState setQueueResumedDate:] : 80 -> 12
~ -[SYLogEngineState setRequestStartedDate:] : 80 -> 12
~ -[SYLogEngineState setRequestEndedDate:] : 80 -> 12
~ -[SYLogEngineState setResponseStartedDate:] : 80 -> 12
~ -[SYLogEngineState setResponseEndedDate:] : 80 -> 12
~ -[SYLogEngineState setOobDataStartedDate:] : 80 -> 12
~ -[SYLogEngineState setOobDataEndedDate:] : 80 -> 12
CStrings:
+ "T@\"NSDate\",&,V_oobDataEndedDate"
+ "T@\"NSDate\",&,V_oobDataStartedDate"
+ "T@\"NSDate\",&,V_queueResumedDate"
+ "T@\"NSDate\",&,V_queueSuspendedDate"
+ "T@\"NSDate\",&,V_requestEndedDate"
+ "T@\"NSDate\",&,V_requestStartedDate"
+ "T@\"NSDate\",&,V_responseEndedDate"
+ "T@\"NSDate\",&,V_responseStartedDate"
- "T@\"NSDate\",&,N,V_oobDataEndedDate"
- "T@\"NSDate\",&,N,V_oobDataStartedDate"
- "T@\"NSDate\",&,N,V_queueResumedDate"
- "T@\"NSDate\",&,N,V_queueSuspendedDate"
- "T@\"NSDate\",&,N,V_requestEndedDate"
- "T@\"NSDate\",&,N,V_requestStartedDate"
- "T@\"NSDate\",&,N,V_responseEndedDate"
- "T@\"NSDate\",&,N,V_responseStartedDate"

```
