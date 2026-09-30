## BTAudioHALPlugin

> `/System/Library/Audio/Plug-Ins/HAL/BTAudioHALPlugin.driver/BTAudioHALPlugin`

```diff

 193.9.0.0.0
-  __TEXT.__text: 0x803b8
+  __TEXT.__text: 0x7b3e4
   __TEXT.__auth_stubs: 0x12e0
   __TEXT.__objc_stubs: 0x2720
-  __TEXT.__init_offsets: 0xa4
+  __TEXT.__init_offsets: 0xa0
   __TEXT.__objc_methlist: 0x1164
-  __TEXT.__gcc_except_tab: 0x20ec
-  __TEXT.__const: 0x1a0c
-  __TEXT.__cstring: 0x4aed
-  __TEXT.__oslogstring: 0x1471f
+  __TEXT.__gcc_except_tab: 0x1fd4
+  __TEXT.__const: 0x185c
+  __TEXT.__cstring: 0x4a84
+  __TEXT.__oslogstring: 0x142cb
   __TEXT.__objc_classname: 0x155
   __TEXT.__objc_methname: 0x3e7c
   __TEXT.__objc_methtype: 0x120f
-  __TEXT.__unwind_info: 0x1b78
+  __TEXT.__unwind_info: 0x1a68
   __TEXT.__eh_frame: 0x50
   __DATA_CONST.__auth_got: 0x980
   __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x5398
+  __DATA_CONST.__const: 0x4c30
   __DATA_CONST.__cfstring: 0x1620
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x20

   __DATA.__objc_ivar: 0x184
   __DATA.__objc_data: 0x410
   __DATA.__data: 0xb08
-  __DATA.__bss: 0x21008
+  __DATA.__bss: 0x16f58
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf.dylib
-  UUID: 69B94707-E020-3B61-A763-3B709F07C0B1
-  Functions: 2741
+  UUID: 000532C9-7CE2-3657-9207-8BEF47819A5A
+  Functions: 2647
   Symbols:   467
-  CStrings:  3016
+  CStrings:  2994
 
CStrings:
- "Delayed Transport Disconnect: Disconnect Timer Fired..Disconnect CIS"
- "Delayed Transport Disconnect: cisConnected = %d. Transport = %d"
- "Device sample rate changed %f -> %f [encoder = %d, decoder = %d]"
- "Input Decode: Bytes read is 0 bytesRead %lu"
- "LC3"
- "LECA Device XPC connection for UID %s connected to[ %d ] "
- "LECA StartIO CIS Already up"
- "LECA StartIO returns %x (%llu)"
- "LECA Starting IO on profile %{public}s, activeIO:%llu to %{public}@ mAudioObjectID: %u Wait IO Start %d"
- "LECA StopIO %{public}s, activeIO:%llu, need immediate CIS disconnect:%d"
- "LECA StopIO returns noErr (%llu)"
- "LECA StopIO: failed to stop because the ref count was already 0"
- "LECA: Codec Update completed Input = %{public}s Decoder = %d , Output = %{public}s Encoder = %d"
- "LECA: Direction %x Stream state output = %d input = %d"
- "LECA: Setting Supported Codecs"
- "LECA: UpdateSamplingRate minRate %f, maxRate %f"
- "LECA: Updating Codecs Input = %{public}s Decoder = %d , Output = %{public}s Encoder = %d"
- "Not disconnecting CIS"
- "Status : IO = %{public}s. CIS Up = %{public}s. Delayed Transport Disconnect: %{public}s"
- "UpdateCurrentBTAudioDeviceFromSampleRate LE Connected Audio  %f = %f"
- "kBTAudioMsgPropertyMaxChannels"
- "xpc_get_type(maxChannelsProp) == XPC_TYPE_INT64"

```
