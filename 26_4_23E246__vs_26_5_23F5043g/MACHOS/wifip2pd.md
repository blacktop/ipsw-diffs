## wifip2pd

> `/usr/libexec/wifip2pd`

```diff

-855.33.0.0.0
-  __TEXT.__text: 0x4dd4cc
+860.5.0.0.0
+  __TEXT.__text: 0x4e3c20
   __TEXT.__auth_stubs: 0x49b0
   __TEXT.__objc_stubs: 0x3b00
   __TEXT.__objc_methlist: 0x177c
-  __TEXT.__const: 0x38f98
-  __TEXT.__swift5_typeref: 0xb3fe
+  __TEXT.__const: 0x38fe8
+  __TEXT.__swift5_typeref: 0xb428
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0xa7aa
-  __TEXT.__oslogstring: 0x16c7c
-  __TEXT.__constg_swiftt: 0xe080
+  __TEXT.__cstring: 0xad49
+  __TEXT.__oslogstring: 0x170fc
+  __TEXT.__constg_swiftt: 0xe098
   __TEXT.__swift5_fieldmd: 0x14640
-  __TEXT.__swift5_types: 0x10b0
+  __TEXT.__swift5_types: 0x10b4
   __TEXT.__swift5_reflstr: 0x126f6
   __TEXT.__swift5_builtin: 0x1590
   __TEXT.__swift5_assocty: 0x2958

   __TEXT.__objc_classname: 0xd39
   __TEXT.__objc_methtype: 0x1bc7
   __TEXT.__objc_methname: 0x8785
-  __TEXT.__swift5_capture: 0x4bf4
+  __TEXT.__swift5_capture: 0x4ec8
   __TEXT.__swift5_mpenum: 0x16c
   __TEXT.__swift_as_entry: 0xfc
   __TEXT.__swift_as_ret: 0x98
-  __TEXT.__unwind_info: 0xdbf0
-  __TEXT.__eh_frame: 0x17ea8
+  __TEXT.__unwind_info: 0xdc48
+  __TEXT.__eh_frame: 0x17fb0
   __DATA_CONST.__auth_got: 0x24e0
   __DATA_CONST.__got: 0xf00
   __DATA_CONST.__auth_ptr: 0x1e30
-  __DATA_CONST.__const: 0x2ef28
+  __DATA_CONST.__const: 0x2f578
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x270

   __DATA.__objc_const: 0x8b68
   __DATA.__objc_selrefs: 0x12e8
   __DATA.__objc_data: 0x1390
-  __DATA.__data: 0x11390
+  __DATA.__data: 0x113b0
   __DATA.__common: 0x8e8
   __DATA.__bss: 0x54140
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 43489080-1987-3D9F-8AE7-CCE1C18F44BD
-  Functions: 21131
+  UUID: 34C1EB06-A3C5-318D-99DC-772B82E9C9C1
+  Functions: 21201
   Symbols:   2140
-  CStrings:  4256
+  CStrings:  4299
 
CStrings:
+ " for authentication response"
+ "%@ cancel"
+ "%@ datapath request from peer device: version=%s, platform=%s, flags=%s (0x%s)"
+ "%@ discovery result from peer device: version=%s, platform=%s, flags=%s (0x%s)"
+ "%@: no data path retries when pairing is enabled"
+ "%s: Authentication response transmission failed. Aborting"
+ "%s: Deinit"
+ "%s: Indicating pairing failure"
+ "%s: authentication response sent"
+ "%s: bootstrap request transmission completed with status: %{bool}d"
+ "%s: bootstrap request transmission failed!"
+ "%s: bootstrap request transmission succeeded!"
+ "%s: bootstrap response transmission completed with status: %{bool}d"
+ "%s: bootstrap response transmission failed!"
+ "%s: bootstrap response transmission succeeded!"
+ "%s: bootstrap retry request transmission completed with status: %{bool}d"
+ "%s: bootstrap retry request transmission failed!"
+ "%s: bootstrap retry request transmission succeeded!"
+ "%s: failed because: %s: %s"
+ "/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd"
+ "Authentication rejection received"
+ "Authentication request but no pairing session found"
+ "Authentication response transmission failed. Aborting"
+ "Bootstrap request transmission failed"
+ "Bootstrap response handling failed"
+ "Bootstrap response status: comeback value is invalid"
+ "Bootstrap response status: none"
+ "Bootstrap response status: rejected"
+ "Bootstrap response transmission failed"
+ "Bootstrap retry request transmission failed"
+ "Cannot create new datapath for %@ to %s[%hhu] because NAN capabilities do not contain a pairing cipher suite %s"
+ "Cannot create new datapath for %@ to %s[%hhu] because connection mode is %s but no security parameters were provided"
+ "Cannot create new datapath for %@ to %s[%hhu] because failed to initialize the NAN Pairing Initiator Instance"
+ "DatapathInitiator created for %s: active=%{bool}d"
+ "Discovery result: peer=%@ publishID=%hhu rssi=%ld pairSetupRequired=%{bool}d pairedUUID=%s"
+ "Error sending follow-up frame"
+ "Error sending follow-up frame, in invalid state: "
+ "Error sending the authentication confirmation"
+ "Failed to handle authentication frame"
+ "Failed to handle bootstrap response"
+ "Failed to handle bootstrap response advertised method is not valid, method: response: "
+ "Failed to handle bootstrap response not in requested state"
+ "Failed to send authentication confirmation because "
+ "Invalid Password"
+ "Invalid password"
+ "NAN Init - POST merge customAttributes: %s"
+ "NAN Init - PRE merge customAttributes: %s"
+ "NAN Init - merging attributes: %s"
+ "No DFS Proxy Support"
+ "No KDEs found in pairing caching follow-up frame"
+ "No NAN interface found. Creating NAN interface"
+ "Pairing caching follow-up transmission failed!"
+ "Pairing responder timed out could not pair for "
+ "Providing PTR record for %s — SRV cached in peer, resolve ready"
+ "Received NIK is all zeros"
+ "Received: pairing caching follow up but not authenticated confirmation generated state!"
+ "Received: pairing caching follow up but not authenticated state!"
+ "Received: pairing caching follow up with no shared key descriptor!"
+ "WiFiP2P-860.5 Mar 20 2026 22:03:43"
+ "[%s] Cached SRV for %s: %s:%hu (resolve ready)"
+ "[%s] MI payload overflow (SUI updated): service TLVs may be truncated — received=[%s], droppedFromCache=[%s]"
+ "[%s] No SRV for %s: skipping cache (overflow=%{bool}d, hadPrevCachedSRV=%{bool}d)"
+ "nira: [%s]: no matching nira found in key store - tag=%s nonce=%s"
+ "nira: [%s]: no nira found in NAN peer"
+ "nira: [%s]: no paired peers stored in the key store"
+ "nira: [%s]: tag=%s nonce=%s"
- "%@ datapath request from peer device: version=%s, platform=%s, flags=0x%s"
- "%@ discovery result from peer device: version=%s, platform=%s, flags=0x%s"
- "%s: Invalid password"
- "%s: No KDEs found in pairing caching follow-up frame"
- "%s: bootstrap response handling failed: %@"
- "%s: bootstrap response status: none"
- "%s: error sending follow-up frame"
- "%s: error sending the authentication confirmation"
- "%s: error sending the follow-up frame"
- "%s: failed because %s"
- "%s: failed to handle bootstrap response"
- "%s: failed to handle bootstrap response advertised method is not valid, method: response: %hu"
- "%s: failed to handle bootstrap response not in requested state"
- "%s: failed to send authentication confirmation because %@"
- "%s: received: pairing caching follow up but not authenticated confirmation generated state!"
- "%s: received: pairing caching follow up but not authenticated state!"
- "%s: received: pairing caching follow up with no shared key descriptor!"
- "Providing PTR record for %s"
- "WiFiP2P-855.33 Mar 06 2026 18:03:47"
- "authentication failed"
- "authentication rejection received"
- "authentication request but no pairing session found"
- "failed to handle authentication frame"

```
