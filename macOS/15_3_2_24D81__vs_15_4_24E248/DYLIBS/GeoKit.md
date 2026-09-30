## GeoKit

> `/System/Library/PrivateFrameworks/GeoKit.framework/Versions/A/GeoKit`

```diff

-90.0.0.0.0
-  __TEXT.__text: 0xcf44
+90.3.2.0.0
+  __TEXT.__text: 0xcf60
   __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_methlist: 0x1154
+  __TEXT.__objc_methlist: 0x137c
   __TEXT.__cstring: 0x1c9c
   __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__unwind_info: 0x4f8
   __TEXT.__objc_classname: 0x1b5
   __TEXT.__objc_methname: 0x3c52
   __TEXT.__objc_methtype: 0xac8

   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1188
+  __DATA_CONST.__objc_selrefs: 0x1268
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x1c60
-  __AUTH_CONST.__objc_const: 0x2208
+  __AUTH_CONST.__objc_const: 0x1e00
   __AUTH_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_ivar: 0x158
   __DATA.__data: 0x250

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 68758BF9-AB67-3D87-997E-39478E79931A
-  Functions: 392
-  Symbols:   1312
+  UUID: 01B64FBF-EB18-38AD-8148-29265AE3AFEE
+  Functions: 393
+  Symbols:   1313
   CStrings:  1374
 
Symbols:
+ GEOCreateImageFromResources.cold.1
Functions:
~ _GEOCreateImageFromResources : 480 -> 460
~ -[GEOTimezoneHitMap _areaLabelAtLongitude:latitude:] : 264 -> 260
~ -[NSData(gzip) gzipInflate] : 392 -> 388
~ -[GEOCityPickerViewPrivController _searchByNameCallback:returnedCityIDs:] : 304 -> 312
~ -[GEOCityPickerView _bindPublicToPrivateProperties] : 416 -> 420
~ _GEOWarningLog : 84 -> 88
~ _GEONoticeLog : 88 -> 92
~ _GEOLog : 68 -> 72
~ -[GEOWorldTimeZoneView _drawCityResultInContext:dotImage:contextSize:city:] : 204 -> 216
~ -[GEOWorldTimeZoneView observeValueForKeyPath:ofObject:change:context:] : 128 -> 124
~ -[GEOWorldTimeZoneView pinPoint] : 64 -> 68
~ -[GEOWorldView updatedWorldMapEnabled] : 188 -> 192
~ -[GEOWorldView globeRotation] : 84 -> 80
~ -[GEOWorldView viewPrimeMeridian] : 116 -> 112
~ -[GEOWorldView mouseEntered:] : 104 -> 100
~ -[GEOWorldView mouseExited:] : 104 -> 100
~ -[GEOWorldView mouseUp:] : 108 -> 112
~ -[GEOWorldView mouseDown:] : 108 -> 112
~ -[GEOWorldView mouseDragged:] : 108 -> 112
~ -[GEOWorldView mouseDown:coordinate:] : 216 -> 220
~ -[GEOWorldImageLayer imageSize] : 64 -> 68
~ -[GEOWorldCityLightsLayer initWithImages:] : 492 -> 484

```
