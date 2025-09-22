## HomeAI

> `/System/Library/PrivateFrameworks/HomeAI.framework/HomeAI`

```diff

-348.1.1.0.0
-  __TEXT.__text: 0x15b42c
+351.0.0.0.0
+  __TEXT.__text: 0x15b374
   __TEXT.__auth_stubs: 0x1c70
   __TEXT.__init_offsets: 0x10
   __TEXT.__objc_methlist: 0x9aec
-  __TEXT.__const: 0x485d
-  __TEXT.__cstring: 0xd150
-  __TEXT.__gcc_except_tab: 0xc414
-  __TEXT.__oslogstring: 0x767e
+  __TEXT.__const: 0x484d
+  __TEXT.__cstring: 0xd13b
+  __TEXT.__gcc_except_tab: 0xc400
+  __TEXT.__oslogstring: 0x76b3
   __TEXT.__dlopen_cstrs: 0x116
-  __TEXT.__unwind_info: 0x4e40
+  __TEXT.__unwind_info: 0x4e38
   __TEXT.__eh_frame: 0x1e4
   __TEXT.__objc_classname: 0x1816
   __TEXT.__objc_methname: 0x15e56

   __DATA_CONST.__objc_arraydata: 0x618
   __AUTH_CONST.__auth_got: 0xe50
   __AUTH_CONST.__const: 0x45a0
-  __AUTH_CONST.__cfstring: 0x8760
+  __AUTH_CONST.__cfstring: 0x8740
   __AUTH_CONST.__objc_const: 0x14b30
   __AUTH_CONST.__objc_intobj: 0x540
   __AUTH_CONST.__objc_arrayobj: 0x360

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36DE63FB-CDAA-3B73-8E64-2E4A3DC8B7C2
-  Functions: 5222
-  Symbols:   17731
-  CStrings:  7909
+  UUID: C35C42F7-02BD-349C-8ECB-4247349F2AB8
+  Functions: 5220
+  Symbols:   17728
+  CStrings:  7908
 
Symbols:
+ -[HMIVideoAnalyzerClient analyzeFragment:configuration:]
+ -[HMIVideoAnalyzerServer analyzeFragment:configuration:]
+ ___39-[HMIVideoAnalyzerClient ensureSession]_block_invoke.228
+ ___56-[HMIVideoAnalyzerServer analyzeFragment:configuration:]_block_invoke
+ ___56-[HMIVideoAnalyzerServer analyzeFragment:configuration:]_block_invoke_2
+ _objc_msgSend$analyzeFragment:configuration:
- -[HMIVideoAnalyzerClient handleAssetData:withOptions:completionHandler:]
- -[HMIVideoAnalyzerServer handleAssetData:withOptions:completionHandler:]
- -[HMIVideoAnalyzerServer handleAssetData:withOptions:completionHandler:].cold.1
- _HMIGetMemoryState
- ___39-[HMIVideoAnalyzerClient ensureSession]_block_invoke.225
- ___72-[HMIVideoAnalyzerServer handleAssetData:withOptions:completionHandler:]_block_invoke
- ___72-[HMIVideoAnalyzerServer handleAssetData:withOptions:completionHandler:]_block_invoke_2
- _objc_msgSend$handleAssetData:withOptions:completionHandler:
CStrings:
+ "%{public}@Failed to create decompression session: %d"

```
