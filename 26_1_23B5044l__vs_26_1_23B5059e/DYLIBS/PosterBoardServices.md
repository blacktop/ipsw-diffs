## PosterBoardServices

> `/System/Library/PrivateFrameworks/PosterBoardServices.framework/PosterBoardServices`

```diff

-296.100.0.0.0
-  __TEXT.__text: 0x48308
-  __TEXT.__auth_stubs: 0xa60
-  __TEXT.__objc_methlist: 0x3944
-  __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x4588
-  __TEXT.__gcc_except_tab: 0x788
-  __TEXT.__oslogstring: 0x282b
-  __TEXT.__dlopen_cstrs: 0x203
-  __TEXT.__unwind_info: 0xf98
-  __TEXT.__objc_classname: 0x860
-  __TEXT.__objc_methname: 0x9e8e
-  __TEXT.__objc_methtype: 0x1a1a
-  __TEXT.__objc_stubs: 0x5da0
-  __DATA_CONST.__got: 0x450
-  __DATA_CONST.__const: 0x1140
-  __DATA_CONST.__objc_classlist: 0x208
+302.100.0.0.0
+  __TEXT.__text: 0x4a564
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_methlist: 0x3b24
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x47a9
+  __TEXT.__gcc_except_tab: 0x90c
+  __TEXT.__oslogstring: 0x2867
+  __TEXT.__dlopen_cstrs: 0x244
+  __TEXT.__unwind_info: 0x1028
+  __TEXT.__objc_classname: 0x87f
+  __TEXT.__objc_methname: 0xa30a
+  __TEXT.__objc_methtype: 0x1aca
+  __TEXT.__objc_stubs: 0x5fe0
+  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__const: 0x11c8
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1de8
+  __DATA_CONST.__objc_selrefs: 0x1ec8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1e0
-  __AUTH_CONST.__auth_got: 0x540
+  __DATA_CONST.__objc_superrefs: 0x1f0
+  __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x33c0
-  __AUTH_CONST.__objc_const: 0xb778
+  __AUTH_CONST.__cfstring: 0x36c0
+  __AUTH_CONST.__objc_const: 0xbfb8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x3ec
+  __AUTH.__objc_data: 0xaf0
+  __DATA.__objc_ivar: 0x418
   __DATA.__data: 0x5c0
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x98
   __DATA_DIRTY.__objc_data: 0xa00
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 53745497-19DE-314F-97E2-769741B8E80F
-  Functions: 1648
-  Symbols:   5846
-  CStrings:  2799
+  UUID: 3E7DC08C-A40C-3626-A1AA-EF4E034A9040
+  Functions: 1699
+  Symbols:   6031
+  CStrings:  2909
 
Symbols:
+ +[PRSDisplayInfo supportsBSXPCSecureCoding]
+ +[PRSDisplayInfo supportsSecureCoding]
+ +[PRSHostContext hostContextWithCompletion:]
+ +[PRSHostContext new]
+ +[PRSHostContext supportsBSXPCSecureCoding]
+ +[PRSHostContext supportsSecureCoding]
+ -[PRSDisplayInfo .cxx_destruct]
+ -[PRSDisplayInfo bounds]
+ -[PRSDisplayInfo description]
+ -[PRSDisplayInfo encodeWithBSXPCCoder:]
+ -[PRSDisplayInfo encodeWithCoder:]
+ -[PRSDisplayInfo hardwareIdentifier]
+ -[PRSDisplayInfo hash]
+ -[PRSDisplayInfo initWithBSXPCCoder:]
+ -[PRSDisplayInfo initWithCoder:]
+ -[PRSDisplayInfo initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:]
+ -[PRSDisplayInfo initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:].cold.1
+ -[PRSDisplayInfo interfaceOrientation]
+ -[PRSDisplayInfo isEqual:]
+ -[PRSDisplayInfo isMainDisplay]
+ -[PRSDisplayInfo pointScale]
+ -[PRSHostContext .cxx_destruct]
+ -[PRSHostContext auditToken]
+ -[PRSHostContext connectedDisplays]
+ -[PRSHostContext description]
+ -[PRSHostContext encodeWithBSXPCCoder:]
+ -[PRSHostContext encodeWithCoder:]
+ -[PRSHostContext hash]
+ -[PRSHostContext hostApplicationIdentifier]
+ -[PRSHostContext initWithAuditToken:primaryDisplay:connectedDisplays:hostApplicationIdentifier:userInterfaceStyle:]
+ -[PRSHostContext initWithBSXPCCoder:]
+ -[PRSHostContext initWithCoder:]
+ -[PRSHostContext init]
+ -[PRSHostContext isEqual:]
+ -[PRSHostContext primaryDisplayInfo]
+ -[PRSHostContext userInterfaceStyle]
+ -[PRSPosterSnapshotRequest hostContext]
+ -[PRSPosterSnapshotRequest setHostContext:]
+ -[PRSServer overnightUpdate:completion:]
+ -[PRSServer prewarm:completion:]
+ _BSDispatchMain
+ _BSDispatchQueueAssertMain
+ _BSInterfaceOrientationIsValid
+ _BSRectFromValue
+ _BSValueWithRect
+ _CGRectEqualToRect
+ _OBJC_CLASS_$_BSAuditToken
+ _OBJC_CLASS_$_NSValue
+ _OBJC_CLASS_$_PRSDisplayInfo
+ _OBJC_CLASS_$_PRSHostContext
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_PRSDisplayInfo._bounds
+ _OBJC_IVAR_$_PRSDisplayInfo._hardwareIdentifier
+ _OBJC_IVAR_$_PRSDisplayInfo._interfaceOrientation
+ _OBJC_IVAR_$_PRSDisplayInfo._isMainDisplay
+ _OBJC_IVAR_$_PRSDisplayInfo._pointScale
+ _OBJC_IVAR_$_PRSHostContext._auditToken
+ _OBJC_IVAR_$_PRSHostContext._connectedDisplays
+ _OBJC_IVAR_$_PRSHostContext._hostApplicationIdentifier
+ _OBJC_IVAR_$_PRSHostContext._primaryDisplayInfo
+ _OBJC_IVAR_$_PRSHostContext._userInterfaceStyle
+ _OBJC_IVAR_$_PRSPosterSnapshotRequest._hostContext
+ _OBJC_METACLASS_$_PRSDisplayInfo
+ _OBJC_METACLASS_$_PRSHostContext
+ _UIKitLibrary
+ _UIKitLibrary.cold.1
+ __OBJC_$_CLASS_METHODS_PRSDisplayInfo
+ __OBJC_$_CLASS_METHODS_PRSHostContext
+ __OBJC_$_CLASS_PROP_LIST_PRSDisplayInfo
+ __OBJC_$_CLASS_PROP_LIST_PRSHostContext
+ __OBJC_$_INSTANCE_METHODS_PRSDisplayInfo
+ __OBJC_$_INSTANCE_METHODS_PRSHostContext
+ __OBJC_$_INSTANCE_VARIABLES_PRSDisplayInfo
+ __OBJC_$_INSTANCE_VARIABLES_PRSHostContext
+ __OBJC_$_PROP_LIST_PRSDisplayInfo
+ __OBJC_$_PROP_LIST_PRSHostContext
+ __OBJC_CLASS_PROTOCOLS_$_PRSDisplayInfo
+ __OBJC_CLASS_PROTOCOLS_$_PRSHostContext
+ __OBJC_CLASS_RO_$_PRSDisplayInfo
+ __OBJC_CLASS_RO_$_PRSHostContext
+ __OBJC_METACLASS_RO_$_PRSDisplayInfo
+ __OBJC_METACLASS_RO_$_PRSHostContext
+ ___36-[PRSService prewarmWithCompletion:]_block_invoke_2
+ ___36-[PRSService prewarmWithCompletion:]_block_invoke_2.cold.1
+ ___44+[PRSHostContext hostContextWithCompletion:]_block_invoke
+ ___44-[PRSService overnightUpdateWithCompletion:]_block_invoke_2
+ ___44-[PRSService overnightUpdateWithCompletion:]_block_invoke_2.cold.1
+ ___57-[PRSService fetchPosterSnapshotsWithRequest:completion:]_block_invoke_2
+ ___57-[PRSService fetchPosterSnapshotsWithRequest:completion:]_block_invoke_2.cold.1
+ ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.140
+ ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.140.cold.1
+ ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.138
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_64_e8_32s40s48bs_e24_v16?0"PRSHostContext"8ls32l8s40l8s48l8
+ ___getUIApplicationClass_block_invoke
+ ___getUIApplicationClass_block_invoke.cold.1
+ ___getUIScreenClass_block_invoke
+ ___getUIScreenClass_block_invoke.cold.1
+ ___getUIWindowSceneClass_block_invoke
+ ___getUIWindowSceneClass_block_invoke.cold.1
+ _getUIApplicationClass.softClass
+ _getUIScreenClass.softClass
+ _getUIWindowSceneClass.softClass
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$appendBool:withName:ifEqualTo:
+ _objc_msgSend$appendFloat:withName:
+ _objc_msgSend$appendInt64:withName:
+ _objc_msgSend$appendRect:withName:
+ _objc_msgSend$bounds
+ _objc_msgSend$bundleID
+ _objc_msgSend$connectedScenes
+ _objc_msgSend$displayConfiguration
+ _objc_msgSend$hardwareIdentifier
+ _objc_msgSend$hostContextWithCompletion:
+ _objc_msgSend$initWithAuditToken:primaryDisplay:connectedDisplays:hostApplicationIdentifier:userInterfaceStyle:
+ _objc_msgSend$initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:
+ _objc_msgSend$interfaceOrientation
+ _objc_msgSend$isMainDisplay
+ _objc_msgSend$overnightUpdate:completion:
+ _objc_msgSend$performSelector:
+ _objc_msgSend$prewarm:completion:
+ _objc_msgSend$server:overnightUpdate:completion:
+ _objc_msgSend$server:prewarm:completion:
+ _objc_msgSend$setHostContext:
+ _objc_msgSend$tokenForCurrentProcess
+ _objc_msgSend$valueForKey:
+ _objc_opt_respondsToSelector
- -[PRSServer overnightUpdateWithCompletion:]
- -[PRSServer prewarmWithCompletion:]
- ___36-[PRSService prewarmWithCompletion:]_block_invoke.cold.1
- ___44-[PRSService overnightUpdateWithCompletion:]_block_invoke.cold.1
- ___57-[PRSService fetchPosterSnapshotsWithRequest:completion:]_block_invoke.cold.1
- ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.138
- ___64-[PRSService _selectConfigurationAndRefreshSnapshot:completion:]_block_invoke.138.cold.1
- ___77-[PRSService createAndSelectLegacyPosterConfigurationIfNeededWithCompletion:]_block_invoke.134
- _objc_msgSend$overnightUpdateWithCompletion:
- _objc_msgSend$prewarmWithCompletion:
- _objc_msgSend$server:overnightUpdateWithCompletion:
- _objc_msgSend$server:prewarmWithCompletion:
CStrings:
+ "-[PRSServer overnightUpdate:completion:]"
+ "-[PRSServer prewarm:completion:]"
+ "@\"BSAuditToken\""
+ "@\"PRSDisplayInfo\""
+ "@\"PRSHostContext\""
+ "@56@0:8@16@24@32@40q48"
+ "@76@0:8@16q24{CGRect={CGPoint=dd}{CGSize=dd}}32d64B72"
+ "Class getUIApplicationClass(void)_block_invoke"
+ "Class getUIScreenClass(void)_block_invoke"
+ "Class getUIWindowSceneClass(void)_block_invoke"
+ "LandscapeLeft"
+ "LandscapeRight"
+ "Not a UIKit app; bailing on most of PRSHostContext creation"
+ "PRSDisplayInfo"
+ "PRSHostContext"
+ "PRSHostContext.m"
+ "Portrait"
+ "PortraitUpsideDown"
+ "T@\"BSAuditToken\",R,N,V_auditToken"
+ "T@\"NSArray\",R,C,N,V_connectedDisplays"
+ "T@\"NSString\",R,C,N,V_hardwareIdentifier"
+ "T@\"NSString\",R,C,N,V_hostApplicationIdentifier"
+ "T@\"PRSDisplayInfo\",R,N,V_primaryDisplayInfo"
+ "T@\"PRSHostContext\",&,N,V_hostContext"
+ "TB,R,N,V_isMainDisplay"
+ "Td,R,N,V_pointScale"
+ "Tq,R,N,V_userInterfaceStyle"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_bounds"
+ "UIApplication"
+ "UIScreen"
+ "UIWindowScene"
+ "Unknown(%ld)"
+ "Vv32@0:8@\"PRSHostContext\"16@?<v@?@\"NSError\">24"
+ "_auditToken"
+ "_bounds"
+ "_connectedDisplays"
+ "_hardwareIdentifier"
+ "_hostApplicationIdentifier"
+ "_hostContext"
+ "_isMainDisplay"
+ "_pointScale"
+ "_primaryDisplayInfo"
+ "_userInterfaceStyle"
+ "appendBool:withName:ifEqualTo:"
+ "appendFloat:withName:"
+ "appendInt64:withName:"
+ "appendRect:withName:"
+ "bounds"
+ "bundleID"
+ "connectedDisplays"
+ "connectedScenes"
+ "display-%lu"
+ "displayConfiguration"
+ "hardwareIdentifier"
+ "hostApplicationIdentifier"
+ "hostContext"
+ "hostContextWithCompletion:"
+ "initWithAuditToken:primaryDisplay:connectedDisplays:hostApplicationIdentifier:userInterfaceStyle:"
+ "initWithHardwareIdentifier:interfaceOrientation:bounds:pointScale:isMainDisplay:"
+ "isMainDisplay"
+ "main"
+ "new"
+ "overnightUpdate:completion:"
+ "pointScale"
+ "prewarm:completion:"
+ "primaryDisplayInfo"
+ "screen"
+ "screens"
+ "server:overnightUpdate:completion:"
+ "server:prewarm:completion:"
+ "setHostContext:"
+ "sharedApplication"
+ "tokenForCurrentProcess"
+ "userInterfaceStyle"
+ "v16@?0@\"PRSHostContext\"8"
+ "valueForKey:"
- "\""
- "-[PRSServer overnightUpdateWithCompletion:]"
- "-[PRSServer prewarmWithCompletion:]"
- "server:overnightUpdateWithCompletion:"
- "server:prewarmWithCompletion:"

```
