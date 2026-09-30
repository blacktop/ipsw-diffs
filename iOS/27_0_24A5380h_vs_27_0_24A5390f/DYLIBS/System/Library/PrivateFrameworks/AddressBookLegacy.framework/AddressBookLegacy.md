## AddressBookLegacy

> `/System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-12875.100.2.0.0
-  __TEXT.__text: 0x77c20
-  __TEXT.__objc_methlist: 0x3074
+12876.100.1.0.0
+  __TEXT.__text: 0x78440
+  __TEXT.__objc_methlist: 0x307c
   __TEXT.__const: 0x371
-  __TEXT.__cstring: 0x26eb5
+  __TEXT.__cstring: 0x26ff0
   __TEXT.__oslogstring: 0x2d7f
   __TEXT.__gcc_except_tab: 0x644
   __TEXT.__dlopen_cstrs: 0xb8
   __TEXT.__ustring: 0x24c
-  __TEXT.__unwind_info: 0x1a88
+  __TEXT.__unwind_info: 0x1aa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2858
+  __DATA_CONST.__const: 0x2880
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2570
+  __DATA_CONST.__objc_selrefs: 0x2580
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x5d8
   __AUTH_CONST.__const: 0xf00
-  __AUTH_CONST.__cfstring: 0xdd80
+  __AUTH_CONST.__cfstring: 0xde40
   __AUTH_CONST.__objc_const: 0x4cb0
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x120

   __DATA.__objc_ivar: 0x400
   __DATA.__data: 0x2c8
   __DATA.__common: 0x4
-  __DATA.__bss: 0x3c0
+  __DATA.__bss: 0x3b0
   __DATA_DIRTY.__objc_data: 0x410
   __DATA_DIRTY.__data: 0x168
-  __DATA_DIRTY.__bss: 0xf8
+  __DATA_DIRTY.__bss: 0x108
   __DATA_DIRTY.__common: 0x398
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2620
-  Symbols:   5442
-  CStrings:  2542
+  Functions: 2627
+  Symbols:   5451
+  CStrings:  2548
 
Symbols:
+ +[ABSQLPredicate predicateForContactsMatchingMultivaluePropertyPrefix:values:groupIdentifiers:containerIdentifiers:limitToOneResult:map:]
+ ___137+[ABSQLPredicate predicateForContactsMatchingMultivaluePropertyPrefix:values:groupIdentifiers:containerIdentifiers:limitToOneResult:map:]_block_invoke
+ ___137+[ABSQLPredicate predicateForContactsMatchingMultivaluePropertyPrefix:values:groupIdentifiers:containerIdentifiers:limitToOneResult:map:]_block_invoke_2
+ ___137+[ABSQLPredicate predicateForContactsMatchingMultivaluePropertyPrefix:values:groupIdentifiers:containerIdentifiers:limitToOneResult:map:]_block_invoke_3
+ ___137+[ABSQLPredicate predicateForContactsMatchingMultivaluePropertyPrefix:values:groupIdentifiers:containerIdentifiers:limitToOneResult:map:]_block_invoke_4
+ ___137+[ABSQLPredicate predicateForContactsMatchingMultivaluePropertyPrefix:values:groupIdentifiers:containerIdentifiers:limitToOneResult:map:]_block_invoke_5
+ ___137+[ABSQLPredicate predicateForContactsMatchingMultivaluePropertyPrefix:values:groupIdentifiers:containerIdentifiers:limitToOneResult:map:]_block_invoke_6
+ ___block_descriptor_76_e8_32o40o48o56o64o_e19_v16?0"ABBinders"8ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
CStrings:
+ "SELECT %@ FROM ABMultivalue abmv %@ %@ WHERE value LIKE ? ESCAPE '\\' AND property = ? %@ %@ %@"
+ "WITH ABQuery(term) AS ( %@ ) SELECT %@ FROM ABMultivalue abmv JOIN ABQuery ON SUBSTR(value, 1, LENGTH(term)) = term COLLATE NOCASE %@ %@ WHERE property = ? %@ %@ %@"
+ "\\%"
+ "\\_"
+ "_"
+ "ab_collect_value_row_map(?, ?, abmv.record_id)"
```
