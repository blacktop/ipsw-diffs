## IPConfiguration

> `/System/Library/SystemConfiguration/IPConfiguration.bundle/Contents/MacOS/IPConfiguration`

```diff

-551.0.0.0.0
-  __TEXT.__text: 0x5dafc sha256:e1e7d8c2533704e5e6636f2f1f8671009374f3dd86b584d3ac1ac949bdaf1258
-  __TEXT.__auth_stubs: 0x1160 sha256:4900a19b885f728728bec1391d93fce4badbcd6c41e31bc17720014686e18b5a
-  __TEXT.__const: 0x310 sha256:00af477299b0d10b05385df92786efedf3166efeb4adfed4682cbd051ee9a909
-  __TEXT.__cstring: 0x4311 sha256:54e42718f5195d1f4d4f5420ff49cc25ef2b5e850a3ec2f1bf24355cd7fad28b
-  __TEXT.__oslogstring: 0x630c sha256:e939b47b9adfb616202e2e85d2bca09353d11bf45f934af55493b1acf6b8927a
-  __TEXT.__unwind_info: 0xc20 sha256:041ab2729e53d76e63410532bc085339216623db21e67481c762d4abe203b72a
-  __DATA_CONST.__const: 0x1e70 sha256:34cf5b747b057142ca8aea93f071affaaf8b20ea19759708c7067ef36d44850f
-  __DATA_CONST.__cfstring: 0x2c80 sha256:e4087a4cd2b4c602edc5bfe50f12f7a856a10f1d2f246b04ed103edfe52712f7
+553.0.0.0.0
+  __TEXT.__text: 0x5dc1c sha256:dcc96fd8fce0dba292550198c228cb37ff5e58d4fa60f7a0273604c595a115df
+  __TEXT.__auth_stubs: 0x11c0 sha256:88938ac463a8e580e0bf06772dcf766e07fa288cfd137877e2c3aafa86393ae4
+  __TEXT.__const: 0x310 sha256:ac5dab355860ddc993bf9108cedede6a65db1a0ada68beb0f397805b64288a61
+  __TEXT.__cstring: 0x4336 sha256:d61ea54386a636456a0ed574c2f5d2af5f3304f676d11154b763ddf618b3e153
+  __TEXT.__oslogstring: 0x633f sha256:166f5b53e89f6aaa25f0a50bdcb5945fa0ab45f24c7d0d94dbb31e464be51451
+  __TEXT.__unwind_info: 0xc20 sha256:3395867b87b591e41d10b1e62d975b32094d463941ed6be5f749d769e40c4979
+  __DATA_CONST.__const: 0x1e58 sha256:19a985ac3417684a7286591ddd18176dc4eac65c0d652b7203e6d3c4a7f685b2
+  __DATA_CONST.__cfstring: 0x2ca0 sha256:54834af9b20d236c467eadf4497422febb60ae58d8afe835c27331d324c569fb
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__auth_got: 0x8b0 sha256:e4526c86cf516956880c7f2480baa3f853061a000b11aeb4f724b54265f3e6f0
-  __DATA_CONST.__got: 0x410 sha256:269803864aae68a125fc7adbed4096abbe77db7bf456824c271c5e8c74d837fa
-  __DATA_CONST.__auth_ptr: 0x100 sha256:daa41f81e4bf2407c0b5fe482d880f01175889d8e993643a5dc7a6abfb397d81
-  __DATA.__data: 0x118 sha256:8e33041cfa55c87eba886406494c9dd93757848fea9420d6d9dad6b61c266f80
+  __DATA_CONST.__auth_got: 0x8e0 sha256:3280643377639e2ebbf232a846dd00656b926066033e628f12048a80db2a5b59
+  __DATA_CONST.__got: 0x408 sha256:d2a2c697249bd3173f7d0775408b1f1159d542e699f1178b5b4d6e26fce10c99
+  __DATA_CONST.__auth_ptr: 0x100 sha256:f3e2a96d2f7214eec9e301c0088b0f93cf4499670e3ad1e5e57ae30504377208
+  __DATA.__data: 0x118 sha256:03c49fe1022bdc9a98f2b926c111cae88c58002bb14c0dc9b30c6f4c6b913ce4
   __DATA.__bss: 0x228 sha256:0345bffb28f80f4d0ded1a2af09a337b18ab3a80c68205bc8321a6ad4d409500
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 762E690B-78F1-3B67-AC8B-BE9C6EF27972
-  Functions: 1047
-  Symbols:   523
-  CStrings:  2121
+  UUID: 9D0DB5B5-95FA-3C06-B592-D18808DB4B68
+  Functions: 1046
+  Symbols:   528
+  CStrings:  2125
 
Symbols:
+ _dispatch_mach_connect
+ _dispatch_mach_create_f
+ _dispatch_mach_mig_demux
+ _dispatch_mach_msg_get_msg
+ _dispatch_set_qos_class_fallback
+ _mach_msg_destroy
+ _mach_port_deallocate
- __dispatch_source_type_mach_recv
- _dispatch_mig_server
CStrings:
+ "%s: dispatch_mach_mig_demux failed"
+ "IPConfigurationAgent"
+ "dispatch_mach_create() failed"
+ "ipconfiguration_mach_handler"
+ "no domains "
- "%s: failed %d"
- "server_init_block_invoke"

```
