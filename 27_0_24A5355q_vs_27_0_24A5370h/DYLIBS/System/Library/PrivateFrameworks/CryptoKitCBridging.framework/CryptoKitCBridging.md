## CryptoKitCBridging

> `/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging`

```diff

-381.0.0.0.0
-  __TEXT.__text: 0x2044 sha256:3272c3af35d67a033fb60adbe2ad6a9dfa74498fdb0be15e2c90437be31e0d0a
-  __TEXT.__objc_methlist: 0x1f8 sha256:87b9b8a751ff9e346c295321654dc3ec44745c6cf42e3796ec2dc1fae7d03708
+383.0.3.0.0
+  __TEXT.__text: 0x2044 sha256:be9dc7444a121905c227af251805965378c794a12f1bf3b6ad9f332aab6b8443
+  __TEXT.__objc_methlist: 0x1f8 sha256:558a7049af4dbdec761364644ecfee476bcaf3d9d39c6c6475c29a4b675c8654
   __TEXT.__const: 0x40 sha256:42f6786852f2eca2084651da244433b9cf4e0f7468546a7da7272e7acc716a17
   __TEXT.__cstring: 0x23 sha256:419c0706258714baabc6815b145bb5dd16383ed587b8f94255b612c73101a91f
-  __TEXT.__unwind_info: 0xe8 sha256:9860eaad41c2bafbd8931c04509e349c2837ff3119f18c2324a344c916be65b4
+  __TEXT.__unwind_info: 0xe8 sha256:391f54314964c49f9d35195d6cb6d575e85e9881c094a8b0ba0ae7bb92ea5f50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__objc_classlist: 0x20 sha256:2b287b7011b0d8b50e2683f3b2fe2071e2c43ffc9550ccdb9cbecd9dc7c5ce5b
+  __DATA_CONST.__objc_classlist: 0x20 sha256:acda447b6505982282e97f6f37bad87c19a357565d3634d69925a44ca2a03c99
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x130 sha256:06397478d53aa8912f04bd72b3ad94fce8c427db0a41870a41eb86797a14cd93
-  __DATA_CONST.__objc_superrefs: 0x18 sha256:35050680dc2dc2dac0f6ec0da7d43bfd4714af0cb24ed1a1d5005fb38da1f38c
-  __DATA_CONST.__got: 0x40 sha256:95c09d1d4bba8667a7f6fd73b8dd70488e0df9c16e092c4ebe9de63719e5fcd6
-  __AUTH_CONST.__objc_const: 0x368 sha256:aa7ebc9c4d4820940203597314fa0d3b209021a32300874d7d6856c59821cd8f
+  __DATA_CONST.__objc_selrefs: 0x130 sha256:dfaac6054111934352a9683929350267ace19d376a7f18eeea96f6b1cc18c7da
+  __DATA_CONST.__objc_superrefs: 0x18 sha256:6d5546d7f7217f1ca2508303b7d25bcfa2f0c824e3fb131a9a0e1ed754feca9d
+  __DATA_CONST.__got: 0x40 sha256:c68a28870fe056298e4855ded1f8c35b34732f17010a84dd6852ce476c5c8ff1
+  __AUTH_CONST.__objc_const: 0x368 sha256:19943d44eaec64cb203c578e9de9e5152bb83046174715a18749519781dce5df
   __AUTH_CONST.__auth_got: 0x248 sha256:62ec1707572ac5078d31a687a5d23de0c6d2a58d3462efb7039957548a7986cc
   __DATA.__objc_ivar: 0x18 sha256:0f90eeb58ff64398c563f0b14e14de9e18ec71087166435503616df93222d1ae
-  __DATA_DIRTY.__objc_data: 0x140 sha256:f60dde2b1c8e864a3fc5ee9669839095b8c94d13ec2ffbfa2498c8b921be267a
+  __DATA_DIRTY.__objc_data: 0x140 sha256:bc369433ea5581f47b865bf2bd75fe1f9b0e1d372e53c7ac5e5eed10b859d6b1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 217C5421-42ED-3871-9DD4-2881B0513861
+  UUID: 8C915082-520B-34F3-9116-0694F2705CBF
   Functions: 55
   Symbols:   228
   CStrings:  1
Functions:
~ +[CKCBCorecryptoECPoint groupOrderByteCountForCP:] : sha256 091ad945cc566645e04af13d686486c48b597950f73dc8c5bca1b89d8e189327 -> 54c1851fcb679a5dec99493c4b28d57af609147e6d8ce5016ab8b65f4c670b20
~ _ccrng_generate_bridge : sha256 53dfeef96b5d944628b221ac27263a4b2461b0bfe93e2736f90d920ba89c86d6 -> d16dfa55f8cac3ddf5fdc307fb7d4d04f91f8261428c8d45a38daba4cbbbde8d
~ +[SEPUtils dataFromACL:] -> _keyIsCompactRepresentable : 44 -> 340
~ _SPAKE2CtxSize -> +[SEPUtils dataFromACL:] : 40 -> 44
~ _SPAKE2Alishaz0Size -> _SPAKE2CtxSize : sha256 d9f7d1c050d00e4103f011edd42931752f02fd72f2dde1e0069d12a18fef5ed3 -> 94d786ca93be47a37de73379e0ad5fb5c829b90d7b47b11dd72640fae4875875
~ _SPAKE2GetSessionKey -> _SPAKE2Alishaz0Size : 4 -> 40
~ _AESLubyRackoffContextSize -> _SPAKE2GetSessionKey : 8 -> 4
~ _keyIsCompactRepresentable -> _AESLubyRackoffContextSize : 340 -> 8
~ _ccss_sizeof_parameters_fix : sha256 7b43d7d2edb74e2d65a87fcf331b72c133f6f501da7a3ada9eca1d2bac9baa8e -> a51eed745ee664405214a03389edfd184fe1a5b5029a19ac64fb9e36b7e974a6
~ -[CKSSShare initWithParams:x:y:] : sha256 634365bbe3f2c3063f452c96ad0d810ef3190f2325f273cccdada395019ab559 -> 8e689c839facb850a299cdb02bcc52d62b5a9cf1b018ffbb37ec37fd5387d8d6
~ -[CKSSShare initWithParams:share:] : sha256 02d5e9a33e6ee5f1425a2c40709663e87e7f0ae8d5ce6d7d168691e2cb11bb58 -> 13931f54114f4bfd178848b02bebcc898d9ab001b3e471b71fb0cb6efcaa760d
~ -[CKSSShare x] : sha256 add8bd581598a28d303ddc5b3999ef23c68eb20fc9fc47120f5b7ed8d926c072 -> 5189e19e7348fcc1bd35d30da5381a1bdc70ee921ab1a4ca7246dd7c98a57cbe
~ -[CKSSShare y] : sha256 725b14758687044c802abd82ca5fd94308dec1c28d1bab0598bb8c8312c05553 -> 511272d26eed81ef8d6d373fb5cd6aade5ade07a9252ac513bed9c46d7598bd1
~ -[CKSSShare dealloc] : sha256 9dacaa32ce7c7b5486798535069b4f707ffc9db84a2975b2f032c7773268e57e -> 3b59e938390375e70c69a1907b12bd7091fe86658f5339257416d64324f909e6
~ -[CKCBCorecryptoECScalar initWithx963Representation:group:] : sha256 a010f04d538cd96bc4f5c3b90b2f29b18f34c98049da709c4be73f685538dec7 -> 2220ec1c08f5c45826ea41db3dace852f6664eb70a59fadab7fda2bf4e771f04
~ -[CKCBCorecryptoECScalar initWithScalarPointer:forGroup:] : sha256 9f1ba5941fb529391ac40ae3710943af20cd1ae089413b337d16fda6b168b03b -> 937e54977ef619fdb64f9ece5c3cbbbd90ec56a709e7c728e9df109b16a4b726
~ -[CKCBCorecryptoECScalar x963Representation] : sha256 7e920c3ec20887dd2c9f01705a8de18a050d29cfa1d3de5fc21234db46f9e1a2 -> 54505426e69a9e3f1d344d14bc71e1c28021cb3162c49e0ff5c4e512c1d51977
~ -[CKCBCorecryptoECScalar initWithRandomScalarInGroup:] : sha256 4536231695233e64042a726b0bdaad083053da97066a7d7e69c2d88f86cad92b -> cd31a095a12248437ed007e7c774679ebb011266f88abf47810a7348f4495791
~ -[CKCBCorecryptoECScalar initWithData:inGroup:reduction:corecryptoError:] : sha256 f8094a4290061109426c41c0d82ab3c7d7cd9a0c353089af13babc6f170cc188 -> 0ec680ac1d3425bc19306e413aadf0ac348772c02c7b106d921015228bc015f7
~ -[CKCBCorecryptoECScalar serializedBigEndianScalar] : sha256 a2500406b9b3da921540d9cf74f48ffdd66fc9f81d9a8f92960c7bde154a3bce -> 943ef7be0a2e3ddcf455875976dd154fda68d8e9adcfa1c9c449ca98ab5dd767
~ -[CKCBCorecryptoECScalar mapToCurve_SSWU_RandomOracle] : sha256 fb525666db6433b7da1ffb579b9dcd099c225d799654519275bc2ffbeb1dc663 -> a87972ee4598dae42856b9f50cdf40b8a24f8ae6c571543b14941ca637571b28
~ -[CKCBCorecryptoECScalar add:corecryptoError:] : sha256 9be43fe345945c53fe696a5c0b25597cae407c3591b265b29009e214ecd180ec -> 2ac91d67c4fb5a39c0637f1f7ef76e26d4776cb9b03e85d277ded257090c174c
~ -[CKCBCorecryptoECScalar sub:corecryptoError:] : sha256 2544c54dbf3b529b21b700d0764ecfedfc040eee0db88bc41ff93bb8a39b6f80 -> 1370479f8b9b272cb130d061923dcecfe0f357b56cc7d686c6c5d4a5b3f87091
~ -[CKCBCorecryptoECScalar multiply:corecryptoError:] : sha256 7c2579a265b211c5507ea11b30fa154d5ae9c58744ce5a9123c9931378d1cf46 -> 9373b4fe5d2ab578dd6ebff2e7bd4b10e816fba870d422f367b690c1f3d144b4
~ -[CKCBCorecryptoECScalar isEqual:] : sha256 9017cc4f6868c6534d8b4a086b5526899c972a5d22b27c75447f1c8bef2a72e9 -> 88edbaae052e767aeb0fe4de1d9e38f8b2c204d97e5604cf884fa8f8006c4b31
~ -[CKCBCorecryptoECScalar inverseModOrder] : sha256 04fc15b2c0a07f630a69579e70dae177a1c2e600e2053901dcfb8209802e9fb2 -> 37198af9f7c9712c92cbbf418869483026ef9be67422e16abe4a8228fb72b519
~ -[CKCBCorecryptoECScalar dealloc] : sha256 5bb74bd3e45d915a176d011b9aa412620a461f76be657155d17249272ca62460 -> c1a97639f5ff3251390d3071f421daa1e6e4acbe308dc2829d17c466647fced5
~ _getGCMCtxSize : sha256 60d9763fd5d477142a878b776ab3d29f4e9298d045889c0d07f778a33f585e3a -> 89ca1a9b6aad8f9737fb0e9f97bb90f14646bf09a95977af4e9be1d610bbb02f
~ _getCMACContextSize : sha256 3e5fd299d97e39f92b56565f02142e71baf8a2d5b0f77e56163ef3da39ea4524 -> acbb3345b9c2fdaa71c69f697faa1d0e6ecc7741ae9057df5285a9aae9657bd3
~ _getContextSizeForECBMode : sha256 d56ac50959d794901ef32abf4988da7f5d889e3ebceba51ae8f2ebea470da7d4 -> 7cea2dbfccfc540be9c3b4a93ce7104625274bac8425b22099133e3a01cd9b80
~ -[CKCBCorecryptoECPoint pointAllocationSizeForGroup:] : sha256 3e2993ea952e0fff234f68de88c83db1376c35b48c284d217795cbfdbea81667 -> 6c57812346769baf08394412b34ac5cf5d261a6e789c6b2ba5d85df46bb0ad61
~ -[CKCBCorecryptoECPoint initPoint:onGroup:] : sha256 7f3b402fe831cef022b2e8059a8caddac4c234f434256c7b47ed751f0b0e0409 -> d5dc803f4630ca2c0750f6194383ec5508fb43b17c5533eb4da253351f2042bd
~ -[CKCBCorecryptoECPoint initFromPublicKeyBytes:inGroup:compressed:corecryptoError:] : sha256 8fad31fdb93214bb92309b03249e07dc572397adc52e4f05b341a87fd0cd25c6 -> 6ad05b9d49eefbc5b3df807f2e436641be22c78b17c5f1228653bcf509e19655
~ -[CKCBCorecryptoECPoint initWithGeneratorForCP:] : sha256 a2c5fb57aafa2fb830eecb3a893f35213b4fc1371bfecc31467617b4adba4d63 -> f591694a74cab63575c3bc904ea9347f509353188d5132b8d927189558b1f9a0
~ -[CKCBCorecryptoECPoint initWithPublicKey:] : sha256 7e4124e0f0f93a78f292cca94deea15f7d28e22e772e166f1af8287c4e0c26fe -> 080b37e6df19b265268a1e9239a2fad5718d729bdfea631f666a578659cb1003
~ -[CKCBCorecryptoECPoint isEqual:] : sha256 39989242dc17fc99e385ac641455d0e4a65d53c55f10471e4034c4afce6d2869 -> a2ad1bc116bc156cb260d839b09e9067d1e8551ea3b65c65a646402f834e4322
~ -[CKCBCorecryptoECPoint serializedPublicKey:] : sha256 7e4b79c6c476fa3230073e983aa4db07e847f60cefa9383906201822a5661ae6 -> 69f1756f4e834f92b02cd9a4134ca6375e768eb98bbda4af585f0849da927ab5
~ +[CKCBCorecryptoECPoint compressedx962PointByteCountForCurveParameters:] : sha256 ae5211aeabf278ee87854187211fa7427cfa9ed68a3a1f79c01de6c145828102 -> 6a8da81fddcb51f1731786bed91a0821086912bc43a3471b5b8041f834dda5b4
~ -[CKCBCorecryptoECPoint add:corecryptoError:] : sha256 df083fcfbfe7f018398321bf594e66db1503fd0c4af687aee609a69918200c72 -> 6d0f43b4fe349e4dd0d9bb6c82c8995d5b071c53533addc5e11e2dbe0b4e785a
~ -[CKCBCorecryptoECPoint sub:corecryptoError:] : sha256 0f889ad2745f815fbde50183e1dae03dda6102af138fc48c5427035d9e20a95e -> e4e79338a28a1827fe1b1ae03bd96af863e78a8368bfc4a85b7d59cdd5b6b81e
~ -[CKCBCorecryptoECPoint multiply:corecryptoError:] : sha256 218b4e8655bb6bcd71ac45d0fe721ef89cb3394b99e6946dde5da649476b6bbb -> 1599a8c9b0c456d7aa34357393d1e975ae30fd60f5f9a87aaeeb8fd7b248e510
~ -[CKCBCorecryptoECPoint dealloc] : sha256 a0cd3ea02472c14e2f36c8cf0a70f44fe4b3c911ba764d66f0832663720c8e99 -> 4d755ea3b8547257c1b9ca52301332f9b106469b6faf8ce9ddefae605573f395

```
