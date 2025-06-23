## Trial

> `/System/Library/PrivateFrameworks/Trial.framework/Trial`

```diff

-463.0.0.0.0
-  __TEXT.__text: 0x696ac
+466.0.0.0.0
+  __TEXT.__text: 0x69818
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x5c78
+  __TEXT.__objc_methlist: 0x5c98
   __TEXT.__const: 0xeca
   __TEXT.__cstring: 0x835e
+  __TEXT.__oslogstring: 0x3eb9
   __TEXT.__gcc_except_tab: 0x52bc
-  __TEXT.__oslogstring: 0x3da7
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2150
+  __TEXT.__unwind_info: 0x2158
   __TEXT.__objc_classname: 0x1069
-  __TEXT.__objc_methname: 0xc07c
-  __TEXT.__objc_methtype: 0x257c
-  __TEXT.__objc_stubs: 0x8340
+  __TEXT.__objc_methname: 0xc0b8
+  __TEXT.__objc_methtype: 0x25b4
+  __TEXT.__objc_stubs: 0x8360
   __DATA_CONST.__got: 0x708
   __DATA_CONST.__const: 0x1918
   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d48
+  __DATA_CONST.__objc_selrefs: 0x2d58
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a8
   __DATA_CONST.__objc_arraydata: 0x1b8
   __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0xda0
   __AUTH_CONST.__cfstring: 0x6780
-  __AUTH_CONST.__objc_const: 0xa568
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__objc_const: 0xa570
   __AUTH_CONST.__objc_intobj: 0x138
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x370
   __AUTH.__data: 0x90

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B1236E71-CB43-3C1E-9AF3-7552339C2194
-  Functions: 2093
-  Symbols:   7694
-  CStrings:  4411
+  UUID: AC612461-7664-39E5-AE69-32D6DDB7FFEE
+  Functions: 2095
+  Symbols:   7699
+  CStrings:  4416
 
Symbols:
+ -[TRIClient _hasAccessToDirectory:]
+ -[TRIClient init]
+ ___101-[TRIXPCNamespaceManagementClient immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:]_block_invoke.194
+ ___109-[TRIXPCNamespaceManagementClient removeLevelsForFactors:withNamespace:factorsState:removeImmediately:error:]_block_invoke.205
+ ___121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.185
+ ___121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.186
+ ___block_literal_global.158
+ ___block_literal_global.164
+ ___block_literal_global.168
+ ___block_literal_global.199
+ _objc_msgSend$_hasAccessToDirectory:
- ___101-[TRIXPCNamespaceManagementClient immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:]_block_invoke.192
- ___109-[TRIXPCNamespaceManagementClient removeLevelsForFactors:withNamespace:factorsState:removeImmediately:error:]_block_invoke.203
- ___121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.183
- ___121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.184
- ___block_literal_global.148
- ___block_literal_global.162
- ___block_literal_global.166
- ___block_literal_global.197
CStrings:
+ "API MISUSE IN CLIENT OF TRIAL: [TRIClient new] and TRIClient() are not supported. Please see TRIClient.h for a recommendation on what to use instead"
+ "Cannot access %@ or %@ - Please ensure you have set the entitlement \n<key>com.apple.trial.client</key> to the right value(s)"
+ "TrialXP-466"
+ "_hasAccessToDirectory:"
+ "experimentHasMatchingNCV:completion:"
+ "v32@0:8@\"TRIExperimentDeployment\"16@?<v@?B@\"NSError\">24"
- "TrialXP-463"

```
