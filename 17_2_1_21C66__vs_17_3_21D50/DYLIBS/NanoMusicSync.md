## NanoMusicSync

> `/System/Library/PrivateFrameworks/NanoMusicSync.framework/NanoMusicSync`

```diff

-2021.300.9.1.0
-  __TEXT.__text: 0x4e9bc
+2021.400.2.0.0
+  __TEXT.__text: 0x4ec70
   __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_methlist: 0x3ebc
+  __TEXT.__objc_methlist: 0x3ec8
   __TEXT.__const: 0x180
   __TEXT.__gcc_except_tab: 0x85c
-  __TEXT.__cstring: 0x35fc
-  __TEXT.__oslogstring: 0x7635
+  __TEXT.__cstring: 0x3612
+  __TEXT.__oslogstring: 0x7721
   __TEXT.__dlopen_cstrs: 0xf3
-  __TEXT.__unwind_info: 0x1280
+  __TEXT.__unwind_info: 0x128c
   __TEXT.__objc_classname: 0xa82
-  __TEXT.__objc_methname: 0xbfa9
-  __TEXT.__objc_methtype: 0x18c1
-  __TEXT.__objc_stubs: 0x8a20
-  __DATA_CONST.__got: 0x460
-  __DATA_CONST.__const: 0x1450
+  __TEXT.__objc_methname: 0xc0d3
+  __TEXT.__objc_methtype: 0x18e1
+  __TEXT.__objc_stubs: 0x8ac0
+  __DATA_CONST.__got: 0x468
+  __DATA_CONST.__const: 0x1478
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5540
-  __DATA_CONST.__objc_selrefs: 0x2b58
+  __DATA_CONST.__objc_const: 0x5580
+  __DATA_CONST.__objc_selrefs: 0x2b80
   __DATA_CONST.__objc_arraydata: 0xf8
   __AUTH_CONST.__cfstring: 0x3560
   __AUTH_CONST.__objc_const: 0x1ea8

   __AUTH_CONST.__objc_intobj: 0x450
   __AUTH_CONST.__auth_got: 0x4f8
   __AUTH.__objc_data: 0x11d0
-  __DATA.__objc_classrefs: 0x590
+  __DATA.__objc_classrefs: 0x598
   __DATA.__objc_superrefs: 0x1d8
-  __DATA.__objc_ivar: 0x468
+  __DATA.__objc_ivar: 0x470
   __DATA.__data: 0x560
   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x690

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2690A49A-DA3C-36F4-9E4A-25F0252F150A
-  Functions: 1735
-  Symbols:   6198
-  CStrings:  3533
+  UUID: BD82BD1E-AD12-3A77-B8D4-8FB81DEC00AE
+  Functions: 1738
+  Symbols:   6214
+  CStrings:  3545
 
Symbols:
+ -[NMSMusicCatalogRecommendationsUpdater _handlePrivacyAcknowledgementDidChangeForIdentifier:isPrivacyAcknowledgementRequired:]
+ GCC_except_table15
+ GCC_except_table24
+ _ICPrivacyIdentifierMusic
+ _OBJC_CLASS_$_ICPrivacyInfo
+ _OBJC_IVAR_$_NMSMusicCatalogRecommendationsUpdater._privacyInfo
+ _OBJC_IVAR_$_NMSMusicCatalogRecommendationsUpdater._privacyObservationToken
+ ___126-[NMSMusicCatalogRecommendationsUpdater _handlePrivacyAcknowledgementDidChangeForIdentifier:isPrivacyAcknowledgementRequired:]_block_invoke
+ ___68-[NMSMusicCatalogRecommendationsUpdater _scheduleNextUpdateIfNeeded]_block_invoke.24
+ ___70-[NMSMusicCatalogRecommendationsUpdater beginAutomaticContentUpdating]_block_invoke_2
+ ___91-[NMSMusicCatalogRecommendationsUpdater _performNextUpdateWithScheduler:completionHandler:]_block_invoke.63
+ ___98-[NMSMusicCatalogRecommendationsUpdater _performNextUpdateWithScheduler:urlBag:completionHandler:]_block_invoke.69
+ ___block_descriptor_40_e8_32s_e21_v20?0"NSString"8B16ls32l8
+ __unnamed_array_storage.32
+ __unnamed_array_storage.35
+ _objc_msgSend$_handlePrivacyAcknowledgementDidChangeForIdentifier:isPrivacyAcknowledgementRequired:
+ _objc_msgSend$beginObservingPrivacyAcknowledgementForIdentifier:handler:
+ _objc_msgSend$endObservingPrivacyAcknowledgementForIdentifier:withToken:
+ _objc_msgSend$privacyAcknowledgementRequiredForMusic
+ _objc_msgSend$sharedPrivacyInfo
- GCC_except_table9
- ___68-[NMSMusicCatalogRecommendationsUpdater _scheduleNextUpdateIfNeeded]_block_invoke.22
- ___91-[NMSMusicCatalogRecommendationsUpdater _performNextUpdateWithScheduler:completionHandler:]_block_invoke.61
- ___98-[NMSMusicCatalogRecommendationsUpdater _performNextUpdateWithScheduler:urlBag:completionHandler:]_block_invoke.67
- __unnamed_array_storage.30
- __unnamed_array_storage.33
CStrings:
+ "\x06\x11"
+ "@\"<NSCopying>\""
+ "@\"ICPrivacyInfo\""
+ "[Recommendation] (Music) (Catalog) Privacy acknowledgement is required for Music, won't schedule next update."
+ "[Recommendation] (Music) (Catalog) Received privacy acknowledgement did change for %@, isPrivacyAcknowledgementRequired: %ld."
+ "_handlePrivacyAcknowledgementDidChangeForIdentifier:isPrivacyAcknowledgementRequired:"
+ "_privacyInfo"
+ "_privacyObservationToken"
+ "beginObservingPrivacyAcknowledgementForIdentifier:handler:"
+ "endObservingPrivacyAcknowledgementForIdentifier:withToken:"
+ "privacyAcknowledgementRequiredForMusic"
+ "sharedPrivacyInfo"
+ "v20@?0@\"NSString\"8B16"
- "\x04\x11"

```
