## libAppleTypeCRetimerUpdater.dylib

> `/usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib`

```diff

-1345.160.8.0.1
-  __TEXT.__text: 0x45a30
+1345.160.9.700.1
+  __TEXT.__text: 0x45af8
   __TEXT.__auth_stubs: 0xa20
   __TEXT.__objc_methlist: 0x42f4
   __TEXT.__cstring: 0x7c80
Symbols:
+ _UARPLayer2RequestBuffer_typed
- _UARPLayer2RequestBuffer
Functions:
~ _uarpAllocateTransmitBuffer2 : 224 -> 232
~ _UARPLayer2RequestBuffer -> _UARPLayer2RequestBuffer_typed : 100 -> 96
~ _UARPLayer2RequestTransmitMsgBuffer : 136 -> 144
~ _uarpPlatformPrepareAsset : 352 -> 368
~ _uarpPlatformCreateRxAsset : 108 -> 124
~ _uarpPlatformRemoteEndpointAddEntry : 228 -> 236
~ _uarpPlatformEndpointRecvMessage : 5284 -> 5292
~ _uarpPlatformAssetPayloadPullData : 380 -> 396
~ _uarpPlatformAssetPullAllPayloadHeaders : 240 -> 260
~ _uarpProcessTLV : 196 -> 212
~ _uarpPlatformAssetPullAllMetaData : 348 -> 356
~ _uarpPlatformEndpointAssetAcceptWithPayloadAndDecompressionWindows : 776 -> 784
~ _uarpPlatformConfigureEndpointIDs : 156 -> 164
~ _uarpPlatformConfigureEndpointTags : 216 -> 224
~ _uarpPlatformEndpointStreamingRecvInit : 176 -> 200
~ _uarpProcessPayloadTLVInternal : 692 -> 724
```
