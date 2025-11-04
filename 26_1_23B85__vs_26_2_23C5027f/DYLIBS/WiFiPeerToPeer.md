## WiFiPeerToPeer

> `/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`

```diff

-835.7.0.0.0
-  __TEXT.__text: 0x21084
+835.8.0.0.0
+  __TEXT.__text: 0x215c4
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_methlist: 0x33a4
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x5467
-  __TEXT.__oslogstring: 0x85f
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x5483
+  __TEXT.__oslogstring: 0xb0e
   __TEXT.__gcc_except_tab: 0x380
   __TEXT.__unwind_info: 0x970
   __TEXT.__objc_classname: 0x779

   __DATA_CONST.__objc_superrefs: 0x130
   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__cfstring: 0x3500
+  __AUTH_CONST.__cfstring: 0x3560
   __AUTH_CONST.__objc_const: 0x5920
   __AUTH.__objc_data: 0x1b8
   __DATA.__objc_ivar: 0x42c

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59599095-9CA7-34B6-A658-A28F4927A80F
+  UUID: 2BBB8DCB-410A-35BF-A4CF-AE55AE0A5EF2
   Functions: 1036
   Symbols:   3701
-  CStrings:  2432
+  CStrings:  2448
 
Symbols:
+ ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke.151
+ ___block_literal_global.166
+ ___block_literal_global.168
+ ___block_literal_global.170
+ ___block_literal_global.172
+ ___block_literal_global.174
+ ___block_literal_global.212
+ ___block_literal_global.268
+ ___block_literal_global.364
+ ___block_literal_global.606
+ ___block_literal_global.608
+ ___block_literal_global.610
- ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke_2
- ___block_literal_global.154
- ___block_literal_global.156
- ___block_literal_global.158
- ___block_literal_global.160
- ___block_literal_global.162
- ___block_literal_global.200
- ___block_literal_global.254
- ___block_literal_global.351
- ___block_literal_global.593
- ___block_literal_global.595
- ___block_literal_global.597
Functions:
~ -[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:] : 612 -> 1532
~ ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke : 120 -> 268
~ ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke_2 -> ___82-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:]_block_invoke.151 : 188 -> 464
CStrings:
+ " (error: %@)"
+ "FAILED"
+ "SUCCESS"
+ "[AWDL Traffic] Adding new registration (total will be %lu)"
+ "[AWDL Traffic] AirPlay legacy clear path (activeFlagOverride=true)"
+ "[AWDL Traffic] Current active registrations count: %lu"
+ "[AWDL Traffic] FAILED: Unknown service '%{public}@'"
+ "[AWDL Traffic] Redirecting to AirPlay connectivity check"
+ "[AWDL Traffic] Result: %{public}@%{public}@"
+ "[AWDL Traffic] Sending XPC: enabled=%d, activeCount=%lu"
+ "[AWDL Traffic] Setting registration: service=%{public}@, peer=%{public}@, options=0x%lx (PreferInfra:%d Background:%d Alert:%d), channels=(%u,%u), flags=(active:%d legacy:%d), hasHandler:%d"
+ "[AWDL Traffic] Updating existing registration at index %lu"
+ "[AWDL Traffic] XPC success. Existing index: %lu"

```
