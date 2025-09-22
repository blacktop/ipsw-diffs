## WiFiAnalytics

> `/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`

```diff

-776.90.4.2.0
-  __TEXT.__text: 0x12d674
+785.10.0.0.0
+  __TEXT.__text: 0x12eb7c
   __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0xf1e8
+  __TEXT.__objc_methlist: 0xf2f0
   __TEXT.__const: 0x310
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__cstring: 0x11fdf
-  __TEXT.__oslogstring: 0xe59c
+  __TEXT.__cstring: 0x1218f
+  __TEXT.__oslogstring: 0xe823
   __TEXT.__constg_swiftt: 0x1e0
   __TEXT.__swift5_typeref: 0x14b
   __TEXT.__swift5_reflstr: 0xb1
   __TEXT.__swift5_fieldmd: 0x88
   __TEXT.__swift5_capture: 0x2d0
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0x2cc8
-  __TEXT.__unwind_info: 0x26a8
+  __TEXT.__gcc_except_tab: 0x2d88
+  __TEXT.__unwind_info: 0x26e0
   __TEXT.__eh_frame: 0x548
-  __TEXT.__objc_classname: 0xe8c
-  __TEXT.__objc_methname: 0x1f354
-  __TEXT.__objc_methtype: 0x3df0
-  __TEXT.__objc_stubs: 0xcb40
-  __DATA_CONST.__got: 0x728
-  __DATA_CONST.__const: 0x1ed8
-  __DATA_CONST.__objc_classlist: 0x3e8
+  __TEXT.__objc_classname: 0xec1
+  __TEXT.__objc_methname: 0x1f539
+  __TEXT.__objc_methtype: 0x3e14
+  __TEXT.__objc_stubs: 0xcd00
+  __DATA_CONST.__got: 0x740
+  __DATA_CONST.__const: 0x1f00
+  __DATA_CONST.__objc_classlist: 0x400
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8198
+  __DATA_CONST.__objc_selrefs: 0x8210
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_superrefs: 0x2d8
   __DATA_CONST.__objc_arraydata: 0x490
   __AUTH_CONST.__auth_got: 0x828
   __AUTH_CONST.__const: 0x1670
-  __AUTH_CONST.__cfstring: 0xd360
-  __AUTH_CONST.__objc_const: 0x14f80
-  __AUTH_CONST.__objc_intobj: 0x258
+  __AUTH_CONST.__cfstring: 0xd500
+  __AUTH_CONST.__objc_const: 0x15258
+  __AUTH_CONST.__objc_intobj: 0x240
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x430
-  __DATA.__objc_ivar: 0xf7c
+  __AUTH.__objc_data: 0x520
+  __DATA.__objc_ivar: 0xf8c
   __DATA.__data: 0x3a0
   __DATA.__bss: 0x1c
   __DATA.__common: 0x11d0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3DF74A8F-F539-3A8E-BC9A-88E7EC142734
-  Functions: 5621
-  Symbols:   15362
-  CStrings:  11800
+  UUID: 55F8372E-236C-3F35-B6C3-77CA944FD316
+  Functions: 5641
+  Symbols:   15443
+  CStrings:  11867
 
Symbols:
+ +[PoliciesPruningMO(CoreDataProperties) fetchRequest]
+ -[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:withError:]
+ -[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:withError:]
+ -[AnalyticsProcessor updateRoamPoliciesForSourceBssAndRoamWithReason:withError:]
+ -[PoliciesMO setRelationOn:to:withError:]
+ -[PoliciesRoamingMO setBSSto:orBssid:onContainer:withError:]
+ -[PoliciesRoamingMO setRoamto:withError:]
+ -[WAPCStoreSize .cxx_destruct]
+ -[WAPCStoreSize currentSize]
+ -[WAPCStoreSize description]
+ -[WAPCStoreSize initWithMaxStoreSize:]
+ -[WAPCStoreSize limit]
+ -[WAPCStoreSize noError]
+ -[WAPCStoreSize setCurrentSize:]
+ -[WAPCStoreSize setLimit:]
+ -[WAPCStoreSize setNoError:]
+ -[WAPCStoreSize setStoreNeedsPruning:]
+ -[WAPCStoreSize storeNeedsPruning]
+ -[WA_AP_BssesToProcess .cxx_destruct]
+ -[WA_AP_BssesToProcess bssesToProcess]
+ -[WA_AP_BssesToProcess queryFrom]
+ -[WA_AP_BssesToProcess setBssesToProcess:]
+ -[WA_AP_BssesToProcess setQueryFrom:]
+ GCC_except_table116
+ GCC_except_table130
+ GCC_except_table136
+ GCC_except_table52
+ GCC_except_table69
+ GCC_except_table82
+ GCC_except_table86
+ GCC_except_table87
+ GCC_except_table99
+ _OBJC_CLASS_$_PoliciesPruningMO
+ _OBJC_CLASS_$_WAPCStoreSize
+ _OBJC_CLASS_$_WA_AP_BssesToProcess
+ _OBJC_IVAR_$_WAPCStoreSize._currentSize
+ _OBJC_IVAR_$_WAPCStoreSize._limit
+ _OBJC_IVAR_$_WAPCStoreSize._noError
+ _OBJC_IVAR_$_WAPCStoreSize._storeNeedsPruning
+ _OBJC_IVAR_$_WA_AP_BssesToProcess._bssesToProcess
+ _OBJC_IVAR_$_WA_AP_BssesToProcess._queryFrom
+ _OBJC_METACLASS_$_PoliciesPruningMO
+ _OBJC_METACLASS_$_WAPCStoreSize
+ _OBJC_METACLASS_$_WA_AP_BssesToProcess
+ __OBJC_$_CLASS_METHODS_PoliciesPruningMO(CoreDataProperties)
+ __OBJC_$_INSTANCE_METHODS_PoliciesMO
+ __OBJC_$_INSTANCE_METHODS_PoliciesRoamingMO
+ __OBJC_$_INSTANCE_METHODS_WAPCStoreSize
+ __OBJC_$_INSTANCE_METHODS_WA_AP_BssesToProcess
+ __OBJC_$_INSTANCE_VARIABLES_WAPCStoreSize
+ __OBJC_$_INSTANCE_VARIABLES_WA_AP_BssesToProcess
+ __OBJC_$_PROP_LIST_WAPCStoreSize
+ __OBJC_$_PROP_LIST_WA_AP_BssesToProcess
+ __OBJC_CLASS_RO_$_PoliciesPruningMO
+ __OBJC_CLASS_RO_$_WAPCStoreSize
+ __OBJC_CLASS_RO_$_WA_AP_BssesToProcess
+ __OBJC_METACLASS_RO_$_PoliciesPruningMO
+ __OBJC_METACLASS_RO_$_WAPCStoreSize
+ __OBJC_METACLASS_RO_$_WA_AP_BssesToProcess
+ ___47-[WAPersistentContainer batchDelete:withError:]_block_invoke.306
+ ___56-[AnalyticsProcessor processDeferredPoliciesWithReason:]_block_invoke_2
+ ___56-[AnalyticsProcessor processDeferredPoliciesWithReason:]_block_invoke_3
+ ___56-[AnalyticsProcessor processDeferredPoliciesWithReason:]_block_invoke_4
+ ___93-[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:withError:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0lr48l8s32l8s40l8r56l8r64l8
+ ___block_literal_global.251
+ _objc_msgSend$currentSize
+ _objc_msgSend$destinationEntity
+ _objc_msgSend$initWithMaxStoreSize:
+ _objc_msgSend$limit
+ _objc_msgSend$noError
+ _objc_msgSend$queryFrom
+ _objc_msgSend$setBSSto:orBssid:onContainer:withError:
+ _objc_msgSend$setCurrentSize:
+ _objc_msgSend$setLimit:
+ _objc_msgSend$setNeedsPruning:
+ _objc_msgSend$setNoError:
+ _objc_msgSend$setQueryFrom:
+ _objc_msgSend$setRoamto:withError:
+ _objc_msgSend$setStoreNeedsPruning:
+ _objc_msgSend$setTimeSinceLastPruning:
+ _objc_msgSend$storeNeedsPruning
+ _objc_msgSend$updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:withError:
+ _objc_msgSend$updateRoamPoliciesForSourceBss:andRoam:withReason:withError:
+ _objc_msgSend$updateRoamPoliciesForSourceBssAndRoamWithReason:withError:
- -[AnalyticsProcessor bssesToProcess]
- -[AnalyticsProcessor lastQueryFrom]
- -[AnalyticsProcessor setBssesToProcess:]
- -[AnalyticsProcessor setLastQueryFrom:]
- -[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:]
- -[AnalyticsProcessor updateRoamPoliciesForSourceBssAndRoamWithReason:]
- GCC_except_table107
- GCC_except_table111
- GCC_except_table119
- GCC_except_table76
- _OBJC_IVAR_$_AnalyticsProcessor._bssesToProcess
- _OBJC_IVAR_$_AnalyticsProcessor._lastQueryFrom
- ___47-[WAPersistentContainer batchDelete:withError:]_block_invoke.260
- ___83-[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:]_block_invoke
- ___block_literal_global.228
- _objc_msgSend$lastQueryFrom
- _objc_msgSend$setLastQueryFrom:
- _objc_msgSend$setRoam:
- _objc_msgSend$updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:
- _objc_msgSend$updateRoamPoliciesForSourceBssAndRoamWithReason:
CStrings:
+ "%{public}s::%d:After the previous Exception we re-fetched the BSSMo for %@ and still run into %@"
+ "%{public}s::%d:After the previous Exception we tried to re-fetch the BSSMo for %@ and run into %@"
+ "%{public}s::%d:Batch deleted %lu records of entity[%@] matching [%@] (deleted so far:%ld)"
+ "%{public}s::%d:CoreData %@.%@=%@ threw exception: %@"
+ "%{public}s::%d:MostRecentPrune: %@"
+ "%{public}s::%d:Stored Policy (%@) run at (%@) with %@ and %@ - %@"
+ "%{public}s::%d:This function runs on entities whose class adopts DeploymentProtocol. %{public}@ (%@) does not"
+ "%{public}s::%d:Unable to set %@.bss to %@: %@"
+ "%{public}s::%d:Unexpected: cannot find %{public}@ for constraints %@"
+ "%{public}s::%d:entity %@ is a sub-entity, skip (aged in the parent entity, i.e., the actual SQL table)"
+ "%{public}s::%d:entity %@ is a sub-entity, skip (will be pruned at the parent level)"
+ "%{public}s::%d:nil bssMO.bssid: %@"
+ "%{public}s::%d:storeSizeInfo: %@"
+ "%{public}s::%d:updateRoamPoliciesForSourceBss:%@ andRoam:%@ withReason:%@ FAILED %@ - bailing"
+ "-[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:withError:]"
+ "-[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:withError:]_block_invoke"
+ "-[AnalyticsProcessor updateRoamPoliciesForSourceBssAndRoamWithReason:withError:]"
+ "-[PoliciesMO setRelationOn:to:withError:]"
+ "-[PoliciesRoamingMO setBSSto:orBssid:onContainer:withError:]"
+ "@\"NSNumber\""
+ "B56@0:8@16@24@32@40^@48"
+ "BSS %@ is not known"
+ "PoliciesPruning"
+ "PoliciesPruningMO"
+ "T@\"NSArray\",&,V_bssesToProcess"
+ "T@\"NSDate\",&,V_queryFrom"
+ "T@\"NSNumber\",&,V_currentSize"
+ "TB,V_noError"
+ "TB,V_storeNeedsPruning"
+ "TQ,V_limit"
+ "Unable to get WAClient"
+ "WAPCStoreSize"
+ "WA_AP_BssesToProcess"
+ "WiFiAnalytics-785.10 Sep 11 2025 20:21:19"
+ "_currentSize"
+ "_limit"
+ "_noError"
+ "_queryFrom"
+ "_storeNeedsPruning"
+ "com.apple.wifi.store.size"
+ "currentSize"
+ "destinationEntity"
+ "initWithMaxStoreSize:"
+ "limit"
+ "limit:%f.2KB currentSize:%f.2KB storeNeedsPruning:%@ error:%@"
+ "needsPruning"
+ "noError"
+ "obj %@(%@) is not of expected entity (%@)"
+ "policyType = %@ AND needsPruning == TRUE"
+ "queryFrom"
+ "relationship %@ does not exist in entity %@"
+ "setBSSto:orBssid:onContainer:withError:"
+ "setCurrentSize:"
+ "setLimit:"
+ "setNeedsPruning:"
+ "setNoError:"
+ "setQueryFrom:"
+ "setRelationOn:to:withError:"
+ "setRoamto:withError:"
+ "setStoreNeedsPruning:"
+ "setTimeSinceLastPruning:"
+ "size"
+ "storeNeedsPruning"
+ "timeSinceLastPruning"
+ "updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:withError:"
+ "updateRoamPoliciesForSourceBss:andRoam:withReason:withError:"
+ "updateRoamPoliciesForSourceBssAndRoamWithReason:withError:"
- "%{public}s::%d:Batch deleted %lu records of entity[%@] matching [%@]"
- "%{public}s::%d:Stored Policy (%@) run at (%@) with %@ and %@"
- "%{public}s::%d:This function runs on entities whose class adopts DeploymentProtocol"
- "%{public}s::%d:Unexpected: cannot find %@ for constraints %@"
- "%{public}s::%d:updateRoamPoliciesForSourceBss:%@ andRoam:%@ withReason:%@ FAILED - bailing"
- "-[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:]"
- "-[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:]_block_invoke"
- "-[AnalyticsProcessor updateRoamPoliciesForSourceBssAndRoamWithReason:]"
- "T@\"NSArray\",&,N,V_bssesToProcess"
- "T@\"NSDate\",&,N,V_lastQueryFrom"
- "WAErrorCodeStore_BSSNotFound"
- "WiFiAnalytics-776.90.4.2 Aug  6 2025 21:47:05"
- "_lastQueryFrom"
- "lastQueryFrom"
- "setLastQueryFrom:"
- "setRoam:"
- "updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:"
- "updateRoamPoliciesForSourceBssAndRoamWithReason:"

```
