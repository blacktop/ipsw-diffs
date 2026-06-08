## libNFC_Comet.dylib

> `/usr/lib/libNFC_Comet.dylib`

```diff

-365.3.1.0.0
-  __TEXT.__text: 0xc28e0
-  __TEXT.__auth_stubs: 0x2c0
-  __TEXT.__const: 0xa30
-  __TEXT.__cstring: 0x3bd0f
-  __TEXT.__unwind_info: 0x1180
-  __DATA_CONST.__got: 0x8
+370.33.1.0.0
+  __TEXT.__text: 0xc16ac
+  __TEXT.__const: 0xa60
+  __TEXT.__cstring: 0x3c358
+  __TEXT.__unwind_info: 0x1230
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1f0
-  __AUTH_CONST.__auth_got: 0x160
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x460
+  __AUTH_CONST.__auth_got: 0x160
   __AUTH.__data: 0x3658
   __DATA.__data: 0x4d1
   __DATA.__common: 0x38
-  __DATA.__bss: 0x7f
-  __DATA_DIRTY.__data: 0x1310
+  __DATA.__bss: 0x7e
+  __DATA_DIRTY.__data: 0x1320
   __DATA_DIRTY.__common: 0xf0
   __DATA_DIRTY.__bss: 0x27
   - /usr/lib/libNFC_HAL.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: AC5B5ACE-2EA5-3C82-AB42-20C9BB919A28
-  Functions: 1871
+  UUID: FD176365-A53A-3DDF-BE47-0CE91234C5A9
+  Functions: 1859
   Symbols:   148
-  CStrings:  5855
+  CStrings:  5846
 
CStrings:
+ "  ISO15693 listen  Rf tech and mode sent "
+ " phLibNfc_LoggingNtfHandler : Invalid Payload During Multitag Debug Event  !!!"
+ "HCE detected as remote device type, try priority discovery"
+ "HCE send failed!"
+ "HCE send success"
+ "In P2P Target/P2P mode: No HCE Send/Receive call back found"
+ "MW Version NFC5.1_R5.7"
+ "RF Tech and Mode:NFC_ISO15693_LISTEN_MODE"
+ "Registering for Generic Debug Logging Notification"
+ "Registering for SMB Logging Notification"
+ "phLibNfc_ChkRfListnerforNFCVListen"
+ "phLibNfc_CrcErrorNtfHandler :pGenericNtfCb[CRC Err recovery info]"
+ "phLibNfc_DelayDiscTimerCb:Timeout"
+ "phLibNfc_DummyDisc: Failed to create Timer!"
+ "phLibNfc_DummyDisc: Failed to start Timer!"
+ "phLibNfc_DummyDisc:Invalid LibNfc context passed"
+ "phLibNfc_DummyDisc:Timer started"
+ "phLibNfc_FelicaChkPresComplete: Completing T3t Connect sequence"
+ "phLibNfc_GenericErrorHandler: Generic error received: MULTI_TAG ERROR"
+ "phLibNfc_GenericErrorHandler: Generic error received: UNEXPECTED MULTI TAG DETECTION ERROR"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_CorruptedTrim"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_DiscAlreadyStarted"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_DiscTearDown"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_DiscTgtActvnFailed"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_ErrorNotDefined -Unknown error code"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_Failed"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_InvalidParam"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_MsgSizeExceeded"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_NotInitiatlized"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_Rejected"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_RfFrameCorrupted"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_SemanticErr"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_SmbTxBlk_WiredNotAllowed"
+ "phLibNfc_GenericErrorHandler: Generic error received: phNciNfc_e_SyntaxErr"
+ "phLibNfc_GenericErrorHandler: Invalid Params received!!"
+ "phLibNfc_GenericErrorHandler: phLibNfc_PropMultiTagStatNtfHandler- Independent Prop Tag Detect NTF Rxd"
+ "phLibNfc_GetSuicaSysCodeComplete: Invalid LibNfc context"
+ "phLibNfc_GetVasCodeCfgComplete: Invalid LibNfc context"
+ "phLibNfc_HCERemoteDev_ReceiveCb"
+ "phLibNfc_HCERemoteDev_SendCb"
+ "phLibNfc_HCESendCmd"
+ "phLibNfc_HCESendComplete"
+ "phLibNfc_HCESendResp"
+ "phLibNfc_IoctlSetPropRfCfgComplete: NFCC Re-Init failed, return failed"
+ "phLibNfc_LoggingNtfHandler: Failed to allocate memory for HLM events"
+ "phLibNfc_LoggingNtfHandler: Failed to allocate memory for L2 debug events"
+ "phLibNfc_LoggingNtfHandler: Failed to allocate memory for LPCD Assist events"
+ "phLibNfc_LoggingNtfHandler: Failed to allocate memory for Reader Mode events"
+ "phLibNfc_LoggingNtfHandler:Failed to allocate memory for Reader Mode MultiTag events"
+ "phLibNfc_MapRemoteDevIso15693_Listen"
+ "phLibNfc_ProcessL2MultitagDebugNtf:Failed to allocate memory for Reader Mode MultiTag events"
+ "phLibNfc_SM_CheckNdefTrans: TOPAZ STATIC NDEF is not supported"
+ "phLibNfc_SM_MwResetTrans: Failed to reset the Rx Delay"
+ "phLibNfc_SM_MwResetTrans: Handle already released/ not initialised!!"
+ "phLibNfc_SM_MwResetTrans: NCI context is NULL"
+ "phNciNfc_CoreUtilsVerifyCrc: Ignoring invalid CRC bytes to recovery the error notifications"
+ "phNciNfc_GenDbgLogNtf: Received More than expected length"
+ "phNciNfc_GenDbgLogNtfTimeOutHandler: Invoke upper layer with Partial generic debug data"
+ "phNciNfc_InvokeCrcErrRecoveryInfo"
+ "phNciNfc_InvokeMfwCommonNtfCb"
+ "phNciNfc_InvokeMfwCommonNtfCb : Invalid Context"
+ "phNciNfc_InvokeMfwCommonNtfCb : Notification Callback not registered "
+ "phNciNfc_PollMgmt: Invalid input parameters"
+ "phNciNfc_PollMgmt: NFCDEP Protocol is detected and being ignored"
+ "phNciNfc_ProcessGenericErrNtf: Can not process Generic Error Ntf - Invalid input parameters"
+ "phNciNfc_ProcessGenericErrNtf: Failed to process Generic Error Ntf"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_COLD_TEMPERATURE_THRESHOLD_REACHED"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_CORRUPTED_TRIM"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_CRC_ERROR"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_DISCOVERY_ALREADY_STARTED"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_DISCOVERY_TEAR_DOWN"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_FAILED"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_INVALID_PARAM"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_MESSAGE_SIZE_EXCEEDED"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_NOT_INITIALIZED"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_REJECTED"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_RF_FRAME_CORRUPTED"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_SEMANTIC_ERROR"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_SMBTXBLK_WIREDNA"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: PH_NCINFC_STATUS_SYNTAX_ERROR"
+ "phNciNfc_ProcessGenericErrNtf: Generic error received: Unknown error code"
+ "phNciNfc_ProcessGenericErrNtf: Invalid buffer or incorrect payload length or                                  Tml receive failed receive failed"
+ "phNciNfc_RegDebugLogNtf"
+ "phNciNfc_SkipFetchingSpmiErrorRegs"
+ "phNciNfc_UpdateCrcErrNtfRecoveryFlag"
+ "phNciNfc_UpdateCrcErrNtfRecoveryFlag: Function invoked by invalid Link type"
+ "phNciNfc_UpdateErrNtfRecoveryFlag: Stack not initialized"
- "CntDiscntDisvrychkprsn_Cb :WTX Event Callback"
- "Failed to allocate memory for HLM events"
- "Failed to allocate memory for L2 debug events"
- "Failed to allocate memory for LPCD Assist events"
- "Failed to allocate memory for Reader Mode events"
- "Failed to process Generic Error Ntf"
- "Generic error received: MULTI_TAG ERROR"
- "Generic error received: PH_NCINFC_STATUS_CRC_ERROR"
- "Generic error received: PH_NCINFC_STATUS_CUST_TRIM_ERROR"
- "Generic error received: PH_NCINFC_STATUS_DISCOVERY_ALREADY_STARTED"
- "Generic error received: PH_NCINFC_STATUS_DISCOVERY_TARGET_ACTIVATION_FAILED"
- "Generic error received: PH_NCINFC_STATUS_DISCOVERY_TEAR_DOWN"
- "Generic error received: PH_NCINFC_STATUS_FAILED"
- "Generic error received: PH_NCINFC_STATUS_GPADC_LOW_TEMPERATURE"
- "Generic error received: PH_NCINFC_STATUS_INVALID_PARAM"
- "Generic error received: PH_NCINFC_STATUS_MESSAGE_SIZE_EXCEEDED"
- "Generic error received: PH_NCINFC_STATUS_NOT_INITIALIZED"
- "Generic error received: PH_NCINFC_STATUS_REJECTED"
- "Generic error received: PH_NCINFC_STATUS_RF_FRAME_CORRUPTED"
- "Generic error received: PH_NCINFC_STATUS_SEMANTIC_ERROR"
- "Generic error received: PH_NCINFC_STATUS_SMB_TX_BLOCKED"
- "Generic error received: PH_NCINFC_STATUS_SYNTAX_ERROR"
- "Generic error received: UNEXPECTED MULTI TAG DETECTION ERROR"
- "Generic error received: Unknown error code"
- "Generic error received: phNciNfc_e_CustTrimAreaAssert"
- "Generic error received: phNciNfc_e_DiscAlreadyStarted"
- "Generic error received: phNciNfc_e_DiscTearDown"
- "Generic error received: phNciNfc_e_DiscTgtActvnFailed"
- "Generic error received: phNciNfc_e_ErrorNotDefined -Unknown error code"
- "Generic error received: phNciNfc_e_Failed"
- "Generic error received: phNciNfc_e_InvalidParam"
- "Generic error received: phNciNfc_e_MsgSizeExceeded"
- "Generic error received: phNciNfc_e_NotInitiatlized"
- "Generic error received: phNciNfc_e_Rejected"
- "Generic error received: phNciNfc_e_RfFrameCorrupted"
- "Generic error received: phNciNfc_e_SemanticErr"
- "Generic error received: phNciNfc_e_SmbTxBlocked"
- "Generic error received: phNciNfc_e_SyntaxErr"
- "In P2P Target/HCE mode: No P2P Send/Receive call back found"
- "Invalid buffer or incorrect payload length or                                  Tml receive failed receive failed"
- "MW Version NFC5.1_R4.35"
- "No Poll Nfc-Dep parameters are being requested by the user to configure"
- "P2P Initiator is enabled"
- "P2P Initiator/HCE detected as remote device type, try priority discovery"
- "P2P Target mode is enabled"
- "P2P send failed!"
- "P2P send success"
- "Registering for FW Debug Info Notification"
- "Registering for HLM Debug Info Notification"
- "StoreReqCrcCfg: Stack not initialized"
- "Timeout:DelayDiscTimerCb"
- "Unknown ntf is received, and dropped "
- "phFriNfc_TopazMap_ChkNdef"
- "phFriNfc_TopazMap_ConvertToReadOnly"
- "phFriNfc_TopazMap_Process"
- "phFriNfc_TopazMap_RdNdef"
- "phFriNfc_TopazMap_WrNdef"
- "phFriNfc_Topaz_CB_Transceive"
- "phFriNfc_Tpz_H_BlkChk"
- "phFriNfc_Tpz_H_CallNxtOp"
- "phFriNfc_Tpz_H_ChkCCBytes"
- "phFriNfc_Tpz_H_ChkCCinChkNdef"
- "phFriNfc_Tpz_H_ChkLockBits"
- "phFriNfc_Tpz_H_CpDataToUsrBuf"
- "phFriNfc_Tpz_H_ProCCTLV"
- "phFriNfc_Tpz_H_ProReadAll"
- "phFriNfc_Tpz_H_ProReadID"
- "phFriNfc_Tpz_H_ProWrNMN"
- "phFriNfc_Tpz_H_ProWrTLV"
- "phFriNfc_Tpz_H_ProWrUsrData"
- "phFriNfc_Tpz_H_RdBytes"
- "phFriNfc_Tpz_H_WrAByte"
- "phFriNfc_Tpz_H_WrByte0ValE1"
- "phFriNfc_Tpz_H_WrCCorTLV"
- "phFriNfc_Tpz_H_WrLByte"
- "phFriNfc_Tpz_H_findNDEFTLV"
- "phLibNfc_GetSetRfTransRegCfgComplete: Invalid LibNfc Ctx"
- "phLibNfc_Invoke_Pending_Cb"
- "phLibNfc_P2PSendCmd"
- "phLibNfc_P2PSendComplete"
- "phLibNfc_P2PSendResp"
- "phLibNfc_P2pRemoteDev_ReceiveCb"
- "phLibNfc_P2pRemoteDev_SendCb"
- "phLibNfc_Pending_CntDiscntDisvrychkprsn_Cb"
- "phLibNfc_Pending_Ndeftransv_Cb"
- "phLibNfc_PropMultiTagStatNtfHandler- Independent Prop Tag Detect NTF Rxd"
- "phLibNfc_SM_MwResetTrans failed"
- "phLibNfc_SetDiscPayload:None of the Technologies are configured for P2P Target Mode"
- "phLibNfc_VldtEepromCheckPollParams"
- "phNciNfc_BuildPollNfcDepParams"
- "phNciNfc_CompleteInitSequence: Crc Configuration Failed"
- "phNciNfc_GenDbgLogNtf: Invoke upper layer with Partial generic debug data"
- "phNciNfc_ProcessMfwRfDataPackets : Notification Callback not registered "
- "phNciNfc_StoreReqCrcCfg"
- "phNciNfc_ValidatePollNfcDepParams"
- "phNciNfc_ValidatePollNfcDepParams failed"

```
