## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-2964.40.20.502.2
-  __TEXT.__text: 0x1beae8
+2964.40.30.0.0
+  __TEXT.__text: 0x1bfc40
   __TEXT.__auth_stubs: 0x1b90
-  __TEXT.__objc_methlist: 0xead8
+  __TEXT.__objc_methlist: 0xeb58
   __TEXT.__const: 0x6a8
-  __TEXT.__cstring: 0x231b5
+  __TEXT.__cstring: 0x231da
   __TEXT.__oslogstring: 0x12926
   __TEXT.__gcc_except_tab: 0x2644
   __TEXT.__ustring: 0x10
   __TEXT.__unwind_info: 0x3700
-  __TEXT.__objc_classname: 0xc15
-  __TEXT.__objc_methname: 0x31520
+  __TEXT.__objc_classname: 0xc17
+  __TEXT.__objc_methname: 0x31710
   __TEXT.__objc_methtype: 0x27d0
-  __TEXT.__objc_stubs: 0x1eb60
+  __TEXT.__objc_stubs: 0x1ec60
   __DATA_CONST.__got: 0xea8
   __DATA_CONST.__const: 0x43a8
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x98d8
+  __DATA_CONST.__objc_selrefs: 0x9928
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x288
-  __DATA_CONST.__objc_arraydata: 0x14990
+  __DATA_CONST.__objc_arraydata: 0x14b20
   __AUTH_CONST.__auth_got: 0xde0
   __AUTH_CONST.__const: 0x1880
   __AUTH_CONST.__cfstring: 0x31100
-  __AUTH_CONST.__objc_const: 0x12908
-  __AUTH_CONST.__objc_intobj: 0x2778
-  __AUTH_CONST.__objc_dictobj: 0x3430
-  __AUTH_CONST.__objc_doubleobj: 0xb60
-  __AUTH_CONST.__objc_arrayobj: 0x2b50
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x127c
+  __AUTH_CONST.__objc_const: 0x129c8
+  __AUTH_CONST.__objc_intobj: 0x27d8
+  __AUTH_CONST.__objc_dictobj: 0x3480
+  __AUTH_CONST.__objc_doubleobj: 0xb90
+  __AUTH_CONST.__objc_arrayobj: 0x2b80
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x128c
   __DATA.__data: 0x400
-  __DATA.__bss: 0x2358
+  __DATA.__bss: 0x2340
   __DATA.__common: 0x74
-  __DATA_DIRTY.__objc_data: 0x15e0
+  __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x388
+  __DATA_DIRTY.__bss: 0x3a0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6D3072F5-A6FD-3523-8EF5-B231997B9B0D
-  Functions: 7824
-  Symbols:   26494
-  CStrings:  22273
+  UUID: 35920AB6-EE78-3406-92D4-964460F4866A
+  Functions: 7834
+  Symbols:   26526
+  CStrings:  22292
 
Symbols:
+ -[PLBatteryUIDrainDateInterval appBreakdown]
+ -[PLBatteryUIDrainDateInterval initWithStartDate:endDate:accumulatedDrain:sortedAppList:appBreakdown:]
+ -[PLBatteryUIDrainDateInterval setAppBreakdown:]
+ -[PLBatteryUIDrainDateInterval setSortedAppList:]
+ -[PLBatteryUIDrainDateInterval sortedAppList]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary breakdownFromCache]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary dynamicBreakdownFromCache]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getAnomalousAppsForTargetComparison:comparedTo:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setBreakdownFromCache:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setDynamicBreakdownFromCache:]
+ _OBJC_IVAR_$_PLBatteryUIDrainDateInterval._appBreakdown
+ _OBJC_IVAR_$_PLBatteryUIDrainDateInterval._sortedAppList
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._breakdownFromCache
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._dynamicBreakdownFromCache
+ ___76-[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap]_block_invoke.332
+ ___block_literal_global.358
+ ___block_literal_global.399
+ _getBundleIDToDisplayNameMap.classDebugEnabled.331
+ _getBundleIDToDisplayNameMap.defaultOnce.330
+ _objc_msgSend$appBreakdown
+ _objc_msgSend$breakdownFromCache
+ _objc_msgSend$dynamicBreakdownFromCache
+ _objc_msgSend$getAnomalousAppsForTargetComparison:comparedTo:
+ _objc_msgSend$initWithStartDate:endDate:accumulatedDrain:sortedAppList:appBreakdown:
+ _objc_msgSend$setAppBreakdown:
+ _objc_msgSend$setSortedAppList:
+ _objc_msgSend$sortedAppList
- ___76-[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap]_block_invoke.213
- ___block_literal_global.239
- _getBundleIDToDisplayNameMap.classDebugEnabled.212
- _getBundleIDToDisplayNameMap.defaultOnce.211
CStrings:
+ "T@\"NSArray\",&,V_breakdownFromCache"
+ "T@\"NSArray\",&,V_dynamicBreakdownFromCache"
+ "T@\"NSArray\",&,V_sortedAppList"
+ "T@\"NSDictionary\",&,V_appBreakdown"
+ "_appBreakdown"
+ "_breakdownFromCache"
+ "_dynamicBreakdownFromCache"
+ "_sortedAppList"
+ "appBreakdown"
+ "breakdownFromCache"
+ "drain_comparison_breakdown_dependent"
+ "dynamicBreakdownFromCache"
+ "getAnomalousAppsForTargetComparison:comparedTo:"
+ "initWithStartDate:endDate:accumulatedDrain:sortedAppList:appBreakdown:"
+ "setAppBreakdown:"
+ "setBreakdownFromCache:"
+ "setDynamicBreakdownFromCache:"
+ "setSortedAppList:"
+ "sortedAppList"

```
