## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/RCS`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

-1491.200.101.2.5
-  __TEXT.__text: 0x106cc0
-  __TEXT.__auth_stubs: 0x1fd0
-  __TEXT.__objc_stubs: 0x59c0
-  __TEXT.__objc_methlist: 0x9c0
-  __TEXT.__const: 0x6448
+1491.300.43.0.0
+  __TEXT.__text: 0x107520
+  __TEXT.__auth_stubs: 0x1ff0
+  __TEXT.__objc_stubs: 0x59e0
+  __TEXT.__objc_methlist: 0x9a8
+  __TEXT.__const: 0x6440
   __TEXT.__objc_classname: 0x49f
-  __TEXT.__objc_methtype: 0x14ef
-  __TEXT.__swift5_typeref: 0x2243
-  __TEXT.__constg_swiftt: 0x2454
+  __TEXT.__objc_methtype: 0x149b
+  __TEXT.__swift5_typeref: 0x223d
+  __TEXT.__constg_swiftt: 0x248c
   __TEXT.__swift5_builtin: 0x1e0
-  __TEXT.__swift5_reflstr: 0x16c4
+  __TEXT.__swift5_reflstr: 0x171a
   __TEXT.__swift5_assocty: 0x310
-  __TEXT.__oslogstring: 0x6a98
-  __TEXT.__swift5_fieldmd: 0x1a50
-  __TEXT.__swift5_proto: 0x354
+  __TEXT.__oslogstring: 0x6cf8
+  __TEXT.__swift5_fieldmd: 0x1a8c
+  __TEXT.__swift5_proto: 0x358
   __TEXT.__swift5_types: 0x1e8
-  __TEXT.__swift_as_entry: 0x2c0
+  __TEXT.__swift_as_entry: 0x2c4
   __TEXT.__swift_as_ret: 0x340
-  __TEXT.__swift_as_cont: 0x9b4
-  __TEXT.__swift5_capture: 0xcc8
-  __TEXT.__cstring: 0x2913
+  __TEXT.__swift_as_cont: 0x8e4
+  __TEXT.__swift5_capture: 0xce0
+  __TEXT.__cstring: 0x29e3
   __TEXT.__swift5_mpenum: 0xd4
-  __TEXT.__objc_methname: 0x61d3
+  __TEXT.__objc_methname: 0x6263
   __TEXT.__swift5_protos: 0x54
-  __TEXT.__unwind_info: 0x4558
-  __TEXT.__eh_frame: 0xaa48
+  __TEXT.__unwind_info: 0x4448
+  __TEXT.__eh_frame: 0xa528
   __DATA_CONST.__const: 0x50e0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__auth_got: 0xff0
-  __DATA_CONST.__got: 0x9d0
-  __DATA_CONST.__auth_ptr: 0x1570
-  __DATA.__objc_const: 0x23b8
-  __DATA.__objc_selrefs: 0x1968
-  __DATA.__objc_data: 0x6a8
-  __DATA.__data: 0x3cc8
-  __DATA.__common: 0xe8
+  __DATA_CONST.__auth_got: 0x1000
+  __DATA_CONST.__got: 0x9e0
+  __DATA_CONST.__auth_ptr: 0x1598
+  __DATA.__objc_const: 0x23b0
+  __DATA.__objc_selrefs: 0x1970
+  __DATA.__objc_data: 0x6b8
+  __DATA.__data: 0x3d40
+  __DATA.__common: 0xf0
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3899
-  Symbols:   492
-  CStrings:  1695
+  Functions: 3857
+  Symbols:   491
+  CStrings:  1708
 
Symbols:
+ _IMSupportsRCSRelayTypingIndicators
- _IDSRegistrationPropertySupportsRBMChatBot
- _objc_release_x10
CStrings:
+ "@32@0:8@16@24"
+ "Discarding metric submissions for messageGUID %s since isDelivered is %{bool}d"
+ "Error while sending message %s: %s"
+ "Failed to build message %s with error %@"
+ "Not firing ABC, isDelivered:%{bool}d, fzError: %u)"
+ "Not relaying cancel typing indicator -- messageGUID: %s, chatGUID: %s, shouldRelay: %{bool}d, supportsRCSRelayTypingIndicators: %{bool}d."
+ "Not relaying typing indicator -- messageGUID: %s, chatGUID: %s, supportsRCSRelayTypingIndicators: %{bool}d."
+ "RCSIgnoreRelayTypingIndicatorsCapability"
+ "Relaying cancelled typing indicator for %s"
+ "Relaying typing indicator for %s"
+ "Required capabilities to relay received message: %s"
+ "badChatIdentifier"
+ "cleanupFailedBuildForParts:"
+ "didReceiveError:forMessageID:forceError:submitMetric:"
+ "failedToDecryptMessageHasInvalidEncryption"
+ "isRCSRelayTypingIndicatorsEnabled"
+ "recipientHandleNotFound"
+ "requiredRelayCapabilitiesForMessage:chat:"
+ "sendDuration"
+ "supports-rcs-relay-typing-indicators"
+ "v24@0:8@\"NSArray\"16"
+ "v24@0:8@?<v@?@\"IMMessageItem\"B@\"NSArray\">16"
+ "v28@?0@\"IMMessageItem\"8B16@\"NSArray\"20"
- "Error while sending message %s, %@"
- "cleanupFailedBuildWithError:forParts:"
- "didReceiveError:forMessageID:forceError:"
- "maxChatParticipantsForContext:"
- "q24@0:8@\"IMServiceReachabilityContext\"16"
- "q24@0:8@16"
- "v24@0:8@?<v@?@\"IMMessageItem\"B@\"NSArray\"I>16"
- "v28@0:8I16@\"NSArray\"20"
- "v28@0:8I16@20"
- "v32@?0@\"IMMessageItem\"8B16@\"NSArray\"20I28"
```
