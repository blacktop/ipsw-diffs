## CoreLocationRepromptAlwaysAuthPromptPlugin

> `/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationRepromptAlwaysAuthPromptPlugin.appex/CoreLocationRepromptAlwaysAuthPromptPlugin`

```diff

-2964.0.4.0.0
-  __TEXT.__text: 0x2614
-  __TEXT.__auth_stubs: 0x1d0
-  __TEXT.__objc_stubs: 0xaa0
-  __TEXT.__objc_methlist: 0x500
-  __TEXT.__const: 0xbc
-  __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__oslogstring: 0x305
-  __TEXT.__objc_methname: 0xdfc
-  __TEXT.__cstring: 0x88
-  __TEXT.__objc_classname: 0xbe
-  __TEXT.__objc_methtype: 0x4a5
-  __TEXT.__unwind_info: 0x148
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0xb0
+3051.0.3.0.0
+  __TEXT.__text: 0x3e18
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__objc_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x570
+  __TEXT.__const: 0xe4
+  __TEXT.__gcc_except_tab: 0x58c
+  __TEXT.__oslogstring: 0x2be
+  __TEXT.__objc_methname: 0xe78
+  __TEXT.__cstring: 0xa0
+  __TEXT.__objc_classname: 0xc7
+  __TEXT.__objc_methtype: 0x573
+  __TEXT.__unwind_info: 0x1c0
+  __DATA_CONST.__auth_got: 0x150
+  __DATA_CONST.__got: 0xe8
   __DATA_CONST.__cfstring: 0x120
-  __DATA_CONST.__objc_classlist: 0x18
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__objc_doubleobj: 0x40
-  __DATA.__objc_const: 0xdd8
-  __DATA.__objc_selrefs: 0x478
-  __DATA.__objc_ivar: 0x34
-  __DATA.__objc_data: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x20
+  __DATA.__objc_const: 0xf08
+  __DATA.__objc_selrefs: 0x4b8
+  __DATA.__objc_ivar: 0x40
+  __DATA.__objc_data: 0x140
   __DATA.__data: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 902E4A70-BBB7-3C4A-B775-397A289BE949
-  Functions: 46
-  Symbols:   70
-  CStrings:  271
+  UUID: CBD9787A-19A9-36CB-A447-24FB286C8659
+  Functions: 68
+  Symbols:   89
+  CStrings:  294
 
Symbols:
+ _MKCoordinateRegionForMapRect
+ _MKMapPointForCoordinate
+ _MKMapRectNull
+ _MKMapRectWorld
+ _OBJC_CLASS_$_MapRect
+ _OBJC_METACLASS_$_MapRect
+ _SBSUIUserNotificationContentCornerRadius
+ __ZNSt11logic_errorC2EPKc
+ __ZNSt12length_errorD1Ev
+ __ZNSt20bad_array_new_lengthC1Ev
+ __ZNSt20bad_array_new_lengthD1Ev
+ __ZTISt12length_error
+ __ZTISt20bad_array_new_length
+ __ZTVSt12length_error
+ __ZdlPv
+ __ZnwmSt19__type_descriptor_t
+ ___cxa_allocate_exception
+ ___cxa_free_exception
+ ___cxa_throw
+ ___sincos_stret
+ __os_feature_enabled_impl
+ _atan2
+ _memcpy
+ _memmove
- _OBJC_CLASS_$_NSConstantDoubleNumber
- _OBJC_CLASS_$_NSMutableArray
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
CStrings:
+ "#BaseViewController viewWillLayoutSubviews mapview frame updated width: %f height: %f"
+ "@80@0:8{?={?=dd}{?=dd}}16{?={?=dd}{?=dd}}48"
+ "MapRect"
+ "Solarium"
+ "SwiftUI"
+ "Td,N,V_mapViewHeight"
+ "Tf,N,V_latDelta"
+ "Tf,N,V_lonDelta"
+ "T{?={?=dd}{?=dd}},R,N,V_rect"
+ "_latDelta"
+ "_lonDelta"
+ "_mapViewHeight"
+ "_rect"
+ "boundingWithNormalizedRects:"
+ "f"
+ "f16@0:8"
+ "frame"
+ "initWithRectA:rectB:"
+ "latDelta"
+ "layer"
+ "lonDelta"
+ "mapViewHeight"
+ "rect"
+ "setCornerRadius:"
+ "setFrame:"
+ "setLatDelta:"
+ "setLonDelta:"
+ "setMapViewHeight:"
+ "setMaskedCorners:"
+ "setMasksToBounds:"
+ "v20@0:8f16"
+ "vector"
+ "viewWillLayoutSubviews"
+ "{?=\"origin\"{?=\"x\"d\"y\"d}\"size\"{?=\"width\"d\"height\"d}}"
+ "{?={?=dd}{?=dd}}16@0:8"
+ "{?={?=dd}{?=dd}}40@0:8{vector<MKMapRect, std::allocator<MKMapRect>>=^{?}^{?}^{?}}16"
- "#reprompt Location: [%{sensitive}f, %{sensitive}f]"
- "@\"NSMutableArray\""
- "CoreLocationAuthPromptPlugin: Extremities: [%{sensitive}f, %{sensitive}f], [%{sensitive}f, %{sensitive}f]"
- "T@\"NSMutableArray\",&,N,V_regionExtremities"
- "_regionExtremities"
- "_updateMapExtremities:"
- "floatValue"
- "initWithCapacity:"
- "numberWithDouble:"
- "objectAtIndexedSubscript:"
- "regionExtremities"
- "setObject:atIndexedSubscript:"
- "setRegionExtremities:"

```
