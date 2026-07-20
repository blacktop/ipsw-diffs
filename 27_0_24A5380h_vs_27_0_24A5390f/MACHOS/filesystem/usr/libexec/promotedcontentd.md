## promotedcontentd

> `/usr/libexec/promotedcontentd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
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
-  __TEXT.__text: 0x3d8ec4
-  __TEXT.__auth_stubs: 0x5bc0
+557.1.26.0.0
+  __TEXT.__text: 0x3dd98c
+  __TEXT.__auth_stubs: 0x5ce0
   __TEXT.__objc_stubs: 0x1a1e0
   __TEXT.__objc_methlist: 0x15228
-  __TEXT.__const: 0x2b1da
+  __TEXT.__const: 0x2b3aa
   __TEXT.__gcc_except_tab: 0x1348
-  __TEXT.__cstring: 0x15ce5
-  __TEXT.__objc_methname: 0x26fed
-  __TEXT.__oslogstring: 0x10edc
+  __TEXT.__cstring: 0x15dd5
+  __TEXT.__objc_methname: 0x2708d
+  __TEXT.__oslogstring: 0x10fdc
   __TEXT.__objc_classname: 0x4c17
   __TEXT.__objc_methtype: 0x512d
-  __TEXT.__constg_swiftt: 0x6400
-  __TEXT.__swift5_typeref: 0x42f4
-  __TEXT.__swift5_reflstr: 0x3636
-  __TEXT.__swift5_fieldmd: 0x4970
-  __TEXT.__swift5_builtin: 0x154
+  __TEXT.__constg_swiftt: 0x6488
+  __TEXT.__swift5_typeref: 0x43a0
+  __TEXT.__swift5_reflstr: 0x3726
+  __TEXT.__swift5_fieldmd: 0x4a24
+  __TEXT.__swift5_builtin: 0x168
   __TEXT.__swift5_assocty: 0x3d8
-  __TEXT.__swift5_proto: 0x848
-  __TEXT.__swift5_types: 0x5c0
-  __TEXT.__swift5_capture: 0x1288
-  __TEXT.__swift5_protos: 0x120
+  __TEXT.__swift5_proto: 0x850
+  __TEXT.__swift5_types: 0x5cc
+  __TEXT.__swift5_capture: 0x12bc
+  __TEXT.__swift5_protos: 0x124
   __TEXT.__swift_as_entry: 0xf0
   __TEXT.__swift_as_ret: 0x11c
   __TEXT.__swift_as_cont: 0x26c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x7148
+  __TEXT.__unwind_info: 0x7178
   __TEXT.__eh_frame: 0x4c5c
-  __DATA_CONST.__const: 0x1c6c8
-  __DATA_CONST.__cfstring: 0xf800
+  __DATA_CONST.__const: 0x1c908
+  __DATA_CONST.__cfstring: 0xf7e0
   __DATA_CONST.__objc_classlist: 0xfe8
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x310

   __DATA_CONST.__objc_dictobj: 0xa50
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x2df0
-  __DATA_CONST.__got: 0x1850
-  __DATA_CONST.__auth_ptr: 0x15c0
-  __DATA.__objc_const: 0x2b388
+  __DATA_CONST.__auth_got: 0x2e80
+  __DATA_CONST.__got: 0x18b8
+  __DATA_CONST.__auth_ptr: 0x1608
+  __DATA.__objc_const: 0x2b448
   __DATA.__objc_selrefs: 0x94a0
   __DATA.__objc_ivar: 0x1458
-  __DATA.__objc_data: 0x9840
-  __DATA.__data: 0xe618
+  __DATA.__objc_data: 0x9848
+  __DATA.__data: 0xe6c8
   __DATA.__common: 0xd70
-  __DATA.__bss: 0xde40
+  __DATA.__bss: 0xdec0
   - /AppleInternal/Library/Frameworks/TestHookService.framework/TestHookService
   - /AppleInternal/Library/Frameworks/TestHookShared.framework/TestHookShared
   - /System/Library/Frameworks/AdServices.framework/AdServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11788
-  Symbols:   2298
-  CStrings:  11649
+  Functions: 11808
+  Symbols:   2297
+  CStrings:  11663
 
Symbols:
- _objc_retain_x10
CStrings:
+ "Attaching pageLayoutFinal %{public}@ to %{public}@ for content %{public}@"
+ "Attribution request received with nil timestamp (intervalId: %{public}llu); proceeding without it."
+ "DELETE FROM Tokens"
+ "Off"
+ "On"
+ "SELECT SUM(val) FROM (SELECT (slotVisibleAdCount + slotVisibleNoAdCount + impressionCount + clickCount + downloadCount + redownloadCount + preOrderPlacedCount + viewDownloadCount + viewRedownloadCount + viewPreorderPlacedCount) AS val FROM APDBExperimentationReport WHERE triggerRowId = ? AND source = ? AND adType = ? AND day IN (SELECT e.value FROM json_each('%@') e)%@)"
+ "Sending CoreAnalytics event '%s' with payload: %s"
+ "Stored attribution token does not match its key. Purging all stored tokens."
+ "account"
+ "actualBirthYearAvailable"
+ "applicationDiagnostics"
+ "com.apple.adplatforms.agenoising.application"
+ "initWithError:outcome:"
+ "initWithToken:tokenKey:outcome:"
+ "noisedBirthYearAvailable"
+ "retryDiagnostics"
+ "storefrontIDSource"
+ "userAgeNoisingStoreDiagnosticsDepot"
- "SELECT SUM(val) FROM (SELECT (slotVisibleAdCount + impressionCount + clickCount + downloadCount + redownloadCount + preOrderPlacedCount + viewDownloadCount + viewRedownloadCount + viewPreorderPlacedCount) AS val FROM APDBExperimentationReport WHERE triggerRowId = ? AND source = ? AND adType = ? AND day IN (SELECT e.value FROM json_each('%@') e)%@)"
- "attribution.timings"
- "initWithError:"
- "initWithToken:tokenKey:source:"
```
