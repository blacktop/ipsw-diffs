## InputAnalytics

> `/System/Library/PrivateFrameworks/InputAnalytics.framework/InputAnalytics`

```diff

-111.4.6.0.0
-  __TEXT.__text: 0x20c40
+111.5.1.0.0
+  __TEXT.__text: 0x20da4
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x25dc
+  __TEXT.__objc_methlist: 0x260c
   __TEXT.__const: 0x32a
   __TEXT.__gcc_except_tab: 0x48c
-  __TEXT.__cstring: 0x4de2
-  __TEXT.__oslogstring: 0x296c
+  __TEXT.__cstring: 0x5092
+  __TEXT.__oslogstring: 0x27ac
   __TEXT.__ustring: 0x4
   __TEXT.__swift5_typeref: 0x8b
   __TEXT.__constg_swiftt: 0x4c

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0x9f8
+  __TEXT.__unwind_info: 0xa00
   __TEXT.__eh_frame: 0x310
   __TEXT.__objc_classname: 0x74d
-  __TEXT.__objc_methname: 0x4cae
-  __TEXT.__objc_methtype: 0xadd
-  __TEXT.__objc_stubs: 0x3240
+  __TEXT.__objc_methname: 0x4dae
+  __TEXT.__objc_methtype: 0xb0d
+  __TEXT.__objc_stubs: 0x3260
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__const: 0x1a50
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11e0
+  __DATA_CONST.__objc_selrefs: 0x1200
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0xea0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: DA04CB9F-A86F-3FAA-BB17-07BB2884633E
-  Functions: 1037
-  Symbols:   4176
-  CStrings:  3257
+  UUID: B379D921-A544-3FB1-B073-83FD6E463984
+  Functions: 1035
+  Symbols:   4169
+  CStrings:  3268
 
Symbols:
+ +[IASignalAnalytics _dispatchSignal:caller:]
+ +[IASignalAnalytics _dispatchSignal:caller:].cold.1
+ +[IASignalAnalytics sendSignal:toChannel:withCreationTimestamp:withPayload:]
+ +[IASignalAnalytics sendSignal:toChannel:withNullableSessionID:withCreationTimestamp:withPayload:]
+ +[IASignalAnalytics sendSignal:toChannel:withNullableUniqueStringID:withCreationTimestamp:withPayload:]
+ _objc_msgSend$_dispatchSignal:caller:
- +[IASignalAnalytics sendSignal:toChannel:withNullableSessionID:withPayload:].cold.1
- +[IASignalAnalytics sendSignal:toChannel:withNullableUniqueStringID:withPayload:].cold.1
- +[IASignalAnalytics sendSignal:toChannel:withPayload:].cold.1
- ___81+[IASignalAnalytics asyncSendSignal:toChannel:withNullableSessionID:withPayload:]_block_invoke.cold.1
- ___86+[IASignalAnalytics asyncSendSignal:toChannel:withNullableUniqueStringID:withPayload:]_block_invoke.cold.1
CStrings:
+ "%{private}s server does not respond to didAction. xpc client 0x%lx with server 0x%lx"
+ "+[IASignalAnalytics asyncSendSignal:toChannel:withNullableSessionID:withPayload:]_block_invoke"
+ "+[IASignalAnalytics asyncSendSignal:toChannel:withNullableUniqueStringID:withPayload:]_block_invoke"
+ "+[IASignalAnalytics sendSignal:toChannel:withCreationTimestamp:withPayload:]"
+ "+[IASignalAnalytics sendSignal:toChannel:withNullableSessionID:withCreationTimestamp:withPayload:]"
+ "+[IASignalAnalytics sendSignal:toChannel:withNullableSessionID:withPayload:]"
+ "+[IASignalAnalytics sendSignal:toChannel:withNullableUniqueStringID:withCreationTimestamp:withPayload:]"
+ "+[IASignalAnalytics sendSignal:toChannel:withNullableUniqueStringID:withPayload:]"
+ "+[IASignalAnalytics sendSignal:toChannel:withPayload:]"
+ "_dispatchSignal:caller:"
+ "channel:%{private}@ signal:%{private}@ creationTimestamp:%{private}f timestamp:%{private}f payload:%{sensitive}@"
+ "sendSignal:toChannel:withCreationTimestamp:withPayload:"
+ "sendSignal:toChannel:withNullableSessionID:withCreationTimestamp:withPayload:"
+ "sendSignal:toChannel:withNullableUniqueStringID:withCreationTimestamp:withPayload:"
+ "v32@0:8@16r*24"
+ "v56@0:8@16@24@32@40@48"
- "asyncSendSignal:toChannel:withNullableSessionID:withPayload: server does not respond to didAction. xpc client 0x%lx with server 0x%lx"
- "asyncSendSignal:toChannel:withNullableUniqueStringID:withPayload: server does not respond to didAction. xpc client 0x%lx with server 0x%lx"
- "sendSignal:toChannel:withNullableSessionID:withPayload: server does not respond to didAction. xpc client 0x%lx with server 0x%lx"
- "sendSignal:toChannel:withNullableUniqueStringID:withPayload: server does not respond to didAction. xpc client 0x%lx with server 0x%lx"
- "sendSignal:toChannel:withPayload: server does not respond to didAction. xpc client 0x%lx with server 0x%lx"

```
