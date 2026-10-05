## libobjc.A.dylib

> `/usr/lib/libobjc.A.dylib`

```diff

 973.1.0.0.0
-  __TEXT.__text: 0x378b4
+  __TEXT.__text: 0x37944
   __TEXT.__lazy_helpers: 0xa8
   __TEXT.__objc_methlist: 0x5ec
   __TEXT.__const: 0x4130

   __DATA_CONST.__objc_selrefs: 0x1d0
   __DATA_CONST.__objc_scoffs: 0x28
   __DATA_CONST.__got: 0x60
-  __AUTH_CONST.__const: 0x578
+  __AUTH_CONST.__const: 0x590
   __AUTH_CONST.__objc_const: 0x468
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__auth_got: 0x400

   __DATA.__crash_info: 0x148
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0x8e0
-  __DATA_DIRTY.__bss: 0x11c0
+  __DATA_DIRTY.__data: 0x8d8
+  __DATA_DIRTY.__bss: 0x1400
   __DATA_DIRTY.__common: 0x28
   - /usr/lib/libRosetta.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libobjc-env.dylib
   - /usr/lib/objc/libobjcMsgSend.dylib
   Functions: 867
-  Symbols:   1426
+  Symbols:   1425
   CStrings:  480
 
Symbols:
- __ZZ16get_xprr_versionvE19cached_xprr_version
Functions:
~ _object_setClass : 660 -> 656
~ -[NSObject init] : 4 -> 8
~ __ZN19AutoreleasePoolPage12releaseUntilEPP11objc_object : 304 -> 316
~ __ZN19AutoreleasePoolPage3addEP11objc_object : 356 -> 360
~ __ZL38objc_destructInstance_nonnull_realizedP11objc_object : 168 -> 164
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_E4findERKS5_ : 92 -> 96
~ _objc_autoreleaseReturnValue : 300 -> 312
~ -[NSObject dealloc] : 8 -> 12
~ _objc_loadWeakRetained : 664 -> 676
~ __objc_rootDealloc : 80 -> 84
~ _objc_alloc_init : 72 -> 84
~ _weak_register_no_lock : 380 -> 384
~ _objc_storeWeak : 536 -> 532
~ _weak_unregister_no_lock : 496 -> 500
~ __ZL23callSetWeaklyReferencedP11objc_object : 248 -> 260
~ __ZL17weak_entry_insertP12weak_table_tP12weak_entry_t : 204 -> 208
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPK8method_tPvNS_17DenseMapValueInfoIS5_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S5_EEEES4_S5_S7_S9_SC_E15LookupBucketForIS4_EEbRKT_RPKSC_ : 236 -> 232
~ -[NSObject mutableCopy] : 24 -> 28
~ __ZN13list_array_ttIm15protocol_list_t6RawPtrE12iteratorImplILb0EEC2ENS2_12ListIteratorES5_ : 356 -> 352
~ -[NSObject copy] : 28 -> 16
~ __ZNK10class_rw_t2roEv : 80 -> 92
~ -[NSObject autorelease] : 12 -> 16
~ -[NSObject isProxy] : 8 -> 20
~ +[NSObject allocWithZone:] : 4 -> 8
~ _lookUpImpOrNilTryCache : 256 -> 252
~ +[NSObject resolveInstanceMethod:] : 12 -> 16
~ _objc_copyWeak : 64 -> 76
~ __ZL15append_referrerP12weak_entry_tPP11objc_object : 392 -> 380
~ _objc_destroyWeak : 268 -> 264
~ _weak_clear_no_lock : 392 -> 396
~ -[NSObject hash] : 8 -> 4
~ __ZL20grow_refs_and_insertP12weak_entry_tPP11objc_object : 268 -> 272
~ _objc_getAssociatedObject : 368 -> 364
~ __ZN11objc_object16rootAutorelease2Ev : 136 -> 140
~ __ZL19namedClassTableHashPKc : 152 -> 148
~ +[NSObject isSubclassOfClass:] : 84 -> 88
~ _sel_registerName : 16 -> 12
~ +[NSObject self] : 16 -> 4
~ _class_respondsToSelector : 20 -> 16
~ +[NSObject isProxy] : 8 -> 12
~ _objc_opt_new : 108 -> 104
~ +[NSObject class] : 12 -> 16
~ _objc_opt_class : 152 -> 148
~ __ZNK11objc_object24sidetable_isDeallocatingEv : 128 -> 116
~ __ZN4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrIK11objc_objectEmN12_GLOBAL__N_125RefcountMapValuePurgeableENS_12DenseMapInfoIS5_EENS_6detail12DenseMapPairIS5_mEEEES5_mS7_S9_SC_E20InsertIntoBucketImplIS5_EEPSC_RKS5_RKT_SG_ : 196 -> 208
~ __ZNK11objc_object14sidetable_lockEv : 68 -> 72
~ -[NSObject methodForSelector:] : 76 -> 72
~ +[NSObject instanceMethodForSelector:] : 56 -> 60
~ _objc_sync_nil : 12 -> 8
~ +[NSObject instancesRespondToSelector:] : 20 -> 24
~ __method_getImplementationAndName : 204 -> 200
~ +[NSObject isEqual:] : 12 -> 16
~ _sel_hash : 16 -> 12
~ +[NSObject hash] : 4 -> 8
~ _sel_getUid : 16 -> 12
~ __ZN19AutoreleasePoolPage19autoreleaseFullPageEP11objc_objectPS_ : 212 -> 200
~ _objc_opt_isKindOfClass : 212 -> 208
~ -[NSObject retainCount] : 12 -> 16
~ __ZN7cache_t13collectNolockEb : 476 -> 488
~ +[NSObject isMemberOfClass:] : 32 -> 20
~ _protocol_getName : 28 -> 20
~ __ZN10protocol_t13demangledNameEv : 132 -> 124
~ __ZL13SkipFirstTypePKc : 212 -> 208
~ __ZL11static_initv : 228 -> 232
~ _map_images_nolock : 8296 -> 8328
~ __ZNK11header_info9classlistEPm : 148 -> 144
~ __ZL24hasSignedClassROPointersPK14mach_header_64P29_dyld_section_location_info_s : 96 -> 100
~ __ZL12allocBucketsj : 88 -> 96
~ __ZL9protocolsv : 192 -> 200
~ _objc_opt_self : 44 -> 40
~ __ZL11weak_resizeP12weak_table_tm : 188 -> 192
~ _CALLING_SOME_+initialize_METHOD : 36 -> 32
~ +[NSObject initialize] : 8 -> 12
~ ____ZL17addMethods_finishP10objc_classP13method_list_t_block_invoke : 44 -> 56
~ +[NSObject resolveClassMethod:] : 12 -> 16
~ __ZN4objc7Scanner13isSwiftObjectEP10objc_class : 108 -> 104
~ +[NSObject retain] : 4 -> 8
~ _objc_getClass : 16 -> 12
~ +[NSObject superclass] : 40 -> 44
~ __ZN11objc_object21rootRelease_underflowEb : 592 -> 584
~ __ZL11getProtocolPKc : 152 -> 144
~ _method_getReturnType : 156 -> 168
~ +[NSObject respondsToSelector:] : 16 -> 20
~ __ZL33objc_initializeClassPair_internalP10objc_classPKcS0_S0_ : 1500 -> 1496
~ __ZL27_allocateTrampolinesAndDatav : 524 -> 512
~ __ZNK4objc12DenseMapBaseINS_8DenseMapIPK8method_tP23objc_method_descriptionNS_17DenseMapValueInfoIS6_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S6_EEEES4_S6_S8_SA_SD_E15LookupBucketForIS4_EEbRKT_RPKSD_ : 232 -> 244
~ +[NSObject isKindOfClass:] : 80 -> 84
~ __ZNK4objc12DenseMapBaseINS_8DenseMapI12DisguisedPtrI10objc_classES4_NS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS4_EENS_6detail12DenseMapPairIS4_S4_EEEES4_S4_S6_S8_SB_E15LookupBucketForIS4_EEbRKT_RPKSB_ : 236 -> 232
~ +[NSObject new] : 80 -> 68
~ __ZNSt3__118__stable_sort_moveINS_17_ClassicAlgPolicyERN8method_t16SortBySELAddressEPNS2_9bigSignedEEEvT1_S7_T0_NS_15iterator_traitsIS7_E15difference_typeEPNSA_10value_typeE : 984 -> 996
~ +[NSObject performSelector:] : 80 -> 68
~ ____ZZL16attachCategoriesP10objc_classPK21locstamped_category_tjS0_iENK3$_0clEPZL16attachCategoriesS0_S3_jS0_iE5Listsb_block_invoke : 52 -> 48
~ +[NSObject release] : 12 -> 16
~ __ZN10objc_class37installMangledNameForLazilyNamedClassEv : 420 -> 416
~ __ZL25pageAndIndexContainingIMPPFvvEPm : 216 -> 204
~ -[NSObject debugDescription] : 20 -> 12
~ __ZL13fixupProtocolP10protocol_tjbU13block_pointerFvjE : 1264 -> 1272
~ __ZL23fixupProtocolMethodListP10protocol_tP13method_list_tbbbPPP13objc_selector : 592 -> 588
~ +[NSObject performSelector:withObject:] : 84 -> 88
~ _protocol_copyProtocolList : 416 -> 428
~ +[NSObject copyWithZone:] : 16 -> 4
~ _NXMapKeyCopyingInsert : 252 -> 248
~ __headerForAddress : 180 -> 184
~ _property_getAttributes : 8 -> 20
~ __ZNK19AutoreleasePoolPage10busted_dieEv : 40 -> 44
~ _objc_addLoadImageFunc : 288 -> 300
~ _objc_weak_error : 4 -> 8
~ __ZL13weakTableScanv : 360 -> 356
~ _objc_autoreleaseNoPool : 8 -> 12
~ _objc_autoreleasePoolInvalid : 12 -> 8
~ __ZNK11objc_object21sidetable_retainCountEv : 208 -> 212
~ -[__NSUnrecognizedTaggedPointer autorelease] : 8 -> 4
~ +[NSObject forwardInvocation:] : 76 -> 80
~ -[NSObject forwardInvocation:] : 76 -> 72
~ +[NSObject description] : 12 -> 16
~ -[NSObject description] : 8 -> 20
~ __ZNK19AutoreleasePoolPage6bustedIPFvPKczEEEvT_ : 152 -> 156
~ __ZNK4objc12DenseMapBaseINS_13SmallDenseMapIPKvNS_15ObjcAssociationELj1ENS_17DenseMapValueInfoIS4_EENS_12DenseMapInfoIS3_EENS_6detail12DenseMapPairIS3_S4_EEEES3_S4_S6_S8_SB_E22FatalCorruptHashTablesEPKSB_j : 104 -> 100
~ __ZL22defaultBadAllocHandlerP10objc_class : 40 -> 44
~ __ZL18startWeakTableScanv : 120 -> 132
~ +[NSObject doesNotRecognizeSelector:] : 68 -> 72
~ -[NSObject doesNotRecognizeSelector:] : 80 -> 76
~ +[NSObject methodSignatureForSelector:] : 28 -> 32
```
