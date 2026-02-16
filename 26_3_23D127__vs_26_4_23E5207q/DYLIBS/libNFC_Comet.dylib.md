## libNFC_Comet.dylib

> `/usr/lib/libNFC_Comet.dylib`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0xc5458
+364.20.0.0.0
+  __TEXT.__text: 0xc28e0
   __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__const: 0x9d8
-  __TEXT.__cstring: 0x3c51f
-  __TEXT.__unwind_info: 0x10e0
+  __TEXT.__const: 0xa30
+  __TEXT.__cstring: 0x3bd0f
+  __TEXT.__unwind_info: 0x1180
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x1f0
   __AUTH_CONST.__auth_got: 0x160
   __AUTH_CONST.__const: 0x460
-  __AUTH.__data: 0x3748
+  __AUTH.__data: 0x3658
   __DATA.__data: 0x4d1
   __DATA.__common: 0x38
   __DATA.__bss: 0x7f
-  __DATA_DIRTY.__data: 0x1388
-  __DATA_DIRTY.__bss: 0x4f
+  __DATA_DIRTY.__data: 0x1310
   __DATA_DIRTY.__common: 0xf0
+  __DATA_DIRTY.__bss: 0x27
   - /usr/lib/libNFC_HAL.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: 828B10B6-89F7-3CD5-ACCB-61055F554016
-  Functions: 1864
-  Symbols:   149
-  CStrings:  5894
+  UUID: 9C748B44-6642-3B14-B7B2-D9309B6EC9D4
+  Functions: 1871
+  Symbols:   148
+  CStrings:  5855
 
Symbols:
+ _phTmlNfc_ConfigureTestParams
- _memset_pattern16
- _phLibNfc_Mgt_InvalidateSeRmProhibitTimer
CStrings:
+ "MW Version NFC5.1_R4.35"
+ "phDnldNfc_BuildDnldEsePkt : Failed to create start timer"
+ "phDnldNfc_BuildDnldEsePkt : pDnldEseCoreCtx->dwCrdtTimeOutMs:"
+ "phDnldNfc_Validate_DnldHeaderRcvd"
+ "phDnldNfc_Validate_DnldHeaderRcvd: Invalid Download core context received!!"
+ "phLibNfc_SM_DeInitTrans: Failed to reset the Rx Delay"
+ "phLibNfc_SM_IoctlConfigDebugModeTrans: Invalid configuration"
+ "phLibNfc_SM_IoctlConfigDebugModeTrans: Invalid configuration "
+ "phNciNfc_ClearUpperLayerCb"
+ "phNciNfc_ClearUpperLayerCb: Clear callback and context"
+ "phNciNfc_ConfigRxDelayTimeFlag"
+ "phNciNfc_ConfigRxDelayTimeFlag: Stack not initialized"
+ "phNciNfc_CoreRxDelayReqNciPkt"
+ "phNciNfc_CoreRxDelayReqNciPkt: Invalid Core context!"
+ "phNciNfc_CoreRxDelayReqNciPkt: Set Rx delay failed!"
+ "phNciNfc_CoreRxDelayReqNciPkt: Tml Read request failed!"
+ "phNciNfc_StoreNfcFTechParams: DTA is not enabled"
- "#######Get Prohibit timer status notification TIMEOUT########\n"
- "De-register pres chk extension ntf call back failed!"
- "Get Prohibit - Status failed!, status byte:"
- "Get Prohibit Timer Status Ntf received with rejected from NFCC"
- "Get Prohibit Timer status Notification timer failed to restart for extended time\n\n"
- "Get Prohibit timer status info Notification timer restarted for extended time\n"
- "Ioctl_ConfigDebugMode: LIBNFC Not Initialized"
- "MW Version"
- "Nci context null (phNciNfc_GetProhibitTimerStsTimeOutHandler)\n"
- "Registering for Get prohibit timer status Notification"
- "Timeout:dwGetProhibitTimerStsNtfTimerId"
- "dwGetProhibitTimerStsNtfTimerId"
- "phDnldEseNfc_HciRecvManager: Data from unknown Pipe ID"
- "phDnldEseNfc_MultiOSGetPipeId:Invalid Context or Pipe Id"
- "phLibNfc_CommonSeqComplete"
- "phLibNfc_CommonSeqComplete: Status failed"
- "phLibNfc_CommonSeqComplete: Status success"
- "phLibNfc_GetProhibitTimerStsCmd"
- "phLibNfc_GetProhibitTimerStsCmd: Invalid parameter, Libnfc Context is Invalid"
- "phLibNfc_GetProhibitTimerStsSeqComplete"
- "phLibNfc_GetProhibitTimerStsSeqComplete: Failed"
- "phLibNfc_GetProhibitTimerStsSeqComplete: Failed, Received unknown Timer ID"
- "phLibNfc_GetProhibitTimerStsSeqComplete: Invalid LibNfc Ctx received from NCI"
- "phLibNfc_Mgt_InvalidateSeRmProhibitTimer"
- "phLibNfc_Mgt_InvalidateSeRmProhibitTimer: Invalid input parameters"
- "phLibNfc_SM_GetProhibitTimerStatusTrans"
- "phLibNfc_SM_GetProhibitTimerStatusTrans: Get prohibit timer status not supported on this platform"
- "phLibNfc_SM_GetProhibitTimerStatusTrans: Invalid context"
- "phLibNfc_SM_IoctlConfigDebugModeTrans: Failed to update SeTransceive Modified Timeout details "
- "phLibNfc_SM_IoctlSetSysConfigTrans- Inconsistent Input buffer, Status"
- "phLibNfc_StartProhibitTimerCmd"
- "phLibNfc_StartProhibitTimerCmd: Invalid parameter, Libnfc Context is Invalid"
- "phLibNfc_StopProhibitTimerCmd"
- "phLibNfc_StopProhibitTimerCmd: Invalid parameter, Libnfc Context is Invalid"
- "phLibNfc_SwioPadNtfHandler: Info buffer not valid"
- "phNciNfc_GetProhibitTimerStatus"
- "phNciNfc_GetProhibitTimerStatus: Invalid parameters"
- "phNciNfc_GetProhibitTimerStatus: Sequence failed!"
- "phNciNfc_GetProhibitTimerStatus: Stack not initialized"
- "phNciNfc_GetProhibitTimerStsCmd"
- "phNciNfc_GetProhibitTimerStsCmd: Invalid input parameter"
- "phNciNfc_GetProhibitTimerStsRsp"
- "phNciNfc_GetProhibitTimerStsRsp: Successful"
- "phNciNfc_GetProhibitTimerStsRsp: failed!"
- "phNciNfc_GetProhibitTimerStsRsp: invalid payload length"
- "phNciNfc_GetProhibitTimerStsRsp: received with failure status"
- "phNciNfc_GetProhibitTimerStsRsp: rejected by NFCC"
- "phNciNfc_GetProhibitTimerStsSeqComplete"
- "phNciNfc_GetProhibitTimerStsSeqComplete: Notification timer start FAILED\n\n"
- "phNciNfc_GetProhibitTimerStsSeqComplete: Notification timer started\n"
- "phNciNfc_GetProhibitTimerStsSeqComplete: Timer Create failed!!"
- "phNciNfc_GetProhibitTimerStsSeqComplete: Timer Created Successfully"
- "phNciNfc_GetProhibitTimerStsTimeOutHandler"
- "phNciNfc_ProcessGetProhibitTimerStsNtf"
- "phNciNfc_ProcessGetProhibitTimerStsNtf: dropping ..."
- "phNciNfc_ProcessGetProhibitTimerStsNtf:Get Prohibit Timer Status Ntf - Payload parsing failed, wLength"

```
