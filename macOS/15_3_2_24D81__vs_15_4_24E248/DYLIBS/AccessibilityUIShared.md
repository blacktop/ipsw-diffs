## AccessibilityUIShared

> `/System/iOSSupport/System/Library/PrivateFrameworks/AccessibilityUIShared.framework/Versions/A/AccessibilityUIShared`

```diff

-3148.7.15.0.0
-  __TEXT.__text: 0x3274
+3148.15.11.1.0
+  __TEXT.__text: 0x3284
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x318
+  __TEXT.__objc_methlist: 0x434
   __TEXT.__cstring: 0x49a
   __TEXT.__const: 0x30
   __TEXT.__oslogstring: 0x225

   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e0
+  __DATA_CONST.__objc_selrefs: 0x378
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x2a0
-  __AUTH_CONST.__objc_const: 0x9e8
+  __AUTH_CONST.__objc_const: 0x7d8
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x110

   - /System/Library/PrivateFrameworks/BoardServices.framework/Versions/A/BoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4AF53ECB-F5A9-324D-9A86-3651210AC929
-  Functions: 95
-  Symbols:   392
+  UUID: 19EDB7E1-A134-3DAD-8DE6-B937AA5E2590
+  Functions: 96
+  Symbols:   393
   CStrings:  286
 
Symbols:
+ AXUIServiceManagerLaunchAngelInterface.cold.1
Functions:
~ _AXUIServiceManagerLaunchAngelInterface : 84 -> 68
~ +[AXUIMessageReplyHandler createReplyObject:fromMessage:withError:] : 456 -> 448
~ -[AXUIMessageSender delegate] : 264 -> 260
~ -[AXUIMessageSender setDelegate:] : 152 -> 148
~ -[AXUIMessageSender sendAsynchronousMessage:withIdentifier:context:targetAccessQueue:completionRequiresWritingBlock:completion:timeout:] : 740 -> 744
~ __61-[AXUIMessageSendHandler _sendMessage:context:previousError:]_block_invoke.6 : 312 -> 336
+ AXUIServiceManagerLaunchAngelInterface.cold.1
~ -[AXUIMessageSender sendAsynchronousMessage:withIdentifier:context:targetAccessQueue:completionRequiresWritingBlock:completion:timeout:].cold.1 : 116 -> 68
~ -[AXUIMessageSender sendAsynchronousMessage:withIdentifier:context:targetAccessQueue:completionRequiresWritingBlock:completion:timeout:].cold.2 : 68 -> 116

```
