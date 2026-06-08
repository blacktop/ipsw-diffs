## CoreLocationTiles

> `/System/Library/PrivateFrameworks/CoreLocationTiles.framework/CoreLocationTiles`

```diff

-3075.0.8.0.0
-  __TEXT.__text: 0x2014
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0xf8
+3164.0.0.0.0
+  __TEXT.__text: 0x2b20
+  __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0xc9
-  __TEXT.__cstring: 0x354
-  __TEXT.__oslogstring: 0x899
-  __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__unwind_info: 0x198
-  __TEXT.__objc_classname: 0x32
-  __TEXT.__objc_methname: 0x3d1
-  __TEXT.__objc_methtype: 0x194
-  __TEXT.__objc_stubs: 0x380
-  __DATA_CONST.__got: 0x80
+  __TEXT.__cstring: 0x484
+  __TEXT.__oslogstring: 0xa73
+  __TEXT.__gcc_except_tab: 0x224
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x138
+  __DATA_CONST.__weak_got: 0x8
+  __DATA_CONST.__objc_selrefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1f8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0xb0
-  __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__objc_const: 0x210
+  __AUTH_CONST.__weak_auth_got: 0x18
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0x8d0
+  __DATA.__objc_ivar: 0x14
+  __DATA.__data: 0x910
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x10

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3D0AA1B7-D0FA-31BB-B1E1-C2F83741BD92
-  Functions: 52
-  Symbols:   578
-  CStrings:  131
+  UUID: 26A14B4E-5D64-378A-A226-ED57F54D310C
+  Functions: 62
+  Symbols:   633
+  CStrings:  84
 
Symbols:
+ -[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:]
+ -[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:].cold.1
+ -[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:].cold.2
+ -[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:].cold.3
+ -[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:].cold.4
+ -[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:].cold.5
+ -[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:].cold.6
+ -[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:].cold.7
+ -[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:].cold.8
+ -[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:].cold.9
+ -[CLTileRemoteDownloader onFileDownload]
+ -[CLTileRemoteDownloader setOnFileDownload:]
+ GCC_except_table12
+ GCC_except_table30
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table43
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table46
+ GCC_except_table47
+ _OBJC_IVAR_$_CLTileRemoteDownloader._onFileDownload
+ __ZNSt12length_errorC1B9foe220100EPKc
+ __ZNSt3__110unique_ptrI12CLConnection19CLConnectionDeleterE5resetB9foe220100EPS1_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe220100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE22__init_internal_bufferB9foe220100Em
+ __ZNSt3__112construct_atB9foe220100I19CLConnectionMessageJRA26_KcRP12NSDictionaryEPS1_EEPT_SA_DpOT0_
+ __ZNSt3__112construct_atB9foe220100I19CLConnectionMessageJRA32_KcEPS1_EEPT_S7_DpOT0_
+ __ZNSt3__112construct_atB9foe220100I19CLConnectionMessageJRA35_KcRP12NSDictionaryEPS1_EEPT_SA_DpOT0_
+ __ZNSt3__112construct_atB9foe220100I19CLConnectionMessageJRA41_KcEPS1_EEPT_S7_DpOT0_
+ __ZNSt3__115allocate_sharedB9foe220100I19CLConnectionMessageNS_9allocatorIS1_EEJRA26_KcRP12NSDictionaryELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I19CLConnectionMessageNS_9allocatorIS1_EEJRA32_KcELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I19CLConnectionMessageNS_9allocatorIS1_EEJRA35_KcRP12NSDictionaryELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB9foe220100I19CLConnectionMessageNS_9allocatorIS1_EEJRA41_KcELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__119__shared_weak_count16__release_sharedB9foe220100Ev
+ __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B9foe220100IJRA26_KcRP12NSDictionaryES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B9foe220100IJRA32_KcES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B9foe220100IJRA35_KcRP12NSDictionaryES3_Li0EEES3_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B9foe220100IJRA41_KcES3_Li0EEES3_DpOT_
+ __ZNSt3__120__throw_length_errorB9foe220100EPKc
+ _logObject_CLPerceptionHelper_Default
+ _logObject_Flip_Default
+ _logObject_Geotagging_Default
+ _logObject_HeadToHeadset_Default
+ _objc_msgSend$onFileDownload
+ _objc_msgSend$setOnFileDownload:
+ _onceToken_CLPerceptionHelper_Default
+ _onceToken_Flip_Default
+ _onceToken_Geotagging_Default
+ _onceToken_HeadToHeadset_Default
- GCC_except_table24
- GCC_except_table26
- GCC_except_table29
- GCC_except_table34
- GCC_except_table35
- GCC_except_table36
- GCC_except_table37
- __ZNSt12length_errorC1B9nqe210106EPKc
- __ZNSt3__110unique_ptrI12CLConnection19CLConnectionDeleterE5resetB9nqe210106EPS1_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9nqe210106Ev
- __ZNSt3__112construct_atB9nqe210106I19CLConnectionMessageJRA35_KcRP12NSDictionaryEPS1_EEPT_SA_DpOT0_
- __ZNSt3__112construct_atB9nqe210106I19CLConnectionMessageJRA41_KcEPS1_EEPT_S7_DpOT0_
- __ZNSt3__115allocate_sharedB9nqe210106I19CLConnectionMessageNS_9allocatorIS1_EEJRA35_KcRP12NSDictionaryELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB9nqe210106I19CLConnectionMessageNS_9allocatorIS1_EEJRA41_KcELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__119__shared_weak_count16__release_sharedB9nqe210106Ev
- __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B9nqe210106IJRA35_KcRP12NSDictionaryES3_Li0EEES3_DpOT_
- __ZNSt3__120__shared_ptr_emplaceI19CLConnectionMessageNS_9allocatorIS1_EEEC2B9nqe210106IJRA41_KcES3_Li0EEES3_DpOT_
- __ZNSt3__120__throw_length_errorB9nqe210106EPKc
- _memcpy
CStrings:
+ "TileRemoteDownloader Ignoring new download request with invalid destination url"
+ "kCLConnectionDownloadFile"
+ "kCLConnectionDownloadFileCancel"
+ "kCLConnectionDownloadFileDestinationURLKey"
+ "kCLConnectionDownloadFileError"
+ "kCLConnectionDownloadFileErrorKey"
+ "kCLConnectionDownloadFileKey"
+ "kCLConnectionDownloadFileRequestKey"
+ "kCLConnectionDownloadFileSuccess"
+ "kCLConnectionDownloadFileURLResponseKey"
+ "{\"msg%{public}.0s\":\"#TileRemoteDownloader - starting request\", \"self\":\"%{public}p\", \"connection\":\"%{public}p\", \"canDownloadOverCellular\":%{public}hhd, \"srcURL\":%{public, location:escape_only}@, \"destination\":%{private, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"TileRemoteDownloader Ignoring new download request with invalid destination url\", \"destination\":%{private, location:escape_only}@}"
- ".cxx_construct"
- ".cxx_destruct"
- "@\"NSObject<OS_dispatch_queue>\""
- "@16@0:8"
- "@28@0:8@16B24"
- "@32@0:8{unique_ptr<CLConnection, CLConnectionDeleter>={?=^{CLConnection}}}16@24"
- "@?"
- "@?16@0:8"
- "B"
- "B16@0:8"
- "B48@0:8r*16r*24d32@?40"
- "CLCertificatePinningHelper"
- "CLTileRemoteDownloader"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@?,C,N,V_onDownloadAndDecompression"
- "TB,N,V_canDownloadOverCellular"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLWithString:"
- "UTF8String"
- "_canDownloadOverCellular"
- "_connection"
- "_onDownloadAndDecompression"
- "_queue"
- "allKeys"
- "authenticationMethod"
- "canDownloadOverCellular"
- "cancel"
- "credentialForTrust:"
- "dealloc"
- "dictionaryWithObjects:forKeys:count:"
- "downloadAndDecompressFrom:toDecompressedDestination:withTimeout:withCompletionHandler:"
- "errorWithDomain:code:userInfo:"
- "fileURLWithPath:isDirectory:"
- "handleDisconnection"
- "handleMessage:"
- "host"
- "i40@0:8@16@24@?32"
- "init"
- "initWithConnection:onQueue:"
- "initWithQueue:canDownloadOverCellular:"
- "initialize"
- "isEqualToString:"
- "knownHosts"
- "null"
- "objectForKeyedSubscript:"
- "onDownloadAndDecompression"
- "protectionSpace"
- "queue"
- "requestWithURL:"
- "serverTrust"
- "setAllowsCellularAccess:"
- "setCanDownloadOverCellular:"
- "setOnDownloadAndDecompression:"
- "setQueue:"
- "setTimeoutInterval:"
- "setWithObjects:"
- "setup"
- "stringWithUTF8String:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v32@0:8{shared_ptr<CLConnectionMessage>=^{CLConnectionMessage}^{__shared_weak_count}}16"
- "{unique_ptr<CLConnection, CLConnectionDeleter>=\"\"{?=\"__ptr_\"^{CLConnection}}}"

```
