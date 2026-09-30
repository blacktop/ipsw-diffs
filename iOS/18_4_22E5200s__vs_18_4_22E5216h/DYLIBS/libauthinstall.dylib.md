## libauthinstall.dylib

> `/usr/lib/libauthinstall.dylib`

```diff

-1049.100.21.0.0
-  __TEXT.__text: 0x93b20
-  __TEXT.__auth_stubs: 0x1880
+1049.100.22.0.0
+  __TEXT.__text: 0x9634c
+  __TEXT.__auth_stubs: 0x1900
   __TEXT.__objc_methlist: 0x27cc
-  __TEXT.__cstring: 0x1c575
-  __TEXT.__const: 0x6209
+  __TEXT.__cstring: 0x1cdc8
+  __TEXT.__const: 0x62e6
   __TEXT.__oslogstring: 0x518
-  __TEXT.__gcc_except_tab: 0x2e78
-  __TEXT.__unwind_info: 0x2560
+  __TEXT.__gcc_except_tab: 0x3170
+  __TEXT.__unwind_info: 0x2610
   __TEXT.__objc_classname: 0x8a8
   __TEXT.__objc_methname: 0x28ff
   __TEXT.__objc_methtype: 0x777
   __TEXT.__objc_stubs: 0x2380
-  __DATA_CONST.__got: 0x3b8
-  __DATA_CONST.__const: 0x22a0
+  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__const: 0x2488
   __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_selrefs: 0xb58
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0xc58
+  __AUTH_CONST.__auth_got: 0xc98
   __AUTH_CONST.__auth_ptr: 0x28
-  __AUTH_CONST.__const: 0x1218
-  __AUTH_CONST.__cfstring: 0xca60
+  __AUTH_CONST.__const: 0x1340
+  __AUTH_CONST.__cfstring: 0xcee0
   __AUTH_CONST.__objc_const: 0x4c18
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH.__objc_data: 0x1400
   __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0x328
-  __DATA.__data: 0x768
+  __DATA.__data: 0x8c8
   __DATA.__bss: 0xd90
   __DATA.__common: 0x10
   __DATA_DIRTY.__data: 0x38

   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 3138
-  Symbols:   4309
-  CStrings:  4887
+  Functions: 3165
+  Symbols:   4351
+  CStrings:  4968
 
Symbols:
+ _AMSupportCopySetValueForKeyPathInDict
+ __ZN3ctu2cf12dict_adapterC1EPK14__CFDictionaryb
+ __ZN3ctu2cf12dict_adapterD1Ev
+ __ZNK3ctu2cf11map_adapter7getBoolEPK10__CFStringb
+ __ZNSt3__14stolERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
+ __ZNSt3__1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
+ __ZTISt16invalid_argument
+ ___maskrune
+ _getopt_long
+ _optarg
+ _optind
+ _optreset
CStrings:
+ "%s::%s: Baseband Firmware override has wrong type %lu\n"
+ "%s::%s: BasebandUpdater Version: %s\n"
+ "%s::%s: Let's check if we need to take the regular bbticket vs prov flow\n"
+ "%s::%s: Prov flow\n"
+ "%s::%s: Regular bbticket flow\n"
+ "%s::%s: Tag %s doesn't exist -- continue...\n"
+ "%s::%s: failed to copy options\n"
+ "%s::%s: failed to create Baseband Firmware override key path (read)\n"
+ "%s::%s: failed to create Baseband Firmware override key path (write)\n"
+ "%s::%s: failed to create options cp\n"
+ "%s::%s: failed to init firmware\n"
+ "%s::%s: incorrect baseband prov info type\n"
+ "%s::%s: incorrect device info type\n"
+ "%s::%s: invalid type for %s\n"
+ "%s::%s: null device info\n"
+ "%s::%s: null error parameter\n"
+ "%s::%s: reset epro to false for all firmware file tags\n"
+ "%s::%s: rtkitos bundle data unavailable\n"
+ "%s::%s: security mode demotion disallowed for Baseband\n"
+ "@Cellular1,Ticket"
+ "Baseband"
+ "BasebandProvInfo"
+ "Cellular1,BbActivationBypassEnable"
+ "Cellular1,BbActivationManifestKeyHash"
+ "Cellular1,BbCalibrationEnable"
+ "Cellular1,BbFATPCalibrationEnable"
+ "Cellular1,BbFDRSecurityKeyHash"
+ "Cellular1,BbFactoryActivationManifestKeyHash"
+ "Cellular1,BbFactoryDebugEnable"
+ "Cellular1,BbProvisioningEnable"
+ "Cellular1,BbProvisioningManifestKeyHash"
+ "Cellular1,BoardID"
+ "Cellular1,CdpAscDl"
+ "Cellular1,CdpAscUl"
+ "Cellular1,CdpHost"
+ "Cellular1,ChipID"
+ "Cellular1,ECID"
+ "Cellular1,FDRAllowUnsealed"
+ "Cellular1,HardwareConfigLockOverride"
+ "Cellular1,L1CL1S"
+ "Cellular1,LLB"
+ "Cellular1,Nonce"
+ "Cellular1,PMUFW"
+ "Cellular1,PMUFW2"
+ "Cellular1,ProductionMode"
+ "Cellular1,ProvisioningFirmware"
+ "Cellular1,RTKitOS"
+ "Cellular1,Recipe"
+ "Cellular1,SecurityDomain"
+ "Cellular1,SecurityMode"
+ "Cellular1,Ticket"
+ "Cellular1,UID_MODE"
+ "Cellular1,iBSS"
+ "DebugArgs"
+ "HelsinkiRestore-56.4.13"
+ "SinopeRestoreHost"
+ "SinopeRestoreInfo"
+ "SinopeUpdaterCopyFirmware"
+ "SinopeUpdaterCreateRequest"
+ "SinopeUpdaterCreateRequest: failed to create request dict"
+ "SinopeUpdaterCreateRequest: failed to open firmware"
+ "SinopeUpdaterGetTags"
+ "VinylRestore-78~6715"
+ "allow-no-imeisv"
+ "apmu"
+ "bypass-nvm-sync"
+ "cdpd"
+ "cdph"
+ "cdpu"
+ "copyFirmware: failed to init firmware"
+ "copyFirmware: rtkitos bundle data unavailable"
+ "demote-prod"
+ "dfl:tnp:iuse"
+ "enable-transport-logs"
+ "force"
+ "force-fusing"
+ "gap "
+ "ignore-fusing-sec-boot-status"
+ "l1cs"
+ "libauthinstall_device-1049.100.22"
+ "no-timeout"
+ "ping-attempts"
+ "pmfw"
+ "prfw"
+ "rcpi"
- " beta"
- "HelsinkiRestore-56.4.12"
- "VinylRestore-78~6589"
- "libauthinstall_device-1049.100.21"

```
