## OctagonTrust

> `/System/Library/PrivateFrameworks/OctagonTrust.framework/OctagonTrust`

```diff

-61901.80.19.0.0
-  __TEXT.__text: 0x1eb94
+61901.80.22.0.0
+  __TEXT.__text: 0x1ecac
   __TEXT.__auth_stubs: 0x670
-  __TEXT.__delay_helper: 0x668
+  __TEXT.__delay_helper: 0x99c
   __TEXT.__objc_methlist: 0x197c
   __TEXT.__const: 0xf8
   __TEXT.__gcc_except_tab: 0x7c4
-  __TEXT.__cstring: 0x1348
+  __TEXT.__cstring: 0x13bf
   __TEXT.__oslogstring: 0x293e
   __TEXT.__unwind_info: 0x548
   __TEXT.__objc_classname: 0x202
   __TEXT.__objc_methname: 0x3fbb
   __TEXT.__objc_methtype: 0x5b3
-  __TEXT.__objc_stubs: 0x2880
+  __TEXT.__objc_stubs: 0x28c0
   __DATA_CONST.__got: 0x350
   __DATA_CONST.__const: 0x260
   __DATA_CONST.__objc_classlist: 0x90

   __DATA_CONST.__objc_selrefs: 0xf50
   __DATA_CONST.__objc_superrefs: 0x88
   __AUTH_CONST.__auth_got: 0x348
-  __AUTH_CONST.__cfstring: 0x15a0
+  __AUTH_CONST.__cfstring: 0x1640
   __AUTH_CONST.__objc_const: 0x24a8
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x18c

   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AAC566A2-0BA2-37CD-970E-E38E4F4FBCC9
+  UUID: D0351F00-251E-3818-83EB-FC5A2F13B672
   Functions: 558
-  Symbols:   1980
-  CStrings:  1319
+  Symbols:   1982
+  CStrings:  1329
 
Symbols:
+ _objc_msgSend$daysLeftOnRateLimit
+ _objc_msgSend$rateLimitState
Functions:
~ -[OTEscrowCheckCallResult dictionaryRepresentation] : 448 -> 560
~ -[OTEscrowCheckCallResult encodeWithCoder:] : 248 -> 304
~ -[OTEscrowCheckCallResult initWithCoder:] : 240 -> 280
~ -[OTEscrowCheckCallResult description] : 360 -> 432
CStrings:
+ "<OTEscrowCheckCallResult: needsReenroll: %@, octagonTrusted: %@, moveRequest? %@, secureTermsNeeded? %@, repairReason: %ld, repairDisabled: %@, rateLimitState: %@, daysLeftOnRateLimit: %ld>"
+ "not rate limited"
+ "rate limited"
+ "unknown"
- "<OTEscrowCheckCallResult: needsReenroll: %@, octagonTrusted: %@, moveRequest? %@, secureTermsNeeded? %@, repairReason: %ld, repairDisabled: %@>"

```
