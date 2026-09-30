## libfire9.dylib

> `/usr/lib/libfire9.dylib`

```diff

-  __TEXT.__text: 0x2fe12c
-  __TEXT.__const: 0x9ef78
-  __TEXT.__cstring: 0x1b666
-  __TEXT.__oslogstring: 0x19248
+  __TEXT.__text: 0x301c60
+  __TEXT.__const: 0x9f698
+  __TEXT.__cstring: 0x1bd8d
+  __TEXT.__oslogstring: 0x1938e
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xa9e0
+  __DATA_CONST.__const: 0xaa00
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xf730
+  __AUTH_CONST.__const: 0xf728
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__auth_got: 0x228
   __DATA.__data: 0x148

   __DATA.__bss: 0x26d8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 7591
-  Symbols:   16923
-  CStrings:  5143
+  Functions: 7594
+  Symbols:   16939
+  CStrings:  5203
 
Sections:
~ __AUTH_CONST.__weak_auth_got : content changed
~ __DATA.__data : content changed
Symbols:
+ __ZN13FireDeviceLog13LoggingBuffer14appendInternalEPKcm
+ __ZN13FireDeviceLog13LoggingBuffer8writeLogEPKcm
+ __ZN13FireDeviceLog13LoggingBuffer9writeHeadEv
+ __ZN13FireDeviceLog13LoggingBuffer9writeLineEPKcmRKNSt3__117basic_string_viewIcNS3_11char_traitsIcEEEE
+ __ZN13FireDeviceLog13LoggingBuffer9writeStopEv
+ __ZN18FireMessageHandler11stopRequestENS_11RequestTypeE
+ __ZN18FireMessageHandler12startRequestENS_11RequestTypeE
+ __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_668981EPvs
+ __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_668981EPvs
+ __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_668981EPvs
+ __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_668981EPvs
+ __ZN7BlueFin15GlMeSrdAsicinit30mcuCheckForReceivedPacket_PikeEv
+ __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_668981EPvs
+ __ZN7BlueFin24GlMeSrdAsicUnitConverter22EswAidingFrequencyToHzEsRKNS_10GlSignalIdE
+ __ZN7BlueFin7GlUtils12LogBoundsOOBEPKcjS2_jS2_j
+ __ZN7BlueFin7GlUtils14LogBoundsClampEPKcjS2_jS2_j
+ __ZN7BlueFin7GlUtils14LogBoundsResetEPKcjS2_jS2_j
+ __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_668981EPvs
+ __ZNSt3__18to_charsEPcS0_dNS_12chars_formatEi
+ __ZZN13FireDeviceLog13LoggingBuffer5flushEvE7kPrefix
+ __ZZN13FireDeviceLog13LoggingBuffer9writeNmeaEPKcmE7kPrefix
+ ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_668981EPvs
- __ZN13FireDeviceLog13DeviceLogLineERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE
- __ZN13FireDeviceLog13LoggingBuffer5writeEPKcm
- __ZN13FireDeviceLog13LoggingBuffer7kPrefixE
- __ZN18FireMessageHandler11stopRequestENS_7RequestE
- __ZN18FireMessageHandler12startRequestENS_7RequestEPN7BlueFin9GlRequestE
- __ZN7BlueFin10GlDineCtrl23ChipData_GRABSNQ_667335EPvs
- __ZN7BlueFin11GlDbgEngine23ChipData_GRABSNQ_667335EPvs
- __ZN7BlueFin13GlPeMeIfDummy23ChipData_GRABSNQ_667335EPvs
- __ZN7BlueFin14GlDbgCodecBase8InitBaseEv
- __ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_667335EPvs
- __ZN7BlueFin18GlComStressTestMgr23ChipData_GRABSNQ_667335EPvs
- __ZN7BlueFin19GlRequestImplSyncin6CreateEPvS1_PFvPNS_9GlRequestENS_17GL_REQ_START_CODEEEsPFvS3_NS_16GL_SYNCIN_STATUSEPKNS_7GL_TIMEEEPFvS3_S7_EPFvS3_S7_dE
- __ZN7BlueFin9GlDbgMeIf23ChipData_GRABSNQ_667335EPvs
- __ZNK7BlueFin11GlMeDSPMeas16GetMeasTrackModeEv
- __ZNKSt3__112__hash_tableINS_17__hash_value_typeIN18FireMessageHandler7RequestEPN7BlueFin9GlRequestEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE4findIS3_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS7_PvEEEERKT_
- __ZNSt3__19to_stringEd
- __ZZNSt3__112__hash_tableINS_17__hash_value_typeIN18FireMessageHandler7RequestEPN7BlueFin9GlRequestEEENS_22__unordered_map_hasherIS3_NS_4pairIKS3_S6_EENS_4hashIS3_EENS_8equal_toIS3_EEEENS_21__unordered_map_equalIS3_SB_SF_SD_EENS_9allocatorISB_EEE16__emplace_uniqueB9fqn220106IJRKNS_21piecewise_construct_tENS_5tupleIJRSA_EEENSQ_IJEEEEEENS9_INS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEEDpOT_ENKUlSR_SP_OSS_OST_E_clESR_SP_S14_S15_
- ___func__._ZN7BlueFin15GlEngineImplStd23ChipData_GRABSNQ_667335EPvs
- ___func__._ZN7BlueFin17GlMeSrdBitHistBufC2ERKS0_
CStrings:
+ "#fftd,periodic,sendStart,failed"
+ "#fftd,response,fail,%d,%s"
+ "#fftd,rft,sendStart,failed,%d"
+ "#fftd,tm,sendOneShortRequest,failed"
+ "#fftd,tm,sendStopRequest,failed"
+ "#fgd,GllFix,meas,%zu,svinfo,%zu"
+ "#fmh,eraseRequest,request,%p,%d,age,%.1f,pf,%p,meas,%p,sync,%p"
+ "#fmh,startRequest,%d,createFailed"
+ "#fmh,startRequest,%p,%d,alreadyExist,age,%.1f"
+ "(GlIntU16)(GlMeSrdAsicNavBitTrkMsmt::MAX_NUM_TRK_DATA_WORDS * 32)"
+ "(GlIntU16)GlMeSrdAsicNavBitTrkMsmt::MAX_NUM_TRK_DATA_WORDS"
+ "(GlIntU16)GlMeSrdAsicNavBitTrkMsmt::MAX_NUM_TRK_LOW_TOW_DATA_WORDS"
+ "(GlIntU16)NUM_SBAS_PRNS"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/FIREGPS9/proprietary/deliverables/gll_dev/gl_frame/glcrypto/glcrypto_rsa.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/FIREGPS9/proprietary/deliverables/gll_dev/gldebug/src/gldebug_glpeif.cpp:395"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/FIREGPS9/proprietary/deliverables/gll_dev/gldebug/src/gldebug_glpeif.cpp:489"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/FIREGPS9/proprietary/deliverables/gll_dev/gldebug/src/gldebug_glpeif.cpp:861"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/FIREGPS9/proprietary/deliverables/gll_dev/gldebug/src/gldebug_record.cpp"
+ "@(#)Broadcom GLL ver. 172.20.28 668981, 2026/Jun/22, 17:45:22, build_job_id:__BUILDJOBID__, %s://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/...\n"
+ "@end"
+ "ChipData_GRABSNQ_668981"
+ "Clamped: %s (%u) > %s (%u); clamping to %u [%s:%u]\n"
+ "EngineAlreadyInRun,engine,%p,pf,%p,sync,%p"
+ "FIRE@28 GLL@668981"
+ "GL_MAX_IONEX_MAPS"
+ "GlMeSrdEstLowTow::GLMESRD_ESTLOWTOW_LT_MAX_PHASES"
+ "GlReqOnStart,request,ok,%p,pf,%p,sync,%p"
+ "Handle_SatEvt_SmSatIdListReport"
+ "Handle_SatRpt_TrkGridMsmt"
+ "Handle_Utils_Health_Eram_Profile"
+ "Jun 26 2026, 22:15:22"
+ "MAX_HDGPS_SUPPORT_LEN"
+ "MAX_NB_OF_HIST_BINS"
+ "OOB reset: %s (%u) >= %s (%u); resetting to 0 [%s:%u]\n"
+ "Out-of-bounds: %s (%u) >= %s (%u); rejecting [%s:%u]\n"
+ "_DIM(m_otRawdata.u.sSearch.satrpt_search)"
+ "bytes"
+ "cpu_clock"
+ "dc_idle_clock"
+ "dsp_clock"
+ "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_A8@$Change: 668937 $"
+ "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_B0@$Change: 668937 $"
+ "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_FE@$Change: 668937 $"
+ "fftd,recordIQ,sendStart,failed"
+ "fmh,StartRequest,request,%p,%d,pf,%p,sync,%p"
+ "idle_clock"
+ "ionexHdr.ulNumBlocks"
+ "m_pAsicConfigIfc->GetMaxNumSats()"
+ "m_ucMaxNumSatChn"
+ "m_ucNbHistBins"
+ "m_ucPrebitFllBestPhase"
+ "m_uiMaxOffset"
+ "m_usNumOfSbasAlm"
+ "num"
+ "num_words"
+ "readRecord"
+ "startRequest"
+ "static_cast<GlIntU32>(sizeof(bn->digit) + 1)"
+ "static_cast<GlIntU8>(_DIM(ST_GRID_CONTEXT::ast4779Band5GridNoiseTbl) - 1)"
+ "static_cast<GlIntU8>(_DIM(ST_GRID_CONTEXT::astBand5GridNoiseTbl) - 1)"
+ "static_cast<GlIntU8>(_DIM(ST_GRID_CONTEXT::astCalculatedGridNoise[0]) - 1)"
+ "static_cast<GlIntU8>(_DIM(fDspLUTmW_esw4) - 1)"
+ "static_cast<GlIntU8>(_DIM(fEcpuIdleLUTmW_esw4) - 1)"
+ "static_cast<GlIntU8>(_DIM(fEcpuOnLUTmW_esw4) - 1)"
+ "static_cast<uint8>(RM_REPORT_SIZE) + 1u"
+ "static_cast<uint8>(_DIM(m_rAsicInit.m_uRpcResponse.stReadResponse.ulValue))"
+ "ucEramSft"
+ "ucGridCoh"
+ "ucSatId"
+ "ucSatid"
+ "uiEnd"
+ "uiNsearchReportCnt"
+ "ulTotalLength"
+ "usLowTowNumWords"
+ "usNumSymInMsmtInt"
+ "usNumWords"
+ "usWordsNeeded"
- "#fmh,eraseRequest,request,%p,%d,size,%zu"
- "#fmh,startRequest,%p,%d,alreadyExist"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/FIREGPS9/proprietary/deliverables/gll_dev/gldebug/src/gldebug_glpeif.cpp:389"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/FIREGPS9/proprietary/deliverables/gll_dev/gldebug/src/gldebug_glpeif.cpp:483"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/FIREGPS9/proprietary/deliverables/gll_dev/gldebug/src/gldebug_glpeif.cpp:855"
- "@(#)Broadcom GLL ver. 170.20.28 667335, 2026/Jun/05, 14:46:17, build_job_id:__BUILDJOBID__, %s://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/...\n"
- "ChipData_GRABSNQ_667335"
- "EngineAlreadyInRun,engine,%p,reqSize,%zu"
- "FIRE@24 GLL@667335"
- "GL_NMEA"
- "GlMeSrdBitHistBuf"
- "GlReqOnStart,request,ok,%p,size,%zu"
- "Jun 15 2026, 23:59:02"
- "Mcu_EswLoadSetMcuData"
- "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_A8@$Change: 667311 $"
- "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_B0@$Change: 667311 $"
- "esw_gll_patch_generator.py:://depot/client/core/rel/Olympic/OSX_20.28.658483.v9.0/proprietary/deliverables/esw5_dev:LOX_FE@$Change: 667311 $"
- "fmh,StartRequest,request,%p,%d,size,%zu"

```
