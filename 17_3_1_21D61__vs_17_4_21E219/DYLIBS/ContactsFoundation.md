## ContactsFoundation

> `/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation`

```diff

-1237.0.0.0.0
-  __TEXT.__text: 0x7dd78
-  __TEXT.__auth_stubs: 0x17a0
-  __TEXT.__objc_methlist: 0x9330
-  __TEXT.__cstring: 0x6c4b
+1238.2.0.0.0
+  __TEXT.__text: 0x7ef00
+  __TEXT.__auth_stubs: 0x17c0
+  __TEXT.__objc_methlist: 0x9418
+  __TEXT.__cstring: 0x6f0b
   __TEXT.__const: 0x3a8
-  __TEXT.__oslogstring: 0x1cf8
+  __TEXT.__oslogstring: 0x1e3d
   __TEXT.__gcc_except_tab: 0x10bc
   __TEXT.__ustring: 0x2e2
   __TEXT.__dlopen_cstrs: 0xb5

   __TEXT.__swift5_fieldmd: 0xdc
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__unwind_info: 0x3064
+  __TEXT.__unwind_info: 0x30cc
   __TEXT.__eh_frame: 0x88
-  __TEXT.__objc_classname: 0x1fae
-  __TEXT.__objc_methname: 0x11c63
-  __TEXT.__objc_methtype: 0x2d20
-  __TEXT.__objc_stubs: 0xcdc0
-  __DATA_CONST.__got: 0x308
-  __DATA_CONST.__const: 0x3550
-  __DATA_CONST.__objc_classlist: 0x918
+  __TEXT.__objc_classname: 0x201a
+  __TEXT.__objc_methname: 0x11def
+  __TEXT.__objc_methtype: 0x2d6a
+  __TEXT.__objc_stubs: 0xce60
+  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__const: 0x3558
+  __DATA_CONST.__objc_classlist: 0x930
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x1c0
+  __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf050
-  __DATA_CONST.__objc_selrefs: 0x4698
+  __DATA_CONST.__objc_const: 0xf2d8
+  __DATA_CONST.__objc_selrefs: 0x46e8
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_classrefs: 0x950
+  __DATA_CONST.__objc_superrefs: 0x558
   __DATA_CONST.__objc_arraydata: 0x9c90
-  __AUTH_CONST.__cfstring: 0xa6a0
-  __AUTH_CONST.__objc_const: 0x6220
-  __AUTH_CONST.__const: 0x1f70
+  __AUTH_CONST.__cfstring: 0xa6e0
+  __AUTH_CONST.__objc_const: 0x6340
+  __AUTH_CONST.__const: 0x1f90
   __AUTH_CONST.__objc_dictobj: 0x2580
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__auth_got: 0xbe0
-  __AUTH.__objc_data: 0x2b00
+  __AUTH_CONST.__auth_got: 0xbf0
+  __AUTH.__objc_data: 0x2ba0
   __AUTH.__data: 0xf8
-  __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x930
-  __DATA.__objc_superrefs: 0x550
-  __DATA.__objc_ivar: 0x798
+  __DATA.__objc_ivar: 0x7a4
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x1908
-  __DATA.__bss: 0x2c8
-  __DATA_DIRTY.__objc_data: 0x32a0
+  __DATA.__data: 0x1a08
+  __DATA.__bss: 0x2d8
+  __DATA.__common: 0x0
+  __DATA_DIRTY.__objc_data: 0x32f0
   __DATA_DIRTY.__data: 0x58
   __DATA_DIRTY.__bss: 0x560
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4BE74AD2-4494-39CE-A081-7238CF5D38F0
-  Functions: 4308
-  Symbols:   14299
-  CStrings:  6910
+  UUID: 5CF330B6-BBA4-3F56-BB5A-B76CA42C1839
+  Functions: 4341
+  Symbols:   14403
+  CStrings:  6960
 
Symbols:
+ +[CNAuditTokenUtilities _bundleIdentifierFromInfoPlistForAuditToken:].cold.2
+ +[CNAuditTokenUtilities _bundleIdentifierFromSecTaskForAuditToken:]
+ +[CNAuditTokenUtilities _bundleIdentifierFromSecTaskForAuditToken:].cold.1
+ +[CNAuditTokenUtilities _bundleIdentifierFromSecTaskForAuditToken:].cold.2
+ +[CNAuditTokenUtilities _bundleIdentifierFromSecTaskForAuditToken:].cold.3
+ +[CNEncryptionHelper decryptAddressingGrammarString:].cold.1
+ +[CNEncryptionHelper decryptAddressingGrammarString:].cold.2
+ +[CNPostalAddressFormats _unitTestableLocalizedStringForPostalAddressString:returningNilIfNotFound:]
+ +[CNPostalAddressFormats makeLocalizer]
+ +[CNPostalAddressFormats sharedLocalizer]
+ +[CNWatchdog defaultWatchdog]
+ -[CNEnvironment isGreenTeaDevice]
+ -[CNEnvironment watchdog]
+ -[CNEnvironmentTestDouble setGreenTeaDevice:]
+ -[CNEnvironmentTestDouble setWatchdog:]
+ -[CNManagedConfiguration hasContactProviderRestrictions]
+ -[CNManagedConfiguration initForContactProvider]
+ -[CNWatchdog .cxx_destruct]
+ -[CNWatchdog init]
+ -[CNWatchdog recordExceptionForEvent:]
+ -[CNWatchdog setStatus:forEvent:]
+ -[CNWatchdog statusForEvent:]
+ -[_GreenTeaPostalAddressLocalizer localizedStringForPostalAddressString:returningNilIfNotFound:]
+ -[_StandardPostalAddressLocalizer localizedStringForPostalAddressString:returningNilIfNotFound:]
+ OBJC_IVAR_$_CNEnvironment._isGreenTeaDeviceStorage
+ OBJC_IVAR_$_CNEnvironment._watchdog
+ _CNWatchdogEventSuggestionsTimeout
+ _GetBundle.cn_once_object_1
+ _GetBundle.cn_once_token_1
+ _OBJC_CLASS_$_CNWatchdog
+ _OBJC_CLASS_$__GreenTeaPostalAddressLocalizer
+ _OBJC_CLASS_$__StandardPostalAddressLocalizer
+ _OBJC_IVAR_$_CNWatchdog._events
+ _OBJC_METACLASS_$_CNWatchdog
+ _OBJC_METACLASS_$__GreenTeaPostalAddressLocalizer
+ _OBJC_METACLASS_$__StandardPostalAddressLocalizer
+ __OBJC_$_CLASS_METHODS_CNWatchdog
+ __OBJC_$_CLASS_PROP_LIST_CNWatchdog
+ __OBJC_$_INSTANCE_METHODS_CNWatchdog
+ __OBJC_$_INSTANCE_METHODS__GreenTeaPostalAddressLocalizer
+ __OBJC_$_INSTANCE_METHODS__StandardPostalAddressLocalizer
+ __OBJC_$_INSTANCE_VARIABLES_CNWatchdog
+ __OBJC_$_PROP_LIST_CNAuthorizationContext.223
+ __OBJC_$_PROP_LIST_CNEncodedFetchResponse.88
+ __OBJC_$_PROP_LIST_CNFoundationUserDefaults.120
+ __OBJC_$_PROP_LIST_CNFuture.152
+ __OBJC_$_PROP_LIST_CNSchedulerProvider.107
+ __OBJC_$_PROP_LIST_CNTimeProvider.50
+ __OBJC_$_PROP_LIST_CNWatchdog
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CNPostalAddressFormatsLocalizer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CNWatchdog
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNPostalAddressFormatsLocalizer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNWatchdog
+ __OBJC_$_PROTOCOL_REFS_CNWatchdog
+ __OBJC_CLASS_PROTOCOLS_$_CNWatchdog
+ __OBJC_CLASS_PROTOCOLS_$__GreenTeaPostalAddressLocalizer
+ __OBJC_CLASS_PROTOCOLS_$__StandardPostalAddressLocalizer
+ __OBJC_CLASS_RO_$_CNWatchdog
+ __OBJC_CLASS_RO_$__GreenTeaPostalAddressLocalizer
+ __OBJC_CLASS_RO_$__StandardPostalAddressLocalizer
+ __OBJC_LABEL_PROTOCOL_$_CNPostalAddressFormatsLocalizer
+ __OBJC_LABEL_PROTOCOL_$_CNWatchdog
+ __OBJC_METACLASS_RO_$_CNWatchdog
+ __OBJC_METACLASS_RO_$__GreenTeaPostalAddressLocalizer
+ __OBJC_METACLASS_RO_$__StandardPostalAddressLocalizer
+ __OBJC_PROTOCOL_$_CNPostalAddressFormatsLocalizer
+ __OBJC_PROTOCOL_$_CNWatchdog
+ __PROTOCOLS__TtC18ContactsFoundation26CNKeychainFacadeTestDouble.19
+ ___33-[CNEnvironment isGreenTeaDevice]_block_invoke
+ ___39-[CNEnvironmentTestDouble setWatchdog:]_block_invoke
+ ___41+[CNPostalAddressFormats sharedLocalizer]_block_invoke
+ ___45-[CNEnvironmentTestDouble setGreenTeaDevice:]_block_invoke
+ ___GetBundle_block_invoke
+ ___block_literal_global.122
+ ___block_literal_global.199
+ ___block_literal_global.595
+ ___block_literal_global.74
+ ___block_literal_global.76
+ ___block_literal_global.90
+ _objc_msgSend$_bundleIdentifierFromSecTaskForAuditToken:
+ _objc_msgSend$defaultWatchdog
+ _objc_msgSend$localizedStringForPostalAddressString:returningNilIfNotFound:
+ _objc_msgSend$makeLocalizer
+ _objc_msgSend$setStatus:forEvent:
+ _objc_msgSend$sharedLocalizer
+ _sharedLocalizer.cn_once_object_2
+ _sharedLocalizer.cn_once_token_2
- +[CNAuditTokenUtilities _bundleIdentifierFromEntitlementForAuditToken:]
- -[CNManagedConfiguration hasContactsProviderRestrictions]
- -[CNManagedConfiguration initForContactsProvider]
- __OBJC_$_PROP_LIST_CNAuthorizationContext.225
- __OBJC_$_PROP_LIST_CNEncodedFetchResponse.87
- __OBJC_$_PROP_LIST_CNFoundationUserDefaults.119
- __OBJC_$_PROP_LIST_CNFuture.151
- __OBJC_$_PROP_LIST_CNSchedulerProvider.106
- __OBJC_$_PROP_LIST_CNTimeProvider.49
- __PROTOCOLS__TtC18ContactsFoundation26CNKeychainFacadeTestDouble.20
- ___block_literal_global.120
- ___block_literal_global.198
- ___block_literal_global.594
- ___block_literal_global.70
- ___block_literal_global.89
- _objc_msgSend$_bundleIdentifierFromEntitlementForAuditToken:
- _objc_retain_x10
CStrings:
+ "\x0f\x01"
+ "@\"<CNWatchdog>\""
+ "@\"NSString\"28@0:8@\"NSString\"16B24"
+ "CNPostalAddressFormatsLocalizer"
+ "CNPostalAddressValues_cn"
+ "CNWatchdog"
+ "Could not look up Entitlement Application Identifier using SecTaskRef."
+ "Could not look up SecTaskRef using audit token."
+ "Could not look up Signing Identifier using SecTaskRef, %@"
+ "Could not look up proc_pidpath using pid %d."
+ "Failed to decrypt pronoun, empty string supplied"
+ "Failed to decrypt pronoun, invalid base64 string supplied"
+ "Fatal error"
+ "Insufficient space allocated to copy string contents"
+ "Looked up bundle ID %@ from audit token using SecTask."
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "T@\"<CNWatchdog>\",&,D"
+ "T@\"<CNWatchdog>\",R"
+ "T@\"<CNWatchdog>\",R,V_watchdog"
+ "T@\"NSString\",?,R,C"
+ "TB,D,GisGreenTeaDevice"
+ "TB,R,GisGreenTeaDevice"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.moveInitialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "_GreenTeaPostalAddressLocalizer"
+ "_StandardPostalAddressLocalizer"
+ "_bundleIdentifierFromSecTaskForAuditToken:"
+ "_isGreenTeaDeviceStorage"
+ "_unitTestableLocalizedStringForPostalAddressString:returningNilIfNotFound:"
+ "_watchdog"
+ "defaultWatchdog"
+ "greenTeaDevice"
+ "hasContactProviderRestrictions"
+ "initForContactProvider"
+ "invalid Collection: less than 'count' elements in collection"
+ "makeLocalizer"
+ "recordExceptionForEvent:"
+ "setGreenTeaDevice:"
+ "setStatus:forEvent:"
+ "setWatchdog:"
+ "sharedLocalizer"
+ "statusForEvent:"
+ "suggestions-timeout"
+ "v32@0:8Q16@\"NSString\"24"
+ "watchdog"
- "\x0e"
- "Looked up bundle ID %@ from audit token using entitlement."
- "_bundleIdentifierFromEntitlementForAuditToken:"
- "hasContactsProviderRestrictions"
- "initForContactsProvider"

```
