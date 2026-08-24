## adc-eris-j129.im4p

> `Firmware/isp_bni/adc-eris-j129.im4p`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`
- `__DATA.__data_copy`
- `__DATA._fwinfo`
- `__DATA._rtk_mtab`
- `__DATA.__chain_starts`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x985480
-  __TEXT.__const: 0x24fc50
+  __TEXT.__text: 0x9871c4
+  __TEXT.__const: 0x24fcd4
   __TEXT.text_env: 0xef0
-  __TEXT.__cstring: 0xf468e
+  __TEXT.__cstring: 0xf55d1
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x3b240
+  __DATA.__const: 0x3b310
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xdb718
   __DATA._rtk_power: 0x3f8

   __DATA.__chain_starts: 0x28
   __DATA.__mod_init_func: 0x8
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x862ef8
-  Functions: 8448
+  __DATA.__zerofill: 0x85eef8
+  Functions: 8456
   Symbols:   0
-  CStrings:  27026
+  CStrings:  27107
 
CStrings:
+ "23:12:38"
+ "CAICamAnstResV2.cpp"
+ "CISP_CMD_CH_EXTERNAL_SYNC_PULSE_ADJUST"
+ "CISP_CMD_CH_LOCAL_HUEMAP_BUFFER_ENABLE_DUMMY"
+ "CISP_CMD_CH_PIPELINE_DUMP_DUMMY"
+ "CISP_CMD_CH_PREPARE_START_DUMMY"
+ "CMLVNRProcImp.cpp"
+ "EXTSYNC_PULSE_ADJUST not supported for Depth Camera, ignoring\n"
+ "GDCTable"
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
+ "MemTable in AlgoControl Mismatch with Driver Algo:%llu DistDrv:%llu"
+ "ShowIPCMemoryAllocations"
+ "aneProgramTblTotal %u"
+ "ch:%zu EXTSYNC_PULSE_ADJUST bAdjusting=%d\n"
+ "ch=%ld,Raw:%dx%d, FES:%dx%d, CropIn:%d %d %dx%d, Center:%d %d"
+ "ch=%ld,frame=%d,%d->%d optC:%d %d cxyX %f %f fes %d raw %d,DynGDC=%d %d"
+ "eitGainHistory != nullptr"
+ "maxRadius %d, Radius %d radScale %d outw %d outh %d"
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
+ "warpM3BufSizeInWord %d\n"
- "22:20:44"
- "Not sending tuningset to algoctrl due to last frame (idx %u) is raw only\n"
- "[DSI] Invalid Structure size allocated!"
- "ch=%zu, EnterFrameRate(%d) should be not larger than ExitFrameRate(%d)"
- "ch=%zu, EnterThreshold(%d) should be not less than ExitThreshold(%d)"
```
