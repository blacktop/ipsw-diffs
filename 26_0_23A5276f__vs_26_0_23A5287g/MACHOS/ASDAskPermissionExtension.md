## ASDAskPermissionExtension

> `/System/Library/PrivateFrameworks/AppStoreDaemon.framework/PlugIns/ASDAskPermissionExtension.appex/ASDAskPermissionExtension`

```diff

-12.0.48.0.0
-  __TEXT.__text: 0x908
-  __TEXT.__auth_stubs: 0x170
-  __TEXT.__objc_stubs: 0x280
+12.0.54.2.1
+  __TEXT.__text: 0xde8
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__objc_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x20
-  __TEXT.__const: 0x28
-  __TEXT.__oslogstring: 0x2a3
-  __TEXT.__cstring: 0x41
+  __TEXT.__const: 0x30
+  __TEXT.__gcc_except_tab: 0xcc
+  __TEXT.__oslogstring: 0x3c9
+  __TEXT.__cstring: 0xa1
   __TEXT.__objc_classname: 0x1e
-  __TEXT.__objc_methname: 0x1a0
+  __TEXT.__objc_methname: 0x29a
   __TEXT.__objc_methtype: 0x17
-  __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0xc0
-  __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x50
-  __DATA_CONST.__cfstring: 0x20
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__auth_got: 0x140
+  __DATA_CONST.__got: 0x78
+  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__cfstring: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xb0
+  __DATA.__objc_selrefs: 0x100
   __DATA.__objc_data: 0x50
+  - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AskPermission.framework/AskPermission
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9888DB79-2569-3E25-A86C-2E55D8B6FCBC
-  Functions: 4
-  Symbols:   41
-  CStrings:  38
+  UUID: F002E040-7E25-33E1-A67C-3945FE54CC43
+  Functions: 7
+  Symbols:   62
+  CStrings:  61
 
Symbols:
+ _ASDLogHandleForCategory
+ _OBJC_CLASS_$_ACAccountStore
+ _OBJC_CLASS_$_AMSBag
+ _OBJC_CLASS_$_AMSMetricsIdentifierKey
+ _OBJC_CLASS_$_AMSMetricsIdentifierStore
+ _OBJC_CLASS_$_NSArray
+ __Block_object_dispose
+ __Unwind_Resume
+ ___objc_personality_v0
+ __os_log_debug_impl
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_time
+ _objc_release
+ _objc_release_x25
+ _objc_release_x26
+ _objc_release_x27
+ _objc_release_x28
+ _objc_retain_x23
+ _objc_storeStrong
CStrings:
+ "1"
+ "APPSTORE_PAYMENTS_ENGAGEMENT"
+ "[%{public}@] Failed to load AMSMetricsIdentifierStore"
+ "[%{public}@] Failed to lookup AMSMetricsIdentifierStore due to error: %{public}@"
+ "[%{public}@] Got the following fields from the AMSMetricsIdentifierStore. Fields: %@"
+ "[%{public}@] Timed out attempting to initialize AMSMetricsIdentifierStore"
+ "ams_activeiTunesAccount"
+ "ams_sharedAccountStore"
+ "appstored"
+ "arrayWithObjects:count:"
+ "bagForProfile:profileVersion:"
+ "count"
+ "generateEventFieldsForKeys:"
+ "identifierStoreWithAccount:bagNamespace:bag:"
+ "keyWithName:crossDeviceSync:"
+ "resultWithCompletion:"
+ "setMetricsOverlay:"
+ "userId"
+ "v24@?0@\"AMSMetricsIdentifierStore\"8@\"NSError\"16"

```
