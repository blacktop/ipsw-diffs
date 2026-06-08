## SatelliteSMS

> `/System/Library/Messages/PlugIns/SatelliteSMS.imservice/SatelliteSMS`

```diff

-1450.600.61.2.7
-  __TEXT.__text: 0xdf10
-  __TEXT.__auth_stubs: 0xb70
-  __TEXT.__objc_stubs: 0xfe0
+1481.100.29.2.9
+  __TEXT.__text: 0xde6c
+  __TEXT.__auth_stubs: 0xc40
+  __TEXT.__objc_stubs: 0x1060
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x648
-  __TEXT.__objc_methname: 0x13a0
+  __TEXT.__objc_methname: 0x1437
   __TEXT.__oslogstring: 0x96d
   __TEXT.__objc_methtype: 0x302
   __TEXT.__swift5_typeref: 0x21c
   __TEXT.__swift5_capture: 0x38
-  __TEXT.__cstring: 0x3b5
+  __TEXT.__cstring: 0x3be
   __TEXT.__constg_swiftt: 0x188
   __TEXT.__swift5_reflstr: 0x103
   __TEXT.__swift5_fieldmd: 0xf4
-  __TEXT.__objc_classname: 0x137
+  __TEXT.__objc_classname: 0x127
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x30
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0x14
   __TEXT.__gcc_except_tab: 0x30
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x308
   __TEXT.__eh_frame: 0x258
-  __DATA_CONST.__auth_got: 0x5c8
-  __DATA_CONST.__got: 0x218
-  __DATA_CONST.__auth_ptr: 0x160
-  __DATA_CONST.__const: 0x650
+  __DATA_CONST.__const: 0x5b0
   __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__auth_got: 0x630
+  __DATA_CONST.__got: 0x220
+  __DATA_CONST.__auth_ptr: 0x1e0
   __DATA.__objc_const: 0x840
-  __DATA.__objc_selrefs: 0x508
+  __DATA.__objc_selrefs: 0x528
   __DATA.__objc_ivar: 0x3c
   __DATA.__objc_data: 0x1b0
   __DATA.__data: 0x438

   - /System/Library/PrivateFrameworks/IMDaemonCore.framework/IMDaemonCore
   - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
   - /System/Library/PrivateFrameworks/IMSharedUtilities.framework/IMSharedUtilities
+  - /System/Library/PrivateFrameworks/MessagesSecurityPolicy.framework/MessagesSecurityPolicy
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 7028D41E-5AB9-336E-A7D4-1B271BCD0DA6
-  Functions: 248
-  Symbols:   204
-  CStrings:  320
+  UUID: D1A4874B-570D-346E-B4D4-8E6524B21857
+  Functions: 247
+  Symbols:   216
+  CStrings:  324
 
Symbols:
+ _OBJC_CLASS_$_IMSecurityPolicyManager
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x28
+ _objc_retain_x3
+ _objc_retain_x9
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x24
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x28
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftVideoToolbox
- _swift_unknownObjectRelease_n
CStrings:
+ "finalResultForService:handleIDs:allAreReachable:allSupportEncryption:allSupportReplies:checkedServer:error:"
+ "finalResultForService:handleIDs:allAreReachable:allSupportEncryption:allSupportReplies:handleIsReachable:handleSupportsEncryption:checkedServer:error:"
+ "isCentralizedKnownSenderPolicyEnabled"
+ "isKnownSenderForHandleID:"
+ "labelID"
+ "sharedManager"
+ "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:isEmergencyNumber:isPartiallyActiveSIM:isEncrypted:strugglingMessageIndicationSent:error:ckvPolicyMetrics:"
+ "updateLastAddressedHandle:forceUpdate:"
+ "updateLastAddressedSIMID:"
- "finalResultForService:handleIDs:allAreReachable:allSupportEncryption:checkedServer:error:"
- "finalResultForService:handleIDs:allAreReachable:allSupportEncryption:handleIsReachable:handleSupportsEncryption:checkedServer:error:"
- "isSatelliteContinuityEnabled"
- "isSatelliteRelayEnabled"
- "trackSentMessageEventOfType:subtype:originalServiceName:messageSize:sendDuration:receiverType:receiverGroupType:wasSuccessful:isEmergencyNumber:isPartiallyActiveSIM:isEncrypted:strugglingMessageIndicationSent:error:"

```
