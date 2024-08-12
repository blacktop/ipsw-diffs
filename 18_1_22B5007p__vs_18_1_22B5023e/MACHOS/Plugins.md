## Plugins

> `/System/Library/PrivateFrameworks/VisualUnderstanding.framework/Plugins.bundle/Plugins`

```diff

-58.3.0.0.0
-  __TEXT.__text: 0x1a1e4
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__const: 0x1e8
-  __TEXT.__cstring: 0x681
-  __TEXT.__constg_swiftt: 0x17c
-  __TEXT.__swift5_typeref: 0x325
-  __TEXT.__swift5_reflstr: 0x5f
-  __TEXT.__swift5_fieldmd: 0x68
-  __TEXT.__oslogstring: 0xebe
-  __TEXT.__objc_methname: 0x5a0
+59.7.0.0.0
+  __TEXT.__text: 0x1b224
+  __TEXT.__auth_stubs: 0xd00
+  __TEXT.__const: 0x228
+  __TEXT.__cstring: 0x701
+  __TEXT.__constg_swiftt: 0x1cc
+  __TEXT.__swift5_typeref: 0x335
+  __TEXT.__swift5_reflstr: 0xdf
+  __TEXT.__swift5_fieldmd: 0x98
+  __TEXT.__oslogstring: 0x114e
+  __TEXT.__objc_methname: 0x5f4
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x8
   __TEXT.__objc_classname: 0x3b
   __TEXT.__objc_methtype: 0x100
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x2c0
-  __TEXT.__eh_frame: 0x768
-  __DATA_CONST.__auth_got: 0x670
-  __DATA_CONST.__got: 0x1c0
+  __TEXT.__unwind_info: 0x2d8
+  __TEXT.__eh_frame: 0x7a0
+  __DATA_CONST.__auth_got: 0x680
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0xa0
-  __DATA_CONST.__const: 0x368
+  __DATA_CONST.__const: 0x3a8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x528
-  __DATA.__objc_selrefs: 0x1a8
+  __DATA.__objc_const: 0x5a8
+  __DATA.__objc_selrefs: 0x1c0
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x620
-  __DATA.__common: 0x10
+  __DATA.__data: 0x6c0
+  __DATA.__common: 0x18
   __DATA.__bss: 0x100
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/Vision.framework/Vision
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /System/Library/PrivateFrameworks/VisualUnderstanding.framework/VisualUnderstanding

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 153
-  Symbols:   147
-  CStrings:  195
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 158
+  Symbols:   157
+  CStrings:  208
 
Symbols:
+ _OBJC_CLASS_$_BGSystemTaskCheckpoints
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _swift_endAccess
CStrings:
+ "Adding a new entity to the entityNumTopModalitiesMap, adding: %!l(MISSING)d"
+ "Readiness check passed, attempting to call into BackgroundSystemTasksCheckpoints"
+ "Readiness checkpoint not passed. Entity %!l(MISSING)d does not have enough looks. Found %!l(MISSING)d looks, but needed: %!l(MISSING)d"
+ "Readiness checkpoint not passed. Entity %!l(MISSING)d was not found in entity to top modalities mapping"
+ "Readiness checkpoint not passed. Not enough tagged entities found for the known/important people from Photos. VU found: %!l(MISSING)d tagged entities in the VUGallery, when the minimum required amount is: %!l(MISSING)d"
+ "Readiness checkpoint not passed. UUID %!s(MISSING) isn't valid"
+ "VUPersonalizationPluginFeatureId"
+ "entityNumTopModalitiesMap"
+ "initWithShort:"
+ "readinessLooksCount"
+ "readinessPersonCount"
+ "reportFeatureCheckpoint:forFeature:error:"
+ "setIncludedDetectionTypes:"

```
