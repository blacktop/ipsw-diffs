## NetworkInfo

> `/System/Library/PrivateFrameworks/NetworkInfo.framework/NetworkInfo`

```diff

-194.100.10.0.0
-  __TEXT.__text: 0xebcc0
-  __TEXT.__auth_stubs: 0x23a0
+194.120.6.0.0
+  __TEXT.__text: 0xeca9c
+  __TEXT.__auth_stubs: 0x23b0
   __TEXT.__objc_methlist: 0x8f4
   __TEXT.__const: 0x35d0
-  __TEXT.__cstring: 0x3ebf
-  __TEXT.__oslogstring: 0x2234
+  __TEXT.__cstring: 0x3f1f
+  __TEXT.__oslogstring: 0x22a4
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__swift5_typeref: 0xf85
   __TEXT.__swift5_capture: 0x292c

   __DATA_CONST.__objc_selrefs: 0x5e0
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x11e0
+  __AUTH_CONST.__auth_got: 0x11e8
   __AUTH_CONST.__const: 0x8660
   __AUTH_CONST.__cfstring: 0x320
   __AUTH_CONST.__objc_const: 0x2518

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4E606817-9228-3F7C-8290-A85244B6FF36
+  UUID: A747C445-303B-3EE2-B56B-4FF9672B4294
   Functions: 3496
-  Symbols:   1980
-  CStrings:  1331
+  Symbols:   1984
+  CStrings:  1335
 
Symbols:
+ -[PacketCaptureur startTask:destination:withCompletion:].cold.1
+ -[PacketCaptureur stopTask:withCompletion:].cold.1
+ ___43-[PacketCaptureur stopTask:withCompletion:]_block_invoke.26
+ ___56-[PacketCaptureur startTask:destination:withCompletion:]_block_invoke.19
- ___43-[PacketCaptureur stopTask:withCompletion:]_block_invoke_2
- ___56-[PacketCaptureur startTask:destination:withCompletion:]_block_invoke_2
CStrings:
+ "%s:%u - No connection to XPC service, cannot start task: %@"
+ "%s:%u - No connection to XPC service, cannot stop task: %@"
+ "-[PacketCaptureur startTask:destination:withCompletion:]"
+ "-[PacketCaptureur startTask:destination:withCompletion:]_block_invoke"
+ "-[PacketCaptureur stopTask:withCompletion:]"
+ "-[PacketCaptureur stopTask:withCompletion:]_block_invoke"
- "-[PacketCaptureur startTask:destination:withCompletion:]_block_invoke_2"
- "-[PacketCaptureur stopTask:withCompletion:]_block_invoke_2"

```
