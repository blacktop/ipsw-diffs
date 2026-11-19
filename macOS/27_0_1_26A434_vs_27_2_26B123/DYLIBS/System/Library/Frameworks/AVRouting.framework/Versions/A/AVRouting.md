## AVRouting

> `/System/Library/Frameworks/AVRouting.framework/Versions/A/AVRouting`

```diff

-360.75.1.0.0
-  __TEXT.__text: 0x46cdc
-  __TEXT.__objc_methlist: 0x62b0
+385.10.5.1.0
+  __TEXT.__text: 0x46f20
+  __TEXT.__objc_methlist: 0x62f0
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x99d2
+  __TEXT.__cstring: 0x9ac0
   __TEXT.__oslogstring: 0x5e76
   __TEXT.__gcc_except_tab: 0x4f0
   __TEXT.__unwind_info: 0x1580

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7b0
+  __DATA_CONST.__const: 0x7c8
   __DATA_CONST.__objc_classlist: 0x370
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1dd8
+  __DATA_CONST.__objc_selrefs: 0x1e00
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__got: 0xfd8
   __AUTH_CONST.__const: 0xdf0
-  __AUTH_CONST.__cfstring: 0x43c0
-  __AUTH_CONST.__objc_const: 0xb718
+  __AUTH_CONST.__cfstring: 0x44a0
+  __AUTH_CONST.__objc_const: 0xb790
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x1220
-  __DATA.__objc_ivar: 0x538
+  __DATA.__objc_ivar: 0x540
   __DATA.__data: 0xb70
-  __DATA.__bss: 0x88
+  __DATA.__bss: 0xa0
   __DATA.__common: 0x80
-  __DATA_DIRTY.__objc_data: 0x1040
+  __DATA_DIRTY.__objc_data: 0x2260
   __DATA_DIRTY.__common: 0x140
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/Versions/A/CoreMedia

   - /System/Library/PrivateFrameworks/MediaExperience.framework/Versions/A/MediaExperience
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2389
-  Symbols:   5186
-  CStrings:  1082
+  Functions: 2394
+  Symbols:   5198
+  CStrings:  1089
 
Symbols:
+ -[AVClusterComponentOutputDeviceDescription initWithDeviceID:deviceName:deviceSubType:isClusterLeader:modelID:surroundRole:]
+ -[AVClusterComponentOutputDeviceDescription surroundRole]
+ -[AVOutputContextPredictedDevicesOptions pebbleInitiatedAppBundleID]
+ -[AVOutputContextPredictedDevicesOptions setPebbleInitiatedAppBundleID:]
+ OBJC_IVAR_$_AVClusterComponentOutputDeviceDescription._surroundRole
+ OBJC_IVAR_$_AVOutputContextPredictedDevicesOptions._pebbleInitiatedAppBundleID
+ _AVOutputDeviceCarPlayScreenBeginFadeInNotification
+ _AVOutputDeviceCarPlayScreenBeginFadeOutNotification
+ _AVOutputDeviceCarPlayScreenFadeDurationKey
+ _AVOutputDevicePostCarPlayScreenFadeNotification
+ _objc_msgSend$initWithDeviceID:deviceName:deviceSubType:isClusterLeader:modelID:surroundRole:
+ _objc_msgSend$unsignedLongLongValue
CStrings:
+ "AVOutputDeviceCarPlayScreenBeginFadeInNotification"
+ "AVOutputDeviceCarPlayScreenBeginFadeOutNotification"
+ "AVOutputDeviceCarPlayScreenFadeDurationKey"
+ "CarPlayScreenFadeDurationInSeconds"
+ "EndpointSubType_HomeAccessory"
+ "HomeAccessory"
+ "SurroundRole"
```
