## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-6.21.0.0.0
-  __TEXT.__text: 0x1d6c70
+6.103.0.0.0
+  __TEXT.__text: 0x1d6d88
   __TEXT.__objc_methlist: 0x270
   __TEXT.__gcc_except_tab: 0x6448
-  __TEXT.__const: 0x2f298
+  __TEXT.__const: 0x2f2a2
   __TEXT.__cstring: 0x19c87
   __TEXT.__oslogstring: 0x1e771
-  __TEXT.__unwind_info: 0x66b0
+  __TEXT.__unwind_info: 0x66b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc148
+  __DATA_CONST.__const: 0xc158
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x18f0
-  __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x38
   __DATA.__data: 0x382670
-  __DATA.__common: 0x30
-  __DATA_DIRTY.__objc_data: 0x50
+  __DATA.__common: 0x2c
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x220
   __DATA_DIRTY.__bss: 0x9a8
+  __DATA_DIRTY.__common: 0x4
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6000
-  Symbols:   8558
+  Functions: 6001
+  Symbols:   8561
   CStrings:  6470
 
Symbols:
+ __ZN6H16ISP12H16ISPDevice35InvokeDeviceMessageNotificationProcEjPv
+ __ZN6H16ISP12SystemStatus26CopyBuiltInCameraDeviceUIDEv
+ __oidAppleExtendedKeyUsageSWUpdateSigning
+ _oidAppleExtendedKeyUsageSWUpdateSigning
- __ZN6H16ISP12SystemStatus17CopyCMIODeviceUIDEv
Functions:
~ __ZN6H16ISPL35H16ISPDeviceServiceInterestCallbackEPvjjS0_ : 32 -> 12
~ __ZN6H16ISP12H16ISPDevice37RegisterDeviceMessageNotificationProcEPFiPS0_jPvS2_ES2_ : 8 -> 76
~ __ZN6H16ISP19H16ISPFrameReceiverC2EPNS_12H16ISPDeviceEjP21H16ISPTNRConfigStruct29H16ISPRationalFrameRateStructS5_ : 1512 -> 1516
~ __ZL32H16ISPCaptureStreamStartInternalP22OpaqueFigCaptureStream : 28092 -> 28100
~ __ZN6H16ISP12H16ISPDeviceC2EPNS_22H16ISPDeviceControllerEj : 1284 -> 1304
~ __ZN6H16ISP12H16ISPDevice16H16ISPDeviceOpenEPFiPS0_jPvS2_ES2_ : 332 -> 356
~ __ZN6H16ISP12H16ISPDevice17H16ISPDeviceCloseEv : 128 -> 160
~ __ZN6H16ISP19H16ISPFrameReceiver29removeIODispatcherFromRunLoopEv : 220 -> 216
+ __ZN6H16ISP12H16ISPDevice35InvokeDeviceMessageNotificationProcEjPv
```
