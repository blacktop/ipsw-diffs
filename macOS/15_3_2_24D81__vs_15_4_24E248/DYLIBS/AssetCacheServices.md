## AssetCacheServices

> `/System/Library/PrivateFrameworks/AssetCacheServices.framework/Versions/A/AssetCacheServices`

```diff

-135.0.0.0.0
-  __TEXT.__text: 0x17664
+135.1.0.0.0
+  __TEXT.__text: 0x17d88
   __TEXT.__auth_stubs: 0x960
-  __TEXT.__objc_methlist: 0x7c0
-  __TEXT.__const: 0x130
+  __TEXT.__objc_methlist: 0xa6c
+  __TEXT.__const: 0x138
   __TEXT.__gcc_except_tab: 0x260
   __TEXT.__cstring: 0x114f
   __TEXT.__oslogstring: 0xd58
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__unwind_info: 0x4e8
   __TEXT.__objc_classname: 0x151
   __TEXT.__objc_methname: 0x1e45
   __TEXT.__objc_methtype: 0xa1e

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6e0
+  __DATA_CONST.__objc_selrefs: 0x790
   __DATA_CONST.__objc_superrefs: 0x28
   __AUTH_CONST.__auth_got: 0x4c0
   __AUTH_CONST.__const: 0xdb0
   __AUTH_CONST.__cfstring: 0xf00
-  __AUTH_CONST.__objc_const: 0x13a8
+  __AUTH_CONST.__objc_const: 0xed8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x54

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B32AEFAB-5BDF-37CA-A974-47D8EB0D058E
-  Functions: 393
-  Symbols:   1038
+  UUID: 7ABE9AB3-285E-3BD7-A7BF-27601F1973DA
+  Functions: 437
+  Symbols:   1088
   CStrings:  789
 
Symbols:
+ +[ACSURLSession sharedSession].cold.1
+ -[ACSURLSession _cancelDownloadTask:byProducingResumeData:].cold.3
+ -[ACSURLSession _locateCachingServerForURL:isUpload:completionHandler:].cold.1
+ -[ACSURLSession _resumeData:toNSURLResumeData:originalRequest:currentRequest:error:].cold.1
+ ACSImportFileIntoCachingServer.cold.1
+ ACSLocateCachingServer.cold.1
+ ACSMightCurrentNetworkHaveCachingServer.cold.1
+ ACSUpdateCachingServerHealth.cold.1
+ _ACSIntrospect.cold.1
+ _ACSLocateAllCachingServers.cold.1
+ _ACSSetTestFlags.cold.1
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __51-[ACSURLSession URLSession:task:needNewBodyStream:]_block_invoke.cold.1
+ __52-[ACSURLSession URLSession:dataTask:didReceiveData:]_block_invoke.cold.1
+ __52-[ACSURLSession URLSession:dataTask:didReceiveData:]_block_invoke.cold.2
+ __54-[ACSURLSession URLSession:didBecomeInvalidWithError:]_block_invoke.cold.1
+ __54-[ACSURLSession URLSession:task:didCompleteWithError:]_block_invoke.cold.1
+ __57-[ACSURLSession URLSession:dataTask:didBecomeStreamTask:]_block_invoke.cold.1
+ __57-[ACSURLSession URLSession:dataTask:didBecomeStreamTask:]_block_invoke.cold.2
+ __57-[ACSURLSession URLSession:taskIsWaitingForConnectivity:]_block_invoke.cold.1
+ __59-[ACSURLSession URLSession:dataTask:didBecomeDownloadTask:]_block_invoke.cold.1
+ __59-[ACSURLSession URLSession:dataTask:didBecomeDownloadTask:]_block_invoke.cold.2
+ __59-[ACSURLSession _cancelDownloadTask:byProducingResumeData:]_block_invoke.136.cold.1
+ __60-[ACSURLSession URLSession:task:didFinishCollectingMetrics:]_block_invoke.cold.1
+ __66-[ACSURLSession URLSession:didReceiveChallenge:completionHandler:]_block_invoke.cold.1
+ __67-[ACSURLSession URLSession:downloadTask:didFinishDownloadingToURL:]_block_invoke.cold.1
+ __67-[ACSURLSession URLSession:downloadTask:didFinishDownloadingToURL:]_block_invoke.cold.2
+ __71-[ACSURLSession URLSession:task:didReceiveChallenge:completionHandler:]_block_invoke.cold.1
+ __73-[ACSURLSession URLSession:dataTask:willCacheResponse:completionHandler:]_block_invoke.cold.1
+ __73-[ACSURLSession URLSession:dataTask:willCacheResponse:completionHandler:]_block_invoke.cold.2
+ __74-[ACSURLSession URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.cold.1
+ __74-[ACSURLSession URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke.cold.2
+ __78-[ACSURLSession URLSession:downloadTask:didResumeAtOffset:expectedTotalBytes:]_block_invoke.cold.1
+ __78-[ACSURLSession URLSession:downloadTask:didResumeAtOffset:expectedTotalBytes:]_block_invoke.cold.2
+ __89-[ACSURLSession URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:]_block_invoke.cold.1
+ __89-[ACSURLSession URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]_block_invoke.cold.1
+ __98-[ACSURLSession URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:]_block_invoke.cold.1
+ __98-[ACSURLSession URLSession:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:]_block_invoke.cold.2

```
