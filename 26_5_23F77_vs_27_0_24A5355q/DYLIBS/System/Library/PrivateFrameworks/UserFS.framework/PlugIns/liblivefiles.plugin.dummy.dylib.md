## liblivefiles.plugin.dummy.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/liblivefiles.plugin.dummy.dylib`

```diff

-741.100.13.0.0
-  __TEXT.__text: 0x564 sha256:82e5b74097b5d9e292f562bfb75297defe964b25c27160f5d53c952cfef41386
-  __TEXT.__auth_stubs: 0x10 sha256:bec549934e99a577e3a55094eb4a479b521a4673d4cf05c517bdf49006f62332
+762.0.0.0.0
+  __TEXT.__text: 0x56c sha256:46d07f07513ac99f7f93785162bb0d4f6ddb6a64b0b7b94d3f9563805e6ae953
   __TEXT.__cstring: 0x118 sha256:f8c6e21ab41bcd558526381b8e8b06fa36254023123adaf5c1c5a953ec74e23b
   __TEXT.__const: 0x10 sha256:be45cb2605bf36bebde684841a28f0fd43c69850a3dce5fedba69928ee3a8991
-  __TEXT.__unwind_info: 0x70 sha256:a7e1a7cd2a9b238c2e0f79ff9c65c3d95e19310e19f7594206489b5f7fb3a768
-  __AUTH_CONST.__auth_got: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __AUTH.__data: 0x140 sha256:dbbc1e4e774b2140f21108335ffc48eeaa4c41b6e8e6a14e524a13dd55429948
+  __TEXT.__unwind_info: 0x70 sha256:9c7839ec8a039098e3d1667361589ae3d609051a5bdafdc306aa837bcdd34b1c
+  __TEXT.__auth_stubs: 0x0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x148 sha256:aa724ca0bf6c7d1f9498530b425023e5982e8c6fd01ca32beae06c268153b781
   __DATA.__data: 0xb8 sha256:de9bbb2b0ef717dd926fbed81a9fbc4c0b13f96e630ee321293a81332d560b3b
   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
-  UUID: 8DE95E05-8E6F-3869-991F-61865068A963
-  Functions: 27
-  Symbols:   56
+  UUID: A50E8036-3D37-3BBE-850D-9151D1BBEF9C
+  Functions: 28
+  Symbols:   58
   CStrings:  21
 
Symbols:
+ _dummy_fsops_sync_file
Functions:
~ _dummy_fsops_mount : sha256 0715c4bc1dae13dd81554ed0045b190c8e3fe79bcc5e00f954ca3763cf503d34 -> 94d1e376045097355fee7a46143ba2ffd51ceeb2fa896352f975b55a8ed17a05
~ _dummy_fsops_unmount : sha256 bf973055297aad77d67a7ecbfec341c9ac1f5b9de4dd5f06b4686600ad01601d -> ebe25d88e8708a4335dcf408f0fd40a4b7d33dba26d00b42de78c5b77bb9001b
~ _dummy_fsops_getfsattr : sha256 08ebb48b743672e646df991c235d61b8d5e568213c4bf617d6a4f07e89b5d454 -> 27b0c5fba38bc0b34dd5e3df48b3882a30fe9526eca242c89f6922a1a8387201
~ _dummy_fsops_getattr : sha256 9bf4657b79f618ccc93840773dbc39ffe725a5e09d31854b20f6bf06e7c5cf07 -> 0218bca98660dfb41959c660e872f319e453b7b1166527c1ea7c0e9441c21674
+ _dummy_fsops_sync_file
~ _livefiles_plugin_init : sha256 29fe6a7d4c8aa94913fec3791278a384dd4681611cab0d5d4ce977f382230106 -> 3184ec5a102248d342fb48a680443e9f4370fec3ca3729aaa943a2a7c0e4441c

```
