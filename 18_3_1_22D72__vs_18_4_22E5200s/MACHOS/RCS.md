## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/RCS`

```diff

-1402.400.131.2.6
-  __TEXT.__text: 0xf2a94
-  __TEXT.__auth_stubs: 0x1ac0
+1402.500.128.2.2
+  __TEXT.__text: 0xd1ea4
+  __TEXT.__auth_stubs: 0x1a60
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__objc_methlist: 0x46c
-  __TEXT.__const: 0x4050
+  __TEXT.__objc_methlist: 0x83c
+  __TEXT.__const: 0x49b2
   __TEXT.__objc_classname: 0xd1
-  __TEXT.__objc_methname: 0x41d8
+  __TEXT.__objc_methname: 0x4400
   __TEXT.__objc_methtype: 0xd75
-  __TEXT.__cstring: 0x3205
-  __TEXT.__constg_swiftt: 0x1c0c
-  __TEXT.__swift5_typeref: 0x1c93
-  __TEXT.__swift5_builtin: 0x154
-  __TEXT.__swift5_reflstr: 0xf32
+  __TEXT.__cstring: 0x2e65
+  __TEXT.__constg_swiftt: 0x1c8c
+  __TEXT.__swift5_typeref: 0x1ce7
+  __TEXT.__swift5_builtin: 0x168
+  __TEXT.__swift5_reflstr: 0xf52
   __TEXT.__swift5_assocty: 0x2a8
-  __TEXT.__oslogstring: 0x4dba
+  __TEXT.__oslogstring: 0x50ba
+  __TEXT.__swift5_fieldmd: 0x14c0
   __TEXT.__swift5_proto: 0x334
-  __TEXT.__swift5_types: 0x18c
-  __TEXT.__swift5_capture: 0x920
+  __TEXT.__swift5_types: 0x190
+  __TEXT.__swift_as_entry: 0x230
+  __TEXT.__swift_as_ret: 0x288
+  __TEXT.__swift5_capture: 0x924
   __TEXT.__swift5_mpenum: 0xbc
-  __TEXT.__swift5_fieldmd: 0x148c
   __TEXT.__swift5_protos: 0x44
-  __TEXT.__unwind_info: 0x3308
-  __TEXT.__eh_frame: 0x81f8
-  __DATA_CONST.__auth_got: 0xd68
-  __DATA_CONST.__got: 0x700
+  __TEXT.__unwind_info: 0x2e70
+  __TEXT.__eh_frame: 0x8118
+  __DATA_CONST.__auth_got: 0xd38
+  __DATA_CONST.__got: 0x738
   __DATA_CONST.__auth_ptr: 0x5e0
-  __DATA_CONST.__const: 0x4c40
+  __DATA_CONST.__const: 0x4d10
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA.__objc_const: 0x2540
-  __DATA.__objc_selrefs: 0x11c8
-  __DATA.__objc_data: 0x410
-  __DATA.__data: 0x3798
+  __DATA.__objc_const: 0x1e50
+  __DATA.__objc_selrefs: 0x1380
+  __DATA.__objc_data: 0x438
+  __DATA.__data: 0x3878
   __DATA.__bss: 0x5380
   __DATA.__common: 0xb8
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3473
-  Symbols:   379
-  CStrings:  1351
+  Functions: 3135
+  Symbols:   386
+  CStrings:  1368
 
Symbols:
+ _IDSRegistrationPropertySupportsRBMChatBot
+ _OBJC_CLASS_$_IMBrandInfo
+ _OBJC_CLASS_$_IMMultiplexingServiceReachabilityResponseHandler
+ _OBJC_CLASS_$_IMServiceReachabilityResponseBlockHandler
+ _OBJC_CLASS_$_NSDate
+ _swift_allocateGenericValueMetadataWithLayoutString
+ _swift_enumFn_getEnumTag
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_generic_instantiateLayoutString
+ _swift_getExistentialTypeMetadata
+ _swift_getTupleTypeMetadata2
+ _swift_getTupleTypeMetadata3
+ _swift_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_initStructMetadataWithLayoutString
+ _swift_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_multiPayloadEnumGeneric_getEnumTag
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_release_x10
- _objc_release_x9
- _objc_retain_x1
- _objc_retain_x10
- _objc_retain_x9
- _swift_allocateGenericValueMetadata
- _swift_getTupleTypeLayout2
- _swift_initEnumMetadataMultiPayload
- _swift_initStructMetadata
- _swift_unknownObjectUnownedCopyAssign
- _swift_unknownObjectUnownedCopyInit
- _swift_unknownObjectUnownedTakeAssign
- _swift_unknownObjectUnownedTakeInit
CStrings:
+ " reason "
+ "Ignoring read disposition for message already read %s"
+ "Not sending read receipt in chat %s as it's an unknown chat"
+ "Persistent Menu - Cannot find any chat for %s"
+ "Persistent Menu - Failed to fetch chatbot info for %s with error %@"
+ "Persistent Menu - Fetch chatbot info for %s, with %s number: %s"
+ "Persistent Menu - Fetched from %{public}s destination: %s info: %s"
+ "Persistent Menu - Found no chat in need of persistent menu for %s "
+ "Persistent Menu - No render info found for chat: %s"
+ "Persistent Menu - Populate cached chatbot info for %s"
+ "Persistent Menu - Populate persistent menu for chat: %s"
+ "Persistent Menu - Trying to fetch but cannot find any chat for %s "
+ "Sending RCS send message metric with subtype %s, duration %f, error %u"
+ "Update brand info %s for chat %s, brand logo guid: %s, brand logo data: %ld"
+ "Update empty stamp menu for chat %s"
+ "Update persistent menu %s for chat %s"
+ "__im_dateWithCurrentServerTime"
+ "__im_isChatBotPatterned"
+ "allExistingChatsWithIdentifier:"
+ "brandInfoDictionary"
+ "brandLogoData"
+ "brandLogoGuid"
+ "clientSendTime"
+ "com.apple.Messages"
+ "handle"
+ "hasChatBotBrandInfo"
+ "hasChatBotPersistentMenu"
+ "initWithBlock:"
+ "initWithResponseHandlers:"
+ "isFiltered"
+ "isRelayChatBotEnabled"
+ "persistentMenuDictionary"
+ "rcs.advised-action"
+ "relayDictionaryRepresentation"
+ "relayEmptyStampProperty"
+ "requestBrandInfo"
+ "requestPersistentMenu"
+ "setBrandInfoDictionary:"
+ "setBrandLogoData:"
+ "setPersistentMenuDictionary:"
+ "setRcsAdvisedAction:"
+ "time"
+ "timeIntervalSinceDate:"
+ "trackSentMessageEventOfType:subtype:sendDuration:wasSuccessful:handle:error:"
+ "updateBrandLogo:transferGuid:"
+ "v24@?0@\"IMServiceReachabilityRequest\"8@\"IMServiceReachabilityResult\"16"
- "%{public}s destination: %s info: %s"
- "Division by zero"
- "Division results in an overflow"
- "Failed to fetch chatbot info for %s with error %@"
- "Fatal error"
- "Fetch chatbot info for %s, with %s number: %s"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Populate persistent menu for chat: %s"
- "Read cached chatbot info for %s"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "X-Apple-ExampleHeader"
- "finalResultForService:handleIDs:allAreReachable:checkedServer:error:"
- "invalid Collection: less than 'count' elements in collection"

```
