## mediaplaybackd

> `/usr/libexec/mediaplaybackd`

```diff

-  __TEXT.__text: 0x1b0
-  __TEXT.__auth_stubs: 0xd0
+  __TEXT.__text: 0x178
+  __TEXT.__auth_stubs: 0xc0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x48
+  __TEXT.__cstring: 0x1e
   __TEXT.__oslogstring: 0x22
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x68
+  __DATA_CONST.__auth_got: 0x60
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__cfstring: 0x40
-  __DATA.__common: 0x10
   - /AppleInternal/Library/Frameworks/CoreMediaTestFoundation.framework/CoreMediaTestFoundation
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1
-  Symbols:   17
-  CStrings:  7
+  Symbols:   15
+  CStrings:  3
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
- ___CFConstantStringClassReference
- _fig_note_initialize_category_with_default_work_cf
Functions:
~ sub_100000a68 -> sub_100000980 : 432 -> 376
CStrings:
- "com.apple.coremedia"
- "mediaplaybackd_trace"

```
