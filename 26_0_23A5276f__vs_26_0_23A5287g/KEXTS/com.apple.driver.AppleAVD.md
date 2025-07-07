## com.apple.driver.AppleAVD

> `com.apple.driver.AppleAVD`

```diff

-899.3.0.0.0
-  __TEXT.__os_log: 0x147d7
+900.0.0.0.0
+  __TEXT.__os_log: 0x147e8
   __TEXT.__cstring: 0x5b84
   __TEXT.__const: 0x931b9
-  __TEXT_EXEC.__text: 0x58028
+  __TEXT_EXEC.__text: 0x58068
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x12dc
   __DATA.__common: 0x78

   __DATA_CONST.__const: 0x3c30
   __DATA_CONST.__kalloc_var: 0xf50
   __DATA_CONST.__kalloc_type: 0x2b00
-  UUID: AB6392B7-C33C-3CAE-85D5-A821985DF914
+  UUID: C8786EB4-BDBA-30FA-A46C-87927ED72BED
   Functions: 1828
   Symbols:   0
   CStrings:  1592
Functions:
~ __ZN22AVDSharedMemoryManager14getVPInstrFifoEjj13eAvdCodecType : 248 -> 256
~ sub_fffffff008c75af8 -> sub_fffffff008c85c70 : 56 -> 68
~ sub_fffffff008c7f8c0 -> sub_fffffff008c8fa44 : 28 -> 32
~ __ZN8AppleAVD12memCacheInitEj : 472 -> 512
CStrings:
+ "AppleAVD: WARNING: %s(): nMCSize is %u! (avdDSID = %d)\n"
- "AppleAVD: %s(): WARNING! nMCSize is %d"

```
