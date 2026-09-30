## transparencyd

> `/usr/libexec/transparencyd`

```diff

-1218.100.244.0.0
-  __TEXT.__text: 0x291700
+1218.120.13.0.1
+  __TEXT.__text: 0x292574
   __TEXT.__auth_stubs: 0x2ce0
-  __TEXT.__objc_stubs: 0x1b780
-  __TEXT.__objc_methlist: 0x149b0
+  __TEXT.__objc_stubs: 0x1b800
+  __TEXT.__objc_methlist: 0x149e0
   __TEXT.__cstring: 0x11fa2
   __TEXT.__objc_classname: 0x2c24
-  __TEXT.__objc_methname: 0x21a56
-  __TEXT.__objc_methtype: 0x710b
+  __TEXT.__objc_methname: 0x21aab
+  __TEXT.__objc_methtype: 0x714b
   __TEXT.__const: 0xa1f8
-  __TEXT.__gcc_except_tab: 0x4d90
-  __TEXT.__oslogstring: 0x109de
+  __TEXT.__gcc_except_tab: 0x4d78
+  __TEXT.__oslogstring: 0x10bda
   __TEXT.__swift5_typeref: 0x2378
   __TEXT.__swift5_reflstr: 0x16ba
   __TEXT.__swift5_assocty: 0x480

   __TEXT.__swift_as_entry: 0x110
   __TEXT.__swift_as_ret: 0xb8
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0xa118
+  __TEXT.__unwind_info: 0xa148
   __TEXT.__eh_frame: 0x4d88
   __DATA_CONST.__auth_got: 0x1680
   __DATA_CONST.__got: 0xe80
-  __DATA_CONST.__auth_ptr: 0x610
-  __DATA_CONST.__const: 0x15810
+  __DATA_CONST.__auth_ptr: 0x5d8
+  __DATA_CONST.__const: 0x159a0
   __DATA_CONST.__cfstring: 0xdc00
   __DATA_CONST.__objc_classlist: 0xc90
   __DATA_CONST.__objc_catlist: 0x48

   __DATA_CONST.__objc_arraydata: 0x1a8
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_arrayobj: 0x1e0
-  __DATA.__objc_const: 0x2da98
-  __DATA.__objc_selrefs: 0x81c0
-  __DATA.__objc_ivar: 0x107c
+  __DATA.__objc_const: 0x2da78
+  __DATA.__objc_selrefs: 0x81e8
+  __DATA.__objc_ivar: 0x1078
   __DATA.__objc_data: 0x9000
   __DATA.__data: 0xa530
   __DATA.__thread_vars: 0x48
   __DATA.__thread_bss: 0xc
-  __DATA.__bss: 0x11498
+  __DATA.__bss: 0x114a8
   __DATA.__common: 0x6f0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 15931
+  Functions: 15955
   Symbols:   1349
-  CStrings:  11397
+  CStrings:  11412
 
CStrings:
+ "/\x0f\x0f\t"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
+ "/AppleInternal/Library/BuildRoots/fa4539c7-059d-11f0-b0c1-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "Error: getCurrentRegistrationState not supported"
+ "IDS returned in-process registration"
+ "IDS returned no registration states for service %@"
+ "IDS returned state incorrect account key"
+ "IDS returned state with incorrect signature"
+ "IDS returned state with missing account key"
+ "IDS returned state with no KT data"
+ "IDS returned unregistered states with recent HSA2 upsell"
+ "IDS returned valid registration, type %d"
+ "No valid AppleID registration, so we are not in a good state"
+ "Skipping registration for non-apple ID. Type %d"
+ "deviceSignature"
+ "getCurrentRegistrationState:withCompletion:"
+ "hasUpdatedRegistrationChecks"
+ "ktAccountKey"
+ "legacyPokeAndUpdateIDSStateWithPublicKey:items:"
+ "pokeAndUpdateIDSState:withPublicKey:"
+ "registrationType"
+ "v32@0:8@\"IDSRegistrationStateRequest\"16@?<v@?@\"NSDictionary\">24"
- "/\x0f\x0f\n"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/aeskeywrap.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/platform/platform_lib.c"
- "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
- "T@\"KTNearFutureScheduler\",&,V_checkIDSRegistration"
- "_checkIDSRegistration"
- "setCheckIDSRegistration:"

```
