## AgentSessionKit

> `/System/Library/PrivateFrameworks/AgentSessionKit.framework/Versions/A/AgentSessionKit`

```diff

-291.6.0.3.203
-  __TEXT.__text: 0x8c178
-  __TEXT.__objc_methlist: 0x3f8
-  __TEXT.__swift5_typeref: 0x267e
-  __TEXT.__const: 0xbe6c
-  __TEXT.__constg_swiftt: 0x1e78
-  __TEXT.__swift5_reflstr: 0x1675
-  __TEXT.__swift5_fieldmd: 0x2d08
+297.12.2.1.0
+  __TEXT.__text: 0x96970
+  __TEXT.__objc_methlist: 0x418
+  __TEXT.__swift5_typeref: 0x2800
+  __TEXT.__const: 0xc15c
+  __TEXT.__constg_swiftt: 0x1f10
+  __TEXT.__swift5_reflstr: 0x1785
+  __TEXT.__swift5_fieldmd: 0x2ddc
   __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__cstring: 0x1f1a
-  __TEXT.__swift5_proto: 0xb34
-  __TEXT.__swift5_types: 0x328
-  __TEXT.__swift5_capture: 0x81c
+  __TEXT.__cstring: 0x1f9a
+  __TEXT.__swift5_proto: 0xb4c
+  __TEXT.__swift5_types: 0x330
+  __TEXT.__swift5_capture: 0xa70
   __TEXT.__swift5_assocty: 0x300
-  __TEXT.__oslogstring: 0xacc
+  __TEXT.__oslogstring: 0xb9c
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__swift_as_entry: 0x1d0
-  __TEXT.__swift_as_ret: 0x1fc
-  __TEXT.__swift_as_cont: 0x48c
-  __TEXT.__unwind_info: 0x39f0
-  __TEXT.__eh_frame: 0x5fb0
+  __TEXT.__swift_as_entry: 0x20c
+  __TEXT.__swift_as_ret: 0x29c
+  __TEXT.__swift_as_cont: 0x500
+  __TEXT.__unwind_info: 0x3c08
+  __TEXT.__eh_frame: 0x6398
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x358
+  __DATA_CONST.__objc_selrefs: 0x380
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x7c20
-  __AUTH_CONST.__objc_const: 0xa10
-  __AUTH_CONST.__auth_got: 0x9b0
+  __AUTH_CONST.__const: 0x8348
+  __AUTH_CONST.__objc_const: 0xa20
+  __AUTH_CONST.__auth_got: 0x9f0
   __AUTH_CONST.__auth_ptr: 0x4b0
   __AUTH.__objc_data: 0x48
-  __AUTH.__data: 0x7a0
-  __DATA.__data: 0x1460
-  __DATA.__bss: 0xf200
+  __AUTH.__data: 0x688
+  __DATA.__data: 0x11c0
+  __DATA.__bss: 0xd410
   __DATA_DIRTY.__objc_data: 0x98
-  __DATA_DIRTY.__data: 0x20a8
-  __DATA_DIRTY.__bss: 0x7480
+  __DATA_DIRTY.__data: 0x2560
+  __DATA_DIRTY.__bss: 0x9580
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5919
-  Symbols:   141
-  CStrings:  275
+  Functions: 6217
+  Symbols:   146
+  CStrings:  282
 
Symbols:
+ _NSCocoaErrorDomain
+ _swift_getKeyPath
+ _swift_readAtKeyPath
+ _swift_release_n
+ _swift_retain_n
+ _swift_setAtWritableKeyPath
+ _swift_setDeallocating
+ _swift_task_future_wait_throwing
- _swift_asyncLet_begin
- _swift_asyncLet_finish
- _swift_asyncLet_get
CStrings:
+ "AgentEventUpdate.observationDidReset"
+ "AgentSessionStore XPC call interrupted, re-sending (attempt %{public}ld of %{public}ld)."
+ "AgentSessionStore failed to sync event forwarding: %{public}@"
+ "AgentSessionStore failed to sync session forwarding: %{public}@"
+ "AgentSessionStore not recovering forwarding: no consumer stream exists."
+ "AgentSessionStore not recovering forwarding: released, so the daemon is left to exit."
+ "AgentSessionStore release found the daemon already gone: %{public}@"
+ "AgentSessionUpdate.observationDidReset"
+ "CascadeDonationDeletedForWatchOSDisable"
+ "QuotaBackoffExponent"
+ "QuotaHoldOffUntil"
+ "Remote Configuration:"
+ "observationDidReset"
+ "observationDidReset must not be sent over XPC"
+ "remoteConfiguration"
+ "remoteConfigurationDefaults"
- "AgentSessionKit/AgentSessionStoreXPCService.swift"
- "AgentSessionStore failed to resubscribe to event updates: %@"
- "AgentSessionStore failed to resubscribe to session updates: %@"
- "AgentSessionStoreXPCClient: BidirectionalXPCServiceClientConnection.init failed: "
- "CascadeFullDonationAfterV15ResetCompleted"
- "Failed to subscribe to event updates: %s"
- "Failed to subscribe to session updates: %s"
- "Failed to unsubscribe from event updates: %s"
- "Failed to unsubscribe from session updates: %s"
```
