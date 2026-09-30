## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/Versions/A/CoreCDPInternal`

```diff

-  __TEXT.__text: 0x93408
-  __TEXT.__objc_methlist: 0x553c
+  __TEXT.__text: 0x93a64
+  __TEXT.__objc_methlist: 0x5554
   __TEXT.__const: 0x890
-  __TEXT.__oslogstring: 0x144da
-  __TEXT.__cstring: 0xdad6
+  __TEXT.__oslogstring: 0x145fa
+  __TEXT.__cstring: 0xdae6
   __TEXT.__gcc_except_tab: 0xb48
   __TEXT.__dlopen_cstrs: 0xbc
   __TEXT.__constg_swiftt: 0x1e4

   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x1de8
+  __TEXT.__unwind_info: 0x1df8
   __TEXT.__eh_frame: 0x8f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x180
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3860
+  __DATA_CONST.__objc_selrefs: 0x3870
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__got: 0x1080
+  __DATA_CONST.__got: 0x1088
   __AUTH_CONST.__const: 0x2d90
-  __AUTH_CONST.__cfstring: 0x90c0
+  __AUTH_CONST.__cfstring: 0x90e0
   __AUTH_CONST.__objc_const: 0xfb08
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH.__objc_data: 0x1020
-  __AUTH.__data: 0x58
+  __AUTH.__objc_data: 0x120
   __DATA.__objc_ivar: 0x3a4
   __DATA.__data: 0x1190
-  __DATA.__bss: 0x4c8
-  __DATA_DIRTY.__objc_data: 0xa10
-  __DATA_DIRTY.__data: 0x1a8
-  __DATA_DIRTY.__bss: 0x188
+  __DATA.__bss: 0x498
+  __DATA_DIRTY.__objc_data: 0x1910
+  __DATA_DIRTY.__data: 0x208
+  __DATA_DIRTY.__bss: 0x1b8
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3163
-  Symbols:   7163
-  CStrings:  3906
+  Functions: 3169
+  Symbols:   7173
+  CStrings:  3911
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ -[CDPDFollowUpController _existingTelemetryFlowIDForIdentifier:usingController:]
+ -[CDPInternalWalrusStateController _hydrateRepairTelemetryOnContext]
+ GCC_except_table21
+ _CDPFollowUpItemUserInfoKeyTelemetryFlowID
+ _objc_msgSend$_existingTelemetryFlowIDForIdentifier:usingController:
+ _objc_msgSend$_hydrateRepairTelemetryOnContext
- GCC_except_table20
CStrings:
+ "AKAccountStateErrorDomain"
+ "CDPInternalWalrusStateController: no CDPContext available; walrusRepair telemetry will lack flow/session IDs"
+ "CDPInternalWalrusStateController: no telemetryFlowID on daemon _context; minted for repair pair: %{public}@"
+ "Failed to fetch pending CFUs for telemetryFlowID reuse (%@): %@"

```
