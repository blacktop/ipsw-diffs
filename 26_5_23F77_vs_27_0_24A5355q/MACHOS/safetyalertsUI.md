## safetyalertsUI

> `/System/Library/PrivateFrameworks/SafetyAlerts.framework/PlugIns/safetyalertsUI.appex/safetyalertsUI`

```diff

-67.0.4.0.0
-  __TEXT.__text: 0x2e78
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x680
-  __TEXT.__objc_methlist: 0x364
-  __TEXT.__const: 0x3fb
-  __TEXT.__gcc_except_tab: 0x404
-  __TEXT.__cstring: 0x1c6
-  __TEXT.__oslogstring: 0x50f
-  __TEXT.__objc_methname: 0xb15
-  __TEXT.__objc_classname: 0x57
-  __TEXT.__objc_methtype: 0x4b9
-  __TEXT.__unwind_info: 0x190
-  __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x280
-  __DATA_CONST.__cfstring: 0x240
-  __DATA_CONST.__objc_classlist: 0x8
+70.0.15.0.0
+  __TEXT.__text: 0x402c
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x3a4
+  __TEXT.__const: 0xe8
+  __TEXT.__gcc_except_tab: 0x938
+  __TEXT.__objc_methname: 0xd8d
+  __TEXT.__objc_classname: 0x8a
+  __TEXT.__objc_methtype: 0x3e8
+  __TEXT.__cstring: 0x3b6
+  __TEXT.__oslogstring: 0xb15
+  __TEXT.__unwind_info: 0x1b8
+  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__cfstring: 0x5a0
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x450
-  __DATA.__objc_selrefs: 0x390
-  __DATA.__objc_ivar: 0x10
-  __DATA.__objc_data: 0x50
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x108
+  __DATA.__objc_const: 0x6e0
+  __DATA.__objc_selrefs: 0x528
+  __DATA.__objc_ivar: 0x34
+  __DATA.__objc_data: 0x140
   __DATA.__data: 0x120
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B54172AA-93EC-3D69-8732-1E4AC127E752
-  Functions: 73
-  Symbols:   103
-  CStrings:  231
+  UUID: A66C601C-368D-3E13-BE7E-3AE41549618D
+  Functions: 58
+  Symbols:   126
+  CStrings:  376
 
Symbols:
+ _CGContextAddLineToPoint
+ _CGContextClip
+ _CGContextMoveToPoint
+ _CGContextRestoreGState
+ _CGContextSaveGState
+ _CGContextStrokePath
+ _CGPathCreateWithEllipseInRect
+ _CGPathRelease
+ _CGRectZero
+ _MKMapPointForCoordinate
+ _MKMapPointsPerMeterAtLatitude
+ _OBJC_CLASS_$_CLLocationManager
+ _OBJC_CLASS_$_CompletionGuard
+ _OBJC_CLASS_$_MKCircle
+ _OBJC_CLASS_$_MKCircleRenderer
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSLayoutConstraint
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_CLASS_$_NSURLQueryItem
+ _OBJC_CLASS_$_SACircleRenderer
+ _OBJC_CLASS_$_SATapToRadar
+ _OBJC_CLASS_$_UILabel
+ _OBJC_CLASS_$_UIStackView
+ _OBJC_CLASS_$_UIView
+ _OBJC_CLASS_$__MKStaticMapView
+ _OBJC_METACLASS_$_CompletionGuard
+ _OBJC_METACLASS_$_MKCircleRenderer
+ _OBJC_METACLASS_$_SACircleRenderer
+ _OBJC_METACLASS_$_SATapToRadar
+ __dispatch_main_q
+ __os_log_default
+ __os_log_error_impl
+ _dispatch_async
+ _objc_claimAutoreleasedReturnValue
+ _objc_copyWeak
+ _objc_enumerationMutation
+ _objc_initWeak
+ _objc_release
+ _objc_release_x25
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
+ _objc_storeStrong
- _CFRelease
- _CGColorCreateGenericRGB
- _CGContextFillEllipseInRect
- _CGContextFillPath
- _CGContextStrokeEllipseInRect
- _CGContextStrokeLineSegments
- _CGPathCreateWithRoundedRect
- _CGPointZero
- _NSFontAttributeName
- _NSForegroundColorAttributeName
- _NSLog
- _OBJC_CLASS_$_MKMapSnapshotOptions
- _OBJC_CLASS_$_MKMapSnapshotter
- _OBJC_CLASS_$_NSDictionary
- _OBJC_CLASS_$_UIGraphicsImageRenderer
- _OBJC_CLASS_$_UITraitCollection
- __ZN16SACircleRenderer10drawCircleEdddP7CGColorS1_b
- __ZNSt20bad_array_new_lengthC1Ev
- __ZNSt20bad_array_new_lengthD1Ev
- __ZNSt3__117bad_function_callD1Ev
- __ZTINSt3__117bad_function_callE
- __ZTISt20bad_array_new_length
- __ZTVN10__cxxabiv117__class_type_infoE
- __ZTVN10__cxxabiv120__si_class_type_infoE
- __ZTVNSt3__117bad_function_callE
- __ZdlPvSt19__type_descriptor_t
- _memcpy
- _objc_retainAutoreleasedReturnValue
- _strcmp
CStrings:
+ "#saIgneousNotificationExtension,CompletionGuard auto-completing"
+ "#saIgneousNotificationExtension,didReceiveNotification"
+ "#saIgneousNotificationExtension,didReceiveNotification,endUpdates,awaitingDelegate"
+ "#saIgneousNotificationExtension,didReceiveNotification,invalidCoordinates,returning"
+ "#saIgneousNotificationExtension,didReceiveNotification,missingAlertLevel"
+ "#saIgneousNotificationExtension,didReceiveNotification,overlayCount:%d"
+ "#saIgneousNotificationExtension,didReceiveNotification,payload,epiLat:%{sensitive}f,epiLon:%{sensitive}f,regionSpan:%{private}f,eqRadius:%{private}f,strongShaking:%d,epicenter:%d,shaded:%d,alertLevel:%d"
+ "#saIgneousNotificationExtension,didReceiveNotificationResponse,Failed to open Maps app with alert hash: %@"
+ "#saIgneousNotificationExtension,didReceiveNotificationResponse,Missing alert hash."
+ "#saIgneousNotificationExtension,didReceiveNotificationResponse,Successfully opened Maps app with alert hash: %@"
+ "#saIgneousNotificationExtension,didReceiveNotificationResponse,User tapped 'Open in Maps' action"
+ "#saIgneousNotificationExtension,didReceiveNotificationResponse,User tapped 'Tap To Radar' action"
+ "#saIgneousNotificationExtension,didReceiveNotificationResponse,action identifier: %@"
+ "#saIgneousNotificationExtension,didReceiveNotificationResponse,alertHash: %@"
+ "#saIgneousNotificationExtension,didReceiveNotificationResponse,nil URL"
+ "#saIgneousNotificationExtension,didReceiveNotificationResponse,unsupported action identifier:%@"
+ "#saIgneousNotificationExtension,mapViewDidFailLoadingMap,error:%{public}@"
+ "#saIgneousNotificationExtension,mapViewDidFinishLoadingMap"
+ "#saIgneousNotificationExtension,rendererForOverlay,title:%{public}@"
+ "#saIgneousNotificationExtension,setupMapView,created _MKStaticMapView"
+ "#saIgneousNotificationExtension,tapToRadar,failed"
+ "#saIgneousNotificationExtension,tapToRadar,launched"
+ "#saIgneousNotificationExtension,tapToRadar,nil URL"
+ ".cxx_construct"
+ "/System/Library/LocationBundles/SafetyAlerts.bundle"
+ "/System/Library/UserNotifications/Bundles/com.apple.safetyalerts.gen.bundle"
+ "1979088"
+ "2280104"
+ "@\"CLLocationManager\""
+ "@\"MKAnnotationView\"32@0:8@\"_MKStaticMapView\"16@\"<MKAnnotation>\"24"
+ "@\"MKOverlayRenderer\"32@0:8@\"_MKStaticMapView\"16@\"<MKOverlay>\"24"
+ "@\"_MKStaticMapView\""
+ "@20@0:8i16"
+ "@32@0:8@?16Q24"
+ "@?"
+ "@?16@0:8"
+ "B"
+ "CompletionGuard"
+ "ComponentID"
+ "ComponentName"
+ "ComponentVersion"
+ "Description"
+ "Keywords"
+ "Liveon"
+ "Please attach screen shots and provide a brief description of the issue faced."
+ "Q"
+ "SACircleRenderer"
+ "SAFETY_ALERTS_EARTHQUAKE_AREA_POTENTIAL_SHAKING"
+ "SAFETY_ALERTS_TAP_TO_RADAR_ACTION_TITLE"
+ "SATapToRadar"
+ "Safety Alerts"
+ "T@\"CLLocationManager\",&,N,V_locationManager"
+ "T@\"_MKStaticMapView\",&,N,V_mapView"
+ "T@?,C,N,V_completion"
+ "TB,N,V_shaded"
+ "TB,V_hasCompleted"
+ "TQ,N,V_responseOption"
+ "TimeOfIssue"
+ "Title"
+ "URL"
+ "URLWithString:"
+ "[ESA][Liveon][EQ]"
+ "[ESA][Liveon][IT]"
+ "_MKStaticMapViewDelegate"
+ "_completion"
+ "_hasCompleted"
+ "_locationManager"
+ "_mapView"
+ "_responseOption"
+ "_shaded"
+ "actionIdentifier"
+ "actionTitle"
+ "activateConstraints:"
+ "addArrangedSubview:"
+ "addLegendToMapView:showStrongShaking:isAwareness:"
+ "addObject:"
+ "addOverlays:"
+ "addSubview:"
+ "alertHash"
+ "array"
+ "arrayWithObjects:count:"
+ "beginUpdates"
+ "blackColor"
+ "bottomAnchor"
+ "buildURLForNotificationWithAlertType:"
+ "c"
+ "centerYAnchor"
+ "circle"
+ "circleWithCenterCoordinate:radius:"
+ "colorWithRed:green:blue:alpha:"
+ "complete"
+ "completion"
+ "constraintEqualToAnchor:"
+ "constraintEqualToAnchor:constant:"
+ "constraintEqualToConstant:"
+ "coordinate"
+ "count"
+ "countByEnumeratingWithState:objects:count:"
+ "d"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "dealloc"
+ "displayMapViewHolder:"
+ "drawMapRect:zoomScale:inContext:"
+ "en"
+ "endUpdates"
+ "epicenter"
+ "extensionContext"
+ "fIsMapSnapshotLoaded"
+ "fIsStrongShakingAreaLineShaded"
+ "fUid"
+ "fUserTappedTsSeconds"
+ "hasCompleted"
+ "heightAnchor"
+ "init"
+ "initWithCircle:"
+ "initWithCompletion:responseOption:"
+ "initWithEffectiveBundle:"
+ "initWithFrame:locationManager:"
+ "isEqualToString:"
+ "layer"
+ "layoutIfNeeded"
+ "leadingAnchor"
+ "length"
+ "level"
+ "locationManager"
+ "lproj"
+ "mapView"
+ "maps"
+ "new"
+ "notification"
+ "objectForKeyedSubscript:"
+ "openURL:completionHandler:"
+ "pathForResource:ofType:"
+ "pointForMapPoint:"
+ "queryItemWithName:value:"
+ "radius"
+ "removeFromSuperview"
+ "responseOption"
+ "saTapToRadar"
+ "safetyAlertsSettings"
+ "setActive:"
+ "setAlignment:"
+ "setAxis:"
+ "setBackgroundColor:"
+ "setCompletion:"
+ "setCornerRadius:"
+ "setDateFormat:"
+ "setDefaultEffectiveBundle:"
+ "setDelegate:"
+ "setFillColor:"
+ "setFont:"
+ "setHasCompleted:"
+ "setHidden:"
+ "setHost:"
+ "setLineWidth:"
+ "setLocationManager:"
+ "setMapView:"
+ "setMasksToBounds:"
+ "setQueryItems:"
+ "setResponseOption:"
+ "setScheme:"
+ "setShaded:"
+ "setShowsUserLocation:"
+ "setSpacing:"
+ "setStrokeColor:"
+ "setTag:"
+ "setTextColor:"
+ "setTitle:"
+ "setTranslatesAutoresizingMaskIntoConstraints:"
+ "setupMapView"
+ "shaded"
+ "stringFromDate:"
+ "stringWithFormat:"
+ "strongShaking"
+ "tap-to-radar"
+ "title"
+ "topAnchor"
+ "trailingAnchor"
+ "v12@?0B8"
+ "v20@0:8B16"
+ "v24@0:8@\"_MKStaticMapView\"16"
+ "v24@0:8@?16"
+ "v24@0:8Q16"
+ "v28@0:8B16B20B24"
+ "v32@0:8@\"_MKStaticMapView\"16@\"NSError\"24"
+ "v64@0:8{?={?=dd}{?=dd}}16d48^{CGContext=}56"
+ "v8@?0"
+ "view"
+ "viewWithTag:"
+ "whiteColor"
+ "widthAnchor"
+ "x-maps-emergency-alert://?alert-id=%@"
+ "yyyy.MM.dd_HH-mm-ss"
+ "{\"msg%{public}.0s\":\"#saIgneousNotif,didReceiveNotification,overlays\", \"count\":%{private}d}"
+ "{\"msg%{public}.0s\":\"#saIgneousNotif,mapViewDidFailLoadingMap\", \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#saIgneousNotif,mapViewDidFinishLoadingMap\"}"
+ "{\"msg%{public}.0s\":\"#saIgneousNotif,setupMapView,created _MKStaticMapView\"}"
+ "{\"msg%{public}.0s\":\"#saIgneousNotif,setupMapView,failedToCreate_MKStaticMapView\"}"
+ "{\"msg%{public}.0s\":\"#tapToRadar,#warning,buildURLForNotification,alertTypeNone,defaultingToIT\"}"
+ "{basic_string<char, std::char_traits<char>, std::allocator<char>>=\"\"{?=\"__rep_\"(__rep=\"__s\"{__short=\"__data_\"[23c]\"__size_\"b7\"__is_long_\"b1}\"__l\"{__long=\"__data_\"*\"__size_\"Q\"__cap_\"b63\"__is_long_\"b1})}}"
+ "\x92"
- "#notif,snapshotCallback,getLegendFont"
- "@\"MKAnnotationView\"32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "@\"MKClusterAnnotation\"32@0:8@\"MKMapView\"16@\"NSArray\"24"
- "@\"MKOverlayRenderer\"32@0:8@\"MKMapView\"16@\"<MKOverlay>\"24"
- "@\"MKOverlayView\"32@0:8@\"MKMapView\"16@\"<MKOverlay>\"24"
- "@\"MKSelectionAccessory\"32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "@\"UIImageView\""
- "CGContext"
- "MKMapViewDelegate"
- "T@\"UIImageView\",W,N,V_mapImageView"
- "_mapImageView"
- "_setUseSnapshotService:"
- "attachments"
- "colorWithCGColor:"
- "dictionaryWithObjects:forKeys:count:"
- "drawAtPoint:"
- "drawAtPoint:withAttributes:"
- "getRed:green:blue:alpha:"
- "image"
- "imageWithActions:"
- "initWithOptions:"
- "initWithSize:"
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
- "renderLegendBgWithContext:color:topLeftX:topLeftY:width:height:"
- "setFill"
- "setImage:"
- "setMapImageView:"
- "setMapType:"
- "setSize:"
- "setStroke"
- "setTraitCollection:"
- "sizeWithAttributes:"
- "startWithCompletionHandler:"
- "traitCollectionWithUserInterfaceStyle:"
- "userLat"
- "userLon"
- "v16@?0@\"UIGraphicsImageRendererContext\"8"
- "v24@0:8@\"MKMapView\"16"
- "v24@?0@\"MKMapSnapshot\"8@\"NSError\"16"
- "v28@0:8@\"MKMapView\"16B24"
- "v28@0:8@16B24"
- "v32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
- "v32@0:8@\"MKMapView\"16@\"MKAnnotationView\"24"
- "v32@0:8@\"MKMapView\"16@\"MKUserLocation\"24"
- "v32@0:8@\"MKMapView\"16@\"NSArray\"24"
- "v32@0:8@\"MKMapView\"16@\"NSError\"24"
- "v36@0:8@\"MKMapView\"16q24B32"
- "v36@0:8@16q24B32"
- "v40@0:8@\"MKMapView\"16@\"MKAnnotationView\"24@\"UIControl\"32"
- "v40@0:8@16@24@32"
- "v48@0:8@\"MKMapView\"16@\"MKAnnotationView\"24Q32Q40"
- "v48@0:8@16@24Q32Q40"
- "v64@0:8^{CGContext=}16^{CGColor=}24d32d40d48d56"
- "vector"
- "{\"msg%{public}.0s\":\"#notif,#warning,getSystemRedFailed\"}"
- "{\"msg%{public}.0s\":\"#notif,objects\", \"options\":%{private, location:escape_only}@, \"snapshot\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#notif,snapshotCallback\", \"snapshot\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@}"
- "{\"msg%{public}.0s\":\"#notif,snapshotCallback,geometry,center\", \"epiLat\":\"%{private}0.2f\", \"epiLon\":\"%{private}0.2f\", \"x\":\"%{private}0.1f\", \"y\":\"%{sensitive}0.1f\"}"
- "{\"msg%{public}.0s\":\"#notif,snapshotCallback,geometry,currentLocation\", \"lat\":\"%{sensitive}0.2f\", \"lon\":\"%{sensitive}0.2f\", \"x\":\"%{sensitive}0.1f\", \"y\":\"%{sensitive}0.1f\"}"
- "{\"msg%{public}.0s\":\"#notif,snapshotCallback,geometry,quadrant\", \"epiLat\":\"%{private}0.2f\", \"epiLon\":\"%{private}0.2f\", \"eqRadius\":\"%{private}0.1f\", \"spanLat\":\"%{private}0.1f\", \"spanLon\":\"%{private}0.1f\"}"

```
