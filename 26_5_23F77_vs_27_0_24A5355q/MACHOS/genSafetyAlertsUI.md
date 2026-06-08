## genSafetyAlertsUI

> `/System/Library/PrivateFrameworks/SafetyAlerts.framework/PlugIns/genSafetyAlertsUI.appex/genSafetyAlertsUI`

```diff

-67.0.4.0.0
-  __TEXT.__text: 0x7958
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0x11a0
-  __TEXT.__objc_methlist: 0x5c4
-  __TEXT.__const: 0x2a8
-  __TEXT.__cstring: 0x2f1
-  __TEXT.__gcc_except_tab: 0xc50
-  __TEXT.__objc_classname: 0x79
-  __TEXT.__objc_methname: 0x14e0
-  __TEXT.__objc_methtype: 0x52a
-  __TEXT.__oslogstring: 0x165f
-  __TEXT.__unwind_info: 0x330
-  __DATA_CONST.__auth_got: 0x278
-  __DATA_CONST.__got: 0x160
-  __DATA_CONST.__const: 0x1d0
-  __DATA_CONST.__cfstring: 0x320
-  __DATA_CONST.__objc_classlist: 0x10
+70.0.15.0.0
+  __TEXT.__text: 0x9260
+  __TEXT.__auth_stubs: 0x430
+  __TEXT.__objc_stubs: 0x1b00
+  __TEXT.__objc_methlist: 0x90c
+  __TEXT.__const: 0x130
+  __TEXT.__cstring: 0x4e4
+  __TEXT.__gcc_except_tab: 0x1154
+  __TEXT.__objc_classname: 0xc1
+  __TEXT.__objc_methname: 0x221b
+  __TEXT.__objc_methtype: 0x9b7
+  __TEXT.__oslogstring: 0x1f67
+  __TEXT.__unwind_info: 0x348
+  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__cfstring: 0x680
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x18
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x730
-  __DATA.__objc_selrefs: 0x6c0
-  __DATA.__objc_ivar: 0x3c
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x120
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0x228
+  __DATA_CONST.__got: 0x1c0
+  __DATA.__objc_const: 0xc40
+  __DATA.__objc_selrefs: 0xa60
+  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_data: 0x140
+  __DATA.__data: 0x1e0
   __DATA.__common: 0x10
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1F13831A-3C5A-3C66-99A0-2DE27BF8C490
-  Functions: 113
-  Symbols:   149
-  CStrings:  448
+  UUID: 7287A5A0-77A8-3E8B-A61C-7C303B96A164
+  Functions: 146
+  Symbols:   154
+  CStrings:  716
 
Symbols:
+ _CGRectZero
+ _MKMapRectNull
+ _MKMapRectUnion
+ _NSLinkAttributeName
+ _NSTextCheckingCityKey
+ _NSTextCheckingStateKey
+ _NSTextCheckingStreetKey
+ _OBJC_CLASS_$_CLLocationManager
+ _OBJC_CLASS_$_CompletionGuard
+ _OBJC_CLASS_$_MKPolygon
+ _OBJC_CLASS_$_MKPolygonRenderer
+ _OBJC_CLASS_$_NSCharacterSet
+ _OBJC_CLASS_$_NSDataDetector
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_CLASS_$_SATapToRadar
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UIView
+ _OBJC_CLASS_$__MKStaticMapView
+ _OBJC_METACLASS_$_CompletionGuard
+ _OBJC_METACLASS_$_SATapToRadar
+ __NSConcreteGlobalBlock
+ __os_log_error_impl
+ _bzero
+ _dispatch_once
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_initWeak
+ _objc_retain_x23
+ _objc_setProperty_nonatomic_copy
- _CFRelease
- _CGColorCreateGenericRGB
- _CGContextAddLineToPoint
- _CGContextAddPath
- _CGContextBeginPath
- _CGContextClosePath
- _CGContextFillEllipseInRect
- _CGContextFillPath
- _CGContextMoveToPoint
- _CGContextSetLineWidth
- _CGContextSetStrokeColorWithColor
- _CGContextStrokeEllipseInRect
- _CGContextStrokeLineSegments
- _CGContextStrokePath
- _CGPathCreateWithRoundedRect
- _CGPointZero
- _NSForegroundColorAttributeName
- _OBJC_CLASS_$_MKMapSnapshotOptions
- _OBJC_CLASS_$_MKMapSnapshotter
- _OBJC_CLASS_$_UITraitCollection
- __ZN16SACircleRenderer10drawCircleEdddP7CGColorS1_b
- __ZNSt3__117bad_function_callD1Ev
- __ZTINSt3__117bad_function_callE
- __ZTVN10__cxxabiv117__class_type_infoE
- __ZTVN10__cxxabiv120__si_class_type_infoE
- __ZTVNSt3__117bad_function_callE
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
- _objc_retain_x28
- _strcmp
CStrings:
+ "#saGeneralNotif,setupMapWithNotification,networkUsageMode:Minimized,isDailyLivabilityAlert:%d"
+ "#saGeneralNotif,setupMapWithNotification,networkUsageMode:Normal,isDailyLivabilityAlert:%d"
+ "#saGeneralNotif,setupMapWithNotification,usingMapRect,overlayCount:%{public}d"
+ "#saGeneralNotif,setupMapWithNotification,usingRegionFallback"
+ "#saGeneralNotificationExtension,CompletionGuard auto-completing"
+ "#saGeneralNotificationExtension,didReceiveNotificationResponse,Failed to open Maps app with alert hash: %@, isLt :%d"
+ "#saGeneralNotificationExtension,didReceiveNotificationResponse,Missing alert hash."
+ "#saGeneralNotificationExtension,didReceiveNotificationResponse,Successfully opened Maps app with alert hash: %@, isLt :%d"
+ "#saGeneralNotificationExtension,didReceiveNotificationResponse,User tapped 'Open in Maps' action"
+ "#saGeneralNotificationExtension,didReceiveNotificationResponse,User tapped 'Tap To Radar' action"
+ "#saGeneralNotificationExtension,didReceiveNotificationResponse,action identifier: %@"
+ "#saGeneralNotificationExtension,didReceiveNotificationResponse,alertHash: %@"
+ "#saGeneralNotificationExtension,didReceiveNotificationResponse,nil URL"
+ "#saGeneralNotificationExtension,didReceiveNotificationResponse,unsupported action identifier:%@"
+ "#saGeneralNotificationExtension,mapViewDidFailLoadingMap,error:%{public}@"
+ "#saGeneralNotificationExtension,mapViewDidFinishLoadingMap"
+ "#saGeneralNotificationExtension,mutableAttributedStringWithLinks,detectedURL: %{public}@"
+ "#saGeneralNotificationExtension,mutableAttributedStringWithLinks,result: %{public}@"
+ "#saGeneralNotificationExtension,openURL,success:%d url:%{public}@"
+ "#saGeneralNotificationExtension,openURL: %{public}@"
+ "#saGeneralNotificationExtension,setupMapWithNotification,centroidInvalid"
+ "#saGeneralNotificationExtension,setupMapWithNotification,invalidGeometry"
+ "#saGeneralNotificationExtension,setupMapWithNotification,noGeometry"
+ "#saGeneralNotificationExtension,setupMapWithNotification,regionSpan:%{public}f"
+ "#saGeneralNotificationExtension,setupMapWithNotification,usingGeometryCentroid, lat:%{sensitive}f, lon:%{sensitive}f"
+ "#saGeneralNotificationExtension,setupMapWithNotification,valid polygons:%{public}lu"
+ "#saGeneralNotificationExtension,tapToRadar,failed"
+ "#saGeneralNotificationExtension,tapToRadar,launched"
+ "#saGeneralNotificationExtension,tapToRadar,nil URL"
+ ","
+ ".cxx_construct"
+ "/System/Library/LocationBundles/SafetyAlerts.bundle"
+ "1979088"
+ "2280104"
+ "@\"CLLocationManager\""
+ "@\"MKAnnotationView\"32@0:8@\"_MKStaticMapView\"16@\"<MKAnnotation>\"24"
+ "@\"MKOverlayRenderer\"32@0:8@\"_MKStaticMapView\"16@\"<MKOverlay>\"24"
+ "@\"NSArray\"40@0:8@\"UITextView\"16{_NSRange=QQ}24"
+ "@\"UIAction\"40@0:8@\"UITextView\"16@\"UITextItem\"24@\"UIAction\"32"
+ "@\"UIMenu\"40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSArray\"32"
+ "@\"UIMenu\"48@0:8@\"UITextView\"16{_NSRange=QQ}24@\"NSArray\"40"
+ "@\"UITextItemMenuConfiguration\"40@0:8@\"UITextView\"16@\"UITextItem\"24@\"UIMenu\"32"
+ "@\"UIView\"24@0:8@\"UIScrollView\"16"
+ "@\"_MKStaticMapView\""
+ "@20@0:8i16"
+ "@24@0:8@16"
+ "@32@0:8@?16Q24"
+ "@40@0:8@16@24@32"
+ "@40@0:8@16B24B28@32"
+ "@40@0:8@16{_NSRange=QQ}24"
+ "@48@0:8@16{_NSRange=QQ}24@40"
+ "@?"
+ "@?16@0:8"
+ "B"
+ "B24@0:8@\"UIScrollView\"16"
+ "B24@0:8@\"UITextView\"16"
+ "B40@0:8@\"UITextView\"16@\"NSArray\"24@\"NSString\"32"
+ "B40@0:8@16@24@32"
+ "B48@0:8@\"UITextView\"16@\"NSTextAttachment\"24{_NSRange=QQ}32"
+ "B48@0:8@\"UITextView\"16@\"NSURL\"24{_NSRange=QQ}32"
+ "B48@0:8@\"UITextView\"16{_NSRange=QQ}24@\"NSString\"40"
+ "B48@0:8@16@24{_NSRange=QQ}32"
+ "B48@0:8@16{_NSRange=QQ}24@40"
+ "B56@0:8@\"UITextView\"16@\"NSTextAttachment\"24{_NSRange=QQ}32q48"
+ "B56@0:8@\"UITextView\"16@\"NSURL\"24{_NSRange=QQ}32q48"
+ "B56@0:8@16@24{_NSRange=QQ}32q48"
+ "CompletionGuard"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Description"
+ "Keywords"
+ "Liveon"
+ "Please attach screen shots and provide a brief description of the issue faced."
+ "Q"
+ "R"
+ "SAFETY_ALERTS_TAP_TO_RADAR_ACTION_TITLE"
+ "SATapToRadar"
+ "Safety Alerts"
+ "T@\"CLLocationManager\",&,N,V_locationManager"
+ "T@\"UIImageView\",&,N,V_ltStatusIcon"
+ "T@\"UILabel\",&,N,V_additionalDetailsLt"
+ "T@\"UILabel\",&,N,V_additionalDetailsOriginal"
+ "T@\"UILabel\",&,N,V_ltByIPhone"
+ "T@\"UILabel\",&,N,V_ltTitle"
+ "T@\"UIStackView\",&,N,V_ltStatusStack"
+ "T@\"UIStackView\",&,N,V_saLtStack"
+ "T@\"UnselectableUITextView\",&,N,V_instructionTextLt"
+ "T@\"UnselectableUITextView\",&,N,V_instructionTextOriginal"
+ "T@\"UnselectableUITextView\",&,N,V_ltBody"
+ "T@\"_MKStaticMapView\",&,N,V_mapView"
+ "T@?,C,N,V_completion"
+ "TB,N,V_hasCompleted"
+ "TQ,N,V_responseOption"
+ "TimeOfIssue"
+ "Title"
+ "UIScrollViewDelegate"
+ "UITextViewDelegate"
+ "URL"
+ "URLHostAllowedCharacterSet"
+ "URLQueryAllowedCharacterSet"
+ "URLWithString:"
+ "[ESA][Liveon][EQ]"
+ "[ESA][Liveon][IT]"
+ "_MKStaticMapViewDelegate"
+ "_additionalDetailsLt"
+ "_additionalDetailsOriginal"
+ "_completion"
+ "_hasCompleted"
+ "_instructionTextLt"
+ "_instructionTextOriginal"
+ "_locationManager"
+ "_ltBody"
+ "_ltByIPhone"
+ "_ltStatusIcon"
+ "_ltStatusStack"
+ "_ltTitle"
+ "_mapView"
+ "_responseOption"
+ "_saLtStack"
+ "actionIdentifier"
+ "actionTitle"
+ "addAttribute:value:range:"
+ "addLegendToMapView"
+ "addOverlays:"
+ "addSubview:"
+ "additionalDetailsLt"
+ "additionalDetailsOriginal"
+ "addressComponents"
+ "alertHash"
+ "array"
+ "arrayWithObjects:count:"
+ "attributedStringWithText:isBold:isItalic:textStyle:"
+ "beginUpdates"
+ "blackColor"
+ "boolValue"
+ "bottomAnchor"
+ "boundingMapRect"
+ "bounds"
+ "buildURLForNotificationWithAlertType:"
+ "colorWithRed:green:blue:alpha:"
+ "complete"
+ "completion"
+ "componentsJoinedByString:"
+ "constraintEqualToAnchor:"
+ "d"
+ "dataDetectorWithTypes:error:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "dealloc"
+ "displaySaLtStack:"
+ "en"
+ "endUpdates"
+ "enumerateMatchesInString:options:range:usingBlock:"
+ "extensionContext"
+ "fIsMapSnapshotLoaded"
+ "fUid"
+ "fUserTappedTsSeconds"
+ "hasCompleted"
+ "initWithCompletion:responseOption:"
+ "initWithEffectiveBundle:"
+ "initWithFrame:"
+ "initWithFrame:locationManager:"
+ "initWithPolygon:"
+ "instructionTextLt"
+ "instructionTextOriginal"
+ "isDailyLivabilityAlert"
+ "layer"
+ "leadingAnchor"
+ "locationManager"
+ "lproj"
+ "ltBody"
+ "ltByIPhone"
+ "ltStatusIcon"
+ "ltStatusStack"
+ "ltTitle"
+ "mapView"
+ "maps"
+ "maps://?address="
+ "mutableAttributedStringWithLinks:isBold:isItalic:textStyle:"
+ "mutableCopy"
+ "new"
+ "notification"
+ "objectAtIndexedSubscript:"
+ "openURL:completionHandler:"
+ "pathForResource:ofType:"
+ "phoneNumber"
+ "polygonWithCoordinates:count:"
+ "queryItemWithName:value:"
+ "range"
+ "removeFromSuperview"
+ "responseOption"
+ "resultType"
+ "saLtStack"
+ "saTapToRadar"
+ "scrollViewDidChangeAdjustedContentInset:"
+ "scrollViewDidEndDecelerating:"
+ "scrollViewDidEndDragging:willDecelerate:"
+ "scrollViewDidEndScrollingAnimation:"
+ "scrollViewDidEndZooming:withView:atScale:"
+ "scrollViewDidScroll:"
+ "scrollViewDidScrollToTop:"
+ "scrollViewDidZoom:"
+ "scrollViewShouldScrollToTop:"
+ "scrollViewWillBeginDecelerating:"
+ "scrollViewWillBeginDragging:"
+ "scrollViewWillBeginZooming:withView:"
+ "scrollViewWillEndDragging:withVelocity:targetContentOffset:"
+ "setActive:"
+ "setAdditionalDetailsLt:"
+ "setAdditionalDetailsOriginal:"
+ "setBorderColor:"
+ "setBorderWidth:"
+ "setClipsToBounds:"
+ "setCompletion:"
+ "setCornerRadius:"
+ "setDateFormat:"
+ "setDefaultEffectiveBundle:"
+ "setDelegate:"
+ "setFillColor:"
+ "setFont:"
+ "setFrame:"
+ "setHasCompleted:"
+ "setHost:"
+ "setInstructionTextLt:"
+ "setInstructionTextOriginal:"
+ "setLabel:withText:isBold:isItalic:textStyle:"
+ "setLineWidth:"
+ "setLocationManager:"
+ "setLtBody:"
+ "setLtByIPhone:"
+ "setLtStatusIcon:"
+ "setLtStatusStack:"
+ "setLtTitle:"
+ "setMapView:"
+ "setQueryItems:"
+ "setResponseOption:"
+ "setSaLtStack:"
+ "setScheme:"
+ "setShadowColor:"
+ "setShadowOffset:"
+ "setShadowOpacity:"
+ "setShadowRadius:"
+ "setShowsUserLocation:"
+ "setStrokeColor:"
+ "setTag:"
+ "setTextView:withText:isBold:isItalic:textStyle:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "setVisibleMapRect:edgePadding:"
+ "setupMapView"
+ "setupMapWithNotification:"
+ "setupViewConstraints"
+ "stringByAddingPercentEncodingWithAllowedCharacters:"
+ "stringByAppendingString:"
+ "stringFromDate:"
+ "stringWithFormat:"
+ "switchToAppleIntelligenceIcon"
+ "tag"
+ "tap-to-radar"
+ "tel://%@"
+ "textView:didBeginFormattingWithViewController:"
+ "textView:didEndFormattingWithViewController:"
+ "textView:editMenuForTextInRange:suggestedActions:"
+ "textView:editMenuForTextInRanges:suggestedActions:"
+ "textView:insertInputSuggestion:"
+ "textView:menuConfigurationForTextItem:defaultMenu:"
+ "textView:primaryActionForTextItem:defaultAction:"
+ "textView:shouldChangeTextInRange:replacementText:"
+ "textView:shouldChangeTextInRanges:replacementText:"
+ "textView:shouldInteractWithTextAttachment:inRange:"
+ "textView:shouldInteractWithTextAttachment:inRange:interaction:"
+ "textView:shouldInteractWithURL:inRange:"
+ "textView:shouldInteractWithURL:inRange:interaction:"
+ "textView:textItemMenuWillDisplayForTextItem:animator:"
+ "textView:textItemMenuWillEndForTextItem:animator:"
+ "textView:willBeginFormattingWithViewController:"
+ "textView:willDismissEditMenuWithAnimator:"
+ "textView:willEndFormattingWithViewController:"
+ "textView:willPresentEditMenuWithAnimator:"
+ "textView:writingToolsIgnoredRangesInEnclosingRange:"
+ "textViewDidBeginEditing:"
+ "textViewDidChange:"
+ "textViewDidChangeSelection:"
+ "textViewDidEndEditing:"
+ "textViewShouldBeginEditing:"
+ "textViewShouldEndEditing:"
+ "textViewWritingToolsDidEnd:"
+ "textViewWritingToolsWillBegin:"
+ "topAnchor"
+ "trailingAnchor"
+ "urlForMatch:"
+ "v12@?0B8"
+ "v24@0:8@\"UIScrollView\"16"
+ "v24@0:8@\"UITextView\"16"
+ "v24@0:8@\"_MKStaticMapView\"16"
+ "v24@0:8@?16"
+ "v24@0:8Q16"
+ "v28@0:8@\"UIScrollView\"16B24"
+ "v32@0:8@\"UIScrollView\"16@\"UIView\"24"
+ "v32@0:8@\"UITextView\"16@\"<UIEditMenuInteractionAnimating>\"24"
+ "v32@0:8@\"UITextView\"16@\"UIInputSuggestion\"24"
+ "v32@0:8@\"UITextView\"16@\"UITextFormattingViewController\"24"
+ "v32@0:8@\"_MKStaticMapView\"16@\"NSError\"24"
+ "v32@?0@\"NSTextCheckingResult\"8Q16^B24"
+ "v40@0:8@\"UIScrollView\"16@\"UIView\"24d32"
+ "v40@0:8@\"UITextView\"16@\"UITextItem\"24@\"<UIContextMenuInteractionAnimating>\"32"
+ "v40@0:8@16@24d32"
+ "v48@0:8@\"UIScrollView\"16{CGPoint=dd}24N^{CGPoint=dd}40"
+ "v48@0:8@16@24B32B36@40"
+ "v48@0:8@16{CGPoint=dd}24N^{CGPoint=dd}40"
+ "viewForZoomingInScrollView:"
+ "x-maps-emergency-alert://?alert-id=%@&is-lt=0"
+ "yyyy.MM.dd_HH-mm-ss"
+ "{\"msg%{public}.0s\":\"#saGeneralNotif,mapSnapshotFailed\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotif,mapSnapshotLoaded\"}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotif,rendererForOverlay\"}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotif,setupMapView,created _MKStaticMapView\"}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotif,setupMapView,failedToCreate_MKStaticMapView\"}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotif,setupMapWithNotification,overlays\", \"count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotificationExtension,invalidGeometry\"}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotificationExtension,mutableAttributedStringWithLinks,dataDetectorInitFailed\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotificationExtension,mutableAttributedStringWithLinks,detectedURL\", \"url\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotificationExtension,mutableAttributedStringWithLinks,result\", \"attrString\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotificationExtension,openURL\", \"url\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saGeneralNotificationExtension,openURL,result\", \"url\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#tapToRadar,#warning,buildURLForNotification,alertTypeNone,defaultingToIT\"}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
- "#saGeneralNotificationExtension,processMapImageInfo,about to request snapshot with options:%{public}@, snapshot:%{public}@"
- "#saGeneralNotificationExtension,processMapImageInfo,centroidInvalid"
- "#saGeneralNotificationExtension,processMapImageInfo,noGeometry"
- "#saGeneralNotificationExtension,processMapImageInfo,regionSpan:%{public}f"
- "#saGeneralNotificationExtension,processMapImageInfo,snapshotCallback,mapOverlayImage has been set to mapImageView"
- "#saGeneralNotificationExtension,processMapImageInfo,snapshotCallback,snapshot:%{public}@, error:%{public}@"
- "#saGeneralNotificationExtension,processMapImageInfo,usingGeometryCentroid, lat:%f, lon:%f"
- "#saGeneralNotificationExtension,processMapImageInfo,valid polygons with number of polygons:%{public}lu"
- "<"
- "@\"MKAnnotationView\"32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "@\"MKClusterAnnotation\"32@0:8@\"MKMapView\"16@\"NSArray\"24"
- "@\"MKOverlayRenderer\"32@0:8@\"MKMapView\"16@\"<MKOverlay>\"24"
- "@\"MKOverlayView\"32@0:8@\"MKMapView\"16@\"<MKOverlay>\"24"
- "@\"MKSelectionAccessory\"32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "@36@0:8@16B24@28"
- "CGContext"
- "MKMapViewDelegate"
- "T@\"UIImageView\",W,N,V_mapImageView"
- "_mapImageView"
- "_setUseSnapshotService:"
- "attachments"
- "attributedStringWithText:isBold:textStyle:"
- "colorWithCGColor:"
- "drawAtPoint:"
- "drawAtPoint:withAttributes:"
- "getRed:green:blue:alpha:"
- "image"
- "initWithOptions:"
- "mapImageView"
- "mapView:annotationView:calloutAccessoryControlTapped:"
- "mapView:annotationView:didChangeDragState:fromOldState:"
- "mapView:clusterAnnotationForMemberAnnotations:"
- "mapView:didAddAnnotationViews:"
- "mapView:didAddOverlayRenderers:"
- "mapView:didAddOverlayViews:"
- "mapView:didChangeUserTrackingMode:animated:"
- "mapView:didDeselectAnnotation:"
- "mapView:didDeselectAnnotationView:"
- "mapView:didFailToLocateUserWithError:"
- "mapView:didSelectAnnotation:"
- "mapView:didSelectAnnotationView:"
- "mapView:didUpdateUserLocation:"
- "mapView:regionDidChangeAnimated:"
- "mapView:regionWillChangeAnimated:"
- "mapView:selectionAccessoryForAnnotation:"
- "mapView:viewForOverlay:"
- "mapViewDidChangeVisibleRegion:"
- "mapViewDidFinishRenderingMap:fullyRendered:"
- "mapViewDidStopLocatingUser:"
- "mapViewWillStartLocatingUser:"
- "mapViewWillStartRenderingMap:"
- "pointForCoordinate:"
- "processMapImageInfo:"
- "renderLegendBgWithContext:color:topLeftX:topLeftY:width:height:"
- "setFill"
- "setLabel:withText:isBold:textStyle:"
- "setMapImageView:"
- "setMapType:"
- "setSize:"
- "setStroke"
- "setTextView:withText:isBold:textStyle:"
- "setTraitCollection:"
- "startWithCompletionHandler:"
- "traitCollectionWithUserInterfaceStyle:"
- "userLat"
- "userLon"
- "v24@0:8@\"MKMapView\"16"
- "v24@?0@\"MKMapSnapshot\"8@\"NSError\"16"
- "v28@0:8@\"MKMapView\"16B24"
- "v32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "v32@0:8@\"MKMapView\"16@\"MKAnnotationView\"24"
- "v32@0:8@\"MKMapView\"16@\"MKUserLocation\"24"
- "v32@0:8@\"MKMapView\"16@\"NSArray\"24"
- "v32@0:8@\"MKMapView\"16@\"NSError\"24"
- "v36@0:8@\"MKMapView\"16q24B32"
- "v36@0:8@16q24B32"
- "v40@0:8@\"MKMapView\"16@\"MKAnnotationView\"24@\"UIControl\"32"
- "v44@0:8@16@24B32@36"
- "v48@0:8@\"MKMapView\"16@\"MKAnnotationView\"24Q32Q40"
- "v48@0:8@16@24Q32Q40"
- "v64@0:8^{CGContext=}16^{CGColor=}24d32d40d48d56"
- "{\"msg%{public}.0s\":\"#saGeneralNotif,#warning,getSystemRedFailed\"}"
- "{\"msg%{public}.0s\":\"#saGeneralNotif,objects\", \"options\":%{private, location:escape_only}@, \"snapshot\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saGeneralNotif,snapshotCallback\", \"snapshot\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#saGeneralNotif,snapshotCallback,geometry,currentLocation\", \"lat\":\"%{sensitive}0.2f\", \"lon\":\"%{sensitive}0.2f\", \"x\":\"%{sensitive}0.1f\", \"y\":\"%{sensitive}0.1f\"}"

```
