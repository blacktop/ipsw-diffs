## WorkflowUIServices

> `/System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices`

```diff

-4027.2.1.0.0
-  __TEXT.__text: 0xd71e8
-  __TEXT.__auth_stubs: 0x3720
-  __TEXT.__objc_methlist: 0x5814
-  __TEXT.__const: 0x8634
+4030.0.2.0.0
+  __TEXT.__text: 0xe25c4
+  __TEXT.__auth_stubs: 0x37f0
+  __TEXT.__objc_methlist: 0x5954
+  __TEXT.__const: 0x8784
   __TEXT.__dlopen_cstrs: 0x23d
   __TEXT.__cstring: 0x483b
-  __TEXT.__swift5_typeref: 0x7116
-  __TEXT.__swift5_reflstr: 0x14ac
+  __TEXT.__swift5_typeref: 0x71f2
+  __TEXT.__swift5_reflstr: 0x151c
   __TEXT.__swift5_assocty: 0x710
-  __TEXT.__constg_swiftt: 0x31a4
-  __TEXT.__swift5_fieldmd: 0x2078
+  __TEXT.__constg_swiftt: 0x3230
+  __TEXT.__swift5_fieldmd: 0x20d0
   __TEXT.__swift5_builtin: 0x1e0
-  __TEXT.__swift5_capture: 0x4b4
-  __TEXT.__swift5_proto: 0x518
+  __TEXT.__swift5_capture: 0x534
+  __TEXT.__swift5_proto: 0x51c
   __TEXT.__swift5_types: 0x2bc
   __TEXT.__swift5_mpenum: 0x84
-  __TEXT.__swift_as_entry: 0x120
-  __TEXT.__swift_as_ret: 0xbc
-  __TEXT.__swift5_protos: 0x3c
-  __TEXT.__oslogstring: 0x18a8
+  __TEXT.__swift_as_entry: 0x164
+  __TEXT.__swift_as_ret: 0x10c
+  __TEXT.__swift5_protos: 0x40
+  __TEXT.__oslogstring: 0x1992
   __TEXT.__gcc_except_tab: 0x564
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x3aa8
-  __TEXT.__eh_frame: 0x30e0
-  __TEXT.__objc_classname: 0x1056
-  __TEXT.__objc_methname: 0x11329
-  __TEXT.__objc_methtype: 0x39b2
-  __TEXT.__objc_stubs: 0xb6a0
-  __DATA_CONST.__got: 0x1350
-  __DATA_CONST.__const: 0x1350
+  __TEXT.__unwind_info: 0x3d68
+  __TEXT.__eh_frame: 0x3da8
+  __TEXT.__objc_classname: 0x1057
+  __TEXT.__objc_methname: 0x1160f
+  __TEXT.__objc_methtype: 0x3a04
+  __TEXT.__objc_stubs: 0xb8a0
+  __DATA_CONST.__got: 0x1370
+  __DATA_CONST.__const: 0x1360
   __DATA_CONST.__objc_classlist: 0x338
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3e48
+  __DATA_CONST.__objc_selrefs: 0x3ef8
   __DATA_CONST.__objc_protorefs: 0x80
-  __DATA_CONST.__objc_superrefs: 0x218
+  __DATA_CONST.__objc_superrefs: 0x220
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x1ba0
-  __AUTH_CONST.__const: 0x5598
+  __AUTH_CONST.__auth_got: 0x1c08
+  __AUTH_CONST.__const: 0x56e0
   __AUTH_CONST.__cfstring: 0x1880
-  __AUTH_CONST.__objc_const: 0xb3d8
+  __AUTH_CONST.__objc_const: 0xb630
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x26b8
-  __AUTH.__data: 0x1e88
-  __DATA.__objc_ivar: 0x5e4
-  __DATA.__data: 0x4278
-  __DATA.__bss: 0x8d88
-  __DATA.__common: 0xc0
+  __AUTH.__objc_data: 0x26c0
+  __AUTH.__data: 0x1f08
+  __DATA.__objc_ivar: 0x60c
+  __DATA.__data: 0x42b8
+  __DATA.__bss: 0x8e08
+  __DATA.__common: 0xc8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0x498
   __DATA_DIRTY.__bss: 0x700

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FE30C591-67D7-3CB0-8261-4B29A42D6F76
-  Functions: 6068
-  Symbols:   9754
-  CStrings:  4132
+  UUID: 27551540-CFED-39CE-8375-A36076A7B9A8
+  Functions: 6295
+  Symbols:   10134
+  CStrings:  4176
 
Symbols:
+ +[UIColor(WorkflowEditor_CrossPlatform) wf_slotTemplateSlotTypingBackgroundColorForUseCase:]
+ +[WFSlotTemplateSlot(Convenience) addingSlotWithIdentifier:imageScaleFactor:]
+ +[WFSlotTemplateView heightForWidth:withContents:horizontalPadding:font:unpopulatedFont:alignment:useCase:]
+ -[WFSlotTemplateImageAttachment imageScaleFactor]
+ -[WFSlotTemplateImageAttachment initWithData:ofType:]
+ -[WFSlotTemplateImageAttachment setImageScaleFactor:]
+ -[WFSlotTemplateLayoutManager initWithUseCase:]
+ -[WFSlotTemplateLayoutManager setUseCase:]
+ -[WFSlotTemplateLayoutManager slotBackgroundInsetsAtCharIndex:]
+ -[WFSlotTemplateLayoutManager useCase]
+ -[WFSlotTemplateSlot representsButton]
+ -[WFSlotTemplateSlot setRepresentsButton:]
+ -[WFSlotTemplateTextStorage initWithUseCase:]
+ -[WFSlotTemplateTextStorage prefersTypingForSlotFilling]
+ -[WFSlotTemplateTextStorage setPrefersTypingForSlotFilling:]
+ -[WFSlotTemplateTextStorage setUseCase:]
+ -[WFSlotTemplateTextStorage useCase]
+ -[WFSlotTemplateView beginTypingInSlotWithIdentifier:atPosition:]
+ -[WFSlotTemplateView initWithUseCase:]
+ -[WFSlotTemplateView setUseCase:]
+ -[WFSlotTemplateView singleLineHeight]
+ -[WFSlotTemplateView slotTemplateTypingTextViewDidPaste:pasteRange:withOriginalBlock:]
+ -[WFSlotTemplateView useCase]
+ -[WFWidgetCell configureWithAction:dataSource:cornerRadius:widgetType:family:homeScreenTintColor:isClearStyleEnabled:]
+ -[WFWidgetCell isClear]
+ -[WFWidgetCell setClearStyle:]
+ -[WFWidgetCell setIsClear:]
+ -[WFWidgetConfigurationViewController isCancelled]
+ -[WFWidgetConfigurationViewController setCancelled:]
+ -[WFWidgetGridView isClearStyleEnabled]
+ -[WFWidgetGridView setCellsToClear:]
+ -[WFWidgetGridView setIsClearStyleEnabled:]
+ -[WFWidgetViewController isClearStyleEnabled]
+ -[WFWidgetViewController setIsClearStyleEnabled:]
+ -[WFWidgetViewController setWidgetStyleToClear:]
+ GCC_except_table103
+ GCC_except_table1075
+ GCC_except_table119
+ GCC_except_table1264
+ GCC_except_table1317
+ GCC_except_table147
+ GCC_except_table150
+ GCC_except_table1502
+ GCC_except_table1506
+ GCC_except_table158
+ GCC_except_table292
+ GCC_except_table399
+ GCC_except_table402
+ GCC_except_table406
+ GCC_except_table413
+ GCC_except_table462
+ GCC_except_table466
+ GCC_except_table497
+ GCC_except_table533
+ GCC_except_table616
+ GCC_except_table622
+ GCC_except_table892
+ GCC_except_table902
+ _LinkServicesLibrary.1422
+ _LinkServicesLibrary.3187
+ _LinkServicesLibraryCore.frameworkLibrary.1428
+ _LinkServicesLibraryCore.frameworkLibrary.3193
+ _OBJC_IVAR_$_WFSlotTemplateImageAttachment._imageScaleFactor
+ _OBJC_IVAR_$_WFSlotTemplateLayoutManager._useCase
+ _OBJC_IVAR_$_WFSlotTemplateSlot._representsButton
+ _OBJC_IVAR_$_WFSlotTemplateTextStorage._prefersTypingForSlotFilling
+ _OBJC_IVAR_$_WFSlotTemplateTextStorage._useCase
+ _OBJC_IVAR_$_WFSlotTemplateView._useCase
+ _OBJC_IVAR_$_WFWidgetCell._isClear
+ _OBJC_IVAR_$_WFWidgetConfigurationViewController._cancelled
+ _OBJC_IVAR_$_WFWidgetGridView._isClearStyleEnabled
+ _OBJC_IVAR_$_WFWidgetViewController._isClearStyleEnabled
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_104
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_93
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_95
+ _OUTLINED_FUNCTION_96
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ _WFLogCategoryParameterSummary
+ _WFSlotTemplateSlotCornerRadiusForUseCase
+ _WFSlotTemplateSlotInnerSpacingForUseCase
+ _WFSlotTemplateSlotSurroundingSpacingForUseCase
+ ___LinkServicesLibraryCore_block_invoke.1429
+ ___LinkServicesLibraryCore_block_invoke.3194
+ ___block_descriptor_145_e8_32s40s48bs_e43_v48?0{CGRect={CGPoint=dd}{CGSize=dd}}8^B40ls32l8s40l8s48l8
+ ___block_literal_global.1216
+ ___block_literal_global.1324
+ ___block_literal_global.1539
+ ___block_literal_global.173
+ ___block_literal_global.2305
+ ___block_literal_global.2622
+ ___block_literal_global.2781
+ ___block_literal_global.2877
+ ___block_literal_global.330
+ ___block_literal_global.3621
+ ___block_literal_global.3642
+ ___block_literal_global.4941
+ ___block_literal_global.5175
+ ___block_literal_global.5187
+ ___block_literal_global.5263
+ ___getLNActionClass_block_invoke.3185
+ ___getLNFocusConfigurationSuggestionContextClass_block_invoke.1419
+ ___getLNFullyQualifiedActionIdentifierClass_block_invoke.1417
+ _audit_stringLinkServices.1432
+ _audit_stringLinkServices.3200
+ _getLNActionClass.softClass.3184
+ _getLNFocusConfigurationSuggestionContextClass.softClass.1418
+ _getLNFullyQualifiedActionIdentifierClass.softClass.1416
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyAA4ViewPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQOyAeAEAfgH_Qrqd___SbyyctSQRd__lFQOyACyACyAA01_e9Modifier_D0Vy18WorkflowUIServices014CardBackgroundJ033_C05175F39C03079DE35453898668CF9FLLVGAA033_ContainerRoundedRectangularShapeJ0VyAA0U9RectangleVGGAA011_InsettablenwJ0VyAA5ColorVASGG_AA0Z6SchemeOQo__A1_SgQo_AA022_EnvironmentKeyWritingJ0VyA1_GGA6_yAK05SolidZ14ThemeTampolineCSgGGAaDHPA8_AaDHPqd0__AaDHD3_A4_HO_A7_AA0eJ0HPyHCHC_A12_AAA14_HPyHCHC.53
+ _objc_msgSend$addingSlotWithIdentifier:imageScaleFactor:
+ _objc_msgSend$beginTypingInSlotWithIdentifier:atPosition:
+ _objc_msgSend$colorWithWhite:alpha:
+ _objc_msgSend$configureWithAction:dataSource:cornerRadius:widgetType:family:homeScreenTintColor:isClearStyleEnabled:
+ _objc_msgSend$imageScaleFactor
+ _objc_msgSend$initWithUseCase:
+ _objc_msgSend$isCancelled
+ _objc_msgSend$isClearStyleEnabled
+ _objc_msgSend$prefersTypingForSlotFilling
+ _objc_msgSend$representsButton
+ _objc_msgSend$selectedRange
+ _objc_msgSend$setCancelled:
+ _objc_msgSend$setCellsToClear:
+ _objc_msgSend$setClearStyle:
+ _objc_msgSend$setImageScaleFactor:
+ _objc_msgSend$setRepresentsButton:
+ _objc_msgSend$setUseCase:
+ _objc_msgSend$slotBackgroundInsetsAtCharIndex:
+ _objc_msgSend$slotTemplateTypingTextViewDidPaste:pasteRange:withOriginalBlock:
+ _objc_msgSend$slotTemplateView:typingDidPasteWithRange:originalBlock:
+ _objc_msgSend$useCase
+ _objc_msgSend$wf_slotTemplateSlotTypingBackgroundColorForUseCase:
+ _objectdestroy.14Tm
+ _swift_deletedAsyncMethodErrorTu
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain_n
+ _symbolic $s18WorkflowUIServices29PasteboardSupportingParameterP
+ _symbolic G0R1_
+ _symbolic SS6toolId_t
+ _symbolic Si6offset______7elementt 7ToolKit10TypedValueO
+ _symbolic Si6offset______7elementtSg 7ToolKit10TypedValueO
+ _symbolic _____ 7ToolKit10TypedValueO010CollectionD0V
+ _symbolic _____ 7ToolKit10TypedValueO08DeferredD0V
+ _symbolic _____ 7ToolKit12TypeInstanceO
+ _symbolic _____Sg 7ToolKit0A10DefinitionV
+ _symbolic _____Sg 7ToolKit0A10InvocationV
+ _symbolic _____Sg 7ToolKit12TypeInstanceO
+ _symbolic __________Iegnr_ 18WorkflowUIServices28ParameterSummaryToolTemplateO AA0cF7ElementO
+ _symbolic __________Yac 18WorkflowUIServices24ParameterTemplateElementO AA0c11SummaryToolD0O
+ _symbolic ______pSg 7ToolKit0A20ExecutionSessionPoolP
+ _symbolic _____yAAy_____y_____G_____y_____GG_____y_____AFGG 7SwiftUI15ModifiedContentV AA014_ViewModifier_D0V 18WorkflowUIServices014CardBackgroundF033_C05175F39C03079DE35453898668CF9FLLV AA033_ContainerRoundedRectangularShapeF0V AA0Q9RectangleV AA011_InsettablejsF0V AA5ColorV
+ _symbolic _____yAAy_____y_____yAAyAAy_____y_____G_____y_____GG_____y_____AFGG______Qo__AMSgQo______yAMGGAQy_____SgGG 7SwiftUI15ModifiedContentV AA4ViewPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQO AeAEAfgH_Qrqd___SbyyctSQRd__lFQO AA01_e9Modifier_D0V 18WorkflowUIServices014CardBackgroundJ033_C05175F39C03079DE35453898668CF9FLLV AA033_ContainerRoundedRectangularShapeJ0V AA0U9RectangleV AA011_InsettablenwJ0V AA5ColorV AA0Z6SchemeO AA022_EnvironmentKeyWritingJ0V AK05SolidZ14ThemeTampolineC
+ _symbolic _____y_____G 7SwiftUI41_ContainerRoundedRectangularShapeModifierV AA0D9RectangleV
+ _symbolic _____y_____yAAy_____y_____G_____y_____GG_____y_____AFGG______Qo_ 7SwiftUI4ViewPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQO AA15ModifiedContentV AA01_c9Modifier_I0V 18WorkflowUIServices014CardBackgroundJ033_C05175F39C03079DE35453898668CF9FLLV AA033_ContainerRoundedRectangularShapeJ0V AA0U9RectangleV AA011_InsettablenwJ0V AA5ColorV AA0Z6SchemeO
+ _symbolic _____y_____y_____G_____y_____GG 7SwiftUI15ModifiedContentV AA014_ViewModifier_D0V 18WorkflowUIServices014CardBackgroundF033_C05175F39C03079DE35453898668CF9FLLV AA033_ContainerRoundedRectangularShapeF0V AA0Q9RectangleV
+ _symbolic _____y_____y_____yAAyAAy_____y_____G_____y_____GG_____y_____AFGG______Qo__AMSgQo______yAMGG 7SwiftUI15ModifiedContentV AA4ViewPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQO AeAEAfgH_Qrqd___SbyyctSQRd__lFQO AA01_e9Modifier_D0V 18WorkflowUIServices014CardBackgroundJ033_C05175F39C03079DE35453898668CF9FLLV AA033_ContainerRoundedRectangularShapeJ0V AA0U9RectangleV AA011_InsettablenwJ0V AA5ColorV AA0Z6SchemeO AA022_EnvironmentKeyWritingJ0V
+ _symbolic _____y_____y_____yAAy_____y_____G_____y_____GG_____y_____AFGG______Qo__AMSgQo_ 7SwiftUI4ViewPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQO AcAEAdeF_Qrqd___SbyyctSQRd__lFQO AA15ModifiedContentV AA01_c9Modifier_I0V 18WorkflowUIServices014CardBackgroundJ033_C05175F39C03079DE35453898668CF9FLLV AA033_ContainerRoundedRectangularShapeJ0V AA0U9RectangleV AA011_InsettablenwJ0V AA5ColorV AA0Z6SchemeO
+ _symbolic ytSg
+ _symbolic ytSgIeAgHr_
- +[UIColor(WorkflowEditor_CrossPlatform) wf_slotTemplateSlotTypingBackgroundColor]
- +[WFSlotTemplateView heightForWidth:withContents:horizontalPadding:font:unpopulatedFont:alignment:]
- -[WFSlotTemplateLayoutManager getPreferredLeadingSpacing:trailingSpacing:forDrawingTextAttachment:atCharacterIndex:]
- -[WFSlotTemplateLayoutManager init]
- -[WFSlotTemplateTextStorage init]
- -[WFSlotTemplateView initWithFrame:]
- -[WFSlotTemplateView slotTemplateTypingTextViewDidPaste:withOriginalBlock:]
- -[WFWidgetCell configureWithAction:dataSource:cornerRadius:widgetType:family:homeScreenTintColor:]
- GCC_except_table101
- GCC_except_table1061
- GCC_except_table117
- GCC_except_table1246
- GCC_except_table1296
- GCC_except_table143
- GCC_except_table146
- GCC_except_table1475
- GCC_except_table1479
- GCC_except_table154
- GCC_except_table284
- GCC_except_table383
- GCC_except_table394
- GCC_except_table398
- GCC_except_table405
- GCC_except_table454
- GCC_except_table458
- GCC_except_table489
- GCC_except_table525
- GCC_except_table608
- GCC_except_table614
- GCC_except_table881
- GCC_except_table891
- _LinkServicesLibrary.1400
- _LinkServicesLibrary.3172
- _LinkServicesLibraryCore.frameworkLibrary.1406
- _LinkServicesLibraryCore.frameworkLibrary.3178
- ___LinkServicesLibraryCore_block_invoke.1407
- ___LinkServicesLibraryCore_block_invoke.3179
- ___block_descriptor_121_e8_32s40bs_e43_v48?0{CGRect={CGPoint=dd}{CGSize=dd}}8^B40ls32l8s40l8
- ___block_literal_global.1190
- ___block_literal_global.1300
- ___block_literal_global.1518
- ___block_literal_global.167.2274
- ___block_literal_global.2292
- ___block_literal_global.2605
- ___block_literal_global.2764
- ___block_literal_global.2861
- ___block_literal_global.324
- ___block_literal_global.3603
- ___block_literal_global.3624
- ___block_literal_global.4899
- ___block_literal_global.5133
- ___block_literal_global.5145
- ___block_literal_global.5222
- ___getLNActionClass_block_invoke.3170
- ___getLNFocusConfigurationSuggestionContextClass_block_invoke.1397
- ___getLNFullyQualifiedActionIdentifierClass_block_invoke.1395
- _audit_stringLinkServices.1410
- _audit_stringLinkServices.3185
- _getLNActionClass.softClass.3169
- _getLNFocusConfigurationSuggestionContextClass.softClass.1396
- _getLNFullyQualifiedActionIdentifierClass.softClass.1394
- _get_witness_table 7SwiftUI15ModifiedContentVyACyAA4ViewPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQOyAeAEAfgH_Qrqd___SbyyctSQRd__lFQOyACyACyAA01_e9Modifier_D0Vy18WorkflowUIServices014CardBackgroundJ033_C05175F39C03079DE35453898668CF9FLLVGAA015_ContainerShapeJ0VyAA16RoundedRectangleVGGAA011_InsettablenuJ0VyAA5ColorVASGG_AA0Y6SchemeOQo__A1_SgQo_AA022_EnvironmentKeyWritingJ0VyA1_GGA6_yAK05SolidY14ThemeTampolineCSgGGAaDHPA8_AaDHPqd0__AaDHD3_A4_HO_A7_AA0eJ0HPyHCHC_A12_AAA14_HPyHCHC.53
- _objc_msgSend$blackColor
- _objc_msgSend$configureWithAction:dataSource:cornerRadius:widgetType:family:homeScreenTintColor:
- _objc_msgSend$slotTemplateTypingTextViewDidPaste:withOriginalBlock:
- _objc_msgSend$slotTemplateView:typingDidPasteWithOriginalBlock:
- _objc_msgSend$slotWithLocalizedName:localizedPlaceholder:languageCode:key:
- _objc_msgSend$wf_slotTemplateSlotTypingBackgroundColor
- _objectdestroy.10Tm
- _symbolic __________c 18WorkflowUIServices24ParameterTemplateElementO AA0c11SummaryToolD0O
- _symbolic _____yAAy_____y_____G_____y_____GG_____y_____AFGG 7SwiftUI15ModifiedContentV AA014_ViewModifier_D0V 18WorkflowUIServices014CardBackgroundF033_C05175F39C03079DE35453898668CF9FLLV AA015_ContainerShapeF0V AA16RoundedRectangleV AA011_InsettablejqF0V AA5ColorV
- _symbolic _____yAAy_____y_____yAAyAAy_____y_____G_____y_____GG_____y_____AFGG______Qo__AMSgQo______yAMGGAQy_____SgGG 7SwiftUI15ModifiedContentV AA4ViewPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQO AeAEAfgH_Qrqd___SbyyctSQRd__lFQO AA01_e9Modifier_D0V 18WorkflowUIServices014CardBackgroundJ033_C05175F39C03079DE35453898668CF9FLLV AA015_ContainerShapeJ0V AA16RoundedRectangleV AA011_InsettablenuJ0V AA5ColorV AA0Y6SchemeO AA022_EnvironmentKeyWritingJ0V AK05SolidY14ThemeTampolineC
- _symbolic _____y_____G 7SwiftUI23_ContainerShapeModifierV AA16RoundedRectangleV
- _symbolic _____y_____yAAy_____y_____G_____y_____GG_____y_____AFGG______Qo_ 7SwiftUI4ViewPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQO AA15ModifiedContentV AA01_c9Modifier_I0V 18WorkflowUIServices014CardBackgroundJ033_C05175F39C03079DE35453898668CF9FLLV AA015_ContainerShapeJ0V AA16RoundedRectangleV AA011_InsettablenuJ0V AA5ColorV AA0Y6SchemeO
- _symbolic _____y_____y_____G_____y_____GG 7SwiftUI15ModifiedContentV AA014_ViewModifier_D0V 18WorkflowUIServices014CardBackgroundF033_C05175F39C03079DE35453898668CF9FLLV AA015_ContainerShapeF0V AA16RoundedRectangleV
- _symbolic _____y_____y_____yAAyAAy_____y_____G_____y_____GG_____y_____AFGG______Qo__AMSgQo______yAMGG 7SwiftUI15ModifiedContentV AA4ViewPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQO AeAEAfgH_Qrqd___SbyyctSQRd__lFQO AA01_e9Modifier_D0V 18WorkflowUIServices014CardBackgroundJ033_C05175F39C03079DE35453898668CF9FLLV AA015_ContainerShapeJ0V AA16RoundedRectangleV AA011_InsettablenuJ0V AA5ColorV AA0Y6SchemeO AA022_EnvironmentKeyWritingJ0V
- _symbolic _____y_____y_____yAAy_____y_____G_____y_____GG_____y_____AFGG______Qo__AMSgQo_ 7SwiftUI4ViewPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQO AcAEAdeF_Qrqd___SbyyctSQRd__lFQO AA15ModifiedContentV AA01_c9Modifier_I0V 18WorkflowUIServices014CardBackgroundJ033_C05175F39C03079DE35453898668CF9FLLV AA015_ContainerShapeJ0V AA16RoundedRectangleV AA011_InsettablenuJ0V AA5ColorV AA0Y6SchemeO
CStrings:
+ "\"2"
+ "<%p %@> Setting widget style to clear: %@"
+ "@32@0:8@16d24"
+ "Could not create parameter because there was no tool found in the db:  %s"
+ "Failed to resolve default value with error %@ setting default value to nil"
+ "Resolved default value to %s"
+ "TB,N,GisCancelled,V_cancelled"
+ "TB,N,V_isClear"
+ "TB,N,V_isClearStyleEnabled"
+ "TB,N,V_prefersTypingForSlotFilling"
+ "TB,N,V_representsButton"
+ "TQ,N,V_useCase"
+ "Td,N,V_imageScaleFactor"
+ "_cancelled"
+ "_imageScaleFactor"
+ "_isClear"
+ "_isClearStyleEnabled"
+ "_prefersTypingForSlotFilling"
+ "_representsButton"
+ "_useCase"
+ "addingSlotWithIdentifier:imageScaleFactor:"
+ "beginTypingInSlotWithIdentifier:atPosition:"
+ "cancelled"
+ "colorWithWhite:alpha:"
+ "configureWithAction:dataSource:cornerRadius:widgetType:family:homeScreenTintColor:isClearStyleEnabled:"
+ "d72@0:8d16@24d32@40@48q56Q64"
+ "heightForWidth:withContents:horizontalPadding:font:unpopulatedFont:alignment:useCase:"
+ "imageScaleFactor"
+ "initWithUseCase:"
+ "isCancelled"
+ "isClear"
+ "isClearStyleEnabled"
+ "prefersTypingForSlotFilling"
+ "representsButton"
+ "setCancelled:"
+ "setCellsToClear:"
+ "setClearStyle:"
+ "setImageScaleFactor:"
+ "setIsClear:"
+ "setIsClearStyleEnabled:"
+ "setPrefersTypingForSlotFilling:"
+ "setRepresentsButton:"
+ "setUseCase:"
+ "setWidgetStyleToClear:"
+ "singleLineHeight"
+ "slotBackgroundInsetsAtCharIndex:"
+ "slotTemplateTypingTextViewDidPaste:pasteRange:withOriginalBlock:"
+ "slotTemplateView:typingDidPasteWithRange:originalBlock:"
+ "toolSessionPool"
+ "typeInstance"
+ "useCase"
+ "v48@0:8@\"WFSlotTemplateTypingTextView\"16{_NSRange=QQ}24@?<v@?>40"
+ "v48@0:8@16{_NSRange=QQ}24@?40"
+ "v68@0:8@16@24d32q40q48@56B64"
+ "wf_slotTemplateSlotTypingBackgroundColorForUseCase:"
+ "{UIEdgeInsets=dddd}24@0:8Q16"
- "configureWithAction:dataSource:cornerRadius:widgetType:family:homeScreenTintColor:"
- "d64@0:8d16@24d32@40@48q56"
- "getPreferredLeadingSpacing:trailingSpacing:forDrawingTextAttachment:atCharacterIndex:"
- "heightForWidth:withContents:horizontalPadding:font:unpopulatedFont:alignment:"
- "is.workflow.actions.runworkflow.WFInput"
- "slotTemplateTypingTextViewDidPaste:withOriginalBlock:"
- "slotTemplateView:typingDidPasteWithOriginalBlock:"
- "v48@0:8^d16^d24@\"NSTextAttachment\"32Q40"
- "v48@0:8^d16^d24@32Q40"
- "v64@0:8@16@24d32q40q48@56"
- "valueParameters"
- "wf_slotTemplateSlotTypingBackgroundColor"

```
