## SoftwareUpdateCore

> `/System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/Versions/A/SoftwareUpdateCore`

```diff

-2718.0.18.0.0
-  __TEXT.__text: 0xb2ddc
-  __TEXT.__objc_methlist: 0x7fcc
-  __TEXT.__cstring: 0x1592d
+2718.40.17.0.0
+  __TEXT.__text: 0xb2e5c
+  __TEXT.__objc_methlist: 0x7ffc
+  __TEXT.__cstring: 0x1590d
   __TEXT.__const: 0x1e2
   __TEXT.__gcc_except_tab: 0x758
-  __TEXT.__oslogstring: 0xbe43
+  __TEXT.__oslogstring: 0xbdc3
   __TEXT.__constg_swiftt: 0x50
   __TEXT.__swift5_typeref: 0x43
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1818
+  __TEXT.__unwind_info: 0x1820
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4758
+  __DATA_CONST.__objc_selrefs: 0x4778
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0xe8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3207
-  Symbols:   7567
-  CStrings:  3182
+  Functions: 3211
+  Symbols:   7575
+  CStrings:  3180
 
Symbols:
+ +[SUCoreDescriptor _booleanValueForKey:withAttributes:defaultValues:fallback:]
+ +[SUCoreDescriptor _ullValueForKey:withAttributes:defaultValues:fallback:]
+ -[SUCoreUpdateDownloader _stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:]
+ -[SUCoreUpdateDownloader initWithDelegate:forUpdate:updateUUID:maControl:maControlSplombo:]
+ _objc_msgSend$_booleanValueForKey:withAttributes:defaultValues:fallback:
+ _objc_msgSend$_stageDownloadGroups:awaitingAllGroups:withStagingTimeout:reportingProgress:completion:
+ _objc_msgSend$_ullValueForKey:withAttributes:defaultValues:fallback:
+ _objc_msgSend$initWithDelegate:forUpdate:updateUUID:maControl:maControlSplombo:
CStrings:
+ "2.2.0"
+ "HomeAccessory"
- "1.0.6"
- "[POWER_ASSERTION] DISPATCH: created dispatch queue domain(%{public}@)"
- "[SPACE] DISPATCH: created dispatch queue domain(%{public}@)"
- "unable to create dispatch queue domain(%@)"
```
