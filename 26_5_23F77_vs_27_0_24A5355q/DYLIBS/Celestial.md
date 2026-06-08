## Celestial

> `/System/Library/PrivateFrameworks/Celestial.framework/Celestial`

```diff

-3320.8.1.1.0
-  __TEXT.__text: 0xc30
-  __TEXT.__auth_stubs: 0x270
+3350.58.3.11.1
+  __TEXT.__text: 0x16c0
   __TEXT.__objc_methlist: 0xa0
-  __TEXT.__const: 0x4
-  __TEXT.__cstring: 0x509
+  __TEXT.__const: 0x10
+  __TEXT.__cstring: 0x57d
+  __TEXT.__oslogstring: 0x2cc
   __TEXT.__unwind_info: 0x98
-  __TEXT.__objc_classname: 0x25
-  __TEXT.__objc_methname: 0x2b8
-  __TEXT.__objc_methtype: 0x68
-  __TEXT.__objc_stubs: 0x220
-  __DATA_CONST.__got: 0x48
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xb0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x140
-  __AUTH_CONST.__cfstring: 0x8a0
+  __DATA_CONST.__got: 0x48
+  __AUTH_CONST.__cfstring: 0x8e0
   __AUTH_CONST.__objc_const: 0x168
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x68
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 67B91F1E-C6E0-35C8-B640-4BB3BC93D07D
+  UUID: 7D0DE5F4-84CF-384F-AE96-280194A66931
   Functions: 33
-  Symbols:   165
-  CStrings:  178
+  Symbols:   169
+  CStrings:  154
 
Symbols:
+ _FigNote_AllowInternalDefaultLogs
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _gFigCheckpointTrace
+ _os_log_type_enabled
- _objc_release_x20
- _objc_release_x21
- _objc_release_x28
Functions:
~ +[FigCheckpointSupport makeDictionary] : 8 -> 104
~ __computeCheckpoint : 1960 -> 4080
~ +[FigCheckpointSupport makeDictionaryForDevice:] : 8 -> 116
~ _FigAspenAddMPDataToJPEG : 4 -> 24
~ _FigAspenCopyMPDataFromJPEG : 4 -> 24
~ _FigAspenGetMPDataCountFromJPEG : 4 -> 24
~ _FigAspenCreateJPEGFromSbuf : 4 -> 24
~ _FigAspenCreateJPEGFromCVPixelBuffer : 4 -> 24
~ _FigAspenCreateJPEGFromIOSurface : 4 -> 24
~ _FigAspenCreateJPEGNativePixelFormatArray : 4 -> 24
~ _FigAspenCreateJPEGNativeSubsamplingArray : 4 -> 24
~ _FigAspenGetJPEGEncodeTiming : 4 -> 24
~ _FigAspenCreateJPEGOutputIOSurface : 4 -> 24
~ _FigCreateIOSurfaceFromJPEG : 4 -> 24
~ _FigCreateCGImageFromJPEG : 4 -> 24
~ _FigAspenDecodeJPEGIntoRGBSurface : 4 -> 24
~ _FigCreateCGImageFromIOSurface : 4 -> 24
~ _FigAspenCalculateOutputDimensionsForJPEG : 4 -> 24
~ _FigAspenCreateJPEGNativeDecodePixelFormatArray : 4 -> 24
~ _FigAspenGetMaximumOutputDimensionsForJPEG : 4 -> 24
~ _FigAspenShouldUseHardwareDecode : 4 -> 24
~ _FigAspenGetJPEGDecodeTiming : 4 -> 24
CStrings:
+ "<<<< FigCheckpointSupport >>>> %s: CHECKPOINT %@"
+ "<<<< FigCheckpointSupport >>>> %s: Finished creating audio codec list %@"
+ "<<<< FigCheckpointSupport >>>> %s: Finished creating complete list %@"
+ "<<<< FigCheckpointSupport >>>> %s: Finished creating video codec list %@"
+ "<<<< FigCheckpointSupport >>>> %s: Opening checkpointAdditionsSpecificationDictionary %@"
+ "<<<< FigCheckpointSupport >>>> %s: creating audio and video codec dictionary from input %@"
+ "<<<< FigCheckpointSupport >>>> %s: failed to create dictionary from %s"
+ "<<<< FigCheckpointSupport >>>> %s: specificationDictionary was NIL, audioSpecificationDictionary %@"
+ "<<<< FigCheckpointSupport >>>> %s: specificationDictionary was NIL, videoSpecificationDictionary %@"
+ "DeviceSupportsEnhancedAC3"
+ "MaxH264PlaybackLevel"
+ "RenderWideGamutImagesAtDisplayTime"
+ "_addSpecificationAdditions"
+ "_computeCheckpoint"
+ "_twiddleCheckpoint"
+ "checkpoint_trace"
+ "com.apple.coremedia"
- "4W7X4OWHjri5PGaAGsCWxw"
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@40@0:8@16@24@?32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24^@32@?40"
- "@?"
- "AVFileProcessor"
- "FigCheckpointSupport"
- "_percentComplete"
- "_progressBlock"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dateWithTimeIntervalSince1970:"
- "dealloc"
- "dictionary"
- "dictionaryWithObject:forKey:"
- "errorWithDomain:code:userInfo:"
- "f"
- "fileProcessor"
- "initWithDictionary:"
- "intValue"
- "jMiqevikb6QWeHOhvLsw6A"
- "kyszW/uUGJFTVNQwFaf6og"
- "makeDictionary"
- "makeDictionaryForDevice:"
- "numberWithUnsignedInt:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "processPurchasedItem:withAttributes:"
- "processPurchasedItem:withAttributes:progressBlock:"
- "processPurchasedItem:withAttributes:resultInfo:"
- "processPurchasedItem:withAttributes:resultInfo:progressBlock:"
- "removeObjectForKey:"
- "rentalInfo:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "sinfInfoFromFilePath:"
- "sinfsFromFilePath:"
- "stringByAppendingFormat:"
- "v16@0:8"

```
