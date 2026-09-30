## CoreLocationMapLNPromptPlugin

> `/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationMapLNPromptPlugin.appex/CoreLocationMapLNPromptPlugin`

```diff

-2956.0.3.0.2
-  __TEXT.__text: 0x69e0
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x1600
-  __TEXT.__objc_methlist: 0x3c0
-  __TEXT.__const: 0xd0
-  __TEXT.__gcc_except_tab: 0x1000
-  __TEXT.__cstring: 0x22b
-  __TEXT.__objc_methname: 0x18bb
+2956.0.5.0.0
+  __TEXT.__text: 0x74b4
+  __TEXT.__auth_stubs: 0x380
+  __TEXT.__objc_stubs: 0x1660
+  __TEXT.__objc_methlist: 0x3e0
+  __TEXT.__const: 0x108
+  __TEXT.__gcc_except_tab: 0x1080
+  __TEXT.__cstring: 0x330
+  __TEXT.__objc_methname: 0x18e5
   __TEXT.__objc_classname: 0xa6
-  __TEXT.__objc_methtype: 0x6aa
-  __TEXT.__oslogstring: 0x2cc
-  __TEXT.__unwind_info: 0x210
-  __DATA_CONST.__auth_got: 0x1a8
+  __TEXT.__objc_methtype: 0x7f0
+  __TEXT.__oslogstring: 0x4c0
+  __TEXT.__unwind_info: 0x250
+  __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__cfstring: 0x2a0

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0x14d8
-  __DATA.__objc_selrefs: 0x600
+  __DATA.__objc_selrefs: 0x618
   __DATA.__objc_ivar: 0x60
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 90
-  Symbols:   119
-  CStrings:  402
+  Functions: 99
+  Symbols:   124
+  CStrings:  417
 
Symbols:
+ _MKCoordinateRegionForMapRect
+ _MKMapRectForCoordinateRegion
+ ___sincos_stret
+ _abort_report_np
+ _atan2
CStrings:
+ "%s:%d: assertion failure in %s"
+ "-[CLAuthWithLocalNetworkCalloutViewController averageOfCoordinates:]"
+ "/Library/Caches/com.apple.xbs/Sources/CoreLocation/Plugins/CoreLocationMapLNPromptPlugin/CLAuthWithLocalNetworkCalloutViewController.mm"
+ "assert"
+ "averageOfCoordinates:"
+ "coords.size() > 0"
+ "must supply at least one coordinate if computing average"
+ "region"
+ "toCartesian:"
+ "{\"msg%{public}.0s\":\"callout with coordinate\", \"lat\":\"%{sensitive}.08f\", \"lon\":\"%{sensitive}.08f\"}"
+ "{\"msg%{public}.0s\":\"centering map view at\", \"lat\":\"%{private}.5f\", \"lon\":\"%{private}.5f\"}"
+ "{\"msg%{public}.0s\":\"computed average\", \"latitude\":\"%{private}.5f\", \"lon\":\"%{private}.5f\"}"
+ "{\"msg%{public}.0s\":\"computed midpoint\", \"latitude\":\"%{private}.5f\", \"lon\":\"%{private}.5f\"}"
+ "{\"msg%{public}.0s\":\"must supply at least one coordinate if computing average\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{CLLocationCoordinate2D=dd}40@0:8{vector<CLLocationCoordinate2D, std::allocator<CLLocationCoordinate2D>>=^{CLLocationCoordinate2D}^{CLLocationCoordinate2D}{__compressed_pair<CLLocationCoordinate2D *, std::allocator<CLLocationCoordinate2D>>=^{CLLocationCoordinate2D}}}16"
+ "{CartesianCoord=ddd}32@0:8{CLLocationCoordinate2D=dd}16"
- "{\"msg%{public}.0s\":\"callout with coordinate\", \"lat\":\"%{private}.08f\", \"lon\":\"%{private}.08f\"}"

```
