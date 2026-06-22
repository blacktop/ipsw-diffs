## AppleAVE2FW_H13S.im4p

> `Firmware/ave/AppleAVE2FW_H13S.im4p`

```diff

 
-  __TEXT.__text: 0xdfd08 sha256:a0bf2812f727f9eaa2d58f64f23c290e077ef410204fb4000f17a56ad092bed4
-  __TEXT.__const: 0x21ff4 sha256:76fcac84a4426ccde9ad11aca96e7301fe88a9a471fb1945d0c797be3bbec621
-  __TEXT.__cstring: 0x149fe sha256:0fa34549b72807b101af102cec48f4713df1ac862f2c5b91de7030e1ffde0517
+  __TEXT.__text: 0xe05ec sha256:33151be9dc2665972a85fa32ce57c7f1612bb9a8914147f5122068d022f70777
+  __TEXT.__const: 0x22004 sha256:477c90ed989e51f1f74843b287767b48a5cc9eac9c01fb4b36cad8df08644000
+  __TEXT.__cstring: 0x149ba sha256:5b456a0890da517f47cb0c5537d8532231e19a824103d3fe0dad537390ff5cc9
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18 sha256:5af910100fc38755cb6998ff61f64c35301482fa7636e4c898b253bf37bf8a77
-  __DATA._rtk_patchbay: 0x211 sha256:27d2b2d804c739f705705bed4856237e74c0da68a235d4aa63668f69c61cd779
-  __DATA.__data: 0x1090 sha256:1ad89278f330c58321e6f33ef6fbe3c16cd3e7cee10f1f292ca0a4345f057916
-  __DATA._rtk_mtab: 0x2b8 sha256:ce2ae5aaf3a81941cec4a561ae684586469d14a470af11e86d7474a75daa96e4
-  __DATA.__const: 0x3a60 sha256:7ca31de8fd3860752afcb1a877ade7a1196734bf9f547f2a37e4058c29cdb289
+  __DATA._rtk_patchbay: 0x211 sha256:a5b9f384b5d2b4c19034465ab01abb46158770db31b264ee46e80cd1bd0fd58f
+  __DATA.__data: 0x1090 sha256:e747dd04da58e27fb82306550f801d276a7e17b59a230ed5cc3979f4c4301ba4
+  __DATA._rtk_mtab: 0x2b8 sha256:927839ec2cd03c419df5fe702af01b4a053c6fe1aa8080f78d291ed3f7c0f9d5
+  __DATA.__const: 0x3a60 sha256:0cfecfe548fe6cfcea09e49ad0b050cf5f89d14ff91a2a040ce11c72559c3ce1
   __DATA._rtk_power: 0x3b8 sha256:e20d675ab78a680c7ad177a29a6acd99cdeccbcd997246017c5358ea48bb0579
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x1e8 sha256:ddade0037eec2bfe870a7e2ca0ef8c73274c435ca6a918ab8140b2d7b5eb36cc

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc67e0 sha256:97e2b894ee672676e83a96e0cb7b5fc8d793571b1b78a2b22f15e2ec5f1cc957
-  UUID: 1DCF3C63-9C94-3E0E-AD0F-36D9FC933F17
-  Functions: 1096
+  UUID: 989EBAB5-6E27-32B2-9CA8-EA1E5EDD69AA
+  Functions: 1097
   Symbols:   1518
   CStrings:  2351
 
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
