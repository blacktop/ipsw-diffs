## com.apple.driver.ApplePearlSEPDriver

> `com.apple.driver.ApplePearlSEPDriver`

```diff

-873.60.2.0.0
+877.100.21.0.0
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0xa847
-  __TEXT.__os_log: 0x48ed
-  __TEXT_EXEC.__text: 0x403d0
+  __TEXT.__cstring: 0xa992
+  __TEXT.__os_log: 0x498f
+  __TEXT_EXEC.__text: 0x3d2bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8

   __DATA_CONST.__const: 0x2050
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: FC3D928E-90A5-38FC-967B-123AA66FE5E0
-  Functions: 623
+  UUID: FB215959-4D22-3E1B-B57A-5427B22FE57F
+  Functions: 655
   Symbols:   0
-  CStrings:  1668
+  CStrings:  1677
 
CStrings:
+ "%s: Dummy Mode enrollment for userID:%d, err:0x%x\n"
+ "%s: Dummy Mode match for userID:%d, err:0x%x\n"
+ "%s: Skipping camera power-on for attention sequence in SFD mode\n"
+ "/Library/Caches/com.apple.xbs/05BC2D32-1B21-4498-8369-DABC4A1C2388/TemporaryDirectory.TPxQAa/Sources/Pearl_Kernel/ApplePearlSEPDriver/ApplePearlSEPDriver.cpp"
+ "/Library/Caches/com.apple.xbs/05BC2D32-1B21-4498-8369-DABC4A1C2388/TemporaryDirectory.TPxQAa/Sources/Pearl_Kernel/ApplePearlSEPDriver/ApplePearlUserClient.cpp"
+ "/Library/Caches/com.apple.xbs/05BC2D32-1B21-4498-8369-DABC4A1C2388/TemporaryDirectory.TPxQAa/Sources/Pearl_Kernel/ApplePearlSEPDriver/IOPearlFrameSupport.cpp"
+ "121111121222121211212111111111111111111111211211222222221222112222222212111211111212222111212111222222222222211222222222212211121112112221112222222122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222212222222212212222222212122222222221222122222222222222221212112222222212212221221111222222221121222231112221221221111111111121122211122"
+ "HandleDummyMode"
+ "HandleDummyModeCommand"
+ "IOBioUtils::isInternal() || !enrollInit->dummyEnrollment"
+ "IOBioUtils::isInternal() || !matchInit->dummyMatch"
+ "_dcnKernelsLoaded == kBoolNotSet"
+ "_dummyModeOperation"
+ "payloadSize >= sizeof(*request)"
- "/Library/Caches/com.apple.xbs/Sources/Pearl_Kernel/ApplePearlSEPDriver/ApplePearlSEPDriver.cpp"
- "/Library/Caches/com.apple.xbs/Sources/Pearl_Kernel/ApplePearlSEPDriver/ApplePearlUserClient.cpp"
- "/Library/Caches/com.apple.xbs/Sources/Pearl_Kernel/ApplePearlSEPDriver/IOPearlFrameSupport.cpp"
- "12111112122212121121211111111111111111111121121122222222122211222222221211121111121222211121211122222222222221122222222221221112111211222111222222212222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222221222222221221222222221212222222222122212222222222222222121211222222221221222122111122222222112122223111222122122111111111112112221112"
- "The offset of the pointer inside its valid memory range can't be represented using int32_t"

```
