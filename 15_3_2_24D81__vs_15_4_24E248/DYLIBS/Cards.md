## Cards

> `/System/Library/PrivateFrameworks/Cards.framework/Versions/A/Cards`

```diff

 3400.20.1.0.0
-  __TEXT.__text: 0xa508
+  __TEXT.__text: 0xa4d0
   __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0xc3c
+  __TEXT.__objc_methlist: 0x145c
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x9f0
   __TEXT.__gcc_except_tab: 0x1e0
   __TEXT.__oslogstring: 0x39e
   __TEXT.__ustring: 0x70
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x318
   __TEXT.__objc_classname: 0x442
-  __TEXT.__objc_methname: 0x2274
-  __TEXT.__objc_methtype: 0x786
+  __TEXT.__objc_methname: 0x22fc
+  __TEXT.__objc_methtype: 0x7c3
   __TEXT.__objc_stubs: 0x1d40
   __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__const: 0x78

   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8f8
+  __DATA_CONST.__objc_selrefs: 0xb90
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x1f0
   __AUTH_CONST.__const: 0x2d0
   __AUTH_CONST.__cfstring: 0xee0
-  __AUTH_CONST.__objc_const: 0x8f00
+  __AUTH_CONST.__objc_const: 0x80d8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x7f8

   - /System/Library/PrivateFrameworks/SearchFoundation.framework/Versions/A/SearchFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8D6AD997-36CB-3603-A7B5-5071162A9664
-  Functions: 265
-  Symbols:   1337
-  CStrings:  867
+  UUID: 50860CF0-CA30-3500-96FF-FBDE30887DF4
+  Functions: 268
+  Symbols:   1341
+  CStrings:  874
 
Symbols:
+ +[CRJSContext sharedContext].cold.1
+ +[CRSFCardLoader sharedLoader].cold.1
+ +[SFCard(CRCard) _interactionsByIntentDataHashes].cold.1
+ CRLogInitIfNeeded.cold.1
Functions:
~ _CRLogInitIfNeeded : 40 -> 44
~ _CRErrorCodeGetName : 124 -> 108
- sub_1cfd42424
~ -[CRBundleManager getBundlesWithCompletion:] : 220 -> 216
~ -[CRBundleManager _getBundlesOnCurrentQueueWithCompletion:] : 1572 -> 1568
~ +[CRCardMocks movieCard] : 3796 -> 3784
~ +[CRCardMocks rosterCard] : 1472 -> 1468
~ -[CRProtocolRestrictedInvocationChain conformsToProtocol:] : 276 -> 268
~ -[CRProtocolRestrictedInvocationChain invocationChain:shouldForwardInvocation:toTarget:] : 96 -> 80
~ +[SFCard(CRCard) _interactionsByIntentDataHashes] : 84 -> 68
~ +[CRSFCardLoader sharedLoader] : 84 -> 68
~ -[CRSFCardLoader loadSFCard:completion:] : 388 -> 384
~ -[CRJSContext initWithVirtualMachine:] : 692 -> 688
~ +[CRJSContext sharedContext] : 84 -> 68
~ -[CRJSContext evaluateScript:completionHandler:] : 768 -> 764
~ __48-[CRJSContext evaluateScript:completionHandler:]_block_invoke.78 : 108 -> 104
~ -[CRJSContext _cardWithTitle:cardSections:interaction:error:] : 1564 -> 1572
+ CRLogInitIfNeeded.cold.1
~ -[CRInvocationChain _forwardInvocation:].cold.1 : 120 -> 136
~ -[CRInvocationChain _forwardInvocation:].cold.2 : 136 -> 120
+ +[SFCard(CRCard) _interactionsByIntentDataHashes].cold.1
CStrings:
+ "@\"NSMutableDictionary\"16@0:8"
+ "T@\"NSMutableDictionary\",&,N"
+ "racFeedbackLoggingContent"
+ "racFeedbackSubfeatureId"
+ "setRacFeedbackLoggingContent:"
+ "setRacFeedbackSubfeatureId:"
+ "v24@0:8@\"NSMutableDictionary\"16"

```
