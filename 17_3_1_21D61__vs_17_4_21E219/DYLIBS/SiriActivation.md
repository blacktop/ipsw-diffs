## SiriActivation

> `/System/Library/PrivateFrameworks/SiriActivation.framework/SiriActivation`

```diff

-3302.13.3.1.1
-  __TEXT.__text: 0x3f40c
+3304.61.1.0.0
+  __TEXT.__text: 0x3fcc0
   __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x46a0
+  __TEXT.__objc_methlist: 0x46e0
   __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x84f4
-  __TEXT.__oslogstring: 0x5e7a
+  __TEXT.__cstring: 0x8601
+  __TEXT.__oslogstring: 0x5f1c
   __TEXT.__gcc_except_tab: 0x73c
   __TEXT.__dlopen_cstrs: 0x168
-  __TEXT.__unwind_info: 0x106c
-  __TEXT.__objc_classname: 0xd3a
-  __TEXT.__objc_methname: 0xbede
+  __TEXT.__unwind_info: 0x107c
+  __TEXT.__objc_classname: 0xd23
+  __TEXT.__objc_methname: 0xbf70
   __TEXT.__objc_methtype: 0x1d4d
-  __TEXT.__objc_stubs: 0x8220
+  __TEXT.__objc_stubs: 0x8280
   __DATA_CONST.__got: 0x1b8
-  __DATA_CONST.__const: 0x1278
-  __DATA_CONST.__objc_classlist: 0x298
+  __DATA_CONST.__const: 0x1280
+  __DATA_CONST.__objc_classlist: 0x290
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7148
-  __DATA_CONST.__objc_selrefs: 0x26a8
-  __DATA_CONST.__objc_arraydata: 0x440
+  __DATA_CONST.__objc_const: 0x7160
+  __DATA_CONST.__objc_selrefs: 0x26c0
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x488
+  __DATA_CONST.__objc_superrefs: 0x218
+  __DATA_CONST.__objc_arraydata: 0x450
   __AUTH_CONST.__cfstring: 0x3d20
-  __AUTH_CONST.__objc_const: 0x2240
+  __AUTH_CONST.__objc_const: 0x21f8
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__objc_intobj: 0x750
+  __AUTH_CONST.__objc_intobj: 0x768
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x498
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x4a0
-  __DATA.__objc_superrefs: 0x218
-  __DATA.__objc_ivar: 0x554
+  __DATA.__objc_ivar: 0x55c
   __DATA.__data: 0xe58
   __DATA.__bss: 0xa0
-  __DATA_DIRTY.__objc_data: 0x1270
+  __DATA_DIRTY.__objc_data: 0x1220
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB9F4E96-9A25-36BC-8CB9-89B88A0EB93D
-  Functions: 1724
-  Symbols:   6142
-  CStrings:  3904
+  UUID: 55E0FD9B-4B37-38FD-BD3E-A6F649C3A3D0
+  Functions: 1742
+  Symbols:   6176
+  CStrings:  3916
 
Symbols:
+ -[BluetoothDevice(SiriClientAdditions) ac_isBluetoothVehicle]
+ -[SASMyriadController _scdaCheckForAttention:withTimeout:]
+ -[SASMyriadController _scdaCheckForAttention:withTimeout:].cold.1
+ -[SASMyriadController _scdaCheckForAttention:withTimeout:].cold.2
+ -[SASMyriadController _scdaCheckForAttention:withTimeout:].cold.3
+ -[SASMyriadController _scdaCheckForAttention:withTimeout:].cold.4
+ -[SASMyriadController _scdaCheckForAttention:withTimeout:].cold.5
+ -[SASMyriadController activateForRequest:withTimeout:visible:].cold.7
+ -[SASRequestOptions setSupportsCarPlayVehicleData:]
+ -[SASRequestOptions supportsCarPlayVehicleData]
+ -[SASSystemState isConnectedToBluetoothVehicle]
+ -[SASSystemState setSupportsCarPlayVehicleData:]
+ -[SASSystemState supportsCarPlayVehicleData]
+ -[SiriActivationService _isEyesFreeEligibleWithRequest:]
+ GCC_except_table28
+ _BTDeviceGetDeviceType
+ _OBJC_IVAR_$_SASRequestOptions._supportsCarPlayVehicleData
+ _OBJC_IVAR_$_SASSystemState._supportsCarPlayVehicleData
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___93-[SiriActivationService _activatePresentationWithIdentifier:requestOptions:analyticsContext:]_block_invoke.146
+ ___block_literal_global.517
+ __unnamed_array_storage.301
+ _objc_msgSend$_isEyesFreeEligibleWithRequest:
+ _objc_msgSend$_scdaCheckForAttention:withTimeout:
+ _objc_msgSend$ac_isBluetoothVehicle
+ _objc_msgSend$faceDetectedBoostWithContext:
+ _objc_msgSend$scdaContext
+ _objc_msgSend$setSupportsCarPlayVehicleData:
+ _objc_msgSend$startObserversWithOptions:
+ _objc_msgSend$supportsCarPlayVehicleData
+ _objc_msgSend$supportsVehicleData
- +[SASTipKitSignalEmitter _checkAndEmitSignalsWithSource:forRequestOptions:]
- +[SASTipKitSignalEmitter checkAndEmitSignalsForRequestOptions:]
- GCC_except_table27
- _AFMyriadGoodnessComputeExponentialBoost
- _OBJC_CLASS_$_BMDiscoverabilitySignalEvent
- _OBJC_CLASS_$_BMStreams
- _OBJC_CLASS_$_SASTipKitSignalEmitter
- _OBJC_METACLASS_$_SASTipKitSignalEmitter
- __OBJC_$_CLASS_METHODS_SASTipKitSignalEmitter
- __OBJC_CLASS_RO_$_SASTipKitSignalEmitter
- __OBJC_METACLASS_RO_$_SASTipKitSignalEmitter
- ___93-[SiriActivationService _activatePresentationWithIdentifier:requestOptions:analyticsContext:]_block_invoke.147
- ___block_literal_global.514
- __unnamed_array_storage.296
- _objc_msgSend$_checkAndEmitSignalsWithSource:forRequestOptions:
- _objc_msgSend$checkAndEmitSignalsForRequestOptions:
- _objc_msgSend$discoverabilitySignal
- _objc_msgSend$initWithIdentifier:bundleID:context:
- _objc_msgSend$sendEvent:
- _objc_msgSend$startObservers
CStrings:
+ "%s #activation checking if EyesFree is eligible: isCarDND = %d, isDebugSettingOn = %d, isEyesFreeDevice = %d, isRequestSourceEyesFreeEligible = %d"
+ "%s #myriad exponential bump %f"
+ "%s #myriad myriadContext: %@"
+ "%s #myriad scdaContext: %@"
+ "-[SASMyriadController _scdaCheckForAttention:withTimeout:]"
+ "-[SiriActivationService _isEyesFreeEligibleWithRequest:]"
+ "/"
+ ";is(speech=%i; textInput=%i;stark=%i;CPconnected=%i;dnd=%i;rightHandDrive=%i);carDNDStatus=%@;remotePresentationBringUp=%i;supportsCarPlayVehicleData=%i"
+ "SASRequestOptionsSupportsCarPlayVehicleData"
+ "SystemShellPresentationFailure"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_supportsCarPlayVehicleData"
+ "UndirectedSpeechDuringAttending"
+ "_isEyesFreeEligibleWithRequest:"
+ "_scdaCheckForAttention:withTimeout:"
+ "_supportsCarPlayVehicleData"
+ "ac_isBluetoothVehicle"
+ "eyesfree_redesign_eyesfree_disabled"
+ "eyesfree_redesign_only_steeringwheel_enabled"
+ "faceDetectedBoostWithContext:"
+ "scdaContext"
+ "setSupportsCarPlayVehicleData:"
+ "startObserversWithOptions:"
+ "supportsCarPlayVehicleData"
+ "supportsVehicleData"
- "\x1f"
- "%s #myriad attention myriadContext: %@"
- "%s #myriad trial bump uint8_t %d"
- ";is(speech=%i; textInput=%i;stark=%i;CPconnected=%i;dnd=%i;rightHandDrive=%i);carDNDStatus=%@;remotePresentationBringUp=%i"
- "SASTipKitSignalEmitter"
- "UndirectedSpeechOnHearstRoute"
- "_checkAndEmitSignalsWithSource:forRequestOptions:"
- "checkAndEmitSignalsForRequestOptions:"
- "com.apple.siri.button.on.carplay"
- "com.apple.siri.hs.on.carplay"
- "discoverabilitySignal"
- "initWithIdentifier:bundleID:context:"
- "sendEvent:"
- "startObservers"

```
