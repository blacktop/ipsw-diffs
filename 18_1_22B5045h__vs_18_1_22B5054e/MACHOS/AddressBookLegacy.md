## AddressBookLegacy

> `/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy`

```diff

-12723.0.0.0.0
-  __TEXT.__text: 0x1370
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_stubs: 0x2e0
-  __TEXT.__objc_methlist: 0xc8
+12725.0.0.0.0
+  __TEXT.__text: 0x1740
+  __TEXT.__auth_stubs: 0x3e0
+  __TEXT.__objc_stubs: 0x320
+  __TEXT.__objc_methlist: 0xd4
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x7c
-  __TEXT.__objc_methname: 0x312
-  __TEXT.__cstring: 0x209
-  __TEXT.__oslogstring: 0x1fd
+  __TEXT.__objc_methname: 0x359
+  __TEXT.__cstring: 0x225
+  __TEXT.__oslogstring: 0x2de
   __TEXT.__objc_classname: 0x19
   __TEXT.__objc_methtype: 0x8a
   __TEXT.__dlopen_cstrs: 0xa3
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__auth_got: 0x1a8
-  __DATA_CONST.__got: 0x30
+  __TEXT.__unwind_info: 0xf0
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__cfstring: 0x100
+  __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x130
-  __DATA.__objc_selrefs: 0xe8
+  __DATA.__objc_selrefs: 0xf8
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
   __DATA.__bss: 0x20

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 27
-  Symbols:   67
-  CStrings:  76
+  Functions: 29
+  Symbols:   79
+  CStrings:  83
 
Symbols:
+ _ABRecordGetIntValue
+ _objc_enumerationMutation
+ _kABSourceTypeProperty
+ _ABAddressBookRemoveRecord
+ _objc_retain
+ _ABAddressBookSave
+ _ABAddressBookGetIntegerProperty
+ _objc_release_x25
+ _ABAddressBookHasUnsavedChanges
+ _ABAddressBookCreate
+ _ABAddressBookSetIntegerProperty
+ _ABAddressBookCopyArrayOfAllSources
CStrings:
+ "AB Migration - Contact Provider container was not deleted, %!@(MISSING)"
+ "AB Migration - Contact Provider did reset, took %!f(MISSING)s"
+ "AB Migration - Failed to save Contact Provider content deletion, %!@(MISSING)"
+ "AB Migration - Contact Provider will reset"
+ "resetContactProviderFeature"
+ "ResetContactProviderFeature"
+ "countByEnumeratingWithState:objects:count:"

```
