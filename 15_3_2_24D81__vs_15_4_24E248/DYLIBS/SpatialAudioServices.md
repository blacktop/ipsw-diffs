## SpatialAudioServices

> `/System/Library/PrivateFrameworks/SpatialAudioServices.framework/Versions/A/SpatialAudioServices`

```diff

-23.1.0.0.0
-  __TEXT.__text: 0x1114
+24.26.0.0.0
+  __TEXT.__text: 0x1168
   __TEXT.__auth_stubs: 0x190
-  __TEXT.__objc_methlist: 0x170
+  __TEXT.__objc_methlist: 0x1bc
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x2c
   __TEXT.__cstring: 0x381
-  __TEXT.__unwind_info: 0xd8
+  __TEXT.__unwind_info: 0xe0
   __TEXT.__objc_classname: 0x88
   __TEXT.__objc_methname: 0x440
   __TEXT.__objc_methtype: 0x112

   __AUTH_CONST.__auth_got: 0xd8
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x3b8
+  __AUTH_CONST.__objc_const: 0x340
   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x20
   __DATA.__data: 0x1f0

   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7A73366-DAF7-3A23-8DE2-E48FAED90A1E
-  Functions: 43
-  Symbols:   162
+  UUID: 7CFEA792-2FAB-3FAB-8EEF-68D7A96445CC
+  Functions: 53
+  Symbols:   172
   CStrings:  101
 
Symbols:
+ -[SpatialAudioClient _ensureXPCStarted].cold.1
+ -[SpatialAudioClient _fetchSpatialSoundProfileRecordWithCompletion:].cold.1
+ -[SpatialAudioClient _interrupted].cold.1
+ -[SpatialAudioClient _invalidated].cold.1
+ -[SpatialAudioClient _invalidated].cold.2
+ -[SpatialAudioClient isSystemContext].cold.1
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __32-[SpatialAudioClient invalidate]_block_invoke.cold.1
+ __68-[SpatialAudioClient _fetchSpatialSoundProfileRecordWithCompletion:]_block_invoke.cold.1
Functions:
~ __67-[SpatialAudioClient fetchSpatialSoundProfileRecordWithCompletion:]_block_invoke.1 : 216 -> 204
~ -[SpatialAudioClient _fetchSpatialSoundProfileRecordWithCompletion:] : 500 -> 472
~ ___68-[SpatialAudioClient _fetchSpatialSoundProfileRecordWithCompletion:]_block_invoke : 184 -> 148
~ -[SpatialAudioClient _ensureXPCStarted] : 696 -> 692
~ -[SpatialAudioClient _interrupted] : 164 -> 136
~ ___32-[SpatialAudioClient invalidate]_block_invoke : 196 -> 160
~ -[SpatialAudioClient _invalidated] : 324 -> 268
~ -[SpatialAudioClient isSystemContext] : 68 -> 56

```
