## videocodecd

> `/usr/libexec/videocodecd`

```diff

-  __TEXT.__text: 0x34c
+  __TEXT.__text: 0x1ac
   __TEXT.__auth_stubs: 0x110
-  __TEXT.__const: 0x10
+  __TEXT.__const: 0x8
   __TEXT.__cstring: 0x46
-  __TEXT.__oslogstring: 0xcc
+  __TEXT.__oslogstring: 0x33
   __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__cfstring: 0x40
-  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   Functions: 1
   Symbols:   21
-  CStrings:  9
+  CStrings:  7
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__cfstring : content changed
Functions:
~ sub_1000009f8 -> sub_100000960 : 844 -> 428
CStrings:
- "<<<< videocodecd >>>> %s: Failed to elevate inactive jetsam priority, error: %d"
- "<<<< videocodecd >>>> %s: Succeeded to elevate inactive jetsam priority."

```
