## CarPlaySupport

> `/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport`

```diff

-515.17.3.2.0
-  __TEXT.__text: 0x11bcc8
+515.22.0.0.0
+  __TEXT.__text: 0x11bce4
   __TEXT.__auth_stubs: 0x1360
   __TEXT.__objc_methlist: 0xa44c
   __TEXT.__const: 0xd64

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__unwind_info: 0x1d00
   __TEXT.__objc_classname: 0x17be
-  __TEXT.__objc_methname: 0x1d262
+  __TEXT.__objc_methname: 0x1d282
   __TEXT.__objc_methtype: 0x52a4
   __TEXT.__objc_stubs: 0x13da0
   __DATA_CONST.__got: 0xdf0

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6558
+  __DATA_CONST.__objc_selrefs: 0x6560
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x300
   __DATA_CONST.__objc_arraydata: 0x100

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AC60A431-CA16-32CB-96AA-B437BFFD3667
+  UUID: 357D0D3E-50B3-386B-8385-2E1A1CCEC104
   Functions: 3694
   Symbols:   14760
-  CStrings:  6055
+  CStrings:  6056
 
Symbols:
+ ___61-[CPSMapTemplateViewController showNavigationAlert:animated:]_block_invoke.249
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.223
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.224
+ ___77-[CPSTemplateInstance presentVoiceTemplate:withProxyDelegate:animated:reply:]_block_invoke.128
+ ___86-[CPSTemplateInstance templateViewController:requestsPlaybackPresentation:completion:]_block_invoke.218
+ ___90-[CPSTemplateInstance pushMapTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.115
+ ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.120
+ ___93-[CPSTemplateInstance pushEntityTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.135
+ ___93-[CPSTemplateInstance pushSearchTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.124
+ ___97-[CPSTemplateInstance pushNowPlayingTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.121
+ ___99-[CPSTemplateInstance pushVoiceControlTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.129
+ ___block_literal_global.144
+ ___block_literal_global.148
+ ___block_literal_global.152
+ ___block_literal_global.155
+ ___block_literal_global.240
+ ___block_literal_global.242
+ ___block_literal_global.359
+ ___block_literal_global.375
+ ___block_literal_global.390
+ _objc_msgSend$mapTemplateShouldProvideNavigationMetadata:
- ___61-[CPSMapTemplateViewController showNavigationAlert:animated:]_block_invoke.252
- ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.219
- ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.222
- ___77-[CPSTemplateInstance presentVoiceTemplate:withProxyDelegate:animated:reply:]_block_invoke.126
- ___86-[CPSTemplateInstance templateViewController:requestsPlaybackPresentation:completion:]_block_invoke.216
- ___90-[CPSTemplateInstance pushMapTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.113
- ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.116
- ___93-[CPSTemplateInstance pushEntityTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.133
- ___93-[CPSTemplateInstance pushSearchTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.122
- ___97-[CPSTemplateInstance pushNowPlayingTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.119
- ___99-[CPSTemplateInstance pushVoiceControlTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.127
- ___block_literal_global.142
- ___block_literal_global.146
- ___block_literal_global.150
- ___block_literal_global.153
- ___block_literal_global.243
- ___block_literal_global.245
- ___block_literal_global.362
- ___block_literal_global.378
- ___block_literal_global.393
- _objc_msgSend$sendsNavigationMetadata
Functions:
~ -[CPSTemplateInstance pushMapTemplate:withProxyDelegate:animated:presentationStyle:reply:] : 748 -> 892
~ -[CPSTemplateInstance didCreateNavigator:] : 1516 -> 1412
~ -[CPSMapTemplateViewController _handleShareButtonTapped:] : 1228 -> 1216
CStrings:
+ "DESTINATION_SHARING_ALERT_TITLE_%@"
+ "mapTemplateShouldProvideNavigationMetadata:"
- "DESTINATION_SHARING_ALERT_TITLE"

```
