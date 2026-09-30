## mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

-3255.73.1.11.3
-  __TEXT.__text: 0x198
-  __TEXT.__auth_stubs: 0xb0
+3255.77.2.11.2
+  __TEXT.__text: 0x178
+  __TEXT.__auth_stubs: 0xc0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x48
+  __TEXT.__cstring: 0x1e
   __TEXT.__oslogstring: 0x22
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x58
+  __DATA_CONST.__auth_got: 0x60
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__cfstring: 0x40
-  __DATA.__common: 0x10
+  __DATA_CONST.__auth_ptr: 0x8
+  - /AppleInternal/Library/Frameworks/CoreMediaTestFoundation.framework/CoreMediaTestFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/Celestial.framework/Celestial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B7D113AF-AC3E-3D1F-8A67-BB16834BE1D3
+  UUID: F1151CA5-D0DE-30CB-9952-3183E7F95C7B
   Functions: 1
   Symbols:   15
-  CStrings:  7
+  CStrings:  3
 
Symbols:
+ _CoreMediaTestFoundationStartServer
+ _FigDebugIsInternalBuild
- ___CFConstantStringClassReference
- _fig_note_initialize_category_with_default_work_cf
Functions:
~ sub_1000009a0 -> sub_100000980 : 408 -> 376
CStrings:
- "com.apple.coremedia"
- "mediaplaybackd_trace"

```
