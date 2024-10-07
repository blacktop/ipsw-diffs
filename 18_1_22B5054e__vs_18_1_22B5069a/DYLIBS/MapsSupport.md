## MapsSupport

> `/System/Library/PrivateFrameworks/MapsSupport.framework/MapsSupport`

```diff

-2864.31.7.31.20
-  __TEXT.__text: 0x7d544
+2864.31.7.31.22
+  __TEXT.__text: 0x7e628
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x6f78
+  __TEXT.__objc_methlist: 0x6ff0
   __TEXT.__const: 0x280
-  __TEXT.__cstring: 0x5e63
-  __TEXT.__oslogstring: 0x8012
-  __TEXT.__gcc_except_tab: 0x1324
+  __TEXT.__cstring: 0x5f41
+  __TEXT.__oslogstring: 0x82a6
+  __TEXT.__gcc_except_tab: 0x135c
   __TEXT.__dlopen_cstrs: 0x104
   __TEXT.__ustring: 0x2b2
-  __TEXT.__unwind_info: 0x1db8
+  __TEXT.__unwind_info: 0x1de0
   __TEXT.__objc_classname: 0x12c8
-  __TEXT.__objc_methname: 0x1186f
-  __TEXT.__objc_methtype: 0x34e1
-  __TEXT.__objc_stubs: 0xcc20
+  __TEXT.__objc_methname: 0x1199f
+  __TEXT.__objc_methtype: 0x34a3
+  __TEXT.__objc_stubs: 0xcd20
   __DATA_CONST.__got: 0x6d0
-  __DATA_CONST.__const: 0x2a40
+  __DATA_CONST.__const: 0x2b38
   __DATA_CONST.__objc_classlist: 0x348
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x238
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4110
+  __DATA_CONST.__objc_selrefs: 0x4150
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x350
+  __DATA_CONST.__objc_superrefs: 0x358
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x578
-  __AUTH_CONST.__const: 0xbe0
-  __AUTH_CONST.__cfstring: 0x4360
-  __AUTH_CONST.__objc_const: 0xf940
-  __AUTH_CONST.__objc_intobj: 0x210
+  __AUTH_CONST.__const: 0xc40
+  __AUTH_CONST.__cfstring: 0x43c0
+  __AUTH_CONST.__objc_const: 0xf9a8
+  __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_doubleobj: 0x20
+  __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH.__objc_data: 0x1720
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x4bc
-  __DATA.__data: 0x1d90
+  __DATA.__data: 0x1dc0
   __DATA.__bss: 0x30
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_ivar: 0x35c
+  __DATA_DIRTY.__objc_ivar: 0x36c
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__bss: 0x260

   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2833
-  Symbols:   3360
-  CStrings:  4874
+  Functions: 2848
+  Symbols:   3378
+  CStrings:  4900
 
Symbols:
+ _GEOConfigMSPShareETAMessageQueueBatchSize
+ _GEOConfigMSPShareETAMessageQueueDelayInterval
+ _GEOConfigMSPShareETAMessageQueueInitialInterval
CStrings:
+ "%!l(MISSING)u handles have cached statuses, removing from handles to fetch"
+ "-[MSPSharedTripMessagesCapabilityFetchingQueue _scheduleBatchDelayTimerWithInterval:]_block_invoke"
+ "Filtered out %!l(MISSING)u contacts: %!{(MISSING)private}@"
+ "MSPShareETAMessageQueueBatchSizeKey"
+ "MSPShareETAMessageQueueDelayIntervalKey"
+ "MSPShareETAMessageQueueInitialIntervalKey"
+ "[%!{(MISSING)public}@] - %!{(MISSING)public}@ not permitted for Share ETA"
+ "[%!{(MISSING)public}@] Batch delay timer fired"
+ "[%!{(MISSING)public}@] Cannot notify delegate, %!l(MISSING)fs remaining until permitted"
+ "[%!{(MISSING)public}@] Fetched %!{(MISSING)private}@: %!{(MISSING)public}@@"
+ "[%!{(MISSING)public}@] Fetched service %!{(MISSING)public}@ for %!{(MISSING)private}@"
+ "[%!{(MISSING)public}@] Fetched service %!{(MISSING)public}@ for %!{(MISSING)private}@, but it was no longer in fetch queue, dropping"
+ "[%!{(MISSING)public}@] No more in-flight handles, resetting flags and clearing batch delay timer"
+ "[%!{(MISSING)public}@] Notifying: %!{(MISSING)private}@"
+ "[%!{(MISSING)public}@] Scheduling batch delay for %!l(MISSING)fs"
+ "[%!{(MISSING)public}@] Will fetch best text service for %!{(MISSING)private}@"
+ "[%!{(MISSING)public}@] Will notify delegate, batch reached %!l(MISSING)u items"
+ "[%!{(MISSING)public}@] Will notify delegate, no delay timer"
+ "[%!{(MISSING)public}@] Will notify delegate, no more handles in-flight"
+ "[%!{(MISSING)public}@] requesting %!l(MISSING)u Text Message handles from IDS"
+ "_batchDelayInterval"
+ "_batchDelayTimer"
+ "_batchSize"
+ "_fetchedStatusesByHandle"
+ "_notifyDelegateIfNeeded"
+ "_notifyDelegateNow"
+ "_processFetchedServiceName:forHandle:permittedServiceNames:"
+ "_processFetchedStatus:forHandle:"
+ "_processPendingHandles"
+ "_resetAfterLastHandleFetched"
+ "_resetIfNeeded"
+ "_resolvedStatusForHandle:"
+ "_scheduleBatchDelayTimerWithInterval:"
+ "_shouldPermitFetchingHandle:"
+ "com.apple.Maps.MSPSharedTripCapabilityLevelFetcher"
- "- %!{(MISSING)public}@ not permitted for Share ETA"
- "B32@0:8@\"MSPSharedTripCapabilityFetchingQueue\"16@\"NSString\"24"
- "Fetched service %!{(MISSING)public}@ for %!{(MISSING)private}@"
- "Fetched service %!{(MISSING)public}@ for %!{(MISSING)private}@, but it was no longer in fetch queue, dropping"
- "Will fetch best text service for %!{(MISSING)private}@"
- "capabilityFetchingQueue:shouldFetchHandle:"
- "com.apple.Maps.MSPSharedTripCapabilityFetcher"
- "processPendingHandles"
- "requesting %!l(MISSING)u Text Message handles from IDS"

```
