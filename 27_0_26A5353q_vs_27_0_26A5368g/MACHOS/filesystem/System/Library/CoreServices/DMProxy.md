## DMProxy

> `/System/Library/CoreServices/DMProxy`

```diff

 32.0.0.0.0
-  __TEXT.__text: 0x27bc sha256:27e064d22c1583a488bfdadcea7043a39db996fafa0942821fdb2eed654cf5b4
+  __TEXT.__text: 0x2798 sha256:91e0ad0e43fa96af0eaeea5e914495bef6047ab557da7e83b3259fa62ebf9364
   __TEXT.__auth_stubs: 0x6e0 sha256:3c37b53056a7314c7de29c1526e1b656d5e3c79ae988ae4df6238b2a2ed52f1f
-  __TEXT.__cstring: 0xf0c sha256:25d45d2f4c7b49034952a6b986cf14b799139694810a50408b5ca46bad56e559
+  __TEXT.__cstring: 0xf0c sha256:857fac4a37ebd261274053deaf7f842bf865bcd4528fae74857e020fb7ced881
   __TEXT.__const: 0x8 sha256:22b6f43bd8d27738d3213f29e96b62d01d9d6c0ab4f9732aaae803186f51eab7
-  __TEXT.__unwind_info: 0xb0 sha256:26f80da2505b83d68783b5fa87929d7bf3c7a82bb9528c36cf7b6e5aff34cbfd
+  __TEXT.__unwind_info: 0xb0 sha256:edeb1364a6bd7d7af859d0261bf83f6b8a9993638a3162922a27088e67f1317f
   __DATA_CONST.__const: 0x18 sha256:92d797a1cf4fd38bfda0957b3f277d646f64dad26d30a8318155beede7e11263
-  __DATA_CONST.__cfstring: 0x340 sha256:260ede3eef36694432ea8ae087967c1fe71333b8be78a5dbe51d7817558221e0
+  __DATA_CONST.__cfstring: 0x340 sha256:25184174da20772111ae430337e8cda2b1acbd3ac44c7089c60bf8b6ff4581e6
   __DATA_CONST.__auth_got: 0x370 sha256:d9a0709f4073397ed98548afcd06361517fffc3d6dd501a28a80b712be1a26e5
   __DATA_CONST.__got: 0x90 sha256:08b2c575b6b10118a596c34671b2e2d66b6098fbdd5a7774e67ce5dfd2c77ed4
   __DATA_CONST.__auth_ptr: 0x10 sha256:404e9250503f0ad990979a0d9d8f990dc22e2033a8aa21ed52ab390f2154a6a9

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AmbientDisplay.framework/Versions/A/AmbientDisplay
   - /usr/lib/libSystem.B.dylib
-  UUID: E96145FE-D569-3A67-9E03-DB444E30AEA3
+  UUID: EAF9BDFF-4AC4-3090-BCFA-C778FD039762
   Functions: 19
   Symbols:   131
   CStrings:  157
Functions:
~ sub_1000009e0 : 1028 -> 1024
~ sub_100000de4 -> sub_100000de0 : sha256 8cedbfb888f38fc42a6c6f92a515e38c6916824b2907a8a907827716944d0c73 -> c1e387bb11e782544d22681dca6441b185eebbb9aa9f8a3148a5c61e2f46c154
~ sub_100000e4c -> sub_100000e48 : sha256 aadc05ee3aa255a5a0113768e80f196afa65898cdd243cac9b69e7d263a8caa6 -> e6e17159fa064f6be9cca1a233bdeaacec6e8b06902f3939c42e41314da60ba3
~ sub_100000e58 -> sub_100000e54 : 2408 -> 2404
~ sub_1000017c0 -> sub_1000017b8 : 2064 -> 2060
~ sub_100001fd0 -> sub_100001fc4 : sha256 d8c2f9c5462d00eb58b7c85aa5ca925778f9d6b0dbb4ddfd51f19e8f174d65f1 -> 5c860ae61bb2bdd1574ecc4289f9b57512092624e5ed9e17d18ca94da54bbaf9
~ sub_100001ff8 -> sub_100001fec : 188 -> 184
~ sub_1000020b4 -> sub_1000020a4 : 984 -> 964
~ sub_10000248c -> sub_100002468 : sha256 262624d2585d07d63b9a956deeaf62fd7d8d854e07e82a48fc482c8a959f9429 -> 61aa330185faa1fea612bbad882b6b0502fe95cafdee695d2d8bf2d7477501fc
~ sub_10000265c -> sub_100002638 : sha256 e8bd7c78f512a0c577dcc85533e3966e59e7a84aa4b260e93c14c038e6300c02 -> 9d029fa8f1246916e3a38d2385afd6d5c597e57ad8c0dacc13efac0a5e4bdec4
~ sub_100002ac0 -> sub_100002a9c : sha256 0e1a5bf8b01db8429151c9e606264077a805d923c0b2d5d9f83588ea83b874b8 -> 42c43fb66f737e2cae6dd69172caa2a3201b24e6e24d3be69a9ab443b365315e
~ sub_100002b2c -> sub_100002b08 : sha256 ec5f5daccbeff053f57e8d5d2b4ffc0b6349211b6518083778da4f38051deaf3 -> 7430a9efe01190e4068efd030497689a5d6531c2fd36533c460034732a9b5c75
~ sub_100002ee8 -> sub_100002ec4 : sha256 171eae9f16d775d1cdd28e835c28550c0a89b53823dbe8adaa8584a6394dedf1 -> 92df95efaeb7030d1d3216f2637d4e0fed78c4ac9a05363a9cbc991188a5440c
~ sub_100002f8c -> sub_100002f68 : sha256 52ae8f6bf5fb3a7c2cda5a3cecc7cc00a08b237b19036bfd17b1b421a82afcdd -> 5965f9ea3d983a386433bdb6e8e98035b7ffe40410fa140fab22f5bfd513f508
~ sub_100003154 -> sub_100003130 : sha256 172dd1775a5fb424630cd66f1f2a6337d7435a7c60ec478f6f4909ce572db3c6 -> b3107014e4c02b2eb115f89cde0ed72372c26bd36bcd164779525be7c60e514d
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRb2ugDVv7sbkp5Jv7BuGnLkaR0eN3iIt-RsXLI/Library/Caches/com.apple.xbs/TemporaryDirectory.dVSHfQ/Sources/DMProxy/DMProxy.c"
- "/AppleInternal/Library/BuildRoots/4~CQCjugAiz9QMb6kGRatahNMVe_t4eI15vzOrHGI/Library/Caches/com.apple.xbs/TemporaryDirectory.qdZ8lc/Sources/DMProxy/DMProxy.c"

```
