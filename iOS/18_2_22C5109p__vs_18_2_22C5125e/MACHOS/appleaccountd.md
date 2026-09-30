## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1007.225.2.0.0
-  __TEXT.__text: 0x285d80
-  __TEXT.__auth_stubs: 0x2650
-  __TEXT.__objc_methlist: 0x644
-  __TEXT.__objc_methname: 0x40d1
+1007.226.0.0.0
+  __TEXT.__text: 0x28b274
+  __TEXT.__auth_stubs: 0x2690
+  __TEXT.__objc_methlist: 0x664
+  __TEXT.__objc_methname: 0x4126
   __TEXT.__objc_classname: 0x20a
   __TEXT.__objc_methtype: 0x1466
-  __TEXT.__cstring: 0x7f74
-  __TEXT.__swift5_typeref: 0x5c45
+  __TEXT.__cstring: 0x8214
+  __TEXT.__swift5_typeref: 0x5d89
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xbc50
-  __TEXT.__constg_swiftt: 0x9808
-  __TEXT.__swift5_reflstr: 0x4ee4
-  __TEXT.__swift5_fieldmd: 0x4e74
+  __TEXT.__const: 0xbe90
+  __TEXT.__constg_swiftt: 0x9a58
+  __TEXT.__swift5_reflstr: 0x4fb4
+  __TEXT.__swift5_fieldmd: 0x4f5c
   __TEXT.__swift5_builtin: 0x1a4
-  __TEXT.__swift5_assocty: 0x638
-  __TEXT.__swift5_proto: 0x934
-  __TEXT.__swift5_types: 0x4a4
-  __TEXT.__swift5_protos: 0x1c0
-  __TEXT.__oslogstring: 0x163d6
-  __TEXT.__swift5_capture: 0x547c
+  __TEXT.__swift5_assocty: 0x650
+  __TEXT.__swift5_proto: 0x950
+  __TEXT.__swift5_types: 0x4b4
+  __TEXT.__swift5_protos: 0x1cc
+  __TEXT.__oslogstring: 0x16596
+  __TEXT.__swift5_capture: 0x5474
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5180
-  __TEXT.__eh_frame: 0x5428
-  __DATA_CONST.__auth_got: 0x1328
-  __DATA_CONST.__got: 0xc20
-  __DATA_CONST.__auth_ptr: 0x17d8
-  __DATA_CONST.__const: 0x10270
-  __DATA_CONST.__objc_classlist: 0x4c0
+  __TEXT.__unwind_info: 0x53d8
+  __TEXT.__eh_frame: 0x5e40
+  __DATA_CONST.__auth_got: 0x1348
+  __DATA_CONST.__got: 0xc28
+  __DATA_CONST.__auth_ptr: 0x1f80
+  __DATA_CONST.__const: 0x104b0
+  __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x14d20
-  __DATA.__objc_selrefs: 0x11b0
+  __DATA.__objc_const: 0x15208
+  __DATA.__objc_selrefs: 0x11c8
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x2620
-  __DATA.__data: 0xf3e0
+  __DATA.__objc_data: 0x2728
+  __DATA.__data: 0xf730
   __DATA.__objc_stublist: 0x68
-  __DATA.__bss: 0xe080
-  __DATA.__common: 0x3a8
+  __DATA.__bss: 0xe280
+  __DATA.__common: 0x3b0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7574
-  Symbols:   1175
-  CStrings:  3229
+  Functions: 7671
+  Symbols:   1185
+  CStrings:  3258
 
Symbols:
+ _$s8AllCasess12CaseIterablePTl
+ _$ss12CaseIterableMp
+ _$ss12CaseIterableP8AllCasesAB_SlTn
+ _$ss12CaseIterableP8allCases03AllD0QzvgZTq
+ _OBJC_CLASS_$_AADataclassManager
+ __swift_FORCE_LOAD_$_swiftAppleArchive
+ _xpc_array_apply
+ _xpc_dictionary_get_array
+ _xpc_dictionary_get_dictionary
+ _xpc_string_get_string_ptr
CStrings:
+ "App install observer error: %!@(MISSING)"
+ "AppInstallObserver: Handling distributed notification."
+ "AppInstallObserver: Ignoring event %!s(MISSING)"
+ "AppInstallObserver: Missing bundleIDs for notification."
+ "B24@?0q8@\"<OS_xpc_object>\"16"
+ "Custodianship %!s(MISSING) verified. Generating session with code..."
+ "Dataclass App Install Observer - Failed to refresh %!@(MISSING)"
+ "Dataclass App Install Observer - Ignoring %!s(MISSING)"
+ "Dataclass App Install Observer - Missing reference to self."
+ "Dataclass App Install Observer - No apps provided."
+ "Dataclass App Install Observer - Refreshed %!@(MISSING)"
+ "Found custodian for id %!s(MISSING): %!s(MISSING)"
+ "Found health check record for %!s(MISSING): %!s(MISSING)"
+ "Found recovery info for id %!s(MISSING): %!s(MISSING)"
+ "Generate recovery code failed: %!@(MISSING)"
+ "UserInfo"
+ "_TtC13appleaccountd18AppInstallObserver"
+ "_TtC13appleaccountd20DaemonTaskDispatcher"
+ "_TtC13appleaccountd28DataclassAppInstallObserving"
+ "aa_appleAccounts"
+ "appleaccountd.AppInstallObserver"
+ "bundleIDs"
+ "bundleIDsForDataclasses"
+ "com.apple.LaunchServices.applicationRegistered"
+ "com.apple.LaunchServices.applicationUnregistered"
+ "dataclassBundleMap"
+ "discoverPropertiesForAccount:options:completion:"
+ "fetchCustodianshipInfo(with:)"
+ "fetchRecoveryInfo(with:)"
+ "isForcedUpdate"
+ "isPlaceholder"
+ "observers"
+ "sendCustodianMessage(for:nextStep:altDSID:telemetryFlowID:)"
+ "taskDispatcher"
+ "v24@?0@\"ACAccount\"8@\"NSError\"16"
- "Custodianship %!s(MISSING) verified, Generating session with code"
- "CustodianshipInfoFetchError"
- "Error fetching recovery records: %!@(MISSING)"
- "Failed to fetch custodianship info record: %!@(MISSING)"
- "Failed to verify custodianship with error: %!@(MISSING)"
- "distnoted Event name unavailable"
- "distnoted Event name: %!s(MISSING)"

```
