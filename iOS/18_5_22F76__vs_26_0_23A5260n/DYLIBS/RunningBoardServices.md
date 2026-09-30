## RunningBoardServices

> `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

```diff

-961.100.17.0.0
-  __TEXT.__text: 0x40c30
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_methlist: 0x5790
-  __TEXT.__const: 0x148
-  __TEXT.__cstring: 0x468f
-  __TEXT.__oslogstring: 0x26e1
-  __TEXT.__gcc_except_tab: 0x920
+1002.0.0.502.1
+  __TEXT.__text: 0x42084
+  __TEXT.__auth_stubs: 0xe30
+  __TEXT.__delay_helper: 0xc8
+  __TEXT.__objc_methlist: 0x5a38
+  __TEXT.__const: 0x150
+  __TEXT.__cstring: 0x480f
+  __TEXT.__oslogstring: 0x2768
+  __TEXT.__gcc_except_tab: 0x92c
   __TEXT.__dlopen_cstrs: 0x76
-  __TEXT.__unwind_info: 0x14a0
-  __TEXT.__objc_classname: 0xec7
-  __TEXT.__objc_methname: 0x7ab8
-  __TEXT.__objc_methtype: 0x14fb
-  __TEXT.__objc_stubs: 0x48a0
-  __DATA_CONST.__got: 0x4b8
-  __DATA_CONST.__const: 0xce8
-  __DATA_CONST.__objc_classlist: 0x430
+  __TEXT.__unwind_info: 0x1550
+  __TEXT.__objc_classname: 0xf04
+  __TEXT.__objc_methname: 0x8029
+  __TEXT.__objc_methtype: 0x1595
+  __TEXT.__objc_stubs: 0x4aa0
+  __DATA_CONST.__got: 0x4e0
+  __DATA_CONST.__const: 0xcf0
+  __DATA_CONST.__objc_classlist: 0x440
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c08
+  __DATA_CONST.__objc_selrefs: 0x1ce0
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2c8
-  __AUTH_CONST.__auth_got: 0x718
+  __DATA_CONST.__objc_superrefs: 0x2d8
+  __AUTH_CONST.__auth_got: 0x728
   __AUTH_CONST.__const: 0x660
-  __AUTH_CONST.__cfstring: 0x5d00
-  __AUTH_CONST.__objc_const: 0xa928
+  __AUTH_CONST.__cfstring: 0x5e40
+  __AUTH_CONST.__objc_const: 0xacb8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x1720
-  __DATA.__objc_ivar: 0x58c
-  __DATA.__data: 0x620
-  __DATA.__bss: 0x270
-  __DATA_DIRTY.__objc_data: 0x12c0
+  __AUTH.__objc_data: 0x1680
+  __DATA.__objc_ivar: 0x5bc
+  __DATA.__data: 0x624
+  __DATA.__bss: 0x260
+  __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x130
+  __DATA_DIRTY.__bss: 0x140
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppServerSupport.framework/AppServerSupport
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F3D2C9B7-E451-37AB-82F7-B2C16E22B107
-  Functions: 2196
-  Symbols:   6934
-  CStrings:  3592
+  UUID: 29C29724-C8F4-3811-AB07-B7AF9C937160
+  Functions: 2253
+  Symbols:   7098
+  CStrings:  3674
 
Symbols:
+ +[RBSExtensionProcessIdentity extensionIdentityFromDataRepresentation:]
+ +[RBSExtensionProcessIdentity shouldManageExtensionWithExtensionPoint:]
+ +[RBSProcessHandle _handleForIdentifier:pidVersion:ignoreCache:error:]
+ +[RBSProcessHandle forceLookupIdentifer:error:]
+ +[RBSProcessHandle handleForAuditToken:error:]
+ +[RBSProcessHandle handleForIdentifier:pidVersion:error:]
+ +[RBSProcessIdentity(Extension) identityForExtensionIdentity:]
+ +[RBSProcessIdentity(Extension) identityForExtensionIdentity:].cold.1
+ +[RBSProcessIdentity(Extension) identityForExtensionIdentity:hostIdentifier:]
+ +[RBSProcessIdentity(Extension) identityForExtensionIdentity:hostIdentifier:].cold.1
+ -[RBSExtensionProcessIdentity .cxx_destruct]
+ -[RBSExtensionProcessIdentity _initWithExtensionIdentity:hostIdentity:hostIdentifier:]
+ -[RBSExtensionProcessIdentity _initWithExtensionIdentity:hostIdentity:hostIdentifier:auid:]
+ -[RBSExtensionProcessIdentity _matchesIdentity:]
+ -[RBSExtensionProcessIdentity copyWithAuid:]
+ -[RBSExtensionProcessIdentity defaultManageFlags]
+ -[RBSExtensionProcessIdentity encodeForJob]
+ -[RBSExtensionProcessIdentity encodeForJob].cold.1
+ -[RBSExtensionProcessIdentity encodeWithRBSXPCCoder:]
+ -[RBSExtensionProcessIdentity extensionIdentity]
+ -[RBSExtensionProcessIdentity hostIdentifier]
+ -[RBSExtensionProcessIdentity hostIdentity]
+ -[RBSExtensionProcessIdentity inheritsCoalitionBand]
+ -[RBSExtensionProcessIdentity initWithDecodeFromJob:uuid:]
+ -[RBSExtensionProcessIdentity initWithRBSXPCCoder:]
+ -[RBSExtensionProcessIdentity isAnonymous]
+ -[RBSExtensionProcessIdentity isEqualToIdentity:]
+ -[RBSExtensionProcessIdentity isExtension]
+ -[RBSExtensionProcessIdentity isExternal]
+ -[RBSExtensionProcessIdentity isMultiInstanceExtension]
+ -[RBSExtensionProcessIdentity isXPCService]
+ -[RBSExtensionProcessIdentity personaString]
+ -[RBSExtensionProcessIdentity persona]
+ -[RBSExtensionProcessIdentity setExtensionIdentity:]
+ -[RBSExtensionProcessIdentity supportsLaunchingDirectly]
+ -[RBSExtensionProcessIdentity uuid]
+ -[RBSExtensionProcessIdentity validationToken]
+ -[RBSLaunchContext clientRestriction]
+ -[RBSLaunchContext launchdJobProperties]
+ -[RBSLaunchContext setClientRestriction:]
+ -[RBSLaunchContext setLaunchdJobProperties:]
+ -[RBSLaunchdJobDescriptor .cxx_destruct]
+ -[RBSLaunchdJobDescriptor attributes]
+ -[RBSLaunchdJobDescriptor backoff]
+ -[RBSLaunchdJobDescriptor bundleIdentifier]
+ -[RBSLaunchdJobDescriptor clientRestriction]
+ -[RBSLaunchdJobDescriptor executableURL]
+ -[RBSLaunchdJobDescriptor initWithExecutableURL:bundleIdentifier:]
+ -[RBSLaunchdJobDescriptor jobProperties]
+ -[RBSLaunchdJobDescriptor launchRequestEndpointIdentifiers]
+ -[RBSLaunchdJobDescriptor managedEndpointLaunchIdentifiers]
+ -[RBSLaunchdJobDescriptor setAttributes:]
+ -[RBSLaunchdJobDescriptor setBackoff:]
+ -[RBSLaunchdJobDescriptor setBundleIdentifier:]
+ -[RBSLaunchdJobDescriptor setClientRestriction:]
+ -[RBSLaunchdJobDescriptor setExecutableURL:]
+ -[RBSLaunchdJobDescriptor setJobProperties:]
+ -[RBSLaunchdJobDescriptor setLaunchRequestEndpointIdentifiers:]
+ GCC_except_table43
+ _OBJC_CLASS_$_OSLaunchdJobProperties
+ _OBJC_CLASS_$_RBSExtensionProcessIdentity
+ _OBJC_CLASS_$_RBSLaunchdJobDescriptor
+ _OBJC_CLASS_$__EXExtensionIdentity
+ _OBJC_IVAR_$_RBSExtensionProcessIdentity._extensionIdentity
+ _OBJC_IVAR_$_RBSExtensionProcessIdentity._hostIdentifier
+ _OBJC_IVAR_$_RBSExtensionProcessIdentity._hostIdentity
+ _OBJC_IVAR_$_RBSLaunchContext._clientRestriction
+ _OBJC_IVAR_$_RBSLaunchContext._launchdJobProperties
+ _OBJC_IVAR_$_RBSLaunchdJobDescriptor._attributes
+ _OBJC_IVAR_$_RBSLaunchdJobDescriptor._backoff
+ _OBJC_IVAR_$_RBSLaunchdJobDescriptor._bundleIdentifier
+ _OBJC_IVAR_$_RBSLaunchdJobDescriptor._clientRestriction
+ _OBJC_IVAR_$_RBSLaunchdJobDescriptor._executableURL
+ _OBJC_IVAR_$_RBSLaunchdJobDescriptor._jobProperties
+ _OBJC_IVAR_$_RBSLaunchdJobDescriptor._launchRequestEndpointIdentifiers
+ _OBJC_METACLASS_$_RBSExtensionProcessIdentity
+ _OBJC_METACLASS_$_RBSLaunchdJobDescriptor
+ __OBJC_$_CLASS_METHODS_RBSExtensionProcessIdentity
+ __OBJC_$_CLASS_METHODS_RBSProcessIdentity(RBCompatibility|Extension)
+ __OBJC_$_INSTANCE_METHODS_RBSExtensionProcessIdentity
+ __OBJC_$_INSTANCE_METHODS_RBSLaunchdJobDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_RBSExtensionProcessIdentity
+ __OBJC_$_INSTANCE_VARIABLES_RBSLaunchdJobDescriptor
+ __OBJC_$_PROP_LIST_RBSExtensionProcessIdentity
+ __OBJC_$_PROP_LIST_RBSLaunchdJobDescriptor
+ __OBJC_CLASS_RO_$_RBSExtensionProcessIdentity
+ __OBJC_CLASS_RO_$_RBSLaunchdJobDescriptor
+ __OBJC_METACLASS_RO_$_RBSExtensionProcessIdentity
+ __OBJC_METACLASS_RO_$_RBSLaunchdJobDescriptor
+ ___NSArray0__struct
+ ___NSDictionary0__struct
+ ____BSXPCDecodeObject_block_invoke.205
+ ___block_descriptor_64_e8_32s40s48r_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8u56l8s40l8r48l8
+ _dlopen
+ _dlopenHelper$ExtensionFoundation
+ _dlopenHelperFlag$ExtensionFoundation
+ _gotLoadHelper_x20$_OBJC_CLASS_$__EXExtensionIdentity
+ _objc_msgSend$_initWithExtensionIdentity:hostIdentity:hostIdentifier:
+ _objc_msgSend$_initWithExtensionIdentity:hostIdentity:hostIdentifier:auid:
+ _objc_msgSend$auditToken
+ _objc_msgSend$clientRestriction
+ _objc_msgSend$dataRepresentation
+ _objc_msgSend$extensionIdentity
+ _objc_msgSend$extensionIdentityFromDataRepresentation:
+ _objc_msgSend$extensionPointType
+ _objc_msgSend$identityFromDataRepresentation:error:
+ _objc_msgSend$instanceUUID
+ _objc_msgSend$launchRequestIdentifierToMachNameMap
+ _objc_msgSend$launchdJobProperties
+ _objc_msgSend$pidversion
+ _objc_msgSend$setClientRestriction:
+ _objc_msgSend$setLaunchRequestIdentifierToMachNameMap:
+ _objc_msgSend$setLaunchdJobProperties:
+ _objc_setProperty_atomic
- GCC_except_table39
- __OBJC_$_CLASS_METHODS_RBSProcessIdentity(RBCompatibility)
- ____BSXPCDecodeObject_block_invoke.202
- ___block_descriptor_56_e8_32s40s_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8u48l8s40l8
CStrings:
+ " process has mismatched pid version"
+ "/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation"
+ "@\"<RBSExtensionIdentityProtocol>\""
+ "@\"NSURL\""
+ "@\"OSLaunchdJobProperties\""
+ "@\"RBDomainRestriction\""
+ "@36@0:8@16i24o^@28"
+ "@44@0:8@16@24@32I40"
+ "@56@0:8{?=[8I]}16o^@48"
+ "Element %@ at index %zu failed to decode, expected class was %@"
+ "Found different PID versions for handle in local process cache, now trying to fetch new handle %@"
+ "RBSExtensionProcessIdentity"
+ "RBSLaunchdJobDescriptor"
+ "RBSProcessIdentity+Extension.m"
+ "T@\"<RBSExtensionIdentityProtocol>\",&,V_extensionIdentity"
+ "T@\"NSArray\",&,V_attributes"
+ "T@\"NSDictionary\",&,V_clientRestriction"
+ "T@\"NSDictionary\",&,V_launchRequestEndpointIdentifiers"
+ "T@\"NSSet\",R"
+ "T@\"NSString\",&,V_bundleIdentifier"
+ "T@\"NSURL\",&,V_executableURL"
+ "T@\"OSLaunchdJobProperties\",&,N,V_launchdJobProperties"
+ "T@\"OSLaunchdJobProperties\",&,V_jobProperties"
+ "T@\"RBDomainRestriction\",&,N,V_clientRestriction"
+ "T@\"RBSProcessIdentifier\",R,V_hostIdentifier"
+ "T@\"RBSProcessIdentity\",R,V_hostIdentity"
+ "TB,V_backoff"
+ "Unable to decode array: an object within the array failed to decode. %@"
+ "UserInitiated"
+ "_backoff"
+ "_clientRestriction"
+ "_executableURL"
+ "_extensionIdentity"
+ "_hostIdentifier"
+ "_hostIdentity"
+ "_initWithExtensionIdentity:hostIdentity:hostIdentifier:"
+ "_initWithExtensionIdentity:hostIdentity:hostIdentifier:auid:"
+ "_jobProperties"
+ "_launchRequestEndpointIdentifiers"
+ "_launchdJobProperties"
+ "`hostless_extensions` feature is disabled."
+ "backoff"
+ "clientRestriction"
+ "dataRepresentation"
+ "executableURL"
+ "extension<%@(%@:%@)(%d)>"
+ "extension<%@(%@:%@)>"
+ "extensionIdentity"
+ "extensionIdentityFromDataRepresentation:"
+ "extensionPointType"
+ "forceLookupIdentifer:error:"
+ "handle %@ has mismatched pid version"
+ "handleForAuditToken:error:"
+ "handleForIdentifier:pidVersion:error:"
+ "hostless_extensions"
+ "identityForExtensionIdentity:"
+ "identityForExtensionIdentity:hostIdentifier:"
+ "identityFromDataRepresentation:error:"
+ "initWithExecutableURL:bundleIdentifier:"
+ "instanceUUID"
+ "jobProperties"
+ "launchRequestEndpointIdentifiers"
+ "launchdJobProperties"
+ "setBackoff:"
+ "setClientRestriction:"
+ "setExecutableURL:"
+ "setExtensionIdentity:"
+ "setJobProperties:"
+ "setLaunchRequestEndpointIdentifiers:"
+ "setLaunchdJobProperties:"
- "1`"

```
