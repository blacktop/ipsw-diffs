## ShareSheet

> `/System/Library/PrivateFrameworks/ShareSheet.framework/ShareSheet`

```diff

-2094.40.31.0.0
-  __TEXT.__text: 0xc6fb4
+2094.40.71.0.0
+  __TEXT.__text: 0xc75c4
   __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x11254
+  __TEXT.__objc_methlist: 0x11324
   __TEXT.__const: 0x628
   __TEXT.__gcc_except_tab: 0x2308
-  __TEXT.__oslogstring: 0x6c77
-  __TEXT.__cstring: 0x6c2d
+  __TEXT.__oslogstring: 0x6caf
+  __TEXT.__cstring: 0x6c50
   __TEXT.__dlopen_cstrs: 0xa59
   __TEXT.__ustring: 0xca
-  __TEXT.__unwind_info: 0x33b8
-  __TEXT.__objc_classname: 0x24b3
-  __TEXT.__objc_methname: 0x2dbd9
-  __TEXT.__objc_methtype: 0x7685
-  __TEXT.__objc_stubs: 0x1c7e0
+  __TEXT.__unwind_info: 0x33d0
+  __TEXT.__objc_classname: 0x24b0
+  __TEXT.__objc_methname: 0x2dd85
+  __TEXT.__objc_methtype: 0x7688
+  __TEXT.__objc_stubs: 0x1c8e0
   __DATA_CONST.__got: 0xfe0
   __DATA_CONST.__const: 0x2800
   __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8c20
+  __DATA_CONST.__objc_selrefs: 0x8c60
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x408
   __DATA_CONST.__objc_arraydata: 0x678
   __AUTH_CONST.__auth_got: 0x7b0
   __AUTH_CONST.__const: 0x10c0
-  __AUTH_CONST.__cfstring: 0x5760
-  __AUTH_CONST.__objc_const: 0x2a478
+  __AUTH_CONST.__cfstring: 0x57c0
+  __AUTH_CONST.__objc_const: 0x2a5b8
   __AUTH_CONST.__objc_arrayobj: 0x510
   __AUTH_CONST.__objc_dictobj: 0x730
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x2300
   __AUTH.__data: 0x128
-  __DATA.__objc_ivar: 0x14c4
+  __DATA.__objc_ivar: 0x14dc
   __DATA.__data: 0x2be8
   __DATA.__bss: 0x800
   __DATA_DIRTY.__objc_data: 0x1b80

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F79E7DF3-3F69-3A42-B00D-6E38AEC9DC1A
-  Functions: 5841
-  Symbols:   20897
-  CStrings:  9706
+  UUID: 03E2EC4C-AEB1-31B5-AEE2-FC8CD0B55115
+  Functions: 5857
+  Symbols:   20941
+  CStrings:  9728
 
Symbols:
+ -[SHSheetContentDataSource excludeTopActionViewLess]
+ -[SHSheetContentDataSource initWithState:excludeSectionTypes:topActionsMaximumCount:excludeTopActionViewLess:]
+ -[SHSheetContentDataSource initWithState:excludeSectionTypes:topActionsMaximumCount:excludeTopActionViewLess:].cold.1
+ -[SHSheetContentDataSource setExcludeTopActionViewLess:]
+ -[SHSheetContentDataSourceChangeRequest excludeTopActionViewLess]
+ -[SHSheetContentDataSourceChangeRequest setExcludeTopActionViewLess:]
+ -[SHSheetContentDataSourceManager moreActionExpandedIdentifier]
+ -[SHSheetContentDataSourceManager setMoreActionExpandedIdentifier:]
+ -[SHSheetContentDataSourceState moreActionExpandedIdentifier]
+ -[SHSheetContentDataSourceState setMoreActionExpandedIdentifier:]
+ -[SHSheetPresenter updateHostPortraitWindowSize:]
+ -[SHSheetSession hostPortraitWindowSize]
+ -[SHSheetSession setHostPortraitWindowSize:]
+ -[UIActivityViewController isContentManagedConsideringResponderChain]
+ -[_UIUserDefaultsActivity isExpanded]
+ -[_UIUserDefaultsActivity setIsExpanded:]
+ GCC_except_table126
+ GCC_except_table177
+ GCC_except_table67
+ GCC_except_table75
+ _OBJC_IVAR_$_SHSheetContentDataSource._excludeTopActionViewLess
+ _OBJC_IVAR_$_SHSheetContentDataSourceChangeRequest._excludeTopActionViewLess
+ _OBJC_IVAR_$_SHSheetContentDataSourceManager._moreActionExpandedIdentifier
+ _OBJC_IVAR_$_SHSheetContentDataSourceState._moreActionExpandedIdentifier
+ _OBJC_IVAR_$_SHSheetSession._hostPortraitWindowSize
+ _OBJC_IVAR_$__UIUserDefaultsActivity._isExpanded
+ __OBJC_$_PROP_LIST_SHSheetPresenter.647
+ __OBJC_$_PROP_LIST_SHSheetSession.511
+ __ShareSheetActiveInterfaceOrientation
+ __ShareSheetHostPortraitWindowSize
+ ___block_literal_global.621
+ ___block_literal_global.625
+ _objc_msgSend$_dataOwnerForCopy
+ _objc_msgSend$_windowInterfaceOrientation
+ _objc_msgSend$excludeTopActionViewLess
+ _objc_msgSend$initWithState:excludeSectionTypes:topActionsMaximumCount:excludeTopActionViewLess:
+ _objc_msgSend$isContentManagedConsideringResponderChain
+ _objc_msgSend$moreActionExpandedIdentifier
+ _objc_msgSend$setExcludeTopActionViewLess:
+ _objc_msgSend$setIsExpanded:
+ _objc_msgSend$setMoreActionExpandedIdentifier:
+ _objc_msgSend$updateHostPortraitWindowSize:
- -[SHSheetContentDataSource initWithState:excludeSectionTypes:topActionsMaximumCount:]
- -[SHSheetContentDataSource initWithState:excludeSectionTypes:topActionsMaximumCount:].cold.1
- GCC_except_table176
- GCC_except_table66
- GCC_except_table70
- __OBJC_$_PROP_LIST_SHSheetPresenter.645
- __OBJC_$_PROP_LIST_SHSheetSession.502
- ___block_literal_global.620
- ___block_literal_global.624
- _objc_msgSend$activeInterfaceOrientation
- _objc_msgSend$initWithState:excludeSectionTypes:topActionsMaximumCount:
CStrings:
+ "@44@0:8@16q24Q32B40"
+ "T@\"NSUUID\",C,N,V_moreActionExpandedIdentifier"
+ "TB,N,V_excludeTopActionViewLess"
+ "TB,N,V_isExpanded"
+ "T{CGSize=dd},R,N"
+ "Updating host portrait window size (%f, %f) -> (%f, %f)"
+ "View Less"
+ "View More"
+ "_dataOwnerForCopy"
+ "_excludeTopActionViewLess"
+ "_isExpanded"
+ "_moreActionExpandedIdentifier"
+ "_windowInterfaceOrientation"
+ "chevron.down"
+ "chevron.up"
+ "excludeTopActionViewLess"
+ "initWithState:excludeSectionTypes:topActionsMaximumCount:excludeTopActionViewLess:"
+ "isContentManagedConsideringResponderChain"
+ "moreActionExpandedIdentifier"
+ "setExcludeTopActionViewLess:"
+ "setIsExpanded:"
+ "setMoreActionExpandedIdentifier:"
+ "updateHostPortraitWindowSize:"
- "@40@0:8@16q24Q32"
- "activeInterfaceOrientation"
- "ellipsis"
- "initWithState:excludeSectionTypes:topActionsMaximumCount:"

```
