## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

-4008.3.2.0.0
-  __TEXT.__text: 0x1de394
+4009.19.0.0.0
+  __TEXT.__text: 0x1df470
   __TEXT.__auth_stubs: 0x20a0
-  __TEXT.__objc_methlist: 0x15230
-  __TEXT.__const: 0x2d70
+  __TEXT.__objc_methlist: 0x15388
+  __TEXT.__const: 0x2d58
   __TEXT.__gcc_except_tab: 0x2404
-  __TEXT.__cstring: 0x127fb
-  __TEXT.__oslogstring: 0x11d7c
+  __TEXT.__cstring: 0x12898
+  __TEXT.__oslogstring: 0x11e33
   __TEXT.__dlopen_cstrs: 0x310
   __TEXT.__ustring: 0x8
-  __TEXT.__objc_const_ax: 0xe9c0
-  __TEXT.__unwind_info: 0x84c4
-  __TEXT.__objc_classname: 0x4a20
-  __TEXT.__objc_methname: 0x7ff67
-  __TEXT.__objc_methtype: 0xd7d4
-  __TEXT.__objc_stubs: 0x49c60
-  __DATA_CONST.__got: 0x1150
-  __DATA_CONST.__const: 0x6248
-  __DATA_CONST.__objc_classlist: 0xec8
+  __TEXT.__objc_const_ax: 0xea20
+  __TEXT.__unwind_info: 0x8514
+  __TEXT.__objc_classname: 0x4a6e
+  __TEXT.__objc_methname: 0x80543
+  __TEXT.__objc_methtype: 0xd86f
+  __TEXT.__objc_stubs: 0x49f40
+  __DATA_CONST.__got: 0x1170
+  __DATA_CONST.__const: 0x6220
+  __DATA_CONST.__objc_classlist: 0xed0
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x5d8
+  __DATA_CONST.__objc_protolist: 0x5e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3b798
-  __DATA_CONST.__objc_selrefs: 0x14610
+  __DATA_CONST.__objc_const: 0x3bc20
+  __DATA_CONST.__objc_selrefs: 0x146e0
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_classrefs: 0x1688
+  __DATA_CONST.__objc_superrefs: 0xc70
   __DATA_CONST.__objc_arraydata: 0xcf0
-  __AUTH_CONST.__cfstring: 0x12ae0
-  __AUTH_CONST.__objc_const: 0x9f80
+  __AUTH_CONST.__cfstring: 0x12b20
+  __AUTH_CONST.__objc_const: 0x9fc8
   __AUTH_CONST.__objc_intobj: 0x15a8
   __AUTH_CONST.__objc_doubleobj: 0x500
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0xb28
-  __AUTH_CONST.__const: 0xa80
+  __AUTH_CONST.__const: 0xaa0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x1060
-  __AUTH.__objc_data: 0x2af8
-  __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x1670
-  __DATA.__objc_superrefs: 0xc68
-  __DATA.__objc_ivar: 0x3198
+  __AUTH.__objc_data: 0x2648
+  __DATA.__objc_ivar: 0x31bc
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x46c0
-  __DATA.__bss: 0x208
-  __DATA_DIRTY.__objc_data: 0x68d8
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x290
+  __DATA.__data: 0x4778
+  __DATA.__bss: 0x1f0
+  __DATA_DIRTY.__objc_data: 0x6dd8
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x2b8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
   - /System/Library/Frameworks/Metal.framework/Metal
+  - /System/Library/Frameworks/PDFKit.framework/PDFKit
   - /System/Library/Frameworks/Photos.framework/Photos
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/Frameworks/QuickLook.framework/QuickLook
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications

   - /System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit
   - /System/Library/PrivateFrameworks/CompanionCamera.framework/CompanionCamera
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera
   - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F101EBF3-0F7C-3166-8A05-B6E9F560D603
-  Functions: 13794
-  Symbols:   47022
-  CStrings:  24832
+  UUID: 944FE7F0-A34B-392F-BEFE-C11B1E0CD732
+  Functions: 13834
+  Symbols:   47162
+  CStrings:  24893
 
Symbols:
+ +[CAMSemanticStyle styleWithDictionary:error:]
+ -[CAMCaptureCapabilities _isProResCinematicVideoSupported]
+ -[CAMCaptureCapabilities standardSemanticStyle]
+ -[CAMDescriptionOverlayView buttonStyle]
+ -[CAMExternalStorage generateDestinationURLWithExtension:]
+ -[CAMExternalStorage generateDestinationURLWithExtension:].cold.1
+ -[CAMPhysicalCaptureNotifier .cxx_destruct]
+ -[CAMPhysicalCaptureNotifier _cameraButtonRequest]
+ -[CAMPhysicalCaptureNotifier _handleVolumeDownButtonDownNotification:]
+ -[CAMPhysicalCaptureNotifier _handleVolumeDownButtonUpNotification:]
+ -[CAMPhysicalCaptureNotifier _handleVolumeUpButtonDownNotification:]
+ -[CAMPhysicalCaptureNotifier _handleVolumeUpButtonUpNotification:]
+ -[CAMPhysicalCaptureNotifier _setState:]
+ -[CAMPhysicalCaptureNotifier _setVolumeDownButtonState:]
+ -[CAMPhysicalCaptureNotifier _setVolumeUpButtonState:]
+ -[CAMPhysicalCaptureNotifier _updateCaptureButtonNotifications]
+ -[CAMPhysicalCaptureNotifier _updateCaptureButtonNotifications].cold.1
+ -[CAMPhysicalCaptureNotifier _updateStateAndNotifyDelegateIfNeededForButton:]
+ -[CAMPhysicalCaptureNotifier _view]
+ -[CAMPhysicalCaptureNotifier _volumeDownButtonState]
+ -[CAMPhysicalCaptureNotifier _volumeUpButtonState]
+ -[CAMPhysicalCaptureNotifier dealloc]
+ -[CAMPhysicalCaptureNotifier delegate]
+ -[CAMPhysicalCaptureNotifier includesVolumeButtons]
+ -[CAMPhysicalCaptureNotifier initWithView:includeVolumeButtons:]
+ -[CAMPhysicalCaptureNotifier isEnabled]
+ -[CAMPhysicalCaptureNotifier setDelegate:]
+ -[CAMPhysicalCaptureNotifier setEnabled:]
+ -[CAMPhysicalCaptureNotifier set_cameraButtonRequest:]
+ -[CAMPhysicalCaptureNotifier state]
+ -[CAMSemanticStyle analyticsDictionary]
+ -[CAMSemanticStyle avSemanticStyle]
+ -[CAMSemanticStyle dictionaryRepresentation]
+ -[CAMSemanticStyleControl _createSliderForIndex:]
+ -[CAMSpatialVideoDescriptionOverlayView buttonStyle]
+ -[CAMUserPreferences _semanticStyleIndexKey]
+ -[CAMUserPreferences _semanticStylesKey]
+ -[CAMViewfinderView adoptMachineReadableCodeButton:animated:]
+ -[CAMViewfinderView dismissMachineReadableCodeButtonAnimated:]
+ -[CAMViewfinderViewController _cameraCaseShutterNotifier]
+ -[CAMViewfinderViewController _createCameraCaseShutterNotifierIfNeeded]
+ -[CAMViewfinderViewController machineReadableCodeButtonDidTapDismiss:]
+ -[CAMViewfinderViewController physicalCaptureNotifierDidChangeState:forButton:]
+ -[CAMViewfinderViewController set_cameraCaseShutterNotifier:]
+ GCC_except_table1042
+ GCC_except_table1048
+ GCC_except_table1157
+ GCC_except_table1162
+ GCC_except_table1167
+ GCC_except_table210
+ GCC_except_table538
+ GCC_except_table540
+ GCC_except_table594
+ GCC_except_table66
+ GCC_except_table753
+ GCC_except_table771
+ GCC_except_table827
+ _OBJC_CLASS_$_BKSHIDEventDeferringToken
+ _OBJC_CLASS_$_CAMPhysicalCaptureNotifier
+ _OBJC_CLASS_$_SBSHardwareButtonService
+ _OBJC_IVAR_$_CAMCaptureCapabilities.__proResCinematicVideoSupported
+ _OBJC_IVAR_$_CAMCaptureCapabilities._standardSemanticStyle
+ _OBJC_IVAR_$_CAMPhysicalCaptureNotifier.__cameraButtonRequest
+ _OBJC_IVAR_$_CAMPhysicalCaptureNotifier.__view
+ _OBJC_IVAR_$_CAMPhysicalCaptureNotifier.__volumeDownButtonState
+ _OBJC_IVAR_$_CAMPhysicalCaptureNotifier.__volumeUpButtonState
+ _OBJC_IVAR_$_CAMPhysicalCaptureNotifier._delegate
+ _OBJC_IVAR_$_CAMPhysicalCaptureNotifier._enabled
+ _OBJC_IVAR_$_CAMPhysicalCaptureNotifier._includesVolumeButtons
+ _OBJC_IVAR_$_CAMPhysicalCaptureNotifier._state
+ _OBJC_IVAR_$_CAMViewfinderViewController.__cameraCaseShutterNotifier
+ _OBJC_METACLASS_$_CAMPhysicalCaptureNotifier
+ __OBJC_$_INSTANCE_METHODS_CAMPhysicalCaptureNotifier
+ __OBJC_$_INSTANCE_VARIABLES_CAMPhysicalCaptureNotifier
+ __OBJC_$_PROP_LIST_CAMCaptureStyle
+ __OBJC_$_PROP_LIST_CAMPhysicalCaptureNotifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAMCaptureStyle
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAMPhysicalCaptureNotifierDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAMCaptureStyle
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAMPhysicalCaptureNotifierDelegate
+ __OBJC_$_PROTOCOL_REFS_CAMCaptureStyle
+ __OBJC_$_PROTOCOL_REFS_CAMPhysicalCaptureNotifierDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CAMSemanticStyle
+ __OBJC_CLASS_RO_$_CAMPhysicalCaptureNotifier
+ __OBJC_LABEL_PROTOCOL_$_CAMCaptureStyle
+ __OBJC_LABEL_PROTOCOL_$_CAMPhysicalCaptureNotifierDelegate
+ __OBJC_METACLASS_RO_$_CAMPhysicalCaptureNotifier
+ __OBJC_PROTOCOL_$_CAMCaptureStyle
+ __OBJC_PROTOCOL_$_CAMPhysicalCaptureNotifierDelegate
+ __UIApplicationVolumeDownButtonDownNotification
+ __UIApplicationVolumeDownButtonUpNotification
+ __UIApplicationVolumeUpButtonDownNotification
+ __UIApplicationVolumeUpButtonUpNotification
+ ___122-[CAMCameraViewController persistenceController:didGenerateStillImageLocalPersistenceResult:forCaptureResult:fromRequest:]_block_invoke.174
+ ___57-[CAMTimelapseBackendController _frameTransformForState:]_block_invoke
+ ___58-[CAMNebulaDaemonProxyManager _getProxyForExecutingBlock:]_block_invoke.75
+ ___58-[CAMNebulaDaemonProxyManager _getProxyForExecutingBlock:]_block_invoke.77
+ ___61-[CAMViewfinderView adoptMachineReadableCodeButton:animated:]_block_invoke
+ ___62-[CAMViewfinderView dismissMachineReadableCodeButtonAnimated:]_block_invoke
+ ___62-[CAMViewfinderView dismissMachineReadableCodeButtonAnimated:]_block_invoke_2
+ ___63-[CAMNebulaDaemonConnectionManager _getProxyForExecutingBlock:]_block_invoke.77
+ ___68-[CAMViewfinderViewController _setWantsVisualTextAnalysis:animated:]_block_invoke.422
+ ___72-[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]_block_invoke.932
+ ___80-[CAMPersistenceController persistBurstWithIdentifier:result:completionHandler:]_block_invoke.299
+ ___80-[CAMPersistenceController persistBurstWithIdentifier:result:completionHandler:]_block_invoke.299.cold.1
+ ___82-[CAMPersistenceController performDeferredRemotePersistenceWithCompletionHandler:]_block_invoke.297
+ ___94-[CAMCameraViewController _handleCTMVideoLocalPersistenceResult:forCaptureResult:fromRequest:]_block_invoke.183
+ ___block_descriptor_41_e8_32s_e34_v32?0"<CAMCaptureStyle>"8Q16^B24ls32l8
+ ___block_literal_global.1009
+ ___block_literal_global.1151
+ ___block_literal_global.256
+ ___block_literal_global.294
+ ___block_literal_global.304
+ ___block_literal_global.444
+ ___block_literal_global.466
+ ___block_literal_global.68
+ ___block_literal_global.80
+ ___block_literal_global.83
+ __backgroundImage.onceToken.217
+ __frameTransformForState:.frontCameraRotation
+ __frameTransformForState:.onceToken
+ __unnamed_array_storage.1012
+ __unnamed_array_storage.1015
+ __unnamed_array_storage.1018
+ __unnamed_array_storage.1071
+ __unnamed_array_storage.330
+ __unnamed_array_storage.336
+ __unnamed_array_storage.341
+ __unnamed_array_storage.344
+ __unnamed_array_storage.347
+ __unnamed_array_storage.350
+ __unnamed_array_storage.353
+ __unnamed_array_storage.360
+ __unnamed_array_storage.381
+ __unnamed_array_storage.384
+ __unnamed_array_storage.387
+ __unnamed_array_storage.3907
+ __unnamed_array_storage.3910
+ __unnamed_array_storage.3913
+ __unnamed_array_storage.392
+ __unnamed_array_storage.395
+ __unnamed_array_storage.400
+ __unnamed_array_storage.432
+ __unnamed_array_storage.435
+ __unnamed_array_storage.438
+ __unnamed_array_storage.441
+ __unnamed_array_storage.444
+ __unnamed_array_storage.447
+ __unnamed_array_storage.450
+ __unnamed_array_storage.629
+ __unnamed_array_storage.650
+ __unnamed_array_storage.761
+ __unnamed_array_storage.764
+ __unnamed_array_storage.767
+ __unnamed_array_storage.770
+ __unnamed_array_storage.773
+ __unnamed_array_storage.776
+ __unnamed_array_storage.779
+ __unnamed_array_storage.782
+ __unnamed_array_storage.785
+ __unnamed_array_storage.788
+ __unnamed_array_storage.791
+ __unnamed_array_storage.794
+ __unnamed_array_storage.797
+ __unnamed_array_storage.800
+ __unnamed_array_storage.803
+ __unnamed_array_storage.806
+ __unnamed_array_storage.809
+ __unnamed_array_storage.812
+ __unnamed_array_storage.815
+ __unnamed_array_storage.818
+ __unnamed_array_storage.821
+ __unnamed_array_storage.824
+ __unnamed_array_storage.827
+ __unnamed_array_storage.830
+ __unnamed_array_storage.833
+ __unnamed_array_storage.836
+ __unnamed_array_storage.839
+ __unnamed_array_storage.842
+ __unnamed_array_storage.845
+ _objc_msgSend$_cameraButtonRequest
+ _objc_msgSend$_cameraCaseShutterNotifier
+ _objc_msgSend$_contextId
+ _objc_msgSend$_createCameraCaseShutterNotifierIfNeeded
+ _objc_msgSend$_createSliderForIndex:
+ _objc_msgSend$_isProResCinematicVideoSupported
+ _objc_msgSend$_semanticStyleIndexKey
+ _objc_msgSend$_semanticStylesKey
+ _objc_msgSend$_setVolumeDownButtonState:
+ _objc_msgSend$_setVolumeUpButtonState:
+ _objc_msgSend$_updateCaptureButtonNotifications
+ _objc_msgSend$_updateStateAndNotifyDelegateIfNeededForButton:
+ _objc_msgSend$_view
+ _objc_msgSend$_volumeDownButtonState
+ _objc_msgSend$_volumeUpButtonState
+ _objc_msgSend$adoptMachineReadableCodeButton:animated:
+ _objc_msgSend$analyticsDictionary
+ _objc_msgSend$avSemanticStyle
+ _objc_msgSend$buttonStyle
+ _objc_msgSend$deferHIDEventsForButtonKind:toToken:
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$generateDestinationURLWithExtension:
+ _objc_msgSend$includesVolumeButtons
+ _objc_msgSend$initWithTitle:minimumValue:maximumValue:defaultValue:
+ _objc_msgSend$initWithView:includeVolumeButtons:
+ _objc_msgSend$physicalCaptureNotifierDidChangeState:forButton:
+ _objc_msgSend$set_cameraButtonRequest:
+ _objc_msgSend$set_cameraCaseShutterNotifier:
+ _objc_msgSend$standardSemanticStyle
+ _objc_msgSend$styleWithDictionary:error:
+ _objc_msgSend$tokenForIdentifierOfCAContext:
- +[CAMCaptureConversions AVSemanticStyleForCAMSemanticStyle:]
- +[CAMCaptureConversions CAMSemanticStyleForAVSemanticStyle:presetType:]
- +[CAMSemanticStyle styleWithDictionary:support:error:]
- -[CAMExternalStorage generateDestinationURLForMode:]
- -[CAMExternalStorage generateDestinationURLForMode:].cold.1
- -[CAMSemanticStyle dictionaryRepresentationForSupport:]
- -[CAMSemanticStyleControl _toneSlider]
- -[CAMSemanticStyleControl _warmthSlider]
- GCC_except_table1039
- GCC_except_table1045
- GCC_except_table1154
- GCC_except_table1159
- GCC_except_table1164
- GCC_except_table209
- GCC_except_table537
- GCC_except_table539
- GCC_except_table593
- GCC_except_table65
- GCC_except_table752
- GCC_except_table768
- GCC_except_table821
- _OBJC_IVAR_$_CAMSemanticStyleControl.__toneSlider
- _OBJC_IVAR_$_CAMSemanticStyleControl.__warmthSlider
- ___122-[CAMCameraViewController persistenceController:didGenerateStillImageLocalPersistenceResult:forCaptureResult:fromRequest:]_block_invoke.173
- ___58-[CAMNebulaDaemonProxyManager _getProxyForExecutingBlock:]_block_invoke.74
- ___58-[CAMNebulaDaemonProxyManager _getProxyForExecutingBlock:]_block_invoke.76
- ___63-[CAMNebulaDaemonConnectionManager _getProxyForExecutingBlock:]_block_invoke.76
- ___68-[CAMViewfinderViewController _setWantsVisualTextAnalysis:animated:]_block_invoke.418
- ___72-[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]_block_invoke.928
- ___80-[CAMPersistenceController persistBurstWithIdentifier:result:completionHandler:]_block_invoke.298
- ___80-[CAMPersistenceController persistBurstWithIdentifier:result:completionHandler:]_block_invoke.298.cold.1
- ___82-[CAMPersistenceController performDeferredRemotePersistenceWithCompletionHandler:]_block_invoke.296
- ___94-[CAMCameraViewController _handleCTMVideoLocalPersistenceResult:forCaptureResult:fromRequest:]_block_invoke.182
- ___block_descriptor_41_e8_32s_e33_v32?0"CAMSemanticStyle"8Q16^B24ls32l8
- ___block_literal_global.1004
- ___block_literal_global.1146
- ___block_literal_global.255
- ___block_literal_global.293
- ___block_literal_global.303
- ___block_literal_global.440
- ___block_literal_global.462
- ___block_literal_global.79
- ___block_literal_global.82
- __backgroundImage.onceToken.216
- __unnamed_array_storage.1010
- __unnamed_array_storage.1013
- __unnamed_array_storage.1016
- __unnamed_array_storage.1069
- __unnamed_array_storage.326
- __unnamed_array_storage.332
- __unnamed_array_storage.337
- __unnamed_array_storage.340
- __unnamed_array_storage.343
- __unnamed_array_storage.346
- __unnamed_array_storage.349
- __unnamed_array_storage.352
- __unnamed_array_storage.377
- __unnamed_array_storage.380
- __unnamed_array_storage.383
- __unnamed_array_storage.388
- __unnamed_array_storage.3889
- __unnamed_array_storage.3892
- __unnamed_array_storage.3895
- __unnamed_array_storage.391
- __unnamed_array_storage.396
- __unnamed_array_storage.428
- __unnamed_array_storage.431
- __unnamed_array_storage.434
- __unnamed_array_storage.437
- __unnamed_array_storage.440
- __unnamed_array_storage.443
- __unnamed_array_storage.446
- __unnamed_array_storage.625
- __unnamed_array_storage.646
- __unnamed_array_storage.757
- __unnamed_array_storage.760
- __unnamed_array_storage.763
- __unnamed_array_storage.766
- __unnamed_array_storage.769
- __unnamed_array_storage.772
- __unnamed_array_storage.775
- __unnamed_array_storage.778
- __unnamed_array_storage.781
- __unnamed_array_storage.784
- __unnamed_array_storage.787
- __unnamed_array_storage.790
- __unnamed_array_storage.793
- __unnamed_array_storage.796
- __unnamed_array_storage.799
- __unnamed_array_storage.802
- __unnamed_array_storage.805
- __unnamed_array_storage.808
- __unnamed_array_storage.811
- __unnamed_array_storage.814
- __unnamed_array_storage.817
- __unnamed_array_storage.820
- __unnamed_array_storage.823
- __unnamed_array_storage.826
- __unnamed_array_storage.829
- __unnamed_array_storage.832
- __unnamed_array_storage.835
- __unnamed_array_storage.838
- __unnamed_array_storage.841
- _objc_msgSend$AVSemanticStyleForCAMSemanticStyle:
- _objc_msgSend$_toneSlider
- _objc_msgSend$_warmthSlider
- _objc_msgSend$arrayWithObjects:
- _objc_msgSend$dictionaryRepresentationForSupport:
- _objc_msgSend$generateDestinationURLForMode:
- _objc_msgSend$styleWithDictionary:support:error:
- _objc_msgSend$toneBias
CStrings:
+ "%{public}@: Stop capturing burst"
+ "@\"<BSInvalidatable>\""
+ "@\"<CAMCaptureStyle>\""
+ "@\"<CAMCaptureStyle>\"24@0:8@\"CAMFullscreenViewfinder\"16"
+ "@\"<CAMPhysicalCaptureNotifierDelegate>\""
+ "@\"AVSemanticStyle\"16@0:8"
+ "@\"CAMPhysicalCaptureNotifier\""
+ "@32@0:8@16^@24"
+ "CAMCaptureStyle"
+ "CAMFeatureDevelopmentCinematicProRes"
+ "CAMPhysicalCaptureNotifier"
+ "CAMPhysicalCaptureNotifierDelegate"
+ "CAMSemanticStyleControl.m"
+ "Expecting style object to be of class CAMSemanticStyle: %@"
+ "FrontCameraRotationForISP"
+ "T@\"<BSInvalidatable>\",&,N,V__cameraButtonRequest"
+ "T@\"<CAMCaptureStyle>\",&,D,N"
+ "T@\"<CAMCaptureStyle>\",&,N,SsetSemanticStyle:,V_semanticStyle"
+ "T@\"<CAMCaptureStyle>\",&,N,V_semanticStyle"
+ "T@\"<CAMCaptureStyle>\",R,N,V__style"
+ "T@\"<CAMCaptureStyle>\",R,N,V_previewSemanticStyle"
+ "T@\"<CAMCaptureStyle>\",R,N,V_semanticStyle"
+ "T@\"<CAMCaptureStyle>\",R,N,V_standardSemanticStyle"
+ "T@\"<CAMPhysicalCaptureNotifierDelegate>\",W,N,V_delegate"
+ "T@\"AVSemanticStyle\",R,N"
+ "T@\"CAMPhysicalCaptureNotifier\",&,N,V__cameraCaseShutterNotifier"
+ "T@\"NSArray\",R,N,V__allSliders"
+ "T@\"NSString\",?,R,C"
+ "T@\"UIView\",R,N,V__view"
+ "T@\"UIWindow\",?,&,N"
+ "TB,?,R,N"
+ "TB,R,N,G_isProResCinematicVideoSupported,V__proResCinematicVideoSupported"
+ "TB,R,N,V_includesVolumeButtons"
+ "TQ,?,R,N"
+ "TS,?,R,N"
+ "Tq,N,S_setState:,V_state"
+ "Tq,N,S_setVolumeDownButtonState:,V__volumeDownButtonState"
+ "Tq,N,S_setVolumeUpButtonState:,V__volumeUpButtonState"
+ "T{?=qiIq},?,R,N"
+ "Unable to generate a valid BKSHIDEventDeferringToken from a view's window (%{public}@), not deferring camera case events for SBSHardwareButtonService"
+ "_UIApplicationCameraShutterButtonDownNotification"
+ "_UIApplicationCameraShutterButtonUpNotification"
+ "__cameraButtonRequest"
+ "__cameraCaseShutterNotifier"
+ "__proResCinematicVideoSupported"
+ "__view"
+ "__volumeDownButtonState"
+ "__volumeUpButtonState"
+ "_cameraButtonRequest"
+ "_cameraCaseShutterNotifier"
+ "_contextId"
+ "_createCameraCaseShutterNotifierIfNeeded"
+ "_createSliderForIndex:"
+ "_handleVolumeDownButtonDownNotification:"
+ "_handleVolumeDownButtonUpNotification:"
+ "_handleVolumeUpButtonDownNotification:"
+ "_handleVolumeUpButtonUpNotification:"
+ "_includesVolumeButtons"
+ "_isProResCinematicVideoSupported"
+ "_proResCinematicVideoSupported"
+ "_semanticStyleIndexKey"
+ "_semanticStylesKey"
+ "_setVolumeDownButtonState:"
+ "_setVolumeUpButtonState:"
+ "_standardSemanticStyle"
+ "_updateCaptureButtonNotifications"
+ "_updateStateAndNotifyDelegateIfNeededForButton:"
+ "_volumeDownButtonState"
+ "_volumeUpButtonState"
+ "adoptMachineReadableCodeButton:animated:"
+ "analyticsDictionary"
+ "avSemanticStyle"
+ "buttonStyle"
+ "deferHIDEventsForButtonKind:toToken:"
+ "dictionaryRepresentation"
+ "generateDestinationURLWithExtension:"
+ "includesVolumeButtons"
+ "initWithTitle:minimumValue:maximumValue:defaultValue:"
+ "initWithView:includeVolumeButtons:"
+ "physicalCaptureNotifierDidChangeState:forButton:"
+ "set_cameraButtonRequest:"
+ "set_cameraCaseShutterNotifier:"
+ "standardSemanticStyle"
+ "styleWithDictionary:error:"
+ "tokenForIdentifierOfCAContext:"
+ "v32@0:8@\"CAMPhysicalCaptureNotifier\"16q24"
+ "v32@?0@\"<CAMCaptureStyle>\"8Q16^B24"
+ "\x92\xf0\xf0\xf0\xf0\xf0\xf0\xf0Q\xf0\xf0\xf0\xb3\x11"
+ "\xbf\x031\xf0\xe1!\x11?\x05/\r-2\x12\x14!B\x12\x1f\x011a"
+ "\xf0\xf0\xf0\xc1Rq\xf0\xf0!x"
- "@\"CAMSemanticStyle\"24@0:8@\"CAMFullscreenViewfinder\"16"
- "@\"CEKExpandingSlider\""
- "@40@0:8@16Q24^@32"
- "AVSemanticStyleForCAMSemanticStyle:"
- "CAMSemanticStyleForAVSemanticStyle:presetType:"
- "SemanticStyleCustomized"
- "SemanticStylePreset"
- "SemanticStyleToneBias"
- "SemanticStyleWarmthBias"
- "T@\"CAMSemanticStyle\",&,D,N"
- "T@\"CAMSemanticStyle\",&,N,SsetSemanticStyle:,V_semanticStyle"
- "T@\"CAMSemanticStyle\",R,N,V__style"
- "T@\"CAMSemanticStyle\",R,N,V_previewSemanticStyle"
- "T@\"CAMSemanticStyle\",R,N,V_semanticStyle"
- "T@\"CEKExpandingSlider\",R,N,V__toneSlider"
- "T@\"CEKExpandingSlider\",R,N,V__warmthSlider"
- "T@\"NSMutableArray\",R,N,V__allSliders"
- "T@\"UIWindow\",&,N"
- "__toneSlider"
- "__warmthSlider"
- "_toneSlider"
- "_warmthSlider"
- "arrayWithObjects:"
- "dictionaryRepresentationForSupport:"
- "generateDestinationURLForMode:"
- "styleWithDictionary:support:error:"
- "toneBias"
- "v32@?0@\"CAMSemanticStyle\"8Q16^B24"
- "\x92\xf0\xf0\xf0\xf0\xf0\xf0\xf0Q\xf0\xf0\xf0\xa3\x11"
- "\xbf\x031\xf0\xe1!\x11?\x05/\r,2\x12\x14!B\x12\x1f\x011a"
- "\xf0\xf0\xf0\xf0\"q\xf0\xf0!x"

```
