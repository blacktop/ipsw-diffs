## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1975.0.0.0.0
-  __TEXT.__text: 0x1251f4
+1976.0.0.0.0
+  __TEXT.__text: 0x125300
   __TEXT.__objc_methlist: 0xaedc
   __TEXT.__const: 0x988
   __TEXT.__gcc_except_tab: 0x4a90

   __AUTH_CONST.__objc_arrayobj: 0x11d60
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_dictobj: 0x22858
-  __AUTH_CONST.__auth_got: 0x800
-  __AUTH.__objc_data: 0x1db0
+  __AUTH_CONST.__auth_got: 0x808
   __DATA.__objc_ivar: 0xf34
-  __DATA.__data: 0x428
-  __DATA_DIRTY.__objc_data: 0x1950
+  __DATA_DIRTY.__objc_data: 0x3700
+  __DATA_DIRTY.__data: 0x428
   __DATA_DIRTY.__bss: 0x520
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 5368
-  Symbols:   7993
+  Symbols:   7994
   CStrings:  17939
 
Symbols:
+ __CDStringByConvertingPhoneNumberStringToASCII
Functions:
~ -[_PSContactCache getContactForHandle:handleType:] : 1124 -> 1144
~ -[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:predictionContext:] : 15044 -> 15140
~ -[_PSEnsembleModel psr_suggestionsFromSuggestionProxies:interactionsStatistics:maxSuggestions:predictionContext:] : 1948 -> 1976
~ ___37-[_PSFamilyRecommender currentFamily]_block_invoke : 1444 -> 1472
~ -[_PSContactResolver resolveContactIdentifier:] : 800 -> 816
~ -[_PSContactResolver resolveContactIfPossibleFromContactIdentifierString:pickFirstOfMultiple:] : 268 -> 296
~ +[_PSContactResolver normalizedHandlesDictionaryFromHandles:] : 404 -> 436
~ -[_PSContactCatalog resolveVisualIdentifiersForHandles:catalogContactData:keepGoing:] : 8920 -> 8940
```
