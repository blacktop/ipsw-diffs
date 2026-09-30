## CompanionSync

> `/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync`

```diff

-275.1.0.0.0
-  __TEXT.__text: 0xa012c
-  __TEXT.__auth_stubs: 0x10e0
-  __TEXT.__objc_methlist: 0x8db0
-  __TEXT.__cstring: 0x7746
+275.2.0.0.0
+  __TEXT.__text: 0x9eed8
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__objc_methlist: 0x8c70
+  __TEXT.__cstring: 0x76a1
   __TEXT.__const: 0x1c0
   __TEXT.__oslogstring: 0x9512
   __TEXT.__gcc_except_tab: 0x35e0
-  __TEXT.__unwind_info: 0x2df0
-  __TEXT.__objc_classname: 0xd61
-  __TEXT.__objc_methname: 0xd39b
-  __TEXT.__objc_methtype: 0x2a52
-  __TEXT.__objc_stubs: 0xa700
+  __TEXT.__unwind_info: 0x2de8
+  __TEXT.__objc_classname: 0xd5b
+  __TEXT.__objc_methname: 0xcfa0
+  __TEXT.__objc_methtype: 0x2a3d
+  __TEXT.__objc_stubs: 0xa4e0
   __DATA_CONST.__got: 0x5f8
   __DATA_CONST.__const: 0x2020
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3580
+  __DATA_CONST.__objc_selrefs: 0x34a8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x880
+  __AUTH_CONST.__auth_got: 0x878
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x3920
-  __AUTH_CONST.__objc_const: 0x14890
+  __AUTH_CONST.__cfstring: 0x37e0
+  __AUTH_CONST.__objc_const: 0x14570
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1fe0
-  __DATA.__objc_ivar: 0xc70
+  __DATA.__objc_ivar: 0xc20
   __DATA.__data: 0xb68
   __DATA.__bss: 0x130
   __DATA_DIRTY.__objc_data: 0x370

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6DE94132-CD92-37CE-A487-B9B37B7359EF
-  Functions: 3786
-  Symbols:   14133
-  CStrings:  5097
+  UUID: E77E0D85-D816-3EFE-9940-19C3C4DAB7C1
+  Functions: 3759
+  Symbols:   14041
+  CStrings:  5027
 
Symbols:
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.73
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.73.cold.1
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.73.cold.2
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.80
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.84
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.84.cold.1
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.84.cold.2
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.75
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.81
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.81.cold.1
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.86
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.86.cold.1
- -[SYLogEngineState .cxx_destruct]
- -[SYLogEngineState handledRequestID]
- -[SYLogEngineState handledResponseID]
- -[SYLogEngineState oobDataEndedDate]
- -[SYLogEngineState oobDataStartedDate]
- -[SYLogEngineState queueResumedDate]
- -[SYLogEngineState queueSuspendedDate]
- -[SYLogEngineState requestEndedDate]
- -[SYLogEngineState requestStartedDate]
- -[SYLogEngineState responseEndedDate]
- -[SYLogEngineState responseStartedDate]
- -[SYLogEngineState setHandledRequestID:]
- -[SYLogEngineState setHandledResponseID:]
- -[SYLogEngineState setOobDataEndedDate:]
- -[SYLogEngineState setOobDataStartedDate:]
- -[SYLogEngineState setQueueResumedDate:]
- -[SYLogEngineState setQueueSuspendedDate:]
- -[SYLogEngineState setRequestEndedDate:]
- -[SYLogEngineState setRequestStartedDate:]
- -[SYLogEngineState setResponseEndedDate:]
- -[SYLogEngineState setResponseStartedDate:]
- -[SYMessengerSyncEngine _oobDataEnded]
- -[SYMessengerSyncEngine _oobDataStarted]
- -[SYMessengerSyncEngine _requestEnded]
- -[SYMessengerSyncEngine _requestStarted:]
- -[SYMessengerSyncEngine _responseEnded]
- -[SYMessengerSyncEngine _responseStarted:]
- _OBJC_IVAR_$_SYLogEngineState._handledRequestID
- _OBJC_IVAR_$_SYLogEngineState._handledResponseID
- _OBJC_IVAR_$_SYLogEngineState._oobDataEndedDate
- _OBJC_IVAR_$_SYLogEngineState._oobDataStartedDate
- _OBJC_IVAR_$_SYLogEngineState._queueResumedDate
- _OBJC_IVAR_$_SYLogEngineState._queueSuspendedDate
- _OBJC_IVAR_$_SYLogEngineState._requestEndedDate
- _OBJC_IVAR_$_SYLogEngineState._requestStartedDate
- _OBJC_IVAR_$_SYLogEngineState._responseEndedDate
- _OBJC_IVAR_$_SYLogEngineState._responseStartedDate
- _OBJC_IVAR_$_SYMessengerSyncEngine._handledRequestID
- _OBJC_IVAR_$_SYMessengerSyncEngine._handledResponseID
- _OBJC_IVAR_$_SYMessengerSyncEngine._oobDataEndedDate
- _OBJC_IVAR_$_SYMessengerSyncEngine._oobDataStartedDate
- _OBJC_IVAR_$_SYMessengerSyncEngine._queueResumedDate
- _OBJC_IVAR_$_SYMessengerSyncEngine._queueSuspendedDate
- _OBJC_IVAR_$_SYMessengerSyncEngine._requestEndedDate
- _OBJC_IVAR_$_SYMessengerSyncEngine._requestStartedDate
- _OBJC_IVAR_$_SYMessengerSyncEngine._responseEndedDate
- _OBJC_IVAR_$_SYMessengerSyncEngine._responseStartedDate
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.74.cold.1
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.74.cold.2
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.75
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.81
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.85.cold.1
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.85.cold.2
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.86
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.76
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.82
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.82.cold.1
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.87
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.87.cold.1
- _objc_msgSend$_oobDataEnded
- _objc_msgSend$_oobDataStarted
- _objc_msgSend$_requestEnded
- _objc_msgSend$_requestStarted:
- _objc_msgSend$_responseEnded
- _objc_msgSend$_responseStarted:
- _objc_msgSend$numberWithShort:
- _objc_msgSend$setHandledRequestID:
- _objc_msgSend$setHandledResponseID:
- _objc_msgSend$setOobDataEndedDate:
- _objc_msgSend$setOobDataStartedDate:
- _objc_msgSend$setQueueResumedDate:
- _objc_msgSend$setQueueSuspendedDate:
- _objc_msgSend$setRequestEndedDate:
- _objc_msgSend$setRequestStartedDate:
- _objc_msgSend$setResponseEndedDate:
- _objc_msgSend$setResponseStartedDate:
- _objc_setProperty_atomic
CStrings:
- "T@\"NSDate\",&,V_oobDataEndedDate"
- "T@\"NSDate\",&,V_oobDataStartedDate"
- "T@\"NSDate\",&,V_queueResumedDate"
- "T@\"NSDate\",&,V_queueSuspendedDate"
- "T@\"NSDate\",&,V_requestEndedDate"
- "T@\"NSDate\",&,V_requestStartedDate"
- "T@\"NSDate\",&,V_responseEndedDate"
- "T@\"NSDate\",&,V_responseStartedDate"
- "Ts,N,V_handledRequestID"
- "Ts,N,V_handledResponseID"
- "_handledRequestID"
- "_handledResponseID"
- "_oobDataEnded"
- "_oobDataEndedDate"
- "_oobDataStarted"
- "_oobDataStartedDate"
- "_queueResumedDate"
- "_queueSuspendedDate"
- "_requestEnded"
- "_requestEndedDate"
- "_requestStarted:"
- "_requestStartedDate"
- "_responseEnded"
- "_responseEndedDate"
- "_responseStarted:"
- "_responseStartedDate"
- "handledRequestID"
- "handledResponseID"
- "numberWithShort:"
- "oobDataEndedDate"
- "oobDataStartedDate"
- "queueResumedDate"
- "queueSuspendedDate"
- "requestEnded"
- "requestEndedDate"
- "requestStarted"
- "requestStartedDate"
- "responseEnded"
- "responseEndedDate"
- "responseStarted"
- "responseStartedDate"
- "s"
- "s16@0:8"
- "setHandledRequestID:"
- "setHandledResponseID:"
- "setOobDataEndedDate:"
- "setOobDataStartedDate:"
- "setQueueResumedDate:"
- "setQueueSuspendedDate:"
- "setRequestEndedDate:"
- "setRequestStartedDate:"
- "setResponseEndedDate:"
- "setResponseStartedDate:"
- "v20@0:8s16"

```
