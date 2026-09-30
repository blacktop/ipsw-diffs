## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-  __TEXT.__text: 0xa5943c
-  __TEXT.__objc_methlist: 0x976c
-  __TEXT.__const: 0x2d910
-  __TEXT.__cstring: 0x49825
-  __TEXT.__oslogstring: 0x1fd62
-  __TEXT.__gcc_except_tab: 0xd2c4
+  __TEXT.__text: 0xa74398
+  __TEXT.__objc_methlist: 0x9844
+  __TEXT.__const: 0x2e190
+  __TEXT.__cstring: 0x4cfa5
+  __TEXT.__oslogstring: 0x20462
+  __TEXT.__gcc_except_tab: 0xd520
   __TEXT.__ustring: 0x176e
   __TEXT.__dlopen_cstrs: 0xc3
-  __TEXT.__constg_swiftt: 0x14464
-  __TEXT.__swift5_typeref: 0x148d0
+  __TEXT.__constg_swiftt: 0x1466c
+  __TEXT.__swift5_typeref: 0x14ade
   __TEXT.__swift5_builtin: 0x8e8
-  __TEXT.__swift5_reflstr: 0xf64d
-  __TEXT.__swift5_fieldmd: 0xce7c
+  __TEXT.__swift5_reflstr: 0xf7cd
+  __TEXT.__swift5_fieldmd: 0xd0e4
   __TEXT.__swift5_mpenum: 0x13c
-  __TEXT.__swift5_assocty: 0x29a8
-  __TEXT.__swift5_capture: 0x1a7c4
-  __TEXT.__swift5_proto: 0x1c4c
-  __TEXT.__swift5_types: 0xc24
+  __TEXT.__swift5_assocty: 0x29f0
+  __TEXT.__swift5_capture: 0x1a868
+  __TEXT.__swift5_proto: 0x1cb8
+  __TEXT.__swift5_types: 0xc4c
   __TEXT.__swift5_types2: 0x8
   __TEXT.__swift_as_entry: 0x1b4
   __TEXT.__swift_as_ret: 0x188
-  __TEXT.__swift_as_cont: 0x370
+  __TEXT.__swift_as_cont: 0x36c
   __TEXT.__swift5_protos: 0xbc
-  __TEXT.__unwind_info: 0x161a0
-  __TEXT.__eh_frame: 0x2c688
+  __TEXT.__unwind_info: 0x16550
+  __TEXT.__eh_frame: 0x2d118
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4688
-  __DATA_CONST.__objc_classlist: 0x570
+  __DATA_CONST.__const: 0x46d8
+  __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6188
+  __DATA_CONST.__objc_selrefs: 0x61d8
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x118
-  __DATA_CONST.__got: 0x18d0
-  __AUTH_CONST.__const: 0x49750
+  __DATA_CONST.__got: 0x1910
+  __AUTH_CONST.__const: 0x4bbd0
   __AUTH_CONST.__cfstring: 0x72c0
-  __AUTH_CONST.__objc_const: 0x27598
+  __AUTH_CONST.__objc_const: 0x27b18
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x30d0
-  __AUTH.__objc_data: 0x1968
-  __AUTH.__data: 0x2738
-  __DATA.__objc_ivar: 0xb9c
-  __DATA.__data: 0x81d0
-  __DATA.__bss: 0x26ef0
-  __DATA.__common: 0x1eb
-  __DATA_DIRTY.__objc_data: 0x3360
-  __DATA_DIRTY.__data: 0x10910
-  __DATA_DIRTY.__bss: 0xf588
-  __DATA_DIRTY.__common: 0x8c0
+  __AUTH_CONST.__auth_got: 0x3120
+  __AUTH.__objc_data: 0x1b08
+  __AUTH.__data: 0x2888
+  __DATA.__objc_ivar: 0xba4
+  __DATA.__data: 0x8010
+  __DATA.__bss: 0x27360
+  __DATA.__common: 0x20b
+  __DATA_DIRTY.__objc_data: 0x33b0
+  __DATA_DIRTY.__data: 0x10dc0
+  __DATA_DIRTY.__bss: 0xfe98
+  __DATA_DIRTY.__common: 0x8f0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 31187
-  Symbols:   34806
-  CStrings:  8810
+  Functions: 31484
+  Symbols:   34941
+  CStrings:  8946
 
Sections:
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_types2 : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
Symbols:
+ -[FPDAppMonitor _markInitialPopulateReady]
+ -[FPDAppMonitor dealloc]
+ -[FPDAppMonitor waitForInitialPopulate]
+ -[FPDDomainDeadEndBackend searchableItemIdentifiersForURL:request:completionHandler:]
+ -[FPDDomainExtensionBackend searchableItemIdentifiersForURL:request:completionHandler:]
+ -[FPDXPCServicer _test_exitDaemonWithCompletionHandler:]
+ -[FPDXPCServicer _test_setForceLowDiskState:completionHandler:]
+ -[FPDXPCServicer searchableItemIdentifiersForURL:completionHandler:]
+ GCC_except_table125
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table141
+ GCC_except_table160
+ GCC_except_table165
+ GCC_except_table166
+ GCC_except_table172
+ GCC_except_table174
+ GCC_except_table180
+ GCC_except_table181
+ GCC_except_table193
+ GCC_except_table194
+ GCC_except_table200
+ GCC_except_table206
+ GCC_except_table211
+ GCC_except_table214
+ GCC_except_table229
+ GCC_except_table236
+ GCC_except_table238
+ GCC_except_table255
+ GCC_except_table257
+ GCC_except_table258
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table273
+ GCC_except_table282
+ GCC_except_table288
+ GCC_except_table289
+ GCC_except_table291
+ GCC_except_table297
+ GCC_except_table307
+ GCC_except_table314
+ GCC_except_table316
+ GCC_except_table317
+ GCC_except_table319
+ GCC_except_table337
+ GCC_except_table363
+ GCC_except_table364
+ GCC_except_table365
+ GCC_except_table394
+ GCC_except_table415
+ GCC_except_table418
+ GCC_except_table422
+ GCC_except_table431
+ GCC_except_table435
+ GCC_except_table436
+ GCC_except_table437
+ GCC_except_table438
+ GCC_except_table440
+ GCC_except_table441
+ GCC_except_table442
+ _FPFileLockedByFlock
+ _OBJC_CLASS_$_FPDPurgeableRepairer
+ _OBJC_CLASS_$_NSThread
+ _OBJC_IVAR_$_FPDAppMonitor._initialPopulateGroup
+ _OBJC_IVAR_$_FPDAppMonitor._initialPopulateReady
+ _OBJC_METACLASS_$_FPDPurgeableRepairer
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ __CLASS_METHODS_FPDPurgeableRepairer
+ __DATA_FPDPurgeableRepairer
+ __DATA__TtC18FileProviderDaemon22PurgeableRepairerState
+ __DATA__TtC18FileProviderDaemon23PurgeableRepairerReport
+ __DATA__TtC18FileProviderDaemon26PurgeableRepairerAppReport
+ __DATA__TtC18FileProviderDaemon28PurgeableRepairerRootContext
+ __INSTANCE_METHODS_FPDPurgeableRepairer
+ __IVARS_FPDPurgeableRepairer
+ __IVARS__TtC18FileProviderDaemon22PurgeableRepairerState
+ __IVARS__TtC18FileProviderDaemon23PurgeableRepairerReport
+ __IVARS__TtC18FileProviderDaemon26PurgeableRepairerAppReport
+ __IVARS__TtC18FileProviderDaemon28PurgeableRepairerRootContext
+ __METACLASS_DATA_FPDPurgeableRepairer
+ __METACLASS_DATA__TtC18FileProviderDaemon22PurgeableRepairerState
+ __METACLASS_DATA__TtC18FileProviderDaemon23PurgeableRepairerReport
+ __METACLASS_DATA__TtC18FileProviderDaemon26PurgeableRepairerAppReport
+ __METACLASS_DATA__TtC18FileProviderDaemon28PurgeableRepairerRootContext
+ ___56-[FPDXPCServicer _test_exitDaemonWithCompletionHandler:]_block_invoke
+ ___63-[FPDXPCServicer _test_setForceLowDiskState:completionHandler:]_block_invoke
+ ___68-[FPDXPCServicer searchableItemIdentifiersForURL:completionHandler:]_block_invoke
+ ___87-[FPDDomainExtensionBackend searchableItemIdentifiersForURL:request:completionHandler:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48s56bs_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___swift_closure_destructor.1012Tm
+ ___swift_closure_destructor.1015Tm
+ ___swift_closure_destructor.1018Tm
+ ___swift_closure_destructor.1021Tm
+ ___swift_closure_destructor.104Tm
+ ___swift_closure_destructor.109Tm
+ ___swift_closure_destructor.112Tm
+ ___swift_closure_destructor.121Tm
+ ___swift_closure_destructor.1224Tm
+ ___swift_closure_destructor.123Tm
+ ___swift_closure_destructor.148Tm
+ ___swift_closure_destructor.1547Tm
+ ___swift_closure_destructor.157Tm
+ ___swift_closure_destructor.160Tm
+ ___swift_closure_destructor.1624Tm
+ ___swift_closure_destructor.165Tm
+ ___swift_closure_destructor.1672Tm
+ ___swift_closure_destructor.1675Tm
+ ___swift_closure_destructor.168Tm
+ ___swift_closure_destructor.1708Tm
+ ___swift_closure_destructor.1735Tm
+ ___swift_closure_destructor.174Tm
+ ___swift_closure_destructor.1751Tm
+ ___swift_closure_destructor.1760Tm
+ ___swift_closure_destructor.1844Tm
+ ___swift_closure_destructor.185Tm
+ ___swift_closure_destructor.1872Tm
+ ___swift_closure_destructor.190Tm
+ ___swift_closure_destructor.1933Tm
+ ___swift_closure_destructor.196Tm
+ ___swift_closure_destructor.200Tm
+ ___swift_closure_destructor.202Tm
+ ___swift_closure_destructor.210Tm
+ ___swift_closure_destructor.217Tm
+ ___swift_closure_destructor.224Tm
+ ___swift_closure_destructor.22Tm
+ ___swift_closure_destructor.231Tm
+ ___swift_closure_destructor.244Tm
+ ___swift_closure_destructor.2455Tm
+ ___swift_closure_destructor.256Tm
+ ___swift_closure_destructor.2762Tm
+ ___swift_closure_destructor.281Tm
+ ___swift_closure_destructor.283Tm
+ ___swift_closure_destructor.285Tm
+ ___swift_closure_destructor.2875Tm
+ ___swift_closure_destructor.290Tm
+ ___swift_closure_destructor.299Tm
+ ___swift_closure_destructor.3012Tm
+ ___swift_closure_destructor.3019Tm
+ ___swift_closure_destructor.3029Tm
+ ___swift_closure_destructor.302Tm
+ ___swift_closure_destructor.3032Tm
+ ___swift_closure_destructor.3106Tm
+ ___swift_closure_destructor.3137Tm
+ ___swift_closure_destructor.317Tm
+ ___swift_closure_destructor.3243Tm
+ ___swift_closure_destructor.332Tm
+ ___swift_closure_destructor.3381Tm
+ ___swift_closure_destructor.3411Tm
+ ___swift_closure_destructor.347Tm
+ ___swift_closure_destructor.3487Tm
+ ___swift_closure_destructor.3497Tm
+ ___swift_closure_destructor.3500Tm
+ ___swift_closure_destructor.3503Tm
+ ___swift_closure_destructor.3579Tm
+ ___swift_closure_destructor.3585Tm
+ ___swift_closure_destructor.3594Tm
+ ___swift_closure_destructor.360Tm
+ ___swift_closure_destructor.377Tm
+ ___swift_closure_destructor.379Tm
+ ___swift_closure_destructor.398Tm
+ ___swift_closure_destructor.401Tm
+ ___swift_closure_destructor.4080Tm
+ ___swift_closure_destructor.4124Tm
+ ___swift_closure_destructor.4130Tm
+ ___swift_closure_destructor.4260Tm
+ ___swift_closure_destructor.440Tm
+ ___swift_closure_destructor.4467Tm
+ ___swift_closure_destructor.4470Tm
+ ___swift_closure_destructor.4474Tm
+ ___swift_closure_destructor.4477Tm
+ ___swift_closure_destructor.450Tm
+ ___swift_closure_destructor.4557Tm
+ ___swift_closure_destructor.4583Tm
+ ___swift_closure_destructor.4622Tm
+ ___swift_closure_destructor.470Tm
+ ___swift_closure_destructor.4738Tm
+ ___swift_closure_destructor.4744Tm
+ ___swift_closure_destructor.481Tm
+ ___swift_closure_destructor.48Tm
+ ___swift_closure_destructor.4959Tm
+ ___swift_closure_destructor.512Tm
+ ___swift_closure_destructor.5147Tm
+ ___swift_closure_destructor.529Tm
+ ___swift_closure_destructor.5420Tm
+ ___swift_closure_destructor.5452Tm
+ ___swift_closure_destructor.5755Tm
+ ___swift_closure_destructor.5966Tm
+ ___swift_closure_destructor.607Tm
+ ___swift_closure_destructor.613Tm
+ ___swift_closure_destructor.6268Tm
+ ___swift_closure_destructor.6282Tm
+ ___swift_closure_destructor.6488Tm
+ ___swift_closure_destructor.6495Tm
+ ___swift_closure_destructor.6520Tm
+ ___swift_closure_destructor.6643Tm
+ ___swift_closure_destructor.686Tm
+ ___swift_closure_destructor.696Tm
+ ___swift_closure_destructor.713Tm
+ ___swift_closure_destructor.72Tm
+ ___swift_closure_destructor.817Tm
+ ___swift_closure_destructor.828Tm
+ ___swift_closure_destructor.837Tm
+ ___swift_closure_destructor.851Tm
+ _associated conformance 18FileProviderDaemon20PurgeableRepairErrorOSHAASQ
+ _associated conformance 18FileProviderDaemon22PurgeableRepairerStateC10CodingKeys33_471D95EECC0FBC90BCC7A6C823859DB6LLOSHAASQ
+ _associated conformance 18FileProviderDaemon22PurgeableRepairerStateC10CodingKeys33_471D95EECC0FBC90BCC7A6C823859DB6LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 18FileProviderDaemon22PurgeableRepairerStateC10CodingKeys33_471D95EECC0FBC90BCC7A6C823859DB6LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 18FileProviderDaemon23PurgeableRepairerReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLOSHAASQ
+ _associated conformance 18FileProviderDaemon23PurgeableRepairerReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 18FileProviderDaemon23PurgeableRepairerReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 18FileProviderDaemon26PurgeableRepairerAppReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLOSHAASQ
+ _associated conformance 18FileProviderDaemon26PurgeableRepairerAppReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLOs0H3KeyAAs23CustomStringConvertible
+ _associated conformance 18FileProviderDaemon26PurgeableRepairerAppReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLOs0H3KeyAAs28CustomDebugStringConvertible
+ _fpfs_get_purgeable_info_at
+ _fpfs_query_purgeable_bytes
+ _fpfs_unset_purgeable_at
+ _objc_msgSend$_markInitialPopulateReady
+ _objc_msgSend$fp_uncachedContainerURLForSecurityApplicationGroupIdentifier:forPrimaryPersona:
+ _objc_msgSend$registerBackgroundTaskWithMonitor:
+ _objc_msgSend$searchableItemIdentifierForURL:completionHandler:
+ _objc_msgSend$searchableItemIdentifiersForURL:request:completionHandler:
+ _objc_msgSend$sleepForTimeInterval:
+ _objc_msgSend$waitForInitialPopulate
+ _symbolic SDySS_____G 18FileProviderDaemon26PurgeableRepairerAppReportC
+ _symbolic SaySSGSg______pSgIeggg_ s5ErrorP
+ _symbolic SaySSGSg______pSgIegng_ s5ErrorP
+ _symbolic Say_____G 18FileProviderDaemon28PurgeableRepairerRootContextC
+ _symbolic Say_____GSg 18FileProviderDaemon28PurgeableRepairerRootContextC
+ _symbolic So12BGSystemTaskC
+ _symbolic So13FPDAppMonitorC
+ _symbolic _____ 18FileProviderDaemon20FPDPurgeableRepairerC
+ _symbolic _____ 18FileProviderDaemon20PurgeableRepairErrorO
+ _symbolic _____ 18FileProviderDaemon22PurgeableRepairerStateC
+ _symbolic _____ 18FileProviderDaemon22PurgeableRepairerStateC10CodingKeys33_471D95EECC0FBC90BCC7A6C823859DB6LLO
+ _symbolic _____ 18FileProviderDaemon23PurgeableRepairerReportC
+ _symbolic _____ 18FileProviderDaemon23PurgeableRepairerReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLO
+ _symbolic _____ 18FileProviderDaemon26PurgeableRepairerAppReportC
+ _symbolic _____ 18FileProviderDaemon26PurgeableRepairerAppReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLO
+ _symbolic _____ 18FileProviderDaemon28PurgeableRepairerRootContextC
+ _symbolic _____ 18FileProviderDaemon9ScanStats33_AB222CD6284BFE4248F27F1897F2367ALLV
+ _symbolic _____XMT 18FileProviderDaemon20FPDPurgeableRepairerC
+ _symbolic _____y2ID_____QzG 18FileProviderDaemon21ForceIngestionTrackerV AA0A4ItemP
+ _symbolic _____ySDy2ID_____Qz_____yxq__GGG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon0C4ItemP AD18BackgroundUploaderC0G12UploadReasonO
+ _symbolic _____ySDyxSiGG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____ySS_____G s18_DictionaryStorageC 18FileProviderDaemon26PurgeableRepairerAppReportC
+ _symbolic _____yShy2ID_____Qy_GG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon0C4ItemP
+ _symbolic _____yShy2ID_____QzGG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon0C4ItemP
+ _symbolic _____y_____G s22KeyedDecodingContainerV 18FileProviderDaemon22PurgeableRepairerStateC10CodingKeys33_471D95EECC0FBC90BCC7A6C823859DB6LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 18FileProviderDaemon23PurgeableRepairerReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 18FileProviderDaemon26PurgeableRepairerAppReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 18FileProviderDaemon22PurgeableRepairerStateC10CodingKeys33_471D95EECC0FBC90BCC7A6C823859DB6LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 18FileProviderDaemon23PurgeableRepairerReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 18FileProviderDaemon26PurgeableRepairerAppReportC10CodingKeys33_238FDA26D33F14DB7C127E2A475654E1LLO
+ _symbolic _____y_____So6FPItemCq0_q1_GSgXwz_AB_AD__________SaySSGSgABRszADRs______yABGRb0______R0_AKyADGRb1______R1_AB13URLBackedItem_____Rt0_r2__lXX 18FileProviderDaemon10SyncEngineC AA7VFSItemV AA11VFSFileTreeC AA06FPFileH0C AA0aH6WriterC AA09URLBackedahJ0P AA012DomainBackedahJ0P AM
+ _symbolic _____y__________G s6ResultOsRi_zRi0_zrlE s6UInt64V 10Foundation10POSIXErrorV
+ _symbolic _____y_____y2ID_____QzGSgG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon20InUseTrackerSnapshotV AD0C4ItemP
+ _symbolic _____y_____yq_GG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon0C20TreeChangeAggregatorV
+ _symbolic _____y_____yxG_SDy_____Shy2ID_____QzGGtG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon0C20TreeChangeAggregatorV s6UInt64V AD0C4ItemP
+ _symbolic _____y_____yxq__GG 15Synchronization5MutexVAARi_zrlE 18FileProviderDaemon16ConcreteDatabaseC25DirectoryManifestInstance33_E89B838F23AA85B19E281E0E7007A7C8LLV
- GCC_except_table129
- GCC_except_table145
- GCC_except_table147
- GCC_except_table148
- GCC_except_table164
- GCC_except_table170
- GCC_except_table176
- GCC_except_table177
- GCC_except_table178
- GCC_except_table184
- GCC_except_table185
- GCC_except_table197
- GCC_except_table202
- GCC_except_table208
- GCC_except_table210
- GCC_except_table215
- GCC_except_table218
- GCC_except_table233
- GCC_except_table240
- GCC_except_table242
- GCC_except_table259
- GCC_except_table261
- GCC_except_table266
- GCC_except_table267
- GCC_except_table276
- GCC_except_table277
- GCC_except_table290
- GCC_except_table293
- GCC_except_table295
- GCC_except_table296
- GCC_except_table301
- GCC_except_table311
- GCC_except_table320
- GCC_except_table322
- GCC_except_table325
- GCC_except_table327
- GCC_except_table341
- GCC_except_table367
- GCC_except_table368
- GCC_except_table369
- GCC_except_table398
- GCC_except_table423
- GCC_except_table426
- GCC_except_table430
- ___swift_closure_destructor.1001Tm
- ___swift_closure_destructor.105Tm
- ___swift_closure_destructor.114Tm
- ___swift_closure_destructor.11Tm
- ___swift_closure_destructor.1204Tm
- ___swift_closure_destructor.145Tm
- ___swift_closure_destructor.147Tm
- ___swift_closure_destructor.1543Tm
- ___swift_closure_destructor.154Tm
- ___swift_closure_destructor.1604Tm
- ___swift_closure_destructor.1652Tm
- ___swift_closure_destructor.1655Tm
- ___swift_closure_destructor.167Tm
- ___swift_closure_destructor.1701Tm
- ___swift_closure_destructor.1721Tm
- ___swift_closure_destructor.1740Tm
- ___swift_closure_destructor.1744Tm
- ___swift_closure_destructor.176Tm
- ___swift_closure_destructor.179Tm
- ___swift_closure_destructor.1824Tm
- ___swift_closure_destructor.182Tm
- ___swift_closure_destructor.1852Tm
- ___swift_closure_destructor.192Tm
- ___swift_closure_destructor.1941Tm
- ___swift_closure_destructor.201Tm
- ___swift_closure_destructor.203Tm
- ___swift_closure_destructor.204Tm
- ___swift_closure_destructor.208Tm
- ___swift_closure_destructor.211Tm
- ___swift_closure_destructor.218Tm
- ___swift_closure_destructor.225Tm
- ___swift_closure_destructor.2463Tm
- ___swift_closure_destructor.250Tm
- ___swift_closure_destructor.264Tm
- ___swift_closure_destructor.267Tm
- ___swift_closure_destructor.275Tm
- ___swift_closure_destructor.2770Tm
- ___swift_closure_destructor.284Tm
- ___swift_closure_destructor.287Tm
- ___swift_closure_destructor.2883Tm
- ___swift_closure_destructor.296Tm
- ___swift_closure_destructor.3020Tm
- ___swift_closure_destructor.3027Tm
- ___swift_closure_destructor.3037Tm
- ___swift_closure_destructor.3040Tm
- ___swift_closure_destructor.3114Tm
- ___swift_closure_destructor.311Tm
- ___swift_closure_destructor.3145Tm
- ___swift_closure_destructor.3251Tm
- ___swift_closure_destructor.326Tm
- ___swift_closure_destructor.3389Tm
- ___swift_closure_destructor.3419Tm
- ___swift_closure_destructor.341Tm
- ___swift_closure_destructor.346Tm
- ___swift_closure_destructor.3495Tm
- ___swift_closure_destructor.3505Tm
- ___swift_closure_destructor.3508Tm
- ___swift_closure_destructor.3511Tm
- ___swift_closure_destructor.3587Tm
- ___swift_closure_destructor.3593Tm
- ___swift_closure_destructor.3602Tm
- ___swift_closure_destructor.363Tm
- ___swift_closure_destructor.371Tm
- ___swift_closure_destructor.381Tm
- ___swift_closure_destructor.386Tm
- ___swift_closure_destructor.395Tm
- ___swift_closure_destructor.4088Tm
- ___swift_closure_destructor.4132Tm
- ___swift_closure_destructor.4138Tm
- ___swift_closure_destructor.422Tm
- ___swift_closure_destructor.425Tm
- ___swift_closure_destructor.4268Tm
- ___swift_closure_destructor.4475Tm
- ___swift_closure_destructor.4478Tm
- ___swift_closure_destructor.4482Tm
- ___swift_closure_destructor.4485Tm
- ___swift_closure_destructor.454Tm
- ___swift_closure_destructor.4565Tm
- ___swift_closure_destructor.458Tm
- ___swift_closure_destructor.4591Tm
- ___swift_closure_destructor.4630Tm
- ___swift_closure_destructor.4746Tm
- ___swift_closure_destructor.474Tm
- ___swift_closure_destructor.4752Tm
- ___swift_closure_destructor.475Tm
- ___swift_closure_destructor.4967Tm
- ___swift_closure_destructor.5155Tm
- ___swift_closure_destructor.515Tm
- ___swift_closure_destructor.5428Tm
- ___swift_closure_destructor.5460Tm
- ___swift_closure_destructor.5763Tm
- ___swift_closure_destructor.57Tm
- ___swift_closure_destructor.5974Tm
- ___swift_closure_destructor.603Tm
- ___swift_closure_destructor.609Tm
- ___swift_closure_destructor.6276Tm
- ___swift_closure_destructor.6290Tm
- ___swift_closure_destructor.6445Tm
- ___swift_closure_destructor.6452Tm
- ___swift_closure_destructor.6477Tm
- ___swift_closure_destructor.6600Tm
- ___swift_closure_destructor.66Tm
- ___swift_closure_destructor.682Tm
- ___swift_closure_destructor.698Tm
- ___swift_closure_destructor.709Tm
- ___swift_closure_destructor.813Tm
- ___swift_closure_destructor.830Tm
- ___swift_closure_destructor.839Tm
- ___swift_closure_destructor.847Tm
- ___swift_closure_destructor.94Tm
- ___swift_closure_destructor.992Tm
- ___swift_closure_destructor.995Tm
- ___swift_closure_destructor.998Tm
- ___unnamed_59
- ___unnamed_60
- _get_type_metadata 15Synchronization5MutexVy18FileProviderDaemon10FPCKReportVG noncopyable
- _get_type_metadata 15Synchronization5MutexVy18FileProviderDaemon12DynamicErrorVSgAFcSgG noncopyable
- _get_type_metadata 15Synchronization5MutexVy18FileProviderDaemon12VFSIOContextVG noncopyable
- _get_type_metadata 15Synchronization5MutexVySDySO18FileProviderDaemon14WeakEnumeratorVGG noncopyable
- _get_type_metadata 15Synchronization5MutexVySDySSSiGG noncopyable
- _get_type_metadata 15Synchronization5MutexVySDySo27NSFileProviderContentPolicyV04FileD6Daemon0eF18BehaviorDescriptorVGG noncopyable
- _get_type_metadata 15Synchronization5MutexVySays6UInt64V_So10wharf_stepVtGG noncopyable
- _get_type_metadata 15Synchronization5MutexVySbG noncopyable
- _get_type_metadata 15Synchronization5MutexVySo26OS_dispatch_source_data_or_p17garbageCollection_SoAD_p15capturedContenttSgG noncopyable
- _get_type_metadata 15Synchronization6AtomicVySbG noncopyable
- _get_type_metadata 15Synchronization6AtomicVys6UInt64VG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_AA0A10TreeWriterCyxGRb0_ADyq_GRb1_r2_l15Synchronization5MutexVyAA20InUseTrackerSnapshotVy2IDQzGSgG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_AA0A10TreeWriterCyxGRb0_ADyq_GRb1_r2_lAA21ForceIngestionTrackerVy2IDQzG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVyAA0A20TreeChangeAggregatorVyq_GG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVyAA0A20TreeChangeAggregatorVyxG_SDys6UInt64VShy2IDQzGGtG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVyAA16ConcreteDatabaseC25DirectoryManifestInstance33_E89B838F23AA85B19E281E0E7007A7C8LLVyxq__GG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVySDy2IDQzAA18BackgroundUploaderC0H12UploadReasonOyxq__GGG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVyShy2IDQy_GG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVyShy2IDQzGG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization5MutexVySo17OS_os_transaction_pSgG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVySbG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVySo45FPDExclusiveSharedSystemSchedulerWatcherStateVG noncopyable
- _get_type_metadata 18FileProviderDaemon0A4ItemRzAaBR_r0_l15Synchronization6AtomicVys5Int64VG noncopyable
- _get_type_metadata 18FileProviderDaemon0A6ItemIDRzl15Synchronization5MutexVySDyxSiGG noncopyable
- _get_type_metadata l18FileProviderDaemon17VFSFileDescriptorV noncopyable
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "\n   ORDER BY fp.metadata_last_used_date DESC"
+ "\n   ORDER BY fp.metadata_last_used_date DESC\n   LIMIT "
+ "\n ORDER BY bd.scheduling_timestamp\n LIMIT "
+ "\n ORDER BY bd.scheduling_timestamp DESC"
+ "\n ORDER BY bd.scheduling_timestamp DESC\n LIMIT "
+ "  SELECT fp.metadata_size\n    FROM background_downloader AS bd INDEXED BY background_downloader__reason_speculativeSet\n   INNER JOIN reconciliation_table AS rt ON (rt.fs_id = bd.id)\n   INNER JOIN fp_snapshot AS fp ON (fp.id = rt.fp_id)\n   WHERE bd.reason & "
+ "%{public}s: found=%llu fixed=%llu"
+ "-[FPDXPCServicer _test_exitDaemonWithCompletionHandler:]"
+ "-[FPDXPCServicer _test_exitDaemonWithCompletionHandler:]_block_invoke"
+ "-[FPDXPCServicer _test_setForceLowDiskState:completionHandler:]"
+ "-[FPDXPCServicer _test_setForceLowDiskState:completionHandler:]_block_invoke"
+ "-[FPDXPCServicer searchableItemIdentifiersForURL:completionHandler:]"
+ "-[FPDXPCServicer searchableItemIdentifiersForURL:completionHandler:]_block_invoke"
+ "/var/mobile/Library/Application Support/FileProvider/com.apple.FileProvider.LocalStorage/"
+ "App registry empty after startMonitoring (attempt %ld/3), waiting before retry"
+ "App registry still empty after 3 attempts; scanning LocalStorage root only"
+ "BGSystemTask asked us to defer; stopping after %llu roots"
+ "CO-ROUTINE enumeration_view\nCO-ROUTINE (subquery-3)\nCOMPOUND QUERY\nLEFT-MOST SUBQUERY\nSEARCH reconciliation_table USING COVERING INDEX reconciliation_materialized_set_opt\nUNION ALL\nSEARCH tombstone_table USING COVERING INDEX tombstone_materialized_set_opt\nSEARCH (subquery-3)\nSCAN enumeration_view"
+ "CO-ROUTINE parent_dirs\nSETUP\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nRECURSIVE STEP\nSCAN pd\nSEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSCAN pd\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "CO-ROUTINE parent_dirs\nSETUP\nSEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nRECURSIVE STEP\nSCAN pd\nSEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSCAN pd\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "CO-ROUTINE parent_dirs\nSETUP\nSEARCH snap USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nRECURSIVE STEP\nSCAN pd\nSEARCH snap USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nSCAN pd\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "Couldn't clear purgeable on %{public}s: %{darwin.errno,public}d"
+ "Couldn't lstat LocalStorage root at %{public}s: %{darwin.errno,public}d"
+ "Couldn't lstat app %{public}s at %{public}s: %{darwin.errno,public}d"
+ "Couldn't lstat home dir %{public}s: %{darwin.errno,public}d"
+ "Couldn't open FTS stream on %{public}s: %{darwin.errno,public}d"
+ "Couldn't query purgeable info on %{public}s: %{darwin.errno,public}d"
+ "Couldn't retrieve home directory"
+ "Couldn't retrieve root dir for LocalStorage"
+ "DIR_STATS failed on %{public}s: %d (falling back to FTS scan)"
+ "Discarding state plist at %{public}s: %{public}@"
+ "FPDPurgeableRepairer [run: %.*fs%{public}s] ran and fixed %llu items across %llu roots (%llu dir-stats fallbacks)"
+ "FPDPurgeableRepairer [run: %.*fs] failed with %{public}@"
+ "FPDPurgeableRepairer.plist"
+ "FPDPurgeableRepairerReport.plist"
+ "Failed to submit %{public}s task: %{public}@"
+ "FileProviderDaemon.FPDPurgeableRepairer"
+ "Invalid volume UUID (device migration?): %s != %s"
+ "Loading PurgeableRepairerState from %{public}s"
+ "MERGE (UNION)\nLEFT\nSEARCH background_downloader USING COVERING INDEX background_downloader__state__scheduling_timestamp (state=?)\nUSE TEMP B-TREE FOR ORDER BY\nRIGHT\nSEARCH background_downloader USING INDEX background_downloader__state__scheduling_timestamp (state=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "MULTI-INDEX OR\nINDEX 1\nSEARCH reconciliation_table USING INDEX reconciliation_background_upload_simple (fs_scheduling_state=? AND fs_scheduling_state_conditions=?)\nINDEX 2\nSEARCH reconciliation_table USING INDEX reconciliation_fp_scheduling_state (fp_scheduling_state=?)"
+ "MULTI-INDEX OR\nINDEX 1\nSEARCH reconciliation_table USING INDEX reconciliation_background_upload_simple (fs_scheduling_state=?)\nINDEX 2\nSEARCH reconciliation_table USING INDEX reconciliation_fp_scheduling_state (fp_scheduling_state=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "MULTI-INDEX OR\nINDEX 1\nSEARCH reconciliation_table USING INDEX reconciliation_is_pending (is_pending=?)\nINDEX 2\nSEARCH reconciliation_table USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "Precondition throwed error "
+ "Root has no purgeable bytes, skipping FTS: %{public}s"
+ "Root reports %llu purgeable bytes, scanning: %{public}s"
+ "SCAN background_downloader"
+ "SCAN bd USING INDEX background_downloader__reason_speculativeSet\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)"
+ "SCAN bd USING INDEX background_downloader__reason_speculativeSet\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SCAN parent_rt\nCORRELATED SCALAR SUBQUERY 1\nSEARCH snap USING INDEX FS_snapshot_parent_id_idx (parent_id=?)\nSEARCH child_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SCAN reconciliation_table"
+ "SCAN reconciliation_table\nUSE TEMP B-TREE FOR ORDER BY"
+ "SCAN reconciliation_table USING COVERING INDEX reconciliation_table__item_is_flocked"
+ "SCAN rt\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SCAN rt USING INDEX recursive_deletion_root"
+ "SCAN tombstone_table"
+ "SEARCH background_downloader USING COVERING INDEX sqlite_autoindex_background_downloader_1 (id=? AND extent_location=? AND extent_length=?)"
+ "SEARCH background_downloader USING COVERING INDEX sqlite_autoindex_background_downloader_1 (id=?)"
+ "SEARCH background_downloader USING INDEX background_downloader__state__scheduling_timestamp (state=?)"
+ "SEARCH background_downloader USING INDEX sqlite_autoindex_background_downloader_1 (id=?)"
+ "SEARCH bd USING INDEX background_downloader__state__scheduling_timestamp (state=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SEARCH child_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH child_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH snap USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH jobs USING INDEX jobs_state__side__scheduling_ordering (scheduling_state=? AND side=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH jobs USING INDEX jobs_state__side__scheduling_ordering (scheduling_state=? AND side=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)"
+ "SEARCH original_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH original_snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH sibling_snap USING INDEX FS_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH original_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH original_snap USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nSEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH sibling_snap USING INDEX FP_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH snap USING INDEX FP_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH snap USING INDEX FP_snapshot_parent_id__filename_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH snap USING INDEX FP_snapshot_parent_id_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH snap USING INDEX FS_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH snap USING INDEX FS_snapshot_parent_id__filename_idx_other (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH parent_rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH snap USING INDEX FS_snapshot_parent_id_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH reconciliation_table USING COVERING INDEX reconciliation_fs_disk_import_status__fs_id (fs_disk_import_status=?)"
+ "SEARCH reconciliation_table USING COVERING INDEX reconciliation_fs_id_old_version_clone (fs_captured_content_file_id=?)"
+ "SEARCH reconciliation_table USING COVERING INDEX reconciliation_pending_set (fp_id>?)"
+ "SEARCH reconciliation_table USING COVERING INDEX reconciliation_table__item_is_flocked (item_is_flocked=?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation__fp_scheduling_state__fp_id (fp_scheduling_state=? AND fp_id>?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation_background_upload_simple (fs_scheduling_state=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fp_scheduling_state (fp_scheduling_state=?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fs_disk_import_status__fp_id (fs_disk_import_status=? AND fp_id>?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fs_disk_import_status__fp_id (fs_disk_import_status=?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fs_disk_import_status__fp_id (fs_disk_import_status=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fs_disk_import_status__fs_id (fs_disk_import_status=? AND fs_id>?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH reconciliation_table USING INDEX reconciliation_fs_disk_import_status__fs_id (fs_disk_import_status=?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation_global_progress_materialize (fs_materialization_status=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH reconciliation_table USING INDEX reconciliation_is_pending (is_pending=?)"
+ "SEARCH reconciliation_table USING INDEX reconciliation_table__item_is_flocked (item_is_flocked=?)"
+ "SEARCH reconciliation_table USING INTEGER PRIMARY KEY (rowid=?)"
+ "SEARCH reconciliation_table USING INTEGER PRIMARY KEY (rowid>?)"
+ "SEARCH rt USING COVERING INDEX reconciliation_fs_id_old_version_clone (fs_captured_content_file_id>?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH rt USING INDEX reconciliation_global_progress_fp (kind=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SEARCH rt USING INDEX reconciliation_global_progress_fs (kind=?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)"
+ "SEARCH rt USING INDEX reconciliation_global_progress_materialize (fs_materialization_status=? AND kind=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SEARCH rt USING INDEX reconciliation_kind_last_content_change (kind=? AND last_content_change=? AND rowid>?)"
+ "SEARCH rt USING INDEX reconciliation_kind_last_content_change (kind=?)\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)"
+ "SEARCH rt USING INDEX reconciliation_table_last_change (last_change>?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?) LEFT-JOIN\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?) LEFT-JOIN"
+ "SEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?) LEFT-JOIN\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?) LEFT-JOIN"
+ "SEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?) LEFT-JOIN\nSEARCH fp USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?) LEFT-JOIN"
+ "SEARCH rt USING INTEGER PRIMARY KEY (rowid>?)"
+ "SEARCH rt USING INTEGER PRIMARY KEY (rowid>?)\nSEARCH fs USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)"
+ "SEARCH snap USING INDEX FP_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH snap USING INDEX FP_snapshot_parent_id__filename_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH snap USING INDEX FP_snapshot_parent_id_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH snap USING INDEX FS_snapshot_parent_id__filename_idx (parent_id=? AND filename=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH snap USING INDEX FS_snapshot_parent_id_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH snap USING INDEX FS_snapshot_parent_id_idx (parent_id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)\nUSE TEMP B-TREE FOR ORDER BY"
+ "SEARCH snap USING INDEX sqlite_autoindex_FP_snapshot_1 (id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_2 (fp_id=?)"
+ "SEARCH snap USING INDEX sqlite_autoindex_FS_snapshot_1 (id=?)\nSEARCH rt USING INDEX sqlite_autoindex_reconciliation_table_1 (fs_id=?)"
+ "SEARCH tombstone_table USING COVERING INDEX tombstone_materialized_set_opt (enumeration_anchor<?)"
+ "SEARCH tombstone_table USING COVERING INDEX tombstone_table_asc (last_change<?)"
+ "SEARCH tombstone_table USING COVERING INDEX tombstone_table_asc (last_change>?)"
+ "SELECT fp.metadata_size\n  FROM background_downloader AS bd\n INNER JOIN reconciliation_table AS rt ON (rt.fs_id = bd.id)\n INNER JOIN fp_snapshot AS fp ON (fp.id = rt.fp_id)\n WHERE bd.state = "
+ "Scan failed: %{public}@"
+ "Skipping app %{public}s because Documents lives on a different volume"
+ "Unable to persist report: %{public}@"
+ "Unable to resolve volume UUID for parent of %{public}s"
+ "Unsupported version "
+ "[ERROR] can't get CS identifiers for URL %@ for extension %@; %@"
+ "a"
+ "byApp"
+ "com.apple.FileProvider.maintenance.purgeable-repair"
+ "deletion of unknown item racing with deferred ingestion on "
+ "fpd-purgeable-repair-bgst"
+ "fpd-purgeable-repairer"
+ "fts_read failed on %{public}s: %{darwin.errno,public}d"
+ "group.com.apple.FileProvider.LocalStorage"
+ "lastUpdate"
+ "mostRecentPurgeableMtime"
+ "purgeable_repair_global"
+ "rescansPerformed"
+ "searchableItemIdentifiers("
+ "searchableItemIdentifiers(for:request:completionHandler:)"
+ "strdup failed for %{public}s"
+ "totalItemsFixed"
+ "totalItemsFound"
+ "totalRootsDiscovered"
+ "volumeUUID"
- "\n   ORDER BY fp.metadata_last_used_date DESC\n   "
- "\n ORDER BY bd.scheduling_timestamp\n "
- "\n ORDER BY bd.scheduling_timestamp DESC\n  "
- "fp.metadata_size"

```
