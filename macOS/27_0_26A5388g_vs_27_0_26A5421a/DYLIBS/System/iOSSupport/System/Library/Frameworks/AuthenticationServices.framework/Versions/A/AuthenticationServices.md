## AuthenticationServices

> `/System/iOSSupport/System/Library/Frameworks/AuthenticationServices.framework/Versions/A/AuthenticationServices`

```diff

-625.1.24.11.2
-  __TEXT.__text: 0xf2704
-  __TEXT.__objc_methlist: 0x53d8
-  __TEXT.__const: 0x123a4
+625.1.29.11.25
+  __TEXT.__text: 0xf2480
+  __TEXT.__objc_methlist: 0x53f0
+  __TEXT.__const: 0x12394
   __TEXT.__gcc_except_tab: 0xf30
-  __TEXT.__cstring: 0x565b
-  __TEXT.__oslogstring: 0x22fb
+  __TEXT.__cstring: 0x566b
+  __TEXT.__oslogstring: 0x237b
   __TEXT.__dlopen_cstrs: 0x1a8
   __TEXT.__ustring: 0x3608
-  __TEXT.__swift5_typeref: 0x29aa
+  __TEXT.__swift5_typeref: 0x298a
   __TEXT.__constg_swiftt: 0x1da4
   __TEXT.__swift5_reflstr: 0x13cc
   __TEXT.__swift5_fieldmd: 0x268c

   __TEXT.__swift_as_ret: 0x228
   __TEXT.__swift_as_cont: 0x404
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__unwind_info: 0x49b0
-  __TEXT.__eh_frame: 0x5a4c
+  __TEXT.__unwind_info: 0x49c0
+  __TEXT.__eh_frame: 0x5a44
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a10
+  __DATA_CONST.__objc_selrefs: 0x2a28
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x250
   __DATA_CONST.__objc_arraydata: 0x170
-  __DATA_CONST.__got: 0xb00
+  __DATA_CONST.__got: 0xaf0
   __AUTH_CONST.__const: 0x81c0
   __AUTH_CONST.__cfstring: 0x2c60
-  __AUTH_CONST.__objc_const: 0xb970
+  __AUTH_CONST.__objc_const: 0xb990
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1390
+  __AUTH_CONST.__auth_got: 0x1358
   __AUTH.__objc_data: 0x2668
   __AUTH.__data: 0x13c0
-  __DATA.__objc_ivar: 0x558
-  __DATA.__data: 0x2ca0
+  __DATA.__objc_ivar: 0x55c
+  __DATA.__data: 0x2c80
   __DATA.__bss: 0x10d60
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x808

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6484
-  Symbols:   5822
-  CStrings:  847
+  Functions: 6488
+  Symbols:   5825
+  CStrings:  848
 
Symbols:
+ -[_ASPasswordManagerIconController resumeFetching]
+ -[_ASPasswordManagerIconController suspendFetching]
+ GCC_except_table62
+ OBJC_IVAR_$__ASPasswordManagerIconController._fetchingSuspended
+ __97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_2
+ ___50-[_ASPasswordManagerIconController resumeFetching]_block_invoke
+ ___51-[_ASPasswordManagerIconController suspendFetching]_block_invoke
+ _objc_msgSend$removeAllObjects
- GCC_except_table54
- __97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_3
- ___97-[_ASPasswordManagerIconController _requestTouchIconForDomain:options:requestID:responseHandler:]_block_invoke_3
- _symbolic Sny_____G 10Foundation4DateV
- _symbolic _____5lower_AA5uppert 10Foundation4DateV
CStrings:
+ "Allow “%@” to temporarily access verification codes?"
+ "Skipping touch icon fetch while suspended; domain=%{sensitive, mask.hash}@"
+ "Suspending icon fetching; cancelling %d in-flight request(s)"
+ "“%@” will be able to use one-time verification codes in %@ while it signs in to your accounts."
+ "“%@” will be able to use one-time verification codes while it signs in to your accounts."
- "Allow “%@” to temporarily access verification codes you receive?"
- "This will make one-time verification codes available to “%@” for up to %@."
- "This will make one-time verification codes received in %@ available to “%@” for up to %@."
- "\xf1"
```
