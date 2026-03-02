## NewsCore

> `/System/Library/PrivateFrameworks/NewsCore.framework/NewsCore`

```diff

-5864.0.0.0.0
-  __TEXT.__text: 0x431638
+5867.0.0.0.0
+  __TEXT.__text: 0x4321b4
   __TEXT.__auth_stubs: 0x3ce0
-  __TEXT.__objc_methlist: 0x34944
+  __TEXT.__objc_methlist: 0x34ab4
   __TEXT.__const: 0xdfc8
   __TEXT.__swift5_typeref: 0x425a
   __TEXT.__constg_swiftt: 0x324c

   __TEXT.__swift5_proto: 0x9e0
   __TEXT.__swift5_types: 0x424
   __TEXT.__swift5_capture: 0xe24
-  __TEXT.__oslogstring: 0x1807b
+  __TEXT.__oslogstring: 0x180b4
   __TEXT.__swift5_protos: 0x68
   __TEXT.__swift_as_entry: 0x310
   __TEXT.__swift_as_ret: 0x398
-  __TEXT.__cstring: 0x54ede
+  __TEXT.__cstring: 0x55112
   __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x3a0
   __TEXT.__swift5_mpenum: 0x54
   __TEXT.__gcc_except_tab: 0x50a4
   __TEXT.__dlopen_cstrs: 0x11c
   __TEXT.__ustring: 0x280
-  __TEXT.__unwind_info: 0x10000
+  __TEXT.__unwind_info: 0x10008
   __TEXT.__eh_frame: 0xa058
-  __TEXT.__objc_classname: 0x805f
-  __TEXT.__objc_methname: 0x88af0
-  __TEXT.__objc_methtype: 0xcdd0
-  __TEXT.__objc_stubs: 0x35c00
+  __TEXT.__objc_classname: 0x8060
+  __TEXT.__objc_methname: 0x89220
+  __TEXT.__objc_methtype: 0xcdd3
+  __TEXT.__objc_stubs: 0x35ce0
   __DATA_CONST.__got: 0x2bc0
   __DATA_CONST.__const: 0x11850
   __DATA_CONST.__objc_classlist: 0x1cc0
   __DATA_CONST.__objc_catlist: 0x298
   __DATA_CONST.__objc_protolist: 0x908
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14828
+  __DATA_CONST.__objc_selrefs: 0x148e0
   __DATA_CONST.__objc_protorefs: 0x258
   __DATA_CONST.__objc_superrefs: 0x15b8
   __DATA_CONST.__objc_arraydata: 0x2a80
   __AUTH_CONST.__auth_got: 0x1e88
   __AUTH_CONST.__const: 0xc300
-  __AUTH_CONST.__cfstring: 0x317a0
-  __AUTH_CONST.__objc_const: 0x78e48
+  __AUTH_CONST.__cfstring: 0x31980
+  __AUTH_CONST.__objc_const: 0x79130
   __AUTH_CONST.__objc_arrayobj: 0x6a8
   __AUTH_CONST.__objc_intobj: 0x13c8
   __AUTH_CONST.__objc_dictobj: 0xc30
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH.__objc_data: 0x40d0
   __AUTH.__data: 0x630
-  __DATA.__objc_ivar: 0x4524
+  __DATA.__objc_ivar: 0x4544
   __DATA.__data: 0x67f0
   __DATA.__bss: 0xdd80
   __DATA.__common: 0x88
-  __DATA_DIRTY.__objc_ivar: 0xf8c
+  __DATA_DIRTY.__objc_ivar: 0xf90
   __DATA_DIRTY.__objc_data: 0xdfc0
   __DATA_DIRTY.__data: 0x2d00
   __DATA_DIRTY.__common: 0x490

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 14BBAF6F-8C62-373E-981F-DF681D3DC03F
-  Functions: 24584
-  Symbols:   65743
-  CStrings:  37593
+  UUID: 315C1247-338D-3224-89A2-2B7B4559BE92
+  Functions: 24605
+  Symbols:   65800
+  CStrings:  37663
 
Symbols:
+ -[FCNewsAppConfig blockedCuratedStorySelectionMessage]
+ -[FCNewsAppConfig blockingConfirmationChannelMessage]
+ -[FCNewsAppConfig blockingConfirmationDialogEnabled]
+ -[FCNewsAppConfig channelPickerKeepFollowsForCustomChannelPickerIDs]
+ -[FCNewsAppConfig maxRecipeUnitConversionError]
+ -[FCNewsAppConfig maxRecipeUnitConversionTbspBeforeWeight]
+ -[FCNewsAppConfig recipeAlcoholicDrinkTagID]
+ -[FCNewsAppConfig recipeBakingTagID]
+ -[FCNewsAppConfig recipeNonAlcoholicDrinkTagID]
+ -[FCRecipe initWithRecipeRecord:sourceChannel:articles:assetManager:interestToken:appConfiguration:]
+ -[FCRecipe isBakingRecipe]
+ -[FCRecipe isCocktailRecipe]
+ -[FCTagFeedPromotedHeadlinesFetchOperation initWithConfiguration:cloudContext:tagID:expireAfterTimeWindow:filterOptions:]
+ -[FCTipConfig localHubAutoFollowEnticeBubbleTipBody]
+ -[FCTipConfig localHubAutoFollowEnticeBubbleTipIconUrl]
+ -[FCTipConfig localHubAutoFollowEnticeBubbleTipPresentationsQuiescenceInterval]
+ -[FCTipConfig localHubAutoFollowEnticeBubbleTipTitle]
+ -[FCTipConfig localHubLocationsBubbleTipBody]
+ -[FCTipConfig localHubLocationsBubbleTipIconUrl]
+ -[FCTipConfig localHubLocationsBubbleTipPresentationsQuiescenceInterval]
+ -[FCTipConfig localHubLocationsBubbleTipTitle]
+ -[FCTipConfig maxLocalHubAutoFollowEnticeBubbleTipPresentations]
+ -[FCTipConfig maxLocalHubLocationsBubbleTipPresentations]
+ -[FCTipConfig setLocalHubAutoFollowEnticeBubbleTipBody:]
+ -[FCTipConfig setLocalHubAutoFollowEnticeBubbleTipIconUrl:]
+ -[FCTipConfig setLocalHubAutoFollowEnticeBubbleTipTitle:]
+ -[FCTipConfig setLocalHubLocationsBubbleTipBody:]
+ -[FCTipConfig setLocalHubLocationsBubbleTipIconUrl:]
+ -[FCTipConfig setLocalHubLocationsBubbleTipTitle:]
+ -[NTPBTagRecord(FCAdditions) generateFeedNavDarkModeImageAssetHandleWithAssetManager:]
+ -[NTPBTagRecord(FCAdditions) generateFeedNavDarkModeImageHQAssetHandleWithAssetManager:]
+ _OBJC_IVAR_$_FCRecipe._isBakingRecipe
+ _OBJC_IVAR_$_FCRecipe._isCocktailRecipe
+ _OBJC_IVAR_$_FCTipConfig._localHubAutoFollowEnticeBubbleTipBody
+ _OBJC_IVAR_$_FCTipConfig._localHubAutoFollowEnticeBubbleTipIconUrl
+ _OBJC_IVAR_$_FCTipConfig._localHubAutoFollowEnticeBubbleTipPresentationsQuiescenceInterval
+ _OBJC_IVAR_$_FCTipConfig._localHubAutoFollowEnticeBubbleTipTitle
+ _OBJC_IVAR_$_FCTipConfig._localHubLocationsBubbleTipBody
+ _OBJC_IVAR_$_FCTipConfig._localHubLocationsBubbleTipIconUrl
+ _OBJC_IVAR_$_FCTipConfig._localHubLocationsBubbleTipPresentationsQuiescenceInterval
+ _OBJC_IVAR_$_FCTipConfig._localHubLocationsBubbleTipTitle
+ _OBJC_IVAR_$_FCTipConfig._maxLocalHubAutoFollowEnticeBubbleTipPresentations
+ _OBJC_IVAR_$_FCTipConfig._maxLocalHubLocationsBubbleTipPresentations
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeI26NTPBKeyValuePair_ValueTypeU8__strongPU32objcproto21FCKeyValueStoreCoding10objc_classEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEED1B9nqe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
+ ___block_literal_global.2349
+ ___block_literal_global.2378
+ ___block_literal_global.2802
+ ___block_literal_global.2890
+ ___block_literal_global.3013
+ ___block_literal_global.3015
+ ___block_literal_global.3017
+ ___block_literal_global.3025
+ ___block_literal_global.3036
+ ___block_literal_global.3041
+ ___block_literal_global.3046
+ ___block_literal_global.3051
+ _objc_msgSend$feedNavDarkModeImage
+ _objc_msgSend$feedNavDarkModeImageHQ
+ _objc_msgSend$feedNavDarkModeImageHQURL
+ _objc_msgSend$generateFeedNavDarkModeImageHQAssetHandleWithAssetManager:
+ _objc_msgSend$initWithRecipeRecord:sourceChannel:articles:assetManager:interestToken:appConfiguration:
+ _objc_msgSend$recipeAlcoholicDrinkTagID
+ _objc_msgSend$recipeBakingTagID
+ _objc_msgSend$recipeNonAlcoholicDrinkTagID
- -[FCRecipe initWithRecipeRecord:sourceChannel:articles:assetManager:interestToken:]
- -[FCSmarterMessagingConfig localHubLocationsBubbleTipBody]
- -[FCSmarterMessagingConfig localHubLocationsBubbleTipPresentationsQuiescenceInterval]
- -[FCSmarterMessagingConfig localHubLocationsBubbleTipTitle]
- -[FCSmarterMessagingConfig maxLocalHubLocationsBubbleTipPresentations]
- -[FCSmarterMessagingConfig setLocalHubLocationsBubbleTipBody:]
- -[FCSmarterMessagingConfig setLocalHubLocationsBubbleTipTitle:]
- -[FCTag primaryLiveActivityID]
- -[FCTag secondaryLiveActivityIDs]
- -[FCTagFeedPromotedHeadlinesFetchOperation initWithConfiguration:cloudContext:tagID:expireAfterTimeWindow:]
- _OBJC_IVAR_$_FCSmarterMessagingConfig._localHubLocationsBubbleTipBody
- _OBJC_IVAR_$_FCSmarterMessagingConfig._localHubLocationsBubbleTipPresentationsQuiescenceInterval
- _OBJC_IVAR_$_FCSmarterMessagingConfig._localHubLocationsBubbleTipTitle
- _OBJC_IVAR_$_FCSmarterMessagingConfig._maxLocalHubLocationsBubbleTipPresentations
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeI26NTPBKeyValuePair_ValueTypeU8__strongPU32objcproto21FCKeyValueStoreCoding10objc_classEEPvEENS_22__hash_node_destructorINS_9allocatorIS9_EEEEED1B9foe210106Ev
- __ZSt28__throw_bad_array_new_lengthB9foe210106v
- ___block_literal_global.2340
- ___block_literal_global.2369
- ___block_literal_global.2793
- ___block_literal_global.2881
- ___block_literal_global.3004
- ___block_literal_global.3006
- ___block_literal_global.3008
- ___block_literal_global.3016
- ___block_literal_global.3027
- ___block_literal_global.3032
- ___block_literal_global.3037
- ___block_literal_global.3042
- _objc_msgSend$initWithRecipeRecord:sourceChannel:articles:assetManager:interestToken:
CStrings:
+ "%{public}@ did filter promoted headlines from %lu to %lu"
+ "3##"
+ "@56@0:8@16@24@32d40Q48"
+ "C\x85"
+ "T@\"NSString\",C,N,V_localHubAutoFollowEnticeBubbleTipBody"
+ "T@\"NSString\",C,N,V_localHubAutoFollowEnticeBubbleTipIconUrl"
+ "T@\"NSString\",C,N,V_localHubAutoFollowEnticeBubbleTipTitle"
+ "T@\"NSString\",C,N,V_localHubLocationsBubbleTipIconUrl"
+ "TB,R,N,V_isBakingRecipe"
+ "TB,R,N,V_isCocktailRecipe"
+ "Tq,R,N,V_localHubAutoFollowEnticeBubbleTipPresentationsQuiescenceInterval"
+ "Tq,R,N,V_maxLocalHubAutoFollowEnticeBubbleTipPresentations"
+ "_isBakingRecipe"
+ "_isCocktailRecipe"
+ "_localHubAutoFollowEnticeBubbleTipBody"
+ "_localHubAutoFollowEnticeBubbleTipIconUrl"
+ "_localHubAutoFollowEnticeBubbleTipPresentationsQuiescenceInterval"
+ "_localHubAutoFollowEnticeBubbleTipTitle"
+ "_localHubLocationsBubbleTipIconUrl"
+ "_maxLocalHubAutoFollowEnticeBubbleTipPresentations"
+ "blockedCuratedStorySelectionMessage"
+ "blockingConfirmationChannelMessage"
+ "blockingConfirmationDialogEnabled"
+ "channelPickerKeepFollowsForCustomChannelPickerIDs"
+ "feedNavDarkModeImageHQURL"
+ "generateFeedNavDarkModeImageHQAssetHandleWithAssetManager:"
+ "initWithConfiguration:cloudContext:tagID:expireAfterTimeWindow:filterOptions:"
+ "initWithRecipeRecord:sourceChannel:articles:assetManager:interestToken:appConfiguration:"
+ "isBakingRecipe"
+ "isCocktailRecipe"
+ "localHubAutoFollowEnticeBubbleTipBody"
+ "localHubAutoFollowEnticeBubbleTipIconUrl"
+ "localHubAutoFollowEnticeBubbleTipPresentationsQuiescenceInterval"
+ "localHubAutoFollowEnticeBubbleTipTitle"
+ "localHubLocationsBubbleTipIconUrl"
+ "maxLocalHubAutoFollowEnticeBubbleTipPresentations"
+ "maxRecipeUnitConversionError"
+ "maxRecipeUnitConversionTbspBeforeWeight"
+ "recipeAlcoholicDrinkTagID"
+ "recipeAlcoholicDrinkTagId"
+ "recipeBakingTagID"
+ "recipeBakingTagId"
+ "recipeNonAlcoholicDrinkTagID"
+ "recipeNonAlcoholicDrinkTagId"
+ "setLocalHubAutoFollowEnticeBubbleTipBody:"
+ "setLocalHubAutoFollowEnticeBubbleTipIconUrl:"
+ "setLocalHubAutoFollowEnticeBubbleTipTitle:"
+ "setLocalHubLocationsBubbleTipIconUrl:"
- "@48@0:8@16@24@32d40"
- "C\x85B"
- "initWithConfiguration:cloudContext:tagID:expireAfterTimeWindow:"
- "initWithRecipeRecord:sourceChannel:articles:assetManager:interestToken:"

```
