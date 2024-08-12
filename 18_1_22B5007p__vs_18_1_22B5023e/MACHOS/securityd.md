## securityd

> `/usr/libexec/securityd`

```diff

-61439.40.9.0.0
-  __TEXT.__text: 0x22eae8
+61439.40.30.0.1
+  __TEXT.__text: 0x22eb98
   __TEXT.__auth_stubs: 0x38c0
-  __TEXT.__objc_stubs: 0x1a4c0
-  __TEXT.__objc_methlist: 0x12924
-  __TEXT.__const: 0x8cd
-  __TEXT.__cstring: 0x2035e
-  __TEXT.__oslogstring: 0x28cbf
-  __TEXT.__gcc_except_tab: 0xab44
+  __TEXT.__objc_stubs: 0x1a4e0
+  __TEXT.__objc_methlist: 0x1292c
+  __TEXT.__const: 0x8d5
+  __TEXT.__cstring: 0x20346
+  __TEXT.__oslogstring: 0x28c9f
+  __TEXT.__gcc_except_tab: 0xac3c
   __TEXT.__objc_classname: 0x22ba
-  __TEXT.__objc_methname: 0x29233
-  __TEXT.__objc_methtype: 0x9865
+  __TEXT.__objc_methname: 0x29221
+  __TEXT.__objc_methtype: 0x9885
   __TEXT.__dlopen_cstrs: 0x2c4
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6240
+  __TEXT.__unwind_info: 0x6258
   __DATA_CONST.__auth_got: 0x1c70
-  __DATA_CONST.__got: 0xdd8
+  __DATA_CONST.__got: 0xdd0
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x131b8
-  __DATA_CONST.__cfstring: 0x1afa0
+  __DATA_CONST.__const: 0x131d0
+  __DATA_CONST.__cfstring: 0x1af80
   __DATA_CONST.__objc_classlist: 0x880
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x7e0
-  __DATA_CONST.__objc_intobj: 0x1320
+  __DATA_CONST.__objc_intobj: 0x1308
   __DATA_CONST.__objc_arraydata: 0x3d8
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x23628
-  __DATA.__objc_selrefs: 0x8768
-  __DATA.__objc_ivar: 0x1868
+  __DATA.__objc_const: 0x23608
+  __DATA.__objc_selrefs: 0x8778
+  __DATA.__objc_ivar: 0x1864
   __DATA.__objc_data: 0x5500
   __DATA.__data: 0x20b8
   __DATA.__thread_vars: 0xd8
   __DATA.__thread_bss: 0x1e
-  __DATA.__bss: 0xa50
+  __DATA.__bss: 0xa48
   __DATA.__common: 0x10
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9084
-  Symbols:   1374
-  CStrings:  15232
+  Functions: 9087
+  Symbols:   1373
+  CStrings:  15230
 
Symbols:
- _AKAppleIDAuthenticationErrorDomain
CStrings:
+ "-[CuttlefishXPCWrapper markTrustedDeviceListFetchFailed:reply:]_block_invoke"
+ "-[CuttlefishXPCWrapper requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:knownFederations:flowID:deviceSessionID:reply:]_block_invoke"
+ "Disabling SOS from monitor mode"
+ "Error fetching IQEs for zone %!@(MISSING): %!@(MISSING)"
+ "Error fetching out of band fetch permission, relying on forceFetch enablement (%!@(MISSING)) : %!@(MISSING)"
+ "Successfully marked machineID list as out of date"
+ "Unable to mark machineID list as out of date: %!@(MISSING)"
+ "allowOutOfBandFetch:"
+ "authKitAccountWithAltDSID returned error: %!@(MISSING)"
+ "authKitAccountWithAltDSID:error:"
+ "ckks-operation: linear dependencies exceeds %!d(MISSING) operations"
+ "currentlyEnforcingIDMSTDL:"
+ "fetchDeviceSessionIDFromAuthKit:"
+ "honorIDMSListChanges"
+ "initWithDependencies:intendedState:listUpdatesState:errorState:retryFlag:"
+ "markTrustedDeviceListFetchFailed:reply:"
+ "requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:knownFederations:flowID:deviceSessionID:reply:"
+ "v64@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@\"NSString\"40@\"NSString\"48@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">56"
+ "v64@0:8@16B24B28@32@40@48@?56"
- "-[CuttlefishXPCWrapper requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:knownFederations:reply:]_block_invoke"
- "LostAccountAuth"
- "Putting SOS into monitor mode"
- "SOSMonitorMode is not turned on for this platform"
- "SecKeychainStaticPersistentRefs"
- "SecPersistentRefCreateWithItem: Creating old persistent ref for %!l(MISSING)lu"
- "Static Persistent Refs are %!@(MISSING) (via feature flags)"
- "T@\"NSString<OctagonStateString>\",&,V_stateIfAuthenticationError"
- "Uploading %!d(MISSING) new TLKShares"
- "Uploading TLKShare to %!@(MISSING) (as %!@(MISSING))"
- "_stateIfAuthenticationError"
- "allowOutOfBandFetch"
- "attributes to query illegal; both row_id and other attributes can't be searched at the same time"
- "initWithDependencies:intendedState:listUpdatesState:authenticationErrorState:errorState:retryFlag:"
- "requestHealthCheckWithSpecificUser:requiresEscrowCheck:repair:knownFederations:reply:"
- "s3dl_query_row_digest: Creating old persistent ref for %!l(MISSING)lu"
- "setStateIfAuthenticationError:"
- "sosEvaluateIfNeeded - Turning on SOS since monitor mode is unavailable"
- "stateIfAuthenticationError"
- "v48@0:8@\"TPSpecificUser\"16B24B28@\"NSArray\"32@?<v@?@\"TrustedPeersHelperHealthCheckResult\"@\"NSError\">40"
- "v48@0:8@16B24B28@32@?40"

```
