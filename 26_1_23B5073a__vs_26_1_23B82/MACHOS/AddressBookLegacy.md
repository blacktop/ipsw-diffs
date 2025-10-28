## AddressBookLegacy

> `/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy`

```diff

-12851.200.61.0.0
-  __TEXT.__text: 0x2628
-  __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__objc_stubs: 0x560
-  __TEXT.__objc_methlist: 0x110
+12851.200.61.2.4
+  __TEXT.__text: 0x2734
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0x580
+  __TEXT.__objc_methlist: 0x11c
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0xb0
-  __TEXT.__objc_methname: 0x519
+  __TEXT.__gcc_except_tab: 0xa4
+  __TEXT.__objc_methname: 0x575
   __TEXT.__cstring: 0x31c
-  __TEXT.__oslogstring: 0x61c
+  __TEXT.__oslogstring: 0x71a
   __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methtype: 0x9e
+  __TEXT.__objc_methtype: 0xad
   __TEXT.__dlopen_cstrs: 0xa3
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x260
+  __TEXT.__unwind_info: 0x120
+  __DATA_CONST.__auth_got: 0x250
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x180

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x130
-  __DATA.__objc_selrefs: 0x180
+  __DATA.__objc_selrefs: 0x190
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x30

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D97CD344-42F2-3C2E-94EB-7F60921AD58D
-  Functions: 40
-  Symbols:   95
-  CStrings:  133
+  UUID: 058CB71D-DDBF-3B73-B40D-5AE7D4B27C84
+  Functions: 41
+  Symbols:   93
+  CStrings:  141
 
Symbols:
+ _objc_release_x26
- _ABAddressBookSetSuppressChangeNotifications
- _objc_release_x24
- _objc_release_x27
CStrings:
+ "@32@0:8@16^v24"
+ "AB Migration - delegate images database found at %@"
+ "AB Migration - delegate images database not found at %@"
+ "AB Migration - main images database found at %@"
+ "AB Migration - main images database not found at %@"
+ "AB Migration - migrating main images database"
+ "_matchUUIDsToPersons:addressBook:"
+ "_recordIDsOfContactsMissingBackgroundColors:"
+ "predicateForContactsWithUUIDs:ignoreUnifiedIdentifiers:"
+ "subarrayWithRange:"
- "_cn_slicesWithMaximumCount:"
- "_contactsMissingBackgroundColors:"

```
