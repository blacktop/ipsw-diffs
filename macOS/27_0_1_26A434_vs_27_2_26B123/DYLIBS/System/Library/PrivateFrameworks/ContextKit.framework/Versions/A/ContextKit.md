## ContextKit

> `/System/Library/PrivateFrameworks/ContextKit.framework/Versions/A/ContextKit`

```diff

-307.0.0.0.0
-  __TEXT.__text: 0xff40
-  __TEXT.__objc_methlist: 0x1024
-  __TEXT.__const: 0xa8
+308.0.0.0.0
+  __TEXT.__text: 0x10140
+  __TEXT.__objc_methlist: 0x102c
+  __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x900
   __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__oslogstring: 0x903
-  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__oslogstring: 0x96f
+  __TEXT.__unwind_info: 0x4c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xba8
+  __DATA_CONST.__objc_selrefs: 0xbb0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x170

   __AUTH.__objc_data: 0xa0
   __DATA.__objc_ivar: 0x1a4
   __DATA.__data: 0x240
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x188
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/ContextKitCore.framework/Versions/A/ContextKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 481
-  Symbols:   1113
-  CStrings:  201
+  Functions: 483
+  Symbols:   1119
+  CStrings:  202
 
Symbols:
+ +[CKContextXPCClient resetConnectionFailureTrackingForTesting]
+ _clock_gettime_nsec_np
+ _kConnectionFailureRunStartNs
+ _kConsecutiveConnectionFailures
+ _kFailFastUntilNs
+ _kLastConnectionFailureNs
Functions:
~ __27-[CKContextRequest execute]_block_invoke.142 : 360 -> 376
~ __38-[CKContextRequest _executeWithReply:]_block_invoke.157 : 300 -> 348
~ +[CKContextXPCClient isXPCConnectionError:] : 272 -> 552
+ +[CKContextXPCClient resetConnectionFailureTrackingForTesting]
~ +[CKContextXPCClient initialize].cold.1 : 72 -> 68
~ +[CKContextXPCClient isXPCConnectionError:].cold.1 : 72 -> 80
~ +[CKContextXPCClient isXPCConnectionError:].cold.2 : 72 -> 68
+ +[CKContextXPCClient isXPCConnectionError:].cold.3
CStrings:
+ "ContextService is not accepting connections; failing fast without retry: %@"
+ "XPC connection unusable after %lu consecutive failures, establishing new connection: %@"
- "XPC connection invalid, establishing new connection: %@"
```
