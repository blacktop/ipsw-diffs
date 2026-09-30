## OfficeImport

> `/System/Library/PrivateFrameworks/OfficeImport.framework/OfficeImport`

```diff

-311.0.0.0.0
-  __TEXT.__text: 0x427c98
+313.0.0.0.0
+  __TEXT.__text: 0x427ef4
   __TEXT.__auth_stubs: 0x2d10
-  __TEXT.__objc_methlist: 0x373ec
+  __TEXT.__objc_methlist: 0x3740c
   __TEXT.__const: 0x1679a
-  __TEXT.__gcc_except_tab: 0x52044
+  __TEXT.__gcc_except_tab: 0x52088
   __TEXT.__cstring: 0x24f73
   __TEXT.__ustring: 0x9f8
-  __TEXT.__unwind_info: 0x1c6e8
+  __TEXT.__unwind_info: 0x1c700
   __TEXT.__objc_classname: 0x6dae
-  __TEXT.__objc_methname: 0x554bc
-  __TEXT.__objc_methtype: 0x14cdf
-  __TEXT.__objc_stubs: 0x452c0
+  __TEXT.__objc_methname: 0x554ea
+  __TEXT.__objc_methtype: 0x14cfe
+  __TEXT.__objc_stubs: 0x452e0
   __DATA_CONST.__got: 0xc30
   __DATA_CONST.__const: 0x82a8
   __DATA_CONST.__objc_classlist: 0x2fd8
   __DATA_CONST.__objc_catlist: 0x110
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15e28
+  __DATA_CONST.__objc_selrefs: 0x15e38
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1ae0
   __DATA_CONST.__objc_arraydata: 0x11c0
   __AUTH_CONST.__auth_got: 0x16a0
   __AUTH_CONST.__const: 0x1d3c0
   __AUTH_CONST.__cfstring: 0x29bc0
-  __AUTH_CONST.__objc_const: 0x628e0
+  __AUTH_CONST.__objc_const: 0x628e8
   __AUTH_CONST.__objc_arrayobj: 0x4f8
   __AUTH_CONST.__objc_intobj: 0x6a8
   __AUTH_CONST.__objc_dictobj: 0xf0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 556A4EBD-9AC5-3567-8D86-1B08D4527029
-  Functions: 29341
-  Symbols:   94686
-  CStrings:  32261
+  UUID: FF93B09B-967E-3946-A6F2-5BEEDD12F6FA
+  Functions: 29344
+  Symbols:   94694
+  CStrings:  32264
 
Symbols:
+ -[EDCollection countByEnumeratingWithState:objects:count:]
+ -[EMWorksheetMapper(Private) forceRecountForTesting:]
+ -[EMWorksheetMapper(Private) isCellNonEmpty:state:]
+ _objc_msgSend$isCellNonEmpty:state:
Functions:
+ -[EDCollection countByEnumeratingWithState:objects:count:]
~ -[WMSectionMapper(Private) mapHeaderAt:withState:] : 976 -> 996
~ -[EMWorksheetMapper(Private) countRowsAndColumnsWithState:] : 876 -> 1096
+ -[EMWorksheetMapper(Private) isCellNonEmpty:state:]
+ -[EMWorksheetMapper(Private) forceRecountForTesting:]
CStrings:
+ "B32@0:8^{EDCellHeader=II}16@24"
+ "forceRecountForTesting:"
+ "isCellNonEmpty:state:"

```
