## BasebandVoice

> `/System/Library/Audio/Plug-Ins/HAL/BasebandVoice.driver/BasebandVoice`

```diff

-1075.0.0.0.0
-  __TEXT.__text: 0x9fe8 sha256:7aeb0ac5c3dd8d8ab22fa6b3ca7acb76cf926685e07f58831b7954094e3d5e47
-  __TEXT.__auth_stubs: 0x640 sha256:32be223ea9bede00fb0db366b4034d279debf042df95389d9d0e67122dd1d9f1
+1158.0.0.0.0
+  __TEXT.__text: 0x9a20 sha256:f0b0477ebeeed48b81fb9a272ab3d6fd903e7c81d7bbbd1bc44b205e848249c4
+  __TEXT.__auth_stubs: 0x640 sha256:3e7e21b9f27926c8746420713229cf3021472982541a56347c3e1a715007a3a8
   __TEXT.__const: 0x251 sha256:1519b3da0f84eb8f0333a198c43c4f2214b5c2e73395fd6362067f4a8ae33812
-  __TEXT.__gcc_except_tab: 0x658 sha256:627596e69e83ac8251813e1452f289abe835ccac525afcd953d25d10a046adc2
-  __TEXT.__oslogstring: 0x91f sha256:e19a8c28250920c300637a3350f9beae84c71adb3ff3c9953465b239e2c2aa62
+  __TEXT.__gcc_except_tab: 0x55c sha256:86d0443fd98de578a2aec49776b7c437998cbed4f858657b722689598d22f4e5
+  __TEXT.__oslogstring: 0x91f sha256:b1a5b6700b61e42be95ab41691e2cd2f5ecfc9273c75f258bed110489541a175
   __TEXT.__cstring: 0x4cb sha256:8672e18080eb92f254ef05747c5882a70816b2c9bf63657457461f95ba3435be
-  __TEXT.__unwind_info: 0x3d0 sha256:713e7a9ffd9c8e3359925368d77e9c8711d652cdde86f58ebe011a55e82dc1de
-  __DATA_CONST.__auth_got: 0x328 sha256:80cbb12ceb628d4f36b9d2fa534791505b559b5cbf720d7ea722263d88798e17
-  __DATA_CONST.__got: 0x78 sha256:054a8f3f6d644ad779d11db47326b22c694f277244eaeb5bbef2cc0f861be4fc
-  __DATA_CONST.__const: 0x2b8 sha256:28701a3ff37098b1da8882ee5809e51472d011a4146ff25133a2c1703a60eb86
-  __DATA_CONST.__cfstring: 0x400 sha256:2daf46edae669d4ac5bd8caee0d4b9f3a5346b38eb691e9d5008e4883931c9f7
-  __DATA.__data: 0x218 sha256:711c330ed63d149d5aad716922da7010c724ae179b8169a9bf81f00398a41a16
+  __TEXT.__unwind_info: 0x380 sha256:fb975a5ef6c6747ff67e2acf7af5028dff8d435a1eefcc430f3712a8d585d0fc
+  __DATA_CONST.__const: 0x2b8 sha256:d80a6a160e1ee5310a9649224c64cca87045b22e7586655c7d70c24b0a43ea71
+  __DATA_CONST.__cfstring: 0x400 sha256:46c0a9f8ad9b70edfdb6ae31009519bc71eb3b168165c32ac16be92b882d8c6f
+  __DATA_CONST.__auth_got: 0x328 sha256:364287313e08bddcb3253a38fd4431a5afe39e5c05e1bdb6f75d152e1ac973c6
+  __DATA_CONST.__got: 0x78 sha256:299507b317fa11d49bef133528c6de2bf7554bb1eb5186d5860150a2e563c364
+  __DATA.__data: 0x218 sha256:0daaecd31c9de9062e0b6ec7158f6fd9b25301f845b24b4c78a683ef45fd8ee9
   __DATA.__bss: 0x31 sha256:78877fa898f0b4c45c9c33ae941e40617ad7c8657a307db62bc5691f92f4f60e
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libWirelessAudioIPC.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 3B4A5E16-A3EA-35DB-82CE-5EE927E22D11
+  UUID: 6310B839-87F5-3ED3-9808-8B73EC29BF02
   Functions: 125
   Symbols:   124
   CStrings:  188
CStrings:
+ "failed %{multichar}x"
+ "object %u, selector %{multichar}x, scope %{multichar}x, element %u"
+ "op %{multichar}x"
+ "op %{multichar}x, stream %u, currentTime %llu, ioBufferFrameSize %u"
+ "result %{multichar}x"
+ "result %{multichar}x, changed %zu"
+ "result %{multichar}x, dataSize %u"
+ "result %{multichar}x, isSettable %{BOOL}d"
+ "result %{multichar}x, sampleTime %lf, hostTime %llu, seed %llu"
+ "result %{multichar}x, willDo %{BOOL}d, willDoInPlace %{BOOL}d"
+ "sampleRate %lf, formatID %{multichar}x, formatFlags 0x%08x, bytesPerPacket %u, framesPerPacket %u, bytesPerFrame %u, channelsPerFrame %u, bitsPerChannel %u"
+ "success %{multichar}x"
+ "unsupported format ID %{multichar}x"
- "failed %{waipc:4cc}u"
- "object %u, selector %{waipc:4cc}u, scope %{waipc:4cc}u, element %u"
- "op %{waipc:4cc}u"
- "op %{waipc:4cc}u, stream %u, currentTime %llu, ioBufferFrameSize %u"
- "result %{waipc:4cc}u"
- "result %{waipc:4cc}u, changed %zu"
- "result %{waipc:4cc}u, dataSize %u"
- "result %{waipc:4cc}u, isSettable %{BOOL}d"
- "result %{waipc:4cc}u, sampleTime %lf, hostTime %llu, seed %llu"
- "result %{waipc:4cc}u, willDo %{BOOL}d, willDoInPlace %{BOOL}d"
- "sampleRate %lf, formatID %{waipc:4cc}u, formatFlags 0x%08x, bytesPerPacket %u, framesPerPacket %u, bytesPerFrame %u, channelsPerFrame %u, bitsPerChannel %u"
- "success %{waipc:4cc}u"
- "unsupported format ID %{waipc:4cc}u"

```
