## CalendarNotification

> `/System/Library/PrivateFrameworks/CalendarNotification.framework/CalendarNotification`

```diff

-1502.1.1.2.0
-  __TEXT.__text: 0x5744c
+1502.1.1.3.0
+  __TEXT.__text: 0x57358
   __TEXT.__auth_stubs: 0x7e0
   __TEXT.__objc_methlist: 0x590c
   __TEXT.__const: 0x130
-  __TEXT.__oslogstring: 0xda04
+  __TEXT.__oslogstring: 0xd9ca
   __TEXT.__cstring: 0x3efd
   __TEXT.__gcc_except_tab: 0x3e8
-  __TEXT.__unwind_info: 0x151c
+  __TEXT.__unwind_info: 0x1514
   __TEXT.__objc_classname: 0x1bfa
-  __TEXT.__objc_methname: 0x126c8
-  __TEXT.__objc_methtype: 0x309f
+  __TEXT.__objc_methname: 0x12692
+  __TEXT.__objc_methtype: 0x3094
   __TEXT.__objc_stubs: 0xbb00
-  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0xd10
   __DATA_CONST.__objc_classlist: 0x488
   __DATA_CONST.__objc_catlist: 0x0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49A580BD-0EEF-3A5A-B0B5-53A9087E78AD
+  UUID: 2D7A64CC-02D6-3BA8-B33E-ED449EA137D0
   Functions: 2264
-  Symbols:   9066
-  CStrings:  4293
+  Symbols:   9065
+  CStrings:  4292
 
Symbols:
+ +[CALNDefaultTriggeredEventNotificationMapItemURLProvider _mapItemURLForEventLocation:hypothesis:]
+ +[CALNDefaultTriggeredEventNotificationMapItemURLProvider _mapItemURLLaunchOptionsForDirectionsMode:isFromTimeToLeaveNotification:]
+ +[CALNDefaultTriggeredEventNotificationMapItemURLProvider _mapItemURLLaunchOptionsForHypothesis:routing:]
+ -[CALNDefaultTriggeredEventNotificationMapItemURLProvider mapItemURLForOptionalEventLocation:hypothesis:]
+ _objc_msgSend$_mapItemURLForEventLocation:hypothesis:
+ _objc_msgSend$_mapItemURLLaunchOptionsForDirectionsMode:isFromTimeToLeaveNotification:
+ _objc_msgSend$_mapItemURLLaunchOptionsForHypothesis:routing:
+ _objc_msgSend$mapItemURLForOptionalEventLocation:hypothesis:
- +[CALNDefaultTriggeredEventNotificationMapItemURLProvider _mapItemURLForEventLocation:eventStartDate:hypothesis:]
- +[CALNDefaultTriggeredEventNotificationMapItemURLProvider _mapItemURLLaunchOptionsForDirectionsMode:eventDate:isFromTimeToLeaveNotification:]
- +[CALNDefaultTriggeredEventNotificationMapItemURLProvider _mapItemURLLaunchOptionsForHypothesis:routing:eventStartDate:]
- -[CALNDefaultTriggeredEventNotificationMapItemURLProvider mapItemURLForOptionalEventLocation:eventStartDate:hypothesis:]
- __MKLaunchOptionsRoutingArrivalDateKey
- _objc_msgSend$_mapItemURLForEventLocation:eventStartDate:hypothesis:
- _objc_msgSend$_mapItemURLLaunchOptionsForDirectionsMode:eventDate:isFromTimeToLeaveNotification:
- _objc_msgSend$_mapItemURLLaunchOptionsForHypothesis:routing:eventStartDate:
- _objc_msgSend$mapItemURLForOptionalEventLocation:eventStartDate:hypothesis:
CStrings:
+ "@\"NSURL\"32@0:8@\"EKStructuredLocation\"16@\"EKTravelEngineHypothesis\"24"
+ "_mapItemURLForEventLocation:hypothesis:"
+ "_mapItemURLLaunchOptionsForDirectionsMode:isFromTimeToLeaveNotification:"
+ "_mapItemURLLaunchOptionsForHypothesis:routing:"
+ "mapItemURLForOptionalEventLocation:hypothesis:"
- "@\"NSURL\"40@0:8@\"EKStructuredLocation\"16@\"NSDate\"24@\"EKTravelEngineHypothesis\"32"
- "No arrival date provided for map item url launch options."
- "_mapItemURLForEventLocation:eventStartDate:hypothesis:"
- "_mapItemURLLaunchOptionsForDirectionsMode:eventDate:isFromTimeToLeaveNotification:"
- "_mapItemURLLaunchOptionsForHypothesis:routing:eventStartDate:"
- "mapItemURLForOptionalEventLocation:eventStartDate:hypothesis:"

```
