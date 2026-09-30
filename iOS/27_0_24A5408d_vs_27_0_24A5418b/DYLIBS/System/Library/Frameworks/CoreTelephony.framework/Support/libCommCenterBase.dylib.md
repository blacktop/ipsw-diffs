## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-13487.3.0.0.0
-  __TEXT.__text: 0xd2ff4
+13487.6.0.0.0
+  __TEXT.__text: 0xd293c
   __TEXT.__init_offsets: 0x20
   __TEXT.__objc_methlist: 0x110
-  __TEXT.__const: 0xd370
-  __TEXT.__cstring: 0x14ac8
-  __TEXT.__gcc_except_tab: 0x13be4
-  __TEXT.__oslogstring: 0x2849
-  __TEXT.__unwind_info: 0x4e60
+  __TEXT.__const: 0xd360
+  __TEXT.__cstring: 0x148cb
+  __TEXT.__gcc_except_tab: 0x13bc4
+  __TEXT.__oslogstring: 0x26f1
+  __TEXT.__unwind_info: 0x4e58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x76e0
+  __DATA_CONST.__const: 0x7640
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_selrefs: 0x188
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__got: 0x218
-  __AUTH_CONST.__const: 0x14480
+  __AUTH_CONST.__const: 0x14448
   __AUTH_CONST.__cfstring: 0x2ce0
   __AUTH_CONST.__objc_const: 0x200
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0xc38
+  __AUTH_CONST.__auth_got: 0xc28
   __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x70
   __DATA.__bss: 0x5

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 5765
-  Symbols:   9507
-  CStrings:  4497
+  Symbols:   9504
+  CStrings:  4464
 
Symbols:
+ ___TUAssertTrigger
- _TelephonyUtilIsOversteerEnabled
- __ZNK3xpc6object9to_stringEv
- __ZZ29cellularInterfaceNameForIndexiE24kOversteerInterfaceNames
- __os_log_debug_impl
Functions:
~ __ZN10subscriber9isSimDeadENS_8SimStateE : 88 -> 64
~ __ZN10subscriber12isSimPresentENS_8SimStateE : 88 -> 64
~ __Z25PersonalityIdFromSlotIdExRKNSt3__110shared_ptrIK8RegistryEEN10subscriber7SimSlotE : 1012 -> 688
~ __ZNK13DisplayStatus9dumpStateEPKN3ctu11OsLogLoggerE : 172 -> 4
~ __ZN13CSIPDPManager20getInterfaceNameByIdEiRNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 124 -> 88
~ __ZN19SignalStrengthModel11handleInputENSt3__110shared_ptrIK6InputsEE : 424 -> 248
~ __ZN16HelperRestServer17handleRestMessageERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictE : 680 -> 532
~ __ZN16HelperRestServer26handleRestMessageWithReplyERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictENS0_8functionIFvNS7_6objectEEEE : 780 -> 624
~ __ZN16HelperRestServer23handleDroppedConnectionERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc6objectE : 432 -> 352
~ __Z34getActiveFakePositiveInterfaceName18DataConnectionType : 88 -> 28
~ __Z17getGsm7TableIndexN3sms12TextEncodingE : 88 -> 64
~ __ZNK20FeatureConfiguration40isFakingSuccessfulBasebandRequestEnabledEv : 4 -> 8
~ __ZN10subscriber21isSimInTransientStateENS_8SimStateE : 88 -> 64
~ __ZN10subscriber11isSimAbsentENS_8SimStateE : 88 -> 64
~ __ZN10subscriber13isSimInsertedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber15isSimUnreadableENS_8SimStateE : 88 -> 64
~ __ZN10subscriber10isSimReadyENS_8SimStateE : 88 -> 64
~ __ZN10subscriber12isSimSettledENS_8SimStateE : 88 -> 64
~ __ZN10subscriber11isSimLockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber18isSimReadyOrLockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber23isSimPermanentlyBlockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber20isSimPresentAndValidENS_8SimStateE : 88 -> 64
~ __ZNK12BasicSimInfo22isEmptyEsimCapableCardEv : 116 -> 92
~ __ZN12OTASPService20sendOTASPSuccessToUIEv : 516 -> 448
~ __ZN10LineParser15parseFromStreamEPKN3ctu11OsLogLoggerERNSt3__113basic_istreamIcNS4_11char_traitsIcEEEENS4_8functionIFvRKNS4_12basic_stringIcS7_NS4_9allocatorIcEEEEEEE : 2356 -> 2284
~ __Z18isXLAT464InterfacePKc : 184 -> 168
~ __Z20getCLAT46IPv6AddressPKcRjPhRS0_ : 608 -> 588
~ __ZN9DataUtils27loadPlistFromBundleResourceEPKN3ctu11OsLogLoggerEPKc : 460 -> 396
CStrings:
+ "kNotSupportedInBuddy"
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
