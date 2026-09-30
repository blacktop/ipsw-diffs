## EmojiKit

> `/System/Library/PrivateFrameworks/EmojiKit.framework/EmojiKit`

```diff

-41.0.0.0.0
-  __TEXT.__text: 0xabe4
+42.0.0.0.0
+  __TEXT.__text: 0xca00
   __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0xbf4
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x339
+  __TEXT.__objc_methlist: 0xef4
+  __TEXT.__const: 0x160
+  __TEXT.__oslogstring: 0x530
+  __TEXT.__cstring: 0x408
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__oslogstring: 0x25b
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x3c8
-  __TEXT.__objc_classname: 0x1bc
-  __TEXT.__objc_methname: 0x2d06
-  __TEXT.__objc_methtype: 0x990
-  __TEXT.__objc_stubs: 0x2560
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x410
-  __DATA_CONST.__objc_classlist: 0x68
-  __DATA_CONST.__objc_catlist: 0x30
+  __TEXT.__unwind_info: 0x458
+  __TEXT.__objc_classname: 0x217
+  __TEXT.__objc_methname: 0x3711
+  __TEXT.__objc_methtype: 0xa84
+  __TEXT.__objc_stubs: 0x2cc0
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x520
+  __DATA_CONST.__objc_classlist: 0x80
+  __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb28
-  __DATA_CONST.__objc_superrefs: 0x58
+  __DATA_CONST.__objc_selrefs: 0xd28
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0x10
   __AUTH_CONST.__auth_got: 0x390
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x200
-  __AUTH_CONST.__objc_const: 0x1da0
+  __AUTH_CONST.__const: 0xa0
+  __AUTH_CONST.__cfstring: 0x2a0
+  __AUTH_CONST.__objc_const: 0x2380
+  __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x128
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_ivar: 0x16c
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x280

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 276
-  Symbols:   457
-  CStrings:  657
+  Functions: 344
+  Symbols:   535
+  CStrings:  805
 
Symbols:
+ _NSTextAnimationAttributeName
+ _NSTextEffectAttributeName
+ _OBJC_CLASS_$_EMKRippleAnimation
+ _OBJC_CLASS_$_EMKRippleAnimator
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$__UITextAnimation
+ _OBJC_METACLASS_$_EMKGlyphRippler
+ _OBJC_METACLASS_$_EMKRippleAnimation
+ _OBJC_METACLASS_$_EMKRippleAnimator
+ _OBJC_METACLASS_$__EMKTextContainerOverlayView
CStrings:
+ "\x011Q\""
+ "\x05"
+ "\x12\x13"
+ "\x12\x18"
+ "%!p(MISSING) _updateEmojiAttributesOfText"
+ "@\"<EMKTextViewEmojiAnimationDelegate>\""
+ "@\"<_NSTextAnimation>\""
+ "@\"<_NSTextAnimator>\""
+ "@\"EMKRippleAnimation\""
+ "@\"EMKRippleAnimationCoordinator\""
+ "@\"NSObject<OS_os_log>\""
+ "@32@0:8{_NSRange=QQ}16"
+ "@40@0:8@16@24@?32"
+ "@48@0:8@16@24@32@40"
+ "@?16@0:8"
+ "B32@?0@\"EMKEmojiTokenList\"8{_NSRange=QQ}16"
+ "EMKRippleAnimation"
+ "EMKRippleAnimationCoordinator"
+ "EMKRippleAnimator"
+ "RippleAnimation"
+ "T@\"<EMKTextViewEmojiAnimationDelegate>\",W,N,V_emojiAnimationDelegate"
+ "T@\"<_NSTextAnimation>\",&,N,V_glimmerFilterAnimation"
+ "T@\"<_NSTextAnimation>\",&,N,V_scaleRippleAnimation"
+ "T@\"<_NSTextAnimator>\",&,N,V_glimmerAnimator"
+ "T@\"<_NSTextAnimator>\",&,N,V_scaleRippleAnimator"
+ "T@\"EMKRippleAnimation\",&,N,V_animation"
+ "T@\"EMKRippleAnimationCoordinator\",&,N,V_rippleCoordinator"
+ "T@\"NSArray\",&,N,V_rippleAnimations"
+ "T@\"NSObject<OS_os_log>\",&,N,V_log"
+ "T@\"UIColor\",C,N,V_foregroundColor"
+ "T@?,C,N,V_completionHandler"
+ "T@?,C,N,V_notify"
+ "TB,N,GisStopped,V_stopped"
+ "TB,N,GisUsingTextEffectBasedEmojiAnimations"
+ "TB,R,GisUsingTextEffectBasedEmojiAnimations"
+ "TB,R,N,GisIdle"
+ "TB,R,N,GisPlaying"
+ "TQ,N,V_startedRippleAnimationsIndex"
+ "TQ,R,N"
+ "Td,R,N"
+ "_NSTextFilterAnimation"
+ "__legacy_setTokenListsHighlighted_emk:rippler:"
+ "__rippleCoordinatorDidCompleteWithFinished:"
+ "__startLegacyRippleAnimation"
+ "__startTextEffectBasedAnimation"
+ "__textEffects_setTokenListsHighlighted_emk:"
+ "_animation"
+ "_animatorForTextAnimation:notify:"
+ "_completeWithFinished:"
+ "_completionHandler"
+ "_emojiAnimationDelegate"
+ "_foregroundColor"
+ "_glimmerAnimator"
+ "_glimmerFilterAnimation"
+ "_hasNext"
+ "_log"
+ "_notify"
+ "_rippleAnimations"
+ "_rippleCoordinator"
+ "_scaleRippleAnimation"
+ "_scaleRippleAnimator"
+ "_startAnimationAtIndex:"
+ "_startOrStopAnimation: _emojiAnimationActive: %!{(MISSING)BOOL}d - _emojiConversionActive: %!{(MISSING)BOOL}d"
+ "_startOrStopAnimation: stopAnimation: %!{(MISSING)BOOL}d - startAnimation: %!{(MISSING)BOOL}d - hideHighlight: %!{(MISSING)BOOL}d"
+ "_startedRippleAnimationsIndex"
+ "_stopped"
+ "_usingTextEffectBasedEmojiAnimations"
+ "addRippleAnimationForRange_emk:"
+ "allowsTextAnimations"
+ "animation"
+ "animationWithName:"
+ "animator state change for animation %!p(MISSING)"
+ "beginEditing"
+ "bulge"
+ "cleanup ripple coordinator %!p(MISSING)"
+ "cleanupIncludingFilterEffect:"
+ "complete ripple coordinator %!p(MISSING) - finished: %!{(MISSING)BOOL}d"
+ "completionHandler"
+ "coordinator finished: %!{(MISSING)BOOL}d"
+ "created ripple coordinator: %!p(MISSING)"
+ "creating coordinator"
+ "duration"
+ "emojiAnimationDelegate"
+ "endEditing"
+ "finished ripple animation: %!p(MISSING)"
+ "foregroundColor"
+ "glimmer"
+ "glimmerAnimator"
+ "glimmerFilterAnimation"
+ "idle"
+ "idle ripple animator - is last: %!{(MISSING)BOOL}d"
+ "initWithAnimation:foregroundColor:"
+ "initWithGlimmerFilterAnimation:scaleRippleAnimation:"
+ "initWithTextView:animations:foregroundColor:log:"
+ "isIdle"
+ "isPlaying"
+ "isStopped"
+ "isUsingTextEffectBasedEmojiAnimations"
+ "last ripple animation: %!p(MISSING)"
+ "lastObject"
+ "layoutIfNeeded"
+ "newRippleAnimatorForAnimation:foregroundColor:notify_emk:"
+ "nextAnimationTriggerDelay"
+ "notify"
+ "objectAtIndexedSubscript:"
+ "playing"
+ "removeRippleAnimation:includingFilterEffect_emk:"
+ "ripple animations: %!@(MISSING)"
+ "rippleAnimations"
+ "rippleCoordinator"
+ "scaleRipple"
+ "scaleRippleAnimation"
+ "scaleRippleAnimator"
+ "self.rippleCoordinator: %!@(MISSING)"
+ "setAllowsTextAnimations:"
+ "setAnimation:"
+ "setCompletionHandler:"
+ "setConfiguration:"
+ "setEmojiAnimationDelegate:"
+ "setForegroundColor:"
+ "setGlimmerAnimator:"
+ "setGlimmerFilterAnimation:"
+ "setLog:"
+ "setNotify:"
+ "setRippleAnimations:"
+ "setRippleCoordinator:"
+ "setScaleRippleAnimation:"
+ "setScaleRippleAnimator:"
+ "setStartedRippleAnimationsIndex:"
+ "setStopped:"
+ "setUsingTextEffectBasedEmojiAnimations:"
+ "start ripple at index: %!l(MISSING)u - animation: %!p(MISSING)"
+ "start ripple coordinator"
+ "startWithCompletionHandler:"
+ "startWithDuration:"
+ "startedRippleAnimationsIndex"
+ "state"
+ "stop"
+ "stop ripple coordinator %!p(MISSING)"
+ "stopped"
+ "textViewDidEndEmojiRippleAnimation:"
+ "textViewWillBeginEmojiRippleAnimation:"
+ "usingTextEffectBasedEmojiAnimations"
+ "v16@?0@\"<_NSTextAnimator>\"8"
+ "v16@?0@\"EMKRippleAnimator\"8"
+ "v20@?0@\"EMKRippleAnimationCoordinator\"8B16"
+ "v28@0:8@16B24"
+ "was asked to start but no ripple animations specified. %!p(MISSING)"
+ "\xc1"
- "\x011S"
- "\x12\x17"

```
