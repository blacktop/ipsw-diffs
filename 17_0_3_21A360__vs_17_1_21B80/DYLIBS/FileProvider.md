## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-1681.0.14.0.0
-  __TEXT.__text: 0x1185a4
-  __TEXT.__auth_stubs: 0x1960
-  __TEXT.__objc_methlist: 0xb188
-  __TEXT.__const: 0x380
-  __TEXT.__gcc_except_tab: 0x7730
-  __TEXT.__cstring: 0x121e7
-  __TEXT.__oslogstring: 0xc81b
+1703.42.2.0.0
+  __TEXT.__text: 0x1186b0
+  __TEXT.__auth_stubs: 0x19b0
+  __TEXT.__objc_methlist: 0xb180
+  __TEXT.__const: 0x3b0
+  __TEXT.__gcc_except_tab: 0x7728
+  __TEXT.__cstring: 0x12233
+  __TEXT.__oslogstring: 0xc828
   __TEXT.__dlopen_cstrs: 0x7ed
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x4e28
+  __TEXT.__unwind_info: 0x4e0c
   __TEXT.__objc_classname: 0x1db7
-  __TEXT.__objc_methname: 0x1e787
-  __TEXT.__objc_methtype: 0x5b60
-  __TEXT.__objc_stubs: 0x12800
-  __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0x5ba0
+  __TEXT.__objc_methname: 0x1e747
+  __TEXT.__objc_methtype: 0x5b63
+  __TEXT.__objc_stubs: 0x127c0
+  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__const: 0x5bc8
   __DATA_CONST.__objc_classlist: 0x620
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x278
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1f090
-  __DATA_CONST.__objc_selrefs: 0x5fc0
+  __DATA_CONST.__objc_selrefs: 0x5fb0
   __DATA_CONST.__objc_arraydata: 0xa98
   __AUTH_CONST.__objc_const: 0x53e0
-  __AUTH_CONST.__cfstring: 0xed40
+  __AUTH_CONST.__cfstring: 0xed80
   __AUTH_CONST.__const: 0x18a0
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__auth_ptr: 0x30
   __AUTH_CONST.__objc_intobj: 0x108
-  __AUTH_CONST.__auth_got: 0xcc0
+  __AUTH_CONST.__auth_got: 0xce8
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x10
   __DATA.__objc_protorefs: 0x128

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6657
-  Symbols:   21189
-  CStrings:  9075
+  Functions: 6661
+  Symbols:   21204
+  CStrings:  9076
 
Symbols:
+ -[_FPItemDecorationValueResolver _formatNameComponents:]
+ _CFDataCreateWithBytesNoCopy
+ _CFPropertyListCreateData
+ _FPDiagnosticAttributeKeyDBFParentItemID
+ _FPEntitlementValueForAuditToken
+ _FPExecutableNameForAuditToken
+ _FPFSD2DRestorePluginIsEnabled
+ _FPFSD2DRestorePluginIsEnabled.enabled
+ _FPFSD2DRestorePluginIsEnabled.onceToken
+ _FPPassivePresenterEntitlement
+ _NSFileProviderErrorApplicationExtensionNotFound
+ _NSFileProviderErrorProviderDomainNotFound
+ _NSFileProviderErrorProviderDomainTemporarilyUnavailable
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ __FPProviderNotFoundErrorHelper
+ ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.336
+ ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.343
+ ___50-[NSFileProviderManager _signalPendingEnumerators]_block_invoke.167
+ ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.138
+ ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.138.cold.1
+ ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.138.cold.2
+ ___FPFSD2DRestorePluginIsEnabled_block_invoke
+ ___block_literal_global.142
+ ___block_literal_global.200
+ ___block_literal_global.342
+ ___block_literal_global.351
+ _dyld_program_sdk_at_least
+ _fpfs_enable_fts_thread_fchdir
+ _fpfs_set_bplist_xattr
+ _fpfs_set_bplist_xattr.cold.1
+ _fpfs_set_bplist_xattr.cold.2
+ _kCFAllocatorMalloc
+ _objc_msgSend$_formatNameComponents:
+ _objc_msgSend$listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:
+ _proc_pidpath_audittoken
- -[GSAddition(FPVersions) _fp_markResolvedWithError:]
- -[GSAddition(FPVersions) conflictLoser]
- -[GSAddition(FPVersions) conflictLoser].cold.1
- __CFExecutableLinkedOnOrAfter
- ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.333
- ___107-[NSFileProviderExtension(CreateItem) createItemBasedOnTemplate:fields:contents:options:completionHandler:]_block_invoke.340
- ___50-[NSFileProviderManager _signalPendingEnumerators]_block_invoke.168
- ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.139
- ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.139.cold.1
- ___98-[NSFileProviderManager fetchDomainServicerSynchronously:useOutgoingConnection:completionHandler:]_block_invoke.139.cold.2
- ___block_literal_global.143
- ___block_literal_global.201
- ___block_literal_global.341
- ___block_literal_global.350
- ___fpfs_supports_endpoint_security_block_invoke
- _fpfs_supports_endpoint_security
- _fpfs_supports_endpoint_security.feature_enabled
- _fpfs_supports_endpoint_security.once_token
- _objc_msgSend$__itemAtURL:didResolveConflictVersionWithClientID:name:purposeID:
- _objc_msgSend$_fp_markResolvedWithError:
- _objc_msgSend$conflictLoser
- _objc_msgSend$listRemoteVersionsOfItemAtURL:completionHandler:
CStrings:
+ "1703.42.2"
+ "Cannot create CFStringCreateWithCString"
+ "Cannot format data with CFPropertyListCreateData %@"
+ "D2D-restore-plugin"
+ "FTS_USE_THREAD_FCHDIR=YES"
+ "_formatNameComponents:"
+ "com.apple.private.fileprovider.passive-presenter"
+ "db_fp_parent_item_id"
+ "listRemoteVersionsOfItemAtURL:includeCachedVersions:completionHandler:"
+ "v36@0:8@\"NSURL\"16B24@?<v@?B@\"FPItem\"@\"NSArray\"@\"NSError\">28"
- "1681.0.14"
- "AddEndpointSecurityCheck"
- "[ERROR] Failed to deserialize conflict loser with name %@ to URL %@. Error: %@"
- "__itemAtURL:didResolveConflictVersionWithClientID:name:purposeID:"
- "_fp_markResolvedWithError:"
- "conflictLoser"
- "listRemoteVersionsOfItemAtURL:completionHandler:"
- "v32@0:8@\"NSURL\"16@?<v@?B@\"FPItem\"@\"NSArray\"@\"NSError\">24"

```
