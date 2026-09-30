## PosterFoundation

> `/System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation`

```diff

-280.101.0.0.0
-  __TEXT.__text: 0x41f98
-  __TEXT.__auth_stubs: 0x1020
-  __TEXT.__objc_methlist: 0x3168
-  __TEXT.__const: 0x176
-  __TEXT.__cstring: 0x3b1d
-  __TEXT.__oslogstring: 0x2d1a
-  __TEXT.__gcc_except_tab: 0xf18
-  __TEXT.__unwind_info: 0x1200
-  __TEXT.__objc_classname: 0x728
-  __TEXT.__objc_methname: 0x73e7
+283.101.0.0.0
+  __TEXT.__text: 0x424b8
+  __TEXT.__auth_stubs: 0x1040
+  __TEXT.__objc_methlist: 0x3128
+  __TEXT.__const: 0x18e
+  __TEXT.__cstring: 0x3b43
+  __TEXT.__oslogstring: 0x305a
+  __TEXT.__gcc_except_tab: 0x10c8
+  __TEXT.__unwind_info: 0x1230
+  __TEXT.__objc_classname: 0x720
+  __TEXT.__objc_methname: 0x73c3
   __TEXT.__objc_methtype: 0x1273
-  __TEXT.__objc_stubs: 0x55c0
-  __DATA_CONST.__got: 0x4d8
-  __DATA_CONST.__const: 0x1330
-  __DATA_CONST.__objc_classlist: 0x1a8
+  __TEXT.__objc_stubs: 0x55e0
+  __DATA_CONST.__got: 0x4d0
+  __DATA_CONST.__const: 0x1350
+  __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x78
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d48
+  __DATA_CONST.__objc_selrefs: 0x1d40
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x120
-  __AUTH_CONST.__auth_got: 0x820
-  __AUTH_CONST.__const: 0x8e0
-  __AUTH_CONST.__cfstring: 0x39e0
-  __AUTH_CONST.__objc_const: 0x8180
+  __AUTH_CONST.__auth_got: 0x830
+  __AUTH_CONST.__const: 0x920
+  __AUTH_CONST.__cfstring: 0x3a60
+  __AUTH_CONST.__objc_const: 0x80c8
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x500
-  __DATA.__objc_ivar: 0x2e0
+  __AUTH.__objc_data: 0x4b0
+  __DATA.__objc_ivar: 0x2dc
   __DATA.__data: 0x850
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0xa8
   __DATA_DIRTY.__objc_data: 0xb90
   __DATA_DIRTY.__bss: 0x1e0
   __DATA_DIRTY.__common: 0xc

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 0CC8E9D4-AD4F-3285-A1E0-A912860650D6
-  Functions: 1576
-  Symbols:   5535
-  CStrings:  2776
+  UUID: 7622650B-B6EA-36E2-BD44-CDF994B96587
+  Functions: 1581
+  Symbols:   5543
+  CStrings:  2795
 
Symbols:
+ -[PFPosterArchiver _unarchiveWithHandler:manifest:error:].cold.10
+ -[PFPosterArchiver _unarchiveWithHandler:manifest:error:].cold.11
+ -[PFPosterPath _issueSandboxExtensionTokenWithContext:]
+ -[PFPosterPath initWithBSXPCCoder:].cold.2
+ -[PFPosterPath initWithCoder:].cold.2
+ -[PFSandboxExtendedURL _consumeSandboxExtensionHandleForXPCObject:context:]
+ -[PFSandboxExtendedURL _consumeSandboxExtensionHandleForXPCObject:context:].cold.1
+ -[PFSandboxExtendedURL _issueSandboxExtensionTokenWithContext:]
+ -[PFSandboxExtendedURL _issueSandboxExtensionTokenWithContext:].cold.1
+ GCC_except_table94
+ _PFLogLayout
+ _PFLogLayout.__logObj
+ _PFLogLayout.cold.1
+ _PFLogLayout.onceToken
+ _PFPosterDefaultRoleForBundleIdentifier.cold.1
+ ___57-[PFPosterArchiver _unarchiveWithHandler:manifest:error:]_block_invoke.63
+ ___80+[PFSandboxExtendedURL temporaryReadwriteSandboxExtendedURLForAuditToken:error:]_block_invoke
+ ___80+[PFSandboxExtendedURL temporaryReadwriteSandboxExtendedURLForAuditToken:error:]_block_invoke.cold.1
+ ___PFLogLayout_block_invoke
+ ___PFPosterDefaultRoleForBundleIdentifier_block_invoke
+ ___block_descriptor_32_e18_B16?0"NSString"8l
+ ___block_literal_global.126
+ ___block_literal_global.150
+ __consumeSandboxExtensionHandleForXPCObject
+ _dispatch_get_global_queue
+ _objc_msgSend$_consumeSandboxExtensionHandleForXPCObject:context:
+ _objc_msgSend$_issueSandboxExtensionTokenWithContext:
+ _objc_msgSend$pf_description
+ _xpc_type_get_name
- +[PFDefer block:]
- +[PFDefer new]
- +[PFServerPosterIdentity configurationIdentityWithProvider:identifier:role:posterUUID:version:supplement:].cold.8
- -[PFDefer .cxx_destruct]
- -[PFDefer _initWithBlock:]
- -[PFDefer dealloc]
- -[PFDefer init]
- -[PFPosterPath _initDecodedWithContentsURL:role:serverIdentity:descriptorIdentifier:sandboxExtensionHandle:].cold.1
- -[PFPosterPath _initDecodedWithContentsURL:role:serverIdentity:descriptorIdentifier:sandboxExtensionHandle:].cold.2
- -[PFPosterPath _initDecodedWithContentsURL:role:serverIdentity:descriptorIdentifier:sandboxExtensionHandle:].cold.3
- -[PFPosterPath _initDecodedWithContentsURL:role:serverIdentity:descriptorIdentifier:sandboxExtensionHandle:].cold.4
- -[PFPosterPath encodeWithBSXPCCoder:].cold.1
- -[PFPosterPath encodeWithCoder:].cold.3
- -[PFSandboxExtendedURL invalidate].cold.4
- -[PFServerPosterIdentity initWithBSXPCCoder:].cold.1
- -[PFServerPosterIdentity initWithCoder:].cold.1
- GCC_except_table92
- _OBJC_CLASS_$_PFDefer
- _OBJC_IVAR_$_PFDefer._deferBlock
- _OBJC_METACLASS_$_PFDefer
- __OBJC_$_CLASS_METHODS_PFDefer
- __OBJC_$_INSTANCE_METHODS_PFDefer
- __OBJC_$_INSTANCE_VARIABLES_PFDefer
- __OBJC_CLASS_RO_$_PFDefer
- __OBJC_METACLASS_RO_$_PFDefer
- ___block_literal_global.147
- _objc_msgSend$_initWithBlock:
- _objc_msgSend$block:
CStrings:
+ "%@: cannot extend access of %@ due to sandbox errno=%i (%s)"
+ "B16@?0@\"NSString\"8"
+ "BSXPC"
+ "Failed to decode PFPosterPath with invalid role: %{public}@, supported roles for device class: %{public}@"
+ "Invalidating <%{public}@ path=%{public}@>"
+ "Layout"
+ "No known role for bundle identifier: %{public}@, Recovering with %{public}@"
+ "Set purgability on URL %@"
+ "Successfully created server path: %{public}@"
+ "Unable to create finalURL: %@"
+ "Unable to move item at provider URL to finalURL: %@"
+ "Unable to set purgability on URL %@: %{public}@"
+ "Warning, contentsURL was not reachable: %{public}@"
+ "[%{public}@] failed to consume sandboxToken %@ with %{darwin.errno}d : <%{public}@ path=%{public}@>"
+ "[%{public}@] failed to decode sandbox token for %{public}@: No XPC object found"
+ "[%{public}@] failed to decode sandbox token: Bad XPC object: %s %@ : <%{public}@ path=%{public}@>"
+ "[%{public}@] failed to issue sandbox extension for path %{public}@: %{darwin.errno}d"
+ "[%{public}@] failed to issue sandbox extension to PID %d for path %{public}@: %{darwin.errno}d"
+ "[Invalid Role][%{public}s] role %{public}@ was invalid, recovered: %{public}@ for provider: %{public}@"
+ "_consumeSandboxExtensionHandleForXPCObject:context:"
+ "_issueSandboxExtensionTokenWithContext:"
+ "bsxpc"
+ "consumed %{public}@ decoded sandboxToken %@ : <%{public}@ %{public}@ path=%{public}@>"
+ "consumed %{public}@ decoded sandboxToken %@ : <%{public}@ path=%{public}@>"
+ "encodeWithCoder"
+ "failed to consume sandboxToken %@ from %{public}@ with %{darwin.errno}d : <%{public}@ %{public}@ path=%{public}@>"
+ "failed to consume sandboxToken %@ from %{public}@ with %{darwin.errno}d : <%{public}@ path=%{public}@>"
+ "found no sandboxToken from %{public}@ : <%{public}@ %{public}@ path=%{public}@>"
+ "initWithCoder"
+ "nsxpc"
+ "sandboxToken was invalid XPC type %s in %@ from %{public}@ with %{darwin.errno}d : <%{public}@ %{public}@ path=%{public}@>"
+ "sandboxToken was invalid XPC type %s in %@ from %{public}@ with %{darwin.errno}d : <%{public}@ path=%{public}@>"
- "<%@:%p> requires %@ rather than %@ : %@"
- "PFDefer"
- "[Invalid Role][%{public}s] role was invalid, recovered: %@"
- "_deferBlock"
- "_initDecodedWithContentsURL:role:serverIdentity:descriptorIdentifier:sandboxExtensionHandle:"
- "_initWithBlock:"
- "block:"
- "cannot extend access of %@ due to sandbox errno=%i (%s)"
- "consumed bsxpc decoded sandboxToken %@ : <%{public}@ %{public}@ path=%{public}@>"
- "consumed bsxpc decoded sandboxToken %@ : <%{public}@ path=%{public}@>"
- "consumed nsxpc decoded sandboxToken %@ : <%{public}@ %{public}@ path=%{public}@>"
- "consumed nsxpc decoded sandboxToken %@ : <%{public}@ path=%{public}@>"
- "failed to consume sandboxToken %@ from bsxpc with errno=%i (%{public}s) : <%{public}@ %{public}@ path=%{public}@>"
- "failed to consume sandboxToken %@ from bsxpc with errno=%i (%{public}s) : <%{public}@ path=%{public}@>"
- "failed to consume sandboxToken %@ from coder with errno=%i (%{public}s) : <%{public}@ path=%{public}@>"
- "failed to consume sandboxToken %@ from nsxpc with errno=%i (%{public}s) : <%{public}@ %{public}@ path=%{public}@>"
- "failed to consume sandboxToken %@ from nsxpc with errno=%i (%{public}s) : <%{public}@ path=%{public}@>"

```
