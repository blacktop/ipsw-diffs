## AppleAVE2FW_H13D.im4p

> `Firmware/ave/AppleAVE2FW_H13D.im4p`

```diff

 
-  __TEXT.__text: 0xfb2c8 sha256:245bac781f9f39eacb8ebc8128102e87d530185c109cb30613319c515e504195
-  __TEXT.__const: 0x228d4 sha256:6568d432eac836e1a7c35ac1106b39cfc0ed9d76fa9f099405c65ed33bf5eeeb
-  __TEXT.__cstring: 0x162dc sha256:13dcc4e7d9e92e6e2ecec3b25fac821f62a0421e64b099eae121fda6e2e4ae75
+  __TEXT.__text: 0xfd710 sha256:48c922eb8a252f004c54bb7fdc3323a821d0fd72c08961a95d15af608f8ff0f2
+  __TEXT.__const: 0x21130 sha256:0560ecab75b90cf6fdee7f5f372e39fafec462ba4793248aaeadee4953393dc1
+  __TEXT.__cstring: 0x14587 sha256:6b6335300d869c601a7c1a1308841a6ac31a470a693646b594e864d91754bead
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x18 sha256:f7aacdffbecb01f600f76c16c652b654acc0f23de33c0eada5da809691951e7c
-  __DATA._rtk_patchbay: 0x211 sha256:086c33db7b68c6daf48001bdc366ef85d726e4fffbe45b3a89e44eab9719296d
-  __DATA.__data: 0x10b0 sha256:466a40570ca7a83e617c0ed34ed64d0795cd3ef9d54d2031ba3909d22170b4e6
-  __DATA._rtk_mtab: 0x2b8 sha256:2dd4812e2e98f733e774080cfda2200a1513bd1aaf589d42ff87f0351caf6aa7
-  __DATA.__const: 0x3bc8 sha256:f5b245578b37673698b51d7748f5a30df9d328dc9a35c032fb5822cbc57c6f68
-  __DATA._rtk_power: 0x3b8 sha256:e5f2861039b10d5ce950444126546f1f7eca5a90c7b4376bfc6831c9918b7046
+  __TEXT.__chain_starts: 0x20 sha256:82adcb75e44549a170eeb824dd16f2286537127fb728a788e186d1e4ad72f6a9
+  __DATA._rtk_patchbay: 0x211 sha256:6bd53cb4aef056709bd6d7569d2c20738aa6a279eed62277fae5654844ea7ac3
+  __DATA.__data: 0x1050 sha256:2803aca56dddaf80e336ac0934b02e46adb4008dd3321c8de8b33474a2f211b9
+  __DATA._rtk_mtab: 0x2b8 sha256:ec15efa62cf115feb912661e929c070f5605ca3492883c0e99a7d8201b30a821
+  __DATA._rtk_power: 0x3b8 sha256:a5a4085e91b142843f800a5cde425ba63dde40d24e62f258dabef1bd687309f7
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
+  __DATA.__const: 0x33e0 sha256:1c94fa8f6e8ec5c9bd63db4629c86e17efd2e4c566e6d860634a8d4d1764d11c
   __DATA._rtk_tunables: 0x1e8 sha256:ddade0037eec2bfe870a7e2ca0ef8c73274c435ca6a918ab8140b2d7b5eb36cc
   __DATA._rtk_init_stack: 0x10000 sha256:854fb91a21433799707bd85798d5fe48998be2719204088d0d153f31fdb39bd3
   __DATA._rtk_irq_stack: 0x1000 sha256:a58a5a5fd0fbe091da4f0002b097ea1d54081034cedc964226a8fcf703e37c81

   __DATA._rtk_heap: 0x0
   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
-  __DATA.__zerofill: 0xd2ee0 sha256:89c8d9216789bfc73db1a1d834c4f0a222940a172c29f5283fc855f33494850b
-  UUID: BB5AD4BA-055B-32B5-9B80-7B9282131960
-  Functions: 1151
-  Symbols:   1611
-  CStrings:  2524
+  __DATA.__zerofill: 0xd2680 sha256:66d8b4d104eed3801a7e38a489ab8dee50e349e5fbd83d2dde42ac78ac08f807
+  UUID: 7EA461B7-CB38-3F84-B919-3230C889DCF7
+  Functions: 1110
+  Symbols:   1558
+  CStrings:  2385
 
Symbols:
+ _RTK_scheduler_pause
+ __Z15AVE_History_AddP14_S_AVE_HistoryyiiiiPKcz
+ __Z15AVE_PSInfo_MakePKh13_E_AVE_PSTypeiiP16_S_AVE_PSContext
+ __Z17AVE_History_PrintP14_S_AVE_Historyji
+ __Z17AVE_SetTunableRegP14sAVERegTunablejj
+ __Z18AVE_History_Createi
+ __Z19AVE_History_DestroyP14_S_AVE_History
+ __Z27AVE_H264_PrepareSliceHeaderP13sCommonParamsPK26H264_PICTURE_HEADER_PARAMSP24H264_SLICE_HEADER_PARAMSji
+ __Z27AVE_HEVC_PrepareSliceHeaderP13sCommonParamsPK27HEVC_SEQUENCE_HEADER_PARAMSPK26HEVC_PICTURE_HEADER_PARAMSP24HEVC_SLICE_HEADER_PARAMSjbbi
+ __Z32AVE_H264_Update_POClsb_SliceTypeP13sCommonParamsP24H264_SLICE_HEADER_PARAMSij
+ __Z32AVE_HEVC_Update_POClsb_SliceTypeP13sCommonParamsP24HEVC_SLICE_HEADER_PARAMSij
+ __Z7barrierPv
+ __ZN10HEVC_Slice12slice_headerEP16AVE_SyntaxWriterRK27HEVC_SEQUENCE_HEADER_PARAMSRK26HEVC_PICTURE_HEADER_PARAMSP8HEVC_RPSjj
+ __ZN10HEVC_Slice23generateSliceHeaderInKFERK27HEVC_SEQUENCE_HEADER_PARAMSRK26HEVC_PICTURE_HEADER_PARAMSP8HEVC_RPS
+ __ZN11AVE_DevInfo15GetDevSubIDFlagEv
+ __ZN11AVE_DevInfo17GetDevNumPerGroupEv
+ __ZN11AVE_DevInfo8GetDevIDEv
+ __ZN11AVE_DevInfo8GetSVEIDEv
+ __ZN11AVE_DevInfo9GetDevNumEv
+ __ZN11RateControl14CreateInstanceERK21RateControlParametersP10FrameStatsjPv
+ __ZN11RateControl17updateRateControlEjj
+ __ZN11RateControl18insertCBRFillerAVCEP17_S_AVE_FillerInfo13_E_AVE_RCModej
+ __ZN11RateControl18processRateControlEjii
+ __ZN11RateControl19insertCBRFillerHEVCEP17_S_AVE_FillerInfo13_E_AVE_RCModejjj
+ __ZN11RateControl23updateBitsFromTranscodeEjjiPj
+ __ZN11RateControlC2ERK21RateControlParametersP10FrameStatsjPv
+ __ZN12CAvePipeMcpu9StartUnitEiii
+ __ZN12CRateControl10AccumulateEj9SliceTypejjP16sCRCStatPerFramehS0_
+ __ZN12CRateControl11RateControlEj9SliceTypejjbjbbbjiS0_bb
+ __ZN12CRateControl16computeCorrCoeffEPjjj
+ __ZN12CRateControl17ProcessAccumulateEj9SliceTypejjP16sCRCStatPerFramehS0_
+ __ZN12CRateControl18ProcessRateControlEj9SliceTypejjbjbbbjiS0_b
+ __ZN12CRateControl20AVE_CBR_InsertFillerEjjPK24HEVC_SLICE_HEADER_PARAMS13_E_AVE_RCModeP17_S_AVE_FillerInfo
+ __ZN13CAVECommonDPB10DRLConvertEP14_S_AVE_DRL_Cfgd
+ __ZN13CAVECommonDPB22ProvideReferenceFramesEjP16AVE_VIDEO_PARAMSj
+ __ZN13COFControllerC1EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN13COFControllerC2EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN14CAVCController12SetTranscodeEv
+ __ZN14CAVCController14ConfigureMCPUsEP18AVE_PICMGMT_PARAMS
+ __ZN14CAVCController14stitchColoDataEy
+ __ZN14CAVCController16SyncCheckQPMcoreEPvj
+ __ZN14CAVCController19GetSliceHeaderForFWEPhPjj
+ __ZN14CAVCController20SetLRMERCPerSrcFrameEPK18AVE_PICMGMT_PARAMS
+ __ZN14CAVCController26UpdateStaticAreaCbp0CountsEP14CODED_DATA_HDRj
+ __ZN14CAVCController28ProcessDataFromCpusMultiCoreEv
+ __ZN14CAVCController32PipeProcessStandaloneRateControlEP18AVE_PICMGMT_PARAMSP24H264_SLICE_HEADER_PARAMS
+ __ZN14CAVCController7setPipeEP18AVE_PICMGMT_PARAMS
+ __ZN14CAVCController9SetLRMERCEPK18AVE_PICMGMT_PARAMS
+ __ZN14CAVCController9setPipeGoEP15sCmdInformation
+ __ZN14CAVCControllerC1EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN14CAVCControllerC2EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN14CAVEFilterBaseC2EPKcP7CObjectibmm
+ __ZN14CDMVControllerC1EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN14CDMVControllerC2EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN15CFlowController20McpuControllerCreateEPKci
+ __ZN15CFlowController20PipeISRManagerCreateEPKciPPVm
+ __ZN15CHEVCController10SetRpsVarsEjP25HEVC_SLICE_SHORT_TERM_RPSP24HEVC_SLICE_LONG_TERM_RPSP22HEVC_SPS_LONG_TERM_RPSjh
+ __ZN15CHEVCController14ConfigureMCPUsEP18AVE_PICMGMT_PARAMS
+ __ZN15CHEVCController16SyncCheckQPMcoreEPvj
+ __ZN15CHEVCController20StaticAreaInterApplyEP18AVE_PICMGMT_PARAMSPjjj
+ __ZN15CHEVCController26GenerateScalingListDataPPSEv
+ __ZN15CHEVCController32PipeProcessStandaloneRateControlEP18AVE_PICMGMT_PARAMSP24HEVC_SLICE_HEADER_PARAMS
+ __ZN15CHEVCController8calc_rpsEhiP23HEVC_SPS_SHORT_TERM_RPSP19HEVC_SHORT_TERM_RPSP22HEVC_SPS_LONG_TERM_RPSP24HEVC_SLICE_LONG_TERM_RPSj
+ __ZN15CHEVCController9setPipeGoEP15sCmdInformation
+ __ZN15CHEVCControllerC1EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN15CHEVCControllerC2EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN16AVE_SyntaxWriter16RBSPTrailingBitsEPh
+ __ZN16AVE_SyntaxWriter6SetEBPEb
+ __ZN16AVE_SyntaxWriterC1EPhib
+ __ZN16AVE_SyntaxWriterD0Ev
+ __ZN18CAVEPipeISRManagerC1EPKcP7CObjectibPPVmP14AVE_PIODMACtrl
+ __ZN18CAVEPipeISRManagerC2EPKcP7CObjectibPPVmP14AVE_PIODMACtrl
+ __ZN19CFlowControllerBase13DoneEventPipeEPv
+ __ZN19CFlowControllerBase14StartEventPipeEPv
+ __ZN19CFlowControllerBase14StartEventPipeEv
+ __ZN19CFlowControllerBase17GetStatsEventPipeEPv
+ __ZN19CFlowControllerBase26HandleCmdQueueForFrameDropEP15sCmdInformationj
+ __ZN19CFlowControllerBase7FSMPipeE
+ __ZN20CAVECommonController10SetTunableEb
+ __ZN20CAVECommonController11initWeightsEP18_S_AVE_WtPred_Infoii
+ __ZN20CAVECommonController14PrintDbgCyclesEbj
+ __ZN20CAVECommonController14computeWeightsEjjPjjP18_S_AVE_WtPred_Infojj9SliceType
+ __ZN20CAVECommonController16g_bTunableLoadedE
+ __ZN20CAVECommonController17CreateRateControlEi
+ __ZN20CAVECommonController17GetThroughputModeEv
+ __ZN20CAVECommonController18finalizeWeightsSEsEP24HEVC_SLICE_HEADER_PARAMSj
+ __ZN20CAVECommonController21g_bCodecTunableLoadedE
+ __ZN20CAVECommonController23g_bMePipe1TunableLoadedE
+ __ZN20CAVECommonControllerC2EPKcP7CObjectPvijbP14AVE_PIODMACtrl
+ __ZN20CPlatformEnvironment17RTK_platform_initEv
+ __ZN21ConstantQpRateControl18processRateControlEjii
+ __ZN22CAVEPipeISRManagerBaseC2EPKcP7CObjectib
+ __ZN22CAVEPipeMcpuController12StartAvePipeEiiijPv
+ __ZN22CAVEPipeMcpuController5StartEiiijPv
+ __ZN22CAVEPipeMcpuControllerC1EPKcP7CObjectib
+ __ZN26CAVEPipeMcpuControllerBaseC2EPKcP7CObjectib
+ __ZN3HRD15updateHrdStatusEjPK11_S_AVE_TimefRiS3_f
+ __ZN3HRD4initEbjPK11_S_AVE_Timejff
+ __ZN5AveRC23qp2qscale_float_genericEjj
+ __ZN5AveRC23qscale2qp_float_genericEfj
+ __ZN7AVC_PPS22pic_parameter_set_rbspEii
+ __ZN7AVC_PPS8GenerateEiiiibP16_S_AVE_PSContext
+ __ZN7AVC_PPSC1EP26H264_PICTURE_HEADER_PARAMS
+ __ZN7AVC_SPS22seq_parameter_set_rbspEv
+ __ZN7AVC_SPSC1EP27H264_SEQUENCE_HEADER_PARAMS
+ __ZN7RQModel23qp2qscale_float_genericILi0EEEfj
+ __ZN7RQModel23qp2qscale_float_genericILi12EEEfj
+ __ZN8HEVC_PPS22pic_parameter_set_rbspEv
+ __ZN8HEVC_PTL14ptl_parametersEP16AVE_SyntaxWriterbj
+ __ZN8HEVC_VPS13vps_extensionEP15HEVC_VUI_PARAMS
+ __ZN8HEVC_VPS31video_header_parameter_set_rbspEP15HEVC_VUI_PARAMS
+ __ZN9AVC_Slice12slice_headerERK27H264_SEQUENCE_HEADER_PARAMSRK26H264_PICTURE_HEADER_PARAMSi
+ __ZN9AVC_Slice17pred_weight_tableEv
+ __ZN9AVC_Slice19dec_ref_pic_markingEv
+ __ZN9AVC_Slice23generateSliceHeaderInKFERK27H264_SEQUENCE_HEADER_PARAMSRK26H264_PICTURE_HEADER_PARAMS
+ __ZN9AVC_Slice25ref_pic_list_modificationEv
+ __ZNK11RateControl16applyAbrFeedbackEjf
+ __ZNK11RateControl17temporalQpScalingEfPK14LookAheadStats
+ __ZNK12MappedMemory10HwToTargetEm
+ __ZNK14CAVCController15SetLRMERCPerRefEv
+ __ZNK7AVC_SPS14vui_parametersEv
+ __ZTV16AVE_SyntaxWriter
+ _sqrt
- _AVE_History_Add
- _AVE_History_Create
- _AVE_History_Destroy
- _AVE_History_Print
- _RTK_DEV_TIMEBASE
- _RTK_timebase_get_time
- __Z12AVE_WritePTLPK23S_HEVC_ProfileTierLevelbiP16AVE_SyntaxWriter
- __Z14AVE_AVC_SetPPSPK21_S_AVE_Syntax_Cfg_AVCP10_S_AVC_PPS
- __Z14AVE_AVC_SetSPSPK21_S_AVE_Syntax_Cfg_AVCyP10_S_AVC_SPS
- __Z14AVE_IOP_Configv
- __Z15AVE_PSInfo_Make13_E_AVE_PSTypeiiP16_S_AVE_PSContext
- __Z16AVC_scaling_listPKhiiP16AVE_SyntaxWriter
- __Z16AVE_AVC_SetSlicePK23_S_AVE_Syntax_PFCfg_AVCP12_S_AVC_Slice
- __Z16AVE_Tunables_Set14_E_AVE_EncTypeb
- __Z17AVE_ApplyTunablesPK19_S_AVE_Tunables_Cfg
- __Z18AVE_Tunables_Resetv
- __Z19AVC_FindLevelLimits12_E_AVC_Level
- __Z20AVC_FindMaxMvsPer2Mb12_E_AVC_Level
- __Z20AVE_IOP_Config_pandav
- __Z20AVE_MCTFProfileFirstP24sCAvePerfProfileInternali16_E_AVE_MCTFStats
- __Z21AVE_EventProfileFirstP24sCAvePerfProfileInternalii14_E_AVE_FwStats
- __Z24AVC_FindMaxSubMbRectSize12_E_AVC_Level
- __Z26AVE_AVC_PrepareSliceHeaderPK10_S_AVC_PPSjiP13sCommonParamsP23_S_AVE_Syntax_PFCfg_AVC
- __Z26AVE_GenerateAVCHeaderStart18_E_AVC_NalUnitTypeP16AVE_SyntaxWriter
- __Z27AVE_GenerateHEVCHeaderStart19_E_HEVC_NalUnitTypehhP16AVE_SyntaxWriter
- __Z27AVE_HEVC_PrepareSliceHeaderPK11_S_HEVC_PPSjiibP13sCommonParamsP13_S_HEVC_Slice
- __Z29AVE_AVC_UpdatePOClsbSliceTypePK13sCommonParamsjiP23_S_AVE_Syntax_PFCfg_AVC
- __Z32AVE_HEVC_Update_POClsb_SliceTypePK13sCommonParamsjiP13_S_HEVC_Slice
- __ZN10CAVEClient22ResetSrcFrameRefCountsEv
- __ZN10HEVC_Slice12slice_headerEP16AVE_SyntaxWriterRK11_S_HEVC_SPSRK11_S_HEVC_PPSP8HEVC_RPS19_E_HEVC_NalUnitTypej
- __ZN10HEVC_Slice23generateSliceHeaderInKFERK11_S_HEVC_SPSRK11_S_HEVC_PPSP8HEVC_RPSPh
- __ZN11AVE_AVC_PPS4InitEyPK21_S_AVE_Syntax_Cfg_AVCP10_S_AVC_PPS
- __ZN11AVE_AVC_PPS8GenerateEPKsiiP16_S_AVE_PSContext
- __ZN11AVE_AVC_PPSC1Ev
- __ZN11AVE_AVC_PPSD1Ev
- __ZN11AVE_AVC_SPS4InitEyPK21_S_AVE_Syntax_Cfg_AVCP10_S_AVC_SPSy
- __ZN11AVE_AVC_SPS8GenerateEP16_S_AVE_PSContext
- __ZN11AVE_AVC_SPSC1Ev
- __ZN11AVE_AVC_SPSD1Ev
- __ZN11AVE_DevInfoD1Ev
- __ZN11RateControl13updateBitRateExj
- __ZN11RateControl14CreateInstanceERK21RateControlParametersP10FrameStatsiPv
- __ZN11RateControl15updateDRLParamsEjf
- __ZN11RateControl17updateRateControlExiiPi
- __ZN11RateControl18insertCBRFillerAVCEP17_S_AVE_FillerInfo13_E_AVE_RCModei
- __ZN11RateControl18processRateControlExii
- __ZN11RateControl19insertCBRFillerHEVCEP17_S_AVE_FillerInfo13_E_AVE_RCModeiii
- __ZN11RateControl21RestoreRCSegmentCtxLAERK22_S_AVE_RC_SegmentCtxLAx
- __ZN11RateControl22GenerateRCSegmentCtxLAEx
- __ZN11RateControl23updateBitsFromTranscodeExxiPi
- __ZN11RateControl24updateConstantRateFactorEd
- __ZN11RateControl27updateHRDUsingTranscodeBitsExiPi
- __ZN11RateControl31updateModeDistributionForZeroLAExiii
- __ZN11RateControlC2ERK21RateControlParametersP10FrameStatsiPv
- __ZN12CAvePipeMcpu9StartUnitEii
- __ZN12CRateControl10AccumulateEa9SliceTypejjP16sCRCStatPerFramehS0_
- __ZN12CRateControl11RateControlEa9SliceTypejjbjbbbjiS0_bb
- __ZN12CRateControl16computeCorrCoeffEPKjjj
- __ZN12CRateControl17ProcessAccumulateEa9SliceTypejjP16sCRCStatPerFramehS0_
- __ZN12CRateControl18ProcessRateControlEa9SliceTypejjbjbbbjiS0_b
- __ZN12CRateControl19RestoreRCSegmentCtxERK20_S_AVE_RC_SegmentCtx
- __ZN12CRateControl20AVE_CBR_InsertFillerEjjPK13_S_HEVC_Slice13_E_AVE_RCModeP17_S_AVE_FillerInfo
- __ZN12CRateControl20GenerateRCSegmentCtxEjj
- __ZN13AVE_AVC_Slice4InitEyPK23_S_AVE_Syntax_PFCfg_AVCP12_S_AVC_Slice
- __ZN13AVE_AVC_Slice8GenerateEPK10_S_AVC_SPSPK10_S_AVC_PPSPhiPi
- __ZN13AVE_AVC_SliceC1Ev
- __ZN13AVE_AVC_SliceD1Ev
- __ZN13CAVECommonDPB22ProvideReferenceFramesEjP14_S_AVE_Buf_Setj
- __ZN13COFControllerC1EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
- __ZN13COFControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
- __ZN14CAVCController12SetTranscodeEP26CAVEControllerAvcEncodeCmd
- __ZN14CAVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMSPK12_S_AVC_Slice
- __ZN14CAVCController19GetSliceHeaderForFWEPK12_S_AVC_SliceyiPhPji
- __ZN14CAVCController20SetLRMERCPerSrcFrameEPK26CAVEControllerAvcEncodeCmd
- __ZN14CAVCController26UpdateStaticAreaCbp0CountsEP14CODED_DATA_HDR9SliceTypej
- __ZN14CAVCController28ProcessDataFromCpusMultiCoreE9SliceType
- __ZN14CAVCController32PipeProcessStandaloneRateControlEP18AVE_PICMGMT_PARAMSP23_S_AVE_Syntax_PFCfg_AVC
- __ZN14CAVCController7setPipeEP26CAVEControllerAvcEncodeCmd
- __ZN14CAVCController9SetLRMERCEPK26CAVEControllerAvcEncodeCmd
- __ZN14CAVCControllerC1EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
- __ZN14CAVCControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
- __ZN14CAVEFilterBaseC2EPKcP7CObjectyibmm
- __ZN14CDMVController20SetDefaultParametersEv
- __ZN14CDMVControllerC1EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
- __ZN14CDMVControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
- __ZN15CFlowController20McpuControllerCreateEPKcyi
- __ZN15CFlowController20PipeISRManagerCreateEPKcyiPPVm
- __ZN15CHEVCController10SetRpsVarsEjP25HEVC_SLICE_SHORT_TERM_RPSP24HEVC_SLICE_LONG_TERM_RPSPK22HEVC_SPS_LONG_TERM_RPSjh
- __ZN15CHEVCController14ConfigureMCPUsEPK18AVE_PICMGMT_PARAMS
- __ZN15CHEVCController20StaticAreaInterApplyEPK18AVE_PICMGMT_PARAMSPjjj
- __ZN15CHEVCController26GenerateScalingListDataPPSEP11_S_HEVC_PPS
- __ZN15CHEVCController32PipeProcessStandaloneRateControlEP18AVE_PICMGMT_PARAMSP13_S_HEVC_Slice
- __ZN15CHEVCController8calc_rpsEhiP23HEVC_SPS_SHORT_TERM_RPSP19HEVC_SHORT_TERM_RPSPK22HEVC_SPS_LONG_TERM_RPSP24HEVC_SLICE_LONG_TERM_RPSj
- __ZN15CHEVCControllerC1EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
- __ZN15CHEVCControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
- __ZN16AVE_SyntaxWriter16AlignToByteWith1Ev
- __ZN16AVE_SyntaxWriter4InitEyPhib
- __ZN18CAVEPipeISRManagerC1EPKcP7CObjectyibPPVmP14AVE_PIODMACtrl
- __ZN18CAVEPipeISRManagerC2EPKcP7CObjectyibPPVmP14AVE_PIODMACtrl
- __ZN19CFlowControllerBase10FSMEncPipeE
- __ZN19CFlowControllerBase10FSMStfPipeE
- __ZN19CFlowControllerBase16DoneEventEncPipeEPv
- __ZN19CFlowControllerBase16DoneEventStfPipeEPv
- __ZN19CFlowControllerBase17StartEventEncPipeEPv
- __ZN19CFlowControllerBase17StartEventEncPipeEv
- __ZN19CFlowControllerBase17StartEventStfPipeEPv
- __ZN19CFlowControllerBase17StartEventStfPipeEv
- __ZN19CFlowControllerBase20GetStatsEventEncPipeEPv
- __ZN19CFlowControllerBase20GetStatsEventStfPipeEPv
- __ZN19CFlowControllerBase20SrcFrameForceReleaseEP10CAVEClient
- __ZN19CFlowControllerBase25SrcFrameDecrementRefCountEP10CAVEClientj
- __ZN19CFlowControllerBase26HandleCmdQueueForFrameDropEPK15sCmdInformationi
- __ZN20CAVECommonController11initWeightsEP17_S_VC_WtPred_Infoii
- __ZN20CAVECommonController14PrintDbgCyclesEv
- __ZN20CAVECommonController14computeWeightsEjjPjjP17_S_VC_WtPred_Infojj9SliceType
- __ZN20CAVECommonController15PrintLRMERCCRCsEjjb
- __ZN20CAVECommonController16InitRCParametersEP18_S_AVE_Session_CfgP21RateControlParameters
- __ZN20CAVECommonController16getDRLMaxBitRateEP14_S_AVE_DRL_Cfg
- __ZN20CAVECommonController17CreateRateControlEP18_S_AVE_Session_Cfg
- __ZN20CAVECommonController17GetThroughputModeE17_E_AVE_FrameStage
- __ZN20CAVECommonController18finalizeWeightsSEsEP13_S_HEVC_Slicej
- __ZN20CAVECommonControllerC2EPKcP7CObjectyPvijbP14AVE_PIODMACtrl
- __ZN20CPlatformEnvironmentD2Ev
- __ZN21ConstantQpRateControl18processRateControlExii
- __ZN22CAVEPipeISRManagerBaseC2EPKcP7CObjectyib
- __ZN22CAVEPipeMcpuController12StartAvePipeEiijPv
- __ZN22CAVEPipeMcpuController5StartEiijPv
- __ZN22CAVEPipeMcpuControllerC1EPKcP7CObjectyib
- __ZN25ConstantRateFactorRQModel12updateParamsEd
- __ZN26CAVEPipeMcpuControllerBaseC2EPKcP7CObjectyib
- __ZN3HRD15updateHrdStatusExPK11_S_AVE_TimefRiS3_f
- __ZN3HRD4initEbiPK11_S_AVE_Timeiff
- __ZN3HRD5printEPKc
- __ZN5AveRC23qp2qscale_float_genericEii
- __ZN5AveRC23qscale2qp_float_genericEfi
- __ZN7AVC_PPS28Write_pic_parameter_set_rbspEP16AVE_SyntaxWriteriii
- __ZN7AVC_PPS4InitEyPK10_S_AVC_PPS
- __ZN7AVC_PPS8GenerateEPKsiiP16_S_AVE_PSContext
- __ZN7AVC_PPS8GenerateEiiiP16_S_AVE_PSContext
- __ZN7AVC_PPSC1Ev
- __ZN7AVC_PPSD1Ev
- __ZN7AVC_SPS28Write_seq_parameter_set_rbspEP16AVE_SyntaxWriter
- __ZN7AVC_SPS4InitEyPK10_S_AVC_SPS
- __ZN7AVC_SPSC1Ev
- __ZN7AVC_SPSD1Ev
- __ZN7RQModel23qp2qscale_float_genericILi0EEEfi
- __ZN7RQModel23qp2qscale_float_genericILi12EEEfi
- __ZN8HEVC_PPS28Write_pic_parameter_set_rbspEv
- __ZN8HEVC_VPS13vps_extensionEv
- __ZN8HEVC_VPS24video_parameter_set_rbspEv
- __ZN8HEVC_VPS39vps_encode_independent_layer_parametersEPhS0_
- __ZN8HEVC_VPS7vps_vuiEv
- __ZN8HEVC_VPS8GenerateEiP16_S_AVE_PSContext
- __ZN8HEVC_VPSC1EP11_S_HEVC_VPSPK10S_HEVC_VUI
- __ZN9AVC_Slice18Write_slice_headerEPK10_S_AVC_SPSPK10_S_AVC_PPSiP16AVE_SyntaxWriter
- __ZN9AVC_Slice25Write_dec_ref_pic_markingEP16AVE_SyntaxWriter
- __ZN9AVC_Slice31Write_ref_pic_list_modificationEP16AVE_SyntaxWriter
- __ZN9AVC_Slice4InitEyPK12_S_AVC_Slice
- __ZN9AVC_Slice8GenerateEPK10_S_AVC_SPSPK10_S_AVC_PPSPhiPi
- __ZN9AVC_SliceC1Ev
- __ZN9AVC_SliceD1Ev
- __ZNK11AVE_DevInfo15GetDevSubIDFlagEv
- __ZNK11AVE_DevInfo17GetDevNumPerGroupEv
- __ZNK11AVE_DevInfo8GetDevIDEv
- __ZNK11AVE_DevInfo8GetSVEIDEv
- __ZNK11AVE_DevInfo9GetDevNumEv
- __ZNK11RateControl16applyAbrFeedbackExf
- __ZNK14CAVCController15SetLRMERCPerRefEPK17_S_VC_WtPred_Info
- __ZNK19CFlowControllerBase12GetPicParamsEPK15sCmdInformation
- __ZNK7AVC_SPS20Write_vui_parametersEP16AVE_SyntaxWriter
- __ZNK9AVC_Slice23Write_pred_weight_tableE12_E_ChromaFmtP16AVE_SyntaxWriter
- __rtk_ior
- _exp2f
- _gc_psaAVC_ScalingList
- _gc_sAVE_DevCap_DPMMap_AV1_Boreas
- _powf
CStrings:
+ "       (%d xx) C roi_marker: 0x%x, pipborder: 0x%x"
+ "       (%d xx) L roi_marker: 0x%x pipborder: 0x%x, iBoxWidth: %d"
+ "       (%d xx) R roi_marker: 0x%x, pipborder: 0x%x"
+ "!r"
+ "%s Enter %p %d %d %d %p"
+ "%s Exit %p %d %d %d %p %d"
+ "%s:%d %s | PS data overflows %p %d %d %d %p | %d %d %d %ld"
+ "%s:%d %s | not padded to bytes %p %d %d %d %p"
+ "%s:%d %s | wrong parameters %p %p"
+ "%s:%d Enter %d"
+ "%s:%d Exit %d"
+ "%s:%d Possible wrong encode of VPS"
+ "%s:%d [RC Check] %p %d %p %p %d %d %d %d %d"
+ "%s::%s ENTER %d"
+ "%s::%s Enter %d %d %d %d %p"
+ "%s::%s Enter %d %d %p %d %d %d"
+ "%s::%s Exit %d %d %d %d %p"
+ "%s::%s Exit %d %d %d %d %p %d"
+ "%s::%s Exit %d %d %p %d %d %d"
+ "%s::%s Exit %p %d %p %d %d %lld %lld"
+ "%s::%s client_id %lld, cmd %p, mctf %d\n"
+ "%s::%s exit %d"
+ "%s::%s: %d-%d-%d, %d-%d, %d-%d-%d, %d-%d-%d, %d"
+ "%s::%s:%d %s HRD status: max_bitrate %d cpb_size %d, init_cpb_delay %d, t_af %d, t_c %d, t_scale %d, 1st_dts %lld"
+ "%s::%s:%d %s | m_psParams->header_len(%d) %p"
+ "%s::%s:%d BITBOX (%d %d) Frame[%d] %d %d %d | %d %d %d %d | %d.%03d | inter %d intra %d | %d %d %d %d %d.%03d | LRvar %d.%03d"
+ "%s::%s:%d BITBOX (%d %d) HRD fullness %d underflow %d overflow %d filler %d bitsFromTranscode %d"
+ "%s::%s:%d BITBOX (%d %d) cavlcBits %d transcodeBits %d estTranscodeBits %d"
+ "%s::%s:%d BITBOX (%d %d) cavlcBits %d transcodeBits %d estTranscodeBits %d modelParam %d"
+ "%s::%s:%d BITBOX (%d %d) minQP %d maxQP %d"
+ "%s::%s:%d BITBOX (%d %d) qscale %d.%03d qp %d"
+ "%s::%s:%d BITBOX (%d %d) type %d ABR %d.%03d -> %d.%03d"
+ "%s::%s:%d BITBOX (%d %d) type %d M %d numP %d"
+ "%s::%s:%d BITBOX (%d %d) type %d SliceType/Temporal Scaling %d.%03d -> %d.%03d"
+ "%s::%s:%d BITBOX (%d %d) type %d VbvPlanning %d.%03d -> %d.%03d"
+ "%s::%s:%d BITBOX (%d %d) type %d bits %d cplxFilter %d blur %d"
+ "%s::%s:%d BITBOX (%d %d) type %d bits %d cplxFilter %d sum %d snapshotlen %d"
+ "%s::%s:%d BITBOX (%d %d) type %d cqscale %d.%03d, qscale %d.%03d"
+ "%s::%s:%d BITBOX (%d %d) type %d getQScale %d.%03d"
+ "%s::%s:%d BITBOX LrmeVarToVar (%d, %d) frameSumOfVar: %d, lowResVar: %d"
+ "%s::%s:%d BITBOX SegmentEncoding VBV (%d %d) startLoop %d EndLoop %d curLoop %d"
+ "%s::%s:%d BITBOX estimateBits (%d, %d) transcode: %d, estTranscode: %d, estBitsfromRC: %d"
+ "%s::%s:%d BITBOX iIsFirstFrame %d SegmentEncoding Enabled %d totalFrames %d"
+ "%s::%s:%d Client %llu Mode %d %d %d %d"
+ "%s::%s:%d ENC: StartCount %d-%d-%d-%d, Idle %d-%d-%d-%d"
+ "%s::%s:%d EncCommParams.uiPSHeaderBitsCount %d"
+ "%s::%s:%d Enc_Client IDs %lld-%lld-%lld-%lld CTX %d-%d-%d-%d"
+ "%s::%s:%d Enc_Client IDs %lld-%lld-%lld-%lld-%lld CTX %d-%d-%d-%d"
+ "%s::%s:%d F %d BITBOX QPMod qp %d hrdfullness %d.%03d Str %d.%03d range [%d.%03d, %d.%03d]\n"
+ "%s::%s:%d F(%d, %d) Unexpected TimeScale changed from %d to %d"
+ "%s::%s:%d Frame %d PIP CTU (%dx%d) rect(%d, %d, %d, %d)"
+ "%s::%s:%d HRD Init iscbr %d %d %d %d, %d"
+ "%s::%s:%d HRD planning status: (%d %d) type %d HrdFullness Start %d.%03d End %d.%03d Min %d.%03d loop %d"
+ "%s::%s:%d MVHEVC (%d %d) pFrame.bitsFromCAVLC %d pFrame.estimatedTranscodeBits %d"
+ "%s::%s:%d NULL video context!!! %p"
+ "%s::%s:%d PIP Partial Flag %d %d %d %d"
+ "%s::%s:%d PIP ctu (%d %d)"
+ "%s::%s:%d PIP ctu (%d %d) roi_marker 0x%x, iPIPBorder 0x%x"
+ "%s::%s:%d PipeDone currCtuRow %d curr_slice_number %d"
+ "%s::%s:%d StartCount %d-%d-%d-%d, HW %d-%d-%d-%d"
+ "%s::%s:%d Wrong parameter %d %d %d %p"
+ "%s::%s:%d [ABR] Frame %d totalBits %d targetBits %d overflow %d"
+ "%s::%s:%d clientID %llu pps headerNum %d header_len %d bits %d bytes i %d PPS ID %d PPS count %d"
+ "%s::%s:%d clientID %llu pps headerNum %d header_len %d bits %d bytes i %d PPS ID %d numView %d"
+ "%s::%s:%d currEncCmd %p pCmd %p %d %lld %d"
+ "%s::%s:%d failed to allocate memory"
+ "%s::%s:%d failed to generate PPS %d %d %d %d %p %d %d %d"
+ "%s::%s:%d get NOTIFICATION_GET_PIPE_CONTINUE signal, for client %lld"
+ "%s::%s:%d get NOTIFICATION_GET_PIPE_STATS_DONE signal, for client %lld"
+ "%s::%s:%d insert a new slice @ %d for restart"
+ "%s::%s:%d invalid sps and pps bFWCreatesHeader %d %d"
+ "%s::%s:%d invalid sps and pps bFWCreatesHeader %d %d %d"
+ "%s::%s:%d lrmddone currCtuRow %d curr_slice_number %d"
+ "%s::%s:%d lrme_ready %d, client_id = %lld, Idle %d-%d-%d\n"
+ "%s::%s:%d numOfFrame %d bits %d 1stdts %lld iTimescale %d iValue %lld hrd_t_c %d t_c %d"
+ "%s::%s:%d restart frame contextID %d encode_row_init %d context_height_in_mb %d picHeightInMb %d"
+ "%s::%s:%d uiPSHeaderBitsCount %d"
+ "%s::%s:%d xcode Done currCtuRow %d curr_slice_number %d"
+ "%s::%s:%d | failed to generate SPS %d"
+ "%s::%s:%d | failed to generate VUI %d"
+ "%s::%s:%d | failed to set RBSP %d"
+ "%s::%s:%d: m_psParams->header_len %d (bytes %d)"
+ "( sps.sps_max_sub_layers_minus1 != 0 ) || ( sps.sps_max_sub_layers_minus1 == 0 && sps.sps_temporal_id_nesting_flag == true )"
+ "((pPicParams->sLowResOutput.LowResResults + i*iLowResResultsDMASize) & 63) == 0"
+ "((pPicParams->sLowResOutput.LowResResults + ii*iLowResResultsDMASize) & 63) == 0"
+ "((pPicParams->sLowResOutput.LowResSrcLumaScaled + ((m_psEncCommParams->encode_row_init/4) * LRME_LOWRES_REF_LUMA_TILED_STRIDE(m_psSequenceInits.uWidthInMbs))) & 63) == 0"
+ "((pPicParams->sLowResOutput.LowResSrcLumaScaled + (EncCommParams.encode_row_init/4) * HEVCVIDEOENCODER_LOWRES_REF_LUMA_TILED_STRIDE(EncCommParams.width)) & 63) == 0"
+ "((pPicParams->sLowResOutput.LowResSrcLumaScaled + EncCommParams.encode_row_init/4*lr_stride) & 63) == 0"
+ "((pPicParams->sRef.Colocated_L1[0] + coloDataContextOffset + multiCoreOffset) & 63) == 0"
+ "((pPicParams->sRef.Colocated_L1[0] + coloDataContextOffset - 20 * sizeof(aveCommon_AVECoLoData_t)) & 63) == 0"
+ "(pPicParams->sLowResOutput.LowResResults & 63) == 0"
+ "(pPicParams->sLowResOutput.LowResSrcLumaScaled + (EncCommParams.encode_row_init/4) * HEVCVIDEOENCODER_LOWRES_REF_LUMA_TILED_STRIDE(EncCommParams.width)) != 0"
+ "(pPicParams->sLowResOutput.LowResSrcLumaScaled + EncCommParams.encode_row_init/4*lr_stride) != 0"
+ "(pPicParams->sRecon.UV_LSB & 127) == 0"
+ "(pPicParams->sRecon.UV_MSB & 127) == 0"
+ "(pPicParams->sRecon.Y_LSB & 127) == 0"
+ "(pPicParams->sRecon.Y_MSB & 127) == 0"
+ "(pPicParams->sRef.Colocated_L1[0] + coloDataContextOffset + multiCoreOffset) != 0"
+ "(pPicParams->sRef.Colocated_L1[0] + coloDataContextOffset - 20 * sizeof(aveCommon_AVECoLoData_t)) != 0"
+ "(pPicParams->sRef.Low_Res_Y_L0[me_ref_index] & 63) == 0"
+ "(pPicParams->sRef.Low_Res_Y_L1[l1_me_ref_index] & 63) == 0"
+ "(pPicParams->sRef.Y_L0_LSB[me_ref_index] & 63) == 0"
+ "(pPicParams->sRef.Y_L0_MSB[me_ref_index] & 63) == 0"
+ "(pPicParams->sRef.Y_L1_LSB[l1_me_ref_index] & 63) == 0"
+ "(pPicParams->sRef.Y_L1_MSB[l1_me_ref_index] & 63) == 0"
+ "----CropParams----\n"
+ "----PPS----\n"
+ "----SPS----\n"
+ "----VUI----\n"
+ "./AppleAVE2FW/Common/Utils/H264_headers.cpp"
+ "./AppleAVE2FW/External/Algorithm/RateControl.cpp"
+ "./AppleAVE2FW/Firmware/HeartBeat/AVE_PP.cpp"
+ "./AppleAVE2FW/Firmware/HeartBeat/CControllerHeartBeat.cpp"
+ "9003.78.0"
+ "AVE ERROR: AVE_H264_PrepareSliceHeader pEncParams == NULL"
+ "AVE ERROR: AVE_H264_Update_POClsb_SliceType frametype not recognized"
+ "AVE ERROR: AVE_HEVC_PrepareSliceHeader pEncParams == NULL"
+ "AVE ERROR: AVE_HEVC_Update_POClsb_SliceType frametype not recognized"
+ "AVE ERROR: prepareSliceHeaderForFW frametype not recognized"
+ "AVE ERROR: prepareSliceHeaderForFW with pps = NULL "
+ "AVE ERROR: prepareSliceHeaderForFW with slice_header = NULL "
+ "AVE Error: SliceCnt exceed %d [%d, %d]"
+ "AVEController"
+ "BITBOX (%d %d) totalBits %d, estTrancodeBits %d\n"
+ "CFSM::Get(fsmPipe) == GETTINGPIPESTATS"
+ "Caller is /AppleInternal/Library/BuildRoots/4~CQ4sugBz3X4wb5H3P_E4toyOHctbluAsSdF9cKg/Library/Caches/com.apple.xbs/TemporaryDirectory.NFhvjf/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:751"
+ "Caller is /AppleInternal/Library/BuildRoots/4~CQ4sugBz3X4wb5H3P_E4toyOHctbluAsSdF9cKg/Library/Caches/com.apple.xbs/TemporaryDirectory.NFhvjf/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:756"
+ "Client:%llu %llu %llu %llu AXI Error: 0x%x 0x%x 0x%x 0x%x\n"
+ "CropParams.frame_crop_bottom_offset %d\n"
+ "CropParams.frame_crop_left_offset %d\n"
+ "CropParams.frame_crop_right_offset %d\n"
+ "CropParams.frame_crop_top_offset %d\n"
+ "CropParams.frame_cropping_flag %d\n"
+ "DoneEventPipe"
+ "FSMPIPE"
+ "GetStatsEventPipe"
+ "HEVC COMMON:: pPicParams->sLowResOutput.LowResResults[%d]:%016llx\n"
+ "HEVC COMMON:: slice->num_ref_idx_l0_active_minus1 %d slice->num_ref_idx_l1_active_minus1 %d\n"
+ "MaxMvsPer2Mb: %d"
+ "MaxSubMbRectSize: %d"
+ "PPS %d: m_psParams->header_len %d (bytes %d). Prev PPSs header_len %d (bytes %d)"
+ "PPS header length:%d\n"
+ "PPSParams.bFWCreatesHeader %d"
+ "PPSParams.bottom_field_pic_order_in_frame_present_flag %d\n"
+ "PPSParams.chroma_qp_index_offset[%d] %d\n"
+ "PPSParams.constrained_intra_pred_flag %d\n"
+ "PPSParams.deblocking_filter_control_present_flag %d\n"
+ "PPSParams.entropy_coding_mode_flag %d\n"
+ "PPSParams.header_len %d"
+ "PPSParams.num_ref_idx_l0_default_active_minus1 %d\n"
+ "PPSParams.num_ref_idx_l1_default_active_minus1 %d\n"
+ "PPSParams.num_slice_groups_minus1 %d\n"
+ "PPSParams.pic_init_qp_minus26 %d\n"
+ "PPSParams.pic_init_qs_minus26 %d\n"
+ "PPSParams.pic_parameter_set_id %d\n"
+ "PPSParams.pic_scaling_matrix_present_flag %d\n"
+ "PPSParams.redundant_pic_cnt_present_flag %d\n"
+ "PPSParams.second_chroma_qp_index_offset[%d] %d\n"
+ "PPSParams.seq_parameter_set_id %d\n"
+ "PPSParams.transform_8x8_mode_flag %d\n"
+ "PPSParams.weighted_bipred_idc %d\n"
+ "PPSParams.weighted_pred_flag %d\n"
+ "RC params: %d %d %d %d %d 0x%llx"
+ "RC params:%d %d %d %d %d %d %d %d %d %d %d %d"
+ "ROI[%d]: [%d, %d], [%d, %d]"
+ "RTK_platform_init"
+ "SPS header length:%d\n"
+ "SPSparams.VUI.aspect_ratio_idc %d"
+ "SPSparams.VUI.aspect_ratio_info_present_flag %d"
+ "SPSparams.VUI.aspect_ratio_info_present_flag %d\n"
+ "SPSparams.VUI.bitstream_restriction_flag %d"
+ "SPSparams.VUI.bitstream_restriction_flag %d\n"
+ "SPSparams.VUI.chroma_loc_info_present_flag %d"
+ "SPSparams.VUI.chroma_sample_loc_type_bottom_field %d"
+ "SPSparams.VUI.chroma_sample_loc_type_top_field %d"
+ "SPSparams.VUI.colour_description_present_flag %d"
+ "SPSparams.VUI.colour_description_present_flag %d\n"
+ "SPSparams.VUI.colour_primaries %d"
+ "SPSparams.VUI.colour_primaries %d\n"
+ "SPSparams.VUI.default_display_window.def_disp_win_bottom_offset %d"
+ "SPSparams.VUI.default_display_window.def_disp_win_left_offset %d"
+ "SPSparams.VUI.default_display_window.def_disp_win_right_offset %d"
+ "SPSparams.VUI.default_display_window.def_disp_win_top_offset %d"
+ "SPSparams.VUI.default_display_window_flag %d"
+ "SPSparams.VUI.field_seq_flagg %d"
+ "SPSparams.VUI.fixed_frame_rate_flag %d\n"
+ "SPSparams.VUI.frame_field_info_present_flag %d"
+ "SPSparams.VUI.log2_max_mv_length_horizontal %d"
+ "SPSparams.VUI.log2_max_mv_length_vertical %d"
+ "SPSparams.VUI.matrix_coefficients %d\n"
+ "SPSparams.VUI.matrix_coeffs %d"
+ "SPSparams.VUI.max_bits_per_min_cu_denom %d"
+ "SPSparams.VUI.max_bytes_per_pic_denom %d"
+ "SPSparams.VUI.min_spatial_segmentation_idc %d"
+ "SPSparams.VUI.motion_vectors_over_pic_boundaries_flag %d"
+ "SPSparams.VUI.nal_hrd_parameters_present_flag %d\n"
+ "SPSparams.VUI.neutral_chroma_indication_flag %d"
+ "SPSparams.VUI.num_units_in_tick %d\n"
+ "SPSparams.VUI.overscan_info_present_flag %d"
+ "SPSparams.VUI.overscan_info_present_flag %d\n"
+ "SPSparams.VUI.pic_struct_present_flag %d\n"
+ "SPSparams.VUI.restricted_ref_pic_lists_flag %d"
+ "SPSparams.VUI.sar_height %d"
+ "SPSparams.VUI.sar_width %d"
+ "SPSparams.VUI.tiles_fixed_structure_flag %d"
+ "SPSparams.VUI.time_scale %d\n"
+ "SPSparams.VUI.timing_info_present_flag %d\n"
+ "SPSparams.VUI.transfer_characteristics %d"
+ "SPSparams.VUI.transfer_characteristics %d\n"
+ "SPSparams.VUI.vcl_hrd_parameters_present_flag %d\n"
+ "SPSparams.VUI.video_format %d"
+ "SPSparams.VUI.video_format %d\n"
+ "SPSparams.VUI.video_full_range_flag %d"
+ "SPSparams.VUI.video_full_range_flag %d\n"
+ "SPSparams.VUI.video_signal_type_present_flag %d"
+ "SPSparams.VUI.video_signal_type_present_flag %d\n"
+ "SPSparams.VUI.vui_parameters_present_flag %d"
+ "SPSparams.VUI.vui_parameters_present_flag %d\n"
+ "SPSparams.VUI.vui_timing_info_present_flag %d"
+ "SPSparams.bFWCreatesHeader %d"
+ "SPSparams.bit_depth_chroma_minus8 %d\n"
+ "SPSparams.bit_depth_luma_minus8 %d\n"
+ "SPSparams.chroma_format_idc %d\n"
+ "SPSparams.constraint_set0_flag %d\n"
+ "SPSparams.constraint_set1_flag %d\n"
+ "SPSparams.constraint_set2_flag %d\n"
+ "SPSparams.constraint_set3_flag %d\n"
+ "SPSparams.constraint_set4_flag %d\n"
+ "SPSparams.constraint_set5_flag %d\n"
+ "SPSparams.direct_8x8_inference_flag %d\n"
+ "SPSparams.eLevel %d\n"
+ "SPSparams.eProfile %d\n"
+ "SPSparams.frame_mbs_only_flag %d\n"
+ "SPSparams.gaps_in_frame_num_value_allowed_flag %d\n"
+ "SPSparams.header_len %d"
+ "SPSparams.log2_max_frame_num_minus4 %d\n"
+ "SPSparams.log2_max_pic_order_cnt_lsb_minus4 %d\n"
+ "SPSparams.max_num_ref_frames %d\n"
+ "SPSparams.pic_height_in_map_units_minus1 %d\n"
+ "SPSparams.pic_order_cnt_type %d\n"
+ "SPSparams.pic_width_in_mbs_minus1 %d\n"
+ "SPSparams.qpprime_y_zero_transform_bypass_flag %d\n"
+ "SPSparams.scaling_matrix %d\n"
+ "SPSparams.separate_colour_plane_flag %d\n"
+ "SPSparams.seq_parameter_set_id %d\n"
+ "SPSparams.seq_scaling_list_present_flag[%d] %d\n"
+ "SPSparams.seq_scaling_matrix_present_flag %d\n"
+ "SetTunable"
+ "StartEventPipe"
+ "cid:%lld fid:%d core_idx:%d fnum:%d dfnum:%d qp:%d\n"
+ "currCtuRow < AVE_SLICE_MAX_NUM"
+ "fps %d.%03d totalFrames %d"
+ "frame->cplxFiltered > 0"
+ "frm->cplxFiltered > 0"
+ "fsmPipe != 0"
+ "hClientQueue.GetIDFromIndex(ch) == tmpPIPECmd->client_id"
+ "hClientQueue.client(ch) != NULL"
+ "hevc_pps->scaling_list_data.scaling_list_dc_coef_minus8[sizeId - 2][matrixId] >= -7 && hevc_pps->scaling_list_data.scaling_list_dc_coef_minus8[sizeId - 2][matrixId] <= 247"
+ "hrd_time_scale == dts->iTimescale"
+ "iSliceIdx<AVE_SLICE_ACTIVE_MAX_NUM"
+ "m_psParams->header_len == 0"
+ "max_num_ref_frames: %d"
+ "mismatch cid:%lld fid:%d core_idx:%d fnum:%d dfnum:%d qp:%d\n"
+ "mode_8x8_transform: %d"
+ "nextCoef == ExplicitVideoScalingList8x8[mode][cmp][0]"
+ "pFrame->snapshotLen"
+ "pInPicParams.sExtraBuff.SrcNbrData %016llx\n"
+ "pInPicParams.sExtraBuff.SrcNbrInfo %016llx\n"
+ "pInPicParams.sExtraBuff.SrcNbrPixels %016llx\n"
+ "pInPicParams.sOutput.Coded %08x\n"
+ "pInPicParams.sOutput.coded_dataHeader[%d] %08x\n"
+ "pInPicParams.sRecon.UV_MSB %016llx\n"
+ "pInPicParams.sRecon.Y_MSB %016llx\n"
+ "pInPicParams.sRef.Colocated_L1 %016llx\n"
+ "pInPicParams.sRef.UV_L0_MSB[0] %016llx\n"
+ "pInPicParams.sRef.UV_L0_MSB[1] %016llx\n"
+ "pInPicParams.sRef.UV_L0_MSB[2] %016llx\n"
+ "pInPicParams.sRef.UV_L0_MSB[3] %016llx\n"
+ "pInPicParams.sRef.UV_L1_MSB[0] %016llx\n"
+ "pInPicParams.sRef.UV_L1_MSB[1] %016llx\n"
+ "pInPicParams.sRef.UV_L1_MSB[2] %016llx\n"
+ "pInPicParams.sRef.UV_L1_MSB[3] %016llx\n"
+ "pInPicParams.sRef.Y_L0_MSB[0] %016llx\n"
+ "pInPicParams.sRef.Y_L0_MSB[1] %016llx\n"
+ "pInPicParams.sRef.Y_L0_MSB[2] %016llx\n"
+ "pInPicParams.sRef.Y_L0_MSB[3] %016llx\n"
+ "pInPicParams.sRef.Y_L1_MSB[0] %016llx\n"
+ "pInPicParams.sRef.Y_L1_MSB[1] %016llx\n"
+ "pInPicParams.sRef.Y_L1_MSB[2] %016llx\n"
+ "pInPicParams.sRef.Y_L1_MSB[3] %016llx\n"
+ "pInVideoParams->LowDelay %d"
+ "pInVideoParams->adaptB_poc_delay %d"
+ "pInVideoParams->bSliceEncodingMode %d, %d"
+ "pInVideoParams->low_res_pipe_sync_mode"
+ "pInVideoParams->sSliceMap.iNum>=1"
+ "pPicParams->sInput.sMultiPassStats.iAddr != 0"
+ "pPicParams->sLowResOutput.LowResResults != 0"
+ "pPicParams->sLowResOutput.LowResSrcLumaScaled + ((m_psEncCommParams->encode_row_init/4) * LRME_LOWRES_REF_LUMA_TILED_STRIDE(m_psSequenceInits.uWidthInMbs))"
+ "pPicParams->sOutput.Coded"
+ "pPicParams->sOutput.Coded == EncCommParams.bitstream_addr_dst[index]"
+ "pPicParams->sOutput.CodedBufSize > (minBufSize/2)"
+ "pPicParams->sRecon.UV_LSB != 0"
+ "pPicParams->sRecon.UV_MSB != 0"
+ "pPicParams->sRecon.Y_LSB != 0"
+ "pPicParams->sRecon.Y_MSB != 0"
+ "pPicParams->sRef.Low_Res_Y_L0[me_ref_index] != 0"
+ "pPicParams->sRef.Low_Res_Y_L1[l1_me_ref_index] != 0"
+ "pPicParams->sRef.Y_L0_LSB[me_ref_index] != 0"
+ "pPicParams->sRef.Y_L0_MSB[me_ref_index] != 0"
+ "pPicParams->sRef.Y_L1_LSB[l1_me_ref_index] != 0"
+ "pPicParams->sRef.Y_L1_MSB[l1_me_ref_index] != 0"
+ "pSessionCfg->sEnc.sAlgCfg.sGOP.iNumOfFrame[AVE_FrameType_B] %d"
+ "paddr < m_paddr + m_size"
+ "paddr >= m_paddr"
+ "phevc_rps.CurrRpsIdx %d"
+ "piPSData != __null && psPSContext != __null"
+ "pic_parameter_set_rbsp"
+ "pps.num_extra_slice_header_bits == 0"
+ "qcoeff_cancel: %d"
+ "restart transcode contextID %d bitstreamAddr %016llx, bytes_to_be_removed: %d\n"
+ "restart transcode frame_id %d bitstreamAddr %016llx, bytes_to_be_removed: %d\n"
+ "sBufSet.saRecon[%d][0].iAddr:%016llx\n"
+ "sExtraBuff.Cavlc[%d][%d]:%016llx\n"
+ "set buffers contextID %d index %d pPicParams->sOutput.Coded 0x%08llx EncCommParams.bitstream_addr_dst[index] %016llx\n"
+ "setPipeGo() slice_type= %d, bothMEInUse= %d\n"
+ "skip_mode: %d"
+ "slice_header"
+ "sps.VUI.vui_parameters_present_flag == true"
+ "stitch colo data encode_row_init %d\n"
+ "stitchColoData"
+ "vui_parameters"
+ "wrong entropy_coding_mode_flag\n"
- "%s Enter %d %d"
- "%s Enter %d %d %d %p"
- "%s Enter %p"
- "%s Enter %p %d %d %p"
- "%s Enter %p %p %d %d %d %d %p %p"
- "%s Exit %d %d"
- "%s Exit %d %d %d %p %d"
- "%s Exit %p %d"
- "%s Exit %p %d %d %p %d"
- "%s Exit %p %p %d %d %d %d %p %p %d"
- "%s on non Stf Hw"
- "%s:%d %d %d %d %d %d %d %d %d %p %p %d %d"
- "%s:%d %d %d %d %d %d %d %d %p %p %d"
- "%s:%d %d %d %d %d %d %p %p %d %d"
- "%s:%d %d %d %d %p %p %d %d %d"
- "%s:%d %d %d %d %p %p 0x%x"
- "%s:%d %p %d %d %p %d %d %d"
- "%s:%d %s | PS data overflows %d %d %d %p | %d %d %d %ld"
- "%s:%d %s | invalid level %d"
- "%s:%d %s | not padded to bytes %d %d %d %p"
- "%s:%d %s | wrong frame type  %p %p %d %d %d"
- "%s:%d %s | wrong frame type %p %d %d %p %d"
- "%s:%d %s | wrong parameter %p %p"
- "%s:%d %s | wrong parameter %p 0x%llx %p"
- "%s:%d %s | wrong parameters %p"
- "%s:%d %s | wrong parameters %p %d"
- "%s:%d %s | wrong parameters %p %p %p"
- "%s:%d %s | wrong scaling matrix mode %p %llu %d"
- "%s:%d %s | wrong slice type %d %p %d"
- "%s:%d %s | wrong tunables %p %d %d"
- "%s:%d PIP Partial Flag %d %d %d %d"
- "%s:%d Unexpected pipe mode mask. only one bit expected, Got: 0x%x\n"
- "%s:%d Unhandled pipe_mode, Mask: 0x%x\n"
- "%s:%d [RC Check] %p %d %p %p %d %lld %lld %d %d"
- "%s:%s Enter"
- "%s::%s %s decodeOrder=%lld c=%d filterIdx=%d unPredIdx=%d.%03d"
- "%s::%s Already initialized %p %llu"
- "%s::%s Enter %d %d %d %p"
- "%s::%s Enter %p %llu %d %d %d %p"
- "%s::%s Enter %p %llu %p"
- "%s::%s Enter %p %llu %p %d %d"
- "%s::%s Enter %p %llu %p %p %p %d %p"
- "%s::%s Enter %s %d %d %p %d %d %d"
- "%s::%s Exit %d %d %d %p"
- "%s::%s Exit %p %d %d %d"
- "%s::%s Exit %p %d %p %d %d %lld %lld %d"
- "%s::%s Exit %p %llu %d %d %d %p %d"
- "%s::%s Exit %p %llu %p %d"
- "%s::%s Exit %p %llu %p %d %d %d"
- "%s::%s Exit %p %p %d"
- "%s::%s Exit %p %p %p %d %p %d"
- "%s::%s Exit %s %d %d %p %d %d.%03d %d.%03d"
- "%s::%s InitEncodingParameters failed %d"
- "%s::%s client_id %lld, cmd %p\n"
- "%s::%s cplxFiltered %d.%03d m_rateFactor %d.%03d"
- "%s::%s decodeOrder=%d numIntra=%d numInter=%d numSkip=%d IntraSumSatd=%u, InterSumSatd=%u"
- "%s::%s: %d-%d-%d, %d-%d, %d-%d-%d, %d-%d, %d"
- "%s::%s: Enter, %d - %d"
- "%s::%s: Enter, %d - %d, %d, %d"
- "%s::%s: Enter, %d - %d, %d, %d %d %d %d %d %d"
- "%s::%s: Enter, %lld"
- "%s::%s: Exit"
- "%s::%s: Exit, %d - %d, %d, %d"
- "%s::%s: Exit, %d - %d, %d, %d %d %d %d %d %d"
- "%s::%s:%d %p %llu %p SPS bits %d (bytes %d)"
- "%s::%s:%d %p %llu abs diff pic num minus1 %d %d"
- "%s::%s:%d %p %llu adaptive ref pic marking mode flag %d"
- "%s::%s:%d %p %llu difference of pic nums minus1 %d"
- "%s::%s:%d %p %llu failed to generate PPS %d %d %d %p %d"
- "%s::%s:%d %p %llu failed to generate VUI %p %d"
- "%s::%s:%d %p %llu failed to set RBSP %p %d"
- "%s::%s:%d %p %llu failed to set RBSP %p %d %d %d %d"
- "%s::%s:%d %p %llu long term frame idx %d"
- "%s::%s:%d %p %llu long term pic num %d"
- "%s::%s:%d %p %llu long term pic num %d %d"
- "%s::%s:%d %p %llu long term reference flag %d"
- "%s::%s:%d %p %llu max long term frame idx plus1 %d"
- "%s::%s:%d %p %llu memory management control operation 0x%x"
- "%s::%s:%d %p %llu modification of pic nums idc %d %d"
- "%s::%s:%d %p %llu no output of prior pics flag %d"
- "%s::%s:%d %p %llu ref pic list reordering flag l0 %d"
- "%s::%s:%d %p %p %llu failed %d"
- "%s::%s:%d %p %p %llu failed to generate slice header %d"
- "%s::%s:%d %p F %d BITBOX QPMod qp %d hrdfullness %d.%03d Str %d.%03d range [%d.%03d, %d.%03d]"
- "%s::%s:%d %p MCTF LFSRef buffers num %d"
- "%s::%s:%d %p bits %d (bytes %d)"
- "%s::%s:%d %p get NOTIFICATION_GET_TRANSCODE_CONTINUE signal, for client %lld"
- "%s::%s:%d %p num_ref_idx_l0_active_minus1 %d num_ref_idx_l1_active_minus1 %d"
- "%s::%s:%d %p unsupported encoder type %d"
- "%s::%s:%d %p wrong entropy coding mode flag %d"
- "%s::%s:%d %s %s status: max_bitrate %d cpb_size %d.%06d, init_cpb_delay %d.%06d, t_af %d.%06d, t_c %d.%06d, t_scale %d, 1st_dts %lld"
- "%s::%s:%d %s Init iscbr %d %d %d %d %d.%03d %d.%03d, %d.%03d"
- "%s::%s:%d %s numOfFrame %lld bits %d 1stdts %lld iTimescale %d iValue %lld hrd_t_c %d.%06d t_c %d.%06d"
- "%s::%s:%d %s updated params: max_bitrate %d cpb_size %d.%03d"
- "%s::%s:%d %s | Failed to initialize DPB %d"
- "%s::%s:%d %s | Failed to initialize picture parameter set class %p %llu %p %p"
- "%s::%s:%d %s | Failed to initialize scaling list registers %d"
- "%s::%s:%d %s | Failed to initialize sequence parameter set class %p %llu %p %p"
- "%s::%s:%d %s | Failed to initialize slice header parameter set class %p %llu %p %p"
- "%s::%s:%d %s | Failed to set picture parameter set structure %p %llu %p %p"
- "%s::%s:%d %s | Failed to set sequence parameter set structure %p %llu %p 0x%llx %p"
- "%s::%s:%d %s | Failed to set slice header parameter set structure %p %llu %p %p"
- "%s::%s:%d %s | NULL video context!!! %p"
- "%s::%s:%d %s | No SPS or PPS %d"
- "%s::%s:%d %s | No enough memory for slice header! %p %d %d"
- "%s::%s:%d %s | No enough memory for slice header! %p %d %d %d"
- "%s::%s:%d %s | No slice header buffer! %p"
- "%s::%s:%d %s | No slice header buffer! %p %d"
- "%s::%s:%d %s | VUI pointer is null %p"
- "%s::%s:%d %s | fail to generate PPS %p %p %d %d %d %d %d"
- "%s::%s:%d %s | fail to generate PPS %p %p %d %d %p %d"
- "%s::%s:%d %s | fail to generate Slice %p %p %p %p %d %p %d"
- "%s::%s:%d %s | fail to initialize syntax writer %p %llu %p %d %d"
- "%s::%s:%d %s | fail to initialize syntax writer %p %p %d"
- "%s::%s:%d %s | fail to initialize syntax writer %p %p %p %d %d"
- "%s::%s:%d %s | failed to allocate memory"
- "%s::%s:%d %s | failed to allocate syntax writer %p %llu %p %p %d %d"
- "%s::%s:%d %s | failed to generate SPS %p %llu %p"
- "%s::%s:%d %s | failed to make PS info %p %llu %d %p %d"
- "%s::%s:%d %s | failed to write SPS RBSP %p %llu %p %p %d"
- "%s::%s:%d %s | num slice groups not supported %p %llu %d"
- "%s::%s:%d %s | offset for ref frame not supported %p %llu %d"
- "%s::%s:%d %s | scaling matrix mode not support %p %llu %d"
- "%s::%s:%d %s | too many PPS %p %d %d"
- "%s::%s:%d %s | wong num ref idx active override flag %p %llu %d %d %d %d %d %d %d"
- "%s::%s:%d %s | wrong parameter"
- "%s::%s:%d %s | wrong parameter %p"
- "%s::%s:%d %s | wrong parameter %p %llu"
- "%s::%s:%d %s | wrong parameter %p %llu %p"
- "%s::%s:%d %s | wrong parameters %p %llu %p %p"
- "%s::%s:%d %s | wrong parameters %p %llu %p %p %p %d %p"
- "%s::%s:%d %s | wrong scaling matrix mode %p %llu %d"
- "%s::%s:%d BITBOX (%lld %lld) Frame[%lld] %lld %d %d | %d %d %d %d | %d.%03d | inter %d intra %d | %lld %lld %lld %d %d.%03d | LRvar %d.%03d"
- "%s::%s:%d BITBOX (%lld %lld) HRD fullness %d underflow %d overflow %d bitsFromTranscode[%d] %lld"
- "%s::%s:%d BITBOX (%lld %lld) HRD fullness %d underflow %d overflow %d filler %d bitsFromTranscode %lld"
- "%s::%s:%d BITBOX (%lld %lld) cavlcBits %lld transcodeBits %lld estTranscodeBits %lld"
- "%s::%s:%d BITBOX (%lld %lld) cavlcBits %lld transcodeBits %lld estTranscodeBits %lld modelParam %d"
- "%s::%s:%d BITBOX (%lld %lld) minQP %d maxQP %d"
- "%s::%s:%d BITBOX (%lld %lld) qscale %d.%03d qp %d"
- "%s::%s:%d BITBOX (%lld %lld) type %d ABR %d.%03d -> %d.%03d"
- "%s::%s:%d BITBOX (%lld %lld) type %d M %d numP %d"
- "%s::%s:%d BITBOX (%lld %lld) type %d SliceType/Temporal Scaling %d.%03d -> %d.%03d"
- "%s::%s:%d BITBOX (%lld %lld) type %d VbvPlanning %d.%03d -> %d.%03d"
- "%s::%s:%d BITBOX (%lld %lld) type %d bits %d cplxFilter %d blur %d"
- "%s::%s:%d BITBOX (%lld %lld) type %d bits %d cplxFilter %d sum %d snapshotlen %d"
- "%s::%s:%d BITBOX (%lld %lld) type %d cqscale %d.%03d, qscale %d.%03d"
- "%s::%s:%d BITBOX (%lld %lld) type %d getQScale %d.%03d"
- "%s::%s:%d BITBOX LrmeVarToVar (%lld, %lld) frameSumOfVar: %d, lowResVar: %d"
- "%s::%s:%d BITBOX SegmentEncoding VBV (%lld %lld) startLoop %d EndLoop %d curLoop %d"
- "%s::%s:%d BITBOX estimateBits (%lld, %lld) transcode: %lld, estTranscode: %lld, estBitsfromRC: %d"
- "%s::%s:%d BITBOX iIsFirstFrame %d SegmentEncoding Enabled %d totalFrames %lld"
- "%s::%s:%d Client %llu Mode %d %d %d"
- "%s::%s:%d ENC: StartCount %d-%d-%d-%d, Idle %d-%d-%d-%d-%d"
- "%s::%s:%d Enc_Client IDs %lld-%lld-%lld-%lld CTX %d-%d-%d-%d-%d"
- "%s::%s:%d Enc_Client IDs %lld-%lld-%lld-%lld-%lld CTX %d-%d-%d-%d-%d"
- "%s::%s:%d F(%lld, %lld) Unexpected TimeScale changed from %d to %d"
- "%s::%s:%d HRD planning status: (%lld %lld) type %d HrdFullness Start %d.%03d End %d.%03d Min %d.%03d loop %d"
- "%s::%s:%d LookAhead Update Past Frame Tid %d decodeOrder %lld LayerID %d unPredIdx %d.%03d "
- "%s::%s:%d MVHEVC (%lld %lld) pFrame.bitsFromCAVLC %lld pFrame.estimatedTranscodeBits %lld"
- "%s::%s:%d No PS available %d %d %d"
- "%s::%s:%d PSInfo num %d PS header bits count %d"
- "%s::%s:%d StartCount %d-%d-%d-%d, HW %d-%d-%d-%d-%d"
- "%s::%s:%d UnPredIdx (%lld %lld) tid %d LayerID %dProc past %d.%03d %d.%03d %d.%03d %d.%03d"
- "%s::%s:%d UnPredIdx (Update) (%lld %lld) frameType %s tid %d past %d.%03d %d.%03d %d.%03d %d.%03d"
- "%s::%s:%d Unexpected TimeScale change in timestamp %d %d %lld %p"
- "%s::%s:%d [ABR] Frame %lld totalBits %d targetBits %d overflow %d"
- "%s::%s:%d clientID %llu pps Num %d header %d bits %d bytes i %d PPS ID %d PPS count %d"
- "%s::%s:%d clientID %llu pps Num %d header %d bits %d bytes i %d PPS ID %d numView %d"
- "%s::%s:%d get NOTIFICATION_GET_ENC_PIPE_CONTINUE signal, for client %lld"
- "%s::%s:%d get NOTIFICATION_GET_ENC_PIPE_STATS_DONE signal, for client %lld"
- "%s::%s:%d invalid sps and pps iFWCreatesHeader %d %d %d"
- "%s::%s:%d is not initialized %p %llu %d %d"
- "%s::%s:%d lrme_ready %d, client_id = %lld, Idle %d-%d-%d-%d\n"
- "%s::%s:%d slice bytes: %d"
- "%s::%s:%d total PS bits %d"
- "%s::%s:%d vps_video_parameter_set_id %p %d"
- "%s::%s:%d xcode Done curr_slice_number %d"
- "%s::%s:%d | failed %d"
- "%s::%s:%d | failed to generate VPS %d %d"
- "%s::%s:%d: ResumableEncoding = %d - %d, %d"
- "%s::%s:%d: ResumableEncodingLA = %d - %d, %d, %d - %d, %d, %d"
- "((pPicParams->sBufPFSet.sLFSOutput.iAddr + i*iLowResResultsDMASize) & 63) == 0"
- "((pPicParams->sBufPFSet.sLFSOutput.iAddr + ii*iLowResResultsDMASize) & 63) == 0"
- "((pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr + ((m_psEncCommParams->encode_row_init/4) * LRME_LOWRES_REF_LUMA_TILED_STRIDE(m_psSequenceInits.uWidthInMbs))) & 63) == 0"
- "((pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr + (EncCommParams.encode_row_init/4) * HEVCVIDEOENCODER_LOWRES_REF_LUMA_TILED_STRIDE(EncCommParams.width)) & 63) == 0"
- "((pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr + EncCommParams.encode_row_init/4*lr_stride) & 63) == 0"
- "((pPicParams->sBufPFSet.sRefColocated.iAddr + coloDataContextOffset + multiCoreOffset) & 63) == 0"
- "(m_sSPS.sps_max_sub_layers_minus1 != 0) || (m_sSPS.sps_max_sub_layers_minus1 == 0 && m_sSPS.sps_temporal_id_nesting_flag == true)"
- "(pPicParams->sBufPFSet.sLFSOutput.iAddr & 63) == 0"
- "(pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr + (EncCommParams.encode_row_init/4) * HEVCVIDEOENCODER_LOWRES_REF_LUMA_TILED_STRIDE(EncCommParams.width)) != 0"
- "(pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr + EncCommParams.encode_row_init/4*lr_stride) != 0"
- "(pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr & 127) == 0"
- "(pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Header].iAddr & 127) == 0"
- "(pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr & 127) == 0"
- "(pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr & 127) == 0"
- "(pPicParams->sBufPFSet.sRefColocated.iAddr + coloDataContextOffset + multiCoreOffset) != 0"
- "(pPicParams->sBufPFSet.saLRRef[AVE_RefDir_Neg][me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr & 63) == 0"
- "(pPicParams->sBufPFSet.saLRRef[AVE_RefDir_Pos][l1_me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr & 63) == 0"
- "(pPicParams->sBufPFSet.saRef[AVE_RefDir_Neg][me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr & 63) == 0"
- "(pPicParams->sBufPFSet.saRef[AVE_RefDir_Neg][me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr & 63) == 0"
- "(pPicParams->sBufPFSet.saRef[AVE_RefDir_Pos][l1_me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr & 63) == 0"
- "(pPicParams->sBufPFSet.saRef[AVE_RefDir_Pos][l1_me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr & 63) == 0"
- "(pSessionCfg->iHwFeature & AVE_HW_FEATURE_LRME_PIPE_SYNC) == 0"
- "(shPos + 1) * (((((64) + (32) - 1) & ~((32) - 1))) > ((((1152) + (32) - 1) & ~((32) - 1))) ? ((((64) + (32) - 1) & ~((32) - 1))) : ((((1152) + (32) - 1) & ~((32) - 1)))) <= EncCommParams.sSliceHeader.iSize"
- "----PPS----"
- "----VUI----"
- "./AppleAVE2FW/Legacy/CDebugPrints.cpp"
- "./RTKit/platform/common/IOP/AVE_IOP_panda.cpp"
- "/AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp"
- "9012.99.0"
- "AVCController"
- "AVC_FindMaxMvsPer2Mb"
- "AVC_FindMaxSubMbRectSize"
- "AVC_Slice"
- "AVE_AVC_PPS"
- "AVE_AVC_PrepareSliceHeader"
- "AVE_AVC_SPS"
- "AVE_AVC_SetPPS"
- "AVE_AVC_SetSPS"
- "AVE_AVC_SetSlice"
- "AVE_AVC_Slice"
- "AVE_AVC_UpdatePOClsbSliceType"
- "AVE_ApplyTunables"
- "AVE_HEVC_PrepareSliceHeader"
- "AVE_HEVC_Update_POClsb_SliceType"
- "AVE_IOP_Config_panda"
- "AVE_Tunables_Set"
- "AvePipeDoneHandler"
- "B"
- "BITBOX (%lld %lld) totalBits %d, estTrancodeBits %lld\n"
- "CFSM::Get(fsmEncPipe) == GETTINGENCPIPESTATS"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:853"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:858"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:899"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:911"
- "Client:%llu %llu %llu %llu %llu AXI Error: 0x%x 0x%x 0x%x 0x%x\n"
- "Conccurent Mode check : F:%d : %d"
- "DMVController"
- "DoneEventEncPipe"
- "DoneEventStfPipe"
- "Enc ConcurrentMode:%d"
- "EncCommParams.pCbp0CntPrv != __null"
- "EncCommParams.sPIPInfo.iNum == 0"
- "EncCommParams.sSliceHeader.iAddr != 0"
- "EncCommParams.slice_count < AVE_SLICE_ACTIVE_MAX_NUM"
- "EncCommParams.slices_per_frame <= AVE_SLICE_ACTIVE_MAX_NUM"
- "FSMENCPIPE"
- "FSMSTFPIPE"
- "FillFWFrameStats"
- "GenerateRCSegmentCtx"
- "GenerateRCSegmentCtxLA"
- "GetStatsEventEncPipe"
- "GetStatsEventStfPipe"
- "HEVC COMMON:: pPicParams->sBufPFSet.sLFSOutput.iAddr[%d]:%016llx\n"
- "HEVCController"
- "HEVC_VPS"
- "HRD_CBRFiller"
- "HRD_Main"
- "HRD_VBVPlan_%d"
- "HevcPipeDoneHandler"
- "InitRCParameters"
- "InitScalingListRegs"
- "LowDelay %d"
- "MaxPicOrderCntLsb N/A"
- "OFController"
- "P"
- "PPSParams.bottom_field_pic_order_in_frame_present_flag %d"
- "PPSParams.chroma_qp_index_offset[%d] %d"
- "PPSParams.entropy_coding_mode_flag %d"
- "PPSParams.iFWCreatesHeader %d"
- "PPSParams.num_slice_groups_minus1 %d"
- "PPSParams.pic_init_qp_minus26 %d"
- "PPSParams.pic_init_qs_minus26 %d"
- "PPSParams.pic_scaling_matrix_present_flag %d"
- "PPSParams.redundant_pic_cnt_present_flag %d"
- "PPSParams.second_chroma_qp_index_offset[%d] %d"
- "PPSParams.seq_parameter_set_id %d"
- "PPSParams.transform_8x8_mode_flag %d"
- "PPSParams.weighted_bipred_idc %d"
- "PrepTemplateFlags"
- "RestoreRCSegmentCtx"
- "RestoreRCSegmentCtxLA"
- "SPS VUI.aspect_ratio_info_present_flag %d"
- "SPS VUI.bitstream_restriction_flag %d"
- "SPS VUI.colour_description_present_flag %d"
- "SPS VUI.colour_primaries %d"
- "SPS VUI.fixed_frame_rate_flag %d"
- "SPS VUI.matrix_coefficients %d"
- "SPS VUI.nal_hrd_parameters_present_flag %d"
- "SPS VUI.num_units_in_tick %d"
- "SPS VUI.overscan_info_present_flag %d"
- "SPS VUI.pic_struct_present_flag %d"
- "SPS VUI.time_scale %d"
- "SPS VUI.timing_info_present_flag %d"
- "SPS VUI.transfer_characteristics %d"
- "SPS VUI.vcl_hrd_parameters_present_flag %d"
- "SPS VUI.video_format %d"
- "SPS VUI.video_full_range_flag %d"
- "SPS VUI.video_signal_type_present_flag %d"
- "SPS VUI.vui_parameters_present_flag %d"
- "SPS bit_depth_chroma_minus8 %d"
- "SPS bit_depth_luma_minus8 %d"
- "SPS chroma_format_idc %d"
- "SPS constraint_set0_flag %d"
- "SPS constraint_set1_flag %d"
- "SPS constraint_set2_flag %d"
- "SPS constraint_set3_flag %d"
- "SPS constraint_set4_flag %d"
- "SPS constraint_set5_flag %d"
- "SPS direct_8x8_inference_flag %d"
- "SPS eScalingMatrixMode %d"
- "SPS frame_crop_bottom_offset %d"
- "SPS frame_crop_left_offset %d"
- "SPS frame_crop_right_offset %d"
- "SPS frame_crop_top_offset %d"
- "SPS frame_cropping_flag %d"
- "SPS frame_mbs_only_flag %d"
- "SPS gaps_in_frame_num_value_allowed_flag %d"
- "SPS iMaxNumRefFrames %d"
- "SPS level_idc %d"
- "SPS log2_max_frame_num_minus4 %d"
- "SPS log2_max_pic_order_cnt_lsb_minus4 %d"
- "SPS pic_height_in_map_units_minus1 %d"
- "SPS pic_order_cnt_type %d"
- "SPS pic_width_in_mbs_minus1 %d"
- "SPS profile_idc %d"
- "SPS qpprime_y_zero_transform_bypass_flag %d"
- "SPS separate_colour_plane_flag %d"
- "SPS seq_parameter_set_id %d"
- "SPSparams.iFWCreatesHeader %d"
- "SPSparams.sVUI.aspect_ratio_idc %d"
- "SPSparams.sVUI.aspect_ratio_info_present_flag %d"
- "SPSparams.sVUI.bitstream_restriction_flag %d"
- "SPSparams.sVUI.chroma_loc_info_present_flag %d"
- "SPSparams.sVUI.chroma_sample_loc_type_bottom_field %d"
- "SPSparams.sVUI.chroma_sample_loc_type_top_field %d"
- "SPSparams.sVUI.colour_description_present_flag %d"
- "SPSparams.sVUI.colour_primaries %d"
- "SPSparams.sVUI.default_display_window.def_disp_win_bottom_offset %d"
- "SPSparams.sVUI.default_display_window.def_disp_win_left_offset %d"
- "SPSparams.sVUI.default_display_window.def_disp_win_right_offset %d"
- "SPSparams.sVUI.default_display_window.def_disp_win_top_offset %d"
- "SPSparams.sVUI.default_display_window_flag %d"
- "SPSparams.sVUI.field_seq_flagg %d"
- "SPSparams.sVUI.frame_field_info_present_flag %d"
- "SPSparams.sVUI.log2_max_mv_length_horizontal %d"
- "SPSparams.sVUI.log2_max_mv_length_vertical %d"
- "SPSparams.sVUI.matrix_coeffs %d"
- "SPSparams.sVUI.max_bits_per_min_cu_denom %d"
- "SPSparams.sVUI.max_bytes_per_pic_denom %d"
- "SPSparams.sVUI.min_spatial_segmentation_idc %d"
- "SPSparams.sVUI.motion_vectors_over_pic_boundaries_flag %d"
- "SPSparams.sVUI.neutral_chroma_indication_flag %d"
- "SPSparams.sVUI.overscan_info_present_flag %d"
- "SPSparams.sVUI.restricted_ref_pic_lists_flag %d"
- "SPSparams.sVUI.sar_height %d"
- "SPSparams.sVUI.sar_width %d"
- "SPSparams.sVUI.tiles_fixed_structure_flag %d"
- "SPSparams.sVUI.transfer_characteristics %d"
- "SPSparams.sVUI.video_format %d"
- "SPSparams.sVUI.video_full_range_flag %d"
- "SPSparams.sVUI.video_signal_type_present_flag %d"
- "SPSparams.sVUI.vui_parameters_present_flag %d"
- "SPSparams.sVUI.vui_timing_info_present_flag %d"
- "Setup_HEVC_B_Frame"
- "Setup_HEVC_CRA_Frame"
- "Setup_HEVC_I_Frame"
- "SrcFrameDecrementRefCount"
- "StartEventEncPipe"
- "StartEventStfPipe"
- "Unexpected enc_type: %d. Cannot map to pipe mode"
- "Write_dec_ref_pic_marking"
- "Write_pic_parameter_set_rbsp"
- "Write_pred_weight_table"
- "Write_ref_pic_list_modification"
- "Write_seq_parameter_set_rbsp"
- "Write_slice_header"
- "Write_vui_parameters"
- "bNumRefIdxActiveOverrideFlag == ((m_psSlice->num_ref_idx_active_override_flag) != 0)"
- "cRPS.CurrRpsIdx %d"
- "client->m_saSrcFrameRefCount[idx].iRefCount >= 0"
- "coded_data_hdr->sSliceInfo.iNum"
- "coded_data_hdr->sSliceInfo.iNum < AVE_SLICE_ACTIVE_MAX_NUM"
- "currPipeEncCmd.Get()"
- "failed to get dev info"
- "false"
- "fps %d.%03d totalFrames %lld"
- "fsmEncPipe != 0"
- "fsmStfPipe != 0"
- "getQScale"
- "hClientQueue.GetIDFromIndex(ch) == currPipeEncCmd->client_id"
- "iMaxNumRefFrames: %d"
- "iNum <= 9"
- "m_psPPS->num_slice_groups_minus1 == 0"
- "m_psSPS->eScalingMatrixMode >= ScalingMatrixMode_Flat && m_psSPS->eScalingMatrixMode <= ScalingMatrixMode_ExplicitHighComp"
- "m_psSPS->num_ref_frames_in_pic_order_cnt_cycle == 0"
- "m_psVUI != __null"
- "m_sPPS.num_extra_slice_header_bits == 0"
- "m_sSPS.sVUI.vui_parameters_present_flag == true"
- "mctf_currPipeCmd"
- "pCmd != __null"
- "pInPicParams.sBufPFSet.SrcNbrInfo %016llx\n"
- "pInPicParams.sBufPFSet.SrcNbrPixels %016llx\n"
- "pInPicParams.sBufPFSet.sCodedData.iAddr %08x\n"
- "pInPicParams.sBufPFSet.sCodedHeader.iAddr[%d] %08x\n"
- "pInPicParams.sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data] %016llx\n"
- "pInPicParams.sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data] %016llx\n"
- "pInPicParams.sBufPFSet.sRefColocated %016llx\n"
- "pInPicParams.sBufPFSet.sSrcNbrData %016llx\n"
- "pInPicParams.sBufPFSet.saRef[AVE_RefDir_Neg][AVE_Ref_A].saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr %016llx\n"
- "pInPicParams.sBufPFSet.saRef[AVE_RefDir_Neg][AVE_Ref_A].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr %016llx\n"
- "pInPicParams.sBufPFSet.saRef[AVE_RefDir_Neg][AVE_Ref_B].saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr %016llx\n"
- "pInPicParams.sBufPFSet.saRef[AVE_RefDir_Neg][AVE_Ref_B].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr %016llx\n"
- "pInPicParams.sBufPFSet.saRef[AVE_RefDir_Pos][AVE_Ref_A].saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr %016llx\n"
- "pInPicParams.sBufPFSet.saRef[AVE_RefDir_Pos][AVE_Ref_A].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr %016llx\n"
- "pInPicParams.sBufPFSet.saRef[AVE_RefDir_Pos][AVE_Ref_B].saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr %016llx\n"
- "pInPicParams.sBufPFSet.saRef[AVE_RefDir_Pos][AVE_Ref_B].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr %016llx\n"
- "pInitParams != __null"
- "pPicParams->sBufPFSet.sLFSOutput.iAddr != 0"
- "pPicParams->sBufPFSet.sLRInput.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr + ((m_psEncCommParams->encode_row_init/4) * LRME_LOWRES_REF_LUMA_TILED_STRIDE(m_psSequenceInits.uWidthInMbs))"
- "pPicParams->sBufPFSet.sMultiPassStats.iAddr != 0"
- "pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Data].iAddr != 0"
- "pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Chroma].saIBuf[AVE_BufIdx_Header].iAddr != 0"
- "pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr != 0"
- "pPicParams->sBufPFSet.sRecon.saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr != 0"
- "pPicParams->sBufPFSet.sSliceHeader.iAddr != 0"
- "pPicParams->sBufPFSet.sSliceHeader.iSize >= (((64) + (32) - 1) & ~((32) - 1))"
- "pPicParams->sBufPFSet.saLRRef[AVE_RefDir_Neg][me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr != 0"
- "pPicParams->sBufPFSet.saLRRef[AVE_RefDir_Pos][l1_me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr != 0"
- "pPicParams->sBufPFSet.saRef[AVE_RefDir_Neg][me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr != 0"
- "pPicParams->sBufPFSet.saRef[AVE_RefDir_Neg][me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr != 0"
- "pPicParams->sBufPFSet.saRef[AVE_RefDir_Pos][l1_me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Data].iAddr != 0"
- "pPicParams->sBufPFSet.saRef[AVE_RefDir_Pos][l1_me_ref_index].saCIBuf[AVE_BufIdx_Luma].saIBuf[AVE_BufIdx_Header].iAddr != 0"
- "pSessionCfg->sEnc.sAlgCfg.sGOP.iAdaptDelay %d"
- "pSessionCfg->sEnc.sAlgCfg.sGOP.iaNumOfFrame[AVE_FrameType_B] %d"
- "pcSWriter != __null"
- "prepareSliceHeaderForFW"
- "psAvcProcCmd != __null"
- "psCfg != __null"
- "psEncCmd != __null"
- "psLimit != __null"
- "psPPS != __null"
- "psPPS != __null && psCommonParams != __null && psSlice != __null"
- "psPPS != __null && psCommonParams != __null && psSyntaxPFCfg != __null"
- "psPSContext != __null"
- "psPSInfo->iNum > 0"
- "psRegCfg->iAddr != (uint32_t)(-1)"
- "psSL != __null"
- "psSPS != __null"
- "psSPS != __null && psPPS != __null && piSH != __null && iBufSize > 0 && piSHNumOfBit != __null"
- "psSlice != __null"
- "psSyntaxCfg != __null && psPPS != __null"
- "psSyntaxCfg != __null && psSPS != __null"
- "psSyntaxPFCfg != __null && psSlice != __null"
- "sBufPFSet.saEntropyCoding[%d][%d]:%016llx\n"
- "sBufSet.saDPB[%d][0].iAddr:%016llx\n"
- "sHeartBeatParams.terminateSema != (SEMA)0"
- "sPP.terminateSema != (SEMA)0"
- "shPos < AVE_SLICE_ACTIVE_MAX_NUM"
- "sps.eScalingMatrixMode >= ScalingMatrixMode_Flat && sps.eScalingMatrixMode <= ScalingMatrixMode_ExplicitHighComp"
- "updateBitRate"
- "updateConstantRateFactor"
- "updateDRLParams"
- "updateHRDUsingTranscodeBits"
- "updateHrdParams"
- "updateModeDistributionForZeroLA"
- "updateParams"
- "video_parameter_set_rbsp"
- "vps_encode_independent_layer_parameters"
- "vps_extension"
- "vps_vui"

```
