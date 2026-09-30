## MapsIntents

> `/System/Library/ExtensionKit/Extensions/MapsIntents.appex/MapsIntents`

```diff

-  __TEXT.__text: 0x51e70
-  __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0xf8c
-  __TEXT.__const: 0x4d34
-  __TEXT.__cstring: 0x1c85
-  __TEXT.__objc_methname: 0x4887
-  __TEXT.__oslogstring: 0x1786
-  __TEXT.__objc_classname: 0x13b
-  __TEXT.__objc_methtype: 0xfd0
-  __TEXT.__swift5_typeref: 0x2386
-  __TEXT.__swift5_reflstr: 0x10ec
+  __TEXT.__text: 0x537c8
+  __TEXT.__auth_stubs: 0x1ba0
+  __TEXT.__objc_stubs: 0x1140
+  __TEXT.__objc_methlist: 0xffc
+  __TEXT.__const: 0x4df4
+  __TEXT.__cstring: 0x1c95
+  __TEXT.__objc_methname: 0x49df
+  __TEXT.__oslogstring: 0x195b
+  __TEXT.__objc_classname: 0x1cb
+  __TEXT.__objc_methtype: 0x1000
+  __TEXT.__swift5_typeref: 0x23c8
+  __TEXT.__swift5_reflstr: 0x10fc
   __TEXT.__swift5_assocty: 0x808
-  __TEXT.__constg_swiftt: 0x648
-  __TEXT.__swift5_fieldmd: 0x9b0
-  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__constg_swiftt: 0x6ac
+  __TEXT.__swift5_fieldmd: 0x9e8
+  __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x420
-  __TEXT.__swift5_types: 0x8c
-  __TEXT.__swift_as_entry: 0xec
-  __TEXT.__swift_as_ret: 0x13c
-  __TEXT.__swift_as_cont: 0x248
-  __TEXT.__swift5_capture: 0xbc
+  __TEXT.__swift5_types: 0x94
+  __TEXT.__swift_as_entry: 0xf0
+  __TEXT.__swift_as_ret: 0x144
+  __TEXT.__swift_as_cont: 0x250
+  __TEXT.__swift5_capture: 0xc0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x14d8
-  __TEXT.__eh_frame: 0x26a8
-  __DATA_CONST.__const: 0x1c28
+  __TEXT.__unwind_info: 0x1510
+  __TEXT.__eh_frame: 0x27a0
+  __DATA_CONST.__const: 0x1ca8
   __DATA_CONST.__cfstring: 0x200
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0xc0
-  __DATA_CONST.__objc_doubleobj: 0x380
+  __DATA_CONST.__objc_doubleobj: 0x3a0
   __DATA_CONST.__objc_intobj: 0x780
   __DATA_CONST.__objc_floatobj: 0x20
-  __DATA_CONST.__auth_got: 0xda0
-  __DATA_CONST.__got: 0x518
-  __DATA_CONST.__auth_ptr: 0x9f8
-  __DATA.__objc_const: 0x1d50
-  __DATA.__objc_selrefs: 0xcf0
+  __DATA_CONST.__auth_got: 0xdd8
+  __DATA_CONST.__got: 0x540
+  __DATA_CONST.__auth_ptr: 0xa08
+  __DATA.__objc_const: 0x1e98
+  __DATA.__objc_selrefs: 0xd70
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x140
-  __DATA.__data: 0x19e0
+  __DATA.__data: 0x1bf8
   __DATA.__bss: 0x84b0
   __DATA.__common: 0x120
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/Frameworks/_GeoToolbox_AppIntents.framework/_GeoToolbox_AppIntents
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
+  - /System/Library/PrivateFrameworks/MapsSync.framework/MapsSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1473
-  Symbols:   249
-  CStrings:  1241
+  Functions: 1489
+  Symbols:   254
+  CStrings:  1271
 
Sections:
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_entry : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
Symbols:
+ _OBJC_CLASS_$_GEOFeatureStyleAttributes
+ _OBJC_CLASS_$_GEOIdealTransportTypeFinder
+ _OBJC_CLASS_$_MKMapCamera
+ _OBJC_CLASS_$_MKMapSnapshotCustomFeatureAnnotation
+ _OBJC_CLASS_$_MKMapSnapshotOptions
+ _OBJC_CLASS_$_MKMapSnapshotter
+ _swift_getErrorValue
+ _swift_initStackObject
+ _swift_retain_x26
- _OBJC_CLASS_$_MKAnnotatedMapSnapshotter
- _objc_retain_x27
- _objc_retain_x9
- _swift_willThrowTypedImpl
CStrings:
+ "@\"VKCustomFeature\"16@0:8"
+ "CalculateETAIntent: Creating MKMapSnapshotter"
+ "CalculateETAIntent: Failed to fetch favorite item for GEOMapItem: %@. Error=%s."
+ "IntentsUtil.mapItem: MKMapItemRequest failed: %s — rethrowing as unableToResolveLocation"
+ "IntentsUtil.mapItem: MKMapService.shared() unavailable — throwing unableToFetchMapService"
+ "MKCustomFeatureAnnotation"
+ "Td,?,N"
+ "T{?=dd},N"
+ "VKAnnotation"
+ "VKCustomFeatureAnnotation"
+ "_TtC11MapsIntentsP33_6597ACF131A204F9DE7B67B3B7CF945219ResourceBundleClass"
+ "_setCustomFeatureAnnotations:"
+ "_setSearchResultsType:"
+ "calculateETA(from:to:departureTime:resolvedTransportationType:)"
+ "cameraLookingAtMapItem:forViewSize:allowPitch:"
+ "course"
+ "customFeatureAnnotationForMapItem:styleAttributes:"
+ "favoriteType"
+ "feature"
+ "homeStyleAttributes"
+ "idealTransportTypeForCoordinates:count:mapType:"
+ "initWithOptions:"
+ "resolveTransportationType: explicit type=%s, passing through"
+ "resolveTransportationType: idealTTF resolved .any → %s"
+ "resolveTransportationType: insufficient coordinates (%ld), returning .any"
+ "schoolStyleAttributes"
+ "setCamera:"
+ "setCoordinate:"
+ "setCourse:"
+ "setSize:"
+ "showsBalloonCallout"
+ "v32@0:8{?=dd}16"
+ "workStyleAttributes"
- "CalculateETAIntent: Creating MKAnnotatedMapSnapshotter"
- "calculateETA(from:to:departureTime:)"
- "initWithMapItems:mapSize:useSnapshotService:"

```
