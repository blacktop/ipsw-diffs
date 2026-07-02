## CoreCDPInternal

> `/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal`

```diff

-  __TEXT.__text: 0x96600
+  __TEXT.__text: 0x96be0
   __TEXT.__auth_stubs: 0x1160
-  __TEXT.__objc_methlist: 0x5664
+  __TEXT.__objc_methlist: 0x567c
   __TEXT.__const: 0x850
-  __TEXT.__oslogstring: 0x1494e
+  __TEXT.__oslogstring: 0x14a5e
   __TEXT.__cstring: 0xdda5
   __TEXT.__gcc_except_tab: 0xc90
   __TEXT.__dlopen_cstrs: 0xb0

   __TEXT.__swift5_capture: 0x200
   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x58
-  __TEXT.__unwind_info: 0x1f88
+  __TEXT.__unwind_info: 0x1f98
   __TEXT.__eh_frame: 0x958
   __TEXT.__objc_classname: 0xdbd
-  __TEXT.__objc_methname: 0xfaff
+  __TEXT.__objc_methname: 0xfb5f
   __TEXT.__objc_methtype: 0x2aa7
-  __TEXT.__objc_stubs: 0xcd40
-  __DATA_CONST.__got: 0x10b0
+  __TEXT.__objc_stubs: 0xcd80
+  __DATA_CONST.__got: 0x10b8
   __DATA_CONST.__const: 0x25c0
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38f0
+  __DATA_CONST.__objc_selrefs: 0x3900
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x208

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3159
-  Symbols:   10426
-  CStrings:  6589
+  Functions: 3165
+  Symbols:   10443
+  CStrings:  6594
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[CDPDFollowUpController _existingTelemetryFlowIDForIdentifier:usingController:]
+ -[CDPInternalWalrusStateController _hydrateRepairTelemetryOnContext]
+ _CDPFollowUpItemUserInfoKeyTelemetryFlowID
+ _objc_msgSend$_existingTelemetryFlowIDForIdentifier:usingController:
+ _objc_msgSend$_hydrateRepairTelemetryOnContext
CStrings:
+ "CDPInternalWalrusStateController: no CDPContext available; walrusRepair telemetry will lack flow/session IDs"
+ "CDPInternalWalrusStateController: no telemetryFlowID on daemon _context; minted for repair pair: %{public}@"
+ "Failed to fetch pending CFUs for telemetryFlowID reuse (%@): %@"
+ "_existingTelemetryFlowIDForIdentifier:usingController:"
+ "_hydrateRepairTelemetryOnContext"

```
