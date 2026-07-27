## avmediainfo

> `/usr/bin/avmediainfo`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-2430.10.1.0.0
-  __TEXT.__text: 0x6370
+2430.13.1.0.0
+  __TEXT.__text: 0x62a0
   __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_stubs: 0x14e0
   __TEXT.__objc_methlist: 0x2ec

   __TEXT.__objc_methname: 0xe27
   __TEXT.__objc_classname: 0x1e
   __TEXT.__objc_methtype: 0x169
-  __TEXT.__cstring: 0x1f4a
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__cstring: 0x1eec
+  __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__auth_got: 0x210
   __DATA_CONST.__got: 0x320
   __DATA_CONST.__const: 0x80

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 74
+  Functions: 70
   Symbols:   173
-  CStrings:  547
+  CStrings:  542
 
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
