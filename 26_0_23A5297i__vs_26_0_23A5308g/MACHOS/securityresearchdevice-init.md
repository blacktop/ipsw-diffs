## securityresearchdevice-init

> `/usr/libexec/securityresearchdevice-init`

```diff

-221.0.22.0.0
-  __TEXT.__text: 0x17ce0
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__const: 0x828
+221.0.27.0.0
+  __TEXT.__text: 0x19a14
+  __TEXT.__auth_stubs: 0xe70
+  __TEXT.__const: 0x818
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x55c
-  __TEXT.__swift_as_entry: 0x68
-  __TEXT.__swift_as_ret: 0x98
-  __TEXT.__oslogstring: 0x73c
-  __TEXT.__swift5_typeref: 0x14e
-  __TEXT.__constg_swiftt: 0x220
-  __TEXT.__swift5_reflstr: 0x4f4
-  __TEXT.__swift5_fieldmd: 0x328
+  __TEXT.__cstring: 0x70c
+  __TEXT.__swift_as_entry: 0x6c
+  __TEXT.__swift_as_ret: 0xa0
+  __TEXT.__oslogstring: 0x82c
+  __TEXT.__swift5_typeref: 0x158
+  __TEXT.__constg_swiftt: 0x21c
+  __TEXT.__swift5_reflstr: 0x534
+  __TEXT.__swift5_fieldmd: 0x340
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__objc_methname: 0x29a
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift5_types2: 0x4
+  __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_capture: 0x20
-  __TEXT.__unwind_info: 0x630
-  __TEXT.__eh_frame: 0x1620
-  __DATA_CONST.__auth_got: 0x6c0
-  __DATA_CONST.__got: 0x1c0
+  __TEXT.__unwind_info: 0x650
+  __TEXT.__eh_frame: 0x16a8
+  __DATA_CONST.__auth_got: 0x738
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0xd0
   __DATA_CONST.__const: 0x560
   __DATA_CONST.__cfstring: 0x20

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0xb8
   __DATA.__objc_selrefs: 0xd0
-  __DATA.__data: 0x4c8
+  __DATA.__data: 0x4f0
   __DATA.__bss: 0x5a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 9ABEA9F7-0FAC-35EB-AD39-90EF298ABAC5
-  Functions: 335
-  Symbols:   317
-  CStrings:  112
+  UUID: B73ACB8C-0A9F-3A9A-B8EA-EAE1D83C3493
+  Functions: 343
+  Symbols:   337
+  CStrings:  125
 
Symbols:
+ _$s10Foundation12CharacterSetV22whitespacesAndNewlinesACvgZ
+ _$s10Foundation12CharacterSetVMa
+ _$sSS14_fromSubstringySSSshFZ
+ _$sSS18_fromUTF8RepairingySS6result_Sb11repairsMadetSRys5UInt8VGFZ
+ _$sSS5index5afterSS5IndexVAD_tF
+ _$sSS8IteratorV4nextSJSgyF
+ _$sSa28_allocateBufferUninitialized15minimumCapacitys06_ArrayB0VyxGSi_tFZ
+ _$sSbN
+ _$sSqMa
+ _$sSs5index5afterSS5IndexVAD_tF
+ _$sSsN
+ _$sSsySJSS5IndexVcig
+ _$sSsySsSScfC
+ _$sSsySsSnySS5IndexVGcig
+ _$sSy10FoundationE18trimmingCharacters2inSSAA12CharacterSetV_tF
+ _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_SSAHSus6UInt32VtF
+ _$ss22_stringCompareInternal____9expectingSbs11_StringGutsV_SnySiGAdEs01_E16ComparisonResultOtF
+ _$ss4Int8VN
+ _bzero
+ _swift_cvw_initStructMetadataWithLayoutString
+ _sysctlbyname
- _swift_initStructMetadata
CStrings:
+ ", exiting gracefully"
+ "Cryptex installation not needed."
+ "Detected disabled research configuration for %s in bootargs, exiting"
+ "Fatal error"
+ "Malformed txm_research(_extended)_config != 2: count %ld, boot-arg %s"
+ "No valid configuration detected for securityresearchdevice-init"
+ "Personalize failed on iteration: "
+ "Personalize succeeded on iteration: %ld"
+ "Removed %s key from NVRAM"
+ "SecurityResearchDeviceInit was already run, exiting"
+ "SecurityResearchDeviceInitCore returned error: "
+ "SecurityResearchDeviceInitCore/NVRAM.swift"
+ "SecurityResearchDeviceInitCore/Retry.swift"
+ "Task.sleep failed with error: "
+ "kern.bootargs"
+ "personalize(cryptex:for:nonce:)"
+ "retry(backoff:numRetries:body:shouldRetry:onRetry:)"
+ "securityresearchdevice initialization"
+ "txm_research_config="
+ "txm_research_extended_config="
- "Cryptex should not be installed"
- "NVRAM forced provisioning removed"
- "No cryptex to download"
- "Not in target"
- "SecurityResearchDeviceInit was already run, exit"
- "SecurityResearchDeviceInitCore: "
- "aea-decrypt"

```
