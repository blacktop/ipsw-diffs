## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1345.1.0.1.1
-  __TEXT.__text: 0x2c8578
+1349.1.2.0.0
+  __TEXT.__text: 0x2c8774
   __TEXT.__auth_stubs: 0x1b00
   __TEXT.__objc_methlist: 0x257bc
   __TEXT.__const: 0x1d0c
   __TEXT.__dlopen_cstrs: 0x3a1
-  __TEXT.__cstring: 0x2a4ce
+  __TEXT.__cstring: 0x2a512
   __TEXT.__swift5_typeref: 0xa4c
   __TEXT.__constg_swiftt: 0x8fc
   __TEXT.__swift5_reflstr: 0x391

   __TEXT.__swift5_types: 0xa4
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__oslogstring: 0x2ab40
+  __TEXT.__oslogstring: 0x2ab9d
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__gcc_except_tab: 0x706c
   __TEXT.__ustring: 0x50

   __TEXT.__objc_classname: 0x4fc1
   __TEXT.__objc_methname: 0x48353
   __TEXT.__objc_methtype: 0x88d8
-  __TEXT.__objc_stubs: 0x25c40
+  __TEXT.__objc_stubs: 0x25c80
   __DATA_CONST.__got: 0x1818
-  __DATA_CONST.__const: 0x7e08
+  __DATA_CONST.__const: 0x7e10
   __DATA_CONST.__objc_classlist: 0x1228
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x4b0

   __DATA_CONST.__objc_superrefs: 0xf30
   __DATA_CONST.__objc_arraydata: 0x1380
   __AUTH_CONST.__auth_got: 0xd90
-  __AUTH_CONST.__const: 0x2a30
-  __AUTH_CONST.__cfstring: 0x277a0
+  __AUTH_CONST.__const: 0x2cc8
+  __AUTH_CONST.__cfstring: 0x277c0
   __AUTH_CONST.__objc_const: 0x436b0
   __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x8488
+  __AUTH.__objc_data: 0x8348
   __AUTH.__data: 0x580
   __DATA.__objc_ivar: 0x2528
-  __DATA.__data: 0x3e08
-  __DATA.__bss: 0x31d0
+  __DATA.__data: 0x3e18
+  __DATA.__bss: 0x31b0
   __DATA.__common: 0x59
-  __DATA_DIRTY.__objc_data: 0x32a0
-  __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x250
+  __DATA_DIRTY.__objc_data: 0x33e0
+  __DATA_DIRTY.__data: 0x28
+  __DATA_DIRTY.__bss: 0x270
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 506F74F8-B5BF-3192-A080-44FAD67B3BB5
-  Functions: 14331
-  Symbols:   44044
-  CStrings:  25657
+  UUID: 2C3D9A3B-A54D-351B-B639-99766A27FCFB
+  Functions: 14342
+  Symbols:   44048
+  CStrings:  25661
 
Symbols:
+ _CoreAnalyticsLibraryCore.frameworkLibrary.40535
+ _CoreHAPLibraryCore.frameworkLibrary.32831
+ _IDSFoundationLibraryCore.44865
+ _IDSFoundationLibraryCore.frameworkLibrary.44868
+ _UIKitLibrary.45096
+ _UIKitLibraryCore.45092
+ _UIKitLibraryCore.frameworkLibrary.45105
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.788
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.792
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.796
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.798
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.797
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.795
+ ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.528
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.800
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.802
+ ___46-[HMHomeManager removeHome:completionHandler:]_block_invoke.641
+ ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.710
+ ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.767
+ ___51-[HMHomeManager addHomeWithName:completionHandler:]_block_invoke.637
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.623
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.624
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.728
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.732
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.734
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.736
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.737
+ ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.859
+ ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.707
+ ___Block_byref_object_copy_.31290
+ ___Block_byref_object_copy_.32932
+ ___Block_byref_object_copy_.35110
+ ___Block_byref_object_copy_.40422
+ ___Block_byref_object_copy_.43893
+ ___Block_byref_object_copy_.63700
+ ___Block_byref_object_copy_.66062
+ ___Block_byref_object_dispose_.31291
+ ___Block_byref_object_dispose_.32933
+ ___Block_byref_object_dispose_.35111
+ ___Block_byref_object_dispose_.40423
+ ___Block_byref_object_dispose_.43894
+ ___Block_byref_object_dispose_.63701
+ ___Block_byref_object_dispose_.66063
+ ___CoreAnalyticsLibraryCore_block_invoke.40536
+ ___CoreHAPLibraryCore_block_invoke.32832
+ ___IDSFoundationLibraryCore_block_invoke.44869
+ ___UIKitLibraryCore_block_invoke.45106
+ ___block_literal_global.101.40543
+ ___block_literal_global.101.42737
+ ___block_literal_global.12.51280
+ ___block_literal_global.31408
+ ___block_literal_global.31747
+ ___block_literal_global.32006
+ ___block_literal_global.32292
+ ___block_literal_global.32372
+ ___block_literal_global.33.65399
+ ___block_literal_global.33076
+ ___block_literal_global.33572
+ ___block_literal_global.33844
+ ___block_literal_global.34896
+ ___block_literal_global.35133
+ ___block_literal_global.35435
+ ___block_literal_global.36751
+ ___block_literal_global.37724
+ ___block_literal_global.37958
+ ___block_literal_global.38187
+ ___block_literal_global.38583
+ ___block_literal_global.39333
+ ___block_literal_global.40530
+ ___block_literal_global.40780
+ ___block_literal_global.41119
+ ___block_literal_global.41785
+ ___block_literal_global.42747
+ ___block_literal_global.43011
+ ___block_literal_global.43280
+ ___block_literal_global.43565
+ ___block_literal_global.43785
+ ___block_literal_global.44930
+ ___block_literal_global.45024
+ ___block_literal_global.45731
+ ___block_literal_global.45923
+ ___block_literal_global.47106
+ ___block_literal_global.47548
+ ___block_literal_global.47874
+ ___block_literal_global.48640
+ ___block_literal_global.49297
+ ___block_literal_global.49655
+ ___block_literal_global.50929
+ ___block_literal_global.51292
+ ___block_literal_global.514
+ ___block_literal_global.51576
+ ___block_literal_global.51772
+ ___block_literal_global.52002
+ ___block_literal_global.52719
+ ___block_literal_global.52839
+ ___block_literal_global.53594
+ ___block_literal_global.53828
+ ___block_literal_global.54283
+ ___block_literal_global.54544
+ ___block_literal_global.55626
+ ___block_literal_global.57918
+ ___block_literal_global.58.37953
+ ___block_literal_global.58782
+ ___block_literal_global.60072
+ ___block_literal_global.60803
+ ___block_literal_global.61358
+ ___block_literal_global.61669
+ ___block_literal_global.62186
+ ___block_literal_global.62363
+ ___block_literal_global.62753
+ ___block_literal_global.63001
+ ___block_literal_global.64802
+ ___block_literal_global.65138
+ ___block_literal_global.65405
+ ___block_literal_global.65763
+ ___block_literal_global.66001
+ ___block_literal_global.66357
+ ___block_literal_global.701
+ ___block_literal_global.749
+ ___block_literal_global.751
+ ___block_literal_global.84.40724
+ ___block_literal_global.863
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.40533
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.45101
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.45095
+ ___swift_memcpy8_8
+ _audit_stringCoreAnalytics.40539
+ _audit_stringCoreHAP.32834
+ _audit_stringIDSFoundation.44871
+ _audit_stringUIKit.45108
+ _getAnalyticsSendEventLazySymbolLoc.ptr.40532
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.45100
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.45094
+ _logCategory._hmf_once_t0.32005
+ _logCategory._hmf_once_t0.32371
+ _logCategory._hmf_once_t0.43564
+ _logCategory._hmf_once_t0.45730
+ _logCategory._hmf_once_t0.45922
+ _logCategory._hmf_once_t0.63000
+ _logCategory._hmf_once_t1.40756
+ _logCategory._hmf_once_t1.47105
+ _logCategory._hmf_once_t1.51279
+ _logCategory._hmf_once_t1.52838
+ _logCategory._hmf_once_t1.57917
+ _logCategory._hmf_once_t13.42736
+ _logCategory._hmf_once_t14.62752
+ _logCategory._hmf_once_t16.31407
+ _logCategory._hmf_once_t16.37957
+ _logCategory._hmf_once_t16.64801
+ _logCategory._hmf_once_t2.33571
+ _logCategory._hmf_once_t21.62362
+ _logCategory._hmf_once_t24.41118
+ _logCategory._hmf_once_t24.41784
+ _logCategory._hmf_once_t25.65762
+ _logCategory._hmf_once_t27.61668
+ _logCategory._hmf_once_t3.43010
+ _logCategory._hmf_once_t3.53817
+ _logCategory._hmf_once_t3.65398
+ _logCategory._hmf_once_t31.54282
+ _logCategory._hmf_once_t31.66356
+ _logCategory._hmf_once_t32.53593
+ _logCategory._hmf_once_t366
+ _logCategory._hmf_once_t37.54570
+ _logCategory._hmf_once_t44.32291
+ _logCategory._hmf_once_t51.43279
+ _logCategory._hmf_once_t6.34895
+ _logCategory._hmf_once_t6.37723
+ _logCategory._hmf_once_t6.43784
+ _logCategory._hmf_once_t6.49296
+ _logCategory._hmf_once_t6.58781
+ _logCategory._hmf_once_t7.52718
+ _logCategory._hmf_once_t8.38186
+ _logCategory._hmf_once_t8.48639
+ _logCategory._hmf_once_t8.51790
+ _logCategory._hmf_once_v1.32007
+ _logCategory._hmf_once_v1.32373
+ _logCategory._hmf_once_v1.43566
+ _logCategory._hmf_once_v1.45732
+ _logCategory._hmf_once_v1.45924
+ _logCategory._hmf_once_v1.63002
+ _logCategory._hmf_once_v14.42738
+ _logCategory._hmf_once_v15.62754
+ _logCategory._hmf_once_v17.31409
+ _logCategory._hmf_once_v17.37959
+ _logCategory._hmf_once_v17.64803
+ _logCategory._hmf_once_v2.40757
+ _logCategory._hmf_once_v2.47107
+ _logCategory._hmf_once_v2.51281
+ _logCategory._hmf_once_v2.52840
+ _logCategory._hmf_once_v2.57919
+ _logCategory._hmf_once_v22.62364
+ _logCategory._hmf_once_v25.41120
+ _logCategory._hmf_once_v25.41786
+ _logCategory._hmf_once_v26.65764
+ _logCategory._hmf_once_v28.61670
+ _logCategory._hmf_once_v3.33573
+ _logCategory._hmf_once_v32.54284
+ _logCategory._hmf_once_v32.66358
+ _logCategory._hmf_once_v33.53595
+ _logCategory._hmf_once_v367
+ _logCategory._hmf_once_v38.54571
+ _logCategory._hmf_once_v4.43012
+ _logCategory._hmf_once_v4.53818
+ _logCategory._hmf_once_v4.65400
+ _logCategory._hmf_once_v45.32293
+ _logCategory._hmf_once_v52.43281
+ _logCategory._hmf_once_v7.34897
+ _logCategory._hmf_once_v7.37725
+ _logCategory._hmf_once_v7.43786
+ _logCategory._hmf_once_v7.49298
+ _logCategory._hmf_once_v7.58783
+ _logCategory._hmf_once_v8.52720
+ _logCategory._hmf_once_v9.38188
+ _logCategory._hmf_once_v9.48641
+ _logCategory._hmf_once_v9.51791
+ _objc_msgSend$isAllowedToEnableAdaptiveTemperatureAutomations
+ _objc_msgSend$setIsAllowedToEnableAdaptiveTemperatureAutomations:
+ _objectdestroy.22Tm
+ _sharedInstance.onceToken.42746
+ _sharedManager.onceToken.61815
+ _supportedValueClasses.onceToken.51575
+ _supportedValueClasses.onceToken.60034
+ _supportedValueClasses.supportedValueClasses.51577
+ _supportedValueClasses.supportedValueClasses.60035
- _CoreAnalyticsLibraryCore.frameworkLibrary.40536
- _CoreHAPLibraryCore.frameworkLibrary.32825
- _IDSFoundationLibraryCore.44867
- _IDSFoundationLibraryCore.frameworkLibrary.44870
- _UIKitLibrary.45098
- _UIKitLibraryCore.45094
- _UIKitLibraryCore.frameworkLibrary.45107
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.783
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.785
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.793
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.795
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.788
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.792
- ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.525
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.797
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.799
- ___46-[HMHomeManager removeHome:completionHandler:]_block_invoke.638
- ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.707
- ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.764
- ___51-[HMHomeManager addHomeWithName:completionHandler:]_block_invoke.634
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.620
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.621
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.725
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.729
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.731
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.733
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.734
- ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.856
- ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.704
- ___Block_byref_object_copy_.31289
- ___Block_byref_object_copy_.32926
- ___Block_byref_object_copy_.35103
- ___Block_byref_object_copy_.40423
- ___Block_byref_object_copy_.43894
- ___Block_byref_object_copy_.63712
- ___Block_byref_object_copy_.66074
- ___Block_byref_object_dispose_.31290
- ___Block_byref_object_dispose_.32927
- ___Block_byref_object_dispose_.35104
- ___Block_byref_object_dispose_.40424
- ___Block_byref_object_dispose_.43895
- ___Block_byref_object_dispose_.63713
- ___Block_byref_object_dispose_.66075
- ___CoreAnalyticsLibraryCore_block_invoke.40537
- ___CoreHAPLibraryCore_block_invoke.32826
- ___IDSFoundationLibraryCore_block_invoke.44871
- ___UIKitLibraryCore_block_invoke.45108
- ___block_literal_global.101.40544
- ___block_literal_global.101.42738
- ___block_literal_global.12.51282
- ___block_literal_global.31407
- ___block_literal_global.31746
- ___block_literal_global.32005
- ___block_literal_global.32291
- ___block_literal_global.32371
- ___block_literal_global.33.65411
- ___block_literal_global.33069
- ___block_literal_global.33565
- ___block_literal_global.33837
- ___block_literal_global.34889
- ___block_literal_global.35126
- ___block_literal_global.35428
- ___block_literal_global.36752
- ___block_literal_global.37725
- ___block_literal_global.37959
- ___block_literal_global.38188
- ___block_literal_global.38584
- ___block_literal_global.39334
- ___block_literal_global.40531
- ___block_literal_global.40781
- ___block_literal_global.41120
- ___block_literal_global.41786
- ___block_literal_global.42748
- ___block_literal_global.43012
- ___block_literal_global.43281
- ___block_literal_global.43566
- ___block_literal_global.43786
- ___block_literal_global.44932
- ___block_literal_global.45026
- ___block_literal_global.45733
- ___block_literal_global.45925
- ___block_literal_global.47108
- ___block_literal_global.47550
- ___block_literal_global.47876
- ___block_literal_global.48642
- ___block_literal_global.49299
- ___block_literal_global.49657
- ___block_literal_global.50931
- ___block_literal_global.511
- ___block_literal_global.51294
- ___block_literal_global.51578
- ___block_literal_global.51774
- ___block_literal_global.52004
- ___block_literal_global.52721
- ___block_literal_global.52841
- ___block_literal_global.53596
- ___block_literal_global.53830
- ___block_literal_global.54285
- ___block_literal_global.54546
- ___block_literal_global.55628
- ___block_literal_global.57929
- ___block_literal_global.58.37954
- ___block_literal_global.58793
- ___block_literal_global.60083
- ___block_literal_global.60815
- ___block_literal_global.61370
- ___block_literal_global.61681
- ___block_literal_global.62198
- ___block_literal_global.62375
- ___block_literal_global.62765
- ___block_literal_global.63013
- ___block_literal_global.64814
- ___block_literal_global.65150
- ___block_literal_global.65417
- ___block_literal_global.65775
- ___block_literal_global.66013
- ___block_literal_global.66369
- ___block_literal_global.698
- ___block_literal_global.746
- ___block_literal_global.748
- ___block_literal_global.84.40725
- ___block_literal_global.860
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.40534
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.45103
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.45097
- _audit_stringCoreAnalytics.40540
- _audit_stringCoreHAP.32828
- _audit_stringIDSFoundation.44873
- _audit_stringUIKit.45110
- _getAnalyticsSendEventLazySymbolLoc.ptr.40533
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.45102
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.45096
- _logCategory._hmf_once_t0.32004
- _logCategory._hmf_once_t0.32370
- _logCategory._hmf_once_t0.43565
- _logCategory._hmf_once_t0.45732
- _logCategory._hmf_once_t0.45924
- _logCategory._hmf_once_t0.63012
- _logCategory._hmf_once_t1.40757
- _logCategory._hmf_once_t1.47107
- _logCategory._hmf_once_t1.51281
- _logCategory._hmf_once_t1.52840
- _logCategory._hmf_once_t1.57928
- _logCategory._hmf_once_t13.42737
- _logCategory._hmf_once_t14.62764
- _logCategory._hmf_once_t16.31406
- _logCategory._hmf_once_t16.37958
- _logCategory._hmf_once_t16.64813
- _logCategory._hmf_once_t2.33564
- _logCategory._hmf_once_t21.62374
- _logCategory._hmf_once_t24.41119
- _logCategory._hmf_once_t24.41785
- _logCategory._hmf_once_t25.65774
- _logCategory._hmf_once_t27.61680
- _logCategory._hmf_once_t3.43011
- _logCategory._hmf_once_t3.53819
- _logCategory._hmf_once_t3.65410
- _logCategory._hmf_once_t31.54284
- _logCategory._hmf_once_t31.66368
- _logCategory._hmf_once_t32.53595
- _logCategory._hmf_once_t365
- _logCategory._hmf_once_t37.54572
- _logCategory._hmf_once_t44.32290
- _logCategory._hmf_once_t51.43280
- _logCategory._hmf_once_t6.34888
- _logCategory._hmf_once_t6.37724
- _logCategory._hmf_once_t6.43785
- _logCategory._hmf_once_t6.49298
- _logCategory._hmf_once_t6.58792
- _logCategory._hmf_once_t7.52720
- _logCategory._hmf_once_t8.38187
- _logCategory._hmf_once_t8.48641
- _logCategory._hmf_once_t8.51792
- _logCategory._hmf_once_v1.32006
- _logCategory._hmf_once_v1.32372
- _logCategory._hmf_once_v1.43567
- _logCategory._hmf_once_v1.45734
- _logCategory._hmf_once_v1.45926
- _logCategory._hmf_once_v1.63014
- _logCategory._hmf_once_v14.42739
- _logCategory._hmf_once_v15.62766
- _logCategory._hmf_once_v17.31408
- _logCategory._hmf_once_v17.37960
- _logCategory._hmf_once_v17.64815
- _logCategory._hmf_once_v2.40758
- _logCategory._hmf_once_v2.47109
- _logCategory._hmf_once_v2.51283
- _logCategory._hmf_once_v2.52842
- _logCategory._hmf_once_v2.57930
- _logCategory._hmf_once_v22.62376
- _logCategory._hmf_once_v25.41121
- _logCategory._hmf_once_v25.41787
- _logCategory._hmf_once_v26.65776
- _logCategory._hmf_once_v28.61682
- _logCategory._hmf_once_v3.33566
- _logCategory._hmf_once_v32.54286
- _logCategory._hmf_once_v32.66370
- _logCategory._hmf_once_v33.53597
- _logCategory._hmf_once_v366
- _logCategory._hmf_once_v38.54573
- _logCategory._hmf_once_v4.43013
- _logCategory._hmf_once_v4.53820
- _logCategory._hmf_once_v4.65412
- _logCategory._hmf_once_v45.32292
- _logCategory._hmf_once_v52.43282
- _logCategory._hmf_once_v7.34890
- _logCategory._hmf_once_v7.37726
- _logCategory._hmf_once_v7.43787
- _logCategory._hmf_once_v7.49300
- _logCategory._hmf_once_v7.58794
- _logCategory._hmf_once_v8.52722
- _logCategory._hmf_once_v9.38189
- _logCategory._hmf_once_v9.48643
- _logCategory._hmf_once_v9.51793
- _objectdestroy.14Tm
- _sharedInstance.onceToken.42747
- _sharedManager.onceToken.61827
- _supportedValueClasses.onceToken.51577
- _supportedValueClasses.onceToken.60045
- _supportedValueClasses.supportedValueClasses.51579
- _supportedValueClasses.supportedValueClasses.60046
CStrings:
+ "%{public}@Updating isAllowedToEnableAdaptiveTemperatureAutomations from %{BOOL}d to %{BOOL}d"
+ "CheckPickerEligibility"
+ "HMHomeManagerDataSyncStateUnsupportedAccount"

```
