## MediaServices

> `/System/Library/PrivateFrameworks/MediaServices.framework/MediaServices`

```diff

-4023.400.1.0.0
-  __TEXT.__text: 0x506c4
-  __TEXT.__auth_stubs: 0x1bf0
-  __TEXT.__objc_methlist: 0x4924
+4023.510.1.0.0
+  __TEXT.__text: 0x51b78
+  __TEXT.__auth_stubs: 0x1be0
+  __TEXT.__objc_methlist: 0x4a84
   __TEXT.__const: 0x288
-  __TEXT.__gcc_except_tab: 0xbf8
-  __TEXT.__cstring: 0x581b
-  __TEXT.__oslogstring: 0x27c1
+  __TEXT.__gcc_except_tab: 0xc44
+  __TEXT.__cstring: 0x58e5
+  __TEXT.__oslogstring: 0x2a00
   __TEXT.__dlopen_cstrs: 0x11d
   __TEXT.__ustring: 0x18
-  __TEXT.__unwind_info: 0x1518
-  __TEXT.__objc_classname: 0xa20
-  __TEXT.__objc_methname: 0xad9f
-  __TEXT.__objc_methtype: 0x1a20
-  __TEXT.__objc_stubs: 0x7520
+  __TEXT.__unwind_info: 0x156c
+  __TEXT.__objc_classname: 0xa74
+  __TEXT.__objc_methname: 0xafcf
+  __TEXT.__objc_methtype: 0x1a3c
+  __TEXT.__objc_stubs: 0x76a0
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x1550
-  __DATA_CONST.__objc_classlist: 0x2d0
+  __DATA_CONST.__const: 0x1578
+  __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6c70
-  __DATA_CONST.__objc_selrefs: 0x2a08
+  __DATA_CONST.__objc_const: 0x6f68
+  __DATA_CONST.__objc_selrefs: 0x2a88
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x3d8
+  __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x120
-  __AUTH_CONST.__cfstring: 0x5460
-  __AUTH_CONST.__objc_const: 0x2878
-  __AUTH_CONST.__const: 0x580
+  __AUTH_CONST.__cfstring: 0x5560
+  __AUTH_CONST.__objc_const: 0x2998
+  __AUTH_CONST.__const: 0x5c0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xe10
-  __AUTH.__objc_data: 0x13b0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x3c8
-  __DATA.__objc_superrefs: 0x228
-  __DATA.__objc_ivar: 0x5e8
-  __DATA.__data: 0x7e8
-  __DATA.__bss: 0xd4
+  __AUTH_CONST.__auth_got: 0xe08
+  __AUTH.__objc_data: 0x14a0
+  __DATA.__objc_ivar: 0x618
+  __DATA.__data: 0x858
+  __DATA.__bss: 0xe4
   __DATA_DIRTY.__objc_data: 0x870
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1937
-  Symbols:   6803
-  CStrings:  3485
+  Functions: 1967
+  Symbols:   6917
+  CStrings:  3535
 
Symbols:
+ +[MSVSonicAssertion hasEntitlement]
+ +[MSVSonicAssertion sharedObserver]
+ +[MSVSonicAssertion shouldAlsoUseOSTransaction]
+ -[MSVLyricsAudioAttributes .cxx_destruct]
+ -[MSVLyricsAudioAttributes isSpatialRole]
+ -[MSVLyricsAudioAttributes lyricsOffset]
+ -[MSVLyricsAudioAttributes role]
+ -[MSVLyricsAudioAttributes setLyricsOffset:]
+ -[MSVLyricsAudioAttributes setRole:]
+ -[MSVLyricsAudioAttributes setSpatialRole:]
+ -[MSVLyricsSongInfo audioAttributes]
+ -[MSVLyricsSongInfo setAudioAttributes:]
+ -[MSVSonicAssertion .cxx_destruct]
+ -[MSVSonicAssertion dealloc]
+ -[MSVSonicAssertion description]
+ -[MSVSonicAssertion handleInvalidation:]
+ -[MSVSonicAssertion initWithName:]
+ -[MSVSonicAssertion invalidate]
+ -[MSVSonicAssertion invalidationHandler]
+ -[MSVSonicAssertion name]
+ -[MSVSonicAssertion setInvalidationHandler:]
+ -[MSVSonicAssertionObserver assertion:didInvalidateWithError:]
+ -[MSVSonicBackgroundTaskProvider .cxx_destruct]
+ -[MSVSonicBackgroundTaskProvider _taskDidTimeout:]
+ -[MSVSonicBackgroundTaskProvider beginTaskWithExpirationHandler:]
+ -[MSVSonicBackgroundTaskProvider beginTaskWithName:expirationHandler:]
+ -[MSVSonicBackgroundTaskProvider endTask:]
+ -[MSVSonicBackgroundTaskProvider initWithInvalidationDuration:]
+ -[NSError(MSVErrorAdditions) msv_firstUnwrappedErrorMatchingDomain:code:]
+ GCC_except_table1007
+ GCC_except_table1011
+ GCC_except_table1015
+ GCC_except_table1102
+ GCC_except_table1142
+ GCC_except_table1148
+ GCC_except_table118
+ GCC_except_table1352
+ GCC_except_table1461
+ GCC_except_table1465
+ GCC_except_table1467
+ GCC_except_table1469
+ GCC_except_table1471
+ GCC_except_table1473
+ GCC_except_table1475
+ GCC_except_table1477
+ GCC_except_table1481
+ GCC_except_table149
+ GCC_except_table1550
+ GCC_except_table1551
+ GCC_except_table1556
+ GCC_except_table1559
+ GCC_except_table1560
+ GCC_except_table1564
+ GCC_except_table1567
+ GCC_except_table1571
+ GCC_except_table1573
+ GCC_except_table1575
+ GCC_except_table1576
+ GCC_except_table1581
+ GCC_except_table160
+ GCC_except_table1674
+ GCC_except_table1750
+ GCC_except_table1754
+ GCC_except_table1756
+ GCC_except_table1791
+ GCC_except_table1827
+ GCC_except_table1832
+ GCC_except_table1848
+ GCC_except_table1849
+ GCC_except_table1850
+ GCC_except_table232
+ GCC_except_table238
+ GCC_except_table246
+ GCC_except_table271
+ GCC_except_table448
+ GCC_except_table457
+ GCC_except_table521
+ GCC_except_table583
+ GCC_except_table585
+ GCC_except_table590
+ GCC_except_table592
+ GCC_except_table599
+ GCC_except_table611
+ GCC_except_table618
+ GCC_except_table648
+ GCC_except_table656
+ GCC_except_table744
+ GCC_except_table764
+ GCC_except_table882
+ GCC_except_table934
+ GCC_except_table937
+ GCC_except_table938
+ GCC_except_table951
+ GCC_except_table958
+ GCC_except_table960
+ _MSVFastHexStringFromBytes.hexCharacters.3488
+ _OBJC_CLASS_$_MSVLyricsAudioAttributes
+ _OBJC_CLASS_$_MSVSonicAssertion
+ _OBJC_CLASS_$_MSVSonicAssertionObserver
+ _OBJC_CLASS_$_MSVSonicBackgroundTaskProvider
+ _OBJC_IVAR_$_MSVLyricsAudioAttributes._lyricsOffset
+ _OBJC_IVAR_$_MSVLyricsAudioAttributes._role
+ _OBJC_IVAR_$_MSVLyricsAudioAttributes._spatialRole
+ _OBJC_IVAR_$_MSVLyricsSongInfo._audioAttributes
+ _OBJC_IVAR_$_MSVSonicAssertion._invalidationHandler
+ _OBJC_IVAR_$_MSVSonicAssertion._name
+ _OBJC_IVAR_$_MSVSonicAssertion._needsInvalidation
+ _OBJC_IVAR_$_MSVSonicBackgroundTaskProvider._assertions
+ _OBJC_IVAR_$_MSVSonicBackgroundTaskProvider._expirationHandlers
+ _OBJC_IVAR_$_MSVSonicBackgroundTaskProvider._invalidationDuration
+ _OBJC_IVAR_$_MSVSonicBackgroundTaskProvider._lastIdentifier
+ _OBJC_IVAR_$_MSVSonicBackgroundTaskProvider._lock
+ _OBJC_IVAR_$_MSVSonicBackgroundTaskProvider._timeoutGuards
+ _OBJC_METACLASS_$_MSVLyricsAudioAttributes
+ _OBJC_METACLASS_$_MSVSonicAssertion
+ _OBJC_METACLASS_$_MSVSonicAssertionObserver
+ _OBJC_METACLASS_$_MSVSonicBackgroundTaskProvider
+ __OBJC_$_CLASS_METHODS_MSVSonicAssertion
+ __OBJC_$_INSTANCE_METHODS_MSVLyricsAudioAttributes
+ __OBJC_$_INSTANCE_METHODS_MSVSonicAssertion
+ __OBJC_$_INSTANCE_METHODS_MSVSonicAssertionObserver
+ __OBJC_$_INSTANCE_METHODS_MSVSonicBackgroundTaskProvider
+ __OBJC_$_INSTANCE_VARIABLES_MSVLyricsAudioAttributes
+ __OBJC_$_INSTANCE_VARIABLES_MSVSonicAssertion
+ __OBJC_$_INSTANCE_VARIABLES_MSVSonicBackgroundTaskProvider
+ __OBJC_$_PROP_LIST_MSVLyricsAudioAttributes
+ __OBJC_$_PROP_LIST_MSVSonicAssertion
+ __OBJC_$_PROP_LIST_MSVSonicAssertionObserver
+ __OBJC_$_PROP_LIST_MSVSonicBackgroundTaskProvider
+ __OBJC_CLASS_PROTOCOLS_$_MSVSonicAssertionObserver
+ __OBJC_CLASS_PROTOCOLS_$_MSVSonicBackgroundTaskProvider
+ __OBJC_CLASS_RO_$_MSVLyricsAudioAttributes
+ __OBJC_CLASS_RO_$_MSVSonicAssertion
+ __OBJC_CLASS_RO_$_MSVSonicAssertionObserver
+ __OBJC_CLASS_RO_$_MSVSonicBackgroundTaskProvider
+ __OBJC_METACLASS_RO_$_MSVLyricsAudioAttributes
+ __OBJC_METACLASS_RO_$_MSVSonicAssertion
+ __OBJC_METACLASS_RO_$_MSVSonicAssertionObserver
+ __OBJC_METACLASS_RO_$_MSVSonicBackgroundTaskProvider
+ __ZNKSt3__16vectorI14sortColorEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI22sortQuantizeColorEntryNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorI7ITColorNS_9allocatorIS1_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_Lb0EEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEb
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_Lb0EEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEb
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorI7ITColorEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__127__insertion_sort_incompleteB8ue170006INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEbT1_S7_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8ue170006INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEbT1_S7_T0_
+ __ZNSt3__17__sort3B8ue170006INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEjT1_S7_S7_T0_
+ __ZNSt3__17__sort3B8ue170006INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEjT1_S7_S7_T0_
+ __ZNSt3__17__sort4B8ue170006INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEvT1_S7_S7_S7_T0_
+ __ZNSt3__17__sort4B8ue170006INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEvT1_S7_S7_S7_T0_
+ __ZNSt3__17__sort5B8ue170006INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEvT1_S7_S7_S7_S7_T0_
+ __ZNSt3__17__sort5B8ue170006INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEvT1_S7_S7_S7_S7_T0_
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___31-[MSVSonicAssertion invalidate]_block_invoke
+ ___35+[MSVSonicAssertion hasEntitlement]_block_invoke
+ ___35+[MSVSonicAssertion sharedObserver]_block_invoke
+ ___47+[MSVSonicAssertion shouldAlsoUseOSTransaction]_block_invoke
+ ___70-[MSVSonicBackgroundTaskProvider beginTaskWithName:expirationHandler:]_block_invoke
+ ___70-[MSVSonicBackgroundTaskProvider beginTaskWithName:expirationHandler:]_block_invoke_2
+ ___Block_byref_object_copy_.1589
+ ___Block_byref_object_copy_.1673
+ ___Block_byref_object_copy_.2099
+ ___Block_byref_object_copy_.2630
+ ___Block_byref_object_copy_.2944
+ ___Block_byref_object_copy_.3437
+ ___Block_byref_object_copy_.3482
+ ___Block_byref_object_copy_.3742
+ ___Block_byref_object_copy_.3898
+ ___Block_byref_object_copy_.4043
+ ___Block_byref_object_copy_.4325
+ ___Block_byref_object_copy_.5064
+ ___Block_byref_object_copy_.5451
+ ___Block_byref_object_copy_.5810
+ ___Block_byref_object_dispose_.1590
+ ___Block_byref_object_dispose_.1674
+ ___Block_byref_object_dispose_.2100
+ ___Block_byref_object_dispose_.2631
+ ___Block_byref_object_dispose_.2945
+ ___Block_byref_object_dispose_.3438
+ ___Block_byref_object_dispose_.3483
+ ___Block_byref_object_dispose_.3743
+ ___Block_byref_object_dispose_.3899
+ ___Block_byref_object_dispose_.4044
+ ___Block_byref_object_dispose_.4326
+ ___Block_byref_object_dispose_.5065
+ ___Block_byref_object_dispose_.5452
+ ___Block_byref_object_dispose_.5811
+ ___assertion.5329
+ ___assertionCount.5324
+ ___assertionInvalidationNonce.5328
+ ___assertionLock.5323
+ ___block_descriptor_48_e8_32w_e27_v16?0"MSVSonicAssertion"8lw32l8
+ ___block_literal_global.1049
+ ___block_literal_global.121
+ ___block_literal_global.123
+ ___block_literal_global.128.4321
+ ___block_literal_global.1442
+ ___block_literal_global.1776
+ ___block_literal_global.1864
+ ___block_literal_global.1993
+ ___block_literal_global.2040
+ ___block_literal_global.2148
+ ___block_literal_global.2493
+ ___block_literal_global.2856
+ ___block_literal_global.2888
+ ___block_literal_global.3009
+ ___block_literal_global.3733
+ ___block_literal_global.3902
+ ___block_literal_global.4281
+ ___block_literal_global.5012
+ ___block_literal_global.5368
+ ___block_literal_global.5458
+ ___block_literal_global.55
+ ___block_literal_global.5733
+ ___block_literal_global.61
+ ___block_literal_global.619
+ ___block_literal_global.834
+ ___transaction
+ __unnamed_array_storage.209
+ __unnamed_array_storage.3162
+ _objc_msgSend$addObserver:
+ _objc_msgSend$addObserver:selector:name:object:
+ _objc_msgSend$hasEntitlement
+ _objc_msgSend$initWithName:
+ _objc_msgSend$invalidationHandler
+ _objc_msgSend$msv_firstUnwrappedErrorMatchingDomain:code:
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$setAudioAttributes:
+ _objc_msgSend$setLyricsOffset:
+ _objc_msgSend$setSpatialRole:
+ _objc_msgSend$sharedObserver
+ _objc_msgSend$shouldAlsoUseOSTransaction
+ _sharedObserver.observer
+ _sharedObserver.onceToken
+ _shouldAlsoUseOSTransaction.onceToken
+ _shouldAlsoUseOSTransaction.useOSTransaction
- -[_MSVSQLSonicAssertion .cxx_destruct]
- -[_MSVSQLSonicAssertion description]
- -[_MSVSQLSonicAssertion invalidate]
- GCC_except_table1084
- GCC_except_table1124
- GCC_except_table1130
- GCC_except_table117
- GCC_except_table129
- GCC_except_table1334
- GCC_except_table1437
- GCC_except_table1441
- GCC_except_table1443
- GCC_except_table1445
- GCC_except_table1447
- GCC_except_table1449
- GCC_except_table1451
- GCC_except_table1453
- GCC_except_table1457
- GCC_except_table1532
- GCC_except_table1533
- GCC_except_table1535
- GCC_except_table1537
- GCC_except_table1538
- GCC_except_table1540
- GCC_except_table1541
- GCC_except_table1542
- GCC_except_table1546
- GCC_except_table1549
- GCC_except_table1557
- GCC_except_table1563
- GCC_except_table159
- GCC_except_table1656
- GCC_except_table170
- GCC_except_table1732
- GCC_except_table1736
- GCC_except_table1738
- GCC_except_table1773
- GCC_except_table1797
- GCC_except_table1802
- GCC_except_table1818
- GCC_except_table1819
- GCC_except_table1820
- GCC_except_table242
- GCC_except_table248
- GCC_except_table256
- GCC_except_table281
- GCC_except_table449
- GCC_except_table458
- GCC_except_table522
- GCC_except_table584
- GCC_except_table586
- GCC_except_table591
- GCC_except_table595
- GCC_except_table601
- GCC_except_table631
- GCC_except_table639
- GCC_except_table726
- GCC_except_table746
- GCC_except_table864
- GCC_except_table916
- GCC_except_table919
- GCC_except_table920
- GCC_except_table924
- GCC_except_table933
- GCC_except_table940
- GCC_except_table971
- GCC_except_table993
- GCC_except_table997
- _MSVFastHexStringFromBytes.hexCharacters.3364
- _OBJC_CLASS_$__MSVSQLSonicAssertion
- _OBJC_IVAR_$__MSVSQLSonicAssertion._name
- _OBJC_METACLASS_$__MSVSQLSonicAssertion
- __OBJC_$_INSTANCE_METHODS__MSVSQLSonicAssertion
- __OBJC_$_INSTANCE_VARIABLES__MSVSQLSonicAssertion
- __OBJC_$_PROP_LIST__MSVSQLSonicAssertion
- __OBJC_CLASS_PROTOCOLS_$__MSVSQLSonicAssertion
- __OBJC_CLASS_RO_$__MSVSQLSonicAssertion
- __OBJC_METACLASS_RO_$__MSVSQLSonicAssertion
- __ZNKSt3__16vectorI14sortColorEntryNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI22sortQuantizeColorEntryNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorI7ITColorNS_9allocatorIS1_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeE
- __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeE
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorI7ITColorEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__127__insertion_sort_incompleteIRPFb14sortColorEntryS1_EPS1_EEbT0_S6_T_
- __ZNSt3__127__insertion_sort_incompleteIRPFb22sortQuantizeColorEntryS1_EPS1_EEbT0_S6_T_
- __ZNSt3__17__sort3B7v160006INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEjT1_S7_S7_T0_
- __ZNSt3__17__sort3B7v160006INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEjT1_S7_S7_T0_
- __ZNSt3__17__sort4B7v160006INS_17_ClassicAlgPolicyERPFb14sortColorEntryS2_EPS2_EEjT1_S7_S7_S7_T0_
- __ZNSt3__17__sort4B7v160006INS_17_ClassicAlgPolicyERPFb22sortQuantizeColorEntryS2_EPS2_EEjT1_S7_S7_S7_T0_
- __ZNSt3__17__sort5IRPFb14sortColorEntryS1_EPS1_EEjT0_S6_S6_S6_S6_T_
- __ZNSt3__17__sort5IRPFb22sortQuantizeColorEntryS1_EPS1_EEjT0_S6_S6_S6_S6_T_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___35-[_MSVSQLSonicAssertion invalidate]_block_invoke
- ___39+[_MSVSQLSonicAssertion hasEntitlement]_block_invoke
- ___Block_byref_object_copy_.1570
- ___Block_byref_object_copy_.1984
- ___Block_byref_object_copy_.2516
- ___Block_byref_object_copy_.2828
- ___Block_byref_object_copy_.3320
- ___Block_byref_object_copy_.3358
- ___Block_byref_object_copy_.3633
- ___Block_byref_object_copy_.3784
- ___Block_byref_object_copy_.3929
- ___Block_byref_object_copy_.4188
- ___Block_byref_object_copy_.4947
- ___Block_byref_object_copy_.5288
- ___Block_byref_object_copy_.5647
- ___Block_byref_object_copy_.596
- ___Block_byref_object_dispose_.1571
- ___Block_byref_object_dispose_.1985
- ___Block_byref_object_dispose_.2517
- ___Block_byref_object_dispose_.2829
- ___Block_byref_object_dispose_.3321
- ___Block_byref_object_dispose_.3359
- ___Block_byref_object_dispose_.3634
- ___Block_byref_object_dispose_.3785
- ___Block_byref_object_dispose_.3930
- ___Block_byref_object_dispose_.4189
- ___Block_byref_object_dispose_.4948
- ___Block_byref_object_dispose_.5289
- ___Block_byref_object_dispose_.5648
- ___Block_byref_object_dispose_.597
- ___assertion.5178
- ___assertionCount.5176
- ___assertionInvalidationNonce.5177
- ___assertionLock.5175
- ___block_literal_global.1064
- ___block_literal_global.120.2054
- ___block_literal_global.122
- ___block_literal_global.128.4185
- ___block_literal_global.1452
- ___block_literal_global.1667
- ___block_literal_global.1756
- ___block_literal_global.1884
- ___block_literal_global.1925
- ___block_literal_global.2033
- ___block_literal_global.2380
- ___block_literal_global.2740
- ___block_literal_global.2772
- ___block_literal_global.2895
- ___block_literal_global.3624
- ___block_literal_global.3788
- ___block_literal_global.4148
- ___block_literal_global.4895
- ___block_literal_global.5241
- ___block_literal_global.5295
- ___block_literal_global.5570
- ___block_literal_global.629
- ___block_literal_global.844
- __unnamed_array_storage.208
- __unnamed_array_storage.3041
- _objc_opt_self
CStrings:
+ "!"
+ "3"
+ "8"
+ "@\"MSVLyricsAudioAttributes\""
+ "MSVLyricsAudioAttributes"
+ "MSVSonicAssertion"
+ "MSVSonicAssertion.m"
+ "MSVSonicAssertionObserver"
+ "MSVSonicAssertionsWereInvalidatedNotification"
+ "MSVSonicBackgroundTaskProvider"
+ "MSVSonicBackgroundTaskProvider %p Task #%ld [%{public}@] ended"
+ "MSVSonicBackgroundTaskProvider %p Task #%ld [%{public}@] expired"
+ "MSVSonicBackgroundTaskProvider %p Task #%ld [%{public}@] failed to start"
+ "MSVSonicBackgroundTaskProvider %p Task #%ld [%{public}@] started"
+ "T@\"MSVLyricsAudioAttributes\",&,N,V_audioAttributes"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_role"
+ "TB,N,GisSpatialRole,V_spatialRole"
+ "Td,N,V_lyricsOffset"
+ "Warning: <audio> element should be inside <iTunesMetadata>"
+ "[MSVSonicAssertion] Acquired RBSAssertion %p"
+ "[MSVSonicAssertion] Created os_transaction %p"
+ "[MSVSonicAssertion] Failed to acquire RBSAssertion %p error=%{public}@"
+ "[MSVSonicAssertion] Invalidating RBSAssertion %p] Timeout"
+ "[MSVSonicAssertion] Invalidating existing RBSAssertion %p"
+ "[MSVSonicAssertion] RBSAssertion %p was invalidated error=%{public}@"
+ "[MSVSonicAssertion] Releasing os_transaction %p"
+ "[MSVSonicAssertion] Releasing os_transaction %p Timeout"
+ "__assertionCount can't be negative"
+ "_assertions"
+ "_audioAttributes"
+ "_lyricsOffset"
+ "_needsInvalidation"
+ "_spatialRole"
+ "addObserver:"
+ "addObserver:selector:name:object:"
+ "audio"
+ "audioAttributes"
+ "com.apple.MediaPlayer.RemotePlayerService"
+ "handleInvalidation:"
+ "hasEntitlement"
+ "initWithInvalidationDuration:"
+ "isSpatialRole"
+ "lyricOffset"
+ "lyricsOffset"
+ "msv_firstUnwrappedErrorMatchingDomain:code:"
+ "postNotificationName:object:"
+ "setAudioAttributes:"
+ "setLyricsOffset:"
+ "setSpatialRole:"
+ "sharedObserver"
+ "shouldAlsoUseOSTransaction"
+ "spatial"
+ "spatialRole"
+ "v16@?0@\"MSVSonicAssertion\"8"
- "[SQL] Acquired RBSAssertion %p"
- "[SQL] Failed to acquire RBSAssertion %p error=%{public}@"
- "[SQL] Invalidating RBSAssertion %p Timeout"
- "[SQL] Invalidating existing RBSAssertion %p"
- "[SQL] Taking RBSAssertion"
- "_MSVSQLSonicAssertion"

```
