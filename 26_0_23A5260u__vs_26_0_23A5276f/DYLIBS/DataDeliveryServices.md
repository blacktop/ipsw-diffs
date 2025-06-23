## DataDeliveryServices

> `/System/Library/PrivateFrameworks/DataDeliveryServices.framework/DataDeliveryServices`

```diff

-93.0.0.0.0
+95.0.0.0.0
   __TEXT.__text: 0x23d90
   __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_methlist: 0x2564
   __TEXT.__const: 0x168
   __TEXT.__gcc_except_tab: 0x6f0
-  __TEXT.__cstring: 0x1230
+  __TEXT.__cstring: 0x1232
   __TEXT.__oslogstring: 0x2dfb
   __TEXT.__unwind_info: 0xa80
   __TEXT.__objc_classname: 0x4ba

   __DATA_DIRTY.__bss: 0xe8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
-  - /System/Library/PrivateFrameworks/BackgroundTaskAgent.framework/BackgroundTaskAgent
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/Trial.framework/Trial

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 11F808EB-D117-3CE3-B51E-DE510EFA5345
+  UUID: ABB0C956-EBF2-308D-9BC8-65B1753BAA9F
   Functions: 878
   Symbols:   3438
   CStrings:  1705
Symbols:
+ -[DDSMobileAssetv2Provider assetsInCatalogForQuery:errorPtr:]
+ -[DDSMobileAssetv2Provider assetsInCatalogForQuery:errorPtr:].cold.1
+ -[DDSMobileAssetv2Provider assetsInCatalogForQuery:errorPtr:].cold.2
+ -[DDSMobileAssetv2Provider assetsInCatalogForQuery:errorPtr:].cold.3
+ -[DDSMobileAssetv2Provider assetsInCatalogForQuery:errorPtr:].cold.4
+ -[DDSMobileAssetv2Provider assetsInCatalogForQuery:errorPtr:].cold.5
+ -[DDSMobileAssetv2Provider compatibilityVersionByAssetType]
+ _OBJC_IVAR_$_DDSMobileAssetv2Provider._compatibilityVersionByAssetType
+ _objc_msgSend$assetsInCatalogForQuery:errorPtr:
+ _objc_msgSend$compatibilityVersionByAssetType
- -[DDSMobileAssetv2Provider assetsInCalalogForQuery:errorPtr:]
- -[DDSMobileAssetv2Provider assetsInCalalogForQuery:errorPtr:].cold.1
- -[DDSMobileAssetv2Provider assetsInCalalogForQuery:errorPtr:].cold.2
- -[DDSMobileAssetv2Provider assetsInCalalogForQuery:errorPtr:].cold.3
- -[DDSMobileAssetv2Provider assetsInCalalogForQuery:errorPtr:].cold.4
- -[DDSMobileAssetv2Provider assetsInCalalogForQuery:errorPtr:].cold.5
- -[DDSMobileAssetv2Provider compatabilityVersionByAssetType]
- _OBJC_IVAR_$_DDSMobileAssetv2Provider._compatabilityVersionByAssetType
- _objc_msgSend$assetsInCalalogForQuery:errorPtr:
- _objc_msgSend$compatabilityVersionByAssetType
CStrings:
+ "-[DDSMobileAssetv2Provider assetsInCatalogForQuery:errorPtr:]"
+ "Cannot accept the new update request for an asset as update is already in progress"
+ "Missing compatibility version for asset type: %@"
+ "T@\"NSMutableDictionary\",R,N,V_compatibilityVersionByAssetType"
+ "Unable to fetch the update status as catalog update is failed"
+ "_compatibilityVersionByAssetType"
+ "assetsInCatalogForQuery:errorPtr:"
+ "compatibilityVersionByAssetType"
- "-[DDSMobileAssetv2Provider assetsInCalalogForQuery:errorPtr:]"
- "Cannot accept the new update request for an asset as update is already in progess"
- "Missing compatability version for asset type: %@"
- "T@\"NSMutableDictionary\",R,N,V_compatabilityVersionByAssetType"
- "Unable to fetch the update status as catlog update is failed"
- "_compatabilityVersionByAssetType"
- "assetsInCalalogForQuery:errorPtr:"
- "compatabilityVersionByAssetType"

```
