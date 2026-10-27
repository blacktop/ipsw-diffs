## SiriRequestDispatcher

> `/System/Library/PrivateFrameworks/SiriRequestDispatcher.framework/Versions/A/SiriRequestDispatcher`

```diff

-3600.54.24.0.0
-  __TEXT.__text: 0x2da70
-  __TEXT.__objc_methlist: 0x598
-  __TEXT.__const: 0x1b30
-  __TEXT.__swift5_typeref: 0xc95
-  __TEXT.__swift5_fieldmd: 0x810
-  __TEXT.__constg_swiftt: 0x10a8
+3605.26.1.0.0
+  __TEXT.__text: 0x300a0
+  __TEXT.__objc_methlist: 0x5b8
+  __TEXT.__const: 0x1c50
+  __TEXT.__swift5_typeref: 0xcb9
+  __TEXT.__swift5_fieldmd: 0x878
+  __TEXT.__constg_swiftt: 0x111c
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_reflstr: 0x8e8
+  __TEXT.__swift5_reflstr: 0x958
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_protos: 0x24
-  __TEXT.__swift5_proto: 0x98
-  __TEXT.__swift5_types: 0xac
-  __TEXT.__swift5_capture: 0x580
-  __TEXT.__oslogstring: 0x2417
-  __TEXT.__cstring: 0x785
+  __TEXT.__swift5_proto: 0xa4
+  __TEXT.__swift5_types: 0xb4
+  __TEXT.__swift5_capture: 0x6b4
+  __TEXT.__oslogstring: 0x25b7
+  __TEXT.__cstring: 0x839
   __TEXT.__swift_as_entry: 0x2c
   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift_as_cont: 0x64
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xb38
-  __TEXT.__eh_frame: 0xb28
+  __TEXT.__unwind_info: 0xbb0
+  __TEXT.__eh_frame: 0xb10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x240
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b8
+  __DATA_CONST.__objc_selrefs: 0x5c8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x2040
-  __AUTH_CONST.__objc_const: 0x4018
-  __AUTH_CONST.__auth_got: 0x9c0
-  __AUTH_CONST.__auth_ptr: 0x328
-  __AUTH.__objc_data: 0xb0
-  __AUTH.__data: 0x28
-  __DATA.__data: 0x6a0
-  __DATA.__bss: 0xe00
+  __AUTH_CONST.__const: 0x23c8
+  __AUTH_CONST.__objc_const: 0x41b8
+  __AUTH_CONST.__auth_got: 0x9f8
+  __AUTH_CONST.__auth_ptr: 0x330
+  __AUTH.__objc_data: 0x100
+  __AUTH.__data: 0xe0
+  __DATA.__data: 0x6b8
+  __DATA.__bss: 0xf80
   __DATA_DIRTY.__objc_data: 0xa0
-  __DATA_DIRTY.__data: 0xf48
+  __DATA_DIRTY.__data: 0xf58
   __DATA_DIRTY.__common: 0xd8
   __DATA_DIRTY.__bss: 0x300
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1474
-  Symbols:   764
-  CStrings:  180
+  Functions: 1553
+  Symbols:   775
+  CStrings:  189
 
Symbols:
+ __DATA__TtC21SiriRequestDispatcher27RequestProcessorHandoffGate
+ __IVARS__TtC21SiriRequestDispatcher27RequestProcessorHandoffGate
+ __METACLASS_DATA__TtC21SiriRequestDispatcher27RequestProcessorHandoffGate
+ _associated conformance 21SiriRequestDispatcher0A25DeviceRoutingFeatureFlagsOSHAASQ
+ _dispatch_resume
+ _dispatch_suspend
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _symbolic Say_____G 21SiriRequestDispatcher0B13ProcessorBaseC
+ _symbolic _____ 21SiriRequestDispatcher0A25DeviceRoutingFeatureFlagsO
+ _symbolic _____ 21SiriRequestDispatcher0B20ProcessorHandoffGateC
+ _symbolic _____ 8Dispatch0A8WorkItemC
CStrings:
+ "#AsyncSequentialExecutor Dropping async task submitted after main loop finished, with no drop handler: %s"
+ "#AsyncSequentialExecutor Dropping async task submitted after main loop finished: %s"
+ "Holding request %{public}s while outgoing request %{public}s finishes"
+ "Message %{public}s is not registered by any handler"
+ "No RequestProcessor claimed message: %{public}s with requestId: %{public}s. Offered to %{public}ld. Dropping it."
+ "Not holding request %{public}s: it is already the outgoing processor, so there is nothing to wait for"
+ "Previous processor for requestId: %{public}s is still active; holding request %{public}s until it finishes"
+ "Request %{public}s did not finish processing pending messages in time, starting request %{public}s anyway"
+ "Resuming %{public}s: %{public}s"
+ "SiriCrossDeviceArbitration"
+ "outgoing request drained"
+ "outgoing request timed out"
+ "siriDeviceRouting"
+ "siriDeviceRoutingMessageCenterTransport"
- "Previous processor for requestId: %s didn't finish processing all pending messages, creating a new processor"
- "Previous processor for requestId: %s finished processing all pending messages"
- "Timed out waiting for ActiveRequestProcessor with requestId: %s to finish processing."
- "We still have previous processor checking waiting for it to finish"
- "Will wait up to %s for the current active request to finish"
```
