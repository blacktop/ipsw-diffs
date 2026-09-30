## StatusKitAgent

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-154.100.1.0.0
-  __TEXT.__text: 0xc8c
+154.200.11.0.0
+  __TEXT.__text: 0xbc0
   __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_stubs: 0x100
+  __TEXT.__objc_stubs: 0xc0
   __TEXT.__const: 0x78
   __TEXT.__cstring: 0xcf
-  __TEXT.__oslogstring: 0x22a
-  __TEXT.__objc_methname: 0xa4
-  __TEXT.__unwind_info: 0xd0
+  __TEXT.__oslogstring: 0x20e
+  __TEXT.__objc_methname: 0x8c
+  __TEXT.__unwind_info: 0xc8
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x140
   __DATA_CONST.__got: 0x30
-  __DATA.__objc_selrefs: 0x40
+  __DATA.__objc_selrefs: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/StatusKitAgentCore.framework/Versions/A/StatusKitAgentCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 27
-  Symbols:   101
-  CStrings:  34
+  Functions: 26
+  Symbols:   98
+  CStrings:  31
 
Symbols:
+ _HandleSignal
+ _objc_alloc_init
- ___HandleSignal_block_invoke
- ____HandleSignal_block_invoke
- _dispatch_async
- _objc_msgSend$sharedInstance
- _objc_msgSend$shutdown
CStrings:
- "Quit - shutting down daemon"
- "sharedInstance"
- "shutdown"
```
