## PassKitUIFoundation

> `/System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation`

```diff

-1642.5.12.3.0
-  __TEXT.__text: 0x29a14
+1642.5.14.3.0
+  __TEXT.__text: 0x29984
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x1ed4
+  __TEXT.__objc_methlist: 0x1ec4
   __TEXT.__const: 0x668
   __TEXT.__cstring: 0xe33
-  __TEXT.__oslogstring: 0x1450
+  __TEXT.__oslogstring: 0x13f3
   __TEXT.__gcc_except_tab: 0x87c
   __TEXT.__unwind_info: 0xb58
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x66f
-  __TEXT.__objc_methname: 0x73a0
+  __TEXT.__objc_methname: 0x7369
   __TEXT.__objc_methtype: 0x14ec
-  __TEXT.__objc_stubs: 0x6080
+  __TEXT.__objc_stubs: 0x6040
   __DATA_CONST.__got: 0x588
   __DATA_CONST.__const: 0xfe0
   __DATA_CONST.__objc_classlist: 0x108

   __AUTH_CONST.__auth_got: 0x650
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__objc_const: 0x4c50
-  __AUTH_CONST.__objc_intobj: 0x3c0
+  __AUTH_CONST.__objc_const: 0x4c20
+  __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH.__objc_data: 0x910
-  __DATA.__objc_ivar: 0x500
+  __DATA.__objc_ivar: 0x4fc
   __DATA.__data: 0x660
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6117C9D6-8127-39D3-A66B-3064EC9A8873
-  Functions: 861
-  Symbols:   3682
-  CStrings:  1961
+  UUID: 8DBB2C7D-8FF1-300F-BC38-1264FCE46E78
+  Functions: 860
+  Symbols:   3677
+  CStrings:  1959
 
Symbols:
+ GCC_except_table178
+ GCC_except_table186
+ GCC_except_table190
+ GCC_except_table198
+ GCC_except_table200
+ ___41+[PKAuthenticator currentStateForPolicy:]_block_invoke.494
+ ___block_literal_global.604
+ ___block_literal_global.619
- -[PKAuthenticatorEvaluationContext shouldIgnorePriorEventsForExternalizedContext]
- GCC_except_table179
- GCC_except_table187
- GCC_except_table191
- GCC_except_table199
- GCC_except_table201
- _OBJC_IVAR_$_PKAuthenticatorEvaluationContext._shouldIgnorePriorEventsForExternalizedContext
- ___41+[PKAuthenticator currentStateForPolicy:]_block_invoke.495
- ___block_literal_global.603
- ___block_literal_global.618
- _objc_msgSend$restartEvaluation
- _objc_msgSend$setShouldIgnorePriorEventsForExternalizedContext:
Functions:
~ -[PKAuthenticatorEvaluationContext initWithRequest:completionHandler:forAuthenticator:] : 1164 -> 1152
~ ___55-[PKAuthenticatorEvaluationContext event:params:reply:]_block_invoke : 384 -> 224
- -[PKAuthenticatorEvaluationContext presentationFlags]
~ -[PKAuthenticator _optionsForEvaluationRequest:withEvaluationContext:] : 1480 -> 1516
CStrings:
- "An externalized context recorded an event when evaluation was paused - restarting evaluation"
- "TB,R,N,V_shouldIgnorePriorEventsForExternalizedContext"

```
