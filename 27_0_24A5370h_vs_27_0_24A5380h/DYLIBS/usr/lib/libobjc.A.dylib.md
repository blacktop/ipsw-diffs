## libobjc.A.dylib

> `/usr/lib/libobjc.A.dylib`

```diff

-  __TEXT.__text: 0x3d000
+  __TEXT.__text: 0x3c8a0
   __TEXT.__lazy_helpers: 0xa8
   __TEXT.__objc_methlist: 0x5ec
   __TEXT.__const: 0x4130
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__objc_opt_ro : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__dof_objc_runt : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_nlclslist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_scoffs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__lazy_load_got : content changed
~ __AUTH_CONST.__auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__objc_opt_ptrs : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Functions:
~ _objc_retainAutoreleasedReturnValue : 156 -> 160
~ __objc_rootAllocWithZone : 328 -> 324
~ _objc_alloc : 52 -> 44
~ _objc_release_full : 216 -> 212
~ __ZN10objc_class15realizeIfNeededEv : 236 -> 244
~ _object_setClass : 668 -> 676
~ -[NSObject init] : 8 -> 4
~ _objc_autoreleasePoolPop : 424 -> 420
~ __ZN11objc_object9changeIsaEP10objc_class : 500 -> 504
~ __ZN19AutoreleasePoolPage12releaseUntilEPP11objc_object : 308 -> 312
~ __ZN19AutoreleasePoolPage3addEP11objc_object : 356 -> 364
~ __ZL38objc_destructInstance_nonnull_realizedP11objc_object : 168 -> 160
~ _class_createInstance : 320 -> 324
~ __ZN11objc_object27sidetable_clearDeallocatingEv : 288 -> 296
~ _objc_autoreleaseReturnValue : 332 -> 336
~ -[NSObject dealloc] : 16 -> 4
~ -[NSObject isKindOfClass:] : 140 -> 136
~ _object_getIndexedIvars : 216 -> 204
~ _objc_lookUpImpOrForward : 812 -> 824
~ __ZL35realizeAndInitializeIfNeeded_lockedP11objc_objectP10objc_classb : 200 -> 192
~ __ZN7cache_t6insertEP13objc_selectorPFvvEP11objc_object : 568 -> 556
~ __ZL23getMethodNoSuper_nolockP10objc_classP13objc_selector : 2144 -> 1992
~ __ZNK8method_t3impEb : 308 -> 312
~ __ZL11fetch_cacheb : 276 -> 272
~ _objc_loadWeakRetained : 680 -> 676
~ __objc_rootDealloc : 100 -> 96
~ _objc_alloc_init : 88 -> 92
~ _weak_register_no_lock : 400 -> 404
~ _objc_storeWeak : 592 -> 588
~ _weak_unregister_no_lock : 508 -> 500
~ __ZN12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEE8lockWithERS3_ : 212 -> 208
~ __ZL23callSetWeaklyReferencedP11objc_object : 328 -> 324
~ __ZL17weak_entry_insertP12weak_table_tP12weak_entry_t : 208 -> 200
~ __ZN12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEE10unlockWithERS3_ : 144 -> 140
~ __ZL22getMethodFromListArrayIPP13method_list_tEP8method_tT_jP13objc_selector : 1716 -> 1572
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPK8method_tPvNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S5_EEEES4_S5_S7_S9_SC_E15LookupBucketForIS4_EEbRKT_RPKSC_ : 264 -> 260
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12iteratorImplILb0EE14skipEmptyListsEv : 576 -> 580
~ -[NSObject class] : 8 -> 16
~ _class_conformsToProtocol : 220 -> 208
~ __ZL34protocol_conformsToProtocol_nolockP10protocol_tS0_ : 228 -> 232
~ _objc_loadWeak : 56 -> 60
~ _object_getClass : 192 -> 200
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12ListIteratorC2ERKS3_ : 104 -> 96
~ _objc_setProperty_nonatomic_copy : 136 -> 128
~ __ZN10objc_class13demangledNameEb : 852 -> 848
~ _class_getName : 28 -> 24
~ __ZNK10class_rw_t2roEv : 152 -> 144
~ -[NSObject autorelease] : 8 -> 16
~ __ZL27object_cxxDestructFromClassP11objc_objectP10objc_class : 224 -> 220
~ _objc_storeStrong : 120 -> 124
~ __ZNK7cache_t20isConstantEmptyCacheEv : 128 -> 132
~ _objc_opt_respondsToSelector : 212 -> 208
~ _class_respondsToSelector_inst : 268 -> 256
~ _objc_autoreleasePoolPush : 300 -> 292
~ -[NSObject isProxy] : 8 -> 20
~ +[NSObject allocWithZone:] : 8 -> 16
~ _object_isClass : 28 -> 40
~ _lookUpImpOrNilTryCache : 276 -> 272
~ +[NSObject resolveInstanceMethod:] : 20 -> 8
~ _objc_copyWeak : 80 -> 76
~ __ZL15append_referrerP12weak_entry_tPP11objc_object : 404 -> 392
~ _objc_destroyWeak : 280 -> 276
~ _weak_clear_no_lock : 396 -> 400
~ -[NSObject hash] : 12 -> 8
~ __ZL20grow_refs_and_insertP12weak_entry_tPP11objc_object : 284 -> 292
~ _objc_getAssociatedObject : 400 -> 392
~ __ZN11objc_object16rootAutorelease2Ev : 144 -> 136
~ _objc_getProperty : 232 -> 220
~ __ZL14_mapStrIsEqualP11_NXMapTablePKvS2_ : 120 -> 116
~ _objc_lookUpClass : 24 -> 16
~ __ZL20_NXMapMemberWithHashP11_NXMapTablePKvjPPv : 272 -> 268
~ ___getPreoptimizedClass_block_invoke : 36 -> 24
~ __ZL27getClassFromNamedClassTablePKc : 136 -> 140
~ __ZL19namedClassTableHashPKc : 152 -> 148
~ __ZL10remapClassP10objc_class : 236 -> 244
~ _sel_registerName : 12 -> 20
~ +[NSObject self] : 12 -> 4
~ __ZL18__sel_registerNamePKcbb : 384 -> 372
~ _objc_allocWithZone : 56 -> 44
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12iteratorImplILb0EEppEv : 788 -> 796
~ _class_respondsToSelector : 12 -> 20
~ +[NSObject isProxy] : 8 -> 16
~ _object_getMethodImplementation : 456 -> 452
~ -[NSObject respondsToSelector:] : 76 -> 80
~ _object_getClassName : 204 -> 208
~ _objc_opt_new : 108 -> 112
~ +[NSObject class] : 8 -> 4
~ _objc_opt_class : 200 -> 204
~ __ZNK11objc_object24sidetable_isDeallocatingEv : 144 -> 136
~ _class_getMethodImplementation : 264 -> 268
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_E20InsertIntoBucketImplIS5_EEPSC_RKS5_RKT_SG_ : 196 -> 200
~ __ZNK11objc_object14sidetable_lockEv : 60 -> 64
~ -[NSObject methodForSelector:] : 84 -> 80
~ +[NSObject instanceMethodForSelector:] : 72 -> 60
~ _objc_storeWeakOrNil : 588 -> 592
~ _objc_sync_nil : 4 -> 12
~ +[NSObject instancesRespondToSelector:] : 28 -> 20
~ _method_getImplementation : 72 -> 60
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_EixEOS5_ : 100 -> 96
~ _method_getTypeEncoding : 56 -> 48
~ __ZNK8method_t5typesEv : 192 -> 184
~ __method_getImplementationAndName : 252 -> 244
~ _protocol_getMethodDescription : 256 -> 264
~ __ZL18search_method_listPK13method_list_tP13objc_selector : 1676 -> 1548
~ _sel_hash : 16 -> 8
~ +[NSObject hash] : 12 -> 4
~ _sel_getUid : 24 -> 16
~ __ZN19AutoreleasePoolPage19autoreleaseFullPageEP11objc_objectPS_ : 200 -> 212
~ _class_copyProtocolList : 1148 -> 1144
~ _objc_setProperty_atomic : 252 -> 264
~ __ZN11objc_object36sidetable_setWeaklyReferenced_nolockEv : 92 -> 84
~ _objc_opt_isKindOfClass : 292 -> 296
~ -[NSObject retainCount] : 4 -> 12
~ _objc_setProperty_nonatomic : 144 -> 140
~ __ZN11objc_object19rootRetain_overflowEb : 288 -> 296
~ __ZNK11objc_object16sidetable_unlockEv : 64 -> 68
~ __ZN4objc12DenseMapBaseINS_8DenseMapIPKcNS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_SB_E11try_emplaceIJRS5_EEENSt3__14pairINS_16DenseMapIteratorIS3_S5_S7_S9_SB_Lb0EEEbEERKS3_DpOT_ : 312 -> 316
~ -[NSObject isMemberOfClass:] : 64 -> 52
~ ___objc_personality_v0 : 208 -> 204
~ -[NSObject retain] : 12 -> 16
~ __Z18protocol_getMethodP10protocol_tP13objc_selectorbbb : 316 -> 304
~ -[NSObject release] : 4 -> 12
~ __ZNK4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classEP10objc_classNS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S6_EEEES4_S6_S8_SA_SD_E15LookupBucketForIS4_EEbRKT_RPKSD_ : 256 -> 260
~ __ZL26_objc_exception_destructorPv : 124 -> 128
~ __objc_rootRelease : 152 -> 160
~ -[NSObject allowsWeakReference] : 40 -> 36
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPKcNS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_SB_E15LookupBucketForIS3_EEbRKT_RPKSB_ : 316 -> 312
~ __ZN11objc_object27sidetable_addExtraRC_nolockEm : 112 -> 120
~ -[NSObject _isDeallocating] : 48 -> 52
~ _class_getInstanceSize : 108 -> 104
~ -[NSObject performSelector:] : 84 -> 92
~ __ZNK10class_rw_t10propertiesEv : 224 -> 220
~ __ZNK13list_array_ttI10property_t15property_list_t6RawPtrE5beginEv : 524 -> 536
~ _objc_retainBlock : 8 -> 12
~ __ZN7cache_t13collectNolockEb : 496 -> 488
~ +[NSObject isMemberOfClass:] : 24 -> 28
~ __objc_rootTryRetain : 144 -> 156
~ _protocol_getName : 24 -> 32
~ __ZN10protocol_t13demangledNameEv : 124 -> 132
~ _protocol_copyMethodDescriptionList : 684 -> 680
~ __ZN15entsize_list_ttI8method_t13method_list_tLj4294901763ENS0_16pointer_modifierEE3endEv : 108 -> 96
~ __protocol_getMethodTypeEncoding : 288 -> 280
~ __ZL32getExtendedTypesIndexesForMethodP10protocol_tPK8method_tbbRjS4_ : 164 -> 172
~ _objc_constructInstance : 212 -> 220
~ _sel_isEqual : 20 -> 24
~ __ZL25getMethodFromRelativeListP20relative_list_list_tI13method_list_tEP13objc_selector : 1860 -> 1728
~ __ZNK13list_array_ttI10property_t15property_list_t6RawPtrE3endEv : 260 -> 256
~ _class_getProperty : 504 -> 492
~ __ZN13list_array_ttI10property_t15property_list_t6RawPtrE12iteratorImplILb0EEppEv : 900 -> 892
~ __ZL7getIvarP10objc_classPKc : 236 -> 220
~ __class_getVariable : 284 -> 276
~ __ZL13SkipFirstTypePKc : 216 -> 208
~ __ZL11static_initv : 236 -> 228
~ _map_images_nolock : 8364 -> 8352
~ __ZNK11header_info9classlistEPm : 140 -> 152
~ __ZL24hasSignedClassROPointersPK14mach_header_64P29_dyld_section_location_info_s : 100 -> 88
~ __ZL12allocBucketsj : 96 -> 92
~ __ZL9protocolsv : 200 -> 188
~ __ZNK11header_info9nlclslistEPm : 148 -> 144
~ ____ZN10objc_class36setInstancesRequireRawIsaRecursivelyEb_block_invoke : 124 -> 116
~ __ZN10objc_class34setDisallowPreoptCachesRecursivelyEPKc : 272 -> 264
~ ____ZN10objc_class34setDisallowPreoptCachesRecursivelyEPKc_block_invoke : 292 -> 280
~ _objc_opt_self : 44 -> 48
~ __ZL11weak_resizeP12weak_table_tm : 208 -> 196
~ __ZL9addMethodP10objc_classP13objc_selectorPFvvEPKcb : 456 -> 460
~ __ZL37foreach_realized_class_and_subclass_2P10objc_classRxbU13block_pointerFbS0_E : 768 -> 764
~ __ZN10class_rw_t16extAllocIfNeededEv : 104 -> 112
~ __ZL11addSubclassP10objc_classS0_ : 820 -> 816
~ __ZL13getChildClassP10objc_classM14metaclass_rw_tS0_ : 188 -> 192
~ __ZL18prepareMethodListsP10objc_classPP13method_list_tibbPKc : 1616 -> 1596
~ __ZN22OriginalMetaclassMap_t19originalMetaclassOfEP10objc_class : 256 -> 252
~ __ZL24realizeClassWithoutSwiftP10objc_classS0_ : 4364 -> 4348
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classENS_13category_listENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S5_EEEES4_S5_S7_S9_SC_E4findERKS4_ : 188 -> 176
~ __ZNK4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classENS_13category_listENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S5_EEEES4_S5_S7_S9_SC_E15LookupBucketForIS4_EEbRKT_RPKSC_ : 296 -> 284
~ __ZN10objc_class36setInstancesRequireRawIsaRecursivelyEb : 200 -> 212
~ _initializeNonMetaClass : 1040 -> 1048
~ __ZL24initializeAndMaybeRelockP10objc_classP11objc_objectR12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEEb : 360 -> 352
~ __ZL11unlockClassP10objc_class : 52 -> 60
~ __ZL33realizeClassMaybeSwiftMaybeRelockP10objc_classR12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEEb : 548 -> 552
~ __ZN4objc7Scanner15scanMethodListsIN13list_array_ttI8method_t13method_list_t24method_list_t_authed_ptrE12ListIteratorEEEjT_S8_ : 2064 -> 2032
~ __ZN4objc7Scanner18scanAddedClassImplEP10objc_classNS0_11metaclass_tE : 2652 -> 2640
~ _CALLING_SOME_+initialize_METHOD : 36 -> 44
~ __ZN13list_array_ttI8method_t13method_list_t24method_list_t_authed_ptrE12ListIteratorC2ERKS4_ : 192 -> 188
~ __ZNK10class_rw_t7methodsEv : 296 -> 292
~ __ZN23tls_autoptr_direct_implI18_objc_pthread_dataL7tls_key0EE5dtor_EPv : 156 -> 160
~ __ZN19AutoreleasePoolPage4killEv : 208 -> 200
~ __ZN11objc_object16sidetable_retainEb : 180 -> 188
~ __ZN11objc_object17sidetable_releaseEbb : 308 -> 320
~ _class_getClassMethod : 68 -> 64
~ _method_copyReturnType : 144 -> 140
~ __ZL12SubtypeUntilPKcc : 160 -> 152
~ _sel_lookUpByName : 292 -> 280
~ _class_addProtocol : 364 -> 360
~ __ZL27internal_class_getImageNameP10objc_classPPKc : 60 -> 48
~ __ZNK13list_array_ttIm15protocol_list_t6RawPtrE8validateEv : 632 -> 640
~ ____ZL17addMethods_finishP10objc_classP13method_list_t_block_invoke : 44 -> 56
~ +[NSObject resolveClassMethod:] : 8 -> 16
~ __ZN7cache_t11eraseNolockEPKc : 568 -> 560
~ +[NSObject retain] : 8 -> 16
~ _objc_getClass : 16 -> 24
~ +[NSObject superclass] : 60 -> 68
~ __ZN4objc12DenseMapBaseINS_8DenseMapIPKcNS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_SB_E4findES3_ : 136 -> 140
~ __ZN11objc_object21rootRelease_underflowEb : 600 -> 612
~ __ZL11getProtocolPKc : 152 -> 144
~ _NXMapGet : 108 -> 120
~ ___getPreoptimizedProtocol_block_invoke : 36 -> 28
~ _method_getReturnType : 200 -> 196
~ +[NSObject respondsToSelector:] : 20 -> 24
~ _objc_moveWeak : 280 -> 288
~ _class_replaceMethod : 324 -> 312
~ __ZN13list_array_ttI8method_t13method_list_t24method_list_t_authed_ptrE11attachListsEPKPS1_jbPKc : 1460 -> 1440
~ ____ZL11flushCachesP10objc_classPKcU13block_pointerFbS0_E_block_invoke : 76 -> 84
~ __ZL17addMethods_finishP10objc_classP13method_list_t : 300 -> 292
~ _class_addMethod : 252 -> 248
~ __ZL23_collecting_in_criticalv : 552 -> 548
~ _objc_initWeakOrNil : 576 -> 580
~ __ZL19schedule_class_loadP10objc_class : 392 -> 396
~ __ZN10objc_class13getLoadMethodEv : 3716 -> 3436
~ __ZL25_method_setImplementationP10objc_classP8method_tPFvvE : 372 -> 380
~ ____ZL25_method_setImplementationP10objc_classP8method_tPFvvE_block_invoke : 28 -> 24
~ __ZNK7cache_t11shouldFlushEP13objc_selectorPFvvE : 184 -> 192
~ __ZL22copySwiftV1MangledNamePKcb : 328 -> 336
~ __ZL14empty_getClassPKcPP10objc_class : 20 -> 24
~ __ZN4objc7Scanner17scanChangedMethodEP10objc_classPK8method_t : 944 -> 948
~ __ZL27_allocateTrampolinesAndDatav : 652 -> 664
~ __ZN13list_array_ttI8method_t13method_list_t24method_list_t_authed_ptrE12iteratorImplILb1EE14skipEmptyListsEv : 808 -> 812
~ __ZNK8method_t20getCachedDescriptionEv : 656 -> 648
~ _method_getDescription : 88 -> 80
~ +[NSObject isKindOfClass:] : 108 -> 96
~ __ZL13addNamedClassP10objc_classPKcS0_ : 588 -> 600
~ _objc_registerClassPair : 716 -> 712
~ _objc_getProtocol : 192 -> 180
~ _NXMapInsertWithHash : 440 -> 432
~ __ZN4objc20UnattachedCategories11addForClassE21locstamped_category_tP10objc_class : 616 -> 620
~ __category_getLoadMethod : 1808 -> 1664
~ __ZN11objc_object29sidetable_clearExtraRC_nolockEv : 120 -> 112
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_E7compactEv : 184 -> 172
~ __ZN17loadImageCallbackaSERKS_ : 176 -> 180
~ _class_setVersion : 344 -> 340
~ __ZNK4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classES4_NS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S4_EEEES4_S4_S6_S8_SB_E15LookupBucketForIS4_EEbRKT_RPKSB_ : 248 -> 256
~ +[NSObject new] : 80 -> 92
~ __ZN10objc_class11mangledNameEv : 92 -> 88
~ _property_copyAttributeValue : 264 -> 260
~ __ZL16findOneAttributejPvS_PKcmS1_m : 172 -> 168
~ __ZZL16attachCategoriesP10objc_classPK21locstamped_category_tjS0_iENK3$_0clEPZL16attachCategoriesS0_S3_jS0_iE5Listsb : 388 -> 396
~ _gdb_objc_class_changed : 8 -> 12
~ _class_copyIvarList : 416 -> 420
~ __ZL15fixupMethodListP13method_list_tbbbPPP13objc_selector : 1020 -> 992
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classENS_13category_listENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S5_EEEES4_S5_S7_S9_SC_E7compactEv : 368 -> 344
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_E4growEj : 524 -> 496
~ _protocol_copyPropertyList2 : 388 -> 396
~ _property_copyAttributeList : 404 -> 400
~ __ZL16copyOneAttributejPvS_PKcmS1_m : 160 -> 164
~ __ZL9readClassP10objc_classbb : 1708 -> 1700
~ _objc_readClassPair : 672 -> 676
~ __ZNSt3__118__stable_sort_moveINS_17_ClassicAlgPolicyERN8method_t16SortBySELAddressEPNS2_9bigSignedEEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEPNSA_10value_typeE : 1244 -> 1288
~ +[NSObject performSelector:] : 92 -> 84
~ __objc_realizeClassFromSwift : 340 -> 336
~ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERN8method_t16SortBySELAddressEPNS2_9bigSignedEEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEPNSA_10value_typeEl : 2248 -> 2132
~ ____class_setCustomDeallocInitiation_block_invoke : 20 -> 24
~ -[NSObject forwardingTargetForSelector:] : 12 -> 20
~ ____ZZL16attachCategoriesP10objc_classPK21locstamped_category_tjS0_iENK3$_0clEPZL16attachCategoriesS0_S3_jS0_iE5Listsb_block_invoke : 52 -> 56
~ +[NSObject release] : 12 -> 4
~ _class_initialize : 116 -> 120
~ _class_addIvar : 1008 -> 1012
~ _protocol_conformsToProtocol : 188 -> 200
~ __ZN4objc8DenseMapI12DisguisedPtrI10objc_classENS_13category_listENS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S4_EEE4growEj : 556 -> 536
~ _object_setIvarWithStrongDefault : 152 -> 156
~ _objc_isUniquelyReferenced : 264 -> 256
~ -[NSObject self] : 16 -> 8
~ __ZNK11header_info12protocollistEPm : 148 -> 140
~ _method_copyArgumentType : 188 -> 184
~ __ZN13method_list_t18allocateMethodListEjj : 116 -> 120
~ __ZN13method_list_t16sortBySELAddressEv : 464 -> 476
~ __ZN4objc8DenseMapIPK8method_tP23objc_method_descriptionNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S5_EEE4growEj : 500 -> 508
~ __thisThreadIsInitializingClass : 152 -> 148
~ __ZL24make_ro_writeable_nolockP10objc_class : 144 -> 140
~ __ZL16addRemappedClassP10objc_classS0_ : 464 -> 472
~ __ZL16scanMangledFieldRPKcS0_S1_Ri : 152 -> 160
~ __ZL25pageAndIndexContainingIMPPFvvEPm : 304 -> 312
~ _method_exchangeImplementations : 944 -> 940
~ __ZN4objc8DenseMapIPK8method_tPvNS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S4_EEE4growEj : 532 -> 520
~ ___method_exchangeImplementations_block_invoke : 108 -> 100
~ __objc_beginClassEnumeration : 468 -> 464
~ _objc_claimAutoreleasedReturnValue : 148 -> 136
~ __objc_enumerateNextClass : 624 -> 632
~ __ZN8method_t7setNameEP13objc_selector : 92 -> 104
~ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERN8method_t16SortBySELAddressEPNS2_3bigEEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEPNSA_10value_typeEl : 1196 -> 1108
~ __ZNSt3__118__stable_sort_moveINS_17_ClassicAlgPolicyERN8method_t16SortBySELAddressEPNS2_3bigEEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEPNSA_10value_typeE : 1172 -> 1136
~ _object_getInstanceVariable : 132 -> 124
~ __ZL12_NXMapRehashP11_NXMapTable : 240 -> 232
~ __ZL27namedClassTableHashCallbackP11_NXMapTablePKv : 16 -> 12
~ -[NSObject isFault] : 12 -> 8
~ _protocol_copyPropertyList : 20 -> 12
~ _object_dispose : 76 -> 80
~ __ZL31objc_retainAutoreleaseAndReturnP11objc_object : 40 -> 48
~ -[NSObject debugDescription] : 20 -> 24
~ __ZL23fixupProtocolMethodListP10protocol_tP13method_list_tbbbPPP13objc_selector : 664 -> 656
~ +[NSObject copyWithZone:] : 8 -> 16
~ _object_setInstanceVariableWithStrongDefault : 184 -> 188
~ __ZN19AutoreleasePoolPage12popPageDebugEPvPS_PP11objc_object : 272 -> 268
~ _objc_copyCppObjectAtomic : 148 -> 156
~ _protocol_getProperty : 236 -> 232
~ __objc_deallocOnMainThreadHelper : 16 -> 12
~ _objc_removeAssociatedObjects : 48 -> 44
~ -[NSObject superclass] : 96 -> 84
~ _NXMapKeyCopyingInsert : 260 -> 268
~ __headerForAddress : 188 -> 180
~ __Z12_objc_informPKcz : 112 -> 124
~ __ZL12_objc_syslogPKc : 196 -> 192
~ __ZL14nonMetaClassesv : 188 -> 200
~ __ZL11_mapPtrHashP11_NXMapTablePKv : 20 -> 16
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI11objc_objectENS_13SmallDenseMapIPKvNS_15ObjcAssociationELj1ENS_17DenseMapValueInfoIS8_EENS_12DenseMapInfoIS7_EENS_6detail12DenseMapPairIS7_S8_EEEENS9_ISG_EENSB_IS4_EENSE_IS4_SG_EEEES4_SG_SH_SI_SJ_E5eraseENS_16DenseMapIteratorIS4_SG_SH_SI_SJ_Lb0EEE : 396 -> 380
~ ____ZL13setSuperclassP10objc_classS0__block_invoke.204 : 8 -> 16
~ __ZN4objc8DenseMapI12DisguisedPtrI11objc_objectENS_13SmallDenseMapIPKvNS_15ObjcAssociationELj1ENS_17DenseMapValueInfoIS7_EENS_12DenseMapInfoIS6_EENS_6detail12DenseMapPairIS6_S7_EEEENS8_ISF_EENSA_IS3_EENSD_IS3_SF_EEE4growEj : 604 -> 600
~ _class_getVersion : 180 -> 168
~ _NXMapInsert : 112 -> 120
~ __ZL16_objc_fault_implbbPKcPc : 320 -> 332
~ __ZL12_objc_fatalvyyPKcPc : 168 -> 172
~ _property_getAttributes : 12 -> 20
~ __ZNK19AutoreleasePoolPage10busted_dieEv : 36 -> 44
~ _class_getSuperclass : 68 -> 72
~ __ZN19AutoreleasePoolPage18autoreleaseNewPageEP11objc_object : 108 -> 104
~ _method_getName : 192 -> 204
~ -[NSObject performSelector:withObject:withObject:] : 116 -> 104
~ _property_getName : 12 -> 20
~ _objc_copyClassList : 188 -> 196
~ ____ZL33objc_copyRealizedClassList_nolockPj_block_invoke.38 : 40 -> 28
~ ___getSharedCachePreoptimizedProtocol_block_invoke : 64 -> 56
~ __ZNK4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classEP10objc_classNS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S6_EEEES4_S6_S8_SA_SD_E22FatalCorruptHashTablesEPKSD_j : 92 -> 96
~ sub_180433c50 -> sub_18043363c : 4 -> 8
~ _NXResetMapTable : 204 -> 192
~ _NXMapGetWithHash : 60 -> 52
~ _NXMapRemove : 692 -> 696
~ __ZL10_mapNoFreeP11_NXMapTablePvS1_ : 8 -> 4
~ _instrumentObjcMessageSends : 4 -> 16
~ __objc_warn_deprecated : 16 -> 4
~ __ZN4objc8DenseMapI12DisguisedPtrI10objc_classEP17PendingInitializeNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S5_EEE4growEj : 504 -> 496
~ __objc_setClassCopyFixupHandler : 380 -> 392
~ __ZNK13method_list_t9duplicateEv : 2824 -> 2820
~ __ZL10free_classP10objc_class : 1712 -> 1696
~ _ivar_getName : 20 -> 12
~ _protocol_addProperty : 636 -> 628
~ ___copy_helper_block_e8_32c49_ZTSKZL33objc_copyRealizedClassList_nolockPjE3$_1 : 24 -> 16
~ _objc_copyProtocolList : 1148 -> 1144
~ _objc_debug_class_getNameRaw : 172 -> 164
~ _gdb_object_getClass : 192 -> 196
~ ___copy_helper_block_e8_32c69_ZTSKZN10objc_class39setDisallowPreoptInlinedSelsRecursivelyEPKcE3$_0 : 12 -> 20
~ _class_setWeakIvarLayout : 492 -> 488
~ __ZL30objc_duplicateClassImpl_nolockP10objc_classPKcm : 1644 -> 1632
~ _object_copy : 1024 -> 1016
~ __ZN4objc8DenseMapI12DisguisedPtrI10objc_classES3_NS_17DenseMapValueInfoIS3_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S3_EEE4growEj : 532 -> 524
~ __ZN4objc8DenseMapI12DisguisedPtrI10objc_classEP10objc_classNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S5_EEE4growEj : 532 -> 512
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERN8method_t16SortBySELAddressEPNS2_3bigEEEvT1_S7_S7_OT0_NS_15iterator_traitsIS7_E15difference_typeESC_PNSB_10value_typeEl : 2040 -> 1920
~ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB9fqn220106IRPN8method_t9bigSignedES7_EEvOT_OT0_ : 564 -> 572
~ __ZNSt3__115__inplace_mergeINS_17_ClassicAlgPolicyERN8method_t16SortBySELAddressEPNS2_9bigSignedEEEvT1_S7_S7_OT0_NS_15iterator_traitsIS7_E15difference_typeESC_PNSB_10value_typeEl : 2584 -> 2512
~ __ZNSt3__112construct_atB9fqn220106IN8method_t9bigSignedEJS2_EPS2_EEPT_S5_DpOT0_ : 172 -> 180
~ ___copy_helper_block_e8_32c127_ZTSKZZL16attachCategoriesP10objc_classPK21locstamped_category_tjS0_iENK3$_0clEPZL16attachCategoriesS0_S3_jS0_iE5ListsbEUlS0_E_ : 4 -> 16
~ __ZNSt3__16vectorI29_dyld_objc_notify_mapped_infoNS_9allocatorIS1_EEE24__emplace_back_slow_pathIJRKS1_EEEPS1_DpOT_ : 216 -> 220
~ ___copy_helper_block_e8_32c67_ZTSKZL25_method_setImplementationP10objc_classP8method_tPFvvEE3$_0 : 20 -> 16
~ __ZNK15entsize_list_ttI8method_t13method_list_tLj4294901763ENS0_16pointer_modifierEE3getEj : 104 -> 96
~ ___copy_helper_block_e8_32c61_ZTSKZL32objc_getRealizedClassList_nolockPP10objc_classmE3$_1 : 24 -> 20
~ __ZNSt3__16vectorIPK14mach_header_64NS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 212 -> 220
~ __ZL20empty_lazyClassNamerP10objc_class : 12 -> 20
~ __ZN4objc7Scanner19setNSObjectSwizzledEP10objc_classjNS0_11metaclass_tE : 100 -> 92
~ ___copy_helper_block_e8_32c60_ZTSKZL17addMethods_finishP10objc_classP13method_list_tE3$_0 : 4 -> 8
~ ___copy_helper_block_e8_32c43_ZTSKZL13setSuperclassP10objc_classS0_E3$_1 : 8 -> 16
~ __ZN4objc8DenseMapIPKcP8ProtocolNS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS2_EENS_6detail12DenseMapPairIS2_S4_EEE4growEj : 520 -> 496
~ __objc_atfork_child : 504 -> 512
~ _objc_weak_error : 12 -> 16
~ __ZL13weakTableScanv : 360 -> 356
~ _objc_autoreleaseNoPool : 12 -> 16
~ _objc_autoreleasePoolInvalid : 16 -> 12
~ __ZNK11objc_object21sidetable_retainCountEv : 220 -> 232
~ _objc_unretainedPointer : 16 -> 8
~ -[__NSUnrecognizedTaggedPointer autorelease] : 8 -> 4
~ +[NSObject forwardInvocation:] : 84 -> 88
~ -[NSObject forwardInvocation:] : 84 -> 96
~ +[NSObject description] : 20 -> 8
~ -[NSObject description] : 16 -> 12
~ __ZNK19AutoreleasePoolPage6bustedIPFvPKczEEEvT_ : 152 -> 148
~ ___copy_helper_block_e8_32c48_ZTSKZ35getPreoptimizedClassesWithMetaClassE3$_0 : 24 -> 20
~ ___destroy_helper_block_e8_32 : 16 -> 4
~ ___destroy_helper_block_e8_32.671 : 8 -> 4
~ __ZN7cache_t9bad_cacheEP11objc_objectP13objc_selector : 236 -> 232
~ __Z11_objc_errorP11objc_objectPKcPc : 84 -> 88
~ __ZN10objc_class27printInstancesRequireRawIsaEb : 116 -> 112
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPK8method_tPvNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S5_EEEES4_S5_S7_S9_SC_E22FatalCorruptHashTablesEPKSC_j : 96 -> 88
~ __ZN4objc7Scanner11printCustomEPKcP10objc_classNS0_11inherited_tE : 128 -> 140
~ __ZL17printReplacementsP10objc_classPK21locstamped_category_tj : 1304 -> 1272
~ __ZSt28__throw_bad_array_new_lengthB9fqn220106v : 28 -> 20
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPK8method_tP23objc_method_descriptionNS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S6_EEEES4_S6_S8_SA_SD_E22FatalCorruptHashTablesEPKSD_j : 88 -> 96
~ __ZNK4objc12DenseMapBaseINS_13SmallDenseMapIPKvNS_15ObjcAssociationELj1ENS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S4_EEEES3_S4_S6_S8_SB_E22FatalCorruptHashTablesEPKSB_j : 100 -> 92
~ __ZL22defaultBadAllocHandlerP10objc_class : 48 -> 36
~ __Z25_objc_callBadAllocHandlerP10objc_class : 24 -> 32
~ __ZL18startWeakTableScanv : 128 -> 132
~ +[NSObject doesNotRecognizeSelector:] : 76 -> 80
~ -[NSObject doesNotRecognizeSelector:] : 68 -> 80
~ +[NSObject methodSignatureForSelector:] : 36 -> 24
~ -[NSObject methodSignatureForSelector:] : 24 -> 32

```
