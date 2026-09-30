## TouchController

> `/System/Library/Frameworks/TouchController.framework/TouchController`

```diff

-1.0.9.0.0
-  __TEXT.__text: 0xbf24
-  __TEXT.__auth_stubs: 0x500
-  __TEXT.__objc_methlist: 0x1c7c
-  __TEXT.__const: 0x254
-  __TEXT.__cstring: 0x1eb
-  __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x370
-  __TEXT.__objc_classname: 0x1de
-  __TEXT.__objc_methname: 0x2b37
-  __TEXT.__objc_methtype: 0x636
-  __TEXT.__objc_stubs: 0x2660
-  __DATA_CONST.__got: 0x280
-  __DATA_CONST.__const: 0x68
-  __DATA_CONST.__objc_classlist: 0xa8
+1.0.11.0.0
+  __TEXT.__text: 0xda0c
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_methlist: 0x200c
+  __TEXT.__const: 0x274
+  __TEXT.__cstring: 0x1ab
+  __TEXT.__oslogstring: 0x5e
+  __TEXT.__gcc_except_tab: 0x30
+  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__objc_classname: 0x1ed
+  __TEXT.__objc_methname: 0x2ccf
+  __TEXT.__objc_methtype: 0x608
+  __TEXT.__objc_stubs: 0x27e0
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0x98
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbd0
-  __DATA_CONST.__objc_superrefs: 0xa0
-  __AUTH_CONST.__auth_got: 0x290
+  __DATA_CONST.__objc_selrefs: 0xc38
+  __DATA_CONST.__objc_superrefs: 0xb0
+  __AUTH_CONST.__auth_got: 0x2c0
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0x4e0
-  __AUTH_CONST.__objc_const: 0x6338
-  __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x3d8
+  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__objc_const: 0x6f80
+  __AUTH.__objc_data: 0x6e0
+  __DATA.__objc_ivar: 0x424
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x130
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 97F47497-238C-36CC-88FE-42FF64080F6E
-  Functions: 584
-  Symbols:   2191
-  CStrings:  773
+  UUID: 142768AD-92CA-3C08-B1AF-CF8A5F6D848D
+  Functions: 663
+  Symbols:   2426
+  CStrings:  742
 
Symbols:
+ +[TCControlContents _cornerRadius]
+ +[TCControlContents _fillColor]
+ +[TCControlContents _iconColor]
+ +[TCControlContents _shadowBlurRadius]
+ +[TCControlContents _shadowColor]
+ +[TCControlContents _shadowOffset]
+ +[TCControlContents _strokeColor]
+ +[TCControlContents _strokeWidth]
+ +[TCControlContents _switchFillColor]
+ +[TCControlContents _switchStrokeColor]
+ +[TCControlContents buttonContentsForLabel:size:shape:controller:]
+ +[TCControlContents buttonContentsForSystemImageNamed:size:shape:controller:]
+ +[TCControlContents buttonImageWithSize:shape:fillColor:strokeColor:shadowColor:]
+ +[TCControlContents buttonLabelWithSize:label:]
+ +[TCControlContents contentsWithImages:]
+ +[TCControlContents directionPadContentsForLabel:size:style:direction:controller:]
+ +[TCControlContents dpadImageWithSize:fillColor:strokeColor:shadowColor:]
+ +[TCControlContents rotateImageData:byAngle:]
+ +[TCControlContents scaleFactor]
+ +[TCControlContents switchedOnContentsForLabel:size:shape:controller:]
+ +[TCControlContents switchedOnContentsForSystemImageNamed:size:shape:controller:]
+ +[TCControlContents symbolForLabel:]
+ +[TCControlContents symbolForLabel:].cold.1
+ +[TCControlContents systemImageNamed:color:size:]
+ +[TCControlContents textForLabel:]
+ +[TCControlContents textForLabel:].cold.1
+ +[TCControlContents textureForImage:controller:]
+ +[TCControlContents throttleBackgroundContentsOfSize:controller:]
+ +[TCControlContents throttleImageWithSize:fillColor:strokeColor:shadowColor:]
+ +[TCControlContents throttleIndicatorContentsOfSize:controller:]
+ +[TCControlContents thumbstickBackgroundContentsOfSize:controller:]
+ +[TCControlContents thumbstickStickContentsOfSize:controller:]
+ +[TCControlLabel labelWithName:role:]
+ +[TCSwitch(GCSJSONSerializable) descriptorForJsonDictionary:]
+ +[TCTouchController isSupported]
+ -[TCButton anchorCoordinateSystem]
+ -[TCButton colliderShape]
+ -[TCButton contents]
+ -[TCButton highlightDuration]
+ -[TCButton highlightIntensity]
+ -[TCButton isEnabled]
+ -[TCButton isPressed]
+ -[TCButton setAnchorCoordinateSystem:]
+ -[TCButton setContents:]
+ -[TCButton setHighlightDuration:]
+ -[TCButton setHighlightIntensity:]
+ -[TCButton setZIndex:]
+ -[TCButton zIndex]
+ -[TCButtonDescriptor anchorCoordinateSystem]
+ -[TCButtonDescriptor colliderShape]
+ -[TCButtonDescriptor contents]
+ -[TCButtonDescriptor highlightDuration]
+ -[TCButtonDescriptor setAnchorCoordinateSystem:]
+ -[TCButtonDescriptor setColliderShape:]
+ -[TCButtonDescriptor setContents:]
+ -[TCButtonDescriptor setHighlightDuration:]
+ -[TCButtonDescriptor setZIndex:]
+ -[TCButtonDescriptor zIndex]
+ -[TCButtonQuad highlightIntensity]
+ -[TCButtonQuad setHighlightIntensity:]
+ -[TCButtonQuad setTintColor:]
+ -[TCButtonQuad tintColor]
+ -[TCCircleCollider colliderShape]
+ -[TCCircleCollider initWithControlLayout:]
+ -[TCCircleCollider isEnabled]
+ -[TCControlContents .cxx_destruct]
+ -[TCControlContents images]
+ -[TCControlContents initWithImages:]
+ -[TCControlImage .cxx_destruct]
+ -[TCControlImage highlightTexture]
+ -[TCControlImage initWithCGImage:size:device:]
+ -[TCControlImage initWithCGImage:size:device:].cold.1
+ -[TCControlImage initWithTexture:size:]
+ -[TCControlImage initWithTexture:size:highlightTexture:offset:tintColor:]
+ -[TCControlImage initWithUIImage:size:device:]
+ -[TCControlImage initWithUIImage:size:device:].cold.1
+ -[TCControlImage offset]
+ -[TCControlImage setHighlightTexture:]
+ -[TCControlImage setOffset:]
+ -[TCControlImage setSize:]
+ -[TCControlImage setTexture:]
+ -[TCControlImage setTintColor:]
+ -[TCControlImage size]
+ -[TCControlImage texture]
+ -[TCControlImage tintColor]
+ -[TCControlLabel initWithName:role:]
+ -[TCControlLabel role]
+ -[TCDirectionPad anchorCoordinateSystem]
+ -[TCDirectionPad colliderShape]
+ -[TCDirectionPad downContents]
+ -[TCDirectionPad highlightDuration]
+ -[TCDirectionPad highlightIntensity]
+ -[TCDirectionPad inputIsMutuallyExclusive]
+ -[TCDirectionPad isEnabled]
+ -[TCDirectionPad isPressed]
+ -[TCDirectionPad leftContents]
+ -[TCDirectionPad rightContents]
+ -[TCDirectionPad setAnchorCoordinateSystem:]
+ -[TCDirectionPad setDownContents:]
+ -[TCDirectionPad setHighlightDuration:]
+ -[TCDirectionPad setHighlightIntensity:]
+ -[TCDirectionPad setLeftContents:]
+ -[TCDirectionPad setRightContents:]
+ -[TCDirectionPad setUpContents:]
+ -[TCDirectionPad setZIndex:]
+ -[TCDirectionPad upContents]
+ -[TCDirectionPad zIndex]
+ -[TCDirectionPadDescriptor anchorCoordinateSystem]
+ -[TCDirectionPadDescriptor colliderShape]
+ -[TCDirectionPadDescriptor downContents]
+ -[TCDirectionPadDescriptor highlightDuration]
+ -[TCDirectionPadDescriptor inputIsMutuallyExclusive]
+ -[TCDirectionPadDescriptor leftContents]
+ -[TCDirectionPadDescriptor rightContents]
+ -[TCDirectionPadDescriptor setAnchorCoordinateSystem:]
+ -[TCDirectionPadDescriptor setColliderShape:]
+ -[TCDirectionPadDescriptor setDownContents:]
+ -[TCDirectionPadDescriptor setHighlightDuration:]
+ -[TCDirectionPadDescriptor setLeftContents:]
+ -[TCDirectionPadDescriptor setRightContents:]
+ -[TCDirectionPadDescriptor setUpContents:]
+ -[TCDirectionPadDescriptor setZIndex:]
+ -[TCDirectionPadDescriptor upContents]
+ -[TCDirectionPadDescriptor zIndex]
+ -[TCRectCollider colliderShape]
+ -[TCRectCollider initWithControlLayout:]
+ -[TCRectCollider isEnabled]
+ -[TCRegionCollider colliderShape]
+ -[TCRegionCollider isEnabled]
+ -[TCSwitch .cxx_destruct]
+ -[TCSwitch _calculatePosition]
+ -[TCSwitch anchorCoordinateSystem]
+ -[TCSwitch anchor]
+ -[TCSwitch collectQuadDataInto:]
+ -[TCSwitch colliderShape]
+ -[TCSwitch collider]
+ -[TCSwitch contents]
+ -[TCSwitch handleTouchBeganAtPoint:]
+ -[TCSwitch handleTouchEndedAtPoint:]
+ -[TCSwitch handleTouchMovedAtPoint:]
+ -[TCSwitch highlightDuration]
+ -[TCSwitch highlightIntensity]
+ -[TCSwitch initWithDescriptor:touchController:]
+ -[TCSwitch isEnabled]
+ -[TCSwitch isPressed]
+ -[TCSwitch isSwitchedOn]
+ -[TCSwitch label]
+ -[TCSwitch layoutIfNeeded]
+ -[TCSwitch offset]
+ -[TCSwitch position]
+ -[TCSwitch setAnchor:]
+ -[TCSwitch setAnchorCoordinateSystem:]
+ -[TCSwitch setCollider:]
+ -[TCSwitch setContents:]
+ -[TCSwitch setEnabled:]
+ -[TCSwitch setHighlightDuration:]
+ -[TCSwitch setHighlightIntensity:]
+ -[TCSwitch setLabel:]
+ -[TCSwitch setOffset:]
+ -[TCSwitch setSize:]
+ -[TCSwitch setSwitchedOnContents:]
+ -[TCSwitch setZIndex:]
+ -[TCSwitch size]
+ -[TCSwitch switchedOnContents]
+ -[TCSwitch touchController]
+ -[TCSwitch zIndex]
+ -[TCSwitch(GCSJSONSerializable) initWithJSONObject:]
+ -[TCSwitch(GCSJSONSerializable) jsonObject]
+ -[TCSwitchDescriptor .cxx_destruct]
+ -[TCSwitchDescriptor anchorCoordinateSystem]
+ -[TCSwitchDescriptor anchor]
+ -[TCSwitchDescriptor colliderShape]
+ -[TCSwitchDescriptor contents]
+ -[TCSwitchDescriptor highlightDuration]
+ -[TCSwitchDescriptor init]
+ -[TCSwitchDescriptor label]
+ -[TCSwitchDescriptor offset]
+ -[TCSwitchDescriptor setAnchor:]
+ -[TCSwitchDescriptor setAnchorCoordinateSystem:]
+ -[TCSwitchDescriptor setColliderShape:]
+ -[TCSwitchDescriptor setContents:]
+ -[TCSwitchDescriptor setHighlightDuration:]
+ -[TCSwitchDescriptor setLabel:]
+ -[TCSwitchDescriptor setOffset:]
+ -[TCSwitchDescriptor setSize:]
+ -[TCSwitchDescriptor setSwitchedOnContents:]
+ -[TCSwitchDescriptor setZIndex:]
+ -[TCSwitchDescriptor size]
+ -[TCSwitchDescriptor switchedOnContents]
+ -[TCSwitchDescriptor zIndex]
+ -[TCThrottle anchorCoordinateSystem]
+ -[TCThrottle backgroundContents]
+ -[TCThrottle colliderShape]
+ -[TCThrottle highlightDuration]
+ -[TCThrottle highlightIntensity]
+ -[TCThrottle indicatorContents]
+ -[TCThrottle isEnabled]
+ -[TCThrottle isPressed]
+ -[TCThrottle setAnchorCoordinateSystem:]
+ -[TCThrottle setBackgroundContents:]
+ -[TCThrottle setHighlightDuration:]
+ -[TCThrottle setHighlightIntensity:]
+ -[TCThrottle setIndicatorContents:]
+ -[TCThrottle setSnapsToBaseValue:]
+ -[TCThrottle setZIndex:]
+ -[TCThrottle snapsToBaseValue]
+ -[TCThrottle zIndex]
+ -[TCThrottleDescriptor anchorCoordinateSystem]
+ -[TCThrottleDescriptor backgroundContents]
+ -[TCThrottleDescriptor colliderShape]
+ -[TCThrottleDescriptor highlightDuration]
+ -[TCThrottleDescriptor indicatorContents]
+ -[TCThrottleDescriptor setAnchorCoordinateSystem:]
+ -[TCThrottleDescriptor setBackgroundContents:]
+ -[TCThrottleDescriptor setColliderShape:]
+ -[TCThrottleDescriptor setHighlightDuration:]
+ -[TCThrottleDescriptor setIndicatorContents:]
+ -[TCThrottleDescriptor setSnapsToBaseValue:]
+ -[TCThrottleDescriptor setZIndex:]
+ -[TCThrottleDescriptor snapsToBaseValue]
+ -[TCThrottleDescriptor zIndex]
+ -[TCThumbstick anchorCoordinateSystem]
+ -[TCThumbstick backgroundContents]
+ -[TCThumbstick colliderShape]
+ -[TCThumbstick hidesWhenNotPressed]
+ -[TCThumbstick highlightDuration]
+ -[TCThumbstick highlightIntensity]
+ -[TCThumbstick isEnabled]
+ -[TCThumbstick isPressed]
+ -[TCThumbstick setAnchorCoordinateSystem:]
+ -[TCThumbstick setBackgroundContents:]
+ -[TCThumbstick setHidesWhenNotPressed:]
+ -[TCThumbstick setHighlightDuration:]
+ -[TCThumbstick setHighlightIntensity:]
+ -[TCThumbstick setStickContents:]
+ -[TCThumbstick setZIndex:]
+ -[TCThumbstick stickContents]
+ -[TCThumbstick zIndex]
+ -[TCThumbstickDescriptor anchorCoordinateSystem]
+ -[TCThumbstickDescriptor backgroundContents]
+ -[TCThumbstickDescriptor colliderShape]
+ -[TCThumbstickDescriptor hidesWhenNotPressed]
+ -[TCThumbstickDescriptor highlightDuration]
+ -[TCThumbstickDescriptor setAnchorCoordinateSystem:]
+ -[TCThumbstickDescriptor setBackgroundContents:]
+ -[TCThumbstickDescriptor setColliderShape:]
+ -[TCThumbstickDescriptor setHidesWhenNotPressed:]
+ -[TCThumbstickDescriptor setHighlightDuration:]
+ -[TCThumbstickDescriptor setStickContents:]
+ -[TCThumbstickDescriptor setZIndex:]
+ -[TCThumbstickDescriptor stickContents]
+ -[TCThumbstickDescriptor zIndex]
+ -[TCTouchController _makeButtonWithAnchor:offset:label:colliderShape:]
+ -[TCTouchController _makeHiddenThumbstickWithLabel:colliderShape:]
+ -[TCTouchController addButtonWithDescriptor:]
+ -[TCTouchController addDirectionPadWithDescriptor:]
+ -[TCTouchController addSwitchWithDescriptor:]
+ -[TCTouchController addThrottleWithDescriptor:]
+ -[TCTouchController addThumbstickWithDescriptor:]
+ -[TCTouchController addTouchpadWithDescriptor:]
+ -[TCTouchController automaticallyLayoutControlsForLabels:]
+ -[TCTouchController drawableSize]
+ -[TCTouchController offsetForAnchor:anchorCoordinateSystem:]
+ -[TCTouchController renderUsingRenderCommandEncoder:]
+ -[TCTouchController setDrawableSize:]
+ -[TCTouchController setSize:]
+ -[TCTouchController size]
+ -[TCTouchController switches]
+ -[TCTouchControllerDescriptor drawableSize]
+ -[TCTouchControllerDescriptor initWithMTKView:]
+ -[TCTouchControllerDescriptor init]
+ -[TCTouchControllerDescriptor setDrawableSize:]
+ -[TCTouchControllerDescriptor setSize:]
+ -[TCTouchControllerDescriptor size]
+ -[TCTouchpad anchorCoordinateSystem]
+ -[TCTouchpad colliderShape]
+ -[TCTouchpad contents]
+ -[TCTouchpad highlightDuration]
+ -[TCTouchpad highlightIntensity]
+ -[TCTouchpad isEnabled]
+ -[TCTouchpad isPressed]
+ -[TCTouchpad reportsRelativeValues]
+ -[TCTouchpad setAnchorCoordinateSystem:]
+ -[TCTouchpad setContents:]
+ -[TCTouchpad setHighlightDuration:]
+ -[TCTouchpad setHighlightIntensity:]
+ -[TCTouchpad setReportsRelativeValues:]
+ -[TCTouchpad setZIndex:]
+ -[TCTouchpad zIndex]
+ -[TCTouchpadDescriptor anchorCoordinateSystem]
+ -[TCTouchpadDescriptor colliderShape]
+ -[TCTouchpadDescriptor contents]
+ -[TCTouchpadDescriptor highlightDuration]
+ -[TCTouchpadDescriptor reportsRelativeValues]
+ -[TCTouchpadDescriptor setAnchorCoordinateSystem:]
+ -[TCTouchpadDescriptor setColliderShape:]
+ -[TCTouchpadDescriptor setContents:]
+ -[TCTouchpadDescriptor setHighlightDuration:]
+ -[TCTouchpadDescriptor setReportsRelativeValues:]
+ -[TCTouchpadDescriptor setZIndex:]
+ -[TCTouchpadDescriptor zIndex]
+ -[_TCGameController addButtonWithLabel:]
+ -[_TCGameController addDirectionPadWithLabel:]
+ _CGColorCreateGenericRGB
+ _MTKTextureLoaderOptionSRGB
+ _OBJC_CLASS_$_GCDeviceButtonInputDescription
+ _OBJC_CLASS_$_GCDeviceDirectionPadDescription
+ _OBJC_CLASS_$_MTKTextureLoader
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_TCControlContents
+ _OBJC_CLASS_$_TCControlImage
+ _OBJC_CLASS_$_TCSwitch
+ _OBJC_CLASS_$_TCSwitchDescriptor
+ _OBJC_IVAR_$_TCButton._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCButton._colliderShape
+ _OBJC_IVAR_$_TCButton._contents
+ _OBJC_IVAR_$_TCButton._highlightDuration
+ _OBJC_IVAR_$_TCButton._zIndex
+ _OBJC_IVAR_$_TCButton.highlightIntensity
+ _OBJC_IVAR_$_TCButtonDescriptor._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCButtonDescriptor._colliderShape
+ _OBJC_IVAR_$_TCButtonDescriptor._contents
+ _OBJC_IVAR_$_TCButtonDescriptor._highlightDuration
+ _OBJC_IVAR_$_TCButtonDescriptor._zIndex
+ _OBJC_IVAR_$_TCButtonQuad._highlightIntensity
+ _OBJC_IVAR_$_TCButtonQuad._tintColor
+ _OBJC_IVAR_$_TCCircleCollider._controlLayout
+ _OBJC_IVAR_$_TCControlContents._images
+ _OBJC_IVAR_$_TCControlImage._highlightTexture
+ _OBJC_IVAR_$_TCControlImage._offset
+ _OBJC_IVAR_$_TCControlImage._size
+ _OBJC_IVAR_$_TCControlImage._texture
+ _OBJC_IVAR_$_TCControlImage._tintColor
+ _OBJC_IVAR_$_TCControlLabel._role
+ _OBJC_IVAR_$_TCDirectionPad._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCDirectionPad._colliderShape
+ _OBJC_IVAR_$_TCDirectionPad._downContents
+ _OBJC_IVAR_$_TCDirectionPad._highlightDuration
+ _OBJC_IVAR_$_TCDirectionPad._leftContents
+ _OBJC_IVAR_$_TCDirectionPad._rightContents
+ _OBJC_IVAR_$_TCDirectionPad._upContents
+ _OBJC_IVAR_$_TCDirectionPad._zIndex
+ _OBJC_IVAR_$_TCDirectionPad.highlightIntensity
+ _OBJC_IVAR_$_TCDirectionPadDescriptor._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCDirectionPadDescriptor._colliderShape
+ _OBJC_IVAR_$_TCDirectionPadDescriptor._downContents
+ _OBJC_IVAR_$_TCDirectionPadDescriptor._highlightDuration
+ _OBJC_IVAR_$_TCDirectionPadDescriptor._leftContents
+ _OBJC_IVAR_$_TCDirectionPadDescriptor._rightContents
+ _OBJC_IVAR_$_TCDirectionPadDescriptor._upContents
+ _OBJC_IVAR_$_TCDirectionPadDescriptor._zIndex
+ _OBJC_IVAR_$_TCRectCollider._controlLayout
+ _OBJC_IVAR_$_TCSwitch._anchor
+ _OBJC_IVAR_$_TCSwitch._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCSwitch._collider
+ _OBJC_IVAR_$_TCSwitch._colliderShape
+ _OBJC_IVAR_$_TCSwitch._contents
+ _OBJC_IVAR_$_TCSwitch._enabled
+ _OBJC_IVAR_$_TCSwitch._highlightDuration
+ _OBJC_IVAR_$_TCSwitch._label
+ _OBJC_IVAR_$_TCSwitch._offset
+ _OBJC_IVAR_$_TCSwitch._position
+ _OBJC_IVAR_$_TCSwitch._size
+ _OBJC_IVAR_$_TCSwitch._switchedOn
+ _OBJC_IVAR_$_TCSwitch._switchedOnContents
+ _OBJC_IVAR_$_TCSwitch._touchController
+ _OBJC_IVAR_$_TCSwitch._zIndex
+ _OBJC_IVAR_$_TCSwitch.highlightIntensity
+ _OBJC_IVAR_$_TCSwitch.pressed
+ _OBJC_IVAR_$_TCSwitchDescriptor._anchor
+ _OBJC_IVAR_$_TCSwitchDescriptor._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCSwitchDescriptor._colliderShape
+ _OBJC_IVAR_$_TCSwitchDescriptor._contents
+ _OBJC_IVAR_$_TCSwitchDescriptor._highlightDuration
+ _OBJC_IVAR_$_TCSwitchDescriptor._label
+ _OBJC_IVAR_$_TCSwitchDescriptor._offset
+ _OBJC_IVAR_$_TCSwitchDescriptor._size
+ _OBJC_IVAR_$_TCSwitchDescriptor._switchedOnContents
+ _OBJC_IVAR_$_TCSwitchDescriptor._zIndex
+ _OBJC_IVAR_$_TCThrottle._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCThrottle._backgroundContents
+ _OBJC_IVAR_$_TCThrottle._colliderShape
+ _OBJC_IVAR_$_TCThrottle._highlightDuration
+ _OBJC_IVAR_$_TCThrottle._indicatorContents
+ _OBJC_IVAR_$_TCThrottle._snapsToBaseValue
+ _OBJC_IVAR_$_TCThrottle._zIndex
+ _OBJC_IVAR_$_TCThrottle.highlightIntensity
+ _OBJC_IVAR_$_TCThrottleDescriptor._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCThrottleDescriptor._backgroundContents
+ _OBJC_IVAR_$_TCThrottleDescriptor._colliderShape
+ _OBJC_IVAR_$_TCThrottleDescriptor._highlightDuration
+ _OBJC_IVAR_$_TCThrottleDescriptor._indicatorContents
+ _OBJC_IVAR_$_TCThrottleDescriptor._snapsToBaseValue
+ _OBJC_IVAR_$_TCThrottleDescriptor._zIndex
+ _OBJC_IVAR_$_TCThumbstick._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCThumbstick._backgroundContents
+ _OBJC_IVAR_$_TCThumbstick._colliderShape
+ _OBJC_IVAR_$_TCThumbstick._hidesWhenNotPressed
+ _OBJC_IVAR_$_TCThumbstick._highlightDuration
+ _OBJC_IVAR_$_TCThumbstick._stickContents
+ _OBJC_IVAR_$_TCThumbstick._zIndex
+ _OBJC_IVAR_$_TCThumbstick.highlightIntensity
+ _OBJC_IVAR_$_TCThumbstickDescriptor._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCThumbstickDescriptor._backgroundContents
+ _OBJC_IVAR_$_TCThumbstickDescriptor._colliderShape
+ _OBJC_IVAR_$_TCThumbstickDescriptor._hidesWhenNotPressed
+ _OBJC_IVAR_$_TCThumbstickDescriptor._highlightDuration
+ _OBJC_IVAR_$_TCThumbstickDescriptor._stickContents
+ _OBJC_IVAR_$_TCThumbstickDescriptor._zIndex
+ _OBJC_IVAR_$_TCTouchController._drawableSize
+ _OBJC_IVAR_$_TCTouchController._size
+ _OBJC_IVAR_$_TCTouchControllerDescriptor._drawableSize
+ _OBJC_IVAR_$_TCTouchControllerDescriptor._size
+ _OBJC_IVAR_$_TCTouchpad._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCTouchpad._colliderShape
+ _OBJC_IVAR_$_TCTouchpad._contents
+ _OBJC_IVAR_$_TCTouchpad._highlightDuration
+ _OBJC_IVAR_$_TCTouchpad._reportsRelativeValues
+ _OBJC_IVAR_$_TCTouchpad._zIndex
+ _OBJC_IVAR_$_TCTouchpad.highlightIntensity
+ _OBJC_IVAR_$_TCTouchpadDescriptor._anchorCoordinateSystem
+ _OBJC_IVAR_$_TCTouchpadDescriptor._colliderShape
+ _OBJC_IVAR_$_TCTouchpadDescriptor._contents
+ _OBJC_IVAR_$_TCTouchpadDescriptor._highlightDuration
+ _OBJC_IVAR_$_TCTouchpadDescriptor._reportsRelativeValues
+ _OBJC_IVAR_$_TCTouchpadDescriptor._zIndex
+ _OBJC_METACLASS_$_TCControlContents
+ _OBJC_METACLASS_$_TCControlImage
+ _OBJC_METACLASS_$_TCSwitch
+ _OBJC_METACLASS_$_TCSwitchDescriptor
+ _TCGameControllerProductCategoryTouchController
+ __OBJC_$_CLASS_METHODS_TCControlContents
+ __OBJC_$_CLASS_METHODS_TCSwitch(GCSJSONSerializable)
+ __OBJC_$_CLASS_PROP_LIST_TCControlLabel
+ __OBJC_$_CLASS_PROP_LIST_TCTouchController
+ __OBJC_$_INSTANCE_METHODS_TCControlContents
+ __OBJC_$_INSTANCE_METHODS_TCControlImage
+ __OBJC_$_INSTANCE_METHODS_TCSwitch(GCSJSONSerializable)
+ __OBJC_$_INSTANCE_METHODS_TCSwitchDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_TCControlContents
+ __OBJC_$_INSTANCE_VARIABLES_TCControlImage
+ __OBJC_$_INSTANCE_VARIABLES_TCSwitch
+ __OBJC_$_INSTANCE_VARIABLES_TCSwitchDescriptor
+ __OBJC_$_PROP_LIST_TCCollider
+ __OBJC_$_PROP_LIST_TCControlContents
+ __OBJC_$_PROP_LIST_TCControlImage
+ __OBJC_$_PROP_LIST_TCControlLayout
+ __OBJC_$_PROP_LIST_TCSwitch
+ __OBJC_$_PROP_LIST_TCSwitchDescriptor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TCControlLayout
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TCControlLayout
+ __OBJC_$_PROTOCOL_REFS_TCControlLayout
+ __OBJC_CLASS_PROTOCOLS_$_TCSwitch
+ __OBJC_CLASS_RO_$_TCControlContents
+ __OBJC_CLASS_RO_$_TCControlImage
+ __OBJC_CLASS_RO_$_TCSwitch
+ __OBJC_CLASS_RO_$_TCSwitchDescriptor
+ __OBJC_LABEL_PROTOCOL_$_TCControlLayout
+ __OBJC_METACLASS_RO_$_TCControlContents
+ __OBJC_METACLASS_RO_$_TCControlImage
+ __OBJC_METACLASS_RO_$_TCSwitch
+ __OBJC_METACLASS_RO_$_TCSwitchDescriptor
+ __OBJC_PROTOCOL_$_TCControlLayout
+ ___34+[TCControlContents textForLabel:]_block_invoke
+ ___36+[TCControlContents symbolForLabel:]_block_invoke
+ ___47-[_TCGameController setValue:forButtonElement:]_block_invoke
+ ___56-[_TCGameController setPosition:forDirectionPadElement:]_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.139
+ ___kCFBooleanTrue
+ __os_log_error_impl
+ __os_log_impl
+ _objc_msgSend$_buttonWithDescription:
+ _objc_msgSend$_cornerRadius
+ _objc_msgSend$_directionPadWithDescription:
+ _objc_msgSend$_fillColor
+ _objc_msgSend$_iconColor
+ _objc_msgSend$_makeButtonWithAnchor:offset:label:colliderShape:
+ _objc_msgSend$_makeHiddenThumbstickWithLabel:colliderShape:
+ _objc_msgSend$_setValue:queue:
+ _objc_msgSend$_shadowBlurRadius
+ _objc_msgSend$_shadowColor
+ _objc_msgSend$_shadowOffset
+ _objc_msgSend$_strokeColor
+ _objc_msgSend$_strokeWidth
+ _objc_msgSend$_switchFillColor
+ _objc_msgSend$_switchStrokeColor
+ _objc_msgSend$addButtonWithDescriptor:
+ _objc_msgSend$addButtonWithLabel:
+ _objc_msgSend$addDirectionPadWithDescriptor:
+ _objc_msgSend$addDirectionPadWithLabel:
+ _objc_msgSend$addThumbstickWithDescriptor:
+ _objc_msgSend$allKeys
+ _objc_msgSend$anchorCoordinateSystem
+ _objc_msgSend$backgroundContents
+ _objc_msgSend$buttonContentsForSystemImageNamed:size:shape:controller:
+ _objc_msgSend$buttons
+ _objc_msgSend$colliderShape
+ _objc_msgSend$contentsWithImages:
+ _objc_msgSend$debugName
+ _objc_msgSend$depthStencilPixelFormat
+ _objc_msgSend$directionPadContentsForLabel:size:style:direction:controller:
+ _objc_msgSend$downContents
+ _objc_msgSend$dpads
+ _objc_msgSend$drawableSize
+ _objc_msgSend$elements
+ _objc_msgSend$handlerQueue
+ _objc_msgSend$hidesWhenNotPressed
+ _objc_msgSend$highlightDuration
+ _objc_msgSend$highlightIntensity
+ _objc_msgSend$images
+ _objc_msgSend$indicatorContents
+ _objc_msgSend$initWithCGImage:size:device:
+ _objc_msgSend$initWithControlLayout:
+ _objc_msgSend$initWithDevice:
+ _objc_msgSend$initWithImages:
+ _objc_msgSend$initWithName:additionalAliases:attributes:nameLocalizationKey:symbolName:sourceAttributes:sourceExtendedEventField:
+ _objc_msgSend$initWithName:additionalAliases:attributes:nameLocalizationKey:symbolName:sourceAttributes:sourceUpExtendedEventField:sourceDownExtendedEventField:sourceLeftExtendedEventField:sourceRightExtendedEventField:
+ _objc_msgSend$initWithName:role:
+ _objc_msgSend$initWithTexture:size:highlightTexture:offset:tintColor:
+ _objc_msgSend$inputIsMutuallyExclusive
+ _objc_msgSend$isMacCatalystApp
+ _objc_msgSend$isPressed
+ _objc_msgSend$isiOSAppOnMac
+ _objc_msgSend$labelWithName:role:
+ _objc_msgSend$leftContents
+ _objc_msgSend$newTextureWithCGImage:options:error:
+ _objc_msgSend$offsetForAnchor:anchorCoordinateSystem:
+ _objc_msgSend$physicalInputProfile
+ _objc_msgSend$processInfo
+ _objc_msgSend$reportsRelativeValues
+ _objc_msgSend$rightContents
+ _objc_msgSend$role
+ _objc_msgSend$scale
+ _objc_msgSend$setBackgroundContents:
+ _objc_msgSend$setColliderShape:
+ _objc_msgSend$setContents:
+ _objc_msgSend$setDownContents:
+ _objc_msgSend$setHidesWhenNotPressed:
+ _objc_msgSend$setHighlightDuration:
+ _objc_msgSend$setHighlightIntensity:
+ _objc_msgSend$setLeftContents:
+ _objc_msgSend$setRightContents:
+ _objc_msgSend$setStickContents:
+ _objc_msgSend$setTintColor:
+ _objc_msgSend$setUpContents:
+ _objc_msgSend$setZIndex:
+ _objc_msgSend$snapsToBaseValue
+ _objc_msgSend$stickContents
+ _objc_msgSend$switchedOnContents
+ _objc_msgSend$textureForImage:controller:
+ _objc_msgSend$thumbstickBackgroundContentsOfSize:controller:
+ _objc_msgSend$thumbstickStickContentsOfSize:controller:
+ _objc_msgSend$tintColor
+ _objc_msgSend$upContents
+ _objc_msgSend$valueChangedHandler
+ _objc_msgSend$xAxis
+ _objc_msgSend$yAxis
+ _objc_msgSend$zIndex
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _os_log_type_enabled
- +[TCControlLabel labelWithName:type:]
- +[TCControlVisuals visualsWithSprites:]
- -[TCButton enabled]
- -[TCButton highlightFactor]
- -[TCButton highlightTime]
- -[TCButton isToggle]
- -[TCButton isToggle].111
- -[TCButton layer]
- -[TCButton pressed]
- -[TCButton setHighlightFactor:]
- -[TCButton setHighlightTime:]
- -[TCButton setLayer:]
- -[TCButton setToggle:]
- -[TCButton setToggleVisuals:]
- -[TCButton setVisuals:]
- -[TCButton toggleVisuals]
- -[TCButton visuals]
- -[TCButtonDescriptor colliderType]
- -[TCButtonDescriptor highlightTime]
- -[TCButtonDescriptor isToggle]
- -[TCButtonDescriptor layer]
- -[TCButtonDescriptor setColliderType:]
- -[TCButtonDescriptor setHighlightTime:]
- -[TCButtonDescriptor setLayer:]
- -[TCButtonDescriptor setToggle:]
- -[TCButtonDescriptor setToggleVisuals:]
- -[TCButtonDescriptor setVisuals:]
- -[TCButtonDescriptor toggleVisuals]
- -[TCButtonDescriptor visuals]
- -[TCButtonQuad colorTint]
- -[TCButtonQuad highlightFactor]
- -[TCButtonQuad setColorTint:]
- -[TCButtonQuad setHighlightFactor:]
- -[TCCircleCollider colliderType]
- -[TCCircleCollider enabled]
- -[TCCircleCollider initWithTransform:]
- -[TCControlLabel initWithName:type:]
- -[TCControlLabel type]
- -[TCControlSystemVisualsProvider .cxx_destruct]
- -[TCControlSystemVisualsProvider buttonImageWithSize:shape:fillColor:strokeColor:shadowColor:]
- -[TCControlSystemVisualsProvider buttonLabelWithSize:label:]
- -[TCControlSystemVisualsProvider buttonVisualsForLabel:ofSize:ofShape:]
- -[TCControlSystemVisualsProvider buttonVisualsForSystemImageNamed:ofSize:ofShape:]
- -[TCControlSystemVisualsProvider directionPadVisualsForLabel:ofSize:ofStyle:withDirection:]
- -[TCControlSystemVisualsProvider dpadImageWithSize:fillColor:strokeColor:shadowColor:]
- -[TCControlSystemVisualsProvider initWithTouchController:]
- -[TCControlSystemVisualsProvider rotateImageData:byAngle:]
- -[TCControlSystemVisualsProvider symbolForLabel:]
- -[TCControlSystemVisualsProvider symbolForLabel:].cold.1
- -[TCControlSystemVisualsProvider systemImageNamed:color:size:]
- -[TCControlSystemVisualsProvider textForLabel:]
- -[TCControlSystemVisualsProvider textForLabel:].cold.1
- -[TCControlSystemVisualsProvider textureForImage:]
- -[TCControlSystemVisualsProvider throttleBackgroundVisualsOfSize:]
- -[TCControlSystemVisualsProvider throttleImageWithSize:fillColor:strokeColor:shadowColor:]
- -[TCControlSystemVisualsProvider throttleIndicatorVisualsOfSize:]
- -[TCControlSystemVisualsProvider thumbstickBackgroundVisualsForLabel:ofSize:]
- -[TCControlSystemVisualsProvider thumbstickStickVisualsForLabel:ofSize:]
- -[TCControlSystemVisualsProvider toggleVisualsForLabel:ofSize:ofShape:]
- -[TCControlSystemVisualsProvider toggleVisualsForSystemImageNamed:ofSize:ofShape:]
- -[TCControlVisuals .cxx_destruct]
- -[TCControlVisuals initWithSprites:]
- -[TCControlVisuals setSprites:]
- -[TCControlVisuals sprites]
- -[TCDirectionPad downVisuals]
- -[TCDirectionPad enabled]
- -[TCDirectionPad hasMutuallyExclusiveInput]
- -[TCDirectionPad highlightFactor]
- -[TCDirectionPad highlightTime]
- -[TCDirectionPad layer]
- -[TCDirectionPad leftVisuals]
- -[TCDirectionPad pressed]
- -[TCDirectionPad rightVisuals]
- -[TCDirectionPad setDownVisuals:]
- -[TCDirectionPad setHighlightFactor:]
- -[TCDirectionPad setHighlightTime:]
- -[TCDirectionPad setLayer:]
- -[TCDirectionPad setLeftVisuals:]
- -[TCDirectionPad setRightVisuals:]
- -[TCDirectionPad setUpVisuals:]
- -[TCDirectionPad upVisuals]
- -[TCDirectionPadDescriptor colliderType]
- -[TCDirectionPadDescriptor downVisuals]
- -[TCDirectionPadDescriptor hasMutuallyExclusiveInput]
- -[TCDirectionPadDescriptor highlightTime]
- -[TCDirectionPadDescriptor layer]
- -[TCDirectionPadDescriptor leftVisuals]
- -[TCDirectionPadDescriptor rightVisuals]
- -[TCDirectionPadDescriptor setColliderType:]
- -[TCDirectionPadDescriptor setDownVisuals:]
- -[TCDirectionPadDescriptor setHighlightTime:]
- -[TCDirectionPadDescriptor setLayer:]
- -[TCDirectionPadDescriptor setLeftVisuals:]
- -[TCDirectionPadDescriptor setRightVisuals:]
- -[TCDirectionPadDescriptor setUpVisuals:]
- -[TCDirectionPadDescriptor upVisuals]
- -[TCRectCollider colliderType]
- -[TCRectCollider enabled]
- -[TCRectCollider initWithTransform:]
- -[TCRegionCollider colliderType]
- -[TCRegionCollider enabled]
- -[TCSpriteRenderer .cxx_destruct]
- -[TCSpriteRenderer colorTint]
- -[TCSpriteRenderer highlightTexture]
- -[TCSpriteRenderer initWithTexture:size:]
- -[TCSpriteRenderer initWithTexture:size:highlightTexture:offset:colorTint:]
- -[TCSpriteRenderer offset]
- -[TCSpriteRenderer setColorTint:]
- -[TCSpriteRenderer setHighlightTexture:]
- -[TCSpriteRenderer setOffset:]
- -[TCSpriteRenderer setSize:]
- -[TCSpriteRenderer setTexture:]
- -[TCSpriteRenderer size]
- -[TCSpriteRenderer texture]
- -[TCThrottle backgroundVisuals]
- -[TCThrottle enabled]
- -[TCThrottle highlightFactor]
- -[TCThrottle highlightTime]
- -[TCThrottle indicatorVisuals]
- -[TCThrottle layer]
- -[TCThrottle pressed]
- -[TCThrottle setBackgroundVisuals:]
- -[TCThrottle setHighlightFactor:]
- -[TCThrottle setHighlightTime:]
- -[TCThrottle setIndicatorVisuals:]
- -[TCThrottle setLayer:]
- -[TCThrottle setSnapToBaseValue:]
- -[TCThrottle snapToBaseValue]
- -[TCThrottleDescriptor backgroundVisuals]
- -[TCThrottleDescriptor colliderType]
- -[TCThrottleDescriptor highlightTime]
- -[TCThrottleDescriptor indicatorVisuals]
- -[TCThrottleDescriptor layer]
- -[TCThrottleDescriptor setBackgroundVisuals:]
- -[TCThrottleDescriptor setColliderType:]
- -[TCThrottleDescriptor setHighlightTime:]
- -[TCThrottleDescriptor setIndicatorVisuals:]
- -[TCThrottleDescriptor setLayer:]
- -[TCThrottleDescriptor setSnapToBaseValue:]
- -[TCThrottleDescriptor snapToBaseValue]
- -[TCThumbstick backgroundVisuals]
- -[TCThumbstick enabled]
- -[TCThumbstick hideWhenNotPressed]
- -[TCThumbstick highlightFactor]
- -[TCThumbstick highlightTime]
- -[TCThumbstick layer]
- -[TCThumbstick pressed]
- -[TCThumbstick setBackgroundVisuals:]
- -[TCThumbstick setHideWhenNotPressed:]
- -[TCThumbstick setHighlightFactor:]
- -[TCThumbstick setHighlightTime:]
- -[TCThumbstick setLayer:]
- -[TCThumbstick setStickVisuals:]
- -[TCThumbstick stickVisuals]
- -[TCThumbstickDescriptor backgroundVisuals]
- -[TCThumbstickDescriptor colliderType]
- -[TCThumbstickDescriptor hideWhenNotPressed]
- -[TCThumbstickDescriptor highlightTime]
- -[TCThumbstickDescriptor layer]
- -[TCThumbstickDescriptor setBackgroundVisuals:]
- -[TCThumbstickDescriptor setColliderType:]
- -[TCThumbstickDescriptor setHideWhenNotPressed:]
- -[TCThumbstickDescriptor setHighlightTime:]
- -[TCThumbstickDescriptor setLayer:]
- -[TCThumbstickDescriptor setStickVisuals:]
- -[TCThumbstickDescriptor stickVisuals]
- -[TCTouchController _handleTouchBeganAtGlobalPoint:index:]
- -[TCTouchController _handleTouchEndedAtGlobalPoint:index:]
- -[TCTouchController _handleTouchMovedAtGlobalPoint:index:]
- -[TCTouchController _makeButtonWithAnchor:offset:label:colliderType:]
- -[TCTouchController _makeHiddenThumbstickWithLabel:colliderType:]
- -[TCTouchController addButton:]
- -[TCTouchController addDirectionPad:]
- -[TCTouchController addThrottle:]
- -[TCTouchController addThumbstick:]
- -[TCTouchController buttonWithDescriptor:]
- -[TCTouchController directionPadWithDescriptor:]
- -[TCTouchController drawableSizeWillChange:scaleFactor:]
- -[TCTouchController offsetForAnchor:]
- -[TCTouchController removeAllButtons]
- -[TCTouchController removeAllDirectionPads]
- -[TCTouchController removeAllThrottles]
- -[TCTouchController removeAllThumbsticks]
- -[TCTouchController removeAllTouchpads]
- -[TCTouchController removeButton:]
- -[TCTouchController removeDirectionPad:]
- -[TCTouchController removeThrottle:]
- -[TCTouchController removeThumbstick:]
- -[TCTouchController removeTouchpad:]
- -[TCTouchController renderWithRenderCommandEncoder:]
- -[TCTouchController scaleFactor]
- -[TCTouchController screenHeight]
- -[TCTouchController screenWidth]
- -[TCTouchController setupDefaultLayoutForLabels:]
- -[TCTouchController throttleWithDescriptor:]
- -[TCTouchController thumbstickWithDescriptor:]
- -[TCTouchController touchpadWithDescriptor:]
- -[TCTouchControllerDescriptor scaleFactor]
- -[TCTouchControllerDescriptor screenHeight]
- -[TCTouchControllerDescriptor screenWidth]
- -[TCTouchControllerDescriptor setScaleFactor:]
- -[TCTouchControllerDescriptor setScreenHeight:]
- -[TCTouchControllerDescriptor setScreenWidth:]
- -[TCTouchpad enabled]
- -[TCTouchpad highlightFactor]
- -[TCTouchpad highlightTime]
- -[TCTouchpad layer]
- -[TCTouchpad pressed]
- -[TCTouchpad reportsDeltas]
- -[TCTouchpad setHighlightFactor:]
- -[TCTouchpad setHighlightTime:]
- -[TCTouchpad setLayer:]
- -[TCTouchpad setReportsDeltas:]
- -[TCTouchpad setVisuals:]
- -[TCTouchpad visuals]
- -[TCTouchpadDescriptor colliderType]
- -[TCTouchpadDescriptor highlightTime]
- -[TCTouchpadDescriptor layer]
- -[TCTouchpadDescriptor reportsDeltas]
- -[TCTouchpadDescriptor setColliderType:]
- -[TCTouchpadDescriptor setHighlightTime:]
- -[TCTouchpadDescriptor setLayer:]
- -[TCTouchpadDescriptor setReportsDeltas:]
- -[TCTouchpadDescriptor setVisuals:]
- -[TCTouchpadDescriptor visuals]
- _GCCurrentProcessLinkedOnAfter
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_TCControlSystemVisualsProvider
- _OBJC_CLASS_$_TCControlVisuals
- _OBJC_CLASS_$_TCSpriteRenderer
- _OBJC_IVAR_$_TCButton._highlightTime
- _OBJC_IVAR_$_TCButton._layer
- _OBJC_IVAR_$_TCButton._toggle
- _OBJC_IVAR_$_TCButton._toggleVisuals
- _OBJC_IVAR_$_TCButton._toggled
- _OBJC_IVAR_$_TCButton._visuals
- _OBJC_IVAR_$_TCButton.highlightFactor
- _OBJC_IVAR_$_TCButtonDescriptor._colliderType
- _OBJC_IVAR_$_TCButtonDescriptor._highlightTime
- _OBJC_IVAR_$_TCButtonDescriptor._layer
- _OBJC_IVAR_$_TCButtonDescriptor._toggle
- _OBJC_IVAR_$_TCButtonDescriptor._toggleVisuals
- _OBJC_IVAR_$_TCButtonDescriptor._visuals
- _OBJC_IVAR_$_TCButtonQuad._colorTint
- _OBJC_IVAR_$_TCButtonQuad._highlightFactor
- _OBJC_IVAR_$_TCCircleCollider._transform
- _OBJC_IVAR_$_TCControlLabel._type
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._cornerRadius
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._fillColor
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._iconColor
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._shadowBlurRadius
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._shadowColor
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._shadowOffset
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._strokeColor
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._strokeWidth
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._toggleFillColor
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._toggleStrokeColor
- _OBJC_IVAR_$_TCControlSystemVisualsProvider._touchController
- _OBJC_IVAR_$_TCControlVisuals._sprites
- _OBJC_IVAR_$_TCDirectionPad._downVisuals
- _OBJC_IVAR_$_TCDirectionPad._highlightTime
- _OBJC_IVAR_$_TCDirectionPad._layer
- _OBJC_IVAR_$_TCDirectionPad._leftVisuals
- _OBJC_IVAR_$_TCDirectionPad._rightVisuals
- _OBJC_IVAR_$_TCDirectionPad._upVisuals
- _OBJC_IVAR_$_TCDirectionPad.highlightFactor
- _OBJC_IVAR_$_TCDirectionPadDescriptor._colliderType
- _OBJC_IVAR_$_TCDirectionPadDescriptor._downVisuals
- _OBJC_IVAR_$_TCDirectionPadDescriptor._highlightTime
- _OBJC_IVAR_$_TCDirectionPadDescriptor._layer
- _OBJC_IVAR_$_TCDirectionPadDescriptor._leftVisuals
- _OBJC_IVAR_$_TCDirectionPadDescriptor._rightVisuals
- _OBJC_IVAR_$_TCDirectionPadDescriptor._upVisuals
- _OBJC_IVAR_$_TCRectCollider._transform
- _OBJC_IVAR_$_TCSpriteRenderer._colorTint
- _OBJC_IVAR_$_TCSpriteRenderer._highlightTexture
- _OBJC_IVAR_$_TCSpriteRenderer._offset
- _OBJC_IVAR_$_TCSpriteRenderer._size
- _OBJC_IVAR_$_TCSpriteRenderer._texture
- _OBJC_IVAR_$_TCThrottle._backgroundVisuals
- _OBJC_IVAR_$_TCThrottle._highlightTime
- _OBJC_IVAR_$_TCThrottle._indicatorVisuals
- _OBJC_IVAR_$_TCThrottle._layer
- _OBJC_IVAR_$_TCThrottle._snapToBaseValue
- _OBJC_IVAR_$_TCThrottle.highlightFactor
- _OBJC_IVAR_$_TCThrottleDescriptor._backgroundVisuals
- _OBJC_IVAR_$_TCThrottleDescriptor._colliderType
- _OBJC_IVAR_$_TCThrottleDescriptor._highlightTime
- _OBJC_IVAR_$_TCThrottleDescriptor._indicatorVisuals
- _OBJC_IVAR_$_TCThrottleDescriptor._layer
- _OBJC_IVAR_$_TCThrottleDescriptor._snapToBaseValue
- _OBJC_IVAR_$_TCThumbstick._backgroundVisuals
- _OBJC_IVAR_$_TCThumbstick._hideWhenNotPressed
- _OBJC_IVAR_$_TCThumbstick._highlightTime
- _OBJC_IVAR_$_TCThumbstick._layer
- _OBJC_IVAR_$_TCThumbstick._stickVisuals
- _OBJC_IVAR_$_TCThumbstick.highlightFactor
- _OBJC_IVAR_$_TCThumbstickDescriptor._backgroundVisuals
- _OBJC_IVAR_$_TCThumbstickDescriptor._colliderType
- _OBJC_IVAR_$_TCThumbstickDescriptor._hideWhenNotPressed
- _OBJC_IVAR_$_TCThumbstickDescriptor._highlightTime
- _OBJC_IVAR_$_TCThumbstickDescriptor._layer
- _OBJC_IVAR_$_TCThumbstickDescriptor._stickVisuals
- _OBJC_IVAR_$_TCTouchController._buttons
- _OBJC_IVAR_$_TCTouchController._directionPads
- _OBJC_IVAR_$_TCTouchController._scaleFactor
- _OBJC_IVAR_$_TCTouchController._screenHeight
- _OBJC_IVAR_$_TCTouchController._screenWidth
- _OBJC_IVAR_$_TCTouchController._throttles
- _OBJC_IVAR_$_TCTouchController._thumbsticks
- _OBJC_IVAR_$_TCTouchController._touchpads
- _OBJC_IVAR_$_TCTouchControllerDescriptor._scaleFactor
- _OBJC_IVAR_$_TCTouchControllerDescriptor._screenHeight
- _OBJC_IVAR_$_TCTouchControllerDescriptor._screenWidth
- _OBJC_IVAR_$_TCTouchpad._highlightTime
- _OBJC_IVAR_$_TCTouchpad._layer
- _OBJC_IVAR_$_TCTouchpad._reportsDeltas
- _OBJC_IVAR_$_TCTouchpad._visuals
- _OBJC_IVAR_$_TCTouchpad.highlightFactor
- _OBJC_IVAR_$_TCTouchpadDescriptor._colliderType
- _OBJC_IVAR_$_TCTouchpadDescriptor._highlightTime
- _OBJC_IVAR_$_TCTouchpadDescriptor._layer
- _OBJC_IVAR_$_TCTouchpadDescriptor._reportsDeltas
- _OBJC_IVAR_$_TCTouchpadDescriptor._visuals
- _OBJC_METACLASS_$_TCControlSystemVisualsProvider
- _OBJC_METACLASS_$_TCControlVisuals
- _OBJC_METACLASS_$_TCSpriteRenderer
- __OBJC_$_CLASS_METHODS_TCControlVisuals
- __OBJC_$_INSTANCE_METHODS_TCControlSystemVisualsProvider
- __OBJC_$_INSTANCE_METHODS_TCControlVisuals
- __OBJC_$_INSTANCE_METHODS_TCSpriteRenderer
- __OBJC_$_INSTANCE_VARIABLES_TCControlSystemVisualsProvider
- __OBJC_$_INSTANCE_VARIABLES_TCControlVisuals
- __OBJC_$_INSTANCE_VARIABLES_TCSpriteRenderer
- __OBJC_$_PROP_LIST_TCControlVisuals
- __OBJC_$_PROP_LIST_TCSpriteRenderer
- __OBJC_$_PROP_LIST_TCTransform
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_TCTransform
- __OBJC_$_PROTOCOL_METHOD_TYPES_TCTransform
- __OBJC_$_PROTOCOL_REFS_TCTransform
- __OBJC_CLASS_RO_$_TCControlSystemVisualsProvider
- __OBJC_CLASS_RO_$_TCControlVisuals
- __OBJC_CLASS_RO_$_TCSpriteRenderer
- __OBJC_LABEL_PROTOCOL_$_TCTransform
- __OBJC_METACLASS_RO_$_TCControlSystemVisualsProvider
- __OBJC_METACLASS_RO_$_TCControlVisuals
- __OBJC_METACLASS_RO_$_TCSpriteRenderer
- __OBJC_PROTOCOL_$_TCTransform
- ___47-[TCControlSystemVisualsProvider textForLabel:]_block_invoke
- ___49-[TCControlSystemVisualsProvider symbolForLabel:]_block_invoke
- ___block_literal_global.126
- ___block_literal_global.30
- _objc_msgSend$_makeButtonWithAnchor:offset:label:colliderType:
- _objc_msgSend$_makeHiddenThumbstickWithLabel:colliderType:
- _objc_msgSend$addButton:
- _objc_msgSend$addDirectionPad:
- _objc_msgSend$addThumbstick:
- _objc_msgSend$backgroundVisuals
- _objc_msgSend$buttonVisualsForLabel:ofSize:ofShape:
- _objc_msgSend$buttonWithDescriptor:
- _objc_msgSend$colliderType
- _objc_msgSend$colorTint
- _objc_msgSend$copy
- _objc_msgSend$directionPadVisualsForLabel:ofSize:ofStyle:withDirection:
- _objc_msgSend$directionPadWithDescriptor:
- _objc_msgSend$downVisuals
- _objc_msgSend$handleTouchBeganAtPoint:index:
- _objc_msgSend$handleTouchEndedAtPoint:index:
- _objc_msgSend$handleTouchMovedAtPoint:index:
- _objc_msgSend$hasMutuallyExclusiveInput
- _objc_msgSend$hideWhenNotPressed
- _objc_msgSend$highlightFactor
- _objc_msgSend$highlightTime
- _objc_msgSend$indicatorVisuals
- _objc_msgSend$initWithName:type:
- _objc_msgSend$initWithSprites:
- _objc_msgSend$initWithTexture:size:highlightTexture:offset:colorTint:
- _objc_msgSend$initWithTouchController:
- _objc_msgSend$initWithTransform:
- _objc_msgSend$isToggle
- _objc_msgSend$labelWithName:type:
- _objc_msgSend$layer
- _objc_msgSend$leftVisuals
- _objc_msgSend$numberWithInt:
- _objc_msgSend$offsetForAnchor:
- _objc_msgSend$pressed
- _objc_msgSend$removeAllButtons
- _objc_msgSend$removeAllDirectionPads
- _objc_msgSend$removeAllThrottles
- _objc_msgSend$removeAllThumbsticks
- _objc_msgSend$removeAllTouchpads
- _objc_msgSend$removeButton:
- _objc_msgSend$removeControl:
- _objc_msgSend$removeDirectionPad:
- _objc_msgSend$removeThrottle:
- _objc_msgSend$removeThumbstick:
- _objc_msgSend$removeTouchpad:
- _objc_msgSend$reportsDeltas
- _objc_msgSend$rightVisuals
- _objc_msgSend$screenHeight
- _objc_msgSend$screenWidth
- _objc_msgSend$setBackgroundVisuals:
- _objc_msgSend$setColliderType:
- _objc_msgSend$setColorTint:
- _objc_msgSend$setDownVisuals:
- _objc_msgSend$setHideWhenNotPressed:
- _objc_msgSend$setHighlightFactor:
- _objc_msgSend$setHighlightTime:
- _objc_msgSend$setLayer:
- _objc_msgSend$setLeftVisuals:
- _objc_msgSend$setRightVisuals:
- _objc_msgSend$setStickVisuals:
- _objc_msgSend$setUpVisuals:
- _objc_msgSend$setVisuals:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$snapToBaseValue
- _objc_msgSend$sprites
- _objc_msgSend$stickVisuals
- _objc_msgSend$textureForImage:
- _objc_msgSend$thumbstickBackgroundVisualsForLabel:ofSize:
- _objc_msgSend$thumbstickStickVisualsForLabel:ofSize:
- _objc_msgSend$thumbstickWithDescriptor:
- _objc_msgSend$toggleVisuals
- _objc_msgSend$type
- _objc_msgSend$upVisuals
- _objc_msgSend$visuals
- _objc_msgSend$visualsWithSprites:
CStrings:
+ ""
+ "%@"
+ "%@ changed: %@"
+ "@\"<TCControlLayout>\""
+ "@\"TCControlContents\""
+ "@48@0:8@16{CGSize=dd}24@40"
+ "@48@0:8^{CGImage=}16{CGSize=dd}24@40"
+ "@56@0:8@16{CGSize=dd}24q40@48"
+ "@64@0:8@16{CGSize=dd}24q40q48@56"
+ "B40@0:8{CGPoint=dd}16q32"
+ "Error creating texture from CGImage: %@"
+ "Failed to get CGImage from UIImage."
+ "T@\"GCController\",R,N"
+ "T@\"NSArray\",R,N"
+ "T@\"NSArray\",R,N,V_images"
+ "T@\"TCControlContents\",&,N,V_backgroundContents"
+ "T@\"TCControlContents\",&,N,V_contents"
+ "T@\"TCControlContents\",&,N,V_downContents"
+ "T@\"TCControlContents\",&,N,V_indicatorContents"
+ "T@\"TCControlContents\",&,N,V_leftContents"
+ "T@\"TCControlContents\",&,N,V_rightContents"
+ "T@\"TCControlContents\",&,N,V_stickContents"
+ "T@\"TCControlContents\",&,N,V_switchedOnContents"
+ "T@\"TCControlContents\",&,N,V_upContents"
+ "T@\"TCTouchController\",R,W,N,V_touchController"
+ "TB,N,GinputIsMutuallyExclusive,V_mutuallyExclusiveInput"
+ "TB,N,GisEnabled"
+ "TB,N,GisEnabled,V_enabled"
+ "TB,N,V_hidesWhenNotPressed"
+ "TB,N,V_reportsRelativeValues"
+ "TB,N,V_snapsToBaseValue"
+ "TB,R,N,GisPressed"
+ "TB,R,N,GisPressed,Vpressed"
+ "TB,R,N,GisSupported"
+ "TB,R,N,GisSwitchedOn,V_switchedOn"
+ "TCControlContents"
+ "TCControlImage"
+ "TCControlLayout"
+ "TCSwitch"
+ "TCSwitchDescriptor"
+ "T^{CGColor=},N,V_tintColor"
+ "Td,?,N"
+ "Td,N,V_highlightDuration"
+ "Tf,N,V_highlightIntensity"
+ "Tq,N,V_anchorCoordinateSystem"
+ "Tq,N,V_colliderShape"
+ "Tq,N,V_zIndex"
+ "Tq,R,N"
+ "Tq,R,N,V_colliderShape"
+ "Tq,R,N,V_role"
+ "T{CGPoint=dd},R,N"
+ "T{CGSize=dd},N,V_drawableSize"
+ "_anchorCoordinateSystem"
+ "_backgroundContents"
+ "_buttonWithDescription:"
+ "_colliderShape"
+ "_contents"
+ "_controlLayout"
+ "_directionPadWithDescription:"
+ "_downContents"
+ "_drawableSize"
+ "_hidesWhenNotPressed"
+ "_highlightDuration"
+ "_highlightIntensity"
+ "_images"
+ "_indicatorContents"
+ "_leftContents"
+ "_makeButtonWithAnchor:offset:label:colliderShape:"
+ "_makeHiddenThumbstickWithLabel:colliderShape:"
+ "_reportsRelativeValues"
+ "_rightContents"
+ "_role"
+ "_setValue:queue:"
+ "_snapsToBaseValue"
+ "_stickContents"
+ "_switchFillColor"
+ "_switchStrokeColor"
+ "_switchedOn"
+ "_switchedOnContents"
+ "_tintColor"
+ "_upContents"
+ "_zIndex"
+ "addButtonWithDescriptor:"
+ "addButtonWithLabel:"
+ "addDirectionPadWithDescriptor:"
+ "addDirectionPadWithLabel:"
+ "addSwitchWithDescriptor:"
+ "addThrottleWithDescriptor:"
+ "addThumbstickWithDescriptor:"
+ "addTouchpadWithDescriptor:"
+ "allKeys"
+ "anchorCoordinateSystem"
+ "automaticallyLayoutControlsForLabels:"
+ "backgroundContents"
+ "buttonContentsForLabel:size:shape:controller:"
+ "buttonContentsForSystemImageNamed:size:shape:controller:"
+ "colliderShape"
+ "contentsWithImages:"
+ "debugName"
+ "depthStencilPixelFormat"
+ "directionPadContentsForLabel:size:style:direction:controller:"
+ "downContents"
+ "dpads"
+ "drawableSize"
+ "elements"
+ "handlerQueue"
+ "hidesWhenNotPressed"
+ "highlightDuration"
+ "highlightIntensity"
+ "images"
+ "indicatorContents"
+ "initWithCGImage:size:device:"
+ "initWithControlLayout:"
+ "initWithDevice:"
+ "initWithImages:"
+ "initWithMTKView:"
+ "initWithName:additionalAliases:attributes:nameLocalizationKey:symbolName:sourceAttributes:sourceExtendedEventField:"
+ "initWithName:additionalAliases:attributes:nameLocalizationKey:symbolName:sourceAttributes:sourceUpExtendedEventField:sourceDownExtendedEventField:sourceLeftExtendedEventField:sourceRightExtendedEventField:"
+ "initWithName:role:"
+ "initWithTexture:size:highlightTexture:offset:tintColor:"
+ "initWithUIImage:size:device:"
+ "inputIsMutuallyExclusive"
+ "isEnabled"
+ "isMacCatalystApp"
+ "isPressed"
+ "isSupported"
+ "isSwitchedOn"
+ "isiOSAppOnMac"
+ "labelWithName:role:"
+ "leftContents"
+ "newTextureWithCGImage:options:error:"
+ "offsetForAnchor:anchorCoordinateSystem:"
+ "physicalInputProfile"
+ "processInfo"
+ "renderUsingRenderCommandEncoder:"
+ "reportsRelativeValues"
+ "rightContents"
+ "role"
+ "scale"
+ "setAnchorCoordinateSystem:"
+ "setBackgroundContents:"
+ "setColliderShape:"
+ "setContents:"
+ "setDownContents:"
+ "setDrawableSize:"
+ "setHidesWhenNotPressed:"
+ "setHighlightDuration:"
+ "setHighlightIntensity:"
+ "setIndicatorContents:"
+ "setLeftContents:"
+ "setReportsRelativeValues:"
+ "setRightContents:"
+ "setSnapsToBaseValue:"
+ "setStickContents:"
+ "setSwitchedOnContents:"
+ "setTintColor:"
+ "setUpContents:"
+ "setZIndex:"
+ "snapsToBaseValue"
+ "stickContents"
+ "supported"
+ "switchedOn"
+ "switchedOnContents"
+ "switchedOnContentsForLabel:size:shape:controller:"
+ "switchedOnContentsForSystemImageNamed:size:shape:controller:"
+ "switches"
+ "textureForImage:controller:"
+ "throttleBackgroundContentsOfSize:controller:"
+ "throttleIndicatorContentsOfSize:controller:"
+ "thumbstickBackgroundContentsOfSize:controller:"
+ "thumbstickStickContentsOfSize:controller:"
+ "tintColor"
+ "upContents"
+ "valueChangedHandler"
+ "xAxis"
+ "yAxis"
+ "zIndex"
+ "{CGPoint=dd}32@0:8q16q24"
+ "\x91"
+ "\xa1"
+ "\xa19"
+ "\xd1"
+ "\xf0!"
+ "\xf0a"
+ "\xf0\xa1"
- "!"
- "#"
- ")"
- "@\"<TCCollider>\"16@0:8"
- "@\"<TCTransform>\""
- "@\"TCControlVisuals\""
- "@\"UIColor\""
- "@32@0:8{CGSize=dd}16"
- "@48@0:8@16{CGSize=dd}24q40"
- "@56@0:8@16{CGSize=dd}24q40q48"
- "A"
- "Apple"
- "B40@0:8{CGPoint=dd}16@32"
- "L1"
- "L2"
- "L3"
- "R1"
- "R2"
- "R3"
- "T@\"<TCCollider>\",&,N"
- "T@\"<TCCollider>\",&,N,V_collider"
- "T@\"NSArray\",&,N,V_sprites"
- "T@\"NSArray\",R,N,V_buttons"
- "T@\"NSArray\",R,N,V_directionPads"
- "T@\"NSArray\",R,N,V_throttles"
- "T@\"NSArray\",R,N,V_thumbsticks"
- "T@\"NSArray\",R,N,V_touchpads"
- "T@\"TCControlVisuals\",&,N,V_backgroundVisuals"
- "T@\"TCControlVisuals\",&,N,V_downVisuals"
- "T@\"TCControlVisuals\",&,N,V_indicatorVisuals"
- "T@\"TCControlVisuals\",&,N,V_leftVisuals"
- "T@\"TCControlVisuals\",&,N,V_rightVisuals"
- "T@\"TCControlVisuals\",&,N,V_stickVisuals"
- "T@\"TCControlVisuals\",&,N,V_toggleVisuals"
- "T@\"TCControlVisuals\",&,N,V_upVisuals"
- "T@\"TCControlVisuals\",&,N,V_visuals"
- "T@\"TCTouchController\",R,N,V_touchController"
- "TB,N"
- "TB,N,GhasMutuallyExclusiveInput,V_mutuallyExclusiveInput"
- "TB,N,GisToggle,V_toggle"
- "TB,N,V_hideWhenNotPressed"
- "TB,N,V_reportsDeltas"
- "TB,N,V_snapToBaseValue"
- "TB,R,N"
- "TB,R,N,GisToggle,V_toggled"
- "TB,R,N,Vpressed"
- "TCControlSystemVisualsProvider"
- "TCControlVisuals"
- "TCSpriteRenderer"
- "TCTransform"
- "T^{CGColor=},N,V_colorTint"
- "Td,N,V_scaleFactor"
- "Td,N,V_screenHeight"
- "Td,N,V_screenWidth"
- "Td,R,N,V_scaleFactor"
- "Td,R,N,V_screenHeight"
- "Td,R,N,V_screenWidth"
- "Tf,?,N"
- "Tf,?,N,VhighlightFactor"
- "Tf,N,V_highlightFactor"
- "Tf,N,V_highlightTime"
- "Ti,N"
- "Ti,N,V_layer"
- "Touch Controls"
- "Tq,N,V_colliderType"
- "Tq,R,N,V_type"
- "X"
- "Y"
- "_backgroundVisuals"
- "_buttons"
- "_colliderType"
- "_colorTint"
- "_directionPads"
- "_downVisuals"
- "_handleTouchBeganAtGlobalPoint:index:"
- "_handleTouchEndedAtGlobalPoint:index:"
- "_handleTouchMovedAtGlobalPoint:index:"
- "_hideWhenNotPressed"
- "_highlightFactor"
- "_highlightTime"
- "_indicatorVisuals"
- "_layer"
- "_leftVisuals"
- "_makeButtonWithAnchor:offset:label:colliderType:"
- "_makeHiddenThumbstickWithLabel:colliderType:"
- "_reportsDeltas"
- "_rightVisuals"
- "_scaleFactor"
- "_screenHeight"
- "_screenWidth"
- "_snapToBaseValue"
- "_sprites"
- "_stickVisuals"
- "_throttles"
- "_thumbsticks"
- "_toggle"
- "_toggleFillColor"
- "_toggleStrokeColor"
- "_toggleVisuals"
- "_toggled"
- "_touchpads"
- "_transform"
- "_type"
- "_upVisuals"
- "_visuals"
- "addButton:"
- "addDirectionPad:"
- "addThrottle:"
- "addThumbstick:"
- "backgroundVisuals"
- "buttonVisualsForLabel:ofSize:ofShape:"
- "buttonVisualsForSystemImageNamed:ofSize:ofShape:"
- "buttonWithDescriptor:"
- "colliderType"
- "colorTint"
- "copy"
- "directionPadVisualsForLabel:ofSize:ofStyle:withDirection:"
- "directionPadWithDescriptor:"
- "downVisuals"
- "drawableSizeWillChange:scaleFactor:"
- "ellipsis"
- "hasMutuallyExclusiveInput"
- "hideWhenNotPressed"
- "highlightFactor"
- "highlightTime"
- "i"
- "i16@0:8"
- "indicatorVisuals"
- "initWithName:type:"
- "initWithSprites:"
- "initWithTexture:size:highlightTexture:offset:colorTint:"
- "initWithTouchController:"
- "initWithTransform:"
- "isToggle"
- "labelWithName:type:"
- "leftVisuals"
- "line.3.horizontal"
- "numberWithInt:"
- "offsetForAnchor:"
- "removeAllButtons"
- "removeAllDirectionPads"
- "removeAllThrottles"
- "removeAllThumbsticks"
- "removeAllTouchpads"
- "removeButton:"
- "removeDirectionPad:"
- "removeThrottle:"
- "removeThumbstick:"
- "removeTouchpad:"
- "renderWithRenderCommandEncoder:"
- "reportsDeltas"
- "rightVisuals"
- "screenHeight"
- "screenWidth"
- "setBackgroundVisuals:"
- "setColliderType:"
- "setColorTint:"
- "setDownVisuals:"
- "setHideWhenNotPressed:"
- "setHighlightFactor:"
- "setHighlightTime:"
- "setIndicatorVisuals:"
- "setLayer:"
- "setLeftVisuals:"
- "setReportsDeltas:"
- "setRightVisuals:"
- "setScaleFactor:"
- "setScreenHeight:"
- "setScreenWidth:"
- "setSnapToBaseValue:"
- "setSprites:"
- "setStickVisuals:"
- "setToggle:"
- "setToggleVisuals:"
- "setUpVisuals:"
- "setVisuals:"
- "setWithObjects:"
- "setupDefaultLayoutForLabels:"
- "snapToBaseValue"
- "sprites"
- "stickVisuals"
- "textureForImage:"
- "throttleBackgroundVisualsOfSize:"
- "throttleIndicatorVisualsOfSize:"
- "throttleWithDescriptor:"
- "thumbstickBackgroundVisualsForLabel:ofSize:"
- "thumbstickStickVisualsForLabel:ofSize:"
- "thumbstickWithDescriptor:"
- "toggle"
- "toggleVisuals"
- "toggleVisualsForLabel:ofSize:ofShape:"
- "toggleVisualsForSystemImageNamed:ofSize:ofShape:"
- "toggled"
- "touchpadWithDescriptor:"
- "type"
- "upVisuals"
- "v20@0:8i16"
- "v24@0:8@\"<TCCollider>\"16"
- "v40@0:8{CGSize=dd}16d32"
- "visuals"
- "visualsWithSprites:"
- "{CGPoint=dd}24@0:8q16"

```
