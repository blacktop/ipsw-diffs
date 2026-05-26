## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-371.120.3.0.0
+371.160.2.0.0
   __TEXT.__text: 0x1a4dc
   __TEXT.__auth_stubs: 0x14e0
   __TEXT.__objc_stubs: 0x620
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0xa479
+  __TEXT.__cstring: 0xa48b
   __TEXT.__const: 0x6e8
   __TEXT.__objc_methname: 0x4cd
   __TEXT.__objc_classname: 0xc

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  UUID: EAB20091-6125-3298-B60E-C204AF1C0443
+  UUID: 62F98642-932B-32D6-ACFD-E5942715F55E
   Functions: 277
   Symbols:   385
   CStrings:  1428
CStrings:
+ "removeExcept /(ANE|AOP|AOP2|AVE|GFX|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware))\\.img4/"
+ "removeExcept /(ANE|AOP|AOP2|AVE|GFX|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware|ExclaveOSVolume|ExclaveOSIntegrityCatalog|ExclaveOSTrustCache|cL4))\\.img4/ /Ap,ExclaveOS.dmg/"
- "removeExcept /(ANE|GFX|AVE|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware))\\.img4/"
- "removeExcept /(ANE|GFX|AVE|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware|ExclaveOSVolume|ExclaveOSIntegrityCatalog|ExclaveOSTrustCache|cL4))\\.img4/ /Ap,ExclaveOS.dmg/"

```
