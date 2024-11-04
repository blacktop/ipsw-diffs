## Plugins

> `/System/Library/PrivateFrameworks/VisualUnderstanding.framework/Plugins.bundle/Plugins`

```diff

-61.1.0.0.0
-  __TEXT.__text: 0x1b2ec
-  __TEXT.__auth_stubs: 0xd00
-  __TEXT.__const: 0x228
-  __TEXT.__cstring: 0x701
-  __TEXT.__constg_swiftt: 0x1cc
-  __TEXT.__swift5_typeref: 0x335
-  __TEXT.__swift5_reflstr: 0xdf
-  __TEXT.__swift5_fieldmd: 0x98
-  __TEXT.__oslogstring: 0x108e
-  __TEXT.__objc_methname: 0x5f4
+63.0.0.0.0
+  __TEXT.__text: 0xe040
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__const: 0x1b8
+  __TEXT.__cstring: 0x625
+  __TEXT.__constg_swiftt: 0x15c
+  __TEXT.__swift5_typeref: 0x1f1
+  __TEXT.__swift5_reflstr: 0x3f
+  __TEXT.__swift5_fieldmd: 0x5c
+  __TEXT.__oslogstring: 0xd9e
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
   __TEXT.__objc_classname: 0x3b
+  __TEXT.__objc_methname: 0x401
   __TEXT.__objc_methtype: 0x100
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x2d8
-  __TEXT.__eh_frame: 0x7a0
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x1d8
-  __DATA_CONST.__auth_ptr: 0xa0
-  __DATA_CONST.__const: 0x3b8
+  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__eh_frame: 0x340
+  __DATA_CONST.__auth_got: 0x4f0
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__auth_ptr: 0x90
+  __DATA_CONST.__const: 0x328
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x5a8
-  __DATA.__objc_selrefs: 0x1c0
+  __DATA.__objc_const: 0x508
+  __DATA.__objc_selrefs: 0xe0
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x6c0
-  __DATA.__common: 0x18
+  __DATA.__data: 0x550
+  __DATA.__common: 0x10
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Photos.framework/Photos
-  - /System/Library/Frameworks/Vision.framework/Vision
-  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 158
-  Symbols:   157
-  CStrings:  206
+  Functions: 102
+  Symbols:   138
+  CStrings:  163
 
Symbols:
- _CGRectGetHeight
- _CGRectGetMaxX
- _CGRectGetMaxY
- _CGRectGetMinX
- _CGRectGetMinY
- _CGRectGetWidth
- _OBJC_CLASS_$_BGSystemTaskCheckpoints
- _OBJC_CLASS_$_NSNumber
- _OBJC_CLASS_$_PHAsset
- _OBJC_CLASS_$_PHFace
- _OBJC_CLASS_$_PHMoment
- _PHAssetPropertySetPhotosInfoPanelExtended
- _VNImageRectForNormalizedRect
- _objc_retain_x10
- _objc_retain_x28
- _swift_dynamicCastClass
- _swift_endAccess
- _swift_unknownObjectRelease
- _swift_unknownObjectRetain_n
CStrings:
+ "Personalization plugin updated"
- "Adding a new entity to the entityNumTopModalitiesMap, adding: %!l(MISSING)d"
- "Attempting to cache personalization data for %!l(MISSING)d tags"
- "Caching personalization for tag %!s(MISSING)..."
- "Division by zero"
- "Division results in an overflow"
- "More than %!l(MISSING)d entities to update, skipping the next %!l(MISSING)d"
- "No highly scoring face available for %!l(MISSING)d, falling back to the highest quality..."
- "Readiness check passed, attempting to call into BackgroundSystemTasksCheckpoints"
- "Readiness checkpoint not passed. Found %!l(MISSING)d top entities in VU, of which %!l(MISSING)d had more than or equal to %!l(MISSING)d top looks. Requirements to pass checkpoint are: at least %!l(MISSING)d entities with at least %!l(MISSING)d each."
- "Skipping %!s(MISSING) as cache already up to date"
- "Swift/IntegerTypes.swift"
- "UUID %!s(MISSING) isn't valid, cannot add UUID to entities list for readiness checkpoint"
- "VUPersonalizationPluginFeatureId"
- "blurScore"
- "centerX"
- "centerY"
- "creationDate"
- "entityNumTopModalitiesMap"
- "eyesState"
- "fetchAssetsGroupedByFaceUUIDForFaces:fetchPropertySets:"
- "fetchFacesWithVuObservationIDs:options:"
- "fetchMomentUUIDByAssetUUIDForAssetUUIDs:options:"
- "generativeAIType"
- "glassesType"
- "hasFaceMask"
- "hasSmile"
- "headgearType"
- "initWithInteger:"
- "initWithShort:"
- "isMediaSubtype:"
- "isScreenRecording"
- "photosInfoPanelExtendedProperties"
- "poseType"
- "poseYaw"
- "readinessLooksCount"
- "readinessPersonCount"
- "reportFeatureCheckpoint:forFeature:error:"
- "roll"
- "setIncludedDetectionTypes:"
- "size"
- "sourceHeight"
- "sourceWidth"
- "uuid"
- "vuObservationID"

```
