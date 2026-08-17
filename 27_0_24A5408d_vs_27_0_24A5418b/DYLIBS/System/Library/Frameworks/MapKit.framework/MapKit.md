## MapKit

> `/System/Library/Frameworks/MapKit.framework/MapKit`

```diff

-2552.30.6.12.9
-  __TEXT.__text: 0x28ff04
+2552.30.6.12.12
+  __TEXT.__text: 0x28fef0
   __TEXT.__objc_methlist: 0x26b94
   __TEXT.__const: 0x6910
   __TEXT.__dlopen_cstrs: 0xbc

   __TEXT.__swift_as_entry: 0x13c
   __TEXT.__swift_as_ret: 0x134
   __TEXT.__swift_as_cont: 0x1cc
-  __TEXT.__gcc_except_tab: 0x61bc
+  __TEXT.__gcc_except_tab: 0x61c0
   __TEXT.__ustring: 0x19c
   __TEXT.__unwind_info: 0xa7e8
   __TEXT.__eh_frame: 0x241c
Symbols:
+ +[MKPolygon _polygonWithCoordinates:count:interiorPolygons:vectorOverlayStyle:]
+ GCC_except_table9913
+ GCC_except_table9917
+ _objc_msgSend$_polygonWithCoordinates:count:interiorPolygons:vectorOverlayStyle:
- -[MKPolygon _initWithCoordinates:count:interiorPolygons:vectorOverlayStyle:]
- GCC_except_table9911
- GCC_except_table9916
- _objc_msgSend$_initWithCoordinates:count:interiorPolygons:vectorOverlayStyle:
Functions:
~ -[MKPolygon _initWithCoordinates:count:interiorPolygons:vectorOverlayStyle:] -> +[MKPolygon _polygonWithCoordinates:count:interiorPolygons:vectorOverlayStyle:] : 256 -> 244
~ +[MKPolygon polygonWithCoordinates:count:] : 80 -> 72
```
