## asktod

> `/usr/libexec/asktod`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0x2fb70
-  __TEXT.__auth_stubs: 0x1380
-  __TEXT.__objc_methlist: 0xb8
-  __TEXT.__const: 0x1250
-  __TEXT.__cstring: 0x1a3c
-  __TEXT.__objc_methname: 0xe1d
-  __TEXT.__oslogstring: 0x22b7
+37.1.0.0.0
+  __TEXT.__text: 0x33f94
+  __TEXT.__auth_stubs: 0x1370
+  __TEXT.__objc_methlist: 0xc0
+  __TEXT.__const: 0x1330
+  __TEXT.__cstring: 0x1c9c
+  __TEXT.__objc_methname: 0xe56
+  __TEXT.__oslogstring: 0x26b7
   __TEXT.__swift5_entry: 0x8
+  __TEXT.__constg_swiftt: 0xb9c
+  __TEXT.__swift5_typeref: 0xdd1
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_types: 0x98
   __TEXT.__objc_classname: 0x77
   __TEXT.__objc_methtype: 0x936
-  __TEXT.__constg_swiftt: 0xb38
-  __TEXT.__swift5_typeref: 0xcff
-  __TEXT.__swift5_reflstr: 0xa9d
-  __TEXT.__swift5_fieldmd: 0x918
-  __TEXT.__swift5_capture: 0x2c0
-  __TEXT.__swift5_proto: 0xec
-  __TEXT.__swift5_types: 0x90
+  __TEXT.__swift5_reflstr: 0xb0d
+  __TEXT.__swift5_fieldmd: 0x980
+  __TEXT.__swift5_capture: 0x2f4
+  __TEXT.__swift5_proto: 0xf4
   __TEXT.__swift5_assocty: 0x108
-  __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_mpenum: 0x20
+  __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x48
   __TEXT.__info_plist: 0x4c4
-  __TEXT.__unwind_info: 0xa50
-  __TEXT.__eh_frame: 0x1548
-  __DATA_CONST.__auth_got: 0x9c0
+  __TEXT.__unwind_info: 0xb08
+  __TEXT.__eh_frame: 0x1780
+  __DATA_CONST.__auth_got: 0x9b8
   __DATA_CONST.__got: 0x298
-  __DATA_CONST.__auth_ptr: 0x328
-  __DATA_CONST.__const: 0x17a8
+  __DATA_CONST.__auth_ptr: 0x350
+  __DATA_CONST.__const: 0x18a8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
-  __DATA.__objc_const: 0x1740
+  __DATA.__objc_const: 0x1748
   __DATA.__objc_selrefs: 0x248
-  __DATA.__objc_data: 0x308
-  __DATA.__data: 0x1378
-  __DATA.__bss: 0x1610
-  __DATA.__common: 0xf0
+  __DATA.__objc_data: 0x320
+  __DATA.__data: 0x13b8
+  __DATA.__bss: 0x1710
+  __DATA.__common: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/IMCore.framework/IMCore
+  - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
   - /System/Library/PrivateFrameworks/People.framework/People
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 800
-  Symbols:   478
-  CStrings:  528
+  Functions: 838
+  Symbols:   479
+  CStrings:  553
 
Symbols:
+ _$s10Foundation12URLQueryItemV4nameSSvg
+ _$s10Foundation12URLQueryItemV5valueSSSgvg
+ _$s5AskTo14ATAnswerChoiceCMn
+ _$sBi64_WV
+ _$sSo13os_log_type_ta0A0E5debugABvgZ
+ _IMBalloonBundleIdentifierLegacyScreenTime
+ _IMBalloonExtensionIDWithSuffix
+ _IMSPIBatchFetchMessageGUIDsWithBalloonBundleID
+ _swift_getForeignTypeMetadata
- _$s8Dispatch0A3QoSV0B6SClassO8rawValueSo11qos_class_tavg
- _$s8Dispatch0A3QoSV0B6SClassOMa
- _$s8Dispatch0A3QoSV7defaultACvgZ
- _$s8Dispatch0A3QoSV8qosClassAC0B6SClassOvg
- _$sSo17OS_dispatch_queueC8DispatchE4mainABvgZ
- _$ss15ContiguousArrayV15reserveCapacityyySiFyXl_Ts5
- _IMSPIQueryMessageWithGUIDAndLoadAttachmentsWithQOS
- _OBJC_CLASS_$_IMSPIMessage
CStrings:
+ "%!s(MISSING) Unable to derive STAskForTimeAnswer from AskTo answer choice: %!@(MISSING)"
+ "%!s(MISSING) called"
+ "%!s(MISSING) called with requestID %!s(MISSING), responderDSID: %!s(MISSING), answer: %!@(MISSING)"
+ "B24@?0@\"NSString\"8@\"NSURL\"16"
+ "Calling into ScreenTimeAnswerHandler with requestID %!s(MISSING), responderDSID: %!s(MISSING), answer: %!@(MISSING)"
+ "Calling into ScreenTimeAnswerHandler with requestID %!s(MISSING), responderDSID: %!s(MISSING), answer: %!l(MISSING)d"
+ "Could not parse ATPayload from messagesPayloadURL %!s(MISSING). error: %!@(MISSING)"
+ "Did not find a message for request ID "
+ "Found %!l(MISSING)d Messages messages matching request ID %!s(MISSING)"
+ "Found a match! Request with ID %!s(MISSING) has message GUID %!s(MISSING). Payload URL: %!s(MISSING)"
+ "Got back nil message GUID from IMSPI"
+ "Inspecting ScreenTime request message with GUID %!s(MISSING) in Messages DB to see if it matches with request ID %!s(MISSING)"
+ "Looking for Messages messages with request ID %!s(MISSING)"
+ "Matching messages for request ID %!s(MISSING) have message GUIDs %!s(MISSING)"
+ "Message with GUID %!s(MISSING) has request ID %!s(MISSING), is not for request with ID %!s(MISSING)"
+ "Messages returned a nil balloon bundle identifier for IMBalloonBundleIdentifierLegacyScreenTime."
+ "No ScreenTime request message in the Messages DB matched request ID %!s(MISSING)"
+ "Payload URL for message with GUID %!s(MISSING) was nil. Skipping."
+ "Resuming continuation for query with request ID %!s(MISSING)"
+ "ScreenTime SPI call provided an unknown Screen Time request answer "
+ "ScreenTime answer ID was %!s(MISSING)"
+ "ScreenTime request messages extension bundle identifier was nil"
+ "ScreenTimeAnswerHandler"
+ "The Biome event had an invalid Screen Time request status "
+ "The Biome event had an unknown Screen Time request answer "
+ "The Biome event was missing the responder DSID."
+ "The request already has an answer in the Messages database."
+ "URL components for message with GUID %!s(MISSING) was nil. Skipping."
+ "URL had no request ID for message with GUID %!s(MISSING). Skipping."
+ "Updating message with GUID %!s(MISSING) in Messages with response: %!@(MISSING)"
+ "findAllMessagesInMessagesDatabase(matching:)"
+ "init(requestID:responderDSID:answer:)"
+ "screenTimeDidReceiveAnswer(_:forRequestWithID:responderDSID:)"
+ "screenTimeDidReceiveAnswer:forRequestWithID:responderDSID:completionHandler:"
+ "v48@0:8@\"_TtC5AskTo14ATAnswerChoice\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
- "%!s(MISSING): Message for GUID %!s(MISSING) had no payload URL. message: %!@(MISSING)"
- "Biome event had an invalid Screen Time request status "
- "Biome event had an unknown Screen Time request answer "
- "Could not find message for GUID %!s(MISSING) for %!s(MISSING)"
- "Could not parse ATPayload from messagesPayloadURL %!s(MISSING) for %!s(MISSING). error: %!@(MISSING)"
- "Did not find a message for GUID "
- "Looking for Messages messages with GUID %!s(MISSING) for %!s(MISSING)"
- "ScreenTime answer ID for %!s(MISSING) biome event was %!s(MISSING)"
- "The event was missing the responder DSID."
- "Updating message with GUID %!s(MISSING) in Messages with response derived from biome event: %!@(MISSING)"
- "extensionPayloadURL"

```
