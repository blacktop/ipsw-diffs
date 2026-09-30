## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

```diff

-320.80.3.0.0
-  __TEXT.__text: 0x15af8
+320.100.12.0.2
+  __TEXT.__text: 0x15c08
   __TEXT.__auth_stubs: 0x1400
   __TEXT.__objc_stubs: 0x620
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x9015
-  __TEXT.__const: 0x688
+  __TEXT.__cstring: 0x91f9
+  __TEXT.__const: 0x6c8
   __TEXT.__objc_methname: 0x478
   __TEXT.__objc_classname: 0xc
   __TEXT.__objc_methtype: 0x3a
-  __TEXT.__gcc_except_tab: 0x110
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__gcc_except_tab: 0x114
+  __TEXT.__unwind_info: 0x3c8
   __DATA_CONST.__auth_got: 0xa10
   __DATA_CONST.__got: 0x158
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x628
-  __DATA_CONST.__cfstring: 0x14e0
+  __DATA_CONST.__cfstring: 0x1540
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x920
-  __DATA.__common: 0x11c
-  __DATA.__bss: 0x4f0
+  __DATA.__common: 0x200
+  __DATA.__bss: 0x4e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 222
+  Functions: 231
   Symbols:   371
-  CStrings:  1113
+  CStrings:  1120
 
CStrings:
+ "%@/(appv|(|mansta-)fCfg|pcrt|scrt|seal|ChMf|SCfT)-%@/ "
+ "%s: Exclaves are enabled, preserve exclave assets"
+ "%s: Failed to determine exclaves status: %d"
+ "Cryptexes"
+ "kern.exclaves_status"
+ "removeExcept /(ANE|GFX|AVE|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware))\\.img4/"
+ "removeExcept /(ANE|GFX|AVE|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware|ExclaveOSVolume|ExclaveOSIntegrityCatalog|ExclaveOSTrustCache|cL4))\\.img4/ /Ap,ExclaveOS.dmg/"
+ "removeExcept /ExclaveOS/"
+ "removeExcept /devicetree.img4/ /root_hash.img4/ /sep-firmware.img4/ /sep-patches.img4/"
+ "supports_exclaves"
- "%@/(appv|(|mansta-)fCfg|pcrt|scrt|seal)-%@/ "
- "removeExcept /(ANE|GFX|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor))\\.img4/"
- "removeExcept /devicetree.img4/ /root_hash.img4/ /sep-firmware.img4/"

```
