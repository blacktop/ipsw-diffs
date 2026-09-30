## CoreUI

> `/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`

```diff

-973.0.0.0.0
-  __TEXT.__text: 0xca248
+973.1.0.0.0
+  __TEXT.__text: 0xca334
   __TEXT.__auth_stubs: 0x2c10
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0xa298
+  __TEXT.__objc_methlist: 0xa290
   __TEXT.__const: 0x4fd8
   __TEXT.__gcc_except_tab: 0x1624
-  __TEXT.__cstring: 0x2577b
+  __TEXT.__cstring: 0x258bb
   __TEXT.__oslogstring: 0x200
   __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__constg_swiftt: 0x33c

   __TEXT.__swift5_capture: 0x15c
   __TEXT.__swift5_proto: 0x20
   __TEXT.__swift5_assocty: 0x58
-  __TEXT.__unwind_info: 0x3918
+  __TEXT.__unwind_info: 0x3920
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x10e8
-  __TEXT.__objc_methname: 0x16350
+  __TEXT.__objc_methname: 0x16341
   __TEXT.__objc_methtype: 0x5f9b
-  __TEXT.__objc_stubs: 0xe820
+  __TEXT.__objc_stubs: 0xe800
   __DATA_CONST.__got: 0x9e0
   __DATA_CONST.__const: 0xe9d0
   __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f20
+  __DATA_CONST.__objc_selrefs: 0x4f18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x4a8
   __DATA_CONST.__objc_arraydata: 0xbc0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0011AE50-F122-3FF5-962B-63EE2AD8C2D5
-  Functions: 5313
-  Symbols:   15868
-  CStrings:  12137
+  UUID: 0B488C39-EEB5-338F-B19C-EC343E7BFFA5
+  Functions: 5312
+  Symbols:   15865
+  CStrings:  12140
 
Symbols:
- -[CUICommonAssetStorage _swapKeyFormat]
- _objc_msgSend$_swapKeyFormat
Functions:
~ _CUIRenditionKeyInitializeAttributeIndexWithKeyFormat : 164 -> 280
- -[CUICommonAssetStorage _swapKeyFormat]
~ -[CUICommonAssetStorage _commonInitWithStorage:forWritting:] : 1672 -> 1836
~ ___swift_instantiateConcreteTypeFromMangledNameV2 : 72 -> 84
~ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2 : 72 -> 92
CStrings:
+ "CoreUI: %s keyidentifier is > CUIThemeKeyAttributeIndexCount not allowing over write of memory"
+ "CoreUI: Car file '%s' couldn't read header block."
+ "CoreUI: Car file '%s' has malformed tags information ignoring all tags"
+ "CoreUI: Car file '%s' has no header information."
+ "void CUIRenditionKeyInitializeAttributeIndexWithKeyFormat(CUIRenditionKeyAttributeIndex *, const CUIRenditionKeyFormat *)"
- "CoreUI: Car file '%s' has no header information.  Using default values"
- "_swapKeyFormat"

```
