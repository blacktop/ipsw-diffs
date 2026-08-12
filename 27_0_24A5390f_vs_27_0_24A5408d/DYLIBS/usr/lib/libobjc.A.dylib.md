## libobjc.A.dylib

> `/usr/lib/libobjc.A.dylib`

```diff

-971.0.0.0.0
-  __TEXT.__text: 0x3c8a0
+973.1.0.0.0
+  __TEXT.__text: 0x3c900
   __TEXT.__lazy_helpers: 0xa8
   __TEXT.__objc_methlist: 0x5ec
   __TEXT.__const: 0x4130
Functions:
~ _objc_retainAutoreleasedReturnValue : 160 -> 168
~ __objc_rootAllocWithZone : 324 -> 332
~ _object_setClass : 676 -> 668
~ -[NSObject init] : 4 -> 12
~ __ZN19AutoreleasePoolPage12releaseUntilEPP11objc_object : 312 -> 304
~ _class_createInstance : 324 -> 332
~ _objc_autoreleaseReturnValue : 336 -> 344
~ -[NSObject dealloc] : 4 -> 12
~ __ZNK8method_t3impEb : 312 -> 320
~ __ZL11fetch_cacheb : 272 -> 280
~ _objc_loadWeakRetained : 676 -> 684
~ __objc_rootDealloc : 96 -> 104
~ _objc_alloc_init : 92 -> 84
~ _weak_register_no_lock : 404 -> 396
~ _objc_storeWeak : 588 -> 596
~ __ZN12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEE8lockWithERS3_ : 208 -> 216
~ __ZL23callSetWeaklyReferencedP11objc_object : 324 -> 332
~ __ZN12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEE10unlockWithERS3_ : 140 -> 148
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPK8method_tPvNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S5_EEEES4_S5_S7_S9_SC_E15LookupBucketForIS4_EEbRKT_RPKSC_ : 260 -> 252
~ -[NSObject mutableCopy] : 28 -> 20
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12iteratorImplILb0EEC2ENS2_12ListIteratorES5_ : 388 -> 396
~ -[NSObject copy] : 28 -> 20
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12ListIteratorC2ERKS3_ : 96 -> 104
~ _objc_setProperty_nonatomic_copy : 128 -> 136
~ __ZNK10class_rw_t2roEv : 144 -> 152
~ -[NSObject autorelease] : 16 -> 8
~ -[NSObject isProxy] : 20 -> 12
~ +[NSObject allocWithZone:] : 16 -> 8
~ _lookUpImpOrNilTryCache : 272 -> 264
~ +[NSObject resolveInstanceMethod:] : 8 -> 16
~ _objc_copyWeak : 76 -> 84
~ __ZL15append_referrerP12weak_entry_tPP11objc_object : 392 -> 400
~ _objc_destroyWeak : 276 -> 284
~ _weak_clear_no_lock : 400 -> 408
~ -[NSObject hash] : 8 -> 16
~ __ZN11objc_object16rootAutorelease2Ev : 136 -> 144
~ _object_cxxConstructFromClass : 372 -> 364
~ _objc_getProperty : 220 -> 228
~ _look_up_class : 476 -> 468
~ _objc_lookUpClass : 16 -> 24
~ __ZL19namedClassTableHashPKc : 148 -> 156
~ +[NSObject isSubclassOfClass:] : 104 -> 96
~ __ZL10remapClassP10objc_class : 244 -> 236
~ __ZL18__sel_registerNamePKcbb : 372 -> 380
~ _class_respondsToSelector : 20 -> 12
~ _objc_setAssociatedObject : 1680 -> 1688
~ _objc_opt_new : 112 -> 120
~ +[NSObject class] : 4 -> 12
~ _objc_opt_class : 204 -> 212
~ _objc_setProperty_atomic_copy : 216 -> 224
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_E20InsertIntoBucketImplIS5_EEPSC_RKS5_RKT_SG_ : 200 -> 208
~ __ZNK11objc_object14sidetable_lockEv : 64 -> 72
~ -[NSObject methodForSelector:] : 80 -> 88
~ +[NSObject instanceMethodForSelector:] : 60 -> 68
~ _objc_storeWeakOrNil : 592 -> 600
~ +[NSObject instancesRespondToSelector:] : 20 -> 28
~ __method_getImplementationAndName : 244 -> 252
~ +[NSObject isEqual:] : 16 -> 24
~ __ZL18search_method_listPK13method_list_tP13objc_selector : 1548 -> 1540
~ __ZN19AutoreleasePoolPage19autoreleaseFullPageEP11objc_objectPS_ : 212 -> 204
~ _class_copyProtocolList : 1144 -> 1136
~ _objc_setProperty_atomic : 264 -> 256
~ _objc_opt_isKindOfClass : 296 -> 288
~ _objc_setProperty_nonatomic : 140 -> 148
~ __ZN7cache_t13collectNolockEb : 488 -> 496
~ +[NSObject isMemberOfClass:] : 28 -> 20
~ __ZL32getExtendedTypesIndexesForMethodP10protocol_tPK8method_tbbRjS4_ : 172 -> 164
~ _sel_isEqual : 24 -> 16
~ _method_getNumberOfArguments : 196 -> 188
~ __ZL11static_initv : 228 -> 236
~ _map_images : 324 -> 316
~ _map_images_nolock : 8352 -> 8360
~ __ZNK11header_info9classlistEPm : 152 -> 144
~ __ZL24hasSignedClassROPointersPK14mach_header_64P29_dyld_section_location_info_s : 88 -> 96
~ __ZNK11header_info9nlclslistEPm : 144 -> 152
~ __ZL20classSlotForTagIndex16objc_tag_index_t : 116 -> 108
~ _objc_opt_self : 48 -> 40
~ __ZL11weak_resizeP12weak_table_tm : 196 -> 204
~ _CALLING_SOME_+initialize_METHOD : 44 -> 36
~ +[NSObject initialize] : 8 -> 16
~ __ZN7cache_t26maybeConvertToPreoptimizedEv : 372 -> 364
~ __ZN23tls_autoptr_direct_implI18_objc_pthread_dataL7tls_key0EE5dtor_EPv : 160 -> 152
~ _method_copyReturnType : 140 -> 132
~ _sel_lookUpByName : 280 -> 288
~ _class_addProtocol : 360 -> 368
~ __ZL27internal_class_getImageNameP10objc_classPPKc : 48 -> 56
~ ____ZL17addMethods_finishP10objc_classP13method_list_t_block_invoke : 56 -> 48
~ +[NSObject resolveClassMethod:] : 16 -> 8
~ __ZN4objc7Scanner13isSwiftObjectEP10objc_class : 120 -> 128
~ __ZN4objc12DenseMapBaseINS_8DenseMapIPKcNS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_SB_E4findES3_ : 140 -> 132
~ -[NSObject performSelector:withObject:] : 104 -> 96
~ _encoding_getArgumentInfo : 420 -> 412
~ _method_getReturnType : 196 -> 204
~ +[NSObject respondsToSelector:] : 24 -> 16
~ __ZN4objc7Scanner17scanChangedMethodEP10objc_classPK8method_t : 948 -> 940
~ __ZL27_allocateTrampolinesAndDatav : 664 -> 656
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPK8method_tP23objc_method_descriptionNS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S6_EEEES4_S6_S8_SA_SD_E15LookupBucketForIS4_EEbRKT_RPKSD_ : 264 -> 256
~ +[NSObject isKindOfClass:] : 96 -> 104
~ __ZL13addNamedClassP10objc_classPKcS0_ : 600 -> 592
~ _objc_registerClassPair : 712 -> 720
~ _objc_getFutureClass : 616 -> 624
~ _class_setSuperclass : 728 -> 736
~ __ZL14removeSubclassP10objc_classS0_ : 304 -> 312
~ __ZN17loadImageCallbackaSERKS_ : 180 -> 188
~ __ZN4objc8DenseMapI12DisguisedPtrI10objc_classEP17PendingInitializeNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S5_EEE4initEj : 236 -> 228
~ __objc_getClassForTag : 88 -> 80
~ __ZNK4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classES4_NS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S4_EEEES4_S4_S6_S8_SB_E15LookupBucketForIS4_EEbRKT_RPKSB_ : 256 -> 248
~ +[NSObject new] : 92 -> 84
~ __ZL9readClassP10objc_classbb : 1700 -> 1708
~ _objc_readClassPair : 676 -> 668
~ __ZNSt3__118__stable_sort_moveINS_17_ClassicAlgPolicyERN8method_t16SortBySELAddressEPNS2_9bigSignedEEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEPNSA_10value_typeE : 1288 -> 1280
~ +[NSObject performSelector:] : 84 -> 92
~ ____ZZL16attachCategoriesP10objc_classPK21locstamped_category_tjS0_iENK3$_0clEPZL16attachCategoriesS0_S3_jS0_iE5Listsb_block_invoke : 56 -> 48
~ +[NSObject release] : 4 -> 12
~ __ZN4objc8DenseMapIPK8method_tP23objc_method_descriptionNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S5_EEE4growEj : 508 -> 500
~ -[Protocol isEqual:] : 200 -> 208
~ __ZN10objc_class37installMangledNameForLazilyNamedClassEv : 444 -> 436
~ __ZL25pageAndIndexContainingIMPPFvvEPm : 312 -> 304
~ _protocol_copyPropertyList : 12 -> 20
~ _object_dispose : 80 -> 72
~ __ZL23fixupProtocolMethodListP10protocol_tP13method_list_tbbbPPP13objc_selector : 656 -> 664
~ +[NSObject performSelector:withObject:] : 96 -> 104
~ _protocol_copyProtocolList : 416 -> 424
~ -[Protocol hash] : 20 -> 12
~ __ZN19AutoreleasePoolPage12popPageDebugEPvPS_PP11objc_object : 268 -> 276
~ _objc_copyCppObjectAtomic : 156 -> 148
~ __objc_deallocOnMainThreadHelper : 12 -> 20
~ _objc_removeAssociatedObjects : 44 -> 36
~ _NXMapKeyCopyingInsert : 268 -> 260
~ __headerForAddress : 180 -> 188
~ __ZL11_mapPtrHashP11_NXMapTablePKv : 16 -> 8
~ __ZN4objc8DenseMapI12DisguisedPtrI11objc_objectENS_13SmallDenseMapIPKvNS_15ObjcAssociationELj1ENS_17DenseMapValueInfoIS7_EENS_12DenseMapInfoIS6_EENS_6detail12DenseMapPairIS6_S7_EEEENS8_ISF_EENSA_IS3_EENSD_IS3_SF_EEE4growEj : 600 -> 592
~ _property_getAttributes : 20 -> 12
~ __ZNK19AutoreleasePoolPage10busted_dieEv : 44 -> 36
~ __ZL30objc_duplicateClassImpl_nolockP10objc_classPKcm : 1632 -> 1656
~ __objc_getFreedObjectClass : 12 -> 20
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classES4_NS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S4_EEEES4_S4_S6_S8_SB_E5eraseERKS4_ : 260 -> 268
~ ___copy_helper_block_e8_32c43_ZTSKZL13setSuperclassP10objc_classS0_E3$_1 : 16 -> 8
~ __ZN4objc8DenseMapIPKcP8ProtocolNS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS2_EENS_6detail12DenseMapPairIS2_S4_EEE4growEj : 496 -> 504
~ _objc_weak_error : 16 -> 8
~ __ZL13weakTableScanv : 356 -> 364
~ _objc_autoreleaseNoPool : 16 -> 8
~ _objc_autoreleasePoolInvalid : 12 -> 4
~ __ZNK11objc_object21sidetable_retainCountEv : 232 -> 224
~ -[__NSUnrecognizedTaggedPointer autorelease] : 4 -> 12
~ +[NSObject forwardInvocation:] : 88 -> 96
~ -[NSObject forwardInvocation:] : 96 -> 88
~ +[NSObject description] : 8 -> 16
~ -[NSObject description] : 12 -> 20
~ __ZNK19AutoreleasePoolPage6bustedIPFvPKczEEEvT_ : 148 -> 140
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPK8method_tP23objc_method_descriptionNS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S6_EEEES4_S6_S8_SA_SD_E22FatalCorruptHashTablesEPKSD_j : 96 -> 88
~ __ZL22defaultBadAllocHandlerP10objc_class : 36 -> 44
~ __ZL18startWeakTableScanv : 132 -> 124
~ +[NSObject doesNotRecognizeSelector:] : 80 -> 72
~ -[NSObject doesNotRecognizeSelector:] : 80 -> 72
~ +[NSObject methodSignatureForSelector:] : 24 -> 32
```
