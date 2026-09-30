## SettingsCellularUI

> `/System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI`

```diff

-752.0.0.0.0
-  __TEXT.__text: 0x91960
+756.0.0.0.0
+  __TEXT.__text: 0x919b8
   __TEXT.__objc_methlist: 0x9cbc
   __TEXT.__const: 0x498
   __TEXT.__dlopen_cstrs: 0x6a1

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x56a8
+  __DATA_CONST.__objc_selrefs: 0x56a0
   __DATA_CONST.__objc_superrefs: 0x440
   __DATA_CONST.__objc_arraydata: 0x1b8
   __DATA_CONST.__got: 0xad8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 3363
-  Symbols:   7615
+  Symbols:   7614
   CStrings:  2070
 
Symbols:
+ -[PSUIDataUsageCategorySpecifier initWithAppType:usageType:subSpecifiers:statisticsCache:]
+ _objc_msgSend$bundleIDsForAppType:usageType:
+ _objc_msgSend$initWithAppType:usageType:subSpecifiers:statisticsCache:
- -[PSUIDataUsageCategorySpecifier initWithAppType:usageType:subSpecifiers:]
- _objc_msgSend$bundleIDsForAppType:
- _objc_msgSend$initWithAppType:usageType:subSpecifiers:
- _objc_msgSend$rightAnchor
Functions:
~ -[PSUIAppsAndCategoriesDataUsageSubgroup specifiersWithSortComparator:] : 376 -> 380
~ -[PSUIAppsAndCategoriesDataUsageSubgroup addDataUsageCategorySpecifierToSpecifiers:appType:] : 252 -> 260
~ ___40-[PSUITopAppUsageGroup createSpecifiers]_block_invoke : 2816 -> 2820
~ -[PSUIDataUsageCategoryListController shouldShowSpinner] : 172 -> 228
~ -[PSUIDataUsageCategorySpecifier initWithAppType:usageType:subSpecifiers:] -> -[PSUIDataUsageCategorySpecifier initWithAppType:usageType:subSpecifiers:statisticsCache:] : 668 -> 664
~ -[PSUICellularPlanAddOnPlanTableCell _setupView:] : 1620 -> 1640
```
