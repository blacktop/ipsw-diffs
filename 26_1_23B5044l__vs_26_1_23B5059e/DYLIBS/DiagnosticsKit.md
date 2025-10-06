## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit`

```diff

-72.40.4.0.0
-  __TEXT.__text: 0x1eba8
+72.40.6.0.0
+  __TEXT.__text: 0x1f080
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0x2ed4
+  __TEXT.__objc_methlist: 0x2f44
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x1a47
-  __TEXT.__oslogstring: 0x17c0
+  __TEXT.__cstring: 0x1a87
+  __TEXT.__oslogstring: 0x1817
   __TEXT.__gcc_except_tab: 0xb14
-  __TEXT.__unwind_info: 0x920
+  __TEXT.__unwind_info: 0x938
   __TEXT.__objc_classname: 0x6c9
-  __TEXT.__objc_methname: 0x5970
-  __TEXT.__objc_methtype: 0x1080
-  __TEXT.__objc_stubs: 0x4540
+  __TEXT.__objc_methname: 0x5a48
+  __TEXT.__objc_methtype: 0x10d5
+  __TEXT.__objc_stubs: 0x45e0
   __DATA_CONST.__got: 0x2d0
   __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1538
+  __DATA_CONST.__objc_selrefs: 0x1560
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x308
-  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__const: 0x420
   __AUTH_CONST.__cfstring: 0xe20
-  __AUTH_CONST.__objc_const: 0x5190
+  __AUTH_CONST.__objc_const: 0x51b0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x78

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 362781CC-0767-3470-8B3E-FA6F2527E2B9
-  Functions: 926
-  Symbols:   3491
-  CStrings:  1661
+  UUID: 737F8177-5358-35B9-837B-5DD7BC16F346
+  Functions: 934
+  Symbols:   3514
+  CStrings:  1671
 
Symbols:
+ -[DKDiagnosticContext setNeedsUpdateResponder]
+ -[DKDiagnosticHostContext setNeedsUpdateResponder]
+ -[DKDiagnosticManager request:presentViewController:completion:responderChainUpdateHandler:]
+ -[DKDiagnosticViewController setNeedsUpdateResponder]
+ GCC_except_table18
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_DKRequestViewControllerDelegate
+ ___39-[DKExtensionRequest beginWithPayload:]_block_invoke.99
+ ___39-[DKExtensionRequest beginWithPayload:]_block_invoke_4
+ ___39-[DKExtensionRequest beginWithPayload:]_block_invoke_5
+ ___48-[DKDiagnosticHostContext cancelWithCompletion:]_block_invoke.106
+ ___50-[DKDiagnosticHostContext setNeedsUpdateResponder]_block_invoke
+ ___50-[DKDiagnosticHostContext setNeedsUpdateResponder]_block_invoke.cold.1
+ ___54-[DKDiagnosticContext _getRemoteProxyAndSetUpHandlers]_block_invoke.149
+ ___55-[DKDiagnosticHostContext startWithPayload:completion:]_block_invoke.102
+ ___80-[DKDiagnosticContext startRemoteDiagnosticWithDiagnosticParameters:completion:]_block_invoke.131
+ ___block_literal_global.105
+ ___block_literal_global.108
+ ___block_literal_global.110
+ ___block_literal_global.147
+ ___block_literal_global.153
+ ___block_literal_global.63
+ ___block_literal_global.76
+ _objc_msgSend$becomeFirstResponder
+ _objc_msgSend$diagnosticManager:presentViewController:completion:responderChainUpdateHandler:
+ _objc_msgSend$request:presentViewController:completion:responderChainUpdateHandler:
+ _objc_msgSend$resignFirstResponder
+ _objc_msgSend$setNeedsUpdateResponder
- GCC_except_table16
- ___39-[DKExtensionRequest beginWithPayload:]_block_invoke.97
- ___48-[DKDiagnosticHostContext cancelWithCompletion:]_block_invoke.105
- ___54-[DKDiagnosticContext _getRemoteProxyAndSetUpHandlers]_block_invoke.147
- ___55-[DKDiagnosticHostContext startWithPayload:completion:]_block_invoke.101
- ___80-[DKDiagnosticContext startRemoteDiagnosticWithDiagnosticParameters:completion:]_block_invoke.130
- ___block_literal_global.104
- ___block_literal_global.107
- ___block_literal_global.145
- ___block_literal_global.149
- ___block_literal_global.74
CStrings:
+ "-[DKDiagnosticHostContext setNeedsUpdateResponder]_block_invoke"
+ "About to call setNeedsUpdateResponder"
+ "DKDiagnosticHostContext::setNeedsUpdateResponder"
+ "becomeFirstResponder"
+ "diagnosticManager:presentViewController:completion:responderChainUpdateHandler:"
+ "request:presentViewController:completion:responderChainUpdateHandler:"
+ "resignFirstResponder"
+ "setNeedsUpdateResponder"
+ "v48@0:8@\"<DKRequest>\"16@\"UIViewController\"24@?<v@?>32@?<v@?>40"
+ "v48@0:8@16@24@?32@?40"

```
