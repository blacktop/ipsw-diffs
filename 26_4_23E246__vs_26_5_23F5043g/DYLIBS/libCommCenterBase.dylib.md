## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-13173.1.3.0.0
-  __TEXT.__text: 0xc1e28
-  __TEXT.__auth_stubs: 0x1790
+13184.1.0.0.0
+  __TEXT.__text: 0xc2520
+  __TEXT.__auth_stubs: 0x17b0
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__const: 0xd030
-  __TEXT.__cstring: 0x12a0f
-  __TEXT.__gcc_except_tab: 0x11f94
-  __TEXT.__oslogstring: 0x20ff
-  __TEXT.__unwind_info: 0x4a58
+  __TEXT.__cstring: 0x12c21
+  __TEXT.__gcc_except_tab: 0x11fc8
+  __TEXT.__oslogstring: 0x2233
+  __TEXT.__unwind_info: 0x4a68
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methname: 0x3bc
   __TEXT.__objc_methtype: 0x2fa
   __TEXT.__objc_stubs: 0x360
   __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x7010
+  __DATA_CONST.__const: 0x70b8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH_CONST.__const: 0x139d8
+  __AUTH_CONST.__auth_got: 0xbe8
+  __AUTH_CONST.__const: 0x13a00
   __AUTH_CONST.__cfstring: 0x2aa0
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8922A512-E8B9-32A9-BE25-0CD6D9220D42
+  UUID: 4EB394C8-170A-3D73-8708-245910DFC6BE
   Functions: 5528
-  Symbols:   12515
-  CStrings:  4686
+  Symbols:   12520
+  CStrings:  4719
 
Symbols:
+ _.str.81
+ _.str.82
+ _TelephonyUtilIsOversteerEnabled
+ __ZNK3xpc6object9to_stringEv
+ __ZZ29cellularInterfaceNameForIndexiE24kOversteerInterfaceNames
+ __os_log_debug_impl
- ___TUAssertTrigger
Functions:
~ __ZN10subscriber15isSimUnreadableENS_8SimStateE : 64 -> 88
~ __ZN10subscriber11isSimAbsentENS_8SimStateE : 64 -> 88
~ __ZN10subscriber9isSimDeadENS_8SimStateE : 64 -> 88
~ __ZN10subscriber12isSimPresentENS_8SimStateE : 64 -> 88
~ __ZNK13DisplayStatus9dumpStateEPKN3ctu11OsLogLoggerE : 4 -> 200
~ __Z25PersonalityIdFromSlotIdExRKNSt3__110shared_ptrIK8RegistryEEN10subscriber7SimSlotE : 688 -> 1072
~ __ZN13CSIPDPManager20getInterfaceNameByIdEiRNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 88 -> 124
~ __ZN19SignalStrengthModel11handleInputENSt3__110shared_ptrIK6InputsEE : 248 -> 472
~ __Z34getActiveFakePositiveInterfaceName18DataConnectionType : 28 -> 88
~ __Z17getGsm7TableIndexN3sms12TextEncodingE : 64 -> 88
~ __ZN16HelperRestServer17handleRestMessageERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictE : 532 -> 680
~ __ZN16HelperRestServer26handleRestMessageWithReplyERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictENS0_8functionIFvNS7_6objectEEEE : 624 -> 780
~ __ZN16HelperRestServer23handleDroppedConnectionERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc6objectE : 352 -> 432
~ __ZNK20FeatureConfiguration40isFakingSuccessfulBasebandRequestEnabledEv : 8 -> 4
~ __ZN10subscriber21isSimInTransientStateENS_8SimStateE : 64 -> 88
~ __ZN10subscriber13isSimInsertedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber10isSimReadyENS_8SimStateE : 64 -> 88
~ __ZN10subscriber12isSimSettledENS_8SimStateE : 64 -> 88
~ __ZN10subscriber11isSimLockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber18isSimReadyOrLockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber23isSimPermanentlyBlockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber20isSimPresentAndValidENS_8SimStateE : 64 -> 88
~ __ZNK12BasicSimInfo22isEmptyEsimCapableCardEv : 92 -> 116
~ __ZN12OTASPService20sendOTASPSuccessToUIEv : 448 -> 516
~ __Z18isXLAT464InterfacePKc : 168 -> 184
~ __Z20getCLAT46IPv6AddressPKcRjPhRS0_ : 624 -> 644
~ __ZN9DataUtils27loadPlistFromBundleResourceEPKN3ctu11OsLogLoggerEPKc : 396 -> 460
CStrings:
+ "#D DisplayStatus [isOn=%{bool}d, isLocked=%{bool}d, isCoversheetActive=%{bool}d, isPasscodeSet=%{bool}d]"
+ "#D Getting main bundle"
+ "#D Input(%s) = %f"
+ "#D Personality Info: %s - %s"
+ "#D Sending OTASP success dialogue to UI"
+ "#D ThumperID: %s, info: %p"
+ "#D [conn %p] Connection closed."
+ "#D [conn %p] Got REST message: %s"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CSI/Source/Common/SmsPduEncoder.cpp"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/SubscriberDefinitions.cpp"
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
+ "not active"

```
