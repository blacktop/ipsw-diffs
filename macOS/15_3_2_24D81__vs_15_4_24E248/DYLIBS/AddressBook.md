## AddressBook

> `/System/iOSSupport/System/Library/Frameworks/AddressBook.framework/Versions/A/AddressBook`

```diff

 12669.0.0.0.0
-  __TEXT.__text: 0x1b758
+  __TEXT.__text: 0x1b7e8
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0x1670
+  __TEXT.__objc_methlist: 0x18a4
   __TEXT.__const: 0xd4
   __TEXT.__cstring: 0x1f49
   __TEXT.__ustring: 0x1d6
   __TEXT.__oslogstring: 0x36e
-  __TEXT.__gcc_except_tab: 0x184
-  __TEXT.__unwind_info: 0x708
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__unwind_info: 0x730
   __TEXT.__objc_classname: 0x1e9
   __TEXT.__objc_methname: 0x3a28
   __TEXT.__objc_methtype: 0x76c

   __DATA_CONST.__objc_catlist: 0x128
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1098
+  __DATA_CONST.__objc_selrefs: 0x1118
   __DATA_CONST.__objc_superrefs: 0xa8
   __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0x6a0
   __AUTH_CONST.__cfstring: 0xfe0
-  __AUTH_CONST.__objc_const: 0x2890
+  __AUTH_CONST.__objc_const: 0x2490
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x8

   - /System/Library/PrivateFrameworks/ContactsFoundation.framework/Versions/A/ContactsFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 297078FF-EDAD-358D-8AF4-61B5ADFBEFA9
-  Functions: 672
-  Symbols:   2035
+  UUID: 51AF78A1-1E0C-3680-977E-7E957BFD4343
+  Functions: 695
+  Symbols:   2061
   CStrings:  1199
 
Symbols:
+ +[ABSConstantsMapping ABToCNContactSortOrderConstantsMapping].cold.1
+ +[ABSConstantsMapping ABToCNContainerTypeConstantsMapping].cold.1
+ +[ABSConstantsMapping ABToCNLabelConstantsMapping].cold.1
+ +[ABSConstantsMapping ABToCNPersonAddressConstantsMapping].cold.1
+ +[ABSConstantsMapping ABToCNPersonInstantMessageConstantsMapping].cold.1
+ +[ABSConstantsMapping ABToCNPersonKindConstantsMapping].cold.1
+ +[ABSConstantsMapping ABToCNPersonSocialProfileConstantsMapping].cold.1
+ +[ABSConstantsMapping ABtoCNContactDisplayNameOrderConstantsMapping].cold.1
+ +[ABSLog apiLog].cold.1
+ +[ABSLog log].cold.1
+ +[ABSPerson defaultKeysToFetch].cold.1
+ -[ABSPersonFetchRequest initWithPredicate:additionalKeysToFetch:sortOrder:].cold.3
+ -[ABSPersonFetchRequest initWithPredicate:additionalKeysToFetch:sortOrder:].cold.4
+ ABAddressBookCreate.cold.1
+ ABAddressBookCreateWithOptions.cold.1
+ ABAddressBookCreateWithOptionsAndPolicy.cold.1
+ ABMultiValueCreateMutable.cold.1
+ ABMultiValueCreateMutableCopy.cold.1
+ ABSAddressBookGetTypeID.cold.1
+ ABSIsAPILogEnabled.cold.1
+ ABSMultiValueGetTypeID.cold.1
+ ABSPeoplePickerPrefs.cold.1
+ ABSRecordGetTypeID.cold.1
+ initCNAssistantConversion.cold.1
+ socialProfileFromURL.cold.1
+ socialProfileURLForServiceAndUsername.cold.1

```
