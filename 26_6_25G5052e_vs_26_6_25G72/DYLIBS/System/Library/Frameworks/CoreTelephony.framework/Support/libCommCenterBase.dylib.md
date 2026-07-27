## libCommCenterBase.dylib

> `/System/Library/Frameworks/CoreTelephony.framework/Support/libCommCenterBase.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-13192.0.0.0.0
-  __TEXT.__text: 0xc26a4
-  __TEXT.__auth_stubs: 0x16d0
+13193.0.0.0.0
+  __TEXT.__text: 0xc202c
+  __TEXT.__auth_stubs: 0x16c0
   __TEXT.__init_offsets: 0x30
   __TEXT.__objc_methlist: 0xf8
   __TEXT.__const: 0xd040
-  __TEXT.__cstring: 0x12bfb
-  __TEXT.__gcc_except_tab: 0x11fc4
-  __TEXT.__oslogstring: 0x2233
-  __TEXT.__unwind_info: 0x4a10
+  __TEXT.__cstring: 0x12a26
+  __TEXT.__gcc_except_tab: 0x11f94
+  __TEXT.__oslogstring: 0x20ff
+  __TEXT.__unwind_info: 0x4a00
   __TEXT.__objc_classname: 0x2c
   __TEXT.__objc_methname: 0x3bc
   __TEXT.__objc_methtype: 0x2fa

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xb78
-  __AUTH_CONST.__const: 0x13a28
+  __AUTH_CONST.__auth_got: 0xb70
+  __AUTH_CONST.__const: 0x139f0
   __AUTH_CONST.__cfstring: 0x2a80
   __AUTH_CONST.__objc_const: 0x200
   __DATA.__objc_ivar: 0x8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 5530
-  Symbols:   9147
-  CStrings:  4357
+  Symbols:   9146
+  CStrings:  4345
 
Symbols:
+ ___TUAssertTrigger
- __ZNK3xpc6object9to_stringEv
- __os_log_debug_impl
Functions:
~ __Z17getGsm7TableIndexN3sms12TextEncodingE : 88 -> 64
~ __ZN16HelperRestServer17handleRestMessageERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictE : 680 -> 532
~ __ZN16HelperRestServer26handleRestMessageWithReplyERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc4dictENS0_8functionIFvNS7_6objectEEEE : 780 -> 624
~ __ZN16HelperRestServer23handleDroppedConnectionERKNSt3__110shared_ptrIN3ctu22RestResourceConnectionEEEN3xpc6objectE : 432 -> 352
~ __ZN19SignalStrengthModel11handleInputENSt3__110shared_ptrIK6InputsEE : 472 -> 248
~ __ZNK13DisplayStatus9dumpStateEPKN3ctu11OsLogLoggerE : 200 -> 4
~ __ZN10subscriber12isSimPresentENS_8SimStateE : 88 -> 64
~ __ZN10subscriber21isSimInTransientStateENS_8SimStateE : 88 -> 64
~ __ZN10subscriber11isSimAbsentENS_8SimStateE : 88 -> 64
~ __ZN10subscriber13isSimInsertedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber15isSimUnreadableENS_8SimStateE : 88 -> 64
~ __ZN10subscriber10isSimReadyENS_8SimStateE : 88 -> 64
~ __ZN10subscriber12isSimSettledENS_8SimStateE : 88 -> 64
~ __ZN10subscriber11isSimLockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber18isSimReadyOrLockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber9isSimDeadENS_8SimStateE : 88 -> 64
~ __ZN10subscriber23isSimPermanentlyBlockedENS_8SimStateE : 88 -> 64
~ __ZN10subscriber20isSimPresentAndValidENS_8SimStateE : 88 -> 64
~ __ZNK12BasicSimInfo22isEmptyEsimCapableCardEv : 116 -> 92
~ __ZN12OTASPService20sendOTASPSuccessToUIEv : 516 -> 448
~ __Z25PersonalityIdFromSlotIdExRKNSt3__110shared_ptrIK8RegistryEEN10subscriber7SimSlotE : 1072 -> 688
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxN472/Sources/CoreTelephony/CSI/Source/Common/SmsPduEncoder.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HxN472/Sources/CoreTelephony/CommCenter/CommCenterCommandDrivers/Sim/SubscriberDefinitions.cpp"
- "Assertion failure: ( %s ), in file %s, line: %d"
- "not active"
```
