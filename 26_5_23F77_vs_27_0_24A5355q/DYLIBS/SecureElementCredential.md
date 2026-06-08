## SecureElementCredential

> `/System/Library/Frameworks/SecureElementCredential.framework/SecureElementCredential`

```diff

-65.3.1.0.0
-  __TEXT.__text: 0x20cbc
-  __TEXT.__auth_stubs: 0xb90
+70.31.1.0.0
+  __TEXT.__text: 0x1e1b0
   __TEXT.__objc_methlist: 0x1e0
-  __TEXT.__const: 0x14c0
-  __TEXT.__swift5_typeref: 0x684
-  __TEXT.__swift5_capture: 0x580
-  __TEXT.__swift_as_entry: 0x130
-  __TEXT.__swift_as_ret: 0x108
+  __TEXT.__const: 0x14d8
+  __TEXT.__swift5_typeref: 0x679
+  __TEXT.__swift5_capture: 0x568
+  __TEXT.__swift_as_entry: 0x120
+  __TEXT.__swift_as_ret: 0xfc
+  __TEXT.__swift_as_cont: 0x294
   __TEXT.__swift5_fieldmd: 0x538
   __TEXT.__constg_swiftt: 0x440
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__oslogstring: 0x671
   __TEXT.__cstring: 0x708
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x9f8
-  __TEXT.__eh_frame: 0x1b64
-  __TEXT.__objc_classname: 0x1f8
-  __TEXT.__objc_methname: 0x6c6
-  __TEXT.__objc_methtype: 0x6ce
-  __TEXT.__objc_stubs: 0x3c0
-  __DATA_CONST.__got: 0x100
+  __TEXT.__unwind_info: 0x9c8
+  __TEXT.__eh_frame: 0x1924
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x138
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0x5d0
-  __AUTH_CONST.__const: 0x18f8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x1920
   __AUTH_CONST.__objc_const: 0x578
+  __AUTH_CONST.__auth_got: 0x658
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x4e8
-  __DATA.__data: 0x2d0
+  __DATA.__data: 0x2c8
   __DATA.__bss: 0xf80
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D5AE17D2-97E4-36DD-AC8E-D3E654DA7FAD
-  Functions: 780
-  Symbols:   126
-  CStrings:  167
+  UUID: 2F2A0E17-2AE3-300F-80AB-26091437B1ED
+  Functions: 785
+  Symbols:   142
+  CStrings:  67
 
Symbols:
+ _swift_release_x10
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x27
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x26
- _swift_retain_n
- _swift_unknownObjectRetain_n
CStrings:
- "$defaultActor"
- "@16@0:8"
- "@24@0:8@?16"
- "@24@0:8@?<v@?@\"NSError\">16"
- "NSXPCProxyCreating"
- "SecureElementCredential"
- "_TtC23SecureElementCredential17CredentialSession"
- "_TtC23SecureElementCredential9SECClient"
- "_TtCC23SecureElementCredential17CredentialSession26PresentmentIntentAssertion"
- "_TtP23SecureElementCredential18SECredentialServer_"
- "_TtP23SecureElementCredential25SECredentialServerSession_"
- "_TtP23SecureElementCredential27SECSessionCallbackInterface_"
- "_TtP23SecureElementCredential38SECredentialPresentmentIntentAssertion_"
- "acquirePresentmentIntentAssertionWithReply:"
- "activate"
- "armCredentialForCardEmulation:sceneIdentifier:reply:"
- "armCurrentCredentialForCardEmulationWithSceneIdentifier:reply:"
- "assertionProxy"
- "authorizeCredentialInWiredModeWith:instanceAID:sceneIdentifier:reply:"
- "computeEligibilityWithReply:"
- "connection"
- "createCredentialWithServerConfigUUID:friendlyName:reply:"
- "currentAssertion"
- "currentEventStream"
- "currentEventStreamContinuation"
- "delegate"
- "deleteCredential:reply:"
- "endCardEmulationWithReply:"
- "endWiredModeWithReply:"
- "endWithReply:"
- "getAssertionStateWithReply:"
- "getSessionStateWithReply:"
- "initWithMachServiceName:options:"
- "installationCompletedWithCredentials:completionHandler:"
- "interfaceWithProtocol:"
- "listCredentialUUIDAndNamesWithReply:"
- "modifyAccessForCredential:addingOwners:removingOwners:addingUsers:removingUsers:reply:"
- "presentmentAssertionTimeoutWithError:completionHandler:"
- "queueSessionWithCallbackProxy:reply:"
- "receivedHciDataWithData:appletIdentifier:completionHandler:"
- "relinquishAssertionWithReply:"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "remoteProxy"
- "rfFieldChanged:completionHandler:"
- "secureElementInfoWithReply:"
- "securityDomainCounterFor:reply:"
- "sessionEndedWithError:"
- "sessionErrorEventWithReason:completionHandler:"
- "sessionIdentifier"
- "sessionStarted"
- "sessionStartedContinuation"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setCredentialInWiredModeWith:reply:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterface:forSelector:argumentIndex:ofReply:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "transceive:reply:"
- "v16@?0@\"NSError\"8"
- "v16@?0q8"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?>16"
- "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSError\">16"
- "v24@0:8@?<v@?@\"NSObject\"@\"NSError\">16"
- "v24@0:8@?<v@?@\"_TtC9SEService23SECHardwareInfoInternal\"@\"NSError\">16"
- "v24@0:8@?<v@?q>16"
- "v24@0:8@?<v@?q@\"_TtC9SEService18CredentialInternal\">16"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v24@?0@\"NSData\"8@\"NSError\"16"
- "v24@?0@\"NSNumber\"8@\"NSError\"16"
- "v24@?0@\"NSObject\"8@\"NSError\"16"
- "v24@?0@\"_TtC9SEService18CredentialInternal\"8@\"NSError\"16"
- "v24@?0@\"_TtC9SEService23SECHardwareInfoInternal\"8@\"NSError\"16"
- "v24@?0q8@\"_TtC9SEService18CredentialInternal\"16"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?>20"
- "v32@0:8@\"<_TtP23SecureElementCredential27SECSessionCallbackInterface_>\"16@?<v@?@\"NSObject\"@\"NSError\">24"
- "v32@0:8@\"NSArray\"16@?<v@?>24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSNumber\"@\"NSError\">24"
- "v32@0:8@\"NSError\"16@?<v@?>24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSUUID\"16@?<v@?@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSData\"16@\"NSData\"24@?<v@?>32"
- "v40@0:8@\"NSUUID\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSUUID\"16@\"NSString\"24@?<v@?@\"_TtC9SEService18CredentialInternal\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSUUID\"16@\"NSData\"24@\"NSString\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v64@0:8@\"NSUUID\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"NSArray\"48@?<v@?@\"NSError\">56"
- "v64@0:8@16@24@32@40@48@?56"
- "v8@?0"

```
