## GameCenterFoundation

> `/System/Library/PrivateFrameworks/GameCenterFoundation.framework/GameCenterFoundation`

```diff

-821.1.8.0.0
-  __TEXT.__text: 0x16b264
-  __TEXT.__objc_methlist: 0x12614
-  __TEXT.__cstring: 0x19190
+821.1.16.0.0
+  __TEXT.__text: 0x16ba48
+  __TEXT.__objc_methlist: 0x1263c
+  __TEXT.__cstring: 0x192b0
   __TEXT.__const: 0x6608
-  __TEXT.__gcc_except_tab: 0x12dc
-  __TEXT.__oslogstring: 0xdf4b
+  __TEXT.__gcc_except_tab: 0x12f4
+  __TEXT.__oslogstring: 0xe0eb
   __TEXT.__ustring: 0x18
   __TEXT.__dlopen_cstrs: 0xba
   __TEXT.__swift5_typeref: 0x2062

   __TEXT.__swift_as_ret: 0x1dc
   __TEXT.__swift_as_cont: 0x3f4
   __TEXT.__swift5_mpenum: 0x48
-  __TEXT.__unwind_info: 0x80d0
-  __TEXT.__eh_frame: 0x5968
+  __TEXT.__unwind_info: 0x8120
+  __TEXT.__eh_frame: 0x59f0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x61d8
+  __DATA_CONST.__const: 0x6218
   __DATA_CONST.__objc_classlist: 0x828
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x230
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8588
+  __DATA_CONST.__objc_selrefs: 0x85a0
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_arraydata: 0x280
-  __DATA_CONST.__got: 0x1120
-  __AUTH_CONST.__const: 0x6d28
-  __AUTH_CONST.__cfstring: 0x11640
-  __AUTH_CONST.__objc_const: 0x24cd8
+  __DATA_CONST.__got: 0x1118
+  __AUTH_CONST.__const: 0x6d48
+  __AUTH_CONST.__cfstring: 0x11680
+  __AUTH_CONST.__objc_const: 0x24d08
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__auth_got: 0x1560
   __AUTH.__objc_data: 0x2c30
   __AUTH.__data: 0x1088
-  __DATA.__objc_ivar: 0xfd4
-  __DATA.__data: 0x3a60
+  __DATA.__objc_ivar: 0xfd8
+  __DATA.__data: 0x3a58
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x2c40
-  __DATA_DIRTY.__data: 0x748
-  __DATA_DIRTY.__bss: 0xe20
+  __DATA_DIRTY.__data: 0x758
+  __DATA_DIRTY.__bss: 0xf30
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11343
-  Symbols:   12465
-  CStrings:  4213
+  Functions: 11358
+  Symbols:   12478
+  CStrings:  4222
 
Symbols:
+ -[GKMatch handleUnresolvedConnectedPlayersWithCompletion:]
+ -[GKMatch pendingPlayerIdentityResolutionGroup]
+ -[GKMatch setPendingPlayerIdentityResolutionGroup:]
+ GCC_except_table160
+ GCC_except_table167
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table179
+ GCC_except_table181
+ GCC_except_table188
+ _GKOverlayBundleIDs
+ _GKOverlayBundleIDs.onceToken
+ _GKOverlayBundleIDs.sOverlayBundleIDs
+ _OBJC_IVAR_$_GKMatch._pendingPlayerIdentityResolutionGroup
+ ___58-[GKMatch handleUnresolvedConnectedPlayersWithCompletion:]_block_invoke
+ ___58-[GKMatch handleUnresolvedConnectedPlayersWithCompletion:]_block_invoke_2
+ ___GKOverlayBundleIDs_block_invoke
+ ___block_descriptor_48_e8_32bs40r_e5_v8?0lr40l8s32l8
+ _kUnshippedOverlayBundleIDs
- GCC_except_table164
- GCC_except_table168
- GCC_except_table170
- GCC_except_table172
- GCC_except_table176
- GCC_except_table178
- GCC_except_table185
CStrings:
+ "%@ (completion != ((void*)0))\n[%s (%s:%d)]"
+ "-[GKMatch handleUnresolvedConnectedPlayersWithCompletion:]"
+ "GKLocalPlayer.setInternal: nil write, substituting unauthenticated sentinel as this                     violates a class invariant. Stack trace:%@"
+ "Y29tLmFwcGxlLkdhbWVMYXllclVJ"
+ "Y29tLmFwcGxlLkdhbWVMYXllclVJLlNvbW1lbGllcg=="
+ "Y29tLmFwcGxlLkdhbWVPdmVybGF5VUkuR2FtZUNlbnRlckV4dGVuc2lvbg=="
+ "com.apple.gamecenter.match.pendingplayeridentityresolution"
+ "handleUnresolvedConnectedPlayersWithCompletion: timed out after %.1fs waiting for player identity resolution, proceeding with a possibly-incomplete roster"
+ "handleUnresolvedConnectedPlayersWithCompletion: waiting up to %.1fs for any in-flight player identity resolution"
```
