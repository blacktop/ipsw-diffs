## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-302.100.0.0.0
-  __TEXT.__text: 0x90348
+304.1.2.100.0
+  __TEXT.__text: 0x904a0
   __TEXT.__auth_stubs: 0x1c60
-  __TEXT.__objc_methlist: 0xa5a4
+  __TEXT.__objc_methlist: 0xa5b4
   __TEXT.__const: 0xb44
   __TEXT.__oslogstring: 0x3711
-  __TEXT.__cstring: 0x5e32
-  __TEXT.__gcc_except_tab: 0x1650
+  __TEXT.__cstring: 0x5e72
+  __TEXT.__gcc_except_tab: 0x165c
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__swift5_typeref: 0x502
   __TEXT.__constg_swiftt: 0x1d4

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x2728
+  __TEXT.__unwind_info: 0x2730
   __TEXT.__objc_classname: 0x1789
-  __TEXT.__objc_methname: 0x18d35
-  __TEXT.__objc_methtype: 0x3e26
-  __TEXT.__objc_stubs: 0x10ec0
+  __TEXT.__objc_methname: 0x18d6b
+  __TEXT.__objc_methtype: 0x3e3d
+  __TEXT.__objc_stubs: 0x10ee0
   __DATA_CONST.__got: 0xe30
   __DATA_CONST.__const: 0x2650
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5600
+  __DATA_CONST.__objc_selrefs: 0x5608
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x3f0
   __DATA_CONST.__objc_arraydata: 0x1b0
   __AUTH_CONST.__auth_got: 0xe40
   __AUTH_CONST.__const: 0xf80
-  __AUTH_CONST.__cfstring: 0x6880
+  __AUTH_CONST.__cfstring: 0x68c0
   __AUTH_CONST.__objc_const: 0x1df40
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x318

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A5D91A59-906A-37A2-BD03-F090F742065A
-  Functions: 3886
-  Symbols:   13919
-  CStrings:  6746
+  UUID: 2AE21498-FBDF-3888-BC29-9221A5B92869
+  Functions: 3887
+  Symbols:   13922
+  CStrings:  6752
 
Symbols:
+ -[PUIPosterSnapshotBundleBuilder buildWithOutputURL:diskFormat:finalizedMutator:error:]
+ ___45-[PUIPosterSnapshotter _teardownAllSnapshots]_block_invoke.39
+ ___54-[PUIPosterSnapshotter _mainQueue_lock_startExtension]_block_invoke.42
+ ___54-[PUIPosterSnapshotter _mainQueue_lock_startExtension]_block_invoke.43
+ ___54-[PUIPosterSnapshotter _mainQueue_lock_startExtension]_block_invoke.43.cold.1
+ ___54-[PUIPosterSnapshotter _mainQueue_lock_startExtension]_block_invoke.43.cold.2
+ ___78-[PUIPosterSnapshotter enqueueSnapshotRequest:destinationProvider:completion:]_block_invoke.37
+ ___87-[PUIPosterSnapshotBundleBuilder buildWithOutputURL:diskFormat:finalizedMutator:error:]_block_invoke
+ ___87-[PUIPosterSnapshotBundleBuilder buildWithOutputURL:diskFormat:finalizedMutator:error:]_block_invoke.119
+ ___98-[PUIPosterSnapshotter sceneSnapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:]_block_invoke.40
+ ___block_descriptor_48_e8_32s40w_e33_v16?0"FBSMutableSceneSettings"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e35_v16?0"FBSMutableSceneParameters"8lw40l8s32l8
+ _objc_msgSend$buildWithOutputURL:diskFormat:finalizedMutator:error:
- ___45-[PUIPosterSnapshotter _teardownAllSnapshots]_block_invoke.33
- ___54-[PUIPosterSnapshotter _mainQueue_lock_startExtension]_block_invoke.36
- ___54-[PUIPosterSnapshotter _mainQueue_lock_startExtension]_block_invoke.37
- ___54-[PUIPosterSnapshotter _mainQueue_lock_startExtension]_block_invoke.37.cold.1
- ___54-[PUIPosterSnapshotter _mainQueue_lock_startExtension]_block_invoke.37.cold.2
- ___70-[PUIPosterSnapshotBundleBuilder buildWithOutputURL:diskFormat:error:]_block_invoke
- ___70-[PUIPosterSnapshotBundleBuilder buildWithOutputURL:diskFormat:error:]_block_invoke.119
- ___78-[PUIPosterSnapshotter enqueueSnapshotRequest:destinationProvider:completion:]_block_invoke.31
- ___98-[PUIPosterSnapshotter sceneSnapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:]_block_invoke.34
- ___block_descriptor_48_e8_32s40w_e33_v16?0"FBSMutableSceneSettings"8ls32l8w40l8
- ___block_descriptor_48_e8_32s40w_e35_v16?0"FBSMutableSceneParameters"8ls32l8w40l8
Functions:
~ -[PUIPosterSnapshotter enqueueSnapshotRequest:destinationProvider:completion:] : 944 -> 1072
~ -[_PUIPosterEnqueuedSnapshot applyToSceneSettings:] : 124 -> 136
~ -[_PUIPosterSnapshotCapture _captureLevelSet:error:] : 2184 -> 2152
~ ___52-[_PUIPosterSnapshotCapture _captureLevelSet:error:]_block_invoke.79 : 576 -> 588
~ -[PUIPosterSnapshotBundleBuilder buildWithOutputURL:diskFormat:error:] : 2076 -> 12
+ -[PUIPosterSnapshotBundleBuilder buildWithOutputURL:diskFormat:finalizedMutator:error:]
~ -[PUIPosterSceneSnapshotter _mainQueue_setupScene] : 956 -> 1100
~ -[PUIPosterSceneSnapshotter _mainQueue_setupScene].cold.2 : 140 -> 136
CStrings:
+ "@48@0:8@16@24@?32o^@40"
+ "Snapshot info was nil; bailing on setup scene"
+ "buildWithOutputURL:diskFormat:finalizedMutator:error:"
+ "request was nil"

```
