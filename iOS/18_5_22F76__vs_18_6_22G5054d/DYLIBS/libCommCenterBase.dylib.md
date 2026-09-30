## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

```diff

-12410.0.0.0.0
-  __TEXT.__text: 0xb9b0c
-  __TEXT.__auth_stubs: 0x1740
+12412.0.0.0.0
+  __TEXT.__text: 0xba240
+  __TEXT.__auth_stubs: 0x1760
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__const: 0xddbe
-  __TEXT.__cstring: 0x121cd
-  __TEXT.__gcc_except_tab: 0x11100
-  __TEXT.__oslogstring: 0x1efb
-  __TEXT.__unwind_info: 0x4860
+  __TEXT.__cstring: 0x1235f
+  __TEXT.__gcc_except_tab: 0x11134
+  __TEXT.__oslogstring: 0x2017
+  __TEXT.__unwind_info: 0x4878
   __TEXT.__objc_classname: 0x2b
   __TEXT.__objc_methname: 0x3bc
   __TEXT.__objc_methtype: 0x344
   __TEXT.__objc_stubs: 0x360
   __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0x6d10
+  __DATA_CONST.__const: 0x6db8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xbb0
-  __AUTH_CONST.__const: 0x135b0
+  __AUTH_CONST.__auth_got: 0xbc0
+  __AUTH_CONST.__const: 0x135e8
   __AUTH_CONST.__cfstring: 0x2b80
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 15D47687-23DB-3124-B9DA-2BE89B94C377
+  UUID: A39BA6E2-727D-3ABA-845E-95BBF12DCECD
   Functions: 5386
-  Symbols:   12440
-  CStrings:  4542
+  Symbols:   12444
+  CStrings:  4575
 
Symbols:
+ _.str.112
+ _.str.113
+ _.str.94
+ _.str.95
+ _TelephonyUtilIsOversteerEnabled
+ __ZNK3xpc6object9to_stringEv
+ __ZZ29cellularInterfaceNameForIndexiE24kOversteerInterfaceNames
+ __os_log_debug_impl
- _.str.109
- _.str.110
- _.str.114
- _.str.84
- _.str.85
- ___TUAssertTrigger
Functions:
~ __ZN10subscriber9isSimDeadENS_8SimStateE : 64 -> 88
~ __ZN10subscriber12isSimPresentENS_8SimStateE : 64 -> 88
~ __Z25PersonalityIdFromSlotIdExRKNSt3__110shared_ptrIK8RegistryEEN10subscriber7SimSlotE : 700 -> 1084
~ __ZN10subscriber15isSimUnreadableENS_8SimStateE : 64 -> 88
~ __ZN10subscriber10isSimReadyENS_8SimStateE : 64 -> 88
~ __ZN10subscriber11isSimAbsentENS_8SimStateE : 64 -> 88
~ __Z34getActiveFakePositiveInterfaceName18DataConnectionType : 28 -> 88
~ __Z17getGsm7TableIndexN3sms12TextEncodingE : 64 -> 88
~ __ZN13CSIPDPManager20getInterfaceNameByIdEiRNSt3__112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE : 88 -> 124
~ __ZN16HelperRestServer17handleRestMessageERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictE : 540 -> 688
~ __ZN16HelperRestServer26handleRestMessageWithReplyERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictENS0_8functionIFvNS7_6objectEEEE : 616 -> 772
~ __ZN16HelperRestServer23handleDroppedConnectionERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc6objectE : 360 -> 440
~ __ZNK20FeatureConfiguration40isFakingSuccessfulBasebandRequestEnabledEv : 8 -> 4
~ __ZN19SignalStrengthModel11handleInputENSt3__110shared_ptrIK6InputsEE : 248 -> 480
~ __ZNK13DisplayStatus9dumpStateEPKN3ctu11OsLogLoggerE : 4 -> 252
~ __ZN10subscriber21isSimInTransientStateENS_8SimStateE : 60 -> 84
~ __ZN10subscriber13isSimInsertedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber12isSimSettledENS_8SimStateE : 64 -> 88
~ __ZN10subscriber11isSimLockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber18isSimReadyOrLockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber23isSimPermanentlyBlockedENS_8SimStateE : 64 -> 88
~ __ZN10subscriber20isSimPresentAndValidENS_8SimStateE : 64 -> 88
~ __ZNK12BasicSimInfo22isEmptyEsimCapableCardEv : 92 -> 116
~ __ZN12OTASPService20sendOTASPSuccessToUIEv : 464 -> 532
~ __Z18isXLAT464InterfacePKc : 168 -> 184
~ __Z20getCLAT46IPv6AddressPKcRjPhRS0_ : 624 -> 644
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
+ "not active"

```
