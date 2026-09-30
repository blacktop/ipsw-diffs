## HearingModeService

> `/System/Library/PrivateFrameworks/HearingModeService.framework/HearingModeService`

```diff

-30.48.2.1.2
-  __TEXT.__text: 0x13a7c
+30.51.1.1.1
+  __TEXT.__text: 0x13e50
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x161c
+  __TEXT.__objc_methlist: 0x162c
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x44c6
+  __TEXT.__cstring: 0x4613
   __TEXT.__gcc_except_tab: 0x1bc
-  __TEXT.__unwind_info: 0x450
+  __TEXT.__unwind_info: 0x470
   __TEXT.__objc_classname: 0x130
-  __TEXT.__objc_methname: 0x5493
+  __TEXT.__objc_methname: 0x54f4
   __TEXT.__objc_methtype: 0x8bf
-  __TEXT.__objc_stubs: 0x2060
-  __DATA_CONST.__got: 0x120
+  __TEXT.__objc_stubs: 0x20e0
+  __DATA_CONST.__got: 0x128
   __DATA_CONST.__const: 0x5e8
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfc0
+  __DATA_CONST.__objc_selrefs: 0xfe8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __AUTH_CONST.__auth_got: 0x250
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x15a0
+  __AUTH_CONST.__cfstring: 0x15c0
   __AUTH_CONST.__objc_const: 0x2cf8
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x168

   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96913BBF-D4EE-3F75-A005-CA062B8329AF
-  Functions: 563
-  Symbols:   1859
-  CStrings:  1684
+  UUID: 5EBEB43B-F3FC-30AE-A398-D1FBEE7F34E3
+  Functions: 570
+  Symbols:   1878
+  CStrings:  1697
 
Symbols:
+ -[HMDeviceConfigurations updateVolumeIOS:]
+ -[HMDeviceConfigurations updateVolumeIOS:].cold.1
+ -[HMDeviceConfigurations updateVolumeIOS:].cold.2
+ -[HMDeviceConfigurations updateVolumeIOS:].cold.3
+ -[HMDeviceConfigurations updateVolumeIOS:].cold.4
+ -[HMDeviceConfigurations updateVolumeIOS:].cold.5
+ _OBJC_CLASS_$_AVSystemController
+ _objc_msgSend$getVolume:forCategory:
+ _objc_msgSend$routed
+ _objc_msgSend$setVolumeTo:forCategory:
+ _objc_msgSend$sharedAVSystemController
CStrings:
+ "### Error %@ is not routed. System volume not updated."
+ "### Error fetching current volume. System volume not updated."
+ "### Error updating system volume: %f -> %f, for currently routed %@"
+ "-[HMDeviceConfigurations updateVolumeIOS:]"
+ "Audio/Video"
+ "No need to update system volume: %f"
+ "Updated system volume: %f -> %f, for currently routed %@"
+ "getVolume:forCategory:"
+ "routed"
+ "setVolumeTo:forCategory:"
+ "sharedAVSystemController"
+ "updateVolumeIOS:"

```
