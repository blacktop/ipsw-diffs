## AppleAVE2FW_H13G.im4p

> `Firmware/ave/AppleAVE2FW_H13G.im4p`

```diff

 
-  __TEXT.__text: 0xdb378 sha256:fd28784c645c00501e5ce1877a0de622c7c8a5916a11f1ca04ff6e7679c513aa
-  __TEXT.__const: 0x1ea84 sha256:f660a208143d3fd2e82c3b449c4629173305dcd2a6e34460c3214ad62f0f34f7
-  __TEXT.__cstring: 0x14943 sha256:7d4e78086526415c93d3b2fe8474efa651f3ec017d3d4e7fac860cce2961ffbf
+  __TEXT.__text: 0xdbf2c sha256:2a9d0e86c56a6896b30d7c63d0074a6fc616de50e5775137b7933b957d01099b
+  __TEXT.__const: 0x1ea94 sha256:743c59aaa59707de5e57ee542564551c81a14fce3ff9be1afd1a69e1924be7d0
+  __TEXT.__cstring: 0x148ff sha256:da31bbadf84cc24112fe582ba5c915be783228c97f27cf4b7f55253098e19336
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18 sha256:090ad943e6566808412b237cc9909e160cc6544e027f16f4658130ca571f8eff
-  __DATA._rtk_patchbay: 0x211 sha256:5e100eb60fae4d6b7b518a1000a679994ba83bc4ca2ff8247b557f1d592680e9
-  __DATA.__data: 0x1090 sha256:a68410d56813304034733bcbe170ab86e2e176c1ea74bc68323f556920f532c7
-  __DATA._rtk_mtab: 0x2b8 sha256:e41e1faf5b5115c404d21c2e542e344c4b0f4085e86091f72a6f450e72727506
-  __DATA.__const: 0x37d8 sha256:4fafe84339f0d87af1de4a9167c984dc7b10be2e376274e5c0bff645a8adbda6
+  __DATA._rtk_patchbay: 0x211 sha256:0a02306f88ae1e5464ab7ac4f1ef220840693268bd88d9527fa4aa98c2cfe23f
+  __DATA.__data: 0x1090 sha256:20c220dcca1d557b705b2e5e7c787e619bc3ccdf6455ad5e990c6719d6a88dca
+  __DATA._rtk_mtab: 0x2b8 sha256:05d585bfdd7357343d9845d897a5bdcb294c3073f4d6bcca353d193dca3858bc
+  __DATA.__const: 0x37d8 sha256:11ab95e0ff51540873b559f2c773f79eb8fb6e29e2b78766434db32800556444
   __DATA._rtk_power: 0x3b8 sha256:c517018b04e689f718e8f15d61068b53442ee22aa4eefe7ec146649c05451b2a
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x1e8 sha256:ddade0037eec2bfe870a7e2ca0ef8c73274c435ca6a918ab8140b2d7b5eb36cc

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc67e0 sha256:97e2b894ee672676e83a96e0cb7b5fc8d793571b1b78a2b22f15e2ec5f1cc957
-  UUID: 2D316E06-07A1-3FD6-8791-BE9BFB35F91F
-  Functions: 1070
+  UUID: 06D67E9E-5BE9-3242-82F4-6B5F59C59F36
+  Functions: 1071
   Symbols:   1479
   CStrings:  2329
 
CStrings:
+ "(uint32_t)psSliceOffsetBuf[AVE_BufIdx_Header].iOffset + (((1152) + (32) - 1) & ~((32) - 1)) <= (uint32_t)EncCommParams.sSliceHeader.iSize"
+ "/AppleInternal/Library/BuildRoots/4~CRjhugDJia0PCW_Ej3Zq9XWFHp0LcVl0KeXY2WQ/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp"
+ "9013.12.1"
+ "Caller is /AppleInternal/Library/BuildRoots/4~CRjhugDJia0PCW_Ej3Zq9XWFHp0LcVl0KeXY2WQ/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:855"
+ "Caller is /AppleInternal/Library/BuildRoots/4~CRjhugDJia0PCW_Ej3Zq9XWFHp0LcVl0KeXY2WQ/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:860"
+ "Caller is /AppleInternal/Library/BuildRoots/4~CRjhugDJia0PCW_Ej3Zq9XWFHp0LcVl0KeXY2WQ/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:901"
+ "Caller is /AppleInternal/Library/BuildRoots/4~CRjhugDJia0PCW_Ej3Zq9XWFHp0LcVl0KeXY2WQ/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:913"
- "(shPos + 1) * (((((64) + (32) - 1) & ~((32) - 1))) > ((((1152) + (32) - 1) & ~((32) - 1))) ? ((((64) + (32) - 1) & ~((32) - 1))) : ((((1152) + (32) - 1) & ~((32) - 1)))) <= EncCommParams.sSliceHeader.iSize"
- "/AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp"
- "9012.99.0"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:853"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:858"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:899"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:911"

```
