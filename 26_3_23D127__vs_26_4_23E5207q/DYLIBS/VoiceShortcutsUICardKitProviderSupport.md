## VoiceShortcutsUICardKitProviderSupport

> `/System/Library/PrivateFrameworks/VoiceShortcutsUICardKitProviderSupport.framework/VoiceShortcutsUICardKitProviderSupport`

```diff

-3515.12.1.0.0
-  __TEXT.__text: 0x3300
-  __TEXT.__auth_stubs: 0x2b0
+3520.88.6.1.4
+  __TEXT.__text: 0x393c
+  __TEXT.__auth_stubs: 0x280
   __TEXT.__objc_methlist: 0x5dc
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0x109
   __TEXT.__oslogstring: 0x9e
   __TEXT.__ustring: 0x40
-  __TEXT.__unwind_info: 0x120
+  __TEXT.__unwind_info: 0x150
   __TEXT.__objc_classname: 0x1cd
-  __TEXT.__objc_methname: 0x135d
+  __TEXT.__objc_methname: 0x1355
   __TEXT.__objc_methtype: 0x62c
   __TEXT.__objc_stubs: 0x1040
   __DATA_CONST.__got: 0xf8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x5a0
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x160
+  __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0xbc8
   __AUTH.__objc_data: 0x1e0

   - /System/Library/PrivateFrameworks/SiriUICore.framework/SiriUICore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6EBD57C9-82C3-360D-B012-721BA1451CC0
+  UUID: 943B76E1-3720-3291-8FA6-8E198A24F697
   Functions: 80
-  Symbols:   500
+  Symbols:   497
   CStrings:  314
 
Symbols:
+ _objc_msgSend$numberWithInteger:
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$numberWithUnsignedInteger:
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[VSUIProgressCardViewController _setUpViews] : 1548 -> 1776
~ -[VSUIProgressCardViewController _setUpHelpers] : 204 -> 220
~ -[VSUIProgressCardViewController _updateDelegateOnBoundsDidChange] : 80 -> 84
~ -[VSUIProgressCardViewController _progressStateMachine] : 92 -> 108
~ -[VSUIProgressCardViewController _progressIndicatorViewController] : 124 -> 132
~ -[VSUIProgressCardViewController _hairlineView] : 180 -> 192
~ -[VSUIProgressCardViewController _statusView] : 136 -> 144
~ -[VSUIProgressCardViewController _loadingIndicatorView] : 140 -> 148
~ -[VSUIProgressCardViewController actionStatusView:didAddViewFromProgressViewController:] : 152 -> 160
~ ___95-[VSUIProgressCardViewController progressStateMachine:didTransitionToState:fromState:forEvent:]_block_invoke : 364 -> 388
~ -[VSUIProgressCardViewController cardSectionViewWillAppearForCardSection:withAppearanceFeedback:] : 280 -> 300
~ -[VSUIProgressCardViewController cardSectionViewDidAppearForCardSection:withAppearanceFeedback:] : 260 -> 268
~ -[VSUIProgressCardViewController contentHeightForWidth:] : 240 -> 248
~ -[VSUIProgressCardViewController progress] : 16 -> 64
~ -[VSUIProgressCardViewController _setStatusView:] : 20 -> 80
~ -[VSUIProgressCardViewController _setLoadingIndicatorView:] : 20 -> 80
~ -[VSUIProgressCardViewController _setProgressIndicatorViewController:] : 20 -> 80
~ -[VSUIProgressCardViewController _setHairlineView:] : 20 -> 80
~ -[VSUIProgressCardViewController _setProgressStateMachine:] : 20 -> 80
~ -[VSUIVoiceShortcutCard _configureWithCard:] : 704 -> 776
~ -[VSUIVoiceShortcutCard cardIdentifier] : 16 -> 64
~ -[VSUIVoiceShortcutCard loadCardWithCompletion:] : 240 -> 248
~ -[VSUIVoiceShortcutCard loadCardWithContent:completion:] : 276 -> 268
~ ___56-[VSUIVoiceShortcutCard loadCardWithContent:completion:]_block_invoke : 212 -> 224
~ -[VSUICKPEntryPoint displayPriorityForCard:] : 76 -> 84
~ -[VSUICKPEntryPoint cardViewControllerForCard:] : 484 -> 528
~ -[VSUIActionStatusView resetState] : 108 -> 116
~ -[VSUIActionStatusView sizeThatFits:] : 180 -> 188
~ -[VSUIActionStatusView progressStateMachine:didTransitionToState:fromState:forEvent:] : 324 -> 336
~ -[VSUIActionStatusView _setUpViews] : 928 -> 1028
~ -[VSUIActionStatusView _updateAcitivityViewSubviewWithDelegateProvidedView] : 560 -> 624
~ -[VSUIActionStatusView setActivityView:] : 20 -> 80
~ -[VSUIActionStatusView setErrorView:] : 20 -> 80
~ -[_VSUIActionStatusErrorView sizeThatFits:] : 108 -> 112
~ -[_VSUIActionStatusErrorView _setUpViews] : 1816 -> 2004
~ -[_VSUIActionStatusErrorView setErrorLabel:] : 20 -> 80
~ -[_VSUIActionStatusErrorView setErrorIconView:] : 20 -> 80
~ -[_VSUIActionStatusErrorView setErrorIconBackgroundView:] : 20 -> 80
~ -[VSUIVoiceShortcutCard loadCardWithCompletion:].cold.1 : 196 -> 204
~ -[VSUIActionStatusView progressStateMachine:ignoredEvent:].cold.1 : 188 -> 192
CStrings:
+ "B40@0:8q16q24@\"SUICProgressIndicatorViewController\"32"
+ "B40@0:8q16q24@32"
+ "numberWithInteger:"
+ "v32@0:8@\"SUICProgressStateMachine\"16q24"
+ "v32@0:8@16q24"
+ "v48@0:8@\"SUICProgressStateMachine\"16q24q32q40"
+ "v48@0:8@16q24q32q40"
- "B40@0:8Q16Q24@\"SUICProgressIndicatorViewController\"32"
- "B40@0:8Q16Q24@32"
- "numberWithUnsignedInteger:"
- "v32@0:8@\"SUICProgressStateMachine\"16Q24"
- "v32@0:8@16Q24"
- "v48@0:8@\"SUICProgressStateMachine\"16Q24Q32Q40"
- "v48@0:8@16Q24Q32Q40"

```
