## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`

```diff

-795.21.4.2.0
-  __TEXT.__text: 0x14c54c
+795.21.4.3.0
+  __TEXT.__text: 0x14cb10
   __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_methlist: 0xfe28
+  __TEXT.__objc_methlist: 0xfe38
   __TEXT.__const: 0x390
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0x138b5
-  __TEXT.__oslogstring: 0x1061a
+  __TEXT.__cstring: 0x13934
+  __TEXT.__oslogstring: 0x1076c
   __TEXT.__constg_swiftt: 0x1e0
   __TEXT.__swift5_typeref: 0x145
   __TEXT.__swift5_reflstr: 0xb1
   __TEXT.__swift5_fieldmd: 0x88
   __TEXT.__swift5_capture: 0x1b0
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x3030
-  __TEXT.__unwind_info: 0x3010
+  __TEXT.__gcc_except_tab: 0x3048
+  __TEXT.__unwind_info: 0x3018
   __TEXT.__eh_frame: 0x398
   __TEXT.__objc_classname: 0xf79
-  __TEXT.__objc_methname: 0x2106b
+  __TEXT.__objc_methname: 0x2109b
   __TEXT.__objc_methtype: 0x3fb4
-  __TEXT.__objc_stubs: 0xe360
+  __TEXT.__objc_stubs: 0xe3a0
   __DATA_CONST.__got: 0x7a0
   __DATA_CONST.__const: 0x2118
   __DATA_CONST.__objc_classlist: 0x438
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x87e0
+  __DATA_CONST.__objc_selrefs: 0x87f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x318
   __DATA_CONST.__objc_arraydata: 0x8e0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 9C99C309-DC12-3550-A558-969AA7358C8B
-  Functions: 5882
-  Symbols:   16205
-  CStrings:  12580
+  UUID: A6D5EB72-A5BB-33E9-8287-7A56DDC60F66
+  Functions: 5884
+  Symbols:   16211
+  CStrings:  12590
 
Symbols:
+ -[WAPersistentContainer pruneFailedRoamEventsWithError:]
+ GCC_except_table124
+ GCC_except_table126
+ GCC_except_table138
+ GCC_except_table145
+ GCC_except_table84
+ ___47-[WAPersistentContainer batchDelete:withError:]_block_invoke.345
+ ___56-[AnalyticsProcessor processDeferredPoliciesWithReason:]_block_invoke.245
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$pruneFailedRoamEventsWithError:
- GCC_except_table125
- GCC_except_table129
- GCC_except_table144
- ___47-[WAPersistentContainer batchDelete:withError:]_block_invoke.341
- ___block_literal_global.253
Functions:
~ -[AnalyticsProcessor processDeferredPoliciesWithReason:] : 1796 -> 1924
~ ___56-[AnalyticsProcessor processDeferredPoliciesWithReason:]_block_invoke : 104 -> 404
+ ___56-[AnalyticsProcessor processDeferredPoliciesWithReason:]_block_invoke_3
+ -[WAPersistentContainer pruneFailedRoamEventsWithError:]
~ +[WAMigrationUtils modelWithHash:withError:] : 892 -> 1068
~ -[WAEventRoamStatus processEventOnPersistentContainer:andRunPostprocessing:withError:] : 4200 -> 4344
CStrings:
+ "%{public}s::%d:Found matching on-disk model: %@ with %@"
+ "%{public}s::%d:Pruned %lu failed roam events"
+ "%{public}s::%d:Skipping roam failure event (status: %d)"
+ "%{public}s::%d:pruneFailedRoamEvents error: %@"
+ "%{public}s::%d:pruneFailedRoamEvents: currentSize=%lluKB maxSize=%lluKB"
+ "%{public}s::%d:pruneFailedRoamEvents: pruned %lu records (%@)"
+ "-[AnalyticsProcessor processDeferredPoliciesWithReason:]_block_invoke"
+ "-[WAPersistentContainer pruneFailedRoamEventsWithError:]"
+ "WiFiAnalytics-795.21.4.3 Mar  6 2026 18:33:20"
+ "lastPathComponent"
+ "pruneFailedRoamEventsWithError:"
- "WiFiAnalytics-795.21.4.2 Mar  3 2026 23:20:46"

```
