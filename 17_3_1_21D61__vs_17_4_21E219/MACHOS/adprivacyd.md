## adprivacyd

> `/usr/libexec/adprivacyd`

```diff

-608.0.0.0.0
+618.0.0.0.0
   __TEXT.__text: 0x46c
   __TEXT.__auth_stubs: 0x160
   __TEXT.__objc_stubs: 0x140

   __DATA_CONST.__const: 0x60
   __DATA_CONST.__cfstring: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x40
   __DATA_CONST.__linkguard: 0x1e
   __DATA.__objc_selrefs: 0x50
-  __DATA.__objc_classrefs: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AdCore.framework/AdCore

```
