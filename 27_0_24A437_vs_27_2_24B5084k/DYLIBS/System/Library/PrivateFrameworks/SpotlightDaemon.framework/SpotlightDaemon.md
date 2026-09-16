## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2459.105.0.0.0
-  __TEXT.__text: 0xc21e4
-  __TEXT.__objc_methlist: 0x4bd4
-  __TEXT.__const: 0x3e8
-  __TEXT.__cstring: 0x991b
-  __TEXT.__gcc_except_tab: 0x4a1c
-  __TEXT.__oslogstring: 0xd359
+2465.1.2.0.0
+  __TEXT.__text: 0xc37d8
+  __TEXT.__objc_methlist: 0x4c6c
+  __TEXT.__const: 0x410
+  __TEXT.__cstring: 0x9c05
+  __TEXT.__gcc_except_tab: 0x48e4
+  __TEXT.__oslogstring: 0xd4c0
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x3488
+  __TEXT.__unwind_info: 0x3508
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x47b0
-  __DATA_CONST.__objc_classlist: 0x1b0
+  __DATA_CONST.__const: 0x4810
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d18
+  __DATA_CONST.__objc_selrefs: 0x3d68
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x138
+  __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x310
-  __DATA_CONST.__got: 0xbf8
-  __AUTH_CONST.__const: 0x1328
-  __AUTH_CONST.__cfstring: 0x7fa0
-  __AUTH_CONST.__objc_const: 0x6128
+  __DATA_CONST.__got: 0xc10
+  __AUTH_CONST.__const: 0x13a8
+  __AUTH_CONST.__cfstring: 0x81a0
+  __AUTH_CONST.__objc_const: 0x63a8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x1120
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x540
+  __AUTH_CONST.__auth_got: 0x1130
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x558
   __DATA.__data: 0x418
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0xfa0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 3378
-  Symbols:   6750
-  CStrings:  2701
+  Functions: 3412
+  Symbols:   6830
+  CStrings:  2736
 
Symbols:
+ +[CSAccessMetricsRegistry sharedRegistry]
+ +[CSAccessMetricsReporter reportAccessForClient:target:kind:]
+ -[CSAccessMetricsRegistry .cxx_destruct]
+ -[CSAccessMetricsRegistry claimFirstSightOfClient:target:kind:]
+ -[CSAccessMetricsRegistry init]
+ -[CSAccessTuple .cxx_destruct]
+ -[CSAccessTuple hash]
+ -[CSAccessTuple initWithClient:target:kind:]
+ -[CSAccessTuple isEqual:]
+ -[MDSearchableIndexService _processIndexDataForBundle:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:completionHandler:]
+ -[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]
+ -[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]
+ GCC_except_table1028
+ GCC_except_table1029
+ GCC_except_table1054
+ GCC_except_table1095
+ GCC_except_table1100
+ GCC_except_table1151
+ GCC_except_table1185
+ GCC_except_table1191
+ GCC_except_table1192
+ GCC_except_table1199
+ GCC_except_table1201
+ GCC_except_table1210
+ GCC_except_table1212
+ GCC_except_table1227
+ GCC_except_table1233
+ GCC_except_table1237
+ GCC_except_table1251
+ GCC_except_table1267
+ GCC_except_table1274
+ GCC_except_table1281
+ GCC_except_table1288
+ GCC_except_table1295
+ GCC_except_table1312
+ GCC_except_table1390
+ GCC_except_table1391
+ GCC_except_table1393
+ GCC_except_table1400
+ GCC_except_table1460
+ GCC_except_table1467
+ GCC_except_table1594
+ GCC_except_table1595
+ GCC_except_table324
+ GCC_except_table342
+ GCC_except_table348
+ GCC_except_table382
+ GCC_except_table396
+ GCC_except_table429
+ GCC_except_table430
+ GCC_except_table434
+ GCC_except_table457
+ GCC_except_table486
+ GCC_except_table487
+ GCC_except_table49
+ GCC_except_table502
+ GCC_except_table503
+ GCC_except_table53
+ GCC_except_table533
+ GCC_except_table557
+ GCC_except_table56
+ GCC_except_table571
+ GCC_except_table574
+ GCC_except_table585
+ GCC_except_table586
+ GCC_except_table587
+ GCC_except_table60
+ GCC_except_table625
+ GCC_except_table639
+ GCC_except_table651
+ GCC_except_table674
+ GCC_except_table680
+ GCC_except_table699
+ GCC_except_table700
+ GCC_except_table710
+ GCC_except_table738
+ GCC_except_table763
+ GCC_except_table764
+ GCC_except_table765
+ GCC_except_table791
+ GCC_except_table857
+ GCC_except_table881
+ GCC_except_table903
+ GCC_except_table907
+ GCC_except_table911
+ GCC_except_table939
+ GCC_except_table968
+ GCC_except_table999
+ _CSAccessMetricsReportQuery
+ _CSAccessMetricsSendQueue.onceToken
+ _CSAccessMetricsSendQueue.queue
+ _CSShouldTraceMessagesDonation
+ _OBJC_CLASS_$_CSAccessMetricsRegistry
+ _OBJC_CLASS_$_CSAccessMetricsReporter
+ _OBJC_CLASS_$_CSAccessTuple
+ _OBJC_IVAR_$_CSAccessMetricsRegistry._lock
+ _OBJC_IVAR_$_CSAccessMetricsRegistry._seen
+ _OBJC_IVAR_$_CSAccessTuple._client
+ _OBJC_IVAR_$_CSAccessTuple._hash
+ _OBJC_IVAR_$_CSAccessTuple._kind
+ _OBJC_IVAR_$_CSAccessTuple._target
+ _OBJC_METACLASS_$_CSAccessMetricsRegistry
+ _OBJC_METACLASS_$_CSAccessMetricsReporter
+ _OBJC_METACLASS_$_CSAccessTuple
+ __OBJC_$_CLASS_METHODS_CSAccessMetricsRegistry
+ __OBJC_$_CLASS_METHODS_CSAccessMetricsReporter
+ __OBJC_$_INSTANCE_METHODS_CSAccessMetricsRegistry
+ __OBJC_$_INSTANCE_METHODS_CSAccessTuple
+ __OBJC_$_INSTANCE_VARIABLES_CSAccessMetricsRegistry
+ __OBJC_$_INSTANCE_VARIABLES_CSAccessTuple
+ __OBJC_CLASS_RO_$_CSAccessMetricsRegistry
+ __OBJC_CLASS_RO_$_CSAccessMetricsReporter
+ __OBJC_CLASS_RO_$_CSAccessTuple
+ __OBJC_METACLASS_RO_$_CSAccessMetricsRegistry
+ __OBJC_METACLASS_RO_$_CSAccessMetricsReporter
+ __OBJC_METACLASS_RO_$_CSAccessTuple
+ __SDEventMonitorSetUserInfoError
+ ___234-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke
+ ___234-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
+ ___234-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3
+ ___234-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke_4
+ ___234-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke_5
+ ___242-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke
+ ___242-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
+ ___41+[CSAccessMetricsRegistry sharedRegistry]_block_invoke
+ ___CSAccessMetricsSendQueue_block_invoke
+ ___CSAccessMetricsSend_block_invoke
+ ___CSAccessMetricsSend_block_invoke_2
+ ____bgst_queue_block_invoke
+ ___bgst_complete_task_block_invoke
+ ___bgst_expire_task_block_invoke
+ ___bgst_register_task_block_invoke
+ ___block_descriptor_160_e8_32s40s48s56s64s72s80r88r96r104r112r120w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40lw120l8r80l8r88l8s32l8s40l8r96l8r104l8r112l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_162_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0ls32l8s120l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s104s112s120r128r136r_e40_v16?0"SPConcreteCoreSpotlightIndexer"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8r120l8r128l8r136l8
+ ___block_descriptor_202_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136bs144w_e18_v20?0^{__SI=}8C16lw144l8s136l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8
+ ___block_descriptor_48_e8_32s40s_e25_v16?0"OSLogEventProxy"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e37_v24?0Q8"OSLogEventStreamPosition"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_73_e8_32s40s48s56r64r_e5_v8?0lr56l8r64l8s32l8s40l8s48l8
+ ___logForCSLogCategoryDonationTracing_block_invoke
+ ___syslogCollectSlice_block_invoke
+ ___syslogMakeStream_block_invoke
+ __bgst_queue
+ __bgst_queue.onceToken
+ __bgst_queue.queue
+ _bgst_complete_task
+ _bgst_expire_task
+ _bgst_register_task
+ _kSPUserActivityPurgeTargets_block_invoke_11.registered
+ _kSyslogSliceDurations
+ _logForCSLogCategoryDonationTracing
+ _logForCSLogCategoryDonationTracing.onceToken
+ _logForCSLogCategoryDonationTracing.sDonationTracingLog
+ _objc_msgSend$_processIndexDataForBundle:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:completionHandler:
+ _objc_msgSend$claimFirstSightOfClient:target:kind:
+ _objc_msgSend$indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:
+ _objc_msgSend$indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:
+ _objc_msgSend$initWithClient:target:kind:
+ _objc_msgSend$lossCount
+ _objc_msgSend$lossEndUnixDate
+ _objc_msgSend$lossStartUnixDate
+ _objc_msgSend$numberWithUnsignedChar:
+ _objc_msgSend$predicateFrameworkGenerated
+ _objc_msgSend$predicateSearchToolGenerated
+ _objc_msgSend$reportAccessForClient:target:kind:
+ _objc_msgSend$setTarget:
+ _objc_msgSend$sharedRegistry
+ _objc_msgSend$unixDate
+ _sharedRegistry.onceToken
+ _sharedRegistry.sharedInstance
+ _syslogDateString
+ _syslogEventTimestamp
+ _syslogFileGeneration
+ _syslogLocalTimeString
+ _syslogLossMarker
+ _syslogRotateGenerations
+ _syslogSliceStamp
+ _syslogWriteHeader
+ _syslogWriteLine
+ _syslogWriteTrailer
+ _xpc_data_get_bytes_ptr
+ _xpc_data_get_length
- -[MDSearchableIndexService _processIndexDataForBundle:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:completionHandler:]
- -[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]
- -[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]
- GCC_except_table1012
- GCC_except_table1013
- GCC_except_table1022
- GCC_except_table1039
- GCC_except_table1083
- GCC_except_table1088
- GCC_except_table1139
- GCC_except_table1173
- GCC_except_table1179
- GCC_except_table1180
- GCC_except_table1186
- GCC_except_table1187
- GCC_except_table1188
- GCC_except_table1189
- GCC_except_table1215
- GCC_except_table1221
- GCC_except_table1225
- GCC_except_table1239
- GCC_except_table1255
- GCC_except_table1262
- GCC_except_table1269
- GCC_except_table1276
- GCC_except_table1283
- GCC_except_table1300
- GCC_except_table1378
- GCC_except_table1379
- GCC_except_table1381
- GCC_except_table1388
- GCC_except_table1448
- GCC_except_table1455
- GCC_except_table1582
- GCC_except_table1583
- GCC_except_table314
- GCC_except_table322
- GCC_except_table338
- GCC_except_table362
- GCC_except_table386
- GCC_except_table419
- GCC_except_table420
- GCC_except_table424
- GCC_except_table447
- GCC_except_table476
- GCC_except_table477
- GCC_except_table48
- GCC_except_table492
- GCC_except_table493
- GCC_except_table50
- GCC_except_table523
- GCC_except_table54
- GCC_except_table547
- GCC_except_table561
- GCC_except_table564
- GCC_except_table57
- GCC_except_table575
- GCC_except_table576
- GCC_except_table577
- GCC_except_table61
- GCC_except_table615
- GCC_except_table629
- GCC_except_table640
- GCC_except_table659
- GCC_except_table665
- GCC_except_table684
- GCC_except_table685
- GCC_except_table695
- GCC_except_table723
- GCC_except_table748
- GCC_except_table749
- GCC_except_table750
- GCC_except_table776
- GCC_except_table842
- GCC_except_table866
- GCC_except_table887
- GCC_except_table891
- GCC_except_table895
- GCC_except_table923
- GCC_except_table952
- GCC_except_table983
- _OUTLINED_FUNCTION_46
- __SDEventMonitorErrorMake
- ___215-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke
- ___215-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
- ___215-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke_3
- ___215-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke_4
- ___215-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke_5
- ___223-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke
- ___223-[SPCoreSpotlightIndexer indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke_2
- ___block_descriptor_152_e8_32s40s48s56s64s72r80r88r96r104r112w_e69_v48?0"SPQueryJob"8q16Q24^{__MDStoreOIDArray=}32^{__MDPlistBytes=}40lw112l8r72l8s32l8r80l8r88l8r96l8r104l8s40l8s48l8s56l8s64l8
- ___block_descriptor_154_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0ls32l8s120l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
- ___block_descriptor_160_e8_32s40s48s56s64s72s80s88s96s104s112s120r128r136r_e40_v16?0"SPConcreteCoreSpotlightIndexer"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8r120l8r128l8r136l8
- ___block_descriptor_194_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136bs144w_e18_v20?0^{__SI=}8C16lw144l8s136l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8
- ___block_descriptor_40_e8_32s_e25_v16?0"OSLogEventProxy"8ls32l8
- ___block_descriptor_40_e8_32s_e37_v24?0Q8"OSLogEventStreamPosition"16ls32l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8r64l8s32l8s40l8s48l8
- ___collectSpotlightLogs_block_invoke_2
- _objc_msgSend$_processIndexDataForBundle:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:completionHandler:
- _objc_msgSend$dateByAddingTimeInterval:
- _objc_msgSend$indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:
- _objc_msgSend$indexFromBundle:fromClient:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:
- _objc_msgSend$truncateAtOffset:error:
CStrings:
+ "### BEGIN slice=[%@, %@]\n"
+ "### END status=%s events=%llu lossEvents=%llu lossMessages=%llu%s writeFailures=%llu\n"
+ "### LOG LOSS: %u%s message(s) dropped between %@ and %@\n"
+ "###collectSpotlightLogs Deadline reached after %zu of %zu slices"
+ "###collectSpotlightLogs Failed to create stream for slice"
+ "###collectSpotlightLogs Getting spotlight oslog past 60 mins in %zu slices, newest first"
+ "###collectSpotlightLogs Timeout draining oslog handlers"
+ "###collectSpotlightLogs Write failed, log will be short: %@"
+ "%@.%06d%c%02ld%02ld"
+ "%Y%m%dT%H%M%S%z"
+ "%Y-%m-%d %H:%M:%S"
+ "%Y-%m-%d %H:%M:%S%z"
+ "%ld%@"
+ "%llu"
+ "(all)"
+ "+"
+ "+ (counter saturated)"
+ "-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:donationXPCTraceID:deletes:canCreateNewIndex:completionHandler:]_block_invoke"
+ ".1.%@.log"
+ "23F"
+ "3rd party"
+ "Access"
+ "BGST activity:%@ already registered, launch handler unchanged"
+ "BGST activity:%@ rejected, never registered in this process"
+ "ClientBundleID"
+ "DaemonName"
+ "Donation dispatched to concrete indexer, donationXPCTraceID=%llu bundleID=%@ dataclass=%@ itemsBytes=%lu deletesBytes=%lu"
+ "DonationTracing"
+ "Failed to deserialize user info property list, class:%@, error:%@"
+ "Failed to expire BGST activity:%@, completing instead, error:%@"
+ "IsCrossBundle"
+ "Received \"%s\" notification with no event name"
+ "Registered BGST activity:%@"
+ "TRUNCATED-deadline"
+ "TRUNCATED-no-stream"
+ "TRUNCATED-undrained"
+ "TargetBundleID"
+ "com.apple.corespotlight.syslog-collect"
+ "com.apple.distnoted.matching.trusted"
+ "com.apple.searchd.bgst"
+ "com.apple.spotlight.CSAccessMetrics.send"
+ "com.apple.spotlight.index.BundleAccess"
+ "complete"
+ "donation-xpc-trace-id"
+ "invalid"
+ "stream-error"
- "###collectSpotlightLogs  Writing to file: %s"
- "###collectSpotlightLogs Failed to truncate file: %s"
- "###collectSpotlightLogs Getting spotlight oslog past 60 mins"
- "###collectSpotlightLogs Timeout on getting oslog stream"
- "-[SPConcreteCoreSpotlightIndexer indexFromBundle:fromClient:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:donationTimestamp:deletes:canCreateNewIndex:completionHandler:]_block_invoke"
- ".%d.log"
- ".1.log"
- "Failed to expire task %@ with error: %@"
- "Failed to expire task with error"
- "Registering BGST activity:%@"
- "Registering BGST repeating task %@"
```
