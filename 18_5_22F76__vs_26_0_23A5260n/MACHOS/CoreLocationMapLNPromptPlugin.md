## CoreLocationMapLNPromptPlugin

> `/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationMapLNPromptPlugin.appex/CoreLocationMapLNPromptPlugin`

```diff

-2964.0.4.0.0
-  __TEXT.__text: 0x73c8
+3051.0.3.0.0
+  __TEXT.__text: 0x7dac
   __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_stubs: 0x1660
-  __TEXT.__objc_methlist: 0x658
-  __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x10b0
-  __TEXT.__cstring: 0x330
-  __TEXT.__objc_methname: 0x18e5
-  __TEXT.__objc_classname: 0xa6
-  __TEXT.__objc_methtype: 0x7f0
-  __TEXT.__oslogstring: 0x4c8
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__objc_stubs: 0x1720
+  __TEXT.__objc_methlist: 0x668
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0x1234
+  __TEXT.__cstring: 0x23c
+  __TEXT.__objc_methname: 0x19f5
+  __TEXT.__objc_classname: 0xa7
+  __TEXT.__objc_methtype: 0x678
+  __TEXT.__oslogstring: 0x386
+  __TEXT.__unwind_info: 0x230
   __DATA_CONST.__auth_got: 0x1d8
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1020
-  __DATA.__objc_selrefs: 0x790
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_const: 0x1080
+  __DATA.__objc_selrefs: 0x7b8
+  __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /System/Library/PrivateFrameworks/VectorKit.framework/VectorKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7D7F538-A996-3193-8D24-E2336A3BE60B
-  Functions: 99
-  Symbols:   125
-  CStrings:  435
+  UUID: 263E1BC2-3DBC-3915-A27B-EF694D8E5AA7
+  Functions: 97
+  Symbols:   127
+  CStrings:  438
 
Symbols:
+ _OBJC_CLASS_$_CLLocation
+ _SBSUIUserNotificationContentCornerRadius
+ __ZnwmSt19__type_descriptor_t
+ __os_feature_enabled_impl
- __Znwm
- _abort_report_np
CStrings:
+ "#BaseViewController viewWillLayoutSubviews mapview frame updated width: %f height: %f"
+ "Solarium"
+ "SwiftUI"
+ "T@\"NSMutableArray\",&,N,V_locationCoordinates"
+ "Td,N,V_mapViewHeight"
+ "_locationCoordinates"
+ "_mapViewHeight"
+ "constraintGreaterThanOrEqualToSystemSpacingBelowAnchor:multiplier:"
+ "d"
+ "d16@0:8"
+ "initWithLatitude:longitude:"
+ "locationCoordinates"
+ "mapViewHeight"
+ "setAdjustsFontForContentSizeCategory:"
+ "setLocationCoordinates:"
+ "setMapViewHeight:"
+ "setMaskedCorners:"
+ "setMasksToBounds:"
+ "{?={?=dd}{?=dd}}40@0:8{vector<MKMapRect, std::allocator<MKMapRect>>=^{?}^{?}^{?}}16"
- "%s:%d: assertion failure in %s"
- "-[CLAuthWithLocalNetworkCalloutViewController averageOfCoordinates:]"
- "/Library/Caches/com.apple.xbs/Sources/CoreLocation/Plugins/CoreLocationMapLNPromptPlugin/CLAuthWithLocalNetworkCalloutViewController.mm"
- "assert"
- "averageOfCoordinates:"
- "coords.size() > 0"
- "must supply at least one coordinate if computing average"
- "setLayoutMargins:"
- "toCartesian:"
- "viewDidLayoutSubviews"
- "{\"msg%{public}.0s\":\"computed average\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"computed midpoint\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\"}"
- "{\"msg%{public}.0s\":\"must supply at least one coordinate if computing average\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "{?={?=dd}{?=dd}}40@0:8{vector<MKMapRect, std::allocator<MKMapRect>>=^{?}^{?}{__compressed_pair<MKMapRect *, std::allocator<MKMapRect>>=^{?}}}16"
- "{CLLocationCoordinate2D=dd}40@0:8{vector<CLLocationCoordinate2D, std::allocator<CLLocationCoordinate2D>>=^{CLLocationCoordinate2D}^{CLLocationCoordinate2D}{__compressed_pair<CLLocationCoordinate2D *, std::allocator<CLLocationCoordinate2D>>=^{CLLocationCoordinate2D}}}16"
- "{CartesianCoord=ddd}32@0:8{CLLocationCoordinate2D=dd}16"

```
