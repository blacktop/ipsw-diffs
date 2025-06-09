## CoreServicesStore

> `/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore`

```diff

-1378.19.1.0.0
-  __TEXT.__text: 0x2c464
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_methlist: 0x56c
-  __TEXT.__const: 0x204
-  __TEXT.__gcc_except_tab: 0x3b74
-  __TEXT.__cstring: 0x205f
-  __TEXT.__oslogstring: 0x1822
+1420.0.0.0.0
+  __TEXT.__text: 0x2b64c
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0x85c
+  __TEXT.__const: 0x208
+  __TEXT.__gcc_except_tab: 0x3a04
+  __TEXT.__cstring: 0x2018
+  __TEXT.__oslogstring: 0x17d1
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x1140
-  __TEXT.__objc_classname: 0xfe
-  __TEXT.__objc_methname: 0x18a8
-  __TEXT.__objc_methtype: 0x9c1
-  __TEXT.__objc_stubs: 0x1be0
-  __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x9e8
-  __DATA_CONST.__objc_classlist: 0x38
+  __TEXT.__unwind_info: 0x1160
+  __TEXT.__objc_classname: 0x115
+  __TEXT.__objc_methname: 0x1ce0
+  __TEXT.__objc_methtype: 0xb89
+  __TEXT.__objc_stubs: 0x1c00
+  __DATA_CONST.__got: 0x308
+  __DATA_CONST.__const: 0x9c0
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a8
-  __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH_CONST.__const: 0x820
-  __AUTH_CONST.__cfstring: 0x1a60
-  __AUTH_CONST.__objc_const: 0x888
-  __AUTH_CONST.__objc_intobj: 0x780
+  __DATA_CONST.__objc_selrefs: 0x960
+  __DATA_CONST.__objc_superrefs: 0x38
+  __AUTH_CONST.__auth_got: 0x670
+  __AUTH_CONST.__const: 0x800
+  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__objc_const: 0x9b8
+  __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x190
+  __AUTH.__objc_data: 0x1e0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x5c
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x120
-  __DATA.__bss: 0x558
+  __DATA.__bss: 0x550
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0E0F6347-973D-31F2-8D45-D5E79FC4FD7E
-  Functions: 625
-  Symbols:   2176
-  CStrings:  986
+  UUID: 2BE1B431-B1CF-3252-A832-2200AF217FD9
+  Functions: 658
+  Symbols:   2300
+  CStrings:  1062
 
Symbols:
+ +[CSStoreAttributedStringWriter newWithBuffer:]
+ +[CSStoreAttributedStringWriter newWithStore:buffer:]
+ +[CSStoreAttributedStringWriter new]
+ +[CSStoreAttributedStringWriter separatorForTitle:separator:]
+ -[CSStoreAttributedStringWriter .cxx_construct]
+ -[CSStoreAttributedStringWriter .cxx_destruct]
+ -[CSStoreAttributedStringWriter attributedString]
+ -[CSStoreAttributedStringWriter beginBitfieldFlags:]
+ -[CSStoreAttributedStringWriter beginFlags:flags:]
+ -[CSStoreAttributedStringWriter childUnit:table:unit:]
+ -[CSStoreAttributedStringWriter childUnit:unit:]
+ -[CSStoreAttributedStringWriter elidesEmptyValues]
+ -[CSStoreAttributedStringWriter endFlags]
+ -[CSStoreAttributedStringWriter flag:name:]
+ -[CSStoreAttributedStringWriter flag:name:color:]
+ -[CSStoreAttributedStringWriter init:outBuffer:]
+ -[CSStoreAttributedStringWriter insertsNewlines]
+ -[CSStoreAttributedStringWriter link:unit:]
+ -[CSStoreAttributedStringWriter link:unit:linkedAttributedText:]
+ -[CSStoreAttributedStringWriter link:unit:linkedText:]
+ -[CSStoreAttributedStringWriter link:unitID:linkedAttributedText:]
+ -[CSStoreAttributedStringWriter linkURL:]
+ -[CSStoreAttributedStringWriter linkURL:linkedAttributedText:]
+ -[CSStoreAttributedStringWriter linkURL:linkedText:]
+ -[CSStoreAttributedStringWriter locale]
+ -[CSStoreAttributedStringWriter missingFlag:name:]
+ -[CSStoreAttributedStringWriter missingFlag:name:color:]
+ -[CSStoreAttributedStringWriter setElidesEmptyValues:]
+ -[CSStoreAttributedStringWriter setInsertsNewlines:]
+ -[CSStoreAttributedStringWriter setLocale:]
+ -[CSStoreAttributedStringWriter setVisualizer:]
+ -[CSStoreAttributedStringWriter visualizer]
+ -[CSStoreAttributedStringWriter withAppliedAttribute:value:block:]
+ -[CSStoreAttributedStringWriter withReferenceToUnit:unit:block:]
+ -[CSStoreAttributedStringWriter withTextColor:backgroundColor:block:]
+ -[CSStoreAttributedStringWriter withTextColor:block:]
+ -[CSStoreAttributedStringWriter withWarningColors:]
+ -[CSStoreAttributedStringWriter write:]
+ -[CSStoreAttributedStringWriter write:args:]
+ -[CSStoreAttributedStringWriter write:array:]
+ -[CSStoreAttributedStringWriter write:arrayID:]
+ -[CSStoreAttributedStringWriter write:arrayIDs:count:]
+ -[CSStoreAttributedStringWriter write:arrayStringID:]
+ -[CSStoreAttributedStringWriter write:attributedString:]
+ -[CSStoreAttributedStringWriter write:bool:]
+ -[CSStoreAttributedStringWriter write:code:]
+ -[CSStoreAttributedStringWriter write:format:]
+ -[CSStoreAttributedStringWriter write:format:args:]
+ -[CSStoreAttributedStringWriter write:interval:]
+ -[CSStoreAttributedStringWriter write:number:]
+ -[CSStoreAttributedStringWriter write:separator:]
+ -[CSStoreAttributedStringWriter write:string:]
+ -[CSStoreAttributedStringWriter write:stringID:]
+ -[CSStoreAttributedStringWriter writeArray:]
+ -[CSStoreAttributedStringWriter writeArrayID:]
+ -[CSStoreAttributedStringWriter writeArrayIDs:count:]
+ -[CSStoreAttributedStringWriter writeAttributedString:]
+ -[CSStoreAttributedStringWriter writeFormat:]
+ -[CSStoreAttributedStringWriter writeLink:unitID:linkedText:]
+ -[CSStoreAttributedStringWriter writeNumber:]
+ -[CSStoreAttributedStringWriter writeSeparator:]
+ -[CSStoreAttributedStringWriter writeSeparator]
+ -[CSStoreAttributedStringWriter writeString:]
+ -[CSStoreAttributedStringWriter writeStringID:]
+ -[_CSVisualizationArchiver .cxx_construct]
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table106
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table117
+ GCC_except_table123
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table15
+ GCC_except_table157
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table165
+ GCC_except_table17
+ GCC_except_table172
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table178
+ GCC_except_table187
+ GCC_except_table19
+ GCC_except_table197
+ GCC_except_table202
+ GCC_except_table204
+ GCC_except_table219
+ GCC_except_table242
+ GCC_except_table244
+ GCC_except_table252
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table259
+ GCC_except_table260
+ GCC_except_table262
+ GCC_except_table263
+ GCC_except_table264
+ GCC_except_table265
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table269
+ GCC_except_table274
+ GCC_except_table276
+ GCC_except_table283
+ GCC_except_table284
+ GCC_except_table285
+ GCC_except_table287
+ GCC_except_table288
+ GCC_except_table305
+ GCC_except_table307
+ GCC_except_table308
+ GCC_except_table309
+ GCC_except_table312
+ GCC_except_table314
+ GCC_except_table315
+ GCC_except_table319
+ GCC_except_table323
+ GCC_except_table329
+ GCC_except_table33
+ GCC_except_table330
+ GCC_except_table343
+ GCC_except_table348
+ GCC_except_table354
+ GCC_except_table36
+ GCC_except_table362
+ GCC_except_table363
+ GCC_except_table364
+ GCC_except_table369
+ GCC_except_table37
+ GCC_except_table372
+ GCC_except_table373
+ GCC_except_table376
+ GCC_except_table396
+ GCC_except_table40
+ GCC_except_table404
+ GCC_except_table406
+ GCC_except_table412
+ GCC_except_table419
+ GCC_except_table422
+ GCC_except_table424
+ GCC_except_table426
+ GCC_except_table427
+ GCC_except_table429
+ GCC_except_table430
+ GCC_except_table431
+ GCC_except_table432
+ GCC_except_table44
+ GCC_except_table447
+ GCC_except_table45
+ GCC_except_table457
+ GCC_except_table461
+ GCC_except_table474
+ GCC_except_table481
+ GCC_except_table482
+ GCC_except_table483
+ GCC_except_table484
+ GCC_except_table491
+ GCC_except_table492
+ GCC_except_table493
+ GCC_except_table494
+ GCC_except_table499
+ GCC_except_table504
+ GCC_except_table506
+ GCC_except_table511
+ GCC_except_table512
+ GCC_except_table514
+ GCC_except_table519
+ GCC_except_table520
+ GCC_except_table522
+ GCC_except_table523
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table554
+ GCC_except_table565
+ GCC_except_table567
+ GCC_except_table591
+ GCC_except_table592
+ GCC_except_table595
+ GCC_except_table597
+ GCC_except_table601
+ GCC_except_table603
+ GCC_except_table611
+ GCC_except_table613
+ GCC_except_table614
+ GCC_except_table617
+ GCC_except_table618
+ GCC_except_table619
+ GCC_except_table620
+ GCC_except_table622
+ GCC_except_table623
+ GCC_except_table624
+ GCC_except_table625
+ GCC_except_table629
+ GCC_except_table632
+ GCC_except_table635
+ GCC_except_table636
+ GCC_except_table639
+ GCC_except_table640
+ GCC_except_table641
+ GCC_except_table642
+ GCC_except_table645
+ GCC_except_table647
+ GCC_except_table650
+ GCC_except_table661
+ GCC_except_table668
+ GCC_except_table673
+ GCC_except_table71
+ GCC_except_table74
+ GCC_except_table75
+ GCC_except_table79
+ GCC_except_table84
+ GCC_except_table85
+ GCC_except_table86
+ GCC_except_table93
+ _OBJC_CLASS_$_CSStoreAttributedStringWriter
+ _OBJC_IVAR_$_CSStoreAttributedStringWriter._attributedString
+ _OBJC_IVAR_$_CSStoreAttributedStringWriter._writer
+ _OBJC_METACLASS_$_CSStoreAttributedStringWriter
+ __CSStoreIsTableBalanced
+ __CSStringGetRetainCount
+ __CSStringIsConst
+ __CSStringIsPacked
+ __OBJC_$_CLASS_METHODS_CSStoreAttributedStringWriter
+ __OBJC_$_INSTANCE_METHODS_CSStoreAttributedStringWriter
+ __OBJC_$_INSTANCE_METHODS__CSVisualizer
+ __OBJC_$_INSTANCE_VARIABLES_CSStoreAttributedStringWriter
+ __OBJC_$_PROP_LIST_CSStoreAttributedStringWriter
+ __OBJC_CLASS_RO_$_CSStoreAttributedStringWriter
+ __OBJC_METACLASS_RO_$_CSStoreAttributedStringWriter
+ __ZNKRSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8nn200100Ev
+ __ZNSt3__110unique_ptrIN8CSStore25StoreENS_14default_deleteIS2_EEE5resetB8nn200100EPS2_
+ __ZNSt3__110unique_ptrIN8CSStore25StoreENS_14default_deleteIS2_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIPKvU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorISA_EEEEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeImU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEED1B8nn200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn200100ILi0EEEPKc
+ __ZNSt3__119__shared_weak_count16__release_sharedB8nn200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEmEEPvEEEEEclB8nn200100EPSB_
+ __ZNSt3__124__put_character_sequenceB8nn200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI8_NSRangeNS_9allocatorIS1_EEE9push_backB8nn200100ERKS1_
+ __ZNSt3__16vectorIN8CSStore27HashMapIjNS1_17_StringCacheEntryENS1_16_StringFunctionsELy0EE12KeyValuePairENS_9allocatorIS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN8CSStore27HashMapIjNS1_17_StringCacheEntryENS1_16_StringFunctionsELy0EE12KeyValuePairENS_9allocatorIS6_EEE9push_backB8nn200100ERKS6_
+ __ZNSt3__16vectorIN8CSStore27HashMapIjjNS1_10Dictionary10_FunctionsELy0EE12KeyValuePairENS_9allocatorIS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN8CSStore27HashMapIjjNS1_10Dictionary10_FunctionsELy0EE12KeyValuePairENS_9allocatorIS6_EEE9push_backB8nn200100ERKS6_
+ __ZNSt3__16vectorIN8CSStore27HashMapIjjNS1_20_IdentifierFunctionsELy1EE12KeyValuePairENS_9allocatorIS5_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN8CSStore27HashMapIjjNS1_20_IdentifierFunctionsELy1EE12KeyValuePairENS_9allocatorIS5_EEE9push_backB8nn200100ERKS5_
+ __ZNSt3__16vectorINS0_IN8CSStore27HashMapIjNS1_17_StringCacheEntryENS1_16_StringFunctionsELy0EE12KeyValuePairENS_9allocatorIS6_EEEENS7_IS9_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS0_IN8CSStore27HashMapIjjNS1_10Dictionary10_FunctionsELy0EE12KeyValuePairENS_9allocatorIS6_EEEENS7_IS9_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS0_IN8CSStore27HashMapIjjNS1_20_IdentifierFunctionsELy1EE12KeyValuePairENS_9allocatorIS5_EEEENS6_IS8_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairIP8NSStringP11objc_objectEENS_9allocatorIS8_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__19allocatorI8_NSRangeE17allocate_at_leastB8nn200100Em
+ __ZNSt3__19allocatorIjE17allocate_at_leastB8nn200100Em
+ __ZNSt3__19allocatorImE17allocate_at_leastB8nn200100Em
+ __ZNSt3__19allocatorItE17allocate_at_leastB8nn200100Em
+ __ZNSt3__1ssB8nn200100IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
+ __ZSt28__throw_bad_array_new_lengthB8nn200100v
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZZN8CSStore2L15IsAppleInternalEvE4once.168
+ __ZZN8CSStore2L15IsAppleInternalEvE6result.169
+ __ZZN8CSStore2L6getLogEvE4once.519
+ __ZZN8CSStore2L6getLogEvE6result.521
+ ___Block_byref_object_copy_.114
+ ___Block_byref_object_copy_.214
+ ___Block_byref_object_copy_.242
+ ___Block_byref_object_copy_.369
+ ___Block_byref_object_copy_.761
+ ___Block_byref_object_dispose_.115
+ ___Block_byref_object_dispose_.215
+ ___Block_byref_object_dispose_.243
+ ___Block_byref_object_dispose_.370
+ ___Block_byref_object_dispose_.762
+ ____ZN8CSStore2L15IsAppleInternalEv_block_invoke.171
+ ____ZN8CSStore2L6getLogEv_block_invoke.530
+ ___block_literal_global.120
+ ___block_literal_global.165
+ ___block_literal_global.199
+ ___block_literal_global.247
+ ___block_literal_global.273
+ ___block_literal_global.405
+ ___block_literal_global.41
+ ___block_literal_global.520
+ ___block_literal_global.777
+ ___block_literal_global.813
+ ___destroy_helper_block_ea8_32.219
+ ___destroy_helper_block_ea8_32.389
+ ___destroy_helper_block_ea8_32.605
+ _objc_msgSend$init:outBuffer:
- -[_CSVisualizer(Deprecated) handlerForTable:]
- -[_CSVisualizer(Deprecated) initWithStore:useStandardTableHandlers:]
- -[_CSVisualizer(Deprecated) setHandler:forTable:]
- -[_CSVisualizer(Deprecated) setStandardTableHandlers]
- GCC_except_table102
- GCC_except_table109
- GCC_except_table114
- GCC_except_table115
- GCC_except_table119
- GCC_except_table120
- GCC_except_table121
- GCC_except_table125
- GCC_except_table127
- GCC_except_table129
- GCC_except_table133
- GCC_except_table135
- GCC_except_table136
- GCC_except_table14
- GCC_except_table140
- GCC_except_table141
- GCC_except_table144
- GCC_except_table146
- GCC_except_table147
- GCC_except_table148
- GCC_except_table153
- GCC_except_table16
- GCC_except_table164
- GCC_except_table169
- GCC_except_table171
- GCC_except_table177
- GCC_except_table18
- GCC_except_table180
- GCC_except_table186
- GCC_except_table194
- GCC_except_table195
- GCC_except_table196
- GCC_except_table199
- GCC_except_table203
- GCC_except_table206
- GCC_except_table207
- GCC_except_table208
- GCC_except_table211
- GCC_except_table212
- GCC_except_table214
- GCC_except_table215
- GCC_except_table216
- GCC_except_table217
- GCC_except_table220
- GCC_except_table223
- GCC_except_table225
- GCC_except_table226
- GCC_except_table227
- GCC_except_table231
- GCC_except_table232
- GCC_except_table237
- GCC_except_table238
- GCC_except_table240
- GCC_except_table245
- GCC_except_table256
- GCC_except_table261
- GCC_except_table27
- GCC_except_table272
- GCC_except_table278
- GCC_except_table28
- GCC_except_table281
- GCC_except_table290
- GCC_except_table292
- GCC_except_table306
- GCC_except_table311
- GCC_except_table321
- GCC_except_table325
- GCC_except_table326
- GCC_except_table328
- GCC_except_table334
- GCC_except_table338
- GCC_except_table345
- GCC_except_table349
- GCC_except_table35
- GCC_except_table359
- GCC_except_table368
- GCC_except_table374
- GCC_except_table38
- GCC_except_table380
- GCC_except_table382
- GCC_except_table385
- GCC_except_table388
- GCC_except_table390
- GCC_except_table391
- GCC_except_table392
- GCC_except_table395
- GCC_except_table403
- GCC_except_table41
- GCC_except_table417
- GCC_except_table42
- GCC_except_table420
- GCC_except_table428
- GCC_except_table435
- GCC_except_table440
- GCC_except_table441
- GCC_except_table443
- GCC_except_table450
- GCC_except_table451
- GCC_except_table452
- GCC_except_table453
- GCC_except_table458
- GCC_except_table462
- GCC_except_table463
- GCC_except_table467
- GCC_except_table470
- GCC_except_table478
- GCC_except_table479
- GCC_except_table50
- GCC_except_table508
- GCC_except_table51
- GCC_except_table510
- GCC_except_table515
- GCC_except_table516
- GCC_except_table517
- GCC_except_table521
- GCC_except_table525
- GCC_except_table527
- GCC_except_table528
- GCC_except_table529
- GCC_except_table539
- GCC_except_table540
- GCC_except_table549
- GCC_except_table550
- GCC_except_table553
- GCC_except_table555
- GCC_except_table556
- GCC_except_table557
- GCC_except_table558
- GCC_except_table568
- GCC_except_table572
- GCC_except_table575
- GCC_except_table576
- GCC_except_table577
- GCC_except_table578
- GCC_except_table580
- GCC_except_table583
- GCC_except_table584
- GCC_except_table587
- GCC_except_table590
- GCC_except_table604
- GCC_except_table605
- GCC_except_table606
- GCC_except_table607
- GCC_except_table615
- GCC_except_table63
- GCC_except_table633
- GCC_except_table637
- GCC_except_table638
- GCC_except_table64
- GCC_except_table67
- GCC_except_table70
- GCC_except_table73
- GCC_except_table76
- GCC_except_table95
- GCC_except_table98
- GCC_except_table99
- __OBJC_$_INSTANCE_METHODS__CSVisualizer(Deprecated)
- __ZL13GetContextLogv
- __ZN8CSStore222AttributedStringWriter10beginFlagsEP8NSStringm
- __ZN8CSStore222AttributedStringWriter11stringArrayEPKjj
- __ZN8CSStore222AttributedStringWriter11stringArrayEj
- __ZN8CSStore222AttributedStringWriter12fourCharCodeEP8NSStringj
- __ZN8CSStore222AttributedStringWriter13setVisualizerEP13_CSVisualizer
- __ZN8CSStore222AttributedStringWriter18beginBitfieldFlagsEP8NSString
- __ZN8CSStore222AttributedStringWriter18setInsertsNewlinesEb
- __ZN8CSStore222AttributedStringWriter20setElidesEmptyValuesEb
- __ZN8CSStore222AttributedStringWriter4Impl12createMarkerEP18NSAttributedString
- __ZN8CSStore222AttributedStringWriter4Impl13kMarkerLengthE
- __ZN8CSStore222AttributedStringWriter4ImplC1EPK9__CSStoreP25NSMutableAttributedString
- __ZN8CSStore222AttributedStringWriter4ImplC2EPK9__CSStoreP25NSMutableAttributedString
- __ZN8CSStore222AttributedStringWriter5arrayEP7NSArray
- __ZN8CSStore222AttributedStringWriter6stringEj
- __ZN8CSStore222AttributedStringWriter8endFlagsEv
- __ZN8CSStore222AttributedStringWriter9childUnitEjj
- __ZN8CSStore222AttributedStringWriter9setLocaleEP8NSLocale
- __ZN8CSStore222AttributedStringWriter9timestampEP8NSStringd
- __ZN8CSStore222AttributedStringWriterC1ERKS0_
- __ZN8CSStore222AttributedStringWriterC2EPK9__CSStoreP25NSMutableAttributedString
- __ZN8CSStore222AttributedStringWriterC2ERKS0_
- __ZN8CSStore222AttributedStringWriteraSERKS0_
- __ZNK8CSStore222AttributedStringWriter13getVisualizerEv
- __ZNK8CSStore222AttributedStringWriter15insertsNewlinesEv
- __ZNK8CSStore222AttributedStringWriter17elidesEmptyValuesEv
- __ZNK8CSStore222AttributedStringWriter4Impl16getDateFormatterEv
- __ZNK8CSStore222AttributedStringWriter4Impl26getDateComponentsFormatterEv
- __ZNK8CSStore222AttributedStringWriter4Impl8getStoreEv
- __ZNK8CSStore222AttributedStringWriter9getLocaleEv
- __ZNKSt3__114default_deleteIN8CSStore25StoreEEclB8nn190102EPS2_
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
- __ZNKSt3__14lessINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn190102ERKS6_S9_
- __ZNSt3__110unique_ptrIN8CSStore25StoreENS_14default_deleteIS2_EEE5resetB8nn190102EPS2_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIPKvU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorISA_EEEEE5resetB8nn190102EPSA_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeImU8__strongP8NSStringEEPvEENS_22__hash_node_destructorINS_9allocatorIS8_EEEEE5resetB8nn190102EPS8_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImU8__strongP8NSStringEENS_22__unordered_map_hasherImS5_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE27__node_insert_multi_performEPNS_11__hash_nodeIS5_PvEEPNS_16__hash_node_baseISK_EE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImU8__strongP8NSStringEENS_22__unordered_map_hasherImS5_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE27__node_insert_multi_prepareEmRS5_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImU8__strongP8NSStringEENS_22__unordered_map_hasherImS5_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS5_SA_S8_Lb1EEENS_9allocatorIS5_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImjEENS_22__unordered_map_hasherImS2_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE27__node_insert_multi_performEPNS_11__hash_nodeIS2_PvEEPNS_16__hash_node_baseISH_EE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImjEENS_22__unordered_map_hasherImS2_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE27__node_insert_multi_prepareEmRS2_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeImjEENS_22__unordered_map_hasherImS2_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS2_S7_S5_Lb1EEENS_9allocatorIS2_EEE8__rehashILb1EEEvm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ILi0EEEPKc
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI8_NSRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN8CSStore27HashMapIjNS2_17_StringCacheEntryENS2_16_StringFunctionsELy0EE12KeyValuePairEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN8CSStore27HashMapIjjNS2_10Dictionary10_FunctionsELy0EE12KeyValuePairEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN8CSStore27HashMapIjjNS2_20_IdentifierFunctionsELy1EE12KeyValuePairEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_4pairIP8NSStringP11objc_objectEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorItEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__shared_weak_count16__release_sharedB8nn190102Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn190102Ev
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEmEEPvEEEEEclB8nn190102EPSB_
- __ZNSt3__124__put_character_sequenceB8nn190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__16vectorINS0_IN8CSStore27HashMapIjNS1_17_StringCacheEntryENS1_16_StringFunctionsELy0EE12KeyValuePairENS_9allocatorIS6_EEEENS7_IS9_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS0_IN8CSStore27HashMapIjjNS1_10Dictionary10_FunctionsELy0EE12KeyValuePairENS_9allocatorIS6_EEEENS7_IS9_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS0_IN8CSStore27HashMapIjjNS1_20_IdentifierFunctionsELy1EE12KeyValuePairENS_9allocatorIS5_EEEENS6_IS8_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS_4pairIP8NSStringP11objc_objectEENS_9allocatorIS8_EEE11__vallocateB8nn190102Em
- __ZSt28__throw_bad_array_new_lengthB8nn190102v
- __ZZL13GetContextLogvE4once
- __ZZL13GetContextLogvE6result
- __ZZN8CSStore2L15IsAppleInternalEvE4once.118
- __ZZN8CSStore2L15IsAppleInternalEvE6result.119
- __ZZN8CSStore2L6getLogEvE4once.454
- __ZZN8CSStore2L6getLogEvE6result.456
- __Znwm
- ___45-[_CSVisualizer(Deprecated) handlerForTable:]_block_invoke
- ___49-[_CSVisualizer(Deprecated) setHandler:forTable:]_block_invoke
- ___49-[_CSVisualizer(Deprecated) setHandler:forTable:]_block_invoke_2
- ___Block_byref_object_copy_.193
- ___Block_byref_object_copy_.213
- ___Block_byref_object_copy_.300
- ___Block_byref_object_copy_.692
- ___Block_byref_object_copy_.81
- ___Block_byref_object_dispose_.194
- ___Block_byref_object_dispose_.214
- ___Block_byref_object_dispose_.301
- ___Block_byref_object_dispose_.693
- ___Block_byref_object_dispose_.82
- ____ZL13GetContextLogv_block_invoke
- ____ZN8CSStore2L15IsAppleInternalEv_block_invoke.121
- ____ZN8CSStore2L6getLogEv_block_invoke.465
- ___assert_rtn
- ___block_descriptor_52_ea8_32s40s_e20_v36?0I8^12^20^28ls32l8s40l8
- ___block_literal_global.115
- ___block_literal_global.12
- ___block_literal_global.207
- ___block_literal_global.246
- ___block_literal_global.336
- ___block_literal_global.455
- ___block_literal_global.521
- ___block_literal_global.708
- ___block_literal_global.745
- ___block_literal_global.83
- ___block_literal_global.86
- ___destroy_helper_block_ea8_32.173
- ___destroy_helper_block_ea8_32.320
- ___destroy_helper_block_ea8_32.550
- _objc_retain_x27
- _objc_retain_x9
CStrings:
+ "%@"
+ "@\"NSMutableAttributedString\""
+ "@28@0:8@16c24"
+ "@32@0:8@16@24"
+ "@32@0:8I16I20@24"
+ "@32@0:8^{__CSStore=}16@24"
+ "CSStoreAttributedStringWriter"
+ "T@\"NSAttributedString\",R,C,D"
+ "T@\"NSLocale\",C,D"
+ "T@\"_CSVisualizer\",&,D"
+ "TB,D"
+ "_attributedString"
+ "_writer"
+ "attributedString"
+ "beginBitfieldFlags:"
+ "beginFlags:flags:"
+ "childUnit:table:unit:"
+ "childUnit:unit:"
+ "elidesEmptyValues"
+ "endFlags"
+ "flag:name:"
+ "flag:name:color:"
+ "init:outBuffer:"
+ "insertsNewlines"
+ "link:unit:"
+ "link:unit:linkedAttributedText:"
+ "link:unit:linkedText:"
+ "link:unitID:linkedAttributedText:"
+ "linkURL:"
+ "linkURL:linkedAttributedText:"
+ "linkURL:linkedText:"
+ "locale"
+ "missingFlag:name:"
+ "missingFlag:name:color:"
+ "newWithBuffer:"
+ "newWithStore:buffer:"
+ "separatorForTitle:separator:"
+ "setElidesEmptyValues:"
+ "setInsertsNewlines:"
+ "setVisualizer:"
+ "true "
+ "v20@0:8I16"
+ "v20@0:8c16"
+ "v28@0:8@16B24"
+ "v28@0:8@16c24"
+ "v28@0:8r^I16I24"
+ "v32@0:8@16*24"
+ "v32@0:8@16@24"
+ "v32@0:8@16I24I28"
+ "v32@0:8@16Q24"
+ "v32@0:8@16d24"
+ "v32@0:8Q16@24"
+ "v36@0:8@16r^I24I32"
+ "v36@0:8Q16@24I32"
+ "v40@0:8@16@24*32"
+ "withAppliedAttribute:value:block:"
+ "withReferenceToUnit:unit:block:"
+ "withTextColor:backgroundColor:block:"
+ "withTextColor:block:"
+ "withWarningColors:"
+ "write:"
+ "write:args:"
+ "write:array:"
+ "write:arrayID:"
+ "write:arrayIDs:count:"
+ "write:arrayStringID:"
+ "write:attributedString:"
+ "write:bool:"
+ "write:code:"
+ "write:format:"
+ "write:format:args:"
+ "write:interval:"
+ "write:number:"
+ "write:separator:"
+ "write:string:"
+ "write:stringID:"
+ "writeArray:"
+ "writeArrayID:"
+ "writeArrayIDs:count:"
+ "writeAttributedString:"
+ "writeFormat:"
+ "writeLink:unitID:linkedText:"
+ "writeNumber:"
+ "writeSeparator"
+ "writeSeparator:"
+ "writeString:"
+ "writeStringID:"
+ "{optional<CSStore2::AttributedStringWriter>=\"\"(?=\"__null_state_\"c\"__val_\"{AttributedStringWriter=\"_vptr$AttributedStringWriter\"^^?\"_reserved\"[30Q]\"_impl\"^{Impl}})\"__engaged_\"B}"
+ "\xf0\xf01"
- "@?20@0:8I16"
- "AttributedStringWriter"
- "Deprecated"
- "New length of store is %llu bytes"
- "[T = "
- "access_context"
- "accessing for read: %@"
- "accessing for write: %@"
- "handlerForTable:"
- "initWithStore:useStandardTableHandlers:"
- "setHandler:forTable:"
- "setStandardTableHandlers"
- "this != &other"
- "v28@0:8@?16I24"
- "v36@?0I8^@12^@20^@28"

```
