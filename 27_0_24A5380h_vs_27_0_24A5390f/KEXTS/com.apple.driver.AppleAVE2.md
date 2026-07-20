## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-913.8.0.0.0
-  __TEXT.__const: 0x4b760
-  __TEXT.__cstring: 0x4736f
-  __TEXT.__os_log: 0x5bc39
-  __TEXT_EXEC.__text: 0x1c9a80
+913.29.1.0.0
+  __TEXT.__const: 0x4b680
+  __TEXT.__cstring: 0x47f24
+  __TEXT.__os_log: 0x5c7be
+  __TEXT_EXEC.__text: 0x1cd2a0
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x2c8
   __DATA.__common: 0x130
   __DATA.__bss: 0x3c0
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0xb020
+  __DATA_CONST.__const: 0xae10
   __DATA_CONST.__kalloc_type: 0x5300
   __DATA_CONST.__kalloc_var: 0x1e00
   __DATA_CONST.__auth_got: 0x3d8

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 2994
   Symbols:   0
-  CStrings:  9759
+  CStrings:  9847
 
Functions:
~ __ZN13AVE_MD_Crypto14PrepareTaskCmdEPK14_S_AVE_CmdInfoP23_S_AVE_TaskInCmd_Crypto : 756 -> 748
~ __Z22AVE_AXI2AF_GetTunables12_E_AVE_DevIDjiPPK17_S_AVE_AXI2AF_Cfg : 1324 -> 1276
~ sub_fffffe000871b4a0 -> sub_fffffe0008727f18 : 140 -> 444
~ __Z26AVE_CalcBufSizeOfCodedDatai14_E_AVE_DevType14_E_AVE_EncTypeii12_E_ChromaFmtiibb14_E_AVE_EncMode13_E_AVE_RCModeii : 1148 -> 1368
~ sub_fffffe000871bc08 -> sub_fffffe000872888c : 172 -> 508
~ sub_fffffe000871bd28 -> sub_fffffe0008728afc : 72 -> 348
~ sub_fffffe000871bd70 -> sub_fffffe0008728c58 : 108 -> 400
~ sub_fffffe000871be90 -> sub_fffffe0008728e9c : 1640 -> 1988
~ sub_fffffe000871c54c -> sub_fffffe00087296b4 : 180 -> 520
~ sub_fffffe000871c6a4 -> sub_fffffe0008729960 : 900 -> 1168
~ sub_fffffe000871ca48 -> sub_fffffe0008729e10 : 264 -> 580
~ sub_fffffe000871cbd8 -> sub_fffffe000872a0dc : 656 -> 1036
~ sub_fffffe000871ced8 -> sub_fffffe000872a558 : 144 -> 460
~ sub_fffffe000871cf7c -> sub_fffffe000872a738 : 116 -> 428
~ sub_fffffe000871d000 -> sub_fffffe000872a8f4 : 76 -> 368
~ sub_fffffe000871d060 -> sub_fffffe000872aa78 : 104 -> 368
~ sub_fffffe000871d0dc -> sub_fffffe000872abfc : 156 -> 428
~ sub_fffffe000871d1a0 -> sub_fffffe000872add0 : 92 -> 360
~ sub_fffffe000871d218 -> sub_fffffe000872af54 : 80 -> 360
~ sub_fffffe000871d284 -> sub_fffffe000872b0d8 : 64 -> 348
~ sub_fffffe000871d2e0 -> sub_fffffe000872b250 : 152 -> 436
~ sub_fffffe000871d430 -> sub_fffffe000872b4bc : 208 -> 488
~ sub_fffffe000871d514 -> sub_fffffe000872b6b8 : 64 -> 336
~ sub_fffffe000871d62c -> sub_fffffe000872b8e0 : 736 -> 1052
~ __Z27AVE_CHM_MakeFwCmd_Start_AV1P10_S_AVE_CHMyjP14_S_AVE_TimeOutP16sCAveCmdAv1Start : 1724 -> 1728
~ __Z25AVE_CHM_SetDataInfo_FrameP10_S_AVE_CHMP16_S_AVE_FrameInfoP18AVE_PICMGMT_PARAMS : 616 -> 620
~ __Z25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMS : 20540 -> 23124
~ __Z23AVE_Client_Enc_PrintAVCP13_S_AVE_ClientjiPKci : 4236 -> 4232
~ sub_fffffe000874b858 -> sub_fffffe000875a664 : 136 -> 132
~ sub_fffffe000874bfe4 -> sub_fffffe000875adec : 504 -> 496
~ __Z26AVE_Client_CheckCommonInfoP13_S_AVE_ClientbP35AVE_SessionSettings_UserKernel_Data : 2520 -> 2304
~ __Z20AVE_Client_CheckInfoP13_S_AVE_ClientbP35AVE_SessionSettings_UserKernel_Data : 1356 -> 2020
~ __Z17AVE_Client_VerifyP13_S_AVE_ClientbP35AVE_SessionSettings_UserKernel_Data : 740 -> 752
~ __Z16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutjiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKc : 7792 -> 7804
~ sub_fffffe000875907c -> __Z22AVE_Client_PrintStatusP13_S_AVE_ClientjiPKci : 1456 -> 1468
~ __Z18AVE_Client_ProcessP13_S_AVE_ClientP14_S_AVE_TimeOuti : 1952 -> 1964
~ __Z19AVE_Client_CompleteP13_S_AVE_ClientP14_S_AVE_TimeOuti : 1632 -> 1644
~ __Z16AVE_Client_FlushP13_S_AVE_ClientP14_S_AVE_TimeOuti : 1632 -> 1644
~ __Z16AVE_Client_ResetP13_S_AVE_ClientP14_S_AVE_TimeOuti : 1632 -> 1644
~ __Z20AVE_Client_AppendCmdP13_S_AVE_Client10_E_AVE_Cmd15_E_AVE_Cmd_ModejP14_S_AVE_TimeOutPv : 1368 -> 1444
~ __Z29AVE_Client_VerifyDataResourceP13_S_AVE_ClientP14_S_AVE_CmdInfoiyP16_S_AVE_FrameInfo : 1600 -> 1596
~ sub_fffffe000875f238 -> sub_fffffe000876e294 : 408 -> 404
~ sub_fffffe000875f908 -> sub_fffffe000876e960 : 388 -> 384
~ __Z27AVE_TaskCmd_LACost_SetInputPK14_S_AVE_CmdInfoiiiPK21_S_AVE_SurfaceInfoSetP23_S_AVE_TaskInCmd_LACost : 404 -> 416
~ __ZL16AVE_LAGOP_DecideP10_S_AVE_CHMP10_S_AVE_Cmd : 3916 -> 3864
~ __ZN7AVE_Drv22ProcessInputCmd_AssignEP13_S_AVE_ClientP10_S_AVE_Cmd : 3016 -> 3008
~ sub_fffffe00087a4900 -> sub_fffffe00087b3924 : 88 -> 84
~ __ZN6AVE_MD13PrintCmdStatsEjjiPKci : 836 -> 832
~ __ZN7AVE_HwC9SendFwCmdEP10_S_AVE_CHMPviS2_ : 1820 -> 2076
~ __ZN7AVE_SwC15ProcessIntr_CmdEm : 3396 -> 3424
~ __ZN8HEVC_VPS24video_parameter_set_rbspEv : 1436 -> 1468
~ sub_fffffe0008815ad4 -> sub_fffffe0008824c2c : 1668 -> 1724
~ __ZN8HEVC_VPS13vps_extensionEv : 3184 -> 3420
~ _AVE_VSNPrintf -> __Z23AVE_Prop_Cfg_HEVC_PrintP20_S_AVE_Prop_Cfg_HEVCjiPKci : 46564 -> 48444
~ __Z22AVE_CreateDataSurfacesP14AVE_SurfaceMgrP4taskP23_S_AVE_SurfaceIDDataSetP21_S_AVE_SurfaceInfoSetyjP21_S_AVE_SurfaceDataSet : 4256 -> 5612
~ __Z23AVE_DARTMapDataSurfacesP14AVE_SurfaceMgrP21_S_AVE_SurfaceDataSetP21_S_AVE_SurfaceInfoSetj : 3140 -> 4000
~ sub_fffffe0008856fc8 -> sub_fffffe0008867244 : 96 -> 92
~ __ZN10AVE_MD_SVE23DARTMapExternalSurfacesEy : 1096 -> 1092
~ sub_fffffe0008859b40 -> sub_fffffe0008869db4 : 604 -> 600
~ __ZN10AVE_MD_SVE23DARTMapInternalSurfacesEy : 1124 -> 1120
~ sub_fffffe000885a200 -> sub_fffffe000886a46c : 604 -> 600
~ __Z22AVE_Work_Enc_TuneParamP13_S_AVE_Clientii : 1848 -> 1860
~ sub_fffffe00088775c0 -> sub_fffffe0008887834 : 300 -> 332
~ sub_fffffe00088778b4 -> sub_fffffe0008887b48 : 272 -> 284
~ sub_fffffe0008877d94 -> sub_fffffe0008888034 : 228 -> 240
~ sub_fffffe000888d9e4 -> sub_fffffe000889dc90 : 200 -> 204
~ sub_fffffe000888daac -> sub_fffffe000889dd5c : 320 -> 324
~ sub_fffffe000888dbec -> sub_fffffe000889dea0 : 320 -> 324
~ sub_fffffe000888dd2c -> sub_fffffe000889dfe4 : 352 -> 360
~ sub_fffffe000888de8c -> sub_fffffe000889e14c : 328 -> 332
~ sub_fffffe00088a8874 -> sub_fffffe00088b8b38 : 44 -> 56
CStrings:
+ "%lld %d AVE %s: %p %lld AuxLayer[%d]: profile=%s width=%d height=%d"
+ "%lld %d AVE %s: %p %lld AuxLayer[%d]: profile=%s width=%d height=%d\n"
+ "%lld %d AVE %s: %p %lld AuxiliaryLayerProperties num=%d"
+ "%lld %d AVE %s: %p %lld AuxiliaryLayerProperties num=%d\n"
+ "%lld %d AVE %s: %p %lld EncodesAuxiliaryWithAuxID=%d"
+ "%lld %d AVE %s: %p %lld EncodesAuxiliaryWithAuxID=%d\n"
+ "%lld %d AVE %s: %p %lld HEVCAuxiliaryIDs [%d] %d"
+ "%lld %d AVE %s: %p %lld HEVCAuxiliaryIDs [%d] %d\n"
+ "%lld %d AVE %s: %p %lld HEVCAuxiliaryIDs num=%d"
+ "%lld %d AVE %s: %p %lld HEVCAuxiliaryIDs num=%d\n"
+ "%lld %d AVE %s: %p %lld HEVCAuxiliaryLayerIDs [%d] %d"
+ "%lld %d AVE %s: %p %lld HEVCAuxiliaryLayerIDs [%d] %d\n"
+ "%lld %d AVE %s: %p %lld HEVCAuxiliaryLayerIDs num=%d"
+ "%lld %d AVE %s: %p %lld HEVCAuxiliaryLayerIDs num=%d\n"
+ "%lld %d AVE %s: %s:%d %s | DPB size overflow %d %d %d %d %d %d %d %d %lld"
+ "%lld %d AVE %s: %s:%d %s | DPB size overflow %d %d %d %d %d %d %d %d %lld\n"
+ "%lld %d AVE %s: %s:%d %s | EncType mismatch with session %p %lld %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | EncType mismatch with session %p %lld %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HSCOutput size overflow %d %d %d %d %d %d %d %lld"
+ "%lld %d AVE %s: %s:%d %s | HSCOutput size overflow %d %d %d %d %d %d %d %lld\n"
+ "%lld %d AVE %s: %s:%d %s | LRB size overflow %d %d %d %d %d %d %d %d %lld"
+ "%lld %d AVE %s: %s:%d %s | LRB size overflow %d %d %d %d %d %d %d %d %lld\n"
+ "%lld %d AVE %s: %s:%d %s | MCTFOutput size overflow %d %d %d %d %d %d %d %lld"
+ "%lld %d AVE %s: %s:%d %s | MCTFOutput size overflow %d %d %d %d %d %d %d %lld\n"
+ "%lld %d AVE %s: %s:%d %s | frame dimension out of range %p %lld %d %d %d %lld"
+ "%lld %d AVE %s: %s:%d %s | frame dimension out of range %p %lld %d %d %d %lld\n"
+ "%lld %d AVE %s: %s:%d %s | invalid L%d%c low res ref firmware buffer in direct mode %p %d %lld %p %lld | %d %p"
+ "%lld %d AVE %s: %s:%d %s | invalid L%d%c low res ref firmware buffer in direct mode %p %d %lld %p %lld | %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid L%d%c ref firmware buffer in direct mode %p %d %lld %p %lld | %d %p"
+ "%lld %d AVE %s: %s:%d %s | invalid L%d%c ref firmware buffer in direct mode %p %d %lld %p %lld | %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | invalid LRMERC result in direct encode mode %p %d %lld %p %lld | %d"
+ "%lld %d AVE %s: %s:%d %s | invalid LRMERC result in direct encode mode %p %d %lld %p %lld | %d\n"
+ "%lld %d AVE %s: %s:%d %s | pixel area overflow %d %d %d %d %lld"
+ "%lld %d AVE %s: %s:%d %s | pixel area overflow %d %d %d %d %lld\n"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %d %d %lld"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %d %d %lld\n"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %d %lld"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %d %lld\n"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %d %lld %lld"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %d %lld %lld\n"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %lld"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %lld\n"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %lld %lld"
+ "%lld %d AVE %s: %s:%d %s | size overflow %d %d %lld %lld\n"
+ "%lld %d AVE %s: %s:%d %s | slice number is out of range %p %lld %d %d [%d %d]"
+ "%lld %d AVE %s: %s:%d %s | slice number is out of range %p %lld %d %d [%d %d]\n"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid command slot %p %d %p %p %d %p %d [0, %d)"
+ "%lld %d AVE %s: %s::%s:%d %s | invalid command slot %p %d %p %p %d %p %d [0, %d)\n"
+ "%p %lld AuxLayer[%d]: profile=%s width=%d height=%d"
+ "%p %lld AuxLayer[%d]: profile=%s width=%d height=%d\n"
+ "%p %lld AuxiliaryLayerProperties num=%d"
+ "%p %lld AuxiliaryLayerProperties num=%d\n"
+ "%p %lld EncodesAuxiliaryWithAuxID=%d"
+ "%p %lld EncodesAuxiliaryWithAuxID=%d\n"
+ "%p %lld HEVCAuxiliaryIDs [%d] %d"
+ "%p %lld HEVCAuxiliaryIDs [%d] %d\n"
+ "%p %lld HEVCAuxiliaryIDs num=%d"
+ "%p %lld HEVCAuxiliaryIDs num=%d\n"
+ "%p %lld HEVCAuxiliaryLayerIDs [%d] %d"
+ "%p %lld HEVCAuxiliaryLayerIDs [%d] %d\n"
+ "%p %lld HEVCAuxiliaryLayerIDs num=%d"
+ "%p %lld HEVCAuxiliaryLayerIDs num=%d\n"
+ "0 <= fwCmdSlot && fwCmdSlot < (AVE_Cmd_Max + (((3 + 2) + 2 + 5 + (2 + 1)) * ((2) < ((63 + 1)) ? (2) : ((63 + 1)))))"
+ "0 <= pInfo->sSessionCfg.sEnc.sSliceMap.iNum && pInfo->sSessionCfg.sEnc.sSliceMap.iNum <= ((32) < (256) ? (32) : (256))"
+ "11121111111111111111111111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222222222222222222222222222222222222222222222222222222222222222222"
+ "21:36:33"
+ "913.29.1"
+ "AVE_CalcBufSizeOfColoFwDataInfo"
+ "AVE_CalcBufSizeOfColocated"
+ "AVE_CalcBufSizeOfDPB"
+ "AVE_CalcBufSizeOfEntropyCoding"
+ "AVE_CalcBufSizeOfEntropyCodingHeader"
+ "AVE_CalcBufSizeOfHSCOutput"
+ "AVE_CalcBufSizeOfLFSOutput"
+ "AVE_CalcBufSizeOfLRB"
+ "AVE_CalcBufSizeOfLRSOutput"
+ "AVE_CalcBufSizeOfMBInputCtrl"
+ "AVE_CalcBufSizeOfMBStats"
+ "AVE_CalcBufSizeOfMCTFOutput"
+ "AVE_CalcBufSizeOfSTFSrcNeighborInfo"
+ "AVE_CalcBufSizeOfSrcNeighborAboveFltPixel"
+ "AVE_CalcBufSizeOfSrcNeighborData"
+ "AVE_CalcBufSizeOfSrcNeighborFwData"
+ "AVE_CalcBufSizeOfSrcNeighborInfo"
+ "AVE_CalcBufSizeOfSrcNeighborLeftInfo"
+ "AVE_CalcBufSizeOfSrcNeighborLeftPixel"
+ "AVE_CalcBufSizeOfSrcNeighborPixel"
+ "AVE_CalcBufSizeOfStaticAreaCBP0Cntr"
+ "Jul 14 2026"
+ "iLumaDataSize >= 0 && iLumaHeaderSize >= 0 && iChromaDataSize >= 0 && iChromaHeaderSize >= 0 && iTotal <= 2147483647"
+ "iPixelArea >= 0 && iPixelArea <= 2147483647"
+ "iSize >= 0 && iSize <= 2147483647"
+ "pInfo->sSessionCfg.sEnc.eType == pClient->eEncType"
+ "size >= 0 && size <= 2147483647"
+ "width >= 0 && height >= 0 && iPixelProduct <= 2147483647"
- "%lld %d AVE %s: %s:%d %s | slice number is out of range %p %lld %d %d (%d %d]"
- "%lld %d AVE %s: %s:%d %s | slice number is out of range %p %lld %d %d (%d %d]\n"
- "0 < pInfo->sSessionCfg.sEnc.sSliceMap.iNum && pInfo->sSessionCfg.sEnc.sSliceMap.iNum <= ((32) < (256) ? (32) : (256))"
- "111211111111111111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222121222222222222222222222222222222222222222222222222222222222222222222"
- "21:20:05"
- "913.8.0"
- "Jun 29 2026"
```
