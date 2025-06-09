## AppleAVE2FW_H17.im4p

> `AppleAVE2FW_H17.im4p`

```diff

 
-  __TEXT.__text: 0xf3d48
-  __TEXT._rtk_mtab: 0x2d0
-  __TEXT.__const: 0x22844
-  __TEXT.__cstring: 0x1417b
-  __TEXT.__constructor: 0x0
-  __TEXT.__chain_starts: 0x0
-  __DATA.__const: 0x2a20
-  __DATA._rtk_patchbay: 0x228
-  __DATA.__data: 0x1070
-  __DATA._rtk_power: 0x368
+  __TEXT.__text: 0x1081f4
+  __TEXT.__const: 0x249ec
+  __TEXT.__cstring: 0x14ec5
+  __TEXT.__init_offsets: 0x0
+  __TEXT.__chain_starts: 0x20
+  __DATA.__const: 0x3310
+  __DATA._rtk_patchbay: 0x211
+  __DATA.__data: 0x1110
+  __DATA._rtk_mtab: 0x2d0
+  __DATA._rtk_power: 0x3b8
   __DATA.__gxf_data: 0x10
   __DATA._rtk_tunables: 0x6a0
   __DATA._rtk_init_stack: 0x10000

   __DATA._rtk_data_uuid: 0x0
   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0xcbd58
-  UUID: 1B669F0D-BFB8-3858-B53D-25C1E631B641
-  Functions: 0
-  Symbols:   1538
-  CStrings:  2423
+  __DATA.__constructor: 0x0
+  __DATA.__zerofill: 0xccb58
+  UUID: 9523E67D-FFA5-396E-896B-A93F42F6B070
+  Functions: 1158
+  Symbols:   1641
+  CStrings:  2476
 
Symbols:
+ _AVE_Log_CheckLevel
+ _AVE_VSNPrintf
+ _RTK_DEV_ICU
+ _RTK_DEV_REMOTE_CONTROL
+ _RTK_stack_guard_allocate
+ _RTK_stack_guard_free
+ _VarThRatioN
+ _VarThRatioP
+ __Z13AVE_GetFwModev
+ __Z14AVE_EventTraceP19_S_AVE_HWEventTracePi15_E_AVE_EngineID14_E_AVE_HWEModei15_E_AVE_HWEStatePKj
+ __Z15AVE_CheckDMVCmdPv
+ __Z15AVE_MCTFProfileP24sCAvePerfProfileInternali16_E_AVE_MCTFStats
+ __Z15AVE_PSInfo_MakePKh13_E_AVE_PSTypeiiP16_S_AVE_PSContext
+ __Z16AVC_FindLevelIdc12_E_AVC_Level
+ __Z16AVE_EventProfileP24sCAvePerfProfileInternalii14_E_AVE_FwStats
+ __Z16AVE_UpdateFwModej
+ __Z17AVE_SetTunableRegP14sAVERegTunablejj
+ __Z17HEVC_FindLevelIdc13_E_HEVC_Level
+ __Z17HEVC_FindTierFlag12_E_HEVC_Tier
+ __Z18AVC_FindProfileIdc14_E_AVC_Profile
+ __Z18DecideLowerQP4MbEnP13sCommonParams
+ __Z19HEVC_FindProfileIdc15_E_HEVC_Profile
+ __Z22AVE_CreateSliceMapRowsPK15_S_AVE_SliceMap18_E_AVE_DevCap_TypePh
+ __Z24AVE_MCTFProfileWithValueP24sCAvePerfProfileInternali16_E_AVE_MCTFStatsx
+ __Z25AVE_EventProfileWithValueP24sCAvePerfProfileInternalii14_E_AVE_FwStatsx
+ __Z27AVE_H264_PrepareSliceHeaderP13sCommonParamsPK26H264_PICTURE_HEADER_PARAMSP24H264_SLICE_HEADER_PARAMSji
+ __Z27AVE_HEVC_PrepareSliceHeaderP13sCommonParamsPK27HEVC_SEQUENCE_HEADER_PARAMSPK26HEVC_PICTURE_HEADER_PARAMSP24HEVC_SLICE_HEADER_PARAMSjbbi
+ __Z28AVE_MCTF_PixelWeightLUT_FindPK30_S_AVE_MCTF_PixelWeightLUT_Set16_E_AVE_MCTF_Mode
+ __ZN10CAVEClient12CommandQueue15EnqueueMCTFCmdQEjyyPvPNS_9FrameInfoEjj
+ __ZN10CAVEClient12CommandQueue8ConvertPEj
+ __ZN10CAVEClient24GetCommandQueueToDequeueEv
+ __ZN10CAVEClient8CompleteEj19_E_Proc_Mode_Queues
+ __ZN10CAVEClient9FrameInfoC1Ejjjjjjj
+ __ZN10CFrameType16LookAheadBFramesER7MPQueueILi16E21_S_AVE_MultiPassStatsE14_E_AVE_EncType
+ __ZN10CFrameType9FrameTypeEP11RCFrameInfoPjR7MPQueueILi16E21_S_AVE_MultiPassStatsE14_E_AVE_EncType
+ __ZN10CQueuePoolC2EPKcP7CObjectm
+ __ZN10CTimerPoolC2EPKcP7CObjectm
+ __ZN11CController15PeriodicProcessEv
+ __ZN11CScopedLockC2EPVmi
+ __ZN11CSignalPoolC2EPKcP7CObjectm
+ __ZN12AVE_KeyFrame4InitEyiiddi
+ __ZN12AVE_KeyFrame7ProcessExyjP11_S_AVE_TimeP19_S_AVE_KeyFrameHint
+ __ZN12CMailboxPoolC2EPKcP7CObjectm
+ __ZN12CRateControl10AccumulateEj9SliceTypejjP16sCRCStatPerFramehS0_
+ __ZN12CRateControl10UpdateBitsEjjP16sCRCStatPerFrame6Engine
+ __ZN12CRateControl11ProcessInitEPK14sCRCInitParams
+ __ZN12CRateControl11RateControlEj9SliceTypejjbjbbbjiS0_bb
+ __ZN12CRateControl17ProcessUpdateBitsEjjP16sCRCStatPerFrame6Engine
+ __ZN12CRateControl4InitEPK14sCRCInitParamsh
+ __ZN13COFController4InitE14_E_AVE_EncType26sCAveInitCmdInternalParamsijPj
+ __ZN14AVE_PIODMACtrl10GroupErrorEj
+ __ZN14AVE_PIODMACtrl11GetCmdGroupEP22_S_AVE_PIODMACmdStatus
+ __ZN14AVE_PIODMACtrl14SetCmdSequenceEjyyjjjb
+ __ZN14AVE_PIODMACtrl5StartEjyjyjj
+ __ZN14AVE_PIODMACtrl9GroupDoneEj
+ __ZN14CAVCController12LoadFWUTSCfgEv
+ __ZN14CAVCController14stitchColoDataEy
+ __ZN14CAVCController22GatherSharedFrameStatsEP14CODED_DATA_HDRPvS2_
+ __ZN14CAVCController23UpdateFlatMbLowQPParamsEv
+ __ZN14CAVCController25InitStaticAreaLowQPParamsEii
+ __ZN14CAVCController26UpdateStaticAreaCbp0CountsEP14CODED_DATA_HDRj
+ __ZN14CAVCController4InitE14_E_AVE_EncType26sCAveInitCmdInternalParamsijPj
+ __ZN14CAVERefManager4InitEPK14sCRCInitParamsb
+ __ZN14CAVERefManager9UpdatePTSEP11RCFrameInfoP11_S_AVE_Timei
+ __ZN14CDMVController11ProcessInitEPv
+ __ZN14CDMVController14ProcessDMVDoneEv
+ __ZN14CDMVController15ProcessDMVStartEPv
+ __ZN14CDMVController4InitE14_E_AVE_EncType26sCAveInitCmdInternalParamsijPj
+ __ZN14CDMVController8StartDMVEP15sCmdInformationi
+ __ZN14CDMVControllerC1EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN14CDMVControllerC2EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN14CDMVControllerD0Ev
+ __ZN14CDMVControllerD1Ev
+ __ZN15CHEVCController12LoadFWUTSCfgEv
+ __ZN15CHEVCController18GetMaxLowerDelatQPEj
+ __ZN15CHEVCController20StaticAreaInterApplyEP18AVE_PICMGMT_PARAMSPjjj
+ __ZN15CHEVCController22GatherSharedFrameStatsEP14CODED_DATA_HDRPv
+ __ZN15CHEVCController24FindStaticAreaActionModeEjjb
+ __ZN15CHEVCController26UpdateStaticAreaCbp0CountsEP14CODED_DATA_HDR
+ __ZN15CHEVCController4InitE14_E_AVE_EncType26sCAveInitCmdInternalParamsijPj
+ __ZN15CHEVCController9SetEncCmdEPK15sCmdInformationP27CAVEControllerHevcEncodeCmd
+ __ZN15CMCTFController13ConfigLRMEDMAEP14MCTF_FrameInfojb
+ __ZN15CMCTFController13ConfigReadDMAEP18AVE_PICMGMT_PARAMSP14MCTF_FrameInfoj
+ __ZN15CMCTFController14ConfigWriteDMAEP18AVE_PICMGMT_PARAMSP14MCTF_FrameInfo
+ __ZN15CMCTFController14GetRefCompInfoEbPK18AVE_PICMGMT_PARAMSP14MCTF_FrameInfoS4_PbPhS6_P17_S_AVE_CompBufExt
+ __ZN15CMCTFController15SetFilterGatingEP14MCTF_FrameInfoPb
+ __ZN15CMCTFController15SetRefFrameInfoEPK18AVE_PICMGMT_PARAMSPP14MCTF_FrameInfoS4_
+ __ZN15CMCTFController16CollectPipeStatsEP14MCTF_FrameInfoPb
+ __ZN15CMCTFController16ConfigLRMESrcDMAEP18AVE_PICMGMT_PARAMSb
+ __ZN15CMCTFController17GetRefCompOutInfoEPK18AVE_PICMGMT_PARAMSP14MCTF_FrameInfoP17_S_AVE_CompBufExt
+ __ZN15CMCTFController17ProcessLRMERCDoneEP15sCmdInformation
+ __ZN15CMCTFController20MakeFrameCopyForMCTFEPK20_S_AVE_CompressedBufP18AVE_PICMGMT_PARAMSbb
+ __ZN15CMCTFController20SetLRMERCPerSrcFrameEPK18AVE_PICMGMT_PARAMS
+ __ZN15CMCTFController7SetMCTFEP18AVE_PICMGMT_PARAMSP14MCTF_FrameInfo
+ __ZN16AVE_SyntaxWriter14WriteBitNTimesEji
+ __ZN16AVE_SyntaxWriter16RBSPTrailingBitsEPh
+ __ZN16AVE_SyntaxWriter6SetEBPEb
+ __ZN16AVE_SyntaxWriterC1EPhib
+ __ZN16LinearRegression4initEffff
+ __ZN17CAVEPriorityQueue24GetCommandQueueToDequeueEb
+ __ZN17CAVEPriorityQueue24GetCommandQueueToDequeueEy
+ __ZN17CAVEPriorityQueue4PeekEPjS0_PyS1_S0_PPvb
+ __ZN17CAVEPriorityQueue7DequeueEP15sCmdInformationb
+ __ZN17CAVEPriorityQueue7EnqueueEyyyjPvPN10CAVEClient9FrameInfoEj
+ __ZN17CAVEPriorityQueue7IsEmptyEv
+ __ZN18CAVEPipeISRManagerC1EPKcP7CObjectibPPVmP14AVE_PIODMACtrl
+ __ZN18CAVEPipeISRManagerC2EPKcP7CObjectibPPVmP14AVE_PIODMACtrl
+ __ZN19CFlowControllerBase15MCTFStopProcessEj
+ __ZN19CFlowControllerBase15PeriodicProcessEv
+ __ZN19CFlowControllerBase18NotificationToHostEtyyijj
+ __ZN19CFlowControllerBase18SendCommandToQueueEP20CAVECommonControllerjPvjjyyj
+ __ZN19CFlowControllerBase19PrintHwClientStatusEji
+ __ZN19CFlowControllerBase20ProcessDoneWithFrameEyPvi
+ __ZN19CFlowControllerBase22PostXCODEProcessForEncEv
+ __ZN19CFlowControllerBase22ProcessCmd_Process_DMVEv
+ __ZN19CFlowControllerBase27AcquireAndTriggerPIPEForEncEv
+ __ZN19CFlowControllerBase28AcquireAndTriggerXCODEForEncEv
+ __ZN19CFlowControllerBase29AcquireAndTriggerLRMEFSForEncEv
+ __ZN19CFlowControllerBase29AcquireAndTriggerLRMERCForEncEv
+ __ZN19CFlowControllerBase30SendScaledFrameToFilterProcessEP15sCmdInformationj
+ __ZN19CFlowControllerBase33SendFilteredFramesToEncodeProcessEj
+ __ZN19CPlatformISRManager23HandleSoftwareInterruptEj
+ __ZN19H264VideoEncoderDPB15ManageDPBBufferEP14CAVERefManagerP27_S_AVE_RefManager_FrameInfoP26AVE_PICMGMT_RC_UPDATE_DATAP20_S_AVE_Session_PFCfgP22ReferenceFrameInfoDatajiP18AVE_PICMGMT_PARAMSb
+ __ZN19H264VideoEncoderDPBC1Ejjjybbj
+ __ZN20CAVECommonController12GetPicParamsEPv
+ __ZN20CAVECommonController12SetPSContextEPK16_S_AVE_PSContexty
+ __ZN20CAVECommonController12getNextSveIDEP12_S_AVE_EUMapj
+ __ZN20CAVECommonController12getPrevSveIDEP12_S_AVE_EUMapj
+ __ZN20CAVECommonController13PrintLRMECRCsEjjb
+ __ZN20CAVECommonController13PrintPipeCRCsEjjbb
+ __ZN20CAVECommonController13ResetROIFlagsEjy
+ __ZN20CAVECommonController14PrintDbgCyclesEbj
+ __ZN20CAVECommonController15MCTFProcessInitE14_E_AVE_EncType26sCAveInitCmdInternalParams
+ __ZN20CAVECommonController15PrepareROIFlagsEjy
+ __ZN20CAVECommonController17CreateRateControlEPK13S_AVE_RCParami
+ __ZN20CAVECommonController17MCTF_GetExecStageEPv
+ __ZN20CAVECommonController17MCTF_GetFrameInfoEP15sCmdInformation
+ __ZN20CAVECommonController17MCTF_GetQueueIterEv
+ __ZN20CAVECommonController17MCTF_SetExecStageEPv18_E_MCTF_Exec_Stage
+ __ZN20CAVECommonController17PerformDeltaQPModEj
+ __ZN20CAVECommonController19MCTF_GetFrameNumberEPv
+ __ZN20CAVECommonController19prepareVarQpModLUTsE14_E_AVE_EncTypePvhh
+ __ZN20CAVECommonController20GetNumFilteredFramesEv
+ __ZN20CAVECommonController20MakeFrameCopyForMCTFEPK20_S_AVE_CompressedBuf
+ __ZN20CAVECommonController21MCTF_IsLastNoiseFrameEPv
+ __ZN20CAVECommonController22MCTF_GetCmdCounterInfoEP15sCmdInformation
+ __ZN20CAVECommonController22MCTF_IsFirstNoiseFrameEPv
+ __ZN20CAVECommonController22MCTF_PeekHeadFrameInfoEv
+ __ZN20CAVECommonController23MCTF_IsViewToBeFilteredEj
+ __ZN20CAVECommonController23getContextHeightQuadRowEP12_S_AVE_EUMapjj
+ __ZN20CAVECommonController24MCTF_GetNumNextRefFramesEv
+ __ZN20CAVECommonController24MCTF_GetNumPrevRefFramesEv
+ __ZN20CAVECommonController24SignalEndOfNoiseSequenceEv
+ __ZN20CAVECommonController26MCTF_GetPastCmdCounterInfoEj
+ __ZN20CAVECommonController28MCTF_IsNoiseSequenceCompleteEP18AVE_PICMGMT_PARAMS
+ __ZN20CAVECommonController28MCTF_IsNoiseSequenceFilteredEv
+ __ZN20CAVECommonController29GetCurrentNoiseSequenceLengthEv
+ __ZN20CAVECommonController29MCTFClientGetPIODMACopyStatusEv
+ __ZN20CAVECommonController29getContextHeightTopBottomHalfEP12_S_AVE_EUMapj
+ __ZN20CAVECommonController30MCTFClientMakeFrameCopyForMCTFEPK20_S_AVE_CompressedBufP18AVE_PICMGMT_PARAMSbb
+ __ZN20CAVECommonController31MCTF_GetOverallNoiseFrameNumberEPv
+ __ZN21PlatformIOPIPCManager24CalculateSystemBaseAddrsEy
+ __ZN3HRD15updateHrdStatusEj11_S_AVE_TimefRiS1_f
+ __ZN6AVE_PP4TaskEv
+ __ZN7AVC_PPS22pic_parameter_set_rbspEii
+ __ZN7AVC_PPS8GenerateEiiiibP16_S_AVE_PSContext
+ __ZN7AVC_PPSC1EP26H264_PICTURE_HEADER_PARAMS
+ __ZN7AVC_SPS22seq_parameter_set_rbspEv
+ __ZN7AVC_SPS8GenerateEP16_S_AVE_PSContext
+ __ZN7AVC_SPSC1EP27H264_SEQUENCE_HEADER_PARAMS
+ __ZN7AVE_FPS4InitEyiii
+ __ZN7AVE_FPS6UninitEv
+ __ZN9AVC_Slice12slice_headerERK27H264_SEQUENCE_HEADER_PARAMSRK26H264_PICTURE_HEADER_PARAMSi
+ __ZN9AVC_Slice17pred_weight_tableEv
+ __ZN9AVC_Slice19dec_ref_pic_markingEv
+ __ZN9AVC_Slice23generateSliceHeaderInKFERK27H264_SEQUENCE_HEADER_PARAMSRK26H264_PICTURE_HEADER_PARAMS
+ __ZN9AVC_Slice25ref_pic_list_modificationEv
+ __ZN9AdaptiveB4InitEjjb14_E_AVE_EncType
+ __ZNK11RateControl17temporalQpScalingEfPK14LookAheadStats
+ __ZNK12MappedMemory10HwToTargetEv
+ __ZNK15CMCTFController15SetLRMERCPerRefEv
+ __ZNK15CMCTFController16SetLRMERCPerPassEP14MCTF_FrameInfo
+ __ZNK7AVC_SPS14vui_parametersEv
+ __ZTV14CDMVController
+ __ZZN19CAVE_PICMGMT_PARAMS22GetPlaneCompressedInfoE13_E_AVE_BufIdxE10nullCPInfo
+ __rtk_astris_island
+ __rtk_crashlog_is_local
+ __rtk_crashlog_local_buffer
+ __rtk_crashlog_requested_size
+ __rtk_pac_safe_interrupts_disable
+ __rtk_pac_safe_interrupts_restore
+ __rtk_patch_RTK_lock_legacy
+ __rtk_sign_initial_thread_state
+ __rtk_thread_entry
+ _gc_sAVE_DevCap_DPMMap_AVC_Erebus
+ _gc_sAVE_DevCap_DPMMap_DMV_Erebus
+ _gc_sAVE_DevCap_DPMMap_GGM_Erebus
+ _gc_sAVE_DevCap_DPMMap_HEVC_Erebus
+ _gc_sAVE_DevCap_DPMMap_LRME_Erebus
+ _gc_sAVE_DevCap_DPMMap_MCTF_Erebus
+ _gc_sAVE_DevCap_PDMap_Erebus
+ _qp2LambdaBEF
+ _qp2LambdaMD_satd16x16
+ _qp2LambdaMD_satd32x32
+ _qp2LambdaMD_satd8x8
+ _qp2LambdaMD_split16x16
+ _qp2LambdaMD_split32x32
+ _qp2LambdaMD_ssd16x16
+ _qp2LambdaMD_ssd32x32
+ _qp2LambdaMD_ssd8x8
+ _qp2LambdaME
+ _qp2LambdaRCR_BP
+ _qp2LambdaRCR_I
+ _qp2LambdaSATD
+ _qp2LambdaSSD
- _GetLinkDate
- _GetLinkTime
- _GetRepositoryInfo
- _RTK_dev_syslog_mbi
- _RTK_dev_syslog_mbi_dispatch
- __Z16staticAreaQpTaskv
- __Z18AccumulateCbp0CntsP13sCommonParamsPjj
- __Z20InitCbp0FlagBufQueueP26_CavlcCbp0FlagBufQueueTypePh
- __Z21AVE_MCTF_Param_getNumPK21_S_AVE_MCTF_Param_Set16_E_AVE_MCTF_Mode
- __Z27AVE_H264_PrepareSliceHeaderP13sCommonParamsP27H264_SEQUENCE_HEADER_PARAMSPK26H264_PICTURE_HEADER_PARAMSP24H264_SLICE_HEADER_PARAMSji
- __Z27AVE_HEVC_PrepareSliceHeaderP13sCommonParamsP27HEVC_SEQUENCE_HEADER_PARAMSP26HEVC_PICTURE_HEADER_PARAMSP24HEVC_SLICE_HEADER_PARAMSjbbi
- __Z28AVE_MCTF_pixelWeightLUT_FindPK30_S_AVE_MCTF_pixelWeightLUT_Set16_E_AVE_MCTF_Mode
- __Z31TryGetEmptyCbp0FlagBufFromQueueP26_CavlcCbp0FlagBufQueueType
- __Z32GetEmptyCbp0FlagBufFromQueueDoneP26_CavlcCbp0FlagBufQueueType
- __ZN10CAVEClient12CommandQueue15EnqueueMCTFCmdQEjyyPvPNS_9FrameInfoEb
- __ZN10CAVEClient12CommandQueue17ConvertNoiseFrameEv
- __ZN10CAVEClient12CommandQueue4PeekEv
- __ZN10CAVEClient15GetCommandQueueE19_E_Proc_Mode_Queues
- __ZN10CAVEClient9FrameInfoC1Ejjjjj
- __ZN10CFrameType16LookAheadBFramesER7MPQueueILi16E21_S_AVE_MultiPassStatsE20AVE_VIDEO_CODEC_TYPE
- __ZN10CFrameType9FrameTypeEP11RCFrameInfoPjR7MPQueueILi16E21_S_AVE_MultiPassStatsE20AVE_VIDEO_CODEC_TYPE
- __ZN12AVE_KeyFrame4InitEiiddiii
- __ZN12AVE_KeyFrame7ProcessExyP11_S_AVE_TimeP19_S_AVE_KeyFrameHint
- __ZN12CRateControl10AccumulateEj9SliceTypejjP16sCRCStatPerFramebhS0_
- __ZN12CRateControl10UpdateBitsEjjP16sCRCStatPerFrame6Engineb
- __ZN12CRateControl11ProcessInitEP14sCRCInitParams
- __ZN12CRateControl11RateControlEj9SliceTypejjbbjbbbjiS0_bb
- __ZN12CRateControl4InitEP14sCRCInitParamsbh
- __ZN13CAVECommonDPB8ResetDPBEv
- __ZN13COFController13EnqueueFramesEP18AVE_PICMGMT_PARAMSPv
- __ZN13COFController4InitE20AVE_VIDEO_CODEC_TYPE26sCAveInitCmdInternalParamsijPj
- __ZN14AVE_PIODMACtrl5StartEyyjj
- __ZN14CAVCController25InitStaticAreaLowQPParamsEP13S_AVE_RCParam
- __ZN14CAVCController4InitE20AVE_VIDEO_CODEC_TYPE26sCAveInitCmdInternalParamsijPj
- __ZN14CAVERefManager4InitEv
- __ZN14CAVERefManager9UpdatePTSEP11RCFrameInfoi
- __ZN15CHEVCController4InitE20AVE_VIDEO_CODEC_TYPE26sCAveInitCmdInternalParamsijPj
- __ZN15CMCTFController11ResetParamsEv
- __ZN15CMCTFController13ConfigLRMEDMAEP14MCTF_FrameInfojjb
- __ZN15CMCTFController13ConfigReadDMAEP18AVE_PICMGMT_PARAMSP14MCTF_FrameInfojj
- __ZN15CMCTFController13IsMCTFDrainedEv
- __ZN15CMCTFController14ConfigWriteDMAEP18AVE_PICMGMT_PARAMSj
- __ZN15CMCTFController15SetFilterGatingEjbPb
- __ZN15CMCTFController15SetMCTFCompleteEv
- __ZN15CMCTFController16CollectPipeStatsEjPb
- __ZN15CMCTFController16ConfigLRMESrcDMAEP18AVE_PICMGMT_PARAMSjb
- __ZN15CMCTFController17ProcessLRMERCDoneEv
- __ZN15CMCTFController18MarkFrameAsFlushedEj
- __ZN15CMCTFController20MakeFrameCopyForMCTFEP17sAVECompInputBufsP18AVE_PICMGMT_PARAMSbb
- __ZN15CMCTFController20SetLRMERCPerSrcFrameEP14MCTF_FrameInfoi
- __ZN15CMCTFController7SetMCTFEP18AVE_PICMGMT_PARAMS
- __ZN16AVE_SyntaxWriter10AVE_SetEBPEb
- __ZN16AVE_SyntaxWriter16RbspTrailingBitsEPh
- __ZN16LinearRegression4initEfff
- __ZN17CAVEPriorityQueue13DestroyClientEP10CAVEClient
- __ZN17CAVEPriorityQueue22PrepareClientMCTFQueueEyyyPv
- __ZN17CAVEPriorityQueue24GetCommandQueueToDequeueEv
- __ZN17CAVEPriorityQueue4PeekEPjS0_PyS1_S0_PPv
- __ZN17CAVEPriorityQueue7DequeueEP15sCmdInformation
- __ZN17CAVEPriorityQueue7EnqueueEyyyjPvPN10CAVEClient9FrameInfoEy
- __ZN18CAVEPipeISRManagerC1EPKcP7CObjectibPPVm
- __ZN18CAVEPipeISRManagerC2EPKcP7CObjectibPPVm
- __ZN19CFlowControllerBase12MCTFCompleteEv
- __ZN19CFlowControllerBase15MCTFStopProcessEP10CAVEClienty
- __ZN19CFlowControllerBase18NotificationToHostEtyy12AVE_FW_ERRORjj
- __ZN19CFlowControllerBase18SendCommandToQueueEP20CAVECommonControllerjPvjjyyy
- __ZN19CFlowControllerBase19PrintHwClientStatusEi
- __ZN19CFlowControllerBase20ProcessDoneWithFrameEyPv12AVE_FW_ERROR
- __ZN19CFlowControllerBase25MarkFrameAsFlushedForMCTFEyj
- __ZN19CFlowControllerBase32SendFilteredFrameToEncodeProcessEP15sCmdInformationj
- __ZN19CFlowControllerBase9MCTFFlushEP20CAVECommonControllerP10CAVEClienty
- __ZN19H264VideoEncoderDPB15ManageDPBBufferEP14CAVERefManagerP27_S_AVE_RefManager_FrameInfoP26AVE_PICMGMT_RC_UPDATE_DATAP22ReferenceFrameInfoDatajiP18AVE_PICMGMT_PARAMSb
- __ZN19H264VideoEncoderDPBC1Ejj15SH_PROFILE_TYPE13SH_LEVEL_TYPEjybbj
- __ZN20CAVECommonController12getNextSveIDEP13_S_AVE_SVEMapj
- __ZN20CAVECommonController12getPrevSveIDEP13_S_AVE_SVEMapj
- __ZN20CAVECommonController13IsMCTFDrainedEv
- __ZN20CAVECommonController13IsMctfEnabledEP18AVE_PICMGMT_PARAMS
- __ZN20CAVECommonController13PrintLRMECRCsEj
- __ZN20CAVECommonController13PrintPipeCRCsEjb
- __ZN20CAVECommonController13ResetROIFlagsEj
- __ZN20CAVECommonController15MCTFProcessInitE20AVE_VIDEO_CODEC_TYPE26sCAveInitCmdInternalParams
- __ZN20CAVECommonController15PrepareROIFlagsEj
- __ZN20CAVECommonController15ResetMCTFParamsEv
- __ZN20CAVECommonController17AVE_PSType_SetBufEP13_S_AVE_PSInfoj13_E_AVE_PSTypehj
- __ZN20CAVECommonController17CreateRateControlEPK13S_AVE_RCParam
- __ZN20CAVECommonController18SignalMCTFCompleteEv
- __ZN20CAVECommonController19prepareVarQpModLUTsE20AVE_VIDEO_CODEC_TYPEPvhh
- __ZN20CAVECommonController20CalcAccumCPB0CntNMbsEv
- __ZN20CAVECommonController20MakeFrameCopyForMCTFEP17sAVECompInputBufs
- __ZN20CAVECommonController22MarkFrameAsFlushedMCTFEj
- __ZN20CAVECommonController23getContextHeightQuadRowEP13_S_AVE_SVEMapjj
- __ZN20CAVECommonController29getContextHeightTopBottomHalfEP13_S_AVE_SVEMapj
- __ZN20CAVECommonController30IsNextMctfScalerFrameAvailableEv
- __ZN20CAVECommonController30MCTFClientMakeFrameCopyForMCTFEP17sAVECompInputBufsP18AVE_PICMGMT_PARAMSbb
- __ZN3PPS22pic_parameter_set_rbspEP3SPS
- __ZN3SPS14vui_parametersEv
- __ZN3SPS22seq_parameter_set_rbspEv
- __ZN5Slice12slice_headerEP16AVE_SyntaxWriterRK27H264_SEQUENCE_HEADER_PARAMSRK26H264_PICTURE_HEADER_PARAMSi
- __ZN5Slice17pred_weight_tableEP16AVE_SyntaxWriter
- __ZN5Slice19dec_ref_pic_markingEP16AVE_SyntaxWriter
- __ZN5Slice23generateSliceHeaderInKFERK27H264_SEQUENCE_HEADER_PARAMSRK26H264_PICTURE_HEADER_PARAMS
- __ZN5Slice25ref_pic_list_modificationEP16AVE_SyntaxWriter
- __ZN7AVE_FPS4InitEiii
- __ZN9AdaptiveB4InitEjjb20AVE_VIDEO_CODEC_TYPE
- __ZNK15CMCTFController16SetLRMERCPerPassEj
- __rtk_patch_gxf_private_phy_space_base
- __rtk_patch_gxf_private_phy_space_size
- _aligned_alloc
- _linkdate
- _linktime
- _repobranch
- _reponames
CStrings:
+ "                size : %zu [%#08lx] [%zu.%zu MB]\n"
+ "!(m_iScalerToFsDelay > 0 && pcCurrScalerFrmInfo->GetExecStage() >= MCTF_Stage_Scaled)"
+ "%lld %p %p"
+ "%s %d %d | %d %lld %lld | %p %d %d %d %d | %d %d 0x%x"
+ "%s %d %lld %lld | %p %d %d %d | %d %d 0x%x"
+ "%s %lld %lld %d"
+ "%s B->P %d %lld %lld | %p %d %d | %d %d 0x%x "
+ "%s Constructor!!"
+ "%s Enter %d %lld %lld 0x%08x %d %d"
+ "%s Enter %p %d %d %d %p"
+ "%s Exit %d %lld %lld 0x%08x %d %d"
+ "%s Exit %p %d %d %d %p %d"
+ "%s F %d, NumWUs %d totalLowQPMB %d!"
+ "%s TIMEOUT waiting host ACK %lld %d %lld time %lld %lld"
+ "%s: Frame:%u (NF:%u) : %d -> %d"
+ "%s: m_iaFiltStrength[%u] = %d, Noise frame number:%u , First Noise frame:%d"
+ "%s:%d %lld %lld"
+ "%s:%d %llu F %d %d"
+ "%s:%d %s | PS data overflows %p %d %d %d %p | %d %d %d %ld"
+ "%s:%d %s | fail to get DevCap %p %d %p %d"
+ "%s:%d %s | not padded to bytes %p %d %d %d %p"
+ "%s:%d %s | wrong PS type %d"
+ "%s:%d %s | wrong layer ID %d"
+ "%s:%d %s | wrong parameter %d"
+ "%s:%d %s | wrong parameters %p %d %p"
+ "%s:%d %s | wrong parameters %p %p"
+ "%s:%d 0x%llx %d %d %d"
+ "%s:%d DPB ERROR: %u %d"
+ "%s:%d FrameType: %d FrameNum: %lld POC: %d qp: %d"
+ "%s:%d: maxClientBufferSize = %d, %zu-%zu-%zu-%zu-%zu"
+ "%s::%s AccCbp0Cnts: F %d, Mode %d, IB %d %d %d; cbpReset %d, %d; LowerDeltaQP %d %d"
+ "%s::%s EXIT"
+ "%s::%s Enter %lld | %d %d %d"
+ "%s::%s Enter %llu %d %d"
+ "%s::%s Enter %p %lld"
+ "%s::%s Enter %p %lld %d %d %d"
+ "%s::%s Enter %p %lld %d %d %d.%03d %d.%03d %d"
+ "%s::%s Enter %p %lld %lld %d"
+ "%s::%s Enter %p %lld %lld 0x%llx 0x%x %p %p"
+ "%s::%s Enter %p %lld %p"
+ "%s::%s Enter %p, %d-%d-%d"
+ "%s::%s Enter %u"
+ "%s::%s Enter %zu"
+ "%s::%s Enter %zu %zu %zu %p"
+ "%s::%s Enter %zu %zu %zu %p %d"
+ "%s::%s Enter, Frame ID = %d"
+ "%s::%s Enter, frame ID = %d"
+ "%s::%s Exit %d %d %d %d %p %d"
+ "%s::%s Exit %d %lld %lld %lld %d"
+ "%s::%s Exit %d %lld %lld 0x%08x %d %d"
+ "%s::%s Exit %lld | %d %d %d"
+ "%s::%s Exit %llu "
+ "%s::%s Exit %llu %d"
+ "%s::%s Exit %p %lld %d"
+ "%s::%s Exit %p %lld %d %d %d"
+ "%s::%s Exit %p %lld %d %d %d %d"
+ "%s::%s Exit %p %lld %d %d %d.%03d %d.%03d %d %d"
+ "%s::%s Exit %p %lld %lld %d %d"
+ "%s::%s Exit %p %lld %lld 0x%llx 0x%x %p %p %d"
+ "%s::%s Exit %p %lld %p %d"
+ "%s::%s Exit %p %p %llx %d %d %lld %d %d %d"
+ "%s::%s Exit %u"
+ "%s::%s F %d LowerDeltaQPMode %d, ApplyStaticAreaQP %d"
+ "%s::%s RCMode %d CRFScale %d"
+ "%s::%s clientIndex %d"
+ "%s::%s exit"
+ "%s::%s exit %d"
+ "%s::%s: %d-%d"
+ "%s::%s: %d-%d, %d-%d, %d-%d, %d-%d"
+ "%s::%s: %d-%d-%d, %d-%d, %d-%d-%d, %d-%d-%d, %d"
+ "%s::%s: pInitParams is NULL"
+ "%s::%s: pOFInitCmd is NULL"
+ "%s::%s:%d  %llu F %d Type %d POC %d | %d %d | S0 %d %hhu %d %hhu | S1 %d %hhu"
+ "%s::%s:%d  Thread = %p, priority = %d\n"
+ "%s::%s:%d %d PocStCurrAfter %d"
+ "%s::%s:%d %d PocStCurrBefore %d PocStFoll %d"
+ "%s::%s:%d %d, client_id %lld cmdID %d FrameNum %d"
+ "%s::%s:%d %d, client_id %lld, cmdCounter %lld"
+ "%s::%s:%d %lld %d %llu %d"
+ "%s::%s:%d %lld %lld %d"
+ "%s::%s:%d %lld | %d %d | %d %llu"
+ "%s::%s:%d %lld | %lld %d %d %d %d | %lld | %d %d %d | %d %d %d %d"
+ "%s::%s:%d %llu %lld"
+ "%s::%s:%d %llu %u %u | %d %llu %llu %p | %d %d %d | %d %d 0x%x"
+ "%s::%s:%d %llu F %d %d %d %d"
+ "%s::%s:%d %llu F %d POC %d numTemporalLayers %d cur_temporalId %d max_ref_pic_temporalId %d %d %d"
+ "%s::%s:%d %llu F %d POC %d ref_poc %d"
+ "%s::%s:%d %llu F %d Type %d POC %d | %d %d | %d %hhu %d %hhu"
+ "%s::%s:%d %p %lld %d %d %d | %d %lld %d - %d %lld %d | %d.%03d %d.%03d"
+ "%s::%s:%d %p %lld %d %d | %d %lld %d - %d %lld %d | %d.%03d  %d.%03d"
+ "%s::%s:%d %p %lld Frame[%lld] op 0x%llx 0x%x PTS %lld | interval %d %d %d.%03d %d.%03d | status %lld %lld %lld %d | Hint %d 0x%x"
+ "%s::%s:%d %s HRD status: max_bitrate %d cpb_size %d, init_cpb_delay %d, t_af %d, t_c %d, t_scale %d, 1st_dts %lld"
+ "%s::%s:%d %s | Fail to find device capability (TargetID: %d | DevID: %d DevType: %d ChipType: %d DevRevision: %d Arch: %d SVE Num: %d NumPerGroup: %d DevSubIDFlag: 0x%llx) ret: %d"
+ "%s::%s:%d %s | Frame number out of range %p %lld %lld %d %lld"
+ "%s::%s:%d %s | Wrong parameter %p %lld %lld %d"
+ "%s::%s:%d %s | Wrong parameter %p %lld %lld 0x%llx 0x%x %p %p"
+ "%s::%s:%d %s | Wrong parameter %p %lld %lld 0x%llx 0x%x %p %p | %f %f %d %d"
+ "%s::%s:%d %s | fail to add PTS to FPS %p %lld %lld 0x%llx 0x%x %p %p %d"
+ "%s::%s:%d %s | fail to initialize FPS %p %lld %d %d %d.%03d %d.%03d %d %d"
+ "%s::%s:%d %s | fail to instantiate memory %d"
+ "%s::%s:%d %s | fail to update FPS %p %lld %d %d %d.%03d %d.%03d %d %d"
+ "%s::%s:%d %s | fail to update FPS %p %lld %lld 0x%llx 0x%x %p %p %d"
+ "%s::%s:%d %s | failed to allocate memory of timestamp %p %lld %d %d %d"
+ "%s::%s:%d %s | failed to calculate average FPS %p %lld %p"
+ "%s::%s:%d %s | failed to calculate realtime FPS %p %lld %p"
+ "%s::%s:%d %s | failed to calculate sliding average FPS %p %lld %p"
+ "%s::%s:%d %s | m_psParams->header_len(%d) %p"
+ "%s::%s:%d %s | wrong parameters %p %lld %d %d %d"
+ "%s::%s:%d %s | wrong state %p %lld"
+ "%s::%s:%d %s | wrong state %p %lld %p"
+ "%s::%s:%d Adjust Priority %lld %lld %d %d %lld"
+ "%s::%s:%d BITBOX SegmentEncoding Enabled %d totalFrames %d"
+ "%s::%s:%d BITBOX SegmentEncoding VBV (%d %d) startLoop %d EndLoop %d curLoop %d"
+ "%s::%s:%d Client %llu Mode %d %d %d %d"
+ "%s::%s:%d Client %llu unregistered from m_client_ids[%u]\n"
+ "%s::%s:%d Complete B->P %llu %d %d | %d %lld %lld | %p %d %d | %d %d 0x%x"
+ "%s::%s:%d Enqueue %llu %d Q in SVE %d counter %d"
+ "%s::%s:%d Enqueue %llu %d, Q in SVE %d, counter %d"
+ "%s::%s:%d Enter %lld %lld"
+ "%s::%s:%d Exit %d %d"
+ "%s::%s:%d Exit %lld %lld %d"
+ "%s::%s:%d F(%d, %d) Unexpected TimeScale changed from %d to %d"
+ "%s::%s:%d Frame %d"
+ "%s::%s:%d FrmNum %d frame_id (%d) coded_data_hdr 0x%llx, FT %d"
+ "%s::%s:%d HRD Init iscbr %d %d %d %d, %d"
+ "%s::%s:%d MCTF LFSRef buffers num %d"
+ "%s::%s:%d MCTF output buffers num %d"
+ "%s::%s:%d MaxKeyFrameInterval %d FrameRate %d MaxKeyFrameIntervalDuration %f"
+ "%s::%s:%d No more space for new client:%llu"
+ "%s::%s:%d Not Supported EncType %d"
+ "%s::%s:%d PSInfo num %d"
+ "%s::%s:%d RESET: DMV Cmd is empty"
+ "%s::%s:%d RESET: DMV Cmd is supposed to be empty by now"
+ "%s::%s:%d Row: %d, numEntryPointOffsets: %d offset_len_minus1 %d\n"
+ "%s::%s:%d SVEMap Core %d | %d %d"
+ "%s::%s:%d SetFrameInfo drl 0 %s%lld.%02lld %s%lld.%02lld"
+ "%s::%s:%d Warning : Client %llu already registered"
+ "%s::%s:%d adjust piority %lld %lld | %d %d"
+ "%s::%s:%d allocate bigger memory of timestamp %p %lld %d %d <- %d"
+ "%s::%s:%d bFlatAreaLowQpEn is enable incorrectly %d %d"
+ "%s::%s:%d bpp=%d.%02d bitrate=%d framerate=%d"
+ "%s::%s:%d cid %lld Frame %d lrmeSyncStateReady %d %s  %d"
+ "%s::%s:%d client %llu Cmd %d %lld cannot be found in client queue\n"
+ "%s::%s:%d clientID %llu PPS count %d PS num %d View num %d"
+ "%s::%s:%d clientID %llu PSInfo num %d"
+ "%s::%s:%d clientID %llu idx %d eType %d iLayerID %d iOffset %d iSize %d"
+ "%s::%s:%d clientID %llu pInitParams->sPSInfo.iNum %d header [%d] eType %d iLayerID %d iOffset %d iSize %d"
+ "%s::%s:%d clientID %llu pps headerNum %d header_len %d bits %d bytes i %d PPS ID %d PPS count %d"
+ "%s::%s:%d clientID %llu pps headerNum %d header_len %d bits %d bytes i %d PPS ID %d numView %d"
+ "%s::%s:%d client_id %llu primo_sve_id: %d next_core_sve_id: %d"
+ "%s::%s:%d copy slice header %d to 0x%08llx size %d\n"
+ "%s::%s:%d decOrder %d bits %d 1stdts %lld, dts.iTimeScale %d dts.iValue %lld hrd_t_c %d t_c %d"
+ "%s::%s:%d eWorkType %d FW creates header %d %d"
+ "%s::%s:%d failed to allocate memory of timestamp %p %lld %d"
+ "%s::%s:%d failed to generate PPS %d %d %d %d %p %d %d %d"
+ "%s::%s:%d fr %d slice_type %d, qp_val %d, slice_cb/cr_present %d slice_qp_delta %d slice_cb/cr_qp %d %d pps_cb/cr_qp %d %d"
+ "%s::%s:%d get NOTIFICATION_GET_PIPE_CONTINUE signal, for client %lld"
+ "%s::%s:%d hMCTFCmdQueue %d, cmd->client_id %llu"
+ "%s::%s:%d i %d eType %d iLayerID %d iOffset %d iSize %d"
+ "%s::%s:%d invalid encoding command %zu"
+ "%s::%s:%d mode %d SR %d"
+ "%s::%s:%d msc %d enc %d | %d %d | %d %d %d | %d"
+ "%s::%s:%d no PSInfo"
+ "%s::%s:%d restart frame contextID %d encode_row_init %d context_height_in_mb %d picHeightInMb %d"
+ "%s::%s:%d sAlgCfg.sGOP.iFeature 0x%x, numTemporalLayers %d"
+ "%s::%s:%d slice %d offset %d size %d"
+ "%s::%s:%d slice count %d"
+ "%s::%s:%d slice per frame = %d, slice_map_rows[255] = %d"
+ "%s::%s:%d uiPSHeaderBitsCount %d"
+ "%s::%s:%d | %d %d | %llu %u %u | %d %llu %llu %p | %d %d %d | %d %d 0x%x | %d"
+ "%s::%s:%d | failed to generate SPS %d"
+ "%s::%s:%d | failed to generate VUI %d"
+ "%s::%s:%d | failed to set RBSP %d"
+ "%s::%s:%d: m_psParams->header_len %d (bytes %d)"
+ "%s::%s::%d bDrop=%d bitrate=%d Fps=%d aveNDR=0x%x nTL=%d nB=%d bBref=%d mode=%d"
+ "%u:NumFilteredFrames:%u"
+ "(AVC_Level_Invalid < eLevel) && (eLevel < AVC_Level_Max)"
+ "(AVC_Profile_Invalid < eProfile) && (eProfile < AVC_Profile_Max)"
+ "(EncCommParams.ePixelConvType >= AVE_PixelConvType_None) && (EncCommParams.ePixelConvType <= AVE_PixelConvType_Custom)"
+ "(F:%lld, FN:%d): Prev frame: %p (%d), Next frame: %p (%d)"
+ "(Flag Calculation) F %d, sliceType %d VTID %d accumcbp0Cnts %d NumTemporalLayers %d \n"
+ "(HEVC_Level_Invalid < eLevel) && (eLevel < HEVC_Level_Max)"
+ "(HEVC_Profile_Invalid < eProfile) && (eProfile < HEVC_Profile_Max)"
+ "(HEVC_Tier_Invalid < eTier) && (eTier < HEVC_Tier_Max)"
+ "(Read cbp0 flag) F %d  %d accumCbp0Cnts %d  sliceType %d  VTId %d\n"
+ "(Read cbp0 flag) F %d, sliceType %d accumcbp0Cnts %d \n"
+ "(Write cbp0 flag) F %d, sliceType %d  VTId %d \n"
+ "(Write cbp0 flag) F %d, sliceType %d VTId %d accumcbp0Cnts %d  \n"
+ "(cPicMgmtParams[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr & 63) == 0"
+ "(cPicMgmtParams[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr & 63) == 0"
+ "(iBits & 7) == 0"
+ "(iFwDataBufAddr != 0) && ((iFwDataBufAddr & 127) == 0)"
+ "(psPSInfo->saBuf[iNum].sBuf.iOffset + psPSInfo->saBuf[iNum].sBuf.iSize) <= (int32_t)sizeof(psPSContext->iaPSData)"
+ "(psSliceMap != __null) && (eDevCapType >= 0) && (eDevCapType < AVE_DevCap_Type_Max) && (piSliceMapRows != __null)"
+ "./AppleAVE2FW/Common/Utils/SysUtil.cpp"
+ "./AppleAVE2FW/Firmware/HeartBeat/AVE_PP.cpp"
+ "./AppleAVE2FW/Firmware/Resource/PIODMA/AVE_PIODMACtrl.cpp"
+ "./AppleAVE2FW/Legacy/CDMVController.cpp"
+ "./AppleAVE2FW/Legacy/CMCTFControllerCommon.cpp"
+ "0 <= iLayerID && iLayerID < ((2) < ((63 + 1)) ? (2) : ((63 + 1)))"
+ "9002.78.1"
+ "AVC_FindLevelIdc"
+ "AVC_FindProfileIdc"
+ "AVC_PPS"
+ "AVC_SPS"
+ "AVE WARNING: sPTS.iTimescale changed current timescale = %d previous timescale - %d"
+ "AVE_CreateSliceMapRows"
+ "AVE_PP"
+ "AVE_PSInfo_Make"
+ "AVE_PSType_None < eType && eType < AVE_PSType_Max"
+ "AVE_QPMOD iFeature: 0x%x"
+ "AcquireAndTriggerLRMEFSForEnc"
+ "AcquireAndTriggerLRMERCForEnc"
+ "AcquireAndTriggerPIPEForEnc"
+ "AcquireAndTriggerXCODEForEnc"
+ "Adjust Piority, client_id: %lld, frm# %lld, adjust piority: %d, %d\n"
+ "Apply static QP MOD F %d, sliceType %d VTID %d accumcbp0Cnts %d \n"
+ "Baseline"
+ "Boot arguments entries : %u\n"
+ "CAVLC 4:4:4 Intra"
+ "CDMVController"
+ "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:604"
+ "Caller is /Library/Caches/com.apple.xbs/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:606"
+ "Client:%llu %llu %llu %llu AXI Error: 0x%x 0x%x 0x%x 0x%x\n"
+ "CmdStatusLookup[tag].pCmdsDoneHandle != NULL"
+ "ConfigWriteDMA"
+ "Constrained Baseline"
+ "DATA : %zu [%#zx] - data %zu, bss %zu, common %zu, noinit %zu\n"
+ "Data Cache Line Size: %u [%#x]\n"
+ "DebugStats"
+ "EncCommParams.sAlgCfg.sComm.iFrameRate > 0"
+ "EncCommParams.slicePPSIdIdx < AVE_PPS_MAX_NUM"
+ "Error: HW HANG 0x%x"
+ "Extended"
+ "FW: AppleAVE2FW-%s"
+ "FetchNthFrameInfo"
+ "GatherSharedFrameStats"
+ "Generate"
+ "GetClientBufferSize"
+ "GetCmdBuf"
+ "GetInterval"
+ "GetPicMgmtParams"
+ "GetRefCompInfo"
+ "HEVC_FindLevelIdc"
+ "HEVC_FindProfileIdc"
+ "HEVC_FindTierFlag"
+ "Heap allocated space : %zu [%#08zx]\n"
+ "Heap free space : %zu [%#08zx]\n"
+ "High"
+ "High 10"
+ "High 4:2:2"
+ "High 4:4:4"
+ "Instruction Cache Line Size: %u \n"
+ "IsGreaterOrEqual(m_start, m_end + m_iQueueSize) == false"
+ "IsNoiseSequenceComplete"
+ "LowLatency MCTF + Encode not supported in AVE"
+ "MCTF PIODMA error:%d:[%d][%d] Dst: 0x%llx (Size:%d), Src: 0x%llx (Size:%d)"
+ "MCTF_GetPastCmdCounterInfo"
+ "MV-HEVC"
+ "Main"
+ "Main 10"
+ "Main 4:2:2 10"
+ "Main 4:4:4"
+ "Main 4:4:4 10"
+ "Main RExt"
+ "Main Still"
+ "Monochrome"
+ "Monochrome 10"
+ "PPS %d: m_psParams->header_len %d (bytes %d). Prev PPSs header_len %d (bytes %d)"
+ "PerfFeature: 0x%x"
+ "PerformDeltaQPMod"
+ "PeriodicProcess"
+ "PopFront"
+ "PopFront MCTF %d %d %d %d"
+ "PopFront() for a frame in stage : %d expected to be in Output"
+ "PostXCODEProcessForEnc"
+ "ProcessCmd_Process_DMV"
+ "ProcessDMVDone"
+ "ProcessDMVStart"
+ "PushBack: F %d Q state %d, %d, %d"
+ "QPMod debug: iFeature=0x%x\n"
+ "RC params: %d %d %d %d %d 0x%llx"
+ "RC2: %s: F %d fAveFps %d (sPTS.iTimescale %d fFrameDuration %d, fAveFrameDuration %d)"
+ "RPSparams.strps.rps[%d].UsedByCurrPicS0[%d]  %hhu\n"
+ "RPSparams.strps.rps[%d].UsedByCurrPicS1[%d]  %hhu\n"
+ "RPSparams.strps.rps[%d].use_delta_flag[%d]  %hhu\n"
+ "RPSparams.strps.rps[%d].used_by_curr_pic_flag[%d]  %hhu\n"
+ "RealTime: %d"
+ "SCRATCH_REG32_RD: addr %016lx value %08x"
+ "SCRATCH_REG32_WR: addr %016lx value %08x"
+ "SPSparams.PTL.eProfile %d"
+ "SPSparams.eLevel %d\n"
+ "SPSparams.eProfile %d\n"
+ "SendFilteredFramesToEncodeProcess"
+ "SendScaledFrameToFilterProcess"
+ "SetCmdSequence"
+ "SetExecStage"
+ "SetFilterGating"
+ "SetPSContext"
+ "SignalEndOfNoiseSequence"
+ "StartDMV"
+ "Static QP MOD LOG F %d, sliceType %d VTID %d accumcbp0Cnts %d eLowerMbQPMode %d \n"
+ "TEXT : %zu [%#zx] - text %zu, cstring  %zu, const %zu\n"
+ "UpdateStaticAreaCbp0Counts"
+ "[PERF] XXXX client[%llu] EncCommParams.pFwProfile %p\n"
+ "[PERF] XXXX client[%llu] dump buffer %p\n"
+ "[PERF] client %llu dump buffer %p (allocated)\n"
+ "bOutputStageSet"
+ "bStageSet"
+ "cPicMgmtParams.GetScaledPlaneBuf(AVE_BufIdx_Luma).saIBuf[AVE_BufIdx_Data].iAddr == 0"
+ "cPicMgmtParams[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr != 0"
+ "cPicMgmtParams[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr != 0"
+ "cPicMgmtParams[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr %016llx\n"
+ "calcVbvLoopNum"
+ "clientBufferAvailableSize >= kClientBufferSize[iWorkType - 1]"
+ "command != NULL && command->canExecute == true"
+ "currEncCmd.cmdQueueCmdIndex != 0"
+ "currFrameNum == pInPicParams->sFrameInfo.sGOPInfo.iFrameNum"
+ "enc_type <= AVE_EncType_Max"
+ "entry->stack != NULL"
+ "fCRFScale: %d.%03d"
+ "fchou_debug: bFlatAreaLowQpEn=%d bExtremeLumaQPModEn=%d\n"
+ "fchou_debug: bLowerQP4MbEn=%d\n"
+ "hCtrl->MCTF_GetExecStage(pCmdBufOut) == MCTF_Stage_Filtered"
+ "hMctfCtrl != NULL"
+ "hrd_time_scale == dts.iTimescale"
+ "iClientBufferAvailableSize >= kClientBufferSize"
+ "iFrmPosPlus1 > 0"
+ "iN > 0 && iN <= m_iCurSize"
+ "iTotalFrameCnt: %d"
+ "level %d"
+ "m_AVEController != NULL"
+ "m_iNumFilteredFramesAtHead"
+ "m_iNumFilteredFramesAtHead == 0"
+ "m_psMgmtParams != NULL"
+ "m_psParams->header_len == 0"
+ "m_queue->m_sFifo[m_position].m_pCmdBuf != NULL || m_queue->m_sFifo[m_position].m_eExecStage >= MCTF_Stage_Output"
+ "mctf_pipeClient->WorkType() == AVE_WorkType_MCTF"
+ "outputChromaStride != 0"
+ "outputLumaStride != 0"
+ "pAvcInitCmd->sFwClientMem.iAddr != 0"
+ "pClient != NULL"
+ "pClientBuffer != NULL"
+ "pCmd->frameType==IMG_MCTF_FILTERING"
+ "pCmdCounterInfo->iFrameNum == hCtrl->MCTF_GetFrameNumber(pCmdBufOut)"
+ "pCurrFrmInfo != NULL"
+ "pHevcInitCmd->sFwClientMem.iAddr != 0"
+ "pInPicParams->sFrameInfo.sGOPInfo.iFrameType == IMG_MCTF_FILTERING"
+ "pPicParams != NULL && cPicMgmtParams.IsCompressed()"
+ "pPicParams->sInput.sMultiPassStats.iAddr != 0"
+ "pSessionCfg->sEnc.sAlgCfg.sGOP.iFeature 0x%x"
+ "pSessionCfg->sEnc.sAlgCfg.sGOP.iNumOfFrame[AVE_FrameType_B] %d"
+ "pSessionCfg->sEnc.sAlgCfg.sGOP.iNumOfTemporalLayer %d"
+ "pcCurrFrmInfo != NULL"
+ "pcCurrFrmInfo != NULL && pcCurrFrmInfo->m_iFrameNumber == currFrameNum"
+ "pcRefFrameInfo->m_bIsCompressInput || pcRefFrameInfo->GetExecStage() >= MCTF_Stage_Scaled"
+ "piPSData != __null && psPSContext != __null"
+ "print"
+ "res == RTK_ST_OK"
+ "ret"
+ "rt == AVE_OK"
+ "sBufSet.saCodedData[%d].iAddr:%016llx\n"
+ "sBufSet.saCodedData[%d].iSize:0x%x\n"
+ "sBufSet.saEntropyCoding[%d][%d].iAddr:%016llx\n"
+ "sBufSet.saRecon[%d][0].iAddr:%016llx\n"
+ "sLambdaMod.iFeature: 0x%x"
+ "semaArray[SIGNAL_CHANNEL_PERIODIC_PROCESS] != (SEMA)0"
+ "stack_ptr != NULL"
+ "tmpPIPECmd->frameType == IMG_MCTF_FILTERING"
+ "updateHrdStatus"
+ "updateTempID"
+ "vui_parameters"
+ "~CAVECommonController"
- "\t%d : %d\n"
- "\n----AVE_VERBOSE_INIT_PARAMS----"
- "                size : %zu [%#08x] [%zu.%zu MB]\n"
- "    slice %d ui32BytesWritten %d"
- "   ~~~ Clean Reset ~~~~ "
- "   ~~~ Optimal Reset ~~~~ "
- " + CMCTFController::EnqueueFrames (%d)"
- "!a64e"
- "%d %p %p %d %d"
- "%s %d %lld %d"
- "%s : %s\n"
- "%s:%d %d F %d %d"
- "%s:%d 0x%llx %d %d"
- "%s:%d DPB ERROR: %lld %d"
- "%s:%d FrameType: %d FrameNum: %d POC: %d qp: %d"
- "%s:%d HRD Init iscbr %d %d %d %d"
- "%s::%d: F %d pos %d set to MCTF_Stage_Ready"
- "%s::%s Enter %d %d %d"
- "%s::%s Enter %d %d %d %p"
- "%s::%s Enter %d %d %d %p %d"
- "%s::%s Enter %p %d %d %d"
- "%s::%s Enter %p %p %llx %d %d %lld %d %d %d"
- "%s::%s Exit %d "
- "%s::%s Exit %d %lld"
- "%s::%s Exit %d %lld %lld %d %d"
- "%s::%s Exit %lld %d %lld 0x%08x %d %d"
- "%s::%s Exit %p %d %d %d"
- "%s::%s Exit %p %d %d %d %d"
- "%s::%s Exit %p %p %d"
- "%s::%s RCMode %d fQuality %d quality %d"
- "%s::%s:%d  %d F %d Type %d POC %d | %d %d | S0 %d %hhu %d %hhu | S1 %d %hhu"
- "%s::%s:%d  Thread = %#x, priority = %d\n"
- "%s::%s:%d %d %lld %lld"
- "%s::%s:%d %d %lld %lld | %p %d %d %d | %p %d %d | %d %d 0x%x"
- "%s::%s:%d %d F %d %d %d %d"
- "%s::%s:%d %d F %d POC %d numTemporalLayers %d cur_temporalId %d max_ref_pic_temporalId %d %d %d"
- "%s::%s:%d %d F %d POC %d ref_poc %d"
- "%s::%s:%d %d F %d Type %d POC %d | %d %d | %d %hhu %d %hhu"
- "%s::%s:%d %lld %d %d %d"
- "%s::%s:%d %lld %d %d %d | %lld | %d %d %d | %d %d %d %d"
- "%s::%s:%d %lld %d %lld %d"
- "%s::%s:%d %lld %d %lld 0x%08x"
- "%s::%s:%d %lld %d %lld 0x%08x %d"
- "%s::%s:%d %p %d %d %d | %d %lld %d - %d %lld %d | %d.%03d %d.%03d"
- "%s::%s:%d %p %d %d | %d %lld %d - %d %lld %d | %d.%03d  %d.%03d"
- "%s::%s:%d %p %lld 0x%llx %p %p %d %d"
- "%s::%s:%d %s | Frame number out of range %p %lld %d %lld"
- "%s::%s:%d %s | Wrong parameter %p %lld %d"
- "%s::%s:%d %s | Wrong parameter %p %lld 0x%llx %p %p"
- "%s::%s:%d %s | Wrong parameter %p %lld 0x%llx %p %p | %f %f %d %d"
- "%s::%s:%d %s | fail to add PTS to FPS %p %lld 0x%llx %p %p %d"
- "%s::%s:%d %s | fail to initialize FPS %p %d %d %d.%03d %d.%03d %d %d %d %d"
- "%s::%s:%d %s | fail to update FPS %p %d %d %d.%03d %d.%03d %d %d %d %d"
- "%s::%s:%d %s | fail to update FPS %p %lld 0x%llx %p %p %d"
- "%s::%s:%d %s | failed to allocate memory of timestamp %p %d %d %d"
- "%s::%s:%d %s | failed to calculate average FPS %p %p"
- "%s::%s:%d %s | failed to calculate realtime FPS %p %p"
- "%s::%s:%d %s | failed to calculate sliding average FPS %p %p"
- "%s::%s:%d %s | wrong parameters %p %d %d %d"
- "%s::%s:%d %s | wrong state %p"
- "%s::%s:%d %s | wrong state %p %p"
- "%s::%s:%d Adjust Priority %lld %d %d %d %lld"
- "%s::%s:%d Client %d Mode %d %d %d %d"
- "%s::%s:%d Client %d unregistered from m_client_ids[%lld]\n"
- "%s::%s:%d Client is not MCTF enabled %lld"
- "%s::%s:%d Complete B->P %d %d %d | %d %lld %lld | %p %d %d | %d %d 0x%x"
- "%s::%s:%d Enqueue %d %d Q in SVE %lld counter %d"
- "%s::%s:%d Enqueue %d %d, Q in SVE %lld, counter %d"
- "%s::%s:%d Enter lrmeRCPassNum %d refIdxRc  %d rcPass %d"
- "%s::%s:%d Frame[%lld] op %llu PTS %lld | interval %d %d %d.%03d %d.%03d | status %lld %lld %lld | Hint %d %d"
- "%s::%s:%d FrmNum %d coded_data_hdr 0x%llx, FT %d"
- "%s::%s:%d InitEncodingParameters: sAlgCfg.sGOP.iFeature 0x%x, HiB %d, numTemporalLayers %d"
- "%s::%s:%d No more space for new client:%d"
- "%s::%s:%d Not Supported Codec %d"
- "%s::%s:%d PSInfo.Num %d"
- "%s::%s:%d PocStCurrAfter %d"
- "%s::%s:%d PocStCurrBefore %d PocStFoll %d"
- "%s::%s:%d SVEMap Core %d | %d %d %d"
- "%s::%s:%d Warning : Client %d already registered"
- "%s::%s:%d adjust piority %lld %d | %d %d"
- "%s::%s:%d align32MbW is invalid %d %d"
- "%s::%s:%d allocate bigger memory of timestamp %p %d %d <- %d"
- "%s::%s:%d bFlatAreaLowQpEn is enable incorrectly %d %d %d"
- "%s::%s:%d cid %lld Frame %d lrmeSyncStateReady %d %s codec %d"
- "%s::%s:%d client %d Cmd %d %lld cannot be found in client queue\n"
- "%s::%s:%d client_id %d primo_sve_id: %d next_core_sve_id: %d"
- "%s::%s:%d client_id %lld cmdID %d FrameNum %d"
- "%s::%s:%d client_id %lld, cmdID %d"
- "%s::%s:%d completeQueue is Empty"
- "%s::%s:%d enable_qp_mod is disabled incorrectly %d"
- "%s::%s:%d failed to allocate memory of timestamp %p %d"
- "%s::%s:%d hMCTFCmdQueue %d, cmd->client_id %d"
- "%s::%s:%d i %d Complete client %lld Frame %d"
- "%s::%s:%d iMaxKeyFrameInterval %d iExpectedFrameRate %d fMaxKeyFrameIntervalDuration %f"
- "%s::%s:%d idx %d etype %d iLayerID %d iOffset %d iSize %d headerp %p"
- "%s::%s:%d invalid encoding command %lld"
- "%s::%s:%d move complete from MCTF to Enc %d %d"
- "%s::%s:%d pps 2 header_len bits = %d bytes = %d pps_pic_parameter_set_id = %d"
- "%s::%s:%d restart frame contextID %d encode_row_init %d force_context_stop %d context_height_in_mb %d picHeightInMb %d"
- "%s::%s:%d slice per frame = %d, slices_map_rows[255] = %d"
- "%s::%s:%d | %lld %d %d %d | %lld | %d %d %d | %d %d %d %d"
- "%s::%s:%d, client_id %lld, cmdCounter %lld"
- "(MCTFStrength + 1) <= (uint32_t)numFilterLevels"
- "(Read cbp0 flag) F %d  %d accumCbp0Cnts %d  sliceType %d  \n"
- "(Write cbp0 flag) F %d, sliceType %d  \n"
- "(mbAddressCPUFWData & 63) == 0"
- "(pInPicParams->sInput.Y & 63) == 0"
- "(pInputData->UV & 63) == 0"
- "(pPicParams->sInput.UV & 63) == 0"
- "(pPicParams->sInput.Y & 63) == 0"
- "(psInputData->UV & 63) == 0"
- "(psInputData->Y & 63) == 0"
- "+ CMCTFController::ProcessLRMEDone\n"
- "+ CMCTFController::SetDefaultParameters\n"
- "+ CRateControl::ProcessInit"
- "- CMCTFController::SetDefaultParameters\n"
- "- CRateControl::ProcessInit"
- "------  Reset MCTF Params ------"
- "----AVE_VERBOSE_BUFFERS----\n"
- "----AVE_VERBOSE_INIT_PARAMS----\n"
- "----AVE_VERBOSE_RPS----\n"
- "----AVE_VERBOSE_SLICE----\n"
- "----AVE_VERBOSE_SPS_PPS----"
- "----AVE_VERBOSE_SPS_PPS----\n"
- "8002.46.0"
- "AVC COMMON:: disable_intra_mode: %x\n"
- "AVE ERROR HEADER OVERFLOW"
- "AVE WARNING: PTSTimescale changed current timescale = %d previous timescale - %d"
- "AcquireAndTriggerLRMEFS"
- "AcquireAndTriggerLRMERC"
- "AcquireAndTriggerPIPE"
- "AcquireAndTriggerXCODE"
- "Adjust Piority, client_id: %lld, frm# %d, adjust piority: %d, %d\n"
- "Boot arguments entries : %zu\n"
- "CMCTFController Constructor!!"
- "CPlatformEnvironment"
- "Client:%d %d %d %d AXI Error: 0x%x 0x%x 0x%x 0x%x\n"
- "Complete B->P %d %lld %lld | %p %d %d | %d %d 0x%x "
- "DATA : %zu [%#x] - data %zu, bss %zu, common %zu, noinit %zu\n"
- "Data Cache Line Size: %zu [%#zx]\n"
- "EncCommParams.cycleBuffer0"
- "EncCommParams.cycleBuffer1"
- "EncCommParams.eStaticAreasLowQpSel == STATICAREAS_LOWQP_DISABLE"
- "EncCommParams.slicePPSIdIdx < AVE_MAX_NUMBER_OF_PPS"
- "EncCommParams.slices_per_frame <= AVE_SLICE_MAX_NUM"
- "F %d Graceful shutdown mark m_bIsReadyToDequeue as true"
- "F %d process cbp0Cnt, IsThisFrameMarkedAsNonReferenceReturned = %d\n"
- "FW: AppleAVE2FW-%s \n"
- "FetchPrevRefFrame"
- "FetchReadyFrame (%s): F %d, %p"
- "FetchScalerFrame (%s): F %d, %p m_iCurSize %d"
- "HEVC COMMON:: disable_intra_mode: %x\n"
- "Halt "
- "Heap allocated space : %zu [%#08x]\n"
- "Heap free space : %zu [%#08x]\n"
- "IBDebug F %d process cbp0Cnt, IsThisFrameMarkedAsNonReferenceReturned = %d EncCommParams.bCbp0CntBufReset %d\n"
- "Instruction Cache Line Size: %zu \n"
- "LRFS"
- "LRMERC"
- "Linked on : %s - %s\n"
- "MCTF mark as flushed %d"
- "MCTFComplete"
- "MD_InterLambda: %d"
- "MD_IntraLambda: %d"
- "MD_IntraOffset: %d"
- "ME_FullPelLambda: %d"
- "ME_LowResLambda: %d"
- "ME_SubPelLambda: %d"
- "MarkFrameAsFlushedForMCTF"
- "No conversion C %lld, Q %d, F %d"
- "NotificationToHost %d %lld %d 0x%x "
- "NotificationToHost %d %lld %d 0x%x %d "
- "Open %lld %lld"
- "PIPE"
- "PPSParams.SizeOfStructure %d"
- "PopBack MCTF %d %d %d"
- "PopBack() when MctfFrameQueue is empty!"
- "PopBack: F %d Q state %d, %d, %d"
- "PopFront Dummy Frame num %d curSize%d"
- "PopFront MCTF %d %d %d %d %d"
- "PopFront() for a frame that's not filtered yet!"
- "Pos: %d, numEntryPointOffsets: %d offset_len_minus1 %d\n"
- "PostXCODEProcess"
- "PrepareClientMCTFQueue"
- "PushBack: F %d Q state %d, %d, %d, D %d"
- "RC params: %d %d %d %d %d %d"
- "RC2: %s: F %d fAveFps %d (PTStimescale %d fFrameDuration %d, fAveFrameDuration %d)"
- "RDDMALOWRESSRC_FMT 0x%x "
- "RDDMAMBSRCCHROMA_FMT 0x%x "
- "RDDMAMBSRCLUMA_FMT 0x%x "
- "RPSparams.strps.rps[%d].UsedByCurrPicS0[%d]  %d\n"
- "RPSparams.strps.rps[%d].UsedByCurrPicS1[%d]  %d\n"
- "RPSparams.strps.rps[%d].use_delta_flag[%d]  %d\n"
- "RPSparams.strps.rps[%d].used_by_curr_pic_flag[%d]  %d\n"
- "RealTimeClient: %d"
- "Row: %d, numEntryPointOffsets: %d offset_len_minus1 %d\n"
- "SCRATCH_REG32_RD: addr %016llx value %08x"
- "SCRATCH_REG32_WR: addr %016llx value %08x"
- "SHParams.SizeOfStructure %d\n"
- "SPSparams.PTL.general_profile_idc %d"
- "SPSparams.SizeOfStructure %d"
- "SPSparams.level_idc %d\n"
- "SPSparams.profile_idc %d\n"
- "Scaler"
- "SendFrameToEncodeProcess"
- "SetFilteredState for a frame %d that's not processed yet!"
- "SetFrameInfo drl 0 %s%lld.%02lld %s%lld.%02lld"
- "SetReadyExecStage"
- "SlicesSize[%d] is %d\n"
- "Start AVC %lld %lld"
- "Start HEVC %lld %lld"
- "Start LRME %lld %lld"
- "StaticAreaQpTask"
- "Stop %lld %lld"
- "TEXT : %zu [%#x] - text %zu, cstring  %zu, const %zu\n"
- "TotalNumberOfFrames: %d"
- "Unexpected F %d!"
- "WARN [%d, %d]: ramp stage %d m_iCurSize %d"
- "WARN: F (%d) NEXT IsDummy %d, ReadyToDequeue %d"
- "WARN: F (%d) PREV %d IsDummyFrame %d, ReadyToDequeue %d"
- "WARNING: FetchNextRefFrame() when MctfFrameQueue is empty!"
- "WARNING: FetchPrevRefFrame() when MctfFrameQueue is empty!"
- "WARNING: FetchReadyFrame() when MctfFrameQueue is empty!"
- "WARNING: FetchScalerFrame() when MctfFrameQueue is empty!"
- "WARNING: Frame %d Pos %d might have already been scaled!"
- "WARNING: Not a valid position %d for F %d!"
- "WARNING: PopFront() for a frame that's not processed yet!"
- "WARNING: PopFront() when CPB Frame Queue is empty!"
- "WARNING: PushBack() when CPB Frame Queue %d is full!"
- "WARNING: SetProcessedState for a frame %d that's not Run yet!"
- "[PERF] XXXX client[%d] EncCommParams.pFwProfile %p\n"
- "[PERF] XXXX client[%d] dump buffer %p\n"
- "[PERF] client %d dump buffer %p (allocated)\n"
- "[last]: slice_count = %d, remove = %d\n"
- "bAllowFrameReordering: %d"
- "bDisableBinCountsInNALunitCheck: %d"
- "bDisableIntra16x16: %d"
- "bDisableIntra4x4: %d"
- "bDisableIntra8x8: %d"
- "bEnableContextSwitchInTheMiddleOfAFrame: %d"
- "bEnableLamdaMod: %d"
- "bEnableMBInputCtrl: %d"
- "bEnableQPMod: %d"
- "bEnableQPModChroma: %d"
- "bEnableQPModRefresh: %d"
- "bRestrictInter4x4: %d"
- "bSkipThrdEn: %d"
- "bUseCAVLCBits: %d"
- "cdai_debug: bpp=%d.%02d, bitrate=%d, framerate=%d,"
- "clientBufferAvailableSize >= kClientBufferSize[client_type - 1]"
- "codec_type <= AVE_VIDEO_CODEC_MAX"
- "coded_data_hdr->ui32_numAccumSkipMbCntNMbs <= EncCommParams.valid_mb_height*EncCommParams.pic_width_in_mbs"
- "commandQueue"
- "copy slice header %d to 0x%08llx size %d\n"
- "disable_intra_mode: %d"
- "eStaticAreasLowQpSel: %d"
- "enable_IPCM_in_IntraSlice: %d"
- "entry->stack != 0"
- "fQuality: %d"
- "fchou_debug: bFlatAreaLowQpEn=%d bPerceptualQualityOptimization=%d bExtremeLumaQPModEn=%d\n"
- "fchou_debug: eStaticAreasLowQpSel=%d bLowerQP4MbEn=%d\n"
- "fr %d slice_type %d, slice_cb/cr_present %d slice_qp_delta %d slice_cb/cr_qp %d %d pps_cb/cr_qp %d %d"
- "frame num = %d \n"
- "frame_done"
- "general_level_idc %d"
- "gpTimerArray[0] != 0"
- "iAverageNonDroppableFrameRate: %d"
- "inputReadySema != (SEMA)0"
- "long_term_ref: %d"
- "ltr_refidx: %d"
- "m_sFifo[iPrevFrmPos].m_eExecStage >= CPB_Stage_Run"
- "m_sFifo[iPrevFrmPos].m_eExecStage >= MCTF_Stage_Run"
- "mbAddrFWData:%016llx, mbAddrFWData sz:%016zx\n"
- "mbAddressCPUFWData != 0"
- "nSuccess==0"
- "no_bipred: %d"
- "numEntryPointOffsets != 0"
- "numFPCPUCand: %d"
- "outputReadySema != (SEMA)0"
- "pAvcInitCmd->iFwClientMemAddr != 0"
- "pHevcInitCmd->iFwClientMemAddr != 0"
- "pInPicParams"
- "pInPicParams->sInput.Y != 0"
- "pInPicParams.sInput.Y %016llx\n"
- "pInVideoParams->enable_tmvp %d, %d"
- "pInVideoParams->iBFrames %d"
- "pInVideoParams->no_bipred %d, %d"
- "pInVideoParams->numBTemporalLayers %d"
- "pInVideoParams->numFPCPUCand %d, %d"
- "pInVideoParams->numTemporalLayers %d"
- "pInVideoParams->sAlgCfg.sGOP.iFeature 0x%x"
- "pInVideoParams->sao_enb_config %d, %d"
- "pInVideoParams->sao_eo_bo_offset_config %d, %d"
- "pInVideoParams->sao_rdd_off_offset_chroma %d, %d"
- "pInVideoParams->sao_rdd_off_offset_luma %d, %d"
- "pInVideoParams->split_mode %d, %d"
- "pInputData->UV != 0"
- "pPicParams->sInput.MultiPassStatsInBuffer != 0"
- "pPicParams->sInput.UV != 0"
- "pPicParams->sInput.Y != 0"
- "pRCParams->iExpectedFrameRate > 0"
- "p_apsCodedSize[%d]:0x%x\n"
- "p_apsCoded[%d]:%016llx\n"
- "p_apsEntropyCoding[%d][%d]:%016llx\n"
- "p_apsReconPictures[%d][0]:%016llx\n"
- "pcPrevFrmInfo[meRefIdx]"
- "psInputData->ScaledSrc == 0"
- "psInputData->UV != 0"
- "psInputData->Y != 0"
- "sao_enb_config: %d"
- "sao_eo_bo_offset_config: %d"
- "sao_rdd_off_offset_chroma: %d"
- "sao_rdd_off_offset_luma: %d"
- "sigAvail == true"
- "slice %d offset %d\n"
- "slice count is:%d\n"
- "slices_per_frame is %d\n"
- "staticAreaQpTask"
- "statsDMAAddr:%016llx, statsDMABufferSz:%08x\n"
- "verbose: %d"

```
