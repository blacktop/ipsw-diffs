## AskToMessagesExtension

> `/Applications/AskToMessagesHost.app/PlugIns/AskToMessagesExtension.appex/AskToMessagesExtension`

```diff

-40.0.0.0.0
-  __TEXT.__text: 0x1b26c
-  __TEXT.__auth_stubs: 0x1310
+41.0.0.0.0
+  __TEXT.__text: 0x1c8c4
+  __TEXT.__auth_stubs: 0x1480
   __TEXT.__objc_methlist: 0x94
-  __TEXT.__const: 0xbe4
-  __TEXT.__objc_methname: 0x598
-  __TEXT.__cstring: 0xaa6
-  __TEXT.__constg_swiftt: 0x558
-  __TEXT.__swift5_typeref: 0x17a2
-  __TEXT.__swift5_reflstr: 0x2d4
-  __TEXT.__swift5_fieldmd: 0x348
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_types: 0x4c
+  __TEXT.__const: 0xbf4
+  __TEXT.__objc_methname: 0x59d
+  __TEXT.__cstring: 0xb36
+  __TEXT.__constg_swiftt: 0x504
+  __TEXT.__swift5_typeref: 0x1766
+  __TEXT.__swift5_reflstr: 0x334
+  __TEXT.__swift5_fieldmd: 0x368
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_types: 0x48
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x48
   __TEXT.__swift5_capture: 0x90
-  __TEXT.__oslogstring: 0x90e
-  __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x4e8
+  __TEXT.__oslogstring: 0xc3e
+  __TEXT.__unwind_info: 0x4e0
   __TEXT.__eh_frame: 0x2d8
-  __DATA_CONST.__auth_got: 0x988
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__auth_ptr: 0x3c0
-  __DATA_CONST.__const: 0x820
+  __DATA_CONST.__auth_got: 0xa40
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__auth_ptr: 0x3e8
+  __DATA_CONST.__const: 0x790
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x3e0
-  __DATA.__objc_selrefs: 0x210
-  __DATA.__objc_data: 0x1b8
-  __DATA.__data: 0x9e0
-  __DATA.__common: 0x78
+  __DATA.__objc_const: 0x400
+  __DATA.__objc_selrefs: 0x218
+  __DATA.__objc_data: 0x180
+  __DATA.__data: 0xa00
+  __DATA.__common: 0x80
   __DATA.__bss: 0x840
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/PrivateFrameworks/AskToCore.framework/AskToCore
   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
+  - /System/Library/PrivateFrameworks/People.framework/People
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 430
-  Symbols:   170
-  CStrings:  177
+  Functions: 418
+  Symbols:   169
+  CStrings:  197
 
Symbols:
+ _swift_getEnumCaseMultiPayload
+ _swift_initEnumMetadataMultiPayload
- _swift_getErrorValue
- _objc_retain_x28
- _swift_isClassType
CStrings:
+ "%!s(MISSING) nil message url"
+ "com.apple.screentime.moretime"
+ "Failed to parse ATPayload and there was no GUID on the MSMessage. %!@(MISSING)"
+ "MessageDetails.eventSource was unknown"
+ "Successfully parsed MessageDetails from MSMessage. messageGUID: %!s(MISSING)"
+ "Trying to derive ATPayload from MessageDetails with GUID %!s(MISSING)"
+ "%!s(MISSING) called with nil message.session"
+ "AskForTimeActionApproveHour"
+ "MessageDetails.requestID was empty"
+ "selectedPayload"
+ "Failed to parse an ATPayload or MessageDetails from the MSMessage. MSMessage: %!@(MISSING) url: %!s(MISSING)"
+ "No payload image in message URL"
+ "messageParser"
+ "ScreenTimeRequest"
+ "%!s(MISSING) called with conversation that had no selected message"
+ "Couldn't parse MessageDetails because the URLComponents derived from %!s(MISSING) were nil."
+ "iconFromMessageURL was nil. Trying to use icon for the ATPayload instead as a last resort. This means that a blank icon might end up being shown to the user."
+ "originalPayload"
+ "selectedMessageDidUpdate(in:)"
+ "%!s(MISSING) called with message %!@(MISSING)"
+ "AskForTimeActionDontApprove"
+ "renderContent(in:icon:context:)"
+ "MessageDetails threw an error: %!@(MISSING)"
+ "Got payload from MessageDetails: %!@(MISSING)"
+ "guid"
+ "%!s(MISSING) called with nil selectedPayload"
+ "MessageDetails.eventSource was unsupported \"%!s(MISSING)\""
+ "AskForTimeActionApproveDay"
+ "Failed to parse an ATPayload from the MSMessage. Trying to parse MessageDetails instead. MSMessage: %!@(MISSING)"
+ "%!s(MISSING) called"
+ "AskForTimeActionApprove15"
+ "icon(for:derivedAskToPayload:)"
- "%!s(MISSING): %!s(MISSING) called with message.session nil"
- "Error parsing AskTo payload from MSMessage: %!@(MISSING)"
- "%!s(MISSING): %!s(MISSING) called with message nil"
- "MessageParserUnknownError"
- "MSMessage updated to nil!"
- "MessageParserMissingURLError"
- "iconFromData was nil. Trying to use icon for the ATPayload instead as a last resort. This means that a blank icon might end up being shown to the user."
- "renderContent(for:in:)"
- "%!s(MISSING): %!s(MISSING) called with message %!@(MISSING), url: %!s(MISSING)"
- "MessageParserFailedJSONDecodeError"
- "MessageParserDescriptionError"

```
