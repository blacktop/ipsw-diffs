## exclave_sharedcache

> `Firmware/image4/exclavecore_bundle.t8150.RELEASE.im4p/exclave_sharedcache`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_entry`
- `__DATA.__TIGHTBEAM_VT`
- `__DATA.__data`
- `__DATA.__const`
- `__DATA.__mod_init_func`
- `__DATA.__auth_ptr`
- `__DATA.__shared_cache`
- `__DATA.__got`
- `__DATA.__bss`
- `__DATA.__common`
- `__PDATA.__data`
- `__PDATA.__const`
- `__PDATA.__auth_ptr`
- `__PDATA.__bss`
- `__PDATA.__common`

```diff

 1148.120.6.0.0
-  __TEXT.__text: 0xd2cee8
+  __TEXT.__text: 0xd2d350
   __TEXT.__lcxx_override: 0x34c
   __TEXT.__cstring: 0x96d41
   __TEXT.__const: 0x17fec4

   __TEXT.__term_offsets: 0x0
   __TEXT.__thread_starts: 0x0
   __TEXT.__chain_fixups: 0x118
-  __TEXT.__eh_frame: 0x73638
+  __TEXT.__eh_frame: 0x735c8
   __DATA.__TIGHTBEAM_VT: 0x11a0
   __DATA.__TIGHTBEAM: 0x470
   __DATA.__data: 0x45488
Functions:
~ sub_8170a80 : 392 -> 468
~ sub_8170d4c -> sub_8170d98 : 264 -> 440
~ sub_8170f58 -> sub_8171054 : 208 -> 216
~ sub_8171028 -> sub_817112c : 244 -> 240
~ sub_817111c -> sub_817121c : 244 -> 240
~ sub_8171210 -> sub_817130c : 244 -> 240
~ sub_8171304 -> sub_81713fc : 244 -> 240
~ sub_81713f8 -> sub_81714ec : 244 -> 240
~ sub_81714ec -> sub_81715dc : 244 -> 240
~ sub_81715e0 -> sub_81716cc : 244 -> 240
~ sub_8171a24 -> sub_8171b0c : 3104 -> 2676
~ sub_8172644 -> sub_8172580 : 184 -> 188
~ sub_8172898 -> sub_81727d8 : 388 -> 392
~ sub_8172ae0 -> sub_8172a24 : 208 -> 220
~ sub_8172bb0 -> sub_8172b00 : 220 -> 196
~ sub_8172c8c -> sub_8172bc4 : 204 -> 180
~ sub_8173204 -> sub_8173124 : 364 -> 440
~ sub_8173a14 -> sub_8173980 : 1744 -> 1896
~ sub_83a1be0 -> sub_83a1be4 : 1512 -> 1440
~ sub_83a3cf8 -> sub_83a3cb4 : 228 -> 216
~ sub_83a3ddc -> sub_83a3d8c : 208 -> 232
~ sub_83a4040 -> sub_83a4008 : 204 -> 212
~ sub_83a410c -> sub_83a40dc : 244 -> 268
~ sub_83a43ec -> sub_83a43d4 : 236 -> 264
~ sub_83a44d8 -> sub_83a44dc : 300 -> 324
~ sub_83a47dc -> sub_83a47f8 : 260 -> 276
~ sub_83a48f8 -> sub_83a4924 : 240 -> 264
~ sub_83a4a40 -> sub_83a4a84 : 264 -> 284
~ sub_83a4b48 -> sub_83a4ba0 : 212 -> 236
~ sub_83a4ee0 -> sub_83a4f50 : 196 -> 220
~ sub_845632c -> sub_84563b4 : 664 -> 720
~ sub_84565c4 -> sub_8456684 : 1652 -> 1604
~ sub_845702c -> sub_84570bc : 112 -> 120
~ sub_845709c -> sub_8457134 : 212 -> 196
~ sub_8457170 -> sub_84571f8 : 288 -> 320
~ sub_8458984 -> sub_8458a2c : 228 -> 216
~ sub_8458a68 -> sub_8458b04 : 208 -> 232
~ sub_8458ccc -> sub_8458d80 : 204 -> 212
~ sub_8458d98 -> sub_8458e54 : 244 -> 268
~ sub_8459094 -> sub_8459168 : 236 -> 264
~ sub_8459180 -> sub_8459270 : 300 -> 324
~ sub_8459484 -> sub_845958c : 260 -> 276
~ sub_8459588 -> sub_84596a0 : 236 -> 260
~ sub_84596cc -> sub_84597fc : 264 -> 284
~ sub_84597d4 -> sub_8459918 : 212 -> 236
~ sub_8459b6c -> sub_8459cc8 : 196 -> 220
~ sub_8aad180 -> sub_8aad2f4 : 1296 -> 1292
~ sub_8b4a97c -> sub_8b4aaec : 280 -> 356
~ sub_8b4aa94 -> sub_8b4ac50 : 600 -> 680
~ sub_8b4ad64 -> sub_8b4af70 : 272 -> 348
~ sub_8b4ae74 -> sub_8b4b0cc : 280 -> 356
~ sub_8b4cfbc -> sub_8b4d260 : 172 -> 200
~ sub_8b4d068 -> sub_8b4d328 : 204 -> 236
~ sub_8b4d37c -> sub_8b4d65c : 188 -> 204
~ sub_8b4d438 -> sub_8b4d728 : 224 -> 248
~ sub_8b4d6b4 -> sub_8b4d9bc : 204 -> 208
~ sub_8b4d780 -> sub_8b4da8c : 244 -> 272
~ sub_8b51278 -> sub_8b515a0 : 696 -> 752
~ sub_8b51530 -> sub_8b51890 : 792 -> 852
~ sub_8b53100 -> sub_8b5349c : 228 -> 216
~ sub_8b531e4 -> sub_8b53574 : 208 -> 232
~ sub_8b53448 -> sub_8b537f0 : 204 -> 212
~ sub_8b53514 -> sub_8b538c4 : 244 -> 268
~ sub_8b53810 -> sub_8b53bd8 : 236 -> 264
~ sub_8b538fc -> sub_8b53ce0 : 300 -> 324
~ sub_8b53c00 -> sub_8b53ffc : 260 -> 276
~ sub_8b53d04 -> sub_8b54110 : 236 -> 260
~ sub_8b53e48 -> sub_8b5426c : 264 -> 284
~ sub_8b53f50 -> sub_8b54388 : 212 -> 236
~ sub_8b542e8 -> sub_8b54738 : 196 -> 220
CStrings:
+ "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Sat Jul 11 15:52:20 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
+ "Build Date: Sat Jul 11 15:40:27 PDT 2026"
+ "ExclaveOS Image4 Framework Version 7.0.0: Sat Jul 11 15:52:20 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
+ "Sat Jul 11 16:23:59 PDT 2026"
- "@(#)VERSION:ExclaveOS Image4 Framework Version 7.0.0: Thu Jul  9 23:29:21 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "Build Date: Wed Jul  8 23:43:39 PDT 2026"
- "ExclaveOS Image4 Framework Version 7.0.0: Thu Jul  9 23:29:21 PDT 2026; root:/ExclaveImage4/RELEASE_ARM64E"
- "Fri Jul 10 00:06:45 PDT 2026"
```
