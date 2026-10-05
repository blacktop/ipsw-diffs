## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-751.200.41.0.0
-  __TEXT.__text: 0xdaa1c
-  __TEXT.__objc_methlist: 0xa190
-  __TEXT.__cstring: 0x14dfc
-  __TEXT.__const: 0x41b8
+751.200.74.0.0
+  __TEXT.__text: 0xdad58
+  __TEXT.__objc_methlist: 0xa1a8
+  __TEXT.__cstring: 0x14eac
+  __TEXT.__const: 0x41a8
   __TEXT.__gcc_except_tab: 0x1518
-  __TEXT.__oslogstring: 0x26fd
+  __TEXT.__oslogstring: 0x26bd
   __TEXT.__swift5_typeref: 0xc4f
   __TEXT.__swift5_capture: 0x950
   __TEXT.__swift5_fieldmd: 0xb34

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x3bf0
+  __TEXT.__unwind_info: 0x3c00
   __TEXT.__eh_frame: 0x960
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x28b0
+  __DATA_CONST.__const: 0x28d8
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4600
+  __DATA_CONST.__objc_selrefs: 0x4610
   __DATA_CONST.__objc_protorefs: 0xf0
   __DATA_CONST.__objc_superrefs: 0x1f8
   __DATA_CONST.__objc_arraydata: 0xb0
   __DATA_CONST.__got: 0x4e8
   __AUTH_CONST.__const: 0x27c0
-  __AUTH_CONST.__cfstring: 0x6160
-  __AUTH_CONST.__objc_const: 0x11670
-  __AUTH_CONST.__objc_intobj: 0x258
+  __AUTH_CONST.__cfstring: 0x5f40
+  __AUTH_CONST.__objc_const: 0x11678
+  __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x1188
-  __AUTH.__objc_data: 0x1350
-  __AUTH.__data: 0x538
+  __AUTH_CONST.__auth_got: 0x1190
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x111c
-  __DATA.__data: 0x2218
+  __DATA.__data: 0x678
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x1318
-  __DATA_DIRTY.__data: 0x588
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__objc_data: 0x2618
+  __DATA_DIRTY.__data: 0x2660
+  __DATA_DIRTY.__bss: 0xd8
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5840
-  Symbols:   6867
-  CStrings:  3081
+  Functions: 5843
+  Symbols:   6872
+  CStrings:  3073
 
Symbols:
+ -[RPClient endpointContextForService:trustCircles:parameters:completion:]
+ ___73-[RPClient endpointContextForService:trustCircles:parameters:completion:]_block_invoke
+ ___73-[RPClient endpointContextForService:trustCircles:parameters:completion:]_block_invoke_2
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ _nw_parameters_copy_dictionary
CStrings:
+ "### Specifying the trust flags using RPOptionStatusFlags for registering message '%@' is required."
+ "-[RPClient endpointContextForService:trustCircles:parameters:completion:]"
+ "-[RPClient endpointContextForService:trustCircles:parameters:completion:]_block_invoke"
+ "Access permitted for %~@ for %@"
+ "Access revoked for %~@ for %@"
+ "Failed to encode parameters"
+ "Failed to encode parameters %@ for %@: %{error}"
+ "MusicHandoffScan"
+ "No change in devices: "
+ "No context provided"
+ "Requesting endpoint context for %@ with %@ and %#ll{flags}\n"
- "### Specifying the trust flags using RPOptionStatusFlags for registering message '%@' is required. Please file a radar in 'Rapport | All' to get more information."
- "FaceTimeAgent"
- "GeneralKnowledgeAgent"
- "HomeKitAgent"
- "HomepodSystemAgent"
- "IMSHPApp"
- "IMSTVApp"
- "MediaAgent"
- "No change in devices: %@"
- "PhotosAgent"
- "ScreenSaverAgent"
- "SearchAgent"
- "SystemAgent"
- "acousticcalibrationd"
- "idac-client"
- "idacd"
- "idactool"
- "imsutil"
- "sgsutil"
```
