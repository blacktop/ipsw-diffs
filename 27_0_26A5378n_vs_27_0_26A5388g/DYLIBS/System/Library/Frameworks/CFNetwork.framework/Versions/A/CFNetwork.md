## CFNetwork

> `/System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__dof_CFNetwork`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__cfstring_CFN`
- `__DATA_DIRTY.__objc_data`

```diff

-3890.100.1.0.0
-  __TEXT.__text: 0x25b12c
+3892.100.1.0.0
+  __TEXT.__text: 0x25b17c
   __TEXT.__lazy_helpers: 0x21cc
   __TEXT.__objc_methlist: 0x9cac
   __TEXT.__const: 0xc9c2c

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0xa88
+  __DATA_CONST.__got: 0xaf0
   __AUTH_CONST.__const: 0x17760
   __AUTH_CONST.__cfstring: 0xeb80
   __AUTH_CONST.__objc_const: 0x13f38

   __AUTH.__data: 0x3e8
   __AUTH.__cfstring_CFN: 0x7cb0
   __DATA.__objc_ivar: 0x136c
-  __DATA.__data: 0xe08
+  __DATA.__data: 0xe04
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xd68
+  __DATA.__bss: 0xd40
   __DATA_DIRTY.__objc_data: 0x1900
-  __DATA_DIRTY.__data: 0x1a8
-  __DATA_DIRTY.__bss: 0x9a0
+  __DATA_DIRTY.__data: 0x1ac
+  __DATA_DIRTY.__bss: 0x9c8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
Functions:
~ __ZN19URLConnectionLoader41protocolDidReceiveAuthenticationChallengeEP19_CFURLAuthChallenge : 876 -> 892
~ __ZN19URLConnectionLoader15touchConnectionEv : 464 -> 480
~ ____ZN19URLConnectionLoader15invalidateAsyncENSt3__110shared_ptrI23CoreSchedulingSetOneOffEE_block_invoke : 536 -> 552
~ __ZN19URLConnectionLoader29ensureLoaderHasProtocolNoLockEP12NSURLRequest : 1088 -> 1104
~ __ZN19URLConnectionLoader20scheduleTimeoutTimerEv : 188 -> 200
~ __ZN27URLConnectionLoader_ClassicC1EP26InterfaceRequiredForLoaderRKN19URLConnectionLoader11ConfigFlagsEP19__NSURLSessionLocalPv : 400 -> 404
```
