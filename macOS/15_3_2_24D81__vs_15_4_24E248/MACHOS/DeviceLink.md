## DeviceLink

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceLink.framework/Versions/A/DeviceLink`

```diff

 299.0.0.0.0
-  __TEXT.__text: 0xf350
+  __TEXT.__text: 0xf2cc
   __TEXT.__auth_stubs: 0xd10
   __TEXT.__cstring: 0x5560
   __TEXT.__const: 0x48
-  __TEXT.__unwind_info: 0x388
+  __TEXT.__unwind_info: 0x378
   __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__auth_ptr: 0x8
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x220
   __DATA_CONST.__cfstring: 0x3780
   __DATA.__data: 0x38

   - /System/Library/PrivateFrameworks/CacheDelete.framework/Versions/A/CacheDelete
   - /System/Library/PrivateFrameworks/MobileDevice.framework/Versions/A/MobileDevice
   - /usr/lib/libSystem.B.dylib
-  UUID: AEED335D-A90E-38B4-A996-F335ABBEE42B
-  Functions: 292
+  UUID: F9A9AF27-A2CF-3FFD-B876-FF200FE72436
+  Functions: 290
   Symbols:   551
   CStrings:  1055
 
Functions:
~ _printFileTransferStatus : 448 -> 444
~ __DLHandlerThreadMessagePortCallback : 6264 -> 6344
- sub_3688
~ __DLHandlerThreadWriteMessage : 116 -> 104
~ _DLWaitForConnection : 424 -> 420
~ _DLConnect : 408 -> 404
~ _DLDeviceReady : 116 -> 104
~ __DLOperationProgressContextInit : 152 -> 156
~ __DLEnumerateContentsOfDirectoryOnComputer : 456 -> 452
~ __DLCopyFileOnComputer : 488 -> 492
~ ___DLCopyItemOnComputer : 328 -> 324
~ __DLMoveItemsOnComputerCallback : 320 -> 312
~ __DLRemoveItemOnComputer : 260 -> 252
~ __DLBulkOperationSendFinalChunk : 180 -> 176
~ __DLSendFileForBulkOperation : 352 -> 332
~ __DLReceiveFileForBulkOperation : 552 -> 524
~ __DLMainThreadMessagePortCallback : 3648 -> 3728
- sub_841c
~ _SocketCreateLocalServer : 280 -> 268
~ _SocketLog : 108 -> 96
~ _SocketConnectLocal : 216 -> 212
~ __DLLog : 1936 -> 1956
~ _DLGetFlockForFileWithCancel : 880 -> 884
~ _initializeLogging : 112 -> 108
~ _DLConnectionInfoCreateForEndpoint : 256 -> 200
~ _DLEndpointCreateDescription : 144 -> 136
~ _DLDeviceWaitForAttachedDevice : 432 -> 424
~ _DLConnectToServiceOnDeviceWithOptions : 364 -> 368
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DeviceLink/Utility/DeviceLinkListener.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DeviceLink/Utility/DeviceLinkThread.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DeviceLink/Utility/DeviceLinkUtility.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DeviceLink/WireProtocol/DeviceLinkConnection.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DeviceLink/WireProtocol/GenericConnectionCallbacks.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DeviceLink/WireProtocol/SocketStreamHandler.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/DeviceLink/WireProtocol/StreamHandler.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DeviceLink/Utility/DeviceLinkListener.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DeviceLink/Utility/DeviceLinkThread.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DeviceLink/Utility/DeviceLinkUtility.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DeviceLink/WireProtocol/DeviceLinkConnection.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DeviceLink/WireProtocol/GenericConnectionCallbacks.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DeviceLink/WireProtocol/SocketStreamHandler.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/DeviceLink/WireProtocol/StreamHandler.c"

```
