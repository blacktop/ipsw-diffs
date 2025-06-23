## CoreFoundation

> `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

```diff

-4030.1.101.0.0
-  __TEXT.__text: 0x1bda54
+4032.1.0.0.0
+  __TEXT.__text: 0x1bdd4c
   __TEXT.__auth_stubs: 0x31e0
   __TEXT.__init_offsets: 0x4
   __TEXT.__objc_methlist: 0x7a34
-  __TEXT.__const: 0x1a1710
-  __TEXT.__oslogstring: 0x5815
-  __TEXT.__cstring: 0x14b147
+  __TEXT.__const: 0x1a1718
+  __TEXT.__oslogstring: 0x5819
+  __TEXT.__cstring: 0x14b20d
   __TEXT.__gcc_except_tab: 0x44d4
   __TEXT.__ustring: 0x484
   __TEXT.__dof_CFRunLoop: 0x964
   __TEXT.__dof_Cocoa_Aut: 0x486
-  __TEXT.__unwind_info: 0x5800
+  __TEXT.__unwind_info: 0x5810
   __TEXT.__eh_frame: 0x588
   __TEXT.__objc_classname: 0xa9a
   __TEXT.__objc_methname: 0x8323
   __TEXT.__objc_methtype: 0xb399d
   __TEXT.__objc_stubs: 0x6060
   __DATA_CONST.__got: 0x490
-  __DATA_CONST.__const: 0x37d600
+  __DATA_CONST.__const: 0x37d6a0
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_nlclslist: 0x58
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x16e0
   __AUTH_CONST.__auth_got: 0x1908
-  __AUTH_CONST.__const: 0x4d48
-  __AUTH_CONST.__cfstring: 0x1412e0
+  __AUTH_CONST.__const: 0x4d68
+  __AUTH_CONST.__cfstring: 0x141420
   __AUTH_CONST.__objc_const: 0x9ac8
   __AUTH_CONST.__const_cfobj2: 0x40
   __AUTH_CONST.__objc_dictobj: 0x7f8

   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_data: 0x4
   __DATA.__objc_ivar: 0x51c
-  __DATA.__data: 0x6ec
+  __DATA.__data: 0x6f4
   __DATA.__cf_except_bt: 0x2000
   __DATA.__cf_except_pack: 0x410
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x9d8
-  __DATA.__common: 0x98
+  __DATA.__bss: 0x9e8
+  __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x21c0
   __DATA_DIRTY.__data: 0x170
   __DATA_DIRTY.__bss: 0xe60

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4B41978-0DE5-3D20-BF02-C4E2255BEB3F
-  Functions: 7984
-  Symbols:   20427
-  CStrings:  100935
+  UUID: 2A272802-97C0-323E-BFCF-7C7C9232AF79
+  Functions: 7991
+  Symbols:   20453
+  CStrings:  100955
 
Symbols:
+ _CFStringCopyStatisticalWritingDirections
+ _CFStringCopyStatisticalWritingDirections.cold.1
+ __CFBundleMainBundleHasCompatibilityIdentifier
+ __CFBundleMainBundleHasCompatibilityShortVersion
+ __CFGetDirectionalOverridesStrategyForStringStatisticalWritingDirections
+ __CFSetDirectionalOverridesStrategyForStringStatisticalWritingDirections
+ __CFStringGetCStringPtrWithOptions
+ __CFStringHasStrongOrWeakRTL
+ ___CFBundleShortVersionString
+ ___CFStringEncodingCopyNameAsCF
+ ___appendParagraphRangeInfo_block_invoke
+ ___block_literal_global.162
+ ___block_literal_global.199
+ _appendParagraphRangeInfo.onceToken
+ _appendParagraphRangeInfo.sArrayOfStatisticalWritingDirectionParagraphKeys
+ _kCFStatisticalWritingDirectionParagraphInfoHasMixedDirectionality
+ _kCFStatisticalWritingDirectionParagraphInfoLength
+ _kCFStatisticalWritingDirectionParagraphInfoLocation
+ _kCFStatisticalWritingDirectionParagraphInfoNumberOfLeftToRightNumbers
+ _kCFStatisticalWritingDirectionParagraphInfoNumberOfLeftToRightWords
+ _kCFStatisticalWritingDirectionParagraphInfoNumberOfRightToLeftNumbers
+ _kCFStatisticalWritingDirectionParagraphInfoNumberOfRightToLeftWords
+ _kCFStatisticalWritingDirectionParagraphInfoNumberOfWeakNumbers
+ _kCFStatisticalWritingDirectionParagraphInfoNumberOfWeakWords
+ _kCFStatisticalWritingDirectionParagraphInfoWritingDirection
- _CFGetDirectionalOverridesStrategyForStatisticalWritingDirections
- _CFSetDirectionalOverridesStrategyForStatisticalWritingDirections
- __CFStringHasStrongRTL
- ___CFStringEncodingGetNameAsCF
CStrings:
+ "HasMixedDirectionality"
+ "Length"
+ "Location"
+ "NumberOfLeftToRightNumbers"
+ "NumberOfLeftToRightWords"
+ "NumberOfRightToLeftNumbers"
+ "NumberOfRightToLeftWords"
+ "NumberOfWeakNumbers"
+ "NumberOfWeakWords"
+ "Process %{public}d (%{public}s) wrote the key(s) %{private}s in { %{public}s, %{public}s, %{public}s, %{public}s, managed: %d }"
+ "WritingDirection"
+ "rejecting write of key(s) %{private}s in { %{public}s, %{public}s, %{public}s, %{public}s, managed: %d } from process %{public}d (%{public}s) because %{public}s"
+ "writing key %{private}@ in cloud domain %{public}@"
+ "writing key %{private}@ in cloud domain %{public}@ failed with exception %{public}@"
- "Process %{public}d (%{public}s) wrote the key(s) %{public}s in { %{public}s, %{public}s, %{public}s, %{public}s, managed: %d }"
- "rejecting write of key(s) %{public}s in { %{public}s, %{public}s, %{public}s, %{public}s, managed: %d } from process %{public}d (%{public}s) because %{public}s"
- "writing key %{public}@ in cloud domain %{public}@"
- "writing key %{public}@ in cloud domain %{public}@ failed with exception %{public}@"

```
