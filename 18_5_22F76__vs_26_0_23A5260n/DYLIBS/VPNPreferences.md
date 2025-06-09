## VPNPreferences

> `/System/Library/PreferenceBundles/VPNPreferences.bundle/VPNPreferences`

```diff

-361.120.2.0.0
-  __TEXT.__text: 0x23ac4
+367.0.0.0.0
+  __TEXT.__text: 0x26054
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x22c4
+  __TEXT.__objc_methlist: 0x2584
+  __TEXT.__gcc_except_tab: 0x37c
+  __TEXT.__cstring: 0x1350
   __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x328
-  __TEXT.__cstring: 0x131c
   __TEXT.__oslogstring: 0x1a4
-  __TEXT.__unwind_info: 0x558
-  __TEXT.__objc_classname: 0x1c7
-  __TEXT.__objc_methname: 0x6b7e
-  __TEXT.__objc_methtype: 0xd30
-  __TEXT.__objc_stubs: 0x55c0
+  __TEXT.__unwind_info: 0x5d0
+  __TEXT.__objc_classname: 0x211
+  __TEXT.__objc_methname: 0x6d6e
+  __TEXT.__objc_methtype: 0xd54
+  __TEXT.__objc_stubs: 0x5720
   __DATA_CONST.__got: 0x3b8
   __DATA_CONST.__const: 0x558
-  __DATA_CONST.__objc_classlist: 0x90
+  __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bd8
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_selrefs: 0x1c60
+  __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x2140
-  __AUTH_CONST.__objc_const: 0x2e40
+  __AUTH_CONST.__cfstring: 0x21a0
+  __AUTH_CONST.__objc_const: 0x31f0
   __AUTH_CONST.__objc_intobj: 0x1e0
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x2b0
+  __AUTH.__objc_data: 0x550
+  __DATA.__objc_ivar: 0x2d8
   __DATA.__data: 0x150
   __DATA.__bss: 0x50
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FC5EAC6E-8807-347D-AEEB-21F1B741A363
-  Functions: 703
-  Symbols:   2765
-  CStrings:  1930
+  UUID: 689F9D5C-5251-3D2C-BACF-A51C82E340C3
+  Functions: 759
+  Symbols:   2921
+  CStrings:  1962
 
Symbols:
+ +[VPNPrimaryTableCell cellStyle]
+ +[VPNTableCell cellStyle]
+ -[URLFilterController .cxx_destruct]
+ -[URLFilterController currentConnection]
+ -[URLFilterController dealloc]
+ -[URLFilterController getURLFilterState:]
+ -[URLFilterController init]
+ -[URLFilterController serviceID]
+ -[URLFilterController setCurrentConnection:]
+ -[URLFilterController setServiceID:]
+ -[URLFilterController setSystemSpecifiers:]
+ -[URLFilterController setURLFilterActive:specifier:]
+ -[URLFilterController setURLFilterState:forSpecifier:]
+ -[URLFilterController someConfigurationChanged:]
+ -[URLFilterController someStatusChanged:]
+ -[URLFilterController specifiers]
+ -[URLFilterController systemSpecifiers]
+ -[URLFilterController tableView:cellForRowAtIndexPath:]
+ -[URLFilterController tableView:didSelectRowAtIndexPath:]
+ -[URLFilterController urlFilterStatusChanged:]
+ -[URLFilterSetupListController .cxx_destruct]
+ -[URLFilterSetupListController appName]
+ -[URLFilterSetupListController appWillEnterForeground:]
+ -[URLFilterSetupListController bundle]
+ -[URLFilterSetupListController connection]
+ -[URLFilterSetupListController dealloc]
+ -[URLFilterSetupListController displayNameForSpecifier:]
+ -[URLFilterSetupListController displayName]
+ -[URLFilterSetupListController getDescriptionForApp:]
+ -[URLFilterSetupListController includedBundleIDs]
+ -[URLFilterSetupListController init]
+ -[URLFilterSetupListController loadView]
+ -[URLFilterSetupListController organization]
+ -[URLFilterSetupListController serviceID]
+ -[URLFilterSetupListController setAppName:]
+ -[URLFilterSetupListController setDisplayName:]
+ -[URLFilterSetupListController setIncludedBundleIDs:]
+ -[URLFilterSetupListController setOrganization:]
+ -[URLFilterSetupListController setServiceID:]
+ -[URLFilterSetupListController setStateForServiceID:]
+ -[URLFilterSetupListController setVpnGrade:]
+ -[URLFilterSetupListController specifiers]
+ -[URLFilterSetupListController statusForConnection:]
+ -[URLFilterSetupListController viewDidAppear:]
+ -[URLFilterSetupListController viewWillAppear:]
+ -[URLFilterSetupListController vpnConfigurationChanged:]
+ -[URLFilterSetupListController vpnGradeNameForSpecifier:]
+ -[URLFilterSetupListController vpnGrade]
+ -[URLFilterSetupListController vpnStatusChanged:]
+ -[VPNBundleController setUrlFilterSpecifier:]
+ -[VPNBundleController urlFilterSpecifier]
+ -[VPNBundleController urlFilterStatusForSpecifier:]
+ -[VPNConnectionStore iterateURLFilterServicesWithBlock:]
+ -[VPNController viewDidLoad]
+ -[VPNPrimaryTableCell initWithStyle:reuseIdentifier:]
+ -[VPNTableCell initWithStyle:reuseIdentifier:]
+ _OBJC_CLASS_$_URLFilterController
+ _OBJC_CLASS_$_URLFilterSetupController
+ _OBJC_CLASS_$_URLFilterSetupListController
+ _OBJC_IVAR_$_URLFilterController._currentConnection
+ _OBJC_IVAR_$_URLFilterController._serviceID
+ _OBJC_IVAR_$_URLFilterController._systemSpecifiers
+ _OBJC_IVAR_$_URLFilterSetupListController._appName
+ _OBJC_IVAR_$_URLFilterSetupListController._displayName
+ _OBJC_IVAR_$_URLFilterSetupListController._includedBundleIDs
+ _OBJC_IVAR_$_URLFilterSetupListController._organization
+ _OBJC_IVAR_$_URLFilterSetupListController._serviceID
+ _OBJC_IVAR_$_URLFilterSetupListController._vpnGrade
+ _OBJC_IVAR_$_VPNBundleController._urlFilterSpecifier
+ _OBJC_METACLASS_$_URLFilterController
+ _OBJC_METACLASS_$_URLFilterSetupController
+ _OBJC_METACLASS_$_URLFilterSetupListController
+ __OBJC_$_CLASS_METHODS_VPNPrimaryTableCell
+ __OBJC_$_CLASS_METHODS_VPNTableCell
+ __OBJC_$_INSTANCE_METHODS_URLFilterController
+ __OBJC_$_INSTANCE_METHODS_URLFilterSetupListController
+ __OBJC_$_INSTANCE_VARIABLES_URLFilterController
+ __OBJC_$_INSTANCE_VARIABLES_URLFilterSetupListController
+ __OBJC_$_PROP_LIST_URLFilterController
+ __OBJC_$_PROP_LIST_URLFilterSetupListController
+ __OBJC_CLASS_RO_$_URLFilterController
+ __OBJC_CLASS_RO_$_URLFilterSetupController
+ __OBJC_CLASS_RO_$_URLFilterSetupListController
+ __OBJC_METACLASS_RO_$_URLFilterController
+ __OBJC_METACLASS_RO_$_URLFilterSetupController
+ __OBJC_METACLASS_RO_$_URLFilterSetupListController
+ ___33-[URLFilterController specifiers]_block_invoke
+ ___51-[VPNBundleController urlFilterStatusForSpecifier:]_block_invoke
+ _objc_msgSend$cellReuseIdentifier
+ _objc_msgSend$currentConnection
+ _objc_msgSend$iterateURLFilterServicesWithBlock:
+ _objc_msgSend$registerClass:forCellReuseIdentifier:
+ _objc_msgSend$setCurrentConnection:
+ _objc_msgSend$setURLFilterActive:specifier:
+ _objc_msgSend$setUrlFilterSpecifier:
+ _objc_msgSend$table
+ _objc_msgSend$urlFilter
+ _objc_msgSend$urlFilterSpecifier
+ _objc_msgSend$urlFilterStatusChanged:
- -[VPNPrimaryTableCell initWithStyle:reuseIdentifier:specifier:]
- -[VPNTableCell initWithStyle:reuseIdentifier:specifier:]
CStrings:
+ "@\"VPNConnection\""
+ "@32@0:8q16@24"
+ "T@\"PSSpecifier\",&,V_urlFilterSpecifier"
+ "T@\"VPNConnection\",&,V_currentConnection"
+ "URLFilterController"
+ "URLFilterSetupController"
+ "URLFilterSetupListController"
+ "URL_FILTER"
+ "URL_FILTER_FOOTER"
+ "URL_FILTER_GROUP_TITLE"
+ "[10@\"NSMutableArray\"]"
+ "[10@\"NSMutableDictionary\"]"
+ "[10@\"NSUUID\"]"
+ "[10@\"VPNConnection\"]"
+ "[10B]"
+ "_currentConnection"
+ "_urlFilterSpecifier"
+ "cellReuseIdentifier"
+ "cellStyle"
+ "currentConnection"
+ "getURLFilterState:"
+ "initWithStyle:reuseIdentifier:"
+ "iterateURLFilterServicesWithBlock:"
+ "registerClass:forCellReuseIdentifier:"
+ "setCurrentConnection:"
+ "setURLFilterActive:specifier:"
+ "setURLFilterState:forSpecifier:"
+ "setUrlFilterSpecifier:"
+ "table"
+ "urlFilter"
+ "urlFilterSpecifier"
+ "urlFilterStatusChanged:"
+ "urlFilterStatusForSpecifier:"
+ "viewDidLoad"
- "[9@\"NSMutableArray\"]"
- "[9@\"NSMutableDictionary\"]"
- "[9@\"NSUUID\"]"
- "[9@\"VPNConnection\"]"
- "[9B]"

```
