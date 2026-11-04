## UARPUpdaterServiceUSBPD

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1587.40.33.0.0
-  __TEXT.__text: 0x24548
+1587.60.11.0.0
+  __TEXT.__text: 0x24c84
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0x35a0
-  __TEXT.__objc_methlist: 0x1ac0
+  __TEXT.__objc_stubs: 0x36a0
+  __TEXT.__objc_methlist: 0x1ae0
   __TEXT.__const: 0xd0
-  __TEXT.__oslogstring: 0x2a7b
-  __TEXT.__cstring: 0x3101
+  __TEXT.__oslogstring: 0x2c04
+  __TEXT.__cstring: 0x31b0
   __TEXT.__objc_classname: 0x1c4
   __TEXT.__objc_methtype: 0x39d2
   __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__objc_methname: 0x4841
-  __TEXT.__unwind_info: 0xdb8
+  __TEXT.__objc_methname: 0x48f6
+  __TEXT.__unwind_info: 0xdd0
   __DATA_CONST.__const: 0x740
-  __DATA_CONST.__cfstring: 0x640
+  __DATA_CONST.__cfstring: 0x660
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__auth_got: 0x470
   __DATA_CONST.__got: 0x1b0
-  __DATA.__objc_const: 0x3748
-  __DATA.__objc_selrefs: 0x10c0
-  __DATA.__objc_ivar: 0x248
+  __DATA.__objc_const: 0x3778
+  __DATA.__objc_selrefs: 0x1100
+  __DATA.__objc_ivar: 0x24c
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x375
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1139
+  Functions: 1146
   Symbols:   604
-  CStrings:  1600
+  CStrings:  1623
 
CStrings:
+ "%s: %@ is actively staging on %@"
+ "%s: Invalid tag format '%@', must start with 'A'"
+ "%s: Invalid tag length %lu, expected 5 characters"
+ "%s: no pending assets, not marking isStagingAsset %@"
+ "-[UARPMagSafeCable queryExpectedPayloadTag]"
+ "-[UARPUSBPDUpdater assetOnLocalStorage:assetID:]_block_invoke"
+ "-[UARPUSBPDUpdater qHpmHasActiveAssetStaging:]"
+ "A"
+ "AMN=<%@> needsFirmware=<%s>, needsLogs=<%s>, needsAnalytics=<%s>, autoAppliesStagedFirmware=<%s> supportsAccmode7=<%s> isStagingAsset=<%s>"
+ "No supported accessories on %@"
+ "Skip power adapter check on this hpm, asset actively staging on %@"
+ "TB,V_isStagingAsset"
+ "_isStagingAsset"
+ "alternativeAppleModelNumbers"
+ "anyObject"
+ "hasPrefix:"
+ "isStagingAsset"
+ "isStagingAsset -> NO %@"
+ "isStagingAsset -> YES (dynamic asset progress) %@"
+ "isStagingAsset -> YES (firmware) %@"
+ "pendingAssets"
+ "qHpmHasActiveAssetStaging:"
+ "setIsStagingAsset:"
+ "substringWithRange:"
- "AMN=<%@> needsFirmware=<%s>, needsLogs=<%s>, needsAnalytics=<%s>, autoAppliesStagedFirmware=<%s> supportsAccmode7=<%s>"
```
