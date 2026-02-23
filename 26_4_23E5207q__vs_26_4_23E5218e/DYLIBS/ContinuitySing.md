## ContinuitySing

> `/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing`

```diff

-665.100.6.0.0
-  __TEXT.__text: 0x5de18
+665.100.8.0.0
+  __TEXT.__text: 0x5e014
   __TEXT.__auth_stubs: 0x17f0
   __TEXT.__objc_methlist: 0x35bc
   __TEXT.__const: 0xe24
-  __TEXT.__gcc_except_tab: 0xb34
-  __TEXT.__cstring: 0x5b59
-  __TEXT.__oslogstring: 0x30e9
+  __TEXT.__gcc_except_tab: 0xb44
+  __TEXT.__cstring: 0x5b89
+  __TEXT.__oslogstring: 0x3139
   __TEXT.__ustring: 0x2a
   __TEXT.__swift5_typeref: 0x968
   __TEXT.__swift5_fieldmd: 0x340

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 50671F92-47C0-39AE-8224-A7C8DB439F63
+  UUID: EA891F88-A38C-3D41-B035-83BECE823AB5
   Functions: 1863
   Symbols:   5657
-  CStrings:  3384
+  CStrings:  3386
 
Symbols:
+ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.16
+ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.16.cold.1
+ ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke.27
+ ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke.27.cold.1
- ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.12.cold.1
- ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.14
- ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke_3
- ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke_3.cold.1
Functions:
~ -[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:] : 1020 -> 1132
~ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.12 : 168 -> 288
~ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.14 -> ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_2 : 288 -> 16
~ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_2 -> ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_3 : 16 -> 232
~ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_3 -> ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.16 : 212 -> 168
~ ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke.25 : 464 -> 572
~ ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke_3 -> ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke.27 : 288 -> 304
~ sub_24cfd4a8c -> sub_24d0e3b8c : 536 -> 628
~ sub_24cfe6c48 -> sub_24d0f5da4 : 1420 -> 1432
~ sub_24cfe7304 -> sub_24d0f646c : 5204 -> 5248
~ sub_24cfe88a8 -> sub_24d0f7a3c : 4376 -> 4428
~ sub_24cfe9ab0 -> sub_24d0f8c78 : 1320 -> 1328
~ sub_24cfea3e8 -> sub_24d0f95b8 : 536 -> 552
~ sub_24cfea600 -> sub_24d0f97e0 : 5028 -> 4980
~ sub_24cff140c -> sub_24d1005bc : 2180 -> 2256
CStrings:
+ "%s: Activating discovery client: %@"
+ "%s: Activating message client: %@"
+ "%s: Device found:%@, pending activation:%d"
+ "%s: Successfully activated message client: %@"
+ "-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]"
- "%s: Device found pending activation: %@"
- "%s: Successfully activated message client"
- "-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke_3"

```
