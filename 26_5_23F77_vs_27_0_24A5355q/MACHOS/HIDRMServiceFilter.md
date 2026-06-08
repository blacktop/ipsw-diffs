## HIDRMServiceFilter

> `/System/Library/HIDPlugins/ServiceFilters/HIDRMServiceFilter.plugin/HIDRMServiceFilter`

```diff

-43.120.2.0.0
-  __TEXT.__text: 0x60e4
-  __TEXT.__auth_stubs: 0x770
+47.0.0.0.0
+  __TEXT.__text: 0x5488
+  __TEXT.__auth_stubs: 0x860
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x2ac
-  __TEXT.__const: 0x1d2
-  __TEXT.__cstring: 0x1ba
-  __TEXT.__swift5_typeref: 0xed
+  __TEXT.__const: 0x1b2
+  __TEXT.__cstring: 0x3c7
+  __TEXT.__swift5_typeref: 0xee
   __TEXT.__objc_methname: 0x572
-  __TEXT.__oslogstring: 0x3a3
+  __TEXT.__oslogstring: 0x102
   __TEXT.__swift5_capture: 0x58
   __TEXT.__objc_methtype: 0x358
   __TEXT.__objc_classname: 0x40
-  __TEXT.__constg_swiftt: 0x1f0
+  __TEXT.__constg_swiftt: 0x220
   __TEXT.__swift5_reflstr: 0x7f
   __TEXT.__swift5_fieldmd: 0xa4
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x178
-  __DATA_CONST.__auth_got: 0x3c0
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__auth_ptr: 0xb8
+  __TEXT.__unwind_info: 0x190
   __DATA_CONST.__const: 0x228
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__auth_got: 0x438
+  __DATA_CONST.__got: 0x148
+  __DATA_CONST.__auth_ptr: 0xb8
   __DATA.__objc_const: 0x358
   __DATA.__objc_selrefs: 0x178
-  __DATA.__objc_data: 0x290
-  __DATA.__data: 0x200
+  __DATA.__objc_data: 0x2c0
+  __DATA.__data: 0x210
   __DATA.__common: 0x28
   __DATA.__bss: 0x220
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6CE90205-BA2C-34D5-A00A-C39DE5B6E027
-  Functions: 103
-  Symbols:   95
-  CStrings:  139
+  UUID: 93D5B1D7-23BE-3131-82AC-5CE0DF59E890
+  Functions: 111
+  Symbols:   106
+  CStrings:  141
 
Symbols:
+ _objc_retain_x22
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x24
+ _swift_retain_x25
- _objc_release_x26
- _objc_release_x28
- _objc_retain_x24
- _swift_retain
CStrings:
+ " and is keyboard down: "
+ " event for accessibility support"
+ "%s: %s"
+ ", allowing pass-through"
+ "Approving device"
+ "Created HIDRMDevice"
+ "Failed to setProperty:"
+ "Forgetting device"
+ "Ignoring SlowKeys phase "
+ "New event with event type: "
+ "Registering with system"
+ "Revoking device approval"
+ "Safe user input event with type: "
+ "Service is null, skipping registration"
- "Approving device: %llx"
- "Failed to setProperty:%s forKey:%s"
- "Forgetting device %llx"
- "HIDRM Device: %llx Filter State: %s -> %s"
- "HIDRM Device: %llx State: %s -> %s"
- "Ignoring SlowKeys phase %ld event for accessibility support"
- "New event with event type: %u and is keyboard down: %{bool}d"
- "Registering %llx for device: %llx with system"
- "Revoking device approval for %llx"
- "Safe user input event with type: %u, allowing pass-through"
- "Service %llx for device: %llx is null, skipping registration"
- "setProperty:%s forKey:%s"

```
