## SKAskPermissionExtension

> `/System/Library/Frameworks/StoreKit.framework/PlugIns/SKAskPermissionExtension.appex/SKAskPermissionExtension`

```diff

-813.1.7.0.0
-  __TEXT.__text: 0x5298
+813.2.8.0.0
+  __TEXT.__text: 0x4edc
   __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x2ec
+  __TEXT.__objc_stubs: 0x920
+  __TEXT.__objc_methlist: 0x2c4
   __TEXT.__const: 0x28
-  __TEXT.__gcc_except_tab: 0x394
-  __TEXT.__cstring: 0xb60
-  __TEXT.__objc_methname: 0x1719
-  __TEXT.__oslogstring: 0x2eb
-  __TEXT.__objc_classname: 0x18b
-  __TEXT.__objc_methtype: 0xc73
-  __TEXT.__unwind_info: 0x2b4
+  __TEXT.__gcc_except_tab: 0x33c
+  __TEXT.__cstring: 0xb68
+  __TEXT.__objc_methname: 0x164d
+  __TEXT.__oslogstring: 0x29d
+  __TEXT.__objc_classname: 0x1b1
+  __TEXT.__objc_methtype: 0xc10
+  __TEXT.__unwind_info: 0x29c
   __DATA_CONST.__auth_got: 0x360
   __DATA_CONST.__got: 0xb0
-  __DATA_CONST.__const: 0x5a8
-  __DATA_CONST.__cfstring: 0x19c0
+  __DATA_CONST.__const: 0x5b0
+  __DATA_CONST.__cfstring: 0x19e0
   __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x80
+  __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1860
-  __DATA.__objc_selrefs: 0x360
+  __DATA.__objc_const: 0x1820
+  __DATA.__objc_selrefs: 0x340
   __DATA.__objc_protorefs: 0x30
   __DATA.__objc_classrefs: 0xa8
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x9a0
+  __DATA.__data: 0xa60
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/AskPermission.framework/AskPermission
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7BDB0CA1-C960-39FF-98B2-8619F76579E0
-  Functions: 108
+  UUID: 12FE7A3C-2F9E-3994-9A8B-0AAC6A7544AA
+  Functions: 104
   Symbols:   162
-  CStrings:  749
+  CStrings:  746
 
CStrings:
+ "OverrideService"
+ "PurchaseIntentService"
+ "addPurchaseIntentWithRequest:reply:"
+ "clearPurchaseIntentsWithRequest:reply:"
+ "clientOverridesWithReply:"
+ "context"
+ "overrideServiceWithErrorHandler:"
+ "overrideSynchronousServiceWithErrorHandler:"
+ "purchaseIntentServiceWithErrorHandler:"
+ "purchaseIntentsWithRequest:reply:"
+ "setAppInstallSheetBundleID:reply:"
+ "setClientOverrideWithRequest:reply:"
+ "v24@0:8@?<v@?@\"NSData\"@\"NSError\">16"
+ "v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24"
- "%{public}@: Error in remote proxy while fetching purchase intents: %{public}@"
- "_checkForPendingPurchaseIntents"
- "_purchaseIntentObserverAdded"
- "_purchaseIntentObserverRemoved"
- "addPurchaseIntent:reply:"
- "clearPurchaseIntentForProductIdentifier:"
- "clearPurchaseIntentsForBundleIdentifier:"
- "forceSandboxForBundleIdentifier:untilDate:reply:"
- "purchaseIntentAppInstallSheetOpenForBundleIdentifier:reply:"
- "purchaseIntentsForClient:clearOnRetrieval:reply:"
- "receivedPurchaseIntentsForProductIdentifiers:"
- "registerPurchaseIntentsListener:"
- "setClientOverrides:forBundleIdentifier:untilDate:reply:"
- "unregisterPurchaseIntentsListener:"
- "v32@0:8@\"NSDictionary\"16@?<v@?>24"
- "v32@0:8@\"NSString\"16@?<v@?>24"
- "v40@0:8@\"NSString\"16@\"NSDate\"24@?<v@?>32"
- "v48@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSDate\"32@?<v@?@\"NSError\">40"

```
