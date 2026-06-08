## PersonaUI

> `/System/Library/PrivateFrameworks/PersonaUI.framework/PersonaUI`

```diff

-1366.500.41.0.0
-  __TEXT.__text: 0x85bc
-  __TEXT.__auth_stubs: 0x700
+1372.100.2.0.0
+  __TEXT.__text: 0x7ef0
   __TEXT.__objc_methlist: 0xb64
   __TEXT.__const: 0x348
-  __TEXT.__cstring: 0x76a
+  __TEXT.__cstring: 0x77a
   __TEXT.__oslogstring: 0x1ff
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x2d0
-  __TEXT.__objc_classname: 0xe4
-  __TEXT.__objc_methname: 0x1e8d
-  __TEXT.__objc_methtype: 0x696
-  __TEXT.__objc_stubs: 0x1c80
-  __DATA_CONST.__got: 0x1a0
+  __TEXT.__unwind_info: 0x2c8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2c0
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x9c8
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x390
+  __DATA_CONST.__got: 0x1a0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x7a0
   __AUTH_CONST.__objc_const: 0x1130
   __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x3b8
   __DATA.__objc_ivar: 0xb4
   __DATA.__data: 0x128
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x2d0
-  __DATA_DIRTY.__bss: 0x10
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F2338155-A1E5-34DF-BDB6-0E198B6E4AEF
+  UUID: 27F07872-6511-3047-A9C8-93A6C67A1BA0
   Functions: 222
-  Symbols:   1003
-  CStrings:  632
+  Symbols:   1008
+  CStrings:  146
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x26
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
Functions:
~ __InvalidPRLikenessCacheSize : 140 -> 128
~ -[PRImageView initWithFrame:] : 100 -> 104
~ -[PRImageView drawRect:] : 148 -> 140
~ -[PRImageView image] : 16 -> 20
~ -[PRImageView isCircular] : 16 -> 20
~ -[PRImageView setCircular:] : 16 -> 20
~ -[PRMonogram initWithText:fontIndex:monogramColor:] : 156 -> 164
~ -[PRMonogram setText:] : 192 -> 180
~ -[PRMonogram color] : 80 -> 60
~ -[PRMonogram plateGradientStartColor] : 152 -> 136
~ -[PRMonogram plateGradientEndColor] : 152 -> 136
~ -[PRMonogram plateSelectedActiveColor] : 152 -> 136
~ -[PRMonogram plateSelectedInactiveColor] : 152 -> 136
~ -[PRMonogram plateSelectedActiveTextColor] : 152 -> 136
~ -[PRMonogram setFontIndex:] : 108 -> 104
~ -[PRMonogram stringAttributesForDiameter:] : 424 -> 408
~ -[PRMonogram snapshotWithSize:scale:options:] : 660 -> 644
~ -[PRMonogram _renderTextInContext:frame:] : 456 -> 452
~ -[PRMonogram description] : 256 -> 232
~ +[PRMonogram _fontSpecs] : 84 -> 68
~ ___24+[PRMonogram _fontSpecs]_block_invoke : 600 -> 560
~ +[PRMonogram countOfFonts] : 60 -> 56
~ +[PRMonogram fontForIndex:plateDiameter:] : 280 -> 256
~ +[PRMonogram kerningForFontIndex:fontSize:] : 116 -> 108
~ +[PRMonogram updatePlateOverlayLayer:] : 260 -> 248
~ -[PRMonogram setColor:] : 64 -> 12
~ -[PRMonogram setMonogramColor:] : 64 -> 12
~ -[PRMonogram(DataRepresentation) dataRepresentationWithVersion:] : 488 -> 464
~ -[PRMonogram(DataRepresentation) _takeValuesFromDataRepresentation:] : 920 -> 896
~ -[NSArray(PersonaUI) pr_objectPassingTest:] : 92 -> 88
~ +[UIColor(PersonaUI) pr_colorNamed:] : 144 -> 136
~ +[PRLikenessCache sharedInstance] : 176 -> 160
~ +[PRLikenessCache _applicationCacheDirectory] : 180 -> 160
~ +[PRLikenessCache _staticRepresentationCacheURL] : 152 -> 140
~ +[PRLikenessCache _ensureExistenceOfDirectory:] : 312 -> 264
~ -[PRLikenessCache init] : 380 -> 368
~ -[PRLikenessCache _cacheKeyForLikeness:context:] : 272 -> 252
~ -[PRLikenessCache _cacheURLForLikeness:context:] : 160 -> 148
~ -[PRLikenessCache imageForLikeness:context:completion:] : 408 -> 412
~ ___55-[PRLikenessCache imageForLikeness:context:completion:]_block_invoke_2 : 200 -> 204
~ ___55-[PRLikenessCache imageForLikeness:context:completion:]_block_invoke_3 : 284 -> 280
~ ___55-[PRLikenessCache imageForLikeness:context:completion:]_block_invoke_5 : 228 -> 236
~ -[PRLikenessCache _fetchFromMemory:context:renderBlock:completion:] : 384 -> 396
~ ___67-[PRLikenessCache _fetchFromMemory:context:renderBlock:completion:]_block_invoke_2 : 108 -> 104
~ -[PRLikenessCache _fetchFromFilesystem:context:renderBlock:completion:] : 364 -> 372
~ -[PRLikenessCache _renderImageForLikeness:context:completion:] : 552 -> 536
~ +[PRLikenessCache _imageAtURL:] : 352 -> 348
~ +[PRLikenessCache _writeImage:toURL:] : 508 -> 452
~ +[PRLikenessCache _removeImageAtURL:] : 304 -> 256
~ +[PRLikenessCache _purgeOldCacheFilesInDirectory:] : 908 -> 884
~ +[PRLikenessCache _propertyValueForURL:forKey:] : 272 -> 232
~ -[PRLikenessCache setCacheDirectory:] : 64 -> 12
~ -[PRLikeness(PersonaUI) accentColor] : 112 -> 104
~ -[PRLikeness(PersonaUI) _accentColorForMonogram] : 160 -> 144
~ -[PRLikeness(PersonaUI) _accentColorForPhoto] : 444 -> 440
~ -[PRLikeness(PersonaUI) snapshotWithSize:scale:options:] : 268 -> 252
~ -[PRLikeness(PersonaUI) _photoSnapshotWithSize:scale:options:] : 440 -> 424
~ +[UIImage(PRLikenessView) pr_imageWithCGImage:cropRect:] : 108 -> 104
~ -[UIImage(PRLikenessView) pr_circleImageOfDiameter:cropRect:] : 160 -> 156
~ +[PRMonogramColor gradientStartColor:] : 168 -> 164
~ +[PRMonogramColor generateMonogramGradientColorsByNameDictionary] : 3668 -> 3392
~ +[PRMonogramColor monogramGradientColorNamed:] : 204 -> 200
~ ___46+[PRMonogramColor monogramGradientColorNamed:]_block_invoke : 64 -> 60
~ +[PRMonogramColor colorWithName:inBundle:] : 156 -> 144
~ +[PRMonogramColor defaultGradientStartColor] : 104 -> 96
~ +[PRMonogramColor defaultGradientEndColor] : 104 -> 96
~ +[PRMonogramColor defaultSelectedActiveColor] : 104 -> 96
~ +[PRMonogramColor defaultSelectedInactiveColor] : 104 -> 96
~ +[PRMonogramColor defaultSelectedActiveTextColor] : 104 -> 96
~ +[PRMonogramColor availableColorNames] : 288 -> 284
~ +[PRMonogramColor availableColors] : 100 -> 92
~ -[PRMonogramColor initWithRandomColor] : 124 -> 116
~ -[PRMonogramColor initWithColorName:] : 104 -> 100
~ -[PRMonogramColor setColorName:] : 200 -> 192
~ -[PRMonogramColor gradientStartColor] : 196 -> 176
~ -[PRMonogramColor gradientEndColor] : 196 -> 176
~ -[PRMonogramColor isEqual:] : 160 -> 164
~ -[PRMonogramColor hash] : 60 -> 56
~ -[PRMonogramColor copyWithZone:] : 40 -> 4
~ -[PRMonogramColor setColor:] : 64 -> 12
~ -[PRMonogramColor setGradientStartColor:] : 64 -> 12
~ -[PRMonogramColor setGradientEndColor:] : 64 -> 12
~ -[PRMonogramColor setSelectedActiveColor:] : 64 -> 12
~ -[PRMonogramColor setSelectedInactiveColor:] : 64 -> 12
~ -[PRMonogramColor setSelectedActiveTextColor:] : 64 -> 12
~ -[PRMonogramColor setBundle:] : 64 -> 12
~ +[NSBundle(PersonaUI) pr_personaUIBundle] : 84 -> 68
~ ___41+[NSBundle(PersonaUI) pr_personaUIBundle]_block_invoke : 96 -> 92
~ -[PRLikenessView initWithFrame:] : 124 -> 136
~ -[PRLikenessView dealloc] : 88 -> 92
~ -[PRLikenessView _updateViewForLikeness:] : 496 -> 476
~ ___41-[PRLikenessView _updateViewForLikeness:]_block_invoke : 404 -> 364
~ -[PRLikenessView _shouldRenderStaticRepresentation] : 240 -> 216
~ -[PRLikenessView _monogramView] : 164 -> 160
~ -[PRLikenessView _imageView] : 176 -> 172
~ -[PRLikenessView _imageForLikeness:completion:] : 416 -> 404
~ ___47-[PRLikenessView _imageForLikeness:completion:]_block_invoke : 272 -> 276
~ -[PRLikenessView setLikeness:] : 296 -> 288
~ -[PRLikenessView _isLikenessEqual:] : 252 -> 264
~ -[PRLikenessView setCircular:] : 128 -> 140
~ -[PRLikenessView setHighlighted:] : 44 -> 52
~ -[PRLikenessView _setDisplayedView:] : 184 -> 188
~ -[PRLikenessView layoutSubviews] : 116 -> 124
~ -[PRLikenessView likeness] : 16 -> 20
~ -[PRLikenessView isCircular] : 16 -> 20
~ -[PRLikenessView highlighted] : 16 -> 20
~ -[PRLikenessView shouldDecode] : 16 -> 20
~ -[PRLikenessView setShouldDecode:] : 16 -> 20
~ -[PRMonogramView initWithFrame:] : 400 -> 396
~ -[PRMonogramView dealloc] : 136 -> 140
~ -[PRMonogramView setMonogram:] : 284 -> 276
~ -[PRMonogramView setBordered:] : 32 -> 36
~ -[PRMonogramView setSelected:] : 28 -> 32
~ -[PRMonogramView setAllowsEditing:] : 28 -> 36
~ -[PRMonogramView setCircular:] : 32 -> 36
~ -[PRMonogramView textFieldResignFirstResponder] : 16 -> 20
~ -[PRMonogramView observeValueForKeyPath:ofObject:change:context:] : 228 -> 232
~ -[PRMonogramView _updateTextLabel] : 968 -> 928
~ -[PRMonogramView layoutSubviews] : 208 -> 212
~ -[PRMonogramView _updateCornerRadii] : 92 -> 96
~ -[PRMonogramView textFieldShouldReturn:] : 40 -> 44
~ -[PRMonogramView textFieldDidBeginEditing:] : 164 -> 148
~ -[PRMonogramView textFieldDidEndEditing:] : 196 -> 184
~ -[PRMonogramView textField:shouldChangeCharactersInRange:replacementString:] : 480 -> 472
~ -[PRMonogramView didMoveToWindow] : 148 -> 144
~ -[PRMonogramView monogram] : 16 -> 20
~ -[PRMonogramView bordered] : 16 -> 20
~ -[PRMonogramView isSelected] : 16 -> 20
~ -[PRMonogramView highlighted] : 16 -> 20
~ -[PRMonogramView setHighlighted:] : 16 -> 20
~ -[PRMonogramView allowsEditing] : 16 -> 20
~ -[PRMonogramView isCircular] : 16 -> 20
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"CAGradientLayer\""
- "@\"NSBundle\""
- "@\"NSCache\""
- "@\"NSData\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSURL\""
- "@\"PRImageView\""
- "@\"PRLikeness\""
- "@\"PRMonogram\""
- "@\"PRMonogramColor\""
- "@\"PRMonogramView\""
- "@\"UIColor\""
- "@\"UIImage\""
- "@\"UIMenu\"40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSArray\"32"
- "@\"UIMenu\"48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSArray\"40"
- "@\"UITextField\""
- "@16@0:8"
- "@20@0:8C16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8@?16"
- "@24@0:8Q16"
- "@24@0:8^{CGImage=}16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8d16"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8Q16d24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16Q24@32"
- "@40@0:8@16d24d32"
- "@48@0:8@16{_NSRange=QQ}24@40"
- "@48@0:8^{CGImage=}16{CGSize=dd}24d40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@48@0:8{CGSize=dd}16d32@40"
- "@56@0:8^{CGImage=}16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "@56@0:8d16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"UITextField\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B40@0:8@\"UITextField\"16@\"NSArray\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "B48@0:8@\"UITextField\"16{_NSRange=QQ}24@\"NSString\"40"
- "B48@0:8@16{_NSRange=QQ}24@40"
- "B56@0:8^{CGContext=}16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "CGColor"
- "CGImage"
- "DataRepresentation"
- "NSCopying"
- "NSObject"
- "PRImageView"
- "PRLikenessCache"
- "PRLikenessCacheContext"
- "PRLikenessView"
- "PRLocalization"
- "PRMonogram"
- "PRMonogramColor"
- "PRMonogramView"
- "PersonaUI"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"CAGradientLayer\",R,N"
- "T@\"NSArray\",R,N"
- "T@\"NSBundle\",&,N,V_bundle"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_text"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_colorName"
- "T@\"NSString\",R,N,V_fontName"
- "T@\"NSURL\",&,N,V_cacheDirectory"
- "T@\"PRLikeness\",&,N,V_likeness"
- "T@\"PRMonogram\",&,N,V_monogram"
- "T@\"PRMonogramColor\",&,N,V_monogramColor"
- "T@\"UIColor\",&,N,V_color"
- "T@\"UIColor\",&,N,V_gradientEndColor"
- "T@\"UIColor\",&,N,V_gradientStartColor"
- "T@\"UIColor\",&,N,V_selectedActiveColor"
- "T@\"UIColor\",&,N,V_selectedActiveTextColor"
- "T@\"UIColor\",&,N,V_selectedInactiveColor"
- "T@\"UIColor\",R,N"
- "T@\"UIImage\",&,N,V_image"
- "TB,N,GisCircular,V_circular"
- "TB,N,GisSelected,V_selected"
- "TB,N,V_allowsEditing"
- "TB,N,V_bordered"
- "TB,N,V_circular"
- "TB,N,V_forceDecode"
- "TB,N,V_highlighted"
- "TB,N,V_renderIfNeeded"
- "TB,N,V_shouldDecode"
- "TB,N,V_useFilesystem"
- "TB,N,V_useMemory"
- "TQ,N,V_cacheSize"
- "TQ,N,V_fontIndex"
- "TQ,R"
- "Td,N,V_scale"
- "Td,R,N,V_baseSize"
- "Td,R,N,V_tracking"
- "UITextFieldDelegate"
- "URLByAppendingPathComponent:"
- "UTF8String"
- "Vv16@0:8"
- "^{CGImage=}"
- "^{CGImage=}16@0:8"
- "^{_NSZone=}16@0:8"
- "_PRMonogramFontSpec"
- "_accentColorForMonogram"
- "_accentColorForPhoto"
- "_allowsEditing"
- "_applicationCacheDirectory"
- "_baseSize"
- "_bordered"
- "_bundle"
- "_cacheDirectory"
- "_cacheKeyForLikeness:context:"
- "_cacheLookupQueue"
- "_cacheSize"
- "_cacheURLForLikeness:context:"
- "_circleGradientLayer"
- "_circular"
- "_cn_SHA1String"
- "_cn_map:"
- "_color"
- "_colorName"
- "_cropRect"
- "_ensureExistenceOfDirectory:"
- "_fetchFromFilesystem:context:renderBlock:completion:"
- "_fetchFromMemory:context:renderBlock:completion:"
- "_fetchWithReadBlock:writeBlock:renderBlock:completion:"
- "_fontIndex"
- "_fontName"
- "_fontSpecs"
- "_forceDecode"
- "_gradientEndColor"
- "_gradientStartColor"
- "_highlighted"
- "_image"
- "_imageAtURL:"
- "_imageForLikeness:completion:"
- "_imageView"
- "_inMemoryCache"
- "_initWithData:"
- "_isLikenessEqual:"
- "_likeness"
- "_likenessType"
- "_monogram"
- "_monogramColor"
- "_monogramView"
- "_photoSnapshotWithSize:scale:options:"
- "_propertyValueForURL:forKey:"
- "_purgeOldCacheFilesInDirectory:"
- "_recipe"
- "_removeImageAtURL:"
- "_renderIfNeeded"
- "_renderImageForLikeness:context:completion:"
- "_renderTextInContext:frame:"
- "_scale"
- "_selected"
- "_selectedActiveColor"
- "_selectedActiveTextColor"
- "_selectedInactiveColor"
- "_setDisplayedView:"
- "_shouldDecode"
- "_shouldRenderStaticRepresentation"
- "_staticRepresentation"
- "_staticRepresentationCacheURL"
- "_takeValuesFromDataRepresentation:"
- "_text"
- "_textField"
- "_tracking"
- "_updateCornerRadii"
- "_updateTextLabel"
- "_updateViewForLikeness:"
- "_useFilesystem"
- "_useMemory"
- "_writeImage:toURL:"
- "accentColor"
- "addClip"
- "addObserver:forKeyPath:options:context:"
- "addSublayer:"
- "addSubview:"
- "allowsEditing"
- "appendBytes:length:"
- "appendToRecipe:text:"
- "appendToRecipe:text:fontIndex:"
- "arrayWithObjects:count:"
- "attributedText"
- "autorelease"
- "availableColorNames"
- "availableColors"
- "baseSize"
- "begin"
- "bezierPathWithOvalInRect:"
- "boolValue"
- "bordered"
- "bounds"
- "bundle"
- "bundleForClass:"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "bytes"
- "cacheDirectory"
- "cacheSize"
- "circular"
- "class"
- "colorName"
- "colorNamed:inBundle:compatibleWithTraitCollection:"
- "colorWithAlphaComponent:"
- "colorWithName:inBundle:"
- "colorWithRed:green:blue:alpha:"
- "colorWithWhite:alpha:"
- "commit"
- "compare:"
- "conformsToProtocol:"
- "contentsOfDirectoryAtURL:includingPropertiesForKeys:options:error:"
- "contextWithCacheSize:"
- "copy"
- "copyWithZone:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "countOfFonts"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "cropRect"
- "d"
- "d16@0:8"
- "d32@0:8Q16d24"
- "dataRepresentation"
- "dataRepresentationWithVersion:"
- "dateWithTimeIntervalSinceNow:"
- "dealloc"
- "debugDescription"
- "defaultBundle"
- "defaultGradientEndColor"
- "defaultGradientStartColor"
- "defaultManager"
- "defaultSelectedActiveColor"
- "defaultSelectedActiveTextColor"
- "defaultSelectedInactiveColor"
- "description"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToWindow"
- "drawInRect:"
- "drawRect:"
- "editRect"
- "endOfDocument"
- "enumerateSubstringsInRange:options:usingBlock:"
- "exceptionWithName:reason:userInfo:"
- "fileURLWithPath:isDirectory:"
- "fileURLWithPath:isDirectory:relativeToURL:"
- "font"
- "fontForIndex:plateDiameter:"
- "fontName"
- "fontWithName:size:"
- "forceDecode"
- "generateMonogramGradientColorsByNameDictionary"
- "getBytes:range:"
- "getRed:green:blue:alpha:"
- "getResourceValue:forKey:error:"
- "gradientEndColor"
- "gradientEndName:"
- "gradientStartColor"
- "gradientStartColor:"
- "gradientStartName:"
- "hash"
- "highlighted"
- "image"
- "imageForLikeness:context:completion:"
- "imageWithCGImage:"
- "imageWithCGImage:scale:orientation:"
- "indexOfObjectPassingTest:"
- "init"
- "initWithBytes:length:encoding:"
- "initWithColorName:"
- "initWithColorName:inBundle:"
- "initWithFrame:"
- "initWithLikeness:"
- "initWithRandomColor"
- "initWithString:attributes:"
- "initWithText:fontIndex:monogramColor:"
- "initialize"
- "isCircular"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "isSelected"
- "kerningForFontIndex:fontSize:"
- "lastObject"
- "layer"
- "layoutSubviews"
- "length"
- "lengthOfBytesUsingEncoding:"
- "likeness"
- "mainBundle"
- "mainScreen"
- "markedTextRange"
- "monogram"
- "monogramColor"
- "monogramGradientColorNamed:"
- "monogramWithData:"
- "mutableCopy"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "observeValueForKeyPath:ofObject:change:context:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "plateFlatColor"
- "plateGradientEndColor"
- "plateGradientStartColor"
- "plateOverlayLayer"
- "plateSelectedActiveColor"
- "plateSelectedActiveTextColor"
- "plateSelectedInactiveColor"
- "pointSize"
- "pr_backgroundColor"
- "pr_circleImageOfDiameter:cropRect:"
- "pr_circleImageWithCropRect:"
- "pr_colorNamed:"
- "pr_darkAccentColor"
- "pr_errorWithCode:"
- "pr_imageRef"
- "pr_imageWithCGImage:"
- "pr_imageWithCGImage:cropRect:"
- "pr_imageWithCGImage:size:scale:"
- "pr_lightAccentColor"
- "pr_objectPassingTest:"
- "pr_personaUIBundle"
- "recipe"
- "release"
- "removeItemAtURL:error:"
- "removeObserver:forKeyPath:"
- "renderIfNeeded"
- "resignFirstResponder"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "scale"
- "screen"
- "selected"
- "selectedActiveColor"
- "selectedActiveTextColor"
- "selectedInactiveColor"
- "self"
- "setAdjustsFontSizeToFitWidth:"
- "setAlignment:"
- "setAllowsDefaultTighteningForTruncation:"
- "setAllowsEditing:"
- "setAttributedText:"
- "setAutocapitalizationType:"
- "setAutocorrectionType:"
- "setBordered:"
- "setBundle:"
- "setCacheDirectory:"
- "setCacheSize:"
- "setCircular:"
- "setColor:"
- "setColorName:"
- "setColors:"
- "setContentMode:"
- "setCornerRadius:"
- "setDelegate:"
- "setDisableActions:"
- "setEnabled:"
- "setEndPoint:"
- "setFont:"
- "setFontIndex:"
- "setFontIndexToUnsupportedValue"
- "setForceDecode:"
- "setFrame:"
- "setGradientEndColor:"
- "setGradientStartColor:"
- "setHidden:"
- "setHighlighted:"
- "setImage:"
- "setKeyboardType:"
- "setLikeness:"
- "setMonogram:"
- "setMonogramColor:"
- "setName:"
- "setNeedsDisplay"
- "setNeedsLayout"
- "setNeedsRedraw"
- "setObject:forKey:"
- "setObject:forKey:cost:"
- "setOpaque:"
- "setRasterizationScale:"
- "setRenderIfNeeded:"
- "setReturnKeyType:"
- "setScale:"
- "setSelected:"
- "setSelectedActiveColor:"
- "setSelectedActiveTextColor:"
- "setSelectedInactiveColor:"
- "setSelectedTextRange:"
- "setShouldDecode:"
- "setSpellCheckingType:"
- "setStartPoint:"
- "setText:"
- "setTextAlignment:"
- "setTintColor:"
- "setTotalCostLimit:"
- "setUseFilesystem:"
- "setUseMemory:"
- "sharedInstance"
- "shouldDecode"
- "size"
- "sizeWithAttributes:"
- "snapshotWithSize:scale:options:"
- "specForFontWithName:baseSize:tracking:"
- "staticRepresentation"
- "staticRepresentationData"
- "stringAttributesForDiameter:"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByReplacingCharactersInRange:withString:"
- "stringWithFormat:"
- "superclass"
- "systemFontOfSize:weight:design:"
- "textField:editMenuForCharactersInRange:suggestedActions:"
- "textField:editMenuForCharactersInRanges:suggestedActions:"
- "textField:insertInputSuggestion:"
- "textField:shouldChangeCharactersInRange:replacementString:"
- "textField:shouldChangeCharactersInRanges:replacementString:"
- "textField:willDismissEditMenuWithAnimator:"
- "textField:willPresentEditMenuWithAnimator:"
- "textFieldDidBeginEditing:"
- "textFieldDidChangeSelection:"
- "textFieldDidEndEditing:"
- "textFieldDidEndEditing:reason:"
- "textFieldResignFirstResponder"
- "textFieldShouldBeginEditing:"
- "textFieldShouldClear:"
- "textFieldShouldEndEditing:"
- "textFieldShouldReturn:"
- "textRangeFromPosition:toPosition:"
- "tracking"
- "type"
- "uniqueIdentifier"
- "updatePlateOverlayLayer:"
- "useFilesystem"
- "useMemory"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"UITextField\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v32@0:8@\"UITextField\"16@\"<UIEditMenuInteractionAnimating>\"24"
- "v32@0:8@\"UITextField\"16@\"UIInputSuggestion\"24"
- "v32@0:8@\"UITextField\"16q24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16q24"
- "v36@0:8@16@24C32"
- "v40@0:8@16@24@?32"
- "v48@0:8@16@24@32^v40"
- "v48@0:8@16@24@?32@?40"
- "v48@0:8@?16@?24@?32@?40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "whiteColor"
- "window"
- "zone"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"

```
