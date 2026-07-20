## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2451.1.101.0.0
-  __TEXT.__text: 0x2a910
-  __TEXT.__objc_methlist: 0x1648
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0xef0
-  __TEXT.__cstring: 0x2758
-  __TEXT.__oslogstring: 0x24bd
-  __TEXT.__unwind_info: 0x9d8
+2454.100.0.0.0
+  __TEXT.__text: 0x29f40
+  __TEXT.__objc_methlist: 0x1628
+  __TEXT.__const: 0x128
+  __TEXT.__gcc_except_tab: 0xf4c
+  __TEXT.__cstring: 0x22fc
+  __TEXT.__oslogstring: 0x24ec
+  __TEXT.__unwind_info: 0x9c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc90
+  __DATA_CONST.__const: 0xc68
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1120
+  __DATA_CONST.__objc_selrefs: 0x1108
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__objc_arraydata: 0xa50
+  __DATA_CONST.__objc_arraydata: 0x930
   __DATA_CONST.__got: 0x278
   __AUTH_CONST.__const: 0x520
-  __AUTH_CONST.__cfstring: 0x4b40
+  __AUTH_CONST.__cfstring: 0x45e0
   __AUTH_CONST.__objc_const: 0x2380
-  __AUTH_CONST.__objc_dictobj: 0xf0
+  __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60

   __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0x730
   __DATA_DIRTY.__data: 0x258
-  __DATA_DIRTY.__bss: 0x2e8
+  __DATA_DIRTY.__bss: 0x2d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 826
-  Symbols:   1806
-  CStrings:  917
+  Functions: 820
+  Symbols:   1796
+  CStrings:  875
 
Symbols:
+ -[SRParameter initWithBoolean:name:]
+ -[SRParameter initWithDouble:name:]
+ -[SRParameter initWithFilePath:name:]
+ -[SRParameter initWithLong:name:]
+ -[SRParameter initWithString:name:]
+ -[SRParameter initWithType:name:]
+ -[SRParameter isCurrent]
+ -[SRParameter setIsCurrent:]
+ _OBJC_IVAR_$_SRParameter._isCurrent
+ _objc_msgSend$initWithBoolean:name:
+ _objc_msgSend$initWithDouble:name:
+ _objc_msgSend$initWithFilePath:name:
+ _objc_msgSend$initWithLong:name:
+ _objc_msgSend$initWithString:name:
+ _objc_msgSend$initWithType:name:
+ _objc_msgSend$isCurrent
+ _objc_msgSend$setIsCurrent:
+ _uafAssetSetName_block_invoke_2.kDeliveryTypes
- +[SRResourcesManager defaultParameterWithType:value:name:]
- +[SRResourcesManager fetchUserDefaults]
- +[SRResourcesManager updateDefaultParameter:withValue:]
- -[SRParameter flag]
- -[SRParameter initWithBoolean:flags:name:]
- -[SRParameter initWithDouble:flags:name:]
- -[SRParameter initWithFilePath:flags:name:]
- -[SRParameter initWithLong:flags:name:]
- -[SRParameter initWithString:flags:name:]
- -[SRParameter initWithType:flags:name:]
- -[SRParameter setFlag:]
- _OBJC_IVAR_$_SRParameter._flag
- ___39+[SRResourcesManager fetchUserDefaults]_block_invoke
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
- _fetchUserDefaults.userListOnceToken
- _objc_msgSend$defaultParameterWithType:value:name:
- _objc_msgSend$fetchUserDefaults
- _objc_msgSend$flag
- _objc_msgSend$initWithBoolean:flags:name:
- _objc_msgSend$initWithDouble:flags:name:
- _objc_msgSend$initWithFilePath:flags:name:
- _objc_msgSend$initWithLong:flags:name:
- _objc_msgSend$initWithString:flags:name:
- _objc_msgSend$initWithType:flags:name:
- _objc_msgSend$parametersOfNamespaceWithName:
- _objc_msgSend$setFlag:
- _sUserDefaultsParameterList
- _sUserDefaultsParameterListLock
CStrings:
+ "Delta2026"
+ "Delta2026Test"
+ "Optional2026"
+ "Optional2026Test"
+ "[%d] Error loading (%@, %@) assets: %@"
+ "loadOTA[%llu] server 3.1.1 found (%@, %@)"
+ "loadOTA[%llu] server 3.1.2 no match for (%@, %@)"
- "BlueButton"
- "CommittedScreenMatchingBehavior"
- "Delta"
- "Delta2025"
- "Delta2025Test"
- "EnableSafariTopHitsLogic"
- "FilterLocalSuggestions"
- "HideSearchThroughSuggestions"
- "L1Threshold"
- "L2Threshold"
- "Legacy"
- "MaxCountTopHits"
- "MaxSectionsBeforeShowMore"
- "MaxSectionsBeforeShowMoreWithScopedSearch"
- "MaxVisibleResultsCountPerSection"
- "MinSectionCountThresholdForShowMore"
- "MinSpellCorrectedAppTopHitScore"
- "MinTopHitScore"
- "MinTopHitThresholdForBigResult"
- "Optional"
- "Optional2024"
- "Optional2025"
- "Optional2025Test"
- "Parameter %@ has value from user defaults"
- "SPBlueButtonBehavior"
- "SPBullseyeFilterLocalSuggestions"
- "SPBullseyeMinSpellCorrectedAppTopHitScore"
- "SPBullseyeMinTopHitScore"
- "SPCommittedScreenMatchingBehavior"
- "SPEnableSafariTopHitsLogic"
- "SPHideSearchThroughSuggestions"
- "SPL1Threshold"
- "SPL2Threshold"
- "SPMaxCountTopHits"
- "SPMaxSectionsBeforeShowMore"
- "SPMaxSectionsBeforeShowMoreWithScopedSearch"
- "SPMaxVisibleResultsCountPerSection"
- "SPMinSectionCountThresholdForShowMore"
- "SPMinTopHitThresholdForBigResult"
- "SPSuggestionDetailTextBehavior"
- "SPUIBullseyeShowDebugLocalSuggestions"
- "SPUIBullseyeShowTopHitSectionHeaderInAsYouTypeScreen"
- "ShowDebugLocalSuggestions"
- "ShowTopHitSectionHeaderInAsYouTypeScreen"
- "SuggestionDetailTextBehaviorType"
- "User default is not set for parameter %@"
- "UserDefault"
- "UserDefaultFirst"
- "com.apple.searchd"
```
