## com.apple.driver.AppleThunderboltNHI

> `com.apple.driver.AppleThunderboltNHI`

```diff

-829.0.0.0.0
+817.100.5.0.0
   __TEXT.__const: 0x28a18 sha256:f9775d59536e9d7c025de70f9fb7eb03b779287ec7f0e8d47a33f4882bc319d1
-  __TEXT.__cstring: 0xc88b sha256:a127a0effa0e852008493a6a713f2b77dade743b033c6f2d11d199e2f6839f58
-  __TEXT.__os_log: 0x7ac2 sha256:10b63536ffa086d5aeb0806fb244b65c04e8f51e445bfd5fb68458cb9570edd1
-  __TEXT_EXEC.__text: 0x3c598 sha256:f93182fd831d618e1939ffd8706ff265210453ab425223a5a68b45451d0ace6b
+  __TEXT.__cstring: 0xc074 sha256:d90e80c11b9496a6cb33834091c3a908e1fa1340562a18463ed955dd3b8b685a
+  __TEXT.__os_log: 0x74df sha256:9c17c244386f8d9729e7c6a519458c8d9c2173b44aa356d5281142a7e503aa00
+  __TEXT_EXEC.__text: 0x3ac18 sha256:2b48fd8d9c8822d9ddef9fbacea49e5fba30241d45875e02e4666ac243a565cc
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x280 sha256:83067a258ef884fab0d91eb9cec810dbda4914f073d6031c30110e8e9d7dd8ed
+  __DATA.__data: 0x280 sha256:9ea822ee98776854f3c1497a4295d87890948910288f0f450f5e47742a894bfb
   __DATA.__common: 0x478 sha256:7f079a43b601f72ccb08113d0e16422786f18f27e3e2c01d88e1b24b3b239f12
-  __DATA_CONST.__mod_init_func: 0xe0 sha256:a217c620282591deb323fc2be4a78bcfaba77d6c05afe37dc9cc5c44069fe83e
-  __DATA_CONST.__mod_term_func: 0xe0 sha256:217cbb0847bdac972222023e456ee8d95c0589cf6aa6d4e607d041923d3725b5
-  __DATA_CONST.__const: 0xacf0 sha256:cc7dd832a20507444f722ae0963c310bb9848200014190772f016a430b967e8d
-  __DATA_CONST.__kalloc_type: 0x740 sha256:4723beff0138655821ee10a102eb792c0d35e2c02d1405d110c3d305cd09dc5f
-  __DATA_CONST.__kalloc_var: 0x460 sha256:467bef73eff70f96f337b4de1d3b007925c7ae1da6bfa5c71a2690099bde00eb
-  __DATA_CONST.__auth_got: 0x490 sha256:97b61749888ac55d642600216837806c108edafac5ece884e59abc146bcfb2f6
-  __DATA_CONST.__got: 0x148 sha256:1d29e08fd75f03f86dd06b750f5621e01e98b6d02179221806a025e9a76829df
-  UUID: CA5CB5AA-F5D0-37D5-96AB-20A73FF0A963
-  Functions: 954
-  Symbols:   2161
-  CStrings:  1034
+  __DATA_CONST.__auth_got: 0x410 sha256:461ec77a54ed354383edcfdd367cfdc745939148d27f1c50cdeed8051a7acda3
+  __DATA_CONST.__got: 0x148 sha256:d88f01bbfdc5fc2ab864e483412fa3ce1f69281de79735aeede3f66c7f759a04
+  __DATA_CONST.__mod_init_func: 0xe0 sha256:62cf787804b18aa710198ec8b694f001e80b425941f29de1438c0c2de45b13a4
+  __DATA_CONST.__mod_term_func: 0xe0 sha256:7f76c7dc7adfd22d59b7653e658b35819dc95ef135fe0026d1924f16bb488e52
+  __DATA_CONST.__const: 0xacf0 sha256:fbc344ba6fbc7b080f2a327075301abd2e6cdafd1d3496052b432356e4c4e2e3
+  __DATA_CONST.__kalloc_type: 0x740 sha256:2c2b79bea799194a4b8a52db1f8e68f23e66d35844612be5cdd0942d96028af5
+  __DATA_CONST.__kalloc_var: 0x460 sha256:7e87d4fbafc974006fe16f0c88af6aa5934f53a46342f670ea97ebaebf8896ad
+  UUID: 2864079B-2018-3CB8-BD01-BCC9B1C9FBA7
+  Functions: 952
+  Symbols:   2131
+  CStrings:  1003
 
Symbols:
+ __ZN31AppleThunderboltNHITransmitRing18getNextFrameLengthEPy
+ __ZZN41AppleThunderboltNHIReceiveRingGenericACIO19createDoubleBuffersEvE20kalloc_type_view_198
+ __ZZN42AppleThunderboltNHITransmitRingGenericACIO19createDoubleBuffersEvE20kalloc_type_view_227
- __ZN18IOTimerEventSource16timerEventSourceEP8OSObjectPFvS1_PS_E
- __ZN22IOThunderboltFrameList14getSizeAtIndexEjPy
- __ZN22IOThunderboltFrameList23getSizeAndOffsetAtIndexEjPyS0_
- __ZN22IOThunderboltFrameList8getCountEv
- __ZN28IOThunderboltTransmitCommand12hasFrameListEv
- __ZN28IOThunderboltTransmitCommand18getEOFForFrameListEj
- __ZN28IOThunderboltTransmitCommand18getSOFForFrameListEj
- __ZN28IOThunderboltTransmitCommand21getFrameListDescCacheEjj
- __ZN28IOThunderboltTransmitCommand21getMidEOFForFrameListEj
- __ZN28IOThunderboltTransmitCommand21getMidSOFForFrameListEj
- __ZN28IOThunderboltTransmitCommand21setFrameListDescCacheEPNS_18TxBufferDescriptorEjj
- __ZN28IOThunderboltTransmitCommand25getPDFMiddleModeSupportedEv
- __ZN28IOThunderboltTransmitCommand39getProducerUpdateModeForCommandOverrideEv
- __ZN28IOThunderboltTransmitCommand39setProducerUpdateModeForCommandOverrideEb
- __ZN28IOThunderboltTransmitCommand9getMidEOFEv
- __ZN28IOThunderboltTransmitCommand9getMidSOFEv
- __ZN30AppleThunderboltHALGenericACIO26interruptPollTimerCallbackEP18IOTimerEventSource_vfpthunk_
- __ZN31AppleThunderboltNHITransmitRing14setMidPDFRulesEPN28IOThunderboltTransmitCommand18TxBufferDescriptorEbby
- __ZN31AppleThunderboltNHITransmitRing18getNextFrameLengthEPyPbS1_
- __ZZN31AppleThunderboltNHITransmitRing14setMidPDFRulesEPN28IOThunderboltTransmitCommand18TxBufferDescriptorEbbyE11_os_log_fmt
- __ZZN31AppleThunderboltNHITransmitRing14setMidPDFRulesEPN28IOThunderboltTransmitCommand18TxBufferDescriptorEbbyE11_os_log_fmt_0
- __ZZN31AppleThunderboltNHITransmitRing14setMidPDFRulesEPN28IOThunderboltTransmitCommand18TxBufferDescriptorEbbyE11_os_log_fmt_1
- __ZZN31AppleThunderboltNHITransmitRing14setMidPDFRulesEPN28IOThunderboltTransmitCommand18TxBufferDescriptorEbbyE11_os_log_fmt_2
- __ZZN31AppleThunderboltNHITransmitRing14setMidPDFRulesEPN28IOThunderboltTransmitCommand18TxBufferDescriptorEbbyE11_os_log_fmt_3
- __ZZN31AppleThunderboltNHITransmitRing14setMidPDFRulesEPN28IOThunderboltTransmitCommand18TxBufferDescriptorEbbyE11_os_log_fmt_4
- __ZZN31AppleThunderboltNHITransmitRing14setMidPDFRulesEPN28IOThunderboltTransmitCommand18TxBufferDescriptorEbbyE11_os_log_fmt_5
- __ZZN31AppleThunderboltNHITransmitRing14setMidPDFRulesEPN28IOThunderboltTransmitCommand18TxBufferDescriptorEbbyE11_os_log_fmt_6
- __ZZN31AppleThunderboltNHITransmitRing14setMidPDFRulesEPN28IOThunderboltTransmitCommand18TxBufferDescriptorEbbyE11_os_log_fmt_7
- __ZZN31AppleThunderboltNHITransmitRing19writeNextDescriptorEPbS0_E11_os_log_fmt_3
- __ZZN31AppleThunderboltNHITransmitRing19writeNextDescriptorEPbS0_E11_os_log_fmt_4
- __ZZN31AppleThunderboltNHITransmitRing19writeNextDescriptorEPbS0_E11_os_log_fmt_5
- __ZZN41AppleThunderboltNHIReceiveRingGenericACIO19createDoubleBuffersEvE20kalloc_type_view_214
- __ZZN42AppleThunderboltNHITransmitRingGenericACIO19createDoubleBuffersEvE20kalloc_type_view_243
CStrings:
+ "%lldus AppleThunderboltHALGenericACIO::unpoweredStart - bootargs: acio = 0x%08x\n"
+ "/AppleInternal/Library/BuildRoots/4~CRefugAPnuF-h-Q8lrdLUl8lIrPgWZ5TRVWRtWM/Library/Caches/com.apple.xbs/TemporaryDirectory.CGBU4f/Sources/AppleThunderboltNHI/AppleThunderboltNHIDARTVMAllocator.cpp"
+ "12111222222112111122222112"
+ "1211122222211211112222211221"
+ "22:44:19"
+ "Jun  9 2026"
- "\"AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::shouldDoubleBuffer - \" \"double buffering detected (o=0x%x, l=0x%x, seg=0x%llx)\\n\" @%s:%d"
- "\"AppleThunderboltNHITransmitRing(%d)<%d>::shouldDoubleBuffer - \" \"double buffering detected (o=0x%x, l=0x%x, seg=0x%llx)\\n\" @%s:%d"
- "\"AppleThunderboltNHITransmitRingGenericACIO(%d)<%d>::shouldDoubleBuffer - \" \"double buffering detected (o=0x%x, l=0x%x, seg=0x%llx)\\n\" @%s:%d"
- "%lldus AppleThunderboltHALGenericACIO::unpoweredStart - bootargs: acio = 0x%08x, tb_poll_interrupts = %d\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - FrameList cache STORE: cmd=%p listIdx=%u frameIdx=%u addr=0x%llx details=0x%x\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - FrameList cache lookup: listIdx=%u frameIdx=%u cache_hit=%d\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - frame (currentFrameListIndex=0x%x,fCurrentFrameListFrameIndex=0x%llx) frame_length=0x%x total command (o=0x%x,l=0x%x)\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules EOF PDF - setting EOF to EOF index = 0x%llx - 0x%x\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules EOF PDF - setting EOF to Mid EOF index = 0x%llx - 0x%x\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules Mid PDF - setting SOF to MidSOF index = 0x%llx - 0x%x\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules Mid PDF - setting SOF to SOF index = 0x%llx - 0x%x\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List  Mid PDF - setting SOF to MidSOF - 0x%x\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List EOF PDF - setting EOF to EOF - 0x%x\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List EOF PDF - setting EOF to Mid EOF - 0x%x\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List Mid PDF - setting SOF to SOF - 0x%x\n"
- "%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules setMidPDFRules details - 0x%x\n"
- "/AppleInternal/Library/BuildRoots/4~CQdZugAygdJy3BhVwJPM_92D-3ZMpEoB2zIrNmI/Library/Caches/com.apple.xbs/TemporaryDirectory.t5NSZs/Sources/AppleThunderboltNHI/AppleThunderboltNHIDARTVMAllocator.cpp"
- "01:30:10"
- "121112222221121111222222112"
- "12111222222112111122222211221"
- "AppleThunderboltNHIReceiveRingGenericACIO.cpp"
- "AppleThunderboltNHITransmitRing.cpp"
- "AppleThunderboltNHITransmitRingGenericACIO.cpp"
- "May 27 2026"
- "tb_poll_interrupts"

```
