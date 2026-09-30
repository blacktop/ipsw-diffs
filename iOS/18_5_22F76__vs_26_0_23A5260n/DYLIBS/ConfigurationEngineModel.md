## ConfigurationEngineModel

> `/System/Library/PrivateFrameworks/ConfigurationEngineModel.framework/ConfigurationEngineModel`

```diff

-221.5.1.0.0
-  __TEXT.__text: 0xb22a4
+239.0.0.0.0
+  __TEXT.__text: 0xb2aa0
   __TEXT.__auth_stubs: 0x350
-  __TEXT.__objc_methlist: 0x15b5c
+  __TEXT.__objc_methlist: 0x15c34
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x94cd
-  __TEXT.__unwind_info: 0x2d28
+  __TEXT.__cstring: 0x94f4
+  __TEXT.__unwind_info: 0x2d40
   __TEXT.__objc_classname: 0x4669
-  __TEXT.__objc_methname: 0x28457
+  __TEXT.__objc_methname: 0x287c6
   __TEXT.__objc_methtype: 0x13ce
-  __TEXT.__objc_stubs: 0x8b60
+  __TEXT.__objc_stubs: 0x8c40
   __DATA_CONST.__got: 0xee0
   __DATA_CONST.__const: 0x1588
   __DATA_CONST.__objc_classlist: 0xe48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f10
+  __DATA_CONST.__objc_selrefs: 0x4f60
   __DATA_CONST.__objc_superrefs: 0x8e0
   __DATA_CONST.__objc_arraydata: 0xb40
   __AUTH_CONST.__auth_got: 0x1b0
-  __AUTH_CONST.__const: 0x1d20
-  __AUTH_CONST.__cfstring: 0xd980
-  __AUTH_CONST.__objc_const: 0x4e3a8
+  __AUTH_CONST.__const: 0x1ea0
+  __AUTH_CONST.__cfstring: 0xd9c0
+  __AUTH_CONST.__objc_const: 0x4e4c8
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_ivar: 0x136c
+  __DATA.__objc_ivar: 0x1384
   __DATA.__data: 0x1e0
   __DATA_DIRTY.__objc_data: 0x8ed0
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 571DFEF9-D3C4-393B-8269-FD76600CF8CA
-  Functions: 7004
-  Symbols:   22626
-  CStrings:  8680
+  UUID: CAF35ABD-F0F9-3B3A-AF1F-ECA3344E2B52
+  Functions: 7034
+  Symbols:   22711
+  CStrings:  8698
 
Symbols:
+ +[CEMPolicyAppDeclaration buildWithIdentifier:withMode:withApps:withExemptApps:]
+ +[CEMPolicyCategoryDeclaration buildWithIdentifier:withMode:withCategories:withCategoriesVersion2:withExemptApps:]
+ +[CEMPolicyWebSiteDeclaration buildWithIdentifier:withMode:withHostnames:withExemptApps:]
+ +[CEMPredicateBudget buildWithCalendarIdentifier:withMonitor:withIdentifiers:withIdentifiersVersion2:withExemptApps:withNotificationTimes:withTimeBudget:]
+ +[CEMPredicateCompositeBudget_Monitors buildWithApps:withWebSites:withCategories:withCategoriesVersion2:withExemptApps:]
+ +[CEMSystemRatingsDeclaration buildWithIdentifier:withRatingRegion:withRatingApps:withRatingMovies:withRatingTVShows:withAllowExplicitContent:withAllowShowingUndownloadedTV:withAllowShowingUndownloadedMovies:withAppsRatingExemptedBundleIDs:]
+ -[CEMPolicyAppDeclaration payloadExemptApps]
+ -[CEMPolicyAppDeclaration setPayloadExemptApps:]
+ -[CEMPolicyCategoryDeclaration payloadExemptApps]
+ -[CEMPolicyCategoryDeclaration setPayloadExemptApps:]
+ -[CEMPolicyWebSiteDeclaration payloadExemptApps]
+ -[CEMPolicyWebSiteDeclaration setPayloadExemptApps:]
+ -[CEMPredicateBudget payloadExemptApps]
+ -[CEMPredicateBudget setPayloadExemptApps:]
+ -[CEMPredicateCompositeBudget_Monitors payloadExemptApps]
+ -[CEMPredicateCompositeBudget_Monitors setPayloadExemptApps:]
+ -[CEMSystemRatingsDeclaration payloadAppsRatingExemptedBundleIDs]
+ -[CEMSystemRatingsDeclaration setPayloadAppsRatingExemptedBundleIDs:]
+ _OBJC_IVAR_$_CEMPolicyAppDeclaration._payloadExemptApps
+ _OBJC_IVAR_$_CEMPolicyCategoryDeclaration._payloadExemptApps
+ _OBJC_IVAR_$_CEMPolicyWebSiteDeclaration._payloadExemptApps
+ _OBJC_IVAR_$_CEMPredicateBudget._payloadExemptApps
+ _OBJC_IVAR_$_CEMPredicateCompositeBudget_Monitors._payloadExemptApps
+ _OBJC_IVAR_$_CEMSystemRatingsDeclaration._payloadAppsRatingExemptedBundleIDs
+ ___40-[CEMPredicateBudget loadPayload:error:]_block_invoke_4
+ ___45-[CEMPolicyAppDeclaration loadPayload:error:]_block_invoke_2
+ ___49-[CEMPolicyWebSiteDeclaration loadPayload:error:]_block_invoke_2
+ ___49-[CEMSystemRatingsDeclaration loadPayload:error:]_block_invoke
+ ___50-[CEMPolicyCategoryDeclaration loadPayload:error:]_block_invoke_3
+ ___57-[CEMPredicateBudget serializePayloadWithAssetProviders:]_block_invoke_5
+ ___58-[CEMPredicateCompositeBudget_Monitors loadPayload:error:]_block_invoke_5
+ ___62-[CEMPolicyAppDeclaration serializePayloadWithAssetProviders:]_block_invoke_2
+ ___66-[CEMPolicyWebSiteDeclaration serializePayloadWithAssetProviders:]_block_invoke_2
+ ___66-[CEMSystemRatingsDeclaration serializePayloadWithAssetProviders:]_block_invoke
+ ___67-[CEMPolicyCategoryDeclaration serializePayloadWithAssetProviders:]_block_invoke_3
+ ___75-[CEMPredicateCompositeBudget_Monitors serializePayloadWithAssetProviders:]_block_invoke_5
+ ___block_literal_global.101
+ ___block_literal_global.184
+ ___block_literal_global.186
+ ___block_literal_global.188
+ ___block_literal_global.190
+ ___block_literal_global.192
+ ___block_literal_global.194
+ ___block_literal_global.196
+ ___block_literal_global.198
+ ___block_literal_global.200
+ ___block_literal_global.219
+ ___block_literal_global.221
+ ___block_literal_global.243
+ ___block_literal_global.245
+ ___block_literal_global.47
+ ___block_literal_global.49
+ ___block_literal_global.51
+ ___block_literal_global.91
+ ___block_literal_global.93
+ ___block_literal_global.95
+ _objc_msgSend$buildWithApps:withWebSites:withCategories:withCategoriesVersion2:withExemptApps:
+ _objc_msgSend$buildWithCalendarIdentifier:withMonitor:withIdentifiers:withIdentifiersVersion2:withExemptApps:withNotificationTimes:withTimeBudget:
+ _objc_msgSend$buildWithIdentifier:withMode:withApps:withExemptApps:
+ _objc_msgSend$buildWithIdentifier:withMode:withCategories:withCategoriesVersion2:withExemptApps:
+ _objc_msgSend$buildWithIdentifier:withMode:withHostnames:withExemptApps:
+ _objc_msgSend$setPayloadAppsRatingExemptedBundleIDs:
+ _objc_msgSend$setPayloadExemptApps:
- ___block_literal_global.100
- ___block_literal_global.178
- ___block_literal_global.189
- ___block_literal_global.191
- ___block_literal_global.193
- ___block_literal_global.205
- ___block_literal_global.207
- ___block_literal_global.229
- ___block_literal_global.231
- ___block_literal_global.90
- ___block_literal_global.96
- ___block_literal_global.98
CStrings:
+ "ExemptApps"
+ "T@\"NSArray\",C,N,V_payloadAppsRatingExemptedBundleIDs"
+ "T@\"NSArray\",C,N,V_payloadExemptApps"
+ "_payloadAppsRatingExemptedBundleIDs"
+ "_payloadExemptApps"
+ "appsRatingExemptedBundleIDs"
+ "buildWithApps:withWebSites:withCategories:withCategoriesVersion2:withExemptApps:"
+ "buildWithCalendarIdentifier:withMonitor:withIdentifiers:withIdentifiersVersion2:withExemptApps:withNotificationTimes:withTimeBudget:"
+ "buildWithIdentifier:withMode:withApps:withExemptApps:"
+ "buildWithIdentifier:withMode:withCategories:withCategoriesVersion2:withExemptApps:"
+ "buildWithIdentifier:withMode:withHostnames:withExemptApps:"
+ "buildWithIdentifier:withRatingRegion:withRatingApps:withRatingMovies:withRatingTVShows:withAllowExplicitContent:withAllowShowingUndownloadedTV:withAllowShowingUndownloadedMovies:withAppsRatingExemptedBundleIDs:"
+ "payloadAppsRatingExemptedBundleIDs"
+ "payloadExemptApps"
+ "setPayloadAppsRatingExemptedBundleIDs:"
+ "setPayloadExemptApps:"

```
