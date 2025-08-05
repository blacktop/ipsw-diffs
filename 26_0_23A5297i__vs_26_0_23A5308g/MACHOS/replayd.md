## replayd

> `/usr/libexec/replayd`

```diff

-650.49.1.0.0
-  __TEXT.__text: 0x61e48
-  __TEXT.__auth_stubs: 0x1090
-  __TEXT.__objc_stubs: 0x87a0
-  __TEXT.__objc_methlist: 0x445c
+650.53.2.0.0
+  __TEXT.__text: 0x61a5c
+  __TEXT.__auth_stubs: 0x10a0
+  __TEXT.__objc_stubs: 0x8780
+  __TEXT.__objc_methlist: 0x447c
   __TEXT.__const: 0x1b4
-  __TEXT.__objc_methname: 0xca5c
-  __TEXT.__cstring: 0xc91b
-  __TEXT.__oslogstring: 0x9688
+  __TEXT.__objc_methname: 0xca99
+  __TEXT.__cstring: 0xc9a5
+  __TEXT.__oslogstring: 0x95d0
   __TEXT.__objc_classname: 0x69b
-  __TEXT.__objc_methtype: 0x22bb
+  __TEXT.__objc_methtype: 0x22c1
   __TEXT.__gcc_except_tab: 0x7c8
   __TEXT.__unwind_info: 0x12e8
-  __DATA_CONST.__auth_got: 0x858
-  __DATA_CONST.__got: 0x750
+  __DATA_CONST.__auth_got: 0x860
+  __DATA_CONST.__got: 0x770
   __DATA_CONST.__const: 0x1928
-  __DATA_CONST.__cfstring: 0x3a20
+  __DATA_CONST.__cfstring: 0x3aa0
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x108
-  __DATA_CONST.__objc_intobj: 0x318
-  __DATA_CONST.__objc_doubleobj: 0x30
-  __DATA.__objc_const: 0x9630
-  __DATA.__objc_selrefs: 0x2ac8
-  __DATA.__objc_ivar: 0x5b8
+  __DATA_CONST.__objc_intobj: 0x360
+  __DATA_CONST.__objc_doubleobj: 0x40
+  __DATA.__objc_const: 0x9650
+  __DATA.__objc_selrefs: 0x2ad8
+  __DATA.__objc_ivar: 0x5bc
   __DATA.__objc_data: 0xe60
   __DATA.__data: 0xa98
   __DATA.__bss: 0x1d0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 74AEBE2D-DC1C-3474-B7A3-506A810A31A5
-  Functions: 1980
-  Symbols:   512
-  CStrings:  4528
+  UUID: 0168B45B-17E7-3BA5-9E49-5E4F079CA5D0
+  Functions: 1979
+  Symbols:   517
+  CStrings:  4538
 
Symbols:
+ _CFPreferencesGetAppIntegerValue
+ _kVTCompressionPropertyKey_ConstantQualityFactor
+ _kVTCompressionPropertyKey_SpatialAdaptiveQPLevel
+ _kVTCompressionPropertyKey_SuggestedLookAheadFrameCount
+ _kVTCompressionPropertyKey_VBVMaxBitRate
CStrings:
+ " [INFO] %{public}s:%d audio only - skipping camera capture for delegate %@"
+ " [INFO] %{public}s:%d delegate=%@, micDeviceID=%@, cameraDeviceID=%@, audioOnly=%d"
+ " [INFO] %{public}s:%d use default write CQF=%lf"
+ " [INFO] %{public}s:%d use default write VBVMaxBitRate=%ld"
+ "-[RPCaptureManager startHQLRCaptureForDelegate:micDeviceID:cameraDeviceID:windowSize:audioOnly:didStartHandler:]"
+ "-[RPCaptureManager startHQLRCaptureForDelegate:micDeviceID:cameraDeviceID:windowSize:audioOnly:didStartHandler:]_block_invoke"
+ "-[RPHighQualityLocalRecordingSession handleDeviceLockedWarning]"
+ "-[RPHighQualityLocalRecordingSession handleDeviceLockedWarning]_block_invoke"
+ "-[RPHighQualityLocalRecordingSession startHQLRRecordingWithMicrophoneID:cameraDeviceID:destination:fileURL:sandboxExtensionTokenForFileURL:audioOnly:windowSize:handler:]"
+ "-[RPHighQualityLocalRecordingSession startHQLRRecordingWithMicrophoneID:cameraDeviceID:destination:fileURL:sandboxExtensionTokenForFileURL:audioOnly:windowSize:handler:]_block_invoke"
+ "SCKCQFOverride"
+ "SCKVBVMaxBitRateOverride"
+ "_audioOnly"
+ "audioOnly"
+ "callservicesd"
+ "csdProcessId"
+ "numberWithFloat:"
+ "startHQLRCaptureForDelegate:micDeviceID:cameraDeviceID:windowSize:audioOnly:didStartHandler:"
+ "startHQLRRecordingWithMicrophoneID:cameraDeviceID:destination:fileURL:sandboxExtensionTokenForFileURL:audioOnly:windowSize:handler:"
+ "v68@0:8@16@24@32{CGSize=dd}40B56@?60"
+ "v84@0:8@16@24Q32@40@48B56{CGSize=dd}60@?76"
- " [INFO] %{public}s:%d Crossed disk threshold: Disk space can support saving current recording"
- " [INFO] %{public}s:%d Crossed disk threshold: Disk space cannot support saving current recording"
- " [INFO] %{public}s:%d Disk space can still support current recording"
- " [INFO] %{public}s:%d Disk space cannot support current continued recording, Stopping and discarding current recording"
- " [INFO] %{public}s:%d delegate=%@, micDeviceID=%@, cameraDeviceID=%@"
- "-[RPCaptureManager startHQLRCaptureForDelegate:micDeviceID:cameraDeviceID:windowSize:didStartHandler:]"
- "-[RPCaptureManager startHQLRCaptureForDelegate:micDeviceID:cameraDeviceID:windowSize:didStartHandler:]_block_invoke"
- "-[RPHighQualityLocalRecordingSession handleTimerDidUpdate:]"
- "-[RPHighQualityLocalRecordingSession startHQLRRecordingWithMicrophoneID:cameraDeviceID:destination:fileURL:sandboxExtensionTokenForFileURL:windowSize:handler:]"
- "-[RPHighQualityLocalRecordingSession startHQLRRecordingWithMicrophoneID:cameraDeviceID:destination:fileURL:sandboxExtensionTokenForFileURL:windowSize:handler:]_block_invoke"
- "-[RPSystemRecordSession handleTimerDidUpdate:]"
- "startHQLRCaptureForDelegate:micDeviceID:cameraDeviceID:windowSize:didStartHandler:"
- "startHQLRRecordingWithMicrophoneID:cameraDeviceID:destination:fileURL:sandboxExtensionTokenForFileURL:windowSize:handler:"
- "v64@0:8@16@24@32{CGSize=dd}40@?56"
- "v80@0:8@16@24Q32@40@48{CGSize=dd}56@?72"

```
