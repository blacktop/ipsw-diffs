## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

 56.0.0.0.0
-  __TEXT.__text: 0x24394
+  __TEXT.__text: 0x26094
   __TEXT.__auth_stubs: 0x800
   __TEXT.__objc_stubs: 0xa00
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x31c
   __TEXT.__gcc_except_tab: 0x2598
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x5773
+  __TEXT.__cstring: 0x5869
   __TEXT.__objc_classname: 0x55
   __TEXT.__objc_methname: 0xb71
   __TEXT.__objc_methtype: 0x657
-  __TEXT.__oslogstring: 0x8d2
-  __TEXT.__unwind_info: 0x710
+  __TEXT.__oslogstring: 0x99e
+  __TEXT.__unwind_info: 0x738
   __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x558

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 54B0AF17-7241-36EB-8C52-918D918FE25A
-  Functions: 439
-  Symbols:   407
-  CStrings:  1414
+  UUID: ABDF7AC7-584E-3BBC-8EA4-D70E8B195B5A
+  Functions: 462
+  Symbols:   411
+  CStrings:  1432
 
Symbols:
+ _generateAndVerifyAriesHostAuthorization
+ _getAttestationToPDAK
+ _getDummy0PSDData
+ _getPDAK
CStrings:
+ "(outData->attestationLength > 0) && (outData->attestationLength <= (16 * 1024))"
+ "att"
+ "attestation && attestationLength"
+ "clearBuffer"
+ "encryptedBuffer"
+ "generateAndVerifyAriesHostAuthorization\n"
+ "generateAndVerifyAriesHostAuthorization -> %d\n"
+ "getAttestationToPDAK\n"
+ "getAttestationToPDAK -> %d\n"
+ "getDummy0PSDData\n"
+ "getDummy0PSDData -> %d\n"
+ "getPDAK\n"
+ "getPDAK -> %d\n"
+ "outData"
+ "outDataLength"
+ "pdak && pdakLength"
+ "replySize == sizeof(*outData)"
+ "replySize >= sizeof(*outData)"

```
