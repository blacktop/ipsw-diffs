## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1061.0.0.0.0
-  __TEXT.__text: 0x5ec628
+1062.0.1.0.0
+  __TEXT.__text: 0x5ec8ec
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x31020
+  __TEXT.__objc_methlist: 0x31030
   __TEXT.__const: 0x4640
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x762a0
-  __TEXT.__cstring: 0x45352
+  __TEXT.__oslogstring: 0x7630c
+  __TEXT.__cstring: 0x4538e
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c

   __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x28a28
   __TEXT.__ustring: 0x1e
-  __TEXT.__unwind_info: 0xdc58
+  __TEXT.__unwind_info: 0xdc50
   __TEXT.__eh_frame: 0x390
-  __TEXT.__objc_classname: 0x58c9
-  __TEXT.__objc_methname: 0x91589
-  __TEXT.__objc_methtype: 0xcf8a
-  __TEXT.__objc_stubs: 0x55a60
+  __TEXT.__objc_classname: 0x58ca
+  __TEXT.__objc_methname: 0x915ca
+  __TEXT.__objc_methtype: 0xcf9f
+  __TEXT.__objc_stubs: 0x55a80
   __DATA_CONST.__got: 0x30f0
   __DATA_CONST.__const: 0xf4f8
   __DATA_CONST.__objc_classlist: 0x1548
   __DATA_CONST.__objc_catlist: 0x3a8
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19418
+  __DATA_CONST.__objc_selrefs: 0x19420
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x1198
-  __DATA_CONST.__objc_arraydata: 0x2a08
+  __DATA_CONST.__objc_arraydata: 0x2a00
   __AUTH_CONST.__auth_got: 0x10d8
   __AUTH_CONST.__const: 0x3260
-  __AUTH_CONST.__cfstring: 0x287e0
-  __AUTH_CONST.__objc_const: 0x50a70
+  __AUTH_CONST.__cfstring: 0x28800
+  __AUTH_CONST.__objc_const: 0x50a60
   __AUTH_CONST.__objc_intobj: 0x4608
   __AUTH_CONST.__objc_arrayobj: 0xe70
   __AUTH_CONST.__objc_doubleobj: 0xb00
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH.__objc_data: 0x2208
+  __AUTH.__objc_data: 0x2258
   __DATA.__objc_ivar: 0x2584
   __DATA.__data: 0x2cc0
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_ivar: 0x1158
-  __DATA_DIRTY.__objc_data: 0xb380
+  __DATA_DIRTY.__objc_data: 0xb330
   __DATA_DIRTY.__data: 0x5c8
   __DATA_DIRTY.__bss: 0x200
   __DATA_DIRTY.__common: 0x8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 488B7418-652E-3101-ACD3-DDFEFCF74E59
-  Functions: 20178
-  Symbols:   65148
-  CStrings:  40135
+  UUID: A1CFFE5C-96C1-3E66-82E1-265D106754F2
+  Functions: 20179
+  Symbols:   65151
+  CStrings:  40140
 
Symbols:
+ +[RTTripClusterRoadTransitionsData2MO managedObjectWithTripClusterRoadTransitions:inManagedObjectContext:]
+ +[RTTripClusterRoadTransitionsData2MO(CoreDataProperties) fetchRequest]
+ -[RTPersistenceMirroringManager _changeCountForManagedObjectContext:currentExporterToken:excludeImport:error:]
+ -[RTPersistenceMirroringManager _createHistoryChangeRequestWithManagedObjectContext:currentExporterToken:excludeImport:store:]
+ _OBJC_CLASS_$_RTTripClusterRoadTransitionsData2MO
+ _OBJC_METACLASS_$_RTTripClusterRoadTransitionsData2MO
+ __OBJC_$_CLASS_METHODS_RTTripClusterRoadTransitionsData2MO(CoreDataProperties)
+ __OBJC_CLASS_RO_$_RTTripClusterRoadTransitionsData2MO
+ __OBJC_METACLASS_RO_$_RTTripClusterRoadTransitionsData2MO
+ ___229-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]_block_invoke.287
+ ___78-[RTTripClusterProcessor getSimulatedLocationOnRoute:convertedRoutes:cluster:]_block_invoke.255
+ ___block_literal_global.254
+ ___block_literal_global.260
+ ___block_literal_global.265
+ _objc_msgSend$_changeCountForManagedObjectContext:currentExporterToken:excludeImport:error:
+ _objc_msgSend$_createHistoryChangeRequestWithManagedObjectContext:currentExporterToken:excludeImport:store:
- +[RTTripClusterRoadTransitionsDataMO managedObjectWithTripClusterRoadTransitions:inManagedObjectContext:]
- +[RTTripClusterRoadTransitionsDataMO(CoreDataProperties) fetchRequest]
- -[RTPersistenceMirroringManager changeCountForManagedObjectContext:currentExporterToken:changeRequestError:]
- GCC_except_table113
- _OBJC_CLASS_$_RTTripClusterRoadTransitionsDataMO
- _OBJC_METACLASS_$_RTTripClusterRoadTransitionsDataMO
- __OBJC_$_CLASS_METHODS_RTTripClusterRoadTransitionsDataMO(CoreDataProperties)
- __OBJC_CLASS_RO_$_RTTripClusterRoadTransitionsDataMO
- __OBJC_METACLASS_RO_$_RTTripClusterRoadTransitionsDataMO
- ___229-[RTTripClusterProcessor updateClusterRouteUsingClusterRoadTransitionsWithClusterID:tripClusterStore:tripClusterRouteStore:tripClusterWaypointStore:tripClusterRouteTransitionsStore:startLat:startLon:endLat:endLon:traversalCount:]_block_invoke.289
- ___78-[RTTripClusterProcessor getSimulatedLocationOnRoute:convertedRoutes:cluster:]_block_invoke.256
- ___block_literal_global.261
- ___block_literal_global.266
- _objc_msgSend$changeCountForManagedObjectContext:currentExporterToken:changeRequestError:
CStrings:
+ "%@, Road transitions exist in the local for clusterID,%@,continuing with DTW attempt"
+ "%@, Road transitions not found in the local for clusterID,%@,skipping this cluster for DTW attempt"
+ "%@, failed to create transactionrequest"
+ "%@, failed to extract transactions, error, %@"
+ "%@, invalid inputs, managedObjectContext, %@, store, %@"
+ "%@, transactionRequest, %@, transactionRequest.fetchRequest, %@, change count, %lu"
+ "02:51:52"
+ "Aug  5 2025"
+ "NSCloudKitMirroringDelegate.import"
+ "Q44@0:8@16@24B32^@36"
+ "RTTripClusterRoadTransitionsData2MO"
+ "Total change count from all authors, %lu"
+ "_changeCountForManagedObjectContext:currentExporterToken:excludeImport:error:"
+ "_createHistoryChangeRequestWithManagedObjectContext:currentExporterToken:excludeImport:store:"
- "%@, Road transitions exist in the cloud for clusterID,%@,continuing with DTW attempt"
- "%@, Road transitions not found in the cloud for clusterID,%@,skipping this cluster for DTW attempt"
- "%@, request, %@, change count, %@, error, %@"
- "%@,%@,Distance between origins,%{public}.3lf,destinations,%{public}.3lf"
- "05:39:03"
- "Change count, %@"
- "Jul 26 2025"
- "RTTripClusterRoadTransitionsDataMO"
- "changeCountForManagedObjectContext:currentExporterToken:changeRequestError:"
- "tripClusterRoadTransitionsData"

```
