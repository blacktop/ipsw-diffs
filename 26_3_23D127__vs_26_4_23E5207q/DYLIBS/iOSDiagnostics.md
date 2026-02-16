## iOSDiagnostics

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iOSDiagnostics`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0x521c
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x91c
+1066.100.26.0.0
+  __TEXT.__text: 0x5970
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x97c
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0xa51
+  __TEXT.__cstring: 0xa8a
   __TEXT.__oslogstring: 0x396
-  __TEXT.__gcc_except_tab: 0xd4
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_classname: 0x269
-  __TEXT.__objc_methname: 0x16e7
-  __TEXT.__objc_methtype: 0x55f
-  __TEXT.__objc_stubs: 0x12c0
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x348
-  __DATA_CONST.__objc_classlist: 0x40
+  __TEXT.__gcc_except_tab: 0xbc
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__objc_classname: 0x29d
+  __TEXT.__objc_methname: 0x17fd
+  __TEXT.__objc_methtype: 0x588
+  __TEXT.__objc_stubs: 0x1400
+  __DATA_CONST.__got: 0x140
+  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x660
+  __DATA_CONST.__objc_selrefs: 0x6a8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__auth_got: 0x1f8
+  __AUTH_CONST.__auth_got: 0x1e0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x560
-  __AUTH_CONST.__objc_const: 0x1a20
+  __AUTH_CONST.__cfstring: 0x5c0
+  __AUTH_CONST.__objc_const: 0x1b18
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0x64
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D7FCD5C9-BDF0-39B0-8548-9262D332853F
-  Functions: 166
-  Symbols:   800
-  CStrings:  463
+  UUID: DEFA20CD-8277-3082-9385-C9B1500D2403
+  Functions: 178
+  Symbols:   844
+  CStrings:  483
 
Symbols:
+ +[DADiagnosticsRemoteViewController requestViewControllerWithHostBundleID:flow:handler:]
+ -[DADiagnosticFlow countryCode]
+ -[DADiagnosticFlow initWithDestination:serialNumber:sessionID:passcode:countryCode:]
+ -[DADiagnosticFlow setCountryCode:]
+ -[DADiagnosticsRemoteViewController requestViewControllerWithHostBundleID:flow:handler:]
+ -[DADiagnosticsRemoteViewControllerSceneSpecification .cxx_destruct]
+ -[DADiagnosticsRemoteViewControllerSceneSpecification hostApplicationBundleIdentifier]
+ -[DADiagnosticsRemoteViewControllerSceneSpecification setHostApplicationBundleIdentifier:]
+ -[DADiagnosticsRemoteViewControllerSceneSpecification setStartingFlow:]
+ -[DADiagnosticsRemoteViewControllerSceneSpecification startingFlow]
+ -[DADiagnosticsRemoteViewControllerSceneSpecification userActivity]
+ _OBJC_CLASS_$_DADiagnosticsRemoteViewControllerSceneSpecification
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSUserActivity
+ _OBJC_IVAR_$_DADiagnosticFlow._countryCode
+ _OBJC_IVAR_$_DADiagnosticsRemoteViewControllerSceneSpecification._hostApplicationBundleIdentifier
+ _OBJC_IVAR_$_DADiagnosticsRemoteViewControllerSceneSpecification._startingFlow
+ _OBJC_METACLASS_$_DADiagnosticsRemoteViewControllerSceneSpecification
+ _OBJC_METACLASS_$__UISceneHostingSceneSpecification
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ __OBJC_$_INSTANCE_METHODS_DADiagnosticsRemoteViewControllerSceneSpecification
+ __OBJC_$_INSTANCE_VARIABLES_DADiagnosticsRemoteViewControllerSceneSpecification
+ __OBJC_$_PROP_LIST_DADiagnosticsRemoteViewControllerSceneSpecification
+ __OBJC_CLASS_RO_$_DADiagnosticsRemoteViewControllerSceneSpecification
+ __OBJC_METACLASS_RO_$_DADiagnosticsRemoteViewControllerSceneSpecification
+ ___88-[DADiagnosticsRemoteViewController requestViewControllerWithHostBundleID:flow:handler:]_block_invoke
+ _objc_msgSend$archivedDataWithRootObject:requiringSecureCoding:error:
+ _objc_msgSend$countryCode
+ _objc_msgSend$dictionary
+ _objc_msgSend$hostApplicationBundleIdentifier
+ _objc_msgSend$initWithActivityType:
+ _objc_msgSend$initWithDestination:serialNumber:sessionID:passcode:countryCode:
+ _objc_msgSend$length
+ _objc_msgSend$requestViewControllerWithHostBundleID:flow:handler:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setStartingFlow:
+ _objc_msgSend$setUserInfo:
+ _objc_msgSend$startingFlow
+ _objc_retainAutoreleasedReturnValue
- -[DADiagnosticsRemoteViewController hostApplicationBundleIdentifier]
- -[DADiagnosticsRemoteViewController requestViewControllerWithHostBundleID:handler:]
- -[DADiagnosticsRemoteViewController setHostApplicationBundleIdentifier:]
- -[DADiagnosticsRemoteViewControllerHostToServiceAction performActionForHostedWindowScene:].cold.5
- _OBJC_IVAR_$_DADiagnosticsRemoteViewController._hostApplicationBundleIdentifier
- ___83-[DADiagnosticsRemoteViewController requestViewControllerWithHostBundleID:handler:]_block_invoke
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$remoteViewControllerDidSetHostBundleIdentifier:
- _objc_msgSend$specification
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
CStrings:
+ "#"
+ "<%@: %p> destination: %lu, serialNumber: %@, sessionID: %@, passcode: %@, countryCode: %@"
+ "@56@0:8Q16@24@32@40@48"
+ "DADiagnosticsRemoteViewControllerSceneSpecification"
+ "T@\"NSString\",&,N,V_countryCode"
+ "_countryCode"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "com.apple.diagnostics.rvc"
+ "countryCode"
+ "dictionary"
+ "initWithActivityType:"
+ "initWithDestination:serialNumber:sessionID:passcode:countryCode:"
+ "length"
+ "requestViewControllerWithHostBundleID:flow:handler:"
+ "setCountryCode:"
+ "setObject:forKeyedSubscript:"
+ "setUserInfo:"
+ "startingFlowData"
+ "userActivity"
+ "v40@0:8@16@24@?32"
- "$"
- "<%@: %p> destination: %lu, serialNumber: %@, sessionID: %@, passcode: %@"
- "HostToServiceActionTypeSetHostBundleIdentifier"
- "remoteViewControllerDidSetHostBundleIdentifier:"
- "specification"

```
