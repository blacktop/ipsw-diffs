## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/Versions/A/TVRemoteCore`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_imageinfo`

```diff

-627.0.28.0.0
-  __TEXT.__text: 0x4bc24
-  __TEXT.__objc_methlist: 0x63a8
-  __TEXT.__const: 0x230
-  __TEXT.__cstring: 0x3627
-  __TEXT.__gcc_except_tab: 0xb1c
-  __TEXT.__oslogstring: 0x6697
-  __TEXT.__unwind_info: 0x11f0
+627.10.51.0.0
+  __TEXT.__text: 0x4c5dc
+  __TEXT.__objc_methlist: 0x6748
+  __TEXT.__const: 0x242
+  __TEXT.__cstring: 0x36ac
+  __TEXT.__gcc_except_tab: 0xb68
+  __TEXT.__oslogstring: 0x68bb
+  __TEXT.__unwind_info: 0x1218
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x910
+  __DATA_CONST.__const: 0x960
   __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f90
+  __DATA_CONST.__objc_selrefs: 0x3238
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x208
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__got: 0x4a0
-  __AUTH_CONST.__const: 0x1300
-  __AUTH_CONST.__cfstring: 0x49a0
-  __AUTH_CONST.__objc_const: 0x9d90
+  __AUTH_CONST.__const: 0x1360
+  __AUTH_CONST.__cfstring: 0x4a80
+  __AUTH_CONST.__objc_const: 0xa028
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x1860
-  __DATA.__objc_ivar: 0x690
-  __DATA.__data: 0x9d0
+  __DATA.__objc_ivar: 0x698
+  __DATA.__data: 0xa30
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x160
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2154
-  Symbols:   4739
-  CStrings:  1266
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  Functions: 2168
+  Symbols:   4797
+  CStrings:  1280
 
Symbols:
+ -[TVRCHMHomeObserver _isAtHome]
+ -[TVRCHMHomeObserver homeDidUpdateHomeLocationStatus:]
+ -[TVRCRPCompanionLinkClientWrapper _finishInvalidatingWithCompletionHandler:]
+ -[TVRCRPCompanionLinkClientWrapper _updateFindMyRemoteSupport]
+ -[TVRCRPCompanionLinkClientWrapper activating]
+ -[TVRCRPCompanionLinkClientWrapper setActivating:]
+ -[TVRCSiriRemoteInfo productID]
+ -[TVRCSiriRemoteInfo setProductID:]
+ -[TVRCXPCClient _beginDeviceQueryWithResponse:]
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table109
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table125
+ GCC_except_table145
+ GCC_except_table151
+ GCC_except_table157
+ GCC_except_table164
+ GCC_except_table171
+ GCC_except_table24
+ GCC_except_table46
+ GCC_except_table55
+ GCC_except_table65
+ OBJC_IVAR_$_TVRCRPCompanionLinkClientWrapper._activating
+ OBJC_IVAR_$_TVRCSiriRemoteInfo._productID
+ _GestaltGetDeviceClass
+ _HMStringFromHomeLocation
+ _TVRCMessageKeyGroupRenderingMode
+ _TVRCRequestIDSurroundGetGroupRenderingMode
+ _TVRCRequestIDSurroundSetGroupRenderingMode
+ __47-[TVRCXPCClient _beginDeviceQueryWithResponse:]_block_invoke
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMHomeDelegatePrivate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMHomeDelegatePrivate
+ __OBJC_$_PROTOCOL_REFS_HMHomeDelegatePrivate
+ __OBJC_LABEL_PROTOCOL_$_HMHomeDelegatePrivate
+ __OBJC_PROTOCOL_$_HMHomeDelegatePrivate
+ ___47-[TVRCXPCClient _beginDeviceQueryWithResponse:]_block_invoke
+ ___block_descriptor_48_e8_32bs40r_e8_v12?0B8l
+ ___block_descriptor_48_e8_32w40w_e5_v8?0l
+ ___copy_helper_block_e8_32b40r
+ ___copy_helper_block_e8_32w40w
+ ___destroy_helper_block_e8_32w40w
+ ___swift_reflection_version
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_TVRemoteCore
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_TVRemoteCore
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_TVRemoteCore
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_TVRemoteCore
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_TVRemoteCore
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_TVRemoteCore
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_TVRemoteCore
+ _objc_msgSend$_beginDeviceQueryWithResponse:
+ _objc_msgSend$_finishInvalidatingWithCompletionHandler:
+ _objc_msgSend$_isAtHome
+ _objc_msgSend$_updateFindMyRemoteSupport
+ _objc_msgSend$activating
+ _objc_msgSend$appendUnsignedInteger:withName:format:
+ _objc_msgSend$deletionCount
+ _objc_msgSend$forwardDeletionCount
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$homeLocationStatus
+ _objc_msgSend$insertionText
+ _objc_msgSend$keyboardOutput
+ _objc_msgSend$productID
+ _objc_msgSend$setActivating:
+ _objc_msgSend$setProductID:
+ _objc_msgSend$textOperations
+ _objc_msgSend$unsignedIntValue
- GCC_except_table100
- GCC_except_table102
- GCC_except_table104
- GCC_except_table110
- GCC_except_table114
- GCC_except_table120
- GCC_except_table130
- GCC_except_table146
- GCC_except_table152
- GCC_except_table159
- GCC_except_table16
- GCC_except_table166
- GCC_except_table37
- GCC_except_table47
- GCC_except_table50
- GCC_except_table61
- GCC_except_table96
- GCC_except_table98
- __46-[TVRCXPCClient beginDeviceQueryWithResponse:]_block_invoke
CStrings:
+ "AppleTV18"
+ "CompanionClient is already activating %@"
+ "CompanionLinkClient is currently invalidating. Queuing request until after invalidation %@"
+ "Executing queued connection request %@"
+ "Find my remote support level for %@: %@, device capability: %{bool}d, paired remote support: %{bool}d, paired remote productID: %@"
+ "HomeKit informed us that the home location status for home %{public}@ is now %{public}@"
+ "Ignoring activation from a replaced companionLinkClient. Error - %@ %@"
+ "Ignoring invalidation from a replaced companionLinkClient %@"
+ "Ignoring location status update for a home we are not observing"
+ "Keyboard RemoteTextInput send operation - insert length:%lu deleteBackward:%lu forwardDelete:%lu"
+ "Skipping accessory %{public}@ because we are away from home"
+ "SurroundGetGroupRenderingMode"
+ "SurroundSetGroupRenderingMode"
+ "activating"
+ "audio.GroupRenderingMode"
+ "isInvalidating"
+ "productID"
- "Executing queued connection request"
- "Find my remote support level for %@: %@, device capability: %{bool}d, paired remote support: %{bool}d"
- "Keyboard RemoteTextInput send payload string length: %lu"
```
