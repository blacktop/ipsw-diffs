## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2400.16.0.0.0
-  __TEXT.__text: 0xcff48
+2400.17.1.0.0
+  __TEXT.__text: 0xd0030
   __TEXT.__auth_stubs: 0x1c00
   __TEXT.__objc_methlist: 0xca48
   __TEXT.__const: 0xcdc

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DA089917-1935-358D-9B21-2E1DCD51872F
+  UUID: 8F6EE4CE-E059-3041-87C8-9B6E0FA62C75
   Functions: 5480
   Symbols:   17271
   CStrings:  12099
Symbols:
+ ___21-[CSSearchQuery poll]_block_invoke.1047
+ ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1075
+ ___block_literal_global.1050
+ ___block_literal_global.1056
- ___21-[CSSearchQuery poll]_block_invoke.1046
- ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1074
- ___block_literal_global.1049
- ___block_literal_global.1055
Functions:
~ -[CSSearchableItemAttributeSet _getNonNullValueForKey:] : 360 -> 380
~ -[CSSearchableItemAttributeSet attributeIsDelete:] : 484 -> 504
~ -[CSSearchableItemAttributeSet attributeForKey:] : 700 -> 720
~ -[CSSearchableItemCodedArray objectAtIndex:] : 492 -> 512
~ -[CSSearchQuery(CSSearchQueryResultCreation) copyCSSearchableItemWithValues:valueCount:attrKeys:protectionClass:mappingStrategy:attrInfo:requestedAttributeCount:unpackInfo:userFSDomain:] : 1160 -> 1180
~ -[CSLiveFSVolume sendCSLiveFSEvent:] : 2236 -> 2256
~ -[CSAttributeEvaluator evaluateAttribute:ignoreSubtokens:strongCompounds:skipTranscriptions:withFuzzyHandler:] : 692 -> 772
~ -[CSSearchQuery debugDescriptionWithQueryString:] : 728 -> 760

```
