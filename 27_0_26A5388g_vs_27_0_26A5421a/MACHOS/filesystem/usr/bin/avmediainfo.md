## avmediainfo

> `/usr/bin/avmediainfo`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-2450.71.1.0.0
-  __TEXT.__text: 0x63e4
+2450.77.5.1.0
+  __TEXT.__text: 0x6314
   __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_stubs: 0x14e0
   __TEXT.__objc_methlist: 0x2ec

   __TEXT.__objc_methname: 0xe27
   __TEXT.__objc_classname: 0x1e
   __TEXT.__objc_methtype: 0x169
-  __TEXT.__cstring: 0x1f67
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__cstring: 0x1f09
+  __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__const: 0x80
   __DATA_CONST.__cfstring: 0x2300
   __DATA_CONST.__objc_classlist: 0x10

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 74
+  Functions: 70
   Symbols:   174
-  CStrings:  548
+  CStrings:  543
 
Symbols:
+ _FigSignalErrorAtGM
- _FigSignalErrorAt3
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "-1"
- "FigDebugPlatform.h"
- "FigRunCommandWithArguments"
- "allocation failed"
- "invalid argv"
```
