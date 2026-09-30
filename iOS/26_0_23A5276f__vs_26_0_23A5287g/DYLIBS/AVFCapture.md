## AVFCapture

> `/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`

```diff

-655.0.0.122.4
-  __TEXT.__text: 0x150278
+659.0.0.0.4
+  __TEXT.__text: 0x1513b0
   __TEXT.__auth_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0xde9c
+  __TEXT.__objc_methlist: 0xdef4
   __TEXT.__const: 0x960
-  __TEXT.__gcc_except_tab: 0x28b4
-  __TEXT.__cstring: 0x2798a
-  __TEXT.__oslogstring: 0x1f1bd
+  __TEXT.__gcc_except_tab: 0x28b8
+  __TEXT.__cstring: 0x27aa2
+  __TEXT.__oslogstring: 0x1f59e
   __TEXT.__dlopen_cstrs: 0x178
   __TEXT.__ustring: 0x54
-  __TEXT.__unwind_info: 0x45e8
-  __TEXT.__objc_classname: 0x17e6
-  __TEXT.__objc_methname: 0x26e2c
-  __TEXT.__objc_methtype: 0x3c28
-  __TEXT.__objc_stubs: 0x16b00
-  __DATA_CONST.__got: 0x27c8
-  __DATA_CONST.__const: 0x7088
+  __TEXT.__unwind_info: 0x4780
+  __TEXT.__objc_classname: 0x17ef
+  __TEXT.__objc_methname: 0x26f6b
+  __TEXT.__objc_methtype: 0x3c6c
+  __TEXT.__objc_stubs: 0x16c40
+  __DATA_CONST.__got: 0x27a8
+  __DATA_CONST.__const: 0x7100
   __DATA_CONST.__objc_classlist: 0x580
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x71d8
+  __DATA_CONST.__objc_selrefs: 0x7220
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x4c0
   __DATA_CONST.__objc_arraydata: 0x428
   __AUTH_CONST.__auth_got: 0xdb0
   __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x13920
-  __AUTH_CONST.__objc_const: 0x168a0
+  __AUTH_CONST.__cfstring: 0x13ae0
+  __AUTH_CONST.__objc_const: 0x16920
   __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x2e8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x17d8
+  __DATA.__objc_ivar: 0x17e0
   __DATA.__data: 0xc60
   __DATA.__common: 0x280
   __DATA.__bss: 0x6f0

   __DATA_DIRTY.__common: 0x2b0
   __DATA_DIRTY.__bss: 0x3d0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
+  - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1B713B7B-26AD-3409-AB9D-CFD501414446
-  Functions: 5907
-  Symbols:   20970
-  CStrings:  13381
+  UUID: 6A28D6FA-F0AA-3DF2-BEE3-283ACE1FC92A
+  Functions: 5916
+  Symbols:   21000
+  CStrings:  13436
 
Symbols:
+ -[AVCaptureFigAudioDevice _currentAudioInputDeviceLocalizedName:]
+ -[AVCaptureFigAudioDevice _currentAudioInputRouteIsBuiltInMic]
+ -[AVCaptureFigAudioDevice _systemHasAudioInputDevice]
+ -[AVCaptureFigAudioDevice _updateStateForInputDevice:]
+ -[AVCaptureFigAudioDevice _updateStateForInputDevice:].cold.1
+ -[AVCaptureFigAudioDevice audioInputDeviceDidChangeHandler:]
+ -[AVCaptureFigAudioDevice manufacturer]
+ -[AVCaptureFigAudioDevice setAllowsBluetoothHighQualityRecording:]
+ -[AVCaptureSession _setAudioInputDeviceHighQualityBluetoothEnabled:]
+ -[AVInputDevice(Equality) isEqualToInputDevice:]
+ GCC_except_table115
+ GCC_except_table137
+ GCC_except_table141
+ GCC_except_table150
+ GCC_except_table164
+ GCC_except_table172
+ GCC_except_table174
+ GCC_except_table178
+ GCC_except_table182
+ GCC_except_table184
+ GCC_except_table186
+ GCC_except_table188
+ GCC_except_table194
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table216
+ GCC_except_table218
+ GCC_except_table220
+ GCC_except_table492
+ _AVAUVoiceIOBundleIDIsFaceTimeVariant
+ _AVGQFrontFacingCameraDeferredPrewarmingDisabled
+ _AVInputContextInputDeviceDidChangeNotification
+ _OBJC_CLASS_$_AVInputContext
+ _OBJC_CLASS_$_AVInputDevice
+ _OBJC_CLASS_$_AVInputDeviceDiscoverySession
+ _OBJC_IVAR_$_AVCaptureFigAudioDevice._allowsBluetoothHighQualityRecording
+ _OBJC_IVAR_$_AVCaptureFigAudioDevice._committedInputDevice
+ _OBJC_IVAR_$_AVCaptureFigAudioDevice._inputContext
+ _OBJC_IVAR_$_AVCaptureFigAudioDevice._inputDeviceDiscoverySession
+ _OBJC_IVAR_$_AVCaptureFigAudioDevice._isConnectedLock
+ __OBJC_$_CATEGORY_AVInputDevice_$_Equality
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_AVInputDevice_$_Equality
+ ___54-[AVCaptureFigAudioDevice _updateStateForInputDevice:]_block_invoke
+ ___60-[AVCaptureFigAudioDevice audioInputDeviceDidChangeHandler:]_block_invoke
+ ___66-[AVCaptureFigAudioDevice setAllowsBluetoothHighQualityRecording:]_block_invoke
+ ___block_descriptor_50_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_literal_global.1102
+ ___block_literal_global.1104
+ ___block_literal_global.1109
+ ___block_literal_global.1372
+ ___block_literal_global.1379
+ __inputDeviceString
+ _objc_msgSend$_currentAudioInputDeviceLocalizedName:
+ _objc_msgSend$_currentAudioInputRouteIsBuiltInMic
+ _objc_msgSend$_setAudioInputDeviceHighQualityBluetoothEnabled:
+ _objc_msgSend$_systemHasAudioInputDevice
+ _objc_msgSend$_updateStateForInputDevice:
+ _objc_msgSend$availableInputDevices
+ _objc_msgSend$deviceName
+ _objc_msgSend$deviceSubType
+ _objc_msgSend$initWithDeviceFeatures:
+ _objc_msgSend$inputDevice
+ _objc_msgSend$isEqualToInputDevice:
+ _objc_msgSend$isHighQualityContentCaptureEnabled
+ _objc_msgSend$setAllowsBluetoothHighQualityRecording:
+ _objc_msgSend$setAudioSessionID:
+ _objc_msgSend$setCategory:withOptions:error:
+ _objc_msgSend$setDiscoveryMode:forClientIdentifiers:
+ _objc_msgSend$sharedSystemAudioInputContext
+ _objc_msgSend$supportsHighQualityContentCapture
- -[AVCaptureFigAudioDevice audioInputDeviceLocalizedNameDidChangeHandler:]
- -[AVCaptureFigAudioDevice audioInputDevicesDidChangeHandler:]
- -[AVCaptureFigAudioDevice currentAudioInputRouteIsBuiltInMic:]
- GCC_except_table136
- GCC_except_table162
- GCC_except_table170
- GCC_except_table173
- GCC_except_table177
- GCC_except_table179
- GCC_except_table185
- GCC_except_table190
- GCC_except_table198
- GCC_except_table202
- GCC_except_table204
- GCC_except_table207
- GCC_except_table213
- GCC_except_table217
- GCC_except_table219
- GCC_except_table491
- GCC_except_table98
- _AVAudioSessionPortBuiltInMic
- _AVSystemController_ActiveInputRouteForPlayAndRecordNoBluetoothAttribute
- _AVSystemController_ActiveInputRouteForPlayAndRecordNoBluetoothDidChangeNotification
- _AVSystemController_SubscribeToNotificationsAttribute
- _AVSystemController_SystemHasAudioInputDeviceExcludingBluetoothAttribute
- _AVSystemController_SystemHasAudioInputDeviceExcludingBluetoothDidChangeNotification
- _OBJC_CLASS_$_AVSystemController
- _OBJC_IVAR_$_AVCaptureDevice._manufacturer
- _OBJC_IVAR_$_AVCaptureFigAudioDevice._localizedNameFirstQueryGroup
- _OBJC_IVAR_$_AVCaptureFigAudioDevice._localizedNameFirstQueryQueue
- ___53-[AVCaptureFigAudioDevice _initWithFigCaptureSource:]_block_invoke_2
- ___73-[AVCaptureFigAudioDevice audioInputDeviceLocalizedNameDidChangeHandler:]_block_invoke
- ___73-[AVCaptureFigAudioDevice audioInputDeviceLocalizedNameDidChangeHandler:]_block_invoke_2
- ___block_literal_global.1101
- ___block_literal_global.1103
- ___block_literal_global.1108
- ___block_literal_global.1375
- ___block_literal_global.1382
- _objc_msgSend$attributeForKey:
- _objc_msgSend$availableInputs
- _objc_msgSend$currentAudioInputRouteIsBuiltInMic:
- _objc_msgSend$portName
- _objc_msgSend$portType
- _objc_msgSend$setAttribute:forKey:error:
- _objc_msgSend$setCategory:error:
- _objc_msgSend$sharedAVSystemController
CStrings:
+ "%p n:%@ typ:%@ styp:%@ supHQ:%d enbHQ:%d"
+ "-[AVCaptureFigAudioDevice _updateStateForInputDevice:]"
+ "-[AVCaptureFigAudioDevice _updateStateForInputDevice:]_block_invoke"
+ "-[AVCaptureFigAudioDevice setAllowsBluetoothHighQualityRecording:]_block_invoke"
+ "0fc71cd6c11007070fa06c9f109046af164392d6"
+ "4b6e3d8790e69de2ca8879c2ffd37a979da2e695"
+ "4c8026313c8deb46069197fa963180c366d4c374"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: %p updating auxSession category options to %s bluetooth high quality recording"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p Changing audioInputRouteIsBuiltInMic from %s to %s"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p Changing isConnected from %d to %d"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p Changing localized name from %{public}@ to %{public}@"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p Input device changed to nil, DS available inputs count is 0, but carrying on with last committed"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p Input device changed to nil, but last committed wasn't found in discovery session available inputs, so forgetting it"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p Input device changed to nil, found last committed in DS available inputs, so keeping it"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p discoverySession:[%d] %@"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p falling back to AudioCaptureModeAuto from mode %ld"
+ "<<<< AVCaptureFigAudioDevice >>>> %s: [Routing] %p new inputDevice: %@"
+ "<<<< AVCaptureFigAudioDevice >>>> Fig"
+ "<<<< AVCaptureSession >>>> %s: [Routing] (%p) (thread %p) Not triggering buildAndRunGraph for audioInputRouteIsBuiltInMic change due to in-progress movie recording"
+ "<<<< AVCaptureSession >>>> %s: [Routing] (%p) (thread %p) Triggering buildAndRunGraph for audioInputRouteIsBuiltInMic change %{public}@ current audioCaptureMode %ld on input %{public}@"
+ "@\"AVInputContext\""
+ "@\"AVInputDevice\""
+ "@\"AVInputDeviceDiscoverySession\""
+ "AVCaptureFigAudioDevice.m"
+ "AVGQFrontFacingCameraDeferredPrewarmingDisabled"
+ "Apple, Inc"
+ "Equality"
+ "_FigIsCurrentDispatchQueue( _audioRoutesInfoUpdateQueue )"
+ "_allowsBluetoothHighQualityRecording"
+ "_committedInputDevice"
+ "_currentAudioInputDeviceLocalizedName:"
+ "_currentAudioInputRouteIsBuiltInMic"
+ "_inputContext"
+ "_inputDeviceDiscoverySession"
+ "_isConnectedLock"
+ "_setAudioInputDeviceHighQualityBluetoothEnabled:"
+ "_systemHasAudioInputDevice"
+ "_updateStateForInputDevice:"
+ "audioInputDeviceDidChangeHandler:"
+ "availableInputDevices"
+ "bluetooth"
+ "built-in"
+ "carplay"
+ "description=CameraCapture_AVF-659.0.0.0.4"
+ "deviceName"
+ "deviceSubType"
+ "exclude"
+ "headset"
+ "include"
+ "initWithDeviceFeatures:"
+ "inputDevice"
+ "isEqualToInputDevice:"
+ "isHighQualityContentCaptureEnabled"
+ "line-in"
+ "low-energy"
+ "microphone"
+ "setAllowsBluetoothHighQualityRecording:"
+ "setAudioSessionID:"
+ "setCategory:withOptions:error:"
+ "setDiscoveryMode:forClientIdentifiers:"
+ "sharedSystemAudioInputContext"
+ "standard"
+ "supportsHighQualityContentCapture"
+ "usb"
+ "vehicle"
+ "wired"
- "-[AVCaptureFigAudioDevice audioInputDeviceLocalizedNameDidChangeHandler:]_block_invoke"
- "-[AVCaptureFigAudioDevice audioInputDeviceLocalizedNameDidChangeHandler:]_block_invoke_2"
- "6cce482db0e978aa552469d2202544b27a85953f"
- "<<<< AVCaptureFigAudioDevice >>>> %s: %@ falling back to AudioCaptureModeAuto from mode %ld"
- "<<<< AVCaptureFigAudioDevice >>>> %s: %{public}@ Changing audioInputRouteIsBuiltInMic from %d to %d"
- "<<<< AVCaptureFigAudioDevice >>>> %s: %{public}@ Changing localized name from %{public}@ to %{public}@"
- "<<<< AVCaptureSession >>>> %s: (%p) (thread %p) Triggering buildAndRunGraph for audioInputRouteIsBuiltInMic change %{public}@ current audioCaptureMode %ld on input %{public}@"
- "T@\"NSString\",R,N,V_manufacturer"
- "_localizedNameFirstQueryGroup"
- "_localizedNameFirstQueryQueue"
- "_manufacturer"
- "a1f7aeecd16c4ee262e82496405ddd12bf40fbc6"
- "attributeForKey:"
- "audioInputDeviceLocalizedNameDidChangeHandler:"
- "audioInputDevicesDidChangeHandler:"
- "availableInputs"
- "com.apple.avfoundation.audiocapturedevice.localized_name_first_query_queue"
- "currentAudioInputRouteIsBuiltInMic:"
- "description=CameraCapture_AVF-655.0.0.122.4"
- "ed6240ee295d09fa1ebcb64acd38b914cbb5013c"
- "portName"
- "portType"
- "setAttribute:forKey:error:"
- "setCategory:error:"
- "sharedAVSystemController"

```
