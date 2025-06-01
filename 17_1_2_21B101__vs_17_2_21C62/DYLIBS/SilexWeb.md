## SilexWeb

> `/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb`

```diff

-3529.2.0.0.0
-  __TEXT.__text: 0x146ac
+3557.1.0.0.0
+  __TEXT.__text: 0x15244
   __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x21f8
+  __TEXT.__objc_methlist: 0x2320
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x1818
+  __TEXT.__cstring: 0x18ef
   __TEXT.__gcc_except_tab: 0x150
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x754
-  __TEXT.__objc_classname: 0x7a1
-  __TEXT.__objc_methname: 0x5b70
-  __TEXT.__objc_methtype: 0x186a
-  __TEXT.__objc_stubs: 0x3ca0
+  __TEXT.__unwind_info: 0x77c
+  __TEXT.__objc_classname: 0x7b8
+  __TEXT.__objc_methname: 0x5de4
+  __TEXT.__objc_methtype: 0x18c6
+  __TEXT.__objc_stubs: 0x3de0
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x878
-  __DATA_CONST.__objc_classlist: 0x270
+  __DATA_CONST.__const: 0x8a8
+  __DATA_CONST.__objc_classlist: 0x278
   __DATA_CONST.__objc_catlist: 0x0
-  __DATA_CONST.__objc_protolist: 0x1b0
+  __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x79f8
-  __DATA_CONST.__objc_selrefs: 0x1178
-  __AUTH_CONST.__cfstring: 0x1480
-  __AUTH_CONST.__objc_const: 0x17a0
-  __AUTH_CONST.__const: 0x7a0
+  __DATA_CONST.__objc_const: 0x7c58
+  __DATA_CONST.__objc_selrefs: 0x11d8
+  __AUTH_CONST.__cfstring: 0x1540
+  __AUTH_CONST.__objc_const: 0x1830
+  __AUTH_CONST.__const: 0x7c0
   __AUTH_CONST.__auth_got: 0x250
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_protorefs: 0x108
-  __DATA.__objc_classrefs: 0x3b0
-  __DATA.__objc_superrefs: 0x1f8
-  __DATA.__objc_ivar: 0x388
-  __DATA.__data: 0x1448
+  __AUTH.__objc_data: 0x280
+  __DATA.__objc_protorefs: 0x110
+  __DATA.__objc_classrefs: 0x3b8
+  __DATA.__objc_superrefs: 0x200
+  __DATA.__objc_ivar: 0x3a4
+  __DATA.__data: 0x14a8
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x1630
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x28
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7351F184-64A2-3CEA-9F4A-8CC075B86A86
-  Functions: 756
-  Symbols:   3442
-  CStrings:  1641
+  UUID: 7B4F3230-CAC6-3799-AED7-BB6F6B83DCD2
+  Functions: 781
+  Symbols:   3534
+  CStrings:  1680
 
Symbols:
+ +[SWDatastore emptyDatastore]
+ +[SWDatastoreUpdateScript executableSource]
+ +[SWDatastoreUpdateScript userScriptSource]
+ +[SWLocalDatastoreUpdateScript executableSource]
+ +[SWLocalDatastoreUpdateScript userScriptSource]
+ -[SWConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:isTransitioning:]
+ -[SWConfiguration setSupportsLiveActivities:]
+ -[SWConfiguration supportsLiveActivities]
+ -[SWContainerConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:]
+ -[SWContainerConfiguration setSupportsLiveActivities:]
+ -[SWContainerConfiguration supportsLiveActivities]
+ -[SWContainerViewController initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:]
+ -[SWContainerViewController preferredSizeManager]
+ -[SWContainerViewController scriptsManager]
+ -[SWContainerViewController webViewSetNeedsLayout]
+ -[SWDatastoreUpdateScript userScript]
+ -[SWLocalDatastoreUpdateScript userScript]
+ -[SWMutableConfiguration setSupportsLiveActivities:]
+ -[SWMutableConfiguration supportsLiveActivities]
+ -[SWPreferredSizeManager .cxx_destruct]
+ -[SWPreferredSizeManager didReceiveMessage:securityOrigin:]
+ -[SWPreferredSizeManager initWithMessageHandlerManager:logger:]
+ -[SWPreferredSizeManager logger]
+ -[SWPreferredSizeManager onPreferredSize:]
+ -[SWPreferredSizeManager preferredSizeBlock]
+ -[SWScriptsManager removeScriptByIdentifier:]
+ -[SWScriptsManager scripts]
+ -[SWViewController webViewSetNeedsLayout]
+ GCC_except_table10
+ GCC_except_table13
+ _OBJC_CLASS_$_SWPreferredSizeManager
+ _OBJC_IVAR_$_SWConfiguration._supportsLiveActivities
+ _OBJC_IVAR_$_SWContainerConfiguration._supportsLiveActivities
+ _OBJC_IVAR_$_SWContainerViewController._preferredSizeManager
+ _OBJC_IVAR_$_SWMutableConfiguration.supportsLiveActivities
+ _OBJC_IVAR_$_SWPreferredSizeManager._logger
+ _OBJC_IVAR_$_SWPreferredSizeManager.preferredSizeBlock
+ _OBJC_IVAR_$_SWScriptsManager._scripts
+ _OBJC_METACLASS_$_SWPreferredSizeManager
+ _SWPreferredSizeMessageName
+ _SWWidthKey
+ __OBJC_$_CLASS_METHODS_SWDatastore
+ __OBJC_$_CLASS_PROP_LIST_SWDatastore
+ __OBJC_$_INSTANCE_METHODS_SWPreferredSizeManager
+ __OBJC_$_INSTANCE_VARIABLES_SWPreferredSizeManager
+ __OBJC_$_PROP_LIST_SWDatastoreManager.91
+ __OBJC_$_PROP_LIST_SWPreferredSizeManager
+ __OBJC_$_PROP_LIST_SWPreferredSizeManager.68
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SWPreferredSizeManager
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SWPreferredSizeManager
+ __OBJC_$_PROTOCOL_REFS_SWPreferredSizeManager
+ __OBJC_CLASS_PROTOCOLS_$_SWPreferredSizeManager
+ __OBJC_CLASS_RO_$_SWPreferredSizeManager
+ __OBJC_LABEL_PROTOCOL_$_SWPreferredSizeManager
+ __OBJC_METACLASS_RO_$_SWPreferredSizeManager
+ __OBJC_PROTOCOL_$_SWPreferredSizeManager
+ __OBJC_PROTOCOL_REFERENCE_$_SWPreferredSizeManager
+ ___36-[SWManagerAssembly loadInRegistry:]_block_invoke_30
+ ___43+[SWDatastoreUpdateScript executableSource]_block_invoke
+ ___43+[SWDatastoreUpdateScript userScriptSource]_block_invoke
+ ___48+[SWLocalDatastoreUpdateScript executableSource]_block_invoke
+ ___48+[SWLocalDatastoreUpdateScript userScriptSource]_block_invoke
+ ___block_descriptor_32_e48_"<SWPreferredSizeManager>"16?0"<TFResolver>"8l
+ ___block_literal_global.101
+ ___block_literal_global.104
+ ___block_literal_global.11
+ ___block_literal_global.119
+ ___block_literal_global.126
+ ___block_literal_global.129
+ ___block_literal_global.137
+ ___block_literal_global.141
+ ___block_literal_global.145
+ ___block_literal_global.166
+ ___block_literal_global.191
+ ___block_literal_global.195
+ ___block_literal_global.203
+ ___block_literal_global.211
+ ___block_literal_global.215
+ ___block_literal_global.223
+ ___block_literal_global.239
+ ___block_literal_global.246
+ ___block_literal_global.308
+ ___block_literal_global.64
+ ___block_literal_global.71
+ ___block_literal_global.80
+ ___block_literal_global.93
+ _executableSource.onceToken
+ _executableSource.source
+ _objc_msgSend$emptyDatastore
+ _objc_msgSend$executableSource
+ _objc_msgSend$initWithMessageHandlerManager:logger:
+ _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:
+ _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:isTransitioning:
+ _objc_msgSend$initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:
+ _objc_msgSend$preferredSizeBlock
+ _objc_msgSend$removeScriptByIdentifier:
+ _objc_msgSend$scripts
+ _objc_msgSend$setNeedsLayout
+ _objc_msgSend$setSupportsLiveActivities:
+ _objc_msgSend$supportsLiveActivities
+ _objc_msgSend$userScriptSource
+ _objc_msgSend$webViewSetNeedsLayout
+ _userScriptSource.onceToken
+ _userScriptSource.source
- +[SWDatastoreUpdateScript source]
- +[SWLocalDatastoreUpdateScript source]
- -[SWConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:keyboardConfiguration:isTransitioning:]
- -[SWContainerConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:]
- -[SWContainerViewController initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:configurationManager:presentationManager:scaleManager:snapshotManager:]
- -[SWDatastoreManager reset]
- GCC_except_table11
- GCC_except_table8
- __OBJC_$_PROP_LIST_SWDatastoreManager.95
- ___33+[SWDatastoreUpdateScript source]_block_invoke
- ___38+[SWLocalDatastoreUpdateScript source]_block_invoke
- ___block_literal_global.10
- ___block_literal_global.100
- ___block_literal_global.103
- ___block_literal_global.118
- ___block_literal_global.125
- ___block_literal_global.128
- ___block_literal_global.136
- ___block_literal_global.140
- ___block_literal_global.144
- ___block_literal_global.165
- ___block_literal_global.190
- ___block_literal_global.194
- ___block_literal_global.202
- ___block_literal_global.210
- ___block_literal_global.214
- ___block_literal_global.222
- ___block_literal_global.238
- ___block_literal_global.245
- ___block_literal_global.70
- ___block_literal_global.77
- ___block_literal_global.79
- ___block_literal_global.92
- _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:
- _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:keyboardConfiguration:isTransitioning:
- _objc_msgSend$initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:configurationManager:presentationManager:scaleManager:snapshotManager:
- _objc_msgSend$reset
CStrings:
+ "\x14"
+ "\x1c"
+ "; supportsLiveActivities: %d"
+ "@\"<SWPreferredSizeManager>\""
+ "@\"<SWPreferredSizeManager>\"16@?0@\"<TFResolver>\"8"
+ "@140@0:8@16@24@32@40{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64@96@104@112@120@128B136"
+ "@152@0:8@16@24@32@40{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64@96@104@112@120@128B136@140B148"
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "@?<v@?{CGSize=dd}>16@0:8"
+ "PreferredSize: Received `%@` message with width: %@, height: %@"
+ "SWPreferredSizeManager"
+ "T@\"<SWPreferredSizeManager>\",R,N,V_preferredSizeManager"
+ "T@\"<SWScriptsManager>\",R,N"
+ "T@\"NSMutableDictionary\",R,N,V_scripts"
+ "T@?,C,N,SonPreferredSize:"
+ "T@?,C,N,SonPreferredSize:,VpreferredSizeBlock"
+ "TB,N,V_supportsLiveActivities"
+ "TB,N,VsupportsLiveActivities"
+ "_preferredSizeManager"
+ "_scripts"
+ "_supportsLiveActivities"
+ "datastore-init"
+ "emptyDatastore"
+ "executableSource"
+ "initWithMessageHandlerManager:logger:"
+ "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:"
+ "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:isTransitioning:"
+ "initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:"
+ "local-datastore-init"
+ "onPreferredSize:"
+ "preferredSize"
+ "preferredSizeBlock"
+ "preferredSizeManager"
+ "removeScriptByIdentifier:"
+ "setNeedsLayout"
+ "setSupportsLiveActivities:"
+ "supportsLiveActivities"
+ "userScriptSource"
+ "v24@0:8@?<v@?{CGSize=dd}>16"
+ "webViewSetNeedsLayout"
- "\n"
- "\x1b"
- "@136@0:8@16@24@32@40{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64@96@104@112@120@128"
- "@148@0:8@16@24@32@40{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64@96@104@112@120@128@136B144"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:"
- "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:keyboardConfiguration:isTransitioning:"
- "initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:configurationManager:presentationManager:scaleManager:snapshotManager:"
- "reset"

```
