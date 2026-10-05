## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

```diff

-913.48.1.0.0
-  __TEXT.__const: 0x4b6f0
-  __TEXT.__cstring: 0x48053
-  __TEXT.__os_log: 0x5cac2
-  __TEXT_EXEC.__text: 0x1cde98
+913.63.1.0.0
+  __TEXT.__const: 0x4b6c0
+  __TEXT.__cstring: 0x491f4
+  __TEXT.__os_log: 0x5decc
+  __TEXT_EXEC.__text: 0x1d1a28
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x2c8
   __DATA.__common: 0x130
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0xae10
+  __DATA_CONST.__const: 0xad60
   __DATA_CONST.__kalloc_type: 0x5300
   __DATA_CONST.__kalloc_var: 0x1e00
   __DATA_CONST.__auth_got: 0x3d8
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 2995
+  Functions: 2998
   Symbols:   0
-  CStrings:  9866
+  CStrings:  9945
 
CStrings:
+ "%d Kernel: %p %p"
+ "%lld %d AVE %s: %s:%d %s | AV1 MCTF strength count out of range %d %d [0 %d]"
+ "%lld %d AVE %s: %s:%d %s | AV1 MCTF strength count out of range %d %d [0 %d]\n"
+ "%lld %d AVE %s: %s:%d %s | AVC PPS count is out of range %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | AVC PPS count is out of range %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | AVC bit depth is not supported %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | AVC bit depth is not supported %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | AVC log2_max is out of range %d %d %d (max %d)"
+ "%lld %d AVE %s: %s:%d %s | AVC log2_max is out of range %d %d %d (max %d)\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC MCTF strength count out of range %d %d [0 %d]"
+ "%lld %d AVE %s: %s:%d %s | HEVC MCTF strength count out of range %d %d [0 %d]\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC PPS count is out of range %d %d %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC PPS count is out of range %d %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC RPS count is out of range %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC RPS count is out of range %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC SPS count is out of range %d %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC SPS count is out of range %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS count is out of range %d %d %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS count is out of range %d %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS extension layer/OLS counts are out of range %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS extension layer/OLS counts are out of range %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS highest_layer_idx_plus1 sum is out of range %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS highest_layer_idx_plus1 sum is out of range %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS layer-set total is out of range %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS layer-set total is out of range %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS layer_id_in_nuh is out of range %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS layer_id_in_nuh is out of range %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS num_add_layer_sets is out of range %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS num_add_layer_sets is out of range %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS output-layer-set total is out of range %d %d %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS output-layer-set total is out of range %d %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS vps_max_layers_minus1 is out of range %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | HEVC VPS vps_max_layers_minus1 is out of range %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | HEVC log2_max_pic_order_cnt_lsb_minus4 is out of range %d %d %d (max %d)"
+ "%lld %d AVE %s: %s:%d %s | HEVC log2_max_pic_order_cnt_lsb_minus4 is out of range %d %d %d (max %d)\n"
+ "%lld %d AVE %s: %s:%d %s | LRME info is not correct %p %lld %d"
+ "%lld %d AVE %s: %s:%d %s | LRME info is not correct %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | MCTF info is not correct %p %lld %d"
+ "%lld %d AVE %s: %s:%d %s | MCTF info is not correct %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | MCTF strength count out of range %p %lld %d [0 %d]"
+ "%lld %d AVE %s: %s:%d %s | MCTF strength count out of range %p %lld %d [0 %d]\n"
+ "%lld %d AVE %s: %s:%d %s | number of sub layer is out of range %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | number of sub layer is out of range %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | number of temporal layers (prop) is out of range %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | number of temporal layers (prop) is out of range %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | source and destination alias %p %d %p"
+ "%lld %d AVE %s: %s:%d %s | source and destination alias %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | too many parameter sets %d %d %d %p %d"
+ "%lld %d AVE %s: %s:%d %s | too many parameter sets %d %d %d %p %d\n"
+ "%lld %d AVE %s: %s:%d %s | too many parameter sets %p %d %d %d %p %d"
+ "%lld %d AVE %s: %s:%d %s | too many parameter sets %p %d %d %d %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | DispatchCmd failed %p %lld %p %lld | %lld %d"
+ "%lld %d AVE %s: %s::%s:%d %s | DispatchCmd failed %p %lld %p %lld | %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | GOPMgr Process failed %p %lld %p %lld | %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | GOPMgr Process failed %p %lld %p %lld | %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | iRefNum is out of range %p %lld | %d [%d %d]"
+ "%lld %d AVE %s: %s::%s:%d %s | iRefNum is out of range %p %lld | %d [%d %d]\n"
+ "%lld %d AVE %s: FwLog %p %d | Phy %p Kernel %p DART %p | %d %d %d | %d %d"
+ "%lld %d AVE %s: FwLog %p %d | Phy %p Kernel %p DART %p | %d %d %d | %d %d\n"
+ "%lld %d AVE %s: HwC %s | %p %d | IPC: %p IPC Surface: %p Heap: %p Command Buffer: %p %d Notify Buffer: %p %d"
+ "%lld %d AVE %s: HwC %s | %p %d | IPC: %p IPC Surface: %p Heap: %p Command Buffer: %p %d Notify Buffer: %p %d\n"
+ "%lld %d AVE %s: Mapper %s | %p %d %d | State: %d BaseAddr: %p size: 0x%llx Page Size: 0x%llx"
+ "%lld %d AVE %s: Mapper %s | %p %d %d | State: %d BaseAddr: %p size: 0x%llx Page Size: 0x%llx\n"
+ "%p %lld "
+ "(uint32_t)pVPS->num_add_olss + pVPS->vps_num_layer_sets_minus1 + 1 + pVPS->num_add_layer_sets <= (63 + 1)"
+ "(uint32_t)pVPS->vps_num_layer_sets_minus1 + 1 + pVPS->num_add_layer_sets <= (63 + 1)"
+ "0 < pInfo->sSessionCfg.sEnc.sAlgCfg.sGOP.iNumOfTemporalLayer && (pInfo->sSessionCfg.sEnc.sAlgCfg.sGOP.iNumOfTemporalLayer <= 7)"
+ "0 <= iNum && iNum < (1 + ((2) < ((63 + 1)) ? (2) : ((63 + 1))) * (1 + 9 ))"
+ "0 <= iRefNum && iRefNum <= iMaxRefNum"
+ "0 <= pInfo->sSessionCfg.sEnc.sAlgCfg.sGOP.iNumOfTemporalLayer && (pInfo->sSessionCfg.sEnc.sAlgCfg.sGOP.iNumOfTemporalLayer <= 7)"
+ "0 <= pInfo->uPropCfg.sHEVC.iNumberOfTemporalLayers && pInfo->uPropCfg.sHEVC.iNumberOfTemporalLayers <= 7"
+ "4 <= pInfo->sSyntaxCfgAVC.iLog2MaxFrameNum && pInfo->sSyntaxCfgAVC.iLog2MaxFrameNum <= (12 + 4) && 4 <= pInfo->sSyntaxCfgAVC.iLog2MaxPOCLsb && pInfo->sSyntaxCfgAVC.iLog2MaxPOCLsb <= (12 + 5)"
+ "913.63.1"
+ "AVE_Client_CheckLRMEInfo"
+ "AVE_Client_CheckMCTFInfo"
+ "AVE_HEVC_CheckVPSExtBounds"
+ "FwLog %p %d | Phy %p Kernel %p DART %p | %d %d %d | %d %d"
+ "FwLog %p %d | Phy %p Kernel %p DART %p | %d %d %d | %d %d\n"
+ "HwC %s | %p %d | IPC: %p IPC Surface: %p Heap: %p Command Buffer: %p %d Notify Buffer: %p %d"
+ "HwC %s | %p %d | IPC: %p IPC Surface: %p Heap: %p Command Buffer: %p %d Notify Buffer: %p %d\n"
+ "Mapper %s | %p %d %d | State: %d BaseAddr: %p size: 0x%llx Page Size: 0x%llx"
+ "Mapper %s | %p %d %d | State: %d BaseAddr: %p size: 0x%llx Page Size: 0x%llx\n"
+ "layerNumSum <= (63 + 1)"
+ "pInfo->sHEVC_RPS.strps.num_short_term_ref_pic_sets < 65 && (pInfo->sHEVC_RPS.slice_ltrps.num_long_term_sps + pInfo->sHEVC_RPS.slice_ltrps.num_long_term_pics) <= 16"
+ "pInfo->sHEVC_VPS.num_add_layer_sets <= (63 + 1)"
+ "pInfo->sHEVC_VPS.vps_max_sub_layers_minus1 < 7 && pInfo->sHEVC_VPS.vps_num_layer_sets_minus1 < 16 && pInfo->sHEVC_VPS.vps_num_hrd_parameters <= 16 && pInfo->sHEVC_VPS.vps_num_rep_formats_minus1 < 2 && pInfo->sHEVC_VPS.vps_max_layer_id < (64 - 1)"
+ "pInfo->sSyntaxCfgAVC.iBitDepthLuma == 8 && pInfo->sSyntaxCfgAVC.iBitDepthChroma == 8"
+ "pInfo->sSyntaxCfgAVC.iNumSliceGroups == 1 && 1 <= pInfo->sSyntaxCfgAVC.iNumRefIdxL0DefaultActive && pInfo->sSyntaxCfgAVC.iNumRefIdxL0DefaultActive <= (15 + 1) && 1 <= pInfo->sSyntaxCfgAVC.iNumRefIdxL1DefaultActive && pInfo->sSyntaxCfgAVC.iNumRefIdxL1DefaultActive <= (15 + 1)"
+ "pInfo->saHEVC_PPS[i].num_tile_columns_minus1 <= 256 && pInfo->saHEVC_PPS[i].num_tile_rows_minus1 <= 256 && pInfo->saHEVC_PPS[i].chroma_qp_offset_list_len_minus1 <= 5 && pInfo->saHEVC_PPS[i].num_extra_slice_header_bits == 0"
+ "pInfo->saHEVC_SPS[i].log2_max_pic_order_cnt_lsb_minus4 <= 12"
+ "pInfo->saHEVC_SPS[i].sps_max_sub_layers_minus1 < 7 && pInfo->saHEVC_SPS[i].num_long_term_ref_pics_sps <= 16"
+ "pInfo->uPropCfg.sAV1.iMCTFStrengthLevelNum >= 0 && pInfo->uPropCfg.sAV1.iMCTFStrengthLevelNum <= ((2) < ((63 + 1)) ? (2) : ((63 + 1)))"
+ "pInfo->uPropCfg.sHEVC.iMCTFStrengthLevelNum >= 0 && pInfo->uPropCfg.sHEVC.iMCTFStrengthLevelNum <= ((2) < ((63 + 1)) ? (2) : ((63 + 1)))"
+ "pInfo->uPropCfg.sMCTF.iMCTFStrengthLevelNum >= 0 && pInfo->uPropCfg.sMCTF.iMCTFStrengthLevelNum <= ((2) < ((63 + 1)) ? (2) : ((63 + 1)))"
+ "pVPS->layer_id_in_nuh[i] < (63 + 1)"
+ "pVPS->vps_max_layers_minus1 < (63 + 1)"
+ "psPSCtxSrc != psPSCtxDst"
- "%d Kernel: %p 0x%lx"
- "%lld %d AVE %s: %s:%d %s | number of sub layer is out of range %d %d %d %d"
- "%lld %d AVE %s: %s:%d %s | number of sub layer is out of range %d %d %d %d\n"
- "%lld %d AVE %s: FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d | %d %d"
- "%lld %d AVE %s: FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d | %d %d\n"
- "%lld %d AVE %s: HwC %s | %p %d | IPC: %p IPC Surface: %p Heap: %p Command Buffer: 0x%lx %d Notify Buffer: 0x%lx %d"
- "%lld %d AVE %s: HwC %s | %p %d | IPC: %p IPC Surface: %p Heap: %p Command Buffer: 0x%lx %d Notify Buffer: 0x%lx %d\n"
- "%lld %d AVE %s: Mapper %s | %p %d %d | State: %d BaseAddr: 0x%llx size: 0x%llx Page Size: 0x%llx"
- "%lld %d AVE %s: Mapper %s | %p %d %d | State: %d BaseAddr: 0x%llx size: 0x%llx Page Size: 0x%llx\n"
- "0 <= pInfo->sSessionCfg.sEnc.sAlgCfg.sGOP.iNumOfTemporalLayer && ((pInfo->sSessionCfg.sEnc.sAlgCfg.sGOP.iNumOfTemporalLayer - 1) <= 7) && ((pInfo->sSessionCfg.sEnc.sAlgCfg.sGOP.iNumOfTemporalLayer - 1) <= 7)"
- "0x%llx %lld "
- "913.48.1"
- "FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d | %d %d"
- "FwLog %p %d | Phy 0x%lx Kernel 0x%lx DART 0x%llx | %d %d %d | %d %d\n"
- "HwC %s | %p %d | IPC: %p IPC Surface: %p Heap: %p Command Buffer: 0x%lx %d Notify Buffer: 0x%lx %d"
- "HwC %s | %p %d | IPC: %p IPC Surface: %p Heap: %p Command Buffer: 0x%lx %d Notify Buffer: 0x%lx %d\n"
- "Mapper %s | %p %d %d | State: %d BaseAddr: 0x%llx size: 0x%llx Page Size: 0x%llx"
- "Mapper %s | %p %d %d | State: %d BaseAddr: 0x%llx size: 0x%llx Page Size: 0x%llx\n"
```
