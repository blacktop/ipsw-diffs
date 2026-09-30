## DeviceProximityDetection

> `/System/ExclaveKit/System/Library/Frameworks/DeviceProximityDetection.framework/DeviceProximityDetection`

```diff

-507.0.5.0.0
-  __TEXT.__text: 0xed8
+524.0.6.0.0
+  __TEXT.__text: 0xf2c
   __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x98

   __DATA.__objc_const: 0x1f0
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x50
+  - /System/ExclaveKit/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/ExclaveKit/System/Library/Frameworks/Foundation.framework/Foundation
   - /System/ExclaveKit/System/Library/PrivateFrameworks/CoreVideo.framework/CoreVideo
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
-  UUID: FE038C26-2272-381D-8AD9-2A96CF2171DD
+  UUID: 4A9CACD9-B4C4-3AB1-95F8-10217D564DDC
   Functions: 33
   Symbols:   98
   CStrings:  68
Symbols:
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ -[ODT3DSessionWrapper setEXSurface:] : 12 -> 52
~ -[ODT3DSessionWrapper .cxx_destruct] : 68 -> 56
~ _DeviceProximityDetectionPipelineRelease : 72 -> 60
~ _DeviceProximityDetectionPipelineSetDeviceModels : 188 -> 196
~ _DeviceProximityDetectionPipelineSetDeviceFamilies : 188 -> 196
~ _DeviceProximityDetectionOutputGetDeviceModel : 60 -> 64
~ _DeviceProximityDetectionOutputGetPoseMatrix : 68 -> 72
~ _DeviceProximityDetectionOutputGetConfidence : 60 -> 76
~ _DeviceProximityDetectionOutputGetConfidenceBin : 136 -> 152
~ _DeviceProximityDetectionOutputCreateDebugParameters : 256 -> 268

```
