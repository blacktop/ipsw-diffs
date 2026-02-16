## PersonaKit

> `/System/Library/PrivateFrameworks/PersonaKit.framework/PersonaKit`

```diff

-1366.200.2.0.0
-  __TEXT.__text: 0x6704
-  __TEXT.__auth_stubs: 0x3a0
+1366.500.41.0.0
+  __TEXT.__text: 0x699c
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_methlist: 0x8a0
   __TEXT.__const: 0x59
   __TEXT.__cstring: 0x1098
   __TEXT.__oslogstring: 0xb2f
-  __TEXT.__unwind_info: 0x1f8
+  __TEXT.__unwind_info: 0x220
   __TEXT.__objc_classname: 0xed
   __TEXT.__objc_methname: 0x172f
   __TEXT.__objc_methtype: 0x866

   __DATA_CONST.__objc_selrefs: 0x5f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1d8
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x6c0
   __AUTH_CONST.__objc_const: 0xe68

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C406FCAD-EDF1-3583-8057-4C258F5EF446
+  UUID: 5C45BB29-C05E-3736-B4D9-BCD772B2ADDF
   Functions: 169
-  Symbols:   648
+  Symbols:   644
   CStrings:  583
 
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x22
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x21
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[PRLikeness init] : 100 -> 108
~ -[PRLikeness _initWithIdentifier:] : 160 -> 152
~ -[PRLikeness initWithCoder:] : 1072 -> 1140
~ -[PRLikeness encodeWithCoder:] : 496 -> 520
~ +[PRLikeness likenessWithPropagatedData:] : 424 -> 440
~ -[PRLikeness setRecipe:] : 120 -> 124
~ -[PRLikeness setExternalIdentifier:] : 120 -> 124
~ -[PRLikeness staticRepresentation] : 392 -> 400
~ -[PRLikeness staticRepresentationData] : 576 -> 588
~ -[PRLikeness setStaticRepresentationData:] : 48 -> 56
~ +[PRLikeness scopeFromDescription:] : 96 -> 100
~ -[PRLikeness description] : 740 -> 804
~ +[PRLikeness _dateFormatter] : 68 -> 84
~ -[PRLikeness setCreationDate:] : 12 -> 64
~ -[PRLikeness setExpirationDate:] : 12 -> 64
~ -[PRLikeness setSoftExpirationDate:] : 12 -> 64
~ -[PRLikeness setOwnerID:] : 12 -> 64
~ -[PRLikeness setInsertionDate:] : 12 -> 64
~ -[PRLikeness setDirtyProperties:] : 12 -> 64
~ -[NSString(PersonaKit) pr_numericValue] : 188 -> 208
~ +[NSString(PersonaKit) pr_hexStringWithData:] : 192 -> 196
~ +[PRPersonaServiceInterface XPCInterface] : 68 -> 84
~ ___41+[PRPersonaServiceInterface XPCInterface]_block_invoke : 296 -> 308
~ -[NSError(PersonaKit) pr_isNetworkAvailabilityError] : 276 -> 284
~ -[NSError(PersonaKit) pr_isInPersonaDomain] : 64 -> 68
~ -[PRPersonaStore _setHasVendedData:] : 220 -> 224
~ -[PRPersonaStore likenessForPhoneNumber:desiredFreshness:completion:] : 380 -> 372
~ -[PRPersonaStore likenessForEmailAddress:desiredFreshness:completion:] : 380 -> 372
~ ___68-[PRPersonaStore saveLikeness:forPrimayiCloudAccountWithCompletion:]_block_invoke : 440 -> 444
~ -[PRPersonaStore changeCurrentSelfLikenessToLikenessWithUniqueID:completion:] : 360 -> 356
~ ___77-[PRPersonaStore changeCurrentSelfLikenessToLikenessWithUniqueID:completion:]_block_invoke : 440 -> 444
~ -[PRPersonaStore removeLikeness:forPrimayiCloudAccountWithCompletion:] : 360 -> 356
~ ___70-[PRPersonaStore removeLikeness:forPrimayiCloudAccountWithCompletion:]_block_invoke : 440 -> 444
~ ___73-[PRPersonaStore removeAllLikenessForPrimaryiCloudAccountWithCompletion:]_block_invoke : 440 -> 444
~ ___56-[PRPersonaStore handleAppleIDEvent:account:completion:]_block_invoke : 440 -> 444
~ -[PRPersonaStore donateLikeness:forEmailAddress:completion:] : 380 -> 372
~ ___60-[PRPersonaStore donateLikeness:forEmailAddress:completion:]_block_invoke : 468 -> 472
~ -[PRPersonaStore donateLikeness:forPhoneNumber:completion:] : 380 -> 372
~ ___59-[PRPersonaStore donateLikeness:forPhoneNumber:completion:]_block_invoke : 468 -> 472
~ -[PRPersonaStore likenessesWithExternalIdentifier:completion:] : 380 -> 372
~ -[PRPersonaStore screenNameForEmailAddress:completion:] : 412 -> 408
~ -[PRPersonaStore screenNameForPhoneNumber:completion:] : 412 -> 408
~ -[PRPersonaStore screenNameForPrimaryiCloudAccountWithCompletion:] : 364 -> 368
~ -[PRPersonaStore screenNameForAppleIDWithAltDSID:completion:] : 412 -> 408
~ -[PRPersonaStore setScreenName:forPrimaryiCloudAccountWithCompletion:] : 364 -> 368
~ ___70-[PRPersonaStore setScreenName:forPrimaryiCloudAccountWithCompletion:]_block_invoke : 440 -> 444
~ -[PRPersonaStore setScreenName:forAppleIDWithAltDSID:completion:] : 412 -> 408
~ ___65-[PRPersonaStore setScreenName:forAppleIDWithAltDSID:completion:]_block_invoke : 468 -> 472
~ -[PRPersonaStore _startListeningForCacheChangeNotifications] : 284 -> 288
~ __PRHandleSelfCacheDidChange : 360 -> 368
~ __PRHandleOtherCacheDidChange : 360 -> 368
~ -[PRPersonaStore _stopListeningForCacheChangeNotifications] : 244 -> 248
~ +[PRLikenessChange changeForLikeness:withType:] : 252 -> 276
~ +[PRLikenessChange changeTypeFromDescription:] : 88 -> 92
~ -[PRLikenessChange description] : 144 -> 152
~ __PRGetLogSystem : 68 -> 84

```
