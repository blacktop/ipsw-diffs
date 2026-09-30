## ContextKit

> `/System/Library/PrivateFrameworks/ContextKit.framework/ContextKit`

```diff

-307.0.0.0.0
-  __TEXT.__text: 0xf01c
-  __TEXT.__objc_methlist: 0x104c
-  __TEXT.__const: 0xa8
+308.0.0.0.0
+  __TEXT.__text: 0xf1fc
+  __TEXT.__objc_methlist: 0x1054
+  __TEXT.__const: 0xb0
   __TEXT.__cstring: 0x9c3
   __TEXT.__gcc_except_tab: 0x310
-  __TEXT.__oslogstring: 0x937
-  __TEXT.__unwind_info: 0x658
+  __TEXT.__oslogstring: 0x9a3
+  __TEXT.__unwind_info: 0x660
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbe0
+  __DATA_CONST.__objc_selrefs: 0xbe8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__got: 0x180

   - /System/Library/PrivateFrameworks/ContextKitCore.framework/ContextKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 465
-  Symbols:   1124
-  CStrings:  208
+  Functions: 467
+  Symbols:   1130
+  CStrings:  209
 
Symbols:
+ +[CKContextXPCClient resetConnectionFailureTrackingForTesting]
+ _clock_gettime_nsec_np
+ _kConnectionFailureRunStartNs
+ _kConsecutiveConnectionFailures
+ _kFailFastUntilNs
+ _kLastConnectionFailureNs
Functions:
~ ___27-[CKContextRequest execute]_block_invoke.201 : 340 -> 356
~ ___38-[CKContextRequest _executeWithReply:]_block_invoke.210 : 284 -> 324
~ +[CKContextXPCClient isXPCConnectionError:] : 248 -> 516
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
