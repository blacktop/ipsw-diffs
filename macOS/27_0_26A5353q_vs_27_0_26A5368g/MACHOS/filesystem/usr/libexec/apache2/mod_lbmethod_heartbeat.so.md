## mod_lbmethod_heartbeat.so

> `/usr/libexec/apache2/mod_lbmethod_heartbeat.so`

```diff

-886.0.0.0.0
-  __TEXT.__text: 0x1324 sha256:af85ea4bdf3f8b599afe8851069573781eaec0fa7b78b1199aaf699e8127218e
+888.0.0.0.0
+  __TEXT.__text: 0x1320 sha256:9c413569657248319a7051a955bbdd48cd5541373fd8687be2f4ad523f8f4a56
   __TEXT.__auth_stubs: 0x290 sha256:0282c957eacdb56113ca85336608c9f3c8807a099e8f639dc817f2f7e77318bc
-  __TEXT.__cstring: 0x2bb sha256:06207dda5406c17efacd8bca5e61d5e3309c29a11976bd3ddde2f171f21deea3
-  __TEXT.__unwind_info: 0x70 sha256:eb9859ed3272784f60af4c4f3faf261ead82729fea8cc8d07cb851880513a7ec
-  __DATA_CONST.__const: 0x90 sha256:90d78ad343aaa85c1dccf574ab3e3b2400f05e6fb5793c8f2538bb2ec263ea44
+  __TEXT.__cstring: 0x2bb sha256:68e3985780b3b6c77e679d4ed95a8d82dd767ad484753c85cb5f6eb018276cac
+  __TEXT.__unwind_info: 0x70 sha256:e5cfeeeacedcf10dd3089e9ca13f0e2eb6d25358f07b5ffaf31efc6d288a8676
+  __DATA_CONST.__const: 0x90 sha256:33ffe2e2415a8a7a313b6e4bbf62000105f7fd151a3ca206092050f714a74c46
   __DATA_CONST.__auth_got: 0x148 sha256:ae68491e27c8941d25c5f1c5b1fe2d6fefee1e72cf2ce84430f0185d5348ac99
   __DATA_CONST.__got: 0x8 sha256:7129bc16bdb1a29e6d5213fbc43dd52e3987c8ba6fe1da2367be517e270f2e85
   __DATA_CONST.__auth_ptr: 0x8 sha256:1e7b1d8d821a2120c73f102dbf0ba88c1c8482e2c958dbcd43f60cca5028f772
-  __DATA.__data: 0x70 sha256:6026fb69dd1d32896a962cbacf90fa2a1ea733b254535c036acb3d319d65b060
+  __DATA.__data: 0x70 sha256:71aefa7e95a1be0f8188b135b02e08ec78a0af27e9c03ee8996afd18d4998366
   __DATA.__bss: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: CA626A3E-53D7-3F2D-8BFE-5C35D27A533C
+  UUID: A755B465-1A35-3A4B-A210-6C1EF924C38F
   Functions: 13
   Symbols:   63
   CStrings:  26
Functions:
~ _lb_hb_create_config : sha256 d6a430bea45489301ba78e85fef1cad5e1a7b1467d5efba361edfda59f4f5000 -> 70f2af776ea113e34e1b3e84dd273fcc1b1bdcd219e88e7c04c424e36e1f2bd3
~ _lb_hb_merge_config : sha256 b3ef42eefd701772bd0503c0e54667261d0ee56d328ec5e6dbef298a10658bb4 -> b4354f4390f04a9ec1f19f71d03e648d59e796cd42ac67ade5391b4462dc3362
~ _register_hooks : sha256 0e676d54b970496bd03eef1a9294dc03fa6a10f3c6fa0f8ca0bd3e3f2de1e738 -> a0615d6d593123a3261fdc903654dfb013463bd4878e8f4dbb7669ef5c3c7291
~ _cmd_lb_hb_storage : sha256 5c90172f8e65f7cdcb63e69c06186a8bde46115c127b918fba4b7d0a218e829e -> 4cee772526bfc7c2f031d9a5cde822a885ed96c92afe4d73d416bf82efb25b08
~ _lb_hb_init : sha256 d7ac27042311f28adb1f064409ec4e0ab12de879f29922b871189d5774b63cda -> 66efa294f416ad7422057e035c3d0e65abb3526012780e80c1ed5fe175cdb6fe
~ _find_best_hb : 1832 -> 1828
~ _readslot_heartbeats : sha256 11979f5f7fcaef6341a0b553b83448f1e8d6cbda8a7ba37ef730418c200deb30 -> 59fd0da598c23b42e312f81eec8a77eef2fe2f3d451c326d93940414231d4345
~ _readfile_heartbeats : sha256 6073efb7b9b8fd6f96cae2439eb0deac233c357c197126c669e394da7aaceef6 -> b8f333962d658b26966df80c2dfb0391df5ebad209d1af10e1baed3dfb0f3649
~ _argstr_to_table : sha256 2605e9a1c2bab71afabf6f65a3d3c7498cca4101117c6927a950e53cf088cdc9 -> e79a61f9dcdf8ea0b01f6c8a7f1762ec96747403f58564bbf6f382070c0c98b3
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRbjugDs63E_nh9LrKXIzNhaKOKGLV_zLQv5WSg/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/proxy/balancers/mod_lbmethod_heartbeat.c"
- "/AppleInternal/Library/BuildRoots/4~CQCNugBXuVk5QyWQghtZ7Xdpnx7s5XYALnb8teQ/Library/Caches/com.apple.xbs/TemporaryDirectory.AuKlu0/Sources/apache/httpd/modules/proxy/balancers/mod_lbmethod_heartbeat.c"

```
