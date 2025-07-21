## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

 12412.1.0.0.0
-  __TEXT.__text: 0xba240
-  __TEXT.__auth_stubs: 0x1760
+  __TEXT.__text: 0xb9b0c
+  __TEXT.__auth_stubs: 0x1740
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__const: 0xddbe
-  __TEXT.__cstring: 0x1235f
-  __TEXT.__gcc_except_tab: 0x11134
-  __TEXT.__oslogstring: 0x2017
-  __TEXT.__unwind_info: 0x4878
+  __TEXT.__cstring: 0x121cd
+  __TEXT.__gcc_except_tab: 0x11100
+  __TEXT.__oslogstring: 0x1efb
+  __TEXT.__unwind_info: 0x4860
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methname: 0x3bc
   __TEXT.__objc_methtype: 0x344
   __TEXT.__objc_stubs: 0x360
   __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x6db8
+  __DATA_CONST.__const: 0x6d10
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xbc0
-  __AUTH_CONST.__const: 0x135e8
+  __AUTH_CONST.__auth_got: 0xbb0
+  __AUTH_CONST.__const: 0x135b0
   __AUTH_CONST.__cfstring: 0x2b80
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E8EE735F-D7E7-32F0-8823-5DB6C25A73A8
+  UUID: 5482D9CF-FFF6-3B7D-9FFE-802C6F2C6372
   Functions: 5386
-  Symbols:   12444
-  CStrings:  4575
+  Symbols:   12440
+  CStrings:  4542
 
Symbols:
+ _.str.109
+ _.str.110
+ _.str.114
+ _.str.84
+ _.str.85
+ ___TUAssertTrigger
- _.str.112
- _.str.113
- _.str.94
- _.str.95
- _TelephonyUtilIsOversteerEnabled
- __ZNK3xpc6object9to_stringEv
- __ZZ29cellularInterfaceNameForIndexiE24kOversteerInterfaceNames
- __os_log_debug_impl
Functions:
~ __ZN10subscriber9isSimDeadENS_8SimStateE : 88 -> 64
~ __ZN10subscriber12isSimPresentENS_8SimStateE : 88 -> 64
~ __Z25PersonalityIdFromSlotIdExRKNSt3__110shared_ptrIK8RegistryEEN10subscriber7SimSlotE : 1084 -> 700
~ __ZN10subscriber15isSimUnreadableENS_8SimStateE : 88 -> 64
~ __ZN10subscriber10isSimReadyENS_8SimStateE : 88 -> 64
~ __ZN10subscriber11isSimAbsentENS_8SimStateE : 88 -> 64
~ __Z34getActiveFakePositiveInterfaceName18DataConnectionType : 88 -> 28
~ __Z17getGsm7TableIndexN3sms12TextEncodingE : 88 -> 64
~ __ZN13CSIPDPManager20getInterfaceNameByIdEiRNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 124 -> 88
~ __ZN16HelperRestServer17handleRestMessageERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictE : 688 -> 540
~ __ZN16HelperRestServer26handleRestMessageWithReplyERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictENS0_8functionIFvNS7_6objectEEEE : 772 -> 616
~ __ZN16HelperRestServer23handleDroppedConnectionERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc6objectE : 440 -> 360
~ __ZNK20FeatureConfiguration40isFakingSuccessfulBasebandRequestEnabledEv : 4 -> 8
~ __ZN19SignalStrengthModel11handleInputENSt3__110shared_ptrIK6InputsEE : 480 -> 248
~ __ZNK13DisplayStatus9dumpStateEPKN3ctu11OsLogLoggerE : 252 -> 4
~ __ZN10subscriber21isSimInTransientStateENS_8SimStateE : 84 -> 60
~ __ZN10subscriber13isSimInsertedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber12isSimSettledENS_8SimStateE : 88 -> 64
~ __ZN10subscriber11isSimLockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber18isSimReadyOrLockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber23isSimPermanentlyBlockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber20isSimPresentAndValidENS_8SimStateE : 88 -> 64
~ __ZNK12BasicSimInfo22isEmptyEsimCapableCardEv : 116 -> 92
~ __ZN12OTASPService20sendOTASPSuccessToUIEv : 532 -> 464
~ __Z18isXLAT464InterfacePKc : 184 -> 168
~ __Z20getCLAT46IPv6AddressPKcRjPhRS0_ : 644 -> 624
~ __ZN9DataUtils27loadPlistFromBundleResourceEPKN3ctu11OsLogLoggerEPKc : 464 -> 400
CStrings:
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
