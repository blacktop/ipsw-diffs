## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

 2145.62.1.2.0
-  __TEXT.__text: 0x792504
-  __TEXT.__auth_stubs: 0x5600
-  __TEXT.__objc_methlist: 0x35980
+  __TEXT.__text: 0x793058
+  __TEXT.__auth_stubs: 0x5610
+  __TEXT.__objc_methlist: 0x359a8
   __TEXT.__const: 0xc760
-  __TEXT.__cstring: 0x8ef02
-  __TEXT.__oslogstring: 0x10e5c4
+  __TEXT.__cstring: 0x8f09e
+  __TEXT.__oslogstring: 0x10e79c
   __TEXT.__gcc_except_tab: 0x2a80
   __TEXT.__ustring: 0x2d4
-  __TEXT.__unwind_info: 0x10820
+  __TEXT.__unwind_info: 0x10838
   __TEXT.__objc_classname: 0x4eb2
-  __TEXT.__objc_methname: 0x7d75e
-  __TEXT.__objc_methtype: 0x28277
-  __TEXT.__objc_stubs: 0x4e9c0
-  __DATA_CONST.__got: 0x1a30
-  __DATA_CONST.__const: 0x6a30
+  __TEXT.__objc_methname: 0x7d880
+  __TEXT.__objc_methtype: 0x28278
+  __TEXT.__objc_stubs: 0x4ea40
+  __DATA_CONST.__got: 0x1a58
+  __DATA_CONST.__const: 0x6a50
   __DATA_CONST.__objc_classlist: 0x12e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x168d0
+  __DATA_CONST.__objc_selrefs: 0x16900
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
-  __AUTH_CONST.__auth_got: 0x2b18
-  __AUTH_CONST.__const: 0x3bc8
-  __AUTH_CONST.__cfstring: 0x261c0
-  __AUTH_CONST.__objc_const: 0x63390
+  __AUTH_CONST.__auth_got: 0x2b20
+  __AUTH_CONST.__const: 0x3c08
+  __AUTH_CONST.__cfstring: 0x26240
+  __AUTH_CONST.__objc_const: 0x633c0
   __AUTH_CONST.__objc_intobj: 0x4968
   __AUTH_CONST.__objc_arrayobj: 0x1b30
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0x6c38
-  __DATA.__data: 0x7870
-  __DATA.__bss: 0xd20
+  __DATA.__objc_ivar: 0x6c3c
+  __DATA.__data: 0x78b0
+  __DATA.__bss: 0xd30
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0xa780
   __DATA_DIRTY.__data: 0x160

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9DD0B6DB-41F7-351C-A59C-95855C864369
-  Functions: 31529
-  Symbols:   97233
-  CStrings:  57117
+  UUID: BF52978D-0DD4-31FD-B6C2-2500A929ECEA
+  Functions: 31539
+  Symbols:   97272
+  CStrings:  57145
 
Symbols:
+ -[VCAVFoundationCapture updateVideoCaptureAspectRatioWithRequestResolution:requestHeight:captureFormat:]
+ -[VCVirtualAVCaptureDeviceFormat setSupportedOutputAspectRatios:]
+ -[VCVirtualAVCaptureDeviceFormat supportedOutputAspectRatios]
+ _AVCaptureAspectRatio16x9
+ _AVCaptureAspectRatio1x1
+ _AVCaptureAspectRatio3x4
+ _AVCaptureAspectRatio4x3
+ _AVCaptureAspectRatio9x16
+ _OBJC_IVAR_$_VCVirtualAVCaptureDeviceFormat._supportedOutputAspectRatios
+ _VCFeatureFlagManager_EnableMTERetagging
+ _VCFeatureFlagManager_EnableMTERetagging.cold.1
+ _VCFeatureFlagManager_EnableMTERetagging.flag
+ _VCFeatureFlagManager_EnableMTERetagging.onceToken
+ _VCVirtualHardwareCode_D23
+ ___104-[VCAVFoundationCapture updateVideoCaptureAspectRatioWithRequestResolution:requestHeight:captureFormat:]_block_invoke
+ ___104-[VCAVFoundationCapture updateVideoCaptureAspectRatioWithRequestResolution:requestHeight:captureFormat:]_block_invoke.cold.1
+ ___VCFeatureFlagManager_EnableMTERetagging_block_invoke
+ ___block_descriptor_32_e27_v40?0{?=qiIq}8"NSError"32l
+ ___block_literal_global.199
+ ___builtin_available.mte_enabled.ifunc
+ ___builtin_available.no
+ ___builtin_available.yes
+ _kVCVirtualDeviceFormatSupportsAspectRatio
+ _objc_msgSend$outputAspectRatio
+ _objc_msgSend$outputDimensions
+ _objc_msgSend$setOutputAspectRatio:completionHandler:
+ _objc_msgSend$setSupportedOutputAspectRatios:
+ _objc_msgSend$supportedOutputAspectRatios
+ _objc_msgSend$updateVideoCaptureAspectRatioWithRequestResolution:requestHeight:captureFormat:
- _objc_msgSend$setupLocalABTestSwitches
- _objc_msgSend$setupLocalOnOffSwitches
CStrings:
+ " [%s] %s:%d Failed to lock device error=%@"
+ " [%s] %s:%d No AVCaptureAspectRatio matches request width=%d height=%d"
+ " [%s] %s:%d SwitchManager: Non-seed build - using master local switch: %08X"
+ " [%s] %s:%d [AR_TX] _deviceOrientationMatchesReceiver=%d, _remotePreferFullBleed=%d, captureAspectRatio=%@, overrideByDefault=%d"
+ " [%s] %s:%d capture request format supports max FOV with AR w=%.0f,h=%.0f"
+ " [%s] %s:%d keyExist, _deviceOrientationMatchesReceiver=%d"
+ " [%s] %s:%d setOutputAspectRatio error=%@"
+ "-[VCAVFoundationCapture updateCaptureSizeWithAspectRatio:width:height:]"
+ "-[VCAVFoundationCapture updateVideoCaptureAspectRatioWithRequestResolution:requestHeight:captureFormat:]"
+ "-[VCAVFoundationCapture updateVideoCaptureAspectRatioWithRequestResolution:requestHeight:captureFormat:]_block_invoke"
+ "AVCaptureCameraMatchesOrientation"
+ "D23"
+ "EnableMTERetagging"
+ "T@\"NSArray\",&,N,V_supportedOutputAspectRatios"
+ "VCFeatureFlagManager: EnableMTERetagging=%d (feature flag=%d)"
+ "^{tagVCMemoryPool={?=^vq}QQQB}"
+ "_supportedOutputAspectRatios"
+ "aspect_ratio"
+ "enableMTERetagging"
+ "outputAspectRatio"
+ "outputDimensions"
+ "setOutputAspectRatio:completionHandler:"
+ "setSupportedOutputAspectRatios:"
+ "supportedOutputAspectRatios"
+ "updateVideoCaptureAspectRatioWithRequestResolution:requestHeight:captureFormat:"
+ "v40@?0{?=qiIq}8@\"NSError\"32"
- " [%s] %s:%d SwitchManager: A/B testing turned off - using master local switch: %08X"
- "^{tagVCMemoryPool={?=^vq}QQQ}"

```
