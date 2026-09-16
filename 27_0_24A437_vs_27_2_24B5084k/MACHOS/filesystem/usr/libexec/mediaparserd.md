## mediaparserd

> `/usr/libexec/mediaparserd`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`

```diff

-3350.77.1.6.0
-  __TEXT.__text: 0x160
-  __TEXT.__auth_stubs: 0xa0
+3385.7.1.0.0
+  __TEXT.__text: 0x198
+  __TEXT.__auth_stubs: 0xb0
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0x1c
+  __TEXT.__cstring: 0x44
   __TEXT.__oslogstring: 0x3f
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x50
+  __DATA_CONST.__cfstring: 0x40
+  __DATA_CONST.__auth_got: 0x58
   __DATA_CONST.__got: 0x8
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 1
-  Symbols:   13
-  CStrings:  3
+  Symbols:   15
+  CStrings:  5
 
Symbols:
+ ___CFConstantStringClassReference
+ _fig_note_initialize_category_with_default_work_cf
Functions:
~ sub_1000008b8 -> sub_1000009a0 : 352 -> 408
CStrings:
+ "com.apple.coremedia"
+ "mediaparserd_trace"
```
