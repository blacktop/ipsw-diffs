## UIKitCore

> `/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`

```diff

-9088.1.106.0.0
-  __TEXT.__text: 0x19e86d4
-  __TEXT.__auth_stubs: 0xd310
+9088.1.110.0.0
+  __TEXT.__text: 0x19edc20
+  __TEXT.__auth_stubs: 0xd320
   __TEXT.__delay_helper: 0x158
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1913d8
-  __TEXT.__const: 0x37f70
+  __TEXT.__objc_methlist: 0x191470
+  __TEXT.__const: 0x37fa0
   __TEXT.__dlopen_cstrs: 0x48a9
-  __TEXT.__cstring: 0x108260
-  __TEXT.__swift5_typeref: 0x126e0
+  __TEXT.__cstring: 0x108350
+  __TEXT.__swift5_typeref: 0x12700
   __TEXT.__swift5_capture: 0xd22c
-  __TEXT.__swift5_reflstr: 0x11537
+  __TEXT.__swift5_reflstr: 0x11557
   __TEXT.__swift5_assocty: 0x3728
-  __TEXT.__swift5_fieldmd: 0x119b8
-  __TEXT.__constg_swiftt: 0x172b4
+  __TEXT.__swift5_fieldmd: 0x119c4
+  __TEXT.__constg_swiftt: 0x172ec
   __TEXT.__swift5_builtin: 0x1068
   __TEXT.__swift5_protos: 0x1ec
-  __TEXT.__swift5_proto: 0x1a58
+  __TEXT.__swift5_proto: 0x1a5c
   __TEXT.__swift5_types: 0x1550
   __TEXT.__oslogstring: 0x4b375
   __TEXT.__swift_as_entry: 0x180
   __TEXT.__swift_as_ret: 0x12c
   __TEXT.__swift5_mpenum: 0x1f4
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x2723c
+  __TEXT.__gcc_except_tab: 0x27228
   __TEXT.__ustring: 0x2752
-  __TEXT.__unwind_info: 0x68c68
+  __TEXT.__unwind_info: 0x68cb8
   __TEXT.__eh_frame: 0x7108
-  __TEXT.__objc_classname: 0x35ab4
-  __TEXT.__objc_methname: 0x3099b1
-  __TEXT.__objc_methtype: 0x747a3
-  __TEXT.__objc_stubs: 0x1d96e0
+  __TEXT.__objc_classname: 0x35ad2
+  __TEXT.__objc_methname: 0x309b33
+  __TEXT.__objc_methtype: 0x747ea
+  __TEXT.__objc_stubs: 0x1d97a0
   __DATA_CONST.__got: 0x7810
-  __DATA_CONST.__const: 0x3bec0
-  __DATA_CONST.__objc_classlist: 0xace0
+  __DATA_CONST.__const: 0x3bec8
+  __DATA_CONST.__objc_classlist: 0xace8
   __DATA_CONST.__objc_catlist: 0x328
   __DATA_CONST.__objc_protolist: 0x3158
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x91a40
+  __DATA_CONST.__objc_selrefs: 0x91a78
   __DATA_CONST.__objc_protorefs: 0xc00
-  __DATA_CONST.__objc_superrefs: 0x7380
+  __DATA_CONST.__objc_superrefs: 0x7388
   __DATA_CONST.__objc_arraydata: 0x4620
-  __AUTH_CONST.__auth_got: 0x69a0
-  __AUTH_CONST.__const: 0x58f30
+  __AUTH_CONST.__auth_got: 0x69a8
+  __AUTH_CONST.__const: 0x58f90
   __AUTH_CONST.__cfstring: 0xaf6a0
-  __AUTH_CONST.__objc_const: 0x261590
+  __AUTH_CONST.__objc_const: 0x261698
   __AUTH_CONST.__objc_arrayobj: 0x2f28
   __AUTH_CONST.__objc_doubleobj: 0x1000
   __AUTH_CONST.__objc_intobj: 0x4f98
   __AUTH_CONST.__objc_dictobj: 0xb40
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH.__objc_data: 0x53730
+  __AUTH.__objc_data: 0x537b0
   __AUTH.__data: 0x86e8
-  __DATA.__objc_ivar: 0x10bb4
-  __DATA.__data: 0x2e064
+  __DATA.__objc_ivar: 0x10bb8
+  __DATA.__data: 0x2e0b4
   __DATA.__uikit_ip: 0x8c8
   __DATA.__uikit_ipl: 0x18
-  __DATA.__bss: 0x2f178
+  __DATA.__bss: 0x2f208
   __DATA.__common: 0x29d8
-  __DATA_DIRTY.__objc_ivar: 0x930c
+  __DATA_DIRTY.__objc_ivar: 0x9310
   __DATA_DIRTY.__objc_data: 0x29158
   __DATA_DIRTY.__uikit_ip: 0x11f0
   __DATA_DIRTY.__data: 0x66d8
-  __DATA_DIRTY.__bss: 0x10ab8
+  __DATA_DIRTY.__bss: 0x10aa8
   __DATA_DIRTY.__common: 0x430
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accessibility.framework/Accessibility

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A8BAD607-EAE6-3324-A030-D5B04C1AE681
-  Functions: 170643
-  Symbols:   432864
-  CStrings:  180755
+  UUID: C386FC81-4D16-373B-A18B-48D936145AD0
+  Functions: 170668
+  Symbols:   432899
+  CStrings:  180772
 
Symbols:
+ +[UIInputActiveSetContainerView _shouldHitTestInputViewFirst]
+ +[UIInputActiveSetContainerView requiresConstraintBasedLayout]
+ -[UIInputActiveSetContainerView hitTest:withEvent:]
+ -[UIInputActiveSetContainerView textEffectsVisibilityLevel]
+ -[UIInputLayoutHostingItem constraintsForView:embeddedInGuide:insets:identifier:]
+ -[UIInputLayoutHostingItem setAccessoryViewVisible:delay:]
+ -[UIInputSetContainerView _containerForKeyplaneViews]
+ -[UIScrollView _keyForAccessoryViewAtEdge:]
+ -[UISystemInputAssistantViewController _shouldCheckItemsVisibility]
+ -[UIView(UIKB_UIViewExtras) _containerForKeyplaneViews]
+ -[_UINavigationBarVisualProviderCarPlaySolarium backButtonLeadingConstraint]
+ -[_UINavigationBarVisualProviderCarPlaySolarium backButtonTrailingConstraint]
+ -[_UINavigationBarVisualProviderCarPlaySolarium setBackButtonLeadingConstraint:]
+ -[_UINavigationBarVisualProviderCarPlaySolarium setBackButtonTrailingConstraint:]
+ GCC_except_table209
+ GCC_except_table215
+ GCC_except_table292
+ GCC_except_table298
+ GCC_except_table302
+ GCC_except_table315
+ GCC_except_table393
+ GCC_except_table400
+ GCC_except_table406
+ GCC_except_table407
+ GCC_except_table436
+ GCC_except_table475
+ GCC_except_table489
+ GCC_except_table499
+ GCC_except_table502
+ GCC_except_table522
+ _OBJC_CLASS_$_UIInputActiveSetContainerView
+ _OBJC_IVAR_$_UIInputView._suppressBackgroundStyling
+ _OBJC_METACLASS_$_UIInputActiveSetContainerView
+ __IVARS__TtCE5UIKitCSo17_UILiquidLensViewP33_4C400BD973F5E4E0B779D1A21A7AEB2711DestOutView
+ __MergedGlobals.28
+ __OBJC_$_CLASS_METHODS_UIInputActiveSetContainerView
+ __OBJC_$_INSTANCE_METHODS_UIInputActiveSetContainerView
+ __OBJC_CLASS_RO_$_UIInputActiveSetContainerView
+ __OBJC_METACLASS_RO_$_UIInputActiveSetContainerView
+ ___48-[UIInputWindowController viewDidLayoutSubviews]_block_invoke.516
+ ___58-[UIInputLayoutHostingItem setAccessoryViewVisible:delay:]_block_invoke
+ ___58-[UITrackingElementWindowController viewDidLayoutSubviews]_block_invoke_2
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.552
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.557
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.558
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.559
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.575
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.579
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_2.556
+ ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_2.576
+ ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.330
+ ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.335
+ ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.336
+ ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.337
+ ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_2.353
+ ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_3.354
+ ___93-[UIInputLayoutHostingItem animatingTransitionFromState:toState:animationType:totalDuration:]_block_invoke.89
+ ___block_descriptor_40_e8_32s_e27_v16?0"UITraitCollection"8ls32l8
+ ___block_descriptor_42_e8_32s_e40_v16?0"UIInputViewSetNotificationInfo"8ls32l8
+ ___block_literal_global.1132
+ ___block_literal_global.1155
+ ___block_literal_global.2045
+ ___block_literal_global.2091
+ ___block_literal_global.2123
+ ___block_literal_global.2127
+ ___block_literal_global.423
+ ___block_literal_global.459
+ ___block_literal_global.531
+ ___block_literal_global.602
+ ___block_literal_global.636
+ ___block_literal_global.658
+ ___block_literal_global.829
+ ___block_literal_global.840
+ _block_copy_helper.155
+ _block_copy_helper.204
+ _block_descriptor.157
+ _block_descriptor.206
+ _block_destroy_helper.156
+ _block_destroy_helper.205
+ _objc_msgSend$_keyForAccessoryViewAtEdge:
+ _objc_msgSend$_shouldCheckItemsVisibility
+ _objc_msgSend$backButtonLeadingConstraint
+ _objc_msgSend$backButtonTrailingConstraint
+ _objc_msgSend$constraintsForView:embeddedInGuide:insets:identifier:
+ _objc_msgSend$setBackButtonLeadingConstraint:
+ _objc_msgSend$setBackButtonTrailingConstraint:
+ _symbolic So20CAMatchMoveAnimationCSg
- -[UIInputLayoutHostingItem constraintsForView:embeddedInGuide:identifier:]
- -[UIInputLayoutHostingItem resetPlacement]
- -[UIInputLayoutHostingItem setPlacement]
- -[UIInputLayoutHostingItem someViewDidLayoutSubviews]
- -[_UINavigationBarVisualProviderCarPlaySolarium backButtonConstraints]
- -[_UINavigationBarVisualProviderCarPlaySolarium setBackButtonConstraints:]
- GCC_except_table230
- GCC_except_table241
- GCC_except_table284
- GCC_except_table313
- GCC_except_table395
- GCC_except_table498
- GCC_except_table501
- GCC_except_table517
- GCC_except_table547
- ___48-[UIInputWindowController viewDidLayoutSubviews]_block_invoke.507
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.541
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.543
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.548
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.549
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.566
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.570
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_2.547
- ___77-[UIInputWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_2.567
- ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.325
- ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.329
- ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.332
- ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke.333
- ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_2.350
- ___87-[UITrackingElementWindowController moveFromPlacement:toPlacement:starting:completion:]_block_invoke_3.351
- ___93-[UIInputLayoutHostingItem animatingTransitionFromState:toState:animationType:totalDuration:]_block_invoke.87
- ___block_descriptor_32_e27_v16?0"UITraitCollection"8l
- ___block_descriptor_74_e8_32s_e40_v16?0"UIInputViewSetNotificationInfo"8ls32l8
- ___block_literal_global.1112
- ___block_literal_global.1141
- ___block_literal_global.1151
- ___block_literal_global.2090
- ___block_literal_global.2126
- ___block_literal_global.420
- ___block_literal_global.446
- ___block_literal_global.450
- ___block_literal_global.593
- ___block_literal_global.598
- ___block_literal_global.638
- ___block_literal_global.649
- ___block_literal_global.826
- ___block_literal_global.837
- _block_copy_helper.123
- _block_copy_helper.143
- _block_copy_helper.193
- _block_copy_helper.201
- _block_descriptor.125
- _block_descriptor.145
- _block_descriptor.195
- _block_descriptor.203
- _block_destroy_helper.124
- _block_destroy_helper.144
- _block_destroy_helper.194
- _block_destroy_helper.202
- _objc_msgSend$constraintsForView:embeddedInGuide:identifier:
CStrings:
+ "@\"UIInputActiveSetContainerView\""
+ "@\"_TtCE5UIKitCSo17_UILiquidLensViewP33_4C400BD973F5E4E0B779D1A21A7AEB2711DestOutView\""
+ "@72@0:8@16@24{UIEdgeInsets=dddd}32@64"
+ "T@\"NSLayoutConstraint\",&,N,V_backButtonLeadingConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_backButtonTrailingConstraint"
+ "T@\"_TtCE5UIKitCSo17_UILiquidLensViewP33_4C400BD973F5E4E0B779D1A21A7AEB2711DestOutView\",N,&,VliftedContentPunchout"
+ "UIInputActiveSetContainerView"
+ "_backButtonLeadingConstraint"
+ "_backButtonTrailingConstraint"
+ "_containerForKeyplaneViews"
+ "_keyForAccessoryViewAtEdge:"
+ "_shouldCheckItemsVisibility"
+ "backButtonLeadingConstraint"
+ "backButtonTrailingConstraint"
+ "com.apple.CarPlayTemplateUIHost"
+ "constraintsForView:embeddedInGuide:insets:identifier:"
+ "matchMoveAnimation"
+ "setBackButtonLeadingConstraint:"
+ "setBackButtonTrailingConstraint:"
- "T@\"UIView\",N,&,VliftedContentPunchout"
- "constraintsForView:embeddedInGuide:identifier:"

```
