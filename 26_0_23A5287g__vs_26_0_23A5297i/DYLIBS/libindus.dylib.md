## libindus.dylib

> `/usr/lib/libindus.dylib`

```diff

-93.0.0.0.0
-  __TEXT.__text: 0x13f144
+95.0.1.0.0
+  __TEXT.__text: 0x13e538
   __TEXT.__auth_stubs: 0x860
-  __TEXT.__const: 0x4c70
+  __TEXT.__const: 0x4c80
   __TEXT.__gcc_except_tab: 0x4bf8
-  __TEXT.__cstring: 0x26dbd
+  __TEXT.__cstring: 0x26ccd
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x1ca8
+  __TEXT.__unwind_info: 0x1c88
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x528
+  __DATA_CONST.__const: 0x558
   __AUTH_CONST.__auth_got: 0x438
-  __AUTH_CONST.__const: 0x1d28
+  __AUTH_CONST.__const: 0x1d10
   __AUTH_CONST.__cfstring: 0x20
   __AUTH.__data: 0x3f8
   __DATA.__data: 0x28698

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 7874BCAE-2620-3543-8681-29366A1ED292
-  Functions: 1756
-  Symbols:   5270
-  CStrings:  4023
+  UUID: AEEA3720-8354-3397-AE23-8CE7FF224DC1
+  Functions: 1752
+  Symbols:   5264
+  CStrings:  4011
 
Symbols:
+ __Z21Hal_GnssBaseBandReset21_e_HAL_GNSSTrapReason
+ __Z25Hal29_TriggerTrapOverPCIe21_e_HAL_GNSSTrapReason
+ __ZL19Gnm03_06InitHWResetv
+ ___FUNCTION__._Z21Hal_GnssBaseBandReset21_e_HAL_GNSSTrapReason
+ ___func__._Z21GN_GPS_Hard_Reset_GNBv
+ ___func__._Z24Gnm03_60BaseBandResetReq19e_Gnm_BbResetReason
- __Z16GncP19_01ResetCB15e_HAL_RetStatus
- __Z20GncP19_02TrigHWResetv
- __Z20Hal32_SetPowerReportb
- __Z21Hal_GnssBaseBandResetPFv15e_HAL_RetStatusE
- __Z24GncP08_03HandleHardResetPKc
- __Z29GncP19_03HandleResetStatusIndP11t_MsgHeader
- __ZL13g_MEResetInfo.0
- __ZL13g_MEResetInfo.1
- __ZL19g_PowerReportStatus
- __ZL21Gnm03_BasebandResetCb15e_HAL_RetStatus
- ___FUNCTION__._Z20GncP19_02TrigHWResetv
- ___func__._Z21Hal_GNSS_SessionStartv
- ___func__._Z21Hal_GnssBaseBandResetPFv15e_HAL_RetStatusE
CStrings:
+ "%10u %s%c %s: #%04hx pcie trap command\n"
+ "%10u %s%c %s: GNSS SW triggered #Trap: %s\n"
+ "%10u %s%c %s: GNSS session start, CD_NO_PE_DATA,%c, FTA_Log,%c, ProxyCD,%c\n"
+ "%10u %s%c %s: No ME data, LastReadMEData,%u, WDTExpiryCounter,%d\n"
+ "G5K_ME_Decode_Meas: GN_GPS_Hard_Reset_GNB >6 Checksum Errors in <=5000 ms !"
+ "GNSS HW failure detected"
+ "GNSS HW init sequence failed"
+ "GNSS HW reported transport error event"
+ "GNSS HW wake failed, GNSS read revision post SPMI wake failed"
+ "GNSS ME NV data restore failed"
+ "GNSS ME coex configuration failed"
+ "GNSS ME failed to ACK for sleep entry"
+ "GNSS PE requested GNSS HW reset"
+ "GNSS SW received generic failure response"
+ "Hal29_TriggerTrapOverPCIe"
+ "Jul 12 2025"
+ "SW did not receice GNSS ME data"
+ "Unknown reason for triggering trap"
+ "v2.111.3.2025-07-11"
- "%10u %s%c %s: #%04hx ### GNSS crash detected ### - Reason %s\n"
- "%10u %s%c %s: #%04hx ### GNSS crash detected ###, No data received for %u ms\n"
- "%10u %s%c %s: #%04hx HWError\n"
- "%10u %s%c %s: #%04hx WaitBeforeStart,%ums\n"
- "%10u %s%c %s: #%04hx status,%s\n"
- "%10u %s%c %s: #%04hx status,%s err,%x\n"
- "%10u %s%c %s: FSM:GNCP_HOST_RESET_CB_IND =>GNCP Stat,%u\n"
- "%10u %s%c %s: FSM:GNCP_HOST_RESET_CB_IND Status,%u\n"
- "%10u %s%c %s: FSM:GNCP_HW_RESET_REQ =>GNCP\n"
- "%10u %s%c %s: GNSS session start, EN_PE_NO_DATA_FW_RECOVERY_COREDUMP\n"
- "%10u %s%c %s: No ME data, LastReadMEData,%u\n"
- "%10u %s%c %s: Success,%s\n"
- "%10u %s%c %s: status ,%hhu\n"
- "Dis"
- "En"
- "G5K_ME_Decode_Meas: GN_GPS_Hard_Reset_GNB >4 Checksum Errors in <=3000 ms !"
- "GncP08_03HandleHardReset"
- "GncP19_01ResetCB"
- "GncP19_02TrigHWReset"
- "GncP19_03HandleResetStatusInd"
- "Gnm03_BasebandResetCb"
- "Hal32_SetPowerReport"
- "Jun 26 2025"
- "No ME Data"
- "Sleep ACK delayed"
- "Timeout in state transition"
- "eBetaTableRestoreFailure"
- "eBetaTableRestoreTimeout"
- "eGNSS_FW_NV_RestoreTimeOut"
- "eOTHER"
- "v2.110.0.2025-06-14"

```
