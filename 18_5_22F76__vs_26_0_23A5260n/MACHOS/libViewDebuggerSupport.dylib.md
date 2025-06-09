## libViewDebuggerSupport.dylib

> `/usr/lib/libViewDebuggerSupport.dylib`

```diff

-71.0.0.0.0
-  __TEXT.__text: 0x2a4e8
-  __TEXT.__auth_stubs: 0x8f0
+73.0.0.0.0
+  __TEXT.__text: 0x2a3b4
+  __TEXT.__auth_stubs: 0x8d0
   __TEXT.__objc_methlist: 0x1204
   __TEXT.__const: 0xc8
   __TEXT.__cstring: 0x3c4c

   __TEXT.__swift5_reflstr: 0x19
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x3e8
+  __TEXT.__unwind_info: 0x3e0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x1a1
   __TEXT.__objc_methname: 0x20ad
   __TEXT.__objc_methtype: 0x2fd
   __TEXT.__objc_stubs: 0x2940
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__const: 0x138
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x220
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_selrefs: 0xc20
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x488
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x5be0
   __AUTH_CONST.__objc_const: 0x15a28

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
-  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
+  - /usr/lib/swift/libswiftMLCompute.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: A5E7C82B-9E3C-3C76-B3A9-9199C4290C38
+  UUID: 0090CECF-3381-3C36-AC58-3488EBAFC1F4
   Functions: 298
-  Symbols:   2089
+  Symbols:   2077
   CStrings:  1938
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMLCompute
+ __swift_FORCE_LOAD_$_swiftMLCompute_$_libViewDebuggerSupport
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_libViewDebuggerSupport
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_libViewDebuggerSupport
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_libViewDebuggerSupport
- _CFMakeCollectable
- __swift_FORCE_LOAD_$_swiftDataDetection
- __swift_FORCE_LOAD_$_swiftDataDetection_$_libViewDebuggerSupport
- __swift_FORCE_LOAD_$_swiftMetalKit
- __swift_FORCE_LOAD_$_swiftMetalKit_$_libViewDebuggerSupport
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_libViewDebuggerSupport
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_libViewDebuggerSupport
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_libViewDebuggerSupport
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_libViewDebuggerSupport
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_libViewDebuggerSupport
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_libViewDebuggerSupport
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_libViewDebuggerSupport
- _swift_retain
Functions:
~ +[DBGViewDebuggerSupport _collectSubviewInfoForView:encodeLayers:] : 376 -> 372
~ _$ss22__RawDictionaryStorageC4find_9hashValues10_HashTableV6BucketV6bucket_Sb5foundtx_SitSHRzlFSS_Tg5 : 228 -> 184
~ _$s10RealityKit6ARViewC22libViewDebuggerSupportE37fallback_debugHierarchyObjectsInGroup6withID2on10outOptionsSaySo05DebugJ15Object_Fallback_pGSgSS_ypSAySo12NSDictionaryCSgGtFZTf4nndd_n : 1008 -> 972
~ ___swift_destroy_boxed_opaque_existential_0 : 80 -> 76
~ _$ss17_NativeDictionaryV20_copyOrMoveAndResize8capacity12moveElementsySi_SbtFSS_Say22libViewDebuggerSupport38SpatialSceneDebugRepresentationWrapperCGTg5 : 808 -> 672
~ _$ss17_NativeDictionaryV8setValue_6forKey8isUniqueyq_n_xSbtFSS_Say22libViewDebuggerSupport38SpatialSceneDebugRepresentationWrapperCGTg5 : 364 -> 380
~ _$ss17_NativeDictionaryV4copyyyFSS_Say22libViewDebuggerSupport38SpatialSceneDebugRepresentationWrapperCGTg5 : 460 -> 360

```
