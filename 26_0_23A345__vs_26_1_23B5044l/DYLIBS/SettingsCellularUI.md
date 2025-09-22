## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

```diff

-652.3.0.0.0
-  __TEXT.__text: 0x89244
+655.0.0.0.0
+  __TEXT.__text: 0x89504
   __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_methlist: 0x8d54
+  __TEXT.__objc_methlist: 0x8d64
   __TEXT.__const: 0x7c8
   __TEXT.__dlopen_cstrs: 0x649
   __TEXT.__cstring: 0x8105

   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x38
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__oslogstring: 0x65e0
+  __TEXT.__oslogstring: 0x664c
   __TEXT.__gcc_except_tab: 0x1a30
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x20c0
+  __TEXT.__unwind_info: 0x20d0
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_classname: 0x13f6
-  __TEXT.__objc_methname: 0x13b04
+  __TEXT.__objc_methname: 0x13b74
   __TEXT.__objc_methtype: 0x2972
-  __TEXT.__objc_stubs: 0xdac0
+  __TEXT.__objc_stubs: 0xdb00
   __DATA_CONST.__got: 0x960
   __DATA_CONST.__const: 0x1120
   __DATA_CONST.__objc_classlist: 0x480
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4bd8
+  __DATA_CONST.__objc_selrefs: 0x4bf0
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x190
   __AUTH_CONST.__auth_got: 0x720

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1B7B2E92-98C4-3855-99EA-0A2C401C447D
-  Functions: 3113
-  Symbols:   10196
-  CStrings:  6371
+  UUID: EF09F3B2-E612-33B4-83DB-90D9F199174F
+  Functions: 3117
+  Symbols:   10206
+  CStrings:  6378
 
Symbols:
+ +[SettingsCellularUtils satelliteDataPlanTier]
+ -[PSUIAddCellularPlanSpecifier isRequestingOngoing]
+ -[PSUIAddCellularPlanSpecifier setIsRequestingOngoing:]
+ GCC_except_table126
+ ___59-[PSUIAddCellularPlanSpecifier addCellularPlanCellPressed:]_block_invoke.40
+ ___59-[PSUIAddCellularPlanSpecifier addCellularPlanCellPressed:]_block_invoke.45
+ ___62-[PSUICellularController wirelessDataUsageChangedNotification]_block_invoke
+ _objc_msgSend$satelliteDataPlanTier
+ _objc_msgSend$setIsRequestingOngoing:
- -[PSUIAddCellularPlanSpecifier isRequestingFirstViewController]
- -[PSUIAddCellularPlanSpecifier setIsRequestingFirstViewController:]
- GCC_except_table125
CStrings:
+ "TB,V_isRequestingOngoing"
+ "_isRequestingOngoing"
+ "firstViewController is returned and reset isRequestingOngoing"
+ "isRequestingOngoing"
+ "satelliteDataPlanTier"
+ "setIsRequestingOngoing:"
+ "show wifi alert and reset isRequestingOngoing"

```
