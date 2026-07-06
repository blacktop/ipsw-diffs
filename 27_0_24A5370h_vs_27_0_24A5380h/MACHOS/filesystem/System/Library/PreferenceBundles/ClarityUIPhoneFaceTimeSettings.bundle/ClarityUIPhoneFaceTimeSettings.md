## ClarityUIPhoneFaceTimeSettings

> `/System/Library/PreferenceBundles/ClarityUIPhoneFaceTimeSettings.bundle/ClarityUIPhoneFaceTimeSettings`

```diff

-  __TEXT.__text: 0x2ed4
-  __TEXT.__auth_stubs: 0x270
-  __TEXT.__objc_stubs: 0xee0
-  __TEXT.__objc_methlist: 0x59c
+  __TEXT.__text: 0x300c
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_stubs: 0xf40
+  __TEXT.__objc_methlist: 0x5a4
   __TEXT.__const: 0x28
-  __TEXT.__objc_methname: 0x13ad
+  __TEXT.__gcc_except_tab: 0x20
+  __TEXT.__objc_methname: 0x1422
   __TEXT.__cstring: 0x28f
   __TEXT.__objc_classname: 0x97
   __TEXT.__objc_methtype: 0x363
   __TEXT.__oslogstring: 0x33a
-  __TEXT.__unwind_info: 0x108
-  __DATA_CONST.__const: 0xb0
+  __TEXT.__unwind_info: 0x128
+  __DATA_CONST.__const: 0xd8
   __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA_CONST.__auth_got: 0x140
-  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0x130
   __DATA.__objc_const: 0x620
-  __DATA.__objc_selrefs: 0x598
+  __DATA.__objc_selrefs: 0x5b0
   __DATA.__objc_ivar: 0x28
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 86
-  Symbols:   341
-  CStrings:  322
+  Functions: 88
+  Symbols:   354
+  CStrings:  325
 
Sections:
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[CLPHController _didUpdateOutgoingCommunicationLimit]
+ GCC_except_table23
+ __Unwind_Resume
+ ___29-[CLPHController viewDidLoad]_block_invoke
+ ___block_descriptor_40_e8_32w_e5_v8?0lw32l8
+ ___objc_personality_v0
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_didUpdateOutgoingCommunicationLimit
+ _objc_msgSend$registerUpdateBlock:forRetrieveSelector:withListener:
+ _objc_msgSend$reloadSpecifier:animated:
Functions:
~ -[CLPHController viewDidLoad] : 184 -> 376
+ ___29-[CLPHController viewDidLoad]_block_invoke
+ -[CLPHController _didUpdateOutgoingCommunicationLimit]
~ -[AXCLFCommunicationLimitController tableView:didSelectRowAtIndexPath:] : 476 -> 468
~ -[AXCLFCommunicationLimitController _updateForOutgoingCommunicationLimit] : 292 -> 352
CStrings:
+ "_didUpdateOutgoingCommunicationLimit"
+ "registerUpdateBlock:forRetrieveSelector:withListener:"
+ "reloadSpecifier:animated:"

```
