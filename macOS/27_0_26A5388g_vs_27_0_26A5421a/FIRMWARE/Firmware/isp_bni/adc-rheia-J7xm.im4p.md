## adc-rheia-J7xm.im4p

> `Firmware/isp_bni/adc-rheia-J7xm.im4p`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`
- `__DATA.__data_copy`
- `__DATA._rtk_mtab`
- `__DATA.__chain_starts`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x8eee54
-  __TEXT.__const: 0x34886c
+  __TEXT.__text: 0x8efde4
+  __TEXT.__const: 0x348930
   __TEXT.text_env: 0x45b74
-  __TEXT.__cstring: 0xe6ecc
+  __TEXT.__cstring: 0xe7d15
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x37080
+  __DATA.__const: 0x37140
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xd9940
   __DATA._rtk_power: 0x3b8

   __DATA.__mod_init_func: 0x10
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x2de5f8
-  Functions: 8349
+  Functions: 8359
   Symbols:   0
-  CStrings:  25561
+  CStrings:  25637
 
CStrings:
+ " (adjusting)"
+ "23:12:45"
+ "CAICamAnstResV2.cpp"
+ "CISP_CMD_CH_EXTERNAL_SYNC_PULSE_ADJUST"
+ "CISP_CMD_CH_LOCAL_HUEMAP_BUFFER_ENABLE_DUMMY"
+ "CISP_CMD_CH_PIPELINE_DUMP_DUMMY"
+ "CISP_CMD_CH_PREPARE_START_DUMMY"
+ "CMLVNRProcImp.cpp"
+ "EXTSYNC_PULSE_ADJUST not supported for Depth Camera, ignoring\n"
+ "IPCMemAllocation[%u] requestor %s size %zu"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelB1) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelB2) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelB3) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelB4) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelGB1) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelGB2) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelGB3) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelGB4) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelGR1) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelGR2) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelGR3) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelGR4) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelR1) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelR2) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelR3) <= maxBase"
+ "LSC_GET_BASE_U32(pChImbCorrConfig->channelR4) <= maxBase"
+ "LSC_GET_BASE_U32(pLSCTableConfig->channelB) <= maxBase"
+ "LSC_GET_BASE_U32(pLSCTableConfig->channelGB) <= maxBase"
+ "LSC_GET_BASE_U32(pLSCTableConfig->channelGR) <= maxBase"
+ "LSC_GET_BASE_U32(pLSCTableConfig->channelR) <= maxBase"
+ "LSC_GET_BASE_U32(pMacroLSCTableConfig->luma) == 0"
+ "Set Ch:%zu EXTSYNC bAdjustingExternalSyncPulse=%d"
+ "ShowIPCMemoryAllocations"
+ "aneProgramTblTotal %u"
+ "ch %zu EXTSYNC fail fps:%.2f,config: %d framecount: %d, RVSYNC [%llu.%06llu] RVSYNC_Prev [%llu.%06llu]%s"
+ "ch %zu EXTSYNC pass fps:%.2f,config: %d framecount: %d%s"
+ "ch:%zu EXTSYNC_PULSE_ADJUST bAdjusting=%d\n"
+ "eitGainHistory != nullptr"
+ "pChImbCorrConfig->channelB1.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelB1.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelB2.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelB2.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelB3.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelB3.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelB4.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelB4.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelGB1.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelGB1.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelGB2.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelGB2.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelGB3.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelGB3.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelGB4.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelGB4.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelGR1.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelGR1.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelGR2.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelGR2.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelGR3.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelGR3.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelGR4.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelGR4.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelR1.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelR1.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelR2.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelR2.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelR3.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelR3.gridCountY <= maxGridY"
+ "pChImbCorrConfig->channelR4.gridCountX <= maxGridX"
+ "pChImbCorrConfig->channelR4.gridCountY <= maxGridY"
+ "pCmd->chId < CAM_CH_TOT"
+ "pLSCTableConfig->channelB.gridCountX <= maxGridX"
+ "pLSCTableConfig->channelB.gridCountY <= maxGridY"
+ "pLSCTableConfig->channelGB.gridCountX <= maxGridX"
+ "pLSCTableConfig->channelGB.gridCountY <= maxGridY"
+ "pLSCTableConfig->channelGR.gridCountX <= maxGridX"
+ "pLSCTableConfig->channelGR.gridCountY <= maxGridY"
+ "pLSCTableConfig->channelR.gridCountX <= maxGridX"
+ "pLSCTableConfig->channelR.gridCountY <= maxGridY"
+ "pMacroLSCTableConfig->luma.gridCountX <= maxGridX"
+ "pMacroLSCTableConfig->luma.gridCountY <= maxGridY"
+ "pSetCamConfig->index < chDescr->configs"
+ "tbl[%u] module %#x:%c (%#02x) rev %#02x\n"
+ "tuningTable.tb_Sifr != 0"
- "22:21:29"
- "Not sending tuningset to algoctrl due to last frame (idx %u) is raw only\n"
- "ProcessCaptureOutputConfigSet"
- "[DSI] Invalid Structure size allocated!"
- "ch %zu EXTSYNC fail fps:%.2f,config: %d framecount: %d, RVSYNC [%llu.%06llu] RVSYNC_Prev [%llu.%06llu]"
- "ch %zu EXTSYNC pass fps:%.2f,config: %d framecount: %d"
- "ch=%zu, EnterFrameRate(%d) should be not larger than ExitFrameRate(%d)"
- "ch=%zu, EnterThreshold(%d) should be not less than ExitThreshold(%d)"
```
