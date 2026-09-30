## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-800.14.111.0.0
-  __TEXT.__text: 0x1950b4
+800.20.101.0.0
+  __TEXT.__text: 0x19646c
   __TEXT.__auth_stubs: 0xf00
-  __TEXT.__objc_methlist: 0x12f3c
+  __TEXT.__objc_methlist: 0x130f4
   __TEXT.__const: 0x2f8
-  __TEXT.__gcc_except_tab: 0x4510
-  __TEXT.__oslogstring: 0x146cf
-  __TEXT.__cstring: 0x13fc3
-  __TEXT.__unwind_info: 0x5ae8
-  __TEXT.__objc_classname: 0x1e05
-  __TEXT.__objc_methname: 0x2a95e
-  __TEXT.__objc_methtype: 0x456b
-  __TEXT.__objc_stubs: 0x19d00
-  __DATA_CONST.__got: 0xa38
-  __DATA_CONST.__const: 0x60f0
-  __DATA_CONST.__objc_classlist: 0x878
+  __TEXT.__gcc_except_tab: 0x4674
+  __TEXT.__oslogstring: 0x146d4
+  __TEXT.__cstring: 0x1400d
+  __TEXT.__unwind_info: 0x5b90
+  __TEXT.__objc_classname: 0x1e86
+  __TEXT.__objc_methname: 0x2ad02
+  __TEXT.__objc_methtype: 0x4683
+  __TEXT.__objc_stubs: 0x19f80
+  __DATA_CONST.__got: 0xa48
+  __DATA_CONST.__const: 0x6178
+  __DATA_CONST.__objc_classlist: 0x888
   __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x120
+  __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8510
+  __DATA_CONST.__objc_selrefs: 0x85d0
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x810
+  __DATA_CONST.__objc_superrefs: 0x820
   __DATA_CONST.__objc_arraydata: 0x1320
   __AUTH_CONST.__auth_got: 0x790
-  __AUTH_CONST.__const: 0x25c0
-  __AUTH_CONST.__cfstring: 0x154c0
-  __AUTH_CONST.__objc_const: 0x1dea8
+  __AUTH_CONST.__const: 0x2620
+  __AUTH_CONST.__cfstring: 0x15540
+  __AUTH_CONST.__objc_const: 0x1e238
   __AUTH_CONST.__objc_intobj: 0x5b8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x17bc
-  __DATA.__data: 0xf48
+  __AUTH.__objc_data: 0x5a0
+  __DATA.__objc_ivar: 0x17e4
+  __DATA.__data: 0x1008
   __DATA.__bss: 0xa88
   __DATA.__common: 0x21
   __DATA_DIRTY.__objc_data: 0x4fb0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B130BC07-4FAB-3566-850B-88F6E2D44EEF
-  Functions: 8407
-  Symbols:   25972
-  CStrings:  14792
+  UUID: 1C890D41-6873-3917-A858-3183B4BFB480
+  Functions: 8447
+  Symbols:   26119
+  CStrings:  14850
 
Symbols:
+ -[CPLBackgroundActivity reportThroughputWorkForMetrics:itemCount:done:]
+ -[CPLEngineSyncTask setThroughputReporter:]
+ -[CPLEngineSyncTask withThroughputReporter:]
+ -[CPLPullFromTransportScopeTask addCountOfPulledAssets:]
+ -[CPLStatus delegateQueue]
+ -[CPLStatus setDelegateQueue:]
+ -[CPLSyncSession makeThroughputReporterForCategory:]
+ -[CPLSyncSession throughputReporter:addedItemCount:]
+ -[CPLSyncSession throughputReporterDidFinish:]
+ -[CPLSyncSessionThroughputMetrics .cxx_destruct]
+ -[CPLSyncSessionThroughputMetrics initWithIdentifier:]
+ -[CPLSyncSessionThroughputMetrics metricsIdentifier]
+ -[CPLSyncSessionThroughputMetrics setStartTime:]
+ -[CPLSyncSessionThroughputMetrics setTotalCount:]
+ -[CPLSyncSessionThroughputMetrics startTime]
+ -[CPLSyncSessionThroughputMetrics totalCount]
+ -[CPLSyncThroughputReporter .cxx_destruct]
+ -[CPLSyncThroughputReporter addCompletedWorkItemCount:]
+ -[CPLSyncThroughputReporter addCompletedWorkItemCount:kindOfWork:]
+ -[CPLSyncThroughputReporter delegate]
+ -[CPLSyncThroughputReporter endTrackingWork]
+ -[CPLSyncThroughputReporter initWithCategory:parentMetrics:]
+ -[CPLSyncThroughputReporter initWithCategory:parentReport:]
+ -[CPLSyncThroughputReporter makeChildReportForCategory:]
+ -[CPLSyncThroughputReporter makeSiblingReportForCategory:]
+ -[CPLSyncThroughputReporter metrics]
+ -[CPLSyncThroughputReporter setDelegate:]
+ -[CPLSyncThroughputReporter setMetrics:]
+ -[CPLSyncThroughputReporter startTrackingWork]
+ GCC_except_table1006
+ GCC_except_table1008
+ GCC_except_table1180
+ GCC_except_table1232
+ GCC_except_table1236
+ GCC_except_table1244
+ GCC_except_table1246
+ GCC_except_table1253
+ GCC_except_table1256
+ GCC_except_table1259
+ GCC_except_table1265
+ GCC_except_table1267
+ GCC_except_table1348
+ GCC_except_table1434
+ GCC_except_table1982
+ GCC_except_table2089
+ GCC_except_table2095
+ GCC_except_table2136
+ GCC_except_table2224
+ GCC_except_table2231
+ GCC_except_table2374
+ GCC_except_table2463
+ GCC_except_table2688
+ GCC_except_table2690
+ GCC_except_table2776
+ GCC_except_table2841
+ GCC_except_table2843
+ GCC_except_table2963
+ GCC_except_table2987
+ GCC_except_table3069
+ GCC_except_table3071
+ GCC_except_table3075
+ GCC_except_table3196
+ GCC_except_table3243
+ GCC_except_table3487
+ GCC_except_table3556
+ GCC_except_table3560
+ GCC_except_table3562
+ GCC_except_table3571
+ GCC_except_table3851
+ GCC_except_table3881
+ GCC_except_table3908
+ GCC_except_table3925
+ GCC_except_table3940
+ GCC_except_table3942
+ GCC_except_table3956
+ GCC_except_table3958
+ GCC_except_table3961
+ GCC_except_table4298
+ GCC_except_table4342
+ GCC_except_table4430
+ GCC_except_table4440
+ GCC_except_table4497
+ GCC_except_table4500
+ GCC_except_table4675
+ GCC_except_table4683
+ GCC_except_table4763
+ GCC_except_table4771
+ GCC_except_table4776
+ GCC_except_table4791
+ GCC_except_table4792
+ GCC_except_table4796
+ GCC_except_table4840
+ GCC_except_table4848
+ GCC_except_table4903
+ GCC_except_table4905
+ GCC_except_table4907
+ GCC_except_table4919
+ GCC_except_table5058
+ GCC_except_table5109
+ GCC_except_table5110
+ GCC_except_table5169
+ GCC_except_table5172
+ GCC_except_table5252
+ GCC_except_table5254
+ GCC_except_table5288
+ GCC_except_table5454
+ GCC_except_table5482
+ GCC_except_table5524
+ GCC_except_table5544
+ GCC_except_table5570
+ GCC_except_table5581
+ GCC_except_table5602
+ GCC_except_table5622
+ GCC_except_table5626
+ GCC_except_table5652
+ GCC_except_table5684
+ GCC_except_table5724
+ GCC_except_table5783
+ GCC_except_table5824
+ GCC_except_table5837
+ GCC_except_table5848
+ GCC_except_table5855
+ GCC_except_table5908
+ GCC_except_table6033
+ GCC_except_table6046
+ GCC_except_table6049
+ GCC_except_table6529
+ GCC_except_table6568
+ GCC_except_table6574
+ GCC_except_table6589
+ GCC_except_table6595
+ GCC_except_table6603
+ GCC_except_table6609
+ GCC_except_table6613
+ GCC_except_table6621
+ GCC_except_table6624
+ GCC_except_table6644
+ GCC_except_table6651
+ GCC_except_table6674
+ GCC_except_table6708
+ GCC_except_table6732
+ GCC_except_table6741
+ GCC_except_table6759
+ GCC_except_table6762
+ GCC_except_table6764
+ GCC_except_table6766
+ GCC_except_table6798
+ GCC_except_table6868
+ GCC_except_table687
+ GCC_except_table689
+ GCC_except_table693
+ GCC_except_table695
+ GCC_except_table7013
+ GCC_except_table7035
+ GCC_except_table704
+ GCC_except_table706
+ GCC_except_table7065
+ GCC_except_table708
+ GCC_except_table710
+ GCC_except_table712
+ GCC_except_table714
+ GCC_except_table716
+ GCC_except_table718
+ GCC_except_table720
+ GCC_except_table722
+ GCC_except_table724
+ GCC_except_table7248
+ GCC_except_table7257
+ GCC_except_table726
+ GCC_except_table7262
+ GCC_except_table7276
+ GCC_except_table7290
+ GCC_except_table7300
+ GCC_except_table7305
+ GCC_except_table733
+ GCC_except_table735
+ GCC_except_table737
+ GCC_except_table7386
+ GCC_except_table739
+ GCC_except_table741
+ GCC_except_table7487
+ GCC_except_table7496
+ GCC_except_table750
+ GCC_except_table752
+ GCC_except_table754
+ GCC_except_table7552
+ GCC_except_table756
+ GCC_except_table758
+ GCC_except_table7590
+ GCC_except_table7606
+ GCC_except_table7614
+ GCC_except_table7615
+ GCC_except_table7629
+ GCC_except_table778
+ GCC_except_table784
+ GCC_except_table793
+ GCC_except_table800
+ GCC_except_table811
+ GCC_except_table902
+ GCC_except_table988
+ _OBJC_CLASS_$_CPLSyncSessionThroughputMetrics
+ _OBJC_CLASS_$_CPLSyncThroughputReporter
+ _OBJC_IVAR_$_CPLEngineSyncTask._throughputReporter
+ _OBJC_IVAR_$_CPLEngineSyncTask._throughputReporterLock
+ _OBJC_IVAR_$_CPLStatus._delegateQueue
+ _OBJC_IVAR_$_CPLSyncSessionThroughputMetrics._metricsIdentifier
+ _OBJC_IVAR_$_CPLSyncSessionThroughputMetrics._startTime
+ _OBJC_IVAR_$_CPLSyncSessionThroughputMetrics._totalCount
+ _OBJC_IVAR_$_CPLSyncThroughputReporter._delegate
+ _OBJC_IVAR_$_CPLSyncThroughputReporter._kindOfWorkReporters
+ _OBJC_IVAR_$_CPLSyncThroughputReporter._metrics
+ _OBJC_IVAR_$_CPLSyncThroughputReporter._parentMetricsIdentifier
+ _OBJC_METACLASS_$_CPLSyncSessionThroughputMetrics
+ _OBJC_METACLASS_$_CPLSyncThroughputReporter
+ __OBJC_$_INSTANCE_METHODS_CPLSyncSessionThroughputMetrics
+ __OBJC_$_INSTANCE_METHODS_CPLSyncThroughputReporter
+ __OBJC_$_INSTANCE_VARIABLES_CPLSyncSessionThroughputMetrics
+ __OBJC_$_INSTANCE_VARIABLES_CPLSyncThroughputReporter
+ __OBJC_$_PROP_LIST_CPLSyncSessionThroughputMetrics
+ __OBJC_$_PROP_LIST_CPLSyncThroughputReporter
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLSyncSessionThroughputReporting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPLSyncThroughputReporterDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLSyncSessionThroughputReporting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPLSyncThroughputReporterDelegate
+ __OBJC_$_PROTOCOL_REFS_CPLSyncSessionThroughputReporting
+ __OBJC_$_PROTOCOL_REFS_CPLSyncThroughputReporterDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CPLBackgroundActivity
+ __OBJC_CLASS_RO_$_CPLSyncSessionThroughputMetrics
+ __OBJC_CLASS_RO_$_CPLSyncThroughputReporter
+ __OBJC_LABEL_PROTOCOL_$_CPLSyncSessionThroughputReporting
+ __OBJC_LABEL_PROTOCOL_$_CPLSyncThroughputReporterDelegate
+ __OBJC_METACLASS_RO_$_CPLSyncSessionThroughputMetrics
+ __OBJC_METACLASS_RO_$_CPLSyncThroughputReporter
+ __OBJC_PROTOCOL_$_CPLSyncSessionThroughputReporting
+ __OBJC_PROTOCOL_$_CPLSyncThroughputReporterDelegate
+ ___121-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:updatedFlags:newSyncAnchor:partnerScopesNeedingToPullChanges:]_block_invoke.51
+ ___121-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:updatedFlags:newSyncAnchor:partnerScopesNeedingToPullChanges:]_block_invoke.53
+ ___121-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:updatedFlags:newSyncAnchor:partnerScopesNeedingToPullChanges:]_block_invoke.55
+ ___121-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:updatedFlags:newSyncAnchor:partnerScopesNeedingToPullChanges:]_block_invoke.59
+ ___27-[CPLEngineSyncTask cancel]_block_invoke
+ ___27-[CPLEngineSyncTask launch]_block_invoke
+ ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke.117
+ ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke_2.118
+ ___37-[CPLUploadPushedChangesTask cancel:]_block_invoke.172
+ ___38-[CPLPushToTransportScopeTask _launch]_block_invoke.88
+ ___38-[CPLPushToTransportScopeTask _launch]_block_invoke_2.90
+ ___43-[CPLEngineSyncTask setThroughputReporter:]_block_invoke
+ ___44-[CPLEngineSyncTask taskDidFinishWithError:]_block_invoke
+ ___44-[CPLEngineSyncTask withThroughputReporter:]_block_invoke
+ ___46-[CPLPushToTransportScopeTask _launchSubTask:]_block_invoke_2
+ ___46-[CPLSyncSession throughputReporterDidFinish:]_block_invoke
+ ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke.67
+ ___52-[CPLSyncSession throughputReporter:addedItemCount:]_block_invoke
+ ___53-[CPLPullFromTransportScopeTask _launchNextQueryTask]_block_invoke.97
+ ___53-[CPLPullFromTransportScopeTask _launchNextQueryTask]_block_invoke.98
+ ___53-[CPLPullFromTransportScopeTask _launchNextQueryTask]_block_invoke.99
+ ___54-[CPLEngineMultiscopeSyncTask _launchTaskForNextScope]_block_invoke
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.126
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.129
+ ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke_2.127
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.144
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.155
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.157
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.158
+ ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.159
+ ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke.117
+ ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke_2.118
+ ___56-[CPLPullFromTransportScopeTask addCountOfPulledAssets:]_block_invoke
+ ___56-[CPLPullFromTransportScopeTask taskDidFinishWithError:]_block_invoke.145
+ ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke.102
+ ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke_2.103
+ ___60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.179
+ ___61-[CPLPullFromTransportScopeTask _launchQueryForClass:cursor:]_block_invoke.89
+ ___61-[CPLPullFromTransportScopeTask _launchQueryForClass:cursor:]_block_invoke_2.90
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.115
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.117
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke_2.118
+ ___67-[CPLPullFromTransportScopeTask _launchFetchChangesFromSyncAnchor:]_block_invoke.72
+ ___67-[CPLPullFromTransportScopeTask _launchFetchChangesFromSyncAnchor:]_block_invoke.78
+ ___67-[CPLPullFromTransportScopeTask _launchFetchChangesFromSyncAnchor:]_block_invoke_2.73
+ ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.110
+ ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.111
+ ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.112
+ ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.113
+ ___73-[CPLPullFromTransportScopeTask _checkExtraRecordsWithScopedIdentifiers:]_block_invoke.42
+ ___73-[CPLPullFromTransportScopeTask _checkExtraRecordsWithScopedIdentifiers:]_block_invoke_2.43
+ ___73-[CPLPullFromTransportScopeTask _checkExtraRecordsWithScopedIdentifiers:]_block_invoke_3.45
+ ___80-[CPLPullFromTransportScopeTask _relaunchFetchChangesFromOtherRewindSyncAnchors]_block_invoke.67
+ ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.127
+ ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.139
+ ___82-[CPLPullFromTransportScopeTask _handleNewBatchFromQuery:newCursor:inTransaction:]_block_invoke.82
+ ___88-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:newSyncAnchor:inTransaction:]_block_invoke.27
+ ___90-[CPLPullFromTransportScopeTask _extractAndMingleAssetsIfPossibleFromBatch:inTransaction:]_block_invoke.25
+ ___96-[CPLPullFromTransportScopeTask _updateLastFeatureVersionAndRelaunchFetchChangesFromSyncAnchor:]_block_invoke.60
+ ___Block_byref_object_copy_.10004
+ ___Block_byref_object_copy_.11238
+ ___Block_byref_object_copy_.11533
+ ___Block_byref_object_copy_.12293
+ ___Block_byref_object_copy_.13111
+ ___Block_byref_object_copy_.1344
+ ___Block_byref_object_copy_.13691
+ ___Block_byref_object_copy_.14017
+ ___Block_byref_object_copy_.14204
+ ___Block_byref_object_copy_.15021
+ ___Block_byref_object_copy_.15629
+ ___Block_byref_object_copy_.16355
+ ___Block_byref_object_copy_.16677
+ ___Block_byref_object_copy_.17148
+ ___Block_byref_object_copy_.1744
+ ___Block_byref_object_copy_.17750
+ ___Block_byref_object_copy_.18573
+ ___Block_byref_object_copy_.20046
+ ___Block_byref_object_copy_.20186
+ ___Block_byref_object_copy_.2053
+ ___Block_byref_object_copy_.20698
+ ___Block_byref_object_copy_.21312
+ ___Block_byref_object_copy_.21794
+ ___Block_byref_object_copy_.22132
+ ___Block_byref_object_copy_.23148
+ ___Block_byref_object_copy_.23449
+ ___Block_byref_object_copy_.24285
+ ___Block_byref_object_copy_.2541
+ ___Block_byref_object_copy_.2619
+ ___Block_byref_object_copy_.2940
+ ___Block_byref_object_copy_.3257
+ ___Block_byref_object_copy_.5773
+ ___Block_byref_object_copy_.6478
+ ___Block_byref_object_copy_.6641
+ ___Block_byref_object_copy_.7257
+ ___Block_byref_object_copy_.7636
+ ___Block_byref_object_copy_.7922
+ ___Block_byref_object_copy_.8355
+ ___Block_byref_object_copy_.9759
+ ___Block_byref_object_dispose_.10005
+ ___Block_byref_object_dispose_.11239
+ ___Block_byref_object_dispose_.11534
+ ___Block_byref_object_dispose_.12294
+ ___Block_byref_object_dispose_.13112
+ ___Block_byref_object_dispose_.1345
+ ___Block_byref_object_dispose_.13692
+ ___Block_byref_object_dispose_.14018
+ ___Block_byref_object_dispose_.14205
+ ___Block_byref_object_dispose_.15022
+ ___Block_byref_object_dispose_.15630
+ ___Block_byref_object_dispose_.16356
+ ___Block_byref_object_dispose_.16678
+ ___Block_byref_object_dispose_.17149
+ ___Block_byref_object_dispose_.1745
+ ___Block_byref_object_dispose_.17751
+ ___Block_byref_object_dispose_.18574
+ ___Block_byref_object_dispose_.20047
+ ___Block_byref_object_dispose_.20187
+ ___Block_byref_object_dispose_.2054
+ ___Block_byref_object_dispose_.20699
+ ___Block_byref_object_dispose_.21313
+ ___Block_byref_object_dispose_.21795
+ ___Block_byref_object_dispose_.22133
+ ___Block_byref_object_dispose_.23149
+ ___Block_byref_object_dispose_.23450
+ ___Block_byref_object_dispose_.24286
+ ___Block_byref_object_dispose_.2542
+ ___Block_byref_object_dispose_.2620
+ ___Block_byref_object_dispose_.2941
+ ___Block_byref_object_dispose_.3258
+ ___Block_byref_object_dispose_.5774
+ ___Block_byref_object_dispose_.6479
+ ___Block_byref_object_dispose_.6642
+ ___Block_byref_object_dispose_.7258
+ ___Block_byref_object_dispose_.7637
+ ___Block_byref_object_dispose_.7923
+ ___Block_byref_object_dispose_.8356
+ ___Block_byref_object_dispose_.9760
+ ___CPLConfigurationOSLogDomain.19407
+ ___CPLConfigurationOSLogDomain.onceToken.19413
+ ___CPLConfigurationOSLogDomain.result.19415
+ ___CPLForceSyncOSLogDomain.20841
+ ___CPLForceSyncOSLogDomain.onceToken.20850
+ ___CPLForceSyncOSLogDomain.result.20851
+ ___CPLSchedulerOSLogDomain.7584
+ ___CPLSchedulerOSLogDomain.onceToken.7585
+ ___CPLSchedulerOSLogDomain.result.7586
+ ___CPLSessionOSLogDomain.16226
+ ___CPLSessionOSLogDomain.18133
+ ___CPLSessionOSLogDomain.22735
+ ___CPLSessionOSLogDomain.onceToken.16228
+ ___CPLSessionOSLogDomain.onceToken.18138
+ ___CPLSessionOSLogDomain.onceToken.22737
+ ___CPLSessionOSLogDomain.result.16229
+ ___CPLSessionOSLogDomain.result.18139
+ ___CPLSessionOSLogDomain.result.22739
+ ___CPLStorageOSLogDomain.11206
+ ___CPLStorageOSLogDomain.11291
+ ___CPLStorageOSLogDomain.17718
+ ___CPLStorageOSLogDomain.20166
+ ___CPLStorageOSLogDomain.2035
+ ___CPLStorageOSLogDomain.21459
+ ___CPLStorageOSLogDomain.22119
+ ___CPLStorageOSLogDomain.22367
+ ___CPLStorageOSLogDomain.6231
+ ___CPLStorageOSLogDomain.7872
+ ___CPLStorageOSLogDomain.8607
+ ___CPLStorageOSLogDomain.9048
+ ___CPLStorageOSLogDomain.9214
+ ___CPLStorageOSLogDomain.9407
+ ___CPLStorageOSLogDomain.onceToken.11217
+ ___CPLStorageOSLogDomain.onceToken.11294
+ ___CPLStorageOSLogDomain.onceToken.14541
+ ___CPLStorageOSLogDomain.onceToken.17720
+ ___CPLStorageOSLogDomain.onceToken.20168
+ ___CPLStorageOSLogDomain.onceToken.2037
+ ___CPLStorageOSLogDomain.onceToken.20446
+ ___CPLStorageOSLogDomain.onceToken.21463
+ ___CPLStorageOSLogDomain.onceToken.22124
+ ___CPLStorageOSLogDomain.onceToken.22375
+ ___CPLStorageOSLogDomain.onceToken.6233
+ ___CPLStorageOSLogDomain.onceToken.7874
+ ___CPLStorageOSLogDomain.onceToken.8615
+ ___CPLStorageOSLogDomain.onceToken.9054
+ ___CPLStorageOSLogDomain.onceToken.9216
+ ___CPLStorageOSLogDomain.onceToken.9409
+ ___CPLStorageOSLogDomain.result.11219
+ ___CPLStorageOSLogDomain.result.11296
+ ___CPLStorageOSLogDomain.result.14543
+ ___CPLStorageOSLogDomain.result.17722
+ ___CPLStorageOSLogDomain.result.20170
+ ___CPLStorageOSLogDomain.result.2039
+ ___CPLStorageOSLogDomain.result.20447
+ ___CPLStorageOSLogDomain.result.21465
+ ___CPLStorageOSLogDomain.result.22126
+ ___CPLStorageOSLogDomain.result.22377
+ ___CPLStorageOSLogDomain.result.6235
+ ___CPLStorageOSLogDomain.result.7875
+ ___CPLStorageOSLogDomain.result.8616
+ ___CPLStorageOSLogDomain.result.9056
+ ___CPLStorageOSLogDomain.result.9217
+ ___CPLStorageOSLogDomain.result.9410
+ ___CPLStoreOSLogDomain.3045
+ ___CPLStoreOSLogDomain.onceToken.3046
+ ___CPLStoreOSLogDomain.result.3047
+ ___CPLTaskOSLogDomain.11478
+ ___CPLTaskOSLogDomain.1342
+ ___CPLTaskOSLogDomain.13991
+ ___CPLTaskOSLogDomain.14453
+ ___CPLTaskOSLogDomain.15525
+ ___CPLTaskOSLogDomain.17059
+ ___CPLTaskOSLogDomain.21259
+ ___CPLTaskOSLogDomain.23075
+ ___CPLTaskOSLogDomain.24240
+ ___CPLTaskOSLogDomain.2604
+ ___CPLTaskOSLogDomain.5461
+ ___CPLTaskOSLogDomain.7180
+ ___CPLTaskOSLogDomain.onceToken.11514
+ ___CPLTaskOSLogDomain.onceToken.1370
+ ___CPLTaskOSLogDomain.onceToken.13993
+ ___CPLTaskOSLogDomain.onceToken.14455
+ ___CPLTaskOSLogDomain.onceToken.15535
+ ___CPLTaskOSLogDomain.onceToken.17066
+ ___CPLTaskOSLogDomain.onceToken.21301
+ ___CPLTaskOSLogDomain.onceToken.23087
+ ___CPLTaskOSLogDomain.onceToken.24248
+ ___CPLTaskOSLogDomain.onceToken.2606
+ ___CPLTaskOSLogDomain.onceToken.5464
+ ___CPLTaskOSLogDomain.onceToken.7192
+ ___CPLTaskOSLogDomain.result.11516
+ ___CPLTaskOSLogDomain.result.1371
+ ___CPLTaskOSLogDomain.result.13995
+ ___CPLTaskOSLogDomain.result.14456
+ ___CPLTaskOSLogDomain.result.15536
+ ___CPLTaskOSLogDomain.result.17067
+ ___CPLTaskOSLogDomain.result.21302
+ ___CPLTaskOSLogDomain.result.23088
+ ___CPLTaskOSLogDomain.result.24249
+ ___CPLTaskOSLogDomain.result.2608
+ ___CPLTaskOSLogDomain.result.5466
+ ___CPLTaskOSLogDomain.result.7194
+ _____CPLConfigurationOSLogDomain_block_invoke.19418
+ _____CPLForceSyncOSLogDomain_block_invoke.20853
+ _____CPLSchedulerOSLogDomain_block_invoke.7588
+ _____CPLSessionOSLogDomain_block_invoke.16231
+ _____CPLSessionOSLogDomain_block_invoke.18141
+ _____CPLSessionOSLogDomain_block_invoke.22742
+ _____CPLStorageOSLogDomain_block_invoke.11222
+ _____CPLStorageOSLogDomain_block_invoke.11299
+ _____CPLStorageOSLogDomain_block_invoke.14548
+ _____CPLStorageOSLogDomain_block_invoke.17725
+ _____CPLStorageOSLogDomain_block_invoke.20173
+ _____CPLStorageOSLogDomain_block_invoke.2042
+ _____CPLStorageOSLogDomain_block_invoke.20453
+ _____CPLStorageOSLogDomain_block_invoke.21468
+ _____CPLStorageOSLogDomain_block_invoke.22129
+ _____CPLStorageOSLogDomain_block_invoke.22380
+ _____CPLStorageOSLogDomain_block_invoke.6238
+ _____CPLStorageOSLogDomain_block_invoke.7877
+ _____CPLStorageOSLogDomain_block_invoke.8618
+ _____CPLStorageOSLogDomain_block_invoke.9059
+ _____CPLStorageOSLogDomain_block_invoke.9219
+ _____CPLStorageOSLogDomain_block_invoke.9412
+ _____CPLStoreOSLogDomain_block_invoke.3049
+ _____CPLTaskOSLogDomain_block_invoke.11519
+ _____CPLTaskOSLogDomain_block_invoke.1373
+ _____CPLTaskOSLogDomain_block_invoke.13998
+ _____CPLTaskOSLogDomain_block_invoke.14458
+ _____CPLTaskOSLogDomain_block_invoke.15538
+ _____CPLTaskOSLogDomain_block_invoke.17069
+ _____CPLTaskOSLogDomain_block_invoke.21304
+ _____CPLTaskOSLogDomain_block_invoke.23090
+ _____CPLTaskOSLogDomain_block_invoke.24251
+ _____CPLTaskOSLogDomain_block_invoke.2611
+ _____CPLTaskOSLogDomain_block_invoke.5469
+ _____CPLTaskOSLogDomain_block_invoke.7197
+ ___block_descriptor_32_e35_v16?0"CPLSyncThroughputReporter"8l
+ ___block_descriptor_40_e35_v16?0"CPLSyncThroughputReporter"8l
+ ___block_descriptor_48_e35_v16?0"CPLSyncThroughputReporter"8l
+ ___block_descriptor_48_e8_32s40r_e35_v16?0"CPLSyncThroughputReporter"8lr40l8s32l8
+ ___block_literal_global.10108
+ ___block_literal_global.10429
+ ___block_literal_global.105.18931
+ ___block_literal_global.10825
+ ___block_literal_global.110.20998
+ ___block_literal_global.11064
+ ___block_literal_global.11218
+ ___block_literal_global.11295
+ ___block_literal_global.11515
+ ___block_literal_global.12.7996
+ ___block_literal_global.12414
+ ___block_literal_global.12636
+ ___block_literal_global.13.24560
+ ___block_literal_global.13132
+ ___block_literal_global.13994
+ ___block_literal_global.14.14489
+ ___block_literal_global.1411
+ ___block_literal_global.142.21002
+ ___block_literal_global.14252
+ ___block_literal_global.14488
+ ___block_literal_global.14542
+ ___block_literal_global.14705
+ ___block_literal_global.1490
+ ___block_literal_global.15238
+ ___block_literal_global.15258
+ ___block_literal_global.15323
+ ___block_literal_global.15543
+ ___block_literal_global.1571
+ ___block_literal_global.159.21003
+ ___block_literal_global.16081
+ ___block_literal_global.16296
+ ___block_literal_global.16856
+ ___block_literal_global.171.21004
+ ___block_literal_global.17171
+ ___block_literal_global.1741
+ ___block_literal_global.17515
+ ___block_literal_global.17721
+ ___block_literal_global.18151
+ ___block_literal_global.18323
+ ___block_literal_global.18461
+ ___block_literal_global.1873
+ ___block_literal_global.19044
+ ___block_literal_global.1908
+ ___block_literal_global.19414
+ ___block_literal_global.19799
+ ___block_literal_global.20169
+ ___block_literal_global.20333
+ ___block_literal_global.2038
+ ___block_literal_global.20449
+ ___block_literal_global.20994
+ ___block_literal_global.21319
+ ___block_literal_global.21464
+ ___block_literal_global.21638
+ ___block_literal_global.22125
+ ___block_literal_global.22376
+ ___block_literal_global.22536
+ ___block_literal_global.22738
+ ___block_literal_global.22888
+ ___block_literal_global.2307
+ ___block_literal_global.23144
+ ___block_literal_global.23775
+ ___block_literal_global.23911
+ ___block_literal_global.23983
+ ___block_literal_global.24.14206
+ ___block_literal_global.24423
+ ___block_literal_global.24537
+ ___block_literal_global.24658
+ ___block_literal_global.2482
+ ___block_literal_global.24843
+ ___block_literal_global.252
+ ___block_literal_global.2540
+ ___block_literal_global.2607
+ ___block_literal_global.27.16315
+ ___block_literal_global.271
+ ___block_literal_global.2957
+ ___block_literal_global.3024
+ ___block_literal_global.32.22504
+ ___block_literal_global.3274
+ ___block_literal_global.33.7308
+ ___block_literal_global.34.10001
+ ___block_literal_global.34.2479
+ ___block_literal_global.3546
+ ___block_literal_global.37.10745
+ ___block_literal_global.3782
+ ___block_literal_global.4017
+ ___block_literal_global.42.8003
+ ___block_literal_global.439
+ ___block_literal_global.4451
+ ___block_literal_global.4588
+ ___block_literal_global.4802
+ ___block_literal_global.5.24550
+ ___block_literal_global.50.7299
+ ___block_literal_global.5250
+ ___block_literal_global.5327
+ ___block_literal_global.54.5223
+ ___block_literal_global.5465
+ ___block_literal_global.5605
+ ___block_literal_global.57.8007
+ ___block_literal_global.6.15541
+ ___block_literal_global.6146
+ ___block_literal_global.6234
+ ___block_literal_global.6454
+ ___block_literal_global.6750
+ ___block_literal_global.7193
+ ___block_literal_global.72.16814
+ ___block_literal_global.7307
+ ___block_literal_global.77.16076
+ ___block_literal_global.7706
+ ___block_literal_global.7993
+ ___block_literal_global.8738
+ ___block_literal_global.8949
+ ___block_literal_global.9055
+ ___block_literal_global.9153
+ ___block_literal_global.93.18935
+ ___block_literal_global.93.7769
+ ___block_literal_global.9458
+ ___block_literal_global.9630
+ ___block_literal_global.9900
+ ___cpl_dispatch_async_block_invoke.10085
+ ___cpl_dispatch_async_block_invoke.11474
+ ___cpl_dispatch_async_block_invoke.12115
+ ___cpl_dispatch_async_block_invoke.1376
+ ___cpl_dispatch_async_block_invoke.14003
+ ___cpl_dispatch_async_block_invoke.14377
+ ___cpl_dispatch_async_block_invoke.14450
+ ___cpl_dispatch_async_block_invoke.15618
+ ___cpl_dispatch_async_block_invoke.16634
+ ___cpl_dispatch_async_block_invoke.17125
+ ___cpl_dispatch_async_block_invoke.17471
+ ___cpl_dispatch_async_block_invoke.17958
+ ___cpl_dispatch_async_block_invoke.1822
+ ___cpl_dispatch_async_block_invoke.18457
+ ___cpl_dispatch_async_block_invoke.19393
+ ___cpl_dispatch_async_block_invoke.20681
+ ___cpl_dispatch_async_block_invoke.21257
+ ___cpl_dispatch_async_block_invoke.21646
+ ___cpl_dispatch_async_block_invoke.22890
+ ___cpl_dispatch_async_block_invoke.23092
+ ___cpl_dispatch_async_block_invoke.24293
+ ___cpl_dispatch_async_block_invoke.2944
+ ___cpl_dispatch_async_block_invoke.6693
+ ___cpl_dispatch_async_block_invoke.7178
+ ___cpl_dispatch_async_block_invoke.7447
+ ___cpl_dispatch_async_block_invoke.7883
+ ___cpl_dispatch_async_block_invoke.9743
+ __doProtected:.onceToken.15257
+ __doProtected:.onceToken.22887
+ __doProtected:.queue.22889
+ __statusDidChange.12311
+ _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.18954
+ _initWithCoder:.logOnceToken.20335
+ _initWithCoder:.onceToken.10769
+ _initWithCoder:.onceToken.14251
+ _initWithCoder:.onceToken.18150
+ _initWithCoder:.onceToken.20332
+ _initWithCoder:.onceToken.22535
+ _initWithCoder:.onceToken.24842
+ _initWithCoder:.onceToken.5222
+ _initWithCoder:.onceToken.5326
+ _initWithCoder:.onceToken.6449
+ _initWithCoder:.pushContextsClasses.22537
+ _initWithCoder:.stringClass.10770
+ _objc_msgSend$addCompletedWorkItemCount:
+ _objc_msgSend$addCompletedWorkItemCount:kindOfWork:
+ _objc_msgSend$addCountOfPulledAssets:
+ _objc_msgSend$endTrackingWork
+ _objc_msgSend$initWithCategory:parentMetrics:
+ _objc_msgSend$initWithCategory:parentReport:
+ _objc_msgSend$makeChildReportForCategory:
+ _objc_msgSend$makeThroughputReporterForCategory:
+ _objc_msgSend$metrics
+ _objc_msgSend$metricsIdentifier
+ _objc_msgSend$reportThroughputWorkForMetrics:itemCount:done:
+ _objc_msgSend$setStartTime:
+ _objc_msgSend$setThroughputReporter:
+ _objc_msgSend$setTotalCount:
+ _objc_msgSend$startTime
+ _objc_msgSend$startTrackingWork
+ _objc_msgSend$throughputReporter:addedItemCount:
+ _objc_msgSend$throughputReporterDidFinish:
+ _objc_msgSend$totalCount
+ _objc_msgSend$withThroughputReporter:
+ _propertiesForChangeType:.onceToken.15093
+ _propertiesForChangeType:.onceToken.18968
+ _propertiesForChangeType:.onceToken.23910
+ _propertiesForChangeType:.properties.23912
- GCC_except_table1001
- GCC_except_table1003
- GCC_except_table1175
- GCC_except_table1222
- GCC_except_table1231
- GCC_except_table1239
- GCC_except_table1241
- GCC_except_table1248
- GCC_except_table1251
- GCC_except_table1254
- GCC_except_table1260
- GCC_except_table1262
- GCC_except_table1343
- GCC_except_table1429
- GCC_except_table1977
- GCC_except_table2084
- GCC_except_table2090
- GCC_except_table2131
- GCC_except_table2219
- GCC_except_table2226
- GCC_except_table2369
- GCC_except_table2456
- GCC_except_table2680
- GCC_except_table2682
- GCC_except_table2768
- GCC_except_table2833
- GCC_except_table2835
- GCC_except_table2955
- GCC_except_table2979
- GCC_except_table3055
- GCC_except_table3059
- GCC_except_table3061
- GCC_except_table3188
- GCC_except_table3235
- GCC_except_table3479
- GCC_except_table3548
- GCC_except_table3552
- GCC_except_table3554
- GCC_except_table3563
- GCC_except_table3843
- GCC_except_table3873
- GCC_except_table3900
- GCC_except_table3917
- GCC_except_table3924
- GCC_except_table3934
- GCC_except_table3948
- GCC_except_table3950
- GCC_except_table3952
- GCC_except_table4289
- GCC_except_table4333
- GCC_except_table4421
- GCC_except_table4431
- GCC_except_table4488
- GCC_except_table4491
- GCC_except_table4666
- GCC_except_table4674
- GCC_except_table4754
- GCC_except_table4758
- GCC_except_table4762
- GCC_except_table4782
- GCC_except_table4783
- GCC_except_table4787
- GCC_except_table4831
- GCC_except_table4839
- GCC_except_table4894
- GCC_except_table4896
- GCC_except_table4898
- GCC_except_table4910
- GCC_except_table5049
- GCC_except_table5091
- GCC_except_table5101
- GCC_except_table5160
- GCC_except_table5163
- GCC_except_table5437
- GCC_except_table5465
- GCC_except_table5507
- GCC_except_table5527
- GCC_except_table5553
- GCC_except_table5564
- GCC_except_table5585
- GCC_except_table5605
- GCC_except_table5609
- GCC_except_table5635
- GCC_except_table5667
- GCC_except_table5707
- GCC_except_table5766
- GCC_except_table5807
- GCC_except_table5820
- GCC_except_table5831
- GCC_except_table5838
- GCC_except_table5891
- GCC_except_table6016
- GCC_except_table6029
- GCC_except_table6032
- GCC_except_table6512
- GCC_except_table6551
- GCC_except_table6555
- GCC_except_table6557
- GCC_except_table6578
- GCC_except_table6586
- GCC_except_table6592
- GCC_except_table6596
- GCC_except_table6604
- GCC_except_table6607
- GCC_except_table6627
- GCC_except_table6634
- GCC_except_table6657
- GCC_except_table6691
- GCC_except_table6715
- GCC_except_table6724
- GCC_except_table6742
- GCC_except_table6745
- GCC_except_table6747
- GCC_except_table6749
- GCC_except_table6781
- GCC_except_table6851
- GCC_except_table688
- GCC_except_table690
- GCC_except_table699
- GCC_except_table6996
- GCC_except_table701
- GCC_except_table7018
- GCC_except_table703
- GCC_except_table7048
- GCC_except_table705
- GCC_except_table707
- GCC_except_table709
- GCC_except_table711
- GCC_except_table713
- GCC_except_table715
- GCC_except_table717
- GCC_except_table719
- GCC_except_table721
- GCC_except_table7231
- GCC_except_table7240
- GCC_except_table7245
- GCC_except_table7259
- GCC_except_table7273
- GCC_except_table728
- GCC_except_table7283
- GCC_except_table7288
- GCC_except_table730
- GCC_except_table732
- GCC_except_table734
- GCC_except_table736
- GCC_except_table7367
- GCC_except_table7448
- GCC_except_table745
- GCC_except_table7457
- GCC_except_table747
- GCC_except_table749
- GCC_except_table751
- GCC_except_table7513
- GCC_except_table753
- GCC_except_table7550
- GCC_except_table7566
- GCC_except_table7574
- GCC_except_table7575
- GCC_except_table7589
- GCC_except_table773
- GCC_except_table779
- GCC_except_table788
- GCC_except_table795
- GCC_except_table806
- GCC_except_table897
- GCC_except_table983
- ___121-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:updatedFlags:newSyncAnchor:partnerScopesNeedingToPullChanges:]_block_invoke.46
- ___121-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:updatedFlags:newSyncAnchor:partnerScopesNeedingToPullChanges:]_block_invoke.48
- ___121-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:updatedFlags:newSyncAnchor:partnerScopesNeedingToPullChanges:]_block_invoke.49
- ___121-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:updatedFlags:newSyncAnchor:partnerScopesNeedingToPullChanges:]_block_invoke.50
- ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke.102
- ___37-[CPLEngineMultiscopeSyncTask launch]_block_invoke_2.103
- ___37-[CPLUploadPushedChangesTask cancel:]_block_invoke.164
- ___38-[CPLPushToTransportScopeTask _launch]_block_invoke.87
- ___38-[CPLPushToTransportScopeTask _launch]_block_invoke_2.89
- ___51-[CPLPushToTransportScopeTask _updateContributors:]_block_invoke.66
- ___53-[CPLPullFromTransportScopeTask _launchNextQueryTask]_block_invoke.92
- ___53-[CPLPullFromTransportScopeTask _launchNextQueryTask]_block_invoke.93
- ___53-[CPLPullFromTransportScopeTask _launchNextQueryTask]_block_invoke.94
- ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.111
- ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke.114
- ___55-[CPLEngineMultiscopeSyncTask task:didFinishWithError:]_block_invoke_2.112
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.147
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.149
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.150
- ___55-[CPLUploadPushedChangesTask _extractAndUploadOneBatch]_block_invoke.151
- ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke.112
- ___56-[CPLPullFromTransportScopeTask _fetchInitialSyncAnchor]_block_invoke_2.113
- ___56-[CPLPullFromTransportScopeTask taskDidFinishWithError:]_block_invoke.140
- ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke.101
- ___59-[CPLPushToTransportScopeTask _pushTaskDidFinishWithError:]_block_invoke_2.102
- ___60-[CPLUploadPushedChangesTask _uploadTaskDidFinishWithError:]_block_invoke.171
- ___61-[CPLPullFromTransportScopeTask _launchQueryForClass:cursor:]_block_invoke.84
- ___61-[CPLPullFromTransportScopeTask _launchQueryForClass:cursor:]_block_invoke_2.85
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.114
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.116
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke_2.117
- ___67-[CPLPullFromTransportScopeTask _launchFetchChangesFromSyncAnchor:]_block_invoke.67
- ___67-[CPLPullFromTransportScopeTask _launchFetchChangesFromSyncAnchor:]_block_invoke.73
- ___67-[CPLPullFromTransportScopeTask _launchFetchChangesFromSyncAnchor:]_block_invoke_2.68
- ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.105
- ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.106
- ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.107
- ___67-[CPLPullFromTransportScopeTask _launchPullTasksAndDisableQueries:]_block_invoke.108
- ___73-[CPLPullFromTransportScopeTask _checkExtraRecordsWithScopedIdentifiers:]_block_invoke.37
- ___73-[CPLPullFromTransportScopeTask _checkExtraRecordsWithScopedIdentifiers:]_block_invoke_2.38
- ___73-[CPLPullFromTransportScopeTask _checkExtraRecordsWithScopedIdentifiers:]_block_invoke_3.40
- ___80-[CPLPullFromTransportScopeTask _relaunchFetchChangesFromOtherRewindSyncAnchors]_block_invoke.62
- ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.122
- ___81-[CPLPullFromTransportScopeTask _checkServerFeatureVersionWithCompletionHandler:]_block_invoke.134
- ___82-[CPLPullFromTransportScopeTask _handleNewBatchFromQuery:newCursor:inTransaction:]_block_invoke.77
- ___88-[CPLPullFromTransportScopeTask _handleNewBatchFromChanges:newSyncAnchor:inTransaction:]_block_invoke.22
- ___90-[CPLPullFromTransportScopeTask _extractAndMingleAssetsIfPossibleFromBatch:inTransaction:]_block_invoke.20
- ___96-[CPLPullFromTransportScopeTask _updateLastFeatureVersionAndRelaunchFetchChangesFromSyncAnchor:]_block_invoke.55
- ___Block_byref_object_copy_.11171
- ___Block_byref_object_copy_.11464
- ___Block_byref_object_copy_.12222
- ___Block_byref_object_copy_.13039
- ___Block_byref_object_copy_.1346
- ___Block_byref_object_copy_.13620
- ___Block_byref_object_copy_.13946
- ___Block_byref_object_copy_.14133
- ___Block_byref_object_copy_.14950
- ___Block_byref_object_copy_.15551
- ___Block_byref_object_copy_.16272
- ___Block_byref_object_copy_.16594
- ___Block_byref_object_copy_.17066
- ___Block_byref_object_copy_.1747
- ___Block_byref_object_copy_.17667
- ___Block_byref_object_copy_.18490
- ___Block_byref_object_copy_.19961
- ___Block_byref_object_copy_.20101
- ___Block_byref_object_copy_.2055
- ___Block_byref_object_copy_.20611
- ___Block_byref_object_copy_.21225
- ___Block_byref_object_copy_.21707
- ___Block_byref_object_copy_.22044
- ___Block_byref_object_copy_.23057
- ___Block_byref_object_copy_.23356
- ___Block_byref_object_copy_.24118
- ___Block_byref_object_copy_.2551
- ___Block_byref_object_copy_.2628
- ___Block_byref_object_copy_.2951
- ___Block_byref_object_copy_.3268
- ___Block_byref_object_copy_.5787
- ___Block_byref_object_copy_.6487
- ___Block_byref_object_copy_.6638
- ___Block_byref_object_copy_.7200
- ___Block_byref_object_copy_.7580
- ___Block_byref_object_copy_.7859
- ___Block_byref_object_copy_.8292
- ___Block_byref_object_copy_.9696
- ___Block_byref_object_copy_.9938
- ___Block_byref_object_dispose_.11172
- ___Block_byref_object_dispose_.11465
- ___Block_byref_object_dispose_.12223
- ___Block_byref_object_dispose_.13040
- ___Block_byref_object_dispose_.1347
- ___Block_byref_object_dispose_.13621
- ___Block_byref_object_dispose_.13947
- ___Block_byref_object_dispose_.14134
- ___Block_byref_object_dispose_.14951
- ___Block_byref_object_dispose_.15552
- ___Block_byref_object_dispose_.16273
- ___Block_byref_object_dispose_.16595
- ___Block_byref_object_dispose_.17067
- ___Block_byref_object_dispose_.1748
- ___Block_byref_object_dispose_.17668
- ___Block_byref_object_dispose_.18491
- ___Block_byref_object_dispose_.19962
- ___Block_byref_object_dispose_.20102
- ___Block_byref_object_dispose_.2056
- ___Block_byref_object_dispose_.20612
- ___Block_byref_object_dispose_.21226
- ___Block_byref_object_dispose_.21708
- ___Block_byref_object_dispose_.22045
- ___Block_byref_object_dispose_.23058
- ___Block_byref_object_dispose_.23357
- ___Block_byref_object_dispose_.24119
- ___Block_byref_object_dispose_.2552
- ___Block_byref_object_dispose_.2629
- ___Block_byref_object_dispose_.2952
- ___Block_byref_object_dispose_.3269
- ___Block_byref_object_dispose_.5788
- ___Block_byref_object_dispose_.6488
- ___Block_byref_object_dispose_.6639
- ___Block_byref_object_dispose_.7201
- ___Block_byref_object_dispose_.7581
- ___Block_byref_object_dispose_.7860
- ___Block_byref_object_dispose_.8293
- ___Block_byref_object_dispose_.9697
- ___Block_byref_object_dispose_.9939
- ___CPLConfigurationOSLogDomain.19321
- ___CPLConfigurationOSLogDomain.onceToken.19327
- ___CPLConfigurationOSLogDomain.result.19329
- ___CPLForceSyncOSLogDomain.20754
- ___CPLForceSyncOSLogDomain.onceToken.20763
- ___CPLForceSyncOSLogDomain.result.20764
- ___CPLSchedulerOSLogDomain.7528
- ___CPLSchedulerOSLogDomain.onceToken.7529
- ___CPLSchedulerOSLogDomain.result.7530
- ___CPLSessionOSLogDomain.16143
- ___CPLSessionOSLogDomain.18050
- ___CPLSessionOSLogDomain.22647
- ___CPLSessionOSLogDomain.onceToken.16145
- ___CPLSessionOSLogDomain.onceToken.18055
- ___CPLSessionOSLogDomain.onceToken.22649
- ___CPLSessionOSLogDomain.result.16146
- ___CPLSessionOSLogDomain.result.18056
- ___CPLSessionOSLogDomain.result.22651
- ___CPLStorageOSLogDomain.11139
- ___CPLStorageOSLogDomain.11224
- ___CPLStorageOSLogDomain.17635
- ___CPLStorageOSLogDomain.20081
- ___CPLStorageOSLogDomain.2037
- ___CPLStorageOSLogDomain.21372
- ___CPLStorageOSLogDomain.22031
- ___CPLStorageOSLogDomain.22279
- ___CPLStorageOSLogDomain.6239
- ___CPLStorageOSLogDomain.7809
- ___CPLStorageOSLogDomain.8543
- ___CPLStorageOSLogDomain.8984
- ___CPLStorageOSLogDomain.9150
- ___CPLStorageOSLogDomain.9343
- ___CPLStorageOSLogDomain.onceToken.11150
- ___CPLStorageOSLogDomain.onceToken.11227
- ___CPLStorageOSLogDomain.onceToken.14470
- ___CPLStorageOSLogDomain.onceToken.17637
- ___CPLStorageOSLogDomain.onceToken.20083
- ___CPLStorageOSLogDomain.onceToken.20361
- ___CPLStorageOSLogDomain.onceToken.2039
- ___CPLStorageOSLogDomain.onceToken.21376
- ___CPLStorageOSLogDomain.onceToken.22036
- ___CPLStorageOSLogDomain.onceToken.22287
- ___CPLStorageOSLogDomain.onceToken.6241
- ___CPLStorageOSLogDomain.onceToken.7811
- ___CPLStorageOSLogDomain.onceToken.8551
- ___CPLStorageOSLogDomain.onceToken.8990
- ___CPLStorageOSLogDomain.onceToken.9152
- ___CPLStorageOSLogDomain.onceToken.9345
- ___CPLStorageOSLogDomain.result.11152
- ___CPLStorageOSLogDomain.result.11229
- ___CPLStorageOSLogDomain.result.14472
- ___CPLStorageOSLogDomain.result.17639
- ___CPLStorageOSLogDomain.result.20085
- ___CPLStorageOSLogDomain.result.20362
- ___CPLStorageOSLogDomain.result.2041
- ___CPLStorageOSLogDomain.result.21378
- ___CPLStorageOSLogDomain.result.22038
- ___CPLStorageOSLogDomain.result.22289
- ___CPLStorageOSLogDomain.result.6243
- ___CPLStorageOSLogDomain.result.7812
- ___CPLStorageOSLogDomain.result.8552
- ___CPLStorageOSLogDomain.result.8992
- ___CPLStorageOSLogDomain.result.9153
- ___CPLStorageOSLogDomain.result.9346
- ___CPLStoreOSLogDomain.3056
- ___CPLStoreOSLogDomain.onceToken.3057
- ___CPLStoreOSLogDomain.result.3058
- ___CPLTaskOSLogDomain.11412
- ___CPLTaskOSLogDomain.1344
- ___CPLTaskOSLogDomain.13920
- ___CPLTaskOSLogDomain.14382
- ___CPLTaskOSLogDomain.15448
- ___CPLTaskOSLogDomain.16977
- ___CPLTaskOSLogDomain.21172
- ___CPLTaskOSLogDomain.22983
- ___CPLTaskOSLogDomain.24075
- ___CPLTaskOSLogDomain.2614
- ___CPLTaskOSLogDomain.5473
- ___CPLTaskOSLogDomain.7123
- ___CPLTaskOSLogDomain.onceToken.11448
- ___CPLTaskOSLogDomain.onceToken.1372
- ___CPLTaskOSLogDomain.onceToken.13922
- ___CPLTaskOSLogDomain.onceToken.14384
- ___CPLTaskOSLogDomain.onceToken.15457
- ___CPLTaskOSLogDomain.onceToken.16984
- ___CPLTaskOSLogDomain.onceToken.21214
- ___CPLTaskOSLogDomain.onceToken.22994
- ___CPLTaskOSLogDomain.onceToken.24083
- ___CPLTaskOSLogDomain.onceToken.2616
- ___CPLTaskOSLogDomain.onceToken.5476
- ___CPLTaskOSLogDomain.onceToken.7135
- ___CPLTaskOSLogDomain.result.11450
- ___CPLTaskOSLogDomain.result.1373
- ___CPLTaskOSLogDomain.result.13924
- ___CPLTaskOSLogDomain.result.14385
- ___CPLTaskOSLogDomain.result.15459
- ___CPLTaskOSLogDomain.result.16985
- ___CPLTaskOSLogDomain.result.21215
- ___CPLTaskOSLogDomain.result.22996
- ___CPLTaskOSLogDomain.result.24084
- ___CPLTaskOSLogDomain.result.2618
- ___CPLTaskOSLogDomain.result.5478
- ___CPLTaskOSLogDomain.result.7137
- _____CPLConfigurationOSLogDomain_block_invoke.19332
- _____CPLForceSyncOSLogDomain_block_invoke.20766
- _____CPLSchedulerOSLogDomain_block_invoke.7532
- _____CPLSessionOSLogDomain_block_invoke.16148
- _____CPLSessionOSLogDomain_block_invoke.18058
- _____CPLSessionOSLogDomain_block_invoke.22654
- _____CPLStorageOSLogDomain_block_invoke.11155
- _____CPLStorageOSLogDomain_block_invoke.11232
- _____CPLStorageOSLogDomain_block_invoke.14477
- _____CPLStorageOSLogDomain_block_invoke.17642
- _____CPLStorageOSLogDomain_block_invoke.20088
- _____CPLStorageOSLogDomain_block_invoke.20368
- _____CPLStorageOSLogDomain_block_invoke.2044
- _____CPLStorageOSLogDomain_block_invoke.21381
- _____CPLStorageOSLogDomain_block_invoke.22041
- _____CPLStorageOSLogDomain_block_invoke.22292
- _____CPLStorageOSLogDomain_block_invoke.6246
- _____CPLStorageOSLogDomain_block_invoke.7814
- _____CPLStorageOSLogDomain_block_invoke.8554
- _____CPLStorageOSLogDomain_block_invoke.8995
- _____CPLStorageOSLogDomain_block_invoke.9155
- _____CPLStorageOSLogDomain_block_invoke.9348
- _____CPLStoreOSLogDomain_block_invoke.3060
- _____CPLTaskOSLogDomain_block_invoke.11453
- _____CPLTaskOSLogDomain_block_invoke.1375
- _____CPLTaskOSLogDomain_block_invoke.13927
- _____CPLTaskOSLogDomain_block_invoke.14387
- _____CPLTaskOSLogDomain_block_invoke.15462
- _____CPLTaskOSLogDomain_block_invoke.16987
- _____CPLTaskOSLogDomain_block_invoke.21217
- _____CPLTaskOSLogDomain_block_invoke.22999
- _____CPLTaskOSLogDomain_block_invoke.24086
- _____CPLTaskOSLogDomain_block_invoke.2621
- _____CPLTaskOSLogDomain_block_invoke.5481
- _____CPLTaskOSLogDomain_block_invoke.7140
- ___block_literal_global.10042
- ___block_literal_global.10361
- ___block_literal_global.105.18845
- ___block_literal_global.10758
- ___block_literal_global.10997
- ___block_literal_global.110.20911
- ___block_literal_global.11151
- ___block_literal_global.11228
- ___block_literal_global.11449
- ___block_literal_global.12.7933
- ___block_literal_global.12342
- ___block_literal_global.12564
- ___block_literal_global.13060
- ___block_literal_global.13923
- ___block_literal_global.14.14418
- ___block_literal_global.1413
- ___block_literal_global.14181
- ___block_literal_global.142.20915
- ___block_literal_global.14417
- ___block_literal_global.14471
- ___block_literal_global.14634
- ___block_literal_global.1493
- ___block_literal_global.15167
- ___block_literal_global.15187
- ___block_literal_global.15252
- ___block_literal_global.15458
- ___block_literal_global.1574
- ___block_literal_global.159.20916
- ___block_literal_global.15998
- ___block_literal_global.16213
- ___block_literal_global.16773
- ___block_literal_global.17089
- ___block_literal_global.171.20917
- ___block_literal_global.17432
- ___block_literal_global.1744.5763
- ___block_literal_global.17638
- ___block_literal_global.18068
- ___block_literal_global.18240
- ___block_literal_global.18378
- ___block_literal_global.1876
- ___block_literal_global.18958
- ___block_literal_global.1911
- ___block_literal_global.19328
- ___block_literal_global.19713
- ___block_literal_global.20084
- ___block_literal_global.20248
- ___block_literal_global.20364
- ___block_literal_global.2040
- ___block_literal_global.20907
- ___block_literal_global.21232
- ___block_literal_global.21377
- ___block_literal_global.21551
- ___block_literal_global.22037
- ___block_literal_global.22288
- ___block_literal_global.22448
- ___block_literal_global.22650
- ___block_literal_global.22800
- ___block_literal_global.23053
- ___block_literal_global.2317
- ___block_literal_global.23609
- ___block_literal_global.23745
- ___block_literal_global.23817
- ___block_literal_global.24.14135
- ___block_literal_global.24249
- ___block_literal_global.24363
- ___block_literal_global.24482
- ___block_literal_global.24667
- ___block_literal_global.2492
- ___block_literal_global.2550
- ___block_literal_global.2617
- ___block_literal_global.264.22995
- ___block_literal_global.27.16232
- ___block_literal_global.2968
- ___block_literal_global.3035
- ___block_literal_global.32.22416
- ___block_literal_global.3285
- ___block_literal_global.33.7251
- ___block_literal_global.34.2489
- ___block_literal_global.34.9935
- ___block_literal_global.3557
- ___block_literal_global.37.10678
- ___block_literal_global.3795
- ___block_literal_global.4033
- ___block_literal_global.42.7940
- ___block_literal_global.430
- ___block_literal_global.4465
- ___block_literal_global.4600
- ___block_literal_global.4814
- ___block_literal_global.5.24376
- ___block_literal_global.50.7242
- ___block_literal_global.5262
- ___block_literal_global.5339
- ___block_literal_global.54.5235
- ___block_literal_global.5477
- ___block_literal_global.5617
- ___block_literal_global.57.7944
- ___block_literal_global.6154
- ___block_literal_global.6242
- ___block_literal_global.6463
- ___block_literal_global.6743
- ___block_literal_global.7136
- ___block_literal_global.72.16731
- ___block_literal_global.7250
- ___block_literal_global.7650
- ___block_literal_global.77.15993
- ___block_literal_global.7930
- ___block_literal_global.8674
- ___block_literal_global.8885
- ___block_literal_global.8991
- ___block_literal_global.9089
- ___block_literal_global.93.18849
- ___block_literal_global.93.7713
- ___block_literal_global.9394
- ___block_literal_global.9567
- ___block_literal_global.9834
- ___cpl_dispatch_async_block_invoke.10019
- ___cpl_dispatch_async_block_invoke.11408
- ___cpl_dispatch_async_block_invoke.12042
- ___cpl_dispatch_async_block_invoke.1378
- ___cpl_dispatch_async_block_invoke.13932
- ___cpl_dispatch_async_block_invoke.14306
- ___cpl_dispatch_async_block_invoke.14379
- ___cpl_dispatch_async_block_invoke.15541
- ___cpl_dispatch_async_block_invoke.16551
- ___cpl_dispatch_async_block_invoke.17043
- ___cpl_dispatch_async_block_invoke.17388
- ___cpl_dispatch_async_block_invoke.17875
- ___cpl_dispatch_async_block_invoke.1825
- ___cpl_dispatch_async_block_invoke.18374
- ___cpl_dispatch_async_block_invoke.19307
- ___cpl_dispatch_async_block_invoke.20594
- ___cpl_dispatch_async_block_invoke.21170
- ___cpl_dispatch_async_block_invoke.21559
- ___cpl_dispatch_async_block_invoke.22802
- ___cpl_dispatch_async_block_invoke.23002
- ___cpl_dispatch_async_block_invoke.24127
- ___cpl_dispatch_async_block_invoke.2955
- ___cpl_dispatch_async_block_invoke.6686
- ___cpl_dispatch_async_block_invoke.7121
- ___cpl_dispatch_async_block_invoke.7391
- ___cpl_dispatch_async_block_invoke.7820
- ___cpl_dispatch_async_block_invoke.9680
- __doProtected:.onceToken.15186
- __doProtected:.onceToken.22799
- __doProtected:.queue.22801
- __statusDidChange.12239
- _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.18868
- _initWithCoder:.logOnceToken.20250
- _initWithCoder:.onceToken.10702
- _initWithCoder:.onceToken.14180
- _initWithCoder:.onceToken.18067
- _initWithCoder:.onceToken.20247
- _initWithCoder:.onceToken.22447
- _initWithCoder:.onceToken.24666
- _initWithCoder:.onceToken.5234
- _initWithCoder:.onceToken.5338
- _initWithCoder:.onceToken.6458
- _initWithCoder:.pushContextsClasses.22449
- _initWithCoder:.stringClass.10703
- _propertiesForChangeType:.onceToken.15022
- _propertiesForChangeType:.onceToken.18882
- _propertiesForChangeType:.onceToken.23744
- _propertiesForChangeType:.properties.23746
CStrings:
+ "@\"<CPLSyncThroughputReporterDelegate>\""
+ "@\"CPLSyncSessionThroughputMetrics\""
+ "@\"CPLSyncThroughputReporter\""
+ "@\"CPLSyncThroughputReporter\"24@0:8@\"NSString\"16"
+ "CPLSyncSessionThroughputMetrics"
+ "CPLSyncSessionThroughputReporting"
+ "CPLSyncThroughputReporter"
+ "CPLSyncThroughputReporterDelegate"
+ "CloudPhotoLibrary-800.20.101"
+ "Removing just-in-case from %@ as it has been associated with a rescheduler"
+ "T@\"<CPLSyncThroughputReporterDelegate>\",W,N,V_delegate"
+ "T@\"CPLSyncSessionThroughputMetrics\",&,N,V_metrics"
+ "T@\"NSDate\",&,N,V_startTime"
+ "T@\"NSObject<OS_dispatch_queue>\",W,N,V_delegateQueue"
+ "T@\"NSString\",R,N,V_metricsIdentifier"
+ "TQ,N,V_totalCount"
+ "_delegateQueue"
+ "_kindOfWorkReporters"
+ "_metricsIdentifier"
+ "_parentMetricsIdentifier"
+ "_throughputReporter"
+ "_throughputReporterLock"
+ "_totalCount"
+ "addCompletedWorkItemCount:"
+ "addCompletedWorkItemCount:kindOfWork:"
+ "addCountOfPulledAssets:"
+ "changes"
+ "delegateQueue"
+ "endTrackingWork"
+ "initWithCategory:parentMetrics:"
+ "initWithCategory:parentReport:"
+ "kb"
+ "makeChildReportForCategory:"
+ "makeSiblingReportForCategory:"
+ "makeThroughputReporterForCategory:"
+ "metrics"
+ "metricsIdentifier"
+ "pull.assets"
+ "reportThroughputWorkForMetrics:itemCount:done:"
+ "setDelegateQueue:"
+ "setMetrics:"
+ "setStartTime:"
+ "setThroughputReporter:"
+ "setTotalCount:"
+ "startTrackingWork"
+ "system-library"
+ "throughputReporter:addedItemCount:"
+ "throughputReporterDidFinish:"
+ "totalCount"
+ "v16@?0@\"CPLSyncThroughputReporter\"8"
+ "v24@0:8@\"CPLSyncThroughputReporter\"16"
+ "v32@0:8@\"CPLSyncThroughputReporter\"16Q24"
+ "v36@0:8@\"CPLSyncSessionThroughputMetrics\"16Q24B32"
+ "withThroughputReporter:"
- "CloudPhotoLibrary-800.14.111"
- "Removing just-in-case from %@ as it was associated with a rescheduler"

```
