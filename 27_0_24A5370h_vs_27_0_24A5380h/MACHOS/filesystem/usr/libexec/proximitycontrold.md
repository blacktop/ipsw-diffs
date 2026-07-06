## proximitycontrold

> `/usr/libexec/proximitycontrold`

```diff

-  __TEXT.__text: 0x265aec
-  __TEXT.__auth_stubs: 0x3640
-  __TEXT.__objc_stubs: 0x4220
+  __TEXT.__text: 0x2642e8
+  __TEXT.__auth_stubs: 0x3570
+  __TEXT.__objc_stubs: 0x4200
   __TEXT.__objc_methlist: 0x29c8
-  __TEXT.__const: 0x21648
-  __TEXT.__objc_methname: 0xdf29
+  __TEXT.__const: 0x21618
+  __TEXT.__objc_methname: 0xdf39
   __TEXT.__objc_classname: 0x2407
-  __TEXT.__cstring: 0x7d99
+  __TEXT.__cstring: 0x7d29
   __TEXT.__objc_methtype: 0x36db
-  __TEXT.__swift5_typeref: 0xf156
-  __TEXT.__constg_swiftt: 0xd7e4
+  __TEXT.__swift5_typeref: 0xf2ea
+  __TEXT.__constg_swiftt: 0xd7ec
   __TEXT.__swift5_reflstr: 0x99b3
   __TEXT.__swift5_fieldmd: 0x9360
   __TEXT.__swift5_builtin: 0x5a0
   __TEXT.__swift5_assocty: 0xed0
-  __TEXT.__swift5_capture: 0x347c
-  __TEXT.__oslogstring: 0x7eae
+  __TEXT.__swift5_capture: 0x349c
+  __TEXT.__oslogstring: 0x7d0e
   __TEXT.__swift5_proto: 0x17d8
   __TEXT.__swift5_types: 0x8c0
   __TEXT.__swift_as_entry: 0xf4

   __TEXT.__swift_as_cont: 0x1cc
   __TEXT.__swift5_protos: 0x144
   __TEXT.__swift5_mpenum: 0x11c
-  __TEXT.__unwind_info: 0x6c30
-  __TEXT.__eh_frame: 0x6704
-  __DATA_CONST.__const: 0x15480
+  __TEXT.__unwind_info: 0x6be8
+  __TEXT.__eh_frame: 0x6694
+  __DATA_CONST.__const: 0x154a8
   __DATA_CONST.__cfstring: 0x460
   __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__auth_got: 0x1b28
-  __DATA_CONST.__got: 0xea8
-  __DATA_CONST.__auth_ptr: 0x1a60
+  __DATA_CONST.__auth_got: 0x1ac0
+  __DATA_CONST.__got: 0xea0
+  __DATA_CONST.__auth_ptr: 0x1a50
   __DATA.__objc_const: 0x18930
-  __DATA.__objc_selrefs: 0x1da8
+  __DATA.__objc_selrefs: 0x1db0
   __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0x3910
   __DATA.__data: 0x17c68
   __DATA.__bss: 0x2bc60
-  __DATA.__common: 0x8a8
+  __DATA.__common: 0x890
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 10340
-  Symbols:   1646
-  CStrings:  4239
+  Functions: 10330
+  Symbols:   1631
+  CStrings:  4229
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
Symbols:
+ _RPOptionStatusFlags
- _$s15Synchronization5MutexVMa
- _$sSh5IndexV8_asCocoas02__C3SetVAAVvM
- _$sSh5IndexVMn
- _$sSy10FoundationE15appendingFormatySSqd___s7CVarArg_pdtSyRd__lF
- _$ss10__CocoaSetV10startIndexAB0D0Vvg
- _$ss10__CocoaSetV5IndexV16handleBitPatternSuvg
- _$ss10__CocoaSetV5IndexV3ages5Int32Vvg
- _$ss10__CocoaSetV5IndexV7elementyXlvg
- _$ss10__CocoaSetV7element2atyXlAB5IndexV_tF
- _$ss10__CocoaSetV9formIndex5after8isUniqueyAB0D0Vz_SbtF
- _NSSelectorFromString
- __xpc_event_key_name
- _objc_retainAutorelease
- _swift_runtimeSupportsNoncopyableTypes
- _swift_willThrowTypedImpl
- _xpc_dictionary_get_string
CStrings:
- "### RPCompanionLinkDevice: No selector for 'publicBluetoothAddress'"
- "%s: key=%s"
- "(Non-communal, r1CapableNearby="
- "CBDevices changed, count=%ld"
- "No edge for state input: %s, state=%s"
- "Received xpc stream event: %s"
- "Sending state input %s"
- "Should start ranging = %{bool}d %s"
- "Should start ranging = %{bool}d (Communal, candidates=%ld), allowGuests=%{bool}d"
- "State after receiving %s: %s"

```
