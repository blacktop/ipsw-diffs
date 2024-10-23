## AutocompleteAppIntentsExtension

> `/System/Library/ExtensionKit/Extensions/AutocompleteAppIntentsExtension.appex/AutocompleteAppIntentsExtension`

```diff

-4.0.0.0.0
-  __TEXT.__text: 0x1a0
-  __TEXT.__auth_stubs: 0x60
-  __TEXT.__swift5_typeref: 0x46
-  __TEXT.__const: 0x92
-  __TEXT.__swift5_reflstr: 0xe
-  __TEXT.__swift5_assocty: 0x18
+22.0.0.0.0
+  __TEXT.__text: 0x1fc20
+  __TEXT.__auth_stubs: 0xc60
+  __TEXT.__cstring: 0xf5a
+  __TEXT.__swift5_typeref: 0xe40
+  __TEXT.__const: 0x2cd8
+  __TEXT.__swift5_reflstr: 0x5e1
+  __TEXT.__swift5_assocty: 0x510
+  __TEXT.__constg_swiftt: 0x2a4
+  __TEXT.__swift5_fieldmd: 0x390
+  __TEXT.__swift5_proto: 0x2b4
+  __TEXT.__swift5_types: 0x48
+  __TEXT.__objc_methname: 0x97
+  __TEXT.__oslogstring: 0x24a
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x28
-  __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x80
-  __DATA_CONST.__auth_got: 0x30
-  __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0xd8
+  __TEXT.__unwind_info: 0xb80
+  __TEXT.__eh_frame: 0x330
+  __DATA_CONST.__auth_got: 0x630
+  __DATA_CONST.__got: 0x2d8
+  __DATA_CONST.__auth_ptr: 0x530
+  __DATA_CONST.__const: 0xe80
+  __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__data: 0x10
-  __DATA.__bss: 0x100
+  __DATA.__objc_const: 0x90
+  __DATA.__objc_selrefs: 0x48
+  __DATA.__data: 0xab8
+  __DATA.__bss: 0x5680
+  __DATA.__common: 0x98
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/ContactsAutocomplete.framework/ContactsAutocomplete
+  - /System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 8
-  Symbols:   30
-  CStrings:  0
+  Functions: 949
+  Symbols:   99
+  CStrings:  115
 
Symbols:
+ _OBJC_CLASS_$_CNEnvironment
+ _OBJC_CLASS_$_CNTimeIntervalFormatter
+ _OBJC_CLASS_$_NSPersonNameComponentsFormatter
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ ___chkstk_darwin
+ __objc_empty_cache
+ __os_log_impl
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ _free
+ _malloc
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend
+ _objc_opt_self
+ _objc_release_x19
+ _objc_release_x20
+ _objc_release_x21
+ _objc_release_x22
+ _objc_release_x23
+ _objc_release_x24
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retainAutoreleasedReturnValue
+ _os_log_type_enabled
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_bridgeObjectRetain_n
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_initStructMetadata
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_release_n
+ _swift_retain
+ _swift_retain_n
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _usleep
CStrings:
+ "%!s(MISSING) sleeping %!l(MISSING)u secs before fetch"
+ ".applicationDefined("
+ "Application defined: "
+ "AutocompleteAppIntentsExtension/ComposeRecipientHandleAppEntity.swift"
+ "Availability Cache Policy"
+ "COMPOSE_RECIPIENT_ENTITY_HANDLE_NAME"
+ "COMPOSE_RECIPIENT_ENTITY_HANDLE_SERVICE_NAME"
+ "COMPOSE_RECIPIENT_ENTITY_HANDLE_VALUE_NAME"
+ "COMPOSE_RECIPIENT_ENTITY_PROPERTY_ALIASES_NAME"
+ "COMPOSE_RECIPIENT_ENTITY_PROPERTY_CONTACT_IDENTIFIER_NAME"
+ "Client: %!s(MISSING), privacy: .private)"
+ "Compose Recipient"
+ "Compose Recipient Contact Identifier"
+ "Control the caching behavior"
+ "Description for Complete Name Intent"
+ "Description for Fetch Handle Availability Intent"
+ "Division by zero"
+ "Division results in an overflow"
+ "Fatal error"
+ "Fetch Handle Availability"
+ "Handle Availability"
+ "Insufficient space allocated to copy string contents"
+ "Not enough bits to represent the passed value"
+ "Partially Resolved"
+ "Querying for identifiers %!s(MISSING)"
+ "RCS"
+ "Received %!l(MISSING)d availabilities (%!s(MISSING))"
+ "Received %!l(MISSING)d recipients (%!s(MISSING))"
+ "Recipient (%!s(MISSING)) --> Entity (%!l(MISSING)d)"
+ "Refresh and cache availability"
+ "Returning %!l(MISSING)d entities: %!{(MISSING)private}s"
+ "Services: %!s(MISSING)"
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/IntegerTypes.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafePointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "The aliases of the \"Compose Recipient\" entity"
+ "The aliases of the \"Contact Identifier\" entity"
+ "The client making the call"
+ "The description of the Complete Name intent parameter 'client'"
+ "The description of the Complete Name intent parameter 'names'"
+ "The description of the Fetch Handle Availability intent parameter 'cachePolicy'"
+ "The description of the Fetch Handle Availability intent parameter 'names'"
+ "The description of the Fetch Handle Availability intent parameter 'services'"
+ "The handle of the \"Compose Recipient\" entity"
+ "The handle of the \"Handle Availability\" entity"
+ "The label of the Complete Name intent parameter 'client'"
+ "The label of the Complete Name intent parameter 'names'"
+ "The label of the Fetch Handle Availability intent parameter 'cachePolicy'"
+ "The label of the Fetch Handle Availability intent parameter 'names'"
+ "The label of the Fetch Handle Availability intent parameter 'services'"
+ "The name of the \"Compose Recipient\" entity handle availability type."
+ "The name of the \"Compose Recipient\" entity handle service type."
+ "The name of the \"Compose Recipient\" entity handle type."
+ "The name of the \"Compose Recipient\" entity handle value type."
+ "The name of the \"Compose Recipient\" entity type."
+ "The name of the \"Contact Identifier\" entity type."
+ "The name of the \"Handle Availability\" entity type."
+ "The names to search for"
+ "The person of the \"Compose Recipient\" entity"
+ "The service of the \"Handle Availability\" entity"
+ "The services to check"
+ "The status of the \"Compose Recipient\" entity"
+ "The status of the \"Handle Availability\" entity"
+ "Title for Complete (verb) Name Intent"
+ "Title for Fetch Handle Availability Intent"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "Unhandled ComposeRecipient.Handle.Label: "
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutablePointer.initialize overlapping range"
+ "UnsafeMutablePointer.initialize with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "Use cached availability only"
+ "Using last known status"
+ "Using refreshed status"
+ "Value is application defined: %!s(MISSING)"
+ "Value is email address: %!s(MISSING)"
+ "Value is phone number: %!s(MISSING)"
+ "Value is unknown"
+ "Will perform CompleteNameIntent for %!{(MISSING)private}s"
+ "Will perform FetchHandleAvailabilityIntent for %!{(MISSING)private}s"
+ "_TtC31AutocompleteAppIntentsExtension30ComposeRecipientEntityProvider"
+ "adHocIdentifier: "
+ "available"
+ "calendar"
+ "com.apple.contacts.autocomplete"
+ "com.apple.contacts.autocomplete.intents"
+ "com.apple.contacts.intents"
+ "com.apple.private.contacts.intents-delay"
+ "contactIdentifier: "
+ "currentEnvironment"
+ "faceTime"
+ "faceTimeAudio"
+ "faceTimeVideo"
+ "fullyResolved"
+ "generic"
+ "iMessage"
+ "init"
+ "initWithSuiteName:"
+ "invalid Collection: less than 'count' elements in collection"
+ "messages"
+ "objectForKey:"
+ "partiallyResolved"
+ "sharedFormatter"
+ "stringForTimeInterval:"
+ "stringFromPersonNameComponents:"
+ "timeProvider"
+ "timestamp"
+ "unavailable"
+ "unknown"
+ "unresolved"

```
