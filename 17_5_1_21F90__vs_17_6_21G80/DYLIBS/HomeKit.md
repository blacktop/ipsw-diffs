## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1124.6.30.0.1
-  __TEXT.__text: 0x27e31c
+1124.7.30.0.0
+  __TEXT.__text: 0x27f36c
   __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_methlist: 0x20ce4
+  __TEXT.__objc_methlist: 0x20dfc
   __TEXT.__const: 0x290
   __TEXT.__gcc_except_tab: 0x40ac
-  __TEXT.__cstring: 0x261a7
+  __TEXT.__cstring: 0x26271
   __TEXT.__oslogstring: 0x25d4f
   __TEXT.__dlopen_cstrs: 0x3ee
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x9484
-  __TEXT.__objc_classname: 0x4ae3
-  __TEXT.__objc_methname: 0x422d7
-  __TEXT.__objc_methtype: 0x7d28
-  __TEXT.__objc_stubs: 0x23700
+  __TEXT.__unwind_info: 0x9498
+  __TEXT.__objc_classname: 0x4ae5
+  __TEXT.__objc_methname: 0x42605
+  __TEXT.__objc_methtype: 0x7d9e
+  __TEXT.__objc_stubs: 0x23780
   __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x6ee0
+  __DATA_CONST.__const: 0x6f00
   __DATA_CONST.__objc_classlist: 0x10a8
   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x478
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x32980
-  __DATA_CONST.__objc_selrefs: 0xc1b8
+  __DATA_CONST.__objc_const: 0x32ae0
+  __DATA_CONST.__objc_selrefs: 0xc268
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_classrefs: 0x1348
   __DATA_CONST.__objc_superrefs: 0xe18
   __DATA_CONST.__objc_arraydata: 0x1330
-  __AUTH_CONST.__cfstring: 0x23e00
+  __AUTH_CONST.__cfstring: 0x23ee0
   __AUTH_CONST.__objc_const: 0xf4e8
   __AUTH_CONST.__const: 0x19c0
   __AUTH_CONST.__objc_intobj: 0x798

   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0x6a8
   __AUTH.__objc_data: 0x7df0
-  __DATA.__objc_ivar: 0x2260
+  __DATA.__objc_ivar: 0x2278
   __DATA.__data: 0x36c0
   __DATA.__common: 0x18
   __DATA.__bss: 0x818

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BC973D4E-950D-3EB2-BCC9-101AC305F278
-  Functions: 12840
-  Symbols:   40968
-  CStrings:  23548
+  UUID: 00295FB4-4C8A-33F5-96D5-6957A2A57946
+  Functions: 12864
+  Symbols:   41027
+  CStrings:  23595
 
Symbols:
+ +[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo nearbyVisibleDeviceInfosType]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo StringAsPrimaryResidentStatus:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo addNearbyVisibleDeviceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo clearNearbyVisibleDeviceInfos]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasNumAppleMediaAccessories]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasNumResidents]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo hasPrimaryResidentStatus]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo nearbyVisibleDeviceInfosAtIndex:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo nearbyVisibleDeviceInfosCount]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo nearbyVisibleDeviceInfos]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo numAppleMediaAccessories]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo numResidents]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo primaryResidentStatusAsString:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo primaryResidentStatus]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setHasNumAppleMediaAccessories:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setHasNumResidents:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setHasPrimaryResidentStatus:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setNearbyVisibleDeviceInfos:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setNumAppleMediaAccessories:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setNumResidents:]
+ -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setPrimaryResidentStatus:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo hasNumAppleMediaAccessories]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo hasNumResidents]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo numAppleMediaAccessories]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo numResidents]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setHasNumAppleMediaAccessories:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setHasNumResidents:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setNumAppleMediaAccessories:]
+ -[HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo setNumResidents:]
+ -[HMHomeManager fetchNetworkMismatchInfoWithCompletionHandler:]
+ GCC_except_table10199
+ GCC_except_table10238
+ GCC_except_table10251
+ GCC_except_table10588
+ GCC_except_table10590
+ GCC_except_table10592
+ GCC_except_table10593
+ GCC_except_table10624
+ GCC_except_table10626
+ GCC_except_table10628
+ GCC_except_table10634
+ GCC_except_table10635
+ GCC_except_table10636
+ GCC_except_table10744
+ GCC_except_table10745
+ GCC_except_table10771
+ GCC_except_table10773
+ GCC_except_table10777
+ GCC_except_table10778
+ GCC_except_table10826
+ GCC_except_table10852
+ GCC_except_table10889
+ GCC_except_table10893
+ GCC_except_table10934
+ GCC_except_table10935
+ GCC_except_table10936
+ GCC_except_table10937
+ GCC_except_table10938
+ GCC_except_table10939
+ GCC_except_table10940
+ GCC_except_table10942
+ GCC_except_table10943
+ GCC_except_table10944
+ GCC_except_table10945
+ GCC_except_table10946
+ GCC_except_table10947
+ GCC_except_table10948
+ GCC_except_table10965
+ GCC_except_table10992
+ GCC_except_table11099
+ GCC_except_table11100
+ GCC_except_table11103
+ GCC_except_table11167
+ GCC_except_table11169
+ GCC_except_table11177
+ GCC_except_table11183
+ GCC_except_table11184
+ GCC_except_table11190
+ GCC_except_table11192
+ GCC_except_table11197
+ GCC_except_table11198
+ GCC_except_table11199
+ GCC_except_table11402
+ GCC_except_table11403
+ GCC_except_table11573
+ GCC_except_table11576
+ GCC_except_table11581
+ GCC_except_table11585
+ GCC_except_table11591
+ GCC_except_table11596
+ GCC_except_table11598
+ GCC_except_table11603
+ GCC_except_table11604
+ GCC_except_table11606
+ GCC_except_table11691
+ GCC_except_table11710
+ GCC_except_table11711
+ GCC_except_table11712
+ GCC_except_table11713
+ GCC_except_table11718
+ GCC_except_table11732
+ GCC_except_table11738
+ GCC_except_table11741
+ GCC_except_table11743
+ GCC_except_table11825
+ GCC_except_table11827
+ GCC_except_table11839
+ GCC_except_table11844
+ GCC_except_table11850
+ GCC_except_table11852
+ GCC_except_table11854
+ GCC_except_table11856
+ GCC_except_table11858
+ GCC_except_table11860
+ GCC_except_table11862
+ GCC_except_table11996
+ GCC_except_table12052
+ GCC_except_table12053
+ GCC_except_table12054
+ GCC_except_table12055
+ GCC_except_table12066
+ GCC_except_table12091
+ GCC_except_table12092
+ GCC_except_table12145
+ GCC_except_table12168
+ GCC_except_table12171
+ GCC_except_table12303
+ GCC_except_table12415
+ GCC_except_table12416
+ GCC_except_table12417
+ GCC_except_table12465
+ GCC_except_table12466
+ GCC_except_table12468
+ GCC_except_table12471
+ GCC_except_table12473
+ GCC_except_table12475
+ GCC_except_table12507
+ GCC_except_table12550
+ GCC_except_table12555
+ GCC_except_table12558
+ GCC_except_table12618
+ GCC_except_table12703
+ GCC_except_table12711
+ GCC_except_table12764
+ GCC_except_table12766
+ GCC_except_table12775
+ GCC_except_table12778
+ GCC_except_table12798
+ GCC_except_table12800
+ GCC_except_table12801
+ GCC_except_table6752
+ GCC_except_table6759
+ GCC_except_table6767
+ GCC_except_table6814
+ GCC_except_table6826
+ GCC_except_table6838
+ GCC_except_table6865
+ GCC_except_table6874
+ GCC_except_table6881
+ GCC_except_table6884
+ GCC_except_table6887
+ GCC_except_table6890
+ GCC_except_table6893
+ GCC_except_table6902
+ GCC_except_table6912
+ GCC_except_table6932
+ GCC_except_table6935
+ GCC_except_table6938
+ GCC_except_table6941
+ GCC_except_table6944
+ GCC_except_table6947
+ GCC_except_table6950
+ GCC_except_table6953
+ GCC_except_table6956
+ GCC_except_table6959
+ GCC_except_table6962
+ GCC_except_table6965
+ GCC_except_table6968
+ GCC_except_table6971
+ GCC_except_table6974
+ GCC_except_table6977
+ GCC_except_table6980
+ GCC_except_table6984
+ GCC_except_table6996
+ GCC_except_table6997
+ GCC_except_table7006
+ GCC_except_table7025
+ GCC_except_table7050
+ GCC_except_table7066
+ GCC_except_table7086
+ GCC_except_table7090
+ GCC_except_table7265
+ GCC_except_table7479
+ GCC_except_table7549
+ GCC_except_table7658
+ GCC_except_table7669
+ GCC_except_table7745
+ GCC_except_table7763
+ GCC_except_table7769
+ GCC_except_table7771
+ GCC_except_table7773
+ GCC_except_table7774
+ GCC_except_table7911
+ GCC_except_table7921
+ GCC_except_table7924
+ GCC_except_table7926
+ GCC_except_table7929
+ GCC_except_table7960
+ GCC_except_table7962
+ GCC_except_table7980
+ GCC_except_table7988
+ GCC_except_table7990
+ GCC_except_table7992
+ GCC_except_table7994
+ GCC_except_table8001
+ GCC_except_table8007
+ GCC_except_table8009
+ GCC_except_table8011
+ GCC_except_table8012
+ GCC_except_table8021
+ GCC_except_table8089
+ GCC_except_table8093
+ GCC_except_table8095
+ GCC_except_table8097
+ GCC_except_table8119
+ GCC_except_table8121
+ GCC_except_table8123
+ GCC_except_table8125
+ GCC_except_table8144
+ GCC_except_table8294
+ GCC_except_table8296
+ GCC_except_table8297
+ GCC_except_table8298
+ GCC_except_table8300
+ GCC_except_table8302
+ GCC_except_table8303
+ GCC_except_table8304
+ GCC_except_table8340
+ GCC_except_table8343
+ GCC_except_table8344
+ GCC_except_table8347
+ GCC_except_table8350
+ GCC_except_table8351
+ GCC_except_table8395
+ GCC_except_table8396
+ GCC_except_table8397
+ GCC_except_table8404
+ GCC_except_table8405
+ GCC_except_table8407
+ GCC_except_table8469
+ GCC_except_table8470
+ GCC_except_table8471
+ GCC_except_table8508
+ GCC_except_table8690
+ GCC_except_table8691
+ GCC_except_table8692
+ GCC_except_table8696
+ GCC_except_table8751
+ GCC_except_table8772
+ GCC_except_table8843
+ GCC_except_table8849
+ GCC_except_table8851
+ GCC_except_table8853
+ GCC_except_table8855
+ GCC_except_table8863
+ GCC_except_table8912
+ GCC_except_table8913
+ GCC_except_table8915
+ GCC_except_table8940
+ GCC_except_table8968
+ GCC_except_table9143
+ GCC_except_table9195
+ GCC_except_table9202
+ GCC_except_table9207
+ GCC_except_table9212
+ GCC_except_table9229
+ GCC_except_table9232
+ GCC_except_table9235
+ GCC_except_table9237
+ GCC_except_table9267
+ GCC_except_table9287
+ GCC_except_table9288
+ GCC_except_table9289
+ GCC_except_table9326
+ GCC_except_table9327
+ GCC_except_table9331
+ GCC_except_table9333
+ GCC_except_table9335
+ GCC_except_table9394
+ GCC_except_table9421
+ GCC_except_table9426
+ GCC_except_table9428
+ GCC_except_table9432
+ GCC_except_table9438
+ GCC_except_table9440
+ GCC_except_table9446
+ GCC_except_table9450
+ GCC_except_table9453
+ GCC_except_table9464
+ GCC_except_table9470
+ GCC_except_table9476
+ GCC_except_table9479
+ GCC_except_table9487
+ GCC_except_table9488
+ GCC_except_table9501
+ GCC_except_table9511
+ GCC_except_table9715
+ GCC_except_table9728
+ GCC_except_table9777
+ GCC_except_table9778
+ GCC_except_table9780
+ GCC_except_table9784
+ GCC_except_table9792
+ GCC_except_table9848
+ GCC_except_table9851
+ GCC_except_table9852
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._nearbyVisibleDeviceInfos
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._numAppleMediaAccessories
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._numResidents
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._primaryResidentStatus
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._has
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._numAppleMediaAccessories
+ OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoPrimaryResidentDiagnosticInfo._numResidents
+ _CoreAnalyticsLibraryCore.frameworkLibrary.36758
+ _CoreHAPLibraryCore.frameworkLibrary.29872
+ _HMHomeManagerNetworkMismatchInfoMessage
+ _IDSFoundationLibraryCore.40451
+ _IDSFoundationLibraryCore.frameworkLibrary.40453
+ _UIKitLibrary.40683
+ _UIKitLibraryCore.40679
+ _UIKitLibraryCore.frameworkLibrary.40692
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.785
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.789
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.793
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.795
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.794
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.796
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.792
+ ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.535
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.798
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.800
+ ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.707
+ ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.767
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.629
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.630
+ ___58-[HMHomeManager __resolveAccountHandle:completionHandler:]_block_invoke.694
+ ___61-[HMHomeManager __removeAccountWithHandle:completionHandler:]_block_invoke.696
+ ___63-[HMHomeManager fetchNetworkMismatchInfoWithCompletionHandler:]_block_invoke
+ ___65-[HMHomeManager __removeAccountWithIdentifier:completionHandler:]_block_invoke.695
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.725
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.729
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.731
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.733
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.734
+ ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.851
+ ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.704
+ ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke.697
+ ___Block_byref_object_copy_.29968
+ ___Block_byref_object_copy_.36645
+ ___Block_byref_object_copy_.39577
+ ___Block_byref_object_copy_.61134
+ ___Block_byref_object_dispose_.29969
+ ___Block_byref_object_dispose_.36646
+ ___Block_byref_object_dispose_.39578
+ ___Block_byref_object_dispose_.61135
+ ___CoreAnalyticsLibraryCore_block_invoke.36759
+ ___CoreHAPLibraryCore_block_invoke.29873
+ ___IDSFoundationLibraryCore_block_invoke.40454
+ ___UIKitLibraryCore_block_invoke.40693
+ _____HMHomeManagerRegisterForNotifications_block_invoke.1407
+ ___block_literal_global.101.36766
+ ___block_literal_global.12.46681
+ ___block_literal_global.121.49625
+ ___block_literal_global.30182
+ ___block_literal_global.30650
+ ___block_literal_global.30922
+ ___block_literal_global.31769
+ ___block_literal_global.32140
+ ___block_literal_global.33.60474
+ ___block_literal_global.33242
+ ___block_literal_global.34146
+ ___block_literal_global.34378
+ ___block_literal_global.34603
+ ___block_literal_global.35558
+ ___block_literal_global.36753
+ ___block_literal_global.37003
+ ___block_literal_global.37345
+ ___block_literal_global.37975
+ ___block_literal_global.38842
+ ___block_literal_global.38969
+ ___block_literal_global.39246
+ ___block_literal_global.40515
+ ___block_literal_global.40611
+ ___block_literal_global.41320
+ ___block_literal_global.41510
+ ___block_literal_global.42133
+ ___block_literal_global.42759
+ ___block_literal_global.43205
+ ___block_literal_global.43524
+ ___block_literal_global.44286
+ ___block_literal_global.45174
+ ___block_literal_global.46402
+ ___block_literal_global.46693
+ ___block_literal_global.46959
+ ___block_literal_global.47154
+ ___block_literal_global.47383
+ ___block_literal_global.48090
+ ___block_literal_global.48210
+ ___block_literal_global.48942
+ ___block_literal_global.49378
+ ___block_literal_global.49712
+ ___block_literal_global.50626
+ ___block_literal_global.516
+ ___block_literal_global.521
+ ___block_literal_global.53195
+ ___block_literal_global.53903
+ ___block_literal_global.55230
+ ___block_literal_global.55925
+ ___block_literal_global.56460
+ ___block_literal_global.56772
+ ___block_literal_global.57286
+ ___block_literal_global.57463
+ ___block_literal_global.57827
+ ___block_literal_global.58067
+ ___block_literal_global.59708
+ ___block_literal_global.59876
+ ___block_literal_global.60214
+ ___block_literal_global.60480
+ ___block_literal_global.60842
+ ___block_literal_global.61132
+ ___block_literal_global.61428
+ ___block_literal_global.73.37338
+ ___block_literal_global.746
+ ___block_literal_global.748
+ ___block_literal_global.81.36975
+ ___block_literal_global.855
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.36756
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.40688
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.40682
+ __unnamed_array_storage.29871
+ __unnamed_array_storage.55353
+ __unnamed_array_storage.56897
+ __unnamed_array_storage.60330
+ _audit_stringCoreAnalytics.36762
+ _audit_stringCoreHAP.29875
+ _audit_stringIDSFoundation.40456
+ _audit_stringUIKit.40695
+ _getAnalyticsSendEventLazySymbolLoc.ptr.36755
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.40687
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.40681
+ _logCategory._hmf_once_t0.41319
+ _logCategory._hmf_once_t0.41509
+ _logCategory._hmf_once_t0.42132
+ _logCategory._hmf_once_t0.58066
+ _logCategory._hmf_once_t1.36979
+ _logCategory._hmf_once_t1.42758
+ _logCategory._hmf_once_t1.46680
+ _logCategory._hmf_once_t1.48209
+ _logCategory._hmf_once_t1.53194
+ _logCategory._hmf_once_t14.57826
+ _logCategory._hmf_once_t16.34377
+ _logCategory._hmf_once_t16.59875
+ _logCategory._hmf_once_t2.30649
+ _logCategory._hmf_once_t24.37337
+ _logCategory._hmf_once_t25.60841
+ _logCategory._hmf_once_t27.49459
+ _logCategory._hmf_once_t27.56771
+ _logCategory._hmf_once_t28.61427
+ _logCategory._hmf_once_t3.38968
+ _logCategory._hmf_once_t3.60473
+ _logCategory._hmf_once_t31.59707
+ _logCategory._hmf_once_t33.49735
+ _logCategory._hmf_once_t346
+ _logCategory._hmf_once_t35.35557
+ _logCategory._hmf_once_t42.55924
+ _logCategory._hmf_once_t6.31768
+ _logCategory._hmf_once_t6.34145
+ _logCategory._hmf_once_t6.53902
+ _logCategory._hmf_once_t64.55229
+ _logCategory._hmf_once_t7.48089
+ _logCategory._hmf_once_t8.34602
+ _logCategory._hmf_once_t8.44285
+ _logCategory._hmf_once_t8.47172
+ _logCategory._hmf_once_v1.41321
+ _logCategory._hmf_once_v1.41511
+ _logCategory._hmf_once_v1.42134
+ _logCategory._hmf_once_v1.58068
+ _logCategory._hmf_once_v15.57828
+ _logCategory._hmf_once_v17.34379
+ _logCategory._hmf_once_v17.59877
+ _logCategory._hmf_once_v2.36980
+ _logCategory._hmf_once_v2.42760
+ _logCategory._hmf_once_v2.46682
+ _logCategory._hmf_once_v2.48211
+ _logCategory._hmf_once_v2.53196
+ _logCategory._hmf_once_v25.37339
+ _logCategory._hmf_once_v26.60843
+ _logCategory._hmf_once_v28.49460
+ _logCategory._hmf_once_v28.56773
+ _logCategory._hmf_once_v29.61429
+ _logCategory._hmf_once_v3.30651
+ _logCategory._hmf_once_v32.59709
+ _logCategory._hmf_once_v34.49736
+ _logCategory._hmf_once_v347
+ _logCategory._hmf_once_v36.35559
+ _logCategory._hmf_once_v4.38970
+ _logCategory._hmf_once_v4.60475
+ _logCategory._hmf_once_v43.55926
+ _logCategory._hmf_once_v65.55231
+ _logCategory._hmf_once_v7.31770
+ _logCategory._hmf_once_v7.34147
+ _logCategory._hmf_once_v7.53904
+ _logCategory._hmf_once_v8.48091
+ _logCategory._hmf_once_v9.34604
+ _logCategory._hmf_once_v9.44287
+ _logCategory._hmf_once_v9.47173
+ _objc_msgSend$addNearbyVisibleDeviceInfos:
+ _objc_msgSend$clearNearbyVisibleDeviceInfos
+ _objc_msgSend$nearbyVisibleDeviceInfosAtIndex:
+ _objc_msgSend$nearbyVisibleDeviceInfosCount
+ _sharedInstance.onceToken.38841
+ _sharedManager.onceToken.56914
+ _supportedValueClasses.onceToken.46958
+ _supportedValueClasses.onceToken.55195
+ _supportedValueClasses.supportedValueClasses.46960
+ _supportedValueClasses.supportedValueClasses.55196
+ _unconfigureQueue.onceToken.37344
+ _unconfigureQueue.unconfigureQueue.37346
- +[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo proximityVisibleDeviceInfosType]
- -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo addProximityVisibleDeviceInfos:]
- -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo clearProximityVisibleDeviceInfos]
- -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo proximityVisibleDeviceInfosAtIndex:]
- -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo proximityVisibleDeviceInfosCount]
- -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo proximityVisibleDeviceInfos]
- -[HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo setProximityVisibleDeviceInfos:]
- GCC_except_table10175
- GCC_except_table10214
- GCC_except_table10227
- GCC_except_table10564
- GCC_except_table10566
- GCC_except_table10568
- GCC_except_table10569
- GCC_except_table10600
- GCC_except_table10602
- GCC_except_table10604
- GCC_except_table10610
- GCC_except_table10611
- GCC_except_table10612
- GCC_except_table10720
- GCC_except_table10721
- GCC_except_table10747
- GCC_except_table10749
- GCC_except_table10753
- GCC_except_table10754
- GCC_except_table10802
- GCC_except_table10828
- GCC_except_table10841
- GCC_except_table10869
- GCC_except_table10910
- GCC_except_table10911
- GCC_except_table10912
- GCC_except_table10913
- GCC_except_table10914
- GCC_except_table10915
- GCC_except_table10916
- GCC_except_table10917
- GCC_except_table10918
- GCC_except_table10919
- GCC_except_table10920
- GCC_except_table10921
- GCC_except_table10922
- GCC_except_table10923
- GCC_except_table10924
- GCC_except_table10968
- GCC_except_table11075
- GCC_except_table11076
- GCC_except_table11079
- GCC_except_table11143
- GCC_except_table11145
- GCC_except_table11153
- GCC_except_table11159
- GCC_except_table11160
- GCC_except_table11166
- GCC_except_table11168
- GCC_except_table11173
- GCC_except_table11174
- GCC_except_table11175
- GCC_except_table11378
- GCC_except_table11379
- GCC_except_table11549
- GCC_except_table11552
- GCC_except_table11557
- GCC_except_table11561
- GCC_except_table11567
- GCC_except_table11572
- GCC_except_table11574
- GCC_except_table11579
- GCC_except_table11580
- GCC_except_table11582
- GCC_except_table11665
- GCC_except_table11667
- GCC_except_table11686
- GCC_except_table11687
- GCC_except_table11688
- GCC_except_table11694
- GCC_except_table11708
- GCC_except_table11714
- GCC_except_table11717
- GCC_except_table11719
- GCC_except_table11801
- GCC_except_table11803
- GCC_except_table11806
- GCC_except_table11814
- GCC_except_table11815
- GCC_except_table11820
- GCC_except_table11826
- GCC_except_table11828
- GCC_except_table11832
- GCC_except_table11834
- GCC_except_table11836
- GCC_except_table11972
- GCC_except_table12028
- GCC_except_table12029
- GCC_except_table12030
- GCC_except_table12031
- GCC_except_table12042
- GCC_except_table12043
- GCC_except_table12068
- GCC_except_table12121
- GCC_except_table12144
- GCC_except_table12147
- GCC_except_table12279
- GCC_except_table12391
- GCC_except_table12392
- GCC_except_table12393
- GCC_except_table12441
- GCC_except_table12442
- GCC_except_table12444
- GCC_except_table12447
- GCC_except_table12449
- GCC_except_table12451
- GCC_except_table12483
- GCC_except_table12526
- GCC_except_table12531
- GCC_except_table12534
- GCC_except_table12594
- GCC_except_table12679
- GCC_except_table12687
- GCC_except_table12740
- GCC_except_table12742
- GCC_except_table12751
- GCC_except_table12754
- GCC_except_table12774
- GCC_except_table12776
- GCC_except_table12777
- GCC_except_table6750
- GCC_except_table6755
- GCC_except_table6765
- GCC_except_table6808
- GCC_except_table6824
- GCC_except_table6836
- GCC_except_table6863
- GCC_except_table6872
- GCC_except_table6879
- GCC_except_table6882
- GCC_except_table6885
- GCC_except_table6888
- GCC_except_table6891
- GCC_except_table6900
- GCC_except_table6910
- GCC_except_table6930
- GCC_except_table6933
- GCC_except_table6936
- GCC_except_table6939
- GCC_except_table6942
- GCC_except_table6945
- GCC_except_table6948
- GCC_except_table6951
- GCC_except_table6954
- GCC_except_table6957
- GCC_except_table6960
- GCC_except_table6963
- GCC_except_table6966
- GCC_except_table6969
- GCC_except_table6972
- GCC_except_table6975
- GCC_except_table6978
- GCC_except_table6982
- GCC_except_table6994
- GCC_except_table6995
- GCC_except_table7004
- GCC_except_table7021
- GCC_except_table7048
- GCC_except_table7062
- GCC_except_table7084
- GCC_except_table7088
- GCC_except_table7249
- GCC_except_table7463
- GCC_except_table7533
- GCC_except_table7637
- GCC_except_table7642
- GCC_except_table7729
- GCC_except_table7747
- GCC_except_table7753
- GCC_except_table7755
- GCC_except_table7757
- GCC_except_table7758
- GCC_except_table7892
- GCC_except_table7895
- GCC_except_table7905
- GCC_except_table7910
- GCC_except_table7913
- GCC_except_table7944
- GCC_except_table7946
- GCC_except_table7964
- GCC_except_table7972
- GCC_except_table7974
- GCC_except_table7976
- GCC_except_table7978
- GCC_except_table7985
- GCC_except_table7991
- GCC_except_table7993
- GCC_except_table7995
- GCC_except_table7996
- GCC_except_table8005
- GCC_except_table8063
- GCC_except_table8065
- GCC_except_table8073
- GCC_except_table8075
- GCC_except_table8077
- GCC_except_table8087
- GCC_except_table8105
- GCC_except_table8109
- GCC_except_table8128
- GCC_except_table8278
- GCC_except_table8280
- GCC_except_table8281
- GCC_except_table8282
- GCC_except_table8284
- GCC_except_table8286
- GCC_except_table8287
- GCC_except_table8288
- GCC_except_table8324
- GCC_except_table8327
- GCC_except_table8328
- GCC_except_table8331
- GCC_except_table8334
- GCC_except_table8335
- GCC_except_table8379
- GCC_except_table8380
- GCC_except_table8381
- GCC_except_table8388
- GCC_except_table8389
- GCC_except_table8391
- GCC_except_table8453
- GCC_except_table8454
- GCC_except_table8455
- GCC_except_table8492
- GCC_except_table8674
- GCC_except_table8675
- GCC_except_table8676
- GCC_except_table8680
- GCC_except_table8735
- GCC_except_table8756
- GCC_except_table8827
- GCC_except_table8833
- GCC_except_table8835
- GCC_except_table8837
- GCC_except_table8839
- GCC_except_table8847
- GCC_except_table8896
- GCC_except_table8897
- GCC_except_table8899
- GCC_except_table8924
- GCC_except_table8952
- GCC_except_table9127
- GCC_except_table9179
- GCC_except_table9186
- GCC_except_table9191
- GCC_except_table9196
- GCC_except_table9200
- GCC_except_table9213
- GCC_except_table9219
- GCC_except_table9221
- GCC_except_table9251
- GCC_except_table9271
- GCC_except_table9272
- GCC_except_table9273
- GCC_except_table9310
- GCC_except_table9311
- GCC_except_table9315
- GCC_except_table9317
- GCC_except_table9319
- GCC_except_table9378
- GCC_except_table9405
- GCC_except_table9408
- GCC_except_table9410
- GCC_except_table9412
- GCC_except_table9414
- GCC_except_table9416
- GCC_except_table9422
- GCC_except_table9434
- GCC_except_table9437
- GCC_except_table9444
- GCC_except_table9448
- GCC_except_table9454
- GCC_except_table9463
- GCC_except_table9471
- GCC_except_table9472
- GCC_except_table9485
- GCC_except_table9495
- GCC_except_table9699
- GCC_except_table9712
- GCC_except_table9761
- GCC_except_table9762
- GCC_except_table9764
- GCC_except_table9768
- GCC_except_table9776
- GCC_except_table9832
- GCC_except_table9835
- GCC_except_table9836
- OBJC_IVAR_$_HMAccessoryDiagnosticInfoProtoAppleMediaAccessoryDiagnosticInfo._proximityVisibleDeviceInfos
- _CoreAnalyticsLibraryCore.frameworkLibrary.36699
- _CoreHAPLibraryCore.frameworkLibrary.29869
- _IDSFoundationLibraryCore.40392
- _IDSFoundationLibraryCore.frameworkLibrary.40394
- _UIKitLibrary.40624
- _UIKitLibraryCore.40620
- _UIKitLibraryCore.frameworkLibrary.40633
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.780
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.782
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.790
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.792
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.785
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.793
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.789
- ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.532
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.795
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.797
- ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.704
- ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.764
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.626
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.627
- ___58-[HMHomeManager __resolveAccountHandle:completionHandler:]_block_invoke.691
- ___61-[HMHomeManager __removeAccountWithHandle:completionHandler:]_block_invoke.693
- ___65-[HMHomeManager __removeAccountWithIdentifier:completionHandler:]_block_invoke.692
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.722
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.726
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.728
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.730
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.731
- ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.848
- ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.701
- ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke.694
- ___Block_byref_object_copy_.29959
- ___Block_byref_object_copy_.36586
- ___Block_byref_object_copy_.39518
- ___Block_byref_object_copy_.61067
- ___Block_byref_object_dispose_.29960
- ___Block_byref_object_dispose_.36587
- ___Block_byref_object_dispose_.39519
- ___Block_byref_object_dispose_.61068
- ___CoreAnalyticsLibraryCore_block_invoke.36700
- ___CoreHAPLibraryCore_block_invoke.29870
- ___IDSFoundationLibraryCore_block_invoke.40395
- ___UIKitLibraryCore_block_invoke.40634
- _____HMHomeManagerRegisterForNotifications_block_invoke.1403
- ___block_literal_global.101.36707
- ___block_literal_global.12.46592
- ___block_literal_global.121.49537
- ___block_literal_global.30171
- ___block_literal_global.30585
- ___block_literal_global.30857
- ___block_literal_global.31704
- ___block_literal_global.32075
- ___block_literal_global.33.60407
- ___block_literal_global.33176
- ___block_literal_global.34087
- ___block_literal_global.34319
- ___block_literal_global.34544
- ___block_literal_global.35499
- ___block_literal_global.36694
- ___block_literal_global.36944
- ___block_literal_global.37286
- ___block_literal_global.37916
- ___block_literal_global.38783
- ___block_literal_global.38910
- ___block_literal_global.39187
- ___block_literal_global.40456
- ___block_literal_global.40552
- ___block_literal_global.41261
- ___block_literal_global.41451
- ___block_literal_global.42074
- ___block_literal_global.42700
- ___block_literal_global.43146
- ___block_literal_global.43465
- ___block_literal_global.44197
- ___block_literal_global.45085
- ___block_literal_global.46313
- ___block_literal_global.46604
- ___block_literal_global.46870
- ___block_literal_global.47065
- ___block_literal_global.47294
- ___block_literal_global.48001
- ___block_literal_global.48121
- ___block_literal_global.48854
- ___block_literal_global.49290
- ___block_literal_global.49624
- ___block_literal_global.50538
- ___block_literal_global.513
- ___block_literal_global.518
- ___block_literal_global.53128
- ___block_literal_global.53836
- ___block_literal_global.55163
- ___block_literal_global.55857
- ___block_literal_global.56392
- ___block_literal_global.56704
- ___block_literal_global.57218
- ___block_literal_global.57395
- ___block_literal_global.57759
- ___block_literal_global.57999
- ___block_literal_global.59641
- ___block_literal_global.59809
- ___block_literal_global.60147
- ___block_literal_global.60413
- ___block_literal_global.60775
- ___block_literal_global.61065
- ___block_literal_global.61361
- ___block_literal_global.73.37279
- ___block_literal_global.743
- ___block_literal_global.745
- ___block_literal_global.81.36916
- ___block_literal_global.852
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.36697
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.40629
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.40623
- __unnamed_array_storage.29868
- __unnamed_array_storage.55286
- __unnamed_array_storage.56829
- __unnamed_array_storage.60263
- _audit_stringCoreAnalytics.36703
- _audit_stringCoreHAP.29872
- _audit_stringIDSFoundation.40397
- _audit_stringUIKit.40636
- _getAnalyticsSendEventLazySymbolLoc.ptr.36696
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.40628
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.40622
- _logCategory._hmf_once_t0.41260
- _logCategory._hmf_once_t0.41450
- _logCategory._hmf_once_t0.42073
- _logCategory._hmf_once_t0.57998
- _logCategory._hmf_once_t1.36920
- _logCategory._hmf_once_t1.42699
- _logCategory._hmf_once_t1.46591
- _logCategory._hmf_once_t1.48120
- _logCategory._hmf_once_t1.53127
- _logCategory._hmf_once_t14.57758
- _logCategory._hmf_once_t16.34318
- _logCategory._hmf_once_t16.59808
- _logCategory._hmf_once_t2.30584
- _logCategory._hmf_once_t24.37278
- _logCategory._hmf_once_t25.60774
- _logCategory._hmf_once_t27.49371
- _logCategory._hmf_once_t27.56703
- _logCategory._hmf_once_t28.61360
- _logCategory._hmf_once_t3.38909
- _logCategory._hmf_once_t3.60406
- _logCategory._hmf_once_t31.59640
- _logCategory._hmf_once_t33.49647
- _logCategory._hmf_once_t344
- _logCategory._hmf_once_t35.35498
- _logCategory._hmf_once_t42.55856
- _logCategory._hmf_once_t6.31703
- _logCategory._hmf_once_t6.34086
- _logCategory._hmf_once_t6.53835
- _logCategory._hmf_once_t64.55162
- _logCategory._hmf_once_t7.48000
- _logCategory._hmf_once_t8.34543
- _logCategory._hmf_once_t8.44196
- _logCategory._hmf_once_t8.47083
- _logCategory._hmf_once_v1.41262
- _logCategory._hmf_once_v1.41452
- _logCategory._hmf_once_v1.42075
- _logCategory._hmf_once_v1.58000
- _logCategory._hmf_once_v15.57760
- _logCategory._hmf_once_v17.34320
- _logCategory._hmf_once_v17.59810
- _logCategory._hmf_once_v2.36921
- _logCategory._hmf_once_v2.42701
- _logCategory._hmf_once_v2.46593
- _logCategory._hmf_once_v2.48122
- _logCategory._hmf_once_v2.53129
- _logCategory._hmf_once_v25.37280
- _logCategory._hmf_once_v26.60776
- _logCategory._hmf_once_v28.49372
- _logCategory._hmf_once_v28.56705
- _logCategory._hmf_once_v29.61362
- _logCategory._hmf_once_v3.30586
- _logCategory._hmf_once_v32.59642
- _logCategory._hmf_once_v34.49648
- _logCategory._hmf_once_v345
- _logCategory._hmf_once_v36.35500
- _logCategory._hmf_once_v4.38911
- _logCategory._hmf_once_v4.60408
- _logCategory._hmf_once_v43.55858
- _logCategory._hmf_once_v65.55164
- _logCategory._hmf_once_v7.31705
- _logCategory._hmf_once_v7.34088
- _logCategory._hmf_once_v7.53837
- _logCategory._hmf_once_v8.48002
- _logCategory._hmf_once_v9.34545
- _logCategory._hmf_once_v9.44198
- _logCategory._hmf_once_v9.47084
- _sharedInstance.onceToken.38782
- _sharedManager.onceToken.56846
- _supportedValueClasses.onceToken.46869
- _supportedValueClasses.onceToken.55128
- _supportedValueClasses.supportedValueClasses.46871
- _supportedValueClasses.supportedValueClasses.55129
- _unconfigureQueue.onceToken.37285
- _unconfigureQueue.unconfigureQueue.37287
CStrings:
+ "("
+ "-[HMHomeManager fetchNetworkMismatchInfoWithCompletionHandler:]"
+ "HMHM.networkMismatchInfo"
+ "K\x16"
+ "KnownPrimary"
+ "NoKnownPrimary"
+ "StringAsPrimaryResidentStatus:"
+ "T@\"NSMutableArray\",&,N,V_nearbyVisibleDeviceInfos"
+ "Ti,N,V_primaryResidentStatus"
+ "Tq,N,V_numAppleMediaAccessories"
+ "Tq,N,V_numResidents"
+ "_nearbyVisibleDeviceInfos"
+ "_numAppleMediaAccessories"
+ "_numResidents"
+ "_primaryResidentStatus"
+ "addNearbyVisibleDeviceInfos:"
+ "clearNearbyVisibleDeviceInfos"
+ "fetchNetworkMismatchInfoWithCompletionHandler:"
+ "hasNumAppleMediaAccessories"
+ "hasNumResidents"
+ "hasPrimaryResidentStatus"
+ "nearbyVisibleDeviceInfos"
+ "nearbyVisibleDeviceInfosAtIndex:"
+ "nearbyVisibleDeviceInfosCount"
+ "nearbyVisibleDeviceInfosType"
+ "numAppleMediaAccessories"
+ "numResidents"
+ "primaryResidentStatus"
+ "primaryResidentStatusAsString:"
+ "setHasNumAppleMediaAccessories:"
+ "setHasNumResidents:"
+ "setHasPrimaryResidentStatus:"
+ "setNearbyVisibleDeviceInfos:"
+ "setNumAppleMediaAccessories:"
+ "setNumResidents:"
+ "setPrimaryResidentStatus:"
+ "{?=\"generationTime\"b1\"numAppleMediaAccessories\"b1\"numResidents\"b1\"sfProblemFlags\"b1\"primaryResidentStatus\"b1}"
+ "{?=\"numAppleMediaAccessories\"b1\"numResidents\"b1}"
- "/\x02"
- "{?=\"generationTime\"b1\"sfProblemFlags\"b1}"

```
