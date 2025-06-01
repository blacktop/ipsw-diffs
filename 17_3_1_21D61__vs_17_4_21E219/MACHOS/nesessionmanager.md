## nesessionmanager

> `/usr/libexec/nesessionmanager`

```diff

-1838.80.4.0.0
-  __TEXT.__text: 0x8e4ec
-  __TEXT.__auth_stubs: 0x1900
-  __TEXT.__objc_stubs: 0x7020
+1838.102.2.0.0
+  __TEXT.__text: 0x8fd80
+  __TEXT.__auth_stubs: 0x1920
+  __TEXT.__objc_stubs: 0x7080
   __TEXT.__objc_methlist: 0x27ac
   __TEXT.__const: 0x88
   __TEXT.__gcc_except_tab: 0x14bc
   __TEXT.__objc_classname: 0x8a9
-  __TEXT.__objc_methname: 0x7f3e
+  __TEXT.__objc_methname: 0x7fd0
   __TEXT.__objc_methtype: 0x1b3a
-  __TEXT.__oslogstring: 0xad15
-  __TEXT.__cstring: 0x3d1d
-  __TEXT.__unwind_info: 0x1210
-  __DATA_CONST.__auth_got: 0xc90
+  __TEXT.__oslogstring: 0xb084
+  __TEXT.__cstring: 0x3dc3
+  __TEXT.__unwind_info: 0x1208
+  __DATA_CONST.__auth_got: 0xca0
   __DATA_CONST.__got: 0x320
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x1990
-  __DATA_CONST.__cfstring: 0x20a0
+  __DATA_CONST.__cfstring: 0x2100
   __DATA_CONST.__objc_classlist: 0x1d0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_classrefs: 0x490
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x138
   __DATA_CONST.__objc_arrayobj: 0x108
   __DATA_CONST.__objc_intobj: 0x1f8
   __DATA_CONST.__objc_dictobj: 0x78
-  __DATA.__objc_const: 0x72c0
-  __DATA.__objc_selrefs: 0x1d40
-  __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x490
-  __DATA.__objc_superrefs: 0x188
-  __DATA.__objc_ivar: 0x5dc
+  __DATA.__objc_const: 0x72e0
+  __DATA.__objc_selrefs: 0x1d58
+  __DATA.__objc_ivar: 0x5e0
   __DATA.__objc_data: 0x1220
   __DATA.__data: 0xbb8
   __DATA.__bss: 0xf0

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileWiFi.framework/MobileWiFi
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SystemWake.framework/SystemWake
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnetworkextension.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 003B326D-0F34-30B6-B1AB-D6F64ACABA6D
-  Functions: 1516
-  Symbols:   604
-  CStrings:  3540
+  UUID: 2CA68CB4-DA70-34EE-8E57-F014D87F2850
+  Functions: 1517
+  Symbols:   606
+  CStrings:  3570
 
Symbols:
+ _NEHelperCachePopulateUUIDsForConfiguration
+ _ne_copy_cached_uuids_for_bundle_identifier
CStrings:
+ "\x11?\x06"
+ "%@: Handling %s notification, starting"
+ "%@: No UUIDs in the cache for %@, populating the cache from the path rules"
+ "%@: Updating agent on fallback interface change"
+ "%@: Updating policies and agent on install"
+ "%@: Updating policies on app state change"
+ "%@: Updating policies on fallback app change"
+ "%s: Adding policy %@ for DeviceCommunication DIRECTLINK interfaces"
+ "%s: Adding policy %@ for account id %s (priority %d)"
+ "%s: Adding policy for TCP listeners"
+ "-[NEPolicySession(AlwaysOnVPN) addDeviceCommunicationExceptionWithOrder:]"
+ "Added DeviceCommunication DIRECTLINK policy: %@"
+ "Added DeviceCommunication account id policy: %@"
+ "Deny Policy IDs added for %@: %@"
+ "DeviceCommunication"
+ "Failed to add policy for DeviceCommunication DIRECTLINK: %@"
+ "Failed to add policy for DeviceCommunication account id: %@"
+ "Failed to handle device communication exception"
+ "Silent deny Policy IDs added for %@: %@"
+ "Silent deny Policy IDs to be removed for %@: %@"
+ "T@\"NSString\",?,R,C"
+ "Updating on KVO change, policies=%d, agent=%d"
+ "_pathRuleSilentDenyMulticastPolicyIDs"
+ "com.apple.WebKit.Networking"
+ "com.apple.remotepairing.devicecommunication"
+ "excludeDeviceCommunication"
+ "multicastPreferenceSet"
+ "scopedInterfaceFlags:eflags:xflags:"
- "\x11?\x05"

```
