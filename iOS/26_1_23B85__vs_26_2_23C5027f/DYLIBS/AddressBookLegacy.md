## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12851.200.61.2.4
-  __TEXT.__text: 0x75624
-  __TEXT.__auth_stubs: 0x2220
-  __TEXT.__objc_methlist: 0x2fac
+12851.300.13.2.1
+  __TEXT.__text: 0x758dc
+  __TEXT.__auth_stubs: 0x2210
+  __TEXT.__objc_methlist: 0x2fc4
   __TEXT.__const: 0x339
-  __TEXT.__cstring: 0x268f6
-  __TEXT.__oslogstring: 0x24b2
-  __TEXT.__gcc_except_tab: 0x618
+  __TEXT.__cstring: 0x268f7
+  __TEXT.__oslogstring: 0x25ea
+  __TEXT.__gcc_except_tab: 0x62c
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x1980
+  __TEXT.__unwind_info: 0x1988
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x91fa
+  __TEXT.__objc_methname: 0x922e
   __TEXT.__objc_methtype: 0x1454
-  __TEXT.__objc_stubs: 0x7ba0
-  __DATA_CONST.__got: 0x5b8
+  __TEXT.__objc_stubs: 0x7c00
+  __DATA_CONST.__got: 0x5c8
   __DATA_CONST.__const: 0x27f8
   __DATA_CONST.__objc_classlist: 0x190
-  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24d0
+  __DATA_CONST.__objc_selrefs: 0x24e8
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x1120
+  __AUTH_CONST.__auth_got: 0x1118
   __AUTH_CONST.__const: 0xe80
   __AUTH_CONST.__cfstring: 0xd9e0
-  __AUTH_CONST.__objc_const: 0x4b40
+  __AUTH_CONST.__objc_const: 0x4b80
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x48

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
   - /System/Library/PrivateFrameworks/ContactsMetrics.framework/ContactsMetrics

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 4012257C-91A2-3E43-9D9C-202247A69D75
-  Functions: 2522
-  Symbols:   7141
-  CStrings:  6061
+  UUID: 09D9BB47-7C2C-30B5-8F5A-C7A7C162D269
+  Functions: 2528
+  Symbols:   7159
+  CStrings:  6068
 
Symbols:
+ -[UTType(ABVCardAdditions) vCardTypeString]
+ GCC_except_table82
+ GCC_except_table90
+ _ABAddressBookCopyAllPeopleForBufferPredicate.cold.1
+ _ABAddressBookCopyAllPeopleForBufferPredicate.cold.2
+ _ABAddressBookCopyAllPeopleForBufferPredicate.cold.3
+ _ABAddressBookCopyAllPeopleForBufferPredicate.cold.4
+ _OBJC_CLASS_$_UTType
+ _UTTypeHEIC
+ _UTTypeJPEG
+ _UTTypePNG
+ _UTTypeTIFF
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UTType_$_ABVCardAdditions
+ __OBJC_$_CATEGORY_UTType_$_ABVCardAdditions
+ ___block_literal_global.173
+ ___block_literal_global.176
+ ___block_literal_global.424
+ ___block_literal_global.81
+ _objc_msgSend$conformsToType:
+ _objc_msgSend$typeWithIdentifier:
+ _objc_msgSend$vCardTypeString
- GCC_except_table81
- GCC_except_table88
- _UTTypeConformsTo
- ___block_literal_global.163
- ___block_literal_global.166
- ___block_literal_global.414
- ___block_literal_global.71
- _kUTTypeJPEG
- _kUTTypePNG
- _kUTTypeTIFF
CStrings:
+ "ABAddressBookCopyAllPeopleForBufferPredicate: ABCPersonClass is NULL"
+ "ABAddressBookCopyAllPeopleForBufferPredicate: Failed to create query string"
+ "ABAddressBookCopyAllPeopleForBufferPredicate: addressBook->dbContext is NULL"
+ "ABAddressBookCopyAllPeopleForBufferPredicate: predicate.query is NULL"
+ "Returning the original image (converted to HEIC)."
+ "conformsToType:"
+ "public.heic"
+ "typeWithIdentifier:"
+ "vCardTypeString"
- "Returning the original image."
- "public.png"

```
