## SearchUI

> `/System/Library/PrivateFrameworks/SearchUI.framework/SearchUI`

```diff

-634.1.4.0.0
-  __TEXT.__text: 0xed39c
-  __TEXT.__auth_stubs: 0x2d50
-  __TEXT.__objc_methlist: 0x12078
-  __TEXT.__const: 0x2f04
-  __TEXT.__gcc_except_tab: 0xa1c
-  __TEXT.__cstring: 0x4607
-  __TEXT.__oslogstring: 0x25e8
+634.1.10.0.0
+  __TEXT.__text: 0xef3d8
+  __TEXT.__auth_stubs: 0x2db0
+  __TEXT.__objc_methlist: 0x12110
+  __TEXT.__const: 0x2f84
+  __TEXT.__cstring: 0x4697
+  __TEXT.__oslogstring: 0x272f
+  __TEXT.__gcc_except_tab: 0xa34
   __TEXT.__ustring: 0x9c
   __TEXT.__dlopen_cstrs: 0x160
-  __TEXT.__constg_swiftt: 0x12f8
-  __TEXT.__swift5_typeref: 0x2e0a
-  __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x6b8
-  __TEXT.__swift5_fieldmd: 0x87c
+  __TEXT.__constg_swiftt: 0x1318
+  __TEXT.__swift5_typeref: 0x2ec6
+  __TEXT.__swift5_reflstr: 0x6d0
+  __TEXT.__swift5_fieldmd: 0x8a4
+  __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_assocty: 0x2f8
-  __TEXT.__swift5_capture: 0x6c4
   __TEXT.__swift5_proto: 0x140
-  __TEXT.__swift5_types: 0xd8
+  __TEXT.__swift5_types: 0xdc
+  __TEXT.__swift5_capture: 0x748
+  __TEXT.__swift_as_entry: 0x12c
+  __TEXT.__swift_as_ret: 0x110
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift_as_entry: 0x120
-  __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4720
-  __TEXT.__eh_frame: 0x1ef0
-  __TEXT.__objc_classname: 0x30c7
-  __TEXT.__objc_methname: 0x2a318
-  __TEXT.__objc_methtype: 0x7722
-  __TEXT.__objc_stubs: 0x204e0
-  __DATA_CONST.__got: 0x2470
-  __DATA_CONST.__const: 0x27c0
-  __DATA_CONST.__objc_classlist: 0xab8
-  __DATA_CONST.__objc_catlist: 0x400
+  __TEXT.__unwind_info: 0x47f0
+  __TEXT.__eh_frame: 0x220c
+  __TEXT.__objc_classname: 0x310b
+  __TEXT.__objc_methname: 0x2a3ab
+  __TEXT.__objc_methtype: 0x7729
+  __TEXT.__objc_stubs: 0x20540
+  __DATA_CONST.__got: 0x2490
+  __DATA_CONST.__const: 0x27f0
+  __DATA_CONST.__objc_classlist: 0xac8
+  __DATA_CONST.__objc_catlist: 0x408
   __DATA_CONST.__objc_protolist: 0x360
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9eb8
+  __DATA_CONST.__objc_selrefs: 0x9ee8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x6e8
+  __DATA_CONST.__objc_superrefs: 0x6f0
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x16b8
-  __AUTH_CONST.__const: 0x2748
-  __AUTH_CONST.__cfstring: 0x3140
-  __AUTH_CONST.__objc_const: 0x1dc18
-  __AUTH_CONST.__objc_arrayobj: 0x48
+  __AUTH_CONST.__auth_got: 0x16e8
+  __AUTH_CONST.__const: 0x28d8
+  __AUTH_CONST.__cfstring: 0x31c0
+  __AUTH_CONST.__objc_const: 0x1ddc8
   __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x40f8
+  __AUTH.__objc_data: 0x4198
   __AUTH.__data: 0x7a0
-  __DATA.__objc_ivar: 0xca4
-  __DATA.__data: 0x31c8
-  __DATA.__bss: 0x1ad0
+  __DATA.__objc_ivar: 0xcac
+  __DATA.__data: 0x31f8
+  __DATA.__bss: 0x1ad8
   __DATA.__common: 0xd8
   __DATA_DIRTY.__objc_data: 0x36f0
-  __DATA_DIRTY.__data: 0x4d0
+  __DATA_DIRTY.__data: 0x4c0
   __DATA_DIRTY.__bss: 0xd28
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient
   - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
   - /System/Library/PrivateFrameworks/WeatherUI.framework/WeatherUI
+  - /System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices
   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 14521C92-C308-3AE5-A2FE-DD5086A9A67A
-  Functions: 6775
-  Symbols:   21042
-  CStrings:  9110
+  UUID: 43A734C1-72FB-334A-825E-72B129D2F17B
+  Functions: 6821
+  Symbols:   21087
+  CStrings:  9136
 
Symbols:
+ +[SearchUIRequestUserReportHandler didSelectFeedbackPunchout:rowModel:feedbackDelegate:]
+ -[SFExecuteToolCommand(SearchUICommandClass) _searchUICommandHandlerClass]
+ -[SearchUICardViewController scrollViewForPocketInteraction]
+ -[SearchUICollectionViewController scrollViewForPocketInteraction]
+ -[SearchUIExecuteToolCommandHandler command]
+ -[SearchUIExecuteToolCommandHandler doesRunSynchronously]
+ -[SearchUIExecuteToolCommandHandler performCommand:triggerEvent:environment:]
+ -[SearchUIExecuteToolCommandHandler performCommand:triggerEvent:environment:].cold.1
+ -[SearchUIHomeScreenAppIconView maxLabelSize]
+ -[SearchUIQuickLookCommandHandler defaultSymbolName]
+ -[SearchUIQuickLookCommandHandler defaultTitle]
+ -[SearchUIQuickLookCommandHandler destination]
+ -[SearchUIQuickLookCommandHandler performCommand:triggerEvent:environment:]
+ -[SearchUIResultsViewController scrollViewForPocketInteraction]
+ -[SearchUIVerticalLayoutCardSectionView setUseToolTips:]
+ -[SearchUIVerticalLayoutCardSectionView useToolTips]
+ _CGRectIntersectsRect
+ _OBJC_CLASS_$_SearchUIExecuteToolCommandHandler
+ _OBJC_CLASS_$_SearchUIQuickLookCommandHandler
+ _OBJC_IVAR_$_SearchUICommandHandler._contextMenu
+ _OBJC_IVAR_$_SearchUIVerticalLayoutCardSectionView._useToolTips
+ _OBJC_METACLASS_$_SearchUIExecuteToolCommandHandler
+ _OBJC_METACLASS_$_SearchUIQuickLookCommandHandler
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_SFExecuteToolCommand_$_SearchUICommandClass
+ __OBJC_$_CATEGORY_RFSimpleItemVisualElementCardSection_$_SearchUIGridSectionModel
+ __OBJC_$_CATEGORY_SFCallCommand_$_SearchUIButtonItem
+ __OBJC_$_CATEGORY_SFExecuteToolCommand_$_SearchUICommandClass
+ __OBJC_$_CATEGORY_SFStoreButtonItem_$_SearchUIButtonItem
+ __OBJC_$_CLASS_METHODS_SFCardSection(SearchUIViewClass|SearchUIGridSectionModel|SearchUIHorizontallyScrollingSectionModel|SearchUILeadingTrailingSectionModel|SearchUI)
+ __OBJC_$_INSTANCE_METHODS_RFSimpleItemVisualElementCardSection(SearchUIGridSectionModel|SearchUIHorizontallyScrollingSectionModel|SearchUILeadingTrailingSectionModel)
+ __OBJC_$_INSTANCE_METHODS_SFAppIconCardSection(SearchUIViewClass|SearchUIGridSectionModel|SearchUILeadingTrailingSectionModel)
+ __OBJC_$_INSTANCE_METHODS_SFCallCommand(SearchUIButtonItem|SearchUICommandClass)
+ __OBJC_$_INSTANCE_METHODS_SFCardSection(SearchUIViewClass|SearchUIGridSectionModel|SearchUIHorizontallyScrollingSectionModel|SearchUILeadingTrailingSectionModel|SearchUI)
+ __OBJC_$_INSTANCE_METHODS_SFStoreButtonItem(SearchUIButtonItem|SearchUIButtonItemViewController)
+ __OBJC_$_INSTANCE_METHODS_SearchUIExecuteToolCommandHandler
+ __OBJC_$_INSTANCE_METHODS_SearchUIQuickLookCommandHandler
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SearchUIRowModelViewDelegate
+ __OBJC_CLASS_PROTOCOLS_$_SFCardSection(SearchUIViewClass|SearchUIGridSectionModel|SearchUIHorizontallyScrollingSectionModel|SearchUILeadingTrailingSectionModel|SearchUI)
+ __OBJC_CLASS_RO_$_SearchUIExecuteToolCommandHandler
+ __OBJC_CLASS_RO_$_SearchUIQuickLookCommandHandler
+ __OBJC_METACLASS_RO_$_SearchUIExecuteToolCommandHandler
+ __OBJC_METACLASS_RO_$_SearchUIQuickLookCommandHandler
+ ___47-[SearchUIRequestUserReportHandler contextMenu]_block_invoke
+ ___75-[SearchUIShortcutsImage loadImageWithScale:isDarkStyle:completionHandler:]_block_invoke.61
+ ___77-[SearchUIExecuteToolCommandHandler performCommand:triggerEvent:environment:]_block_invoke
+ ___77-[SearchUIExecuteToolCommandHandler performCommand:triggerEvent:environment:]_block_invoke.cold.1
+ ___block_descriptor_64_e8_32s40s48s56w_e18_v16?0"UIAction"8lw56l8s32l8s40l8s48l8
+ _block_copy_helper.19
+ _block_copy_helper.25
+ _block_descriptor.21
+ _block_descriptor.27
+ _block_destroy_helper.20
+ _block_destroy_helper.26
+ _get_witness_table qd__7SwiftUI4ViewHD2_AaBPAAE9focusableyQrSbFQOyAcAE11buttonStyleyQrqd__AA015PrimitiveButtonF0Rd__lFQOyAA0H0VyAA15ModifiedContentVyAJyAJyAJyAJyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAL5ScaleOGGAA14_PaddingLayoutVGATGAA011_BackgroundfO0VyAA8MaterialVGGAA11_ClipEffectVyAA16RoundedRectangleVGGG_AA05PlainhF0VQo__Qo_HO.3
+ _objc_msgSend$didSelectFeedbackPunchout:rowModel:feedbackDelegate:
+ _objc_msgSend$executeToolInvocationFromData:completionHandler:
+ _objc_msgSend$isSafari
+ _objc_msgSend$loadIconFromData:size:completionHandler:
+ _objc_msgSend$scrollViewForPocketInteraction
+ _objc_msgSend$setUseToolTips:
+ _objc_msgSend$toolInvocationData
+ _objectdestroy.17Tm
+ _objectdestroy.32Tm
+ _objectdestroy.9Tm
+ _symbolic Sb______pSgIegyg_ s5ErrorP
+ _symbolic So6NSDataC
+ _symbolic So7UIImageCSgIeyBy_Sg
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ So6CGSizeV
+ _symbolic _____So7NSErrorCSgIeyByy_ 10ObjectiveC8ObjCBoolV
+ _symbolic _____y_____y_____y_____yAByAByAByABy__________y_____GG_____GAHG_____y_____GG_____y_____GGG______Qo__Qo_ 7SwiftUI4ViewPAAE9focusableyQrSbFQO AcAE11buttonStyleyQrqd__AA015PrimitiveButtonF0Rd__lFQO AA0H0V AA15ModifiedContentV AA5ImageV AA30_EnvironmentKeyWritingModifierV AL5ScaleO AA14_PaddingLayoutV AA011_BackgroundfO0V AA8MaterialV AA11_ClipEffectV AA16RoundedRectangleV AA05PlainhF0V
+ _type_layout_string So6CGSizeV
- +[SearchUIRequestUserReportHandler contextMenuForCardSection:result:feedbackRequest:environment:]
- -[SearchUICardViewController disableScrollPocketInteractionAtEdge:]
- -[SearchUICardViewController registerView:forScrollPocketInteractionAtEdge:]
- -[SearchUICollectionViewController disableScrollPocketInteractionAtEdge:]
- -[SearchUICollectionViewController registerView:forScrollPocketInteractionAtEdge:]
- -[SearchUICreateCalendarEventHandler prefersContextMenu]
- -[SearchUICreateContactHandler prefersContextMenu]
- -[SearchUIResultsViewController disableScrollPocketInteractionAtEdge:]
- -[SearchUIResultsViewController registerView:forScrollPocketInteractionAtEdge:]
- _OBJC_CLASS_$__UIScrollPocketInteraction
- __OBJC_$_CATEGORY_RFSimpleItemVisualElementCardSection_$_SearchUILeadingTrailingSectionModel
- __OBJC_$_CATEGORY_SFCallCommand_$_SearchUICommandClass
- __OBJC_$_CATEGORY_SFStoreButtonItem_$_SearchUIButtonItemViewController
- __OBJC_$_CLASS_METHODS_SFCardSection(SearchUIViewClass|SearchUILeadingTrailingSectionModel|SearchUIGridSectionModel|SearchUIHorizontallyScrollingSectionModel|SearchUI)
- __OBJC_$_INSTANCE_METHODS_RFSimpleItemVisualElementCardSection(SearchUILeadingTrailingSectionModel|SearchUIGridSectionModel|SearchUIHorizontallyScrollingSectionModel)
- __OBJC_$_INSTANCE_METHODS_SFAppIconCardSection(SearchUIViewClass|SearchUILeadingTrailingSectionModel|SearchUIGridSectionModel)
- __OBJC_$_INSTANCE_METHODS_SFCallCommand(SearchUICommandClass|SearchUIButtonItem)
- __OBJC_$_INSTANCE_METHODS_SFCardSection(SearchUIViewClass|SearchUILeadingTrailingSectionModel|SearchUIGridSectionModel|SearchUIHorizontallyScrollingSectionModel|SearchUI)
- __OBJC_$_INSTANCE_METHODS_SFStoreButtonItem(SearchUIButtonItemViewController|SearchUIButtonItem)
- __OBJC_CLASS_PROTOCOLS_$_SFCardSection(SearchUIViewClass|SearchUILeadingTrailingSectionModel|SearchUIGridSectionModel|SearchUIHorizontallyScrollingSectionModel|SearchUI)
- ___97+[SearchUIRequestUserReportHandler contextMenuForCardSection:result:feedbackRequest:environment:]_block_invoke
- ___block_descriptor_64_e8_32s40s48s56w_e18_v16?0"UIAction"8ls32l8w56l8s40l8s48l8
- _block_copy_helper.29
- _block_copy_helper.55
- _block_descriptor.31
- _block_descriptor.57
- _block_destroy_helper.30
- _block_destroy_helper.56
- _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE11buttonStyleyQrqd__AA015PrimitiveButtonE0Rd__lFQOyAA0G0VyAA15ModifiedContentVyAIyAIyAIyAIyAA5ImageVAA30_EnvironmentKeyWritingModifierVyAK5ScaleOGGAA14_PaddingLayoutVGASGAA011_BackgroundeN0VyAA8MaterialVGGAA11_ClipEffectVyAA16RoundedRectangleVGGG_AA05PlaingE0VQo_HO.14
- _objc_msgSend$contextMenuForCardSection:result:feedbackRequest:environment:
- _objc_msgSend$disableScrollPocketInteractionAtEdge:
- _objc_msgSend$initWithScrollView:edge:style:
- _objc_msgSend$registerView:forScrollPocketInteractionAtEdge:
- _objectdestroy.27Tm
- _objectdestroy.42Tm
- _objectdestroy.5Tm
CStrings:
+ "B24@0:8@\"SearchUIRowModel\"16"
+ "Executing tool command with data length: %lu"
+ "Failed to execute tool invocation: %s"
+ "OPEN_ONENESS"
+ "OPEN_QUICKLOOK"
+ "SearchUIExecuteToolCommandHandler"
+ "SearchUIExecuteToolCommandHandler: empty toolInvocationData"
+ "SearchUIExecuteToolCommandHandler: tool execution failed: %@"
+ "SearchUIQuickLookCommandHandler"
+ "SearchUIShortcutsImage failed to load image with image data"
+ "T@\"UIMenu\",R,V_contextMenu"
+ "TB,N,V_useToolTips"
+ "Tool execution completed successfully"
+ "_contextMenu"
+ "_useToolTips"
+ "didSelectFeedbackPunchout:rowModel:feedbackDelegate:"
+ "executeToolInvocationFromData:completionHandler:"
+ "eye"
+ "hasPreviewForRowModel:"
+ "iphone.gen3"
+ "isSafari"
+ "loadIconFromData:size:completionHandler:"
+ "maxLabelSize"
+ "scrollViewForPocketInteraction"
+ "setUseToolTips:"
+ "toolInvocationData"
+ "useToolTips"
+ "v48@0:8@\"NSData\"16{CGSize=dd}24@?<v@?@\"UIImage\">40"
- "T@\"UIMenu\",R"
- "contextMenuForCardSection:result:feedbackRequest:environment:"
- "disableScrollPocketInteractionAtEdge:"
- "initWithScrollView:edge:style:"
- "registerView:forScrollPocketInteractionAtEdge:"
- "v32@0:8@\"UIView\"16Q24"

```
