## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-555.16.0.0.0
-  __TEXT.__text: 0x2a568
-  __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x30fc
+555.21.0.0.0
+  __TEXT.__text: 0x2c324
+  __TEXT.__auth_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x349c
   __TEXT.__const: 0x5b4
-  __TEXT.__oslogstring: 0x1274
-  __TEXT.__cstring: 0x16c2
+  __TEXT.__oslogstring: 0x12d4
+  __TEXT.__cstring: 0x1742
   __TEXT.__gcc_except_tab: 0x5d4
   __TEXT.__swift5_typeref: 0x1da
   __TEXT.__swift5_fieldmd: 0x12c

   __TEXT.__swift5_types: 0x18
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__unwind_info: 0xe10
+  __TEXT.__unwind_info: 0xec8
   __TEXT.__eh_frame: 0x40
-  __TEXT.__objc_classname: 0x10b1
-  __TEXT.__objc_methname: 0x645a
-  __TEXT.__objc_methtype: 0x16a5
-  __TEXT.__objc_stubs: 0x46e0
-  __DATA_CONST.__got: 0x510
+  __TEXT.__objc_classname: 0x1121
+  __TEXT.__objc_methname: 0x6b56
+  __TEXT.__objc_methtype: 0x1805
+  __TEXT.__objc_stubs: 0x4a60
+  __DATA_CONST.__got: 0x530
   __DATA_CONST.__const: 0xab8
-  __DATA_CONST.__objc_classlist: 0x2c0
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17d0
+  __DATA_CONST.__objc_selrefs: 0x1920
   __DATA_CONST.__objc_protorefs: 0x98
-  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x5c0
+  __AUTH_CONST.__auth_got: 0x5d0
   __AUTH_CONST.__const: 0xbc8
-  __AUTH_CONST.__cfstring: 0x1280
-  __AUTH_CONST.__objc_const: 0xf718
+  __AUTH_CONST.__cfstring: 0x1400
+  __AUTH_CONST.__objc_const: 0x10b40
+  __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1c70
+  __AUTH.__objc_data: 0x1db0
   __AUTH.__data: 0xe8
-  __DATA.__objc_ivar: 0x32c
+  __DATA.__objc_ivar: 0x370
   __DATA.__data: 0x11e0
   __DATA.__bss: 0x728
   __DATA.__common: 0xf8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D2EC14AF-0719-3FD7-8FFE-B438B0A0C101
-  Functions: 1248
-  Symbols:   4541
-  CStrings:  1865
+  UUID: 50308D86-E095-393E-96FF-144148E7BBAA
+  Functions: 1320
+  Symbols:   4820
+  CStrings:  1974
 
Symbols:
+ +[CRSUIClusterThemeWallpaperOverlay supportsBSXPCSecureCoding]
+ +[CRSUIPersistentElement supportsBSXPCSecureCoding]
+ +[CRSUIPersistentElement supportsSecureCoding]
+ +[CRSUIPersistentElementRect supportsBSXPCSecureCoding]
+ +[CRSUIPersistentElementRect supportsSecureCoding]
+ +[CRSUIPersistentElements supportsBSXPCSecureCoding]
+ +[CRSUIPersistentElements supportsSecureCoding]
+ -[CRSUIClusterThemeDisplay initWithIdentifier:displayType:size:requiresDarkAppearance:layouts:wallpaperOverlay:]
+ -[CRSUIClusterThemeDisplay wallpaperOverlay]
+ -[CRSUIClusterThemeLayout excludedWallpaperIDs]
+ -[CRSUIClusterThemeLayout initWithIdentifier:displayName:palettes:wallpapers:excludedWallpaperIDs:preview:]
+ -[CRSUIClusterThemeWallpaperOverlay .cxx_destruct]
+ -[CRSUIClusterThemeWallpaperOverlay asset]
+ -[CRSUIClusterThemeWallpaperOverlay encodeWithBSXPCCoder:]
+ -[CRSUIClusterThemeWallpaperOverlay initWithAsset:lightModeState:darkModeState:]
+ -[CRSUIClusterThemeWallpaperOverlay initWithAsset:state:]
+ -[CRSUIClusterThemeWallpaperOverlay initWithBSXPCCoder:]
+ -[CRSUIClusterThemeWallpaperOverlay stateForInterfaceStyle:]
+ -[CRSUIClusterThemeWallpaperOverlay supportsDynamicAppearance]
+ -[CRSUIPersistentElement copyWithZone:]
+ -[CRSUIPersistentElement encodeWithBSXPCCoder:]
+ -[CRSUIPersistentElement encodeWithCoder:]
+ -[CRSUIPersistentElement frame]
+ -[CRSUIPersistentElement initWithBSXPCCoder:]
+ -[CRSUIPersistentElement initWithCoder:]
+ -[CRSUIPersistentElement initWithIsLocallyDrawn:frame:]
+ -[CRSUIPersistentElement init]
+ -[CRSUIPersistentElement isLocallyDrawn]
+ -[CRSUIPersistentElement setFrame:]
+ -[CRSUIPersistentElement setIsLocallyDrawn:]
+ -[CRSUIPersistentElementRect copyWithZone:]
+ -[CRSUIPersistentElementRect encodeWithBSXPCCoder:]
+ -[CRSUIPersistentElementRect encodeWithCoder:]
+ -[CRSUIPersistentElementRect initWithBSXPCCoder:]
+ -[CRSUIPersistentElementRect initWithCoder:]
+ -[CRSUIPersistentElementRect initWithRect:]
+ -[CRSUIPersistentElementRect rect]
+ -[CRSUIPersistentElementRect setRect:]
+ -[CRSUIPersistentElements .cxx_destruct]
+ -[CRSUIPersistentElements _updateFrameForElement:windowFrame:mainWindow:scale:isRHD:]
+ -[CRSUIPersistentElements ac]
+ -[CRSUIPersistentElements canSupport:]
+ -[CRSUIPersistentElements copyWithZone:]
+ -[CRSUIPersistentElements encodeWithBSXPCCoder:]
+ -[CRSUIPersistentElements encodeWithCoder:]
+ -[CRSUIPersistentElements fan]
+ -[CRSUIPersistentElements frontDefrost]
+ -[CRSUIPersistentElements initWithAC:fan:frontDefrost:rearDefrost:targetTemperature:]
+ -[CRSUIPersistentElements initWithBSXPCCoder:]
+ -[CRSUIPersistentElements initWithCoder:]
+ -[CRSUIPersistentElements intersectionElements:]
+ -[CRSUIPersistentElements isEmpty]
+ -[CRSUIPersistentElements isEqualToPersistentElements:]
+ -[CRSUIPersistentElements rearDefrost]
+ -[CRSUIPersistentElements setAc:]
+ -[CRSUIPersistentElements setFan:]
+ -[CRSUIPersistentElements setFrontDefrost:]
+ -[CRSUIPersistentElements setIsEmpty:]
+ -[CRSUIPersistentElements setRearDefrost:]
+ -[CRSUIPersistentElements setSet:]
+ -[CRSUIPersistentElements setTargetTemperature:]
+ -[CRSUIPersistentElements set]
+ -[CRSUIPersistentElements targetTemperature]
+ -[CRSUIPersistentElements updateFramesWithWindowFrame:mainWindowFrame:scale:isRHD:]
+ -[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:automakerPunchthrough:]
+ -[CRSUIStatusBarStyleAssertion automakerPunchthrough]
+ -[CRSUIStatusBarStyleAssertion initForAutomakerPunchthrough]
+ -[CRSUIStatusBarStyleAssertion setAutomakerPunchthrough:]
+ -[CRSUIStatusBarStyleAssertionData isAutomakerPunchthrough]
+ -[CRSUIStatusBarStyleAssertionData setAutomakerPunchthrough:]
+ -[CRSUIStatusBarStyleService clientAcquireForAutomakerPunchthroughWithFenceHandle:animationSettings:]
+ -[CRSUIStatusBarStyleService isAutomakerPunchthrough]
+ GCC_except_table7
+ _CGAffineTransformTranslate
+ _CGRectApplyAffineTransform
+ _CGRectZero
+ _OBJC_CLASS_$_CRSUIClusterThemeWallpaperOverlay
+ _OBJC_CLASS_$_CRSUIPersistentElement
+ _OBJC_CLASS_$_CRSUIPersistentElementRect
+ _OBJC_CLASS_$_CRSUIPersistentElements
+ _OBJC_IVAR_$_CRSUIClusterThemeDisplay._wallpaperOverlay
+ _OBJC_IVAR_$_CRSUIClusterThemeLayout._excludedWallpaperIDs
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaperOverlay._asset
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaperOverlay._darkModeState
+ _OBJC_IVAR_$_CRSUIClusterThemeWallpaperOverlay._lightModeState
+ _OBJC_IVAR_$_CRSUIPersistentElement._frame
+ _OBJC_IVAR_$_CRSUIPersistentElement._isLocallyDrawn
+ _OBJC_IVAR_$_CRSUIPersistentElementRect._rect
+ _OBJC_IVAR_$_CRSUIPersistentElements._ac
+ _OBJC_IVAR_$_CRSUIPersistentElements._fan
+ _OBJC_IVAR_$_CRSUIPersistentElements._frontDefrost
+ _OBJC_IVAR_$_CRSUIPersistentElements._isEmpty
+ _OBJC_IVAR_$_CRSUIPersistentElements._rearDefrost
+ _OBJC_IVAR_$_CRSUIPersistentElements._set
+ _OBJC_IVAR_$_CRSUIPersistentElements._targetTemperature
+ _OBJC_IVAR_$_CRSUIStatusBarStyleAssertion._automakerPunchthrough
+ _OBJC_IVAR_$_CRSUIStatusBarStyleAssertionData._automakerPunchthrough
+ _OBJC_METACLASS_$_CRSUIClusterThemeWallpaperOverlay
+ _OBJC_METACLASS_$_CRSUIPersistentElement
+ _OBJC_METACLASS_$_CRSUIPersistentElementRect
+ _OBJC_METACLASS_$_CRSUIPersistentElements
+ __OBJC_$_CLASS_METHODS_CRSUIClusterThemeWallpaperOverlay
+ __OBJC_$_CLASS_METHODS_CRSUIPersistentElement
+ __OBJC_$_CLASS_METHODS_CRSUIPersistentElementRect
+ __OBJC_$_CLASS_METHODS_CRSUIPersistentElements
+ __OBJC_$_CLASS_PROP_LIST_CRSUIPersistentElement
+ __OBJC_$_CLASS_PROP_LIST_CRSUIPersistentElementRect
+ __OBJC_$_CLASS_PROP_LIST_CRSUIPersistentElements
+ __OBJC_$_INSTANCE_METHODS_CRSUIClusterThemeWallpaperOverlay
+ __OBJC_$_INSTANCE_METHODS_CRSUIPersistentElement
+ __OBJC_$_INSTANCE_METHODS_CRSUIPersistentElementRect
+ __OBJC_$_INSTANCE_METHODS_CRSUIPersistentElements
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIClusterThemeWallpaperOverlay
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIPersistentElement
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIPersistentElementRect
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIPersistentElements
+ __OBJC_$_PROP_LIST_CRSUIClusterThemeWallpaperOverlay
+ __OBJC_$_PROP_LIST_CRSUIPersistentElement
+ __OBJC_$_PROP_LIST_CRSUIPersistentElementRect
+ __OBJC_$_PROP_LIST_CRSUIPersistentElements
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIClusterThemeWallpaperOverlay
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIPersistentElement
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIPersistentElementRect
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIPersistentElements
+ __OBJC_CLASS_RO_$_CRSUIClusterThemeWallpaperOverlay
+ __OBJC_CLASS_RO_$_CRSUIPersistentElement
+ __OBJC_CLASS_RO_$_CRSUIPersistentElementRect
+ __OBJC_CLASS_RO_$_CRSUIPersistentElements
+ __OBJC_METACLASS_RO_$_CRSUIClusterThemeWallpaperOverlay
+ __OBJC_METACLASS_RO_$_CRSUIPersistentElement
+ __OBJC_METACLASS_RO_$_CRSUIPersistentElementRect
+ __OBJC_METACLASS_RO_$_CRSUIPersistentElements
+ ___101-[CRSUIStatusBarStyleService clientAcquireForAutomakerPunchthroughWithFenceHandle:animationSettings:]_block_invoke
+ ___101-[CRSUIStatusBarStyleService clientAcquireForAutomakerPunchthroughWithFenceHandle:animationSettings:]_block_invoke_2
+ ___122-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:automakerPunchthrough:]_block_invoke
+ ___122-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:automakerPunchthrough:]_block_invoke.5
+ ___122-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:automakerPunchthrough:]_block_invoke.5.cold.1
+ ___122-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:automakerPunchthrough:]_block_invoke.6
+ ___122-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:automakerPunchthrough:]_block_invoke.6.cold.1
+ ___122-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:automakerPunchthrough:]_block_invoke_2
+ ___72-[CRSUIStatusBarStyleService listener:didReceiveConnection:withContext:]_block_invoke.123
+ ___block_literal_global.31
+ _objc_msgSend$_initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:automakerPunchthrough:
+ _objc_msgSend$_updateFrameForElement:windowFrame:mainWindow:scale:isRHD:
+ _objc_msgSend$automakerPunchthrough
+ _objc_msgSend$clientAcquireForAutomakerPunchthroughWithFenceHandle:animationSettings:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeObjectForKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$excludedWallpaperIDs
+ _objc_msgSend$initWithAC:fan:frontDefrost:rearDefrost:targetTemperature:
+ _objc_msgSend$initWithAsset:lightModeState:darkModeState:
+ _objc_msgSend$initWithIdentifier:displayName:palettes:wallpapers:excludedWallpaperIDs:preview:
+ _objc_msgSend$initWithIdentifier:displayType:size:requiresDarkAppearance:layouts:wallpaperOverlay:
+ _objc_msgSend$initWithIsLocallyDrawn:frame:
+ _objc_msgSend$initWithRect:
+ _objc_msgSend$intersectSet:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$isAutomakerPunchthrough
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$isLocallyDrawn
+ _objc_msgSend$rect
+ _objc_msgSend$setAc:
+ _objc_msgSend$setAutomakerPunchthrough:
+ _objc_msgSend$setFan:
+ _objc_msgSend$setFrontDefrost:
+ _objc_msgSend$setIsLocallyDrawn:
+ _objc_msgSend$setRearDefrost:
+ _objc_msgSend$setRect:
+ _objc_msgSend$setSet:
+ _objc_msgSend$setTargetTemperature:
+ _objc_msgSend$wallpaperOverlay
- -[CRSUIClusterThemeLayout initWithIdentifier:displayName:palettes:wallpapers:preview:]
- -[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:]
- ___100-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:]_block_invoke
- ___100-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:]_block_invoke.5
- ___100-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:]_block_invoke.5.cold.1
- ___100-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:]_block_invoke.6
- ___100-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:]_block_invoke.6.cold.1
- ___100-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:]_block_invoke_2
- ___72-[CRSUIStatusBarStyleService listener:didReceiveConnection:withContext:]_block_invoke.118
- ___block_literal_global.28
- _objc_msgSend$_initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:
- _objc_msgSend$initWithIdentifier:displayName:palettes:wallpapers:preview:
- _objc_msgSend$initWithIdentifier:displayType:size:requiresDarkAppearance:layouts:
CStrings:
+ "@\"CRSUIClusterThemeWallpaperOverlay\""
+ "@\"CRSUIPersistentElement\""
+ "@\"NSSet\""
+ "@100@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24{CGRect={CGPoint=dd}{CGSize=dd}}56d88B96"
+ "@44@0:8q16q24B32B36B40"
+ "@52@0:8B16{CGRect={CGPoint=dd}{CGSize=dd}}20"
+ "@64@0:8@16@24@32@40@48@56"
+ "@68@0:8@16Q24{CGSize=dd}32B48@52@60"
+ "@92@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48d80B88"
+ "Acquiring assertion for automaker punch through"
+ "CRSUIClusterThemeWallpaperOverlay"
+ "CRSUIPersistentElement"
+ "CRSUIPersistentElementRect"
+ "CRSUIPersistentElements"
+ "Received automaker punchthrough override request!"
+ "T@\"CRSUIClusterThemeWallpaperOverlay\",R,N,V_wallpaperOverlay"
+ "T@\"CRSUIPersistentElement\",&,N,V_ac"
+ "T@\"CRSUIPersistentElement\",&,N,V_fan"
+ "T@\"CRSUIPersistentElement\",&,N,V_frontDefrost"
+ "T@\"CRSUIPersistentElement\",&,N,V_rearDefrost"
+ "T@\"CRSUIPersistentElement\",&,N,V_targetTemperature"
+ "T@\"CRSUIPersistentElements\",C,N"
+ "T@\"CRSUIPersistentElements\",R,C,N"
+ "T@\"NSArray\",R,C,N,V_excludedWallpaperIDs"
+ "T@\"NSSet\",&,N,V_set"
+ "TB,N,GisAutomakerPunchthrough,V_automakerPunchthrough"
+ "TB,N,V_automakerPunchthrough"
+ "TB,N,V_isEmpty"
+ "TB,N,V_isLocallyDrawn"
+ "TB,R,N,GisAutomakerPunchthrough"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_rect"
+ "_ac"
+ "_automakerPunchthrough"
+ "_excludedWallpaperIDs"
+ "_fan"
+ "_frame"
+ "_frontDefrost"
+ "_initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:automakerPunchthrough:"
+ "_isEmpty"
+ "_isLocallyDrawn"
+ "_rearDefrost"
+ "_rect"
+ "_set"
+ "_targetTemperature"
+ "_updateFrameForElement:windowFrame:mainWindow:scale:isRHD:"
+ "_wallpaperOverlay"
+ "ac"
+ "automakerPunchthrough"
+ "canSupport:"
+ "clientAcquireForAutomakerPunchthroughWithFenceHandle:animationSettings:"
+ "containsObject:"
+ "decodeDoubleForKey:"
+ "decodeObjectForKey:"
+ "encodeDouble:forKey:"
+ "excludedWallpaperIDs"
+ "fan"
+ "frontDefrost"
+ "front_defrost"
+ "height"
+ "initForAutomakerPunchthrough"
+ "initWithAC:fan:frontDefrost:rearDefrost:targetTemperature:"
+ "initWithAsset:lightModeState:darkModeState:"
+ "initWithAsset:state:"
+ "initWithIdentifier:displayName:palettes:wallpapers:excludedWallpaperIDs:preview:"
+ "initWithIdentifier:displayType:size:requiresDarkAppearance:layouts:wallpaperOverlay:"
+ "initWithIsLocallyDrawn:frame:"
+ "initWithRect:"
+ "intersectSet:"
+ "intersectionElements:"
+ "intersectsSet:"
+ "isAutomakerPunchthrough"
+ "isEmpty"
+ "isEqualToPersistentElements:"
+ "isEqualToSet:"
+ "isLocallyDrawn"
+ "is_locally_drawn"
+ "rearDefrost"
+ "rear_defrost"
+ "rect"
+ "setAc:"
+ "setAutomakerPunchthrough:"
+ "setFan:"
+ "setFrontDefrost:"
+ "setIsEmpty:"
+ "setIsLocallyDrawn:"
+ "setRearDefrost:"
+ "setRect:"
+ "setSet:"
+ "setTargetTemperature:"
+ "targetTemperature"
+ "target_temperature"
+ "updateFramesWithWindowFrame:mainWindowFrame:scale:isRHD:"
+ "wallpaperOverlay"
+ "width"
+ "x"
+ "y"
- "@40@0:8q16q24B32B36"
- "T@\"NSNumber\",C,N"
- "T@\"NSNumber\",R,C,N"
- "_initWithInterfaceStyle:colorVariant:siriPresentation:standByScreen:"
- "initWithIdentifier:displayName:palettes:wallpapers:preview:"

```
