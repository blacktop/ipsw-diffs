## demod_helper

> `/usr/libexec/demod_helper`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-1871.60.21.0.0
-  __TEXT.__text: 0x2e370
-  __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__objc_stubs: 0x4400
-  __TEXT.__objc_methlist: 0x1bd8
-  __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x6949
-  __TEXT.__objc_classname: 0x1ec
-  __TEXT.__objc_methname: 0x4c2c
-  __TEXT.__objc_methtype: 0x5d5
+1871.60.27.0.0
+  __TEXT.__text: 0x2f730
+  __TEXT.__auth_stubs: 0x1230
+  __TEXT.__objc_stubs: 0x4540
+  __TEXT.__objc_methlist: 0x1c70
+  __TEXT.__const: 0x148
+  __TEXT.__cstring: 0x6b71
+  __TEXT.__objc_classname: 0x1fa
+  __TEXT.__objc_methname: 0x4d24
+  __TEXT.__objc_methtype: 0x60a
   __TEXT.__gcc_except_tab: 0x338
-  __TEXT.__oslogstring: 0x6475
+  __TEXT.__oslogstring: 0x6942
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__unwind_info: 0xe40
+  __TEXT.__unwind_info: 0xea8
   __DATA_CONST.__const: 0x688
-  __DATA_CONST.__cfstring: 0x52e0
-  __DATA_CONST.__objc_classlist: 0xa8
+  __DATA_CONST.__cfstring: 0x5460
+  __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x60
+  __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x320
   __DATA_CONST.__objc_arrayobj: 0x2e8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x8f0
-  __DATA_CONST.__got: 0x380
-  __DATA.__objc_const: 0x19c0
-  __DATA.__objc_selrefs: 0x1580
-  __DATA.__objc_ivar: 0xbc
-  __DATA.__objc_data: 0x690
+  __DATA_CONST.__auth_got: 0x928
+  __DATA_CONST.__got: 0x388
+  __DATA.__objc_const: 0x1a90
+  __DATA.__objc_selrefs: 0x15e0
+  __DATA.__objc_ivar: 0xc0
+  __DATA.__objc_data: 0x6e0
   __DATA.__data: 0x85c
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libsysdiagnose.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1056
-  Symbols:   400
-  CStrings:  2199
+  Functions: 1086
+  Symbols:   408
+  CStrings:  2251
 
Symbols:
+ _IOConnectCallScalarMethod
+ _IOConnectCallStructMethod
+ _IOServiceClose
+ _IOServiceMatching
+ _IOServiceOpen
+ ___memcpy_chk
+ _mach_task_self_
+ _sleep
CStrings:
+ "-[MSDHMessageResponder fallbackToQiOne:]"
+ "AppleSMC"
+ "Closing SMC connection..."
+ "EnableQi1ChargingFallback"
+ "Entering %s"
+ "Failed to close SMC connection: %{public}@"
+ "Failed to close service port to SMC; ret: %d"
+ "Failed to disable cloak requests (WAFC) with error: %{public}@"
+ "Failed to find matching io service to %s"
+ "Failed to force Qi 1 (WAFC) with error: %{public}@"
+ "Failed to open SMC connection: %{public}@"
+ "Failed to open SMC with error: %{public}@"
+ "Failed to open SMC, attempt %d/%d, retrying in %ds..."
+ "Failed to open service port to SMC; ret: %d"
+ "Failed to reset inductive firmware (WAFC) with error: %{public}@"
+ "Failed to send user client close command to SMC; ret: %d"
+ "Failed to send user client open command to SMC; ret: %d"
+ "Failed to write SMC key: %@; invalid key"
+ "Failed to write SMC key: %@; no open SMC connection"
+ "Failed to write SMC key: %{public}@; invalid key"
+ "Failed to write SMC key: %{public}@; no open SMC connection"
+ "Failed to write key: %@; data %@ exceeds maximum allowed length: %d"
+ "Failed to write key: %@; ret: 0x%X; smc ret: 0x%X"
+ "Failed to write key: %{public}@; data %{public}@ exceeds maximum allowed length: %d"
+ "Failed to write key: %{public}@; ret: 0x%X; smc ret: 0x%X"
+ "Forcing Qi 1: disabling MPP (WAFC = %{public}@)"
+ "Forcing Qi 1: disabling cloak requests (WAFC = %{public}@)"
+ "Forcing Qi 1: resetting inductive firmware (WAFC = %{public}@)"
+ "I24@0:8@16"
+ "I24@0:8^@16"
+ "MSDHSMCHelper"
+ "Opening io connection to SMC ..."
+ "Successfully closed SMC connection"
+ "Successfully opened io connection to SMC"
+ "Successfully written key %{public}@ with data: %{public}@"
+ "TI,N,V_connection"
+ "WAFC"
+ "_closeAppleSMC:"
+ "_connection"
+ "_isValidKeyString:"
+ "_openAppleSMC:"
+ "_smcKeyFromString:"
+ "canBeConvertedToEncoding:"
+ "connection"
+ "enableQi1ChargingFallback"
+ "fallbackToQiOne"
+ "fallbackToQiOne:"
+ "openAppleSMC:"
+ "setConnection:"
+ "v24@0:8^@16"
+ "v40@0:8@16@24^@32"
+ "writeSMCKey:data:error:"
```
