## FindMyDeviceSharedConfigurationXPCService

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/XPCServices/FindMyDeviceSharedConfigurationXPCService.xpc/Contents/MacOS/FindMyDeviceSharedConfigurationXPCService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-482.20.6.14.14
-  __TEXT.__text: 0x13d14
-  __TEXT.__auth_stubs: 0xbe0
+482.21.6.16.21
+  __TEXT.__text: 0x16a38
+  __TEXT.__auth_stubs: 0xc90
   __TEXT.__objc_stubs: 0x840
   __TEXT.__objc_methlist: 0x234
-  __TEXT.__const: 0x938
-  __TEXT.__cstring: 0x3e4
-  __TEXT.__swift5_typeref: 0x431
+  __TEXT.__const: 0xaa8
+  __TEXT.__cstring: 0x441
+  __TEXT.__swift5_typeref: 0x4e3
   __TEXT.__objc_methname: 0x91a
-  __TEXT.__swift5_capture: 0x238
-  __TEXT.__objc_methtype: 0x274
-  __TEXT.__oslogstring: 0x702
+  __TEXT.__swift5_capture: 0x2d0
+  __TEXT.__oslogstring: 0x7f0
+  __TEXT.__objc_methtype: 0x27a
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
-  __TEXT.__swift_as_entry: 0x1c
-  __TEXT.__swift_as_ret: 0x20
-  __TEXT.__swift_as_cont: 0x50
+  __TEXT.__swift5_proto: 0x50
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift_as_entry: 0x50
+  __TEXT.__swift_as_ret: 0x54
+  __TEXT.__swift_as_cont: 0x9c
+  __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x4f0
-  __TEXT.__eh_frame: 0x600
-  __DATA_CONST.__const: 0x7c0
+  __TEXT.__unwind_info: 0x668
+  __TEXT.__eh_frame: 0xb40
+  __DATA_CONST.__const: 0x928
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__auth_ptr: 0x2c8
+  __DATA_CONST.__auth_got: 0x650
+  __DATA_CONST.__got: 0x2c0
+  __DATA_CONST.__auth_ptr: 0x2d8
   __DATA.__objc_const: 0x668
   __DATA.__objc_selrefs: 0x308
   __DATA.__objc_data: 0x170
-  __DATA.__data: 0x438
+  __DATA.__data: 0x468
   __DATA.__common: 0x28
-  __DATA.__bss: 0xa20
+  __DATA.__bss: 0xa40
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 328
+  Functions: 389
   Symbols:   129
-  CStrings:  199
+  CStrings:  205
 
CStrings:
+ "Complete device (serialNumber: %s) coverage check failed: %@"
+ "Complete device coverage timed out"
+ "Could not read from other devices."
+ "Final error verifying coverage: %@."
+ "getTheftAndLossCoverage(serialNumber:)"
+ "getTheftAndLossCoverage(udid:)"
+ "rdar://187622475 fix build: accepted XPC connection from pid %d"
+ "rdar://187622475: FindMyBase absent -> plain Task fallback"
+ "rdar://187622475: FindMyBase present -> Transaction.asyncTask"
+ "rdar://187622475: getTheftAndLossCoverage(serialNumber:) body entered"
- "Could not read from other devices, returning %{bool}d."
- "Failed to get device coverage for serialNumber: %s"
- "Failed to get device coverage for serialNumber: %s, error: %@"
- "Found device coverage: %{bool}d, for serialNumber: %s"
```
