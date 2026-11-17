## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-13504.1.0.0.0
-  __TEXT.__text: 0xd1784
+13508.0.0.0.0
+  __TEXT.__text: 0xd149c
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0x110
-  __TEXT.__const: 0xce80
-  __TEXT.__cstring: 0x14b4a
-  __TEXT.__gcc_except_tab: 0x13e44
-  __TEXT.__oslogstring: 0x2849
-  __TEXT.__unwind_info: 0x5500
+  __TEXT.__const: 0xceb0
+  __TEXT.__cstring: 0x14976
+  __TEXT.__gcc_except_tab: 0x13e64
+  __TEXT.__oslogstring: 0x26f1
+  __TEXT.__unwind_info: 0x5508
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x76e8
+  __DATA_CONST.__const: 0x7650
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x218
-  __AUTH_CONST.__const: 0x14478
-  __AUTH_CONST.__cfstring: 0x2ce0
+  __AUTH_CONST.__const: 0x144e8
+  __AUTH_CONST.__cfstring: 0x2d20
   __AUTH_CONST.__objc_const: 0x200
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0xc48
+  __AUTH_CONST.__auth_got: 0xc38
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x70
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5755
-  Symbols:   9445
-  CStrings:  4504
+  Functions: 5766
+  Symbols:   9456
+  CStrings:  4474
 
Symbols:
+ __ZN28LazuliHealthMonitorInterface14addPushArrivalERK13PersonalityIDi
+ __ZN28LazuliHealthMonitorInterface17addMessageOutcomeERK13PersonalityIDRK17MessageHealthInfo
+ __ZN28LazuliHealthMonitorInterface21addProvisioningResultERK13PersonalityIDRK22ProvisioningHealthInfo
+ __ZN28LazuliHealthMonitorInterface22addPcscfConnectFailureERK13PersonalityID
+ __ZN28LazuliHealthMonitorInterface27addMessageEncryptionFailureERK13PersonalityID
+ __ZN2sd17getImsPhoneNumberERKNSt3__110shared_ptrIK8RegistryEERK13PersonalityIDb15QuickSwitchRoleRKNS1_I14CSIPhoneNumberEE
+ __ZN2sd30IMSConnectivityHelperInterface22restartPcscfResolutionEv
+ __ZNSt3__120__shared_ptr_emplaceI14CSIPhoneNumberNS_9allocatorIS1_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceI14CSIPhoneNumberNS_9allocatorIS1_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceI14CSIPhoneNumberNS_9allocatorIS1_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceI14CSIPhoneNumberNS_9allocatorIS1_EEED1Ev
+ __ZTINSt3__120__shared_ptr_emplaceI14CSIPhoneNumberNS_9allocatorIS1_EEEE
+ __ZTSNSt3__120__shared_ptr_emplaceI14CSIPhoneNumberNS_9allocatorIS1_EEEE
+ __ZTVNSt3__120__shared_ptr_emplaceI14CSIPhoneNumberNS_9allocatorIS1_EEEE
+ ___TUAssertTrigger
- _TelephonyUtilIsOversteerEnabled
- __ZNK3xpc6object9to_stringEv
- __ZZ29cellularInterfaceNameForIndexiE24kOversteerInterfaceNames
- __os_log_debug_impl
CStrings:
+ "AltPhoneNumber"
+ "kMessagesAppNotInstalled"
+ "kMlsControl"
+ "phonebook"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CSI/Source/Common/SmsPduEncoder.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/SubscriberDefinitions.cpp"
- "Assertion failure: ( %s ), in file %s, line: %d"
- "DisplayStatus [isOn=%{bool}d, isLocked=%{bool}d, isCoversheetActive=%{bool}d, isPasscodeSet=%{bool}d, isEffectivelyLocked=%{bool}d]"
- "Getting main bundle"
- "Input(%s) = %f"
- "Parsed %zu lines successfully"
- "Personality Info: %s - %s"
- "Sending OTASP success dialogue to UI"
- "ThumperID: %s, info: %p"
- "[conn %p] Connection closed."
- "[conn %p] Got REST message: %s"
- "feth0"
- "feth1"
- "feth10"
- "feth11"
- "feth12"
- "feth13"
- "feth14"
- "feth15"
- "feth16"
- "feth17"
- "feth18"
- "feth19"
- "feth2"
- "feth20"
- "feth3"
- "feth4"
- "feth5"
- "feth6"
- "feth7"
- "feth8"
- "feth9"
- "not active"
```
