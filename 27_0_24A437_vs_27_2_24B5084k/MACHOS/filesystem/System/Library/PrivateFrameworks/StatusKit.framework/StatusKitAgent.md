## StatusKitAgent

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKitAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-154.100.1.0.0
-  __TEXT.__text: 0x6cc
+154.200.11.0.0
+  __TEXT.__text: 0x5e8
   __TEXT.__auth_stubs: 0x250
-  __TEXT.__objc_stubs: 0x100
+  __TEXT.__objc_stubs: 0xc0
   __TEXT.__const: 0x6c
   __TEXT.__cstring: 0x74
-  __TEXT.__oslogstring: 0x89
-  __TEXT.__objc_methname: 0xa4
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__oslogstring: 0x6d
+  __TEXT.__objc_methname: 0x8c
+  __TEXT.__unwind_info: 0x98
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x28
-  __DATA.__objc_selrefs: 0x40
+  __DATA.__objc_selrefs: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 16
-  Symbols:   92
-  CStrings:  19
+  Functions: 14
+  Symbols:   88
+  CStrings:  16
 
Symbols:
+ _HandleSignal
+ _objc_alloc_init
- _OUTLINED_FUNCTION_1
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
