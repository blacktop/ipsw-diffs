## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-13171.6.0.0.0
-  __TEXT.__text: 0xc24ac
-  __TEXT.__auth_stubs: 0x17b0
+13172.1.3.0.0
+  __TEXT.__text: 0xc1dec
+  __TEXT.__auth_stubs: 0x1790
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__const: 0xd030
-  __TEXT.__cstring: 0x12be0
-  __TEXT.__gcc_except_tab: 0x11fc8
-  __TEXT.__oslogstring: 0x2233
-  __TEXT.__unwind_info: 0x4a68
+  __TEXT.__cstring: 0x129ce
+  __TEXT.__gcc_except_tab: 0x11f94
+  __TEXT.__oslogstring: 0x20ff
+  __TEXT.__unwind_info: 0x4a58
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methname: 0x3bc
   __TEXT.__objc_methtype: 0x2fa
   __TEXT.__objc_stubs: 0x360
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x7098
+  __DATA_CONST.__const: 0x6ff0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xbe8
-  __AUTH_CONST.__const: 0x139e8
+  __AUTH_CONST.__auth_got: 0xbd8
+  __AUTH_CONST.__const: 0x139c0
   __AUTH_CONST.__cfstring: 0x2aa0
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C1378278-A8E4-356D-9B9B-1EBE33E2C7A8
-  Functions: 5525
-  Symbols:   12517
-  CStrings:  4715
+  UUID: 23771B69-E513-3E53-9A7D-2CC8FAF83F08
+  Functions: 5526
+  Symbols:   12513
+  CStrings:  4682
 
Symbols:
+ __ZNK16CSIPacketAddress20isUniqueLocalAddressEv
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
~ __ZNK13DisplayStatus9dumpStateEPKN3ctu11OsLogLoggerE : 200 -> 4
~ __Z25PersonalityIdFromSlotIdExRKNSt3__110shared_ptrIK8RegistryEEN10subscriber7SimSlotE : 1072 -> 688
~ __ZN13CSIPDPManager20getInterfaceNameByIdEiRNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 124 -> 88
~ __ZN19SignalStrengthModel11handleInputENSt3__110shared_ptrIK6InputsEE : 472 -> 248
~ __Z15read_rest_valueR15CallDialRequestRKN3xpc6objectE : 1316 -> 1320
~ __Z34getActiveFakePositiveInterfaceName18DataConnectionType : 88 -> 28
~ __Z17getGsm7TableIndexN3sms12TextEncodingE : 88 -> 64
~ __ZN16HelperRestServer17handleRestMessageERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictE : 680 -> 532
~ __ZN16HelperRestServer26handleRestMessageWithReplyERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictENS0_8functionIFvNS7_6objectEEEE : 780 -> 624
~ __ZN16HelperRestServer23handleDroppedConnectionERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc6objectE : 432 -> 352
~ __ZNK20FeatureConfiguration40isFakingSuccessfulBasebandRequestEnabledEv : 4 -> 8
+ __ZNK16CSIPacketAddress20isUniqueLocalAddressEv
~ __ZN10subscriber21isSimInTransientStateENS_8SimStateE : 88 -> 64
~ __ZN10subscriber13isSimInsertedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber10isSimReadyENS_8SimStateE : 88 -> 64
~ __ZN10subscriber12isSimSettledENS_8SimStateE : 88 -> 64
~ __ZN10subscriber11isSimLockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber18isSimReadyOrLockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber23isSimPermanentlyBlockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber20isSimPresentAndValidENS_8SimStateE : 88 -> 64
~ __ZNK12BasicSimInfo22isEmptyEsimCapableCardEv : 116 -> 92
~ __ZN12OTASPService20sendOTASPSuccessToUIEv : 516 -> 448
~ __Z18isXLAT464InterfacePKc : 184 -> 168
~ __Z20getCLAT46IPv6AddressPKcRjPhRS0_ : 644 -> 624
~ __ZN8CallInfoC2ERKS_ : 792 -> 800
~ __ZN9DataUtils27loadPlistFromBundleResourceEPKN3ctu11OsLogLoggerEPKc : 460 -> 396
CStrings:
- "#D DisplayStatus [isOn=%{bool}d, isLocked=%{bool}d, isCoversheetActive=%{bool}d, isPasscodeSet=%{bool}d]"
- "#D Getting main bundle"
- "#D Input(%s) = %f"
- "#D Personality Info: %s - %s"
- "#D Sending OTASP success dialogue to UI"
- "#D ThumperID: %s, info: %p"
- "#D [conn %p] Connection closed."
- "#D [conn %p] Got REST message: %s"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CSI/Source/Common/SmsPduEncoder.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/SubscriberDefinitions.cpp"
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
