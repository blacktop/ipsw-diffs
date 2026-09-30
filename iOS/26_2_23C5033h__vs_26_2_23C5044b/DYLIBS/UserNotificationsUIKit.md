## UserNotificationsUIKit

> `/System/Library/PrivateFrameworks/UserNotificationsUIKit.framework/UserNotificationsUIKit`

```diff

-1003.2.10.100.0
-  __TEXT.__text: 0x1af4d0
-  __TEXT.__auth_stubs: 0x2970
-  __TEXT.__objc_methlist: 0x1a994
+1003.2.11.101.0
+  __TEXT.__text: 0x1b1240
+  __TEXT.__auth_stubs: 0x2980
+  __TEXT.__objc_methlist: 0x1ab84
   __TEXT.__const: 0x4354
-  __TEXT.__gcc_except_tab: 0x2f98
-  __TEXT.__cstring: 0xd526
-  __TEXT.__oslogstring: 0xd9ad
+  __TEXT.__gcc_except_tab: 0x2fb4
+  __TEXT.__cstring: 0xd776
+  __TEXT.__oslogstring: 0xda7d
   __TEXT.__ustring: 0x22
   __TEXT.__swift5_typeref: 0x3ba8
   __TEXT.__swift5_fieldmd: 0x1234

   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__unwind_info: 0x7280
+  __TEXT.__unwind_info: 0x7308
   __TEXT.__eh_frame: 0xcc0
-  __TEXT.__objc_classname: 0x3761
-  __TEXT.__objc_methname: 0x45f41
-  __TEXT.__objc_methtype: 0xbf13
-  __TEXT.__objc_stubs: 0x284e0
-  __DATA_CONST.__got: 0x1808
+  __TEXT.__objc_classname: 0x378f
+  __TEXT.__objc_methname: 0x46199
+  __TEXT.__objc_methtype: 0xc023
+  __TEXT.__objc_stubs: 0x285c0
+  __DATA_CONST.__got: 0x1838
   __DATA_CONST.__const: 0x4190
-  __DATA_CONST.__objc_classlist: 0x7e8
+  __DATA_CONST.__objc_classlist: 0x800
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x608
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc918
-  __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_selrefs: 0xc9c0
+  __DATA_CONST.__objc_protorefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0x560
   __DATA_CONST.__objc_arraydata: 0x158
-  __AUTH_CONST.__auth_got: 0x14c8
+  __AUTH_CONST.__auth_got: 0x14d0
   __AUTH_CONST.__const: 0x5ad0
   __AUTH_CONST.__cfstring: 0x7e40
-  __AUTH_CONST.__objc_const: 0x263a0
+  __AUTH_CONST.__objc_const: 0x26750
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x2a50
-  __AUTH.__data: 0x500
-  __DATA.__objc_ivar: 0x1714
-  __DATA.__data: 0x5450
+  __AUTH.__objc_data: 0x2b80
+  __AUTH.__data: 0x550
+  __DATA.__objc_ivar: 0x171c
+  __DATA.__data: 0x54c0
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x1910
-  __DATA.__common: 0x60
+  __DATA.__common: 0x78
   __DATA_DIRTY.__objc_data: 0x3528
-  __DATA_DIRTY.__data: 0x12e0
+  __DATA_DIRTY.__data: 0x1300
   __DATA_DIRTY.__bss: 0x1440
   __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/Charts.framework/Charts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A668B3AC-6F56-34B5-BDD9-BECAA98E1710
-  Functions: 10906
-  Symbols:   28639
-  CStrings:  13766
+  UUID: 266F34C1-8ADB-300E-BD49-658D487149B7
+  Functions: 10963
+  Symbols:   28689
+  CStrings:  13822
 
Symbols:
+ +[NCPlatterActionButtonBackgroundConfiguration customBackgroundConfigurationWithView:]
+ +[NCPlatterActionButtonBackgroundConfiguration defaultConfiguration]
+ +[NCPlatterActionButtonBackgroundConfiguration glassConfigurationWithGlassConfiguration:]
+ +[NCPlatterActionButtonBackgroundConfiguration materialConfigurationWithRecipe:groupNameBase:tintColor:]
+ -[NCNotificationAppSectionList supplementaryActionsBackgroundConfigurationForNotificationGroupList:]
+ -[NCNotificationGroupList supplementaryActionsBackgroundConfigurationForListCell:]
+ -[NCNotificationListCell buttonsBackgroundConfigurationForSwipeInteraction:]
+ -[NCNotificationListSupplementaryViewsGroup supplementaryActionsBackgroundConfigurationForListCell:]
+ -[NCNotificationStructuredSectionList supplementaryActionsBackgroundConfigurationForNotificationGroupList:]
+ -[NCNotificationSummarizedSectionList buttonsBackgroundConfigurationForSwipeInteraction:]
+ -[NCPlatterActionButton backgroundType]
+ -[NCPlatterActionButton glassConfiguration]
+ -[NCPlatterActionButton setBackgroundType:]
+ -[NCPlatterActionButton setGlassConfiguration:]
+ -[NCPlatterActionButtonBackgroundConfiguration .cxx_destruct]
+ -[NCPlatterActionButtonBackgroundConfiguration backgroundType]
+ -[NCPlatterActionButtonBackgroundConfiguration copyWithZone:]
+ -[NCPlatterActionButtonBackgroundConfiguration customBackgroundView]
+ -[NCPlatterActionButtonBackgroundConfiguration glassConfiguration]
+ -[NCPlatterActionButtonBackgroundConfiguration init]
+ -[NCPlatterActionButtonBackgroundConfiguration isEqual:]
+ -[NCPlatterActionButtonBackgroundConfiguration materialGroupNameBase]
+ -[NCPlatterActionButtonBackgroundConfiguration materialRecipe]
+ -[NCPlatterActionButtonBackgroundConfiguration materialTintColor]
+ -[NCPlatterActionButtonBackgroundConfiguration setBackgroundType:]
+ -[NCPlatterActionButtonBackgroundConfiguration setCustomBackgroundView:]
+ -[NCPlatterActionButtonBackgroundConfiguration setGlassConfiguration:]
+ -[NCPlatterActionButtonBackgroundConfiguration setMaterialGroupNameBase:]
+ -[NCPlatterActionButtonBackgroundConfiguration setMaterialRecipe:]
+ -[NCPlatterActionButtonBackgroundConfiguration setMaterialTintColor:]
+ -[NCPlatterActionButtonsView _updateActionButtonsBackground]
+ -[NCPlatterActionButtonsView backgroundConfiguration]
+ -[NCPlatterActionButtonsView initWithFrame:actions:cornerRadius:shouldVerticallyStack:]
+ -[NCPlatterActionButtonsView setBackgroundConfiguration:]
+ -[NCSwipeInteraction _updateActionButtonViewsBackground]
+ -[NCSwipeInteraction forceUpdateButtonsBackground]
+ GCC_except_table131
+ GCC_except_table135
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table161
+ GCC_except_table170
+ GCC_except_table185
+ GCC_except_table188
+ GCC_except_table217
+ GCC_except_table38
+ GCC_except_table40
+ _OBJC_CLASS_$_NCGlassConfiguration
+ _OBJC_CLASS_$_NCIntelligenceLightHandle
+ _OBJC_CLASS_$_NCPlatterActionButtonBackgroundConfiguration
+ _OBJC_IVAR_$_NCPlatterActionButton._backgroundType
+ _OBJC_IVAR_$_NCPlatterActionButton._glassConfiguration
+ _OBJC_IVAR_$_NCPlatterActionButtonBackgroundConfiguration._backgroundType
+ _OBJC_IVAR_$_NCPlatterActionButtonBackgroundConfiguration._customBackgroundView
+ _OBJC_IVAR_$_NCPlatterActionButtonBackgroundConfiguration._glassConfiguration
+ _OBJC_IVAR_$_NCPlatterActionButtonBackgroundConfiguration._materialGroupNameBase
+ _OBJC_IVAR_$_NCPlatterActionButtonBackgroundConfiguration._materialRecipe
+ _OBJC_IVAR_$_NCPlatterActionButtonBackgroundConfiguration._materialTintColor
+ _OBJC_IVAR_$_NCPlatterActionButtonsView._backgroundConfiguration
+ _OBJC_METACLASS_$_NCGlassConfiguration
+ _OBJC_METACLASS_$_NCIntelligenceLightHandle
+ _OBJC_METACLASS_$_NCPlatterActionButtonBackgroundConfiguration
+ __DATA_NCGlassConfiguration
+ __DATA_NCIntelligenceLightHandle
+ __INSTANCE_METHODS_NCGlassConfiguration
+ __INSTANCE_METHODS_NCIntelligenceLightHandle
+ __IVARS_NCGlassConfiguration
+ __IVARS_NCIntelligenceLightHandle
+ __METACLASS_DATA_NCGlassConfiguration
+ __METACLASS_DATA_NCIntelligenceLightHandle
+ __OBJC_$_CLASS_METHODS_NCPlatterActionButtonBackgroundConfiguration
+ __OBJC_$_CLASS_METHODS_UIView(NCTextSupportingAdditions|NCDeferredActions|NCPlatterShadowAdditions|NCHighFrameRate|NCNotificationGlass)
+ __OBJC_$_INSTANCE_METHODS_NCPlatterActionButtonBackgroundConfiguration
+ __OBJC_$_INSTANCE_METHODS_UIView(NCTextSupportingAdditions|NCDeferredActions|NCPlatterShadowAdditions|NCHighFrameRate|NCNotificationGlass)
+ __OBJC_$_INSTANCE_VARIABLES_NCPlatterActionButtonBackgroundConfiguration
+ __OBJC_$_PROP_LIST_NCPlatterActionButtonBackgroundConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NCSwipeInteractionDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NCSwipeInteractionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NCSwipeInteractionDelegate
+ __OBJC_$_PROTOCOL_REFS_NCSwipeInteractionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_NCPlatterActionButtonBackgroundConfiguration
+ __OBJC_CLASS_RO_$_NCPlatterActionButtonBackgroundConfiguration
+ __OBJC_LABEL_PROTOCOL_$_NCSwipeInteractionDelegate
+ __OBJC_METACLASS_RO_$_NCPlatterActionButtonBackgroundConfiguration
+ __OBJC_PROTOCOL_$_NCSwipeInteractionDelegate
+ __PROPERTIES_NCGlassConfiguration
+ __PROPERTIES_NCIntelligenceLightHandle
+ __PROTOCOLS_NCGlassConfiguration
+ __PROTOCOLS_NCGlassConfiguration.5
+ ___63-[NCClickInteractionPresenter _animatePresentation:completion:]_block_invoke.22
+ ___87-[NCPlatterActionButtonsView initWithFrame:actions:cornerRadius:shouldVerticallyStack:]_block_invoke
+ ___block_literal_global.56
+ ___block_literal_global.58
+ ___block_literal_global.67
+ ___swift_project_boxed_opaque_existential_0
+ _objc_msgSend$_isInAWindow
+ _objc_msgSend$_updateActionButtonViewsBackground
+ _objc_msgSend$_updateActionButtonsBackground
+ _objc_msgSend$backgroundConfiguration
+ _objc_msgSend$backgroundType
+ _objc_msgSend$buttonsBackgroundConfigurationForSwipeInteraction:
+ _objc_msgSend$customBackgroundConfigurationWithView:
+ _objc_msgSend$defaultConfiguration
+ _objc_msgSend$forceUpdateButtonsBackground
+ _objc_msgSend$glassConfiguration
+ _objc_msgSend$glassConfigurationWithGlassConfiguration:
+ _objc_msgSend$initWithFrame:actions:cornerRadius:shouldVerticallyStack:
+ _objc_msgSend$initWithVariant:size:smoothness:subdued:subVariant:adaptiveFixedLuminance:backdropGroupName:identifier:lightHandle:
+ _objc_msgSend$materialConfigurationWithRecipe:groupNameBase:tintColor:
+ _objc_msgSend$nc_configureGlassWithGlassConfiguration:
+ _objc_msgSend$nc_setGlassHighlighted:glassConfiguration:
+ _objc_msgSend$setBackgroundConfiguration:
+ _objc_msgSend$setBackgroundType:
+ _objc_msgSend$setGlassConfiguration:
+ _objc_msgSend$supplementaryActionsBackgroundConfigurationForListCell:
+ _objc_msgSend$supplementaryActionsBackgroundConfigurationForNotificationGroupList:
- -[NCNotificationListCell _buttonCustomBackgroundView]
- -[NCNotificationListCell buttonCustomBackgroundViewForSwipeInteraction:]
- -[NCNotificationListCell buttonsGlassBackgroundIdForSwipeInteraction:]
- -[NCNotificationListCell buttonsGlassBackgroundSmoothnessForSwipeInteraction:]
- -[NCNotificationListCell buttonsGlassBackgroundStateForSwipeInteraction:]
- -[NCNotificationListCell buttonsGlassLuminanceForSwipeInteraction:]
- -[NCNotificationListCell buttonsGlassShouldUseRegularForSwipeInteraction:]
- -[NCNotificationListCell buttonsRecipeForSwipeInteraction:]
- -[NCNotificationListCell buttonsTintColorForSwipeInteraction:]
- -[NCNotificationSummarizedSectionList buttonsGlassBackgroundIdForSwipeInteraction:]
- -[NCNotificationSummarizedSectionList buttonsGlassBackgroundSmoothnessForSwipeInteraction:]
- -[NCNotificationSummarizedSectionList buttonsGlassBackgroundStateForSwipeInteraction:]
- -[NCNotificationSummarizedSectionList buttonsGlassLuminanceForSwipeInteraction:]
- -[NCNotificationSummarizedSectionList buttonsGlassShouldUseRegularForSwipeInteraction:]
- -[NCPlatterActionButton isBackgroundGlass]
- -[NCPlatterActionButton setIsBackgroundGlass:]
- -[NCPlatterActionButtonsView backgroundMaterialRecipe]
- -[NCPlatterActionButtonsView backgroundTintColor]
- -[NCPlatterActionButtonsView customBackgroundView]
- -[NCPlatterActionButtonsView glassLuminance]
- -[NCPlatterActionButtonsView hasGlassBackground]
- -[NCPlatterActionButtonsView initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:glassLuminance:]
- -[NCPlatterActionButtonsView materialGroupNameBase]
- -[NCPlatterActionButtonsView setBackgroundMaterialRecipe:]
- -[NCPlatterActionButtonsView setBackgroundTintColor:]
- -[NCPlatterActionButtonsView setCustomBackgroundView:]
- -[NCPlatterActionButtonsView setHasGlassBackground:]
- -[NCPlatterActionButtonsView setMaterialGroupNameBase:]
- GCC_except_table130
- GCC_except_table134
- GCC_except_table136
- GCC_except_table143
- GCC_except_table147
- GCC_except_table160
- GCC_except_table167
- GCC_except_table169
- GCC_except_table187
- GCC_except_table216
- GCC_except_table37
- _OBJC_CLASS_$_PLPlatterActionButton
- _OBJC_CLASS_$_PLSwipeInteraction
- _OBJC_IVAR_$_NCPlatterActionButton._isBackgroundGlass
- _OBJC_IVAR_$_NCPlatterActionButtonsView._backgroundMaterialRecipe
- _OBJC_IVAR_$_NCPlatterActionButtonsView._backgroundTintColor
- _OBJC_IVAR_$_NCPlatterActionButtonsView._customBackgroundView
- _OBJC_IVAR_$_NCPlatterActionButtonsView._glassLuminance
- _OBJC_IVAR_$_NCPlatterActionButtonsView._hasGlassBackground
- _OBJC_IVAR_$_NCPlatterActionButtonsView._materialGroupNameBase
- __OBJC_$_CLASS_METHODS_UIView(NCTextSupportingAdditions|NCDeferredActions|NCPlatterShadowAdditions|NCHighFrameRate)
- __OBJC_$_INSTANCE_METHODS_UIView(NCTextSupportingAdditions|NCDeferredActions|NCPlatterShadowAdditions|NCHighFrameRate)
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PLSwipeInteractionDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PLSwipeInteractionDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_PLSwipeInteractionDelegate
- __OBJC_$_PROTOCOL_REFS_PLSwipeInteractionDelegate
- __OBJC_LABEL_PROTOCOL_$_PLSwipeInteractionDelegate
- __OBJC_PROTOCOL_$_PLSwipeInteractionDelegate
- __OBJC_PROTOCOL_REFERENCE_$_NCNotificationLookView
- __UISolariumEnabled
- ___162-[NCPlatterActionButtonsView initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:glassLuminance:]_block_invoke
- ___block_literal_global.46
- ___block_literal_global.48
- ___block_literal_global.57
- _objc_msgSend$_buttonCustomBackgroundView
- _objc_msgSend$buttonCustomBackgroundViewForSwipeInteraction:
- _objc_msgSend$buttonsGlassBackgroundIdForSwipeInteraction:
- _objc_msgSend$buttonsGlassBackgroundSmoothnessForSwipeInteraction:
- _objc_msgSend$buttonsGlassBackgroundStateForSwipeInteraction:
- _objc_msgSend$buttonsGlassLuminanceForSwipeInteraction:
- _objc_msgSend$buttonsRecipeForSwipeInteraction:
- _objc_msgSend$buttonsTintColorForSwipeInteraction:
- _objc_msgSend$customPlatterBackgroundView
- _objc_msgSend$glassLuminance
- _objc_msgSend$hasGlassBackground
- _objc_msgSend$initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:glassLuminance:
- _objc_msgSend$initWithVariant:size:smoothness:subdued:
- _objc_msgSend$setIsBackgroundGlass:
CStrings:
+ "$"
+ "%{public}@ some view is not in a window; skipping animation for presenting %{BOOL}d; fromViewIsInWindow: %{BOOL}d; toViewIsInWindow: %{BOOL}d."
+ "@\"NCGlassConfiguration\""
+ "@\"NCIntelligenceLightHandle\""
+ "@\"NCPlatterActionButtonBackgroundConfiguration\""
+ "@\"NCPlatterActionButtonBackgroundConfiguration\"24@0:8@\"NCNotificationGroupList\"16"
+ "@\"NCPlatterActionButtonBackgroundConfiguration\"24@0:8@\"NCNotificationListCell\"16"
+ "@\"NCPlatterActionButtonBackgroundConfiguration\"24@0:8@\"NCSwipeInteraction\"16"
+ "@\"NCSwipeInteraction\""
+ "@\"NSArray\"32@0:8@\"NCSwipeInteraction\"16Q24"
+ "@\"UIColor\"24@0:8@\"NCSwipeInteraction\"16"
+ "@\"UIView\"24@0:8@\"NCSwipeInteraction\"16"
+ "@\"UIView<NSCopying>\""
+ "@24@0:8^v16"
+ "@40@0:8q16@24@32"
+ "@68@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48d56B64"
+ "@84@0:8q16q24d32B40@44d52@60q68@76"
+ "B24@0:8@\"NCSwipeInteraction\"16"
+ "B32@0:8@\"NCSwipeInteraction\"16Q24"
+ "NCGlassConfiguration"
+ "NCIntelligenceLightHandle"
+ "NCNotificationGlass"
+ "NCPlatterActionButtonBackgroundConfiguration"
+ "NCSwipeInteractionDelegate"
+ "Some views are not in a window; Skip morph animation."
+ "T@\"NCGlassConfiguration\",&,N,V_glassConfiguration"
+ "T@\"NCGlassConfiguration\",C,N,V_glassConfiguration"
+ "T@\"NCIntelligenceLightHandle\",N,&,VlightHandle"
+ "T@\"NCPlatterActionButtonBackgroundConfiguration\",&,N,V_backgroundConfiguration"
+ "T@\"NCSwipeInteraction\",&,N,V_summaryPlatterViewSwipeInteraction"
+ "T@\"NCSwipeInteraction\",R,N"
+ "T@\"NCSwipeInteraction\",W,N,V_swipeInteractionInRevealedState"
+ "T@\"UIColor\",&,N,V_materialTintColor"
+ "T@\"UIView<NSCopying>\",&,N,V_customBackgroundView"
+ "TB,N,Vsubdued"
+ "TQ,N,V_backgroundType"
+ "Td,N,VadaptiveFixedLuminance"
+ "Td,N,Vsmoothness"
+ "Tq,N,Videntifier"
+ "Tq,N,Vsize"
+ "Tq,N,Vvariant"
+ "UserNotificationsUIKit_Internal.NCGlassConfiguration"
+ "_backgroundConfiguration"
+ "_backgroundType"
+ "_glassConfiguration"
+ "_handle"
+ "_isInAWindow"
+ "_updateActionButtonViewsBackground"
+ "_updateActionButtonsBackground"
+ "adaptiveFixedLuminance"
+ "backdropGroupName"
+ "backgroundConfiguration"
+ "backgroundType"
+ "buttonsBackgroundConfigurationForSwipeInteraction:"
+ "customBackgroundConfigurationWithView:"
+ "d24@0:8@\"NCSwipeInteraction\"16"
+ "defaultConfiguration"
+ "forceUpdateButtonsBackground"
+ "glassConfiguration"
+ "glassConfigurationWithGlassConfiguration:"
+ "initWithFrame:actions:cornerRadius:shouldVerticallyStack:"
+ "initWithVariant:size:smoothness:subdued:subVariant:adaptiveFixedLuminance:backdropGroupName:identifier:lightHandle:"
+ "isEdgeLightVisible"
+ "isFillLightVisible"
+ "materialConfigurationWithRecipe:groupNameBase:tintColor:"
+ "nc_configureGlassWithGlassConfiguration:"
+ "nc_setGlassHighlighted:glassConfiguration:"
+ "setBackgroundConfiguration:"
+ "setBackgroundType:"
+ "setGlassConfiguration:"
+ "setIsEdgeLightVisible:"
+ "setIsFillLightVisible:"
+ "setLightHandle:"
+ "setSize:"
+ "setSmoothness:"
+ "setSubVariant:"
+ "setSubdued:"
+ "setVariant:"
+ "smoothness"
+ "subVariant"
+ "subdued"
+ "supplementaryActionsBackgroundConfigurationForListCell:"
+ "supplementaryActionsBackgroundConfigurationForNotificationGroupList:"
+ "v24@0:8@\"NCSwipeInteraction\"16"
+ "v32@0:8@\"NCNotificationListCell\"16@\"NCSwipeInteraction\"24"
+ "v32@0:8@\"NCSwipeInteraction\"16d24"
+ "v36@0:8@\"<NCNotificationListBaseComponent>\"16@\"NCSwipeInteraction\"24B32"
- "@\"NSArray\"32@0:8@\"PLSwipeInteraction\"16Q24"
- "@\"PLSwipeInteraction\""
- "@\"UIColor\"24@0:8@\"PLSwipeInteraction\"16"
- "@\"UIView\"24@0:8@\"PLSwipeInteraction\"16"
- "@104@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48d56B64B68Q72d80q88d96"
- "B24@0:8@\"PLSwipeInteraction\"16"
- "B32@0:8@\"PLSwipeInteraction\"16Q24"
- "PLSwipeInteractionDelegate"
- "Q24@0:8@\"PLSwipeInteraction\"16"
- "T@\"PLSwipeInteraction\",&,N,V_summaryPlatterViewSwipeInteraction"
- "T@\"PLSwipeInteraction\",R,N"
- "T@\"PLSwipeInteraction\",W,N,V_swipeInteractionInRevealedState"
- "T@\"UIColor\",&,N,V_backgroundTintColor"
- "TB,N,V_hasGlassBackground"
- "TB,N,V_isBackgroundGlass"
- "Td,R,N,V_glassLuminance"
- "_buttonCustomBackgroundView"
- "_glassLuminance"
- "_hasGlassBackground"
- "_isBackgroundGlass"
- "buttonCustomBackgroundViewForSwipeInteraction:"
- "buttonsGlassBackgroundIdForSwipeInteraction:"
- "buttonsGlassBackgroundSmoothnessForSwipeInteraction:"
- "buttonsGlassBackgroundStateForSwipeInteraction:"
- "buttonsGlassLuminanceForSwipeInteraction:"
- "buttonsGlassShouldUseRegularForSwipeInteraction:"
- "buttonsRecipeForSwipeInteraction:"
- "buttonsTintColorForSwipeInteraction:"
- "d24@0:8@\"PLSwipeInteraction\"16"
- "glassLuminance"
- "hasGlassBackground"
- "initWithFrame:actions:cornerRadius:shouldVerticallyStack:shouldGetGlassBackground:glassState:glassSmoothness:glassId:glassLuminance:"
- "initWithVariant:size:smoothness:subdued:"
- "isBackgroundGlass"
- "q24@0:8@\"PLSwipeInteraction\"16"
- "setHasGlassBackground:"
- "setIsBackgroundGlass:"
- "v24@0:8@\"PLSwipeInteraction\"16"
- "v32@0:8@\"NCNotificationListCell\"16@\"PLSwipeInteraction\"24"
- "v32@0:8@\"PLSwipeInteraction\"16d24"
- "v36@0:8@\"<NCNotificationListBaseComponent>\"16@\"PLSwipeInteraction\"24B32"

```
