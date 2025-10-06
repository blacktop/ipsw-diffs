## CompanionSync

> `/System/Library/PrivateFrameworks/CompanionSync.framework/CompanionSync`

```diff

-271.0.0.0.0
-  __TEXT.__text: 0x9b264
+272.0.0.0.0
+  __TEXT.__text: 0x9c654
   __TEXT.__auth_stubs: 0x1110
-  __TEXT.__objc_methlist: 0x8b80
-  __TEXT.__cstring: 0x747e
+  __TEXT.__objc_methlist: 0x8cc0
+  __TEXT.__cstring: 0x7530
   __TEXT.__const: 0x1c0
   __TEXT.__oslogstring: 0x9502
-  __TEXT.__gcc_except_tab: 0x368c
-  __TEXT.__unwind_info: 0x2990
-  __TEXT.__objc_classname: 0xd5a
-  __TEXT.__objc_methname: 0xcbff
-  __TEXT.__objc_methtype: 0x296f
-  __TEXT.__objc_stubs: 0xa340
+  __TEXT.__gcc_except_tab: 0x36cc
+  __TEXT.__unwind_info: 0x29a8
+  __TEXT.__objc_classname: 0xd60
+  __TEXT.__objc_methname: 0xd00a
+  __TEXT.__objc_methtype: 0x2984
+  __TEXT.__objc_stubs: 0xa560
   __DATA_CONST.__got: 0x5f8
   __DATA_CONST.__const: 0x1fb8
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3430
+  __DATA_CONST.__objc_selrefs: 0x3508
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0x898
-  __AUTH_CONST.__const: 0x480
-  __AUTH_CONST.__cfstring: 0x3520
-  __AUTH_CONST.__objc_const: 0x14330
+  __AUTH_CONST.__const: 0x4a0
+  __AUTH_CONST.__cfstring: 0x36a0
+  __AUTH_CONST.__objc_const: 0x14650
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1fe0
-  __DATA.__objc_ivar: 0xbfc
+  __DATA.__objc_ivar: 0xc4c
   __DATA.__data: 0xb68
-  __DATA.__bss: 0x130
+  __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0x370
   __DATA_DIRTY.__common: 0x50
   __DATA_DIRTY.__bss: 0x68

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 09F441BA-5EE2-3A4A-8F1A-7ACB03ADE0DA
-  Functions: 3708
-  Symbols:   13823
-  CStrings:  4953
+  UUID: F341B2C8-4CA7-3DE5-B562-5CDFF213C24E
+  Functions: 3737
+  Symbols:   13922
+  CStrings:  5025
 
Symbols:
+ -[SYLogEngineState .cxx_destruct]
+ -[SYLogEngineState dictionaryRepresentation].cold.1
+ -[SYLogEngineState handledRequestID]
+ -[SYLogEngineState handledResponseID]
+ -[SYLogEngineState oobDataEndedDate]
+ -[SYLogEngineState oobDataStartedDate]
+ -[SYLogEngineState queueResumedDate]
+ -[SYLogEngineState queueSuspendedDate]
+ -[SYLogEngineState requestEndedDate]
+ -[SYLogEngineState requestStartedDate]
+ -[SYLogEngineState responseEndedDate]
+ -[SYLogEngineState responseStartedDate]
+ -[SYLogEngineState setHandledRequestID:]
+ -[SYLogEngineState setHandledResponseID:]
+ -[SYLogEngineState setOobDataEndedDate:]
+ -[SYLogEngineState setOobDataStartedDate:]
+ -[SYLogEngineState setQueueResumedDate:]
+ -[SYLogEngineState setQueueSuspendedDate:]
+ -[SYLogEngineState setRequestEndedDate:]
+ -[SYLogEngineState setRequestStartedDate:]
+ -[SYLogEngineState setResponseEndedDate:]
+ -[SYLogEngineState setResponseStartedDate:]
+ -[SYMessengerSyncEngine _oobDataEnded]
+ -[SYMessengerSyncEngine _oobDataStarted]
+ -[SYMessengerSyncEngine _requestEnded]
+ -[SYMessengerSyncEngine _requestStarted:]
+ -[SYMessengerSyncEngine _responseEnded]
+ -[SYMessengerSyncEngine _responseStarted:]
+ _OBJC_IVAR_$_SYLogEngineState._handledRequestID
+ _OBJC_IVAR_$_SYLogEngineState._handledResponseID
+ _OBJC_IVAR_$_SYLogEngineState._oobDataEndedDate
+ _OBJC_IVAR_$_SYLogEngineState._oobDataStartedDate
+ _OBJC_IVAR_$_SYLogEngineState._queueResumedDate
+ _OBJC_IVAR_$_SYLogEngineState._queueSuspendedDate
+ _OBJC_IVAR_$_SYLogEngineState._requestEndedDate
+ _OBJC_IVAR_$_SYLogEngineState._requestStartedDate
+ _OBJC_IVAR_$_SYLogEngineState._responseEndedDate
+ _OBJC_IVAR_$_SYLogEngineState._responseStartedDate
+ _OBJC_IVAR_$_SYMessengerSyncEngine._handledRequestID
+ _OBJC_IVAR_$_SYMessengerSyncEngine._handledResponseID
+ _OBJC_IVAR_$_SYMessengerSyncEngine._oobDataEndedDate
+ _OBJC_IVAR_$_SYMessengerSyncEngine._oobDataStartedDate
+ _OBJC_IVAR_$_SYMessengerSyncEngine._queueResumedDate
+ _OBJC_IVAR_$_SYMessengerSyncEngine._queueSuspendedDate
+ _OBJC_IVAR_$_SYMessengerSyncEngine._requestEndedDate
+ _OBJC_IVAR_$_SYMessengerSyncEngine._requestStartedDate
+ _OBJC_IVAR_$_SYMessengerSyncEngine._responseEndedDate
+ _OBJC_IVAR_$_SYMessengerSyncEngine._responseStartedDate
+ ___30-[SYService _sendResetRequest]_block_invoke.129
+ ___30-[SYService _sendResetRequest]_block_invoke.129.cold.1
+ ___30-[SYService _sendResetRequest]_block_invoke.129.cold.2
+ ___35-[SYService _processPendingChanges]_block_invoke.119
+ ___35-[SYService _processPendingChanges]_block_invoke.119.cold.1
+ ___35-[SYService _processPendingChanges]_block_invoke.119.cold.2
+ ___37-[SYService sessionDidEnd:withError:]_block_invoke.151
+ ___40-[SYService _switchToNewTargetedDevice:]_block_invoke.91
+ ___40-[SYService _switchToNewTargetedDevice:]_block_invoke.91.cold.1
+ ___40-[SYService _switchToNewTargetedDevice:]_block_invoke.91.cold.2
+ ___40-[SYService _switchToNewTargetedDevice:]_block_invoke.94
+ ___44-[SYLogEngineState dictionaryRepresentation]_block_invoke
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.184
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.184.cold.1
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.185
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.185.cold.1
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.185.cold.2
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.185.cold.3
+ ___44-[SYService _handleStartSession:completion:]_block_invoke.185.cold.4
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.74.cold.1
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.74.cold.2
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.75
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.81
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.85.cold.1
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.85.cold.2
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.86
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.76
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.82
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.82.cold.1
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.87
+ ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.87.cold.1
+ ___50-[SYService handleSyncResponse:ofType:completion:]_block_invoke.163
+ ___50-[SYService handleSyncResponse:ofType:completion:]_block_invoke.163.cold.1
+ ___52-[SYService handleFileTransfer:metadata:completion:]_block_invoke.175
+ ___52-[SYService handleFileTransfer:metadata:completion:]_block_invoke.175.cold.1
+ ___52-[SYService handleFileTransfer:metadata:completion:]_block_invoke.175.cold.2
+ ___70-[SYService(CompanionSyncProtoV1) _v1_handleChangeMessage:completion:]_block_invoke.496
+ ___71-[SYService(CompanionSyncProtoV1) _v1_handleBatchSyncStart:completion:]_block_invoke.493
+ ___71-[SYService(CompanionSyncProtoV1) _v1_handleSyncAllObjects:completion:]_block_invoke.490
+ ___71-[SYService(CompanionSyncProtoV1) _v1_handleSyncAllObjects:completion:]_block_invoke.490.cold.1
+ ___block_literal_global.159
+ ___block_literal_global.165
+ _dictionaryRepresentation.__formatter
+ _dictionaryRepresentation.onceToken
+ _objc_msgSend$_oobDataEnded
+ _objc_msgSend$_oobDataStarted
+ _objc_msgSend$_requestEnded
+ _objc_msgSend$_requestStarted:
+ _objc_msgSend$_responseEnded
+ _objc_msgSend$_responseStarted:
+ _objc_msgSend$numberWithShort:
+ _objc_msgSend$setHandledRequestID:
+ _objc_msgSend$setHandledResponseID:
+ _objc_msgSend$setOobDataEndedDate:
+ _objc_msgSend$setOobDataStartedDate:
+ _objc_msgSend$setQueueResumedDate:
+ _objc_msgSend$setQueueSuspendedDate:
+ _objc_msgSend$setRequestEndedDate:
+ _objc_msgSend$setRequestStartedDate:
+ _objc_msgSend$setResponseEndedDate:
+ _objc_msgSend$setResponseStartedDate:
- ___30-[SYService _sendResetRequest]_block_invoke.127
- ___30-[SYService _sendResetRequest]_block_invoke.127.cold.1
- ___30-[SYService _sendResetRequest]_block_invoke.127.cold.2
- ___35-[SYService _processPendingChanges]_block_invoke.117
- ___35-[SYService _processPendingChanges]_block_invoke.117.cold.1
- ___35-[SYService _processPendingChanges]_block_invoke.117.cold.2
- ___37-[SYService sessionDidEnd:withError:]_block_invoke.149
- ___40-[SYService _switchToNewTargetedDevice:]_block_invoke.89
- ___40-[SYService _switchToNewTargetedDevice:]_block_invoke.89.cold.1
- ___40-[SYService _switchToNewTargetedDevice:]_block_invoke.89.cold.2
- ___40-[SYService _switchToNewTargetedDevice:]_block_invoke.92
- ___44-[SYService _handleStartSession:completion:]_block_invoke.182
- ___44-[SYService _handleStartSession:completion:]_block_invoke.182.cold.1
- ___44-[SYService _handleStartSession:completion:]_block_invoke.183
- ___44-[SYService _handleStartSession:completion:]_block_invoke.183.cold.1
- ___44-[SYService _handleStartSession:completion:]_block_invoke.183.cold.2
- ___44-[SYService _handleStartSession:completion:]_block_invoke.183.cold.3
- ___44-[SYService _handleStartSession:completion:]_block_invoke.183.cold.4
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.73
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.73.cold.1
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.73.cold.2
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.80
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.84
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.84.cold.1
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke.84.cold.2
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.75
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.81
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.81.cold.1
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.86
- ___46-[SYMessengerSyncEngine _hookupMessageHandler]_block_invoke_2.86.cold.1
- ___50-[SYService handleSyncResponse:ofType:completion:]_block_invoke.161
- ___50-[SYService handleSyncResponse:ofType:completion:]_block_invoke.161.cold.1
- ___52-[SYService handleFileTransfer:metadata:completion:]_block_invoke.173
- ___52-[SYService handleFileTransfer:metadata:completion:]_block_invoke.173.cold.1
- ___52-[SYService handleFileTransfer:metadata:completion:]_block_invoke.173.cold.2
- ___70-[SYService(CompanionSyncProtoV1) _v1_handleChangeMessage:completion:]_block_invoke.494
- ___71-[SYService(CompanionSyncProtoV1) _v1_handleBatchSyncStart:completion:]_block_invoke.491
- ___71-[SYService(CompanionSyncProtoV1) _v1_handleSyncAllObjects:completion:]_block_invoke.488
- ___71-[SYService(CompanionSyncProtoV1) _v1_handleSyncAllObjects:completion:]_block_invoke.488.cold.1
- ___block_literal_global.157
- ___block_literal_global.163
CStrings:
+ "Error while generating state: %@"
+ "T@\"NSDate\",&,N,V_oobDataEndedDate"
+ "T@\"NSDate\",&,N,V_oobDataStartedDate"
+ "T@\"NSDate\",&,N,V_queueResumedDate"
+ "T@\"NSDate\",&,N,V_queueSuspendedDate"
+ "T@\"NSDate\",&,N,V_requestEndedDate"
+ "T@\"NSDate\",&,N,V_requestStartedDate"
+ "T@\"NSDate\",&,N,V_responseEndedDate"
+ "T@\"NSDate\",&,N,V_responseStartedDate"
+ "Ts,N,V_handledRequestID"
+ "Ts,N,V_handledResponseID"
+ "_handledRequestID"
+ "_handledResponseID"
+ "_oobDataEnded"
+ "_oobDataEndedDate"
+ "_oobDataStarted"
+ "_oobDataStartedDate"
+ "_queueResumedDate"
+ "_queueSuspendedDate"
+ "_requestEnded"
+ "_requestEndedDate"
+ "_requestStarted:"
+ "_requestStartedDate"
+ "_responseEnded"
+ "_responseEndedDate"
+ "_responseStarted:"
+ "_responseStartedDate"
+ "handledRequestID"
+ "handledResponseID"
+ "numberWithShort:"
+ "oobDataEndedDate"
+ "oobDataStartedDate"
+ "queueResumedDate"
+ "queueSuspendedDate"
+ "requestEnded"
+ "requestEndedDate"
+ "requestStarted"
+ "requestStartedDate"
+ "responseEnded"
+ "responseEndedDate"
+ "responseStarted"
+ "responseStartedDate"
+ "s"
+ "s16@0:8"
+ "setHandledRequestID:"
+ "setHandledResponseID:"
+ "setOobDataEndedDate:"
+ "setOobDataStartedDate:"
+ "setQueueResumedDate:"
+ "setQueueSuspendedDate:"
+ "setRequestEndedDate:"
+ "setRequestStartedDate:"
+ "setResponseEndedDate:"
+ "setResponseStartedDate:"
+ "v20@0:8s16"
+ "yyyy-MM-dd HH:mm:ss.SSS ZZZZZ"

```
