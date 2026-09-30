## AXSoundDetection

> `/System/Library/PrivateFrameworks/AXSoundDetection.framework/AXSoundDetection`

```diff

-496.13.0.0.0
-  __TEXT.__text: 0x4100
-  __TEXT.__auth_stubs: 0x280
+496.15.0.0.0
+  __TEXT.__text: 0x42e4
+  __TEXT.__auth_stubs: 0x2b0
   __TEXT.__objc_methlist: 0x380
-  __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xdc2
-  __TEXT.__oslogstring: 0x29b
+  __TEXT.__const: 0x78
+  __TEXT.__cstring: 0xe50
+  __TEXT.__oslogstring: 0x2e1
   __TEXT.__unwind_info: 0x1b8
   __TEXT.__objc_classname: 0x22
   __TEXT.__objc_methname: 0xe3a

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x490
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x148
+  __AUTH_CONST.__auth_got: 0x160
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x14e0
+  __AUTH_CONST.__cfstring: 0x1560
   __AUTH_CONST.__objc_const: 0x398
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x18

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libAccessibility.dylib
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F6880BB0-7CB8-3F59-B92A-455096395BCF
-  Functions: 111
-  Symbols:   517
-  CStrings:  538
+  UUID: 99C2F1DD-F973-3007-A68E-A2F1A9EC318B
+  Functions: 112
+  Symbols:   521
+  CStrings:  553
 
Symbols:
+ _AXSoundDetectionSupportsVirtualAudioDevice
+ _MGGetBoolAnswer
+ _MGGetSInt32Answer
+ __os_feature_enabled_impl
Functions:
+ _AXSoundDetectionSupportsVirtualAudioDevice
CStrings:
+ "Device supports VAD: NO"
+ "DeviceClassNumber"
+ "DeviceSupportsIndependentOutputOnSpeaker"
+ "DeviceSupportsUSBTypeC"
+ "NO"
+ "VirtualAudio"
+ "YES"
+ "YiUtBQygkHRhLcdO3LFB4A"
+ "additive_routing"
+ "iPad supports VAD: %s"
+ "iPhone supports VAD: %s"

```
