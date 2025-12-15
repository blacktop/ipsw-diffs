## RCS

> `/System/Library/Messages/PlugIns/RCS.imservice/RCS`

```diff

-1450.300.41.2.7
-  __TEXT.__text: 0xef6dc
-  __TEXT.__auth_stubs: 0x1d80
+1450.400.3.2.1
+  __TEXT.__text: 0xf2678
+  __TEXT.__auth_stubs: 0x1d90
   __TEXT.__objc_stubs: 0x40
-  __TEXT.__objc_methlist: 0x844
-  __TEXT.__const: 0x5a18
+  __TEXT.__objc_methlist: 0x85c
+  __TEXT.__const: 0x5b28
   __TEXT.__objc_classname: 0x96
-  __TEXT.__objc_methname: 0x4dee
+  __TEXT.__objc_methname: 0x4f2c
   __TEXT.__objc_methtype: 0xe70
-  __TEXT.__cstring: 0x32d5
-  __TEXT.__constg_swiftt: 0x2014
-  __TEXT.__swift5_typeref: 0x1f41
+  __TEXT.__cstring: 0x33b5
+  __TEXT.__constg_swiftt: 0x20a4
+  __TEXT.__swift5_typeref: 0x1f81
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_reflstr: 0x12ad
+  __TEXT.__swift5_reflstr: 0x1323
   __TEXT.__swift5_assocty: 0x2c8
-  __TEXT.__oslogstring: 0x5d69
-  __TEXT.__swift5_fieldmd: 0x1730
-  __TEXT.__swift5_proto: 0x300
-  __TEXT.__swift5_types: 0x1b0
-  __TEXT.__swift_as_entry: 0x250
-  __TEXT.__swift_as_ret: 0x2b0
-  __TEXT.__swift5_capture: 0x974
+  __TEXT.__oslogstring: 0x60f8
+  __TEXT.__swift5_fieldmd: 0x178c
+  __TEXT.__swift5_proto: 0x30c
+  __TEXT.__swift5_types: 0x1b8
+  __TEXT.__swift_as_entry: 0x254
+  __TEXT.__swift_as_ret: 0x2bc
+  __TEXT.__swift5_capture: 0x978
   __TEXT.__swift5_mpenum: 0xcc
   __TEXT.__swift5_protos: 0x50
-  __TEXT.__unwind_info: 0x3558
-  __TEXT.__eh_frame: 0x9130
-  __DATA_CONST.__auth_got: 0xec8
-  __DATA_CONST.__got: 0x858
-  __DATA_CONST.__auth_ptr: 0x5d0
-  __DATA_CONST.__const: 0x5390
-  __DATA_CONST.__objc_classlist: 0x88
+  __TEXT.__unwind_info: 0x35b0
+  __TEXT.__eh_frame: 0x9330
+  __DATA_CONST.__auth_got: 0xed0
+  __DATA_CONST.__got: 0x870
+  __DATA_CONST.__auth_ptr: 0x5e8
+  __DATA_CONST.__const: 0x5470
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA.__objc_const: 0x1ed0
-  __DATA.__objc_selrefs: 0x1630
+  __DATA.__objc_const: 0x1ff0
+  __DATA.__objc_selrefs: 0x1698
   __DATA.__objc_data: 0x448
-  __DATA.__data: 0x3690
-  __DATA.__bss: 0x4a80
+  __DATA.__data: 0x3780
+  __DATA.__bss: 0x4c00
   __DATA.__common: 0xd8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 950DA9B1-2B4F-397E-86DE-64E00AC900AA
-  Functions: 3402
-  Symbols:   417
-  CStrings:  1534
+  UUID: 4B3FB534-FFE5-3547-B2CC-D120F4FF627D
+  Functions: 3428
+  Symbols:   419
+  CStrings:  1562
 
Symbols:
+ _OBJC_CLASS_$_IMDServiceReachabilityController
+ _OBJC_CLASS_$_IMServiceReachabilityRequest
+ _OBJC_CLASS_$_IMUnifiedMessageMetric
- _IMChatPropertyLastKnownHybridState
CStrings:
+ "Attempting to add participants %{private}s for change ID %s"
+ "Ignoring reachability result allSupportEncryption(%{bool}d) for ID %s because result is not final"
+ "No encryption reachability result for addParticipantChange %s with requestID %s for %s"
+ "No encryption state defined on chat originalGroupID %s, defaulting to `.unencrypted`..."
+ "Not doing reachability request for %s for a new compose to a Google RBM, assume it's reachable"
+ "Removing stale reachabilityResult for requestID %s value %s"
+ "Sending %s operationID %s with encryption(%s), modifiedEncryption(%s)"
+ "Succeeded capabilities fetch for participant change ID %s, requestID %s, all support encryption: %s"
+ "Succeeded capabilities fetch\u00a0(FORCED) for addParticipantChange %s, all support encryption: %s"
+ "UserDefaults.forceEncryption is ON, forcing encryption for addParticipant change %s in %s"
+ "_TtC3RCS28RCSReachabilityResultHandler"
+ "__im_isGoogleRBM"
+ "accountID"
+ "addParticipants(_:to:allSupportEncryption:operation:)"
+ "allSupportEncryption"
+ "execute(telephonyParticipantChange:)"
+ "initWithHandleIDs:requestID:serviceName:accountID:context:"
+ "isFinal"
+ "isHybridGroup"
+ "legacyMetricSubmissionsDisabled"
+ "messageSize"
+ "messageType"
+ "reachabilityContextForChat:"
+ "reachabilityResultHandler"
+ "requestID"
+ "setMessageLatency:"
+ "setMessageStatus:"
+ "setMessageType:"
+ "submit"
+ "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:isEmergencyNumber:isPartiallyActiveSIM:error:"
+ "unifiedMetricForOutgoingMessage:inChat:transportType:"
- "bodyData"
- "handle"
- "totalBytes"
- "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:sourceHandle:destinationHandle:error:"

```
