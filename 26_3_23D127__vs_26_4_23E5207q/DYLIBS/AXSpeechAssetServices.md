## AXSpeechAssetServices

> `/System/Library/PrivateFrameworks/AXSpeechAssetServices.framework/AXSpeechAssetServices`

```diff

-3191.7.24.0.0
-  __TEXT.__text: 0xd98
-  __TEXT.__auth_stubs: 0x200
+3191.19.0.0.0
+  __TEXT.__text: 0xee4
+  __TEXT.__auth_stubs: 0x1e0
   __TEXT.__objc_methlist: 0x29c
   __TEXT.__const: 0x8
   __TEXT.__cstring: 0x158
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0xa0
+  __TEXT.__unwind_info: 0xa8
   __TEXT.__objc_classname: 0x71
   __TEXT.__objc_methname: 0x6b4
   __TEXT.__objc_methtype: 0x282

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x108
+  __AUTH_CONST.__auth_got: 0xf8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x200
   __AUTH_CONST.__objc_const: 0x3e8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EFFE9298-2A5F-30F8-8B88-93E5C8DA1490
+  UUID: 1C9265A4-6CBD-375F-AA8F-272598D10BFC
   Functions: 22
-  Symbols:   165
+  Symbols:   163
   CStrings:  149
 
Symbols:
+ ___block_literal_global.416
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x27
- ___block_literal_global.377
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[AXSpeechPronunciationOptions initWithCoder:] : 208 -> 216
~ -[AXSpeechPronunciationOptions encodeWithCoder:] : 156 -> 164
~ -[AXSpeechPronunciationOptions description] : 140 -> 152
~ -[AXSpeechPronunciationOptions setOrthography:] : 12 -> 64
~ -[AXSpeechPronunciationOptions setLanguage:] : 12 -> 64
~ -[AXSpeechPronunciationHelper _assetUpdaterClient] : 68 -> 84
~ -[AXSpeechPronunciationHelper dealloc] : 92 -> 96
~ -[AXSpeechPronunciationHelper supportsPronunciationSessions] : 80 -> 84
~ -[AXSpeechPronunciationHelper userInterfaceClient:processMessageFromServer:withIdentifier:error:] : 508 -> 544
~ -[AXSpeechPronunciationHelper audioLevel] : 144 -> 156
~ -[AXSpeechPronunciationHelper startPronunciationSession:resultCallback:] : 1032 -> 1104
~ -[AXSpeechPronunciationHelper stopPronunciationSession] : 404 -> 432
~ -[AXSpeechPronunciationHelper cancelPronunciationSession] : 408 -> 436

```
