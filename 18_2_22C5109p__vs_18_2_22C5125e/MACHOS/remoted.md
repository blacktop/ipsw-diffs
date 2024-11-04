## remoted

> `/usr/libexec/remoted`

```diff

-170.0.0.0.0
-  __TEXT.__text: 0x3de44
+172.0.0.0.0
+  __TEXT.__text: 0x3e110
   __TEXT.__auth_stubs: 0x17f0
   __TEXT.__objc_stubs: 0x2200
   __TEXT.__objc_methlist: 0x1358
   __TEXT.__const: 0x21a
-  __TEXT.__oslogstring: 0x8096
+  __TEXT.__oslogstring: 0x81b2
   __TEXT.__cstring: 0x1ec8
   __TEXT.__objc_methname: 0x229d
   __TEXT.__objc_classname: 0x27b
   __TEXT.__objc_methtype: 0x6e6
-  __TEXT.__gcc_except_tab: 0x12b0
+  __TEXT.__gcc_except_tab: 0x12c8
   __TEXT.__unwind_info: 0xdc8
   __DATA_CONST.__auth_got: 0xc08
   __DATA_CONST.__got: 0x210

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1344
+  Functions: 1347
   Symbols:   485
-  CStrings:  1716
+  CStrings:  1720
 
CStrings:
+ "%!{(MISSING)public}@> Peer protocol version too low for TLS (%!l(MISSING)lu < %!d(MISSING))."
+ "DAK-attested public key mismatches the public key of the peer's certificate."
+ "Failed to extract ephemeral public key from attestation with aks error: 0x%!x(MISSING)"
+ "Failed to extract pubkey param from attestation with error: %!x(MISSING)"

```
