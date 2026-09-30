## FrontBoardServices

> `/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA.__data`

```diff

-1149.0.0.0.0
+1150.0.0.0.0
   __TEXT.__text: 0x987d4
-  __TEXT.__delay_helper: 0xdc
+  __TEXT.__lazy_helpers: 0x54
   __TEXT.__objc_methlist: 0x8638
   __TEXT.__const: 0x270
-  __TEXT.__cstring: 0xc0cb
+  __TEXT.__cstring: 0xc079
   __TEXT.__oslogstring: 0x3b78
   __TEXT.__gcc_except_tab: 0x1e30
   __TEXT.__unwind_info: 0x2ac8

   __AUTH_CONST.__const: 0x840
   __AUTH_CONST.__cfstring: 0xa280
   __AUTH_CONST.__objc_const: 0x100b8
+  __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x870
-  __AUTH.__objc_data: 0xe10
+  __AUTH_CONST.__auth_got: 0x878
+  __AUTH.__objc_data: 0xdc0
   __DATA.__objc_ivar: 0xa58
   __DATA.__data: 0x1a14
   __DATA.__bss: 0x2f0
-  __DATA_DIRTY.__objc_data: 0x1f90
-  __DATA_DIRTY.__bss: 0x1d0
+  __DATA_DIRTY.__objc_data: 0x1fe0
+  __DATA_DIRTY.__bss: 0x1c8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BoardServices.framework/BoardServices
-  - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 4371
-  Symbols:   7892
-  CStrings:  1936
+  Symbols:   7893
+  CStrings:  1935
 
Symbols:
+ _OBJC_CLASS_$_AITransactionLog$lazyGOT
+ _OBJC_CLASS_$_AITransactionLog$lazyGOT$loadHelper_x8
+ __dyld_lazy_load
+ _lazyLoadFlag$MobileInstallation
- _OBJC_CLASS_$_AITransactionLog$loadHelper_x8
- _dlopenHelper$MobileInstallation
- _dlopenHelperFlag$MobileInstallation
CStrings:
- "/System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation"
```
