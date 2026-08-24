## Cinematic

> `/System/Library/Frameworks/Cinematic.framework/Versions/A/Cinematic`

```diff

-558.0.0.0.0
-  __TEXT.__text: 0x1521c
+560.21.2.0.0
+  __TEXT.__text: 0x152d0
   __TEXT.__objc_methlist: 0xeb4
   __TEXT.__cstring: 0x359
   __TEXT.__const: 0x9d8
-  __TEXT.__oslogstring: 0x927
-  __TEXT.__gcc_except_tab: 0x290
+  __TEXT.__oslogstring: 0x98f
+  __TEXT.__gcc_except_tab: 0x2c0
   __TEXT.__constg_swiftt: 0x5b0
   __TEXT.__swift5_typeref: 0x332
   __TEXT.__swift5_reflstr: 0x22d

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 769
+  Functions: 771
   Symbols:   1291
-  CStrings:  82
+  CStrings:  83
 
Functions:
~ ____CNLoadMetadataTrackForVideoTrack_block_invoke : 1204 -> 1336
~ _OUTLINED_FUNCTION_1 : 16 -> 20
+ _OUTLINED_FUNCTION_2
~ __65+[CNAssetInfo _loadFromAsset:requireDisparity:completionHandler:]_block_invoke.20.cold.1 : 60 -> 52
~ +[CNAssetInfo loadFromCinematicVideoTracks:requireDisparity:error:].cold.2 : 60 -> 52
~ +[CNAssetInfo loadFromCinematicVideoTracks:requireDisparity:error:].cold.3 : 64 -> 56
~ ___CNLoadMetadataTrackForVideoTrack_block_invoke.cold.1 : 68 -> 52
+ ___CNLoadMetadataTrackForVideoTrack_block_invoke.cold.2
CStrings:
+ "Warning: Cannot find associated metadata track. Using last found instance with correct tract identifier"
```
