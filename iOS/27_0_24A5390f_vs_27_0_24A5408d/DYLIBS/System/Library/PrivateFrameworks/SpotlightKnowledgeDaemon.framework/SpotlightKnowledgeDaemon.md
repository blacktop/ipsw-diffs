## SpotlightKnowledgeDaemon

> `/System/Library/PrivateFrameworks/SpotlightKnowledgeDaemon.framework/SpotlightKnowledgeDaemon`

```diff

-2454.100.0.0.0
-  __TEXT.__text: 0x4659a8
-  __TEXT.__objc_methlist: 0x9918
-  __TEXT.__const: 0x16928
-  __TEXT.__oslogstring: 0x1132e
-  __TEXT.__cstring: 0x14613
-  __TEXT.__gcc_except_tab: 0x5a94
+2459.102.0.0.0
+  __TEXT.__text: 0x48acd0
+  __TEXT.__objc_methlist: 0x9968
+  __TEXT.__const: 0x17408
+  __TEXT.__oslogstring: 0x116be
+  __TEXT.__gcc_except_tab: 0x5aac
+  __TEXT.__cstring: 0x15963
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__swift5_typeref: 0xe528
-  __TEXT.__constg_swiftt: 0x89bc
+  __TEXT.__swift5_typeref: 0xe9a8
+  __TEXT.__constg_swiftt: 0x8dc0
   __TEXT.__swift5_builtin: 0x244
-  __TEXT.__swift5_reflstr: 0x82fd
-  __TEXT.__swift5_fieldmd: 0x88b8
+  __TEXT.__swift5_reflstr: 0x87ed
+  __TEXT.__swift5_fieldmd: 0x8d40
   __TEXT.__swift5_assocty: 0x1398
-  __TEXT.__swift5_capture: 0x3698
-  __TEXT.__swift5_proto: 0x1010
-  __TEXT.__swift5_types: 0x878
-  __TEXT.__swift_as_entry: 0x430
-  __TEXT.__swift_as_ret: 0x468
-  __TEXT.__swift_as_cont: 0x4ec
-  __TEXT.__swift5_protos: 0x268
+  __TEXT.__swift5_capture: 0x37e8
+  __TEXT.__swift5_proto: 0x107c
+  __TEXT.__swift5_types: 0x8bc
+  __TEXT.__swift_as_entry: 0x488
+  __TEXT.__swift_as_ret: 0x4d4
+  __TEXT.__swift_as_cont: 0x574
+  __TEXT.__swift5_protos: 0x274
   __TEXT.__swift5_mpenum: 0x94
-  __TEXT.__unwind_info: 0xc1e0
-  __TEXT.__eh_frame: 0x13618
+  __TEXT.__unwind_info: 0xc858
+  __TEXT.__eh_frame: 0x145a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x35b0
-  __DATA_CONST.__objc_classlist: 0x960
+  __DATA_CONST.__const: 0x35b8
+  __DATA_CONST.__objc_classlist: 0x970
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f48
+  __DATA_CONST.__objc_selrefs: 0x5f88
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x8a0
-  __DATA_CONST.__got: 0x2210
-  __AUTH_CONST.__const: 0x17ef8
-  __AUTH_CONST.__cfstring: 0x9400
-  __AUTH_CONST.__objc_const: 0x18478
+  __DATA_CONST.__got: 0x2260
+  __AUTH_CONST.__const: 0x18b30
+  __AUTH_CONST.__cfstring: 0x9420
+  __AUTH_CONST.__objc_const: 0x186f0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x9d8
   __AUTH_CONST.__objc_arrayobj: 0x5e8
   __AUTH_CONST.__objc_dictobj: 0x280
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x3680
-  __AUTH.__objc_data: 0x1738
-  __AUTH.__data: 0x2638
+  __AUTH_CONST.__auth_got: 0x36e8
+  __AUTH.__objc_data: 0x1788
+  __AUTH.__data: 0x2a28
   __DATA.__objc_ivar: 0xbd8
-  __DATA.__data: 0x35e8
-  __DATA.__bss: 0xedf0
-  __DATA.__common: 0x98
-  __DATA_DIRTY.__objc_data: 0x3ed8
-  __DATA_DIRTY.__data: 0xc328
+  __DATA.__data: 0x3a60
+  __DATA.__bss: 0xf900
+  __DATA.__common: 0xc0
+  __DATA_DIRTY.__objc_data: 0x3ef0
+  __DATA_DIRTY.__data: 0xc338
   __DATA_DIRTY.__bss: 0x8900
   __DATA_DIRTY.__common: 0x3a0
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/FileDerivatives.framework/FileDerivatives
   - /System/Library/PrivateFrameworks/GRDBInternal.framework/GRDBInternal
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
-  - /System/Library/PrivateFrameworks/GenerativeSearch.framework/GenerativeSearch
   - /System/Library/PrivateFrameworks/HybridSearch.framework/HybridSearch
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
   - /System/Library/PrivateFrameworks/IntelligencePlatformLibrary.framework/IntelligencePlatformLibrary

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 16148
-  Symbols:   14211
-  CStrings:  3605
+  Functions: 16549
+  Symbols:   14305
+  CStrings:  3672
 
Symbols:
+ -[SKDPipelineState _resetSerialsIfGenerationChanged:forPipeline:forIndexType:]
+ -[SKDPipelineState prioritySerialNumberForPipeline:indexType:]
+ -[SKDPipelineState setPrioritySerialNumber:forPipeline:forIndexType:]
+ -[SKDPipelineState setPrioritySerialNumber:journalCookie:forPipeline:forIndexType:]
+ -[SKDPipelineState(Internal) removePrioritySerialNumberForPipeline:forIndexType:]
+ __DATA__TtC24SpotlightKnowledgeDaemon24ScannedSerialAccumulator
+ __DATA__TtC24SpotlightKnowledgeDaemon34PipelineStateDeadReckoningRecorder
+ __IVARS__TtC24SpotlightKnowledgeDaemon24ScannedSerialAccumulator
+ __IVARS__TtC24SpotlightKnowledgeDaemon34PipelineStateDeadReckoningRecorder
+ __IVARS__TtC24SpotlightKnowledgeDaemon41PipelineStateTransitionLoggingMultiplexer
+ __METACLASS_DATA__TtC24SpotlightKnowledgeDaemon24ScannedSerialAccumulator
+ __METACLASS_DATA__TtC24SpotlightKnowledgeDaemon34PipelineStateDeadReckoningRecorder
+ ___swift__destructor.19Tm
+ ___swift_closure_destructor.119Tm
+ ___swift_closure_destructor.123Tm
+ ___swift_closure_destructor.162Tm
+ ___swift_closure_destructor.166Tm
+ ___swift_closure_destructor.180Tm
+ ___swift_closure_destructor.189Tm
+ ___swift_closure_destructor.19Tm
+ ___swift_closure_destructor.209Tm
+ ___swift_closure_destructor.266Tm
+ ___swift_closure_destructor.282Tm
+ ___swift_closure_destructor.293Tm
+ ___swift_closure_destructor.346Tm
+ ___swift_closure_destructor.34Tm
+ ___swift_closure_destructor.460Tm
+ ___swift_closure_destructor.562Tm
+ ___swift_closure_destructor.653Tm
+ ___swift_closure_destructor.69Tm
+ ___swift_closure_destructor.78Tm
+ ___swift_closure_destructor.7Tm
+ ___swift_exist.box.addr_destructor.57Tm
+ ___swift_exist.box.addr_destructor.666Tm
+ ___swift_exist.box.addr_destructor.671Tm
+ ___swift_exist.box.addr_destructor.737Tm
+ ___swift_memcpy156_8
+ ___unnamed_86
+ ___unnamed_87
+ ___unnamed_88
+ _associated conformance 24SpotlightKnowledgeDaemon10PipelineIDVSHAASQ
+ _associated conformance 24SpotlightKnowledgeDaemon10PipelineIDVSLAASQ
+ _associated conformance 24SpotlightKnowledgeDaemon10PipelineIDVs25LosslessStringConvertibleAAs06CustomgH0
+ _associated conformance 24SpotlightKnowledgeDaemon15DASFeatureFlagsOSHAASQ
+ _associated conformance 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLOSHAASQ
+ _associated conformance 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV3RowV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLOSHAASQ
+ _associated conformance 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV3RowV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV3RowV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 24SpotlightKnowledgeDaemon26PipelineProgressTimeWindowVSHAASQ
+ _associated conformance 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_A35D547553989C3894BDE2B07983E4B5LLOSHAASQ
+ _associated conformance 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_A35D547553989C3894BDE2B07983E4B5LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_A35D547553989C3894BDE2B07983E4B5LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _dlopen
+ _objc_msgSend$_resetSerialsIfGenerationChanged:forPipeline:forIndexType:
+ _objc_msgSend$isDASPhasedProcessingEnabled
+ _objc_msgSend$prioritySerialNumberForPipeline:indexType:
+ _objc_msgSend$removePrioritySerialNumberForPipeline:forIndexType:
+ _objc_msgSend$setPrimaryDomain:
+ _objc_msgSend$setPrioritySerialNumber:forPipeline:forIndexType:
+ _objc_msgSend$setPrioritySerialNumber:journalCookie:forPipeline:forIndexType:
+ _objc_msgSend$setPurpose:
+ _objc_msgSend$valueType
+ _symbolic $s24SpotlightKnowledgeDaemon26PipelineProgressEstimatingP
+ _symbolic $s24SpotlightKnowledgeDaemon26PipelineProgressPersistingP
+ _symbolic $s24SpotlightKnowledgeDaemon32PipelineCompletenessCoordinatingP
+ _symbolic BASSSg______pIeNghHTgILrzo_ s5ErrorP
+ _symbolic SDy_____SDy_____SDy__________GGG 24SpotlightKnowledgeDaemon26PipelineProgressTimeWindowV AA0D2IDV AA06BundleH0V AA0dE6CountsV
+ _symbolic SDy__________G 18SpotlightKnowledge9IndexTypeO 0aB6Daemon13ScannedSerialV
+ _symbolic SDy__________G 24SpotlightKnowledgeDaemon8BundleIDV AA16DonationSnapshotV
+ _symbolic SDy__________GIeAgHr_ 24SpotlightKnowledgeDaemon8BundleIDV AA16DonationSnapshotV
+ _symbolic SDy__________GSg 24SpotlightKnowledgeDaemon8BundleIDV AA16DonationSnapshotV
+ _symbolic Say_____G 24SpotlightKnowledgeDaemon21DestinationDescriptorV
+ _symbolic Say_____G 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV3RowV
+ _symbolic Say_____G 24SpotlightKnowledgeDaemon24PipelineMetricsAggregateV
+ _symbolic ScCySDy__________GSg_____G 24SpotlightKnowledgeDaemon8BundleIDV AA16DonationSnapshotV s5NeverO
+ _symbolic ScCySSSg_____G s5NeverO
+ _symbolic ScCySSSg______pG s5ErrorP
+ _symbolic ScCySSSg______pGSg s5ErrorP
+ _symbolic So20SKDCancellationTokenC_____Ieghg_Ieghgg_ 24SpotlightKnowledgeDaemon9SchedulerC9TaskStateO
+ _symbolic _____ 24SpotlightKnowledgeDaemon10PipelineIDV
+ _symbolic _____ 24SpotlightKnowledgeDaemon13ScannedSerialV
+ _symbolic _____ 24SpotlightKnowledgeDaemon15DASFeatureFlagsO
+ _symbolic _____ 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV
+ _symbolic _____ 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLO
+ _symbolic _____ 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV3RowV
+ _symbolic _____ 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV3RowV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLO
+ _symbolic _____ 24SpotlightKnowledgeDaemon22PipelineProgressCountsV
+ _symbolic _____ 24SpotlightKnowledgeDaemon23CascadeMetricsCollectorC0E11AggregationV
+ _symbolic _____ 24SpotlightKnowledgeDaemon24PipelineMetricsAggregateV
+ _symbolic _____ 24SpotlightKnowledgeDaemon24ScannedSerialAccumulatorC
+ _symbolic _____ 24SpotlightKnowledgeDaemon24TransitionLoggingContextV
+ _symbolic _____ 24SpotlightKnowledgeDaemon26PipelineProgressTimeWindowV
+ _symbolic _____ 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_A35D547553989C3894BDE2B07983E4B5LLO
+ _symbolic _____ 24SpotlightKnowledgeDaemon29FilePipelineProgressPersisterV
+ _symbolic _____ 24SpotlightKnowledgeDaemon33SettingsUIPipelineCompletenessJobC18FreshDonationCache33_F12AE226D200986B9BC282FED6F3D63ELLV
+ _symbolic _____ 24SpotlightKnowledgeDaemon34PipelineStateDeadReckoningRecorderC
+ _symbolic _____ 24SpotlightKnowledgeDaemon34PipelineStateDeadReckoningRecorderC0E033_44BE4499ADFAF1565E65DF7E76B11EAFLLV
+ _symbolic _____ 24SpotlightKnowledgeDaemon41PipelineStateTransitionLoggingMultiplexerC
+ _symbolic _____ 24SpotlightKnowledgeDaemon9SchedulerC18UnscheduleJobErrorV
+ _symbolic _____Ieghg_ 24SpotlightKnowledgeDaemon9SchedulerC4TaskC6ResultO
+ _symbolic _____Ieghg_ 24SpotlightKnowledgeDaemon9SchedulerC9TaskStateO
+ _symbolic _____Sg 24SpotlightKnowledgeDaemon13ScannedSerialV
+ _symbolic _____Sg 24SpotlightKnowledgeDaemon24TransitionLoggingContextV
+ _symbolic _____Sg 24SpotlightKnowledgeDaemon33SettingsUIPipelineCompletenessJobC18FreshDonationCache33_F12AE226D200986B9BC282FED6F3D63ELLV
+ _symbolic _____XDXMT 24SpotlightKnowledgeDaemon20CascadeProcessingJobC
+ _symbolic ___________pIeghrzo_ 18SpotlightKnowledge14UpdaterCommandO26FetchPipelineDeadReckoningV8ResponseV s5ErrorP
+ _symbolic ___________pIeghrzo_ 18SpotlightKnowledge14UpdaterCommandO26ResetPipelineDeadReckoningV8ResponseV s5ErrorP
+ _symbolic ___________t 18SpotlightKnowledge9IndexTypeO 0aB6Daemon13ScannedSerialV
+ _symbolic ___________t s5Int64V 12GRDBInternal3RowC
+ _symbolic ___________t s5Int64V 24SpotlightKnowledgeDaemon23CascadeMetricsCollectorC0F11AggregationV
+ _symbolic ______pSg 24SpotlightKnowledgeDaemon26PipelineProgressEstimatingP
+ _symbolic ______pSg 24SpotlightKnowledgeDaemon26PipelineProgressPersistingP
+ _symbolic ______pSg 24SpotlightKnowledgeDaemon32PipelineCompletenessCoordinatingP
+ _symbolic _____ySDy__________GG 15Synchronization5MutexVAARi_zrlE 18SpotlightKnowledge9IndexTypeO 0cD6Daemon13ScannedSerialV
+ _symbolic _____ySSSgG 24SpotlightKnowledgeDaemon15TimeoutExecutorC
+ _symbolic _____ySbG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____ySiSg_____G s18_DictionaryStorageC 24SpotlightKnowledgeDaemon26PipelineProgressTimeWindowV
+ _symbolic _____ySiSg______tG s23_ContiguousArrayStorageC 24SpotlightKnowledgeDaemon26PipelineProgressTimeWindowV
+ _symbolic _____y_____G 15Synchronization5MutexVAARi_zrlE 24SpotlightKnowledgeDaemon34PipelineStateDeadReckoningRecorderC0G033_44BE4499ADFAF1565E65DF7E76B11EAFLLV
+ _symbolic _____y_____G 15Synchronization5_CellVAARi_zrlE 24SpotlightKnowledgeDaemon34PipelineStateDeadReckoningRecorderC0G033_44BE4499ADFAF1565E65DF7E76B11EAFLLV
+ _symbolic _____y_____G s22KeyedDecodingContainerV 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV3RowV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_A35D547553989C3894BDE2B07983E4B5LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV3RowV10CodingKeys33_77A5220524D4D3A03A1C41EC8E837895LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_A35D547553989C3894BDE2B07983E4B5LLO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 18SpotlightKnowledge14UpdaterCommandO26FetchPipelineDeadReckoningV3RowV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 24SpotlightKnowledgeDaemon22PersistedDeadReckoningV3RowV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 24SpotlightKnowledgeDaemon24PipelineMetricsAggregateV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 24SpotlightKnowledgeDaemon26PipelineProgressTimeWindowV
+ _symbolic _____y_____SDy_____SDy__________GGG s18_DictionaryStorageC 24SpotlightKnowledgeDaemon26PipelineProgressTimeWindowV AC0F2IDV AC06BundleJ0V AC0fG6CountsV
+ _symbolic _____y_____SDy__________GG s18_DictionaryStorageC 24SpotlightKnowledgeDaemon10PipelineIDV AC06BundleG0V AC0F14ProgressCountsV
+ _symbolic _____y_____SgG 2os21OSAllocatedUnfairLockV 24SpotlightKnowledgeDaemon33SettingsUIPipelineCompletenessJobC18FreshDonationCache33_F12AE226D200986B9BC282FED6F3D63ELLV
+ _symbolic _____y_____Sg_____G s13ManagedBufferCsRi__rlE 24SpotlightKnowledgeDaemon33SettingsUIPipelineCompletenessJobC18FreshDonationCache33_F12AE226D200986B9BC282FED6F3D63ELLV So16os_unfair_lock_sV
+ _symbolic _____y__________G s18_DictionaryStorageC 18SpotlightKnowledge9IndexTypeO 0cD6Daemon13ScannedSerialV
+ _symbolic _____y__________G s18_DictionaryStorageC 24SpotlightKnowledgeDaemon8BundleIDV AC22PipelineProgressCountsV
+ _symbolic _____y__________G s18_DictionaryStorageC s5Int64V 12GRDBInternal3RowC
+ _symbolic _____y__________G s18_DictionaryStorageC s5Int64V 24SpotlightKnowledgeDaemon23CascadeMetricsCollectorC0H11AggregationV
+ _symbolic _____y___________G 18SpotlightKnowledge14UpdaterCommandO13CodableResultO AC26FetchPipelineDeadReckoningV8ResponseV AC0D5ErrorO
+ _symbolic _____y___________G 18SpotlightKnowledge14UpdaterCommandO13CodableResultO AC26ResetPipelineDeadReckoningV8ResponseV AC0D5ErrorO
+ _symbolic _____y___________GIeghn_ 18SpotlightKnowledge14UpdaterCommandO13CodableResultO AC26FetchPipelineDeadReckoningV8ResponseV AC0D5ErrorO
+ _symbolic _____y___________GIeghn_ 18SpotlightKnowledge14UpdaterCommandO13CodableResultO AC26ResetPipelineDeadReckoningV8ResponseV AC0D5ErrorO
+ _symbolic _____y___________QPG 24SpotlightKnowledgeDaemon41PipelineStateTransitionLoggingMultiplexerC AA0dE21DeadReckoningRecorderC AA0deF6LoggerC
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC s5Int64V 12GRDBInternal3RowC
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC s5Int64V 24SpotlightKnowledgeDaemon23CascadeMetricsCollectorC0I11AggregationV
- ___swift__destructor.9Tm
- ___swift_closure_destructor.116Tm
- ___swift_closure_destructor.11Tm
- ___swift_closure_destructor.122Tm
- ___swift_closure_destructor.161Tm
- ___swift_closure_destructor.165Tm
- ___swift_closure_destructor.167Tm
- ___swift_closure_destructor.170Tm
- ___swift_closure_destructor.179Tm
- ___swift_closure_destructor.183Tm
- ___swift_closure_destructor.22Tm
- ___swift_closure_destructor.245Tm
- ___swift_closure_destructor.261Tm
- ___swift_closure_destructor.264Tm
- ___swift_closure_destructor.273Tm
- ___swift_closure_destructor.321Tm
- ___swift_closure_destructor.410Tm
- ___swift_closure_destructor.44Tm
- ___swift_closure_destructor.550Tm
- ___swift_closure_destructor.57Tm
- ___swift_closure_destructor.626Tm
- ___swift_closure_destructor.66Tm
- ___swift_exist.box.addr_destructor.36Tm
- ___swift_exist.box.addr_destructor.636Tm
- ___swift_exist.box.addr_destructor.641Tm
- ___swift_exist.box.addr_destructor.695Tm
- ___unnamed_76
- ___unnamed_77
- ___unnamed_78
- _associated conformance 24SpotlightKnowledgeDaemon11MetricsItemVSHAASQ
- _associated conformance 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_9969AF35D243A68D3B15563CD6CAA9B1LLOSHAASQ
- _associated conformance 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_9969AF35D243A68D3B15563CD6CAA9B1LLOs0H3KeyAAs23CustomStringConvertible
- _associated conformance 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_9969AF35D243A68D3B15563CD6CAA9B1LLOs0H3KeyAAs28CustomDebugStringConvertible
- _associated conformance 24SpotlightKnowledgeDaemon9SchedulerC4TaskC6ResultOSHAASQ
- _associated conformance 24SpotlightKnowledgeDaemon9SchedulerC9TaskStateOSHAASQ
- _kCFPreferencesAnyHost
- _kCFPreferencesAnyUser
- _objc_msgSend$showRelatedContentIsEnabled
- _symbolic So20SKDCancellationTokenC_____Ieghy_Ieghgg_ 24SpotlightKnowledgeDaemon9SchedulerC9TaskStateO
- _symbolic _____ 24SpotlightKnowledgeDaemon11MetricsItemV
- _symbolic _____ 24SpotlightKnowledgeDaemon23CascadeMetricsCollectorC32generateDailyStatusForAllBundles3for10reportDate17cancellationTokenSayAA014PipelineBundleE0VGSS_10Foundation0O0VSgSo015SKDCancellationQ0CtYaKF0E11AggregationL_V
- _symbolic _____ 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_9969AF35D243A68D3B15563CD6CAA9B1LLO
- _symbolic _____Ieghy_ 24SpotlightKnowledgeDaemon9SchedulerC4TaskC6ResultO
- _symbolic _____Ieghy_ 24SpotlightKnowledgeDaemon9SchedulerC9TaskStateO
- _symbolic ___________t s5Int64V 24SpotlightKnowledgeDaemon23CascadeMetricsCollectorC32generateDailyStatusForAllBundles3for10reportDate17cancellationTokenSayAC014PipelineBundleF0VGSS_10Foundation0P0VSgSo015SKDCancellationR0CtYaKF0F11AggregationL_V
- _symbolic _____ySDy__________GSgG 2os21OSAllocatedUnfairLockV 24SpotlightKnowledgeDaemon8BundleIDV AD16DonationSnapshotV
- _symbolic _____ySDy__________GSg_____G s13ManagedBufferCsRi__rlE 24SpotlightKnowledgeDaemon8BundleIDV AC16DonationSnapshotV So16os_unfair_lock_sV
- _symbolic _____y_____G 24SpotlightKnowledgeDaemon18AsyncBatchSequenceV AA11MetricsItemV
- _symbolic _____y_____G s22KeyedDecodingContainerV 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_9969AF35D243A68D3B15563CD6CAA9B1LLO
- _symbolic _____y_____G s22KeyedEncodingContainerV 24SpotlightKnowledgeDaemon28PipelineStateTransitionEventV10CodingKeys33_9969AF35D243A68D3B15563CD6CAA9B1LLO
- _symbolic _____y_____G s23_ContiguousArrayStorageC 24SpotlightKnowledgeDaemon11MetricsItemV
- _symbolic _____y__________G s18_DictionaryStorageC s5Int64V 24SpotlightKnowledgeDaemon23CascadeMetricsCollectorC32generateDailyStatusForAllBundles3for10reportDate17cancellationTokenSayAE014PipelineBundleH0VGSS_10Foundation0R0VSgSo015SKDCancellationT0CtYaKF0H11AggregationL_V
- _symbolic _____y______pSg_____G s13ManagedBufferCsRi__rlE So14OS_os_activityP So0D14_unfair_lock_sV
CStrings:
+ " AND pi.processedVersion IS NULL "
+ " THEN 1 END)\nORDER BY pi.identityID\nLIMIT  :batchSize"
+ " run requires a matching recency on the pipeline descriptor"
+ "%s: Deleted %ld fully-confirmed items."
+ "%s: Deleting fully-confirmed items was interrupted; will retry on the next backlog run."
+ "%s: Deleting fully-confirmed items."
+ "%{public}s run for %{public}s with no %{public}s recency configured"
+ "((pi.priorityDate > :startOfSixMonthsAgo AND pi.priorityDate < :endOfSixMonthsAhead) AND NOT "
+ "(pi.priorityDate > :startOfOneMonthAgo AND pi.priorityDate < :endOfOneMonthAhead)"
+ "), 0)                            AS eligibleWithinMonth,\n       COALESCE(SUM("
+ "), 0)                           AS eligibleWithinSixMonths,\n       COALESCE(SUM(pi.processedVersion IS NOT NULL AND "
+ "), 0)  AS processedWithinMonth,\n       COALESCE(SUM(pi.processedVersion IS NOT NULL AND "
+ "), 0) AS processedWithinSixMonths\nFROM   pipeline p\nJOIN   pipeline_item pi INDEXED BY idx_pipeline_item_pipeline_deleteStatus_source\n       ON p.id = pi.pipeline\nWHERE  p.name = :name\nAND    pi.deleteStatus IS NULL\nGROUP BY pi.source"
+ "/usr/lib/system/libsystem_trace.dylib"
+ ":PR::A:kMDItemUserDownloadedDate"
+ "AND pi.errorCount < :maximumErrorCount"
+ "Could not read dead-reckoning snapshot at %{public}s: %@"
+ "DAS"
+ "DELETE FROM item WHERE identityID IN (SELECT value FROM _batch_uuids)"
+ "DeadReckoning.json"
+ "Failed to persist dead-reckoning snapshot: %@"
+ "GLP Embeddings Processing Phase 1"
+ "GLP Mail Attachments Processing Phase 1"
+ "Index creation version unavailable/non-numeric for %{public}s"
+ "Job requesting unschedule: %{public}s"
+ "Job throttled%{public}s: %{public}ld/%{public}ld consecutive failures; resetting budget, DAS will retry at next scheduled interval"
+ "Journal processing does not support the phase1 run type"
+ "Legacy SSR journal processing does not support the phase1 run type"
+ "Phase1 rehydration for %{public}s with no phase1 recency configured"
+ "Phase1 rehydration requires a phase1 recency on the pipeline descriptor"
+ "Pipeline Completeness"
+ "PipelineProgressPersistence"
+ "Querying StateStore metrics aggregates for pipeline %s"
+ "Recompute (telemetry)"
+ "Requested reindex for spotlight item: %s"
+ "Running %{public}s Cascade Rehydration for pipeline %{public}s"
+ "SELECT identityID, source, textContentHash FROM item WHERE lookupID = ?"
+ "SELECT p.name AS name, pi.processedVersion AS processedVersion,\n       pi.errorCount AS errorCount, i.identityID AS identityID,\n       i.source AS source, i.priorityDate AS priorityDate,\n       i.textContentHash AS textContentHash\nFROM   pipeline_item pi\nJOIN   pipeline p ON p.id = pi.pipeline\nJOIN   item i ON i.identityID = pi.identityID\nWHERE  i.identityID IN (SELECT identityID FROM item WHERE lookupID = ?)\nAND    pi.deleteStatus IS NULL"
+ "SELECT pi.errorCount, pi.processedVersion, i.identityID, i.source, i.textContentHash\nFROM   item i\nJOIN   pipeline_item pi ON pi.identityID = i.identityID\nJOIN   pipeline p ON p.id = pi.pipeline\nWHERE  i.lookupID = ? AND p.name = ?"
+ "SELECT pi.identityID\nFROM   pipeline_item pi INDEXED BY pipeline_item_identityID\nWHERE  pi.identityID > :lastKey\nGROUP BY pi.identityID\nHAVING COUNT(*) = COUNT(CASE WHEN pi.deleteStatus = "
+ "SELECT pi.itemHash, pi.processedVersion\nFROM   pipeline_item pi\nJOIN   pipeline p ON p.id = pi.pipeline\nWHERE  p.name = ? AND pi.identityID = ?"
+ "SELECT pi.source                                                 AS source,\n       COUNT(*)                                                  AS eligible,\n       SUM(pi.processedVersion IS NULL)                          AS needProcessing,\n       SUM(pi.processedVersion IS NOT NULL)                      AS processed,\n       COALESCE(SUM(pi.processedVersion IS NOT NULL AND pi.hasResult = 1), 0) AS withProcessingResults,\n       SUM(pi.processedVersion IS NULL AND pi.errorCount > 0)    AS withProcessingError,\n       SUM(pi.errorCount >= :cap)                                AS withMaxedProcessingError,\n       COALESCE(SUM("
+ "SELECT pi.source AS source,\n       SUM(i.textContentHash IS NULL)                              AS awaitingIndexProcessing,\n       SUM(i.textContentHash IS NOT NULL\n           AND     EXISTS(SELECT 1 FROM document_store_cache dsc\n                          WHERE dsc.lookupID = i.lookupID))        AS awaitingJournalProcessing,\n       SUM(i.textContentHash IS NOT NULL\n           AND NOT EXISTS(SELECT 1 FROM document_store_cache dsc\n                          WHERE dsc.lookupID = i.lookupID)\n           AND     EXISTS(SELECT 1 FROM rehydration r\n                          WHERE r.identityID = i.identityID))      AS awaitingRedonation,\n       SUM(i.textContentHash IS NOT NULL\n           AND NOT EXISTS(SELECT 1 FROM document_store_cache dsc\n                          WHERE dsc.lookupID = i.lookupID)\n           AND NOT EXISTS(SELECT 1 FROM rehydration r\n                          WHERE r.identityID = i.identityID))      AS awaitingReindex\nFROM   pipeline p\nJOIN   pipeline_item pi INDEXED BY idx_pipeline_item_pipeline_deleteStatus_source\n       ON p.id = pi.pipeline\nJOIN   item i ON pi.identityID = i.identityID\nWHERE  p.name = :name\nAND    pi.deleteStatus IS NULL\nAND    pi.processedVersion IS NULL\nGROUP BY pi.source"
+ "SKG: journal store not yet provisioned for protection class %{public}s; nothing to transfer"
+ "SKG: transferJournals: done — transferred %lu/%lu, skipped(inaccessible) %lu, skipped(not-provisioned) %lu, timedOut %lu, errored %lu"
+ "Settings UI Pipeline Completeness (Telemetry)"
+ "SettingsUIPipelineCompleteness.Telemetry"
+ "SpotlightKnowledgeDaemon/CascadeProcessingJob.swift"
+ "SpotlightKnowledgeDaemon/CascadeRehydrationJob.swift"
+ "SpotlightKnowledgeDaemon/JournalProcessingJob.swift"
+ "SpotlightKnowledgeDaemon/LegacySSRJournalProcessingJob.swift"
+ "Task finished and requesting unschedule: %{public}s"
+ "[HDBCutover] Fresh-index check: Class C creation version %s < %s, skipping"
+ "[HDBCutover] Fresh-index check: Class C creation version unknown, skipping"
+ "[HDBCutover] Fresh-index cutover for %s: Class C creation version %s >= %s"
+ "analytics:indexcreationversion:"
+ "awaitingIndexProcessing"
+ "awaitingJournalProcessing"
+ "awaitingRedonation"
+ "com.apple.spotlightknowledged.pipelines.glpembedding.processing.phase1"
+ "com.apple.spotlightknowledged.pipelines.glpmailattachments.processing.phase1"
+ "com.apple.spotlightknowledged.settings-ui-pipeline-completeness.telemetry"
+ "eligibleWithinMonth"
+ "eligibleWithinSixMonths"
+ "endOfOneMonthAhead"
+ "endOfSixMonthsAhead"
+ "fresh_index_class_c"
+ "indexCreationVersion(protectionClass:)"
+ "indexcreationversion command failed: %{public}@"
+ "indexcreationversion command timed out: %{public}@"
+ "itemScannedAdded"
+ "itemScannedUpdatedContentChanged"
+ "itemScannedUpdatedContentUnchanged"
+ "performFreshSurfacedDonationsFetch()"
+ "pipelineMetricsAggregates"
+ "prioritySerialNumber"
+ "processedWithinMonth"
+ "processedWithinSixMonths"
+ "startOfOneMonthAgo"
+ "startOfSixMonthsAgo"
+ "support_phased_processing"
+ "withMaxedProcessingError"
+ "withProcessingError"
+ "withProcessingResults"
- " AND pi.processedVersion IS NULL)"
- "CA donation: gated (%{public}sh since last)"
- "DELETE FROM item\nWHERE NOT EXISTS (\n    SELECT 1 FROM pipeline_item pi\n    WHERE pi.identityID = item.identityID\n    AND (pi.deleteStatus IS NULL OR pi.deleteStatus != "
- "Failed to create OS Activity"
- "Job throttled (charging): %{public}ld/%{public}ld consecutive failures; resetting charging budget, DAS will retry at next scheduled interval"
- "Job throttled: %{public}ld/%{public}ld consecutive failures; resetting budget, DAS will retry at next scheduled interval"
- "No serial number saved for pipeline: %s"
- "Querying StateStore metrics for pipeline %s"
- "Running Priority Cascade Rehydration for pipeline %{public}s"
- "SELECT i.source,\n       pi.processedVersion,\n       i.textContentHash,\n       EXISTS (SELECT 1 FROM document_store_cache dsc\n               WHERE dsc.lookupID = i.lookupID) AS isInDocumentCache,\n       EXISTS (SELECT 1 FROM rehydration r\n               WHERE r.identityID = i.identityID) AS isInRehydration,\n       i.priorityDate,\n       pi.hasResult,\n       pi.errorCount\nFROM   pipeline p\nJOIN   pipeline_item pi ON p.id = pi.pipeline\nJOIN   item i ON pi.identityID = i.identityID\nWHERE  p.name = :pipelineName\nAND    pi.deleteStatus IS NULL\nORDER BY pi.identityID\nLIMIT  :limit\nOFFSET :offset"
- "SKG: transferJournals: done — transferred %lu/%lu, skipped %lu, timedOut %lu, errored %lu"
- "SpotlightKnowledgeDaemon/OSActivity.swift"
- "Unable to calculate currentWeekday"
- "isInDocumentCache"
- "itemScanned"
- "metricsItemsForPipeline"
- "pipelineCompleteness.lastCADonationAt"
```
