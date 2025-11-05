## iMessage

> `/System/Library/Messages/PlugIns/iMessage.imservice/Contents/MacOS/iMessage`

```diff

-1402.400.131.1.3
-  __TEXT.__text: 0x9ec58
-  __TEXT.__auth_stubs: 0x1140
-  __TEXT.__objc_stubs: 0xae80
-  __TEXT.__objc_methlist: 0x2144
+1402.500.181.1.1
+  __TEXT.__text: 0x9edb8
+  __TEXT.__auth_stubs: 0x1100
+  __TEXT.__objc_stubs: 0xaf80
+  __TEXT.__objc_methlist: 0x26c4
   __TEXT.__const: 0x33e
-  __TEXT.__gcc_except_tab: 0xa594
-  __TEXT.__cstring: 0x2eed
-  __TEXT.__oslogstring: 0x13c86
+  __TEXT.__gcc_except_tab: 0xa840
+  __TEXT.__cstring: 0x2cad
+  __TEXT.__oslogstring: 0x13c88
   __TEXT.__objc_classname: 0x4e1
-  __TEXT.__objc_methname: 0x10011
+  __TEXT.__objc_methname: 0x1015b
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
-  __TEXT.__unwind_info: 0x1e40
-  __TEXT.__eh_frame: 0x2b8
-  __DATA_CONST.__auth_got: 0x8b0
-  __DATA_CONST.__got: 0xd50
+  __TEXT.__unwind_info: 0x1e38
+  __TEXT.__eh_frame: 0x2c0
+  __DATA_CONST.__auth_got: 0x890
+  __DATA_CONST.__got: 0xd60
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x2f88
-  __DATA_CONST.__cfstring: 0x30c0
+  __DATA_CONST.__const: 0x2f90
+  __DATA_CONST.__cfstring: 0x3180
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_arraydata: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_const: 0x3570
-  __DATA.__objc_selrefs: 0x3110
+  __DATA.__objc_const: 0x2b38
+  __DATA.__objc_selrefs: 0x3318
   __DATA.__objc_ivar: 0x1b0
-  __DATA.__objc_data: 0x880
+  __DATA.__objc_data: 0x888
   __DATA.__data: 0x798
   __DATA.__bss: 0xa8
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftFileProvider.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 0DC58D94-FC5F-315B-939F-CF09FE1BD791
-  Functions: 1314
-  Symbols:   730
-  CStrings:  4494
+  UUID: 5FEACD84-DCBC-328F-B069-2B4D5E8E6B2A
+  Functions: 1318
+  Symbols:   732
+  CStrings:  4502
 
Symbols:
+ _OBJC_CLASS_$_IDSMessageContext
+ _OBJC_CLASS_$_IDSServiceMetricContext
+ _OBJC_CLASS_$_IMDLocalDaemon
+ __swift_FORCE_LOAD_$_swiftDataDetection
- _IMDMessageHistorySyncNotifyCKChatSyncControllerWantsSync
- __swift_FORCE_LOAD_$_swiftFileProvider
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
