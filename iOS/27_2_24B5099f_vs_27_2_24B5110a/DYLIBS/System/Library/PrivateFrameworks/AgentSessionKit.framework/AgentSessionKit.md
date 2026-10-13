## AgentSessionKit

> `/System/Library/PrivateFrameworks/AgentSessionKit.framework/AgentSessionKit`

```diff

-297.12.0.1.2
-  __TEXT.__text: 0x8a954
-  __TEXT.__objc_methlist: 0x408
-  __TEXT.__swift5_typeref: 0x2742
-  __TEXT.__const: 0xbf5c
-  __TEXT.__constg_swiftt: 0x1e88
-  __TEXT.__swift5_reflstr: 0x16f5
-  __TEXT.__swift5_fieldmd: 0x2d68
+297.12.4.0.0
+  __TEXT.__text: 0x8d484
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
-  __TEXT.__swift5_capture: 0xb14
+  __TEXT.__cstring: 0x1f9a
+  __TEXT.__swift5_proto: 0xb4c
+  __TEXT.__swift5_types: 0x330
+  __TEXT.__swift5_capture: 0xa70
   __TEXT.__swift5_assocty: 0x300
-  __TEXT.__oslogstring: 0xb2c
+  __TEXT.__oslogstring: 0xb9c
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__swift_as_entry: 0x204
-  __TEXT.__swift_as_ret: 0x27c
-  __TEXT.__swift_as_cont: 0x4e4
-  __TEXT.__unwind_info: 0x4728
-  __TEXT.__eh_frame: 0x6400
+  __TEXT.__swift_as_entry: 0x20c
+  __TEXT.__swift_as_ret: 0x29c
+  __TEXT.__swift_as_cont: 0x500
+  __TEXT.__unwind_info: 0x47e0
+  __TEXT.__eh_frame: 0x6380
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x370
+  __DATA_CONST.__objc_selrefs: 0x380
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x83a8
-  __AUTH_CONST.__objc_const: 0xa18
-  __AUTH_CONST.__auth_got: 0xb50
+  __AUTH_CONST.__const: 0x8348
+  __AUTH_CONST.__objc_const: 0xa20
+  __AUTH_CONST.__auth_got: 0xb68
   __AUTH.__objc_data: 0x48
   __AUTH.__data: 0x688
-  __DATA.__data: 0x1148
+  __DATA.__data: 0x11c0
   __DATA_DIRTY.__objc_data: 0x98
-  __DATA_DIRTY.__data: 0x2558
+  __DATA_DIRTY.__data: 0x2598
   __DATA_DIRTY.__bss: 0x9580
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6169
-  Symbols:   191
-  CStrings:  279
+  Functions: 6227
+  Symbols:   192
+  CStrings:  282
 
Symbols:
+ _swift_getKeyPath
+ _swift_readAtKeyPath
+ _swift_retain_x28
+ _swift_setAtWritableKeyPath
- _swift_asyncLet_begin
- _swift_asyncLet_finish
- _swift_asyncLet_get
CStrings:
+ "AgentEventUpdate.observationDidReset"
+ "AgentSessionStore failed to sync event forwarding: %{public}@"
+ "AgentSessionStore failed to sync session forwarding: %{public}@"
+ "AgentSessionStore not recovering forwarding: no consumer stream exists."
+ "AgentSessionStore not recovering forwarding: released, so the daemon is left to exit."
+ "AgentSessionStore release found the daemon already gone: %{public}@"
+ "AgentSessionUpdate.observationDidReset"
+ "observationDidReset"
+ "observationDidReset must not be sent over XPC"
- "AgentSessionStore failed to resubscribe to event updates: %@"
- "AgentSessionStore failed to resubscribe to session updates: %@"
- "Failed to subscribe to event updates: %s"
- "Failed to subscribe to session updates: %s"
- "Failed to unsubscribe from event updates: %s"
- "Failed to unsubscribe from session updates: %s"
```
