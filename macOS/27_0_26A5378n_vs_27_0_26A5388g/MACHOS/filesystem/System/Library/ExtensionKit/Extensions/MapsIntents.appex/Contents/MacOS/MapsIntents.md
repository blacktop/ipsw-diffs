## MapsIntents

> `/System/Library/ExtensionKit/Extensions/MapsIntents.appex/Contents/MacOS/MapsIntents`

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

-2972.20.6.12.13
-  __TEXT.__text: 0x52700
-  __TEXT.__auth_stubs: 0x1ba0
-  __TEXT.__objc_stubs: 0x10e0
+2972.20.6.12.30
+  __TEXT.__text: 0x55068
+  __TEXT.__auth_stubs: 0x1c40
+  __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0xfe4
-  __TEXT.__const: 0x4b54
-  __TEXT.__cstring: 0x1c35
-  __TEXT.__objc_methname: 0x495b
-  __TEXT.__oslogstring: 0x18fb
+  __TEXT.__const: 0x4c14
+  __TEXT.__cstring: 0x1d05
+  __TEXT.__objc_methname: 0x4a3a
+  __TEXT.__oslogstring: 0x194b
   __TEXT.__objc_classname: 0x1cb
   __TEXT.__objc_methtype: 0xff0
-  __TEXT.__swift5_typeref: 0x2326
-  __TEXT.__swift5_reflstr: 0x108c
+  __TEXT.__swift5_typeref: 0x29ac
+  __TEXT.__swift5_reflstr: 0x10de
   __TEXT.__swift5_assocty: 0x7b0
   __TEXT.__constg_swiftt: 0x690
-  __TEXT.__swift5_fieldmd: 0x9c0
+  __TEXT.__swift5_fieldmd: 0x9e4
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x3f8
   __TEXT.__swift5_types: 0x90
-  __TEXT.__swift_as_entry: 0xec
-  __TEXT.__swift_as_ret: 0x140
-  __TEXT.__swift_as_cont: 0x250
-  __TEXT.__swift5_capture: 0xc0
+  __TEXT.__swift_as_entry: 0xf4
+  __TEXT.__swift_as_ret: 0x154
+  __TEXT.__swift_as_cont: 0x258
+  __TEXT.__swift5_capture: 0xd0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x1498
-  __TEXT.__eh_frame: 0x2720
-  __DATA_CONST.__const: 0x1c30
+  __TEXT.__unwind_info: 0x14c0
+  __TEXT.__eh_frame: 0x2878
+  __DATA_CONST.__const: 0x1c80
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x88

   __DATA_CONST.__objc_arraydata: 0x70
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__objc_doubleobj: 0x370
-  __DATA_CONST.__objc_intobj: 0x738
+  __DATA_CONST.__objc_intobj: 0x750
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA_CONST.__auth_got: 0xdd8
-  __DATA_CONST.__got: 0x538
-  __DATA_CONST.__auth_ptr: 0xa00
+  __DATA_CONST.__auth_got: 0xe28
+  __DATA_CONST.__got: 0x570
+  __DATA_CONST.__auth_ptr: 0xa18
   __DATA.__objc_const: 0x1e48
-  __DATA.__objc_selrefs: 0xd48
+  __DATA.__objc_selrefs: 0xda0
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x1b88
+  __DATA.__data: 0x1c58
   __DATA.__bss: 0x7fb0
-  __DATA.__common: 0x120
+  __DATA.__common: 0x128
   - /System/Library/Frameworks/AppIntents.framework/Versions/A/AppIntents
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1456
-  Symbols:   254
-  CStrings:  1240
+  Functions: 1477
+  Symbols:   259
+  CStrings:  1254
 
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
