## PersonaUI

> `/System/Library/PrivateFrameworks/PersonaUI.framework/PersonaUI`

```diff

-1366.200.2.0.0
-  __TEXT.__text: 0x7edc
-  __TEXT.__auth_stubs: 0x750
+1366.500.41.0.0
+  __TEXT.__text: 0x85bc
+  __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_methlist: 0xb64
   __TEXT.__const: 0x348
   __TEXT.__cstring: 0x76a
   __TEXT.__oslogstring: 0x1ff
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__unwind_info: 0x2d0
   __TEXT.__objc_classname: 0xe4
   __TEXT.__objc_methname: 0x1e8d
   __TEXT.__objc_methtype: 0x696

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x9c8
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__auth_got: 0x390
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x7a0
   __AUTH_CONST.__objc_const: 0x1130

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8913B8C-5991-3AE0-B0E9-6DBE8026246D
+  UUID: AE974C85-7563-3C87-891D-96F1EDFCCE03
   Functions: 222
-  Symbols:   1008
+  Symbols:   1003
   CStrings:  632
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x25
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ __InvalidPRLikenessCacheSize : 128 -> 140
~ -[PRImageView setImage:] : 124 -> 128
~ -[PRImageView drawRect:] : 140 -> 148
~ -[PRMonogram initWithText:fontIndex:monogramColor:] : 164 -> 156
~ -[PRMonogram setText:] : 180 -> 192
~ -[PRMonogram color] : 60 -> 80
~ -[PRMonogram plateGradientStartColor] : 136 -> 152
~ -[PRMonogram plateGradientEndColor] : 136 -> 152
~ -[PRMonogram plateSelectedActiveColor] : 136 -> 152
~ -[PRMonogram plateSelectedInactiveColor] : 136 -> 152
~ -[PRMonogram plateSelectedActiveTextColor] : 136 -> 152
~ -[PRMonogram setFontIndex:] : 104 -> 108
~ -[PRMonogram stringAttributesForDiameter:] : 408 -> 424
~ -[PRMonogram snapshotWithSize:scale:options:] : 644 -> 660
~ -[PRMonogram _renderTextInContext:frame:] : 452 -> 456
~ -[PRMonogram description] : 232 -> 256
~ +[PRMonogram _fontSpecs] : 68 -> 84
~ ___24+[PRMonogram _fontSpecs]_block_invoke : 560 -> 600
~ +[PRMonogram countOfFonts] : 56 -> 60
~ +[PRMonogram fontForIndex:plateDiameter:] : 256 -> 280
~ +[PRMonogram kerningForFontIndex:fontSize:] : 108 -> 116
~ +[PRMonogram updatePlateOverlayLayer:] : 248 -> 260
~ -[PRMonogram setColor:] : 12 -> 64
~ -[PRMonogram setMonogramColor:] : 12 -> 64
~ -[PRMonogram(DataRepresentation) dataRepresentationWithVersion:] : 464 -> 488
~ -[PRMonogram(DataRepresentation) _takeValuesFromDataRepresentation:] : 896 -> 920
~ -[NSArray(PersonaUI) pr_objectPassingTest:] : 88 -> 92
~ +[UIColor(PersonaUI) pr_colorNamed:] : 136 -> 144
~ +[PRLikenessCache sharedInstance] : 160 -> 176
~ +[PRLikenessCache _applicationCacheDirectory] : 160 -> 180
~ +[PRLikenessCache _staticRepresentationCacheURL] : 140 -> 152
~ +[PRLikenessCache _ensureExistenceOfDirectory:] : 308 -> 312
~ -[PRLikenessCache init] : 368 -> 380
~ -[PRLikenessCache _cacheKeyForLikeness:context:] : 252 -> 272
~ -[PRLikenessCache _cacheURLForLikeness:context:] : 148 -> 160
~ -[PRLikenessCache imageForLikeness:context:completion:] : 412 -> 408
~ ___55-[PRLikenessCache imageForLikeness:context:completion:]_block_invoke_2 : 204 -> 200
~ ___55-[PRLikenessCache imageForLikeness:context:completion:]_block_invoke_3 : 280 -> 284
~ ___55-[PRLikenessCache imageForLikeness:context:completion:]_block_invoke_5 : 236 -> 228
~ -[PRLikenessCache _fetchFromMemory:context:renderBlock:completion:] : 396 -> 384
~ ___67-[PRLikenessCache _fetchFromMemory:context:renderBlock:completion:]_block_invoke_2 : 104 -> 108
~ -[PRLikenessCache _fetchFromFilesystem:context:renderBlock:completion:] : 372 -> 364
~ -[PRLikenessCache _renderImageForLikeness:context:completion:] : 536 -> 552
~ +[PRLikenessCache _imageAtURL:] : 348 -> 352
~ +[PRLikenessCache _writeImage:toURL:] : 496 -> 508
~ +[PRLikenessCache _removeImageAtURL:] : 300 -> 304
~ +[PRLikenessCache _purgeOldCacheFilesInDirectory:] : 892 -> 908
~ +[PRLikenessCache _propertyValueForURL:forKey:] : 276 -> 272
~ -[PRLikenessCache setCacheDirectory:] : 12 -> 64
~ -[PRLikeness(PersonaUI) accentColor] : 104 -> 112
~ -[PRLikeness(PersonaUI) _accentColorForMonogram] : 144 -> 160
~ -[PRLikeness(PersonaUI) _accentColorForPhoto] : 440 -> 444
~ -[PRLikeness(PersonaUI) snapshotWithSize:scale:options:] : 252 -> 268
~ -[PRLikeness(PersonaUI) _photoSnapshotWithSize:scale:options:] : 424 -> 440
~ +[UIImage(PRLikenessView) pr_imageWithCGImage:cropRect:] : 104 -> 108
~ -[UIImage(PRLikenessView) pr_circleImageOfDiameter:cropRect:] : 156 -> 160
~ +[PRMonogramColor gradientStartColor:] : 164 -> 168
~ +[PRMonogramColor generateMonogramGradientColorsByNameDictionary] : 3392 -> 3668
~ +[PRMonogramColor monogramGradientColorNamed:] : 200 -> 204
~ ___46+[PRMonogramColor monogramGradientColorNamed:]_block_invoke : 60 -> 64
~ +[PRMonogramColor colorWithName:inBundle:] : 144 -> 156
~ +[PRMonogramColor defaultGradientStartColor] : 96 -> 104
~ +[PRMonogramColor defaultGradientEndColor] : 96 -> 104
~ +[PRMonogramColor defaultSelectedActiveColor] : 96 -> 104
~ +[PRMonogramColor defaultSelectedInactiveColor] : 96 -> 104
~ +[PRMonogramColor defaultSelectedActiveTextColor] : 96 -> 104
~ +[PRMonogramColor availableColorNames] : 284 -> 288
~ +[PRMonogramColor availableColors] : 92 -> 100
~ -[PRMonogramColor initWithRandomColor] : 116 -> 124
~ -[PRMonogramColor initWithColorName:] : 100 -> 104
~ -[PRMonogramColor setColorName:] : 192 -> 200
~ -[PRMonogramColor gradientStartColor] : 176 -> 196
~ -[PRMonogramColor gradientEndColor] : 176 -> 196
~ -[PRMonogramColor isEqual:] : 164 -> 160
~ -[PRMonogramColor hash] : 56 -> 60
~ -[PRMonogramColor copyWithZone:] : 4 -> 40
~ -[PRMonogramColor setColor:] : 12 -> 64
~ -[PRMonogramColor setGradientStartColor:] : 12 -> 64
~ -[PRMonogramColor setGradientEndColor:] : 12 -> 64
~ -[PRMonogramColor setSelectedActiveColor:] : 12 -> 64
~ -[PRMonogramColor setSelectedInactiveColor:] : 12 -> 64
~ -[PRMonogramColor setSelectedActiveTextColor:] : 12 -> 64
~ -[PRMonogramColor setBundle:] : 12 -> 64
~ +[NSBundle(PersonaUI) pr_personaUIBundle] : 68 -> 84
~ ___41+[NSBundle(PersonaUI) pr_personaUIBundle]_block_invoke : 92 -> 96
~ -[PRLikenessView _updateViewForLikeness:] : 472 -> 496
~ -[PRLikenessView _shouldRenderStaticRepresentation] : 216 -> 240
~ -[PRLikenessView _monogramView] : 156 -> 164
~ -[PRLikenessView _imageView] : 168 -> 176
~ -[PRLikenessView _imageForLikeness:completion:] : 404 -> 416
~ ___47-[PRLikenessView _imageForLikeness:completion:]_block_invoke : 276 -> 272
~ -[PRLikenessView setLikeness:] : 276 -> 296
~ -[PRLikenessView _isLikenessEqual:] : 248 -> 252
~ -[PRLikenessView _setDisplayedView:] : 180 -> 184
~ -[PRMonogramView initWithFrame:] : 388 -> 400
~ -[PRMonogramView setMonogram:] : 272 -> 284
~ -[PRMonogramView _updateTextLabel] : 916 -> 968
~ -[PRMonogramView layoutSubviews] : 204 -> 208
~ -[PRMonogramView textFieldDidBeginEditing:] : 148 -> 164
~ -[PRMonogramView textFieldDidEndEditing:] : 176 -> 196
~ -[PRMonogramView textField:shouldChangeCharactersInRange:replacementString:] : 472 -> 480
~ -[PRMonogramView didMoveToWindow] : 140 -> 148

```
