## TilesService

> `/System/Library/PrivateFrameworks/CoreLocationTiles.framework/XPCServices/TilesService.xpc/TilesService`

```diff

-3075.0.8.0.0
-  __TEXT.__text: 0x633c
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0x660
-  __TEXT.__objc_methlist: 0x2f4
+3164.0.0.0.0
+  __TEXT.__text: 0x822c
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_stubs: 0x760
+  __TEXT.__objc_methlist: 0x34c
   __TEXT.__const: 0x1b8
-  __TEXT.__gcc_except_tab: 0x3e8
-  __TEXT.__cstring: 0x77d
-  __TEXT.__oslogstring: 0x19fc
-  __TEXT.__objc_classname: 0x84
-  __TEXT.__objc_methname: 0x92a
+  __TEXT.__gcc_except_tab: 0x4fc
+  __TEXT.__cstring: 0xac9
+  __TEXT.__oslogstring: 0x1ee8
+  __TEXT.__objc_classname: 0x83
+  __TEXT.__objc_methname: 0xac2
   __TEXT.__objc_methtype: 0x5d2
-  __TEXT.__unwind_info: 0x380
-  __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0xc0
+  __TEXT.__unwind_info: 0x408
   __DATA_CONST.__const: 0x378
-  __DATA_CONST.__cfstring: 0x260
+  __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x4c0
-  __DATA.__objc_selrefs: 0x2c8
-  __DATA.__objc_ivar: 0x18
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0xd0
+  __DATA.__objc_const: 0x520
+  __DATA.__objc_selrefs: 0x308
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0xa00
+  __DATA.__data: 0xa40
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B5976E97-3B56-3907-98F7-5C2A30D9CEE5
-  Functions: 147
-  Symbols:   148
-  CStrings:  288
+  UUID: 3EC846E1-C709-3DA6-B605-DED7E97BFF00
+  Functions: 182
+  Symbols:   152
+  CStrings:  326
 
Symbols:
+ _NSLocalizedDescriptionKey
+ _NSUnderlyingErrorKey
+ __ZN14CLTilesService25handleFileDownloadRequestENSt3__110shared_ptrI12CLConnectionEENS1_I19CLConnectionMessageEE
+ __ZN14CLTilesService33handleFileDownloadRequestCallbackENSt3__110shared_ptrI12CLConnectionEEP5NSURLP13NSURLResponseP7NSError
+ __ZN14CLTilesService37handleFileDownloadRequestCancellationENSt3__110shared_ptrI12CLConnectionEE
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- ___cxa_end_catch
- ___cxa_rethrow
CStrings:
+ "#TilesService unable to move downloaded file to destination"
+ "-[CLTileDownloadRequest onFileDownloadCompleted:withResponse:withError:]"
+ "/AppleInternal/Library/BuildRoots/4~CRCGugDwzbj2lBjcpHJMe1jm5_E0Hma95caVUkU/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__hash_table:1855: libc++ Hardening assertion __p != end() failed: unordered container::erase(iterator) called with a non-dereferenceable iterator\n"
+ "Invalid download location received from NSURLSession"
+ "T@\"NSURL\",&,N,V_downloadDestination"
+ "T@?,C,N,V_downloadCompletionHandler"
+ "_downloadCompletionHandler"
+ "_downloadDestination"
+ "downloadCompletionHandler"
+ "downloadDestination"
+ "downloadFileWithURLRequest:withURL:completionHandler:"
+ "handleFileDownloadRequest"
+ "handleFileDownloadRequestCallback"
+ "kCLConnectionDownloadFile"
+ "kCLConnectionDownloadFileCancel"
+ "kCLConnectionDownloadFileDestinationURLKey"
+ "kCLConnectionDownloadFileError"
+ "kCLConnectionDownloadFileErrorKey"
+ "kCLConnectionDownloadFileKey"
+ "kCLConnectionDownloadFileRequestKey"
+ "kCLConnectionDownloadFileSuccess"
+ "kCLConnectionDownloadFileURLResponseKey"
+ "moveItemAtURL:toURL:error:"
+ "onFileDownloadCompleted:withResponse:withError:"
+ "serveFileDownloadCompletionHandler:withResponse:withError:"
+ "setDownloadCompletionHandler:"
+ "setDownloadDestination:"
+ "{\"msg%{public}.0s\":\"#TilesService Successfully downloaded file\", \"statusCode\":%{public}ld, \"downloadDestination\":%{private, location:escape_only}@, \"self\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"#TilesService dropping response to connection due to it not being active anymore\", \"connection\":\"%{public}p\", \"downloadedFile\":%{private, location:escape_only}@, \"response\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#TilesService onDownloadCompleted\", \"location\":%{private, location:escape_only}@, \"response\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@, \"decompressionCompletionHandler\":\"%{public}p\", \"self\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"#TilesService onFileDownloadCompleted\", \"location\":%{private, location:escape_only}@, \"response\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@, \"downloadCompletionHandler\":\"%{public}p\", \"self\":\"%{public}p\"}"
+ "{\"msg%{public}.0s\":\"#TilesService sending response for download request\", \"connection\":\"%{public}p\", \"downloadedFile\":%{private, location:escape_only}@, \"response\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#TilesService unable to move downloaded file to destination\", \"temporaryLocation\":%{private, location:escape_only}@, \"finalDestination\":%{private, location:escape_only}@, \"moveError\":%{private, location:escape_only}@, \"self\":\"%{public}p\"}"
- "{\"msg%{public}.0s\":\"#TilesService onDowloadCompleted\", \"location\":%{private, location:escape_only}@, \"response\":%{private, location:escape_only}@, \"error\":%{private, location:escape_only}@, \"decompressionCompletionHandler\":\"%{public}p\", \"self\":\"%{public}p\"}"

```
