## mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

-3235.8.2.0.0
-  __TEXT.__text: 0x160
-  __TEXT.__auth_stubs: 0xa0
+3235.10.1.0.0
+  __TEXT.__text: 0x198
+  __TEXT.__auth_stubs: 0xb0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x1e
+  __TEXT.__cstring: 0x48
   __TEXT.__oslogstring: 0x22
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x50
+  __DATA_CONST.__auth_got: 0x58
   __DATA_CONST.__got: 0x8
+  __DATA_CONST.__cfstring: 0x40
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 20CEE343-36A3-383B-BD44-4C855845DCF0
+  UUID: 7B44C24A-9E4C-3CBB-941C-E61D079EEA88
   Functions: 1
-  Symbols:   13
-  CStrings:  3
+  Symbols:   15
+  CStrings:  7
 
Symbols:
+ ___CFConstantStringClassReference
+ _fig_note_initialize_category_with_default_work_cf
Functions:
~ sub_1000008b8 -> sub_1000009a0 : 352 -> 408
CStrings:
+ "com.apple.coremedia"
+ "mediaplaybackd_trace"

```
