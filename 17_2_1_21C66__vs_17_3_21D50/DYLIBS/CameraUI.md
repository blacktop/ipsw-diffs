## CameraUI

> `/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`

```diff

-4007.14.0.0.0
-  __TEXT.__text: 0x1dec1c
+4008.3.2.0.0
+  __TEXT.__text: 0x1de394
   __TEXT.__auth_stubs: 0x20a0
-  __TEXT.__objc_methlist: 0x152a0
+  __TEXT.__objc_methlist: 0x15230
   __TEXT.__const: 0x2d70
   __TEXT.__gcc_except_tab: 0x2404
-  __TEXT.__cstring: 0x12763
-  __TEXT.__oslogstring: 0x11f21
+  __TEXT.__cstring: 0x127fb
+  __TEXT.__oslogstring: 0x11d7c
   __TEXT.__dlopen_cstrs: 0x310
   __TEXT.__ustring: 0x8
-  __TEXT.__objc_const_ax: 0xe9b0
-  __TEXT.__unwind_info: 0x84f0
-  __TEXT.__objc_classname: 0x4a4d
-  __TEXT.__objc_methname: 0x80281
-  __TEXT.__objc_methtype: 0xd84d
-  __TEXT.__objc_stubs: 0x49e40
-  __DATA_CONST.__got: 0x1170
-  __DATA_CONST.__const: 0x6290
-  __DATA_CONST.__objc_classlist: 0xed0
+  __TEXT.__objc_const_ax: 0xe9c0
+  __TEXT.__unwind_info: 0x84c4
+  __TEXT.__objc_classname: 0x4a20
+  __TEXT.__objc_methname: 0x7ff67
+  __TEXT.__objc_methtype: 0xd7d4
+  __TEXT.__objc_stubs: 0x49c60
+  __DATA_CONST.__got: 0x1150
+  __DATA_CONST.__const: 0x6248
+  __DATA_CONST.__objc_classlist: 0xec8
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x5e0
+  __DATA_CONST.__objc_protolist: 0x5d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3b978
-  __DATA_CONST.__objc_selrefs: 0x146a0
+  __DATA_CONST.__objc_const: 0x3b798
+  __DATA_CONST.__objc_selrefs: 0x14610
   __DATA_CONST.__objc_arraydata: 0xcf0
-  __AUTH_CONST.__cfstring: 0x12a80
-  __AUTH_CONST.__objc_const: 0x9fc8
+  __AUTH_CONST.__cfstring: 0x12ae0
+  __AUTH_CONST.__objc_const: 0x9f80
   __AUTH_CONST.__objc_intobj: 0x15a8
   __AUTH_CONST.__objc_doubleobj: 0x500
   __AUTH_CONST.__objc_dictobj: 0x1e0

   __AUTH_CONST.__const: 0xa80
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x1060
-  __AUTH.__objc_data: 0x2b48
+  __AUTH.__objc_data: 0x2af8
   __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x16a0
+  __DATA.__objc_classrefs: 0x1670
   __DATA.__objc_superrefs: 0xc68
-  __DATA.__objc_ivar: 0x31b4
+  __DATA.__objc_ivar: 0x3198
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x4720
+  __DATA.__data: 0x46c0
   __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0x68d8
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x290
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/AVKit.framework/AVKit
-  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/ACTFramework.framework/ACTFramework
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
-  - /System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 15D0EC3D-A23E-322A-A53A-B708C21F393C
-  Functions: 13806
-  Symbols:   47094
-  CStrings:  24865
+  UUID: F101EBF3-0F7C-3166-8A05-B6E9F560D603
+  Functions: 13794
+  Symbols:   47022
+  CStrings:  24832
 
Symbols:
+ -[CAMDescriptionOverlayView _buttonTitleTransformerForTextStyle:]
+ -[CAMDescriptionOverlayView detailButtonTapped]
+ -[CAMDescriptionOverlayView detailTextShouldHaveVibrancyEffect]
+ -[CAMDescriptionOverlayView handleDescriptionLabelTapped:]
+ -[CAMDescriptionOverlayView infoTextStyleUsingNarrowWidth:]
+ -[CAMSpatialVideoDescriptionOverlayView _didTapDetail]
+ -[CAMSpatialVideoDescriptionOverlayView _maxTextWidthForNarrowWidth:isLandscape:usingFontSizeMultiplier:]
+ -[CAMSpatialVideoDescriptionOverlayView acknowledgmentTextUsingNarrowWidth:]
+ -[CAMSpatialVideoDescriptionOverlayView attributedDescriptionTextUsingNarrowWidth:]
+ -[CAMSpatialVideoDescriptionOverlayView detailButtonTapped]
+ -[CAMSpatialVideoDescriptionOverlayView detailTextShouldHaveVibrancyEffect]
+ -[CAMSpatialVideoDescriptionOverlayView detailTextUsingNarrowWidth:]
+ -[CAMSpatialVideoDescriptionOverlayView handleDescriptionLabelTapped:]
+ -[CAMSpatialVideoDescriptionOverlayView infoTextUsingNarrowWidth:]
+ -[CAMSpatialVideoDescriptionOverlayView isTitleMultiline]
+ -[CAMSpatialVideoDescriptionOverlayView maxDescriptionTextWidthForNarrowWidth:isLandscape:usingFontSizeMultiplier:]
+ -[CAMSpatialVideoDescriptionOverlayView maxTitleTextWidthForNarrowWidth:isLandscape:]
+ -[CAMSpatialVideoDescriptionOverlayView setOrientation:animated:]
+ -[CAMSpatialVideoDescriptionOverlayView set_didTapDetail:]
+ -[CAMSpatialVideoDescriptionOverlayView titleTextUsingNarrowWidth:]
+ -[CAMUserPreferences didAcknowledgeSpatialVideoOverlayDescription]
+ -[CAMUserPreferences setDidAcknowledgeSpatialVideoOverlayDescription:]
+ -[CAMUserPreferences setSpatialVideoControlEnabled:]
+ -[CAMViewfinderViewController _embedDescriptionOverlayViewIfNecessaryForGraphConfiguration:]
+ -[CAMViewfinderViewController _handleUserChangedSpatialVideoEnabled:]
+ -[CAMViewfinderViewController _shouldShowDescriptionOverlayViewForGraphConfiguration:]
+ -[CAMViewfinderViewController _shouldShowDescriptionOverlayViewForGraphConfiguration:viewClass:]
+ GCC_except_table1039
+ GCC_except_table1045
+ GCC_except_table1154
+ GCC_except_table1159
+ GCC_except_table1164
+ GCC_except_table768
+ GCC_except_table821
+ GCC_except_table824
+ _CAMUserPreferenceDidAcknowledgeSpatialVideoOverlayDescription
+ _OBJC_CLASS_$_CAMSpatialVideoDescriptionOverlayView
+ _OBJC_IVAR_$_CAMSpatialVideoDescriptionOverlayView.__didTapDetail
+ _OBJC_IVAR_$_CAMUserPreferences._didAcknowledgeSpatialVideoOverlayDescription
+ _OBJC_METACLASS_$_CAMSpatialVideoDescriptionOverlayView
+ __OBJC_$_INSTANCE_METHODS_CAMSpatialVideoDescriptionOverlayView
+ __OBJC_$_INSTANCE_VARIABLES_CAMSpatialVideoDescriptionOverlayView
+ __OBJC_$_PROP_LIST_CAMSpatialVideoDescriptionOverlayView
+ __OBJC_CLASS_RO_$_CAMSpatialVideoDescriptionOverlayView
+ __OBJC_METACLASS_RO_$_CAMSpatialVideoDescriptionOverlayView
+ ___65-[CAMDescriptionOverlayView _buttonTitleTransformerForTextStyle:]_block_invoke
+ ___72-[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]_block_invoke.928
+ ___block_literal_global.1004
+ ___block_literal_global.1146
+ __unnamed_array_storage.1010
+ __unnamed_array_storage.1013
+ __unnamed_array_storage.1016
+ __unnamed_array_storage.1069
+ __unnamed_array_storage.3889
+ __unnamed_array_storage.3892
+ __unnamed_array_storage.3895
+ __unnamed_array_storage.413
+ __unnamed_array_storage.625
+ __unnamed_array_storage.646
+ __unnamed_array_storage.757
+ __unnamed_array_storage.760
+ __unnamed_array_storage.763
+ __unnamed_array_storage.766
+ __unnamed_array_storage.769
+ __unnamed_array_storage.772
+ __unnamed_array_storage.775
+ __unnamed_array_storage.778
+ __unnamed_array_storage.781
+ __unnamed_array_storage.784
+ __unnamed_array_storage.787
+ __unnamed_array_storage.790
+ __unnamed_array_storage.793
+ __unnamed_array_storage.796
+ __unnamed_array_storage.799
+ __unnamed_array_storage.802
+ __unnamed_array_storage.805
+ __unnamed_array_storage.808
+ __unnamed_array_storage.811
+ __unnamed_array_storage.814
+ __unnamed_array_storage.817
+ __unnamed_array_storage.820
+ __unnamed_array_storage.823
+ __unnamed_array_storage.826
+ __unnamed_array_storage.829
+ __unnamed_array_storage.832
+ __unnamed_array_storage.835
+ __unnamed_array_storage.838
+ __unnamed_array_storage.841
+ _objc_msgSend$_buttonTitleTransformerForTextStyle:
+ _objc_msgSend$_didTapDetail
+ _objc_msgSend$_embedDescriptionOverlayViewIfNecessaryForGraphConfiguration:
+ _objc_msgSend$_handleUserChangedSpatialVideoEnabled:
+ _objc_msgSend$_maxTextWidthForNarrowWidth:isLandscape:usingFontSizeMultiplier:
+ _objc_msgSend$_shouldShowDescriptionOverlayViewForGraphConfiguration:
+ _objc_msgSend$_shouldShowDescriptionOverlayViewForGraphConfiguration:viewClass:
+ _objc_msgSend$detailButtonTapped
+ _objc_msgSend$detailTextShouldHaveVibrancyEffect
+ _objc_msgSend$didAcknowledgeSpatialVideoOverlayDescription
+ _objc_msgSend$infoTextStyleUsingNarrowWidth:
+ _objc_msgSend$setDidAcknowledgeSpatialVideoOverlayDescription:
+ _objc_msgSend$setSpatialVideoControlEnabled:
+ _objc_msgSend$set_didTapDetail:
- +[CAMAccountController _isRealityDevice:]
- +[CAMAccountController _shouldCheckPrimaryAccountForRegisteredRealityDevices]
- +[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]
- -[CAMPhysicalCaptureNotifier .cxx_destruct]
- -[CAMPhysicalCaptureNotifier _cameraButtonRequest]
- -[CAMPhysicalCaptureNotifier _handleVolumeDownButtonDownNotification:]
- -[CAMPhysicalCaptureNotifier _handleVolumeDownButtonUpNotification:]
- -[CAMPhysicalCaptureNotifier _handleVolumeUpButtonDownNotification:]
- -[CAMPhysicalCaptureNotifier _handleVolumeUpButtonUpNotification:]
- -[CAMPhysicalCaptureNotifier _setState:]
- -[CAMPhysicalCaptureNotifier _setVolumeDownButtonState:]
- -[CAMPhysicalCaptureNotifier _setVolumeUpButtonState:]
- -[CAMPhysicalCaptureNotifier _updateCaptureButtonNotifications]
- -[CAMPhysicalCaptureNotifier _updateCaptureButtonNotifications].cold.1
- -[CAMPhysicalCaptureNotifier _updateStateAndNotifyDelegateIfNeededForButton:]
- -[CAMPhysicalCaptureNotifier _view]
- -[CAMPhysicalCaptureNotifier _volumeDownButtonState]
- -[CAMPhysicalCaptureNotifier _volumeUpButtonState]
- -[CAMPhysicalCaptureNotifier dealloc]
- -[CAMPhysicalCaptureNotifier delegate]
- -[CAMPhysicalCaptureNotifier includesVolumeButtons]
- -[CAMPhysicalCaptureNotifier initWithView:includeVolumeButtons:]
- -[CAMPhysicalCaptureNotifier isEnabled]
- -[CAMPhysicalCaptureNotifier setDelegate:]
- -[CAMPhysicalCaptureNotifier setEnabled:]
- -[CAMPhysicalCaptureNotifier set_cameraButtonRequest:]
- -[CAMPhysicalCaptureNotifier state]
- -[CAMViewfinderViewController _cameraCaseShutterNotifier]
- -[CAMViewfinderViewController _createCameraCaseShutterNotifierIfNeeded]
- -[CAMViewfinderViewController _getOrCreateDescriptionOverlayViewIfNecessaryForMode:]
- -[CAMViewfinderViewController _shouldShowDescriptionOverlayViewForMode:]
- -[CAMViewfinderViewController _shouldShowDescriptionOverlayViewForMode:viewClass:]
- -[CAMViewfinderViewController physicalCaptureNotifierDidChangeState:forButton:]
- -[CAMViewfinderViewController set_cameraCaseShutterNotifier:]
- GCC_except_table1040
- GCC_except_table1046
- GCC_except_table1155
- GCC_except_table1160
- GCC_except_table1165
- GCC_except_table770
- GCC_except_table823
- GCC_except_table826
- _CAMUserDeviceListLastCheckDate
- _OBJC_CLASS_$_AADeviceListRequest
- _OBJC_CLASS_$_AADeviceListResponse
- _OBJC_CLASS_$_ACAccountStore
- _OBJC_CLASS_$_BKSHIDEventDeferringToken
- _OBJC_CLASS_$_CAMAccountController
- _OBJC_CLASS_$_CAMPhysicalCaptureNotifier
- _OBJC_CLASS_$_SBSHardwareButtonService
- _OBJC_IVAR_$_CAMPhysicalCaptureNotifier.__cameraButtonRequest
- _OBJC_IVAR_$_CAMPhysicalCaptureNotifier.__view
- _OBJC_IVAR_$_CAMPhysicalCaptureNotifier.__volumeDownButtonState
- _OBJC_IVAR_$_CAMPhysicalCaptureNotifier.__volumeUpButtonState
- _OBJC_IVAR_$_CAMPhysicalCaptureNotifier._delegate
- _OBJC_IVAR_$_CAMPhysicalCaptureNotifier._enabled
- _OBJC_IVAR_$_CAMPhysicalCaptureNotifier._includesVolumeButtons
- _OBJC_IVAR_$_CAMPhysicalCaptureNotifier._state
- _OBJC_IVAR_$_CAMViewfinderViewController.__cameraCaseShutterNotifier
- _OBJC_METACLASS_$_CAMAccountController
- _OBJC_METACLASS_$_CAMPhysicalCaptureNotifier
- __OBJC_$_CLASS_METHODS_CAMAccountController
- __OBJC_$_INSTANCE_METHODS_CAMPhysicalCaptureNotifier
- __OBJC_$_INSTANCE_VARIABLES_CAMPhysicalCaptureNotifier
- __OBJC_$_PROP_LIST_CAMPhysicalCaptureNotifier
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAMPhysicalCaptureNotifierDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CAMPhysicalCaptureNotifierDelegate
- __OBJC_$_PROTOCOL_REFS_CAMPhysicalCaptureNotifierDelegate
- __OBJC_CLASS_RO_$_CAMAccountController
- __OBJC_CLASS_RO_$_CAMPhysicalCaptureNotifier
- __OBJC_LABEL_PROTOCOL_$_CAMPhysicalCaptureNotifierDelegate
- __OBJC_METACLASS_RO_$_CAMAccountController
- __OBJC_METACLASS_RO_$_CAMPhysicalCaptureNotifier
- __OBJC_PROTOCOL_$_CAMPhysicalCaptureNotifierDelegate
- __UIApplicationVolumeDownButtonDownNotification
- __UIApplicationVolumeDownButtonUpNotification
- __UIApplicationVolumeUpButtonDownNotification
- __UIApplicationVolumeUpButtonUpNotification
- ___43-[CAMDescriptionOverlayView initWithFrame:]_block_invoke
- ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke
- ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke.21
- ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke_2
- ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke_2.cold.1
- ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke_2.cold.2
- ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke_2.cold.3
- ___70+[CAMAccountController checkPrimaryAccountForRegisteredRealityDevices]_block_invoke_2.cold.4
- ___72-[CAMViewfinderViewController _createPhysicalCaptureInteractionIfNeeded]_block_invoke.929
- ___block_descriptor_40_e46_v32?0"AARequest"8"AAResponse"16"NSError"24l
- ___block_descriptor_48_e8_32r_e25_v32?0"AADevice"8Q16^B24lr32l8
- ___block_literal_global.1006
- ___block_literal_global.1147
- __unnamed_array_storage.1001
- __unnamed_array_storage.1004
- __unnamed_array_storage.1007
- __unnamed_array_storage.1060
- __unnamed_array_storage.3899
- __unnamed_array_storage.3902
- __unnamed_array_storage.3905
- __unnamed_array_storage.410
- __unnamed_array_storage.626
- __unnamed_array_storage.647
- __unnamed_array_storage.758
- __unnamed_array_storage.761
- __unnamed_array_storage.764
- __unnamed_array_storage.767
- __unnamed_array_storage.770
- __unnamed_array_storage.773
- __unnamed_array_storage.776
- __unnamed_array_storage.779
- __unnamed_array_storage.782
- __unnamed_array_storage.785
- __unnamed_array_storage.788
- __unnamed_array_storage.791
- __unnamed_array_storage.794
- __unnamed_array_storage.797
- __unnamed_array_storage.800
- __unnamed_array_storage.803
- __unnamed_array_storage.806
- __unnamed_array_storage.809
- __unnamed_array_storage.812
- __unnamed_array_storage.815
- __unnamed_array_storage.818
- __unnamed_array_storage.821
- __unnamed_array_storage.824
- __unnamed_array_storage.827
- __unnamed_array_storage.830
- __unnamed_array_storage.833
- __unnamed_array_storage.836
- __unnamed_array_storage.839
- __unnamed_array_storage.842
- _objc_msgSend$_cameraButtonRequest
- _objc_msgSend$_cameraCaseShutterNotifier
- _objc_msgSend$_contextId
- _objc_msgSend$_createCameraCaseShutterNotifierIfNeeded
- _objc_msgSend$_getOrCreateDescriptionOverlayViewIfNecessaryForMode:
- _objc_msgSend$_isRealityDevice:
- _objc_msgSend$_setVolumeDownButtonState:
- _objc_msgSend$_setVolumeUpButtonState:
- _objc_msgSend$_shouldCheckPrimaryAccountForRegisteredRealityDevices
- _objc_msgSend$_shouldShowDescriptionOverlayViewForMode:
- _objc_msgSend$_shouldShowDescriptionOverlayViewForMode:viewClass:
- _objc_msgSend$_updateCaptureButtonNotifications
- _objc_msgSend$_updateStateAndNotifyDelegateIfNeededForButton:
- _objc_msgSend$_view
- _objc_msgSend$_volumeDownButtonState
- _objc_msgSend$_volumeUpButtonState
- _objc_msgSend$aa_primaryAppleAccount
- _objc_msgSend$checkPrimaryAccountForRegisteredRealityDevices
- _objc_msgSend$defaultStore
- _objc_msgSend$deferHIDEventsForButtonKind:toToken:
- _objc_msgSend$includesVolumeButtons
- _objc_msgSend$initWithAccount:
- _objc_msgSend$initWithView:includeVolumeButtons:
- _objc_msgSend$performRequestWithHandler:
- _objc_msgSend$physicalCaptureNotifierDidChangeState:forButton:
- _objc_msgSend$set_cameraButtonRequest:
- _objc_msgSend$set_cameraCaseShutterNotifier:
- _objc_msgSend$statusCode
- _objc_msgSend$tokenForIdentifierOfCAContext:
CStrings:
+ "@?24@0:8@16"
+ "B32@0:8@16^#24"
+ "CAMSpatialVideoDescriptionOverlayView"
+ "CAMUserPreferenceDidAcknowledgeSpatialVideoOverlayDescription"
+ "SPATIAL_VIDEO_CAPTURE_OVERLAY_CONTINUE"
+ "SPATIAL_VIDEO_CAPTURE_OVERLAY_DESCRIPTION"
+ "SPATIAL_VIDEO_CAPTURE_OVERLAY_DESCRIPTION_LINK"
+ "SPATIAL_VIDEO_CAPTURE_OVERLAY_SET_UP_LATER"
+ "SPATIAL_VIDEO_CAPTURE_OVERLAY_TITLE"
+ "TB,N,V__didTapDetail"
+ "TB,N,V_didAcknowledgeSpatialVideoOverlayDescription"
+ "TB,N,V_spatialVideoControlEnabled"
+ "__didTapDetail"
+ "_buttonTitleTransformerForTextStyle:"
+ "_didAcknowledgeSpatialVideoOverlayDescription"
+ "_didTapDetail"
+ "_embedDescriptionOverlayViewIfNecessaryForGraphConfiguration:"
+ "_handleUserChangedSpatialVideoEnabled:"
+ "_maxTextWidthForNarrowWidth:isLandscape:usingFontSizeMultiplier:"
+ "_shouldShowDescriptionOverlayViewForGraphConfiguration:"
+ "_shouldShowDescriptionOverlayViewForGraphConfiguration:viewClass:"
+ "detailButtonTapped"
+ "detailTextShouldHaveVibrancyEffect"
+ "didAcknowledgeSpatialVideoOverlayDescription"
+ "handleDescriptionLabelTapped:"
+ "https://support.apple.com/guide/iphone/record-spatial-videos-for-apple-vision-pro-iph6e3a6d4fe/ios"
+ "infoTextStyleUsingNarrowWidth:"
+ "setDidAcknowledgeSpatialVideoOverlayDescription:"
+ "setSpatialVideoControlEnabled:"
+ "set_didTapDetail:"
+ "\x92\xf0\xf0\xf0\xf0\xf0\xf0\xf0Q\xf0\xf0\xf0\xa3\x11"
+ "\xbf\x031\xf0\xe1!\x11?\x05/\r,2\x12\x14!B\x12\x1f\x011a"
- "@\"<BSInvalidatable>\""
- "@\"<CAMPhysicalCaptureNotifierDelegate>\""
- "@\"CAMPhysicalCaptureNotifier\""
- "B32@0:8q16^#24"
- "CAMAccountController"
- "CAMPhysicalCaptureNotifier"
- "CAMPhysicalCaptureNotifierDelegate"
- "CAMUserDeviceListLastCheckDate"
- "Device list request failed with missing response and error: %{public}@"
- "Device list request failed with response error: %{public}@ and request error: %{public}@"
- "Device list request succeeded with no reality device found"
- "Device list request succeeded, reality device found"
- "RealityDevice"
- "T@\"<BSInvalidatable>\",&,N,V__cameraButtonRequest"
- "T@\"<CAMPhysicalCaptureNotifierDelegate>\",W,N,V_delegate"
- "T@\"CAMPhysicalCaptureNotifier\",&,N,V__cameraCaseShutterNotifier"
- "T@\"UIView\",R,N,V__view"
- "TB,R,N,V_includesVolumeButtons"
- "TB,R,N,V_spatialVideoControlEnabled"
- "Tq,N,S_setState:,V_state"
- "Tq,N,S_setVolumeDownButtonState:,V__volumeDownButtonState"
- "Tq,N,S_setVolumeUpButtonState:,V__volumeUpButtonState"
- "Unable to generate a valid BKSHIDEventDeferringToken from a view's window (%{public}@), not deferring camera case events for SBSHardwareButtonService"
- "_UIApplicationCameraShutterButtonDownNotification"
- "_UIApplicationCameraShutterButtonUpNotification"
- "__cameraButtonRequest"
- "__cameraCaseShutterNotifier"
- "__view"
- "__volumeDownButtonState"
- "__volumeUpButtonState"
- "_cameraButtonRequest"
- "_cameraCaseShutterNotifier"
- "_contextId"
- "_createCameraCaseShutterNotifierIfNeeded"
- "_getOrCreateDescriptionOverlayViewIfNecessaryForMode:"
- "_handleVolumeDownButtonDownNotification:"
- "_handleVolumeDownButtonUpNotification:"
- "_handleVolumeUpButtonDownNotification:"
- "_handleVolumeUpButtonUpNotification:"
- "_includesVolumeButtons"
- "_isRealityDevice:"
- "_setVolumeDownButtonState:"
- "_setVolumeUpButtonState:"
- "_shouldCheckPrimaryAccountForRegisteredRealityDevices"
- "_shouldShowDescriptionOverlayViewForMode:"
- "_shouldShowDescriptionOverlayViewForMode:viewClass:"
- "_updateCaptureButtonNotifications"
- "_updateStateAndNotifyDelegateIfNeededForButton:"
- "_volumeDownButtonState"
- "_volumeUpButtonState"
- "aa_primaryAppleAccount"
- "checkPrimaryAccountForRegisteredRealityDevices"
- "defaultStore"
- "deferHIDEventsForButtonKind:toToken:"
- "includesVolumeButtons"
- "initWithAccount:"
- "initWithView:includeVolumeButtons:"
- "performRequestWithHandler:"
- "physicalCaptureNotifierDidChangeState:forButton:"
- "set_cameraButtonRequest:"
- "set_cameraCaseShutterNotifier:"
- "statusCode"
- "tokenForIdentifierOfCAContext:"
- "v32@0:8@\"CAMPhysicalCaptureNotifier\"16q24"
- "v32@?0@\"AADevice\"8Q16^B24"
- "v32@?0@\"AARequest\"8@\"AAResponse\"16@\"NSError\"24"
- "\x92\xf0\xf0\xf0\xf0\xf0\xf0\xf0Q\xf0\xf0\xf0\xb3\x11"
- "\xbf\x031\xf0\xe1!\x11?\x05/\r-2\x12\x14!B\x12\x1f\x011a"

```
