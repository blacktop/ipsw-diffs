## AddressBookLegacy

> `/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy`

```diff

-12851.500.111.0.0
-  __TEXT.__text: 0x27c4
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0x580
+12851.500.121.0.0
+  __TEXT.__text: 0x2758
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0x540
   __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0xa4
-  __TEXT.__objc_methname: 0x575
-  __TEXT.__cstring: 0x31c
+  __TEXT.__objc_methname: 0x554
+  __TEXT.__cstring: 0x30a
   __TEXT.__oslogstring: 0x71a
   __TEXT.__objc_classname: 0x19
   __TEXT.__objc_methtype: 0xad
   __TEXT.__dlopen_cstrs: 0xa3
   __TEXT.__unwind_info: 0x128
-  __DATA_CONST.__auth_got: 0x238
-  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__auth_got: 0x240
+  __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x130
-  __DATA.__objc_selrefs: 0x190
+  __DATA.__objc_selrefs: 0x180
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x30

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F7F413C7-D0F4-3216-85FE-141338D86353
+  UUID: FB6C9BDD-0C82-37FF-982A-106EE0A815BB
   Functions: 44
   Symbols:   90
-  CStrings:  141
+  CStrings:  139
 
Symbols:
+ _objc_release_x23
+ _objc_release_x27
- _OBJC_CLASS_$_CIImage
- _objc_release_x26
Functions:
~ sub_1c84 : 1912 -> 1856
~ sub_261c -> sub_25e4 : 156 -> 104
CStrings:
+ "CNDominantColorAnalyzer"
+ "Class getCNDominantColorAnalyzerClass(void)_block_invoke"
+ "_imageDataForPersonIfNeedsBackgroundColors:"
+ "analyzeAndEncode:count:"
- "CNCoreImageDerivedColorGenerator"
- "Class getCNCoreImageDerivedColorGeneratorClass(void)_block_invoke"
- "_ciImageForPersonIfNeedsBackgroundColors:"
- "encodedDataFromColors:"
- "fetchColorsForImage:"
- "imageWithData:"

```
