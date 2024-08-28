## PairedDeviceRegistry

> `/System/Library/PrivateFrameworks/PairedDeviceRegistry.framework/PairedDeviceRegistry`

```diff

-985.0.0.0.0
-  __TEXT.__text: 0x18230
+988.0.0.0.0
+  __TEXT.__text: 0x182bc
   __TEXT.__auth_stubs: 0xdc0
   __TEXT.__objc_methlist: 0xb10
   __TEXT.__const: 0x760
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__cstring: 0x1beb
-  __TEXT.__oslogstring: 0x5d4
+  __TEXT.__cstring: 0x1b8b
+  __TEXT.__oslogstring: 0x624
   __TEXT.__constg_swiftt: 0x724
   __TEXT.__swift5_typeref: 0x508
   __TEXT.__swift5_builtin: 0x50

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x48
-  __TEXT.__swift5_capture: 0x1f4
+  __TEXT.__swift5_capture: 0x1f8
   __TEXT.__unwind_info: 0x670
   __TEXT.__eh_frame: 0xf8
   __TEXT.__objc_classname: 0x162

   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x2b0
   __AUTH_CONST.__auth_got: 0x6f0
-  __AUTH_CONST.__auth_ptr: 0x1b0
+  __AUTH_CONST.__auth_ptr: 0x1a8
   __AUTH_CONST.__const: 0xa68
   __AUTH_CONST.__cfstring: 0x1320
   __AUTH_CONST.__objc_const: 0x1d70

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 662
+  Functions: 663
   Symbols:   1138
-  CStrings:  749
+  CStrings:  747
 
CStrings:
+ "Process is not entitled to access PairedDeviceRegistry - You MUST add the YES boolean entitlement 'com.apple.nano.nanoregistry.generalaccess'. This will be a fatal error."
+ "definitelyFetchRegistryState(oldToken:)"
- "definitelyFetchRegistryState()"
- "Process is missing entitlement necessary to access NanoRegistry"
- "Process is not entitled to access PairedDeviceRegistry - This process is about to crash"
- "PairedDeviceRegistry/RegistryCrux.swift"

```
