## create_automation_image_overlay

> `/usr/libexec/create_automation_image_overlay`

```diff

 9.0.0.0.0
-  __TEXT.__text: 0x1550 sha256:5a12de841b2cf78e189056b8f848e3ffb2a5f6c447fea9a7b41a8e2940e4f005
+  __TEXT.__text: 0x1550 sha256:f11ed1a755b1030bbe1fe625be0da817e4b08c55ac2b5cdb2862d0d7c17e868d
   __TEXT.__auth_stubs: 0x280 sha256:e82ef583b62fe4e896c8f6d289ca9d36aac65f2c76157fddeb96d9565f1f49e2
   __TEXT.__objc_stubs: 0x420 sha256:d8cb7b5785f6a346250ab7a630f2ae3ab6553e8d96717aa3839eb3213d2f44eb
-  __TEXT.__objc_methlist: 0x14 sha256:7b90e725815e99ad3d90cc04316cd574c2148b39c83174382e8eeb44e2d1ce0c
+  __TEXT.__objc_methlist: 0x14 sha256:66cbf0ef877ee9a967fab50ff530c446fd4f126b9ab271ab5181bf0596164a3c
   __TEXT.__const: 0x5d sha256:f62104a5f2d6add32a195af807cd27486bb5817d8cbc9bc67ed3d2669716c57d
   __TEXT.__cstring: 0x556 sha256:00bfe74df69cee56e984559a4fdeb95ea553daffb2a266d71a2027e69169ea58
   __TEXT.__objc_classname: 0xf sha256:85a7ce5561d77cc99b2ab72f82a16ba970a1c02810aab96bd7fac4cc1032517e
   __TEXT.__objc_methtype: 0x8 sha256:f800facdcdbe56f6a2a8ba11e9e3d4c2a8852b2cef57d7b935bf3d348e3437ce
   __TEXT.__objc_methname: 0x32a sha256:c451e7a0a417c1b7d0640e423f87b4bfef3b5544177ffd8c966ec99b39357ac3
-  __TEXT.__unwind_info: 0x90 sha256:3e94dc8d613394bceedfd2ee23e9153dd7746094b80b30feb66bb22decbc4ef7
+  __TEXT.__unwind_info: 0x90 sha256:84917748c15d1b76d66f9c95abf18fdebf18b0fb2147d0d772b3441f3b307b71
   __DATA_CONST.__const: 0x80 sha256:1d985fd3964102393b7eefac616271df65bb31170d47d001ee07ffe529ad53d0
   __DATA_CONST.__cfstring: 0x120 sha256:0ff82537b9f6ffd41df1576ce4dcf5e4c119f07c7909980b936e396a02fa3b95
   __DATA_CONST.__objc_catlist: 0x8 sha256:8da6463fa1ce25df7f02d6a7e97e4896aa844d61e08bfd95ebc128882ceb3012

   __DATA_CONST.__auth_got: 0x148 sha256:c11732abd785cbf2e6e05b065e72d43d5a62742df95bdf0af29745d296bc573a
   __DATA_CONST.__got: 0x78 sha256:d85b84bfc3f81d3bed1e09b5d7db626e545a0bce65cbd7396eb24c0b72ff7263
   __DATA.__objc_const: 0x40 sha256:b1de8513913e5968b49f0a87f385a727ef957c9e8bc2b7eff7944d396f922f2a
-  __DATA.__objc_selrefs: 0x108 sha256:f7b6116f21e2bb6efd82609365f7aa86fe486083a0b94b34a3af03f2aa142a0e
+  __DATA.__objc_selrefs: 0x108 sha256:69e4e78920ba53a519f105223f67d3b32b8bfdd584426ac409bb8918706d935b
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 527FC25E-9D5D-3E0A-9385-DE4B64FCD414
+  UUID: 64DEDE47-C2E2-38CF-9F2B-48C9ACCD0852
   Functions: 13
   Symbols:   63
   CStrings:  107
Functions:
~ sub_100000b18 : 804 -> 808
~ sub_100000e58 -> sub_100000e5c : 2568 -> 2572
~ sub_100001860 -> sub_100001868 : sha256 cfec82eb9f673ff639297f1c25ba90529bad056b914c1f5b498aab6cc8ff78e2 -> 6e25a4cabf3250d9fee2c4d3babfebdc219ce08fdaec1a517e5d130b5d2529fa
~ sub_1000018a8 -> sub_1000018b0 : sha256 b7b3790e11cce0f61a245fd84d301f383865d3b47e29e75e090bae7e9d3be44a -> 29dee15602fc8c7008c4deef6267358442c95bdf194aefef10c85a828073f19d
~ sub_10000193c -> sub_100001944 : 896 -> 892
~ sub_100001cbc -> sub_100001cc0 : sha256 efe49f98a6db1676c5ea3f2da8410e3826bc4f574148b89adf07ef9a04f2c541 -> 3541f0fe0d03e68bf414ca87ca23725671d29fce6358dd4db316670c56c4f8be
~ sub_100001d00 -> sub_100001d04 : sha256 49823c44538fad88e3bca106834f9afc6ad9c9cc306754ee8bd042f54a05b191 -> 1ed93aa5e66808902f93327eeba4df18261aef53fc4a6a028252a5047d057e00
~ sub_100001d34 -> sub_100001d38 : sha256 dc830f523f9edb783eeb07bdea8c4ac7b1a0a3338ee0f1bebad457c30e59263e -> 5fe620b806eb798b02dc27be9aa181a9dbb4d7917bd42465db10177611584c4f
~ sub_100001d6c -> sub_100001d70 : sha256 b9bcbf761425501e4d212b5ebf0abf9ff8d723faee30a7adc5e80e1602bd3095 -> 461531f87654d45148498e21bfc9d9e99bf84b1e33b003dd3198e66a03428dbe
~ sub_100001da0 -> sub_100001da4 : 500 -> 496

```
