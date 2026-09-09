## libfire7.dylib

> `/usr/lib/libfire7.dylib`

```diff

 135.0.5.0.0
-  __TEXT.__text: 0x284208
+  __TEXT.__text: 0x28468c
   __TEXT.__init_offsets: 0x10
   __TEXT.__const: 0x2cd1c
   __TEXT.__cstring: 0x3ffb7
   __TEXT.__gcc_except_tab: 0x5514
-  __TEXT.__unwind_info: 0x5718
+  __TEXT.__unwind_info: 0x5720
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x84a0
   __DATA_CONST.__weak_got: 0x8
Functions:
~ __ZN7BlueFin21MinnowGllRpcParserImp11ParseMethodEhhPht : 12036 -> 12040
~ __ZN7BlueFin7GlReqSm15SetAsstFromPendEbb : 4772 -> 4780
~ __ZN7BlueFin20GlMeSrdPacketManager18AppendReliableDataEPht : 388 -> 396
~ __ZN7BlueFin7GlReqSm18sendMeSignalAidingERKNS_17GlMeSignalAidInfoE : 3136 -> 3172
~ __ZN7BlueFin7GlReqSm17AddSignalTypeFlagERNS_17GlMeSignalAidInfoE : 1116 -> 1164
~ __ZN7BlueFin7GlReqSm45ReorderSigAidBasedOnSatAidElvAndLimitChannelsEv : 2400 -> 2412
~ __ZN7BlueFin10GlPeAlmMgr15SetSignalAidingERKNS_9GlSvIdSetEPNS_17GlMeSignalAidInfoEPKbRS4_ : 7740 -> 7844
~ __ZN7BlueFin10GlPeAlmMgr21ChooseInitialOppPairsERNS_15GlPeAlmSvIdListERKNS_11GlGnssIdSetE : 1104 -> 1120
~ __ZN7BlueFin7GlReqSm15SetSignalAidingERKNS_9GlSvIdSetE : 14828 -> 14904
~ __ZN7BlueFin7GlReqSm15UpdateSatAidingEjPKNS_21GlPeExtendedFixStatusE : 1672 -> 1680
~ __ZN7BlueFin15GlPeRangeAidGen6updateEjRKNS_9GlSvIdSetENS_22GLME_USER_TCXO_DYNAMICE : 5924 -> 5940
~ __ZN7BlueFin7GlReqSm33GenerateAidingForParallelFarStartEjRKNS_9GlSvIdSetEPKNS_21GlPeExtendedFixStatusE : 4764 -> 4784
~ __ZN7BlueFin21MinnowEswRpcSatEncImp27esw_sat_rpc_init_multi_carrEPNS_18GlMeSrdTransactionEhPKNS_24sv_param_multi_carr_typeEPhhhPNS_18control_param_typeEPKNS_23sat_init_aid_param_typeEh : 1520 -> 1524
~ __ZN7BlueFin15GlMeSrdAcqMgrSm25UpdateSvidToSearchForMgrsEv : 23888 -> 23880
~ __ZN7BlueFin20GlMeSrdPacketManager20RemoveEventFromQueueEhh : 244 -> 248
~ __ZN7BlueFin22GlMeSrdCtrlSmRpcSatEvt30gll_satevt_rpc_rm_event_reportEhPNS_21satevt_rm_report_typeE : 1856 -> 1864
~ __ZN7BlueFin21MinnowGllRpcParserImp31Handle_SatRpt_AcquisitionWindowERNS_8GlStreamE : 1028 -> 1032
~ __ZN7BlueFin23GlSignalIdArrayIterator4NextEv : 316 -> 320
~ __ZNK7BlueFin12GlPeGnssTime6GetUtcERNS_9GlUtcTimeE : 1028 -> 1036
~ __ZN7BlueFin7GlReqSm16initializeAidingEv : 684 -> 688
~ __ZN7BlueFin14GlSettingsImpl28SetNotchFiltersConfigurationEPKNS_19NOTCH_FILTER_CONFIGEh : 252 -> 256
~ __ZN7BlueFin10GlDbgCodec3RvwERh : 232 -> 240
~ __ZNK7BlueFin9GlSvIdSet6GetStrEPctcb : 816 -> 820
~ __ZN7BlueFin14GlSettingsImpl16SetSvIdSupportedERKNS_9GlSvIdSetE : 420 -> 424
~ __ZN7BlueFin35GlMeSrdReceiverParametersProgrammer24ProgramCommonJobManagersEPNS_18GlMeSrdTransactionERKNS_20GlMeSrdAsicConfigIfcE : 1160 -> 1164
~ __ZN7BlueFin13GlPeSensStats5resetEv : 208 -> 216
~ __ZN7BlueFin9GlUtcTime12breakdownFctEv : 508 -> 516
~ __ZNK7BlueFin12GlPeGnssTime6GetUtcERNS_8UTC_TIMEE : 1008 -> 1016
~ __ZN7BlueFin11GlPeNmeaGen13FormatNmeaGSAEPKNS_13GL_FIX_STATUSEPcs : 1556 -> 1548
~ __ZN7BlueFin11GlPeNmeaGen13FormatNmeaGSVEPKNS_13GL_FIX_STATUSEPcs : 1760 -> 1752
~ __ZN7BlueFin11GlPeNmeaGen13FormatNmeaSVCEPKNS_13GL_FIX_STATUSEPcs : 828 -> 832
~ __ZN7BlueFin11GlPeNmeaGen13FormatNmeaSTAEPKNS_13GL_FIX_STATUSERKNS_14GlSettingsImplEPcs : 1240 -> 1244
~ __ZN7BlueFin6GlPeKF7SetMsmtEb : 43084 -> 43100
~ __ZN7BlueFin17GlMeSignalAidInfo20RemoveAllNullSignalsEv : 120 -> 124
~ __ZN7BlueFin22GlMeSrdSatRptTrkMsmtMI15BuildNavBitMsmtEv : 1420 -> 1428
~ __ZN7BlueFin20GlMeSrdSvIdReportMgr18ReportMeasurementsEj : 5072 -> 5076
~ __ZN7BlueFin21GlMeMeasSelfAidFilter13SetSatAidInfoEPKNS_12GlSatAidInfoE : 312 -> 316
~ __ZN7BlueFin8GlPeHula21SetLmsFromSensorInputERKNS_13GlExtSensDataE : 2476 -> 2484
~ __ZN7BlueFin12GlMeFrameMgr11AddBestWordEjjjjjjj : 3252 -> 3264
~ __ZN7BlueFin11GlPeNmeaGen13FormatTimeTagEj : 1024 -> 1032
~ __ZN7BlueFin21GlMeSrdViterbiDecoder10RunViterbiEtPjS1_b : 1664 -> 1668
~ __ZN7BlueFin14GlMeMsmtHolder10SetDSPMeasERKNS_11GlMeDSPMeasE : 1428 -> 1432
~ __ZN7BlueFin11GlPeSbasMgr9HandleMsgERKNS_16GlDataSubFrmMeasE : 1960 -> 1976
~ __ZN7BlueFin14GlMeMsmtHolder17MsmtsCompleteInitEjt : 8556 -> 8564
~ __ZN7BlueFin8GlMeMeas9SerializeERKNS_6GlMeasEPNS_11GlCallBacksEh : 2024 -> 2032
~ __ZN7BlueFin13GlPeFixStatus16SetSIGMeasuementERNS_11GlPeMsmtMgrEPKNS_13GlMePlatfStatE : 4812 -> 4816
~ __ZN7BlueFin12CT_GRID_FULL8loadGridEPKjRKNS_15ST_GRID_CONTEXTERNS_12CT_GRID_XWCVE : 388 -> 392
~ __ZN7BlueFin21GlPeSvVisibilityCache20UpdateVisibilityInfoEPKNS_9GlSigMeasEPKNS_13stPeSigMeasKFEj : 1476 -> 1480
~ __ZN7BlueFin10GlPeLtoMgr18UpdateGnssL5HealthENS_6teGNSSEPKNS_24GlUncmprsdGnssSvL5HealthEjb : 2748 -> 2752
~ __ZN7BlueFin7GlReqSm11CreateMeJobEv : 2844 -> 2852
~ __ZN7BlueFin13GlPeEphemeris11DeserializeERNS_13GlSysLogEntryE : 756 -> 760
~ __ZN7BlueFin21GlPeSpecialTimeEvents18ScheduleTimeEventsERNS_15GlPeTimeManagerE : 2912 -> 2928
~ __ZN7BlueFin13GlPeEphemeris17DeserializeHeaderERNS_13GlSysLogEntryERNS_6teGNSSERNS0_9teFormatsE : 496 -> 500
~ __ZN7BlueFin11GlMeMsmtMgr24GetB1cL1cSecCodePhsInSymERKNS_10GlSignalIdERKNS_10GlMeAcqWinERt : 688 -> 692
~ __ZNSt3__15dequeIN7BlueFin13GlExtSensDataENS_9allocatorIS2_EEE19__add_back_capacityEv : 1116 -> 1128
~ __ZNSt3__114__split_bufferIPN7BlueFin13GlExtSensDataENS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_ : 256 -> 260
~ __ZN7BlueFin25GlPeSvVisibilityCacheData11DeserializeERNS_13GlSysLogEntryE : 512 -> 516
~ __ZN7BlueFin10GlPeAlmMgr9Alm2PlaneEv : 2560 -> 2568
~ __ZN7BlueFin17stPeStoredDoppler11DeserializeERNS_13GlSysLogEntryE : 628 -> 636
~ __ZN7BlueFin10GlPeAlmMgr16UseHardCodedDataEv : 1436 -> 1432
~ __ZN7BlueFin13GlPeRtoReader14parseClkErrTgdERNS_13GlPeBitReaderEPNS_27GlUncmprsdGpsNonL1ClkErrTgdEPNS_20GlUncmprsdGpsL1CAIscEjt : 620 -> 624
~ __ZN7BlueFin13GlPeLtoReaderC2EPNS_10GlPeLtoMgrEPNS_21GlPePexHostEncoderIfcEjPNS_15GlPeLtoReadStatEPNS_8GlEngineEPNS_11GlPeAsstMgrERNS_15GlPeTimeManagerEPNS_19GlPeEngineCallBacksEPNS_11GlNvMemImplERNS_15GlPeRangeAidGenERNS_15GlPeSvHealthMgrERNS_16GlPeRtiRequestorERNS_14GlPeStartupMgrERNS_19GlPeClkCalibrateMgrERNS_10GlPeOscMgrE : 4000 -> 3992
~ __ZN7BlueFin13GlPeRtoReader23getRtoUncmprsdEphBufferERKNS_6GlGnssE : 224 -> 216
~ __ZNK7BlueFin13GlPeKFAltAsst15altAsstFirstFixERNS_9stAltAsstERKNS_8LLA_TYPEEj : 800 -> 804
~ __ZN7BlueFin12GlPeFirstFix11FirstFixMgrERKNS0_15stFirstFixInputERNS0_16stFirstFixReturnE : 17140 -> 17132
~ __ZN7BlueFin10GlDbgCodec3RvwERs : 232 -> 240
~ __ZN7BlueFin10GlDbgCodec3RvwERj : 232 -> 240
~ __ZN7BlueFin10GlDbgCodec3RvwERf : 232 -> 240
~ __ZNSt3__15dequeIN7BlueFin13GlSensRawDataENS_9allocatorIS2_EEE19__add_back_capacityEv : 1104 -> 1116
~ __ZNSt3__114__split_bufferIPN7BlueFin13GlSensRawDataENS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_ : 248 -> 252
~ __ZN7BlueFin10GlDbgCodec3RvwERd : 232 -> 240
~ __ZN7BlueFin10GlDbgCodec3RvwERy : 232 -> 240
~ __ZN7BlueFin10GlDbgCodec3RvwERt : 232 -> 240
~ __ZN7BlueFin10GlDbgCodec3RvwERb : 232 -> 240
~ __ZN7BlueFin10GlDbgCodec3RvwERi : 232 -> 240
~ __ZN7BlueFin17GlPeGpsQzssEphMgr17SetDataSubFrmMeasEPNS_16GlDataSubFrmMeasE : 6368 -> 6372
~ __ZN7BlueFin10GlDbgCodec3RvwERa : 232 -> 240
~ __ZNK7BlueFin16GlPeSvHealthData13SerializeImplEPNS_11GlCallBacksEh : 692 -> 696
~ __ZNK7BlueFin17stPeStoredDoppler13SerializeImplEPNS_11GlCallBacksEh : 704 -> 712
~ __ZNSt3__15dequeIN18FireMessageHandler7MessageENS_9allocatorIS2_EEE19__add_back_capacityEv : 1116 -> 1128
~ __ZNSt3__114__split_bufferIPN18FireMessageHandler7MessageENS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_ : 256 -> 260
~ __ZNSt3__15dequeIN18FireMessageHandler21GLRefPositionExtendedENS_9allocatorIS2_EEE19__add_back_capacityEv : 1104 -> 1116
~ __ZNK7BlueFin12GlSatAidInfo13SerializeImplEPNS_11GlCallBacksEh : 1092 -> 1096
~ __ZN7BlueFin12GlSatAidInfo11DeserializeERNS_13GlSysLogEntryE : 1008 -> 1016
~ __ZNK7BlueFin16GlDataSubFrmMeas13SerializeImplEPNS_11GlCallBacksEh : 456 -> 460
~ __ZN7BlueFin16GlDataSubFrmMeas11DeserializeERNS_13GlSysLogEntryE : 300 -> 304
~ __ZN7BlueFin19GlGlonassDataString11DeserializeERNS_13GlSysLogEntryE : 284 -> 288
~ __ZNK7BlueFin19GlGlonassDataString13SerializeImplEPNS_11GlCallBacksEh : 440 -> 444
~ __ZN7BlueFin17GlGalileoINavPage11DeserializeERNS_13GlSysLogEntryE : 364 -> 368
~ __ZNK7BlueFin17GlGalileoINavPage13SerializeImplEPNS_11GlCallBacksEh : 512 -> 516
~ __ZN7BlueFin15GlNavICSubFrame11DeserializeERNS_13GlSysLogEntryE : 304 -> 308
~ __ZNK7BlueFin15GlNavICSubFrame13SerializeImplEPNS_11GlCallBacksEh : 456 -> 460
~ __ZNK7BlueFin17GlMeSignalAidInfo13SerializeImplEPNS_11GlCallBacksEh : 556 -> 564
~ __ZN7BlueFin17GlMeSignalAidInfo11DeserializeERNS_13GlSysLogEntryE : 364 -> 368
~ __ZN7BlueFin9GlSvIdSet6SetStrEPKc : 600 -> 608
~ __ZN7BlueFin10GlDbgCodec3RvwERNS_17GlGnssAgcInfoDataE : 160 -> 164
~ __ZN7BlueFin10GlDbgCodec3RvwERc : 232 -> 240
~ __ZN7BlueFin10GlDbgCodec3RvwERx : 232 -> 240
~ __ZN7BlueFin21MinnowGllRpcParserImp24Handle_SatRpt_SubTrkMsmtERNS_8GlStreamE : 1360 -> 1364
~ __ZN7BlueFin16GlMeSrdAidingMgr16LogMappingChangeEbRKNS_10GlSignalIdEh : 288 -> 292
~ __ZN7BlueFin18GlMeSrdGeofenceMgr7runningEPS0_PKNS_7GlEventE : 1648 -> 1652
~ __ZN7BlueFin18GlMeSrdGeofenceMgr9hostsleepEPS0_PKNS_7GlEventE : 7340 -> 7360
~ __ZNK7BlueFin34GlMeSrdEstBitPhsSerializeContainer13SerializeImplEPNS_11GlCallBacksEh : 804 -> 808
~ __ZN7BlueFin34GlMeSrdEstBitPhsSerializeContainer11DeserializeERNS_13GlSysLogEntryE : 700 -> 704
~ __ZNK7BlueFin20GlMeCorrVecContainer13SerializeImplEPNS_11GlCallBacksEh : 2072 -> 2076
~ __ZN7BlueFin20GlMeCorrVecContainer11DeserializeERNS_13GlSysLogEntryE : 1112 -> 1116
~ __ZNK7BlueFin17GlMeSrdDspMeasAux13SerializeImplEPNS_11GlCallBacksEh : 2308 -> 2320
~ __ZN7BlueFin17GlMeSrdDspMeasAux11DeserializeERNS_13GlSysLogEntryE : 1920 -> 1924
~ __ZN7BlueFin16GlMeSrdEstLowTow3RunERKNS_16GlMeSrdPhysConstERKNS_19GlMeSrdGlbTrkParamsERKNS_16GlMeEswTrkParamsERKNS_10GlSignalIdERKNS_24GlMeSrdAsicNavBitTrkMsmtEdjRKNS_22GlMeSrdTowAssistHolderERNS_20GlMeSrdLowTowResultsE : 1616 -> 1620
~ __ZN7BlueFin16GlMeSrdEstLowTow13SearchPatternEPNS_16GlMeSrdLowTowMgrERKNS_22GlMeSrdTowAssistHolderE : 2264 -> 2268
~ __ZN7BlueFin13GlMeSrdEstMPF8MPFLogicERNS_17GlMeSrdMPFResultsE : 1028 -> 1032
~ __ZN7BlueFin21GlMeSatIdProbationMgr6IgnoreEhRKNS_6GlSvIdE : 112 -> 116
~ __ZN7BlueFin28GlMeSrdSvIdMsmtHistoryBuffer27MsmtHistoryGarbageCollectorEv : 548 -> 552
~ __ZN7BlueFin19CarpEswRpcSatEncImp16esw_sat_rpc_initEPNS_18GlMeSrdTransactionEhPNS_13sv_param_typeEhPNS_18control_param_typeEhhh : 1036 -> 1040
~ __ZN7BlueFin22CarpEswRpcGeomgrEncImp27geo_mgr_rpc_set_geo_sv_infoEPNS_18GlMeSrdTransactionEPNS_21geofence_sv_info_typeE : 548 -> 552
~ __ZNK7BlueFin16GlMeResourceData13SerializeImplEPNS_11GlCallBacksEh : 652 -> 656
~ __ZN7BlueFin16GlMeResourceData11DeserializeERNS_13GlSysLogEntryE : 452 -> 456
~ __ZN7BlueFin28GlMeReceiverParametersLogger18ModeTrkParamToSlogERKNS_25GlMeReceiverParametersIfcENS_11CNSTL_TYPESENS_10MODE_TYPESE : 1944 -> 1948
~ __ZN7BlueFin19GlMeBeidouDecodeMgr6SearchENS_19GlMeBeidouBitSourceE : 108 -> 116
~ __ZN7BlueFin19GlMeBeidouDecodeMgr8PreambleENS_19GlMeBeidouBitSourceE : 112 -> 120
~ __ZN7BlueFin15GlMeBeidouFrame11SetDataBitsERNS_19GlMeBeidouDecodeMgrENS_19GlMeBeidouBitSourceERNS_11GlBitBufferES5_j : 5948 -> 5944
~ __ZN7BlueFin21GlMeBeidouPolarityMgr7SetBitsEbRNS_11GlBitBufferEjbS2_j : 1008 -> 1012
~ __ZNK7BlueFin11GlMeDSPMeas13SerializeImplEPNS_11GlCallBacksEh : 860 -> 864
~ __ZN7BlueFin11GlMeDSPMeas11DeserializeERNS_13GlSysLogEntryE : 1184 -> 1188
~ __ZN7BlueFin13GlPeNicEphMgr17SetDataSubFrmMeasERKNS_16GlDataSubFrmMeasE : 3816 -> 3820
~ __ZNK7BlueFin10GlMeAcqWin13SerializeImplEPNS_11GlCallBacksEh : 632 -> 636
~ __ZN7BlueFin10GlMeAcqWin11DeserializeERNS_13GlSysLogEntryE : 896 -> 900
~ __ZN7BlueFin16NonGeoMsgProcess16EphUpdateProcessEPNS_14PerSubFrmWordsEPt : 580 -> 592
~ __ZN7BlueFin13GeoMsgProcess16EphUpdateProcessEPNS_14PerSubFrmWordsEPt : 808 -> 828
~ __ZN7BlueFin11GlPeAsstMgr11GetAsstStatERNS_12GlAidRequestEj : 3228 -> 3244
~ __ZN7BlueFin16GlPeEphBadDecode11DeserializeERNS_13GlSysLogEntryE : 232 -> 236
~ __ZNK7BlueFin16GlPeEphBadDecode13SerializeImplEPNS_11GlCallBacksEh : 480 -> 484
~ __ZNK7BlueFin25GlPeSvVisibilityCacheData13SerializeImplEPNS_11GlCallBacksEh : 712 -> 716
~ __ZNK7BlueFin8GlPosEng21GetSatelliteOrbitInfoEPNS_20GlSatelliteOrbitDataEt : 1516 -> 1524
~ __ZNK7BlueFin27GlPeCachedAtmosDelaysWriter13SerializeImplEPNS_11GlCallBacksEh : 608 -> 612
~ __ZN7BlueFin14GlPeCoarseTime13SetDtsFromTowERKNS_9GlSvIdSetEdddRKNS0_8SettingsE : 5116 -> 5172
~ __ZN7BlueFin18GlPeNavGnssMeasMgr16CheckMissingBitsEbPaS1_ : 452 -> 444
~ __ZN7BlueFin8stRtdMgr10RtdComputeEjRKNS_8LLA_TYPEEfb : 3528 -> 3536
~ __ZN7BlueFin11GlPePrawnKf15ComputePositionERKNS_15GlPeNavGnssKFIf8SettingsERKNS_16GlPeNavGnssStateE : 10676 -> 10668
~ __ZN7BlueFin13GlPeFixStatus12UpdateSvAzElEv : 248 -> 252
~ __ZN7BlueFin14GlPeRqHdlrMeas16SetSIGMeasuementERNS_11GlPeMsmtMgrE : 6828 -> 6836
~ __ZN7BlueFin14GlPeMeasStatus7GetMeasERNS_11GlPeMsmtMgrERNS_11GL_RES_MEASEbbbb : 4744 -> 4752
~ __ZN7BlueFin7GlReqSm31HighestVisibilitySigAidOverrideEv : 1644 -> 1660
~ __ZN7BlueFin7GlReqSm15SetSimSigAidingERKNS_17GlMeSignalAidInfoERKNS_9GlSvIdSetERS1_ : 1888 -> 1908
~ __ZN7BlueFin7GlReqSm35GenerateAidingForSequentialFarStartEjRKNS_9GlSvIdSetEPKNS_21GlPeExtendedFixStatusE : 2800 -> 2812
~ __ZN7BlueFin14GlSettingsImpl11SetDbgParamERA64_KcRA256_S1_ : 160 -> 164
~ __ZNK7BlueFin14GlSettingsImpl11GetDbgParamEiRA64_cRA256_c : 172 -> 180
~ __ZN7BlueFin14GlPeGlnTimeMgr22CheckGlonassStringTimeEhi : 720 -> 724
```
