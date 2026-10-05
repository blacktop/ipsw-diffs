## RemoteUI

> `/System/Library/PrivateFrameworks/RemoteUI.framework/RemoteUI`

```diff

-640.125.2.0.0
-  __TEXT.__text: 0x146ff8
-  __TEXT.__objc_methlist: 0x8f5c
-  __TEXT.__const: 0xfd54
-  __TEXT.__cstring: 0x56fd
+640.125.5.0.0
+  __TEXT.__text: 0x148958
+  __TEXT.__objc_methlist: 0x9064
+  __TEXT.__const: 0xfd64
+  __TEXT.__cstring: 0x570d
   __TEXT.__oslogstring: 0x2c8e
-  __TEXT.__gcc_except_tab: 0x7e8
+  __TEXT.__gcc_except_tab: 0x7f8
   __TEXT.__dlopen_cstrs: 0x313
-  __TEXT.__swift5_typeref: 0xa3ec
-  __TEXT.__swift5_reflstr: 0x2cba
+  __TEXT.__swift5_typeref: 0xa412
+  __TEXT.__swift5_reflstr: 0x2cda
   __TEXT.__swift5_assocty: 0x14d8
   __TEXT.__constg_swiftt: 0x572c
-  __TEXT.__swift5_fieldmd: 0x3ac8
+  __TEXT.__swift5_fieldmd: 0x3ae0
   __TEXT.__swift5_proto: 0x978
   __TEXT.__swift5_types: 0x4bc
   __TEXT.__swift5_capture: 0xd94

   __TEXT.__swift5_protos: 0x7c
   __TEXT.__swift5_builtin: 0x1b8
   __TEXT.__swift5_mpenum: 0x34
-  __TEXT.__unwind_info: 0x7200
+  __TEXT.__unwind_info: 0x7260
   __TEXT.__eh_frame: 0x506c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1678
-  __DATA_CONST.__objc_classlist: 0x458
+  __DATA_CONST.__const: 0x16a0
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x56f8
+  __DATA_CONST.__objc_selrefs: 0x57a0
   __DATA_CONST.__objc_protorefs: 0xc0
-  __DATA_CONST.__objc_superrefs: 0x1b8
+  __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x100
-  __DATA_CONST.__got: 0x1288
-  __AUTH_CONST.__const: 0x89d8
+  __DATA_CONST.__got: 0x1290
+  __AUTH_CONST.__const: 0x8af0
   __AUTH_CONST.__cfstring: 0x44a0
-  __AUTH_CONST.__objc_const: 0xefd0
+  __AUTH_CONST.__objc_const: 0xf230
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2210
-  __AUTH.__objc_data: 0x3fe0
-  __AUTH.__data: 0x3310
-  __DATA.__objc_ivar: 0x81c
-  __DATA.__data: 0x4ae0
+  __AUTH_CONST.__auth_got: 0x2220
+  __AUTH.__objc_data: 0x4030
+  __AUTH.__data: 0x3308
+  __DATA.__objc_ivar: 0x848
+  __DATA.__data: 0x4b10
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x208

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8208
-  Symbols:   6667
+  Functions: 8233
+  Symbols:   6714
   CStrings:  1149
 
Symbols:
+ -[RUITableView _installTableHeaderView:]
+ -[RUITableView _loadServerFooterView]
+ -[RUITableView _pageDescribesItsOwnTableHeader:]
+ -[RUITableView externalHeaderFooterDidResize]
+ -[RUITableView externalTableFooterView]
+ -[RUITableView externalTableHeaderView]
+ -[RUITableView externallyManagedHeaderFooter]
+ -[RUITableView loadExternalHeaderAndFooterViews]
+ -[RUITableView setExternalHeaderFooterDidResize:]
+ -[RUITableView setExternallyManagedHeaderFooter:]
+ -[RUITableWelcomeController .cxx_destruct]
+ -[RUITableWelcomeController _headerTopOffset]
+ -[RUITableWelcomeController _hostRUITableView:]
+ -[RUITableWelcomeController _installExternalHeaderFooterIfNeeded]
+ -[RUITableWelcomeController _layoutButtonTray]
+ -[RUITableWelcomeController _restoreTableViewDelegate]
+ -[RUITableWelcomeController _suppressesInternalHeaderPadding]
+ -[RUITableWelcomeController _updateParentPreferredContentSize]
+ -[RUITableWelcomeController headerViewBottomToTableViewTopPadding]
+ -[RUITableWelcomeController initWithHostedTableView:title:detailText:]
+ -[RUITableWelcomeController rendersHeaderContent]
+ -[RUITableWelcomeController setShouldUseCustomButtonTray:]
+ -[RUITableWelcomeController setTableView:]
+ -[RUITableWelcomeController shouldUseCustomButtonTray]
+ -[RUITableWelcomeController viewDidLayoutSubviews]
+ -[RUITableWelcomeController viewDidLoad]
+ -[RUITableWelcomeController viewWillAppear:]
+ GCC_except_table1
+ GCC_except_table105
+ GCC_except_table109
+ GCC_except_table113
+ GCC_except_table137
+ _CGRectEqualToRect
+ _OBJC_CLASS_$_OBTableWelcomeController
+ _OBJC_CLASS_$_RUITableWelcomeController
+ _OBJC_IVAR_$_RUITableView._externalHeaderFooterDidResize
+ _OBJC_IVAR_$_RUITableView._externalTableFooterView
+ _OBJC_IVAR_$_RUITableView._externalTableHeaderView
+ _OBJC_IVAR_$_RUITableView._externallyManagedHeaderFooter
+ _OBJC_IVAR_$_RUITableView._lastPublishedFooterSize
+ _OBJC_IVAR_$_RUITableView._lastPublishedHeaderSize
+ _OBJC_IVAR_$_RUITableWelcomeController._installedFooterView
+ _OBJC_IVAR_$_RUITableWelcomeController._installedHeaderView
+ _OBJC_IVAR_$_RUITableWelcomeController._rendersHeaderContent
+ _OBJC_IVAR_$_RUITableWelcomeController._ruiTableView
+ _OBJC_IVAR_$_RUITableWelcomeController._shouldUseCustomButtonTray
+ _OBJC_METACLASS_$_OBTableWelcomeController
+ _OBJC_METACLASS_$_RUITableWelcomeController
+ __OBJC_$_INSTANCE_METHODS_OBButtonTray(RUI_Internal|RemoteUI|RUITableWelcome)
+ __OBJC_$_INSTANCE_METHODS_RUITableWelcomeController
+ __OBJC_$_INSTANCE_VARIABLES_RUITableWelcomeController
+ __OBJC_$_PROP_LIST_RUITableWelcomeController
+ __OBJC_CLASS_RO_$_RUITableWelcomeController
+ __OBJC_METACLASS_RO_$_RUITableWelcomeController
+ ___47-[RUITableWelcomeController _hostRUITableView:]_block_invoke
+ ___62-[RUITableWelcomeController _updateParentPreferredContentSize]_block_invoke
+ ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
+ _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQOyACyAA03AnyE0VAA012_EnvironmentJ17TransformModifierVySay06RemoteB00E7ContextOGGG_Qo_AA017_AppearanceActionN0VGAaDHPqd__AaDHD2_ASHO_AuA0eN0HPyHCHC
+ _symbolic _____y__________ySay_____GGG 7SwiftUI15ModifiedContentV AA7AnyViewV AA32_EnvironmentKeyTransformModifierV 06RemoteB00F7ContextO
+ _symbolic _____y_____yAAy__________ySay_____GGG_Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQO AA03AnyE0V AA012_EnvironmentJ17TransformModifierV 06RemoteB00E7ContextO AA017_AppearanceActionN0V
+ _symbolic _____y_____y__________ySay_____GGG_Qo_ 7SwiftUI4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQO AA15ModifiedContentV AA03AnyC0V AA012_EnvironmentH17TransformModifierV 06RemoteB00C7ContextO
- -[RUIObjectModel supportedInterfaceOrientationsForRUIPage:]
- -[RUIPage supportedInterfaceOrientations]
- -[RemoteUIController supportedInterfaceOrientationsForObjectModel:page:]
- GCC_except_table100
- GCC_except_table110
- GCC_except_table114
- GCC_except_table132
- GCC_except_table97
- __OBJC_$_INSTANCE_METHODS_OBButtonTray(RUI_Internal|RemoteUI)
- __OBJC_$_PROP_LIST_OBButtonTray_$_RUI_Internal
- _get_witness_table 7SwiftUI15ModifiedContentVyAA4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQOyAE06RemoteB0E06appendE7ContextyQrAI0eM0OFQOyAA03AnyE0V_Qo__Qo_AA25_AppearanceActionModifierVGAaDHPqd__AaDHD2_APHO_ArA0eQ0HPyHCHC
- _symbolic _____y______Qo_ 7SwiftUI4ViewP06RemoteB0E06appendC7ContextyQrAD0cF0OFQO AA03AnyC0V
- _symbolic _____y_____y______Qo__Qo_ 7SwiftUI4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQO AC06RemoteB0E06appendC7ContextyQrAG0cK0OFQO AA03AnyC0V
- _symbolic _____y_____y_____y______Qo__Qo______G 7SwiftUI15ModifiedContentV AA4ViewPAAE15navigationTitleyQrAA18LocalizedStringKeyVFQO AE06RemoteB0E06appendE7ContextyQrAI0eM0OFQO AA03AnyE0V AA25_AppearanceActionModifierV
CStrings:
+ "forceHeaderInLeadingColumn"
- "\xf0\xa2"
```
