## AppleVideoEncoder

> `/System/Library/Video/Plug-Ins/AppleVideoEncoder.bundle/AppleVideoEncoder`

```diff

-903.95.1.0.0
-  __TEXT.__text: 0x189b94
-  __TEXT.__auth_stubs: 0x1040
+904.17.0.0.0
+  __TEXT.__text: 0x18b234
+  __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0xc
-  __TEXT.__const: 0x17018
-  __TEXT.__cstring: 0x51fec
-  __TEXT.__gcc_except_tab: 0x6c0
+  __TEXT.__const: 0x17028
+  __TEXT.__cstring: 0x520ab
+  __TEXT.__gcc_except_tab: 0x6fc
   __TEXT.__objc_methname: 0xb
-  __TEXT.__unwind_info: 0x888
-  __DATA_CONST.__auth_got: 0x830
-  __DATA_CONST.__got: 0x748
+  __TEXT.__unwind_info: 0x898
+  __DATA_CONST.__auth_got: 0x838
+  __DATA_CONST.__got: 0x760
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0xa568
-  __DATA_CONST.__cfstring: 0x15e0
+  __DATA_CONST.__const: 0xa510
+  __DATA_CONST.__cfstring: 0x1580
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x158
-  __DATA.__bss: 0xea8
+  __DATA.__bss: 0xfe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 922BEACB-FE32-3C64-880A-731B3B7A55C9
-  Functions: 1571
-  Symbols:   507
-  CStrings:  6743
+  UUID: 1E140DEF-DEC2-3C96-9E2A-86177DF7D4B9
+  Functions: 1577
+  Symbols:   511
+  CStrings:  6746
 
Symbols:
+ _kVTSampleAttachmentQualityMetricsKey_ChromaBlueMeanSquaredError
+ _kVTSampleAttachmentQualityMetricsKey_ChromaRedMeanSquaredError
+ _kVTSampleAttachmentQualityMetricsKey_LumaMeanSquaredError
+ _strtol
CStrings:
+ "%lld %d AVE %s: %s: Added (%d, %d) to SurfaceID dict, %p %lld %d"
+ "%lld %d AVE %s: %s: Added (%d, %d) to SurfaceID dict, %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %d %d %d %d %d | %d %d"
+ "%lld %d AVE %s: %s:%d %d %d %d %d %d | %d %d\n"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x gain %d rIdx %d s %d"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x gain %d rIdx %d s %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create CFArray %p %d %p"
+ "%lld %d AVE %s: %s:%d %s | fail to create CFArray %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize VCP %p %lld %d %d %d"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize VCP %p %lld %d %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to set up IPC %p %lld %d"
+ "%lld %d AVE %s: %s:%d %s | fail to set up IPC %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | sensorID not supported 0x%x"
+ "%lld %d AVE %s: %s:%d %s | sensorID not supported 0x%x\n"
+ "%lld %d AVE %s: %s:%d starting with bitrate %d (RCMode %d) FrameRate %d USAGE %d"
+ "%lld %d AVE %s: %s:%d starting with bitrate %d (RCMode %d) FrameRate %d USAGE %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %llu Created frame #%lld at %p"
+ "%lld %d AVE %s: %s::%s:%d %p %llu Created frame #%lld at %p\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to create mutex %p %lld"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to create mutex %p %lld\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to create thread %p %lld %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to create thread %p %lld %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to create thread mutex %p %lld"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to create thread mutex %p %lld\n"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to make MSE dictionary %d"
+ "%lld %d AVE %s: %s::%s:%d %s | fail to make MSE dictionary %d\n"
+ "%lld %d AVE %s: %s::%s:%d long thread creation time %p %lld %d"
+ "%lld %d AVE %s: %s::%s:%d long thread creation time %p %lld %d\n"
+ "%lld %d AVE %s: MCTF with %d refs no change. overallgain: %d.%03d"
+ "%lld %d AVE %s: MCTF with %d refs no change. overallgain: %d.%03d\n"
+ "%lld %d AVE %s: MCTF with 1refs. overallgain: %d.%03d"
+ "%lld %d AVE %s: MCTF with 1refs. overallgain: %d.%03d\n"
+ "%lld %d AVE %s: MCTF with 2refs. overallgain: %d.%03d"
+ "%lld %d AVE %s: MCTF with 2refs. overallgain: %d.%03d\n"
+ "(-1) <= maxCnt && maxCnt <= 48"
+ "21:01:10"
+ "21:01:12"
+ "21:01:14"
+ "904.17.0"
+ "AVE_Enc_DecideInputQueueMaxCnt"
+ "AVE_MCTFISPGain1RefThreshold"
+ "AVE_MCTFISPGain2RefThreshold"
+ "AVE_MCTFMaxNextRefNum"
+ "AVE_MCTF_SMap"
+ "AVE_MSE_MakeDict"
+ "AVE_PROPERTY_KEY_MCTF_MAX_NEXT_REF_NUM"
+ "AVE_Prop_AVC_SetVBVBufferDuration"
+ "AVE_Prop_HEVC_GetMCTFMaxNextRefNum"
+ "AVE_Prop_HEVC_SetMCTFMaxNextRefNum"
+ "AVE_Prop_HEVC_SetVBVBufferDuration"
+ "Jun 18 2025"
+ "MCTFMaxNextRefNum"
+ "SetUpIPC"
+ "TearDownIPC"
+ "iMaxNextRefNum >= 0"
+ "pChromaBlueMSEArr != __null"
+ "pChromaRedMSEArr != __null"
+ "pLumaMSEArr != __null"
+ "pMSEDict != __null"
- "%lld %d AVE %s: %s Enter %lld %d %d %d"
- "%lld %d AVE %s: %s Enter %lld %d %d %d\n"
- "%lld %d AVE %s: %s Exit %lld %d %d %d %p %d"
- "%lld %d AVE %s: %s Exit %lld %d %d %d %p %d\n"
- "%lld %d AVE %s: %s: Addded (%d, %d) to SurfaceID dict, %p %lld %d"
- "%lld %d AVE %s: %s: Addded (%d, %d) to SurfaceID dict, %p %lld %d\n"
- "%lld %d AVE %s: %s:%d %p sID %d gain %d rIdx %d s %d"
- "%lld %d AVE %s: %s:%d %p sID %d gain %d rIdx %d s %d\n"
- "%lld %d AVE %s: %s:%d %s | AVE ERROR: AVE_USL_Drv_Prepare, Null pointer for pRCParams."
- "%lld %d AVE %s: %s:%d %s | AVE ERROR: AVE_USL_Drv_Prepare, Null pointer for pRCParams.\n"
- "%lld %d AVE %s: %s:%d %s | AVE ERROR: AVE_USL_Drv_Start, Null pointer for pRCParams."
- "%lld %d AVE %s: %s:%d %s | AVE ERROR: AVE_USL_Drv_Start, Null pointer for pRCParams.\n"
- "%lld %d AVE %s: %s:%d %s | fail to create CFDictionary"
- "%lld %d AVE %s: %s:%d %s | fail to create CFDictionary\n"
- "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d%d"
- "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d%d\n"
- "%lld %d AVE %s: %s:%d %s | failed to create VCP instance %p %lld %d %d"
- "%lld %d AVE %s: %s:%d %s | failed to create VCP instance %p %lld %d %d\n"
- "%lld %d AVE %s: %s:%d %s | sensorID not supported %d"
- "%lld %d AVE %s: %s:%d %s | sensorID not supported %d\n"
- "%lld %d AVE %s: %s:%d starting with bitrate %d (RCMode %d) FrameRate %d USAGE %d MaxNumLTR %d"
- "%lld %d AVE %s: %s:%d starting with bitrate %d (RCMode %d) FrameRate %d USAGE %d MaxNumLTR %d\n"
- "%lld %d AVE %s: %s::%s:%d %p %llu Created frame #%lld at %p, prev:%p next:%p"
- "%lld %d AVE %s: %s::%s:%d %p %llu Created frame #%lld at %p, prev:%p next:%p\n"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create mutex %p %lld %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create mutex %p %lld %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create thread %p %lld %p %p %d"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create thread %p %lld %p %p %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create thread mutex %p %lld %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create thread mutex %p %lld %d %d\n"
- "(-1) <= maxCnt && maxCnt <= 32"
- "20:31:42"
- "20:31:43"
- "20:31:46"
- "20:31:47"
- "903.95.1"
- "AVE_Prop_AVC_SetVBVBufferDuratoin"
- "AVE_Prop_HEVC_SetVBVBufferDuratoin"
- "AVE_VCP_Create"
- "AVE_VCP_Destroy"
- "ChromaBlueMeanSquaredError"
- "ChromaRedMeanSquaredError"
- "CreateQualityMetricsDictionary"
- "EntropyCodingHeader"
- "LumaMeanSquaredError"
- "May 30 2025"
- "VBVMaxRate"
- "kVTCompressionPropertyKey_VBVMaxRate"
- "pChromaBlueMeanSquaredErrorArr != __null"
- "pChromaRedMeanSquaredErrorArr != __null"
- "pINS->pcVCP != __null"
- "pInitSettings->pRCParams"
- "pLumaMeanSquaredErrorArr != __null"
- "pQualityMetricsDict != __null"
- "pcVCP != __null"

```
