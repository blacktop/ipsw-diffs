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
-  CStrings:  3355
+  CStrings:  3357
 
Functions:
~ __ZN14SBREncodeFrame14CalculatePatchEP17SBR_CONFIGURATIONP16SBRFrequencyBand : 152 -> 200
~ __ZN16SBRFrequencyBand17CalculateSBRPatchEhjhPKhjP15PatchParametersPj : 504 -> 516
~ __ZNSt3__110__list_impIN22DynamicRangeCompressor19DRCExtensionPayload8BandInfoENS_9allocatorIS3_EEE5clearEv : 104 -> 108
~ __ZN4apac3obj20ContributionMetadata11DeserializeER16TBitstreamReaderIjEb : 720 -> 724
CStrings:
+ "CalculatePatch"
+ "patch < 0 || patch >= kMax_SBRNumberOfPatches_Is6 "
```
