## DialogEngine

> `/System/Library/PrivateFrameworks/DialogEngine.framework/DialogEngine`

```diff

-3404.15.1.0.0
-  __TEXT.__text: 0x4f9308
-  __TEXT.__auth_stubs: 0x20a0
+3405.7.1.0.0
+  __TEXT.__text: 0x4fa484
+  __TEXT.__auth_stubs: 0x20e0
   __TEXT.__init_offsets: 0x28
-  __TEXT.__objc_methlist: 0x335c
-  __TEXT.__const: 0x1ba3b
-  __TEXT.__cstring: 0x66252
-  __TEXT.__gcc_except_tab: 0x3c78c
+  __TEXT.__objc_methlist: 0x3374
+  __TEXT.__const: 0x1ba43
+  __TEXT.__cstring: 0x6658f
+  __TEXT.__gcc_except_tab: 0x3c9cc
   __TEXT.__oslogstring: 0x2bf
   __TEXT.__ustring: 0xaa
-  __TEXT.__unwind_info: 0x13ea0
+  __TEXT.__unwind_info: 0x13f78
   __TEXT.__objc_classname: 0x4de
-  __TEXT.__objc_methname: 0x6a9c
+  __TEXT.__objc_methname: 0x6b89
   __TEXT.__objc_methtype: 0x5f55
-  __TEXT.__objc_stubs: 0x4240
-  __DATA_CONST.__got: 0x5a8
-  __DATA_CONST.__const: 0x3108
+  __TEXT.__objc_stubs: 0x4320
+  __DATA_CONST.__got: 0x5c8
+  __DATA_CONST.__const: 0x3110
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18c8
+  __DATA_CONST.__objc_selrefs: 0x1900
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x188
-  __AUTH_CONST.__auth_got: 0x1068
+  __AUTH_CONST.__auth_got: 0x1088
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x12948
-  __AUTH_CONST.__cfstring: 0x1ae0
-  __AUTH_CONST.__objc_const: 0x62a8
+  __AUTH_CONST.__cfstring: 0x1b60
+  __AUTH_CONST.__objc_const: 0x62d8
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH.__data: 0x888
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x3b4
+  __DATA.__objc_ivar: 0x3b8
   __DATA.__data: 0x570
   __DATA.__common: 0x1288
-  __DATA.__bss: 0x3538
+  __DATA.__bss: 0x35b8
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__data: 0x17f8
-  __DATA_DIRTY.__common: 0x29b0
-  __DATA_DIRTY.__bss: 0x238
+  __DATA_DIRTY.__common: 0x29a8
+  __DATA_DIRTY.__bss: 0x268
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FeatureStore.framework/FeatureStore
   - /System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 15461
-  Symbols:   18136
-  CStrings:  28166
+  Functions: 15486
+  Symbols:   18171
+  CStrings:  28204
 
Symbols:
+ _CATDisableLogging
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_CLASS_$_UTType
+ __ZN4siri12dialogengine19ReadOneMetadataFileERKNS0_20DialogMetadataParserERKNSt3__112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEESC_RNS0_13SemanticModelERNS4_3mapIN7morphun6dialog13SemanticValueENSH_32SemanticFeatureModel_DisplayDataENS4_4lessISI_EENS8_INS4_4pairIKSI_SJ_EEEEEE
+ __ZN4siri12dialogengine20RunningBoardAsserted35IsCurrentProcessRunningBoardManagedEv
+ __ZN4siri12dialogengine20RunningBoardAssertedC1ERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZN4siri12dialogengine20RunningBoardAssertedC2ERKNSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE
+ __ZN4siri12dialogengine20RunningBoardAssertedD1Ev
+ __ZN4siri12dialogengine20RunningBoardAssertedD2Ev
+ __ZN4siri12dialogengine21ForceLoggingIsEnabledEv
+ __ZN4siri12dialogengine22OPTION_DISABLE_LOGGINGE
+ __ZN4siri12dialogengine22SemanticModel_PostLoadERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_RNS0_13SemanticModelERNS1_3mapIN7morphun6dialog13SemanticValueENSE_32SemanticFeatureModel_DisplayDataENS1_4lessISF_EENS5_INS1_4pairIKSF_SG_EEEEEE
+ __ZN4siri12dialogengine23GetProductNameForDeviceERKNSt3__112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_
+ __ZN4siri12dialogengine3Log11DisableLockC1Em
+ __ZN4siri12dialogengine3Log11DisableLockC2Em
+ __ZN4siri12dialogengine3Log11DisableLockD1Ev
+ __ZN4siri12dialogengine3Log11DisableLockD2Ev
+ __ZN4siri12dialogengine3Log13EnableLoggingERKNS1_11DisableLockE
+ __ZN4siri12dialogengine3Log14DisableLoggingEv
+ __ZN4siri12dialogengine3Log16IsLoggingEnabledEv
+ __ZN4siri12dialogengine7Context14DisableLoggingEv
+ __ZNK4siri12dialogengine3Log11DisableLock7releaseEv
+ __ZNSt3__115recursive_mutex4lockEv
+ __ZNSt3__115recursive_mutex6unlockEv
+ __ZNSt3__115recursive_mutexC1Ev
+ __ZNSt3__16chrono12steady_clock3nowEv
- __ZN4siri12dialogengine25GetCurrentProcessBundleIdEv
CStrings:
+ "3405.7.1"
+ "5.5"
+ "Aborting on-demand Morphun asset download; request executed from RunningBoard managed process."
+ "CAT Request (Dialog Engine 3405.7.1)"
+ "Could not create FinishTaskUninterruptable background assertion for operation \"%s\": %s"
+ "Created FinishTaskUninterruptable background assertion for operation \"%s\""
+ "Disable logging requested"
+ "Failed to release FinishTaskUninterruptable background assertion for operation \"%s\""
+ "FinishTaskUninterruptable"
+ "FinishTaskUninterruptable background assertion unnecessary for assistant_service process and was not created."
+ "Log::DisableLogging"
+ "Log::EnableLogging"
+ "Released FinishTaskUninterruptable background assertion for operation \"%s\""
+ "RunningBoard-asserted UAFAssetSet retrieval for CAT assets"
+ "RunningBoard-asserted UAFAssetSet update handler retrieval for CAT assets"
+ "TB,N,V_disableLogging"
+ "UAFAssetSet CAT update assertion"
+ "[GetProductNameForDevice] Unsupported device [%s]"
+ "_disableLogging"
+ "_localizedDescriptionWithPreferredLocalizations:"
+ "acquireWithError:"
+ "apple_tv"
+ "apple_watch"
+ "attributeWithDomain:name:"
+ "com.apple.apple-tv"
+ "com.apple.common"
+ "com.apple.homepod"
+ "com.apple.ipad"
+ "com.apple.iphone"
+ "com.apple.mac"
+ "com.apple.visionpro"
+ "com.apple.watch"
+ "disableLogging"
+ "error undefined"
+ "forceLogging"
+ "homepod"
+ "initWithExplanation:target:attributes:"
+ "invalidateWithError:"
+ "ipad"
+ "isManaged"
+ "mac"
+ "reality_device"
+ "setDisableLogging:"
+ "typeWithIdentifier:"
- "3404.15.1"
- "Aborting on-demand Morphun asset download; request executed from non-assistant_service process."
- "CAT Request (Dialog Engine 3404.15.1)"
- "DialogEngine executed from a non-assistant_service process; aborting UAFAsset update to avoid RunningBoard crash."
- "bundle"
- "com.apple.AssistantServices"

```
