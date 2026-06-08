## ProgressUI

> `/System/Library/PrivateFrameworks/ProgressUI.framework/ProgressUI`

```diff

-2842.4.0.0.0
-  __TEXT.__text: 0x3360
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x414
+2851.0.0.0.0
+  __TEXT.__text: 0x3230
+  __TEXT.__objc_methlist: 0x41c
   __TEXT.__const: 0x248
   __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__cstring: 0x970
-  __TEXT.__unwind_info: 0x140
-  __TEXT.__objc_classname: 0x77
-  __TEXT.__objc_methname: 0xd4f
-  __TEXT.__objc_methtype: 0x41e
-  __TEXT.__objc_stubs: 0xbc0
-  __DATA_CONST.__got: 0x100
+  __TEXT.__cstring: 0x978
+  __TEXT.__unwind_info: 0x148
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x440
+  __DATA_CONST.__objc_selrefs: 0x448
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x300
+  __DATA_CONST.__got: 0x100
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x620
   __AUTH_CONST.__objc_const: 0xb30
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x88
   __DATA.__data: 0x160

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D06BEF3D-75E0-3106-8015-76D8BA2E667C
-  Functions: 57
-  Symbols:   429
-  CStrings:  378
+  UUID: B45F42F6-A1A9-3308-BC6B-36BB19EE700E
+  Functions: 58
+  Symbols:   432
+  CStrings:  135
 
Symbols:
+ +[PUIProgressWindow _setContextIsSecure:]
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_setContextIsSecure:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x24
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x20
- _objc_retain_x21
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<CAAction>\"32@0:8@\"CALayer\"16@\"NSString\"24"
- "@\"CAContext\""
- "@\"CALayer\""
- "@\"CATextLayer\""
- "@\"FBSDisplayMonitor\""
- "@\"NSMutableArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"PUIEnvironment\""
- "@16@0:8"
- "@20@0:8B16"
- "@24@0:8:16"
- "@24@0:8@?16"
- "@24@0:8B16f20"
- "@28@0:8B16@20"
- "@28@0:8B16f20B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@36@0:8B16B20f24q28"
- "@36@0:8Q16f24q28"
- "@40@0:8:16@24@32"
- "@44@0:8Q16f24q28@36"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "CALayerDelegate"
- "FBSDisplayObserving"
- "NSObject"
- "PUIEnvironment"
- "PUIFramebufferSizeChangeNotifier"
- "PUIProgressWindow"
- "Q16@0:8"
- "T#,R"
- "T@\"CALayer\",R,N,V_appleLogoAssetLayer"
- "T@\"CALayer\",R,N,V_layer"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_errorDescription"
- "TQ,R"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_appleLogoFrameWithinAsset"
- "UTF8String"
- "Vv16@0:8"
- "^{CGColor=}16@0:8"
- "^{CGColor=}24@0:8r^d16"
- "^{CGImage=}"
- "^{CGImage=}32@0:8r*16i24i28"
- "^{_NSZone=}16@0:8"
- "^{__IOSurface=}"
- "_appendErrorDescriptionWithString:"
- "_appleLogo"
- "_appleLogoAssetLayer"
- "_appleLogoFrameWithinAsset"
- "_appleTVProductSuffix"
- "_collectDisplayInfo"
- "_context"
- "_copyBlackCGColorRef"
- "_copyCGColorRefWithComponents:"
- "_copyWhiteCGColorRef"
- "_createContext"
- "_createImageWithName:scale:displayHeight:"
- "_createLayer"
- "_currentDeviceShouldMuteErrors"
- "_currentProgress"
- "_deviceClass"
- "_displayMonitor"
- "_displayOrientation"
- "_displayScale"
- "_displaySize"
- "_drawProgressLayerInContext:"
- "_environment"
- "_errorDescription"
- "_errorDescriptionForAppleLogoNotFound"
- "_errorDescriptionForUnknownDeviceClass"
- "_errorDescriptionForUnsupportedScreenClass"
- "_forceInverted"
- "_framebufferListenerToken"
- "_framebufferSize"
- "_initWithOptions:contextLevel:appearance:environment:"
- "_ioSurface"
- "_ioSurfaceLayer"
- "_isSecurityResearchDevice"
- "_layer"
- "_layerPositioningSize"
- "_layoutScreen"
- "_listeners"
- "_onMainQueue_notifyListeners"
- "_productSuffix"
- "_productType"
- "_progressHeight"
- "_progressLayer"
- "_progressWidth"
- "_progressXDelta"
- "_progressYDelta"
- "_renderWithIOSurface"
- "_screenClass"
- "_showsProgressBar"
- "_sideways"
- "_statusTextLayer"
- "_unsupportedScreenClass"
- "_updateIOSurface"
- "_updateLayerForFramebufferSize:"
- "_usesPreBoardAppearance"
- "_weCreatedTheContext"
- "_white"
- "actionForLayer:forKey:"
- "addListener:"
- "addObject:"
- "addObserver:"
- "addSublayer:"
- "affineTransform"
- "appleLogoAssetLayer"
- "appleLogoFrameWithinAsset"
- "arrayWithObjects:count:"
- "autorelease"
- "begin"
- "bounds"
- "bundleForClass:"
- "class"
- "commit"
- "conformsToProtocol:"
- "containsObject:"
- "copy"
- "countByEnumeratingWithState:objects:count:"
- "currentMode"
- "d"
- "dealloc"
- "debugDescription"
- "description"
- "deviceClass"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "displayLayer:"
- "displayMonitor:didConnectIdentity:withConfiguration:"
- "displayMonitor:didUpdateIdentity:withConfiguration:"
- "displayMonitor:willDisconnectIdentity:"
- "drawLayer:inContext:"
- "errorDescription"
- "f"
- "firstObject"
- "floatValue"
- "hash"
- "i"
- "i16@0:8"
- "init"
- "initWithForceInverted:"
- "initWithInitializationCompletion:"
- "initWithOptions:contextLevel:appearance:"
- "initWithProgressBarVisibility:"
- "initWithProgressBarVisibility:context:"
- "initWithProgressBarVisibility:createContext:contextLevel:appearance:"
- "initWithProgressBarVisibility:level:"
- "initWithProgressBarVisibility:level:forceInverted:"
- "invalidate"
- "isEqual:"
- "isEqualToString:"
- "isHidden"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lastObject"
- "layer"
- "layerWillDraw:"
- "layoutSublayersOfLayer:"
- "mainConfiguration"
- "mainDisplay"
- "mainScreenClass"
- "mainScreenScale"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLong:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pixelSize"
- "position"
- "productType"
- "r*16@0:8"
- "release"
- "remoteContextWithOptions:"
- "removeListener:"
- "removeObject:"
- "renderInContext:"
- "resourcePath"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setAffineTransform:"
- "setAlignmentMode:"
- "setAllowsDisplayCompositing:"
- "setBackgroundColor:"
- "setBounds:"
- "setContents:"
- "setDelegate:"
- "setDisableUpdateMask:"
- "setFontSize:"
- "setForegroundColor:"
- "setFrame:"
- "setHidden:"
- "setLayer:"
- "setLevel:"
- "setNeedsDisplay"
- "setObject:forKey:"
- "setPosition:"
- "setProgressValue:"
- "setSecure:"
- "setStatusText:"
- "setString:"
- "setUsesPreBoardAppearance"
- "setVisible:"
- "setWrapped:"
- "sharedInstance"
- "string"
- "stringByAppendingString:"
- "superclass"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8f16"
- "v24@0:8@\"CALayer\"16"
- "v24@0:8@16"
- "v24@0:8^{CGContext=}16"
- "v32@0:8@\"CALayer\"16^{CGContext=}24"
- "v32@0:8@\"FBSDisplayMonitor\"16@\"FBSDisplayIdentity\"24"
- "v32@0:8@16@24"
- "v32@0:8@16^{CGContext=}24"
- "v32@0:8{CGSize=dd}16"
- "v40@0:8@\"FBSDisplayMonitor\"16@\"FBSDisplayIdentity\"24@\"FBSDisplayConfiguration\"32"
- "v40@0:8@16@24@32"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=\"width\"d\"height\"d}"

```
