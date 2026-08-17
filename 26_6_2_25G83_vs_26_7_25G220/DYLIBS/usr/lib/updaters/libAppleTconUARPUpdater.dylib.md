## libAppleTconUARPUpdater.dylib

> `/usr/lib/updaters/libAppleTconUARPUpdater.dylib`

```diff

-1345.160.8.0.1
-  __TEXT.__text: 0x40244
+1345.160.9.700.1
+  __TEXT.__text: 0x40360
   __TEXT.__auth_stubs: 0x370
   __TEXT.__objc_methlist: 0x3e34
   __TEXT.__cstring: 0x3c93
   __TEXT.__const: 0x90
-  __TEXT.__oslogstring: 0x1398
+  __TEXT.__oslogstring: 0x13db
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x1188
+  __TEXT.__unwind_info: 0x1190
   __TEXT.__objc_classname: 0x145b
   __TEXT.__objc_methname: 0x4645
   __TEXT.__objc_methtype: 0x947

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1749
-  Symbols:   3494
-  CStrings:  1839
+  Functions: 1752
+  Symbols:   3495
+  CStrings:  1840
 
Symbols:
+ _OUTLINED_FUNCTION_18
Functions:
~ -[UARPSuperBinaryPayloadLayer3 decompressPayload] : 1056 -> 1020
+ _OUTLINED_FUNCTION_12
~ -[UARPSuperBinaryPayloadLayer3 decompressPayload].cold.1 : 88 -> 136
~ -[UARPSuperBinaryPayloadLayer3 decompressPayload].cold.2 : 88 -> 164
- -[UARPSuperBinaryPayloadLayer3 expandPayloadDictionary:].cold.4
+ -[UARPSuperBinaryPayloadLayer3 expandPayloadDictionary:].cold.3
+ -[UARPSuperBinaryPayloadLayer3 expandPayloadDictionaryData:].cold.1
+ -[UARPSuperBinaryPayloadLayer3 composePersonalizedFTAB].cold.1
CStrings:
+ "%s: uncompressedLength (%u) exceeds decompressionBuffer size (%lu)"
```
