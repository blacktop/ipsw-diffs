## secd

> `/usr/libexec/secd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__cstring`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__bss`

```diff

-62460.0.38.0.1
-  __TEXT.__text: 0x28a2d8
+62460.0.55.0.1
+  __TEXT.__text: 0x28a3cc
   __TEXT.__auth_stubs: 0x40e0
-  __TEXT.__objc_stubs: 0x1d7c0
+  __TEXT.__objc_stubs: 0x1d7e0
   __TEXT.__objc_methlist: 0x15e50
   __TEXT.__const: 0x920
   __TEXT.__objc_classname: 0x24f5
-  __TEXT.__objc_methname: 0x2e46a
+  __TEXT.__objc_methname: 0x2e47a
   __TEXT.__objc_methtype: 0xafe1
   __TEXT.__constg_swiftt: 0x274
   __TEXT.__swift5_typeref: 0x35e

   __DATA_CONST.__got: 0x1460
   __DATA_CONST.__auth_ptr: 0x1d8
   __DATA.__objc_const: 0x23c38
-  __DATA.__objc_selrefs: 0x9808
+  __DATA.__objc_selrefs: 0x9810
   __DATA.__objc_ivar: 0x1ae8
   __DATA.__objc_data: 0x5d48
   __DATA.__data: 0x3098

   - /usr/lib/swift/libswiftos.dylib
   Functions: 10030
   Symbols:   1843
-  CStrings:  16249
+  CStrings:  16250
 
Symbols:
+ _kSecurityRTCEventNameJoinButDistrustEveryone
- _kSecurityRTCFieldDistrustEveryoneOnJoin
Functions:
~ sub_10017e440 : 1020 -> 1164
~ sub_100227284 -> sub_100227314 : 1092 -> 1104
~ sub_100280420 -> sub_1002804bc : 1576 -> 1588
~ sub_100280c88 -> sub_100280d30 : 124 -> 200
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.j7jzB6/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "setPreventCylonUsage:"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wifYPg/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
```
