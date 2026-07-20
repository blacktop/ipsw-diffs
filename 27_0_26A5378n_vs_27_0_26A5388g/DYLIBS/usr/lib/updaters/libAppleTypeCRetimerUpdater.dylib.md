## libAppleTypeCRetimerUpdater.dylib

> `/usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-1587.0.21.0.0
-  __TEXT.__text: 0x4495c
+1587.0.27.0.0
+  __TEXT.__text: 0x44a2c
   __TEXT.__objc_methlist: 0x42f4
   __TEXT.__cstring: 0x89ed
   __TEXT.__const: 0x570
Symbols:
+ _UARPLayer2RequestBuffer_typed
- _UARPLayer2RequestBuffer
Functions:
~ _uarpAllocateTransmitBuffer2 : 224 -> 232
~ _UARPLayer2RequestBuffer -> _UARPLayer2RequestBuffer_typed : 100 -> 96
~ _UARPLayer2RequestTransmitMsgBuffer : 136 -> 144
~ _uarpPlatformPrepareAsset : 352 -> 368
~ _uarpPlatformCreateRxAsset : 108 -> 124
~ _uarpPlatformRemoteEndpointAddEntry : 232 -> 240
~ _uarpPlatformEndpointRecvMessage : 5460 -> 5468
~ _uarpPlatformAssetResponseData : 452 -> 460
~ _uarpPlatformAssetPayloadPullData : 380 -> 396
~ _uarpPlatformAssetPullAllPayloadHeaders : 240 -> 260
~ _uarpProcessTLV2 : 228 -> 244
~ _uarpPlatformAssetPullAllMetaData : 348 -> 356
~ _uarpPlatformEndpointAssetAcceptWithPayloadAndDecompressionWindows : 776 -> 784
~ _uarpPlatformConfigureEndpointIDs : 168 -> 176
~ _uarpPlatformConfigureEndpointTags : 232 -> 240
~ _uarpPlatformEndpointStreamingRecvInit : 176 -> 200
~ _uarpProcessPayloadTLVInternal : 692 -> 724
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hUpfM6/Sources/libAppleSilicon/tunableh/v2/tunableh.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Wa6rN3/Sources/libAppleSilicon/tunableh/v2/tunableh.c"
```
