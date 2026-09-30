## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-605.1.18.0.0
-  __TEXT.__text: 0xbb68c
+605.1.19.101.0
+  __TEXT.__text: 0xbc18c
   __TEXT.__auth_stubs: 0x1660
-  __TEXT.__objc_methlist: 0x8be0
-  __TEXT.__const: 0x2038
+  __TEXT.__objc_methlist: 0x8bf8
+  __TEXT.__const: 0x2350
   __TEXT.__cstring: 0xa718
-  __TEXT.__oslogstring: 0x9c9f
+  __TEXT.__oslogstring: 0x9d1f
   __TEXT.__gcc_except_tab: 0x1be4
   __TEXT.__constg_swiftt: 0x8b4
   __TEXT.__swift5_typeref: 0xba4

   __TEXT.__swift_as_ret: 0x64
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x2e88
-  __TEXT.__eh_frame: 0x1628
+  __TEXT.__unwind_info: 0x2e90
+  __TEXT.__eh_frame: 0x1630
   __TEXT.__objc_classname: 0x18d3
-  __TEXT.__objc_methname: 0x16fee
+  __TEXT.__objc_methname: 0x1706e
   __TEXT.__objc_methtype: 0x24f8
-  __TEXT.__objc_stubs: 0xd640
+  __TEXT.__objc_stubs: 0xd680
   __DATA_CONST.__got: 0xbc8
   __DATA_CONST.__const: 0x1b68
   __DATA_CONST.__objc_classlist: 0x610
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4bc0
+  __DATA_CONST.__objc_selrefs: 0x4bd0
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb40
   __AUTH_CONST.__const: 0x1ce0
   __AUTH_CONST.__cfstring: 0x8ce0
-  __AUTH_CONST.__objc_const: 0x10648
+  __AUTH_CONST.__objc_const: 0x10678
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x30c8
   __AUTH.__data: 0x340
-  __DATA.__objc_ivar: 0x620
-  __DATA.__data: 0x1b98
+  __DATA.__objc_ivar: 0x624
+  __DATA.__data: 0x1ba8
   __DATA.__bss: 0x3560
   __DATA.__common: 0x68
   __DATA_DIRTY.__objc_data: 0x1418
-  __DATA_DIRTY.__data: 0x50
+  __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ACEB7654-0D3E-3A6F-B271-8D0DBA9C504A
-  Functions: 4595
-  Symbols:   11914
-  CStrings:  7019
+  UUID: 8DF754D4-C736-38B0-BF66-F01A89D0ED21
+  Functions: 4597
+  Symbols:   11923
+  CStrings:  7025
 
Symbols:
+ -[STAltDistroAppRequestData requestToRetryOnFailure]
+ -[STAltDistroAppRequestData setRequestToRetryOnFailure:]
+ _OBJC_IVAR_$_STAltDistroAppRequestData._requestToRetryOnFailure
+ ___45-[STAltDistroAppInfoLoader _startNextRequest]_block_invoke.cold.1
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ _objc_msgSend$requestToRetryOnFailure
+ _objc_msgSend$setRequestToRetryOnFailure:
- ___swift_instantiateConcreteTypeFromMangledName
- ___swift_instantiateConcreteTypeFromMangledNameAbstract
CStrings:
+ "Loading alt distro app info for %@"
+ "Loading info for budleId:%@ distributorId:%@ failed. Retrying with nil distributor id."
+ "T@\"ASCLockupRequest\",C,N,V_requestToRetryOnFailure"
+ "_requestToRetryOnFailure"
+ "requestToRetryOnFailure"
+ "setRequestToRetryOnFailure:"

```
