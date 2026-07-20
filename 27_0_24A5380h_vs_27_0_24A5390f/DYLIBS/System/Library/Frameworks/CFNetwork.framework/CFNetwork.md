## CFNetwork

> `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`

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
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__lazy_load_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__AUTH.__cfstring_CFN`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-3890.100.1.0.0
-  __TEXT.__text: 0x25639c
+3892.100.1.0.0
+  __TEXT.__text: 0x2563ec
   __TEXT.__lazy_helpers: 0x2808
   __TEXT.__objc_methlist: 0x9c74
   __TEXT.__const: 0xc9c1c

   __DATA.__objc_ivar: 0x1360
   __DATA.__data: 0xe1c
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xd70
+  __DATA.__bss: 0xd50
   __DATA_DIRTY.__objc_data: 0x1900
   __DATA_DIRTY.__data: 0x1b8
-  __DATA_DIRTY.__bss: 0x9a8
+  __DATA_DIRTY.__bss: 0x9d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
Functions:
~ __ZN19URLConnectionLoader29ensureLoaderHasProtocolNoLockEP12NSURLRequest : 1088 -> 1104
~ __ZN19URLConnectionLoader20scheduleTimeoutTimerEv : 188 -> 200
~ __ZN27URLConnectionLoader_ClassicC1EP26InterfaceRequiredForLoaderRKN19URLConnectionLoader11ConfigFlagsEP19__NSURLSessionLocalPv : 396 -> 400
~ __ZN19URLConnectionLoader15touchConnectionEv : 464 -> 480
~ ____ZN19URLConnectionLoader15invalidateAsyncENSt3__110shared_ptrI23CoreSchedulingSetOneOffEE_block_invoke : 536 -> 552
~ __ZN19URLConnectionLoader41protocolDidReceiveAuthenticationChallengeEP19_CFURLAuthChallenge : 960 -> 976
```
