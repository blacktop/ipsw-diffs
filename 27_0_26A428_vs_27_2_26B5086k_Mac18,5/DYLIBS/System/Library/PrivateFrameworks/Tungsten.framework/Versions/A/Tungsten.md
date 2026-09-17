## Tungsten

> `/System/Library/PrivateFrameworks/Tungsten.framework/Versions/A/Tungsten`

```diff

-911.0.134.0.0
-  __TEXT.__text: 0x102fa0
-  __TEXT.__objc_methlist: 0x11b8c
+916.41.100.0.0
+  __TEXT.__text: 0x104e20
+  __TEXT.__objc_methlist: 0x11dec
   __TEXT.__const: 0x39f0
   __TEXT.__constg_swiftt: 0x244
   __TEXT.__swift5_typeref: 0x125e

   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_fieldmd: 0x7c8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__cstring: 0xd6fb
-  __TEXT.__gcc_except_tab: 0x3528
-  __TEXT.__oslogstring: 0x2225
+  __TEXT.__cstring: 0xd714
+  __TEXT.__gcc_except_tab: 0x357c
+  __TEXT.__oslogstring: 0x225a
   __TEXT.__ustring: 0x94
-  __TEXT.__unwind_info: 0x5738
+  __TEXT.__unwind_info: 0x57e0
   __TEXT.__eh_frame: 0x304
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1040
-  __DATA_CONST.__objc_classlist: 0x810
+  __DATA_CONST.__const: 0x1080
+  __DATA_CONST.__objc_classlist: 0x818
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x2c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x80e0
+  __DATA_CONST.__objc_selrefs: 0x8258
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x6c0
+  __DATA_CONST.__objc_superrefs: 0x6c8
   __DATA_CONST.__objc_arraydata: 0xb48
-  __DATA_CONST.__got: 0xe78
+  __DATA_CONST.__got: 0xeb0
   __AUTH_CONST.__const: 0x59b8
   __AUTH_CONST.__cfstring: 0x7de0
-  __AUTH_CONST.__objc_const: 0x22848
+  __AUTH_CONST.__objc_const: 0x22cc0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x2010
   __AUTH_CONST.__auth_got: 0x1130
-  __AUTH.__objc_data: 0x2de8
-  __DATA.__objc_ivar: 0x1a14
+  __AUTH.__objc_data: 0x2e38
+  __DATA.__objc_ivar: 0x1a6c
   __DATA.__data: 0x2670
   __DATA.__common: 0xc
   __DATA_DIRTY.__objc_data: 0x2288

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6901
-  Symbols:   15112
-  CStrings:  1884
+  Functions: 6960
+  Symbols:   15245
+  CStrings:  1885
 
Symbols:
+ +[PXGDisplayAssetPlaceholderConfiguration configurationWithPlaceholderStyle:]
+ -[PXGDecoratingLayout _effectiveActiveDecorationIndexes]
+ -[PXGDecoratingLayout _setEffectiveActiveDecorationIndexes:]
+ -[PXGDecoratingLayout focusRingThickness]
+ -[PXGDecoratingLayout removeActiveDecorations:]
+ -[PXGDecorationDefaultBadgeDrawingHelper checkmarkBackgroundColor]
+ -[PXGDecorationDefaultBadgeDrawingHelper checkmarkForegroundColor]
+ -[PXGDecorationDefaultBadgeDrawingHelper dealloc]
+ -[PXGDecorationDefaultBadgeDrawingHelper focusRingColor]
+ -[PXGDecorationDefaultBadgeDrawingHelper focusRingThickness]
+ -[PXGDecorationDefaultBadgeDrawingHelper setCheckmarkBackgroundColor:]
+ -[PXGDecorationDefaultBadgeDrawingHelper setCheckmarkForegroundColor:]
+ -[PXGDecorationDefaultBadgeDrawingHelper setFocusRingColor:]
+ -[PXGDecorationDefaultBadgeDrawingHelper setFocusRingThickness:]
+ -[PXGDisplayAssetPlaceholderConfiguration .cxx_destruct]
+ -[PXGDisplayAssetPlaceholderConfiguration _newSymbolImageWithUserInterfaceStyle:scale:outSizePoints:]
+ -[PXGDisplayAssetPlaceholderConfiguration _resolvedColor:forUserInterfaceStyle:]
+ -[PXGDisplayAssetPlaceholderConfiguration backgroundColor]
+ -[PXGDisplayAssetPlaceholderConfiguration copyWithZone:]
+ -[PXGDisplayAssetPlaceholderConfiguration createPlaceholderImageForUserInterfaceStyle:scale:ignoringSymbol:]
+ -[PXGDisplayAssetPlaceholderConfiguration initWithBackgroundColor:]
+ -[PXGDisplayAssetPlaceholderConfiguration initWithBackgroundColor:systemImageName:symbolConfiguration:]
+ -[PXGDisplayAssetPlaceholderConfiguration initWithBackgroundColor:systemImageName:symbolConfiguration:minimumSideLength:]
+ -[PXGDisplayAssetPlaceholderConfiguration minimumSideLength]
+ -[PXGDisplayAssetPlaceholderConfiguration resolvedDarkColor]
+ -[PXGDisplayAssetPlaceholderConfiguration resolvedLightColor]
+ -[PXGDisplayAssetPlaceholderConfiguration symbolConfiguration]
+ -[PXGDisplayAssetPlaceholderConfiguration systemImageName]
+ -[PXGDisplayAssetTextureProvider _setNoThumbnailPlaceholderMinPixelSideLength:]
+ -[PXGDisplayAssetTextureProvider _updateNoThumbnailPlaceholderImages]
+ -[PXGDisplayAssetTextureProvider noThumbnailPlaceholderConfiguration]
+ -[PXGDisplayAssetTextureProvider noThumbnailPlaceholderImageDarkSmall]
+ -[PXGDisplayAssetTextureProvider noThumbnailPlaceholderImageLightSmall]
+ -[PXGDisplayAssetTextureProvider setNoThumbnailPlaceholderConfiguration:]
+ -[PXGDisplayAssetTextureProvider setNoThumbnailPlaceholderImageDarkSmall:]
+ -[PXGDisplayAssetTextureProvider setNoThumbnailPlaceholderImageLightSmall:]
+ -[PXGDisplayAssetTextureProvider smallPlaceholderImage]
+ -[PXGView _updateProviderPlaceholderConfiguration]
+ -[PXGView noThumbnailPlaceholderConfiguration]
+ -[PXGView setCustomAssetImageViewsNeedReconfiguration]
+ -[PXGView setNoThumbnailPlaceholderConfiguration:]
+ -[PXGViewEnvironment displayScale]
+ -[PXGViewGestureController _handleDoubleClickAtLocation:]
+ -[PXGViewGestureController _isTouchDoubleTapAtLocation:indexPath:]
+ -[PXGViewGestureController _mouseDoubleClickRecognized:]
+ -[PXGViewGestureController _resetTouchDoubleTapState]
+ -[PXGViewGestureController _updateTouchDoubleTapStateForClickAtLocation:]
+ -[PXGViewRenderer _retireViewInfoForSpriteIndex:]
+ -[PXGViewRenderer setCustomAssetImageViewsNeedReconfiguration]
+ GCC_except_table1318
+ GCC_except_table1333
+ GCC_except_table1357
+ GCC_except_table1383
+ GCC_except_table1413
+ GCC_except_table1452
+ GCC_except_table1536
+ GCC_except_table1570
+ GCC_except_table1573
+ GCC_except_table1581
+ GCC_except_table1608
+ GCC_except_table1763
+ GCC_except_table1901
+ GCC_except_table1912
+ GCC_except_table1920
+ GCC_except_table1924
+ GCC_except_table1929
+ GCC_except_table1936
+ GCC_except_table1980
+ GCC_except_table2007
+ GCC_except_table2153
+ GCC_except_table2223
+ GCC_except_table2229
+ GCC_except_table2246
+ GCC_except_table2298
+ GCC_except_table2300
+ GCC_except_table2320
+ GCC_except_table2458
+ GCC_except_table2477
+ GCC_except_table2491
+ GCC_except_table2496
+ GCC_except_table2514
+ GCC_except_table2748
+ GCC_except_table2750
+ GCC_except_table2754
+ GCC_except_table2794
+ GCC_except_table2797
+ GCC_except_table2803
+ GCC_except_table2805
+ GCC_except_table2848
+ GCC_except_table2858
+ GCC_except_table2860
+ GCC_except_table2879
+ GCC_except_table2922
+ GCC_except_table2946
+ GCC_except_table3000
+ GCC_except_table3014
+ GCC_except_table3100
+ GCC_except_table3411
+ GCC_except_table3416
+ GCC_except_table3632
+ GCC_except_table3636
+ GCC_except_table3658
+ GCC_except_table3671
+ GCC_except_table3691
+ GCC_except_table3745
+ GCC_except_table3749
+ GCC_except_table3771
+ GCC_except_table3816
+ GCC_except_table3918
+ GCC_except_table3928
+ GCC_except_table3954
+ GCC_except_table4057
+ GCC_except_table4061
+ GCC_except_table4089
+ GCC_except_table4096
+ GCC_except_table4217
+ GCC_except_table4372
+ GCC_except_table4374
+ GCC_except_table4395
+ GCC_except_table4403
+ GCC_except_table4408
+ GCC_except_table4412
+ GCC_except_table4416
+ GCC_except_table4449
+ GCC_except_table4452
+ GCC_except_table4457
+ GCC_except_table4460
+ GCC_except_table4479
+ GCC_except_table4521
+ GCC_except_table4533
+ GCC_except_table4612
+ GCC_except_table4648
+ GCC_except_table4650
+ GCC_except_table4724
+ GCC_except_table4815
+ GCC_except_table4941
+ GCC_except_table4995
+ GCC_except_table4997
+ GCC_except_table4999
+ GCC_except_table5003
+ GCC_except_table5005
+ GCC_except_table5128
+ GCC_except_table5143
+ GCC_except_table5159
+ GCC_except_table5161
+ GCC_except_table5165
+ GCC_except_table5303
+ GCC_except_table5418
+ GCC_except_table5498
+ GCC_except_table5499
+ GCC_except_table5533
+ GCC_except_table5759
+ GCC_except_table5767
+ GCC_except_table5775
+ GCC_except_table5783
+ GCC_except_table5784
+ GCC_except_table5786
+ GCC_except_table5787
+ GCC_except_table5788
+ GCC_except_table5793
+ GCC_except_table5794
+ GCC_except_table5797
+ GCC_except_table5798
+ GCC_except_table5807
+ GCC_except_table5817
+ GCC_except_table5818
+ GCC_except_table5819
+ GCC_except_table5820
+ GCC_except_table5822
+ GCC_except_table5823
+ GCC_except_table5825
+ GCC_except_table5830
+ GCC_except_table5831
+ GCC_except_table5832
+ GCC_except_table5836
+ GCC_except_table5845
+ GCC_except_table5846
+ GCC_except_table5849
+ GCC_except_table5853
+ GCC_except_table5854
+ GCC_except_table5855
+ GCC_except_table5858
+ GCC_except_table5878
+ GCC_except_table5880
+ GCC_except_table5881
+ GCC_except_table5882
+ GCC_except_table5883
+ GCC_except_table5887
+ GCC_except_table5889
+ GCC_except_table5892
+ GCC_except_table5893
+ GCC_except_table5901
+ GCC_except_table5904
+ GCC_except_table5906
+ GCC_except_table5913
+ GCC_except_table5914
+ GCC_except_table5915
+ GCC_except_table5916
+ GCC_except_table5917
+ GCC_except_table5918
+ GCC_except_table5919
+ GCC_except_table5922
+ GCC_except_table5923
+ GCC_except_table5924
+ GCC_except_table5925
+ GCC_except_table5926
+ GCC_except_table5928
+ GCC_except_table5989
+ GCC_except_table6004
+ OBJC_IVAR_$_PXGDecoratingLayout._focusRingThickness
+ OBJC_IVAR_$_PXGDecorationDefaultBadgeDrawingHelper._checkmarkBackgroundColor
+ OBJC_IVAR_$_PXGDecorationDefaultBadgeDrawingHelper._checkmarkForegroundColor
+ OBJC_IVAR_$_PXGDecorationDefaultBadgeDrawingHelper._focusRingColor
+ OBJC_IVAR_$_PXGDecorationDefaultBadgeDrawingHelper._focusRingThickness
+ OBJC_IVAR_$_PXGDisplayAssetPlaceholderConfiguration._backgroundColor
+ OBJC_IVAR_$_PXGDisplayAssetPlaceholderConfiguration._minimumSideLength
+ OBJC_IVAR_$_PXGDisplayAssetPlaceholderConfiguration._resolvedDarkColor
+ OBJC_IVAR_$_PXGDisplayAssetPlaceholderConfiguration._resolvedLightColor
+ OBJC_IVAR_$_PXGDisplayAssetPlaceholderConfiguration._symbolConfiguration
+ OBJC_IVAR_$_PXGDisplayAssetPlaceholderConfiguration._systemImageName
+ OBJC_IVAR_$_PXGDisplayAssetTextureProvider._noThumbnailPlaceholderConfiguration
+ OBJC_IVAR_$_PXGDisplayAssetTextureProvider._noThumbnailPlaceholderImageDarkSmall
+ OBJC_IVAR_$_PXGDisplayAssetTextureProvider._noThumbnailPlaceholderImageLightSmall
+ OBJC_IVAR_$_PXGDisplayAssetTextureProvider._noThumbnailPlaceholderImageLock
+ OBJC_IVAR_$_PXGDisplayAssetTextureProvider._noThumbnailPlaceholderMinPixelSideLength
+ OBJC_IVAR_$_PXGMetalRenderer._clampToEdgeSampler
+ OBJC_IVAR_$_PXGView._noThumbnailPlaceholderConfiguration
+ OBJC_IVAR_$_PXGViewEnvironment._displayScale
+ OBJC_IVAR_$_PXGViewGestureController._lastTouchClickIndexPath
+ OBJC_IVAR_$_PXGViewGestureController._lastTouchClickLocationInWindow
+ OBJC_IVAR_$_PXGViewGestureController._lastTouchClickTime
+ OBJC_IVAR_$_PXGViewGestureController._mouseDoubleClickRecognizer
+ OBJC_IVAR_$_PXGViewRenderer._spritesNeedUpdate
+ _NSAppearanceNameAqua
+ _NSAppearanceNameDarkAqua
+ _NSDeviceRGBColorSpace
+ _NSZeroPoint
+ _OBJC_CLASS_$_NSAppearance
+ _OBJC_CLASS_$_NSBitmapImageRep
+ _OBJC_CLASS_$_PXGDisplayAssetPlaceholderConfiguration
+ _OBJC_METACLASS_$_PXGDisplayAssetPlaceholderConfiguration
+ __OBJC_$_CLASS_METHODS_PXGDisplayAssetPlaceholderConfiguration
+ __OBJC_$_INSTANCE_METHODS_PXGDisplayAssetPlaceholderConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_PXGDisplayAssetPlaceholderConfiguration
+ __OBJC_$_PROP_LIST_PXGDisplayAssetPlaceholderConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_PXGDisplayAssetPlaceholderConfiguration
+ __OBJC_CLASS_RO_$_PXGDisplayAssetPlaceholderConfiguration
+ __OBJC_METACLASS_RO_$_PXGDisplayAssetPlaceholderConfiguration
+ ___101-[PXGDisplayAssetPlaceholderConfiguration _newSymbolImageWithUserInterfaceStyle:scale:outSizePoints:]_block_invoke
+ ___108-[PXGDisplayAssetPlaceholderConfiguration createPlaceholderImageForUserInterfaceStyle:scale:ignoringSymbol:]_block_invoke
+ ___108-[PXGDisplayAssetPlaceholderConfiguration createPlaceholderImageForUserInterfaceStyle:scale:ignoringSymbol:]_block_invoke_2
+ ___80-[PXGDisplayAssetPlaceholderConfiguration _resolvedColor:forUserInterfaceStyle:]_block_invoke
+ ___block_descriptor_40_e54_v48?0{CGRect={CGPoint=dd}{CGSize=dd}}8^{CGContext=}40l
+ ___block_descriptor_80_e54_v48?0{CGRect={CGPoint=dd}{CGSize=dd}}8^{CGContext=}40l
+ _objc_msgSend$CGImage
+ _objc_msgSend$_effectiveActiveDecorationIndexes
+ _objc_msgSend$_handleDoubleClickAtLocation:
+ _objc_msgSend$_isTouchDoubleTapAtLocation:indexPath:
+ _objc_msgSend$_newSymbolImageWithUserInterfaceStyle:scale:outSizePoints:
+ _objc_msgSend$_resetTouchDoubleTapState
+ _objc_msgSend$_resolvedColor:forUserInterfaceStyle:
+ _objc_msgSend$_retireViewInfoForSpriteIndex:
+ _objc_msgSend$_setEffectiveActiveDecorationIndexes:
+ _objc_msgSend$_setNoThumbnailPlaceholderMinPixelSideLength:
+ _objc_msgSend$_updateNoThumbnailPlaceholderImages
+ _objc_msgSend$_updateProviderPlaceholderConfiguration
+ _objc_msgSend$_updateTouchDoubleTapStateForClickAtLocation:
+ _objc_msgSend$appearanceNamed:
+ _objc_msgSend$checkmarkBackgroundColor
+ _objc_msgSend$checkmarkForegroundColor
+ _objc_msgSend$colorWithCGColor:
+ _objc_msgSend$colorWithSRGBRed:green:blue:alpha:
+ _objc_msgSend$configurationWithPlaceholderStyle:
+ _objc_msgSend$controlAccentColor
+ _objc_msgSend$createPlaceholderImageForUserInterfaceStyle:scale:ignoringSymbol:
+ _objc_msgSend$drawInRect:
+ _objc_msgSend$focusRingThickness
+ _objc_msgSend$focusRingThicknessInLayout:
+ _objc_msgSend$graphicsContextWithBitmapImageRep:
+ _objc_msgSend$initWithBackgroundColor:
+ _objc_msgSend$initWithBackgroundColor:systemImageName:symbolConfiguration:
+ _objc_msgSend$initWithBackgroundColor:systemImageName:symbolConfiguration:minimumSideLength:
+ _objc_msgSend$initWithBitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:
+ _objc_msgSend$minimumSideLength
+ _objc_msgSend$px_checkmarkImageWithBackgroundColor:foregroundColor:checked:
+ _objc_msgSend$removeActiveDecorations:
+ _objc_msgSend$resolvedDarkColor
+ _objc_msgSend$resolvedLightColor
+ _objc_msgSend$setCustomAssetImageViewsNeedReconfiguration
+ _objc_msgSend$setNoThumbnailPlaceholderConfiguration:
+ _objc_msgSend$setNoThumbnailPlaceholderImageDarkSmall:
+ _objc_msgSend$setNoThumbnailPlaceholderImageLightSmall:
+ _objc_msgSend$smallPlaceholderImage
+ _objc_msgSend$symbolConfiguration
+ _objc_msgSend$systemImageName
- -[PXGViewGestureController _doubleClickRecognized:]
- GCC_except_table1306
- GCC_except_table1321
- GCC_except_table1345
- GCC_except_table1371
- GCC_except_table1400
- GCC_except_table1434
- GCC_except_table1518
- GCC_except_table1552
- GCC_except_table1555
- GCC_except_table1563
- GCC_except_table1590
- GCC_except_table1745
- GCC_except_table1883
- GCC_except_table1894
- GCC_except_table1902
- GCC_except_table1906
- GCC_except_table1911
- GCC_except_table1918
- GCC_except_table1962
- GCC_except_table1971
- GCC_except_table2117
- GCC_except_table2205
- GCC_except_table2211
- GCC_except_table2228
- GCC_except_table2281
- GCC_except_table2419
- GCC_except_table2438
- GCC_except_table2452
- GCC_except_table2457
- GCC_except_table2475
- GCC_except_table2709
- GCC_except_table2711
- GCC_except_table2715
- GCC_except_table2755
- GCC_except_table2758
- GCC_except_table2764
- GCC_except_table2766
- GCC_except_table2770
- GCC_except_table2819
- GCC_except_table2821
- GCC_except_table2840
- GCC_except_table2882
- GCC_except_table2906
- GCC_except_table2960
- GCC_except_table2974
- GCC_except_table3056
- GCC_except_table3367
- GCC_except_table3372
- GCC_except_table3584
- GCC_except_table3588
- GCC_except_table3610
- GCC_except_table3623
- GCC_except_table3643
- GCC_except_table3697
- GCC_except_table3701
- GCC_except_table3723
- GCC_except_table3768
- GCC_except_table3870
- GCC_except_table3880
- GCC_except_table3906
- GCC_except_table4009
- GCC_except_table4013
- GCC_except_table4041
- GCC_except_table4048
- GCC_except_table4168
- GCC_except_table4322
- GCC_except_table4324
- GCC_except_table4345
- GCC_except_table4353
- GCC_except_table4358
- GCC_except_table4360
- GCC_except_table4362
- GCC_except_table4366
- GCC_except_table4399
- GCC_except_table4402
- GCC_except_table4407
- GCC_except_table4429
- GCC_except_table4471
- GCC_except_table4483
- GCC_except_table4562
- GCC_except_table4598
- GCC_except_table4600
- GCC_except_table4674
- GCC_except_table4765
- GCC_except_table4891
- GCC_except_table4945
- GCC_except_table4947
- GCC_except_table4949
- GCC_except_table4953
- GCC_except_table4955
- GCC_except_table5078
- GCC_except_table5093
- GCC_except_table5109
- GCC_except_table5111
- GCC_except_table5115
- GCC_except_table5252
- GCC_except_table5314
- GCC_except_table5444
- GCC_except_table5445
- GCC_except_table5479
- GCC_except_table5705
- GCC_except_table5706
- GCC_except_table5710
- GCC_except_table5712
- GCC_except_table5713
- GCC_except_table5714
- GCC_except_table5716
- GCC_except_table5717
- GCC_except_table5719
- GCC_except_table5720
- GCC_except_table5721
- GCC_except_table5722
- GCC_except_table5727
- GCC_except_table5728
- GCC_except_table5729
- GCC_except_table5730
- GCC_except_table5732
- GCC_except_table5733
- GCC_except_table5734
- GCC_except_table5737
- GCC_except_table5738
- GCC_except_table5739
- GCC_except_table5740
- GCC_except_table5741
- GCC_except_table5742
- GCC_except_table5743
- GCC_except_table5744
- GCC_except_table5745
- GCC_except_table5746
- GCC_except_table5747
- GCC_except_table5751
- GCC_except_table5753
- GCC_except_table5755
- GCC_except_table5761
- GCC_except_table5763
- GCC_except_table5765
- GCC_except_table5769
- GCC_except_table5777
- GCC_except_table5778
- GCC_except_table5779
- GCC_except_table5804
- GCC_except_table5808
- GCC_except_table5811
- GCC_except_table5826
- GCC_except_table5829
- GCC_except_table5838
- GCC_except_table5839
- GCC_except_table5847
- GCC_except_table5852
- GCC_except_table5860
- GCC_except_table5861
- GCC_except_table5864
- GCC_except_table5870
- GCC_except_table5871
- GCC_except_table5872
- GCC_except_table5874
- GCC_except_table5935
- GCC_except_table5950
- OBJC_IVAR_$_PXGViewGestureController._doubleClickRecognizer
- OBJC_IVAR_$_PXGViewRenderer._spritesNeedUpate
- _objc_msgSend$doubleClickInterval
CStrings:
+ "-[PXGDecoratingLayout _setEffectiveActiveDecorationIndexes:]"
+ "Failed to create placeholder image glyph for name %@"
+ "PhotosUICore.mouseDoubleClickRecognizer"
+ "\xa1a\x81"
+ "\xf0\xf0aQ"
- "-[PXGDecoratingLayout setActiveDecorations:]"
- "PhotosUICore.doubleClickRecognizer"
- "\xa1Q\x81"
- "\xf0\xf0QQ"
```
