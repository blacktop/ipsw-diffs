## com.apple.dt.instruments.dtsecurity

> `/System/Library/PrivateFrameworks/DVTInstrumentsFoundation.framework/XPCServices/com.apple.dt.instruments.dtsecurity.xpc/com.apple.dt.instruments.dtsecurity`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-64578.160.1.0.0
-  __TEXT.__text: 0x115d8
-  __TEXT.__auth_stubs: 0x16d0
-  __TEXT.__objc_stubs: 0x12c0
+64578.209.1.0.0
+  __TEXT.__text: 0x11b58
+  __TEXT.__auth_stubs: 0x1740
+  __TEXT.__objc_stubs: 0x1300
   __TEXT.__objc_methlist: 0x5c0
   __TEXT.__const: 0x492
-  __TEXT.__oslogstring: 0x12cc
-  __TEXT.__cstring: 0x1216
+  __TEXT.__oslogstring: 0x136c
+  __TEXT.__cstring: 0x1326
   __TEXT.__objc_classname: 0x15f
   __TEXT.__objc_methtype: 0x2c1
   __TEXT.__gcc_except_tab: 0x3c0
-  __TEXT.__objc_methname: 0x13c5
+  __TEXT.__objc_methname: 0x1415
   __TEXT.__constg_swiftt: 0x140
   __TEXT.__swift5_typeref: 0xa0
   __TEXT.__swift5_reflstr: 0x2c4

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x638
+  __TEXT.__unwind_info: 0x648
   __TEXT.__eh_frame: 0x160
   __DATA_CONST.__const: 0xec0
-  __DATA_CONST.__cfstring: 0xa40
+  __DATA_CONST.__cfstring: 0xb20
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x198
   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0xb80
-  __DATA_CONST.__got: 0x1d0
+  __DATA_CONST.__auth_got: 0xbb8
+  __DATA_CONST.__got: 0x1d8
   __DATA_CONST.__auth_ptr: 0xd8
   __DATA.__objc_const: 0xec0
-  __DATA.__objc_selrefs: 0x5a8
+  __DATA.__objc_selrefs: 0x5b8
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x508
   __DATA.__data: 0x280

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 394
-  Symbols:   456
-  CStrings:  589
+  Functions: 398
+  Symbols:   465
+  CStrings:  600
 
Symbols:
+ _CFBooleanGetTypeID
+ _CFBooleanGetValue
+ _CFGetTypeID
+ _DVTAuditedCodeValidlyHoldsEntitlement
+ _OBJC_CLASS_$_NSCharacterSet
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _os_variant_allows_internal_security_policies
+ _xpc_connection_get_audit_token
CStrings:
+ "\"\\"
+ "DVTEntitlementCheck"
+ "Denying connection from process (%d : %p) because it does not validly hold the entitlement: %{public}s"
+ "characterSetWithCharactersInString:"
+ "invalid entitlement name: contains a quote or backslash"
+ "rangeOfCharacterFromSet:"
+ "the audited process does not hold %@"
+ "the audited process holds %@ but is neither a platform binary nor debuggable (%#x)"
+ "the entitlement name was missing or malformed"
+ "unable to inspect the audited process"
+ "unable to read the audited process' code signing status"
```
