## ContactsAutocompleteUI

> `/System/Library/PrivateFrameworks/ContactsAutocompleteUI.framework/ContactsAutocompleteUI`

```diff

-812.100.2.2.3
-  __TEXT.__text: 0x45944
+814.100.1.0.0
+  __TEXT.__text: 0x45abc
   __TEXT.__auth_stubs: 0xb00
   __TEXT.__objc_methlist: 0x703c
   __TEXT.__const: 0x424
   __TEXT.__cstring: 0x172e
   __TEXT.__gcc_except_tab: 0x4fc
-  __TEXT.__oslogstring: 0xb8d
+  __TEXT.__oslogstring: 0xbc5
   __TEXT.__ustring: 0x14
   __TEXT.__dlopen_cstrs: 0x4a
   __TEXT.__swift5_typeref: 0x26

   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__unwind_info: 0x13d8
+  __TEXT.__unwind_info: 0x13d0
   __TEXT.__objc_classname: 0xcfd
-  __TEXT.__objc_methname: 0x14c75
+  __TEXT.__objc_methname: 0x14c98
   __TEXT.__objc_methtype: 0x52c7
   __TEXT.__objc_stubs: 0xd980
-  __DATA_CONST.__got: 0x8e0
-  __DATA_CONST.__const: 0x1378
+  __DATA_CONST.__got: 0x8f0
+  __DATA_CONST.__const: 0x1358
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x128

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2FA9BD9A-F70E-39D4-9E8B-A47BD592F685
-  Functions: 1971
-  Symbols:   7472
+  UUID: 66B61CB2-CFBE-3D57-A842-24F3F52F780E
+  Functions: 1966
+  Symbols:   7453
   CStrings:  4241
 
Symbols:
+ _UIApp
+ _UIFontTextStyleTitle1
+ ___block_literal_global.725
+ ___block_literal_global.751
+ _isPortraitIPhone
+ _objc_msgSend$activeInterfaceOrientation
+ _objc_msgSend$imageByApplyingSymbolConfiguration:
- -[CNAutocompleteSearchManager _handleContactsAutocompleteSearch:returnedResults:taskID:].cold.1
- -[CNAutocompleteSearchManager _handleContactsAutocompleteSearchFinished:taskID:].cold.1
- -[CNAutocompleteSearchManager _handleTaskFinished:context:].cold.1
- -[CNAutocompleteSearchManager cancelTaskWithID:].cold.1
- -[CNAutocompleteSearchManager searchForText:withAutocompleteFetchContext:consumer:].cold.1
- ___45-[CNContactsAutocompleteSearchOperation main]_block_invoke_2.cold.1
- ___block_literal_global.724
- ___block_literal_global.750
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_ContactsAutocompleteUI_Private
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ContactsAutocompleteUI_Private
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ContactsAutocompleteUI_Private
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ContactsAutocompleteUI_Private
- _objc_msgSend$contactType
- _objc_msgSend$setContactType:
CStrings:
+ "Beginning CNContactsAutocompleteSearchOperation for \"%{private}@\" (task %{public}@)"
+ "CNAutocompleteFetch Error for task %{public}@: %@"
+ "activeInterfaceOrientation"
+ "canceling CNAutocompleteFetch for task %{public}@"
+ "imageByApplyingSymbolConfiguration:"
+ "task %{public}@ cancelled"
+ "task %{public}@ finished"
+ "task %{public}@ found %ld autocomplete results"
- "Beginning CNContactsAutocompleteSearchOperation for \"%@\" (task %@)"
- "CNAutocompleteFetch Error for task %@: %@"
- "canceling CNAutocompleteFetch for task %@"
- "contactType"
- "setContactType:"
- "task %@ cancelled"
- "task %@ finished"
- "task %@: found %ld autocomplete results"

```
