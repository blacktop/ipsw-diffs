## watchlistd

> `/System/Library/PrivateFrameworks/WatchListKit.framework/Support/watchlistd`

```diff

-800.40.27.0.0
-  __TEXT.__text: 0x27038
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x5060
-  __TEXT.__objc_methlist: 0x21f4
-  __TEXT.__cstring: 0x455d
-  __TEXT.__oslogstring: 0x2431
-  __TEXT.__objc_classname: 0x486
-  __TEXT.__objc_methname: 0x5eb9
-  __TEXT.__objc_methtype: 0xf2c
+800.50.8.0.0
+  __TEXT.__text: 0x2766c
+  __TEXT.__auth_stubs: 0x950
+  __TEXT.__objc_stubs: 0x50e0
+  __TEXT.__objc_methlist: 0x2234
+  __TEXT.__cstring: 0x45b7
+  __TEXT.__oslogstring: 0x2468
+  __TEXT.__objc_classname: 0x498
+  __TEXT.__objc_methname: 0x5f21
+  __TEXT.__objc_methtype: 0xf4f
   __TEXT.__const: 0xf0
   __TEXT.__gcc_except_tab: 0xbb0
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__unwind_info: 0xb24
-  __DATA_CONST.__auth_got: 0x4b0
+  __TEXT.__unwind_info: 0xb40
+  __DATA_CONST.__auth_got: 0x4b8
   __DATA_CONST.__got: 0x258
-  __DATA_CONST.__const: 0x1338
-  __DATA_CONST.__cfstring: 0x3a80
-  __DATA_CONST.__objc_classlist: 0x118
+  __DATA_CONST.__const: 0x1378
+  __DATA_CONST.__cfstring: 0x3ae0
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_classrefs: 0x3e0
+  __DATA_CONST.__objc_classrefs: 0x3e8
   __DATA_CONST.__objc_superrefs: 0xf0
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x54d0
-  __DATA.__objc_selrefs: 0x1aa0
+  __DATA.__objc_const: 0x5580
+  __DATA.__objc_selrefs: 0x1ac0
   __DATA.__objc_ivar: 0x284
-  __DATA.__objc_data: 0xaf0
+  __DATA.__objc_data: 0xb40
   __DATA.__data: 0x510
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0xf8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 27E78206-3BA5-3BE4-82AE-CB288003844B
-  Functions: 887
-  Symbols:   2653
-  CStrings:  2435
+  UUID: 91EF6620-0456-3C78-AC78-FC0AF5542247
+  Functions: 895
+  Symbols:   2678
+  CStrings:  2450
 
Symbols:
+ +[WLDChannelManager defaultChannelManager]
+ -[WLDChannelManager vppaConsentedBundleIDsWithCompletion:]
+ -[WLDClientConnection vppaConsentedBundleIDsWithCompletion:]
+ GCC_except_table49
+ _BagObserverLog.log
+ _BagObserverLog.onceToken
+ _OBJC_CLASS_$_WLDChannelManager
+ _OBJC_METACLASS_$_WLDChannelManager
+ __BagObserverLog
+ __OBJC_$_CLASS_METHODS_WLDChannelManager
+ __OBJC_$_INSTANCE_METHODS_WLDChannelManager
+ __OBJC_CLASS_RO_$_WLDChannelManager
+ __OBJC_METACLASS_RO_$_WLDChannelManager
+ ___42+[WLDChannelManager defaultChannelManager]_block_invoke
+ ___58-[WLDChannelManager vppaConsentedBundleIDsWithCompletion:]_block_invoke
+ ___58-[WLDChannelManager vppaConsentedBundleIDsWithCompletion:]_block_invoke_2
+ ____BagObserverLog_block_invoke
+ __block_literal_global.12
+ _objc_msgSend$defaultChannelManager
+ _objc_msgSend$setByAddingObjectsFromArray:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$vppaConsentedBundleIDsWithCompletion:
+ _os_log_create
+ defaultChannelManager.defaultChannelManager
+ defaultChannelManager.token
- GCC_except_table46
- GCC_except_table48
CStrings:
+ "Bag did change notifications"
+ "BagObserver"
+ "Consented Bundle IDs: %@"
+ "Consented Channel IDs: %@"
+ "Consented brands not found"
+ "Update tracked bag values"
+ "WLDChannelManager"
+ "defaultChannelManager"
+ "setByAddingObjectsFromArray:"
+ "setWithArray:"
+ "v24@0:8@?<v@?@\"NSSet\"@\"NSError\">16"
+ "vppaConsentedBundleIDsWithCompletion:"

```
