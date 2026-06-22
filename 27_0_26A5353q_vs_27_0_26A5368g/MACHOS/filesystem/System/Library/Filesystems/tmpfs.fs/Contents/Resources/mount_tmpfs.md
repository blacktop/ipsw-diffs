## mount_tmpfs

> `/System/Library/Filesystems/tmpfs.fs/Contents/Resources/mount_tmpfs`

```diff

-92.0.0.0.0
-  __TEXT.__text: 0x55c sha256:51017d047f9eb36373ed9e90eb370af7f7b7474b0f6b4966b33ec5eace91cfc4
-  __TEXT.__auth_stubs: 0x120 sha256:ff91d695f38c98fa26f25c7de54f88576dd89679249df074747aa6df69af5dc4
-  __TEXT.__cstring: 0x250 sha256:ece0d62a5d10fc3f42d14a2c3fcdb808ad28a071343d29774a968c555089d525
-  __TEXT.__unwind_info: 0x60 sha256:0102a136c180c73030c7129841a59833ffffd9c17de596ab213a0a5d2c1a7735
-  __DATA_CONST.__auth_got: 0x90 sha256:a6725f094753f245bed63e86bedcfbc5be6cc48866dfae54492d02b7d2e8cc24
-  __DATA_CONST.__got: 0x30 sha256:9677f5f7c2e9526dcc9d86ecac8e273d237d22c93406b3c470fd1628d160ce81
-  __DATA.__data: 0x240 sha256:bea335b66129de148eb19c3ad806793d643cb91c8bce3cd1e5f99b68b54898e7
+93.0.0.0.0
+  __TEXT.__text: 0x5a4 sha256:98befb7ab27cd40c328592cd0dc69d0fd40d71a361fd15855322e4ad8c288d6c
+  __TEXT.__auth_stubs: 0x130 sha256:a179a0ce758b047e9887cacd0c0c93db4c401d634976c30d6716fe06f454006e
+  __TEXT.__cstring: 0x279 sha256:94e0d0e372fe375ecfcf3f68c9b3b3f15eb4e9ed179253fd3c6a4cac3f68531d
+  __TEXT.__unwind_info: 0x60 sha256:f1b3c389123d2c28bf1d4cf41f8ec5cebff01b0dbc6dc1e76c1e19be90ae4ef8
+  __DATA_CONST.__auth_got: 0x98 sha256:5fe86db3de63469b84d1b33dec29dd2873d9f8693adae1696664e42861ff1dfa
+  __DATA_CONST.__got: 0x30 sha256:3c4a88b1c0f6368b064a484545bd882c5d87d5658ccf9b51af9eb96fd4e1dec3
+  __DATA.__data: 0x240 sha256:1bc79ea3d7d25d2cb5cea6fb455e0b81defea9b137c4de15ee559eabe53816ab
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 94B49B5A-7530-3111-B8CB-537CD2D270BC
+  UUID: E6A231DC-802A-3AA0-A4B6-8B3BD25A9DD3
   Functions: 3
-  Symbols:   26
-  CStrings:  33
+  Symbols:   27
+  CStrings:  34
 
Symbols:
+ _strcmp
Functions:
~ sub_100000570 : 1300 -> 1372
~ sub_100000a84 -> sub_100000acc : sha256 ba2b1fce2f9f88e1e09644652ee6958c6df6d0b91038e3e44facf41933076e7b -> f3d6159bcc5a7c614b92fa0a6ac617268a7ce709485d8986af3f13c248bc3bb0
~ sub_100000ab0 -> sub_100000af8 : sha256 7b4352e0fa43c4505bf542ec7268e7d068bc8d290f70dcc4f1de0a035f3bfa04 -> 3d207062eabc244131623949ab8707ac7f9235608f509012209ff8912783ca5b
CStrings:
+ "unexpected special device: %s\n"
+ "usage: mount_tmpfs [-o options] [-i | -e] [-n max_nodes] [-s max_mem_size] [special] <directory>"
- "usage: mount_tmpfs [-o options] [-i | -e] [-n max_nodes] [-s max_mem_size] <directory>"

```
