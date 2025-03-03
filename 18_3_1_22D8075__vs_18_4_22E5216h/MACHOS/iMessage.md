## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/iMessage`

```diff

-1402.400.131.2.6
-  __TEXT.__text: 0x91d68
-  __TEXT.__auth_stubs: 0x1380
-  __TEXT.__objc_stubs: 0xb180
-  __TEXT.__objc_methlist: 0x2164
+1402.500.164.2.1
+  __TEXT.__text: 0x91e04
+  __TEXT.__auth_stubs: 0x1330
+  __TEXT.__objc_stubs: 0xb280
+  __TEXT.__objc_methlist: 0x26ec
   __TEXT.__const: 0x37e
-  __TEXT.__gcc_except_tab: 0xa674
-  __TEXT.__cstring: 0x2fad
-  __TEXT.__oslogstring: 0x13ee6
+  __TEXT.__gcc_except_tab: 0xa948
+  __TEXT.__cstring: 0x2d7d
+  __TEXT.__oslogstring: 0x13ed8
   __TEXT.__objc_classname: 0x4e2
-  __TEXT.__objc_methname: 0x102d4
+  __TEXT.__objc_methname: 0x1041e
   __TEXT.__objc_methtype: 0x2779
   __TEXT.__ustring: 0x4
-  __TEXT.__constg_swiftt: 0x168
+  __TEXT.__constg_swiftt: 0x178
   __TEXT.__swift5_typeref: 0x261
   __TEXT.__swift5_reflstr: 0x1f
   __TEXT.__swift5_fieldmd: 0x48
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift5_capture: 0xa0
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1d90
-  __TEXT.__eh_frame: 0x2b8
-  __DATA_CONST.__auth_got: 0x9d0
-  __DATA_CONST.__got: 0xda0
+  __TEXT.__unwind_info: 0x1d98
+  __TEXT.__eh_frame: 0x2c0
+  __DATA_CONST.__auth_got: 0x9a8
+  __DATA_CONST.__got: 0xdb0
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2ad0
-  __DATA_CONST.__cfstring: 0x3220
+  __DATA_CONST.__const: 0x2ac8
+  __DATA_CONST.__cfstring: 0x32e0
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3570
-  __DATA.__objc_selrefs: 0x31c8
+  __DATA.__objc_const: 0x2b38
+  __DATA.__objc_selrefs: 0x33d0
   __DATA.__objc_ivar: 0x1b0
-  __DATA.__objc_data: 0x380
+  __DATA.__objc_data: 0x388
   __DATA.__data: 0x790
   __DATA.__bss: 0x60
   __DATA_DIRTY.__objc_data: 0x500

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
-  Functions: 1175
+  Functions: 1179
   Symbols:   778
-  CStrings:  4159
+  CStrings:  4161
 
Symbols:
+ _OBJC_CLASS_$_IDSMessageContext
+ _OBJC_CLASS_$_IDSServiceMetricContext
+ _OBJC_CLASS_$_IMDLocalDaemon
- _IMDMessageHistorySyncNotifyCKChatSyncControllerWantsSync
- __swift_FORCE_LOAD_$_swiftFileProvider
- _objc_retain_x9
CStrings:
+ "/"
+ "ChatBot Logo - Update brand logo %@ to chatID %@ identifier %@"
+ "RCSChatBot_Brand"
+ "__im_dateWithCurrentServerTime"
+ "_automation_receiveDictionary:options:fromHandle:"
+ "areDualSIMDevicesExceptionsDisabled"
+ "attachment"
+ "iMessage"
+ "iMessageIDSHandler"
+ "initWithDictionary:boostContext:"
+ "initWithSenderInfo:time:timeRead:timeDelivered:timePlayed:subject:body:bodyData:attributes:fileTransferGUIDs:flags:guid:messageID:account:accountID:service:handle:roomName:unformattedID:countryCode:expireState:balloonBundleID:payloadData:expressiveSendStyleID:timeExpressiveSendPlayed:errorType:associatedMessageGUID:associatedMessageType:associatedMessageRange:bizIntent:locale:biaReferenceID:messageSummaryInfo:partCount:threadIdentifier:dateRecovered:"
+ "initWithTimestamp:identifier:"
+ "message-context"
+ "noteMetricOfType:context:"
+ "sendBrandLogoUpdate early return -- no chat identifier"
+ "sendBrandLogoUpdate:toChatID:identifier:style:account:"
+ "setRunningInAutomation:"
+ "sharedDaemon"
+ "text"
+ "trackSentMessageEventOfType:subtype:sendDuration:wasSuccessful:handle:error:"
+ "typingIndicator"
- "Chat: Could not update balloon payload for missing message GUID: %@"
- "Chat: Could not update balloon payload for missing payload: %@"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "initWithSenderInfo:time:timeRead:timeDelivered:timePlayed:subject:body:bodyData:attributes:fileTransferGUIDs:flags:guid:messageID:account:accountID:service:handle:roomName:unformattedID:countryCode:expireState:balloonBundleID:payloadData:expressiveSendStyleID:timeExpressiveSendPlayed:errorType:associatedMessageGUID:associatedMessageType:associatedMessageRange:bizIntent:locale:biaReferenceID:messageSummaryInfo:partCount:threadIdentifier:"
- "invalid Collection: less than 'count' elements in collection"
- "postNotificationName:object:"
- "updateBalloonPayload:attachments:forMessageGUID:"

```
