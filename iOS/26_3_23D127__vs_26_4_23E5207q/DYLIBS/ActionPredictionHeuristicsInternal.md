## ActionPredictionHeuristicsInternal

> `/System/Library/PrivateFrameworks/ActionPredictionHeuristicsInternal.framework/ActionPredictionHeuristicsInternal`

```diff

-619.19.0.0.0
-  __TEXT.__text: 0x3f114
-  __TEXT.__auth_stubs: 0x910
-  __TEXT.__objc_methlist: 0x2a0c
-  __TEXT.__const: 0x328
+627.8.3.1.0
+  __TEXT.__text: 0x40f34
+  __TEXT.__auth_stubs: 0x8a0
+  __TEXT.__objc_methlist: 0x2a34
+  __TEXT.__const: 0x330
   __TEXT.__cstring: 0x31ca
-  __TEXT.__gcc_except_tab: 0xe8c
+  __TEXT.__gcc_except_tab: 0xeb0
   __TEXT.__oslogstring: 0x6d8c
   __TEXT.__dlopen_cstrs: 0x1a0
-  __TEXT.__unwind_info: 0xe90
+  __TEXT.__unwind_info: 0x1060
   __TEXT.__objc_classname: 0xc98
-  __TEXT.__objc_methname: 0x7adc
-  __TEXT.__objc_methtype: 0x11b6
-  __TEXT.__objc_stubs: 0x6da0
-  __DATA_CONST.__got: 0x8c0
+  __TEXT.__objc_methname: 0x7d30
+  __TEXT.__objc_methtype: 0x121e
+  __TEXT.__objc_stubs: 0x6e00
+  __DATA_CONST.__got: 0x8c8
   __DATA_CONST.__const: 0xc98
   __DATA_CONST.__objc_classlist: 0x320
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e80
+  __DATA_CONST.__objc_selrefs: 0x1ea8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x130
-  __AUTH_CONST.__auth_got: 0x498
+  __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__const: 0x980
   __AUTH_CONST.__cfstring: 0x34e0
-  __AUTH_CONST.__objc_const: 0x9b08
+  __AUTH_CONST.__objc_const: 0x9b38
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x690
-  __DATA.__objc_ivar: 0x2f8
+  __DATA.__objc_ivar: 0x2fc
   __DATA.__data: 0x340
-  __DATA.__bss: 0x300
+  __DATA.__bss: 0x2e0
   __DATA_DIRTY.__objc_data: 0x18b0
   __DATA_DIRTY.__data: 0x40
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IntelligencePlatform.framework/IntelligencePlatform
+  - /System/Library/PrivateFrameworks/LinkServices.framework/LinkServices
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore

   - /System/Library/PrivateFrameworks/VoiceShortcutClient.framework/VoiceShortcutClient
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AFFCDC60-60A6-356C-95B9-89DF8CC6D09E
-  Functions: 1193
-  Symbols:   5106
-  CStrings:  2800
+  UUID: A4BAF01A-4F1B-3A0C-AB85-4EBD9CAC3AD1
+  Functions: 1215
+  Symbols:   5195
+  CStrings:  2810
 
Symbols:
+ +[ATXContextHeuristicSuggestionProducer _suggestionWithAction:predictionReasons:localizedReason:score:dateInterval:allowedOnLockscreen:allowedOnHomeScreen:allowedOnSpotlight:shouldClearOnEngagement:]
+ +[ATXContextHeuristicSuggestionProducer _uiSpecWithTitle:subtitle:predictionReason:allowedOnLockscreen:allowedOnHomeScreen:allowedOnSpotlight:shouldClearOnEngagement:predictionReasons:dateInterval:]
+ +[ATXContextHeuristicSuggestionProducer groceryShoppingWithTitle:subtitle:heuristicName:predictionReasons:localizedReason:score:]
+ +[ATXContextHeuristicSuggestionProducer suggestionWithAction:predictionReasons:localizedReason:score:dateInterval:allowedOnLockscreen:allowedOnHomeScreen:allowedOnSpotlight:]
+ -[ATXHeuristicDevice relevantIntentProvider]
+ GCC_except_table16
+ _OBJC_CLASS_$_LNRelevantIntentProvider
+ _OBJC_IVAR_$_ATXHeuristicDevice._relevantIntentProvider
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ ___54-[ATXInformationHeuristicRefreshLocationTrigger _stop]_block_invoke
+ ___block_literal_global.28
+ ___block_literal_global.338
+ _objc_autorelease
+ _objc_msgSend$_suggestionWithAction:predictionReasons:localizedReason:score:dateInterval:allowedOnLockscreen:allowedOnHomeScreen:allowedOnSpotlight:shouldClearOnEngagement:
+ _objc_msgSend$_uiSpecWithTitle:subtitle:predictionReason:allowedOnLockscreen:allowedOnHomeScreen:allowedOnSpotlight:shouldClearOnEngagement:predictionReasons:dateInterval:
+ _objc_msgSend$atx_openShoppingExperienceActionWithTitle:subtitle:criteria:heuristicName:
+ _objc_msgSend$suggestionWithAction:predictionReasons:localizedReason:score:dateInterval:allowedOnLockscreen:allowedOnHomeScreen:allowedOnSpotlight:
+ _objc_release_x2
- +[ATXContextHeuristicSuggestionProducer _uiSpecWithTitle:subtitle:predictionReason:shouldClearOnEngagement:predictionReasons:dateInterval:]
- GCC_except_table29
- GCC_except_table32
- ___block_literal_global.25
- ___block_literal_global.329
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_uiSpecWithTitle:subtitle:predictionReason:shouldClearOnEngagement:predictionReasons:dateInterval:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "@\"LNRelevantIntentProvider\""
+ "@68@0:8@16Q24@32d40@48B56B60B64"
+ "@72@0:8@16@24@32B40B44B48B52Q56@64"
+ "@72@0:8@16Q24@32d40@48B56B60B64B68"
+ "T@\"LNRelevantIntentProvider\",R,N"
+ "_relevantIntentProvider"
+ "_suggestionWithAction:predictionReasons:localizedReason:score:dateInterval:allowedOnLockscreen:allowedOnHomeScreen:allowedOnSpotlight:shouldClearOnEngagement:"
+ "_uiSpecWithTitle:subtitle:predictionReason:allowedOnLockscreen:allowedOnHomeScreen:allowedOnSpotlight:shouldClearOnEngagement:predictionReasons:dateInterval:"
+ "atx_openShoppingExperienceActionWithTitle:subtitle:criteria:heuristicName:"
+ "groceryShoppingWithTitle:subtitle:heuristicName:predictionReasons:localizedReason:score:"
+ "relevantIntentProvider"
+ "suggestionWithAction:predictionReasons:localizedReason:score:dateInterval:allowedOnLockscreen:allowedOnHomeScreen:allowedOnSpotlight:"
- "@60@0:8@16@24@32B40Q44@52"
- "_uiSpecWithTitle:subtitle:predictionReason:shouldClearOnEngagement:predictionReasons:dateInterval:"

```
