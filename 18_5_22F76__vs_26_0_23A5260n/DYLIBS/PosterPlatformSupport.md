## PosterPlatformSupport

> `/System/Library/PrivateFrameworks/PosterPlatformSupport.framework/PosterPlatformSupport`

```diff

-228.5.12.0.0
-  __TEXT.__text: 0x2174
-  __TEXT.__auth_stubs: 0x330
+276.105.0.0.0
+  __TEXT.__text: 0x2014
+  __TEXT.__auth_stubs: 0x320
   __TEXT.__objc_methlist: 0x1c8
   __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x78
-  __TEXT.__cstring: 0x1f9
-  __TEXT.__oslogstring: 0x4d7
-  __TEXT.__unwind_info: 0xf0
+  __TEXT.__gcc_except_tab: 0x40
+  __TEXT.__cstring: 0x1ff
+  __TEXT.__oslogstring: 0x3fe
+  __TEXT.__unwind_info: 0xe8
   __TEXT.__objc_classname: 0x69
-  __TEXT.__objc_methname: 0x854
-  __TEXT.__objc_methtype: 0x1d8
-  __TEXT.__objc_stubs: 0x620
-  __DATA_CONST.__got: 0xa8
-  __DATA_CONST.__const: 0xe8
+  __TEXT.__objc_methname: 0x8b8
+  __TEXT.__objc_methtype: 0x198
+  __TEXT.__objc_stubs: 0x680
+  __DATA_CONST.__got: 0x90
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x218
+  __DATA_CONST.__objc_selrefs: 0x230
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x1a8
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x1a0
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x300
-  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x1c
   __DATA.__data: 0x60
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/PosterFoundation.framework/PosterFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 011683B0-2C98-370E-A27C-12DE4AE05E70
-  Functions: 63
-  Symbols:   305
-  CStrings:  156
+  UUID: 874148D8-40C5-3942-B47A-C4A0F33F485B
+  Functions: 62
+  Symbols:   308
+  CStrings:  155
 
Symbols:
+ -[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:]
+ -[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:].cold.1
+ -[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:]
+ -[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:].cold.1
+ -[PPSHostConfigurationManager updatedSwitcherConfigurationForRole:currentSwitcherConfiguration:error:]
+ GCC_except_table17
+ _OBJC_CLASS_$_PRSHostConfigurationEntry
+ _PFFeatureEnabled
+ ___102-[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:]_block_invoke
+ ___102-[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:]_block_invoke.8
+ ___102-[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:]_block_invoke.8.cold.1
+ ___102-[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:]_block_invoke.cold.1
+ ___102-[PPSHostConfigurationManager updatedSwitcherConfigurationForRole:currentSwitcherConfiguration:error:]_block_invoke
+ ___99-[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:]_block_invoke
+ ___99-[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:]_block_invoke.16
+ ___99-[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:]_block_invoke.16.cold.1
+ ___99-[PPSHostConfigurationManager _lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:]_block_invoke.cold.1
+ ___block_descriptor_32_e35_16?0"PRSHostConfigurationEntry"8l
+ ___block_literal_global.43
+ _objc_msgSend$_lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:
+ _objc_msgSend$_lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:
+ _objc_msgSend$bs_compactMap:
+ _objc_msgSend$descriptorID
+ _objc_msgSend$entries
+ _objc_msgSend$entryWithExtensionID:descriptorID:
+ _objc_msgSend$extensionID
+ _objc_msgSend$hostConfigurationForBundleAtURL:currentSwitcherConfiguration:forRole:completion:
+ _objc_msgSend$hostConfigurationWithConfigurationEntries:
+ _objc_msgSend$switcherConfigurationForBundleAtURL:currentSwitcherConfiguration:forRole:completion:
- -[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:]
- -[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:].cold.1
- -[PPSHostConfigurationManager _lock_updatedPosterConfigurationsForRole:currentHostConfiguration:error:]
- -[PPSHostConfigurationManager updatedPosterConfigurationsForRole:currentHostConfiguration:error:]
- GCC_except_table16
- _OBJC_CLASS_$_NSArray
- _OBJC_CLASS_$_NSOrderedSet
- _OBJC_CLASS_$_NSSet
- _OBJC_CLASS_$_NSUUID
- ___103-[PPSHostConfigurationManager _lock_updatedPosterConfigurationsForRole:currentHostConfiguration:error:]_block_invoke
- ___103-[PPSHostConfigurationManager _lock_updatedPosterConfigurationsForRole:currentHostConfiguration:error:]_block_invoke.13
- ___103-[PPSHostConfigurationManager _lock_updatedPosterConfigurationsForRole:currentHostConfiguration:error:]_block_invoke.13.cold.1
- ___103-[PPSHostConfigurationManager _lock_updatedPosterConfigurationsForRole:currentHostConfiguration:error:]_block_invoke.cold.1
- ___73-[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:]_block_invoke
- ___73-[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:]_block_invoke.8
- ___73-[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:]_block_invoke.8.cold.1
- ___73-[PPSHostConfigurationManager _lock_loadBundledHostConfigurationForRole:]_block_invoke.cold.1
- ___block_descriptor_56_e8_32s40r48r_e17_v16?0"NSError"8ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8s32l8r48l8
- _objc_msgSend$_lock_loadBundledHostConfigurationForRole:
- _objc_msgSend$_lock_updatedPosterConfigurationsForRole:currentHostConfiguration:error:
- _objc_msgSend$hostConfigurationForBundleAtURL:forRole:completion:
- _objc_msgSend$orderedSetWithArray:
- _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
- _objc_msgSend$setWithObjects:
- _objc_msgSend$updatedPosterConfigurationsForBundleAtURL:currentHostConfiguration:forRole:completion:
- _objc_retain_x23
- _objc_retain_x24
CStrings:
+ "@16@?0@\"PRSHostConfigurationEntry\"8"
+ "@32@0:8@16@24"
+ "_lock_loadBundledHostConfigurationForRole:currentSwitcherConfiguration:"
+ "_lock_loadSwitcherConfigurationForRole:currentSwitcherConfiguration:"
+ "bs_compactMap:"
+ "descriptorID"
+ "entries"
+ "entryWithExtensionID:descriptorID:"
+ "extensionID"
+ "hostConfigurationForBundleAtURL:currentSwitcherConfiguration:forRole:completion:"
+ "hostConfigurationWithConfigurationEntries:"
+ "switcherConfigurationForBundleAtURL:currentSwitcherConfiguration:forRole:completion:"
+ "updatedSwitcherConfigurationForRole"
+ "updatedSwitcherConfigurationForRole:currentSwitcherConfiguration:error:"
+ "v48@0:8@\"NSURL\"16@\"PRSHostConfiguration\"24@\"NSString\"32@?<v@?@\"PRSHostConfiguration\"@\"NSError\">40"
- "Connection failed updating poster configurations for role %{public}@: %{public}@"
- "Failed updating poster configurations for role %{public}@: %{public}@"
- "Updated poster configurations for role %{public}@   to: %{public}@"
- "_lock_loadBundledHostConfigurationForRole:"
- "_lock_updatedPosterConfigurationsForRole:currentHostConfiguration:error:"
- "hostConfigurationForBundleAtURL:forRole:completion:"
- "orderedSetWithArray:"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setWithObjects:"
- "updatedPosterConfigurationsForBundleAtURL:currentHostConfiguration:forRole:completion:"
- "updatedPosterConfigurationsForRole"
- "updatedPosterConfigurationsForRole:currentHostConfiguration:error:"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v40@0:8@\"NSURL\"16@\"NSString\"24@?<v@?@\"PRSHostConfiguration\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSURL\"16@\"PRSHostConfiguration\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"

```
