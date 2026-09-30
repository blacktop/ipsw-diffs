## libSavageRestoreInfo_iOS.dylib

> `/usr/lib/updaters/libSavageRestoreInfo_iOS.dylib`

```diff

-6.35.5.0.0
-  __TEXT.__text: 0x4630
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__cstring: 0x160e
-  __TEXT.__const: 0x1f0
-  __TEXT.__unwind_info: 0xd0
+6.71.100.0.0
+  __TEXT.__text: 0x5f20
+  __TEXT.__auth_stubs: 0x420
+  __TEXT.__cstring: 0x1c35
+  __TEXT.__const: 0x290
+  __TEXT.__unwind_info: 0xe8
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__const: 0x3a0
-  __AUTH_CONST.__auth_got: 0x218
-  __AUTH_CONST.__cfstring: 0xf20
+  __DATA_CONST.__const: 0x4d8
+  __AUTH_CONST.__auth_got: 0x210
+  __AUTH_CONST.__cfstring: 0x1440
   __DATA.__data: 0x15d
   __DATA.__common: 0x1000
   __DATA.__bss: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: A3741F9F-9313-32B6-A4DD-9A535DE5BD1B
-  Functions: 37
-  Symbols:   268
-  CStrings:  314
+  UUID: 95BB01C5-0009-31B6-8BF3-896D7749AA07
+  Functions: 48
+  Symbols:   328
+  CStrings:  406
 
Symbols:
+ _CreateJasmineIRMeasurementDict
+ _CreateJasmineIRMeasurementDictVT
+ _CreateJasmineIRRequestDictForTATSU
+ _GetJasmineIRFabRevisionTags
+ _GetJasmineIRMeasurementTags
+ _JasmineIRAddEntitlementsToTATSURequestDict
+ _OUTLINED_FUNCTION_4
+ __ZL19_computePatchDigestPKhmPh
+ _kJasmineIR1DeviceInfo
+ _kJasmineIR1FirmwareData
+ _kJasmineIR1FirmwareDataVT
+ _kJasmineIR1TagAccessSecurity
+ _kJasmineIR1TagAccessSensor
+ _kJasmineIR1TagAllowEntropyTest
+ _kJasmineIR1TagAllowNonEncryptedImages
+ _kJasmineIR1TagAllowOfflineBoot
+ _kJasmineIR1TagAllowTamperOverride
+ _kJasmineIR1TagAuthenticate
+ _kJasmineIR1TagCertificateEpoch
+ _kJasmineIR1TagDebugRegisterAccess
+ _kJasmineIR1TagDebugStatus
+ _kJasmineIR1TagDeviceBoardID
+ _kJasmineIR1TagDeviceChipID
+ _kJasmineIR1TagDeviceECID
+ _kJasmineIR1TagDeviceFabRevision
+ _kJasmineIR1TagDeviceNonce
+ _kJasmineIR1TagDeviceProductionMode
+ _kJasmineIR1TagDeviceRootPublicKeyIdentifier
+ _kJasmineIR1TagFADemote
+ _kJasmineIR1TagFdrRootCaDigest
+ _kJasmineIR1TagHarvestUnwrap
+ _kJasmineIR1TagHarvestWrap
+ _kJasmineIR1TagPatchEpoch
+ _kJasmineIR1TagProvisioning
+ _kJasmineIR1TagReadECKey
+ _kJasmineIR1TagReadFWKey
+ _kJasmineIR1TagReadGID
+ _kJasmineIR1TagRequestTicket
+ _kJasmineIR1TagResponseTicket
+ _kJasmineIR1TagTempDemote
+ _kJasmineIR1TagWriteECID
+ _kJasmineIR1TagWriteECKey
+ _kJasmineIR1TagWriteEpoch
+ _kJasmineIRErrorDomain
+ _kJasmineIRPreflightRequiredOption
+ _kJasmineIRSkipOption
+ _kJasmineIRTagDeviceUID
- _CFDictionaryGetCount
CStrings:
+ "%s [input]: JasmineIRMeasurementDict - %s \n"
+ "%s [input]: JasmineIRVTMeasurementDict - %s \n"
+ "@JasmineIR1,Ticket"
+ "JasmineIR1,AccessSecurity"
+ "JasmineIR1,AccessSensor"
+ "JasmineIR1,AllowEntropyTest"
+ "JasmineIR1,AllowNonEncryptedImages"
+ "JasmineIR1,AllowOfflineBoot"
+ "JasmineIR1,AllowTamperOverride"
+ "JasmineIR1,Authenticate"
+ "JasmineIR1,BoardID"
+ "JasmineIR1,CertificateEpoch"
+ "JasmineIR1,ChipID"
+ "JasmineIR1,DebugRegisterAccess"
+ "JasmineIR1,DebugStatus"
+ "JasmineIR1,ECID"
+ "JasmineIR1,FADemote"
+ "JasmineIR1,FabRevision"
+ "JasmineIR1,FdrRootCaDigest"
+ "JasmineIR1,FwPatch%X"
+ "JasmineIR1,HarvestUnwrap"
+ "JasmineIR1,HarvestWrap"
+ "JasmineIR1,Nonce"
+ "JasmineIR1,PatchEpoch"
+ "JasmineIR1,ProductionMode"
+ "JasmineIR1,Provisioning"
+ "JasmineIR1,ReadECKey"
+ "JasmineIR1,ReadFWKey"
+ "JasmineIR1,ReadGID"
+ "JasmineIR1,RootKeyIdentifier"
+ "JasmineIR1,SepObject"
+ "JasmineIR1,TempDemote"
+ "JasmineIR1,Ticket"
+ "JasmineIR1,UID"
+ "JasmineIR1,VideoPatch%X"
+ "JasmineIR1,WriteECID"
+ "JasmineIR1,WriteECKey"
+ "JasmineIR1,WriteEpoch"
+ "JasmineIR1DeviceInfo"
+ "JasmineIR1Firmware"
+ "JasmineIR1FirmwareVT"
+ "JasmineIRErrorDomain"
+ "JasmineIRIsProvisioned"
+ "SavageUpdaterCopyFirmware: Cannot allocate memoty for outputDict"
+ "SavageUpdaterCopyFirmware: Didn't get jasmine ir patch measurement tags"
+ "SavageUpdaterCopyFirmware: Empty JasmineIR VT firmware file?"
+ "SavageUpdaterCopyFirmware: Empty JasmineIR firmware file?"
+ "SavageUpdaterCreateRequest: CreateJasmineIRRequestDictForTATSU fails."
+ "SavageUpdaterCreateRequest: CreateMeasurementDict fails for JasmineIR for VT Patch."
+ "SavageUpdaterCreateRequest: CreateMeasurementDict fails for JasmineIR."
+ "SavageUpdaterGetTags: Unable to get kJasmineIRTagMeasurementPatch"

```
