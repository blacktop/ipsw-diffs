## AddressBookLegacy

> `/System/Library/DataClassMigrators/AddressBookLegacy.migrator/AddressBookLegacy`

```diff

-12851.200.11.0.0
-  __TEXT.__text: 0x1b30
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_stubs: 0x3e0
-  __TEXT.__objc_methlist: 0xe0
-  __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x74
-  __TEXT.__objc_methname: 0x3de
-  __TEXT.__cstring: 0x298
-  __TEXT.__oslogstring: 0x397
+12851.200.41.0.0
+  __TEXT.__text: 0x25f8
+  __TEXT.__auth_stubs: 0x480
+  __TEXT.__objc_stubs: 0x580
+  __TEXT.__objc_methlist: 0x11c
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0xa4
+  __TEXT.__objc_methname: 0x575
+  __TEXT.__cstring: 0x31c
+  __TEXT.__oslogstring: 0x61c
   __TEXT.__objc_classname: 0x19
-  __TEXT.__objc_methtype: 0x8a
+  __TEXT.__objc_methtype: 0xad
   __TEXT.__dlopen_cstrs: 0xa3
-  __TEXT.__unwind_info: 0xf8
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x38
+  __TEXT.__unwind_info: 0x118
+  __DATA_CONST.__auth_got: 0x250
+  __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0xa0
-  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__cfstring: 0x180
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0x130
-  __DATA.__objc_selrefs: 0x120
+  __DATA.__objc_selrefs: 0x190
   __DATA.__objc_ivar: 0xc
   __DATA.__objc_data: 0x50
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AddressBookLegacy.framework/AddressBookLegacy
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1AF8BBF9-B016-37CB-A61D-8A94A17A1C8E
-  Functions: 34
-  Symbols:   81
-  CStrings:  104
+  UUID: 93432817-BEFF-38A5-BAA7-834B2787881A
+  Functions: 41
+  Symbols:   93
+  CStrings:  136
 
Symbols:
+ _ABAddressBookCopyAllPeopleForBufferPredicate
+ _ABPersonCopyImageData
+ _ABPersonHasImageData
+ _ABRecordCopyValue
+ _ABRecordSetValue
+ _OBJC_CLASS_$_ABSQLPredicate
+ _OBJC_CLASS_$_CIImage
+ _OBJC_CLASS_$_NSProcessInfo
+ _kABPersonImageBackgroundColorsDataProperty
+ _objc_release_x26
+ _objc_release_x28
+ _objc_release_x8
CStrings:
+ "@24@0:8^v16"
+ "@32@0:8@16^v24"
+ "AB Migration - Avatar background colors were generated for %li contacts (from %lu candidates), took %fs"
+ "AB Migration - Failed to save batch of avatar background colors, %@"
+ "AB Migration - Failed to set background color data for contact: %@"
+ "AB Migration - Found %lu contacts needing background color generation"
+ "AB Migration - No avatar background colors needed to be generated"
+ "AB Migration - No contacts need background color generation"
+ "AB Migration - Processed batch %lu of %lu: %li contacts in %.2fs (%.2fs per contact)"
+ "AB Migration - Starting background color generation in batches of %lu"
+ "AB Migration - Using batch size: %lu (memory: %llu MB)"
+ "CNCoreImageDerivedColorGenerator"
+ "Class getCNCoreImageDerivedColorGeneratorClass(void)_block_invoke"
+ "Q16@0:8"
+ "SetBackgroundColor"
+ "_ciImageForPersonIfNeedsBackgroundColors:"
+ "_matchUUIDsToPersons:addressBook:"
+ "_optimalBatchSizeForImageProcessing"
+ "_recordIDsOfContactsMissingBackgroundColors:"
+ "count"
+ "encodedDataFromColors:"
+ "fetchColorsForImage:"
+ "generateAvatarBackgroundColorsIfNeeded"
+ "imageWithData:"
+ "physicalMemory"
+ "predicateForContactsMissingBackgroundColors"
+ "predicateForContactsWithUUIDs:ignoreUnifiedIdentifiers:"
+ "processInfo"
+ "subarrayWithRange:"
+ "unknown error"

```
