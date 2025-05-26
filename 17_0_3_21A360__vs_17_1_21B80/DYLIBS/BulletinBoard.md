## BulletinBoard

> `/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard`

```diff

-887.0.0.0.0
-  __TEXT.__text: 0x75760
+887.1.1.0.0
+  __TEXT.__text: 0x75798
   __TEXT.__auth_stubs: 0x9e0
-  __TEXT.__objc_methlist: 0x7558
+  __TEXT.__objc_methlist: 0x7568
   __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0xac0
   __TEXT.__cstring: 0x5de6
-  __TEXT.__oslogstring: 0x6303
+  __TEXT.__oslogstring: 0x631a
   __TEXT.__dlopen_cstrs: 0x13e
-  __TEXT.__unwind_info: 0x20c8
+  __TEXT.__unwind_info: 0x20cc
   __TEXT.__objc_classname: 0xbb3
-  __TEXT.__objc_methname: 0x12751
-  __TEXT.__objc_methtype: 0x2a4e
+  __TEXT.__objc_methname: 0x1279b
+  __TEXT.__objc_methtype: 0x2a5f
   __TEXT.__objc_stubs: 0xcae0
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x2080
+  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__const: 0x20a8
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x10b70
-  __DATA_CONST.__objc_selrefs: 0x3ba8
+  __DATA_CONST.__objc_selrefs: 0x3bb0
   __DATA_CONST.__objc_arraydata: 0x140
   __AUTH_CONST.__cfstring: 0x63e0
   __AUTH_CONST.__objc_const: 0x2548
   __AUTH_CONST.__const: 0x1280
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x500
   __AUTH.__objc_data: 0x550
   __DATA.__objc_protorefs: 0x80

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3381
-  Symbols:   10887
-  CStrings:  4655
+  Functions: 3384
+  Symbols:   10891
+  CStrings:  4657
 
Symbols:
+ -[BBDataProviderProxy withdrawBulletinWithPublisherBulletinID:shouldSync:]
+ -[BBRemoteDataProvider withdrawBulletinWithPublisherBulletinID:shouldSync:]
+ -[BBServer withdrawBulletinID:shouldSync:]
+ -[BBServer(Publication) withdrawBulletinRequestsWithPublisherBulletinID:shouldSync:forSectionID:]
+ GCC_except_table84
+ GCC_except_table90
+ _BBDataProviderWithdrawBulletinWithPublisherBulletinIDShouldSync
+ ___74-[BBDataProviderProxy withdrawBulletinWithPublisherBulletinID:shouldSync:]_block_invoke
+ ___74-[BBRemoteDataProvider deliverResponse:forBulletinRequest:withCompletion:]_block_invoke.166
+ ___75-[BBRemoteDataProvider withdrawBulletinWithPublisherBulletinID:shouldSync:]_block_invoke
+ ___BBDataProviderWithdrawBulletinWithPublisherBulletinIDShouldSync_block_invoke
+ ___block_descriptor_41_e8_32s_e43_v16?0"<BBRemoteDataProviderServerProxy>"8ls32l8
+ ___block_literal_global.109
+ ___block_literal_global.155
+ _objc_msgSend$withdrawBulletinID:shouldSync:
+ _objc_msgSend$withdrawBulletinRequestsWithPublisherBulletinID:shouldSync:forSectionID:
+ _objc_msgSend$withdrawBulletinWithPublisherBulletinID:shouldSync:
- -[BBServer withdrawBulletinID:]
- -[BBServer(Publication) withdrawBulletinRequestsWithPublisherBulletinID:forSectionID:]
- GCC_except_table83
- GCC_except_table89
- GCC_except_table93
- _IDSSendMessageOptionPushPriorityKey
- _IDSSendMessageOptionSendModeKey
- ___63-[BBDataProviderProxy withdrawBulletinWithPublisherBulletinID:]_block_invoke
- ___64-[BBRemoteDataProvider withdrawBulletinWithPublisherBulletinID:]_block_invoke
- ___74-[BBRemoteDataProvider deliverResponse:forBulletinRequest:withCompletion:]_block_invoke.165
- ___BBDataProviderWithdrawBulletinWithPublisherBulletinID_block_invoke
- ___block_literal_global.107
- ___block_literal_global.96
- _objc_msgSend$withdrawBulletinID:
- _objc_msgSend$withdrawBulletinRequestsWithPublisherBulletinID:forSectionID:
- _objc_msgSend$withdrawBulletinWithPublisherBulletinID:
CStrings:
+ "BBDataProvider: Withdraw bulletin in section %{public}@, publisher bulletin ID %{public}@, should sync %{BOOL}d"
+ "v36@0:8@16B24@28"
+ "withdrawBulletinID:shouldSync:"
+ "withdrawBulletinRequestsWithPublisherBulletinID:shouldSync:forSectionID:"
+ "withdrawBulletinWithPublisherBulletinID:shouldSync:"
- "BBDataProvider: Withdraw bulletin in section %{public}@ publisher bulletin ID %{public}@"
- "withdrawBulletinID:"
- "withdrawBulletinRequestsWithPublisherBulletinID:forSectionID:"

```
