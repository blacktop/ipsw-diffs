## WebUI

> `/System/Library/PrivateFrameworks/WebUI.framework/WebUI`

```diff

-617.2.4.10.8
-  __TEXT.__text: 0xf980
+618.1.15.10.11
+  __TEXT.__text: 0xfa00
   __TEXT.__auth_stubs: 0x5b0
-  __TEXT.__objc_methlist: 0xb2c
+  __TEXT.__objc_methlist: 0xb44
   __TEXT.__const: 0x28
   __TEXT.__gcc_except_tab: 0x3fc
   __TEXT.__cstring: 0xc29

   __TEXT.__ustring: 0x746
   __TEXT.__unwind_info: 0x468
   __TEXT.__objc_classname: 0x241
-  __TEXT.__objc_methname: 0x5cc6
-  __TEXT.__objc_methtype: 0x108c
-  __TEXT.__objc_stubs: 0x3520
+  __TEXT.__objc_methname: 0x5db0
+  __TEXT.__objc_methtype: 0x1095
+  __TEXT.__objc_stubs: 0x3540
   __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0xa10
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1bf8
-  __DATA_CONST.__objc_selrefs: 0xff8
+  __DATA_CONST.__objc_const: 0x1c28
+  __DATA_CONST.__objc_selrefs: 0x1010
+  __DATA_CONST.__objc_classrefs: 0x258
+  __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__cfstring: 0xac0

   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__auth_got: 0x2e8
-  __DATA.__objc_classrefs: 0x258
-  __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0xdc
+  __DATA.__objc_ivar: 0xe0
   __DATA.__data: 0x370
   __DATA.__bss: 0x88
   __DATA_DIRTY.__const: 0x160

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 329
-  Symbols:   1634
-  CStrings:  1026
+  Functions: 331
+  Symbols:   1640
+  CStrings:  1033
 
Symbols:
+ -[WBUFormDataController previouslyFilledVirtualCardNumbers]
+ -[WBUFormDataController setPreviouslyFilledVirtualCardNumbers:]
+ _OBJC_IVAR_$_WBUFormDataController._previouslyFilledVirtualCardNumbers
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80bs_e8_v12?0B8ls32l8s40l8s48l8s80l8s56l8s64l8s72l8
+ ___block_literal_global.527
+ _objc_msgSend$ancestorFrameURLs
+ _objc_msgSend$isVirtualCard:previouslyFilledVirtualCardNumbers:completion:
+ _objc_msgSend$sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledVirtualCardData:
+ _objc_msgSend$tellWalletThatExistingCardWasFilledInForm:previouslyFilledVirtualCardNumbers:
- ___block_descriptor_97_e8_32s40s48s56s64s72s80s88bs_e8_v12?0B8ls32l8s40l8s48l8s88l8s56l8s64l8s72l8s80l8
- ___block_literal_global.520
- _objc_msgSend$isVirtualCard:lastFilledCardData:completion:
- _objc_msgSend$sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledCardData:
- _objc_msgSend$tellWalletThatExistingCardWasFilledInForm:lastFilledCardData:
CStrings:
+ "\x12\x13"
+ "@\"NSSet\""
+ "T@\"NSSet\",&,N,V_previouslyFilledVirtualCardNumbers"
+ "T@\"NSString\",?,R,C"
+ "_previouslyFilledVirtualCardNumbers"
+ "ancestorFrameURLs"
+ "isVirtualCard:previouslyFilledVirtualCardNumbers:completion:"
+ "previouslyFilledVirtualCardNumbers"
+ "sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledVirtualCardData:"
+ "setPreviouslyFilledVirtualCardNumbers:"
+ "tellWalletThatExistingCardWasFilledInForm:previouslyFilledVirtualCardNumbers:"
- "\x12\x12"
- "isVirtualCard:lastFilledCardData:completion:"
- "sendCardholderNameEnteredInFormToWalletIfNecessary:lastFilledCardData:"
- "tellWalletThatExistingCardWasFilledInForm:lastFilledCardData:"

```
