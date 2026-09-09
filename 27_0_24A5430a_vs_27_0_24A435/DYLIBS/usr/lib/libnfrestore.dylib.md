## libnfrestore.dylib

> `/usr/lib/libnfrestore.dylib`

```diff

 370.42.1.0.0
-  __TEXT.__text: 0xceac
+  __TEXT.__text: 0x10cd0
   __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x2181
-  __TEXT.__oslogstring: 0x18cb
-  __TEXT.__unwind_info: 0x120
+  __TEXT.__cstring: 0x2db2
+  __TEXT.__oslogstring: 0x20bf
+  __TEXT.__unwind_info: 0x130
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x30
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__cfstring: 0x6c0
-  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH_CONST.__cfstring: 0x940
+  __AUTH_CONST.__auth_got: 0x538
   __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libPN548_API.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  Functions: 53
-  Symbols:   186
-  CStrings:  492
+  Functions: 57
+  Symbols:   202
+  CStrings:  632
 
Symbols:
+ _CFDataCreate
+ _CFStringCreateWithFormat
+ _NFDriverClearControllerInfoCache
+ _NFDriverClearFactoryPageE0Tag
+ _NFDriverCustomerFactoryPageIsUnlocked
+ _NFDriverFactoryPageHasExpectedConfigForTag
+ _NFDriverFactoryPageHasProductionContent
+ _NFDriverFactoryPageHasTagConfigured
+ _NFDriverGetBootMeasurements
+ _NFDriverGetFactoryPage
+ _NFDriverReleaseBootMeasurements
+ _NFDriverWriteFactoryPage
+ _NFIsProductType
+ _NFPlatformHasBootMeasurements
+ _NFProductHasFactoryPage
+ _NFValidateNFCCHashes
CStrings:
+ "%02X.%02X.%02X"
+ "%02X.%02X.%03X"
+ "%02X_%02X_%03X"
+ "%s:%i Address Start:0x%08X End:0x%08X"
+ "%s:%i Chip version %02x.%02x.%02x"
+ "%s:%i Customer factory page is already locked with production content. Nothing to do."
+ "%s:%i Customer factory page is locked"
+ "%s:%i Customer factory page is locked without production content !"
+ "%s:%i Error : Invalid TLV: 0x%x"
+ "%s:%i Error : Unexpected TLV: 0x%x"
+ "%s:%i Error : invalid length %d"
+ "%s:%i Error : more than 1 TLV : %d"
+ "%s:%i Error : unexpected length %d"
+ "%s:%i Error: Failed to validate boot measurements"
+ "%s:%i Factory page E0 clear not supported on this hardware."
+ "%s:%i Factory page already has production content. Nothing to do."
+ "%s:%i Failed to clear E0 tag : %d"
+ "%s:%i Failed to decode plist"
+ "%s:%i Failed to find file %s"
+ "%s:%i Failed to get factory page : %d"
+ "%s:%i Failed to get factory page."
+ "%s:%i Failed to get file name %s"
+ "%s:%i Failed to get info."
+ "%s:%i Failed to load plist"
+ "%s:%i Failed to parse index file as dictionary"
+ "%s:%i Failed to query Boot measurements"
+ "%s:%i Failed to read index file"
+ "%s:%i Failed to update customer factory page"
+ "%s:%i Failed to update customer factory page."
+ "%s:%i Failed to validate Boot measurements"
+ "%s:%i Failed to write factory page : %d"
+ "%s:%i Found matching unlock firmware: %s"
+ "%s:%i Invalid format"
+ "%s:%i Invalid hashes length"
+ "%s:%i Locking factory page (%s)"
+ "%s:%i Malformed Customer page !"
+ "%s:%i Retrieving boot measurements"
+ "%s:%i Running customer factory page update with %s"
+ "%s:%i Unexpected NULL parameter"
+ "%s:%i Unexpected length mismatch : %zu vs %zu"
+ "%s:%i Using custom hashes"
+ "%s:%i Validating boot measurements"
+ "%s:%i Warning : more than 1 TLV : %d"
+ "%s:%i Warning: failed to validate boot measurements, skipping"
+ "%s:%i Writing factory page (E0:%s F0:%s 02:%s 03:%s 04:%s 05:%s 06:%s)"
+ "%{public}s:%i Address Start:0x%08X End:0x%08X"
+ "%{public}s:%i Chip version %02x.%02x.%02x"
+ "%{public}s:%i Customer factory page is already locked with production content. Nothing to do."
+ "%{public}s:%i Customer factory page is locked"
+ "%{public}s:%i Customer factory page is locked without production content !"
+ "%{public}s:%i Error : Invalid TLV: 0x%x"
+ "%{public}s:%i Error : Unexpected TLV: 0x%x"
+ "%{public}s:%i Error : invalid length %d"
+ "%{public}s:%i Error : more than 1 TLV : %d"
+ "%{public}s:%i Error : unexpected length %d"
+ "%{public}s:%i Error: Failed to validate boot measurements"
+ "%{public}s:%i Factory page E0 clear not supported on this hardware."
+ "%{public}s:%i Factory page already has production content. Nothing to do."
+ "%{public}s:%i Failed to clear E0 tag : %d"
+ "%{public}s:%i Failed to decode plist"
+ "%{public}s:%i Failed to find file %s"
+ "%{public}s:%i Failed to get factory page : %d"
+ "%{public}s:%i Failed to get factory page."
+ "%{public}s:%i Failed to get file name %s"
+ "%{public}s:%i Failed to get info."
+ "%{public}s:%i Failed to load plist"
+ "%{public}s:%i Failed to parse index file as dictionary"
+ "%{public}s:%i Failed to query Boot measurements"
+ "%{public}s:%i Failed to read index file"
+ "%{public}s:%i Failed to update customer factory page"
+ "%{public}s:%i Failed to update customer factory page."
+ "%{public}s:%i Failed to validate Boot measurements"
+ "%{public}s:%i Failed to write factory page : %d"
+ "%{public}s:%i Found matching unlock firmware: %s"
+ "%{public}s:%i Invalid format"
+ "%{public}s:%i Invalid hashes length"
+ "%{public}s:%i Locking factory page (%s)"
+ "%{public}s:%i Malformed Customer page !"
+ "%{public}s:%i Retrieving boot measurements"
+ "%{public}s:%i Running customer factory page update with %s"
+ "%{public}s:%i Unexpected NULL parameter"
+ "%{public}s:%i Unexpected length mismatch : %zu vs %zu"
+ "%{public}s:%i Using custom hashes"
+ "%{public}s:%i Validating boot measurements"
+ "%{public}s:%i Warning : more than 1 TLV : %d"
+ "%{public}s:%i Warning: failed to validate boot measurements, skipping"
+ "%{public}s:%i Writing factory page (E0:%s F0:%s 02:%s 03:%s 04:%s 05:%s 06:%s)"
+ "/usr/standalone/firmware/nfrestore/firmware/fury-fw-hashes/PN800V-hashes.plist"
+ "/usr/standalone/firmware/nfrestore/firmware/fw-hashes/SN450V-hashes.plist"
+ "ClearE0Tag"
+ "Current platform info from customer factory page is "
+ "Customer factory page"
+ "DisableBootMeasurementEnforcement"
+ "Dump: "
+ "InvalidBStateSettingsPolicy"
+ "LockFactoryPage"
+ "Mismatched info hash"
+ "Mismatched protected firmware hash"
+ "Mismatched protected lifecycle hash"
+ "Mismatched scratch firmware hash"
+ "Mismatched scratch lifecycle hash"
+ "NFCBootHashOverride"
+ "PN800V A0/A1"
+ "PN800V_FW_A0_"
+ "PN800V_FW_A0_01_01_08_rev163891.bin"
+ "PN800V_FW_A0_01_01_A8_rev164283.bin"
+ "PN800V_FW_A1_"
+ "PN800V_FW_A1_01_01_14_rev46806918.bin"
+ "PN800V_FW_A1_01_01_B4_rev47094117.bin"
+ "SN450V A0/A1"
+ "SN450V B0/B1/B2"
+ "SN450V_FW_A1_"
+ "SN450V_FW_A1_01_01_00A_rev14059249.bin"
+ "SN450V_FW_A1_01_01_80A_rev14497923.bin"
+ "SN450V_FW_B0_"
+ "SN450V_FW_B0_02_01_014_rev46800544.bin"
+ "SN450V_FW_B0_02_01_814_rev46829584.bin"
+ "SN450V_FW_B1_"
+ "SN450V_FW_B1_03_01_015_rev48923467.bin"
+ "SN450V_FW_B1_03_01_814_rev46829584.bin"
+ "_NFRestoreBootMeasurements"
+ "_NFRestoreClearE0Tag"
+ "_NFRestoreReadPlatformInfoFromFactoryPage"
+ "_NFRestoreValidateBootMeasurements"
+ "_NFRestoreWriteFactoryPage"
+ "_NfRestoreCopyCustomerPageUpdateFirmware"
+ "_NfRestoreCustomerFactoryPageMatches"
+ "_NfRestoreCustomerFactoryPageUpdate"
+ "_NfRestoreStripHeaderFromPlatformInfoTLV"
+ "apply"
+ "debug"
+ "fixup"
+ "fw-unlock"
+ "ignore"
+ "index.plist"
+ "mask"
+ "prod"
+ "skip"
+ "value"
+ "yes"
```
