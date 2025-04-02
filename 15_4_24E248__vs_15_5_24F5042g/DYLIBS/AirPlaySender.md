## AirPlaySender

> `/System/Library/PrivateFrameworks/AirPlaySender.framework/Versions/A/AirPlaySender`

```diff

-850.19.1.0.0
-  __TEXT.__text: 0x178308
-  __TEXT.__auth_stubs: 0x4690
+860.3.1.0.0
+  __TEXT.__text: 0x1791f0
+  __TEXT.__auth_stubs: 0x46a0
   __TEXT.__objc_methlist: 0x52c
   __TEXT.__const: 0xcf30
-  __TEXT.__gcc_except_tab: 0x554
-  __TEXT.__cstring: 0x591ba
+  __TEXT.__gcc_except_tab: 0x560
+  __TEXT.__cstring: 0x5978e
   __TEXT.__dlopen_cstrs: 0x164
   __TEXT.__oslogstring: 0x33e
-  __TEXT.__unwind_info: 0x3580
+  __TEXT.__unwind_info: 0x35a0
   __TEXT.__objc_classname: 0xb4
   __TEXT.__objc_methname: 0x14a4
   __TEXT.__objc_methtype: 0x8f1

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x660
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x2358
+  __AUTH_CONST.__auth_got: 0x2360
   __AUTH_CONST.__const: 0x7130
   __AUTH_CONST.__cfstring: 0xcdc0
   __AUTH_CONST.__objc_const: 0x6e0

   __AUTH.__data: 0x568
   __DATA.__objc_ivar: 0x44
   __DATA.__data: 0x179a0
-  __DATA.__bss: 0xf30
+  __DATA.__bss: 0xf38
   __DATA_DIRTY.__data: 0x5b0
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/Versions/A/WiFiPeerToPeer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6510
-  Symbols:   10314
-  CStrings:  7564
+  Functions: 6521
+  Symbols:   10333
+  CStrings:  7620
 
Symbols:
+ APAudioSourceSharedMemoryReaderCreate.cold.6
+ APAudioSourceSharedMemoryReaderCreate.cold.7
+ APAudioSourceSharedMemoryReaderCreate.cold.8
+ APAudioSourceSharedMemoryReaderCreate.cold.9
+ _FigSignalErrorAt3
+ ___getkMRMediaRemoteNowPlayingInfoAssetURLSymbolLoc_block_invoke
+ __block_descriptor_tmp.120
+ __block_descriptor_tmp.25
+ __block_descriptor_tmp.507
+ __block_descriptor_tmp.511
+ __block_descriptor_tmp.549
+ __block_descriptor_tmp.551
+ __block_descriptor_tmp.62
+ __block_descriptor_tmp.68
+ _fig_log_get_emitter
+ bufferedAudioEngine_updateMATAtmosPlaybackPreferenceIfNecessary.cold.3
+ getkMRMediaRemoteNowPlayingInfoAssetURLSymbolLoc.ptr
+ metadataSource_handleNowPlayingInfoChangedInternal.cold.45
- _FigSignalErrorAt
- __block_descriptor_tmp.20
- __block_descriptor_tmp.48
- __block_descriptor_tmp.501
- __block_descriptor_tmp.505
- __block_descriptor_tmp.543
- __block_descriptor_tmp.545
- __block_descriptor_tmp.58
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "(Fig)"
+ "-108"
+ "-876"
+ "-877"
+ "-878"
+ "-879"
+ "-880"
+ "860.3.1"
+ "APAudioSourceSharedMemory.c"
+ "APEndpoint.c"
+ "APEndpointPlaybackSessionRemoteControl.m"
+ "APEndpointStreamAggregateAudio.c"
+ "APSampleBufferConsumerForEndpointStreamAudioEngine.c"
+ "APVirtualDisplayTestSink.c"
+ "Action not supported"
+ "Allocation error"
+ "Audio source has been invalidated"
+ "CFStringRef getkMRMediaRemoteNowPlayingInfoAssetURL(void)"
+ "Cannot register path"
+ "Failed to create bufferMemObject"
+ "Failed to create deep copy"
+ "Failed to create stateMemObject"
+ "Failed to de-serialize"
+ "Failed to serialize"
+ "Invalid Trigger Token"
+ "Item is NULL"
+ "NULL audioEngine"
+ "NULL bufferMemObject in message"
+ "NULL stateMemObject in message"
+ "NULL trigger"
+ "NULL triggerTokenOut"
+ "No data in response"
+ "No incoming message"
+ "No matched request found"
+ "No trigger installed"
+ "Object invalidated"
+ "Only support one trigger installed at a time"
+ "alloc failed"
+ "bufferMemory region maps to NULL"
+ "bufferMemorySize is zero"
+ "can't find valid video track"
+ "err"
+ "kCMBaseObjectError_Invalidated"
+ "kCMBaseObjectError_ParamErr"
+ "kFigBaseObjectError_AllocationFailed"
+ "kFigBaseObjectError_ValueNotAvailable"
+ "kFigEndpointError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_AllocationFailed"
+ "kFigEndpointPlaybackSessionError_InvalidParameter"
+ "kMRMediaRemoteNowPlayingInfoAssetURL"
+ "messageID is missing in response event"
+ "sbceas_InstallLowWaterTrigger_block_invoke"
+ "sbceas_RemoveLowWaterTrigger_block_invoke"
+ "stateMemObject maps to NULL"
+ "stateMemoryLength < sizeof(RingState)"
+ "type is missing in response event"
- "850.19.1"

```
