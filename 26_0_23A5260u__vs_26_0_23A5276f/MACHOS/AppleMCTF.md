## AppleMCTF

> `/System/Library/Video/Plug-Ins/AppleMCTF.bundle/AppleMCTF`

```diff

-903.95.1.0.0
-  __TEXT.__text: 0x72bdc
-  __TEXT.__auth_stubs: 0xd10
+904.17.0.0.0
+  __TEXT.__text: 0x73800
+  __TEXT.__auth_stubs: 0xd30
   __TEXT.__objc_stubs: 0x20
   __TEXT.__init_offsets: 0x4
-  __TEXT.__cstring: 0x22bc9
-  __TEXT.__gcc_except_tab: 0x620
-  __TEXT.__const: 0x135e8
+  __TEXT.__gcc_except_tab: 0x648
+  __TEXT.__cstring: 0x22c8f
+  __TEXT.__const: 0x135d8
   __TEXT.__objc_methname: 0xb
   __TEXT.__unwind_info: 0x600
-  __DATA_CONST.__auth_got: 0x698
-  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__auth_got: 0x6a8
+  __DATA_CONST.__got: 0x438
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x3b80
-  __DATA_CONST.__cfstring: 0x300
+  __DATA_CONST.__const: 0x3b70
+  __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0xe0
-  __DATA.__bss: 0x718
+  __DATA.__bss: 0x858
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8442806B-04E2-3A71-8BAE-B6D6F82B85CA
-  Functions: 607
-  Symbols:   348
-  CStrings:  2930
+  UUID: 8AF22133-E638-3ED4-A106-9C1D5C5CD133
+  Functions: 612
+  Symbols:   353
+  CStrings:  2935
 
Symbols:
+ _VTTemporalFilterPluginSessionCleanUpAfterProcessing
+ _kVTSampleAttachmentQualityMetricsKey_ChromaBlueMeanSquaredError
+ _kVTSampleAttachmentQualityMetricsKey_ChromaRedMeanSquaredError
+ _kVTSampleAttachmentQualityMetricsKey_LumaMeanSquaredError
+ _strtol
CStrings:
+ "%lld %d AVE %s: %s:%d %d %d %d %d %d | %d %d"
+ "%lld %d AVE %s: %s:%d %d %d %d %d %d | %d %d\n"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x gain %d rIdx %d s %d"
+ "%lld %d AVE %s: %s:%d %p sID 0x%x gain %d rIdx %d s %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to create CFArray %p %d %p"
+ "%lld %d AVE %s: %s:%d %s | fail to create CFArray %p %d %p\n"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d"
+ "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to set up IPC %p %lld %d"
+ "%lld %d AVE %s: %s:%d %s | fail to set up IPC %p %lld %d\n"
+ "%lld %d AVE %s: %s:%d %s | sensorID not supported 0x%x"
+ "%lld %d AVE %s: %s:%d %s | sensorID not supported 0x%x\n"
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
+ "20:51:05"
+ "904.17.0"
+ "AVE_Enc_DecideInputQueueMaxCnt"
+ "AVE_MCTFISPGain1RefThreshold"
+ "AVE_MCTFISPGain2RefThreshold"
+ "AVE_MCTFMaxNextRefNum"
+ "AVE_MCTF_SMap"
+ "AVE_MSE_MakeDict"
+ "Jun 18 2025"
+ "SetUpIPC"
+ "TearDownIPC"
+ "pChromaBlueMSEArr != __null"
+ "pChromaRedMSEArr != __null"
+ "pLumaMSEArr != __null"
+ "pMSEDict != __null"
- "%lld %d AVE %s: %s:%d %p sID %d gain %d rIdx %d s %d"
- "%lld %d AVE %s: %s:%d %p sID %d gain %d rIdx %d s %d\n"
- "%lld %d AVE %s: %s:%d %s | AVE ERROR: AVE_USL_Drv_Start, Null pointer for pRCParams."
- "%lld %d AVE %s: %s:%d %s | AVE ERROR: AVE_USL_Drv_Start, Null pointer for pRCParams.\n"
- "%lld %d AVE %s: %s:%d %s | fail to create CFDictionary"
- "%lld %d AVE %s: %s:%d %s | fail to create CFDictionary\n"
- "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d%d"
- "%lld %d AVE %s: %s:%d %s | fail to initialize DAL %d %d%d\n"
- "%lld %d AVE %s: %s:%d %s | sensorID not supported %d"
- "%lld %d AVE %s: %s:%d %s | sensorID not supported %d\n"
- "%lld %d AVE %s: %s::%s:%d %p %llu Created frame #%lld at %p, prev:%p next:%p"
- "%lld %d AVE %s: %s::%s:%d %p %llu Created frame #%lld at %p, prev:%p next:%p\n"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create mutex %p %lld %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create mutex %p %lld %d %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create thread %p %lld %p %p %d"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create thread %p %lld %p %p %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create thread mutex %p %lld %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | fail to create thread mutex %p %lld %d %d\n"
- "20:22:35"
- "903.95.1"
- "ChromaBlueMeanSquaredError"
- "ChromaRedMeanSquaredError"
- "CreateQualityMetricsDictionary"
- "EntropyCodingHeader"
- "LumaMeanSquaredError"
- "May 30 2025"
- "pChromaBlueMeanSquaredErrorArr != __null"
- "pChromaRedMeanSquaredErrorArr != __null"
- "pInitSettings->pRCParams"
- "pLumaMeanSquaredErrorArr != __null"
- "pQualityMetricsDict != __null"

```
