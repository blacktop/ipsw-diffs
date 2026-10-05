## APFS

> `/System/Library/PrivateFrameworks/APFS.framework/APFS`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3288.40.14.0.0
-  __TEXT.__text: 0x540f4
+3288.40.17.0.0
+  __TEXT.__text: 0x540d4
   __TEXT.__const: 0x8540
   __TEXT.__cstring: 0xe88d
   __TEXT.__oslogstring: 0x11b8

   __AUTH_CONST.__cfstring: 0x13a0
   __AUTH_CONST.__weak_auth_got: 0x8
   __AUTH_CONST.__auth_got: 0x638
-  __AUTH.__data: 0x148
-  __DATA.__data: 0x9c
+  __DATA.__data: 0xc
   __DATA.__common: 0x418
+  __DATA_DIRTY.__data: 0x1d8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
CStrings:
+ "3288.40.17"
- "3288.40.14"
```
