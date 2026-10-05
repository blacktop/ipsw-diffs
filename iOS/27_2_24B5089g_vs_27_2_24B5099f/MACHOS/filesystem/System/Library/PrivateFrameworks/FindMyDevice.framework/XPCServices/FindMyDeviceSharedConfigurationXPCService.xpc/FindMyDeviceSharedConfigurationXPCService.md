## FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/FindMyDeviceSharedConfigurationXPCService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-482.31.6.16.11
-  __TEXT.__text: 0x1ae78
-  __TEXT.__auth_stubs: 0xef0
+482.31.6.16.16
+  __TEXT.__text: 0x1c04c
+  __TEXT.__auth_stubs: 0xf40
   __TEXT.__objc_stubs: 0x920
   __TEXT.__objc_methlist: 0x264
-  __TEXT.__const: 0x968
-  __TEXT.__cstring: 0x454
-  __TEXT.__swift5_typeref: 0x51c
+  __TEXT.__const: 0xaf8
+  __TEXT.__cstring: 0x4b1
+  __TEXT.__swift5_typeref: 0x58a
   __TEXT.__objc_methname: 0x9fe
-  __TEXT.__swift5_capture: 0x328
-  __TEXT.__objc_methtype: 0x2df
-  __TEXT.__oslogstring: 0x9b2
+  __TEXT.__swift5_capture: 0x358
+  __TEXT.__oslogstring: 0xa10
+  __TEXT.__objc_methtype: 0x2e5
+  __TEXT.__constg_swiftt: 0x1e0
+  __TEXT.__swift5_fieldmd: 0x1ec
   __TEXT.__objc_classname: 0x147
-  __TEXT.__constg_swiftt: 0x188
   __TEXT.__swift5_reflstr: 0x1f7
-  __TEXT.__swift5_fieldmd: 0x1bc
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_assocty: 0x90
-  __TEXT.__swift5_proto: 0x4c
-  __TEXT.__swift5_types: 0x24
-  __TEXT.__swift_as_entry: 0x20
-  __TEXT.__swift_as_ret: 0x24
-  __TEXT.__swift_as_cont: 0x5c
+  __TEXT.__swift5_proto: 0x50
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift_as_entry: 0x54
+  __TEXT.__swift_as_ret: 0x5c
+  __TEXT.__swift_as_cont: 0xac
+  __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x580
-  __TEXT.__eh_frame: 0x6d8
-  __DATA_CONST.__const: 0xa00
+  __TEXT.__unwind_info: 0x6f0
+  __TEXT.__eh_frame: 0xc80
+  __DATA_CONST.__const: 0xa28
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x780
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__auth_ptr: 0x2d8
+  __DATA_CONST.__auth_got: 0x7a8
+  __DATA_CONST.__got: 0x2e0
+  __DATA_CONST.__auth_ptr: 0x2e0
   __DATA.__objc_const: 0x6b8
   __DATA.__objc_selrefs: 0x350
   __DATA.__objc_data: 0x170
-  __DATA.__data: 0x450
+  __DATA.__data: 0x470
   __DATA.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 380
-  Symbols:   175
-  CStrings:  229
+  Functions: 424
+  Symbols:   171
+  CStrings:  232
 
Symbols:
+ _swift_arrayInitWithCopy
+ _swift_retain_x22
- _objc_retain_x27
- _os_unfair_lock_lock
- _os_unfair_lock_unlock
- _swift_retain_x23
- _swift_retain_x24
- _swift_retain_x26
CStrings:
+ "getTheftAndLossCoverage(serialNumber:)"
+ "getTheftAndLossCoverage(udid:)"
+ "rdar://187622475 fix build: accepted XPC connection from pid %d"
+ "rdar://187622475: FindMyBase absent -> plain Task fallback"
+ "rdar://187622475: FindMyBase present -> Transaction.asyncTask"
+ "rdar://187622475: getTheftAndLossCoverage(serialNumber:) body entered"
- "Failed to get device coverage for serialNumber: %s"
- "Failed to get device coverage for serialNumber: %s, error: %@"
- "Found device coverage: %{bool}d, for serialNumber: %s"
```
