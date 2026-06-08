## com.apple.driver.AppleThunderboltNHI

> `com.apple.driver.AppleThunderboltNHI`

```diff

-817.100.5.0.0
-  __TEXT.__cstring: 0xc04e sha256:f5546eeb628d99412f136e502b084939dcaca48a41b01de19f2a59285a449527
+829.0.0.0.0
+  __TEXT.__cstring: 0xc865 sha256:4f36ab86ad4cdef09a6679e2a0f583a5a87afd93d4757ce6263e28445eab4d2f
   __TEXT.__const: 0x28a20 sha256:c718c3e601053bd7cf9f6be826b69cfad6924b17d832d698dd7d6e9207b96793
-  __TEXT.__os_log: 0x74df sha256:47e88fbb5d543eb08f6474feae6f99f23677b0a20a1f7f0c7d6ba40b11e5cc0c
-  __TEXT_EXEC.__text: 0x39520 sha256:3ac18db5c7d5f575097d0ef144905b9a22e05e0f588718a6bffc8aa199b7925a
+  __TEXT.__os_log: 0x7ac2 sha256:797250a0dbfb02ea22ee8e6a8308c17959d0db722ff9ec7dec52c509ec496a51
+  __TEXT_EXEC.__text: 0x3ae38 sha256:3c8165dba6499118b945d6d7b09e23cdeaea8f21732368838dc1adcb9d19895b
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x280 sha256:a97c7695775bac335cabd3e08a9bec8a45e36ec7dbf32a44d1a664332e03b42b
+  __DATA.__data: 0x280 sha256:212a0e1efc6e2e4d3ad07b083b4643e9908dfe7206cedd3a1ccc6b2ff2d87959
   __DATA.__common: 0x478 sha256:7f079a43b601f72ccb08113d0e16422786f18f27e3e2c01d88e1b24b3b239f12
-  __DATA_CONST.__auth_got: 0x410 sha256:c0efe25d77882e7eba7d25025ef905e9d3c782dc944296f19522edc23a66f111
-  __DATA_CONST.__got: 0x148 sha256:173a9e0f2ede19599c30ee15a37f8c7e221f205777292f085e4651458564700d
-  __DATA_CONST.__mod_init_func: 0xe0 sha256:b2a49982c284e2121804493af7dc5d253c3a4fa9d0a5bcec0b08c6a0eff5c0ee
-  __DATA_CONST.__mod_term_func: 0xe0 sha256:3e8d69138419a219bfd39e2a499ec9dbf4584efe6553369e2f6b5b99caae0b42
-  __DATA_CONST.__const: 0x69f0 sha256:6fb5afb879c481a2879d5d682c62571f1b14438410843bae7785bfde64c14843
-  __DATA_CONST.__kalloc_type: 0x740 sha256:ef4551ace97ac1f45008b53b6be4b90c9e172b8e112be68a6b0d8cde6bf9258a
-  __DATA_CONST.__kalloc_var: 0x460 sha256:21b77e7feb0c0838d8ca3a47ce1dcc69a8fd128a473017241bfd9012ea56e131
-  UUID: 5407CB1A-33D2-3482-9B12-74329C0E0014
-  Functions: 952
+  __DATA_CONST.__mod_init_func: 0xe0 sha256:d21984fe2e251ac115c804155cf4da835c2ebb5d33863216c73e804429abd59d
+  __DATA_CONST.__mod_term_func: 0xe0 sha256:292787efb210f4f0e0d10a292cfc89aa64a4468843e05adc55152581bcf57c15
+  __DATA_CONST.__const: 0x69f0 sha256:f6a191859e27aed52076d3f7782b7272a45c33efc1ea914e1a84df0eea5b6e16
+  __DATA_CONST.__kalloc_type: 0x740 sha256:5d7f7dfd2ae1bf3d684b6c19194902bbc66f7594c4272797732154a9949ccd35
+  __DATA_CONST.__kalloc_var: 0x460 sha256:8decf22663c2f6be3c44d950462d8c2936d69bf25b934b101e1f44e0d832a0b4
+  __DATA_CONST.__auth_got: 0x490 sha256:21dccb1dd5e751f0971a65d40b7a8ebf38b7f7391c0db6eda763adec78d2cee3
+  __DATA_CONST.__got: 0x148 sha256:7e8a5fc3ab0e4edf060b3ccc783fbe9d6e260b7a1aae4d56c753e663c0c66dd0
+  UUID: 91520CE0-535A-398B-BA2F-BD6A14FC3C62
+  Functions: 954
   Symbols:   0
-  CStrings:  1003
+  CStrings:  1034
 
CStrings:
+ "\"AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::shouldDoubleBuffer - \" \"double buffering detected (o=0x%x, l=0x%x, seg=0x%llx)\\n\" @%s:%d"
+ "\"AppleThunderboltNHITransmitRing(%d)<%d>::shouldDoubleBuffer - \" \"double buffering detected (o=0x%x, l=0x%x, seg=0x%llx)\\n\" @%s:%d"
+ "\"AppleThunderboltNHITransmitRingGenericACIO(%d)<%d>::shouldDoubleBuffer - \" \"double buffering detected (o=0x%x, l=0x%x, seg=0x%llx)\\n\" @%s:%d"
+ "%lldus AppleThunderboltHALGenericACIO::unpoweredStart - bootargs: acio = 0x%08x, tb_poll_interrupts = %d\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - FrameList cache STORE: cmd=%p listIdx=%u frameIdx=%u addr=0x%llx details=0x%x\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - FrameList cache lookup: listIdx=%u frameIdx=%u cache_hit=%d\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - frame (currentFrameListIndex=0x%x,fCurrentFrameListFrameIndex=0x%llx) frame_length=0x%x total command (o=0x%x,l=0x%x)\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules EOF PDF - setting EOF to EOF index = 0x%llx - 0x%x\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules EOF PDF - setting EOF to Mid EOF index = 0x%llx - 0x%x\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules Mid PDF - setting SOF to MidSOF index = 0x%llx - 0x%x\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules Mid PDF - setting SOF to SOF index = 0x%llx - 0x%x\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List  Mid PDF - setting SOF to MidSOF - 0x%x\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List EOF PDF - setting EOF to EOF - 0x%x\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List EOF PDF - setting EOF to Mid EOF - 0x%x\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List Mid PDF - setting SOF to SOF - 0x%x\n"
+ "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules setMidPDFRules details - 0x%x\n"
+ "121112222221121111222222112"
+ "12111222222112111122222211221"
+ "22:46:06"
+ "AppleThunderboltNHIReceiveRingGenericACIO.cpp"
+ "AppleThunderboltNHITransmitRing.cpp"
+ "AppleThunderboltNHITransmitRingGenericACIO.cpp"
+ "May 27 2026"
+ "tb_poll_interrupts"
- "%lldus AppleThunderboltHALGenericACIO::unpoweredStart - bootargs: acio = 0x%08x\n"
- "12111222222112111122222112"
- "1211122222211211112222211221"
- "20:24:04"
- "Apr 23 2026"

```
