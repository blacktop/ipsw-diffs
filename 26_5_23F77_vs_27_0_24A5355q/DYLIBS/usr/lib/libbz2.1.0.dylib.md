## libbz2.1.0.dylib

> `/usr/lib/libbz2.1.0.dylib`

```diff

 49.0.0.0.0
-  __TEXT.__text: 0xa9c4 sha256:dba01f85f34ceed66cd9d9501aabf2ffb7f4ead79059f97952e066501a768293
-  __TEXT.__auth_stubs: 0x130 sha256:185eda933d3171ad87d4c39b18666f5d45fc9ad6c04fdd50384c148756c73e80
+  __TEXT.__text: 0xb004 sha256:d55d01a8550ee03fea4ec9f4d406beb564236f3f28f8776b0156f3ed302fee21
   __TEXT.__const: 0x4e0 sha256:0d7794e35ec0ef9b50d9530d4c1f7d11e4ae346946d4da1c4c171f1ed9cc3366
   __TEXT.__cstring: 0x94b sha256:eb916c9f6f93f8837dab12d47f895f815c8a2472140b04c87db732e14b3964b5
-  __TEXT.__unwind_info: 0x110 sha256:41124836e6af61cc6400c1b9b821f5d5e93cf71ede689cca92ff77e6e29f21ff
-  __DATA_CONST.__got: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
-  __DATA_CONST.__const: 0x80 sha256:d3b00c6c19f34140446f5be0dc9f24b399f50d012862985634d53f0e064e6034
+  __TEXT.__unwind_info: 0x120 sha256:62c4b0445b9a1736315c404f81328a73d6229ad2bd95b38a88ab5ddc0a7b687b
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x80 sha256:725a0d26f24cb01e4c1f47c61c6d3f38f0641b37790edafd708930c67c62bba8
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x98 sha256:85ada57e1f601e962d705f389285adb4e74f450bc00672240dfef7399d82457f
   __DATA.__data: 0x800 sha256:fa6f7d5596f6084ee582060b76239c49c1bf8567f7ea556e2d83971c75e26951
   - /usr/lib/libSystem.B.dylib
-  UUID: EC2C66EE-C164-3F43-B397-967BDD8F54E6
+  UUID: 61A9068B-C5CD-3BDD-851F-791201750406
   Functions: 43
   Symbols:   48
   CStrings:  40
Functions:
~ _BZ2_bzCompressInit : sha256 401e4ca2bfdbd0cedf313c6718836e18431fd2f0d3d5ee4abe7f10c3de5d5627 -> ccc5783383683613438b4079757c5af1b2c5e8db699589ba6b69aeb1175f6f65
~ _BZ2_bzBuffToBuffCompress -> sub_2bd05281c : 260 -> 20
~ sub_2a2ce0920 -> _BZ2_bzBuffToBuffCompress : 20 -> 260
~ sub_2a2ce0ac4 -> sub_2bd052ac4 : sha256 3fd6d6f65841b8e70ffef3a88da3ee2232ad715a982d784b91ba8a7cd7ee7dcc -> bd5aec0640532a265a2d73d2a25da59614147b2c63467cc0af0debed6dfc9a49
~ sub_2a2ce0ec4 -> sub_2bd052ec4 : 312 -> 324
~ sub_2a2ce0ffc -> sub_2bd053008 : 13504 -> 3984
~ sub_2a2ce44bc -> sub_2bd053f98 : 3884 -> 13968
~ sub_2a2ce53e8 -> sub_2bd057628 : 2224 -> 684
~ sub_2a2ce5e2c -> sub_2bd057a68 : 1008 -> 1168
~ sub_2a2ce6274 -> _BZ2_bzCompressEnd : 16 -> 144
~ _BZ2_bzCompressEnd -> sub_2bd057fe0 : 144 -> 16
~ sub_2a2ce6314 -> sub_2bd057ff0 : 684 -> 100
~ sub_2a2ce65c0 -> sub_2bd058054 : 100 -> 2260
~ sub_2a2ce6624 -> sub_2bd058928 : sha256 719c0b4e45f0317def954abf8ac63e33e24ebae58c6ffbf7d98135d53bfa45b1 -> c1f44ae6e30f739b31a5477e177d02deb68fe17b8672ef86abe6ad6c8acca6e4
~ sub_2a2ce66c8 -> sub_2bd0589cc : sha256 ed0ff0eeab6be38be585ee4fa9ca6ed1e7eec9cfef6bf29d726bb3cf10312667 -> 76e77091c8a1091b57fbab141e6725c782a23904d16d735e0cf900a438272176
~ _BZ2_bzlibVersion : sha256 db4754848849ed57229ea621c865e45cb84c39432b85a1f1efaf859256f2b76f -> ba4bb15a3e45b6e0b85f163b78e46b0a6da7a9cebb4399194d777493fe69136a
~ _BZ2_bzDecompressInit : sha256 128c6cfea54c2a3bd99c5188437f1f8882e814b99f25c1b3fea5b9db11911cc6 -> 22b5819dd427daf8428f2d9936f16cf3d79cd52f88a68319349ef2fe24db4f5f
~ _BZ2_bzDecompress : 3448 -> 3488
~ _BZ2_bzWriteOpen : sha256 c1d1e2f4db47ecfa60347abc78cbc73d7be6319218bb87db8841fb18c3244b1e -> 76a85d5972cc6f4773b3f6ae060d8b1b5672e1c24dd2559d1d3f2b23df1aabdc
~ _BZ2_bzWrite : 324 -> 328
~ _BZ2_bzWriteClose64 : 516 -> 520
~ _BZ2_bzReadOpen : sha256 6e2eba5d7d31bae44a888824fbaf1df6aa766f53a560bc84eb5c8fefbcd3c1d0 -> fe0b208cb85342b2fb2a93a7010146579ab67e0706ebf71aafb6b9021b0f4f4c
~ _BZ2_bzReadClose : sha256 4fec943876319e7af23881f3d0a7f46406f97d47eb7167091db62ae747098059 -> 465213b2e577a3daa0c462a450b45c6c24fae73297294258b16d2b6254bd256a
~ _BZ2_bzRead : 452 -> 456
~ sub_2a2ce7fdc -> sub_2bd05a314 : sha256 0544ed31816b64f5bd68bd8403e94ef49f797a2720ae5d946d22c1ef74f18ba1 -> 61258db27632d3ccbd5ee2aa71751dee40082d5a56b8466211b622d8b965a101
~ _BZ2_bzBuffToBuffDecompress : sha256 e9fda7256b365ad8c776f2aabb4a330c0fd3fd1f83479053c2c880041e469bc1 -> 74e9d86adfc91788132131c8e903c1420d17e1a1395081ddcfe5b628cc19a512
~ sub_2a2ce81a8 -> sub_2bd05a4e0 : sha256 3d95e53aec39aeaa6fadc5833814c43706465d954d643ee6e914b5fd6abe39d9 -> e671b7d2c68d41dc2372ae67c8bc159b9ae79f9abaf4aa49f3f8f32c05757d28
~ _BZ2_bzread : sha256 f3d7332d69d13111370328ccafd813ef8e742a0e1d529aafa9fbf865d995b916 -> dc3be34b38a04ce07038a620a64d91e4fec23ed8b8efe9e460b95c70b80d1dcc
~ _BZ2_bzwrite : sha256 b61fad290dcfb8a123581e29b38a14f0d02536c0499857f4f05b8d14b78a0efe -> 806ed48a661c1460a73875912cfe09c36ba03f617b1aa4d7730592500ac2aed7
~ _BZ2_bzclose : 200 -> 204
~ _BZ2_bzerror : sha256 b27dbaca31d420edfbab43382db59c6ed0083619d00e2048856dd748328d3eec -> 42e828f3062f5323bad669ea7dab33eaacae92b921b10c4fd2c7471701bfea02
~ sub_2a2ce856c -> sub_2bd05a8a8 : 10576 -> 11336
~ sub_2a2ceaebc -> sub_2bd05d4f0 : 320 -> 332

```
