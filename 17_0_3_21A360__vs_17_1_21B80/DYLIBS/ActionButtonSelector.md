## ActionButtonSelector

> `/System/Library/PrivateFrameworks/ActionButtonSelector.framework/ActionButtonSelector`

```diff

-25.4.0.0.0
-  __TEXT.__text: 0xbc58
-  __TEXT.__auth_stubs: 0x540
-  __TEXT.__objc_methlist: 0x6a8
-  __TEXT.__const: 0x280
-  __TEXT.__gcc_except_tab: 0x298
-  __TEXT.__cstring: 0x482
-  __TEXT.__oslogstring: 0x1b3
-  __TEXT.__unwind_info: 0x42c
-  __TEXT.__objc_classname: 0x25f
-  __TEXT.__objc_methname: 0x206a
-  __TEXT.__objc_methtype: 0xb4f
-  __TEXT.__objc_stubs: 0x2320
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x358
-  __DATA_CONST.__objc_classlist: 0x98
+25.9.0.0.0
+  __TEXT.__text: 0xcc90
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_methlist: 0x6d8
+  __TEXT.__const: 0x2d0
+  __TEXT.__gcc_except_tab: 0x308
+  __TEXT.__cstring: 0x4a6
+  __TEXT.__oslogstring: 0x2fb
+  __TEXT.__unwind_info: 0x47c
+  __TEXT.__objc_classname: 0x291
+  __TEXT.__objc_methname: 0x21b9
+  __TEXT.__objc_methtype: 0xbd5
+  __TEXT.__objc_stubs: 0x23e0
+  __DATA_CONST.__got: 0x60
+  __DATA_CONST.__const: 0x380
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1930
-  __DATA_CONST.__objc_selrefs: 0x9c8
+  __DATA_CONST.__objc_const: 0x1aa8
+  __DATA_CONST.__objc_selrefs: 0xa08
   __DATA_CONST.__objc_arraydata: 0xc0
-  __AUTH_CONST.__objc_const: 0x510
-  __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__cfstring: 0x7c0
+  __AUTH_CONST.__objc_const: 0x5e8
+  __AUTH_CONST.__const: 0x100
+  __AUTH_CONST.__cfstring: 0x860
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x1b0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2b0
-  __AUTH.__objc_data: 0x5f0
-  __DATA.__objc_classrefs: 0x1a8
-  __DATA.__objc_superrefs: 0x78
-  __DATA.__objc_ivar: 0x194
+  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH.__objc_data: 0x690
+  __DATA.__objc_classrefs: 0x1d8
+  __DATA.__objc_superrefs: 0x88
+  __DATA.__objc_ivar: 0x1b8
   __DATA.__data: 0x240
-  __DATA.__bss: 0x70
+  __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/SceneKit.framework/SceneKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/Fluid.framework/Fluid
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C61812DC-E636-3040-98DD-C243BAEDA0C0
-  Functions: 238
-  Symbols:   1219
-  CStrings:  718
+  UUID: 974104F5-428E-31EA-8F97-7DB93C3DFEF2
+  Functions: 265
+  Symbols:   1315
+  CStrings:  758
 
Symbols:
+ +[ABActionSelectorViewController assistantSelectorWithActionItems:selectedIndex:welcomeView:detailsView:]
+ +[ABActionSelectorViewController settingsSelectorWithActionItems:selectedIndex:detailsView:]
+ +[ABLoadingSplashView assistantSplashView]
+ +[ABLoadingSplashView settingsSplashView]
+ -[ABActionSelectorDriver .cxx_destruct]
+ -[ABActionSelectorDriver _sceneParamsForState:]
+ -[ABActionSelectorDriver _scheduleZoomOutIfNeeded]
+ -[ABActionSelectorDriver _updateButtonAnimatorActiveState]
+ -[ABActionSelectorDriver _updateForDisplayLink:]
+ -[ABActionSelectorDriver _updateRenderInputs]
+ -[ABActionSelectorDriver _updateSceneInterpolatorsResettingToTarget:]
+ -[ABActionSelectorDriver _updateTransitionSchedulerState]
+ -[ABActionSelectorDriver _updateWithState:dragProgress:]
+ -[ABActionSelectorDriver didRevealScene]
+ -[ABActionSelectorDriver endDragging]
+ -[ABActionSelectorDriver initWithItems:selectedIndex:isInWelcomeMode:renderBlock:]
+ -[ABActionSelectorDriver isInWelcomeMode]
+ -[ABActionSelectorDriver items]
+ -[ABActionSelectorDriver occlusionDidChange:]
+ -[ABActionSelectorDriver overlayRenderInputs]
+ -[ABActionSelectorDriver pause]
+ -[ABActionSelectorDriver resume]
+ -[ABActionSelectorDriver sceneRenderInputs]
+ -[ABActionSelectorDriver selectedIndex]
+ -[ABActionSelectorDriver startDragging]
+ -[ABActionSelectorDriver updateDragProgress:]
+ -[ABActionSelectorDriver updateItems:animateButtonColor:]
+ -[ABActionSelectorDriver updateSelectedIndex:animateButtonColor:]
+ -[ABActionSelectorDriver updateWithZoomedOutSceneParamsOverride:zoomedInSceneParamsOverride:]
+ -[ABActionSelectorDriver zoomIn]
+ -[ABActionSelectorDriver zoomOutAfterDelay:]
+ -[ABActionSelectorDriver zoomOut]
+ -[ABActionSelectorViewController _didTapToZoomIn]
+ -[ABActionSelectorViewController _doRevealScene]
+ -[ABActionSelectorViewController dealloc]
+ -[ABActionSelectorViewController initWithActionItems:selectedIndex:welcomeView:detailsView:]
+ -[ABActionSelectorViewController overrideSceneParamsWithZoomedOutParams:zoomedInParams:]
+ -[ABActionSelectorViewController selectActionItemWithIndex:animated:]
+ -[ABActionSelectorViewController updateActionItems:animated:]
+ -[ABActionSelectorViewController zoomIn]
+ -[ABActionSelectorViewController zoomOut]
+ -[ABCarouselView _addItemViewForItem:index:]
+ -[ABCarouselView reloadWithItems:animated:]
+ -[ABDeviceButtonAnimator .cxx_destruct]
+ -[ABDeviceButtonAnimator color]
+ -[ABDeviceButtonAnimator initWithBaseColor:]
+ -[ABDeviceButtonAnimator isRingHighlightVisible]
+ -[ABDeviceButtonAnimator islandMode]
+ -[ABDeviceButtonAnimator opacity]
+ -[ABDeviceButtonAnimator pressProgress]
+ -[ABDeviceButtonAnimator setActive:]
+ -[ABDeviceButtonAnimator setBaseColor:animated:]
+ -[ABDeviceButtonAnimator update]
+ -[ABDeviceSceneResourceLoader _didCancelWithToken:completion:]
+ -[ABDeviceSceneViewController _didPresentFrame]
+ -[ABDeviceSceneViewController _subscribeToFramePresentationIfNeeded]
+ -[ABDeviceSceneViewController isScenePresented]
+ -[ABDeviceSceneViewController scenePresentationBarrier]
+ -[ABDeviceSceneViewController setScenePresentationBarrier:]
+ -[ABDeviceSceneViewController viewDidAppear:]
+ -[ABLoadingSplashView .cxx_destruct]
+ -[ABLoadingSplashView initWithAssistantMode:]
+ -[ABLoadingSplashView initWithAssistantMode:].cold.1
+ -[ABLoadingSplashView layoutSubviews]
+ GCC_except_table12
+ GCC_except_table16
+ GCC_except_table18
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table7
+ _ABBackdropHeightRatio
+ _ABWelcomeModeZoomedInSceneParams
+ _ABWelcomeModeZoomedInSceneParams.onceToken
+ _ABWelcomeModeZoomedInSceneParams.params
+ _ABWelcomeModeZoomedOutSceneParams
+ _ABWelcomeModeZoomedOutSceneParams.onceToken
+ _ABWelcomeModeZoomedOutSceneParams.params
+ _MGIsDeviceOfType
+ _OBJC_CLASS_$_ABActionSelectorDriver
+ _OBJC_CLASS_$_ABDeviceButtonAnimator
+ _OBJC_CLASS_$_ABLoadingSplashView
+ _OBJC_CLASS_$_NSHashTable
+ _OBJC_CLASS_$_NSMutableOrderedSet
+ _OBJC_CLASS_$_UIImage
+ _OBJC_IVAR_$_ABActionSelectorDriver._buttonAnimator
+ _OBJC_IVAR_$_ABActionSelectorDriver._displayLink
+ _OBJC_IVAR_$_ABActionSelectorDriver._dragProgress
+ _OBJC_IVAR_$_ABActionSelectorDriver._isInWelcomeMode
+ _OBJC_IVAR_$_ABActionSelectorDriver._isOccluded
+ _OBJC_IVAR_$_ABActionSelectorDriver._isSceneRevealed
+ _OBJC_IVAR_$_ABActionSelectorDriver._items
+ _OBJC_IVAR_$_ABActionSelectorDriver._overlayRenderInputs
+ _OBJC_IVAR_$_ABActionSelectorDriver._renderBlock
+ _OBJC_IVAR_$_ABActionSelectorDriver._sceneInterpolators
+ _OBJC_IVAR_$_ABActionSelectorDriver._sceneRenderInputs
+ _OBJC_IVAR_$_ABActionSelectorDriver._selectedIndex
+ _OBJC_IVAR_$_ABActionSelectorDriver._state
+ _OBJC_IVAR_$_ABActionSelectorDriver._transitionScheduler
+ _OBJC_IVAR_$_ABActionSelectorDriver._zoomedInParams
+ _OBJC_IVAR_$_ABActionSelectorDriver._zoomedOutParams
+ _OBJC_IVAR_$_ABActionSelectorViewController._detailsView
+ _OBJC_IVAR_$_ABActionSelectorViewController._didRevealScene
+ _OBJC_IVAR_$_ABActionSelectorViewController._driver
+ _OBJC_IVAR_$_ABActionSelectorViewController._splashView
+ _OBJC_IVAR_$_ABActionSelectorViewController._tapToZoomInRecognizer
+ _OBJC_IVAR_$_ABActionSelectorViewController._welcomeView
+ _OBJC_IVAR_$_ABDeviceButtonAnimator._active
+ _OBJC_IVAR_$_ABDeviceButtonAnimator._buttonGlowInterpolator
+ _OBJC_IVAR_$_ABDeviceButtonAnimator._buttonPressInterpolator
+ _OBJC_IVAR_$_ABDeviceButtonAnimator._buttonReleaseTimestamp
+ _OBJC_IVAR_$_ABDeviceButtonAnimator._highlightColorInterpolator
+ _OBJC_IVAR_$_ABDeviceButtonAnimator._highlightOpacityInterpolator
+ _OBJC_IVAR_$_ABDeviceButtonAnimator._islandMode
+ _OBJC_IVAR_$_ABDeviceButtonAnimator._ringHighlightVisible
+ _OBJC_IVAR_$_ABDeviceSceneResourceLoader._cancellables
+ _OBJC_IVAR_$_ABDeviceSceneViewController._isScenePresented
+ _OBJC_IVAR_$_ABDeviceSceneViewController._scenePresentationBarrier
+ _OBJC_IVAR_$_ABLoadingSplashView._imageView
+ _OBJC_METACLASS_$_ABActionSelectorDriver
+ _OBJC_METACLASS_$_ABDeviceButtonAnimator
+ _OBJC_METACLASS_$_ABLoadingSplashView
+ __OBJC_$_CLASS_METHODS_ABActionSelectorViewController
+ __OBJC_$_INSTANCE_METHODS_ABActionSelectorDriver
+ __OBJC_$_INSTANCE_METHODS_ABDeviceButtonAnimator
+ __OBJC_$_INSTANCE_METHODS_ABLoadingSplashView
+ __OBJC_$_INSTANCE_VARIABLES_ABActionSelectorDriver
+ __OBJC_$_INSTANCE_VARIABLES_ABDeviceButtonAnimator
+ __OBJC_$_INSTANCE_VARIABLES_ABLoadingSplashView
+ __OBJC_CLASS_RO_$_ABActionSelectorDriver
+ __OBJC_CLASS_RO_$_ABDeviceButtonAnimator
+ __OBJC_CLASS_RO_$_ABLoadingSplashView
+ __OBJC_METACLASS_RO_$_ABActionSelectorDriver
+ __OBJC_METACLASS_RO_$_ABDeviceButtonAnimator
+ __OBJC_METACLASS_RO_$_ABLoadingSplashView
+ ___43-[ABCarouselView reloadWithItems:animated:]_block_invoke
+ ___44-[ABActionSelectorDriver zoomOutAfterDelay:]_block_invoke
+ ___47-[ABDeviceSceneViewController _didPresentFrame]_block_invoke
+ ___54-[ABActionSelectorViewController _revealSceneIfNeeded]_block_invoke_2
+ ___59-[ABDeviceSceneResourceLoader loadResourcesWithCompletion:]_block_invoke.18
+ ___68-[ABDeviceSceneViewController _subscribeToFramePresentationIfNeeded]_block_invoke
+ ___69-[ABActionSelectorDriver _updateSceneInterpolatorsResettingToTarget:]_block_invoke
+ ___92-[ABActionSelectorViewController initWithActionItems:selectedIndex:welcomeView:detailsView:]_block_invoke
+ ___ABWelcomeModeZoomedInSceneParams_block_invoke
+ ___ABWelcomeModeZoomedOutSceneParams_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_56_e8_32bs40r48w_e5_v8?0lw48l8r40l8s32l8
+ ___block_literal_global.89
+ __os_log_error_impl
+ _objc_getProperty
+ _objc_moveWeak
+ _objc_msgSend$_addGPUFramePresentedHandler:
+ _objc_msgSend$_addItemViewForItem:index:
+ _objc_msgSend$_didCancelWithToken:completion:
+ _objc_msgSend$_didPresentFrame
+ _objc_msgSend$_doRevealScene
+ _objc_msgSend$_sceneParamsForState:
+ _objc_msgSend$_subscribeToFramePresentationIfNeeded
+ _objc_msgSend$_updateButtonAnimatorActiveState
+ _objc_msgSend$_updateSceneInterpolatorsResettingToTarget:
+ _objc_msgSend$_updateTransitionSchedulerState
+ _objc_msgSend$animateWithDuration:animations:completion:
+ _objc_msgSend$date
+ _objc_msgSend$imageNamed:inBundle:withConfiguration:
+ _objc_msgSend$initWithActionItems:selectedIndex:welcomeView:detailsView:
+ _objc_msgSend$initWithAssistantMode:
+ _objc_msgSend$initWithImage:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$redColor
+ _objc_msgSend$scenePresentationBarrier
+ _objc_msgSend$setEnabled:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setOpaque:
+ _objc_msgSend$setScenePresentationBarrier:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$weakObjectsHashTable
+ _objc_retain_x28
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_setProperty_atomic
- -[ABActionSelectorViewController _doScheduleUpdateWithMode:afterDelay:]
- -[ABActionSelectorViewController _occlusionDidChange]
- -[ABActionSelectorViewController _sceneStateDidChange:previosState:]
- -[ABActionSelectorViewController _scheduleZoomOutIfNeeded]
- -[ABActionSelectorViewController _updateCurrentMode]
- -[ABActionSelectorViewController _updateHighlightColorAnimated:]
- -[ABActionSelectorViewController initWithActionItems:selectedIndex:mode:contentView:]
- -[ABActionSelectorViewController mode]
- -[ABActionSelectorViewController scheduleUpdateWithMode:]
- -[ABActionSelectorViewController scheduleUpdateWithMode:afterDelay:]
- -[ABActionSelectorViewController setSelectedIndex:]
- -[ABActionSelectorViewController setSelectedIndex:animated:]
- -[ABActionSelectorViewController updateWithActionItems:]
- -[ABActionSelectorViewController updateWithMode:]
- -[ABActionSelectorViewController updateWithZoomedOutStateParamsOverride:zoomedInStateParamsOverride:]
- -[ABActionSelectorViewController viewDidAppear:]
- -[ABCarouselView _carouselItemViewForItem:index:]
- -[ABCarouselView _itemImageViewFrameForIndex:]
- -[ABCarouselView _setupSubviews]
- -[ABCarouselView reloadWithItems:]
- -[ABDeviceSceneDriver .cxx_destruct]
- -[ABDeviceSceneDriver _paramsForState:]
- -[ABDeviceSceneDriver _setButtonAnimationActive:]
- -[ABDeviceSceneDriver _setupInterpolators]
- -[ABDeviceSceneDriver _updateButtonAnimation]
- -[ABDeviceSceneDriver _updateForCurrentStateAnimated:]
- -[ABDeviceSceneDriver _updateForDisplayLink:]
- -[ABDeviceSceneDriver _updateRenderInputs]
- -[ABDeviceSceneDriver _updateWithState:dragProgress:]
- -[ABDeviceSceneDriver endDragging]
- -[ABDeviceSceneDriver initWithState:stateUpdateBlock:renderBlock:]
- -[ABDeviceSceneDriver overlayRenderInputs]
- -[ABDeviceSceneDriver sceneRenderInputs]
- -[ABDeviceSceneDriver startDragging]
- -[ABDeviceSceneDriver start]
- -[ABDeviceSceneDriver state]
- -[ABDeviceSceneDriver stop]
- -[ABDeviceSceneDriver updateDragProgress:]
- -[ABDeviceSceneDriver updateWithItemColor:animated:]
- -[ABDeviceSceneDriver updateWithZoomedOutStateParamsOverride:zoomedInStateParamsOverride:]
- -[ABDeviceSceneDriver zoomIn]
- -[ABDeviceSceneDriver zoomOut]
- -[ABDeviceSceneViewController dealloc]
- GCC_except_table10
- GCC_except_table13
- GCC_except_table25
- GCC_except_table30
- _ABInitialZoomedOutSceneParams
- _ABInitialZoomedOutSceneParams.onceToken
- _ABInitialZoomedOutSceneParams.params
- _OBJC_CLASS_$_ABDeviceSceneDriver
- _OBJC_IVAR_$_ABActionSelectorViewController._actionItems
- _OBJC_IVAR_$_ABActionSelectorViewController._contentView
- _OBJC_IVAR_$_ABActionSelectorViewController._mode
- _OBJC_IVAR_$_ABActionSelectorViewController._sceneDriver
- _OBJC_IVAR_$_ABActionSelectorViewController._selectedIndex
- _OBJC_IVAR_$_ABActionSelectorViewController._transitionScheduler
- _OBJC_IVAR_$_ABDeviceSceneDriver._buttonGlowInterpolator
- _OBJC_IVAR_$_ABDeviceSceneDriver._buttonPressInterpolator
- _OBJC_IVAR_$_ABDeviceSceneDriver._buttonReleaseTimestamp
- _OBJC_IVAR_$_ABDeviceSceneDriver._displayLink
- _OBJC_IVAR_$_ABDeviceSceneDriver._dragProgress
- _OBJC_IVAR_$_ABDeviceSceneDriver._highlightColorInterpolator
- _OBJC_IVAR_$_ABDeviceSceneDriver._highlightOpacityInterpolator
- _OBJC_IVAR_$_ABDeviceSceneDriver._isButtonAnimationActive
- _OBJC_IVAR_$_ABDeviceSceneDriver._isInitialZoomedOutState
- _OBJC_IVAR_$_ABDeviceSceneDriver._isRingHighlightVisible
- _OBJC_IVAR_$_ABDeviceSceneDriver._islandMode
- _OBJC_IVAR_$_ABDeviceSceneDriver._overlayRenderInputs
- _OBJC_IVAR_$_ABDeviceSceneDriver._renderBlock
- _OBJC_IVAR_$_ABDeviceSceneDriver._sceneInterpolators
- _OBJC_IVAR_$_ABDeviceSceneDriver._sceneRenderInputs
- _OBJC_IVAR_$_ABDeviceSceneDriver._state
- _OBJC_IVAR_$_ABDeviceSceneDriver._stateUpdateBlock
- _OBJC_IVAR_$_ABDeviceSceneDriver._zoomedInParams
- _OBJC_IVAR_$_ABDeviceSceneDriver._zoomedOutParams
- _OBJC_METACLASS_$_ABDeviceSceneDriver
- _SCNMatrix4Identity
- __OBJC_$_INSTANCE_METHODS_ABDeviceSceneDriver
- __OBJC_$_INSTANCE_VARIABLES_ABDeviceSceneDriver
- __OBJC_CLASS_RO_$_ABDeviceSceneDriver
- __OBJC_METACLASS_RO_$_ABDeviceSceneDriver
- ___34-[ABCarouselView reloadWithItems:]_block_invoke
- ___54-[ABDeviceSceneDriver _updateForCurrentStateAnimated:]_block_invoke
- ___59-[ABDeviceSceneResourceLoader loadResourcesWithCompletion:]_block_invoke_3
- ___71-[ABActionSelectorViewController _doScheduleUpdateWithMode:afterDelay:]_block_invoke
- ___85-[ABActionSelectorViewController initWithActionItems:selectedIndex:mode:contentView:]_block_invoke
- ___85-[ABActionSelectorViewController initWithActionItems:selectedIndex:mode:contentView:]_block_invoke_2
- ___ABInitialZoomedOutSceneParams_block_invoke
- ___block_descriptor_40_e8_32w_e11_v24?0q8q16lw32l8
- _objc_msgSend$_carouselItemViewForItem:index:
- _objc_msgSend$_doScheduleUpdateWithMode:afterDelay:
- _objc_msgSend$_itemImageViewFrameForIndex:
- _objc_msgSend$_occlusionDidChange
- _objc_msgSend$_paramsForState:
- _objc_msgSend$_sceneStateDidChange:previosState:
- _objc_msgSend$_setButtonAnimationActive:
- _objc_msgSend$_setupInterpolators
- _objc_msgSend$_setupSubviews
- _objc_msgSend$_updateButtonAnimation
- _objc_msgSend$_updateCurrentMode
- _objc_msgSend$_updateForCurrentStateAnimated:
- _objc_msgSend$_updateHighlightColorAnimated:
- _objc_msgSend$actionSelectorViewController:didUpdateMode:
- _objc_msgSend$animateWithDuration:animations:
- _objc_msgSend$removeAllGestureRecognizers
- _objc_msgSend$scheduleUpdateWithMode:afterDelay:
- _objc_msgSend$setSelectedIndex:animated:
- _objc_msgSend$updateWithMode:
- _objc_retain_x26
CStrings:
+ "\x02\x11\x1b"
+ "\x05"
+ "\x06\x12\x11A\xf0\xb1"
+ "\v"
+ "\v\x83!"
+ "(%{public}@) begin loading scene resources"
+ "(%{public}@) delaying scene presentation"
+ "(%{public}@) did present frame"
+ "(%{public}@) loading the view; scene resources are ready: %{public}@"
+ "(%{public}@) pause scene updates"
+ "(%{public}@) requested scene resources, current state is (%{public}@)"
+ "(%{public}@) resume scene updates"
+ "(%{public}@) reveal the scene"
+ "@\"ABActionSelectorDriver\""
+ "@\"ABDeviceButtonAnimator\""
+ "@\"NSHashTable\""
+ "@\"NSMutableOrderedSet\""
+ "@\"UITapGestureRecognizer\""
+ "@\"UIView\""
+ "@\"UIView<ABActionSelectorDetailsView>\""
+ "@20@0:8B16"
+ "@40@0:8@16q24@32"
+ "@48@0:8@16q24@32@40"
+ "ABActionSelectorDriver"
+ "ABDeviceButtonAnimator"
+ "ABLoadingSplashView"
+ "D83"
+ "D84"
+ "Failed to load snapshot image for name: %{public}@"
+ "Finished resource loading, isSuccess: %{public}@"
+ "T@\"NSNumber\",&,V_scenePresentationBarrier"
+ "Unsupported device. Fallback to using screen size."
+ "_active"
+ "_addGPUFramePresentedHandler:"
+ "_addItemViewForItem:index:"
+ "_buttonAnimator"
+ "_cancellables"
+ "_detailsView"
+ "_didCancelWithToken:completion:"
+ "_didPresentFrame"
+ "_didRevealScene"
+ "_didTapToZoomIn"
+ "_doRevealScene"
+ "_driver"
+ "_isInWelcomeMode"
+ "_isOccluded"
+ "_isScenePresented"
+ "_isSceneRevealed"
+ "_ringHighlightVisible"
+ "_sceneParamsForState:"
+ "_scenePresentationBarrier"
+ "_splashView"
+ "_subscribeToFramePresentationIfNeeded"
+ "_tapToZoomInRecognizer"
+ "_updateButtonAnimatorActiveState"
+ "_updateSceneInterpolatorsResettingToTarget:"
+ "_updateTransitionSchedulerState"
+ "_welcomeView"
+ "animateWithDuration:animations:completion:"
+ "assistant"
+ "assistantSelectorWithActionItems:selectedIndex:welcomeView:detailsView:"
+ "date"
+ "imageNamed:inBundle:withConfiguration:"
+ "initWithActionItems:selectedIndex:welcomeView:detailsView:"
+ "initWithAssistantMode:"
+ "initWithImage:"
+ "numberWithBool:"
+ "overrideSceneParamsWithZoomedOutParams:zoomedInParams:"
+ "redColor"
+ "scenePresentationBarrier"
+ "scene_snapshot_%@-%@"
+ "selectActionItemWithIndex:animated:"
+ "setEnabled:"
+ "setObject:atIndexedSubscript:"
+ "setOpaque:"
+ "setScenePresentationBarrier:"
+ "settings"
+ "settingsSelectorWithActionItems:selectedIndex:detailsView:"
+ "stringWithFormat:"
+ "updateActionItems:animated:"
+ "v28@0:8@16B24"
+ "v32@0:8@16@?24"
+ "weakObjectsHashTable"
+ "zoomIn"
+ "zoomOut"
+ "{ABOverlayRenderInputs=\"carouselInputs\"{ABCarouselInputs=\"pressProgress\"d\"itemOpacity\"d\"selectedItemIgnoresOpacity\"B\"isScrollingEnabled\"B}\"highlightRingInputs\"{ABHighlightRingInputs=\"color\"@\"UIColor\"\"isVisible\"B}\"detailsViewOpacity\"d\"welcomeViewOpacity\"d\"topShadowRatio\"d\"isZoomInByTapEnabled\"B}"
+ "\xf0\x81"
- "\x01\x11\x1b"
- "\x02\x18"
- "\v\x83"
- "\fa\xf0\x91"
- "(%{public}@) begin loading scene resources with completion (%{public}@), current state is (%{public}@)"
- "(%{public}@) loading the view; scene resources are ready: (%{public}@)"
- "@\"ABDeviceSceneDriver\""
- "@\"UIView<ABActionSelectorContent>\""
- "@32@0:8@16q24"
- "@48@0:8@16q24q32@40"
- "ABDeviceSceneDriver"
- "Tq,N,V_selectedIndex"
- "_actionItems"
- "_carouselItemViewForItem:index:"
- "_contentView"
- "_doScheduleUpdateWithMode:afterDelay:"
- "_isButtonAnimationActive"
- "_isInitialZoomedOutState"
- "_isRingHighlightVisible"
- "_itemImageViewFrameForIndex:"
- "_mode"
- "_occlusionDidChange"
- "_paramsForState:"
- "_sceneDriver"
- "_sceneStateDidChange:previosState:"
- "_setButtonAnimationActive:"
- "_setupInterpolators"
- "_setupSubviews"
- "_stateUpdateBlock"
- "_updateButtonAnimation"
- "_updateCurrentMode"
- "_updateForCurrentStateAnimated:"
- "_updateHighlightColorAnimated:"
- "actionSelectorViewController:didUpdateMode:"
- "animateWithDuration:animations:"
- "initWithActionItems:selectedIndex:mode:contentView:"
- "mode"
- "removeAllGestureRecognizers"
- "scheduleUpdateWithMode:"
- "scheduleUpdateWithMode:afterDelay:"
- "setSelectedIndex:"
- "setSelectedIndex:animated:"
- "updateWithActionItems:"
- "updateWithMode:"
- "updateWithZoomedOutStateParamsOverride:zoomedInStateParamsOverride:"
- "v24@0:8q16"
- "v24@?0q8q16"
- "v32@0:8q16d24"
- "v32@0:8q16q24"
- "{ABOverlayRenderInputs=\"carouselInputs\"{ABCarouselInputs=\"pressProgress\"d\"itemOpacity\"d\"selectedItemIgnoresOpacity\"B}\"highlightRingInputs\"{ABHighlightRingInputs=\"color\"@\"UIColor\"\"isVisible\"B}\"contentViewOpacity\"d\"topShadowRatio\"d}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8q16"
- "\xf0q"

```
