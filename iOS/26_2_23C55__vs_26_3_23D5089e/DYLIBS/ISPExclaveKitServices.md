## ISPExclaveKitServices

> `/System/Library/PrivateFrameworks/ISPExclaveKitServices.framework/ISPExclaveKitServices`

```diff

-4.211.5.0.0
-  __TEXT.__text: 0x210f0
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x564
-  __TEXT.__oslogstring: 0x1f2a
-  __TEXT.__cstring: 0x3c6e
-  __TEXT.__unwind_info: 0x5d0
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xbd0
-  __AUTH_CONST.__auth_got: 0x2d0
-  __AUTH_CONST.__cfstring: 0x320
-  __DATA.__data: 0x1061b3
-  __DATA.__common: 0x9
+5.301.5.0.0
+  __TEXT.__text: 0x29328
+  __TEXT.__auth_stubs: 0x6e0
+  __TEXT.__const: 0x280
+  __TEXT.__gcc_except_tab: 0x6d4
+  __TEXT.__oslogstring: 0x2c87
+  __TEXT.__cstring: 0x49f0
+  __TEXT.__unwind_info: 0x730
+  __DATA_CONST.__got: 0x40
+  __DATA_CONST.__const: 0xeb0
+  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__const: 0x20
+  __AUTH_CONST.__cfstring: 0x340
+  __DATA.__data: 0x1163b9
+  __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 6685A7CD-6E3F-3E6F-A4A0-8D54CBBE02E5
-  Functions: 680
-  Symbols:   1562
-  CStrings:  410
+  UUID: F8036678-CC40-312B-A18B-C5390A5548EC
+  Functions: 840
+  Symbols:   1967
+  CStrings:  540
 
Symbols:
+ GCC_except_table11
+ GCC_except_table47
+ _FileServiceBufferName
+ _FileServiceBufferNameExtension
+ _MemoryReadOnlyRegionName
+ _MemoryReadOnlyRegionNameShort
+ _MemoryReadOnlyRegionSize
+ _MemoryWriteOnlyRegionName
+ _MemoryWriteOnlyRegionNameShort
+ _MemoryWriteOnlyRegionSize
+ __NSConcreteGlobalBlock
+ __Z12getFrameType28fidflowmodule_fidframetype_s
+ __Z13getStrobeType34ispexclavekitshared_ekstrobetype_s
+ __Z19getEngagementStatus47attentionawarenessmodule_userengagementstatus_s
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.48
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.49
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.50
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.51
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.52
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.53
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.54
+ __Z20ispExclaveKitCommandP20sExclaveKitIspCmdHdr.cold.55
+ __Z22decodeBufferDescriptorP32fidflowmodule_bufferdescriptor_sP16BufferDescriptor
+ __Z22exclaveKitDefaultsInitP21ISPExclaveKitDefaults.cold.2
+ __Z22getBufferChannelLayout29fidflowmodule_channellayout_s
+ __Z22getBufferElementFormat29fidflowmodule_elementformat_s
+ __Z28ispExclaveKitCommandChRunFidP20sExclaveKitIspCmdHdr
+ __Z28ispExclaveKitCommandChRunFidP20sExclaveKitIspCmdHdr.cold.1
+ __Z28ispExclaveKitCommandChRunFidP20sExclaveKitIspCmdHdr.cold.2
+ __Z28ispExclaveKitCommandChRunPceP20sExclaveKitIspCmdHdr
+ __Z28ispExclaveKitCommandChRunPceP20sExclaveKitIspCmdHdr.cold.1
+ __Z28ispExclaveKitCommandChRunPceP20sExclaveKitIspCmdHdr.cold.2
+ __Z29ispExclaveKitCommandChRunAdv2P20sExclaveKitIspCmdHdr.cold.3
+ __Z30ispExclaveKitCommandChRunStatsP20sExclaveKitIspCmdHdr
+ __Z30ispExclaveKitCommandChRunStatsP20sExclaveKitIspCmdHdr.cold.1
+ __Z30ispExclaveKitCommandChRunStatsP20sExclaveKitIspCmdHdr.cold.2
+ __Z32getMemoryReadOnlyRegionTypeIndexm
+ __Z32getMemoryReadOnlyRegionTypeIndexm.cold.1
+ __Z32ispExclavePrivatePropertiesResetv.cold.2
+ __Z32ispExclavePrivatePropertiesResetv.cold.3
+ __Z33getMemoryWriteOnlyRegionTypeIndexm26FileServiceBufferNameIndex
+ __Z33getMemoryWriteOnlyRegionTypeIndexm26FileServiceBufferNameIndex.cold.1
+ __Z33getMemoryWriteOnlyRegionTypeIndexm26FileServiceBufferNameIndex.cold.2
+ __Z33isDataCollectionBufferDumpEnabledP21ISPExclaveKitDefaults
+ __Z33ispExclaveKitCommandChFidGetStateP20sExclaveKitIspCmdHdr
+ __Z33ispExclaveKitCommandChFidGetStateP20sExclaveKitIspCmdHdr.cold.1
+ __Z38exclaveBufferInfoToFrameworkBufferInfo48ispexclavekitdebugmodule_debugbufferdescriptor_s
+ __Z38frameworkBufferInfoToExclaveBufferInfo21FileServiceBufferInfo
+ __Z38ispExclaveKitCommandChFidBufferReleaseP20sExclaveKitIspCmdHdr
+ __Z38ispExclaveKitCommandChFidBufferReleaseP20sExclaveKitIspCmdHdr.cold.1
+ __Z38ispExclaveKitCommandChFidBufferReleaseP20sExclaveKitIspCmdHdr.cold.2
+ __Z38ispExclaveKitCommandChFidBufferReleaseP20sExclaveKitIspCmdHdr.cold.3
+ __Z38ispExclaveKitCommandChFidBufferReleaseP20sExclaveKitIspCmdHdr.cold.4
+ __Z40frameworkBufferNameToTightbeamBufferName26FileServiceBufferNameIndex
+ __Z40frameworkBufferNameToTightbeamBufferName26FileServiceBufferNameIndex.cold.1
+ __Z40tightbeamBufferNameToFrameworkBufferName58ispexclavekitdebugmodule_debugbufferdescriptorbuffername_s
+ __Z40tightbeamBufferNameToFrameworkBufferName58ispexclavekitdebugmodule_debugbufferdescriptorbuffername_s.cold.1
+ __Z41isDataCollectionBufferDumpSkipCopyEnabledP21ISPExclaveKitDefaults
+ __Z41ispExclaveKitCommandChRunAeBracketCaptureP20sExclaveKitIspCmdHdr
+ __Z41ispExclaveKitCommandChRunAeBracketCaptureP20sExclaveKitIspCmdHdr.cold.1
+ __Z41ispExclaveKitCommandChRunAeBracketCaptureP20sExclaveKitIspCmdHdr.cold.2
+ __Z44ispExclaveKitCommandChRunMLGlobalToneMappingP20sExclaveKitIspCmdHdr
+ __Z44ispExclaveKitCommandChRunMLGlobalToneMappingP20sExclaveKitIspCmdHdr.cold.1
+ __Z44ispExclaveKitCommandChRunMLGlobalToneMappingP20sExclaveKitIspCmdHdr.cold.2
+ __Z45ispExclaveKitCommandChAeInitBracketSettingGetP20sExclaveKitIspCmdHdr
+ __Z45ispExclaveKitCommandChAeInitBracketSettingGetP20sExclaveKitIspCmdHdr.cold.1
+ __Z45ispExclaveKitCommandChAeInitBracketSettingGetP20sExclaveKitIspCmdHdr.cold.2
+ __Z45ispExclaveKitCommandChDataCollectionBufferGetP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService
+ __Z45ispExclaveKitCommandChDataCollectionBufferGetP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService.cold.1
+ __Z45ispExclaveKitCommandChDataCollectionBufferGetP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService.cold.2
+ __Z45ispExclaveKitCommandChDataCollectionBufferGetP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService.cold.3
+ __Z48_dataCollectionBufferTypeToFileServiceBufferName24DataCollectionBufferTypeP28ISPExclaveKitFileDumpService
+ __Z48_dataCollectionBufferTypeToFileServiceBufferName24DataCollectionBufferTypeP28ISPExclaveKitFileDumpService.cold.1
+ __Z48_dataCollectionBufferTypeToFileServiceBufferName24DataCollectionBufferTypeP28ISPExclaveKitFileDumpService.cold.2
+ __Z49ispExclaveKitCommandChDataCollectionBufferInfoGetP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService
+ __Z49ispExclaveKitCommandChDataCollectionBufferInfoGetP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService.cold.1
+ __Z49ispExclaveKitCommandChDataCollectionBufferInfoGetP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService.cold.2
+ __Z49ispExclaveKitCommandChDataCollectionBufferInfoGetP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService.cold.3
+ __ZN28ISPExclaveKitFileDumpService11_dumpBufferEP21FileServiceBufferInfo
+ __ZN28ISPExclaveKitFileDumpService11_dumpBufferEP21FileServiceBufferInfo.cold.1
+ __ZN28ISPExclaveKitFileDumpService11_dumpBufferEP21FileServiceBufferInfo.cold.2
+ __ZN28ISPExclaveKitFileDumpService11_dumpBufferEP21FileServiceBufferInfo.cold.3
+ __ZN28ISPExclaveKitFileDumpService11_dumpBufferEP21FileServiceBufferInfo.cold.4
+ __ZN28ISPExclaveKitFileDumpService11_dumpBufferEP21FileServiceBufferInfo.cold.5
+ __ZN28ISPExclaveKitFileDumpService14_copyoutBufferEP21FileServiceBufferInfo
+ __ZN28ISPExclaveKitFileDumpService14_copyoutBufferEP21FileServiceBufferInfo.cold.1
+ __ZN28ISPExclaveKitFileDumpService14_copyoutBufferEP21FileServiceBufferInfo.cold.2
+ __ZN28ISPExclaveKitFileDumpService14_copyoutBufferEP21FileServiceBufferInfo.cold.3
+ __ZN28ISPExclaveKitFileDumpService14_copyoutBufferEP21FileServiceBufferInfo.cold.4
+ __ZN28ISPExclaveKitFileDumpService14_copyoutBufferEP21FileServiceBufferInfo.cold.5
+ __ZN28ISPExclaveKitFileDumpService14_copyoutBufferEP21FileServiceBufferInfo.cold.6
+ __ZN28ISPExclaveKitFileDumpService14_copyoutBufferEP21FileServiceBufferInfo.cold.7
+ __ZN28ISPExclaveKitFileDumpService14_copyoutBufferEP21FileServiceBufferInfo.cold.8
+ __ZN28ISPExclaveKitFileDumpService14_copyoutBufferEP21FileServiceBufferInfo.cold.9
+ __ZN28ISPExclaveKitFileDumpService16_spawnDumpThreadEv
+ __ZN28ISPExclaveKitFileDumpService17dumpOneBufferSyncEP21FileServiceBufferInfo
+ __ZN28ISPExclaveKitFileDumpService17dumpOneBufferSyncEP21FileServiceBufferInfo.cold.1
+ __ZN28ISPExclaveKitFileDumpService17dumpOneBufferSyncEP21FileServiceBufferInfo.cold.2
+ __ZN28ISPExclaveKitFileDumpService18dumpOneBufferAsyncEP21FileServiceBufferInfo
+ __ZN28ISPExclaveKitFileDumpService18dumpOneBufferAsyncEP21FileServiceBufferInfo.cold.1
+ __ZN28ISPExclaveKitFileDumpService18dumpOneBufferAsyncEP21FileServiceBufferInfo.cold.2
+ __ZN28ISPExclaveKitFileDumpService4stopEv
+ __ZN28ISPExclaveKitFileDumpServiceC1Ebb
+ __ZN28ISPExclaveKitFileDumpServiceC2Ebb
+ __ZN28ISPExclaveKitFileDumpServiceC2Ebb.cold.1
+ __ZN28ISPExclaveKitFileDumpServiceC2Ebb.cold.2
+ __ZN28ISPExclaveKitFileDumpServiceD1Ev
+ __ZN28ISPExclaveKitFileDumpServiceD2Ev
+ __ZN28ISPExclaveKitFileServiceBase10_resetFifoEv
+ __ZN28ISPExclaveKitFileServiceBase11getFifoSizeEv
+ __ZN28ISPExclaveKitFileServiceBase12_printBufferEPhm
+ __ZN28ISPExclaveKitFileServiceBase19_resetBufferCounterEv
+ __ZN28ISPExclaveKitFileServiceBase27getBufferAvailableInExclaveE26FileServiceBufferNameIndex
+ __ZN28ISPExclaveKitFileServiceBase30_resetBufferAvailableInExclaveEv
+ __ZN28ISPExclaveKitFileServiceBase30updateBufferAvailableInExclaveE26FileServiceBufferNameIndexb
+ __ZN28ISPExclaveKitFileServiceBase35bufferAvailableInExclaveSanityCheckEv
+ __ZN28ISPExclaveKitFileServiceBase35bufferAvailableInExclaveSanityCheckEv.cold.1
+ __ZN28ISPExclaveKitFileServiceBaseC1Ebb
+ __ZN28ISPExclaveKitFileServiceBaseC2Ebb
+ __ZN28ISPExclaveKitFileServiceBaseD1Ev
+ __ZN28ISPExclaveKitFileServiceBaseD2Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZNSt3__114__split_bufferIP21FileServiceBufferInfoNS_9allocatorIS2_EEE12emplace_backIJRS2_EEEvDpOT_
+ __ZNSt3__114__split_bufferIP21FileServiceBufferInfoNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_
+ __ZNSt3__114__split_bufferIP21FileServiceBufferInfoNS_9allocatorIS2_EEE13emplace_frontIJS2_EEEvDpOT_
+ __ZNSt3__114__split_bufferIP21FileServiceBufferInfoNS_9allocatorIS2_EEED2Ev
+ __ZNSt3__114__split_bufferIP21FileServiceBufferInfoRNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_
+ __ZNSt3__114__split_bufferIP21FileServiceBufferInfoRNS_9allocatorIS2_EEE13emplace_frontIJRS2_EEEvDpOT_
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIP21FileServiceBufferInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__15dequeI21FileServiceBufferInfoNS_9allocatorIS1_EEE19__add_back_capacityEv
+ __ZNSt3__15dequeI21FileServiceBufferInfoNS_9allocatorIS1_EEE26__maybe_remove_front_spareB8ne200100Eb
+ __ZNSt3__15dequeI21FileServiceBufferInfoNS_9allocatorIS1_EEE9push_backERKS1_
+ __ZNSt3__15dequeI21FileServiceBufferInfoNS_9allocatorIS1_EEED2B8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTISt20bad_array_new_length
+ __ZdlPv
+ ___Block_byref_object_copy_.12
+ ___Block_byref_object_copy_.16
+ ___Block_byref_object_copy_.19
+ ___Block_byref_object_copy_.20
+ ___Block_byref_object_copy_.23
+ ___Block_byref_object_copy_.24
+ ___Block_byref_object_copy_.28
+ ___Block_byref_object_copy_.32
+ ___Block_byref_object_copy_.36
+ ___Block_byref_object_copy_.40
+ ___Block_byref_object_copy_.7
+ ___Block_byref_object_dispose_.13
+ ___Block_byref_object_dispose_.17
+ ___Block_byref_object_dispose_.20
+ ___Block_byref_object_dispose_.21
+ ___Block_byref_object_dispose_.24
+ ___Block_byref_object_dispose_.25
+ ___Block_byref_object_dispose_.29
+ ___Block_byref_object_dispose_.33
+ ___Block_byref_object_dispose_.37
+ ___Block_byref_object_dispose_.41
+ ___Block_byref_object_dispose_.8
+ ____Z28ispExclaveKitCommandChRunPceP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z30ispExclaveKitCommandChRunStatsP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z38ispExclaveKitCommandChFidBufferReleaseP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z41ispExclaveKitCommandChRunAeBracketCaptureP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z41ispExclaveKitCommandChRunAeBracketCaptureP20sExclaveKitIspCmdHdr_block_invoke_2
+ ____Z44ispExclaveKitCommandChRunMLGlobalToneMappingP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z45ispExclaveKitCommandChAeInitBracketSettingGetP20sExclaveKitIspCmdHdr_block_invoke
+ ____Z45ispExclaveKitCommandChAeInitBracketSettingGetP20sExclaveKitIspCmdHdr_block_invoke_2
+ ____Z45ispExclaveKitCommandChDataCollectionBufferGetP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService_block_invoke
+ ____Z49ispExclaveKitCommandChDataCollectionBufferInfoGetP20sExclaveKitIspCmdHdrP28ISPExclaveKitFileDumpService_block_invoke
+ ____ZN28ISPExclaveKitFileDumpService16_spawnDumpThreadEv_block_invoke
+ ____ZN28ISPExclaveKitFileDumpService16_spawnDumpThreadEv_block_invoke.3
+ ____ZN28ISPExclaveKitFileDumpService16_spawnDumpThreadEv_block_invoke.cold.1
+ ____ZN28ISPExclaveKitFileDumpService18dumpOneBufferAsyncEP21FileServiceBufferInfo_block_invoke
+ ____ZN28ISPExclaveKitFileServiceBase10_resetFifoEv_block_invoke
+ ____ZN28ISPExclaveKitFileServiceBase11getFifoSizeEv_block_invoke
+ ____ZN28ISPExclaveKitFileServiceBaseD2Ev_block_invoke
+ ___autoexposuremodule_ekautoexposurebracketsetting__v_decode_block_invoke
+ ___autoexposuremodule_ekautoexposurebracketsetting__v_visit_block_invoke
+ ___block_descriptor_tmp.10
+ ___block_descriptor_tmp.11
+ ___block_descriptor_tmp.15
+ ___block_descriptor_tmp.19
+ ___block_descriptor_tmp.22
+ ___block_descriptor_tmp.23
+ ___block_descriptor_tmp.26
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.309
+ ___block_descriptor_tmp.31
+ ___block_descriptor_tmp.313
+ ___block_descriptor_tmp.35
+ ___block_descriptor_tmp.39
+ ___block_descriptor_tmp.43
+ ___block_descriptor_tmp.6
+ ___block_descriptor_tmp.650
+ ___block_descriptor_tmp.719
+ ___block_descriptor_tmp.720
+ ___block_literal_global
+ ___cxa_allocate_exception
+ ___cxa_throw
+ _attentionawarenessmodule_ekattentionawareness_channelrunpce
+ _attentionawarenessmodule_ekattentionawareness_channelrunpce__result_get_success
+ _autoexposuremodule_ekautoexposure_channelautoexposureinitbracketsettingsget
+ _autoexposuremodule_ekautoexposure_channelautoexposureinitbracketsettingsget__result_get_success
+ _autoexposuremodule_ekautoexposure_channelrunautoexposurebracketcapture
+ _autoexposuremodule_ekautoexposure_channelrunautoexposurebracketcapture__result_get_success
+ _autoexposuremodule_ekautoexposurebracketsetting__decode
+ _autoexposuremodule_ekautoexposurebracketsetting__decode.cold.1
+ _autoexposuremodule_ekautoexposurebracketsetting__decode.cold.2
+ _autoexposuremodule_ekautoexposurebracketsetting__decode.cold.3
+ _autoexposuremodule_ekautoexposurebracketsetting__v_visit
+ _autoexposuremodule_ekautoexposurebracketsetting__v_visit.cold.1
+ _autoexposuremodule_ekautoexposurebracketsetting__v_visit.cold.2
+ _autoexposuremodule_ekautoexposurebracketsetting__v_visit.cold.3
+ _autoexposuremodule_ekbracketautoexposureresult__decode
+ _close
+ _dirname
+ _dispatch_async
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_sync
+ _exclaves_outbound_buffer_copyout
+ _exclaves_outbound_buffer_create
+ _fidflowmodule_ekfidflow_channelfidbufferrelease
+ _fidflowmodule_ekfidflow_channelrunattentiondetectv2.cold.1
+ _fidflowmodule_ekfidflow_channelrunattentiondetectv2.cold.2
+ _fidflowmodule_ekfidflow_channelrunattentiondetectv2.cold.3
+ _free
+ _ispexclavekitdebugmodule_ekchanneldebugbuffergetoutput__decode
+ _ispexclavekitdebugmodule_ekchanneldebugbufferinfogetoutput__decode
+ _ispexclavekitdebugmodule_ekchanneldebugbufferinfogetoutput__decode.cold.1
+ _ispexclavekitdebugmodule_ekdebug_channeldatacollectionbufferget
+ _ispexclavekitdebugmodule_ekdebug_channeldatacollectionbufferget.cold.1
+ _ispexclavekitdebugmodule_ekdebug_channeldatacollectionbufferinfoget
+ _ispexclavekitdebugmodule_ekdebug_channeldatacollectionbufferinfoget.cold.1
+ _ispexclavekitshared_ekispmanager_channelrunmlglobaltonemapping
+ _ispexclavekitshared_ekispmanager_channelrunmlglobaltonemapping__result_get_failure
+ _ispexclavekitshared_ekispmanager_channelrunstatsmanager
+ _ispexclavekitshared_ekispmanager_channelrunstatsmanager__result_get_failure
+ _malloc_type_malloc
+ _memmove
+ _mkpath_np
+ _motiontowakemodule_ekmotiontowake_channelrunmotiondetect__result_get_success
+ _open
+ _pFileDumpServiceSynced
+ _snprintf
+ _strcat
+ _write
- GCC_except_table13
- GCC_except_table17
- GCC_except_table21
- GCC_except_table29
- GCC_except_table33
- GCC_except_table37
- __Z29ispExclaveKitCommandChRunAndkP20sExclaveKitIspCmdHdr.cold.3
- __Z32ispExclaveKitCommandChAlgoEnableP20sExclaveKitIspCmdHdr.cold.32
- __Z32ispExclaveKitCommandChAlgoEnableP20sExclaveKitIspCmdHdr.cold.33
- __ZL19getEngagementStatus47attentionawarenessmodule_userengagementstatus_s
- __ZL22decodeBufferDescriptorP32fidflowmodule_bufferdescriptor_sP16BufferDescriptor
- ____Z29ispExclaveKitCommandChRunAndkP20sExclaveKitIspCmdHdr_block_invoke
- ___block_descriptor_tmp.198
- ___block_descriptor_tmp.205
- ___block_descriptor_tmp.620
- ___block_descriptor_tmp.621
- _andkmodule_ekandk__init
- _andkmodule_ekandk_runandk
- _andkmodule_ekandk_runandk__result_get_failure
- _fidflowmodule_attentiondetectresultv2__decode
- _fidflowmodule_attentiondetectresultv2__decode.cold.1
- _fidflowmodule_attentiondetectresultv2__decode.cold.2
- _fidflowmodule_attentiondetectresultv2__decode.cold.3
CStrings:
+ "%s:%d - ADResultV2: pCmdEKIspAD->result.frameInfo.rawFrame.bufferId: %llu\n"
+ "%s:%d - ERROR: AE Bracket Capture TB cmd failed for ch:%d\n"
+ "%s:%d - ERROR: Channel camera configuration being set doesn't match with the data received from EK configIndex = %d\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_IDL_CALL_FAIL, chIdx: %d\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_INPUT, chIdx: %d\n"
+ "%s:%d - ERROR: ISP_EXCLAVEKIT_CMD_HANDLER_ERR_WRONG_OUTPUT\n"
+ "%s:%d - ERROR: Invalid input for Run AE cmd, ch:%d\n"
+ "%s:%d - ERROR: Run Auto Exposure TB Cmd failed for ch:%d\n"
+ "%s:%d - ERROR: Unsupported platform!\n"
+ "%s:%d - ERROR: Wrong input for init bracket settings AE cmd\n"
+ "%s:%d - ERROR: wrong input for cmd ispExclaveKitCommandChRunAeBracketCapture, chIDx: %d\n"
+ "%s:%d - Expected values: %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u\n"
+ "%s:%d - FidGetState\n"
+ "%s:%d - ISP_EXCLAVEKIT_CMD_CH_DATA_COLLECTION_BUFFER_GET\n"
+ "%s:%d - ISP_EXCLAVEKIT_CMD_CH_DATA_COLLECTION_BUFFER_INFO_GET\n"
+ "%s:%d - Received values: %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u %u\n"
+ "%s:%d - Started and waiting for incoming buffer dumping request...\n"
+ "%s:%d - [EK] buffer copy time: %lld us, size=%ld, bufferName=%d\n"
+ "%s:%d - [EK] dumpBufferInfo: offset=%ld\n"
+ "%s:%d - [EK] dumpBufferInfo: regionType=%d\n"
+ "%s:%d - [EK] dumpBufferInfo: regionType=%s\n"
+ "%s:%d - [EK] dumpBufferInfo: size=%ld\n"
+ "%s:%d - [EK] dumped buffer full name: %s\n"
+ "%s:%d - [EK] dumped buffer name: %s\n"
+ "%s:%d - [EK] failed on creating path\n"
+ "%s:%d - [EK] failed on open file\n"
+ "%s:%d - [EK] failed on writing to file: write size=%ld, original size=%ld\n"
+ "%s:%d - [EK] incoming buffer size larger than local temp buffer size=%ld\n"
+ "%s:%d - [FileService] buffer[%d]=0x%x\n"
+ "%s:%d - [IR-EK] Attention Detection V2 Buffer offset raw %llu meta %llu ref %llu \n"
+ "%s:%d - [IR-EK] PCEMgr Finished\n"
+ "%s:%d - [IR-EK] Run PCEMgr\n"
+ "%s:%d - _isMemoryPortCreated is false\n"
+ "%s:%d - async server receives sync'ed request\n"
+ "%s:%d - creating shared memory region: %s done\n"
+ "%s:%d - creating shared memory region: %s failed with err: %d\n"
+ "%s:%d - currently only support one RAW buffer case, SIF and FEP RAW can not both available\n"
+ "%s:%d - dataCollectionBufferDumpEnabled=%d\n"
+ "%s:%d - dumpOneBufferAsync\n"
+ "%s:%d - dumpOneBufferSync\n"
+ "%s:%d - exclaves_outbound_buffer_copyout failed with err: %d\n"
+ "%s:%d - if both FEP and SIF RAW not available, user should not ask for it\n"
+ "%s:%d - illegal dataCollectionBufferType: %d\n"
+ "%s:%d - in release mode, ISP_EXCLAVEKIT_CMD_CH_DATA_COLLECTION_BUFFER_GET is not available\n"
+ "%s:%d - in release mode, ISP_EXCLAVEKIT_CMD_CH_DATA_COLLECTION_BUFFER_INFO_GET is not available\n"
+ "%s:%d - index: %zu - after create\n"
+ "%s:%d - index: %zu - before create\n"
+ "%s:%d - invalid buffer name: %d\n"
+ "%s:%d - invalid buffer name: %llu\n"
+ "%s:%d - invalid buffer type: %d\n"
+ "%s:%d - invalid channel index %zu\n"
+ "%s:%d - invalid input buffer size: input buffer size: %llu, EK buffer size: %zu\n"
+ "%s:%d - isAsync=%d, needDiskAccess=%d\n"
+ "%s:%d - isDataCollectionBufferDumpEnabled=%d\n"
+ "%s:%d - isDataCollectionBufferDumpSkipCopyEnabled=%d\n"
+ "%s:%d - main thread exist....\n"
+ "%s:%d - no input buffer dest, _pLocalTempBuffer can not be null\n"
+ "%s:%d - pCmdEKIspAD->result.frameInfo.rawFrame.bufferId: %llu\n"
+ "%s:%d - pFileDumpService not available\n"
+ "%s:%d - pFileDumpServiceSynced is nil, dumpEnabled=%d, dumpSkipCopyEnabled=%d\n"
+ "%s:%d - pixel format not supported: %d\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_FID_BUFFER_RELEASE!\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_FID_GET_STATE!\n"
+ "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_RUN_FID!\n"
+ "%s:%d - run PCE \n"
+ "%s:%d - skip copy is enabled, output buffer should not be written\n"
+ "%s:%d - sync'ed server receives async request\n"
+ "%s:%d - tb_res->value.success.frameinfo.rawframe.bufferid: %llu\n"
+ "%s:%d - write only total: %d, total: %d\n"
+ "%s_%s_%zu.%s"
+ "/private/var/mobile/Media/DCIM/"
+ "ISPExclaveKitCmdHandlerChDebug.cpp"
+ "ISPExclaveKitFileDumpService"
+ "ISPExclaveKitFileDumpService.cpp"
+ "ISPExclaveKitFileServiceBase.cpp"
+ "ISPExclaveKitFileServiceCommon.cpp"
+ "ISP_EXCLAVEKIT_CMD_CH_DATA_COLLECTION_BUFFER_GET"
+ "ISP_EXCLAVEKIT_CMD_CH_DATA_COLLECTION_BUFFER_INFO_GET"
+ "ISP_EXCLAVEKIT_CMD_CH_FID_GET_STATE"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_FID"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_MLGLOBALTONEMAPPING"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_PCE"
+ "ISP_EXCLAVEKIT_CMD_CH_RUN_STATS"
+ "_copyoutBuffer"
+ "_dataCollectionBufferTypeToFileServiceBufferName"
+ "_dumpBuffer"
+ "_printBuffer"
+ "_spawnDumpThread_block_invoke"
+ "_spawnDumpThread_block_invoke_2"
+ "bufferAvailableInExclaveSanityCheck"
+ "com.apple.cameracaptured.SharedMemIR"
+ "com.apple.cameracaptured.SharedMemIRCopyin"
+ "com.apple.cameracaptured.SharedMemRGBNRT"
+ "com.apple.cameracaptured.SharedMemRGBRT"
+ "com.ispexclavekit.fileservice.sync"
+ "com.ispexclavekit.fileservice.work"
+ "dataCollectionBufferDumpEnabled"
+ "decodeAAResultV2"
+ "dumpOneBufferAsync"
+ "dumpOneBufferSync"
+ "fep_output"
+ "frameworkBufferNameToTightbeamBufferName"
+ "getMemoryReadOnlyRegionTypeIndex"
+ "getMemoryWriteOnlyRegionTypeIndex"
+ "hostmetadata_output"
+ "ir"
+ "irReadonly"
+ "ispExclaveKitCommandChAeInitBracketSettingGet"
+ "ispExclaveKitCommandChDataCollectionBufferGet"
+ "ispExclaveKitCommandChDataCollectionBufferInfoGet"
+ "ispExclaveKitCommandChFidBufferRelease"
+ "ispExclaveKitCommandChFidGetState"
+ "ispExclaveKitCommandChRunAeBracketCapture"
+ "ispExclaveKitCommandChRunFid"
+ "ispExclaveKitCommandChRunMLGlobalToneMapping"
+ "ispExclaveKitCommandChRunPce"
+ "ispExclaveKitCommandChRunStats"
+ "meta"
+ "raw"
+ "rgbnrt"
+ "rgbrt"
+ "sif_output"
+ "tightbeamBufferNameToFrameworkBufferName"
+ "v104@?0{ispexclavekitshared_ekispmanager_channelcameraconfigurationget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitshared_ekchannelcameraconfiguration_s=ISSSSIISICSIIISSIIIIIIIII})}8"
+ "v24@?0Q8r^{autoexposuremodule_ekautoexposurebracketsetting_s=IIIIIIIffIIfICCC}16"
+ "v24@?0{attentionawarenessmodule_ekattentionawareness_channelrunpce__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}B)}8"
+ "v24@?0{fidflowmodule_ekfidflow_channelfidbufferrelease__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekitshared_ekispmanager_channelrunmlglobaltonemapping__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v24@?0{ispexclavekitshared_ekispmanager_channelrunstatsmanager__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
+ "v40@?0{ispexclavekitdebugmodule_ekdebug_channeldatacollectionbufferinfoget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitdebugmodule_ekchanneldebugbufferinfogetoutput_s=BIIII})}8"
+ "v64@?0{ispexclavekitdebugmodule_ekdebug_channeldatacollectionbufferget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitdebugmodule_ekchanneldebugbuffergetoutput_s={ispexclavekitdebugmodule_debugbufferdescriptor_s={ispexclavekitdebugmodule_debugbufferdescriptorbuffername_s=Q}QQ{ispexclavekitdebugmodule_debugbufferdescriptorbufferstatus_s=Q}QQ}})}8"
+ "v96@?0{autoexposuremodule_ekautoexposure_channelautoexposureinitbracketsettingsget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{autoexposuremodule_ekbracketautoexposureresult_s=IIQ{exclavesispshared_exclavesispresultcommon_s=QB}{autoexposuremodule_ekautoexposurebracketsetting_v_s=C(?={?=^{autoexposuremodule_ekautoexposurebracketsetting_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}B})}8"
+ "v96@?0{autoexposuremodule_ekautoexposure_channelrunautoexposurebracketcapture__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{autoexposuremodule_ekbracketautoexposureresult_s=IIQ{exclavesispshared_exclavesispresultcommon_s=QB}{autoexposuremodule_ekautoexposurebracketsetting_v_s=C(?={?=^{autoexposuremodule_ekautoexposurebracketsetting_s}Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}B})}8"
+ "vispipe_output"
+ "yuv"
- "%s:%d - ERROR: Channel camera configuration being set doesn't match with the data received from EK\n"
- "%s:%d - ISP_EXCLAVE_KIT_SERVICE_TYPE_ANDK handler is created\n"
- "%s:%d - [Conclave] (EKType:%d) Failed to setup ANDK client\n\n"
- "%s:%d - run ISP_EXCLAVEKIT_CMD_CH_FID_BUFFER_RELEASE! - do nothing now!\n"
- "v24@?0{andkmodule_ekandk_runandk__result_s=C(?={exclavesispshared_exclavesisperror_s=Q})}8"
- "v88@?0{ispexclavekitshared_ekispmanager_channelcameraconfigurationget__result_s=C(?={exclavesispshared_exclavesisperror_s=Q}{ispexclavekitshared_ekchannelcameraconfiguration_s=ISSSSIISICSIIISSIIIII})}8"

```
