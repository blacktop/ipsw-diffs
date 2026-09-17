## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/Versions/A/SPOwner`

```diff

-449.20.6.14.21
-  __TEXT.__text: 0x7b25c
+449.21.6.16.15
+  __TEXT.__text: 0x7b450
   __TEXT.__objc_methlist: 0xbe34
   __TEXT.__const: 0x5e8
   __TEXT.__gcc_except_tab: 0x1514
   __TEXT.__cstring: 0x6a49
-  __TEXT.__oslogstring: 0x8378
+  __TEXT.__oslogstring: 0x8438
   __TEXT.__constg_swiftt: 0x148
   __TEXT.__swift5_typeref: 0x133
   __TEXT.__swift5_builtin: 0x28

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x2f68
+  __TEXT.__unwind_info: 0x2f70
   __TEXT.__eh_frame: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4426
-  Symbols:   8982
-  CStrings:  1591
+  Functions: 4428
+  Symbols:   8983
+  CStrings:  1594
 
Symbols:
+ -[SPBeaconManager submitDeviceEvent:source:timestamp:attachedTo:completion:]
+ _OUTLINED_FUNCTION_4
+ ___76-[SPBeaconManager submitDeviceEvent:source:timestamp:attachedTo:completion:]_block_invoke
+ ___block_descriptor_76_e8_32s40s48s56s64bs_e5_v8?0l
+ _objc_msgSend$submitDeviceEvent:source:timestamp:attachedTo:completion:
- -[SPBeaconManager submitDeviceEvent:source:attachedTo:completion:]
- ___66-[SPBeaconManager submitDeviceEvent:source:attachedTo:completion:]_block_invoke
- ___block_descriptor_68_e8_32s40s48s56bs_e5_v8?0l
- _objc_msgSend$submitDeviceEvent:source:attachedTo:completion:
CStrings:
+ "NVRAM data (length %lu) failed to deserialize as a property list: %@"
+ "NVRAM data deserialized to %@ instead of NSDictionary (data length %lu) - treating as absent"
+ "No NVRAM data present for fm-spkeys"
```
