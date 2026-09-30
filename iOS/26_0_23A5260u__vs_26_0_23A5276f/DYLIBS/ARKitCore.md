## ARKitCore

> `/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore`

```diff

-735.0.1.0.0
-  __TEXT.__text: 0x1934cc
+738.0.1.0.0
+  __TEXT.__text: 0x194494
   __TEXT.__auth_stubs: 0x3c80
-  __TEXT.__objc_methlist: 0x1109c
-  __TEXT.__const: 0x2c128
-  __TEXT.__gcc_except_tab: 0x13d08
-  __TEXT.__cstring: 0x1d8bb
-  __TEXT.__oslogstring: 0x1e3ef
+  __TEXT.__objc_methlist: 0x110dc
+  __TEXT.__const: 0x2c118
+  __TEXT.__cstring: 0x1d925
+  __TEXT.__oslogstring: 0x1e511
+  __TEXT.__gcc_except_tab: 0x13e14
   __TEXT.__ustring: 0xe6
-  __TEXT.__unwind_info: 0x6530
-  __TEXT.__objc_classname: 0x2024
-  __TEXT.__objc_methname: 0x2a16b
-  __TEXT.__objc_methtype: 0xa62a
-  __TEXT.__objc_stubs: 0x1aba0
+  __TEXT.__unwind_info: 0x6590
+  __TEXT.__objc_classname: 0x2027
+  __TEXT.__objc_methname: 0x2a2e8
+  __TEXT.__objc_methtype: 0xa641
+  __TEXT.__objc_stubs: 0x1ac00
   __DATA_CONST.__got: 0x1680
-  __DATA_CONST.__const: 0x3650
+  __DATA_CONST.__const: 0x3658
   __DATA_CONST.__objc_classlist: 0x860
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7d50
+  __DATA_CONST.__objc_selrefs: 0x7d78
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x790
-  __DATA_CONST.__objc_arraydata: 0x870
+  __DATA_CONST.__objc_arraydata: 0x880
   __AUTH_CONST.__auth_got: 0x1e58
   __AUTH_CONST.__const: 0x3c98
-  __AUTH_CONST.__cfstring: 0x10440
-  __AUTH_CONST.__objc_const: 0x3cd70
-  __AUTH_CONST.__objc_intobj: 0x3210
-  __AUTH_CONST.__objc_arrayobj: 0x5e8
+  __AUTH_CONST.__cfstring: 0x10480
+  __AUTH_CONST.__objc_const: 0x3ce20
+  __AUTH_CONST.__objc_intobj: 0x3240
   __AUTH_CONST.__objc_doubleobj: 0x380
+  __AUTH_CONST.__objc_arrayobj: 0x600
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x3660
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x1fe4
+  __DATA.__objc_ivar: 0x1ff8
   __DATA.__data: 0x1ca0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1dd8
+  __DATA.__bss: 0x1de0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1d60
-  __DATA_DIRTY.__bss: 0x4b0
+  __DATA_DIRTY.__bss: 0x4a8
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: 04CA4B53-93D4-37D5-A19D-BCB580FF92AD
-  Functions: 7754
-  Symbols:   30022
-  CStrings:  14392
+  UUID: 3B5F2A97-D300-34C6-97B6-BDA6AF011D3B
+  Functions: 7766
+  Symbols:   30055
+  CStrings:  14412
 
Symbols:
+ +[ARFaceTrackingConfiguration setShouldProvideRGBVideoFormats:]
+ +[ARFaceTrackingConfiguration shouldProvideRGBVideoFormats]
+ +[ARVideoFormat bestVideoFormatForDevicePosition:deviceType:resolution:frameRate:videoBinned:needsHDRSupport:needsMultiCamSupport:pixelFormat:]
+ +[ARVideoFormat bestVideoFormatForDevicePosition:deviceType:resolution:frameRate:videoBinned:needsHDRSupport:needsMultiCamSupport:pixelFormat:].cold.1
+ -[ARFaceTrackingConfiguration _selectedVideoFormatSupportsMulticam]
+ -[ARFrame visionDataWasDelivered]
+ -[ARImageData setVisionDataWasDelivered:]
+ -[ARImageData visionDataWasDelivered]
+ -[ARImageSensor captureHighResolutionFrameWithPhotoSettings:].cold.1
+ -[ARRemoteService initWithEndpoint:startConnection:dispatchChannelQueue:fixedPriorityQueueForXPC:]
+ -[ARRemoteService originFromWorld_Internal]
+ GCC_except_table76
+ _ARFaceTrackingAdditionalRGBFormatsDefaultsKey
+ _ARPreCheckEntitlementBoolValueInClientProcess
+ _ARPreCheckEntitlementValueInClientProcess
+ _ARPreCheckEntitlementValueInClientProcess.cold.1
+ _OBJC_IVAR_$_ARAppClipCodeTechnique._prepared
+ _OBJC_IVAR_$_ARAppClipCodeTechnique._resultDispatchingQueue
+ _OBJC_IVAR_$_ARFrame._visionDataWasDelivered
+ _OBJC_IVAR_$_ARImageData._visionDataWasDelivered
+ _OBJC_IVAR_$_ARImageSensor._sensorHasReceivedImageData
+ ___53+[ARQAHelper traceFrameData:withFrameIndex:writeOBJ:]_block_invoke.451
+ ___AppClipCodeUpdateCallbackHandler_block_invoke.34
+ ___block_literal_global.382
+ ___block_literal_global.453
+ ___block_literal_global.517
+ ___block_literal_global.519
+ ___block_literal_global.521
+ ___block_literal_global.649
+ ___block_literal_global.652
+ _objc_msgSend$_selectedVideoFormatSupportsMulticam
+ _objc_msgSend$bestVideoFormatForDevicePosition:deviceType:resolution:frameRate:videoBinned:needsHDRSupport:needsMultiCamSupport:pixelFormat:
+ _objc_msgSend$shouldProvideRGBVideoFormats
+ _objc_msgSend$visionDataWasDelivered
+ _s_shouldProvideRGBVideoFormats
- +[ARVideoFormat bestVideoFormatForDevicePosition:deviceType:resolution:frameRate:videoBinned:needsHDRSupport:pixelFormat:]
- +[ARVideoFormat bestVideoFormatForDevicePosition:deviceType:resolution:frameRate:videoBinned:needsHDRSupport:pixelFormat:].cold.1
- _AREntitlementIsPresentForCurrentProcess
- _AREntitlementIsPresentForCurrentProcess.cold.1
- ___53+[ARQAHelper traceFrameData:withFrameIndex:writeOBJ:]_block_invoke.445
- ___block_literal_global.102
- ___block_literal_global.376
- ___block_literal_global.447
- ___block_literal_global.512
- ___block_literal_global.516
- ___block_literal_global.518
- ___block_literal_global.643
- ___block_literal_global.646
- ___block_literal_global.99
- _objc_msgSend$bestVideoFormatForDevicePosition:deviceType:resolution:frameRate:videoBinned:needsHDRSupport:pixelFormat:
CStrings:
+ "%{public}@ <%p>: %@ Failed to capture a high resolution frame: %@"
+ "%{public}@ <%p>: %@ received first image data with timestamp: %f"
+ "%{public}@ <%p>: %@ received first image data with timestamp: %f, has vision data: %d"
+ "@40@0:8@16B24@28B36"
+ "@64@0:8q16@24{?=ii}32d40B48B52B56I60"
+ "Error: %{public}@ <%p>: %@ Failed to capture a high resolution frame: %@"
+ "TB,N,V_visionDataWasDelivered"
+ "TB,R,N,V_visionDataWasDelivered"
+ "_resultDispatchingQueue"
+ "_selectedVideoFormatSupportsMulticam"
+ "_sensorHasReceivedImageData"
+ "_visionDataWasDelivered"
+ "bestVideoFormatForDevicePosition:deviceType:resolution:frameRate:videoBinned:needsHDRSupport:needsMultiCamSupport:pixelFormat:"
+ "com.apple.arkit.accresults"
+ "com.apple.arkit.faceTracking.exposeAdditionalRGBFormats"
+ "initWithEndpoint:startConnection:dispatchChannelQueue:fixedPriorityQueueForXPC:"
+ "originFromWorld_Internal"
+ "setShouldProvideRGBVideoFormats:"
+ "setVisionDataWasDelivered:"
+ "shouldProvideRGBVideoFormats"
+ "visionDataWasDelivered"
- "@60@0:8q16@24{?=ii}32d40B48B52I56"
- "bestVideoFormatForDevicePosition:deviceType:resolution:frameRate:videoBinned:needsHDRSupport:pixelFormat:"
- "originFromWorld"
- "worldFromOrigin"

```
