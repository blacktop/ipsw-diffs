## ndp

> `/usr/sbin/ndp`

```diff

-741.100.2.0.0
-  __TEXT.__text: 0x3afc sha256:c835dcc4c534aab8a56e334574b4c28600070a2749f9277307385dbe1eac74e0
-  __TEXT.__auth_stubs: 0x310 sha256:adcfb929a6f8c2ccdfc27a82a2a1c071dcaf70e10cfc6cd6737af8bd2f36579f
+754.0.0.0.0
+  __TEXT.__text: 0x3c5c sha256:ba869221978a4e53f230ad8e1a71e3d8530fe29992baf9e338f4412aa387f277
+  __TEXT.__auth_stubs: 0x310 sha256:0abca2f7afe2c5ca3b6c9c265f3a131dee7d1052fec7c3c41e5c5734b8b55037
   __TEXT.__const: 0x50 sha256:425a5928eac73d357c67e7339d902279271680db5575cfca02b863357b321732
-  __TEXT.__cstring: 0xbc9 sha256:49342aa526f3b7932eb631a7e69e32e1bb610b43798983009ffaeca579a17862
-  __TEXT.__unwind_info: 0xb8 sha256:89e9083f904bd36a75f8482336847453525d967fe18e207c67cabead2a92e62c
+  __TEXT.__cstring: 0xbfb sha256:e527b0f19daa10e3edc553fb04bc5cc801c135e67caa49a6291dae1a05aa7f63
+  __TEXT.__unwind_info: 0xb8 sha256:b579cf6929f5f58234c8b1d64d76e381ae1466da4d171cbc95634c196c7b99e9
+  __DATA_CONST.__const: 0x58 sha256:2bc1a0f721d9b67e7de6c6922920a5038d3456561145e91fbace85f0fdb49fe2
   __DATA_CONST.__auth_got: 0x188 sha256:1a9d3596f654eca6a3c384ccaf5d79742cea78cb48beb9dc372eff6c3366c4db
-  __DATA_CONST.__got: 0x28 sha256:61c7c48009cb4aba8b66078dc06614e15d57bb9a198b2be3f3f11be7b9df2113
-  __DATA_CONST.__const: 0x58 sha256:86ca1cf27f716db7dce47f66464f6ab95fc28d5e964a42cf3ecb239f05c77c4d
+  __DATA_CONST.__got: 0x28 sha256:0d41ad89fb140939b39c6784737afe244647cdf582a8c436049926ec70ff4176
   __DATA.__data: 0x50 sha256:b4d8880f7b80962bb092ec66543d39b4f83e4ea0b482bd2cdea293323a3d92bc
   __DATA.__bss: 0x25d4 sha256:d4fec03cdb443dd27029f97c9b22bc8f355752cbc72bbf1304def4c27ba6d0cc
   __DATA.__common: 0x298 sha256:a9696dcbc2bef81a08d6b1a798091d2b1a49654218d3ebdb12f9b255cbb1476f
   - /usr/lib/libSystem.B.dylib
-  UUID: 4FECA6C6-4825-301D-A6CD-32C13C9A0ECF
-  Functions: 24
-  Symbols:   99
-  CStrings:  201
+  UUID: 17E9C4F8-D54B-3095-88D5-E555911E5B10
+  Functions: 25
+  Symbols:   100
+  CStrings:  203
 
Symbols:
+ _rti_flush
CStrings:
+ "       ndp -Z interface"
+ "acndfIilprstA:HPRxwWzZ%:"
+ "ioctl(SIOCSRTIFLUSH_IN6)"
+ "ndp: cannot apply flag '%s' to all interfaces\n"
- "acndfIilprstA:HPRxwWz%:"
- "ndp: cannpt apply flag '%s' to all interfaces\n"

```
