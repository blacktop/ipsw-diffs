## iTunesCloud

> `/System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud`

```diff

-4025.100.115.0.0
-  __TEXT.__text: 0x305ccc
+4025.100.124.0.0
+  __TEXT.__text: 0x310a24
   __TEXT.__auth_stubs: 0x14a0
-  __TEXT.__objc_methlist: 0x17654
-  __TEXT.__const: 0x18e4c
+  __TEXT.__objc_methlist: 0x17704
+  __TEXT.__const: 0x18f6c
   __TEXT.__dlopen_cstrs: 0x4cf
-  __TEXT.__gcc_except_tab: 0x34d4
-  __TEXT.__cstring: 0x16ebe
-  __TEXT.__oslogstring: 0x1f63e
+  __TEXT.__gcc_except_tab: 0x349c
+  __TEXT.__cstring: 0x170e5
+  __TEXT.__oslogstring: 0x1fd59
   __TEXT.__ustring: 0x8e
-  __TEXT.__unwind_info: 0x6528
+  __TEXT.__unwind_info: 0x6540
   __TEXT.__eh_frame: 0xb8
-  __TEXT.__objc_classname: 0x3a9e
-  __TEXT.__objc_methname: 0x34f12
-  __TEXT.__objc_methtype: 0x7d5a
-  __TEXT.__objc_stubs: 0x1b020
-  __DATA_CONST.__got: 0xf70
-  __DATA_CONST.__const: 0x71d0
-  __DATA_CONST.__objc_classlist: 0xd40
+  __TEXT.__objc_classname: 0x3ac9
+  __TEXT.__objc_methname: 0x35026
+  __TEXT.__objc_methtype: 0x7d65
+  __TEXT.__objc_stubs: 0x1b0e0
+  __DATA_CONST.__got: 0xf78
+  __DATA_CONST.__const: 0x7208
+  __DATA_CONST.__objc_classlist: 0xd50
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9fe0
+  __DATA_CONST.__objc_selrefs: 0xa008
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0xb70
+  __DATA_CONST.__objc_superrefs: 0xb80
   __DATA_CONST.__objc_arraydata: 0x468
   __AUTH_CONST.__auth_got: 0xa60
-  __AUTH_CONST.__const: 0x11818
-  __AUTH_CONST.__cfstring: 0x18320
-  __AUTH_CONST.__objc_const: 0x2f358
+  __AUTH_CONST.__const: 0x12938
+  __AUTH_CONST.__cfstring: 0x18340
+  __AUTH_CONST.__objc_const: 0x2f538
   __AUTH_CONST.__objc_intobj: 0x420
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH.__objc_data: 0x4b00
-  __DATA.__objc_ivar: 0x22f0
-  __DATA.__data: 0x2670
-  __DATA.__bss: 0x360
-  __DATA.__common: 0xa40
+  __AUTH.__objc_data: 0x4ba0
+  __DATA.__objc_ivar: 0x22fc
+  __DATA.__data: 0x2620
+  __DATA.__bss: 0x370
+  __DATA.__common: 0xa90
   __DATA_DIRTY.__objc_data: 0x3980
   __DATA_DIRTY.__data: 0xa0
   __DATA_DIRTY.__bss: 0x450

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 296C8DEC-49F8-3EA2-A983-D52811069E85
-  Functions: 9710
-  Symbols:   30837
-  CStrings:  17588
+  UUID: CC8B6AA3-8E09-3B84-9F96-F39F302C9BEC
+  Functions: 9723
+  Symbols:   30891
+  CStrings:  17618
 
Symbols:
+ +[ICCertificateCache shared]
+ -[ICCertificateCache .cxx_destruct]
+ -[ICCertificateCache enqueueCertificateRequest:isSAP:withCompletionHandler:]
+ -[ICCertificateCache getDataForCertificateRequest:isSAP:withCompletionHandler:]
+ -[ICCertificateCache getDataForCertificateRequest:withCompletionHandler:]
+ -[ICCertificateCache getDataForSAPCertificateRequest:withCompletionHandler:]
+ -[ICCertificateCache init]
+ -[ICCertificateCacheEntry .cxx_destruct]
+ -[ICCertificateCacheEntry data]
+ -[ICCertificateCacheEntry expirationDate]
+ -[ICCertificateCacheEntry initWithData:expirationDate:]
+ -[ICCertificateCacheEntry isExpired]
+ GCC_except_table6568
+ GCC_except_table6575
+ GCC_except_table6747
+ GCC_except_table6751
+ GCC_except_table6780
+ GCC_except_table6826
+ GCC_except_table7008
+ GCC_except_table7141
+ GCC_except_table7284
+ GCC_except_table7297
+ GCC_except_table7320
+ GCC_except_table7331
+ GCC_except_table7376
+ GCC_except_table7377
+ GCC_except_table7421
+ GCC_except_table7439
+ GCC_except_table7491
+ GCC_except_table7494
+ GCC_except_table7503
+ GCC_except_table7510
+ GCC_except_table7557
+ GCC_except_table7576
+ GCC_except_table7609
+ GCC_except_table7667
+ GCC_except_table7668
+ GCC_except_table7681
+ GCC_except_table8098
+ GCC_except_table8102
+ GCC_except_table8106
+ GCC_except_table8128
+ GCC_except_table8132
+ GCC_except_table8143
+ GCC_except_table8148
+ GCC_except_table8183
+ GCC_except_table8186
+ GCC_except_table8253
+ GCC_except_table8298
+ GCC_except_table8347
+ GCC_except_table8375
+ GCC_except_table8380
+ GCC_except_table8416
+ GCC_except_table8559
+ GCC_except_table8567
+ GCC_except_table8572
+ GCC_except_table8587
+ GCC_except_table8595
+ GCC_except_table8639
+ GCC_except_table8672
+ GCC_except_table8787
+ GCC_except_table8791
+ GCC_except_table8793
+ GCC_except_table8833
+ GCC_except_table8840
+ GCC_except_table8843
+ GCC_except_table9052
+ GCC_except_table9056
+ GCC_except_table9096
+ GCC_except_table9193
+ GCC_except_table9198
+ _MSVFastHexStringFromBytes.hexCharacters.41875
+ _MusicLibraryLibraryCore.frameworkLibrary.22208
+ _MusicLibraryLibraryCore.frameworkLibrary.31674
+ _OBJC_CLASS_$_ICCertificateCache
+ _OBJC_CLASS_$_ICCertificateCacheEntry
+ _OBJC_CLASS_$_NSCache
+ _OBJC_IVAR_$_ICCertificateCache._cache
+ _OBJC_IVAR_$_ICCertificateCacheEntry._data
+ _OBJC_IVAR_$_ICCertificateCacheEntry._expirationDate
+ _OBJC_METACLASS_$_ICCertificateCache
+ _OBJC_METACLASS_$_ICCertificateCacheEntry
+ __MSV_XXH_XXH32_update.11826
+ __MSV_XXH_XXH32_update.17689
+ __MSV_XXH_XXH32_update.17806
+ __MSV_XXH_XXH32_update.20629
+ __MSV_XXH_XXH32_update.31612
+ __MSV_XXH_XXH32_update.41865
+ __MSV_XXH_XXH64_digest.17813
+ __MSV_XXH_XXH64_digest.31617
+ __MSV_XXH_XXH64_update.11827
+ __MSV_XXH_XXH64_update.17690
+ __MSV_XXH_XXH64_update.17807
+ __MSV_XXH_XXH64_update.20630
+ __MSV_XXH_XXH64_update.31613
+ __MSV_XXH_XXH64_update.41866
+ __OBJC_$_CLASS_METHODS_ICCertificateCache
+ __OBJC_$_CLASS_PROP_LIST_ICCertificateCache
+ __OBJC_$_INSTANCE_METHODS_ICCertificateCache
+ __OBJC_$_INSTANCE_METHODS_ICCertificateCacheEntry
+ __OBJC_$_INSTANCE_VARIABLES_ICCertificateCache
+ __OBJC_$_INSTANCE_VARIABLES_ICCertificateCacheEntry
+ __OBJC_$_PROP_LIST_ICCertificateCacheEntry
+ __OBJC_CLASS_RO_$_ICCertificateCache
+ __OBJC_CLASS_RO_$_ICCertificateCacheEntry
+ __OBJC_METACLASS_RO_$_ICCertificateCache
+ __OBJC_METACLASS_RO_$_ICCertificateCacheEntry
+ ___147-[ICMusicSubscriptionFairPlayController generateSubscriptionBagRequestWithAccountUniqueIdentifier:transactionType:machineIDData:completionHandler:]_block_invoke.22
+ ___155-[ICMusicSubscriptionFairPlayController generateSubscriptionLeaseRequestWithAccountUniqueID:transactionType:certificateData:assetIDData:completionHandler:]_block_invoke.23
+ ___28+[ICCertificateCache shared]_block_invoke
+ ___52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke_2.61
+ ___52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke_3.62
+ ___76-[ICCertificateCache enqueueCertificateRequest:isSAP:withCompletionHandler:]_block_invoke
+ ___77-[ICMusicSubscriptionFairPlayController stopSubscriptionLeaseWithCompletion:]_block_invoke.24
+ ___79-[ICCertificateCache getDataForCertificateRequest:isSAP:withCompletionHandler:]_block_invoke
+ ___82-[ICSecureKeyDeliveryRequestOperation _createServerPlaybackContextWithCompletion:]_block_invoke.116
+ ___Block_byref_object_copy_.10613
+ ___Block_byref_object_copy_.10809
+ ___Block_byref_object_copy_.10937
+ ___Block_byref_object_copy_.12414
+ ___Block_byref_object_copy_.13789
+ ___Block_byref_object_copy_.14337
+ ___Block_byref_object_copy_.14509
+ ___Block_byref_object_copy_.14774
+ ___Block_byref_object_copy_.15190
+ ___Block_byref_object_copy_.16338
+ ___Block_byref_object_copy_.16843
+ ___Block_byref_object_copy_.17070
+ ___Block_byref_object_copy_.17420
+ ___Block_byref_object_copy_.18904
+ ___Block_byref_object_copy_.19258
+ ___Block_byref_object_copy_.19475
+ ___Block_byref_object_copy_.20463
+ ___Block_byref_object_copy_.21373
+ ___Block_byref_object_copy_.22171
+ ___Block_byref_object_copy_.22777
+ ___Block_byref_object_copy_.22886
+ ___Block_byref_object_copy_.25297
+ ___Block_byref_object_copy_.25739
+ ___Block_byref_object_copy_.26334
+ ___Block_byref_object_copy_.26695
+ ___Block_byref_object_copy_.27691
+ ___Block_byref_object_copy_.28647
+ ___Block_byref_object_copy_.29670
+ ___Block_byref_object_copy_.30014
+ ___Block_byref_object_copy_.31047
+ ___Block_byref_object_copy_.31959
+ ___Block_byref_object_copy_.32347
+ ___Block_byref_object_copy_.32533
+ ___Block_byref_object_copy_.32694
+ ___Block_byref_object_copy_.33448
+ ___Block_byref_object_copy_.35582
+ ___Block_byref_object_copy_.35808
+ ___Block_byref_object_copy_.35942
+ ___Block_byref_object_copy_.36878
+ ___Block_byref_object_copy_.37040
+ ___Block_byref_object_copy_.37730
+ ___Block_byref_object_copy_.37999
+ ___Block_byref_object_copy_.38624
+ ___Block_byref_object_copy_.38805
+ ___Block_byref_object_copy_.39121
+ ___Block_byref_object_copy_.39968
+ ___Block_byref_object_copy_.40540
+ ___Block_byref_object_copy_.6792
+ ___Block_byref_object_copy_.6905
+ ___Block_byref_object_copy_.7400
+ ___Block_byref_object_copy_.9670
+ ___Block_byref_object_copy_.9775
+ ___Block_byref_object_dispose_.10614
+ ___Block_byref_object_dispose_.10810
+ ___Block_byref_object_dispose_.10938
+ ___Block_byref_object_dispose_.12415
+ ___Block_byref_object_dispose_.13790
+ ___Block_byref_object_dispose_.14338
+ ___Block_byref_object_dispose_.14510
+ ___Block_byref_object_dispose_.14775
+ ___Block_byref_object_dispose_.15191
+ ___Block_byref_object_dispose_.16339
+ ___Block_byref_object_dispose_.16844
+ ___Block_byref_object_dispose_.17071
+ ___Block_byref_object_dispose_.17421
+ ___Block_byref_object_dispose_.18905
+ ___Block_byref_object_dispose_.19259
+ ___Block_byref_object_dispose_.19476
+ ___Block_byref_object_dispose_.20464
+ ___Block_byref_object_dispose_.21374
+ ___Block_byref_object_dispose_.22172
+ ___Block_byref_object_dispose_.22778
+ ___Block_byref_object_dispose_.22887
+ ___Block_byref_object_dispose_.25298
+ ___Block_byref_object_dispose_.25740
+ ___Block_byref_object_dispose_.26335
+ ___Block_byref_object_dispose_.26696
+ ___Block_byref_object_dispose_.27692
+ ___Block_byref_object_dispose_.28648
+ ___Block_byref_object_dispose_.29671
+ ___Block_byref_object_dispose_.30015
+ ___Block_byref_object_dispose_.31048
+ ___Block_byref_object_dispose_.31960
+ ___Block_byref_object_dispose_.32348
+ ___Block_byref_object_dispose_.32534
+ ___Block_byref_object_dispose_.32695
+ ___Block_byref_object_dispose_.33449
+ ___Block_byref_object_dispose_.35583
+ ___Block_byref_object_dispose_.35809
+ ___Block_byref_object_dispose_.35943
+ ___Block_byref_object_dispose_.36879
+ ___Block_byref_object_dispose_.37041
+ ___Block_byref_object_dispose_.37731
+ ___Block_byref_object_dispose_.38000
+ ___Block_byref_object_dispose_.38625
+ ___Block_byref_object_dispose_.38806
+ ___Block_byref_object_dispose_.39122
+ ___Block_byref_object_dispose_.39969
+ ___Block_byref_object_dispose_.40541
+ ___Block_byref_object_dispose_.6793
+ ___Block_byref_object_dispose_.6906
+ ___Block_byref_object_dispose_.7401
+ ___Block_byref_object_dispose_.9671
+ ___Block_byref_object_dispose_.9776
+ ___MusicLibraryLibraryCore_block_invoke.22209
+ ___MusicLibraryLibraryCore_block_invoke.31675
+ ___block_descriptor_57_e8_32s40s48bs_e35_v24?0"ICURLResponse"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48bs56r_e28_v24?0"NSData"8"NSError"16ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e28_v24?0"NSData"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_literal_global.10.26348
+ ___block_literal_global.10171
+ ___block_literal_global.11563
+ ___block_literal_global.11980
+ ___block_literal_global.12.15227
+ ___block_literal_global.12.25087
+ ___block_literal_global.12.26346
+ ___block_literal_global.12544
+ ___block_literal_global.13.39130
+ ___block_literal_global.13186
+ ___block_literal_global.13228
+ ___block_literal_global.13823
+ ___block_literal_global.14960
+ ___block_literal_global.15243
+ ___block_literal_global.16766
+ ___block_literal_global.170.28953
+ ___block_literal_global.17474
+ ___block_literal_global.17933
+ ___block_literal_global.18.26344
+ ___block_literal_global.18.35641
+ ___block_literal_global.18330
+ ___block_literal_global.18727
+ ___block_literal_global.18956
+ ___block_literal_global.19163
+ ___block_literal_global.20.26342
+ ___block_literal_global.202.25287
+ ___block_literal_global.20352
+ ___block_literal_global.22.26339
+ ___block_literal_global.22008
+ ___block_literal_global.22231
+ ___block_literal_global.22681
+ ___block_literal_global.22790
+ ___block_literal_global.24334
+ ___block_literal_global.24458
+ ___block_literal_global.25086
+ ___block_literal_global.25283
+ ___block_literal_global.25845
+ ___block_literal_global.25997
+ ___block_literal_global.26210
+ ___block_literal_global.26354
+ ___block_literal_global.27726
+ ___block_literal_global.28234
+ ___block_literal_global.29049
+ ___block_literal_global.29389
+ ___block_literal_global.29685
+ ___block_literal_global.29835
+ ___block_literal_global.3.17940
+ ___block_literal_global.30831
+ ___block_literal_global.31379
+ ___block_literal_global.31438
+ ___block_literal_global.31846
+ ___block_literal_global.32426
+ ___block_literal_global.33044
+ ___block_literal_global.33485
+ ___block_literal_global.34711
+ ___block_literal_global.35219
+ ___block_literal_global.35664
+ ___block_literal_global.36820
+ ___block_literal_global.37742
+ ___block_literal_global.38102
+ ___block_literal_global.38200
+ ___block_literal_global.38490
+ ___block_literal_global.38949
+ ___block_literal_global.39140
+ ___block_literal_global.40069
+ ___block_literal_global.40210
+ ___block_literal_global.40357
+ ___block_literal_global.40545
+ ___block_literal_global.41120
+ ___block_literal_global.41361
+ ___block_literal_global.41700
+ ___block_literal_global.53.13778
+ ___block_literal_global.6.26352
+ ___block_literal_global.66.22657
+ ___block_literal_global.68.31336
+ ___block_literal_global.6974
+ ___block_literal_global.7070
+ ___block_literal_global.7287
+ ___block_literal_global.7447
+ ___block_literal_global.7681
+ ___block_literal_global.8.26350
+ ___block_literal_global.82.31503
+ ___block_literal_global.8397
+ ___block_literal_global.8468
+ ___block_literal_global.9377
+ ___getML3MusicLibraryClass_block_invoke.22207
+ _audit_stringMusicLibrary.22224
+ _audit_stringMusicLibrary.31678
+ _getML3MusicLibraryClass.22205
+ _getML3MusicLibraryClass.softClass.22206
+ _objc_msgSend$enqueueCertificateRequest:isSAP:withCompletionHandler:
+ _objc_msgSend$getDataForCertificateRequest:isSAP:withCompletionHandler:
+ _objc_msgSend$getDataForCertificateRequest:withCompletionHandler:
+ _objc_msgSend$getDataForSAPCertificateRequest:withCompletionHandler:
+ _objc_msgSend$initWithData:expirationDate:
+ _objc_msgSend$shared
+ _shared._sharedInstance
+ _shared.onceToken.38489
+ _sharedCache.sOnceToken.29834
+ _sharedCache.sSharedCache.29836
+ _sharedController.sOnceToken.35663
+ _sharedController.sOnceToken.39139
+ _sharedController.sSharedController.35665
+ _sharedController.sSharedController.39141
+ _sharedManager.sOnceToken.19162
+ _sharedManager.sOnceToken.28233
+ _sharedManager.sSharedManager.19164
+ _sharedManager.sSharedManager.28235
+ _sharedMonitor.sOnceToken.18329
+ _sharedMonitor.sOnceToken.40068
+ _sharedMonitor.sSharedMonitor.18331
+ _sharedMonitor.sSharedMonitor.40070
+ _sharedProvider.sOnceToken.40356
+ _sharedProvider.sSharedProvider.40358
- GCC_except_table6369
- GCC_except_table6570
- GCC_except_table6577
- GCC_except_table6749
- GCC_except_table6755
- GCC_except_table6782
- GCC_except_table6828
- GCC_except_table7010
- GCC_except_table7143
- GCC_except_table7286
- GCC_except_table7299
- GCC_except_table7322
- GCC_except_table7333
- GCC_except_table7381
- GCC_except_table7382
- GCC_except_table7423
- GCC_except_table7441
- GCC_except_table7493
- GCC_except_table7496
- GCC_except_table7505
- GCC_except_table7512
- GCC_except_table7559
- GCC_except_table7578
- GCC_except_table7611
- GCC_except_table7669
- GCC_except_table7670
- GCC_except_table7683
- GCC_except_table8100
- GCC_except_table8104
- GCC_except_table8108
- GCC_except_table8130
- GCC_except_table8134
- GCC_except_table8145
- GCC_except_table8150
- GCC_except_table8185
- GCC_except_table8188
- GCC_except_table8255
- GCC_except_table8300
- GCC_except_table8349
- GCC_except_table8377
- GCC_except_table8386
- GCC_except_table8418
- GCC_except_table8561
- GCC_except_table8569
- GCC_except_table8574
- GCC_except_table8589
- GCC_except_table8597
- GCC_except_table8641
- GCC_except_table8674
- GCC_except_table8774
- GCC_except_table8778
- GCC_except_table8780
- GCC_except_table8817
- GCC_except_table8820
- GCC_except_table8827
- GCC_except_table9039
- GCC_except_table9043
- GCC_except_table9083
- GCC_except_table9180
- GCC_except_table9185
- _MSVFastHexStringFromBytes.hexCharacters.41801
- _MusicLibraryLibraryCore.frameworkLibrary.22206
- _MusicLibraryLibraryCore.frameworkLibrary.31673
- __MSV_XXH_XXH32_update.11823
- __MSV_XXH_XXH32_update.17687
- __MSV_XXH_XXH32_update.17804
- __MSV_XXH_XXH32_update.20627
- __MSV_XXH_XXH32_update.31611
- __MSV_XXH_XXH32_update.41791
- __MSV_XXH_XXH64_digest.17811
- __MSV_XXH_XXH64_digest.31616
- __MSV_XXH_XXH64_update.11824
- __MSV_XXH_XXH64_update.17688
- __MSV_XXH_XXH64_update.17805
- __MSV_XXH_XXH64_update.20628
- __MSV_XXH_XXH64_update.31612
- __MSV_XXH_XXH64_update.41792
- ___147-[ICMusicSubscriptionFairPlayController generateSubscriptionBagRequestWithAccountUniqueIdentifier:transactionType:machineIDData:completionHandler:]_block_invoke_2
- ___155-[ICMusicSubscriptionFairPlayController generateSubscriptionLeaseRequestWithAccountUniqueID:transactionType:certificateData:assetIDData:completionHandler:]_block_invoke_2
- ___52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke_2.60
- ___52-[ICMusicSubscriptionPlaybackRequestOperation start]_block_invoke_3.61
- ___77-[ICMusicSubscriptionFairPlayController stopSubscriptionLeaseWithCompletion:]_block_invoke_2
- ___82-[ICSecureKeyDeliveryRequestOperation _createServerPlaybackContextWithCompletion:]_block_invoke.118
- ___Block_byref_object_copy_.10610
- ___Block_byref_object_copy_.10806
- ___Block_byref_object_copy_.10934
- ___Block_byref_object_copy_.12411
- ___Block_byref_object_copy_.13787
- ___Block_byref_object_copy_.14335
- ___Block_byref_object_copy_.14507
- ___Block_byref_object_copy_.14772
- ___Block_byref_object_copy_.15188
- ___Block_byref_object_copy_.16336
- ___Block_byref_object_copy_.16841
- ___Block_byref_object_copy_.17068
- ___Block_byref_object_copy_.17418
- ___Block_byref_object_copy_.18902
- ___Block_byref_object_copy_.19256
- ___Block_byref_object_copy_.19473
- ___Block_byref_object_copy_.20461
- ___Block_byref_object_copy_.21371
- ___Block_byref_object_copy_.22169
- ___Block_byref_object_copy_.22775
- ___Block_byref_object_copy_.22884
- ___Block_byref_object_copy_.25293
- ___Block_byref_object_copy_.25735
- ___Block_byref_object_copy_.26330
- ___Block_byref_object_copy_.26691
- ___Block_byref_object_copy_.26733
- ___Block_byref_object_copy_.27690
- ___Block_byref_object_copy_.28646
- ___Block_byref_object_copy_.29669
- ___Block_byref_object_copy_.30013
- ___Block_byref_object_copy_.31046
- ___Block_byref_object_copy_.31958
- ___Block_byref_object_copy_.32346
- ___Block_byref_object_copy_.32532
- ___Block_byref_object_copy_.32693
- ___Block_byref_object_copy_.33447
- ___Block_byref_object_copy_.35581
- ___Block_byref_object_copy_.35807
- ___Block_byref_object_copy_.35941
- ___Block_byref_object_copy_.36877
- ___Block_byref_object_copy_.37039
- ___Block_byref_object_copy_.37729
- ___Block_byref_object_copy_.37998
- ___Block_byref_object_copy_.38558
- ___Block_byref_object_copy_.38739
- ___Block_byref_object_copy_.39044
- ___Block_byref_object_copy_.39894
- ___Block_byref_object_copy_.40466
- ___Block_byref_object_copy_.6789
- ___Block_byref_object_copy_.6902
- ___Block_byref_object_copy_.7397
- ___Block_byref_object_copy_.9667
- ___Block_byref_object_copy_.9772
- ___Block_byref_object_dispose_.10611
- ___Block_byref_object_dispose_.10807
- ___Block_byref_object_dispose_.10935
- ___Block_byref_object_dispose_.12412
- ___Block_byref_object_dispose_.13788
- ___Block_byref_object_dispose_.14336
- ___Block_byref_object_dispose_.14508
- ___Block_byref_object_dispose_.14773
- ___Block_byref_object_dispose_.15189
- ___Block_byref_object_dispose_.16337
- ___Block_byref_object_dispose_.16842
- ___Block_byref_object_dispose_.17069
- ___Block_byref_object_dispose_.17419
- ___Block_byref_object_dispose_.18903
- ___Block_byref_object_dispose_.19257
- ___Block_byref_object_dispose_.19474
- ___Block_byref_object_dispose_.20462
- ___Block_byref_object_dispose_.21372
- ___Block_byref_object_dispose_.22170
- ___Block_byref_object_dispose_.22776
- ___Block_byref_object_dispose_.22885
- ___Block_byref_object_dispose_.25294
- ___Block_byref_object_dispose_.25736
- ___Block_byref_object_dispose_.26331
- ___Block_byref_object_dispose_.26692
- ___Block_byref_object_dispose_.26734
- ___Block_byref_object_dispose_.27691
- ___Block_byref_object_dispose_.28647
- ___Block_byref_object_dispose_.29670
- ___Block_byref_object_dispose_.30014
- ___Block_byref_object_dispose_.31047
- ___Block_byref_object_dispose_.31959
- ___Block_byref_object_dispose_.32347
- ___Block_byref_object_dispose_.32533
- ___Block_byref_object_dispose_.32694
- ___Block_byref_object_dispose_.33448
- ___Block_byref_object_dispose_.35582
- ___Block_byref_object_dispose_.35808
- ___Block_byref_object_dispose_.35942
- ___Block_byref_object_dispose_.36878
- ___Block_byref_object_dispose_.37040
- ___Block_byref_object_dispose_.37730
- ___Block_byref_object_dispose_.37999
- ___Block_byref_object_dispose_.38559
- ___Block_byref_object_dispose_.38740
- ___Block_byref_object_dispose_.39045
- ___Block_byref_object_dispose_.39895
- ___Block_byref_object_dispose_.40467
- ___Block_byref_object_dispose_.6790
- ___Block_byref_object_dispose_.6903
- ___Block_byref_object_dispose_.7398
- ___Block_byref_object_dispose_.9668
- ___Block_byref_object_dispose_.9773
- ___MusicLibraryLibraryCore_block_invoke.22207
- ___MusicLibraryLibraryCore_block_invoke.31674
- ___block_descriptor_64_e8_32s40bs48bs56r_e35_v24?0"ICURLResponse"8"NSError"16ls32l8r56l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e35_v24?0"ICURLResponse"8"NSError"16ls32l8s40l8s48l8s56l8r64l8
- ___block_literal_global.10.26344
- ___block_literal_global.10168
- ___block_literal_global.11560
- ___block_literal_global.11977
- ___block_literal_global.12.15225
- ___block_literal_global.12.25083
- ___block_literal_global.12.26342
- ___block_literal_global.12541
- ___block_literal_global.13.39053
- ___block_literal_global.13184
- ___block_literal_global.13226
- ___block_literal_global.13821
- ___block_literal_global.14958
- ___block_literal_global.15241
- ___block_literal_global.16764
- ___block_literal_global.170.28952
- ___block_literal_global.17472
- ___block_literal_global.17931
- ___block_literal_global.18.26340
- ___block_literal_global.18.35640
- ___block_literal_global.18328
- ___block_literal_global.18725
- ___block_literal_global.18954
- ___block_literal_global.19161
- ___block_literal_global.20.26338
- ___block_literal_global.202.25283
- ___block_literal_global.20350
- ___block_literal_global.22.26335
- ___block_literal_global.22006
- ___block_literal_global.22229
- ___block_literal_global.22679
- ___block_literal_global.22788
- ___block_literal_global.24330
- ___block_literal_global.24454
- ___block_literal_global.25082
- ___block_literal_global.25279
- ___block_literal_global.25841
- ___block_literal_global.25993
- ___block_literal_global.26206
- ___block_literal_global.26350
- ___block_literal_global.27725
- ___block_literal_global.28233
- ___block_literal_global.29048
- ___block_literal_global.29388
- ___block_literal_global.29684
- ___block_literal_global.29834
- ___block_literal_global.3.17938
- ___block_literal_global.30830
- ___block_literal_global.31378
- ___block_literal_global.31437
- ___block_literal_global.31845
- ___block_literal_global.32425
- ___block_literal_global.33043
- ___block_literal_global.33484
- ___block_literal_global.34710
- ___block_literal_global.35218
- ___block_literal_global.35663
- ___block_literal_global.36819
- ___block_literal_global.37741
- ___block_literal_global.38101
- ___block_literal_global.38199
- ___block_literal_global.38883
- ___block_literal_global.39063
- ___block_literal_global.39995
- ___block_literal_global.40136
- ___block_literal_global.40283
- ___block_literal_global.40471
- ___block_literal_global.41046
- ___block_literal_global.41287
- ___block_literal_global.41626
- ___block_literal_global.53.13776
- ___block_literal_global.6.26348
- ___block_literal_global.66.22655
- ___block_literal_global.68.31335
- ___block_literal_global.6971
- ___block_literal_global.7067
- ___block_literal_global.7284
- ___block_literal_global.7444
- ___block_literal_global.7678
- ___block_literal_global.8.26346
- ___block_literal_global.82.31502
- ___block_literal_global.8394
- ___block_literal_global.8465
- ___block_literal_global.9374
- ___getML3MusicLibraryClass_block_invoke.22205
- _audit_stringMusicLibrary.22222
- _audit_stringMusicLibrary.31677
- _getML3MusicLibraryClass.22203
- _getML3MusicLibraryClass.softClass.22204
- _sharedCache.sOnceToken.29833
- _sharedCache.sSharedCache.29835
- _sharedController.sOnceToken.35662
- _sharedController.sOnceToken.39062
- _sharedController.sSharedController.35664
- _sharedController.sSharedController.39064
- _sharedManager.sOnceToken.19160
- _sharedManager.sOnceToken.28232
- _sharedManager.sSharedManager.19162
- _sharedManager.sSharedManager.28234
- _sharedMonitor.sOnceToken.18327
- _sharedMonitor.sOnceToken.39994
- _sharedMonitor.sSharedMonitor.18329
- _sharedMonitor.sSharedMonitor.39996
- _sharedProvider.sOnceToken.40282
- _sharedProvider.sSharedProvider.40284
CStrings:
+ "%s - FairPlayGetSubscriptionStatus() - error=%{public}@"
+ "%s - FairPlayGetSubscriptionStatus() could not get fairplay context for identifier - error=%{public}@"
+ "%s - generateSubscriptionBagRequestWithAccountUniqueIdentifier:transactionType:machineIDData: could not get context for identifier - error=%{public}@"
+ "%s - generateSubscriptionBagRequestWithAccountUniqueIdentifier:transactionType:machineIDData: generating subscription request failed with error=%{public}@"
+ "%s - generateSubscriptionLeaseRequestWithAccountUniqueID:transactionType:certificateData:assetIDData could not get context for identifier - error=%{public}@"
+ "%s - generateSubscriptionLeaseRequestWithAccountUniqueID:transactionType:certificateData:assetIDData generating lease request failed with error=%{public}@"
+ "%s - stopSubscriptionLeaseWithCompletion: could not get context for identifier - error=%{public}@"
+ "%s - stopSubscriptionLeaseWithCompletion: stopping lease request failed with error=%{public}@"
+ "-[ICMusicSubscriptionFairPlayController generateSubscriptionBagRequestWithAccountUniqueIdentifier:transactionType:machineIDData:completionHandler:]_block_invoke"
+ "-[ICMusicSubscriptionFairPlayController generateSubscriptionLeaseRequestWithAccountUniqueID:transactionType:certificateData:assetIDData:completionHandler:]_block_invoke"
+ "-[ICMusicSubscriptionFairPlayController importSubscriptionKeyBagData:completionHandler:]_block_invoke"
+ "-[ICMusicSubscriptionFairPlayController stopSubscriptionLeaseWithCompletion:]_block_invoke"
+ "@\"NSCache\""
+ "ICCertificateCache"
+ "ICCertificateCacheEntry"
+ "T@\"ICCertificateCache\",R,N"
+ "UnknownServerDialogResponse"
+ "[%{public}@]: Failed to fetch certificate data for URL: %{public}@, error: %{public}@"
+ "[%{public}@]: Failed to fetch certificate data for URL: %{public}@, error: %{public}@, response: %{public}@"
+ "[%{public}@]: Returning cached certificate data for URL: %{public}@, expiration: %{public}@"
+ "[%{public}@]: Updated cached certificate data for URL: %{public}@, length: %ld, expiration: %{public}@"
+ "[Lease] %s - importSubscriptionKeyBagData:completionHandler: could not get fairplay context for identifier - error=%{public}@"
+ "[Lease] %s - importSubscriptionKeyBagData:completionHandler: could not import subscription bag - error=%{public}@"
+ "[Lease] %s - importSubscriptionKeyBagData:leaseInfoData:completionHandler: could not get fairplay context for identifier - error=%{public}@"
+ "[Lease] %s - importSubscriptionKeyBagData:leaseInfoData:completionHandler: could not import subscription bag - error=%{public}@"
+ "enqueueCertificateRequest:isSAP:withCompletionHandler:"
+ "getDataForCertificateRequest:isSAP:withCompletionHandler:"
+ "getDataForCertificateRequest:withCompletionHandler:"
+ "getDataForSAPCertificateRequest:withCompletionHandler:"
+ "initWithData:expirationDate:"
- "%s - FairPlayGetSubscriptionStatus() - Error"

```
