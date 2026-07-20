## MobileSafari

> `/System/Library/PrivateFrameworks/MobileSafari.framework/MobileSafari`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__data`

```diff

-625.1.22.10.3
-  __TEXT.__text: 0x4e1554
-  __TEXT.__objc_methlist: 0x1cae8
-  __TEXT.__const: 0x1cb14
-  __TEXT.__cstring: 0x134a9
-  __TEXT.__gcc_except_tab: 0x7830
-  __TEXT.__oslogstring: 0x45d9
+625.1.24.10.1
+  __TEXT.__text: 0x4eaedc
+  __TEXT.__objc_methlist: 0x1cb90
+  __TEXT.__const: 0x1cd24
+  __TEXT.__cstring: 0x13529
+  __TEXT.__gcc_except_tab: 0x7840
+  __TEXT.__oslogstring: 0x4849
   __TEXT.__ustring: 0x2440
   __TEXT.__dlopen_cstrs: 0x48e
-  __TEXT.__constg_swiftt: 0x11d64
-  __TEXT.__swift5_typeref: 0xd0cc
+  __TEXT.__constg_swiftt: 0x11e54
+  __TEXT.__swift5_typeref: 0xd10e
   __TEXT.__swift5_builtin: 0x44c
-  __TEXT.__swift5_reflstr: 0xc701
-  __TEXT.__swift5_fieldmd: 0x9ac4
+  __TEXT.__swift5_reflstr: 0xc721
+  __TEXT.__swift5_fieldmd: 0x9b44
   __TEXT.__swift5_assocty: 0x1bb0
-  __TEXT.__swift5_proto: 0x11a0
-  __TEXT.__swift5_types: 0x960
-  __TEXT.__swift5_capture: 0x7220
-  __TEXT.__swift_as_entry: 0x4a4
-  __TEXT.__swift_as_ret: 0x36c
+  __TEXT.__swift5_proto: 0x11c0
+  __TEXT.__swift5_types: 0x968
+  __TEXT.__swift5_capture: 0x7224
+  __TEXT.__swift_as_entry: 0x4c0
+  __TEXT.__swift_as_ret: 0x388
   __TEXT.__swift_as_cont: 0x4e4
   __TEXT.__swift5_mpenum: 0x5c
   __TEXT.__swift5_protos: 0xd8
-  __TEXT.__unwind_info: 0x12388
-  __TEXT.__eh_frame: 0x8e4c
+  __TEXT.__unwind_info: 0x12448
+  __TEXT.__eh_frame: 0x8e74
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6578
+  __DATA_CONST.__const: 0x65c8
   __DATA_CONST.__objc_classlist: 0x10b0
   __DATA_CONST.__objc_catlist: 0x180
   __DATA_CONST.__objc_protolist: 0x788
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10398
+  __DATA_CONST.__objc_selrefs: 0x10400
   __DATA_CONST.__objc_protorefs: 0x260
   __DATA_CONST.__objc_superrefs: 0x7d0
   __DATA_CONST.__objc_arraydata: 0x2e8
-  __DATA_CONST.__got: 0x2998
-  __AUTH_CONST.__const: 0x20d10
-  __AUTH_CONST.__cfstring: 0xab40
-  __AUTH_CONST.__objc_const: 0x3b238
+  __DATA_CONST.__got: 0x29a8
+  __AUTH_CONST.__const: 0x20e98
+  __AUTH_CONST.__cfstring: 0xab60
+  __AUTH_CONST.__objc_const: 0x3b328
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x130
-  __AUTH_CONST.__auth_got: 0x3918
-  __AUTH.__objc_data: 0x10e20
-  __AUTH.__data: 0x7f98
-  __DATA.__objc_ivar: 0x1cd4
-  __DATA.__data: 0xe208
+  __AUTH_CONST.__auth_got: 0x3998
+  __AUTH.__objc_data: 0x10dd0
+  __AUTH.__data: 0x7fb8
+  __DATA.__objc_ivar: 0x1ce0
+  __DATA.__data: 0xe278
   __DATA.__objc_stublist: 0x30
-  __DATA.__bss: 0x20a70
-  __DATA.__common: 0xcd1
-  __DATA_DIRTY.__objc_data: 0x4a78
+  __DATA.__bss: 0x20e80
+  __DATA.__common: 0xcc9
+  __DATA_DIRTY.__objc_data: 0x4a88
   __DATA_DIRTY.__data: 0x1840
   __DATA_DIRTY.__bss: 0x88
   __DATA_DIRTY.__common: 0x258

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26842
-  Symbols:   26165
-  CStrings:  2677
+  Functions: 26894
+  Symbols:   26197
+  CStrings:  2694
 
Symbols:
+ +[UIAction(MobileSafariExtras) _sf_openInNewTabActionWithTabOrder:handler:identifierSuffix:openToSide:]
+ +[UIAction(MobileSafariExtras) _sf_openInNewTabActionsWithHandler:identifierSuffix:openToSide:]
+ +[UIColor(MobileSafariExtras) sf_alternateTertiaryLabelColor]
+ -[SFNotifyMeWhenBanner _preferredContentSizeCategoryDidChange:previousTraitCollection:]
+ -[SFNotifyMeWhenBanner _updateConstraints]
+ -[SFStartPageCollectionViewController _updateNavigationBarTitleColor]
+ GCC_except_table178
+ GCC_except_table210
+ GCC_except_table222
+ _OBJC_IVAR_$_SFNotifyMeWhenBanner._activeLayoutConstraints
+ _OBJC_IVAR_$_SFStartPageCollectionViewController._hasComputedTitleSitsOnGlass
+ _OBJC_IVAR_$_SFStartPageCollectionViewController._titleSitsOnGlass
+ __CLASS_PROPERTIES_SFNotifyMeWhenController
+ ___103+[UIAction(MobileSafariExtras) _sf_openInNewTabActionWithTabOrder:handler:identifierSuffix:openToSide:]_block_invoke
+ ___48-[SFUnifiedTabBarItemView makeActionsMenuButton]_block_invoke_2
+ ___48-[SFUnifiedTabBarItemView makeActionsMenuButton]_block_invoke_3
+ ___48-[SFUnifiedTabBarItemView makeActionsMenuButton]_block_invoke_4
+ ___48-[SFUnifiedTabBarItemView makeActionsMenuButton]_block_invoke_5
+ ___block_descriptor_40_e8_32bs_e45_v16?0"<UIContextMenuInteractionAnimating>"8ls32l8
+ ___block_descriptor_40_e8_32w_e48_v24?0d8"<UIContextMenuInteractionAnimating>"16lw32l8
+ ___dynamicAlternateColor_block_invoke
+ ___swift_closure_destructor.338Tm
+ ___swift_closure_destructor.344Tm
+ ___swift_closure_destructor.403Tm
+ ___swift_closure_destructor.406Tm
+ ___swift_closure_destructor.67Tm
+ ___swift_closure_destructor.71Tm
+ ___swift_closure_destructor.78Tm
+ ___unnamed_15
+ _associated conformance 12MobileSafari11TabOverviewC15DropDestinationV9PlacementOSHAASQ
+ _associated conformance 12MobileSafari12OpenBookmarkV10AppIntents15AssistantIntentAaD0eH0
+ _associated conformance 12MobileSafari12OpenBookmarkV10AppIntents21AssistantSchemaIntentAaD0gI0
+ _associated conformance 12MobileSafari34SFFluidCollectionViewDropPlacementOSHAASQ
+ _associated conformance So41SFOnDemandSummarizationFeedbackControllerC0D0013FBKEvaluationE24DelegateDynamicPresenter12MobileSafariAC0feG4Base
+ _dynamicAlternateColor
+ _objc_msgSend$_sf_openInNewTabActionWithTabOrder:handler:identifierSuffix:openToSide:
+ _objc_msgSend$_sf_openInNewTabActionsWithHandler:identifierSuffix:openToSide:
+ _objc_msgSend$_updateConstraints
+ _objc_msgSend$_updateNavigationBarTitleColor
+ _objc_msgSend$scrollEdgeAppearance
+ _objc_msgSend$setMenuWillDisplayHandler:
+ _objc_msgSend$sf_alternateTertiaryLabelColor
+ _objc_msgSend$userDidSelectOption:summaryText:readerTextUsedForSummarization:associateWithAppleAccount:presentingViewController:
+ _sf_alternateTertiaryLabelColor.alternateTertiaryLabelColor
+ _symbolic _____ 12MobileSafari11TabOverviewC15DropDestinationV9PlacementO
+ _symbolic _____ 12MobileSafari21SFFluidCollectionViewC15DropDestination028_DEE45FB2756E4D0D7AAFBDBEAE2K3B72LLV
+ _symbolic _____ 12MobileSafari34SFFluidCollectionViewDropPlacementO
+ _symbolic ___________Sg_____t 12MobileSafari11TabOverviewC7SectionV AC4ItemV AA34SFFluidCollectionViewDropPlacementO
+ _symbolic ___________Sg_____tSg 12MobileSafari11TabOverviewC7SectionV AC4ItemV AA34SFFluidCollectionViewDropPlacementO
+ _symbolic ______pSg 14SafariSharedUI31WBSNotifyMeWhenTriggerConditionP
+ _symbolic _____y________________G 12MobileSafari21SFFluidCollectionViewC15DropDestination028_DEE45FB2756E4D0D7AAFBDBEAE2K3B72LLV AA11TabOverviewC7SectionV AH4ItemV AA0coP13SupplementaryO
+ _symbolic _____yxq_q0__GSg 12MobileSafari21SFFluidCollectionViewC15DropDestination028_DEE45FB2756E4D0D7AAFBDBEAE2K3B72LLV
+ _symbolic x_q_Sg_____t 12MobileSafari34SFFluidCollectionViewDropPlacementO
- -[SFNotifyMeWhenBanner _setUpConstraints]
- GCC_except_table198
- GCC_except_table218
- ___92+[UIAction(MobileSafariExtras) _sf_openInNewTabActionWithTabOrder:handler:identifierSuffix:]_block_invoke
- ___dynamicAlteranteColor_block_invoke
- ___swift_closure_destructor.336Tm
- ___swift_closure_destructor.342Tm
- ___swift_closure_destructor.401Tm
- ___swift_closure_destructor.404Tm
- ___swift_closure_destructor.70Tm
- ___swift_closure_destructor.74Tm
- ___swift_closure_destructor.77Tm
- _associated conformance 12MobileSafari41SFOnDemandSummarizationFeedbackControllerC0F0013FBKEvaluationG24DelegateDynamicPresenterAaD0hgI4Base
- _dynamicAlteranteColor
- _symbolic So16UIViewControllerCSg
- _symbolic _____ 12MobileSafari41SFOnDemandSummarizationFeedbackControllerC
- _symbolic _____Sg 8Feedback23FBKEvaluationControllerC
- _symbolic ___________Sgt 12MobileSafari11TabOverviewC7SectionV AC4ItemV
- _symbolic _____y______G So24SFNotifyMeWhenControllerC12MobileSafariE07HostingD0C 0F8SharedUI09WBSNotifybC9AlertViewV
- _symbolic _____y_xG So24SFNotifyMeWhenControllerC12MobileSafariE07HostingD0C
- _symbolic x_q_Sgt
CStrings:
+ "Before drop group in first column"
+ "Between drop groups: left section"
+ "Between drop groups: new section"
+ "Between drop groups: right section"
+ "Between sections: left"
+ "Between sections: preserving placeholder section between drop groups"
+ "Between sections: right"
+ "Default destination"
+ "Dragging over %{public}s"
+ "Dragging over placeholder, keep current destination"
+ "Drop destination changed to %{public}s"
+ "Missing frame for section %ld"
+ "Notification permission for Safari was denied."
+ "Notification permission request for Safari was not granted."
+ "Open Link to Side"
+ "Over collapsed section background"
+ "Space in empty row"
+ "v16@?0@\"<UIContextMenuInteractionAnimating>\"8"
+ "v24@?0d8@\"<UIContextMenuInteractionAnimating>\"16"
+ "\xe1"
- "Notification permission denied"
- "Turn on Notifications in Settings to use Notify Me automations."
- "\xd1"
```
