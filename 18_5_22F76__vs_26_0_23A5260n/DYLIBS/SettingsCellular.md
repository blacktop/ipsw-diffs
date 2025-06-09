## SettingsCellular

> `/System/Library/PrivateFrameworks/SettingsCellular.framework/SettingsCellular`

```diff

-566.0.0.0.0
-  __TEXT.__text: 0xa274
-  __TEXT.__auth_stubs: 0x530
+639.0.0.0.0
+  __TEXT.__text: 0xa3c8
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_methlist: 0xdc4
   __TEXT.__const: 0xa8
   __TEXT.__dlopen_cstrs: 0xba
-  __TEXT.__cstring: 0x708
-  __TEXT.__oslogstring: 0x940
+  __TEXT.__cstring: 0x73a
+  __TEXT.__oslogstring: 0x95c
   __TEXT.__gcc_except_tab: 0x1fc
   __TEXT.__unwind_info: 0x310
-  __TEXT.__objc_classname: 0x2ce
-  __TEXT.__objc_methname: 0x2650
-  __TEXT.__objc_methtype: 0x8c4
-  __TEXT.__objc_stubs: 0x1dc0
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0x200
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__objc_classname: 0x2aa
+  __TEXT.__objc_methname: 0x26e5
+  __TEXT.__objc_methtype: 0x8de
+  __TEXT.__objc_stubs: 0x1e60
+  __DATA_CONST.__got: 0x208
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb20
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_selrefs: 0xb50
+  __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x2a8
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x600
-  __AUTH_CONST.__objc_const: 0x1440
+  __AUTH_CONST.__cfstring: 0x640
+  __AUTH_CONST.__objc_const: 0x1410
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0x60
+  __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x2a8
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_ivar: 0x28
-  __DATA_DIRTY.__objc_data: 0x370
+  __DATA_DIRTY.__objc_ivar: 0x2c
+  __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2A956D3A-6C36-3E9A-9B47-D53DC2ADBAA1
-  Functions: 234
-  Symbols:   1089
-  CStrings:  715
+  UUID: 1BB0D80C-66DF-3F17-8AA0-097DEFBF2BB7
+  Functions: 236
+  Symbols:   1093
+  CStrings:  728
 
Symbols:
+ +[PSAppCellularUsageSpecifier _specifierWithDisplayName:bundleID:shouldShowUsage:icon:statisticsCache:usageType:]
+ +[PSAppCellularUsageSpecifier appSpecifierWithBundleID:name:statisticsCache:usageType:]
+ -[PSAppCellularUsageSpecifier setUsagePolicy:]
+ -[PSAppCellularUsageSpecifier setUsageType:]
+ -[PSAppCellularUsageSpecifier usagePolicy]
+ -[PSAppCellularUsageSpecifier usageType]
+ -[PSAppDataUsagePolicySwitchSpecifier setUsagePolicy:]
+ -[PSAppDataUsagePolicySwitchSpecifier usagePolicy]
+ -[PSDataUsageSpecifier appType]
+ -[PSDataUsageSpecifier initWithAppType:bundleID:name:statisticsCache:usageType:]
+ -[PSDataUsageSpecifier setAppType:]
+ -[PSDataUsageSpecifier setUsageType:]
+ -[PSDataUsageSpecifier usageType]
+ _OBJC_IVAR_$_PSAppCellularUsageSpecifier._usageType
+ _PSSimStatusChangedNotification
+ ___54-[PSAppDataUsagePolicySwitchSpecifier setUsagePolicy:]_block_invoke
+ _kPSDataUsageTypeKey
+ _objc_msgSend$_specifierWithDisplayName:bundleID:shouldShowUsage:icon:statisticsCache:usageType:
+ _objc_msgSend$satellite
+ _objc_msgSend$setSatellite:
+ _objc_msgSend$setUsageType:
+ _objc_msgSend$shouldShowUsage
+ _objc_msgSend$usageType
- +[PSAppCellularUsageSpecifier _specifierWithDisplayName:bundleID:shouldShowUsage:icon:statisticsCache:]
- +[PSAppCellularUsageSpecifier appSpecifierWithBundleID:name:statisticsCache:]
- +[PSAppDataUsagePolicySwitchTableCell cellStyle]
- -[PSAppCellularUsageSpecifier cellularUsagePolicy]
- -[PSAppCellularUsageSpecifier setCellularUsagePolicy:]
- -[PSAppDataUsagePolicySwitchSpecifier cellularUsagePolicy]
- -[PSAppDataUsagePolicySwitchSpecifier setCellularUsagePolicy:]
- -[PSAppDataUsagePolicySwitchTableCell refreshCellContentsWithSpecifier:]
- -[PSDataUsageSpecifier initWithType:bundleID:name:statisticsCache:]
- -[PSDataUsageSpecifier setType:]
- -[PSDataUsageSpecifier type]
- _OBJC_CLASS_$_PSAppDataUsagePolicySwitchTableCell
- _OBJC_METACLASS_$_PSAppDataUsagePolicySwitchTableCell
- _OBJC_METACLASS_$_PSSubtitleSwitchTableCell
- __OBJC_$_CLASS_METHODS_PSAppDataUsagePolicySwitchTableCell
- __OBJC_$_INSTANCE_METHODS_PSAppDataUsagePolicySwitchTableCell
- __OBJC_CLASS_RO_$_PSAppDataUsagePolicySwitchTableCell
- __OBJC_METACLASS_RO_$_PSAppDataUsagePolicySwitchTableCell
- ___62-[PSAppDataUsagePolicySwitchSpecifier setCellularUsagePolicy:]_block_invoke
- _objc_msgSend$_specifierWithDisplayName:bundleID:shouldShowUsage:icon:statisticsCache:
- _objc_retain_x6
CStrings:
+ "@48@0:8@16@24@32Q40"
+ "@56@0:8Q16@24@32@40Q48"
+ "@60@0:8@16@24B32@36@44Q52"
+ "Delegate does not respond to didFailToSetPolicyForSpecifier:"
+ "PSDataUsageTypeKey"
+ "PSSimStatusChangedNotification"
+ "Posting notification %@"
+ "TQ,N,V_appType"
+ "TQ,N,V_usageType"
+ "_appType"
+ "_specifierWithDisplayName:bundleID:shouldShowUsage:icon:statisticsCache:usageType:"
+ "_usageType"
+ "appSpecifierWithBundleID:name:statisticsCache:usageType:"
+ "appType"
+ "initWithAppType:bundleID:name:statisticsCache:usageType:"
+ "satellite"
+ "setAppType:"
+ "setSatellite:"
+ "setUsagePolicy:"
+ "setUsageType:"
+ "usagePolicy"
+ "usageType"
- "@48@0:8Q16@24@32@40"
- "@52@0:8@16@24B32@36@44"
- "Delegate does respond to didFailToSetPolicyForSpecifier:"
- "PSAppDataUsagePolicySwitchTableCell"
- "TQ,N,V_type"
- "_specifierWithDisplayName:bundleID:shouldShowUsage:icon:statisticsCache:"
- "_type"
- "appSpecifierWithBundleID:name:statisticsCache:"
- "initWithType:bundleID:name:statisticsCache:"
- "setType:"
- "type"

```
