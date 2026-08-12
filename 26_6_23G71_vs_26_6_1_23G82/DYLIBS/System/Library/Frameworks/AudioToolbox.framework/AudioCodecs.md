## AudioCodecs

> `/System/Library/Frameworks/AudioToolbox.framework/AudioCodecs`

```diff

 783.6.5.0.0
-  __TEXT.__text: 0x5f4218
+  __TEXT.__text: 0x5f4258
   __TEXT.__auth_stubs: 0x1740
   __TEXT.__const: 0x335f88
-  __TEXT.__cstring: 0xb590
+  __TEXT.__cstring: 0xb5d8
   __TEXT.__gcc_except_tab: 0x11ac0
   __TEXT.__oslogstring: 0x1a60a
   __TEXT.__ustring: 0x20

   - /usr/lib/libc++.1.dylib
   Functions: 9424
   Symbols:   16776
-  CStrings:  3366
+  CStrings:  3368
 
Functions:
~ __ZN16SBRFrequencyBand17CalculateSBRPatchEhjhPKhjP15PatchParametersPj : 504 -> 516
~ __ZN4apac3obj20ContributionMetadata11DeserializeER16TBitstreamReaderIjEb : 720 -> 724
~ __ZN14SBREncodeFrame14CalculatePatchEP17SBR_CONFIGURATIONP16SBRFrequencyBand : 152 -> 200
CStrings:
+ "CalculatePatch"
+ "patch < 0 || patch >= kMax_SBRNumberOfPatches_Is6 "
```
