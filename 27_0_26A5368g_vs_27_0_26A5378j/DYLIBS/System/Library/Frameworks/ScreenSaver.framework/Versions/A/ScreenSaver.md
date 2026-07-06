## ScreenSaver

> `/System/Library/Frameworks/ScreenSaver.framework/Versions/A/ScreenSaver`

```diff

-  __TEXT.__text: 0x11ccc
-  __TEXT.__objc_methlist: 0x19ac
+  __TEXT.__text: 0x13620
+  __TEXT.__objc_methlist: 0x1a14
   __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x200
-  __TEXT.__cstring: 0x2432
-  __TEXT.__oslogstring: 0x1aa0
-  __TEXT.__unwind_info: 0x678
+  __TEXT.__gcc_except_tab: 0x288
+  __TEXT.__cstring: 0x2541
+  __TEXT.__oslogstring: 0x1c2d
+  __TEXT.__unwind_info: 0x6c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x80
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1628
+  __DATA_CONST.__objc_selrefs: 0x1650
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0x340
-  __AUTH_CONST.__const: 0x690
+  __DATA_CONST.__got: 0x348
+  __AUTH_CONST.__const: 0x6b0
   __AUTH_CONST.__cfstring: 0x1880
-  __AUTH_CONST.__objc_const: 0x2330
+  __AUTH_CONST.__objc_const: 0x24d0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x410
-  __DATA.__objc_ivar: 0x164
+  __AUTH.__objc_data: 0x460
+  __DATA.__objc_ivar: 0x180
   __DATA.__data: 0x5b8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x188

   - /System/Library/PrivateFrameworks/login.framework/Versions/A/login
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 584
-  Symbols:   1690
-  CStrings:  642
+  Functions: 597
+  Symbols:   1731
+  CStrings:  655
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[ScreenSaverExtensionModule .cxx_destruct]
+ -[ScreenSaverExtensionModule _extensionInUseTokensDidChange]
+ -[ScreenSaverExtensionModule releaseTokenForView:]
+ -[ScreenSaverExtensionView invalidate]
+ -[ScreenSaverView invalidate]
+ -[_ScreenSaverExtensionInUseToken .cxx_destruct]
+ -[_ScreenSaverExtensionInUseToken beginUsingDidCompleteWithExtension:error:]
+ -[_ScreenSaverExtensionInUseToken dealloc]
+ -[_ScreenSaverExtensionInUseToken debugName]
+ -[_ScreenSaverExtensionInUseToken initWithView:debugName:]
+ -[_ScreenSaverExtensionInUseToken invalidate]
+ -[_ScreenSaverExtensionInUseToken view]
+ GCC_except_table10
+ OBJC_IVAR_$_ScreenSaverExtensionModule._extensionInUseTokens
+ OBJC_IVAR_$_ScreenSaverExtensionView._didInvalidate
+ OBJC_IVAR_$__ScreenSaverExtensionInUseToken._debugName
+ OBJC_IVAR_$__ScreenSaverExtensionInUseToken._extension
+ OBJC_IVAR_$__ScreenSaverExtensionInUseToken._hostInvalidated
+ OBJC_IVAR_$__ScreenSaverExtensionInUseToken._state
+ OBJC_IVAR_$__ScreenSaverExtensionInUseToken._view
+ _OBJC_CLASS_$__ScreenSaverExtensionInUseToken
+ _OBJC_METACLASS_$__ScreenSaverExtensionInUseToken
+ __OBJC_$_INSTANCE_METHODS__ScreenSaverExtensionInUseToken
+ __OBJC_$_INSTANCE_VARIABLES__ScreenSaverExtensionInUseToken
+ __OBJC_$_PROP_LIST__ScreenSaverExtensionInUseToken
+ __OBJC_CLASS_RO_$__ScreenSaverExtensionInUseToken
+ __OBJC_METACLASS_RO_$__ScreenSaverExtensionInUseToken
+ ___45-[_ScreenSaverExtensionInUseToken invalidate]_block_invoke
+ ___76-[_ScreenSaverExtensionInUseToken beginUsingDidCompleteWithExtension:error:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e5_v8?0l
+ ___block_descriptor_40_e8_32w_e21_v16?0"<NSCopying>"8l
+ ___block_descriptor_40_e8_32w_e33_v24?0"<NSCopying>"8"NSArray"16l
+ ___block_descriptor_40_e8_32w_e33_v24?0"<NSCopying>"8"NSError"16l
+ ___block_descriptor_48_e8_32s40bs_e44_v24?0"NSRemoteViewController"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e33_v24?0"<NSCopying>"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs48bs_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48bs_e53_v24?0"ScreenSaverRemoteViewController"8"NSError"16l
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48bs_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48s56bs_e17_v16?0"NSError"8l
+ ___block_descriptor_81_e8_32s40s48s56s64bs_e5_v8?0l
+ ___copy_helper_block_e8_32s
+ ___copy_helper_block_e8_32s40b
+ ___copy_helper_block_e8_32s40b48b
+ ___copy_helper_block_e8_32s40s
+ ___copy_helper_block_e8_32s40s48b
+ ___copy_helper_block_e8_32s40s48s
+ ___copy_helper_block_e8_32s40s48s56b
+ ___copy_helper_block_e8_32s40s48s56s64b
+ ___destroy_helper_block_e8_32s
+ ___destroy_helper_block_e8_32s40s
+ ___destroy_helper_block_e8_32s40s48s
+ ___destroy_helper_block_e8_32s40s48s56s
+ ___destroy_helper_block_e8_32s40s48s56s64s
+ _objc_loadWeakRetained
+ _objc_msgSend$_extensionInUseTokensDidChange
+ _objc_msgSend$beginUsingDidCompleteWithExtension:error:
+ _objc_msgSend$debugName
+ _objc_msgSend$initWithView:debugName:
+ _objc_msgSend$releaseTokenForView:
+ _objc_retainAutorelease
+ _objc_retainAutoreleaseReturnValue
+ _objc_storeStrong
- -[ScreenSaverExtensionManager dealloc]
- -[ScreenSaverExtensionModule dealloc]
- -[ScreenSaverExtensionModule disconnect]
- -[ScreenSaverExtensionModule unloadModule]
- _OUTLINED_FUNCTION_9
- ___40-[ScreenSaverExtensionModule disconnect]_block_invoke
- ___block_descriptor_40_e8_32b_e5_v8?0l
- ___block_descriptor_40_e8_32o_e21_v16?0"<NSCopying>"8l
- ___block_descriptor_40_e8_32o_e33_v24?0"<NSCopying>"8"NSArray"16l
- ___block_descriptor_40_e8_32o_e33_v24?0"<NSCopying>"8"NSError"16l
- ___block_descriptor_41_e8_32o_e5_v8?0l
- ___block_descriptor_48_e8_32o40b_e44_v24?0"NSRemoteViewController"8"NSError"16l
- ___block_descriptor_48_e8_32o40o_e33_v24?0"<NSCopying>"8"NSError"16l
- ___block_descriptor_48_e8_32o40o_e5_v8?0l
- ___block_descriptor_48_e8_32o40w_e5_v8?0l
- ___block_descriptor_56_e8_32o40b48b_e5_v8?0l
- ___block_descriptor_56_e8_32o40o48b_e53_v24?0"ScreenSaverRemoteViewController"8"NSError"16l
- ___block_descriptor_56_e8_32o40o48b_e5_v8?0l
- ___block_descriptor_64_e8_32o40o48b_e5_v8?0l
- ___block_descriptor_64_e8_32o40o48o56b_e5_v8?0l
- ___block_descriptor_65_e8_32o40o48b_e17_v16?0"NSError"8l
- ___block_descriptor_65_e8_32o40o48b_e5_v8?0l
- ___block_descriptor_72_e8_32o40o48o56b_e5_v8?0l
- ___copy_helper_block_e8_32o40b
- ___copy_helper_block_e8_32o40b48b
- ___copy_helper_block_e8_32o40o48b
- ___copy_helper_block_e8_32o40o48o56b
- ___copy_helper_block_e8_32o40w
- ___destroy_helper_block_e8_32b
- ___destroy_helper_block_e8_32o40b
- ___destroy_helper_block_e8_32o40b48b
- ___destroy_helper_block_e8_32o40o48b
- ___destroy_helper_block_e8_32o40o48o56b
- ___destroy_helper_block_e8_32o40w
CStrings:
+ "\f"
+ "%s -- Screen Saver extension view was invalidated twice for: %{public}@"
+ "%s -- The host did not invalidate Screen Saver extension token for: %{public}@"
+ "%s -- The host did not invalidate Screen Saver extension view for: %{public}@"
+ "%s -- Updated token count: %ld for: %{public}@"
+ "%s -- beginUsing: %{public}@"
+ "%s -- beginUsing: completion fired on non-pending token for: %{public}@"
+ "%s -- endUsing: %{public}@"
+ "%s -- endUsing: %{public}@ (host invalidated during begin)"
+ "-[ScreenSaverExtensionModule _extensionInUseTokensDidChange]"
+ "-[ScreenSaverExtensionView dealloc]"
+ "-[ScreenSaverExtensionView invalidate]"
+ "-[_ScreenSaverExtensionInUseToken beginUsingDidCompleteWithExtension:error:]"
+ "-[_ScreenSaverExtensionInUseToken dealloc]"
+ "-[_ScreenSaverExtensionInUseToken invalidate]"
+ "1"
- "%s -- beginUsing “%{public}@”"
- "%s -- endUsing “%{public}@”"
- "-[ScreenSaverExtensionModule disconnect]"

```
