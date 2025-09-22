## AssetCacheServices

> `/System/Library/PrivateFrameworks/AssetCacheServices.framework/AssetCacheServices`

```diff

-131.0.0.0.0
-  __TEXT.__text: 0x14b14
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x7a4
+134.0.0.0.0
+  __TEXT.__text: 0x15034
+  __TEXT.__auth_stubs: 0xb00
+  __TEXT.__objc_methlist: 0x7bc
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x17c
-  __TEXT.__cstring: 0x10b7
-  __TEXT.__oslogstring: 0xbf9
+  __TEXT.__cstring: 0x10d6
+  __TEXT.__oslogstring: 0xd75
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x460
+  __TEXT.__unwind_info: 0x468
   __TEXT.__objc_classname: 0x151
-  __TEXT.__objc_methname: 0x1e12
-  __TEXT.__objc_methtype: 0xa1c
-  __TEXT.__objc_stubs: 0x1820
+  __TEXT.__objc_methname: 0x1e68
+  __TEXT.__objc_methtype: 0xa1e
+  __TEXT.__objc_stubs: 0x1860
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0xe78
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1188
-  __DATA_CONST.__objc_selrefs: 0x6d0
-  __AUTH_CONST.__cfstring: 0xe80
+  __DATA_CONST.__objc_const: 0x11b8
+  __DATA_CONST.__objc_selrefs: 0x6e0
+  __DATA_CONST.__objc_classrefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__cfstring: 0xea0
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__auth_got: 0x588
-  __DATA.__objc_classrefs: 0xd8
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x50
+  __AUTH_CONST.__auth_got: 0x590
+  __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x300
   __DATA.__bss: 0x30
-  __DATA_DIRTY.__const: 0x60
+  __DATA_DIRTY.__const: 0x40
   __DATA_DIRTY.__objc_const: 0x1f0
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x78

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CB7833DA-0782-3B66-B1A8-329B0151E060
-  Functions: 346
-  Symbols:   1350
-  CStrings:  768
+  UUID: 8FD559BC-403C-304F-B5F7-0C3EFCD8522D
+  Functions: 355
+  Symbols:   1372
+  CStrings:  783
 
Symbols:
+ -[ACSURLSession _cancelDownloadTask:byProducingResumeData:].cold.2
+ -[ACSURLSession _resumeTask:].cold.2
+ -[ACSURLSessionTask _internalState]
+ -[ACSURLSessionTask set_internalState:]
+ _OBJC_IVAR_$_ACSURLSessionTask.__internalState
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___29-[ACSURLSession _cancelTask:]_block_invoke.cold.1
+ ___30-[ACSURLSession _suspendTask:]_block_invoke.cold.1
+ ___54-[ACSURLSession URLSession:task:didCompleteWithError:]_block_invoke.210
+ ___59-[ACSURLSession _cancelDownloadTask:byProducingResumeData:]_block_invoke.122
+ ___59-[ACSURLSession _cancelDownloadTask:byProducingResumeData:]_block_invoke.cold.1
+ ___67-[ACSURLSession URLSession:downloadTask:didFinishDownloadingToURL:]_block_invoke.231
+ ___74-[ACSURLSession URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.214
+ ___74-[ACSURLSession URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke_2.217
+ ___78-[ACSURLSession _dataTask:completedWithData:response:error:completionHandler:]_block_invoke.144
+ ___86-[ACSURLSession _downloadTask:completedWithLocation:response:error:completionHandler:]_block_invoke.155
+ ___block_descriptor_72_e8_32s40s48bs56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.167
+ __os_log_fault_impl
+ _objc_msgSend$_internalState
+ _objc_msgSend$set_internalState:
- ___54-[ACSURLSession URLSession:task:didCompleteWithError:]_block_invoke.207
- ___59-[ACSURLSession _cancelDownloadTask:byProducingResumeData:]_block_invoke.118
- ___67-[ACSURLSession URLSession:downloadTask:didFinishDownloadingToURL:]_block_invoke.228
- ___74-[ACSURLSession URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.211
- ___74-[ACSURLSession URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke_2.214
- ___78-[ACSURLSession _dataTask:completedWithData:response:error:completionHandler:]_block_invoke.140
- ___86-[ACSURLSession _downloadTask:completedWithLocation:response:error:completionHandler:]_block_invoke.151
- ___block_descriptor_64_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.164
CStrings:
+ "ACSURLSession failed to convert resume data: %{public}@"
+ "ACSURLSessionDownloadTask _cancelDownloadTask:byProducingResumeData: completing with nil"
+ "Invalid resume data from NSURL"
+ "T@\"NSString\",?,R,C"
+ "Tq,V__internalState"
+ "__internalState"
+ "_cancelDownloadTask:%@ task already completed"
+ "_cancelTask:%@ task already completed"
+ "_internalState"
+ "_resumeTask:%@ task is aleady completed"
+ "_suspendTask:%@ task already completed"
+ "q"
+ "set_internalState:"

```
