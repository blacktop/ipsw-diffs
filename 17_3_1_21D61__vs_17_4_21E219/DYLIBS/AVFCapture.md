## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-472.1.2.0.0
-  __TEXT.__text: 0xd8f08
-  __TEXT.__auth_stubs: 0x1820
-  __TEXT.__objc_methlist: 0xb6f0
-  __TEXT.__const: 0x868
-  __TEXT.__gcc_except_tab: 0x1c98
-  __TEXT.__cstring: 0x16f33
-  __TEXT.__oslogstring: 0x3e0e
+475.31.1.0.0
+  __TEXT.__text: 0xdce6c
+  __TEXT.__auth_stubs: 0x1840
+  __TEXT.__objc_methlist: 0xb7e0
+  __TEXT.__const: 0x848
+  __TEXT.__gcc_except_tab: 0x1d24
+  __TEXT.__cstring: 0x17713
+  __TEXT.__oslogstring: 0x4706
   __TEXT.__dlopen_cstrs: 0x178
-  __TEXT.__unwind_info: 0x3834
-  __TEXT.__objc_classname: 0x1548
-  __TEXT.__objc_methname: 0x207e8
-  __TEXT.__objc_methtype: 0x3529
-  __TEXT.__objc_stubs: 0x132a0
-  __DATA_CONST.__got: 0x1e50
-  __DATA_CONST.__const: 0x62a8
+  __TEXT.__unwind_info: 0x38c8
+  __TEXT.__objc_classname: 0x155c
+  __TEXT.__objc_methname: 0x20a82
+  __TEXT.__objc_methtype: 0x3514
+  __TEXT.__objc_stubs: 0x133c0
+  __DATA_CONST.__got: 0x1e70
+  __DATA_CONST.__const: 0x6328
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf4e8
-  __DATA_CONST.__objc_selrefs: 0x5ed8
+  __DATA_CONST.__objc_const: 0xf608
+  __DATA_CONST.__objc_selrefs: 0x5f48
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x790
+  __DATA_CONST.__objc_superrefs: 0x418
   __DATA_CONST.__objc_arraydata: 0x348
   __AUTH_CONST.__objc_const: 0x3f40
-  __AUTH_CONST.__cfstring: 0xf200
-  __AUTH_CONST.__objc_intobj: 0x7b0
+  __AUTH_CONST.__cfstring: 0xf420
+  __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__const: 0x760
   __AUTH_CONST.__objc_arrayobj: 0x258
-  __AUTH_CONST.__auth_got: 0xc20
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x780
-  __DATA.__objc_superrefs: 0x418
-  __DATA.__objc_ivar: 0x1390
-  __DATA.__data: 0xca0
+  __AUTH_CONST.__auth_got: 0xc30
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x13ac
+  __DATA.__data: 0xcc8
   __DATA.__common: 0x60
-  __DATA.__bss: 0x2d8
-  __DATA_DIRTY.__objc_data: 0x2e40
+  __DATA.__bss: 0x300
+  __DATA_DIRTY.__objc_data: 0x2ee0
   __DATA_DIRTY.__data: 0x18
   __DATA_DIRTY.__common: 0x140
-  __DATA_DIRTY.__bss: 0x370
+  __DATA_DIRTY.__bss: 0x390
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4634
-  Symbols:   16863
-  CStrings:  7473
+  Functions: 4667
+  Symbols:   16970
+  CStrings:  7568
 
Symbols:
+ +[AVCaptureDevice _checkEligiblityForEffect:]
+ +[AVCaptureDevice _haveShownGesturesDefaultDisabledNotificationChanged:]
+ +[AVCaptureDevice haveShownGesturesDefaultDisabledNotification]
+ +[AVCaptureDevice requestGesturesDefaultDisabledNotification]
+ +[AVCaptureDevice setUpGesturesDefaultDisabledNotification]
+ -[AVCaptureConnection _setVideoRotationAngle:]
+ -[AVCaptureDevice(SceneClassification) documentSceneConfidence]
+ -[AVCaptureDevice(SceneClassification) isSceneClassificationActive]
+ -[AVCaptureFigVideoDevice documentSceneConfidence]
+ -[AVCaptureFigVideoDevice isSceneClassificationActive]
+ -[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:]
+ -[AVCaptureProprietaryDefaultsSingleton _runBlockOnProprietaryDefaultsSourceQueueSync:]
+ -[AVCaptureProprietaryDefaultsSingleton unobserveChangesForKey:]
+ -[AVCaptureSession _initWithMediaEnvironment:]
+ -[AVCaptureSession initWithMediaEnvironment:]
+ -[AVCaptureSession mediaEnvironment]
+ -[AVMetadataFaceObject confidence]
+ -[AVMetadataFaceObject hasConfidence]
+ -[AVMetadataFaceObjectInternal confidence]
+ -[AVMetadataFaceObjectInternal hasConfidence]
+ -[AVMetadataFaceObjectInternal setConfidence:]
+ -[AVMetadataFaceObjectInternal setHasConfidence:]
+ GCC_except_table118
+ GCC_except_table119
+ GCC_except_table137
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table143
+ GCC_except_table16
+ GCC_except_table208
+ GCC_except_table30
+ GCC_except_table433
+ GCC_except_table46
+ GCC_except_table68
+ GCC_except_table72
+ GCC_except_table741
+ GCC_except_table784
+ GCC_except_table83
+ GCC_except_table98
+ _AVCaptureBundleCameraReactionEffectGesturesEnabledDefaultKey
+ _AVCaptureClientHasEntitlement.checkWebBrowserEngineRenderingOnceToken
+ _AVCaptureClientHasEntitlement.isWebBrowserEngineGPUProcess
+ _AVCaptureDeviceTypeBuiltInUltraWideAngleMetadataCamera
+ _AVCaptureEntitlementWebBrowserEngineRendering
+ _AVControlCenterVideoEffectsGesturesEnabledDefaultPreferenceKey
+ _AVControlCenterVideoEffectsHaveShownGesturesDefaultDisabledNotificationPreferenceKey
+ _AVControlCenterVideoEffectsObserveGesturesDefaultDisabled
+ _AVControlCenterVideoEffectsObserveGesturesDefaultDisabled.onceToken
+ _AVControlCenterVideoEffectsObserveGesturesDefaultDisabled.sObserver
+ _AVControlCenterVideoEffectsRequestGesturesDefaultDisabledNotificationPreferenceKey
+ _FigCaptureCameraRequires180DegreesRotation
+ _FigCaptureDeferredPhotoProcessorIsAllowedToPrewarm
+ _OBJC_CLASS_$_LSBundleRecord
+ _OBJC_IVAR_$_AVCaptureConnectionInternal.clientUsesVideoRotationAngleAPI
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._sceneClassificationActive
+ _OBJC_IVAR_$_AVCaptureFigVideoDevice._sceneClassificationKVO
+ _OBJC_IVAR_$_AVCaptureSessionInternal.mediaEnvironment
+ _OBJC_IVAR_$_AVControlCenterModuleState._gesturesEnabledDefaultKey
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._confidence
+ _OBJC_IVAR_$_AVMetadataFaceObjectInternal._hasConfidence
+ __OBJC_$_CLASS_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification)
+ __OBJC_$_INSTANCE_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit|SceneClassification)
+ ___132-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:]_block_invoke
+ ___132-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:]_block_invoke_2
+ ___46-[AVCaptureConnection _setVideoRotationAngle:]_block_invoke
+ ___46-[AVCaptureSession _initWithMediaEnvironment:]_block_invoke
+ ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke.398
+ ___50-[AVCaptureFigVideoDevice documentSceneConfidence]_block_invoke
+ ___54-[AVCaptureFigVideoDevice isSceneClassificationActive]_block_invoke
+ ___55+[AVCaptureDevice reactionEffectGesturesEnabledDefault]_block_invoke
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_38
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_39
+ ___55-[AVCaptureFigVideoDevice _handleNotification:payload:]_block_invoke_40
+ ___59+[AVCaptureDevice setUpGesturesDefaultDisabledNotification]_block_invoke
+ ___59+[AVCaptureDevice setUpGesturesDefaultDisabledNotification]_block_invoke_2
+ ___64-[AVControlCenterModuleState installProprietaryDefaultsHandlers]_block_invoke_20
+ ___64-[AVControlCenterModuleState installProprietaryDefaultsHandlers]_block_invoke_21
+ ___67-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:]_block_invoke.277
+ ___67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.266
+ ___74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.555
+ ___87-[AVCaptureProprietaryDefaultsSingleton _runBlockOnProprietaryDefaultsSourceQueueSync:]_block_invoke
+ ___AVControlCenterVideoEffectsObserveGesturesDefaultDisabled_block_invoke
+ ___AVControlCenterVideoEffectsObserveGesturesDefaultDisabled_block_invoke_2
+ ___block_descriptor_40_e8_32b_e21_v24?0"NSString"816ls32l8
+ ___block_descriptor_64_e8_32o40o48o56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_descriptor_72_e8_32o40r48r56r64r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_73_e8_32o40o48o56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_82_e8_32o40o48o56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
+ ___block_literal_global.1220
+ ___block_literal_global.1227
+ ___block_literal_global.162
+ ___block_literal_global.167
+ ___block_literal_global.241
+ ___block_literal_global.258
+ ___block_literal_global.260
+ ___block_literal_global.263
+ ___block_literal_global.342
+ ___block_literal_global.350
+ ___block_literal_global.355
+ ___block_literal_global.386
+ ___block_literal_global.394
+ ___block_literal_global.414
+ ___block_literal_global.446
+ ___block_literal_global.478
+ ___block_literal_global.483
+ ___block_literal_global.486
+ ___block_literal_global.669
+ __unnamed_array_storage.63
+ _kFigCaptureSourceProperty_SceneClassificationActive
+ _kFigCaptureSourceProperty_SceneClassificationConfidences
+ _kFigCaptureStreamMetadata_ConfidenceLevel
+ _kFigCaptureStreamSceneType_Document
+ _objc_msgSend$_checkEligiblityForEffect:
+ _objc_msgSend$_handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:
+ _objc_msgSend$_haveShownGesturesDefaultDisabledNotificationChanged:
+ _objc_msgSend$_initWithMediaEnvironment:
+ _objc_msgSend$_runBlockOnProprietaryDefaultsSourceQueueSync:
+ _objc_msgSend$_setVideoRotationAngle:
+ _objc_msgSend$bundleRecordForCurrentProcess
+ _objc_msgSend$hasConfidence
+ _objc_msgSend$haveShownGesturesDefaultDisabledNotification
+ _objc_msgSend$requestGesturesDefaultDisabledNotification
+ _objc_msgSend$setConfidence:
+ _objc_msgSend$setHasConfidence:
+ _objc_msgSend$setUpGesturesDefaultDisabledNotification
+ _objc_msgSend$unobserveChangesForKey:
+ _reactionEffectGesturesEnabledDefault.gesturesEnabledDefault
+ _reactionEffectGesturesEnabledDefault.onceToken
+ _sGesturesDefaultDisabledNotificationLock
+ _sHaveShownGesturesDefaultDisabledNotification
+ _sHaveShownGesturesDefaultDisabledNotificationKey
+ _sRequestGesturesDefaultDisabledNotificationKey
+ _setUpGesturesDefaultDisabledNotification.onceToken
- -[AVCaptureMovieFileOutput _updateMovieFragmentInterval:forVideoConnection:dimensions:]
- -[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:callHandlersAsync:]
- -[AVCaptureProprietaryDefaultsSingleton _runBlockOnProprietaryDefaultsSourceQueue:]
- GCC_except_table104
- GCC_except_table11
- GCC_except_table116
- GCC_except_table123
- GCC_except_table124
- GCC_except_table130
- GCC_except_table132
- GCC_except_table134
- GCC_except_table140
- GCC_except_table202
- GCC_except_table21
- GCC_except_table22
- GCC_except_table425
- GCC_except_table6
- GCC_except_table65
- GCC_except_table738
- GCC_except_table94
- _AVCaptureWarnGesturesInternalFeature
- __OBJC_$_CLASS_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit)
- __OBJC_$_INSTANCE_METHODS_AVCaptureDevice(AVCaptureProprietaryDefaultsDomain|DeviceHistoryInternal|ServerConnection|DockKit)
- ___108-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:callHandlersAsync:]_block_invoke
- ___108-[AVCaptureProprietaryDefaultsSingleton _handleDefaultChangedNotificationForKey:newValue:callHandlersAsync:]_block_invoke_2
- ___24-[AVCaptureSession init]_block_invoke
- ___45-[AVCaptureConnection setVideoRotationAngle:]_block_invoke
- ___48+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke_5
- ___67-[AVCaptureFigVideoDevice _setActiveVideoMaxFrameDurationInternal:]_block_invoke.271
- ___67-[AVCaptureFigVideoDevice _setActiveVideoMinFrameDurationInternal:]_block_invoke.260
- ___74-[AVCaptureFigVideoDevice _handleCMIOExtensionPropertyChangeNotification:]_block_invoke.549
- ___83-[AVCaptureProprietaryDefaultsSingleton _runBlockOnProprietaryDefaultsSourceQueue:]_block_invoke
- ___87-[AVCaptureMovieFileOutput _updateMovieFragmentInterval:forVideoConnection:dimensions:]_block_invoke
- ___block_descriptor_57_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_66_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.1195
- ___block_literal_global.1202
- ___block_literal_global.159
- ___block_literal_global.164
- ___block_literal_global.226
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.248
- ___block_literal_global.307
- ___block_literal_global.318
- ___block_literal_global.326
- ___block_literal_global.366
- ___block_literal_global.379
- ___block_literal_global.387
- ___block_literal_global.389
- ___block_literal_global.420
- ___block_literal_global.471
- ___block_literal_global.476
- ___block_literal_global.479
- ___block_literal_global.659
- __unnamed_array_storage.56
- __updateMovieFragmentInterval:forVideoConnection:dimensions:.onceToken
- _objc_msgSend$_handleDefaultChangedNotificationForKey:newValue:callHandlersAsync:
- _objc_msgSend$_runBlockOnProprietaryDefaultsSourceQueue:
- _objc_msgSend$_updateMovieFragmentInterval:forVideoConnection:dimensions:
- _objc_msgSend$bundleWithIdentifier:
- _objc_msgSend$setVideoRotationAngle:
CStrings:
+ "%@did-show-gestures-default-disabled-notification"
+ "%@gestures-enabled-default"
+ "%@request-gestures-default-disabled-notification"
+ "+[AVCaptureDevice _checkEligiblityForEffect:]"
+ "+[AVCaptureDevice _haveShownGesturesDefaultDisabledNotificationChanged:]"
+ "+[AVCaptureDevice reactionEffectGesturesEnabledDefault]_block_invoke"
+ "+[AVCaptureDevice requestGesturesDefaultDisabledNotification]"
+ "+[AVCaptureDevice setUpReactionEffectsStateOnce]_block_invoke"
+ "-[AVCaptureDeferredPhotoProcessor cancelAllPrewarming]"
+ "-[AVCaptureDeferredPhotoProcessor prewarmWithSettings:]"
+ "-[AVCaptureProprietaryDefaultsSingleton updateCameraOverrideHistory:withCameraInfo:setOverride:]"
+ "-[AVCaptureProprietaryDefaultsSingleton updateCameraOverrideHistory:withCameraInfo:setOverride:]_block_invoke"
+ "-[AVCaptureSession _addVideoPreviewLayer:exceptionReason:]"
+ "-[AVCaptureSession _addVideoPreviewLayerWithNoConnection:exceptionReason:]"
+ "-[AVCaptureSession _initWithMediaEnvironment:]"
+ "-[AVCaptureSession addConnection:]"
+ "-[AVCaptureSession addInputWithNoConnections:]"
+ "-[AVCaptureSession addOutput:]"
+ "-[AVCaptureSession addOutputWithNoConnections:]"
+ "-[AVCaptureSession initWithAssumedIdentity:]"
+ "-[AVCaptureSession initWithMediaEnvironment:]"
+ "-[AVCaptureSession initWithMediaEnvironment:] may only be called by processes with the %@ entitlement"
+ "-[AVCaptureSession init] may not be called by processes with the %@ entitlement"
+ "-[AVCaptureSession removeConnection:]"
+ "-[AVCaptureSession removeOutput:]"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Delivering failure callback %{public}@ with error status %d%{public}@ (%d of %d)"
+ "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: SKIPPING PREWARMING -- unsupported by this platform"
+ "<<<< AVCaptureDevice >>>> %s: App with preferencesDomain '%@' bundle '%@' %s eligible for %@ effects"
+ "<<<< AVCaptureDevice >>>> %s: App with preferencesDomain '%@' recognized eligible for %@"
+ "<<<< AVCaptureDevice >>>> %s: User value %@ overriding gesture default %d"
+ "<<<< AVCaptureDevice >>>> %s: Using default from Info.plist %d"
+ "<<<< AVCaptureDevice >>>> %s: Using default from system %d"
+ "<<<< AVCaptureDevice >>>> %s: gestures-disabled requesting notification (didShow %d)"
+ "<<<< AVCaptureDevice >>>> %s: haveShownGesturesDefaultDisabledNotificationChanged handler (newValue: %d) backtrace"
+ "<<<< AVCaptureDevice >>>> %s: haveShownGesturesDefaultDisabledNotificationChanged handler (newValue: %d) backtrace entries count %ld backtraceSymbols is null? %d"
+ "<<<< AVCaptureDevice >>>> %s: sHaveShownGesturesDefaultDisabledNotification changed (newValue: %d)"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: userPreferredCamera changing from %{public}@ to %{public}@"
+ "<<<< AVCaptureFigVideoDevice >>>> %s: userPreferredCamera not changing from %{public}@, but we need to cooerce the systemPreferredCamera (which is currently %@)"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: sending out new camera override history %{private}@"
+ "<<<< AVCaptureProprietaryDefaults >>>> %s: updating history %@, overrideChanged changed %c, new camera override history %{private}@"
+ "<<<< AVCaptureSession >>>> %s: (%p) called"
+ "<<<< AVCaptureSession >>>> %s: (%p) called with assumed identity: %{public}@"
+ "<<<< AVCaptureSession >>>> %s: (%p) called with media environment: %{public}@"
+ "<<<< AVCaptureSession >>>> %s: (%p) failureReason = %{public}@"
+ "<<<< AVCaptureSession >>>> %s: (%p) finished"
+ "<<<< AVControlCenterModules >>>> %s: %{private}@ %{private}@ enabled:%s"
+ "<<<< AVControlCenterModules >>>> %s: AVCCM Using default from Info.plist %d"
+ "<<<< AVControlCenterModules >>>> %s: AVCCM Using default from system %d"
+ "<<<< AVControlCenterModules >>>> %s: AVCCM Using value from PD %@"
+ "<<<< AVControlCenterModules >>>> %s: Already gave gestures-disabled user guidance for %@"
+ "<<<< AVControlCenterModules >>>> %s: Callback indicates gestures-disabled user guidance %s given for %@ (name %@)"
+ "<<<< AVControlCenterModules >>>> %s: Control Center is querying reactions-enabled of %@ before it has initialized, lookup indicates %d (not necessarily a fault, but unexpected)"
+ "<<<< AVControlCenterModules >>>> %s: Could not locate record for %@: %@"
+ "<<<< AVControlCenterModules >>>> %s: Unavailable reasons %lu for %{private}@ on %{private}@"
+ "AVCaptureDeviceTypeBuiltInUltraWideAngleMetadataCamera"
+ "AVControlCenterVideoEffectsModuleGetUnavailableReasons"
+ "AVControlCenterVideoEffectsModuleIsEffectEnabledForBundleID"
+ "AVControlCenterVideoEffectsObserveGesturesDefaultDisabled_block_invoke"
+ "AVControlCenterVideoEffectsObserveGesturesDefaultDisabled_block_invoke_2"
+ "NSCameraReactionEffectGesturesEnabledDefault"
+ "Not available - use -hasConfidence"
+ "Not available - use -hasPitchAngle"
+ "SceneClassification"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_hasConfidence"
+ "TB,R,N,GisSceneClassificationActive"
+ "TI,V_firedCallbackFlags"
+ "Td,N,V_confidence"
+ "The passed device is nil, which is not allowed"
+ "UWM"
+ "UltraWideMetadata"
+ "_checkEligiblityForEffect:"
+ "_gesturesEnabledDefaultKey"
+ "_handleDefaultChangedNotificationForKey:newValue:handlersForKeyObservers:callHandlersAsync:"
+ "_hasConfidence"
+ "_haveShownGesturesDefaultDisabledNotificationChanged:"
+ "_initWithMediaEnvironment:"
+ "_runBlockOnProprietaryDefaultsSourceQueueSync:"
+ "_sceneClassificationActive"
+ "_sceneClassificationKVO"
+ "_setVideoRotationAngle:"
+ "bundleRecordForCurrentProcess"
+ "clientUsesVideoRotationAngleAPI"
+ "com.apple.developer.web-browser-engine.rendering"
+ "description=CameraCapture_AVF-475.31.1"
+ "documentSceneConfidence"
+ "gestures-enabled-default"
+ "hasConfidence"
+ "haveShownGesturesDefaultDisabledNotification"
+ "initWithMediaEnvironment:"
+ "is"
+ "is NOT"
+ "isSceneClassificationActive"
+ "mediaEnvironment"
+ "requestGesturesDefaultDisabledNotification"
+ "sceneClassificationActive"
+ "setConfidence:"
+ "setHasConfidence:"
+ "setUpGesturesDefaultDisabledNotification"
+ "uid:%lld %@:{%@%@%@%@%@%@%@%@%@%@ }%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
+ "unobserveChangesForKey:"
+ "v44@0:8@16@24@32B40"
+ "was"
+ "was not"
- "-[AVCaptureMovieFileOutput _updateMovieFragmentInterval:forVideoConnection:dimensions:]"
- "<<<< AVCaptureDeferredPhotoProcessor >>>> %s: Delivering failure callback %{private}@ with error status %d%{public}@"
- "<<<< AVCaptureFigVideoDevice >>>> %s: userPreferredCameraChanged changing from %{public}@ to %{public}@"
- "<<<< AVCaptureMovieFileOutput >>>> %s: Warning! Overwriting movieFragmentInterval from %f to %f with bitrate %llu"
- "<<<< AVCaptureSession >>>> %s: (%p)failureReason = %{public}@"
- "AVCaptureDeviceNames-MetadataCamera"
- "_handleDefaultChangedNotificationForKey:newValue:callHandlersAsync:"
- "_runBlockOnProprietaryDefaultsSourceQueue:"
- "_updateMovieFragmentInterval:forVideoConnection:dimensions:"
- "bundleWithIdentifier:"
- "description=CameraCapture_AVF-472.1.2"
- "uid:%lld %@:{%@%@%@%@%@%@%@%@%@%@ }%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
- "{?=qiIq}64@0:8{?=qiIq}16@40{CGSize=dd}48"

```
