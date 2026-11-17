## MigrationKit

> `/System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit`

```diff

-1446.60.1.0.0
-  __TEXT.__text: 0x78dbb8
-  __TEXT.__objc_methlist: 0x70ec
-  __TEXT.__const: 0x3d254
-  __TEXT.__oslogstring: 0x1135c
-  __TEXT.__cstring: 0x1cdb1
-  __TEXT.__gcc_except_tab: 0x16f8
+1446.60.5.0.0
+  __TEXT.__text: 0x791104
+  __TEXT.__objc_methlist: 0x7124
+  __TEXT.__const: 0x3d274
+  __TEXT.__oslogstring: 0x113fc
+  __TEXT.__cstring: 0x1cf31
+  __TEXT.__gcc_except_tab: 0x1758
   __TEXT.__constg_swiftt: 0x10418
-  __TEXT.__swift5_typeref: 0xd026
+  __TEXT.__swift5_typeref: 0xd034
   __TEXT.__swift5_builtin: 0x398
-  __TEXT.__swift5_reflstr: 0xe1b2
-  __TEXT.__swift5_fieldmd: 0xf1b0
+  __TEXT.__swift5_reflstr: 0xe212
+  __TEXT.__swift5_fieldmd: 0xf1d4
   __TEXT.__swift5_assocty: 0x2500
-  __TEXT.__swift5_proto: 0x2570
+  __TEXT.__swift5_proto: 0x2574
   __TEXT.__swift5_types: 0xe10
   __TEXT.__swift_as_entry: 0x190c
   __TEXT.__swift_as_ret: 0x1e84
   __TEXT.__swift_as_cont: 0x45d4
-  __TEXT.__swift5_capture: 0x45b0
+  __TEXT.__swift5_capture: 0x45d0
   __TEXT.__swift5_protos: 0x15c
   __TEXT.__swift5_mpenum: 0xdc
   __TEXT.__swift5_types2: 0x8
-  __TEXT.__unwind_info: 0x1f450
-  __TEXT.__eh_frame: 0x4df90
+  __TEXT.__unwind_info: 0x1f498
+  __TEXT.__eh_frame: 0x4dec8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc18
-  __DATA_CONST.__objc_classlist: 0xca0
+  __DATA_CONST.__objc_classlist: 0xca8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x2b8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4e90
+  __DATA_CONST.__objc_selrefs: 0x4ea0
   __DATA_CONST.__objc_protorefs: 0x120
-  __DATA_CONST.__objc_superrefs: 0x340
+  __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__objc_arraydata: 0x488
   __DATA_CONST.__got: 0x2458
-  __AUTH_CONST.__const: 0x1df20
+  __AUTH_CONST.__const: 0x1dfc8
   __AUTH_CONST.__cfstring: 0x57e0
-  __AUTH_CONST.__objc_const: 0x1d2d8
+  __AUTH_CONST.__objc_const: 0x1d3c0
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0xcc0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x210
-  __AUTH_CONST.__auth_got: 0x3688
-  __AUTH.__objc_data: 0x7d98
+  __AUTH_CONST.__auth_got: 0x36a0
+  __AUTH.__objc_data: 0x7de8
   __AUTH.__data: 0x18700
-  __DATA.__objc_ivar: 0x80c
-  __DATA.__data: 0xee58
+  __DATA.__objc_ivar: 0x814
+  __DATA.__data: 0xee98
   __DATA.__common: 0x1bb8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 27039
-  Symbols:   10628
-  CStrings:  4629
+  Functions: 27061
+  Symbols:   10644
+  CStrings:  4641
 
Symbols:
+ -[MKChargeLimitAssertion dealloc]
+ -[MKChargeLimitAssertion init]
+ -[MKUSBHTTPServer isUsed]
+ -[MKUSBHTTPServer setUsed:]
+ _IOPSLimitBatteryLevel
+ _IOPSLimitBatteryLevelCancel
+ _IOPSLimitBatteryLevelRegister
+ _OBJC_CLASS_$_MKChargeLimitAssertion
+ _OBJC_IVAR_$_MKAPIServer._chargeLimitAssertion
+ _OBJC_IVAR_$_MKChargeLimitAssertion._token
+ _OBJC_METACLASS_$_MKChargeLimitAssertion
+ __OBJC_$_INSTANCE_METHODS_MKChargeLimitAssertion
+ __OBJC_$_INSTANCE_VARIABLES_MKChargeLimitAssertion
+ __OBJC_CLASS_RO_$_MKChargeLimitAssertion
+ __OBJC_METACLASS_RO_$_MKChargeLimitAssertion
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 12MigrationKit9APIClientV
CStrings:
+ ", invalid argument"
+ "Deadline for each static app-mapping lookup after the first, in seconds"
+ "Deadline for the first static app-mapping lookup in a batch, which also pays the one-time AMS media-token fetch, in seconds"
+ "appMatchFirstRequestTimeoutSeconds"
+ "appMatchRequestTimeoutSeconds"
+ "cancelled charge limit"
+ "failed to cancel charge limit: 0x%x"
+ "failed to register for charge limit: 0x%x"
+ "failed to set charge limit: 0x%x"
+ "missingPlatformInfo(_:)"
+ "notRegularFile"
+ "set charge limit to %d%%"
+ "static app mapping lookup timed out after "
+ "\xf0\xf1"
- "match(for:usingBag:)"
- "\xf0\xe1"
```
