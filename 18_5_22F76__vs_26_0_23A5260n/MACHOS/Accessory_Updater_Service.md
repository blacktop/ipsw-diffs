## Accessory Updater Service

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/Accessory Updater Service.xpc/Accessory Updater Service`

```diff

-3196.122.1.0.0
-  __TEXT.__text: 0x74708
-  __TEXT.__auth_stubs: 0x1870
-  __TEXT.__objc_stubs: 0x2ce0
-  __TEXT.__objc_methlist: 0x2e64
-  __TEXT.__const: 0x5c80
+3476.0.6.0.1
+  __TEXT.__text: 0x774d0
+  __TEXT.__auth_stubs: 0x1860
+  __TEXT.__objc_stubs: 0x2d00
+  __TEXT.__objc_methlist: 0x2e8c
+  __TEXT.__const: 0x5c90
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__cstring: 0x163b1
-  __TEXT.__objc_methname: 0x364e
+  __TEXT.__cstring: 0x1701b
+  __TEXT.__objc_methname: 0x3672
   __TEXT.__objc_classname: 0xb12
-  __TEXT.__objc_methtype: 0xd02
-  __TEXT.__oslogstring: 0x1536
-  __TEXT.__unwind_info: 0x1808
-  __DATA_CONST.__auth_got: 0xc48
+  __TEXT.__objc_methtype: 0xd01
+  __TEXT.__oslogstring: 0x1562
+  __TEXT.__unwind_info: 0x1878
+  __DATA_CONST.__auth_got: 0xc40
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x2378
-  __DATA_CONST.__cfstring: 0xf500
+  __DATA_CONST.__const: 0x2ac8
+  __DATA_CONST.__cfstring: 0x10f40
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_intobj: 0x78
   __DATA.__objc_const: 0x54a0
-  __DATA.__objc_selrefs: 0xf58
+  __DATA.__objc_selrefs: 0xf68
   __DATA.__objc_ivar: 0x37c
   __DATA.__objc_data: 0x14f0
-  __DATA.__data: 0xaf0
+  __DATA.__data: 0xaf8
   __DATA.__bss: 0xa00
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E8964E1F-2F8F-3566-A26B-9CF2C04575DE
-  Functions: 2444
-  Symbols:   1800
-  CStrings:  6471
+  UUID: DD05C204-5D52-3EFB-B79D-3C5CD5548232
+  Functions: 2477
+  Symbols:   1836
+  CStrings:  6906
 
Symbols:
+ _AMAuthInstallApFtabIsValid
+ _AMAuthInstallApplyRecoveryRequestEntries
+ _AMBootedModeDeviceGetBoardID
+ _AMBootedModeDeviceGetChipID
+ _AMBootedModeDeviceGetProductionMode
+ _AMBootedModeDeviceGetTypeID
+ _AMBootedModeDeviceIsBootstrapOnly
+ _AMDFUModeDeviceGetTypeID
+ _AMGenericDeviceGetBoardID
+ _AMGenericDeviceGetChipID
+ _AMGenericDeviceGetProductionMode
+ _AMGenericDeviceIsBootstrapOnly
+ _AMPortDFUModeDeviceGetBoardID
+ _AMPortDFUModeDeviceGetChipID
+ _AMPortDFUModeDeviceGetTypeID
+ _AMPortDFUModeDeviceGetWrappedDFUDevice
+ _AMRAuthInstallInitOptionalFirmware
+ _AMRecoveryModeDeviceGetTypeID
+ _AMRestorePerformGenericDFURestore
+ _AMRestorePerformTADRestore
+ _AMTADModeDeviceCopyAuthInstallPreflightOptions
+ _AMTADModeDeviceGetBoardID
+ _AMTADModeDeviceGetChipID
+ _AMTADModeDeviceGetECID
+ _AMTADModeDeviceGetProductionMode
+ _AMTADModeDeviceGetTypeID
+ _AMTADModeDeviceIsBootstrapOnly
+ __AMRAuthInstallApplyOptionalFirmware
+ __AMRTADDeviceCopyEpochString
+ __AMRTADDeviceCopySerialNumber
+ _kAMAuthInstallApParameterAPTagOverrides
+ _kAMAuthInstallApParameterCertificateEpoch
+ _kAMAuthInstallApParameterSerialString
+ _kAMAuthInstallRecoveryRequestEntries
+ _libDFU_deviceEpochString
+ _libDFU_deviceNonceString
+ _libDFU_devicePID
+ _libDFU_deviceSerialNumberString
+ _libDFU_downloadToDevice
+ _objc_setProperty_atomic_copy
- _AMSupportCopyURLWithAppendedComponent
- _CFAllocatorCreate
- _image3Free
- _image3Malloc
CStrings:
+ "\tBoot Nonce: "
+ "%@ OptionalFirmware: %@"
+ "%lld"
+ "%s WARNING: port DFU boardID should never be queried (doesn't exist)"
+ "%s WARNING: the Port DFU ChipID should never be queried (doesn't exist)"
+ "AMAuthInstallApFtabIsValid"
+ "AMPortDFUModeDeviceGetBoardID"
+ "AMPortDFUModeDeviceGetChipID"
+ "AMTADModeDeviceCopyAuthInstallPreflightOptions"
+ "AOP2"
+ "AVISP1,ACIO"
+ "AVISP1,AOP"
+ "AVISP1,AudioLeft"
+ "AVISP1,AudioRight"
+ "AVISP1,DiagRTKitOS"
+ "AVISP1,Display"
+ "AVISP1,DisplaySec"
+ "AVISP1,ISP"
+ "AVISP1,LLB"
+ "AVISP1,LeapBinsDigestsArray"
+ "AVISP1,PERTOS"
+ "AVISP1,RTKitOS"
+ "AVISP1,SCodec"
+ "AVISP1,TMU"
+ "AVISP1,kmpi"
+ "Adding"
+ "Ap,AVD"
+ "Ap,ApplePMCFirmware"
+ "Ap,AppleTypeCPhyFirmware"
+ "Ap,AppleVideoEncoder0"
+ "Ap,AppleVideoEncoder1"
+ "Ap,AppleVideoEncoder2"
+ "Ap,AppleVideoEncoder3"
+ "Ap,AppleVideoEncoder4"
+ "Ap,AppleVideoEncoder5"
+ "Ap,AppleVideoEncoder6"
+ "Ap,AppleVideoEncoder7"
+ "Ap,AppleVideoEncoder8"
+ "Ap,CryptexInfoPlist"
+ "Ap,DisplayVendorCalibration"
+ "Ap,ExclaveOS"
+ "Ap,ExclaveOSIntegrityCatalog"
+ "Ap,ExclaveOSTrustCache"
+ "Ap,ExclaveOSVolume"
+ "Ap,LowPowerMode"
+ "Ap,MSRFirmware"
+ "Ap,MandoFW"
+ "Ap,RestoreDCP2"
+ "Ap,RestoreMSRFirmware"
+ "Ap,RestoreSecureM3Firmware"
+ "Ap,RestoreSecurePageTableMonitor"
+ "Ap,RestoreTrustedExecutionMonitor"
+ "Ap,RestorecL4"
+ "Ap,SCodec"
+ "Ap,SecureM3Firmware"
+ "Ap,XHC"
+ "ApTagOverrides"
+ "Audio1,RTKitOS"
+ "AudioAP1,ACIBT"
+ "AudioAP1,PhyBlueTooth"
+ "AudioAP1,RTKitOS"
+ "AudioAP1,RTKitOSFeature"
+ "AudioAP1,SoftwareBinaryDsp1"
+ "Baobab,BacklightController"
+ "Baobab,Cabal"
+ "Baobab,TCON"
+ "Baobab,Trinity"
+ "Buttons1,ButtonsFirmware"
+ "Cellular1,CdpAscDl"
+ "Cellular1,CdpAscUl"
+ "Cellular1,CdpHost"
+ "Cellular1,LLB"
+ "Cellular1,PMUFW"
+ "Cellular1,PMUFW2"
+ "Cellular1,RTKitOS"
+ "Cellular1,iBootData"
+ "CertificateEpoch"
+ "Cryptex1,AppOS"
+ "Cryptex1,AppTrustCache"
+ "Cryptex1,AppVolume"
+ "Cryptex1,CryptexInfoPlist"
+ "Cryptex1,GenericDmg"
+ "Cryptex1,GenericIntegrityCatalog"
+ "Cryptex1,GenericTrustCache"
+ "Cryptex1,GenericVolume"
+ "Cryptex1,MobileAssetBrainOS"
+ "Cryptex1,MobileAssetBrainTrustCache"
+ "Cryptex1,MobileAssetBrainVolume"
+ "Cryptex1,SystemOS"
+ "Cryptex1,SystemTrustCache"
+ "Cryptex1,SystemVolume"
+ "CryptexDMG"
+ "DMC,BaobabTCONPresets"
+ "DMC,BaobabTCONTrinityCabalLUTs"
+ "DMC,Firmware1"
+ "DMC,HarmonyDB"
+ "DMC,USBPDThunderboltFirmware"
+ "DMC,UsbHubFirmware"
+ "DMC,VCOMFirmware1"
+ "Entering AMRestorePerformTADRestore"
+ "FTAB Error: %s"
+ "Failed to read file %@: error=%d"
+ "HTTP Request Header: %@=%@"
+ "Rap,RTKitIOConfig"
+ "Rap,RTKitOS"
+ "Rap,RestoreRTKitOS"
+ "Rap,SoftwareBinaryDsp1"
+ "RecoveryRequestEntries"
+ "Removing"
+ "Removing %@ from the build identity"
+ "RequestedRecoveryEntitlements"
+ "SE,Bootloader"
+ "SE,Firmware"
+ "SE,MigrationOS"
+ "SE,OS"
+ "SE,RapRTKitOS"
+ "SE,RapSwBinDsp"
+ "SE,UpdatePayload"
+ "SepStage1"
+ "SerialString"
+ "Starting DFU Download for device in location 0x%x"
+ "T@\"NSData\",C,V_ecidData"
+ "T@\"NSData\",C,V_manifest"
+ "T@\"NSData\",C,V_nonce"
+ "T@\"NSNumber\",C,V_demote"
+ "T@\"NSNumber\",C,V_trustedOverride"
+ "Timer,AppleTypeCPhyFirmware,1"
+ "Timer,RTKitOS,1"
+ "UARP: TSS Request to default server"
+ "USBPortController1,USBFirmware"
+ "Wireless1,RTKitOS"
+ "YonkersIR1,SepObject"
+ "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?IIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}"
+ "_AMAuthInstallBundleCreateAbridgedEntries"
+ "_AMRAuthInstallBundleModifyFirmwareEntries"
+ "_AMRTADModeDeviceConfigureAuthInstall"
+ "acio"
+ "alpm"
+ "aop2"
+ "apmu"
+ "audl"
+ "audr"
+ "avdf"
+ "ave0"
+ "ave1"
+ "ave2"
+ "ave3"
+ "ave4"
+ "ave5"
+ "ave6"
+ "ave7"
+ "ave8"
+ "bklc"
+ "bstc"
+ "bsys"
+ "butn"
+ "c411"
+ "cabl"
+ "caos"
+ "casy"
+ "cdpd"
+ "cdph"
+ "cdpu"
+ "com.apple.private.restrict-post.HaywireAccessoryAttached"
+ "cpxd"
+ "csos"
+ "cssy"
+ "csys"
+ "dcp2"
+ "device does not have epochs."
+ "device has epochs."
+ "dfw1"
+ "disp"
+ "diss"
+ "drko"
+ "duhf"
+ "dutf"
+ "dven"
+ "dvf1"
+ "exic"
+ "exos"
+ "extc"
+ "exvl"
+ "failed to get dfuFileHandle"
+ "failed to set recovery entitlements"
+ "ftabData is invalid"
+ "ftabWriteData:error:"
+ "gdmg"
+ "ginc"
+ "ginf"
+ "gtcd"
+ "gtgv"
+ "icnf"
+ "isGreaterThan:"
+ "isys"
+ "kmpi"
+ "libDFU_deviceNonceString returned %d"
+ "libauthinstall_device-1104.0.0.0.1"
+ "mndo"
+ "msrf"
+ "msys"
+ "no"
+ "osab"
+ "pmcf"
+ "pmfw"
+ "rdc2"
+ "rkof"
+ "rmsr"
+ "rosi"
+ "rsm3"
+ "rspt"
+ "rtrx"
+ "rxcl"
+ "sebl"
+ "sefw"
+ "semo"
+ "seos"
+ "seph"
+ "sm3f"
+ "strc"
+ "syab"
+ "tcon"
+ "thrd"
+ "tprd"
+ "trab"
+ "trca"
+ "trcs"
+ "trin"
+ "ttld"
+ "unable to abridge the build identity"
+ "unable to get TAD device product ID - %d"
+ "usbf"
+ "x-intnt-apboardid"
+ "x-intnt-apchipid"
+ "x-intnt-apecid"
+ "x-intnt-approductionmode"
+ "x-intnt-apsecuritydomain"
+ "x-intnt-apsecuritymode"
+ "x-intnt-authuserid"
+ "x-intnt-buildvariant"
+ "x-intnt-certcepo"
+ "x-intnt-usbserialstr"
+ "xhcf"
+ "yes"
- "AMAuthInstallPlatformCopyURLWithAppendedComponent failed %d"
- "AMAuthInstallSupportCreateDictionaryFromFileURL failed %d"
- "Adding OptionalFirmware: %@"
- "Appending {%s : %s} to http header"
- "Automatically adding SEP:DisableStrongSSMAChecks entitlement for a dev board."
- "RealityDevice"
- "SupportedProductTypes"
- "SupportedProductTypes not a CFArray"
- "T@\"NSData\",&,V_ecidData"
- "T@\"NSData\",&,V_manifest"
- "T@\"NSData\",&,V_nonce"
- "T@\"NSNumber\",&,V_demote"
- "T@\"NSNumber\",&,V_trustedOverride"
- "^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHeader=SISS}I^?^?CIIIIIiI*I*}iiiC{uarpPayloadObj={UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}CIICi*Ii*I*I*IiI^vIC^vI}^{uarpProcessedPayloadObj}*IC*IC*III^{uarpPlatformRemoteEndpoint}^v^{uarpPlatformAsset}^{uarpProcessedTLV}}"
- "_AMRAuthInstallBundleAppendFirmwareEntriesToArrays"
- "com.apple.HaywireAccessoryAttached"
- "deviceinterfaced is supported on this OS."
- "libauthinstall_device-1049.100.23"
- "productType not a CFString"

```
