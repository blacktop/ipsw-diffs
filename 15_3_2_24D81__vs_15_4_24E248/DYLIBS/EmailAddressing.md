## EmailAddressing

> `/System/Library/PrivateFrameworks/EmailAddressing.framework/Versions/A/EmailAddressing`

```diff

-3826.400.131.1.6
-  __TEXT.__text: 0x6f4c
+3826.500.181.1.5
+  __TEXT.__text: 0x6f44
   __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x408
-  __TEXT.__gcc_except_tab: 0xac8
+  __TEXT.__objc_methlist: 0x55c
+  __TEXT.__gcc_except_tab: 0xae4
   __TEXT.__cstring: 0x269
-  __TEXT.__const: 0x48
+  __TEXT.__const: 0x38
   __TEXT.__ustring: 0x4
   __TEXT.__oslogstring: 0x77
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x3e0
   __TEXT.__objc_classname: 0xc8
   __TEXT.__objc_methname: 0xfb4
   __TEXT.__objc_methtype: 0x255

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a0
+  __DATA_CONST.__objc_selrefs: 0x528
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x190
   __AUTH_CONST.__const: 0xf0
   __AUTH_CONST.__cfstring: 0x6e0
-  __AUTH_CONST.__objc_const: 0x988
+  __AUTH_CONST.__objc_const: 0x720
   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x10
   __DATA.__data: 0x190

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 394F531E-DFD0-3ACF-A959-DFD39E667D67
-  Functions: 94
-  Symbols:   456
+  UUID: E2A354A8-2FBB-331E-AC85-53A72CCF9704
+  Functions: 100
+  Symbols:   462
   CStrings:  338
 
Symbols:
+ +[EAEmailAddressGenerator formattedAddressWithName:email:useQuotes:].cold.1
+ +[EAEmailAddressLists addressListFromHeaderValue:].cold.1
+ +[EAEmailAddressParser displayNameFromAddress:cacheResults:].cold.1
+ +[EAEmailAddressParser rawAddressFromFullAddress:cacheResults:].cold.1
+ -[NSString(EmailAddressingAdditions) ea_isLegalEmailAddress].cold.1
+ _createStringByApplyingIDNATranslationWithRange.cold.1

```
