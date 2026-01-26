## PassKitCore

> `/System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore`

```diff

-1642.4.2.0.0
-  __TEXT.__text: 0x7cc158
+1642.4.3.0.0
+  __TEXT.__text: 0x7cc2a8
   __TEXT.__auth_stubs: 0x4a40
   __TEXT.__objc_methlist: 0x6cb60
   __TEXT.__const: 0x248b8
-  __TEXT.__cstring: 0x6907c
+  __TEXT.__cstring: 0x69115
   __TEXT.__swift5_typeref: 0x597e
   __TEXT.__constg_swiftt: 0x4e34
   __TEXT.__swift5_reflstr: 0x42cd

   __DATA_CONST.__objc_arraydata: 0x27d8
   __AUTH_CONST.__auth_got: 0x2530
   __AUTH_CONST.__const: 0x1e818
-  __AUTH_CONST.__cfstring: 0x71740
+  __AUTH_CONST.__cfstring: 0x71780
   __AUTH_CONST.__objc_const: 0xc41f0
   __AUTH_CONST.__objc_arrayobj: 0xd38
   __AUTH_CONST.__objc_intobj: 0x1080

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2FBAA401-00B9-3C1F-B237-6A76681CCC96
+  UUID: 1846722E-EFCA-3289-9D3E-45810597F05F
   Functions: 49649
   Symbols:   128488
-  CStrings:  67561
+  CStrings:  67565
 
Symbols:
+ ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.411
+ ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.412
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.465
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.467
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.469
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.470
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.466
+ ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.468
+ ___48-[PKMobileAssetManager _purgeAssets:completion:]_block_invoke.472
+ ___68-[PKMobileAssetManager updateCashStickersIfNecessaryWithCompletion:]_block_invoke.433
+ ___74-[PKMobileAssetManager _downloadAsset:isDiscretionary:timeout:completion:]_block_invoke.477
+ ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.452
+ ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.455
+ ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke.437
+ ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke.439
+ ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke.442
+ ___block_literal_global.408
+ ___block_literal_global.451
+ ___block_literal_global.454
+ ___block_literal_global.457
+ ___block_literal_global.459
- ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.402
- ___104-[PKMobileAssetManager dynamicAssetWithIdentifier:mappedIdentifierPrefix:parameters:timeout:completion:]_block_invoke.403
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.456
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.458
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.460
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke.461
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.457
- ___142-[PKMobileAssetManager _retrieveAssetWithQuery:maxCompatibleVersion:isDiscretionary:sortDescriptors:timeout:catalogExpirationDays:completion:]_block_invoke_2.459
- ___48-[PKMobileAssetManager _purgeAssets:completion:]_block_invoke.463
- ___68-[PKMobileAssetManager updateCashStickersIfNecessaryWithCompletion:]_block_invoke.424
- ___74-[PKMobileAssetManager _downloadAsset:isDiscretionary:timeout:completion:]_block_invoke.468
- ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.443
- ___80-[PKMobileAssetManager performScheduledActivityWithIdentifier:activityCriteria:]_block_invoke.446
- ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke.428
- ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke.430
- ___86-[PKMobileAssetManager _downloadPrefetchableAssetsForType:isDiscretionary:completion:]_block_invoke.433
- ___block_literal_global.399
- ___block_literal_global.445
- ___block_literal_global.450
Functions:
~ ___swift_instantiateConcreteTypeFromMangledNameV2 : 72 -> 84
~ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2 : 72 -> 92
~ __PKValidateTopLevelPassStructure : 10604 -> 10836
~ __PKValidateUpcomingPassInformationImagesDict : 1484 -> 1556
CStrings:
+ "entry in URLs array needs to be a dictionary. Found object of class %@."
+ "entry in relevantDates array needs to be a dictionary. Found object of class %@."

```
