## IMTransferAgent

> `/System/Library/PrivateFrameworks/IMTransferAgent.framework/IMTransferAgent`

```diff

-1491.200.101.2.5
-  __TEXT.__text: 0x16ad0
-  __TEXT.__objc_methlist: 0xa84
+1491.300.43.0.0
+  __TEXT.__text: 0x17614
+  __TEXT.__objc_methlist: 0xa9c
   __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x1748
+  __TEXT.__gcc_except_tab: 0x17cc
   __TEXT.__cstring: 0xbe5
-  __TEXT.__oslogstring: 0x2a99
-  __TEXT.__unwind_info: 0x5f0
+  __TEXT.__oslogstring: 0x2e2f
+  __TEXT.__unwind_info: 0x620
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x830
+  __DATA_CONST.__const: 0x8d0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd80
+  __DATA_CONST.__objc_selrefs: 0xd98
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__got: 0x398
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0xdc0
   __AUTH_CONST.__objc_const: 0xdb0

   - /System/Library/PrivateFrameworks/Marco.framework/Marco
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 250
-  Symbols:   264
-  CStrings:  354
+  Functions: 256
+  Symbols:   269
+  CStrings:  362
 
Symbols:
+ _IMIsCommSafetySensitiveFromSCSensitivityAnalysis
+ _IMMMCSForceFallbackPathForTesting
+ _IMMMCSRegionStoreFeatureEnabled
+ _IMMMCSResponseRequiresFailure
+ _IMShouldDisableMMCSFallbackForRegion
+ _OBJC_CLASS_$_IMRegionConnectionPolicy
- _IMCommSafetyStateFromSCSensitivityAnalysis
CStrings:
+ "Avatar image was checked for sensitive content. Is sensitive: %{BOOL}d, error: %@"
+ "Failing download for transfer %@ rather than falling back to the unoptimized MMCS path in a region that disallows it."
+ "Failing upload for transfer %@ rather than falling back to the unoptimized MMCS path in a region that disallows it."
+ "Ignoring the AuthGet opt-out for download with GUID %@: region disallows the MMCS fallback."
+ "Ignoring the AuthPut opt-out for upload with GUID %@: region disallows the MMCS fallback."
+ "Madrid did not preauthorize ('cV': %tu); failing download rather than falling back to the unoptimized MMCS path in a region that disallows it (transfer: %@)"
+ "Madrid did not preauthorize ('cV': %tu); failing upload rather than falling back to the unoptimized MMCS path in a region that disallows it (transfer: %@)"
+ "Region disallows the MMCS fallback; refusing the unoptimized MMCS path for this transfer."
+ "Wallpaper image was checked for sensitive content. Is sensitive: %{BOOL}d, error: %@"
+ "Withholding Madrid content headers to force the MMCS fallback path due to user default."
- "Avatar image was checked for sensitive content. Is sensitive: %d, error: %@"
- "Wallpaper image was checked for sensitive content. Is sensitive: %d, error: %@"
```
