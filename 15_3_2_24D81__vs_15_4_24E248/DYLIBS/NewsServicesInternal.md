## NewsServicesInternal

> `/System/iOSSupport/System/Library/PrivateFrameworks/NewsServicesInternal.framework/Versions/A/NewsServicesInternal`

```diff

-5626.0.0.0.0
-  __TEXT.__text: 0xb554
+5676.0.3.0.0
+  __TEXT.__text: 0xba98
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0xad8
+  __TEXT.__objc_methlist: 0xcb4
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x1954
+  __TEXT.__cstring: 0x1a06
   __TEXT.__oslogstring: 0xd3
   __TEXT.__gcc_except_tab: 0x98
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0x370
+  __TEXT.__unwind_info: 0x380
   __TEXT.__objc_classname: 0x279
-  __TEXT.__objc_methname: 0x2b44
+  __TEXT.__objc_methname: 0x2bca
   __TEXT.__objc_methtype: 0x4e5
   __TEXT.__objc_stubs: 0x2740
   __DATA_CONST.__got: 0x1d0
-  __DATA_CONST.__const: 0x550
+  __DATA_CONST.__const: 0x580
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc58
+  __DATA_CONST.__objc_selrefs: 0xd20
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x248
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x1360
-  __AUTH_CONST.__objc_const: 0x1a90
+  __AUTH_CONST.__cfstring: 0x1440
+  __AUTH_CONST.__objc_const: 0x17b0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x30

   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6FA1B07D-0555-3B3A-A54C-E2CBB33435FB
-  Functions: 318
-  Symbols:   1129
-  CStrings:  998
+  UUID: AB51A1DC-1377-334D-933F-ECE36139A7A7
+  Functions: 326
+  Symbols:   1144
+  CStrings:  1019
 
Symbols:
+ +[NSURL(NSSAdditions) nss_NewsURLForFood]
+ +[NSURL(NSSAdditions) nss_NewsURLForRecipeBox]
+ +[NSURL(NSSAdditions) nss_NewsURLForRecipeCatalog:]
+ +[NSURL(NSSAdditions) nss_NewsURLForRecipeCatalog]
+ +[NSURL(NSSAdditions) nss_NewsURLForRecipeID:articleID:]
+ +[NSURL(NSSAdditions) nss_NewsURLForRecipeID:articleID:].cold.1
+ +[NSURL(NSSAdditions) nss_NewsURLForRecipeID:articleID:].cold.2
+ NSSBundleInternal.cold.1
+ NSSNewsAnalyticsPBEventAccumulatorLog.cold.1
+ _NSSArticleIDQueryName
+ _NSSNewsFoodComponnent
+ _NSSNewsRecipeBoxComponent
+ _NSSNewsRecipeCatalogComponent
+ _NSSRecipeCatalogSearchFilterQueryName
+ _NSSRecipeCatalogSearchQueryName
CStrings:
+ "+[NSURL(NSSAdditions) nss_NewsURLForRecipeID:articleID:]"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSExternalAnalyticsEvent.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSNewsAnalyticsPBEventAccumulator.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSNewsAnalyticsSubmitEnvelopesOperation.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSNewsAnalyticsUtilities.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSNewsDataDestruction.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSNewsTermination.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSURL+NSSAdditions.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/NTPBNewsAnalytics+NSSAdditions.m"
+ "article_id"
+ "filter_tags"
+ "food"
+ "nss_NewsURLForFood"
+ "nss_NewsURLForRecipeBox"
+ "nss_NewsURLForRecipeCatalog"
+ "nss_NewsURLForRecipeCatalog:"
+ "nss_NewsURLForRecipeID:articleID:"
+ "recipe IDs with slashes won't be handled properly"
+ "recipeID != nil"
+ "recipes"
+ "savedRecipes"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSExternalAnalyticsEvent.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSNewsAnalyticsPBEventAccumulator.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSNewsAnalyticsSubmitEnvelopesOperation.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSNewsAnalyticsUtilities.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSNewsDataDestruction.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSSNewsTermination.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/Frameworks/NewsServicesInternal/NSURL+NSSAdditions.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/feldspar/NTPBNewsAnalytics+NSSAdditions.m"

```
