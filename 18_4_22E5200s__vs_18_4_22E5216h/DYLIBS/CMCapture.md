## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-587.100.12.0.0
-  __TEXT.__text: 0x774370
-  __TEXT.__auth_stubs: 0x4f00
-  __TEXT.__objc_methlist: 0x2d698
+587.100.15.0.0
+  __TEXT.__text: 0x7747ec
+  __TEXT.__auth_stubs: 0x4f60
+  __TEXT.__objc_methlist: 0x2d6b0
   __TEXT.__const: 0x150608
-  __TEXT.__cstring: 0xc12b4
-  __TEXT.__oslogstring: 0x106ac7
+  __TEXT.__cstring: 0xc0afa
+  __TEXT.__oslogstring: 0x106ec5
   __TEXT.__gcc_except_tab: 0x4200
   __TEXT.__dlopen_cstrs: 0x6d8
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0xdcd8
+  __TEXT.__unwind_info: 0xdcb8
   __TEXT.__objc_classname: 0x7625
-  __TEXT.__objc_methname: 0x940c8
+  __TEXT.__objc_methname: 0x9410c
   __TEXT.__objc_methtype: 0x13a82
-  __TEXT.__objc_stubs: 0x40ca0
-  __DATA_CONST.__got: 0x5fd8
-  __DATA_CONST.__const: 0xa7e0
+  __TEXT.__objc_stubs: 0x40ce0
+  __DATA_CONST.__got: 0x62a0
+  __DATA_CONST.__const: 0xa3e8
   __DATA_CONST.__objc_classlist: 0x18e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x127e8
+  __DATA_CONST.__objc_selrefs: 0x127f8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x1758
-  __DATA_CONST.__objc_arraydata: 0x3658
-  __AUTH_CONST.__auth_got: 0x2790
+  __DATA_CONST.__objc_arraydata: 0x3660
+  __AUTH_CONST.__auth_got: 0x27c0
   __AUTH_CONST.__auth_ptr: 0xd0
-  __AUTH_CONST.__const: 0x3f50
-  __AUTH_CONST.__cfstring: 0x429c0
-  __AUTH_CONST.__objc_const: 0x83ce0
-  __AUTH_CONST.__objc_intobj: 0x4f38
+  __AUTH_CONST.__const: 0x3eb0
+  __AUTH_CONST.__cfstring: 0x41f00
+  __AUTH_CONST.__objc_const: 0x83d30
+  __AUTH_CONST.__objc_intobj: 0x4f50
   __AUTH_CONST.__objc_arrayobj: 0x2628
   __AUTH_CONST.__objc_doubleobj: 0xa80
   __AUTH_CONST.__objc_floatobj: 0x230
   __AUTH_CONST.__objc_dictobj: 0x1798
   __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x96c0
-  __DATA.__data: 0x48f0
+  __DATA.__objc_ivar: 0x96c8
+  __DATA.__data: 0x48e0
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x10a0
-  __DATA.__bss: 0x1828
+  __DATA.__bss: 0x1810
   __DATA_DIRTY.__objc_data: 0xf050
-  __DATA_DIRTY.__data: 0xfe0
+  __DATA_DIRTY.__data: 0xfc0
   __DATA_DIRTY.__common: 0x1040
-  __DATA_DIRTY.__bss: 0xcb0
+  __DATA_DIRTY.__bss: 0xca0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/PrivateFrameworks/AudioSession.framework/AudioSession
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CMCaptureCore.framework/CMCaptureCore
+  - /System/Library/PrivateFrameworks/CMCaptureDevice.framework/CMCaptureDevice
   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 30667
-  Symbols:   40513
-  CStrings:  52221
+  Functions: 30662
+  Symbols:   40483
+  CStrings:  52138
 
Symbols:
+ _kFigCaptureSessionNotificationPayloadKey_CameraStolenInterruptor
- _FigCaptureDeviceGetTypeID
- _FigCaptureISPProcessingSessionGetClassID
- _FigCaptureISPProcessingSessionGetTypeID
- _FigCaptureStreamGetTypeID
- _FigCaptureSynchronizedStreamsGroupGetClassID
- _FigCaptureSynchronizedStreamsGroupGetTypeID
- _kFigCaptureAddAttachmentsOptionsKey_SelectedAttachmentKeys
- _kFigCaptureDeviceNotification_SensorAccessRevoked
- _kFigCaptureDeviceNotification_StreamArrayChanged
- _kFigCaptureISPProcessingSessionOutputID_IntermediateTap
- _kFigCaptureISPProcessingSessionOutputID_PrimaryScalerLowRes
- _kFigCaptureISPProcessingSessionOutputID_Vision
- _kFigCaptureISPProcessingSessionOutputParameterKey_InputCropRect
- _kFigCaptureISPProcessingSessionParameterKey_MetadataDictionary
- _kFigCaptureISPProcessingSessionParameterKey_OutputParameters
- _kFigCaptureISPProcessingSessionParameterKey_SessionTypeSpecificParameters
- _kFigCaptureISPProcessingSessionProperty_DefaultProcessingParameters
- _kFigCaptureISPProcessingSessionProperty_DeferAdditionOfAttachments
- _kFigCaptureISPProcessingSessionProperty_OutputHandler
- _kFigCaptureISPProcessingSessionProperty_SupportedOutputs
- _kFigCapturePropertyShouldBeSerializedKey
- _kFigCapturePropertyType_Allocator
- _kFigCapturePropertyType_BufferQueue
- _kFigCapturePropertyType_Enumeration
- _kFigCapturePropertyType_FormatDescription
- _kFigCapturePropertyType_PixelBuffer
- _kFigCapturePropertyType_Unused
- _kFigCaptureStreamNotification_OverflowDetected
- _kFigCaptureStreamNotification_StreamInterruption_InterruptionEnded
- _kFigCaptureStreamNotification_StreamInterruption_StopNow
- _kFigCaptureStreamProperty_BufferQueue
- _kFigCaptureStreamProperty_CMIODeviceHasUltraWideCamera
- _kFigCaptureStreamProperty_CMIODeviceHasWideCamera
- _kFigCaptureStreamProperty_Clock
- _kFigCaptureStreamProperty_FormatDescription
- _kFigCaptureStreamProperty_ManualFramingDeviceType
- _kFigCaptureStreamProperty_StillImageBufferQueue
- _kFigCaptureStreamProperty_SuspendedByUser
- _kFigSupportedFormat_AudioMaxSampleRate
- _kFigSupportedFormat_AudioMinSampleRate
- _kFigSupportedFormat_VideoScaleFactor
CStrings:
+ "( v1Flags || v2Flags || v3Flags )"
+ "-[BWFigCaptureDeviceVendor _deviceAvailabilityChangedForClient:available:postNotification:reason:canShareWithFlashlight:cameraStolenInterruptor:]_block_invoke"
+ "<<<< BWDeferredContainer >>>> %s: Asset for tag %{public}@ is not an NSArray; class is %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Asset for tag %{public}@ is not an NSDictionary; class is %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Could not open manifest"
+ "<<<< BWDeferredContainer >>>> %s: Error %ld creating unarchiver: %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Failed to decode application ID, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Failed to decode photo descriptors, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Failed to decode still image capture settings, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Failed to decode still image settings, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Invalid capture request identifier %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Invalid number of intermediates"
+ "<<<< BWDeferredContainer >>>> %s: Invalid photo descriptors"
+ "<<<< BWDeferredContainer >>>> %s: Invalid still image capture settings"
+ "<<<< BWDeferredContainer >>>> %s: Invalid still image settings"
+ "<<<< BWDeferredContainer >>>> %s: Malformed captureRequestIdentifierString in manifest %{public}@, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Manifest failed to decode version number, %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: Mismatched intermediate type for %{public}@ (asset name %{public}@)"
+ "<<<< BWDeferredContainer >>>> %s: Missing asset for tag %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: No matching asset for tag %{public}@"
+ "<<<< BWDeferredContainer >>>> %s: URL for manifest %{public}@ is invalid"
+ "<<<< BWDeferredContainer >>>> %s: captureRequestIdentifier in manifest %{public}@ is not a valid UUID"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Iris still image capture time is outside of the Iris video boundaries, movie is hard cut, override error for client (%d), %@"
+ "<<<< FigCaptureClientApplicationStateMonitor >>>> %s: %{public}@ Cannot store reference to %{public}@[%d] without a root host application ID"
+ "CameraStolenInterruptor"
+ "TB,N,V_isHardCut"
+ "V59"
+ "_bypassConnection"
+ "_isHardCut"
+ "_willStopStreaming"
+ "com.apple.private.avfoundation.capture.camera-stolen-interruptor.allow"
+ "description=CameraCapture-587.100.15"
+ "isHardCut"
+ "setIsHardCut:"
+ "v28@?0i8B12i16@\"NSString\"20"
- "-[BWFigCaptureDeviceVendor _deviceAvailabilityChangedForClient:available:postNotification:reason:canShareWithFlashlight:]_block_invoke"
- "<<<< BWDeferredContainer >>>> %s: Asset for tag %@ is not an NSArray"
- "<<<< BWDeferredContainer >>>> %s: Asset for tag %@ is not an NSDictionary"
- "<<<< BWDeferredContainer >>>> %s: Error %ld creating unarchiver: %@"
- "<<<< BWDeferredContainer >>>> %s: Failed to decode application ID, %@"
- "<<<< BWDeferredContainer >>>> %s: Failed to decode photo descriptors, %@"
- "<<<< BWDeferredContainer >>>> %s: Failed to decode still image capture settings, %@"
- "<<<< BWDeferredContainer >>>> %s: Failed to decode still image settings, %@"
- "<<<< BWDeferredContainer >>>> %s: Malformed captureRequestIdentifierString in manifest %@, %@"
- "<<<< BWDeferredContainer >>>> %s: Mismatched intermediate type for %@ (asset name %@)"
- "<<<< BWDeferredContainer >>>> %s: No matching asset for tag %@"
- "<<<< BWDeferredContainer >>>> %s: URL for manifest %@ is invalid"
- "<<<< BWDeferredContainer >>>> %s: captureRequestIdentifier in manifest %@ is not a valid UUID"
- "Allocator"
- "AudioMaxSampleRate"
- "AudioMinSampleRate"
- "AutoAENow"
- "AutoFocusNow"
- "BatteryLevelChanged"
- "BatteryStateChanged"
- "Boolean"
- "BufferQueue"
- "CMIOCenterStageRectOfInterest"
- "CMIOCinematicFramingEnabled"
- "CMIOCompressedFormat"
- "CMIOExtensionDeviceID"
- "CMIOExtensionPropertyArray"
- "CMIOExtensionPropertyChanged"
- "CMIOFlashMode"
- "CMIOFlashSupported"
- "CMIOHighResolutionPhotoEnabled"
- "CMIOMaxPhotoDimensionsHeight"
- "CMIOMaxPhotoDimensionsWidth"
- "CMIOQualityPrioritization"
- "CMIOStillImageMaxQualityPrioritization"
- "CMIOVideoZoomFactor"
- "ClientPriority"
- "Collection"
- "CompressedStillImageCaptureSupported"
- "Could not open manifest"
- "Could not update URL for tag %@"
- "DefaultFormatIndexDisabled"
- "DefaultProcessingParameters"
- "DeferAdditionOfAttachments"
- "DeviceNoLongerAvailable"
- "DeviceTrackingActiveChanged"
- "Discontinuity"
- "Enumeration"
- "EventTimeStamp"
- "FigCaptureISPProcessingSession"
- "FigCaptureStream"
- "FigCaptureSynchronizedStreamsGroup"
- "FormatIndex"
- "HiddenStateChanged"
- "InputCropRect"
- "InputPixelBufferAttributes"
- "IntermediateTap"
- "Invalid intermediates"
- "Invalid still image capture settings"
- "Invalid still image settings"
- "MaximumAllowedFrameRate"
- "MaximumFrameRate"
- "MetadataDictionary"
- "MinimumFrameRate"
- "Number"
- "ObjectsDetectionSupportedConfigurationKeys"
- "OutputHandler"
- "OutputParameters"
- "OutputPixelBufferAttributes"
- "OverflowDetected"
- "PixelBuffer"
- "PrimaryScaler"
- "PrimaryScalerLowRes"
- "PropertyType"
- "ReadOnly"
- "ReadWrite"
- "ReadWriteStatus"
- "ReadyToUnhideChanged"
- "SecondaryScaler"
- "SelectedAttachmentKeys"
- "SensorAccessRevoked"
- "SessionType"
- "SessionTypeSpecificParameters"
- "ShouldBeSerialized"
- "StillImageBufferQueue"
- "StreamArray"
- "StreamArrayChanged"
- "StreamInterruption_InterruptionEnded"
- "StreamInterruption_StopNow"
- "StreamStarted"
- "StreamStopped"
- "String"
- "SupportedFormatsArray"
- "SupportedOutputs"
- "SupportedPropertiesDictionary"
- "SuspendedByUser"
- "UnrecoverableError"
- "Unused"
- "Value"
- "VideoBinningFactorHorizontal"
- "VideoBinningFactorVertical"
- "VideoIsBinned"
- "VideoMinFrameRate"
- "VideoScaleFactor"
- "WriteOnly"
- "[FigCaptureDevice %p]"
- "[FigCaptureISPProcessingSession %p]"
- "[FigCaptureStream %p]"
- "[FigCaptureSynchronizedStreamsGroup %p]"
- "_bypassPipelineStage"
- "captureRequestIdentifierIsValid"
- "description=CameraCapture-587.100.12"
- "intermediatesAreValid"
- "photoDescriptorsAreValid"
- "stillImageCaptureSettingsIsValid"
- "stillImageSettingsIsValid"
- "v20@?0i8B12i16"

```
