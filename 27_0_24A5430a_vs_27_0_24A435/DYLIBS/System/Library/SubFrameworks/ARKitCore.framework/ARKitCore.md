## ARKitCore

> `/System/Library/SubFrameworks/ARKitCore.framework/ARKitCore`

```diff

 781.0.7.0.0
-  __TEXT.__text: 0x19a784
-  __TEXT.__objc_methlist: 0x1140c
-  __TEXT.__const: 0x25d68
-  __TEXT.__cstring: 0x1d98c
-  __TEXT.__gcc_except_tab: 0x13480
-  __TEXT.__oslogstring: 0x20d74
+  __TEXT.__text: 0x19ad54
+  __TEXT.__objc_methlist: 0x1143c
+  __TEXT.__const: 0x25d78
+  __TEXT.__cstring: 0x1d99a
+  __TEXT.__gcc_except_tab: 0x13490
+  __TEXT.__oslogstring: 0x20dc6
   __TEXT.__ustring: 0xe6
   __TEXT.__unwind_info: 0x6ad0
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x7ec0
+  __DATA_CONST.__objc_selrefs: 0x7ed8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x7a8
   __DATA_CONST.__objc_arraydata: 0x870
-  __DATA_CONST.__got: 0x15e8
-  __AUTH_CONST.__const: 0x3dd8
-  __AUTH_CONST.__cfstring: 0xff20
-  __AUTH_CONST.__objc_const: 0x3d080
+  __DATA_CONST.__got: 0x15f8
+  __AUTH_CONST.__const: 0x3e18
+  __AUTH_CONST.__cfstring: 0xff40
+  __AUTH_CONST.__objc_const: 0x3d0e0
   __AUTH_CONST.__weak_auth_got: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x390
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x38b8
-  __AUTH_CONST.__auth_got: 0x1f08
+  __AUTH_CONST.__auth_got: 0x1f10
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x2030
+  __DATA.__objc_ivar: 0x2038
   __DATA.__data: 0x1c90
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8

   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  Functions: 8008
-  Symbols:   18032
-  CStrings:  4551
+  Functions: 8024
+  Symbols:   18060
+  CStrings:  4554
 
Symbols:
+ -[ARCamera displayRegion]
+ -[ARCamera initWithIntrinsics:imageResolution:devicePosition:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:displayRegion:]
+ -[ARCamera setDisplayRegion:]
+ -[ARImageData displayRegion]
+ -[ARImageData setDisplayRegion:]
+ _ARDeviceIsV68
+ _ARDeviceIsV68.onceToken
+ _ARDisplayCenterTransformForRegion
+ _ARDisplayCenterTransformForRegion.frontTransforms
+ _ARDisplayCenterTransformForRegion.onceToken
+ _ARDisplayCenterTransformForRegion.rearTransforms
+ _ARDisplayRegionFromAVCaptureDisplayRegion
+ _ARFrontCameraDisplayCenterTransformForDisplayIndex
+ _ARFrontWideCameraTransformFromBackWideAngleCameraTransformForRegion
+ _ARFrontWideCameraTransformFromBackWideAngleCameraTransformWithZFlipForRegion
+ _ARGetFrontCameraOffset
+ _ARGetRearCameraOffset
+ _ARMobileGestaltArrayForKeyAndDisplayIndex
+ _AROverrideARDeviceIsV68
+ _ARRearCameraDisplayCenterTransformForDisplayIndex
+ _ARResetARDeviceIsV68
+ _MGCopyAnswerForDisplayAtIndex
+ _OBJC_IVAR_$_ARCamera._displayRegion
+ _OBJC_IVAR_$_ARImageData._displayRegion
+ ___ARDeviceIsV68_block_invoke
+ ___ARDisplayCenterTransformForRegion_block_invoke
+ _kMGDisplayIndexedQueryFrontCameraOffsetFromDisplayCenter
+ _kMGDisplayIndexedQueryRearCameraOffsetFromDisplayCenter
+ _objc_msgSend$displayRegion
+ _objc_msgSend$initWithIntrinsics:imageResolution:devicePosition:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:displayRegion:
+ _objc_msgSend$primaryDisplayRegion
+ _objc_msgSend$setDisplayRegion:
+ _s_deviceIsV68
- -[ARCamera initWithIntrinsics:imageResolution:devicePosition:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:]
- _ARDisplayCenterTransformForCaptureDevicePosition
- _ARFrontWideCameraTransformFromBackWideAngleCameraTransform
- _ARFrontWideCameraTransformFromBackWideAngleCameraTransformWithZFlip
- _objc_msgSend$initWithIntrinsics:imageResolution:devicePosition:radialDistortion:tangentialDistortion:exposureDuration:calibrationData:extrinsicsMap:captureLens:
CStrings:
+ "A!"
+ "MobileGestalt display-indexed query failed (error %d, display %ld) for device: %@"
+ "displayRegion"
```
