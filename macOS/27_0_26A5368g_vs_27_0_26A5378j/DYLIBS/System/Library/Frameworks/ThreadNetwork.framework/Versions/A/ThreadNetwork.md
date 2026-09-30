## ThreadNetwork

> `/System/Library/Frameworks/ThreadNetwork.framework/Versions/A/ThreadNetwork`

```diff

-  __TEXT.__text: 0xfa14
-  __TEXT.__objc_methlist: 0xd50
+  __TEXT.__text: 0x106bc
+  __TEXT.__objc_methlist: 0xdc0
   __TEXT.__const: 0xb8
-  __TEXT.__cstring: 0x1689
-  __TEXT.__oslogstring: 0xa7b
+  __TEXT.__cstring: 0x18e8
+  __TEXT.__oslogstring: 0xc67
   __TEXT.__gcc_except_tab: 0x190
-  __TEXT.__unwind_info: 0x3d0
+  __TEXT.__unwind_info: 0x3e0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a0
+  __DATA_CONST.__objc_selrefs: 0x7f0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__got: 0x138
-  __AUTH_CONST.__const: 0x5d0
-  __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x1b98
+  __AUTH_CONST.__const: 0x600
+  __AUTH_CONST.__cfstring: 0x880
+  __AUTH_CONST.__objc_const: 0x1bd0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xf8
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xfc
   __DATA.__data: 0x130
   __DATA.__bss: 0x28
-  __DATA_DIRTY.__objc_data: 0x280
+  __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 378
-  Symbols:   951
-  CStrings:  276
+  Functions: 392
+  Symbols:   974
+  CStrings:  302
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __DATA.__data : content changed
Symbols:
+ -[THClient addDataSetWithCompletion:datasetData:completion:]
+ -[THClient deleteDataSetWithCompletion:completion:]
+ -[THClient findAndGetDataSetWithCompletion:completion:]
+ -[THClient getTheProxyWithDataSetCompletion:]
+ -[THClient initCommonForThreadradiodDataset]
+ -[THClient initForThreadradiodDatasetOperations]
+ GCC_except_table35
+ GCC_except_table44
+ GCC_except_table45
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table68
+ GCC_except_table73
+ GCC_except_table8
+ GCC_except_table81
+ OBJC_IVAR_$_THClient._isClientFromThreadradiod
+ _SCDynamicStoreCopyConsoleUser
+ __45-[THClient getTheProxyWithDataSetCompletion:]_block_invoke
+ ___45-[THClient getTheProxyWithDataSetCompletion:]_block_invoke
+ ___51-[THClient deleteDataSetWithCompletion:completion:]_block_invoke
+ ___55-[THClient findAndGetDataSetWithCompletion:completion:]_block_invoke
+ ___60-[THClient addDataSetWithCompletion:datasetData:completion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSData"8"NSError"16l
+ _objc_msgSend$_setTargetUserIdentifier:
+ _objc_msgSend$ctcsServerAddDataSetWithCompletion:datasetData:completion:
+ _objc_msgSend$ctcsServerDeleteDataSetWithCompletion:completion:
+ _objc_msgSend$ctcsServerFindAndGetDataSetWithCompletion:completion:
+ _objc_msgSend$getTheProxyWithDataSetCompletion:
+ _objc_msgSend$initCommonForThreadradiodDataset
- GCC_except_table33
- GCC_except_table42
- GCC_except_table43
- GCC_except_table48
- GCC_except_table51
- GCC_except_table54
- GCC_except_table6
- GCC_except_table66
- GCC_except_table71
- GCC_except_table79
CStrings:
+ "%s:%d: - Response: datasetData length = %lu, error = %@"
+ "%s:%d: - Response: error = %@"
+ "-[THClient addDataSetWithCompletion:datasetData:completion:]"
+ "-[THClient addDataSetWithCompletion:datasetData:completion:]_block_invoke"
+ "-[THClient deleteDataSetWithCompletion:completion:]"
+ "-[THClient deleteDataSetWithCompletion:completion:]_block_invoke"
+ "-[THClient findAndGetDataSetWithCompletion:completion:]"
+ "-[THClient findAndGetDataSetWithCompletion:completion:]_block_invoke"
+ "-[THClient getTheProxyWithDataSetCompletion:]_block_invoke"
+ "-[THClient initForThreadradiodDatasetOperations]"
+ "Active"
+ "CTCS XPC Client Thread Safe Property Queue (RCP Dataset)"
+ "Client: %s - XPC Client Init for Threadradiod Dataset Failed"
+ "Client: %s - XPC Client Init for Threadradiod Dataset done"
+ "Client: %s:%d - Adding %@ dataset"
+ "Client: %s:%d - Deleting %@ dataset"
+ "Client: %s:%d - Error: %@"
+ "Client: %s:%d - Retrieving %@ dataset"
+ "Client: %s:%d Threadradiod RCP Dataset - TargetUserSession %ld for %@"
+ "Client: %s:%d Threadradiod RCP Dataset - TargetUserSession, no console user found"
+ "Invalid dataset data"
+ "Pending"
+ "thclient"
+ "thserver"
+ "v24@?0@\"NSData\"8@\"NSError\"16"
- "THClient"
- "THServer"

```
