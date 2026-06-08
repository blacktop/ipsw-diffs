## com.apple.photos.VideoConversionService

> `/System/Library/PrivateFrameworks/MediaConversionService.framework/XPCServices/com.apple.photos.VideoConversionService.xpc/com.apple.photos.VideoConversionService`

```diff

-852.0.102.0.0
-  __TEXT.__text: 0x212d4
-  __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_stubs: 0x5c00
-  __TEXT.__objc_methlist: 0x1bdc
+910.14.107.0.0
+  __TEXT.__text: 0x21a4c
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__objc_stubs: 0x61a0
+  __TEXT.__objc_methlist: 0x1cfc
   __TEXT.__dlopen_cstrs: 0xbe
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0xb54
-  __TEXT.__objc_methname: 0x781d
-  __TEXT.__oslogstring: 0x2d37
-  __TEXT.__cstring: 0x2f2a
-  __TEXT.__objc_classname: 0x365
-  __TEXT.__objc_methtype: 0xcf5
-  __TEXT.__unwind_info: 0x738
-  __DATA_CONST.__auth_got: 0x518
-  __DATA_CONST.__got: 0x758
-  __DATA_CONST.__const: 0xa58
-  __DATA_CONST.__cfstring: 0x2320
-  __DATA_CONST.__objc_classlist: 0x98
+  __TEXT.__const: 0x1c0
+  __TEXT.__gcc_except_tab: 0xb14
+  __TEXT.__objc_methname: 0x7ce8
+  __TEXT.__oslogstring: 0x2f03
+  __TEXT.__cstring: 0x34f6
+  __TEXT.__objc_classname: 0x361
+  __TEXT.__objc_methtype: 0xd1b
+  __TEXT.__unwind_info: 0x790
+  __DATA_CONST.__const: 0xbd0
+  __DATA_CONST.__cfstring: 0x2740
+  __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x28c8
-  __DATA.__objc_selrefs: 0x1b60
-  __DATA.__objc_ivar: 0x210
-  __DATA.__objc_data: 0x5f0
+  __DATA_CONST.__auth_got: 0x590
+  __DATA_CONST.__got: 0x758
+  __DATA.__objc_const: 0x29e8
+  __DATA.__objc_selrefs: 0x1c88
+  __DATA.__objc_ivar: 0x21c
+  __DATA.__objc_data: 0x640
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x58
+  __DATA.__bss: 0xc8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
+  - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/NeutrinoCore.framework/NeutrinoCore
   - /System/Library/PrivateFrameworks/PhotoFoundation.framework/PhotoFoundation
   - /System/Library/PrivateFrameworks/PhotoImaging.framework/PhotoImaging

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 118586D8-00CA-34E7-BD26-09EE171C2AFC
-  Functions: 616
-  Symbols:   405
-  CStrings:  2073
+  UUID: E2C1CCE3-8324-35EA-9CD3-76E102BF3804
+  Functions: 657
+  Symbols:   419
+  CStrings:  2201
 
Symbols:
+ _AnalyticsSendEvent
+ _CGSizeFromPFIntSize
+ _CMTimeRangeMake
+ _CMTimeRangeMakeFromDictionary
+ _IPAOrientationFromClockwiseRotation
+ _NSIsEmptyRect
+ _OBJC_CLASS_$_PFImageIODestinationOptionsBuilder
+ _PFIntSizeFromCGSize
+ _dispatch_block_create_with_qos_class
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _os_log_create
- _OBJC_CLASS_$_PFImageIOOptionsBuilder
- __os_log_default
CStrings:
+ "(none)"
+ "@60@0:8@16B24@28@36@44@52"
+ "Attempting to create empty destination output file at path %@ but parent directory creation failed: %{public}@"
+ "Configure for resumable export: configured=%d, resuming=%d, failure reason=%{public}@"
+ "Crop adjustment missing PAMediaConversionServiceAdjustmentCropKey and/or PAMediaConversionServiceAdjustmentOrientationKey"
+ "DeferredProcessingVideoTranscodingTask"
+ "Error creating adjustment from crop adjustment."
+ "Export progress to %@ for conversion task (%{public}@) %{public}@: %.1f"
+ "Export session to %@ for conversion task %{public}@ finished, status %ld (%@), conversion duration %.1fs, input asset duration %.1fs (%.1ffps), %.1f x realtime (%.1ffps)"
+ "Export was paused"
+ "FAILED"
+ "Failed to copy file from %@ to %@ with error %@"
+ "Missing scale parameters"
+ "PAMediaConversionResourceRolePartialResultsTemporaryStorage"
+ "PAMediaConversionServiceAdjustmentCropKey"
+ "PAMediaConversionServiceAdjustmentOrientationKey"
+ "PAMediaConversionServiceJobStatus"
+ "PAMediaConversionServiceOptionAVMetadataIncludeKeywordsKey"
+ "PAMediaConversionServiceOptionCropAdjustmentInformationKey"
+ "PAMediaConversionServiceOptionEnableOutputCorruptionDetectionHeuristicsKey"
+ "PAMediaConversionServiceOptionFormatConversionOnlyKey"
+ "PAMediaConversionServiceOptionMaximumLongSideLengthKey"
+ "PAMediaConversionServiceOptionOrientationKey"
+ "PAMediaConversionServiceOptionRotationAngleDegreesKey"
+ "PAMediaConversionServiceOptionTrimRangeKey"
+ "PAMediaConversionServiceOptionUseEmbeddedImageAsSourceKey"
+ "PAMediaConversionServiceOptionVideoDeferredProcessingRequiredKey"
+ "PICropAdjustmentKey"
+ "PIOrientationAdjustmentKey"
+ "Pausing resumable export. Partial results are in %@"
+ "SUCCESS"
+ "Starting job: %{public}@ preset: %{public}@"
+ "T@\"NSProgress\",&,V_xpcProgress"
+ "TB,V_isResumable"
+ "TB,V_shouldDeleteParentDirectoryOnDeallocation"
+ "Temporary cache directory for partial results specified for conversion task %{public}@: %{private}@"
+ "Temporary parent directory already removed at %@"
+ "Unable to delete temporary parent directory %@: %@"
+ "[BlastDoor] Failed to create temporary source location for blast door reference. Error: %@"
+ "_isResumable"
+ "_shouldDeleteParentDirectoryOnDeallocation"
+ "_xpcProgress"
+ "adjustmentInformationForCropAdjustmentInformation:sourceURLCollection:error:"
+ "com.apple.photos.mediaconversion"
+ "com.apple.photos.videoconversionservice.request"
+ "configurationFailureReason"
+ "configureColorSpaceFromRequestOptions:error:"
+ "configureCompositionController:sourceURLCollection:"
+ "configureForResumableExportWithCompletionHandler:"
+ "configureOrientationFromRequestOptions:"
+ "configurePhotosAdjustmentsFromRequestOptions:error:"
+ "configureScaleFactorFromRequestOptions:"
+ "configureWithRequestOptions:error:"
+ "conversionDurationSeconds"
+ "coreAnalyticsEventInformation"
+ "defaultDeallocationOptions"
+ "errorCode"
+ "errorDomain"
+ "exportSessionForInputAsset:presetName:partialResultsTemporaryDirectoryURL:"
+ "exportSessionWithAsset:presetName:"
+ "hasTrimTimeRange"
+ "imaging-utils"
+ "inputDurationSecondsBinned"
+ "inputFrameRate"
+ "inputHeight"
+ "inputWidth"
+ "isResumable"
+ "isResumingFromPreviousState"
+ "isResumptionConfigured"
+ "lowercaseString"
+ "markCompletionAndRetrieveClientRequestsForQueueEntry:didConvertSuccessfully:conversionOutputInformation:conversionOutputData:conversionOutputFileType:conversionError:"
+ "newComposition"
+ "newCompositionControllerWithComposition:"
+ "numberWithFloat:"
+ "optionsRequireVideoDeferredProcessing:"
+ "priority"
+ "processCompletedQueueEntry:didConvertSuccessfully:conversionOutputInformation:conversionOutputData:conversionOutputFileType:conversionError:"
+ "rectValue"
+ "resumable-video-processing"
+ "sendCoreAnalyticsEvent"
+ "service.tracking"
+ "service.utilities"
+ "service.video"
+ "serviceCIContext"
+ "setCropRect:"
+ "setDirectoryForTemporaryFiles:"
+ "setIsResumable:"
+ "setResourceURL:forRole:deallocationOptions:"
+ "setResumable:"
+ "setResumableIntermediateDirectory:"
+ "setShouldDeleteParentDirectoryOnDeallocation:"
+ "setSource:mediaType:"
+ "setTimeRange:"
+ "setXpcProgress:"
+ "shouldDeleteParentDirectoryOnDeallocation"
+ "substringFromIndex:"
+ "taskType"
+ "trimTimeRange"
+ "unknown"
+ "urlcollection"
+ "v16@?0@\"AVAssetExportSessionResumptionState\"8"
+ "v16@?0@\"PICropAdjustmentController\"8"
+ "v16@?0@\"PIOrientationAdjustmentController\"8"
+ "v40@0:8@16@24Q32"
+ "v60@0:8@16B24@28@36@44@52"
+ "xpcProgress"
+ "{?={?=qiIq}{?=qiIq}}16@0:8"
- "@68@0:8@16@24B32@36@44@52@60"
- "Attempting to create empty destination output file at path %@ but parent directory creation failed:"
- "Export progress for conversion task (%{public}@) %{public}@: %.1f"
- "Export session for conversion task %{public}@ finished, status %ld, conversion duration %.1fs, input asset duration %.1fs (%.1ffps), %.1f x realtime (%.1ffps)"
- "[BlastDoor] Failed to create tempory source location for blast door reference. Error: %@"
- "allValues"
- "exportSessionForInputAsset:presetName:"
- "filenameSummaryStringForDictionaryRepresentation:"
- "initWithAsset:presetName:"
- "markCompletionAndRetrieveClientRequestsForQueueEntry:resultURLCollection:didConvertSuccessfully:conversionOutputInformation:conversionOutputData:conversionOutputFileType:conversionError:"
- "processCompletedQueueEntry:resultURLCollection:didConvertSuccessfully:conversionOutputInformation:conversionOutputData:conversionOutputFileType:conversionError:"
- "v68@0:8@16@24B32@36@44@52@60"

```
