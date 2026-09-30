## StatusKitAgentCore

> `/System/Library/PrivateFrameworks/StatusKitAgentCore.framework/StatusKitAgentCore`

```diff

-80.500.111.0.0
-  __TEXT.__text: 0xb5d6c
+80.500.161.0.0
+  __TEXT.__text: 0xbb4e0
   __TEXT.__auth_stubs: 0x17f0
-  __TEXT.__objc_methlist: 0x7320
+  __TEXT.__objc_methlist: 0x7388
   __TEXT.__const: 0x784
-  __TEXT.__cstring: 0x2d9a
-  __TEXT.__oslogstring: 0x1067d
-  __TEXT.__gcc_except_tab: 0xdec
+  __TEXT.__cstring: 0x2dba
+  __TEXT.__oslogstring: 0x109ad
+  __TEXT.__gcc_except_tab: 0xe24
   __TEXT.__swift5_typeref: 0x9d0
   __TEXT.__swift5_capture: 0x488
   __TEXT.__constg_swiftt: 0x160

   __TEXT.__swift_as_entry: 0x70
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x20d0
-  __TEXT.__eh_frame: 0x1218
-  __TEXT.__objc_classname: 0xe22
-  __TEXT.__objc_methname: 0xfd07
-  __TEXT.__objc_methtype: 0x4440
-  __TEXT.__objc_stubs: 0x8e60
-  __DATA_CONST.__got: 0x778
-  __DATA_CONST.__const: 0x1a38
+  __TEXT.__unwind_info: 0x2108
+  __TEXT.__eh_frame: 0x12d8
+  __TEXT.__objc_classname: 0xe24
+  __TEXT.__objc_methname: 0xff3a
+  __TEXT.__objc_methtype: 0x44af
+  __TEXT.__objc_stubs: 0x9000
+  __DATA_CONST.__got: 0x780
+  __DATA_CONST.__const: 0x1b00
   __DATA_CONST.__objc_classlist: 0x2c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3058
+  __DATA_CONST.__objc_selrefs: 0x30c0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x240
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0xc08
   __AUTH_CONST.__auth_ptr: 0x1c8
   __AUTH_CONST.__const: 0x1540
-  __AUTH_CONST.__cfstring: 0x23c0
-  __AUTH_CONST.__objc_const: 0xde08
+  __AUTH_CONST.__cfstring: 0x2420
+  __AUTH_CONST.__objc_const: 0xde58
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x8b8
-  __DATA.__objc_ivar: 0x5e0
+  __DATA.__objc_ivar: 0x5e4
   __DATA.__data: 0x1220
   __DATA.__bss: 0x3d0
   __DATA_DIRTY.__objc_data: 0x1440

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 3468
-  Symbols:   3658
-  CStrings:  4042
+  Functions: 3489
+  Symbols:   3679
+  CStrings:  4076
 
Symbols:
+ _OBJC_CLASS_$_IDSFirewall
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initWithTake
- _swift_generic_initializeBufferWithCopyOfBuffer
- _swift_initStructMetadataWithLayoutString
CStrings:
+ "\x15"
+ "Could not retreive IDS firewall for %@"
+ "Error querying IDS for destination info: %@"
+ "Invitation message did not contain a presence identifier with a valid client ID, dropping: %@"
+ "Invitation message missing date channel created. Will use current server time"
+ "Invitation was rejected for sender insecurity, dropping: %@"
+ "No URI destinations to query"
+ "Presence channel has never been seen before, accepting"
+ "Querying IDS for URI destinations: %@ looking for sender merge ID: %@"
+ "Querying if sender %@ is in list of valid sender handles: %@"
+ "Received incoming message: %@ fromID: %@ (%@)"
+ "Retreived IDS firewall entries for %@: %@"
+ "Retreiving IDS firewall for %@ returned error: %@"
+ "Sender %@ was in list of valid sender handles, accepting"
+ "Sender %@ was not in list of valid sender handles"
+ "Sender %@ was not in list of valid sender handles, checking firewall for %@"
+ "Sender %@ was not in the firewall for %@"
+ "T@\"IDSURI\",R,N"
+ "URI destinations: %@ map to valid merge IDs: %@"
+ "_acceptInvitationMessage:fromHandle:toHandle:messageGuid:existingChannel:databaseContext:"
+ "_shouldAcceptInvitationMessageForPresenceIdentifier:fromHandle:fromMergeID:inServiceFirewall:databaseContext:completion:"
+ "addListenerID:forService:"
+ "com.apple.private.alloy.home"
+ "currentEntries:"
+ "destinationURIs"
+ "endpoints"
+ "handleIncomingInvitationMessage:fromHandle:fromID:fromMergeID:toHandle:messageGuid:"
+ "homed"
+ "idInfoForDestinations:service:infoTypes:options:listenerID:queue:completionBlock:"
+ "idsURI"
+ "initWithService:queue:"
+ "isHandle:inFirewallForService:completion:"
+ "listOfValidSenderHandles:containsSenderMergeID:completion:"
+ "senderCorrelationIdentifier"
+ "service:didReceiveIncomingMessage:fromID:fromMergeID:toID:messageGuid:"
+ "uri"
+ "v40@0:8@\"NSSet\"16@\"NSString\"24@?<v@?B>32"
+ "v40@0:8@\"SKHandle\"16@\"NSString\"24@?<v@?B>32"
+ "v64@0:8@\"NSDictionary\"16@\"SKHandle\"24@\"NSString\"32@\"NSString\"40@\"SKHandle\"48@\"NSString\"56"
+ "v64@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56"
- "Invitation message missing date channel created. Using current server time"
- "Received incoming message: %@ fromID: %@"
- "handleIncomingInvitationMessage:fromHandle:fromID:toHandle:messageGuid:"
- "service:didReceiveIncomingMessage:fromID:toID:messageGuid:"
- "v56@0:8@\"NSDictionary\"16@\"SKHandle\"24@\"NSString\"32@\"SKHandle\"40@\"NSString\"48"
- "v56@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@\"NSString\"40@\"NSString\"48"

```
