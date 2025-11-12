## PassKitUIFoundation

> `/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation`

```diff

-1642.3.2.0.0
-  __TEXT.__text: 0x28750
+1642.3.3.0.0
+  __TEXT.__text: 0x28864
   __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__objc_methlist: 0x1ebc
+  __TEXT.__objc_methlist: 0x1ee4
   __TEXT.__const: 0x668
   __TEXT.__cstring: 0xe31
-  __TEXT.__oslogstring: 0x13f3
+  __TEXT.__oslogstring: 0x1450
   __TEXT.__gcc_except_tab: 0x870
   __TEXT.__unwind_info: 0xaf0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x66f
-  __TEXT.__objc_methname: 0x7083
+  __TEXT.__objc_methname: 0x717e
   __TEXT.__objc_methtype: 0x14ec
-  __TEXT.__objc_stubs: 0x5de0
+  __TEXT.__objc_stubs: 0x5e40
   __DATA_CONST.__got: 0x568
   __DATA_CONST.__const: 0xf90
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c68
+  __DATA_CONST.__objc_selrefs: 0x1c78
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x668
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x4bd0
+  __AUTH_CONST.__objc_const: 0x4c30
   __AUTH_CONST.__objc_intobj: 0x3c0
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x4f4
+  __DATA.__objc_ivar: 0x4fc
   __DATA.__data: 0x660
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F11041CB-1EC2-30CC-B05F-8F4C210F9D96
-  Functions: 850
-  Symbols:   3633
-  CStrings:  1937
+  UUID: 8371A7DA-9132-37A1-9C6D-258E023BED01
+  Functions: 853
+  Symbols:   3644
+  CStrings:  1943
 
Symbols:
+ -[PKAuthenticatorEvaluationContext shouldIgnorePriorEventsForExternalizedContext]
+ -[PKAuthenticatorEvaluationRequest setShouldIgnorePriorEventsForExternalizedContext:]
+ -[PKAuthenticatorEvaluationRequest shouldIgnorePriorEventsForExternalizedContext]
+ GCC_except_table106
+ GCC_except_table179
+ GCC_except_table187
+ GCC_except_table191
+ GCC_except_table199
+ GCC_except_table201
+ GCC_except_table59
+ GCC_except_table71
+ GCC_except_table78
+ GCC_except_table92
+ GCC_except_table93
+ _OBJC_IVAR_$_PKAuthenticatorEvaluationContext._shouldIgnorePriorEventsForExternalizedContext
+ _OBJC_IVAR_$_PKAuthenticatorEvaluationRequest._shouldIgnorePriorEventsForExternalizedContext
+ ___41+[PKAuthenticator currentStateForPolicy:]_block_invoke.495
+ ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.252
+ ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.253
+ ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.254
+ ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.255
+ ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke.261
+ ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_2.262
+ ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_3.263
+ ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_4.266
+ ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke.274
+ ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke_2.275
+ ___block_literal_global.273
+ ___block_literal_global.277
+ ___block_literal_global.331
+ ___block_literal_global.333
+ ___block_literal_global.603
+ ___block_literal_global.618
+ _objc_msgSend$restartEvaluation
+ _objc_msgSend$setShouldIgnorePriorEventsForExternalizedContext:
+ _objc_msgSend$shouldIgnorePriorEventsForExternalizedContext
- GCC_except_table104
- GCC_except_table176
- GCC_except_table184
- GCC_except_table188
- GCC_except_table196
- GCC_except_table198
- GCC_except_table57
- GCC_except_table67
- GCC_except_table90
- GCC_except_table91
- GCC_except_table97
- ___41+[PKAuthenticator currentStateForPolicy:]_block_invoke.489
- ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.247
- ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.248
- ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.249
- ___57-[PKAuthenticatorEvaluationContext invalidateWithIntent:]_block_invoke.250
- ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke.256
- ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_2.257
- ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_3.258
- ___67-[PKAuthenticatorEvaluationContext evaluateWithOptions:completion:]_block_invoke_4.261
- ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke.269
- ___79-[PKAuthenticatorEvaluationContext _presentAuthenticatorViewOfType:withParams:]_block_invoke_2.270
- ___block_literal_global.268
- ___block_literal_global.272
- ___block_literal_global.326
- ___block_literal_global.328
- ___block_literal_global.597
- ___block_literal_global.612
CStrings:
+ "An externalized context recorded an event when evaluation was paused - restarting evaluation"
+ "TB,N,V_shouldIgnorePriorEventsForExternalizedContext"
+ "TB,R,N,V_shouldIgnorePriorEventsForExternalizedContext"
+ "_shouldIgnorePriorEventsForExternalizedContext"
+ "setShouldIgnorePriorEventsForExternalizedContext:"
+ "shouldIgnorePriorEventsForExternalizedContext"

```
