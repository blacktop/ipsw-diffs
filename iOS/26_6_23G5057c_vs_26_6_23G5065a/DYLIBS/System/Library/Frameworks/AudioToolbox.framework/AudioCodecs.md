## AudioCodecs

> `/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x5f4208
+  __TEXT.__text: 0x5f4218
   __TEXT.__auth_stubs: 0x1740
   __TEXT.__const: 0x335f88
   __TEXT.__cstring: 0xb590
Functions:
~ __ZN23SBRIndividChannelStream13ResetSbrSliceERK9SBRHeaderR7SBRInfoR16SBRFrequencyBandR15SBRFreqBandDatabb : 360 -> 368
~ __ZN23SBRIndividChannelStream28ApplySpectralBandReplicationER9SBRHeaderR7SBRInfoR15SBRFreqBandData : 476 -> 480
~ __ZN16PSChannelElement14DecodeSbrSliceEPPKf : 10340 -> 10344
CStrings:
+ "22:56:43"
+ "Jul  7 2026"
- "16:27:36"
- "Jun 26 2026"
```
