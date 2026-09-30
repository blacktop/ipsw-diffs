## SpotlightDaemon

> `/System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon`

```diff

-2333.56.0.0.0
-  __TEXT.__text: 0xa3ec8
+2333.57.1.0.0
+  __TEXT.__text: 0xa4038
   __TEXT.__auth_stubs: 0x1e10
   __TEXT.__objc_methlist: 0x3fc4
   __TEXT.__const: 0x378
   __TEXT.__cstring: 0x7c25
-  __TEXT.__oslogstring: 0xa18b
+  __TEXT.__oslogstring: 0xa18e
   __TEXT.__gcc_except_tab: 0x4168
   __TEXT.__dlopen_cstrs: 0x4a
   __TEXT.__unwind_info: 0x21b0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  UUID: 25903C82-B049-3801-9365-9CBA7BCA756D
+  UUID: 681369B5-C0F5-36D1-9575-1BCCDFF17393
   Functions: 2683
   Symbols:   9169
   CStrings:  5524
Functions:
~ -[SPCoreSpotlightIndexer indexSearchableItems:deleteSearchableItemsWithIdentifiers:clientState:expectedClientState:clientStateName:protectionClass:forBundleID:options:completionHandler:] : 788 -> 800
~ -[SPCoreSpotlightIndexer clientDidCheckin:protectionClass:service:completionHandler:] : 640 -> 660
~ -[SPCoreSpotlightIndexer fetchLastClientStateWithProtectionClass:forBundleID:clientStateName:options:completionHandler:] : 284 -> 304
~ -[SPCoreSpotlightIndexer indexFromBundle:protectionClass:personaID:options:items:itemsText:itemsHTML:clientState:expectedClientState:clientStateName:deletes:canCreateNewIndex:completionHandler:] : 864 -> 884
~ -[SPCoreSpotlightIndexer deleteSearchableItemsWithDomainIdentifiers:protectionClass:forBundleID:fromClient:options:completionHandler:] : 308 -> 328
~ -[SPCoreSpotlightIndexer _issueCommand:outFileDescriptor:searchContext:completionHandler:] : 19376 -> 19396
~ -[SPConcreteCoreSpotlightIndexer openIndex:shouldReindexAll:readOnly:forcePC:] : 8724 -> 8704
~ -[SPCoreSpotlightIndexer prepareIndexingWhileLocked:protectionClass:holdAssertionFor:completionHandler:] : 244 -> 264
~ -[SPCoreSpotlightIndexer finishIndexingWhileLocked:protectionClass:completionHandler:] : 244 -> 264
~ -[SPCoreSpotlightIndexer deleteAllSearchableItemsWithBundleID:fromClient:protectionClass:shouldGC:completionHandler:] : 852 -> 872
~ -[SPCoreSpotlightIndexer deleteSearchableItemsSinceDate:protectionClass:forBundleID:options:completionHandler:] : 284 -> 304
~ -[SPCoreSpotlightIndexer changeStateOfSearchableItemsWithUIDs:toState:protectionClass:forBundleID:forUTIType:options:] : 200 -> 220
~ -[SPCoreSpotlightIndexer userPerformedAction:withItem:protectionClass:forBundleID:personaID:] : 1184 -> 1204
~ -[SPCoreSpotlightIndexer willModifySearchableItemsWithIdentifiers:protectionClass:forBundleID:options:completionHandler:] : 376 -> 396
~ -[SPCoreSpotlightIndexer _issueCacheCommand:xpc:searchContext:completionHandler:] : 2048 -> 2124
~ -[SPCoreSpotlightIndexer fetchAttributes:protectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:] : 500 -> 520
~ -[SPCoreSpotlightIndexer fetchAttributesForProtectionClass:attributes:bundleID:identifiers:userCtx:flags:completion:] : 492 -> 512
~ -[SPCoreSpotlightIndexer fetchCacheFileDescriptorsForProtectionClass:bundleID:identifiers:userCtx:flags:qos:completionHandler:] : 468 -> 488
CStrings:
+ "(%@) deleteActivities, options:0x%lx"
+ "(%@) deleteAllActivities, options:0x%lx"
+ "2333.57.1"
+ "Complete will modify fixup query for bundleID:%@ pc: %@"
+ "com.apple.spotlight.mds-import"
+ "com.apple.spotlight.thermals"
- "(%@) deleteActivties, options:0x%lx"
- "(%@) deleteAllActivties, options:0x%lx"
- "2333.56"
- "Complete wil modify fixup query for bundleID:%@ pc: %@"
- "com.appple.spotlight.mds-import"
- "com.appple.spotlight.thermals"

```
