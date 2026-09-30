## SPOwner

> `/System/Library/PrivateFrameworks/SPOwner.framework/SPOwner`

```diff

-449.30.6.14.26
-  __TEXT.__text: 0x74ec0
+449.31.6.16.16
+  __TEXT.__text: 0x750ac
   __TEXT.__objc_methlist: 0xbc0c
   __TEXT.__const: 0x5b8
   __TEXT.__gcc_except_tab: 0x15a0
   __TEXT.__cstring: 0x6ac9
-  __TEXT.__oslogstring: 0x7fa8
+  __TEXT.__oslogstring: 0x8078
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__constg_swiftt: 0x148
   __TEXT.__swift5_typeref: 0x133

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x8
-  __TEXT.__unwind_info: 0x3018
+  __TEXT.__unwind_info: 0x3020
   __TEXT.__eh_frame: 0x330
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4411
-  Symbols:   8759
-  CStrings:  1577
+  Functions: 4414
+  Symbols:   8760
+  CStrings:  1580
 
Symbols:
+ -[SPBeaconManager submitDeviceEvent:source:timestamp:attachedTo:completion:]
+ _OUTLINED_FUNCTION_4
+ ___76-[SPBeaconManager submitDeviceEvent:source:timestamp:attachedTo:completion:]_block_invoke
+ ___block_descriptor_76_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ _objc_msgSend$submitDeviceEvent:source:timestamp:attachedTo:completion:
- -[SPBeaconManager submitDeviceEvent:source:attachedTo:completion:]
- ___66-[SPBeaconManager submitDeviceEvent:source:attachedTo:completion:]_block_invoke
- ___block_descriptor_68_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- _objc_msgSend$submitDeviceEvent:source:attachedTo:completion:
CStrings:
+ "NVRAM data (length %lu) failed to deserialize as a property list: %@"
+ "NVRAM data deserialized to %@ instead of NSDictionary (data length %lu) - treating as absent"
+ "No NVRAM data present for fm-spkeys"
```
