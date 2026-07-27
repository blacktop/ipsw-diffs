## ExtensionShim

> `/System/Library/Video/Professional Video Workflow Plug-Ins/ExtensionShim.bundle/Contents/MacOS/ExtensionShim`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-3330.10.1.0.0
-  __TEXT.__text: 0xc090
-  __TEXT.__auth_stubs: 0x610
+3330.13.2.0.0
+  __TEXT.__text: 0xa164
+  __TEXT.__auth_stubs: 0x5b0
   __TEXT.__objc_stubs: 0x10c0
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x18e0
-  __TEXT.__oslogstring: 0x74f
+  __TEXT.__const: 0x50
+  __TEXT.__cstring: 0x3dd
   __TEXT.__objc_classname: 0xa
-  __TEXT.__gcc_except_tab: 0x1e4
+  __TEXT.__gcc_except_tab: 0x188
   __TEXT.__objc_methname: 0xe92
   __TEXT.__objc_methtype: 0xad
-  __TEXT.__unwind_info: 0x260
-  __DATA_CONST.__auth_got: 0x318
+  __TEXT.__unwind_info: 0x248
+  __DATA_CONST.__auth_got: 0x2e8
   __DATA_CONST.__got: 0x318
   __DATA_CONST.__const: 0x760
   __DATA_CONST.__cfstring: 0x180

   __DATA.__objc_selrefs: 0x4c0
   __DATA.__data: 0x60
   __DATA.__bss: 0x138
-  __DATA.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /System/Library/Frameworks/VideoToolbox.framework/Versions/A/VideoToolbox
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 213
-  Symbols:   204
-  CStrings:  361
+  Functions: 198
+  Symbols:   198
+  CStrings:  204
 
Symbols:
+ _FigSignalErrorAtGM
- _CMTimeGetSeconds
- _FigCFCopyCompactDescription
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _os_log_type_enabled
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CZB9Hh/Sources/CoreMedia_MediaExtension/Sources/MediaExtension/ExtensionShimBundle/ExtensionDecoderWrapper.m %s: Extension decoder isReadyForMoreMediaData is NO but no frame is pending"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CZB9Hh/Sources/CoreMedia_MediaExtension/Sources/MediaExtension/ExtensionShimBundle/ExtensionDecoderWrapper.m %s: still waiting for extension decoder after %d seconds"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CZB9Hh/Sources/CoreMedia_MediaExtension/Sources/MediaExtension/ExtensionShimBundle/ExtensionRAWProcessorWrapper.m %s: Extension processor isReadyForMoreMediaData is NO but no frame is pending"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CZB9Hh/Sources/CoreMedia_MediaExtension/Sources/MediaExtension/ExtensionShimBundle/ExtensionRAWProcessorWrapper.m %s: still waiting for extension processor after %d seconds"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.CZB9Hh/Sources/CoreMedia_MediaExtension/Sources/MediaExtension/ExtensionShimBundle/ExtensionRAWProcessorWrapper.m %s: unrecognized property key: %@"
- "<<<< MEFormatReaderWrapper >>>> %s: (%p)"
- "<<<< MEFormatReaderWrapper >>>> %s: (%p) %@"
- "<<<< MEFormatReaderWrapper >>>> %s: (%p) %@ -> err %d, %@"
- "<<<< MEFormatReaderWrapper >>>> %s: (%p) -> %@"
- "<<<< MEFormatReaderWrapper >>>> %s: (%p) -> err %d, %@"
- "<<<< MEFormatReaderWrapper >>>> %s: (%p) flagsIn %#x -> err %d, flagsOut %#x"
- "<<<< MEFormatReaderWrapper >>>> %s: (%p) pts %1.3f -> err %d, %@"
- "CFDictionaryCreate failed"
- "Cannot copy a  sampelCursor"
- "Extension factory returned no error but NULL decoder instance"
- "Extension factory returned no error but NULL processor instance"
- "ExtensionDecoderWrapper.m"
- "ExtensionDecoderWrapper_CopyProperty"
- "ExtensionDecoderWrapper_CopySupportedPropertyDictionary"
- "ExtensionDecoderWrapper_CreateInstance"
- "ExtensionDecoderWrapper_DecodeFrame"
- "ExtensionDecoderWrapper_SetProperty"
- "ExtensionDecoderWrapper_StartSession"
- "ExtensionDecoderWrapper_createSupportedPropertyDictionary"
- "ExtensionFormatReaderWrapper.m"
- "ExtensionRAWProcessorWrapper.m"
- "ExtensionRAWProcessorWrapper_CopyProperty"
- "ExtensionRAWProcessorWrapper_CopySupportedPropertyDictionary"
- "ExtensionRAWProcessorWrapper_CreateInstance"
- "ExtensionRAWProcessorWrapper_ProcessFrame"
- "ExtensionRAWProcessorWrapper_SetProcessingParameters"
- "ExtensionRAWProcessorWrapper_SetProperty"
- "ExtensionRAWProcessorWrapper_StartSession"
- "ExtensionRAWProcessorWrapper_createSupportedPropertyDictionary"
- "Failed to create CFArrayMutable"
- "Failed to create MTPluginMetadataItem"
- "FigDerivedObjectCreate failed"
- "List parameter ID not found in List"
- "List parameter ID not found in List after validation"
- "MTPluginFormatReaderVTable NULL"
- "MTPluginTrackReaderVTable NULL"
- "NULL dependencyInfoOut"
- "NULL extendedSampleDependencyAttributesOut"
- "NULL flagsOut"
- "NULL formatReader"
- "NULL meFormatReader"
- "NULL meFormatReaderExtension"
- "NULL mePluginByteSource"
- "NULL metadata array"
- "NULL newSampleCursorOut"
- "NULL playableHorizonOut"
- "NULL postDecodeProcessingMetadataOut"
- "NULL primaryByteSource"
- "NULL refinementData"
- "NULL sampleCursor"
- "NULL sampleCursor1"
- "NULL sampleCursor2"
- "NULL sampleCursorX"
- "NULL sampleCursorY"
- "NULL sampleTimingInfoOut"
- "NULL supportedPropertyDictionaryOut"
- "NULL syncInfoOut"
- "NULL trackArrayOut"
- "No Extension Factory"
- "No matrixArrayOut"
- "No propertyValueOut"
- "Out of range Float parameter value"
- "Out of range Integer parameter value"
- "Unrecognized parameter key"
- "can not find metatdata info"
- "can not get file info"
- "cannot set disabled parameter"
- "copy track info failed"
- "copyInfoGroup failed"
- "couldn't allocate ReducedResolution dictionary"
- "create3x3MatrixArrayFromCGAffineTransform"
- "decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource failed"
- "editOut NULL"
- "empty metadata array"
- "err"
- "err = kVTAllocationFailedErr"
- "err = kVTParameterErr"
- "err = kVTVideoDecoderUnsupportedDataFormatErr"
- "estimatedSampleLocationReturningError failed"
- "extendedSampleDependencyAttributes allocation failed"
- "extensionErrorToMTError( [error code] )"
- "extensionErrorToMTError( error.code )"
- "formatReader NULL"
- "getChunkDetailsReturningError failed"
- "getFileInfoGroup failed"
- "getSampleLocationReturningError failed"
- "invalid reduced resolution"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_PropertyNotFound"
- "kMTPluginFormatReaderError_AllocationFailure"
- "kMTPluginFormatReaderError_InternalFailure"
- "kMTPluginFormatReaderError_InvalidParameter"
- "kMTPluginFormatReaderError_ParsingFailure"
- "kMTPluginFormatReaderError_PropertyNotSupported"
- "kMTPluginFormatReaderError_UnsupportedFeature"
- "kVTAllocationFailedErr"
- "kVTPropertyNotSupportedErr"
- "makeSampleCursorAtPresentationTimeStamp failed"
- "makeSampleCursorGroup failed"
- "metadataNSArrayToCFArray"
- "newSampleCursorOut NULL"
- "not supported parameter"
- "objcWrapperPluginFormatReader_CopyInfoAsync"
- "objcWrapperPluginFormatReader_CopyProperty"
- "objcWrapperPluginFormatReader_CopyTrackArray"
- "objcWrapperPluginFormatReader_CreateInstance"
- "objcWrapperPluginFormatReader_Finalize"
- "objcWrapperPluginFormatReader_ParseAdditionalFragments"
- "objcWrapperPluginFormatReader_createInternal"
- "objcWrapperPluginSampleCursor_CompareInDecodeOrder"
- "objcWrapperPluginSampleCursor_Copy"
- "objcWrapperPluginSampleCursor_CopyChunkDetails"
- "objcWrapperPluginSampleCursor_CopyDebugDescription"
- "objcWrapperPluginSampleCursor_CopyExtendedSampleDependencyAttributes"
- "objcWrapperPluginSampleCursor_CopyFormatDescription"
- "objcWrapperPluginSampleCursor_CopyPostDecodeProcessingMetadata"
- "objcWrapperPluginSampleCursor_CopySampleLocation"
- "objcWrapperPluginSampleCursor_CopyUnrefinedSampleLocation"
- "objcWrapperPluginSampleCursor_CreateSampleBuffer"
- "objcWrapperPluginSampleCursor_Finalize"
- "objcWrapperPluginSampleCursor_GetDependencyInfo"
- "objcWrapperPluginSampleCursor_GetPlayableHorizon"
- "objcWrapperPluginSampleCursor_GetSampleTiming"
- "objcWrapperPluginSampleCursor_GetSyncInfo"
- "objcWrapperPluginSampleCursor_RefineSampleLocation"
- "objcWrapperPluginSampleCursor_StepByDecodeTime"
- "objcWrapperPluginSampleCursor_StepByPresentationTime"
- "objcWrapperPluginSampleCursor_StepInDecodeOrderAndReportStepsTaken"
- "objcWrapperPluginSampleCursor_StepInPresentationOrderAndReportStepsTaken"
- "objcWrapperPluginSampleCursor_TestReorderingBoundary"
- "objcWrapperPluginTrackReader_CopyInfoAsync"
- "objcWrapperPluginTrackReader_CopyProperty"
- "objcWrapperPluginTrackReader_CreateCursorInternal"
- "objcWrapperPluginTrackReader_Finalize"
- "objcWrapperPluginTrackReader_GetTrackEditCount"
- "objcWrapperPluginTrackReader_GetTrackEditWithIndex"
- "objcWrapperPluginTrackReader_GetTrackInfo"
- "objcWrapperPluginTrackReader_MakeSampleCursorAsync"
- "objcWrapperPluginTrackReader_createInternal"
- "parseAdditionalFragments failed"
- "parseFragmentsGroup allocation failed"
- "propertyKey NULL"
- "propertyValueOut NULL"
- "refineSampleLocation failed"
- "rwLock allocation failed"
- "semaphore creation failed"
- "should not happen !!! : trackInfo is nil"
- "stepCursorDispatchGroup allocation failed"
- "there is no track in the movie file"
- "trackArray allocation failed"
- "trackReader NULL"
- "unrecognised property key"
```
