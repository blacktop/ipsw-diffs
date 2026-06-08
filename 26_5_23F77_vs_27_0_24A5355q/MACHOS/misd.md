## misd

> `/usr/libexec/misd`

```diff

-381.120.6.0.0
-  __TEXT.__text: 0x21540
-  __TEXT.__auth_stubs: 0x1230
+394.0.0.0.0
+  __TEXT.__text: 0x21bbc
+  __TEXT.__auth_stubs: 0x1250
   __TEXT.__objc_stubs: 0x4e0
-  __TEXT.__objc_methlist: 0x38c
-  __TEXT.__const: 0x168
-  __TEXT.__cstring: 0xb3d5
+  __TEXT.__objc_methlist: 0x39c
+  __TEXT.__const: 0x158
+  __TEXT.__cstring: 0xb5c4
   __TEXT.__oslogstring: 0x1e
-  __TEXT.__objc_methname: 0x8f6
+  __TEXT.__objc_methname: 0x915
   __TEXT.__objc_classname: 0x74
-  __TEXT.__objc_methtype: 0x69e
-  __TEXT.__unwind_info: 0x508
-  __DATA_CONST.__auth_got: 0x920
-  __DATA_CONST.__got: 0x2c0
-  __DATA_CONST.__const: 0x9e8
+  __TEXT.__objc_methtype: 0x6b7
+  __TEXT.__unwind_info: 0x500
+  __DATA_CONST.__const: 0xa18
   __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x480
-  __DATA.__objc_selrefs: 0x2c0
+  __DATA_CONST.__auth_got: 0x930
+  __DATA_CONST.__got: 0x2e0
+  __DATA.__objc_const: 0x488
+  __DATA.__objc_selrefs: 0x2c8
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0x3a0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 328C8726-1AC7-3152-B7CE-DDE713A1F023
-  Functions: 451
-  Symbols:   387
-  CStrings:  1826
+  UUID: 959092B6-DE26-3E44-BAC3-726530242B0F
+  Functions: 455
+  Symbols:   393
+  CStrings:  1841
 
Symbols:
+ _SCDynamicStoreCreateWithOptions
+ _dispatch_time
+ _kPFSubTag
+ _kPFSubTagged
+ _kPFTagDict
+ _kSCDynamicStoreUseSessionKeys
CStrings:
+ "%s: SCDynamicStoreCreateWithOptions() failed: %s"
+ "%s: connectivity restored during grace period, cancelling teardown"
+ "%s: failed to create grace period timer"
+ "%s: grace period already pending"
+ "%s: grace period expired, proceeding with teardown"
+ "%s: grace period not applicable, immediate teardown"
+ "%s: grace period started (%d seconds)"
+ "%s: mis_pf_configure_nat_loopback failed, %d"
+ "%s: mis_pf_configure_rdr failed, network %s (anyexternal), %d"
+ "%s: mis_pf_configure_rdr failed, network %s (non-anyexternal), %d"
+ "%s: mis_pf_configure_rdr loopback failed, %d"
+ "%s: tethering connection not active, starting grace period"
+ "%s: tethering connection not available or active, starting grace period"
+ "com.apple.loopback-redirect"
+ "lo0"
+ "mis_pdp_grace_expire"
+ "mis_pdp_grace_start"
+ "mis_pf_configure_nat_loopback"
+ "pttSlicingCapabilityDidChange:"
+ "v24@0:8@\"NSDictionary\"16"
- "%s: SCDynamicStoreCreate() failed: %s"
- "%s: mis_pf_configure_rdr, network %s (anyexternal)"
- "%s: mis_pf_configure_rdr, network %s (non-anyexternal)"
- "%s: tethering connection not active, teardown external interface"
- "%s: tethering connection not available or active, teardown external interface"

```
