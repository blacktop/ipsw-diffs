## AudioCodecs

> `/System/Library/Components/AudioCodecs.component/Contents/MacOS/AudioCodecs`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

 783.6.5.0.0
-  __TEXT.__text: 0x603ca4
+  __TEXT.__text: 0x603ce8
   __TEXT.__auth_stubs: 0x1750
   __TEXT.__const: 0x32d9e0
-  __TEXT.__cstring: 0xbd8f
+  __TEXT.__cstring: 0xbdcf
   __TEXT.__gcc_except_tab: 0x12ff4
   __TEXT.__oslogstring: 0x1a6bb
   __TEXT.__ustring: 0x20

   - /usr/lib/libc++.1.dylib
   Functions: 9523
   Symbols:   17230
-  CStrings:  3356
+  CStrings:  3358
 
Functions:
~ __ZN14SBREncodeFrame14CalculatePatchEP17SBR_CONFIGURATIONP16SBRFrequencyBand : 152 -> 200
~ __ZN16SBRFrequencyBand17CalculateSBRPatchEhjhPKhjP15PatchParametersPj : 504 -> 516
~ __ZNSt3__110__list_impIN22DynamicRangeCompressor19DRCExtensionPayload8BandInfoENS_9allocatorIS3_EEE5clearEv : 104 -> 108
~ __ZN4apac3obj20ContributionMetadata11DeserializeER16TBitstreamReaderIjEb : 720 -> 724
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/AACEncoderFactory.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACEnhancedLowDelaySBREncoder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACHighEfficiencyEncoder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACHighEfficiencyV2Encoder.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncode.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeChannel.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeFrame.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeFrame.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEldEncoderChannel.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncode.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncodeChannel.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncodeFrame.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/aacencifc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/aux_func.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_aac.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_enc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_fram.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_pam.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/cm_utils.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/cod_chan.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/fifo_buf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/intensity.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/ms_chan.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/ms_stereo.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pam.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pam_loopmain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/paminit.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pns_tool.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/prconfig.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psy_chan.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psy_conf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psymain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psyout.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psyparam.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/scaling.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/sw_cont.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/thr_chan.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/tns_enc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/toolmain.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/Speex/libspeex/ltp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.OQThps/Sources/AudioCodecs/Source/Codecs/Speex/libspeex/nb_celp.c"
+ "20:50:29"
+ "CalculatePatch"
+ "Jul 31 2026"
+ "patch < 0 || patch >= kMax_SBRNumberOfPatches_Is6 "
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/AACEncoderFactory.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACEnhancedLowDelaySBREncoder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACHighEfficiencyEncoder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/AACHighEfficiencyV2Encoder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncode.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeChannel.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeFrame.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/psEncodeFrame.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEldEncoderChannel.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncode.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncodeChannel.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/HEAACEncoder/sbrEncodeFrame.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/aacencifc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/aux_func.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_aac.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_enc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_fram.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/bit_pam.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/cm_utils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/cod_chan.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/fifo_buf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/intensity.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/ms_chan.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/ms_stereo.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pam.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pam_loopmain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/paminit.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/pns_tool.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/prconfig.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psy_chan.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psy_conf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psymain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psyout.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/psyparam.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/scaling.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/sw_cont.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/thr_chan.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/tns_enc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/MPEG4/AACEncoder/toolmain.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/Speex/libspeex/ltp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.opAA8J/Sources/AudioCodecs/Source/Codecs/Speex/libspeex/nb_celp.c"
- "17:15:56"
- "Jul 11 2026"
```
