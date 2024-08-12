## FileProviderDaemon

> `/System/Library/PrivateFrameworks/FileProviderDaemon.framework/FileProviderDaemon`

```diff

-2732.0.44.0.0
-  __TEXT.__text: 0xcbd74
-  __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0x52b0
-  __TEXT.__const: 0x1e0
-  __TEXT.__cstring: 0xccdd
-  __TEXT.__oslogstring: 0xdd27
-  __TEXT.__gcc_except_tab: 0xd33c
-  __TEXT.__ustring: 0x18e4
+2732.0.85.0.0
+  __TEXT.__text: 0xcc984
+  __TEXT.__auth_stubs: 0x11e0
+  __TEXT.__objc_methlist: 0x5350
+  __TEXT.__const: 0x1f8
+  __TEXT.__cstring: 0xcd65
+  __TEXT.__oslogstring: 0xde1a
+  __TEXT.__gcc_except_tab: 0xd254
+  __TEXT.__ustring: 0x1972
   __TEXT.__dlopen_cstrs: 0x50
-  __TEXT.__unwind_info: 0x3928
+  __TEXT.__unwind_info: 0x3938
   __TEXT.__objc_classname: 0xa2d
-  __TEXT.__objc_methname: 0x15204
-  __TEXT.__objc_methtype: 0x5375
-  __TEXT.__objc_stubs: 0xdd60
+  __TEXT.__objc_methname: 0x154dc
+  __TEXT.__objc_methtype: 0x53da
+  __TEXT.__objc_stubs: 0xdea0
   __DATA_CONST.__got: 0x810
-  __DATA_CONST.__const: 0x3930
+  __DATA_CONST.__const: 0x3990
   __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4220
+  __DATA_CONST.__objc_selrefs: 0x4288
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0xc8
-  __AUTH_CONST.__auth_got: 0x8d0
+  __AUTH_CONST.__auth_got: 0x900
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0xa00
-  __AUTH_CONST.__cfstring: 0x5b20
-  __AUTH_CONST.__objc_const: 0x12310
+  __AUTH_CONST.__cfstring: 0x5c20
+  __AUTH_CONST.__objc_const: 0x12330
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x938
-  __DATA.__data: 0xeb8
+  __AUTH.__objc_data: 0x9b0
+  __DATA.__objc_ivar: 0x944
+  __DATA.__data: 0xeb0
   __DATA.__bss: 0xd0
-  __DATA_DIRTY.__objc_data: 0xd20
+  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__bss: 0x140
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
-  Functions: 3479
-  Symbols:   4362
-  CStrings:  5871
+  Functions: 3496
+  Symbols:   4380
+  CStrings:  5906
 
Symbols:
+ _FPDomainStateDirectoryName
+ _FPDomainTemporaryDirectoryName
+ _FPPerformWithPersona
+ _fgetxattr
+ _fpfs_is_detached_root
+ _fremovexattr
+ _fsetxattr
+ _stat
CStrings:
+ "\x03\"\x12"
+ " "
+ "  + features: %!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)\n"
+ "%!@(MISSING) - %!@(MISSING)"
+ "+[FPDVolume prettyNameForDomain:]"
+ "-[FPDVolume _computeKnownPathsForRole:]_block_invoke"
+ "@28@0:8I16^@20"
+ "@36@0:8@16I24^@28"
+ "B20@0:8I16"
+ "B44@0:8@16I24^@28^@36"
+ "T@\"NSURL\",R,N,V_syncRootsDirectory"
+ "Tq,R,N,V_speculativeRefreshInheritedContentPolicyMaximumJobs"
+ "[DEBUG] known folder %!l(MISSING)u out of %!l(MISSING)u is a symlink to the logical location"
+ "[ERROR] Failed gathering persona for role: %!d(MISSING) - failing volume init"
+ "[INFO] couldn't retrieve provider domainID from %!@(MISSING): %!@(MISSING)"
+ "[INFO] couldn't upgrade domain xattr on %!@(MISSING): %!d(MISSING)"
+ "_computeKnownPathsForRole:"
+ "_findDomainDirectory:location:error:"
+ "_getProviderDomainIDFromFD:shortDescription:location:domainID:error:"
+ "_skipSystemAlerts"
+ "_speculativeRefreshInheritedContentPolicyMaximumJobs"
+ "_speculativeRefreshInheritedContentPolicyMaximumJobs"
+ "_subAppSupportPathForDomain:fileName:error:"
+ "_syncRootsDirectory"
+ "com.apple.file-provider-domain-id#PN"
+ "contentsOfDirectoryAtPath:error:"
+ "findProviderDomainDirectory:location:error:"
+ "fp_createPathIfNeeded:"
+ "getProviderDomainID:location:foundDomainID:error:"
+ "i48@0:8i16@20I28^@32^@40"
+ "prettyNameForDomain:"
+ "reindexAllItemsForBundleID:protectionClass:reason:acknowledgementHandler:"
+ "remoteVersions,"
+ "removedURL"
+ "removed_domain_"
+ "rootURLForLocation:error:"
+ "setSupportsRemoteVersions:"
+ "speculativeRefreshInheritedContentPolicyMaximumJobs"
+ "stateDirectoryURL:error:"
+ "supportPathForDomain:failIfNotExisting:error:"
+ "supportsRemoteVersions"
+ "temporaryDirectoryURL:error:"
+ "tmp"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?>40"
- "\x03\"\x11"
- "  + features: %!@(MISSING)%!@(MISSING)%!@(MISSING)\n"
- "-[FPDVolume _computeSystemDirectoryForRole:]"
- "@20@0:8I16"
- "_computeSystemDirectoryForRole:"
- "stateDirectoryURLWithCompletionHandler:"
- "temporaryDirectoryURLWithCompletionHandler:"
- "uid"
- "unexpected persona %!@(MISSING) (%!i(MISSING)) instead of expected %!@(MISSING)"
- "v24@0:8@?<v@?@\"NSURL\"@\"NSError\">16"

```
