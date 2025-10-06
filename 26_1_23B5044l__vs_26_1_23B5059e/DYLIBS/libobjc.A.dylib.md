## libobjc.A.dylib

> `/usr/lib/libobjc.A.dylib`

```diff

-950.0.0.0.0
-  __TEXT.__text: 0x3fe04
+951.1.0.0.0
+  __TEXT.__text: 0x3fe54
   __TEXT.__auth_stubs: 0x760
   __TEXT.__delay_helper: 0xec
   __TEXT.__objc_methlist: 0x5ec

   - /usr/lib/libc++abi.dylib
   - /usr/lib/libobjc-env.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  UUID: 23E64DF5-DC0C-3CEF-9E03-C3B8B95C54D6
+  UUID: AF9349A3-834F-369E-ACE5-C50571C9C7BA
   Functions: 889
   Symbols:   2003
   CStrings:  565
Symbols:
+ _malloc_type_zone_malloc_with_options
- _malloc_type_zone_malloc_with_options_internal
Functions:
~ _objc_retainAutoreleaseReturnValue : 356 -> 364
~ __ZN19AutoreleasePoolPage24moveTLSAutoreleaseToPoolE21ReturnAutoreleaseInfo : 160 -> 168
~ _objc_alloc_init : 88 -> 84
~ __objc_rootAllocWithZone : 332 -> 320
~ __ZN10objc_class15realizeIfNeededEv : 236 -> 244
~ +[NSObject alloc] : 12 -> 4
~ _objc_alloc : 40 -> 48
~ __objc_rootAlloc : 40 -> 48
~ _objc_autorelease : 492 -> 504
~ _class_createInstance : 320 -> 332
~ -[NSObject autorelease] : 16 -> 8
~ _objc_storeWeak : 596 -> 592
~ __ZN12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEE8lockWithERS3_ : 204 -> 216
~ _weak_unregister_no_lock : 496 -> 504
~ _objc_autoreleasePoolPush : 300 -> 292
~ __ZN19AutoreleasePoolPage3addEP11objc_object : 360 -> 352
~ _object_getMethodImplementation : 448 -> 456
~ __objc_rootAutorelease : 328 -> 320
~ _objc_allocWithZone : 56 -> 48
~ __ZL17weak_entry_insertP12weak_table_tP12weak_entry_t : 212 -> 200
~ __ZN12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEE10unlockWithERS3_ : 148 -> 152
~ __ZN19AutoreleasePoolPage12releaseUntilEPP11objc_object : 296 -> 304
~ -[NSObject dealloc] : 12 -> 4
~ _objc_retainAutorelease : 40 -> 52
~ __ZL7id2dataP11objc_object8SyncKind5usage : 804 -> 808
~ _objc_copyWeak : 88 -> 84
~ __ZL11fetch_cacheb : 276 -> 272
~ -[NSObject copy] : 20 -> 24
~ __ZL38objc_destructInstance_nonnull_realizedP11objc_object : 168 -> 156
~ _object_cxxConstructFromClass : 368 -> 360
~ __ZN19AutoreleasePoolPage17autoreleaseNoPageEP11objc_object : 320 -> 324
~ _objc_getProperty : 220 -> 224
~ __ZNK7cache_t20isConstantEmptyCacheEv : 140 -> 136
~ __ZN4objc12DenseMapBaseINS_8DenseMapIPKvNS_15ObjcAssociationENS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S4_EEEES3_S4_S6_S8_SB_E4findES3_ : 124 -> 120
~ __ZL20grow_refs_and_insertP12weak_entry_tPP11objc_object : 292 -> 280
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPKvNS_15ObjcAssociationENS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S4_EEEES3_S4_S6_S8_SB_E15LookupBucketForIS3_EEbRKT_RPKSB_ : 256 -> 252
~ __ZL15append_referrerP12weak_entry_tPP11objc_object : 396 -> 388
~ __ZL21objc_releaseAndReturnP11objc_object : 52 -> 48
~ _objc_destructInstance : 68 -> 72
~ _objc_loadWeak : 56 -> 68
~ __ZNK4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI11objc_objectENS1_IPKvNS_15ObjcAssociationENS_17DenseMapValueInfoIS7_EENS_12DenseMapInfoIS6_EENS_6detail12DenseMapPairIS6_S7_EEEENS8_ISF_EENSA_IS4_EENSD_IS4_SF_EEEES4_SF_SG_SH_SI_E15LookupBucketForIS4_EEbRKT_RPKSI_ : 276 -> 272
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_E4findERKS5_ : 116 -> 124
~ __ZN11objc_object27sidetable_clearDeallocatingEv : 284 -> 292
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_E15LookupBucketForIS5_EEbRKT_RPSC_ : 276 -> 280
~ _objc_setProperty_nonatomic_copy : 124 -> 136
~ _weak_clear_no_lock : 392 -> 400
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_EixEOS5_ : 108 -> 100
~ __ZNK11objc_object24sidetable_isDeallocatingEv : 140 -> 148
~ -[NSObject _isDeallocating] : 40 -> 48
~ +[NSObject class] : 4 -> 12
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12iteratorImplILb0EEppEv : 792 -> 784
~ -[NSObject zone] : 8 -> 12
~ __ZL18__sel_registerNamePKcbb : 380 -> 384
~ _objc_opt_self : 48 -> 40
~ +[NSObject self] : 16 -> 8
~ _class_respondsToSelector : 12 -> 24
~ _objc_setProperty_atomic_copy : 220 -> 224
~ _object_getIndexedIvars : 204 -> 200
~ _sel_registerName : 16 -> 20
~ ___getPreoptimizedClass_block_invoke : 24 -> 32
~ +[NSObject isProxy] : 16 -> 8
~ _class_getMethodImplementation : 260 -> 256
~ _objc_setAssociatedObject : 1680 -> 1676
~ __ZN19AutoreleasePoolPageC2EPS_ : 284 -> 288
~ __ZN4objc8DenseMapIPKvNS_15ObjcAssociationENS_17DenseMapValueInfoIS3_EENS_12DenseMapInfoIS2_EENS_6detail12DenseMapPairIS2_S3_EEE4growEj : 724 -> 728
~ _objc_weak_error : 8 -> 16
~ __ZN19AutoreleasePoolPage19autoreleaseFullPageEP11objc_objectPS_ : 204 -> 212
~ __ZL27getClassFromNamedClassTablePKc : 148 -> 144
~ _objc_lookUpClass : 12 -> 16
~ __ZL20_NXMapMemberWithHashP11_NXMapTablePKvjPPv : 264 -> 260
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI11objc_objectENS1_IPKvNS_15ObjcAssociationENS_17DenseMapValueInfoIS7_EENS_12DenseMapInfoIS6_EENS_6detail12DenseMapPairIS6_S7_EEEENS8_ISF_EENSA_IS4_EENSD_IS4_SF_EEEES4_SF_SG_SH_SI_E5eraseENS_16DenseMapIteratorIS4_SF_SG_SH_SI_Lb0EEE : 456 -> 460
~ -[NSObject allowsWeakReference] : 44 -> 40
~ -[Protocol hash] : 12 -> 16
~ _protocol_isEqual : 116 -> 112
~ _sel_hash : 8 -> 12
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPK8method_tP23objc_method_descriptionNS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S6_EEEES4_S6_S8_SA_SD_E15LookupBucketForIS4_EEbRKT_RPKSD_ : 268 -> 264
~ __objc_init : 2176 -> 2212
~ __ZNK8method_t20getCachedDescriptionEv : 644 -> 656
~ _map_images_nolock : 8768 -> 8772
~ __ZNK11objc_object16sidetable_unlockEv : 64 -> 56
~ __objc_rootRetainCount : 220 -> 228
~ __method_getImplementationAndName : 252 -> 248
~ _sel_isEqual : 24 -> 12
~ __ZL25getMethodFromRelativeListP20relative_list_list_tI13method_list_tEP13objc_selector : 1708 -> 1720
~ _objc_constructInstance : 216 -> 220
~ _class_getInstanceMethod : 312 -> 308
~ _objc_copyStruct : 212 -> 200
~ _method_getNumberOfArguments : 200 -> 196
~ _encoding_getArgumentInfo : 436 -> 440
~ _method_getReturnType : 200 -> 196
~ __ZN4objc10SafeRanges3addEmm : 208 -> 196
~ __ZNK11header_info9classlistEPm : 148 -> 144
~ __ZNSt3__110__function6__funcIZ12appendHeaderE3$_0NS_9allocatorIS2_EEFvPK18segment_command_64lEE7destroyEv : 8 -> 12
~ __ZNK11header_info7selrefsEPm : 148 -> 144
~ __ZL24hasSignedClassROPointersPK14mach_header_64P29_dyld_section_location_info_s : 92 -> 96
~ __ZL18addClassTableEntryP10objc_classb : 348 -> 344
~ __ZN4objc10SafeRanges4findEmRj : 224 -> 228
~ __ZNK4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classENS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS4_EENS5_12DenseSetPairIS4_EEEES4_S6_S8_SA_SC_E15LookupBucketForIS4_EEbRKT_RPKSC_ : 252 -> 264
~ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN4objc10SafeRanges4findEmRjE3$_0PNS3_5RangeELb0EEEvT1_S9_T0_NS_15iterator_traitsIS9_E15difference_typeEb : 2852 -> 2856
~ _lookUpImpOrNilTryCache : 268 -> 276
~ __ZL11weak_resizeP12weak_table_tm : 200 -> 192
~ __ZN20objc_tls_direct_baseIP19AutoreleasePoolPageL7tls_key3ENS0_14HotPageDeallocEE5dtor_EPv : 220 -> 216
~ __ZN23tls_autoptr_direct_implI18_objc_pthread_dataL7tls_key0EE5dtor_EPv : 148 -> 136
~ __ZN11objc_object17sidetable_releaseEbb : 320 -> 328
~ __ZNK19AutoreleasePoolPage10busted_dieEv : 48 -> 40
~ __ZN10objc_class15setInstanceSizeEj : 132 -> 144
~ __ZN4objc8DenseMapI12DisguisedPtrI11objc_objectENS0_IPKvNS_15ObjcAssociationENS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_S6_EEEENS7_ISE_EENS9_IS3_EENSC_IS3_SE_EEE4growEj : 796 -> 800
~ __ZNK13list_array_ttIm15protocol_list_t6RawPtrE8validateEv : 632 -> 644
~ __ZL20classSlotForTagIndex16objc_tag_index_t : 112 -> 116
~ ____ZN10objc_class34setDisallowPreoptCachesRecursivelyEPKc_block_invoke : 280 -> 276
~ _class_setSuperclass : 732 -> 736
~ __ZN15entsize_list_ttI8method_t13method_list_tLj4294901763ENS0_16pointer_modifierEE3endEv : 104 -> 100
~ ____ZL13setSuperclassP10objc_classS0__block_invoke.197 : 20 -> 8
~ __ZN4objc20UnattachedCategories13attachToClassEP10objc_classS2_i : 380 -> 376
~ _objc_addLoadImageFunc2 : 400 -> 404
~ __ZL32getExtendedTypesIndexesForMethodP10protocol_tPK8method_tbbRjS4_ : 160 -> 172
~ _objc_getClass : 12 -> 16
~ __ZL33_setThisThreadIsInitializingClassP10objc_class : 292 -> 300
~ __ZL42_initializeSwiftRefcountingThenCallReleaseP11objc_object : 108 -> 100
~ __ZL11unlockClassP10objc_class : 64 -> 56
~ +[NSObject initialize] : 16 -> 8
~ __ZN11objc_object21rootRelease_underflowEb : 608 -> 600
~ +[NSObject new] : 80 -> 88
~ __ZL9readClassP10objc_classbb : 1756 -> 1768
~ _objc_readClassPair : 676 -> 664
~ ____ZZL16attachCategoriesP10objc_classPK21locstamped_category_tjS0_iENK3$_0clEPZL16attachCategoriesS0_S3_jS0_iE5Listsb_block_invoke : 52 -> 48
~ _objc_allocateClassPair : 380 -> 384
~ __ZL24alloc_class_for_subclassP10objc_classm : 264 -> 276
~ __ZL33objc_initializeClassPair_internalP10objc_classPKcS0_S0_ : 1792 -> 1796
~ __ZN4objc8DenseMapI12DisguisedPtrI10objc_classENS_13category_listENS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S4_EEE4growEj : 732 -> 744
~ _objc_registerClassPair : 952 -> 940
~ _class_initialize : 124 -> 116
~ _imp_implementationWithBlock : 992 -> 984
~ _class_addMethod : 244 -> 252
~ __ZN24TrampolinePointerWrapper18TrampolinePointers17TrampolineAddressC2EPvPKc : 336 -> 328
~ __ZL27_allocateTrampolinesAndDatav : 684 -> 660
~ __ZL25pageAndIndexContainingIMPPFvvEPm : 312 -> 320
~ __ZN19AutoreleasePoolPage12popPageDebugEPvPS_PP11objc_object : 276 -> 272
~ __ZL12SubtypeUntilPKcc : 148 -> 152
~ __ZN13list_array_ttI10property_t15property_list_t6RawPtrE12iteratorImplILb0EEppEv : 892 -> 888
~ __ZL27internal_class_getImageNameP10objc_classPPKc : 52 -> 56
~ _protocol_copyPropertyList2 : 384 -> 392
~ +[NSObject retain] : 16 -> 8
~ _class_getProperty : 728 -> 724
~ _objc_removeAssociatedObjects : 40 -> 44
~ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8nn200100IRPN8method_t9bigSignedES7_EEvOT_OT0_ : 564 -> 560
~ __ZN4objc12DenseMapBaseINS_8DenseMapIPKcNS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_SB_E4findES3_ : 136 -> 140
~ __ZL7getIvarP10objc_classPKc : 212 -> 208
~ _sel_lookUpByName : 292 -> 280
~ -[NSObject self] : 8 -> 16
~ +[NSObject release] : 8 -> 16
~ _objc_enumerateClasses : 300 -> 296
~ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERZN4objc10SafeRanges4findEmRjE3$_0PNS3_5RangeEEEbT1_S9_T0_ : 824 -> 828
~ _method_getName : 192 -> 204
~ _objc_copyCppObjectAtomic : 152 -> 156
~ -[NSObject superclass] : 96 -> 92
~ _objc_addLoadImageFunc : 320 -> 308
~ _objc_duplicateClass : 1852 -> 1848
~ __objc_atfork_child : 508 -> 504
~ __ZNK11objc_object21sidetable_retainCountEv : 224 -> 232
~ __ZL17printReplacementsP10objc_classPK21locstamped_category_tj : 1216 -> 1212
~ __ZNK4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI11objc_objectENS1_IPKvNS_15ObjcAssociationENS_17DenseMapValueInfoIS7_EENS_12DenseMapInfoIS6_EENS_6detail12DenseMapPairIS6_S7_EEEENS8_ISF_EENSA_IS4_EENSD_IS4_SF_EEEES4_SF_SG_SH_SI_E22FatalCorruptHashTablesEPKSI_j : 84 -> 88

```
