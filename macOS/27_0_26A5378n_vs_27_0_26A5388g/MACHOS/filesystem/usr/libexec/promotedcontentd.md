## promotedcontentd

> `/usr/libexec/promotedcontentd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_selrefs`

```diff

-557.1.24.0.0
-  __TEXT.__text: 0x34bcb4
-  __TEXT.__auth_stubs: 0x5730
+557.1.26.0.0
+  __TEXT.__text: 0x34eb5c
+  __TEXT.__auth_stubs: 0x57c0
   __TEXT.__objc_stubs: 0x19980
   __TEXT.__objc_methlist: 0x15210
-  __TEXT.__const: 0x743da
+  __TEXT.__const: 0x7455a
   __TEXT.__gcc_except_tab: 0x12a0
-  __TEXT.__cstring: 0x15565
-  __TEXT.__objc_methname: 0x26cfd
-  __TEXT.__oslogstring: 0x1032c
+  __TEXT.__cstring: 0x155e5
+  __TEXT.__objc_methname: 0x26dad
+  __TEXT.__oslogstring: 0x103ec
   __TEXT.__objc_classname: 0x4bb7
   __TEXT.__objc_methtype: 0x513d
-  __TEXT.__constg_swiftt: 0x6164
-  __TEXT.__swift5_typeref: 0x4162
-  __TEXT.__swift5_reflstr: 0x3586
-  __TEXT.__swift5_fieldmd: 0x4734
-  __TEXT.__swift5_builtin: 0x140
+  __TEXT.__constg_swiftt: 0x61ec
+  __TEXT.__swift5_typeref: 0x41e8
+  __TEXT.__swift5_reflstr: 0x3656
+  __TEXT.__swift5_fieldmd: 0x47c4
+  __TEXT.__swift5_builtin: 0x154
   __TEXT.__swift5_assocty: 0x3a8
-  __TEXT.__swift5_proto: 0x7d0
-  __TEXT.__swift5_types: 0x58c
-  __TEXT.__swift5_capture: 0x11d8
-  __TEXT.__swift5_protos: 0x120
+  __TEXT.__swift5_proto: 0x7d8
+  __TEXT.__swift5_types: 0x598
+  __TEXT.__swift5_capture: 0x11ec
+  __TEXT.__swift5_protos: 0x124
   __TEXT.__swift_as_entry: 0xe8
   __TEXT.__swift_as_ret: 0x10c
   __TEXT.__swift_as_cont: 0x258
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x6e20
+  __TEXT.__unwind_info: 0x6e30
   __TEXT.__eh_frame: 0x495c
-  __DATA_CONST.__const: 0x16750
-  __DATA_CONST.__cfstring: 0xf340
+  __DATA_CONST.__const: 0x168d0
+  __DATA_CONST.__cfstring: 0xf320
   __DATA_CONST.__objc_classlist: 0xfe8
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x310

   __DATA_CONST.__objc_dictobj: 0xa50
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x2ba8
-  __DATA_CONST.__got: 0x17d0
-  __DATA_CONST.__auth_ptr: 0x14f8
-  __DATA.__objc_const: 0x2b2f8
+  __DATA_CONST.__auth_got: 0x2bf0
+  __DATA_CONST.__got: 0x1810
+  __DATA_CONST.__auth_ptr: 0x1528
+  __DATA.__objc_const: 0x2b3b8
   __DATA.__objc_selrefs: 0x9398
   __DATA.__objc_ivar: 0x1458
-  __DATA.__objc_data: 0x97b0
-  __DATA.__data: 0xda18
+  __DATA.__objc_data: 0x97b8
+  __DATA.__data: 0xda48
   __DATA.__common: 0xc30
-  __DATA.__bss: 0xcf30
+  __DATA.__bss: 0xcfb0
   - /AppleInternal/Library/Frameworks/TestHookService.framework/Versions/A/TestHookService
   - /AppleInternal/Library/Frameworks/TestHookShared.framework/Versions/A/TestHookShared
   - /System/Library/Frameworks/AdServices.framework/Versions/A/AdServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11429
+  Functions: 11438
   Symbols:   2192
-  CStrings:  11500
+  CStrings:  11508
 
CStrings:
+ "Attaching pageLayoutFinal %{public}@ to %{public}@ for content %{public}@"
+ "Attribution request received with nil timestamp (intervalId: %{public}llu); proceeding without it."
+ "DELETE FROM Tokens"
+ "SELECT SUM(val) FROM (SELECT (slotVisibleAdCount + slotVisibleNoAdCount + impressionCount + clickCount + downloadCount + redownloadCount + preOrderPlacedCount + viewDownloadCount + viewRedownloadCount + viewPreorderPlacedCount) AS val FROM APDBExperimentationReport WHERE triggerRowId = ? AND source = ? AND adType = ? AND day IN (SELECT e.value FROM json_each('%@') e)%@)"
+ "Stored attribution token does not match its key. Purging all stored tokens."
+ "account"
+ "applicationDiagnostics"
+ "initWithError:outcome:"
+ "initWithToken:tokenKey:outcome:"
+ "retryDiagnostics"
+ "storefrontIDSource"
+ "userAgeNoisingStoreDiagnosticsDepot"
- "SELECT SUM(val) FROM (SELECT (slotVisibleAdCount + impressionCount + clickCount + downloadCount + redownloadCount + preOrderPlacedCount + viewDownloadCount + viewRedownloadCount + viewPreorderPlacedCount) AS val FROM APDBExperimentationReport WHERE triggerRowId = ? AND source = ? AND adType = ? AND day IN (SELECT e.value FROM json_each('%@') e)%@)"
- "attribution.timings"
- "initWithError:"
- "initWithToken:tokenKey:source:"
```
