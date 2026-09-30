## libPN548_API.dylib

> `/usr/lib/libPN548_API.dylib`

```diff

 370.42.1.0.0
-  __TEXT.__text: 0x3fe34
-  __TEXT.__const: 0x640
-  __TEXT.__cstring: 0x92f1
-  __TEXT.__oslogstring: 0x791c
-  __TEXT.__unwind_info: 0x5a0
+  __TEXT.__text: 0x459a0
+  __TEXT.__const: 0x660
+  __TEXT.__cstring: 0xab18
+  __TEXT.__oslogstring: 0x8791
+  __TEXT.__unwind_info: 0x618
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0xe38
+  __DATA_CONST.__const: 0x1128
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__const: 0x368
+  __AUTH_CONST.__cfstring: 0x780
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x18
   __DATA_DIRTY.__bss: 0x18

   - /usr/lib/libNFC_HAL.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
-  Functions: 417
-  Symbols:   350
-  CStrings:  1790
+  Functions: 453
+  Symbols:   377
+  CStrings:  1946
 
Symbols:
+ _NFDataAppendBytes
+ _NFDriverClearFactoryPageE0Tag
+ _NFDriverCustomerFactoryPageIsUnlocked
+ _NFDriverFactoryPageHasExpectedConfigForTag
+ _NFDriverFactoryPageHasProductionContent
+ _NFDriverFactoryPageHasTagConfigured
+ _NFDriverGetBootMeasurements
+ _NFDriverGetFactoryPage
+ _NFDriverGetRFState
+ _NFDriverReleaseBootMeasurements
+ _NFDriverSetRFState
+ _NFDriverWriteFactoryPage
+ _NFIsProductType
+ _NFPlatformHasAlternateRFSettings
+ _NFPlatformHasBootMeasurements
+ _NFPlatformHasSecureBoot
+ _NFProductGetFactoryPageGPIODefaultConfig
+ _NFProductGetFactoryPageGPIODriveConfig
+ _NFProductGetFactoryPageGPIOPullConfig
+ _NFProductGetFactoryPageLoadSwitchConfig
+ _NFProductGetFactoryPagePlatformConfig
+ _NFProductGetFactoryPageVGPIOEventsConfig
+ _NFProductGetFactoryPageVGPIOTargetsConfig
+ _phLibNfc_Mgt_ConfigCustFactoryPage
+ _phLibNfc_Mgt_FMM_GetHashDump
+ _phLibNfc_Mgt_GetSecureFwInfo
+ _phTmlNfc_RegisterBootStopInterruptCallback
CStrings:
+ "%s:%i 0x%02X TLV doesn't match"
+ "%s:%i 0x%02X TLV length doesn't match expected (%d)"
+ "%s:%i BFAR=0x%04x CFSR=0x%04x MMFAR=0x%04x"
+ "%s:%i BPMR=0x%04x FMR=0x%04x CR=0x%04x"
+ "%s:%i Boot status=%d\n                        ROM=0x%x, HW Version=0x%x, Chip version=0x%04X, Variant=%x, ModelID=%x\n                        Protected status=%x, Lifecycle:{scratch=0x%04X,protected=0x%04X}, vendorFW={scratch=0x%04X,protected=0x%04X, revision=%d}\n                        SEC_CFG:{lifecycle=0x%04x,scratch=0x%04X,protected=0x%04X}\n                        Endurance Counter ECC=%x\n                        dieID=%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X CRC=0x%04X\n                        Cert:{Scratch=0x%04x,protected=0x%04x,dl_scratch=0x%04X,dl_protected=0x%04X}\n                        App:{vendor=0x%04x,customer=0x%04x}\n                        MW:{Major=0x%04x,Minor=0x%04x}"
+ "%s:%i Cal data for B is correct, flashing."
+ "%s:%i Changing RF settings to alternate"
+ "%s:%i Changing RF settings to default"
+ "%s:%i Clearing E0 tag from customer factory page."
+ "%s:%i Customer Factory page has no data."
+ "%s:%i Customer Factory page is NULL."
+ "%s:%i Customer Factory page is locked."
+ "%s:%i Customer Factory page is unlocked."
+ "%s:%i Customer factory page is locked. Cannot clear E0 tag."
+ "%s:%i Device in degraded mode. Wired not available."
+ "%s:%i Disabling multi-tag polling, RTID=%d"
+ "%s:%i E0 tag cleared successfully."
+ "%s:%i E0 tag not found or already cleared. Nothing to do."
+ "%s:%i Empty factory page"
+ "%s:%i Enabling multi-tag polling, RTID=%d"
+ "%s:%i Error ! Received boot stop interrupt."
+ "%s:%i Error : invalid response."
+ "%s:%i F0 TLV too short (%d), treating as unprogrammed."
+ "%s:%i F0 has production content (version=0x%04x, type=0x%04x), preserving."
+ "%s:%i F0 has testing bit (0x%04x), will overwrite."
+ "%s:%i F0 version is 0, treating as unprogrammed."
+ "%s:%i Failed 0x%04llx"
+ "%s:%i Failed to allocate TLV data"
+ "%s:%i Failed to clear E0 tag : %d"
+ "%s:%i Failed to create page content"
+ "%s:%i Failed to get FDR data : no data."
+ "%s:%i Failed to get boot measurements"
+ "%s:%i Failed to get factory page : %d"
+ "%s:%i Failed to get page : 0x%04llx"
+ "%s:%i Failed to query FW info !"
+ "%s:%i Failed to query chip info. Bailing"
+ "%s:%i Failed to read clock register"
+ "%s:%i Failed to set A1DF: 0x%08llx"
+ "%s:%i Failed to set XTAL clock source"
+ "%s:%i Failed to write RF cal data A to NFCC"
+ "%s:%i Failed to write RF cal data B to NFCC"
+ "%s:%i Failed to write page : 0x%04llx"
+ "%s:%i HFSR=0x%04x SFAR=0x%04x SFSR=0x%04x"
+ "%s:%i Invalid clock register response"
+ "%s:%i Invalid length %d for tag 0x%x: only %zu remaingin"
+ "%s:%i MFW factory page config notification received : NULL"
+ "%s:%i MSPL=0x%04x PSPL=0x%04x PMR=0x%04x"
+ "%s:%i Platform does not have boot measurements"
+ "%s:%i RF settings = %s"
+ "%s:%i RTID Debug mode enabled"
+ "%s:%i Re-configuring XTAL clock source"
+ "%s:%i Received SRAM REPAIR %s notification"
+ "%s:%i This feature is restricted to internal builds."
+ "%s:%i Truncated tag found. Tag 0x%02x, tlvLen: %d, idx: %d, len: %d"
+ "%s:%i Unable to find config tag info for tag 0x%02x"
+ "%s:%i Using cached dieID"
+ "%s:%i Using local RF settings"
+ "%s:%i Warning : B state cal data was written with A state values. Applying .."
+ "%s:%i Warning : B state cal data was written with A state values. Skipping .."
+ "%s:%i Warning : B state cal data was written with A state values. Updating tags ..."
+ "%{public}s:%i 0x%02X TLV doesn't match"
+ "%{public}s:%i 0x%02X TLV length doesn't match expected (%d)"
+ "%{public}s:%i BFAR=0x%04x CFSR=0x%04x MMFAR=0x%04x"
+ "%{public}s:%i BPMR=0x%04x FMR=0x%04x CR=0x%04x"
+ "%{public}s:%i Boot status=%d\n                        ROM=0x%x, HW Version=0x%x, Chip version=0x%04X, Variant=%x, ModelID=%x\n                        Protected status=%x, Lifecycle:{scratch=0x%04X,protected=0x%04X}, vendorFW={scratch=0x%04X,protected=0x%04X, revision=%d}\n                        SEC_CFG:{lifecycle=0x%04x,scratch=0x%04X,protected=0x%04X}\n                        Endurance Counter ECC=%x\n                        dieID=%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X%02X CRC=0x%04X\n                        Cert:{Scratch=0x%04x,protected=0x%04x,dl_scratch=0x%04X,dl_protected=0x%04X}\n                        App:{vendor=0x%04x,customer=0x%04x}\n                        MW:{Major=0x%04x,Minor=0x%04x}"
+ "%{public}s:%i Cal data for B is correct, flashing."
+ "%{public}s:%i Changing RF settings to alternate"
+ "%{public}s:%i Changing RF settings to default"
+ "%{public}s:%i Clearing E0 tag from customer factory page."
+ "%{public}s:%i Customer Factory page has no data."
+ "%{public}s:%i Customer Factory page is NULL."
+ "%{public}s:%i Customer Factory page is locked."
+ "%{public}s:%i Customer Factory page is unlocked."
+ "%{public}s:%i Customer factory page is locked. Cannot clear E0 tag."
+ "%{public}s:%i Device in degraded mode. Wired not available."
+ "%{public}s:%i Disabling multi-tag polling, RTID=%d"
+ "%{public}s:%i E0 tag cleared successfully."
+ "%{public}s:%i E0 tag not found or already cleared. Nothing to do."
+ "%{public}s:%i Empty factory page"
+ "%{public}s:%i Enabling multi-tag polling, RTID=%d"
+ "%{public}s:%i Error ! Received boot stop interrupt."
+ "%{public}s:%i Error : invalid response."
+ "%{public}s:%i F0 TLV too short (%d), treating as unprogrammed."
+ "%{public}s:%i F0 has production content (version=0x%04x, type=0x%04x), preserving."
+ "%{public}s:%i F0 has testing bit (0x%04x), will overwrite."
+ "%{public}s:%i F0 version is 0, treating as unprogrammed."
+ "%{public}s:%i Failed 0x%04llx"
+ "%{public}s:%i Failed to allocate TLV data"
+ "%{public}s:%i Failed to clear E0 tag : %d"
+ "%{public}s:%i Failed to create page content"
+ "%{public}s:%i Failed to get FDR data : no data."
+ "%{public}s:%i Failed to get boot measurements"
+ "%{public}s:%i Failed to get factory page : %d"
+ "%{public}s:%i Failed to get page : 0x%04llx"
+ "%{public}s:%i Failed to query FW info !"
+ "%{public}s:%i Failed to query chip info. Bailing"
+ "%{public}s:%i Failed to read clock register"
+ "%{public}s:%i Failed to set A1DF: 0x%08llx"
+ "%{public}s:%i Failed to set XTAL clock source"
+ "%{public}s:%i Failed to write RF cal data A to NFCC"
+ "%{public}s:%i Failed to write RF cal data B to NFCC"
+ "%{public}s:%i Failed to write page : 0x%04llx"
+ "%{public}s:%i HFSR=0x%04x SFAR=0x%04x SFSR=0x%04x"
+ "%{public}s:%i Invalid clock register response"
+ "%{public}s:%i Invalid length %d for tag 0x%x: only %zu remaingin"
+ "%{public}s:%i MFW factory page config notification received : NULL"
+ "%{public}s:%i MSPL=0x%04x PSPL=0x%04x PMR=0x%04x"
+ "%{public}s:%i Platform does not have boot measurements"
+ "%{public}s:%i RF settings = %s"
+ "%{public}s:%i RTID Debug mode enabled"
+ "%{public}s:%i Re-configuring XTAL clock source"
+ "%{public}s:%i Received SRAM REPAIR %s notification"
+ "%{public}s:%i This feature is restricted to internal builds."
+ "%{public}s:%i Truncated tag found. Tag 0x%02x, tlvLen: %d, idx: %d, len: %d"
+ "%{public}s:%i Unable to find config tag info for tag 0x%02x"
+ "%{public}s:%i Using cached dieID"
+ "%{public}s:%i Using local RF settings"
+ "%{public}s:%i Warning : B state cal data was written with A state values. Applying .."
+ "%{public}s:%i Warning : B state cal data was written with A state values. Skipping .."
+ "%{public}s:%i Warning : B state cal data was written with A state values. Updating tags ..."
+ "(options & (NFDriverCustomerFactoryPageLock | NFDriverCustomerFactoryPageDebug)) == 0"
+ "A0130419191919A00D03610982A06A1000000000000078000000000000000000A09808D9DB098019171717A0AF0911FFF419117DA01902A09E0C07001D960090012BD0070000A0940A072003a200314f001902A0682A064060031914204000930418FF7FFF7F94038404D902840307FA000000350008007D00003500000E0003"
+ "A0130419191919A00D03610982A06A1000000000000078000000000000000000A09808EFB50B8019171717A0AF0911FFF419117DA01902A09E0C07001D960090012BD0070000A0940A072003a200314f001902A0682A064060031914204000930418FF7FFF7F8D096E06D8076B0507FA000000350008007D00003500000E0003"
+ "A0130419191919A00D03610982A09808C0f9088019171717A09E0C07001D960090012BD0070000A0AF0911FFF0191196A01902A06A1000000000000064000000000000000000A0682A064060031914204000930418603F204D450330030B031A0307FA000000350008007D00003500000E0003A0940A072003a200314f001902"
+ "A0130428282828A0AF09116FB0281159B02802A098086FF10B8028171717A09E0C07401F9600FA002B52030000A12E03838322A0682A06406003191420400093041880578057E000C000C000A00007FA000000350008007D00003500000E0003A06A1000000000000064000000000000000000A0A840003333100033231000332410E6113210C5224310C5224310C5224310C5224310C5224310C522431000332210C022231000332210C02223100033541000335410B0130428282828B0AF09116FA0281159A02802B098084B04068028171717B09E0C07401F9600FA002B08070000B12E03838322B0682A064060031914204000930418004B004BE0007F00E0007F0007FA000000350008007D00003500000E0003B06A1000000000000064000000000000000000B0A840003333100033231000332410E6113210DF224310DF224310DF224310DF224310DF224310DF22431000332210E622231000332210E62223100033541000335410"
+ "A0130428282828A12E03838322A09808A4580D80286A6A6AA09E0C07401F9600FA002B52030000A0AF091178B0281159B02802A06A100000000000003C000000000000000000A0682A0640600319142040009304187A1D863D9C00A30077007D0007FA000000350008007D00003500000E0003"
+ "A0130428282828A12E03838322A09808ACF00D8028B1B1B1A09E0C07401F9600FA002B52030000A0AF091178B0281159B02802A06A10000000000000C8000000000000000000A0682A0640600319142040009304180044804CC800B200B100AB0007FA000000350008007D00003500000E0003"
+ "A10A0151"
+ "Customer factory page (all TLVs)"
+ "FAILURE"
+ "Failed to write page :"
+ "MFW factory page config notification received"
+ "NFDriverClearFactoryPageE0Tag"
+ "NFDriverCustomerFactoryPage.c"
+ "NFDriverCustomerFactoryPageIsUnlocked"
+ "NFDriverFactoryPageHasExpectedConfigForTag"
+ "NFDriverFactoryPageHasProductionContent"
+ "NFDriverGetBootMeasurements"
+ "NFDriverGetFactoryPage"
+ "NFDriverGetInternal(driver)->hwInfo != NULL"
+ "NFDriverGetRFState"
+ "NFDriverSetRFState"
+ "NFDriverWriteFactoryPage"
+ "SUCCESS"
+ "ShSA"
+ "ShSB"
+ "Successfully updated page with content : "
+ "Writing customer factory page :"
+ "_Async_NFDriverGetBootMeasurements_block_invoke"
+ "_Async_NFDriverGetSecureFWInfo_block_invoke"
+ "_NFBootStopInterruptCallback"
+ "_NFDriverConfigureBBClockSource"
+ "_NFDriverCustomerFactoryPageFindTLV"
+ "_NFDriverEnableMultiRFSettings"
+ "_NFDriverGetSecureFWInfo"
+ "_NFDriverRFSettingsApplyFDR3CalData"
+ "_NFDriverTranslateRF"
+ "_NFDriverUpdateFactoryPage"
+ "alternate"
+ "default"
- "%s:%i Disabling multi-tag polling"
- "%s:%i Enabling multi-tag polling"
- "%{public}s:%i Disabling multi-tag polling"
- "%{public}s:%i Enabling multi-tag polling"
```
