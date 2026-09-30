## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-  __TEXT.__text: 0x6ed40
-  __TEXT.__objc_methlist: 0x99d0
+  __TEXT.__text: 0x6f144
+  __TEXT.__objc_methlist: 0x9a40
   __TEXT.__const: 0x552
-  __TEXT.__cstring: 0x5996
+  __TEXT.__cstring: 0x59b6
   __TEXT.__oslogstring: 0x3436
   __TEXT.__gcc_except_tab: 0x9bc
   __TEXT.__constg_swiftt: 0x1f8

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0x7c
-  __TEXT.__unwind_info: 0x1f68
+  __TEXT.__unwind_info: 0x1f78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1ef0
+  __DATA_CONST.__const: 0x1f18
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x2e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4310
+  __DATA_CONST.__objc_selrefs: 0x4350
   __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__got: 0x860
   __AUTH_CONST.__const: 0xbc8
-  __AUTH_CONST.__cfstring: 0x5620
-  __AUTH_CONST.__objc_const: 0x21490
+  __AUTH_CONST.__cfstring: 0x5640
+  __AUTH_CONST.__objc_const: 0x214e0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x6c8
-  __AUTH.__objc_data: 0x20a0
-  __AUTH.__data: 0x230
-  __DATA.__objc_ivar: 0xa30
-  __DATA.__data: 0x2070
+  __AUTH.__objc_data: 0x48
+  __DATA.__objc_ivar: 0xa34
+  __DATA.__data: 0x2050
   __DATA.__bss: 0x590
-  __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0x6e0
+  __DATA.__common: 0x18
+  __DATA_DIRTY.__objc_data: 0x2738
+  __DATA_DIRTY.__data: 0x248
   __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3364
-  Symbols:   12383
-  CStrings:  1777
+  Functions: 3374
+  Symbols:   12411
+  CStrings:  1779
 
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
+ _OBJC_IVAR_$_CPListTemplate._useAlternativeCollectionView
+ _OBJC_IVAR_$_CPPanelItem._interactionAllowed
+ _OBJC_IVAR_$_CPPanelItem._panelItemObject
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
- _OBJC_IVAR_$_CPMapPanelItem._interactionAllowed
- _OBJC_IVAR_$_CPMapPanelItem._mapTemplateItemObject
CStrings:
+ "kCPListTemplateUseAlternativeCollectionViewKey"
+ "kCPPanelItemInteractionAllowedKey"
+ "kCPPanelItemObjectKey"
- "kCPMapPanelItemInteractionAllowedKey"
- "kCPMapPanelItemWrappedObjectKey"

```
