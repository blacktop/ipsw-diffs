## libobjc.A.dylib

> `/usr/lib/libobjc.A.dylib`

```diff

 973.2.0.0.0
-  __TEXT.__text: 0x37974
+  __TEXT.__text: 0x37a04
   __TEXT.__lazy_helpers: 0xa8
   __TEXT.__objc_methlist: 0x5ec
   __TEXT.__const: 0x4130
Symbols:
+ _os_unfair_recursive_lock_lock
- _os_unfair_recursive_lock_lock_with_options
Functions:
~ _objc_retainAutoreleasedReturnValue : 144 -> 152
~ __objc_rootAllocWithZone : 280 -> 272
~ __ZN19AutoreleasePoolPage3addEP11objc_object : 360 -> 352
~ _objc_destructInstance : 72 -> 68
~ __object_remove_associations : 1124 -> 1128
~ __ZL38objc_destructInstance_nonnull_realizedP11objc_object : 164 -> 156
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_E4findERKS5_ : 96 -> 104
~ _class_createInstance : 288 -> 280
~ _object_getIndexedIvars : 188 -> 196
~ _objc_lookUpImpOrForward : 792 -> 784
~ __ZNK8method_t3impEb : 296 -> 288
~ __objc_sync_enter_kind : 124 -> 120
~ _objc_sync_exit : 188 -> 192
~ _objc_sync_enter : 40 -> 36
~ __ZL11fetch_cacheb : 272 -> 268
~ _weak_unregister_no_lock : 500 -> 488
~ __ZN12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEE8lockWithERS3_ : 196 -> 192
~ __ZL17weak_entry_insertP12weak_table_tP12weak_entry_t : 208 -> 212
~ __ZN12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEE10unlockWithERS3_ : 136 -> 132
~ -[NSObject mutableCopy] : 24 -> 16
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12iteratorImplILb0EE14skipEmptyListsEv : 500 -> 508
~ -[NSObject class] : 12 -> 4
~ __ZL34protocol_conformsToProtocol_nolockP10protocol_tS0_ : 240 -> 232
~ _object_getClass : 136 -> 144
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12iteratorImplILb0EEC2ENS2_12ListIteratorES5_ : 356 -> 364
~ -[NSObject copy] : 28 -> 20
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12ListIteratorC2ERKS3_ : 88 -> 84
~ _objc_setProperty_nonatomic_copy : 104 -> 108
~ _class_getName : 36 -> 28
~ __ZL27object_cxxDestructFromClassP11objc_objectP10objc_class : 208 -> 200
~ _lookupMethodInClassAndLoadCache : 304 -> 312
~ _object_isClass : 32 -> 40
~ _lookUpImpOrNilTryCache : 252 -> 260
~ +[NSObject resolveInstanceMethod:] : 16 -> 8
~ _lookUpImpOrForwardTryCache : 264 -> 272
~ __ZL20grow_refs_and_insertP12weak_entry_tPP11objc_object : 272 -> 280
~ _objc_getAssociatedObject : 364 -> 356
~ _object_cxxConstructFromClass : 312 -> 316
~ _objc_getProperty : 200 -> 196
~ _look_up_class : 476 -> 468
~ _objc_lookUpClass : 12 -> 20
~ __ZL10remapClassP10objc_class : 208 -> 200
~ _sel_registerName : 12 -> 20
~ +[NSObject self] : 4 -> 12
~ __ZL18__sel_registerNamePKcbb : 384 -> 376
~ _objc_allocWithZone : 52 -> 44
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12iteratorImplILb0EEppEv : 728 -> 720
~ +[NSObject isProxy] : 12 -> 20
~ _objc_setAssociatedObject : 1580 -> 1572
~ __ZNK11objc_object24sidetable_isDeallocatingEv : 116 -> 120
~ _objc_setProperty_atomic_copy : 196 -> 192
~ _objc_storeWeakOrNil : 540 -> 532
~ _objc_sync_nil : 8 -> 16
~ +[NSObject instancesRespondToSelector:] : 20 -> 28
~ _method_getImplementation : 40 -> 48
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_EixEOS5_ : 96 -> 104
~ _method_getTypeEncoding : 36 -> 28
~ _objc_exception_throw : 524 -> 516
~ __method_getImplementationAndName : 204 -> 212
~ +[NSObject isEqual:] : 12 -> 20
~ _sel_hash : 12 -> 20
~ +[NSObject hash] : 8 -> 16
~ _sel_getUid : 12 -> 20
~ __ZN19AutoreleasePoolPage19autoreleaseFullPageEP11objc_objectPS_ : 200 -> 208
~ _class_copyProtocolList : 1076 -> 1088
~ _objc_setProperty_atomic : 228 -> 240
~ -[NSObject retainCount] : 16 -> 4
~ _objc_setProperty_nonatomic : 120 -> 116
~ __ZNK11objc_object16sidetable_unlockEv : 64 -> 56
~ __ZN4objc12DenseMapBaseINS_8DenseMapIPKcNS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_SB_E11try_emplaceIJRS5_EEENSt3__14pairINS_16DenseMapIteratorIS3_S5_S7_S9_SB_Lb0EEEbEERKS3_DpOT_ : 296 -> 304
~ ___objc_personality_v0 : 188 -> 196
~ _class_getInstanceMethod : 284 -> 292
~ -[NSObject retain] : 8 -> 16
~ __Z18protocol_getMethodP10protocol_tP13objc_selectorbbb : 316 -> 308
~ -[NSObject allowsWeakReference] : 44 -> 36
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPKcNS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_SB_E15LookupBucketForIS3_EEbRKT_RPKSB_ : 296 -> 304
~ -[NSObject performSelector:] : 72 -> 80
~ __ZNK13list_array_ttI10property_t15property_list_t6RawPtrE5beginEv : 516 -> 508
~ __objc_rootTryRetain : 136 -> 144
~ _protocol_copyMethodDescriptionList : 660 -> 652
~ __ZN15entsize_list_ttI8method_t13method_list_tLj4294901763ENS0_16pointer_modifierEE3endEv : 104 -> 96
~ _sel_isEqual : 20 -> 12
~ __ZL25getMethodFromRelativeListP20relative_list_list_tI13method_list_tEP13objc_selector : 1668 -> 1660
~ __ZN15entsize_list_ttI10property_t15property_list_tLj0E18PointerModifierNopE3endEv : 72 -> 80
~ _object_getIvar : 116 -> 124
~ __class_getVariable : 268 -> 260
~ _method_getNumberOfArguments : 168 -> 172
~ __ZL13SkipFirstTypePKc : 208 -> 220
~ _map_images : 300 -> 304
~ _map_images_nolock : 8320 -> 8332
~ __ZNK11header_info9classlistEPm : 152 -> 140
~ __ZL24hasSignedClassROPointersPK14mach_header_64P29_dyld_section_location_info_s : 92 -> 88
~ __ZL12allocBucketsj : 92 -> 100
~ __ZL9protocolsv : 188 -> 196
~ __ZNK11header_info9nlclslistEPm : 140 -> 148
~ __ZL20classSlotForTagIndex16objc_tag_index_t : 116 -> 108
~ __ZL33realizeClassMaybeSwiftMaybeRelockP10objc_classR12locker_mixinIN9lockdebug10lock_mixinI16objc_lock_base_tEEEb : 540 -> 532
~ __ZN4objc7Scanner18scanAddedClassImplEP10objc_classNS0_11metaclass_tE : 2372 -> 2380
~ __ZN7cache_t26maybeConvertToPreoptimizedEv : 324 -> 332
~ __ZN23tls_autoptr_direct_implI18_objc_pthread_dataL7tls_key0EE5dtor_EPv : 152 -> 144
~ _method_copyReturnType : 120 -> 124
~ __ZL12SubtypeUntilPKcc : 148 -> 152
~ _sel_lookUpByName : 264 -> 272
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE11attachListsEPKPS0_jbPKc : 1220 -> 1228
~ __ZL27internal_class_getImageNameP10objc_classPPKc : 60 -> 52
~ __ZN7cache_t11eraseNolockEPKc : 532 -> 524
~ __ZN4objc7Scanner13isSwiftObjectEP10objc_class : 104 -> 96
~ +[NSObject retain] : 8 -> 16
~ _objc_getClass : 12 -> 20
~ +[NSObject superclass] : 44 -> 36
~ __ZN4objc12DenseMapBaseINS_8DenseMapIPKcNS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS4_12DenseSetPairIS3_EEEES3_S5_S7_S9_SB_E4findES3_ : 124 -> 116
~ __ZN11objc_object21rootRelease_underflowEb : 580 -> 588
~ __ZL11getProtocolPKc : 148 -> 140
~ -[NSObject performSelector:withObject:] : 96 -> 84
~ _encoding_getArgumentInfo : 420 -> 416
~ _objc_moveWeak : 272 -> 264
~ _class_replaceMethod : 316 -> 324
~ __ZL11flushCachesP10objc_classPKcU13block_pointerFbS0_E : 252 -> 244
~ _class_addMethod : 244 -> 252
~ __ZZL22load_categories_nolockP11header_infoENK3$_0clEPKP10category_tb : 972 -> 984
~ __ZL19schedule_class_loadP10objc_class : 340 -> 336
~ __ZN10objc_class13getLoadMethodEv : 3204 -> 3212
~ __ZN4objc7Scanner17scanChangedMethodEP10objc_classPK8method_t : 876 -> 868
~ __ZL33objc_initializeClassPair_internalP10objc_classPKcS0_S0_ : 1496 -> 1504
~ __ZL27_allocateTrampolinesAndDatav : 512 -> 520
~ __ZN13list_array_ttI8method_t13method_list_t24method_list_t_authed_ptrE12iteratorImplILb1EEC2ENS3_12ListIteratorES6_ : 744 -> 736
~ __ZNK8method_t20getCachedDescriptionEv : 632 -> 624
~ _method_getDescription : 72 -> 64
~ __ZL13addNamedClassP10objc_classPKcS0_ : 588 -> 580
~ _objc_getProtocol : 180 -> 188
~ __ZNK11header_info7catlistEPm : 140 -> 148
~ __category_getLoadMethod : 1556 -> 1548
~ _objc_getFutureClass : 584 -> 576
~ ____ZL13setSuperclassP10objc_classS0__block_invoke : 16 -> 12
~ __ZN17loadImageCallbackaSERKS_ : 136 -> 140
~ _class_setVersion : 280 -> 288
~ __ZN4objc8DenseMapI12DisguisedPtrI10objc_classEP17PendingInitializeNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S5_EEE4initEj : 224 -> 216
~ __objc_getClassForTag : 68 -> 60
~ __ZN10objc_class11mangledNameEv : 84 -> 76
~ _property_copyAttributeValue : 260 -> 268
~ _gdb_objc_class_changed : 8 -> 16
~ _class_copyIvarList : 412 -> 420
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_E4growEj : 428 -> 436
~ _property_copyAttributeList : 408 -> 400
~ __ZL9readClassP10objc_classbb : 1436 -> 1444
~ _objc_readClassPair : 612 -> 604
~ __ZNSt3__113__stable_sortINS_17_ClassicAlgPolicyERN8method_t16SortBySELAddressEPNS2_9bigSignedEEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEPNSA_10value_typeEl : 1528 -> 1536
~ ____class_setCustomDeallocInitiation_block_invoke : 24 -> 32
~ _class_initialize : 100 -> 108
~ _protocol_conformsToProtocol : 188 -> 196
~ ____ZN4objc7Scanner20propagateCustomFlagsEP10objc_classjNS0_11inherited_tE_block_invoke : 460 -> 452
~ __ZL10addMethodsP10objc_classPKP13objc_selectorPKPFvvEPPKcjbPj : 684 -> 692
~ -[NSObject self] : 4 -> 12
~ _class_addMethodsBulk : 312 -> 320
~ __ZN13method_list_t16sortBySELAddressEv : 428 -> 436
~ _protocol_isEqual : 108 -> 100
~ __ZN4objc8DenseMapIPK8method_tP23objc_method_descriptionNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S5_EEE4growEj : 432 -> 436
~ -[Protocol isEqual:] : 172 -> 168
~ __ZL16addRemappedClassP10objc_classS0_ : 444 -> 452
~ __ZL13remapClassRefPP10objc_classjbU13block_pointerFvjE : 484 -> 492
~ __ZL25pageAndIndexContainingIMPPFvvEPm : 216 -> 208
~ _method_exchangeImplementations : 856 -> 864
~ __ZN4objc8DenseMapIPK8method_tPvNS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S4_EEE4growEj : 444 -> 452
~ __objc_beginClassEnumeration : 468 -> 476
~ _objc_claimAutoreleasedReturnValue : 124 -> 132
~ __objc_enumerateNextClass : 564 -> 572
~ _object_getInstanceVariable : 128 -> 136
~ __ZN4objc8DenseMapIPKcNS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS2_EENS3_12DenseSetPairIS2_EEE4growEj : 440 -> 448
~ __ZL12_NXMapRehashP11_NXMapTable : 232 -> 224
~ __ZL27namedClassTableHashCallbackP11_NXMapTablePKv : 8 -> 16
~ -[NSObject isFault] : 16 -> 8
~ _object_dispose : 68 -> 76
~ -[NSObject debugDescription] : 24 -> 16
~ __ZL23fixupProtocolMethodListP10protocol_tP13method_list_tbbbPPP13objc_selector : 584 -> 592
~ +[NSObject performSelector:withObject:] : 84 -> 92
~ _protocol_copyProtocolList : 416 -> 424
~ +[NSObject copyWithZone:] : 4 -> 8
~ -[Protocol hash] : 12 -> 16
~ _method_setImplementation : 452 -> 444
~ __ZN19AutoreleasePoolPage12popPageDebugEPvPS_PP11objc_object : 264 -> 256
~ _sel_getName : 28 -> 24
~ _objc_copyCppObjectAtomic : 144 -> 132
~ _protocol_getProperty : 244 -> 236
~ __objc_deallocOnMainThreadHelper : 24 -> 16
~ _objc_removeAssociatedObjects : 40 -> 48
~ __ZL11_mapPtrHashP11_NXMapTablePKv : 16 -> 20
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI11objc_objectENS_13SmallDenseMapIPKvNS_15ObjcAssociationELj1ENS_17DenseMapValueInfoIS8_EENS_12DenseMapInfoIS7_EENS_6detail12DenseMapPairIS7_S8_EEEENS9_ISG_EENSB_IS4_EENSE_IS4_SG_EEEES4_SG_SH_SI_SJ_E5eraseENS_16DenseMapIteratorIS4_SG_SH_SI_SJ_Lb0EEE : 332 -> 336
~ ____ZL13setSuperclassP10objc_classS0__block_invoke.204 : 12 -> 8
~ __ZN4objc8DenseMapI12DisguisedPtrI11objc_objectENS_13SmallDenseMapIPKvNS_15ObjcAssociationELj1ENS_17DenseMapValueInfoIS7_EENS_12DenseMapInfoIS6_EENS_6detail12DenseMapPairIS6_S7_EEEENS8_ISF_EENSA_IS3_EENSD_IS3_SF_EEE4growEj : 524 -> 528
~ _class_getVersion : 140 -> 132
~ __ZL12_objc_fatalvyyPKcPc : 160 -> 168
~ __ZNK4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classENS_6detail13DenseSetEmptyENS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS4_EENS5_12DenseSetPairIS4_EEEES4_S6_S8_SA_SC_E15LookupBucketForIS4_EEbRKT_RPKSC_ : 224 -> 232
~ __ZN10objc_class14nameForLoggingEv : 400 -> 408
~ _property_getAttributes : 8 -> 16
~ __ZNK19AutoreleasePoolPage10busted_dieEv : 40 -> 48
~ _ivar_getOffset : 24 -> 16
~ __ZN19AutoreleasePoolPage18autoreleaseNewPageEP11objc_object : 80 -> 72
~ _method_getName : 152 -> 160
~ -[NSObject performSelector:withObject:withObject:] : 104 -> 96
~ __ZL17realizeAllClassesv : 496 -> 504
~ ____objc_map_images_block_invoke : 4 -> 16
~ _unmap_image : 1736 -> 1732
~ _protocol_addProperty : 624 -> 616
~ ___copy_helper_block_e8_32c49_ZTSKZL33objc_copyRealizedClassList_nolockPjE3$_1 : 12 -> 20
~ __objc_endClassEnumeration : 28 -> 36
~ __ZL35foreach_realized_class_and_subclassP10objc_classU13block_pointerFbS0_E : 172 -> 180
~ _gdb_object_getClass : 136 -> 128
~ ___copy_helper_block_e8_32c69_ZTSKZN10objc_class39setDisallowPreoptInlinedSelsRecursivelyEPKcE3$_0 : 24 -> 16
~ __objc_getFreedObjectClass : 12 -> 20
~ ___copy_helper_block_e8_32c67_ZTSKZL25_method_setImplementationP10objc_classP8method_tPFvvEE3$_0 : 20 -> 12
~ __ZNSt3__16vectorIPK14mach_header_64NS_9allocatorIS3_EEE24__emplace_back_slow_pathIJS3_EEEPS3_DpOT_ : 212 -> 220
~ ___copy_helper_block_e8_32c60_ZTSKZL17addMethods_finishP10objc_classP13method_list_tE3$_0 : 16 -> 8
~ _sel_isMapped : 276 -> 272
~ __objc_atfork_prepare : 820 -> 816
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPK8method_tP23objc_method_descriptionNS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S6_EEEES4_S6_S8_SA_SD_E22FatalCorruptHashTablesEPKSD_j : 88 -> 96
~ __Z26objc_defaultForwardHandlerP11objc_objectP13objc_selector : 112 -> 108
~ __ZNK4objc12DenseMapBaseINS_13SmallDenseMapIPKvNS_15ObjcAssociationELj1ENS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S4_EEEES3_S4_S6_S8_SB_E22FatalCorruptHashTablesEPKSB_j : 100 -> 96
```
