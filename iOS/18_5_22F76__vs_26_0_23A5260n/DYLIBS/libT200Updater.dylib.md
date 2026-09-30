## libT200Updater.dylib

> `/usr/lib/updaters/libT200Updater.dylib`

```diff

-1.0.0.6.57
-  __TEXT.__text: 0x113e4
+1.0.0.7.65
+  __TEXT.__text: 0x1331c
   __TEXT.__auth_stubs: 0x710
-  __TEXT.__cstring: 0x42a2
-  __TEXT.__const: 0xfef
+  __TEXT.__cstring: 0x4790
+  __TEXT.__const: 0xff7
   __TEXT.__oslogstring: 0x1b9
-  __TEXT.__unwind_info: 0x248
+  __TEXT.__unwind_info: 0x250
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0xd58
+  __DATA_CONST.__const: 0xd70
   __AUTH_CONST.__auth_got: 0x388
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xb60
+  __AUTH_CONST.__cfstring: 0xc60
   __DATA.__data: 0x10
-  __DATA.__common: 0x28
+  __DATA.__common: 0xd0
   __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
-  UUID: 34588686-5BCC-3956-A7A4-CBB6FD141635
-  Functions: 341
-  Symbols:   1255
-  CStrings:  700
+  UUID: B0917D26-FEA6-35E2-BC1A-487B5043BAAA
+  Functions: 388
+  Symbols:   1366
+  CStrings:  760
 
Symbols:
+ _DERParseInteger64Signed
+ _DERParseIntegerSigned
+ _T200DigestDERDictFirmware
+ _T200GetBoardIdFromDT
+ _T200GetBoardIdFromDT.cold.1
+ _T200GetBoardIdFromDT.cold.2
+ _T200GetBoardIdFromDT.cold.3
+ _T200GetBoardIdFromDT.cold.4
+ _T200GetBoardIdFromDT.cold.5
+ _T200GetBoardIdFromDT.cold.6
+ _T200GetBoardIdFromDT.cold.7
+ _T200GetBoardIdFromDT.cold.8
+ _T200MeasurementDictFirmware
+ _T200OptionRequest
+ _T200OptionTicket
+ _T200TagBoardID
+ _T200TagBoardId
+ _T200TagCertificateEpoch
+ _T200TagChipID
+ _T200TagDerFirmwarePlist
+ _T200TagEFFV
+ _T200TagFAEnable
+ _T200TagFWOverWrite
+ _T200TagMeasurementFirmware
+ _T200TagMeasurementFirmwarePlist
+ _T200TagNonce
+ _T200TagProductionMode
+ _T200TagRequestFirmwareTicket
+ _T200TagResponseFirmwareTicket
+ _T200TagRevision
+ _T200TagUniqueID
+ _T200TagVNVEnable
+ _T200UpdaterCopyFirmwareWithLogging.cold.15
+ _T200UpdaterCopyFirmwareWithLogging.cold.16
+ _T200UpdaterCreateRequestWithLogging.cold.23
+ _T200UpdaterGetTagsWithLogging.cold.6
+ _T200UpdaterGetTagsWithLogging.cold.7
+ __T200GetBMUID
+ __T200GetBMUID.cold.1
+ __T200GetBMUID.cold.2
+ __T200GetBMUID.cold.3
+ __T200GetBMUID.cold.4
+ __T200GetBMUID.cold.5
+ __T200GetBMUID.cold.6
+ __T200GetBMUID.cold.7
+ __T200GetBMUID.cold.8
+ __T200GetBMUID.cold.9
+ __getInfoSMCIF.cold.15
+ __releaseBMUTags
+ __updateBMUTags
+ __updateBMUTags.cold.1
+ __updateBMUTags.cold.10
+ __updateBMUTags.cold.11
+ __updateBMUTags.cold.12
+ __updateBMUTags.cold.13
+ __updateBMUTags.cold.14
+ __updateBMUTags.cold.15
+ __updateBMUTags.cold.16
+ __updateBMUTags.cold.17
+ __updateBMUTags.cold.18
+ __updateBMUTags.cold.19
+ __updateBMUTags.cold.2
+ __updateBMUTags.cold.20
+ __updateBMUTags.cold.21
+ __updateBMUTags.cold.22
+ __updateBMUTags.cold.23
+ __updateBMUTags.cold.3
+ __updateBMUTags.cold.4
+ __updateBMUTags.cold.5
+ __updateBMUTags.cold.6
+ __updateBMUTags.cold.7
+ __updateBMUTags.cold.8
+ __updateBMUTags.cold.9
+ _kT200DeviceInfoBMUID
+ _kT200TagBMU
+ _kT200TagBMU2
- __T200UpdaterExecCommand.cold.116
- __T200UpdaterExecCommand.cold.117
- __T200UpdaterExecCommand.cold.118
- __T200UpdaterExecCommand.cold.119
- __T200UpdaterExecCommand.cold.120
CStrings:
+ "%s:%d Add Entitlements T200TagEFFV\n"
+ "%s:%d Add Entitlements T200TagFAEnableOption\n"
+ "%s:%d Add Entitlements T200TagFWOverWrite\n"
+ "%s:%d Add Entitlements T200TagVNVEnableOption\n"
+ "%s:%d BMUID %08x \n"
+ "%s:%d BMUID %d \n"
+ "%s:%d Defaults Node present \n"
+ "%s:%d NumEnabled from IODT %08x \n"
+ "%s:%d NumEnabledBMU %08x \n"
+ "%s:%d NumSupported from IODT %08x \n"
+ "%s:%d NumSupportedBMU %08x \n"
+ "%s:%d PSimPresent from IODT %08x \n"
+ "%s:%d psim-present property available \n"
+ "BMU,"
+ "BMU2,"
+ "BMUID"
+ "CFGetTypeID(num_enabled_data) == CFDataGetTypeID()"
+ "CFGetTypeID(num_supported_data) == CFDataGetTypeID()"
+ "CFNumberGetValue((CFNumberRef)bmuIDNumberRef, kCFNumberSInt32Type, &bmuid)"
+ "Cannot allocate BMUTags"
+ "IODeviceTree:/defaults"
+ "T200MeasurementDictFirmware"
+ "T200OptionRequest"
+ "T200OptionTicket"
+ "T200OptionTicketRef"
+ "T200TagBoardID"
+ "T200TagBoardId"
+ "T200TagCertificateEpoch"
+ "T200TagChipID"
+ "T200TagDerFirmwarePlist"
+ "T200TagEFFV"
+ "T200TagFAEnable"
+ "T200TagFWOverWrite"
+ "T200TagMeasurementFirmware"
+ "T200TagMeasurementFirmwarePlist"
+ "T200TagNonce"
+ "T200TagProductionMode"
+ "T200TagRequestFirmwareTicket"
+ "T200TagResponseFirmwareTicket"
+ "T200TagRevision"
+ "T200TagUniqueID"
+ "T200TagVNVEnable"
+ "Unable to get kT200TagMeasurementPatch"
+ "_T200GetBMUID"
+ "_T200GetNumEnabledBMUFromDT"
+ "_T200GetNumSupportedBMUFromDT"
+ "_T200GetPSimFromDT"
+ "_releaseBMUTags"
+ "_updateBMUTags"
+ "bmu-num-enabled"
+ "bmu-num-supported"
+ "bmu2-board-id"
+ "bmu2-chip-id"
+ "bmu_id"
+ "deviceInfo && (CFGetTypeID(deviceInfo)==CFDictionaryGetTypeID())"
+ "kT200TagMeasurement"
+ "psim-present"
+ "success == true"
- "%s:%d Add Entitlements kT200TagEFFV\n"
- "%s:%d Add Entitlements kT200TagFAEnableOption\n"
- "%s:%d Add Entitlements kT200TagFWOverWrite\n"
- "%s:%d Add Entitlements kT200TagVNVEnableOption\n"
- "num"
- "result"

```
