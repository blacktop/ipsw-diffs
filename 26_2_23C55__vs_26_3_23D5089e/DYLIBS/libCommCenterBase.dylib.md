## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-13126.1.1.0.0
-  __TEXT.__text: 0xc53e0
-  __TEXT.__auth_stubs: 0x1780
+13149.5.0.0.0
+  __TEXT.__text: 0xc5cd0
+  __TEXT.__auth_stubs: 0x17a0
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__const: 0xdbde
-  __TEXT.__cstring: 0x12a60
-  __TEXT.__gcc_except_tab: 0x12190
-  __TEXT.__oslogstring: 0x209f
-  __TEXT.__unwind_info: 0x4b40
+  __TEXT.__cstring: 0x12c0b
+  __TEXT.__gcc_except_tab: 0x121e8
+  __TEXT.__oslogstring: 0x21bb
+  __TEXT.__unwind_info: 0x4b60
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methname: 0x3bc
   __TEXT.__objc_methtype: 0x2fa
   __TEXT.__objc_stubs: 0x360
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x6f08
+  __DATA_CONST.__const: 0x6fd8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xbd0
-  __AUTH_CONST.__const: 0x13b88
+  __AUTH_CONST.__auth_got: 0xbe0
+  __AUTH_CONST.__const: 0x13bf8
   __AUTH_CONST.__cfstring: 0x2aa0
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BA9D8400-FC2F-3CAE-B9F7-56E0DF4C54C9
-  Functions: 5557
-  Symbols:   12631
-  CStrings:  4683
+  UUID: 7E377B24-C672-3956-92D1-75D5090E3B24
+  Functions: 5559
+  Symbols:   12639
+  CStrings:  4717
 
Symbols:
+ _.str.81
+ _.str.82
+ _TelephonyUtilIsOversteerEnabled
+ __ZN10subscriber10sDecodeSPNEPKhm
+ __ZN2sd8asStringENS_18RcsSwitchoverStateE
+ __ZNK3xpc6object9to_stringEv
+ __ZZ29cellularInterfaceNameForIndexiE24kOversteerInterfaceNames
+ __os_log_debug_impl
- ___TUAssertTrigger
Functions:
~ __ZN10subscriber15isSimUnreadableENS_8SimStateE : 64 -> 88
~ __ZN10subscriber11isSimAbsentENS_8SimStateE : 64 -> 88
~ __ZN10subscriber9isSimDeadENS_8SimStateE : 64 -> 88
~ __ZN10subscriber12isSimPresentENS_8SimStateE : 64 -> 88
~ __ZNK13DisplayStatus9dumpStateEPKN3ctu11OsLogLoggerE : 4 -> 252
~ __Z25PersonalityIdFromSlotIdExRKNSt3__110shared_ptrIK8RegistryEEN10subscriber7SimSlotE : 700 -> 1084
~ __ZN13CSIPDPManager20getInterfaceNameByIdEiRNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 88 -> 124
~ __ZN19SignalStrengthModel11handleInputENSt3__110shared_ptrIK6InputsEE : 248 -> 480
~ __Z34getActiveFakePositiveInterfaceName18DataConnectionType : 28 -> 88
~ __Z17getGsm7TableIndexN3sms12TextEncodingE : 64 -> 88
~ __ZN16HelperRestServer17handleRestMessageERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictE : 540 -> 688
~ __ZN16HelperRestServer26handleRestMessageWithReplyERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictENS0_8functionIFvNS7_6objectEEEE : 632 -> 788
~ __ZN16HelperRestServer23handleDroppedConnectionERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc6objectE : 360 -> 440
~ __ZNK20FeatureConfiguration40isFakingSuccessfulBasebandRequestEnabledEv : 8 -> 4
~ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne200100IPKhS6_EEvT_T0_m : 152 -> 116
~ __GLOBAL__sub_I_VinylDefinitions.cpp : 268 -> 276
~ __ZN10subscriber21isSimInTransientStateENS_8SimStateE : 64 -> 88
~ __ZN10subscriber13isSimInsertedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber10isSimReadyENS_8SimStateE : 64 -> 88
~ __ZN10subscriber12isSimSettledENS_8SimStateE : 64 -> 88
~ __ZN10subscriber11isSimLockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber18isSimReadyOrLockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber23isSimPermanentlyBlockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber20isSimPresentAndValidENS_8SimStateE : 64 -> 88
~ __ZNK12BasicSimInfo22isEmptyEsimCapableCardEv : 92 -> 116
~ __ZN12OTASPService20sendOTASPSuccessToUIEv : 464 -> 532
+ __ZN2sd8asStringENS_21ImsRegistrationStatus8CategoryE
+ __ZN10subscriber10sDecodeSPNEPKhm
~ __Z18isXLAT464InterfacePKc : 164 -> 180
~ __Z20getCLAT46IPv6AddressPKcRjPhRS0_ : 624 -> 644
~ __ZN10subscriberL7initGSMERNSt3__113unordered_mapINS_11SimFilePathENS_6FileIdENS0_4hashIS2_EENS0_8equal_toIS2_EENS0_9allocatorINS0_4pairIKS2_S3_EEEEEEt : 5220 -> 5408
~ __ZN9DataUtils27loadPlistFromBundleResourceEPKN3ctu11OsLogLoggerEPKc : 400 -> 464
CStrings:
+ "#D DisplayStatus [isOn=%s, isLocked=%s, isCoversheetActive=%s, isPasscodeSet=%s]"
+ "#D Getting main bundle"
+ "#D Input(%s) = %f"
+ "#D Personality Info: %s - %s"
+ "#D Sending OTASP success dialogue to UI"
+ "#D ThumperID: %s, info: %p"
+ "#D [conn %p] Connection closed."
+ "#D [conn %p] Got REST message: %s"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CSI/Source/Common/SmsPduEncoder.cpp"
+ "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/SubscriberDefinitions.cpp"
+ "Assertion failure: ( %s ), in file %s, line: %d"
+ "feth0"
+ "feth1"
+ "feth10"
+ "feth11"
+ "feth12"
+ "feth13"
+ "feth14"
+ "feth15"
+ "feth16"
+ "feth17"
+ "feth18"
+ "feth19"
+ "feth2"
+ "feth20"
+ "feth3"
+ "feth4"
+ "feth5"
+ "feth6"
+ "feth7"
+ "feth8"
+ "feth9"
+ "kSimFile_SPN"
+ "not active"

```
