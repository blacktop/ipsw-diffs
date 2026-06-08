## IncomingCallFilter

> `/System/Library/PrivateFrameworks/IncomingCallFilter.framework/IncomingCallFilter`

```diff

-181.600.11.0.0
-  __TEXT.__text: 0x37e8
-  __TEXT.__auth_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x80
+194.100.2.0.0
+  __TEXT.__text: 0x4078
+  __TEXT.__objc_methlist: 0x8c
   __TEXT.__const: 0x60
-  __TEXT.__oslogstring: 0x9b9
-  __TEXT.__cstring: 0x36e
-  __TEXT.__gcc_except_tab: 0xe8
-  __TEXT.__unwind_info: 0x150
-  __TEXT.__objc_classname: 0xe
-  __TEXT.__objc_methname: 0x1cf
-  __TEXT.__objc_methtype: 0x71
-  __TEXT.__objc_stubs: 0x2a0
-  __DATA_CONST.__got: 0x80
+  __TEXT.__oslogstring: 0xd23
+  __TEXT.__cstring: 0x389
+  __TEXT.__gcc_except_tab: 0xf8
+  __TEXT.__unwind_info: 0x168
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x268
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb8
+  __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0x90
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0x220
   __AUTH_CONST.__objc_const: 0xf8
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xc
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0x98
+  __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CommunicationsFilter.framework/CommunicationsFilter
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FE707149-D93C-343B-92F3-C415EF3A4984
-  Functions: 76
-  Symbols:   315
-  CStrings:  158
+  UUID: 5369CB50-42AF-39D4-A530-25C34A8B75E3
+  Functions: 78
+  Symbols:   341
+  CStrings:  139
 
Symbols:
+ -[ICFCallServer _requestCallGrantForIdentifiers:forProviderIdentifier:waitForResponse:completionBlock:]
+ -[ICFCallServer shouldAllowIncomingCallForHandles:forProviderIdentifier:response:]
+ GCC_except_table0
+ GCC_except_table12
+ GCC_except_table18
+ _CFArrayGetCount
+ _CFArrayGetValueAtIndex
+ _CFGetTypeID
+ _CFStringGetTypeID
+ _CMFBlockListGetBlockedStatusForItems
+ _CreateCMFItemFromString
+ _ICFCallProviderShouldAllowIncomingGroupCallWithQueue
+ _ICFCallProviderShouldAllowIncomingGroupCallWithQueue.cold.1
+ _ICFCallProviderShouldAllowIncomingGroupCallWithQueue.cold.2
+ _ICFSendRequestMessageWithResponse
+ _ICFSendRequestMessageWithResponse.cold.1
+ _ICFSendRequestMessageWithResponse.connectionRequestQueue
+ _ICFSendRequestMessageWithResponse.onceToken
+ _IMGetXPCArrayFromDictionary
+ _IMInsertArraysToXPCDictionary
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSString
+ __CFArrayContainsOnlyCFStrings
+ ___103-[ICFCallServer _requestCallGrantForIdentifiers:forProviderIdentifier:waitForResponse:completionBlock:]_block_invoke
+ ___103-[ICFCallServer _requestCallGrantForIdentifiers:forProviderIdentifier:waitForResponse:completionBlock:]_block_invoke.38
+ ___103-[ICFCallServer _requestCallGrantForIdentifiers:forProviderIdentifier:waitForResponse:completionBlock:]_block_invoke.38.cold.1
+ ___103-[ICFCallServer _requestCallGrantForIdentifiers:forProviderIdentifier:waitForResponse:completionBlock:]_block_invoke.40
+ ___21-[ICFCallServer init]_block_invoke.23
+ ___33-[ICFCallServer _clientConnected]_block_invoke.45
+ ___82-[ICFCallServer shouldAllowIncomingCallForHandles:forProviderIdentifier:response:]_block_invoke
+ ___ICFSendRequestMessageWithResponse_block_invoke
+ ___ICFSendRequestMessageWithResponse_block_invoke.3
+ ___ICFSendRequestMessageWithResponse_block_invoke.6
+ ___ICFSendRequestMessageWithResponse_block_invoke.6.cold.1
+ ___ICFXPCServer_peer_event_handler.cold.4
+ _____ICFXPCServer_peer_event_handler_block_invoke.11
+ ___block_descriptor_112_e8_32o40o48o56o64o72b80r88r96r104r_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8s40l8r80l8s48l8s72l8r88l8r96l8s56l8s64l8r104l8
+ ___block_descriptor_88_e8_32o40o48o56b64r72r80r_e5_v8?0ls32l8r64l8r72l8s56l8r80l8s40l8s48l8
+ ___block_literal_global.14
+ ___block_literal_global.18
+ ___block_literal_global.42
+ ___block_literal_global.54
+ _objc_msgSend$_requestCallGrantForIdentifiers:forProviderIdentifier:waitForResponse:completionBlock:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$boolValue
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$shouldAllowIncomingCallForHandles:forProviderIdentifier:response:
+ _objc_opt_class
+ _objc_opt_isKindOfClass
+ _objc_release_x26
+ _objc_release_x27
- -[ICFCallServer _requestCallGrantForIdentifier:forProviderIdentifier:waitForResponse:completionBlock:]
- GCC_except_table1
- GCC_except_table11
- GCC_except_table17
- _CMFBlockListIsItemBlocked
- _CMFItemCreateWithEmailAddress
- _CMFItemCreateWithPhoneNumber
- _ICFCallProviderShouldAllowIncomingCallWithQueue.cold.2
- _ICFCallProviderShouldAllowIncomingCallWithQueue.connectionRequestQueue
- _ICFCallProviderShouldAllowIncomingCallWithQueue.onceToken
- _IMPhoneNumberRefCopyForPhoneNumber
- _OUTLINED_FUNCTION_4
- ___102-[ICFCallServer _requestCallGrantForIdentifier:forProviderIdentifier:waitForResponse:completionBlock:]_block_invoke
- ___102-[ICFCallServer _requestCallGrantForIdentifier:forProviderIdentifier:waitForResponse:completionBlock:]_block_invoke.33
- ___102-[ICFCallServer _requestCallGrantForIdentifier:forProviderIdentifier:waitForResponse:completionBlock:]_block_invoke.33.cold.1
- ___102-[ICFCallServer _requestCallGrantForIdentifier:forProviderIdentifier:waitForResponse:completionBlock:]_block_invoke.35
- ___21-[ICFCallServer init]_block_invoke.18
- ___33-[ICFCallServer _clientConnected]_block_invoke_3
- ___ICFCallProviderShouldAllowIncomingCallWithQueue_block_invoke
- ___ICFCallProviderShouldAllowIncomingCallWithQueue_block_invoke.3
- ___ICFCallProviderShouldAllowIncomingCallWithQueue_block_invoke.9
- ___ICFCallProviderShouldAllowIncomingCallWithQueue_block_invoke.9.cold.1
- ___block_descriptor_64_e8_32o40b48r56r_e5_v8?0lr48l8s40l8r56l8s32l8
- ___block_descriptor_80_e8_32o40o48o56r64r72r_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8r56l8r64l8s40l8s48l8r72l8
- ___block_literal_global.13
- ___block_literal_global.37
- ___block_literal_global.48
- ___block_literal_global.9
- _objc_msgSend$_requestCallGrantForIdentifier:forProviderIdentifier:waitForResponse:completionBlock:
- _objc_release_x23
- _objc_release_x24
CStrings:
+ "Early returning due to client requesting call to be blocked - identifier is not allowed %@"
+ "Filter item %@ is blocked in identifiers: %@. Returning YES"
+ "Group completed but we already early ejected, dropping the result"
+ "Invalid handles passed in %@. Allowing request"
+ "Invalid handles passed in: %@, allowing call"
+ "Invalid or empty identifiers, returning NO"
+ "No items blocked in identifiers: %@. Returning NO"
+ "Received group-call-request from (%d)"
+ "Received invalid dictionary from CMF for identifiers %@, returning NO"
+ "Requesting call grant for identifiers %@ providerIdentifier %@ waitForResponse %@ completionBlock %@"
+ "Synchronous query done but we already early ejected, dropping the result"
+ "Unable to create CMFItem from identifier %@, returning NO"
+ "Unable to parse identifiers %@ to CMFItemRefs, returning NO"
+ "[WARN] CT provided a nil number, allowing call"
+ "[WARN] shouldAllowIncomingCallForNumber received nil number for providerIdentifier %@, allowing call through"
+ "group-call-request"
+ "handles"
+ "handles %@, providerIdentifier %@"
+ "number %@, providerIdentifier %@"
- "%@ returning %@"
- "@\"NSMutableArray\""
- "@\"NSObject<OS_xpc_object>\""
- "@16@0:8"
- "B"
- "Requesting call grant for identifier %@ providerIdentifier %@ waitForResponse %@ completionBlock %@"
- "_cleanup"
- "_cleanupClient:"
- "_clientConnected"
- "_clients"
- "_configureWithClient:"
- "_connection"
- "_hasRegistered"
- "_requestCallGrantForIdentifier:forProviderIdentifier:waitForResponse:completionBlock:"
- "addObject:"
- "allKeys"
- "allValues"
- "containsObject:"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "init"
- "length"
- "lock"
- "number %@,   providerIdentifier %@"
- "objectForKey:"
- "removeObject:"
- "removeObjectForKey:"
- "setObject:forKey:"
- "sharedInstance"
- "shouldAllowIncomingCallForNumber:forProviderIdentifier:response:"
- "unlock"
- "v16@0:8"
- "v24@0:8@16"
- "v40@0:8@16@24@?32"
- "v44@0:8@16@24B32@?36"

```
