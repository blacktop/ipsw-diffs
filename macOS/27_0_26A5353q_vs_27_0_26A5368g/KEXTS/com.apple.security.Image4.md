## com.apple.security.Image4

> `com.apple.security.Image4`

```diff

-27.0.0.0.0
-  __TEXT.__cstring: 0x38ee sha256:2b9897681be3b58c233cd2d85a9908a899bfae1d5956665ec0809b57c2bb6967
+27.0.2.0.0
+  __TEXT.__cstring: 0x39cd sha256:cce4a0bfb8902a071d6ff553a2fc61bd713d45ca18ff5a06653110b1275006b7
   __TEXT.__const: 0x79d0 sha256:cf3dabd10a4b4a36136eb2e3d1442048c096b42641c0aa26aaea4c7e322c70bc
-  __TEXT_EXEC.__text: 0x108dc sha256:4bc4259cb3a481f085e5a01fe70878cc86b015e5f2ce1a3682456109420726bd
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x678 sha256:d0c022a7458f9b8bf57ac877021f2bc52ef9efb21ee36eeb32597375f8b38275
+  __TEXT_EXEC.__text: 0x109d8 sha256:0358717a4d65f4c36c6dfdfaa5bc130977eacabd18cae5e9a56b4b7f441dbc24
+  __TEXT_EXEC.__auth_stubs: 0x4f0 sha256:7d5452e35dd5db57bbfe545e4ddfd7c85464267c2f089937415da38143990a24
+  __DATA.__data: 0x678 sha256:2f1ccb5d8a84d3d8ae8a919b522c60d75b16a4918948f54f2c49eb9c563dd94e
   __DATA.__common: 0x128 sha256:250f52cb2d6f1966a29f6ac771fa1cd185b8f8531396c8a4026c0fe635617e0c
-  __DATA_CONST.__mod_init_func: 0x10 sha256:cc2af02a1f9be0e969455c8570eb36dd6e3d0a1e8e9e0d4975ae956748dec704
-  __DATA_CONST.__mod_term_func: 0x10 sha256:825ba07d6f6630644a20f91f3e1a590d961e4f64e1e893bde955adb8835c53f5
-  __DATA_CONST.__const: 0x36e8 sha256:93969a1e62de9cc076ea75ee9f4ac501937e851869e662a6ba3a74f2c3bba107
-  __DATA_CONST.__kalloc_type: 0x80 sha256:a0f942bb51652b8da9a77b13b3729f4a9d93853550ddec9a453d654ee659e108
-  __DATA_CONST.__auth_got: 0x268 sha256:50199a83af31d9ee06fe9c998cf3505ee90191a01bb9037dc6bd273a557da40c
-  __DATA_CONST.__got: 0x68 sha256:784d3c239370f0e88d638beab2d2b1e88fdd26135613353c5a81ce1aed0d7215
-  __DATA_CONST.__auth_ptr: 0x28 sha256:c47fb4a53198f57f2ff52e61b60b093a0fa2b25fa98c5a4248c56c3a86662dce
-  UUID: 96E1BBC6-E20C-3896-A8BA-797C6A4B5714
+  __DATA_CONST.__mod_init_func: 0x10 sha256:f40101e3206d51f7e660a93f1ecb402d5239cb8e238b17bd00a1ba3c1614ba87
+  __DATA_CONST.__mod_term_func: 0x10 sha256:550615265c49750d6705911dc0eecac008ce3cf31e77d2ff48cc32c0f5339b95
+  __DATA_CONST.__const: 0x36e8 sha256:4a74357123031449e7df893442179a65d8def6b4a1acd2d1de65f8ac352169b0
+  __DATA_CONST.__kalloc_type: 0x80 sha256:10805ce991ff34ee5a3402aa1854b2d1a67040ee87a1ddf27ba0140d8f3fb139
+  __DATA_CONST.__auth_got: 0x278 sha256:0664bc9bc053b268531370e404b64d8a4622ad1c4d4fee2551cd8501df1a2235
+  __DATA_CONST.__got: 0x68 sha256:2bfc343026c868bdab0bc4c43d22cef1df258126fd2b4d8afe72f41b6a579e80
+  __DATA_CONST.__auth_ptr: 0x28 sha256:2515f1c36c368f7a0df274038cee78aa81b6470e340f13d69e057c8561216bd4
+  UUID: DEE7A98F-A747-3952-B378-79EA3586EF4B
   Functions: 512
-  Symbols:   1108
-  CStrings:  338
+  Symbols:   1112
+  CStrings:  343
 
Symbols:
+ _IOTaskHasEntitlement
+ _IOTaskHasStringEntitlement
+ __ZN16Image4UserClient12initWithTaskEP4taskPvjP12OSDictionary
- __ZN12IOUserClient12initWithTaskEP4taskPvjP12OSDictionary
CStrings:
+ "Image4: owning task is not entitled for user-client access\n"
+ "com.apple.private.image4.user-client"
+ "com.apple.private.pmap.load-trust-cache"
+ "com.apple.private.security.AppleImage4.user-client"
+ "personalized.cryptex1.update-brain"

```
