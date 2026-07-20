## WebContentRestrictions

> `/System/Library/PrivateFrameworks/WebContentRestrictions.framework/Versions/A/WebContentRestrictions`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__oslogstring`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-67.0.0.0.0
-  __TEXT.__text: 0x10d70
-  __TEXT.__objc_methlist: 0xc00
+70.0.0.0.0
+  __TEXT.__text: 0x10efc
+  __TEXT.__objc_methlist: 0xc20
   __TEXT.__const: 0x670
   __TEXT.__cstring: 0x15a1
   __TEXT.__gcc_except_tab: 0x1cc

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x34
-  __TEXT.__unwind_info: 0x458
+  __TEXT.__unwind_info: 0x460
   __TEXT.__eh_frame: 0x2a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x108
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x888
+  __DATA_CONST.__objc_selrefs: 0x890
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x78
   __DATA_CONST.__got: 0x1b0
   __AUTH_CONST.__const: 0x609
   __AUTH_CONST.__cfstring: 0x1900
-  __AUTH_CONST.__objc_const: 0x1538
+  __AUTH_CONST.__objc_const: 0x1540
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x4e8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 428
-  Symbols:   1273
+  Functions: 432
+  Symbols:   1275
   CStrings:  264
 
Symbols:
+ -[WCRRemoteAskToViewController hasPasscodeWithCompletion:]
+ GCC_except_table49
+ GCC_except_table55
+ _WCROverridePolicyStringForValue
+ _WCROverridePolicyValueForString
- GCC_except_table48
- GCC_except_table54
- __287+[WCRBrowserEngineClient _evaluateURL:mainDocumentURL:inMode:usingBloomFilter:userSettings:language:allowList:appleAllowList:denyList:allowedWebsitesOnlyList:macOSExemptURLList:authenticationSites:allowTransitiveTrust:overridePolicy:ageVerificationText:withCompletion:onCompletionQueue:]_block_invoke_2
CStrings:
+ "%{sensitive}@ -> Not Allowed"
+ "Bloom filter: %{sensitive}@ -> Allowed"
+ "Transitive trust bloom filter: %{sensitive}@ -> Not Allowed"
+ "Transitive trust via authentication sites: %{sensitive}@ -> Allowed"
+ "overridePolicy from DC: %s"
- "overridePolicy from DC: askForPermission"
- "overridePolicy from DC: localApprovalOnly"
- "overridePolicy from DC: notAllowed"
- "overridePolicy from DC: unverifiedAdultLegacyScreenTime"
- "overridePolicy from DC: unverifiedAdultScreenTime"
```
