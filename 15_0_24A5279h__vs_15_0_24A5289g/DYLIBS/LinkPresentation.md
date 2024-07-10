## LinkPresentation

> `/System/iOSSupport/System/Library/Frameworks/LinkPresentation.framework/Versions/A/LinkPresentation`

```diff

-266.1.0.0.0
-  __TEXT.__text: 0xe739c
-  __TEXT.__auth_stubs: 0x1b90
-  __TEXT.__objc_methlist: 0xdeb8
-  __TEXT.__cstring: 0x8160
-  __TEXT.__gcc_except_tab: 0x1e074
-  __TEXT.__const: 0x1f04
+268.1.0.0.0
+  __TEXT.__text: 0xec518
+  __TEXT.__auth_stubs: 0x1c70
+  __TEXT.__objc_methlist: 0xdf28
+  __TEXT.__cstring: 0x8230
+  __TEXT.__gcc_except_tab: 0x1e168
+  __TEXT.__const: 0x1f24
   __TEXT.__ustring: 0x42e
-  __TEXT.__oslogstring: 0x2c79
+  __TEXT.__oslogstring: 0x2f65
   __TEXT.__dlopen_cstrs: 0x6ac
-  __TEXT.__swift5_typeref: 0x95a
+  __TEXT.__swift5_typeref: 0x974
   __TEXT.__swift5_capture: 0x1c8
   __TEXT.__constg_swiftt: 0x81c
   __TEXT.__swift5_fieldmd: 0x4a8

   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_proto: 0xb8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x70c8
-  __TEXT.__eh_frame: 0x600
-  __TEXT.__objc_classname: 0x1fc8
-  __TEXT.__objc_methname: 0x1d9b9
-  __TEXT.__objc_methtype: 0x3a2f
-  __TEXT.__objc_stubs: 0x16100
-  __DATA_CONST.__got: 0xe50
-  __DATA_CONST.__const: 0x21f0
+  __TEXT.__unwind_info: 0x71a8
+  __TEXT.__eh_frame: 0x6f8
+  __TEXT.__objc_classname: 0x1fcc
+  __TEXT.__objc_methname: 0x1da4b
+  __TEXT.__objc_methtype: 0x3a1b
+  __TEXT.__objc_stubs: 0x16140
+  __DATA_CONST.__got: 0xe60
+  __DATA_CONST.__const: 0x2240
   __DATA_CONST.__objc_classlist: 0x7f0
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x1f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6748
+  __DATA_CONST.__objc_selrefs: 0x6780
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x5b0
   __DATA_CONST.__objc_arraydata: 0x14c8
-  __AUTH_CONST.__auth_got: 0xde0
-  __AUTH_CONST.__auth_ptr: 0x3a8
-  __AUTH_CONST.__const: 0x1ca0
+  __AUTH_CONST.__auth_got: 0xe50
+  __AUTH_CONST.__auth_ptr: 0x3b0
+  __AUTH_CONST.__const: 0x1c80
   __AUTH_CONST.__cfstring: 0xc360
-  __AUTH_CONST.__objc_const: 0x2b2d0
+  __AUTH_CONST.__objc_const: 0x2b2f8
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x420
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x1c98
   __AUTH.__data: 0x528
-  __DATA.__objc_ivar: 0x1594
-  __DATA.__data: 0x1af0
+  __DATA.__objc_ivar: 0x1598
+  __DATA.__data: 0x1b00
   __DATA.__bss: 0x1ef8
   __DATA.__common: 0x1f0
   __DATA_DIRTY.__objc_data: 0x34d0

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6044
-  Symbols:   15474
-  CStrings:  1871
+  Functions: 6076
+  Symbols:   15491
+  CStrings:  1875
 
Symbols:
+ -[LPFetcherGroup loggingID]
+ -[LPLinkMetadata _isCurrentlyLoadingOrIncomplete]
+ -[LPLinkMetadata _isCurrentlyLoading]
+ -[LPLinkMetadata _resetIncompleteState]
+ -[LPLinkView _invalidatePresentationPropertiesAndLayout]
+ -[LPURLFetcher dataTask:didReceiveData:].cold.1
+ -[LPVerticalTextStackViewStyle initWithPlatform:sizeClass:fontScalingFactor:]
+ GCC_except_table1013
+ GCC_except_table1014
+ GCC_except_table1023
+ GCC_except_table1024
+ GCC_except_table1032
+ GCC_except_table1033
+ GCC_except_table1034
+ GCC_except_table1049
+ GCC_except_table1050
+ GCC_except_table1060
+ GCC_except_table1065
+ GCC_except_table1066
+ GCC_except_table1067
+ GCC_except_table1085
+ GCC_except_table1086
+ GCC_except_table1087
+ GCC_except_table1103
+ GCC_except_table1105
+ GCC_except_table1107
+ GCC_except_table125
+ GCC_except_table128
+ GCC_except_table138
+ GCC_except_table143
+ GCC_except_table146
+ GCC_except_table150
+ GCC_except_table155
+ GCC_except_table159
+ GCC_except_table169
+ GCC_except_table174
+ GCC_except_table182
+ GCC_except_table188
+ GCC_except_table195
+ GCC_except_table195
+ GCC_except_table198
+ GCC_except_table208
+ GCC_except_table209
+ GCC_except_table210
+ GCC_except_table214
+ GCC_except_table216
+ GCC_except_table218
+ GCC_except_table225
+ GCC_except_table228
+ GCC_except_table232
+ GCC_except_table234
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table243
+ GCC_except_table256
+ GCC_except_table257
+ GCC_except_table258
+ GCC_except_table271
+ GCC_except_table272
+ GCC_except_table285
+ GCC_except_table287
+ GCC_except_table289
+ GCC_except_table298
+ GCC_except_table300
+ GCC_except_table302
+ GCC_except_table320
+ GCC_except_table321
+ GCC_except_table351
+ GCC_except_table352
+ GCC_except_table353
+ GCC_except_table374
+ GCC_except_table375
+ GCC_except_table376
+ GCC_except_table395
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table416
+ GCC_except_table418
+ GCC_except_table433
+ GCC_except_table458
+ GCC_except_table479
+ GCC_except_table508
+ GCC_except_table509
+ GCC_except_table510
+ GCC_except_table531
+ GCC_except_table532
+ GCC_except_table533
+ GCC_except_table556
+ GCC_except_table557
+ GCC_except_table558
+ GCC_except_table583
+ GCC_except_table584
+ GCC_except_table585
+ GCC_except_table606
+ GCC_except_table607
+ GCC_except_table608
+ GCC_except_table629
+ GCC_except_table630
+ GCC_except_table631
+ GCC_except_table650
+ GCC_except_table651
+ GCC_except_table652
+ GCC_except_table669
+ GCC_except_table670
+ GCC_except_table671
+ GCC_except_table694
+ GCC_except_table695
+ GCC_except_table696
+ GCC_except_table715
+ GCC_except_table717
+ GCC_except_table719
+ GCC_except_table738
+ GCC_except_table740
+ GCC_except_table742
+ GCC_except_table759
+ GCC_except_table761
+ GCC_except_table763
+ GCC_except_table781
+ GCC_except_table783
+ GCC_except_table785
+ GCC_except_table828
+ GCC_except_table830
+ GCC_except_table832
+ GCC_except_table853
+ GCC_except_table854
+ GCC_except_table855
+ GCC_except_table868
+ GCC_except_table870
+ GCC_except_table872
+ GCC_except_table892
+ GCC_except_table893
+ GCC_except_table894
+ GCC_except_table904
+ GCC_except_table905
+ GCC_except_table906
+ GCC_except_table922
+ GCC_except_table923
+ GCC_except_table924
+ GCC_except_table937
+ GCC_except_table938
+ GCC_except_table939
+ GCC_except_table964
+ GCC_except_table965
+ GCC_except_table973
+ GCC_except_table974
+ GCC_except_table975
+ GCC_except_table986
+ GCC_except_table987
+ GCC_except_table995
+ GCC_except_table996
+ GCC_except_table997
+ OBJC_IVAR_$_LPFetcherGroup._description
+ OBJC_IVAR_$_LPLinkMetadata._incomplete
+ OBJC_IVAR_$_LPLinkView._presentationPropertyState
+ OBJC_IVAR_$_LPLinkView._suppressNeedsResizeCount
+ __25-[LPTheme adjustForStyle]_block_invoke.1062
+ __25-[LPTheme adjustForStyle]_block_invoke.1072
+ __25-[LPTheme adjustForStyle]_block_invoke_2.1065
+ __25-[LPTheme adjustForStyle]_block_invoke_2.1075
+ __25-[LPTheme adjustForStyle]_block_invoke_3.1068
+ __25-[LPTheme adjustForStyle]_block_invoke_4.1069
+ __40-[LPMetadataProvider _fetchSubresources]_block_invoke.113
+ __42-[LPMetadataProvider _completedWithError:]_block_invoke.123
+ __78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.322
+ __78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.330
+ __Block_byref_object_copy_.120
+ __Block_byref_object_dispose_.121
+ __OBJC_$_PROP_LIST_LPFetcherGroup
+ ___77-[LPVerticalTextStackViewStyle initWithPlatform:sizeClass:fontScalingFactor:]_block_invoke
+ ___block_descriptor_40_ea8_32s_e42_v24?0"LPLinkView"8"UITraitCollection"16ls32l8
+ __block_literal_global.1034
+ __block_literal_global.1047
+ __block_literal_global.1059
+ __block_literal_global.1064
+ __block_literal_global.1067
+ __block_literal_global.1074
+ __block_literal_global.1235
+ __block_literal_global.1244
+ __block_literal_global.133
+ __block_literal_global.151
+ __block_literal_global.1949
+ __block_literal_global.264
+ __block_literal_global.287
+ _objc_msgSend$_invalidatePresentationPropertiesAndLayout
+ _objc_msgSend$_isCurrentlyLoading
+ _objc_msgSend$_isCurrentlyLoadingOrIncomplete
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_continuation_resume
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_isCurrentExecutor
+ _swift_task_reportUnexpectedExecutor
+ _swift_task_switch
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic ytIeAghHr_
+ block_descriptor.30
+ cardHeadingIconSize.normalSize.1238
+ fallbackIconSize.normalSize.1229
+ initWithPlatform:sizeClass:fontScalingFactor:.emailCompatibleVerticalMargin
- -[LPFetcherGroup _addFetcher:atIndex:].cold.1
- -[LPURLFetcher _failedWithErrorCode:underlyingError:].cold.1
- -[LPVerticalTextStackViewStyle initWithPlatform:sizeClass:fontScalingFactor:alignTextAndMediaHorizontalEdges:]
- GCC_except_table1008
- GCC_except_table1010
- GCC_except_table1018
- GCC_except_table1020
- GCC_except_table1028
- GCC_except_table1029
- GCC_except_table1030
- GCC_except_table1044
- GCC_except_table1046
- GCC_except_table1057
- GCC_except_table1061
- GCC_except_table1062
- GCC_except_table1063
- GCC_except_table1081
- GCC_except_table1082
- GCC_except_table1083
- GCC_except_table1100
- GCC_except_table1102
- GCC_except_table1104
- GCC_except_table126
- GCC_except_table129
- GCC_except_table136
- GCC_except_table139
- GCC_except_table144
- GCC_except_table149
- GCC_except_table152
- GCC_except_table156
- GCC_except_table158
- GCC_except_table160
- GCC_except_table161
- GCC_except_table170
- GCC_except_table175
- GCC_except_table183
- GCC_except_table189
- GCC_except_table192
- GCC_except_table192
- GCC_except_table207
- GCC_except_table212
- GCC_except_table215
- GCC_except_table217
- GCC_except_table233
- GCC_except_table235
- GCC_except_table236
- GCC_except_table240
- GCC_except_table250
- GCC_except_table252
- GCC_except_table254
- GCC_except_table268
- GCC_except_table280
- GCC_except_table284
- GCC_except_table293
- GCC_except_table295
- GCC_except_table297
- GCC_except_table315
- GCC_except_table316
- GCC_except_table317
- GCC_except_table348
- GCC_except_table349
- GCC_except_table370
- GCC_except_table371
- GCC_except_table372
- GCC_except_table391
- GCC_except_table392
- GCC_except_table393
- GCC_except_table412
- GCC_except_table413
- GCC_except_table414
- GCC_except_table427
- GCC_except_table428
- GCC_except_table429
- GCC_except_table452
- GCC_except_table473
- GCC_except_table475
- GCC_except_table504
- GCC_except_table505
- GCC_except_table506
- GCC_except_table527
- GCC_except_table528
- GCC_except_table529
- GCC_except_table552
- GCC_except_table553
- GCC_except_table554
- GCC_except_table579
- GCC_except_table580
- GCC_except_table581
- GCC_except_table602
- GCC_except_table603
- GCC_except_table604
- GCC_except_table625
- GCC_except_table626
- GCC_except_table627
- GCC_except_table646
- GCC_except_table647
- GCC_except_table648
- GCC_except_table665
- GCC_except_table666
- GCC_except_table667
- GCC_except_table690
- GCC_except_table691
- GCC_except_table692
- GCC_except_table711
- GCC_except_table712
- GCC_except_table713
- GCC_except_table734
- GCC_except_table735
- GCC_except_table736
- GCC_except_table755
- GCC_except_table756
- GCC_except_table757
- GCC_except_table777
- GCC_except_table778
- GCC_except_table779
- GCC_except_table824
- GCC_except_table825
- GCC_except_table826
- GCC_except_table849
- GCC_except_table850
- GCC_except_table851
- GCC_except_table864
- GCC_except_table865
- GCC_except_table866
- GCC_except_table888
- GCC_except_table889
- GCC_except_table890
- GCC_except_table900
- GCC_except_table901
- GCC_except_table902
- GCC_except_table918
- GCC_except_table919
- GCC_except_table920
- GCC_except_table933
- GCC_except_table934
- GCC_except_table935
- GCC_except_table958
- GCC_except_table959
- GCC_except_table969
- GCC_except_table970
- GCC_except_table971
- GCC_except_table981
- GCC_except_table983
- GCC_except_table991
- GCC_except_table992
- GCC_except_table993
- OBJC_IVAR_$_LPLinkMetadata.__incomplete
- OBJC_IVAR_$_LPLinkView._hasValidPresentationProperties
- OBJC_IVAR_$_LPLinkView._suppressNeedsResize
- _OUTLINED_FUNCTION_8
- __25-[LPTheme adjustForStyle]_block_invoke.1064
- __25-[LPTheme adjustForStyle]_block_invoke.1074
- __25-[LPTheme adjustForStyle]_block_invoke_2.1067
- __25-[LPTheme adjustForStyle]_block_invoke_2.1077
- __25-[LPTheme adjustForStyle]_block_invoke_3.1070
- __25-[LPTheme adjustForStyle]_block_invoke_4.1071
- __42-[LPMetadataProvider _completedWithError:]_block_invoke.121
- __78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.324
- __78-[LPLinkView _openURLAllowingSensitiveSchemes:allowingAssociatedApplications:]_block_invoke.332
- __Block_byref_object_copy_.119
- __Block_byref_object_dispose_.120
- ___110-[LPVerticalTextStackViewStyle initWithPlatform:sizeClass:fontScalingFactor:alignTextAndMediaHorizontalEdges:]_block_invoke
- ___40-[LPMetadataProvider _fetchSubresources]_block_invoke_5
- __block_literal_global.1036
- __block_literal_global.1055
- __block_literal_global.1061
- __block_literal_global.1066
- __block_literal_global.1069
- __block_literal_global.1076
- __block_literal_global.118
- __block_literal_global.1239
- __block_literal_global.1246
- __block_literal_global.135
- __block_literal_global.153
- __block_literal_global.1946
- __block_literal_global.266
- __block_literal_global.289
- _objc_msgSend$initWithPlatform:sizeClass:fontScalingFactor:alignTextAndMediaHorizontalEdges:
- block_copy_helper.24
- block_descriptor.26
- block_destroy_helper.25
- cardHeadingIconSize.normalSize.1240
- fallbackIconSize.normalSize.1231
- initWithPlatform:sizeClass:fontScalingFactor:alignTextAndMediaHorizontalEdges:.emailCompatibleVerticalMargin
CStrings:
+ "@32@0:8#16#24"
+ "@32@0:8@16@24"
+ "LinkPresentation/CustomizationPickerViewController.swift"
+ "LinkPresentation/CustomizationPickerViewControllerTransitionAnimator.swift"
+ "LinkPresentation_Private.LPCustomizationPickerViewController"
- "T@\"LPLinkView\",N,&,Vsource"

```
