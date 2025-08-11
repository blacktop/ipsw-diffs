## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-13090.3.0.0.0
-  __TEXT.__text: 0xc4c68
-  __TEXT.__auth_stubs: 0x1790
+13091.1.6.0.0
+  __TEXT.__text: 0xc45f0
+  __TEXT.__auth_stubs: 0x1770
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__const: 0xdb9e
-  __TEXT.__cstring: 0x12a2d
+  __TEXT.__cstring: 0x128d7
   __TEXT.__gcc_except_tab: 0x11f94
-  __TEXT.__oslogstring: 0x219e
-  __TEXT.__unwind_info: 0x4ae8
+  __TEXT.__oslogstring: 0x2082
+  __TEXT.__unwind_info: 0x4ad8
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methname: 0x3bc
   __TEXT.__objc_methtype: 0x2f6
   __TEXT.__objc_stubs: 0x360
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x6f10
+  __DATA_CONST.__const: 0x6e70
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH_CONST.__const: 0x139e8
+  __AUTH_CONST.__auth_got: 0xbc8
+  __AUTH_CONST.__const: 0x139d8
   __AUTH_CONST.__cfstring: 0x2a40
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F461B723-2898-345D-A5E3-9677372F3D88
-  Functions: 5530
-  Symbols:   12587
-  CStrings:  4689
+  UUID: 3AD93786-0D3C-36C6-98B7-4F9996E89D43
+  Functions: 5531
+  Symbols:   12584
+  CStrings:  4658
 
Symbols:
+ __Z29isCallSourceModeNeedDisableHO16CCCallSourceMode
+ ___TUAssertTrigger
- _.str.81
- _.str.82
- _TelephonyUtilIsOversteerEnabled
- __ZNK3xpc6object9to_stringEv
- __ZZ29cellularInterfaceNameForIndexiE24kOversteerInterfaceNames
- __os_log_debug_impl
Functions:
~ __ZN10subscriber15isSimUnreadableENS_8SimStateE : 88 -> 64
~ __ZN10subscriber11isSimAbsentENS_8SimStateE : 88 -> 64
~ __ZN10subscriber9isSimDeadENS_8SimStateE : 88 -> 64
~ __ZN10subscriber12isSimPresentENS_8SimStateE : 88 -> 64
~ __ZNK13DisplayStatus9dumpStateEPKN3ctu11OsLogLoggerE : 252 -> 4
~ __Z25PersonalityIdFromSlotIdExRKNSt3__110shared_ptrIK8RegistryEEN10subscriber7SimSlotE : 1084 -> 700
~ __ZN13CSIPDPManager20getInterfaceNameByIdEiRNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 124 -> 88
~ __ZN19SignalStrengthModel11handleInputENSt3__110shared_ptrIK6InputsEE : 480 -> 248
~ __Z34getActiveFakePositiveInterfaceName18DataConnectionType : 88 -> 28
~ __Z17getGsm7TableIndexN3sms12TextEncodingE : 88 -> 64
~ __ZN16HelperRestServer17handleRestMessageERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictE : 688 -> 540
~ __ZN16HelperRestServer26handleRestMessageWithReplyERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictENS0_8functionIFvNS7_6objectEEEE : 788 -> 632
~ __ZN16HelperRestServer23handleDroppedConnectionERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc6objectE : 440 -> 360
~ __ZNK20FeatureConfiguration40isFakingSuccessfulBasebandRequestEnabledEv : 4 -> 8
~ __Z16write_rest_valueRK19SetScreeningRequest : 428 -> 528
~ __Z15read_rest_valueR19SetScreeningRequestRKN3xpc6objectE : 440 -> 512
~ __ZN10subscriber21isSimInTransientStateENS_8SimStateE : 88 -> 64
~ __ZN10subscriber13isSimInsertedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber10isSimReadyENS_8SimStateE : 88 -> 64
~ __ZN10subscriber12isSimSettledENS_8SimStateE : 88 -> 64
~ __ZN10subscriber11isSimLockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber18isSimReadyOrLockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber23isSimPermanentlyBlockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber20isSimPresentAndValidENS_8SimStateE : 88 -> 64
~ __ZNK12BasicSimInfo22isEmptyEsimCapableCardEv : 116 -> 92
~ __ZN12OTASPService20sendOTASPSuccessToUIEv : 532 -> 464
~ __Z18isXLAT464InterfacePKc : 180 -> 164
~ __Z20getCLAT46IPv6AddressPKcRjPhRS0_ : 644 -> 624
+ __Z29isCallSourceModeNeedDisableHO16CCCallSourceMode
~ __ZN9DataUtils27loadPlistFromBundleResourceEPKN3ctu11OsLogLoggerEPKc : 464 -> 400
CStrings:
+ "CCCallSourceMode::kCCCallSourceModeScreeningNoHO"
+ "supportsHO"
- "#D DisplayStatus [isOn=%s, isLocked=%s, isCoversheetActive=%s, isPasscodeSet=%s]"
- "#D Getting main bundle"
- "#D Input(%s) = %f"
- "#D Personality Info: %s - %s"
- "#D Sending OTASP success dialogue to UI"
- "#D ThumperID: %s, info: %p"
- "#D [conn %p] Connection closed."
- "#D [conn %p] Got REST message: %s"
- "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CSI/Source/Common/SmsPduEncoder.cpp"
- "/Library/Caches/com.apple.xbs/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/SubscriberDefinitions.cpp"
- "Assertion failure: ( %s ), in file %s, line: %d"
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
