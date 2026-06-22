## mount_tmpfs

> `/System/Library/Filesystems/tmpfs.fs/mount_tmpfs`

```diff

-92.0.0.0.0
-  __TEXT.__text: 0x520 sha256:e6b0be77283ffd7cf95e9533a8dfe876cdac612e3dcebf4b81bce6cafbbb6a28
-  __TEXT.__auth_stubs: 0x110 sha256:5b3748d0fd9803d174ac02dba78def012bf0502181b57368895fa2a77dc3e113
-  __TEXT.__cstring: 0x250 sha256:ece0d62a5d10fc3f42d14a2c3fcdb808ad28a071343d29774a968c555089d525
-  __TEXT.__unwind_info: 0x60 sha256:9c4087b219227b00c24f95d4ec59b9c68502908657846b7057e74e87ac306a9f
-  __DATA_CONST.__auth_got: 0x88 sha256:27bbfea54df58c994fa4191004e52df860cf4496314efe05d61041304212be4d
-  __DATA_CONST.__got: 0x30 sha256:7f17f78b3ccbeebcb59c80abb433f46e740fa0a0cce8bec87f02fb0539d0da21
-  __DATA.__data: 0x240 sha256:cc1fbd489defe8d9c9f4730098ef60d79857ec7d66c788023eac1336f91b6c82
+93.0.0.0.0
+  __TEXT.__text: 0x568 sha256:198b22cc8fb8a69696a8f6ce5a129391e3792a34236404e9e42aec05e9e9d4db
+  __TEXT.__auth_stubs: 0x120 sha256:7e700c49f12c68cc4d50097baeee7a3f3dfccef427feef0ed077e1f88e09c87b
+  __TEXT.__cstring: 0x279 sha256:94e0d0e372fe375ecfcf3f68c9b3b3f15eb4e9ed179253fd3c6a4cac3f68531d
+  __TEXT.__unwind_info: 0x60 sha256:2c8c8775b0f3a3da904f69e53d9fa835fc296a22fb416f9ea52cf09e5052cd15
+  __DATA_CONST.__auth_got: 0x90 sha256:a6725f094753f245bed63e86bedcfbc5be6cc48866dfae54492d02b7d2e8cc24
+  __DATA_CONST.__got: 0x30 sha256:9677f5f7c2e9526dcc9d86ecac8e273d237d22c93406b3c470fd1628d160ce81
+  __DATA.__data: 0x240 sha256:cdd1078fb14fd0c85522a2be409e55e6a9b270b39e8020d4044b8c1458d1ea9a
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 3FD3D925-3AC9-3F6F-9B7F-5A8267F0E766
+  UUID: 0F7F381E-2B1E-3A92-8C03-EBBADD09F49D
   Functions: 3
-  Symbols:   25
-  CStrings:  33
+  Symbols:   26
+  CStrings:  34
 
Symbols:
+ _strcmp
Functions:
~ sub_100000570 : 1240 -> 1312
~ sub_100000a48 -> sub_100000a90 : sha256 68f0b7bfa336d5aa60aea0668d09cae96a3de3b0f50f59de2df7bcd61a137c5e -> fb5fdded3b4b8c00e54a51b191d90fd0bb0de6ab800107941eda8a7baf484873
~ sub_100000a74 -> sub_100000abc : sha256 b386425083cf6f253615f02abf4d829e3dae042f8545856edaf44775f221ef6e -> cd6eef5c1b31aa13122598fc8cf1a3d1fd8cf6241615e399007e96f9de490be3
CStrings:
+ "unexpected special device: %s\n"
+ "usage: mount_tmpfs [-o options] [-i | -e] [-n max_nodes] [-s max_mem_size] [special] <directory>"
- "usage: mount_tmpfs [-o options] [-i | -e] [-n max_nodes] [-s max_mem_size] <directory>"

```
