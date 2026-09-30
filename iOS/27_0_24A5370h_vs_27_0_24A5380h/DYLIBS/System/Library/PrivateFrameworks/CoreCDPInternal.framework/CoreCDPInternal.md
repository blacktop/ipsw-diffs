## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-  __TEXT.__text: 0x8d5a0
-  __TEXT.__objc_methlist: 0x5664
+  __TEXT.__text: 0x8db84
+  __TEXT.__objc_methlist: 0x567c
   __TEXT.__const: 0x888
-  __TEXT.__oslogstring: 0x1494e
-  __TEXT.__cstring: 0xe035
+  __TEXT.__oslogstring: 0x14a5e
+  __TEXT.__cstring: 0xe055
   __TEXT.__gcc_except_tab: 0xb94
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0x3b7

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
   __TEXT.__swift_as_cont: 0x68
-  __TEXT.__unwind_info: 0x1de0
+  __TEXT.__unwind_info: 0x1df0
   __TEXT.__eh_frame: 0x8f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38f0
+  __DATA_CONST.__objc_selrefs: 0x3900
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x220
-  __DATA_CONST.__got: 0x10b0
+  __DATA_CONST.__got: 0x10b8
   __AUTH_CONST.__const: 0xad0
-  __AUTH_CONST.__cfstring: 0x94a0
+  __AUTH_CONST.__cfstring: 0x94c0
   __AUTH_CONST.__objc_const: 0x100b0
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x968
-  __AUTH.__objc_data: 0x1070
-  __AUTH.__data: 0x58
+  __AUTH_CONST.__auth_got: 0x960
+  __AUTH.__objc_data: 0x120
   __DATA.__objc_ivar: 0x3b0
   __DATA.__data: 0x1220
-  __DATA.__bss: 0x4c0
-  __DATA_DIRTY.__objc_data: 0xa60
-  __DATA_DIRTY.__data: 0x1a8
-  __DATA_DIRTY.__bss: 0x1a0
+  __DATA.__bss: 0x490
+  __DATA_DIRTY.__objc_data: 0x19b0
+  __DATA_DIRTY.__data: 0x200
+  __DATA_DIRTY.__bss: 0x1d0
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3151
-  Symbols:   10329
-  CStrings:  3990
+  Functions: 3157
+  Symbols:   10345
+  CStrings:  3995
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
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
+ _CDPFollowUpItemUserInfoKeyTelemetryFlowID
+ _objc_msgSend$_existingTelemetryFlowIDForIdentifier:usingController:
+ _objc_msgSend$_hydrateRepairTelemetryOnContext
- _swift_retain_x25
CStrings:
+ "AKAccountStateErrorDomain"
+ "CDPInternalWalrusStateController: no CDPContext available; walrusRepair telemetry will lack flow/session IDs"
+ "CDPInternalWalrusStateController: no telemetryFlowID on daemon _context; minted for repair pair: %{public}@"
+ "Failed to fetch pending CFUs for telemetryFlowID reuse (%@): %@"

```
