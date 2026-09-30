## SilexWeb

> `/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb`

```diff

-5681.0.0.0.0
-  __TEXT.__text: 0x156d4
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x2e2c
+5718.1.0.0.0
+  __TEXT.__text: 0x16598
+  __TEXT.__auth_stubs: 0x470
+  __TEXT.__objc_methlist: 0x3034
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x194e
+  __TEXT.__cstring: 0x1bb3
   __TEXT.__gcc_except_tab: 0x150
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x7a8
-  __TEXT.__objc_classname: 0x7b8
-  __TEXT.__objc_methname: 0x60a3
-  __TEXT.__objc_methtype: 0x1a18
-  __TEXT.__objc_stubs: 0x3f80
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__const: 0x8c0
-  __DATA_CONST.__objc_classlist: 0x278
-  __DATA_CONST.__objc_protolist: 0x1b8
+  __TEXT.__unwind_info: 0x7e8
+  __TEXT.__objc_classname: 0x861
+  __TEXT.__objc_methname: 0x6506
+  __TEXT.__objc_methtype: 0x1afa
+  __TEXT.__objc_stubs: 0x4060
+  __DATA_CONST.__got: 0x448
+  __DATA_CONST.__const: 0x978
+  __DATA_CONST.__objc_classlist: 0x2a8
+  __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13d8
-  __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0x200
-  __AUTH_CONST.__auth_got: 0x250
-  __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x15e0
-  __AUTH_CONST.__objc_const: 0x8480
-  __AUTH.__objc_data: 0x230
-  __DATA.__objc_ivar: 0x3b8
-  __DATA.__data: 0x14a8
-  __DATA_DIRTY.__objc_data: 0x1680
+  __DATA_CONST.__objc_selrefs: 0x1478
+  __DATA_CONST.__objc_protorefs: 0x128
+  __DATA_CONST.__objc_superrefs: 0x228
+  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__const: 0x840
+  __AUTH_CONST.__cfstring: 0x17c0
+  __AUTH_CONST.__objc_const: 0x8c98
+  __AUTH.__objc_data: 0x3c0
+  __DATA.__objc_ivar: 0x3e8
+  __DATA.__data: 0x1628
+  __DATA_DIRTY.__objc_data: 0x16d0
   __DATA_DIRTY.__bss: 0x68
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C5D7C6A0-9C2C-342D-9FF7-7545CF2C1365
-  Functions: 801
-  Symbols:   3595
-  CStrings:  1714
+  UUID: 9C498222-BAC5-3D88-8CF9-3863BD413A36
+  Functions: 835
+  Symbols:   3763
+  CStrings:  1804
 
Symbols:
+ -[SWConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:layoutGuide:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:]
+ -[SWConfiguration layoutGuide]
+ -[SWConfiguration setLayoutGuide:]
+ -[SWContainerConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:layoutGuide:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:]
+ -[SWContainerConfiguration layoutGuide]
+ -[SWContainerConfiguration setLayoutGuide:]
+ -[SWContainerViewController failureProvider]
+ -[SWContainerViewController initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:failureProvider:shareConfigurationProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:]
+ -[SWContainerViewController setHiddenPocketEdges:]
+ -[SWContainerViewController shareConfigurationProvider]
+ -[SWFailureManager .cxx_destruct]
+ -[SWFailureManager block]
+ -[SWFailureManager didReceiveMessage:securityOrigin:]
+ -[SWFailureManager initWithMessageHandlerManager:logger:]
+ -[SWFailureManager logger]
+ -[SWFailureManager onEvent:]
+ -[SWFailureManager reportFailure:]
+ -[SWFailureMessage .cxx_destruct]
+ -[SWFailureMessage contentDomain]
+ -[SWFailureMessage embedName]
+ -[SWFailureMessage errorType]
+ -[SWFailureMessage initWithContentDomain:embedName:errorType:]
+ -[SWFeedConfigurationFactory createFeedConfigurationForViewController:]
+ -[SWLayoutGuide bounds]
+ -[SWLayoutGuide contentFrame]
+ -[SWLayoutGuide contentSafeAreaFrame]
+ -[SWLayoutGuide copyWithZone:]
+ -[SWLayoutGuide description]
+ -[SWLayoutGuide initWithBounds:contentFrame:contentSafeAreaFrame:systemSafeAreaFrame:]
+ -[SWLayoutGuide isEqual:]
+ -[SWLayoutGuide systemSafeAreaFrame]
+ -[SWMutableConfiguration layoutGuide]
+ -[SWMutableConfiguration setLayoutGuide:]
+ -[SWShareConfiguration .cxx_destruct]
+ -[SWShareConfiguration initWithTitle:shareURL:]
+ -[SWShareConfiguration setShareURL:]
+ -[SWShareConfiguration setTitle:]
+ -[SWShareConfiguration shareURL]
+ -[SWShareConfiguration title]
+ -[SWShareConfigurationManager .cxx_destruct]
+ -[SWShareConfigurationManager didReceiveMessage:securityOrigin:]
+ -[SWShareConfigurationManager initWithMessageHandlerManager:logger:]
+ -[SWShareConfigurationManager logger]
+ -[SWShareConfigurationManager setShareConfigurationBlock:]
+ -[SWShareConfigurationManager shareConfigurationBlock]
+ -[SWViewController setHiddenPocketEdges:]
+ _OBJC_CLASS_$_SWFailureManager
+ _OBJC_CLASS_$_SWFailureMessage
+ _OBJC_CLASS_$_SWFeedConfigurationFactory
+ _OBJC_CLASS_$_SWLayoutGuide
+ _OBJC_CLASS_$_SWShareConfiguration
+ _OBJC_CLASS_$_SWShareConfigurationManager
+ _OBJC_IVAR_$_SWConfiguration._layoutGuide
+ _OBJC_IVAR_$_SWContainerConfiguration._layoutGuide
+ _OBJC_IVAR_$_SWContainerViewController._failureProvider
+ _OBJC_IVAR_$_SWContainerViewController._shareConfigurationProvider
+ _OBJC_IVAR_$_SWFailureManager._block
+ _OBJC_IVAR_$_SWFailureManager._logger
+ _OBJC_IVAR_$_SWFailureMessage._contentDomain
+ _OBJC_IVAR_$_SWFailureMessage._embedName
+ _OBJC_IVAR_$_SWFailureMessage._errorType
+ _OBJC_IVAR_$_SWLayoutGuide._bounds
+ _OBJC_IVAR_$_SWLayoutGuide._contentFrame
+ _OBJC_IVAR_$_SWLayoutGuide._contentSafeAreaFrame
+ _OBJC_IVAR_$_SWLayoutGuide._systemSafeAreaFrame
+ _OBJC_IVAR_$_SWMutableConfiguration.layoutGuide
+ _OBJC_IVAR_$_SWShareConfiguration._shareURL
+ _OBJC_IVAR_$_SWShareConfiguration._title
+ _OBJC_IVAR_$_SWShareConfigurationManager._logger
+ _OBJC_IVAR_$_SWShareConfigurationManager._shareConfigurationBlock
+ _OBJC_METACLASS_$_SWFailureManager
+ _OBJC_METACLASS_$_SWFailureMessage
+ _OBJC_METACLASS_$_SWFeedConfigurationFactory
+ _OBJC_METACLASS_$_SWLayoutGuide
+ _OBJC_METACLASS_$_SWShareConfiguration
+ _OBJC_METACLASS_$_SWShareConfigurationManager
+ _SWFailureContentDomainKey
+ _SWFailureEmbedNameKey
+ _SWFailureErrorTypeKey
+ _SWFailureMessageName
+ _SWShareConfigurationMessageName
+ _SWShareConfigurationTitleKey
+ _SWShareConfigurationURLKey
+ __OBJC_$_INSTANCE_METHODS_SWFailureManager
+ __OBJC_$_INSTANCE_METHODS_SWFailureMessage
+ __OBJC_$_INSTANCE_METHODS_SWFeedConfigurationFactory
+ __OBJC_$_INSTANCE_METHODS_SWLayoutGuide
+ __OBJC_$_INSTANCE_METHODS_SWShareConfiguration
+ __OBJC_$_INSTANCE_METHODS_SWShareConfigurationManager
+ __OBJC_$_INSTANCE_VARIABLES_SWFailureManager
+ __OBJC_$_INSTANCE_VARIABLES_SWFailureMessage
+ __OBJC_$_INSTANCE_VARIABLES_SWLayoutGuide
+ __OBJC_$_INSTANCE_VARIABLES_SWShareConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SWShareConfigurationManager
+ __OBJC_$_PROP_LIST_SWFailureManager
+ __OBJC_$_PROP_LIST_SWFailureMessage
+ __OBJC_$_PROP_LIST_SWFailureProvider
+ __OBJC_$_PROP_LIST_SWFeedConfigurationFactory
+ __OBJC_$_PROP_LIST_SWLayoutGuide
+ __OBJC_$_PROP_LIST_SWShareConfiguration
+ __OBJC_$_PROP_LIST_SWShareConfiguration.64
+ __OBJC_$_PROP_LIST_SWShareConfigurationManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SWFailureProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SWFeedConfigurationFactory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SWShareConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SWFailureProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SWFeedConfigurationFactory
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SWShareConfiguration
+ __OBJC_$_PROTOCOL_REFS_SWFailureProvider
+ __OBJC_$_PROTOCOL_REFS_SWFeedConfigurationFactory
+ __OBJC_$_PROTOCOL_REFS_SWShareConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_SWFailureManager
+ __OBJC_CLASS_PROTOCOLS_$_SWFeedConfigurationFactory
+ __OBJC_CLASS_PROTOCOLS_$_SWShareConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_SWShareConfigurationManager
+ __OBJC_CLASS_RO_$_SWFailureManager
+ __OBJC_CLASS_RO_$_SWFailureMessage
+ __OBJC_CLASS_RO_$_SWFeedConfigurationFactory
+ __OBJC_CLASS_RO_$_SWLayoutGuide
+ __OBJC_CLASS_RO_$_SWShareConfiguration
+ __OBJC_CLASS_RO_$_SWShareConfigurationManager
+ __OBJC_LABEL_PROTOCOL_$_SWFailureProvider
+ __OBJC_LABEL_PROTOCOL_$_SWFeedConfigurationFactory
+ __OBJC_LABEL_PROTOCOL_$_SWShareConfiguration
+ __OBJC_LABEL_PROTOCOL_$_SWShareConfigurationProvider
+ __OBJC_METACLASS_RO_$_SWFailureManager
+ __OBJC_METACLASS_RO_$_SWFailureMessage
+ __OBJC_METACLASS_RO_$_SWFeedConfigurationFactory
+ __OBJC_METACLASS_RO_$_SWLayoutGuide
+ __OBJC_METACLASS_RO_$_SWShareConfiguration
+ __OBJC_METACLASS_RO_$_SWShareConfigurationManager
+ __OBJC_PROTOCOL_$_SWFailureProvider
+ __OBJC_PROTOCOL_$_SWFeedConfigurationFactory
+ __OBJC_PROTOCOL_$_SWShareConfiguration
+ __OBJC_PROTOCOL_$_SWShareConfigurationProvider
+ __OBJC_PROTOCOL_REFERENCE_$_SWFailureProvider
+ __OBJC_PROTOCOL_REFERENCE_$_SWFeedConfigurationFactory
+ __OBJC_PROTOCOL_REFERENCE_$_SWShareConfigurationProvider
+ ___36-[SWManagerAssembly loadInRegistry:]_block_invoke_31
+ ___36-[SWManagerAssembly loadInRegistry:]_block_invoke_32
+ ___36-[SWManagerAssembly loadInRegistry:]_block_invoke_33
+ ___37-[SWProviderAssembly loadInRegistry:]_block_invoke_6
+ ___block_descriptor_32_e40_"SWFailureManager"16?0"<TFResolver>"8l
+ ___block_descriptor_32_e43_"<SWFailureProvider>"16?0"<TFResolver>"8l
+ ___block_descriptor_32_e52_"<SWFeedConfigurationFactory>"16?0"<TFResolver>"8l
+ ___block_descriptor_32_e54_"<SWShareConfigurationProvider>"16?0"<TFResolver>"8l
+ ___block_literal_global.101
+ ___block_literal_global.109
+ ___block_literal_global.112
+ ___block_literal_global.13
+ ___block_literal_global.134
+ ___block_literal_global.137
+ ___block_literal_global.150
+ ___block_literal_global.154
+ ___block_literal_global.157
+ ___block_literal_global.161
+ ___block_literal_global.165
+ ___block_literal_global.186
+ ___block_literal_global.212
+ ___block_literal_global.216
+ ___block_literal_global.224
+ ___block_literal_global.232
+ ___block_literal_global.236
+ ___block_literal_global.244
+ ___block_literal_global.260
+ ___block_literal_global.267
+ ___block_literal_global.281
+ ___block_literal_global.284
+ ___block_literal_global.287
+ ___block_literal_global.304
+ ___block_literal_global.312
+ ___block_literal_global.318
+ ___block_literal_global.329
+ ___block_literal_global.88
+ ___block_literal_global.99
+ _objc_msgSend$_setHiddenPocketEdges:
+ _objc_msgSend$contentSafeAreaFrame
+ _objc_msgSend$description
+ _objc_msgSend$initWithContentDomain:embedName:errorType:
+ _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:layoutGuide:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:
+ _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:layoutGuide:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:
+ _objc_msgSend$initWithTitle:shareURL:
+ _objc_msgSend$initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:failureProvider:shareConfigurationProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:
+ _objc_msgSend$layoutGuide
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$reportFailure:
+ _objc_msgSend$setHiddenPocketEdges:
+ _objc_msgSend$setLayoutGuide:
+ _objc_msgSend$setUsesSingleWebProcess:
+ _objc_msgSend$shareConfigurationBlock
+ _objc_msgSend$systemSafeAreaFrame
- -[SWConfiguration canvasSize]
- -[SWConfiguration contentFrame]
- -[SWConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:]
- -[SWConfiguration setCanvasSize:]
- -[SWConfiguration setContentFrame:]
- -[SWContainerConfiguration canvasSize]
- -[SWContainerConfiguration contentFrame]
- -[SWContainerConfiguration initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:]
- -[SWContainerConfiguration setCanvasSize:]
- -[SWContainerConfiguration setContentFrame:]
- -[SWContainerViewController initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:]
- -[SWMutableConfiguration canvasSize]
- -[SWMutableConfiguration contentFrame]
- -[SWMutableConfiguration setCanvasSize:]
- -[SWMutableConfiguration setContentFrame:]
- -[SWWebViewFactory assignRelatedWebViewToConfiguration:]
- _NSStringFromCGSize
- _OBJC_IVAR_$_SWConfiguration._canvasSize
- _OBJC_IVAR_$_SWConfiguration._contentFrame
- _OBJC_IVAR_$_SWContainerConfiguration._canvasSize
- _OBJC_IVAR_$_SWContainerConfiguration._contentFrame
- _OBJC_IVAR_$_SWMutableConfiguration.canvasSize
- _OBJC_IVAR_$_SWMutableConfiguration.contentFrame
- ___block_literal_global.102
- ___block_literal_global.105
- ___block_literal_global.11
- ___block_literal_global.120
- ___block_literal_global.130
- ___block_literal_global.138
- ___block_literal_global.142
- ___block_literal_global.146
- ___block_literal_global.167
- ___block_literal_global.193
- ___block_literal_global.197
- ___block_literal_global.205
- ___block_literal_global.213
- ___block_literal_global.217
- ___block_literal_global.225
- ___block_literal_global.241
- ___block_literal_global.248
- ___block_literal_global.262
- ___block_literal_global.265
- ___block_literal_global.268
- ___block_literal_global.274
- ___block_literal_global.280
- ___block_literal_global.285
- ___block_literal_global.310
- ___block_literal_global.94
- _objc_msgSend$_setRelatedWebView:
- _objc_msgSend$assignRelatedWebViewToConfiguration:
- _objc_msgSend$canvasSize
- _objc_msgSend$firstObject
- _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:
- _objc_msgSend$initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:
- _objc_msgSend$initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:
- _objc_msgSend$setCanvasSize:
- _objc_msgSend$setContentFrame:
CStrings:
+ "; bounds: %@"
+ "; contentSafeAreaFrame: %@"
+ "; layoutGuide: %@"
+ "; systemSafeAreaFrame: %@"
+ "@\"<SWFailureProvider>\""
+ "@\"<SWFailureProvider>\"16@?0@\"<TFResolver>\"8"
+ "@\"<SWFeedConfigurationFactory>\"16@?0@\"<TFResolver>\"8"
+ "@\"<SWShareConfigurationProvider>\""
+ "@\"<SWShareConfigurationProvider>\"16@?0@\"<TFResolver>\"8"
+ "@\"SWFailureManager\"16@?0@\"<TFResolver>\"8"
+ "@\"SWFeedConfiguration\"24@0:8@\"UIViewController\"16"
+ "@\"SWLayoutGuide\""
+ "@100@0:8@16@24@32@40@48@56@64@72@80@88B96"
+ "@104@0:8@16@24@32@40@48@56@64@72@80@88@96"
+ "@120@0:8@16@24@32@40@48@56@64@72@80@88B96@100q108B116"
+ "@144@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48{CGRect={CGPoint=dd}{CGSize=dd}}80{CGRect={CGPoint=dd}{CGSize=dd}}112"
+ "@?<v@?@\"SWFailureMessage\">16@0:8"
+ "Dropping failure message due to missing information: contentDomain=%@, embedName=%@, errorType=%@"
+ "Recording web embed failure: contentDomain=%@, embedName=%@, errorType=%@"
+ "SWFailureManager"
+ "SWFailureMessage"
+ "SWFailureProvider"
+ "SWFeedConfigurationFactory"
+ "SWLayoutGuide"
+ "SWShareConfiguration"
+ "SWShareConfigurationManager"
+ "SWShareConfigurationProvider"
+ "ShareConfiguration: Web content provided share configuration"
+ "T@\"<SWFailureProvider>\",R,N,V_failureProvider"
+ "T@\"<SWShareConfigurationProvider>\",R,N,V_shareConfigurationProvider"
+ "T@\"NSString\",C,N,V_title"
+ "T@\"NSString\",R,C,N,V_contentDomain"
+ "T@\"NSString\",R,C,N,V_embedName"
+ "T@\"NSString\",R,C,N,V_errorType"
+ "T@\"NSURL\",C,N,V_shareURL"
+ "T@\"SWLayoutGuide\",C,N,V_layoutGuide"
+ "T@\"SWLayoutGuide\",C,N,VlayoutGuide"
+ "T@?,C,N,SonEvent:"
+ "T@?,C,N,SonEvent:,V_block"
+ "T@?,C,N,V_shareConfigurationBlock"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_bounds"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_contentFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_contentSafeAreaFrame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_systemSafeAreaFrame"
+ "_bounds"
+ "_contentDomain"
+ "_contentSafeAreaFrame"
+ "_embedName"
+ "_errorType"
+ "_failureProvider"
+ "_layoutGuide"
+ "_setHiddenPocketEdges:"
+ "_shareConfigurationBlock"
+ "_shareConfigurationProvider"
+ "_shareURL"
+ "_systemSafeAreaFrame"
+ "_title"
+ "contentDomain"
+ "contentSafeAreaFrame"
+ "createFeedConfigurationForViewController:"
+ "embedName"
+ "errorType"
+ "failure"
+ "failureProvider"
+ "initWithBounds:contentFrame:contentSafeAreaFrame:systemSafeAreaFrame:"
+ "initWithContentDomain:embedName:errorType:"
+ "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:layoutGuide:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:"
+ "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:layoutGuide:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:"
+ "initWithTitle:shareURL:"
+ "initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:failureProvider:shareConfigurationProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:"
+ "layoutGuide"
+ "objectForKeyedSubscript:"
+ "onEvent:"
+ "reportFailure:"
+ "setHiddenPocketEdges:"
+ "setLayoutGuide:"
+ "setShareConfigurationBlock:"
+ "setShareURL:"
+ "setTitle:"
+ "setUsesSingleWebProcess:"
+ "shareConfiguration"
+ "shareConfigurationBlock"
+ "shareConfigurationProvider"
+ "shareURL"
+ "systemSafeAreaFrame"
+ "title"
+ "v24@0:8@?<v@?@\"SWFailureMessage\">16"
+ "v32@0:8@\"WKWebView\"16@\"UIInputSuggestion\"24"
+ "webView:insertInputSuggestion:"
- "; canvasSize: %@"
- "@140@0:8@16@24@32@40{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64@96@104@112@120@128B136"
- "@160@0:8@16@24@32@40{CGSize=dd}48{CGRect={CGPoint=dd}{CGSize=dd}}64@96@104@112@120@128B136@140q148B156"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_contentFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,VcontentFrame"
- "T{CGSize=dd},N,V_canvasSize"
- "T{CGSize=dd},N,VcanvasSize"
- "_canvasSize"
- "_setRelatedWebView:"
- "assignRelatedWebViewToConfiguration:"
- "firstObject"
- "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:"
- "initWithStoreFront:locale:contentEnvironment:contentSizeCategory:canvasSize:contentFrame:dataSources:location:sourceURL:activePictureInPictureURL:feedConfiguration:supportsLiveActivities:keyboardConfiguration:networkStatus:isTransitioning:"
- "initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:"
- "setCanvasSize:"
- "setContentFrame:"
- "v32@0:8{CGSize=dd}16"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"

```
