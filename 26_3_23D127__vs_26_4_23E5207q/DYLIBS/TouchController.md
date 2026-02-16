## TouchController

> `/System/Library/Frameworks/TouchController.framework/TouchController`

```diff

 1.0.11.0.0
-  __TEXT.__text: 0xda0c
-  __TEXT.__auth_stubs: 0x560
+  __TEXT.__text: 0xebc0
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_methlist: 0x200c
-  __TEXT.__const: 0x274
+  __TEXT.__const: 0x224
   __TEXT.__cstring: 0x1ab
   __TEXT.__oslogstring: 0x5e
   __TEXT.__gcc_except_tab: 0x30
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x5b8
   __TEXT.__objc_classname: 0x1ed
   __TEXT.__objc_methname: 0x2ccf
   __TEXT.__objc_methtype: 0x608

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xc38
   __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x2c0
+  __AUTH_CONST.__auth_got: 0x290
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__objc_const: 0x6f80

   - /System/Library/PrivateFrameworks/GameControllerSettings.framework/GameControllerSettings
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 40283C20-5A49-3808-BBFA-210DEA879E13
+  UUID: 32D1CEF5-AF67-3E36-BA6A-19C6A2E0259B
   Functions: 663
-  Symbols:   2426
+  Symbols:   2420
   CStrings:  742
 
Symbols:
+ _objc_retain_x26
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x8
Functions:
~ -[TCButtonDescriptor setLabel:] : 12 -> 64
~ -[TCButtonDescriptor setContents:] : 12 -> 64
~ -[TCButton initWithDescriptor:touchController:] : 340 -> 344
~ -[TCButton label] : 8 -> 56
~ -[TCButton setLabel:] : 12 -> 64
~ -[TCButton collectQuadDataInto:] : 496 -> 512
~ -[TCButton setCollider:] : 12 -> 64
~ -[TCButton setContents:] : 12 -> 64
~ +[TCButton(GCSJSONSerializable) descriptorForJsonDictionary:] : 388 -> 412
~ -[TCButton(GCSJSONSerializable) jsonObject] : 444 -> 476
~ -[TCControlContents initWithImages:] : 116 -> 108
~ +[TCControlContents scaleFactor] : 72 -> 76
~ +[TCControlContents textForLabel:] : 140 -> 148
~ +[TCControlContents symbolForLabel:] : 140 -> 148
~ +[TCControlContents buttonContentsForLabel:size:shape:controller:] : 652 -> 696
~ +[TCControlContents buttonContentsForSystemImageNamed:size:shape:controller:] : 468 -> 496
~ +[TCControlContents switchedOnContentsForLabel:size:shape:controller:] : 492 -> 524
~ +[TCControlContents switchedOnContentsForSystemImageNamed:size:shape:controller:] : 488 -> 520
~ +[TCControlContents directionPadContentsForLabel:size:style:direction:controller:] : 696 -> 744
~ +[TCControlContents thumbstickStickContentsOfSize:controller:] : 332 -> 356
~ +[TCControlContents thumbstickBackgroundContentsOfSize:controller:] : 312 -> 332
~ +[TCControlContents throttleIndicatorContentsOfSize:controller:] : 312 -> 332
~ +[TCControlContents throttleBackgroundContentsOfSize:controller:] : 308 -> 328
~ +[TCControlContents buttonImageWithSize:shape:fillColor:strokeColor:shadowColor:] : 784 -> 800
~ +[TCControlContents buttonLabelWithSize:label:] : 504 -> 524
~ +[TCControlContents throttleImageWithSize:fillColor:strokeColor:shadowColor:] : 484 -> 488
~ +[TCControlContents dpadImageWithSize:fillColor:strokeColor:shadowColor:] : 844 -> 856
~ +[TCControlContents rotateImageData:byAngle:] : 244 -> 252
~ +[TCControlContents systemImageNamed:color:size:] : 396 -> 412
~ +[TCControlContents textureForImage:controller:] : 400 -> 404
~ -[TCControlImage initWithTexture:size:highlightTexture:offset:tintColor:] : 208 -> 200
~ -[TCControlImage setTexture:] : 12 -> 64
~ -[TCControlImage setHighlightTexture:] : 12 -> 64
~ +[TCControlLabel buttonA] : 68 -> 84
~ ___25+[TCControlLabel buttonA]_block_invoke : 80 -> 84
~ +[TCControlLabel buttonB] : 68 -> 84
~ ___25+[TCControlLabel buttonB]_block_invoke : 80 -> 84
~ +[TCControlLabel buttonX] : 68 -> 84
~ ___25+[TCControlLabel buttonX]_block_invoke : 80 -> 84
~ +[TCControlLabel buttonY] : 68 -> 84
~ ___25+[TCControlLabel buttonY]_block_invoke : 80 -> 84
~ +[TCControlLabel buttonMenu] : 68 -> 84
~ ___28+[TCControlLabel buttonMenu]_block_invoke : 80 -> 84
~ +[TCControlLabel buttonOptions] : 68 -> 84
~ ___31+[TCControlLabel buttonOptions]_block_invoke : 80 -> 84
~ +[TCControlLabel buttonLeftShoulder] : 68 -> 84
~ ___36+[TCControlLabel buttonLeftShoulder]_block_invoke : 80 -> 84
~ +[TCControlLabel buttonLeftTrigger] : 68 -> 84
~ ___35+[TCControlLabel buttonLeftTrigger]_block_invoke : 80 -> 84
~ +[TCControlLabel buttonRightShoulder] : 68 -> 84
~ ___37+[TCControlLabel buttonRightShoulder]_block_invoke : 80 -> 84
~ +[TCControlLabel buttonRightTrigger] : 68 -> 84
~ ___36+[TCControlLabel buttonRightTrigger]_block_invoke : 80 -> 84
~ +[TCControlLabel leftThumbstick] : 68 -> 84
~ ___32+[TCControlLabel leftThumbstick]_block_invoke : 80 -> 84
~ +[TCControlLabel leftThumbstickButton] : 68 -> 84
~ ___38+[TCControlLabel leftThumbstickButton]_block_invoke : 80 -> 84
~ +[TCControlLabel rightThumbstick] : 68 -> 84
~ ___33+[TCControlLabel rightThumbstick]_block_invoke : 80 -> 84
~ +[TCControlLabel rightThumbstickButton] : 68 -> 84
~ ___39+[TCControlLabel rightThumbstickButton]_block_invoke : 80 -> 84
~ +[TCControlLabel directionPad] : 68 -> 84
~ ___30+[TCControlLabel directionPad]_block_invoke : 80 -> 84
~ -[TCControlLabel isEqual:] : 184 -> 188
~ -[TCControlLabel(GCSJSONSerializable) initWithJSONObject:] : 208 -> 204
~ -[TCControlLabel(GCSJSONSerializable) jsonObject] : 188 -> 196
~ -[TCDirectionPadDescriptor setCompositeLabel:] : 12 -> 64
~ -[TCDirectionPadDescriptor setUpLabel:] : 12 -> 64
~ -[TCDirectionPadDescriptor setDownLabel:] : 12 -> 64
~ -[TCDirectionPadDescriptor setLeftLabel:] : 12 -> 64
~ -[TCDirectionPadDescriptor setRightLabel:] : 12 -> 64
~ -[TCDirectionPadDescriptor setUpContents:] : 12 -> 64
~ -[TCDirectionPadDescriptor setDownContents:] : 12 -> 64
~ -[TCDirectionPadDescriptor setLeftContents:] : 12 -> 64
~ -[TCDirectionPadDescriptor setRightContents:] : 12 -> 64
~ -[TCDirectionPad initWithDescriptor:touchController:] : 608 -> 640
~ -[TCDirectionPad label] : 8 -> 56
~ -[TCDirectionPad processTouch:] : 100 -> 164
~ -[TCDirectionPad collectQuadDataInto:] : 2160 -> 2208
~ -[TCDirectionPad setCollider:] : 12 -> 64
~ -[TCDirectionPad setCompositeLabel:] : 12 -> 64
~ -[TCDirectionPad setUpLabel:] : 12 -> 64
~ -[TCDirectionPad setDownLabel:] : 12 -> 64
~ -[TCDirectionPad setLeftLabel:] : 12 -> 64
~ -[TCDirectionPad setRightLabel:] : 12 -> 64
~ -[TCDirectionPad setUpContents:] : 12 -> 64
~ -[TCDirectionPad setDownContents:] : 12 -> 64
~ -[TCDirectionPad setLeftContents:] : 12 -> 64
~ -[TCDirectionPad setRightContents:] : 12 -> 64
~ +[TCDirectionPad(GCSJSONSerializable) descriptorForJsonDictionary:] : 388 -> 412
~ -[TCDirectionPad(GCSJSONSerializable) jsonObject] : 444 -> 476
~ -[TCSwitchDescriptor setLabel:] : 12 -> 64
~ -[TCSwitchDescriptor setContents:] : 12 -> 64
~ -[TCSwitchDescriptor setSwitchedOnContents:] : 12 -> 64
~ -[TCSwitch initWithDescriptor:touchController:] : 364 -> 372
~ -[TCSwitch label] : 8 -> 56
~ -[TCSwitch setLabel:] : 12 -> 64
~ -[TCSwitch collectQuadDataInto:] : 516 -> 532
~ -[TCSwitch setCollider:] : 12 -> 64
~ -[TCSwitch setContents:] : 12 -> 64
~ -[TCSwitch setSwitchedOnContents:] : 12 -> 64
~ +[TCSwitch(GCSJSONSerializable) descriptorForJsonDictionary:] : 388 -> 412
~ -[TCSwitch(GCSJSONSerializable) jsonObject] : 444 -> 476
~ -[TCThrottleDescriptor setLabel:] : 12 -> 64
~ -[TCThrottleDescriptor setBackgroundContents:] : 12 -> 64
~ -[TCThrottleDescriptor setIndicatorContents:] : 12 -> 64
~ -[TCThrottle initWithDescriptor:touchController:] : 456 -> 464
~ -[TCThrottle label] : 8 -> 56
~ -[TCThrottle setLabel:] : 12 -> 64
~ -[TCThrottle collectQuadDataInto:] : 740 -> 756
~ -[TCThrottle setCollider:] : 12 -> 64
~ -[TCThrottle setBackgroundContents:] : 12 -> 64
~ -[TCThrottle setIndicatorContents:] : 12 -> 64
~ -[TCThrottle(GCSJSONSerializable) jsonObject] : 168 -> 176
~ -[TCThumbstickDescriptor setLabel:] : 12 -> 64
~ -[TCThumbstickDescriptor setBackgroundContents:] : 12 -> 64
~ -[TCThumbstickDescriptor setStickContents:] : 12 -> 64
~ -[TCThumbstick initWithDescriptor:touchController:] : 588 -> 596
~ -[TCThumbstick label] : 8 -> 56
~ -[TCThumbstick setLabel:] : 12 -> 64
~ -[TCThumbstick collectQuadDataInto:] : 800 -> 816
~ -[TCThumbstick setCollider:] : 12 -> 64
~ -[TCThumbstick setBackgroundContents:] : 12 -> 64
~ -[TCThumbstick setStickContents:] : 12 -> 64
~ +[TCThumbstick(GCSJSONSerializable) descriptorForJsonDictionary:] : 472 -> 504
~ -[TCThumbstick(GCSJSONSerializable) jsonObject] : 528 -> 568
~ -[TCTouchpadDescriptor setLabel:] : 12 -> 64
~ -[TCTouchpadDescriptor setContents:] : 12 -> 64
~ -[TCTouchpad initWithDescriptor:touchController:] : 496 -> 500
~ -[TCTouchpad processTouch:] : 240 -> 236
~ -[TCTouchpad label] : 8 -> 56
~ -[TCTouchpad setLabel:] : 12 -> 64
~ -[TCTouchpad collectQuadDataInto:] : 480 -> 492
~ -[TCTouchpad setCollider:] : 12 -> 64
~ -[TCTouchpad setContents:] : 12 -> 64
~ _JSONDictionaryFromCGSize : 228 -> 240
~ _CGSizeFromJSONDictionary : 140 -> 152
~ _JSONDictionaryFromCGPoint : 228 -> 240
~ _CGPointFromJSONDictionary : 140 -> 152
~ -[_TCGameController init] : 948 -> 604
~ -[_TCGameController setValue:forButtonElement:] : 1428 -> 1456
~ ___47-[_TCGameController setValue:forButtonElement:]_block_invoke : 292 -> 312
~ -[_TCGameController setPosition:forDirectionPadElement:] : 828 -> 864
~ ___56-[_TCGameController setPosition:forDirectionPadElement:]_block_invoke : 292 -> 312
~ -[_TCGameController addButtonWithLabel:] : 604 -> 644
~ -[_TCGameController addDirectionPadWithLabel:] : 608 -> 648
~ _getTCLogger : 68 -> 84
~ -[TCTouchController initWithDescriptor:] : 292 -> 304
~ +[TCTouchController isSupported] : 108 -> 116
~ -[TCTouchController buildPipeline] : 1112 -> 1228
~ -[TCTouchController renderUsingRenderCommandEncoder:] : 656 -> 684
~ -[TCTouchController _renderButtonQuadsWithCommandEncoder:] : 1236 -> 1260
~ -[TCTouchController addControl:] : 128 -> 136
~ ___32-[TCTouchController addControl:]_block_invoke : 132 -> 128
~ -[TCTouchController removeControl:] : 128 -> 136
~ ___35-[TCTouchController removeControl:]_block_invoke : 132 -> 128
~ -[TCTouchController addButtonWithDescriptor:] : 152 -> 156
~ -[TCTouchController addSwitchWithDescriptor:] : 152 -> 156
~ -[TCTouchController addThumbstickWithDescriptor:] : 152 -> 156
~ -[TCTouchController addDirectionPadWithDescriptor:] : 420 -> 460
~ -[TCTouchController addThrottleWithDescriptor:] : 152 -> 156
~ -[TCTouchController addTouchpadWithDescriptor:] : 152 -> 156
~ -[TCTouchController controlAtPoint:] : 380 -> 392
~ -[TCTouchController handleTouchBeganAtPoint:index:] : 176 -> 184
~ -[TCTouchController handleTouchMovedAtPoint:index:] : 148 -> 156
~ -[TCTouchController handleTouchEndedAtPoint:index:] : 212 -> 224
~ -[TCTouchController offsetForAnchor:anchorCoordinateSystem:] : 532 -> 536
~ -[TCTouchController connect] : 172 -> 168
~ -[TCTouchController disconnect] : 172 -> 168
~ -[TCTouchController _setButtonValue:forControl:] : 128 -> 140
~ -[TCTouchController _setDirectionPadPosition:forControl:] : 140 -> 152
~ -[TCTouchController automaticallyLayoutControlsForLabels:] : 1252 -> 1312
~ -[TCTouchController _makeButtonWithAnchor:offset:label:colliderShape:] : 324 -> 328
~ -[TCTouchController _makeDpadWithAnchor:offset:label:] : 628 -> 664
~ -[TCTouchController _makeHiddenThumbstickWithLabel:colliderShape:] : 356 -> 364
~ -[TCTouchControllerDescriptor initWithMTKView:] : 148 -> 152
~ -[TCTouchControllerDescriptor setDevice:] : 12 -> 64

```
