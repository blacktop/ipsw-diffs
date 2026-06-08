## mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

-3320.8.1.1.0
-  __TEXT.__text: 0x178
-  __TEXT.__auth_stubs: 0xc0
+3350.58.3.11.1
+  __TEXT.__text: 0x1b0
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x1e
+  __TEXT.__cstring: 0x48
   __TEXT.__oslogstring: 0x22
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x60
+  __DATA_CONST.__cfstring: 0x40
+  __DATA_CONST.__auth_got: 0x68
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__common: 0x10
   - /AppleInternal/Library/Frameworks/CoreMediaTestFoundation.framework/CoreMediaTestFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MediaToolbox.framework/MediaToolbox
+  - /System/Library/Frameworks/Translation.framework/Translation
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 45F9CFFF-073F-32BE-BC87-4561D72260B5
+  UUID: 9890D94E-D575-3F93-92C5-48A7F593ECFE
   Functions: 1
-  Symbols:   15
-  CStrings:  3
+  Symbols:   17
+  CStrings:  7
 
Symbols:
+ ___CFConstantStringClassReference
+ _fig_note_initialize_category_with_default_work_cf
Functions:
~ sub_100000980 -> sub_100000b38 : 376 -> 432
CStrings:
+ "com.apple.coremedia"
+ "mediaplaybackd_trace"

```
