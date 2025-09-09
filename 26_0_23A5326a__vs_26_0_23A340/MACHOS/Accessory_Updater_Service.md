## Accessory Updater Service

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service`

```diff

-3476.0.46.0.0
-  __TEXT.__text: 0x77354
+3476.2.1.0.0
+  __TEXT.__text: 0x78acc
   __TEXT.__auth_stubs: 0x1870
   __TEXT.__objc_stubs: 0x2d00
   __TEXT.__objc_methlist: 0x2e8c
   __TEXT.__const: 0x5c90
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x16f3c
+  __TEXT.__cstring: 0x176e1
   __TEXT.__objc_methname: 0x3672
   __TEXT.__objc_classname: 0xb12
   __TEXT.__objc_methtype: 0xd01
   __TEXT.__oslogstring: 0x155e
-  __TEXT.__unwind_info: 0x1860
+  __TEXT.__unwind_info: 0x18a8
   __DATA_CONST.__auth_got: 0xc48
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x2a88
-  __DATA_CONST.__cfstring: 0x10ee0
+  __DATA_CONST.__const: 0x2ab0
+  __DATA_CONST.__cfstring: 0x110e0
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x58

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: B15D0475-2BF5-350C-A6EA-AC4166BE721D
-  Functions: 2475
-  Symbols:   1837
-  CStrings:  6894
+  UUID: C17381DC-49D6-34CF-B8D4-A7ACB81A3EAA
+  Functions: 2541
+  Symbols:   1853
+  CStrings:  6967
 
Symbols:
+ _AMAuthInstallBasebandMAV25MeasureFirmware
+ _AMAuthInstallBasebandMAV25StitchFirmware
+ _AMAuthInstallMonetMeasureMav25Elf32MBN
+ _AMAuthInstallMonetMeasureMav25Elf64MBN
+ _AMAuthInstallMonetMeasureMav25MiscElf
+ _AMAuthInstallMonetMeasureMav25RestoreSbl1Elf
+ _AMAuthInstallMonetMeasureMav25Sbl1Elf
+ _AMAuthInstallMonetMeasurePT
+ _AMAuthInstallMonetMeasureTmeElf
+ _AMAuthInstallMonetStitchMav25EBootLoader
+ _AMAuthInstallMonetStitchTme
+ _kAMAuthInstallTagBbPTDownloadDigest
+ _kAMAuthInstallTagBbTmeHashTableBody
+ _kAMAuthInstallTagBbTmeHashTableHeader
+ _kAMAuthInstallTagBbTmePartialDigest
+ _kAMAuthInstallTagBbTmeStitch
CStrings:
+ "\n\n"
+ "( LETOH( header->qti_metadata_size ) == 0 ) || ( LETOH( header->qti_metadata_size ) == sizeof(mav25_authority_meta_field_t) )"
+ "AMAuthInstallBasebandMAV25MeasureFirmware"
+ "AMAuthInstallBasebandMAV25StitchFirmware"
+ "AMAuthInstallMonet.c"
+ "AMAuthInstallMonetMeasureMav25Elf32MBN"
+ "AMAuthInstallMonetMeasureMav25Elf64MBN"
+ "AMAuthInstallMonetStitchMav25EBootLoader"
+ "AMAuthInstallMonetStitchTme"
+ "Failed to create hashTableBodyData"
+ "Failed to create jmetMetadataSegmentData"
+ "Failed to create originalFileName"
+ "Failed to create personalizedFileName"
+ "MBN hash_table_size is not non-zero"
+ "MBN hash_table_size is zero"
+ "MBN hash_table_size overflows file"
+ "MBN oem_certificate_chain_size overflows file"
+ "MBN oem_signature_size overflows file"
+ "MBN qti_certificate_chain_size overflows file"
+ "MBN qti_signature_size overflows file"
+ "MBN segment components > size of ELF segment"
+ "PT-DownloadDigest"
+ "Stitch Debug: \n StitchAddress: 0x%x \n 64-Byte-Aligned: %s \n 128-Byte-Aligned: %s\n stitchDataSize = %d stitchDataOffset = %d Len(newFileData) = %d"
+ "TME-HashTableBody"
+ "TME-HashTableBody-Blob"
+ "TME-HashTableHeaderDefault"
+ "TME-PartialDigest"
+ "_AMAuthInstallMonetStitchMav25Chunk"
+ "_AMAuthInstallMonetStitchMav25FirstStage"
+ "_CalculateOEMSignatureCertChainSize"
+ "_CalculateSizeOfJMETMetadataSegment"
+ "amai argument is NULL"
+ "aop_devcfg.mbn"
+ "bbfwDict lacks the dictionary type"
+ "cpucp.elf"
+ "false"
+ "fileData argument is NULL"
+ "hashSectionTag argument is NULL"
+ "hashTableHeaderRef argument is NULL"
+ "kExpectedOEMCertChainSize == kOEMCertChainSize || 0 == kOEMCertChainSize"
+ "kExpectedOEMSignatureSize == kOEMSignatureSize || 0 == kOEMSignatureSize"
+ "mdmddr.mbn"
+ "measurementDict argument is NULL"
+ "outFileData argument is NULL"
+ "partialDigestTag argument is NULL"
+ "pt.mbn"
+ "qdsp6sw_dtbs.elf"
+ "qupv3fw.elf"
+ "responseDict argument is NULL"
+ "restorexbl_sc.elf"
+ "sequencer_ram.elf"
+ "shrm.elf"
+ "signed_firmware_soc_view.elf"
+ "sourceStitchData lacks the dictionary type"
+ "stitch data offset and size exceeds the bounds of stitch data"
+ "stitchTag argument is NULL"
+ "xbl_sc.elf"

```
