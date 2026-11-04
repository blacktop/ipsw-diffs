## AppSystemSettingsUI

> `/System/Library/PrivateFrameworks/AppSystemSettingsUI.framework/AppSystemSettingsUI`

```diff

-2027.1.5.0.0
-  __TEXT.__text: 0x25db8
-  __TEXT.__objc_methlist: 0xd9c
+2027.2.1.0.0
+  __TEXT.__text: 0x26e88
+  __TEXT.__objc_methlist: 0xdbc
   __TEXT.__const: 0xe18
-  __TEXT.__gcc_except_tab: 0x3a4
-  __TEXT.__cstring: 0x26ec
-  __TEXT.__oslogstring: 0xa75
+  __TEXT.__gcc_except_tab: 0x3fc
+  __TEXT.__cstring: 0x27bc
+  __TEXT.__oslogstring: 0xac5
   __TEXT.__ustring: 0x2f6
-  __TEXT.__dlopen_cstrs: 0x5e
+  __TEXT.__dlopen_cstrs: 0xa7
   __TEXT.__constg_swiftt: 0x36c
   __TEXT.__swift5_typeref: 0xc8c
   __TEXT.__swift5_reflstr: 0x2d7

   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x60
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__unwind_info: 0xc60
+  __TEXT.__unwind_info: 0xc90
   __TEXT.__eh_frame: 0x900
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x620
+  __DATA_CONST.__const: 0x638
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfc0
+  __DATA_CONST.__objc_selrefs: 0x1000
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x768
   __AUTH_CONST.__const: 0x890
-  __AUTH_CONST.__cfstring: 0x16e0
+  __AUTH_CONST.__cfstring: 0x1700
   __AUTH_CONST.__objc_const: 0x18c0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 773
-  Symbols:   1085
-  CStrings:  357
+  Functions: 789
+  Symbols:   1097
+  CStrings:  365
 
Symbols:
+ -[AUSystemSettingsSpecifiersProvider(Health) hasRequestedHealthAuthorization]
+ GCC_except_table168
+ _HealthKitLibrary
+ _HealthKitLibraryCore.frameworkLibrary
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_INSTANCE_METHODS_AUSystemSettingsSpecifiersProvider(Health|Internal|AppSystemSettingsUI)
+ ___HealthKitLibraryCore_block_invoke
+ ___getHKAuthorizationStoreClass_block_invoke
+ ___getHKHealthStoreClass_block_invoke
+ _audit_stringHealthKit
+ _getHKAuthorizationStoreClass.softClass
+ _getHKHealthStoreClass.softClass
- __OBJC_$_INSTANCE_METHODS_AUSystemSettingsSpecifiersProvider(Internal|AppSystemSettingsUI)
CStrings:
+ "%{public}s: Failed to fetch Health authorization records for %{public}@: %{public}@"
+ "-[AUSystemSettingsSpecifiersProvider(Health) hasRequestedHealthAuthorization]"
+ "HKAuthorizationStore"
+ "HKHealthStore"
+ "HealthAppAccessSettings"
+ "com.apple.Health"
+ "com.apple.developer.healthkit"
+ "softlink:r:path:/System/Library/Frameworks/HealthKit.framework/HealthKit"
```
