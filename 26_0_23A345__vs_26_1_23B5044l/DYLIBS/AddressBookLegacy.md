## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12851.100.1.0.0
-  __TEXT.__text: 0x74b5c
+12851.200.11.0.0
+  __TEXT.__text: 0x74d3c
   __TEXT.__auth_stubs: 0x21f0
-  __TEXT.__objc_methlist: 0x2fa4
+  __TEXT.__objc_methlist: 0x2fac
   __TEXT.__const: 0x331
-  __TEXT.__cstring: 0x265c4
+  __TEXT.__cstring: 0x26602
   __TEXT.__oslogstring: 0x23f5
   __TEXT.__gcc_except_tab: 0x618
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x1958
+  __TEXT.__unwind_info: 0x1960
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x91aa
+  __TEXT.__objc_methname: 0x91d7
   __TEXT.__objc_methtype: 0x1454
   __TEXT.__objc_stubs: 0x7b80
   __DATA_CONST.__got: 0x5b0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24c0
+  __DATA_CONST.__objc_selrefs: 0x24c8
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x48
   __AUTH_CONST.__auth_got: 0x1108
   __AUTH_CONST.__const: 0xe40
-  __AUTH_CONST.__cfstring: 0xd940
+  __AUTH_CONST.__cfstring: 0xd960
   __AUTH_CONST.__objc_const: 0x4b40
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: CA0848C3-AC49-39F2-9C1A-433561111183
-  Functions: 2512
-  Symbols:   7112
-  CStrings:  6029
+  UUID: 95EBF607-1F42-3CD8-9F0F-1B62D0CDA9A4
+  Functions: 2514
+  Symbols:   7116
+  CStrings:  6032
 
Symbols:
+ +[ABSQLPredicate predicateForContactsWithExternalIdentifiers:]
+ ___62+[ABSQLPredicate predicateForContactsWithExternalIdentifiers:]_block_invoke
CStrings:
+ "SELECT rowid FROM ABPerson WHERE ExternalIdentifier IN ( %@ )"
+ "predicateForContactsWithExternalIdentifiers:"

```
