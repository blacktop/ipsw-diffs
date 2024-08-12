## AirPlaySupport

> `/System/Library/PrivateFrameworks/AirPlaySupport.framework/AirPlaySupport`

```diff

-800.68.1.0.0
-  __TEXT.__text: 0x6fe74
-  __TEXT.__auth_stubs: 0x2bf0
+830.2.0.0.0
+  __TEXT.__text: 0x702fc
+  __TEXT.__auth_stubs: 0x2c00
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0xcb0
+  __TEXT.__const: 0xcc8
   __TEXT.__gcc_except_tab: 0x188
-  __TEXT.__cstring: 0x1d15e
+  __TEXT.__cstring: 0x1d115
   __TEXT.__oslogstring: 0x6c
-  __TEXT.__unwind_info: 0x12d0
+  __TEXT.__unwind_info: 0x12d8
   __TEXT.__objc_classname: 0x18
   __TEXT.__objc_methname: 0x68f
   __TEXT.__objc_methtype: 0x25
   __TEXT.__objc_stubs: 0x880
-  __DATA_CONST.__got: 0x5e8
+  __DATA_CONST.__got: 0x5f8
   __DATA_CONST.__const: 0x1a48
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x220
-  __AUTH_CONST.__auth_got: 0x1610
+  __AUTH_CONST.__auth_got: 0x1618
   __AUTH_CONST.__const: 0x22e8
   __AUTH_CONST.__cfstring: 0x4320
   __AUTH_CONST.__objc_const: 0x130
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x178
   __DATA.__objc_ivar: 0xc
-  __DATA.__data: 0x1968
-  __DATA.__bss: 0x8c0
-  __DATA_DIRTY.__data: 0x770
-  __DATA_DIRTY.__bss: 0x488
+  __DATA.__data: 0x19c8
+  __DATA.__bss: 0x8a0
+  __DATA_DIRTY.__data: 0x780
+  __DATA_DIRTY.__bss: 0x4a8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1566
-  Symbols:   2627
-  CStrings:  2887
+  Functions: 1573
+  Symbols:   2634
+  CStrings:  2873
 
Symbols:
+ _APSAPACApplyIndependentDecodableDependancy
+ _APSAudioFormatDescriptionListCopyRichestFormat
+ _APSAudioFormatDescriptionListCopyRichestFormatAsFigEndpointStreamAudioFormatDescription
+ _APSAudioFormatGetFullRangeChannelCountFromChannelLayoutTag
+ _APSRingBufferDequeueBytes
+ _APSRingBufferEnqueueBytes
+ _FigCFNumberCreateSInt16
+ _FigSignalErrorAt
+ _kCMSampleAttachmentKey_AudioIndependentSampleDecoderRefreshCount
+ _kCMSampleAttachmentKey_NotSync
+ _kMXSessionNotification_AvailableFormatsDidChange
- _APSRingBufferReadBytes
- _APSRingBufferWriteBytes
- _FigSignalErrorAt3
- _kMXSessionNotification_AvailablePhysicalFormatsDidChange
CStrings:
+ "%!s(MISSING): command string could not be created\n"
+ "APAC audioIndependentSampleDecoderRefreshCount %!@(MISSING), notsync %!@(MISSING)"
+ "APSAPACApplyIndependentDecodableDependancy"
+ "APSAPACSupport"
+ "APSAudioFormatDescriptionListCopyRichestFormat"
+ "APSAudioFormatDescriptionListCopyRichestFormatAsFigEndpointStreamAudioFormatDescription"
+ "APSRingBufferDequeueBytes"
+ "APSRingBufferEnqueueBytes"
+ "EAC3/48000/5.1"
+ "OSStatus APSAPACApplyIndependentDecodableDependancy(CMSampleBufferRef)"
+ "OSStatus APSRingBufferDequeueBytes(APSRingBufferRef, size_t, void *)"
+ "OSStatus APSRingBufferEnqueueBytes(APSRingBufferRef, size_t, const void *)"
+ "Unknown ChannelLayoutTag = %!u(MISSING)\n"
+ "[%!{(MISSING)ptr}] APSLocalAudioCapabilityMonitor initialized"
+ "uint32_t APSAudioFormatGetFullRangeChannelCountFromChannelLayoutTag(AudioChannelLayoutTag)"
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "(Fig)"
- "-108"
- "-877"
- "-878"
- "-879"
- "-880"
- "APSAPAPExtensionLoudnessInfoUtils.c"
- "APSAudioFormatDescription.c"
- "APSAudioFormatDescriptionList.c"
- "APSRingBufferReadBytes"
- "APSRingBufferWriteBytes"
- "APSSharedRingBuffer.c"
- "Could not allocate APSAudioFormatDescription"
- "Could not allocate APSAudioFormatDescriptionList"
- "Failed to create bufferMemObject"
- "Failed to create stateMemObject"
- "OSStatus APSRingBufferReadBytes(APSRingBufferRef, size_t, void *)"
- "OSStatus APSRingBufferWriteBytes(APSRingBufferRef, size_t, const void *)"
- "[%!{(MISSING)ptr}] APSLocalAudioCapabilityMonitor initalized"
- "bufferMemory region maps to NULL"
- "bufferMemorySize is zero"
- "kCMBaseObjectError_AllocationFailed"
- "kParamErr"
- "loudness key missing"
- "sample peak key missing"
- "stateMemObject maps to NULL"
- "stateMemoryLength < sizeof(RingState)"
- "true peak key missing"

```
