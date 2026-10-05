## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2260.11.1.0.0
-  __TEXT.__text: 0x7d6d8c
-  __TEXT.__objc_methlist: 0x3ac38
+2260.14.1.0.0
+  __TEXT.__text: 0x7d7974
+  __TEXT.__objc_methlist: 0x3ac50
   __TEXT.__const: 0xc680
-  __TEXT.__cstring: 0x9f784
-  __TEXT.__oslogstring: 0x1435e0
-  __TEXT.__gcc_except_tab: 0x2dc8
+  __TEXT.__cstring: 0x9f79e
+  __TEXT.__oslogstring: 0x143a07
+  __TEXT.__gcc_except_tab: 0x2ddc
   __TEXT.__ustring: 0x2d4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1b6f0
+  __TEXT.__unwind_info: 0x1b708
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_arraydata: 0x27d8
   __DATA_CONST.__got: 0x1dd8
   __AUTH_CONST.__const: 0x4588
-  __AUTH_CONST.__cfstring: 0x29e00
-  __AUTH_CONST.__objc_const: 0x6d1d8
+  __AUTH_CONST.__cfstring: 0x29e40
+  __AUTH_CONST.__objc_const: 0x6d248
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x52f8
   __AUTH_CONST.__objc_arrayobj: 0x1d88

   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__auth_got: 0x2c68
-  __AUTH.__data: 0xf8
-  __DATA.__objc_ivar: 0x7748
-  __DATA.__data: 0x7c68
+  __DATA.__objc_ivar: 0x7754
+  __DATA.__data: 0x1c10
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0xcee0
-  __DATA_DIRTY.__data: 0x420
-  __DATA_DIRTY.__bss: 0xab0
+  __DATA_DIRTY.__data: 0x6570
+  __DATA_DIRTY.__bss: 0x4c0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 35503
-  Symbols:   42030
-  CStrings:  34121
+  Functions: 35510
+  Symbols:   42036
+  CStrings:  34132
 
Symbols:
+ -[VCVideoStreamSendGroupConfig enableSyncGroupReferenceTimestamp]
+ -[VCVideoStreamSendGroupConfig setEnableSyncGroupReferenceTimestamp:]
+ _OBJC_IVAR_$_VCCoreAudio_AudioUnitMock._isImplicitPreferenceSession
+ _OBJC_IVAR_$_VCVideoStreamSendGroup._enableSyncGroupReferenceTimestamp
+ _OBJC_IVAR_$_VCVideoStreamSendGroupConfig._enableSyncGroupReferenceTimestamp
+ ___44-[VCControlChannelMultiWay lastUsedMKIBytes]_block_invoke
+ ___block_descriptor_40_e8_32o_e232_v20?0i8^{FigRemoteOperation=iiQ^{__CFString}(?={?=^{__CFDictionary}^{__CFDictionary}}{?=^v^{__IOSurface}^{__IOSurface}}{?=^{opaqueCMSampleBuffer}Q^{__CFArray}}{?=^{opaqueCMFormatDescription}}{?=q^{opaqueCMFormatDescription}^IQ})}12ls32l8
- ___block_descriptor_40_e8_32o_e229_v20?0i8^{FigRemoteOperation=iiQ^{__CFString}(?={?=^{__CFDictionary}^{__CFDictionary}}{?=^v^{__IOSurface}^{__IOSurface}}{?=^{opaqueCMSampleBuffer}Q^{__CFArray}}{?=^{opaqueCMFormatDescription}}{?=q^{opaqueCMFormatDescription}})}12ls32l8
CStrings:
+ " [%s] %s:%d %@(%p) Video frame is too old and modulated timestamp rolled backward – dropping frame. modulatedTimestamp=%u, frameTimeInSec=%f, rtpTimestampRate=%u"
+ " [%s] %s:%d Bad buffer length(%zu) for FaceTime audio media control info with header bitmap 0x%x, expecting %zu"
+ " [%s] %s:%d Bad buffer length(%zu) for FaceTime audio media control info, expecting %zu"
+ " [%s] %s:%d Not enough buffer for ECN CE count"
+ " [%s] %s:%d Not enough buffer for ECN ECT1 count"
+ " [%s] %s:%d Not enough buffer for bandwidth estimation"
+ " [%s] %s:%d Not enough buffer for video burst loss"
+ " [%s] %s:%d SignalEncoder[%p] MSCEncoderSessionInit failed with error=%d"
+ " [%s] %s:%d Video frame is too old and modulated timestamp rolled backward – dropping frame. modulatedTimestamp=%u, frameTimeInSec=%f, rtpTimestampRate=%u"
+ " [%s] %s:%d [FTDC] _dualCaptureSupported=%d, useVirtualCapture=%d"
+ " [%s] %s:%d configureWithBuffer failed with error %08X for control info=%p, dropping it"
+ "-[VCControlChannelMultiWay lastUsedMKIBytes]_block_invoke"
+ "2260.14.1"
+ "VideoPacketBuffer [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/Others/VideoPacketBuffer.c:%d: VideoPacketBuffer[%p] Reusing cached plaintext for re-assembled frame timestamp=%u frameSequenceNumber=%d isLate=%d"
+ "lcid"
+ "rcid"
+ "v20@?0i8^{FigRemoteOperation=iiQ^{__CFString}(?={?=^{__CFDictionary}^{__CFDictionary}}{?=^v^{__IOSurface}^{__IOSurface}}{?=^{opaqueCMSampleBuffer}Q^{__CFArray}}{?=^{opaqueCMFormatDescription}}{?=q^{opaqueCMFormatDescription}^IQ})}12"
- " [%s] %s:%d Bad buffer length(%zu) for FaceTime audio media control info, expecting %u"
- " [%s] %s:%d SignalEncoder[%p] MSCEncoderSessionCreate failed with error=%i"
- " [%s] %s:%d [FTDC] _dualCaptureSupported=%d"
- "-[VCControlChannelMultiWay lastUsedMKIBytes]"
- "2260.11.1"
- "v20@?0i8^{FigRemoteOperation=iiQ^{__CFString}(?={?=^{__CFDictionary}^{__CFDictionary}}{?=^v^{__IOSurface}^{__IOSurface}}{?=^{opaqueCMSampleBuffer}Q^{__CFArray}}{?=^{opaqueCMFormatDescription}}{?=q^{opaqueCMFormatDescription}})}12"
```
