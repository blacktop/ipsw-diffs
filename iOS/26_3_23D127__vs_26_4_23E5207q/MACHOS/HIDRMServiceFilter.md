## HIDRMServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/HIDRMServiceFilter.plugin/HIDRMServiceFilter`

```diff

-21.0.0.0.0
-  __TEXT.__text: 0x4e94
-  __TEXT.__auth_stubs: 0x740
+43.0.0.0.0
+  __TEXT.__text: 0x5d34
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x2ac
-  __TEXT.__const: 0x1d2
-  __TEXT.__cstring: 0x29e
-  __TEXT.__swift5_typeref: 0xed
-  __TEXT.__objc_methname: 0x344
-  __TEXT.__oslogstring: 0x223
+  __TEXT.__const: 0x12a
+  __TEXT.__cstring: 0x1ad
+  __TEXT.__swift5_typeref: 0xdf
+  __TEXT.__objc_methname: 0x572
+  __TEXT.__oslogstring: 0x3a3
   __TEXT.__swift5_capture: 0x58
-  __TEXT.__constg_swiftt: 0x1e0
-  __TEXT.__swift5_reflstr: 0x7f
-  __TEXT.__swift5_fieldmd: 0xa4
-  __TEXT.__swift5_proto: 0x10
-  __TEXT.__swift5_types: 0x8
-  __TEXT.__objc_classname: 0x2d
-  __TEXT.__objc_methtype: 0x316
-  __TEXT.__unwind_info: 0x170
+  __TEXT.__objc_methtype: 0x358
+  __TEXT.__objc_classname: 0x40
+  __TEXT.__constg_swiftt: 0x1d4
+  __TEXT.__swift5_reflstr: 0x70
+  __TEXT.__swift5_fieldmd: 0x88
+  __TEXT.__swift5_proto: 0x4
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x168
   __DATA_CONST.__auth_got: 0x3a0
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__auth_ptr: 0xb8
-  __DATA_CONST.__const: 0x228
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_ptr: 0x68
+  __DATA_CONST.__const: 0x198
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA.__objc_const: 0x358
-  __DATA.__objc_selrefs: 0x170
-  __DATA.__objc_data: 0x280
-  __DATA.__data: 0x210
-  __DATA.__bss: 0x220
+  __DATA.__objc_selrefs: 0x178
+  __DATA.__objc_data: 0x290
+  __DATA.__data: 0x1f0
   __DATA.__common: 0x28
+  __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
-  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /System/Library/PrivateFrameworks/HID.framework/HID
   - /System/Library/PrivateFrameworks/HIDRMKit.framework/HIDRMKit
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E349B8E6-2FCC-38AA-9805-D3ED693C8324
-  Functions: 102
+  UUID: 77054F0B-3478-3384-96FB-93A7334FA79F
+  Functions: 90
   Symbols:   94
-  CStrings:  140
+  CStrings:  138
 
Symbols:
+ _IOObjectConformsTo
+ _objc_release_x28
+ _objc_retain_x26
- _objc_release_x27
- _swift_deallocPartialClassInstance
- _swift_isaMask
CStrings:
+ "Cannot activate: device is nil"
+ "Cannot setProperty: device is nil"
+ "Conditionally safe device activated, can be registered by default"
+ "Forgetting device %llx"
+ "HIDRMDeviceForget"
+ "HIDRMDeviceNotAKeyboard"
+ "HIDRMServiceFilter"
+ "Ignoring SlowKeys phase %ld event for accessibility support"
+ "Safe user input event with type: %u, allowing pass-through"
+ "Service %llx for device: %llx is null, skipping registration"
+ "isUserInput"
- "hidrmsupport"

```
