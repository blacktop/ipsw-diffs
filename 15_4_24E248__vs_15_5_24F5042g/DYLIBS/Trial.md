## Trial

> `/System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial`

```diff

-429.20.0.0.0
-  __TEXT.__text: 0x87c78
+429.20.2.0.0
+  __TEXT.__text: 0x87ce4
   __TEXT.__auth_stubs: 0xa40
   __TEXT.__delay_helper: 0x258
   __TEXT.__objc_methlist: 0x71f0
   __TEXT.__const: 0xf0a
   __TEXT.__dlopen_cstrs: 0x101
   __TEXT.__gcc_except_tab: 0x5568
-  __TEXT.__cstring: 0x9bc1
+  __TEXT.__cstring: 0x9bc3
   __TEXT.__oslogstring: 0x4be6
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x26b8
   __TEXT.__objc_classname: 0x13e5
-  __TEXT.__objc_methname: 0xeb06
-  __TEXT.__objc_methtype: 0x2e66
-  __TEXT.__objc_stubs: 0x9fe0
+  __TEXT.__objc_methname: 0xeb19
+  __TEXT.__objc_methtype: 0x2e70
+  __TEXT.__objc_stubs: 0x9fc0
   __DATA_CONST.__got: 0x870
   __DATA_CONST.__const: 0x8e8
   __DATA_CONST.__objc_classlist: 0x4f8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36b0
+  __DATA_CONST.__objc_selrefs: 0x36a8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x338
   __DATA_CONST.__objc_arraydata: 0x1b8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2595
-  Symbols:   6744
-  CStrings:  4301
+  Symbols:   6743
+  CStrings:  4300
 
Symbols:
+ +[TRIAllocationStatus activeExperimentInformationWithEnvironments:error:]
+ +[TRIClient activeExperimentInformationWithEnvironments:error:]
+ +[TRIClient printedExperimentInformationWithEnvironments:error:]
+ -[TRIAllocationStatusDefaultProvider activeExperimentInformationWithEnvironments:error:]
+ __101-[TRIXPCNamespaceManagementClient immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:]_block_invoke.191
+ __109-[TRIXPCNamespaceManagementClient removeLevelsForFactors:withNamespace:factorsState:removeImmediately:error:]_block_invoke.202
+ __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.178
+ __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.182
+ __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.185
+ __150-[TRIXPCNamespaceManagementClient registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:error:]_block_invoke.163
+ __88-[TRIAllocationStatusDefaultProvider activeExperimentInformationWithEnvironments:error:]_block_invoke.188
+ ___64+[TRIClient printedExperimentInformationWithEnvironments:error:]_block_invoke
+ ___88-[TRIAllocationStatusDefaultProvider activeExperimentInformationWithEnvironments:error:]_block_invoke
+ __block_literal_global.141
+ __block_literal_global.143
+ __block_literal_global.145
+ __block_literal_global.147
+ __block_literal_global.149
+ __block_literal_global.196
+ _objc_msgSend$activeExperimentInformationWithEnvironments:error:
+ _objc_msgSend$activeExperimentInformationWithEnvironments:privacyFilterPolicy:completion:
- +[TRIAllocationStatus activeExperimentInformationWithError:]
- +[TRIClient activeExperimentInformation:]
- +[TRIClient printedExperimentInformation:]
- -[TRIAllocationStatusDefaultProvider activeExperimentInformationWithError:]
- __101-[TRIXPCNamespaceManagementClient immediateDownloadForNamespaceNames:allowExpensiveNetworking:error:]_block_invoke.189
- __109-[TRIXPCNamespaceManagementClient removeLevelsForFactors:withNamespace:factorsState:removeImmediately:error:]_block_invoke.201
- __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.176
- __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.181
- __121-[TRIXPCNamespaceManagementClient downloadLevelsForFactors:withNamespace:queue:factorsState:options:progress:completion:]_block_invoke.184
- __150-[TRIXPCNamespaceManagementClient registerNamespaceWithNamespaceName:compatibilityVersion:defaultsFileURL:applicationGroup:cloudKitContainerId:error:]_block_invoke.162
- __75-[TRIAllocationStatusDefaultProvider activeExperimentInformationWithError:]_block_invoke.188
- ___42+[TRIClient printedExperimentInformation:]_block_invoke
- ___75-[TRIAllocationStatusDefaultProvider activeExperimentInformationWithError:]_block_invoke
- __block_literal_global.140
- __block_literal_global.142
- __block_literal_global.144
- __block_literal_global.146
- __block_literal_global.148
- __block_literal_global.195
- _objc_msgSend$activeExperimentInformation:
- _objc_msgSend$activeExperimentInformationWithError:
- _objc_msgSend$activeExperimentInformationWithPrivacyFilterPolicy:completion:
CStrings:
+ "TrialXP-429.20.2"
+ "activeExperimentInformationWithEnvironments:error:"
+ "activeExperimentInformationWithEnvironments:privacyFilterPolicy:completion:"
+ "printedExperimentInformationWithEnvironments:error:"
+ "v36@0:8@\"NSSet\"16C24@?<v@?@\"NSArray\">28"
- "TrialXP-429.20"
- "activeExperimentInformation:"
- "activeExperimentInformationWithError:"
- "activeExperimentInformationWithPrivacyFilterPolicy:completion:"
- "printedExperimentInformation:"
- "v28@0:8C16@?<v@?@\"NSArray\">20"

```
