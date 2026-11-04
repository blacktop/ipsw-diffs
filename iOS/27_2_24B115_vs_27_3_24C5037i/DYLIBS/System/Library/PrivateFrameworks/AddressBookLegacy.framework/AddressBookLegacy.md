## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

```diff

-12880.200.21.0.0
-  __TEXT.__text: 0x76c20
-  __TEXT.__objc_methlist: 0x307c
-  __TEXT.__const: 0x371
-  __TEXT.__cstring: 0x2708d
+12880.300.1.0.0
+  __TEXT.__text: 0x7703c
+  __TEXT.__objc_methlist: 0x30f4
+  __TEXT.__const: 0x379
+  __TEXT.__cstring: 0x27182
   __TEXT.__oslogstring: 0x306b
   __TEXT.__gcc_except_tab: 0x644
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x2428
+  __TEXT.__unwind_info: 0x2438
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x2880
-  __DATA_CONST.__objc_classlist: 0x198
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2580
-  __DATA_CONST.__objc_superrefs: 0x100
+  __DATA_CONST.__objc_selrefs: 0x25a8
+  __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x5d8
+  __DATA_CONST.__got: 0x5e0
   __AUTH_CONST.__const: 0xf20
-  __AUTH_CONST.__cfstring: 0xde80
-  __AUTH_CONST.__objc_const: 0x4cb0
+  __AUTH_CONST.__cfstring: 0xdec0
+  __AUTH_CONST.__objc_const: 0x4e40
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__auth_got: 0x1170
-  __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x400
+  __AUTH.__objc_data: 0xa50
+  __DATA.__objc_ivar: 0x414
   __DATA.__data: 0x2c9
   __DATA.__common: 0x4
   __DATA_DIRTY.__objc_data: 0x5f0

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2645
-  Symbols:   4459
-  CStrings:  2562
+  Functions: 2654
+  Symbols:   4481
+  CStrings:  2564
 
Symbols:
+ +[ABPredicate searchPeopleWithPredicate:options:withDelegate:]
+ -[ABNamePredicate authorizationContext]
+ -[ABNamePredicate setAuthorizationContext:]
+ -[ABPredicateSearchOptions addressBook]
+ -[ABPredicateSearchOptions authorizationContext]
+ -[ABPredicateSearchOptions dealloc]
+ -[ABPredicateSearchOptions initWithSortOrder:ranked:addressBook:authorizationContext:]
+ -[ABPredicateSearchOptions ranked]
+ -[ABPredicateSearchOptions sortOrder]
+ GCC_except_table43
+ _ABLimitedAccessContactIdentifierActiveState
+ _OBJC_CLASS_$_ABPredicateSearchOptions
+ _OBJC_IVAR_$_ABNamePredicate._authorizationContext
+ _OBJC_IVAR_$_ABPredicateSearchOptions._addressBook
+ _OBJC_IVAR_$_ABPredicateSearchOptions._authorizationContext
+ _OBJC_IVAR_$_ABPredicateSearchOptions._ranked
+ _OBJC_IVAR_$_ABPredicateSearchOptions._sortOrder
+ _OBJC_METACLASS_$_ABPredicateSearchOptions
+ __OBJC_$_INSTANCE_METHODS_ABPredicateSearchOptions
+ __OBJC_$_INSTANCE_VARIABLES_ABPredicateSearchOptions
+ __OBJC_$_PROP_LIST_ABPredicateSearchOptions
+ __OBJC_CLASS_RO_$_ABPredicateSearchOptions
+ __OBJC_METACLASS_RO_$_ABPredicateSearchOptions
- GCC_except_table36
CStrings:
+ " AND guid IN (SELECT guid FROM LimitedAccess WHERE BundleID = ? AND IsActive = %d)"
+ " INNER JOIN LimitedAccess LimitedAccess_%d ON LimitedAccess_%d.guid = abp.guid AND LimitedAccess_%d.BundleID = ? AND LimitedAccess_%d.IsActive = %d "
+ "CFArrayRef ABAddressBookCopyPeopleWithLinkIdentifiers(ABAddressBookRef, CFArrayRef, CFStringRef)"
- "CFArrayRef ABAddressBookCopyPeopleWithLinkIdentifiers(ABAddressBookRef, CFArrayRef)"
```
