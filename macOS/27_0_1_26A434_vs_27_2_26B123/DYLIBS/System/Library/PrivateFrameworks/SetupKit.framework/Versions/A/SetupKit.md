## SetupKit

> `/System/Library/PrivateFrameworks/SetupKit.framework/Versions/A/SetupKit`

```diff

-900.58.0.0.0
-  __TEXT.__text: 0x26cd8
+910.31.0.0.0
+  __TEXT.__text: 0x26da4
   __TEXT.__objc_methlist: 0x21e0
   __TEXT.__const: 0x1d2
   __TEXT.__constg_swiftt: 0x28
   __TEXT.__swift5_typeref: 0x6
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__gcc_except_tab: 0xbf0
-  __TEXT.__cstring: 0x648b
+  __TEXT.__gcc_except_tab: 0xbfc
+  __TEXT.__cstring: 0x64e5
   __TEXT.__oslogstring: 0x113
-  __TEXT.__unwind_info: 0xa00
+  __TEXT.__unwind_info: 0xa08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__got: 0x190
-  __AUTH_CONST.__const: 0x10e8
+  __AUTH_CONST.__const: 0x1108
   __AUTH_CONST.__cfstring: 0xa20
   __AUTH_CONST.__objc_const: 0x48d8
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__data: 0x20
   __DATA.__objc_ivar: 0x460
-  __DATA.__data: 0xc30
   __DATA.__bss: 0x68
   __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__data: 0xc50
   - /System/Library/Frameworks/CoreBluetooth.framework/Versions/A/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 933
-  Symbols:   2064
-  CStrings:  779
+  Functions: 934
+  Symbols:   2065
+  CStrings:  781
 
Symbols:
+ GCC_except_table286
+ GCC_except_table292
+ GCC_except_table312
+ GCC_except_table314
+ GCC_except_table322
+ GCC_except_table328
+ GCC_except_table333
+ GCC_except_table346
+ GCC_except_table354
+ GCC_except_table383
+ GCC_except_table406
+ GCC_except_table412
+ GCC_except_table418
+ GCC_except_table528
+ GCC_except_table733
+ GCC_except_table740
+ GCC_except_table747
+ GCC_except_table750
+ GCC_except_table784
+ GCC_except_table790
+ GCC_except_table794
+ GCC_except_table857
+ _CNUserInteractionIsRequired
+ ___79-[SKSetupCaptiveNetworkJoinServer _captiveNetworkLoginRequest:responseHandler:]_block_invoke_2
- GCC_except_table285
- GCC_except_table291
- GCC_except_table311
- GCC_except_table313
- GCC_except_table321
- GCC_except_table327
- GCC_except_table332
- GCC_except_table345
- GCC_except_table353
- GCC_except_table382
- GCC_except_table405
- GCC_except_table411
- GCC_except_table417
- GCC_except_table527
- GCC_except_table732
- GCC_except_table739
- GCC_except_table746
- GCC_except_table749
- GCC_except_table783
- GCC_except_table789
- GCC_except_table793
- GCC_except_table856
- _objc_unsafeClaimAutoreleasedReturnValue
Functions:
~ -[SKSetupCaptiveNetworkJoinServer _captiveNetworkLoginRequest:responseHandler:] : 464 -> 620
+ ___79-[SKSetupCaptiveNetworkJoinServer _captiveNetworkLoginRequest:responseHandler:]_block_invoke
~ -[SKConnection _clientPairSetupContinueWithData:] : 928 -> 956
~ -[SKConnection _receivedHeader:encryptedObjectData:] : 672 -> 680
~ -[SKConnection _receivedHeader:unencryptedObjectData:] : 788 -> 796
CStrings:
+ "### CaptiveNetworkLogin failed: captive UI not required"
+ "CNUserInteractionIsRequired false"
```
