## ContactsFoundation

> `/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation`

```diff

 1430.200.41.0.0
-  __TEXT.__text: 0x96748
-  __TEXT.__objc_methlist: 0xac0c
-  __TEXT.__cstring: 0x7224
+  __TEXT.__text: 0x969f4
+  __TEXT.__objc_methlist: 0xac1c
+  __TEXT.__cstring: 0x7264
   __TEXT.__const: 0x1370
   __TEXT.__oslogstring: 0x28f8
-  __TEXT.__gcc_except_tab: 0x122c
+  __TEXT.__gcc_except_tab: 0x123c
   __TEXT.__ustring: 0x514
-  __TEXT.__dlopen_cstrs: 0x117
+  __TEXT.__dlopen_cstrs: 0x167
   __TEXT.__swift5_typeref: 0x84a
   __TEXT.__constg_swiftt: 0x7e8
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_capture: 0x398
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x4960
+  __TEXT.__unwind_info: 0x4978
   __TEXT.__eh_frame: 0xa58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x38f8
+  __DATA_CONST.__const: 0x3910
   __DATA_CONST.__objc_classlist: 0xac0
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4c08
+  __DATA_CONST.__objc_selrefs: 0x4c10
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x9c90

   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3b98
   __DATA_DIRTY.__data: 0x320
-  __DATA_DIRTY.__bss: 0x5f0
+  __DATA_DIRTY.__bss: 0x5f8
   __DATA_DIRTY.__common: 0x28
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 5266
-  Symbols:   8758
-  CStrings:  1914
+  Functions: 5269
+  Symbols:   8764
+  CStrings:  1917
 
Symbols:
+ -[CNFeatureFlags isUIKitEnhancedLandscapeEnabled]
+ _UIKitCoreLibraryCore.frameworkLibrary
+ ___UIKitCoreLibraryCore_block_invoke
+ ___get_UIEnhancedLandscapeEnabledSymbolLoc_block_invoke
+ _audit_stringUIKitCore
+ _get_UIEnhancedLandscapeEnabledSymbolLoc.ptr
Functions:
~ -[CNFeatureFlags isFeatureEnabled:] : 928 -> 968
+ -[CNFeatureFlags isUIKitEnhancedLandscapeEnabled]
+ ___get_UIEnhancedLandscapeEnabledSymbolLoc_block_invoke
+ ___UIKitCoreLibraryCore_block_invoke
+ -[CNLaunchServicesLocalAdapter getDefaultAppProxyFromTU].cold.1
- -[CNLaunchServicesLocalAdapter getDefaultAppProxyFromTU].cold.1
CStrings:
+ "_UIEnhancedLandscapeEnabled"
+ "enhanced_landscape_contacts"
+ "softlink:r:path:/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore"
```
