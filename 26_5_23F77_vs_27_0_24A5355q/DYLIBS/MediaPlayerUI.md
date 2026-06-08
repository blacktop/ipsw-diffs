## MediaPlayerUI

> `/System/Library/PrivateFrameworks/MediaPlayerUI.framework/MediaPlayerUI`

```diff

 4025.100.2.1.0
-  __TEXT.__text: 0x5454
-  __TEXT.__auth_stubs: 0x530
+  __TEXT.__text: 0x52b0
   __TEXT.__objc_methlist: 0x4b0
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x100
-  __TEXT.__cstring: 0x773
+  __TEXT.__gcc_except_tab: 0x120
+  __TEXT.__cstring: 0x77d
   __TEXT.__dlopen_cstrs: 0x169
   __TEXT.__unwind_info: 0x258
-  __TEXT.__objc_classname: 0x72
-  __TEXT.__objc_methname: 0x1309
-  __TEXT.__objc_methtype: 0x32c
-  __TEXT.__objc_stubs: 0x1340
-  __DATA_CONST.__got: 0x150
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x360
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x668
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x2a8
+  __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x6e0
   __AUTH_CONST.__objc_const: 0x728
-  __AUTH.__objc_data: 0xf0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x140
   __DATA.__objc_ivar: 0x58
   __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D2309482-BE31-3104-80D9-F1B025AA07F5
+  UUID: DF417752-24EB-32AE-B28C-626D8C63A4AB
   Functions: 141
-  Symbols:   678
-  CStrings:  425
+  Symbols:   681
+  CStrings:  128
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x9
- _objc_autorelease
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
Functions:
~ +[MPUPlaybackAlertController contentRestrictedPlaybackAlertControllerForContentType:dismissalBlock:] : 804 -> 760
~ ___100+[MPUPlaybackAlertController contentRestrictedPlaybackAlertControllerForContentType:dismissalBlock:]_block_invoke : 164 -> 156
~ _getLSApplicationWorkspaceClass : 220 -> 224
~ ___100+[MPUPlaybackAlertController contentRestrictedPlaybackAlertControllerForContentType:dismissalBlock:]_block_invoke_2 : 480 -> 476
~ +[MPUPlaybackAlertController playbackAlertControllerForItem:contentType:error:dismissalBlock:] : 276 -> 284
~ +[MPUPlaybackAlertController playbackAlertTypeForError:] : 308 -> 288
~ +[MPUPlaybackAlertController genericAlertControllerForItem:error:dismissalBlock:] : 3148 -> 3000
~ ___81+[MPUPlaybackAlertController genericAlertControllerForItem:error:dismissalBlock:]_block_invoke : 408 -> 396
~ ___81+[MPUPlaybackAlertController genericAlertControllerForItem:error:dismissalBlock:]_block_invoke_4 : 132 -> 124
~ +[MPUPlaybackAlertController userRemovedAlertControllerForItem:dismissalBlock:] : 1948 -> 1908
~ ___79+[MPUPlaybackAlertController userRemovedAlertControllerForItem:dismissalBlock:]_block_invoke : 196 -> 188
~ ___79+[MPUPlaybackAlertController userRemovedAlertControllerForItem:dismissalBlock:]_block_invoke_4 : 124 -> 120
~ -[MPUPlaybackAlertController playbackAlertType] : 16 -> 20
~ -[MPUPlaybackAlertController item] : 16 -> 20
~ -[MPUPlaybackAlertController error] : 16 -> 20
~ +[MPUTheme cachedObjectWithKey:block:] : 224 -> 212
~ +[MPUTheme disabledPlaybackControlColor] : 108 -> 100
~ +[MPUTheme _themeAssetCache] : 84 -> 68
~ +[MPURatingControl ratingStarImage] : 116 -> 108
~ +[MPURatingControl ratingDotImage] : 152 -> 148
~ ___34+[MPURatingControl ratingDotImage]_block_invoke : 204 -> 196
~ ___34+[MPURatingControl ratingDotImage]_block_invoke_2 : 208 -> 200
~ -[MPURatingControl initWithFrame:] : 432 -> 436
~ -[MPURatingControl layoutSubviews] : 460 -> 468
~ -[MPURatingControl ratingValueForLocationInView:] : 432 -> 436
~ -[MPURatingControl _handleTapGesture:] : 152 -> 140
~ -[MPURatingControl _handlePanGesture:] : 168 -> 156
~ -[MPURatingControl setRating:animated:] : 32 -> 36
~ -[MPURatingControl sizeThatFits:] : 92 -> 88
~ -[MPURatingControl _updateImageViewsForRatingAnimated:] : 260 -> 252
~ -[MPURatingControl rating] : 16 -> 20
~ -[MPUApplicationDefaults initWithApplicationIdentifier:] : 212 -> 208
~ -[MPUApplicationDefaults dealloc] : 108 -> 104
~ -[MPUApplicationDefaults registerDefaults:] : 160 -> 152
~ ___43-[MPUApplicationDefaults registerDefaults:]_block_invoke : 60 -> 12
~ -[MPUApplicationDefaults boolForKey:] : 376 -> 384
~ ___37-[MPUApplicationDefaults boolForKey:]_block_invoke : 84 -> 80
~ -[MPUApplicationDefaults stringForKey:] : 96 -> 92
~ -[MPUApplicationDefaults arrayForKey:] : 96 -> 92
~ -[MPUApplicationDefaults dictionaryForKey:] : 96 -> 92
~ -[MPUApplicationDefaults integerForKey:] : 376 -> 384
~ ___40-[MPUApplicationDefaults integerForKey:]_block_invoke : 84 -> 80
~ -[MPUApplicationDefaults numberForKey:] : 96 -> 92
~ -[MPUApplicationDefaults setInteger:forKey:] : 132 -> 128
~ -[MPUApplicationDefaults dateForKey:] : 96 -> 92
~ -[MPUApplicationDefaults _applyUpdates] : 164 -> 160
~ ___39-[MPUApplicationDefaults _applyUpdates]_block_invoke : 112 -> 108
~ -[MPUApplicationDefaults _defaultsDidChange] : 108 -> 104
~ -[MPUApplicationDefaults _setObject:forKey:] : 264 -> 268
~ -[MPUArtworkView dealloc] : 72 -> 76
~ -[MPUArtworkView updateConstraints] : 188 -> 180
~ -[MPUArtworkView setHighlighted:animated:] : 104 -> 108
~ -[MPUArtworkView setHighlightedImage:] : 100 -> 104
~ -[MPUArtworkView setHighlightedAnimationImages:] : 100 -> 104
~ -[MPUArtworkView setImage:] : 156 -> 160
~ -[MPUArtworkView startAnimating] : 100 -> 104
~ -[MPUArtworkView stopAnimating] : 100 -> 104
~ -[MPUArtworkView setAutomaticallyApplyAspectConstraints:] : 148 -> 124
~ -[MPUArtworkView setDimsWhenHighlighted:] : 148 -> 128
~ -[MPUArtworkView setPlaceholderImage:] : 168 -> 172
~ -[MPUArtworkView _aspectConstraintMultiplier] : 16 -> 20
~ -[MPUArtworkView _shouldShowHighlightView] : 124 -> 116
~ -[MPUArtworkView _updateHighlightViewAnimated:] : 776 -> 772
~ ___47-[MPUArtworkView _updateHighlightViewAnimated:]_block_invoke : 24 -> 28
~ ___47-[MPUArtworkView _updateHighlightViewAnimated:]_block_invoke_2 : 24 -> 28
~ ___47-[MPUArtworkView _updateHighlightViewAnimated:]_block_invoke_3 : 96 -> 100
~ -[MPUArtworkView _externalImage] : 16 -> 20
~ -[MPUArtworkView automaticallyApplyAspectConstraints] : 16 -> 20
~ -[MPUArtworkView dimsWhenHighlighted] : 16 -> 20
~ -[MPUArtworkView forcesAnimatedUnhighlighting] : 16 -> 20
~ -[MPUArtworkView setForcesAnimatedUnhighlighting:] : 16 -> 20
~ -[MPUArtworkView placeholderImage] : 16 -> 20
~ -[MPUArtworkView isDisplayingPlaceholder] : 16 -> 20
~ -[MPUArtworkView setDisplayingPlaceholder:] : 16 -> 20
~ +[UIImage(MPUAdditions) imageWithSize:opaque:fromBlock:] : 140 -> 144
~ -[UIImage(MPUAdditions) scaledImageWithSize:] : 152 -> 148
CStrings:
- ".cxx_destruct"
- "@\"<MPURatingControlDelegate>\""
- "@\"MPAVItem\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSLayoutConstraint\""
- "@\"NSMutableArray\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"UIImage\""
- "@\"UIPanGestureRecognizer\""
- "@\"UITapGestureRecognizer\""
- "@\"UIView\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@?24"
- "@32@0:8@16Q24"
- "@32@0:8q16@?24"
- "@32@0:8{CGSize=dd}16"
- "@40@0:8@16@24@?32"
- "@44@0:8{CGSize=dd}16B32@?36"
- "@48@0:8@16q24@32@?40"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B40@0:8{CGPoint=dd}16@32"
- "MPUAdditions"
- "MPUApplicationDefaults"
- "MPUArtworkView"
- "MPUPlaybackAlertController"
- "MPURatingControl"
- "MPUTheme"
- "Q"
- "T@\"<MPURatingControlDelegate>\",W,N,V_delegate"
- "T@\"MPAVItem\",R,N,V_item"
- "T@\"NSError\",R,N,V_error"
- "T@\"UIImage\",&,N,V_placeholderImage"
- "T@\"UIImage\",R,N,V_externalImage"
- "TB,N,GisDisplayingPlaceholder,V_displayingPlaceholder"
- "TB,N,V_automaticallyApplyAspectConstraints"
- "TB,N,V_dimsWhenHighlighted"
- "TB,N,V_forcesAnimatedUnhighlighting"
- "TB,R,N"
- "Td,N,G_aspectConstraintMultiplier,S_setAspectConstraintMultiplier:"
- "Td,N,V_rating"
- "Tq,R,N,V_playbackAlertType"
- "T{UIEdgeInsets=dddd},N,V_hitTestEdgeInsets"
- "URL"
- "URLWithString:"
- "^{__CFString=}16@0:8"
- "_accessQueue"
- "_animatesContents"
- "_applicationIdentifier"
- "_applyUpdates"
- "_aspectConstraint"
- "_aspectConstraintMultiplier"
- "_automaticallyApplyAspectConstraints"
- "_defaultValues"
- "_defaultsDidChange"
- "_defaultsDidChangeNotificationName"
- "_defaultsDomain"
- "_delegate"
- "_dimsWhenHighlighted"
- "_displayingPlaceholder"
- "_error"
- "_externalImage"
- "_forcesAnimatedUnhighlighting"
- "_handlePanGesture:"
- "_handleTapGesture:"
- "_highlightView"
- "_hitTestEdgeInsets"
- "_imageDidChange"
- "_imageViews"
- "_isDeallocating"
- "_item"
- "_objectForKey:expectedTypeID:"
- "_panGestureRecognizer"
- "_placeholderImage"
- "_playbackAlertType"
- "_rating"
- "_referenceCountForDefferringUpdates"
- "_setAnimatesContents:"
- "_setAspectConstraintMultiplier:"
- "_setObject:forKey:"
- "_setPlaceholderHidden:"
- "_shouldShowHighlightView"
- "_tapGestureRecognizer"
- "_themeAssetCache"
- "_updateHighlightViewAnimated:"
- "_updateImageView:proposedImage:filled:"
- "_updateImageViewsForRatingAnimated:"
- "actionType"
- "actionWithTitle:style:handler:"
- "addAction:"
- "addConstraint:"
- "addGestureRecognizer:"
- "addObject:"
- "addSubview:"
- "alertControllerWithTitle:message:preferredStyle:"
- "alpha"
- "animateWithDuration:animations:"
- "animateWithDuration:animations:completion:"
- "arrayForKey:"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "aspectConstraintMultiplier"
- "asset"
- "automaticallyApplyAspectConstraints"
- "bezierPathWithRoundedRect:cornerRadius:"
- "boolForKey:"
- "boolValue"
- "bounds"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "buttons"
- "cachedObjectWithKey:block:"
- "center"
- "code"
- "colorWithRed:green:blue:alpha:"
- "colorWithWhite:alpha:"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "contentRestrictedPlaybackAlertControllerForContentType:dismissalBlock:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "d"
- "d16@0:8"
- "d32@0:8{CGPoint=dd}16"
- "dateForKey:"
- "dealloc"
- "defaultButtonIndex"
- "defaultCenter"
- "defaultWorkspace"
- "delegate"
- "deviceMediaLibrary"
- "dictionaryForKey:"
- "dimsWhenHighlighted"
- "disabledPlaybackControlColor"
- "displayingPlaceholder"
- "domain"
- "drawInRect:"
- "easyTouchDefaultHitRectInsets"
- "enumerateObjectsUsingBlock:"
- "error"
- "fill"
- "firstObject"
- "forcesAnimatedUnhighlighting"
- "frame"
- "genericAlertControllerForItem:error:dismissalBlock:"
- "hasRestrictionsPasscode"
- "highlightedAnimationImages"
- "highlightedImage"
- "hitTestEdgeInsets"
- "image"
- "imageNamed:inBundle:"
- "imageWithSize:opaque:fromBlock:"
- "incrementDisplayCount"
- "indexOfObject:"
- "init"
- "initWithApplicationIdentifier:"
- "initWithDialogDictionary:"
- "initWithFrame:"
- "initWithImage:"
- "initWithTarget:action:"
- "integerForKey:"
- "integerValue"
- "isAnimating"
- "isAssetLoaded"
- "isCloudLibraryEnabled"
- "isDisplayable"
- "isDisplayingPlaceholder"
- "isEqualToString:"
- "isFileURL"
- "isHidden"
- "isHighlighted"
- "item"
- "kind"
- "layer"
- "layoutSubviews"
- "length"
- "localizedStringWithFormat:"
- "locationInView:"
- "longLongValue"
- "mainBundle"
- "mainTitle"
- "mediaItem"
- "mediaLibrary"
- "mediaPlayerUIBundle"
- "mediaType"
- "message"
- "multiplier"
- "networkType"
- "noDefaultButton"
- "numberForKey:"
- "numberWithInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "opacity"
- "openSensitiveURL:withOptions:"
- "openURL:options:completionHandler:"
- "performBatchUpdates:"
- "performDefaultActionForDialog:"
- "placeholderImage"
- "playbackAlertControllerForItem:contentType:error:dismissalBlock:"
- "playbackAlertType"
- "playbackAlertTypeForError:"
- "pointInside:withEvent:"
- "postNotificationName:object:"
- "presentationLayer"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "rating"
- "ratingDidChangeForRatingControl:"
- "ratingDotImage"
- "ratingStarImage"
- "ratingValueForLocationInView:"
- "registerDefaults:"
- "removeConstraint:"
- "removeFromSuperview"
- "removeItems:"
- "removeValueForKey:"
- "scaledImageWithSize:"
- "setAlpha:"
- "setArray:forKey:"
- "setAutomaticallyApplyAspectConstraints:"
- "setAutoresizingMask:"
- "setBackgroundColor:"
- "setBool:forKey:"
- "setBoolValue:forSetting:"
- "setCenter:"
- "setClipsToBounds:"
- "setContentMode:"
- "setDate:forKey:"
- "setDelegate:"
- "setDictionary:forKey:"
- "setDimsWhenHighlighted:"
- "setDisplayingPlaceholder:"
- "setFill"
- "setForcesAnimatedUnhighlighting:"
- "setFrame:"
- "setHidden:"
- "setHighlighted:"
- "setHighlighted:animated:"
- "setHighlightedAnimationImages:"
- "setHighlightedImage:"
- "setHitTestEdgeInsets:"
- "setImage:"
- "setInteger:forKey:"
- "setNeedsUpdateConstraints"
- "setNumber:forKey:"
- "setObject:forKey:"
- "setOpaque:"
- "setPlaceholderImage:"
- "setPreferredAction:"
- "setRating:"
- "setRating:animated:"
- "setString:forKey:"
- "sharedApplication"
- "sharedConnection"
- "sharedController"
- "sharedMonitor"
- "sharedRestrictionsMonitor"
- "shouldDisplayPlaceholder"
- "size"
- "sizeThatFits:"
- "startAnimating"
- "state"
- "stopAnimating"
- "storeItemID"
- "stringByAppendingString:"
- "stringForKey:"
- "stringWithFormat:"
- "tableViewContentLeftInset"
- "title"
- "type"
- "updateConstraints"
- "userInfo"
- "userRemovedAlertControllerForItem:dismissalBlock:"
- "usesSubscriptionLease"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8B16B20"
- "v24@0:8d16"
- "v28@0:8B16@20"
- "v28@0:8d16B24"
- "v32@0:8@16@24"
- "v32@0:8q16@24"
- "v36@0:8@16@24B32"
- "v48@0:8{UIEdgeInsets=dddd}16"
- "valueForProperty:"
- "viewDidMoveToSuperview"
- "{CGSize=dd}32@0:8{CGSize=dd}16"
- "{UIEdgeInsets=\"top\"d\"left\"d\"bottom\"d\"right\"d}"
- "{UIEdgeInsets=dddd}16@0:8"

```
