## mobile_obliterator

> `/usr/libexec/mobile_obliterator`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-402.40.2.0.0
-  __TEXT.__text: 0x1ba64
+402.60.4.0.0
+  __TEXT.__text: 0x1bef4
   __TEXT.__auth_stubs: 0x1540
   __TEXT.__objc_stubs: 0x920
-  __TEXT.__objc_methlist: 0x1fc
-  __TEXT.__cstring: 0xaeae
+  __TEXT.__objc_methlist: 0x22c
+  __TEXT.__cstring: 0xb157
   __TEXT.__const: 0x708
   __TEXT.__gcc_except_tab: 0x144
-  __TEXT.__objc_methname: 0x809
+  __TEXT.__objc_methname: 0x847
   __TEXT.__objc_classname: 0x5b
-  __TEXT.__objc_methtype: 0x159
-  __TEXT.__unwind_info: 0x510
-  __DATA_CONST.__const: 0x678
-  __DATA_CONST.__cfstring: 0x2180
+  __TEXT.__objc_methtype: 0x19c
+  __TEXT.__unwind_info: 0x530
+  __DATA_CONST.__const: 0x6c0
+  __DATA_CONST.__cfstring: 0x2200
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0xab8
   __DATA_CONST.__got: 0x1b0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x400
-  __DATA.__objc_selrefs: 0x308
+  __DATA.__objc_const: 0x410
+  __DATA.__objc_selrefs: 0x318
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x248

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 277
+  Functions: 285
   Symbols:   402
-  CStrings:  1417
+  CStrings:  1438
 
Symbols:
+ _objc_release_x24
- _objc_release_x19
CStrings:
+ "%s: %s: Failed to set secure-erase marker to '%s'"
+ "%s: %s: Secure-erase marker: clearing"
+ "%s: %s: Secure-erase marker: setting to '%s'"
+ "%s: %s: readSecureEraseState: could not get the IO registry entry"
+ "%s: %s: readSecureEraseState: secure-erase marker not set (or unreadable)"
+ "%s: %s: safeEACS: secure-erase marker is PENDING - retrying sanitize once"
+ "-[MOXPCServerEmbedded clearSecureEraseStateWithReply:]"
+ "-[MOXPCServerEmbedded getSecureEraseStateWithReply:]"
+ "Missing secure-erase-state entitlement"
+ "clearSecureEraseNVRAMkey"
+ "clearSecureEraseStateWithReply:"
+ "com.apple.private.mobileobliteration.secure-erase-state"
+ "getSecureEraseStateWithReply:"
+ "pending"
+ "pet"
+ "readSecureEraseState"
+ "removeExcept /(ANE|AOP|AOP2|AVE|GFX|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware|MSRFirmware))\\.img4/"
+ "removeExcept /(ANE|AOP|AOP2|AVE|GFX|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware|MSRFirmware|ExclaveOSVolume|ExclaveOSIntegrityCatalog|ExclaveOSTrustCache|cL4))\\.img4/ /Ap,ExclaveOS.dmg/"
+ "secure-erase-incomplete"
+ "setSecureEraseNVRAMState"
+ "v24@0:8@?16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSError\"q>16"
- "removeExcept /(ANE|AOP|AOP2|AVE|GFX|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware))\\.img4/"
- "removeExcept /(ANE|AOP|AOP2|AVE|GFX|PMP|SIO|StaticTrustCache|iBootData|Ap,(ANE1|RestoreTMU|SecurePageTableMonitor|TrustedExecutionMonitor|ApplePMCFirmware|GFX1Firmware|ExclaveOSVolume|ExclaveOSIntegrityCatalog|ExclaveOSTrustCache|cL4))\\.img4/ /Ap,ExclaveOS.dmg/"
```
