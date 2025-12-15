## MediaRemote

> `/System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote`

```diff

-4025.310.1.0.0
-  __TEXT.__text: 0x2f3e38
+4025.400.2.0.0
+  __TEXT.__text: 0x2f4444
   __TEXT.__auth_stubs: 0x16f0
   __TEXT.__objc_methlist: 0x2b0a0
   __TEXT.__const: 0x5f8
-  __TEXT.__cstring: 0x2bce3
-  __TEXT.__oslogstring: 0xdb82
-  __TEXT.__gcc_except_tab: 0x65a8
+  __TEXT.__cstring: 0x2bd96
+  __TEXT.__oslogstring: 0xdbca
+  __TEXT.__gcc_except_tab: 0x66a0
   __TEXT.__dlopen_cstrs: 0x514
   __TEXT.__ustring: 0x796
-  __TEXT.__unwind_info: 0xb2a0
+  __TEXT.__unwind_info: 0xb2b0
   __TEXT.__objc_classname: 0x4dad
   __TEXT.__objc_methname: 0x4d504
   __TEXT.__objc_methtype: 0x90b9

   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb88
   __AUTH_CONST.__const: 0x3080
-  __AUTH_CONST.__cfstring: 0x23200
+  __AUTH_CONST.__cfstring: 0x232c0
   __AUTH_CONST.__objc_const: 0x45ca0
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_intobj: 0x4e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FFA8FB7-7654-3430-8ADB-D1E605F79E3A
+  UUID: 372DF73F-C055-31DF-A8D9-D26AEB4A6C03
   Functions: 20166
-  Symbols:   55367
-  CStrings:  24394
+  Symbols:   55369
+  CStrings:  24407
 
Symbols:
+ -[MRAVReconnaissanceSession _onQueue_concludeSearchWithReason:]
+ ___107-[MRAVLightweightReconnaissanceSession searchForOutputDevices:categories:timeout:details:queue:completion:]_block_invoke_4
+ ___block_descriptor_56_e8_32s40s48s_e18_16?0"NSString"8ls32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs72r_e46_v32?0"NSArray"8"MRAVEndpoint"16"NSError"24ls32l8s64l8s40l8s48l8r72l8s56l8
- -[MRAVReconnaissanceSession _onQueue_concludeSearch]
- ___block_descriptor_48_e8_32s40bs_e46_v32?0"NSArray"8"MRAVEndpoint"16"NSError"24ls40l8s32l8
- ___block_descriptor_48_e8_32s40s_e18_16?0"NSString"8ls32l8s40l8
CStrings:
+ "Found expectedLogicalDevice Match"
+ "Found logicalDevice Match"
+ "Found potential leader"
+ "Found result"
+ "SearchForGroup: Found acceptable leader"
+ "SearchForGroup: Found silentPrimary leader"
+ "[ReconnaissanceSession] Successfully concluded search reason=%{public}@"

```
