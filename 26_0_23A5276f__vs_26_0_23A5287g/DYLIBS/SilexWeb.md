## SilexWeb

> `/System/Library/PrivateFrameworks/SilexWeb.framework/SilexWeb`

```diff

-5722.0.0.0.0
-  __TEXT.__text: 0x16648
+5726.2.0.0.0
+  __TEXT.__text: 0x17bfc
   __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0x304c
+  __TEXT.__objc_methlist: 0x3304
   __TEXT.__const: 0x68
-  __TEXT.__cstring: 0x1bb3
-  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__cstring: 0x1c57
+  __TEXT.__gcc_except_tab: 0x164
   __TEXT.__oslogstring: 0xe
-  __TEXT.__unwind_info: 0x7e8
-  __TEXT.__objc_classname: 0x861
-  __TEXT.__objc_methname: 0x652d
-  __TEXT.__objc_methtype: 0x1afa
-  __TEXT.__objc_stubs: 0x40a0
-  __DATA_CONST.__got: 0x448
-  __DATA_CONST.__const: 0x978
-  __DATA_CONST.__objc_classlist: 0x2a8
-  __DATA_CONST.__objc_protolist: 0x1d8
+  __TEXT.__unwind_info: 0x840
+  __TEXT.__objc_classname: 0x919
+  __TEXT.__objc_methname: 0x6a31
+  __TEXT.__objc_methtype: 0x1c17
+  __TEXT.__objc_stubs: 0x42a0
+  __DATA_CONST.__got: 0x480
+  __DATA_CONST.__const: 0xa18
+  __DATA_CONST.__objc_classlist: 0x2e0
+  __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1488
+  __DATA_CONST.__objc_selrefs: 0x1560
   __DATA_CONST.__objc_protorefs: 0x128
-  __DATA_CONST.__objc_superrefs: 0x228
+  __DATA_CONST.__objc_superrefs: 0x260
   __AUTH_CONST.__auth_got: 0x248
   __AUTH_CONST.__const: 0x840
-  __AUTH_CONST.__cfstring: 0x17c0
-  __AUTH_CONST.__objc_const: 0x8c98
-  __AUTH.__objc_data: 0x3c0
-  __DATA.__objc_ivar: 0x3e8
-  __DATA.__data: 0x1628
+  __AUTH_CONST.__cfstring: 0x1920
+  __AUTH_CONST.__objc_const: 0x9678
+  __AUTH.__objc_data: 0x5f0
+  __DATA.__objc_ivar: 0x438
+  __DATA.__data: 0x16e8
   __DATA_DIRTY.__objc_data: 0x16d0
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x78
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/UIAccessibility.framework/UIAccessibility
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6E2CD8A3-7FB4-37EF-8AE7-76FF302A2BC9
-  Functions: 837
-  Symbols:   3769
-  CStrings:  1806
+  UUID: 20A285A2-6DFB-3393-BAAB-CF964CE60D98
+  Functions: 888
+  Symbols:   3980
+  CStrings:  1907
 
Symbols:
+ +[SWInspectionScript executableSource]
+ -[SWContainerViewController URLSchemeHandlerManager]
+ -[SWContainerViewController initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:failureProvider:navigationBarConfigurationProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:]
+ -[SWContainerViewController loadLocalDatastore:options:completion:]
+ -[SWContainerViewController navigationBarConfigurationProvider]
+ -[SWDatastoreManager updateDatastore:originatingSession:options:completion:]
+ -[SWDatastoreSynchronizationManager synchronizeDatastore:from:previousDatastore:originatingSession:queueable:completion:]
+ -[SWDatastoreUpdateScript initWithDatastore:oldDatastore:originatingSession:queueable:]
+ -[SWInspection .cxx_destruct]
+ -[SWInspection accessibilityElements]
+ -[SWInspection initWithObject:]
+ -[SWInspection links]
+ -[SWInspectionAccessibilityElement .cxx_destruct]
+ -[SWInspectionAccessibilityElement frame]
+ -[SWInspectionAccessibilityElement initWithObject:]
+ -[SWInspectionAccessibilityElement setFrame:]
+ -[SWInspectionAccessibilityElement type]
+ -[SWInspectionAccessibilityElement value]
+ -[SWInspectionLink .cxx_destruct]
+ -[SWInspectionLink frame]
+ -[SWInspectionLink href]
+ -[SWInspectionLink initWithObject:]
+ -[SWInspectionLink label]
+ -[SWInspectionScript executableScript]
+ -[SWInspectionScript identifier]
+ -[SWInspectionScript init]
+ -[SWInspectionScript queueable]
+ -[SWLocalDatastoreUpdateScript initWithDatastore:oldDatastore:originatingSession:queueable:]
+ -[SWNavigationBarConfiguration .cxx_destruct]
+ -[SWNavigationBarConfiguration initWithTitle:shareConfiguration:]
+ -[SWNavigationBarConfiguration setShareConfiguration:]
+ -[SWNavigationBarConfiguration setTitle:]
+ -[SWNavigationBarConfiguration shareConfiguration]
+ -[SWNavigationBarConfiguration title]
+ -[SWNavigationBarConfigurationManager .cxx_destruct]
+ -[SWNavigationBarConfigurationManager didReceiveMessage:securityOrigin:]
+ -[SWNavigationBarConfigurationManager initWithMessageHandlerManager:logger:]
+ -[SWNavigationBarConfigurationManager logger]
+ -[SWNavigationBarConfigurationManager navigationBarConfigurationBlock]
+ -[SWNavigationBarConfigurationManager setNavigationBarConfigurationBlock:]
+ -[SWNavigationBarConfigurationManager shareItemsFromDictionary:]
+ -[SWPresentationManager inspectionWithCompletion:]
+ -[SWPresentationManager reset]
+ -[SWScriptsManager executeScriptWithReturnObject:completion:]
+ -[SWShareConfiguration initWithTitle:shareItems:]
+ -[SWShareConfiguration setShareItems:]
+ -[SWShareConfiguration shareItems]
+ -[SWURLSchemeHandlerManager registerSession:]
+ -[SWURLSchemeHandlerManager session]
+ -[SWURLSchemeHandlerManager setSession:]
+ -[SWURLSchemeHandlerSession .cxx_destruct]
+ -[SWURLSchemeHandlerSession endCallbackBlock]
+ -[SWURLSchemeHandlerSession endSessionForHandler:withTask:]
+ -[SWURLSchemeHandlerSession identifier]
+ -[SWURLSchemeHandlerSession initWithStartCallback:endCallback:]
+ -[SWURLSchemeHandlerSession isEqual:]
+ -[SWURLSchemeHandlerSession startCallbackBlock]
+ -[SWURLSchemeHandlerSession startSessionForHandler:withTask:]
+ -[SWURLSchemeHandlerSession trackingTasks]
+ -[SWURLShareItem .cxx_destruct]
+ -[SWURLShareItem initWithURL:]
+ -[SWURLShareItem kind]
+ -[SWURLShareItem setUrl:]
+ -[SWURLShareItem url]
+ -[SWViewController loadLocalDatastore:options:completion:]
+ GCC_except_table3
+ _OBJC_CLASS_$_SWInspection
+ _OBJC_CLASS_$_SWInspectionAccessibilityElement
+ _OBJC_CLASS_$_SWInspectionLink
+ _OBJC_CLASS_$_SWInspectionScript
+ _OBJC_CLASS_$_SWNavigationBarConfiguration
+ _OBJC_CLASS_$_SWNavigationBarConfigurationManager
+ _OBJC_CLASS_$_SWURLSchemeHandlerSession
+ _OBJC_CLASS_$_SWURLShareItem
+ _OBJC_IVAR_$_SWContainerViewController._URLSchemeHandlerManager
+ _OBJC_IVAR_$_SWContainerViewController._navigationBarConfigurationProvider
+ _OBJC_IVAR_$_SWDatastoreUpdateScript._queueable
+ _OBJC_IVAR_$_SWInspection._accessibilityElements
+ _OBJC_IVAR_$_SWInspection._links
+ _OBJC_IVAR_$_SWInspectionAccessibilityElement._frame
+ _OBJC_IVAR_$_SWInspectionAccessibilityElement._type
+ _OBJC_IVAR_$_SWInspectionAccessibilityElement._value
+ _OBJC_IVAR_$_SWInspectionLink._frame
+ _OBJC_IVAR_$_SWInspectionLink._href
+ _OBJC_IVAR_$_SWInspectionLink._label
+ _OBJC_IVAR_$_SWLocalDatastoreUpdateScript._queueable
+ _OBJC_IVAR_$_SWNavigationBarConfiguration._shareConfiguration
+ _OBJC_IVAR_$_SWNavigationBarConfiguration._title
+ _OBJC_IVAR_$_SWNavigationBarConfigurationManager._logger
+ _OBJC_IVAR_$_SWNavigationBarConfigurationManager._navigationBarConfigurationBlock
+ _OBJC_IVAR_$_SWShareConfiguration._shareItems
+ _OBJC_IVAR_$_SWURLSchemeHandlerManager._session
+ _OBJC_IVAR_$_SWURLSchemeHandlerSession._endCallbackBlock
+ _OBJC_IVAR_$_SWURLSchemeHandlerSession._identifier
+ _OBJC_IVAR_$_SWURLSchemeHandlerSession._startCallbackBlock
+ _OBJC_IVAR_$_SWURLSchemeHandlerSession._trackingTasks
+ _OBJC_IVAR_$_SWURLShareItem._kind
+ _OBJC_IVAR_$_SWURLShareItem._url
+ _OBJC_METACLASS_$_SWInspection
+ _OBJC_METACLASS_$_SWInspectionAccessibilityElement
+ _OBJC_METACLASS_$_SWInspectionLink
+ _OBJC_METACLASS_$_SWInspectionScript
+ _OBJC_METACLASS_$_SWNavigationBarConfiguration
+ _OBJC_METACLASS_$_SWNavigationBarConfigurationManager
+ _OBJC_METACLASS_$_SWURLSchemeHandlerSession
+ _OBJC_METACLASS_$_SWURLShareItem
+ _SWInspectionFrameFromDictionary
+ _SWNavigationBarConfigurationMessageName
+ _SWNavigationBarTitleKey
+ _SWShareConfigurationKey
+ _SWShareConfigurationShareItemKindKey
+ _SWShareConfigurationShareItemKindURL
+ _SWShareConfigurationShareItemValueKey
+ _SWShareConfigurationShareItems
+ __OBJC_$_CLASS_METHODS_SWInspectionScript
+ __OBJC_$_INSTANCE_METHODS_SWInspection
+ __OBJC_$_INSTANCE_METHODS_SWInspectionAccessibilityElement
+ __OBJC_$_INSTANCE_METHODS_SWInspectionLink
+ __OBJC_$_INSTANCE_METHODS_SWInspectionScript
+ __OBJC_$_INSTANCE_METHODS_SWNavigationBarConfiguration
+ __OBJC_$_INSTANCE_METHODS_SWNavigationBarConfigurationManager
+ __OBJC_$_INSTANCE_METHODS_SWURLSchemeHandlerSession
+ __OBJC_$_INSTANCE_METHODS_SWURLShareItem
+ __OBJC_$_INSTANCE_VARIABLES_SWInspection
+ __OBJC_$_INSTANCE_VARIABLES_SWInspectionAccessibilityElement
+ __OBJC_$_INSTANCE_VARIABLES_SWInspectionLink
+ __OBJC_$_INSTANCE_VARIABLES_SWNavigationBarConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_SWNavigationBarConfigurationManager
+ __OBJC_$_INSTANCE_VARIABLES_SWURLSchemeHandlerSession
+ __OBJC_$_INSTANCE_VARIABLES_SWURLShareItem
+ __OBJC_$_PROP_LIST_SWDatastoreManager.90
+ __OBJC_$_PROP_LIST_SWInspection
+ __OBJC_$_PROP_LIST_SWInspectionAccessibilityElement
+ __OBJC_$_PROP_LIST_SWInspectionLink
+ __OBJC_$_PROP_LIST_SWInspectionScript
+ __OBJC_$_PROP_LIST_SWNavigationBarConfiguration
+ __OBJC_$_PROP_LIST_SWNavigationBarConfiguration.64
+ __OBJC_$_PROP_LIST_SWNavigationBarConfigurationManager
+ __OBJC_$_PROP_LIST_SWPresentationManager.124
+ __OBJC_$_PROP_LIST_SWShareItem
+ __OBJC_$_PROP_LIST_SWURLSchemeHandlerSession
+ __OBJC_$_PROP_LIST_SWURLShareItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SWNavigationBarConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SWShareItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SWNavigationBarConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SWShareItem
+ __OBJC_$_PROTOCOL_REFS_SWNavigationBarConfiguration
+ __OBJC_$_PROTOCOL_REFS_SWShareItem
+ __OBJC_CLASS_PROTOCOLS_$_SWInspectionScript
+ __OBJC_CLASS_PROTOCOLS_$_SWNavigationBarConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_SWNavigationBarConfigurationManager
+ __OBJC_CLASS_PROTOCOLS_$_SWURLShareItem
+ __OBJC_CLASS_RO_$_SWInspection
+ __OBJC_CLASS_RO_$_SWInspectionAccessibilityElement
+ __OBJC_CLASS_RO_$_SWInspectionLink
+ __OBJC_CLASS_RO_$_SWInspectionScript
+ __OBJC_CLASS_RO_$_SWNavigationBarConfiguration
+ __OBJC_CLASS_RO_$_SWNavigationBarConfigurationManager
+ __OBJC_CLASS_RO_$_SWURLSchemeHandlerSession
+ __OBJC_CLASS_RO_$_SWURLShareItem
+ __OBJC_LABEL_PROTOCOL_$_SWNavigationBarConfiguration
+ __OBJC_LABEL_PROTOCOL_$_SWNavigationBarConfigurationProvider
+ __OBJC_LABEL_PROTOCOL_$_SWShareItem
+ __OBJC_METACLASS_RO_$_SWInspection
+ __OBJC_METACLASS_RO_$_SWInspectionAccessibilityElement
+ __OBJC_METACLASS_RO_$_SWInspectionLink
+ __OBJC_METACLASS_RO_$_SWInspectionScript
+ __OBJC_METACLASS_RO_$_SWNavigationBarConfiguration
+ __OBJC_METACLASS_RO_$_SWNavigationBarConfigurationManager
+ __OBJC_METACLASS_RO_$_SWURLSchemeHandlerSession
+ __OBJC_METACLASS_RO_$_SWURLShareItem
+ __OBJC_PROTOCOL_$_SWNavigationBarConfiguration
+ __OBJC_PROTOCOL_$_SWNavigationBarConfigurationProvider
+ __OBJC_PROTOCOL_$_SWShareItem
+ __OBJC_PROTOCOL_REFERENCE_$_SWNavigationBarConfigurationProvider
+ ___38+[SWInspectionScript executableSource]_block_invoke
+ ___50-[SWPresentationManager inspectionWithCompletion:]_block_invoke
+ ___55-[SWSnapshotManager takeSnapshotWithCompletionHandler:]_block_invoke_2
+ ___61-[SWScriptsManager executeScriptWithReturnObject:completion:]_block_invoke
+ ___61-[SWScriptsManager executeScriptWithReturnObject:completion:]_block_invoke_2
+ ___block_descriptor_32_e62_"<SWNavigationBarConfigurationProvider>"16?0"<TFResolver>"8l
+ ___block_descriptor_40_e8_32bs_e8_v16?08ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40w_e27_v16?0"<WKURLSchemeTask>"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.103
+ ___block_literal_global.111
+ ___block_literal_global.114
+ ___block_literal_global.129
+ ___block_literal_global.136
+ ___block_literal_global.139
+ ___block_literal_global.152
+ ___block_literal_global.156
+ ___block_literal_global.159
+ ___block_literal_global.163
+ ___block_literal_global.167
+ ___block_literal_global.188
+ ___block_literal_global.220
+ ___block_literal_global.228
+ ___block_literal_global.240
+ ___block_literal_global.248
+ ___block_literal_global.264
+ ___block_literal_global.271
+ ___block_literal_global.285
+ ___block_literal_global.288
+ ___block_literal_global.291
+ ___block_literal_global.297
+ ___block_literal_global.305
+ ___block_literal_global.310
+ ___block_literal_global.324
+ ___block_literal_global.335
+ ___block_literal_global.64
+ ___block_literal_global.67
+ ___block_literal_global.74
+ ___block_literal_global.90
+ _objc_msgSend$URLSchemeHandlerManager
+ _objc_msgSend$_setOverrideContentSecurityPolicy:
+ _objc_msgSend$_setUseSystemAppearance:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$endCallbackBlock
+ _objc_msgSend$endSessionForHandler:withTask:
+ _objc_msgSend$executeScriptWithReturnObject:completion:
+ _objc_msgSend$initWithDatastore:oldDatastore:originatingSession:queueable:
+ _objc_msgSend$initWithObject:
+ _objc_msgSend$initWithTitle:shareConfiguration:
+ _objc_msgSend$initWithTitle:shareItems:
+ _objc_msgSend$initWithURL:
+ _objc_msgSend$initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:failureProvider:navigationBarConfigurationProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:
+ _objc_msgSend$loadLocalDatastore:options:completion:
+ _objc_msgSend$navigationBarConfigurationBlock
+ _objc_msgSend$setSession:
+ _objc_msgSend$shareItemsFromDictionary:
+ _objc_msgSend$startCallbackBlock
+ _objc_msgSend$startSessionForHandler:withTask:
+ _objc_msgSend$synchronizeDatastore:from:previousDatastore:originatingSession:queueable:completion:
+ _objc_msgSend$trackingTasks
+ _objc_msgSend$updateDatastore:originatingSession:options:completion:
+ _objc_retain_x7
- -[SWContainerViewController initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:failureProvider:shareConfigurationProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:]
- -[SWContainerViewController loadLocalDatastore:forceUpdate:completion:]
- -[SWContainerViewController shareConfigurationProvider]
- -[SWDatastoreManager updateDatastore:originatingSession:completion:]
- -[SWDatastoreManager updateDatastore:originatingSession:forceUpdate:completion:]
- -[SWDatastoreSynchronizationManager synchronizeDatastore:from:previousDatastore:originatingSession:completion:]
- -[SWDatastoreUpdateScript initWithDatastore:oldDatastore:originatingSession:]
- -[SWLocalDatastoreUpdateScript initWithDatastore:oldDatastore:originatingSession:]
- -[SWPresentationManager prepareForLegacyResize]
- -[SWShareConfiguration initWithTitle:shareURL:]
- -[SWShareConfiguration setShareURL:]
- -[SWShareConfiguration shareURL]
- -[SWShareConfigurationManager .cxx_destruct]
- -[SWShareConfigurationManager didReceiveMessage:securityOrigin:]
- -[SWShareConfigurationManager initWithMessageHandlerManager:logger:]
- -[SWShareConfigurationManager logger]
- -[SWShareConfigurationManager setShareConfigurationBlock:]
- -[SWShareConfigurationManager shareConfigurationBlock]
- -[SWViewController loadLocalDatastore:forceUpdate:completion:]
- _OBJC_CLASS_$_SWShareConfigurationManager
- _OBJC_IVAR_$_SWContainerViewController._shareConfigurationProvider
- _OBJC_IVAR_$_SWShareConfiguration._shareURL
- _OBJC_IVAR_$_SWShareConfigurationManager._logger
- _OBJC_IVAR_$_SWShareConfigurationManager._shareConfigurationBlock
- _OBJC_METACLASS_$_SWShareConfigurationManager
- _SWShareConfigurationMessageName
- _SWShareConfigurationURLKey
- __OBJC_$_INSTANCE_METHODS_SWShareConfigurationManager
- __OBJC_$_INSTANCE_VARIABLES_SWShareConfigurationManager
- __OBJC_$_PROP_LIST_SWDatastoreManager.92
- __OBJC_$_PROP_LIST_SWPresentationManager.119
- __OBJC_$_PROP_LIST_SWShareConfigurationManager
- __OBJC_CLASS_PROTOCOLS_$_SWShareConfigurationManager
- __OBJC_CLASS_RO_$_SWShareConfigurationManager
- __OBJC_LABEL_PROTOCOL_$_SWShareConfigurationProvider
- __OBJC_METACLASS_RO_$_SWShareConfigurationManager
- __OBJC_PROTOCOL_$_SWShareConfigurationProvider
- __OBJC_PROTOCOL_REFERENCE_$_SWShareConfigurationProvider
- ___45-[SWScriptsManager executeScript:completion:]_block_invoke_2
- ___block_descriptor_32_e54_"<SWShareConfigurationProvider>"16?0"<TFResolver>"8l
- ___block_descriptor_40_e8_32w_e27_v16?0"<WKURLSchemeTask>"8lw32l8
- ___block_literal_global.101
- ___block_literal_global.109
- ___block_literal_global.112
- ___block_literal_global.127
- ___block_literal_global.134
- ___block_literal_global.137
- ___block_literal_global.150
- ___block_literal_global.154
- ___block_literal_global.157
- ___block_literal_global.161
- ___block_literal_global.165
- ___block_literal_global.186
- ___block_literal_global.212
- ___block_literal_global.224
- ___block_literal_global.232
- ___block_literal_global.244
- ___block_literal_global.260
- ___block_literal_global.267
- ___block_literal_global.281
- ___block_literal_global.284
- ___block_literal_global.287
- ___block_literal_global.293
- ___block_literal_global.299
- ___block_literal_global.304
- ___block_literal_global.312
- ___block_literal_global.329
- ___block_literal_global.65
- ___block_literal_global.72
- ___block_literal_global.88
- _objc_msgSend$initWithDatastore:oldDatastore:originatingSession:
- _objc_msgSend$initWithTitle:shareURL:
- _objc_msgSend$initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:failureProvider:shareConfigurationProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:
- _objc_msgSend$loadLocalDatastore:forceUpdate:completion:
- _objc_msgSend$shareConfigurationBlock
- _objc_msgSend$synchronizeDatastore:from:previousDatastore:originatingSession:completion:
- _objc_msgSend$updateDatastore:originatingSession:forceUpdate:completion:
- _objc_retain_x6
CStrings:
+ "@\"<SWNavigationBarConfigurationProvider>\""
+ "@\"<SWNavigationBarConfigurationProvider>\"16@?0@\"<TFResolver>\"8"
+ "@\"<SWShareConfiguration>\""
+ "@\"<SWShareConfiguration>\"16@0:8"
+ "@\"SWURLSchemeHandlerSession\""
+ "@32@0:8@?16@?24"
+ "@44@0:8@16@24@32B40"
+ "SWInspection"
+ "SWInspectionAccessibilityElement"
+ "SWInspectionLink"
+ "SWInspectionScript"
+ "SWNavigationBarConfiguration"
+ "SWNavigationBarConfigurationManager"
+ "SWNavigationBarConfigurationProvider"
+ "SWShareItem"
+ "SWURLSchemeHandlerSession"
+ "SWURLShareItem"
+ "T@\"<SWNavigationBarConfigurationProvider>\",R,N,V_navigationBarConfigurationProvider"
+ "T@\"<SWShareConfiguration>\",&,N,V_shareConfiguration"
+ "T@\"<SWShareConfiguration>\",R,N"
+ "T@\"NSArray\",C,N,V_shareItems"
+ "T@\"NSArray\",R,N"
+ "T@\"NSArray\",R,N,V_accessibilityElements"
+ "T@\"NSArray\",R,N,V_links"
+ "T@\"NSMutableSet\",R,N,V_trackingTasks"
+ "T@\"NSString\",R,C,N,V_identifier"
+ "T@\"NSString\",R,C,N,V_label"
+ "T@\"NSString\",R,C,N,V_type"
+ "T@\"NSString\",R,C,N,V_value"
+ "T@\"NSURL\",C,N,V_url"
+ "T@\"NSURL\",R,C,N,V_href"
+ "T@\"SWURLSchemeHandlerSession\",&,N,V_session"
+ "T@?,C,N,V_navigationBarConfigurationBlock"
+ "T@?,R,N,V_endCallbackBlock"
+ "T@?,R,N,V_startCallbackBlock"
+ "TB,R,N,V_queueable"
+ "Tq,R,N"
+ "Tq,R,N,V_kind"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_frame"
+ "_accessibilityElements"
+ "_endCallbackBlock"
+ "_frame"
+ "_href"
+ "_kind"
+ "_label"
+ "_links"
+ "_navigationBarConfigurationBlock"
+ "_navigationBarConfigurationProvider"
+ "_queueable"
+ "_setOverrideContentSecurityPolicy:"
+ "_setUseSystemAppearance:"
+ "_shareConfiguration"
+ "_shareItems"
+ "_startCallbackBlock"
+ "_trackingTasks"
+ "_url"
+ "_value"
+ "arrayWithArray:"
+ "containsObject:"
+ "endCallbackBlock"
+ "endSessionForHandler:withTask:"
+ "executeScriptWithReturnObject:completion:"
+ "frame"
+ "href"
+ "img-src 'self' https: news-datastore-assets: *"
+ "initWithDatastore:oldDatastore:originatingSession:queueable:"
+ "initWithObject:"
+ "initWithStartCallback:endCallback:"
+ "initWithTitle:shareConfiguration:"
+ "initWithTitle:shareItems:"
+ "initWithURL:"
+ "initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:failureProvider:navigationBarConfigurationProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:"
+ "inspection"
+ "inspectionWithCompletion:"
+ "items"
+ "kind"
+ "label"
+ "links"
+ "loadLocalDatastore:options:completion:"
+ "navigationBarConfiguration"
+ "navigationBarConfigurationBlock"
+ "navigationBarConfigurationProvider"
+ "registerSession:"
+ "reset"
+ "setNavigationBarConfigurationBlock:"
+ "setSession:"
+ "setShareConfiguration:"
+ "setShareItems:"
+ "setUrl:"
+ "shareItems"
+ "shareItemsFromDictionary:"
+ "startCallbackBlock"
+ "startSessionForHandler:withTask:"
+ "synchronizeDatastore:from:previousDatastore:originatingSession:queueable:completion:"
+ "trackingTasks"
+ "updateDatastore:originatingSession:options:completion:"
+ "v16@?0@8"
+ "v24@0:8@\"SWURLSchemeHandlerSession\"16"
+ "v24@0:8@?<v@?@\"SWInspection\">16"
+ "v32@0:8@\"<SWScript>\"16@?<v@?@>24"
+ "v40@0:8@16Q24@?32"
+ "v48@0:8@\"SWDatastore\"16@\"<SWSession>\"24Q32@?<v@?>40"
+ "v48@0:8@16@24Q32@?40"
+ "v60@0:8@\"SWDatastore\"16@\"<SWDatastoreManager>\"24@\"SWDatastore\"32@\"<SWSession>\"40B48@?<v@?>52"
+ "v60@0:8@16@24@32@40B48@?52"
+ "value"
- "@\"<SWShareConfigurationProvider>\""
- "@\"<SWShareConfigurationProvider>\"16@?0@\"<TFResolver>\"8"
- "SWShareConfigurationManager"
- "SWShareConfigurationProvider"
- "T@\"<SWShareConfigurationProvider>\",R,N,V_shareConfigurationProvider"
- "T@\"NSURL\",C,N,V_shareURL"
- "T@?,C,N,V_shareConfigurationBlock"
- "_shareConfigurationBlock"
- "_shareConfigurationProvider"
- "_shareURL"
- "initWithDatastore:oldDatastore:originatingSession:"
- "initWithTitle:shareURL:"
- "initWithWebContentViewController:actionProvider:interactionProvider:errorProvider:failureProvider:shareConfigurationProvider:configurationManager:presentationManager:scaleManager:snapshotManager:preferredSizeManager:"
- "loadLocalDatastore:forceUpdate:completion:"
- "prepareForLegacyResize"
- "setShareConfigurationBlock:"
- "setShareURL:"
- "shareConfigurationBlock"
- "shareConfigurationProvider"
- "shareURL"
- "synchronizeDatastore:from:previousDatastore:originatingSession:completion:"
- "updateDatastore:originatingSession:completion:"
- "updateDatastore:originatingSession:forceUpdate:completion:"
- "v36@0:8@16B24@?28"
- "v44@0:8@\"SWDatastore\"16@\"<SWSession>\"24B32@?<v@?>36"
- "v56@0:8@\"SWDatastore\"16@\"<SWDatastoreManager>\"24@\"SWDatastore\"32@\"<SWSession>\"40@?<v@?>48"

```
