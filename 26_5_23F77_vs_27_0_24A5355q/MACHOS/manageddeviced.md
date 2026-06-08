## manageddeviced

> `/usr/libexec/manageddeviced`

```diff

-5.100.1.0.0
-  __TEXT.__text: 0x460c8
-  __TEXT.__auth_stubs: 0xcc0
-  __TEXT.__objc_stubs: 0x9040
-  __TEXT.__objc_methlist: 0x40e4
-  __TEXT.__const: 0x118
-  __TEXT.__objc_methname: 0xa328
-  __TEXT.__cstring: 0x2feb
-  __TEXT.__objc_classname: 0xd96
+20.0.0.0.0
+  __TEXT.__text: 0x42d14
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_stubs: 0x90e0
+  __TEXT.__objc_methlist: 0x41bc
+  __TEXT.__const: 0x110
+  __TEXT.__objc_methname: 0xa475
+  __TEXT.__cstring: 0x3040
+  __TEXT.__objc_classname: 0xd98
   __TEXT.__objc_methtype: 0x10f4
-  __TEXT.__gcc_except_tab: 0x814
-  __TEXT.__oslogstring: 0x624a
+  __TEXT.__gcc_except_tab: 0x73c
+  __TEXT.__oslogstring: 0x665c
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__ustring: 0x7d0
-  __TEXT.__unwind_info: 0x1390
-  __DATA_CONST.__auth_got: 0x670
-  __DATA_CONST.__got: 0x948
+  __TEXT.__unwind_info: 0x1270
   __DATA_CONST.__const: 0x19d8
   __DATA_CONST.__cfstring: 0x3560
-  __DATA_CONST.__objc_classlist: 0x358
+  __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x2f0
+  __DATA_CONST.__objc_superrefs: 0x2f8
   __DATA_CONST.__objc_intobj: 0x2b8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__objc_arraydata: 0x230
-  __DATA_CONST.__objc_arrayobj: 0x498
+  __DATA_CONST.__objc_arraydata: 0x238
+  __DATA_CONST.__objc_arrayobj: 0x4b0
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x8c48
-  __DATA.__objc_selrefs: 0x2a30
-  __DATA.__objc_ivar: 0x1f8
-  __DATA.__objc_data: 0x2170
+  __DATA_CONST.__auth_got: 0x698
+  __DATA_CONST.__got: 0x960
+  __DATA.__objc_const: 0x8d18
+  __DATA.__objc_selrefs: 0x2a58
+  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_data: 0x21c0
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x358
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  UUID: F2BD315D-15CF-369B-8CD8-DF4BE6D5568C
-  Functions: 1722
-  Symbols:   525
-  CStrings:  3229
+  UUID: FE4120EC-9864-30CE-BCE2-67E65422FC8E
+  Functions: 1732
+  Symbols:   533
+  CStrings:  3250
 
Symbols:
+ _OBJC_CLASS_$_MDFDDMStartManagingAppRequest
+ _OBJC_CLASS_$_MDFDDMStartManagingAppResultObject
+ _OBJC_CLASS_$_UMUserPersonaAttributes
+ __os_feature_enabled_impl
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "<default>"
+ "Cannot add mapping for persona:%{public}@ bundle:%{public}@ error:%{public}@"
+ "Cannot remove mapping for persona:%{public}@ bundle:%{public}@ error:%{public}@"
+ "Cannot remove mapping for personal persona because there is no personal persona. Skipping."
+ "Cannot remove mapping for personal persona:%{public}@ bundle:%{public}@ error:%{public}@"
+ "Could not remove mapping to persona: %{public}@ for bundle identifier: %{public}@, error: %{public}@"
+ "Error associating app %{public}@ with persona %{public}@ when marking as managed: %{public}@"
+ "InstalledContentLibrary"
+ "MDDDDMStartManagingAppOperation"
+ "MDFNotifications"
+ "MI_Persona_BundleID_Relayering"
+ "Managing DDM app: %{public}@"
+ "Marking an app in the installing state as installing"
+ "Removed mapping for personal persona:%{public}@ bundle:%{public}@"
+ "Request to manage DDM app %{public}@ "
+ "Send app store request result error: Provided license is for Free or User Owned App but App is neither free nor user owned."
+ "Send app store request result error: Success = no, error= null, and metadata is null!"
+ "Send app store request result error: Success = no, error= null, but metadata is non nil!"
+ "Start installing enterprise app with persona: %{public}@, manifest URL from: %{public}@"
+ "Start installing enterprise app with persona:%{public}@, manifest URL from: %{public}@"
+ "Start updating enterprise app with persona: %{public}@, manifest URL from: %{public}@"
+ "_personalPersonaID"
+ "addPersonaForUniqueString:toAppWithBundleID:inDomain:error:"
+ "addPersonaMappingForBundleID:personaID:error:"
+ "personaAttributesForPersonaType:"
+ "removeAppMetadataForBundleIdentifier:personaIdentifier:error:"
+ "removeAppPersonaMappingForBundleIdentifier:personaIdentifier:error:"
+ "removePersonaForUniqueString:fromAppWithBundleID:inDomain:error:"
+ "removePersonaMappingForBundleID:personaID:error:"
+ "removePersonalPersonaMappingForBundleIdentifier:"
+ "startInstallingEnterpriseAppWithManifestURL:personaIdentifier:completion:"
- "Could not remove mapping to persona for for bundle identifier: %{bundleIdentifier}@, error: %{public}@"
- "DMFNotifications"
- "Start installing enterprise app with manifest URL from: %{public}@"
- "Start updating enterprise app with manifest URL from: %{public}@"
- "listAllPersonaWithAttributes"
- "override"
- "removeAppMetadataForBundleIdentifier:error:"
- "removePersonaMappingForBundleID:error:"
- "startInstallingEnterpriseAppWithManifestURL:completion:"
- "userPersonaBundleIDList"

```
