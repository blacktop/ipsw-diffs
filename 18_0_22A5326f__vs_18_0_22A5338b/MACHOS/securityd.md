## securityd

> `/usr/libexec/securityd`

```diff

-61439.0.130.502.1
-  __TEXT.__text: 0x22e488
+61439.0.138.0.1
+  __TEXT.__text: 0x22eb98
   __TEXT.__auth_stubs: 0x38c0
-  __TEXT.__objc_stubs: 0x1a4c0
-  __TEXT.__objc_methlist: 0x1291c
+  __TEXT.__objc_stubs: 0x1a4e0
+  __TEXT.__objc_methlist: 0x1292c
   __TEXT.__const: 0x8d5
-  __TEXT.__cstring: 0x2032f
-  __TEXT.__oslogstring: 0x28bf6
-  __TEXT.__gcc_except_tab: 0xac20
+  __TEXT.__cstring: 0x20346
+  __TEXT.__oslogstring: 0x28c9f
+  __TEXT.__gcc_except_tab: 0xac3c
   __TEXT.__objc_classname: 0x22ba
-  __TEXT.__objc_methname: 0x291c7
-  __TEXT.__objc_methtype: 0x9865
+  __TEXT.__objc_methname: 0x29221
+  __TEXT.__objc_methtype: 0x9885
   __TEXT.__dlopen_cstrs: 0x2c4
   __TEXT.__ustring: 0x28
   __TEXT.__unwind_info: 0x6258

   __DATA_CONST.__objc_arraydata: 0x3d8
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x23618
-  __DATA.__objc_selrefs: 0x8768
+  __DATA.__objc_const: 0x23608
+  __DATA.__objc_selrefs: 0x8778
   __DATA.__objc_ivar: 0x1864
   __DATA.__objc_data: 0x5500
   __DATA.__data: 0x20b8

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9086
+  Functions: 9087
   Symbols:   1373
-  CStrings:  15225
+  CStrings:  15230
 
CStrings:
+ "-[CuttlefishXPCWrapper requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:knownFederations:flowID:deviceSessionID:reply:]_block_invoke"
+ "Error fetching IQEs for zone %!@(MISSING): %!@(MISSING)"
+ "Error fetching out of band fetch permission, relying on forceFetch enablement (%!@(MISSING)) : %!@(MISSING)"
+ "allowOutOfBandFetch:"
+ "authKitAccountWithAltDSID returned error: %!@(MISSING)"
+ "authKitAccountWithAltDSID:error:"
+ "fetchDeviceSessionIDFromAuthKit:"
+ "requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:knownFederations:flowID:deviceSessionID:reply:"
+ "v64@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">56"
+ "v64@0:8@16B24B28@32@40@48@?56"
- "-[CuttlefishXPCWrapper requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:knownFederations:reply:]_block_invoke"
- "allowOutOfBandFetch"
- "requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:knownFederations:reply:"
- "v48@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">40"
- "v48@0:8@16B24B28@32@?40"

```
