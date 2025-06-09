## Pasteboard

> `/System/Library/PrivateFrameworks/Pasteboard.framework/Pasteboard`

```diff

-8437.0.0.0.0
-  __TEXT.__text: 0x26008
+9071.0.0.0.0
+  __TEXT.__text: 0x2653c
   __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_methlist: 0x2138
+  __TEXT.__objc_methlist: 0x2260
   __TEXT.__const: 0xd0
-  __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__cstring: 0x1ace
-  __TEXT.__gcc_except_tab: 0xa2c
+  __TEXT.__cstring: 0x1a88
+  __TEXT.__gcc_except_tab: 0x9a8
   __TEXT.__oslogstring: 0x10b8
   __TEXT.__ustring: 0xb0
-  __TEXT.__unwind_info: 0xdd8
-  __TEXT.__objc_classname: 0x3c3
-  __TEXT.__objc_methname: 0x663d
-  __TEXT.__objc_methtype: 0xe16
-  __TEXT.__objc_stubs: 0x3720
+  __TEXT.__unwind_info: 0xe00
+  __TEXT.__objc_classname: 0x3e5
+  __TEXT.__objc_methname: 0x68ab
+  __TEXT.__objc_methtype: 0xf0a
+  __TEXT.__objc_stubs: 0x3780
   __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x1458
-  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__const: 0x1420
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x14c0
+  __DATA_CONST.__objc_selrefs: 0x1500
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0xb8
+  __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x3f8
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x1120
-  __AUTH_CONST.__objc_const: 0x2f00
+  __AUTH_CONST.__cfstring: 0x1180
+  __AUTH_CONST.__objc_const: 0x30c0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x420
-  __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_ivar: 0x38
+  __DATA_DIRTY.__objc_ivar: 0x50
   __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x4
   __DATA_DIRTY.__bss: 0x130

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E9FB9189-57DB-3DE6-9970-F3A96E98EFE3
-  Functions: 1033
-  Symbols:   3290
-  CStrings:  1542
+  UUID: 25148A40-BA93-3BCC-92B4-2E9A6AA71A55
+  Functions: 1051
+  Symbols:   3328
+  CStrings:  1563
 
Symbols:
+ +[PBContextMenuDynamicPasteButtonTag supportsSecureCoding]
+ +[PBPasteButtonTag contextMenuDynamicPasteButtonTagWithSecureName:size:titleFrame:iconFrame:layout:layoutSize:]
+ -[PBCalloutBarPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:contextMenuDynamicPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
+ -[PBContextMenuDynamicPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:contextMenuDynamicPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
+ -[PBContextMenuDynamicPasteButtonTag authenticationMessageContextForStyle:]
+ -[PBContextMenuDynamicPasteButtonTag backgroundStatisticsFailingContrastForStyle:]
+ -[PBContextMenuDynamicPasteButtonTag backgroundStatisticsForegroundForStyle:]
+ -[PBContextMenuDynamicPasteButtonTag backgroundStatisticsPassingContrastForStyle:]
+ -[PBContextMenuDynamicPasteButtonTag backgroundStatisticsRegionForStyle:]
+ -[PBContextMenuDynamicPasteButtonTag encodeWithCoder:]
+ -[PBContextMenuDynamicPasteButtonTag hash]
+ -[PBContextMenuDynamicPasteButtonTag iconFrame]
+ -[PBContextMenuDynamicPasteButtonTag initWithCoder:]
+ -[PBContextMenuDynamicPasteButtonTag initWithSecureName:size:titleFrame:iconFrame:layout:layoutSize:]
+ -[PBContextMenuDynamicPasteButtonTag initialSampleEventForStyle:]
+ -[PBContextMenuDynamicPasteButtonTag isEqual:]
+ -[PBContextMenuDynamicPasteButtonTag isValid]
+ -[PBContextMenuDynamicPasteButtonTag layoutSize]
+ -[PBContextMenuDynamicPasteButtonTag layout]
+ -[PBContextMenuDynamicPasteButtonTag resolvedStyleForStyle:]
+ -[PBContextMenuDynamicPasteButtonTag secureNameForStyle:]
+ -[PBContextMenuDynamicPasteButtonTag secureName]
+ -[PBContextMenuDynamicPasteButtonTag size]
+ -[PBContextMenuDynamicPasteButtonTag titleFrame]
+ -[PBContextMenuPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:contextMenuDynamicPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
+ -[PBEditMenuPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:contextMenuDynamicPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
+ -[PBPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:contextMenuDynamicPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
+ -[PBUndoInteractionHUDIconPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:contextMenuDynamicPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
+ -[PBUndoInteractionHUDTextPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:contextMenuDynamicPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
+ _CGRectContainsRect
+ _CGRectEqualToRect
+ _FPCreateBookmarkableStringFromDocumentURL
+ _FPCreateDocumentURLFromBookmarkableString
+ _FPIsFileProviderBookmark
+ _OBJC_CLASS_$_PBContextMenuDynamicPasteButtonTag
+ _OBJC_METACLASS_$_PBContextMenuDynamicPasteButtonTag
+ __OBJC_$_CLASS_METHODS_PBContextMenuDynamicPasteButtonTag
+ __OBJC_$_INSTANCE_METHODS_PBContextMenuDynamicPasteButtonTag
+ __OBJC_$_INSTANCE_VARIABLES_PBContextMenuDynamicPasteButtonTag
+ __OBJC_$_PROP_LIST_PBContextMenuDynamicPasteButtonTag
+ __OBJC_CLASS_RO_$_PBContextMenuDynamicPasteButtonTag
+ __OBJC_METACLASS_RO_$_PBContextMenuDynamicPasteButtonTag
+ ___60-[PBContextMenuDynamicPasteButtonTag resolvedStyleForStyle:]_block_invoke
+ ___block_literal_global.129
+ _objc_msgSend$decodeRectForKey:
+ _objc_msgSend$encodeRect:forKey:
+ _objc_msgSend$initWithSecureName:size:titleFrame:iconFrame:layout:layoutSize:
- -[PBCalloutBarPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
- -[PBContextMenuPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
- -[PBEditMenuPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
- -[PBPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
- -[PBUndoInteractionHUDIconPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
- -[PBUndoInteractionHUDTextPasteButtonTag _acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:editMenuPasteButtonTagVisit:]
- GCC_except_table13
- GCC_except_table6
- _FileProviderLibrary
- _FileProviderLibraryCore.frameworkLibrary
- __FPIsFileProviderBookmark
- ___FileProviderLibraryCore_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_literal_global.117
- ___getFPCreateBookmarkableStringFromDocumentURLSymbolLoc_block_invoke
- ___getFPCreateDocumentURLFromBookmarkableStringSymbolLoc_block_invoke
- ___getFPIsFileProviderBookmarkSymbolLoc_block_invoke
- __sl_dlopen
- _abort_report_np
- _audit_stringFileProvider
- _dlerror
- _dlsym
- _free
- _getFPCreateBookmarkableStringFromDocumentURLSymbolLoc.ptr
- _getFPCreateDocumentURLFromBookmarkableStringSymbolLoc.ptr
- _getFPIsFileProviderBookmarkSymbolLoc.ptr
CStrings:
+ "@116@0:8I16{CGSize=dd}20{CGRect={CGPoint=dd}{CGSize=dd}}36{CGRect={CGPoint=dd}{CGSize=dd}}68q100q108"
+ "@72@0:8@?16@?24@?32@?40@?48@?56@?64"
+ "PBContextMenuDynamicPasteButtonTag"
+ "Tq,R,V_layout"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,V_iconFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,V_titleFrame"
+ "_acceptCalloutBarPasteButtonTagVisit:systemInputAssistantPasteButtonTagVisit:undoInteractionHUDIconPasteButtonTagVisit:undoInteractionHUDTextPasteButtonTagVisit:contextMenuPasteButtonTagVisit:contextMenuDynamicPasteButtonTagVisit:editMenuPasteButtonTagVisit:"
+ "_iconFrame"
+ "_layout"
+ "_titleFrame"
+ "contextMenuDynamicPasteButtonTagWithSecureName:size:titleFrame:iconFrame:layout:layoutSize:"
+ "contextMenuLayout"
+ "decodeRectForKey:"
+ "encodeRect:forKey:"
+ "iconFrame"
+ "initWithSecureName:size:titleFrame:iconFrame:layout:layoutSize:"
+ "layout"
+ "titleFrame"
+ "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "FPCreateBookmarkableStringFromDocumentURL"
- "FPCreateDocumentURLFromBookmarkableString"
- "FPIsFileProviderBookmark"
- "softlink:r:path:/System/Library/Frameworks/FileProvider.framework/FileProvider"

```
