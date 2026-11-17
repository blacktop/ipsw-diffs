## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

```diff

-913.64.1.0.0
+913.72.1.0.0
   __TEXT.__const: 0x4b6c0
-  __TEXT.__cstring: 0x49270
-  __TEXT.__os_log: 0x5e03a
-  __TEXT_EXEC.__text: 0x1d1d48
+  __TEXT.__cstring: 0x496b8
+  __TEXT.__os_log: 0x5e2d2
+  __TEXT_EXEC.__text: 0x1d2548
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x2c8
   __DATA.__common: 0x130

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 2998
   Symbols:   0
-  CStrings:  9949
+  CStrings:  9970
 
Functions:
~ sub_fffffe000885a674 -> sub_fffffe00087faa34 : 616 -> 624
~ __ZN9AVE_FwLog10PrintEntryExx : 1796 -> 1816
~ __Z20AVE_CalcBufSizeOfDPB14_E_AVE_DevType14_E_AVE_EncTypeiiii12_E_ChromaFmtbPi -> sub_fffffe0008826af0 : 1992 -> 2088
~ sub_fffffe0008887904 -> sub_fffffe0008827d40 : 56 -> 92
~ sub_fffffe0008887dbc -> sub_fffffe000882821c : 464 -> 556
~ __Z27AVE_CalcBufSizeOfMCTFOutput14_E_AVE_DevTypebiii12_E_ChromaFmtbPi -> sub_fffffe00088295e4 : 1056 -> 1148
~ __Z25AVE_CHM_SetDataInfo_FrameP10_S_AVE_CHMP16_S_AVE_FrameInfoP18AVE_PICMGMT_PARAMS : 624 -> 844
~ __Z28AVE_Client_Enc_Check_ProcessP13_S_AVE_ClientP16_S_AVE_FrameInfo : 1392 -> 2120
~ __Z18AVE_Client_PrepareP13_S_AVE_ClientP14_S_AVE_TimeOutP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKc : 2620 -> 2860
~ __Z16AVE_Client_StartP13_S_AVE_ClientP14_S_AVE_TimeOutjiP21_S_AVE_SurfaceIDInSetP35AVE_SessionSettings_UserKernel_DataPKc : 7788 -> 8040
~ __Z18AVE_Client_ProcessP13_S_AVE_ClientP14_S_AVE_TimeOuti : 1968 -> 1984
~ __Z16AVE_Client_ResetP13_S_AVE_ClientP14_S_AVE_TimeOuti : 1648 -> 1652
~ sub_fffffe00088cff7c -> sub_fffffe0008870a48 : 964 -> 988
~ sub_fffffe0008927b98 -> sub_fffffe00088c867c : 2324 -> 1968
~ __ZN7AVE_HwC15ProcessIntr_CmdEmij : 6540 -> 6476
~ __ZN9AVE_PSGen4InitEyPv14_E_AVE_EncTypeii : 5864 -> 5824
~ sub_fffffe00089d8c28 -> sub_fffffe0008979540 : 68 -> 60
~ __ZN9AVE_SVERC11UpdateStatsExixi14IMG_FRAME_TYPEiiiiP25_S_AVE_DistributedRCStats : 1368 -> 1612
~ sub_fffffe00089e888c -> sub_fffffe0008989290 : 2980 -> 2984
~ __Z28AVE_UCCmd_CheckParam_Prepare12_E_AVE_DevID17_E_AVE_ClientTypeP23S_AVE_UCInParam_Prepare : 488 -> 712
~ __Z26AVE_UCCmd_CheckParam_Start12_E_AVE_DevID17_E_AVE_ClientTypeP21S_AVE_UCInParam_Start : 924 -> 1140
CStrings:
+ "%lld %d AVE %s: %s:%d %s | DPB size overflow %d %d %d %d %lld %lld %lld %lld %lld"
+ "%lld %d AVE %s: %s:%d %s | DPB size overflow %d %d %d %d %lld %lld %lld %lld %lld\n"
+ "%lld %d AVE %s: %s:%d %s | MCTFOutput size overflow %d %d %d %lld %lld %lld %lld %lld"
+ "%lld %d AVE %s: %s:%d %s | MCTFOutput size overflow %d %d %d %lld %lld %lld %lld %lld\n"
+ "%lld %d AVE %s: %s:%d %s | client name not NUL-terminated %d %d %p %lld"
+ "%lld %d AVE %s: %s:%d %s | client name not NUL-terminated %d %d %p %lld\n"
+ "%lld %d AVE %s: %s:%d %s | frame number out of range %p %lld %lld (range: [0,%d])"
+ "%lld %d AVE %s: %s:%d %s | frame number out of range %p %lld %lld (range: [0,%d])\n"
+ "%lld %d AVE %s: %s:%d %s | invalid ANFD entry %d %p %lld %d (%d %d %d %d %d)"
+ "%lld %d AVE %s: %s:%d %s | invalid ANFD entry %d %p %lld %d (%d %d %d %d %d)\n"
+ "%lld %d AVE %s: %s:%d %s | layer ID out of range %p %lld %u %d"
+ "%lld %d AVE %s: %s:%d %s | layer ID out of range %p %lld %u %d\n"
+ "%lld %d AVE %s: %s:%d %s | non-contiguous frame number %p %lld %p %u %lld"
+ "%lld %d AVE %s: %s:%d %s | non-contiguous frame number %p %lld %p %u %lld\n"
+ "%lld %d AVE %s: %s:%d %s | prior stop not drained %p %lld %p %p %p %p"
+ "%lld %d AVE %s: %s:%d %s | prior stop not drained %p %lld %p %p %p %p\n"
+ "%lld %d AVE %s: %s:%d UCInfo epoch still live, prior stop not drained %p %lld %p %p %p %p %d"
+ "%lld %d AVE %s: %s:%d UCInfo epoch still live, prior stop not drained %p %lld %p %p %p %p %d\n"
+ "%lld %d AVE %s: %s::%s CBP0 flag size out of range %p %lld | %u %u"
+ "%lld %d AVE %s: %s::%s CBP0 flag size out of range %p %lld | %u %u\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to find CHM %p %d %lld %d %p"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to find CHM %p %d %lld %d %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to find MD %p %d %lld %lld %d"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to find MD %p %d %lld %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to find client %p %d %lld %lld %d"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to find client %p %d %lld %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d command after client die %p %d %p %d %p %lld | %d | %p %d"
+ "%lld %d AVE %s: %s::%s:%d command after client die %p %d %p %d %p %lld | %d | %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d discard frame command due to client die %p %d %p %p %lld | %d | %d %d %lld %d | %p %d %d"
+ "%lld %d AVE %s: %s::%s:%d discard frame command due to client die %p %d %p %p %lld | %d | %d %d %lld %d | %p %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d receive firmware command %p %d %p %p %p %d %lld %d %d %lld"
+ "%lld %d AVE %s: %s::%s:%d receive firmware command %p %d %p %p %p %d %lld %d %d %lld\n"
+ "913.72.1"
+ "pClient->pcUCInfoPool == NULL && pClient->pcExUCInfoPool == NULL && pClient->sClientSurfaceSet.pcUCInfo == NULL && pClient->sClientSurfaceSet.pcExUCInfo == NULL"
+ "pEntry->iBase > 0 && pEntry->sRect.iX >= 0 && pEntry->sRect.iY >= 0 && pEntry->sRect.iWidth >= 0 && pEntry->sRect.iHeight >= 0"
+ "pFrameData->sGOPInfo.iFrameNum >= 0 && pFrameData->sGOPInfo.iFrameNum <= 2147483647"
+ "pIn->frameNumber == (uint32_t)(pClient->iLastFrameNumber + 1)"
+ "pIn->iLayerID < (uint32_t)pClient->sSessionCfg.sEnc.iLayerNum"
- "%lld %d AVE %s: %s:%d %s | DPB size overflow %d %d %d %d %d %d %d %d %lld"
- "%lld %d AVE %s: %s:%d %s | DPB size overflow %d %d %d %d %d %d %d %d %lld\n"
- "%lld %d AVE %s: %s:%d %s | MCTFOutput size overflow %d %d %d %d %d %d %d %lld"
- "%lld %d AVE %s: %s:%d %s | MCTFOutput size overflow %d %d %d %d %d %d %d %lld\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to find CHM %p %d %lld %d %d %p"
- "%lld %d AVE %s: %s::%s:%d %s | failed to find CHM %p %d %lld %d %d %p\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to find MD %p %d %lld %lld %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | failed to find MD %p %d %lld %lld %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | failed to find client %p %d %lld %lld %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | failed to find client %p %d %lld %lld %d %d\n"
- "%lld %d AVE %s: %s::%s:%d command after client die %p %d %p %d %p %lld | %d 0x%x | %p %d"
- "%lld %d AVE %s: %s::%s:%d command after client die %p %d %p %d %p %lld | %d 0x%x | %p %d\n"
- "%lld %d AVE %s: %s::%s:%d discard frame command due to client die %p %d %p %p %lld | %d 0x%x | %d %d %lld %d | %p %d %d"
- "%lld %d AVE %s: %s::%s:%d discard frame command due to client die %p %d %p %p %lld | %d 0x%x | %d %d %lld %d | %p %d %d\n"
- "%lld %d AVE %s: %s::%s:%d receive firmware command %p %d %p %p %p %d %d %lld %d %d %lld"
- "%lld %d AVE %s: %s::%s:%d receive firmware command %p %d %p %p %p %d %d %lld %d %d %lld\n"
- "913.64.1"
```
