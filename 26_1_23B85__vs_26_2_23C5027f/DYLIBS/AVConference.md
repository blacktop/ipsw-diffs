## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2175.14.1.1.0
-  __TEXT.__text: 0x7997e4
+2180.2.1.0.0
+  __TEXT.__text: 0x79a07c
   __TEXT.__auth_stubs: 0x5630
-  __TEXT.__objc_methlist: 0x35cb8
+  __TEXT.__objc_methlist: 0x35d00
   __TEXT.__const: 0xc780
-  __TEXT.__cstring: 0x8f98e
-  __TEXT.__oslogstring: 0x10f994
+  __TEXT.__cstring: 0x8f9e1
+  __TEXT.__oslogstring: 0x10fb59
   __TEXT.__gcc_except_tab: 0x2abc
   __TEXT.__ustring: 0x2d4
-  __TEXT.__unwind_info: 0x10910
-  __TEXT.__objc_classname: 0x4eb2
-  __TEXT.__objc_methname: 0x7e10a
-  __TEXT.__objc_methtype: 0x283a6
-  __TEXT.__objc_stubs: 0x4f040
+  __TEXT.__unwind_info: 0x10918
+  __TEXT.__objc_classname: 0x4ed7
+  __TEXT.__objc_methname: 0x7e16d
+  __TEXT.__objc_methtype: 0x283d7
+  __TEXT.__objc_stubs: 0x4f0c0
   __DATA_CONST.__got: 0x1a60
   __DATA_CONST.__const: 0x6b10
-  __DATA_CONST.__objc_classlist: 0x12e8
+  __DATA_CONST.__objc_classlist: 0x12f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16a70
+  __DATA_CONST.__objc_selrefs: 0x16a90
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
   __AUTH_CONST.__auth_got: 0x2b30
   __AUTH_CONST.__const: 0x3ca8
   __AUTH_CONST.__cfstring: 0x265c0
-  __AUTH_CONST.__objc_const: 0x63910
+  __AUTH_CONST.__objc_const: 0x63a30
   __AUTH_CONST.__objc_intobj: 0x4a10
   __AUTH_CONST.__objc_arrayobj: 0x1b48
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH.__objc_data: 0x1590
-  __DATA.__objc_ivar: 0x6cc4
+  __AUTH.__objc_data: 0x15e0
+  __DATA.__objc_ivar: 0x6cd0
   __DATA.__data: 0x78b0
   __DATA.__bss: 0xd78
   __DATA.__common: 0x55

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 69A7D621-F462-3F9C-8317-6EB61C090086
-  Functions: 31644
-  Symbols:   97572
-  CStrings:  57358
+  UUID: F9362BFE-705E-3A42-A1BB-D04FCA4604B5
+  Functions: 31651
+  Symbols:   97606
+  CStrings:  57374
 
Symbols:
+ -[VCAudioInjector loadSamplesFromTrackOutput:audioConverter:audioBuffer:assetReader:]
+ -[VCAudioInjector loadSamplesFromTrackOutput:audioConverter:audioBuffer:assetReader:].cold.1
+ -[VCVirtualAVCaptureDeviceFormat figCaptureSourceVideoFormat]
+ -[VCVirtualFigCaptureSourceVideoFormat dimensions]
+ -[VCVirtualFigCaptureSourceVideoFormat format]
+ -[VCVirtualFigCaptureSourceVideoFormat setDimensions:]
+ -[VCVirtualFigCaptureSourceVideoFormat setFormat:]
+ _OBJC_CLASS_$_VCVirtualFigCaptureSourceVideoFormat
+ _OBJC_IVAR_$_VCVirtualAVCaptureDeviceFormat._figSourceFormat
+ _OBJC_IVAR_$_VCVirtualFigCaptureSourceVideoFormat._dimensions
+ _OBJC_IVAR_$_VCVirtualFigCaptureSourceVideoFormat._format
+ _OBJC_METACLASS_$_VCVirtualFigCaptureSourceVideoFormat
+ __OBJC_$_INSTANCE_METHODS_VCVirtualFigCaptureSourceVideoFormat
+ __OBJC_$_INSTANCE_VARIABLES_VCVirtualFigCaptureSourceVideoFormat
+ __OBJC_$_PROP_LIST_VCVirtualFigCaptureSourceVideoFormat
+ __OBJC_CLASS_RO_$_VCVirtualFigCaptureSourceVideoFormat
+ __OBJC_METACLASS_RO_$_VCVirtualFigCaptureSourceVideoFormat
+ ___35-[VCAudioManager isMicrophoneMuted]_block_invoke
+ _objc_msgSend$loadSamplesFromTrackOutput:audioConverter:audioBuffer:assetReader:
+ _objc_msgSend$setDimensions:
+ _objc_msgSend$setFormat:
+ _objc_msgSend$setupLocalABTestSwitches
+ _objc_msgSend$setupLocalOnOffSwitches
- -[VCAudioInjector loadSamplesFromTrackOutput:audioConverter:audioBuffer:]
- _objc_msgSend$loadSamplesFromTrackOutput:audioConverter:audioBuffer:
CStrings:
+ " [%s] %s:%d %@(%p) Asset reader failed with status=%ld, error=%@"
+ " [%s] %s:%d %@(%p) Fetching kAudioConverterPropertyCalculateOutputBufferSize failed with err=%d"
+ " [%s] %s:%d %@(%p) Skipping call to audio converter - buffer too small; ioBufferSize=%u, neededSamples=%u"
+ " [%s] %s:%d %@(%p) Skipping empty sample buffer"
+ " [%s] %s:%d %@(%p) isFinal=%d, isLocal=%d, isTranslated=%d, streamToken=%ld, formattedText=%s"
+ " [%s] %s:%d %@(%p) setMicrophoneMuted=%d"
+ " [%s] %s:%d Asset reader failed with status=%ld, error=%@"
+ " [%s] %s:%d Fetching kAudioConverterPropertyCalculateOutputBufferSize failed with err=%d"
+ " [%s] %s:%d Skipping call to audio converter - buffer too small; ioBufferSize=%u, neededSamples=%u"
+ " [%s] %s:%d Skipping empty sample buffer"
+ " [%s] %s:%d SwitchManager: A/B testing turned off - using master local switch: %08X"
+ " [%s] %s:%d isFinal=%d, isLocal=%d, isTranslated=%d, streamToken=%ld, formattedText=%s"
+ " [%s] %s:%d setMicrophoneMuted=%d"
+ "-[VCAudioInjector loadSamplesFromTrackOutput:audioConverter:audioBuffer:assetReader:]"
+ "2180.2.1"
+ "@\"VCVirtualFigCaptureSourceVideoFormat\""
+ "TI,N,V_format"
+ "T{?=ii},N,V_dimensions"
+ "VCVirtualFigCaptureSourceVideoFormat"
+ "_dimensions"
+ "_figSourceFormat"
+ "dimensions"
+ "figCaptureSourceVideoFormat"
+ "i48@0:8@16^{OpaqueAudioConverter=}24^{opaqueVCAudioBufferList=}32@40"
+ "loadSamplesFromTrackOutput:audioConverter:audioBuffer:assetReader:"
+ "setDimensions:"
+ "setFormat:"
+ "{VCAudioHALPluginTimestamp=\"numberOfSlots\"Q\"timestamps\"{vector<tagVCAudioHALPluginTimestampInfo, std::allocator<tagVCAudioHALPluginTimestampInfo> >=\"__begin_\"^{tagVCAudioHALPluginTimestampInfo}\"__end_\"^{tagVCAudioHALPluginTimestampInfo}\"\"{?=\"__cap_\"^{tagVCAudioHALPluginTimestampInfo}}}\"timestampIndex\"{atomic<unsigned long>=\"__a_\"{__cxx_atomic_impl<unsigned long, std::__cxx_atomic_base_impl<unsigned long> >=\"__a_value\"AQ}}\"initLocklessTimestampInfo\"{tagVCAudioHALPluginTimestampInfo=\"sampleTime\"d\"hostTime\"Q\"seed\"Q}}"
- " [%s] %s:%d %@(%p) Fetching kAudioConverterPropertyCalculateOutputBufferSize failed with status=%d"
- " [%s] %s:%d %@(%p) isFinal=%d, isLocal=%d, streamToken=%ld, formattedText=%s"
- " [%s] %s:%d %@(%p) setMicrophoneMuted:%d"
- " [%s] %s:%d Fetching kAudioConverterPropertyCalculateOutputBufferSize failed with status=%d"
- " [%s] %s:%d SwitchManager: Non-seed build - using master local switch: %08X"
- " [%s] %s:%d isFinal=%d, isLocal=%d, streamToken=%ld, formattedText=%s"
- " [%s] %s:%d setMicrophoneMuted:%d"
- "2175.14.1.1"
- "TB,N,GisMicrophoneMuted,V_isMicrophoneMuted"
- "i40@0:8@16^{OpaqueAudioConverter=}24^{opaqueVCAudioBufferList=}32"
- "loadSamplesFromTrackOutput:audioConverter:audioBuffer:"
- "{VCAudioHALPluginTimestamp=\"numberOfSlots\"Q\"timestamps\"{vector<tagVCAudioHALPluginTimestampInfo, std::allocator<tagVCAudioHALPluginTimestampInfo> >=\"__begin_\"^{tagVCAudioHALPluginTimestampInfo}\"__end_\"^{tagVCAudioHALPluginTimestampInfo}\"__cap_\"^{tagVCAudioHALPluginTimestampInfo}}\"timestampIndex\"{atomic<unsigned long>=\"__a_\"{__cxx_atomic_impl<unsigned long, std::__cxx_atomic_base_impl<unsigned long> >=\"__a_value\"AQ}}\"initLocklessTimestampInfo\"{tagVCAudioHALPluginTimestampInfo=\"sampleTime\"d\"hostTime\"Q\"seed\"Q}}"

```
