## DeviceProximityDetection

> `/System/ExclaveKit/System/Library/Frameworks/DeviceProximityDetection.framework/DeviceProximityDetection`

```diff

-524.0.7.0.0
-  __TEXT.__text: 0xf2c
-  __TEXT.__auth_stubs: 0x190
+552.0.2.0.0
+  __TEXT.__text: 0xe0c
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x98
   __TEXT.__const: 0x40
   __TEXT.__objc_methname: 0x1fe
-  __TEXT.__cstring: 0x34
+  __TEXT.__cstring: 0x37
   __TEXT.__oslogstring: 0x138
-  __TEXT.__objc_classname: 0x17
+  __TEXT.__objc_classname: 0x14
   __TEXT.__objc_methtype: 0x253
   __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0xd0
-  __DATA_CONST.__got: 0x20
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0xc8
+  __DATA_CONST.__got: 0x18
   __DATA.__objc_const: 0x1f0
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0x50

   - /System/ExclaveKit/System/Library/PrivateFrameworks/CoreVideo.framework/CoreVideo
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   - /System/ExclaveKit/usr/lib/libobjc.A.dylib
-  UUID: 14B84FEE-5163-319B-94F8-55A9C5E332CA
+  UUID: D7B3C66D-9716-327A-B9AC-0462DF4503EC
   Functions: 33
-  Symbols:   98
+  Symbols:   96
   CStrings:  68
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_release
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ -[ODT3DSessionWrapper initWithEXsurfaceMemoryRegion:andANE:] : 464 -> 420
~ _resetDeviceProximityDetectionOutput : 120 -> 124
~ -[ODT3DSessionWrapper setDeviceModels:] : 192 -> 148
~ -[ODT3DSessionWrapper setTimestamp:] : 172 -> 128
~ -[ODT3DSessionWrapper setImage:] : 248 -> 204
~ -[ODT3DSessionWrapper setCameraIntrinsicMatrix:] : 308 -> 264
~ -[ODT3DSessionWrapper setEXSurface:] : 52 -> 12
~ _DeviceProximityDetectionPipelineSetDeviceModels : 196 -> 188
~ _DeviceProximityDetectionPipelineSetDeviceFamilies : 196 -> 188
~ _DeviceProximityDetectionOutputGetDeviceIdentifier : 60 -> 64
~ _DeviceProximityDetectionOutputGetConfidenceBin : 152 -> 136
~ _DeviceProximityDetectionOutputCreateDebugParameters : 268 -> 264

```
