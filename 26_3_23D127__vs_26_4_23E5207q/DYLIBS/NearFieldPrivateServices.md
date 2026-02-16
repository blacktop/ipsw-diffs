## NearFieldPrivateServices

> `/System/Library/PrivateFrameworks/NearFieldPrivateServices.framework/NearFieldPrivateServices`

```diff

-363.10.0.0.0
-  __TEXT.__text: 0x7bd0
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0x47c
-  __TEXT.__const: 0x98
+364.20.0.0.0
+  __TEXT.__text: 0x6c7c
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_methlist: 0x48c
+  __TEXT.__const: 0x90
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__cstring: 0x1156
-  __TEXT.__oslogstring: 0x786
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__cstring: 0x142c
+  __TEXT.__oslogstring: 0x638
+  __TEXT.__unwind_info: 0x190
   __TEXT.__objc_classname: 0x10f
-  __TEXT.__objc_methname: 0x9d8
+  __TEXT.__objc_methname: 0x9ec
   __TEXT.__objc_methtype: 0x29f
-  __TEXT.__objc_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0x7e0
   __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x510
+  __DATA_CONST.__const: 0x508
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x370
+  __DATA_CONST.__objc_selrefs: 0x378
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x580
-  __AUTH_CONST.__objc_const: 0x6f8
+  __AUTH_CONST.__objc_const: 0x758
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH.__objc_data: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnfshared.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6EFB97D9-A036-3781-A152-79FD24F08CA5
-  Functions: 93
-  Symbols:   106
-  CStrings:  426
+  UUID: 8A44B034-83A2-352A-BE78-ECFBD5B87211
+  Functions: 94
+  Symbols:   102
+  CStrings:  453
 
Symbols:
+ _objc_opt_new
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
- _class_isMetaClass
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x8
- _object_getClass
- _object_getClassName
CStrings:
+ "%s:%i "
+ "%s:%i %@"
+ "%s:%i %{public}@ invalidated"
+ "%s:%i BSService endpoint error"
+ "%s:%i BSServiceConnection=%@"
+ "%s:%i BSServiceConnectionEndpoint=%@"
+ "%s:%i Calling Invalidation for %@"
+ "%s:%i Default do-nothing on event=%{public}@, error=%{public}@"
+ "%s:%i Error : missing user cancel parameter for context pair {local %@, remote %@}"
+ "%s:%i Error : no action."
+ "%s:%i Error : no parameter for context pair {local %@, remote %@}"
+ "%s:%i Failed running command : %@"
+ "%s:%i Failed to call into service : %@"
+ "%s:%i Failed to call into service : no result.."
+ "%s:%i Failed to check reply from service"
+ "%s:%i Failed to connect to restore service"
+ "%s:%i Failed to create root queue"
+ "%s:%i Failed to get reply from service : %@"
+ "%s:%i Invalid bundleIdentifier parameter"
+ "%s:%i Invoking Invalidation handler  for context pair {local %@, remote %@}"
+ "%s:%i Launch error"
+ "%s:%i No Invalidation handler set for context pair {local %@, remote %@}"
+ "%s:%i Reactivate connection"
+ "%s:%i Remote proxy unavailable"
+ "%s:%i Remote scene service %{public}s"
+ "%s:%i Setting Invalidation Handler to %s for %@"
+ "%s:%i Warning un-implemented notification handler."
+ "%s:%i processNDEF error=%@"
+ "%{public}s:%i "
+ "%{public}s:%i %@"
+ "%{public}s:%i %{public}@ invalidated"
+ "%{public}s:%i BSService endpoint error"
+ "%{public}s:%i BSServiceConnection=%@"
+ "%{public}s:%i BSServiceConnectionEndpoint=%@"
+ "%{public}s:%i Calling Invalidation for %@"
+ "%{public}s:%i Default do-nothing on event=%{public}@, error=%{public}@"
+ "%{public}s:%i Error : missing user cancel parameter for context pair {local %@, remote %@}"
+ "%{public}s:%i Error : no action."
+ "%{public}s:%i Error : no parameter for context pair {local %@, remote %@}"
+ "%{public}s:%i Failed running command : %@"
+ "%{public}s:%i Failed to call into service : %@"
+ "%{public}s:%i Failed to call into service : no result.."
+ "%{public}s:%i Failed to check reply from service"
+ "%{public}s:%i Failed to connect to restore service"
+ "%{public}s:%i Failed to create root queue"
+ "%{public}s:%i Failed to get reply from service : %@"
+ "%{public}s:%i Invalid bundleIdentifier parameter"
+ "%{public}s:%i Invoking Invalidation handler  for context pair {local %@, remote %@}"
+ "%{public}s:%i Launch error"
+ "%{public}s:%i No Invalidation handler set for context pair {local %@, remote %@}"
+ "%{public}s:%i Reactivate connection"
+ "%{public}s:%i Remote proxy unavailable"
+ "%{public}s:%i Remote scene service %{public}s"
+ "%{public}s:%i Setting Invalidation Handler to %s for %@"
+ "%{public}s:%i Warning un-implemented notification handler."
+ "%{public}s:%i processNDEF error=%@"
+ "+[NFUIService sceneServiceAvailable]"
+ "-[NFBSClient_BackgroundTagReading _activate]"
+ "-[NFBSClient_BackgroundTagReading _activate]_block_invoke_2"
+ "-[NFBSClient_BackgroundTagReading remoteTarget]"
+ "-[NFBSClient_BackgroundTagReading remoteTarget]_block_invoke"
+ "-[NFPrivateService connectToService:outError:]"
+ "-[NFPrivateService runService:]"
+ "-[NFPrivateService runService:]_block_invoke"
+ "-[NFPrivateService runService:withCompletion:]_block_invoke"
+ "-[NFPrivateService serviceNotificationReceived:]"
+ "-[NFPrivateService serviceNotificationReceived:error:]"
+ "-[NFStorageService deleteAllAppletEntities]"
+ "-[NFStorageService deleteAllESEExpressEntities]"
+ "-[NFStorageService fetchAppletEntitiesWithError:]"
+ "-[NFStorageService fetchESEExpressEntitiesWithError:]"
+ "-[NFStorageService updateAppletEntitiesWithConfig:]"
+ "-[NFStorageService updateESEExpressEntitiesWithConfig:]"
+ "-[NFUIService coreNFCUIInvalidate]"
+ "-[NFUIService coreNFCUISetInvalidationHandler:]"
+ "-[NFUIService launchBundleWithIdentifier:launchReason:launchDomain:]"
+ "-[NFUIService launchBundleWithIdentifier:launchReason:launchDomain:]_block_invoke"
+ "-[NFUIService sceneServiceBackgroundTagReadingWithNDEF:tag:completion:]"
+ "-[NFUIService sceneServiceBackgroundTagReadingWithNDEF:tag:completion:]_block_invoke"
+ "-[NFUIService serviceNotificationReceived:error:]"
+ "initWithDictionary:"
- "%c[%{public}s %{public}s]:%i "
- "%c[%{public}s %{public}s]:%i %@"
- "%c[%{public}s %{public}s]:%i %{public}@ invalidated"
- "%c[%{public}s %{public}s]:%i BSService endpoint error"
- "%c[%{public}s %{public}s]:%i BSServiceConnection=%@"
- "%c[%{public}s %{public}s]:%i BSServiceConnectionEndpoint=%@"
- "%c[%{public}s %{public}s]:%i Calling Invalidation for %@"
- "%c[%{public}s %{public}s]:%i Error : missing user cancel parameter for context pair {local %@, remote %@}"
- "%c[%{public}s %{public}s]:%i Error : no action."
- "%c[%{public}s %{public}s]:%i Error : no parameter for context pair {local %@, remote %@}"
- "%c[%{public}s %{public}s]:%i Failed running command : %@"
- "%c[%{public}s %{public}s]:%i Failed to call into service : %@"
- "%c[%{public}s %{public}s]:%i Failed to call into service : no result.."
- "%c[%{public}s %{public}s]:%i Failed to check reply from service"
- "%c[%{public}s %{public}s]:%i Failed to connect to restore service"
- "%c[%{public}s %{public}s]:%i Failed to create root queue"
- "%c[%{public}s %{public}s]:%i Failed to get reply from service : %@"
- "%c[%{public}s %{public}s]:%i Invalid bundleIdentifier parameter"
- "%c[%{public}s %{public}s]:%i Invoking Invalidation handler  for context pair {local %@, remote %@}"
- "%c[%{public}s %{public}s]:%i Launch error"
- "%c[%{public}s %{public}s]:%i No Invalidation handler set for context pair {local %@, remote %@}"
- "%c[%{public}s %{public}s]:%i Reactivate connection"
- "%c[%{public}s %{public}s]:%i Remote proxy unavailable"
- "%c[%{public}s %{public}s]:%i Remote scene service %{public}s"
- "%c[%{public}s %{public}s]:%i Setting Invalidation Handler to %s for %@"
- "%c[%{public}s %{public}s]:%i Warning un-implemented notification handler."
- "%c[%{public}s %{public}s]:%i processNDEF error=%@"

```
