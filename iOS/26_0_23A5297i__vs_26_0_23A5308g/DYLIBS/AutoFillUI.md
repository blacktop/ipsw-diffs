## AutoFillUI

> `/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI`

```diff

-86.0.0.0.0
-  __TEXT.__text: 0x20a80
+87.0.0.0.0
+  __TEXT.__text: 0x20cf8
   __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_methlist: 0x3590
+  __TEXT.__objc_methlist: 0x35a8
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x18ff
+  __TEXT.__cstring: 0x1924
   __TEXT.__gcc_except_tab: 0x704
   __TEXT.__ustring: 0xe6
   __TEXT.__dlopen_cstrs: 0x14e
   __TEXT.__oslogstring: 0x3
-  __TEXT.__unwind_info: 0x880
+  __TEXT.__unwind_info: 0x888
   __TEXT.__objc_classname: 0x554
-  __TEXT.__objc_methname: 0x9ddb
+  __TEXT.__objc_methname: 0x9e4c
   __TEXT.__objc_methtype: 0x2ec9
-  __TEXT.__objc_stubs: 0x5d60
+  __TEXT.__objc_stubs: 0x5da0
   __DATA_CONST.__got: 0x5f0
   __DATA_CONST.__const: 0x9a0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2618
+  __DATA_CONST.__objc_selrefs: 0x2630
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0xc8
   __AUTH_CONST.__auth_got: 0x350
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0x1700
+  __AUTH_CONST.__cfstring: 0x1740
   __AUTH_CONST.__objc_const: 0x6c30
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x18

   - /System/Library/PrivateFrameworks/WebKitLegacy.framework/WebKitLegacy
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 42927A1F-0466-3E77-A077-781A24CA536F
-  Functions: 818
-  Symbols:   3453
-  CStrings:  2319
+  UUID: 8B47B5A1-C65B-37B2-9492-9F4C28AC4F01
+  Functions: 820
+  Symbols:   3459
+  CStrings:  2326
 
Symbols:
+ -[AFUICreditCardViewController viewDidDisappear:]
+ -[AFUIServiceDelegate _setIsModalUIPresented:forSessionUUID:]
+ GCC_except_table36
+ ___block_literal_global.321
+ ___block_literal_global.330
+ _objc_msgSend$_setIsModalUIPresented:forSessionUUID:
+ _objc_msgSend$creditCardsUIDidEndForSessionUUID:completion:
- GCC_except_table35
- ___block_literal_global.315
- ___block_literal_global.324
Functions:
~ -[AFUIPasswordsController passwordViewController:selectedCredential:] : 116 -> 128
~ -[AFUIPasswordsController passwordViewController:fillUsername:] : 116 -> 128
~ -[AFUIPasswordsController passwordViewController:fillPassword:] : 116 -> 128
~ -[AFUIPasswordsController passwordViewController:fillVerificationCode:] : 116 -> 128
~ -[AFUIPasswordsController passwordViewController:fillText:] : 116 -> 128
+ -[AFUICreditCardViewController viewDidDisappear:]
~ -[AFUIServiceDelegate contactsUIWillBeginForSessionUUID:completion:] : 120 -> 136
~ -[AFUIServiceDelegate contactsUIDidEndForSessionUUID:completion:] : 120 -> 136
~ -[AFUIServiceDelegate passwordsUIWillBeginForSessionUUID:completion:] : 120 -> 136
~ -[AFUIServiceDelegate passwordsUIDidEndForSessionUUID:completion:] : 120 -> 136
~ -[AFUIServiceDelegate creditCardsUIWillBeginForSessionUUID:completion:] : 120 -> 136
~ -[AFUIServiceDelegate creditCardsUIDidEndForSessionUUID:completion:] : 120 -> 136
+ -[AFUIServiceDelegate _setIsModalUIPresented:forSessionUUID:]
~ ___isAutoFillPanelAlwaysAllowedForBundleID_block_invoke : 112 -> 124
CStrings:
+ "_setIsModalUIPresented:forSessionUUID:"
+ "com.apple.Preview"
+ "handleEventFromRemoteSource_autoFillIsModalUIPresented:"
+ "isModalUIPresented"
+ "viewDidDisappear:"

```
