## LinkServices

> `/System/Library/PrivateFrameworks/LinkServices.framework/Versions/A/LinkServices`

```diff

-210.0.6.0.0
-  __TEXT.__text: 0xd48c4
-  __TEXT.__auth_stubs: 0x1d40
-  __TEXT.__objc_methlist: 0x6f28
+208.0.0.0.0
+  __TEXT.__text: 0xd57bc
+  __TEXT.__auth_stubs: 0x1d50
+  __TEXT.__objc_methlist: 0x6e80
   __TEXT.__const: 0x1a08
-  __TEXT.__cstring: 0x8574
+  __TEXT.__cstring: 0x86d7
   __TEXT.__swift5_typeref: 0x115c
   __TEXT.__swift5_capture: 0x4f4
   __TEXT.__constg_swiftt: 0xc2c

   __TEXT.__swift5_proto: 0x18c
   __TEXT.__swift5_types: 0xec
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__oslogstring: 0x490f
+  __TEXT.__oslogstring: 0x4b1b
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__gcc_except_tab: 0x1814
-  __TEXT.__dlopen_cstrs: 0x48a
-  __TEXT.__unwind_info: 0x3938
+  __TEXT.__gcc_except_tab: 0x1918
+  __TEXT.__dlopen_cstrs: 0x5a3
+  __TEXT.__unwind_info: 0x3960
   __TEXT.__eh_frame: 0x2810
-  __TEXT.__objc_classname: 0x1808
-  __TEXT.__objc_methname: 0xf792
-  __TEXT.__objc_methtype: 0x2b6e
-  __TEXT.__objc_stubs: 0x8ac0
+  __TEXT.__objc_classname: 0x17e8
+  __TEXT.__objc_methname: 0xf578
+  __TEXT.__objc_methtype: 0x2aa8
+  __TEXT.__objc_stubs: 0x8a60
   __DATA_CONST.__got: 0xb48
-  __DATA_CONST.__const: 0xbb8
-  __DATA_CONST.__objc_classlist: 0x5d8
+  __DATA_CONST.__const: 0xc00
+  __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c30
+  __DATA_CONST.__objc_selrefs: 0x2c00
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x4e0
-  __AUTH_CONST.__auth_got: 0xeb0
+  __DATA_CONST.__objc_superrefs: 0x4d0
+  __AUTH_CONST.__auth_got: 0xeb8
   __AUTH_CONST.__auth_ptr: 0x4c8
-  __AUTH_CONST.__const: 0x4408
-  __AUTH_CONST.__cfstring: 0x6ac0
-  __AUTH_CONST.__objc_const: 0x11130
+  __AUTH_CONST.__const: 0x4338
+  __AUTH_CONST.__cfstring: 0x6aa0
+  __AUTH_CONST.__objc_const: 0x10fc0
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x3d68
+  __AUTH.__objc_data: 0x3d18
   __AUTH.__data: 0x9c8
-  __DATA.__objc_ivar: 0x81c
+  __DATA.__objc_ivar: 0x80c
   __DATA.__data: 0x1f98
-  __DATA.__bss: 0x1b21
+  __DATA.__bss: 0x1b61
   __DATA.__common: 0x630
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5431
-  Symbols:   8041
-  CStrings:  1149
+  Functions: 5424
+  Symbols:   8030
+  CStrings:  1162
 
Symbols:
+ +[LNConnectionPolicy shouldExecuteActionOnApplicationWithActionMetadata:reason:]
+ -[LNActionExecutor donateIfNecessaryWithResult:completionHandler:]
+ -[LNConnection(FetchListenerEndpoint) getListenerEndpointForBundleIdentifier:completionHandler:]
+ -[LNFetchListenerEndpointConnectionOperation finishWithXPCListenerEndpoint:auditTokenData:error:]
+ -[LNFetchListenerEndpointConnectionOperation initWithConnectionInterface:queue:bundleIdentifier:completionHandler:]
+ -[LNFetchListenerEndpointConnectionOperation setBundleIdentifier:]
+ -[LNTranscriptActionRecord initWithBundleIdentifier:source:clientLabel:executionUUID:executionDate:actionData:resolvedActionData:actionOutputData:predictionsData:]
+ AppKitLibraryCore.frameworkLibrary.11069
+ CascadeSetsLibraryCore.frameworkLibrary
+ CoreSpotlightLibraryCore.frameworkLibrary.10431
+ DialogEngineLibraryCore.frameworkLibrary.4364
+ DialogEngineLibraryCore.frameworkLibrary.4921
+ DialogEngineLibraryCore.frameworkLibrary.511
+ DialogEngineLibraryCore.frameworkLibrary.6103
+ GCC_except_table1041
+ GCC_except_table1059
+ GCC_except_table1069
+ GCC_except_table1136
+ GCC_except_table115
+ GCC_except_table1244
+ GCC_except_table129
+ GCC_except_table1295
+ GCC_except_table1308
+ GCC_except_table1318
+ GCC_except_table1319
+ GCC_except_table1320
+ GCC_except_table1333
+ GCC_except_table1360
+ GCC_except_table1366
+ GCC_except_table1368
+ GCC_except_table1381
+ GCC_except_table1386
+ GCC_except_table1395
+ GCC_except_table1399
+ GCC_except_table142
+ GCC_except_table1451
+ GCC_except_table1455
+ GCC_except_table1511
+ GCC_except_table1514
+ GCC_except_table1515
+ GCC_except_table1523
+ GCC_except_table1525
+ GCC_except_table1527
+ GCC_except_table1528
+ GCC_except_table1529
+ GCC_except_table1590
+ GCC_except_table1604
+ GCC_except_table1626
+ GCC_except_table1634
+ GCC_except_table1695
+ GCC_except_table1712
+ GCC_except_table1729
+ GCC_except_table1815
+ GCC_except_table1817
+ GCC_except_table1819
+ GCC_except_table254
+ GCC_except_table2554
+ GCC_except_table2559
+ GCC_except_table2577
+ GCC_except_table377
+ GCC_except_table384
+ GCC_except_table389
+ GCC_except_table398
+ GCC_except_table464
+ GCC_except_table473
+ GCC_except_table475
+ GCC_except_table477
+ GCC_except_table485
+ GCC_except_table493
+ GCC_except_table513
+ GCC_except_table576
+ GCC_except_table584
+ GCC_except_table641
+ GCC_except_table653
+ GCC_except_table656
+ GCC_except_table694
+ GCC_except_table756
+ GCC_except_table783
+ GCC_except_table795
+ GCC_except_table824
+ GCC_except_table884
+ GCC_except_table917
+ GCC_except_table930
+ GCC_except_table978
+ GCC_except_table981
+ IntelligencePlatformLibraryLibrary.7348
+ IntelligencePlatformLibraryLibraryCore.frameworkLibrary.7350
+ _CascadeSetsLibrary
+ __27-[LNActionExecutor perform]_block_invoke.102
+ __27-[LNActionExecutor perform]_block_invoke.103
+ __27-[LNActionExecutor perform]_block_invoke.107
+ __27-[LNActionExecutor perform]_block_invoke.84
+ __27-[LNActionExecutor perform]_block_invoke.93
+ __59-[LNActionExecutor requestContinueInApp:completionHandler:]_block_invoke.172
+ __69-[LNActionExecutor runShowOutputActionIfNecessary:completionHandler:]_block_invoke.130
+ __87+[LNExtensionMediator getConnectionHostInterfaceForBundleIdentifier:completionHandler:]_block_invoke.16
+ __87+[LNExtensionMediator getConnectionHostInterfaceForBundleIdentifier:completionHandler:]_block_invoke.19
+ __92+[LNSpotlightCascadeBridge donateItems:bundleIdentifier:version:validity:completionHandler:]_block_invoke.28
+ __AppKitLibraryCore_block_invoke.11070
+ __Block_byref_object_copy_.10395
+ __Block_byref_object_copy_.11053
+ __Block_byref_object_copy_.11573
+ __Block_byref_object_copy_.12392
+ __Block_byref_object_copy_.12933
+ __Block_byref_object_copy_.1968
+ __Block_byref_object_copy_.4502
+ __Block_byref_object_copy_.5752
+ __Block_byref_object_copy_.6628
+ __Block_byref_object_copy_.8980
+ __Block_byref_object_dispose_.10396
+ __Block_byref_object_dispose_.11054
+ __Block_byref_object_dispose_.11574
+ __Block_byref_object_dispose_.12393
+ __Block_byref_object_dispose_.12934
+ __Block_byref_object_dispose_.1969
+ __Block_byref_object_dispose_.4503
+ __Block_byref_object_dispose_.5753
+ __Block_byref_object_dispose_.6629
+ __Block_byref_object_dispose_.8981
+ __CoreSpotlightLibraryCore_block_invoke.10432
+ __DialogEngineLibraryCore_block_invoke.4365
+ __DialogEngineLibraryCore_block_invoke.4922
+ __DialogEngineLibraryCore_block_invoke.512
+ __DialogEngineLibraryCore_block_invoke.6104
+ __IntelligencePlatformLibraryLibraryCore_block_invoke.7351
+ ___115-[LNFetchListenerEndpointConnectionOperation initWithConnectionInterface:queue:bundleIdentifier:completionHandler:]_block_invoke
+ ___66-[LNActionExecutor donateIfNecessaryWithResult:completionHandler:]_block_invoke
+ ___92+[LNSpotlightCascadeBridge deleteItems:bundleIdentifier:version:validity:completionHandler:]_block_invoke
+ ___92+[LNSpotlightCascadeBridge donateItems:bundleIdentifier:version:validity:completionHandler:]_block_invoke
+ ___96-[LNConnection(FetchListenerEndpoint) getListenerEndpointForBundleIdentifier:completionHandler:]_block_invoke
+ ___CascadeSetsLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32s_e43_B24?0"CSSearchableItem"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32s_e49_v24?0"<LNConnectionHostInterface>"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e54_v32?0"NSXPCListenerEndpoint"8"NSData"16"NSError"24l
+ ___block_descriptor_56_e8_32s40s48bs_e35_v24?0"CCSetDonation"8"NSError"16l
+ ___block_descriptor_64_e8_32s40s48s56bs_e54_v32?0"NSXPCListenerEndpoint"8"NSData"16"NSError"24l
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e35_v24?0"CCSetDonation"8"NSError"16l
+ ___getCCFullSetDonationClass_block_invoke
+ ___getCCIncrementalSetDonationClass_block_invoke
+ ___getCCSetClass_block_invoke
+ ___getCCSetDescriptorClass_block_invoke
+ ___getCCSetDescriptorKeySourceIdentifierSymbolLoc_block_invoke
+ ___getCCSetDonationClass_block_invoke
+ ___getCSSearchableItemClass_block_invoke
+ __block_literal_global.10398
+ __block_literal_global.10548
+ __block_literal_global.10619
+ __block_literal_global.10675
+ __block_literal_global.11046
+ __block_literal_global.11096
+ __block_literal_global.1153
+ __block_literal_global.11578
+ __block_literal_global.11933
+ __block_literal_global.1199
+ __block_literal_global.12363
+ __block_literal_global.12617
+ __block_literal_global.1290
+ __block_literal_global.13035
+ __block_literal_global.1511
+ __block_literal_global.18
+ __block_literal_global.23.11049
+ __block_literal_global.2391
+ __block_literal_global.2791
+ __block_literal_global.2849
+ __block_literal_global.29.11928
+ __block_literal_global.3233
+ __block_literal_global.3339
+ __block_literal_global.3450
+ __block_literal_global.3616
+ __block_literal_global.3678
+ __block_literal_global.3850
+ __block_literal_global.4197
+ __block_literal_global.4242
+ __block_literal_global.4357
+ __block_literal_global.5010
+ __block_literal_global.5042
+ __block_literal_global.5393
+ __block_literal_global.6168
+ __block_literal_global.6304
+ __block_literal_global.6979
+ __block_literal_global.7439
+ __block_literal_global.7664
+ __block_literal_global.7730
+ __block_literal_global.7899
+ __block_literal_global.7986
+ __block_literal_global.8332
+ __block_literal_global.8477
+ __block_literal_global.853
+ __block_literal_global.9413
+ __block_literal_global.9496
+ __getCATClass_block_invoke.4360
+ __getCATClass_block_invoke.4920
+ __getCATClass_block_invoke.510
+ __getCATClass_block_invoke.6102
+ _audit_stringCascadeSets
+ _dlerror
+ _getCCIncrementalSetDonationClass
+ _getCCSetDescriptorClass
+ _getCCSetDonationClass
+ _objc_msgSend$allSets:
+ _objc_msgSend$changePublisherWithUseCase:
+ _objc_msgSend$descriptorWithKey:
+ _objc_msgSend$donateIfNecessaryWithResult:completionHandler:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$finishWithXPCListenerEndpoint:auditTokenData:error:
+ _objc_msgSend$getListenerEndpointForBundleIdentifier:completionHandler:
+ _objc_msgSend$handleDeletionStream:items:bundleId:completionHandler:
+ _objc_msgSend$handleFullSetStream:items:bundleId:quota:indexName:serialNumber:completionHandler:
+ _objc_msgSend$handleIncrementalStream:items:bundleId:existingItemCount:quota:completionHandler:
+ _objc_msgSend$incrementalSetDonationWithItemType:forAccount:descriptors:version:validity:completion:
+ _objc_msgSend$initWithBundleIdentifier:source:clientLabel:executionUUID:executionDate:actionData:resolvedActionData:actionOutputData:predictionsData:
+ _objc_msgSend$initWithConnectionInterface:queue:bundleIdentifier:completionHandler:
+ _objc_msgSend$isAllowedItem:clientBundleID:
+ _objc_msgSend$isInternalInstall
+ _objc_msgSend$itemType
+ _objc_msgSend$localItemInstanceCount
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$setEnumeratorWithUseCase:
+ _objc_msgSend$shouldExecuteActionOnApplicationWithActionMetadata:reason:
+ _objc_msgSend$sourceIdentifierWithValue:error:
+ audit_stringAppKit.11083
+ audit_stringCoreSpotlight.10438
+ audit_stringDialogEngine.4376
+ audit_stringDialogEngine.4933
+ audit_stringDialogEngine.518
+ audit_stringDialogEngine.6115
+ audit_stringIntelligencePlatformLibrary.7354
+ getCATClass.softClass.4359
+ getCATClass.softClass.4919
+ getCATClass.softClass.509
+ getCATClass.softClass.6101
+ getCCFullSetDonationClass.softClass
+ getCCIncrementalSetDonationClass.softClass
+ getCCSetClass.softClass
+ getCCSetDescriptorClass.softClass
+ getCCSetDescriptorKeySourceIdentifierSymbolLoc.ptr
+ getCCSetDonationClass.softClass
+ getCSSearchableItemClass.softClass
- +[LNConnectionPolicy shouldExecuteActionOnApplicationWithActionMetadata:signals:reason:]
- +[LNExtensionMediator sharedQueue]
- -[LNActionExecutor donateActionIfNecessary:result:completionHandler:]
- -[LNActionExecutor getPrimaryConnectionInterfaceWithOptions:completionHandler:]
- -[LNActionExecutor getXPCListenerConnectionInterfaceWithOptions:completionHandler:]
- -[LNAppIntentConnectionPolicy metadata]
- -[LNConnection(FetchListenerEndpoint) getListenerEndpointForBundleIdentifier:action:completionHandler:]
- -[LNConnectionPolicySignals init]
- -[LNConnectionPolicySignals setShouldExecuteActionOnApplicationBasedOnMetadata:]
- -[LNConnectionPolicySignals shouldExecuteActionOnApplicationBasedOnMetadata]
- -[LNFetchListenerEndpointConnectionOperation action]
- -[LNFetchListenerEndpointConnectionOperation finishWithXPCListenerEndpoint:auditTokenData:resolvedAction:error:]
- -[LNFetchListenerEndpointConnectionOperation initWithConnectionInterface:queue:bundleIdentifier:action:completionHandler:]
- -[LNTranscriptActionRecord hasNextAction]
- -[LNTranscriptActionRecord initWithBundleIdentifier:source:clientLabel:executionUUID:executionDate:actionData:resolvedActionData:actionOutputData:predictionsData:hasNextAction:]
- -[LNXPCListenerEndpointConnection .cxx_destruct]
- -[LNXPCListenerEndpointConnection acquireAssertionsForConnectionOperation:]
- -[LNXPCListenerEndpointConnection connectWithOptions:]
- -[LNXPCListenerEndpointConnection initWithBundleIdentifier:bundleURL:bundleType:appBundleIdentifier:appIntentsEnabledOnly:userIdentity:listenerEndpoint:auditToken:error:]
- -[LNXPCListenerEndpointConnection listenerEndpoint]
- -[LNXPCListenerEndpointConnection refreshWithOptions:]
- AppKitLibraryCore.frameworkLibrary.10999
- DialogEngineLibraryCore.frameworkLibrary.4378
- DialogEngineLibraryCore.frameworkLibrary.4937
- DialogEngineLibraryCore.frameworkLibrary.504
- DialogEngineLibraryCore.frameworkLibrary.6123
- GCC_except_table1048
- GCC_except_table1066
- GCC_except_table1076
- GCC_except_table1143
- GCC_except_table116
- GCC_except_table1251
- GCC_except_table130
- GCC_except_table1302
- GCC_except_table1315
- GCC_except_table1325
- GCC_except_table1326
- GCC_except_table1327
- GCC_except_table1340
- GCC_except_table1367
- GCC_except_table1373
- GCC_except_table1375
- GCC_except_table1388
- GCC_except_table1393
- GCC_except_table1402
- GCC_except_table1406
- GCC_except_table143
- GCC_except_table1458
- GCC_except_table1462
- GCC_except_table1518
- GCC_except_table1521
- GCC_except_table1522
- GCC_except_table1579
- GCC_except_table1593
- GCC_except_table1615
- GCC_except_table1625
- GCC_except_table1689
- GCC_except_table1706
- GCC_except_table1723
- GCC_except_table1803
- GCC_except_table1811
- GCC_except_table1813
- GCC_except_table255
- GCC_except_table2561
- GCC_except_table2566
- GCC_except_table2584
- GCC_except_table383
- GCC_except_table390
- GCC_except_table452
- GCC_except_table455
- GCC_except_table470
- GCC_except_table479
- GCC_except_table487
- GCC_except_table507
- GCC_except_table515
- GCC_except_table517
- GCC_except_table519
- GCC_except_table582
- GCC_except_table590
- GCC_except_table650
- GCC_except_table662
- GCC_except_table665
- GCC_except_table703
- GCC_except_table765
- GCC_except_table792
- GCC_except_table804
- GCC_except_table833
- GCC_except_table893
- GCC_except_table925
- GCC_except_table938
- GCC_except_table985
- GCC_except_table988
- OBJC_IVAR_$_LNConnectionPolicySignals._shouldExecuteActionOnApplicationBasedOnMetadata
- OBJC_IVAR_$_LNFetchListenerEndpointConnectionOperation._action
- OBJC_IVAR_$_LNTranscriptActionRecord._hasNextAction
- OBJC_IVAR_$_LNXPCListenerEndpointConnection._listenerEndpoint
- _OBJC_CLASS_$_LNParameter
- _OBJC_CLASS_$_LNParameterConfiguration
- _OBJC_CLASS_$_LNXPCListenerEndpointConnection
- _OBJC_METACLASS_$_LNXPCListenerEndpointConnection
- __27-[LNActionExecutor perform]_block_invoke.104
- __27-[LNActionExecutor perform]_block_invoke.113
- __27-[LNActionExecutor perform]_block_invoke.114
- __27-[LNActionExecutor perform]_block_invoke.118
- __27-[LNActionExecutor perform]_block_invoke.95
- __59-[LNActionExecutor requestContinueInApp:completionHandler:]_block_invoke.184
- __69-[LNActionExecutor runShowOutputActionIfNecessary:completionHandler:]_block_invoke.142
- __83-[LNActionExecutor getXPCListenerConnectionInterfaceWithOptions:completionHandler:]_block_invoke.84
- __87+[LNExtensionMediator getConnectionHostInterfaceForBundleIdentifier:completionHandler:]_block_invoke.15
- __87+[LNExtensionMediator getConnectionHostInterfaceForBundleIdentifier:completionHandler:]_block_invoke.17
- __87+[LNExtensionMediator getConnectionHostInterfaceForBundleIdentifier:completionHandler:]_block_invoke.20
- __87+[LNExtensionMediator getConnectionHostInterfaceForBundleIdentifier:completionHandler:]_block_invoke.22
- __AppKitLibraryCore_block_invoke.11000
- __Block_byref_object_copy_.10332
- __Block_byref_object_copy_.10982
- __Block_byref_object_copy_.11502
- __Block_byref_object_copy_.12329
- __Block_byref_object_copy_.12911
- __Block_byref_object_copy_.1969
- __Block_byref_object_copy_.4517
- __Block_byref_object_copy_.5773
- __Block_byref_object_copy_.6647
- __Block_byref_object_copy_.8910
- __Block_byref_object_dispose_.10333
- __Block_byref_object_dispose_.10983
- __Block_byref_object_dispose_.11503
- __Block_byref_object_dispose_.12330
- __Block_byref_object_dispose_.12912
- __Block_byref_object_dispose_.1970
- __Block_byref_object_dispose_.4518
- __Block_byref_object_dispose_.5774
- __Block_byref_object_dispose_.6648
- __Block_byref_object_dispose_.8911
- __DialogEngineLibraryCore_block_invoke.4379
- __DialogEngineLibraryCore_block_invoke.4938
- __DialogEngineLibraryCore_block_invoke.505
- __DialogEngineLibraryCore_block_invoke.6124
- __OBJC_$_INSTANCE_METHODS_LNXPCListenerEndpointConnection
- __OBJC_$_INSTANCE_VARIABLES_LNXPCListenerEndpointConnection
- __OBJC_$_PROP_LIST_LNXPCListenerEndpointConnection
- __OBJC_CLASS_RO_$_LNXPCListenerEndpointConnection
- __OBJC_METACLASS_RO_$_LNXPCListenerEndpointConnection
- ___103-[LNConnection(FetchListenerEndpoint) getListenerEndpointForBundleIdentifier:action:completionHandler:]_block_invoke
- ___122-[LNFetchListenerEndpointConnectionOperation initWithConnectionInterface:queue:bundleIdentifier:action:completionHandler:]_block_invoke
- ___34+[LNExtensionMediator sharedQueue]_block_invoke
- ___52-[LNAppIntentConnectionPolicy actionWithParameters:]_block_invoke
- ___52-[LNAppIntentConnectionPolicy actionWithParameters:]_block_invoke_2
- ___54-[LNXPCListenerEndpointConnection connectWithOptions:]_block_invoke
- ___69-[LNActionExecutor donateActionIfNecessary:result:completionHandler:]_block_invoke
- ___79-[LNActionExecutor getPrimaryConnectionInterfaceWithOptions:completionHandler:]_block_invoke
- ___83-[LNActionExecutor getXPCListenerConnectionInterfaceWithOptions:completionHandler:]_block_invoke
- ___83-[LNActionExecutor getXPCListenerConnectionInterfaceWithOptions:completionHandler:]_block_invoke_2
- ___87+[LNExtensionMediator getConnectionHostInterfaceForBundleIdentifier:completionHandler:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e35_B16?0"LNActionParameterMetadata"8l
- ___block_descriptor_40_e8_32s_e36_"LNParameter"24?0"LNProperty"8Q16l
- ___block_descriptor_40_e8_32s_e67_v40?0"NSXPCListenerEndpoint"8"NSData"16"LNAction"24"NSError"32l
- ___block_descriptor_40_e8_32s_e79_v40?0"LNConnection"8"LNAction"16"<LNConnectionHostInterface>"24"NSError"32l
- ___block_descriptor_48_e8_32s40bs_e67_v40?0"NSXPCListenerEndpoint"8"NSData"16"LNAction"24"NSError"32l
- ___block_descriptor_48_e8_32s40s_e37_v24?0"LNSuccessResult"8"NSError"16l
- ___block_descriptor_56_e8_32s40bs_e5_v8?0l
- ___block_descriptor_64_e8_32s40s48s56bs_e67_v40?0"NSXPCListenerEndpoint"8"NSData"16"LNAction"24"NSError"32l
- ___block_descriptor_72_e8_32s40s48s56bs_e54_v32?0"NSXPCListenerEndpoint"8"NSData"16"NSError"24l
- __block_literal_global.10335
- __block_literal_global.10479
- __block_literal_global.10550
- __block_literal_global.10606
- __block_literal_global.10975
- __block_literal_global.11026
- __block_literal_global.1146
- __block_literal_global.11507
- __block_literal_global.11863
- __block_literal_global.1192
- __block_literal_global.12300
- __block_literal_global.12554
- __block_literal_global.1282
- __block_literal_global.12862
- __block_literal_global.13013
- __block_literal_global.1503
- __block_literal_global.19.7924
- __block_literal_global.23.10978
- __block_literal_global.2392
- __block_literal_global.2798
- __block_literal_global.2856
- __block_literal_global.30
- __block_literal_global.30.11857
- __block_literal_global.3241
- __block_literal_global.3347
- __block_literal_global.3458
- __block_literal_global.3624
- __block_literal_global.3686
- __block_literal_global.3861
- __block_literal_global.4210
- __block_literal_global.4255
- __block_literal_global.4371
- __block_literal_global.5026
- __block_literal_global.5058
- __block_literal_global.5409
- __block_literal_global.6188
- __block_literal_global.6324
- __block_literal_global.6998
- __block_literal_global.7375
- __block_literal_global.7600
- __block_literal_global.7666
- __block_literal_global.7835
- __block_literal_global.7923
- __block_literal_global.8268
- __block_literal_global.8413
- __block_literal_global.846
- __block_literal_global.9349
- __block_literal_global.9431
- __getCATClass_block_invoke.4374
- __getCATClass_block_invoke.4936
- __getCATClass_block_invoke.503
- __getCATClass_block_invoke.6122
- _objc_msgSend$actionWithByMergingParameters:
- _objc_msgSend$actionWithNonSecureParameters
- _objc_msgSend$actionWithOpenWhenRun:
- _objc_msgSend$capabilities
- _objc_msgSend$donateActionIfNecessary:result:completionHandler:
- _objc_msgSend$finishWithXPCListenerEndpoint:auditTokenData:resolvedAction:error:
- _objc_msgSend$getListenerEndpointForBundleIdentifier:action:completionHandler:
- _objc_msgSend$getPrimaryConnectionInterfaceWithOptions:completionHandler:
- _objc_msgSend$getXPCListenerConnectionInterfaceWithOptions:completionHandler:
- _objc_msgSend$hasNextAction
- _objc_msgSend$initWithBundleIdentifier:bundleURL:bundleType:appBundleIdentifier:appIntentsEnabledOnly:userIdentity:listenerEndpoint:auditToken:error:
- _objc_msgSend$initWithBundleIdentifier:source:clientLabel:executionUUID:executionDate:actionData:resolvedActionData:actionOutputData:predictionsData:hasNextAction:
- _objc_msgSend$initWithConnectionInterface:queue:bundleIdentifier:action:completionHandler:
- _objc_msgSend$initWithIdentifier:value:configuration:
- _objc_msgSend$metadata
- _objc_msgSend$openEntitySystemProtocol
- _objc_msgSend$setSecure:
- _objc_msgSend$setShouldExecuteActionOnApplicationBasedOnMetadata:
- _objc_msgSend$sharedQueue
- _objc_msgSend$shouldExecuteActionOnApplicationBasedOnMetadata
- _objc_msgSend$shouldExecuteActionOnApplicationWithActionMetadata:signals:reason:
- _objc_msgSend$urlRepresentableProtocol
- _objc_msgSend$validateEntitlement:auditToken:validator:
- _objc_msgSend$valueForKeyPath:
- _objc_msgSend$xpcListenerProtocol
- audit_stringAppKit.11013
- audit_stringDialogEngine.4390
- audit_stringDialogEngine.4949
- audit_stringDialogEngine.511
- audit_stringDialogEngine.6135
- getCATClass.softClass.4373
- getCATClass.softClass.4935
- getCATClass.softClass.502
- getCATClass.softClass.6121
- sharedQueue.onceToken
- sharedQueue.queue
CStrings:
+ "/System/Library/PrivateFrameworks/CascadeSets.framework/Contents/MacOS/CascadeSets"
+ "AppEntityDonation"
+ "B24@?0@\"CSSearchableItem\"8@\"NSDictionary\"16"
+ "CCFullSetDonation"
+ "CCIncrementalSetDonation"
+ "CCSet"
+ "CCSetDescriptor"
+ "CCSetDescriptorKeySourceIdentifier"
+ "CCSetDonation"
+ "CSSearchableItem"
+ "Class getCCFullSetDonationClass(void)_block_invoke"
+ "Class getCCIncrementalSetDonationClass(void)_block_invoke"
+ "Class getCCSetClass(void)_block_invoke"
+ "Class getCCSetDescriptorClass(void)_block_invoke"
+ "Class getCCSetDonationClass(void)_block_invoke"
+ "Class getCSSearchableItemClass(void)_block_invoke"
+ "LNSpotlightCascadeBridge.m"
+ "NSString *getCCSetDescriptorKeySourceIdentifier(void)"
+ "v24@?0@\"CCSetDonation\"8@\"NSError\"16"
+ "validity"
+ "void *CascadeSetsLibrary(void)"
- "@\"LNParameter\"24@?0@\"LNProperty\"8Q16"
- "LNConnectionErrorCodeInvalidXPCHost"
- "LNConnectionErrorCodeMismatchingAuditTokens"
- "com.apple.appintents.extension-mediator.internal-queue"
- "com.apple.private.appintents.xpc-host"
- "hasNextAction"
- "v40@?0@\"LNConnection\"8@\"LNAction\"16@\"<LNConnectionHostInterface>\"24@\"NSError\"32"
- "v40@?0@\"NSXPCListenerEndpoint\"8@\"NSData\"16@\"LNAction\"24@\"NSError\"32"

```
