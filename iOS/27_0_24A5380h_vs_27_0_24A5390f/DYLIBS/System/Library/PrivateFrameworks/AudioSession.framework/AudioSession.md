## AudioSession

> `/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-449.102.0.0.0
-  __TEXT.__text: 0x4dd58
+449.105.0.0.0
+  __TEXT.__text: 0x4e010
   __TEXT.__realtime: 0x178
   __TEXT.__objc_methlist: 0x2364
-  __TEXT.__gcc_except_tab: 0x8e5c
-  __TEXT.__cstring: 0x39bf
+  __TEXT.__gcc_except_tab: 0x8e70
+  __TEXT.__cstring: 0x39df
   __TEXT.__const: 0x21f
-  __TEXT.__oslogstring: 0x472e
+  __TEXT.__oslogstring: 0x47f4
   __TEXT.__unwind_info: 0x2f08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0xb70
   __AUTH_CONST.__const: 0x1be0
-  __AUTH_CONST.__cfstring: 0x2440
+  __AUTH_CONST.__cfstring: 0x2480
   __AUTH_CONST.__objc_const: 0x2b40
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x180

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1739
-  Symbols:   3758
-  CStrings:  744
+  Symbols:   3759
+  CStrings:  750
 
Symbols:
+ _sysctlbyname
Functions:
~ +[AVAudioApplication(SPI) appleTVSupportsEnhanceDialogue] : 220 -> 440
~ +[AVAudioApplication(SPI) iosDeviceSupportsEnhanceDialogue] : 64 -> 292
~ +[AVAudioApplication(SPI) visionosDeviceSupportsEnhanceDialogue] : 32 -> 280
CStrings:
+ "%25s:%-5d EnhanceDialogue: appleTVSupportsEnhanceDialogue = %@"
+ "%25s:%-5d EnhanceDialogue: iosDeviceSupportsEnhanceDialogue = %@"
+ "%25s:%-5d EnhanceDialogue: visionosDeviceSupportsEnhanceDialogue = %@"
+ "NO"
+ "YES"
+ "hw.optional.arm.FEAT_SME"
```
