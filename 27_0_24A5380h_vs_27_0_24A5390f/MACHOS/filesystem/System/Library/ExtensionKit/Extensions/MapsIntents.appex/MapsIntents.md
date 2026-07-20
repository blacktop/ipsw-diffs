## MapsIntents

> `/System/Library/ExtensionKit/Extensions/MapsIntents.appex/MapsIntents`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__bss`

```diff

-2972.30.6.12.16
-  __TEXT.__text: 0x537c8
-  __TEXT.__auth_stubs: 0x1ba0
-  __TEXT.__objc_stubs: 0x1140
+2972.30.6.12.32
+  __TEXT.__text: 0x560c0
+  __TEXT.__auth_stubs: 0x1c40
+  __TEXT.__objc_stubs: 0x12a0
   __TEXT.__objc_methlist: 0xffc
-  __TEXT.__const: 0x4df4
-  __TEXT.__cstring: 0x1c95
-  __TEXT.__objc_methname: 0x49df
-  __TEXT.__oslogstring: 0x195b
+  __TEXT.__const: 0x4eb4
+  __TEXT.__cstring: 0x1d65
+  __TEXT.__objc_methname: 0x4abe
+  __TEXT.__oslogstring: 0x19ab
   __TEXT.__objc_classname: 0x1cb
   __TEXT.__objc_methtype: 0x1000
-  __TEXT.__swift5_typeref: 0x23c8
-  __TEXT.__swift5_reflstr: 0x10fc
+  __TEXT.__swift5_typeref: 0x2a4e
+  __TEXT.__swift5_reflstr: 0x114e
   __TEXT.__swift5_assocty: 0x808
   __TEXT.__constg_swiftt: 0x6ac
-  __TEXT.__swift5_fieldmd: 0x9e8
+  __TEXT.__swift5_fieldmd: 0xa0c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x420
   __TEXT.__swift5_types: 0x94
-  __TEXT.__swift_as_entry: 0xf0
-  __TEXT.__swift_as_ret: 0x144
-  __TEXT.__swift_as_cont: 0x250
-  __TEXT.__swift5_capture: 0xc0
+  __TEXT.__swift_as_entry: 0xf8
+  __TEXT.__swift_as_ret: 0x158
+  __TEXT.__swift_as_cont: 0x258
+  __TEXT.__swift5_capture: 0xd0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1510
-  __TEXT.__eh_frame: 0x27a0
-  __DATA_CONST.__const: 0x1ca8
+  __TEXT.__unwind_info: 0x1538
+  __TEXT.__eh_frame: 0x28f8
+  __DATA_CONST.__const: 0x1cf8
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_doubleobj: 0x3a0
-  __DATA_CONST.__objc_intobj: 0x780
+  __DATA_CONST.__objc_intobj: 0x798
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA_CONST.__auth_got: 0xdd8
-  __DATA_CONST.__got: 0x540
-  __DATA_CONST.__auth_ptr: 0xa08
+  __DATA_CONST.__auth_got: 0xe28
+  __DATA_CONST.__got: 0x578
+  __DATA_CONST.__auth_ptr: 0xa20
   __DATA.__objc_const: 0x1e98
-  __DATA.__objc_selrefs: 0xd70
+  __DATA.__objc_selrefs: 0xdc8
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x1bf8
+  __DATA.__data: 0x1cc8
   __DATA.__bss: 0x84b0
-  __DATA.__common: 0x120
+  __DATA.__common: 0x128
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1489
-  Symbols:   254
-  CStrings:  1252
+  Functions: 1510
+  Symbols:   259
+  CStrings:  1266
 
Symbols:
+ _OBJC_CLASS_$_MKGeodesicPolyline
+ _OBJC_CLASS_$_MKOverlayRenderer
+ _OBJC_CLASS_$_MKPolylineRenderer
+ _OBJC_CLASS_$_NSNumber
+ __MKMapRectThatFits
CStrings:
+ "CalculateETAIntent: Geodesic snapshotter error: %s"
+ "CalculateETAIntent: currentLocationFlags — missing current-location geoMapItem, treating as not current location"
+ "CalculateETAIntent: currentLocationFlags — origin=%{bool}d, destination=%{bool}d"
+ "CalculateETAIntent: currentLocationFlags — unable to fetch current location: %s"
+ "No valid destination waypoints were provided."
+ "This operation is not supported for the current navigation type."
+ "_setOverlayRenderers:forOverlayLevel:"
+ "boundingMapRect"
+ "cameraLookingAtMapItem:forViewSize:allowPitch:viewInsets:"
+ "colorWithAlphaComponent:"
+ "generateGeodesicDistanceSnapshot(from:to:)"
+ "initWithDouble:"
+ "initWithInteger:"
+ "initWithPolyline:"
+ "polylineWithCoordinates:count:"
+ "setLineDashPattern:"
+ "setLineWidth:"
+ "setMapRect:"
+ "setStrokeColor:"
+ "whiteColor"
- "CalculateETAIntent: originIsCurrentLocation — equalForDirectionsWaypoint=%{bool}d"
- "CalculateETAIntent: originIsCurrentLocation — missing geoMapItem, treating as not current location"
- "CalculateETAIntent: originIsCurrentLocation — unable to fetch current location: %s"
- "cameraLookingAtMapItem:forViewSize:allowPitch:"
- "result"
- "systemBackgroundColor"
```
