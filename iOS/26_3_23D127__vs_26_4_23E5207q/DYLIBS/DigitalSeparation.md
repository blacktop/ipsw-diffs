## DigitalSeparation

> `/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`

```diff

-595.0.2.0.0
-  __TEXT.__text: 0x2aa84
-  __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0x1dcc
+618.0.0.0.0
+  __TEXT.__text: 0x2c860
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_methlist: 0x1dec
   __TEXT.__cstring: 0x1366
   __TEXT.__const: 0xb0
-  __TEXT.__gcc_except_tab: 0xd40
-  __TEXT.__oslogstring: 0x2485
+  __TEXT.__gcc_except_tab: 0xcc8
+  __TEXT.__oslogstring: 0x2495
   __TEXT.__dlopen_cstrs: 0x68
-  __TEXT.__unwind_info: 0x890
+  __TEXT.__unwind_info: 0xa08
   __TEXT.__objc_classname: 0x2a3
-  __TEXT.__objc_methname: 0x4ae7
-  __TEXT.__objc_methtype: 0xa50
-  __TEXT.__objc_stubs: 0x4120
-  __DATA_CONST.__got: 0x3f8
-  __DATA_CONST.__const: 0xc80
+  __TEXT.__objc_methname: 0x4b57
+  __TEXT.__objc_methtype: 0xa31
+  __TEXT.__objc_stubs: 0x41c0
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__const: 0xca8
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13f8
+  __DATA_CONST.__objc_selrefs: 0x1418
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x378
+  __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__cfstring: 0x14a0
-  __AUTH_CONST.__objc_const: 0x42c0
+  __AUTH_CONST.__objc_const: 0x42a0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x180
+  __DATA.__objc_ivar: 0x17c
   __DATA.__data: 0x4e8
   __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x460

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0EB3B361-E962-3FB0-894C-661C0C6A06E3
-  Functions: 803
-  Symbols:   3073
-  CStrings:  1524
+  UUID: 4C05BE0F-FA78-31AC-842A-FAF4F8F9DF51
+  Functions: 849
+  Symbols:   3164
+  CStrings:  1526
 
Symbols:
+ +[DSError errorWithException:]
+ -[DSXPCSharingPermissions _sharingPeopleForContacts:completion:]
+ -[DSXPCSharingPermissions _sharingPeopleForIdentities:completion:]
+ -[DSXPCSharingPermissions sharingPeopleForContacts:completion:]
+ -[DSXPCSharingPermissions sharingPeopleForIdentities:completion:]
+ GCC_except_table16
+ GCC_except_table23
+ GCC_except_table27
+ _NSLocalizedFailureReasonErrorKey
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.76
+ ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.76.cold.1
+ ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.cold.1
+ ___63-[DSXPCSharingPermissions sharingPeopleForContacts:completion:]_block_invoke
+ ___64-[DSXPCSharingPermissions _sharingPeopleForContacts:completion:]_block_invoke
+ ___64-[DSXPCSharingPermissions _sharingPeopleForContacts:completion:]_block_invoke.cold.1
+ ___65-[DSXPCSharingPermissions sharingPeopleForIdentities:completion:]_block_invoke
+ ___66-[DSXPCSharingPermissions _sharingPeopleForIdentities:completion:]_block_invoke
+ ___68-[DSXPCSharingPermissions stopSharingSources:withPerson:completion:]_block_invoke.16
+ ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke.15
+ ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke.15.cold.1
+ ___block_descriptor_56_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_literal_global.75
+ _objc_msgSend$_sharingPeopleForContacts:completion:
+ _objc_msgSend$_sharingPeopleForIdentities:completion:
+ _objc_msgSend$cachedFetchError
+ _objc_msgSend$makeSharingPeople
+ _objc_msgSend$reason
- -[DSXPCSharingPermissions _fetchSharingWithCompletion:].cold.1
- -[DSXPCSharingPermissions sharingPeopleForContacts:]
- -[DSXPCSharingPermissions sharingPeopleForContacts:].cold.1
- -[DSXPCSharingPermissions sharingPeopleForIdentities:]
- GCC_except_table18
- GCC_except_table26
- _OBJC_IVAR_$_DSXPCSharingPermissions._dispatchGroup
- ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.77
- ___37-[DSXPCSharingPermissions connectXPC]_block_invoke.77.cold.1
- ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.8.cold.1
- ___55-[DSXPCSharingPermissions _fetchSharingWithCompletion:]_block_invoke.9
- ___68-[DSXPCSharingPermissions stopSharingSources:withPerson:completion:]_block_invoke.17
- ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke.16
- ___97-[DSXPCSharingPermissions addSharingPerson:participant:forSource:sharedResource:deviceOwnerRole:]_block_invoke.16.cold.1
- ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8ls32l8w40l8
- ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
- ___block_literal_global.76
- _dispatch_group_wait
- _dispatch_queue_attr_make_with_qos_class
- _dispatch_time
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "Retaining fetched shared resources and removing people objects"
+ "_sharingPeopleForContacts:completion:"
+ "_sharingPeopleForIdentities:completion:"
+ "errorWithException:"
+ "reason"
+ "sharingPeopleForContacts:completion:"
+ "sharingPeopleForIdentities:completion:"
- "@\"NSObject<OS_dispatch_group>\""
- "Failed fetchSharedResource call due to timeout"
- "_dispatchGroup"
- "sharingPeopleForContacts:"
- "sharingPeopleForIdentities:"

```
