## FlightUtilities

> `/System/Library/PrivateFrameworks/FlightUtilities.framework/FlightUtilities`

```diff

-155.2.0.0.0
-  __TEXT.__text: 0xcdbc
+171.0.0.0.0
+  __TEXT.__text: 0xcdc0
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_methlist: 0x14a8
+  __TEXT.__objc_methlist: 0x14c0
   __TEXT.__const: 0x110
   __TEXT.__ustring: 0x42
   __TEXT.__cstring: 0x30f
   __TEXT.__gcc_except_tab: 0x88
-  __TEXT.__unwind_info: 0x488
+  __TEXT.__unwind_info: 0x490
   __TEXT.__objc_classname: 0x230
-  __TEXT.__objc_methname: 0x438a
+  __TEXT.__objc_methname: 0x4383
   __TEXT.__objc_methtype: 0xa9d
   __TEXT.__objc_stubs: 0x3860
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10

   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/FlightUtilitiesCore.framework/FlightUtilitiesCore
   - /System/Library/PrivateFrameworks/TemplateKit.framework/TemplateKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2D067D42-A439-3506-9CAA-0088788447AC
-  Functions: 364
-  Symbols:   1623
+  UUID: 7BF91BAF-AED3-3871-9296-B13566613FC4
+  Functions: 365
+  Symbols:   1626
   CStrings:  1075
 
Symbols:
+ +[FUPlaneTrackerAnnotationLayer geodesicLocationForStartPosition:endPosition:positionPercentage:]
+ +[FUPlaneTrackerAnnotationView geodesicLocationForStartPosition:endPosition:positionPercentage:]
+ __OBJC_$_CLASS_METHODS_FUPlaneTrackerAnnotationLayer
+ _objc_msgSend$airline
- -[FUPlaneTrackerAnnotationLayer geodesicLocationForStartPosition:endPosition:positionPercentage:]
- _objc_msgSend$displayAirline
Functions:
+ +[FUPlaneTrackerAnnotationView geodesicLocationForStartPosition:endPosition:positionPercentage:]
~ -[FUPlaneTrackerAnnotationLayer updatePlaneStateForProgress:] : 312 -> 324
~ -[FUPlaneTrackerAnnotationLayer currentLocation] : 124 -> 136
~ -[FUPlaneTrackerAnnotationLayer defaultHeadingForStartPosition:endPosition:positionPercentage:] : 244 -> 260
~ -[FUFlightView setAbsoluteIndex:animated:] : 924 -> 876
CStrings:
+ "airline"
- "displayAirline"

```
