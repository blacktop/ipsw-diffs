## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/Versions/A/OctagonTrust`

```diff

-61901.80.19.0.0
-  __TEXT.__text: 0x20fdc
+61901.80.22.0.0
+  __TEXT.__text: 0x21104
   __TEXT.__auth_stubs: 0x4a0
-  __TEXT.__delay_helper: 0x668
+  __TEXT.__delay_helper: 0x99c
   __TEXT.__objc_methlist: 0x197c
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x7c8
-  __TEXT.__cstring: 0x1353
+  __TEXT.__cstring: 0x13ca
   __TEXT.__oslogstring: 0x293e
   __TEXT.__unwind_info: 0x560
   __TEXT.__objc_classname: 0x202
   __TEXT.__objc_methname: 0x3fbb
   __TEXT.__objc_methtype: 0x5b3
-  __TEXT.__objc_stubs: 0x2880
+  __TEXT.__objc_stubs: 0x28c0
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x90

   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x15a0
+  __AUTH_CONST.__cfstring: 0x1640
   __AUTH_CONST.__objc_const: 0x24a8
   __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x13c

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 556B16D2-7908-3313-9995-43325B40923D
+  UUID: 70AEAD71-F40A-35EB-8299-85D78355EBFF
   Functions: 566
-  Symbols:   1416
-  CStrings:  1319
+  Symbols:   1418
+  CStrings:  1329
 
Symbols:
+ _objc_msgSend$daysLeftOnRateLimit
+ _objc_msgSend$rateLimitState
Functions:
~ -[OTEscrowCheckCallResult dictionaryRepresentation] : 508 -> 636
~ -[OTEscrowCheckCallResult encodeWithCoder:] : 260 -> 316
~ -[OTEscrowCheckCallResult initWithCoder:] : 256 -> 296
~ -[OTEscrowCheckCallResult description] : 372 -> 444
CStrings:
+ "<OTEscrowCheckCallResult: needsReenroll: %@, octagonTrusted: %@, moveRequest? %@, secureTermsNeeded? %@, repairReason: %ld, repairDisabled: %@, rateLimitState: %@, daysLeftOnRateLimit: %ld>"
+ "not rate limited"
+ "rate limited"
+ "unknown"
- "<OTEscrowCheckCallResult: needsReenroll: %@, octagonTrusted: %@, moveRequest? %@, secureTermsNeeded? %@, repairReason: %ld, repairDisabled: %@>"

```
