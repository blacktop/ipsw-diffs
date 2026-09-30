## AuthKitUI

> `/System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI`

```diff

-525.127.1.2.0
-  __TEXT.__text: 0xc41f8
+525.250.4.0.0
+  __TEXT.__text: 0xc5288
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x82ac
+  __TEXT.__objc_methlist: 0x832c
   __TEXT.__const: 0x276
-  __TEXT.__gcc_except_tab: 0x1348
-  __TEXT.__cstring: 0x50c8
-  __TEXT.__oslogstring: 0x4963
+  __TEXT.__gcc_except_tab: 0x13d0
+  __TEXT.__cstring: 0x50e8
+  __TEXT.__oslogstring: 0x4b7d
   __TEXT.__dlopen_cstrs: 0x163
   __TEXT.__ustring: 0x2c
   __TEXT.__constg_swiftt: 0xac

   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x14f8
-  __TEXT.__objc_classname: 0x1536
-  __TEXT.__objc_methname: 0x172d1
-  __TEXT.__objc_methtype: 0x472b
-  __TEXT.__objc_stubs: 0x120e0
-  __DATA_CONST.__got: 0xca8
-  __DATA_CONST.__const: 0x24a0
+  __TEXT.__unwind_info: 0x1520
+  __TEXT.__objc_classname: 0x1532
+  __TEXT.__objc_methname: 0x174e7
+  __TEXT.__objc_methtype: 0x47df
+  __TEXT.__objc_stubs: 0x12200
+  __DATA_CONST.__got: 0xcb0
+  __DATA_CONST.__const: 0x24d0
   __DATA_CONST.__objc_classlist: 0x388
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5b98
+  __DATA_CONST.__objc_selrefs: 0x5be0
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x2b8
   __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x4e00
-  __AUTH_CONST.__objc_const: 0x170b8
+  __AUTH_CONST.__cfstring: 0x4e20
+  __AUTH_CONST.__objc_const: 0x17148
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_doubleobj: 0x40
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0x2068
   __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x740
+  __DATA.__objc_ivar: 0x74c
   __DATA.__data: 0x19d0
   __DATA.__bss: 0x160
   __DATA_DIRTY.__objc_data: 0x320

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: BA1D075F-21CE-3EEC-9DFF-250D864526A2
-  Functions: 2699
-  Symbols:   11000
-  CStrings:  6134
+  UUID: 6E9BA445-B2D9-3822-BBE7-08E87CC922F6
+  Functions: 2711
+  Symbols:   11039
+  CStrings:  6156
 
Symbols:
+ -[AKAppleIDFollowUpServerUIPresenter _performSimpleProfileUpgradeWithCompletion:]
+ -[AKAppleIDFollowUpServerUIPresenter presentSimpleProfileUpgradeWithContext:viewController:withCompletion:]
+ -[AKRemoteViewSessionController newSimpleProfileUpgradeController]
+ -[AKRemoteViewSessionController setNewSimpleProfileUpgradeController:]
+ -[_AKRemoteViewService _onmainqueue_presentSimpleProfileUpgradeWithContext:completionHandler:]
+ -[_AKRemoteViewService newSimpleProfileUpgradeController]
+ -[_AKRemoteViewService presentSimpleProfileUpgradeWithContext:completionHandler:]
+ -[_AKRemoteViewService setNewSimpleProfileUpgradeController:]
+ GCC_except_table19
+ GCC_except_table48
+ _OBJC_IVAR_$_AKAppleIDFollowUpServerUIPresenter._skipFollowUpAcknowledgment
+ _OBJC_IVAR_$_AKRemoteViewSessionController._newSimpleProfileUpgradeController
+ _OBJC_IVAR_$__AKRemoteViewService._newSimpleProfileUpgradeController
+ __AKChildProfileUpgradeURLKey
+ ___107-[AKAppleIDFollowUpServerUIPresenter presentSimpleProfileUpgradeWithContext:viewController:withCompletion:]_block_invoke
+ ___81-[AKAppleIDFollowUpServerUIPresenter _performSimpleProfileUpgradeWithCompletion:]_block_invoke
+ ___81-[_AKRemoteViewService presentSimpleProfileUpgradeWithContext:completionHandler:]_block_invoke
+ ___93-[AKAppleIDFollowUpServerUIPresenter _performAuthKitActionWithResponse:additionalData:error:]_block_invoke.62
+ ___93-[AKAppleIDFollowUpServerUIPresenter _performAuthKitActionWithResponse:additionalData:error:]_block_invoke.63
+ ___block_descriptor_48_e8_32bs40w_e20_v20?0B8"NSError"12lw40l8s32l8
+ ___os_log_helper_16_2_3_8_64_8_112_8_64
+ _objc_msgSend$_onmainqueue_presentSimpleProfileUpgradeWithContext:completionHandler:
+ _objc_msgSend$_performSimpleProfileUpgradeWithCompletion:
+ _objc_msgSend$followUpItemIdentifier
+ _objc_msgSend$newSimpleProfileUpgradeController
+ _objc_msgSend$setNewSimpleProfileUpgradeController:
+ _objc_msgSend$setSimpleProfileContext:
+ _objc_msgSend$setUniqueItemIdentifier:
+ _objc_msgSend$setUrlKey:
+ _objc_msgSend$simpleProfileContext
+ _objc_msgSend$upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:
- GCC_except_table46
- ___93-[AKAppleIDFollowUpServerUIPresenter _performAuthKitActionWithResponse:additionalData:error:]_block_invoke.58
- ___93-[AKAppleIDFollowUpServerUIPresenter _performAuthKitActionWithResponse:additionalData:error:]_block_invoke.59
- _objc_msgSend$setContentOffset:animated:
CStrings:
+ "Presenting simple profile upgrade on main queue with context: %@"
+ "T@?,C,N,V_newSimpleProfileUpgradeController"
+ "Vv32@0:8@\"AKSimpleProfileContextUpgrade\"16@?<v@?B@\"NSError\">24"
+ "_newSimpleProfileUpgradeController"
+ "_onmainqueue_presentSimpleProfileUpgradeWithContext:completionHandler:"
+ "_performSimpleProfileUpgradeWithCompletion - Child profile upgrade failed: %@"
+ "_performSimpleProfileUpgradeWithCompletion - missing followUpIdentifier or sponsorAltDSID in follow-up item"
+ "_performSimpleProfileUpgradeWithCompletion:"
+ "_skipFollowUpAcknowledgment"
+ "childProfileUpgrade"
+ "followUpItemIdentifier"
+ "newSimpleProfileUpgradeController"
+ "presentServerUIWithContext - child simpleprofile upgrade detected, urlKey=%@"
+ "presentSimpleProfileUpgradeWithContext"
+ "presentSimpleProfileUpgradeWithContext failed to fetch follow-up item with identifier=%@ altDSID=%{mask.hash}@"
+ "presentSimpleProfileUpgradeWithContext failed with error %@"
+ "presentSimpleProfileUpgradeWithContext:completionHandler:"
+ "presentSimpleProfileUpgradeWithContext:viewController:withCompletion:"
+ "setNewSimpleProfileUpgradeController:"
+ "setSimpleProfileContext:"
+ "simpleProfileContext"
+ "upgradeSimpleProfileWithFollowUpIdentifier:sponsorAltDSID:completion:"
+ "v40@0:8@\"AKSimpleProfileContextUpgrade\"16@\"UIViewController\"24@?<v@?@\"NSHTTPURLResponse\"@\"NSDictionary\"@\"NSError\">32"
- "\v"
- "setContentOffset:animated:"

```
