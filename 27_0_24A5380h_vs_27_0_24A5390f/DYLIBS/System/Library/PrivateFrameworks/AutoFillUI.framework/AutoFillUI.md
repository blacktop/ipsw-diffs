## AutoFillUI

> `/System/Library/PrivateFrameworks/AutoFillUI.framework/AutoFillUI`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-111.0.0.0.0
-  __TEXT.__text: 0x2abe4
-  __TEXT.__objc_methlist: 0x3e90
+113.0.0.0.0
+  __TEXT.__text: 0x2afe4
+  __TEXT.__objc_methlist: 0x3f08
   __TEXT.__const: 0x9b4
-  __TEXT.__cstring: 0x1d74
-  __TEXT.__gcc_except_tab: 0x79c
+  __TEXT.__cstring: 0x1d94
+  __TEXT.__gcc_except_tab: 0x7f4
   __TEXT.__ustring: 0xe6
   __TEXT.__dlopen_cstrs: 0x14e
   __TEXT.__oslogstring: 0x3

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0x40
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xd20
+  __TEXT.__unwind_info: 0xd28
   __TEXT.__eh_frame: 0x1d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc18
-  __DATA_CONST.__objc_classlist: 0x168
+  __DATA_CONST.__const: 0xc58
+  __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ab0
+  __DATA_CONST.__objc_selrefs: 0x2b10
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0xd8
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x288
-  __DATA_CONST.__got: 0x700
+  __DATA_CONST.__got: 0x718
   __AUTH_CONST.__const: 0xa70
-  __AUTH_CONST.__cfstring: 0x1ae0
-  __AUTH_CONST.__objc_const: 0x9498
+  __AUTH_CONST.__cfstring: 0x1b40
+  __AUTH_CONST.__objc_const: 0x9668
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x618
-  __AUTH.__objc_data: 0xce8
+  __AUTH.__objc_data: 0xd38
   __AUTH.__data: 0x2a0
-  __DATA.__objc_ivar: 0x2cc
+  __DATA.__objc_ivar: 0x2dc
   __DATA.__data: 0xe70
   __DATA.__bss: 0xcf0
   __DATA.__common: 0x150

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1300
-  Symbols:   3143
-  CStrings:  315
+  Functions: 1307
+  Symbols:   3176
+  CStrings:  318
 
Symbols:
+ -[AFUICreditCardFieldRow .cxx_destruct]
+ -[AFUICreditCardFieldRow detailText]
+ -[AFUICreditCardFieldRow fillValue]
+ -[AFUICreditCardFieldRow initWithLabel:detailText:fillValue:]
+ -[AFUICreditCardFieldRow label]
+ -[AFUICreditCardViewController displayFieldsByCard]
+ -[AFUICreditCardViewController displayFieldsForCard:]
+ -[AFUICreditCardViewController setDisplayFieldsByCard:]
+ GCC_except_table33
+ _AFTextContentTypeCellularIMEI1Staging
+ _AFTextContentTypeCellularIMEI2Staging
+ _AFTextContentTypeCellularNALStaging
+ _OBJC_CLASS_$_AFUICreditCardFieldRow
+ _OBJC_CLASS_$_UIBlurEffect
+ _OBJC_CLASS_$_UINavigationBarAppearance
+ _OBJC_IVAR_$_AFUICreditCardFieldRow._detailText
+ _OBJC_IVAR_$_AFUICreditCardFieldRow._fillValue
+ _OBJC_IVAR_$_AFUICreditCardFieldRow._label
+ _OBJC_IVAR_$_AFUICreditCardViewController._displayFieldsByCard
+ _OBJC_METACLASS_$_AFUICreditCardFieldRow
+ __OBJC_$_INSTANCE_METHODS_AFUICreditCardFieldRow
+ __OBJC_$_INSTANCE_VARIABLES_AFUICreditCardFieldRow
+ __OBJC_$_PROP_LIST_AFUICreditCardFieldRow
+ __OBJC_CLASS_RO_$_AFUICreditCardFieldRow
+ __OBJC_METACLASS_RO_$_AFUICreditCardFieldRow
+ ___block_descriptor_40_e8_32w_e8_B12?0B8lw32l8
+ _objc_msgSend$configureWithOpaqueBackground
+ _objc_msgSend$detailText
+ _objc_msgSend$displayFieldsByCard
+ _objc_msgSend$displayFieldsForCard:
+ _objc_msgSend$effectWithStyle:
+ _objc_msgSend$fillValue
+ _objc_msgSend$initWithLabel:detailText:fillValue:
+ _objc_msgSend$setBackgroundEffect:
+ _objc_msgSend$setContentScrollView:forEdge:
+ _objc_msgSend$setDisplayFieldsByCard:
+ _objc_msgSend$setStandardAppearance:
- -[AFUIAppCreditCardViewController _cancelTapped]
- GCC_except_table28
- GCC_except_table43
- GCC_except_table6
CStrings:
+ "esim-imei1"
+ "esim-imei2"
+ "esim-nal"
+ "\xc2"
- "\xb2"
```
