## LocationAuthorizationFramework

> `/System/Library/PrivateFrameworks/LocationAuthorizationFramework.framework/LocationAuthorizationFramework`

```diff

-3186.0.17.0.1
-  __TEXT.__text: 0x6572c
-  __TEXT.__objc_methlist: 0x1358
+3186.0.21.0.0
+  __TEXT.__text: 0x65d1c
+  __TEXT.__objc_methlist: 0x1380
   __TEXT.__const: 0x2ae8
   __TEXT.__cstring: 0x2b39
   __TEXT.__swift5_typeref: 0xb97
-  __TEXT.__oslogstring: 0x7432
+  __TEXT.__oslogstring: 0x76fa
   __TEXT.__constg_swiftt: 0xa60
   __TEXT.__swift5_reflstr: 0x645
   __TEXT.__swift5_fieldmd: 0x878

   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x94
   __TEXT.__gcc_except_tab: 0x1054
-  __TEXT.__unwind_info: 0x1ca8
-  __TEXT.__eh_frame: 0x16dc
+  __TEXT.__unwind_info: 0x1cc0
+  __TEXT.__eh_frame: 0x1708
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xef8
+  __DATA_CONST.__objc_selrefs: 0xf10
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0x370
-  __AUTH_CONST.__const: 0x1968
+  __AUTH_CONST.__const: 0x1988
   __AUTH_CONST.__cfstring: 0x1720
   __AUTH_CONST.__objc_const: 0x1c80
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0xd18
   __AUTH.__objc_data: 0x3b0
   __AUTH.__data: 0x170

   __DATA_DIRTY.__objc_data: 0x850
   __DATA_DIRTY.__data: 0xa78
   __DATA_DIRTY.__common: 0x40
-  __DATA_DIRTY.__bss: 0x800
+  __DATA_DIRTY.__bss: 0x810
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1926
+  Functions: 1931
   Symbols:   440
-  CStrings:  589
+  CStrings:  595
 
CStrings:
+ "#AuthorizationDatabase - denying unquarantining for known invalid identity"
+ "#Warning #ClientResolution the passed keyPath is quarantined. Resolving to #nullCKP"
+ "{\"msg%{public}.0s\":\"#AuthorizationDatabase #Quarantine marking client quarantined at migration\", \"client\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#AuthorizationDatabase -  unquarantining client\", \"client\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#AuthorizationDatabase - denying unquarantining for known invalid identity\", \"invalidIdentity\":%{public, location:escape_only}@}"
+ "{\"msg%{public}.0s\":\"#Warning #ClientResolution the passed keyPath is quarantined. Resolving to #nullCKP\", \"InputCKP\":%{public, location:escape_only}@}"
```
