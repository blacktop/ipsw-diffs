## AudioCodecs

> `System/Library/Components/AudioCodecs.component/Contents/MacOS/AudioCodecs`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-783.6.5.0.0
-  __TEXT.__text: 0x603ce8
+783.7.3.0.0
+  __TEXT.__text: 0x603c04
   __TEXT.__auth_stubs: 0x1750
   __TEXT.__const: 0x32d9e0
   __TEXT.__cstring: 0xbdcf
-  __TEXT.__gcc_except_tab: 0x12ff4
+  __TEXT.__gcc_except_tab: 0x12ff8
   __TEXT.__oslogstring: 0x1a6bb
   __TEXT.__ustring: 0x20
   __TEXT.__unwind_info: 0x96b0
Symbols:
+ __ZNK13ACOpusDecoder29IsDiscreteChannelsPacketValidEPKhj
- __ZNK13ACOpusDecoder18IsInputPacketValidEPKhj
Functions:
~ __ZN13ACOpusDecoder21SetCurrentInputFormatERK27AudioStreamBasicDescription : 296 -> 320
~ __ZN13ACOpusDecoder23ProduceOutputBufferListEP15AudioBufferListRjP28AudioStreamPacketDescription : 2068 -> 2064
~ __ZNK13ACOpusDecoder18IsInputPacketValidEPKhj -> __ZNK13ACOpusDecoder29IsDiscreteChannelsPacketValidEPKhj : 212 -> 224
~ __ZN13ACOpusDecoder15AppendInputDataEPKvRjS2_PK28AudioStreamPacketDescription : 608 -> 664
~ __ZN13ACOpusDecoder10InitializeEPK27AudioStreamBasicDescriptionS2_PKvj : 3200 -> 2876
~ __ZN14InstanceConfig6CreateERK18DecoderConfigDescrPPK19OpaqueFigCPECryptor : 1812 -> 1820
```
