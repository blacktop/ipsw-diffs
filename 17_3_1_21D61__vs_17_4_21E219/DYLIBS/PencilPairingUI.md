## PencilPairingUI

> `/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`

```diff

-132.6.0.0.0
-  __TEXT.__text: 0x19f78
-  __TEXT.__auth_stubs: 0x570
-  __TEXT.__objc_methlist: 0x244c
+136.4.4.0.0
+  __TEXT.__text: 0x1af98
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_methlist: 0x263c
   __TEXT.__const: 0x210
-  __TEXT.__cstring: 0xa3b
-  __TEXT.__gcc_except_tab: 0x150
-  __TEXT.__unwind_info: 0x934
-  __TEXT.__objc_classname: 0x757
-  __TEXT.__objc_methname: 0x70d0
-  __TEXT.__objc_methtype: 0x1761
-  __TEXT.__objc_stubs: 0x5ee0
+  __TEXT.__cstring: 0xb0f
+  __TEXT.__gcc_except_tab: 0x17c
+  __TEXT.__unwind_info: 0x980
+  __TEXT.__objc_classname: 0x7b7
+  __TEXT.__objc_methname: 0x7d40
+  __TEXT.__objc_methtype: 0x1ef4
+  __TEXT.__objc_stubs: 0x6180
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x5d8
-  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__const: 0x630
+  __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x8410
-  __DATA_CONST.__objc_selrefs: 0x1b28
-  __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__objc_const: 0x1088
-  __AUTH_CONST.__cfstring: 0x12a0
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __DATA_CONST.__objc_const: 0x8fb0
+  __DATA_CONST.__objc_selrefs: 0x1c28
+  __DATA_CONST.__objc_classrefs: 0x320
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_arraydata: 0xc0
+  __AUTH_CONST.__objc_const: 0x1118
+  __AUTH_CONST.__cfstring: 0x1400
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__objc_intobj: 0x1b0
-  __AUTH_CONST.__auth_got: 0x2c8
-  __AUTH.__objc_data: 0xd20
-  __DATA.__objc_classrefs: 0x308
-  __DATA.__objc_superrefs: 0xe0
-  __DATA.__objc_ivar: 0x370
-  __DATA.__data: 0x9d0
+  __AUTH_CONST.__objc_intobj: 0x210
+  __AUTH_CONST.__auth_got: 0x2d0
+  __AUTH.__objc_data: 0xd70
+  __DATA.__objc_ivar: 0x38c
+  __DATA.__data: 0xaf0
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/PencilKit.framework/PencilKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 851
-  Symbols:   3526
-  CStrings:  1702
+  Functions: 898
+  Symbols:   3683
+  CStrings:  1863
 
Symbols:
+ +[PNPFindMyController _controllerWithType:buttonType:deviceType:delegate:]
+ -[PNPDeviceState identifier]
+ -[PNPDeviceState setIdentifier:]
+ -[PNPFeatureListController configureFor222]
+ -[PNPFeatureListController configureFor332]
+ -[PNPFeatureListController configureFor482]
+ -[PNPFeatureListController configureForGeneric]
+ -[PNPFeatureListController configureForType:]
+ -[PNPFeatureListController tempDoTheNormalThing]
+ -[PNPFindMyController .cxx_destruct]
+ -[PNPFindMyController mapView]
+ -[PNPFindMyController setMapView:]
+ -[PNPFindMyController viewDidLoad]
+ -[PNPWhatsNewController configureFor222]
+ -[PNPWhatsNewController configureFor332]
+ -[PNPWhatsNewController configureFor482]
+ -[PNPWhatsNewController configureForGeneric]
+ -[PNPWhatsNewController configureForType:]
+ -[PNPWhatsNewController tempDoTheNormalThing]
+ -[PNPWizardViewController controllerForType:buttonType:]
+ -[PNPWizardViewController controllerIndex]
+ -[PNPWizardViewController controllerQueue]
+ -[PNPWizardViewController createControllerPlanForDeviceType:isWhatsNew:]
+ -[PNPWizardViewController deviceState]
+ -[PNPWizardViewController didCompleteAccessoryOnboarding:pairingSuccessful:]
+ -[PNPWizardViewController findMyCoordinator]
+ -[PNPWizardViewController fullEducationControllerQueueForType:]
+ -[PNPWizardViewController hasScribbleKeyboard]
+ -[PNPWizardViewController navigationController:willShowViewController:animated:]
+ -[PNPWizardViewController processNextController]
+ -[PNPWizardViewController setControllerIndex:]
+ -[PNPWizardViewController setControllerQueue:]
+ -[PNPWizardViewController setDeviceState:]
+ -[PNPWizardViewController setFindMyCoordinator:]
+ -[PNPWizardViewController setHasScribbleKeyboard:]
+ -[PNPWizardViewController showFindMyController]
+ -[PNPWizardViewController whatsNewControllerQueueForType:]
+ -[PencilSettingsStatisticsManager recordHoverDoubleTap:]
+ -[PencilSettingsStatisticsManager recordHoverPreview:]
+ -[PencilSettingsStatisticsManager recordHoverShadow:]
+ _NSLog
+ _OBJC_CLASS_$_MKMapView
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_PNPFindMyController
+ _OBJC_IVAR_$_PNPDeviceState._identifier
+ _OBJC_IVAR_$_PNPFindMyController._mapView
+ _OBJC_IVAR_$_PNPWizardViewController._controllerIndex
+ _OBJC_IVAR_$_PNPWizardViewController._controllerQueue
+ _OBJC_IVAR_$_PNPWizardViewController._deviceState
+ _OBJC_IVAR_$_PNPWizardViewController._findMyCoordinator
+ _OBJC_IVAR_$_PNPWizardViewController._hasScribbleKeyboard
+ _OBJC_METACLASS_$_PNPFindMyController
+ __OBJC_$_CLASS_METHODS_PNPFindMyController
+ __OBJC_$_INSTANCE_METHODS_PNPFindMyController
+ __OBJC_$_INSTANCE_VARIABLES_PNPFindMyController
+ __OBJC_$_PROP_LIST_PNPFindMyController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_MKMapViewDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_UINavigationControllerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PNPWizardViewDelegatePrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MKMapViewDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_UINavigationControllerDelegate
+ __OBJC_$_PROTOCOL_REFS_CLLocationManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_MKMapViewDelegate
+ __OBJC_$_PROTOCOL_REFS_UINavigationControllerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_PNPFindMyController
+ __OBJC_CLASS_RO_$_PNPFindMyController
+ __OBJC_LABEL_PROTOCOL_$_CLLocationManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_MKMapViewDelegate
+ __OBJC_LABEL_PROTOCOL_$_UINavigationControllerDelegate
+ __OBJC_METACLASS_RO_$_PNPFindMyController
+ __OBJC_PROTOCOL_$_CLLocationManagerDelegate
+ __OBJC_PROTOCOL_$_MKMapViewDelegate
+ __OBJC_PROTOCOL_$_UINavigationControllerDelegate
+ ___48-[PNPWizardViewController processNextController]_block_invoke
+ ___53-[PencilSettingsStatisticsManager recordHoverShadow:]_block_invoke
+ ___54-[PencilSettingsStatisticsManager recordHoverPreview:]_block_invoke
+ ___56-[PencilSettingsStatisticsManager recordHoverDoubleTap:]_block_invoke
+ ___61-[_PNPPencilMovieView completeRevolutionWithCompletionBlock:]_block_invoke_2
+ ___block_descriptor_52_e8_32bs40r_e5_v8?0lr40l8s32l8
+ __unnamed_array_storage.20
+ __unnamed_array_storage.25
+ _objc_msgSend$UUID
+ _objc_msgSend$asset
+ _objc_msgSend$configureFor222
+ _objc_msgSend$configureFor332
+ _objc_msgSend$configureFor482
+ _objc_msgSend$configureForGeneric
+ _objc_msgSend$configureForType:
+ _objc_msgSend$controllerIndex
+ _objc_msgSend$controllerQueue
+ _objc_msgSend$createControllerPlanForDeviceType:isWhatsNew:
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$fullEducationControllerQueueForType:
+ _objc_msgSend$hasScribbleKeyboard
+ _objc_msgSend$loadValuesAsynchronouslyForKeys:completionHandler:
+ _objc_msgSend$numberWithInteger:
+ _objc_msgSend$processNextController
+ _objc_msgSend$setControllerIndex:
+ _objc_msgSend$setControllerQueue:
+ _objc_msgSend$setFindMyCoordinator:
+ _objc_msgSend$setHasScribbleKeyboard:
+ _objc_msgSend$setIdentifier:
+ _objc_msgSend$setMapView:
+ _objc_msgSend$tempDoTheNormalThing
+ _objc_msgSend$whatsNewControllerQueueForType:
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_PNPWizardViewDelegatePrivate
- ___49-[PNPWizardViewController prepareForPresentation]_block_invoke
- _objc_msgSend$decodeObjectForKey:
- _objc_msgSend$showingWhatsNew
- _objc_msgSend$welcomeControllerWithType:buttonType:deviceType:
CStrings:
+ "\x11#\x11"
+ "@\"<UIViewControllerAnimatedTransitioning>\"48@0:8@\"UINavigationController\"16q24@\"UIViewController\"32@\"UIViewController\"40"
+ "@\"<UIViewControllerInteractiveTransitioning>\"32@0:8@\"UINavigationController\"16@\"<UIViewControllerAnimatedTransitioning>\"24"
+ "@\"FMUIAccessoryOnboardingCoordinator\""
+ "@\"MKAnnotationView\"32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
+ "@\"MKClusterAnnotation\"32@0:8@\"MKMapView\"16@\"NSArray\"24"
+ "@\"MKMapView\""
+ "@\"MKOverlayRenderer\"32@0:8@\"MKMapView\"16@\"<MKOverlay>\"24"
+ "@\"MKOverlayView\"32@0:8@\"MKMapView\"16@\"<MKOverlay>\"24"
+ "@\"NSUUID\""
+ "@28@0:8q16B24"
+ "@32@0:8q16q24"
+ "@48@0:8@16q24@32@40"
+ "B24@0:8@\"CLLocationManager\"16"
+ "CLLocationManagerDelegate"
+ "FIND_MY_DESCRIPTION"
+ "FIND_MY_TITLE"
+ "HoverDoubleTapToggle"
+ "HoverDoubleTapValue"
+ "HoverPreviewToggle"
+ "HoverPreviewValue"
+ "HoverShadowToggle"
+ "HoverShadowValue"
+ "MKMapViewDelegate"
+ "PNPFindMyController"
+ "Q24@0:8@\"UINavigationController\"16"
+ "Q24@0:8@16"
+ "Still pencil uuid, using a random UUID"
+ "T@\"FMUIAccessoryOnboardingCoordinator\",&,N,V_findMyCoordinator"
+ "T@\"MKMapView\",&,N,V_mapView"
+ "T@\"NSArray\",&,N,V_controllerQueue"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSUUID\",C,N,V_identifier"
+ "T@\"PNPDeviceState\",&,N,V_deviceState"
+ "TB,N,V_hasScribbleKeyboard"
+ "Td,?,R,N"
+ "Tq,N,V_controllerIndex"
+ "UINavigationControllerDelegate"
+ "UUID"
+ "_controllerIndex"
+ "_controllerQueue"
+ "_findMyCoordinator"
+ "_hasScribbleKeyboard"
+ "_identifier"
+ "_mapView"
+ "asset"
+ "configureFor222"
+ "configureFor332"
+ "configureFor482"
+ "configureForGeneric"
+ "configureForType:"
+ "controllerForType:buttonType:"
+ "controllerIndex"
+ "controllerQueue"
+ "createControllerPlanForDeviceType:isWhatsNew:"
+ "decodeObjectOfClass:forKey:"
+ "didCompleteAccessoryOnboarding:pairingSuccessful:"
+ "findMyCoordinator"
+ "fullEducationControllerQueueForType:"
+ "hasScribbleKeyboard"
+ "loadValuesAsynchronouslyForKeys:completionHandler:"
+ "locationManager:didChangeAuthorizationStatus:"
+ "locationManager:didDetermineState:forRegion:"
+ "locationManager:didEnterRegion:"
+ "locationManager:didExitRegion:"
+ "locationManager:didFailRangingBeaconsForConstraint:error:"
+ "locationManager:didFailWithError:"
+ "locationManager:didFinishDeferredUpdatesWithError:"
+ "locationManager:didRangeBeacons:inRegion:"
+ "locationManager:didRangeBeacons:satisfyingConstraint:"
+ "locationManager:didStartMonitoringForRegion:"
+ "locationManager:didUpdateHeading:"
+ "locationManager:didUpdateLocations:"
+ "locationManager:didUpdateToLocation:fromLocation:"
+ "locationManager:didVisit:"
+ "locationManager:monitoringDidFailForRegion:withError:"
+ "locationManager:rangingBeaconsDidFailForRegion:withError:"
+ "locationManagerDidChangeAuthorization:"
+ "locationManagerDidPauseLocationUpdates:"
+ "locationManagerDidResumeLocationUpdates:"
+ "locationManagerShouldDisplayHeadingCalibration:"
+ "mapView"
+ "mapView:annotationView:calloutAccessoryControlTapped:"
+ "mapView:annotationView:didChangeDragState:fromOldState:"
+ "mapView:clusterAnnotationForMemberAnnotations:"
+ "mapView:didAddAnnotationViews:"
+ "mapView:didAddOverlayRenderers:"
+ "mapView:didAddOverlayViews:"
+ "mapView:didChangeUserTrackingMode:animated:"
+ "mapView:didDeselectAnnotation:"
+ "mapView:didDeselectAnnotationView:"
+ "mapView:didFailToLocateUserWithError:"
+ "mapView:didSelectAnnotation:"
+ "mapView:didSelectAnnotationView:"
+ "mapView:didUpdateUserLocation:"
+ "mapView:regionDidChangeAnimated:"
+ "mapView:regionWillChangeAnimated:"
+ "mapView:rendererForOverlay:"
+ "mapView:viewForAnnotation:"
+ "mapView:viewForOverlay:"
+ "mapViewDidChangeVisibleRegion:"
+ "mapViewDidFailLoadingMap:withError:"
+ "mapViewDidFinishLoadingMap:"
+ "mapViewDidFinishRenderingMap:fullyRendered:"
+ "mapViewDidStopLocatingUser:"
+ "mapViewWillStartLoadingMap:"
+ "mapViewWillStartLocatingUser:"
+ "mapViewWillStartRenderingMap:"
+ "navigationController:animationControllerForOperation:fromViewController:toViewController:"
+ "navigationController:didShowViewController:animated:"
+ "navigationController:interactionControllerForAnimationController:"
+ "navigationController:willShowViewController:animated:"
+ "navigationControllerPreferredInterfaceOrientationForPresentation:"
+ "navigationControllerSupportedInterfaceOrientations:"
+ "numberWithInteger:"
+ "pencilUUID: %@"
+ "processNextController"
+ "q24@0:8@\"UINavigationController\"16"
+ "q24@0:8@16"
+ "recordHoverDoubleTap:"
+ "recordHoverPreview:"
+ "recordHoverShadow:"
+ "setControllerIndex:"
+ "setControllerQueue:"
+ "setFindMyCoordinator:"
+ "setHasScribbleKeyboard:"
+ "setIdentifier:"
+ "setMapView:"
+ "showFindMyController"
+ "tempDoTheNormalThing"
+ "v24@0:8@\"CLLocationManager\"16"
+ "v24@0:8@\"MKMapView\"16"
+ "v28@0:8@\"CLLocationManager\"16i24"
+ "v28@0:8@\"MKMapView\"16B24"
+ "v28@0:8@16i24"
+ "v32@0:8@\"CLLocationManager\"16@\"CLHeading\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"CLRegion\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"CLVisit\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"NSArray\"24"
+ "v32@0:8@\"CLLocationManager\"16@\"NSError\"24"
+ "v32@0:8@\"MKMapView\"16@\"<MKAnnotation>\"24"
+ "v32@0:8@\"MKMapView\"16@\"MKAnnotationView\"24"
+ "v32@0:8@\"MKMapView\"16@\"MKUserLocation\"24"
+ "v32@0:8@\"MKMapView\"16@\"NSArray\"24"
+ "v32@0:8@\"MKMapView\"16@\"NSError\"24"
+ "v36@0:8@\"MKMapView\"16q24B32"
+ "v36@0:8@\"UINavigationController\"16@\"UIViewController\"24B32"
+ "v36@0:8@16@24B32"
+ "v36@0:8@16q24B32"
+ "v40@0:8@\"CLLocationManager\"16@\"CLBeaconIdentityConstraint\"24@\"NSError\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"CLBeaconRegion\"24@\"NSError\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"CLLocation\"24@\"CLLocation\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"CLRegion\"24@\"NSError\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconIdentityConstraint\"32"
+ "v40@0:8@\"CLLocationManager\"16@\"NSArray\"24@\"CLBeaconRegion\"32"
+ "v40@0:8@\"CLLocationManager\"16q24@\"CLRegion\"32"
+ "v40@0:8@\"MKMapView\"16@\"MKAnnotationView\"24@\"UIControl\"32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16q24@32"
+ "v48@0:8@\"MKMapView\"16@\"MKAnnotationView\"24Q32Q40"
+ "v48@0:8@16@24Q32Q40"
+ "whatsNewControllerQueueForType:"
- "\x11!"
- "decodeObjectForKey:"

```
