## libETLDLFDynamic.dylib

> `/usr/lib/libETLDLFDynamic.dylib`

```diff

-1418.1.0.0.0
-  __TEXT.__text: 0x200 sha256:4f85ce024bfd20b2fff8f4f7cc7b98187b768405716e660aeb4605f431b27868
-  __TEXT.__auth_stubs: 0x20 sha256:18b3a6b1f26a21085c0be4757dfff0203b0153ec2a7aac697c4a95a59a5b062a
-  __TEXT.__unwind_info: 0x60 sha256:e2373450b532525e9381269d7b209a3ac74197dfb9702662b3f23a3c88e0725d
-  __DATA_CONST.__got: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __AUTH_CONST.__auth_got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
+1563.0.0.0.0
+  __TEXT.__text: 0x25c sha256:9aa18c78f0d95667cc49b1e7fa84c1d523235c48eca95be6d8012e0cef48aad7
+  __TEXT.__cstring: 0x52 sha256:16632567430728c2d88627ea6fe785fba684ba023e1b00391cafca549729b9b8
+  __TEXT.__unwind_info: 0x60 sha256:71c00c2c3e32570d2e0da6bdc8cb85554c489eb3470d06ec3ecc05458a5b4f1b
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/libETLDynamic.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: 547902B8-C983-347E-8884-BEE119508595
+  UUID: D3CA0CAA-248C-344E-BDEA-3B78F3D1DB26
   Functions: 2
-  Symbols:   7
-  CStrings:  0
+  Symbols:   8
+  CStrings:  3
 
Symbols:
+ __ETLDebugPrint
Functions:
~ _ETLDLFAddVersionReport : sha256 a00ea59fcc6fc6160346b8591d86d92269f0b5e99c33ae20e214421da3167d15 -> 73c7e197283b18b2fbf4b85664d7b5b86f94954924ec85451df75c1f8344a91a
~ _ETLDLFParse : 124 -> 216
CStrings:
+ "ETLDLFParse"
+ "Length %u not enough, need %zu\n"
+ "Length %u not whole payload, need %u\n"

```
