## proximitycontrold

> `/usr/libexec/proximitycontrold`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

 376.1.2.0.0
-  __TEXT.__text: 0x260cdc
+  __TEXT.__text: 0x261cfc
   __TEXT.__auth_stubs: 0x3580
-  __TEXT.__objc_stubs: 0x41a0
+  __TEXT.__objc_stubs: 0x4280
   __TEXT.__objc_methlist: 0x29c0
-  __TEXT.__const: 0x21168
-  __TEXT.__objc_methname: 0xde49
-  __TEXT.__objc_classname: 0x23c7
-  __TEXT.__cstring: 0x7d19
-  __TEXT.__objc_methtype: 0x36db
-  __TEXT.__swift5_typeref: 0xf184
-  __TEXT.__constg_swiftt: 0xd6b0
-  __TEXT.__swift5_reflstr: 0x9943
-  __TEXT.__swift5_fieldmd: 0x92cc
+  __TEXT.__const: 0x211d8
+  __TEXT.__objc_methname: 0xdf59
+  __TEXT.__objc_classname: 0x2427
+  __TEXT.__cstring: 0x7d99
+  __TEXT.__objc_methtype: 0x36fb
+  __TEXT.__swift5_typeref: 0xf1e4
+  __TEXT.__constg_swiftt: 0xd6f4
+  __TEXT.__swift5_reflstr: 0x99a3
+  __TEXT.__swift5_fieldmd: 0x9318
   __TEXT.__swift5_builtin: 0x58c
   __TEXT.__swift5_assocty: 0xe70
-  __TEXT.__swift5_capture: 0x345c
-  __TEXT.__oslogstring: 0x7c0e
+  __TEXT.__swift5_capture: 0x3494
+  __TEXT.__oslogstring: 0x7d4e
   __TEXT.__swift5_proto: 0x1790
-  __TEXT.__swift5_types: 0x8b0
+  __TEXT.__swift5_types: 0x8b4
   __TEXT.__swift_as_entry: 0xf4
   __TEXT.__swift_as_ret: 0xe4
   __TEXT.__swift_as_cont: 0x1cc
   __TEXT.__swift5_protos: 0x144
   __TEXT.__swift5_mpenum: 0x124
-  __TEXT.__unwind_info: 0x6b90
+  __TEXT.__unwind_info: 0x6bb8
   __TEXT.__eh_frame: 0x66cc
-  __DATA_CONST.__const: 0x153e8
+  __DATA_CONST.__const: 0x154b0
   __DATA_CONST.__cfstring: 0x420
-  __DATA_CONST.__objc_classlist: 0x470
+  __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__auth_got: 0x1ac8
-  __DATA_CONST.__got: 0xea0
+  __DATA_CONST.__got: 0xea8
   __DATA_CONST.__auth_ptr: 0x1a58
-  __DATA.__objc_const: 0x187f8
-  __DATA.__objc_selrefs: 0x1d98
+  __DATA.__objc_const: 0x18930
+  __DATA.__objc_selrefs: 0x1dd0
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x38f0
-  __DATA.__data: 0x179c8
+  __DATA.__data: 0x17a88
   __DATA.__common: 0x888
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10273
-  Symbols:   1632
-  CStrings:  4156
+  Functions: 10290
+  Symbols:   1633
+  CStrings:  4175
 
Symbols:
+ _OBJC_CLASS_$_CMDeviceStateManager
CStrings:
+ "[DeviceState] ### Unable to create CMDeviceStateManager; DeviceState source unavailable"
+ "[DeviceState] ### Update error: %{public}s"
+ "[DeviceState] %{public}s: propertyB=%{public}ld -> isDeviceStateSupported=%{bool,public}d"
+ "[DeviceState] Starting; CMDeviceStateManager.isAvailable=%{bool,public}d"
+ "_TtC17proximitycontroldP33_6EE8370B87DB0A53F8CEB2E558CDC55E19DeviceStateObserver"
+ "com.apple.ProximityControl.FrontBoardMonitor"
+ "com.apple.ProximityControl.FrontBoardMonitor.DeviceStateObserver"
+ "deliveryQueue"
+ "deviceStateObserver"
+ "didReceiveInitialEvent"
+ "initWithName:"
+ "isAvailable"
+ "onUpdate"
+ "propertyB"
+ "setMaxConcurrentOperationCount:"
+ "setName:"
+ "startUpdatesToQueue:withHandler:"
+ "stopUpdates"
+ "v24@?0@\"CMDeviceStateEvent\"8@\"NSError\"16"
```
