## relatived

> `/usr/libexec/relatived`

```diff

-300.0.2.0.0
-  __TEXT.__text: 0x14cec
-  __TEXT.__auth_stubs: 0x950
-  __TEXT.__objc_stubs: 0x3040
-  __TEXT.__objc_methlist: 0x1140
-  __TEXT.__const: 0x1d8
-  __TEXT.__gcc_except_tab: 0x6cc
-  __TEXT.__objc_methname: 0x3981
-  __TEXT.__cstring: 0x1005
-  __TEXT.__oslogstring: 0x2355
-  __TEXT.__objc_classname: 0x410
-  __TEXT.__objc_methtype: 0x9ed
-  __TEXT.__unwind_info: 0x5f8
-  __DATA_CONST.__auth_got: 0x4b8
+305.0.15.0.0
+  __TEXT.__text: 0x14470
+  __TEXT.__auth_stubs: 0x910
+  __TEXT.__objc_stubs: 0x3020
+  __TEXT.__objc_methlist: 0x1108
+  __TEXT.__const: 0x178
+  __TEXT.__gcc_except_tab: 0x680
+  __TEXT.__objc_methname: 0x3931
+  __TEXT.__cstring: 0xf87
+  __TEXT.__oslogstring: 0x22ca
+  __TEXT.__objc_classname: 0x3fb
+  __TEXT.__objc_methtype: 0x9ce
+  __TEXT.__unwind_info: 0x5d8
+  __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x328
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xb80
-  __DATA_CONST.__cfstring: 0xa00
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__const: 0xb60
+  __DATA_CONST.__cfstring: 0x980
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_doubleobj: 0x60
   __DATA_CONST.__objc_intobj: 0x48
   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x2af8
-  __DATA.__objc_selrefs: 0xd70
-  __DATA.__objc_ivar: 0x228
-  __DATA.__objc_data: 0x7d0
+  __DATA.__objc_const: 0x29b8
+  __DATA.__objc_selrefs: 0xd58
+  __DATA.__objc_ivar: 0x218
+  __DATA.__objc_data: 0x780
   __DATA.__data: 0x460
-  __DATA.__bss: 0xc0
+  __DATA.__bss: 0xb0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A50913FF-10C4-3375-8B9B-032D9576C969
-  Functions: 562
-  Symbols:   263
-  CStrings:  1158
+  UUID: 4F9BA658-BE4B-3CC8-A6F2-8EFC558070C1
+  Functions: 550
+  Symbols:   259
+  CStrings:  1138
 
Symbols:
+ _OBJC_CLASS_$_NSURL
- _CFStringCreateWithCString
- _CFURLCreateWithFileSystemPath
- _MGIsDeviceOneOfType
- __os_feature_enabled_impl
- _kCMMediaSessionPredictionIntervalMicroseconds
CStrings:
+ "%@ ID %@ model %@ type %ld-%ld transport %@"
+ "@\"CMPose\""
+ "T@\"NSString\",C,N,V_activeAudioRouteAlternateTransportType"
+ "URLWithString:"
+ "[RMAudioAccessoryManager] No active route change, same device %{public}@ is still active"
+ "[RMAudioAccessoryManager] relatived failed to select active audio route for device %{public}@"
+ "[RMAudioAccessoryManager] relatived reset active audio route because no supported device was found"
+ "[RMAudioAccessoryManager] relatived sucessfully selected active audio route for device %{public}@"
+ "_activeAudioRouteAlternateTransportType"
+ "_error"
+ "_orientation"
+ "activeAudioRouteAlternateTransportType"
+ "alternateTransportType"
+ "deviceSubType"
+ "setActiveAudioRouteAlternateTransportType:"
- "@24@0:8r^{?=d}16"
- "CMHeadphoneMotionManagerEnable50HzUpdateInterval"
- "CoreLocation"
- "OpportunisticAnchoredTracking"
- "RMAudioListenerPoseCaptureQueue"
- "RMMediaSessionStatus"
- "Speaker"
- "Starting timer to emulate media session status callback"
- "State: %.0f"
- "T@\"NSUserDefaults\",&,N,V_cmDefaults"
- "TB,N,V_requested50HzHeadphoneMotion"
- "Time"
- "[RMAudioAccessoryManager] Headphone Motion API set to 50Hz for user study."
- "[RMAudioAccessoryManager] current device motion samples per second: %{public}lu. Headphone Motion API set to 50Hz for user study."
- "[RMAudioAccessoryManager] relatived failed to select active audio route for device %{public}@ ID %{private}@ model %{private}@"
- "[RMAudioAccessoryManager] relatived sucessfully selected active audio route for device %{public}@ ID %{private}@ model %{private}@"
- "_cmDefaults"
- "_internal"
- "_predictionIntervalMicroseconds"
- "_requested50HzHeadphoneMotion"
- "_statusTimer"
- "cmDefaults"
- "com.apple.CoreMotion"
- "doubleValue"
- "initWithInternal:"
- "numberWithUnsignedLongLong:"
- "requested50HzHeadphoneMotion"
- "setCmDefaults:"
- "setRequested50HzHeadphoneMotion:"
- "shortDescription"
- "{?=\"machAbsTimestamp\"d}"

```
