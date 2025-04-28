## Sharing

> `/System/Library/PrivateFrameworks/Sharing.framework/Sharing`

```diff

-2060.60.31.0.0
-  __TEXT.__text: 0x2d56ec
+2060.60.41.2.3
+  __TEXT.__text: 0x2d53d0
   __TEXT.__auth_stubs: 0x4790
-  __TEXT.__objc_methlist: 0x13924
+  __TEXT.__objc_methlist: 0x13904
   __TEXT.__const: 0x1aaa4
-  __TEXT.__cstring: 0x39e96
+  __TEXT.__cstring: 0x39da6
   __TEXT.__gcc_except_tab: 0x31e0
   __TEXT.__oslogstring: 0x89fe
   __TEXT.__dlopen_cstrs: 0x536

   __TEXT.__swift_as_entry: 0x2e0
   __TEXT.__swift_as_ret: 0x2e0
   __TEXT.__swift5_mpenum: 0xa8
-  __TEXT.__unwind_info: 0xc548
+  __TEXT.__unwind_info: 0xc550
   __TEXT.__eh_frame: 0xabb0
   __TEXT.__objc_classname: 0x1e15
-  __TEXT.__objc_methname: 0x2bf0d
+  __TEXT.__objc_methname: 0x2be84
   __TEXT.__objc_methtype: 0x5ac1
-  __TEXT.__objc_stubs: 0x183e0
+  __TEXT.__objc_stubs: 0x18360
   __DATA_CONST.__got: 0x1130
-  __DATA_CONST.__const: 0x6b50
+  __DATA_CONST.__const: 0x6b30
   __DATA_CONST.__objc_classlist: 0x800
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x380
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9290
+  __DATA_CONST.__objc_selrefs: 0x9270
   __DATA_CONST.__objc_protorefs: 0x1c0
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x538
   __DATA_CONST.__objc_arraydata: 0x478
   __AUTH_CONST.__auth_got: 0x23e0
-  __AUTH_CONST.__auth_ptr: 0xf08
-  __AUTH_CONST.__const: 0x10920
-  __AUTH_CONST.__cfstring: 0x132a0
-  __AUTH_CONST.__objc_const: 0x354a0
+  __AUTH_CONST.__auth_ptr: 0xf28
+  __AUTH_CONST.__const: 0x10900
+  __AUTH_CONST.__cfstring: 0x13260
+  __AUTH_CONST.__objc_const: 0x35470
   __AUTH_CONST.__objc_intobj: 0x618
   __AUTH_CONST.__objc_dictobj: 0x640
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH.__objc_data: 0x20b8
   __AUTH.__data: 0x1808
-  __DATA.__objc_ivar: 0x2520
+  __DATA.__objc_ivar: 0x251c
   __DATA.__data: 0xb9b8
   __DATA.__bss: 0x31b30
   __DATA.__common: 0xb0

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 19861
-  Symbols:   36989
-  CStrings:  17091
+  Functions: 19855
+  Symbols:   36969
+  CStrings:  17077
 
Symbols:
+ -[SFRemoteHotspotDevice lastSeen]
+ -[SFRemoteHotspotDevice setLastSeen:]
+ GCC_except_table155
+ GCC_except_table162
+ _OBJC_IVAR_$_SFRemoteHotspotDevice._lastSeen
+ _SFIsClassroomEnabled
+ ___block_literal_global.273
+ ___block_literal_global.275
+ ___block_literal_global.280
+ ___block_literal_global.290
+ ___block_literal_global.295
+ ___block_literal_global.301
+ ___block_literal_global.349
+ ___block_literal_global.397
+ _objc_msgSend$isClassroomEnabled
- -[SFPasswordSharingInfo emailHash]
- -[SFPasswordSharingInfo phoneHash]
- -[SFPasswordSharingInfo setEmailHash:]
- -[SFPasswordSharingInfo setPhoneHash:]
- -[SFPasswordSharingService _handleReceivedPassword:].cold.6
- -[SFPasswordSharingService _handleReceivedPassword:].cold.7
- -[SFPasswordSharingService _resolveContactForPeerInfo:]
- GCC_except_table154
- GCC_except_table159
- GCC_except_table161
- _OBJC_IVAR_$_SFPasswordSharingInfo._emailHash
- _OBJC_IVAR_$_SFPasswordSharingInfo._phoneHash
- ___55-[SFPasswordSharingService _resolveContactForPeerInfo:]_block_invoke
- ___55-[SFPasswordSharingService _resolveContactForPeerInfo:]_block_invoke.cold.1
- ___block_descriptor_32_e30_v24?0"NSString"8"NSError"16l
- ___block_literal_global.230
- ___block_literal_global.272
- ___block_literal_global.274
- ___block_literal_global.281
- ___block_literal_global.289
- ___block_literal_global.294
- ___block_literal_global.300
- ___block_literal_global.331
- ___block_literal_global.396
- _objc_msgSend$_resolveContactForPeerInfo:
- _objc_msgSend$emailHash
- _objc_msgSend$phoneHash
- _objc_msgSend$setEmailHash:
- _objc_msgSend$setPhoneHash:
CStrings:
+ "isClassroomEnabled"
- "### No emailHash?\n"
- "### No phoneHash?\n"
- "-[SFPasswordSharingService _resolveContactForPeerInfo:]_block_invoke"
- "T@\"NSString\",&,N,V_emailHash"
- "T@\"NSString\",&,N,V_phoneHash"
- "WiFiPasswordSharing remote peer is a mutual contact: #@.\n"
- "_emailHash"
- "_phoneHash"
- "_resolveContactForPeerInfo:"
- "com.apple.sharing.WiFiPasswordSharing.MutualContact"
- "emailHash"
- "phoneHash"
- "providerIsContact"
- "setEmailHash:"
- "setPhoneHash:"

```
