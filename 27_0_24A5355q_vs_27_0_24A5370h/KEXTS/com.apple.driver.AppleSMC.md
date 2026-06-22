## com.apple.driver.AppleSMC

> `com.apple.driver.AppleSMC`

```diff

-790.0.0.0.0
-  __TEXT.__cstring: 0x9560 sha256:05b2982575cc01873082f7e84a2d62dd7b1dfd28e3d6a24510e00759705c7e03
+793.0.0.0.0
+  __TEXT.__cstring: 0x9603 sha256:ed8c6860baa08fec654ba96646607e818ca67ce61c2a56fe521f32959a96df6b
   __TEXT.__const: 0x1f4 sha256:fbccab43e021bfb0db48b26c3cca10a4e308817209f5393d0c360d9308de5e08
   __TEXT.__os_log: 0xd97 sha256:d026d9628d50f76cc9c5c1892766a35f45fd6aae20f241db76a036d2e18a01a1
-  __TEXT_EXEC.__text: 0x2b1ac sha256:aff55c02b2799645325557ad00f0420fa0ff151cf2c5342738f0d5f01181932b
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xcc sha256:27f8f6ae5c6a5b6d366dea46af2f63270f2e6a8f9cac093726891248b55b8870
+  __TEXT_EXEC.__text: 0x2b570 sha256:e4aff8808ab8b8872f13d6701252a2bea2cec1b4f5f511091e293c523b6ce6c9
+  __TEXT_EXEC.__auth_stubs: 0xac0 sha256:ce1d864f7364fbcf85a4e5c96c245edc2bf6dbb2296d653929d24bcf788f7d20
+  __DATA.__data: 0xcc sha256:1a6d2ac775c361ec013e28a30be8bf0cf19768a9881b4c7829664edc23043a20
   __DATA.__common: 0x4e0 sha256:2c253d268f274610134a7a0131fbf74a507bb6726c1b2c37193efe293c352e2c
   __DATA.__bss: 0x110 sha256:e4d879a3407de578f579dfab4366fcea75a6649c683d9efe4f056f6505437574
-  __DATA_CONST.__mod_init_func: 0xc8 sha256:e94f45855e59b35f7a6940bb75d0c17d1a43831df5dd578c2e6ff79ff46eb487
-  __DATA_CONST.__mod_term_func: 0xb0 sha256:6553551d25ce3cde9673513eaa24d17b676ecb6553e4800c7d61ba3cd9b71cf3
-  __DATA_CONST.__const: 0x8fe8 sha256:3e917bc054f481209475fbdc4161cd132456b04bf908c2021da4e547decd4e87
-  __DATA_CONST.__kalloc_type: 0x880 sha256:a0aaab976b709d7e948eb8019449236ade7365f4c7f7f8297090bc578bf1d270
-  __DATA_CONST.__kalloc_var: 0xa0 sha256:83245d6a07780b99091ecc538b4a155137afe5a76b1717a641e03c8e9dfc47d7
-  __DATA_CONST.__auth_got: 0x560 sha256:2d6b2dfb244c4e9084a2b403fc694a8c347c32b3508663de625577b1def48f4d
-  __DATA_CONST.__got: 0x1e0 sha256:5ae12bd15e932ce1c458e7b8a4c6511f913bf5c9ce45972091c58ed68ca9c636
-  __DATA_CONST.__auth_ptr: 0x8 sha256:4584abf926b9b7cfd34a9915859b05c056bc36708f91b8d53d3a72abe8041b2a
-  UUID: F6255B25-3E17-3DEE-9FB9-A1FC9C3B568E
-  Functions: 1007
+  __DATA_CONST.__mod_init_func: 0xc8 sha256:03913f20c562a90348dfa57090aea97045e3b898391d863783af279a25ede54d
+  __DATA_CONST.__mod_term_func: 0xb0 sha256:12185ef420e48036b0be8a6ea759c195e74c589d0251f981a018a63020491b6a
+  __DATA_CONST.__const: 0x8fe8 sha256:0d07a87050ebdd3eef1ae9c0b22413ee5d7a922bcffe79f550ae847be613b8a0
+  __DATA_CONST.__kalloc_type: 0x880 sha256:fcc16c841de4a44920f3e17b670eb330b98ce329240473a71158764772b6f49b
+  __DATA_CONST.__kalloc_var: 0xa0 sha256:11a67cd23616550fdff70d85f83ec6020560f4ab833c3cbca3fcc15e2259228e
+  __DATA_CONST.__auth_got: 0x560 sha256:6ef5662575f75516223de3654f86a54b18082b12074461432bfa0c5188a8f02c
+  __DATA_CONST.__got: 0x1e0 sha256:abd2ecf9f3b39a365dfe13bef550fb2854a35c790a4b4227768254fb2c33fe15
+  __DATA_CONST.__auth_ptr: 0x8 sha256:54ca7e65c558a303bbfa22a4cf5e033d95690fa3a8d52f5d3bec2b906e6fb0eb
+  UUID: 03A35AA7-DFC9-3DA4-B7A7-B2C029CDA426
+  Functions: 1010
   Symbols:   0
-  CStrings:  1151
+  CStrings:  1157
 
CStrings:
+ "19:40:42"
+ "19:40:44"
+ "AppleSMCPMU::%s(): %s vectorNumber=%d key=%08x cmd=%08x (%s)\n"
+ "AppleSMCPMU::%s(): %s vectorNumber=%d pcIO(gpio%d) cmd=%016llx (%s)\n"
+ "AppleSMCPMU::%s(vn=%d): %s %x cmd=%08x, value=%x [%s]\n"
+ "AppleSMCPMU::%s(vn=%d): %s pcIO(gpio%d) cmd=%016llx, value=%x [%s]\n"
+ "AppleSMCPMU::%s(vn=%d): value=%x vt=%s [%s]\n"
+ "AppleSMCPMU::start: has_smc_extended_keys = %u\n"
+ "ICFG"
+ "ICLR"
+ "IENA"
+ "Jun 18 2026"
+ "_readSmcGpioKey"
+ "_writeSmcGpioKey"
+ "has_smc_extended_keys"
- "22:51:43"
- "22:51:45"
- "AppleSMCPMU::%s(): ICLR vectorNumber=%d key=%08x cmd=%08x (%s)\n"
- "AppleSMCPMU::%s(vN=%d): key=%08x IENA=%08x [%s]\n"
- "AppleSMCPMU::%s(vN=%d): key=%08x IENA=%x [%s]\n"
- "AppleSMCPMU::%s(vn=%d): ICFG %x cmd=%08x, value=%x vt=%s [%s]\n"
- "May 27 2026"
- "disableVectorHard"
- "enableVector"

```
