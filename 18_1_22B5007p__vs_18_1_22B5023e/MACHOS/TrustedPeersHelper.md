## TrustedPeersHelper

> `/System/Library/Frameworks/Security.framework/XPCServices/TrustedPeersHelper.xpc/TrustedPeersHelper`

```diff

-61439.40.9.0.0
-  __TEXT.__text: 0x216154
+61439.40.30.0.1
+  __TEXT.__text: 0x216b8c
   __TEXT.__auth_stubs: 0x1e60
-  __TEXT.__objc_stubs: 0x2ae0
-  __TEXT.__objc_methlist: 0x2bec
-  __TEXT.__const: 0x9148
-  __TEXT.__cstring: 0x160c9
-  __TEXT.__objc_methname: 0x8483
-  __TEXT.__oslogstring: 0x9c15
+  __TEXT.__objc_stubs: 0x2b00
+  __TEXT.__objc_methlist: 0x2c0c
+  __TEXT.__const: 0x9150
+  __TEXT.__cstring: 0x161a9
+  __TEXT.__objc_methname: 0x84e9
+  __TEXT.__oslogstring: 0x9d62
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x3154
+  __TEXT.__constg_swiftt: 0x3174
   __TEXT.__swift5_typeref: 0x3496
-  __TEXT.__swift5_fieldmd: 0x22d4
-  __TEXT.__swift5_reflstr: 0x1d17
+  __TEXT.__swift5_fieldmd: 0x22e0
+  __TEXT.__swift5_reflstr: 0x1d37
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x360
   __TEXT.__swift5_proto: 0x808
   __TEXT.__swift5_types: 0x258
   __TEXT.__objc_classname: 0x4c5
-  __TEXT.__objc_methtype: 0x20a4
+  __TEXT.__objc_methtype: 0x20c4
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__swift5_capture: 0x32f4
-  __TEXT.__gcc_except_tab: 0x1b8
+  __TEXT.__swift5_capture: 0x335c
+  __TEXT.__gcc_except_tab: 0x1d4
   __TEXT.__swift5_protos: 0x18
   __TEXT.__dlopen_cstrs: 0x216
-  __TEXT.__unwind_info: 0x4df8
-  __TEXT.__eh_frame: 0x70f0
+  __TEXT.__unwind_info: 0x4de8
+  __TEXT.__eh_frame: 0x6f70
   __DATA_CONST.__auth_got: 0xf40
   __DATA_CONST.__got: 0x7b0
-  __DATA_CONST.__auth_ptr: 0x640
-  __DATA_CONST.__const: 0xf5a0
+  __DATA_CONST.__auth_ptr: 0x630
+  __DATA_CONST.__const: 0xf6d0
   __DATA_CONST.__cfstring: 0x20c0
   __DATA_CONST.__objc_classlist: 0x268
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x7e20
-  __DATA.__objc_selrefs: 0x1f78
+  __DATA.__objc_const: 0x7e60
+  __DATA.__objc_selrefs: 0x1f88
   __DATA.__objc_ivar: 0x2cc
-  __DATA.__objc_data: 0x2a68
-  __DATA.__data: 0x6fa8
+  __DATA.__objc_data: 0x2a88
+  __DATA.__data: 0x6fa0
   __DATA.__objc_stublist: 0x88
   __DATA.__common: 0x890
   __DATA.__bss: 0xfdf0

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7916
-  Symbols:   489
-  CStrings:  3390
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 7931
+  Symbols:   497
+  CStrings:  3404
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "Error marking machine ID list as unusable: %!{(MISSING)public}s"
+ "Marking MID list as expired"
+ "Marking MID list as expired failed for %!{(MISSING)public}s: %!{(MISSING)public}s"
+ "Marking MID list as expired for %!{(MISSING)public}s"
+ "Setting honorIDMSListChanges to NO"
+ "authKitAccountWithAltDSID returned error: %!@(MISSING)"
+ "authKitAccountWithAltDSID:error:"
+ "fetchDeviceSessionIDFromAuthKit:"
+ "machineIDsEvicted"
+ "machineIDsGhostedFromTDL"
+ "machineIDsUnknownReason"
+ "markTrustedDeviceListFetchFailed complete: %!{(MISSING)public}s"
+ "markTrustedDeviceListFetchFailed(reply:)"
+ "markTrustedDeviceListFetchFailed:reply:"
+ "midVanishedFromTDL"
+ "requestHealthCheck(requiresEscrowCheck:repair:knownFederations:flowID:deviceSessionID:reply:)"
+ "requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:knownFederations:flowID:deviceSessionID:reply:"
+ "v64@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">56"
+ "v64@0:8@16B24B28@32@40@48@?56"
+ "v64@0:8@16B24B28@32@40@48@?56"
- "authKitAccountWithAltDSID:"
- "requestHealthCheck(requiresEscrowCheck:repair:knownFederations:reply:)"
- "requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:knownFederations:reply:"
- "v48@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">40"
- "v48@0:8@16B24B28@32@?40"
- "v48@0:8@16B24B28@32@?40"

```
