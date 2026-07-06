## ISP.mediacapture

> `/System/Library/MediaCapture/ISP.mediacapture`

```diff

-  __TEXT.__text: 0x1a3874
+  __TEXT.__text: 0x1a3d80
   __TEXT.__init_offsets: 0xc
-  __TEXT.__gcc_except_tab: 0x49a8
-  __TEXT.__const: 0x27805
-  __TEXT.__oslogstring: 0x1b406
-  __TEXT.__cstring: 0x15c58
-  __TEXT.__unwind_info: 0x30d0
+  __TEXT.__gcc_except_tab: 0x49ac
+  __TEXT.__const: 0x27725
+  __TEXT.__oslogstring: 0x1b408
+  __TEXT.__cstring: 0x15c5d
+  __TEXT.__unwind_info: 0x30d8
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x8f88
+  __DATA_CONST.__const: 0x8fa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x28
   __DATA_CONST.__objc_selrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x1ed0
-  __AUTH_CONST.__cfstring: 0x7840
+  __AUTH_CONST.__const: 0x1ef0
+  __AUTH_CONST.__cfstring: 0x7800
   __AUTH_CONST.__weak_auth_got: 0xb0
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1330
+  __AUTH_CONST.__auth_got: 0x1320
   __DATA.__data: 0x3b1df0
-  __DATA.__bss: 0xa98
-  __DATA.__common: 0x53c8
+  __DATA.__bss: 0xaa8
+  __DATA.__common: 0x53f8
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 5011
-  Symbols:   8875
-  CStrings:  6645
+  Functions: 5018
+  Symbols:   8889
+  CStrings:  6644
 
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table389
+ GCC_except_table426
+ GCC_except_table436
+ GCC_except_table445
+ GCC_except_table452
+ GCC_except_table505
+ GCC_except_table507
+ GCC_except_table523
+ GCC_except_table527
+ GCC_except_table544
+ GCC_except_table547
+ GCC_except_table554
+ GCC_except_table557
+ GCC_except_table564
+ GCC_except_table592
+ GCC_except_table594
+ GCC_except_table617
+ GCC_except_table696
+ GCC_except_table697
+ GCC_except_table702
+ GCC_except_table710
+ GCC_except_table711
+ GCC_except_table713
+ GCC_except_table720
+ GCC_except_table726
+ GCC_except_table731
+ GCC_except_table754
+ GCC_except_table775
+ GCC_except_table776
+ GCC_except_table786
+ GCC_except_table790
+ GCC_except_table792
+ GCC_except_table794
+ GCC_except_table809
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _ZL18StopExclaveChannelP16ISPCaptureDeviceP16ISPCaptureStream
+ _ZL19ISPPostNotificationPK10__CFStringPKvS3_
+ _ZL22PowerOffExclaveChannelP16ISPCaptureDeviceP16ISPCaptureStream
+ _ZL35ConfigureFrameworkAlgorithmSettingsP16ISPCaptureDeviceP16ISPCaptureStream
+ __ZL18StopExclaveChannelP16ISPCaptureDeviceP16ISPCaptureStream
+ __ZL22PowerOffExclaveChannelP16ISPCaptureDeviceP16ISPCaptureStream
+ __ZL24SetApertureHealthEnabledPKvP16ISPCaptureStreamP15ISPCaptureGroupP16ISPCaptureDevice
+ __ZL35ConfigureFrameworkAlgorithmSettingsP16ISPCaptureDeviceP16ISPCaptureStream
+ __ZN3ISPL19deepCopyDictApplierEPKvS1_Pv
+ __ZN3ISPL22createDeepCopyTolerantEPKv
+ __ZZL23ISPGetNotificationQueuevE5queue
+ __ZZL23ISPGetNotificationQueuevE9onceToken
+ ____ZL23ISPGetNotificationQueuev_block_invoke
+ _kFigCaptureStreamAHKey_MTE
+ _kFigCaptureStreamAHKey_TE
+ _kFigCaptureStreamMetadata_AH
+ _kFigCaptureStreamMetadata_IREnabled
+ _kFigCaptureStreamProperty_AHE
- GCC_except_table388
- GCC_except_table425
- GCC_except_table435
- GCC_except_table444
- GCC_except_table451
- GCC_except_table504
- GCC_except_table506
- GCC_except_table522
- GCC_except_table526
- GCC_except_table543
- GCC_except_table546
- GCC_except_table552
- GCC_except_table556
- GCC_except_table56
- GCC_except_table563
- GCC_except_table591
- GCC_except_table593
- GCC_except_table615
- GCC_except_table692
- GCC_except_table693
- GCC_except_table698
- GCC_except_table705
- GCC_except_table706
- GCC_except_table707
- GCC_except_table712
- GCC_except_table718
- GCC_except_table719
- GCC_except_table746
- GCC_except_table771
- GCC_except_table772
- GCC_except_table783
- GCC_except_table787
- GCC_except_table789
- GCC_except_table791
- GCC_except_table805
- _CFPropertyListCreateDeepCopy
- _ZL18StopExclaveStreamsP16ISPCaptureDeviceP16ISPCaptureStream
- _ZL32AddDCSIMUDataPoolToFrameReceiverP16ISPCaptureStreamP16ISPCaptureDevice
- __ZL32AddDCSIMUDataPoolToFrameReceiverP16ISPCaptureStreamP16ISPCaptureDevice
- _dispatch_get_global_queue
CStrings:
+ "%s - Failed to update config retry=%u ret=%#x\n"
+ "%s - Unable to power off EK, channel=%d\n"
+ "%s - Unable to stop exclave streams, ret=0x%08X, channel=%d\n"
+ "PowerOffExclaveChannel"
+ "Shared VA Stats"
+ "StopExclaveChannel"
+ "com.apple.isp.notifications"
+ "tgtEstMax"
+ "tgtEstStddev"
- "%s - %s - Could not get pool info for CISP_POOL_DCS_IMU_DATA: 0x%08X\n"
- "%s - %s - Failed to add IMU data pool: 0x%08X\n"
- "%s - Unsupported poolType=%d\n"
- "AddDCSIMUDataPoolToFrameReceiver"
- "CISP_POOL_DCS_IMU_DATA"
- "EnableDCSIMUData_Private"
- "IMU"
- "StopExclaveStreams"

```
