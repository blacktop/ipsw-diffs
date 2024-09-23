## Contacts

> `/System/Library/Frameworks/Contacts.framework/Contacts`

```diff

-3659.0.0.0.0
-  __TEXT.__text: 0x18d1f8
-  __TEXT.__auth_stubs: 0x30c0
-  __TEXT.__objc_methlist: 0x166c0
+3660.0.0.0.0
+  __TEXT.__text: 0x1907d0
+  __TEXT.__auth_stubs: 0x3080
+  __TEXT.__objc_methlist: 0x16728
   __TEXT.__const: 0x1268
   __TEXT.__gcc_except_tab: 0x3194
-  __TEXT.__cstring: 0xc292
-  __TEXT.__oslogstring: 0x8d2a
+  __TEXT.__cstring: 0xc332
+  __TEXT.__oslogstring: 0x959a
   __TEXT.__dlopen_cstrs: 0x394
   __TEXT.__ustring: 0x12
-  __TEXT.__constg_swiftt: 0xc4c
-  __TEXT.__swift5_typeref: 0xb5b
+  __TEXT.__constg_swiftt: 0xc7c
+  __TEXT.__swift5_typeref: 0xbaf
   __TEXT.__swift5_reflstr: 0x65b
   __TEXT.__swift5_fieldmd: 0x6ec
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift5_proto: 0x90
   __TEXT.__swift5_types: 0x8c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_capture: 0x444
-  __TEXT.__unwind_info: 0x6e50
-  __TEXT.__eh_frame: 0x1f68
+  __TEXT.__swift5_capture: 0x50c
+  __TEXT.__unwind_info: 0x6ee0
+  __TEXT.__eh_frame: 0x2198
   __TEXT.__objc_classname: 0x3a64
-  __TEXT.__objc_methname: 0x26aea
-  __TEXT.__objc_methtype: 0x4904
-  __TEXT.__objc_stubs: 0x1b9e0
-  __DATA_CONST.__got: 0x19e8
+  __TEXT.__objc_methname: 0x26cca
+  __TEXT.__objc_methtype: 0x4915
+  __TEXT.__objc_stubs: 0x1bb00
+  __DATA_CONST.__got: 0x19d8
   __DATA_CONST.__const: 0x5b80
   __DATA_CONST.__objc_classlist: 0xee8
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x86e0
+  __DATA_CONST.__objc_selrefs: 0x8728
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0x898
   __DATA_CONST.__objc_arraydata: 0x258
-  __AUTH_CONST.__auth_got: 0x1870
+  __AUTH_CONST.__auth_got: 0x1850
   __AUTH_CONST.__auth_ptr: 0x3e0
-  __AUTH_CONST.__const: 0x5e90
-  __AUTH_CONST.__cfstring: 0xd060
-  __AUTH_CONST.__objc_const: 0x299f8
+  __AUTH_CONST.__const: 0x5ff8
+  __AUTH_CONST.__cfstring: 0xd080
+  __AUTH_CONST.__objc_const: 0x29a58
   __AUTH_CONST.__objc_intobj: 0x558
   __AUTH_CONST.__objc_arrayobj: 0x1c8
-  __AUTH.__objc_data: 0x4dd0
+  __AUTH.__objc_data: 0x4db0
   __AUTH.__data: 0x590
-  __DATA.__objc_ivar: 0x1048
-  __DATA.__data: 0x2640
-  __DATA.__bss: 0x21b0
+  __DATA.__objc_ivar: 0x1050
+  __DATA.__data: 0x26e0
+  __DATA.__bss: 0x21a0
   __DATA.__common: 0x90
-  __DATA_DIRTY.__objc_data: 0x51e0
+  __DATA_DIRTY.__objc_data: 0x5230
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0xb10
+  __DATA_DIRTY.__bss: 0xb20
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/ClassKit.framework/ClassKit
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10879
-  Symbols:   11858
-  CStrings:  9984
+  Functions: 10912
+  Symbols:   11864
+  CStrings:  10016
 
Symbols:
+ _CNProviderDomainCommandTypeFetchRegisteredDomains
- _swift_dynamicCastMetatype
- _CNProviderDomainCommandTypeFetchDomains
CStrings:
+ "addDomain(domain: %!{(MISSING)public}s, bundleIdentifier: %!{(MISSING)public}s)"
+ "createProviderContainer() failed to create container with provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "askUserToEnable() user did not enable extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "_registered"
+ "disableDomain() continuing to disable although failed to invalidate %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "resetEnumeration(for: %!s(MISSING), bundleIdentifier: %!{(MISSING)public}s)"
+ "deleteProviderContainer() deleted container with identifier %!{(MISSING)public}s and provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "registered"
+ "synchronize() failed due to some XPC connection error with extension %!{(MISSING)public}s for %!{(MISSING)public}s app, extension proxy might not conform to CNContactProviderExtensionXPCProtocol."
+ "registeredDomainsFor:completionHandler:"
+ "isExtensionEnabled() did not find extension for %!{(MISSING)public}s"
+ "enableDomain() did not find container with provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "invalidateExtensionImpl() failed to invalidate extension %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "invalidateExtensionImpl() did not invalidate as extension is not loaded"
+ "terminateExtension() did terminate extension %!{(MISSING)public}s"
+ "synchronize(using session:, bundleIdentifier: %!{(MISSING)public}s)"
+ "isExtensionEnabled(with: %!{(MISSING)public}s)"
+ "resetEnumeration() will reset extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "synchronize() failed to create remote object proxy for extension %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "resetProviderContainer() did reset provider container for %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "removeDomain:bundleIdentifier:error:"
+ "invalidateExtension(for: %!s(MISSING), bundleIdentifier: %!{(MISSING)public}s)"
+ "disableDomainFor:bundleIdentifier:completionHandler:"
+ "scheduleFirstSynchronization() failed to schedule synchronization for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "resetEnumeration() did not find extension for %!{(MISSING)public}s"
+ "invalidateExtension() did not invalidate as extension is disabled"
+ "disableDomain(for: %!{(MISSING)public}s, bundleIdentifier: %!{(MISSING)public}s)"
+ "synchronize() will synchronize extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "FetchRegisteredDomains"
+ "addDomain() found container already exists with identifier %!{(MISSING)public}s and provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "enableDomain(for: %!{(MISSING)public}s, bundleIdentifier: %!{(MISSING)public}s, showPrompt: %!{(MISSING)bool,public}d, shouldSynchronize: %!{(MISSING)bool,public}d)"
+ "enableProviderContainer() enabled container with identifier %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "terminateExtension() will terminate extension %!{(MISSING)public}s"
+ "enableProviderContainer() failed to enable container with identifier %!{(MISSING)public}s and provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "isRegistered"
+ "initWithType:includingDisabledContainers:"
+ "providerContainer() fetched container with identifier %!{(MISSING)public}s and provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "v40@0:8@\"CNContactProviderSupportDomain\"16@\"NSString\"24@?<v@?@\"NSError\">32"
+ "resetProviderContainer() did not find extension for %!{(MISSING)public}s"
+ "resetProviderContainer() will reset provider container for %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "TB,N,GisRegistered,V_registered"
+ "fetchRegisteredDomains"
+ "registeredDomains(for: %!{(MISSING)public}s)"
+ "removeDomainFor:bundleIdentifier:completionHandler:"
+ "disableDomain() did not find extension for %!{(MISSING)public}s"
+ "predicateForContainersWithType:includingDisabledContainers:"
+ "invalidateExtension() will invalidate extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "synchronize() failed to synchronize extension %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "invalidateExtensionImpl() failed due to some XPC connection error with extension %!{(MISSING)public}s for %!{(MISSING)public}s app, extension proxy might not conform to CNContactProviderExtensionXPCProtocol."
+ "providerContainer() did not find extension for %!{(MISSING)public}s"
+ "appExtensionProcess() did not find extension for %!{(MISSING)public}s"
+ "registeredDomainsForBundleIdentifier:error:"
+ "initWithDomain:code:userInfo:"
+ "fetchProviderContainer() failed to find container with provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "disableDomain() found container already disabled with provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "appExtensionProcess() will not launch extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "registeredDomainsWithError:"
+ "registeredDomains() did not find extension for %!{(MISSING)public}s"
+ "addDomain() did not find extension for %!{(MISSING)public}s"
+ "enableDomainFor:bundleIdentifier:showPrompt:shouldSynchronize:completionHandler:"
+ "appExtensionProcess() if needed will launch extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "terminateExtension() failed to terminate extension %!{(MISSING)public}s, error = %!{(MISSING)public}s"
+ "invalidateExtension() did invalidate extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "setRegistered:"
+ "appExtensionProcess() extension process configuration was interrupted for extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "@28@0:8q16B24"
+ "TB,R,N,V_includeDisabledContainers"
+ "synchronize() did synchronize extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "@56@0:8@16@24@32@40B48B52"
+ "resetEnumeration() continuing to reset although failed to invalidate %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "resetEnumeration() did reset extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "addDomain:bundleIdentifier:completionHandler:"
+ "invalidateExtension() did not find extension for %!{(MISSING)public}s"
+ "resetEnumeration() did not reset as extension is disabled"
+ "providerContainer(for: %!{(MISSING)public}s)"
+ "createProviderContainer() created container with identifier %!{(MISSING)public}s and provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app"
+ "initWithDomainIdentifer:displayName:userInfo:bundleIdentifier:registered:enabled:"
+ "enableDomain() did not find extension for %!{(MISSING)public}s"
+ "deleteProviderContainer() failed to delete container with identifier %!{(MISSING)public}s and provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "invalidateExtensionImpl() failed to create remote object proxy for extension %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
+ "enableDomain() found container already enabled with provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Failed to synchronize extension %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "Extension already enabled %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "App extension process configuration was interrupted with extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Did reset provider container for %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "domainsWithError:"
- "Did not invalidate as extension not found for %!{(MISSING)public}s"
- "Did not reset provider container as extension not found for %!{(MISSING)public}s"
- "Continuing to disable although failed to invalidate %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "Disabled extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Will invalidate extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Failed to delete provider container %!{(MISSING)public}s with provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "Will synchronize extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "User did not enable extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "FetchDomains"
- "Did not reset as extension is disabled"
- "Extension already disabled %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Did synchronize extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "fetchDomains"
- "Failed to enable extension %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "Did reset extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Will not launch disabled extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "disableExtensionFor:bundleIdentifier:completionHandler:"
- "Will reset provider container for %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Failed due to some XPC connection error with extension %!{(MISSING)public}s for %!{(MISSING)public}s app, extension proxy might not conform to CNContactProviderExtensionXPCProtocol."
- "initWithType:"
- "Failed to find provider container with provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "Did invalidate extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Extension not found for %!{(MISSING)public}s"
- "Did not reset as extension not found for %!{(MISSING)public}s"
- "Did not invalidate as extension is disabled"
- "Failed to create provider container for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "providerContainer for %!{(MISSING)public}s"
- "Failed to disable extension %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "Will terminate extension %!{(MISSING)public}s"
- "Created provider container %!{(MISSING)public}s with provider identifier %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Failed to schedule first synchronization for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "Will reset extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Failed to create remote object proxy for extension %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "Continuing to reset although failed to invalidate %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "Did not invalidate as extension is not loaded"
- "Failed to terminate extension %!{(MISSING)public}s, error = %!{(MISSING)public}s"
- "Deleted provider container %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "enableExtensionFor:bundleIdentifier:showPrompt:shouldSynchronize:completionHandler:"
- "No provider container available with disabled extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Failed to invalidate extension %!{(MISSING)public}s for %!{(MISSING)public}s app, error = %!{(MISSING)public}s"
- "Fetched provider container identifier %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "Enabled extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "If needed will launch extension %!{(MISSING)public}s for %!{(MISSING)public}s app"
- "@52@0:8@16@24@32@40B48"
- "Did terminate extension %!{(MISSING)public}s"
- "initWithDomainIdentifer:displayName:userInfo:bundleIdentifier:enabled:"

```
