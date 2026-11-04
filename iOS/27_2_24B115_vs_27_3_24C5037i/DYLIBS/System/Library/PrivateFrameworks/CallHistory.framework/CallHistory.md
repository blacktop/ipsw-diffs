## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-156.200.131.2.6
-  __TEXT.__text: 0x1b2c14
+156.300.51.0.0
+  __TEXT.__text: 0x1b2e50
   __TEXT.__objc_methlist: 0x3c04
   __TEXT.__const: 0x1e960
   __TEXT.__cstring: 0x42e4
-  __TEXT.__oslogstring: 0x6369
+  __TEXT.__oslogstring: 0x6459
   __TEXT.__gcc_except_tab: 0x7e8
   __TEXT.__dlopen_cstrs: 0x147
   __TEXT.__constg_swiftt: 0x1155c

   __TEXT.__swift_as_cont: 0x120
   __TEXT.__swift5_capture: 0x438
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0xaf50
+  __TEXT.__unwind_info: 0xaf60
   __TEXT.__eh_frame: 0x7b10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12495
+  Functions: 12496
   Symbols:   5011
-  CStrings:  1087
+  CStrings:  1091
 
Functions:
~ -[CHRecentCall callerIdLocation] : 276 -> 76
~ -[CHRecentCall setLocationTo:] : 12 -> 216
~ -[CallHistoryDBHandle migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:] : 848 -> 892
~ -[CHRecentCall setLocationOnQueue:completion:] : 400 -> 704
~ ___46-[CHRecentCall setLocationOnQueue:completion:]_block_invoke_2 : 60 -> 228
+ -[CallHistoryDBHandle migrateAllDataFromExtensionWithApplicationID:toExtensionWithApplicationID:withCompletionHandler:].cold.1
CStrings:
+ "156.300.51"
+ "156.300.51~23"
+ "==> callerIdLocation resolved for %@ -> %{public}@"
+ "==> callerIdLocation resolved for %@ -> %{public}@ (handle is not a phone number)"
+ "==> callerIdLocation resolved for %@ -> %{public}@ (no single valid remote handle)"
+ "==> callerIdLocation set for %@ -> %{public}@"
+ "Call record query failed"
- "156.200.131.2.6"
- "156.200.131.2.6~1"
- "==> %{public}@. Current location info for %@ is %@"
```
