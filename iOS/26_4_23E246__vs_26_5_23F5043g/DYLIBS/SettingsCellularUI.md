## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

```diff

-679.0.0.0.0
-  __TEXT.__text: 0x92610
+680.0.0.0.0
+  __TEXT.__text: 0x927c8
   __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x8d34
+  __TEXT.__objc_methlist: 0x8d3c
   __TEXT.__const: 0x478
   __TEXT.__dlopen_cstrs: 0x649
   __TEXT.__swift5_typeref: 0x196

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x10
-  __TEXT.__cstring: 0x7fae
+  __TEXT.__cstring: 0x7fe2
   __TEXT.__oslogstring: 0x65cf
   __TEXT.__gcc_except_tab: 0x1b2c
   __TEXT.__ustring: 0x8
   __TEXT.__unwind_info: 0x27a8
   __TEXT.__eh_frame: 0x100
   __TEXT.__objc_classname: 0x14d1
-  __TEXT.__objc_methname: 0x13fb2
-  __TEXT.__objc_methtype: 0x2921
-  __TEXT.__objc_stubs: 0xdda0
+  __TEXT.__objc_methname: 0x14021
+  __TEXT.__objc_methtype: 0x2935
+  __TEXT.__objc_stubs: 0xde80
   __DATA_CONST.__got: 0x920
   __DATA_CONST.__const: 0x1138
   __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c88
+  __DATA_CONST.__objc_selrefs: 0x4cc0
   __DATA_CONST.__objc_superrefs: 0x408
   __DATA_CONST.__objc_arraydata: 0x190
   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x6d20
+  __AUTH_CONST.__cfstring: 0x6d60
   __AUTH_CONST.__objc_const: 0xec88
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 79959DFF-1193-33B0-9FC2-56E3036900F0
-  Functions: 3057
-  Symbols:   10173
-  CStrings:  6413
+  UUID: D1D42463-31E2-3ABD-8111-F8FBC30D2DE1
+  Functions: 3058
+  Symbols:   10182
+  CStrings:  6425
 
Symbols:
+ +[SettingsCellularUtils isTrialPlanExpired:]
+ -[PSUICellularPlanTableCell _setBadge:andLabel:andExpirationDate:isExpired:]
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.475
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.476
+ ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.481
+ ___block_literal_global.443
+ ___block_literal_global.505
+ _objc_msgSend$_setBadge:andLabel:andExpirationDate:isExpired:
+ _objc_msgSend$components:fromDate:
+ _objc_msgSend$date
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$isTrialPlanExpired:
+ _objc_msgSend$setHour:
+ _objc_msgSend$setMinute:
+ _objc_msgSend$setSecond:
- -[PSUICellularPlanTableCell _setBadge:andLabel:andExpirationDate:]
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.472
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.473
- ___87-[PSUICellularController tableView:trailingSwipeActionsConfigurationForRowAtIndexPath:]_block_invoke.478
- ___block_literal_global.440
- ___block_literal_global.502
- _objc_msgSend$_setBadge:andLabel:andExpirationDate:
CStrings:
+ "NUMBER_EXPIRED_%@"
+ "TRIAL_ESIM_FOOTER_SSIM_EXPIRED_%@"
+ "_setBadge:andLabel:andExpirationDate:isExpired:"
+ "components:fromDate:"
+ "date"
+ "dateFromComponents:"
+ "isTrialPlanExpired:"
+ "setHour:"
+ "setMinute:"
+ "setSecond:"
+ "v44@0:8@16@24@32B40"
- "_setBadge:andLabel:andExpirationDate:"

```
