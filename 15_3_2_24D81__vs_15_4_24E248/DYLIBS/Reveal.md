## Reveal

> `/System/Library/PrivateFrameworks/Reveal.framework/Versions/A/Reveal`

```diff

 52.0.0.0.0
-  __TEXT.__text: 0x5c80
+  __TEXT.__text: 0x5c18
   __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_methlist: 0x3f8
+  __TEXT.__objc_methlist: 0x5d0
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0xe8
+  __TEXT.__gcc_except_tab: 0xf4
   __TEXT.__cstring: 0x161
   __TEXT.__ustring: 0x3c
-  __TEXT.__unwind_info: 0x1d0
+  __TEXT.__unwind_info: 0x1c0
   __TEXT.__objc_classname: 0xb5
   __TEXT.__objc_methname: 0x1bed
   __TEXT.__objc_methtype: 0x630

   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x838
+  __DATA_CONST.__objc_selrefs: 0x900
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x130
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x220
-  __AUTH_CONST.__objc_const: 0xdd0
+  __AUTH_CONST.__objc_const: 0xa60
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x1e0
   __DATA.__objc_ivar: 0x74

   - /System/Library/PrivateFrameworks/TranslationUIServices.framework/Versions/A/TranslationUIServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0860B46C-CAFF-3760-8096-A94F2598E27A
-  Functions: 104
+  UUID: 7F012CEA-F096-34F1-AB16-E589B2A45B8D
+  Functions: 101
   Symbols:   581
   CStrings:  436
 
Functions:
~ -[RVPresentingContext pointerLocationInView] : 56 -> 60
~ -[RVPresentingContext transferIndicator] : 76 -> 60
~ -[RVPresentingContext makeIndicatorWithDelegate:item:] : 412 -> 396
~ ___54-[RVPresentingContext makeIndicatorWithDelegate:item:]_block_invoke : 212 -> 208
~ -[RVPresentingContext preferredEdge] : 124 -> 128
~ -[RVPresenter revealItem:documentContext:presentingContext:options:] : 1976 -> 2000
- sub_1c2c846e4
~ -[RVPresenter menuItemsForItem:documentContext:presentingContext:options:] : 1948 -> 1940
- sub_1c2c8506c
~ +[RVTranslateMenuItem translateTextForItem:] : 424 -> 420
~ -[RVPresenter lookupDataForItem:text:updatedOptions:options:] : 600 -> 596
~ -[RVPresenter animationControllerForItem:documentContext:presentingContext:options:] : 2256 -> 2248
- sub_1c2c86f58
~ -[RVPresenter revealOptionsFromClientOptions:withItem:triggerType:] : 588 -> 584

```
