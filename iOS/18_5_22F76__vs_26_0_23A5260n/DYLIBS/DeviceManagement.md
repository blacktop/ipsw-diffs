## DeviceManagement

> `/System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement`

```diff

-221.5.1.0.0
-  __TEXT.__text: 0x37dfc
+239.0.0.0.0
+  __TEXT.__text: 0x393a0
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x7334
+  __TEXT.__objc_methlist: 0x75c4
   __TEXT.__const: 0x90
-  __TEXT.__cstring: 0x50a3
+  __TEXT.__cstring: 0x50bb
   __TEXT.__oslogstring: 0xeac
   __TEXT.__ustring: 0xb64
   __TEXT.__gcc_except_tab: 0x2e8
-  __TEXT.__unwind_info: 0xf50
-  __TEXT.__objc_classname: 0x178e
-  __TEXT.__objc_methname: 0x9ca2
+  __TEXT.__unwind_info: 0xf88
+  __TEXT.__objc_classname: 0x17cf
+  __TEXT.__objc_methname: 0x9d79
   __TEXT.__objc_methtype: 0xb15
-  __TEXT.__objc_stubs: 0x4d20
-  __DATA_CONST.__got: 0x368
-  __DATA_CONST.__const: 0xe98
-  __DATA_CONST.__objc_classlist: 0x618
+  __TEXT.__objc_stubs: 0x4d60
+  __DATA_CONST.__got: 0x370
+  __DATA_CONST.__const: 0xee0
+  __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1da0
+  __DATA_CONST.__objc_selrefs: 0x1dc8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x4c8
-  __DATA_CONST.__objc_arraydata: 0x6a0
+  __DATA_CONST.__objc_superrefs: 0x4e0
+  __DATA_CONST.__objc_arraydata: 0x6b8
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x7400
-  __AUTH_CONST.__objc_const: 0x10298
-  __AUTH_CONST.__objc_intobj: 0x1518
-  __AUTH_CONST.__objc_arrayobj: 0x888
-  __AUTH.__objc_data: 0x3570
-  __DATA.__objc_ivar: 0x8d0
+  __AUTH_CONST.__cfstring: 0x7420
+  __AUTH_CONST.__objc_const: 0x106c8
+  __AUTH_CONST.__objc_intobj: 0x1560
+  __AUTH_CONST.__objc_arrayobj: 0x8a0
+  __AUTH.__objc_data: 0x36b0
+  __DATA.__objc_ivar: 0x90c
   __DATA.__data: 0x430
   __DATA.__bss: 0x128
-  __DATA_DIRTY.__objc_data: 0x780
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0xe0
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/Catalyst.framework/Catalyst
   - /System/Library/PrivateFrameworks/Categories.framework/Categories

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 87109D05-006F-30C0-9276-95503975019A
-  Functions: 2341
-  Symbols:   8107
-  CStrings:  3992
+  UUID: 646C554C-AADE-3BC8-92D9-9BB0DEB9966F
+  Functions: 2393
+  Symbols:   8240
+  CStrings:  4003
 
Symbols:
+ +[DMFDDMStartManagingAppRequest allowlistedClassForResultObject]
+ +[DMFDDMStartManagingAppRequest isPermittedOnSystemConnection]
+ +[DMFDDMStartManagingAppRequest isPermittedOnUserConnection]
+ +[DMFDDMStartManagingAppRequest permittedPlatforms]
+ +[DMFDDMStartManagingAppRequest supportsSecureCoding]
+ +[DMFDDMStartManagingAppResultObject supportsSecureCoding]
+ +[DMFStopManagingAppRequest supportsSecureCoding]
+ -[DMFDDMStartManagingAppRequest .cxx_destruct]
+ -[DMFDDMStartManagingAppRequest DNSProxyUUIDString]
+ -[DMFDDMStartManagingAppRequest VPNUUIDString]
+ -[DMFDDMStartManagingAppRequest allowUserToHide]
+ -[DMFDDMStartManagingAppRequest allowUserToLock]
+ -[DMFDDMStartManagingAppRequest associatedDomainsEnableDirectDownloads]
+ -[DMFDDMStartManagingAppRequest associatedDomains]
+ -[DMFDDMStartManagingAppRequest cellularSliceUUIDString]
+ -[DMFDDMStartManagingAppRequest contentFilterUUIDString]
+ -[DMFDDMStartManagingAppRequest description]
+ -[DMFDDMStartManagingAppRequest encodeWithCoder:]
+ -[DMFDDMStartManagingAppRequest initWithCoder:]
+ -[DMFDDMStartManagingAppRequest managementOptions]
+ -[DMFDDMStartManagingAppRequest relayUUIDString]
+ -[DMFDDMStartManagingAppRequest removable]
+ -[DMFDDMStartManagingAppRequest setAllowUserToHide:]
+ -[DMFDDMStartManagingAppRequest setAllowUserToLock:]
+ -[DMFDDMStartManagingAppRequest setAssociatedDomains:]
+ -[DMFDDMStartManagingAppRequest setAssociatedDomainsEnableDirectDownloads:]
+ -[DMFDDMStartManagingAppRequest setCellularSliceUUIDString:]
+ -[DMFDDMStartManagingAppRequest setContentFilterUUIDString:]
+ -[DMFDDMStartManagingAppRequest setDNSProxyUUIDString:]
+ -[DMFDDMStartManagingAppRequest setManagementOptions:]
+ -[DMFDDMStartManagingAppRequest setRelayUUIDString:]
+ -[DMFDDMStartManagingAppRequest setRemovable:]
+ -[DMFDDMStartManagingAppRequest setTapToPayScreenLock:]
+ -[DMFDDMStartManagingAppRequest setVPNUUIDString:]
+ -[DMFDDMStartManagingAppRequest tapToPayScreenLock]
+ -[DMFDDMStartManagingAppResultObject .cxx_destruct]
+ -[DMFDDMStartManagingAppResultObject bundleIdentifier]
+ -[DMFDDMStartManagingAppResultObject description]
+ -[DMFDDMStartManagingAppResultObject encodeWithCoder:]
+ -[DMFDDMStartManagingAppResultObject initWithBundleIdentifier:state:]
+ -[DMFDDMStartManagingAppResultObject initWithCoder:]
+ -[DMFDDMStartManagingAppResultObject state]
+ -[DMFEffectivePolicy hasRestrictivePolicies]
+ -[DMFStopManagingAppRequest description]
+ -[DMFStopManagingAppRequest encodeWithCoder:]
+ -[DMFStopManagingAppRequest initWithCoder:]
+ -[DMFStopManagingAppRequest init]
+ -[DMFStopManagingAppRequest setShouldPreserveAppBinary:]
+ -[DMFStopManagingAppRequest shouldPreserveAppBinary]
+ -[DMFWebsitePolicyMonitor hasAnyRestrictivePoliciesWithCompletionHandler:]
+ -[DMFWebsitePolicyMonitor hasAnyRestrictivePoliciesWithError:]
+ _OBJC_CLASS_$_DMFDDMStartManagingAppRequest
+ _OBJC_CLASS_$_DMFDDMStartManagingAppResultObject
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._DNSProxyUUIDString
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._VPNUUIDString
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._allowUserToHide
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._allowUserToLock
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._associatedDomains
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._associatedDomainsEnableDirectDownloads
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._cellularSliceUUIDString
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._contentFilterUUIDString
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._managementOptions
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._relayUUIDString
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._removable
+ _OBJC_IVAR_$_DMFDDMStartManagingAppRequest._tapToPayScreenLock
+ _OBJC_IVAR_$_DMFDDMStartManagingAppResultObject._bundleIdentifier
+ _OBJC_IVAR_$_DMFDDMStartManagingAppResultObject._state
+ _OBJC_IVAR_$_DMFStopManagingAppRequest._shouldPreserveAppBinary
+ _OBJC_METACLASS_$_DMFDDMStartManagingAppRequest
+ _OBJC_METACLASS_$_DMFDDMStartManagingAppResultObject
+ __OBJC_$_CLASS_METHODS_DMFDDMStartManagingAppRequest
+ __OBJC_$_CLASS_METHODS_DMFDDMStartManagingAppResultObject
+ __OBJC_$_INSTANCE_METHODS_DMFDDMStartManagingAppRequest
+ __OBJC_$_INSTANCE_METHODS_DMFDDMStartManagingAppResultObject
+ __OBJC_$_INSTANCE_METHODS_DMFStopManagingAppRequest
+ __OBJC_$_INSTANCE_VARIABLES_DMFDDMStartManagingAppRequest
+ __OBJC_$_INSTANCE_VARIABLES_DMFDDMStartManagingAppResultObject
+ __OBJC_$_INSTANCE_VARIABLES_DMFStopManagingAppRequest
+ __OBJC_$_PROP_LIST_DMFDDMStartManagingAppRequest
+ __OBJC_$_PROP_LIST_DMFDDMStartManagingAppResultObject
+ __OBJC_$_PROP_LIST_DMFStopManagingAppRequest
+ __OBJC_CLASS_RO_$_DMFDDMStartManagingAppRequest
+ __OBJC_CLASS_RO_$_DMFDDMStartManagingAppResultObject
+ __OBJC_METACLASS_RO_$_DMFDDMStartManagingAppRequest
+ __OBJC_METACLASS_RO_$_DMFDDMStartManagingAppResultObject
+ ___74-[DMFWebsitePolicyMonitor hasAnyRestrictivePoliciesWithCompletionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
+ _objc_msgSend$hasRestrictivePolicies
+ _objc_msgSend$shouldPreserveAppBinary
CStrings:
+ "DMFDDMStartManagingAppRequest"
+ "DMFDDMStartManagingAppResultObject"
+ "TB,N,V_shouldPreserveAppBinary"
+ "_shouldPreserveAppBinary"
+ "hasAnyRestrictivePoliciesWithCompletionHandler:"
+ "hasAnyRestrictivePoliciesWithError:"
+ "hasRestrictivePolicies"
+ "setShouldPreserveAppBinary:"
+ "shouldPreserveAppBinary"

```
