## com.apple.driver.AppleThunderboltNHI

> `com.apple.driver.AppleThunderboltNHI`

```diff

-817.100.5.0.0
-  __TEXT.__cstring: 0xc04e
+829.0.0.0.0
+  __TEXT.__cstring: 0xc865
   __TEXT.__const: 0x28a20
-  __TEXT.__os_log: 0x74df
-  __TEXT_EXEC.__text: 0x39520
+  __TEXT.__os_log: 0x7ac2
+  __TEXT_EXEC.__text: 0x3ae38
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x280
   __DATA.__common: 0x478
-  __DATA_CONST.__auth_got: 0x410
-  __DATA_CONST.__got: 0x148
   __DATA_CONST.__mod_init_func: 0xe0
   __DATA_CONST.__mod_term_func: 0xe0
   __DATA_CONST.__const: 0x69f0
   __DATA_CONST.__kalloc_type: 0x740
   __DATA_CONST.__kalloc_var: 0x460
-  UUID: 5407CB1A-33D2-3482-9B12-74329C0E0014
-  Functions: 952
+  __DATA_CONST.__auth_got: 0x490
+  __DATA_CONST.__got: 0x148
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
