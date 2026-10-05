## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4637.1.8.101.0
-  __TEXT.__text: 0xace348
+4637.1.12.101.0
+  __TEXT.__text: 0xacef7c
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xbe040
+  __TEXT.__objc_methlist: 0xbe090
   __TEXT.__const: 0x11360
-  __TEXT.__oslogstring: 0x658b2
-  __TEXT.__cstring: 0x8544f
-  __TEXT.__gcc_except_tab: 0x1864c
+  __TEXT.__oslogstring: 0x659af
+  __TEXT.__cstring: 0x855ed
+  __TEXT.__gcc_except_tab: 0x186e4
   __TEXT.__ustring: 0xd04
   __TEXT.__dlopen_cstrs: 0x373
-  __TEXT.__unwind_info: 0x39ed0
+  __TEXT.__unwind_info: 0x39ef8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1da60
+  __DATA_CONST.__const: 0x1da68
   __DATA_CONST.__objc_classlist: 0x54f8
   __DATA_CONST.__objc_catlist: 0x338
   __DATA_CONST.__objc_nlcatlist: 0x8
   __DATA_CONST.__objc_protolist: 0x2ae0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4eb20
+  __DATA_CONST.__objc_selrefs: 0x4eb60
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x40a0
   __DATA_CONST.__objc_arraydata: 0x18b8
   __DATA_CONST.__got: 0xa980
   __AUTH_CONST.__const: 0x10c48
-  __AUTH_CONST.__cfstring: 0x74ca0
+  __AUTH_CONST.__cfstring: 0x74d80
   __AUTH_CONST.__objc_const: 0x288dd8
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1740

   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH_CONST.__auth_got: 0x2c00
   __AUTH.__objc_data: 0xd840
-  __DATA.__objc_ivar: 0xfca8
+  __DATA.__objc_ivar: 0xfca4
   __DATA.__data: 0x20f80
   __DATA.__common: 0xa40
   __DATA_DIRTY.__objc_data: 0x27970

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 73627
-  Symbols:   119477
-  CStrings:  23575
+  Functions: 73638
+  Symbols:   119483
+  CStrings:  23587
 
Symbols:
+ -[SBAppPlatterDragPreview pendingIconViewListLayoutProvider]
+ -[SBAppPlatterDragPreview setPendingIconViewListLayoutProvider:]
+ -[SBApplication(Identity) isFindMyFindingUI]
+ -[SBFluidSwitcherGestureManager gestureRecognizer:shouldReceiveEvent:]
+ -[SBHomeScreenService replaceApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:options:]
+ -[SBHomeScreenService swapApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]
+ GCC_except_table159
+ _OBJC_IVAR_$_SBAppPlatterDragPreview._pendingIconViewListLayoutProvider
+ _SBFindingUIAngelBundleIdentifier
+ ___block_descriptor_48_e8_32s40r_e33_B16?0"FBSDisplayLayoutElement"8ls32l8r40l8
+ ___block_descriptor_56_e8_32s40r48r_e25_v28?0"NSString"8i16^B20lr40l8r48l8s32l8
+ ___block_descriptor_67_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- GCC_except_table133
- _OBJC_IVAR_$_SBTransitionSwitcherModifier._fromAppLayout
- _OBJC_IVAR_$_SBTransitionSwitcherModifier._toAppLayout
- ___block_descriptor_40_e8_32r_e25_v28?0"NSString"8i16^B20lr32l8
- ___block_descriptor_40_e8_32s_e33_B16?0"FBSDisplayLayoutElement"8ls32l8
- ___block_descriptor_59_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
CStrings:
+ "%@ has a scene hosted by SpringBoard"
+ "%@ is on screen"
+ "%@ is presenting a remote alert"
+ "-[SBHomeScreenService replaceApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:options:]"
+ "-[SBHomeScreenService swapApplicationIconsWithBundleIdentifier:withApplicationIconsWithBundleIdentifier:]"
+ "Alert restriction: allowing %{public}@ to appear over %{public}@ because %{public}@."
+ "Drop cancelled but the platter's icon view could not be snapshotted; keeping the icon image view controller: %@"
+ "Error preparing for app replacement source lookup: %@"
+ "Not sending status bar tap to %{public}@: scene isn't active"
+ "Restricted to only appear over %@, and what is on screen is %@"
+ "com.apple.findmy.FindingUIAngel"
+ "display layout contains \"%@\", matching %@"
+ "homescreen is showing"
+ "no app"
- "Restricted to only appear over the following bundle ids: %@"
- "[ContainerBundleIdentifier debugging] checking widget = %@"
```
