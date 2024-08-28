## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12721.0.0.0.0
-  __TEXT.__text: 0x7281c
-  __TEXT.__auth_stubs: 0x21b0
-  __TEXT.__objc_methlist: 0x2e14
+12722.1.0.0.0
+  __TEXT.__text: 0x72d6c
+  __TEXT.__auth_stubs: 0x21c0
+  __TEXT.__objc_methlist: 0x2e24
   __TEXT.__const: 0x348
-  __TEXT.__cstring: 0x25f40
-  __TEXT.__oslogstring: 0x1fce
-  __TEXT.__gcc_except_tab: 0x5d4
+  __TEXT.__cstring: 0x25f66
+  __TEXT.__oslogstring: 0x1fd6
+  __TEXT.__gcc_except_tab: 0x5ec
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x1868
+  __TEXT.__unwind_info: 0x1890
   __TEXT.__objc_classname: 0x501
-  __TEXT.__objc_methname: 0x90e9
+  __TEXT.__objc_methname: 0x9139
   __TEXT.__objc_methtype: 0x1454
-  __TEXT.__objc_stubs: 0x7b20
-  __DATA_CONST.__got: 0x5b0
+  __TEXT.__objc_stubs: 0x7b40
+  __DATA_CONST.__got: 0x5b8
   __DATA_CONST.__const: 0x26d0
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2410
+  __DATA_CONST.__objc_selrefs: 0x2418
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x10e8
+  __AUTH_CONST.__auth_got: 0x10f0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0xdf0
-  __AUTH_CONST.__cfstring: 0xd720
+  __AUTH_CONST.__cfstring: 0xd740
   __AUTH_CONST.__objc_const: 0x4db0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2385
-  Symbols:   3635
-  CStrings:  4257
+  Functions: 2393
+  Symbols:   3645
+  CStrings:  4259
 
Symbols:
+ _CNIsArrayEmpty
+ _ABAddLimitedAccessIdentifiersForBundle
+ _CNLogicalNot
+ _ABRemoveContactIdentifiersFromLimitedAccessForAllBundles
+ _ABRemoveLimitedAccessIdentifiersForBundle
+ _SQLInClauseStringForParameterCount
CStrings:
+ "ABRemoveLimitedAccessIdentifiersForBundle remove %!@(MISSING) %!@(MISSING)"
+ " abp.StoreID IN "
+ "appendWhereClauseToQueryString:hasLimitedAccess:"
+ "limitedAccessLeftJoinWhereClause"
+ "bindWhereClause:limitedAccessBundleIdentifier:"
+ " la.BundleID = ? AND la.IsActive = %!i(MISSING)"
+ "BOOL ABAddLimitedAccessIdentifiersForBundle(ABAddressBookRef, NSString *, NSArray<NSString *> *)"
+ "ABRemoveContactIdentifiersFromLimitedAccessForAllBundles remove %!@(MISSING)"
+ "UPDATE LimitedAccess set SequenceNumber = ?, IsActive = ? WHERE BundleID = ?  and guid = ?;"
+ "BOOL ABRemoveLimitedAccessIdentifiersForBundle(ABAddressBookRef, NSString *, NSArray<NSString *> *)"
+ "DELETE FROM LimitedAccess WHERE guid IN %!@(MISSING);"
+ " INNER JOIN LimitedAccess la ON la.guid IN (abp.guid, abplink.guid)"
+ "BOOL ABRemoveContactIdentifiersFromLimitedAccessForAllBundles(ABAddressBookRef, NSArray<NSString *> *)"
- " INNER JOIN LimitedAccess la ON la.guid IN (abp.guid, abplink.guid) WHERE la.BundleID = ? AND la.IsActive = %!i(MISSING)"
- " WHERE abp.StoreID IN "
- "ABRemoveLimitedAccessForBundle.. remove %!@(MISSING) %!@(MISSING)"
- "ABRemoveContactIdentifierFromLimitedAccessForAllBundles.. remove %!@(MISSING)"
- "UPDATE LimitedAccess set SequenceNumber= %!i(MISSING), IsActive = %!i(MISSING) WHERE BundleID = '%!@(MISSING)' and guid = '%!@(MISSING)';"
- "bindWhereClause:"
- "BOOL ABRemoveContactIdentifierFromLimitedAccessForAllBundles(ABAddressBookRef, NSString *)"
- "BOOL ABAddLimitedAccessForBundle(ABAddressBookRef, NSString *, NSString *)"
- "appendWhereClauseToQueryString:"
- "DELETE FROM LimitedAccess WHERE guid = '%!@(MISSING)';"
- "BOOL ABRemoveLimitedAccessForBundle(ABAddressBookRef, NSString *, NSString *)"

```
