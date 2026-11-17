## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-113.60.5.0.0
-  __TEXT.__text: 0x54bfc
-  __TEXT.__objc_methlist: 0x440c
+113.60.10.0.0
+  __TEXT.__text: 0x557b8
+  __TEXT.__objc_methlist: 0x44a4
   __TEXT.__const: 0x1aa
   __TEXT.__gcc_except_tab: 0xf40
-  __TEXT.__cstring: 0x5484
-  __TEXT.__oslogstring: 0x737e
+  __TEXT.__cstring: 0x54d8
+  __TEXT.__oslogstring: 0x74d2
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__swift5_typeref: 0x3c
   __TEXT.__swift5_capture: 0x68
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x18d0
+  __TEXT.__unwind_info: 0x1900
   __TEXT.__eh_frame: 0x178
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f58
+  __DATA_CONST.__const: 0x1f68
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3530
+  __DATA_CONST.__objc_selrefs: 0x35a8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x408
-  __DATA_CONST.__got: 0x1208
+  __DATA_CONST.__got: 0x1218
   __AUTH_CONST.__const: 0x630
-  __AUTH_CONST.__cfstring: 0x4c40
-  __AUTH_CONST.__objc_const: 0x6ec0
+  __AUTH_CONST.__cfstring: 0x4ca0
+  __AUTH_CONST.__objc_const: 0x6ef0
   __AUTH_CONST.__objc_arrayobj: 0x8d0
-  __AUTH_CONST.__objc_intobj: 0x660
-  __AUTH_CONST.__auth_got: 0x7e8
+  __AUTH_CONST.__objc_intobj: 0x678
+  __AUTH_CONST.__auth_got: 0x7f0
   __AUTH.__objc_data: 0x688
-  __DATA.__objc_ivar: 0x2d0
+  __DATA.__objc_ivar: 0x2d4
   __DATA.__data: 0x7f0
   __DATA_DIRTY.__objc_data: 0xa28
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1725
-  Symbols:   3457
-  CStrings:  1284
+  Functions: 1741
+  Symbols:   3480
+  CStrings:  1292
 
Symbols:
+ +[MDMDEPPushTokenManager _isPublicTokenFromBurstInHistory:]
+ -[MDMDEPPushTokenManager _pushTokenHistory]
+ -[MDMDEPPushTokenManager _queue_needsAppTokenReissue]
+ -[MDMDEPPushTokenManager _queue_reissueAppToken]
+ -[MDMDEPPushTokenManager _queue_requestAppTokenOncePublicTokenSettles:]
+ -[MDMDEPPushTokenManager _queue_setNeedsAppTokenReissue:]
+ -[MDMDEPPushTokenManager markAppTokenForReissueIfMintedDuringPublicTokenBurst]
+ -[MDMDEPPushTokenManager pendingAppTokenRequest]
+ -[MDMDEPPushTokenManager setPendingAppTokenRequest:]
+ -[MDMPushServiceConnection _appTokenIdentifier]
+ -[MDMPushServiceConnection reissueAppTokenForTopic:]
+ -[MDMPushServiceManager reissueAppTokenForTopic:environment:]
+ GCC_except_table28
+ _DMCEventsDetailsKey
+ _DMCEventsTimestampKey
+ _OBJC_IVAR_$_MDMDEPPushTokenManager._pendingAppTokenRequest
+ __OBJC_$_CLASS_METHODS_MDMDEPPushTokenManager
+ ___61-[MDMPushServiceManager reissueAppTokenForTopic:environment:]_block_invoke
+ ___71-[MDMDEPPushTokenManager _queue_requestAppTokenOncePublicTokenSettles:]_block_invoke
+ ___78-[MDMDEPPushTokenManager markAppTokenForReissueIfMintedDuringPublicTokenBurst]_block_invoke
+ ___82-[MDMDEPPushTokenManager pushServiceManager:didReceivePublicToken:forEnvironment:]_block_invoke
+ _dispatch_block_cancel
+ _kMDMPushTokenEventChannelKey
+ _kMDMPushTokenEventTokenKey
- GCC_except_table23
CStrings:
+ "App Push Token Reissue Needed"
+ "App Push Token Reissue Requested"
+ "Failed to get needsAppTokenReissue with error: %{public}@"
+ "Failed to set needsAppTokenReissue with error: %{public}@"
+ "MDMDEPPushTokenManager: Public token followed another one within %.0f seconds, app token needs reissue"
+ "MDMDEPPushTokenManager: Public token settled, requesting app push token"
+ "MDMDEPPushTokenManager: Reissuing app push token"
+ "NeedsAppTokenReissue"
```
