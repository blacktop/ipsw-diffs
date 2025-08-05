## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-309.3.0.0.0
-  __TEXT.__text: 0x9cc4
+309.5.3.1.0
+  __TEXT.__text: 0x9d20
   __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_methlist: 0xefc
+  __TEXT.__objc_methlist: 0xf1c
   __TEXT.__const: 0x90
   __TEXT.__cstring: 0xa00
   __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__oslogstring: 0x36c
-  __TEXT.__unwind_info: 0x308
+  __TEXT.__oslogstring: 0x3b0
+  __TEXT.__unwind_info: 0x304
   __TEXT.__objc_classname: 0x81c
-  __TEXT.__objc_methname: 0x2a5d
+  __TEXT.__objc_methname: 0x2add
   __TEXT.__objc_methtype: 0x8a8
-  __TEXT.__objc_stubs: 0x2060
+  __TEXT.__objc_stubs: 0x20a0
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__const: 0x498
   __DATA_CONST.__objc_classlist: 0x150

   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x5468
-  __DATA_CONST.__objc_selrefs: 0xaa0
+  __DATA_CONST.__objc_selrefs: 0xab8
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__objc_const: 0xdf0
   __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__auth_got: 0x220
   __AUTH.__objc_data: 0xd20
   __DATA.__objc_protorefs: 0x40
-  __DATA.__objc_classrefs: 0x1f0
+  __DATA.__objc_classrefs: 0x1f8
   __DATA.__objc_superrefs: 0x78
   __DATA.__objc_ivar: 0xb4
   __DATA.__data: 0x908

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BEDEDABD-2DF1-324B-B431-16E8C8FFBE93
-  Functions: 347
-  Symbols:   1727
-  CStrings:  804
+  UUID: 75232A9D-DA08-39C9-995A-9FCF984FAEA0
+  Functions: 350
+  Symbols:   1736
+  CStrings:  808
 
Symbols:
+ -[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:]
+ -[CRSUIStatusBarStyleAssertion colorVariant]
+ -[CRSUIStatusBarStyleAssertion initWithInterfaceStyle:]
+ -[CRSUIStatusBarStyleAssertion initWithInterfaceStyle:colorVariant:]
+ -[CRSUIStatusBarStyleAssertion relinquishWithAnimationSettings:]
+ -[CRSUIStatusBarStyleAssertion setColorVariant:]
+ -[CRSUIStatusBarStyleAssertionData colorVariant]
+ -[CRSUIStatusBarStyleAssertionData setColorVariant:]
+ -[CRSUIStatusBarStyleService clientAcquireWithInterfaceStyle:colorVariant:fenceHandle:animationSettings:]
+ -[CRSUIStatusBarStyleService colorVariant]
+ GCC_except_table4
+ GCC_except_table5
+ _OBJC_CLASS_$_UITraitColorVariant
+ _OBJC_IVAR_$_CRSUIStatusBarStyleAssertion._colorVariant
+ _OBJC_IVAR_$_CRSUIStatusBarStyleAssertionData._colorVariant
+ ___105-[CRSUIStatusBarStyleService clientAcquireWithInterfaceStyle:colorVariant:fenceHandle:animationSettings:]_block_invoke
+ ___105-[CRSUIStatusBarStyleService clientAcquireWithInterfaceStyle:colorVariant:fenceHandle:animationSettings:]_block_invoke_2
+ ___86-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:]_block_invoke
+ ___86-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:]_block_invoke.5
+ ___86-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:]_block_invoke.5.cold.1
+ ___86-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:]_block_invoke.6
+ ___86-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:]_block_invoke.6.cold.1
+ ___86-[CRSUIStatusBarStyleAssertion _initWithInterfaceStyle:colorVariant:siriPresentation:]_block_invoke_2
+ ___block_literal_global.177
+ ___block_literal_global.184
+ ___block_literal_global.76
+ _objc_msgSend$_initWithInterfaceStyle:colorVariant:siriPresentation:
+ _objc_msgSend$clientAcquireWithInterfaceStyle:colorVariant:fenceHandle:animationSettings:
+ _objc_msgSend$colorVariant
+ _objc_msgSend$initWithInterfaceStyle:colorVariant:
+ _objc_msgSend$relinquishWithAnimationSettings:
+ _objc_msgSend$setColorVariant:
+ _objc_msgSend$traitCollectionByReplacingNSIntegerValue:forTrait:
+ _objc_msgSend$valueForNSIntegerTrait:
- -[CRSUIStatusBarStyleAssertion contrast]
- -[CRSUIStatusBarStyleAssertion initWithInterfaceStyle:contrast:siriPresentation:]
- -[CRSUIStatusBarStyleAssertion setContrast:]
- -[CRSUIStatusBarStyleAssertionData contrast]
- -[CRSUIStatusBarStyleAssertionData setContrast:]
- -[CRSUIStatusBarStyleService clientAcquireWithInterfaceStyle:contrast:fenceHandle:animationSettings:]
- -[CRSUIStatusBarStyleService contrast]
- GCC_except_table2
- GCC_except_table3
- _OBJC_IVAR_$_CRSUIStatusBarStyleAssertion._contrast
- _OBJC_IVAR_$_CRSUIStatusBarStyleAssertionData._contrast
- ___101-[CRSUIStatusBarStyleService clientAcquireWithInterfaceStyle:contrast:fenceHandle:animationSettings:]_block_invoke
- ___101-[CRSUIStatusBarStyleService clientAcquireWithInterfaceStyle:contrast:fenceHandle:animationSettings:]_block_invoke_2
- ___81-[CRSUIStatusBarStyleAssertion initWithInterfaceStyle:contrast:siriPresentation:]_block_invoke
- ___81-[CRSUIStatusBarStyleAssertion initWithInterfaceStyle:contrast:siriPresentation:]_block_invoke.5
- ___81-[CRSUIStatusBarStyleAssertion initWithInterfaceStyle:contrast:siriPresentation:]_block_invoke.5.cold.1
- ___81-[CRSUIStatusBarStyleAssertion initWithInterfaceStyle:contrast:siriPresentation:]_block_invoke.6
- ___81-[CRSUIStatusBarStyleAssertion initWithInterfaceStyle:contrast:siriPresentation:]_block_invoke.6.cold.1
- ___81-[CRSUIStatusBarStyleAssertion initWithInterfaceStyle:contrast:siriPresentation:]_block_invoke_2
- ___block_literal_global.176
- ___block_literal_global.183
- ___block_literal_global.75
- _objc_msgSend$accessibilityContrast
- _objc_msgSend$clientAcquireWithInterfaceStyle:contrast:fenceHandle:animationSettings:
- _objc_msgSend$contrast
- _objc_msgSend$initWithInterfaceStyle:contrast:siriPresentation:
- _objc_msgSend$setContrast:
- _objc_msgSend$traitCollectionWithAccessibilityContrast:
CStrings:
+ "Acquiring assertion for interface style: %d, color variant: %d"
+ "Received override request! Style: %@, color variant: %@"
+ "Tq,N,V_colorVariant"
+ "_colorVariant"
+ "_initWithInterfaceStyle:colorVariant:siriPresentation:"
+ "clientAcquireWithInterfaceStyle:colorVariant:fenceHandle:animationSettings:"
+ "colorVariant"
+ "initWithInterfaceStyle:"
+ "initWithInterfaceStyle:colorVariant:"
+ "relinquishWithAnimationSettings:"
+ "setColorVariant:"
+ "traitCollectionByReplacingNSIntegerValue:forTrait:"
+ "valueForNSIntegerTrait:"
- "Received override request! Style: %@, contrast: %@"
- "Tq,N,V_contrast"
- "_contrast"
- "accessibilityContrast"
- "clientAcquireWithInterfaceStyle:contrast:fenceHandle:animationSettings:"
- "contrast"
- "initWithInterfaceStyle:contrast:siriPresentation:"
- "setContrast:"
- "traitCollectionWithAccessibilityContrast:"

```
