## SoftwareUpdate

> `/System/Library/PrivateFrameworks/SoftwareUpdate.framework/Versions/A/SoftwareUpdate`

```diff

-  __TEXT.__text: 0x7c974
-  __TEXT.__objc_methlist: 0x64b4
+  __TEXT.__text: 0x7ca80
+  __TEXT.__objc_methlist: 0x64dc
   __TEXT.__const: 0x670
   __TEXT.__gcc_except_tab: 0x12a8
-  __TEXT.__cstring: 0x8419
-  __TEXT.__oslogstring: 0xb489
+  __TEXT.__cstring: 0x844c
+  __TEXT.__oslogstring: 0xb44b
   __TEXT.__dof_SoftwareU: 0xc20
-  __TEXT.__unwind_info: 0x2200
+  __TEXT.__unwind_info: 0x21f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xa68
+  __DATA_CONST.__const: 0xa78
   __DATA_CONST.__objc_classlist: 0x230
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f30
+  __DATA_CONST.__objc_selrefs: 0x3f58
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x70
-  __DATA_CONST.__got: 0x6c8
+  __DATA_CONST.__got: 0x718
   __AUTH_CONST.__const: 0x29e0
-  __AUTH_CONST.__cfstring: 0x7380
-  __AUTH_CONST.__objc_const: 0x8960
+  __AUTH_CONST.__cfstring: 0x73a0
+  __AUTH_CONST.__objc_const: 0x8980
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__auth_got: 0x800
   __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x798
+  __DATA.__objc_ivar: 0x79c
   __DATA.__data: 0x5c0
   __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xe60

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  Functions: 3204
-  Symbols:   7048
-  CStrings:  2902
+  Functions: 3206
+  Symbols:   7054
+  CStrings:  2903
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__dof_SoftwareU : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[SUPreferenceManager setLastLivabilityEnrollmentDate]
+ -[SUPreferenceManager setMobileAssetPersonalizationServerURL:]
+ -[SUPreferenceManager setPersonalizationServerURL:]
+ -[SUSharedPrefs lastLivabilityEnrollmentDate]
+ -[SUSharedPrefs personalizationServerURL]
+ GCC_except_table72
+ GCC_except_table75
+ GCC_except_table78
+ GCC_except_table81
+ GCC_except_table84
+ OBJC_IVAR_$_SUPreferenceManager._customPersonalizationSigningServerURLString
+ _SULastLivabilityEnrollmentDateKey
+ _SUMobileAssetPersonalizationServerURLKey
+ _SUPersonalizationServerURLKey
+ _objc_msgSend$now
- -[SUSharedPrefs customPersonalizationSigningServerURLString]
- -[SUSharedPrefs personalizationEnabled]
- GCC_except_table30
- GCC_except_table73
- GCC_except_table76
- GCC_except_table82
- _SUPrefsCustomPersonalizationSigningServerURLString
CStrings:
+ "LastLivabilityEnrollmentDate"
+ "MobileAssetPersonalizationServerURL"
+ "PersonalizationServerURL"
- "EnablePersonalization"
- "SUUpdateServiceClient: setIASUCatalogWithValue: value is nil."
- "SigningServerURL"

```
