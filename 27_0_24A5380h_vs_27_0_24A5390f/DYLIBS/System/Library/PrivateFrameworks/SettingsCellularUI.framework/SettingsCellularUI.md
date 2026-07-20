## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-746.0.0.0.0
-  __TEXT.__text: 0x93324
-  __TEXT.__objc_methlist: 0x9c2c
+750.0.0.0.0
+  __TEXT.__text: 0x938fc
+  __TEXT.__objc_methlist: 0x9c9c
   __TEXT.__const: 0x498
   __TEXT.__dlopen_cstrs: 0x6a1
   __TEXT.__swift5_typeref: 0x196

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x10
-  __TEXT.__cstring: 0x912e
+  __TEXT.__cstring: 0x914a
   __TEXT.__oslogstring: 0x6c4b
-  __TEXT.__gcc_except_tab: 0x1864
+  __TEXT.__gcc_except_tab: 0x186c
   __TEXT.__ustring: 0x8
   __TEXT.__unwind_info: 0x2370
   __TEXT.__eh_frame: 0x100

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5648
+  __DATA_CONST.__objc_selrefs: 0x5680
   __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0x1b8
-  __DATA_CONST.__got: 0xac0
+  __DATA_CONST.__got: 0xac8
   __AUTH_CONST.__const: 0x5e0
-  __AUTH_CONST.__cfstring: 0x8720
-  __AUTH_CONST.__objc_const: 0x102c8
+  __AUTH_CONST.__cfstring: 0x86e0
+  __AUTH_CONST.__objc_const: 0x103d0
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__auth_got: 0x678
   __AUTH.__objc_data: 0x1718
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x628
+  __DATA.__objc_ivar: 0x63c
   __DATA.__data: 0xb50
   __DATA.__bss: 0xe8
-  __DATA_DIRTY.__objc_ivar: 0x5f0
+  __DATA_DIRTY.__objc_ivar: 0x5f8
   __DATA_DIRTY.__objc_data: 0x1818
   __DATA_DIRTY.__data: 0x270
   __DATA_DIRTY.__bss: 0x370

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3349
-  Symbols:   7583
-  CStrings:  2064
+  Functions: 3357
+  Symbols:   7602
+  CStrings:  2060
 
Symbols:
+ +[PSUITurnOnThisLineSpecifier specifierWithPlanUniversalReference:cellularPlanManager:planManagerCache:callCache:simStatusCache:hostController:isActivating:]
+ +[SettingsCellularUtils shouldUseSIMConfigSwitchFlowForPlan:simStatusCache:]
+ -[PSUICarrierAppGroup initWithListController:parentSpecifier:featureFlagProvider:]
+ -[PSUICarrierSpaceGroup initWithListController:groupSpecifier:parentSpecifier:ctClient:featureFlagProvider:]
+ -[PSUICarrierSpaceServicesController initWithFeatureFlagProvider:]
+ -[PSUIDataModeSubgroup createTARandomizationSpecifiersIfNeededForDescriptor:]
+ -[PSUIDataModeSubgroup taRandomizationSpecifiersExist]
+ -[PSUISubscriptionContextMenusGroup featureFlagProvider]
+ -[PSUISubscriptionContextMenusGroup setFeatureFlagProvider:]
+ -[PSUISubscriptionContextMenusProductionFactory createCarrierAppGroupWithFeatureFlagProvider:]
+ -[PSUISubscriptionContextMenusProductionFactory createCarrierSpaceSubgroupWithFeatureFlagProvider:]
+ -[PSUISubscriptionContextMenusProductionFactory createFeatureFlagProvider]
+ -[PSUITurnOnThisLineSpecifier initWithPlanUniversalReference:planUUID:cellularPlanManager:planManagerCache:callCache:simStatusCache:hostController:isActivating:]
+ -[PSUITurnOnThisLineSpecifier setSimStatusCache:]
+ -[PSUITurnOnThisLineSpecifier simStatusCache]
+ _OBJC_CLASS_$_SettingsCellularFeatureFlagManager
+ _OBJC_IVAR_$_PSUICarrierAppGroup._featureFlagProvider
+ _OBJC_IVAR_$_PSUICarrierSpaceGroup._featureFlagProvider
+ _OBJC_IVAR_$_PSUIDataModeSubgroup._cachedRegulatoryDisabled
+ _OBJC_IVAR_$_PSUIDataModeSubgroup._cachedServiceDescriptor
+ _OBJC_IVAR_$_PSUISubscriptionContextMenusGroup._featureFlagProvider
+ _objc_msgSend$createCarrierAppGroupWithFeatureFlagProvider:
+ _objc_msgSend$createCarrierSpaceSubgroupWithFeatureFlagProvider:
+ _objc_msgSend$createFeatureFlagProvider
+ _objc_msgSend$createTARandomizationSpecifiersIfNeededForDescriptor:
+ _objc_msgSend$initWithListController:groupSpecifier:parentSpecifier:ctClient:featureFlagProvider:
+ _objc_msgSend$initWithListController:parentSpecifier:featureFlagProvider:
+ _objc_msgSend$initWithNibName:bundle:
+ _objc_msgSend$initWithPlanUniversalReference:planUUID:cellularPlanManager:planManagerCache:callCache:simStatusCache:hostController:isActivating:
+ _objc_msgSend$isEnabled:
+ _objc_msgSend$shouldUseSIMConfigSwitchFlowForPlan:simStatusCache:
+ _objc_msgSend$specifierWithPlanUniversalReference:cellularPlanManager:planManagerCache:callCache:simStatusCache:hostController:isActivating:
+ _objc_msgSend$taRandomizationSpecifiersExist
+ _objc_retain_x7
- +[PSUITurnOnThisLineSpecifier specifierWithPlanUniversalReference:cellularPlanManager:planManagerCache:callCache:hostController:isActivating:]
- -[PSUICarrierAppGroup initWithListController:parentSpecifier:]
- -[PSUICarrierSpaceGroup initWithListController:groupSpecifier:parentSpecifier:ctClient:]
- -[PSUIDataModeSubgroup createTARandomizationSpecifiersIfNeeded]
- -[PSUISubscriptionContextMenusProductionFactory createCarrierAppGroup]
- -[PSUISubscriptionContextMenusProductionFactory createCarrierSpaceSubgroup]
- -[PSUITurnOnThisLineSpecifier initWithPlanUniversalReference:planUUID:cellularPlanManager:planManagerCache:callCache:hostController:isActivating:]
- _objc_msgSend$createCarrierAppGroup
- _objc_msgSend$createCarrierSpaceSubgroup
- _objc_msgSend$createTARandomizationSpecifiersIfNeeded
- _objc_msgSend$initWithListController:groupSpecifier:parentSpecifier:ctClient:
- _objc_msgSend$initWithListController:parentSpecifier:
- _objc_msgSend$initWithPlanUniversalReference:planUUID:cellularPlanManager:planManagerCache:callCache:hostController:isActivating:
- _objc_msgSend$specifierWithPlanUniversalReference:cellularPlanManager:planManagerCache:callCache:hostController:isActivating:
- _objc_retain_x6
CStrings:
+ "QS_DETAILS_ESIM_SETUP"
+ "QS_DETAILS_IOS_VERSION"
+ "QS_DETAILS_MODEL_NAME"
+ "QS_DETAILS_NAME"
+ "QS_DETAILS_SERIAL_NUMBER"
+ "s"
- "CarrierAppInSettings"
- "Model Name"
- "Name"
- "Off"
- "On"
- "S"
- "Serial Number"
- "c"
- "eSIM Setup"
- "iOS Version"
```
