## CalendarNotificationContentExtension

> `/System/Library/PrivateFrameworks/CalendarNotification.framework/PlugIns/CalendarNotificationContentExtension.appex/CalendarNotificationContentExtension`

```diff

-1530.0.0.0.0
-  __TEXT.__text: 0xf54
-  __TEXT.__auth_stubs: 0x320
-  __TEXT.__objc_stubs: 0x7a0
+1530.1.1.0.0
+  __TEXT.__text: 0x10ec
+  __TEXT.__auth_stubs: 0x210
+  __TEXT.__objc_stubs: 0x7c0
   __TEXT.__objc_methlist: 0x1e4
-  __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__oslogstring: 0x8c
-  __TEXT.__objc_methname: 0x742
+  __TEXT.__const: 0x38
+  __TEXT.__gcc_except_tab: 0x88
+  __TEXT.__oslogstring: 0x157
   __TEXT.__cstring: 0x38
-  __TEXT.__objc_classname: 0x51
-  __TEXT.__objc_methtype: 0x1a8
+  __TEXT.__objc_classname: 0x52
+  __TEXT.__objc_methname: 0x76d
+  __TEXT.__objc_methtype: 0x1a1
   __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0x1a0
-  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x318
-  __DATA.__objc_selrefs: 0x2c8
+  __DATA.__objc_selrefs: 0x2d8
   __DATA.__objc_ivar: 0x10
   __DATA.__objc_data: 0x50
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B889155F-B845-3922-B791-47977F778F10
-  Functions: 13
-  Symbols:   81
-  CStrings:  136
+  UUID: 1561CF66-FCD3-33F1-A3F3-341B76795745
+  Functions: 15
+  Symbols:   65
+  CStrings:  144
 
Symbols:
+ _OBJC_CLASS_$_MKCircle
+ _OBJC_CLASS_$_MKCircleRenderer
+ __dispatch_main_q
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_new
+ _objc_retain_x19
+ _objc_retain_x8
- _CGContextFillEllipseInRect
- _CGContextRestoreGState
- _CGContextSaveGState
- _CGContextSetFillColorWithColor
- _CGContextSetStrokeColorWithColor
- _CGContextStrokeEllipseInRect
- _CGPointZero
- _MKCoordinateForMapPoint
- _MKMapPointForCoordinate
- _MKMetersPerMapPointAtLatitude
- _OBJC_CLASS_$_UIView
- _UIGraphicsBeginImageContextWithOptions
- _UIGraphicsEndImageContext
- _UIGraphicsGetCurrentContext
- _UIGraphicsGetImageFromCurrentImageContext
- __Block_object_dispose
- _dispatch_get_global_queue
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _objc_alloc_init
- _objc_autoreleaseReturnValue
- _objc_opt_respondsToSelector
- _objc_release_x9
- _objc_retainAutorelease
- _objc_retain_x23
CStrings:
+ "B"
+ "Error getting snapshot (gridOnly: %d): %@"
+ "Q"
+ "Snapshot image is nil (gridOnly: %d)"
+ "Snapshot is nil (gridOnly: %d)"
+ "_configureForLocation:"
+ "_configureForLocation:gridOnly:"
+ "_configureWithPreviewForEvent:"
+ "_contentView"
+ "_generation"
+ "_mapLoaded"
+ "_setContentView:"
+ "_setOverlayRenderers:forOverlayLevel:"
+ "_snapshotCompleted:error:generation:gridOnly:"
+ "activateConstraints:"
+ "circleWithCenterCoordinate:radius:"
+ "constraintEqualToAnchor:"
+ "generation mismatch (gridOnly: %d): %lu != %lu"
+ "heightAnchor"
+ "initWithCircle:"
+ "leadingAnchor"
+ "map already loaded, dropping grid"
+ "removeFromSuperview"
+ "self is nil"
+ "setFillColor:"
+ "setLineWidth:"
+ "setMapType:"
+ "setStrokeColor:"
+ "topAnchor"
+ "v28@0:8@16B24"
+ "v44@0:8@16@24Q32B40"
+ "widthAnchor"
- "@\"NSArray\""
- "@\"NSURL\""
- "@24@0:8@16"
- "@32@0:8@16q24"
- "CGColor"
- "_entityID"
- "_longLookConstraints"
- "_longLookView"
- "addConstraint:"
- "addConstraints:"
- "addLongLookView:"
- "constraintWithItem:attribute:relatedBy:toItem:attribute:multiplier:constant:"
- "dayPreviewViewForEvent:withStatusOverride:"
- "drawAtPoint:"
- "frame"
- "initWithFrame:"
- "pointForCoordinate:"
- "scale"
- "setOverriddenParticipantStatus:"
- "setView:"
- "size"
- "viewForAlertNotificationForEvent:"
- "viewForEventInvitation:"
- "viewForLocation:"

```
