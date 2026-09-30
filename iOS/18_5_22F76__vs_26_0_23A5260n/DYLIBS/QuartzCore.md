## QuartzCore

> `/System/Library/Frameworks/QuartzCore.framework/QuartzCore`

```diff

-1156.18.0.0.0
-  __TEXT.__text: 0x32aba4
-  __TEXT.__auth_stubs: 0x52f0
-  __TEXT.__objc_methlist: 0xa0a4
-  __TEXT.__const: 0x15d70
+1189.9.5.0.0
+  __TEXT.__text: 0x353d30
+  __TEXT.__auth_stubs: 0x54c0
+  __TEXT.__objc_methlist: 0xb124
+  __TEXT.__const: 0x175c0
   __TEXT.__dlopen_cstrs: 0xe0
-  __TEXT.__cstring: 0x2b91b
-  __TEXT.__gcc_except_tab: 0x6e84
-  __TEXT.__oslogstring: 0xef75
-  __TEXT.__unwind_info: 0x7b80
-  __TEXT.__objc_classname: 0xcc8
-  __TEXT.__objc_methname: 0xf19b
-  __TEXT.__objc_methtype: 0x35d3
-  __TEXT.__objc_stubs: 0xc520
-  __DATA_CONST.__got: 0xc78
-  __DATA_CONST.__const: 0xeaf8
-  __DATA_CONST.__objc_classlist: 0x3d0
+  __TEXT.__cstring: 0x23a03
+  __TEXT.__gcc_except_tab: 0x7174
+  __TEXT.__oslogstring: 0xff4f
+  __TEXT.__unwind_info: 0x7f98
+  __TEXT.__eh_frame: 0xc0
+  __TEXT.__objc_classname: 0xdd3
+  __TEXT.__objc_methname: 0x10d7e
+  __TEXT.__objc_methtype: 0x3a5e
+  __TEXT.__objc_stubs: 0xd380
+  __DATA_CONST.__got: 0xd50
+  __DATA_CONST.__const: 0xee90
+  __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5060
+  __DATA_CONST.__objc_selrefs: 0x5800
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x438
-  __DATA_CONST.__objc_arraydata: 0x38a0
-  __AUTH_CONST.__auth_got: 0x2990
-  __AUTH_CONST.__const: 0x14610
-  __AUTH_CONST.__cfstring: 0x154c0
-  __AUTH_CONST.__objc_const: 0xc668
-  __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_intobj: 0x43e0
+  __DATA_CONST.__objc_superrefs: 0x4c0
+  __DATA_CONST.__objc_arraydata: 0x3680
+  __AUTH_CONST.__auth_got: 0x2a78
+  __AUTH_CONST.__const: 0x156e8
+  __AUTH_CONST.__cfstring: 0x162e0
+  __AUTH_CONST.__objc_const: 0xe0a8
+  __AUTH_CONST.__objc_doubleobj: 0x150
+  __AUTH_CONST.__objc_intobj: 0x4050
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__objc_dictobj: 0x2f8
+  __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1130
-  __AUTH.__data: 0x40
-  __DATA.__objc_ivar: 0x570
-  __DATA.__data: 0x1390
-  __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x4088
-  __DATA.__common: 0xc
-  __DATA_DIRTY.__objc_data: 0x14f0
+  __AUTH.__objc_data: 0x1270
+  __AUTH.__data: 0x60
+  __DATA.__objc_ivar: 0x6a4
+  __DATA.__data: 0x13e8
+  __DATA.__bss: 0x3dd4
+  __DATA.__common: 0x10
+  __DATA_DIRTY.__objc_data: 0x1810
   __DATA_DIRTY.__data: 0x580
-  __DATA_DIRTY.__bss: 0x57b0
+  __DATA_DIRTY.__bss: 0x6128
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 109010DA-3C35-3E22-B001-939786412EE2
-  Functions: 10816
-  Symbols:   29480
-  CStrings:  14466
+  UUID: F011A179-6E57-36EC-B17B-FCB295BF5B3A
+  Functions: 11461
+  Symbols:   31431
+  CStrings:  14372
 
Symbols:
+ +[CADisplayLink(CADisplayLinkPrivate) earlyWakeupOffset]
+ +[CADisplayLink(CADisplayLinkPrivate) setEarlyWakeupOffset:]
+ +[CAFenceHandle handleFromXPCRepresentation:error:]
+ +[CAFenceHandle handleWithPort:data:error:]
+ +[CAFenceResolution _newResolutionWithTime:]
+ +[CAHostingToken _newTokenWithPort:sid:cid:]
+ +[CAHostingToken supportsSecureCoding]
+ +[CAHostingToken tokenFromXPCRepresentation:error:]
+ +[CAHostingToken tokenWithPort:data:error:]
+ +[CALayerHost defaultValueForKey:]
+ +[CAPortalLayer defaultValueForKey:]
+ +[CASDFEffect CAMLParserStartElement:]
+ +[CASDFEffect allEffectsClasses]
+ +[CASDFEffect defaultValueForKey:]
+ +[CASDFEffect defaultValues]
+ +[CASDFEffect supportsSecureCoding]
+ +[CASDFElementLayer CA_automaticallyNotifiesObservers:]
+ +[CASDFElementLayer _hasRenderLayerSubclass]
+ +[CASDFElementLayer defaultValueForKey:]
+ +[CASDFFillEffect defaultValues]
+ +[CASDFFillEffect name]
+ +[CASDFGeneratorRequest requestForEffect:]
+ +[CASDFGeneratorRequest requestForEffects:]
+ +[CASDFGeneratorRequest request]
+ +[CASDFGlassDisplacementEffect defaultValues]
+ +[CASDFGlassDisplacementEffect name]
+ +[CASDFGlassHighlightEffect defaultValues]
+ +[CASDFGlassHighlightEffect name]
+ +[CASDFGradientEffect defaultValues]
+ +[CASDFGradientEffect name]
+ +[CASDFKeyFillHighlightEffect defaultValues]
+ +[CASDFKeyFillHighlightEffect name]
+ +[CASDFLayer CA_automaticallyNotifiesObservers:]
+ +[CASDFLayer _hasRenderLayerSubclass]
+ +[CASDFLayer defaultValueForKey:]
+ +[CASDFOutputEffect defaultValues]
+ +[CASDFOutputEffect name]
+ +[CASDFShadowEffect defaultValues]
+ +[CASDFShadowEffect name]
+ +[CASDFVisualizationEffect defaultValues]
+ +[CASDFVisualizationEffect name]
+ +[CAWindowLayer CA_automaticallyNotifiesObservers:]
+ +[CAWindowLayer _hasRenderLayerSubclass]
+ +[CAWindowLayer defaultValueForKey:]
+ -[CABackdropLayer allowsFilteredLuma]
+ -[CABackdropLayer lumaSubrect]
+ -[CABackdropLayer lumaUpdateRate]
+ -[CABackdropLayer setAllowsFilteredLuma:]
+ -[CABackdropLayer setLumaSubrect:]
+ -[CABackdropLayer setLumaUpdateRate:]
+ -[CABrightnessRamper contrastPreservationBegin]
+ -[CABrightnessRamper contrastPreservationEnd]
+ -[CABrightnessRamper setContrastPreservationBegin:]
+ -[CABrightnessRamper setContrastPreservationEnd:]
+ -[CAContentStreamFrame setUpdateBeginTime:]
+ -[CAContentStreamFrame updateBeginTime]
+ -[CAContentStreamOptions setTrackedLayerIDContent:]
+ -[CAContentStreamOptions trackedLayerIDContent]
+ -[CAContext addFence:completion:]
+ -[CAContext hostingToken]
+ -[CAContext setZombifyOnInvalidate:]
+ -[CAContext zombifyOnInvalidate]
+ -[CADisplay supportedHDRModesWithCriteria:]
+ -[CADisplay(CADebugAdditions) _availableModesInternal]
+ -[CADisplayLink(CADisplayLinkPrivate) localEarlyWakeupOffset]
+ -[CADisplayLink(CADisplayLinkPrivate) setLocalEarlyWakeupOffset:]
+ -[CADisplayMode copyPrivateRepresentation]
+ -[CADisplayModeCriteria disableFrameDoubling]
+ -[CADisplayModeCriteria setDisableFrameDoubling:]
+ -[CADisplayStateControl acquireWirelessDisplayStateControl]
+ -[CADisplayStateControl cloningState]
+ -[CADisplayStateControl transitionToCloningState:withCompletion:]
+ -[CADisplayStateControl(CADebugAdditions) _copyStateInfo]
+ -[CADisplayStateControl(CADebugAdditions) targetCloningState]
+ -[CADisplayStateControl(Internal) displayCloningStateDidChange:seed:result:]
+ -[CADisplayStateControl(Internal) displayStateDidChange:seed:result:]
+ -[CAFenceHandle _createXPCObjForCoding:]
+ -[CAFenceHandle _initWithXPCObj:coding:]
+ -[CAFenceHandle encodeWithBlock:]
+ -[CAFenceResolution description]
+ -[CAFenceResolution init]
+ -[CAFenceResolution time]
+ -[CAFlipBook .cxx_construct]
+ -[CAFlipBook maximumPoolMemory]
+ -[CAFlipBook overAllocationFactor]
+ -[CAFlipBook purgePool]
+ -[CAFlipBook renderForTime:options:userInfo:onRenderBegin:onRenderComplete:]
+ -[CAFlipBook setMaximumPoolMemory:]
+ -[CAFlipBook setOverAllocationFactor:]
+ -[CAFlipBook(Private) _notifyRenderBegin]
+ -[CAFlipBook(Private) _notifyRenderCompletedForTime:status:frameId:oldestFrameId:apl:aplDimming:memoryUsage:rawSurfacePort:rawSurfaceDestRect:]
+ -[CAHostingToken _initWithPort:data:]
+ -[CAHostingToken _initWithPort:data:lenient:error:]
+ -[CAHostingToken _initWithXPCRepresentation:lenient:error:]
+ -[CAHostingToken createXPCRepresentation]
+ -[CAHostingToken dealloc]
+ -[CAHostingToken description]
+ -[CAHostingToken encodeWithBlock:]
+ -[CAHostingToken encodeWithCoder:]
+ -[CAHostingToken hash]
+ -[CAHostingToken initWithCoder:]
+ -[CAHostingToken init]
+ -[CAHostingToken isAuthoritative]
+ -[CAHostingToken isEqual:]
+ -[CAHostingToken pid]
+ -[CALayer _flags]
+ -[CALayer _performPreLayoutUpdate]
+ -[CALayer _thread_flags]
+ -[CALayer allowedContentsHideSublayers]
+ -[CALayer autoresizingMask]
+ -[CALayer contentsCDRStrength]
+ -[CALayer contentsHeadroom]
+ -[CALayer layoutManager]
+ -[CALayer preferredDynamicRange]
+ -[CALayer rasterizeInParentSpace]
+ -[CALayer remapAnimation:forKey:]
+ -[CALayer setAllowedContentsHideSublayers:]
+ -[CALayer setAutoresizingMask:]
+ -[CALayer setContentsCDRStrength:]
+ -[CALayer setContentsHeadroom:]
+ -[CALayer setLayoutManager:]
+ -[CALayer setPreferredDynamicRange:]
+ -[CALayer setRasterizeInParentSpace:]
+ -[CALayer setWantsDynamicContentScaling:]
+ -[CALayer wantsDynamicContentScaling]
+ -[CALayer(CALayerPrivate) allowsColorMatching]
+ -[CALayer(CALayerPrivate) allowsCornerContentsEdgeEffects]
+ -[CALayer(CALayerPrivate) needsPreLayoutUpdate]
+ -[CALayer(CALayerPrivate) setAllowsColorMatching:]
+ -[CALayer(CALayerPrivate) setAllowsCornerContentsEdgeEffects:]
+ -[CALayer(CALayerPrivate) setNeedsPreLayoutUpdate]
+ -[CALayer(CALayerPrivate) setShadowEffectsOnWindowMaskOnly:]
+ -[CALayer(CALayerPrivate) setSkipHitTesting:]
+ -[CALayer(CALayerPrivate) shadowEffectsOnWindowMaskOnly]
+ -[CALayer(CALayerPrivate) skipHitTesting]
+ -[CALayerHost hostingToken]
+ -[CALayerHost setHostingToken:]
+ -[CALayerHost setNeedsAuthoritativeHostingToken]
+ -[CALayerHost setZombificationMode:]
+ -[CALayerHost shouldArchiveValueForKey:]
+ -[CALayerHost zombificationMode]
+ -[CAMetalDrawable signalOnCommandQueue:]
+ -[CAMetalDrawable waitOnCommandQueue:]
+ -[CAMetalLayer residencySet]
+ -[CAMetalLayer(CAMetalLayerPrivate) premultiplied]
+ -[CAMetalLayer(CAMetalLayerPrivate) setPremultiplied:]
+ -[CAPortalLayer excludeSeparated]
+ -[CAPortalLayer setExcludeSeparated:]
+ -[CAPortalLayer setSourceLayerOpacityScale:]
+ -[CAPortalLayer sourceLayerOpacityScale]
+ -[CASDFEffect CAMLParser:setValue:forKey:]
+ -[CASDFEffect CAMLTypeForKey:]
+ -[CASDFEffect configureLayer:transaction:]
+ -[CASDFEffect copyWithZone:]
+ -[CASDFEffect encodeWithCAMLWriter:]
+ -[CASDFEffect encodeWithCoder:]
+ -[CASDFEffect initWithCoder:]
+ -[CASDFEffect init]
+ -[CASDFEffect name]
+ -[CASDFEffect setValue:forKey:]
+ -[CASDFEffect setValue:forKeyPath:]
+ -[CASDFEffect shouldArchiveValueForKey:]
+ -[CASDFEffect valueForKey:]
+ -[CASDFEffect valueForKeyPath:]
+ -[CASDFElementLayer _copyRenderLayer:layerFlags:commitFlags:]
+ -[CASDFElementLayer _renderImageCopyFlags]
+ -[CASDFElementLayer _renderLayerDefinesProperty:]
+ -[CASDFElementLayer contentsOneValueDistance]
+ -[CASDFElementLayer contentsZeroValueDistance]
+ -[CASDFElementLayer didChangeValueForKey:]
+ -[CASDFElementLayer gradientOvalization]
+ -[CASDFElementLayer hitTestsAsFill]
+ -[CASDFElementLayer mode]
+ -[CASDFElementLayer operation]
+ -[CASDFElementLayer setContentsOneValueDistance:]
+ -[CASDFElementLayer setContentsZeroValueDistance:]
+ -[CASDFElementLayer setGradientOvalization:]
+ -[CASDFElementLayer setHitTestsAsFill:]
+ -[CASDFElementLayer setMode:]
+ -[CASDFElementLayer setOperation:]
+ -[CASDFFillEffect color]
+ -[CASDFFillEffect configureLayer:transaction:]
+ -[CASDFFillEffect copyWithZone:]
+ -[CASDFFillEffect dealloc]
+ -[CASDFFillEffect setColor:]
+ -[CASDFGenerator dealloc]
+ -[CASDFGenerator generateSDFWithRequest:forImage:]
+ -[CASDFGenerator init]
+ -[CASDFGeneratorRequest _resetConfiguration]
+ -[CASDFGeneratorRequest _unionConfigurationForEffect:]
+ -[CASDFGeneratorRequest gradientSmoothing]
+ -[CASDFGeneratorRequest includeGradient]
+ -[CASDFGeneratorRequest init]
+ -[CASDFGeneratorRequest maximumDistance]
+ -[CASDFGeneratorRequest oneValueDistance]
+ -[CASDFGeneratorRequest outputBitDepth]
+ -[CASDFGeneratorRequest padding]
+ -[CASDFGeneratorRequest setGradientSmoothing:]
+ -[CASDFGeneratorRequest setIncludeGradient:]
+ -[CASDFGeneratorRequest setMaximumDistance:]
+ -[CASDFGeneratorRequest setOneValueDistance:]
+ -[CASDFGeneratorRequest setOutputBitDepth:]
+ -[CASDFGeneratorRequest setPadding:]
+ -[CASDFGeneratorRequest setZeroValueDistance:]
+ -[CASDFGeneratorRequest zeroValueDistance]
+ -[CASDFGlassDisplacementEffect angle]
+ -[CASDFGlassDisplacementEffect configureLayer:transaction:]
+ -[CASDFGlassDisplacementEffect copyWithZone:]
+ -[CASDFGlassDisplacementEffect curvature]
+ -[CASDFGlassDisplacementEffect height]
+ -[CASDFGlassDisplacementEffect maskOffset]
+ -[CASDFGlassDisplacementEffect setAngle:]
+ -[CASDFGlassDisplacementEffect setCurvature:]
+ -[CASDFGlassDisplacementEffect setHeight:]
+ -[CASDFGlassDisplacementEffect setMaskOffset:]
+ -[CASDFGlassHighlightEffect amount]
+ -[CASDFGlassHighlightEffect angle]
+ -[CASDFGlassHighlightEffect color]
+ -[CASDFGlassHighlightEffect configureLayer:transaction:]
+ -[CASDFGlassHighlightEffect copyWithZone:]
+ -[CASDFGlassHighlightEffect curvature]
+ -[CASDFGlassHighlightEffect dealloc]
+ -[CASDFGlassHighlightEffect global]
+ -[CASDFGlassHighlightEffect height]
+ -[CASDFGlassHighlightEffect setAmount:]
+ -[CASDFGlassHighlightEffect setAngle:]
+ -[CASDFGlassHighlightEffect setColor:]
+ -[CASDFGlassHighlightEffect setCurvature:]
+ -[CASDFGlassHighlightEffect setGlobal:]
+ -[CASDFGlassHighlightEffect setHeight:]
+ -[CASDFGlassHighlightEffect setSpread:]
+ -[CASDFGlassHighlightEffect spread]
+ -[CASDFGradientEffect colors]
+ -[CASDFGradientEffect configureLayer:transaction:]
+ -[CASDFGradientEffect copyWithZone:]
+ -[CASDFGradientEffect dealloc]
+ -[CASDFGradientEffect distances]
+ -[CASDFGradientEffect interpolations]
+ -[CASDFGradientEffect premultiplied]
+ -[CASDFGradientEffect setColors:]
+ -[CASDFGradientEffect setDistances:]
+ -[CASDFGradientEffect setInterpolations:]
+ -[CASDFGradientEffect setPremultiplied:]
+ -[CASDFKeyFillHighlightEffect configureLayer:transaction:]
+ -[CASDFKeyFillHighlightEffect copyWithZone:]
+ -[CASDFKeyFillHighlightEffect curvature]
+ -[CASDFKeyFillHighlightEffect dealloc]
+ -[CASDFKeyFillHighlightEffect fillAmount]
+ -[CASDFKeyFillHighlightEffect fillAngle]
+ -[CASDFKeyFillHighlightEffect fillColor]
+ -[CASDFKeyFillHighlightEffect fillHeightOffset]
+ -[CASDFKeyFillHighlightEffect fillHeightScale]
+ -[CASDFKeyFillHighlightEffect fillHeight]
+ -[CASDFKeyFillHighlightEffect fillSpreadOffset]
+ -[CASDFKeyFillHighlightEffect fillSpreadScale]
+ -[CASDFKeyFillHighlightEffect fillSpread]
+ -[CASDFKeyFillHighlightEffect global]
+ -[CASDFKeyFillHighlightEffect keyAmount]
+ -[CASDFKeyFillHighlightEffect keyAngle]
+ -[CASDFKeyFillHighlightEffect keyColor]
+ -[CASDFKeyFillHighlightEffect keyHeightOffset]
+ -[CASDFKeyFillHighlightEffect keyHeightScale]
+ -[CASDFKeyFillHighlightEffect keyHeight]
+ -[CASDFKeyFillHighlightEffect keySpreadOffset]
+ -[CASDFKeyFillHighlightEffect keySpreadScale]
+ -[CASDFKeyFillHighlightEffect keySpread]
+ -[CASDFKeyFillHighlightEffect setCurvature:]
+ -[CASDFKeyFillHighlightEffect setFillAmount:]
+ -[CASDFKeyFillHighlightEffect setFillAngle:]
+ -[CASDFKeyFillHighlightEffect setFillColor:]
+ -[CASDFKeyFillHighlightEffect setFillHeight:]
+ -[CASDFKeyFillHighlightEffect setFillHeightOffset:]
+ -[CASDFKeyFillHighlightEffect setFillHeightScale:]
+ -[CASDFKeyFillHighlightEffect setFillSpread:]
+ -[CASDFKeyFillHighlightEffect setFillSpreadOffset:]
+ -[CASDFKeyFillHighlightEffect setFillSpreadScale:]
+ -[CASDFKeyFillHighlightEffect setGlobal:]
+ -[CASDFKeyFillHighlightEffect setKeyAmount:]
+ -[CASDFKeyFillHighlightEffect setKeyAngle:]
+ -[CASDFKeyFillHighlightEffect setKeyColor:]
+ -[CASDFKeyFillHighlightEffect setKeyHeight:]
+ -[CASDFKeyFillHighlightEffect setKeyHeightOffset:]
+ -[CASDFKeyFillHighlightEffect setKeyHeightScale:]
+ -[CASDFKeyFillHighlightEffect setKeySpread:]
+ -[CASDFKeyFillHighlightEffect setKeySpreadOffset:]
+ -[CASDFKeyFillHighlightEffect setKeySpreadScale:]
+ -[CASDFLayer _copyRenderLayer:layerFlags:commitFlags:]
+ -[CASDFLayer _renderLayerDefinesProperty:]
+ -[CASDFLayer didChangeValueForKey:]
+ -[CASDFLayer effectOffset]
+ -[CASDFLayer effect]
+ -[CASDFLayer initWithLayer:]
+ -[CASDFLayer mergeElements]
+ -[CASDFLayer reloadValueForKeyPath:]
+ -[CASDFLayer setEffect:]
+ -[CASDFLayer setEffectOffset:]
+ -[CASDFLayer setMergeElements:]
+ -[CASDFLayer setSmoothness:]
+ -[CASDFLayer smoothness]
+ -[CASDFOutputEffect configureLayer:transaction:]
+ -[CASDFOutputEffect copyWithZone:]
+ -[CASDFOutputEffect maximum]
+ -[CASDFOutputEffect minimum]
+ -[CASDFOutputEffect setMaximum:]
+ -[CASDFOutputEffect setMinimum:]
+ -[CASDFShadowEffect color]
+ -[CASDFShadowEffect configureLayer:transaction:]
+ -[CASDFShadowEffect copyWithZone:]
+ -[CASDFShadowEffect dealloc]
+ -[CASDFShadowEffect invert]
+ -[CASDFShadowEffect offset]
+ -[CASDFShadowEffect punchout]
+ -[CASDFShadowEffect radius]
+ -[CASDFShadowEffect setColor:]
+ -[CASDFShadowEffect setInvert:]
+ -[CASDFShadowEffect setOffset:]
+ -[CASDFShadowEffect setPunchout:]
+ -[CASDFShadowEffect setRadius:]
+ -[CASDFVisualizationEffect configureLayer:transaction:]
+ -[CASecureFlipBookLayer userInfo]
+ -[CAWindowLayer _copyRenderLayer:layerFlags:commitFlags:]
+ -[CAWindowLayer _renderLayerDefinesProperty:]
+ -[CAWindowLayer didChangeValueForKey:]
+ -[CAWindowLayer flattenMode]
+ -[CAWindowLayer fullyOccluded]
+ -[CAWindowLayer ignoreAnimations]
+ -[CAWindowLayer postCommitDuration]
+ -[CAWindowLayer setFlattenMode:]
+ -[CAWindowLayer setFullyOccluded:]
+ -[CAWindowLayer setIgnoreAnimations:]
+ -[CAWindowLayer setPostCommitDuration:]
+ -[CAWindowServerDisplay globalLightAngle]
+ -[CAWindowServerDisplay needsGlobalLightCallback]
+ -[CAWindowServerDisplay setAccessibilityBounds:]
+ -[CAWindowServerDisplay setContrastPreservation:]
+ -[CAWindowServerDisplay setGlobalLightAngle:]
+ -[CAWindowServerDisplay setGlobalLightParameters:]
+ -[CAWindowServerDisplay setNeedsGlobalLightCallback:]
+ -[NSDictionary(CARenderValue) CA_copyRenderKeyPathValueArray]
+ GCC_except_table10
+ GCC_except_table10128
+ GCC_except_table10160
+ GCC_except_table10165
+ GCC_except_table10302
+ GCC_except_table10304
+ GCC_except_table10307
+ GCC_except_table10679
+ GCC_except_table10734
+ GCC_except_table10936
+ GCC_except_table10961
+ GCC_except_table10964
+ GCC_except_table10987
+ GCC_except_table10999
+ GCC_except_table11000
+ GCC_except_table11035
+ GCC_except_table11065
+ GCC_except_table11071
+ GCC_except_table11077
+ GCC_except_table11084
+ GCC_except_table11139
+ GCC_except_table11190
+ GCC_except_table11191
+ GCC_except_table11227
+ GCC_except_table11232
+ GCC_except_table11245
+ GCC_except_table11399
+ GCC_except_table11405
+ GCC_except_table11409
+ GCC_except_table11418
+ GCC_except_table11462
+ GCC_except_table11463
+ GCC_except_table11588
+ GCC_except_table11592
+ GCC_except_table1161
+ GCC_except_table1202
+ GCC_except_table1207
+ GCC_except_table1216
+ GCC_except_table1235
+ GCC_except_table1242
+ GCC_except_table1243
+ GCC_except_table1249
+ GCC_except_table1251
+ GCC_except_table1252
+ GCC_except_table1382
+ GCC_except_table1388
+ GCC_except_table1411
+ GCC_except_table1495
+ GCC_except_table1547
+ GCC_except_table1556
+ GCC_except_table1562
+ GCC_except_table1564
+ GCC_except_table1577
+ GCC_except_table1580
+ GCC_except_table1831
+ GCC_except_table2016
+ GCC_except_table2054
+ GCC_except_table2055
+ GCC_except_table2110
+ GCC_except_table2215
+ GCC_except_table2220
+ GCC_except_table2221
+ GCC_except_table2224
+ GCC_except_table2226
+ GCC_except_table2230
+ GCC_except_table2267
+ GCC_except_table2268
+ GCC_except_table2271
+ GCC_except_table2272
+ GCC_except_table2273
+ GCC_except_table2276
+ GCC_except_table2277
+ GCC_except_table2278
+ GCC_except_table2281
+ GCC_except_table2294
+ GCC_except_table2305
+ GCC_except_table2325
+ GCC_except_table2326
+ GCC_except_table2331
+ GCC_except_table2344
+ GCC_except_table2345
+ GCC_except_table2346
+ GCC_except_table2348
+ GCC_except_table2358
+ GCC_except_table2364
+ GCC_except_table2383
+ GCC_except_table2384
+ GCC_except_table2389
+ GCC_except_table2401
+ GCC_except_table2402
+ GCC_except_table2405
+ GCC_except_table2416
+ GCC_except_table2435
+ GCC_except_table2436
+ GCC_except_table2441
+ GCC_except_table245
+ GCC_except_table2453
+ GCC_except_table2456
+ GCC_except_table2511
+ GCC_except_table2563
+ GCC_except_table2572
+ GCC_except_table2575
+ GCC_except_table2586
+ GCC_except_table2589
+ GCC_except_table2609
+ GCC_except_table2612
+ GCC_except_table2626
+ GCC_except_table2629
+ GCC_except_table2631
+ GCC_except_table2633
+ GCC_except_table2657
+ GCC_except_table280
+ GCC_except_table283
+ GCC_except_table286
+ GCC_except_table292
+ GCC_except_table295
+ GCC_except_table298
+ GCC_except_table301
+ GCC_except_table3065
+ GCC_except_table3070
+ GCC_except_table3124
+ GCC_except_table3129
+ GCC_except_table3134
+ GCC_except_table3145
+ GCC_except_table3400
+ GCC_except_table3561
+ GCC_except_table363
+ GCC_except_table3637
+ GCC_except_table3638
+ GCC_except_table3640
+ GCC_except_table3716
+ GCC_except_table3729
+ GCC_except_table3731
+ GCC_except_table3733
+ GCC_except_table3737
+ GCC_except_table3745
+ GCC_except_table3749
+ GCC_except_table3754
+ GCC_except_table3879
+ GCC_except_table4284
+ GCC_except_table4286
+ GCC_except_table4290
+ GCC_except_table4291
+ GCC_except_table4292
+ GCC_except_table4296
+ GCC_except_table4298
+ GCC_except_table4306
+ GCC_except_table4317
+ GCC_except_table4320
+ GCC_except_table4323
+ GCC_except_table4324
+ GCC_except_table4330
+ GCC_except_table4336
+ GCC_except_table4338
+ GCC_except_table4339
+ GCC_except_table4341
+ GCC_except_table4342
+ GCC_except_table4343
+ GCC_except_table4348
+ GCC_except_table4352
+ GCC_except_table4353
+ GCC_except_table450
+ GCC_except_table4509
+ GCC_except_table4512
+ GCC_except_table4529
+ GCC_except_table4532
+ GCC_except_table4539
+ GCC_except_table4540
+ GCC_except_table455
+ GCC_except_table457
+ GCC_except_table461
+ GCC_except_table463
+ GCC_except_table469
+ GCC_except_table473
+ GCC_except_table474
+ GCC_except_table481
+ GCC_except_table4922
+ GCC_except_table4924
+ GCC_except_table4928
+ GCC_except_table494
+ GCC_except_table4946
+ GCC_except_table4949
+ GCC_except_table496
+ GCC_except_table4962
+ GCC_except_table4963
+ GCC_except_table497
+ GCC_except_table4970
+ GCC_except_table4989
+ GCC_except_table4991
+ GCC_except_table4998
+ GCC_except_table4999
+ GCC_except_table5003
+ GCC_except_table5012
+ GCC_except_table5014
+ GCC_except_table5019
+ GCC_except_table502
+ GCC_except_table503
+ GCC_except_table5034
+ GCC_except_table5035
+ GCC_except_table5036
+ GCC_except_table504
+ GCC_except_table5041
+ GCC_except_table5043
+ GCC_except_table5045
+ GCC_except_table5047
+ GCC_except_table5048
+ GCC_except_table5108
+ GCC_except_table5162
+ GCC_except_table5163
+ GCC_except_table5166
+ GCC_except_table5167
+ GCC_except_table5169
+ GCC_except_table5176
+ GCC_except_table549
+ GCC_except_table5492
+ GCC_except_table5495
+ GCC_except_table550
+ GCC_except_table5502
+ GCC_except_table5503
+ GCC_except_table5505
+ GCC_except_table5507
+ GCC_except_table551
+ GCC_except_table5512
+ GCC_except_table5514
+ GCC_except_table5527
+ GCC_except_table5533
+ GCC_except_table5537
+ GCC_except_table555
+ GCC_except_table5554
+ GCC_except_table557
+ GCC_except_table5570
+ GCC_except_table5584
+ GCC_except_table5587
+ GCC_except_table5614
+ GCC_except_table5626
+ GCC_except_table5628
+ GCC_except_table5692
+ GCC_except_table5703
+ GCC_except_table5746
+ GCC_except_table5754
+ GCC_except_table5788
+ GCC_except_table5796
+ GCC_except_table5806
+ GCC_except_table5854
+ GCC_except_table5857
+ GCC_except_table5859
+ GCC_except_table5886
+ GCC_except_table5888
+ GCC_except_table589
+ GCC_except_table5892
+ GCC_except_table5893
+ GCC_except_table5897
+ GCC_except_table5898
+ GCC_except_table5919
+ GCC_except_table5926
+ GCC_except_table5927
+ GCC_except_table5934
+ GCC_except_table5999
+ GCC_except_table6000
+ GCC_except_table6007
+ GCC_except_table603
+ GCC_except_table604
+ GCC_except_table607
+ GCC_except_table6150
+ GCC_except_table6574
+ GCC_except_table6580
+ GCC_except_table6585
+ GCC_except_table6586
+ GCC_except_table6587
+ GCC_except_table6603
+ GCC_except_table6604
+ GCC_except_table6605
+ GCC_except_table6610
+ GCC_except_table6612
+ GCC_except_table6613
+ GCC_except_table6617
+ GCC_except_table6618
+ GCC_except_table662
+ GCC_except_table6639
+ GCC_except_table6646
+ GCC_except_table6647
+ GCC_except_table6649
+ GCC_except_table6651
+ GCC_except_table6656
+ GCC_except_table6660
+ GCC_except_table6661
+ GCC_except_table6662
+ GCC_except_table6664
+ GCC_except_table6674
+ GCC_except_table6676
+ GCC_except_table6678
+ GCC_except_table6698
+ GCC_except_table6699
+ GCC_except_table671
+ GCC_except_table676
+ GCC_except_table685
+ GCC_except_table6891
+ GCC_except_table696
+ GCC_except_table706
+ GCC_except_table708
+ GCC_except_table7113
+ GCC_except_table7114
+ GCC_except_table714
+ GCC_except_table720
+ GCC_except_table7209
+ GCC_except_table7211
+ GCC_except_table7213
+ GCC_except_table7216
+ GCC_except_table722
+ GCC_except_table7255
+ GCC_except_table7259
+ GCC_except_table7262
+ GCC_except_table7264
+ GCC_except_table7265
+ GCC_except_table7267
+ GCC_except_table7268
+ GCC_except_table7269
+ GCC_except_table7272
+ GCC_except_table7283
+ GCC_except_table7291
+ GCC_except_table7317
+ GCC_except_table732
+ GCC_except_table733
+ GCC_except_table740
+ GCC_except_table743
+ GCC_except_table7442
+ GCC_except_table7443
+ GCC_except_table7446
+ GCC_except_table7447
+ GCC_except_table7448
+ GCC_except_table7449
+ GCC_except_table7454
+ GCC_except_table7456
+ GCC_except_table7458
+ GCC_except_table7459
+ GCC_except_table7462
+ GCC_except_table7467
+ GCC_except_table7470
+ GCC_except_table7473
+ GCC_except_table7480
+ GCC_except_table7481
+ GCC_except_table7484
+ GCC_except_table7485
+ GCC_except_table749
+ GCC_except_table7494
+ GCC_except_table7496
+ GCC_except_table7498
+ GCC_except_table7499
+ GCC_except_table7502
+ GCC_except_table7508
+ GCC_except_table7509
+ GCC_except_table7510
+ GCC_except_table7512
+ GCC_except_table7515
+ GCC_except_table7516
+ GCC_except_table7517
+ GCC_except_table7519
+ GCC_except_table7520
+ GCC_except_table7521
+ GCC_except_table7522
+ GCC_except_table7524
+ GCC_except_table7525
+ GCC_except_table7526
+ GCC_except_table7528
+ GCC_except_table7530
+ GCC_except_table7539
+ GCC_except_table7556
+ GCC_except_table7558
+ GCC_except_table7562
+ GCC_except_table7565
+ GCC_except_table7568
+ GCC_except_table7572
+ GCC_except_table7584
+ GCC_except_table7592
+ GCC_except_table7594
+ GCC_except_table7597
+ GCC_except_table7599
+ GCC_except_table760
+ GCC_except_table7606
+ GCC_except_table7608
+ GCC_except_table7610
+ GCC_except_table7616
+ GCC_except_table7617
+ GCC_except_table7618
+ GCC_except_table7620
+ GCC_except_table765
+ GCC_except_table7715
+ GCC_except_table7717
+ GCC_except_table7724
+ GCC_except_table7726
+ GCC_except_table7727
+ GCC_except_table7728
+ GCC_except_table7730
+ GCC_except_table7736
+ GCC_except_table7744
+ GCC_except_table7748
+ GCC_except_table7750
+ GCC_except_table7751
+ GCC_except_table7760
+ GCC_except_table7762
+ GCC_except_table7853
+ GCC_except_table7854
+ GCC_except_table7857
+ GCC_except_table7862
+ GCC_except_table7865
+ GCC_except_table7866
+ GCC_except_table787
+ GCC_except_table788
+ GCC_except_table814
+ GCC_except_table8155
+ GCC_except_table8167
+ GCC_except_table8168
+ GCC_except_table8169
+ GCC_except_table8170
+ GCC_except_table8171
+ GCC_except_table8176
+ GCC_except_table820
+ GCC_except_table823
+ GCC_except_table826
+ GCC_except_table827
+ GCC_except_table828
+ GCC_except_table8305
+ GCC_except_table831
+ GCC_except_table8311
+ GCC_except_table8312
+ GCC_except_table832
+ GCC_except_table8333
+ GCC_except_table834
+ GCC_except_table835
+ GCC_except_table836
+ GCC_except_table838
+ GCC_except_table840
+ GCC_except_table8403
+ GCC_except_table8404
+ GCC_except_table8409
+ GCC_except_table8410
+ GCC_except_table8411
+ GCC_except_table8412
+ GCC_except_table8435
+ GCC_except_table8461
+ GCC_except_table8463
+ GCC_except_table8476
+ GCC_except_table8479
+ GCC_except_table8503
+ GCC_except_table8504
+ GCC_except_table8506
+ GCC_except_table8508
+ GCC_except_table8509
+ GCC_except_table8513
+ GCC_except_table8514
+ GCC_except_table8515
+ GCC_except_table8519
+ GCC_except_table8521
+ GCC_except_table8522
+ GCC_except_table8523
+ GCC_except_table8536
+ GCC_except_table8538
+ GCC_except_table8548
+ GCC_except_table8550
+ GCC_except_table8551
+ GCC_except_table8553
+ GCC_except_table8554
+ GCC_except_table8555
+ GCC_except_table8572
+ GCC_except_table8614
+ GCC_except_table8634
+ GCC_except_table8635
+ GCC_except_table8637
+ GCC_except_table8639
+ GCC_except_table8710
+ GCC_except_table8824
+ GCC_except_table8843
+ GCC_except_table8845
+ GCC_except_table8987
+ GCC_except_table9026
+ GCC_except_table9182
+ GCC_except_table9340
+ GCC_except_table9387
+ GCC_except_table9425
+ GCC_except_table9584
+ GCC_except_table9587
+ GCC_except_table9588
+ GCC_except_table9592
+ GCC_except_table9644
+ GCC_except_table9881
+ GCC_except_table9883
+ GCC_except_table9884
+ GCC_except_table9886
+ GCC_except_table9901
+ _CABackingStoreBeginUpdateWithFormat
+ _CACFAbsoluteTimeToContinuousTime
+ _CADynamicRangeAutomatic
+ _CADynamicRangeConstrainedHigh
+ _CADynamicRangeHigh
+ _CADynamicRangeStandard
+ _CAHostingTokenDataIsValid
+ _CAIOSurfaceReloadColorAttributes
+ _CAObject_valueForAtom
+ _CARenderOGLCopyStats
+ _CARenderUpdateSetGlobalLightAngle
+ _CARenderUpdateSetGlobalLightParameters
+ _CASFlipBookRender
+ _CASSetDisplayCloningState
+ _CAVerifyServerReturn
+ _CA_CFDictionaryGetFloat
+ _CA_CFInt64Value
+ _CGColorCreateWithContentHeadroom
+ _CGColorGetConstantColor
+ _CGColorGetContentHeadroom
+ _CGColorSpaceIsHDR
+ _CGContentToneMappingInfoCreateDictionary
+ _CGGStateGetContentToneMappingInfo
+ _CGImageGetContentAverageLightLevelNits
+ _CGImageSetHeadroom
+ _EDRGetDefaultMinScalingFactor
+ _IOMobileFramebufferAnnounceNextSwapTimestamp
+ _IOMobileFramebufferSetAmmoliteStrength
+ _IOMobileFramebufferSwapSetToneMapConfig
+ _IOSurfaceAppendTransaction
+ _IOSurfaceHasDataProperty
+ _IOSurfaceQueryTransactionList
+ _NSCocoaErrorDomain
+ _NSStringFromCADisplayCloningState
+ _OBJC_CLASS_$_CAFenceResolution
+ _OBJC_CLASS_$_CAHostingToken
+ _OBJC_CLASS_$_CASDFEffect
+ _OBJC_CLASS_$_CASDFElementLayer
+ _OBJC_CLASS_$_CASDFFillEffect
+ _OBJC_CLASS_$_CASDFGenerator
+ _OBJC_CLASS_$_CASDFGeneratorRequest
+ _OBJC_CLASS_$_CASDFGlassDisplacementEffect
+ _OBJC_CLASS_$_CASDFGlassHighlightEffect
+ _OBJC_CLASS_$_CASDFGradientEffect
+ _OBJC_CLASS_$_CASDFKeyFillHighlightEffect
+ _OBJC_CLASS_$_CASDFLayer
+ _OBJC_CLASS_$_CASDFOutputEffect
+ _OBJC_CLASS_$_CASDFShadowEffect
+ _OBJC_CLASS_$_CASDFVisualizationEffect
+ _OBJC_CLASS_$_CAWindowLayer
+ _OBJC_CLASS_$_IOSurfaceTransaction
+ _OBJC_CLASS_$_MTLComputePipelineDescriptor
+ _OBJC_CLASS_$_MTLResidencySetDescriptor
+ _OBJC_IVAR_$_CABrightnessRamper._contrastPreservationBegin
+ _OBJC_IVAR_$_CABrightnessRamper._contrastPreservationEnd
+ _OBJC_IVAR_$_CAContentStream._warmed_up
+ _OBJC_IVAR_$_CAContentStreamFrame._updateBeginTime
+ _OBJC_IVAR_$_CAContentStreamOptions._trackedLayerIDContent
+ _OBJC_IVAR_$_CADisplayPreferences._preferredHdrMode
+ _OBJC_IVAR_$_CADisplayStateControl._cloning_state_transition
+ _OBJC_IVAR_$_CADisplayStateControl._display_state_transition
+ _OBJC_IVAR_$_CAFenceHandle._invalidate_on_dealloc
+ _OBJC_IVAR_$_CAFenceResolution._time
+ _OBJC_IVAR_$_CAFlipBook._cancelTimestamp
+ _OBJC_IVAR_$_CAFlipBook._framesLock
+ _OBJC_IVAR_$_CAFlipBook._maximumPoolMemory
+ _OBJC_IVAR_$_CAFlipBook._onRenderBeginClientIpc
+ _OBJC_IVAR_$_CAFlipBook._onRenderBegunCB
+ _OBJC_IVAR_$_CAFlipBook._onRenderCBLock
+ _OBJC_IVAR_$_CAFlipBook._onRenderCompletedCB
+ _OBJC_IVAR_$_CAFlipBook._onRenderInfo
+ _OBJC_IVAR_$_CAFlipBook._overAllocationFactor
+ _OBJC_IVAR_$_CAFlipBook._renderInProgress
+ _OBJC_IVAR_$_CAFlipBook._renderTimestamp
+ _OBJC_IVAR_$_CAHostingToken._data
+ _OBJC_IVAR_$_CAHostingToken._port
+ _OBJC_IVAR_$_CAHostingToken._xPort
+ _OBJC_IVAR_$_CALayer._autoresizingMask
+ _OBJC_IVAR_$_CALayer._layoutManager
+ _OBJC_IVAR_$_CALayer._wantsDynamicContentScaling
+ _OBJC_IVAR_$_CALayerHost._tokenNeedsPort
+ _OBJC_IVAR_$_CAPortalLayer._excludeSeparated
+ _OBJC_IVAR_$_CASDFFillEffect._color
+ _OBJC_IVAR_$_CASDFGenerator._context
+ _OBJC_IVAR_$_CASDFGenerator._renderer
+ _OBJC_IVAR_$_CASDFGeneratorRequest._gradientSmoothing
+ _OBJC_IVAR_$_CASDFGeneratorRequest._includeGradient
+ _OBJC_IVAR_$_CASDFGeneratorRequest._maximumDistance
+ _OBJC_IVAR_$_CASDFGeneratorRequest._oneValueDistance
+ _OBJC_IVAR_$_CASDFGeneratorRequest._outputBitDepth
+ _OBJC_IVAR_$_CASDFGeneratorRequest._padding
+ _OBJC_IVAR_$_CASDFGeneratorRequest._zeroValueDistance
+ _OBJC_IVAR_$_CASDFGlassDisplacementEffect._angle
+ _OBJC_IVAR_$_CASDFGlassDisplacementEffect._curvature
+ _OBJC_IVAR_$_CASDFGlassDisplacementEffect._height
+ _OBJC_IVAR_$_CASDFGlassDisplacementEffect._maskOffset
+ _OBJC_IVAR_$_CASDFGlassHighlightEffect._amount
+ _OBJC_IVAR_$_CASDFGlassHighlightEffect._angle
+ _OBJC_IVAR_$_CASDFGlassHighlightEffect._color
+ _OBJC_IVAR_$_CASDFGlassHighlightEffect._curvature
+ _OBJC_IVAR_$_CASDFGlassHighlightEffect._global
+ _OBJC_IVAR_$_CASDFGlassHighlightEffect._height
+ _OBJC_IVAR_$_CASDFGlassHighlightEffect._spread
+ _OBJC_IVAR_$_CASDFGradientEffect._colors
+ _OBJC_IVAR_$_CASDFGradientEffect._distances
+ _OBJC_IVAR_$_CASDFGradientEffect._interpolations
+ _OBJC_IVAR_$_CASDFGradientEffect._premultiplied
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._curvature
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._fillAmount
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._fillAngle
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._fillColor
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._fillHeight
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._fillHeightOffset
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._fillHeightScale
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._fillSpread
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._fillSpreadOffset
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._fillSpreadScale
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._global
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._keyAmount
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._keyAngle
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._keyColor
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._keyHeight
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._keyHeightOffset
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._keyHeightScale
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._keySpread
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._keySpreadOffset
+ _OBJC_IVAR_$_CASDFKeyFillHighlightEffect._keySpreadScale
+ _OBJC_IVAR_$_CASDFOutputEffect._maximum
+ _OBJC_IVAR_$_CASDFOutputEffect._minimum
+ _OBJC_IVAR_$_CASDFShadowEffect._color
+ _OBJC_IVAR_$_CASDFShadowEffect._invert
+ _OBJC_IVAR_$_CASDFShadowEffect._offset
+ _OBJC_IVAR_$_CASDFShadowEffect._punchout
+ _OBJC_IVAR_$_CASDFShadowEffect._radius
+ _OBJC_METACLASS_$_CAFenceResolution
+ _OBJC_METACLASS_$_CAHostingToken
+ _OBJC_METACLASS_$_CASDFEffect
+ _OBJC_METACLASS_$_CASDFElementLayer
+ _OBJC_METACLASS_$_CASDFFillEffect
+ _OBJC_METACLASS_$_CASDFGenerator
+ _OBJC_METACLASS_$_CASDFGeneratorRequest
+ _OBJC_METACLASS_$_CASDFGlassDisplacementEffect
+ _OBJC_METACLASS_$_CASDFGlassHighlightEffect
+ _OBJC_METACLASS_$_CASDFGradientEffect
+ _OBJC_METACLASS_$_CASDFKeyFillHighlightEffect
+ _OBJC_METACLASS_$_CASDFLayer
+ _OBJC_METACLASS_$_CASDFOutputEffect
+ _OBJC_METACLASS_$_CASDFShadowEffect
+ _OBJC_METACLASS_$_CASDFVisualizationEffect
+ _OBJC_METACLASS_$_CAWindowLayer
+ _SANDBOX_CHECK_NO_REPORT
+ _SILManagerIndicatorGetFrameData
+ _SILManagerIndicatorUserInfo
+ __CACDisplayCloningStateDidChange
+ __CACDisplayStateDidChange
+ __CASSetDisplayCloningState
+ __CASSetDisplayState
+ __OBJC_$_CLASS_METHODS_CAHostingToken
+ __OBJC_$_CLASS_METHODS_CASDFEffect
+ __OBJC_$_CLASS_METHODS_CASDFElementLayer
+ __OBJC_$_CLASS_METHODS_CASDFFillEffect
+ __OBJC_$_CLASS_METHODS_CASDFGeneratorRequest
+ __OBJC_$_CLASS_METHODS_CASDFGlassDisplacementEffect
+ __OBJC_$_CLASS_METHODS_CASDFGlassHighlightEffect
+ __OBJC_$_CLASS_METHODS_CASDFGradientEffect
+ __OBJC_$_CLASS_METHODS_CASDFKeyFillHighlightEffect
+ __OBJC_$_CLASS_METHODS_CASDFLayer
+ __OBJC_$_CLASS_METHODS_CASDFOutputEffect
+ __OBJC_$_CLASS_METHODS_CASDFShadowEffect
+ __OBJC_$_CLASS_METHODS_CASDFVisualizationEffect
+ __OBJC_$_CLASS_METHODS_CAWindowLayer
+ __OBJC_$_CLASS_PROP_LIST_CAHostingToken
+ __OBJC_$_CLASS_PROP_LIST_CASDFEffect
+ __OBJC_$_INSTANCE_METHODS_CAFenceResolution
+ __OBJC_$_INSTANCE_METHODS_CAHostingToken
+ __OBJC_$_INSTANCE_METHODS_CASDFEffect
+ __OBJC_$_INSTANCE_METHODS_CASDFElementLayer
+ __OBJC_$_INSTANCE_METHODS_CASDFFillEffect
+ __OBJC_$_INSTANCE_METHODS_CASDFGenerator
+ __OBJC_$_INSTANCE_METHODS_CASDFGeneratorRequest
+ __OBJC_$_INSTANCE_METHODS_CASDFGlassDisplacementEffect
+ __OBJC_$_INSTANCE_METHODS_CASDFGlassHighlightEffect
+ __OBJC_$_INSTANCE_METHODS_CASDFGradientEffect
+ __OBJC_$_INSTANCE_METHODS_CASDFKeyFillHighlightEffect
+ __OBJC_$_INSTANCE_METHODS_CASDFLayer
+ __OBJC_$_INSTANCE_METHODS_CASDFOutputEffect
+ __OBJC_$_INSTANCE_METHODS_CASDFShadowEffect
+ __OBJC_$_INSTANCE_METHODS_CASDFVisualizationEffect
+ __OBJC_$_INSTANCE_METHODS_CAWindowLayer
+ __OBJC_$_INSTANCE_VARIABLES_CAFenceResolution
+ __OBJC_$_INSTANCE_VARIABLES_CAHostingToken
+ __OBJC_$_INSTANCE_VARIABLES_CAPortalLayer
+ __OBJC_$_INSTANCE_VARIABLES_CASDFFillEffect
+ __OBJC_$_INSTANCE_VARIABLES_CASDFGenerator
+ __OBJC_$_INSTANCE_VARIABLES_CASDFGeneratorRequest
+ __OBJC_$_INSTANCE_VARIABLES_CASDFGlassDisplacementEffect
+ __OBJC_$_INSTANCE_VARIABLES_CASDFGlassHighlightEffect
+ __OBJC_$_INSTANCE_VARIABLES_CASDFGradientEffect
+ __OBJC_$_INSTANCE_VARIABLES_CASDFKeyFillHighlightEffect
+ __OBJC_$_INSTANCE_VARIABLES_CASDFOutputEffect
+ __OBJC_$_INSTANCE_VARIABLES_CASDFShadowEffect
+ __OBJC_$_PROP_LIST_CAFenceResolution
+ __OBJC_$_PROP_LIST_CAHostingToken
+ __OBJC_$_PROP_LIST_CAMetalDrawable.260
+ __OBJC_$_PROP_LIST_CASDFElementLayer
+ __OBJC_$_PROP_LIST_CASDFFillEffect
+ __OBJC_$_PROP_LIST_CASDFGeneratorRequest
+ __OBJC_$_PROP_LIST_CASDFGlassDisplacementEffect
+ __OBJC_$_PROP_LIST_CASDFGlassHighlightEffect
+ __OBJC_$_PROP_LIST_CASDFGradientEffect
+ __OBJC_$_PROP_LIST_CASDFKeyFillHighlightEffect
+ __OBJC_$_PROP_LIST_CASDFLayer
+ __OBJC_$_PROP_LIST_CASDFOutputEffect
+ __OBJC_$_PROP_LIST_CASDFShadowEffect
+ __OBJC_$_PROP_LIST_CAWindowLayer
+ __OBJC_CLASS_PROTOCOLS_$_CAHostingToken
+ __OBJC_CLASS_PROTOCOLS_$_CASDFEffect
+ __OBJC_CLASS_RO_$_CAFenceResolution
+ __OBJC_CLASS_RO_$_CAHostingToken
+ __OBJC_CLASS_RO_$_CASDFEffect
+ __OBJC_CLASS_RO_$_CASDFElementLayer
+ __OBJC_CLASS_RO_$_CASDFFillEffect
+ __OBJC_CLASS_RO_$_CASDFGenerator
+ __OBJC_CLASS_RO_$_CASDFGeneratorRequest
+ __OBJC_CLASS_RO_$_CASDFGlassDisplacementEffect
+ __OBJC_CLASS_RO_$_CASDFGlassHighlightEffect
+ __OBJC_CLASS_RO_$_CASDFGradientEffect
+ __OBJC_CLASS_RO_$_CASDFKeyFillHighlightEffect
+ __OBJC_CLASS_RO_$_CASDFLayer
+ __OBJC_CLASS_RO_$_CASDFOutputEffect
+ __OBJC_CLASS_RO_$_CASDFShadowEffect
+ __OBJC_CLASS_RO_$_CASDFVisualizationEffect
+ __OBJC_CLASS_RO_$_CAWindowLayer
+ __OBJC_METACLASS_RO_$_CAFenceResolution
+ __OBJC_METACLASS_RO_$_CAHostingToken
+ __OBJC_METACLASS_RO_$_CASDFEffect
+ __OBJC_METACLASS_RO_$_CASDFElementLayer
+ __OBJC_METACLASS_RO_$_CASDFFillEffect
+ __OBJC_METACLASS_RO_$_CASDFGenerator
+ __OBJC_METACLASS_RO_$_CASDFGeneratorRequest
+ __OBJC_METACLASS_RO_$_CASDFGlassDisplacementEffect
+ __OBJC_METACLASS_RO_$_CASDFGlassHighlightEffect
+ __OBJC_METACLASS_RO_$_CASDFGradientEffect
+ __OBJC_METACLASS_RO_$_CASDFKeyFillHighlightEffect
+ __OBJC_METACLASS_RO_$_CASDFLayer
+ __OBJC_METACLASS_RO_$_CASDFOutputEffect
+ __OBJC_METACLASS_RO_$_CASDFShadowEffect
+ __OBJC_METACLASS_RO_$_CASDFVisualizationEffect
+ __OBJC_METACLASS_RO_$_CAWindowLayer
+ __XDisableAutomaticWirelessDisplayStateControl
+ __XDisplayCloningStateDidChange
+ __XDisplayStateDidChange
+ __XFlipBookRenderDidBegin
+ __XFlipBookRenderDidComplete
+ __XSetDisplayCloningState
+ __Z11get_cg_name16CAColorSpaceName
+ __Z17iomfb_relbuf_infoP21__IOMobileFramebufferPFvS0_jyyPvES1_j
+ __Z23CADisplayStateDidChangejhhh
+ __Z25cadisplay_state_to_string14CADisplayState
+ __Z30CADisplayCloningStateDidChangejhhh
+ __Z33cadisplay_cloning_state_to_string21CADisplayCloningState
+ __ZGVZ11get_cg_name16CAColorSpaceNameE20named_cg_colorspaces
+ __ZGVZN2CA7DisplayL20MaxEarlyWakeupOffsetEvE3ret
+ __ZGVZN2CA7DisplayL20MaxEarlyWakeupOffsetEvE7ret_apt
+ __ZL10write_attrjPKv12_CAValueTypePv.20988
+ __ZL11block_ctors.16894
+ __ZL11initialized.18291
+ __ZL12collect_slot.10676
+ __ZL14release_samplejyPv.10677
+ __ZL15_next_encode_idv
+ __ZL15copy_dictionaryjPKv12_CAValueTypePv.21009
+ __ZL15lowLatency_atom.10917
+ __ZL19iomfb_relbuf_info_f
+ __ZL20cg_color_from_valuesIN2CA6Render5ColorEEP7CGColorRKT_P12CGColorSpaceb
+ __ZL20extended_colorspaces
+ __ZL21will_suspend_callbackPN2CA6Render6ObjectEPvS3_.7329
+ __ZL23delete_drawable_privateP23_CAMetalDrawablePrivateP13_CAImageQueue
+ __ZL24layer_collectable_signalP13_CAImageQueuePv.10678
+ __ZL24layer_private_set_deviceP20_CAMetalLayerPrivatePU19objcproto9MTLDevice11objc_object
+ __ZL24unlinearized_colorspaces
+ __ZL25allocate_drawable_texturePU19objcproto9MTLDevice11objc_objectP11__IOSurfacejj14MTLPixelFormaty20CAMetalLayerRotationbP8NSStringmPU26objcproto15MTLResidencySet11objc_object
+ __ZL28presentsWithTransaction_atom.10754
+ __ZL30cg_color_from_pattern_or_colorRK25ReverseSerializationStatePKN2CA6Render7PatternERKNS3_5ColorE
+ __ZL38iomfb_swap_set_contrast_preservation_f
+ __ZL8set_attrPKvS0_Pv.21002
+ __ZL9copy_attrjPKv12_CAValueTypePv.21011
+ __ZN10Transition3endElh30CADisplayStateTransitionStatus
+ __ZN10Transition5beginEllU13block_pointerFvl30CADisplayStateTransitionStatusE
+ __ZN10TransitionD2Ev
+ __ZN12_GLOBAL__N_130_CARenderServerSnapshotDisplayEjPK10__CFStringPKvS4_jiiPK13CATransform3DjmPjj
+ __ZN1X17small_vector_baseIN2CA3OGL12MetalContext17ExecutionIntervalEE5eraseEPKS4_
+ __ZN1X17small_vector_baseIN2CA6Render6Update10EDRRequestEE4growEm
+ __ZN1X17small_vector_baseIN2CA6Render6Update10EDRRequestEE9push_backEOS4_
+ __ZN1X17small_vector_baseIPN2CA6Render13BackdropGroupEE9push_backERKS4_
+ __ZN1X17small_vector_baseIPN2CA6Render16FlattenedSurfaceEE4growEm
+ __ZN1X17small_vector_baseIZN2CA3OGL9LayerNode24merge_sdf_element_layersEPNS2_5LayerEE13SublayerFrameE7reserveEm
+ __ZN1X17small_vector_baseIjE5eraseEPKj
+ __ZN1X17small_vector_baseImE6resizeEm
+ __ZN1X3RefIN2CA5ShapeEEaSEPS2_
+ __ZN1X3RefIN2CA6Render5ShmemEEaSEPS3_
+ __ZN1X3RefIN2CA6Render7SurfaceEEaSEPS3_
+ __ZN1X6Stream6printfEPKcz
+ __ZN20CACGContextEvaluator17update_with_colorEP7CGColor20CGCompositeOperationP8CGGState
+ __ZN20CACGContextEvaluator17update_with_imageEP7CGImageP8CGGState
+ __ZN2CA10BoundsImpl5UnionERNS_11GenericRectIdEERKS2_
+ __ZN2CA10emit_errorEPP7NSErrorNS_11CAErrorCodeEP8NSString
+ __ZN2CA11ColorMatrix17set_ycc_compositeEfffPKf
+ __ZN2CA11ColorMatrix20set_color_monochromeEffPKf
+ __ZN2CA11SurfaceUtil25CASurfaceQuerySharedEventEP11__IOSurface
+ __ZN2CA11SurfaceUtil26CASurfaceAppendSharedEventEP11__IOSurfaceNS0_31CASurfaceSharedEventTransactionE
+ __ZN2CA11Transaction9add_fenceEjP13CAFenceHandleU13block_pointerFvP17CAFenceResolutionE
+ __ZN2CA12ColorProgram5Cache17pop_whippet_cacheEv
+ __ZN2CA12ColorProgram5Cache18push_whippet_cacheEP12CGColorSpaceff13CGToneMappingPK14__CFDictionary
+ __ZN2CA12ColorProgram7Program13color_programEPK21CGColorConversionInfoP12CGColorSpacei28CGColorConversionIterateTypebijfffffRb
+ __ZN2CA12WindowServer11IOMFBServer15current_surfaceEbybb
+ __ZN2CA12WindowServer11IOMFBServer15set_edr_enabledEbbfPNS_6Render6UpdateE
+ __ZN2CA12WindowServer11IOMFBServer16collect_gpu_dataEPNS_3OGL8RendererEjRyS5_
+ __ZN2CA12WindowServer11IOMFBServer20relbuf_info_callbackEP21__IOMobileFramebufferjyyPv
+ __ZN2CA12WindowServer11IOMFBServer20try_swap_begin_asyncEj
+ __ZN2CA12WindowServer11IOMFBServer21set_calibration_phaseEjjj
+ __ZN2CA12WindowServer11IOMFBServer27forward_frame_info_callbackEjPK14__CFDictionaryRKNS0_12IOMFBDisplay9FrameInfoEyy
+ __ZN2CA12WindowServer11IOMFBServer33complete_display_state_transitionENS0_12DisplayStateENS0_19DisplayCloningStateE
+ __ZN2CA12WindowServer12AppleDisplayC2EPK10__CFStringjj16IOMFBDisplayType
+ __ZN2CA12WindowServer12IOMFBDisplay14update_surfaceEbbybb
+ __ZN2CA12WindowServer12IOMFBDisplay15add_timing_infoEjb
+ __ZN2CA12WindowServer12IOMFBDisplay15current_surfaceEbybb
+ __ZN2CA12WindowServer12IOMFBDisplay17swap_wait_timeoutEjjbPd
+ __ZN2CA12WindowServer12IOMFBDisplay18swap_set_icc_curveE13IOMFBCurveLocjjjPK14IOMFBCurveData
+ __ZN2CA12WindowServer12IOMFBDisplay19swap_set_icc_matrixE14IOMFBICCMatLocjjPK16IOMFBColorMatrix
+ __ZN2CA12WindowServer12IOMFBDisplay20current_page_surfaceEbbbbybb
+ __ZN2CA12WindowServer12IOMFBDisplay20wait_for_relbuf_infoEy
+ __ZN2CA12WindowServer12IOMFBDisplay22set_power_state_lockedENS0_17DisplayPowerStateEb
+ __ZN2CA12WindowServer12IOMFBDisplay24set_presentation_latencyEd
+ __ZN2CA12WindowServer12IOMFBDisplay25set_contrast_preservationEf
+ __ZN2CA12WindowServer12IOMFBDisplay25update_power_state_lockedEb
+ __ZN2CA12WindowServer12IOMFBDisplay27set_postprocess_timing_infoEjyy
+ __ZN2CA12WindowServer12IOMFBDisplay28set_low_latency_eligible_pidEi
+ __ZN2CA12WindowServer12IOMFBDisplay29needs_swap_begin_current_pageEj
+ __ZN2CA12WindowServer12IOMFBDisplay31collect_postprocess_timing_infoEjRyS2_Rb
+ __ZN2CA12WindowServer12IOMFBDisplay31update_implicit_power_assertionENS0_12DisplayStateE
+ __ZN2CA12WindowServer12IOMFBDisplay32set_accessibility_display_boundsENS_6BoundsE
+ __ZN2CA12WindowServer12IOMFBDisplay33complete_display_state_transitionENS0_12DisplayStateENS0_19DisplayCloningStateE
+ __ZN2CA12WindowServer12IOMFBDisplay9FrameInfoD2Ev
+ __ZN2CA12WindowServer12IOMFBDisplay9swap_waitEjjb
+ __ZN2CA12WindowServer13IOMFBFlipBook26apply_dbv_flash_workaroundEv
+ __ZN2CA12WindowServer13VirtualServer33complete_display_state_transitionENS0_12DisplayStateENS0_19DisplayCloningStateE
+ __ZN2CA12WindowServer14VirtualDisplay14update_surfaceEbbybb
+ __ZN2CA12WindowServer14VirtualDisplay15current_surfaceEbybb
+ __ZN2CA12WindowServer14VirtualDisplay24set_display_state_lockedEv
+ __ZN2CA12WindowServer14VirtualDisplay33complete_display_state_transitionENS0_12DisplayStateENS0_19DisplayCloningStateE
+ __ZN2CA12WindowServer23display_state_to_stringENS0_12DisplayStateE
+ __ZN2CA12WindowServer31display_cloning_state_to_stringENS0_19DisplayCloningStateE
+ __ZN2CA12WindowServer6Server15current_surfaceEbybb
+ __ZN2CA12WindowServer6Server15set_edr_enabledEbbfPNS_6Render6UpdateE
+ __ZN2CA12WindowServer6Server18RenderIntervalInfo35render_status_to_legacy_reason_codeENS0_12RenderStatusE
+ __ZN2CA12WindowServer6Server20sim_hotplug_callbackEb
+ __ZN2CA12WindowServer6Server20try_swap_begin_asyncEj
+ __ZN2CA12WindowServer6Server21print_display_icc_logEP15x_stream_struct
+ __ZN2CA12WindowServer6Server21set_calibration_phaseEjjj
+ __ZN2CA12WindowServer6Server22set_needs_global_lightEb
+ __ZN2CA12WindowServer6Server23set_frame_info_callbackEU13block_pointerFvjjyyyyjbbbfffyjbyyfE
+ __ZN2CA12WindowServer6Server23set_global_light_paramsENS_6Render17GlobalLightParamsE
+ __ZN2CA12WindowServer6Server24render_display_to_targetEPS1_PNS_6Render17RenderDisplayInfoEPPNS3_7ContextEmPNS3_12RenderTargetE
+ __ZN2CA12WindowServer6Server25set_display_cloning_stateENS0_19DisplayCloningStateEhj
+ __ZN2CA12WindowServer6Server25set_display_cloning_stateEPNS_6Render6ObjectEPvS5_
+ __ZN2CA12WindowServer6Server29schedule_forced_render_updateENS_6Render12UpdateReasonE
+ __ZN2CA12WindowServer6Server30render_display_layer_to_targetEPS1_PNS_6Render22RenderDisplayLayerInfoEPNS3_12RenderTargetE
+ __ZN2CA12WindowServer6Server33complete_display_state_transitionENS0_12DisplayStateENS0_19DisplayCloningStateE
+ __ZN2CA12WindowServer6Server37render_display_context_list_to_targetEPS1_PNS_6Render28RenderDisplayContextListInfoEPNS3_12RenderTargetE
+ __ZN2CA12WindowServer6Server48disable_automatic_wireless_display_state_controlEPNS_6Render6ObjectEPvS5_
+ __ZN2CA12WindowServer7Display15current_surfaceEbybb
+ __ZN2CA12WindowServer7Display15set_power_stateENS0_17DisplayPowerStateEb
+ __ZN2CA12WindowServer7Display18add_shared_surfaceEPNS0_7SurfaceE
+ __ZN2CA12WindowServer7Display20set_user_preferencesEbNS1_7HDRTypeEbbb
+ __ZN2CA12WindowServer7Display21remove_shared_surfaceEPNS0_7SurfaceE
+ __ZN2CA12WindowServer7Display22set_power_state_lockedENS0_17DisplayPowerStateEb
+ __ZN2CA12WindowServer7Display25set_contrast_preservationEf
+ __ZN2CA12WindowServer7Display27DisplayStateTransitionReply5_sendEPKchNS0_28DisplayStateTransitionStatusE
+ __ZN2CA12WindowServer7Display27set_postprocess_timing_infoEjyy
+ __ZN2CA12WindowServer7Display28set_low_latency_eligible_pidEi
+ __ZN2CA12WindowServer7Display29needs_swap_begin_current_pageEj
+ __ZN2CA12WindowServer7Display31collect_postprocess_timing_infoEjRyS2_Rb
+ __ZN2CA12WindowServer7Display31update_implicit_power_assertionENS0_12DisplayStateE
+ __ZN2CA12WindowServer7Display32print_display_trace_shared_eventEP15x_stream_struct
+ __ZN2CA12WindowServer7Display32set_accessibility_display_boundsENS_6BoundsE
+ __ZN2CA12WindowServer7Display7ModeSet22set_mig_representationEPNS1_4ModeEmPjS5_mPNS_6Render11PerModeInfoEmj
+ __ZN2CA12WindowServer7Display9ModePrefs6unpackEPKvPb
+ __ZN2CA12WindowServer7Surface11set_displayEPNS0_7DisplayE
+ __ZN2CA12WindowServer7Surface19set_render_headroomEfb
+ __ZN2CA12WindowServer8FlipBook14collect_memoryEm
+ __ZN2CA12WindowServer9IOSurface19set_render_headroomEfb
+ __ZN2CA12WindowServerL10null_timerEP16__CFRunLoopTimerPv.17653
+ __ZN2CA12WindowServerL16show_layer_treesEP15x_stream_structdPK13x_link_struct
+ __ZN2CA12WindowServerL17print_layer_treesEdPK13x_link_struct
+ __ZN2CA12WindowServerL18edr_request_stringE
+ __ZN2CA12WindowServerL25find_layernode_for_handleEPKNS_6Render9LayerNodeEPKNS1_6HandleE
+ __ZN2CA12WindowServerL27dict_shared_event_set_valueEP14__CFDictionaryPNS_13CASharedEventEbb
+ __ZN2CA13CASharedEvent10initializeEv
+ __ZN2CA13CASharedEvent11UsageStringE
+ __ZN2CA13CASharedEvent12AccessStringE
+ __ZN2CA13CASharedEvent12stream_printEP15x_stream_structP8os_log_s
+ __ZN2CA13CASharedEvent14force_completeEb
+ __ZN2CA13CASharedEvent14get_wait_valueENS0_5UsageENS0_6AccessE
+ __ZN2CA13CASharedEvent15OperationStringE
+ __ZN2CA13CASharedEvent16inc_signal_valueENS0_5UsageENS0_6AccessE
+ __ZN2CA13CASharedEvent19update_signal_valueEyNS0_5UsageENS0_6AccessE
+ __ZN2CA13CASharedEvent24is_complete_with_timeoutEv
+ __ZN2CA13CASharedEvent26update_from_iosurface_listERKN1X12small_vectorINS_11SurfaceUtil31CASurfaceSharedEventTransactionELm5EEE
+ __ZN2CA13CASharedEvent5unrefEv
+ __ZN2CA13CASharedEvent7History3addEPNS_12WindowServer7SurfaceEjNS0_5UsageENS0_9OperationENS0_6AccessEy
+ __ZN2CA14CAHDRProcessor29should_invalidate_tonemappingEffffffff
+ __ZN2CA14CAWorkInterval17release_workgroupEv
+ __ZN2CA14CAWorkInterval21release_work_intervalEv
+ __ZN2CA15ColorAdaptation24RGBXYZConversionMatricesIdEC2ENS0_17RGBColorPrimariesIdEENS0_3xyYIdEE
+ __ZN2CA15ColorAdaptation24RGBXYZConversionMatricesIfEC2ENS0_17RGBColorPrimariesIfEENS0_3xyYIfEE
+ __ZN2CA16TransformDetails7unapplyINS_9TransformEdEEvRKT_RT0_S7_
+ __ZN2CA20HDRProcessorInternal15tonemap_surfaceEP11__IOSurfaceS2_PNS_13CASharedEventES4_PKNS_6Render17DisplayAttributesEPNS5_6UpdateEbyfbPi
+ __ZN2CA20HDRProcessorInternal24tonemap_surface_internalEP11__IOSurfaceS2_PNS_6Render6UpdateEPNS_13CASharedEventES7_R26HDRConfigurationParametersRf22HDRProcessingOperationPKNS3_17DisplayAttributesE24CATonemapAcceleratorTypebPU27objcproto16MTLCommandBuffer11objc_objectPbbNS3_12TextureFlagsEfbPK8__CFDataNS3_11SurfaceTypeEPi
+ __ZN2CA20HDRProcessorInternal30configure_display_pipe_tonemapEP11__IOSurfacejPKNS_6Render17DisplayAttributesEfPP12CGColorSpaceU13block_pointerFvP18IOMFBToneMapConfigEU13block_pointerFv13IOMFBCurveLocPK14IOMFBCurveDataEU13block_pointerFv14IOMFBICCMatLocPK16IOMFBColorMatrixE
+ __ZN2CA20HDRProcessorInternal30create_surface_with_forward_dmEPKNS_6Render7SurfaceEPNS1_6UpdateEPKNS1_17DisplayAttributesEbfNS1_12TextureFlagsEfbbbb
+ __ZN2CA20HDRProcessorInternal36get_or_create_hdr_processor_instanceE25HDRProcessingHardwareTypeP26HDRConfigurationParametersPKNS_6Render17DisplayAttributesE
+ __ZN2CA2CG10fill_imageERNS0_8RendererEP7CGImageRKNS_4RectERKNS_4Mat2IdEEbb22CGInterpolationQualityf13CGToneMappingPK14__CFDictionaryPKNS_6BoundsE
+ __ZN2CA2CG13AccelDrawable22synchronize_attributesEf
+ __ZN2CA2CG13AccelRenderer22synchronize_attributesEf
+ __ZN2CA2CG13GlyphDelegateC2ERNS0_8RendererERNS_3OGL7ContextENS4_13ExtendedColorENS1_10BrightnessEPKNS0_11ShadowStyleEf
+ __ZN2CA2CG13GlyphDelegateD2Ev
+ __ZN2CA2CG14DrawTiledImageD2Ev
+ __ZN2CA2CG15ContextDelegate12device_colorEPKdP12CGColorSpaceff
+ __ZN2CA2CG15FillRectsShadowC1ERNS0_15ContextDelegateERKNS0_9FillRectsEP16CGRenderingStateP8CGGStatePKNS0_11ShadowStyleEj
+ __ZN2CA2CG17AccelDataProvider9wait_dataEv
+ __ZN2CA2CG17IOSurfaceDrawable22synchronize_attributesEf
+ __ZN2CA2CG21FillRoundedRectShadowC1ERNS0_15ContextDelegateERKNS0_15FillRoundedRectEP16CGRenderingStateP8CGGStatePKNS0_11ShadowStyleEj
+ __ZN2CA2CG5Queue31synchronize_attributes_callbackEPv
+ __ZN2CA2CG8Renderer22synchronize_attributesEf
+ __ZN2CA2CG9DrawImageD2Ev
+ __ZN2CA3OGL10FilterNode7prepareEv
+ __ZN2CA3OGL10PathFiller10mark_spansEDv2_fS2_
+ __ZN2CA3OGL10PathFiller7cube_toEDv2_fS2_S2_
+ __ZN2CA3OGL10PathFiller7move_toEDv2_f
+ __ZN2CA3OGL10PathFiller7quad_toEDv2_fS2_
+ __ZN2CA3OGL10PathFiller8add_cubeEDv2_fS2_S2_S2_ff
+ __ZN2CA3OGL10PathFiller9emit_cubeEDv2_fS2_S2_S2_m
+ __ZN2CA3OGL10PathFiller9emit_lineEDv2_fS2_
+ __ZN2CA3OGL10cache_nodeERNS0_8RendererEPNS0_5LayerERKNS_6Render7CacheIdEPNS0_11ImagingNodeEfb
+ __ZN2CA3OGL11GLESContext30create_surface_with_propertiesEiRKNS_6BoundsEjRKNS0_7Context17SurfacePropertiesE
+ __ZN2CA3OGL11NullContext30create_surface_with_propertiesEiRKNS_6BoundsEjRKNS0_7Context17SurfacePropertiesE
+ __ZN2CA3OGL11PathStroker15add_line_pointsEDv2_fS2_
+ __ZN2CA3OGL11PathStroker7cube_toEDv2_fS2_S2_
+ __ZN2CA3OGL11PathStroker7line_toEDv2_f
+ __ZN2CA3OGL11PathStroker7move_toEDv2_f
+ __ZN2CA3OGL11PathStroker7quad_toEDv2_fS2_
+ __ZN2CA3OGL11PathStroker9emit_cubeEDv2_fS2_S2_S2_fm
+ __ZN2CA3OGL11emit_filterERNS0_8RendererERKNS0_6FilterERKNS0_5LayerEfPPNS0_7SurfaceEPfbPKNS_5ShapeESF_SC_SB_
+ __ZN2CA3OGL12MetalContext10image_sizeEPKNS0_5ImageEPm
+ __ZN2CA3OGL12MetalContext11SharedEvent10encode_allEPS1_
+ __ZN2CA3OGL12MetalContext11SharedEvent3addENS2_11PerDrawableE
+ __ZN2CA3OGL12MetalContext15debug_log_imageEP15x_stream_structPKNS_6Render6ObjectEPKNS0_5ImageE
+ __ZN2CA3OGL12MetalContext16add_shared_eventEPNS_13CASharedEventE
+ __ZN2CA3OGL12MetalContext16add_shared_eventEPNS_6Render7SurfaceE
+ __ZN2CA3OGL12MetalContext18destination_formatEv
+ __ZN2CA3OGL12MetalContext19collect_timing_infoEjRyS2_b
+ __ZN2CA3OGL12MetalContext19has_same_mtl_deviceEPNS0_7ContextE
+ __ZN2CA3OGL12MetalContext19shared_event_submitEPNS_13CASharedEventEbNS2_5UsageENS2_6AccessE
+ __ZN2CA3OGL12MetalContext21start_post_processingEj
+ __ZN2CA3OGL12MetalContext22calculate_average_lumaEPNS0_7SurfaceERNS_6BoundsEU13block_pointerFvfE
+ __ZN2CA3OGL12MetalContext22set_protection_optionsEy
+ __ZN2CA3OGL12MetalContext22shared_event_wait_readEPNS_13CASharedEventE
+ __ZN2CA3OGL12MetalContext23ensure_gamma_lut_bufferEv
+ __ZN2CA3OGL12MetalContext23shared_event_wait_writeEPNS_13CASharedEventE
+ __ZN2CA3OGL12MetalContext24shared_event_signal_readEPNS_13CASharedEventE
+ __ZN2CA3OGL12MetalContext24update_texture_ownershipEPNS0_7SurfaceEjiPK10__CFString
+ __ZN2CA3OGL12MetalContext25shared_event_signal_writeEPNS_13CASharedEventE
+ __ZN2CA3OGL12MetalContext30create_surface_with_propertiesEiRKNS_6BoundsEjRKNS0_7Context17SurfacePropertiesE
+ __ZN2CA3OGL12MetalContext32create_variable_blur_mip_surfaceEPNS0_7SurfaceENS_6BoundsENS_4RectEjjfbb
+ __ZN2CA3OGL12_GLOBAL__N_116collect_surfacesEPNS0_7SurfaceEPS3_PNS_6BoundsEbRb
+ __ZN2CA3OGL12_GLOBAL__N_119prepare_blur_mipmapERNS0_8RendererEPNS_6Render13BackdropGroupEPKNS4_13BackdropLayerEPNS0_14BackdropBufferE
+ __ZN2CA3OGL12_GLOBAL__N_128desired_src_edge_replicationEPKNS_6Render13BackdropGroupEPKNS0_5LayerERNS0_7ContextEPNS_4RectEPNS_4Vec2IfEEPbSG_SG_SG_
+ __ZN2CA3OGL12render_shapeERNS0_8RendererEPKNS0_5LayerEPNS_6Render4PathENS_13ScanConverter8FillRuleERKNS_4RectENS_4Vec4IfEEPNS6_7PatternEbf
+ __ZN2CA3OGL15emit_large_brimERNS0_7ContextEPNS0_7SurfaceERNS_4RectEdNS0_13ExtendedColorEfdS7_fRKNS_9TransformEfbi
+ __ZN2CA3OGL15prepare_filtersERNS0_8RendererERNS0_5LayerEPNS_6Render10TypedArrayINS5_6FilterEEEbRNS0_17SourceRequirementEbPS7_
+ __ZN2CA3OGL18prepare_layers_roiERNS0_8RendererEPNS0_5LayerERKNS0_6GstateEPS4_
+ __ZN2CA3OGL19SDFElementGroupNode11compute_dodERNS_6BoundsE
+ __ZN2CA3OGL19SDFElementGroupNode13propagate_roiERKNS_6BoundsE
+ __ZN2CA3OGL19SDFElementGroupNode14retain_surfaceERfj
+ __ZN2CA3OGL19SDFElementGroupNode5applyEfPPNS0_7SurfaceEPf
+ __ZN2CA3OGL19SDFElementGroupNode8grow_roiERNS_6BoundsE
+ __ZN2CA3OGL19SDFElementGroupNodeD0Ev
+ __ZN2CA3OGL19SDFElementGroupNodeD1Ev
+ __ZN2CA3OGL20update_backdrop_lumaERNS0_8RendererE
+ __ZN2CA3OGL22get_filter_color_floatEPKNS_6Render6FilterEjPfb
+ __ZN2CA3OGL22rect_intersects_clip_pERKNS0_6GstateERKNS_4RectE
+ __ZN2CA3OGL23render_solid_backgroundERNS0_8RendererEPKNS0_5LayerENS0_13ExtendedColorEPNS_6Render7PatternEf
+ __ZN2CA3OGL24colormatched_layer_colorERNS0_8RendererEPKNS0_5LayerENS0_13ExtendedColorEf
+ __ZN2CA3OGL24filter_source_layer_nameEPNS0_6FilterE
+ __ZN2CA3OGL25capture_in_place_backdropERNS0_8RendererEbb
+ __ZN2CA3OGL25emit_n_part_rect_occludedERNS0_7ContextERKNS0_9RectStateEiiPKdS7_PKfS9_S9_S9_yj
+ __ZN2CA3OGL27emit_shadow_corner_contentsERNS0_7ContextERNS_4RectERKNS_4Vec2IfEEdNS0_13ExtendedColorEibbRKNS_9TransformEPNS_6Render7TextureES3_fbf
+ __ZN2CA3OGL32compute_variable_blur_parametersEjjRKNS_6BoundsEffb
+ __ZN2CA3OGL33merge_compressed_geometry_clippedEPKdS2_PKfS4_fjPdPfS6_Pt
+ __ZN2CA3OGL7Context10image_sizeEPKNS0_5ImageEPm
+ __ZN2CA3OGL7Context12lookup_imageEPNS_6Render7TextureEb
+ __ZN2CA3OGL7Context13get_debug_logEPNS_6Render6ObjectEPvS5_
+ __ZN2CA3OGL7Context14create_surfaceEiRKNS_6BoundsEj
+ __ZN2CA3OGL7Context15clear_sdf_cacheEv
+ __ZN2CA3OGL7Context15debug_log_imageEP15x_stream_structPKNS_6Render6ObjectEPKNS0_5ImageE
+ __ZN2CA3OGL7Context16add_shared_eventEPNS_13CASharedEventE
+ __ZN2CA3OGL7Context16add_shared_eventEPNS_6Render7SurfaceE
+ __ZN2CA3OGL7Context18destination_formatEv
+ __ZN2CA3OGL7Context18device_float_colorEPfP12CGColorSpacePKdfff
+ __ZN2CA3OGL7Context19collect_timing_infoEjRyS2_b
+ __ZN2CA3OGL7Context19has_same_mtl_deviceEPS1_
+ __ZN2CA3OGL7Context21start_post_processingEj
+ __ZN2CA3OGL7Context21variable_blur_surfaceEfPNS0_7SurfaceEfS3_fPNS_6Render7TextureERKNS_4Mat4IdEERKNS1_10BlurParamsEPfPS3_
+ __ZN2CA3OGL7Context22calculate_average_lumaEPNS0_7SurfaceERNS_6BoundsEU13block_pointerFvfE
+ __ZN2CA3OGL7Context22set_protection_optionsEy
+ __ZN2CA3OGL7Context22shared_event_wait_readEPNS_13CASharedEventE
+ __ZN2CA3OGL7Context23shared_event_wait_writeEPNS_13CASharedEventE
+ __ZN2CA3OGL7Context24shared_event_signal_readEPNS_13CASharedEventE
+ __ZN2CA3OGL7Context24update_texture_ownershipEPNS0_7SurfaceEjiPK10__CFString
+ __ZN2CA3OGL7Context25shared_event_signal_writeEPNS_13CASharedEventE
+ __ZN2CA3OGL7Context30device_color_from_premul_colorEP12CGColorSpaceRKNS0_13ExtendedColorEff
+ __ZN2CA3OGL7Context32create_variable_blur_mip_surfaceEPNS0_7SurfaceENS_6BoundsENS_4RectEjjfbb
+ __ZN2CA3OGL7SDFNode11compute_dodERNS_6BoundsE
+ __ZN2CA3OGL7SDFNode13propagate_roiERKNS_6BoundsE
+ __ZN2CA3OGL7SDFNode17map_shadow_boundsERNS_6BoundsEbNS_4Vec2IfEE
+ __ZN2CA3OGL7SDFNode5applyEfPPNS0_7SurfaceEPf
+ __ZN2CA3OGL7SDFNodeD0Ev
+ __ZN2CA3OGL7SDFNodeD1Ev
+ __ZN2CA3OGL8QuadNode14retain_surfaceERfj
+ __ZN2CA3OGL8Renderer6renderEPKNS_6Render6UpdateEmPNS_13CASharedEventE
+ __ZN2CA3OGL9LayerNode24merge_sdf_element_layersEPNS0_5LayerE
+ __ZN2CA3OGL9LayerNode28retain_filter_source_surfaceEPNS_6Render6StringERfNS_6BoundsEj
+ __ZN2CA3OGL9SWContext30create_surface_with_propertiesEiRKNS_6BoundsEjRKNS0_7Context17SurfacePropertiesE
+ __ZN2CA3OGLL14ycbcr_matricesE.9589
+ __ZN2CA3OGLL18prepare_one_filterERPNS0_6FilterERNS0_8RendererERNS0_5LayerEPKNS_6Render6FilterEbbRNS0_17SourceRequirementE
+ __ZN2CA3OGLL19bind_filter_surfaceERNS0_7ContextEPNS0_7SurfaceEfi
+ __ZN2CA3OGLL20add_primitive_filterEPNS0_6FilterEPKNS_6Render6FilterEb
+ __ZN2CA3OGLL20edr_gain_filter_gainEPKNS_6Render6FilterEPKNS1_6UpdateEff
+ __ZN2CA3OGLL22merge_rr_occl_bins_8x8Ettiib
+ __ZN2CA3OGLL22render_edr_gain_filterERNS0_7ContextEPKNS_6Render6FilterEPKNS3_6UpdateEPNS0_7SurfaceEff
+ __ZN2CA3OGLL27render_vibrant_color_matrixERNS0_8RendererEPKNS_6Render6FilterEPNS0_7SurfaceEfRKNS0_5LayerE
+ __ZN2CA3OGLL31render_edr_gain_multiply_filterERNS0_7ContextEPKNS_6Render6FilterEPKNS3_6UpdateEPNS0_7SurfaceEff
+ __ZN2CA3OGLL38sublayers_could_have_implicit_backdropEPNS_6Render9LayerNodeEPi
+ __ZN2CA5Layer12clear_flags_EPS0_jPNS_11TransactionE
+ __ZN2CA5Layer15perform_update_EPS0_P7CALayerjPNS_11TransactionE
+ __ZN2CA5Layer16update_if_neededEPNS_11TransactionEjj
+ __ZN2CA5Layer17set_needs_update_Ejj
+ __ZN2CA5Layer19thread_flags_match_Ej
+ __ZN2CA6Render11HitTestTree4Node37subtract_subtree_occlusion_from_shapeERKNS_6BoundsEPPNS_5ShapeERi
+ __ZN2CA6Render11PortalLayer12set_propertyEmPKjbmPKd
+ __ZN2CA6Render11ShadowCache13entry_deletedEPNS0_6ObjectEPvS4_
+ __ZN2CA6Render11ShadowCache17free_raster_entryEPNS0_6ObjectEPNS1_11RasterEntryEPv
+ __ZN2CA6Render11ShadowCache17free_shadow_entryEPNS0_6ObjectEPNS1_11ShadowEntryEPv
+ __ZN2CA6Render11WindowLayer12set_propertyEmPKjbmPKd
+ __ZN2CA6Render11WindowLayerC1EPNS0_7DecoderE
+ __ZN2CA6Render11WindowLayerD0Ev
+ __ZN2CA6Render11WindowLayerD1Ev
+ __ZN2CA6Render11show_objectEP15x_stream_structPKNS0_6ObjectE
+ __ZN2CA6Render11show_objectEP15x_stream_structPKNS0_6ObjectEjj
+ __ZN2CA6Render12HostingTokenD0Ev
+ __ZN2CA6Render12HostingTokenD1Ev
+ __ZN2CA6Render12HostingTokenD2Ev
+ __ZN2CA6Render12KeyPathValueC2EPNS0_7DecoderE
+ __ZN2CA6Render12KeyPathValueD0Ev
+ __ZN2CA6Render12KeyPathValueD1Ev
+ __ZN2CA6Render12KeyPathValueD2Ev
+ __ZN2CA6Render12RenderTarget20set_content_headroomEf
+ __ZN2CA6Render13BackdropGroup17subrect_to_masterERKNS_4RectEPNS0_9LayerNodeE
+ __ZN2CA6Render13RenderSurface20set_content_headroomEf
+ __ZN2CA6Render13show_cfstringEP15x_stream_structPK10__CFString
+ __ZN2CA6Render14BasicAnimationC2EPNS0_7DecoderE
+ __ZN2CA6Render14FlattenManager11stage_entryEPNS0_9LayerNodeEPNS0_6UpdateE
+ __ZN2CA6Render14FlattenManager12delete_entryEPNS0_6HandleE
+ __ZN2CA6Render14FlattenManager13restage_entryEPNS0_9LayerNodeEPNS0_6UpdateE
+ __ZN2CA6Render14FlattenManager14flattened_lockE
+ __ZN2CA6Render14FlattenManager15flattened_cacheE
+ __ZN2CA6Render14FlattenManager17flatten_metal_ctxE
+ __ZN2CA6Render14FlattenManager22evaluate_flatten_stateEPNS0_9LayerNodeEPNS0_6UpdateEbb
+ __ZN2CA6Render14FlattenManager24add_free_surface_to_poolEPNS0_16FlattenedSurfaceE
+ __ZN2CA6Render14FlattenManager27flattened_cache_add_surfaceEPKNS0_9LayerNodeEPNS0_16FlattenedSurfaceENS_6BoundsE
+ __ZN2CA6Render14FlattenManager27flattened_free_surface_poolE
+ __ZN2CA6Render14FlattenManager28flatten_cache_current_memoryE
+ __ZN2CA6Render14FlattenManager30flattened_cache_retain_surfaceEPKNS0_9LayerNodeEPNS_3OGL7ContextENS_6BoundsE
+ __ZN2CA6Render14FlattenManager9is_stagerEPKNS0_9LayerNodeE
+ __ZN2CA6Render14color_from_vecEmPKd
+ __ZN2CA6Render14show_transformEP15x_stream_structPKcPKdj
+ __ZN2CA6Render15SDFElementLayer12set_propertyEmPKjbmPKd
+ __ZN2CA6Render15SDFElementLayerC1EPNS0_7DecoderE
+ __ZN2CA6Render15SDFElementLayerD0Ev
+ __ZN2CA6Render15SDFElementLayerD1Ev
+ __ZN2CA6Render15convert_cgcolorEP7CGColorP12CGColorSpaceRNS0_5ColorEPPNS0_7PatternE
+ __ZN2CA6Render15show_statisticsEP15x_stream_struct
+ __ZN2CA6Render17print_group_flagsEP15x_stream_structjj
+ __ZN2CA6Render18OnDemandTonemapCfgaSERKS1_
+ __ZN2CA6Render19FlattenedCacheEntryD2Ev
+ __ZN2CA6Render20InterpolatedFunction13set_locationsEPK9__CFArray
+ __ZN2CA6Render20InterpolatedFunction18set_interpolationsEPK9__CFArray
+ __ZN2CA6Render21print_offscreen_flagsEP15x_stream_structjj
+ __ZN2CA6Render21show_affine_transformEP15x_stream_structPKcRK17CGAffineTransformj
+ __ZN2CA6Render22CloningTerminatorLayerC2EPNS0_7DecoderE
+ __ZN2CA6Render22MatchPropertyAnimationC2EPNS0_7DecoderE
+ __ZN2CA6Render28invoke_presentation_handlersERKNSt3__13setINS0_6Update11ContextInfoENS1_4lessIS4_EENS1_9allocatorIS4_EEEEjdyym
+ __ZN2CA6Render29format_red_component_at_valueEjPKhRf
+ __ZN2CA6Render34get_glass_filter_bleed_blur_radiusEPKNS0_6FilterE
+ __ZN2CA6Render35get_glass_filter_shadow_blur_radiusEPKNS0_6FilterE
+ __ZN2CA6Render5Image16red_component_atEii
+ __ZN2CA6Render6Handle14add_dependenceEPNS1_10DependenceEb
+ __ZN2CA6Render6ObjectC2EPNS0_7DecoderEj
+ __ZN2CA6Render6Server21_decode_commands_lockE
+ __ZN2CA6Render6Update17allowed_in_updateEPNS0_7ContextEPKNS0_5LayerEj
+ __ZN2CA6Render7Context10show_hostsEP15x_stream_struct
+ __ZN2CA6Render7Context11show_hosts_EP15x_stream_structj
+ __ZN2CA6Render7Context17make_hosting_portEv
+ __ZN2CA6Render7Context17show_source_layerEP15x_stream_structjmjj
+ __ZN2CA6Render7Context24context_by_hosting_tokenEPKNS0_12HostingTokenE
+ __ZN2CA6Render7Context7zombifyEv
+ __ZN2CA6Render7Surface16clear_edr_factorEv
+ __ZN2CA6Render7Surface16red_component_atEii
+ __ZN2CA6Render7Texture11get_pointerEPvh
+ __ZN2CA6Render7Texture11set_pointerEPvS2_h
+ __ZN2CA6Render7Texture13unset_pointerEPvh
+ __ZN2CA6Render7Texture16red_component_atEii
+ __ZN2CA6Render7Updater27should_track_layer_headroomEPNS1_10LocalStateEPNS_5ShapeE
+ __ZN2CA6Render7Updater5SDFOp10map_boundsERNS1_11LayerShapesEb
+ __ZN2CA6Render7Updater5SDFOp10unmap_rectERNS_4RectE
+ __ZN2CA6Render7Updater5SDFOp5applyERNS_4RectE
+ __ZN2CA6Render7Updater5SDFOp8map_cropERNS_4RectES4_
+ __ZN2CA6Render7Updater5SDFOp8map_rectERNS_4RectE
+ __ZN2CA6Render7Updater5SDFOpD0Ev
+ __ZN2CA6Render7Updater5SDFOpD1Ev
+ __ZN2CA6Render8Gradient10set_colorsEPK9__CFArrayP12CGColorSpace
+ __ZN2CA6Render8Gradient10set_valuesEmPKjbmPKdP12CGColorSpaceS7_
+ __ZN2CA6Render8SDFLayer12set_propertyEmPKjbmPKd
+ __ZN2CA6Render8SDFLayerC1EPNS0_7DecoderE
+ __ZN2CA6Render8SDFLayerD0Ev
+ __ZN2CA6Render8SDFLayerD1Ev
+ __ZN2CA6Render8SDFLayerD2Ev
+ __ZN2CA6Render9LayerNode22update_frame_transformEPNS_4Vec2IdEEPKNS_4Mat4IdEE
+ __ZN2CA6RenderL11print_flagsEP15x_stream_structoPKPKcmj
+ __ZN2CA6RenderL18release_deallocateEPKvPv.12769
+ __ZN2CA6RenderL18release_image_dataEPKvPv.9206
+ __ZN2CA6RenderL19dynamic_range_atomsE
+ __ZN2CA7Display11DisplayLink20_early_wakeup_offsetE
+ __ZN2CA7Display11DisplayLink8get_linkEPNS0_7DisplayEP11__CFRunLoopPKN1X4ListIPK10__CFStringEEU13block_pointerFbyEU13block_pointerFNS1_11DeferReasonEPK25CADisplayLinkWillFireInfoEU13block_pointerFvR17CATimingReferenceEU13block_pointerFyvE
+ __ZN2CA7Display21DisplayTimingsControl27server_presentation_latencyEv
+ __ZN2CA7Display21DisplayTimingsControl31server_low_latency_eligible_pidEy
+ __ZN2CA7DisplayL20MaxEarlyWakeupOffsetEv
+ __ZN2CA9EDRClient20set_edr_max_headroomEf
+ __ZN2CAL19shared_event_submitEPU19objcproto9MTLDevice11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPNS_13CASharedEventEbNS4_6AccessE
+ __ZNK2CA12ColorProgram7Program4showEP15x_stream_struct
+ __ZNK2CA12WindowServer12AppleDisplay23compressed_pixel_formatEjmNS0_12SurfaceUsageE
+ __ZNK2CA12WindowServer12IOMFBDisplay16minimum_vrr_ioavEv
+ __ZNK2CA12WindowServer12IOMFBDisplay17is_aocp_protectedEv
+ __ZNK2CA12WindowServer12IOMFBDisplay18fvd_mirroring_modeEv
+ __ZNK2CA12WindowServer12IOMFBDisplay18maximum_frame_timeEv
+ __ZNK2CA12WindowServer12IOMFBDisplay18minimum_frame_timeEv
+ __ZNK2CA12WindowServer12IOMFBDisplay20presentation_latencyEv
+ __ZNK2CA12WindowServer12IOMFBDisplay21cloning_active_statusEv
+ __ZNK2CA12WindowServer12IOMFBDisplay21contrast_preservationEv
+ __ZNK2CA12WindowServer12IOMFBDisplay21maximum_vrr_vbl_deltaEv
+ __ZNK2CA12WindowServer12IOMFBDisplay21minimum_vrr_vbl_deltaEv
+ __ZNK2CA12WindowServer12IOMFBDisplay21print_display_icc_logEP15x_stream_struct
+ __ZNK2CA12WindowServer12IOMFBDisplay23compressed_pixel_formatEjmNS0_12SurfaceUsageE
+ __ZNK2CA12WindowServer12IOMFBDisplay23display_can_auto_enableEv
+ __ZNK2CA12WindowServer12IOMFBDisplay24client_preferred_latencyEv
+ __ZNK2CA12WindowServer12IOMFBDisplay24fvd_hdr_tonemapping_modeEv
+ __ZNK2CA12WindowServer12IOMFBDisplay24low_latency_eligible_pidEv
+ __ZNK2CA12WindowServer12IOMFBDisplay27dbv_flash_workaround_activeEv
+ __ZNK2CA12WindowServer12IOMFBDisplay28accessibility_display_boundsEv
+ __ZNK2CA12WindowServer12IOMFBDisplay29is_screen_recording_hdr_localEv
+ __ZNK2CA12WindowServer12IOMFBDisplay33is_screen_recording_hdr_canonicalEv
+ __ZNK2CA12WindowServer12IOMFBDisplay33is_screen_recording_sdr_canonicalEv
+ __ZNK2CA12WindowServer12_GLOBAL__N_122StopBeforeSlotDelegate12render_layerEPNS_6Render9LayerNodeEPKNS3_5LayerE
+ __ZNK2CA12WindowServer20AppleExternalDisplay22minimum_frame_durationEv
+ __ZNK2CA12WindowServer6Server20presentation_latencyEv
+ __ZNK2CA12WindowServer7Display16minimum_vrr_ioavEv
+ __ZNK2CA12WindowServer7Display17is_aocp_protectedEv
+ __ZNK2CA12WindowServer7Display18fvd_mirroring_modeEv
+ __ZNK2CA12WindowServer7Display18maximum_frame_timeEv
+ __ZNK2CA12WindowServer7Display18minimum_frame_timeEv
+ __ZNK2CA12WindowServer7Display20presentation_latencyEv
+ __ZNK2CA12WindowServer7Display21contrast_preservationEv
+ __ZNK2CA12WindowServer7Display21maximum_vrr_vbl_deltaEv
+ __ZNK2CA12WindowServer7Display21minimum_vrr_vbl_deltaEv
+ __ZNK2CA12WindowServer7Display21print_display_icc_logEP15x_stream_struct
+ __ZNK2CA12WindowServer7Display23display_can_auto_enableEv
+ __ZNK2CA12WindowServer7Display24client_preferred_latencyEv
+ __ZNK2CA12WindowServer7Display24fvd_hdr_tonemapping_modeEv
+ __ZNK2CA12WindowServer7Display24low_latency_eligible_pidEv
+ __ZNK2CA12WindowServer7Display27dbv_flash_workaround_activeEv
+ __ZNK2CA12WindowServer7Display27is_enabled_for_vsync_renderEv
+ __ZNK2CA12WindowServer7Display28accessibility_display_boundsEv
+ __ZNK2CA12WindowServer7Display28recording_display_attributesENS_6Render17DisplayAttributesEb
+ __ZNK2CA12WindowServer7Display29is_screen_recording_hdr_localEv
+ __ZNK2CA12WindowServer7Display31all_clones_are_screen_recordingEv
+ __ZNK2CA12WindowServer7Display33is_screen_recording_hdr_canonicalEv
+ __ZNK2CA12WindowServer7Display33is_screen_recording_sdr_canonicalEv
+ __ZNK2CA12WindowServer7Display38is_enabled_for_replay_render_with_modeEv
+ __ZNK2CA12WindowServer7Display7ModeSet28preferred_mode_with_criteriaERKNS2_21PreferredModeCriteriaE
+ __ZNK2CA12WindowServer7Display7ModeSet37preferred_mode_with_criteria_internalE6CGSizefNS1_7HDRTypeEbbRKNS1_14EDIDAttributesEbS4_bbb
+ __ZNK2CA19IOMobileFramebuffer25print_icc_curve_to_streamEP15x_stream_struct13IOMFBCurveLocjjjPK14IOMFBCurveData
+ __ZNK2CA19IOMobileFramebuffer26print_icc_matrix_to_streamEP15x_stream_struct14IOMFBICCMatLocjjPK16IOMFBColorMatrix
+ __ZNK2CA3OGL10BlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfPKNS_11ColorMatrixE
+ __ZNK2CA3OGL12_GLOBAL__N_114PageCurlFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfPKNS_11ColorMatrixE
+ __ZNK2CA3OGL14FilterSubclass17filter_source_roiERNS0_8RendererEPKNS_6Render6FilterEPKNS0_5LayerERNS_6BoundsE
+ __ZNK2CA3OGL14FilterSubclass6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfbPKNS_11ColorMatrixEPKNS_5ShapeESK_SE_SD_
+ __ZNK2CA3OGL15SampleMapFilter10can_renderEPKNS_6Render6FilterEPKNS2_5LayerERNS0_7ContextERKNS0_6GstateE
+ __ZNK2CA3OGL15SampleMapFilter12filter_flagsEPKNS_6Render6FilterEPKNS0_5LayerE
+ __ZNK2CA3OGL15SampleMapFilter12opaque_shapeEPKNS_6Render6FilterEPKNS2_5LayerERNS_4RectE
+ __ZNK2CA3OGL15SampleMapFilter13get_edge_infoEPKNS_6Render6FilterEPKNS2_5LayerERNS0_7ContextEPNS_4RectEPNS_4Vec2IfEEPb
+ __ZNK2CA3OGL15SampleMapFilter18empty_opaque_shapeEPKNS_6Render6FilterEPKNS2_5LayerE
+ __ZNK2CA3OGL15SampleMapFilter18source_requirementEPKNS_6Render6FilterE
+ __ZNK2CA3OGL15SampleMapFilter3DODEPKNS_6Render6FilterEPKNS2_5LayerERNS_4RectE
+ __ZNK2CA3OGL15SampleMapFilter3ROIEPKNS_6Render6FilterEPKNS2_5LayerERNS_4RectE
+ __ZNK2CA3OGL15SampleMapFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfPKNS_11ColorMatrixE
+ __ZNK2CA3OGL15SampleMapFilter8identityEPKNS_6Render6FilterE
+ __ZNK2CA3OGL15SampleMapFilter9max_rangeEPKNS_6Render6FilterE
+ __ZNK2CA3OGL18AverageColorFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfPKNS_11ColorMatrixE
+ __ZNK2CA3OGL18GaussianBlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfbPKNS_11ColorMatrixEPKNS_5ShapeESK_SE_SD_
+ __ZNK2CA3OGL18VariableBlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfbPKNS_11ColorMatrixEPKNS_5ShapeESK_SE_SD_
+ __ZNK2CA3OGL19LanczosResizeFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfPKNS_11ColorMatrixE
+ __ZNK2CA3OGL21DisplacementMapFilter16texture_functionEv
+ __ZNK2CA3OGL21GlassBackgroundFilter10can_renderEPKNS_6Render6FilterEPKNS2_5LayerERNS0_7ContextERKNS0_6GstateE
+ __ZNK2CA3OGL21GlassBackgroundFilter12filter_flagsEPKNS_6Render6FilterEPKNS0_5LayerE
+ __ZNK2CA3OGL21GlassBackgroundFilter12opaque_shapeEPKNS_6Render6FilterEPKNS2_5LayerERNS_4RectE
+ __ZNK2CA3OGL21GlassBackgroundFilter13get_edge_infoEPKNS_6Render6FilterEPKNS2_5LayerERNS0_7ContextEPNS_4RectEPNS_4Vec2IfEEPb
+ __ZNK2CA3OGL21GlassBackgroundFilter17filter_source_roiERNS0_8RendererEPKNS_6Render6FilterEPKNS0_5LayerERNS_6BoundsE
+ __ZNK2CA3OGL21GlassBackgroundFilter18empty_opaque_shapeEPKNS_6Render6FilterEPKNS2_5LayerE
+ __ZNK2CA3OGL21GlassBackgroundFilter18source_requirementEPKNS_6Render6FilterE
+ __ZNK2CA3OGL21GlassBackgroundFilter3DODEPKNS_6Render6FilterEPKNS2_5LayerERNS_4RectE
+ __ZNK2CA3OGL21GlassBackgroundFilter3ROIEPKNS_6Render6FilterEPKNS2_5LayerERNS_4RectE
+ __ZNK2CA3OGL21GlassBackgroundFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfPKNS_11ColorMatrixE
+ __ZNK2CA3OGL21GlassBackgroundFilter8identityEPKNS_6Render6FilterE
+ __ZNK2CA3OGL21GlassForegroundFilter10can_renderEPKNS_6Render6FilterEPKNS2_5LayerERNS0_7ContextERKNS0_6GstateE
+ __ZNK2CA3OGL21GlassForegroundFilter12filter_flagsEPKNS_6Render6FilterEPKNS0_5LayerE
+ __ZNK2CA3OGL21GlassForegroundFilter12opaque_shapeEPKNS_6Render6FilterEPKNS2_5LayerERNS_4RectE
+ __ZNK2CA3OGL21GlassForegroundFilter18empty_opaque_shapeEPKNS_6Render6FilterEPKNS2_5LayerE
+ __ZNK2CA3OGL21GlassForegroundFilter18source_requirementEPKNS_6Render6FilterE
+ __ZNK2CA3OGL21GlassForegroundFilter3DODEPKNS_6Render6FilterEPKNS2_5LayerERNS_4RectE
+ __ZNK2CA3OGL21GlassForegroundFilter3ROIEPKNS_6Render6FilterEPKNS2_5LayerERNS_4RectE
+ __ZNK2CA3OGL21GlassForegroundFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfPKNS_11ColorMatrixE
+ __ZNK2CA3OGL21GlassForegroundFilter8identityEPKNS_6Render6FilterE
+ __ZNK2CA3OGL25ChromaticAberrationFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfPKNS_11ColorMatrixE
+ __ZNK2CA3OGL28ChromaticAberrationMapFilter16texture_functionEv
+ __ZNK2CA3OGL8LimitAPL6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfPKNS_11ColorMatrixE
+ __ZNK2CA4Vec4IfE6word32Ev
+ __ZNK2CA6Render10ImageQueue4showEP15x_stream_structjj
+ __ZNK2CA6Render10MediaLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render10ShapeLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render10Subtexture4showEP15x_stream_structjj
+ __ZNK2CA6Render10Transition4showEP15x_stream_structjj
+ __ZNK2CA6Render11PixelBuffer4showEP15x_stream_structjj
+ __ZNK2CA6Render11PortalLayer12get_propertyEmPKjmPdPS4_
+ __ZNK2CA6Render11PortalLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render11WindowLayer12get_propertyEmPKjmPdPS4_
+ __ZNK2CA6Render11WindowLayer14visit_subclassERKNS0_20LayerSubclassVisitorE
+ __ZNK2CA6Render11WindowLayer4copyEv
+ __ZNK2CA6Render11WindowLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render11WindowLayer6encodeEPNS0_7EncoderE
+ __ZNK2CA6Render12GainMapLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render12Interpolator4showEP15x_stream_structjj
+ __ZNK2CA6Render12KeyPathValue4showEP15x_stream_structjj
+ __ZNK2CA6Render12KeyPathValue6encodeEPNS0_7EncoderE
+ __ZNK2CA6Render12MetalTexture4showEP15x_stream_structjj
+ __ZNK2CA6Render13BackdropLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render13GradientLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render13ImageProvider4showEP15x_stream_structjj
+ __ZNK2CA6Render13MeshTransform4showEP15x_stream_structjj
+ __ZNK2CA6Render13NamedFunction4showEP15x_stream_structjj
+ __ZNK2CA6Render14MatchAnimation20show_match_animationEP15x_stream_structjj
+ __ZNK2CA6Render14UpdateDelegate12render_layerEPNS0_9LayerNodeEPKNS0_5LayerE
+ __ZNK2CA6Render15CompressedImage4showEP15x_stream_structjj
+ __ZNK2CA6Render15EmitterBehavior4showEP15x_stream_structjj
+ __ZNK2CA6Render15ReplicatorLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render15SDFElementLayer10get_boundsEPKNS0_5LayerERNS_4RectEPS5_
+ __ZNK2CA6Render15SDFElementLayer12get_propertyEmPKjmPdPS4_
+ __ZNK2CA6Render15SDFElementLayer14has_backgroundEPKNS0_5LayerERb
+ __ZNK2CA6Render15SDFElementLayer14visit_subclassERKNS0_20LayerSubclassVisitorE
+ __ZNK2CA6Render15SDFElementLayer17hit_test_contentsEPKNS0_5LayerERKNS_4Vec2IdEE
+ __ZNK2CA6Render15SDFElementLayer4copyEv
+ __ZNK2CA6Render15SDFElementLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render15SDFElementLayer6encodeEPNS0_7EncoderE
+ __ZNK2CA6Render15SDFElementLayer8hit_testEPKNS0_5LayerERKNS_4Vec2IdEE
+ __ZNK2CA6Render17DeferredImageSlot4showEP15x_stream_structjj
+ __ZNK2CA6Render17DisplayAttributeseqERKS1_
+ __ZNK2CA6Render18CarPlayRegionLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render18DistanceFieldLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render18MatchMoveAnimation4showEP15x_stream_structjj
+ __ZNK2CA6Render20PresentationModifier4showEP15x_stream_structjj
+ __ZNK2CA6Render20SecureIndicatorLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render22CloningTerminatorLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render22MatchPropertyAnimation4showEP15x_stream_structjj
+ __ZNK2CA6Render4Path4showEP15x_stream_structjj
+ __ZNK2CA6Render5Array4showEP15x_stream_structjj
+ __ZNK2CA6Render5Image4showEP15x_stream_structjj
+ __ZNK2CA6Render5Layer10process_idEv
+ __ZNK2CA6Render5Layer15show_compressedEP15x_stream_structjj
+ __ZNK2CA6Render5Layer24supports_cc_edge_effectsEv
+ __ZNK2CA6Render5Layer4showEP15x_stream_structjj
+ __ZNK2CA6Render5Layer5frameEPKS1_
+ __ZNK2CA6Render5Proxy4showEP15x_stream_structjj
+ __ZNK2CA6Render5Shmem4showEP15x_stream_structjj
+ __ZNK2CA6Render6Filter4showEP15x_stream_structjj
+ __ZNK2CA6Render6Object4showEP15x_stream_structjj
+ __ZNK2CA6Render6String4showEP15x_stream_structjj
+ __ZNK2CA6Render6Timing4showEP15x_stream_structjj
+ __ZNK2CA6Render6Vector4showEP15x_stream_structjj
+ __ZNK2CA6Render7Pattern4showEP15x_stream_structjj
+ __ZNK2CA6Render7Surface4showEP15x_stream_structjj
+ __ZNK2CA6Render7Texture18has_hdr_colorspaceEv
+ __ZNK2CA6Render7Updater5SDFOp4copyEP13x_heap_struct
+ __ZNK2CA6Render8Gradient10get_valuesEmPKjmPdPS4_
+ __ZNK2CA6Render8Gradient16create_color_mapEP12CGColorSpaceb
+ __ZNK2CA6Render8KeyValue4showEP15x_stream_structjj
+ __ZNK2CA6Render8SDFLayer10get_boundsEPKNS0_5LayerERNS_4RectEPS5_
+ __ZNK2CA6Render8SDFLayer11sdf_paddingEv
+ __ZNK2CA6Render8SDFLayer12get_propertyEmPKjmPdPS4_
+ __ZNK2CA6Render8SDFLayer14has_backgroundEPKNS0_5LayerERb
+ __ZNK2CA6Render8SDFLayer14visit_subclassERKNS0_20LayerSubclassVisitorE
+ __ZNK2CA6Render8SDFLayer4copyEv
+ __ZNK2CA6Render8SDFLayer4showEP15x_stream_structjj
+ __ZNK2CA6Render8SDFLayer6encodeEPNS0_7EncoderE
+ __ZNK2CA6Render9Animation4showEP15x_stream_structjj
+ __ZNK2CA6Render9LayerHost4showEP15x_stream_structjj
+ __ZNKSt3__110__function6__funcIZN2CA6Render14FlattenManager43flattened_cache_print_all_flattened_entriesEP15x_stream_structE3$_0NS_9allocatorIS7_EEFvjPNS3_19FlattenedCacheEntryEEE7__cloneEPNS0_6__baseISC_EE
+ __ZNKSt3__110__function6__funcIZN2CA6Render14FlattenManager43flattened_cache_print_all_flattened_entriesEP15x_stream_structE3$_0NS_9allocatorIS7_EEFvjPNS3_19FlattenedCacheEntryEEE7__cloneEv
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8nn200100IPNS_4pairIyyEENS_16__deque_iteratorIS5_S6_RS5_PS6_lLl256EEELi0EEENS4_IT_T0_EESB_SB_SC_
+ __ZNKSt3__116__deque_iteratorINS_4pairIyyEEPS2_RS2_PS3_lLl256EEplB8nn200100El
+ __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB8nn200100IPNS_4pairIyyEENS_16__deque_iteratorIS5_S6_RS5_PS6_lLl256EEELi0EEENS4_IT_T0_EESB_SB_SC_
+ __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn200100EPKvm
+ __ZNKSt3__122__unordered_map_hasherIN2CA3OGL12MetalContext12VertexShader4SpecENS_17__hash_value_typeIS5_PS4_EENS3_12StructHasherIS5_EENS_8equal_toIS5_EELb1EEclB8nn200100ERKS5_
+ __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn200100ERKS6_S9_
+ __ZNSt3__110__function12__value_funcIFbNS_16reverse_iteratorINS_11__wrap_iterIPN2CA12WindowServer8FlipBook5FrameEEEEEEED2B8nn200100Ev
+ __ZNSt3__110__function12__value_funcIFbPN2CA3OGL6VertexEjEED2B8nn200100Ev
+ __ZNSt3__110__function12__value_funcIFvjPN2CA6Render19FlattenedCacheEntryEEED2B8nn200100Ev
+ __ZNSt3__110__function6__funcIZN2CA6Render14FlattenManager43flattened_cache_print_all_flattened_entriesEP15x_stream_structE3$_0NS_9allocatorIS7_EEFvjPNS3_19FlattenedCacheEntryEEE18destroy_deallocateEv
+ __ZNSt3__110__function6__funcIZN2CA6Render14FlattenManager43flattened_cache_print_all_flattened_entriesEP15x_stream_structE3$_0NS_9allocatorIS7_EEFvjPNS3_19FlattenedCacheEntryEEE7destroyEv
+ __ZNSt3__110__function6__funcIZN2CA6Render14FlattenManager43flattened_cache_print_all_flattened_entriesEP15x_stream_structE3$_0NS_9allocatorIS7_EEFvjPNS3_19FlattenedCacheEntryEEED0Ev
+ __ZNSt3__110__function6__funcIZN2CA6Render14FlattenManager43flattened_cache_print_all_flattened_entriesEP15x_stream_structE3$_0NS_9allocatorIS7_EEFvjPNS3_19FlattenedCacheEntryEEED1Ev
+ __ZNSt3__110__function6__funcIZN2CA6Render14FlattenManager43flattened_cache_print_all_flattened_entriesEP15x_stream_structE3$_0NS_9allocatorIS7_EEFvjPNS3_19FlattenedCacheEntryEEEclEOjOSB_
+ __ZNSt3__110unique_ptrIN2CA12WindowServer12IOMFBDisplay9FrameInfoENS_14default_deleteIS4_EEE5resetB8nn200100EPS4_
+ __ZNSt3__110unique_ptrIN2CA12WindowServer12IOMFBDisplay9FrameInfoENS_14default_deleteIS4_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrIN2CA3OGL13DebugRendererENS_14default_deleteIS3_EEE5resetB8nn200100EPS3_
+ __ZNSt3__110unique_ptrIN2CA6Render13ContentStreamENS_14default_deleteIS3_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_IN2CA6Render13ContentStreamENS_14default_deleteIS5_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_mapIjjNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjjEEEEEEEEPvEENS_22__hash_node_destructorINS8_ISG_EEEEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEEEEEPvEENS_22__hash_node_destructorINS8_ISD_EEEEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIiZN2CA3OGL7Context16show_image_cacheEP15x_stream_structE20CachedImagesWithSizeEEPvEENS_22__tree_node_destructorINS_9allocatorISB_EEEEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEMNS_19__async_assoc_stateIP10SILManagerNS_12__async_funcIZL16sil_mgr_instancePvjE3$_0JP19NSMutableDictionaryEEEEEFvvEPSF_EEENS3_ISJ_EEED1B8nn200100Ev
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN2CA12WindowServer12IOMFBDisplay20update_digital_modesERNS3_7Display7ModeSetERNS5_4ModeEPK9__CFArraySC_E3$_0PS8_Lb0EEEvT1_SG_T0_NS_15iterator_traitsISG_E15difference_typeEb
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN2CA12WindowServer8FlipBook10next_frameEmmE3$_0PNS4_5FrameELb0EEEvT1_S9_T0_NS_15iterator_traitsIS9_E15difference_typeEb
+ __ZNSt3__111__introsortINS_17_ClassicAlgPolicyERZN2CA3OGL9LayerNode24merge_sdf_element_layersEPNS3_5LayerEE3$_0PZNS4_24merge_sdf_element_layersES6_E13SublayerFrameLb0EEEvT1_SB_T0_NS_15iterator_traitsISB_E15difference_typeEb
+ __ZNSt3__112__destroy_atB8nn200100IN2CA3OGL22TransientRenderTextureELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8nn200100IN2CA6Render19ContentStreamConfigELi0EEEvPT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2CA3OGL15BoundsAlignmentEmEENS_22__unordered_map_hasherIS4_S5_NS3_19BoundsAlignmentHashENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S5_S9_S7_Lb1EEENS_9allocatorIS5_EEE25__emplace_unique_key_argsIS4_JNS_4pairIKS4_mEEEEENSH_INS_15__hash_iteratorIPNS_11__hash_nodeIS5_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2CA3OGL7Context17RenderObjectSliceEPNS3_5ImageEEENS_22__unordered_map_hasherIS5_S8_NS5_4HashENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SC_SA_Lb1EEENS_9allocatorIS8_EEE4findIS5_EENS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2CA3OGL7Context17RenderObjectSliceEPNS3_5ImageEEENS_22__unordered_map_hasherIS5_S8_NS5_4HashENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SC_SA_Lb1EEENS_9allocatorIS8_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS8_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjPN1X4ListIU13block_pointerFvP17CAFenceResolutionEEEEENS_22__unordered_map_hasherIjSA_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjSA_SF_SD_Lb1EEENS_9allocatorISA_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSQ_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjPN1X4ListIU13block_pointerFvP17CAFenceResolutionEEEEENS_22__unordered_map_hasherIjSA_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjSA_SF_SD_Lb1EEENS_9allocatorISA_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIjPN1X4ListIU13block_pointerFvP17CAFenceResolutionEEEEENS_22__unordered_map_hasherIjSA_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjSA_SF_SD_Lb1EEENS_9allocatorISA_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImPN2CA3OGL7SurfaceEEENS_22__unordered_map_hasherImS6_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findImEENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeImPN2CA3OGL7SurfaceEEENS_22__unordered_map_hasherImS6_NS_4hashImEENS_8equal_toImEELb1EEENS_21__unordered_map_equalImS6_SB_S9_Lb1EEENS_9allocatorIS6_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn200100ILi0EEEPKc
+ __ZNSt3__113__tree_removeB8nn200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__114__split_bufferIPNS_4pairIyyEENS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS3_EEE12emplace_backIJRS3_EEEvDpOT_
+ __ZNSt3__114__thread_proxyB8nn200100INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEMNS_19__async_assoc_stateIP10SILManagerNS_12__async_funcIZL16sil_mgr_instancePvjE3$_0JP19NSMutableDictionaryEEEEEFvvEPSG_EEEEESB_SB_
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI20CAFrameIntervalRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI22CAFrameIntervalRequestEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CA12WindowServer7Display4ModeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CA12WindowServer8FlipBook5FrameEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CA4Vec2IiEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CA6Render10MeshVertexEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CA6Render20ContentStreamSurfaceEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CA6Render6Update15SecureIndicatorEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CA6Render7Context4SlotEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CA6Render8MeshEdgeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CA6Render8MeshFaceEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_10unique_ptrIN2CA12WindowServer12IOMFBDisplay9FrameInfoENS_14default_deleteIS6_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_4pairIjNS_6vectorIN2CA4Vec2IiEENS1_IS6_EEEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPKN2CA6Render15EmitterBehavior4EvalEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPN2CA7Display15DisplayLinkItemEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPNS_4pairIyyEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPPU19objcproto9MTLBuffer11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_future_errorB8nn200100ENS_11future_errcE
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP11CAAnimationPKN2CA6Render14BasicAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP11CAAnimationPKN2CA6Render15SpringAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP11CAAnimationPKN2CA6Render17KeyframeAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP12CAShapeLayerPKN2CA6Render10ShapeLayerEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP15CABackdropLayerPKN2CA6Render13BackdropLayerEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP15CAGradientLayerPKN2CA6Render13GradientLayerEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP16CABasicAnimationPKN2CA6Render14BasicAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP16CABasicAnimationPKN2CA6Render15SpringAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP17CAReplicatorLayerPKN2CA6Render15ReplicatorLayerEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP17CASpringAnimationPKN2CA6Render15SpringAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP19CAKeyframeAnimationPKN2CA6Render17KeyframeAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP19CAPropertyAnimationPKN2CA6Render14BasicAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP19CAPropertyAnimationPKN2CA6Render15SpringAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP19CAPropertyAnimationPKN2CA6Render17KeyframeAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP7CALayerPKN2CA6Render5LayerESF_RKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSP_
+ __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP8CAFilterPKN2CA6Render6FilterEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn200100EPSS_
+ __ZNSt3__125__throw_bad_function_callB8nn200100Ev
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA12WindowServer7Display4ModeEEEbT1_SA_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA6Render12_GLOBAL__N_18IntervalEEEbT1_SA_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERPFbRK22CAFrameIntervalRequestS4_EPS2_EEbT1_S9_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERZ30CAShmemImageQueueCopyImageInfoE3$_0PP23_CAShmemImageQueueImageEEbT1_S7_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERZN2CA12WindowServer12IOMFBDisplay20update_digital_modesERNS3_7Display7ModeSetERNS5_4ModeEPK9__CFArraySC_E3$_0PS8_EEbT1_SG_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERZN2CA12WindowServer8FlipBook10next_frameEmmE3$_0PNS4_5FrameEEEbT1_S9_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERZN2CA3OGL10PathFiller22emit_rects_from_pointsEiiE3$_0PNS4_13ScanlinePointEEEbT1_S9_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERZN2CA3OGL9LayerNode24merge_sdf_element_layersEPNS3_5LayerEE3$_0PZNS4_24merge_sdf_element_layersES6_E13SublayerFrameEEbT1_SB_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERZN2CA6Render13BackdropGroup15finalize_updateEjbPvE3$_0PNS4_4ItemEEEbT1_SA_T0_
+ __ZNSt3__127__tree_balance_after_insertB8nn200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__13mapIiZN2CA3OGL7Context16show_image_cacheEP15x_stream_structE20CachedImagesWithSizeNS_4lessIiEENS_9allocatorINS_4pairIKiS6_EEEEEixERSB_
+ __ZNSt3__15dequeIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE25__maybe_remove_back_spareB8nn200100Eb
+ __ZNSt3__15dequeIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE26__maybe_remove_front_spareB8nn200100Eb
+ __ZNSt3__15dequeIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEED2B8nn200100Ev
+ __ZNSt3__16__treeINS_12__value_typeIiZN2CA3OGL7Context16show_image_cacheEP15x_stream_structE20CachedImagesWithSizeEENS_19__map_value_compareIiS8_NS_4lessIiEELb1EEENS_9allocatorIS8_EEE7destroyEPNS_11__tree_nodeIS8_PvEE
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16localeD1Ev
+ __ZNSt3__16vectorI10CAMeshFaceNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI12CAMeshVertexNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI20CAFrameIntervalRangeNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI22CAFrameIntervalRequestNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN1X3RefIN2CA6Render6HandleEEENS_9allocatorIS6_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorIN1X3RefIN2CA6Render6HandleEEENS_9allocatorIS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN1X3RefIN2CA6Render6HandleEEENS_9allocatorIS6_EEE9push_backB8nn200100EOS6_
+ __ZNSt3__16vectorIN1X3RefIN2CA6Render7ContextEEENS_9allocatorIS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA12WindowServer11IOMFBServer12ContributorsENS_9allocatorIS4_EEE12emplace_backIJS4_EEERS4_DpOT_
+ __ZNSt3__16vectorIN2CA12WindowServer11IOMFBServer12ContributorsENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA12WindowServer12IOMFBDisplay31FrameIntervalReasonRegistrationENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA12WindowServer7Display4ModeENS_9allocatorIS4_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CA12WindowServer7Display4ModeENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA12WindowServer7Display4ModeENS_9allocatorIS4_EEE20__throw_out_of_rangeB8nn200100Ev
+ __ZNSt3__16vectorIN2CA12WindowServer8FlipBook5FrameENS_9allocatorIS4_EEE18__insert_with_sizeB8nn200100INS_11__wrap_iterIPS4_EESB_EESB_NS9_IPKS4_EET_T0_l
+ __ZNSt3__16vectorIN2CA12WindowServer8FlipBook5FrameENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA12WindowServer8FlipBook5FrameENS_9allocatorIS4_EEE9push_backB8nn200100ERKS4_
+ __ZNSt3__16vectorIN2CA3OGL22TransientRenderTextureENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA4Vec2IdEENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA4Vec2IdEENS_9allocatorIS3_EEE9push_backB8nn200100ERKS3_
+ __ZNSt3__16vectorIN2CA4Vec2IiEENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render10MeshVertexENS_9allocatorIS3_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CA6Render10MeshVertexENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render12_GLOBAL__N_111VertexPointENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render12_GLOBAL__N_18IntervalENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render12_GLOBAL__N_18IntervalENS_9allocatorIS4_EEE9push_backB8nn200100EOS4_
+ __ZNSt3__16vectorIN2CA6Render15DeferredEncoder10TimingInfoENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render19ContentStreamConfigENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render20ContentStreamSurfaceENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render20ContentStreamSurfaceENS_9allocatorIS3_EEE9push_backB8nn200100ERKS3_
+ __ZNSt3__16vectorIN2CA6Render6Update15SecureIndicatorENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render6Update15SecureIndicatorENS_9allocatorIS4_EEE9push_backB8nn200100ERKS4_
+ __ZNSt3__16vectorIN2CA6Render7Context13BeginTimeInfoENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render7Context4SlotENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render8MeshEdgeENS_9allocatorIS3_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CA6Render8MeshEdgeENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CA6Render8MeshFaceENS_9allocatorIS3_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CA6Render8MeshFaceENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN2CA12WindowServer12IOMFBDisplay9FrameInfoENS_14default_deleteIS5_EEEENS_9allocatorIS8_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN2CA12WindowServer12IOMFBDisplay9FrameInfoENS_14default_deleteIS5_EEEENS_9allocatorIS8_EEE9push_backB8nn200100EOS8_
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE5clearB8nn200100Ev
+ __ZNSt3__16vectorINS_13unordered_mapIPvPN2CA6Render9LayerNodeENS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorINS_4pairIKS2_S6_EEEEEENSB_ISG_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_13unordered_mapIPvPN2CA6Render9LayerNodeENS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorINS_4pairIKS2_S6_EEEEEENSB_ISG_EEE9push_backB8nn200100EOSG_
+ __ZNSt3__16vectorINS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEENS6_IS8_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEENS6_IS8_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEEENS6_IS8_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEEENS6_IS8_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairIPKN2CA6Render6ObjectEPKNS2_3OGL5ImageEEENS_9allocatorISB_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairIjNS0_IN2CA4Vec2IiEENS_9allocatorIS4_EEEEEENS5_IS8_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairIjNS0_IN2CA4Vec2IiEENS_9allocatorIS4_EEEEEENS5_IS8_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_5tupleIJPN2CA7Context14DeferredCommitES5_EEENS_9allocatorIS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_5tupleIJijijNS_13unordered_setIPN2CA6Render6StringENS_4hashIS6_EENS_8equal_toIS6_EENS_9allocatorIS6_EEEEEEENSB_ISE_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS_5tupleIJijijNS_13unordered_setIPN2CA6Render6StringENS_4hashIS6_EENS_8equal_toIS6_EENS_9allocatorIS6_EEEEEEENSB_ISE_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPKN2CA6Render15EmitterBehavior4EvalENS_9allocatorIS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA12WindowServer12IOMFBDisplayENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA12WindowServer6ServerENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA12WindowServer7SurfaceENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA12WindowServer7SurfaceENS_9allocatorIS4_EEE9push_backB8nn200100ERKS4_
+ __ZNSt3__16vectorIPN2CA6Render16NotificationItemENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA6Render5Fence15TransactionInfoENS_9allocatorIS5_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA6Render6HandleENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA6Render6ObjectENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA6Render7ContextENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA7ContextENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA7Display15DisplayEDRStateENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CA7Display15DisplayLinkItemENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIU13block_pointerFvvENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE9push_backB8nn200100ERKd
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE9push_backB8nn200100EOh
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE9push_backB8nn200100ERKm
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__17__sort3B8nn200100INS_17_ClassicAlgPolicyERZN2CA12WindowServer12IOMFBDisplay20update_digital_modesERNS3_7Display7ModeSetERNS5_4ModeEPK9__CFArraySC_E3$_0PS8_Li0EEEbT1_SG_SG_T0_
+ __ZNSt3__17__sort4B8nn200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA12WindowServer7Display4ModeELi0EEEvT1_SA_SA_SA_T0_
+ __ZNSt3__17__sort4B8nn200100INS_17_ClassicAlgPolicyERZN2CA12WindowServer12IOMFBDisplay20update_digital_modesERNS3_7Display7ModeSetERNS5_4ModeEPK9__CFArraySC_E3$_0PS8_Li0EEEvT1_SG_SG_SG_T0_
+ __ZNSt3__17__sort4B8nn200100INS_17_ClassicAlgPolicyERZN2CA12WindowServer8FlipBook10next_frameEmmE3$_0PNS4_5FrameELi0EEEvT1_S9_S9_S9_T0_
+ __ZNSt3__17__sort4B8nn200100INS_17_ClassicAlgPolicyERZN2CA3OGL9LayerNode24merge_sdf_element_layersEPNS3_5LayerEE3$_0PZNS4_24merge_sdf_element_layersES6_E13SublayerFrameLi0EEEvT1_SB_SB_SB_T0_
+ __ZNSt3__17__sort4B8nn200100INS_17_ClassicAlgPolicyERZN2CA6Render13BackdropGroup15finalize_updateEjbPvE3$_0PNS4_4ItemELi0EEEvT1_SA_SA_SA_T0_
+ __ZNSt3__17__sort5B8nn200100INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA6Render12_GLOBAL__N_18IntervalELi0EEEvT1_SA_SA_SA_SA_T0_
+ __ZNSt3__17__sort5B8nn200100INS_17_ClassicAlgPolicyERPFbRK22CAFrameIntervalRequestS4_EPS2_Li0EEEvT1_S9_S9_S9_S9_T0_
+ __ZNSt3__17__sort5B8nn200100INS_17_ClassicAlgPolicyERZ30CAShmemImageQueueCopyImageInfoE3$_0PP23_CAShmemImageQueueImageLi0EEEvT1_S7_S7_S7_S7_T0_
+ __ZNSt3__17__sort5B8nn200100INS_17_ClassicAlgPolicyERZN2CA12WindowServer12IOMFBDisplay20update_digital_modesERNS3_7Display7ModeSetERNS5_4ModeEPK9__CFArraySC_E3$_0PS8_Li0EEEvT1_SG_SG_SG_SG_T0_
+ __ZNSt3__17__sort5B8nn200100INS_17_ClassicAlgPolicyERZN2CA3OGL10PathFiller22emit_rects_from_pointsEiiE3$_0PNS4_13ScanlinePointELi0EEEvT1_S9_S9_S9_S9_T0_
+ __ZNSt3__17__sort5B8nn200100INS_17_ClassicAlgPolicyERZN2CA6Render13BackdropGroup15finalize_updateEjbPvE3$_0PNS4_4ItemELi0EEEvT1_SA_SA_SA_SA_T0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8nn200100IRPN2CA12WindowServer8FlipBook5FrameES9_EEvOT_OT0_
+ __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8nn200100IRPN2CA6Render13BackdropGroup4ItemES9_EEvOT_OT0_
+ __ZSt28__throw_bad_array_new_lengthB8nn200100v
+ __ZTVN2CA3OGL19SDFElementGroupNodeE
+ __ZTVN2CA3OGL21DisplacementMapFilterE
+ __ZTVN2CA3OGL21GlassBackgroundFilterE
+ __ZTVN2CA3OGL21GlassForegroundFilterE
+ __ZTVN2CA3OGL28ChromaticAberrationMapFilterE
+ __ZTVN2CA3OGL7SDFNodeE
+ __ZTVN2CA6Render11WindowLayerE
+ __ZTVN2CA6Render12HostingTokenE
+ __ZTVN2CA6Render12KeyPathValueE
+ __ZTVN2CA6Render15SDFElementLayerE
+ __ZTVN2CA6Render7Updater5SDFOpE
+ __ZTVN2CA6Render8SDFLayerE
+ __ZTVNSt3__110__function6__funcIZN2CA6Render14FlattenManager43flattened_cache_print_all_flattened_entriesEP15x_stream_structE3$_0NS_9allocatorIS7_EEFvjPNS3_19FlattenedCacheEntryEEEE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZThn1456_N2CA12WindowServer11AccelServer10test_fenceEm
+ __ZThn1456_N2CA12WindowServer11AccelServer12delete_fenceEm
+ __ZThn1456_N2CA12WindowServer11AccelServer15supports_fencesEv
+ __ZThn1456_N2CA12WindowServer11AccelServer20flush_command_streamEv
+ __ZThn1456_N2CA12WindowServer11AccelServer9set_fenceEv
+ __ZZ11get_cg_name16CAColorSpaceNameE20named_cg_colorspaces
+ __ZZ12x_log_get_cgE3log
+ __ZZ12x_log_get_cgE4once
+ __ZZ13x_log_get_apiE3log
+ __ZZ13x_log_get_apiE4once
+ __ZZ13x_log_get_oglE3log
+ __ZZ13x_log_get_oglE4once
+ __ZZ15x_log_get_colorE3log
+ __ZZ15x_log_get_colorE4once
+ __ZZ16x_log_get_renderE3log
+ __ZZ16x_log_get_renderE4once
+ __ZZ16x_log_get_statesE3log
+ __ZZ16x_log_get_statesE4once
+ __ZZ16x_log_get_zombievE3log
+ __ZZ16x_log_get_zombievE4once
+ __ZZ17x_log_get_CADebugE3log
+ __ZZ17x_log_get_CADebugE4once
+ __ZZ17x_log_get_flattenE3log
+ __ZZ17x_log_get_flattenE4once
+ __ZZ18x_log_get_flipbookE3log
+ __ZZ18x_log_get_flipbookE4once
+ __ZZ19CADeviceSupportsGCPE1b
+ __ZZ19CADeviceSupportsGCPE4once
+ __ZZ19x_log_get_filmgrainE3log
+ __ZZ19x_log_get_filmgrainE4once
+ __ZZ19x_log_get_ogl_metalE3log
+ __ZZ19x_log_get_ogl_metalE4once
+ __ZZ19x_log_get_utilitiesE3log
+ __ZZ19x_log_get_utilitiesE4once
+ __ZZ20mode_range_to_stringN2CA12WindowServer7Display10ColorRangeEE5names
+ __ZZ20x_log_get_brightnessE3log
+ __ZZ20x_log_get_brightnessE4once
+ __ZZ20x_log_get_frame_rateE3log
+ __ZZ20x_log_get_frame_rateE4once
+ __ZZ20x_log_get_ogl_openglE3log
+ __ZZ20x_log_get_ogl_openglE4once
+ __ZZ21x_log_get_sharedeventE3log
+ __ZZ21x_log_get_sharedeventE4once
+ __ZZ22CADeviceSupportsMedinaE8chip_ids
+ __ZZ22x_log_get_windowserverE3log
+ __ZZ22x_log_get_windowserverE4once
+ __ZZ23x_log_get_display_stateE3log
+ __ZZ23x_log_get_display_stateE4once
+ __ZZ25CADeviceSupportsPreLayoutE4once
+ __ZZ25CADeviceSupportsPreLayoutE7enabled
+ __ZZ27mode_pixel_format_to_stringN2CA12WindowServer7Display16ColorPixelFormatEE5names
+ __ZZ27x_log_get_secure_indicatorsE3log
+ __ZZ27x_log_get_secure_indicatorsE4once
+ __ZZ27x_log_get_security_analysisE3log
+ __ZZ27x_log_get_security_analysisE4once
+ __ZZ29CADeviceNeeds2kPlaneAlignmentE18needs_2k_alignment
+ __ZZ29CADeviceNeeds2kPlaneAlignmentE4once
+ __ZZ29CADeviceNeeds2kPlaneAlignmentE8chip_ids
+ __ZZ32+[CASDFFillEffect defaultValues]E4dict
+ __ZZ32+[CASDFFillEffect defaultValues]E4once
+ __ZZ34+[CASDFOutputEffect defaultValues]E4dict
+ __ZZ34+[CASDFOutputEffect defaultValues]E4once
+ __ZZ34+[CASDFShadowEffect defaultValues]E4dict
+ __ZZ34+[CASDFShadowEffect defaultValues]E4once
+ __ZZ34CADeviceSupportsWirelessNightShiftE4once
+ __ZZ34CADeviceSupportsWirelessNightShiftE7enabled
+ __ZZ35-[CASDFLayer didChangeValueForKey:]E5atoms
+ __ZZ36CADeviceAllowMetalFrameInterpolationE4once
+ __ZZ36CADeviceAllowMetalFrameInterpolationE7allowed
+ __ZZ38-[CAWindowLayer didChangeValueForKey:]E5atoms
+ __ZZ38CADeviceSupportsPreLayoutLinkedOnCheckE4once
+ __ZZ38CADeviceSupportsPreLayoutLinkedOnCheckE7enabled
+ __ZZ41+[CASDFVisualizationEffect defaultValues]E4dict
+ __ZZ41+[CASDFVisualizationEffect defaultValues]E4once
+ __ZZ42+[CASDFGlassHighlightEffect defaultValues]E4dict
+ __ZZ42+[CASDFGlassHighlightEffect defaultValues]E4once
+ __ZZ42-[CASDFElementLayer didChangeValueForKey:]E5atoms
+ __ZZ42-[CASDFLayer _renderLayerDefinesProperty:]E5atoms
+ __ZZ44+[CASDFKeyFillHighlightEffect defaultValues]E4dict
+ __ZZ44+[CASDFKeyFillHighlightEffect defaultValues]E4once
+ __ZZ45+[CASDFGlassDisplacementEffect defaultValues]E4dict
+ __ZZ45+[CASDFGlassDisplacementEffect defaultValues]E4once
+ __ZZ45-[CAWindowLayer _renderLayerDefinesProperty:]E5atoms
+ __ZZ49-[CASDFElementLayer _renderLayerDefinesProperty:]E5atoms
+ __ZZ52CADeviceNeedsDisplayStateControlDependencyWorkaroundE1b
+ __ZZ52CADeviceNeedsDisplayStateControlDependencyWorkaroundE4once
+ __ZZ62-[CALayer(CALayerPrivate) _renderLayerPropertyAnimationFlags:]E9edr_atoms
+ __ZZL15_next_encode_idvE17encode_count_lock
+ __ZZL15_next_encode_idvE17last_encode_count
+ __ZZL16defines_propertyjE5atoms.17542
+ __ZZL16defines_propertyjE5atoms.23672
+ __ZZN2CA12WindowServer12IOMFBDisplay13finish_updateEPNS_6Render6UpdateEjyENK3$_2clEv
+ __ZZN2CA12WindowServer12IOMFBDisplay13finish_updateEPNS_6Render6UpdateEjyENK3$_4clERNS_4RectE
+ __ZZN2CA12WindowServer12IOMFBDisplay25update_power_state_lockedEbENK3$_0clEv
+ __ZZN2CA12WindowServer12IOMFBDisplay27post_edr_requests_power_logEPKNS_6Render6UpdateEE25edr_requests_telemetry_id
+ __ZZN2CA12WindowServer12IOMFBDisplay27post_edr_requests_power_logEPKNS_6Render6UpdateEE4once
+ __ZZN2CA12WindowServerL21get_sil_telemetry_logEvE17sil_telemetry_log
+ __ZZN2CA12WindowServerL21get_sil_telemetry_logEvE4once
+ __ZZN2CA20HDRProcessorInternal30create_surface_with_forward_dmEPKNS_6Render7SurfaceEPNS1_6UpdateEPKNS1_17DisplayAttributesEbfNS1_12TextureFlagsEfbbbbENK3$_0clEPN1X4ListIPNS0_10HDRSurfaceEEESH_
+ __ZZN2CA3OGL15render_subclassERNS0_8RendererEPKNS0_5LayerEENK7visitor14visit_subclassEPKNS_6Render11WindowLayerE
+ __ZZN2CA3OGL15render_subclassERNS0_8RendererEPKNS0_5LayerEENK7visitor14visit_subclassEPKNS_6Render15SDFElementLayerE
+ __ZZN2CA3OGL15render_subclassERNS0_8RendererEPKNS0_5LayerEENK7visitor14visit_subclassEPKNS_6Render8SDFLayerE
+ __ZZN2CA3OGL17render_sdf_boundsERNS0_8RendererEPKNS0_5LayerENS_4Vec2IfEEfE7indices
+ __ZZN2CA3OGL18initialize_filtersEvE19displacement_filter
+ __ZZN2CA3OGL18initialize_filtersEvE23glass_background_filter
+ __ZZN2CA3OGL18initialize_filtersEvE23glass_foreground_filter
+ __ZZN2CA3OGL18initialize_filtersEvE31chromatic_aberration_map_filter
+ __ZZN2CA3OGL19prepare_layer_imageERNS0_8RendererEPNS0_5LayerERKNS0_6GstateEENK7visitor14visit_subclassEPKNS_6Render11WindowLayerE
+ __ZZN2CA3OGL19prepare_layer_imageERNS0_8RendererEPNS0_5LayerERKNS0_6GstateEENK7visitor14visit_subclassEPKNS_6Render15SDFElementLayerE
+ __ZZN2CA3OGL19prepare_layer_imageERNS0_8RendererEPNS0_5LayerERKNS0_6GstateEENK7visitor14visit_subclassEPKNS_6Render8SDFLayerE
+ __ZZN2CA3OGL8Renderer6renderEPKNS_6Render6UpdateEmPNS_13CASharedEventEE18last_seed_recorded
+ __ZZN2CA3OGL8Renderer6renderEPKNS_6Render6UpdateEmPNS_13CASharedEventEEN3$_08__invokeERNS_4RectEPv
+ __ZZN2CA3OGLL13ogl_trace_logEvE3log
+ __ZZN2CA3OGLL13ogl_trace_logEvE4once
+ __ZZN2CA6Render12_GLOBAL__N_123retain_provider_optionsEbE4once
+ __ZZN2CA6Render14FlattenManager29flatten_cache_max_memory_sizeEvE10max_memory
+ __ZZN2CA6Render14FlattenManager29flatten_cache_max_memory_sizeEvE4once
+ __ZZN2CA6Render16FlattenedSurfaceC1EPNS_3OGL7ContextENS_6BoundsEjjE4once
+ __ZZN2CA6Render22MatchPropertyAnimation17create_dependenceEPNS0_6HandleEENK3$_0clEPKPv
+ __ZZN2CA6Render6Server9is_deniedEvE4once
+ __ZZN2CA6Render6Server9is_deniedEvE6denied
+ __ZZN2CA6Render6Update20add_secure_indicatorENS1_15SecureIndicatorEE4once
+ __ZZN2CA6Render7Updater5SDFOp10map_boundsERNS1_11LayerShapesEbEN3$_08__invokeERNS_4RectEPv
+ __ZZN2CA7DisplayL20MaxEarlyWakeupOffsetEvE3ret
+ __ZZN2CA7DisplayL20MaxEarlyWakeupOffsetEvE7ret_apt
+ __ZZNK2CA3OGL18GaussianBlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfbPKNS_11ColorMatrixEPKNS_5ShapeESK_SE_SD_E10all_linear
+ __ZZNK2CA3OGL18GaussianBlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfbPKNS_11ColorMatrixEPKNS_5ShapeESK_SE_SD_E4once
+ __ZZNK2CA3OGL7Display19has_detached_layersEvEN3$_08__invokeEPNS_6Render6HandleElPNS3_7TextureEPv
+ __ZZNK2CA6Render12GainMapLayer4showEP15x_stream_structjjE10mode_names
+ __ZZNK2CA6Render5Layer4showEP15x_stream_structjjE5names
+ __ZZNK2CA6Render9Animation4showEP15x_stream_structjjE10calc_modes
+ __ZZZ20get_setters_for_typeIN2CA6Render5LayerEERKDavENKUlvE_clEvENUlP7CALayerPKS2_SA_RKNSt3__112basic_stringIcNSB_11char_traitsIcEENSB_9allocatorIcEEEERK25ReverseSerializationStateE122_8__invokeES8_SA_SA_SJ_SM_
+ __ZZZ20get_setters_for_typeIN2CA6Render5LayerEERKDavENKUlvE_clEvENUlP7CALayerPKS2_SA_RKNSt3__112basic_stringIcNSB_11char_traitsIcEENSB_9allocatorIcEEEERK25ReverseSerializationStateE123_8__invokeES8_SA_SA_SJ_SM_
+ __ZZZ20get_setters_for_typeIN2CA6Render5LayerEERKDavENKUlvE_clEvENUlP7CALayerPKS2_SA_RKNSt3__112basic_stringIcNSB_11char_traitsIcEENSB_9allocatorIcEEEERK25ReverseSerializationStateE124_8__invokeES8_SA_SA_SJ_SM_
+ ___32+[CASDFFillEffect defaultValues]_block_invoke
+ ___34+[CASDFOutputEffect defaultValues]_block_invoke
+ ___34+[CASDFShadowEffect defaultValues]_block_invoke
+ ___39-[CAContentStream updateOptions:error:]_block_invoke
+ ___40-[CAContext addFence:completionHandler:]_block_invoke
+ ___41+[CASDFVisualizationEffect defaultValues]_block_invoke
+ ___42+[CASDFGlassHighlightEffect defaultValues]_block_invoke
+ ___44+[CASDFKeyFillHighlightEffect defaultValues]_block_invoke
+ ___45+[CASDFGlassDisplacementEffect defaultValues]_block_invoke
+ ___51-[CAFlipBook renderForTime:options:userInfo:error:]_block_invoke
+ ___Block_byref_object_copy_.13511
+ ___Block_byref_object_copy_.14819
+ ___Block_byref_object_copy_.21196
+ ___Block_byref_object_copy_.373
+ ___Block_byref_object_copy_.376
+ ___Block_byref_object_dispose_.13512
+ ___Block_byref_object_dispose_.14820
+ ___Block_byref_object_dispose_.21197
+ ___Block_byref_object_dispose_.374
+ ___Block_byref_object_dispose_.377
+ ___CADeviceAllowMetalFrameInterpolation_block_invoke
+ ___CADeviceNeeds2kPlaneAlignment_block_invoke
+ ___CADeviceNeedsDisplayStateControlDependencyWorkaround_block_invoke
+ ___CADeviceSupportsGCP_block_invoke
+ ___CADeviceSupportsPreLayoutLinkedOnCheck_block_invoke
+ ___CADeviceSupportsPreLayout_block_invoke
+ ___CADeviceSupportsWirelessNightShift_block_invoke
+ ___NSDictionary0__struct
+ ____Z16x_log_get_zombiev_block_invoke
+ ____Z37CADisplaySupportedHDRModeWithCriteriaRKN2CA12WindowServer7Display7ModeSetERKNS1_14EDIDAttributesEbb_block_invoke
+ ____ZL13emit_tailspinP8NSStringjjijPKc_block_invoke.84
+ ____ZL15ensure_displaysv_block_invoke.942
+ ____ZN2CA11Transaction9add_fenceEjP13CAFenceHandleU13block_pointerFvP17CAFenceResolutionE_block_invoke
+ ____ZN2CA12ColorProgram7Program13color_programEPK21CGColorConversionInfoP12CGColorSpacei28CGColorConversionIterateTypebijfffffRb_block_invoke
+ ____ZN2CA12ColorProgram7Program13color_programEPK21CGColorConversionInfoP12CGColorSpacei28CGColorConversionIterateTypebijfffffRb_block_invoke.27
+ ____ZN2CA12ColorProgram7Program13color_programEPK21CGColorConversionInfoP12CGColorSpacei28CGColorConversionIterateTypebijfffffRb_block_invoke.30
+ ____ZN2CA12ColorProgram7Program13color_programEPK21CGColorConversionInfoP12CGColorSpacei28CGColorConversionIterateTypebijfffffRb_block_invoke_2
+ ____ZN2CA12WindowServer11IOMFBServer20try_swap_begin_asyncEj_block_invoke
+ ____ZN2CA12WindowServer11IOMFBServer21set_calibration_phaseEjjj_block_invoke
+ ____ZN2CA12WindowServer12IOMFBDisplay21set_tonemapping_stateEPNS_6Render6UpdateEPKNS0_7SurfaceEjPP12CGColorSpace_block_invoke.50
+ ____ZN2CA12WindowServer12IOMFBDisplay27post_edr_requests_power_logEPKNS_6Render6UpdateE_block_invoke
+ ____ZN2CA12WindowServer15DebugBrightnessEd_block_invoke.224
+ ____ZN2CA12WindowServer6Server29schedule_forced_render_updateENS_6Render12UpdateReasonE_block_invoke
+ ____ZN2CA12WindowServer6ServerC2EPNS0_7DisplayEPK10__CFString_block_invoke.17
+ ____ZN2CA12WindowServerL21get_sil_telemetry_logEv_block_invoke
+ ____ZN2CA20HDRProcessorInternal30configure_display_pipe_tonemapEP11__IOSurfacejPKNS_6Render17DisplayAttributesEfPP12CGColorSpaceU13block_pointerFvP18IOMFBToneMapConfigEU13block_pointerFv13IOMFBCurveLocPK14IOMFBCurveDataEU13block_pointerFv14IOMFBICCMatLocPK16IOMFBColorMatrixE_block_invoke
+ ____ZN2CA20HDRProcessorInternal30create_surface_with_forward_dmEPKNS_6Render7SurfaceEPNS1_6UpdateEPKNS1_17DisplayAttributesEbfNS1_12TextureFlagsEfbbbb_block_invoke
+ ____ZN2CA3OGL12MetalContext22calculate_average_lumaEPNS0_7SurfaceERNS_6BoundsEU13block_pointerFvfE_block_invoke
+ ____ZN2CA3OGL12MetalContext30compute_calculate_average_lumaEPNS0_7SurfaceERNS_6BoundsEU13block_pointerFvfE_block_invoke
+ ____ZN2CA3OGL12MetalContext5flushEb_block_invoke.63
+ ____ZN2CA3OGL12MetalContext5flushEb_block_invoke.65
+ ____ZN2CA3OGLL13ogl_trace_logEv_block_invoke
+ ____ZN2CA6Render12_GLOBAL__N_123retain_provider_optionsEb_block_invoke
+ ____ZN2CA6Render14FlattenManager29flatten_cache_max_memory_sizeEv_block_invoke
+ ____ZN2CA6Render16FlattenedSurfaceC2EPNS_3OGL7ContextENS_6BoundsEjj_block_invoke
+ ____ZN2CA6Render5Fence11Transaction8Observer8activateENSt3__113unordered_setIyNS4_4hashIyEENS4_8equal_toIyEENS4_9allocatorIyEEEEPFvPS3_RKSC_djyEPFvSD_SF_jjEPFvSD_SF_E_block_invoke.6
+ ____ZN2CA6Render5Fence11Transaction8Observer8activateENSt3__113unordered_setIyNS4_4hashIyEENS4_8equal_toIyEENS4_9allocatorIyEEEEPFvPS3_RKSC_djyEPFvSD_SF_jjEPFvSD_SF_E_block_invoke.9
+ ____ZN2CA6Render6Server9is_deniedEv_block_invoke
+ ____ZN2CA6Render6Update20add_secure_indicatorENS1_15SecureIndicatorE_block_invoke
+ ____ZN2CA7Context18commit_transactionEPNS_11TransactionEdPd_block_invoke.14
+ ____ZN2CA7Context18commit_transactionEPNS_11TransactionEdPd_block_invoke.16
+ ____ZN2CA7Context18commit_transactionEPNS_11TransactionEdPd_block_invoke_2.19
+ ____ZN2CA7Display15DisplayLinkItem8get_linkEP11__CFRunLoopPKN1X4ListIPK10__CFStringEE_block_invoke
+ ____ZNK2CA3OGL18GaussianBlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPPNS0_7SurfaceEPfbPKNS_11ColorMatrixEPKNS_5ShapeESK_SE_SD__block_invoke
+ ___block_descriptor_168_e8_32o40b_e5_v8?0ls32l8s40l8
+ ___block_descriptor_32_e120_B24?0"CALocalDisplay"8^{?=III^{__CFString}^{__CFString}^{__CFString}^QQQQ^?dddIIB^{__CFArray}^{__CFData}^{__CFData}}16l
+ ___block_descriptor_40_e5_Q8?0l
+ ___block_descriptor_40_e8_32b_e27_v16?0"CAFenceResolution"8ls32l8
+ ___block_descriptor_40_e8_32o_e32_v16?0r^{?=IIQQQQIBBBfffQIBQQf}8ls32l8
+ ___block_descriptor_40_e8_32o_e65_v112?0I8I12Q16Q24Q32Q40I48B52B56B60f64f68f72Q76I84B88Q92Q100f108ls32l8
+ ___block_descriptor_48_e8_32b_e101_B16?0^{?=III^{__CFString}^{__CFString}^{__CFString}^QQQQ^?dddIIB^{__CFArray}^{__CFData}^{__CFData}}8ls32l8
+ ___block_descriptor_50_e21_B24?0"NSString"816l
+ ___block_descriptor_56_e8_32o40b_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32o40r48r_e37_v24?0"CAFlipBookFrame"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_85_e5_v8?0l
+ ___block_descriptor_tmp.1.17404
+ ___block_descriptor_tmp.1.18561
+ ___block_descriptor_tmp.1.20554
+ ___block_descriptor_tmp.100
+ ___block_descriptor_tmp.10119
+ ___block_descriptor_tmp.10199
+ ___block_descriptor_tmp.102.14942
+ ___block_descriptor_tmp.104
+ ___block_descriptor_tmp.108.15052
+ ___block_descriptor_tmp.11.17684
+ ___block_descriptor_tmp.11.1780
+ ___block_descriptor_tmp.11.18575
+ ___block_descriptor_tmp.11.2116
+ ___block_descriptor_tmp.11.24014
+ ___block_descriptor_tmp.1128
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.11475
+ ___block_descriptor_tmp.12.23103
+ ___block_descriptor_tmp.12009
+ ___block_descriptor_tmp.121
+ ___block_descriptor_tmp.12365
+ ___block_descriptor_tmp.13927
+ ___block_descriptor_tmp.14040
+ ___block_descriptor_tmp.142
+ ___block_descriptor_tmp.14287
+ ___block_descriptor_tmp.144
+ ___block_descriptor_tmp.148
+ ___block_descriptor_tmp.15.12381
+ ___block_descriptor_tmp.15.2118
+ ___block_descriptor_tmp.15069
+ ___block_descriptor_tmp.154
+ ___block_descriptor_tmp.157
+ ___block_descriptor_tmp.16182
+ ___block_descriptor_tmp.163
+ ___block_descriptor_tmp.163.12527
+ ___block_descriptor_tmp.169
+ ___block_descriptor_tmp.169.17266
+ ___block_descriptor_tmp.170
+ ___block_descriptor_tmp.17166
+ ___block_descriptor_tmp.17403
+ ___block_descriptor_tmp.17716
+ ___block_descriptor_tmp.1783
+ ___block_descriptor_tmp.18
+ ___block_descriptor_tmp.18.21207
+ ___block_descriptor_tmp.18.23139
+ ___block_descriptor_tmp.180
+ ___block_descriptor_tmp.180.17071
+ ___block_descriptor_tmp.18362
+ ___block_descriptor_tmp.18514
+ ___block_descriptor_tmp.18553
+ ___block_descriptor_tmp.18643
+ ___block_descriptor_tmp.18890
+ ___block_descriptor_tmp.194
+ ___block_descriptor_tmp.197
+ ___block_descriptor_tmp.19990
+ ___block_descriptor_tmp.2.5299
+ ___block_descriptor_tmp.2.6094
+ ___block_descriptor_tmp.20
+ ___block_descriptor_tmp.203
+ ___block_descriptor_tmp.20553
+ ___block_descriptor_tmp.209
+ ___block_descriptor_tmp.2105
+ ___block_descriptor_tmp.21199
+ ___block_descriptor_tmp.21262
+ ___block_descriptor_tmp.219
+ ___block_descriptor_tmp.22
+ ___block_descriptor_tmp.22592
+ ___block_descriptor_tmp.23.12397
+ ___block_descriptor_tmp.23099
+ ___block_descriptor_tmp.231
+ ___block_descriptor_tmp.24000
+ ___block_descriptor_tmp.247
+ ___block_descriptor_tmp.25
+ ___block_descriptor_tmp.2567
+ ___block_descriptor_tmp.27
+ ___block_descriptor_tmp.27.16972
+ ___block_descriptor_tmp.280
+ ___block_descriptor_tmp.286
+ ___block_descriptor_tmp.289
+ ___block_descriptor_tmp.29
+ ___block_descriptor_tmp.29.12404
+ ___block_descriptor_tmp.2909
+ ___block_descriptor_tmp.295
+ ___block_descriptor_tmp.3.17721
+ ___block_descriptor_tmp.3.18518
+ ___block_descriptor_tmp.3.2109
+ ___block_descriptor_tmp.3.460
+ ___block_descriptor_tmp.3.9258
+ ___block_descriptor_tmp.301
+ ___block_descriptor_tmp.307
+ ___block_descriptor_tmp.31
+ ___block_descriptor_tmp.31.14166
+ ___block_descriptor_tmp.313
+ ___block_descriptor_tmp.32
+ ___block_descriptor_tmp.322
+ ___block_descriptor_tmp.331
+ ___block_descriptor_tmp.345
+ ___block_descriptor_tmp.3559
+ ___block_descriptor_tmp.358
+ ___block_descriptor_tmp.359
+ ___block_descriptor_tmp.36
+ ___block_descriptor_tmp.3724
+ ___block_descriptor_tmp.376
+ ___block_descriptor_tmp.380
+ ___block_descriptor_tmp.386
+ ___block_descriptor_tmp.387
+ ___block_descriptor_tmp.39
+ ___block_descriptor_tmp.39.20605
+ ___block_descriptor_tmp.393
+ ___block_descriptor_tmp.398
+ ___block_descriptor_tmp.4.10128
+ ___block_descriptor_tmp.4.18524
+ ___block_descriptor_tmp.4.18564
+ ___block_descriptor_tmp.403
+ ___block_descriptor_tmp.408
+ ___block_descriptor_tmp.409
+ ___block_descriptor_tmp.412
+ ___block_descriptor_tmp.419
+ ___block_descriptor_tmp.423
+ ___block_descriptor_tmp.424
+ ___block_descriptor_tmp.427
+ ___block_descriptor_tmp.43
+ ___block_descriptor_tmp.43.12071
+ ___block_descriptor_tmp.43.2930
+ ___block_descriptor_tmp.4457
+ ___block_descriptor_tmp.45
+ ___block_descriptor_tmp.45.22044
+ ___block_descriptor_tmp.450
+ ___block_descriptor_tmp.454
+ ___block_descriptor_tmp.458
+ ___block_descriptor_tmp.47
+ ___block_descriptor_tmp.47.22039
+ ___block_descriptor_tmp.473
+ ___block_descriptor_tmp.49
+ ___block_descriptor_tmp.499
+ ___block_descriptor_tmp.51
+ ___block_descriptor_tmp.51.12430
+ ___block_descriptor_tmp.5159
+ ___block_descriptor_tmp.52
+ ___block_descriptor_tmp.528
+ ___block_descriptor_tmp.5302
+ ___block_descriptor_tmp.541
+ ___block_descriptor_tmp.543
+ ___block_descriptor_tmp.546
+ ___block_descriptor_tmp.55
+ ___block_descriptor_tmp.560
+ ___block_descriptor_tmp.5610
+ ___block_descriptor_tmp.5899
+ ___block_descriptor_tmp.5977
+ ___block_descriptor_tmp.6074
+ ___block_descriptor_tmp.6098
+ ___block_descriptor_tmp.61.12442
+ ___block_descriptor_tmp.6200
+ ___block_descriptor_tmp.6313
+ ___block_descriptor_tmp.64
+ ___block_descriptor_tmp.6761
+ ___block_descriptor_tmp.68
+ ___block_descriptor_tmp.6923
+ ___block_descriptor_tmp.7.10210
+ ___block_descriptor_tmp.7.18527
+ ___block_descriptor_tmp.7.18557
+ ___block_descriptor_tmp.70
+ ___block_descriptor_tmp.71.17140
+ ___block_descriptor_tmp.74.22525
+ ___block_descriptor_tmp.7419
+ ___block_descriptor_tmp.75.2150
+ ___block_descriptor_tmp.76
+ ___block_descriptor_tmp.7688
+ ___block_descriptor_tmp.78.17184
+ ___block_descriptor_tmp.79
+ ___block_descriptor_tmp.79.17183
+ ___block_descriptor_tmp.79.17641
+ ___block_descriptor_tmp.7941
+ ___block_descriptor_tmp.8.1121
+ ___block_descriptor_tmp.8.1791
+ ___block_descriptor_tmp.8.21201
+ ___block_descriptor_tmp.80
+ ___block_descriptor_tmp.83.3537
+ ___block_descriptor_tmp.8752
+ ___block_descriptor_tmp.89
+ ___block_descriptor_tmp.8959
+ ___block_descriptor_tmp.9.18537
+ ___block_descriptor_tmp.90
+ ___block_descriptor_tmp.90.17823
+ ___block_descriptor_tmp.91
+ ___block_descriptor_tmp.9254
+ ___block_descriptor_tmp.93.17644
+ ___block_descriptor_tmp.983
+ ___block_literal_global.10
+ ___block_literal_global.10.1119
+ ___block_literal_global.10117
+ ___block_literal_global.10175
+ ___block_literal_global.10195
+ ___block_literal_global.104.19903
+ ___block_literal_global.1047
+ ___block_literal_global.10696
+ ___block_literal_global.107
+ ___block_literal_global.1126
+ ___block_literal_global.11351
+ ___block_literal_global.116
+ ___block_literal_global.12069
+ ___block_literal_global.123
+ ___block_literal_global.12363
+ ___block_literal_global.13.18573
+ ___block_literal_global.13.2114
+ ___block_literal_global.131
+ ___block_literal_global.13589
+ ___block_literal_global.137
+ ___block_literal_global.13925
+ ___block_literal_global.14.23101
+ ___block_literal_global.14038
+ ___block_literal_global.144
+ ___block_literal_global.15
+ ___block_literal_global.150
+ ___block_literal_global.15067
+ ___block_literal_global.156
+ ___block_literal_global.15889
+ ___block_literal_global.159
+ ___block_literal_global.16211
+ ___block_literal_global.165
+ ___block_literal_global.165.12525
+ ___block_literal_global.17.12379
+ ___block_literal_global.171
+ ___block_literal_global.17264
+ ___block_literal_global.17714
+ ___block_literal_global.1779
+ ___block_literal_global.182
+ ___block_literal_global.18360
+ ___block_literal_global.18478
+ ___block_literal_global.18551
+ ___block_literal_global.18641
+ ___block_literal_global.18743
+ ___block_literal_global.18882
+ ___block_literal_global.19135
+ ___block_literal_global.192
+ ___block_literal_global.196
+ ___block_literal_global.199
+ ___block_literal_global.19917
+ ___block_literal_global.20476
+ ___block_literal_global.205
+ ___block_literal_global.20603
+ ___block_literal_global.21.6937
+ ___block_literal_global.2103
+ ___block_literal_global.211
+ ___block_literal_global.21198
+ ___block_literal_global.21254
+ ___block_literal_global.22038
+ ___block_literal_global.221
+ ___block_literal_global.229
+ ___block_literal_global.23078
+ ___block_literal_global.23093
+ ___block_literal_global.233
+ ___block_literal_global.23835
+ ___block_literal_global.23935
+ ___block_literal_global.240
+ ___block_literal_global.24012
+ ___block_literal_global.241
+ ___block_literal_global.24227
+ ___block_literal_global.249
+ ___block_literal_global.249.12574
+ ___block_literal_global.25
+ ___block_literal_global.25.12395
+ ___block_literal_global.2565
+ ___block_literal_global.271
+ ___block_literal_global.282
+ ___block_literal_global.288
+ ___block_literal_global.29
+ ___block_literal_global.2907
+ ___block_literal_global.291
+ ___block_literal_global.293
+ ___block_literal_global.295
+ ___block_literal_global.297
+ ___block_literal_global.299
+ ___block_literal_global.303
+ ___block_literal_global.303.19771
+ ___block_literal_global.31
+ ___block_literal_global.315
+ ___block_literal_global.324
+ ___block_literal_global.33
+ ___block_literal_global.33.14162
+ ___block_literal_global.3328
+ ___block_literal_global.333
+ ___block_literal_global.337
+ ___block_literal_global.347
+ ___block_literal_global.355
+ ___block_literal_global.3557
+ ___block_literal_global.3719
+ ___block_literal_global.378
+ ___block_literal_global.38
+ ___block_literal_global.382
+ ___block_literal_global.388
+ ___block_literal_global.389
+ ___block_literal_global.395
+ ___block_literal_global.4
+ ___block_literal_global.40
+ ___block_literal_global.400
+ ___block_literal_global.405
+ ___block_literal_global.41
+ ___block_literal_global.410
+ ___block_literal_global.411
+ ___block_literal_global.414
+ ___block_literal_global.420
+ ___block_literal_global.421
+ ___block_literal_global.4211
+ ___block_literal_global.425
+ ___block_literal_global.426
+ ___block_literal_global.429
+ ___block_literal_global.44
+ ___block_literal_global.44.8549
+ ___block_literal_global.4441
+ ___block_literal_global.45.2926
+ ___block_literal_global.452
+ ___block_literal_global.456
+ ___block_literal_global.461
+ ___block_literal_global.464
+ ___block_literal_global.47
+ ___block_literal_global.471
+ ___block_literal_global.49
+ ___block_literal_global.5.17719
+ ___block_literal_global.5.9251
+ ___block_literal_global.501
+ ___block_literal_global.503
+ ___block_literal_global.504
+ ___block_literal_global.507
+ ___block_literal_global.511
+ ___block_literal_global.513
+ ___block_literal_global.515
+ ___block_literal_global.5157
+ ___block_literal_global.5298
+ ___block_literal_global.53
+ ___block_literal_global.53.12428
+ ___block_literal_global.5581
+ ___block_literal_global.5608
+ ___block_literal_global.5624
+ ___block_literal_global.5681
+ ___block_literal_global.57
+ ___block_literal_global.5896
+ ___block_literal_global.5972
+ ___block_literal_global.60
+ ___block_literal_global.6072
+ ___block_literal_global.6096
+ ___block_literal_global.6198
+ ___block_literal_global.63
+ ___block_literal_global.63.12440
+ ___block_literal_global.6311
+ ___block_literal_global.66
+ ___block_literal_global.67
+ ___block_literal_global.6759
+ ___block_literal_global.6940
+ ___block_literal_global.70
+ ___block_literal_global.7414
+ ___block_literal_global.7686
+ ___block_literal_global.77.2148
+ ___block_literal_global.78
+ ___block_literal_global.7934
+ ___block_literal_global.81
+ ___block_literal_global.826
+ ___block_literal_global.85.3535
+ ___block_literal_global.8563
+ ___block_literal_global.8749
+ ___block_literal_global.88
+ ___block_literal_global.89.18764
+ ___block_literal_global.89.4206
+ ___block_literal_global.8957
+ ___block_literal_global.9.10208
+ ___block_literal_global.9.18555
+ ___block_literal_global.913
+ ___block_literal_global.920
+ ___block_literal_global.923
+ ___block_literal_global.9252
+ ___block_literal_global.94
+ ___block_literal_global.940
+ ___block_literal_global.944
+ ___block_literal_global.95.12465
+ ___block_literal_global.958
+ ___block_literal_global.961
+ ___block_literal_global.981
+ ___x_log_get_CADebug_block_invoke
+ ___x_log_get_api_block_invoke
+ ___x_log_get_brightness_block_invoke
+ ___x_log_get_cg_block_invoke
+ ___x_log_get_color_block_invoke
+ ___x_log_get_display_state_block_invoke
+ ___x_log_get_filmgrain_block_invoke
+ ___x_log_get_flatten_block_invoke
+ ___x_log_get_flipbook_block_invoke
+ ___x_log_get_frame_rate_block_invoke
+ ___x_log_get_ogl_block_invoke
+ ___x_log_get_ogl_metal_block_invoke
+ ___x_log_get_ogl_opengl_block_invoke
+ ___x_log_get_render_block_invoke
+ ___x_log_get_secure_indicators_block_invoke
+ ___x_log_get_security_analysis_block_invoke
+ ___x_log_get_sharedevent_block_invoke
+ ___x_log_get_states_block_invoke
+ ___x_log_get_utilities_block_invoke
+ ___x_log_get_windowserver_block_invoke
+ __kHDRProcessingGCPGammaValueKey
+ __kHDRProcessingHDRConstraintStrengthKey
+ __kHDRProcessingScreenCaptureSessionKey
+ __os_log_debug_impl
+ __os_log_fault_impl
+ __xpc_type_data
+ _flipbook
+ _kCABrightnessSyncNotificationHotplugState
+ _kCAContentsFormatAutomaticSPI
+ _kCAFilterChromaticAberrationMap
+ _kCAFilterDisplacementMap
+ _kCAFilterGlassBackground
+ _kCAFilterGlassForeground
+ _kCAFilterInputAberrationAmount
+ _kCAFilterInputAberrationAngle
+ _kCAFilterInputAberrationHeight
+ _kCAFilterInputAberrationOffset
+ _kCAFilterInputAdaptive
+ _kCAFilterInputBackdropAware
+ _kCAFilterInputBleedAmount
+ _kCAFilterInputBleedBlurRadius
+ _kCAFilterInputBleedColorMatrixBlack
+ _kCAFilterInputBleedColorMatrixFillColor
+ _kCAFilterInputBleedColorMatrixSaturation
+ _kCAFilterInputBleedColorMatrixWhite
+ _kCAFilterInputBleedDarkenBlend
+ _kCAFilterInputBleedDistance0
+ _kCAFilterInputBleedDistance1
+ _kCAFilterInputBleedHeight
+ _kCAFilterInputBleedOffset
+ _kCAFilterInputBleedOpacity
+ _kCAFilterInputBleedSaturation
+ _kCAFilterInputBlurDistance0
+ _kCAFilterInputBlurDistance1
+ _kCAFilterInputBlurDistance2
+ _kCAFilterInputBlurDistance3
+ _kCAFilterInputBlurDistance4
+ _kCAFilterInputBlurOpacity0
+ _kCAFilterInputBlurOpacity1
+ _kCAFilterInputBlurOpacity2
+ _kCAFilterInputBlurOpacity3
+ _kCAFilterInputBlurOpacity4
+ _kCAFilterInputBlurRadius
+ _kCAFilterInputEdgeEnd
+ _kCAFilterInputEdgeOpacityEnd
+ _kCAFilterInputEdgeOpacityStart
+ _kCAFilterInputEdgeStart
+ _kCAFilterInputFaceColorMatrixBlack
+ _kCAFilterInputFaceColorMatrixFillColor
+ _kCAFilterInputFaceColorMatrixSaturation
+ _kCAFilterInputFaceColorMatrixWhite
+ _kCAFilterInputFaceOpacity
+ _kCAFilterInputFade
+ _kCAFilterInputInnerRefractionAmount
+ _kCAFilterInputInnerRefractionHeight
+ _kCAFilterInputMaskImage
+ _kCAFilterInputMaxHeadroom
+ _kCAFilterInputOffset
+ _kCAFilterInputOuterRefractionAmount
+ _kCAFilterInputOuterRefractionHeight
+ _kCAFilterInputRefractionAmount
+ _kCAFilterInputRefractionDistance0
+ _kCAFilterInputRefractionDistance1
+ _kCAFilterInputRefractionHeight
+ _kCAFilterInputRefractionOffset
+ _kCAFilterInputRefractionOpacity
+ _kCAFilterInputSDRGradientDistance0
+ _kCAFilterInputSDRGradientDistance1
+ _kCAFilterInputSDRHoldingToneEnabled
+ _kCAFilterInputSDRShadowOpacity
+ _kCAFilterInputShadowAmount
+ _kCAFilterInputShadowBlurRadius
+ _kCAFilterInputShadowColorMatrixBlack
+ _kCAFilterInputShadowColorMatrixFillColor
+ _kCAFilterInputShadowColorMatrixSaturation
+ _kCAFilterInputShadowColorMatrixWhite
+ _kCAFilterInputShadowDistanceOffset
+ _kCAFilterInputShadowHeight
+ _kCAFilterInputShadowOffset
+ _kCAFilterInputShadowOpacity
+ _kCAFilterInputShadowRadius
+ _kCAFilterInputShadowVibrancyContribution
+ _kCAFilterInputSourceSublayerName
+ _kCAFilterPlusDIgnoreAlpha
+ _kCAFilterPlusLIgnoreAlpha
+ _kCAFilterSubtractSIgnoreAlpha
+ _kCAFlipBookMaximumPoolMemory
+ _kCAFlipBookOverAllocationFactor
+ _kCALayerHostZombificationModeAlways
+ _kCALayerHostZombificationModeDefault
+ _kCALayerHostZombificationModeNever
+ _kCASDFElementLayerModeBounds
+ _kCASDFElementLayerModeContents
+ _kCASDFElementLayerOperationSubtraction
+ _kCASDFElementLayerOperationUnion
+ _kCASnapshotCaptureMode
+ _kCASnapshotCaptureModeCanonicalHDR
+ _kCASnapshotCaptureModeCurrentHDR
+ _kCASnapshotCaptureModeSDR
+ _kCASnapshotDestinationEDR
+ _kCASnapshotDestinationSDR
+ _kCAWindowLayerFlattenModeAlways
+ _kCAWindowLayerFlattenModeDefault
+ _kCAWindowLayerFlattenModeNever
+ _kCAWindowServerGlobalLightAngle
+ _kCAWindowServerGlobalLightHeight
+ _kCAWindowServerGlobalLightOpacity
+ _kCAWindowServerGlobalLightSpread
+ _kCGApplyFlexLumaScaling
+ _kCGColorBlack
+ _kCGColorSpaceExtendedDisplayP3
+ _kCGColorSpaceExtendedITUR_2020
+ _kCGColorWhite
+ _kCGContentEDRStrength
+ _kCGFlexGTCTargetHeadroom
+ _kCGRWTMVersion
+ _objc_msgSend$CA_copyRenderKeyPathValueArray
+ _objc_msgSend$_availableModesInternal
+ _objc_msgSend$_copyStateInfo
+ _objc_msgSend$_notifyRenderBegin
+ _objc_msgSend$_notifyRenderCompletedForTime:status:frameId:oldestFrameId:apl:aplDimming:memoryUsage:rawSurfacePort:rawSurfaceDestRect:
+ _objc_msgSend$_performPreLayoutUpdate
+ _objc_msgSend$_resetConfiguration
+ _objc_msgSend$_unionConfigurationForEffect:
+ _objc_msgSend$addAllocation:
+ _objc_msgSend$allocatedSize
+ _objc_msgSend$allowsColorMatching
+ _objc_msgSend$allowsCornerContentsEdgeEffects
+ _objc_msgSend$allowsFilteredLuma
+ _objc_msgSend$amount
+ _objc_msgSend$angle
+ _objc_msgSend$cloningState
+ _objc_msgSend$configureLayer:transaction:
+ _objc_msgSend$contentsCDRStrength
+ _objc_msgSend$contentsHeadroom
+ _objc_msgSend$contentsOneValueDistance
+ _objc_msgSend$contentsZeroValueDistance
+ _objc_msgSend$contrastPreservationBegin
+ _objc_msgSend$contrastPreservationEnd
+ _objc_msgSend$curvature
+ _objc_msgSend$defaultValues
+ _objc_msgSend$disableFrameDoubling
+ _objc_msgSend$disablesUpdates
+ _objc_msgSend$displayCloningStateDidChange:seed:result:
+ _objc_msgSend$displayStateDidChange:seed:result:
+ _objc_msgSend$distances
+ _objc_msgSend$effect
+ _objc_msgSend$effectOffset
+ _objc_msgSend$event
+ _objc_msgSend$eventPort
+ _objc_msgSend$eventPortAtIndex:
+ _objc_msgSend$fillAmount
+ _objc_msgSend$fillAngle
+ _objc_msgSend$fillHeight
+ _objc_msgSend$fillHeightOffset
+ _objc_msgSend$fillHeightScale
+ _objc_msgSend$fillSpread
+ _objc_msgSend$fillSpreadOffset
+ _objc_msgSend$fillSpreadScale
+ _objc_msgSend$flattenMode
+ _objc_msgSend$fullyOccluded
+ _objc_msgSend$global
+ _objc_msgSend$gradientOvalization
+ _objc_msgSend$gradientSmoothing
+ _objc_msgSend$hitTestsAsFill
+ _objc_msgSend$hostingToken
+ _objc_msgSend$ignoreAnimations
+ _objc_msgSend$includeGradient
+ _objc_msgSend$initWithBytes:length:
+ _objc_msgSend$initWithPerceptualDuration:bounce:
+ _objc_msgSend$initWithSharedEvent:waitValue:isWrite:
+ _objc_msgSend$invert
+ _objc_msgSend$isWrite
+ _objc_msgSend$keyAmount
+ _objc_msgSend$keyAngle
+ _objc_msgSend$keyColor
+ _objc_msgSend$keyHeight
+ _objc_msgSend$keyHeightOffset
+ _objc_msgSend$keyHeightScale
+ _objc_msgSend$keySpread
+ _objc_msgSend$keySpreadOffset
+ _objc_msgSend$keySpreadScale
+ _objc_msgSend$lumaSubrect
+ _objc_msgSend$lumaUpdateRate
+ _objc_msgSend$maskOffset
+ _objc_msgSend$maximum
+ _objc_msgSend$maximumDistance
+ _objc_msgSend$mergeElements
+ _objc_msgSend$minimum
+ _objc_msgSend$newComputePipelineStateWithDescriptor:error:
+ _objc_msgSend$newResidencySetWithDescriptor:error:
+ _objc_msgSend$newSharedEventWithMachPort:
+ _objc_msgSend$newTextureViewWithPixelFormat:textureType:levels:slices:
+ _objc_msgSend$oneValueDistance
+ _objc_msgSend$operation
+ _objc_msgSend$outputBitDepth
+ _objc_msgSend$padding
+ _objc_msgSend$postCommitDuration
+ _objc_msgSend$preferredDynamicRange
+ _objc_msgSend$punchout
+ _objc_msgSend$radius
+ _objc_msgSend$rasterizeInParentSpace
+ _objc_msgSend$remapAnimation:forKey:
+ _objc_msgSend$removeAllocation:
+ _objc_msgSend$renderForTime:options:userInfo:onRenderBegin:onRenderComplete:
+ _objc_msgSend$request
+ _objc_msgSend$setCompressionType:
+ _objc_msgSend$setComputeFunction:
+ _objc_msgSend$setContentsCDRStrength:
+ _objc_msgSend$setContentsEDRStrength:
+ _objc_msgSend$setContrastPreservation:
+ _objc_msgSend$setContrastPreservationBegin:
+ _objc_msgSend$setContrastPreservationEnd:
+ _objc_msgSend$setEffect:
+ _objc_msgSend$setHostingToken:
+ _objc_msgSend$setImageblockWidth:height:
+ _objc_msgSend$setInitialCapacity:
+ _objc_msgSend$setMaximumPoolMemory:
+ _objc_msgSend$setOverAllocationFactor:
+ _objc_msgSend$setPreferredDynamicRange:
+ _objc_msgSend$setResponsibleProcess:
+ _objc_msgSend$setUpdateBeginTime:
+ _objc_msgSend$shadowEffectsOnWindowMaskOnly
+ _objc_msgSend$signalEvent:value:
+ _objc_msgSend$skipHitTesting
+ _objc_msgSend$smoothness
+ _objc_msgSend$sourceLayerOpacityScale
+ _objc_msgSend$spread
+ _objc_msgSend$supportedHDRModesWithCriteria:
+ _objc_msgSend$supportsLossyCompression
+ _objc_msgSend$targetCloningState
+ _objc_msgSend$textureType
+ _objc_msgSend$trackedLayerIDContent
+ _objc_msgSend$transactionAtIndex:
+ _objc_msgSend$waitForEvent:value:
+ _objc_msgSend$waitValue
+ _objc_msgSend$zeroValueDistance
+ _objc_msgSend$zombificationMode
+ _objc_release_x2
+ _objc_release_x28
+ _objc_retain_x2
+ _os_release
+ _os_unfair_lock_trylock_with_options
+ _os_workgroup_attr_set_interval_type
+ _os_workgroup_interval_create_with_workload_id
+ _os_workgroup_interval_data_set_complexity
+ _os_workgroup_interval_finish
+ _os_workgroup_interval_start
+ _os_workgroup_join
+ _os_workgroup_leave
+ _printf
+ _sandbox_check
+ _strrchr
+ _vImageScale_Planar8
+ _x_stream_vprintf
+ _xpc_data_get_bytes_ptr
+ _xpc_data_get_length
+ _xpc_dictionary_set_data
+ _xpc_dictionary_set_value
+ _xpc_mach_send_copy_right
+ _xpc_mach_send_create
+ _xpc_mach_send_create_with_disposition
+ _xpc_mach_send_get_right
+ _xpc_retain
- +[CALinearMaskLayer defaultValueForKey:]
- -[CADisplayStateControl(Internal) didChangeToState:seed:result:]
- -[CAFenceHandle _initWithXPCRepresentation:]
- -[CALinearMaskLayer _copyRenderLayer:layerFlags:commitFlags:]
- -[CALinearMaskLayer drawInLinearMaskContext:]
- -[CALinearMaskLayer foregroundColor]
- -[CALinearMaskLayer setForegroundColor:]
- -[CASmoothedTextLayer fontSmoothingStyle]
- -[CASmoothedTextLayer setFontSmoothingStyle:]
- -[CAWindowServerDisplay finishExternalUpdate:withFlags:]
- GCC_except_table10013
- GCC_except_table10062
- GCC_except_table10267
- GCC_except_table10290
- GCC_except_table10293
- GCC_except_table10315
- GCC_except_table10327
- GCC_except_table10360
- GCC_except_table10388
- GCC_except_table10392
- GCC_except_table10398
- GCC_except_table10404
- GCC_except_table10512
- GCC_except_table10513
- GCC_except_table10549
- GCC_except_table10554
- GCC_except_table10567
- GCC_except_table10717
- GCC_except_table10723
- GCC_except_table10727
- GCC_except_table10736
- GCC_except_table10778
- GCC_except_table10779
- GCC_except_table10898
- GCC_except_table10899
- GCC_except_table10903
- GCC_except_table1102
- GCC_except_table1143
- GCC_except_table1148
- GCC_except_table1157
- GCC_except_table1176
- GCC_except_table1183
- GCC_except_table1184
- GCC_except_table1190
- GCC_except_table1192
- GCC_except_table1193
- GCC_except_table1320
- GCC_except_table1326
- GCC_except_table1348
- GCC_except_table1431
- GCC_except_table1483
- GCC_except_table1492
- GCC_except_table1498
- GCC_except_table1500
- GCC_except_table1510
- GCC_except_table1513
- GCC_except_table1750
- GCC_except_table1929
- GCC_except_table1945
- GCC_except_table2066
- GCC_except_table2067
- GCC_except_table2069
- GCC_except_table2071
- GCC_except_table2075
- GCC_except_table2111
- GCC_except_table2112
- GCC_except_table2115
- GCC_except_table2116
- GCC_except_table2117
- GCC_except_table2120
- GCC_except_table2121
- GCC_except_table2122
- GCC_except_table2123
- GCC_except_table2125
- GCC_except_table2138
- GCC_except_table2149
- GCC_except_table2169
- GCC_except_table2170
- GCC_except_table2175
- GCC_except_table2188
- GCC_except_table2189
- GCC_except_table2190
- GCC_except_table2192
- GCC_except_table2202
- GCC_except_table2208
- GCC_except_table2227
- GCC_except_table2228
- GCC_except_table2233
- GCC_except_table2245
- GCC_except_table2246
- GCC_except_table2247
- GCC_except_table2249
- GCC_except_table2260
- GCC_except_table2280
- GCC_except_table2285
- GCC_except_table2297
- GCC_except_table2300
- GCC_except_table235
- GCC_except_table2353
- GCC_except_table2412
- GCC_except_table2415
- GCC_except_table2426
- GCC_except_table2429
- GCC_except_table2449
- GCC_except_table2452
- GCC_except_table2466
- GCC_except_table2469
- GCC_except_table2471
- GCC_except_table2473
- GCC_except_table2497
- GCC_except_table270
- GCC_except_table273
- GCC_except_table276
- GCC_except_table282
- GCC_except_table285
- GCC_except_table2872
- GCC_except_table2877
- GCC_except_table288
- GCC_except_table291
- GCC_except_table2930
- GCC_except_table2935
- GCC_except_table2940
- GCC_except_table2950
- GCC_except_table3195
- GCC_except_table3347
- GCC_except_table3419
- GCC_except_table3420
- GCC_except_table3422
- GCC_except_table3496
- GCC_except_table3509
- GCC_except_table3511
- GCC_except_table3513
- GCC_except_table3517
- GCC_except_table3519
- GCC_except_table3525
- GCC_except_table3529
- GCC_except_table353
- GCC_except_table3534
- GCC_except_table3655
- GCC_except_table4000
- GCC_except_table4001
- GCC_except_table4005
- GCC_except_table4006
- GCC_except_table4007
- GCC_except_table4011
- GCC_except_table4013
- GCC_except_table4021
- GCC_except_table4032
- GCC_except_table4034
- GCC_except_table4037
- GCC_except_table4038
- GCC_except_table4044
- GCC_except_table4050
- GCC_except_table4052
- GCC_except_table4053
- GCC_except_table4055
- GCC_except_table4056
- GCC_except_table4057
- GCC_except_table4062
- GCC_except_table4066
- GCC_except_table4067
- GCC_except_table4222
- GCC_except_table4225
- GCC_except_table4247
- GCC_except_table4250
- GCC_except_table4257
- GCC_except_table4258
- GCC_except_table436
- GCC_except_table439
- GCC_except_table441
- GCC_except_table452
- GCC_except_table454
- GCC_except_table456
- GCC_except_table460
- GCC_except_table464
- GCC_except_table4640
- GCC_except_table4642
- GCC_except_table4646
- GCC_except_table4664
- GCC_except_table4667
- GCC_except_table4680
- GCC_except_table4681
- GCC_except_table4688
- GCC_except_table4707
- GCC_except_table4709
- GCC_except_table471
- GCC_except_table4716
- GCC_except_table4717
- GCC_except_table472
- GCC_except_table4721
- GCC_except_table4730
- GCC_except_table4732
- GCC_except_table4737
- GCC_except_table4752
- GCC_except_table4753
- GCC_except_table4754
- GCC_except_table4759
- GCC_except_table476
- GCC_except_table4761
- GCC_except_table4763
- GCC_except_table4765
- GCC_except_table4766
- GCC_except_table4821
- GCC_except_table483
- GCC_except_table484
- GCC_except_table4874
- GCC_except_table4875
- GCC_except_table4878
- GCC_except_table4879
- GCC_except_table4881
- GCC_except_table4888
- GCC_except_table491
- GCC_except_table492
- GCC_except_table5198
- GCC_except_table5199
- GCC_except_table5201
- GCC_except_table5208
- GCC_except_table5210
- GCC_except_table5217
- GCC_except_table5227
- GCC_except_table5230
- GCC_except_table5249
- GCC_except_table5271
- GCC_except_table5274
- GCC_except_table5301
- GCC_except_table5313
- GCC_except_table5315
- GCC_except_table5318
- GCC_except_table532
- GCC_except_table536
- GCC_except_table537
- GCC_except_table538
- GCC_except_table5390
- GCC_except_table541
- GCC_except_table5426
- GCC_except_table5450
- GCC_except_table5458
- GCC_except_table5491
- GCC_except_table5498
- GCC_except_table5508
- GCC_except_table5557
- GCC_except_table5559
- GCC_except_table5563
- GCC_except_table5583
- GCC_except_table5585
- GCC_except_table5589
- GCC_except_table5590
- GCC_except_table5593
- GCC_except_table5594
- GCC_except_table5595
- GCC_except_table5616
- GCC_except_table5623
- GCC_except_table5624
- GCC_except_table576
- GCC_except_table5840
- GCC_except_table590
- GCC_except_table591
- GCC_except_table594
- GCC_except_table6229
- GCC_except_table6234
- GCC_except_table6235
- GCC_except_table6236
- GCC_except_table6252
- GCC_except_table6253
- GCC_except_table6254
- GCC_except_table6259
- GCC_except_table6261
- GCC_except_table6262
- GCC_except_table6265
- GCC_except_table6286
- GCC_except_table6293
- GCC_except_table6294
- GCC_except_table6296
- GCC_except_table6298
- GCC_except_table6301
- GCC_except_table6305
- GCC_except_table6306
- GCC_except_table6307
- GCC_except_table6309
- GCC_except_table6319
- GCC_except_table6321
- GCC_except_table6341
- GCC_except_table6342
- GCC_except_table645
- GCC_except_table649
- GCC_except_table650
- GCC_except_table6531
- GCC_except_table6533
- GCC_except_table659
- GCC_except_table6659
- GCC_except_table667
- GCC_except_table670
- GCC_except_table6708
- GCC_except_table6711
- GCC_except_table6713
- GCC_except_table6813
- GCC_except_table6815
- GCC_except_table6817
- GCC_except_table6820
- GCC_except_table6853
- GCC_except_table6857
- GCC_except_table6860
- GCC_except_table6862
- GCC_except_table6863
- GCC_except_table6865
- GCC_except_table6866
- GCC_except_table6867
- GCC_except_table687
- GCC_except_table6870
- GCC_except_table6881
- GCC_except_table6912
- GCC_except_table695
- GCC_except_table7022
- GCC_except_table7027
- GCC_except_table7028
- GCC_except_table703
- GCC_except_table7031
- GCC_except_table7032
- GCC_except_table7037
- GCC_except_table7039
- GCC_except_table7041
- GCC_except_table7042
- GCC_except_table7045
- GCC_except_table7048
- GCC_except_table705
- GCC_except_table7051
- GCC_except_table7054
- GCC_except_table7061
- GCC_except_table7062
- GCC_except_table7065
- GCC_except_table7066
- GCC_except_table707
- GCC_except_table7075
- GCC_except_table7077
- GCC_except_table7079
- GCC_except_table7080
- GCC_except_table7083
- GCC_except_table7089
- GCC_except_table7091
- GCC_except_table7093
- GCC_except_table7097
- GCC_except_table7099
- GCC_except_table7100
- GCC_except_table7102
- GCC_except_table7104
- GCC_except_table7105
- GCC_except_table7106
- GCC_except_table7108
- GCC_except_table7110
- GCC_except_table7119
- GCC_except_table7136
- GCC_except_table7138
- GCC_except_table7142
- GCC_except_table7145
- GCC_except_table7148
- GCC_except_table7152
- GCC_except_table7164
- GCC_except_table717
- GCC_except_table7172
- GCC_except_table7174
- GCC_except_table7177
- GCC_except_table7179
- GCC_except_table7186
- GCC_except_table7188
- GCC_except_table7190
- GCC_except_table7196
- GCC_except_table7197
- GCC_except_table7198
- GCC_except_table7200
- GCC_except_table725
- GCC_except_table728
- GCC_except_table7285
- GCC_except_table7287
- GCC_except_table7294
- GCC_except_table7295
- GCC_except_table7296
- GCC_except_table7297
- GCC_except_table7298
- GCC_except_table7299
- GCC_except_table7300
- GCC_except_table7306
- GCC_except_table7314
- GCC_except_table7318
- GCC_except_table7320
- GCC_except_table7330
- GCC_except_table7332
- GCC_except_table734
- GCC_except_table7423
- GCC_except_table7424
- GCC_except_table7427
- GCC_except_table7431
- GCC_except_table7432
- GCC_except_table7435
- GCC_except_table7436
- GCC_except_table7437
- GCC_except_table7438
- GCC_except_table745
- GCC_except_table750
- GCC_except_table772
- GCC_except_table773
- GCC_except_table7731
- GCC_except_table785
- GCC_except_table7889
- GCC_except_table7923
- GCC_except_table794
- GCC_except_table7954
- GCC_except_table7955
- GCC_except_table7956
- GCC_except_table7957
- GCC_except_table7961
- GCC_except_table7962
- GCC_except_table7963
- GCC_except_table7964
- GCC_except_table798
- GCC_except_table7987
- GCC_except_table801
- GCC_except_table8012
- GCC_except_table8013
- GCC_except_table8014
- GCC_except_table8027
- GCC_except_table8030
- GCC_except_table804
- GCC_except_table8054
- GCC_except_table8055
- GCC_except_table8057
- GCC_except_table8059
- GCC_except_table806
- GCC_except_table8060
- GCC_except_table8063
- GCC_except_table8064
- GCC_except_table8065
- GCC_except_table8069
- GCC_except_table8071
- GCC_except_table8072
- GCC_except_table8073
- GCC_except_table8079
- GCC_except_table8086
- GCC_except_table8088
- GCC_except_table809
- GCC_except_table8090
- GCC_except_table8092
- GCC_except_table8098
- GCC_except_table810
- GCC_except_table8100
- GCC_except_table8101
- GCC_except_table8103
- GCC_except_table8104
- GCC_except_table8105
- GCC_except_table811
- GCC_except_table812
- GCC_except_table8122
- GCC_except_table8174
- GCC_except_table8177
- GCC_except_table8179
- GCC_except_table8250
- GCC_except_table8364
- GCC_except_table8383
- GCC_except_table8385
- GCC_except_table8527
- GCC_except_table8566
- GCC_except_table8718
- GCC_except_table8868
- GCC_except_table8914
- GCC_except_table8952
- GCC_except_table9104
- GCC_except_table9107
- GCC_except_table9108
- GCC_except_table9111
- GCC_except_table9163
- GCC_except_table9398
- GCC_except_table9399
- GCC_except_table9400
- GCC_except_table9403
- GCC_except_table9510
- GCC_except_table9515
- GCC_except_table9646
- GCC_except_table9648
- GCC_except_table9651
- GCC_except_table9672
- _CADeviceSupportsOddQuantaFrameRates
- _CADeviceUseSharedEvents
- _CAGetLUTFile
- _CALinearMaskContextClearRect
- _CALinearMaskContextConcatCTM
- _CALinearMaskContextDrawGlyphs
- _CALinearMaskContextGetCTM
- _CARenderOGLSetDestinationIOSurface
- _CARenderServerCopyODStatistics
- _CARenderServerSetOverdriveLUTFile
- _CASSetLUTFile
- _CASSetMessageFile
- _CASetLUTFile
- _CAUpdateEarliestTailspinEmissionTime
- _IOMobileFramebufferGetMatrix
- _IOMobileFramebufferSwapWorkaroundSettings
- _IOSurfaceGetDataProperty
- _MGGetProductType
- _OBJC_CLASS_$_CALinearMaskLayer
- _OBJC_CLASS_$_CASmoothedTextLayer
- _OBJC_IVAR_$_CADisplayStateControl._callback_lock
- _OBJC_IVAR_$_CADisplayStateControl._completion
- _OBJC_IVAR_$_CADisplayStateControl._seed
- _OBJC_IVAR_$_CADisplayStateControl._target_state
- _OBJC_METACLASS_$_CALinearMaskLayer
- _OBJC_METACLASS_$_CASmoothedTextLayer
- __CACDisplayDidChangeToState
- __OBJC_$_CLASS_METHODS_CALinearMaskLayer
- __OBJC_$_INSTANCE_METHODS_CALinearMaskLayer
- __OBJC_$_INSTANCE_METHODS_CASmoothedTextLayer
- __OBJC_$_PROP_LIST_CALinearMaskLayer
- __OBJC_$_PROP_LIST_CAMetalDrawable.266
- __OBJC_$_PROP_LIST_CASmoothedTextLayer
- __OBJC_CLASS_RO_$_CALinearMaskLayer
- __OBJC_CLASS_RO_$_CASmoothedTextLayer
- __OBJC_METACLASS_RO_$_CALinearMaskLayer
- __OBJC_METACLASS_RO_$_CASmoothedTextLayer
- __XDisplayDidChangeToState
- __XGetODStatistics
- __XSetLUTFile
- __XSetMessageFile
- __Z29iomfb_swap_set_tonemap_configP21__IOMobileFramebufferP18IOMFBToneMapConfigj
- __ZGVZ40+[CALinearMaskLayer defaultValueForKey:]E5color
- __ZGVZN2CA20HDRProcessorInternal30create_surface_with_forward_dmEPKNS_6Render7SurfaceEPNS1_6UpdateEPKNS1_17DisplayAttributesEbfNS1_12TextureFlagsEbbbbE9sdr_attrs
- __ZL10write_attrjPKv12_CAValueTypePv.20279
- __ZL10x_log_initv
- __ZL10x_log_once
- __ZL11block_ctors.16539
- __ZL11initialized.17961
- __ZL12collect_slot.10549
- __ZL13x_stream_pop_P15x_stream_struct
- __ZL14release_samplejyPv.10550
- __ZL14x_log_function
- __ZL15copy_dictionaryjPKv12_CAValueTypePv.20301
- __ZL15lowLatency_atom.10757
- __ZL15reason_messages
- __ZL15skip_whitespacePKcS0_
- __ZL15x_log_file_name
- __ZL16release_drawableP20_CAMetalLayerPrivateP23_CAMetalDrawablePrivate
- __ZL16x_close_log_filev
- __ZL17x_log_file_handle
- __ZL17x_log_stream_initv
- __ZL17x_log_stream_once
- __ZL17x_log_stream_slot
- __ZL19x_log_function_info
- __ZL20cg_color_from_valuesIN2CA4Vec4IfEEEP7CGColorRKT_P12CGColorSpaceb
- __ZL21will_suspend_callbackPN2CA6Render6ObjectEPvS3_.7173
- __ZL24layer_collectable_signalP13_CAImageQueuePv.10551
- __ZL25allocate_drawable_texturePU19objcproto9MTLDevice11objc_objectP11__IOSurfacejj14MTLPixelFormaty20CAMetalLayerRotationbP8NSStringm
- __ZL25libedr_min_scale_factor_f
- __ZL28presentsWithTransaction_atom.10633
- __ZL29iomfb_swap_set_aml_strength_f
- __ZL30cg_color_from_pattern_or_colorRK25ReverseSerializationStatePKN2CA6Render7PatternERKNS2_4Vec4IfEE
- __ZL31iomfb_swap_set_tonemap_config_f
- __ZL5blackv.20130
- __ZL8lut_file
- __ZL8set_attrPKvS0_Pv.20293
- __ZL9copy_attrjPKv12_CAValueTypePv.20303
- __ZN12_GLOBAL__N_130_CARenderServerSnapshotDisplayEjPK10__CFStringPKvjiiPK13CATransform3DjmPjj
- __ZN1X17small_vector_baseIU13block_pointerFvPK14__CFDictionaryEEC2EOS6_PS5_
- __ZN20CACGContextEvaluator17update_with_colorEP7CGColor20CGCompositeOperation
- __ZN20CACGContextEvaluator17update_with_imageEP7CGImage
- __ZN24RGBXYZConversionMatricesIdEC2E17RGBColorPrimariesIdE3xyYIdE
- __ZN24RGBXYZConversionMatricesIfEC2E17RGBColorPrimariesIfE3xyYIfE
- __ZN2CA10BoundsImpl8containsERKNS_11GenericRectIiEES4_
- __ZN2CA11Transaction9add_fenceEjP13CAFenceHandleU13block_pointerFvvE
- __ZN2CA12ColorProgram7Program13color_programEPK21CGColorConversionInfoP12CGColorSpacei28CGColorConversionIterateTypebijffRb
- __ZN2CA12WindowServer11IOMFBServer11set_enabledEb
- __ZN2CA12WindowServer11IOMFBServer15current_surfaceEbyb
- __ZN2CA12WindowServer11IOMFBServer15set_edr_enabledEbf
- __ZN2CA12WindowServer11IOMFBServer16signpost_contextEjjjPKciPK10__CFStringyyy
- __ZN2CA12WindowServer11IOMFBServer19add_power_log_timerEv
- __ZN2CA12WindowServer11IOMFBServer21set_calibration_phaseEjj
- __ZN2CA12WindowServer11IOMFBServer27forward_frame_info_callbackEjPK14__CFDictionaryRKNS0_12IOMFBDisplay9FrameInfoE
- __ZN2CA12WindowServer11SharedEvent11UsageStringE
- __ZN2CA12WindowServer11SharedEvent12AccessStringE
- __ZN2CA12WindowServer11SharedEvent14force_completeEb
- __ZN2CA12WindowServer11SharedEvent14get_wait_valueENS1_5UsageENS1_6AccessE
- __ZN2CA12WindowServer11SharedEvent15OperationStringE
- __ZN2CA12WindowServer11SharedEvent16inc_signal_valueENS1_5UsageENS1_6AccessE
- __ZN2CA12WindowServer11SharedEvent24is_complete_with_timeoutEv
- __ZN2CA12WindowServer11SharedEvent7History3addEPNS0_7SurfaceENS1_5UsageENS1_9OperationENS1_6AccessEy
- __ZN2CA12WindowServer11SharedEventD2Ev
- __ZN2CA12WindowServer12IOMFBDisplay11set_enabledEb
- __ZN2CA12WindowServer12IOMFBDisplay11will_enableEv
- __ZN2CA12WindowServer12IOMFBDisplay12set_enabled_Eb
- __ZN2CA12WindowServer12IOMFBDisplay13create_bufferEPNS0_7SurfaceE
- __ZN2CA12WindowServer12IOMFBDisplay13disable_cloneEv
- __ZN2CA12WindowServer12IOMFBDisplay14update_surfaceEbbyb
- __ZN2CA12WindowServer12IOMFBDisplay15collect_buffersEy
- __ZN2CA12WindowServer12IOMFBDisplay15current_surfaceEbyb
- __ZN2CA12WindowServer12IOMFBDisplay15present_surfaceEP11__IOSurface
- __ZN2CA12WindowServer12IOMFBDisplay15set_temperatureEf
- __ZN2CA12WindowServer12IOMFBDisplay18update_framebufferEj
- __ZN2CA12WindowServer12IOMFBDisplay20current_page_surfaceEbbbbyb
- __ZN2CA12WindowServer12IOMFBDisplay22set_power_state_lockedENS0_17DisplayPowerStateEbb
- __ZN2CA12WindowServer12IOMFBDisplay23power_assertion_changedEb
- __ZN2CA12WindowServer12IOMFBDisplay25update_power_state_lockedEbb
- __ZN2CA12WindowServer12IOMFBDisplay26set_blanking_removes_powerEb
- __ZN2CA12WindowServer12IOMFBDisplay26update_interval_complexityEiiih
- __ZN2CA12WindowServer12IOMFBDisplayC2EPK10__CFStringjj16IOMFBDisplayType
- __ZN2CA12WindowServer13VirtualServer11set_enabledEb
- __ZN2CA12WindowServer14VirtualDisplay11set_enabledEb
- __ZN2CA12WindowServer14VirtualDisplay14update_surfaceEbbyb
- __ZN2CA12WindowServer14VirtualDisplay15current_surfaceEbyb
- __ZN2CA12WindowServer20AppleExternalDisplayC2EPK10__CFStringjj16IOMFBDisplayType
- __ZN2CA12WindowServer6Server11set_enabledEb
- __ZN2CA12WindowServer6Server14schedule_blockEU13block_pointerFvvE
- __ZN2CA12WindowServer6Server15current_surfaceEbyb
- __ZN2CA12WindowServer6Server15present_surfaceEP11__IOSurface
- __ZN2CA12WindowServer6Server15set_edr_enabledEbf
- __ZN2CA12WindowServer6Server17get_od_statisticsEPNS_6Render6ObjectEPvS5_
- __ZN2CA12WindowServer6Server21set_calibration_phaseEjj
- __ZN2CA12WindowServer6Server23set_frame_info_callbackEU13block_pointerFvjjyyyyjbbbfffyjbE
- __ZN2CA12WindowServer6Server24OSSignpostRenderInterval23render_status_to_stringENS0_12RenderStatusE
- __ZN2CA12WindowServer6Server24OSSignpostRenderInterval35render_status_to_legacy_reason_codeENS0_12RenderStatusE
- __ZN2CA12WindowServer7Display11will_enableEv
- __ZN2CA12WindowServer7Display13disable_cloneEv
- __ZN2CA12WindowServer7Display15current_surfaceEbyb
- __ZN2CA12WindowServer7Display15present_surfaceEP11__IOSurface
- __ZN2CA12WindowServer7Display15set_power_stateENS0_17DisplayPowerStateEbb
- __ZN2CA12WindowServer7Display15set_temperatureEf
- __ZN2CA12WindowServer7Display18update_clone_flagsEb
- __ZN2CA12WindowServer7Display20complete_powering_onEv
- __ZN2CA12WindowServer7Display20set_user_preferencesEbNS1_7HDRTypeEb
- __ZN2CA12WindowServer7Display22set_power_state_lockedENS0_17DisplayPowerStateEbb
- __ZN2CA12WindowServer7Display26set_blanking_removes_powerEb
- __ZN2CA12WindowServer7Display26update_interval_complexityEiiih
- __ZN2CA12WindowServer7Display31send_display_state_change_replyEv
- __ZN2CA12WindowServer7Display32flush_display_state_change_replyEv
- __ZN2CA12WindowServer7Display7ModeSet22set_mig_representationEPymPjS4_mPNS_6Render11PerModeInfoEmj
- __ZN2CA12WindowServerL10null_timerEP16__CFRunLoopTimerPv.17336
- __ZN2CA12WindowServerL17print_layer_treesEdPK13x_link_structb
- __ZN2CA12WindowServerL17swap_wait_timeoutERNS_19IOMobileFramebufferEjjPd
- __ZN2CA12WindowServerL23no_pq_external_chip_idsE
- __ZN2CA12WindowServerL27dict_shared_event_set_valueEP14__CFDictionaryPNS0_11SharedEventEbb
- __ZN2CA14CAHDRProcessor29should_invalidate_tonemappingEffff
- __ZN2CA19IOMobileFramebuffer13swap_set_timeE18IOMFBTimestampTyped
- __ZN2CA19IOMobileFramebuffer18swap_set_icc_curveE13IOMFBCurveLocjjjPK14IOMFBCurveData
- __ZN2CA19IOMobileFramebuffer19swap_set_icc_matrixE14IOMFBICCMatLocjjPK16IOMFBColorMatrix
- __ZN2CA20HDRProcessorInternal15tonemap_surfaceEP11__IOSurfaceS2_PNS_12WindowServer11SharedEventES5_PKNS_6Render17DisplayAttributesEPNS6_6UpdateEbybPi
- __ZN2CA20HDRProcessorInternal24tonemap_surface_internalEP11__IOSurfaceS2_PNS_6Render6UpdateEPNS_12WindowServer11SharedEventES8_R26HDRConfigurationParametersRf22HDRProcessingOperationPKNS3_17DisplayAttributesE24CATonemapAcceleratorTypebPU27objcproto16MTLCommandBuffer11objc_objectPbbNS3_12TextureFlagsEbPK8__CFDataNS3_11SurfaceTypeEPi
- __ZN2CA20HDRProcessorInternal30configure_display_pipe_tonemapEP11__IOSurfacejPKNS_6Render17DisplayAttributesEPP12CGColorSpaceU13block_pointerFvP18IOMFBToneMapConfigEU13block_pointerFv13IOMFBCurveLocPK14IOMFBCurveDataEU13block_pointerFv14IOMFBICCMatLocPK16IOMFBColorMatrixE
- __ZN2CA20HDRProcessorInternal30create_surface_with_forward_dmEPKNS_6Render7SurfaceEPNS1_6UpdateEPKNS1_17DisplayAttributesEbfNS1_12TextureFlagsEbbbb
- __ZN2CA20HDRProcessorInternal36get_or_create_hdr_processor_instanceE25HDRProcessingHardwareTypeP26HDRConfigurationParameters
- __ZN2CA24emit_package_parse_errorEPP7NSErrorP8NSString
- __ZN2CA2CG10fill_imageERNS0_8RendererEP7CGImageRKNS_4RectERKNS_4Mat2IdEEbb22CGInterpolationQualityfPKNS_6BoundsE
- __ZN2CA2CG13GlyphDelegateC1ERNS0_8RendererERNS_3OGL7ContextENS4_13ExtendedColorENS1_10BrightnessEPKNS0_11ShadowStyleEf
- __ZN2CA2CG15ContextDelegate12device_colorEPKdP12CGColorSpace
- __ZN2CA2CG15FillRectsShadowC2ERNS0_15ContextDelegateERKNS0_9FillRectsEP16CGRenderingStateP8CGGStatePKNS0_11ShadowStyleEj
- __ZN2CA2CG21FillRoundedRectShadowC2ERNS0_15ContextDelegateERKNS0_15FillRoundedRectEP16CGRenderingStateP8CGGStatePKNS0_11ShadowStyleEj
- __ZN2CA2CG5Queue18did_flush_rendererEv
- __ZN2CA2CG8Renderer10mark_dirtyERKNS_6BoundsE
- __ZN2CA3OGL10PathFiller10mark_spansENS_4Vec2IfEES3_
- __ZN2CA3OGL10PathFiller5closeEv
- __ZN2CA3OGL10PathFiller7cube_toENS_4Vec2IfEES3_S3_
- __ZN2CA3OGL10PathFiller7line_toENS_4Vec2IfEE
- __ZN2CA3OGL10PathFiller7quad_toENS_4Vec2IfEES3_
- __ZN2CA3OGL10PathFiller8add_cubeEPKNS_4Vec2IfEEff
- __ZN2CA3OGL10PathFiller9emit_cubeEPNS_4Vec2IfEEm
- __ZN2CA3OGL10PathFiller9emit_lineEPNS_4Vec2IfEE
- __ZN2CA3OGL10cache_nodeERNS0_8RendererEPNS0_5LayerERKNS_6Render7CacheIdEPNS0_11ImagingNodeE
- __ZN2CA3OGL11GLESContext14create_surfaceEiRKNS_6BoundsEj
- __ZN2CA3OGL11NullContext14create_surfaceEiRKNS_6BoundsEj
- __ZN2CA3OGL11NullContext16function_uniformEjmmPKf
- __ZN2CA3OGL11PathStroker11flush_joinsEv
- __ZN2CA3OGL11PathStroker15add_line_pointsEPNS_4Vec2IfEE
- __ZN2CA3OGL11PathStroker20line_to_axis_alignedENS_4Vec2IfEE
- __ZN2CA3OGL11PathStroker7cube_toENS_4Vec2IfEES3_S3_
- __ZN2CA3OGL11PathStroker7line_toENS_4Vec2IfEE
- __ZN2CA3OGL11PathStroker7move_toENS_4Vec2IfEE
- __ZN2CA3OGL11PathStroker7quad_toENS_4Vec2IfEES3_
- __ZN2CA3OGL11PathStroker8add_joinEv
- __ZN2CA3OGL11PathStroker9emit_cubeEPNS_4Vec2IfEEfm
- __ZN2CA3OGL11emit_filterERNS0_8RendererERKNS0_6FilterERKNS0_5LayerEfPNS0_7SurfaceEfbPKNS_5ShapeESD_Pf
- __ZN2CA3OGL12MetalContext14bind_overdriveEjjffifPiRfS3_
- __ZN2CA3OGL12MetalContext14create_surfaceEiRKNS_6BoundsEj
- __ZN2CA3OGL12MetalContext15draw_path_joinsEjPKNS0_8PathJoinE
- __ZN2CA3OGL12MetalContext15draw_path_linesEjPKDv2_f
- __ZN2CA3OGL12MetalContext16function_uniformEjmmPKf
- __ZN2CA3OGL12MetalContext19shared_event_submitEPNS_12WindowServer11SharedEventEbNS3_5UsageENS3_6AccessE
- __ZN2CA3OGL12MetalContext22calculate_average_lumaEPNS0_7SurfaceEU13block_pointerFvfE
- __ZN2CA3OGL12MetalContext22shared_event_wait_readEPNS_12WindowServer11SharedEventE
- __ZN2CA3OGL12MetalContext23shared_event_wait_writeEPNS_12WindowServer11SharedEventE
- __ZN2CA3OGL12MetalContext24shared_event_signal_readEPNS_12WindowServer11SharedEventE
- __ZN2CA3OGL12MetalContext25shared_event_signal_writeEPNS_12WindowServer11SharedEventE
- __ZN2CA3OGL12_GLOBAL__N_116collect_surfacesERNS0_7ContextEPPNS0_7SurfaceEPNS_6BoundsEbRb
- __ZN2CA3OGL12_GLOBAL__N_128desired_src_edge_replicationEPKNS_6Render13BackdropGroupEPKNS0_5LayerERNS0_7ContextEPNS_4RectEPNS_4Vec2IfEEPbSG_
- __ZN2CA3OGL12render_shapeERNS0_8RendererEPKNS0_5LayerEPNS_6Render4PathENS_13ScanConverter8FillRuleERKNS_4RectENS_4Vec4IfEEPNS6_7PatternEb
- __ZN2CA3OGL15emit_large_brimERNS0_7ContextEPNS0_7SurfaceERNS_4RectEdNS0_13ExtendedColorEfdS7_fRKNS_9TransformEfb
- __ZN2CA3OGL15prepare_filtersERNS0_8RendererERNS0_5LayerEPNS_6Render10TypedArrayINS5_6FilterEEEbRNS0_17SourceRequirementEb
- __ZN2CA3OGL18FramebufferSurfaceC2Ev
- __ZN2CA3OGL18prepare_layers_roiERNS0_8RendererEPNS0_5LayerERKNS0_6GstateE
- __ZN2CA3OGL23render_solid_backgroundERNS0_8RendererEPKNS0_5LayerENS0_13ExtendedColorEPNS_6Render7PatternE
- __ZN2CA3OGL25merge_compressed_geometryEPKdS2_PKfS4_fjffPdPfS6_
- __ZN2CA3OGL7Context10_trace_logE
- __ZN2CA3OGL7Context13lookup_image_EPNS_6Render7TextureEb
- __ZN2CA3OGL7Context13remove_imagesEPKNS_6Render6ObjectEPNS0_5ImageEPv
- __ZN2CA3OGL7Context14bind_overdriveEjjffifPiRfS3_
- __ZN2CA3OGL7Context15draw_path_joinsEjPKNS0_8PathJoinE
- __ZN2CA3OGL7Context15draw_path_linesEjPKDv2_f
- __ZN2CA3OGL7Context18device_float_colorEPfP12CGColorSpacePKdf
- __ZN2CA3OGL7Context22calculate_average_lumaEPNS0_7SurfaceEU13block_pointerFvfE
- __ZN2CA3OGL7Context22shared_event_wait_readEPNS_12WindowServer11SharedEventE
- __ZN2CA3OGL7Context23shared_event_wait_writeEPNS_12WindowServer11SharedEventE
- __ZN2CA3OGL7Context24shared_event_signal_readEPNS_12WindowServer11SharedEventE
- __ZN2CA3OGL7Context25shared_event_signal_writeEPNS_12WindowServer11SharedEventE
- __ZN2CA3OGL7Context28variable_masked_blur_surfaceEfPNS0_7SurfaceEfPNS_6Render7TextureERKNS_4Mat4IdEERKNS1_10BlurParamsEPf
- __ZN2CA3OGL7Context34update_color_program_cache_whippetEfP12CGColorSpacef
- __ZN2CA3OGL8Renderer6renderEPKNS_6Render6UpdateEmPNS_12WindowServer11SharedEventE
- __ZN2CA3OGL9GLContext13update_shaderEv
- __ZN2CA3OGL9GLContext16function_uniformEjmmPKf
- __ZN2CA3OGL9SWContext14create_surfaceEiRKNS_6BoundsEj
- __ZN2CA3OGL9SWContext16function_uniformEjmmPKf
- __ZN2CA3OGLL14ycbcr_matricesE.9422
- __ZN2CA3OGLL19bind_filter_surfaceERNS0_7ContextEPNS0_7SurfaceEf
- __ZN2CA3OGLL20add_primitive_filterEPNS0_6FilterEPKNS_6Render6FilterE
- __ZN2CA3OGLL20edr_gain_filter_gainEPKNS_6Render6FilterEff
- __ZN2CA3OGLL21non_srgb_pixel_formatE14MTLPixelFormat
- __ZN2CA3OGLL22overdrive_texture_dataEii
- __ZN2CA3OGLL22render_edr_gain_filterERNS0_7ContextEPKNS_6Render6FilterEPNS0_7SurfaceEff
- __ZN2CA3OGLL23create_gamma_lut_bufferEPU19objcproto9MTLDevice11objc_object
- __ZN2CA3OGLL27render_vibrant_color_matrixERNS0_7ContextEPKNS_6Render6FilterEPNS0_7SurfaceEf
- __ZN2CA3OGLL31render_edr_gain_multiply_filterERNS0_7ContextEPKNS_6Render6FilterEPNS0_7SurfaceEff
- __ZN2CA5Layer16layout_if_neededEPNS_11TransactionE
- __ZN2CA6Render10ShapeLayer8set_pathEPNS0_4PathE
- __ZN2CA6Render11HitTestTree4Node37subtract_subtree_occlusion_from_shapeERKNS_6BoundsEPPNS_5ShapeE
- __ZN2CA6Render11ShadowCache10free_entryEPNS0_4PathEPNS1_5EntryEPv
- __ZN2CA6Render11ShadowCache12path_deletedEPNS0_6ObjectEPvS4_
- __ZN2CA6Render11show_objectEPKNS0_6ObjectE
- __ZN2CA6Render11show_objectEPKNS0_6ObjectEjj
- __ZN2CA6Render12_GLOBAL__N_115PathAccumulator11push_movetoERKNS_4Vec2IdEE
- __ZN2CA6Render12show_newlineEj
- __ZN2CA6Render13show_cfstringEPK10__CFString
- __ZN2CA6Render14BasicAnimationC1EPNS0_7DecoderE
- __ZN2CA6Render14FlattenManager18layer_is_flattenedEPKNS0_5LayerE
- __ZN2CA6Render14FlattenManager30flattened_cache_remove_surfaceEj
- __ZN2CA6Render14FlattenManager32flattened_cache_retain_iosurfaceEj
- __ZN2CA6Render14show_transformEPKcPKdj
- __ZN2CA6Render15show_statisticsEv
- __ZN2CA6Render17print_group_flagsEjj
- __ZN2CA6Render21print_offscreen_flagsEjj
- __ZN2CA6Render21show_affine_transformEPKcRK17CGAffineTransformj
- __ZN2CA6Render22CloningTerminatorLayerC1EPNS0_7DecoderE
- __ZN2CA6Render22MatchPropertyAnimationC1EPNS0_7DecoderE
- __ZN2CA6Render5Image9set_shmemEPNS0_5ShmemE
- __ZN2CA6Render5Layer13set_rim_colorENS_4Vec4IfEE
- __ZN2CA6Render5Layer16set_border_colorENS_4Vec4IfEE
- __ZN2CA6Render5Layer16set_shadow_colorENS_4Vec4IfEE
- __ZN2CA6Render5Layer20set_background_colorENS_4Vec4IfEE
- __ZN2CA6Render5Layer27set_contents_multiply_colorENS_4Vec4IfEE
- __ZN2CA6Render6Handle14add_dependenceEPNS1_10DependenceE
- __ZN2CA6Render6Update17allowed_in_updateEPNS0_7ContextEPKNS0_5LayerE
- __ZN2CA6Render6Update21push_dependence_groupEv
- __ZN2CA6Render7Context10show_hostsEv
- __ZN2CA6Render7Context11show_hosts_Ej
- __ZN2CA6Render7Context17show_source_layerEjmjj
- __ZN2CA6Render7Surface15set_tonemap_cfgENS0_18OnDemandTonemapCfgE
- __ZN2CA6Render7Surface22set_tonemapped_surfaceEPS1_
- __ZN2CA6Render9LayerNode22update_frame_transformEPNS_4Vec2IdEE
- __ZN2CA6RenderL11print_flagsEoPKPKcmj
- __ZN2CA6RenderL14flattened_lockE
- __ZN2CA6RenderL15flattened_cacheE
- __ZN2CA6RenderL18release_deallocateEPKvPv.12523
- __ZN2CA6RenderL18release_image_dataEPKvPv.22863
- __ZN2CA7Display11DisplayLink8get_linkEPNS0_7DisplayEP11__CFRunLoopPKN1X4ListIPK10__CFStringEEU13block_pointerFbyEU13block_pointerFNS1_11DeferReasonEPK25CADisplayLinkWillFireInfoEU13block_pointerFvR17CATimingReferenceE
- __ZN2CA7Display21DisplayTimingsControl22server_triple_bufferedEv
- __ZN2CA8Mat4Impl11mat4_concatEPfPKfS3_
- __ZN2CAL19shared_event_submitEPU19objcproto9MTLDevice11objc_objectPU27objcproto16MTLCommandBuffer11objc_objectPNS_12WindowServer11SharedEventEbNS5_6AccessE
- __ZN2CAL32iomfb_icc_curve_params_to_stringEPK14IOMFBCurveDataPcm
- __ZNK2CA12ColorProgram7Program4showEv
- __ZNK2CA12WindowServer12AppleDisplay23compressed_pixel_formatEjm
- __ZNK2CA12WindowServer12IOMFBDisplay10is_enabledEv
- __ZNK2CA12WindowServer12IOMFBDisplay11temperatureEv
- __ZNK2CA12WindowServer12IOMFBDisplay14od_lut_versionEv
- __ZNK2CA12WindowServer12IOMFBDisplay15needs_overdriveEv
- __ZNK2CA12WindowServer12IOMFBDisplay15triple_bufferedEv
- __ZNK2CA12WindowServer12IOMFBDisplay17workaround_matrixEv
- __ZNK2CA12WindowServer12IOMFBDisplay22blanking_removes_powerEv
- __ZNK2CA12WindowServer12IOMFBDisplay23compressed_pixel_formatEjm
- __ZNK2CA12WindowServer14VirtualDisplay10is_enabledEv
- __ZNK2CA12WindowServer20AppleInternalDisplay10ffr_factorEv
- __ZNK2CA12WindowServer20AppleInternalDisplay18overdrive_lut_typeEv
- __ZNK2CA12WindowServer6Server15triple_bufferedEv
- __ZNK2CA12WindowServer7Display10ffr_factorEv
- __ZNK2CA12WindowServer7Display11temperatureEv
- __ZNK2CA12WindowServer7Display13has_hdr_cloneEv
- __ZNK2CA12WindowServer7Display14od_lut_versionEv
- __ZNK2CA12WindowServer7Display15needs_overdriveEv
- __ZNK2CA12WindowServer7Display15triple_bufferedEv
- __ZNK2CA12WindowServer7Display17workaround_matrixEv
- __ZNK2CA12WindowServer7Display18overdrive_lut_typeEv
- __ZNK2CA12WindowServer7Display22blanking_removes_powerEv
- __ZNK2CA12WindowServer7Display7ModeSet28preferred_mode_with_criteriaE6CGSizeNS1_7HDRTypeEfS4_bRKNS1_14EDIDAttributesE
- __ZNK2CA12WindowServer7Display7ModeSet37preferred_mode_with_criteria_internalE6CGSizeNS1_7HDRTypeEfS4_bbRKNS1_14EDIDAttributesE
- __ZNK2CA12WindowServer7Display7ModeSeteqERKS2_
- __ZNK2CA3OGL10BlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfPKNS_11ColorMatrixE
- __ZNK2CA3OGL12MetalContext12StructHasherINS1_12VertexShader4SpecEEclERKS4_
- __ZNK2CA3OGL12_GLOBAL__N_114PageCurlFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfPKNS_11ColorMatrixE
- __ZNK2CA3OGL14FilterSubclass6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfbPKNS_11ColorMatrixEPKNS_5ShapeESI_Pf
- __ZNK2CA3OGL18AverageColorFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfPKNS_11ColorMatrixE
- __ZNK2CA3OGL18GaussianBlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfbPKNS_11ColorMatrixEPKNS_5ShapeESI_Pf
- __ZNK2CA3OGL18VariableBlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfbPKNS_11ColorMatrixEPKNS_5ShapeESI_Pf
- __ZNK2CA3OGL19LanczosResizeFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfPKNS_11ColorMatrixE
- __ZNK2CA3OGL25ChromaticAberrationFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfPKNS_11ColorMatrixE
- __ZNK2CA3OGL8LimitAPL6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfPKNS_11ColorMatrixE
- __ZNK2CA6Render10ImageQueue4showEjj
- __ZNK2CA6Render10MediaLayer4showEjj
- __ZNK2CA6Render10ShapeLayer4showEjj
- __ZNK2CA6Render10Subtexture4showEjj
- __ZNK2CA6Render10Transition4showEjj
- __ZNK2CA6Render11PixelBuffer4showEjj
- __ZNK2CA6Render11PortalLayer4showEjj
- __ZNK2CA6Render12GainMapLayer4showEjj
- __ZNK2CA6Render12Interpolator4showEjj
- __ZNK2CA6Render12MetalTexture4showEjj
- __ZNK2CA6Render13BackdropLayer4showEjj
- __ZNK2CA6Render13GradientLayer4showEjj
- __ZNK2CA6Render13ImageProvider4showEjj
- __ZNK2CA6Render13MeshTransform4showEjj
- __ZNK2CA6Render13NamedFunction4showEjj
- __ZNK2CA6Render14MatchAnimation20show_match_animationEjj
- __ZNK2CA6Render15CompressedImage18is_unpremultipliedEv
- __ZNK2CA6Render15CompressedImage4showEjj
- __ZNK2CA6Render15EmitterBehavior4showEjj
- __ZNK2CA6Render15ReplicatorLayer4showEjj
- __ZNK2CA6Render17DeferredImageSlot4showEjj
- __ZNK2CA6Render18CarPlayRegionLayer4showEjj
- __ZNK2CA6Render18DistanceFieldLayer4showEjj
- __ZNK2CA6Render18MatchMoveAnimation4showEjj
- __ZNK2CA6Render20PresentationModifier4showEjj
- __ZNK2CA6Render20SecureIndicatorLayer4showEjj
- __ZNK2CA6Render22CloningTerminatorLayer4showEjj
- __ZNK2CA6Render22MatchPropertyAnimation4showEjj
- __ZNK2CA6Render4Path4showEjj
- __ZNK2CA6Render5Array4showEjj
- __ZNK2CA6Render5Image4showEjj
- __ZNK2CA6Render5Layer15show_compressedEjj
- __ZNK2CA6Render5Layer4showEjj
- __ZNK2CA6Render5Layer5frameEPS1_
- __ZNK2CA6Render5Proxy4showEjj
- __ZNK2CA6Render5Shmem4showEjj
- __ZNK2CA6Render6Filter4showEjj
- __ZNK2CA6Render6Object4showEjj
- __ZNK2CA6Render6String4showEjj
- __ZNK2CA6Render6Timing4showEjj
- __ZNK2CA6Render6Vector4showEjj
- __ZNK2CA6Render7Pattern4showEjj
- __ZNK2CA6Render7Surface18is_unpremultipliedEv
- __ZNK2CA6Render7Surface4showEjj
- __ZNK2CA6Render7Texture18is_unpremultipliedEv
- __ZNK2CA6Render8KeyValue4showEjj
- __ZNK2CA6Render9Animation4showEjj
- __ZNK2CA6Render9LayerHost4showEjj
- __ZNK2CA9Transform14unapply_simpleIdEEvRT_S3_
- __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8nn190102IPNS_4pairIyyEENS_16__deque_iteratorIS5_S6_RS5_PS6_lLl256EEELi0EEENS4_IT_T0_EESB_SB_SC_
- __ZNKSt3__116__deque_iteratorINS_4pairIyyEEPS2_RS2_PS3_lLl256EEplB8nn190102El
- __ZNKSt3__120__move_backward_implINS_17_ClassicAlgPolicyEEclB8nn190102IPNS_4pairIyyEENS_16__deque_iteratorIS5_S6_RS5_PS6_lLl256EEELi0EEENS4_IT_T0_EESB_SB_SC_
- __ZNKSt3__121__murmur2_or_cityhashImLm64EEclB8nn190102EPKvm
- __ZNKSt3__18equal_toINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEclB8nn190102ERKS6_S9_
- __ZNSt3__110__function12__value_funcIFbNS_16reverse_iteratorINS_11__wrap_iterIPN2CA12WindowServer8FlipBook5FrameEEEEEEED2B8nn190102Ev
- __ZNSt3__110__function12__value_funcIFbPN2CA3OGL6VertexEjEED2B8nn190102Ev
- __ZNSt3__110unique_ptrIN2CA12WindowServer12IOMFBDisplay9FrameInfoENS_14default_deleteIS4_EEE5resetB8nn190102EPS4_
- __ZNSt3__110unique_ptrIN2CA3OGL13DebugRendererENS_14default_deleteIS3_EEE5resetB8nn190102EPS3_
- __ZNSt3__110unique_ptrIN2CA6Render13ContentStreamENS_14default_deleteIS3_EEE5resetB8nn190102EPS3_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS0_IN2CA6Render13ContentStreamENS_14default_deleteIS5_EEEEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEE5resetB8nn190102EPSB_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_mapIjjNS_4hashIjEENS_8equal_toIjEENS_9allocatorINS_4pairIKjjEEEEEEEEPvEENS_22__hash_node_destructorINS8_ISG_EEEEE5resetB8nn190102EPSG_
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIjNS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEEEEEPvEENS_22__hash_node_destructorINS8_ISD_EEEEE5resetB8nn190102EPSD_
- __ZNSt3__110unique_ptrINS_15__thread_structENS_14default_deleteIS1_EEE5resetB8nn190102EPS1_
- __ZNSt3__110unique_ptrINS_5tupleIJNS0_INS_15__thread_structENS_14default_deleteIS2_EEEEMNS_19__async_assoc_stateIP10SILManagerNS_12__async_funcIZL16sil_mgr_instancePvjE3$_0JP19NSMutableDictionaryEEEEEFvvEPSF_EEENS3_ISJ_EEED1B8nn190102Ev
- __ZNSt3__112__destroy_atB8nn190102IN2CA3OGL22TransientRenderTextureELi0EEEvPT_
- __ZNSt3__112__destroy_atB8nn190102IN2CA6Render19ContentStreamConfigELi0EEEvPT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjPN1X4ListIU13block_pointerFvvEEEEENS_22__unordered_map_hasherIjS8_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS8_SD_SB_Lb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsIjJRKNS_21piecewise_construct_tENS_5tupleIJRKjEEENSO_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjPN1X4ListIU13block_pointerFvvEEEEENS_22__unordered_map_hasherIjS8_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS8_SD_SB_Lb1EEENS_9allocatorIS8_EEE4findIjEENS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIjPN1X4ListIU13block_pointerFvvEEEEENS_22__unordered_map_hasherIjS8_NS_4hashIjEENS_8equal_toIjEELb1EEENS_21__unordered_map_equalIjS8_SD_SB_Lb1EEENS_9allocatorIS8_EEED2Ev
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ILi0EEEPKc
- __ZNSt3__112construct_atB8nn190102IN2CA6Render19ContentStreamConfigEJRKS3_EPS3_EEPT_S8_DpOT0_
- __ZNSt3__113__tree_removeB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__114__split_bufferIN1X3RefIN2CA6Render6HandleEEERNS_9allocatorIS6_EEED2Ev
- __ZNSt3__114__thread_proxyB8nn190102INS_5tupleIJNS_10unique_ptrINS_15__thread_structENS_14default_deleteIS3_EEEEMNS_19__async_assoc_stateIP10SILManagerNS_12__async_funcIZL16sil_mgr_instancePvjE3$_0JP19NSMutableDictionaryEEEEEFvvEPSG_EEEEESB_SB_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI20CAFrameIntervalRangeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI22CAFrameIntervalRequestEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN1X3RefIN2CA6Render6HandleEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CA12WindowServer7Display4ModeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CA12WindowServer8FlipBook5FrameEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CA4Vec2IdEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CA4Vec2IiEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CA6Render10MeshVertexEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CA6Render20ContentStreamSurfaceEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CA6Render6Update15SecureIndicatorEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CA6Render7Context4SlotEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CA6Render8MeshEdgeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CA6Render8MeshFaceEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_10unique_ptrIN2CA12WindowServer12IOMFBDisplay9FrameInfoENS_14default_deleteIS6_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_4pairIjNS_6vectorIN2CA4Vec2IiEENS1_IS6_EEEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPKN2CA6Render15EmitterBehavior4EvalEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPN2CA12WindowServer7SurfaceEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPN2CA7Display15DisplayLinkItemEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPNS_4pairIyyEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPPU19objcproto9MTLBuffer11objc_objectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_future_errorB8nn190102ENS_11future_errcE
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP11CAAnimationPKN2CA6Render14BasicAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP11CAAnimationPKN2CA6Render15SpringAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP11CAAnimationPKN2CA6Render17KeyframeAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP12CAShapeLayerPKN2CA6Render10ShapeLayerEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP15CABackdropLayerPKN2CA6Render13BackdropLayerEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP15CAGradientLayerPKN2CA6Render13GradientLayerEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP16CABasicAnimationPKN2CA6Render14BasicAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP16CABasicAnimationPKN2CA6Render15SpringAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP17CAReplicatorLayerPKN2CA6Render15ReplicatorLayerEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP17CASpringAnimationPKN2CA6Render15SpringAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP19CAKeyframeAnimationPKN2CA6Render17KeyframeAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP19CAPropertyAnimationPKN2CA6Render14BasicAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP19CAPropertyAnimationPKN2CA6Render15SpringAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP19CAPropertyAnimationPKN2CA6Render17KeyframeAnimationEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP7CALayerPKN2CA6Render5LayerESF_RKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSP_
- __ZNSt3__122__hash_node_destructorINS_9allocatorINS_11__hash_nodeINS_17__hash_value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEPFvP8CAFilterPKN2CA6Render6FilterEPKNSC_5LayerERKS8_RK25ReverseSerializationStateEEEPvEEEEEclB8nn190102EPSS_
- __ZNSt3__124__sort5_maybe_branchlessB8nn190102INS_17_ClassicAlgPolicyERZN2CA6Render13BackdropGroup15finalize_updateEjbPvE3$_0PNS4_4ItemELi0EEEvT1_SA_SA_SA_SA_T0_
- __ZNSt3__125__throw_bad_function_callB8nn190102Ev
- __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA12WindowServer7Display4ModeEEEbT1_SA_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA6Render12_GLOBAL__N_18IntervalEEEbT1_SA_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERPFbRK22CAFrameIntervalRequestS4_EPS2_EEbT1_S9_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERZ30CAShmemImageQueueCopyImageInfoE3$_0PP23_CAShmemImageQueueImageEEbT1_S7_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERZN2CA3OGL10PathFiller22emit_rects_from_pointsEiiE3$_0PNS4_13ScanlinePointEEEbT1_S9_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERZN2CA6Render13BackdropGroup15finalize_updateEjbPvE3$_0PNS4_4ItemEEEbT1_SA_T0_
- __ZNSt3__127__tree_balance_after_insertB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__134__uninitialized_allocator_relocateB8nn190102INS_9allocatorIN1X3RefIN2CA6Render6HandleEEEEES7_EEvRT_PT0_SC_SC_
- __ZNSt3__15dequeIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE25__maybe_remove_back_spareB8nn190102Eb
- __ZNSt3__15dequeIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEE26__maybe_remove_front_spareB8nn190102Eb
- __ZNSt3__15dequeIPU19objcproto9MTLBuffer11objc_objectNS_9allocatorIS2_EEED2B8nn190102Ev
- __ZNSt3__16vectorIN1X3RefIN2CA6Render6HandleEEENS_9allocatorIS6_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorIN2CA12WindowServer7Display4ModeENS_9allocatorIS4_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CA12WindowServer8FlipBook5FrameENS_9allocatorIS4_EEE18__insert_with_sizeB8nn190102INS_11__wrap_iterIPS4_EESB_EESB_NS9_IPKS4_EET_T0_l
- __ZNSt3__16vectorIN2CA6Render10MeshVertexENS_9allocatorIS3_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CA6Render8MeshEdgeENS_9allocatorIS3_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CA6Render8MeshFaceENS_9allocatorIS3_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7__clearB8nn190102Ev
- __ZNSt3__16vectorINS_13unordered_setIjNS_4hashIjEENS_8equal_toIjEENS_9allocatorIjEEEENS6_IS8_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS_13unordered_setIyNS_4hashIyEENS_8equal_toIyEENS_9allocatorIyEEEENS6_IS8_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS_4pairIjNS0_IN2CA4Vec2IiEENS_9allocatorIS4_EEEEEENS5_IS8_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS_5tupleIJijijNS_13unordered_setIPN2CA6Render6StringENS_4hashIS6_EENS_8equal_toIS6_EENS_9allocatorIS6_EEEEEEENSB_ISE_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorIhNS_9allocatorIhEEE9push_backB8nn190102EOh
- __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA12WindowServer7Display4ModeEEEjT1_SA_SA_T0_
- __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA6Render12_GLOBAL__N_18IntervalEEEjT1_SA_SA_T0_
- __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERPFbRK22CAFrameIntervalRequestS4_EPS2_EEjT1_S9_S9_T0_
- __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERZ30CAShmemImageQueueCopyImageInfoE3$_0PP23_CAShmemImageQueueImageEEjT1_S7_S7_T0_
- __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERZN2CA3OGL10PathFiller22emit_rects_from_pointsEiiE3$_0PNS4_13ScanlinePointEEEjT1_S9_S9_T0_
- __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERZN2CA6Render13BackdropGroup15finalize_updateEjbPvE3$_0PNS4_4ItemEEEjT1_SA_SA_T0_
- __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA12WindowServer7Display4ModeEEEvT1_SA_SA_SA_T0_
- __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA6Render12_GLOBAL__N_18IntervalEEEvT1_SA_SA_SA_T0_
- __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERPFbRK22CAFrameIntervalRequestS4_EPS2_EEvT1_S9_S9_S9_T0_
- __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERZ30CAShmemImageQueueCopyImageInfoE3$_0PP23_CAShmemImageQueueImageEEvT1_S7_S7_S7_T0_
- __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERZN2CA3OGL10PathFiller22emit_rects_from_pointsEiiE3$_0PNS4_13ScanlinePointEEEvT1_S9_S9_S9_T0_
- __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERZN2CA6Render13BackdropGroup15finalize_updateEjbPvE3$_0PNS4_4ItemEEEvT1_SA_SA_SA_T0_
- __ZNSt3__17__sort5B8nn190102INS_17_ClassicAlgPolicyERNS_6__lessIvvEEPN2CA12WindowServer7Display4ModeEEEvT1_SA_SA_SA_SA_T0_
- __ZNSt3__17__sort5B8nn190102INS_17_ClassicAlgPolicyERPFbRK22CAFrameIntervalRequestS4_EPS2_EEvT1_S9_S9_S9_S9_T0_
- __ZNSt3__18_IterOpsINS_17_ClassicAlgPolicyEE9iter_swapB8nn190102IRPN2CA6Render13BackdropGroup4ItemES9_EEvOT_OT0_
- __ZSt28__throw_bad_array_new_lengthB8nn190102v
- __ZThn1016_N2CA12WindowServer11AccelServer10test_fenceEm
- __ZThn1016_N2CA12WindowServer11AccelServer12delete_fenceEm
- __ZThn1016_N2CA12WindowServer11AccelServer15supports_fencesEv
- __ZThn1016_N2CA12WindowServer11AccelServer20flush_command_streamEv
- __ZThn1016_N2CA12WindowServer11AccelServer9set_fenceEv
- __ZZ11init_libedrvE4once
- __ZZ11init_libedrvE6handle
- __ZZ14CADeviceUseVBLE4once
- __ZZ14CADeviceUseVBLE7use_vbl
- __ZZ26CADebugOptionForceWalkTreeE15walking_options
- __ZZ30CADeviceNeedsTripleBufferedTTLE25wants_triple_buffered_ttl
- __ZZ30CADeviceNeedsTripleBufferedTTLE4once
- __ZZ31CADeviceNeedsDisplayWorkaroundsE17needs_workarounds
- __ZZ31CADeviceNeedsDisplayWorkaroundsE4once
- __ZZ33CADeviceHasHeadroomDependentGammaE20unsupported_chip_ids
- __ZZ34CADeviceDisplayNeedsW40aWorkaroundE19workaround_chip_ids
- __ZZ36CADeviceVertexCoordinateSubpixelBitsE17four_bit_chip_ids
- __ZZ40+[CALinearMaskLayer defaultValueForKey:]E5color
- __ZZ40-[CAFenceHandle createXPCRepresentation]E17encode_count_lock
- __ZZ40-[CAFenceHandle createXPCRepresentation]E17last_encode_count
- __ZZL12x_log_crash_PKcPcE7message
- __ZZL16defines_propertyjE5atoms.17228
- __ZZL16defines_propertyjE5atoms.23033
- __ZZL22load_dynamic_vfd_tablevENK3$_0clERKNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEc
- __ZZN2CA12WindowServer11IOMFBServer19frame_info_callbackEP21__IOMobileFramebufferjPK14__CFDictionaryPvE16frame_info_count
- __ZZN2CA12WindowServer12IOMFBDisplay25update_power_state_lockedEbbENK3$_0clEv
- __ZZN2CA12WindowServer12IOMFBDisplay8vrr_rateEvE11initialized
- __ZZN2CA12WindowServer12IOMFBDisplay8vrr_rateEvE4rate
- __ZZN2CA12WindowServer13DisplayLimits21update_display_limitsERKNS0_12AppleDisplayEE10thresholds
- __ZZN2CA12WindowServer13DisplayLimits21update_display_limitsERKNS0_12AppleDisplayEE17index_to_LUT_type
- __ZZN2CA12WindowServer6Server19server_stall_handleEvE10once_token
- __ZZN2CA12WindowServer6Server19server_stall_handleEvE6handle
- __ZZN2CA20HDRProcessorInternal30create_surface_with_forward_dmEPKNS_6Render7SurfaceEPNS1_6UpdateEPKNS1_17DisplayAttributesEbfNS1_12TextureFlagsEbbbbE9sdr_attrs
- __ZZN2CA20HDRProcessorInternal30create_surface_with_forward_dmEPKNS_6Render7SurfaceEPNS1_6UpdateEPKNS1_17DisplayAttributesEbfNS1_12TextureFlagsEbbbbENK3$_0clEPN1X4ListIPNS0_10HDRSurfaceEEESH_
- __ZZN2CA3OGL12MetalContext18get_Opcode_decoderEvE4once
- __ZZN2CA3OGL12MetalContext18get_Opcode_decoderEvE7decoder
- __ZZN2CA3OGL12MetalContext24get_VertexLayout_decoderEvE4once
- __ZZN2CA3OGL12MetalContext24get_VertexLayout_decoderEvE7decoder
- __ZZN2CA3OGL12MetalContext25get_BlendFunction_decoderEvE4once
- __ZZN2CA3OGL12MetalContext25get_BlendFunction_decoderEvE7decoder
- __ZZN2CA3OGL12MetalContext25get_CoordFunction_decoderEvE4once
- __ZZN2CA3OGL12MetalContext25get_CoordFunction_decoderEvE7decoder
- __ZZN2CA3OGL12MetalContext25get_ImageFunction_decoderEvE4once
- __ZZN2CA3OGL12MetalContext25get_ImageFunction_decoderEvE7decoder
- __ZZN2CA3OGL12MetalContext25get_TextureFilter_decoderEvE4once
- __ZZN2CA3OGL12MetalContext25get_TextureFilter_decoderEvE7decoder
- __ZZN2CA3OGL12MetalContext26get_MTLPixelFormat_decoderEvE4once
- __ZZN2CA3OGL12MetalContext26get_MTLPixelFormat_decoderEvE7decoder
- __ZZN2CA3OGL12MetalContext27get_TextureFunction_decoderEvE4once
- __ZZN2CA3OGL12MetalContext27get_TextureFunction_decoderEvE7decoder
- __ZZN2CA3OGL12MetalContext28get_VertexShaderType_decoderEvE4once
- __ZZN2CA3OGL12MetalContext28get_VertexShaderType_decoderEvE7decoder
- __ZZN2CA3OGL12MetalContext29get_offline_compilation_indexEvE10index_once
- __ZZN2CA3OGL12MetalContext29get_offline_compilation_indexEvE5index
- __ZZN2CA3OGL12MetalContext31get_DestinationFunction_decoderEvE4once
- __ZZN2CA3OGL12MetalContext31get_DestinationFunction_decoderEvE7decoder
- __ZZN2CA3OGL7ContextC1EvE4once
- __ZZN2CA3OGL8Renderer6renderEPKNS_6Render6UpdateEmPNS_12WindowServer11SharedEventEE18last_seed_recorded
- __ZZN2CA3OGL8Renderer6renderEPKNS_6Render6UpdateEmPNS_12WindowServer11SharedEventEEN3$_08__invokeERNS_4RectEPv
- __ZZN2CA6Render12_GLOBAL__N_123retain_provider_optionsEbE11initialized
- __ZZN2CA6Render6Update20add_secure_indicatorERKNS1_15SecureIndicatorEE4once
- __ZZNK2CA12WindowServer12IOMFBDisplay14od_lut_versionEvE13radar_numbers
- __ZZNK2CA3OGL18GaussianBlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfbPKNS_11ColorMatrixEPKNS_5ShapeESI_PfE10all_linear
- __ZZNK2CA3OGL18GaussianBlurFilter6renderEPKNS_6Render6FilterEPKNS0_5LayerERNS0_7ContextEfPNS0_7SurfaceEfbPKNS_11ColorMatrixEPKNS_5ShapeESI_PfE11initialized
- __ZZNK2CA6Render12GainMapLayer4showEjjE10mode_names
- __ZZNK2CA6Render5Layer4showEjjE5names
- __ZZNK2CA6Render9Animation4showEjjE10calc_modes
- __ZZZ22CADeviceNeedsLumaBoostEUb0_E13boost_devices
- __ZZZ25CADeviceSupportsHWGainMapEUb1_E13crete_devices
- __ZZZ25CADeviceSupportsHWGainMapEUb1_E7devices
- __ZZZ31CADeviceNeedsDisplayWorkaroundsEUb_E18workaround_devices
- __Znwm
- ___30-[CADisplay supportedHDRModes]_block_invoke
- ___Block_byref_object_copy_.13196
- ___Block_byref_object_copy_.20491
- ___Block_byref_object_copy_.370
- ___Block_byref_object_copy_.372
- ___Block_byref_object_dispose_.13197
- ___Block_byref_object_dispose_.20492
- ___Block_byref_object_dispose_.371
- ___Block_byref_object_dispose_.373
- ___CADeviceNeedsDisplayWorkarounds_block_invoke
- ___CADeviceNeedsTripleBufferedTTL_block_invoke
- ___CADeviceUseVBL_block_invoke
- ____Z11init_libedrv_block_invoke
- ____ZL13emit_tailspinP8NSStringjjijPKc_block_invoke.87
- ____ZL15ensure_displaysv_block_invoke.924
- ____ZN2CA11Transaction9add_fenceEjP13CAFenceHandleU13block_pointerFvvE_block_invoke
- ____ZN2CA12ColorProgram7Program13color_programEPK21CGColorConversionInfoP12CGColorSpacei28CGColorConversionIterateTypebijffRb_block_invoke
- ____ZN2CA12ColorProgram7Program13color_programEPK21CGColorConversionInfoP12CGColorSpacei28CGColorConversionIterateTypebijffRb_block_invoke.30
- ____ZN2CA12ColorProgram7Program13color_programEPK21CGColorConversionInfoP12CGColorSpacei28CGColorConversionIterateTypebijffRb_block_invoke.35
- ____ZN2CA12ColorProgram7Program13color_programEPK21CGColorConversionInfoP12CGColorSpacei28CGColorConversionIterateTypebijffRb_block_invoke_2
- ____ZN2CA12WindowServer11IOMFBServer21set_calibration_phaseEjj_block_invoke
- ____ZN2CA12WindowServer11IOMFBServer33update_orientation_with_hid_eventEP20__IOHIDServiceClientP12__IOHIDEvent_block_invoke
- ____ZN2CA12WindowServer12IOMFBDisplay21set_tonemapping_stateEPNS_6Render6UpdateEPKNS0_7SurfaceEjPP12CGColorSpace_block_invoke.62
- ____ZN2CA12WindowServer15DebugBrightnessEd_block_invoke.233
- ____ZN2CA12WindowServer6Server19server_stall_handleEv_block_invoke
- ____ZN2CA12WindowServer6Server27update_display_modes_lockedEb_block_invoke
- ____ZN2CA12WindowServer6ServerC2EPNS0_7DisplayEPK10__CFString_block_invoke.7
- ____ZN2CA20HDRProcessorInternal30configure_display_pipe_tonemapEP11__IOSurfacejPKNS_6Render17DisplayAttributesEPP12CGColorSpaceU13block_pointerFvP18IOMFBToneMapConfigEU13block_pointerFv13IOMFBCurveLocPK14IOMFBCurveDataEU13block_pointerFv14IOMFBICCMatLocPK16IOMFBColorMatrixE_block_invoke
- ____ZN2CA20HDRProcessorInternal30create_surface_with_forward_dmEPKNS_6Render7SurfaceEPNS1_6UpdateEPKNS1_17DisplayAttributesEbfNS1_12TextureFlagsEbbbb_block_invoke
- ____ZN2CA3OGL12MetalContext18get_Opcode_decoderEv_block_invoke
- ____ZN2CA3OGL12MetalContext22calculate_average_lumaEPNS0_7SurfaceEU13block_pointerFvfE_block_invoke
- ____ZN2CA3OGL12MetalContext24get_VertexLayout_decoderEv_block_invoke
- ____ZN2CA3OGL12MetalContext25get_BlendFunction_decoderEv_block_invoke
- ____ZN2CA3OGL12MetalContext25get_CoordFunction_decoderEv_block_invoke
- ____ZN2CA3OGL12MetalContext25get_ImageFunction_decoderEv_block_invoke
- ____ZN2CA3OGL12MetalContext25get_TextureFilter_decoderEv_block_invoke
- ____ZN2CA3OGL12MetalContext26get_MTLPixelFormat_decoderEv_block_invoke
- ____ZN2CA3OGL12MetalContext27get_TextureFunction_decoderEv_block_invoke
- ____ZN2CA3OGL12MetalContext28get_VertexShaderType_decoderEv_block_invoke
- ____ZN2CA3OGL12MetalContext29get_offline_compilation_indexEv_block_invoke
- ____ZN2CA3OGL12MetalContext31get_DestinationFunction_decoderEv_block_invoke
- ____ZN2CA3OGL12MetalContext5flushEb_block_invoke.75
- ____ZN2CA3OGL12MetalContext5flushEb_block_invoke.77
- ____ZN2CA3OGL7ContextC2Ev_block_invoke
- ____ZN2CA6Render5Fence11Transaction8Observer8activateENSt3__113unordered_setIyNS4_4hashIyEENS4_8equal_toIyEENS4_9allocatorIyEEEEPFvPS3_RKSC_djyEPFvSD_SF_jjEPFvSD_SF_E_block_invoke.11
- ____ZN2CA6Render5Fence11Transaction8Observer8activateENSt3__113unordered_setIyNS4_4hashIyEENS4_8equal_toIyEENS4_9allocatorIyEEEEPFvPS3_RKSC_djyEPFvSD_SF_jjEPFvSD_SF_E_block_invoke.7
- ____ZN2CA6Render6Update20add_secure_indicatorERKNS1_15SecureIndicatorE_block_invoke
- ____ZN2CA7Context18commit_transactionEPNS_11TransactionEdPd_block_invoke.49
- ____ZN2CA7Context18commit_transactionEPNS_11TransactionEdPd_block_invoke.54
- ____ZN2CA7Context18commit_transactionEPNS_11TransactionEdPd_block_invoke_2.57
- ___block_descriptor_163_e8_32o40b_e5_v8?0ls32l8s40l8
- ___block_descriptor_172_e8_32c39_ZTSN2CA12WindowServer7Display7ModeSetE128c47_ZTSN2CA12WindowServer7Display14EDIDAttributesE_e21_B24?0"NSString"816l
- ___block_descriptor_32_e86_B24?0"CALocalDisplay"8^{?=III^{__CFString}^{__CFString}^{__CFString}^QQQQ^?dddIIB}16l
- ___block_descriptor_40_e8_32o_e29_v16?0r^{?=IIQQQQIBBBfffQIB}8ls32l8
- ___block_descriptor_40_e8_32o_e53_v92?0I8I12Q16Q24Q32Q40I48B52B56B60f64f68f72Q76I84B88ls32l8
- ___block_descriptor_48_e8_32b_e67_B16?0^{?=III^{__CFString}^{__CFString}^{__CFString}^QQQQ^?dddIIB}8ls32l8
- ___block_descriptor_92_e8_32o_e5_v8?0ls32l8
- ___block_descriptor_tmp.1.17099
- ___block_descriptor_tmp.1.18211
- ___block_descriptor_tmp.1.19843
- ___block_descriptor_tmp.10007
- ___block_descriptor_tmp.101.17507
- ___block_descriptor_tmp.102.21893
- ___block_descriptor_tmp.106
- ___block_descriptor_tmp.108.17326
- ___block_descriptor_tmp.109
- ___block_descriptor_tmp.11.18225
- ___block_descriptor_tmp.1117
- ___block_descriptor_tmp.113
- ___block_descriptor_tmp.11307
- ___block_descriptor_tmp.115
- ___block_descriptor_tmp.116
- ___block_descriptor_tmp.11793
- ___block_descriptor_tmp.118
- ___block_descriptor_tmp.12.20496
- ___block_descriptor_tmp.12.23384
- ___block_descriptor_tmp.120
- ___block_descriptor_tmp.12140
- ___block_descriptor_tmp.127
- ___block_descriptor_tmp.132
- ___block_descriptor_tmp.136
- ___block_descriptor_tmp.13635
- ___block_descriptor_tmp.13753
- ___block_descriptor_tmp.14
- ___block_descriptor_tmp.14.17370
- ___block_descriptor_tmp.14.966
- ___block_descriptor_tmp.14007
- ___block_descriptor_tmp.145
- ___block_descriptor_tmp.14733
- ___block_descriptor_tmp.15.12152
- ___block_descriptor_tmp.155
- ___block_descriptor_tmp.155.16764
- ___block_descriptor_tmp.158
- ___block_descriptor_tmp.15861
- ___block_descriptor_tmp.167
- ___block_descriptor_tmp.167.12294
- ___block_descriptor_tmp.16830
- ___block_descriptor_tmp.17.18227
- ___block_descriptor_tmp.17098
- ___block_descriptor_tmp.17402
- ___block_descriptor_tmp.176
- ___block_descriptor_tmp.179
- ___block_descriptor_tmp.18038
- ___block_descriptor_tmp.18152
- ___block_descriptor_tmp.18206
- ___block_descriptor_tmp.18300
- ___block_descriptor_tmp.18556
- ___block_descriptor_tmp.1864
- ___block_descriptor_tmp.189
- ___block_descriptor_tmp.19.22454
- ___block_descriptor_tmp.192
- ___block_descriptor_tmp.19247
- ___block_descriptor_tmp.19842
- ___block_descriptor_tmp.199
- ___block_descriptor_tmp.2.5097
- ___block_descriptor_tmp.201
- ___block_descriptor_tmp.20494
- ___block_descriptor_tmp.20565
- ___block_descriptor_tmp.208
- ___block_descriptor_tmp.21
- ___block_descriptor_tmp.214
- ___block_descriptor_tmp.218
- ___block_descriptor_tmp.21970
- ___block_descriptor_tmp.22450
- ___block_descriptor_tmp.230
- ___block_descriptor_tmp.23372
- ___block_descriptor_tmp.246
- ___block_descriptor_tmp.253
- ___block_descriptor_tmp.26
- ___block_descriptor_tmp.2673
- ___block_descriptor_tmp.279
- ___block_descriptor_tmp.28
- ___block_descriptor_tmp.28.22494
- ___block_descriptor_tmp.2839
- ___block_descriptor_tmp.285
- ___block_descriptor_tmp.288
- ___block_descriptor_tmp.294
- ___block_descriptor_tmp.3.17407
- ___block_descriptor_tmp.3.5911
- ___block_descriptor_tmp.3.9119
- ___block_descriptor_tmp.30
- ___block_descriptor_tmp.300
- ___block_descriptor_tmp.306
- ___block_descriptor_tmp.309
- ___block_descriptor_tmp.33
- ___block_descriptor_tmp.333
- ___block_descriptor_tmp.3354
- ___block_descriptor_tmp.34
- ___block_descriptor_tmp.349
- ___block_descriptor_tmp.35.12176
- ___block_descriptor_tmp.350
- ___block_descriptor_tmp.3558
- ___block_descriptor_tmp.365
- ___block_descriptor_tmp.373
- ___block_descriptor_tmp.377
- ___block_descriptor_tmp.384
- ___block_descriptor_tmp.390
- ___block_descriptor_tmp.395
- ___block_descriptor_tmp.4.10016
- ___block_descriptor_tmp.4.18214
- ___block_descriptor_tmp.402
- ___block_descriptor_tmp.4280
- ___block_descriptor_tmp.435
- ___block_descriptor_tmp.44.13883
- ___block_descriptor_tmp.444
- ___block_descriptor_tmp.449
- ___block_descriptor_tmp.467
- ___block_descriptor_tmp.48
- ___block_descriptor_tmp.482
- ___block_descriptor_tmp.487
- ___block_descriptor_tmp.4949
- ___block_descriptor_tmp.5.10017
- ___block_descriptor_tmp.5.18167
- ___block_descriptor_tmp.50
- ___block_descriptor_tmp.50.13724
- ___block_descriptor_tmp.5100
- ___block_descriptor_tmp.5402
- ___block_descriptor_tmp.548
- ___block_descriptor_tmp.56
- ___block_descriptor_tmp.57
- ___block_descriptor_tmp.57.12200
- ___block_descriptor_tmp.5788
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.5894
- ___block_descriptor_tmp.5915
- ___block_descriptor_tmp.6071
- ___block_descriptor_tmp.61.21357
- ___block_descriptor_tmp.611
- ___block_descriptor_tmp.6195
- ___block_descriptor_tmp.628
- ___block_descriptor_tmp.630
- ___block_descriptor_tmp.633
- ___block_descriptor_tmp.647
- ___block_descriptor_tmp.6580
- ___block_descriptor_tmp.6735
- ___block_descriptor_tmp.69
- ___block_descriptor_tmp.71
- ___block_descriptor_tmp.7263
- ___block_descriptor_tmp.73
- ___block_descriptor_tmp.7621
- ___block_descriptor_tmp.77
- ___block_descriptor_tmp.78.14774
- ___block_descriptor_tmp.7814
- ___block_descriptor_tmp.8.16833
- ___block_descriptor_tmp.8.18171
- ___block_descriptor_tmp.83
- ___block_descriptor_tmp.84.16856
- ___block_descriptor_tmp.85
- ___block_descriptor_tmp.8613
- ___block_descriptor_tmp.8807
- ___block_descriptor_tmp.9.18178
- ___block_descriptor_tmp.9.1873
- ___block_descriptor_tmp.9115
- ___block_descriptor_tmp.946
- ___block_descriptor_tmp.96
- ___block_descriptor_tmp.99
- ___block_literal_global.10005
- ___block_literal_global.10080
- ___block_literal_global.103
- ___block_literal_global.10567
- ___block_literal_global.108
- ___block_literal_global.1093
- ___block_literal_global.11
- ___block_literal_global.1115
- ___block_literal_global.11184
- ___block_literal_global.11884
- ___block_literal_global.120
- ___block_literal_global.12138
- ___block_literal_global.129
- ___block_literal_global.13.18223
- ___block_literal_global.13277
- ___block_literal_global.134
- ___block_literal_global.134.23181
- ___block_literal_global.13633
- ___block_literal_global.13751
- ___block_literal_global.141.23106
- ___block_literal_global.147
- ___block_literal_global.14731
- ___block_literal_global.15614
- ___block_literal_global.157
- ___block_literal_global.15890
- ___block_literal_global.16
- ___block_literal_global.1630
- ___block_literal_global.164
- ___block_literal_global.169
- ___block_literal_global.169.12292
- ___block_literal_global.16946
- ___block_literal_global.17400
- ___block_literal_global.18036
- ___block_literal_global.181
- ___block_literal_global.18130
- ___block_literal_global.18150
- ___block_literal_global.18204
- ___block_literal_global.18298
- ___block_literal_global.18401
- ___block_literal_global.18548
- ___block_literal_global.1861
- ___block_literal_global.18801
- ___block_literal_global.197
- ___block_literal_global.19723
- ___block_literal_global.19901
- ___block_literal_global.203
- ___block_literal_global.20493
- ___block_literal_global.20557
- ___block_literal_global.21.22452
- ___block_literal_global.210
- ___block_literal_global.21356
- ___block_literal_global.216
- ___block_literal_global.2162
- ___block_literal_global.220
- ___block_literal_global.22431
- ___block_literal_global.22444
- ___block_literal_global.232
- ___block_literal_global.23201
- ___block_literal_global.23308
- ___block_literal_global.2333
- ___block_literal_global.23382
- ___block_literal_global.2354
- ___block_literal_global.239
- ___block_literal_global.2444
- ___block_literal_global.246
- ___block_literal_global.248
- ___block_literal_global.255
- ___block_literal_global.2570
- ___block_literal_global.2588
- ___block_literal_global.262
- ___block_literal_global.2627
- ___block_literal_global.2671
- ___block_literal_global.268
- ___block_literal_global.2709
- ___block_literal_global.2786
- ___block_literal_global.281
- ___block_literal_global.2837
- ___block_literal_global.287
- ___block_literal_global.290
- ___block_literal_global.292
- ___block_literal_global.2981
- ___block_literal_global.30
- ___block_literal_global.302
- ___block_literal_global.306
- ___block_literal_global.308
- ___block_literal_global.311
- ___block_literal_global.312
- ___block_literal_global.3168
- ___block_literal_global.335
- ___block_literal_global.3352
- ___block_literal_global.352
- ___block_literal_global.3554
- ___block_literal_global.367
- ___block_literal_global.37.12174
- ___block_literal_global.37.6749
- ___block_literal_global.371
- ___block_literal_global.375
- ___block_literal_global.379
- ___block_literal_global.386
- ___block_literal_global.392
- ___block_literal_global.397
- ___block_literal_global.4016
- ___block_literal_global.404
- ___block_literal_global.424
- ___block_literal_global.4265
- ___block_literal_global.437
- ___block_literal_global.446
- ___block_literal_global.447
- ___block_literal_global.46.13879
- ___block_literal_global.469
- ___block_literal_global.484
- ___block_literal_global.489
- ___block_literal_global.4947
- ___block_literal_global.5.17405
- ___block_literal_global.5.9112
- ___block_literal_global.5096
- ___block_literal_global.51
- ___block_literal_global.512
- ___block_literal_global.518
- ___block_literal_global.519
- ___block_literal_global.52
- ___block_literal_global.52.13719
- ___block_literal_global.521
- ___block_literal_global.523
- ___block_literal_global.525
- ___block_literal_global.529
- ___block_literal_global.5371
- ___block_literal_global.5400
- ___block_literal_global.5784
- ___block_literal_global.5892
- ___block_literal_global.59
- ___block_literal_global.5913
- ___block_literal_global.5971
- ___block_literal_global.6069
- ___block_literal_global.6193
- ___block_literal_global.62
- ___block_literal_global.6578
- ___block_literal_global.6752
- ___block_literal_global.71
- ___block_literal_global.7257
- ___block_literal_global.73
- ___block_literal_global.74
- ___block_literal_global.75
- ___block_literal_global.7619
- ___block_literal_global.7804
- ___block_literal_global.787
- ___block_literal_global.80.14772
- ___block_literal_global.83
- ___block_literal_global.8422
- ___block_literal_global.8610
- ___block_literal_global.8805
- ___block_literal_global.894
- ___block_literal_global.901
- ___block_literal_global.904
- ___block_literal_global.9113
- ___block_literal_global.921
- ___block_literal_global.926
- ___block_literal_global.942
- ___block_literal_global.943
- ___block_literal_global.945
- ___block_literal_global.98
- ___block_literal_global.98.12238
- ___copy_helper_block_e8_32c39_ZTSN2CA12WindowServer7Display7ModeSetE128c47_ZTSN2CA12WindowServer7Display14EDIDAttributesE
- ___destroy_helper_block_e8_32c39_ZTSN2CA12WindowServer7Display7ModeSetE128
- ___stderrp
- ___stdoutp
- __os_log_default
- _ca_debug_lut_changed
- _compression_decode_buffer
- _fprintf
- _fseeko
- _gCRAnnotations
- _localtime_r
- _objc_msgSend$dataWithBytesNoCopy:length:
- _objc_msgSend$dataWithContentsOfFile:options:error:
- _objc_msgSend$didChangeToState:seed:result:
- _objc_msgSend$finishExternalUpdate:withFlags:debugInfo:
- _objc_msgSend$getBytes:range:
- _objc_msgSend$newComputePipelineStateWithFunction:error:
- _objc_msgSend$pathForResource:ofType:
- _setlinebuf
- _strftime
- _time
- _vfprintf
- _wmemchr
- _work_interval_instance_update
- _x_list_copy
- _x_log_
- _x_log_begin
- _x_log_category_CADebug
- _x_log_category_api
- _x_log_category_brightness
- _x_log_category_cg
- _x_log_category_color
- _x_log_category_display_state
- _x_log_category_filmgrain
- _x_log_category_flatten
- _x_log_category_flipbook
- _x_log_category_frame_rate
- _x_log_category_occlusion
- _x_log_category_ogl
- _x_log_category_ogl_metal
- _x_log_category_ogl_opengl
- _x_log_category_render
- _x_log_category_secure_indicators
- _x_log_category_security_analysis
- _x_log_category_sharedevent
- _x_log_category_states
- _x_log_category_utilities
- _x_log_category_video_tonemapping
- _x_log_category_windowserver
- _x_log_crash
- _x_log_end_free_
- _x_log_hook_p
- _x_logv
- _x_set_log_file
- _x_set_log_filename
- _x_stream_push
CStrings:
+ "\t\t ImplicitPowerAssertion\n"
+ "\t\t%d, %d, %s, %d, %s, Display::%s, Display::%s, %s, %s\n"
+ "\tFlex Luminance Scaling params:\n\t\tsource headroom = % 3.10f\n\t\ttarget headroom = % 3.10f\n\t\tcoefficients[0] = % 3.10f\n\t\tcoefficients[1] = % 3.10f\n\t\tcoefficients[2] = % 3.10f\n\t\tcoefficients[3] = % 3.10f\n\t\tcoefficients[4] = % 3.10f\n\t\tFlexGTCTableCount = %zu\n\t\tFlexGTCTable = %p, [%f, %f, ..., %f, %f]\n"
+ "\tcloningState: %s\n"
+ "\tcloningState: %s -> %s\n"
+ "\tinternal modes:\n"
+ "\n%s"
+ "\nCA Shared Events per Surface Free:\n"
+ "\nCA Shared Events per Surface Inuse:\n"
+ "\nCA Shared Events per Surface Shared with Render::Surface:\n"
+ "\nFilter A:"
+ "     "
+ "     \n"
+ "          Time                      Usage              Operation Access       Value        Completed\n"
+ "    Surface 0x%x (%.2lf %s) @ %f (%s), reuse %u, dirty res (%dx%d), alloc res (%dx%d)\n"
+ "    Surface 0x%x (%.2lf %s) @ %f (%s), seed %u enqueued\n"
+ "  Pool Current Memory: %.2lf %s / Max Pool Memory:  %.2lf %s)\n"
+ "  Total frames allocated: %u\n"
+ " (tint %.3g %.3g %.3g %.3g %.3g)"
+ " - %lu Images (%s%.2f %s)\n"
+ " IOSurfaceID=%{public, name=IOSurfaceID}#x ValueCompleted=%{public, name=ValueCompleted}#llx AllFinished=%{public, bool, name=AllFinished}d"
+ "!_reply_port"
+ "!flattened_cache->lookup (cache_id)"
+ "!xPort"
+ "\"Duplicated Entry !!\" && map.map.find (\"allowsColorMatching\") == map.map.end ()"
+ "\"Duplicated Entry !!\" && map.map.find (\"contentsCDRStrength\") == map.map.end ()"
+ "%20s  SharedEvent IOSurface ID: 0x%16llx  Usage: %35s  Operation: %9s  Access: %6s  Value: 0x%16llx\n"
+ "%20s %35s %9s %6s 0x%16llx %9s\n"
+ "%@, "
+ "%d by %d image is too large for software renderer, ignoring\n"
+ "%f %x \"%s\" (%p): adding %p:\n%s"
+ "%f %x \"%s\" (%p): collecting %p (t %f; speed %g; eval %u; frames %u):\n%s"
+ "%f %x \"%s\" (%p): not adding %p:\n%s"
+ "%f %x \"%s\" (%p): removing %p (eval %u; frames %u):\n%s"
+ "%f %x \"%s\" (%p): removing all:\n%s"
+ "%f %x \"%s\" (%p): replacing %p (eval %u; frames %u):\n%s"
+ "%s - %p, size = %zu, expected = %zu"
+ "%s : %d"
+ "%zu start ctxs [%s"
+ "(%s) signal clients display %u %s changed to %s"
+ "(allowedContentsHideSublayers true)"
+ "(allowsColorMatching false)"
+ "(allowsCornerContentsEdgeEffects true)"
+ "(allowsFilteredLuma true)"
+ "(angle %g)"
+ "(backgroundColor (%.3g %.3g %.3g %.0g %.3g))"
+ "(borderColor (%.3g %.3g %.3g %.0g %.3g))"
+ "(color (%.3g %.3g %.3g %.0g %.3g))"
+ "(contents-one-value-distance %g)"
+ "(contents-zero-value-distance %g)"
+ "(contentsCDRStrength %g)"
+ "(contentsHeadroom %g)"
+ "(contentsMultiplyColor %.3g %.3g %.3g %.3g %.3g)"
+ "(curvature %g)"
+ "(effect fill"
+ "(effect glass-displacement"
+ "(effect glass-highlight"
+ "(effect gradient)"
+ "(effect key-fill-highlight"
+ "(effect output"
+ "(effect shadow"
+ "(effect visualize)"
+ "(effect-offset %g)"
+ "(fillAmount %g)"
+ "(fillAngle %g)"
+ "(fillColor %.3g %.3g %.3g %.3g %.3g)"
+ "(fillColor (%.3g %.3g %.3g %.0g), gain (%.3g))"
+ "(fillHeight %g)"
+ "(fillHeightOffset %g)"
+ "(fillHeightScale %g)"
+ "(fillSpread %g)"
+ "(fillSpreadOffset %g)"
+ "(fillSpreadScale %g)"
+ "(fully-occluded)"
+ "(height %g)"
+ "(hit-tests-as-fill true)"
+ "(hosted-ctx-can-zombify)"
+ "(ignore-animations)"
+ "(keyAmount %g)"
+ "(keyAngle %g)"
+ "(keyColor (%.3g %.3g %.3g %.0g), gain (%.3g))"
+ "(keyHeight %g)"
+ "(keyHeightOffset %g)"
+ "(keyHeightScale %g)"
+ "(keySpread %g)"
+ "(keySpreadOffset %g)"
+ "(keySpreadScale %g)"
+ "(lumaSubrect [%g %g; %g %g])"
+ "(lumaUpdateRate %g)"
+ "(maskOffset %g)"
+ "(maximum %g)"
+ "(merge-elements %g)"
+ "(minimum %g)"
+ "(mode "
+ "(mode contents)"
+ "(offset [%g %g])"
+ "(operation subtraction)"
+ "(post-change-duration %f)"
+ "(preferredDynamicRange %s)"
+ "(radius %g)"
+ "(rasterizeInParentSpace true)"
+ "(rimColor (%.3g %.3g %.3g %.0g %.3g))"
+ "(sdf-element-layer"
+ "(sdf-layer"
+ "(shadowColor (%.3g %.3g %.3g %.0g %.3g))"
+ "(shadowEffectsOnWindowMaskOnly true)"
+ "(skipHitTesting true)"
+ "(smoothness %g)"
+ "(sourceLayerOpacityScale %g)"
+ "(strokeColor %.3g %.3g %.3g %.3g %.3g)"
+ "(sublayers (array"
+ "(t & MACH_PORT_TYPE_DEAD_NAME) == MACH_PORT_TYPE_DEAD_NAME"
+ "(window-layer"
+ "(zombificationMode always)"
+ "(zombificationMode default)"
+ "(zombificationMode never)"
+ "+[CAFenceHandle handleWithPort:data:error:]"
+ "+[CAHostingToken _newTokenWithPort:sid:cid:]"
+ "+[CAHostingToken tokenWithPort:data:error:]"
+ "----------------------- ------------------------------ --------- ------ ------------------ ---------\n"
+ "-[CAFenceHandle encodeWithBlock:]"
+ "-[CAFenceResolution _initWithTime:]"
+ "-[CAFenceResolution init]"
+ "-[CAFlipBook(Private) _notifyRenderCompletedForTime:status:frameId:oldestFrameId:apl:aplDimming:memoryUsage:rawSurfacePort:rawSurfaceDestRect:]"
+ "-[CAHostingToken _initWithPort:data:]"
+ "-[CAHostingToken _initWithPort:data:lenient:error:]"
+ "-[CAHostingToken encodeWithBlock:]"
+ "-[CAHostingToken init]"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-animation.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-array.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-backdrop-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-car-play-region-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-coding.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-distance-field-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-emitter-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-filter.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-function.mm"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-gain-map-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-gradient-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-image-compressed.mm"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-image-queue.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-image.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-key-value.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-layer-host.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-match-animation.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-media-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-mesh-transform.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-object.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-path.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-pattern.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-pixel-buffer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-portal-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-proxy.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-replicator-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-sdf-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-secure-indicator-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-shape-layer.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-shmem.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-string.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-surface.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-texture.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-timing.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-vector.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/QuartzCore/LayerKit/render/render-window-layer.cpp"
+ "23A5260l"
+ "<CAFenceResolution: %0.6f>"
+ "<CAFlipBook: maximumSize %zu, maximumPoolMemory %zu, overAllocationFactor %f, generation %u, contextId 0x%x>"
+ "<CAHostingToken:%u-%i-%x %@>"
+ "<CAHostingToken:%u-%i-%x p=%x>"
+ "<CAHostingToken:%u-%i-%x>"
+ "<CAHostingToken:%x>"
+ "<ctx:%#x> cannot zombify, host is dead"
+ "<ctx:%#x> host invalidated, destroying zombie"
+ "<ctx:%#x> zombified context"
+ "== Context %lu Image Cache - %lu Images (%s%.2f %s)\n"
+ "=== "
+ "@\"<CALayoutManager>\""
+ "@\"<MTLTexture>\"24@0:8@\"MTLTextureViewDescriptor\"16"
+ "@\"NSObject<OS_xpc_object>\""
+ "@32@0:8@16^@24"
+ "@36@0:8I16@20^@28"
+ "@40@0:8^{_CAMetalDrawablePrivate={Atomic={?=i}}IIIQQQQd^{_CAMetalLayerPrivate}^{__IOSurface}@@@Q^{CGColorSpace}@@Cb1b1b1b1b1b1b1b1}16@24d32"
+ "Async render times array exceed maximum size."
+ "Asynchronous"
+ "AsynchronousItem"
+ "B16@?0^{?=III^{__CFString}^{__CFString}^{__CFString}^QQQQ^?dddIIB^{__CFArray}^{__CFData}^{__CFData}}8"
+ "B24@?0@\"CALocalDisplay\"8^{?=III^{__CFString}^{__CFString}^{__CFString}^QQQQ^?dddIIB^{__CFArray}^{__CFData}^{__CFData}}16"
+ "Blending"
+ "Bumped indicator t:%u to GPU render due to missing slot"
+ "Bumped indicator to GPU render due to HW limit reached"
+ "CA SDFGenerator Output"
+ "CAAllowMetalFrameInterpolation"
+ "CABackingStoreBeginUpdateWithFormat"
+ "CACGUtil.cpp"
+ "CADisplay %d Supports Blending: %s"
+ "CADisplay %d Supports Detaching but not Blending"
+ "CADisplayCloningStateDidChange display_id=%u, state=%s, seed=%u, result=%s"
+ "CADisplayStateControl %s=%s display_id=%u seed=%u interrupted"
+ "CADisplayStateControl %s=%s display_id=%u seed=%u result=%s"
+ "CADisplayStateControl %s=%s, display_id=%u, seed=%u, completion=%p"
+ "CADisplayStateControl acquireWirelessDisplayStateControl for display %u"
+ "CADisplayStateDidChange display_id=%u, state=%s, seed=%u, result=%s"
+ "CAFenceResolution"
+ "CAFenceResolution.mm"
+ "CAFlipBook initWithDisplayId=%u called but a global flipbook already exist."
+ "CAFlipBook.%i.renderNotification"
+ "CAGetColorSpace"
+ "CAHostingToken"
+ "CAHostingToken.m"
+ "CAHostingTokenDataIsValid (data)"
+ "CAImageQueueSetOwner() is deprecated and does nothing. Please stop calling this method.\n"
+ "CALayerInvalidCGPath"
+ "CALocalDisplayUpdateBlock returned NO\n"
+ "CAML error:%d: %s"
+ "CAML warning:%d: %s"
+ "CAMetalLayer.residencySet"
+ "CAPackage parsing exception %@"
+ "CARender statistics:\n%s"
+ "CARenderServerSetMessageFile() is deprecated. Use libtrace tools instead."
+ "CARender[%p]:\n%s"
+ "CASDFEffect"
+ "CASDFElementLayer"
+ "CASDFFillEffect"
+ "CASDFGenerator"
+ "CASDFGeneratorRequest"
+ "CASDFGlassDisplacementEffect"
+ "CASDFGlassHighlightEffect"
+ "CASDFGradientEffect"
+ "CASDFKeyFillHighlightEffect"
+ "CASDFLayer"
+ "CASDFOutputEffect"
+ "CASDFShadowEffect"
+ "CASDFVisualizationEffect"
+ "CASetMessageFile() is deprecated. Use libtrace tools instead."
+ "CASetMessageFunction() is deprecated. Use libtrace tools instead."
+ "CASpringAnimation damping must be greater than or equal to 0."
+ "CASpringAnimation mass must be greater than 0."
+ "CASpringAnimation stiffness must be greater than 0."
+ "CASupportsGCP"
+ "CAWindowLayer"
+ "CAWorkInterval.cpp"
+ "CA_BACKDROP_LUMA_RATE_OVERRIDE"
+ "CA_BUMP_METAL_LAYER_DRAWABLE_COUNT"
+ "CA_CDR_STRENGTH_OVERRIDE"
+ "CA_COLOR_SDF_GROUP"
+ "CA_CONTENT_AVERAGE_LIGHT_LEVEL_OVERRIDE"
+ "CA_CONTENT_LIGHT_LEVEL_OVERRIDE"
+ "CA_DISABLE_ADAPTIVE_GAIN"
+ "CA_DISABLE_ARBITRARY_PRESENTATION_LATENCY"
+ "CA_DISABLE_ASYNC_SWAP_BEGIN"
+ "CA_DISABLE_COMPUTE_DOWNSAMPLE_BLUR"
+ "CA_DISABLE_CONSTRAINED_STILLS"
+ "CA_DISABLE_CONTRAST_PRESERVATION"
+ "CA_DISABLE_FAST_SWAP_WAIT"
+ "CA_DISABLE_FILTERED_LUMA"
+ "CA_DISABLE_FLATTEN_SURFACE_REUSE"
+ "CA_DISABLE_FRAME_DOUBLING"
+ "CA_DISABLE_FULLSCREEN_LOW_LATENCY_ELIGIBLE_PID"
+ "CA_DISABLE_LOSSY_TEXTURES"
+ "CA_DISABLE_LUMA_COMPUTE"
+ "CA_DISABLE_MIP_SKIP"
+ "CA_DISABLE_OCCLUSION"
+ "CA_DISABLE_REMOTE_EFFECTS_UPDATES"
+ "CA_DISABLE_SEPARATED_SHADOWS"
+ "CA_DISABLE_SERVER_TIMER_EARLY_WAKEUP"
+ "CA_DISABLE_SWAP_LAYERS"
+ "CA_DISABLE_WINDOW_FLATTENING"
+ "CA_DISPLAY_LINK_SHIFT"
+ "CA_EDR_STRENGTH_OVERRIDE"
+ "CA_EMIT_CLIENT_EDR_REQUEST_DEBUG_SIGNPOSTS"
+ "CA_ENABLE_CC_EDGE_EFFECTS"
+ "CA_ENABLE_PREFERS_TRIPLE_BUFFERED_LATENCY"
+ "CA_ENABLE_PRESENTATION_LATENCY_TTL"
+ "CA_ENABLE_SDF_GROUPS"
+ "CA_ENABLE_WORKGROUP_INTERVAL"
+ "CA_FLATTEN_REUSE_POOL_SIZE"
+ "CA_FORCE_CIF10_FRAMEBUFFER"
+ "CA_FORCE_IMMEDIATE_RENDER_ELIGIBLE"
+ "CA_FORCE_TRIPLE_BUFFERED_LATENCY"
+ "CA_FP16_MIN_HEADROOM"
+ "CA_GCP_GAMMA_OVERRIDE"
+ "CA_HDR_SCREEN_RECORDING_TARGET"
+ "CA_PRINT_HEADROOM_TRACKING"
+ "CA_PRINT_ZOMBIE"
+ "CA_copyRenderKeyPathValueArray"
+ "CG image cache at time %f:\n%s"
+ "CGPathRef with unreasonable count: [Elements: %ld, Points: %ld]"
+ "Cache"
+ "CarPlay"
+ "Context is a zombie! cid=%x"
+ "Contrast Preservation"
+ "CoreAnimation: %s (%u) : %s"
+ "CoreAnimation: Cannot send %zu bytes to the server. This exceeds mach ool capabilities!"
+ "CoreAnimation: Client mach port creation failed 0x%x : %s"
+ "CoreAnimation: Could not create backwardDM display properties!"
+ "CoreAnimation: Couldn't allocate buffer of %zu bytes for message!"
+ "CoreAnimation: Encoder size overflow, old size = %zu, extra = %zu\n"
+ "CoreAnimation: Encountered thread with uncommitted CATransaction; created by:%s"
+ "CoreAnimation: Error initializing HDRProcessor."
+ "CoreAnimation: Failed to allocate %zu bytes, requested = %zu, old size = %zu\n"
+ "CoreAnimation: Failed to construct hosting port: 0x%x - %s"
+ "CoreAnimation: Failed to construct server port: 0x%x - %s"
+ "CoreAnimation: Failed to create IOSurfaceAccelerator: 0x%x"
+ "CoreAnimation: Failed to create SILManager, aborting..."
+ "CoreAnimation: Failed to create thread (%d) - %s"
+ "CoreAnimation: Failed to get server port type (%x) - %s"
+ "CoreAnimation: Failed to initialize HDRBackwardDisplayManagement!"
+ "CoreAnimation: Failed to map %ld bytes with port = %u, protection = %u, err = 0x%x\n"
+ "CoreAnimation: Failed to move server port: 0x%x - %s"
+ "CoreAnimation: Invalid TextureEdgeMode 0x%x"
+ "CoreAnimation: Invalid frame interval range %u %u %u from frame rate range %.2f %.2f %.2f"
+ "CoreAnimation: Invalid frame interval range (%d %d %d) or target interval (%d)"
+ "CoreAnimation: Invalid runloop"
+ "CoreAnimation: Invalid shape: %s"
+ "CoreAnimation: Invalid update!"
+ "CoreAnimation: Message buffer underflow, diff: %lld, msgh_size: %lld, desc: %p, _msg: %p!"
+ "CoreAnimation: Message is batched CommandStream, but no batch ports, desc_count: %zu, port->type:%u!"
+ "CoreAnimation: Message is ool CommandStream, but no body, desc_count: %zu, body_ool->type:%u!"
+ "CoreAnimation: Out of bounds access at index %ld to array with count of %ld!\n"
+ "CoreAnimation: Unable to query displays from server (%d)"
+ "CoreAnimation: Unentitled call to server!"
+ "CoreAnimation: Unrecognized display state: %u"
+ "CoreAnimation: Unsupported use of CADisplayLink SPI off the main thread."
+ "CoreAnimation: long synchronize for %x: now (%u,%u): req %c%u(%u)"
+ "CoreAnimation: unexpected error %i sending sync reply from %x"
+ "DBVFlashWorkaround: _seen_brightness_after_power_cycle"
+ "DBVFlashWorkaround: _seen_brightness_after_power_cycle. indicator nits: %g"
+ "DBVFlashWorkaround: _swapped_brightness_after_power_cycle"
+ "DBVFlashWorkaround: enabled"
+ "DBVFlashWorkaround: removing layer due to seen_brightness %i, swapped_brightness %i"
+ "DBVFlashWorkaround: reset"
+ "DBVFlashWorkaround: skipping brightness. Display powered on: %i seen brightness: %i"
+ "DBVFlashWorkaround: swapped blank aod swap %u, ret %u"
+ "DEAD"
+ "Deleted thread with uncommitted CATransaction; created by:%s"
+ "DeviceSupportsDynamicIsland"
+ "DeviceSupportsGammaContrastPreservation"
+ "Display %d ICC Interface Unsupported\n"
+ "Display %d commitBrightness sdr: %g, headroom: %g, potential headroom: %g, ambient lux: %g, filtered ambient: %g, brightness limit: %g, indicator brightness: %g low ambient strength: %g, high ambient strength: %g, contrast preservation: %g, contrast enhancer: %g brightness ctl disabled %d, unlogged brightness transactions:%u\n"
+ "Display %i LowPowerMode=%i"
+ "Display %u automatic wireless display state control disabled"
+ "Display %u automatic wireless display state control reset"
+ "Display %u automatically set to cloning state %s by set_clone_master"
+ "Display %u automatically set to display state %s by hotplug"
+ "Display %u disables updates %i"
+ "Display %u freeze"
+ "Display %u relbuf info notification enable failed: 0x%x"
+ "Display %u setEnabled:%i"
+ "Display %u swap brightness: %g, limit: %g, indicator brightness: %g, ambient lux: %g, low ambient strength: %g, high ambient strength: %g, contrast preservation: %g, contrast enhancer: %g\n"
+ "Display %u swap_set_contrast_preservation %g failed: 0x%x\n"
+ "DisplayID: %u brightness capabilities set to %@"
+ "DisplayID: %u got brightness capabilities %@"
+ "DisplayID: %u simulating HDR10 brightness capabilities %@"
+ "EDRRequests"
+ "Enabling display state control dependency workaround due to boot-arg."
+ "Encountered thread with uncommitted CATransaction; created by:%s"
+ "ExportSurface"
+ "Failed to allocate MTLTexture for %ux%u %c%c%c%c IOSurface(%#x)"
+ "Failed to check sandbox %{darwin.errno}d"
+ "Failed to find Surface in _shared_surfaces"
+ "Failed to find display %u to disable state control."
+ "Failed to find display %u to set cloning state."
+ "Failed to find display %u to set display state."
+ "Failed to get secure indicator data (%u, %u)"
+ "Failed to initialize Metal or OpenGLES contexts!"
+ "Fill"
+ "Filter merging failed:%s"
+ "FlattenManager::flatten_metal_ctx->has_same_mtl_device (c)"
+ "FlattenedSurface"
+ "FlipBook::cancel() - state:kFlipBookStateDisabled - Unexpected, No action performed"
+ "Found matching color program %p in %s cache at %d for color matching from '%s' to '%s'. Search parameters: ri=%d flags=0x%x cube_size=%u tonemap_headroom=%f content_headroom=%f target_nits=%f cdr_strength=%f edr_strength=%f tm=%d dynamic_tm=%d need_target_nits=%d. Color program: ri=%d flags=0x%x cube_size=%u tonemap_headroom=%f content_headroom=%f target_nits=%f cdr_strength=%f edr_strength=%f explicit_tm_method=%d explicit_tm_options=%p.\n%s"
+ "Frame Latency"
+ "FrameUpdate"
+ "GetDisplayInfo returned 0x%x\n"
+ "Glass Displacement"
+ "Glass Highlight"
+ "HDRToneMappingMode"
+ "HardwarePropertyAccess"
+ "Hysteresis"
+ "IOMFBBlendDisabledKey"
+ "IOMFBDisplay::complete_display_state_transition display_id=%u, current_cloning_state=%s"
+ "IOMFBDisplay::complete_display_state_transition display_id=%u, current_state=%s"
+ "IOMFBLTPOFlashMitigationNeeded"
+ "IOMFBRGBMultiPlaneSupportKey"
+ "IOMFBYUVSupportKey"
+ "IOMobileFrameBufferSwapSetContrastPreservationStrength"
+ "IOMobileFramebufferRelbufInfo"
+ "IOSurface (From app)"
+ "IOSurface 0x%x ('%c%c%c%c') has unexpected bytes-per-row value of %zu, expected at least %zu for the width of %zu."
+ "IOSurface 0x%x [%u x %u] doesn't have the proper data alignment! Expected %zu base address and %zu row byte alignment\n"
+ "IOSurfaceID: 0x%x  usage: %s  access: %s  force read access when detached"
+ "IOSurfaceID: 0x%x  usage: %s  operation: %s  access: %s  value: %#llx %s"
+ "Image %p: texture (%lux%lu)\n"
+ "Image %p; no texture\n"
+ "ImageQueue"
+ "Initializing CAWindowServer..."
+ "Invalid Secure Flipbook type %@"
+ "Invalid secure indicator,frame (%u, %u)"
+ "IsAOCPProtected"
+ "IsVirtualDevice"
+ "Key Fill Highlight"
+ "LastSwapID"
+ "LayerContents"
+ "LayerGain"
+ "LayerHost trying to host itself or one of its ancestors (context id %d)\n"
+ "Maximum flipbook pool size %u ignored. Using %zu."
+ "Maximum flipbook size %u ignored. Using %zu."
+ "MaximumVariableRefreshRate"
+ "Mesh"
+ "Message::send_message() returned 0x%x\n"
+ "Metal failed to build compute pipeline\nfunction=%s\n%s"
+ "Metal failed to build render pipeline\nspec=%s\n%s"
+ "Metal failed to build render pipeline with tile shader"
+ "Metal failed to build render pipeline with tile shader\ntile_pipeline=%s_%s\n%s"
+ "Metal failed to load binary archive\n%s"
+ "Metal failed to load compute shader\nfunction=%s\n%s"
+ "Metal failed to load fragment function\nfunction=%s spec=%s\n%s"
+ "Metal failed to load library\n%s"
+ "Metal failed to load render pipeline\npipeline=%s sdk=%s\n%s"
+ "Metal failed to load vertex function\nfunction=%s spec=%s\n%s"
+ "Metal failed to specialize fragment function\nfunction=%s spec=%s\n%s"
+ "Metal failed to specialize vertex function\nfunction=%s spec=%s\n%s"
+ "MetalImage %p: texture (%c%c%c%c) (%lux%lu) (%lu bytes)\n"
+ "MinimumVariableRefreshRate"
+ "MirroringMode"
+ "NULL"
+ "NULL color space set on context (%x)\n"
+ "Name: %s  IOSurfaceID: 0x%x  Value Completed: 0x%llx  All Finished: %s\n"
+ "NightDrive"
+ "No Surface or Display"
+ "No error"
+ "No matching program in %s cache after %d; ri %d; f 0x%x; cu %d; src %s; dst %s; dt %s; targ_hr %f; source_hr %f; cdr_strength: %f, edr_strength: %f, nn %s; tn %f; explicit_tm_method %d; explicit_tm_options %p"
+ "OGL_IMAGE_RECT_SDF"
+ "Output"
+ "Over Allocation Factor %f ignored. Using %f."
+ "Overall"
+ "PBGRABsovXm_TimgA2Xhfc_IsrcCcl"
+ "PBGRABsovXm_TimgA2Xhfc_IsrcN3Ocsmtsdnlnlnl"
+ "PBGRABsovXm_TimgA2Xhfn_IsrcN3Oc0c4nlnlnlnl"
+ "PBGRAXm_TatcA2S1Xhf"
+ "PBGRAXm_TimgA2Xhfc_IxrgN3Oc3mtc4nlnlnlXq"
+ "PBGRAXm_TimgA2Xhfcn_Isrc"
+ "PBGRAXm_TipcA2Xhf_Isrc"
+ "PRGhAXm_TimgA2Xhfcu_IsrcCcl"
+ "Pattern"
+ "Pb3a8BaddXmw_TimgA3Xhfcx_Isrc"
+ "Pb3a8BdotXm_TimgA2S1Xhfcu_Isrc"
+ "Pb3a8BmulXmw_TimgA3S1Xhfcu_Icir"
+ "Pb3a8BsovXm_A2Xhfcxn"
+ "Pb3a8BsovXm_TcimA2S1Xhfcu_Ialp"
+ "Pb3a8BsovXm_TcimA2S1Xhfcu_IalpCcl"
+ "Pb3a8BsovXm_TcimA2S1Xhfcu_Isup"
+ "Pb3a8BsovXm_TcimA2Xhfcx_Isi1"
+ "Pb3a8BsovXm_TcimA2Xhfcxn_Ialp"
+ "Pb3a8BsovXm_TcimA2Xhfcxn_Irrg"
+ "Pb3a8BsovXm_TcmaA2S1LlnXhfcu"
+ "Pb3a8BsovXm_TimgA2S1Xhfcu_Ialp"
+ "Pb3a8BsovXm_TimgA2S1Xhfcu_IalpCcl"
+ "Pb3a8BsovXm_TimgA2S1Xhfcu_Iara"
+ "Pb3a8BsovXm_TimgA2S1Xhfcu_Isrc"
+ "Pb3a8BsovXm_TimgA2S1Xhfcu_IsrcN3Ocsmtsdnlnlnl"
+ "Pb3a8BsovXm_TimgA2S1Xhfcu_Isrg"
+ "Pb3a8BsovXm_TimgA2Xhfcx_IsrcM1"
+ "Pb3a8BsovXm_TimgA2Xhfcx_IsrcN3Oc3mtc4nlnlnl"
+ "Pb3a8BsovXm_TimgA2Xhfcx_IsrcN3Ocsmtsdnlnlnl"
+ "Pb3a8BsovXm_TimgA2Xhfcxn_IsrcCcl"
+ "Pb3a8BsovXm_TimgA2Xhfcxn_IsrcCrd"
+ "Pb3a8BsovXm_TimgA2Xhfcxn_IsrcN3Oc0c4nlnlnlnl"
+ "Pb3a8BsovXm_TimgA2Xhfcxn_IsrcN3Oc0sdnlnlnlnl"
+ "Pb3a8BsovXm_TimgA2Xhfcxn_IsrcN3Oc4nlnlnlnlnl"
+ "Pb3a8BsovXm_TimgA2Xhfcxp_IsrcN3Oc3mtc4nlnlnl"
+ "Pb3a8BsovXm_TimgA2Xhfcxp_IsrcN3Ocsmtsdnlnlnl"
+ "Pb3a8BsovXm_TmuaA2Xhfcx_Igrn_Isqr"
+ "Pb3a8BsovXm_TmuaA2Xhfcx_Isrc_IsrcM1"
+ "Pb3a8BsovXm_TvcmA2Xhfcx_IsrcM1"
+ "Pb3a8Xm_A2S1Xhfcu"
+ "Pb3a8Xm_BadcA2Xhfcx"
+ "Pb3a8Xm_BdsoA2Xhfcx"
+ "Pb3a8Xm_BpldA2Xhfcx"
+ "Pb3a8Xm_TaplA2Xhfn_Isrc"
+ "Pb3a8Xm_TbdsA2Xhfcx_Isi1_Isrc"
+ "Pb3a8Xm_Tc4pA2S1Xhfcu_Idst"
+ "Pb3a8Xm_TcimA2S1Xhfcu_Ialp"
+ "Pb3a8Xm_TcimBadcA2Xhfcx_Ired"
+ "Pb3a8Xm_TcimBaddA2S1Xhfcu_Ialp"
+ "Pb3a8Xm_TcimBdsoA2Xhfcx_Ialp"
+ "Pb3a8Xm_TcimBdsoA2Xhfcxn_Ialp"
+ "Pb3a8Xm_TcimBpldA2Xhfcx_Isup"
+ "Pb3a8Xm_TcimBvcmA2Xhfcx_Isup"
+ "Pb3a8Xm_TcmaA2S1LlnXhfcu"
+ "Pb3a8Xm_TimgA2S1Xhfcu_IsrcM0"
+ "Pb3a8Xm_TimgA2Xhfcx_IxrgCcl"
+ "Pb3a8Xm_TimgA2Xhfcx_IxrgN3Ocsmtsdnlnlnl"
+ "Pb3a8Xm_TimgBadcA2Xhfcx_Ialp"
+ "Pb3a8Xm_TimgBdsoA2Xhfcxn_Isrc"
+ "Pb3a8Xm_TimgBvcmA2Xhfcx_IalpCcl"
+ "Pb3a8Xm_TimgBvcmA2Xhfcx_Isrg"
+ "Pb3a8Xm_TimgBvcmA2Xhfcxn_Isrc"
+ "Pb3a8Xm_TlubA2Xhf_Isrc"
+ "Pb3a8Xm_Tm1aBvcmA2Xhfcx_Isup_Isup"
+ "Pb3a8Xm_TmuaA2Xhfcxn_IsrcCcl_Isup"
+ "Pb3a8Xmw_A3S1Xhfcu"
+ "Pipeline %s excludes %s\n"
+ "Pipeline %s requires %s\n"
+ "Pl64rXm_A2Xghfc"
+ "Plugin"
+ "Posting %@, payload: %@"
+ "Process %d"
+ "Process %d (%s)"
+ "Pw30rBdotXm_TcimA2S1Xhfcu_Ialp"
+ "Pw30rBdotXm_TcmaA2S1LlnXhfcu"
+ "Pw30rBdotXm_TimgA2S1Xhfcu_Ialp"
+ "Pw30rBsovXm_A2S1Xhfcu"
+ "Pw30rBsovXm_A2Xhfcxn"
+ "Pw30rBsovXm_Tc3sA2S1Xhfcu_Idst"
+ "Pw30rBsovXm_Tc4bA2S1Xhfcu_Idst"
+ "Pw30rBsovXm_TcimA2S1Xhfcu_Ialp"
+ "Pw30rBsovXm_TcimA2S1Xhfcu_IalpCcl"
+ "Pw30rBsovXm_TcimA2S1Xhfcu_Ired"
+ "Pw30rBsovXm_TcimA2S1Xhfcu_Isup"
+ "Pw30rBsovXm_TcimA2Xhfcx_IalpCcl"
+ "Pw30rBsovXm_TcimA2Xhfcx_Icir"
+ "Pw30rBsovXm_TcimA2Xhfcx_Igrn"
+ "Pw30rBsovXm_TcimA2Xhfcx_IgrnCcl"
+ "Pw30rBsovXm_TcimA2Xhfcx_Isi0"
+ "Pw30rBsovXm_TcimA2Xhfcx_Isi1"
+ "Pw30rBsovXm_TcimA2Xhfcx_IsrcCcl"
+ "Pw30rBsovXm_TcimA2Xhfcx_IxrgCcl"
+ "Pw30rBsovXm_TcimA2Xhfcx_IxrgN3OcsmtsdnlnlnlXq"
+ "Pw30rBsovXm_TcimA2Xhfcxn_Ialp"
+ "Pw30rBsovXm_TcimA2Xhfcxn_Irrg"
+ "Pw30rBsovXm_TcimA2Xhfcxn_IsrcCcl"
+ "Pw30rBsovXm_TcmaA2S1LlnXhfcu"
+ "Pw30rBsovXm_TimgA2S1Xhfcu_Ialp"
+ "Pw30rBsovXm_TimgA2S1Xhfcu_IalpCcl"
+ "Pw30rBsovXm_TimgA2S1Xhfcu_Iara"
+ "Pw30rBsovXm_TimgA2S1Xhfcu_Isrc"
+ "Pw30rBsovXm_TimgA2S1Xhfcu_Isrg"
+ "Pw30rBsovXm_TimgA2S1Xhfcu_Isup"
+ "Pw30rBsovXm_TimgA2S1Xhfcun_IsrcCrd"
+ "Pw30rBsovXm_TimgA2Xhfcx_Iara"
+ "Pw30rBsovXm_TimgA2Xhfcx_Icir"
+ "Pw30rBsovXm_TimgA2Xhfcx_Igrn"
+ "Pw30rBsovXm_TimgA2Xhfcx_IgrnCcl"
+ "Pw30rBsovXm_TimgA2Xhfcx_Isar"
+ "Pw30rBsovXm_TimgA2Xhfcx_IsrcCcl"
+ "Pw30rBsovXm_TimgA2Xhfcx_IsrcM1"
+ "Pw30rBsovXm_TimgA2Xhfcx_Isrg"
+ "Pw30rBsovXm_TimgA2Xhfcx_IsrgCcl"
+ "Pw30rBsovXm_TimgA2Xhfcx_Isup"
+ "Pw30rBsovXm_TimgA2Xhfcxn_Isrc"
+ "Pw30rBsovXm_TlrpA2Xhfcx_Isrc_Iclr"
+ "Pw30rBsovXm_TlrpA2Xhfcx_Isrc_Isrc"
+ "Pw30rBsovXm_Tm1aA2Xhfcx_Isup_Isup"
+ "Pw30rBsovXm_TmuaA2S1Xhfcu_Ired_Isqr"
+ "Pw30rBsovXm_TmuaA2Xhfcx_Iara_Isqr"
+ "Pw30rBsovXm_TmuaA2Xhfcx_Igrn_Isqr"
+ "Pw30rBsovXm_TmuaA2Xhfcx_IsrcCcl_Isrg"
+ "Pw30rBsovXm_TmuaA2Xhfcx_IsrcM1_Isup"
+ "Pw30rBsovXm_TmuaA2Xhfcx_Isrc_Isqr"
+ "Pw30rBsovXm_TmuaA2Xhfcx_Isrc_Isup"
+ "Pw30rXm_A2S1Xhfcu"
+ "Pw30rXm_BdsoA2Xhfcx"
+ "Pw30rXm_BlsoA2Xhfcx"
+ "Pw30rXm_BpldA2Xhfcx"
+ "Pw30rXm_TaplA2Xhfn_Isrc"
+ "Pw30rXm_TbdsA2Xhfcx_Isi0_Isrc"
+ "Pw30rXm_TbdsA2Xhfcx_Isi0_IsrcM1"
+ "Pw30rXm_TbdsA2Xhfcx_Isi1_Isrc"
+ "Pw30rXm_TbdsA2Xhfcx_Isi1_IsrcM1"
+ "Pw30rXm_Tc4pA2S1Xhfcu_Idst"
+ "Pw30rXm_TcimA2S1Xhfcu_Ialp"
+ "Pw30rXm_TcimA2Xhfcx_Icir"
+ "Pw30rXm_TcimBadcA2Xhfcx_Ialp"
+ "Pw30rXm_TcimBadcA2Xhfcx_Ired"
+ "Pw30rXm_TcimBadcA2Xhfcx_Isrc"
+ "Pw30rXm_TcimBaddA2S1Xhfcu_Ialp"
+ "Pw30rXm_TcimBdsoA2S1Xhfcun_Ialp"
+ "Pw30rXm_TcimBdsoA2Xhfcxn_Ialp"
+ "Pw30rXm_TcimBpldA2Xhfcx_Isup"
+ "Pw30rXm_TcimBvcmA2Xhfcx_Ialp"
+ "Pw30rXm_TcimBvcmA2Xhfcx_IalpCcl"
+ "Pw30rXm_TcimBvcmA2Xhfcx_Isrg"
+ "Pw30rXm_TcmaA2LlnXhfcx"
+ "Pw30rXm_TcmaA2S1LlnXhfcu"
+ "Pw30rXm_TimgA2S1Xhfcu_Ialp"
+ "Pw30rXm_TimgA2S1Xhfcu_IsrcM0"
+ "Pw30rXm_TimgA2S1Xhfcu_IxrgN3Ocsmtsdnlnlnl"
+ "Pw30rXm_TimgA2S1Xhfcun_Isrc"
+ "Pw30rXm_TimgA2Xhfcx_Isrc"
+ "Pw30rXm_TimgA2Xhfcx_Isrg"
+ "Pw30rXm_TimgA2Xhfcx_IxrgCcl"
+ "Pw30rXm_TimgA2Xhfcx_IxrgN3Ocsmtsdnlnlnl"
+ "Pw30rXm_TimgA2Xhfcx_IxrgN3OcsmtsdnlnlnlXq"
+ "Pw30rXm_TimgA2Xhfcxn_IsrcCcl"
+ "Pw30rXm_TimgBadcA2Xhfcx_Ialp"
+ "Pw30rXm_TimgBdsoA2Xhfcxn_Isrg"
+ "Pw30rXm_TimgBlsoA2Xhfcx_Ialp"
+ "Pw30rXm_TimgBvcmA2Xhfcx_IalpCcl"
+ "Pw30rXm_TimgBvcmA2Xhfcx_Iara"
+ "Pw30rXm_TimgBvcmA2Xhfcx_Ired"
+ "Pw30rXm_TimgBvcmA2Xhfcx_Isrg"
+ "Pw30rXm_Tm1aBvcmA2Xhfcx_Isup_Isup"
+ "Pw30rXm_TmuaA2Xhfcxn_IsrcCcl_Isup"
+ "Pw30rXm_TmuaBadcA2Xhfcx_Ired_Isqr"
+ "Pw40aBaddXmw_TimgA3Xhfcx_Isrc"
+ "Pw40aBdinXm_A2Xhfcx"
+ "Pw40aBdinXm_TcimA2Xhfcx_Isrc"
+ "Pw40aBdinXm_TcimA2Xhfcx_IsrcM1"
+ "Pw40aBdotXm_TcimA2S1Xhfcu_Ialp"
+ "Pw40aBdotXm_TcimA2Xhfcx_Ialp"
+ "Pw40aBdotXm_TcmaA2S1LlnXhfcu"
+ "Pw40aBdotXm_TimgA2S1Xhfcu_Ialp"
+ "Pw40aBdotXm_TimgA2S1Xhfcun_Isrc"
+ "Pw40aBdotXm_TimgA2Xhfcx_Ialp"
+ "Pw40aBmulXm_TcimA2Xhfcx_Isrc"
+ "Pw40aBmulXmw_TimgA3S1Xhfcu_Icir"
+ "Pw40aBsapXm_TcimA2S1Xhfcu_Ialp"
+ "Pw40aBsovXm_A2S1Xhfcu"
+ "Pw40aBsovXm_A2Xhfcxn"
+ "Pw40aBsovXm_TaltA2Xhf_Isrc"
+ "Pw40aBsovXm_TbroA2Xhf_Isrc_Isrc"
+ "Pw40aBsovXm_Tc3sA2Xhfcx_IsrcM1"
+ "Pw40aBsovXm_Tc4bA2S1Xhfcu_Idst"
+ "Pw40aBsovXm_TcimA2S1Xhfcu_Ialp"
+ "Pw40aBsovXm_TcimA2S1Xhfcu_IalpCcl"
+ "Pw40aBsovXm_TcimA2S1Xhfcu_Icir"
+ "Pw40aBsovXm_TcimA2S1Xhfcu_Ired"
+ "Pw40aBsovXm_TcimA2S1Xhfcu_Isup"
+ "Pw40aBsovXm_TcimA2Xhfcx_Isi1"
+ "Pw40aBsovXm_TcimA2Xhfcx_IxrgCcl"
+ "Pw40aBsovXm_TcimA2Xhfcx_IxrgN3Oc3mtc4nlnlnl"
+ "Pw40aBsovXm_TcimA2Xhfcx_IxrgN3Oc3mtc4nlnlnlXq"
+ "Pw40aBsovXm_TcimA2Xhfcxn_Ialp"
+ "Pw40aBsovXm_TcimA2Xhfcxn_Irrg"
+ "Pw40aBsovXm_TcmaA2S1LlnXhfcu"
+ "Pw40aBsovXm_Tds8A2Xhf_Isrc"
+ "Pw40aBsovXm_TimgA2S1Xhfcu_Ialp"
+ "Pw40aBsovXm_TimgA2S1Xhfcu_IalpCcl"
+ "Pw40aBsovXm_TimgA2S1Xhfcu_Iara"
+ "Pw40aBsovXm_TimgA2S1Xhfcu_Ired"
+ "Pw40aBsovXm_TimgA2S1Xhfcu_Isrc"
+ "Pw40aBsovXm_TimgA2S1Xhfcu_IsrcM0"
+ "Pw40aBsovXm_TimgA2S1Xhfcu_Isrg"
+ "Pw40aBsovXm_TimgA2S1Xhfcu_IsrgCcl"
+ "Pw40aBsovXm_TimgA2S1Xhfcu_Isup"
+ "Pw40aBsovXm_TimgA2S1Xhfcun_IsrcCrd"
+ "Pw40aBsovXm_TimgA2Xhfcx_IgrnCcl"
+ "Pw40aBsovXm_TimgA2Xhfcx_IsrcM1"
+ "Pw40aBsovXm_TlrpA2Xhfcx_Isrc_Iclr"
+ "Pw40aBsovXm_Tm1aA2S1Xhfcu_Isup_Isup"
+ "Pw40aBsovXm_TmuaA2S1Xhfcu_Ired_Isqr"
+ "Pw40aBsovXm_TmuaA2S1Xhfcu_Isrc_Isqr"
+ "Pw40aBsovXm_TmuaA2Xhfcx_Iara_Isqr"
+ "Pw40aBsovXm_TmuaA2Xhfcx_Igrn_Isqr"
+ "Pw40aBsovXm_TmuaA2Xhfcx_IsrcCcl_Isqr"
+ "Pw40aBsovXm_TmuaA2Xhfcx_IsrcCcl_Isrg"
+ "Pw40aBsovXm_TmuaA2Xhfcx_IsrcCcl_Isup"
+ "Pw40aBsovXm_TmuaA2Xhfcx_IsrcM1_Isqr"
+ "Pw40aBsovXm_TmuaA2Xhfcx_IsrcM1_Isup"
+ "Pw40aBsovXm_TmuaA2Xhfcx_IsrcN3Oc3mtc4nlnlnl_Isqr"
+ "Pw40aBsovXm_TmuaA2Xhfcx_Ixrg_Isqr"
+ "Pw40aBsovXm_TmuaA2Xhfcxn_IsrcCcl_Icir"
+ "Pw40aBsovXm_TmuaA2Xhfcxn_Isrc_Isqr"
+ "Pw40aBsovXm_TsdrA2S1Xhfcu_Idst"
+ "Pw40aXm_A2S1Xhfcu"
+ "Pw40aXm_BdrkA2Xhfcx"
+ "Pw40aXm_BdsoA2Xhfcx"
+ "Pw40aXm_BlsoA2Xhfcx"
+ "Pw40aXm_BovlA2S1Xhfcu"
+ "Pw40aXm_BpldA2Xhfcx"
+ "Pw40aXm_TaltA2Xhf_Isrc"
+ "Pw40aXm_TbdsA2Xhfcx_Isup_IsrcM1"
+ "Pw40aXm_Tc3sA2Xhfcx_Idst"
+ "Pw40aXm_Tc4pA2S1Xhfcu_Idst"
+ "Pw40aXm_TcimA2S1Xhfcu_Ialp"
+ "Pw40aXm_TcimA2S1Xhfcu_Icir"
+ "Pw40aXm_TcimA2Xhfcx_Idst"
+ "Pw40aXm_TcimA2Xhfcx_IsrcM1"
+ "Pw40aXm_TcimBadcA2Xhfcx_Ialp"
+ "Pw40aXm_TcimBadcA2Xhfcx_Ired"
+ "Pw40aXm_TcimBadcA2Xhfcx_Isrc"
+ "Pw40aXm_TcimBadcA2Xhfcx_Isup"
+ "Pw40aXm_TcimBaddA2S1Xhfcu_Ialp"
+ "Pw40aXm_TcimBdsoA2S1Xhfcun_Ialp"
+ "Pw40aXm_TcimBdsoA2Xhfcxn_Ialp"
+ "Pw40aXm_TcimBpldA2Xhfcx_Isup"
+ "Pw40aXm_TcimBvcmA2Xhfcx_Ialp"
+ "Pw40aXm_TcimBvcmA2Xhfcx_IalpCcl"
+ "Pw40aXm_TcimBvcmA2Xhfcx_Icir"
+ "Pw40aXm_TcimBvcmA2Xhfcx_Isrg"
+ "Pw40aXm_TcimBvcmA2Xhfcx_Isup"
+ "Pw40aXm_TcmaA2S1LlnXhfcu"
+ "Pw40aXm_TimgA2S1Xhfcu_Ialp"
+ "Pw40aXm_TimgA2S1Xhfcu_Isrc"
+ "Pw40aXm_TimgA2S1Xhfcu_IsrcM0"
+ "Pw40aXm_TimgA2S1Xhfcu_IxrgN3Oc3mtc4nlnlnl"
+ "Pw40aXm_TimgA2S1Xhfcun_Isrc"
+ "Pw40aXm_TimgA2Xhfcx_IxrgCcl"
+ "Pw40aXm_TimgA2Xhfcx_IxrgN3Oc3mtc4nlnlnl"
+ "Pw40aXm_TimgA2Xhfcx_IxrgN3Ocsmtsdnlnlnl"
+ "Pw40aXm_TimgA2Xhfcx_IxrgN3OcsmtsdnlnlnlXq"
+ "Pw40aXm_TimgA2Xhfcxn_IsrcCcl"
+ "Pw40aXm_TimgBadcA2Xhfcx_Ialp"
+ "Pw40aXm_TimgBdsoA2Xhfcxn_Isrc"
+ "Pw40aXm_TimgBdsoA2Xhfcxn_Isrg"
+ "Pw40aXm_TimgBlsoA2Xhfcx_Ialp"
+ "Pw40aXm_TimgBvcmA2Xhfcx_Ialp"
+ "Pw40aXm_TimgBvcmA2Xhfcx_IalpCcl"
+ "Pw40aXm_TimgBvcmA2Xhfcx_Icir"
+ "Pw40aXm_TimgBvcmA2Xhfcx_IgrnCcl"
+ "Pw40aXm_TimgBvcmA2Xhfcx_Isrg"
+ "Pw40aXm_TimgBvcmA2Xhfcx_Isup"
+ "Pw40aXm_TlubA2Xhf_Isrc"
+ "Pw40aXm_Tm1aBvcmA2Xhfcx_Isup_Isup"
+ "Pw40aXm_TmuaA2S1Xhfcu_Ired_Isqr"
+ "Pw40aXm_TmuaA2Xhfcx_Ixrg_Isqr"
+ "Pw40aXm_TmuaA2Xhfcxn_Isrc_Isqr"
+ "Pw40aXm_TmuaBadcA2Xhfcx_Ired_Isqr"
+ "Pw40aXm_TmuaBaddA2S1Xhfcu_Ired_Isqr"
+ "Pw40aXm_TvcmA2Xhfcx_IsrcM1"
+ "Pw40aXmw_A3S1Xhfcu"
+ "Ramp %d: Setting SDR brightness to %g nits, headroom to %g, limit to %g, contrast enhancer to %g, low_amb_str to %g, high_amb_str to %g, contrast_preservation to %g, indicator_nits to %g indicator_limit to %g"
+ "Render pipeline warmup took %0.2fs, MTLPixelFormats: {%s, %s, %s, %s, %s, %s, %s, %s}\n"
+ "Render::Surface"
+ "RenderSurface"
+ "Required precompiled pipeline not found: %s\n"
+ "SDF"
+ "SDF-element-layer"
+ "SDF-layer"
+ "SDFLayer"
+ "SDFLayerContents"
+ "SDF_A"
+ "SDF_RGBA"
+ "SILManager flipbook size (%u, %u) mismatched provided size (%f, %f)"
+ "SUPERCIRCLE_SDF"
+ "Scaling"
+ "SecureIndicator.Telemetry"
+ "Server::set_display_cloning_state display_id=%u current_cloning_state=%s target_cloning_state=%s result=%s"
+ "Setting blend space failed, display does not support Blending"
+ "Shared Event Value in transaction null, skipping"
+ "Shared Event in transaction null, skipping"
+ "Shared Event transaction list empty"
+ "Shared Event transaction port: %d != Shared Event port: %d"
+ "Shared Event transaction value: %lld <= Shared Event value: %lld"
+ "SupportsVariableRefreshRate"
+ "T@\"<CALayoutManager>\",&,V_layoutManager"
+ "T@\"<MTLResidencySet>\",R"
+ "T@\"CAHostingToken\",&,N"
+ "T@\"CAHostingToken\",R,N"
+ "T@\"CASDFEffect\",&"
+ "T@\"NSArray\",C,V_colors"
+ "T@\"NSArray\",C,V_distances"
+ "T@\"NSArray\",C,V_interpolations"
+ "T@\"NSString\",C,N,V_preferredHdrMode"
+ "TB,GisFloating"
+ "TB,GisSeparated"
+ "TB,N,V_global"
+ "TB,N,V_includeGradient"
+ "TB,N,V_invert"
+ "TB,N,V_punchout"
+ "TB,R,GisAuthoritative"
+ "TB,V_excludeSeparated"
+ "TB,V_premultiplied"
+ "TB,V_wantsDynamicContentScaling"
+ "TI,V_autoresizingMask"
+ "TQ,N,V_maximumPoolMemory"
+ "TQ,V_trackedLayerIDContent"
+ "TQ,V_updateBeginTime"
+ "T^{CGColor=},&,N,V_color"
+ "T^{CGColor=},&,N,V_fillColor"
+ "T^{CGColor=},&,N,V_keyColor"
+ "Td,N,V_amount"
+ "Td,N,V_angle"
+ "Td,N,V_curvature"
+ "Td,N,V_fillAmount"
+ "Td,N,V_fillAngle"
+ "Td,N,V_fillHeight"
+ "Td,N,V_fillHeightOffset"
+ "Td,N,V_fillHeightScale"
+ "Td,N,V_fillSpread"
+ "Td,N,V_fillSpreadOffset"
+ "Td,N,V_fillSpreadScale"
+ "Td,N,V_gradientSmoothing"
+ "Td,N,V_height"
+ "Td,N,V_keyAmount"
+ "Td,N,V_keyAngle"
+ "Td,N,V_keyHeight"
+ "Td,N,V_keyHeightOffset"
+ "Td,N,V_keyHeightScale"
+ "Td,N,V_keySpread"
+ "Td,N,V_keySpreadOffset"
+ "Td,N,V_keySpreadScale"
+ "Td,N,V_maskOffset"
+ "Td,N,V_maximum"
+ "Td,N,V_maximumDistance"
+ "Td,N,V_minimum"
+ "Td,N,V_oneValueDistance"
+ "Td,N,V_padding"
+ "Td,N,V_radius"
+ "Td,N,V_spread"
+ "Td,N,V_zeroValueDistance"
+ "Td,R,N,V_time"
+ "Td,V_contrastPreservationBegin"
+ "Td,V_contrastPreservationEnd"
+ "Tf,N,V_overAllocationFactor"
+ "TiledImage"
+ "Total entries: %d\nTotal Memory: %dMB\n\n"
+ "Total entries: %d\nTotal Memory: %dMB (%dMB)\nMemory Budget: %dMB\n"
+ "Tq,N,V_outputBitDepth"
+ "Transform"
+ "Transition"
+ "T{CGSize=dd},N,V_offset"
+ "UNEVEN_SUPERCIRCLE_SDF"
+ "Unable to get power assertions 0x%x"
+ "Unable to render backdrop-aware vibrant color matrix filter while existing memoryless offscreen surface in use"
+ "Undefined"
+ "Unique ID is a pack of two 32-bit update_seed and swap_id. base_mct=%{signpost.generator:base_mct}llu  args1=%{public, name=args1}#llx args2=%{public, name=args2}#llx contributors=%{public, name=contributors}.*P FrameLifetimeInterval=%{name=FrameLifetimeInterval,signpost.generator:begin_end_32b}llu  FrameRender=%{name=FrameRender,signpost.generator:begin_end_32b}llu  FrameReady=%{name=FrameReady,signpost.generator:event}u  FramePrevious=%{name=FramePrevious,signpost.generator:event}llu "
+ "Unique ID is a pack of two 32-bit update_seed and swap_id. base_mct=%{signpost.generator:base_mct}llu  args1=%{public, name=args1}#llx args2=%{public, name=args2}#llx contributors=%{public, name=contributors}.*P FrameLifetimeInterval=%{name=FrameLifetimeInterval,signpost.generator:begin_end_32b}llu  FrameRender=%{name=FrameRender,signpost.generator:begin_end_32b}llu  FrameReady=%{name=FrameReady,signpost.generator:event}u  FramePrevious=%{name=FramePrevious,signpost.generator:event}llu  FrameGPUExecute=%{name=FrameGPUExecute,signpost.generator:begin_end_32b}llu "
+ "Unique ID is a pack of two 32-bit update_seed and swap_id. base_mct=%{signpost.generator:base_mct}llu  args1=%{public, name=args1}#llx args2=%{public, name=args2}#llx contributors=%{public, name=contributors}.*P FrameLifetimeInterval=%{name=FrameLifetimeInterval,signpost.generator:begin_end_32b}llu  FrameRender=%{name=FrameRender,signpost.generator:begin_end_32b}llu  FrameReady=%{name=FrameReady,signpost.generator:event}u  FramePrevious=%{name=FramePrevious,signpost.generator:event}llu  FrameGPUExecute=%{name=FrameGPUExecute,signpost.generator:begin_end_32b}llu  FrameModifierTarget=%{name=FrameModifierTarget,signpost.generator:event}u "
+ "Unique ID is a pack of two 32-bit update_seed and swap_id. base_mct=%{signpost.generator:base_mct}llu  args1=%{public, name=args1}#llx args2=%{public, name=args2}#llx contributors=%{public, name=contributors}.*P FrameLifetimeInterval=%{name=FrameLifetimeInterval,signpost.generator:begin_end_32b}llu  FrameRender=%{name=FrameRender,signpost.generator:begin_end_32b}llu  FrameReady=%{name=FrameReady,signpost.generator:event}u  FramePrevious=%{name=FramePrevious,signpost.generator:event}llu  FrameGPUExecute=%{name=FrameGPUExecute,signpost.generator:begin_end_32b}llu  FrameProcess=%{name=FrameProcess,signpost.generator:begin_end_32b}llu "
+ "Unique ID is a pack of two 32-bit update_seed and swap_id. base_mct=%{signpost.generator:base_mct}llu  args1=%{public, name=args1}#llx args2=%{public, name=args2}#llx contributors=%{public, name=contributors}.*P FrameLifetimeInterval=%{name=FrameLifetimeInterval,signpost.generator:begin_end_32b}llu  FrameRender=%{name=FrameRender,signpost.generator:begin_end_32b}llu  FrameReady=%{name=FrameReady,signpost.generator:event}u  FramePrevious=%{name=FramePrevious,signpost.generator:event}llu  FrameGPUExecute=%{name=FrameGPUExecute,signpost.generator:begin_end_32b}llu  FrameProcess=%{name=FrameProcess,signpost.generator:begin_end_32b}llu  FrameModifierTarget=%{name=FrameModifierTarget,signpost.generator:event}u "
+ "Unique ID is a pack of two 32-bit update_seed and swap_id. base_mct=%{signpost.generator:base_mct}llu  args1=%{public, name=args1}#llx args2=%{public, name=args2}#llx contributors=%{public, name=contributors}.*P FrameLifetimeInterval=%{name=FrameLifetimeInterval,signpost.generator:begin_end_32b}llu  FrameRender=%{name=FrameRender,signpost.generator:begin_end_32b}llu  FrameReady=%{name=FrameReady,signpost.generator:event}u  FramePrevious=%{name=FramePrevious,signpost.generator:event}llu  FrameModifierTarget=%{name=FrameModifierTarget,signpost.generator:event}u "
+ "Unique ID is a pack of two 32-bit update_seed and swap_id. base_mct=%{signpost.generator:base_mct}llu  args1=%{public, name=args1}#llx args2=%{public, name=args2}#llx contributors=%{public, name=contributors}.*P FrameLifetimeInterval=%{name=FrameLifetimeInterval,signpost.generator:begin_end_32b}llu  FrameRender=%{name=FrameRender,signpost.generator:begin_end_32b}llu  FrameReady=%{name=FrameReady,signpost.generator:event}u  FramePrevious=%{name=FramePrevious,signpost.generator:event}llu  FrameProcess=%{name=FrameProcess,signpost.generator:begin_end_32b}llu "
+ "Unique ID is a pack of two 32-bit update_seed and swap_id. base_mct=%{signpost.generator:base_mct}llu  args1=%{public, name=args1}#llx args2=%{public, name=args2}#llx contributors=%{public, name=contributors}.*P FrameLifetimeInterval=%{name=FrameLifetimeInterval,signpost.generator:begin_end_32b}llu  FrameRender=%{name=FrameRender,signpost.generator:begin_end_32b}llu  FrameReady=%{name=FrameReady,signpost.generator:event}u  FramePrevious=%{name=FramePrevious,signpost.generator:event}llu  FrameProcess=%{name=FrameProcess,signpost.generator:begin_end_32b}llu  FrameModifierTarget=%{name=FrameModifierTarget,signpost.generator:event}u "
+ "Unknown processes"
+ "VirtualDisplay::complete_display_state_transition display_id=%u, current_cloning_state=%s"
+ "VirtualDisplay::complete_display_state_transition display_id=%u, current_state=%s"
+ "VirtualDisplay::set_display_state display_id=%u current_state=%s target_state=%s"
+ "Visualization"
+ "Zombie"
+ "[0x%x] FG attachment Found"
+ "[CAContext setFence:count:] is deprecated. Ignoring!"
+ "[CADisplay allowsVirtualModes] is deprecated!"
+ "[CADisplay colorMode] is deprecated!"
+ "[CADisplay setAllowsVirtualModes] is deprecated!"
+ "[CADisplay setColorMode:] is deprecated!"
+ "[CAWindowServerDisplay setColorMode:] is deprecated!"
+ "[EAGLContext renderbufferStorage:fromDrawable:] was called from a non-main thread in an implicit transaction! Note that this may be unsafe without an explicit CATransaction or a call to [CATransaction flush]."
+ "[Layer-%p] Failed to allocate surface"
+ "^{CADisplayModeCriteriaPriv={CGSize=dd}diB}"
+ "^{CAWindowServerDisplayImpl={Mutex={_opaque_pthread_mutex_t=q[56c]}}^{Server}{CABrightnessTransaction=ffffffffffff{?=[9f]}fBBI}@?@@@@BB}"
+ "^{CGImage=}32@0:8@16^{CGImage=}24"
+ "^{DynamicFrameRateSource=I^v{CAFrameRateRange=fff}{CAFrameIntervalRange=III}QiQQ[4I]b1b1^{DynamicFrameRateSource}b1}"
+ "^{Transition=I*^?^?II{SpinLock={?=i}}q@?C}"
+ "^{_CAMetalDrawablePrivate={Atomic={?=i}}IIIQQQQd^{_CAMetalLayerPrivate}^{__IOSurface}@@@Q^{CGColorSpace}@@Cb1b1b1b1b1b1b1b1}"
+ "^{_CAMetalDrawablePrivate={Atomic={?=i}}IIIQQQQd^{_CAMetalLayerPrivate}^{__IOSurface}@@@Q^{CGColorSpace}@@Cb1b1b1b1b1b1b1b1}16@0:8"
+ "^{__CFData=}16@0:8"
+ "_amount"
+ "_angle"
+ "_autoresizingMask"
+ "_availableModesInternal"
+ "_cancelTimestamp"
+ "_cloning_state_transition"
+ "_colors"
+ "_context"
+ "_contrastPreservationBegin"
+ "_contrastPreservationEnd"
+ "_copyStateInfo"
+ "_curvature"
+ "_display_state_transition"
+ "_distances"
+ "_excludeSeparated"
+ "_fillAmount"
+ "_fillAngle"
+ "_fillColor"
+ "_fillHeight"
+ "_fillHeightOffset"
+ "_fillHeightScale"
+ "_fillSpread"
+ "_fillSpreadOffset"
+ "_fillSpreadScale"
+ "_framesLock"
+ "_global"
+ "_gradientSmoothing"
+ "_height"
+ "_includeGradient"
+ "_interpolations"
+ "_invalidate_on_dealloc"
+ "_invert"
+ "_keyAmount"
+ "_keyAngle"
+ "_keyColor"
+ "_keyHeight"
+ "_keyHeightOffset"
+ "_keyHeightScale"
+ "_keySpread"
+ "_keySpreadOffset"
+ "_keySpreadScale"
+ "_layoutManager"
+ "_maskOffset"
+ "_maximum"
+ "_maximumDistance"
+ "_maximumPoolMemory"
+ "_minimum"
+ "_notifyRenderBegin"
+ "_notifyRenderCompletedForTime:status:frameId:oldestFrameId:apl:aplDimming:memoryUsage:rawSurfacePort:rawSurfaceDestRect:"
+ "_offset"
+ "_onRenderBeginClientIpc"
+ "_onRenderBegunCB"
+ "_onRenderCBLock"
+ "_onRenderCompletedCB"
+ "_onRenderInfo"
+ "_oneValueDistance"
+ "_outputBitDepth"
+ "_overAllocationFactor"
+ "_padding"
+ "_performPreLayoutUpdate"
+ "_performPreLayoutUpdateOfLayer:"
+ "_preferredHdrMode"
+ "_premultiplied"
+ "_punchout"
+ "_radius"
+ "_renderInProgress"
+ "_renderTimestamp"
+ "_renderer"
+ "_resetConfiguration"
+ "_spread"
+ "_thread_flags"
+ "_time"
+ "_tokenNeedsPort"
+ "_trackedLayerIDContent"
+ "_unionConfigurationForEffect:"
+ "_updateBeginTime"
+ "_validateSendRight"
+ "_wantsDynamicContentScaling"
+ "_warmed_up"
+ "_workgroup_interval != nullptr"
+ "_xPort"
+ "_zeroValueDistance"
+ "acquireWirelessDisplayStateControl"
+ "addAllocation:"
+ "addFence:completion:"
+ "add_free_surface_to_pool"
+ "allEffectsClasses"
+ "allowsColorMatching"
+ "allowsCornerContentsEdgeEffects"
+ "allowsFilteredLuma"
+ "allowsRemoteEffectHitTesting"
+ "always"
+ "amount"
+ "angle"
+ "anim-edr"
+ "animId"
+ "at"
+ "at least "
+ "authoritative"
+ "bcm"
+ "begin_work_interval"
+ "blendFactor"
+ "block"
+ "bvc"
+ "ca_no_dsc_dependency"
+ "cache_misses"
+ "captureMode"
+ "captureModeCanonicalHDR"
+ "captureModeCurrentHDR"
+ "captureModeSDR"
+ "changing `contents' on CAMetalLayer may result in undefined behavior\n"
+ "changing over allocate factor to %f"
+ "changing pool memory max size to %zu"
+ "chromaticAberrationMap"
+ "chromatic_aberration_map"
+ "cid != 0"
+ "clone failed to copy detached layer - Disabling detachment"
+ "cloning state"
+ "cloningState"
+ "collect_memory"
+ "com.apple.backboardd.displaythread"
+ "com.apple.coreanimation.FlattenManager"
+ "com.apple.coreanimation.flatten-surface"
+ "com.apple.coreanimation.image-brim-1"
+ "com.apple.coreanimation.image-brim-2"
+ "com.apple.coreanimation.image-capture-backdrop"
+ "com.apple.coreanimation.image-filter-backdrop"
+ "com.apple.coreanimation.image-offscreen"
+ "com.apple.coreanimation.image-render-backdrop"
+ "com.apple.coreanimation.image-render-border"
+ "com.apple.coreanimation.image-render-interpolator"
+ "com.apple.coreanimation.image-render-prepared-layers"
+ "com.apple.coreanimation.image-render-shape"
+ "com.apple.coreanimation.image-render-solid-background"
+ "com.apple.coreanimation.image-render-vibrant-color"
+ "com.apple.coreanimation.iosurface"
+ "com.apple.coreanimation.sdf_generator"
+ "committed-below"
+ "compile_count"
+ "compressed_pixel_format"
+ "compute_average_luma"
+ "compute_sum_luma"
+ "configureLayer:transaction:"
+ "constrainedHigh"
+ "contentsCDRStrength"
+ "contentsHeadroom"
+ "contentsOneValueDistance"
+ "contentsZeroValueDistance"
+ "context hosting changed while locked!\n"
+ "contrastPreservationBegin"
+ "contrastPreservationEnd"
+ "copied CGImageRef %p - RGB mask (bug!)\n"
+ "copied CGImageRef %p - bad RGB image format (%d bpp, %d bpc, %d info)\n"
+ "copied CGImageRef %p - bad alignment for IOSurface 0x%x\n"
+ "copied CGImageRef %p - bad decode array\n"
+ "copied CGImageRef %p - bad grayscale image format (%d bpp, %d bpc, %d info)\n"
+ "copied CGImageRef %p - bad image alignment\n"
+ "copied CGImageRef %p - bad mask\n"
+ "copied CGImageRef %p - bad mask image format (%d bpp, %d bpc)\n"
+ "copied CGImageRef %p - bad row alignment\n"
+ "copied CGImageRef %p - decode or mask\n"
+ "copied CGImageRef %p - format not supported by hardware\n"
+ "copied CGImageRef %p - image size (%lu x %lu) exceeds max texture size\n"
+ "copied CGImageRef %p - mask size\n"
+ "copied CGImageRef %p - mipmap generation\n"
+ "copied CGImageRef %p - needs color matching\n"
+ "copied CGImageRef %p - no data pointer\n"
+ "copied CGImageRef %p - non-RGB color model\n"
+ "copied CGImageRef %p - non-native format (%d)\n"
+ "copyPrivateRepresentation"
+ "coreanimation_prelayout"
+ "coreanimation_prelayout_linkedon_check"
+ "create_surface_with_properties"
+ "create_variable_blur_mip_surface"
+ "create_variable_blur_mip_surface_compute"
+ "create_workgroup"
+ "createsShadowGroup"
+ "ctx-%x_%s(%d)"
+ "curvature"
+ "data provider size invalid"
+ "data provider size is too small"
+ "defaultValues"
+ "desired_mipmap_levels != 0"
+ "destinationEDR"
+ "destinationSDR"
+ "dfa"
+ "dff"
+ "dfg"
+ "dfp"
+ "dfs"
+ "dfu"
+ "dfv"
+ "dgd"
+ "dgf"
+ "dgg"
+ "dgh"
+ "disableFoveation"
+ "disableFrameDoubling"
+ "disabling OpenGL extension %s\n"
+ "displacementMap"
+ "displacement_map"
+ "display-primary"
+ "display-secondary"
+ "displayCloningStateDidChange:seed:result:"
+ "displayStateDidChange:seed:result:"
+ "distances"
+ "dpm"
+ "draw_call_count"
+ "draw_count"
+ "earlyWakeupOffset"
+ "edge_extend"
+ "effect"
+ "effectOffset"
+ "encodeWithBlock:"
+ "end > begin && \"erase invalid iterator range\""
+ "erase"
+ "event"
+ "eventPort"
+ "eventPortAtIndex:"
+ "excludeSeparated"
+ "failed to add monotonic cube ((%g, %g) (%g, %g) (%g, %g) (%g, %g))\n"
+ "failed to allocate %ld bytes\n"
+ "failed to copy main layer"
+ "failed to create Metal context!\n"
+ "failed to lock IOSurface %x\n"
+ "failed to query region %p (%zu bytes)\n"
+ "failed trying to set maximumDrawableCount to %lu outside of the valid range of [2, %d]"
+ "fallback_draws"
+ "fillAmount"
+ "fillAngle"
+ "fillHeight"
+ "fillHeightOffset"
+ "fillHeightScale"
+ "fillSpread"
+ "fillSpreadOffset"
+ "fillSpreadScale"
+ "finish_work_interval"
+ "flattenMode"
+ "flattened_cache_add_surface"
+ "forcing %saccelerated backing\n"
+ "framingOptions"
+ "fullscreenGameMode"
+ "fullyOccluded"
+ "gbg"
+ "gbn"
+ "generateSDFWithRequest:forImage:"
+ "gfg"
+ "glassBackground"
+ "glassForeground"
+ "glass_background"
+ "glass_background_no_bleed"
+ "glass_foreground"
+ "global-light"
+ "globalLightAngle"
+ "globalLightHeight"
+ "globalLightOpacity"
+ "globalLightSpread"
+ "gradientOvalization"
+ "gradientSmoothing"
+ "handleFromXPCRepresentation:error:"
+ "handleWithPort:data:error:"
+ "headroom"
+ "hitTestsAsFill"
+ "hostingToken"
+ "hw.memsize_physical"
+ "ignoreAnimations"
+ "ignored CGImageRef %p - bad RGB 16-is-half format (%d bpp, %d bpc, %d info)\n"
+ "ignored CGImageRef %p - bad grayscale 16-is-half format (%d bpp, %d bpc, %d info)\n"
+ "ignoring exception: %@"
+ "ignoring invalid path\n"
+ "image stride is too large for GPU, ignoring\n"
+ "includeGradient"
+ "initWithBytes:length:"
+ "initWithSharedEvent:waitValue:isWrite:"
+ "inputAberrationAmount"
+ "inputAberrationAngle"
+ "inputAberrationHeight"
+ "inputAberrationOffset"
+ "inputAdaptive"
+ "inputBackdropAware"
+ "inputBleedAmount"
+ "inputBleedBlurRadius"
+ "inputBleedColorMatrixBlack"
+ "inputBleedColorMatrixFillColor"
+ "inputBleedColorMatrixSaturation"
+ "inputBleedColorMatrixWhite"
+ "inputBleedDarkenBlend"
+ "inputBleedDistance0"
+ "inputBleedDistance1"
+ "inputBleedHeight"
+ "inputBleedOffset"
+ "inputBleedOpacity"
+ "inputBleedSaturation"
+ "inputBlurDistance0"
+ "inputBlurDistance1"
+ "inputBlurDistance2"
+ "inputBlurDistance3"
+ "inputBlurDistance4"
+ "inputBlurOpacity0"
+ "inputBlurOpacity1"
+ "inputBlurOpacity2"
+ "inputBlurOpacity3"
+ "inputBlurOpacity4"
+ "inputBlurRadius"
+ "inputEdgeEnd"
+ "inputEdgeOpacityEnd"
+ "inputEdgeOpacityStart"
+ "inputEdgeStart"
+ "inputFaceColorMatrixBlack"
+ "inputFaceColorMatrixFillColor"
+ "inputFaceColorMatrixSaturation"
+ "inputFaceColorMatrixWhite"
+ "inputFaceOpacity"
+ "inputFade"
+ "inputInnerRefractionAmount"
+ "inputInnerRefractionHeight"
+ "inputMaskImage"
+ "inputMaxHeadroom"
+ "inputOffset"
+ "inputOuterRefractionAmount"
+ "inputOuterRefractionHeight"
+ "inputRefractionAmount"
+ "inputRefractionDistance0"
+ "inputRefractionDistance1"
+ "inputRefractionHeight"
+ "inputRefractionOffset"
+ "inputRefractionOpacity"
+ "inputSDRGradientDistance0"
+ "inputSDRGradientDistance1"
+ "inputSDRHoldingToneEnabled"
+ "inputSDRShadowOpacity"
+ "inputShadowAmount"
+ "inputShadowBlurRadius"
+ "inputShadowColorMatrixBlack"
+ "inputShadowColorMatrixFillColor"
+ "inputShadowColorMatrixSaturation"
+ "inputShadowColorMatrixWhite"
+ "inputShadowDistanceOffset"
+ "inputShadowHeight"
+ "inputShadowOffset"
+ "inputShadowOpacity"
+ "inputShadowRadius"
+ "inputShadowVibrancyContribution"
+ "inputSourceSublayerName"
+ "insecure context %x - pid %u [%s].\n%s"
+ "insert"
+ "invalid commit handler phase! Defaulting to pre-commit.\n"
+ "invalid mesh transform - paired edge\n"
+ "invalid mesh transform - too few edges\n"
+ "invalid mesh transform - vertex index\n"
+ "invert"
+ "isAuthoritative"
+ "isFloating"
+ "isWrite"
+ "kCGColorConversionInfoForceCreate"
+ "kCGConstrainedDynamicRange"
+ "kCGContentAverageLightLevelNits"
+ "kCGContentEDRStrength"
+ "kCGContentToneMappingInfo"
+ "kCGContextSynchronizeAttributes"
+ "kCGSourceHeadroom"
+ "kCGTargetHeadroom"
+ "kColorPixelFormat_DolbyVisionLowLatency"
+ "kColorPixelFormat_DolbyVisionNative"
+ "kColorPixelFormat_DolbyVisionTunneled"
+ "kColorPixelFormat_RGBCalibrated_10"
+ "kColorPixelFormat_RGBCalibrated_12"
+ "kColorPixelFormat_RGBCalibrated_8"
+ "kColorPixelFormat_RGBCalibrated_PQ_10"
+ "kColorPixelFormat_RGBCalibrated_PQ_12"
+ "kColorPixelFormat_RGB_10"
+ "kColorPixelFormat_RGB_12"
+ "kColorPixelFormat_RGB_8"
+ "kColorPixelFormat_RGB_PQ_10"
+ "kColorPixelFormat_RGB_PQ_12"
+ "kColorPixelFormat_YCbCr420_10"
+ "kColorPixelFormat_YCbCr420_12"
+ "kColorPixelFormat_YCbCr420_8"
+ "kColorPixelFormat_YCbCr420_PQ_10"
+ "kColorPixelFormat_YCbCr420_PQ_12"
+ "kColorPixelFormat_YCbCr422_10"
+ "kColorPixelFormat_YCbCr422_12"
+ "kColorPixelFormat_YCbCr422_8"
+ "kColorPixelFormat_YCbCr422_PQ_10"
+ "kColorPixelFormat_YCbCr422_PQ_12"
+ "kColorPixelFormat_YCbCr444_10"
+ "kColorPixelFormat_YCbCr444_12"
+ "kColorPixelFormat_YCbCr444_8"
+ "kColorPixelFormat_YCbCr444_PQ_10"
+ "kColorPixelFormat_YCbCr444_PQ_12"
+ "kColorRange_Full"
+ "kColorRange_Limited"
+ "kEDRRequestUncategorized"
+ "kHDRProcessingGCPGammaValueKey"
+ "kHDRProcessingHDRConstraintStrengthKey"
+ "kHDRProcessingScreenCaptureSessionKey"
+ "kUpdateReasonDisplayBrightness \"brightness_deadline\""
+ "kUpdateReasonDisplayBrightness \"edr_deadline\""
+ "kUpdateReasonDisplayBrightness \"needs_brightness_update\""
+ "kUpdateReasonDisplayBrightness \"set_allows_edr\""
+ "kUpdateReasonDisplayBrightness \"set_brightness_limit\""
+ "kUpdateReasonDisplayBrightness \"set_color_matrix\""
+ "kUpdateReasonDisplayBrightness \"set_contrast_preservation\""
+ "kUpdateReasonDisplayBrightness \"set_edr_properties\""
+ "kUpdateReasonDisplayBrightness \"set_high_ambient_adaptation_strength\""
+ "kUpdateReasonDisplayBrightness \"set_ib\""
+ "kUpdateReasonDisplayBrightness \"set_ib_limit\""
+ "kUpdateReasonDisplayBrightness \"set_irdc_hint\""
+ "kUpdateReasonDisplayBrightness \"set_low_ambient_adaptation_strength\""
+ "kUpdateReasonDisplayBrightness \"set_sdr_nits_1\""
+ "kUpdateReasonDisplayBrightness \"set_sdr_nits_2\""
+ "key-path-value"
+ "keyAmount"
+ "keyAngle"
+ "keyColor"
+ "keyHeight"
+ "keyHeightOffset"
+ "keyHeightScale"
+ "keySpread"
+ "keySpreadOffset"
+ "keySpreadScale"
+ "kfh"
+ "localEarlyWakeupOffset"
+ "lumaSubrect"
+ "lumaUpdateRate"
+ "mach-lookup"
+ "mach_make_memory_entry_64 (size %llu, addr 0x%llx, prot 0x%x, port %u) = 0x%x"
+ "maskOffset"
+ "max_desired_headroom"
+ "maximum %d texture units\n"
+ "maximum texture %d pixels\n"
+ "maximumDistance"
+ "maximumPoolMemory"
+ "mergeElements"
+ "mipmap_levels != 0"
+ "missing mask layer 0x%lx\n"
+ "missing sublayer %p\n"
+ "needsGlobalLightCallback"
+ "needsPreLayoutUpdate"
+ "newComputePipelineStateWithDescriptor:error:"
+ "newResidencySetWithDescriptor:error:"
+ "newSharedEventWithMachPort:"
+ "newTextureViewWithDescriptor:"
+ "offscreen_reasons_count"
+ "ogl-blur.cpp"
+ "ogl-imaging.cpp"
+ "oldest_surf"
+ "oneValueDistance"
+ "operation"
+ "outputBitDepth"
+ "overAllocationFactor"
+ "p0x=%g slope_adjusted=%g source_headroom=%g extension_offset=%g extension_weight=%g  a=%g b=%g c=%g d=%g e=%g p0y=%g p1y=%g p2y=%g target_headroom=%g output_gamma=%g luminance_scale=%g"
+ "padding"
+ "pass_count"
+ "path=%{public, name=path}s width=%{public, name=width}d height=%{public, name=height}d buffer=%{public, name=buffer}d level=%{public, name=level}u"
+ "plusDIgnoreAlpha"
+ "plusLIgnoreAlpha"
+ "postCommitDuration"
+ "preferredDynamicRange"
+ "preferred_dynamic_range"
+ "preferred_mode_with_criteria: target resolution [%g x %g] target rate (%g) target hdr (%s) user match content (%i), user preferred hdr type (%s) --> %dx%d@%g %s"
+ "process"
+ "punchout"
+ "purgePool"
+ "r == KERN_SUCCESS"
+ "r1"
+ "radius"
+ "rasterizeInParentSpace"
+ "read-display-identifier"
+ "referenceWhiteTonemapV1"
+ "remapAnimation:forKey:"
+ "remoteEffects"
+ "removeAllocation:"
+ "render cancel"
+ "render-flatten-cache.cpp"
+ "renderForTime called before render completed."
+ "renderForTime called without render completed callback."
+ "renderForTime:options:userInfo:onRenderBegin:onRenderComplete:"
+ "render_for_time statistics:\n%s"
+ "rendering error %s\n"
+ "replay"
+ "request"
+ "requestForEffect:"
+ "requestForEffects:"
+ "request_type"
+ "reset"
+ "residencySet"
+ "ret == 0"
+ "reuse surface 0x%x [%llu], %dx%d for the flipbook, memory pool usage = %.2lf %s, memory max pool = %.2lf %s, Free size: %zu"
+ "rsd"
+ "scd"
+ "sdf-element-layer"
+ "sdf-layer"
+ "sdf_gen_field"
+ "sdf_gen_gradients"
+ "send"
+ "separated"
+ "separatedOptions"
+ "separatedShadowCompositingFilter"
+ "separatedShadowReceiverCompositingFilter"
+ "separatedShadowReceiverMode"
+ "separatedState"
+ "serialization error from context %x\n"
+ "setAccessibilityBounds:"
+ "setAllowsColorMatching:"
+ "setAllowsCornerContentsEdgeEffects:"
+ "setAllowsFilteredLuma:"
+ "setAllowsRemoteEffectHitTesting:"
+ "setAmount:"
+ "setAngle:"
+ "setAutoresizingMask:"
+ "setBlendFactor:"
+ "setCompressionType:"
+ "setComputeFunction:"
+ "setConstraints:"
+ "setContentsCDRStrength:"
+ "setContentsHeadroom:"
+ "setContentsOneValueDistance:"
+ "setContentsZeroValueDistance:"
+ "setContrastPreservation:"
+ "setContrastPreservationBegin:"
+ "setContrastPreservationEnd:"
+ "setCreatesShadowGroup:"
+ "setCurvature:"
+ "setDisableFoveation:"
+ "setDisableFrameDoubling:"
+ "setDistances:"
+ "setEarlyWakeupOffset:"
+ "setEffect:"
+ "setEffectOffset:"
+ "setExcludeSeparated:"
+ "setFillAmount:"
+ "setFillAngle:"
+ "setFillHeight:"
+ "setFillHeightOffset:"
+ "setFillHeightScale:"
+ "setFillSpread:"
+ "setFillSpreadOffset:"
+ "setFillSpreadScale:"
+ "setFlattenMode:"
+ "setFloating:"
+ "setFramingOptions:"
+ "setFullyOccluded:"
+ "setGlobal:"
+ "setGlobalLightAngle:"
+ "setGlobalLightParameters:"
+ "setGradientOvalization:"
+ "setGradientSmoothing:"
+ "setHitTestsAsFill:"
+ "setHostingToken:"
+ "setIgnoreAnimations:"
+ "setImageblockWidth:height:"
+ "setIncludeGradient:"
+ "setInitialCapacity:"
+ "setInvert:"
+ "setInvertsContentsAreFlipped:"
+ "setKeyAmount:"
+ "setKeyAngle:"
+ "setKeyColor:"
+ "setKeyHeight:"
+ "setKeyHeightOffset:"
+ "setKeyHeightScale:"
+ "setKeySpread:"
+ "setKeySpreadOffset:"
+ "setKeySpreadScale:"
+ "setLayoutManager:"
+ "setLocalEarlyWakeupOffset:"
+ "setLumaSubrect:"
+ "setLumaUpdateRate:"
+ "setMargin:"
+ "setMaskOffset:"
+ "setMaximumDistance:"
+ "setMaximumPoolMemory:"
+ "setMergeElements:"
+ "setNeedsAuthoritativeHostingToken"
+ "setNeedsGlobalLightCallback:"
+ "setNeedsPreLayoutUpdate"
+ "setOneValueDistance:"
+ "setOperation:"
+ "setOutputBitDepth:"
+ "setOverAllocationFactor:"
+ "setPadding:"
+ "setPostCommitDuration:"
+ "setPreferredDynamicRange:"
+ "setPunchout:"
+ "setRadius:"
+ "setRasterizeInParentSpace:"
+ "setRemoteEffects:"
+ "setResponsibleProcess:"
+ "setSeparatedOptions:"
+ "setSeparatedShadowCompositingFilter:"
+ "setSeparatedShadowReceiverCompositingFilter:"
+ "setSeparatedShadowReceiverMode:"
+ "setSeparatedState:"
+ "setShadowEffectsOnWindowMaskOnly:"
+ "setSkipHitTesting:"
+ "setSmoothness:"
+ "setSourceLayerOpacityScale:"
+ "setSpread:"
+ "setTrackedLayerIDContent:"
+ "setUpdateBeginTime:"
+ "setWantsDynamicContentScaling:"
+ "setZeroValueDistance:"
+ "setZombificationMode:"
+ "setZombifyOnInvalidate:"
+ "set_dest"
+ "set_user_preferences (uuid=%s, matchContent=%i)"
+ "shadowEffectsOnWindowMaskOnly"
+ "signal clients display %u cloning state changed to %s"
+ "signalEvent:value:"
+ "signalOnCommandQueue:"
+ "size () <= _capacity && \"Invalid size\""
+ "size >= 1"
+ "skipHitTesting"
+ "skipHitTesting = YES"
+ "skipping"
+ "smoothness"
+ "sourceLayerOpacityScale"
+ "space_change"
+ "sparseTextureTier"
+ "spread"
+ "stage_entry"
+ "standard"
+ "stereo-metal-texture"
+ "subtractSIgnoreAlpha"
+ "subtraction"
+ "supportedHDRModesWithCriteria:"
+ "supportsLossyCompression"
+ "surf->surf"
+ "surface %d x %d is too large\n"
+ "surface_usage == kSurfaceUsageAssembly"
+ "sw renderer doesn't support tiling\n"
+ "swap %u : requested %.5f, presented at %.5f, diff %.5f\n"
+ "syncNotificationHotplugState"
+ "targetCloningState"
+ "time"
+ "timed out freeze semaphore\n"
+ "tokenFromXPCRepresentation:error:"
+ "tokenWithPort:data:error:"
+ "too many subdivisions in cubic curve (%a, %a) (%a, %a) (%a, %a) (%a, %a). Stack will most likely overflow. bail out."
+ "trackedLayerIDContent"
+ "transaction.value: %lld <= _last_iosurface_write_value: %lld"
+ "transactionAtIndex:"
+ "transitionToCloningState"
+ "transitionToCloningState:withCompletion:"
+ "transitionToDisplayState"
+ "triple buffered backing store %p\n"
+ "trying to create color from vec of len %zu"
+ "uintptr_t (dst) - uintptr_t (_encoded.frag_uniform) <= kMaxUniformSize"
+ "unable to encode NSValue of type %s"
+ "unable to set static PQ stats, no dictionary created."
+ "unhandled combiner function: %d\n"
+ "union"
+ "unsupported graphics hardware"
+ "update 0x%x track_headroom --> %f:\n%s"
+ "updateBeginTime"
+ "update_display_limits"
+ "update_metal_texture_"
+ "uploaded_bytes"
+ "usd"
+ "v->count () == 5"
+ "v112@?0I8I12Q16Q24Q32Q40I48B52B56B60f64f68f72Q76I84B88Q92Q100f108"
+ "v16@?0@\"CAFenceResolution\"8"
+ "v16@?0^{?=i(?={?=I}{?=CCCCC[3i]i[3i]f[8I]}{?=CCCCCC})}8"
+ "v16@?0r^{?=IIQQQQIBBBfffQIBQQf}8"
+ "v20@?0i8r^{?=i(?={?=fffffff}{?=If^f}{?=I[10I][10f][10[11f]]}{?=If^ff^f}{?=ffI}{?=fffff}{?=I}{?=fffff}{?=ffff}{?=fffff})}12"
+ "v24@0:8@\"<MTL4CommandQueue>\"16"
+ "v24@?0@\"CAFlipBookFrame\"8@\"NSError\"16"
+ "v28@0:8I16r^{CA_content_stream_frame_info=QQIIffffffC}20"
+ "v32@0:8^v16^v24"
+ "v56@0:8Q16@24@32@?40@?48"
+ "v96@0:8Q16I24Q28Q36f44f48Q52I60{CGRect={CGPoint=dd}{CGSize=dd}}64"
+ "variable_blur_clamp_downsample_frag"
+ "variable_blur_downsample_compute"
+ "vrc"
+ "waitForEvent:value:"
+ "waitOnCommandQueue:"
+ "waitValue"
+ "wantsDynamicContentScaling"
+ "warning, CGImageProvider returned multiple blocks\n"
+ "warning, deleted thread with uncommitted CATransaction; set CA_DEBUG_TRANSACTIONS=1 in environment to log backtraces, or set CA_ASSERT_MAIN_THREAD_TRANSACTIONS=1 to abort when an implicit transaction isn't created on a main thread.\n"
+ "warning, encountered thread with uncommitted CATransaction; set CA_DEBUG_TRANSACTIONS=1 in environment to log backtraces, or set CA_ASSERT_MAIN_THREAD_TRANSACTIONS=1 to abort when an implicit transaction isn't created on a main thread.\n"
+ "window-layer"
+ "xPort"
+ "xp"
+ "yuv unsupported"
+ "zPosition should be within (-FLT_MAX, FLT_MAX) range."
+ "zeroValueDistance"
+ "zombificationMode"
+ "zombifyOnInvalidate"
+ "{?=\"sid\"I\"pid\"i\"cid\"I\"type\"I}"
+ "{ModeSet={vector<CA::WindowServer::Display::Mode, std::allocator<CA::WindowServer::Display::Mode>>=^{Mode}^{Mode}^{Mode}}{set<std::tuple<unsigned short, unsigned short>, std::less<std::tuple<unsigned short, unsigned short>>, std::allocator<std::tuple<unsigned short, unsigned short>>>={__tree<std::tuple<unsigned short, unsigned short>, std::less<std::tuple<unsigned short, unsigned short>>, std::allocator<std::tuple<unsigned short, unsigned short>>>=^v{__tree_end_node<std::__tree_node_base<void *> *>=^v}Q}}{unordered_map<unsigned long long, CA::Render::PerModeInfo, std::hash<unsigned long long>, std::equal_to<unsigned long long>, std::allocator<std::pair<const unsigned long long, CA::Render::PerModeInfo>>>={__hash_table<std::__hash_value_type<unsigned long long, CA::Render::PerModeInfo>, std::__unordered_map_hasher<unsigned long long, std::__hash_value_type<unsigned long long, CA::Render::PerModeInfo>, std::hash<unsigned long long>, std::equal_to<unsigned long long>>, std::__unordered_map_equal<unsigned long long, std::__hash_value_type<unsigned long long, CA::Render::PerModeInfo>, std::equal_to<unsigned long long>, std::hash<unsigned long long>>, std::allocator<std::__hash_value_type<unsigned long long, CA::Render::PerModeInfo>>>={unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CA::Render::PerModeInfo>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CA::Render::PerModeInfo>, void *> *> *>>>=^^v{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CA::Render::PerModeInfo>, void *> *> *>>=Q}}{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned long long, CA::Render::PerModeInfo>, void *> *>=^v}Qf}}I}16@0:8"
+ "{small_vector<ContentStreamClientFrame, 8UL>=\"_begin\"^{ContentStreamClientFrame}\"_end\"^{ContentStreamClientFrame}\"_fixedStorage\"^{ContentStreamClientFrame}\"_capacity\"Q\"\"(?=\"storage\"[8(type=\"__data\"[16C])]\"flat_storage\"[0{ContentStreamClientFrame=\"iosurface\"^{__IOSurface}\"id\"I\"port\"I}])}"
+ "{unordered_map<unsigned int, unsigned int, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, unsigned int>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>>=\"__ptr_\"^^v\"__deleter_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>=\"__size_\"Q}}\"__first_node_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *>=\"__next_\"^v}\"__size_\"Q\"__max_load_factor_\"f}}"
- "\tFlex Luminance Scaling params:\n\t\tsource headroom = % 3.10f\n\t\ttarget headroom = % 3.10f\n\t\tcoefficients[0] = % 3.10f\n\t\tcoefficients[1] = % 3.10f\n\t\tcoefficients[2] = % 3.10f\n\t\tcoefficients[3] = % 3.10f\n\t\tcoefficients[4] = % 3.10f\n\t\tFlexGTCTableCount = %zu\n\t\tFlexGTCTable = %p\n"
- "\n\f\n** Log started %s **\n\n"
- "    Surface 0x%x (%.2lf %s) @ %f (%s), seed %u enqueued"
- "  a: %g, b: %g, c: %g, d: %g, e: %g, lum_sat_factor: %g, luminance_scale: %g, source headroom: %g, target    headroom: %g, target_reference_white: %g"
- " (tint %.3g %.3g %.3g %.3g)"
- " high bandwidth"
- "!_shared_event"
- "!tex_info.arg && tex_info.layout.fields[0].count == 0"
- "%20s  SharedEvent IOSurface ID: 0x%16llx  Usage: %23s  Operation: %9s  Access: %6s  Value: 0x%16llx\n"
- "%a %b %e %H:%M:%S %Z %Y"
- "%f %x \"%s\" (%p): adding %p:\n"
- "%f %x \"%s\" (%p): collecting %p (t %f; speed %g; eval %u; frames %u):\n"
- "%f %x \"%s\" (%p): not adding %p:\n"
- "%f %x \"%s\" (%p): removing %p (eval %u; frames %u):\n"
- "%f %x \"%s\" (%p): removing all:\n"
- "%f %x \"%s\" (%p): replacing %p (eval %u; frames %u):\n"
- "%s%.*s"
- "%s: exception %@"
- "%sctx-%x_%s(%d).png"
- "%zu start ctxs ["
- "(backgroundColor (%.3g %.3g %.3g %.0g))"
- "(borderColor (%.3g %.3g %.3g %.0g))"
- "(contentsMultiplyColor %.3g %.3g %.3g %.3g)"
- "(fillColor %.3g %.3g %.3g %.3g)"
- "(flush) signal clients display %u state changed to %s"
- "(rimColor (%.3g %.3g %.3g %.0g))"
- "(send) signal clients display %u state changed to %s"
- "(shadowColor (%.3g %.3g %.3g %.0g))"
- "(strokeColor %.3g %.3g %.3g %.3g)"
- "-[CAFlipBook renderForTime:options:userInfo:error:]"
- "-[CAPackage _readFromArchiveData:options:error:]"
- "/System/Library/PrivateFrameworks/libEDR.framework/libEDR"
- "22F63"
- "<CAFlipBook: maximumSize %zu, generation %u, contextId 0x%x>"
- "@40@0:8^{_CAMetalDrawablePrivate={Atomic={?=i}}IIIQQQQd^{_CAMetalLayerPrivate}^{__IOSurface}@@^{CGColorSpace}@@Cb1b1b1b1b1b1b1}16@24d32"
- "B16@?0^{?=III^{__CFString}^{__CFString}^{__CFString}^QQQQ^?dddIIB}8"
- "B24@?0@\"CALocalDisplay\"8^{?=III^{__CFString}^{__CFString}^{__CFString}^QQQQ^?dddIIB}16"
- "B28@0:8^v16I24"
- "CA Flattened Surface"
- "CABackingStoreBeginUpdate"
- "CADisplayDidChangeToState display_id=%u, state=%s, seed=%u, result=%s"
- "CADisplayStateControl didChangeToState=%s display_id=%u seed=%u result=%s"
- "CADisplayStateControl transition display_id=%u seed=%u interrupted"
- "CADisplayStateControl transitionToDisplayState=%s, display_id=%u, seed=%u, completion=%p"
- "CALinearMaskLayer"
- "CAML error:%d: "
- "CAML warning:%d: "
- "CASecureIndicatorLayerValidDynamicPositionsForIndicator: name can't be nil"
- "CASecureIndicatorLayerValidPositionsForIndicator: name can't be nil"
- "CASmoothedTextLayer"
- "CA_ENABLE_PREFERS_TRIPLE_BUFFERING"
- "CA_ENABLE_TRIPLE_BUFFERED_TTL"
- "CA_ENABLE_WIRELESS_DISPLAY_PROTECTION"
- "CA_FORCE_TIMER"
- "CA_FORCE_TRIPLE_BUFFERING"
- "CA_SKIP_CONTENT_ON_CLONE_PROTECTION_MISMATCH"
- "CG image cache at time %f:\n"
- "Cannot send %zu bytes to the server. This exceeds mach ool capabilities!"
- "Client mach port creation failed 0x%x : %s"
- "ContextInfo"
- "CoreAnimation: %d by %d image is too large for GPU, ignoring\n"
- "CoreAnimation: %d by %d image is too large for software renderer, ignoring\n"
- "CoreAnimation: Async render times array exceed maximum size."
- "CoreAnimation: CALocalDisplayUpdateBlock returned NO\n"
- "CoreAnimation: Failed to initialize Metal or OpenGLES contexts!"
- "CoreAnimation: GetDisplayInfo returned 0x%x\n"
- "CoreAnimation: IOSurface 0x%x ('%c%c%c%c') has unexpected bytes-per-row value of %zu, expected at least %zu for the width of %zu."
- "CoreAnimation: IOSurface 0x%x [%u x %u] doesn't have the proper data alignment! Expected %zu base address and %zu row byte alignment\n"
- "CoreAnimation: Invalid Secure Flipbook type %@"
- "CoreAnimation: LayerHost trying to host itself or one of its ancestors (context id %d)\n"
- "CoreAnimation: Maximum flipbook size %u ignored. Using %zu."
- "CoreAnimation: Message::send_message() returned 0x%x\n"
- "CoreAnimation: NULL color space set on context (%x)\n"
- "CoreAnimation: Software renderer! Simulating crash!\n"
- "CoreAnimation: Warning! CAImageQueueSetOwner() is deprecated and does nothing. Please stop calling this method.\n"
- "CoreAnimation: [CAContext setFence:count:] is deprecated. Ignoring!"
- "CoreAnimation: [CADisplay allowsVirtualModes] is deprecated!"
- "CoreAnimation: [CADisplay colorMode] is deprecated!"
- "CoreAnimation: [CADisplay setAllowsVirtualModes] is deprecated!"
- "CoreAnimation: [CADisplay setColorMode:] is deprecated!"
- "CoreAnimation: [CAWindowServerDisplay setColorMode:] is deprecated!"
- "CoreAnimation: [EAGLContext renderbufferStorage:fromDrawable:] was called from a non-main thread in an implicit transaction! Note that this may be unsafe without an explicit CATransaction or a call to [CATransaction flush]."
- "CoreAnimation: changing `contents' on CAMetalLayer may result in undefined behavior\n"
- "CoreAnimation: clone failed to copy detached layer - Disabling detachment"
- "CoreAnimation: context hosting changed while locked!\n"
- "CoreAnimation: copied CGImageRef %p - RGB mask (bug!)\n"
- "CoreAnimation: copied CGImageRef %p - bad RGB image format (%d bpp, %d bpc, %d info)\n"
- "CoreAnimation: copied CGImageRef %p - bad alignment for IOSurface 0x%x\n"
- "CoreAnimation: copied CGImageRef %p - bad decode array\n"
- "CoreAnimation: copied CGImageRef %p - bad grayscale image format (%d bpp, %d bpc, %d info)\n"
- "CoreAnimation: copied CGImageRef %p - bad image alignment\n"
- "CoreAnimation: copied CGImageRef %p - bad mask\n"
- "CoreAnimation: copied CGImageRef %p - bad mask image format (%d bpp, %d bpc)\n"
- "CoreAnimation: copied CGImageRef %p - bad row alignment\n"
- "CoreAnimation: copied CGImageRef %p - decode or mask\n"
- "CoreAnimation: copied CGImageRef %p - format not supported by hardware\n"
- "CoreAnimation: copied CGImageRef %p - image size (%lu x %lu) exceeds max texture size\n"
- "CoreAnimation: copied CGImageRef %p - mask size\n"
- "CoreAnimation: copied CGImageRef %p - mipmap generation\n"
- "CoreAnimation: copied CGImageRef %p - needs color matching\n"
- "CoreAnimation: copied CGImageRef %p - no data pointer\n"
- "CoreAnimation: copied CGImageRef %p - non-RGB color model\n"
- "CoreAnimation: copied CGImageRef %p - non-native format (%d)\n"
- "CoreAnimation: damping must be greater than or equal to 0."
- "CoreAnimation: data provider size invalid"
- "CoreAnimation: data provider size is too small"
- "CoreAnimation: disabling OpenGL extension %s\n"
- "CoreAnimation: failed to add monotonic cube ((%g, %g) (%g, %g) (%g, %g) (%g, %g))\n"
- "CoreAnimation: failed to allocate %ld bytes\n"
- "CoreAnimation: failed to copy main layer"
- "CoreAnimation: failed to create Metal context!\n"
- "CoreAnimation: failed to lock IOSurface %x\n"
- "CoreAnimation: failed to query region %p (%zu bytes)\n"
- "CoreAnimation: forcing %saccelerated backing\n"
- "CoreAnimation: ignored CGImageRef %p - bad RGB 16-is-half format (%d bpp, %d bpc, %d info)\n"
- "CoreAnimation: ignored CGImageRef %p - bad grayscale 16-is-half format (%d bpp, %d bpc, %d info)\n"
- "CoreAnimation: ignoring exception: %@"
- "CoreAnimation: ignoring invalid path\n"
- "CoreAnimation: image stride is too large for GPU, ignoring\n"
- "CoreAnimation: insecure context %x - pid %u [%s].\n"
- "CoreAnimation: invalid commit handler phase! Defaulting to pre-commit.\n"
- "CoreAnimation: invalid mesh transform - paired edge\n"
- "CoreAnimation: invalid mesh transform - too few edges\n"
- "CoreAnimation: invalid mesh transform - vertex index\n"
- "CoreAnimation: mass must be greater than 0."
- "CoreAnimation: maximum %d texture units\n"
- "CoreAnimation: maximum texture %d pixels\n"
- "CoreAnimation: missing mask layer 0x%lx\n"
- "CoreAnimation: missing sublayer %p\n"
- "CoreAnimation: rendering error %s\n"
- "CoreAnimation: serialization error from context %x\n"
- "CoreAnimation: stiffness must be greater than 0."
- "CoreAnimation: surface %d x %d is too large\n"
- "CoreAnimation: sw renderer doesn't support tiling\n"
- "CoreAnimation: swap %u : requested %.5f, presented at %.5f, diff %.5f\n"
- "CoreAnimation: timed out freeze semaphore\n"
- "CoreAnimation: too many subdivisions in cubic curve (%a, %a) (%a, %a) (%a, %a) (%a, %a). Stack will most likely overflow. bail out."
- "CoreAnimation: triple buffered backing store %p\n"
- "CoreAnimation: unable to encode NSValue of type %s"
- "CoreAnimation: unable to set static PQ stats, no dictionary created."
- "CoreAnimation: unhandled combiner function: %d\n"
- "CoreAnimation: unsupported graphics hardware"
- "CoreAnimation: warning, CGImageProvider returned multiple blocks\n"
- "CoreAnimation: warning, deleted thread with uncommitted CATransaction; created by:\n"
- "CoreAnimation: warning, deleted thread with uncommitted CATransaction; set CA_DEBUG_TRANSACTIONS=1 in environment to log backtraces, or set CA_ASSERT_MAIN_THREAD_TRANSACTIONS=1 to abort when an implicit transaction isn't created on a main thread.\n"
- "CoreAnimation: warning, encountered thread with uncommitted CATransaction; created by:\n"
- "CoreAnimation: warning, encountered thread with uncommitted CATransaction; set CA_DEBUG_TRANSACTIONS=1 in environment to log backtraces, or set CA_ASSERT_MAIN_THREAD_TRANSACTIONS=1 to abort when an implicit transaction isn't created on a main thread.\n"
- "CoreAnimation: zPosition should be within (-FLT_MAX, FLT_MAX) range."
- "Couldn't allocate buffer of %zu bytes for message!"
- "Display %d commitBrightness sdr: %g, headroom: %g, potential headroom: %g, ambient lux: %g, filtered ambient: %g, brightness limit: %g, indicator brightness: %g low ambient strength: %g, high ambient strength: %g, contrast enhancer: %g brightness ctl disabled %d, unlogged brightness transactions:%u\n"
- "Display %u swap brightness: %g, limit: %g, indicator brightness: %g, ambient lux: %g, low ambient strength: %g, high ambient strength: %g, contrast enhancer: %g\n"
- "Display is not ready"
- "DisplayID: %u brightness capabilities set to %s"
- "DisplayID: %u got brightness capabilities %s"
- "DisplayID: %u simulating HDR10 brightness capabilities %s"
- "Does not need render"
- "EDRGetDefaultMinScalingFactor"
- "Encoder size overflow, old size = %zu, extra = %zu\n"
- "Error initializing HDRProcessor."
- "FATAL: Could not create backwardDM display properties!"
- "FFR_raw_index"
- "Failed to allocate %zu bytes, requested = %zu, old size = %zu\n"
- "Failed to create IOSurfaceAccelerator: 0x%x"
- "Failed to create SILManager, aborting..."
- "Failed to create thread (%d) - %s"
- "Failed to get server port type (%x) - %s"
- "Failed to initialize HDRBackwardDisplayManagement!"
- "Film Grain Query Failed 0x%x error0x%x"
- "Filter merging failed.\nFilter A:"
- "Finish update requested to try again"
- "Found matching color program %p in %s cache at %d for color matching from '%s' to '%s'. Search parameters: ri=%d flags=0x%x cube_size=%u tonemap_headroom=%f content_headroom=%f target_nits=%f tm=%d dynamic_tm=%d need_target_nits=%d. Color program: ri=%d flags=0x%x cube_size=%u tonemap_headroom=%f content_headroom=%f target_nits=%f."
- "FrameLifetime"
- "ID is swap ID. %{public, signpost.description:begin_time}llu frame_seed=%{public, name=frame_seed}#x refresh_interval=%{public, name=refresh_interval}llu buffer_count=%{public, name=buffer_count}hhu %{public, signpost.description:end_time}llu prev_frame=%{public, name=prev_frame}llu skip_request=%{public, name=skip_request}hhu display_id=%{public, name=display_id}u surface_id=%{public, name=surface_id}#x presentation_modifier_display_target_mct=%{public, name=presentation_modifier_display_target_mct}llu"
- "ID is swap ID. %{public, signpost.description:begin_time}llu frame_seed=%{public, name=frame_seed}#x refresh_interval=%{public, name=refresh_interval}llu buffer_count=%{public, name=buffer_count}hhu %{public, signpost.description:end_time}llu prev_frame=%{public, name=prev_frame}llu skip_request=%{public, name=skip_request}hhu display_id=%{public, name=display_id}u surface_id=%{public, name=surface_id}#x presentation_modifier_display_target_mct=%{public, name=presentation_modifier_display_target_mct}llu input_time=%{public, name=input_time}llu"
- "ID is update seed. refresh_interval=%{public, name=refresh_interval}llu display_id=%{public, name=display_id}#x %{public, signpost.description:begin_time}llu"
- "ID is update seed. refresh_interval=%{public, name=refresh_interval}llu display_id=%{public, name=display_id}#x %{public, signpost.description:begin_time}llu pass_count=%{public, name=pass_count}hu compile_count=%{public, name=compile_count}hu cache_misses=%{public, name=cache_misses}hu fallback_draws=%{public, name=fallback_draws}hu reasons=%{public, name=reasons}llu"
- "ID is update seed. refresh_interval=%{public, name=refresh_interval}llu display_id=%{public, name=display_id}#x %{public, signpost.description:begin_time}llu pass_count=%{public, name=pass_count}hu compile_count=%{public, name=compile_count}hu cache_misses=%{public, name=cache_misses}hu fallback_draws=%{public, name=fallback_draws}hu reasons=%{public, name=reasons}llu skipped_render_reason=%{public, name=skipped_render_reason}s render_status=%{public, name=render_status}x"
- "ID is update seed. refresh_interval=%{public, name=refresh_interval}llu display_id=%{public, name=display_id}#x %{public, signpost.description:begin_time}llu skipped_render_reason=%{public, name=skipped_render_reason}s render_status=%{public, name=render_status}x"
- "IOMFBDisplay::set_enabled=%u"
- "IOMFBDisplay::set_enabled_ display_id=%u, current_state=%s"
- "IOMobileFramebufferSetAmmoliteStrength"
- "IOMobileFramebufferSwapSetToneMapConfig"
- "IOSurfaceID: 0x%x  usage: %s  operation: %s  access: %s  value: %#llx"
- "Invalid TextureEdgeMode 0x%x"
- "Invalid frame interval range %u %u %u from frame rate range %.2f %.2f %.2f"
- "Invalid frame interval range (%d %d %d) or target interval (%d)"
- "Invalid runloop"
- "Invalid update"
- "Invalid update!"
- "LUT file \"%s.dat\" not found!\n"
- "LocationID"
- "LowPowerMode=%i"
- "Message buffer underflow, diff: %lld, msgh_size: %lld, desc: %p, _msg: %p!"
- "Message is batched CommandStream, but no batch ports, desc_count: %zu, port->type:%u!"
- "Message is ool CommandStream, but no body, desc_count: %zu, body_ool->type:%u!"
- "Metal failed to load binary archive"
- "Metal failed to load pipeline library"
- "Metal failed to load render pipeline"
- "No GPU work needed"
- "No content"
- "No matching program in %s cache after %d; ri %d; f 0x%x; cu %d; src %s; dst %s; dt %s; targ_hr %f; source_hr %f; nn %s; tn %f"
- "ODHN"
- "ODOn"
- "Occlusion"
- "Out of bounds access at index %ld to array with count of %ld!\n"
- "Overdrive"
- "P0553Xm_A2Xghfc"
- "PBGRABaddXmw_TimgA3Xhf_Ialp"
- "PBGRABamlXmw_TimgA3Xhf_Icir"
- "PBGRABdotXmw_TimgA3Xhf_IsrcM1"
- "PBGRABmaxXmw_TbibA3S1Xhf"
- "PBGRABmulXmw_TcmaA3LlnXhf"
- "PBGRABmulXmw_TcmaA3S1LlnXhf"
- "PBGRABmulXmw_TimgA3S1Xhf_Icir"
- "PBGRABmulXmw_TimgA3S1Xhf_Iuec"
- "PBGRABmulXmw_TimgA3Xhf_Icir"
- "PBGRABmulXmw_TpblA3S1Xhf"
- "PBGRABmulXmw_Tpc1A3Xhf"
- "PBGRABmulXmw_TprcA3Xhf"
- "PBGRABsodXmw_A3Xhf"
- "PBGRABsodXmw_TirbA3Xhf_Isrc"
- "PBGRABsovXm_A2Xhf"
- "PBGRABsovXm_TcimA2Xhf_Ialp"
- "PBGRABsovXm_TcimA2Xhf_Icir"
- "PBGRABsovXm_TcimA2Xhf_Igrn"
- "PBGRABsovXm_TcimA2Xhf_Ired"
- "PBGRABsovXm_TcimA2Xhf_Isrc"
- "PBGRABsovXm_TcimA2Xhf_IsrcN3Oc3mtc4nlnlnl"
- "PBGRABsovXm_TcimA2Xhf_Isup"
- "PBGRABsovXm_TcmaA2LlnXhf"
- "PBGRABsovXm_TimgA2S1Xhf_Iara"
- "PBGRABsovXm_TimgA2Xhf_Ialp"
- "PBGRABsovXm_TimgA2Xhf_Igrn"
- "PBGRABsovXm_TimgA2Xhf_Isrc"
- "PBGRABsovXm_TimgA2Xhf_IsrcCcl"
- "PBGRABsovXm_TimgA2Xhf_Isrg"
- "PBGRABsovXm_TimgA2Xhfn_IsrcCcl"
- "PBGRABsovXm_TimgA2Xhfn_IsrcCrd"
- "PBGRABsovXm_Tm1aA2Xhf_Icir_Icir"
- "PBGRABsovXm_Tm1aA2Xhf_Isup_Isup"
- "PBGRABsovXm_TmuaA2Xhf_Ired_Isqr"
- "PBGRABsovXm_TmuaA2Xhfn_IsrcCcl_Isup"
- "PBGRABsovXmw_A3Xhf"
- "PBGRABsovXmw_A3Xhfc"
- "PBGRABsovXmw_A3Xhfcn"
- "PBGRABsovXmw_A3Xhfn"
- "PBGRABsovXmw_TbibA3Xhf"
- "PBGRABsovXmw_TcimA3Xhf_Ialp"
- "PBGRABsovXmw_TcimA3Xhf_Icir"
- "PBGRABsovXmw_TcimA3Xhf_Isrc"
- "PBGRABsovXmw_TcimA3Xhf_Iuec"
- "PBGRABsovXmw_TcmaA3LlnXhf"
- "PBGRABsovXmw_TcmaA3Xhfcn"
- "PBGRABsovXmw_TimgA3Xhf_Icir"
- "PBGRABsovXmw_TimgA3Xhf_Isrc"
- "PBGRABsovXmw_TimgA3Xhf_IsrcM1"
- "PBGRABsovXmw_TimgA3Xhfc_Isrc"
- "PBGRABsovXmw_TimgA3Xhfcn_IsrcN3Ocsmtsdnlnlnl"
- "PBGRABsovXmw_TirbA3Xhf_Isrc"
- "PBGRABsovXmw_TpblA3Xhf"
- "PBGRABsovXmw_Tpc0A3Xhf"
- "PBGRABsovXmw_Tpc1A3Xhf"
- "PBGRABsovXmw_TprcA3Xhf"
- "PBGRABsovXmw_Tps0A3Xhf"
- "PBGRABsovXmw_TpsmA3Xhf"
- "PBGRABsovXmw_TpsrA3Xhf"
- "PBGRABsovXmw_TsplA3Xhf_Isrc"
- "PBGRABsovXmw_TsplA3Xhf_IsrcM1"
- "PBGRABsovXmw_TsplA3Xhfc_IsrcM1"
- "PBGRAXm_A2Xhf"
- "PBGRAXm_BvcmA2Xhf"
- "PBGRAXm_TbdsA2Xhf_Icir_Isrc"
- "PBGRAXm_TbdsA2Xhf_Isup_Isrc"
- "PBGRAXm_Tc33A2Xhf_Idst"
- "PBGRAXm_Tc3bA2Xhf_Idst"
- "PBGRAXm_TcimA2Xhf_Icir"
- "PBGRAXm_TcmaA2LlnXhf"
- "PBGRAXm_TimgA2Xhf_Isrc"
- "PBGRAXm_TimgA2Xhf_Ixrg"
- "PBGRAXm_TimgA2Xhfcn_IxrgN3OcsmtsdnlnlnlXq"
- "PBGRAXm_TimgA2Xhfn_Isrc"
- "PBGRAXm_TimgBvcmA2Xhf_Ialp"
- "PBGRAXm_TimgBvcmA2Xhfn_Isrc"
- "PBGRAXm_TmpcA2Xhf_Idst"
- "PBGRAXm_TmpcA2Xhfc_Idst"
- "PBGRAXm_Tsb3A2Xhf_Isrc"
- "PBGRAXmw_A3S1Xhf"
- "PBGRAXmw_A3Xhf"
- "PBGRAXmw_A3Xhfc"
- "PBGRAXmw_A3Xhfcn"
- "PBGRAXmw_BclrA3Xhf"
- "PBGRAXmw_BsdsA3Xhf"
- "PBGRAXmw_TatcA3S1Xhf"
- "PBGRAXmw_TcimBmpyA3Xhfc_Icir"
- "PBGRAXmw_TcmaA3LlnXhf"
- "PBGRAXmw_TcmaBmpyA3LlnXhfc"
- "PBGRAXmw_TimgA3Xhf_Ialp"
- "PBGRAXmw_TimgA3Xhf_Isrc"
- "PBGRAXmw_TimgA3Xhf_Isxr"
- "PBGRAXmw_TimgA3Xhf_Ixrg"
- "PBGRAXmw_TimgA3Xhfc_Isrc"
- "PBGRAXmw_TimgA3Xhfc_Ixrg"
- "PBGRAXmw_TimgBsdsA3Xhf_Isrc"
- "PBGRAXmw_TirbA3Xhf_Isrc"
- "PLA88Xm_A2Xghfc"
- "PRGhAXm_Tc3bA2Xhfcu_Idst"
- "PRGhAXm_TcabA2Xhf_Isrc"
- "PRGhAXm_Tds8A2Xhf_Isrc"
- "PRGhAXm_ThomA2Xhf_Isrc_Isrc"
- "PRGhAXm_TimgA2Xhfcue_Isrc"
- "PRGhAXm_TmapA2Xhfcu_Idst_Isr1Clm"
- "PRGhAXm_Tn11A2Xhf_Isrc"
- "PRGhAXm_Tn15A2Xhf_Isrc"
- "PRGhAXm_Tn19A2Xhf_Isrc"
- "PRGhAXm_Tn23A2Xhf_Isrc"
- "Pb3a8BaddXm_A2Xhfcx"
- "Pb3a8BmaxXmw_TbibA3S1Xhf"
- "Pb3a8BmulXmw_A3S1Xhfcx"
- "Pb3a8BmulXmw_TcmaA3S1LlnXhfcx"
- "Pb3a8BmulXmw_TimgA3S1Xhfcx_Icir"
- "Pb3a8BmulXmw_TimgA3S1Xhfcx_Iuec"
- "Pb3a8BmulXmw_TpblA3S1Xhf"
- "Pb3a8BmulXmw_Tpc0A3Xhf"
- "Pb3a8BmulXmw_Tpc1A3Xhf"
- "Pb3a8BmulXmw_TprcA3Xhf"
- "Pb3a8BsovXm_TcimA2S1Xhfcx_Ialp"
- "Pb3a8BsovXm_TcimA2S1Xhfcx_Isrc"
- "Pb3a8BsovXm_TcimA2Xhfcx_IsrgCcl"
- "Pb3a8BsovXm_TimgA2S1Xhfcx_Isrc"
- "Pb3a8BsovXm_TimgA2Xhfcx_Isar"
- "Pb3a8BsovXm_TimgA2Xhfcxs_Iara"
- "Pb3a8BsovXm_TmuaA2Xhfcx_IsrcCcl_Icir"
- "Pb3a8BsovXm_TmuaA2Xhfcx_IsrcCcl_Isup"
- "Pb3a8BsovXm_TmuaA2Xhfcx_Isrc_Icir"
- "Pb3a8BsovXm_TmuaA2Xhfcx_Ixrg_Isup"
- "Pb3a8BsovXmw_A3Xhfcxn"
- "Pb3a8BsovXmw_TcimA3Xhfcx_Irrg"
- "Pb3a8BsovXmw_TcimA3Xhfcx_Isqr"
- "Pb3a8BsovXmw_TcimA3Xhfcx_Isrc"
- "Pb3a8BsovXmw_TcimA3Xhfcx_Iuec"
- "Pb3a8BsovXmw_TimgA3Xhfcx_Isar"
- "Pb3a8BsovXmw_TimgA3Xhfcx_IsrcCcl"
- "Pb3a8BsovXmw_TimgA3Xhfcx_IsrcM1"
- "Pb3a8BsovXmw_TimgA3Xhfcx_IsrcN3Oc4sdnlnlnlnl"
- "Pb3a8BsovXmw_TimgA3Xhfcx_Iuec"
- "Pb3a8BsovXmw_Tm1aA3Xhfcx_Icir_Icir"
- "Pb3a8BsovXmw_Tps0A3Xhf"
- "Pb3a8BsovXmw_TpsmA3Xhf"
- "Pb3a8BsovXmw_TpsrA3Xhf"
- "Pb3a8BsovXmw_Ts1aA3Xhfcx_Ialp"
- "Pb3a8BsovXmw_TstlA3Xhf"
- "Pb3a8Xm_Tc3bA2S1Xhfcx_Idst"
- "Pb3a8Xm_TcmaA2S1LlnXhfcx"
- "Pb3a8Xm_TedrA2Xhfn"
- "Pb3a8Xm_TimgA2S1Xhfcx_IsrcM0"
- "Pb3a8Xm_TimgA2Xhfcx_Isr1"
- "Pb3a8Xm_TimgA2Xhfcx_IsrcM1"
- "Pb3a8Xm_TimgA2Xhfcx_IxrgN3Oc4c4nlnlnlnlXq"
- "Pb3a8Xm_TimgBvcmA2Xhfcx_Ired"
- "Pb3a8Xmw_A3S1Xhfcx"
- "Pb3a8Xmw_A3S1Xhfcxn"
- "Pb3a8Xmw_A3Xhfcxn"
- "Pb3a8Xmw_TbimBcpyA3Xhfcx_Isrc_Isrc"
- "Pb3a8Xmw_TcimA3S1Xhfcx_Isrc"
- "Pb3a8Xmw_TcmaA3S1LlnXhfcx"
- "Pb3a8Xmw_TcmaA3S1Xhfcxn"
- "Pb3a8Xmw_TimgA3S1Xhfcx_Icir"
- "Pb3a8Xmw_TimgA3S1Xhfcx_Isrc"
- "Pb3a8Xmw_TimgA3S1Xhfcx_Iuec"
- "Pb3a8Xmw_TimgA3Xhfcx_Isxr"
- "Pb3a8Xmw_TimgA3Xhfcx_Ixrg"
- "Pb3a8Xmw_TimgA3Xhfcx_IxrgCcl"
- "Pb3a8Xmw_TirbA3Xhf_Isrc"
- "Pb3a8Xmw_TpblA3S1Xhf"
- "Pb3a8Xmw_Tpc0A3Xhf"
- "Pb3a8Xmw_Tpc1A3Xhf"
- "Pb3a8Xmw_TprcA3Xhf"
- "Pb3a8Xmw_Tps0A3Xhf"
- "Pipeline %s excludes %@\n"
- "Pipeline %s requires %@\n"
- "Posting %s, payload: %s"
- "Pw30rBdotXm_TcmaA2S1LlnXhfcx"
- "Pw30rBdotXm_TimgA2S1Xhfcx_Isrg"
- "Pw30rBdotXm_TimgA2S1Xhfcx_IsrgCtl"
- "Pw30rBmaxXmw_TbibA3S1Xhf"
- "Pw30rBmulXmw_A3S1Xhfcx"
- "Pw30rBmulXmw_TcmaA3S1LlnXhfcx"
- "Pw30rBmulXmw_TimgA3S1Xhfcx_Icir"
- "Pw30rBmulXmw_TimgA3S1Xhfcx_Iuec"
- "Pw30rBmulXmw_TpblA3S1Xhf"
- "Pw30rBmulXmw_Tpc0A3Xhf"
- "Pw30rBmulXmw_Tpc1A3Xhf"
- "Pw30rBmulXmw_TprcA3Xhf"
- "Pw30rBsovXm_Tc4bA2Xhfcx_IsrcM1"
- "Pw30rBsovXm_Tc4bA2Xhfcxs_IsrcM1"
- "Pw30rBsovXm_TcimA2S1Xhfcx_Ialp"
- "Pw30rBsovXm_TcimA2S1Xhfcx_IalpCcl"
- "Pw30rBsovXm_TcimA2S1Xhfcx_Isup"
- "Pw30rBsovXm_TcimA2Xhfcxs_Isrc"
- "Pw30rBsovXm_TcmaA2S1LlnXhfcx"
- "Pw30rBsovXm_TimgA2S1Xhfcx_Ialp"
- "Pw30rBsovXm_TimgA2S1Xhfcx_IalpCcl"
- "Pw30rBsovXm_TimgA2S1Xhfcx_Iara"
- "Pw30rBsovXm_TimgA2S1Xhfcx_Isrc"
- "Pw30rBsovXm_TimgA2S1Xhfcx_Isrg"
- "Pw30rBsovXm_TimgA2S1Xhfcxn_IsrcCrd"
- "Pw30rBsovXm_TimgA2Xhfcx_IsrcN3Oc3mtc4nlnlnl"
- "Pw30rBsovXm_TimgA2Xhfcx_IsrcN3Ocsmtsdnlnlnl"
- "Pw30rBsovXm_TimgA2Xhfcxn_IsrcN3Oc0c4nlnlnlnl"
- "Pw30rBsovXm_TimgA2Xhfcxn_IsrcN3Oc0sdnlnlnlnl"
- "Pw30rBsovXm_TimgA2Xhfcxs_Ired"
- "Pw30rBsovXm_TimgA2Xhfcxs_Isrc"
- "Pw30rBsovXm_TimgA2Xhfcxs_IsrcCcl"
- "Pw30rBsovXm_TmuaA2S1Xhfcx_Ired_Isqr"
- "Pw30rBsovXm_TmuaA2Xhfcxs_Isrc_Isqr"
- "Pw30rBsovXm_TmuaA2Xhfcxs_Isrc_IsrcM1"
- "Pw30rBsovXm_TmuaA2Xhfcxs_Ixrg_Isrg"
- "Pw30rBsovXm_TvcmA2Xhfcxs_IsrcM1"
- "Pw30rBsovXmw_A3Xhfcxn"
- "Pw30rBsovXmw_TcimA3Xhfcx_Ialp"
- "Pw30rBsovXmw_TcimA3Xhfcx_Irrg"
- "Pw30rBsovXmw_TcimA3Xhfcx_Isqr"
- "Pw30rBsovXmw_TcimA3Xhfcx_Isrc"
- "Pw30rBsovXmw_TcimA3Xhfcx_Iuec"
- "Pw30rBsovXmw_TimgA3Xhfcx_Isar"
- "Pw30rBsovXmw_TimgA3Xhfcx_IsrcCcl"
- "Pw30rBsovXmw_TimgA3Xhfcx_IsrcM1"
- "Pw30rBsovXmw_TimgA3Xhfcx_Iuec"
- "Pw30rBsovXmw_TimgA3Xhfcxn_Isrc"
- "Pw30rBsovXmw_Tm1aA3Xhfcx_Icir_Icir"
- "Pw30rBsovXmw_Tps0A3Xhf"
- "Pw30rBsovXmw_TpsmA3Xhf"
- "Pw30rBsovXmw_TpsrA3Xhf"
- "Pw30rBsovXmw_Ts1aA3Xhfcx_Ialp"
- "Pw30rBsovXmw_TsplA3Xhfcx_Isrc"
- "Pw30rBsovXmw_TsplA3Xhfcx_IsrcM1"
- "Pw30rBsovXmw_TstlA3Xhf"
- "Pw30rXm_A2S1Xhfcx"
- "Pw30rXm_A2Xhfcxs"
- "Pw30rXm_BdrkA2Xhfcxs"
- "Pw30rXm_TbdsA2Xhfcxes_Isup_Isrc"
- "Pw30rXm_Tc3bA2S1Xhfcx_Idst"
- "Pw30rXm_Tc4pA2S1Xhfcx_Idst"
- "Pw30rXm_TcimBdrkA2Xhfcx_Isup"
- "Pw30rXm_TcimBdsoA2Xhfcxs_Ialp"
- "Pw30rXm_TcmaA2S1LlnXhfcx"
- "Pw30rXm_TedrA2Xhfn"
- "Pw30rXm_TimgA2S1Xhfcx_IsrcM0"
- "Pw30rXm_TimgA2Xhfcx_IsrcM1"
- "Pw30rXm_TimgA2Xhfcxs_IsrcCcl"
- "Pw30rXm_TimgA2Xhfcxs_Ixrg"
- "Pw30rXm_TimgBdsoA2Xhfcxsn_Isrc"
- "Pw30rXm_TimgBvcmA2Xhfcxsn_Isrc"
- "Pw30rXmw_A3S1Xhfcx"
- "Pw30rXmw_A3S1Xhfcxn"
- "Pw30rXmw_A3Xhfcxn"
- "Pw30rXmw_TcmaA3S1LlnXhfcx"
- "Pw30rXmw_TcmaA3S1Xhfcxn"
- "Pw30rXmw_TimgA3S1Xhfcx_Icir"
- "Pw30rXmw_TimgA3S1Xhfcx_Isrc"
- "Pw30rXmw_TimgA3Xhfcx_Isxr"
- "Pw30rXmw_TimgA3Xhfcx_IxrgCcl"
- "Pw30rXmw_TirbA3Xhf_Isrc"
- "Pw30rXmw_TpblA3S1Xhf"
- "Pw30rXmw_Tpc0A3Xhf"
- "Pw30rXmw_Tpc1A3Xhf"
- "Pw30rXmw_TprcA3Xhf"
- "Pw40aBaddXmw_TimgA3Xhfcx_Ialp"
- "Pw40aBdinXmw_TimgA3Xhfcx_Isrc"
- "Pw40aBmaxXmw_TimgA3Xhfcx_Ialp"
- "Pw40aBmulXmw_A3Xhfcx"
- "Pw40aBmulXmw_TcmaA3S1LlnXhfcx"
- "Pw40aBmulXmw_TimgA3S1Xhfcx_Icir"
- "Pw40aBmulXmw_TimgA3Xhfcx_Isqr"
- "Pw40aBmulXmw_TimgA3Xhfcx_Isrc"
- "Pw40aBmulXmw_TimgA3Xhfcx_Iuec"
- "Pw40aBmulXmw_TirbA3Xhf_Isrc"
- "Pw40aBmulXmw_TpblA3S1Xhf"
- "Pw40aBmulXmw_TpblA3Xhf"
- "Pw40aBmulXmw_Tpc0A3Xhf"
- "Pw40aBmulXmw_Tpc1A3Xhf"
- "Pw40aBmulXmw_TprcA3Xhf"
- "Pw40aBsovXm_TcimA2S1Xhfcx_IalpCcl"
- "Pw40aBsovXm_TcimA2S1Xhfcx_Isup"
- "Pw40aBsovXm_TcmaA2S1LlnXhfcx"
- "Pw40aBsovXm_TimgA2S1Xhfcx_Iara"
- "Pw40aBsovXm_TimgA2S1Xhfcx_Isrc"
- "Pw40aBsovXm_TimgA2Xhfcxn_Isrc"
- "Pw40aBsovXm_TimgA2Xhfcxn_IsrcN3Oc3mtc4nlnlnl"
- "Pw40aBsovXm_Tm1aA2Xhfcx_Icir_Icir"
- "Pw40aBsovXm_TmuaA2Xhfcx_Isrc_Icir"
- "Pw40aBsovXm_TmuaA2Xhfcxp_IsrcN3Oc3mtc4nlnlnl_Icir"
- "Pw40aBsovXmw_A3Xhfcx"
- "Pw40aBsovXmw_A3Xhfcxn"
- "Pw40aBsovXmw_TcimA3Xhfcx_Ialp"
- "Pw40aBsovXmw_TcimA3Xhfcx_Icir"
- "Pw40aBsovXmw_TcimA3Xhfcx_Isrc"
- "Pw40aBsovXmw_TcmaA3LlnXhfcx"
- "Pw40aBsovXmw_TimgA3Xhfcx_Icir"
- "Pw40aBsovXmw_TimgA3Xhfcx_Isrc"
- "Pw40aBsovXmw_TimgA3Xhfcx_IsrcM1"
- "Pw40aBsovXmw_TirbA3Xhf_Isrc"
- "Pw40aBsovXmw_TpblA3Xhf"
- "Pw40aBsovXmw_Tpc0A3Xhf"
- "Pw40aBsovXmw_Tpc1A3Xhf"
- "Pw40aBsovXmw_TprcA3Xhf"
- "Pw40aBsovXmw_Tps0A3Xhf"
- "Pw40aBsovXmw_TpsmA3Xhf"
- "Pw40aBsovXmw_TsplA3Xhfcx_Isrc"
- "Pw40aXm_A2S1Xhfcx"
- "Pw40aXm_Tc3bA2Xhfcx_Idst"
- "Pw40aXm_TcmaA2S1LlnXhfcx"
- "Pw40aXm_TimgA2S1Xhfcx_IsrcM0"
- "Pw40aXm_TimgA2S1Xhfcxe_Isrc"
- "Pw40aXmw_A3S1Xhfcx"
- "Pw40aXmw_A3S1Xhfcxn"
- "Pw40aXmw_A3Xhfcxn"
- "Pw40aXmw_TbimBdinA3Xhfcx_Isrc_IsrcM1"
- "Pw40aXmw_TcimA3Xhfcx_Ialp"
- "Pw40aXmw_TcimA3Xhfcx_Icir"
- "Pw40aXmw_TcimA3Xhfcx_Irrg"
- "Pw40aXmw_TcmaA3LlnXhfcx"
- "Pw40aXmw_TcmaA3S1Xhfcxn"
- "Pw40aXmw_TimgA3S1Xhfcx_Icir"
- "Pw40aXmw_TimgA3Xhfcx_Ialp"
- "Pw40aXmw_TimgA3Xhfcx_Icir"
- "Pw40aXmw_TimgA3Xhfcx_Isar"
- "Pw40aXmw_TimgA3Xhfcx_Isrc"
- "Pw40aXmw_TimgA3Xhfcx_IsrcCcl"
- "Pw40aXmw_TimgA3Xhfcx_Isxr"
- "Pw40aXmw_TimgA3Xhfcx_Ixrg"
- "Pw40aXmw_TimgA3Xhfcx_IxrgCcl"
- "Pw40aXmw_TpblA3S1Xhf"
- "Pw40aXmw_TpblA3Xhf"
- "Pw40aXmw_Tpc0A3Xhf"
- "Pw40aXmw_Tpc1A3Xhf"
- "Pw40aXmw_TprcA3Xhf"
- "Pw40aXmw_Tps0A3Xhf"
- "Pw40aXmw_TpsmA3Xhf"
- "Pw40aXmw_TradA3Xhfn_Isrc"
- "Pw40aXmw_Ts1aA3Xhfcx_Ialp"
- "Pw40aXmw_Ts1aA3Xhfcx_Irrg"
- "Pw40aXmw_Ts1aA3Xhfcx_Isrc"
- "QUARTZCORE_LOG_FILE"
- "Ramp %d: Setting SDR brightness to %g nits, headroom to %g, limit to %g, contrast enhancer to %g, low_amb_str to %g, high_amb_str to %g indicator_nits to %g indicator_limit to %g"
- "Render pipeline warmup took %0.2fs, MTLPixelFormats: {%s, %s, %s, %s, %s, %s}\n"
- "RenderInterval"
- "Screen blanked"
- "Shape: %s"
- "Signpost ID is context_id. pid=%{public, name=pid}d frame_seed=%{public, name=frame_seed}#x earliest_mct=%{public, name=earliest_mct}llu previous_mct=%{public, name=previous_mct}llu process_name=%{public, name=process_name}s presentation_modifier_display_target_mct=%{public, name=presentation_modifier_display_target_mct}llu client_annotation=%{public, name=client_annotation}@ transaction_seed=%{public, name=transaction_seed}#x"
- "Signpost ID is context_id. pid=%{public, name=pid}d frame_seed=%{public, name=frame_seed}#x earliest_mct=%{public, name=earliest_mct}llu previous_mct=%{public, name=previous_mct}llu process_name=%{public, name=process_name}s presentation_modifier_display_target_mct=%{public, name=presentation_modifier_display_target_mct}llu transaction_seed=%{public, name=transaction_seed}#x"
- "SwapID"
- "T@\"<CALinearMaskLayerDelegate><CALayerDelegate>\",W,D"
- "Unable to get power assertions %x"
- "Unable to open log file for writing: %s\n%s\n"
- "Unable to query displays from server (%d)"
- "Unentitled call to server!"
- "Unknown status"
- "Unrelated"
- "Unsupported use of CADisplayLink SPI off the main thread."
- "Update is empty"
- "VRRDivisor"
- "VRRIdleEnabled"
- "VRRIsIdle"
- "VideoTonemapping"
- "WindowServer.Stalls"
- "X_LOG_FILE"
- "X_LOG_TRUNCATE"
- "[%d] Failed to create flattened OGL::Surface"
- "[%d] Failed to create flattened iosurface"
- "[%d] added surface <%d> <%d %d %d %d> to cache <size: %zu>"
- "[%d] cached flatten info [%s] [%d %d %d %d] [%x] [%d %d %d %d]"
- "[%d] cachedFlatten but no cached surface"
- "[%d] fetched flatten info [%s] [%d %d %d %d] [%llu] [%x] [%d %d %d %d]"
- "[%d] found cached dod <%d %d %d %d>"
- "[%d] found cached surface <%d> <%zu %zu>"
- "[%d] no cached dod"
- "[%d] no cached surface"
- "[%d] removed surface <%d> from cache <size: %zu>"
- "[%d] rendered & cached new surf <%d> <%d %d>"
- "[%d] replacing surface <%d> <%d %d %d %d> with surface <%d> <%d %d %d %d>"
- "[%d] reusing surface <%d>"
- "[%d] trying to flatten an empty surface!"
- "[%d] using cached surf <%d>"
- "[0x%x] FG attachment Found (size: %zu)"
- "^{CADisplayModeCriteriaPriv={CGSize=dd}di}"
- "^{CAWindowServerDisplayImpl={Mutex={_opaque_pthread_mutex_t=q[56c]}}^{Server}{CABrightnessTransaction=fffffffffff{?=[9f]}fBBI}@?@@@@BB}"
- "^{DisplayStateInfo=CCCC}"
- "^{DynamicFrameRateSource=I^v{CAFrameRateRange=fff}{CAFrameIntervalRange=III}QiQQ[4I]b1^{DynamicFrameRateSource}b1}"
- "^{_CAMetalDrawablePrivate={Atomic={?=i}}IIIQQQQd^{_CAMetalLayerPrivate}^{__IOSurface}@@^{CGColorSpace}@@Cb1b1b1b1b1b1b1}"
- "^{_CAMetalDrawablePrivate={Atomic={?=i}}IIIQQQQd^{_CAMetalLayerPrivate}^{__IOSurface}@@^{CGColorSpace}@@Cb1b1b1b1b1b1b1}16@0:8"
- "_completion"
- "_seed"
- "_target_state"
- "brightness_deadline"
- "chrysaor"
- "color-accuracy-index"
- "com.apple.coreanimation.od-texture-%zu"
- "continued...\n"
- "create_shared_event"
- "dat"
- "dataWithBytesNoCopy:length:"
- "dataWithContentsOfFile:options:error:"
- "didChangeToState:seed:result:"
- "display %d cloning failed due to protection mismatch"
- "display_overdrive_linearize"
- "display_overdrive_lut_gen"
- "display_overdrive_srgb_sampler"
- "drawInLinearMaskContext:"
- "draw_path_joins"
- "draw_path_lines"
- "edr_deadline"
- "encode_uniform_function_args"
- "exported [%d %d] buffer to %s\n"
- "failed trying to set maximumDrawableCount to %lu outside of the valid range of [2, 3]"
- "finishExternalUpdate:withFlags:"
- "fontSmoothingStyle"
- "function_uniform"
- "getBytes:range:"
- "get_texture_function () == OGL_TEX_PATH_STROKE_LINE"
- "get_texture_function () == OGL_TEX_PATH_STROKE_MITER_JOIN || get_texture_function () == OGL_TEX_PATH_STROKE_ROUND_JOIN"
- "harmony"
- "hrm"
- "inhibit-container"
- "kCGApplyFlexLumaScaling"
- "kCGFlexGTCTargetHeadroom"
- "kUpdateReasonDisplayBrightness %s"
- "motion-blur"
- "needs_brightness_update"
- "newComputePipelineStateWithFunction:error:"
- "next_frame"
- "odt_%d_%d"
- "ovr"
- "pathForResource:ofType:"
- "path_stroke_line_frag"
- "path_stroke_line_vert"
- "path_stroke_miter_join_frag"
- "path_stroke_miter_join_vert"
- "path_stroke_round_join_frag"
- "path_stroke_round_join_vert"
- "pipeline with function=%s\n%s"
- "pipeline=%s sdk=%s\n%s"
- "preferred_mode_with_criteria: resolution [%g x %g], target hdr (%s), user hdr (%s), rate (%g) --> %dx%d@%g %s"
- "present_surface: swap_end returned error 0x%x"
- "psl"
- "psm"
- "psr"
- "r+"
- "setFontSmoothingStyle:"
- "set_allows_edr"
- "set_blanking_removes_power=%u"
- "set_brightness_limit"
- "set_color_matrix"
- "set_edr_properties"
- "set_high_ambient_adaptation_strength"
- "set_low_ambient_adaptation_strength"
- "set_sdr_nits_1"
- "set_sdr_nits_2"
- "sl"
- "sm"
- "sr"
- "stderr"
- "stdout"
- "stopping display %d cloning due to protection mismatch"
- "total_elements <= kMaxFunctionUniformSize * 4"
- "type () != kFlipBookType_DirtyRegionOnly"
- "uintptr_t (dst) - uintptr_t (_encoded.frag_uniform) <= uniform_size"
- "unexpected error %i sending sync reply from %x"
- "update_metal_texture"
- "v->count () == 4"
- "v16@?0^{?=i(?={?=I}{?=CCCCC[3i]i[3i][8I]}{?=CCCCCC})}8"
- "v16@?0r^{?=IIQQQQIBBBfffQIB}8"
- "v20@?0i8r^{?=i(?={?=fffffff}{?=If^f}{?=I[10I][10f][10[11f]]}{?=If^ff^f}{?=ffI}{?=fffff}{?=I}{?=fffff}{?=ffff})}12"
- "v24@0:8^{CALinearMaskContext=}16"
- "v28@0:8I16r^{CA_content_stream_frame_info=QIIffffffC}20"
- "v92@?0I8I12Q16Q24Q32Q40I48B52B56B60f64f68f72Q76I84B88"
- "w+"
- "windowserver-surface.cpp"
- "{small_vector<ContentStreamClientFrame, 8UL>=\"_begin\"^{ContentStreamClientFrame}\"_end\"^{ContentStreamClientFrame}\"_fixedStorage\"^{ContentStreamClientFrame}\"_capacity\"Q\"\"(?=\"storage\"[8{type=\"__lx\"[16C]}]\"flat_storage\"[0{ContentStreamClientFrame=\"iosurface\"^{__IOSurface}\"id\"I\"port\"I}])}"
- "{unordered_map<unsigned int, unsigned int, std::hash<unsigned int>, std::equal_to<unsigned int>, std::allocator<std::pair<const unsigned int, unsigned int>>>=\"__table_\"{__hash_table<std::__hash_value_type<unsigned int, unsigned int>, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::hash<unsigned int>, std::equal_to<unsigned int>>, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::equal_to<unsigned int>, std::hash<unsigned int>>, std::allocator<std::__hash_value_type<unsigned int, unsigned int>>>=\"__bucket_list_\"{unique_ptr<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>>=\"__ptr_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> **, std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>>=\"__value_\"^^v\"__value_\"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>=\"__data_\"{__compressed_pair<unsigned long, std::allocator<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *> *>>=\"__value_\"Q}}}}\"__p1_\"{__compressed_pair<std::__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *>, std::allocator<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *>>>=\"__value_\"{__hash_node_base<std::__hash_node<std::__hash_value_type<unsigned int, unsigned int>, void *> *>=\"__next_\"^v}}\"__p2_\"{__compressed_pair<unsigned long, std::__unordered_map_hasher<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::hash<unsigned int>, std::equal_to<unsigned int>>>=\"__value_\"Q}\"__p3_\"{__compressed_pair<float, std::__unordered_map_equal<unsigned int, std::__hash_value_type<unsigned int, unsigned int>, std::equal_to<unsigned int>, std::hash<unsigned int>>>=\"__value_\"f}}}"

```
