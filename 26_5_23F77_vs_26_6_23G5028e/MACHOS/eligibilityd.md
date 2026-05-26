## eligibilityd

> `/usr/libexec/eligibilityd`

```diff

-319.122.4.0.0
-  __TEXT.__text: 0x3e8b0
-  __TEXT.__auth_stubs: 0x1840
-  __TEXT.__objc_stubs: 0x2680
-  __TEXT.__objc_methlist: 0x1d94
-  __TEXT.__const: 0x2030
-  __TEXT.__cstring: 0x6365
-  __TEXT.__swift5_typeref: 0x822
-  __TEXT.__oslogstring: 0x24da
-  __TEXT.__constg_swiftt: 0x76c
+319.160.10.0.0
+  __TEXT.__text: 0x426c4
+  __TEXT.__auth_stubs: 0x1880
+  __TEXT.__objc_stubs: 0x2840
+  __TEXT.__objc_methlist: 0x1e04
+  __TEXT.__const: 0x2230
+  __TEXT.__cstring: 0x64f5
+  __TEXT.__swift5_typeref: 0x880
+  __TEXT.__oslogstring: 0x259b
+  __TEXT.__constg_swiftt: 0x790
   __TEXT.__swift5_reflstr: 0x673
   __TEXT.__swift5_fieldmd: 0x678
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_assocty: 0xf0
-  __TEXT.__swift5_proto: 0x1c4
-  __TEXT.__swift5_types: 0xd4
-  __TEXT.__objc_methname: 0x2eef
+  __TEXT.__swift5_assocty: 0x108
+  __TEXT.__swift5_proto: 0x1f4
+  __TEXT.__swift5_types: 0xd8
+  __TEXT.__objc_methname: 0x30df
   __TEXT.__objc_classname: 0x55f
   __TEXT.__objc_methtype: 0x798
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_capture: 0x14
-  __TEXT.__gcc_except_tab: 0x378
-  __TEXT.__unwind_info: 0xcd8
-  __TEXT.__eh_frame: 0xb20
-  __DATA_CONST.__auth_got: 0xc30
-  __DATA_CONST.__got: 0x370
-  __DATA_CONST.__auth_ptr: 0x310
-  __DATA_CONST.__const: 0x2340
-  __DATA_CONST.__cfstring: 0x4b60
+  __TEXT.__gcc_except_tab: 0x388
+  __TEXT.__unwind_info: 0xd80
+  __TEXT.__eh_frame: 0xb50
+  __DATA_CONST.__auth_got: 0xc50
+  __DATA_CONST.__got: 0x398
+  __DATA_CONST.__auth_ptr: 0x320
+  __DATA_CONST.__const: 0x2400
+  __DATA_CONST.__cfstring: 0x4c00
   __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0xa968
   __DATA_CONST.__objc_arrayobj: 0x2ac0
   __DATA_CONST.__objc_dictobj: 0x99c0
-  __DATA.__objc_const: 0x3548
-  __DATA.__objc_selrefs: 0xb08
-  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_const: 0x35a8
+  __DATA.__objc_selrefs: 0xb88
+  __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0xd40
-  __DATA.__data: 0x1188
-  __DATA.__bss: 0x2328
+  __DATA.__data: 0x1228
+  __DATA.__bss: 0x2838
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 8C99D8EF-00A8-3AC7-B7BA-25E0D9F2231C
-  Functions: 1249
-  Symbols:   595
-  CStrings:  2469
+  UUID: 449674EE-7E37-370B-9FE9-A597C800498F
+  Functions: 1323
+  Symbols:   606
+  CStrings:  2509
 
Symbols:
+ _$s10ObjectiveC8SelectorV2eeoiySbAC_ACtFZ
+ _$sSS5IndexVMn
+ _$sSSSysMc
+ _$sSo8_NSRangeV10FoundationE_2inABx_q_tcSXRzSyR_SS5IndexV5BoundRtzr0_lufC
+ _$sSy10FoundationE20replacingOccurrences2of4with7options5rangeSSqd___qd_0_So22NSStringCompareOptionsVSnySS5IndexVGSgtSyRd__SyRd_0_r0_lF
+ _$ss16PartialRangeFromVMn
+ _$ss16PartialRangeFromVyxGSXsMc
+ _NSStringFromSelector
+ _OBJC_CLASS_$_NSRegularExpression
+ _OBJC_CLASS_$_NSSortDescriptor
+ ___NSDictionary0__struct
CStrings:
+ "%s: Domain count does NOT match - MA: %lu vs. %lu"
+ "%s: Mismatched domains after sorting: %@ vs %@"
+ "%s: No diff generated - fallback was used."
+ "%s: Process %@ not entitled to diff the Mobile Asset"
+ "-[MobileAssetManager _onMobileAssetQueue_diffDomainsToFallbackWithError:]"
+ "-[MobileAssetManager fallbackDomains]"
+ "00:01:11"
+ "319.160.10"
+ "<[A-Za-z_][\\w]* 0x[0-9a-f]+>"
+ "Domain count did not match between asset and fallback"
+ "Fallback"
+ "May 15 2026"
+ "Mismatched domain - this should NOT happen"
+ "MobileAsset"
+ "OS_ELIGIBILITY_INPUT_"
+ "OS_ELIGIBILITY_INPUT_STATUS_"
+ "T@\"NSArray\",C,N,V_fallbackDomains"
+ "TB,N,V_usedFallback"
+ "_fallbackDomains"
+ "_onMobileAssetQueue_diffDomainsToFallbackWithError:"
+ "_usedFallback"
+ "arrayWithObjects:count:"
+ "com.apple.private.eligibilityd.diffMobileAsset"
+ "diffAssetToFallbackWithError:"
+ "diffDictionary"
+ "diffDomainsToFallbackWithError:"
+ "fallbackDomains"
+ "initWithPattern:options:error:"
+ "isDomainSameAs:"
+ "mobileAssetDiffDictionary"
+ "normalizeDescription"
+ "objectAtIndexedSubscript:"
+ "setFallbackDomains:"
+ "setUsedFallback:"
+ "sortDescriptorWithKey:ascending:"
+ "sortedArrayUsingDescriptors:"
+ "stringByReplacingMatchesInString:options:range:withTemplate:"
+ "usedFallback"
- "!"
- "19:49:27"
- "319.122.4"
- "Apr 30 2026"

```
