## securityd

> `/usr/libexec/securityd`

```diff

-61439.140.12.701.1
-  __TEXT.__text: 0x2345f0
+61439.140.12.704.2
+  __TEXT.__text: 0x235274
   __TEXT.__auth_stubs: 0x39b0
-  __TEXT.__objc_stubs: 0x1ae40
-  __TEXT.__objc_methlist: 0x146dc
+  __TEXT.__objc_stubs: 0x1aea0
+  __TEXT.__objc_methlist: 0x14728
   __TEXT.__const: 0x3e5
-  __TEXT.__cstring: 0x1f95a
-  __TEXT.__oslogstring: 0x29729
+  __TEXT.__cstring: 0x1fa0c
+  __TEXT.__oslogstring: 0x2994f
   __TEXT.__dlopen_cstrs: 0x1c8
-  __TEXT.__gcc_except_tab: 0xad08
+  __TEXT.__gcc_except_tab: 0xad8c
   __TEXT.__objc_classname: 0x2289
-  __TEXT.__objc_methname: 0x2a17e
-  __TEXT.__objc_methtype: 0x9d86
+  __TEXT.__objc_methname: 0x2a2ae
+  __TEXT.__objc_methtype: 0x9db0
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6090
+  __TEXT.__unwind_info: 0x60b0
   __DATA_CONST.__auth_got: 0x1ce8
   __DATA_CONST.__got: 0x1080
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x137b0
-  __DATA_CONST.__cfstring: 0x1a8c0
+  __DATA_CONST.__const: 0x137f0
+  __DATA_CONST.__cfstring: 0x1a900
   __DATA_CONST.__objc_classlist: 0x870
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x210

   __DATA_CONST.__objc_arraydata: 0x3f8
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x21908
-  __DATA.__objc_selrefs: 0x8bf0
-  __DATA.__objc_ivar: 0x1954
+  __DATA.__objc_const: 0x21950
+  __DATA.__objc_selrefs: 0x8c18
+  __DATA.__objc_ivar: 0x1958
   __DATA.__objc_data: 0x5460
   __DATA.__data: 0x1ee8
   __DATA.__thread_vars: 0xc0

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E37D0D88-9D6A-32D0-8E9D-2A213439FEE4
-  Functions: 9139
+  UUID: 901417AD-C55A-3259-A00D-D35CBA30F533
+  Functions: 9147
   Symbols:   1476
-  CStrings:  18730
+  CStrings:  18751
 
CStrings:
+ "-[CuttlefishXPCWrapper performPeerSecretsFixUpsWithSpecificUser:reply:]_block_invoke"
+ "Continuing despite fixup error: %@"
+ "Device is locked during fixup (errSecInteractionNotAllowed: %@), waiting for unlock"
+ "Device is locked during fixup, waiting for unlock"
+ "Successfully performed peer secrets accessibility fixup"
+ "Successfully persisted peer secrets accessibility fixup state"
+ "TB,N,V_peerSecretsAccessibilityFixUpPerformed"
+ "TPH reports having a different egoPeerID from Octagon"
+ "Trying to perform peer secrets accessibility fixup"
+ "_peerSecretsAccessibilityFixUpPerformed"
+ "hasPeerSecretsAccessibilityFixUpPerformed"
+ "octagon, Failed to perform peer secrets accessibility fixup: %@"
+ "octagon, Failed to persist peer secrets accessibility fixup state: %@"
+ "octagon: Mismatch between TPH's egoPeerID (%@) and Octagon's self peerID (%@)"
+ "peerSecretsAccessibilityFixUpPerformed"
+ "performPeerSecretsFixUpsWithSpecificUser:reply:"
+ "setHasPeerSecretsAccessibilityFixUpPerformed:"
+ "setPeerSecretsAccessibilityFixUpPerformed:"
+ "{?=\"epoch\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"peerSecretsAccessibilityFixUpPerformed\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"
- "{?=\"epoch\"b1\"lastHealthCheckup\"b1\"attemptedJoin\"b1\"cdpState\"b1\"icloudAccountState\"b1\"sendingMetricsPermitted\"b1\"trustState\"b1\"isInheritedAccount\"b1\"warmedEscrowCache\"b1\"warnedTooManyPeers\"b1}"

```
