## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1367.100.1.2.1
-  __TEXT.__text: 0x67be0
+1367.200.12.0.0
+  __TEXT.__text: 0x68598
   __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_methlist: 0x8fd4
+  __TEXT.__objc_methlist: 0x900c
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x626b
-  __TEXT.__oslogstring: 0x3694
+  __TEXT.__cstring: 0x6300
+  __TEXT.__oslogstring: 0x36eb
   __TEXT.__gcc_except_tab: 0x778
-  __TEXT.__unwind_info: 0x1cb0
+  __TEXT.__unwind_info: 0x1cc8
   __TEXT.__objc_classname: 0x1471
-  __TEXT.__objc_methname: 0x11a5d
+  __TEXT.__objc_methname: 0x11b1f
   __TEXT.__objc_methtype: 0x3de8
-  __TEXT.__objc_stubs: 0xaa20
+  __TEXT.__objc_stubs: 0xaa60
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0xd40
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33d0
+  __DATA_CONST.__objc_selrefs: 0x33e8
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x4b0
   __AUTH_CONST.__const: 0x580
   __AUTH_CONST.__cfstring: 0x42a0
-  __AUTH_CONST.__objc_const: 0xebd0
+  __AUTH_CONST.__objc_const: 0xebe0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH.__objc_data: 0x1c20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: C1E2B48D-A839-3D70-961C-7A4135E374CD
-  Functions: 3177
-  Symbols:   10388
-  CStrings:  4689
+  UUID: 5F00DD1E-80E0-3234-9217-FC1D05A5A5BE
+  Functions: 3187
+  Symbols:   10416
+  CStrings:  4695
 
Symbols:
+ -[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:]
+ -[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:].cold.1
+ -[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:].cold.2
+ -[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:].cold.3
+ -[CXCallSourceManager callSource:reportedNewIncomingProtectedIMAVCallWithUUID:update:completion:]
+ -[CXProvider reportNewIncomingProtectedIMAVCallWithUUID:update:completion:]
+ ___49-[CXCallSource reportCallWithUUID:updated:reply:]_block_invoke.24
+ ___49-[CXCallSource reportCallWithUUID:updated:reply:]_block_invoke.25
+ ___50-[CXCallSource actionCompleted:completionHandler:]_block_invoke.100
+ ___50-[CXCallSource actionCompleted:completionHandler:]_block_invoke.101
+ ___53-[CXCallSource requestTransaction:completionHandler:]_block_invoke.93
+ ___53-[CXCallSource requestTransaction:completionHandler:]_block_invoke.94
+ ___57-[CXCallSource reportAudioFinishedForCallWithUUID:reply:]_block_invoke.64
+ ___57-[CXCallSource reportAudioFinishedForCallWithUUID:reply:]_block_invoke.65
+ ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.30
+ ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.34
+ ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.35
+ ___62-[CXProvider reportNewIncomingCallWithUUID:update:completion:]_block_invoke.163
+ ___65-[CXCallSource reportOutgoingCallWithUUID:connectedAtDate:reply:]_block_invoke.58
+ ___65-[CXCallSource reportOutgoingCallWithUUID:connectedAtDate:reply:]_block_invoke.59
+ ___70-[CXCallSource reportOutgoingCallWithUUID:sentInvitationAtDate:reply:]_block_invoke.46
+ ___70-[CXCallSource reportOutgoingCallWithUUID:sentInvitationAtDate:reply:]_block_invoke.47
+ ___72-[CXCallSource reportCallWithUUID:changedMeterLevel:forDirection:reply:]_block_invoke.76
+ ___72-[CXCallSource reportCallWithUUID:changedMeterLevel:forDirection:reply:]_block_invoke.77
+ ___72-[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:]_block_invoke
+ ___72-[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:]_block_invoke.16
+ ___72-[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:]_block_invoke.17
+ ___73-[CXCallSource reportOutgoingCallWithUUID:startedConnectingAtDate:reply:]_block_invoke.52
+ ___73-[CXCallSource reportOutgoingCallWithUUID:startedConnectingAtDate:reply:]_block_invoke.53
+ ___75-[CXCallSource reportCallWithUUID:changedFrequencyData:forDirection:reply:]_block_invoke.70
+ ___75-[CXCallSource reportCallWithUUID:changedFrequencyData:forDirection:reply:]_block_invoke.71
+ ___75-[CXProvider reportNewIncomingProtectedIMAVCallWithUUID:update:completion:]_block_invoke
+ ___75-[CXProvider reportNewIncomingProtectedIMAVCallWithUUID:update:completion:]_block_invoke.165
+ ___75-[CXProvider reportNewIncomingProtectedIMAVCallWithUUID:update:completion:]_block_invoke_2
+ ___82-[CXCallSource reportCallWithUUID:endedAtDate:privateReason:failureContext:reply:]_block_invoke.40
+ ___82-[CXCallSource reportCallWithUUID:endedAtDate:privateReason:failureContext:reply:]_block_invoke.41
+ ___86-[CXCallSource reportCallWithUUID:crossDeviceIdentifier:changedBytesOfDataUsed:reply:]_block_invoke.83
+ ___86-[CXCallSource reportCallWithUUID:crossDeviceIdentifier:changedBytesOfDataUsed:reply:]_block_invoke.84
+ ___97-[CXCallSourceManager callSource:reportedNewIncomingProtectedIMAVCallWithUUID:update:completion:]_block_invoke
+ ___block_literal_global.20
+ ___block_literal_global.27
+ ___block_literal_global.37
+ ___block_literal_global.43
+ ___block_literal_global.49
+ ___block_literal_global.55
+ ___block_literal_global.61
+ ___block_literal_global.67
+ ___block_literal_global.73
+ ___block_literal_global.79
+ _objc_msgSend$callSource:reportedNewIncomingProtectedIMAVCallWithUUID:update:completion:
+ _objc_msgSend$reportNewIncomingProtectedIMAVCallWithUUID:update:reply:
- ___49-[CXCallSource reportCallWithUUID:updated:reply:]_block_invoke.21
- ___49-[CXCallSource reportCallWithUUID:updated:reply:]_block_invoke.22
- ___50-[CXCallSource actionCompleted:completionHandler:]_block_invoke.98
- ___50-[CXCallSource actionCompleted:completionHandler:]_block_invoke.99
- ___53-[CXCallSource requestTransaction:completionHandler:]_block_invoke.91
- ___53-[CXCallSource requestTransaction:completionHandler:]_block_invoke.92
- ___57-[CXCallSource reportAudioFinishedForCallWithUUID:reply:]_block_invoke.62
- ___57-[CXCallSource reportAudioFinishedForCallWithUUID:reply:]_block_invoke.63
- ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.28
- ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.32
- ___60-[CXCallSource reportCallWithUUID:receivedDTMFUpdate:reply:]_block_invoke.33
- ___62-[CXProvider reportNewIncomingCallWithUUID:update:completion:]_block_invoke.162
- ___65-[CXCallSource reportOutgoingCallWithUUID:connectedAtDate:reply:]_block_invoke.56
- ___65-[CXCallSource reportOutgoingCallWithUUID:connectedAtDate:reply:]_block_invoke.57
- ___70-[CXCallSource reportOutgoingCallWithUUID:sentInvitationAtDate:reply:]_block_invoke.44
- ___70-[CXCallSource reportOutgoingCallWithUUID:sentInvitationAtDate:reply:]_block_invoke.45
- ___72-[CXCallSource reportCallWithUUID:changedMeterLevel:forDirection:reply:]_block_invoke.74
- ___72-[CXCallSource reportCallWithUUID:changedMeterLevel:forDirection:reply:]_block_invoke.75
- ___73-[CXCallSource reportOutgoingCallWithUUID:startedConnectingAtDate:reply:]_block_invoke.50
- ___73-[CXCallSource reportOutgoingCallWithUUID:startedConnectingAtDate:reply:]_block_invoke.51
- ___75-[CXCallSource reportCallWithUUID:changedFrequencyData:forDirection:reply:]_block_invoke.68
- ___75-[CXCallSource reportCallWithUUID:changedFrequencyData:forDirection:reply:]_block_invoke.69
- ___82-[CXCallSource reportCallWithUUID:endedAtDate:privateReason:failureContext:reply:]_block_invoke.38
- ___82-[CXCallSource reportCallWithUUID:endedAtDate:privateReason:failureContext:reply:]_block_invoke.39
- ___86-[CXCallSource reportCallWithUUID:crossDeviceIdentifier:changedBytesOfDataUsed:reply:]_block_invoke.81
- ___86-[CXCallSource reportCallWithUUID:crossDeviceIdentifier:changedBytesOfDataUsed:reply:]_block_invoke.82
- ___block_literal_global.35
- ___block_literal_global.41
- ___block_literal_global.47
- ___block_literal_global.53
- ___block_literal_global.59
- ___block_literal_global.65
- ___block_literal_global.71
- ___block_literal_global.77
CStrings:
+ "-[CXCallSource reportNewIncomingProtectedIMAVCallWithUUID:update:reply:]"
+ "-[CXProvider reportNewIncomingProtectedIMAVCallWithUUID:update:completion:]"
+ "Provider %@ was asked to report a new incoming protected call with UUID: %@ update: %@"
+ "callSource:reportedNewIncomingProtectedIMAVCallWithUUID:update:completion:"
+ "reportNewIncomingProtectedIMAVCallWithUUID:update:completion:"
+ "reportNewIncomingProtectedIMAVCallWithUUID:update:reply:"

```
