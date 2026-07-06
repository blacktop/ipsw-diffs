## CarPlay

> `/System/iOSSupport/System/Library/Frameworks/CarPlay.framework/Versions/A/CarPlay`

```diff

-  __TEXT.__text: 0x5c204
-  __TEXT.__objc_methlist: 0x8f08
+  __TEXT.__text: 0x5c608
+  __TEXT.__objc_methlist: 0x8f78
   __TEXT.__const: 0x35a
-  __TEXT.__cstring: 0x5236
+  __TEXT.__cstring: 0x5256
   __TEXT.__oslogstring: 0x218e
   __TEXT.__gcc_except_tab: 0x79c
   __TEXT.__constg_swiftt: 0x134

   __TEXT.__swift5_fieldmd: 0x64
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1c08
+  __TEXT.__unwind_info: 0x1c18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c98
+  __DATA_CONST.__const: 0x1cc0
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3bd8
+  __DATA_CONST.__objc_selrefs: 0x3c18
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x340
   __DATA_CONST.__got: 0x658
   __AUTH_CONST.__const: 0x988
-  __AUTH_CONST.__cfstring: 0x5200
-  __AUTH_CONST.__objc_const: 0x1f500
+  __AUTH_CONST.__cfstring: 0x5220
+  __AUTH_CONST.__objc_const: 0x1f540
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x548
-  __AUTH.__objc_data: 0x20a0
-  __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0x9f0
-  __DATA.__data: 0x1960
+  __AUTH.__objc_data: 0x48
+  __DATA.__objc_ivar: 0x9f4
+  __DATA.__data: 0x1940
   __DATA.__bss: 0x310
-  __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x2738
+  __DATA_DIRTY.__data: 0x1f8
   __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3054
-  Symbols:   8126
-  CStrings:  1591
+  Functions: 3064
+  Symbols:   8144
+  CStrings:  1593
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
Symbols:
+ -[CPListImageRowItem _registerThumbnailUpdaterForElements:]
+ -[CPListSection replaceItem:]
+ -[CPListTemplate setUseAlternativeCollectionView:]
+ -[CPListTemplate useAlternativeCollectionView]
+ -[CPMapPanelItem _allowedPanelItemObjectClasses]
+ -[CPPanelItem _allowedPanelItemObjectClasses]
+ -[CPPanelItem _initWithObject:interactionAllowed:]
+ -[CPPanelItem initWithGridButtons:]
+ -[CPPanelItem initWithListItem:]
+ -[CPPanelItem interactionAllowed]
+ -[CPPanelItem panelItemObject]
+ -[CPPanelItem setInteractionAllowed:]
+ -[CPPanelItem setPanelItemObject:]
+ OBJC_IVAR_$_CPListTemplate._useAlternativeCollectionView
+ OBJC_IVAR_$_CPPanelItem._interactionAllowed
+ OBJC_IVAR_$_CPPanelItem._panelItemObject
+ ___29-[CPListSection replaceItem:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e37_v32?0"<CPListTemplateItem>"8Q16^B24ls32l8s40l8s48l8
+ _objc_msgSend$_allowedPanelItemObjectClasses
+ _objc_msgSend$_initWithObject:interactionAllowed:
+ _objc_msgSend$_registerThumbnailUpdaterForElements:
+ _objc_msgSend$panelItemObject
+ _objc_msgSend$replaceItemAtIndex:withItem:
+ _objc_msgSend$useAlternativeCollectionView
- -[CPMapPanelItem initWithGridButtons:]
- -[CPMapPanelItem initWithListItem:]
- -[CPMapPanelItem interactionAllowed]
- -[CPMapPanelItem setInteractionAllowed:]
- OBJC_IVAR_$_CPMapPanelItem._interactionAllowed
- OBJC_IVAR_$_CPMapPanelItem._mapTemplateItemObject
CStrings:
+ "kCPListTemplateUseAlternativeCollectionViewKey"
+ "kCPPanelItemInteractionAllowedKey"
+ "kCPPanelItemObjectKey"
- "kCPMapPanelItemInteractionAllowedKey"
- "kCPMapPanelItemWrappedObjectKey"

```
