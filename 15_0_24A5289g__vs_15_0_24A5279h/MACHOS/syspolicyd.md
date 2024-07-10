## syspolicyd

> `/usr/libexec/syspolicyd`

```diff

-620.0.16.0.0
-  __TEXT.__text: 0xaa420
+620.0.7.0.0
+  __TEXT.__text: 0xa938c
   __TEXT.__auth_stubs: 0x2970
-  __TEXT.__objc_stubs: 0x9060
+  __TEXT.__objc_stubs: 0x8f60
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x43c0
+  __TEXT.__objc_methlist: 0x4378
   __TEXT.__const: 0x1ccf
-  __TEXT.__objc_classname: 0x732
-  __TEXT.__objc_methtype: 0x1e23
-  __TEXT.__objc_methname: 0xb22d
-  __TEXT.__oslogstring: 0x8d28
-  __TEXT.__gcc_except_tab: 0x1a58
-  __TEXT.__cstring: 0x10c46
+  __TEXT.__objc_methname: 0xb17a
+  __TEXT.__oslogstring: 0x8c78
+  __TEXT.__objc_classname: 0x72b
+  __TEXT.__objc_methtype: 0x1e18
+  __TEXT.__gcc_except_tab: 0x1a14
+  __TEXT.__cstring: 0x10ada
   __TEXT.__swift5_typeref: 0x384
   __TEXT.__swift5_capture: 0x134
-  __TEXT.__swift5_reflstr: 0x20d
+  __TEXT.__swift5_reflstr: 0x1ed
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__constg_swiftt: 0x3a0
-  __TEXT.__swift5_fieldmd: 0x25c
+  __TEXT.__swift5_fieldmd: 0x250
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x30
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__info_plist: 0x3ba
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x2200
+  __TEXT.__unwind_info: 0x21d8
   __TEXT.__eh_frame: 0x218
   __DATA_CONST.__auth_got: 0x14d0
-  __DATA_CONST.__got: 0x7f0
-  __DATA_CONST.__auth_ptr: 0x1c0
-  __DATA_CONST.__const: 0x3c38
-  __DATA_CONST.__cfstring: 0x7620
+  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__auth_ptr: 0x1b8
+  __DATA_CONST.__const: 0x3c30
+  __DATA_CONST.__cfstring: 0x7540
   __DATA_CONST.__objc_classlist: 0x2f0
-  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x30

   __DATA_CONST.__objc_arraydata: 0x510
   __DATA_CONST.__objc_arrayobj: 0x228
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x9f58
-  __DATA.__objc_selrefs: 0x2968
+  __DATA.__objc_const: 0x9ef8
+  __DATA.__objc_selrefs: 0x2930
   __DATA.__objc_ivar: 0x774
   __DATA.__objc_data: 0x1fe8
-  __DATA.__data: 0xc52
+  __DATA.__data: 0xc42
   __DATA.__bss: 0xabd
   __DATA.__common: 0x3b8
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3238
-  Symbols:   988
-  CStrings:  1997
+  Functions: 3223
+  Symbols:   986
+  CStrings:  1987
 
Symbols:
- _NSURLIsSystemImmutableKey
- _NSURLIsUserImmutableKey
CStrings:
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
+ "/AppleInternal/Library/BuildRoots/7abfe40b-2884-11ef-836f-e2437461156c/Library/Caches/com.apple.xbs/Sources/file/file/src/softmagic.c"
+ "/var/db/gke.bundle"
+ "DELETE FROM staged_samples WHERE pk = $1"
+ "INSERT INTO staged_samples (pk, url, type) VALUES (?1, ?2, ?3)"
+ "SELECT pk, url, type from staged_samples"
- "-[ExecManagerService allowGatekeeperPolicy:withReply:]"
- "/AppleInternal/Library/BuildRoots/c496718d-33c1-11ef-b26f-e2437461156c/Library/Caches/com.apple.xbs/Sources/file/file/src/softmagic.c"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/ACMLib/ACMLib.c"
- "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/AppleCredentialManager_ClientLibs/common/LibCall.c"
- "/var/db/SystemPolicyConfiguration/gke/gke.bundle"
- "8"
- "CREATE TABLE staged_samples (  uuid TEXT,  url TEXT NOT NULL,  type INTEGER,  PRIMARY KEY (url))"
- "DELETE FROM staged_samples WHERE url = $1"
- "DROP TABLE IF EXISTS staged_samples"
- "GKPromptErrorDomain"
- "INSERT INTO staged_samples (uuid, url, type) VALUES (?1, ?2, ?3)"
- "SELECT uuid, url, type from staged_samples"
- "disable"
- "enable"
- "lastGKAllowAnywhere"
- "ui-disable-local"
- "ui-enable-local"

```
