## ShortcutsUI

> `/Applications/ShortcutsUI.app/ShortcutsUI`

```diff

-2038.0.1.10.0
-  __TEXT.__text: 0x1b0b0
-  __TEXT.__auth_stubs: 0x660
-  __TEXT.__objc_stubs: 0x5500
-  __TEXT.__objc_methlist: 0x19a4
-  __TEXT.__const: 0x1e0
-  __TEXT.__gcc_except_tab: 0x138
-  __TEXT.__cstring: 0x2448
-  __TEXT.__objc_methname: 0x7b4f
-  __TEXT.__oslogstring: 0x144d
-  __TEXT.__objc_classname: 0x4d1
-  __TEXT.__objc_methtype: 0x194d
-  __TEXT.__unwind_info: 0x6c4
-  __DATA_CONST.__auth_got: 0x340
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x978
-  __DATA_CONST.__cfstring: 0x17e0
+2106.100.3.1.0
+  __TEXT.__text: 0x1bacc
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_stubs: 0x5440
+  __TEXT.__objc_methlist: 0x19b0
+  __TEXT.__const: 0x1f8
+  __TEXT.__gcc_except_tab: 0x168
+  __TEXT.__cstring: 0x2572
+  __TEXT.__objc_methname: 0x7dcf
+  __TEXT.__oslogstring: 0x154c
+  __TEXT.__objc_classname: 0x4cc
+  __TEXT.__objc_methtype: 0x18e0
+  __TEXT.__unwind_info: 0x6e0
+  __DATA_CONST.__auth_got: 0x318
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x9e0
+  __DATA_CONST.__cfstring: 0x1980
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_doubleobj: 0x10
+  __DATA_CONST.__objc_doubleobj: 0x20
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x5228
-  __DATA.__objc_selrefs: 0x1808
-  __DATA.__objc_classrefs: 0x330
+  __DATA.__objc_const: 0x50d0
+  __DATA.__objc_selrefs: 0x1810
+  __DATA.__objc_classrefs: 0x300
   __DATA.__objc_superrefs: 0x90
-  __DATA.__objc_ivar: 0x264
+  __DATA.__objc_ivar: 0x288
   __DATA.__objc_data: 0x690
   __DATA.__data: 0x908
   __DATA.__bss: 0x40

   - /System/Library/PrivateFrameworks/WorkflowUIServices.framework/WorkflowUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 28D12B62-F814-3187-AF31-0E3981353571
-  Functions: 712
-  Symbols:   241
-  CStrings:  2002
+  UUID: 72EB3628-332B-3675-8340-EA5AB0224CBC
+  Functions: 730
+  Symbols:   238
+  CStrings:  2056
 
Symbols:
+ _OBJC_CLASS_$_PTDrillDownRow
+ _OBJC_CLASS_$_WFApertureIconView
+ _OBJC_METACLASS_$_WFApertureIconView
+ _UIFontWeightSemibold
+ _kCAFilterInputHardEdges
+ _kCAFilterInputIntermediateBitDepth
+ _kCAFilterInputNormalizeEdges
+ _kCAFilterInputQuality
+ _kCAFilterInputRadius
- _CATransform3DIdentity
- _CATransform3DMakeScale
- _CGPathCreateCopyByIntersectingPath
- _CGRectInset
- _NSLog
- _OBJC_CLASS_$_NSNumberFormatter
- _OBJC_CLASS_$_UIImageView
- _OBJC_CLASS_$_WFAppIcon
- _OBJC_CLASS_$_WFIconHostingView
- _OBJC_CLASS_$_WFIconStackView
- _OBJC_CLASS_$_WFImage
- _UIRectCenteredAboutPoint
CStrings:
+ "\x11"
+ "\x12\xf01"
+ "%s Dismissal requested while already dismissing presentable, nothing to do."
+ "%s No presentable to dismiss"
+ "%s Non-interruptible dismissal request received while hinting, immediately pushing to poof phase."
+ "%s Revoked running context does not match current presentable."
+ "%s Revoking banner presentable with reason: %@"
+ "-[WFBannerManager getBannerForQueuedDialogRequest:dialogIsBreakthroughSmartPrompt:completionHandler:]_block_invoke_7"
+ "-[WFBannerManager queue_dismissPresentableWithReason:interruptible:]"
+ "-[WFBannerManager queue_dismissPresentableWithReason:interruptible:]_block_invoke_2"
+ "-[WFBannerManager queue_revokeIslandPresentableForContext:reason:]_block_invoke"
+ "-[WFBannerManager requestContainerForRunningContext:]_block_invoke"
+ "3\x17%\x11"
+ "5\x14!"
+ "<%@, embedded platter: %@, presented VC: %@, queuedStatusPlatter: %@, dismissalPhase: %@>"
+ "@\"WFApertureIconAccessoryView\""
+ "@\"WFBannerGestureSettings\""
+ "@\"WFBannerTransitionSettings\""
+ "Alpha Delay"
+ "Alpha Response"
+ "Blur Delay"
+ "Blur Filter"
+ "Blur Radius"
+ "Blur Response"
+ "Gesture"
+ "Gesture Tracking"
+ "Impulse"
+ "Impulse (Unregistered Velocity)"
+ "Interactive Poof (Final Phase)"
+ "Interactive Poof (Intermediate Phase)"
+ "Intermediate Phase Duration"
+ "Offset"
+ "Poof In"
+ "Poof Out"
+ "Runtime UI"
+ "Scale"
+ "Scale Damping"
+ "Scale Response"
+ "T@\"WFApertureIconAccessoryView\",R,N,V_iconView"
+ "T@\"WFBannerGestureSettings\",&,N,V_gestureSettings"
+ "T@\"WFBannerTransitionSettings\",&,N,V_transitionSettings"
+ "T@\"WFDialogAttribution\",&,N,V_pendingDelayedAttribution"
+ "T@\"WFDispatchSourceTimer\",&,N,V_dismissalCompletionTimer"
+ "T@\"WFWorkflowRunningContext\",&,N,V_runningContext"
+ "T@?,C,N,V_interactiveDismissalHandler"
+ "T@?,C,N,V_viewIsAppearingHandler"
+ "TB,N,V_blurFilterEnabled"
+ "TB,N,V_viewIsAppearingCalled"
+ "TQ,N,V_dismissalPhase"
+ "Td,N,V_phase1_artificialInitialOffset"
+ "Td,N,V_phase1_impulse"
+ "Td,N,V_phase1_impulse_unregisteredVelocity"
+ "Td,N,V_phase1_initialBlurRadius"
+ "Td,N,V_phase1_initialScale"
+ "Td,N,V_phase1_phaseDuration"
+ "Td,N,V_phase1_response"
+ "Td,N,V_poofBlurDelay"
+ "Td,N,V_poofInAlphaResponse"
+ "Td,N,V_poofInBlurRadius"
+ "Td,N,V_poofInBlurResponse"
+ "Td,N,V_poofInScale"
+ "Td,N,V_poofInScaleDamping"
+ "Td,N,V_poofInScaleResponse"
+ "Td,N,V_poofOutAlphaDelay"
+ "Td,N,V_poofOutAlphaResponse"
+ "Td,N,V_poofOutBlurDelay"
+ "Td,N,V_poofOutBlurRadius"
+ "Td,N,V_poofOutBlurResponse"
+ "Td,N,V_poofOutScale"
+ "Td,N,V_poofOutScaleDamping"
+ "Td,N,V_poofOutScaleResponse"
+ "Transition"
+ "Upwards Squeeze"
+ "Vertical Scale Multiplier"
+ "WFApertureIconAccessoryView"
+ "WFBannerGestureSettings"
+ "WFBannerTransitionSettings"
+ "_blurFilterEnabled"
+ "_dismissalCompletionTimer"
+ "_dismissalPhase"
+ "_gestureSettings"
+ "_interactiveDismissalHandler"
+ "_pendingDelayedAttribution"
+ "_phase1_artificialInitialOffset"
+ "_phase1_impulse"
+ "_phase1_impulse_unregisteredVelocity"
+ "_phase1_initialBlurRadius"
+ "_phase1_initialScale"
+ "_phase1_phaseDuration"
+ "_phase1_response"
+ "_poofBlurDelay"
+ "_poofInAlphaResponse"
+ "_poofInBlurRadius"
+ "_poofInBlurResponse"
+ "_poofInScale"
+ "_poofInScaleDamping"
+ "_poofInScaleResponse"
+ "_poofOutAlphaDelay"
+ "_poofOutAlphaResponse"
+ "_poofOutBlurDelay"
+ "_poofOutBlurRadius"
+ "_poofOutBlurResponse"
+ "_poofOutScale"
+ "_poofOutScaleDamping"
+ "_poofOutScaleResponse"
+ "_transitionSettings"
+ "_viewIsAppearingCalled"
+ "_viewIsAppearingHandler"
+ "animateEmbeddedPlatterDismissalWithCompletion:interruptible:"
+ "appBundleIdentifier"
+ "blurFilterEnabled"
+ "dismissalCompletionTimer"
+ "dismissalPhase"
+ "dissolve"
+ "gestureSettings"
+ "hint"
+ "hinting request did not find embedded platter, revoking immediately. Hint reason: %@"
+ "interactiveDismissalHandler"
+ "intrinsicContentSize"
+ "isCancelled"
+ "none"
+ "pendingDelayedAttribution"
+ "phase1_artificialInitialOffset"
+ "phase1_impulse"
+ "phase1_impulse_unregisteredVelocity"
+ "phase1_initialBlurRadius"
+ "phase1_initialScale"
+ "phase1_phaseDuration"
+ "phase1_response"
+ "poofBlurDelay"
+ "poofInAlphaResponse"
+ "poofInBlurRadius"
+ "poofInBlurResponse"
+ "poofInScale"
+ "poofInScaleDamping"
+ "poofInScaleResponse"
+ "poofOutAlphaDelay"
+ "poofOutAlphaResponse"
+ "poofOutBlurDelay"
+ "poofOutBlurRadius"
+ "poofOutBlurResponse"
+ "poofOutScale"
+ "poofOutScaleDamping"
+ "poofOutScaleResponse"
+ "primaryColor"
+ "queue_dismissPresentableWithReason:interruptible:"
+ "rowWithTitle:childSettingsKeyPath:"
+ "setBlurFilterEnabled:"
+ "setClipsToBounds:"
+ "setDismissalCompletionTimer:"
+ "setDismissalPhase:"
+ "setGestureSettings:"
+ "setIcon:associatedAppBundleIdentifier:animated:"
+ "setInteractiveDismissalHandler:"
+ "setPendingDelayedAttribution:"
+ "setPhase1_artificialInitialOffset:"
+ "setPhase1_impulse:"
+ "setPhase1_impulse_unregisteredVelocity:"
+ "setPhase1_initialBlurRadius:"
+ "setPhase1_initialScale:"
+ "setPhase1_phaseDuration:"
+ "setPhase1_response:"
+ "setPoofBlurDelay:"
+ "setPoofInAlphaResponse:"
+ "setPoofInBlurRadius:"
+ "setPoofInBlurResponse:"
+ "setPoofInScale:"
+ "setPoofInScaleDamping:"
+ "setPoofInScaleResponse:"
+ "setPoofOutAlphaDelay:"
+ "setPoofOutAlphaResponse:"
+ "setPoofOutBlurDelay:"
+ "setPoofOutBlurRadius:"
+ "setPoofOutBlurResponse:"
+ "setPoofOutScale:"
+ "setPoofOutScaleDamping:"
+ "setPoofOutScaleResponse:"
+ "setTransitionSettings:"
+ "setUserInteractionEnabled:"
+ "setViewIsAppearingCalled:"
+ "setViewIsAppearingHandler:"
+ "systemFontOfSize:weight:"
+ "trackingBlurEnabled == YES"
+ "trackingBlurEnabled == YES && squeezeEnabled = NO"
+ "v24@?0@\"WFDialogResponse\"8@\"NSError\"16"
+ "v28@0:8@?16B24"
+ "viewIsAppearingCalled"
+ "viewIsAppearingHandler"
- "\x12\xf0!"
- "#"
- "%s Revoking presented banner: %@, context: %@, reason: %@"
- "-[WFBannerManager getBannerForQueuedDialogRequest:dialogIsBreakthroughSmartPrompt:completionHandler:]_block_invoke_8"
- "-[WFBannerManager queue_beginHintingDismissalOfPresentedContainerWithReason:]"
- "-[WFBannerManager requestContainerForRunningContext:]_block_invoke_3"
- "5\x15!"
- "<#\x11"
- "<%@, embedded platter: %@, presented VC: %@, queuedStatusPlatter: %@, isHinting: %@>"
- "@\"UIImageView\""
- "@\"WFConfiguredStaccatoAction\""
- "@\"WFIcon\""
- "@\"WFIconStackAccessoryView\""
- "@\"WFIconStackView\""
- "@\"WFStaccatoIconAccessoryView\""
- "Blur"
- "Dissolve Animation Settings"
- "Enabled"
- "NO"
- "Radius"
- "Running UI"
- "T@\"UIImageView\",&,N,V_iconView"
- "T@\"UILabel\",R,N,V_subtitleLabel"
- "T@\"UIView\",&,N,V_contentClippingView"
- "T@\"WFConfiguredStaccatoAction\",&,N,V_action"
- "T@\"WFDialogAttribution\",R,N,V_attribution"
- "T@\"WFDispatchSourceTimer\",&,N,V_hintingCompletionTimer"
- "T@\"WFIcon\",&,N,V_icon"
- "T@\"WFIcon\",&,N,V_pendingDelayedIcon"
- "T@\"WFIconStackAccessoryView\",R,N,V_iconStackView"
- "T@\"WFIconStackView\",R,N,V_stackView"
- "T@\"WFStaccatoIconAccessoryView\",R,N,V_iconView"
- "T@?,C,N,V_bannerWillDismissHandler"
- "TB,N,GisHinting,V_hinting"
- "TB,N,V_blurEnabled"
- "TB,N,V_unregisteredVelocityEdgeCaseEnabled"
- "Td,N,V_edgeCase_artificialInitialOffset"
- "Td,N,V_edgeCase_impulse"
- "Td,N,V_edgeCase_initialBlurRadius"
- "Td,N,V_edgeCase_initialScale"
- "Td,N,V_edgeCase_poofOutDelay"
- "Td,N,V_edgeCase_response"
- "Tracking Settings"
- "UIImage"
- "Unregistered Velocity Edge Case"
- "WFBannerManager: INFLIGHT REQUEST SET TO: %@"
- "WFIconStackAccessoryView"
- "WFStaccatoIconAccessoryView"
- "WFStaccatoIconAccessoryView.m"
- "WFStaccatoPreviewViewController"
- "WFStaccatoPreviewViewController.m"
- "YES"
- "_action"
- "_bannerWillDismissHandler"
- "_baselineOffsetFromBottom"
- "_blurEnabled"
- "_contentClippingView"
- "_edgeCase_artificialInitialOffset"
- "_edgeCase_impulse"
- "_edgeCase_initialBlurRadius"
- "_edgeCase_initialScale"
- "_edgeCase_poofOutDelay"
- "_edgeCase_response"
- "_hinting"
- "_hintingCompletionTimer"
- "_icon"
- "_iconStackView"
- "_pendingDelayedIcon"
- "_stackView"
- "_subtitleLabel"
- "_unregisteredVelocityEdgeCaseEnabled"
- "action"
- "addChildViewController:"
- "appIconAverageColor"
- "applicationIconImageForBundleIdentifier:"
- "artificialInitialOffset"
- "attributionIcon"
- "attributionTitle"
- "bannerWillDismissHandler"
- "beginHintingEmbeddedPlatterDismissalWithCompletion:"
- "bezierPathWithCGPath:"
- "bezierPathWithRoundedRect:cornerRadius:"
- "blurEnabled"
- "blurEnabled = YES"
- "blurEnabled = YES && trackingBlurEnabled == YES"
- "blurEnabled = YES && trackingBlurEnabled == YES && squeezeEnabled = NO"
- "bundleIdentifier"
- "contentClippingView"
- "dawnFluidityEnabled"
- "didMoveToParentViewController:"
- "edgeCase_artificialInitialOffset"
- "edgeCase_impulse"
- "edgeCase_initialBlurRadius"
- "edgeCase_initialScale"
- "edgeCase_poofOutDelay"
- "edgeCase_response"
- "hinting"
- "hinting request did not find embedded platter, revoking immediately"
- "hintingCompletionTimer"
- "iconImage"
- "iconStackView"
- "impulse"
- "initWithAction:"
- "initWithIcon:resolution:"
- "initWithImage:"
- "initialBlurRadius"
- "initialScale"
- "inputHardEdges"
- "inputIntermediateBitDepth"
- "inputNormalizeEdges"
- "inputQuality"
- "inputRadius"
- "isHinting"
- "last connected host disconnected"
- "loadViewIfNeeded"
- "pauseDismissalHintingAnimation"
- "pendingDelayedIcon"
- "poofOutDelay"
- "presentationLayer"
- "presentationMode"
- "previewIcon"
- "queue_beginHintingDismissalOfPresentedContainerWithReason:"
- "renderIcon:size:"
- "response"
- "sensorIntersectionSizeForLabelAtCenter:size:visibleGlyphFrame:"
- "setAction:"
- "setAttributionIcon:"
- "setAttributionTitle:"
- "setBannerWillDismissHandler:"
- "setBlurEnabled:"
- "setBounds:"
- "setCenter:"
- "setContentClippingView:"
- "setContentMode:"
- "setEdgeCase_artificialInitialOffset:"
- "setEdgeCase_impulse:"
- "setEdgeCase_initialBlurRadius:"
- "setEdgeCase_initialScale:"
- "setEdgeCase_poofOutDelay:"
- "setEdgeCase_response:"
- "setHinting:"
- "setHintingCompletionTimer:"
- "setIconView:"
- "setInAperture:"
- "setMasksToBounds:"
- "setMaximumFractionDigits:"
- "setNumberStyle:"
- "setPendingDelayedIcon:"
- "setUnregisteredVelocityEdgeCaseEnabled:"
- "sizeToFit"
- "stackView"
- "stringFromNumber:"
- "subtitleFont"
- "subtitleLabel"
- "transitionToIconOnlyState"
- "transitionWithView:duration:options:animations:completion:"
- "unregisteredVelocityEdgeCaseEnabled"
- "unregisteredVelocityEdgeCaseEnabled = YES"
- "updatePercentageSubtitleWithValue:"
- "{CGSize=dd}80@0:8{CGPoint=dd}16{CGSize=dd}32{CGRect={CGPoint=dd}{CGSize=dd}}48"

```
