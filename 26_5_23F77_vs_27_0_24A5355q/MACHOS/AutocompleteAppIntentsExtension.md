## AutocompleteAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/AutocompleteAppIntentsExtension.appex/AutocompleteAppIntentsExtension`

```diff

-28.500.1.0.0
-  __TEXT.__text: 0x1efbc
-  __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0x120
-  __TEXT.__swift5_typeref: 0xe40
-  __TEXT.__const: 0x2e30
-  __TEXT.__cstring: 0xc1a
-  __TEXT.__swift5_reflstr: 0x5e1
-  __TEXT.__swift5_assocty: 0x510
-  __TEXT.__constg_swiftt: 0x2a4
-  __TEXT.__swift5_fieldmd: 0x390
-  __TEXT.__swift5_proto: 0x2b4
-  __TEXT.__swift5_types: 0x48
-  __TEXT.__swift_as_entry: 0x40
-  __TEXT.__swift_as_ret: 0x3c
-  __TEXT.__oslogstring: 0x23a
-  __TEXT.__objc_classname: 0x46
+33.100.1.0.0
+  __TEXT.__text: 0x2246c
+  __TEXT.__auth_stubs: 0x1040
+  __TEXT.__objc_stubs: 0x1c0
+  __TEXT.__objc_methlist: 0x154
+  __TEXT.__swift5_typeref: 0xed4
+  __TEXT.__const: 0x3028
+  __TEXT.__cstring: 0xdea
+  __TEXT.__objc_classname: 0x91
+  __TEXT.__objc_methname: 0x2c5
+  __TEXT.__objc_methtype: 0x100
+  __TEXT.__swift5_reflstr: 0x611
+  __TEXT.__swift5_assocty: 0x530
+  __TEXT.__constg_swiftt: 0x2f4
+  __TEXT.__swift5_fieldmd: 0x3c4
+  __TEXT.__swift5_proto: 0x2c4
+  __TEXT.__swift5_types: 0x4c
+  __TEXT.__swift_as_entry: 0x48
+  __TEXT.__swift_as_ret: 0x44
+  __TEXT.__swift5_capture: 0x30
+  __TEXT.__oslogstring: 0x2fa
+  __TEXT.__swift_as_cont: 0x24
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__objc_methname: 0x97
-  __TEXT.__unwind_info: 0xae8
-  __TEXT.__eh_frame: 0x3c0
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__auth_ptr: 0x550
-  __DATA_CONST.__const: 0xe60
+  __TEXT.__unwind_info: 0xb88
+  __TEXT.__eh_frame: 0x4e8
+  __DATA_CONST.__const: 0xfd0
   __DATA_CONST.__objc_classlist: 0x8
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x48
-  __DATA.__data: 0xaa8
-  __DATA.__bss: 0x5680
-  __DATA.__common: 0xd0
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__auth_got: 0x828
+  __DATA_CONST.__got: 0x340
+  __DATA_CONST.__auth_ptr: 0x588
+  __DATA.__objc_const: 0x1f0
+  __DATA.__objc_selrefs: 0x130
+  __DATA.__data: 0xd70
+  __DATA.__bss: 0x5880
+  __DATA.__common: 0x108
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
+  - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AEC36696-14DF-3B2C-895D-A4D80FDF9EFF
-  Functions: 901
-  Symbols:   96
-  CStrings:  99
+  UUID: D960F2C7-00C8-3124-BF54-4830752ACE17
+  Functions: 956
+  Symbols:   135
+  CStrings:  169
 
Symbols:
+ _CNContactIdentifierKey
+ _OBJC_CLASS_$_CNContact
+ _OBJC_CLASS_$_CNContactStore
+ _OBJC_CLASS_$_CNPhoneNumber
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_release
+ _objc_retain_x20
+ _objc_retain_x25
+ _objc_retain_x8
+ _swift_deallocObject
+ _swift_deallocUninitializedObject
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassMetadata
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_willThrow
CStrings:
+ "#16@0:8"
+ "@\"NSString\"16@0:8"
+ "@16@0:8"
+ "@24@0:8:16"
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@16"
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "CNKeyDescriptor"
+ "Client: %{private}s"
+ "Complete Name (Data)"
+ "Complete a name, returning raw JSON data"
+ "Description for Complete Name Data Intent"
+ "Encoded %ld recipients into %ld bytes"
+ "Failed to resolve recent identifier: %{public}@"
+ "NSCoding"
+ "NSCopying"
+ "NSObject"
+ "NSSecureCoding"
+ "Q16@0:8"
+ "Received %ld recipients"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TB,R"
+ "TQ,R"
+ "The description of the Complete Name Data intent parameter 'client'"
+ "The description of the Complete Name Data intent parameter 'names'"
+ "The label of the Complete Name Data intent parameter 'client'"
+ "The label of the Complete Name Data intent parameter 'names'"
+ "Title for Complete Name Data Intent"
+ "Vv16@0:8"
+ "Will perform CompleteNameDataIntent for %{private}s"
+ "^{_NSZone=}16@0:8"
+ "autorelease"
+ "class"
+ "conformsToProtocol:"
+ "copyWithZone:"
+ "debugDescription"
+ "description"
+ "encodeWithCoder:"
+ "hash"
+ "identifier"
+ "initWithCoder:"
+ "initWithStringValue:"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "predicateForContactsMatchingEmailAddress:"
+ "predicateForContactsMatchingPhoneNumber:"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "superclass"
+ "supportsSecureCoding"
+ "unifiedContactsMatchingPredicate:keysToFetch:error:"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@16"
+ "zone"
- "Client: %s, privacy: .private)"

```
