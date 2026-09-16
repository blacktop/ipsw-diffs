## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore`

```diff

-2718.0.18.0.0
-  __TEXT.__text: 0xacbb0
-  __TEXT.__objc_methlist: 0x842c
-  __TEXT.__cstring: 0x1620d
+2718.40.13.0.0
+  __TEXT.__text: 0xacabc
+  __TEXT.__objc_methlist: 0x8444
+  __TEXT.__cstring: 0x161ed
   __TEXT.__const: 0x1e2
   __TEXT.__gcc_except_tab: 0x764
-  __TEXT.__oslogstring: 0xcef3
+  __TEXT.__oslogstring: 0xce93
   __TEXT.__dlopen_cstrs: 0x41
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x43

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a60
+  __DATA_CONST.__objc_selrefs: 0x4a70
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0xb30
   __AUTH_CONST.__const: 0x508
-  __AUTH_CONST.__cfstring: 0x137a0
+  __AUTH_CONST.__cfstring: 0x13780
   __AUTH_CONST.__objc_const: 0xbb88
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xa8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3290
-  Symbols:   7804
-  CStrings:  3300
+  Functions: 3292
+  Symbols:   7808
+  CStrings:  3297
 
Symbols:
+ -[SUCoreUpdateDownloader _stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]
+ -[SUCoreUpdateDownloader initWithDelegate:forUpdate:updateUUID:maControl:maControlSplombo:]
+ _objc_msgSend$_stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:
+ _objc_msgSend$initWithDelegate:forUpdate:updateUUID:maControl:maControlSplombo:
CStrings:
+ "2.2.0"
+ "[SPACE] Entitled secured space is taken into account, sharedFreeSpace= %llu, entitledFreeSpace= %llu, freeSpaceAvailableForSoftwareUpdate= %llu, entitledSpaceDisableInSUCore= %{public}@"
- "1.0.6"
- "[POWER_ASSERTION] DISPATCH: created dispatch queue domain(%{public}@)"
- "[SPACE] DISPATCH: created dispatch queue domain(%{public}@)"
- "[SPACE] Entitled secured space is taken into account, sharedFreeSpace= %llu, entitledFreeSpace= %llu, freeSpaceAvailableForSoftwareUpdate= %llu"
- "unable to create dispatch queue domain(%@)"
```
