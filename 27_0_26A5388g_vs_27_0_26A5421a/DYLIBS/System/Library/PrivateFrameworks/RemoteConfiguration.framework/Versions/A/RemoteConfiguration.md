## RemoteConfiguration

> `/System/Library/PrivateFrameworks/RemoteConfiguration.framework/Versions/A/RemoteConfiguration`

```diff

-423.0.0.0.0
-  __TEXT.__text: 0x2f758
+424.0.0.0.0
+  __TEXT.__text: 0x2faac
   __TEXT.__objc_methlist: 0x2ff4
-  __TEXT.__const: 0x208
+  __TEXT.__const: 0x210
   __TEXT.__gcc_except_tab: 0x6cc
-  __TEXT.__oslogstring: 0x1d1d
+  __TEXT.__oslogstring: 0x1d91
   __TEXT.__cstring: 0x4f43
   __TEXT.__swift5_typeref: 0x187
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x28
-  __TEXT.__unwind_info: 0xd70
+  __TEXT.__unwind_info: 0xd78
   __TEXT.__eh_frame: 0x1b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  Functions: 1451
-  Symbols:   3014
-  CStrings:  551
+  Functions: 1453
+  Symbols:   3016
+  CStrings:  552
 
Symbols:
+ RCNumberArrayByDroppingNonNumbers
+ _RCNumberArrayByDroppingNonNumbers
Functions:
~ -[RCConfigurationResource initWithCoder:] : 1112 -> 1176
~ -[RCConfigurationResource setTreatmentIDs:] : 12 -> 72
~ -[RCConfigurationResource setSegmentSetIDs:] : 12 -> 72
+ _RCNumberArrayByDroppingNonNumbers
+ RCNumberArrayByDroppingNonNumbers.cold.1
CStrings:
+ "dropped %lu non-number treatment/segment ID element(s); expected JSON numbers (first: %{public}@, class %{public}@)"
```
