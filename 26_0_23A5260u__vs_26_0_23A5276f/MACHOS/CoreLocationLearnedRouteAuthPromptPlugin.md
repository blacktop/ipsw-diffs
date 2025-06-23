## CoreLocationLearnedRouteAuthPromptPlugin

> `/System/Library/Frameworks/CoreLocation.framework/PlugIns/CoreLocationLearnedRouteAuthPromptPlugin.appex/CoreLocationLearnedRouteAuthPromptPlugin`

```diff

-3051.0.3.0.0
-  __TEXT.__text: 0x3c48
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_stubs: 0xe20
+3056.0.0.0.0
+  __TEXT.__text: 0x4070
+  __TEXT.__auth_stubs: 0x370
+  __TEXT.__objc_stubs: 0xe40
   __TEXT.__objc_methlist: 0x578
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x52f
-  __TEXT.__oslogstring: 0x4aa
+  __TEXT.__cstring: 0x6c9
+  __TEXT.__oslogstring: 0x53c
   __TEXT.__objc_classname: 0xc5
   __TEXT.__objc_methtype: 0x57c
-  __TEXT.__gcc_except_tab: 0x6e4
-  __TEXT.__objc_methname: 0x12de
-  __TEXT.__unwind_info: 0x1c0
-  __DATA_CONST.__auth_got: 0x1d0
+  __TEXT.__gcc_except_tab: 0x738
+  __TEXT.__objc_methname: 0x1303
+  __TEXT.__unwind_info: 0x1b8
+  __DATA_CONST.__auth_got: 0x1c8
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__cfstring: 0x3c0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA.__objc_const: 0xeb0
-  __DATA.__objc_selrefs: 0x588
+  __DATA.__objc_selrefs: 0x590
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x160

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 54899B33-C3DE-31F1-AB74-341AA31F15E5
+  UUID: 9BD0474C-9B22-3018-8A17-3DF53AA1365A
   Functions: 75
-  Symbols:   116
-  CStrings:  380
+  Symbols:   115
+  CStrings:  389
 
Symbols:
- _objc_retain_x3
Functions:
~ sub_100002cd4 : 196 -> 464
~ sub_100003100 -> sub_10000320c : 1124 -> 1212
~ sub_100003564 -> sub_1000036c8 : 952 -> 1052
~ sub_100003e3c -> sub_100004004 : 1680 -> 1900
~ sub_1000044cc -> sub_100004770 : 172 -> 368
~ sub_100004578 -> sub_1000048e0 : 924 -> 1116
CStrings:
+ "-[CLLearnedRouteAuthPromptPluginViewController configureMapView]"
+ "-[CLLearnedRouteAuthPromptPluginViewController configureProperties]"
+ "-[CLLearnedRouteAuthPromptPluginViewController loadView]"
+ "-[CLLearnedRouteAuthPromptPluginViewController mapView:rendererForOverlay:]"
+ "-[CLLearnedRouteAuthPromptPluginViewController mapView:viewForAnnotation:]"
+ "-[CLLearnedRouteAuthPromptPluginViewController parseUserInfo:error:]"
+ "Hiding map view because Show Map in Location Alerts is turned off."
+ "Not fetching learned routes because Show Map in Location Alerts is turned off."
+ "authorizationPromptMapDisplayEnabled"

```
