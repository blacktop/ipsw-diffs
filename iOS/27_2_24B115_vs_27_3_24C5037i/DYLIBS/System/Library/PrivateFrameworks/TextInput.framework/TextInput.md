## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/TextInput`

```diff

-3568.1.8.0.0
-  __TEXT.__text: 0x7da78
-  __TEXT.__objc_methlist: 0xb700
+3568.2.4.0.0
+  __TEXT.__text: 0x7dfc4
+  __TEXT.__objc_methlist: 0xb780
   __TEXT.__dlopen_cstrs: 0x459
   __TEXT.__const: 0x4d0
-  __TEXT.__cstring: 0x495ef
+  __TEXT.__cstring: 0x4964b
   __TEXT.__ustring: 0xc8bd8
   __TEXT.__oslogstring: 0xb19
-  __TEXT.__unwind_info: 0x2a30
+  __TEXT.__unwind_info: 0x2a50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x24a0
-  __DATA_CONST.__objc_classlist: 0x5c8
+  __DATA_CONST.__const: 0x24c8
+  __DATA_CONST.__objc_classlist: 0x5d0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x56e0
+  __DATA_CONST.__objc_selrefs: 0x5720
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x408
-  __DATA_CONST.__objc_arraydata: 0x101a60
+  __DATA_CONST.__objc_superrefs: 0x410
+  __DATA_CONST.__objc_arraydata: 0x101a90
   __DATA_CONST.__got: 0x620
-  __AUTH_CONST.__const: 0xda0
-  __AUTH_CONST.__cfstring: 0x255de0
-  __AUTH_CONST.__objc_const: 0x11dd0
+  __AUTH_CONST.__const: 0xdc0
+  __AUTH_CONST.__cfstring: 0x255e20
+  __AUTH_CONST.__objc_const: 0x11f20
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x5070
+  __AUTH_CONST.__objc_arrayobj: 0x50a0
   __AUTH_CONST.__objc_dictobj: 0xf1b8
   __AUTH_CONST.__objc_intobj: 0xd50
   __AUTH_CONST.__objc_doubleobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH.__objc_data: 0x26c0
-  __DATA.__objc_ivar: 0xb80
+  __AUTH_CONST.__auth_got: 0x800
+  __AUTH.__objc_data: 0x2710
+  __DATA.__objc_ivar: 0xb90
   __DATA.__data: 0xcf0
   __DATA_DIRTY.__objc_data: 0x1310
   __DATA_DIRTY.__bss: 0x2c0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4023
-  Symbols:   7691
-  CStrings:  76813
+  Functions: 4037
+  Symbols:   7720
+  CStrings:  76816
 
Symbols:
+ -[TISupportedEnabledInputModesCache .cxx_destruct]
+ -[TISupportedEnabledInputModesCache cachedEnabledInputModes]
+ -[TISupportedEnabledInputModesCache cachedSupportedEnabledInputModes]
+ -[TISupportedEnabledInputModesCache cachedSupportedInputModes]
+ -[TISupportedEnabledInputModesCache init]
+ -[TISupportedEnabledInputModesCache setCachedEnabledInputModes:]
+ -[TISupportedEnabledInputModesCache setCachedSupportedEnabledInputModes:]
+ -[TISupportedEnabledInputModesCache setCachedSupportedInputModes:]
+ -[TISupportedEnabledInputModesCache setSupportedEnabledInputModes:forEnabledInputModes:supportedInputModes:]
+ -[TISupportedEnabledInputModesCache supportedEnabledInputModesForEnabledInputModes:supportedInputModes:]
+ _OBJC_CLASS_$_TISupportedEnabledInputModesCache
+ _OBJC_IVAR_$_TISupportedEnabledInputModesCache._cachedEnabledInputModes
+ _OBJC_IVAR_$_TISupportedEnabledInputModesCache._cachedSupportedEnabledInputModes
+ _OBJC_IVAR_$_TISupportedEnabledInputModesCache._cachedSupportedInputModes
+ _OBJC_IVAR_$_TISupportedEnabledInputModesCache._queue
+ _OBJC_METACLASS_$_TISupportedEnabledInputModesCache
+ _SupportedEnabledInputModes.cache
+ _SupportedEnabledInputModes.onceToken
+ _SupportedInputModes
+ __OBJC_$_INSTANCE_METHODS_TISupportedEnabledInputModesCache
+ __OBJC_$_INSTANCE_VARIABLES_TISupportedEnabledInputModesCache
+ __OBJC_$_PROP_LIST_TISupportedEnabledInputModesCache
+ __OBJC_CLASS_RO_$_TISupportedEnabledInputModesCache
+ __OBJC_METACLASS_RO_$_TISupportedEnabledInputModesCache
+ ___104-[TISupportedEnabledInputModesCache supportedEnabledInputModesForEnabledInputModes:supportedInputModes:]_block_invoke
+ ___108-[TISupportedEnabledInputModesCache setSupportedEnabledInputModes:forEnabledInputModes:supportedInputModes:]_block_invoke
+ ___SupportedEnabledInputModes_block_invoke
+ ___block_descriptor_64_8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ _dispatch_barrier_sync
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.3.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "QWERTY-Lithuanian"
+ "com.apple.TextInput.SupportedEnabledInputModes"
+ "com.apple.assistant.public"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
```
