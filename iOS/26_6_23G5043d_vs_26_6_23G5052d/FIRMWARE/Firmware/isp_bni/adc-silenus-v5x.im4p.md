## adc-silenus-v5x.im4p

> `Firmware/isp_bni/adc-silenus-v5x.im4p`

```diff

-  __TEXT.__text: 0xb2fd64
-  __TEXT.__const: 0x8522b8
-  __TEXT.__cstring: 0xab2e4
+  __TEXT.__text: 0xb31df8
+  __TEXT.__const: 0x85232c
+  __TEXT.__cstring: 0xac948
   __TEXT.text_env: 0x57888
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0

   __DATA.__chain_starts: 0x30
   __DATA.__mod_init_func: 0x8
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x5eeaf8
-  Functions: 9850
+  __DATA.__zerofill: 0x5eaaf8
+  Functions: 9851
   Symbols:   0
-  CStrings:  18762
+  CStrings:  18861
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA.__const : content changed
~ __DATA.__data : content changed
~ __DATA._rtk_power : content changed
~ __DATA._rtk_patchbay : content changed
~ __DATA.__data_copy : content changed
~ __DATA._fwinfo : content changed
~ __DATA._rtk_mtab : content changed
~ __DATA.__chain_starts : content changed
~ __DATA.__mod_init_func : content changed
CStrings:
+ "((pFDInputCmd->width * pFDInputCmd->height) % 8) == 0"
+ "(pFDInputCmd->height & 0x1) == 0"
+ "(pFDInputCmd->width & 0x1) == 0"
+ "(pParams->stride.rgbPlanar.b % CDSControllerBase::outputStrideDivider[2]) == 0"
+ "(pParams->stride.rgbPlanar.g % CDSControllerBase::outputStrideDivider[1]) == 0"
+ "(pParams->stride.rgbPlanar.r % CDSControllerBase::outputStrideDivider[0]) == 0"
+ "(pParams->stride.yOnly.y % CDSControllerBase::outputStrideDivider[0]) == 0"
+ "(pParams->stride.yuv420SemiPlanar.uv % CDSControllerBase::outputStrideDivider[1]) == 0"
+ "(pParams->stride.yuv420SemiPlanar.y % CDSControllerBase::outputStrideDivider[0]) == 0"
+ "(pParams->stride.yuv422.yuv % CDSControllerBase::outputStrideDivider[0]) == 0"
+ "*outsize >= sizeof(struct sCIspCmdAppleChAEDynamicSceneMeteringConfigSet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChAEDynamicSceneMeteringStart)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChAEDynamicSceneMeteringStop)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChAEFDSceneMeteringConfigGet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChAEFDSceneMeteringConfigSet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChAEWindowParamGet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChAEWindowParamSet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChAFWindowParamGet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChAFWindowParamSet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChAWBWindowParamGet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChFEStatConfigGet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChRowColSumWindowParamSet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChTileRegionSet)"
+ "*outsize >= sizeof(struct sCIspCmdAppleChTileWeightsSet)"
+ "*outsize >= sizeof(struct sCIspCmdChAWBCCTGet)"
+ "*outsize >= sizeof(struct sCIspCmdChAWBManualCCTRangeGet)"
+ "*outsize >= sizeof(struct sCIspCmdChNVStorageInfoGet)"
+ "*outsize >= sizeof(struct sCIspCmdConfigGet)"
+ "*outsize >= sizeof(struct sCIspCmdConfigGetExt)"
+ "*outsize >= sizeof(struct sCIspCmdGetBesParam)"
+ "*outsize >= sizeof(struct sCIspCmdPlatformInfo)"
+ "*outsize >= sizeof(struct sCIspCmdPowerSupplyControl)"
+ "*outsize >= sizeof(struct sCIspCmdPrintEnable)"
+ "*outsize >= sizeof(struct sCIspCmdTraceEnable)"
+ "20:37:05"
+ "CISP_CMD_CH_BES_AUXSCL_CROP_OUTPUT_CONFIG_SET should set AuxScl cascaded by default"
+ "ManualAE ch:%d, acctime:%d %d \n"
+ "insize == sizeof(struct sCIspCmdChReset)"
+ "insize == sizeof(struct sCIspCmdChStandBy)"
+ "insize == sizeof(struct sCIspCmdChStart)"
+ "insize == sizeof(struct sCIspCmdChStop)"
+ "insize == sizeof(struct sCIspCmdConfigGet)"
+ "insize == sizeof(struct sCIspCmdConfigGetExt)"
+ "insize == sizeof(struct sCIspCmdFIDEnter)"
+ "insize == sizeof(struct sCIspCmdFIDExit)"
+ "insize == sizeof(struct sCIspCmdFlickerSensorSet)"
+ "insize == sizeof(struct sCIspCmdGetBesParam)"
+ "insize == sizeof(struct sCIspCmdPlatformInfo)"
+ "insize == sizeof(struct sCIspCmdPowerDown)"
+ "insize == sizeof(struct sCIspCmdPowerSupplyControl)"
+ "insize == sizeof(struct sCIspCmdPrintEnable)"
+ "insize == sizeof(struct sCIspCmdReset)"
+ "insize == sizeof(struct sCIspCmdSuspend)"
+ "insize == sizeof(struct sCIspCmdTimeProfileShow)"
+ "insize == sizeof(struct sCIspCmdTimeProfileStart)"
+ "insize == sizeof(struct sCIspCmdTimeProfileStop)"
+ "insize == sizeof(struct sCIspCmdTraceEnable)"
+ "insize>=sizeof(sCIspCmdChPeridotModeCfgSet)+sizeof(sCIspPeridotModeCfg)-1"
+ "pAuxSclPyrConfig->numberOfLevels"
+ "pChFEThumbnailMaskConfig->downScaleX <= 64 && pChFEThumbnailMaskConfig->downScaleY <= 64"
+ "pCmd->numOfAMCC == CSystemConfigurator::Instance()->DsIdClrMultiAMCCNumGet()"
+ "pCmd->previewStrmBufferPoolId == CISP_POOL_YCC || pCmd->previewStrmBufferPoolId == CISP_POOL_RENDERED_SCL1"
+ "pCmd->regBase != 0"
+ "pCmd->regBase[amcc] != 0"
+ "pCmd->regBase[plane] != 0"
+ "pCmd->regRange >= CSystemConfigurator::Instance()->DsIdClrRegMaxRangeGet()"
+ "pCmd->regRange[plane] >= CSystemConfigurator::Instance()->DsIdClrRegMaxRangeGet()"
+ "pCropSet->virtualGDCOutputSize.height >= pCropSet->rect.height + pCropSet->rect.y"
+ "pCropSet->virtualGDCOutputSize.width >= pCropSet->rect.width + pCropSet->rect.x"
+ "pEGlut->count <= (sizeof(pEGlut->lut) / sizeof(pEGlut->lut[0]))"
+ "pFDInputCmd->height <= 480"
+ "pFDInputCmd->width <= 640"
+ "pHostMetaData != 0 && ((size_t)pHostMetaData == (size_t)(pReprocessFrame->metaData.buffer))"
+ "pLSCTableSet->offsetB != 0"
+ "pLSCTableSet->offsetGB != 0"
+ "pLSCTableSet->offsetGR != 0"
+ "pLSCTableSet->offsetR != 0"
+ "pLSCTableSet->sizeB == sizeof(int16_t)*pLSCTableSet->rows*pLSCTableSet->cols"
+ "pLSCTableSet->sizeGB == sizeof(int16_t)*pLSCTableSet->rows*pLSCTableSet->cols"
+ "pLSCTableSet->sizeGR == sizeof(int16_t)*pLSCTableSet->rows*pLSCTableSet->cols"
+ "pLSCTableSet->sizeR == sizeof(int16_t)*pLSCTableSet->rows*pLSCTableSet->cols"
+ "pMLVNRModeConfigSet->autoModeEnterFrameRate <= pMLVNRModeConfigSet->autoModeExitFrameRate"
+ "pMLVNRModeConfigSet->autoModeEnterThreshold >= pMLVNRModeConfigSet->autoModeExitThreshold"
+ "pMLVNRNightModeConfigSet->autoModeEnterThreshold >= pMLVNRNightModeConfigSet->autoModeExitThreshold"
+ "pMLVNRTimeWarpConfigSet->autoModeEnterThreshold >= pMLVNRTimeWarpConfigSet->autoModeExitThreshold"
+ "pOfflineFD->yuvData.yuvBuffer.buffer != 0"
+ "pOfflineFD->yuvData.yuvBuffer.size > 0"
+ "pOfflineFD->yuvData.yuvBuffer.stride > 0"
+ "pOfflineFD->yuvData.yuvBuffer.stride >= (size_t)(pOfflineFD->imageWidth << 1)"
+ "pOfflineFD->yuvData.yuvBuffer.stride >= (size_t)pOfflineFD->imageWidth"
+ "pOutputEnable->outputSel < CISP_OUTPUT_TOT"
+ "pQuadraShading->size >= SENSOR_PERMODULE_LSC_QUADRA_CH_SHADING_SIZE_MAX_BYTES"
+ "pReprocessFrame->metaData.buffer != 0"
+ "pReprocessFrame->rawData.buffer != 0"
+ "pReprocessFrame->rawData.size > 0"
+ "pReprocessFrame->rawData.stride > 0"
+ "pSetCamBesAuxSclCropOutputConfig->inSel == CISP_SECONDARY_SCALER_SOURCE_BES"
+ "pSetCamOutConfig->bufferHeight >= pSetCamOutConfig->height"
+ "pSysCfg->size == sizeof(struct sSysCfgKeyRosaline)"
+ "pWinSet->winID <= CISP_APPLE_AE_WIN_3"
+ "pWinSet->winID >= CISP_APPLE_AE_WIN_0"
+ "value == ISP_FREQ_DITHER_DISABLED || value == ISP_FREQ_DITHER_4MS || value == ISP_FREQ_DITHER_8MS || value == ISP_FREQ_DITHER_16MS"
- "23:53:13"
- "Jun  9 2026"
- "ManualAE ch:%d, acctime:%d %d"

```
