## SocialLayer

> `/System/Library/PrivateFrameworks/SocialLayer.framework/SocialLayer`

```diff

-191.100.1.0.0
-  __TEXT.__text: 0xbedc4
-  __TEXT.__auth_stubs: 0x2470
+192.100.1.0.0
+  __TEXT.__text: 0xbede0
+  __TEXT.__auth_stubs: 0x2460
   __TEXT.__objc_methlist: 0x641c
   __TEXT.__const: 0x2694
   __TEXT.__gcc_except_tab: 0x17e0

   __TEXT.__unwind_info: 0x31b8
   __TEXT.__eh_frame: 0x1e9c
   __TEXT.__objc_classname: 0xf1f
-  __TEXT.__objc_methname: 0x10816
+  __TEXT.__objc_methname: 0x10852
   __TEXT.__objc_methtype: 0x2878
   __TEXT.__objc_stubs: 0xbaa0
   __DATA_CONST.__got: 0xe80

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x150
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a58
+  __DATA_CONST.__objc_selrefs: 0x3a60
   __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x1248
+  __AUTH_CONST.__auth_got: 0x1240
   __AUTH_CONST.__const: 0x2eb8
   __AUTH_CONST.__cfstring: 0x2f00
   __AUTH_CONST.__objc_const: 0xb488
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x22e0
-  __AUTH.__data: 0xa68
+  __AUTH.__data: 0xa60
   __DATA.__objc_ivar: 0x620
   __DATA.__data: 0x1668
   __DATA.__bss: 0x1f00

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 688D7AFE-A4C1-38A8-BF79-53157D79AB9A
+  UUID: 663763EC-4DA9-34E4-BA2E-59E6A85FC0E6
   Functions: 4714
-  Symbols:   15549
-  CStrings:  4812
+  Symbols:   15548
+  CStrings:  4815
 
Symbols:
+ -[SLDShareableContentService launchApplicationWithBundleIdentifier:sceneIdentifier:forActions:completionHandler:]
+ -[SLDShareableContentService launchApplicationWithBundleIdentifier:sceneIdentifier:forActions:completionHandler:].cold.1
+ -[SLDShareableContentService performAction:onApplicationWithBundleIdentifier:sceneIdentifier:]
+ ___113-[SLDShareableContentService launchApplicationWithBundleIdentifier:sceneIdentifier:forActions:completionHandler:]_block_invoke
+ ___113-[SLDShareableContentService launchApplicationWithBundleIdentifier:sceneIdentifier:forActions:completionHandler:]_block_invoke.cold.1
+ _objc_msgSend$launchApplicationWithBundleIdentifier:sceneIdentifier:forActions:completionHandler:
+ _objc_msgSend$performAction:onApplicationWithBundleIdentifier:sceneIdentifier:
- -[SLDShareableContentService launchApplicationWithBundleIdentifier:forActions:completionHandler:]
- -[SLDShareableContentService launchApplicationWithBundleIdentifier:forActions:completionHandler:].cold.1
- -[SLDShareableContentService performAction:onApplicationWithBundleIdentifier:]
- _$sSo7CKShareC8CloudKitE10oneTimeURL16forParticipantID10Foundation0F0VSgSS_tF
- ___97-[SLDShareableContentService launchApplicationWithBundleIdentifier:forActions:completionHandler:]_block_invoke
- ___97-[SLDShareableContentService launchApplicationWithBundleIdentifier:forActions:completionHandler:]_block_invoke.cold.1
- _objc_msgSend$launchApplicationWithBundleIdentifier:forActions:completionHandler:
- _objc_msgSend$performAction:onApplicationWithBundleIdentifier:
Functions:
~ -[SLDShareableContentService performAction:onApplicationWithBundleIdentifier:] -> -[SLDShareableContentService performAction:onApplicationWithBundleIdentifier:sceneIdentifier:] : 184 -> 212
~ -[SLDShareableContentService fetchShareableContentMetadataFromBundleIdentifier:sceneIdentifier:completion:] : 388 -> 392
~ -[SLDShareableContentService fetchAsynchronousLPMetadataFromBundleIdentifier:sceneIdentifier:completion:] : 384 -> 388
~ -[SLDShareableContentService fetchShareableContentFromBundleIdentifier:sceneIdentifier:requestedTypeIdentifier:requestedItemProviderIndex:responseHandler:] : 320 -> 324
~ -[SLDShareableContentService presentMessageComposeSheetForSceneIdentifier:completion:] : 360 -> 364
~ _$sSTsE10compactMapySayqd__Gqd__Sg7ElementQzKXEKlFSDySo8TUHandleCSo18CKShareParticipantCG_11SocialLayer38CloudKitCollaborationInitiationRequestC8ResponseV9RecipientVTg504$s11g7Layer38ijklm30C24initiateOTLCollaborationAC8n9VyYaKFAF9o6VSgSo8d10C3key_So18eF16C5valuet_tXEfU0_So0E0CTf1cn_nTf4ng_n : 1560 -> 1520
~ _$s11SocialLayer32MeAttributionLocAttributedString6prefix9multiline12localizationSo09NSMutablefG0C09localizedG0_SaySo8_NSRangeVG20baseFontTargetRangesAK06senderopQ0tAA0D10TextPrefixO_SbSSSgtF : 1200 -> 1208
~ _$s11SocialLayer34NameAttributionLocAttributedString6prefix4name9multiline12localizationSo09NSMutablefG0C09localizedG0_SaySo8_NSRangeVG20baseFontTargetRangesAL06senderpqR0tAA0D10TextPrefixO_SSSbSSSgtF : 1356 -> 1364
~ _$s11SocialLayer41ListOfNamesAttributionLocAttributedString6prefix04listdeI09multiline12localizationSo09NSMutablehI0C09localizedI0_SaySo8_NSRangeVG20baseFontTargetRangesAL06senderrsT0tAA0F10TextPrefixO_SSSbSSSgtF : 1356 -> 1364
CStrings:
+ "?"
+ "launchApplicationWithBundleIdentifier:sceneIdentifier:forActions:completionHandler:"
+ "oneTimeURLForParticipantID:"
+ "performAction:onApplicationWithBundleIdentifier:sceneIdentifier:"
- "launchApplicationWithBundleIdentifier:forActions:completionHandler:"
- "performAction:onApplicationWithBundleIdentifier:"

```
