## Diagnostic-8262

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8262.appex/Diagnostic-8262`

```diff

-921.120.4.0.0
-  __TEXT.__text: 0x2874
-  __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_stubs: 0x7a0
+1291.0.0.502.1
+  __TEXT.__text: 0x26e0
+  __TEXT.__auth_stubs: 0x2c0
+  __TEXT.__objc_stubs: 0x800
   __TEXT.__objc_methlist: 0x1fc
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x5cc
-  __TEXT.__oslogstring: 0x380
-  __TEXT.__objc_classname: 0x4c
-  __TEXT.__objc_methname: 0x7e7
+  __TEXT.__gcc_except_tab: 0x1bc
+  __TEXT.__cstring: 0x5f4
+  __TEXT.__oslogstring: 0x411
+  __TEXT.__objc_classname: 0x48
+  __TEXT.__objc_methname: 0x88c
   __TEXT.__objc_methtype: 0x163
-  __TEXT.__gcc_except_tab: 0x17c
-  __TEXT.__unwind_info: 0xc8
-  __DATA_CONST.__auth_got: 0x178
-  __DATA_CONST.__got: 0xd0
+  __TEXT.__unwind_info: 0xc0
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__cfstring: 0x640
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__auth_got: 0x170
+  __DATA_CONST.__got: 0xd0
   __DATA.__objc_const: 0x400
-  __DATA.__objc_selrefs: 0x2b0
+  __DATA.__objc_selrefs: 0x2c8
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8AE0D6A-FD65-35B5-A89A-284145502F6C
-  Functions: 32
-  Symbols:   89
-  CStrings:  272
+  UUID: D1142D46-2C41-3857-985A-C30806755A19
+  Functions: 30
+  Symbols:   88
+  CStrings:  278
 
Symbols:
+ _OBJC_CLASS_$_MAAutoAssetSet
+ _OBJC_CLASS_$_MAAutoAssetSetEntry
+ _OBJC_CLASS_$_MAAutoAssetSetPolicy
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- _OBJC_CLASS_$_MAAutoAsset
- _OBJC_CLASS_$_MAAutoAssetPolicy
- _OBJC_CLASS_$_MAAutoAssetSelector
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x22
- _objc_retain_x24
- _objc_retain_x28
CStrings:
+ "AutoAsset set locked successfully, but with 0 asset"
+ "Eliminate asset content successfully"
+ "Failed to eliminate asset content"
+ "Failed to init autoAssetSet"
+ "Failed to lock asset unexpectedly, original error: %@"
+ "InDiagnosticsMode"
+ "Invalid asset instance ID with no inner error populated"
+ "eliminateAtomicSync:usingClientDomain:forAssetSetIdentifier:"
+ "endAtomicLockSync:ofAtomicInstance:"
+ "initUsingClientDomain:forClientName:forAssetSetIdentifier:comprisedOfEntries:error:"
+ "localContentURL"
+ "lockAtomicSync:forAtomicInstance:withNeedPolicy:withTimeout:lockedAtomicEntries:error:"
+ "objectAtIndexedSubscript:"
- "3kmXfug8VcxLI5yEmsqQKw"
- "Failed to init assetSelector"
- "Failed to init autoAsset"
- "Failed to lock asset"
- "endLockUsageSync:"
- "initForClientName:selectingAsset:error:"
- "lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:"

```
